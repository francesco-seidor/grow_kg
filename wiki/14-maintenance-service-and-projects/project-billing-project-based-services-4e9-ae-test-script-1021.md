---
id: 14-maintenance-service-and-projects/project-billing-project-based-services-4e9-ae-test-script-1021
title: Project Billing – Project-Based Services (4E9_AE) Test Script (4E9_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 4E9_AE: project billing (fixed price, T&E, periodic, usage, down payments, repricing, workflows)."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/project-billing]
aliases: [4E9_S4CLD2608_BPD_EN_AE]
keywords: [Project Billing, fixed price billing, time and expense billing, periodic service billing, usage-based billing, on account prepayment, down payments, repricing schedule, billing request workflows, additional billing items]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4E9_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1021
topic: 14-maintenance-service-and-projects/project-billing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Project Billing – Project-Based Services (4E9_AE) Test Script (4E9_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4E9_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Project Billing** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Project Billing – Project-Based Services (4E9_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Project Billing – Project-Based Services (4E9_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232854937)

[2 Prerequisites 4](#_Toc232854938)

[2.1 System Access 4](#_Toc232854939)

[2.2 Roles 4](#_Toc232854940)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232854941)

[2.4 Business Condition 7](#_Toc232854942)

[2.5 Preliminary Steps 7](#_Toc232854943)

[2.5.1 Maintain a Billing Profile 7](#_Toc232854944)

[2.5.2 Create Condition Records (Optional) 9](#_Toc232854945)

[3 Overview Table 10](#_Toc232854946)

[4 Test Procedures 11](#_Toc232854947)

[4.1 Billing for Fixed Price Item 11](#_Toc232854948)

[4.2 Billing For Time and Expense Item 12](#_Toc232854949)

[4.3 Billing for Periodic Service Item 14](#_Toc232854950)

[4.4 Billing for Usage-based Item 15](#_Toc232854951)

[4.5 Billing for Additional Items 16](#_Toc232854952)

[4.6 Billing for On Account Prepayment 17](#_Toc232854953)

[4.7 Billing for Down Payment 19](#_Toc232854954)

[4.8 Schedule Repricing for Projects 23](#_Toc232854955)

[4.9 Manage Workflows for Project Billing Requests (Optional) 24](#_Toc232854956)

## Purpose

Overview

This scope item realizes the standard way to bill customer projects in project-based services. It supports the billing on a fixed price, time and expense, periodic service, and usage-based basis. Additionally, it includes on-account and down payments for time and expense contracts and down payments for fixed price contracts. One of the major functionalities is the write off and postponement of recorded amounts or quantities in the time and expense scenario. Additionally, an approval workflow for project billing requests can be enabled in various ways.

|  |
| --- |
| Note For more details, refer to [Manage Project Billing](https://help.sap.com/viewer/29cf986299714386847f4d4c9bb86994/latest/en-US/09bddf5612e54600a06539c2e4250d30.html) in the Professional Services of product assistance for SAP S/4HANA Cloud Public Edition. |

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
| Billing Specialist - Projects | SAP_BR_PROJ_BILLG_SPCLST | Project Billing | SAP_BR_PROJ_BILLG_SPCLST | Suggested sample user PROJ_BILLG_SPCLST representing the business role Billing Specialist - Projects. |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK | Suggested sample user BILLING_CLERK representing the business role Billing Clerk. |
| Project Manager - Professional Services | SAP_BR_PROJECT_MANAGER_PROF | Project Management – Professional Services | SAP_BR_PROJECT_MANAGER_PROF | Suggested sample user PROJECT_MANAGER_PROF representing the business role Project Manager – Professional Services. |
| Employee | SAP_BR_EMPLOYEE | Self Services / Self Services / Employee Overview Space | SAP_BR_EMPLOYEE / SAP_CA_SPT_EMPLOYEE_CROSS_PC / SAP_EAM_SPT_EMPLOYEE_PC | Suggested sample user EMPLOYEE representing the business role Employee. |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC | Suggested sample user AP_ACCOUNTANT representing the business role Accounts Payable Accountant. |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT | Suggested sample user AR_ACCOUNTANT representing the business role Accounts Receivable Accountant. |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | Suggested sample user BPC_EXPERT representing the business role Configuration Expert - Business Process Configuration. |

|  |
| --- |
| Note The role template Project Manager - Commercial Services and generic role SAP_BR_PROJ_MANAGE_COMM are deprecated from CE2202 and are respectively replaced by the role template Project Manager - Professional Services and generic role SAP_BR_PROJECT_MANAGER_PROF. For customers installing the system before CE2202, you can still use the role template Project Manager - Commercial Services for your existing projects. However, we recommend using the role template Project Manager - Professional Services to create new projects. For more details, please refer to SAP Note [3121435](https://me.sap.com/notes/3121435). |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | T001 | Junior Consultant | The material determination must have been defined in SSCUI Maintain Project Billing Profile.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |
| Material | E002 | Airfare | The material determination must have been defined in SSCUI Maintain Project Billing Profile.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |
| Material | A001 | On account to be billed |  |
| Material | A002 | On account to be utilized |  |
| Material | B001 | One Time Credit |  |
| Material | B002 | Cloud Revenue |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BND | Create Customer Master - MDS |
| BNN | Create Activity Type and Activity Type Hierarchy - MDS |
| 31X | Create Product Master of type "Service Product" - MDS |
| BET | Create Sales Pricing Condition - MDS |
| 3KW | Create CO Cost Rates - MDS |

### Business Condition

Before you can test this scope item, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J11 - Customer Project Management – Project-Based Services | Before running this test script, you should have finished mandatory steps in J11 including Maintain Customer Projects, Maintain Work packages and Time-based Planning, Maintain Work Package Staffing and Maintain Customer Project Billing. |

|  |
| --- |
| Note In order for billing elements to appear in the Manage Project Billing (F4374) app, the following prerequisites must be met in the Create Customer Projects (F0719) and Plan Customer Projects (F0719) apps:The project must have the Use Project Billing (New) setting set to Yes.The stage of the customer project must be In Execution.The billing items must also have at least one billing plan item defined in it.There should be at least one entry for Billing Due Date in the past or now, with Processing Status Open.For following billing processes like creating customer invoicing, refer to Sales Order Processing – Project-Based Services (J14) test script.For other billing processes like process manual debit memo request and manual credit memo request, process preliminary billing document, cancel billing document, also refer to the J14 test script. |

### Preliminary Steps

#### Maintain a Billing Profile

Purpose

This step allows you to add a billing profile, and to define material determination based on the criteria according to your needs.

Prerequisites

Make sure the corresponding materials, activity types, and G/L accounts are created before maintaining materials determination.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Filter Out SSCUI | Choose Configure Your Solution.Select Enterprise Portfolio & Project Management from the Application Area dropdown list; select Billing from the Sub Application Area dropdown list. |  |  |
| 4 | Maintain the Billing Profile | Choose the Billing Profile item in the All Items table.On the Configure Your Solution – Billing Profile screen, choose the Configuration Steps tab. For Maintain Billing Profile, choose Configure. For more details, choose the dropdown arrow of the Configure button, and select Configuration Help.Note Configuring the billing profile, materials determination, and the criteria is mandatory to the new project billing process. | The Configure Your Solution – Billing Profile screen displays. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Configuration Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain Billing Profile.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Note Configuring the billing profile, materials determination, and the criteria is mandatory to the new project billing process. | The Configure Your Solution – Billing Profile screen displays. |  |

#### Create Condition Records (Optional)

Purpose

In case you have fine tuned the access sequence of SAP pre-shipped condition types, the relative condition records need to be created accordingly. This process step shows you how to create condition records.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Prices - Sales (F4111) app. | The Manage Prices - Sales screen displays. |  |
| 3 | Change Sales Price | Select PSP0 from the Condition Type dropdown list and press Enter.To create a new condition record, choose Create and enter the following entries:Condition Type: PSP0Condition Table: 305 {Customer/material with release Status}Customer: 10100001Sales Organization: 3310Distribution Channel : 10Product: for example, T001Valid From: <Jan 1st of last year>Condition Amount or Ratio: for example, 100.00 EURPricing Unit: for example, 1 HourChoose Save. |  |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Billing for Fixed Price Item](#unique_10) [page ] 11 | Billing Specialist - Projects | Manage Project Billing (F4374) |  |
| [Billing For Time and Expense Item](#unique_11) [page ] 12 | Billing Specialist - Projects | Manage Project Billing (F4374) |  |
| [Billing for Periodic Service Item](#unique_12) [page ] 14 | Billing Specialist - Projects | Manage Project Billing (F4374) |  |
| [Billing for Usage-based Item](#unique_13) [page ] 15 | Billing Specialist - Projects | Manage Project Billing (F4374) |  |
| [Billing for Additional Items](#unique_14) [page ] 16 | Billing Specialist - Projects | Manage Project Billing (F4374) |  |
| [Billing for On Account Prepayment](#unique_15) [page ] 17 | Billing Specialist - Projects | Manage Project Billing (F4374) |  |
| Billing for Down Payment |  |  |  |
| [Billing for Down Payment](#unique_16) [page ] 19 | Billing Specialist - Projects | Manage Project Billing (F4374) |  |
| Schedule Repricing for Project |  |  |  |
| [Schedule Repricing for Projects](#unique_17) [page ] 23 | Billing Specialist - Projects | Schedule Repricing for Projects (F4422). |  |
| Manage Workflows for Project Billing Requests (Optional) |  |  |  |
| [Manage Workflows for Project Billing Requests (Optional)](#unique_18) [page ] 24 | Configuration Expert - Business Process Configuration | Manage Workflow for Project Billing Requests (F5980) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Billing for Fixed Price Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a billing document request for a fixed price item. Before doing this, you should have created a customer project with a fixed price item as per Customer Project Management – Project-Based Services (J11) test script. For details, refer to the chapter [Business Condition](#unique_6) [page ] 7.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Specialist - Projects. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Project Billing (F4374). | Billing element information comes out in the Billing Elements list. |  |
| 3 | Create Billing Document Request | Use the filters to find your project. Billing element ID is WBS element.Choose multiple billing element lines, then choose Prepare Billing. If a project billing request already exists and you would like to change the selection of billing elements such as adding another billing element, you need to delete the project billing request first by choosing the Delete icon. The multiple selections also work for Time and Expense items. | The New Project Billing Request screen displays. |  |
| 4 | Submit Billing Document Request | Choose Submit.Note You can process fixed price billing items with due dates in the future by selecting the checkbox of Include for Billing before submitting the billing document request. | The billing document request (a.k.a. BDR) is created.Note down the number_________________. |  |
| 5 | Create Preliminary Billing Document | In the Success window, choose link Manage Preliminary Billing Documents - Services, and then choose Save. | The preliminary billing document is created. Mark down the number. |  |
| 6 | Change Preliminary Billing Document | Open app Manage Preliminary Billing Documents - Services (F6990).Search the preliminary billing document you just created.Choose the document number in the preliminary billing document list.On the screen Preliminary Billing Document, choose Edit and change Item Description under the Items tab.Choose Save. | The preliminary billing document is changed. |  |

### Billing For Time and Expense Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

In this activity, you create a billing document request for a time and expense item. Before doing this, you should have:

- Created a customer project with time and expense item as per Customer Project Management – Project-Based Services (J11) test script.
- Recorded time for staffed resources. For details, refer to the step Manage My Timesheet of the Time Recording – Project-Based Services (J12) test script.

Purpose

In this step, you create billing document requests for Time and Expense items including postponement and write-off.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Specialist - Projects. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Project Billing (F4374). Search with filter to find out the Billing item for your project. | Billing Element information comes out in Billing Elements list. |  |
| 3 | Check Billing Element | Check whether Billing Element, Project, Customer, Billing Method (must be Time and Expenses) fields are displayed correctly. Also check if the amounts are displayed correctly. | Billing Element ID equals to WBS element.If the Time and Expenses (T&E) Billing Due Date is in the past, then the To Bill column shows the unbilled revenue until the latest T&E Billing Due Date. If the T&E Billing Due Date is in the future, then the To Bill column shows the unbilled revenue until today, based on the actual postings against the Billing WBS Element.The Unbilled column also shows the unbilled revenue, but not for specific billing period and not restricted to a day unlike To Bill.Estimated actuals = Billed + Unbilled + Billing In Process |  |
| 4 | Add or Update Note (Optional) | Choose Prepare Billing. On the New Project Billing Request screen, navigate to the Time and Expense Items tab.Choose the To Bill tab in the Time and Expense Items section. Select the wanted entry, then click Edit in the upper right corner. Choose Add note to maintain your note.Choose OK and Save.On the New Project Billing Request screen, choose Smart Notes for all the Project Billing Request Items or for some of the PBR items. The system will propose grammatically corrected notes. After selecting the items for which you want to save the proposed notes, choose Save.The Proposed Note has been successfully updated. | Smart Notes is a use case that leverages AI. Please refer to the following linkage to make it available:How to Activate the Package - Joule Premium for Finance Management: [Activating Business AI and Assigning Users](https://help.sap.com/docs/joule/capabilities-guide/activating-business-ai-and-assigning-users?locale=en-US&version=LATEST)SAP Help Portal: [AI-Assisted Smart Notes for Project Billing](https://help.sap.com/docs/SAP_S4HANA_CLOUD/29cf986299714386847f4d4c9bb86994/baaa95fc66a147689e80e6527f22c0f9.html?locale=en-US&version=LATEST) |  |
| 5 | Postpone Billing Items | Choose Prepare Billing. On the New Project Billing Request screen, on the Time and Expense Items tab, To Bill tab, select one item, and choose Postpone. Choose Postpone in the dialog box.Alternatively you can postpone Time and Expense items based on service date:On the To Bill tab, choose Restrict Date. Choose whether you want to Postpone to the next bill those items with service date after: the last day of the previous month.If you want to bill, postpone, or write off in partial, choose the Project Billing Request link to open a New Project Billing Request screen. In Time and Expense Items section, under tab To Bill, choose the wanted entry then choose Edit in upper right corner, maintain the partial quantity in the field Quantity to Postpone and Quantity to Write Off, and then choose Save. | The selected items have moved from the To Bill tab to the To Postpone tab.If use specific date of Restrict Date, all postings after the mentioned date are postponed. |  |
| 6 | Reinclude the Postponed Items | On the To Postpone tab, select one item and choose Reinclude. Choose Reinclude in the pop-up window. | The selected items have moved back to the To Bill tab. |  |
| 7 | Write-Off | On the Time and Expense Items tab, To Bill tab, select one item and choose Write Off. Choose Write Off in the dialog box. | The selected items have moved from the To Bill tab to the To Write Off tab.To Bill does not include written off amounts (after BDR creation) or planned write off amounts (before BDR creation).The Written Off column shows the written off amounts after BDR creation. It is updated after Billing Document Request is created. |  |
| 8 | Check Consistency and Run Repricing | Choose Check Consistency in the upper-right corner. If the service price is unchanged, a popup message is displayed: Project billing request is consistent. If the price is changed, a dialog box displays to remind you there is a price inconsistency. Choose Yes to run repricing. | The price is changed in project billing request, and the To Bill value is updated. |  |
| 9 | Submit Billing Document Request | Choose Submit in the right bottom corner of the New Project Billing Request screen. | The Billing Document Request is created.Note down the number_________________. |  |

### Billing for Periodic Service Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a billing document request for a periodic service item. To do this, you should have created a customer project with a periodic service item as per Customer Project Management – Project-Based Services (J11) test script.

The project billing information should be maintained as described in the step Maintain Customer Project Billing of J11.

- Work Package Type should be Resource Based (Time)
- For billing items, there should be at least one entry for the Contract Type: Periodic Service

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Specialist - Projects. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Project Billing (F4374). | Billing Element information shows in the Billing Element list. |  |
| 3 | Create Billing Document Request | Use the filters to find your project. Billing element id is WBS element. Billing Method = Periodic Service.In the Billing Elements table, choose the billing element , then choose Prepare Billing. | The New Project Billing Request screen displays. |  |
| 4 | Include Item for Billing | In the New Project Billing Request screen, choose Edit, then choose the items you want to bill by selecting Include for Billing. |  |  |
| 5 | Submit Billing Document Request | Choose Submit. | The billing document request (a.k.a. BDR) is created.Note down the number_________________. |  |

### Billing for Usage-based Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a billing document request for a unit-based item (for example license). Before doing this, you should have:

- Created a customer project with a unit-based item as per Customer Project Management – Project-Based Services (J11) test script.
- Captured service unit according to relevant steps in J11.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Specialist - Projects. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Project Billing (F4374). | Billing Element information is displayed in the Billing Element list. |  |
| 3 | Create Billing Document Request | Use the filters to find your project. Billing element id is WBS element. Billing Method=Usage-based BillingChoose the billing element, then choose Prepare Billing. | The New Project Billing Request screen displays. |  |
| 4 | Submit Billing Document Request | In the New Project Billing Request screen, choose tab Usage Based Billing, and then the tab To Bill. Then select a line and choose Submit.You may also choose Postpone, Write Off or Defer after Date with relevant button, which is the same as [Billing For Time and Expense Item](#unique_11) [page ] 12. | The billing document request (a.k.a. BDR) is created.Note down the number_________________. |  |

### Billing for Additional Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a billing document request for additional items. Before doing this, you should have created a customer project as per Customer Project Management – Project-Based Services (J11) test script.

The additional item function works for all the contract types.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Billing Specialist - Projects | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Project Billing (F4374). | Billing Element information comes out in the Billing Element list. |  |
| 3 | Create Billing Document Request | Use the filters to find your project. Billing element ID is WBS element.In Billing Elements table, choose the billing element, and then choose Prepare Billing. The New Project Billing Request screen displays.In the New Project Billing Request screen, choose Additional Items tab. Choose Edit. Then choose Add. A blank billing element entry displays. Fill in the blank as follows:Billing Element: WBS element IDMaterial: B002Service Date: todayQuantity: 2To Bill: 200Choose Save. |  |  |
| 4 | Submit Billing Document Request | Choose Submit. | The billing document request (a.k.a. BDR) is created.Note down the number_________________. |  |

### Billing for On Account Prepayment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

In this activity, a customer project needs to be created with a work package for Time and Expense material. Proceed with the following test steps:

1. Create a customer project as per Customer Project Management – Project-Based Services (J11) test script.

|  |
| --- |
| Note For billing item, under the Billing Due Dates tab, make following entries:Billing Due DateItem UsageAmount (EUR)Current Day minus 7 daysPayment On Account200Current DayTime and Expenses |

1. Record time for staffed resources, planned revenue should be over 200. For more details, refer to the Time Recording through Manage My Timesheet section of Time Recording – Project-Based Services (J12) test script.

Purpose

In this step, you manage the billing for On Account Prepayment item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Specialist - Projects. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Project Billing (F4374) app, make the filter to find out the Billing item with your project. | Billing Element information comes out in Billing Elements list. |  |
| 3 | Check Billing Element | Check whether Billing Element, Project, Customer, Billing Method (must be Time and Expenses) fields are displayed correctly. Also check if the amounts are displayed correctly. | Billing Element ID equals to WBS element. |  |
| 4 | Check the On Account Prepayment item | Check the On Account button shows up in the Billing Due Date column for the corresponding billing element. Choose the icon in the To Bill column for that element to see the planned prepayment amount that is due. | The To Bill column now additionally shows an information icon. Choose the icon shows Planned Prepayment: 200 EUR |  |
| 5 | Create Billing Document Request for the On Account Prepayment | Choose On Account. Alternatively, you can also select the billing elementand choose Prepayment. Choose Submit in the pop-up window.Note An On Account prepayment is billed to your customer in advance for Time and Expenses contracts and reduces the amount posted to accounts receivables during billing. This type of prepayment is displayed in the Manage Project Billing app depending on how a billing item in a billing (WBS) element is set up in the Plan Customer Projects app. Such a billing item must have a due date set up with the Item Usage type Payment on Account. | The Billing Document Request_________________ is created. |  |
| 6 | Create Customer Invoicing for On Account Prepayment | Log on to the SAP Fiori launchpad as a Billing Clerk.Open Create Billing Documents (F0798) - Billing Due List Items.Select the Billing Document Request you created previously and choose Create Billing Documents.Enter the following data and choose OK:Billing Type: Invoice(CI01)Billing Date: <Today>On the Maintain Billing Document screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. | Make a note of the billing document number: __________ |  |
| 7 | Check Billing Element for On Account Prepayment | Log on to the SAP Fiori launchpad as a Billing Specialist - Projects. Open Manage Project Billing (F4374) app, and make the filter to find out the Billing item with your project. |  |  |
| 8 | Create Billing Document Request for Time and Expense item | Choose Prepare Billing to open the New Project Bill Request screen. On the Time and Expense Items tab, To Bill tab, select the entry and choose Submit. The Billing Document Request is created.Note down the number_________________ |  |  |

### Billing for Down Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

In this activity, you create billing document requests for a fixed-price service item and a time and expense item. To do this, you should have created a customer project as per Customer Project Management – Project-Based Services (J11) test script.

1. Maintain two work packages: one with the name "Time and Expenses", another with "Fixed Price".
2. Maintain work package Staffing: Choose Role: Junior Consultant; Effort: 100H for Time and Expenses work package, 200H for Fixed Price work package.
3. Maintain Customer Project Billing:
    1. Create a billing item for Time and Expenses. Contract Type= Time and Expenses; Assigned Work Package = Time and Expenses, : 20,000 EUR

Choose the billing item. Under Billing Due Dates tab, apply the following entries: Amount to be billed

| Billing Due Date | Item Usage | Amount (EUR) |
| --- | --- | --- |
| The first date of current month | Down Payment Request | Amount to be 5000 |
| The last date of current month | Time and Expenses |  |

-
    1. Create a billing item for Fixed Price. Contract Type= Fixed Price; Assigned Work Package = Fixed Price, Amount to be billed: 100,000 EUR

Choose the billing item. Under Billing Due Dates tab, apply the following entries:

| Billing Due Date | Item Usage | Amount (EUR) |
| --- | --- | --- |
| The second date of current month | Down Payment Request | 20,000 |
| The first date of next month | Fixed Price | 100,000 |

1. Time Recording for staffed resource: Refer to Time Recording – Project-Based Services (J12) test script and proceed with the step Perform Time Recording.

| Role | Time | Quantity (H) |
| --- | --- | --- |
| Junior Consultant | Current Date | 100 for Time and Expense Work Package |

Purpose

In this step, you manage the billing for Down Payment item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Specialist - Projects. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Project Billing (F4374) app and make the filter to find out the Billing item with your project. | Billing Element information comes out in Billing Element list. |  |
| 3 | Check Billing Element | Check whether Billing Elements, Project, Customer, Billing Method (must be Time and Expenses or Fixed Price) fields are displayed correctly. Also check if the amounts are displayed correctly. In this example, we check billing element item for Fixed Price first.Choose Setting icon, then choose Down Payment Received and Down Payment Requested | Billing Element ID equals to WBS element. |  |
| 4 | Check the Down Payment Item | Choose the yellow triangle icon under To Bill column for the prepayment details. The yellow triangle indicates there are open billing items in customer project. | The To Bill column now additionally shows an information icon. Choose the icon, it shows Planned Prepayment=20000 EUR |  |
| 5 | Create Down Payment Billing Document Request | Choose the billing element item for Fixed Price, then choose Prepayment in the upper right. A pop-up window for down payment shows up. Choose Submit to create Down Payment Billing Document Request. | You will get a success message. The Billing Document Request_________________ is created.In Manage Project Billing (F4374) app, the Down Payment Requested is now 20000. |  |
| 6 | Option 1: Create Down Payment Request Directly Against Billing Document Request | Log on to the SAP Fiori launchpad as a Billing Clerk. Open Create Billing Documents (F0798) - Billing Due List Items.Choose Billing Settings and ensure the settings for Automatically post billing and Display billing document after creation are ON.Select the billing document request you created previously and choose Create Billing Documents.Enter the following data and choose OK:Billing Type: Down Payment Request(FAZ)Billing Date: <Today>On the Manage Billing Document screen, choose Save. Under Process Flow you can see the details of Down Payment Request and Journal Entry. | Take a note of the billing document number: __________Journal Entry:_________________ |  |
|  | Option 2: Create Down Payment Request Against Preliminary Down Payment Request | Log on to the SAP Fiori launchpad as a Billing Clerk. Open Create Preliminary Billing Documents (F2876).Search the billing document request you created previously in SD Document and choose Go.In Billing Due List Items, choose the billing document request you created previously and choose Create Preliminary Billing Documents.On the Manage Preliminary Billing Documents screen, choose Billing Settings and ensure the settings for Automatically post billing documents and Display billing documents after creation are ON.In the Preliminary Billing Documents list, select the preliminary down payment request you just created, and then choose Create Billing Documents. |  |  |
| 7 | Check Billing Processing Status in Customer Project | Log on to the SAP Fiori launchpad as a Project Manager. Open Create Customer Projects (F0719) app. Under Billing tab, Billing Due Dates, you will find the Processing Status is now Invoiced. |  |  |
| 8 | Post Incoming Payments | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. Open Post Incoming Payments app. Under General Information, input below data:Posting Date= todayJournal Entry Date= todayJournal Entry Type: DZ (Customer Payment)G/L Account=10010000Amount= value no more than Down Payment Requested + TAX, here suppose the output tax is 19%, hence amount=10000*(1+19%)= 11900 EURAccount Type/Account ID: Customer/10100001Choose Propose Item.Under Open Items table, choose Select More. In the pop-up window, for Line Item Type, choose Special G/L Transactions.Filter the Journal Entry you want to clear and choose Clear which is under Clear column. The selected journal entry is now in the table of Items to Be Cleared. Input Allocated Amount =e.g. 11900 EUR, then choose Post. | A pop-up window shows that the journal entry posted successfully.Note To close the project, you need to clear open items manually. Please refer to test step Down Payments > Clear Open items Manually describing in scope item Accounts Receivable (J59). |  |
| 9 | Check the Billing Element | Back to Manage Project Billing (F4374) app to check the displayed amount. | The Down Payment Requested is now 0, and Down Payment Received is 10000 EUR. |  |
| 10 | Create Billing Document Request for Fixed Price Item | Manage Project Billing (F4374) app, choose the billing element for Fixed Price, then choose Prepare Billing. On the New Project Billing Request screen, choose Include for Billing, choose Save, and choose Submit. The billing document request is created.Note For Time and Expense Item, there is no column Include for Billing. | Make a note of the billing document request number: __________ |  |
| 11 | Create Customer Invoicing for Fixed Price Item | Log on to the SAP Fiori launchpad as a Billing Clerk. Open Create Billing Documents (F0798) - Billing Due List Items.Choose Billing Settings and ensure the settings for Automatically post billing and Display billing document after creation are On.Select the Billing Document Request you created previously and choose Create Billing Documents.Enter the following data and choose OK:Billing Type: Invoice(CI01)Billing Date: <Today> | In the Items table, there are two entries, one for Fixed Priced item, the other for down payment. |  |
| 12 | Check the Billing Element | Back to Manage Project Billing (F4374) app to check the displayed amount. | The Down Payment Received is now 0, and Billed is 100000 EUR. |  |
| 13 | Billing for Time and Expense Item | Repeat step 5 to 11 for Time and Expense billing element item, here record time for 1 H, Clear journal entry and book account receivable with Allocated Amount no more than down payment request +tax, here suppose the output tax is 19%. Amount=5000 (1+19%)=5950 EURCheck the billing element in Manage Project Billing (F4374) app. | After time recording, To Bill is 10000 EUR.After creating down payment billing document request, the Down Payment Requested is 5000 EUR.After posting incoming payment, the Down Payment Requested is 0, Down Payment Received is 5000 EUR.After creating invoice for Time and Expense item, Down Payment Received is 0, and Billed is 10000 EUR. |  |

### Schedule Repricing for Projects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this app, you (as a billing specialist) can schedule recalculation of the billing amounts when:

- The sales rate changes
- There is a change in material configuration leading to a change in sales rate
- The To Bill amount is not reflected correctly in the Manage Project Billing app due to errors

This process step shows you how to create a customer invoice. The invoices and journal entries are created in finance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Specialist - Projects. | The SAP Fiori launchpad displays. |
| 2 | Access the App | Open Schedule Repricing for Projects (F4422). | A list of application jobs displays. |
| 3 | Create Billing Creation Schedule | Choose Create to define a new billing job. | A new screen displays. |
| 4 | Template Selection | Job Template: Schedule Price Changes for Billing ElementsThen choose Step 2. |  |
| 5 | Scheduling Options | Start Immediately: selector you may define Start time of the job, and Recurrence Pattern.Then Choose Step 3. |  |
| 6 | Parameters | Define parameters like Customer, Project, Service Organization for the billing items to be included in the batch job, then choose Check. | The system displays the messageYou can go ahead and schedule the job. |
| 7 | Schedule Options | Choose Schedule. | A billing creation job is scheduled. |
| 8 | Check Application Job Log | Go back to the list of application jobs where the new job displays. |  |

### Manage Workflows for Project Billing Requests (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Managers can use workflows to approve or reject Project Billing Requests (PBR). This step shows how to create workflows for write-off scenario.

|  |
| --- |
| Note You can use app Manage Project Billing - Project Billing Request (F6545) to check the status of Project Billing Requests. To make your billing element visible in Manage Project Billing - Project Billing Request (F6545), open app Plan Customer Projects (F0719) and assign user Billing Specialist - Projects as a business partner according to the following instructions:Find the Business Partner ID by choosing the Search icon in the upper right of the screen. Select Employee-Workforce from the dropdown list, enter Billing Specialist - Projects, and choose Search.On the Plan Customer Projects (F0719) screen, navigate to Information tab, Responsibility section, and choose Add Project Role.In Business Partner, assign a project role with the Business Partner ID which is found in the previous step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |
| 2 | Access the App | Open Manage Workflow for Project Billing Requests (F5980), and choose Create. | The New Workflow screen displays |
| 3 | Set Parameters | On the New Workflow screen, navigate to Header and make the following entry:Workflow Name: <PBR>Navigate to Properties and make the following entries:Valid From: <Jan 1st of this year>Valid To: <Dec 31st of this year>Navigate to Start Conditions, under Only start the workflow if all of the following preconditions are met:, make the following entries:Revenue to write off in the project billing request is greater than: <20> AEDNote You can also create combined conditions by choosing Create Alternative Preconditions. |  |
| 4 | Create Workflow Steps | Navigate to Steps and choose Create. On the New Step screen, navigate to Recipients, and make the following entries:Assignment By: select RoleRole: select Project ManagerStep to be completed by: choose One of the recipientsChoose Create, then choose Save, and choose Activate. | The workflow for project billing requests has been created and activated. |
| 5 | Create Billing for an On Account Payment Item | Please refer to [Billing For Time and Expense Item](#unique_11) [page ] 12 to write off billing element item quantity. | After choosing Submit, you receive a success information that The project billing request 10xxxxxxxx is sent for approval. |
| 6 | Reject the Project Billing Request | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services.Open app My Inbox - All Items (F0862). In All Tasks pane, select Release Project Billing Request 10xxxxxxxx, and choose Reject.A Submit Decision window pops up, where you can create a decision note. Then choose Submit. | The PBR is rejected.The requester receives a rejection notification. |
| 7 | Check the Project Billing Request Status | Log on to the SAP Fiori launchpad as a Billing Specialist - Projects.Open app Manage Project Billing - Project Billing Request (F6545). On the Manage Project Billing Requests screen, search the rejected Project Billing Request ID and check Status. | The status is Rejected. |
| 8 | Recreate Billing for On Account Payment Item | Repeat step 5 to write off billing item Quantity. On the Prepare Billing screen, you can see the rejected item back to the To Bill column. | After choosing Submit, you receive a success information that The project billing request 10xxxxxxxx is sent for approval. |
| 9 | Approve the Project Billing Request | Open app My Inbox - All Items (F0862). In the All Tasks pane, select the entry Release Project Billing Request 10xxxxxxxx, and choose Release.A Submit Decision window pops up, where you can create a decision note. Then choose Submit. | The PBR is approved, and a billing document request is created. |
| 10 | Check the Project Billing Request Status | Log on to the SAP Fiori launchpad as a Billing Specialist - Projects.Open Manage Project Billing - Project Billing Request (F6545). On the Manage Project Billing Requests screen, search the approved Project Billing Request ID and check Status. | The status is Billing Requested. |
| 11 | Check the Billing Document Request Status | Open app Manage Project Billing (F4374). Check the billing element for Written Off amount | Written Off amount is increased accordingly. |

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
- see-also :: [[14-maintenance-service-and-projects/test-script-time-recording-project-based-services-j12-ae-1297]]
- see-also :: [[14-maintenance-service-and-projects/test-script-project-control-intercompany-4au-ae-sap-s-4hana-cloud-publ]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4E9_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 52,860 chars in the whole document
