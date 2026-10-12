---
id: 14-maintenance-service-and-projects/reactive-maintenance-4hh-ae-test-script-sap-s-4hana-cloud-public-editi
title: "Reactive Maintenance (4HH_AE) - Test Script, SAP S/4HANA Cloud Public Edition (4HH_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 4HH_AE Reactive Maintenance (UAE, plant 3310): prerequisites, preliminary setup and step-by-step Fiori test procedures incl. emergency and minor work."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/corrective-and-emergency-maintenance]
aliases: [4HH_S4CLD2608_BPD_EN_AE]
keywords: [Corrective and Emergency Maintenance, reactive maintenance, maintenance notifications, maintenance orders, maintenance order approval, maintenance backlog, emergency work, minor work, business roles, split valuation]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4HH_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1030
topic: 14-maintenance-service-and-projects/corrective-and-emergency-maintenance
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Reactive Maintenance (4HH_AE) - Test Script, SAP S/4HANA Cloud Public Edition (4HH_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4HH_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Corrective and Emergency Maintenance** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Reactive Maintenance (4HH_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Reactive Maintenance (4HH_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232855141)

[2 Prerequisites 4](#_Toc232855142)

[2.1 System Access 4](#_Toc232855143)

[2.2 Roles 4](#_Toc232855144)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232855145)

[2.4 Business Conditions 7](#_Toc232855146)

[3 Preliminary Steps 8](#_Toc232855147)

[3.1 Configure Flexible Workflow for Maintenance Orders (Optional) 8](#_Toc232855148)

[3.2 Create Planning Bucket 9](#_Toc232855149)

[3.3 Maintain Cost Rates 10](#_Toc232855150)

[3.4 Create Purchasing Information Record (Optional) 12](#_Toc232855151)

[3.5 Activate Split Valuation for Global Data (Optional) 13](#_Toc232855152)

[3.6 Activate Split Valuation for valuation Area (Optional) 16](#_Toc232855153)

[3.7 Enable Split Valuation for Material (Optional) 17](#_Toc232855154)

[3.8 Initializing Material Stock 20](#_Toc232855155)

[4 Overview Table 22](#_Toc232855156)

[5 Test Procedures 24](#_Toc232855157)

[5.1 Reactive Maintenance 24](#_Toc232855158)

[5.1.1 Create Maintenance Notification 24](#_Toc232855159)

[5.1.2 Review Maintenance Notifications 25](#_Toc232855160)

[5.1.3 Screen Maintenance Notifications 26](#_Toc232855161)

[5.1.4 Create and Plan Maintenance Order 28](#_Toc232855162)

[5.1.5 Submit Maintenance Order for Approval 32](#_Toc232855163)

[5.1.6 Approve Maintenance Order (Optional) 33](#_Toc232855164)

[5.1.7 Review and Release Maintenance Order 34](#_Toc232855165)

[5.1.8 Maintenance Backlog Overview 35](#_Toc232855166)

[5.1.9 Convert Purchase Requisitions to Purchase Orders 39](#_Toc232855167)

[5.1.10 Goods Receipt for Purchase Order 40](#_Toc232855168)

[5.1.11 Post Goods Issue 41](#_Toc232855169)

[5.1.12 Submit Order for Scheduling 42](#_Toc232855170)

[5.1.13 Add Safety Instructions (Optional) 43](#_Toc232855171)

[5.1.14 Schedule Maintenance Order and Submit for Execution 45](#_Toc232855172)

[5.1.15 Manage Output 46](#_Toc232855173)

[5.1.16 Execute Maintenance Order 48](#_Toc232855174)

[5.1.17 Complete Main Work 51](#_Toc232855175)

[5.1.18 Maintain Service Entry Sheet 52](#_Toc232855176)

[5.1.19 Execute Post Work Operations 54](#_Toc232855177)

[5.1.20 Review Failure Data 56](#_Toc232855178)

[5.1.21 Review Maintenance Cost 57](#_Toc232855179)

[5.1.22 Technically Complete Maintenance Order 58](#_Toc232855180)

[5.1.23 Create Supplier Invoice with PO/GR Relation 59](#_Toc232855181)

[5.2 Emergency Work 61](#_Toc232855182)

[5.2.1 Create Emergency Work 61](#_Toc232855183)

[5.3 Minor Work 63](#_Toc232855184)

[5.3.1 Create Minor Work 63](#_Toc232855185)

[5.3.2 Record Malfunction Details 65](#_Toc232855186)

[6 Appendix 67](#_Toc232855187)

[6.1 Process Integration 67](#_Toc232855188)

[6.1.1 Preceeding Processes 67](#_Toc232855189)

[6.1.2 Succeeding Processes 67](#_Toc232855190)

## Purpose

Overview

The reactive maintenance process has nine steps from the creation of a maintenance notification to its completion. Reactive maintenance process allows you to perform maintenance of an asset whenever a breakdown or a failure occurs.

First, you create a maintenance notification (Initiation). Next, the maintenance notification is screened and accepted (Screening). The maintenance notification is converted into a maintenance order. During this phase, the required resources for processing the order are also planned (Planning). The maintenance order is then approved for execution (Approval). Next, the maintenance order is prepared for execution. Various requirements such as stock, nonstock material, purchase requisition, and capacity are reviewed (Preparation). After this, the maintenance order is scheduled for execution (Scheduling). The maintenance order is then executed to repair the malfunction (Execution). Activities such as failure data recording and other post-work activities are performed (Post Execution). Finally, the maintenance order is reviewed and is technically completed (Completion).

For minor or emergency work, not all steps need to be executed. When you select the notification processing context in the Manage Maintenance Notification app, you also decide the variation of the reactive maintenance process (minor or emergency).

To enable safety instructions, you need to activate the Health and Safety Management (54A) scope item.

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

| Name (Role Template) | ID (Role Template) | Name (Space) | ID (Space) |
| --- | --- | --- | --- |
| Maintenance Planner | SAP_BR_MAINTENANCE_PLANNER | Maintenance Planning | SAP_BR_MAINTENANCE_PLANNER |
| Maintenance Supervisor | SAP_BR_MAINT_SUPERVISOR | Maintenance Supervision | SAP_BR_MAINTENANCE_SUPERVISOR |
| Maintenance Technician | SAP_BR_MAINTENANCE_TECHNICIAN | Maintenance Execution | SAP_BR_MAINTENANCE_TECHNICIAN |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |
| Purchaser | SAP_BR_PURCHASER |  |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |
| Employee - Maintenance Info | SAP_BR_EMPLOYEE_MAINTENANCE | Self Services / Self Services / Employee Overview Space | SAP_BR_EMPLOYEE / SAP_CA_SPT_EMPLOYEE_CROSS_PC / SAP_EAM_SPT_EMPLOYEE_PC |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company is created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. You can also use the following sample data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Equipment | 233100091 | Cooling Water Circulation Pump |  |
| Equipment | 233100093 | Cooling Water Circulation Pump |  |
| Spare Parts | SP001 | Bearing | Spare parts |
| Spare Parts | SP002 | Coupling | Spare parts |
| Spare Parts | SP003 | Shaft | Spare parts |
| Spare Parts | SP004 | Gaskets 1mm | Spare parts |
| Spare Parts | SP005 | Mechanical Seal | Spare parts |
| Spare Parts | SP006 | Spur gear IS651 | Spare parts |
| Spare Parts | SP007 | Motor (Serialiased Spare Part) | Spare Parts |
| Non-stock Material | NL001 | Screw |  |
| Service Material | SM0001 | Service Material 01 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331B | Std. storage 2 |  |
| Supplier | 33300001 | Domestic UAE Supplier 1 |  |

For more information on creating master data objects, see the following Master Data Scripts (MDS):

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| 5LM | Create Functional Location |
| 5MF | Create Equipment |
| 5MH | Create Maintenance Work Center |
| 5MI | Measuring Point |
| 2J7 | Spare Parts |

Bill of Material Structure

This overview shows the bill of material structure and the usage of each component if you have activated all optional enhancements.

| Material | Level | Material Type | Unit | Characteristics | Optional Enhancements |
| --- | --- | --- | --- | --- | --- |
| 233100091 | 0 | Equipment | PC | Cooling Water Circulation Pump |  |
| SP001 | 1 | ERSA | PC | Bearing |  |
| SP002 | 1 | ERSA | PC | Coupling |  |
| SP003 | 1 | ERSA | PC | Shaft |  |
| SP004 | 1 | ERSA | PC | Gaskets 1mm |  |
| SP005 | 1 | ERSA | PC | Mechanical Seal |  |
| SP006 | 1 | ERSA | PC | Spur Gear IS651 |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period | You have completed the step described in the Create New Open MM Posting Period (BNZ) master data script. The posting period is up to date.To run through this scope item, the materials must be available in stock. |

## Preliminary Steps

### Configure Flexible Workflow for Maintenance Orders (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can configure and activate flexible workflow for maintenance orders.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 2:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Workflows for Maintenance Orders - Asset Management (F4989) app. | The Manage Workflows screen is displayed. |  |
| 3 | Check Automatic Approval of Maintenance Order | In Workflows list, choose Automatic Approval of Maintenance Order, Make sure workflow Automatic Approval of Maintenance Order is in active status. If not, select it and choose Activate. | The workflow item is activated. |  |
| 4 | Manage Workflow | You can also create custom workflow. When a workflow is triggered, it determines the agents who can approve the maintenance order.Below is a custom workflow created for referenceChoose Create and make following entries:Workflow Name: <Enter Text>Go to the START CONDITIONS area and choose Maintenance Order Type is <Enter Order Type> |  |  |
| 5 | Create Step Sequence | Go to the STEPS area, and choose Create, then make the following entries on the next screen:Go to the RECIPIENTS area:Assignment By: UserUser: <Enter User ID>Step to be completed by: One of the recipients.Step Conditions:Go to the Step Conditions area and choose Main Work Center of the maintenance order is <Enter Main Work Center>.Choose Create. |  |  |
| 6 | Save Workflow | Choose Save. | Workflow is created. |  |
| 7 | Activate Workflow | Go back to the workflow list.Select the required workflow and choose Activate. | The workflow is activated. |  |

### Create Planning Bucket

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this app, you can create maintenance planning buckets that aid you in effectively managing your maintenance backlog. By defining maintenance planning buckets, you can divide the maintenance effort into manageable groups based on their scope. The scope of a planning bucket includes time, but also other important attributes of the maintenance jobs such as the planner group.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 3:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Maintenance Planning Buckets (F3888) | The app opens. |  |
| 3 | Create New Planning Bucket | Choose the Create button. Enter the following information:Header:Label: <PUMP_3310>Description: <Planning Bucket for PUMP Unit>General Data:Type: Operational MaintenancePlanning Plant: 3310Time Period:Start Date and Time: Todays date/TimeDuration: 7 DaysRecurrence: WeeklyRecurs Every: 1 WKNumber of Buckets in Advance: 5Scope:Planner Group: <Entry of your Choice >Plant Section: <Entry of your Choice >Maintenance Plant: 3310Main Work Center: <Entry of your Choice >Technical Object: 233100091Choose Create. | Planning bucket is saved. |  |

### Maintain Cost Rates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can maintain, check, and update the actual cost rates.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 4:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Cost Accountant - Overhead. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Cost Rates - Plan (F3162) | The app opens. |  |
| 3 | Check Actual Cost Rates | Set the following filters and choose Go.Valid On: TodayCost Center: 33101701Activity Type: 11Currency: For example, AEDCheck if there is a valid cost rate for given cost center, activity type, and period. | The actual cost rates for given cost center, activity type and period are checked for valid values.Note You can skip the next step if there is a valid cost rate for given cost center, activity type, and period. |  |
| 4 | Maintain Actual Cost Rates | Choose Add and enter the followingCost Center: 33101701Activity Type: 11From Fiscal Year: Current YearFrom Period: Current PeriodFixed Rate: 100Currency: For example, AEDPer:1Activity Unit: HChoose Save. | Cost rates are created. |  |

### Create Purchasing Information Record (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to create the information records for materials, for example, NL001 and choose a valid supplier (for example, 33300001).

This step becomes obsolete if the necessary information records are already present.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 5:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Manage Purchasing Info Records (F1982) app. | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record screen displays. |  |
| 4 | Enter Header Data | Go to header area and enter the following:Purchasing Info Record Category:StandardPurchasing Organization: 3310Supplier: 33300001Material: NL001Plant: 3310Purchasing Group : 001 | Header data is added. |  |
| 5 | Enter General Information | Enter the following:Available From: TodayAvailable To: 12/31/9999 | General information is added. |  |
| 6 | Enter Purchasing Data | Enter the following:Incoterm: EXWIncoterm Location 1: Vendor | Purchasing data is added. |  |
| 7 | Enter Delivery and Quantity Data | Enter the following details:Delivery Time in Days: <XX Days>, for example, 1Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10.0Tax Code: <Tax Code>, for example, I0.Order Unit: PCStandard Order Quantity <Standard Order Quantity>, for example, 10 | Delivery and quantity data is added. |  |
| 8 | Enter Condition Data | Go to the Conditions area. Choose the Create icon. Enter the following:Valid From: <Valid from Date>Amount: <Amount>, for example, 1Currency: <Currency>, for example, AEDPricing Unit: <Pricing Unit>, for example, 1Valid To: <Valid to Date>Choose Apply. | Condition data is added. |  |
| 9 | Enter Reference Data (Optional) | You can enter reference data. | Reference data is added. |  |
| 10 | Create Purchasing Information Record | Choose Create. | A purchasing information record is created. |  |

### Activate Split Valuation for Global Data (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to configure the valuation types and assignment to valuation category for repairable spare part specifying the conditions of the material in its lifecycle.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configura-tion. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country‑/region‑dependent settings for the intended local version, choose Set Local Version.Select the Application Area as LogisticsSelect the Sub Application Area as InventorySelect the row with the item name Material Valuation and Account Assignment | Configuration steps are displayed |  |
| 4 | Open Material Valuation and Account Assignment | Under Configuration Steps, select the step name "Activate Split Valuation for Global Data" and click on Configure | Global Valuation Types are displayed |  |
| 5 | Creation of Valuation Type | Click on New Entries for creating new valuation Types (eg: NEW,DAMAGED,REFURBISHED)Select the Account reference category as 0003 for sparesSelect if External Purchase Order is allowed or notSelect if Internal Purchase Order is allowed or not | The new valuation type will be created |  |
| 6 | Assign Valuation types to valuation category | All the existing valuation categories will be displayed, select the category M and click on the Assigned valuation typesClick on New entries, a screen to enter the valuation type will be displayed.Enter the valuation types created in the previous step and save | Assignment of valuation type to valuation category will be done |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Com-ment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Implementation Activities | The Implementation Activities screen is displayed. |  |
| 3 | Access Configuration | To locate the activity in the tree view,click on search icon and select the extended Search optionEnter the Node Text/Activity Description: "Activate Split Valuation for Global Data" and click on continue | The Activity in Tree View is displayed. |  |
| 4 | Creation of Valuation Type | Click the IMG ActivityClick on New Entries for creating new valuation Types (eg:NEW,DAMAGED,REFURBISHED)Select the Account reference category as 0003 for sparesSelect if External Purchase Order is allowed or notSelect if Internal Purchase Order is allowed or not | The New valuation types will be created |  |
| 5 | Assign Valuation types to valuation category | All the existing valuation categories will be displayed, select the category M and click on the Assigned valuation typesClick on New entries, a screen to enter the valuation type will be displayed.Enter the valuation types created in the previous step and save | Assignment of valuation type to valuation category will be done |  |

### Activate Split Valuation for valuation Area (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to configure the assignment of valuation area to valuation category which has been configured in the previous step.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Com-ment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  | Manage Your Solution screen is displayed. |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country‑/region‑dependent settings for the intended local version, choose Set Local Version.Select the Application Area as LogisticsSelect the Sub Application Area as InventorySelect the row with the item name: Material Valuation and Account Assignment |  | Configure Your Solution screen is displayed. |
| 4 | Open Material Valuation and Account Assignment | Under Configuration Steps, select the step name "Activate Split Valuation for Valuation Area" and click on Configure | Valuation area is displayed |  |
| 5 | Assign valuation Area to valuation category | Select the line item for Valuation area and click on Local Valuation Categories.A New screen will appear for Local valuation categories. Click on New EntriesEnter the Valuation category M and save | Valuation Area to valuation category has been assigned |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Com-ment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Implementation Activities | The Manage Your Solution screen is displayed. |  |
| 3 | Access Configuration | To locate the activity in the tree view,click on search icon and select the extended Search optionEnter the Node Text/Activity Description: "Activate Split Valuation for Valuation Area" and click on continue | The Activity in Tree View is displayed. |  |
| 4 | Assign valuation Area to valuation category | Click the IMG ActivitySelect the line item for Valuation area and double click on Local Valuation CategoriesA New screen will appear for Local valuation categories. Click on New EntriesEnter the Valuation category M and save | Valuation area to valuation category has been assigned |  |

### Enable Split Valuation for Material (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to extend the repairable spare part material for Accounting view to assign the valuation category and extend it with required Valuation types to enable split valuation.

Choose Configure Your Solution.

|  |
| --- |
| Note A valuation category cannot be assigned to a material if it has:Existing stock in the system.Any open documents like purchase orders or reservations.A history of transactions such as goods movements or invoices. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data (MDG). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Change Material (MM02). | Change Material (Initial Screen) displays. |  |
| 3 | Enter Material Basic Data | On the Change Material (Initial Screen), make the following entries:Material: Enter the material number you created in the previous stepMaterial type: ERSA Spare Parts | The Select View(s) view displays. |  |
| 4 | Choose Views | In Select View(s), select the following and choose Continue:Accounting 1 | The Organizational Levels view displays. |  |
| 5 | Enter Organizational Levels Data | On the Organizational Levels view, in the Organizational level section, make the following entries:Plant | The Change Material (Spare Parts) view displays. |  |
| 6 | Enter Accounting Data | From the Change Material (Spare Parts) view, on the Accounting 1 tab, make the following entry:Valuation Class: 3040Valuation Category: MPrice Unit: 1Prc. Ctrl: Moving average (V) |  |  |
| 7 | Save Your Data | Choose Save. | Material is saved |  |
| 8 | Access the SAP Fiori App | Open Create Material (MM01). | Create Material (Initial Screen) displays. |  |
| 9 | Enter Material Basic Data | On the Create Material (Initial Screen), make the following entries:Material: The material number you created in the previous stepMaterial type: for example, ERSA Spare Parts | The Select View(s) view displays. |  |
| 10 | Choose Views | In Select View(s), select the following and choose Continue:Accounting 1 | The Organizational Levels view displays. |  |
| 11 | Enter Organizational Levels Data | On the Organizational Levels view, in the Organizational level section, make the following entries:PlantValuation Type: NEW | The Create Material (Spare Parts) view displays.This system message appears: The material already exists and will be extended. |  |
| 12 | Enter Accounting Data | From the Create Material (Spare Parts) view, on the Accounting 1 tab, in the Prices and Values section, make the following entries:Price Unit: 1Price Control: V (Moving Average)You may enter a Moving Average Price Per Unit (Optional) |  |  |
| 13 | Save Your Data | Choose Save. | Material with Valuation type is created |  |
| 14 | Extend the material for additional valuation types | Repeat the above steps from (11 to 13) for other valuation types relevant (e.g.: REFURBISH and DAMAGED) | Material extended for REFURBISH and DAMAGED |  |

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

This section describes test procedures for each process step that belongs to this scope item.

Table 6:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen is displayed. |  |
| 3 | Input Material | Make the following entries and choose Enter:Material: < material number>. Select one of the Spare Parts Material mentioned in the previous section Master Data, Organizational Data, and Other Data.Note It is possible to select the material with specific valuation type (For Example NEW /DAMAGED/RE-FURBISH) if split valuation is enabled as explained in the previous step.Plant: 3310 | You have entered the details. |  |
| 4 | Select Stock | Select the icon beside the stock that you want to add initial stock, for example:Storage Location: 331BUnrestricted-Use Stock | A dialog box opens. The storage location, stock type and the current quantity are displayed according to your entries in the previous steps. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Document Date: <today>Posting Date: <today>Stock Change: initial entryQuantity: <quantity number>Note Serial Number also can be maintained or automatically assigned if the material is serial number enabled.Inorder to enable serialisation for the Material,required serial Number Profile needs to be as-signed with the material Master in Plant Data/Storage 2 tab.Default Serial Number which can be used is YPM1 | The material document is created and the stock has been added. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

Table 7: Reactive Maintenance

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Create Maintenance Notification | Employee - Maintenance Info | Manage Maintenance Notifications - New Version (F5777) | Maintenance notification is created. |
| Review Maintenance Notifications | Employee | Manage Maintenance Notification (F5777) | Maintenance notification is reviewed. |
| Screen Maintenance Notifications | Maintenance Supervisor | Manage Maintenance Notification (F5777) | Maintenance notification is approved. |
| Create and Plan Maintenance Order | Maintenance Planner | Manage Maintenance Notifications and Orders (F4604)Manage Maintenance Notification (F5777) | Maintenance order is created and resources are planned. |
| Submit Maintenance Order for Approval | Maintenance Planner | Manage Maintenance Notifications and Orders (F4604) | Maintenance order is submitted for approval. |
| Approve Maintenance Order (Optional) | As per agent determined in the workflow. | My Inbox - All Items (F0862) | Maintenance order is approved |
| Review and Release Maintenance Order | Maintenance Planner | Manage Maintenance Notifications and Orders (F4604) | Maintenance order is released. |
| Convert Purchase Requisitions to Purchase Orders | Purchaser | Process Purchase Requisitions (F1048A) | Purchase requisitions are converted to purchase orders. |
| Goods Receipt for Purchase Order | Warehouse Clerk | Post Goods Movement (MIGO) | Goods receipt is posted. |
| Post Goods Issue | Warehouse Clerk | Post Goods Movement (MIGO) | Goods Issue is posted. |
| Maintenance Backlog Overview | Maintenance Planner | Maintenance Backlog Overview (F5105) | Maintenance backlog is reviewed |
| Submit Order for Scheduling | Maintenance Planner | Find Maintenance Orders - Completion (F2175) | Maintenance orders are ready to be scheduled. |
| Add Safety Instructions (Optional) | Maintenance Planner | Change Maintenance Order (EAMS_WDA_ORDNTF_OIF) | Safety instructions are added. |
| Schedule Maintenance Order and Submit for Execution | Maintenance Planner | Find Maintenance Orders - Completion (F2175) | Maintenance orders are scheduled. |
| Manage Output | Maintenance Supervisor | Find Maintenance Orders - Completion (F2175)Manage Work Packs (F6065) | The documents are printed. |
| Execute Maintenance Order | Maintenance Technician | Perform Maintenance Jobs (F5104A) | Time confirmation is posted for pre and main maintenance order operations. |
| Complete Main Work | Maintenance Supervisor | Find Maintenance Orders - Completion (F2175) | Pre and main work are completed. |
| Maintain Service Entry Sheet | Purchaser | Manage Service Entry Sheets - Lean Services (F2027) | The service entry sheet is created. |
| Execute Post Work Operations | Maintenance Technician | Perform Maintenance Jobs (F5104A) | Post work operations are completed. |
| Review Failure Data | Maintenance Supervisor | Find Maintenance Orders and Operations - Dispatching (F2173) | Failure data is reviewed. |
| Review Maintenance Cost | Maintenance Planner | Maintenance Order Costs (F4603) | Maintenance cost is reviewed. |
| Technically Complete Maintenance Order | Maintenance Planner | Find Maintenance Orders - Completion (F2175) | Maintenance order is technically completed. |
| Create Supplier Invoice with PO/GR Relation | Accounts Payable Accountant - Procurement | Create Supplier Invoice - Advanced (MIRO) | Supplier invoice is posted. |

Table 8: Emergency Work

|  |  |  |  |
| --- | --- | --- | --- |
|  |  |  |  |
| [Create Emergency Work](#unique_17) [page ] 61 | Maintenance Supervisor | Manage Maintenance Notifications - New Version (F5777) | Maintenance Notification is created. |

Table 9: Minor Work

|  |  |  |  |
| --- | --- | --- | --- |
|  |  |  |  |
| [Create Minor Work](#unique_18) [page ] 63 | Maintenance Supervisor | Create Maintenance Request (F1511A) | Maintenance notification is created. |
| [Record Malfunction Details](#unique_19) [page ] 65 | Maintenance Supervisor | Manage Maintenance Notifications - New Version (F5777) | Malfunction details are recorded. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Reactive Maintenance

#### Create Maintenance Notification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is the Initiation phase of the maintenance process where an employee can create a maintenance notification.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Maintenance Employee. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Maintenance Notifications - New Version (F5777). | The Manage Maintenance Notification page is displayed. |  |
| 3 | Create Notification | From the List page, choose Create.A popup screen appears. Enter the following details: -Technical Object: 217100091You can search for an object in the search help by entering keywords such as 'water pump' and then choose Go.From the results, select the equipment number 217100091 and description Cooling Water Circulation Pump.Description: Detailed information regarding the maintenance notification can be updated here.Choose Create. | A detail page opens where you can provide more inputs. |  |
| 4 | Enter Details | Enter the following details:Current Location: PlatformFailure Mode: VibrationDetection Method: InspectionEffect: Production restricted. Effect can be selected from the list available.Malfunction Start Date Time:Enter the date and the timeLong Text: Answer the predefined questions. | The details are entered. |  |
| 5 | Assess Priority | Assess Priority: Select relevant consequence and likelihood for each consequence category and choose Assess button. Review the details and choose Apply.Ensure that the following prerequisites are met:Ensure that the technical object is populated.Technical object master data has the maintenance plant populated in the Location Data tab. | Priority is automatically calculated and populated on the screen. |  |
| 6 | Add Attachment/URL (Optional) | In the Attachments section, choose Upload. Select the files you want to upload. You can also choose Add a Link to provide link to relevant information for the maintenance notification. | The files and the links are added to the maintenance notification. |  |
| 7 | Save | Choose Create. | The maintenance notification is submitted and is available in the same app. |  |

#### Review Maintenance Notifications

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Employee can check their existing maintenance notifications in this application with various filter options as explained below.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 10:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Employee - Maintenance Info. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Maintenance Notifications - New Version (F5777) | The app opens. |  |
| 3 | Search for Maintenance Notification Based on the Status | You can filter the list of maintenance notifications based on the subphase such as: Draft , Submitted, Action Required (returned due to insufficient information), Accepted , Rejected, and Completed.To create new maintenance notifications, choose Create button. | System retrieves a list of maintenance notifications based on the selected status. |  |
| 4 | Review Maintenance Notification | Choose the maintenance notification created in the previous step to view details and review progress. | The maintenance notification is reviewed. |  |

#### Screen Maintenance Notifications

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is the Screening phase of the maintenance process where the supervisor reviews all the open maintenance notifications. Change responsibility of the notifications (if required) and take appropriate decision to proceed with the notification or reject the notification.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 11:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Test Step # | Test Step Name | Instruction |  | Pass/Fail/Comments |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Supervisor. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Maintenance Notifications - New Version (F5777) | The app opens. |  |
| 3 | Get List of Maintenance Notifications | By default, the app displays a list of maintenance notifications that are open.Enter the following:Notification Type: Reactive WorkChoose GoYou can filter the list of maintenance notifications in Action Required, Accepted, Rejected, and Completed status. | List of maintenance notifications is displayed based on the filter criteria. |  |
| 4 | Change Responsibility (Optional) | Select one or more open maintenance notifications by selecting the checkbox. Choose Change Responsibility button.On the Change Responsibility screen, the main work center, planner group, planning plant, and person responsible can be changed. | Responsibility details for the maintenance notifications are changed. |  |
| 5 | Review and Modify the Maintenance Notification | Choose a maintenance notification which needs to be reviewed. Maintenance notification is opened and details can be seen.Choose Edit to update the information related to malfunction, responsibility, and other details. Further while reviewing the notification, the supervisor can also reassess the risk and redetermine the priority of the maintenance notification and if required, can manually change the final due date.Choose Save. | Maintenance notification is reviewed and updated. |  |
| 6 | Accept Maintenance Notification | From the top right side, you can choose Accept, Reject, or Action Required.Accept the maintenance notification if all the details are correct in the notification.Note If you choose Action Required, the maintenance notification is sent back and will be available by applying Action Required subphase filter in the app in tab where the initiator, a person responsible, or maintenance supervisor can provide required information and resend it for screening. If you reject a maintenance notification, the notification will not be processed further and can be seen in the Rejected subphase in Manage Maintenance Notifications app. The reason code needs to be selected if maintenance notification is rejected or sent back seeking additional information. | The maintenance notification is accepted. |  |

#### Create and Plan Maintenance Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the maintenance notification is accepted, we are in the Planning phase of the maintenance process. This process step shows how to convert a maintenance notification into a maintenance order and provides details to plan the resources for the order.

Order processing helps you to plan maintenance tasks in greater detail. You decide the tasks to be performed and what components (materials) are needed, and so on.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 12:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Manage Maintenance Notifications and Orders (F4604) app. | The app opens with details. |  |
| 3 | Get List of Maintenance Notifications | Enter the following:Execution Object Type: Maintenance NotificationNotification Type: Reactive Work (Y1)Choose Go | Based on the filter criteria, a list of accepted notifications is displayed. |  |
| 4 | Create or Assign Maintenance Order | To create or assign an order, follow these steps:Select one or more maintenance notifications for which maintenance order needs to be created.Choose Create Order button on the top of the screen.Select the Maintenance Order Type: Reactive Maintenance (YA01)Choose Create.Alternatively, it is possible to assign existing maintenance order to a maintenance notification using the Assign Order button. | The maintenance order is created and is assigned to the maintenance notification.The order number is shown in Associated with under Execution Object Type section of the list view. |  |
| 5 | Plan Maintenance Order | In the Execution Object Type column, choose the maintenance order number to access the quick view and navigate to the Change Maintenance Order (WDA0272) app.To plan maintenance order, add details such as material, services, and labor in the Change Maintenance Order (WDA0272) app as described in steps below. | Change Maintenance order screen is opened. |  |
| 6 | Define the Operations | Go to the Operation Data tab. This selection brings you to the operation overview. Make the following entries in the Operations table.Operation : (example, 0010)Description: <Entry of your choice>Work: <Entry of your choice>Number of Capacities: <2>Stage: <Select Stage as required>The system calculates the duration of the operation based on the time you entered in the Work field and on number of resources maintained in the Number of Capacities field.Add required number of operations based on Pre, Main and Post stage. | Operations are added with Pre, Main and Post stages along with other details. |  |
| 7 | Add Stock and Non Stock Material | Select the checkbox for operation (example, 0010) and choose Materials tab at the bottom of the screen. Select the variant as Standard.For a stock material, follow these steps:Choose Select from Structure List.On the Select Material Component screen, select the stock item of item category L (for example, SP001).Note While adding material in the component tab, the valuation type of the material can be entered in the filed Batch if the material is enabled for split-valuation as mentioned in the preliminary stepChoose OK.You can also plan to return any damaged spare part back to store.Select the stock item of item category L, Quantity (eg: -1)Valuation type of the damaged material to be entered in Batch Field (eg: DAMAGED for split valuated material)If its not split valuated material,you can keep batch field blankChoose OK.For a non-stock material, enter the following:Material: NL001Item Category: Non-stock Item NQuantity: <1>Plant: 3310Purchasing Org: 3310Price: Entry of your choiceSupplier: 33300001G/L Account: 61002000Note To duplicate a material line in the list with all item data, choose Copy Material. You can then change specific fields in the copied line. | Stock and non-stock material are added to the maintenance order. |  |
| 8 | Add Services | Select the checkbox for operation (example, 0010) and choose Services tab at the bottom of the screen.For a service without service material, enter the following:Description: <Description of service>Quantity: <1>Unit:<H>Plant: 3310Price: Entry of your choicePurchasing Org: 3310Purchasing Group: 001Supplier: 33300001G/L Account: 65008000Material Group: YBMM01Note You can choose Settings button to add or remove fields in the screen.For service with service material, enter the following:Product: SM0001Quantity: <1>Supplier: 33300001Press Enter. The system will fill up other fields from Service Product Master. | Services are added to maintenance order. |  |
| 9 | Add Enhanced Limit ServicesNote Enhanced limit services are not available for Brazil. | Select the checkbox for operation (example, 0010) and choose Services tab at the bottom of the screen.For a service without service material, enter the following:Description: <Description of service>Item Categoy: E- Enhanced limitExpected Value: <Entry of your choice>Overall Limit: <Entry of your choice>Note The expected value must not be larger than the overall limit.Plant: 3310Purchasing Org: 3310Purchasing Group: 001Supplier: 33300001G/L Account: 65008000Material Group: YBMM01You can choose Settings button to add or remove fields in the screen.Note You can select a service material for a service, if required. | The quantity is set to 1. The unit is set to AU (Activity Unit) or to the unit of the material master record.The value from the Expected Value field should be copied to the Price field. |  |
| 10 | Cost Review | Go to the Costs tab.On the top of the screen, select Additional Functions > Determine CostsThe planned cost is displayed as per the cost category.The estimated costs can be updated against each cost category. | Planned and estimated costs are reviewed and updated. |  |
| 11 | Check Entries | Choose Check Entries in the upper left corner of the screen. | Entries have been checked. |  |
| 12 | Save Order | Choose Save | The maintenance order is saved and is in Planning phase.The selected stock material is reserved automatically.Note To verify this, log on to the SAP Fiori launchpad as a Inventory Manager.Open Display Stock Overview (MMBE)Enter the stock material, plant, and storage location and choose Execute.Select storage location line under Stock Overview and choose Reservations (Menu -> Environment -> Reservations) |  |

#### Submit Maintenance Order for Approval

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is the Approval phase of the maintenance process, where the maintenance planner submits the order for approval.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 13:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Manage Maintenance Notifications and Orders (F4604) app. | The app opens. |  |
| 3 | Get list of Maintenance Orders | Enter the following:Execution Object Type: Maintenance OrderOrder Type: Reactive MaintenanceChoose Go. | A list of maintenance orders is displayed based on the filter criteria. |  |
| 4 | Submit Order for Approval | Select one or more maintenance orders which are ready for approval.On the top right side of the screen, choose Submit for Approval button. | The maintenance order is submitted for approval.The order goes for approval as per the workflow that you have maintained.Note If custom workflows have not been maintained, the order gets approved automatically.Maintenance order is in Approval phase. |  |

#### Approve Maintenance Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to approve maintenance orders from the My Inbox - All Items (F0862) app.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 14:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Supervisor. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | A list of orders that are ready for approval is displayed. |  |
| 3 | Approve | On the My Inbox screen, select the workflow request for maintenance order. You can review information page which gives details of maintenance order like general data, responsibilities, account assignment, cost, dates and so on.Update comment in Comments section.Approve the maintenance order and add decision note if required.Note If a maintenance order is rejected, it can be processed further and sent for approval again. | The maintenance order is approved and the order will be removed from the list in My Inbox. |  |

#### Review and Release Maintenance Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, a maintenance planner reviews and releases the maintenance order.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 15:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Maintenance Notifications and Orders (F4604) app. | The app opens. |  |
| 3 | Review Maintenance Order | Enter the following:Execution Object: Maintenance Order Number which was approved in the previous stepChoose Go. | Maintenance order is displayed in the list view and is reviewed. |  |
| 4 | Release Maintenance Order | Select the order by selecting the checkbox. Choose Change Order Status and select Release.Plan costs at the time of releasing the order will be taken as baseline cost and will be displayed in detailed cost analysis section of cost tab. Even if there is a change in plan cost later the ,baseline cost will remain the same and this will help to understand the deviation from plan costs. | Maintenance order is released for preparation. |  |
| 5 | Review Purchase Requisitions | When the maintenance order is released, purchase requisition is created for the non-stock material and services.Select the maintenance order. On the Maintenance Order screen that appears, go to the Operations tab.Select the row for operation (example, 0010).On the Maintenance Order Operation screen, go to the Material tab.Note the purchase requisition number for the non-stock material and services from the Purchase Requisition column. | The purchase requisitions are reviewed. |  |

#### Maintenance Backlog Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The maintenance order is in Preparation phase. Maintenance Planner can use the Maintenance Backlog Overview (F5105) app to analyze the maintenance orders in various phases.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 16:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Maintenance Backlog Overview (F5105) app. | The app opens. |  |
| 3 | Open Maintenance Order via Maintenance Backlog Card | Use the filter on the top to get the list of orders based on planning bucket templateReference Planning Bucket: PUMP_3310Past Buckets: 1Future Buckets: 5 | The Maintenance Backlog card, External Procurement card, Rework Orders and Quick Link card are displayed. |  |
| 4 | Manage Maintenance Backlog Card | Select the criteria from the dropdown list for the maintenance backlog card.By PhaseBy Maintenance Activity TypeBy Order and Notification TypeBy Priority | Based on the selected criteria, the maintenance backlog card displays the summary of orders that are associated with a specific maintenance planning bucket. |  |
| 5 | Review Maintenance Orders and Maintenance Notifications | Select any colour segment on the bar chart to review the details of a maintenance notification or a maintenance order. | Based on the selected colour segment, the respective application opens with details of the maintenance notification or the maintenance order. You can review the details. |  |
| 6 | Manage Maintenance Backlog Card (By Phase) | Select By Phase in the maintenance backlog card and choose the bar that indicates preparation. | The Manage Maintenance Backlog screen displays a list of maintenance orders in the Orders in Preparation tab. You can view the status of the maintenance orders for schedule compliance, availability, and readiness. |  |
| 6.1 | Manage Maintenance Backlog Card (By Phase) | Select Stock Components, Non-Stock Components Services and Resources tabs to review the corresponding details. | The maintenance order details have been reviewed. |  |
| 6.2 | Manage Maintenance Backlog Card (By Phase) - Keep Committed Quantities- Activate (Optional) | To keep the committed quantity and to fulfill the shortage quantity, follow these steps:Go to the Stock Components tab.Go to the Orders In Preparation tab.Select the stock components by selecting the checkbox.Choose Keep Committed Quantities > Activate .Note You can schedule the job through the Schedule Material Availability Check Report to perform an ATP check for stock components. | The system assigns the available stock material to the maintenance order if there is a shortage. |  |
| 6.3 | Manage Maintenance Backlog Card (By Phase) – Schedule Order (Optional) | To change the scheduling of the maintenance orders, follow these steps:Go to the Orders tab.Go to the Orders In Preparation tab.Select an order by selecting the checkbox.Choose Change Scheduling and select any one of the options:You can assign the order to the next or the previous bucketYou can change the basic start date or the end dateYou can assign or unassign the order to a maintenance event.To submit the order for scheduling, choose Submit for Scheduling.Note Order can also be submitted for scheduling through Find Maintenance Orders - Completion (F2175) app and is detailed out in the process step [Submit Order for Scheduling](#unique_30) [page ] 42. | The result may be one of the following depending on the selected option:The basic start date or the end date is changedThe order is moved to the next or the previous bucketThe order is assigned or unassigned to the maintenance event.The maintenance order moves into the scheduling phase. |  |
| 7 | Manage External Procurement Card | Click on the bar chart to review the purchase requisition or the purchase order for the corresponding milestone. | The purchase requisition or the purchase order is displayed. |  |
| 8 | Monitoring Procurement Activities | As a maintenance planner, you can monitor the availability status of non-stock components and services (external operations and lean services) in the Manage Maintenance Backlog (F4073) app.For this purpose, the system tracks several milestones in the procurement process. They mark the completion of the following important procurement activities:Procurement ActivityProcurement MilestoneCreate Purchase RequisitionPurchase Requisition CreatedRelease Purchase RequisitionPurchase Requisition ReleasedSend Purchase Order to VendorPurchase Order Sent to VendorReceive Purchase Order ConfirmationOrder Confirmed by VendorReceive Shipment ConfirmationOrder ShippedReceive ShipmentOrder Received in FullNote For non-stock components, all the six milestones are applicable. For lean services or external operations, only the first four milestones are applicable. | A green symbol indicates that the milestones are complete.A yellow symbol indicates that the milestone is pending completion and the warning period has started.A red symbol indicates that the milestone is pending completion and its due date has been reached or passed.A grey symbol indicates that the milestone is not yet pending completion. |  |
| 9 | Procurement Milestone: Purchase Requisition Created | When a maintenance order with non-stock material or service is released and saved, a purchase requisition gets created and released. For more information, see [Review and Release Maintenance Order](#unique_28) [page ] 34. | The procurement milestone Purchase Requisition Created is green in color. |  |
| 10 | Procurement Milestone: Purchase Requisition Released | When a maintenance order with non-stock material or service is released and saved, a purchase requisition gets created and released. For more information, see [Review and Release Maintenance Order](#unique_28) [page ] 34. | Procurement Milestone: Purchase Requisition Released is green in color. |  |
| 11 | Procurement Milestone: Purchase Order Sent to Vendor | If output management is enabled and print or email is taken, then milestone will turn green. | Procurement Milestone: Purchase Order Sent toVendor is green in color. |  |
| 12 | Procurement Milestone: Order Confirmed by Vendor | The order confirmed by the vendor milestone turns green when one or more order acknowledgments for the entire requirement quantity have been entered in the purchase order. Follow these steps:Open the Change Purchase Order - Advanced (ME22N) application after logging in as PurchaserChoose Other Purchase Order button and enter the PO number.Choose Item Detail option and go to the Confirmations tab.Choose Confirmation Control.Select the Acknowl. Reqd checkbox.Press EnterEnter the following:Confirmation control: AB (Order Acknowledgement)Delivery Date:Quantity: <Enter the PO quantity>Press EnterChoose Save | Procurement Milestone: Order Confirmed by Vendor is green in color. |  |
| 13 | Procurement Milestone: Order Shipped | The order shipped milestone turns green when:Option 1: The Delivery Completed checkbox is selected in the purchase order.Option 2: One or more shipping notifications for the entire requirement quantity have been entered in the purchase order.Follow these steps:Open the Change Purchase Order - Advanced (ME22N) application after logging in as PurchaserChoose Other Purchase Order button and enter the PO number.Choose Item Detail option and go to the Confirmations tab.Choose Confirmation Control.Select the Acknowl. Reqd checkbox.Press EnterEnter the following:Confirmation control: LA (Inbound Delivery)Delivery Date:Quantity: <Enter the PO quantity> .Press EnterChoose Save | Procurement Milestone: Order Shipped is green in color. |  |
| 14 | Procurement Milestone: Order Received in Full | Order received in full milestone turns green when the goods receipts have been posted for the entire requirement quantity.You can find the detailed steps in the following sections:For non-stock components, see [Goods Receipt for Purchase Order](#unique_31) [page ] 40.For services, see [Maintain Service Entry Sheet](#unique_32) [page ] 52. | Procurement Milestone: Order Received in Full is green in color. |  |

#### Convert Purchase Requisitions to Purchase Orders

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

This section describes test procedures for each process step that belongs to this scope item.

Table 17:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Process Purchase Requisitions (F1048A) app. | The Process Purchase Requisitions (V2) screen is displayed |  |
| 3 | Search for Purchase Requisition | Enter the following:Plant: 3310Purchasing Group: 001Purchasing Organization: 3310Choose Go | A list of purchase requisitions is displayed. |  |
| 4 | Create the Purchase Orders | Follow these steps:Select the purchase requisition.Choose Create Purchase Order.On New Purchase Order screen that opens, choose Purchase Order Type as the standard purchase order (NB).Choose Order.The created purchase order is displayed in the Display Purchase Order - Advanced (ME23N) app | The purchase order is created. |  |

#### Goods Receipt for Purchase Order

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

This section describes test procedures for each process step that belongs to this scope item.

Table 18:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) app. | The Post Goods Movement screen is displayed. |  |
| 3 | Post Goods Receipt | Enter the following:Trans/Event: Goods ReceiptReference Document: Purchase OrderOrder: <Enter the Purchase order number from the previous step>GR goods receipt: 101Choose Execute.Following details are available:Document Date: default datePosting Date: DefaultFollow these steps:Go to Quantity tab and enter the quantity. For example :1Select the checkbox for Item OKChoose Post. | The material document is posted. |  |

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods issue from storage location.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 19:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) app. | The Post Goods Movement screen is displayed. |  |
| 3 | Post Goods Issue | Enter the following:Trans/Event: Goods IssueReference Document: OrderOrder: <Enter the maintenance order number>GI for order: 261Choose Execute.Following details are available:Document Date: default datePosting Date: DefaultFollow these steps:Go to Quantity tab and enter the quantity. For example, 1Select the checkbox for Item OKChoose Post. | The material document is posted. |  |

#### Submit Order for Scheduling

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once Preparation is done and backlog is reviewed, the order can be set for Ready to Schedule to start Scheduling phase.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 20:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Find Maintenance Orders (F2175) app | A list of orders is displayed. |  |
| 3 | Get List of Maintenance Orders | Enter the following:Technical object: 233100091Choose Go | A list of maintenance orders is displayed based on the filter criteria. |  |
| 4 | Set Order to Ready to Schedule | Select the order by selecting the checkbox.Choose Change Status > Ready to Schedule | The maintenance order is in Scheduling phase. |  |

#### Add Safety Instructions (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

|  |
| --- |
| Note To keep workers safe at their workplace while operating a dangerous equipment, it's necessary to supply them with safety instructions. This test procedure shows how to include safety instructions in a maintenance order.Note You need to activate the scope item ‏54A (Health and Safety Management) . If you have activated the scope item ‏54A, the configuration expert can enable the integration with the Activate Integration with Environment, Health, and Safety activity. For more information, see [Configuration Environment of SAP S/4HANA Cloud Public Edition.](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/0b3f87579f345c08e10000000a441470.html?version=2202.503). |

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 21:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Change Maintenance Order (EAMS_WDA_ORDNTF_OIF) app. | The app opens. |  |
| 3 | Enter Order Number | Enter the order number and choose Continue | Change Maintenance Order screen is displayed. |  |
| 4 | Add Safety Instructions | Follow these steps:Go to the Documents tab. You can see an overview of the documents.Choose the Add Safety Instructions button under Document Assignments.Enter the required parameters and choose Go to get the list of safety instructions.Select the required safety instructions checkbox and choose OK.You can also choose Show/Hide Documents of Dependent Objects to get list of documents assigned to a technical object.Select the required safety instructions checkbox and choose Assign Document to Order under Maintain Document Assignments dropdown list.You can also choose to assign a document to an operation or suboperation or assign a document to a material or a service.Choose Save. | Safety Instructions are included in the maintenance order. |  |

#### Schedule Maintenance Order and Submit for Execution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the Maintenance Planner can dispatch the maintenance orders for execution.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 22:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Find Maintenance Orders (F2175) app. | The app opens. |  |
| 3 | Review List of Maintenance Order | Enter the following:Technical object: 233100091Choose Go | A list of maintenance orders is displayed based on the filter criteria.You can review and check if the order is in Scheduling phase. |  |
| 4 | Set Orders to Ready for Execution | Select the order by selecting the checkbox.Choose the Dispatch Operations button.Note If the scope item 43R (Resource Scheduling) is activated, the corresponding applications can be used for dispatching the operations. | The order operations are dispatched and the maintenance order is in Execution phase. |  |

#### Manage Output

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The maintenance planner can search and apply filters to identify maintenance orders or order operations and create work pack. A work pack consists of a list of job packs. The job packs consists of the corresponding maintenance order operations (jobs). You can create one output request for multiple job packs.

With the Manage Work Packs (F6065) app, you can find existing work packs, select work packs, job packs, and include items in them. You can send them for output immediately or schedule them to be eligible for the mass output.

Work packs allow you to include multiple output types and leverage support for print and email channels for the output.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 23:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Supervisor. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Find Maintenance Orders(F2175) app. | The app opens. |  |
| 3 | Review List of Maintenance Orders | Enter the following:Technical Object: 233100091Choose Go. | A list of maintenance orders is displayed based on the filter criteria. |  |
| 4 | Create Work Pack | Select the Order checkbox and choose Create Work Pack.A popup window appears. Enter the following:Work Pack Name: <Entry of your Choice>Work Pack Type: <Entry of your Choice>Group By <Entry of your Choice>Include operations used in other work packs: Select this checkbox.Note If this checkbox is not selected, then it will skip the order operation for which the work pack already existsChoose Save.Note A work pack can also be created using multiple operations from different orders using the Find Maintenance Orders and Operations - Dispatching (F2173) app. | A message informs you that the work pack creation has been scheduled and you can check the application log to track the status. |  |
| 5 | Check Application Logs | Follow these steps:Choose the Application Logs button.Choose Go.Select the work pack created in previous step to view the log details. | The work pack is created, and the log details are shown with a message and the work pack ID. |  |
| 6 | Access the App | Open the Manage Work Packs (F6065) app. | The app opens. |  |
| 7 | Search Work Pack | Enter the following:Work Pack: Enter the work pack ID created in the previous step.Choose Go.Choose the work pack. | The work pack is displayed based on the filter criteria and work pack details are displayed. |  |
| 8 | Add/Delete Jobs(Optional) | Follow these steps:Go to the Job Packs tab and select the job pack.Go to the Jobs tab and choose the Add icon to add a job.Select the required jobs and choose Add on the popup window.OrSelect the job and choose Delete icon to delete the job. Choose Delete on the popup window. | Job is added or deleted. |  |
| 9 | Send Output | Follow these steps:Go to the Output Items tab.Select one or more items and choose the Send Output button.Choose the Show More per Row icon.To preview the shop paper, choose the icon to display the document. | The item ID is sent for output. |  |
| 10 | Add Attachments to Output | Follow these steps:Go to the Output Items tab.Choose the Show More per Row icon.Select the item ID.Choose the Edit button.Choose the number specified on the Attachments field.A pop window will appear.The attachment will be displayed under Available Attachments.To get output of the attachments, use below options:Merge with Form Template: Drag the document from Available Attachments to Merge with form template section.Additional Attachments for Output: Drag the document from Available Attachments to Additional Attachments for Output section.To preview the final output document, choose the icon to display the document. | With the first option, the attachment will be merged with the work pack document output.With the second option, the attachment will be printed as additional document along with work pack form. |  |

#### Execute Maintenance Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the Maintenance Technician executes the pre and main operations.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 24:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Technician. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Perform Maintenance Jobs (F5104A) app. | The app opens. |  |
| 3 | Get List of Maintenance Order Operations | Enter the following:Execution Object: The maintenance order number which was dispatched for execution in the previous stepChoose Go. | A list of dispatched operations for the selected order is displayed. |  |
| 4 | Assign Operations | Select the operations and choose Assign to MeNote The Assign to Me button is enabled only if the order operation is not assigned to anyone | The operations are assigned to you. |  |
| 5 | Select the Operation for Processing | Choose the operation and navigate to the Perform Maintenance Job screen. | Perform Maintenance Job screen is displayed with the details of the operation. |  |
| 6 | Start the Operation | Choose Start. | The subphase is changed to Work in Execution. |  |
| 7 | Review Components | Go to Components tab and review the planned component details. | The component details are reviewed. |  |
| 8 | Goods Issue & Return for the issued component (Optional) for planned Components | Go to Planned Components in the Components tabChoose Post for the component that the maintenance technician wants to issue.The Post Goods Issue screen is displayed. Enter the required quantity and the movement description.Choose Post.Its possible to return already issued component. Choose Return for the component that the maintenance technician wants to return.The Return Goods screen is displayed. Enter the required quantity and choose Return.A new line item for the respective component is added.Choose Post.The Post Goods Return screen is displayed. Enter the required quantity and the movement description.Choose Post.Note If material is serialized, in the post goods issue screen,enter the required quantity and movement description,then choose next to enter the serial number | The components are issued or returned. |  |
| 9 | Planned return of components (optional) | Go to Planned Components in the Components and Services tab.Choose Post for the component that the maintenance technician wants to return (line item will have an orange marking on the extreme left side)The Post Goods Return screen is displayed. Enter the required quantity and the movement description.Choose PostNote If material is serialized, in the post Goods return enter the required quantity and movement description,then choose next to enter the serial number | The components are returned |  |
| 9 | Review Attachments | Go to the Attachments tab to review the attachments. If required, you can also upload new files and add a link. | The attachments are reviewed.The files and links are added. |  |
| 10 | Pause and Resume Work | Choose Pause button to pause the work.After you pause the work, you can restart the work by choosing Resume. | For an operation that has been paused, the subphase will be Work Paused.When you resume the work, the subphase changes to Work in Execution. |  |
| 11 | Time Confirmation | Choose Record Time on the top left corner of the Perform Maintenance Job screen. The Record Time screen is displayed. Enter the following:Actual work. For example, 4 hoursRemaining work, if any. For example, 2 hours.Enter the confirmation text as required.Select the checkbox Final Confirmation and choose Record to do the final confirmation for the operation.Repeat this for all the operations in the PRE and MAIN execution stages. | The final confirmations are posted and can be reviewed in the Confirmation tabThe work progress is shown as 100 %.The subphase is changed to Work Finished. |  |
| 12 | Add Measurement (Optional) | Follow these steps:Go to Measurements tabSelect All Measuring Points from the Technical Object Association dropdown list.Go to Latest Reading tabChoose Add Meaurements.Enter the current reading for the measuring point and press Enter.Select the date and the time using the Calender button.Choose Save. | The measurement reading is updated and can be seen in the Previous Reading column of the corresponding measuring point. |  |

#### Complete Main Work

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the Maintenance Technician has executed the Pre and Main operations and finally confirmed them, the Maintenance Supervisor can change the status of the maintenance order to Main Work Completed.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 25:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Supervisor. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Find Maintenance Orders (F2175) app. | A list of maintenance orders is displayed. |  |
| 3 | Get List of Maintenance Orders | Enter the following:Technical object: 233100091Choose Go. | A list of maintenance orders is displayed based on the filter criteria. |  |
| 4 | Set Order Status to Order Main Work Completed | Select the order by selecting the checkbox.Choose Change Status > Main Work Completed . | The Main Work Completed screen is displayed. |  |
| 5 | Enter Reference Data | Enter the following:Main Work Completion Date and Time: The default values are displayed. Use the calendar icon to change the values.Set Main Work Completion Date and Time as Reference Date and Time: Select this checkbox.Choose OK | The order status is set to Order Main Work Completed. |  |

#### Maintain Service Entry Sheet

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

This section describes test procedures for each process step that belongs to this scope item.

Table 26:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Manage Service Entry Sheets - Lean Services (F2027) app. | The app opens. |  |
| 3 | Enter Field ValuesCase 1: Purchase service without material numberCase 2: Purchase service with material number | Choose Create.On the Service Entry Sheet screen, enter the following:Name of Service Entry Sheet: <SES Name>, for example, Vincent SunReference Purchase Order: <Purchase order you created>The Add Purchase Order Items dialog box is displayed, choose the checkboxes next to the required purchase order items.Increase or decrease the service entry sheet items using the "+" / "-" buttonsChoose the Add button.Enter the posting date for goods receipt: <Today’s date>In the Items area, choose Purchase Order Item and enter the following for each item:Performance Period: <Enter the date range>Stated Quantity: < Stated Quantity >. For example,10Unit of measure: <Unit>.For example, HChoose Apply. |  |  |
| 4 | Add Attachments in Service Entry Sheet (Optional) | You can upload files using the Upload button or add a link to the service entry sheet and view the existing attachments by following one of these:On the header level, go to tab AttachmentsOn the item level, go to tab Items, open the details and go to tab Attachments.If the attachments are not required any longer, you can delete them.You can view the attachments and save them on your device regardless of the status of the service entry sheet.You can add or delete attachments only while editing the service entry sheet. This means that the status of the service entry sheet must be In Process. |  |  |
| 5 | Create Service Entry Sheet | Choose Create | The service entry sheet is created. |  |
| 6 | Send for Approval | Choose Send for Approval. | The service entry sheet is sent for approval. |  |
| 7 | Check the Status of the Service Entry Sheet. | On the Manage Service Entry Sheets screen, follow these steps:Search for the service entry sheet that you had created aboveCheck the status of the service entry sheet.Send service entry sheet for approval if approval is required.If the status is Approved, do not send the service entry sheet for approval with flexible workflow. |  |  |

#### Execute Post Work Operations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step the technician will execute post operations activities (if any) and also update the malfunction details and failure data.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 27:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Technician. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Perform Maintenance Jobs (F5104A) app. | The app opens. |  |
| 3 | Get List of Maintenance Order Operations | Enter the followingOrder: The maintenance order number which was dispatched for execution in the previous stepChoose Go | A list of dispatched operations for the selected order is displayed. |  |
| 4 | Select the Operation for Processing | Choose the operation in POST stage to navigate to the Perform Maintenance Job screen. | Perform Maintenance Job screen is displayed with the details of the operation. |  |
| 5 | Start the Operation | Choose Start. | The subphase is changed to Work in Execution. |  |
| 6 | Edit Malfunction Data | Follow these steps:Go to the Malfunction Data section.Choose the Edit button.The Edit Malfunction Data screen is displayed.Select an effect from dropdown list.Select a failure mode from dropdown list.Select a detection method from dropdown list.Enter Malfunction Start Date and Time as today's date and time in the following format: 09:00:00 amEnter Malfunction End Date and Time as today's date and time in the following format: 11:00:00 am.Select the checkbox if there is a breakdown. The breakdown duration is calculated.Enter the malfunction long text.Click on Save button. | The malfunction data is saved. |  |
| 7 | Record Malfunction Details | Follow these steps:Go to the Malfunction Data → Malfunction Details.Choose the Add button.The Add Malfunction Data screen is displayed.Enter the following details in the Damage Details tab:Select the object part from dropdown list.Select the damage code from dropdown list.Enter a description for the damage.Enter the following details on the Cause tab:Select the cause code from dropdown list.Enter a description for the cause.Select the Root Cause radio button.Enter the following details on the Activity tab:Select the activity code from dropdown listEnter a description for the activity.Click Record button.You can add additional causes and activities using the New Cause and New Activity buttons respectively. | The malfunction details are recorded. |  |
| 8 | Time confirmation | Choose Record Time on the top right corner of the Perform Maintenance Job screen.The Record Time screen is displayed. Enter the following details:Enter the actual work. For example, 4 hoursEnter the remaining work if any. For example , 2 hours.Enter a description for the confirmation as required.Select the Final Confirmation checkbox and choose Record to do the final confirmation on the operation.Repeat this for all the operations in the POST execution stage. | The final confirmations are posted and can be reviewed under the Confirmation tab.The work progress is shown as 100 %.The subphase is changed to Work Finished. |  |

#### Review Failure Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the supervisor can review the failure data updated by the technician.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 28:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Supervisor. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Find Maintenance Orders and Operations - Dispatching (F2173) app. | The app opens. |  |
| 3 | Get List of Maintenance Order Operations | Enter the following:Order: The maintenance order number from the previous step.Choose Go. | A list of operations for the selected order is displayed. |  |
| 4 | Review and Verify the Details | Choose the maintenance notification number.Note If the notification is not displayed, follow the below steps:Choose Settings from the top right context menu.Choose OK.Click the notification to navigate to required application.In the displayed dialog box, choose Performance Maintenance Job.Select the required operation.Go to the Malfunction Data tab and verify the details. | The malfunction details are reviewed. |  |

#### Review Maintenance Cost

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Maintenance planner can review the cost of maintenance orders.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 29:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Maintenance Order Costs - Plan / Actual (F4603) app. | The app opens. |  |
| 3 | Get Details | Enter the following details as filters:Relative Date Function: Previous 30 daysG/L Account Hierarchy: YPS2Ledger: 0LCompany Code: 3310Equipment: 233100091Choose Go.Note If data is not displayed, it can be due to the Relative Date Function field is set to a past date. | Based on the filter values, different types of maintenance costs are analyzed and reviewed. |  |

#### Technically Complete Maintenance Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The maintenance notification is completed and the maintenance order is technically completed after the required maintenance work has been performed.

The technical completion clears all the purchase requisitions, open reservations, and capacities still outstanding for the maintenance order.

Nevertheless, the order can continue to receive costs, for example, through invoice receipts for delivered and used materials. However it is blocked for all changes in the processing.

The order settlement transfers the costs incurred that were temporarily collected for the maintenance order, to the recipient, for example, to the cost center for the maintained object. This process step shows you how to technically complete a maintenance order.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 30:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Find Maintenance Orders (F2175) app. | The app opens. |  |
| 3 | Get List of Maintenance Orders | Enter the following:Order Type: Reactive MaintenanceChoose GO. | A list of maintenance orders is displayed based on the search criteria. |  |
| 5 | Set order status to Technically Completed | Select the order by selecting the check box.Choose Change Status > Complete Technically. | The Complete Technically screen is displayed. |  |
| 6 | Enter Reference Data | Enter the following:Completion Date/Time: The default values are displayed. Use the calendar icon to change the values.Keep Default Values: Select this checkboxComplete Assigned Notifications: Select this checkbox if you want to complete the assigned notifications.Choose Complete Technically | The order is technically completed. |  |

#### Create Supplier Invoice with PO/GR Relation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the invoice with reference to the purchase order.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 31:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Payable Accountant - Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open the App | Open Create Supplier Invoice - Advanced (MIRO). | The app opens. |  |
| 3 | Navigation | If the system prompts you, enter the following and choose Continue:Company Code: 3310 | The Enter Incoming Invoice screen is displayed. |  |
| 4 | Enter Basic Data | Enter the following:Transaction: InvoiceInvoice Date: Today's datePosting Date: Today's dateReference: <Reference invoice number from invoicing party>Amount: <Amount according to the invoice value>.Currency: AEDSelect Calculate TaxTax Code: Enter the tax code.If there is no tax, specify the tax code I0 (for Brazil, it is 00).If G/L account is subjected to tax, ensure that you enter an appropriate tax code. | Basic data is entered. |  |
| 5 | Enter Purchase Order References | On the Purchase Order References screen, make the following entries:Reference Document Category: Purchase Order/ Scheduling AgreementPurchase Order: Enter the purchase order you posted in the previous step. | The Purchase Order References screen is displayed. |  |
| 6 | Check the Purchase Order Items Data | Check the amount, the quantity and the tax code. | The amount and the quantity correspond to the values of the goods receipts. |  |
| 7 | Check Tax Code | In the Tax area, check the tax code information and the tax amount. |  |  |
| 8 | Simulate Supplier Invoice and Check Messages | Choose Simulate.If there are no differences (or if the value is within the defined tolerance), the Simulation screen displays. You can check the results in the Simulation Overview and Simulation Details areas.Review the Gross Invoice Amount against the items plus tax amount (if tax code is 10, (for Brazil, it is 00), you do not have any tax amount) |  |  |
|  | Post Invoice | Choose Post. | The invoice document is posted. |  |

### Emergency Work

#### Create Emergency Work

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is the Initiation phase of the maintenance process where a planner can create a maintenance notification for an emergency work.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 32:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Maintenance Supervisor. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Maintenance Notifications - New Version (F5777). | The Manage Maintenance Notifications screen is displayed. |  |
| 3 | Create Emergency Work | From the List page, choose Create > Emergency .A popup screen appears.Enter the following details: -Technical Object : 217100091Search for an object in the search field by entering keywords such as 'water pump' and choose Go.From the results, select the equipment with number 217100091 and description Cooling Water Circulation Pump.Description: Detailed information regarding the maintenance notification can be updated here.Choose Create. | A detail page opens where you can provide more inputs. |  |
| 4 | Enter Details | Enter the following details:Current Location: PlatformFailure Mode Group: PM GeneralFailure Mode: VibrationDetection Method: InspectionEffect: Production restricted. Effect can be selected from the list available.Malfunction Start Date Time: Enter the date and the timeLong Text: Answer the predefined questions.Description: Detailed information regarding the maintenance notification can be updated here. | The details are entered. |  |
| 5 | Assess Priority | Assess Priority: Select relevant consequence and likelihood for each consequence category and choose Assess button on the right bottom. Review the details and choose Apply.Ensure that the following prerequisites are met:Ensure that the technical object is populated.Technical object master data has the maintenance plant populated in the Location Data tab. | Priority is automatically calculated and populated on the screen. |  |
| 6 | Add Attachment/URL (Optional) | In the Attachments section, choose Upload. Select the files you want to upload. You can also choose Add a Link to provide link to relevant information for the maintenance notification. | The files and the links are added to the maintenance notification. |  |
| 7 | Save | Choose Create. | The maintenance notification is created.Based on this accepted notification, the system creates a maintenance order, releases it and subsequently dispatches the order operation. This means that the maintenance order of the Reactive Maintenance order type is passed directly to the Execution phase without running through any intermediate planning, approval, preparation, and scheduling steps. |  |

|  |
| --- |
| Note Execution of the emergency maintenance order can be done in the same way as explained in reactive maintenance process.Maintenance planner can add additional operations to involve additional maintenance technicians in the repair work order and dispatch the newly entered operations manually. |

### Minor Work

#### Create Minor Work

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is the Initiation phase of the maintenance process where a planner can create a maintenance request for a minor work.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 33:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Maintenance Supervisor. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Maintenance Notifications - New Version (F5777). | The Create Maintenance Notification screen is displayed. |  |
| 3 | Create Minor Work | From the List page, choose Create > Minor .A popup screen appears.Enter the following details: -Technical Object : 217100091Search for an object in the search field by entering keywords such as 'water pump' and choose Go.From the results, select the equipment number 217100091 and description Cooling Water Circulation Pump.Description: Detailed information regarding the maintenance notification can be updated here.Choose Create. | A detail page opens where you can provide more inputs. |  |
| 4 | Enter Details | Enter the following details:Current Location: PlatformFailure Mode Group: PM GeneralFailure Mode: VibrationDetection Method: InspectionEffect: Production restricted. Effect can be selected from the list available.Malfunction Start Date Time: Enter the date and the timeNotification Processing Context: Minor WorkLong Text: Answer the predefined questions.Description: Detailed information regarding the maintenance notification can be updated here. | The details are entered. |  |
| 5 | Assess Priority (Optional) | Assess Priority: Select relevant consequence and likelihood for each consequence category and choose Assess button. Review the details and choose Apply.Ensure that the following prerequisites are met:Ensure that the technical object is populated.Technical object master data has the maintenance plant populated in the Location Data tab. | Priority is automatically calculated and populated on the screen. |  |
| 6 | Add Attachment/URL (Optional) | In the Attachments area, choose Upload. Select the files you want to upload. You can also choose Add a Link to provide link to relevant information for the maintenance notification. | The files and the links are added to the maintenance notification. |  |
| 7 | Save | Choose Create. | The maintenance notification is created. |  |

#### Record Malfunction Details

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Maintenance Technician can check the accepted maintenance requests in this application with various filter options and record the malfunction data.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 34:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Supervisor. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Maintenance Notifications - New Version (F5777) | The app opens. |  |
| 3 | Record Malfunction Details | Filter the list with Processing context Minor workSelect the maintenance notification created in the previous step.Go to the Malfunction Details section of object page and add the details.Enter the following details in the Damage Details tab:Select the object part from dropdown list.Select the damage code from dropdown list.Enter a description for the damage.Select the line item to add Cause and activities:Select the cause code from dropdown list.Enter a description for the cause.Select the Root Cause radio button.Enter the following details on the Activity tab:Select the activity code from dropdown listEnter a description for the activity.You can add additional causes and activities using the New Cause and New Activity buttons respectively.Enter the following details in the Malfunction Information sub section of Notification Scope section:Enter the malfunction start date and time as today's date and time in the following format: 09:00:00 amEnter the malfunction end date and time as today's date and time in the following format: 11:00:00 am.Select the checkbox if there is a breakdown. The breakdown duration is calculated.Choose the Submit button. | Malfunction details are captured. |  |
| 4 | Complete Notification | Follow these steps:Select the notification.Choose Complete Notification on the top right screen. The Complete Notification screen is displayed.Enter Reference Date Time: The default values are displayed. Use the calendar icon to change the values.Choose Complete Notification button. | Notification is completed. |  |

## Appendix

### Process Integration

#### Preceeding Processes

You must first complete the following processes before you start with the test steps:

Table 35:

| Process | Business Condition |
| --- | --- |
| Create New Open MM Posting Period (BNZ) | A new MM period must exist. |
| Period-End Closing - Maintenance Orders (BF7) | Activity types rates to be maintained. |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

Table 36:

| Process | Business Condition |
| --- | --- |
| Accounts Payable (J60) | Use the master data from this test script and execute the following steps:Invoice payment preparationPayment runSingle outgoing paymentManual payment online |
| Period-End Closing - Maintenance Orders (BF7) | A maintenance order is technically completed as part of this script. |

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
> Flagged while digesting this document, not verified: Sample equipment is 233100091 in prerequisites and most steps, but notification creation steps (create notification, emergency, minor work) use technical object 217100091 labelled Cooling Water Circulation Pump.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/test-script-corrective-maintenance-bh1-ae-sap-s-4hana-cloud-public-edi]]
- related-to :: [[14-maintenance-service-and-projects/test-script-emergency-maintenance-bh2-ae-sap-s-4hana-cloud-public-edit]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4HH_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 112,955 chars in the whole document
