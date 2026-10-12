---
id: 06-management-accounting/test-script-organizational-flexibility-in-financial-accounting-4pg-sap
title: "Test Script: Organizational Flexibility in Financial Accounting (4PG) - SAP S/4HANA Cloud Public Edition (4PG_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 4PG: create, simulate, activate and process a profit center organizational change."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/profit-centers]
aliases: [4PG_S4CLD2608_BPD_EN_XX]
keywords: [Profit Centers and Profit Center Reorganization, organizational change, profit center reassignment, organizational change simulation, organizational change activation, organizational change processing, organizational change reporting, extension ledger, data source extension, wbs elements]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4PG_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1041
topic: 06-management-accounting/profit-centers
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Organizational Flexibility in Financial Accounting (4PG) - SAP S/4HANA Cloud Public Edition (4PG_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4PG_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Profit Centers and Profit Center Reorganization** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Organizational Flexibility in Financial Accounting (4PG) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232835288)

[2 Prerequisites 4](#_Toc232835289)

[2.1 System Access 4](#_Toc232835290)

[2.2 Roles 4](#_Toc232835291)

[2.3 Master Data and Organizational Data 5](#_Toc232835292)

[2.4 Business Conditions 6](#_Toc232835293)

[2.5 Preliminary Steps 6](#_Toc232835294)

[2.5.1 Define Extension Ledger for Simulation (Optional) 6](#_Toc232835295)

[2.5.2 Create Data Source Extension (Optional) 8](#_Toc232835296)

[3 Overview Table 9](#_Toc232835297)

[4 Test Procedures 11](#_Toc232835298)

[4.1 Create an Organizational Change 11](#_Toc232835299)

[4.2 Identify Objects Affected by an Organizational Change (Optional) 12](#_Toc232835300)

[4.3 Add Objects to Organizational Change 13](#_Toc232835301)

[4.4 Simulate an Organizational Change (Optional) 14](#_Toc232835302)

[4.5 Analyze Organizational Change Master Data - Hierarchy (Optional) 16](#_Toc232835303)

[4.6 Analyze Organizational Change Master Data - Lists (Optional) 17](#_Toc232835304)

[4.7 Analyze Profit Center Balances (Optional) 18](#_Toc232835305)

[4.8 Analyze General Ledger Line Items (Optional) 19](#_Toc232835306)

[4.9 Activate an Organizational Change 20](#_Toc232835307)

[4.10 Process and Complete an Organizational Change 22](#_Toc232835308)

[4.11 Analyze Master Data Changes - Hierarchy (Optional) 23](#_Toc232835309)

[4.12 Analyze Master Data Changes - Lists (Optional) 24](#_Toc232835310)

[4.13 Analyze Financial Data Changes (Optional) 25](#_Toc232835311)

[4.14 Analyze Profit Center Balances (Optional) 26](#_Toc232835312)

## Purpose

Overview

Generally, a management decision triggers a change to the profit center structure.

The current scope for organizational changes is designed for Professional Services customers and for all customers who use product-related business processes, such as purchasing, sales, and production.

You can define the profit center reassignment for the designated master data and business objects. The objects affected by the reorganization are reassigned and their balances are reposted to the new organizational entities.

The solution supports the reassignment of profit centers at a key date (effective date).

The solution lets you simulate an organizational change. Analytics capabilities are provided to assess the completeness of the object list and the profit center reassignment status, preview or review the transfer posting and its effect on financial KPIs, and to check the logs for the steps performed.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/4PG_S4CLD2602_BPD_EN_XX.docx)). |

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Extensibility Specialist | SAP_BR_EXTENSIBILITY_SPEC | Extensibility / Extensibility | SAP_BR_EXTENSIBILITY_SPEC / SAP_CA_SPT_EXT_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Divisional Accountant | SAP_BR_DIVISION_ACCOUNTANT | Divisional Accounting | SAP_BR_DIVISION_ACCOUNTANT |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |

### Master Data and Organizational Data

Default Values

The organizational structure and master data of your company was created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

The business process is enabled with this organization-specific master data, examples are provided in the next section.

Using Your Own Master Data

You can also use customized values for any material or organizational data for which you have created master data. For more information on how to create master data, see the Master Data Procedures documentation.

Use the following master data in the process steps described in this document:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Profit Center | <profit center> |  | Two profit centers are required for the organizational change. |
| Company Code | <company code> |  |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNH | Create Profit Center - MDS |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| J11 - Customer Project Management – Project-Based Services | A customer project must be created with three work packages and contract type fixed price for the billing items. |

### Preliminary Steps

#### Define Extension Ledger for Simulation (Optional)

Purpose

In order to use the optional simulation functionality of the organizational change, you need to define an extension ledger for posting the simulated transfer journal entries.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Choose Configure Your Solution. |  |  |
| 4 | Access Configuration | Make the following entries and choose Go:Application Area: FinanceSub Application Area: General Ledger |  |  |
| 5 | Open | Choose the arrow button to the right of the Ledgers and Valuation row. |  |  |
| 6 | Select Configuration Step | For the Define Extension Ledger row, choose Configure. |  |  |
| 7 | Define Extension Ledger | Choose New Entries.Make the following entries and choose Save:Extension Ledger: <XX>Extension Ledger Name: <name>Extension Ledger Type: Line items with technical numbers / deletion possibleUnderlying Ledger: 0L | An extension ledger with type Line items with technical number/ deletion possible is created and assigned to a standard ledger. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Extension Ledger.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Extension Ledger screen is displayed. |  |
| 3 | Define Extension Ledger | Choose New Entries.Make the following entries and choose Save:Extension Ledger: <XX>Extension Ledger Name: <name>Extension Ledger Type: Line items with technical numbers / deletion possibleUnderlying Ledger: 0L | An extension ledger with type Line items with technical number/ deletion possible is created and assigned to a standard ledger. |  |

#### Create Data Source Extension (Optional)

Purpose

The data source extension enables you to check the journal entries created by an organizational change.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Extensibility Specialist. |  |  |
| 2 | Access App | Open Custom Fields (F1481). | The Custom Fields and Logic screen displays. |  |
| 3 | Access Configuration | On the Data Source Extensions tab, choose + (Create). | The New Data Source Extension dialog box displays. |  |
| 4 | Create Data Source Extension | Make the following entries and choose Create:Data Source: Display Line Items in General LedgerDescription: <description>Extension ID: <ID> | A new data source extension is created. |  |
| 5 | Save Field Selection | On the Field Selection tab, expand the node Display Line Items in General Ledger.Drill down in the node I_JournalEntryItemBrowser and select the checkbox for the field Organizational Change.Choose Save. | Under Selected Fields, the selected Field Name and Field Path are displayed.The data source extension is saved. |  |
| 6 | Publish Data Source Selection | Choose Publish. | The data source extension with field Organizational Change is published for the app Display Line Items in General Ledger (F2217). |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create an Organizational Change](#unique_11) [page ] 11 | Divisional Accountant | Manage Organizational Changes (F4567) | The organizational change is created. |
| [Identify Objects Affected by an Organizational Change (Optional)](#unique_12) [page ] 12 | Divisional Accountant | Where-Used List - Profit Centers (F3751) | A list of WBS-elements for the selected profit center is displayed. |
| [Add Objects to Organizational Change](#unique_13) [page ] 13 | Divisional Accountant | Manage Organizational Changes (F4567) | The WBS (billing) elements are added to the organizational change. |
| [Simulate an Organizational Change (Optional)](#unique_14) [page ] 14 | Divisional Accountant | Manage Organizational Changes (F4567) | A simulation job has been started and transfer postings have been created in the extension ledger. |
| [Analyze Organizational Change Master Data - Hierarchy (Optional)](#unique_15) [page ] 16 | Divisional Accountant | Organizational Change Report - Master Data Hierarchy (F4868) | The app for master data reporting shows the complete list of affected objects. |
| [Analyze Organizational Change Master Data - Lists (Optional)](#unique_16) [page ] 17 | Divisional Accountant | Organizational Change Report - Master Data Lists (F7047) | The app for master data reporting shows the complete list of affected objects. |
| [Analyze Profit Center Balances (Optional)](#unique_17) [page ] 18 | Divisional Accountant | Organizational Change Report - Financial Data (W0175) | The report shows the changes affecting the profit centers in the extension ledger. |
| [Analyze General Ledger Line Items (Optional)](#unique_18) [page ] 19 | General Ledger Accountant | Display Line Items in General Ledger (F2217) | The report shows the posted line items in the extension ledger. |
| [Activate an Organizational Change](#unique_19) [page ] 20 | Divisional Accountant | Manage Organizational Changes (F4567) | The organizational change is activated and ready for processing. |
| [Process and Complete an Organizational Change](#unique_20) [page ] 22 | Divisional Accountant | Manage Organizational Changes (F4567) | Jobs are scheduled to process and complete the profit center update in the affected objects and to create the transfer postings. |
| [Analyze Master Data Changes - Hierarchy (Optional)](#unique_21) [page ] 23 | Divisional Accountant | Organizational Change Report - Master Data Hierarchy (F4868) | Check the result of the organizational change and ensure that all object changes are performed. |
| [Analyze Master Data Changes - Lists (Optional)](#unique_22) [page ] 24 | Divisional Accountant | Organizational Change Report - Master Data Lists (F7047) | Check the result of the organizational change and ensure that all object changes are performed. |
| [Analyze Financial Data Changes (Optional)](#unique_23) [page ] 25 | Divisional Accountant | Organizational Change Report - Financial Data (W0175) | The report displays financial data affected by the organizational change. |
| [Analyze Profit Center Balances (Optional)](#unique_24) [page ] 26 | Divisional Accountant | Organizational Change Report - Financial Data (W0175) | The report shows the changes affecting the profit centers in the standard ledger. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create an Organizational Change

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a new organizational change with an effective date.

After creating a new organizational change, the organizational change status remains Inactive and you can perform the following actions:

- Delete organizational change
- Edit effective date
- Edit object list

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Divisional Accountant. |  |  |
| 2 | Access App | Open Manage Organizational Changes (F4567). | The Manage Organizational Changes initial screen displays. |  |
| 3 | Create Organizational Change | Choose Create.On the Organizational Change screen, make the following entries and choose Save:Organizational Change: for example, OCQ120YYDescription: for example, Organizational Change Q1/20YYEffective Date: <choose a date that is the first day of a period>Company Codes: <company code> | The organizational change is created and shows the status Inactive. |  |

### Identify Objects Affected by an Organizational Change (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you identify objects which are affected by an organizational change.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Divisional Accountant. |  |  |
| 2 | Access App | Open Where-Used List - Profit Centers (F3751). | The Where-Used List - Profit Centers screen displays. |  |
| 3 | Identify Objects | Enter the following data and choose Go:Profit Center: <profit center>Used In: for example, WBS Elements | The number of objects assigned to the profit center for the object type are displayed. |  |
| 4 | Display Objects | Choose an Object Type to view:for example, WBS Elements | The list shows all objects of the selected object type that are assigned to the given profit center. |  |

### Add Objects to Organizational Change

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You add the objects identified for reassignment to the organizational change and assign a new profit center to these objects.

After adding the objects, the organizational change status remains Inactive. You can perform the following actions:

- Delete organizational change
- Edit effective date
- Edit object list
- Simulate
- Activate

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Divisional Accountant. |  |  |
| 2 | Access App | Open Manage Organizational Changes (F4567). | The Manage Organizational Changes screen displays. |  |
| 3 | Select Organizational Change | Choose Go.Select your Organizational Change from the list and choose the arrow button at the right of the row. | The Organizational Change screen displays. |  |
| 4 | Create WBS Element | Choose the WBS Element tab. Choose Create. | The WBS Element screen displays. |  |
| 5 | Assign New Profit Center | Make the following entries and choose Save:General InformationWBS Element: <first work package>New Profit Center: <profit center> | The objects are displayed in the WBS Element section with their attributes, e.g., Old Profit Center, New Profit Center, Company Code, and Project Definition. |  |
| 6 | Import Objects | On the WBS Element tab, choose Import Objects | The Import WBS Elements for Organizational Change <organizational change> screen displays. |  |
| 7 | Download Template | Choose Download Template. | The template is downloaded |  |
| 8 | Add WBS Elements | Open the template and make the following entries:WBS ElementNew Profit Center<second work package><profit center><third work package><profit center>Save your file. | Your changes to the template are saved. |  |
| 9 | Upload File | Choose Browse.Select your file and open it. | The file is uploaded and a preview table of the WBS elements displays. |  |
| 10 | Import WBS Elements | Choose Import.Note The Import button will be disabled if any errors are found during the upload. | The WBS elements are imported |  |

### Simulate an Organizational Change (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, you can simulate the organizational change. You can verify whether all provided data are correct, which dependent objects are determined, and which effect the organizational change would have on your financial statement by profit center. Furthermore, you can check for potential errors before processing the organizational change.

After simulation, the organizational change status remains Inactive and you can perform the following actions:

- Delete organizational change
- Edit effective date
- Edit object list
- Simulate
- Activate

|  |
| --- |
| Note You can view the progress of your organizational change under History on the Organizational Change screen. |

|  |
| --- |
| Note Alternatively, you can simulate the organizational change with a job. You can schedule the job with the Schedule Jobs for Organizational Changes (F4754) app. Use the job template Organizational Change: Simulation and provide the Organizational Change under Parameters. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Divisional Accountant. |  |  |
| 2 | Access App | Open Manage Organizational Changes (F4567). | The Manage Organizational Changes screen displays. |  |
| 3 | Simulate Organizational Change | On the entry screen, choose Go.Select your Organizational Change from the list and choose the arrow button at the right of the row.Choose Simulate. | A message displays confirming that a simulation job has been scheduled. |  |
| 4 | Back to Entry View | Choose Back. | The column Run Status now displays a status for your organizational change, for example, Simulation Finished: Success. |  |
| 5 | View Application Logs (Optional) | Choose the Run Status for your organizational change to view the logs.Note You can also navigate to the logs from the Organizational Change screen by choosing Related Apps > Organizational Changes - Application Logs . | The Application Logs screen displays.You can choose the arrow button at the right of the row to view the log details.Results:SuccessWarning: Analyze the warnings and resolve them if needed.Error: Analyze the errors and resolve them. Rerun the simulation afterwards. |  |
| 6 | Rerun Simulation (Optional) | If there are errors, make the necessary corrections and execute the simulation again. | The simulation runs successfully. |  |

### Analyze Organizational Change Master Data - Hierarchy (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you analyze the complete list of objects determined by the organizational change as root objects and dependent objects. All objects should have the status Reassignment not started.

|  |
| --- |
| Note You can filter for several root object types, e.g., production order, process order, product, product cost collector, project, and WBS element. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Divisional Accountant. |  |  |
| 2 | Access App | Open Organizational Change Report - Master Data Hierarchy (F4868). | The Organizational Change Report - Master Data screen displays. |  |
| 3 | View Master Data | On the entry screen, make the following entries and choose Go:Organizational Change: <your organizational change>Note You can also navigate to the report from the Organizational Change screen by choosing Related Apps > Organizational Change Report - Master Data Hierarchy . | A tree table with the structure of master data affected by the organizational change displays.Expand and collapse various list levels for root object types and dependent object types.Check column Status.Results:Reassignment not startedReassignment failedReassignment successful |  |

### Analyze Organizational Change Master Data - Lists (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you analyze the complete list of objects determined by the organizational change. All objects should have the status Reassignment not started.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Divisional Accountant. |  |  |
| 2 | Access App | Open Organizational Change Report - Master Data Lists (F7047). | The Organizational Change Report - Master Data Lists screen displays. |  |
| 3 | View Master Data Object Types | On the entry screen, make the following entries and choose Go:Organizational Change: <your organizational change> | A list of master data object types affected by the organizational change displays. The number of objects per object type displays.Check column Reassignment Status.Results:Reassignment not startedReassignment failedReassignment successful |  |
| 4 | View Master Data Objects | Choose an object type (>) from the list to view the objects.Note You can also navigate to the report from the Organizational Change screen by choosing Related Apps > Organizational Change Report - Master Data Lists . | A list of objects displays for the selected object type. |  |

### Analyze Profit Center Balances (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can analyze the impact of the planned organizational change on the account balances by profit center. These balances are based on the simulated transfer postings in the extension ledger.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Divisional Accountant. |  |  |
| 2 | Access App | Open Organizational Change Report - Financial Data (W0175) |  |  |
| 3 | Analyze Profit Center Balances | Make the following entries and choose OK:Ledger: <your extension ledger>Ledger Fiscal Year: <current year>Profit Center: <your profit center>Key Date: <effective date of organizational change> | The Organizational Change Report - Financial Data screen displays.The report shows the account balances grouped by profit center. |  |
| 4 | View Organizational Change Data | Choose Navigation Panel.For the field Organizational Change, choose Add field to rows axis. | The Navigation Panel displays.The field Organizational Change is added to the Data Analysis view. |  |

### Analyze General Ledger Line Items (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can analyze the line items of journal entries created by the simulation in the extension ledger.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Display Line Items in General Ledger (F2217) | The Display Line Items in General Ledger screen displays. |  |
| 3 | Add Filter | Choose Adapt Filters.Under the Other Fields group choose More Filters.Select the checkbox for Organizational Change.Choose OK. | The filter is added. |  |
| 4 | View Line Items | Enter your organizational change in the field and choose Go. | The line items that have been posted by the organizational change in the extension ledger are displayed. |  |
| 5 | Add Column | Choose Settings.Select the checkbox for Organizational Change and choose OK. | The organizational change column displays in the line items table. |  |
| 6 | Add Filter | Choose Adapt Filters.Select the checkbox for WBS Element.Choose OK. | The filter is added.You can filter for specific WBS elements of your organizational change. |  |
| 7 | Add Column | Choose Settings.Select the checkbox for WBS Element and choose OK. | The WBS element column displays in the line items table. |  |

### Activate an Organizational Change

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you activate the organizational change.

It is recommended to activate the organizational change before the organizational change effective date is reached. The activation of the organizational change influences the derivation of the profit center during posting. If the posting date falls after the effective date, then the new profit center is derived for profit and loss and dedicated balance sheet postings. However, the master data objects have not been changed at this point in time.

Additionally, the activation of the organizational change considers when new depending objects are created which have to be included into the organizational change.

After activation, the organizational change status changes to Active and you can perform the following actions:

- Simulate
- Process

|  |
| --- |
| Note Alternatively, you can activate the organizational change with a job. You can schedule the job with the Schedule Jobs for Organizational Changes (F4754) app. Use the job template Organizational Change: Activation and provide the Organizational Change under Parameters. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Divisional Accountant. |  |  |
| 2 | Access App | Open Manage Organizational Changes (F4567). | The Manage Organizational Changes displays. |  |
| 3 | Select Organizational Change | Choose Go.Select your Organizational Change from the list and choose the arrow button at the right of the row. | The Organizational Change screens displays. |  |
| 4 | Activate the Organizational Change | Choose Activate. | A message displays confirming that an activation job has been scheduled. The job can take several minutes to complete. |  |
| 5 | Back to Entry View | Choose Back. | The column Run Status displays whether the run was successful.The organizational change status is Active. |  |
| 6 | View Application Logs (Optional) | Choose the Run Status for your organizational change to view the logs.Note You can also navigate to the logs from the Organizational Change screen by choosing Related Apps > Organizational Changes - Application Logs . | The Application Logs screen displays.You can choose the arrow button at the right of the row to view the log details.Results:SuccessWarning: Analyze the warnings and resolve them if needed.Error: Analyze the errors and resolve them. |  |

### Process and Complete an Organizational Change

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The objects affected by the reorganization will be assigned to the new profit center and the profit center stocks and balances will be reposted to the newly assigned organizational entities. Afterwards, the system checks the completion of the updated master data and transfer postings.

After processing and completing the organizational change, the status changes to Complete if no errors occurred. The status changes to Processed if errors occurred. Depending on the status of the organizational change, you can perform the following actions:

- Process and Complete (again)
- Process

|  |
| --- |
| Note Alternatively, you can process the organizational change with a job. You can schedule the job with the Schedule Jobs for Organizational Changes (F4754) app. Use the job template Organizational Change: Processing and provide the Organizational Change under Parameters. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Divisional Accountant. |  |  |
| 2 | Access App | Open Manage Organizational Changes (F4567). | The Manage Organizational Changes displays. |  |
| 3 | Select Organizational Change | Choose Go.Select your Organizational Change from the list and choose the arrow button at the right of the row. | The Organizational Change screens displays. |  |
| 4 | Process Organizational Change | Choose Process > Process and Complete . | A message dispalys which explains the combination of the processing run and completion run. When accepting this, a message displays confirming that a processing job has been scheduled. The jobs can take several minutes to complete. |  |
| 5 | Back to Entry View | Choose Back. | The column Run Status displays whether the run was successful.The organizational change status is Processed.Starting from the effective date of the organizational change, the new profit center is used for all postings of affected objects. |  |
| 6 | View Application Logs (Optional) | Choose the Run Status for your organizational change to view the logs.Note You can also navigate to the logs from the Organizational Change screen by choosing Related Apps > Organizational Changes - Application Logs . | The Application Logs screen displays.You can choose the arrow button at the right of the row to view the log details.Results:SuccessWarning: Analyze the warnings and resolve them if needed.Error: Analyze the errors and resolve them. |  |
| 7 | Rerun Processing (Optional) | If there are errors, make the necessary corrections and process the organizational change again. |  |  |

### Analyze Master Data Changes - Hierarchy (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can get an overview of the object master data affected by the organizational change, view how dependent objects are being determined by a given root object, and analyze the status of the profit center reassignment. The status of each object should have changed from Reassignment not started to Reassignment successful.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Divisional Accountant. |  |  |
| 2 | Access App | Open Organizational Change Report - Master Data Hierarchy (F4868). | The Organizational Change Report - Master Data screen displays. |  |
| 3 | View Master Data | On the entry screen, make the following entries and choose Go:Organizational Change: <your organizational change>Note You can also navigate to the report from the Organizational Change screen by choosing Related Apps > Organizational Change Report - Master Data Hierarchy . | A tree table with the structure of master data affected by the organizational change displays.You can expand and collapse various list levels for root object types and dependent object types.The Status column displays the state of your organizational change.Results:Reassignment not startedReassignment failedReassignment successful |  |

### Analyze Master Data Changes - Lists (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can get an overview of the object master data affected by the organizational change and analyze the status of the profit center reassignment. The status of each object should have changed from Reassignment not started to Reassignment successful.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Divisional Accountant. |  |  |
| 2 | Access App | Open Organizational Change Report - Master Data Lists (F7047). | The Organizational Change Report - Master Data Lists screen displays. |  |
| 3 | View Master Data Object Types | On the entry screen, make the following entries and choose Go:Organizational Change: <your organizational change> | A list of master data object types affected by the organizational change displays. The number of objects per object type displays.Check column Reassignment Status.Results:Reassignment not startedReassignment failedReassignment successful |  |
| 4 | View Master Data Objects | Choose an object type (>) from the list to view the objects.Note You can also navigate to the report from the Organizational Change screen by choosing Related Apps > Organizational Change Report - Master Data Lists . | A list of objects displays for the selected object type. |  |

### Analyze Financial Data Changes (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can get an overview of the financial data affected by the organizational change.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Divisional Accountant. |  |  |
| 2 | Access App | Open Organizational Change Report - Financial Data (W0175). | The Organizational Change Report - Financial Data screen displays. |  |
| 3 | View Financial Data | On the entry screen, make the following entries and choose Go:Ledger: <your extension ledger>Organizational Change: <your organizational change>Note You can also navigate to this report from the Organizational Change screen by choosing Related Apps > Organizational Change Report - Financial Data . | Financial data affected by the organizational change displays. |  |

### Analyze Profit Center Balances (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can analyze the impact of the planned organizational change on the account balances by profit center. These balances are based on the simulated transfer postings in the extension ledger.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Divisional Accountant. |  |  |
| 2 | Access App | Open Organizational Change Report - Financial Data (W0175) |  |  |
| 3 | Analyze Profit Center Balances | Make the following entries and choose OK:Ledger: <your extension ledger>Ledger Fiscal Year: <current year>Profit Center: <your profit center>Key Date: <effective date of organizational change> | The Organizational Change Report - Financial Data screen displays.The report shows the account balances grouped by profit center. |  |
| 4 | View Organizational Change Data | Choose Navigation Panel.For the field Organizational Change, choose Add field to rows axis. | The Navigation Panel displays.The field Organizational Change is added to the Data Analysis view. |  |

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
> Flagged while digesting this document, not verified: Process and Complete: the purpose says the status becomes Complete if no errors occurred (Processed only if errors), but test step 5 expects the status to be Processed after the run.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Last process step (Analyze Profit Center Balances, after processing): the Overview Table says the report shows changes in the standard ledger, but the procedure and purpose use the extension ledger and simulated transfer postings.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[06-management-accounting/2608-master-data-fi-en-xx-119]]
- related-to :: [[06-management-accounting/create-profit-center-mds-bnh-605]]
- related-to :: [[06-management-accounting/mds-bnh-607]]
- related-to :: [[06-management-accounting/mds-bnh-609]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4PG_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 45,857 chars in the whole document
