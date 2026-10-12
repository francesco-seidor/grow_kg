---
id: 14-maintenance-service-and-projects/test-script-proactive-maintenance-4hi-ae-sap-s-4hana-cloud-public-edit
title: "Test Script: Proactive Maintenance (4HI_AE) - SAP S/4HANA Cloud Public Edition (4HI_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 4HI (UAE): proactive maintenance planning, order processing, execution, procurement and invoicing steps in Fiori, dated 19-06-26."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/preventive-and-proactive-maintenance]
aliases: [4HI_S4CLD2608_BPD_EN_AE]
keywords: [Preventive and Proactive Maintenance Plans, proactive maintenance, maintenance plans, maintenance strategies, general task lists, measurement documents, maintenance orders, multiple counter plan, order approval workflow, maintenance backlog]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4HI_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1031
topic: 14-maintenance-service-and-projects/preventive-and-proactive-maintenance
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Proactive Maintenance (4HI_AE) - SAP S/4HANA Cloud Public Edition (4HI_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4HI_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Preventive and Proactive Maintenance Plans** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Proactive Maintenance (4HI_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232855170)

[2 Prerequisites 5](#_Toc232855171)

[2.1 System Access 5](#_Toc232855172)

[2.2 Roles 5](#_Toc232855173)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232855174)

[2.4 Business Conditions 8](#_Toc232855175)

[3 Preliminary Steps 9](#_Toc232855176)

[3.1 Initializing Material Stock 9](#_Toc232855177)

[3.2 Configure Flexible Workflow for Maintenance Orders 10](#_Toc232855178)

[3.3 Create Planning Bucket 11](#_Toc232855179)

[3.4 Maintain Cost Rates 13](#_Toc232855180)

[3.5 Create Purchasing Information Record 14](#_Toc232855181)

[3.6 Create Maintenance Plan Class (Optional) 16](#_Toc232855182)

[4 Overview Table 18](#_Toc232855183)

[5 Test Procedures 21](#_Toc232855184)

[5.1 Time-Based Single Cycle Plan 21](#_Toc232855185)

[5.1.1 Create General Task List 21](#_Toc232855186)

[5.1.2 Create Maintenance Item 24](#_Toc232855187)

[5.1.3 Create Maintenance Plan 25](#_Toc232855188)

[5.1.4 Schedule Maintenance Plan 27](#_Toc232855189)

[5.2 Time-Based Strategy Plan 29](#_Toc232855190)

[5.2.1 Maintain Maintenance Strategies 29](#_Toc232855191)

[5.2.2 Create General Task List 31](#_Toc232855192)

[5.2.3 Create Maintenance Item 34](#_Toc232855193)

[5.2.4 Create Maintenance Plan 35](#_Toc232855194)

[5.2.5 Schedule Maintenance Plan 38](#_Toc232855195)

[5.3 Performance-Based Single Cycle Plan 39](#_Toc232855196)

[5.3.1 Create General Task List 39](#_Toc232855197)

[5.3.2 Create Maintenance Item 42](#_Toc232855198)

[5.3.3 Create Maintenance Plan 43](#_Toc232855199)

[5.3.4 Create Measurement Document 45](#_Toc232855200)

[5.3.5 Schedule Maintenance Plan 46](#_Toc232855201)

[5.4 Performance-Based Strategy Plan 47](#_Toc232855202)

[5.4.1 Maintain Maintenance Strategies 47](#_Toc232855203)

[5.4.2 Create General Task List 49](#_Toc232855204)

[5.4.3 Create Maintenance Item 52](#_Toc232855205)

[5.4.4 Create Maintenance Plan 54](#_Toc232855206)

[5.4.5 Create Measurement Document 56](#_Toc232855207)

[5.4.6 Schedule Maintenance Plan 57](#_Toc232855208)

[5.5 Multiple Counter Plan 59](#_Toc232855209)

[5.5.1 Create General Task List 59](#_Toc232855210)

[5.5.2 Create Maintenance Item 62](#_Toc232855211)

[5.5.3 Create Maintenance Plan 63](#_Toc232855212)

[5.5.4 Create Measurement Document 65](#_Toc232855213)

[5.5.5 Schedule Maintenance Plan 66](#_Toc232855214)

[5.6 Screen Maintenance notifications 68](#_Toc232855215)

[5.7 Create and Plan Maintenance Orders 69](#_Toc232855216)

[5.8 Submit Maintenance Order for Approval 73](#_Toc232855217)

[5.9 Approve Maintenance Order (Optional) 74](#_Toc232855218)

[5.10 Review and Release Maintenance Order 75](#_Toc232855219)

[5.11 Convert Purchase Requisitions into Purchase Orders 76](#_Toc232855220)

[5.12 Goods Receipt for Purchase Order 77](#_Toc232855221)

[5.13 Post Goods Issue 78](#_Toc232855222)

[5.14 Maintenance Backlog Overview 79](#_Toc232855223)

[5.15 Submit Order for Scheduling 83](#_Toc232855224)

[5.16 Add Safety Instructions (Optional) 84](#_Toc232855225)

[5.17 Schedule Maintenance Orders and Submit for Execution 86](#_Toc232855226)

[5.18 Manage Output 87](#_Toc232855227)

[5.19 Execute Maintenance Order 89](#_Toc232855228)

[5.20 Complete Main Work 91](#_Toc232855229)

[5.21 Maintain Service Entry Sheet 92](#_Toc232855230)

[5.22 Execute Post Work Operations 94](#_Toc232855231)

[5.23 Review Maintenance Cost 96](#_Toc232855232)

[5.24 Technically Complete Maintenance Order 97](#_Toc232855233)

[5.25 Create Supplier Invoice with PO/GR Relation 98](#_Toc232855234)

[5.26 Condition Based Maintenance (Optional) 100](#_Toc232855235)

[5.26.1 Create Measurement Document 100](#_Toc232855236)

[6 Appendix 102](#_Toc232855237)

[6.1 Process Integration 102](#_Toc232855238)

[6.1.1 Preceding Processes 102](#_Toc232855239)

[6.1.2 Succeeding Processes 102](#_Toc232855240)

## Purpose

Overview

Proactive maintenance allows you to prevent the failure or breakdown of an asset by implementing preventive maintenance and using proactive measures.

You can create a maintenance schedule in the form of a maintenance plan. Maintenance plans include task lists and relevant assets. A task list contains a sequence of tasks that can be planned for resources such as material, service, capacity, and so on. Maintenance planning is carried out based on the performance of an asset or by using time-based strategy or both, which creates maintenance demand. This process supports all the phases of business cycle such as planning, approval, preparation, scheduling, execution, post execution, and completion.

To enable safety instructions, you need to activate the scope item Health and Safety Management (54A).

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
| Employee | SAP_BR_EMPLOYEE | Self Services / Self Services / Employee Overview Space | SAP_BR_EMPLOYEE / SAP_CA_SPT_EMPLOYEE_CROSS_PC / SAP_EAM_SPT_EMPLOYEE_PC |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Maintenance Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331B | Std. storage 2 |  |
| Spare Parts | SP001 | Bearing | Spare parts |
| Spare Parts | SP002 | Coupling | Spare parts |
| Spare Parts | SP003 | Shaft | Spare parts |
| Spare Parts | SP004 | Gaskets 1mm | Spare parts |
| Spare Parts | SP005 | Mechanical Seal | Spare parts |
| Spare Parts | SP006 | Spur gear IS651 | Spare parts |
| Work Center | RES-0100 | Mechanics |  |
| Work Center | RES-0200 | Electric |  |
| Work Center | RES-0300 | Instrumentation |  |
| Characteristics | OPERATING_HOUR | Hour Meter Reading |  |
| Characteristics | PRESSURE | Pressure Reading |  |
| Counter Measuring Point | XXXXXX | Operating Hour | 1-999999 |
| Non Counter Measuring Point | XXXXXX | Pressure Guage | 1-999999 |
| Functional Location | 3310-XXX-XXX-XXXXX-XXXX-XXXX |  | 3310 and the substructures |
| Equipment | 23310XXXX |  | 233100001 ~233100092 |
| Cooling Water Circulation Pump | 233100091 |  | With SP001 ~ SP006 assigned |
| Domestic UAE Supplier 1 | 33300001 | Domestic UAE Supplier 1 |  |

For more information on creating master data objects, see the following Master Data Scripts (MDS):

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| 5LM | Create Functional Location |
| 5MF | Create Equipment |
| 5MH | Create Maintenance Work Center |
| 5MI | Measuring Point |
| 2J7 | Spare Parts |

This overview shows the bill of material structure and the usage of each component if you have activated all optional enhancements.

Table 2:

| Material | Level | Material Type | Unit | Characteristics of Material |
| --- | --- | --- | --- | --- |
| 233100091 | 0 | Equipment | PC | Cooling Water Circulation Pump |
| SP001 | 1 | ERSA | PC | Bearing |
| SP002 | 1 | ERSA | PC | Coupling |
| SP003 | 1 | ERSA | PC | Shaft |
| SP004 | 1 | ERSA | PC | Gaskets 1mm |
| SP005 | 1 | ERSA | PC | Mechanical Seal |
| SP006 | 1 | ERSA | PC | Spur gear IS651 |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period | You have completed the step described in the Create New Open MM Posting Period (BNZ) master data script. The posting period is up to date.To run through this scope item, the materials must be available in stock. |

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

This section describes test procedures for each process step that belongs to this scope item.

Table 3:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen is displayed. |  |
| 3 | Input Material | Enter the following and choose Enter:Material: < material number>. Select one of the spare parts material mentioned in the section Master Data, Organizational Data, and Other Data.Plant: 3310 | You have entered the details. |  |
| 4 | Select Stock | Select the icon next to the stock that you want to add as initial stock. For example:Storage Location: 331BUnrestricted-Use Stock | A dialog box opens. The storage location, stock type and current quantity are displayed according to the entries you selected in the previous steps. |  |
| 5 | Add Initial Entry | Enter the following and choose Post:Document Date: <today>Posting Date: <today>Stock Change: initial entryQuantity: <quantity number> | The material document is created and the stock has been added. |  |

### Configure Flexible Workflow for Maintenance Orders

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

Table 4:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Workflows for Maintenance Orders - Asset Management (F4989) app. | The Manage Workflows screen is displayed. |  |
| 3 | Check Automatic Approval of Maintenance Order | In Workflows list, choose Automatic Approval of Maintenance Order, Make sure workflow Automatic Approval of Maintenance Order is in active status. If not, select it and choose Activate. | The workflow item is activated. |  |
| 4 | Manage Workflow | You can also create custom workflows. When the workflow is triggered, it determines the agents who can approve the maintenance order.Below is a custom workflow created for referenceChoose Create and make following entries:Workflow Name: <Enter Text>Go to the START CONDITIONS area and choose Maintenance Order Type is <Enter Order Type> |  |  |
| 5 | Create Step Sequence | Go to the STEPS area, and choose Create, then make the following entries on the next screen:Go to the RECIPIENTS area:Assignment By: UserUser: <Enter User ID>Step to be completed by: One of the recipients.Step Conditions:Go to the STEP CONDITIONS area and choose Main Work Center of the order is <Enter Work center>Choose Create. |  |  |
| 6 | Save Workflow | Choose Save. | Workflow is created. |  |
| 7 | Activate Workflow | Go back to workflow list. Select the required workflow and choose Activate. | The workflow is activated. |  |

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

Table 5:

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

Table 6:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Cost Accountant - Overhead. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Cost Rates - Plan (F3162) | The app opens. |  |
| 3 | Check Actual Cost Rates | Set the following filters and choose Go.Valid On: TodayCost Center: 33101701Activity Type: 11Currency: For example, AEDCheck if there is a valid cost rate for given cost center, activity type, and period. | The actual cost rates for given cost centre, activity type and period are checked for valid values.Note You can skip the next step if there is a valid cost rate for given cost center, activity type, and period. |  |
| 4 | Maintain Actual Cost Rates | Choose Add and enter the followingCost Center: 33101701Activity Type: 11From Fiscal Year: Current YearFrom Period: Current PeriodFixed Rate: 100Currency: For example, AEDPer:1Activity Unit: HChoose Save. | Cost rates are created. |  |

### Create Purchasing Information Record

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

Table 7:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Manage Purchasing Info Records (F1982) app. | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record screen displays. |  |
| 4 | Enter Header Data | Go to header area and enter the following:Purchasing Info Record Category: StandardPurchasing Organization: 3310Supplier: 33300001Material: NL001Plant: 3310Purchasing Group: 001 | Header data is added. |  |
| 5 | Enter General Information | Enter the following:Available From: TodayAvailable To: 12/31/9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | Enter the following:Incoterm: EXWIncoterm Location 1: Vendor | Purchasing data is added. |  |
| 7 | Enter Delivery and Quantity Data | Enter the following:Delivery Time in Days: <XX Days>, for example, 1Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10.0Tax Code: <Tax Code>, for example, I0.Order Unit: PCStandard Order Quantity <Standard Order Quantity>, for example, 10 | Delivery and quantity data are added. |  |
| 8 | Enter Condition Data | Go to the Conditions area, choose the Create icon. Enter the following:Valid From: <Valid from Date>Amount: <Amount>, for example, 1Pricing Unit: <Pricing Unit>, for example, 1Valid To: <Valid to Date>Currency: <Currency>, for example, AEDChoose Apply. | Condition data is added |  |
| 9 | Enter Reference Data (Optional) | You can enter the reference data. | Reference data is added. |  |
| 10 | Create a Purchasing Information Record | Choose Create. | A purchasing information record is created. |  |

### Create Maintenance Plan Class (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating maintenance plan class data.

Procedure

Table 8:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open the App | Open Manage Classes (CL02) | The screen is displayed. |  |
| 3 | Enter Class Name and Class Type | On the Class screen, make the following entries:Class: <Class Name>Class Type: <080> Maintenance PlansChoose Create or press Enter. | A new screen opens with details such as basic data, keywords, char., and texts. |  |
| 4 | Enter Basic Data | In the Create Class screen, on the Basic Data tab, make the following entries:Description: for example, maintenance plan classStatus: RELEASEDSame classification: Select Warning message. |  |  |
| 5 | Enter Characteristic | In the Char tab, enter the required characteristics. |  |  |
| 6 | Save Your Data | Choose Save. | Class type 080: Class XXXXXX created. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Proactive Maintenance - Time-Based Single Cycle Plans |  |  |  |
| Create General Task List | Maintenance Planner | Create Task List (EAMS_WDA_TL_OIF_V2 (EAMS_WDA_TL_OIF_CFG_V2)) | The task list is created. |
| Create Maintenance Item | Maintenance Planner | Manage Maintenance Items (F5356) | The maintenance item is created. |
| Create Maintenance Plan | Maintenance Planner | Manage Maintenance Plans (F5325) | The maintenance plan is created. |
| Schedule Maintenance Plan | Maintenance Planner | Schedule Maintenance Plan (IP10) | The maintenance plan is scheduled. |
| Proactive Maintenance - Time-Based Strategy Plans |  |  |  |
| Maintain Maintenance Strategies | Maintenance Planner | Maintain Maintenance Strategies (IP11) | The maintenance strategy is created. |
| Create General Task List | Maintenance Planner | Create Task List (EAMS_WDA_TL_OIF_V2 (EAMS_WDA_TL_OIF_CFG_V2)) | The task list is created. |
| Create Maintenance Item | Maintenance Planner | Manage Maintenance Items (F5356) | The maintenance item is created. |
| Create Maintenance Plan | Maintenance Planner | Manage Maintenance Plans (F5325) | The maintenance plan is created. |
| Schedule Maintenance Plan | Maintenance Planner | Schedule Maintenance Plan (IP10) | The maintenance plan is scheduled. |
| Proactive Maintenance - Performance-Based Single Cycle Plan |  |  |  |
| Create General Task List | Maintenance Planner | Create Task List (EAMS_WDA_TL_OIF_V2 (EAMS_WDA_TL_OIF_CFG_V2)) | The task list is created. |
| Create Measurement Document | Maintenance Technician | Create Measurement Document for Technical Object (EAMS_WDA_MD_OIF) | The measurement document is created. |
| Create Maintenance Item | Maintenance Planner | Manage Maintenance Items (F5356) | The maintenance item is created. |
| Create Maintenance Plan | Maintenance Planner | Manage Maintenance Plans (F5325) | The maintenance plan is created. |
| Schedule Maintenance Plan | Maintenance Planner | Schedule Maintenance Plan (IP10) | The maintenance plan is scheduled. |
| Proactive Maintenance - Performance-Based Strategy Plan |  |  |  |
| Maintain Maintenance Strategies | Maintenance Planner | Maintain Maintenance Strategies (IP11) | The maintenance strategy is created. |
| Create General Task List | Maintenance Planner | Create Task List (EAMS_WDA_TL_OIF_V2 (EAMS_WDA_TL_OIF_CFG_V2)) | The task list is created. |
| Create Maintenance Item | Maintenance Planner | Manage Maintenance Items (F5356) | The maintenance item is created. |
| Create Maintenance Plan | Maintenance Planner | Manage Maintenance Plans (F5325) | The maintenance plan is created. |
| Create Measurement Document | Maintenance Technician | Create Measurement Document for Technical Object (EAMS_WDA_MD_OIF) | The measurement document is created. |
| Schedule Maintenance Plan | Maintenance Planner | Schedule Maintenance Plan (IP10) | The maintenance plan is scheduled. |
| Proactive Maintenance - Multiple Counter Plan |  |  |  |
| Create General Task List | Maintenance Planner | Create Task List (EAMS_WDA_TL_OIF_V2 (EAMS_WDA_TL_OIF_CFG_V2)) | The task list is created. |
| Create Maintenance Item | Maintenance Planner | Manage Maintenance Items (F5356) | The maintenance item is created. |
| Create Maintenance Plan | Maintenance Planner | Manage Maintenance Plans (F5325) | The maintenance plan is created. |
| Create Measurement Document | Maintenance Technician | Create Measurement Document for Technical Object (EAMS_WDA_MD_OIF) | The measurement document is created. |
| Schedule Maintenance Plan | Maintenance Planner | Schedule Maintenance Plan (IP10) | The maintenance plan is scheduled. |
| Proactive Maintenance - Order Processing |  |  |  |
| Screen Maintenance Request | Maintenance Supervisor | Screen Maintenance Requests (F4072) | The maintenance request is accepted or rejected. |
| Create and Plan Maintenance Order | Maintenance Planner | Manage Maintenance Notifications and Orders (F4604) | The maintenance order is created. |
| Submit Order for Approval | Maintenance Planner | Manage Maintenance Notifications and Orders (F4604) | Maintenance order is submitted for approval. |
| Approve Maintenance Order | As per agent determined in workflow | My Inbox - All Items (F0862) | Maintenance order is approved |
| Review and Release Maintenance Order | Maintenance Planner | Manage Maintenance Notifications and Orders (F4604) | Maintenance order is released. |
| Maintenance Backlog Overview | Maintenance Planner | Maintenance Backlog Overview (F5105) | Maintenance backlog is reviewed |
| Convert Purchase Requisitions to Purchase Orders | Purchaser | Process Purchase Requisitions (F1048A) | Purchase requisitions are converted to purchase orders. |
| Goods Receipt for Purchase Order | Warehouse Clerk | Post Goods Movement (MIGO) | Goods receipt is posted. |
| Post Goods Issue | Warehouse Clerk | Post Goods Movement (MIGO) | Goods issue is posted. |
| Submit Order for Scheduling | Maintenance Planner | Find Maintenance Orders - Completion (F2175) | Maintenance order is ready to be scheduled. |
| Add Safety Instruction (Optional) | Maintenance Planner | Change Maintenance Order (EAMS_WDA_ORDNTF_OIF) | Safety instructions are added. |
| Schedule Maintenance Order and Submit it for Execution | Maintenance Planner | Find Maintenance Orders - Completion (F2175) | Maintenance order is scheduled. |
| Manage Output | Maintenance Supervisor | Find Maintenance Orders - Completion (F2175)Manage Work Packs (F6065) |  |
| Execute Maintenance Order | Maintenance Technician | Perform Maintenance Jobs (F5104A) | Time confirmation of pre and main maintenance order operations is done. |
| Complete Main Work | Maintenance Supervisor | Find Maintenance Orders - Completion (F2175) | Pre and main work are completed. |
| Maintain Service Entry Sheet | Purchaser | Manage Service Entry Sheets (F2027) | The service entry sheet is created. |
| Execute Post Work Operations | Maintenance Technician | Perform Maintenance Jobs (F5104A) | Post work operations are completed. |
| Review Maintenance Cost | Maintenance Planner | Maintenance Order Costs (F4603) | Maintenance cost is reviewed |
| Technically Complete Maintenance Order | Maintenance Planner | Find Maintenance Orders - Completion (F2175) | Maintenance order is technically completed. |
| Create Supplier Invoice with PO/GR Relation | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) | Supplier invoice is posted. |

## Test Procedures

### Time-Based Single Cycle Plan

#### Create General Task List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Using task lists, you can centrally define and manage maintenance tasks for your technical objects. General task lists can also help you to prepare maintenance plans and orders.

A task list group combines one or more task lists according to their logical features. Within a task list group, each task list is identified by a group counter. This enables you, for example, to combine several task lists in one group. Within the group, the system allocates a sequential number (the group counter) to each individual task list.

Prerequisites

- Technical objects in the form of functional locations, equipment, and maintenance assemblies.
- Organizational units such as maintenance planners and work centers.
- Cost centers defined in the master data of the technical objects.
- Maintenance spare parts and assemblies in the MM (Materials Management) module.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Maintenance Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Create Task List | Open Create Task List (EAMS_WDA_TL_OIF_V2 (EAMS_WDA_TL_OIF_CFG_V2)). | The Create Task List page appears. |  |
| 3 | Choose Task List Type | Choose Task List Type: General Maintenance Task List. | The Create General Maintenance Task List screen displays. |  |
| 4 | Enter Creation Parameters | Enter the following and choose Continue.Task List Group:Comment: Task List Group uses internal number range.Planning Plant: 3310Group Counter:Comment: The group counter would increase automatically if you create another task list under the same task list group.Overall Status: Released (general)Select the relevant profile for the plant.Key Date: <Today>Choose Continue. | The Create General Maintenance Task List page displays. |  |
| 5 | Maintain General Data | Make the following entries:Description: <Description> Enter a description. For example, Mechanical Inspection.Status: Released (General)Planner Group: YB1Work Center: RES-0100Work Center Plant: 3310Usage: 4System Condition: not in operationChoose Operation Data. | The Operation Data tab appears. |  |
| 6 | Maintain Operation Data | Make the following entries and choose Enter.Operation: 0010Description: Check the pumpWork: 2Unit: HCapacities: 2Stage: PREOperation: 0020Description: Check the bearingsWork: 1Unit: HCapacities: 1Stage: MAINOperation : 0030Description: Check the couplingWork: 2Unit: HCapacities: 2Stage: MAINOperation: 0040Description: Check the shaftWork: 3Unit: HCapacities: 3Stage: POSTChoose the Operation 0010.In the lower part of the screen, Details: Operation 0010, Check the pump section, choose Materials.Make the following entries and choose Enter.Material: SP005Quantity: 1Repeat the above step for other operations.Operation Item: 0020Material: SP001Quantity: 2Operation Item: 0030Material: SP002Quantity: 1Operation Item: 0040Material: SP003Quantity: 2Choose Save | The general task list is created. |  |

#### Create Maintenance Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A maintenance item describes which preventive maintenance tasks should take place regularly at a technical object or a group of technical objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Maintenance Planner. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Manage Maintenance Items app | Open Manage Maintenance Items (F5356). | The Manage Maintenance Items page appears. |  |
| 3 | Create Maintenance Item | To create a maintenance item, choose Create button on the top of the screen. Enter following details in the popup window:Item Description: Mechanical Inspection for PumpPlan Category: YM (Maintenance Request)Notification Type: Proactive Work (Y2). Press Enter.Reference Object Type: EquipmentReference Object: <Entry of choice>Task List: <Entry of choice>Comment: You can use the task list created in the previous step.Choose Create.Maintenance Item screen is displayed. Enter following details under Basic Details tab:Priority: <Entry of your choice>Choose Create.Note Maintenance items can also be created through the Manage Maintenance Plans (F5325) app.Note If you wish to generate a maintenance order from a maintenance plan then select the item category as PM (Maintenance Order). You also need to the select order type as Proactive Maintenance (YA02) in the subsequent screen.If you want the order to go through the order approval process, select the Do not Release Immediately button which is available only if the item category is PM (Maintenance Order). | The maintenance item is created. |  |

#### Create Maintenance Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Maintenance plan will have maintenance or inspection activities to be carried out for technical objects.

The frequency or strategy and, scope of the activities are defined in the maintenance plan.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open the App | Open Manage Maintenance Plans (F5325). | The app opens. |  |
| 3 | Create Maintenance Plan | Make the following entries, choose Continue:Plan Description: Mechanical Inspection for PumpPlan Category: Maintenance RequestPlan Type: Single Cycle (Time Based)Choose Create. | The Maintenance Plan screen is displayed. |  |
| 4 | Maintain Maintenance Plan Item Data | To create a maintenance item choose Create Item button by scrolling down to Maintenance item section. Enter following details in the pop-up window-Item Description: Mechanical Inspection for PumpNotification Type: Proactive Work (Y2) and press Enter.Reference Object Type: EquipmentReference Object: 23310XXXXTask List: Entry of your choiceYou can use the task list created in the previous step.Choose Create.Choose a maintenance item and enter following details under Basic Details tab:Maintenance Activity Type: YB4Priority: <Entry of your choice>Choose Apply. | The Maintenance Plan Planning Data screen is displayed. |  |
| 5 | Maintain Maintenance Plan Planning Data | In the Cycle section, make the following entries:Cycle Length: 1Cycle UoM: MONComment: Cycle Length/Cycle UoM defines the duration in which the maintenance is to be executed.Cycle Text: MonthlyIn the Schedule section, enter the following:Scheduling Duration: 365Comment: You can use the scheduling period to determine the length of time for which the system creates maintenance calls during maintenance plan scheduling.Start Date for Scheduling: <Current date>Comment: The start date is needed for mass schedule maintenance plans.End Date for Scheduling: <Entry of Choice>In the Scheduling Parameters section, enter the following:Shift Factor for Early Completion: 100Shift Factor for Late Completion: 100Comment: The shift factor in the event of early/late completion of a maintenance task defines the percentage of the shift to be applied to the calculation of the next date.Tolerance for Early Completion: 10Tolerance for Late Completion: 10Comment: The tolerance, in the case of early/late completion, determines the time span in which variances between actual and planned dates do not influence subsequent scheduling. The tolerance is defined as a percentage rate of the smallest interval between the maintenance cycles of the maintenance strategy.Cycle Modification Factor: 1Call Horizon: 50Comment: The call horizon determines when a maintenance call object, for example, a maintenance order should be generated for a maintenance call for the maintenance planned date.Completion Required: Select Yes or No using the toggle buttonComment: If you set this indicator, the system only generates the next call object once the preceding call object has been confirmed.Scheduling Indicator: TimeChoose Create. | The maintenance plan is created. |  |
| 6 | Assign Maintenance Item (Optional) | Alternatively, it is possible to assign existing maintenance item to a maintenance plan using the Assign Item button. To assign an item, follow these steps:Open the maintenance plan in Manage Maintenance Plans (F5325) app.Choose Assign Item.Select the required maintenance item and choose OK. | The maintenance item is assigned to the maintenance plan. |  |

#### Schedule Maintenance Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When you schedule your maintenance plan for the first time, you trigger the maintenance cycle. The system uses the scheduling information in the maintenance plan to calculate the due date of maintenance call object.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open the App | Open Schedule Maintenance Plan (IP10). | The app opens. |  |
| 3 | Search Maintenance Plan | Enter the following and choose Enter.MaintenancePlan:Use the single cycle plan (time based) created in the previous step. | The Schedule Maintenance Plan: Single Cycle Plan <Maintenance Plan number><Maintenance Plan number> page displays. |  |
| 4 | Schedule Maintenance Plan | Choose Start.On the Start Date screen, enter a start date. For example, enter current date.Start of cycle<: <Current Date>Choose Continue.You receive an overview of scheduled calls with plan date and call date of a schedule call based on the start date you entered and based on the scheduling parameters that are maintained in the maintenance plan.Comment: The scheduling list shows scheduled calls with assigned call dates. Each call has its own system status with scheduling type. The first call has the Type New Start with status Hold.When you want to create a Proactive Request/Order for the first time before reaching the call date, you can use the function release call.Flag the first row in Scheduling List.Choose Release Call.Choose Save and confirm all the messages that appear.To check the automatically created proactive work request, follow these steps:Open Schedule Maintenance Plan again.Enter the maintenance plan number.Choose Enter.In the Scheduling List, choose the first line you have called.Choose Display Call Object.Note the Proactive Maintenance Request number. | Maintenance plan has been scheduled |  |

Result

The maintenance plan has been scheduled.

Hint: In case you want to use mass scheduling instead of manually scheduling maintenance plans, you can use the tile Mass Schedule Maintenance Plans (F2774) with the business role Maintenance Planner.

To start mass scheduling, you must have entered a start date in the maintenance plan or have scheduled the maintenance plan once.

### Time-Based Strategy Plan

#### Maintain Maintenance Strategies

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A maintenance strategy represents a rule for the sequence of planned maintenance and inspection tasks.

A time-based maintenance strategy contains the maintenance packages that define the cycle in which the tasks must be performed, for example, every 10 days, every 3 months, and so on. It contains additional scheduling parameters such as shift factor, preliminary and follow-up buffers, and hierarchy. Maintenance strategies are required in strategy plans.

For each plant, you may use the same maintenance strategy. You can skip this step if the maintenance strategy exists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open the App | Open Maintain Maintenance Strategies (IP11). | The Change Maintenance Strategies: Overview page is displayed. |  |
| 3 | Create Maintenance Strategy | Choose New Entries. Enter the following.Name:EAM_<XX>Description: <Description> for example: Mechanical InspectionScheduling Indicator: TimeStrategy unit: MONChoose Save. | The new maintenance strategy is created. |  |
| 4 | Add Maintenance Packages | On the left side of the screen, in the Dialog Structure, double-click on the Packages folder.Choose New Entries.Enter the following:Package No.: 1Cycl. Length: 1Unit: MONMaintenance cycle text: MonthlyCycle short text: 1MHierarchy: 1Hierarchy short text: 1HRepeat the above step for further cycles. Create the following packages.Package No.: 2Cycl. Length: 3Unit: MONMaintenance cycle text: QuarterlyCycle short text: 3MHierarchy: 1Hierarchy short text: 1HPackage No.: 3Cycl. Length: 6Unit: MONMaintenance cycle text: Half-yearlyCycle short text: 6MHierarchy: 1Hierarchy short text: 1HPackage No.: 4Cycl. Length: 12Unit: MONMaintenance cycle text: YearlyCycle short text: 1YHierarchy: 1Hierarchy short text: 1HChoose Save. | The Change Maintenance Packages page is displayed.The maintenance packages are maintained in maintenance strategy. |  |

#### Create General Task List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Using task lists, you can centrally define and manage maintenance tasks for your technical objects. General task lists can also help you to prepare maintenance plans and orders.

A task list group combines one or more task lists according to their logical features. Within a task list group, each task list is identified by a group counter. This enables you, for example, to combine several task lists in one group. Within the group, the system allocates a sequential number (the group counter) to each individual task list.

Prerequisite

- Technical objects in the form of functional locations, equipment, and maintenance assemblies.
- Organizational units such as maintenance planners and work centers.
- Costs centers defined in the master data of the technical objects.
- Maintenance spare parts and assemblies in the MM (Materials Management) module.
- Maintenance strategy.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad displays. |  |
| 2 | OPen the App | Open Create Task List (EAMS_WDA_TL_OIF_V2 (EAMS_WDA_TL_OIF_CFG_V2)). | The app opens. |  |
| 3 | Choose Task List Type | Choose Task List Type: General Maintenance Task List. | The Create General Maintenance Task List screen displays. |  |
| 4 | Enter Creation Parameters | Enter the following:Task List Group:Comment: Task list group uses internal number range.Planning Plant: 3310Group Counter:Comment: The group counter would increase automatically if you create another task list for the same technical object.Overall Status: Released (general)Select the relevant profile for the plant.Key Date: <Today>Choose Continue. | The Create General Maintenance Task List page displays. |  |
| 5 | Maintain General Data | Enter the following:Description: <Description>Make your own description. For example, Mechanical InspectionStatus:Released (General)Planner Group: YB1Work Center: RES-0100Work Center Plant: 3310Usage: 4Maintenance Strategy: EAM_<XX>Comment: Please use the maintenance strategy created in the previous step.System Condition: not in operationChoose Operation Data. | The Operation Data tab appears. |  |
| 6 | Maintain Operation Data | Enter the following entries and choose Enter.Operation: 0010Description: Check the pumpWork: 2Unit: HCapacities: 2Stage : PreOperation: 0020Description: Check the BearingsWork: 1Unit: HCapacities: 1Stage : MainOperation : 0030Description: Check the couplingWork: 2Unit: HCapacities: 2Stage : MainOperation: 0040Description: Check the shaftWork: 3Unit: HCapacities: 3Stage : PostChoose the operation 0010.In the lower part of the screen, Details: Operation 0010, Check the pump section, choose Materials.Make the following entries and choose Enter.Material: SP005Quantity : 1Repeat the above step for other operationsOperation Item: 0020Material: SP001Quantity: 2Operation Item: 0030Material: SP002Quantity: 1Operation Item: 0040Material: SP003Quantity: 2Choose Maintenance Packages. | The Maintenance Packages tab appears. |  |
| 7 | Maintain Maintenance Packages | Make the following entries and choose Save.For operation 0010, set flag for Monthly, Quarterly, Half-yearly, YearlyFor operation 0020, set flag for Monthly,QuarterlyFor operation 0030, set flag for Half-yearly,YearlyFor operation 0040, set flag for Monthly, Quarterly, Half-yearly, Yearly | The general task list is created. |  |

#### Create Maintenance Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A maintenance item describes which preventive maintenance tasks should take place regularly at a technical object or a group of technical objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Maintenance Planner. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Manage Maintenance Items app | Open Manage Maintenance Items (F5356). | The Manage Maintenance Items page appears. |  |
| 3 | Create Maintenance Item | To create a maintenance item, choose Create button on the top of the screen. Enter following details in the popup window:Item Description: Mechanical Inspection for PumpPlan Category: YM (Maintenance Request)Notification Type: Proactive Work (Y2). Press Enter.Reference Object Type: EquipmentReference Object: <Entry of choice>Maintenance Strategy: EAM_<XX>Comment: You can use the maintenance strategy created in the previous step.Task List: <Entry of choice>Comment: You can use the task list created in the previous step.Choose Create.Maintenance Item screen is displayed. Enter following details under Basic Details tab:Priority: <Entry of your choice>Choose Create.Note Maintenance items can also be created through the Manage Maintenance Plans (F5325) app.Note If you wish to generate a maintenance order from a maintenance plan then select the item category as PM (Maintenance Order). You also need to the select order type as Proactive Maintenance (YA02) in the subsequent screen.If you want the order to go through the order approval process, select the Do not Release Immediately button which is available only if the item category is PM (Maintenance Order). | The maintenance item is created. |  |

#### Create Maintenance Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Maintenance plan will have maintenance or inspection activities to be carried out for technical objects.

The frequency or strategy and, scope of the activities are defined in the maintenance plan.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open the App | Open Manage Maintenance Plans (F5325). | The app opens. |  |
| 3 | Create Maintenance Plan | Make the following entries, choose Continue:Plan Description: Mechanical Inspection for PumpPlan Category: Maintenance RequestPlan Type: StrategySelect Time radio button.Strategy: Entry of your choiceChoose Create. | The Maintenance Plan screen is displayed. |  |
| 4 | Maintain Maintenance Plan Item Data | To create a maintenance item choose Create Item button by scrolling down to Maintenance item section. Enter following details in the pop-up window-Item Description: Mechanical Inspection for PumpNotification Type: Proactive Work (Y2) & press Enter.Reference Object Type: EquipmentReference Object: 23310XXXXTask List: Entry of your choiceYou can use the task list created in the previous step.Choose Create.Click on Maintenance Item line and enter following details under Basic Details tab:Priority: <Entry of your choice>Choose Apply. | The Maintenance Plan Planning Data screen is displayed. |  |
| 5 | Maintain Maintenance Plan Planning Data | In the Schedule section, make following entries:Scheduling Duration: 365Comment: You can use the scheduling period to determine the length of time for which the system creates maintenance calls during maintenance plan scheduling.Start Date for Scheduling: <Current date>Comment: The start date is needed for mass schedule maintenance plans.End Date for Scheduling: <Entry of Choice>In the Scheduling Parameters section, make following entries:Shift Factor for Early Completion: 100Shift Factor for Late Completion: 100Comment: The shift factor in the event of early/late completion of a maintenance task defines the percentage of the shift to be applied to the calculation of the next date.Tolerance for Early Completion: 10Tolerance for Late Completion: 10Comment: The tolerance, in the case of early/late completion, determines the time span in which variances between actual and planned dates do not influence subsequent scheduling. The tolerance is defined as a percentage rate of the smallest interval between the maintenance cycles of the maintenance strategy.Cycle Modification Factor: 1Call Horizon: 50Comment: The call horizon determines when a maintenance call object, for example, a maintenance order should be generated for a maintenance call wrt maintenance planned date.Completion Required: Select Yes or No using the toggle buttonComment: If you set this indicator, the system only generates the next call object once the preceding call object has been confirmed.Scheduling Indicator: TimeChoose Create. | The maintenance plan is created. |  |
| 6 | Assign Maintenance Item (Optional) | Alternatively, it is possible to assign existing maintenance item to a maintenance plan using the Assign Item button. To assign an item, follow these steps:Open the maintenance plan in Manage Maintenance Plans (F5325) app.Choose Assign Item.Select the required maintenance item and choose OK. | The maintenance item is assigned to the maintenance plan. |  |

#### Schedule Maintenance Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When you schedule your maintenance plan for the first time, you trigger the maintenance cycle. The system uses the scheduling information in the maintenance plan to calculate the maintenance package that is due next.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open the App | Open Schedule Maintenance Plan (IP10). | The app opens. |  |
| 3 | Search Maintenance Plan | Enter the following and choose Enter.MaintenancePlan: <Maintenance Plan number>Use the maintenance strategy created in the previous step. | The Schedule Maintenance Plan: Strategy Plan <Maintenance Plan number> page displays. |  |
| 4 | Schedule Maintenance Plan | Choose Start.On the Start Date screen, enter a start date. For example, enter current day's date.Start of cycle: <Current Date>Choose Continue. | Maintenance plan has been scheduled. |  |

Result

The maintenance plan has been scheduled.

Hint: In case you want to use mass scheduling instead of manually scheduling maintenance plans, you can use the tile Mass Schedule Maintenance Plans (F2774) with the business role Maintenance Planner.

To start mass scheduling, you must have entered a start date in the maintenance plan or have scheduled the maintenance plan once.

### Performance-Based Single Cycle Plan

#### Create General Task List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Using task lists, you can centrally define and manage maintenance tasks for your technical objects. General task lists can also help you prepare maintenance plans and orders.

A task list group combines one or more task lists according to their logical features. Within a task list group, each task list is identified by a group counter. This enables you, for example, to combine several task lists in one group. Within the group, the system allocates a sequential number (the group counter) to each individual task list.

Prerequisite

- Technical objects in the form of functional locations, equipment, and maintenance assemblies.
- Organizational units such as maintenance planners and work centers.
- Costs centers defined in the master data of the technical objects.
- Maintenance spare parts and assemblies in the Materials Management (MM) module.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Maintenance Planner . | The SAP Fiori launchpad is displayed. |  |
| 2 | Open the App | Open Create Task List (EAMS_WDA_TL_OIF_V2 (EAMS_WDA_TL_OIF_CFG_V2)). | The app opens. |  |
| 3 | Choose Your Task List Type | Choose Task List Type : General Maintenance Task List | The Create General Maintenance Task List screen appears. |  |
| 4 | Enter Creation Parameters | Enter the following:Task List Group:Comment: The task list group uses internal number range.Planning Plant: 3310Group Counter:Comment: The group counter would increase automatically if you create another task list for the same technical object.Overall Status: Released (general)Select the relevant profile for the plant.Key Date: <Today>● Choose Continue. | The Create General Maintenance Task List screen is displayed. |  |
| 5 | Maintain General Data | Enter the following:Description: DescriptionMake your own description. For example, Mechanical InspectionStatus: Released (General)Planner Group: YB1Work Center: RES-0100Work Center Plant: 3310Usage: 4System Condition: not in operationChoose Operation Data. | The Operation Data tab is displayed. |  |
| 6 | Maintain Operation Data | Enter the following entries and choose Enter.Operation: 0010Description: Check the pumpWork: 2Unit: HCapacities: 2Stage : PreOperation: 0020Description: Check the BearingsWork: 1Unit: HCapacities: 1Stage : MainOperation : 0030Description: Check the couplingWork: 2Unit: HCapacities: 2Stage : MainOperation: 0040Description: Check the shaftWork: 3Unit: HCapacities: 3Stage : PostChoose the operation 0010.In the lower part of the screen, Details: Operation 0010, Check the pump section, choose Materials.Enter the following and choose Enter.Material: SP005Quantity : 1Repeat the above step for other operationsOperation Item: 0020Material: SP001Quantity: 2Operation Item: 0030Material: SP002Quantity: 1Operation Item: 0040Material: SP003Quantity: 2 | The general task list is created. |  |

#### Create Maintenance Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A maintenance item describes which preventive maintenance tasks should take place regularly at a technical object or a group of technical objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Maintenance Planner. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Manage Maintenance Items app | Open Manage Maintenance Items (F5356). | The Manage Maintenance Items page appears. |  |
| 3 | Create Maintenance Item | To create a maintenance item, choose Create button on the top of the screen. Enter following details in the popup window:Item Description: Mechanical Inspection for PumpPlan Category: YM (Maintenance Request)Notification Type: Proactive Work (Y2). Press Enter.Reference Object Type: EquipmentReference Object: <Entry of choice>Task List: <Entry of choice>Comment: You can use the task list created in the previous step.Choose Create.Maintenance Item screen is displayed. Enter following details under Basic Details tab:Priority: <Entry of your choice>Choose Create.Note Maintenance items can also be created through the Manage Maintenance Plans (F5325) app.Note If you wish to generate a maintenance order from a maintenance plan then select the item category as PM (Maintenance Order). You also need to the select order type as Proactive Maintenance (YA02) in the subsequent screen.If you want the order to go through the order approval process, select the Do not Release Immediately button which is available only if the item category is PM (Maintenance Order). | The maintenance item is created. |  |

#### Create Maintenance Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Maintenance plan will have maintenance or inspection activities to be carried out for technical objects.

The frequency or strategy and, scope of the activities are defined in the maintenance plan.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open the App | Open Manage Maintenance Plans (F5325). | The app opens. |  |
| 3 | Create Maintenance Plan | Make the following entries, choose Continue:Plan Description: Mechanical Inspection for PumpPlan Category: Maintenance RequestPlan Type: Single Cycle (Performance Based)Choose Create. | The Maintenance Plan screen is displayed. |  |
| 4 | Maintain Maintenance Plan Item Data | To create a maintenance item choose Create Item button by scrolling down to Maintenance item section. Enter following details in the pop-up window-Item Description: Mechanical Inspection for PumpNotification Type: Proactive Work (Y2) and press Enter.Reference Object Type: EquipmentReference Object: 23310XXXXTask List: Entry of your choiceYou can use the task list created in the previous step.Choose Create.Click on Maintenance Item line and enter following details under Basic Details tab:Priority: <Entry of your choice>Choose Apply. | The Maintenance Plan Planning Data screen is displayed. |  |
| 5 | Maintain Maintenance Plan Planning Data | In the Cycle section, make the following entries:Cycle Length: 100Cycle UoM: HComment: Cycle Length/Cycle UoM defines the duration in which the maintenance is to be executed.Cycle Text: Every 100 HoursCounter: < Measuring Point No >Comment: Enter the measuring point number created for the technical object type. Based on readings entered according to the mentioned measuring point, maintenance call will be trigerred once the plan is scheduled.In the Schedule section, enter the following:Scheduling Duration: 365Comment: You can use the scheduling period to determine the length of time for which the system creates maintenance calls during maintenance plan scheduling.End Date for Scheduling: <Entry of Choice>In the Scheduling Parameters section, enter the following:Shift Factor for Early Completion: 100Shift Factor for Late Completion: 100Comment: The shift factor in the event of early/late completion of a maintenance task defines the percentage of the shift to be applied to the calculation of the next date.Tolerance for Early Completion: 10Tolerance for Late Completion: 10Comment: The tolerance, in the case of early/late completion, determines the time span in which variances between actual and planned dates do not influence subsequent scheduling. The tolerance is defined as a percentage rate of the smallest interval between the maintenance cycles of the maintenance strategy.Cycle Modification Factor: 1Call Horizon: 50Comment: The call horizon determines when a maintenance call object, for example, a maintenance order should be generated for a maintenance call for the maintenance planned date.Completion Required: Select Yes or No using the toggle buttonComment: If you set this indicator, the system only generates the next call object once the preceding call object has been confirmed.Choose Create. | The maintenance plan is created. |  |
| 6 | Assign Maintenance Item (Optional) | Alternatively, it is possible to assign existing maintenance item to a maintenance plan using the Assign Item button. To assign an item, follow these steps:Open the maintenance plan in Manage Maintenance Plans (F5325) app.Choose Assign Item.Select the required maintenance item and choose OK. | The maintenance item is assigned to the maintenance plan. |  |

#### Create Measurement Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Maintenance Planner needs to record initial reading of the technical objects (equipment / functional location) in the SAP system. Atleast one measurement document is required for scheduling the plan. Once the scheduling is done, regular readings must also be recorded in the system by the Maintenance Technician. This process can also be automated my making use of systems which get the reading from technical objects and load to SAP system through interfaces.

Time-to-time recording of these readings are relevant for accurate determination of maintenance due dates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Maintenance Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Open the App | Open Create Measurement Document for Technical Object (EAMS_WDA_MD_OIF).On the Create Measurement Documents screen, make the follow-ing entries:● Basis for measurement reading:Measuring PointMeasuring Point: <Measuring Point No>Comment: Enter the measuring point number created against the technical object.● Choose Continue. | The app opens. |  |
| 3 | Enter Counter | A new screen appears with the measuring point that was entered.● Enter Reading: <Counter reading>● Choose Save. | The measurement document is created. |  |

#### Schedule Maintenance Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When you schedule your maintenance plan for the first time, you trigger the maintenance cycle. The system uses the scheduling information in the maintenance plan to calculate the due date of the maintenance call object.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Open the App | Open Schedule Maintenance Plan (IP10). | The app opens. |  |
| 3 | Search Maintenance Plan | Enter the following and choose Enter.MaintenancePlan: <Maintenance Plan num-ber>Please use the single cycle plan (perfomance based) created in the previous step. | The Schedule Maintenance Plan: Single Cycle Plan <Maintenance Plan number> screen displays. |  |
| 4 | Schedule Maintenance Plan | Choose Start.On the Start Date screen, enter a start date. For example, enter current date.Start of cycle:<Counter reading >Comment: If a start counter reading was entered during the maintenance plan creation, the system will propose that reading as the start counter reading. It can be changed to a different reading as well, if required.Choose Continue. | Maintenance plan has been scheduled |  |

Result

The maintenance plan has been scheduled.

Hint: In case you want to use mass scheduling instead of manually scheduling maintenance plans, you can use the tile Mass Schedule Maintenance Plans (F2774) with the business role Maintenance Planner.

To start mass scheduling, you must have entered a start date in the maintenance plan or have scheduled the maintenance plan once.

### Performance-Based Strategy Plan

#### Maintain Maintenance Strategies

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A maintenance strategy represents a rule for the sequence of planned maintenance and inspection tasks. A maintenance strategy for performance plan contains the maintenance packages that define the cycle in which the tasks must be performed. For example, every 5000 km, every 500 operating hours, and so on. It contains addi-tional scheduling parameters such as shift factor, preliminary and followup buffers, and hierarchy. Maintenance strategies are required in strategy plans.

For each plant, you may use the same maintenance strategy. You can skip this step if the maintenance strategy exists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open the App | Open Maintain Maintenance Strategies (IP11). | The app opens. |  |
| 3 | Create Maintenance Strategy | Choose New Entries. Make the following entries.Name: EAM_<XX>Description: <Description> for example: Mechanical InspectionScheduling Indicator: ActivityStrategy unit: HChoose Save. | The new maintenance strategy is created. |  |
| 4 | Add Maintenance Packages | On the left side of the screen, in Dialog Structure, double-click on the Packages folder.Choose New Entries.Enter the following:Package No.: 1Cycl. Length: 100Unit: HMaintenance cycle text: 100 OPHCycle short text: 1HHierarchy: 1Hierarchy short text: 1HRepeat the above step for further cycles. Create the following packages.Package No.: 2Cycl. Length: 250Unit: HMaintenance cycle text: 250 OPHCycle short text: 2HHierarchy: 1Hierarchy short text: 1HPackage No.: 3Cycl. Length: 500Unit: HMaintenance cycle text: 500 OPHCycle short text: 3HHierarchy: 1Hierarchy short text: 1HPackage No.: 4Cycl. Length: 1000 OPHUnit: HMaintenance cycle text: 1000 OPHCycle short text: 4HHierarchy: 1Hierarchy short text: 1HChoose Save. | The Change Maintenance Packages page is displayed.The maintenance packages are maintained in maintenance strategy. |  |

#### Create General Task List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Using task lists, you can centrally define and manage maintenance tasks for your technical objects. General task lists can also help you to prepare maintenance plans and orders.

A task list group combines one or more task lists according to their logical features. Within a task list group, each task list is identified by a group counter. This enables you, for example, to combine several task lists in one group. Within the group, the system allocates a sequential number (the group counter) to each individual task list.

Prerequisite

- Technical objects in the form of functional locations, equipment, and maintenance assemblies.
- Organizational units such as maintenance planners and work centers.
- Costs centers defined in the master data of the technical objects.
- Maintenance spare parts and assemblies in the Materials Management (MM) module.
- Maintenance strategy.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open the App | Open Create Task List (EAMS_WDA_TL_OIF_V2 (EAMS_WDA_TL_OIF_CFG_V2)). | The app opens. |  |
| 3 | Choose Task List Type | Choose Task List Type: General Maintenance Task List. | The Create General Maintenance Task List screen is displayed. |  |
| 4 | Enter Creation Parameters | Enter the following:Task List Group:Comment: Task List Group uses internal number range.Planning Plant: 3310Group Counter:Comment: The group counter would increase automatically if you create another task list for the same technical object.Overall Status: Released (general)Select the relevant profile for the plant.Key Date:<Today>Choose Continue. | The Create General Maintenance Task List screen is displayed. |  |
| 5 | Maintain General Data | Enter the followin:Description:<Description>Make your own description. For example: Mechanical InspectionStatus: Released (General)Planner Group: YB1Work Center: RES-0100Work Center Plant: 3310Usage: 4Maintenance Strategy: EAM_<XX>Comment: You can use the maintenance strategy created in the previous step.System Condition: not in operationChoose Operation Data. | The Operation Data tab appears. |  |
| 6 | Maintain Operation Data | Enter the following and choose Enter.Operation: 0010Description: Check the pumpWork: 2Unit: HCapacities: 2Stage : PreOperation: 0020Description: Check the BearingsWork: 1Unit: HCapacities: 1Stage : MainOperation : 0030Description: Check the couplingWork: 2Unit: HCapacities: 2Stage : MainOperation: 0040Description: Check the shaftWork: 3Unit: HCapacities: 3Stage : PostChoose the operation 0010.In the lower part of the screen, Details: Operation 0010, Check the pump section, choose Materials.Enter the following and choose Enter.Material: SP005Quantity : 1Repeat the above step for other operationsOperation Item: 0020Material: SP001Quantity: 2Operation Item: 0030Material: SP002Quantity: 1Operation Item: 0040Material: SP003Quantity: 2Choose Maintenance Packages. | The Maintenance Packages tab appears. |  |
| 7 | Maintain Maintenance Packages | Enter the following entries and choose Save.For Operation 0010, set flag for 100,250,500,1000 OPHFor Operation 0020, set flag for 100,250 OPHFor Operation 0030, set flag for 500,1000 OPHFor Operation 0040, set flag for 100,250,500,1000 OPH | The general task list is created. |  |

#### Create Maintenance Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A maintenance item describes which preventive maintenance tasks should take place regularly at a technical object or a group of technical objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Maintenance Planner. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Manage Maintenance Items app | Open Manage Maintenance Items (F5356). | The Manage Maintenance Items page appears. |  |
| 3 | Create Maintenance Item | To create a maintenance item, choose Create button on the top of the screen. Enter following details in the popup window:Item Description: Mechanical Inspection for PumpPlan Category: YM (Maintenance Request)Notification Type: Proactive Work (Y2). Press Enter.Reference Object Type: EquipmentReference Object: <Entry of choice>Maintenance Strategy: EAM_<XX>Comment: You can use the maintenance strategy created in the previous step.Task List: <Entry of choice>Comment: You can use the task list created in the previous step.Choose Create.Maintenance Item screen is displayed. Enter following details under Basic Details tab:Priority: <Entry of your choice>Choose Create.Note Maintenance items can also be created through the Manage Maintenance Plans (F5325) app.Note If you wish to generate a maintenance order from a maintenance plan then select the item category as PM (Maintenance Order). You also need to the select order type as Proactive Maintenance (YA02) in the subsequent screen.If you want the order to go through the order approval process, select the Do not Release Immediately button which is available only if the item category is PM (Maintenance Order). | The maintenance item is created. |  |

#### Create Maintenance Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Maintenance plan will have maintenance or inspection activities to be carried out for technical objects.

The frequency or strategy and, scope of the activities are defined in the maintenance plan.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open the App | Open Manage Maintenance Plans (F5325). | The app opens. |  |
| 3 | Create Maintenance Plan | Make the following entries, choose Continue:Plan Description: Mechanical Inspection for PumpPlan Category: Maintenance RequestPlan Type: StrategySelect Counter radio button.Strategy: Entry of your choice.Choose Create. | The Maintenance Plan screen is displayed. |  |
| 4 | Maintain Maintenance Plan Item Data | To create a maintenance item choose Create Item button by scrolling down to Maintenance item section. Enter following details in the pop-up window-Item Description: Mechanical Inspection for PumpNotification Type: Proactive Work (Y2) & press Enter.Reference Object Type: EquipmentReference Object: 23310XXXXMaintenance Strategy: EAM_<XX>Comment: You can use the maintenance strategy created in the previous step.Task List: Entry of your choiceYou can use the task list created in the previous step.Choose Create.Click on Maintenance Item line and enter following details under Basic Details tab:Priority: <Entry of your choice>Choose Apply. | The Maintenance Plan Planning Data screen is displayed. |  |
| 5 | Maintain Maintenance Plan Planning Data | In the Cycle section, enter the following:Counter: <Measuring Point No>Comment: Enter the measuring point number created for the technical object type. Based on readings entered according to the mentioned measuring point, the maintenance call will be trigerred once the plan is scheduled.In the Schedule section, enter the following:Scheduling Duration: 365Comment: You can use the scheduling period to determine the length of time for which the system creates maintenance calls during maintenance plan scheduling.Start Counter Reading for Scheduling: <Entry of Choice>End Counter Reading for Scheduling: <Entry of Choice>In the Scheduling Parameters section, enter the following:Shift Factor for Early Completion: 100Shift Factor for Late Completion: 100Comment: The shift factor in the event of early/late completion of a maintenance task defines the percentage of the shift to be applied to the calculation of the next date.Tolerance for Early Completion: 10Tolerance for Late Completion: 10Comment: The tolerance, in the case of early/late completion, determines the time span in which variances between actual and planned dates do not influence subsequent scheduling. The tolerance is defined as a percentage rate of the smallest interval between the maintenance cycles of the maintenance strategy.Cycle Modification Factor: 1Call Horizon: 50Comment: The call horizon determines when a maintenance call object, for example, a maintenance order should be generated for a maintenance call wrt maintenance planned date.Completion Required: Select Yes or No using the toggle buttonComment: If you set this indicator, the system only generates the next call object once the preceding call object has been confirmed.Choose Create. | The maintenance plan is created. |  |
| 6 | Assign Maintenance Item (Optional) | Alternatively, it is possible to assign existing maintenance item to a maintenance plan using the Assign Item button. To assign an item, follow these steps:Open the maintenance plan in Manage Maintenance Plans (F5325) app.Choose Assign Item.Select the required maintenance item and choose OK. | The maintenance item is assigned to the maintenance plan. |  |

#### Create Measurement Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Maintenance Planner needs to record initial reading of the technical objects (equipment / functional location) in the SAP system. Atleast one measurement document is required for scheduling the plan. Once scheduling is done, regular readings must also be recorded in the system by the Maintenance Tehnician. This process also can be automated my making use of the systems which gets the reading from technical objects and loads to SAP system through interfaces.

Time-to-time recording of these readings are relevant for accurate determination of maintenance due dates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Maintenance Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Open the App | Open Create Measurement Document for Technical Object (EAMS_WDA_MD_OIF)On the Create Measurement Documents screen, make the following entries:Basis for measurement reading: Measuring PointMeasuring Point: < Measuring Point No>Comment: Enter the measuring point number that was created against the technical object.Choose Continue. | The app opens. |  |
| 3 | Enter Counter Reading | A new screen appears with the measuring points you entered:Reading: <Counter reading >Choose Save | Measurement document is created. |  |

#### Schedule Maintenance Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When you schedule your maintenance plan for the first time, you trigger the maintenance cycle. The system uses the scheduling information in the maintenance plan to calculate the maintenance package that is due next.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open the App | Open Schedule Maintenance Plan (IP10). | The app opens. |  |
| 3 | Search Maintenance Plan | Enter the following and choose Enter.Maintenance Plan: <Maintenance Plan number>You can use the maintenance strategy created in the previous step. | The Schedule Maintenance Plan: Strategy Plan <Maintenance Plan number> screen is displayed. |  |
| 4 | Schedule Maintenance Plan | Follow these steps:Choose Start.Start of cycle: <Current counter reading>Choose Continue.You receive an overview of scheduled calls with plan date and call date of a schedule call based on the start date you entered and on the scheduling parameters maintained in the maintenance plan.Comment: The scheduling list shows scheduled calls with assigned call dates. Each call has its own system status with the scheduling type.The first call has the Type New Start with Status Hold. When you want to create a planned order for the first time before reaching the call date you can use the function Release Call.Flag the first row in Scheduling List.Choose Release Call.Choose Save and confirm all the messages that appear.To automatically check the created Proactive maintenance order, follow these steps:Open Schedule Maintenance Plan againEnter the maintenance plan number.Choose EnterIn the Scheduling List, choose the first line you have called.Choose Display Call Object.Note the maintenance order number. | Maintenance plan has been scheduled. |  |

Result

The maintenance plan has been scheduled.

Hint: In case you want to use mass scheduling instead of manually scheduling maintenance plans, you can use the tile Mass Schedule Maintenance Plans (F2774) with the business role Maintenance Planner.

To start mass scheduling, you must have entered a start date in the maintenance plan or have scheduled the maintenance plan once.

### Multiple Counter Plan

#### Create General Task List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Using task lists, you can centrally define and manage maintenance tasks for your technical objects. General task lists can also help you to prepare maintenance plans and orders.

A task list group combines one or more task lists according to their logical features. Within a task list group, each task list is identified by a group counter. This enables you, for example, to combine several task lists in one group. Within the group, the system allocates a sequential number (the group counter) to each individual task list.

Prerequisite

- Technical objects in the form of functional locations, equipment, and maintenance assemblies.
- Organizational units such as maintenance planners and work centers.
- Costs centers defined in the master data of the technical objects.
- Maintenance spare parts and assemblies in the MM (Materials Management) module.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open the App | Open Create Task List (EAMS_WDA_TL_OIF_V2 (EAMS_WDA_TL_OIF_CFG_V2)). | The app opens. |  |
| 3 | Choose Task List Type | Choose Task List Type: General Maintenance Task List. | The Create General Maintenance Task List screen displays. |  |
| 4 | Enter Creation Parameters | Enter the following:Task List Group:Comment: The task list group uses internal number range.Planning Plant: 3310Group Counter:Comment: The group counter would increase automatically if you create another task list for the same technical object.Overall Status: Released (general)Select the relevant profile for the plant.Key Date: <Today>Choose Continue. | The Create General Maintenance Task List screen displays. |  |
| 5 | Maintain General Data | Enter the following:Description:<Description>Make your own description. For example: Mechanical InspectionStatus: Released (General)Planner Group: YB1Work Center: RES-0100Work Center Plant: 3310Usage: 4System Condition: not in operationChoose Operation Data. | The Operation Data tab appears. |  |
| 6 | Maintain Operation Data | Enter the following and choose Enter.Operation: 0010Description: Check the pumpWork: 2Unit: HCapacities: 2Stage : PreOperation: 0020Description: Check the BearingsWork: 1Unit: HCapacities: 1Stage : MainOperation : 0030Description: Check the couplingWork: 2Unit: HCapacities: 2Stage : MainOperation: 0040Description: Check the shaftWork: 3Unit: HCapacities: 3Stage : PostChoose the operation 0010.In the lower part of the screen, Details: Operation 0010, Check the pump section, choose Materials.Enter the following and choose Enter.Material: SP005Quantity : 1Repeat the above step for other operationsOperation Item: 0020Material: SP001Quantity: 2Operation Item: 0030Material: SP002Quantity: 1Operation Item: 0040Material: SP003Quantity: 2 | The general task list is created. |  |

#### Create Maintenance Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A maintenance item describes which preventive maintenance tasks should take place regularly at a technical object or a group of technical objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Maintenance Planner. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Manage Maintenance Items app | Open Manage Maintenance Items (F5356). | The Manage Maintenance Items page appears. |  |
| 3 | Create Maintenance Item | To create a maintenance item, choose Create button on the top of the screen. Enter following details in the popup window:Item Description: Mechanical Inspection for PumpPlan Category: YM (Maintenance Request)Notification Type: Proactive Work (Y2).Reference Object Type: EquipmentReference Object: <Entry of choice>Task List: <Entry of choice>Comment: You can use the task list created in the previous step.Choose Create.Maintenance Item screen is displayed. Enter following details under Basic Details tab:Priority: <Entry of your choice>Choose Create.Note Maintenance items can also be created through the Manage Maintenance Plans (F5325) app.Note If you wish to generate a maintenance order from a maintenance plan then select the item category as PM (Maintenance Order). You also need to the select order type as Proactive Maintenance (YA02) in the subsequent screen.If you want the order to go through the order approval process, select the Do not Release Immediately button which is available only if the item category is PM (Maintenance Order). | The maintenance item is created. |  |

#### Create Maintenance Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Maintenance plan will have maintenance or inspection activities to be carried out for technical objects.

The frequency or strategy and, scope of the activities are defined in the maintenance plan.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open the App | Open Manage Maintenance Plans (F5325). | The app opens. |  |
| 3 | Create Maintenance Plan | To create a maintenance plan choose the Create button on the top of the screen. Enter the following details in the popup window:Plan Description: Mechanical Inspection for PumpPlan Category: Maintenance RequestPlan Type: Multiple CounterChoose Create. | The Maintenance Plan screen is displayed. |  |
| 4 | Maintain Maintenance Plan Item Data | To create a maintenance item choose Create Item button by scrolling down to Maintenance item section. Enter following details in the pop-up window-Item Description: Mechanical Inspection for PumpNotification Type: Proactive Work (Y2).Reference Object Type: EquipmentReference Object: 23310XXXXTask List: Entry of your choiceYou can use the task list created in the previous step.Choose Create.Click on Maintenance Item line and enter following details under Basic Details tab:Priority: <Entry of your choice>Choose Apply. | The Maintenance Plan Planning Data screen is displayed. |  |
| 5 | Maintain Maintenance Plan Planning Data | In the Cycle section, enter the following:Operator : Choose OR type using the toggle switch.If you select the OR operation, it means that a notification will be created for the earliest planned date. It is the case that occurs first.If you select the AND operation, it means that a notification will be created for the last planned date. It is the case that occurs last.Choose Create and enter the following:Cycle Length: 100 HComment: The cycle length defines the duration in which the maintenance is to be executed.Cycle Text: Every 100 HoursCounter: <Counter No>Comment: Enter the counter number created for the technical object type. Readings entered according to the mentioned counter number will be used to trigger the maintenance call object.Again choose Create and enter the following:Cycle Length: 6 MONComment: The cycle length defines the duration in which the maintenance is to be executed.Cycle Text: Every 6 MonthsIn the Schedule section, enter the following:Scheduling Duration: 365Comment: You can use the scheduling period to determine the length of time for which the system creates maintenance calls during maintenance plan scheduling.Start Date for Scheduling: <Current date>Comment: The start date is needed for mass schedule maintenance plans.End Date for Scheduling: <Entry of Choice>In the Scheduling Parameters section, make following entries:Shift Factor for Early Completion: 100Shift Factor for Late Completion: 100Comment: The shift factor in the event of early/late completion of a maintenance task defines the percentage of the shift to be applied to the calculation of the next date.Tolerance for Early Completion: 10Tolerance for Late Completion: 10Comment: The tolerance, in the case of early/late completion, determines the time span in which variances between actual and planned dates do not influence subsequent scheduling. The tolerance is defined as a percentage rate of the smallest interval between the maintenance cycles of the maintenance strategy.Cycle Modification Factor: 1Completion Required: Select Yes or No using the toggle buttonComment: If you set this indicator, the system only generates the next call object once the preceding call object has been confirmed.Choose Create. | The maintenance plan is created. |  |
| 6 | Assign Maintenance Item (Optional) | Alternatively, it is possible to assign existing maintenance item to a maintenance plan using the Assign Item button. To assign an item, follow these steps:Open the maintenance plan in Manage Maintenance Plans (F5325) app.Choose Assign Item.Select the required maintenance item and choose OK. | The maintenance item is assigned to the maintenance plan. |  |

#### Create Measurement Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Maintenance Planner needs to record initial reading of the technical objects (equipment / functional location) in the SAP system. Atleast one measurement document is required for scheduling the plan.

Once the scheduling is done, regular readings must also be recorded in the system by the Maintenance Technician.

This process can also be automated my making use of systems which get the reading from technical objects and loads to SAP system through interfaces.

Time-to-time recording of these readings are relevant for accurate determination of maintenance due dates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Technician. | The SAP Fiori launchpad is displayed. |  |
| 2 | Create Measurement Document | Open Create Measurement Document for Technical Object (EAMS_WDA_MD_OIF).On the Create Measurement Documents screen, make the following entries:Basis for measurement reading: Measuring PointMeasuring Point: <Measuring Point No>Comment: Enter the measuring point number created against the technical object.Choose Continue. | The Create Measurement Documents screen is displayed. |  |
| 3 | Enter Counter Reading | A new screen appears with measuring point you entered.Reading: <Counter Reading>Choose Save. | The measurement document is created. |  |

Result

Measurement documents are created and these will help to schedule maintenance plan.

#### Schedule Maintenance Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When you schedule your maintenance plan for the first time, you trigger the maintenance cycle. The system uses the scheduling information in the maintenance plan to calculate the maintenance package that is due next.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open the App | Open Schedule Maintenance Plan (IP10). | The app opens. |  |
| 3 | Search Maintenance Plan | Enter the following and choose Enter:Maintenance Plan: <Maintenance Plan number>You can use the multiple counter plan created in the previous step. | The Schedule Maintenance Plan: Single Cycle Plan <Maintenance Plan Number screen is displayed. |  |
| 4 | Schedule Maintenance Plan | Choose Start.Choose Continue button on the information screens which appear.Choose Save buttonYou receive an overview of scheduled calls with plan date and call date of the scheduled call. This is based on your start of cycle counter reading, annual estimate (entered against respective measuring point), and the scheduling parameters maintained in the maintenance plan.Comment: The Scheduling List shows scheduled calls with assigned call dates. Each call has its own system status with scheduling type. The first call has the type New Start with status Hold.When you want to create a planned order for the first time before reaching the call date, you can use the function Release Call.Flag the first row in Scheduling List.Choose Release Call.Choose Save and confirm all the messages if appear.To check the automatically created Proactive maintenance order, follow these steps:Open Schedule Maintenance Plan again.Enter the maintenance plan number.Choose Enter.In the Scheduling List, choose the first line you have called.Choose Display Call Object.Note the maintenance order number. | Maintenance plan has been scheduled |  |

Result

The maintenance plan has been scheduled.

Hint: In case you want to use mass scheduling instead of manually scheduling maintenance plans, you can use the tile Mass Schedule Maintenance Plans (F2774) with the business role Maintenance Planner.

To start mass scheduling, you must have entered a start date in the maintenance plan or have scheduled the maintenance plan once.

### Screen Maintenance notifications

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

Table 9:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Test Step # | Test Step Name | Instruction |  | Pass/Fail/Comments |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Supervisor. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Maintenance Notifications - New Version (F5777) | The app opens. |  |
| 3 | Get List of Maintenance Notifications | By default, the app displays a list of maintenance notifications that are open.Enter the following:Notification Type: Proactive WorkChoose GoYou can switch between the list of maintenance notifications by using subphase filter in the app. | List of maintenance notifications is displayed based on the filter criteria. |  |
| 4 | Change Responsibility (Optional) | Select one or more open maintenance Notifications by selecting the checkbox. Choose Change Responsibility button.On the Change Responsibility screen, the main work center, planner group, planning plant, and person responsible can be changed. | Responsibility details for the maintenance requests are changed. |  |
| 5 | Review and Modify the Maintenance Notification | Choose a maintenance notification which needs to be reviewed. Maintenance Notification is opened and details can be seen.Choose Edit to update the information related to malfunction, responsibility, and other details. Further while reviewing the notification, the supervisor can also reassess the risk and redetermine the priority of the maintenance notification and if required, can manually change the final due date. | Maintenance notification is reviewed and updated. |  |
| 6 | Accept Maintenance Request | From the top right side, you can choose Accept, Reject, or Action Required.Accept the maintenance notification if all the details are correct in the notification.Note If you choose Action Required, the maintenance notification is sent back and will be available in Action Required tab of Manage Maintenance Notifications App where the initiator can provide required information and resend it for screening. If you reject a maintenance Notification, the Notification will not be processed further and can be seen in the Rejected tab of Manage Maintenance Notifications App. The reason code needs to be selected if maintenance notification is rejected or sent back seeking additional information. | The maintenance notification is accepted. |  |

### Create and Plan Maintenance Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the maintenance request is accepted, we are in the Planning phase of the maintenance process. The accepted maintenance request is called as maintenance notification. This process step shows how to convert a maintenance notification into a maintenance order and provides details to plan the resources for the order.

Order processing helps you to plan maintenance tasks in greater detail. You decide the tasks to be performed and what components (materials) are needed, and so on.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 10:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Manage Maintenance Notifications and Orders (F4604) app. | The app opens. |  |
| 3 | Get list of Maintenance Notifications | Enter the following:Execution Object Type: Maintenance NotificationNotification Type: Proactive Work (Y2)Choose Go | Based on the filter criteria, a list of accepted notifications is displayed. |  |
| 4 | Create or Assign Maintenance Order | To create or assign an order, follow these steps:Select one or more maintenance notifications for which maintenance order needs to be created.Choose Create Order button on the top of the screen.Select the Maintenance Order Type: Proactive Maintenance (YA02)Choose Create.Alternatively, it is possible to assign existing maintenance order to a maintenance notification using the Assign Order button. | The maintenance order is created and is assigned to the maintenance notification.The order number is shown in Associated with under Execution Object Type section of the list view. |  |
| 5 | Add Non Stock Material | Choose line of operation (example 0010) and choose Materials tab at the bottom of the screen. Enter the following:Variant: StandardMaterial: NL001Item Category: Non-stock Item NQuantity: <1>Plant: 3310Purchasing Org: 3310Price: Entry of your choiceSupplier: 33300001G/L Account: 61002000Note To duplicate a material line in the list with all item data, choose Copy Material. You can then change specific fields in the copied line. |  |  |
| 6 | Add Services | Select the checkbox for operation (example, 0010) and choose Services tab at the bottom of the screen.For a service without service material, enter the following:Description: <Description of service>Quantity: <1>Unit:<H>Plant: 3310Price: Entry of your choicePurchasing Org: 3310Purchasing Group: 001Supplier: 33300001G/L Account: 65008000Material Group: YBMM01Note You can choose Settings button to add or remove fields in the screen.For service with service material, enter the following:Product: SM0001Quantity: <1>Supplier: 33300001Press Enter. The system will fill up other fields from Service Product Master. |  |  |
| 7 | Add Enhanced Limit ServicesNote Enhanced limit services are not available for Brazil. | Select the checkbox for operation (example, 0010) and choose Services tab at the bottom of the screen.For a service without service material, enter the following:Description: <Description of service>Item Categoy: E- Enhanced limitExpected Value: <Entry of your choice>Overall Limit: <Entry of your choice>Note The expected value must not be larger than the overall limit.Plant: 3310Purchasing Org: 3310Purchasing Group: 001Supplier: 33300001G/L Account: 65008000Material Group: YBMM01You can choose Settings button to add or remove fields in the screen.Note You can select a service material for a service, if required. | The quantity is set to 1. The unit is set to AU (Activity Unit) or to the unit of the material master record. The price becomes read-only.The value from the Expected Value field should be copied to the Price field. |  |
| 8 | Cost Review | Go to the Costs tab.On the top of the screen, select Additional Functions > Determine CostsThe planned cost is displayed as per the cost category.The estimated costs can be updated against each cost category. | Planned / estimated costs reviewed / updated |  |
| 9 | Check Entries | Choose Check Entries in the upper left corner of the screen. | Entries have been checked. |  |
| 10 | Save Order | Choose Save | The maintenance order is saved and is in Planning phase.The selected stock material is reserved automatically.Note To verify this, log on to the SAP Fiori launchpad as a Warehouse Clerk.Open Display Stock Overview (MMBE)Enter the stock material, plant, and storage location and choose Execute.Select storage location line under Stock Overview and choose Reservations (Menu -> Environment -> Reservations) |  |

### Submit Maintenance Order for Approval

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

Table 11:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Manage Maintenance Notifications and Orders (F4604) app. | The app opens. |  |
| 3 | Get list of Maintenance Orders | Enter the following:Execution Object Type: Maintenance OrderOrder Type: Proactive MaintenanceChoose Go | A list of maintenance orders is displayed based on the filter criteria. |  |
| 4 | Submit Order for Approval | Select one or more maintenance orders which are ready for approval.On the top right side of the screen, choose Submit for Approval button. | The maintenance order is submitted for approval.The order goes for approval as per the workflow that you have maintained.Note If custom workflows have not been maintained, the order gets approved automatically.Maintenance order is in Approval phase. |  |

### Approve Maintenance Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to approve maintenance orders from My Inbox - All Items (F0862) app.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 12:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Supervisor. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | A list of orders that are ready for approval is displayed. |  |
| 3 | Approve or Reject Maintenance Order | On the My Inbox screen, select the workflow request for maintenance order. You can review information page which gives details of maintenance order like general data, responsibilities, account assignment, cost, dates and so on.Update comment in Comments section.Approve the maintenance order and add decision note if required.Note If a maintenance order is rejected, it can be processed further and sent for approval again. | The maintenance order is approved and the order will be removed from the list in My Inbox. |  |

### Review and Release Maintenance Order

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

Table 13:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Maintenance Notifications and Orders (F4604) app. | The app opens. |  |
| 3 | Review Maintenance Order | Enter the following:Execution Object: Maintenance Order Number which was approved in the previous stepChoose Go. | Maintenance order is displayed in the list view and is reviewed. |  |
| 4 | Release Maintenance Order | Select the order by selecting the checkbox. Choose Change Order Status and select Release.Plan costs at the time of releasing the order will be taken as baseline cost and will be displayed in detailed cost analysis section of cost tab. Even if there is a change in plan cost later the ,baseline cost will remain the same and this will help to understand the deviation from plan costs. | Maintenance order is released for preparation. |  |
| 5 | Review Purchase Requisitions | When the maintenance order is released, purchase requisition is created for the non-stock material and services.Select the maintenance order. On the Maintenance Order screen that appears, go to the Operations tab.Select the row for operation (example, 0010).On the Maintenance Order Operation screen, go to the Material tab.Note the purchase requisition number for the non-stock material and services from the Purchase Requisition column. | The purchase requisitions are reviewed. |  |

### Convert Purchase Requisitions into Purchase Orders

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

Table 14:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Process Purchase Requisitions (F1048A) app. | The Process Purchase Requisitions (V2) screen is displayed |  |
| 3 | Search for Purchase Requisition | Enter the following:Plant: 3310Purchasing Group: 001Purchasing Organization: 3310Choose Go | A list of purchase requisitions is displayed. |  |
| 4 | Create the Purchase Orders | Follow these steps:Select the purchase requisition.Choose Create Purchase Order.On New Purchase Order screen that opens, choose Purchase Order Type as the standard purchase order (NB).Choose Order.The created purchase order is displayed in the Display Purchase Order - Advanced (ME23N) app | The purchase order is created. |  |

### Goods Receipt for Purchase Order

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

Table 15:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) app. | The Post Goods Movement screen is displayed. |  |
| 3 | Enter Goods Receipt Order | Enter the following:Trans/Event: Goods ReceiptReference Document: Purchase OrderOrder: <Enter the Purchase order number from the previous step>GR goods receipt: 101Choose Execute.Following details are available:Document Date: default datePosting Date: DefaultFollow these steps:Go to Quantity tab and enter the quantity. For example :1Select the checkbox for Item OKChoose Post. | The material document is posted. |  |

### Post Goods Issue

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

Table 16:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad asWarehouse Clerk . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) app. | The Post Goods Movement screen is displayed. |  |
| 3 | Enter Goods Issue Order | Post Goods Issue | Enter the following:Trans/Event: Goods IssueReference Document: OrderOrder: <Enter the maintenance order number>GI for order: 261Choose Execute.Following details are available:Document Date: default datePosting Date: DefaultFollow these steps:Go to Quantity tab and enter the quantity. For example, 1Select the checkbox for Item OKChoose Post. |  |

### Maintenance Backlog Overview

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

Table 17:

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
| 6.3 | Manage Maintenance Backlog Card (By Phase) – Schedule Order (Optional) | To change the scheduling of the maintenance orders, follow these steps:Go to the Orders tab.Go to the Orders In Preparation tab.Select an order by selecting the checkbox.Choose Change Scheduling and select any one of the options:You can assign the order to the next or the previous bucketYou can change the basic start date or the end dateYou can assign or unassign the order to a maintenance event.To submit the order for scheduling, choose Submit for Scheduling.Note Order can also be submitted for scheduling through Find Maintenance Orders - Completion (F2175) app and is detailed out in the process step [Submit Order for Scheduling](#unique_55) [page ] 83. | The result may be one of the following depending on the selected option:The basic start date or the end date is changedThe order is moved to the next or the previous bucketThe order is assigned or unassigned to the maintenance event.The maintenance order moves into the scheduling phase. |  |
| 7 | Manage External Procurement Card | Click on the bar chart to review the purchase requisition or the purchase order for the corresponding milestone. | The purchase requisition or the purchase order is displayed. |  |
| 8 | Monitoring Procurement Activities | As a maintenance planner, you can monitor the availability status of non-stock components and services (external operations and lean services) in the Manage Maintenance Backlog (F4073) app.For this purpose, the system tracks several milestones in the procurement process. They mark the completion of the following important procurement activities:Procurement ActivityProcurement MilestoneCreate Purchase RequisitionPurchase Requisition CreatedRelease Purchase RequisitionPurchase Requisition ReleasedSend Purchase Order to VendorPurchase Order Sent to VendorReceive Purchase Order ConfirmationOrder Confirmed by VendorReceive Shipment ConfirmationOrder ShippedReceive ShipmentOrder Received in FullNote For non-stock components, all the six milestones are applicable. For lean services or external operations, only the first four milestones are applicable. | A green symbol indicates that the milestones are complete.A yellow symbol indicates that the milestone is pending completion and the warning period has started.A red symbol indicates that the milestone is pending completion and its due date has been reached or passed.A grey symbol indicates that the milestone is not yet pending completion. |  |
| 9 | Procurement Milestone: Purchase Requisition Created | When a maintenance order with non-stock material or service is released and saved, a purchase requisition gets created and released. For more information, see [Review and Release Maintenance Order](#unique_50) [page ] 75. | The procurement milestone Purchase Requisition Created is green in color. |  |
| 10 | Procurement Milestone: Purchase Requisition Released | When a maintenance order with non-stock material or service is released and saved, a purchase requisition gets created and released. For more information, see [Review and Release Maintenance Order](#unique_50) [page ] 75. | Procurement Milestone: Purchase Requisition Released is green in color. |  |
| 11 | Procurement Milestone: Purchase Order Sent to Vendor | If output management is enabled and print or email is taken, then milestone will turn green. | Procurement Milestone: Purchase Order Sent toVendor is green in color. |  |
| 12 | Procurement Milestone: Order Confirmed by Vendor | The order confirmed by the vendor milestone turns green when one or more order acknowledgments for the entire requirement quantity have been entered in the purchase order. Follow these steps:Open the Change Purchase Order - Advanced (ME22N) application after logging in as PurchaserChoose Other Purchase Order button and enter the PO number.Choose Item Detail option and go to the Confirmations tab.Choose Confirmation Control.Select the Acknowl. Reqd checkbox.Press EnterEnter the following:Confirmation control: AB (Order Acknowledgement)Delivery Date:Quantity: <Enter the PO quantity>Press EnterChoose Save | Procurement Milestone: Order Confirmed by Vendor is green in color. |  |
| 13 | Procurement Milestone: Order Shipped | The order shipped milestone turns green when:Option 1: The Delivery Completed checkbox is selected in the purchase order.Option 2: One or more shipping notifications for the entire requirement quantity have been entered in the purchase order.Follow these steps:Open the Change Purchase Order - Advanced (ME22N) application after logging in as PurchaserChoose Other Purchase Order button and enter the PO number.Choose Item Detail option and go to the Confirmations tab.Choose Confirmation Control.Select the Acknowl. Reqd checkbox.Press EnterEnter the following:Confirmation control: LA (Inbound Delivery)Delivery Date:Quantity: <Enter the PO quantity> .Press EnterChoose Save | Procurement Milestone: Order Shipped is green in color. |  |
| 14 | Procurement Milestone: Order Received in Full | Order received in full milestone turns green when the goods receipts have been posted for the entire requirement quantity.You can find the detailed steps in the following sections:For non-stock components, see [Goods Receipt for Purchase Order](#unique_52) [page ] 77.For services, see [Maintain Service Entry Sheet](#unique_56) [page ] 92. | Procurement Milestone: Order Received in Full is green in color. |  |

### Submit Order for Scheduling

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

Table 18:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Find Maintenance Orders - Completion (F2175) app. | A list of orders is displayed. |  |
| 3 | Get List of Maintenance Orders | Enter the following:Technical object: 233100091Choose Go | A list of maintenance orders is displayed based on the filter criteria. |  |
| 4 | Set Order to Ready to Schedule | Select the order by selecting the checkbox.Choose Change Status > Ready to Schedule | The maintenance order is in Scheduling phase. |  |

### Add Safety Instructions (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To keep workers safe at their workplace while operating a dangerous equipment, it's necessary to supply them with safety instructions. This test procedure shows how to include safety instructions in a maintenance order.

|  |
| --- |
| Note You need to activate the scope item ‏54A (Health and Safety Management) . If you have activated the scope item ‏54A, the configuration expert can enable the integration with the Activate Integration with Environment, Health, and Safety activity. For more information, see [Configuration Environment of SAP S/4HANA Cloud Public Edition.](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/0b3f87579f345c08e10000000a441470.html?version=2202.503). |

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 19:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Change Maintenance Order (EAMS_WDA_ORDNTF_OIF) app. | The app opens. |  |
| 3 | Enter Order Number | Enter the order number and choose Continue | Change Maintenance Order screen is displayed. |  |
| 4 | Add Safety Instructions | Follow these steps:Go to the Documents tab. You can see an overview of the documents.Choose the Add Safety Instructions button under Document Assignments.Enter the required parameters and choose Go to get the list of safety instructions.Select the required safety instructions checkbox and choose OK.You can also choose Show/Hide Documents of Dependent Objects to get list of documents assigned to a technical object.Select the required safety instructions checkbox and choose Assign Document to Order under Maintain Document Assignments dropdown list.You can also choose to assign a document to an operation or suboperation or assign a document to a material or a service.Choose Save. | Safety Instructions are included in the maintenance order. |  |

### Schedule Maintenance Orders and Submit for Execution

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

Table 20:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Find Maintenance Orders - Completion (F2175) app. | The app opens. |  |
| 3 | Review List of Maintenance Order | Enter the following:Technical object: 233100091Choose Go | A list of maintenance orders is displayed based on the filter criteria.You can review and check if the order is in Scheduling phase. |  |
| 4 | Set Orders to Ready for Execution | Select the order by selecting the checkbox.Choose the Dispatch Operations button.Note If the scope item 43R (Resource Scheduling) is activated, the corresponding applications can be used for dispatching the operations. | The order operations are dispatched and the maintenance order is in Execution phase. |  |

### Manage Output

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

Table 21:

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

### Execute Maintenance Order

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

Table 22:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Technician. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Perform Maintenance Jobs (F5104A) app. | The app opens. |  |
| 3 | Get List of Maintenance Order Operations | Enter the following:Execution Object: The maintenance order number which was dispatched for execution in the previous stepChoose Go. | A list of dispatched operations for the selected order is displayed. |  |
| 4 | Assign Operations | Select the operations and choose Assign to MeNote The Assign to Me button is enabled only if the order operation is not assigned to anyone | The operations are assigned to you. |  |
| 5 | Select the Operation for Processing | Choose the operation and navigate to the Perform Maintenance Job screen. | Perform Maintenance Job screen is displayed with the details of the operation. |  |
| 6 | Start the Operation | Choose Start. | The subphase is changed to Work in Execution. |  |
| 7 | Review Components | Go to Components tab and review the planned component details. | The component details are reviewed. |  |
| 8 | Goods Issue or Return (Optional) | Go to Planned Components in the Components tabChoose Post for the component that the maintenance technician wants to issue.The Post Goods Issue screen is displayed. Enter the required quantity and the movement description.Choose Post.Choose Return for the component that the maintenance technician wants to return.The Return Goods screen is displayed. Enter the required quantity and choose Return.A new line item for the respective component is added.Choose Post.The Post Goods Return screen is displayed. Enter the required quantity and the movement description.Choose Post. | The components are issued or returned. |  |
| 9 | Review Attachments | Go to the Attachments tab to review the attachments. If required, you can also upload new files and add a link. | The attachments are reviewed.The files and links are added. |  |
| 10 | Pause and Resume Work | Choose Pause button to pause the work.After you pause the work, you can restart the work by choosing Resume. | For an operation that has been paused, the subphase will be Work Paused.When you resume the work, the subphase changes to Work in Execution. |  |
| 11 | Time Confirmation | Choose Record Time on the top left corner of the Perform Maintenance Job screen. The Record Time screen is displayed. Enter the following:Actual work. For example, 4 hoursRemaining work, if any. For example, 2 hours.Enter the confirmation text as required.Select the checkbox Final Confirmation and choose Record to do the final confirmation for the operation.Repeat this for all the operations in the PRE and MAIN execution stages. | The final confirmations are posted and can be reviewed in the Confirmation tabThe work progress is shown as 100 %.The subphase is changed to Work Finished. |  |
| 12 | Add Measurement (Optional) | Follow these steps:Go to Measurements tabSelect All Measuring Points from the Technical Object Association dropdown list.Go to Latest Reading tabChoose Add Meaurements.Enter the current reading for the measuring point and press Enter.Select the date and the time using the Calender button.Choose Save. | The measurement reading is updated and can be seen in the Previous Reading column of the corresponding measuring point. |  |

### Complete Main Work

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

Table 23:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Supervisor | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Find Maintenance Orders - Completion (F2175) app. | A list of maintenance orders is displayed. |  |
| 3 | Get List of Maintenance Orders | Enter the following:Technical object: 217100091Choose Go. | A list of maintenance orders is displayed based on the filter criteria. |  |
| 4 | Set Order Status to Order Main Work Completed | Select the order by selecting the checkbox.Choose Change Status > Main Work Completed . | The Main Work Completed screen is displayed. |  |
| 5 | Enter Reference Data | Enter the following:Main Work Completion Date and Time: The default values are displayed. Use the calendar icon to change the values.Set Main Work Completion Date and Time as Reference Date and Time: Select this checkbox.Choose OK | The order status is set to Order Main Work Completed. |  |

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

This section describes test procedures for each process step that belongs to this scope item.

Table 24:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Manage Service Entry Sheets - Lean Services (F2027) app. | The app opens. |  |
| 3 | Enter Field ValuesCase 1: Purchase service without material numberCase 2: Purchase service with material number | Choose Create.On the Service Entry Sheet screen, enter the following:Name of Service Entry Sheet: <SES Name>, for example, Vincent SunReference Purchase Order: <Purchase order you created>In the Add Purchase Order Items popup that opens, select the checkboxes for the purchase order items.Increase or decrease the service entry sheet items using the "+" / "-" buttonsChoose the Add button.Enter the posting date for goods receipt: <Today’s date>In the Items area, choose Purchase Order Item and enter the following for each item:Performance Period: <Enter the date range>Stated Quantity: < Stated Quantity >. For example,10Unit of measure: <Unit>.For example, HChoose Apply. |  |  |
| 4 | Add Attachments in Service Entry Sheet (Optional) | You can upload files using the Upload button or add a link to the service entry sheet and view the existing attachments by following one of these:On the header level, go to tab AttachmentsOn the item level, go to tab Items, open the details and go to tab Attachments.If the attachments are not required any longer, you can delete them.You can view the attachments and save them on your device regardless of the status of the service entry sheet.You can add or delete attachments only while editing the service entry sheet. This means that the status of the service entry sheet must be In Process. |  |  |
| 5 | Create Service Entry Sheet | Choose Create | The service entry sheet is created. |  |
| 6 | Send for Approval | Choose Send for Approval. | The service entry sheet is sent for approval. |  |
| 7 | Check the Status of the Service Entry Sheet. | On the Manage Service Entry Sheets screen, follow these steps:Search for the service entry sheet that you had created aboveCheck the status of the service entry sheet.Send service entry sheet for approval if approval is required.If the status is Approved, do not send the service entry sheet for approval with flexible workflow. |  |  |

### Execute Post Work Operations

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

Table 25:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Technician. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Perform Maintenance Jobs (F5104A) app. | The app opens. |  |
| 3 | Get List of Maintenance Order Operations | Enter the followingExecution Object: The maintenance order number which was dispatched for execution in the previous stepChoose Go | A list of dispatched operations for the selected order is displayed. |  |
| 4 | Select the Operation for Processing | Choose the operation in POST stage to navigate to the Perform Maintenance Job screen. | Perform Maintenance Job screen is displayed with the details of the operation. |  |
| 5 | Start the Operation | Choose Start. | The subphase is changed to Work in Execution. |  |
| 6 | Edit Malfunction Data | Follow these steps:Go to the Malfunction Data section.Choose the Edit button.The Edit Malfunction Data screen is displayed.Select an effect from dropdown list.Select a failure mode from dropdown list.Select a detection method from dropdown list.Enter Malfunction Start Date and Time as today's date and time in the following format: 09:00:00 amEnter Malfunction End Date and Time as today's date and time in the following format: 11:00:00 am.Select the checkbox if there is a breakdown. The breakdown duration is calculated.Enter the malfunction long text.Click on Save button. | The malfunction data is saved. |  |
| 7 | Record Malfunction Details | Follow these steps:Go to the Malfunction Data → Malfunction Details.Choose the Add button.The Add Malfunction Data screen is displayed.Enter the following details in the Damage Details tab:Select the object part from dropdown list.Select the damage code from dropdown list.Enter a description for the damage.Enter the following details on the Cause tab:Select the cause code from dropdown list.Enter a description for the cause.Select the Root Cause radio button.Enter the following details on the Activity tab:Select the activity code from dropdown listEnter a description for the activity.Click Record button.You can add additional causes and activities using the New Cause and New Activity buttons respectively. | The malfunction details are recorded. |  |
| 8 | Time confirmation | Choose Record Time on the top right corner of the Perform Maintenance Job screen.The Record Time screen is displayed. Enter the following details:Enter the actual work. For example, 4 hoursEnter the remaining work if any. For example , 2 hours.Enter a description for the confirmation as required.Select the Final Confirmation checkbox and choose Record to do the final confirmation on the operation.Repeat this for all the operations in the POST execution stage. | The final confirmations are posted and can be reviewed under the Confirmation tab.The work progress is shown as 100 %.The subphase is changed to Work Finished. |  |

### Review Maintenance Cost

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

Table 26:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Maintenance Order Costs - Plan / Actual (F4603) app. | The app opens. |  |
| 3 | Get Details | Enter the following details as filters:Relative Date Function: Previous 30 daysG/L Account Hierarchy: YPS2Ledger: 0LCompany Code: 3310Equipment: 233100091Choose Go. | Based on the filter values, different types of maintenance costs are analyzed and reviewed. |  |

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

The technical completion clears all the purchase requisitions, open reservations, and capacities still outstanding for the maintenance order.

Nevertheless, the order can continue to receive costs, for example, through invoice receipts for delivered and used materials. However it is blocked for all changes in the processing.

The order settlement transfers the costs incurred that were temporarily collected for the maintenance order, to the recipient, for example, to the cost center for the maintained object. This process step shows you how to technically complete a maintenance order.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 27:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Find Maintenance Orders - Completion (F2175) app. | The app opens. |  |
| 3 | Get List of Maintenance Orders | Enter the following:Order Type: Proactive Maintenance (YA02)Choose GO. | A list of maintenance orders is displayed based on the search criteria. |  |
| 5 | Set order status to Technically Completed | Select the order by selecting the check box.Choose Change Status > Complete Technically. | The Complete Technically screen is displayed. |  |
| 6 | Enter Reference Data | Enter the following:Completion Date/Time: The default values are displayed. Use the calendar icon to change the values.Keep Default Values: Select this checkboxComplete Assigned Notifications: Select this checkbox if you want to complete the assigned notifications.Choose Complete Technically | The order is technically completed. |  |

### Create Supplier Invoice with PO/GR Relation

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

Table 28:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open the App | Open Create Supplier Invoice - Advanced (MIRO). | The app opens. |  |
| 3 | Navigation | If the system prompts you, enter the following and choose Continue:Company Code: 3310 | The Enter Incoming Invoice screen is displayed. |  |
| 4 | Enter Basic Data | Enter the following:Transaction: InvoiceInvoice Date: Today's datePosting Date: Today's dateReference: <Reference invoice number from invoicing party>Amount: <Amount according to the invoice value>.Currency: AEDSelect Calculate TaxTax Code: Enter the tax code.If there is no tax, specify the tax code I0 (for Brazil, it is 00).If G/L account is subjected to tax, ensure that you enter an appropriate tax code. | Basic data is entered. |  |
| 5 | Enter Purchase Order References | On the Purchase Order References screen, make the following entries:Reference Document Category: Purchase Order/ Scheduling AgreementPurchase Order: Enter the purchase order you posted in the previous step. | The Purchase Order References screen is displayed. |  |
| 6 | Check the Purchase Order Items Data | Check the amount, the quantity and the tax code. | The amount and the quantity correspond to the values of the goods receipts. |  |
| 7 | Check Tax Code | In the Tax area, check the tax code information and the tax amount. |  |  |
| 8 | Simulate Supplier Invoice and Check Messages | Choose Simulate.If there are no differences (or if the value is within the defined tolerance), the Simulation screen displays. You can check the results in the Simulation Overview and Simulation Details areas.Review the Gross Invoice Amount against the items plus tax amount (if tax code is 10, (for Brazil, it is 00), you do not have any tax amount) |  |  |
|  | Post Invoice | Choose Post. | The invoice document is posted. |  |

### Condition Based Maintenance (Optional)

#### Create Measurement Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Maintenance Tehnician needs to record reading of the technical objects (equipment / functional location) in the SAP system. This process also can be automated my making use of the systems which gets the reading from technical objects and loads to SAP system through interfaces. Once the readings are posted, system will check with the conditions maintained for the measuring point. If any deviation is observed, a notification will be triggered.

|  |
| --- |
| Note Select the Measuring Point for which Measuring Point Category is configured for Condition Based Maintenance. To know how to configure measurement point category for CBM, refer to 5MI test script |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Maintenance Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Open the App | Open Create Measurement Document for Technical Object (EAMS_WDA_MD_OIF).On the Create Measurement Documents screen, make the following entries:Basis for measurement reading: Measuring PointMeasuring Point: < Measuring Point NoComment: Enter the measuring point number that was created against the technical object.Choose Continue | The app opens. |  |
| 3 | Enter | A new screen appears with the measuring points you entered:Reading: < Measuring Point reading >Choose Save | Measurement document is created.A Notification will be created if the reading deviates from the conditions maintained for measuring point |  |

## Appendix

### Process Integration

#### Preceding Processes

You must first complete the following processes before you start with the test steps:

Table 29:

| Process | Business Condition |
| --- | --- |
| Create New Open MM Posting Period (BNZ) | A new MM period must exist |
| Period-End Closing - Maintenance Orders (BF7) | Activity types rates to be maintained |
| Create Measuring Point master data script (5MI) | Measuring point creation |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

Table 30:

| Process | Business Condition |
| --- | --- |
| Accounts Payable (J60) | Use the master data from this test script and execute the following steps:Invoice payment preparationPayment runSingle outgoing paymentManual Payment online |
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

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/test-script-preventive-maintenance-bj2-ae-sap-s-4hana-cloud-public-edi]]
- related-to :: [[14-maintenance-service-and-projects/test-script-recurring-services-4x5-ae-sap-s-4hana-cloud-public-edition]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4HI_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 161,623 chars in the whole document
