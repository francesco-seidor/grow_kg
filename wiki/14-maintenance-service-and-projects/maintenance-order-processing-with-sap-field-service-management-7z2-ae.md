---
id: 14-maintenance-service-and-projects/maintenance-order-processing-with-sap-field-service-management-7z2-ae
title: Maintenance Order Processing with SAP Field Service Management (7Z2_AE) - Test Script (7Z2_S4CLD2608_BPD_EN_AE)
description: "Test script for scope item 7Z2 (AE): reactive maintenance orders in S/4HANA Cloud Public Edition 2608 integrated with SAP Field Service Management; prerequisites, config, test steps."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/field-service-and-mobile-maintenance]
aliases: [7Z2_S4CLD2608_BPD_EN_AE]
keywords: [Field Service Management and Mobile Maintenance, maintenance order processing, field service management integration, reactive maintenance, fsm integration configuration, maintenance notifications, service call dispatching, service confirmation, multiple company replication, technician mobile app]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7Z2_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1238
topic: 14-maintenance-service-and-projects/field-service-and-mobile-maintenance
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Maintenance Order Processing with SAP Field Service Management (7Z2_AE) - Test Script (7Z2_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7Z2_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Field Service Management and Mobile Maintenance** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Maintenance Order Processing with SAP Field Service Management (7Z2_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Maintenance Order Processing with SAP Field Service Management (7Z2_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232860747)

[2 Prerequisites 4](#_Toc232860748)

[2.1 System Access 4](#_Toc232860749)

[2.2 Roles 4](#_Toc232860750)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232860751)

[2.4 Business Conditions 7](#_Toc232860752)

[2.5 Additional Manual Configuration 8](#_Toc232860753)

[2.6 Preliminary Steps 8](#_Toc232860754)

[2.6.1 Initializing Material Stock 8](#_Toc232860755)

[2.6.2 Configure Flexible Workflow for Maintenance Orders 9](#_Toc232860756)

[2.6.3 Maintain Cost Rates 10](#_Toc232860757)

[2.6.4 Create Purchasing Information Record 11](#_Toc232860758)

[2.6.5 Configure Multiple Company Replication for Maintenance Orders (Optional) 13](#_Toc232860759)

[2.6.6 Configure Mapping for Expense Type 17](#_Toc232860760)

[2.6.7 Configure Mapping for Expense Type Item 19](#_Toc232860761)

[2.6.8 Define Plant Specific Order Types 22](#_Toc232860762)

[2.6.9 Define System Status to Filter Maintenance Order Replication 23](#_Toc232860763)

[2.6.10 Configure Mapping for Priority Codelist 26](#_Toc232860764)

[2.6.11 Configure Mapping for Problem Type Codelist 28](#_Toc232860765)

[2.6.12 Configure Region 31](#_Toc232860766)

[2.6.13 Configure Mapping for Service Call Type Codelist 33](#_Toc232860767)

[2.6.14 Set Default Business Partner (Customer) 35](#_Toc232860768)

[2.6.15 Configure Mapping for Phase Codelist 37](#_Toc232860769)

[2.6.16 Creation of Work Centre in SAP Field Service Management 40](#_Toc232860770)

[2.6.17 Download SAP Field Service Management Mobile Application 41](#_Toc232860771)

[3 Overview Table 42](#_Toc232860772)

[4 Test Procedures 44](#_Toc232860773)

[4.1 Create a Reactive Maintenance Order and Replicate to SAP Field Service Management 44](#_Toc232860774)

[4.1.1 Create Maintenance Notification 44](#_Toc232860775)

[4.1.2 Review Maintenance Notifications 45](#_Toc232860776)

[4.1.3 Screen Maintenance Requests 46](#_Toc232860777)

[4.1.4 Create and Plan Maintenance Order 48](#_Toc232860778)

[4.1.5 Submit Maintenance Order for Approval 51](#_Toc232860779)

[4.1.6 Approve Maintenance Order (Optional) 52](#_Toc232860780)

[4.1.7 Review and Release Maintenance Order 52](#_Toc232860781)

[4.1.8 Convert Purchase Requisitions to Purchase Orders 53](#_Toc232860782)

[4.1.9 Submit Order for Scheduling 54](#_Toc232860783)

[4.2 Update a Released Maintenance Order in S/4HANA Public Cloud 56](#_Toc232860784)

[4.2.1 Create a new Operation in Maintenance Order (Optional) 56](#_Toc232860785)

[4.3 Update Maintenance Order in S/4HANA Cloud When Service Call or Activity is Updated in FSM 57](#_Toc232860786)

[4.3.1 Update a Service Call (Optional) 57](#_Toc232860787)

[4.3.2 Update an Actvity (Optional) 59](#_Toc232860788)

[4.3.3 Dispatch Plan and Release Activity 60](#_Toc232860789)

[4.3.4 Reassign Service Technician and Release Activity (Optional) 61](#_Toc232860790)

[4.3.5 Create a New Activity 63](#_Toc232860791)

[4.3.6 Duplicate an Activity 65](#_Toc232860792)

[4.4 Create a Completed Service Confirmation in S/4HANA Cloud when Time Effort, Material or Expense is Approved in FSM 66](#_Toc232860793)

[4.4.1 Technician Starts Working on Activity 66](#_Toc232860794)

[4.4.2 Updates Time, Use Reserved Material, Add Unplanned Material, and Add Expenses 67](#_Toc232860795)

[4.4.3 Manager Approves Time Effort, Expense and Material 69](#_Toc232860796)

[4.5 Technically Complete a Maintenance Order in SAP S/4HANA Cloud Public Edition and Corresponding Service Call is Technically Completed in FSM 70](#_Toc232860797)

[5 Appendix 72](#_Toc232860798)

[5.1 Process Integration 72](#_Toc232860799)

[5.1.1 Preceding Processes 72](#_Toc232860800)

## Purpose

Overview

This scope item describes end-to-end business scenarios that connect SAP S/4HANA Cloud Public Edition reactive maintenance order processing with SAP Field Service Management. The reactive maintenance process lets users perform maintenance on assets when a breakdown or failure occurs.

After users create and release a reactive maintenance order in SAP S/4HANA Cloud Public Edition, the system creates a corresponding service call in SAP Field Service Management. The system creates an activity for each operation in the maintenance order. It also replicates components as reserved materials.

Users assign an activity to a technician on the planning board in SAP Field Service Management. When users release the activity, the system automatically updates the technician in the corresponding maintenance order operation in SAP S/4HANA Cloud Public Edition.

When users approve confirmations such as efforts, expenses, or materials in SAP Field Service Management, the system creates a confirmation in the maintenance order and automatically completes it in SAP S/4HANA Cloud Public Edition.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

### System Access

The test should be conducted with the following system.

|  |
| --- |
| Note For system details contact your System Administrator. |

| System | Access Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP Field Service Management – SAP FSM | Accessible via SAP FSM. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| Cloud Integration Package with SAP Cloud Platform Integration – SAP CPI | Accessible via SAP CPI. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Space) | ID (Space) |
| --- | --- | --- | --- |
| Maintenance Planner | SAP_BR_MAINTENANCE_PLANNER | Maintenance Planning | SAP_BR_MAINTENANCE_PLANNER |
| Employee | SAP_BR_EMPLOYEE | Self Services / Self Services / Employee Overview Space | SAP_BR_EMPLOYEE / SAP_CA_SPT_EMPLOYEE_CROSS_PC / SAP_EAM_SPT_EMPLOYEE_PC |
| Maintenance Supervisor | SAP_BR_MAINT_SUPERVISOR | Maintenance Supervision | SAP_BR_MAINTENANCE_SUPERVISOR |
| Maintenance Technician | SAP_BR_MAINTENANCE_TECHNICIAN | Maintenance Execution | SAP_BR_MAINTENANCE_TECHNICIAN |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |
| Purchaser | SAP_BR_PURCHASER |  |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |
| Employee | SAP_BR_EMPLOYEE | Self Services / Self Services / Employee Overview Space | SAP_BR_EMPLOYEE / SAP_CA_SPT_EMPLOYEE_CROSS_PC / SAP_EAM_SPT_EMPLOYEE_PC |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |

Use the following standard test users or assign roles to testers, respectively for SAP FSM:

| Name | ID | Log On |
| --- | --- | --- |
| Service Technician - Customer Service |  | Your system administrator provides the user and password information. |
| Service Planner |  | Your system administrator provides the user and password information. |
| Backend Office Manager |  | Your system administrator provides the user and password information. |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

|  |
| --- |
| Note For every SAP S/4HANA Cloud Public Edition master data element used in your test procedure, the corresponding master data element with the proper External Id must exist in SAP Field Service Management. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Equipment | 210100091 | Cooling Water Circulation Pump |  |
| Equipment | 210100093 | Cooling Water Circulation Pump |  |
| Equipment | 21010XXXX |  | 210100001 ~210100092 |
| Spare Parts | SP001 | Bearing | Spare parts |
| Spare Parts | SP002 | Coupling | Spare parts |
| Spare Parts | SP003 | Shaft | Spare parts |
| Spare Parts | SP004 | Gaskets 1mm | Spare parts |
| Spare Parts | SP005 | Mechanical Seal | Spare parts |
| Spare Parts | SP006 | Spur gear IS651 | Spare parts |
| Non-stock Material | NL001 | Screw |  |
| Service Material | SM0001 | Service Material 01 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 2 |  |
| Supplier | 33300001 | Domestic 10 Supplier 1 |  |
| Customer | 33100001 | Domestic 10 Customer 1 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| 3KV | Create Service Product for Service Processes - MDS |
| 2J7 | Create Product Master of type "Spare Parts" - MDS |
| 5LM | Create Functional Location - MDS |
| 5MF | Create Equipment - MDS |
| 5MH | Create Maintenance Work Center - MDS |
| 5MI | Create Measuring Point - MDS |

|  |
| --- |
| Note Please take the steps for product SRV_02 in the master data script 3KV as the sample to create the following products.Product IDDescriptionCommentsEXP_FSM_ACCOMExpense Item for AccommodationEXP_FSM_MEALSExpense Item for MealsEXP_FSM_OTHERExpense Item for othersEXP_FSM_TRAVELExpense Item for Travel |

|  |
| --- |
| Note For more information about the Field Mapping between SAP S/4HANA Cloud Public Edition and SAP Field Service Management, see the guide "Set up Guide of Integration with SAP Field Service Management”, sections Field Mapping and Value Mapping. |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 4HH - Reactive Maintenance | Create maintenance orders with Reactive Maintenance. |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific to your implementation and include mandatory settings that are not delivered by SAP and must be created by you.

For more information, see [Setup Instruction of 7Z2](https://help.sap.com/docs/s4hana-best-practices/setting-up-maintenance-order-processing-with-sap-field-service-management-7z2)

### Preliminary Steps

#### Initializing Material Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In a real business case, the materials are usually purchased from external suppliers using standard purchasing or subcontracting processes. This step shows how to post initial stock directly to storage locations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen is displayed. |  |
| 3 | Input Material | Make the following entries and choose Enter:Material: <material number> (select one of the spare parts mentioned in Master Data)Plant: 3310 | You have entered the details. |  |
| 4 | Select Stock | Select the icon beside the stock to add initial stock, for example:Storage Location: 331BStock Type: Unrestricted-Use Stock | A dialog opens showing storage location, stock type, and current quantity based on your entries. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Document Date: <today>Posting Date: <today>Stock Change: Initial entryQuantity: <quantity number> | The material document is created and the stock has been added. |  |

#### Configure Flexible Workflow for Maintenance Orders

Purpose

In this procedure, you configure and activate flexible workflow for maintenance orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Workflows for Maintenance Orders - Asset Management (F4989). | The Manage Workflows screen is displayed. |  |
| 3 | Check Automatic Approval of Maintenance Order | In the Workflows list, choose Automatic Approval of Maintenance Order. Ensure the workflow is active; if not, select it and choose Activate. | The workflow item is activated. |  |
| 4 | Manage Workflow | You can also create a custom workflow. When a workflow is triggered, it determines the agents who can approve the maintenance order. Choose Create and make the following entries:Workflow Name: <Enter Text>Go to the START CONDITIONS area and choose Maintenance Order Type is <Enter Order Type>. | Custom workflow details entered. |  |
| 5 | Create Step Sequence | Go to the STEPS area and choose Create, then on the next screen maintain:In the RECIPIENTS area:Assignment By: UserUser: <Enter User ID>Step to be completed by: One of the recipientsIn the Step Conditions area, choose Main Work Center of the maintenance order is <Enter Main Work Center>. Choose Create. | Step sequence created. |  |
| 6 | Save Workflow | Choose Save. | Workflow is created. |  |
| 7 | Activate Workflow | Go back to the workflow list. Select the required workflow and choose Activate. | The workflow is activated. |  |

#### Maintain Cost Rates

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Cost Rates - Plan (F3162). | The Manage Cost Rates - Plan app opens. |  |
| 3 | Check Actual Cost Rates | Set the following filters and choose Go:Valid On: TodayCost Center: 33101701Activity Type: 11Currency: for example, AED | The actual cost rates for the given cost center, activity type, and period are checked for valid values.Note You can skip the next step if there is a valid cost rate for the given cost center, activity type, and period. |  |
| 4 | Maintain Actual Cost Rates | Choose Add and enter the following data. Then choose Save.Cost Center: 33101701Activity Type: 11From Fiscal Year: Current YearFrom Period: Current PeriodFixed Rate: 100Currency: for example, AEDPer: 1Activity Unit: H | Cost rates are created. |  |

#### Create Purchasing Information Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to create the information records for materials, for example, NL001 and choose a valid supplier (for example, 10300001). This step becomes obsolete if the necessary information records are already present.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Manage Purchasing Info Records (F1982) app. | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record screen displays. |  |
| 4 | Enter Header Data | Go to header area and enter the following:Purchasing Info Record Category: StandardPurchasing Organization: 3310Supplier: 17300001Material: NL001Plant: 3310Purchasing Group: 001 | Header data is added. |  |
| 5 | Enter General Information | Enter the following:Available From: TodayAvailable To: 12/31/9999 | General information is added. |  |
| 6 | Enter Purchasing Data | Enter the following:Incoterm: EXWIncoterm Location 1: Vendor | Purchasing data is added. |  |
| 7 | Enter Delivery and Quantity Data | Enter the following details:Delivery Time in Days: <XX Days>, for example, 1Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10.0Tax Code: <Tax Code>, for example, I0Order Unit: PCStandard Order Quantity: <Standard Order Quantity>, for example, 10 | Delivery and quantity data is added. |  |
| 8 | Enter Condition Data | Go to the Conditions area. Choose the Create icon. Enter the following:Valid From: <Valid from Date>Amount: <Amount>, for example, 1Currency: <Currency>, for example, AEDPricing Unit: <Pricing Unit>, for example, 1Valid To: <Valid to Date>Choose Apply. | Condition data is added. |  |
| 9 | Enter Reference Data (Optional) | You can enter reference data. | Reference data is added. |  |
| 10 | Create Purchasing Information Record | Choose Create. | A purchasing information record is created. |  |

#### Configure Multiple Company Replication for Maintenance Orders (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

We can replicate business objects from SAP S/4HANA Cloud Public Edition to one or more companies in SAP Field Service Management.

In the below table, you can find different business objects mapped to different FSM Companies based on specific rules.

| Business Object | Rule Type | Relevant Value | Maintenance Order Type | FSM Company |
| --- | --- | --- | --- | --- |
| Maintenance Order | Plant | 1010 | YA01 | Company A |
| 1710 | YA01 | Company B |  |  |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Make the following entries:Application Area: select Field Service and Asset Management.Sub Application Area: select Integration.Choose the row with the item names: Integration with SAP Field Service and Asset ManagementFind the step Configure Multiple Company Replication and choose Configure. | The Configure Multiple Company Replication screen displays. |  |
| 4 | Define S/4HANA FSM Company | Choose New Entries.Enter the following details:S/4HANA Company ID: 00001S/4 HANA FSM Company Name: <Provide the description>Choose Save.Note Add the second company in the same way mentioned above. | The FSM Company for SAP S/4HANA Cloud Public Edition is defined. |  |
| 5 | Assign FSM Company Details | Select the company defined in the previous step and click on the new node Assignment of FSM Company Details.Choose New Entries.Enter the following details:Account ID: <Provide the Account ID>Company ID: <Provide the Company ID>Choose Save.Note Ensure that you have the FSM account and company IDs before configuring multiple companies. | The FSM Company details are assigned. |  |
| 6 | Assign Replication Object Details | Choose New Entries.Enter the following details:Replication Object: PM Maintenance OrderChoose Save. | The Replication Object details are defined. |  |
| 7 | Assign Relevant Plants | Select the Replication Object: PM defined from the previous step and click on the node: Assign Relevant PlantsChoose New Entries.Enter the following details:Plant: 3310Order Type: YA01Choose Save.Note Currently Order Type YA01 is only supported in FSM. | The relevant plants and order type are defined against the company ID. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Configure Multiple Company Replication | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: SSCUI ID – 106807 Configure Multiple Company ReplicationChoose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Multiple Company Replication screen displays. |  |
| 3 | Define S/4HANA FSM Company | Choose New Entries.Enter the following details:S/4HANA Company ID: 00001S/4 HANA FSM Company Name: <Provide the description>Choose Save.Note Add the second company in the same way mentioned above. | The FSM Company for SAP S/4HANA Cloud Public Edition is defined. |  |
| 4 | Assign FSM Company Details | Select the company defined in the previous step and click on the new node Assignment of FSM Company Details.Choose New Entries.Enter the following details:Account ID: <Provide the Account ID>Company ID: <Provide the Company ID>Choose Save.Note Ensure that you have the FSM account and company IDs before configuring multiple companies. | The FSM Company details are assigned. |  |
| 5 | Assign Replication Object Details | Choose New Entries.Enter the following detail:Replication Object: PM Maintenance OrderChoose Save. | The Replication Object detail has been defined |  |
| 6 | Assign Relevant Plants | Select the Replication Object: PM defined from the previous step and click on the node: Assign Relevant PlantsChoose New Entries.Enter the following details:Plant: 3310Order Type: YA01Choose Save.Note Currently Order Type YA01 is only supported in FSM. | The relevant plants and order type are defined against the company ID. |  |

#### Configure Mapping for Expense Type

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to configure the mapping for Expense Type.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Edit Configuration | Choose Configure Your Solution.Select the Application Area: Asset ManagementSelect the Sub Application Area: Maintenance ManagementSelect the row with the item name: Integration with SAP Field Service ManagementStep Name: Configure Mapping for Expense Type | The Configure Mapping for Expense Type screen is displayed. |  |
| 4 | Create the Entry | Choose New Entries.Enter the following details:Expense Type: -1Company Code: 3310Document Type: G/L Account DocumentRepeat the step for the following entries:Note If there are multiple Company IDs, repeat the same step for each Company ID.S4 Cmp. IDOrder TypeExpense TypeCompany CodeDocument Type00001 (Defaulted automatically)YA01 (Defaulted automatically)-23310G/L Account Document00001 (Defaulted automatically)YA01 (Defaulted automatically)-33310G/L Account Document00001 (Defaulted automatically)YA01 (Defaulted automatically)-43310G/L Account Document | The Expense Type is created. |  |
| 5 | Save the Entries | Choose Save. | Expense Type is saved. |  |

SAP Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Configure Mapping for Expense Type | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: SSCUI ID - 107208 Configure Mapping for Expense Type.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Mapping for Expense Type screen displays. |  |
| 3 | Create the Entry | Choose New Entries.Enter the following details:Expense Type: -1Company Code: 3310Document Type: G/L Account DocumentRepeat the step for the following entries:Note If there are multiple Company IDs, repeat the same step for each Company ID.S4 Cmp IDOrder TypeExpense TypeCompany CodeDocument Type00001 (Defaulted automatically)YA01 (Defaulted automatically)-23310G/L Account Document00001 (Defaulted automatically)YA01 (Defaulted automatically)-33310G/L Account Document00001 (Defaulted automatically)YA01 (Defaulted automatically)-43310G/L Account Document | The Expense Type is created. |  |
| 4 | Save the Entries | Choose Save. | Expense Type is saved. |  |

#### Configure Mapping for Expense Type Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to used to configure the mapping for Expense Type item.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Select the Application Area as Asset Management.Select the Sub Application Area as Maintenance Management.Select the row with the item name: Integration with SAP Field Service Management.Step Name: Configure Mapping for Expense Type Item. | The Configure Mapping for Expense Type Item screen is displayed. |  |
| 4 | Create the Entry | Choose New Entries.Enter the following details:S/4 Cmp. ID: 00001Order Type: YA01Debit/Credit: HG/L account – Chargeable: Enter Chargeable G/L Account. For example: 65008430G/L account – Non Chargeable: Enter Chargeable G/L Account. For example: 51100000Tax Code: V2Cost Center: 33101001Assignment: Enter valid assignment: For example: 001010110Profit Center:Note If there are multiple Company IDs, repeat the same step for each Company ID.Make sure these cost center and G/L accounts are replicated prior hand.Repeat the step for the following entry.S/4 Cmp. IDOrder TypeDebit/CreditG/L account – ChargeableG/L account – Non ChargeableTax CodeCost CenterAssignmentProfit Center00001YA01S5110000051100000V210101710001010110 | The Expense Item Type is created. |  |
| 5 | Save the Entries | Choose Save. | Expense Type is saved. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Configure Mapping for Expense Type Item | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: SSCUI ID - 107209 Configure Mapping for Expense Type Item.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Mapping for Expense Type Item screen displays. |  |
| 3 | Create the Entry | Choose New Entries.Enter the following details:S/4 Cmp. ID: 00001Order Type: YA01Debit/Credit: HG/L account – Chargeable: Enter Chargeable G/L Account. For example: 65008430G/L account – Non Chargeable: Enter Chargeable G/L Account. For example: 51100000Tax Code: V2Cost Center: 33101001Assignment: Enter valid Assignment: For Example: 001010110Profit Center:YB700Note If there are multiple Company IDs, repeat the same step for each Company ID.Make sure these cost center and G/L accounts are replicated prior hand.Repeat the step for the following entry.S/4 Cmp. IDOrder TypeDebit/CreditG/L account – ChargeableG/L account – Non ChargeableTax CodeCost CenterAssignmentProfit Center00001YA01S5110000051100000V210101710001010110 | The expense type is created. |  |
| 4 | Save the Entries | Choose Save. | Expense Type is saved. |  |

#### Define Plant Specific Order Types

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define the plant-specific order types.

|  |
| --- |
| Note This configuration is applicable only for single company replication. For company IDs relevant for multi-company scenarios, kindly refer to [Configure Multiple Company Replication for Maintenance Orders (Optional)](#unique_13) [page ] 13 to set up plant and order type combinations against the company IDs. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Select the Application Area as Asset Management.Select the Sub Application Area as Maintenance Management.Select the row with the item name: Integration with SAP Field Service Management.Step Name: Define Plant Specific Order Types. | The Define Plant Specific Order Types screen is displayed. |  |
| 4 | Create the Entry | Choose New Entries.Enter the Following details:S/4 Cmp. ID: 00001Order Type:YA01Planning Plant: 3310 | The plant-specific order type is created. |  |
| 5 | Save the Entries | Choose Save. | The plant-specific order type is created and saved. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Plant Specific Order Types | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: SSCUI ID - 107205 Define Plant Specific Order Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Plant Specific Order Types screen displays. |  |
| 4 | Create the Entry | Choose New Entries.Enter the Following details:S/4 Cmp. ID: 00001Order Type: YA01Planning Plant: 3310 | The plant-specific order type is created. |  |
| 5 | Save the Entries | Choose Save. | The plant-specific order type is created and saved. |  |

#### Define System Status to Filter Maintenance Order Replication

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define the System Status to filter Maintenance Order Replication.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Select the Application Area as Asset Management.Select the Sub Application Area as Maintenance Management.Select the row with the item name: Integration with SAP Field Service Management.Step Name: Define System Status to Filter Maintenance Order Replication. | The Define System Status to Filter Maintenance Order Replication screen is displayed. |  |
| 4 | Create the Entry | Choose New Entries.Enter the following details:S4 Cmp. ID: Defaulted to 00001Process Phase: 06Process Sub Phase: 0060ReplicationType: 1 (Replicate Object)Repeat the step for the following entries.Note If there are multiple Company IDs, repeat the same step for each Company ID.S4 Cmp. IDProcess PhaseProcess Sub PhaseReplicationType000010700651000010700701000010800801000010900851 | The System Status filter for Maintenance Order is created. |  |
| 5 | Save the Entries | Choose Save. | The System Status filter for Maintenance Order is saved. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define System Status to Filter Maintenance Order Replication | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: SSCUI ID - 107206 Define System Status to Filter Maintenance Order Replication.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define System Status to Filter Maintenance Order Replication screen displays. |  |
| 3 | Create the Entry | Choose New Entries.Enter the following details:S4 Cmp. ID: Defaulted to 00001Process Phase: 06Process Sub Phase: 0060ReplicationType: 1 (Replicate Object)Repeat the step for the following entries.Note If there are multiple Company IDs, repeat the same step for each Company ID.S4 Cmp. IDProcess PhaseProcess Sub PhaseReplicationType000010700651000010700701000010800801000010900851 | The System Status filter for Maintenance Order is created. |  |
| 4 | Save the Entries | Choose Save. | The System Status filter for Maintenance Order is saved. |  |

#### Configure Mapping for Priority Codelist

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you configure the mapping entries for Priority Codelist from SAP S/4HANA Cloud Public Edition to SAP FSM.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Select the Application Area as Asset Management.Select the Sub Application Area as Maintenance Management.Select the row with the item name: Integration with SAP Field Service Management.Step Name: Configure Mapping for Priority Codelist. | The Configure Mapping for Priority Codelist screen is displayed. |  |
| 4 | Create the Entry | Choose New Entries.Enter the following details:S4 Cmp. ID: 00001Order Type: YA01Priority: 1FSM Priority: HIGHDefault:Repeat the step for the following entries.Note If there are multiple Company IDs, repeat the same step for each Company ID.S4 Cmp. IDOrder TypePriorityFSM PriorityDefault00001YA012HIGH00001YA013MEDIUMX00001YA014LOW | The Mapping for Priority Code List is created. |  |
| 5 | Save the Entries | Choose Save. | The Mapping for Priority Code List is saved. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Configure Mapping for Priority Codelist | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: SSCUI ID - 107210 Configure Mapping for Priority Codelist.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Mapping for Priority Codelist screen displays. |  |
| 3 | Create the Entry | Choose New Entries.Enter the following details:S4 Cmp. ID: 00001Order Type: YA01Priority: 1FSM Priority: HIGHDefault:Repeat the step for the following entries.Note If there are multiple Company IDs, repeat the same step for each Company ID.S4 Cmp. IDOrder TypePriorityFSM PriorityDefault00001YA012HIGH00001YA013MEDIUMX00001YA014LOW | The Mapping for Priority Code List is created. |  |
| 4 | Save the Entries | Choose Save. | The Mapping for Priority Code List is saved. |  |

#### Configure Mapping for Problem Type Codelist

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you configure the mapping for the Problem Type Codelist for integration between SAP S/4HANA Cloud Public Edition and SAP FSM.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Select the Application Area as Asset Management.Select the Sub Application Area as Maintenance Management.Select the row with the item name: Integration with SAP Field Service Management.Step Name: Configure Mapping for Problem Type CodeList. | The Configure Mapping for Problem Type CodeList screen is displayed. |  |
| 4 | Create the Entry | Choose New Entries.Enter the following details:S4 Cmp. ID: 00001Order Type: YA01Activity Type: YA01Problem Type: -5Default:Repeat the step for the following entries.Note If there are multiple Company IDs, repeat the same step for each Company ID.S4 Cmp. IDOrder TypeActivity TypeProblem TypeDefault00001YA01Y02-1X00001YA01709-2 | The Mapping for Problem Type CodeList is created. |  |
| 5 | Save the Entries | Choose Save. | The Mapping for Problem Type CodeList is saved. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Configure Mapping for Problem Type CodeList | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: SSCUI ID - 107211 Configure Mapping for Problem Type CodeList.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Mapping for Problem Type CodeList screen displays. |  |
| 3 | Create the Entry | Choose New Entries.Enter the following details:S4 Cmp. ID: 00001Order Type: YA01Activity Type: YA01Problem Type: -5Default:Repeat the step for the following entries.Note If there are multiple Company IDs, repeat the same step for each Company ID.S4 Cmp. IDOrder TypeActivity TypeProblem TypeDefault00001YA01Y02-1X00001YA01709-2 | The Mapping for Problem Type CodeList is created. |  |
| 4 | Save the Entries | Choose Save. | The Mapping for Problem Type CodeList is saved. |  |

#### Configure Region

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you configure the Region for replication between SAP S/4HANA Cloud Public Edition and SAP FSM.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Select the Application Area as Asset Management.Select the Sub Application Area as Maintenance Management.Select the row with the item name: Integration with SAP Field Service Management.Step Name: Configure Region. | The Configure Region screen is displayed. |  |
| 4 | Create the Entry | Choose New Entries.Enter the following details:S4 Cmp. ID: Defaulted to 00001Region Souce Code: 1Note If there are multiple Company IDs, repeat the same step for each Company ID.You can also define different Regions based on your use cases. | The Region is created. |  |
| 5 | Save the Entries | Choose Save. | The Region is saved. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Configure Region | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: SSCUI ID - 107212 Configure Region.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Region screen displays. |  |
| 3 | Create the Entry | Choose New Entries.Enter the following details:S4 Cmp. ID: Defaulted to 00001Region Source Code: 1Note If there are multiple Company IDs, repeat the same step for each Company ID.You can also define different Regions based on your use cases. | The Region is created. |  |
| 4 | Save the Entries | Choose Save. | The Region is saved. |  |

#### Configure Mapping for Service Call Type Codelist

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define the mapping for Service Call Type Codelist for integration between SAP S/4HANA Cloud Public Edition and SAP FSM.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Select the Application Area as Asset Management.Select the Sub Application Area as Maintenance Management.Select the row with the item name: Integration with SAP Field Service Management.Step Name: Configure Mapping for Service Call Type Codelist. | The Configure Mapping for Service Call Type Codelist screen is displayed. |  |
| 4 | Create the Entry | Choose New Entries.Enter the Following details:S4 Cmp. ID: Defaulted to 00001Order Type: Defaulted to YA01Service Call Type Code List: -3Note If there are multiple Company IDs, repeat the same step for each Company ID. | The Service Call Type Codelist is created. |  |
| 5 | Save the Entries | Choose Save. | The Service Call Type Codelist is saved. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Configure Mapping for Service Call Type Codelist | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: SSCUI ID - 107213 Configure Mapping for Service Call Type Codelist.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Mapping for Service Call Type Codelist screen displays. |  |
| 3 | Create the Entry | Choose New Entries.Enter the Following details:S4 Cmp. ID: Defaulted to 00001Order Type: Defaulted to YA01Service Call Type Code List: -3Note If there are multiple Company IDs, repeat the same step for each Company ID. | The Service Call Type Codelist is created. |  |
| 4 | Save the Entries | Choose Save. | The Service Call Type Codelist is saved. |  |

#### Set Default Business Partner (Customer)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you set the Default Business Partner for the replication between SAP S/4HANA Cloud Public Edition and SAP FSM.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version.Select the Application Area as Asset Management.Select the Sub Application Area as Maintenance Management.Choose the row with the item name: Integration with SAP Field Service Management.Step Name: Default Business Partner Customer. | The Default Business Partner Customer screen is displayed. |  |
| 4 | Create the Entry | Choose New Entries.Enter the Following details:S4 Cmp. ID: Defaulted to 00001Business Partner: Any valid Business Partner replicated from SAP S/4HANA Cloud Public Edition (for example, 33100001)Note If there are multiple Company IDs, repeat the same step for each Company ID.Make sure the replication step for Business Partner is carried as specified in the setup guide. | The Default Business Partner is created. |  |
| 5 | Save the Entries | Choose Save. | The Default Business Partner is saved. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Default Business Partner Customer | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: SSCUI ID - 107215 Default Business Partner Customer.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Default Business Partner Customer screen displays. |  |
| 3 | Create the Entry | Choose New Entries.Enter the Following details:S4 Cmp. ID: Defaulted to 00001Business Partner: Any valid Business Partner replicated from SAP S/4HANA Cloud Public Edition (for example, 33100001)Note If there are multiple Company IDs, repeat the same step for each Company ID.Make sure the replication step for Business Partner is carried as specified in the setup guide. | The Default Business Partner is created. |  |
| 4 | Save the Entries | Choose Save. | The Default Business Partner is saved. |  |

#### Configure Mapping for Phase Codelist

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you configure the mappings for Phase Codelist for the replication between SAP S/4HANA Cloud Public Edition and SAP FSM.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Select the Application Area as Asset Management.Select the Sub Application Area as Maintenance Management.Select the row with the item name: Integration with SAP Field Service Management.Step Name: Configure Mapping for Phase Codelist. | The Configure Mapping for Phase Codelist screen is displayed. |  |
| 4 | Create the Entry | Choose New Entries.Enter the following details:S/4 Cmp. ID: 00001Order Type: YA01Process Phase Code: 03Process Subphase Code: 0035FSM Service Call Status Code: -2Repeat the step for the following entries.Note If there are multiple Company IDs, repeat the same step for each Company ID.S/4 Cmp. IDOrder TypeProcess Phase CodeProcess Subphase CodeFSM Service Call Status Code00001YA01060060-200001YA01070065-200001YA01070070-300001YA01080080-300002YA01090085-5 | The Mapping for Phase Codelist is created. |  |
| 5 | Save the Entries | Choose Save. | The Mapping for Phase Codelist is saved. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Configure Mapping for Phase Codelist | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: SSCUI ID - 107247 Configure Mapping for Phase Codelist.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Mapping for Phase Codelist screen displays. |  |
| 3 | Create the Entry | Choose New Entries.Enter the following details:S/4 Cmp. ID: 00001Order Type: YA01Process Phase Code: 03Process Subphase Code: 0035FSM Service Call Status Code: -2Repeat the step for the following entries.Note If there are multiple Company IDs, repeat the same step for each Company ID.S/4 Cmp. IDOrder TypeProcess Phase CodeProcess Subphase CodeFSM Service Call Status Code00001YA01060060-200001YA01070065-200001YA01070070-300001YA01080080-300001YA01090085-5 | The Mapping for Phase Codelist is created. |  |
| 4 | Save the Entries | Choose Save. | The Mapping for Phase Codelist is saved. |  |

#### Creation of Work Centre in SAP Field Service Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define the work centre in SAP Field Service Management for the replication of maintenance orders from SAP S/4HANA to SAP FSM and vice versa.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the shell environment of SAP Field Service Management launchpad as Administrator.Note For details, see the Shell section of Field Service Management product documentation on SAP Help Portal. | The SAP Field Service Management launchpad is displayed. |  |
| 2 | Select the Company | Select the Company ID that was created as a part of SAP Field Service Management Onboarding.Note For details, see the Admin and Config section of Field Service Management product documentation on SAP Help Portal. | Account is displayed based on the selection. |  |
| 3 | Select Settings and Configuration | Select Settings and Configuration. | The Settings and Configuration application page opens. |  |
| 4 | Maintain Regions | In the Service Regions section, choose the '+’ icon.Enter Region Name = WC_<Plant>_<WorkCenter> Example: WC_1010_RES-0100Enter Code = WC_<Plant>_<WorkCenter> Example: WC_1010_RES-0100Choose Save. | Region has been maintained. |  |

#### Download SAP Field Service Management Mobile Application

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you download the SAP Field Service Management Mobile Application.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Download SAP Field Service Management | The SAP Field Service Management application can be downloaded on the mobile using the link [Download Mobile App](https://help.sap.com/docs/SAP_FIELD_SERVICE_MANAGEMENT/fsm_internal_onboarding/download-mobile-app.html?state=DRAFT).It can be downloaded for IOS, Android, and Windows. | The SAP Field Service Management application can be downloaded. |  |

|  |
| --- |
| Note For details, refer the download section of Field Service Management on the [SAP Help portal](https://help.sap.com/docs/). |

## Overview Table

This process variant starts with the creation of a service order. The key characteristic is that total billed amount is calculated on the basis of time and material.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role. You can find all other (searchable) apps not included on the homepage using the search bar (2434549). If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Maintenance Notification](#unique_27) [page ] 44 | Employee - Maintenance Info | Manage Maintenance Notifications - New Version (F5777) | Maintenance Notification is created |
| [Review Maintenance Notifications](#unique_28) [page ] 45 | Employee - Maintenance Info | Manage Maintenance Notifications - New Version (F5777) | Review maintenance notification is carried out |
| [Screen Maintenance Requests](#unique_29) [page ] 46 | Maintenance Supervisor | Screen Maintenance Requests (F4072) | Review /Modify / Accept/Reject Maintenance request |
| [Create and Plan Maintenance Order](#unique_30) [page ] 48 | Maintenance Planner | Manage Maintenance Notifications and Orders (F4604) | Maintenance order is saved and is in planning phase |
| [Submit Maintenance Order for Approval](#unique_31) [page ] 51 | Maintenance Planner | Manage Maintenance Notifications and Orders (F4604) | Maintenance order is submitted for approval |
| [Approve Maintenance Order (Optional)](#unique_32) [page ] 52 | Maintenance Supervisor | My Inbox - All Items (F0862) | The maintenance order is approved and the order will be removed from the list in "My Inbox" |
| [Review and Release Maintenance Order](#unique_33) [page ] 52 | Maintenance Planner | Manage Maintenance Notifications and Orders (F4604) | Maintenance order is released for preparation |
| [Convert Purchase Requisitions to Purchase Orders](#unique_34) [page ] 53 | Purchaser | Process Purchase Requisitions (F1048A) | The purchase order is created. |
| [Submit Order for Scheduling](#unique_35) [page ] 54 | Maintenance Planner | Find Maintenance Orders - Completion (F2175) | The maintenance order is in Scheduling phase and replicated in SAP Field Service Management ( FSM) |
| [Create a new Operation in Maintenance Order (Optional)](#unique_36) [page ] 56 | Maintenance Planner | Find Maintenance Orders - Completion (F2175) | New Operation is created in the maintenance order & the same is observed FSM |
| [Update a Service Call (Optional)](#unique_37) [page ] 57 | FSM - Service Planner/Dispatcher | Planning and Dispatching | Service call is updated |
| [Update an Actvity (Optional)](#unique_38) [page ] 59 | FSM - Service Planner/Dispatcher | Planning and Dispatching | Service call is updated |
| [Dispatch Plan and Release Activity](#unique_39) [page ] 60 | FSM - Service Planner/Dispatcher | Planning and Dispatching | Service call assigned to Technician is displayed on planning board and the assignment is released |
| [Reassign Service Technician and Release Activity (Optional)](#unique_40) [page ] 61 | FSM - Service Planner/Dispatcher | Planning and Dispatching | The activity is assigned to the other technician and The assignment is released in FSM & in S4hana Maintenance order is displayed and in Execution phase, and Operations should be Ready for Execution sub-phase |
| [Create a New Activity](#unique_41) [page ] 63 | FSM - Service Planner/Dispatcher | Planning and Dispatching | New Activity is created under the Service Call and Activity assigned to Technician is displayed on planning board.The assignment is released in FSMMaintenance order is displayed in S4hana and also Newly created operation will be in Execution phase & Ready for Execution sub-phase. |
| [Duplicate an Activity](#unique_42) [page ] 65 | FSM - Service Planner/Dispatcher | Planning and Dispatching | A new activity is created for the second technician & The assignment is released |
| [Technician Starts Working on Activity](#unique_43) [page ] 66 | Service Technician - Customer Service | FSM Mobile App/ Desktop App | Technician will check assignments assigned to him and choose travel and confirm the same. |
| [Updates Time, Use Reserved Material, Add Unplanned Material, and Add Expenses](#unique_44) [page ] 67 | Service Technician - Customer Service | FSM Mobile App/ Desktop App | Time Effort will be updated, The Reserved Material is updated, The unplanned Material will be updated and Expense will be updated |
| [Manager Approves Time Effort, Expense and Material](#unique_45) [page ] 69 | FSM - Service Planner/Dispatcher | Planning and Dispatching | The Time effort/Expenses/Material added by Technician is approved. Confirmation is created automatically in maintenance order. |
| [Technically Complete a Maintenance Order in SAP S/4HANA Cloud Public Edition and Corresponding Service Call is Technically Completed in FSM](#unique_46) [page ] 70 | Maintenance Planner | Find Maintenance Orders - Completion (F2175) | The order is technically completed in SAP S/4HANA Cloud Public Edition and the status of the service is Technically Completed in FSM. |

## Test Procedures

### Create a Reactive Maintenance Order and Replicate to SAP Field Service Management

#### Create Maintenance Notification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is the Initiation phase of the maintenance process, where an employee can create a maintenance notification.

Procedure

Table 1:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Employee. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Maintenance Notifications - New Version (F5777). | The Manage Maintenance Notification screen is displayed. |  |
| 3 | Create Notification | From the List page, choose Create.A popup screen appears. Enter the following details: -Technical Object: 217100091You can search for an object in the search help by entering keywords such as 'water pump' and then choose Go.From the results, select the equipment number 217100091 and description Cooling Water Circulation Pump.Description: Detailed information regarding the maintenance notification can be updated here.Choose Create. | A detail page opens where you can provide more inputs. |  |
| 4 | Enter Details | Enter the following details:Technical Object: 233100091You can search for an object in the search help by entering some keywords such as 'water pump' and choose Go.From the results, select the equipment with number 233100091 and description Cooling Water Circulation Pump.Current Location: PlatformFailure Mode: VibrationDetection Method: InspectionEffect: Production restricted. Effect can be selected from the list available.Malfunction Start Date Time:Enter the date and the timeAdd Long Text: Answer the predefined questions. | The details are entered. |  |
| 5 | Assess Priority | Assess Priority: Select relevant consequence and likelihood for each consequence category and choose Assess Priority button. Review the details and choose Apply.Ensure that the following prerequisites are met:Ensure that the technical object is populated.Technical object master data has the maintenance plant populated in the Location Data tab. | Priority is automatically calculated and populated on the screen. |  |
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

Employees can check their existing maintenance notifications with various filter options.

Procedure

Table 2:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Employee - Maintenance Info. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Maintenance Notifications - New Version (F5777) | The app opens. |  |
| 3 | Search for Maintenance Notification Based on the Status | You can filter the list of maintenance notifications based on the subphase such as: Draft , Submitted, Action Required (returned due to insufficient information), Accepted , Rejected, and Completed.To create new maintenance notifications, choose Create button. | System retrieves a list of maintenance notifications based on the selected status. |  |
| 4 | Review Maintenance Notification | Choose the maintenance notification created in the previous step to view details and review progress. | The maintenance notification is reviewed. |  |

#### Screen Maintenance Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is the Screening phase of the maintenance process where the supervisor reviews all the open maintenance requests. Change responsibility of the requests (if required) and take appropriate decision to proceed with the request or reject the request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Supervisor. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Screen Maintenance Requests (F4072). | The app opens. |  |
| 3 | Get List of Maintenance Requests | By default, the app displays a list of maintenance requests that are open.Enter the following:Notification Type: Reactive WorkChoose GoYou can switch between the list of maintenance requests in Action Required, Accepted, Rejected, and Completed status. | List of maintenance requests is displayed based on the filter criteria. |  |
| 4 | Change Responsibility (Optional) | Select one or more open maintenance requests by selecting the checkbox. Choose Change Responsibility button.On the Change Responsibility screen, the main work center, planner group, planning plant, and person responsible can be changed.Person responsible: 50000012Main Work center: RES-0100Planning plant: 3310 | Responsibility details for the maintenance requests are changed. |  |
| 5 | Review and Modify the Maintenance Request | Choose a maintenance request which needs to be reviewed. Maintenance Request is opened and details can be seen.Choose Edit to update the information related to malfunction, responsibility, and other details. Further while reviewing the request, the supervisor can also reassess the risk and redetermine the priority of the maintenance request and if required, can manually change the final due date.Choose Save. | Maintenance request is reviewed and updated. |  |
| 6 | Accept Maintenance Request | From the top right side, you can choose Accept, Reject, or Action Required. Accept the maintenance request if all the details are correct in the request.Note If you choose Action Required, the maintenance request is sent back and will be available in Action Required tab of My Maintenance Requests app where the initiator can provide required information and resend it for screening. If you reject a maintenance request, the request will not be processed further and can be seen in the Rejected tab of My Maintenance Requests app. The reason code needs to be selected if maintenance request is rejected or sent back seeking additional information. | The maintenance request is accepted. |  |

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

Table 3:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Manage Maintenance Notifications and Orders (F4604) app. | The app opens with details. |  |
| 3 | Get List of Maintenance Notifications | Enter the following:Execution Object Type: Maintenance NotificationNotification Type: Reactive Work (Y1)Choose Go | Based on the filter criteria, a list of accepted notifications is displayed. |  |
| 4 | Create or Assign Maintenance Order | To create or assign an order, follow these steps:Select one or more maintenance notifications for which maintenance order needs to be created.Choose Create Order button on the top of the screen.Select the Maintenance Order Type: Reactive Maintenance (YA01)Choose Create.Alternatively, it is possible to assign existing maintenance order to a maintenance notification using the Assign Order button. | The maintenance order is created and is assigned to the maintenance notification.The order number is shown in Associated with under Execution Object Type section of the list view. |  |
| 5 | Plan Maintenance Order | Navigate to the Change Maintenance Order (WDA0272) app and in the Execution Object Type column, choose the maintenance order number to access the quick viewTo plan maintenance order, add details such as material, services, and labor in the Change Maintenance Order (WDA0272) app as described in steps below. | Change Maintenance order screen is opened. |  |
| 6 | Define the Operations | Go to the Operation Data tab. This selection brings you to the operation overview. Make the following entries in the Operations table.Operation : (example, 0010)Description: <Entry of your choice>Work: <Entry of your choice>Number of Capacities: <2>Stage: <Select Stage as required>The system calculates the duration of the operation based on the time you entered in the Work field and on number of resources maintained in the Number of Capacities field.Add required number of operations based on Pre, Main and Post stage. | Operations are added with Pre, Main and Post stages along with other details. |  |
| 7 | Add Stock and Non Stock Material | Select the checkbox for operation (example, 0010) and choose Materials tab at the bottom of the screen. Select the variant as Standard.For a stock material, follow these steps:Choose Select from Structure List.On the Select Material Component screen, select the stock item of item category L (for example, SP001).Note While adding material in the component tab, the valuation type of the material can be entered in the filed Batch if the material is enabled for split-valuation as mentioned in the preliminary stepChoose OK.You can also plan to return any damaged spare part back to store.Select the stock item of item category L, Quantity (eg: -1)Valuation type of the damaged material to be entered in Batch Field (eg: DAMAGED for split valuated material)If its not split valuated material,you can keep batch field blankChoose OK.For a non-stock material, enter the following:Material: NL001Item Category: Non-stock Item NQuantity: <1>Plant: 3310Purchasing Org: 3310Price: Entry of your choiceSupplier: 33300001G/L Account: 61002000Note To duplicate a material line in the list with all item data, choose Copy Material. You can then change specific fields in the copied line. | Stock and non-stock material are added to the maintenance order. |  |
| 8 | Cost Review | Go to the Costs tab.On the top of the screen, select Additional Functions > Determine CostsThe planned cost is displayed as per the cost category.The estimated costs can be updated against each cost category. | Planned and estimated costs are reviewed and updated. |  |
| 9 | Check Entries | Choose Check Entries in the upper left corner of the screen. | Entries have been checked. |  |
| 10 | Save Order | Choose Save. | The maintenance order is saved and is in Planning phase.The selected stock material is reserved automatically.Note To verify this, log on to the SAP Fiori launchpad as a Inventory Manager.Open Display Stock Overview (MMBE)Enter the stock material, plant, and storage location and choose Execute.Select storage location line under Stock Overview and choose Reservations (Menu -> Environment -> Reservations) |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Manage Maintenance Notifications and Orders (F4604) app. | The app opens. |  |
| 3 | Get List of Maintenance Orders | Enter the following:Execution Object Type: Maintenance OrderOrder Type: Reactive MaintenanceChoose Go. | A list of maintenance orders is displayed based on the filter criteria. |  |
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

This process step shows you how to approve maintenance orders from My Inbox - All Items (F0862) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comments |
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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Maintenance Notifications and Orders (F4604). | The app opens. |  |
| 3 | Review Maintenance Order | Enter the following:Execution Object: Maintenance Order Number which was approved in the previous stepChoose Go. | Maintenance order is displayed in the list view and is reviewed. |  |
| 4 | Release Maintenance Order | Select the relevant Maintenance order by the filter options selected, and then click on the Maintenance order number and choose the option Change Maintenance Order. On the next screen choose change status option, choose Release, and then save.Plan costs at the time of releasing the order will be taken as baseline cost and will be displayed in detailed cost analysis section of cost tab. Even if there is a change in plan cost later, the baseline cost remains the same and this helps to understand the deviation from plan costs. | Maintenance order is released for preparation. |  |
| 5 | Review Purchase Requisitions | When the maintenance order is released, purchase requisition is created for the non-stock material and services.Select the maintenance order. On the Maintenance Order screen that appears, go to the Operations tab.Select the row for operation (example, 0010).On the Maintenance Order Operation screen, go to the Material tab.Note the purchase requisition number for the non-stock material and services from the Purchase Requisition column. | The purchase requisitions are reviewed. |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Process Purchase Requisitions (F1048A) app. | The Process Purchase Requisitions (V2) screen is displayed. |  |
| 3 | Search for Purchase Requisitions | Enter the following:Plant: 3310Purchasing Group: 001Purchasing Organization: 3310Choose Go | A list of purchase requisitions is displayed. |  |
| 4 | Create Purchase Orders | Follow these steps:Select the purchase requisition.Choose Create Purchase Order.On New Purchase Order screen that opens, choose Purchase Order Type as the standard purchase order (NB).Choose Order. | The created purchase order is displayed in the Display Purchase Order - Advanced (ME23N) app.The purchase order is created. |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Find Maintenance Orders - Completion (F2175). | A list of orders is displayed. |  |
| 3 | Get List of Maintenance Orders | Enter the following:Technical object: 233100091Choose Go | A list of maintenance orders is displayed based on the filter criteria. |  |
| 4 | Set Order to Ready to Schedule | Select the order by selecting the checkbox.Choose Change Status > Ready to Schedule. | The maintenance order is in Scheduling phase.Maintenance order will be replicated in SAP Field Service Management. |  |
| 5 | Log on | Log on to FSM as Service Planner/Dispatcher. | The Planning and Dispatching screen is displayed. |  |
| 6 | Find Service Call | In the Dispatching dashboard search for service call via Description.Note Service External ID will be the maintenance order number. | Service call is displayed.Note If the configuration for multiple companies is maintained in the maintenance order, select an appropriate FSM Company. |  |

### Update a Released Maintenance Order in S/4HANA Public Cloud

#### Create a new Operation in Maintenance Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create an operation in a maintenance order and view the changes in SAP FSM.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Find Maintenance Orders - Scheduling (F2175) app. | A list of orders is displayed. |  |
| 3 | Get List of Maintenance Orders | Enter the following:Technical object: Maintenance Order NumberChoose Go | A list of maintenance orders is displayed based on the filter criteria. |  |
| 4 | Edit and Change Maintenace Order Header | Go to the Operation Data tab. This selection brings you to the operation overview. Make the following entries in the Operations table.Operation : (example, 0010)Description: <Entry of your choice>Work: <Entry of your choice>Number of Capacities: <2>Stage: <Select Stage as required>The system calculates the duration of the operation based on the time you entered in the Work field and on number of resources maintained in the Number of Capacities field.Add required number of operations based on Pre, Main and Post stage. |  |  |
| 5 | Log on | Log on to FSM as Service Planner/Dispatcher. | The Planning and Dispatching screen is displayed. |  |
| 6 | Find Service Call | In the Dispatching dashboard search for service call via Description.Go to the Activities tab | Service call is displayedA new FSM Service Activity should be created |  |

### Update Maintenance Order in S/4HANA Cloud When Service Call or Activity is Updated in FSM

#### Update a Service Call (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you update a service call in SAP FSM, and the corresponding maintenance order is updated in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to FSM as Service Planner/Dispatcher. | The Planning and Dispatching screen is displayed. |  |
| 2 | Find Service Call and Edit | In the Dispatching dashboard search for service call via Description.Choose the Edit button and update the following properties:SubjectPriorityResponsibleProblem TypeService Call RemarksEarliest Start/Due Date and TimeChoose Save. | Service call is updated. |  |
| 3 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 4 | Access the App | Open the Find Maintenance Orders - Completion (F2175) app. | A list of orders is displayed. |  |
| 5 | Get List of Maintenance Orders | Enter the following:Technical object: Maintenance Order NumberChoose Go.Select the maintenance order. On the Maintenance Order screen, check that the following entries are updated correctly as per the details maintained in the SAP FSM:DescriptionLong TextPriorityActivity TypeBasic Start/Final Due DatePerson Responsible | A list of maintenance orders is displayed based on the filter criteria.Updated data is displayed. |  |

#### Update an Actvity (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you update an activity in SAP FSM, and the corresponding maintenance order operation is updated in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to FSM as Service Planner/Dispatcher. | The Planning and Dispatching screen is displayed. |  |
| 2 | Find Service Call and edit an Activity | In the Dispatching dashboard search for service call via Description.Go to Activities tab. Choose an activity and click on Edit button.Update the following properties:SubjectEquipmentEstimated DurationPlannned Start & End DatesRemarksChoose Save. | Service call is updated. |  |
| 3 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 4 | Access the App | Open the Find Maintenance Orders - Completion (F2175) app. | A list of orders is displayed. |  |
| 5 | Get List of Maintenance Orders | Enter the following:Technical object: Maintenance Order NumberChoose Go.Select the maintenance order. On the Maintenance Order screen that appears:Go to the Operations tab and select the row for operation (example, 0010).On the Maintenance Order Operation screen, go to the General Information tab and verify whether the data has been replicated according to the information maintained in FSM:DescriptionLong TextDurationGo to the Planned Dates & Times and verify whether the data has been replicated according to the information maintained in FSM:Planned Start DatePlanned End Date | A list of maintenance orders is displayed based on the filter criteria.Updated data is displayed. |  |

#### Dispatch Plan and Release Activity

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you assign the activity to a service technician and release the assignment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to FSM as Service Planner/Dispatcher. | The Planning and Dispatching screen is displayed. |  |
| 2 | Find Service Call | In the Dispatching dashboard search for service call via Description. | Service call is displayed. |  |
| 3 | Assign Technician | In the planning board there are list of Technicians with specific skill set (hover over technician name to view skills).Drag and drop the service call onto the appropriate technician based on the skill set required.Note Select today’s date in planning board if not already updated. Select all the assignments relevant to service call and then assign it to specific technician. | Service call assigned to Technician is displayed on planning board. |  |
| 4 | Release assignment | On the Dispatching and Planning board, select all the assignments and choose Release Assignment. | The assignment is released. |  |
| 5 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 6 | Access the App | Open the Find Maintenance Orders - Completion (F2175) app. | A list of orders is displayed. |  |
| 7 | Review Maintenance Order | Enter the following:Execution Object: Maintenance Order NumberChoose Go.Select the maintenance order. On the Maintenance Order screen that appears, you can review and check the phase & sub-phase.Go to the Operations tab. Select the row for operation (example, 0010).On the Maintenance Order Operation screen, go to the General Information tab and verify whether the data has been replicated according to the information maintained in FSM.Check that Personnel Number is filled correctlyGo to the Planned Dates & Times and verify whether the data has been replicated according to the information maintained in FSM:Planned Start DatePlanned End Date | Maintenance order is displayed. Maintenance order should be in the Execution phase, and operations should be in the Ready for Execution sub-phase. |  |

#### Reassign Service Technician and Release Activity (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can reassign other service technician to the activity and release the assignment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to FSM as Planner/Dispatcher. | The screen Planning and Dispatching is displayed. |  |
| 2 | Find Activity | In the Dispatching dashboard, find the activity you have released by technician name. | The assigned activity is under the certain technician in the Dispatching dashboard. |  |
| 3 | Reassign Activity | In the Dispatching board, drag and drop the released activity on to the other appropriate Technician based on the skill set required. | The activity is assigned to the other technician. |  |
| 4 | Release Assignment | Select the reassigned activity, choose Release Assignment (on the upper right side of the board). | The assignment is released. |  |
| 5 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 6 | Access the App | Open the Find Maintenance Orders - Completion (F2175) app. | A list of orders is displayed. |  |
| 7 | Review Maintenance Order | Enter the following:Execution Object: Maintenance Order NumberChoose Go.Select the maintenance order. On the Maintenance Order screen that appears,You can review and check the phase & sub-phase of the maintenance order & operationsGo to the Operations tab. Select the row for operation (example, 0010).On the Maintenance Order Operation screen, go to the General Information tab and verify whether the data has been replicated according to the information maintained in FSMCheck that Personnel Number is filled correctlyGo to the Planned Dates & Times and verify whether the data has been replicated according to the information maintained in FSMPlanned Start DatePlanned End Date | Maintenance order is displayed.Maintenance order should be in the Execution phase, and operations should be Ready for Execution sub-phase. |  |

#### Create a New Activity

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a new Service Activity in FSM, which is then replicated to SAP S/4HANA Cloud Public Edition as a new operation in maintenance order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to FSM as Planner/Dispatcher. | The screen Planning and Dispatching is displayed. |  |
| 2 | Find Service Call | In the Planning & Dispatching dashboard go to Service Calls and from the list choose the relevant External Id which is your Plant Maintenance Order. | Service call is displayed. |  |
| 3 | Create a New Activity | a. In the service call screen displayed choose the Activities tab and click on Create and fill in the details as mentioned below:SubjectPlanned start datePlanned end dateNotes (for the technician)EquipmentPlanned DurationChoose Save. | A new activity is created under the service call. |  |
| 4 | Find Activity | Go to the Dispatching dashboard search for newly created activity via Description. | Newly created activity is displayed. |  |
| 5 | Assign Technician | In the Dispatching board there are list of Technicians with specific skill set. (place the cursor on technician name to know the skill set).Drag and drop the activity on to the appropriate Technician based on the skill set required.Note Select today’s date in Planning board if not already updated. Select all the assignments relevant to Service call and then assign it to specific Technician. | Activity assigned to Technician is displayed on planning board. |  |
| 6 | Release Assignment | On the Dispatching and Planning board Select all the assignments and choose Release Assignment (on the upper right side of the board). | The assignment is released. |  |
| 6 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 7 | Access the App | Open the Find Maintenance Orders - Completion (F2175) app. | A list of orders is displayed. |  |
| 8 | Review Maintenance Order | Enter the following:Execution Object: Maintenance Order NumberChoose Go.Select the maintenance order. On the Maintenance Order screen that appears,You can review and check the phase & sub-phase of the newly created operationGo to the Operations tab. Select the row for operation (example, 0010).On the Maintenance Order Operation screen, go to the General Information tab and verify whether the data has been replicated according to the information maintained in FSM.Check that Personnel Number is filled correctlyGo to the Planned Dates & Times and verify whether the data has been replicated according to the information maintained in FSM:Planned Start DatePlanned End Date | Maintenance order is displayed.Newly created operation should be in the Execution phase & Ready for Execution sub-phase. |  |

#### Duplicate an Activity

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you duplicate the activity for another service technician and release the assignment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to FSM as Planner/Dispatcher. | The screen Planning and Dispatching is displayed. |  |
| 2 | Find Activity | In the Dispatching dashboard , find the activity you have released by technician name. | The assigned activity is under the certain technician in the Dispatching dashboard. |  |
| 3 | Duplicate Activity | In the Dispatching board , select the activity and choose More on the upper right side of the pop-up window. Place your cursor onto Duplicate for and choose the other appropriate technician. | A new activity is created for the second technician. |  |
| 4 | Release Assignment | Select the new activity, choose Release Assignment (on the upper right side of the board). | The assignment is released. |  |
| 5 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 6 | Access the App | Open the Find Maintenance Orders - Completion (F2175) app. | A list of orders is displayed. |  |
| 7 | Review Maintenance Order | Enter the following:Execution Object: Maintenance Order NumberChoose Go.Select the maintenance order. On the Maintenance Order screen that appears, you can review and check the phase & sub-phase of the newly created operation.Go to the Operations tab. Select the row for operation (example, 0010).On the Maintenance Order Operation screen, go to the General Information tab and verify whether the data has been replicated according to the information maintained in FSM.Check that Personnel Number is filled correctlyGo to the Planned Dates & Times and verify whether the data has been replicated according to the information maintained in FSMPlanned Start DatePlanned End Date | Maintenance order is displayed. |  |

### Create a Completed Service Confirmation in S/4HANA Cloud when Time Effort, Material or Expense is Approved in FSM

#### Technician Starts Working on Activity

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the technician starts working on the assigned activity using the FSM mobile application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to FSM as a Service Technician - Customer Service on the mobile application. | The message Change company is displayed. |  |
| 2 | Choose Company | Choose the company you belong to, for example, Company 3. | The message Company has never been synchronized is displayed. |  |
| 3 | Sync | Choose Sync. | The screen showing all assignments for the technician is displayed. |  |
| 4 | Choose Activities | Choose the assigned Activity from the list. | The screen Service call Description, Status, Customer, Address, Responsible, Reserved material, and Assignment details are displayed. |  |
| 5 | Choose Travel | Choose Travel. | The screen Are you ready to start traveling is displayed. |  |
| 6 | Start Work | Choose Work (bottom-right). | The message I confirm is displayed. |  |
| 7 | Confirm | Choose Confirm. | The screen showing all the service details is displayed. |  |

#### Updates Time, Use Reserved Material, Add Unplanned Material, and Add Expenses

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, Technician updates time, expenses, and reserved material used.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On (Optional) | Log on to FSM as a Service Technician - Customer Service on mobile application. | The Message Change company is displayed. |  |
| 2 | Sync (Optional) | Choose the company you belong to and then choose Sync. | The screen showing all the assignments assigned to technician is displayed. |  |
| 3 | Choose Activities (Optional) | Choose assigned Activities from the list. | The screen Service call Description, Status, Customer, Address, Responsible, Reserved material, and Assignment details are displayed. |  |
| 4 | Choose Reserved Material (Optional) | Choose Reserved materials > Use > Save. | The Reserved Material is updated.Note This step is mandatory only when the service call is derived from service orders that are created with spare part to be procured, for example SRV_04. |  |
| 5 | Choose Create | Choose Create (+) at the bottom of screen. | The Screen showing Attachment, Checklist Expense, Effort, Feedback code, follow up material, and Mileage are displayed. |  |
| 6 | Choose Material | Choose Material from the list. | The Create Material screen is displayed. |  |
| 7 | Update Unplanned Material | Choose Item code, for example SP003, change Quantity if necessary, for example 2. Then choose Save.Note Please make sure the quantity in the individual stock for unplanned material in SAP S/4HANA system are enough, or it will cause error when creating confirmation. | The unplanned Material will be updated. |  |
| 8 | Choose Create | Choose Create (+) at the bottom of screen. | The Screen showing Attachment, Checklist Expense, Effort, Feedback code, follow up material and Mileage are displayed. |  |
| 9 | Choose Effort | Choose Effort from the list. | The Screen showing New Effort is displayed. |  |
| 10 | Update Effort | Choose Time Entry - Choose Working time - update working time - Choose Effort Type - choose Save. | Time Effort will be updated. |  |
| 11 | Choose Create | Choose Create (+) at the bottom of screen. | The Screen showing Attachment, Checklist Expense, Effort, Feedback code, Follow up material and Mileage are displayed. |  |
| 12 | Choose Expense | Choose Expense from the list. | The Screen showing Create Expense is displayed. |  |
| 13 | Update Expense | Choose Type -Choose Expense type - Choose Currency. Input amount in the field Internal Amount or External Amount. Choose Save. | Expense will be updated. |  |

#### Manager Approves Time Effort, Expense and Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, planner approves the time effort, expenses and material used. Plant Maintenance Confirmation is automatically created in SAP S/4HANA Cloud Public Edition once the planner approves time and expenses in FSM.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to FSM as Service Planner/Dispatcher. | The screen Planning and Dispatching is displayed. |  |
| 2 | Navigate to Time and Expenses | Choose Time and Material journal. | The screen Time effort, Expense, Material, Mileage, and Overview are displayed. |  |
| 3 | Approve Time Effort | Choose Time effort on the top of the board.Choose your service call via Description from the list of Service calls and choose Approve. | The time effort added by Technician is approved.Once Time Effort is approved in FSM, a confirmation is created automatically in Maintenance order. |  |
| 4 | Approve Expense | Choose Expense on the top of the board.Choose your service call via Description from the list of Service calls and choose Approve. | The Expense added by Technician is approved.Once Expenses are approved in FSM, the confirmation is created automatically in the Maintenance order.Note Expense confirmation does not support multiple company scenario in 2608. |  |
| 5 | Approve Material | Choose Material on the top of the board.Choose your service call via Description from the list of Service calls and choose Approve. | The Material added by Technician is approved.Once Material is approved in FSM, the confirmation is created automatically in Maintenance order. |  |
| 6 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 7 | Access the App | Open the Find Maintenance Orders - Completion (F2175) app. | A list of orders is displayed. |  |
| 8 | Review Maintenance Order | Enter the following:Execution Object: Maintenance Order NumberChoose Go.Select the maintenance order. On the Maintenance Order screen that appears,You can review and check the phase & sub-phase of the newly created operation | Maintenance order is displayed.Newly created operation should be in Execution phase & Work in Execution sub-phase. |  |
| 9 | Review Costs | Choose the Costs tab.Check the Actual Costs column. | Actual Costs for Time Efforts, Material Consumption & Expenses should be displayed. |  |
| 10 | Access the App | Open the Document Flow list app. |  |  |
| 11 | Review the Documents | Enter the Order Number & choose Execute. | All the Documents related to Time Efforts, Materials consumption & Expenses incurred are displayed. Individual documents can be viewed. |  |

### Technically Complete a Maintenance Order in SAP S/4HANA Cloud Public Edition and Corresponding Service Call is Technically Completed in FSM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you technically complete the maintenance order in SAP S/4HANA Cloud Public Edition, which automatically updates the corresponding service call to Technically Complete in FSM.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Find Maintenance Orders - Completion (F2175) app. | The app opens. |  |
| 3 | Get List of Maintenance Orders | Enter the following:Order Type: Reactive MaintenanceChoose Go. | A list of maintenance orders is displayed based on the search criteria. |  |
| 4 | Set Order Status to Technically Completed | Select the order by selecting the checkbox.Choose Change Status > Complete Technically. | The Complete Technically screen is displayed. |  |
| 5 | Enter Reference Data | Enter the following:Completion Date/Time: The default values are displayed. Use the calendar icon to change the values.Keep Default Values: Select this checkbox.Complete Assigned Notifications: Select this checkbox if you want to complete the assigned notifications.Choose Complete Technically. | The order is technically completed. |  |
| 6 | Log On | Log on to FSM as Service Planner/Dispatcher. | The Planning and Dispatching screen is displayed. |  |
| 7 | Find Service Call | In the Dispatching dashboard search for service call via Description. | Service call is displayed. The status of the Service is Technically Completed. |  |
| 8 | Find Service Call | Go to Activities tab. All the Activities are displayed. | The status of the Activities are Closed. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can proceed this process.

| Process | Business Condition |
| --- | --- |
| 3NI-Procurement for Service Management | If spare parts need to be procured outside, the preliminary steps in the 3NI should be executed. |

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
> Flagged while digesting this document, not verified: Phase codelist mapping: the Configure Your Solution table lists the last entry (phase 09/0085, status -5) under S/4 Cmp. ID 00002, while the Central Business Configuration table lists it under 00001.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/service-order-processing-with-sap-field-service-management-49x-ae-test]]
- related-to :: [[14-maintenance-service-and-projects/test-script-sap-maintenance-assistant-4rv-sap-s-4hana-cloud-public-edi]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7Z2_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 118,549 chars in the whole document
