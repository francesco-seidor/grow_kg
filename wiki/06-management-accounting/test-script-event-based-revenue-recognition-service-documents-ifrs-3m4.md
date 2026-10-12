---
id: 06-management-accounting/test-script-event-based-revenue-recognition-service-documents-ifrs-3m4
title: "Test Script: Event-Based Revenue Recognition – Service Documents – IFRS (3M4_AE) (3M4_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 3M4_AE: event-based revenue recognition on service contracts/orders (IFRS), prerequisites, steps, settlement."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/ebrr-for-service-documents]
aliases: [3M4_S4CLD2608_BPD_EN_AE]
keywords: [Event-Based Revenue Recognition for Service Documents, event-based revenue recognition, service documents, test scripts, revenue recognition run, revenue recognition issues, revenue recognition reversal, settlement rules, recognition key derivation, substitution and validation rules]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3M4_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-959
topic: 06-management-accounting/ebrr-for-service-documents
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Event-Based Revenue Recognition – Service Documents – IFRS (3M4_AE) (3M4_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3M4_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Event-Based Revenue Recognition for Service Documents** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Event-Based Revenue Recognition – Service Documents – IFRS (3M4_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232853301)

[2 Prerequisites 4](#_Toc232853302)

[2.1 System Access 4](#_Toc232853303)

[2.2 Roles 4](#_Toc232853304)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232853305)

[2.4 Business Conditions 5](#_Toc232853306)

[2.5 Preliminary Steps 6](#_Toc232853307)

[2.5.1 Set Report Relevancy 6](#_Toc232853308)

[2.5.2 Replicate Runtime Hierarchy 7](#_Toc232853309)

[2.5.3 Maintain Settings for Event-Based Revenue Recognition 8](#_Toc232853310)

[2.5.4 Check and Update Derivation of Recognition Key for Service Documents 9](#_Toc232853311)

[2.5.5 Manage Substitution and Validation Rules for Service Documents 10](#_Toc232853312)

[2.5.6 Settlement Rule 11](#_Toc232853313)

[3 Overview Table 13](#_Toc232853314)

[4 Test Procedures 14](#_Toc232853315)

[4.1 Monitor Revenue Recognition (Event-Based): Service Documents 14](#_Toc232853316)

[4.2 Manage Real-Time Revenue Recognition Issues 15](#_Toc232853317)

[4.3 Run Revenue Recognition: Service Document (Period-End Activity) 16](#_Toc232853318)

[4.4 Manage Revenue Recognition Issues – Service Document 17](#_Toc232853319)

[4.5 Review Service Order Actuals 18](#_Toc232853320)

[4.6 Optional: Revenue Recognition Reversal 18](#_Toc232853321)

[5 Appendix 19](#_Toc232853322)

[5.1 Reverse Month-End Revenue Recognition Postings 19](#_Toc232853323)

[5.2 Optional: Maintain Settlement Rule for Service Document 20](#_Toc232853324)

[5.3 Optional: Settlement of Service Order/Contract 22](#_Toc232853325)

## Purpose

Overview

Event-Based Revenue Recognition allows you to manage revenue recognition for service contracts and service orders, using group ledger IFRS functionality. For a service contract, revenue is recognized over time based on the billing plan of the service contract item. For a service order, revenue is recognized based on an event, such as the completion of a service order, and the associated cost is recognized in the same period in which the revenue is recognized. Manual adjustments of revenue and costs are possible. In the Service Actuals app, revenue and costs on service documents are reported in real time and the margin can be easily analyzed. If necessary, period-end closing corrects real-time revenue recognition postings.

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
| Cost Accountant - Sales | SAP_BR_SALES_ACCOUNTANT | Sales Accounting | SAP_BR_SALES_ACCOUNTANT |  |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Controlling area | A000 | Controlling Area A000 |  |
| Company code | 3310 | Company Code 3310 |  |
| Service Organization | 3310 | Service Org 3310 |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met. These steps below provide the source of the revenue recognition.

| Scope Item | Business Condition |
| --- | --- |
| 3MO - Service Contract Management | The service contract must be created and a periodic billing plan assigned.The service contract must also be in the released satus. |
| 3D2 - Service Order Management and Monitoring | Costs on the service contract are posted via service order. |
| 1GA - Accounting and Financial Close – Group Ledger IFRS | You must select and activate this scope item. |
| 3M3 - Event-Based Revenue Recognition – Service Documents | You must select and activate this scope item. |

### Preliminary Steps

#### Set Report Relevancy

Purpose

Report relevancy must be done when you execute any reports for the first time. If you make a subsequent change in cost center, profit center, or G/L hierarchy, perform this step again to get the latest information.

Also, you must manually replicate set-based hierarchies (such as Cost Center Group or Profit Center Group) and financial statement hierarchies to the backend database hierarchy tables. Normally, this would be created as a periodic job that would run in the background.

Procedure

| Step # | Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Set Report Relevancy - Set-Based Hierarchies (F5295). | The Set Report Relevancy for Set-Based Hierarchies screen displays. |  |
| 3 | Enter Header Data | Make the following entries and choose Go:Set Class: For example,0101, for the cost center groupOrganizational Unit: A000Set Name: A000Include Subnodes: Yes |  |  |
| 4 | Mark as Report Relevant | In the Set Report Relevancy section, select the row and choose Edit. In the dialog box, make the following entries:Report Relevant: Yes |  |  |
| 5 | Save | Choose Save.Note If you are using the optional procedure Commitment Management and Cost Center Budgeting, repeat steps 1-5 with the following entries instead:Set Class: 0102Organizational Unit: YCOASet Name: YBA000_CEInclude Subnodes: <Select> | Set updated message displays. |  |

#### Replicate Runtime Hierarchy

Purpose

You must manually replicate set-based hierarchies (such as Cost Center Group or Profit Center Group) and financial statement hierarchies to the backend database hierarchy tables. Normally, this would be created as a periodic job that would run in the background.

Procedure

| Step # | Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Overhead Accounting Jobs (F3767). | The Application Jobs screen displays. |  |
| 3 | Create | Choose the Create button. | The New Job: Replicate Runtime Hierarchy (SAP) view displays. |  |
| 4 | Header Data for Hierarchy ID 0101/A000/A000 | In the header area, make the following entries and choose Schedule:Job Template: Replicate Runtime Hierarchy (SAP)Job Name: <Enter a text>Choose the Step 2 button.Start Immediately: SelectChoose the Step 3 button.In the Create Hierarchy area, make the following entry:Hierarchy ID: 0101/A000/A000Note If you are using the optional procedure Commitment Management and Cost Center Budgeting, follow steps 1-4, but make the following entries instead:Job Template: Manually Replicate Runtime HierarchyHierarchy ID: 0102/YCOA/YBA000_CE |  |  |
| 5 | Hierarchy ID YPS2 | Repeat the above steps using hierarchy ID YPS2. |  |  |

#### Maintain Settings for Event-Based Revenue Recognition

Purpose

In the activity, you can check and update configuration of recognition key for project-based sales documents.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Profitability Analysis

1. For the row with Item Name of Revenue Recognition, choose Details (>).
2. For the displayed row, choose Details (>).
3. For the Maintain Settings for Event-Based Revenue Recognition row, choose Configure.
4. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration (CBC).
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Maintain Settings for Event-Based Revenue Recognition activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Add/Change Entry for Recognition Key | In this configuration step, you can add G/L to predelivered sources based on your business needs.You can also update the assignment rule with the necessary G/L.For more information, see the notes below. |  |  |

|  |
| --- |
| Note CBC only: You can create your own revenue sources with names starting with Z and assign them to the provided assignment rules using customer sequence numbers that start with 1000. Additionally, you can configure the extra P&L and Balance Sheet accounts for revenue/cost adjustments and accrued/deferred revenue. Ensure that the custom source is only assigned to usage 100: Revenue for Revenue Recognition Processing. You must also add usage 400: Currency Result and usage 401: Currency Valuation to the custom source, as well as usage 103 if the default revenue source is assigned with these usages. |

|  |
| --- |
| Note CBC only: Avoid assigning the same G/L account to two source lines. When assigning a source to the assignment rule, the system ensures that no other source is already assigned that would derive the same G/L account. If this condition is met, the assignment is forbidden. During transaction processing, the assignment rule evaluates each source sequence sequentially, regardless of the source's nature (for example, revenue versus cost). Once a G/L account is determined, the process stops and proceeds with the identified source. |

#### Check and Update Derivation of Recognition Key for Service Documents

Purpose

In the activity, you can check and update derivation of recognition key for service documents.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Profitability Analysis

1. For the row with Item Name of Revenue Recognition, choose Details (>).
2. For the displayed row, choose Details (>).
3. For the Derivation of Recognition Key for Service Documents row, choose Configure.
4. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Derivation of Recognition Key for Service Documents activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Add/Change Entry for Required Item Category | Choose the New Entries button and make the following entries:Company Code: <enter your company code>Item Category: <for example, SCN1>Material : <for example, *>Note Keep material as * if the same RA key is valid for all the materials.Recognition Key: <for example, CCOCC or CCS>Save the entries. | The following item categories are supported in event-based revenue recognition. Based on your activated service and contract scope and business requirements, you must ensure that the derivation is set for all used item categories.The allowed item categories for:Periodic Service Contracts: SCN1, SCN2, and SCN3.Service Orders: SEW1, SEW2, SEW5, SVB4, SVB6, SVE1, SVE2, SVE5, SVP1, SVP2, SVP5, SVR1, SVR2, SVR5, SVS1, SVS2, SVS5, SVE6, SVP6, SVR6, and SVB7.Note Service Orders RA key is represented by RecKeyArea 500.Periodic Service Contracts RA keys is represented by RecKeyArea 400.Note The new key NONREV - Universal No Rev Rec is now available for use across the RA key area. This generic non-revenue recognition key represents method 2 for all scenarios supported by Event-Based Revenue Recognition. |  |

#### Manage Substitution and Validation Rules for Service Documents

Purpose

In this activity, you can display, create, and change substitution and validation rules for your selected business contexts and events for service documents. These rules can be used in the respective business processes to validate, derive, or replace values at the time of entry for the relevant fields.

Key Features

The app provides the following key features:

- Create Validation Rules
- Create Substitution Rules
- Change Rules
- Display Rules

Procedure

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Substitution/Validation Rules - Service Documents app.
3. Check and adopt the following default derivation rules according to your business requirements:

Table 1:

| Derivation Rule | Default Rule |
| --- | --- |
| Costing Sheet | The default rule is /0SAP/SV_COSTING_SHEET (SAP default Costing sheet derivation) with costing sheet SV001. You can also create your own substitution rule for costing sheet derivation.Note You need to update the costing sheet SV001 via configuration activity Define Costing Sheets with your required master data. You can also create your own costing sheet and add it to the substitution rule you create according to your business needs. |
| Functional Area Rule | The default rule is /0SAP/SV_FUNCTIONAL_AREA (SAP default Functional area derivation) with functional area YB25. You can also create your own substitution rule for functional area derivation.Note You can also create your own functional area via configuration activity Manage Functional Areas and add it to the substitution rule as per your business needs. |
| Profit Center Rule | There is no default rule provided for profit center derivation. You can define it according to your business requirements.Note The system first determines the cost center of the employee responsible for the item and then the profit center that is defined for this cost center. If no profit center is defined for the cost center, the system uses the dummy profit center defined for the controlling area. You can also manually change the profit center assigned to a service transaction item. Once you have made such a manual change, the system no longer redetermines the profit center if you change the employee responsible. |
| Settlement Rule | The default rule is /0SAP/SV_SETTLEMENT_PROFILE (SAP default Settlement Profile derivation) with settlement profile YNS (Not for Settlement). You can also create your own substitution rule for settlement. All default orders have settlement rule YNS (Not for Settlement). You can settle service order/contract to WBS element or another service order/contract in addition to other cost objects like cost center. We provide default settlement profile YSRV01- Settlement Service. You must create your own settlement rule via substitution or assign settlement profile directly to service order or contract.Note Settlement is possible only for service order/contract with revenue recognition inactive, inactive means either revenue recognition key with method 2 or blank. If‘revenue recognition is active, then settlement profile YNS ‘No Settlement’ would be assigned (instead of calling the SubValTool). |

|  |
| --- |
| Note Every rule needs to be activated. |

#### Settlement Rule

The default rule is /0SAP/SV_SETTLEMENT_PROFILE (SAP default Settlement Profile derivation) with settlement profile YNS (Not for Settlement). You can also create your own substitution rule for settlement.

All default orders have settlement rule YNS (Not for Settlement).

You can settle WBS element or another service order/contract In settlement of service order/service contract to other cost objects like cost center, WBS element or another service order/contract is possible. SAP provides default settlement profile YSRV01- Settlement Service. You must create your own settlement rule via substitution or assign settlement profile directly to service order or contract.

|  |
| --- |
| NoteSettlement is possible only for service order/contract with revenue recognition inactive, inactive means either revenue recognition key with method 2 or blank.If‘revenue recognition is active, then settlement profile YNS ‘No Settlement’ would be assigned (instead of calling the SubValTool). |

## Overview Table

The scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report or Item | Business Role | App Name | Expected Results |
| --- | --- | --- | --- |
| [Monitor Revenue Recognition (Event-Based): Service Documents](#unique_14) [page ] 14 | Cost Accountant - Sales | Event-Based Revenue Recognition - Service Documents (F6007) | Contract documents are reviewed. |
| [Manage Real-Time Revenue Recognition Issues](#unique_15) [page ] 15 | Cost Accountant - Sales | Manage Real-Time Revenue Recognition Issues (F4101) | Issue such as cost/revenue posting with no real time posting are reviewed. |
| [Run Revenue Recognition: Service Document (Period-End Activity)](#unique_16) [page ] 16 | Cost Accountant - Sales | Run Revenue Recognition - Service Documents (F4278). | Values for real-time revenue for service contracts are posted. |
| [Manage Revenue Recognition Issues – Service Document](#unique_17) [page ] 17 | Cost Accountant - Sales | Manage Revenue Recognition Issues - Service Documents (F4186) | Revenue recognition posting issues are reviewed and corrected. |
| [Review Service Order Actuals](#unique_18) [page ] 18 | Cost Accountant - Sales | Service Actuals (W0206) | You can view actual figures based on your selection criteria. |
| [Optional: Revenue Recognition Reversal](#unique_19) [page ] 18 | Cost Accountant - Sales | Revenue Recognition Reversal (F4869) | The document is reversed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Monitor Revenue Recognition (Event-Based): Service Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The service contract revenue can be reviewed.

|  |
| --- |
| Note RA key assigned to service contracts is CCS-Periodic Services Contracts-No Cost def. So to view any data in this app, there must either be billing done for the contract and that would post deferred revenue, or execute the [Run Revenue Recognition: Service Document (Period-End Activity)](#unique_16) [page ] 16 step to accrue revenue if no billing is done. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Event-Based Revenue Recognition - Service Documents (F6007). | The Event-Based Revenue Recognition - Service Documents view displays. |  |
| 3 | Enter Selection Criteria | Make the following entries :Service Document: <Created in scope items Service Contract Management (3MO) and Service Order Management and Monitoring (3D2)>Company Code: 3310Revenue Recognition Key: CCS |  |  |
| 4 | Execute | Choose Go. |  |  |

### Manage Real-Time Revenue Recognition Issues

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

During cost or revenue posting on the cost object, errors that stop real time revenue postings can occur. This activity allows you to review these posting entries where no corresponding real time revenue recognition posting exists and make the necessary corrections. All errors must be addressed prior to the month end revenue recognition month end process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. |  |  |
| 2 | Access the App | Open Manage Real-Time Revenue Recognition Issues (F4101). |  |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:To Fiscal Period/Year: <mm.yyyy>Company Code: 3310 | No data found indicates that there are no issues. If issues are shown, review and process corrections.Tip To download the issue list, make your filter selections and select Show Error Summary. From the list, you can choose the Download button. |  |

### Run Revenue Recognition: Service Document (Period-End Activity)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the event-based revenue recognition for service documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Run Revenue Recognition - Service Documents (F4278). | The Application Jobs view displays. |  |
| 3 | New Job | Choose the Create button. | The New Job view displays. |  |
| 4 | Enter Selection Criteria | Make the following entries and choose the Schedule button:Job Template: Run Revenue Recognition – Service DocumentsJob Name: <Enter a description or leave the default description>Choose the Step 2 button.Start Immediately: <checked>Choose the Step 3 button.Fixed Period: <mm/yyyy>ORDynamic Period: <use the dropdown to select, for example, Current Fiscal Period>Company Code: 3310Ledger: 2L | The new job is executed. |  |

### Manage Revenue Recognition Issues – Service Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Errors in the revenue recognition must be corrected.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. |  |  |
| 2 | Access the App | Open Manage Revenue Recognition Issues - Service Documents (F4186) . |  |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Reprocess to correct and/or skip errors.Fiscal Year Period: <MM/YYYY>Company Code: 3310Ledger: 2LService Document: <service documents>Note The service document is created in scope items Service Contract Management (3MO)and Service Order Management and Monitoring (3D2). | No data found indicates that there are no issues. If issues are shown, review and process corrections.Tip To download the issue list, make your filter selections and select Show Error Summary. From the list, you can choose the Download button. |  |

### Review Service Order Actuals

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the Service Contract Actual Data report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Service Actuals (W0206). | The Service Contracts - Actuals view displays. |  |
| 3 | Enter Report Criteria | Make the following entries and choose OK:Ledger Fiscal Year: <enter a fiscal year>Ledger: 2LService Document: <created in scope item 3MO>Key Date: <enter a date> | The actual figures for Service Contracts - Actuals display. |  |

### Optional: Revenue Recognition Reversal

You could reverse revenue recognition if you made an error. For information on revenue recognition reversal, see the [Reverse Month-End Revenue Recognition Postings](#unique_21) step in the Appendix section.

## Appendix

### Reverse Month-End Revenue Recognition Postings

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Occasionally, you may be required to reverse revenue recognition posts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reverse Revenue Recognition (F4869). | The Application Jobs screen displays. |  |
| 3 | Create | Choose the Create button. | The New Job: Reverse Revenue Recognition view displays. |  |
| 4 | Enter Selection Criteria | In the Template Selection section, make the following entries:Job Template: Reverse Revenue RecognitionJob Name: Reverse Revenue RecognitionChoose Step 2. | The Scheduling Options view display. |  |
| 5 | Scheduling Options | Select Start Immediately checkbox and choose Step 3. | The Parameters view display. |  |
| 6 | Parameters | Make the following entries:Posting Date: <Enter a desired date>Note This must be a month-end date. Otherwise, no selection will be returned.Company Code: 3310Ledger: <enter a ledger>Journal Entry: <Enter the document you want to reverse> | The figures for projects display. |  |
| 7 | Schedule Job | Choose the Schedule button. | The document is reversed. |  |

### Optional: Maintain Settlement Rule for Service Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the settlement rules for service order/contract settlement are maintained. SAP provides default settlement profile YSRV01- Settlement Service. You must create your own settlement rule via substitution or assign settlement profile directly to service order or contract.

Prerequisites

Cost is posted on service. Settlement is only possible when revenue recognition is inactive, inactive means either revenue recognition key with method 2 (Recognize all costs and revenues) or blank.

For service order, method 2 is CCONCC- No Rev Rec-Service Order; and for Service Contract CCSN- Periodic Services Contracts-No rev rec or blank.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Settlement Rules-Service documents (FCO_SRVDOC_STLRLSE). | The Manage Settlement Rule view displays. |  |
| 3 | Select Service Document | Select the service document that you want to settle and choose the Go-Execute button. | Service document with items opens. |  |
| 4 | Maintain Settlement Rule | In the left pane, select the Maintain settlement rules (pencil icon). | The Maintain Settlement Rule: Parameters screen appears. |  |
| 5 | Enter Settlement Profile | Enter settlement profile YSRV01 and press Enter.Note Allocation structure YSERV and source structure YY are defaulted.Choose Save. | The Maintain Settlement Rule: Overview screen appears. |  |
| 6 | Enter Distribution Rules | Under the Distribution rules section, add the following:Cat: <from allowed category>Settlement Receiver:<Select the object to which you want to settle>Settlement Type: Full SettlementChoose OK.Note Settlement rules are common for all the standard ledgers and not different by Ledger. | If you use source structure YY to service, distribution rules by each source is possible and you can select the source line ID in such cases.. |  |
| 7 | Save | Choose Enter and go back to save the entries. |  |  |

### Optional: Settlement of Service Order/Contract

Purpose

The settlement transfers the costs from service order/contract to cost object (cost center, WBS, service order or contract) as specified in the settlement rules.

Prerequisites

- Settlement is only possible when revenue recognition is inactive, inactive means either revenue recognition key with method 2 (Recognize all costs and revenues) or blank.
- Check and update cost element group, for example, COST is assigned to allocation structure YSERV and Source Structure YY.
- Settlement is via secondary cost element, for example, 92105300- Other costs (with category 21) are mapped in Allocation structure YSERV.
- If you settle to WBS (Project, service order/contract) and want this settled amount to be considered for revenue recognition in receiving object, make sure you map the settlement GL example 92105300 - other costs in source of receiver object revenue recognition via configuration activity Event-Based Revenue Recognition.
- The secondary G/L mapped is FSV YPS2 so that it is reflected correctly in project (receiver object) reporting.

|  |
| --- |
| Note This step must be performed for each Ledger individually, settlements are run by Ledger. Repeat these steps for any additional standard ledger such as 2L or 3L that you may have for parallel settlement. |

Procedure

| Step # | Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as either Cost Accountant - Overhead. |  |  |
| 2 | Access the SAP Fiori App | Oen Schedule Overhead Accounting Jobs (F3767). | The Application Jobs screen displays. |  |
| 3 | Create | Choose the Create button. | The New Job screen displays. |  |
| 4 | Template Selection | In the header area, make the following entries and choose Step 2:Job Template: <Select Actual Settlement: Service Documents (SAP)>Tip Delete the entry to see all the job templates available.Job Name: Actual Settlement: Service Documents (SAP) |  |  |
| 5 | Scheduling Options | Make the following entries and choose Step 3:Start Immediately: Select |  |  |
| 6 | Parameters | In the Parameter Section, make the following entries and choose Check to validate your entries:ParametersSettlement Period: <enter current period, for example 002>Settlement Year: <enter the year>Ledger: <for example, 0L or your lead ledger>Note With parallel settlement rule, Lead Ledger only settles to Lead Ledger and you would require additional jobs for Ledger 2L or 3L.Service DocumentsService Document Item: <Enter a service order that you want to settle for while the rule is defined>Processing OptionsActual Settlement: SelectTest Run: Deselect | A message that you can go ahead and schedule the job appears if the check is successful, else make the required corrections. |  |
| 7 | Schedule | Once the check is successful, choose Schedule. | The job is scheduled. |  |

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
- related-to :: [[06-management-accounting/event-based-revenue-recognition-service-documents-us-gaap-3m5-ae-960]]
- related-to :: [[06-management-accounting/test-script-event-based-revenue-recognition-service-documents-3m3-ae-9]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3M4_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 39,195 chars in the whole document
