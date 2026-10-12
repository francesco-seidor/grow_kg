---
id: 02-business-partner-and-product-master-data/test-script-central-governance-for-business-partner-1n7-sap-s-4hana-cl
title: "Test Script: Central Governance for Business Partner (1N7) - SAP S/4HANA Cloud Public Edition (1N7_S4CLD2608_BPD_EN_XX)"
description: "SAP test script for scope item 1N7: mass and single-record business partner governance, approval workflow and inbound replication in S/4HANA Cloud."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/central-governance-products-business-partners]
aliases: [1N7_S4CLD2608_BPD_EN_XX]
keywords: [Central Governance for Products and Business Partners, central governance, business partner mass processing, mass processing automation, business partner creation, business partner changes, governance process approval, governance process rejection, governance process revision, inbound processes]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1N7_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-745
topic: 02-business-partner-and-product-master-data/central-governance-products-business-partners
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Central Governance for Business Partner (1N7) - SAP S/4HANA Cloud Public Edition (1N7_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1N7_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Central Governance for Products and Business Partners** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Central Governance for Business Partner (1N7) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232847792)

[2 Prerequisites 4](#_Toc232847793)

[2.1 System Access 4](#_Toc232847794)

[2.2 Roles 4](#_Toc232847795)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232847796)

[3 Overview Table 6](#_Toc232847797)

[4 Test Procedures 8](#_Toc232847798)

[4.1 Manage Governance Processes Business Partners 8](#_Toc232847799)

[4.1.1 Create Process 8](#_Toc232847800)

[4.1.2 Editing 9](#_Toc232847801)

[4.1.3 Remove Unchanged Data 10](#_Toc232847802)

[4.1.4 Validation 10](#_Toc232847803)

[4.1.5 Activation 11](#_Toc232847804)

[4.1.6 Track Mass Changes 12](#_Toc232847805)

[4.2 Manage Governance Processes with Automation 13](#_Toc232847806)

[4.2.1 Check Derivation Step in Process UI 13](#_Toc232847807)

[4.3 Manage Business Partners Central Governance 14](#_Toc232847808)

[4.3.1 Create New Business Partner Using Governance Process 14](#_Toc232847809)

[4.3.2 Submit Governance Process 16](#_Toc232847810)

[4.3.3 [Optional] Validate and Approve Governance Process 16](#_Toc232847811)

[4.3.4 [Optional] Reject Governance Process 18](#_Toc232847812)

[4.3.5 [Optional] Send Governance Process for Revision 18](#_Toc232847813)

[4.4 Manage Business Partners Central Governance 19](#_Toc232847814)

[4.4.1 Change Active Business Partner Using Governance Process 19](#_Toc232847815)

[4.4.2 Submit Governance Process 21](#_Toc232847816)

[4.4.3 [Optional] Validate and Approve Governance Process 22](#_Toc232847817)

[4.5 Manage Inbound Processes 23](#_Toc232847818)

## Purpose

Overview

This scope item provides comprehensive capabilities for managing business partner data within the SAP S/4HANA Cloud Public Edition system. It supports both single and mass processing scenarios. Users can create new Business Partners or modify existing ones individually using the Manage Business Partners Central Governance app. For broader updates, the Manage Governance Processes Central Governance app enables mass processing, allowing changes to be applied across multiple Business Partners. Additionally, automated mass processing includes a derivation step that streamlines governance workflows. The scope item also facilitates inbound processing by enabling the system to integrate replicated Business Partner data and relationships through SOAP-based services.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible via SAP Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

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

Use your own master data to go through the test procedure.

## Overview Table

This scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 1: Manage Governance Processes Business Partners

| Choose the appropriate entity: Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Process](#unique_7) [page ] 8 | Master Data Specialist - Business Partner Data | SAP Fiori: Start Mass Processing (Business Partners) | Process can be created with records that can be changed. |
| [Editing](#unique_8) [page ] 9 | Master Data Specialist - Business Partner Data | SAP Fiori: Start Mass Processing (Business Partners) | Changes have been applied and are ready for validation. |
| [Remove Unchanged Data](#unique_9) [page ] 10 | Master Data Specialist - Business Partner Data | SAP Fiori: Start Mass Processing (Business Partners) | Unchanged records are removed from the process. |
| [Validation](#unique_10) [page ] 10 | Master Data Specialist - Business Partner Data | SAP Fiori: Start Mass Processing (Business Partners) | Check the result to determine whether records can be activated in the system (based on system customizing) |
| [Activation](#unique_11) [page ] 11 | Master Data Specialist - Business Partner Data | SAP Fiori: Start Mass Processing (Business Partners) | Success message tells that master data has been updated |
| [Track Mass Changes](#unique_12) [page ] 12 | Master Data Specialist - Business Partner Data | SAP Fiori: Track Mass Changes (Business Partners) | Track your changes made during the Mass Processing Process. |

Table 2: Manage Governance Processes with Automation Business Partners

|  |  |  |  |
| --- | --- | --- | --- |
| Choose the appropriate entity: Process Step, Report, or Item | Business Role | App/Transaction | Expected Results |
| [Check Derivation Step in Process UI](#unique_13) [page ] 13 | Master Data Specialist - Business Partner Data | SAP Fiori: Manage Mass Processes – Business Partners | Process with the Derivation step îs automatically when the related data is processed. |

Table 3: Manage Business Partners Central Governance – Create Business Partner

|  |  |  |  |
| --- | --- | --- | --- |
| Choose the appropriate entity: Process Step, Report, or Item | Business Role | App/Transaction | Expected Results |
| [Create New Business Partner Using Governance Process](#unique_14) [page ] 14 | Master Data Specialist - Business Partner Data for Business Partner Data | SAP Fiori: Manage Business Partners Central Governance | Process can be created and business partner data can be entered. |
| [Submit Governance Process](#unique_15) [page ] 16 | Master Data Specialist - Business Partner Data for Business Partner Data | SAP Fiori: Manage Business Partners Central Governance | Process can be submitted for Approval. |
| [[Optional] Validate and Approve Governance Process](#unique_16) [page ] 16 | Master Data Specialist - Business Partner Data for Business Partner Data | SAP Fiori: Manage Business Partners Central Governance | Process can be validated and approved. |

Table 4: Manage Business Partners Central Governance – Change Business Partner

|  |  |  |  |
| --- | --- | --- | --- |
| Choose the appropriate entity: Process Step, Report, or Item | Business Role | App/Transaction | Expected Results |
| [Change Active Business Partner Using Governance Process](#unique_17) [page ] 19 | Master Data Specialist - Business Partner Data for Business Partner Data | SAP Fiori: Manage Business Partners Central Governance | Process can be created and business partner data can be entered. |
| [Submit Governance Process](#unique_18) [page ] 21 | Master Data Specialist - Business Partner Data for Business Partner Data | SAP Fiori: Manage Business Partners Central Governance | Process can be submitted for Approval. |
| [[Optional] Validate and Approve Governance Process](#unique_19) [page ] 22 | Master Data Specialist - Business Partner Data for Business Partner Data | SAP Fiori: Manage Business Partners Central Governance | Process can be validated and approved. |

Table 5: Manage Business Partners Central Governance – Manage Inbound Processes

|  |  |  |  |
| --- | --- | --- | --- |
| Choose the appropriate entity: Process Step, Report, or Item | Business Role | App/Transaction | Expected Results |
| [Manage Inbound Processes](#unique_20) [page ] 23 | Master Data Specialist - Business Partner Data for Business Partner Data | SAP Fiori: Manage Inbound Processes | Business partner data and relationships can be replicated via Inbound Processes. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Manage Governance Processes Business Partners

#### Create Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Scope definition is the first step in mass processing to select the Business Partners that should be changed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad opens. |  |
| 2 | Access App | Open Manage Governance Processes (F6558A) | The Manage Governance Processes (F6558A) app opens. |  |
| 3 | Create Process | Choose Create and enter a description. Choose your process template or use the default template SAP: Mass Processing BP.Choose start process with Selection.Under Selection, enter the business partner number.Choose Check Selection and verify the number of records selected for mass processing.Choose Start. | System saves the data and creates a mass process.The Edit step will be highlighted in green. The KPI will be identified as unchanged records for all the tables |  |

#### Editing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step provides the list of potential records to be changed and the user can define the new field values.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select table for the changes | Select the relevant table in the tab bar. | The current values of the record in this table are shown. |  |
| 2 | Select records for mass change | Select the records that you want to edit.Choose Mass Edit, then choose Selected Items. | Records are selected and the Mass Edit dialog box opens. |  |
| 3 | Mass Change of values | For each field, you can choose to enter a new value, keep the same value, or clear the values.Use Enter New Value and enter new values.Choose Save. | The new field values are applied. The Details column shows the number of completed changes as a link.Opening the link displays the old and new value for the field. |  |
| 4 | Single changes of values | To edit a single record, choose Edit the header and type in directly the new field values individually for each field.Choose Save. | The new field values are applied immediately.The Details column shows the number of completed changes as a link.Opening the link displays the old and new value for the field. |  |
| 5 | Check the number of changes | Choose Back, the system verifies the number of changed rows. | The bar chart in the results section shows the number of changed rows. |  |

#### Remove Unchanged Data

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
| 1 | Start Remove Unchanged Data | Press Continue (on the bottom of the screen) to start the step Remove Unchanged Data. | Unchanged records are removed from the process. Only the changed records will be processed further. |  |

#### Validation

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
| 1 | Verify Validation | Validation step will be executed since there is no check point between Remove Unchanged Data and Validation step. | System starts the validation. |  |
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

The activation step triggers the activation of the data into the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Start Activation | Press Continue (on the bottom of the screen) to start the activation. | The system starts the activation and shows a result screen when finished. |  |
| 2 | Check Errors and Warnings (optional) | When warnings or errors occurred, the system provides this information. Click on the numbers “Errors” and “Warnings” to show details. | Message texts are shown. |  |

#### Track Mass Changes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Track your changes made during the Mass Processing process. You can view the list of changes only if you have made any changes during the Mass Processing process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access App | Go back to the home page of the SAP Fiori launchpad. Open Track Mass Changes (Business Partners). | The Track Mass Changes (Business Partners) screen displays. |  |
| 2 | Filter Inputs | Give in the process ID that you noted down in [Activation](#unique_11) [page ] 11 step 4. Choose Go. | You should be able to see the list of changes made by you during the Mass Processing Process. If no changes are available, then you made no changes during the Mass Processing process. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist for Business Partner Data. | The SAP Fiori launchpad opens. |  |
| 2 | Access App | Open Manage Governance Processes (F6558A) | The Manage Governance Processes (F6558A) app opens. |  |
| 3 | Create Process | Create a New Process, enter a description, and select a process template for automation, for example, SAP: Mass Processing BP Automated. Choose Save. | The system saves the data and creates a mass process. |  |
| 4 | Check | The process UI includes the following steps:EditDerivationRemove Unchanged DataValidationActivation | The Derivation step is included in the process UI. |  |

### Manage Business Partners Central Governance

#### Create New Business Partner Using Governance Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

As a requester you can create a new governance process to create a new business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist for Business Partner Data. | The SAP Fiori launchpad opens. |  |
| 2 | Access App | Open Manage Business Partners (F7204A) | The Manage Business Partners (F7204A) app opens. |  |
| 3 | Create Single Processing for Business Partner | Choose Create, then choose Organization.Enter the general data, if you choose External Alpha - Numeric Numbering (BPAB) as Grouping, enter a Business Partner ID within the interval 'A' - 'ZZZZZZZZZZ.Enter the General Address and Standard Address.Choose OK. | The organization details view opens.The process template SAP: Single Processing BP is filled in. The data that you entered in the Quick Create dialog box is visible in the overview page. |  |
| 4 | Enter Process Information | Choose Create New Process.Enter a description for the process.Choose the Due Date. | The process information is filled in. |  |
| 5 | Enter General In-formation | Enter further general information data: for example, Search Terms, Legal Form, Foundation Date, and Liquidation Data. Choose Show More to display additional fields. | The general information is filled in. |  |
| 6 | Enter Standard Communication Data | In the Overview view, under Standard Communication enter Telephone, Cell Phone, Fax, and e-mail.Select the preferred communication method. | The communication data is filled in. |  |
| 7 | Validate Standard Address | In the Address Details table, choose Validate for the address that you want to use.Go through the steps in the Validate Address dialog box to correct the address data. You may need to correct some of the values manually in the selected address. Confirm the validated address. | The selected address is now complete and the validation status is set to Validated. |  |
| 8 | Add Roles | In the Roles table, choose Create and add the business partner roles. | The selected roles are added in the Roles table. |  |
| 9 | Enter Bank Accounts | in the Bank Accounts table, choose Create and enter the full bank account details.You can use the Propose IBAN to generate an IBAN from the bank details or Propose Bank Details to generate bank details from the IBAN.Choose Apply.Add a secondary Bank Account if needed. | The Bank Account is listed in the Bank Accounts table.The IBAN and bank details can be generated. |  |
| 10 | Add Tax Numbers | In the Tax Numbers table, choose Create.Select a tax category and create three different tax entries. | The tax numbers are listed in the Tax Numbers table. |  |
| 11 | Add Identification Numbers | In the Identification Numbers table, choose Create.Select the ID type and create three different identification numbers. | The Identification Numbers are listed in the Identification Numbers table. The Valid From and Valid To fields are defaulted with today’s date and 12/31/9999 respectively. |  |
| 12 | Add Industries | In the Industries table, choose Create.Select an industry system and enter three different industry types. Mark one entry as Standard Industry. | The Industries are listed in the Industries table. For each industry system, only one industry can be set as Standard Industry. |  |
| 13 | Save Your Process | Choose Save. | A confirmation message with the text Request Created is displayed.The Process ID is displayed as a link under the Process Information section.In case of a validation error, the error will be displayed in a popup window. |  |

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
| 1 | Submit Single Request | Choose Submit. | A confirmation message with the text Process XYZ started displays, where XYZ is the ID of your governance process. | If a workflow is configured in the Configure Process Template app, the workflow for this governance process will be triggered automatically after it is submitted. |
| 2 | Check Process KPI | On the Process Information tab choose the highlighted Process ID. | The Single Processing view for this process opens.The process status is Stopped for Review (Edit).The business partner data is displayed as bars and categorized as Inserted Rows.The Delete and Continue buttons are not visible. | The process cannot be continued or deleted using the process UI because it is controlled by a workflow. |

#### [Optional] Validate and Approve Governance Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The approver validates the business partner data and approves the request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Check Workflow Inbox | Navigate to the home page of the Fiori launchpad and choose My Inbox. | A task named Approve Master Data Request XYZ is displayed in the All Tasks list. XYZ stands for the ID of your governance process. |  |
| 2 | Check Business Partner Data | Choose the task and verify the business partner data.Navigate between the different tabs to view the data entered in each table, for example address or bank accounts. | The data entered during the [Create New Business Partner Using Governance Process](#unique_14) [page ] 14 step is displayed.If no data was entered for certain tables, they are not displayed.The data is not editable. |  |
| 3 | Check Attachments | In the Process Information tab, choose Files. | The number of attached files is displayed next to the Files button in the Process Information tab.The attached files are not editable. |  |
| 4 | Approve Request | Choose Approve. | A confirmation message stating Task processed successfully is displayed. The task is removed from the task list. |  |
| 5 | Check Governance Process | Navigate to the Manage Governance Processes (F6558A) app and check your Single Processing. Verify the KPI chart of the Business Partner[Activation](#unique_11) [page ] 11 step.Navigate to Process Details and check the Attachments. | The process status is set to Completed.One new single record is activated successfully.The KPI chart color is set to green.The Files button is displayed in the Process Header under Process Goal attribute. The number of uploaded files is displayed in next to the Attachments button. The attached files are not editable. |  |
| 6 | Check Activated Business Partner Data | Navigate to the Manage Business Partners - Central Governance (F6555A) app and search for your business partner using the search criteria in the filter bar.Open the business partner details and check the data. | The business partner record is displayed.The data entered during the [Create New Business Partner Using Governance Process](#unique_14) [page ] 14 step is displayed. | The single request process is completed and the business partner data is activated. |

#### [Optional] Reject Governance Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The approver validates the business partner data and rejects the request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Check Workflow Inbox | Navigate back to the Manage Business Partners - Central Governance (F6555A) launchpad and choose My Inbox. | A task named Approve Master Data Request XYZ is displayed in the All Tasks list. XYZ stands for the ID of your governance process. |  |
| 2 | Reject Request | Choose Reject. | A confirmation message stating Task processed successfully is displayed. The task is removed from the task list. |  |
| 3 | Check Governance Process | Navigate to the Manage Governance Processes (F6558A) app and check your Single Processing.Navigate to Process Details and check the Attachments. | The process status is set to Deleted.The process has stopped at the Edit step. A confirmation message with the text The process was deleted is displayed.The Files button is displayed in the Process Header under Process Goal Attribute. The number of uploaded files is displayed in next to the Attachments button. The attached files are not editable. |  |

#### [Optional] Send Governance Process for Revision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The approver validates the business partner data and sends the request for revision.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Check Workflow Inbox | Navigate back to the Manage Business Partners - Central Governance (F6555A) launchpad and choose My Inbox. | A task named Approve Master Data Request XYZ is displayed in the All Tasks list. XYZ stands for the ID of your governance process. |  |
| 2 | Send Request for Revision | Choose Send for Revision. | A confirmation message stating Task processed successfully is displayed. The task is removed from the task list. |  |
| 3 | Check Workflow Inbox | Choose Refresh in the workflow task list and scroll up. | A new task named Rework Master Data Request XYZ is displayed in the All Tasks list. XYZ stands for the ID of your governance process. |  |
| 4 | Revise Request | Choose the task from the task list, then choose Edit and change some of the business partner data.Choose Attachments and create a few attachments and remove some of the existing attachments. Save your changes.Choose Send for Approval and repeat the steps from [[Optional] Validate and Approve Governance Process](#unique_16) [page ] 16. | The request opens in read-only mode.The Edit, Send for Approval, and Withdraw Request buttons are visible.The UI changes to edit mode from the workflow inbox. All available data tabs are enabled for editing. Adding or removing attachments is also enabled. |  |

### Manage Business Partners Central Governance

#### Change Active Business Partner Using Governance Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

As a requester you can create a new governance process to change a new business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist for Business Partner Data. | The SAP Fiori launchpad opens. |  |
| 2 | Access App | Open Manage Business Partners (F7204A) | The Manage Business Partners (F7204A) app opens. |  |
| 3 | Search for Business Partner | Search for your active business partner using the filters. | The search results are displayed. |  |
| 4 | Navigate to Business Partner Details | Choose an entry from the search result list to open the business partner details. | The business partner record opens. |  |
| 5 | Create New Governance Process | Choose Edit and provide the process information details | The UI changes to edit mode and process information can be entered.The Process Information tab displays.The process template SAP: Single Processing is selected by default. |  |
| 6 | Change Business Partner Data | Change values for some of the fields and delete values from other fields. For example, delete and replace some of the values in the General Information table.Delete an existing role and add a new role in the Roles table.Change the Standard Address data and Standard Communication data of an existing address in the Address tables.Delete some of the Standard Communication details and replace them with new details.Delete an existing address and add and validate a new address.Change or Delete an existing Address version and add a new address versionChange an existing bank account in the Bank Accounts table. Delete a bank account and add a new bank account.Change the standard flag for Industries. Delete an existing industry and add a new industry.Change an existing Tax Number. Delete a tax number and add a new tax number.Change an existing Identification Number. Delete an ID number and add a new ID number. |  |  |
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
| 1 | Submit Single Request | Choose Submit. | A confirmation message with the text Process XYZ started displays, where XYZ is the ID of your governance process. | If a workflow is configured in the Configure Process Template app, the workflow for this governance process will be triggered automatically after it is submitted. |
| 2 | Check Single Request Process | In the Process Information tab, choose the highlighted Process ID.Check the KPI chart for the Edit step. | The Single Processing view for this process opens.The process status is Stopped for Review (Edit).The business partner data is displayed as bars and categorized as Changed Rows for the data that you changed.Deleted entries of dependent data such as role or address are categorized as Deleted Rows and added entries are categorized as Inserted Rows. | The process cannot be continued or deleted using the process UI because it is controlled by a workflow. |

#### [Optional] Validate and Approve Governance Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The approver validates the business partner data and approves the request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Check Workflow Inbox | Navigate back to the Manage Business Partners - Central Governance (F6555A) launchpad and choose My Inbox. | A task named Approve Master Data Request XYZ is displayed in the All Tasks list. XYZ stands for the ID of your governance process. |  |
| 2 | Check Business Partner Data | Choose the task, then choose the Changes tab. Verify all of the changes.Choose Check. | The data entered during the [Create New Business Partner Using Governance Process](#unique_14) [page ] 14 step is displayed.Changes made during the [Change Active Business Partner Using Governance Process](#unique_17) [page ] 19 step are displayed in the Changes table.If no data was entered for certain tables, they are not displayed.The data is not editable. |  |
| 3 | Check Attachments | In the Process Information tab, choose Files. | The number of attached files is displayed next to the Files button in the Process Information tab.The attached files are not editable. |  |
| 4 | Approve Request | Choose Approve. | A confirmation message stating Task processed successfully is displayed. The task is removed from the task list. |  |
| 5 | Check Governance Process | Navigate to the Manage Governance Processes (F6558A) app and check your Single Processing. Verify the KPI chart of the Business Partner[Activation](#unique_11) [page ] 11 step.Navigate to Process Details and check the Attachments. | The process status is set to Completed.One new single record is activated successfully.The KPI chart color is set to green.The Files button is displayed in the Process Header under Process Goal Attribute. The number of uploaded files is displayed in next to the Attachments button. The attached files are not editable. |  |
| 6 | Check Activated Business Partner Data | Navigate to the Manage Business Partners - Central Governance (F6555A) app and search for your business partner using the search criteria in the filter bar.Open the business partner details and check the data. | The business partner record is displayed.The data changed during the [Change Active Business Partner Using Governance Process](#unique_17) [page ] 19 step is displayed. |  |

### Manage Inbound Processes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Verify the process template for inbound processing.

Prerequisites

Before testing this scenario, you must complete the configuration steps described in the Set-Up Instructions for this scope item. The configuration is specific to your implementation and includes mandatory settings that are not delivered by SAP and must be configured by you. For more information, refer to the [Setting Up Central Governance for Business Partner (1N7)](https://help.sap.com/docs/s4hana-best-practices/setting-up-central-governance-for-business-partner-1n7/) document.

System Access

The test is conducted in the following systems:

| System | Details |
| --- | --- |
| Target System: SAP S/4HANA Cloud Public Edition | <Provide details on how to access system for example, system client or URL> |
| Source System: SAP S/4HANA Cloud Public Edition | <Provide details on how to access system for example, system client or URL> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to the Source System | Log on to the back end of the source system. |  |  |
| 2 | Create Business Partner | Open transaction bp. Select a Person, Organization, or Group. For this test, choose Organization.Fill in the mandatory fields and choose Save. | A new business partner is created. |  |
| 3 | Log on to the Target System | Log on to the SAP Fiori launchpad of the target system as a Master Data Specialist for Business Partner Data. |  |  |
| 4 | Access App | Open the Manage Inbound Processes app.Navigate to the new inbound process which was created from the replicated business partner of the source system. | The inbound process UI opens. |  |
| 5 | Check Inbound Process | The SAP: Decentr. Create BP+Rel.w/Matchg process includes the following steps:Initial Check BPMatching BPFilter Open Match GroupsBest Record CalculationValidation BPFilter Erroneous RecordsActivation BPMatching RelBest Record Calculation RelValidation RelActivation Rel | The process is executed and completed automatically. |  |
| 6 | Check Business Partner Replication | After the process is completed, navigate to the Activation BP step and choose Show All Changes.The new business partner with the same Name is listed in change Details. | The business partner is replicated from the source system to the target system. |  |
| 7 | Log On to the Source System | Log on to the back end of the source system. |  |  |
| 8 | Change Business Partner | Open transaction bp and search for the business partner you created. Change some values, for example, the Search Term field.Choose Save. | The business partner data is changed. |  |
| 9 | Log on to the Target System | Log on to the SAP Fiori launchpad of the target system as a Master Data Specialist for Business Partner Data. |  |  |
| 10 | Access App | Open the Manage Inbound Processes app.Navigate to the new inbound process which was created from the replicated business partner of the source system. |  |  |
| 11 | Check Inbound Process | The SAP: Decentr. Update BP+Rel process includes the following steps:EditValidation BPFilter Erroneous RecordsActivation BPValidation RelActivation Rel | The process is executed and completed automatically. |  |

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
- related-to :: [[02-business-partner-and-product-master-data/test-script-central-governance-for-product-1n5-sap-s-4hana-cloud-publi]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1N7_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 44,890 chars in the whole document
