---
id: 14-maintenance-service-and-projects/test-script-corrective-maintenance-bh1-ae-sap-s-4hana-cloud-public-edi
title: "Test Script: Corrective Maintenance (BH1_AE) - SAP S/4HANA Cloud Public Edition (BH1_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item BH1 corrective maintenance: roles, sample data, Fiori apps and step-by-step procedures from request to technical completion."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/corrective-and-emergency-maintenance]
aliases: [BH1_S4CLD2608_BPD_EN_AE]
keywords: [Corrective and Emergency Maintenance, corrective maintenance, maintenance notifications, maintenance orders, test scripts, business roles, service entry sheets, maintenance order confirmation, flexible workflow approval, purchase orders]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BH1_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1266
topic: 14-maintenance-service-and-projects/corrective-and-emergency-maintenance
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Corrective Maintenance (BH1_AE) - SAP S/4HANA Cloud Public Edition (BH1_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BH1_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Corrective and Emergency Maintenance** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Corrective Maintenance (BH1_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232861610)

[2 Prerequisites 4](#_Toc232861611)

[2.1 System Access 4](#_Toc232861612)

[2.2 Roles 4](#_Toc232861613)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232861614)

[2.4 Business Conditions 6](#_Toc232861615)

[3 Preliminary Steps 8](#_Toc232861616)

[3.1 Initializing Material Stock 8](#_Toc232861617)

[3.2 Maintain Cost Rates 9](#_Toc232861618)

[3.3 Create Purchasing Info Record 10](#_Toc232861619)

[4 Overview Table 13](#_Toc232861620)

[5 Test Procedures 15](#_Toc232861621)

[5.1 Request Maintenance 15](#_Toc232861622)

[5.2 Monitor Maintenance Requests 16](#_Toc232861623)

[5.3 Change Maintenance Request into Malfunction Report 17](#_Toc232861624)

[5.4 Optional - Create Maintenance Notification 18](#_Toc232861625)

[5.5 Create Maintenance Order 19](#_Toc232861626)

[5.6 Release Maintenance Order 22](#_Toc232861627)

[5.7 Convert Purchase Requisitions to Purchase Orders 23](#_Toc232861628)

[5.8 Post Goods Receipt for Purchase Order 25](#_Toc232861629)

[5.9 Maintain Service Entry Sheet 26](#_Toc232861630)

[5.10 Approve Service Entry Sheet with Flexible Workflow (Optional) 28](#_Toc232861631)

[5.11 Create Supplier Invoice with PO/GR Relation 29](#_Toc232861632)

[5.12 Confirm Maintenance Order 31](#_Toc232861633)

[5.13 Show Costs on Maintenance Order 33](#_Toc232861634)

[5.14 Technically Complete Maintenance Order 33](#_Toc232861635)

[5.15 Review Asset Maintenance Object Pages 35](#_Toc232861636)

[6 Appendix 36](#_Toc232861637)

[6.1 Process Integration 36](#_Toc232861638)

[6.1.1 Preceding Processes 36](#_Toc232861639)

[6.1.2 Succeeding Processes 36](#_Toc232861640)

## Purpose

Overview

This scope item allows you to perform the corrective maintenance of technical objects whenever a breakdown or failure occurs. The plant maintenance component provides a comprehensive notification and order system to facilitate this process. You can process a repair using several planning stages, such as preliminary costing, work scheduling, material provisioning, and resource planning. You can also react immediately to issues that may lead to the shutdown of production facilities. When this becomes necessary, you can create the required maintenance orders and shop papers with minimum entries in the shortest possible time.

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

| Name (Role Template) | ID (Role Template) | Name (Space) | ID (Space) | Log On |
| --- | --- | --- | --- | --- |
| Maintenance Planner | SAP_BR_MAINTENANCE_PLANNER | Maintenance Planning | SAP_BR_MAINTENANCE_PLANNER |  |
| Maintenance Technician | SAP_BR_MAINTENANCE_TECHNICIAN | Maintenance Execution | SAP_BR_MAINTENANCE_TECHNICIAN |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Purchaser | SAP_BR_PURCHASER |  |  |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Employee | SAP_BR_EMPLOYEE | Self Services / Self Services / Employee Overview Space | SAP_BR_EMPLOYEE / SAP_CA_SPT_EMPLOYEE_CROSS_PC / SAP_EAM_SPT_EMPLOYEE_PC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Project Manager - Commercial Services | SAP_BR_PROJ_MANAGE_COMM |  |  |  |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT |  |  |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company is created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. You can also use the following sample data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Equipment | 233100091 | Cooling Water Circulation Pump |  |
| Equipment | 233100093 | Cooling Water Circulation Pump |  |
| Spare Parts Material | SP001 | Bearing |  |
| Spare Parts Material | SP002 | Coupling |  |
| Spare Parts Material | SP003 | Shaft |  |
| Spare Parts Material | SP004 | Gaskets 1mm |  |
| Spare Parts Material | SP005 | Mechanical Seal |  |
| Spare Parts Material | SP006 | Spur gear IS651 |  |
| Non-stock Material | NL001 | Screw |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331B | Std. storage 2 |  |
| Supplier | 33300001 | Domestic UAE Supplier 1 |  |

Bill of Material Structure

This overview shows the bill of material structure and the usage of each component if you have activated all optional enhancements.

| Material | Level | Material Type | Unit | Characteristics of Material | Optional Enhancements |
| --- | --- | --- | --- | --- | --- |
| 233100091 | 0 | Equipment | PC | Cooling Water Circulation Pump |  |
| SP001 | 1 | ERSA | PC | Bearing |  |
| SP002 | 1 | ERSA | PC | Coupling |  |
| SP003 | 1 | ERSA | PC | Shaft |  |
| SP004 | 1 | ERSA | PC | Gaskets 1mm |  |
| SP005 | 1 | ERSA | PC | Mechanical Seal |  |
| SP006 | 1 | ERSA | PC | Spur gear IS651 |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

Table 1:

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. The posting period is up to date.To run through this scope item, the materials must be available in stock. |

## Preliminary Steps

### Initializing Material Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In a real business case, the materials are usually purchased from external suppliers. In this case, the process is covered by the standard purchasing or subcontracting processes. This process step shows you how to post initial stock directly to the storage locations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Input Material | Make the following entries and choose Enter:Material: < material number>. Select one of the Spare Parts Material mentioned in the previous section Master Data, Organizational Data, and Other Data.Plant: Plant 1 AE (3310) |  |  |
| 4 | Select Stock | Select the icon beside the stock that you want to add initial stock, for example:Storage Location: Std. storage 2 (331B)Unrestricted-Use Stock | A dialog box opens. The Storage Location, Stock Type and Current Quantity display according to your entries in the previous steps. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Document Date: <today>Posting Date: <today>Stock Change: initial entryQuantity: <quantity number> | The system displays Material document XXX created. The stock has been added. |  |

### Maintain Cost Rates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can maintain, check and update the actual cost rates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori Launchpad asCost Accountant - Overhead | The launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Cost Rates - Plan (F3162) | The app opens. |  |
| 3 | Check Actual Cost Rates | Make the following entries in filtering section and choose Go.Valid On: TodayCost Center: 33101701Activity Type: 11Currency: for example, AEDCheck if there is a valid cost rate for given cost center, activity type, and period. | The actual cost rates for given cost centre, activity type and period are checked for valid values.Note You can skip the next step if there is a valid cost rate for given cost center, activity type, and period. |  |
| 4 | Maintain Actual Cost Rates | Choose Add and make the following entries:Cost Center: 33101701Activity Type: 11From Fiscal Year: Current YearFrom Period: Current PeriodFixed Rate: 100Currency: for example, AEDPer:1Activity Unit: HChoose Save. | Cost rates are created. |  |

### Create Purchasing Info Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to create the info records for materials, for example, NL001 and choose a valid supplier (for example, 33300001).

This step is obsolete if the necessary info records are present. Check the info records supplier 33300001, material NL001 and Purchasing Organization 3310. The existing info records for this material are displayed on the screen.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records screen displays. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record screen is displayed. |  |
| 4 | Enter Header Data | Enter the following:Purchasing Info Record Category: StandardPurchasing Organization: 3310Supplier: 33300001Material: NL001Plant: 3310Purchasing Group: 001 | Header data is added. |  |
| 5 | Enter General Information | Enter General InformationAvailable From: TodayAvailable To: 12/31/9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | Enter the following:Incoterm: EXWIncoterm Location 1: Vendor | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Enter the following:Delivery Time in Days: <XX Days>, for example, 1Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10.0Tax Code: Enter the tax code.Order Unit: PCStandard Order Quantity: <Standard Order Quantity>, for example, 10 | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | Go to the Conditions area, choose the Create icon. Enter the following data:Valid From: <Valid from Date>Amount: <Amount>, for example, 1Pricing Unit: <Pricing Unit>, for example, 1Valid To: <Valid to Date>Currency: <Currency>, for example, AEDChoose Apply. | Condition Data is added |  |
| 9 | Enter Reference Data (optional) | You can enter reference data. | Reference data is added. |  |
| 10 | Save Your Data | Choose Save. | A purchasing info record is saved. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Request Maintenance](#unique_11) [page ] 15 | Employee | Request Maintenance (F1511) | Malfunction report for an asset is created. |
| [Monitor Maintenance Requests](#unique_12) [page ] 16 | Employee | Monitor Maintenance Requests (F1511) | Check if a malfunction report already exists. |
| [Change Maintenance Request into Malfunction Report](#unique_13) [page ] 17 | Maintenance Planner | Find Maintenance Notification (F2071) | Notification type is changed. |
| [Optional - Create Maintenance Notification](#unique_14) [page ] 18 | Maintenance Technician | Create Maintenance Notification (EAMS_WDA_ORDNTF_OIF (EAMS_WDA_ORDNTF_OIF_CFG)) | Malfunction report for an asset is created. |
| [Create Maintenance Order](#unique_15) [page ] 19 | Maintenance Planner | Change Maintenance Notification | Maintenance order is created for the malfunction report. |
| [Release Maintenance Order](#unique_16) [page ] 22 | Maintenance Planner | Find Maintenance Orders - Completion (F2175) | Maintenance order is released for execution. |
| [Convert Purchase Requisitions to Purchase Orders](#unique_17) [page ] 23 | Purchaser | Process Purchase Requisitions - Deprecated (F1048) | Purchase requisitions are converted to purchase orders. |
| [Post Goods Receipt for Purchase Order](#unique_18) [page ] 25 | Warehouse Clerk | Post Goods Movement (MIGO) | Goods receipt is posted. |
| [Maintain Service Entry Sheet](#unique_19) [page ] 26 | Purchaser | Manage Service Entry Sheets - Lean Services (F2027) | The service entry sheet is created. |
| [Approve Service Entry Sheet with Flexible Workflow (Optional)](#unique_20) [page ] 28 | Project Manager - Commercial Services | My Inbox | The service entry sheet is posted. |
| [Create Supplier Invoice with PO/GR Relation](#unique_21) [page ] 29 | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) | Supplier invoice is posted. |
| [Confirm Maintenance Order](#unique_22) [page ] 31 | Maintenance Technician | Perform Maintenance Jobs (F5104A) | Maintenance order is confirmed, work time is recorded, and used material is recorded. |
| [Show Costs on Maintenance Order](#unique_23) [page ] 33 | Maintenance Planner | Display Maintenance Order | Costs of confirmed maintenance order are calculated. |
| [Technically Complete Maintenance Order](#unique_24) [page ] 33 | Maintenance Planner | Find Maintenance Orders - Completion (F2175) | Maintenance order is technically completed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Request Maintenance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Notification is created in multiple ways. This process step shows you how to use Request Maintenance by employee.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Employee. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Request Maintenance (F1511). | The Request Maintenance screen displays. |  |
| 3 | Enter Details | On the Notification screen, make the following entries:Technical Object: 233100091You can also search for an object by plain text. Use the value help button and provide a keyword, such as water pump. In the result list, select the equipment with number 233100091, a description of Cooling Water Circulation Pump, and Maintenance Planning Plant 3310.Type: M1 (Maintenance Request)Description: Enter description of malfunction. Choose hyper link Use Template, and input detailed description in Long Text field. | Notification entries are checked. |  |
| 4 | Add Attachment/URL (Optional) | On the Attachments area, choose Upload and select JPG or PNG file to upload. | Picture or photo is uploaded to your notification. |  |
| 5 | Save | Choose Submit. | Notification 100000XX savedPlease note down the Notification Number for following steps. |  |

### Monitor Maintenance Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The employee is able to check all existing notifications. This process step shows you how to check the list of existing notifications.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Employee. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Maintenance Requests (F1511). | The List of Notifications screen displays. |  |
| 3 | Search for Notification | On the List of Notifications screen,Choose Filters. Make the following entries:Technical Object: 233100091 .Choose Go.Note If you cannot see the Technical Object field, choose More Filters to add it. |  |  |
| 4 | Review Maintenance Request | Select Notification Number created at previous step and review. |  |  |

### Change Maintenance Request into Malfunction Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A malfunction report describes a malfunction on a maintenance object that may impair object performance. The malfunction report states that a technical system is not functioning correctly or working as well as it should (or not working at all).

Notification type can be adjusted according to the configuration setting. This process step shows how the Maintenance Planner can change maintenance notification type from maintenance request into a malfunction report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Maintenance Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Find Maintenance Notification (F2071). | The Maintenance Notification screen displays. |  |
| 3 | Search for Notification Number | On the Maintenance Notifications screen, make the following entries in the Standard Search area:Notification: <Enter the Maintenance Request Number 1XXXXXXX you created in the previous step>And choose GO.Choose the notification line that you created in the previous step. |  |  |
| 4 | Navigate to Change Maintenance Notification | Click on the Description underlined text, and choose Change Maintenance Notification. | Change Maintenance Notification hyperlink is displayed. |  |
| 5 | Change Notification Type | On the Change Notification: 1XXXXXXX screen, choose Additional Functions and select Change Notification Type from dropdown list.On the Change Notification Type Dialog box, select Notification Type as: Malfunction Report M2 and choose OK. | The notification type is changed. |  |
| 6 | Save | Choose Save. | Notification 1XXXXXXX is saved. |  |

### Optional - Create Maintenance Notification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how a Maintenance Technician is able to directly create a Maintenance Notification using a dedicated Application for this.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Maintenance Notification (EAMS_WDA_ORDNTF_OIF (EAMS_WDA_ORDNTF_OIF_CFG)). | The Create Notification screen displays. |  |
| 3 | Choose Notification Type | On the Create Notification screen, make the following entries:Notification Type: Malfunction Report M2Choose Continue. | The Create Notification: %XXXXXXXX.XXX screen displays. |  |
| 4 | Enter Details | On the Create Notification: %XXXXXXXXXXX screen, go to the General Data tab and make the following entries:Description: Enter description of malfunctionPriority: 1-Very high 1Technical Object: 233100091Choose Check Entries in the upper left corner of the screen.Note You can also search for an object by plain text. Use the value help button and provide a keyword, such as water pump. In the result list, select the equipment with number 233100091, a description of Cooling Water Circulation Pump, and Maintenance Planning Plant 3310. | Notification entries are checked. |  |
| 5 | Save | Choose Save. | Notification 1XXXXXXX is saved. |  |

### Create Maintenance Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Order processing helps you to plan maintenance tasks in greater detail, for example, those tasks from a malfunction report. You decide whether the tasks to be performed and what components (materials) you need for them.

Furthermore, the maintenance order is used to collect all costs for a maintenance task and to debit the cost center that incurred the costs using the settlement functions in the CO module (Controlling). This process step shows you how to create maintenance order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Start Search | Choose Search in the upper right area of the launchpad. | An input field is displayed. |  |
| 3 | Search Criteria | Choose dropdown list as: Maintenance Notifications and input Notification Number from previous section. |  |  |
| 4 | Display Notification Number | Choose hyper link Change Maintenance Notification. | The Change Notification: 1XXXXXXX screen is displayed. |  |
| 5 | Create Order for Notification | On the Change Notification: 1XXXXXXX screen, go to the General Data tab.In General Data area, in the Assigned Order field, choose Assign Order > Create Order for Notification.On the Create Order screen, choose Order type Corrective Maintenance YBA1, then choose OK. |  |  |
| 6 | Enter Details | On the Create Corrective Maintenance Order:%00000000001 screen, go to the General Data tab.Make the following entries:System Condition: not in operation 0 |  |  |
| 7 | Provide Estimated Costs | Go to the Costs tab. Make the following entries:Estimated Costs: <value for estimated costs of order>Note The Estimated Costs field is above the Costs table. |  |  |
| 8 | Defines the Operations to be Performed to Resolve the Malfunction | Go to the Operation Data tab. This selection brings you to the operation overview. Make the following entries in the Operations table for Operation 0010:Work: <Entry of your choice>Number of Capacities: <2>The system calculates the duration of the operation based on the time you entered in the Work field and on how many people you schedule in the Number field to perform this operation. You have now made all of the entries in the header data screen of the order. |  |  |
| 9 | Select Material | Choose line of operation 0010 and choose Materials tab at the bottom of the screen.On the Materials tab, make the following entries:Variant: Standard |  |  |
| 10 | Structure List | For a stock material:Choose Select from Structure List.On the Select Material Component screen, choose a Stock item of Item Category L (For examples: SP001).Choose OK.For a non-stock material:Make the following entries:Material: NL001Item Category: Non-stock Item NQuantity: <1>Plant: 3310Purchasing Org: 3310G/L Account: 61002000Note To duplicate a material line in the list with all item data, choose Copy Material. You can then change specific fields in the copied line. |  |  |
| 11 | Add Services | Choose line of operation 0010 and choose services tab at the bottom of the screen.Service without Service MaterialMake the following entries:Description : Service Material 01Quantity: <1>Unit:<H>Plant: 3310Price: Entry of your choicePurchasing Org: 3310Purchasing Group: 001Supplier33300001G/L Account: 65008000Material Group: YBMM01Note You can choose Settings button to add or remove fields in the screen.Note This case does not apply for Brazil because Tax as a Service (TaaS) uses codified service only to calculate taxes.Service with Service MaterialMake the following entries:Product: SM0001Quantity: <1> |  |  |
| 12 | Check Entries | Choose Check Entries in the upper left corner of the screen. | Entries have been checked. |  |
| 13 | Save Order | Choose Save. | Order 4000XXX is saved with Notification 1XXXXXXX.The selected stock material is reserved automatically.Note To check, log on to the SAP Fiori launchpad as a Warehouse Clerk. Open Display Stock Overview. Enter the stock material, plant, and storage location and choose Environment. Choose Reservation. |  |
| 14 | Check Purchase Requisition Number for Non-Stock Material Items | Select the row for operation 0010 and choose the Materials tab and Services tab respectively at the bottom of the screen.Make a note of the purchase requisition number for non-stock material and services in the PR Number field. | The purchase requisition number is displayed in the respective field. |  |

### Release Maintenance Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The maintenance order is used to collect all costs for a maintenance task and to debit the cost center that incurred the costs using the settlement functions in the CO module (Controlling). This process step shows you how to release maintenance order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Find Maintenance Orders - Completion (F2175). | The Maintenance Order screen is displayed. |  |
| 3 | Search for Order Number | On the Maintenance Order screen, make the following entries:Order Type: Corrective MaintenanceChoose GO.Choose the order that you created in the previous step. | Order list is displayed. |  |
| 4 | Navigate to Change Maintenance Order | Choose Related Apps at the upper right corner of the screen, and choose Change Maintenance Order. | Change Maintenance Order screen is displayed. |  |
| 5 | Set Order Status | Choose Set System Status > Release and choose Save. | The maintenance order is released. |  |
| 6 | Print Job Card | Choose Additional Functions > Print. On the next screen, select the Select All checkbox and choose OK. | The job card is printed. |  |

### Convert Purchase Requisitions to Purchase Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to assign purchase requisitions to a source of supply and to convert assigned source purchase requisitions to purchase orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Open Manage Purchase Requisitions | Open Process Purchase Requisitions - Deprecated (F1048). | The Process Purchase Requisitionsscreen displays. |  |
| 3 | Search for Purchase Requisition | On the Process Purchase Requisitions screen, make the following entries and choose Go.Plant: 3310Purchasing Group: 001Purchasing Organization: 3310 | The Purchase Requisition list displays. |  |
| 4 | Select Purchase Requisition | Select the purchase requisitions you created in the previous step.Choose the link for 1 Sources under the Assigned Supplier field. | The Select Source of Supply screen displays. |  |
| 5 | Assign Source to Purchase Requisition | On the Select Source of Supply screen. Choose a displayed source with a real price (not zero), for example, 33300001 . | The assignment of one source to the requisition is done. The Purchase Requisitions list displays. |  |
| 6 | Prepare the Purchase Order | Choose the purchase Requisition that the assigned supplier is displayed.Choose Create Purchase Order. | The Process Purchase Requisitions screen displays. |  |
| 7 | Create the Purchase Order | On Purchase Order Type, choose Standard PO and choose Save.On the pop-up screen, the system have message Standard PO created under the number 450000XXXX.Choose OK.Please note down PO number for the following steps. | The purchase order is created. |  |

### Post Goods Receipt for Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods receipt for the purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Post Goods Movement screen displays. |  |
| 3 | Enter Goods Receipt Order | Make the following entries and press Enter:First top-left frame: Goods ReceiptSecond top-left frame: Purchaser OrderOrder: <Enter the Purchase order number in the previous step>GR goods receipt: 101Choose Execute. | The GR order is entered. |  |
| 4 | Enter Date | Make the following entries:Document date: defaultPosting date: default |  |  |
| 5 | Quantity | Choose the Quantity tab. |  |  |
| 6 | Enter Quantity | Make the following entries:Qty in Unit of Entry: Enter the quantity you confirmed in the previous step. For example: 1 | The quantity is entered. |  |
| 7 | Set Item OK and Post | Select the Item OK checkbox and choose Post at the bottom of the screen. | The system displays the message Material document 500xxxxxxx posted. |  |

### Maintain Service Entry Sheet

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you report the performed services in the service entry sheet.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Service Entry Sheets - Lean Services (F2027). | The Manage Service Entry Sheets screen is displayed. |  |
| 3 | Enter field valuesCase 1: Purchase service without material numberCase 2: Purchase service with material number | Choose Create.On the Service Entry Sheets screen, enter the following:Name of Service Entry Sheet: <SES Name>, for example, Vincent SunReference Purchase Order: <Purchase order you created>Posting Date for Goods Receipt: <Today’s date>Press EnterIn the Add Purchase Order Items screen that opens, select the checkboxes for the purchase order items.Note If the details of the service entry sheet are not displayed, then refresh the page.Increase or decrease the service entry sheet items using the "+" / "-" buttonsChoose the Add button.In the Items area, choose Purchase Order Item and enter the following for each item:Performance Period: <Enter the date range>Stated Quantity: < Stated Quantity >. For example,10Unit of measure: <Unit>.For example, HChoose Apply. |  |  |
| 4 | Add attachments in the Service Entry Sheet (Optional) | You can upload files using the Upload or add a link to the service entry sheet and view the existing attachments.On the header level, go to tab Attachments)On the item level, go to tab Items, open the details and go to tab Attachments.If the attachments are not required any longer, you can delete them.You can view the attachments and save them on your own device regardless of the status of the service entry sheet.You can add or delete attachments only while editing the service entry sheet. This means that the status of the service entry sheet must be In Process. |  |  |
| 5 | Save the service entry sheet | Choose Create | The service entry sheet is saved. |  |
| 6 | Send for approval | Choose Send for Approval. | The service entry sheet is sent for approval. |  |
| 7 | Check the status of the service entry sheet. | On the Manage Service Entry Sheets screen, follow these steps:Search for the service entry sheet that you had created aboveCheck the status of the service entry sheet.Send service entry sheet for approval if approval is required.If the status is Approved, do not send the service entry sheet for approval with flexible workflow. |  |  |

### Approve Service Entry Sheet with Flexible Workflow (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the service entry sheet is approved by the company. When this is done, the vendor can send an invoice for the approved amount to the service provider.

These flexible workflows are configured in the Manage Workflows for Service Entry Sheets app.

The ordered amount will be converted using system exchange rate to the workflow currency. Then it will be compared with workflow condition.

If the user does not have My Inbox app, you need to assign the following business catalogs to the business role of the user:

- SAP_CA_BC_MYINBOX_PC
- SAP_MM_BC_SES_WIAPPROVE_PC

This is necessary to enable the user to process incoming approval requests related to the workflow for the service entry sheet.

Table 2: Workflow Sequence

| Cases | Triggering Conditions | Workflow Sequence | Business Role |
| --- | --- | --- | --- |
| Automatic Release of Service Entry Sheet | Total net amount of service entry sheet is smaller than or equal to 1000 (for example, AED). | Automatically by system | Not applicable |
| Release of Service Entry Sheet (Multi-Step Approval) | Total net amount of service entry sheet is greater than 1000 (for example, AED). | 1st Creator of Purchase Order | Purchaser |
| 2nd Project Manager - Commercial Services | Project Manager - Commercial Services |  |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Project Manager - Commercial Services. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the app | Open My Inbox application. | The My Inbox screen is displayed. |  |
| 4 | Approve or reject the service entry sheet | To approve or reject the service entry sheet, follow these steps:Go to the Service Entry Sheet screen.Confirm the service entry sheet XXXXX you created.Note This is an optional step:Go to the Attachment section to check if the attachment was uploaded when the service entry sheet was created.Choose Release or Reject.On the Submit Decision screen, add a note, if necessary, and choose Submit. | The service entry sheet is approved or rejected. |  |

### Create Supplier Invoice with PO/GR Relation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create an invoice with reference to the purchase order for material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Open Create Supplier Invoice App | Open Create Supplier Invoice - Advanced (MIRO). | The Create Supplier Invoices screen displays. |  |
| 3 | Navigation | If the system prompts you, make the following entries and choose Continue:Company Code: 3310 | The Enter Incoming Invoice screen is displayed. |  |
| 4 | Enter Basic Data | Enter the following:Transaction: InvoiceInvoice Date: TodayPosting Date: TodayReference: <Reference invoice number from invoicing party>Amount: <Amount according to the invoice value>Currency: Enter the currencyCalculated Tax: SelectedTax Code: Enter the tax code (if there is no tax, specify the tax code <Input Tax Code>).If G/L account is subjected to tax, ensure that you enter an appropriate tax code.Caution In case pro-rata VAT is relevant for you, please make sure you meet the prerequisites as mentioned in chapter 2. | Basic data is entered. |  |
| 5 | Enter Purchase Order References | On the Purchase Order References screen, make the following entries:Reference Document Category: Purchase Order/ Scheduling AgreementPurchase Order: Enter the Purchase Order you posted in the previous step. | The Purchase Order References screen displays. |  |
| 6 | Check the Purchase Order Items data | Check the Amount, the Quantity and the Tax Code. | The amount and the quantity correspond to the values of the Goods Receipts. |  |
| 7 | Check Tax code | In the Tax area, check if there is tax code information and enter the tax amount.<Input Tax Code> . |  |  |
| 9 | Simulate Supplier Invoice and Check Messages | Choose Simulate.If there are no differences (or if the value is within the defined tolerance), the Simulation screen displays. You can check the results in the Simulation Overview and Simulation Details areas.Review the Gross Invoice Amount against the items plus tax amount (if tax code is <Input Tax Code>, you do not have any tax amount) |  |  |
| 10 | Post Invoice | Choose Post.A dialog box displays the Invoice document 51XXXXXXXX was posted (Journal Entry: 51XXXXXXXX ) message.Choose OK. | The invoice is posted. |  |

### Confirm Maintenance Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After finishing the corrective maintenance, you must confirm the order to record the real work time and the spare parts consumption. The data is used for follow-up cost evaluation. This process step shows you how to confirm maintenance order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Technician . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Perform Maintenance Jobs (F5104A). | The app opens. |  |
| 3 | Access Order Operations | Use the filter on the top to enter the order ID and choose Go. | A list of operations for the selected order is displayed. |  |
| 4 | Assign Operation | Select the operation and choose Assign to Me.The Assign to Me button is enabled only if the order operation is not assigned to anyone. | The operation is assigned to you. |  |
| 5 | Select the Operation for Processing | Choose the operations to navigate to the Perform Maintenance Job screen. | It will display the Perform Maintenance Job screen for the operation which was selected on the list page. |  |
| 6 | Start the Operation | Choose Start. | The order status is updated with JIPR (Job In Process) |  |
| 7 | Review components | Check the components which are associated with the order in the respective section on the Perform Maintenance Jobs screen. | It will show the list of components that are associated with the order. |  |
| 8 | Goods Issue or Return (Optional) | Go to Components tabChoose Post.The Post Goods Issue screen is displayed. Enter the required quantity and choose Post.Choose Return for the material that has to be returnedThe Return Goods screen is displayed. Enter the required quantity and choose Return.A new line item for the material is generatedChoose Post.The Post Goods Return screen is displayed. Enter the required quantity and choose Post. | Material is issued or returned. |  |
| 9 | Review Attachments | Check the Attachments tab which is associated with the order in the respective section on the Perform Maintenance Jobs screen. | It will show the list of attachments associated with the order. |  |
| 10 | Pause and Resume Work | Choose Pause button to pause the work.After you pause the work, you can restart the work by choosing Resume. | Work is paused or resumed. |  |
| 11 | Time Confirmation | Choose Record Time on the top left corner of the operation object page to perform time confirmation. The Record Time screen is displayed. Enter the following:Actual work. For example, 4 hoursRemaining work, if any. For example, 2 hours.Enter the confirmation text as required.Select the check box Final Confirmation and choose Record when the time confirmation for the operation is completed.This needs to be repeated for all the operations. | You will receive a message confirming that the time confirmations have been posted. You can view the number of time confirmations that have been posted in the Operation Details screen.The progress of work is shown as 100 %. |  |

### Show Costs on Maintenance Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the planned and actual costs here.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Display Maintenance Order app. | The Display Maintenance Order intial screen is displayed. |  |
| 3 | Enter Order Number | Enter the order number : 4xxxxxx and choose Continue. | The maintenance order is displayed. |  |
| 4 | Review Costs for Order | On the Display Corrective Maintenance Order: 4000XXX screen, go to Costs tab and then check costs. | Maintenance order costs are reviewed. |  |

### Technically Complete Maintenance Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The maintenance notification is completed and the maintenance order is technically completed after the required maintenance work has been performed.

The technical completion reduces all the purchase requisitions, open reservations, and capacities still outstanding for the maintenance order.

Nevertheless, the order can still continue to receive costs, for example, through invoice receipts for delivered and used materials, however it is blocked for all changes in the processing.

The order settlement transfers the costs incurred that were temporarily collected for the maintenance order, to the recipient, for example, to the cost center for the maintained object. this process step shows you how to technically complete maintenance order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as aMaintenance Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Find Maintenance Orders - Completion (F2175). | The Maintenance Order screen displays. |  |
| 3 | Search for Order Number | On the Maintenance Order screen, make the following entries:Order Type: Corrective MaintenanceAnd choose GO.Choose the order that you created in the previous step. |  |  |
| 4 | Navigate to Change Maintenance Order | Choose Related Apps at the upper right corner of the screen, and choose Change Maintenance Order. |  |  |
| 5 | Set Complete (Technically) Status | Choose Set System Status > Complete Technically. | The Complete(Technically) screen displays. |  |
| 6 | Reference Data | Make the following entries:Reference Date: <Date>Reference Time: <Time>Complete Assigned Notifications: flag setChoose OK | The Complete (Technically) status for the maintenance order is done. |  |

### Review Asset Maintenance Object Pages

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the different objects pages available for different roles in Enterprise Asset Management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner.Note You can use any of the maintenance roles from the sections above. | The SAP Fiori launchpad displays. |  |
| 2 | Start Search | Choose Search in the upper right area of the launchpad. |  |  |
| 3 | Set Search Criteria | In the dropdown list, choose Equipment, for example:233100091. |  |  |
| 4 | Tailor the Result Display | Below the search line, choose a symbol (for example, filter, display as table, sort, and so on) to filter the results list. | The result list is filtered according to your selection. |  |
| 5 | Review Object Page | Review overview information for the equipment via the Object Page. |  |  |
| 6 | Repeat Steps | Repeat steps 1 to 5 for any other role in this test script and any other object offered in the search function.For example:NotificationOrderOrder Confirmation |  |  |

## Appendix

### Process Integration

#### Preceding Processes

You must first complete the following processes before you start with the test steps:

| Process | Business Condition |
| --- | --- |
| Create New Open MM Posting Period - MDS (BNZ) | A new MM period must exist. |
|  |  |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Accounts Payable (J60) | Use the Master Data from this test script and execute the following steps:Invoice Payment PreparationPayment runSingle Outgoing PaymentManual Payment Online |
| Period-End Closing – Maintenance Orders (BF7) | A maintenance order technically completed as part of this script. |

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
- related-to :: [[14-maintenance-service-and-projects/reactive-maintenance-4hh-ae-test-script-sap-s-4hana-cloud-public-editi]]
- related-to :: [[14-maintenance-service-and-projects/test-script-emergency-maintenance-bh2-ae-sap-s-4hana-cloud-public-edit]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BH1_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 54,794 chars in the whole document
