---
id: 14-maintenance-service-and-projects/test-script-customer-project-management-project-based-services-j11-ae
title: "Test Script: Customer Project Management – Project-Based Services (J11_AE) (J11_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud 2608 test script for scope item J11_AE: customer project creation, planning, staffing, billing, review and closure (AE demo data)."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/customer-project-management]
aliases: [J11_S4CLD2608_BPD_EN_AE]
keywords: [Customer Project Management (Project-Based Services), customer project management, customer project creation, work packages, work package staffing, project billing, billing document request, service units, material master data, project review]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J11_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1296
topic: 14-maintenance-service-and-projects/customer-project-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Customer Project Management – Project-Based Services (J11_AE) (J11_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J11_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Customer Project Management (Project-Based Services)** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Customer Project Management – Project-Based Services (J11_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232862656)

[2 Prerequisites 4](#_Toc232862657)

[2.1 System Access 4](#_Toc232862658)

[2.2 Roles 4](#_Toc232862659)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232862660)

[2.4 Preliminary Steps 8](#_Toc232862661)

[2.4.1 Check Worker Details 8](#_Toc232862662)

[2.4.2 Check and Maintain Cost Rates 8](#_Toc232862663)

[2.4.3 Check Sales Price 10](#_Toc232862664)

[2.4.4 Check and Maintain Service Organizations 10](#_Toc232862665)

[2.4.5 Define Expense 12](#_Toc232862666)

[2.4.6 Map Resources to Resource Types 13](#_Toc232862667)

[2.4.7 Define Work Items and Groups 15](#_Toc232862668)

[2.4.8 Create Material Master Data 16](#_Toc232862669)

[2.4.9 Manage Situation Types (Optional) 29](#_Toc232862670)

[3 Overview Table 31](#_Toc232862671)

[4 Test Procedures 33](#_Toc232862672)

[4.1 Maintain Customer Project 33](#_Toc232862673)

[4.1.1 Create a New Customer Project 33](#_Toc232862674)

[4.1.2 Copy a Project as Basis for New Project 35](#_Toc232862675)

[4.1.3 Project Control 36](#_Toc232862676)

[4.2 Maintain Work Packages and Time-Based Planning 37](#_Toc232862677)

[4.3 Maintain Work Package Staffing (Without Scope Item 6JO: Resource Management for Projects) 43](#_Toc232862678)

[4.4 Maintain Work Package Staffing (With Scope Item 6JO: Resource Management for Projects) (Optional) 46](#_Toc232862679)

[4.5 Maintain Customer Project Billing 47](#_Toc232862680)

[4.6 Capture Service Units (Optional) 54](#_Toc232862681)

[4.7 Create Billing Document Request 55](#_Toc232862682)

[4.8 Review Customer Project 56](#_Toc232862683)

[4.9 Set Project Status (Completed) 58](#_Toc232862684)

[4.10 Close Customer Projects 59](#_Toc232862685)

[4.11 Reset Project Status to Completed (Optional) 60](#_Toc232862686)

[4.12 Situation Handling (Optional) 60](#_Toc232862687)

[5 Appendix 62](#_Toc232862688)

[5.1 Import Worker Data 62](#_Toc232862689)

[5.2 Report Project Performance 63](#_Toc232862690)

[5.3 Using Scope Item J11 in a 2-Tier Scenario 63](#_Toc232862691)

## Purpose

Overview

The Customer Project Management scope item realizes the key steps of the end-to-end process for Project Services. It integrates sales orders with project management, allowing you to create customer invoices for time and expenses – including external services – recorded against a customer project. Invoices can be generated according to various contract types or combinations. You can also derive contract values and show whether the contract margin is on plan. After the customer invoice is issued, customer payments can be monitored. During period-end closing activities, accounting and financial close activities can be performed. This scope item also supports the analysis of project profitability based on project costs and revenues.

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
| Project Manager - Professional Services | SAP_BR_PROJECT_MANAGER_PROF | Project Management – Professional Services | SAP_BR_PROJECT_MANAGER_PROF | Suggested sample user PROJECT_MANAGER_PROF representing the business role Project Manager – Professional Services. |
| Employee | SAP_BR_EMPLOYEE | Self Services / Self Services / Employee Overview Space | SAP_BR_EMPLOYEE / SAP_CA_SPT_EMPLOYEE_CROSS_PC / SAP_EAM_SPT_EMPLOYEE_PC | Suggested sample user EMPLOYEE representing the business role Employee. |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT | Suggested sample user OVERHEAD_ACCOUNTANT representing the business role Cost Accountant - Overhead. |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | Suggested sample user BPC_EXPERT representing the business role Configuration Expert - Business Process Configuration. |
| Billing Specialist - Projects | SAP_BR_PROJ_BILLG_SPCLST | Project Billing | SAP_BR_PROJ_BILLG_SPCLST | Suggested sample user PROJ_BILLG_SPCLST representing the business role Billing Specialist - Projects. |

|  |
| --- |
| Note The role template Project Manager - Commercial Services and generic role SAP_BR_PROJ_MANAGE_COMM are deprecated from CE2202 and deleted in CE2502. Use the successor role template Project Manager - Professional Services and generic role SAP_BR_PROJECT_MANAGER_PROF. For more details, refer to SAP Note [3121435](https://me.sap.com/notes/3121435). |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company are created in your system during implementation. The organizational structure reflects the structure of your company. The master data depends on the operational focus of your company and represents, for example, materials, customers, and vendors.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices package, you can use the following scenario data:

| Material | Value | Details | Comments |
| --- | --- | --- | --- |
| Service/ Delivery Organization | 3310 | Service Organization – Company AE | The service organization Service Organization – Company AE is also defined as a delivery organization. |
| Controlling Area | A000 | Controlling Area A000 | Assigned to the service organization |
| Company Code | 3310 | Company Code 3310 | Assigned to the service organization |
| Cost Center | 331019023310190333101904 | Csltg Unit A Csltg Unit B Customer Dev | Assigned to the service organization |
| Plant | 3310 | Plant 1 AE | Assigned to the service organization |
| Distribution Channel | 10 | Direct Sales | Assigned to the service organization |
| Division | 00 | Product Division 00 | Assigned to the service organization |
| Sales Organization | 3310 | Dom. Sales Org | Assigned to the service organization |
| Cost Center | Csltg Unit ACsltg Unit BCustomer Dev | 331019023310190333101904 |  |
| Profit Center | Consulting Unit AConsulting Unit BCustomer Development | YB101YB102YB103 |  |
| Customer | Domestic UAE Customer 2 | 33100002 |  |
| Activity Types | T001T002T003T004T005T006 | Junior ConsultantSenior ConsultantPlatinum ConsultantTrainerProject Manager$ Time / Fee type 6 | CO activity types are used to manage CPM roles. |
| Cost Rate | Actual and planned cost rates are maintained for the following combination of cost centers/activity types:Cost Centers: 33101902, 33101903, 33101904Activity Types: T001 - T006 |  |  |
| Pricing Condition Records | Pricing condition records are maintained for the following materials:T001 - T006 | Note Only the following key combinations are visible in the service price list:For standard prices: Material with Release StatusFor project-specific prices: Cust Proj/Material | Pricing condition records are used in the Service Price list to calculate project planned revenues.If you use other key combinations, the system can use them for pricing but you can't display or change them in the service price list. |
| Daily Availability Data | Eight working hours on DATE of INTSERVPERF1010 |  | Information about resources and their availability must be available per day for all relevant resources. If the integration with SuccessFactors Employee Central (SF EC) is in place, resource data, such as work schedule, holiday calendar, and time profile is created in SF EC during the hiring process. If the integration with SF EC has not been set up, you can use the API Manage Workforce Availability (API_MANAGE_WF_AVAILABILITY) to maintain resource data.For more information, go to [https://api.sap.com/](https://api.sap.com/) and search for the API name. |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BND | Create Customer Master - MDS |
| BNN | Create Activity Type and Activity Type Hierarchy - MDS |
| 3KW | Create CO Cost Rates - MDS |

### Preliminary Steps

#### Check Worker Details

Purpose

This process step shows you how to display and view worker (employee and contingent worker) details, including personal information, work agreements, and profiles.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Search for a Worker | Choose the Search icon on the toolbar. Select Worker from the dropdown list and search for a worker. |  |  |
| 3 | View Worker Details | Choose a worker to view the worker details. | The worker details display: personal information and work agreement details are available for detailed analysis. |  |

#### Check and Maintain Cost Rates

Purpose

This process step shows you how to check and maintain the actual and planned cost rates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Cost Rates - Services (F3161). | The Manage Cost Rates - Services screen displays. |  |
| 3 | Check Cost Rate with Selection Criteria | Make the following entries:Company Code: <company code>, for example, 3310Valid On: <current Date or start of a period> |  |  |
| 4 | Maintain Additional Cost Rates | Choose Add and make the following entries:Receiving Company Code: <receiving company code>, for example, 3310Cost Center: <cost center>, for example, 33101902Activity Type: <activity type>, for example, T002Service Cost Levels: optionalWork item ID: optionalPersonal Number: optionalWBS Element: optionalFrom FY: current yearFrom Period: current periodRate: 100Currency: <your company code currency>, for example, AEDPer: 1Activity Unit: HChoose Save.Note Maintain cost rates according to customer business requirements.Here are a few hints for you:At least one of the fields must be maintained: Activity Type, Service Cost Level, or Personnel Number.The Personnel Number and Cost Center are mutually exclusive as key fields for one price.The Personnel Number and Service Cost Level are mutually exclusive as key fields for one price.Fill in the Company Code field (to be billed) when WBS Element is filled in.Choose Save. | The Create Cost Rate(s)-Company Code, for example, 3310 dialog box displays. The new cost rates are created. |  |

#### Check Sales Price

Purpose

This process step shows you how to check the sales price.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Prices - Sales (F4111). | The Manage Prices - Sales screen displays. |  |
| 3 | Check Sales Price | Make the following entries and choose Go:Condition Type: PSP0Service Organization: 3310Sales Org.: 3310Distribution Channel: 10Product: From T001 to T005Kindly be aware that according to your business requirements, another two condition types PCP0 and SOV2 can be defined here for project-specific sales price and employee overtime sales price. | The sales prices are maintained for the five materials/roles.Project planned revenues for different roles are calculated based on these values. |  |

#### Check and Maintain Service Organizations

Purpose

This process step shows you how to check and maintain existing service organizations, and how to create new service organizations.

Prerequisites

The following organization units are assigned to the Service Organization:

- Controlling Area
- Company Code
- Sales Organization
- Distribution Channel
- Division
- Plant
- Cost Center

If you have created your own organization units, you can create new Service Organizations to be used in the project.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Service Organizations (F1421A). | The Manage Service Organizations screen displays. |  |
| 3 | Check a Service Organization | On the Manage Service Organizations screen, you can view the existing service organizations by setting the relevant filter and choosing Go. |  |  |
| 4 | Maintain a Service Organization | On the Manage Service Organizations screen, choose a service organization, go to the details screen, and choose Edit.You may change the following: Name of service organization, Organization Classification, assigned organization units, or the missing ones.Choose Save and the Back icon in the top left corner. | The service organizations display.Note When using the common divisions functionality and therefore at least two different divisions in the professional services scenario, you need to create at least two service organizations. This necessarily results in a need to separate all employees in a similar way as the used divisions, which might not be desired.It is not possible to assign a cross-country purchasing organization to a service organization. You can create a local purchasing organization and assign it to service organizations.The deletion of a service organization is not supported. |  |
| 5 | Create a New Service Organization (Optional) | On the Manage Service Organizations screen, choose Create and make the following entries:In the General Information section:ID: <By your own requirement>Name: <By your own requirement>Enable Time Posting without Staffing: <By your own requirement>Organization Classification: <Project Delivery and Resource>In the Organizational Data, Sales Area Data, and Cost Center Data sections, choose your own organization details.Choose Create.Note The app Maintain Service Organizations - Deprecated (F1421) is deprecated and will be deleted in an upcoming release. The corresponding business catalog SAP_PSP_BC_SERVICE_ORG_PC is deprecated as well and is no longer assigned to the business role template SAP_BR_PROJECT_MANAGER_PROF. For details, see [Maintain Service Organizations (Deprecated)](https://help.sap.com/docs/SAP_S4HANA_CLOUD/29cf986299714386847f4d4c9bb86994/975dec56a9eb6138e10000000a44147b.html). | The new service organization with your own organization units is created.It is only possible to assign a cost center to a service organization once. To use the newly created service organization, make sure:To maintain the cost rates for your own cost center (see section )To assign the cost center to the employees staffed on the project.Note Please assign the purchasing organization to the company code.Ensure that at least one of the purchasing organizations assigned to a plant is also defined as a standard purchasing organization.Assign the plant to the sales area (combination of sales organization, distribution channel, and division). Note that the plant field only displays the plants that are assigned to the selected sales area and purchasing organization. |  |

#### Define Expense

Purpose

This process step allows you to define expenses and map the respective cost accounts for project reporting to enable and ensure reporting on actual expenses in a project.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Access Configuration Steps | On the Manage Your Solution screen, choose Configure Your Solution.Select Professional Services from the Application Area dropdown list, and then choose the filtered line item. | The Configure Your Solution - Customer and Internal Project Management screen area displays. |  |
| 4 | Define Expenses | On the Customer and Internal Project Management screen, go to Define Expenses under configuration steps.Note For detailed steps about defining expenses and mapping the respective cost accounts for project reporting, choose the dropdown arrow of the Configure button, and select Configuration Help.The existing customization is only for demo purposes.Choose Configure.Note You can assign one or more G/L accounts to an expense type. You cannot delete a G/L account assignment if actuals are posted, but you can reassign this G/L account to a different expense type. | The Define Expenses screen displays. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Configuration Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Expenses.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Expenses screen displays. |  |

#### Map Resources to Resource Types

Purpose

This process step allows you to map various resources to appropriate resource types for professional service projects according to your requirements.

Prerequisites

Before you map expenses, you must first define them in Define Expenses the configuration step.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Access Configuration Steps | On the Manage Your Solution screen, choose Configure Your Solution.Select Professional Services from the Application Area dropdown list, and then choose the filtered line item. | The Configure Your Solution - Customer and Internal Project Management screen displays. |  |
| 4 | Map Resources to Resource Types | On the Configure Your Solution - Customer and Internal Project Management screen, navigate to Map Resources to Resource Types under configuration steps, and choose Configure.In the Select Resource Type: Overview view, you can assign resources to one of the following resource types according to your requirements:0ACT - human resources and staffing in work packages0EXP - expenses in work packages0SRV - services in work packages0ADL - additional resources that support the activities in a work packageChoose Save and Back icon in the top left corner. | Note This assignment is mandatory to enable the planning of resources in customer and internal projects.The existing customization is only for demo purposes.The deletion of resource assignments is allowed only if the resource has not been used in project planning. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Configuration Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Map Resources to Resource Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Customer and Internal Project Management screen displays. |  |
| 3 | Map Resources to Resource Types | In the Select Resource Type: Overview view, you can assign resources to one of the following resource types according to your requirements:0ACT - human resources and staffing in work packages0EXP - expenses in work packages0SRV - services in work packages0ADL - additional resources that support the activities in a work packageChoose Save and Back icon in the top left corner. | Note This assignment is mandatory to enable planning of resources in customer and internal projects.The existing customization is only for demo purpose.Deletion of resource assignments is allowed only if the resource has not been used in project planning. |  |

#### Define Work Items and Groups

Purpose

This process step allows you to define work items and group them to simplify the assignment of work items to work packages.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Access Configuration Steps | On the Manage Your Solution screen, choose Configure Your Solution.Select Professional Services from the Application Area dropdown list, and then choose the filtered line item. | The Configure Your Solution - Customer and Internal Project Management screen displays. |  |
| 4 | Define Work Items and Groups | On the Customer and Internal Project Management screen, go to Define Work Items and Groups under Configuration Steps.Note For detailed steps about defining work items and groups, choose the dropdown arrow of the Configure button, and select Configuration Help.The existing customization is only for demo purposes.Choose Configure. | The Define Work Items and Groups: Change screen displays. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Configuration Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Work Items and Groups.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Work Items and Groups: Change screen displays. |  |
| 3 | Define Work Items and Groups | Note For detailed steps about defining expenses and mapping the respective cost accounts for project reporting, choose Configuration Help.The existing customization is only for demo purposes. |  |  |

#### Create Material Master Data

Required Material Master Data

Materials need to be created with the following numbers to run the end-to-end process for project services. Create material master data with numbers A001, A002, B001, B002, P001, P002, and P003 for Basic View and Sales Views by using below parameters before testing. Materials A001, A002, B001, B002 are used for billing scenarios with payment on account and additional billing item(s). Materials P001, P002, and P003 are used when you create billing items with different types of billing contracts (Fixed Price, Time and Expense / Usage-based Item, and Periodic Services). For more information on how to create material master data, refer to Create Product Master of type "Service Product" - MDS (31X) master data script.

|  |
| --- |
| Note Business process will be blocked due to missing material master data (see SAP Note [3422688](https://me.sap.com/notes/3422688) - Unable to select billing contract type when creating project billing item). Make sure the materials are created with numbers A001, A002, B001, B002, P001, P002, P003 in productive systems before running the end-to-end process. You may use your organizational data (Plant, Sales Organization, Distribution Channel, Division, Delivery Plant) or below demo organizational data if they are available in the system. |

| Master | Value | Details |
| --- | --- | --- |
| Material Number | A001 | On account to be billed |
| Material Type | SERV | Service Product |
| Plant | 3310 | Plant 1 AE |
| Sales Organization | 3310 | Dom. Sales Org |
| Distribution Channel | 10 | Direct Sales |
| Division | 00 | Product Division 00 |
| Base Unit of Measure | AU | Activity unit |
| Delivery Plant | 3310 | Plant 1 AE |
| Material Group | A001 | On Account Billed |
| General Item Category Group | PSTE | Time and Expense Item |
| Cash Discount | X |  |
| Tax Classification | 6 | Full Tax (Services) |
| Item Category Group | PSTE | Time and Expense Item |
| Profit Center | YB101 | Consulting Unit A |
| Account Assignment Group | X6 | On Account Billed |

| Master | Value | Details |
| --- | --- | --- |
| Material Number | A002 | On account to be utilized |
| Material Type | SERV | Service Product |
| Plant | 3310 | Plant 1 AE |
| Sales Organization | 3310 | Dom. Sales Org |
| Distribution Channel | 10 | Direct Sales |
| Division | 00 | Product Division 00 |
| Base Unit of Measure | AU | Activity unit |
| Delivery Plant | 3310 | Plant 1 AE |
| Material Group | A002 | On Account Utilized |
| General Item Category Group | PSTE | Time and Expense Item |
| Cash Discount | X |  |
| Tax Classification | 6 | Full Tax (Services) |
| Item Category Group | PSTE | Time and Expense Item |
| Profit Center | YB101 | Consulting Unit A |
| Account Assignment Group | X7 | On Account Utilized |

| Master | Value | Details |
| --- | --- | --- |
| Material Number | B001 | One Time Credit |
| Material Type | SERV | Service Product |
| Plant | 3310 | Plant 1 AE |
| Sales Organization | 3310 | Dom. Sales Org |
| Distribution Channel | 10 | Direct Sales |
| Division | 00 | Product Division 00 |
| Base Unit of Measure | AU | Activity unit |
| Delivery Plant | 3310 | Plant 1 AE |
| Material Group | B001 | One Time Credit |
| General Item Category Group | PSTE | Time and Expense Item |
| Cash Discount | X |  |
| Tax Classification | 6 | Full Tax (Services) |
| Item Category Group | PSTE | Time and Expense Item |
| Profit Center | YB101 | Consulting Unit A |
| Account Assignment Group | X8 | One Time Credit |

| Master | Value | Details |
| --- | --- | --- |
| Material Number | B002 | Cloud Revenue |
| Material Type | SERV | Service Product |
| Plant | 3310 | Plant 1 AE |
| Sales Organization | 3310 | Dom. Sales Org |
| Distribution Channel | 10 | Direct Sales |
| Division | 00 | Product Division 00 |
| Base Unit of Measure | AU | Activity unit |
| Delivery Plant | 3310 | Plant 1 AE |
| Material Group | B002 | Cloud Revenue |
| General Item Category Group | PSTE | Time and Expense Item |
| Cash Discount | X |  |
| Tax Classification | 6 | Full Tax (Services) |
| Item Category Group | PSTE | Time and Expense Item |
| Profit Center | YB101 | Consulting Unit A |
| Account Assignment Group | X8 | One Time Credit |

| Master | Value | Details |
| --- | --- | --- |
| Material Number | P001 | Project-Based Service: Fixed Price |
| Material Type | SERV | Service Product |
| Plant | 3310 | Plant 1 AE |
| Sales Organization | 3310 | Dom. Sales Org |
| Distribution Channel | 10 | Direct Sales |
| Division | 00 | Product Division 00 |
| Base Unit of Measure | AU | Activity unit |
| Delivery Plant | 3310 | Plant 1 AE |
| Material Group | P000 | Contract Type |
| General Item Category Group | PSFP | Fixed Price Item |
| Cash Discount | X |  |
| Tax Classification | 6 | Full Tax (Services) |
| Item Category Group | PSFP | Fixed Price Item |
| Profit Center | YB101 | Consulting Unit A |
| Account Assignment Group | Y1 | Fixed Price |

| Master | Value | Details |
| --- | --- | --- |
| Material Number | P002 | Project-Based Service: Time & Expenses |
| Material Type | SERV | Service Product |
| Plant | 3310 | Plant 1 AE |
| Sales Organization | 3310 | Dom. Sales Org |
| Distribution Channel | 10 | Direct Sales |
| Division | 00 | Product Division 00 |
| Base Unit of Measure | AU | Activity unit |
| Delivery Plant | 3310 | Plant 1 AE |
| Material Group | P000 | Contract Type |
| General Item Category Group | PSTE | Time and Expense Item |
| Cash Discount | X |  |
| Tax Classification | 6 | Full Tax (Services) |
| Item Category Group | PSTE | Time and Expense Item |
| Profit Center | YB101 | Consulting Unit A |

| Master | Value | Details |
| --- | --- | --- |
| Material Number | P003 | Periodic Service |
| Material Type | SERV | Service Product |
| Plant | 3310 | Plant 1 AE |
| Sales Organization | 3310 | Dom. Sales Org |
| Distribution Channel | 10 | Direct Sales |
| Division | 00 | Product Division 00 |
| Base Unit of Measure | AU | Activity unit |
| Delivery Plant | 3310 | Plant 1 AE |
| Material Group | P003 | Periodic Service |
| General Item Category Group | PSTE | Time and Expense Item |
| Cash Discount | X |  |
| Tax Classification | 6 | Full Tax (Services) |
| Item Category Group | PSPS | Periodic Service |
| Profit Center | YB101 | Consulting Unit A |
| Account Assignment Group | X9 | Periodic Service |

Sample Material Master Data

You can create your own material master data for different usage by referring to below sample material master data. The existing materials are for demo purposes.

For more information on how to create material master data, refer to Create Product Master of type "Service Product" - MDS (31X) master data script.

| Master | Value | Details |
| --- | --- | --- |
| Material Number | T001 | Junior Consultant |
| Material Type | SERV | Service Product |
| Plant | 3310 | Plant 1 AE |
| Sales Organization | 3310 | Dom. Sales Org |
| Distribution Channel | 10 | Direct Sales |
| Division | 00 | Product Division 00 |
| Base Unit of Measure | H | Hours |
| Delivery Plant | 3310 | Plant 1 AE |
| Material Group | P001 | Services |
| General Item Category Group | PSTE | Time and Expense Item |
| Cash Discount | X |  |
| Tax Classification | 6 | Full Tax (Services) |
| Item Category Group | PSTE | Time and Expense Item |
| Profit Center | YB101 | Consulting Unit A |
| Account Assignment Group | X1 | SP-Time |
| Purchasing Group | 001 | Group 001 |
| Valuation Class | 3200 | Purchased Services |
| Standard Price | 1 |  |

| Master | Value | Details |
| --- | --- | --- |
| Material Number | U001 | Cloud Sales Licences |
| Material Type | SERV | Service Product |
| Plant | 3310 | Plant 1 AE |
| Sales Organization | 3310 | Dom. Sales Org |
| Distribution Channel | 10 | Direct Sales |
| Division | 00 | Product Division 00 |
| Base Unit of Measure | PC | Piece |
| Delivery Plant | 3310 | Plant 1 AE |
| Material Group | P003 | Periodic Service |
| General Item Category Group | PSTE | Time and Expense Item |
| Cash Discount | X |  |
| Tax Classification | 6 | Full Tax (Services) |
| Item Category Group | PSTE | Time and Expense Item |
| Profit Center | YB101 | Consulting Unit A |
| Account Assignment Group | XA | Revenue Cloud Sales |
| Purchasing Group | 001 | Group 001 |
| Valuation Class | 3200 | Purchased Services |
| Standard Price | 3 |  |

| Master | Value | Details |
| --- | --- | --- |
| Material Number | S001 | Service (Contractor) |
| Material Type | SERV | Service Product |
| Plant | 3310 | Plant 1 AE |
| Sales Organization | 3310 | Dom. Sales Org |
| Distribution Channel | 10 | Direct Sales |
| Division | 00 | Product Division 00 |
| Base Unit of Measure | AU | Activity unit |
| Delivery Plant | 3310 | Plant 1 AE |
| Material Group | P002 | Expenses |
| General Item Category Group | PSTE | Time and Expense Item |
| Cash Discount | X |  |
| Tax Classification | 6 | Full Tax (Services) |
| Item Category Group | PSTE | Time and Expense Item |
| Profit Center | YB101 | Consulting Unit A |
| Account Assignment Group | X2 | SP-External Services |
| Purchasing Group | 001 | Group 001 |
| Valuation Class | 3300 | General Services |
| Standard Price | 1 |  |

| Master | Value | Details |
| --- | --- | --- |
| Material Number | E001 | Accommodation |
| Material Type | SERV | Service Product |
| Plant | 3310 | Plant 1 AE |
| Sales Organization | 3310 | Dom. Sales Org |
| Distribution Channel | 10 | Direct Sales |
| Division | 00 | Product Division 00 |
| Base Unit of Measure | AU | Activity unit |
| Delivery Plant | 3310 | Plant 1 AE |
| Material Group | P002 | Expenses |
| General Item Category Group | PSTE | Time and Expense Item |
| Cash Discount | X |  |
| Tax Classification | 6 | Full Tax (Services) |
| Item Category Group | PSTE | Time and Expense Item |
| Profit Center | YB101 | Consulting Unit A |
| Account Assignment Group | X3 | SP-Disbursements |

| Master | Value | Details |
| --- | --- | --- |
| Material Number | L001 | License 001 |
| Material Type | SERV | Service Product |
| Plant | 3310 | Plant 1 AE |
| Sales Organization | 3310 | Dom. Sales Org |
| Distribution Channel | 10 | Direct Sales |
| Division | 00 | Product Division 00 |
| Base Unit of Measure | AU | Activity unit |
| Delivery Plant | 3310 | Plant 1 AE |
| Material Group | L007 | Licenses |
| General Item Category Group | PSTE | Time and Expense Item |
| Cash Discount | X |  |
| Tax Classification | 6 | Full Tax (Services) |
| Item Category Group | PSTE | Time and Expense Item |
| Profit Center | YB101 | Consulting Unit A |
| Account Assignment Group | X5 | SP-Licences |

H001 and H002 materials are used when a project needs procurement for third-party order processing. Refer to Service and Material Procurement – Project-Based Services (J13) test script for details. Create material master data H001 and H002 for Basic View and Sales Views by using below parameters before testing. For more information, refer to Create Product Master of type "Trading Good" - MDS (BNF) master data script.

| Master | Value | Details |
| --- | --- | --- |
| Material Number | H001H002 | Hardware 001Hardware 002 |
| Material Type | MAT | Material General |
| Plant | 3310 | Plant 1 AE |
| Sales Organization | 3310 | Dom. Sales Org |
| Distribution Channel | 10 | Direct Sales |
| Division | 00 | Product Division 00 |
| Base Unit of Measure | PC | Piece |
| Delivery Plant | 3310 | Plant 1 AE |
| Material Group | L001 | Trading Materials |
| General Item Category Group | PSTE | Time and Expense Item |
| Weight Unit | KG |  |
| Net Weight | 1,200 |  |
| Gross Weight | 1,400 |  |
| Tax Classification | 6 | Full Tax (Services) |
| Item Category Group | PSTE | Time and Expense Item |
| Profit Center | YB101 | Consulting Unit A |
| Transportation Group | 0001 | On Pallets |
| Valuation Class | 3100 | Trading Goods |
| Account Assignment Group | X4 | SP-Hardware |

#### Manage Situation Types (Optional)

Purpose

This process step allows you to create the situation type and execute batch runs by using the delivered situation template. You can follow the steps below to test the situation template for the use case: The project end date was reached, but the project is not set to ‘Completed’.

For more information about situation handling in Professional Services, refer to [End Date for Project Reached But Stage Not Completed](https://help.sap.com/docs/SAP_S4HANA_CLOUD/29cf986299714386847f4d4c9bb86994/e876b2eb2dd947c3a23b953d63a5aa8a.html).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Situation Types - Extended (F5437).Note This app can be started via the app search. | The Manage Situation Types – Extended screen displays. |  |
| 3 | Create a Situation Type | On the Manage Situation Types – Extended screen, search for the situation template with the ID ISPRS_PROJECT_END_REACHED.The situation template is displayed with the following name: End Date for Project Reached But Stage Not Completed.Choose the entry to navigate to the details.Choose Create Situation Type in the upper right corner of the screen.Enter the following data in the Header Information section:IDNameDescriptionSet the Status to Enabled.Enter the following data in the Batch Job Scheduling section, for example:Time Zone: CETRepeat Type: DailyRepeat Interval: 24 HrsScheduled Start Time: 00:00:00Navigate to the Situation Triggers – Batch-Based Triggers section and click on the PERIODICAL_PROJECT_STAGE_CHECK (Periodical Project Stage Check) trigger.Choose Edit in the Conditions section.Define the following filters:Processing Status: !(=40) (not equal to 40).Latest Planned Finish: =PREVIOUSMONTHChoose OK.Choose Apply to return to the main screen of the situation type.Choose Create. | The situation type is maintained. |  |
| 4 | Execute a Batch Run for the New Situation Type | On the Manage Situation Types - Extended screen, choose Trigger Batch in the upper right corner of the screen, to start the batch job.Choose Manage Instances to review the situation instances created.Note In a productive environment, the batch run for creating situation instances runs regularly according to what you have specified in the Batch Job Scheduling section. However, for this test case, it makes sense to start the batch run immediately.As stated in the dialog: It might take some time for the batch run to complete processing. Therefore, you can choose Refresh a couple of times until the batch job is finished and the instances are displayed in the list. | The batch run is executed. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Maintain Customer Project |  |  |  |
| [Create a New Customer Project](#unique_16) [page ] 33 | Project Manager - Professional Services | Project Control - Professional Services Projects (F6869) | The Project Control - Professional Services Projects screen displays. |
| [Copy a Project as Basis for New Project](#unique_17) [page ] 35 | Project Manager - Professional Services | Plan Customer Projects (F0719) | You have marked the template for the copying process. |
| [Project Control](#unique_18) [page ] 36 | Project Manager - Professional Services | Project Control - Professional Services Projects (F6869) | The Project Control – Professional Services Projects screen displays. |
| [Maintain Work Packages and Time-Based Planning](#unique_19) [page ] 37 | Project Manager - Professional Services | Project Control - Professional Services Projects (F6869) | The Project Control - Professional Services Projects screen displays. |
| [Maintain Work Package Staffing (Without Scope Item 6JO: Resource Management for Projects)](#unique_20) [page ] 43 | Project Manager - Professional Services | Project Control - Professional Services Projects (F6869) | The Project Control - Professional Services Projects screen displays. |
| [Maintain Work Package Staffing (With Scope Item 6JO: Resource Management for Projects) (Optional)](#unique_21) [page ] 46 | Refer to Scope Item 6JO. | Refer to Scope Item 6JO. |  |
| [Maintain Customer Project Billing](#unique_22) [page ] 47 | Project Manager - Professional Services | Project Control - Professional Services Projects (F6869) | The Project Control - Professional Services Projects screen displays. |
| [Capture Service Units (Optional)](#unique_23) [page ] 54 | Cost Accountant - Overhead | Manage Direct Activity Allocation - Deprecated (F3697) | The Manage Direct Activity Allocation screen displays. |
| [Create Billing Document Request](#unique_24) [page ] 55 | Project Manager - Professional Services | Manage Project Billing (F4374) | The system provides the list of billing elements of customer projects. |
| [Review Customer Project](#unique_25) [page ] 56 | Project Manager - Professional Services | Project Control - Professional Services Projects (F6869) | The system provides the list of customer projects. Only projects with status In Execution display. |
| [Set Project Status (Completed)](#unique_26) [page ] 58 | Project Manager - Professional Services | Project Control - Professional Services Projects (F6869) | The Project Control - Professional Services Projects screen displays.The projects assigned to the Customer Project Manager display. |
| [Close Customer Projects](#unique_27) [page ] 59 | Project Manager - Professional Services | Project Control - Professional Services Projects (F6869) | The Project Control - Professional Services Projects screen displays.The projects assigned to the Customer Project Manager display. |
| [Reset Project Status to Completed (Optional)](#unique_28) [page ] 60 | Project Manager - Professional Services | Project Control - Professional Services Projects (F6869) | The Project Control - Professional Services Projects screen displays.The projects assigned to the Customer Project Manager display. |
| [Situation Handling (Optional)](#unique_29) [page ] 60 | Project Manager - Professional Services |  |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Maintain Customer Project

#### Create a New Customer Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a new customer project.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Project Control - Professional Services Projects (F6869).Note You can also use the app Create Customer Projects (F0719) directly. | The Project Control - Professional Services Projects screen displays. |  |
| 3 | Maintain Customer Project Information | Under Create, select Customer Project from the dropdown list, and then you are navigated to the Create Customer Project screen.Make the following entries:Service Organization: Service Organization – Company AECost Center: Csltg Unit AProfit Center: <Consulting Unit A(YB101)>Customer: 33100002Project Name: <I-3300>Project ID: <I3300>Stage: In PlanningDuration: <Choose a date>, for example, from <today - 2 days> to <today + 4 months>Currency: AEDDescription: <SAP Implementation Project>Public Project: YESRestrict Unstaffed Posting: YESUse Project Billing (New): YESNote This switch helps decide between the billing applications:Yes - use the billing application that processes information using project billing requests (PBR) and billing document request (BDR). Subsequently, you use the app Manage Project Billing (F4374) to process project billing. It is the default setting for customers installing the SAP S/4HANA Cloud Public Edition system starting from 2502.No - use the billing application that processes information using billing proposals and debit memo requests (DMR). Subsequently, you use the Release Billing Proposals (F0780) app to manage billing for projects. The Release Billing Proposals (F0780) app is deprecated from SAP S/4HANA Cloud Public Edition2108. For customers who installed the system before SAP S/4HANA Cloud Public Edition2108, you can continue using the deprecated app to process billing documents for your existing projects. However, we recommend that you switch to the Manage Project Billing (F4374) app for all new customer projects. For more details, please refer to SAP note [3072179](https://me.sap.com/notes/3072179).Since each billing application uses different document types to process information, it is necessary to choose the billing solution for your project before you change the stage to Contract Preparation. You cannot change this selection after this stage. | The Project I-3300 is created and saved. |  |
| 4 | Maintain Project Roles | On the Create Customer Projects screen, choose Add Project Role in the top right corner of the Responsibility section, and make the following entries:Project Partner: <Business partner>Project Controller: <Business partner>Project Accountant: <Business partner>Note You can define other needed roles and assign them to the project types by SSCUI with the Define Role Types app.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |  |  |
| 5 | Save Your Entries | Choose Create. | The project is created.Note App Project Control - Professional Services Projects (F6869) provides an alternative way to access customer projects. You can view a list of projects with the details, such as general information, staffing, time recording, and billing based on your authorizations. By default, this app displays all projects that are not closed. For detailed information about the app, see [Project Control – Professional Services Projects](https://help.sap.com/docs/SAP_S4HANA_CLOUD/29cf986299714386847f4d4c9bb86994/db25b660143d4ffbad8e7f4825b9d83e.html). |  |

#### Copy a Project as Basis for New Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to make a copy of an existing customer project to create a new customer project.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Plan Customer Projects (F0719). | The Customer Project screen displays. |  |
| 3 | Filter My Projects List | In the Search field, enter project name or ID and choose Search icon.You can choose Group icon to filter by a project manager or a customer name to search for your project.You can also choose Filter icon to filter for My Favorites projects or projects with different status. | The Customer Projects section displays the filtered results. |  |
| 4 | Copy Customer Project | Select a project as template and choose Copy Project.In the Copy Project dialog box, choose Work Packages and Services, or Work Packages, Services, and Resources to define the template content.Select New Start Date checkbox and choose your proposed start date.Choose Copy. | The Create Customer Project screen with new project information displays. |  |
| 5 | Save Project | Maintain relevant information for the new project and choose Create (see [Maintain Work Packages and Time-Based Planning](#unique_19) [page ] 37). | The Customer Projects screen with new project information displays. |  |

#### Project Control

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use the app Project Control - Professional Services Projects (F6869) for projects with detailed information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Project Control - Professional Services Projects (F6869). | The Project Control – Professional Services Projects screen displays. |  |
| 3 | Display Project Details | You can view a list of projects with the details, such as general information, staffing, time recording, and billing based on your authorizations. By default, this app displays all projects that are not closed. For detailed information about the app, see [Project Control – Professional Services Projects](https://help.sap.com/docs/SAP_S4HANA_CLOUD/29cf986299714386847f4d4c9bb86994/db25b660143d4ffbad8e7f4825b9d83e.html). | The projects are listed with details. |  |

### Maintain Work Packages and Time-Based Planning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to maintain work packages and time-based planning details after creating a project.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Project Control - Professional Services Projects (F6869).Note You can also use the app Plan Customer Projects (F0719) directly. | The Project Control - Professional Services Projects screen displays. |  |
| 3 | Choose a Customer Project to Edit | You can view different projects on the Project Control - Professional Services Projects screen.You may search for your project with the Project ID.Specify I-3300 in the Project field, and choose Go. The project is listed.Choose the project, and the detailed information is displayed on the right-hand side.Choose Plan Customer Projects and navigate to the Plan Customer Projects screen. | Project I-3300 displays and is available for further editing. |  |
| 4 | Update the First Work Package | On the Plan Customer Projects screen, choose Work Packages.The first work package is proposed by default.Replace the proposed entries with the following entries and choose Save:Name: <BBP>Duration: <choose a date>, for example, from <today - 3 months> to <today + 1 month>Description: <Business Blue Print Phase>Note If the start date of the work package is earlier than the start date of the project, the start date of the project will be adjusted to the earliest start date of the work package automatically. | The new work package is updated. |  |
| 5 | Create Further Work Packages | On the current screen, to create a new work package, choose Create, and make the following entries:Name: <Realization>Duration: <choose a date>, for example, from <today - 2 months> to <today + 3 month>Description: <Realization Phase>Work Package Type: Resource Based (Time)Note You can also copy work package by choosing to include below items:Blocked FunctionsWork ItemTeamRequested ResourcesAdditional ResourcesExpensesAttachments | The Messages dialog box displays. |  |
| 6 | Create More Work Packages | Repeat previous step 5 with the following values and choose Create:Name: <Test>Duration: <choose a date>, for example, from <today – 1 month> to <today + 4 month>Description: <Test Phase>Work Package Type: Resource Based (Time)Repeat previous step 5 with the following values and choose Create:Name: <Maintenance>Duration: <choose a date>, for example, from <today - 10 days> to <today + 4 month>Description: <Maintenance>Work Package Type: Resource Based (Time)Repeat previous step 5 with the following values and choose Create:Name: <Licenses>Duration: <choose a date>, for example, from <today - 10 days> to <today + 4 month>Description: <Licenses>Work Package Type: Service Based (Unit)Unit: U001Choose Save. | The Messages dialog box displays. |  |
| 7 | Assign Work Items to the Work Package | Choose Select under Work Item for the work package you want to edit, and select P001 Documentation in Select Work Items dialog box. Choose OK and Save.Repeat this step to assign existing work items to relevant work packages.Note If needed, you can review the assigned work items by choosing Assigned. Choose Edit to modify.You can maintain Work Items and Groups by SSCUI with the Manage Your Solution app. Search Define Work Items and Groups.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. | Work Items are assigned to the work package. |  |
| 8 | Add Roles to First Work Packages | Select a Work Package to display the Details screen.Choose Add Team Role in the top right corner to add a new role.Enter the following data, and then choose Add:Work Package: <BBP>Role: Project ManagerDelivery Organization: Service Organization – Company AEWork Item: <work item>Effort (Hours): <100>Enter a new role with below information:Role: Platinum ConsultantDelivery Organization: Service Organization – Company AEWork Item:<work item>Effort (Hours): <350>You can select Billable or Non Billable from Billing Control Category dropdown list. Choose Settings to display Billing Control Category field in the table.Note Non-billable effort is not considered during the calculation of planned revenue, and not charged to the customer during the billing process.Choose Save and Back.On the Customer Project screen, under the Effort column, if you want to distribute planned package, choose the Distribute (Pencil) icon to adjust the effort in the displayed calendar dialog box.By default, total effort is distributed equally. When there is a period change of the work package, a message that informs to review effort distribution displays (by default the planned effort is kept as it is for the existing plan's period and the new plan's period is planned with 0 effort).Choose Save. | Assigned roles are listed for the work package.Planned Costs are automatically calculated from the Planned Effort.Planned Revenues are calculated based on the service price list.Note The business process Intercompany Processes – Project-Based Services (16T) is triggered if you choose a service organization with a different country/region. For more information, refer to the related test script. |  |
| 9 | Add Roles to Work Packages | Repeat the previous step 8 with the following values:Work Package: <Realization>Role: Project ManagerDelivery Organization: Service Organization – Company AEWork Item: <work item>Effort (Hours): <200>Enter a new role with below information:Role: Senior ConsultantDelivery Organization: Service Organization – Company AEWork Item:<work item>Effort (Hours): <600>Enter a new role with below information:Role: Junior ConsultantDelivery Organization: Service Organization – Company AEWork Item: <work item>Effort (Hours): <400>Repeat step 8 with the following values:Work Package: <Test>Role: Project ManagerDelivery Organization: Service Organization – Company DEWork Item: <work item>Planned Effort: <50>Enter a new role with below information:Role: Junior ConsultantDelivery Organization: Service Organization – Company DEWork Item: <work item>Effort (Hours): <300>Repeat step 8 with the following values:Work Package: <Maintenance>Role: Project ManagerDelivery Organization: Service Organization – Company DEWork Item: <work item>Planned Effort: <50>Enter a new role with below information:Role: Junior ConsultantDelivery Organization: Service Organization – Company DEWork Item: <work item>Effort (Hours): <300>Choose Save. | The assigned roles are listed for the work packages.Planned Costs are automatically calculated from the Planned Effort.Planned Revenues are calculated based on the service price list. |  |
| 10 | Specify Required Skills | Choose a work package to display the details screen.Choose Select in the Skills column for assigned roles in the Team section.Enter the required skills in the text box, such as ABAP, or SAP S/4HANA. Choose Add and OK to assign.Note A maximum of 5 skills can be assigned to each role. | The required skills for the role are defined. |  |
| 11 | Add Expense Type to the Work Package | Select a work package to display the Details screen.Choose Add Expense icon in the Expenses section on the right side of the screen.Make the following entries, then choose Save:Work Package: <BBP>Expense Type: AccommodationNote You can maintain Expense Type by SSCUI within the Manage Your Solution app. Search Define Expenses. After it is selected, choose the row to get information:Costs: <Cost>for example, <2000>Revenue: <Revenue>, for example, <2500>Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration.You can select Billable or Non Billable from Billing Control Category dropdown list. Choose Settings to display Billing Control Category field in the table.Non-billable effort is not considered during the calculation of planned revenue, and not charged to the customer during the billing process.Choose Save and Back. | Expenses are added to the work package.Planned costs and revenue are recalculated. |  |
| 12 | Add Quantity to Work Package | Choose work package Licenses and display the details screen.Enter the following data in the Service Details section, and choose Save then Back.Quantity: 15If there is any role planned for unit-based work package, the effort is non-billable by default and not charged to the customer during the billing process. You can select Billing Control Category in Settings to display it in the table. | Planned quantity is assigned to unit-based work package.The Planned Revenue is based on the Planned Service Units, and the Planned Costs are based on the role/time planning. |  |
| 13 | Select Block Functions (optional) | Select a work package to display the Details screen.There are five Blocked Functions to be selected:Activity AllocationConcur Expense PostingTime RecordingPurchasingOther Expense PostingChoose Save. |  |  |
| 14 | Attach Documents to Work Package | On the Work Package details screen, scroll down to the Attachments section.To add a new document, choose Upload. Select the document and choose Open to attach the document.To add a link, choose Add a Link and enter the URL link and description. | New documents are added as attachments to the work package and listed. |  |

### Maintain Work Package Staffing (Without Scope Item 6JO: Resource Management for Projects)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to staff work packages after roles are assigned without reference to Resource Management for Projects (6JO).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Project Control - Professional Services Projects (F6869).Note You can also use the app Plan Customer Projects (F0719) directly. | The Project Control - Professional Services Projects screen displays. |  |
| 3 | View My Projects Header Data and Choose a Customer Project to Edit | Choose Project I-3300 (created in an earlier step), choose Plan Customer Projects, and navigate to the Plan Customer Projects screen. | Project I-3300 information screen displays. |  |
| 4 | Employee Staffing – Add Employee Assignment to Role in Work Package | In the Work Packages section, choose a work package to display the Details screen.For each role, to staff an employee, choose Add Resource.Select the employee checkbox, and choose Add.Make the following entries and choose Save and Back:Work Package: <BBP>Role: Project ManagerEmployee: <employee>Work Package: RealizationRole: Project ManagerEmployee: <employee>Note A list of employees already staffed in the selected role is shown. If there are no names on the list, search for an employee as explained in the next step. | The employees are staffed for the corresponding work package. |  |
| 5 | Employee Staffing – Search for Employee | Choose a work package.On the work package detail screen, choose Add Resource beside role.In the Add Resource to Work Package dialog box, select Yes from the Include External Workers dropdown list to include external or freelance resources.Enter a role or an employee's name to search.Select the checkbox of employee and choose Add.Make the following entries and choose Save and Back:Work Package: BBPRole: Platinum ConsultantEmployee: <employee> | Searched employees are staffed. |  |
| 6 | Employee Staffing – Availability | Choose a work package.On the work package detail screen, choose Add Resource beside role.In the Add Resource to Work Package dialog box, choose See Availability to display the monthly availability of the employee.Availability is calculated monthly based on the weekly working hours of the employee.Number of working days in a month is calculated based on company code calendar of the employee.Already staffed days are deducted.Select the employee checkbox, and choose Add. Number of working days in a month is calculated based on company code calendar of the employee.Make the following entries:Work Package: RealizationRole: Junior ConsultantEmployee: <employee>Choose Save and Back. | The monthly availability of the employee displays. |  |
| 7 | Employee Staffing – View Employee Fact Sheet | Choose a work package.On the work package details screen, choose Add Resource beside role.In the Add Resource to Work Package dialog box, search for the relevant employee, choose the selected employee name, and choose Display Worker to view the worker information.Close the fact sheet in the new window, select the checkbox, and choose Add.Make the following entries:Work Package: RealizationRole: Junior ConsultantEmployee: <employee>Choose Save and Back. | The Worker screen displays employee information: cost center, contacts, employment details, service cost level, and project history are available for detailed analyses.On the Work Agreement Information screen, you may choose the Project ID to navigate to the Project Fact Sheet screen or choose Customer to navigate to the Customer Fact Sheet screen for more information. |  |
| 8 | Employee Staffing – Remove Employee Assignment to Role in Work Package | Choose a work package.On the work package detail screen, choose the Delete icon on the right screen, choose Remove the worker but leave the role to staff it later in the Remove Resource dialog box, and choose OK.Choose Save and Back icon. | The staffed employee is removed. |  |
| 9 | Employee Staffing - Team View | Choose Team to view team details. | You can use this view to add roles, staff employees, or adjust the already planned effort. |  |

### Maintain Work Package Staffing (With Scope Item 6JO: Resource Management for Projects) (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to staff work packages after roles are assigned according to Resource Management for Projects (6JO).

Procedure

Refer to Resource Management for Projects (6JO) for detailed procedures.

|  |
| --- |
| Note Once the integration with the external resource management system is activated, project manager cannot staff an employee ("Requested Resource" is for planning purposes) in the Create Customer Projects (F0719) app. Staffing assignments must be made from the external system only. |

### Maintain Customer Project Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to maintain the project billing information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Project Control - Professional Services Projects (F6869).Note You can also use the app Plan Customer Projects (F0719) directly. | The Project Control - Professional Services Projects screen displays. |  |
| 3 | Change Project Status | Choose ProjectI-3300 (created in an earlier step), choose Plan Customer Projects, and navigate to the Plan Customer Projects screen.On the Information tab, select Contract Preparation from the Stage dropdown list and choose Save. | The Billing tab is available for editing. |  |
| 4 | Create Billing Item for Fixed Price | Choose the Billing tab and make the following entries:Contract Type: Fixed PriceDescription: <Description>Assigned Work Packages: BBPProfit Center: <profit center>Amount to be billed:The amount to be billed is based on the planned revenues of the assigned work packages.For your information: The Material ID is editable on the Billing tab for all contract types as long as the sales order item is created. Different sales materials can be used in the Billing tab. If those materials belong to different categories such as maintenance and service, the profitability analyses would be impacted. P001 is used as the default material ID for fixed price. If not changed, the profit center chosen when creating a new customer project on the information level is shown as defaulted. In addition, if the profit center is changed on the information level, it will not update the ones in billing item automatically.Note To test the bundling functionality in the context of IFRS15, use material ID PIF1 and enter a value for the standalone selling price (Total SSP). For information regarding the bundling functionality in the context of IFRS15, refer to SAP note [2524569](https://me.sap.com/notes/2524569). | The Billing Item for Fixed Price is created. |  |
| 5 | Create Billing Item for Time and Expenses | To create another billing item, choose Create Billing Item.Make the following entries and press Enter.Contract Type: Time and ExpensesDescription: <Description>Assigned Work Packages: Realization, TestProfit Center: <Select profit center by your requirement>Amount to be billed:Amount Cap: <Amount Cap> If a maximum amount to be billed for time & expense projects has been agreed with the customer, it can be entered here. The field is not visible by default and it can be added using table setting button.Cap Notification Threshold: <Cap Notification Threshold> The value is related to the Cap Amount. If an alert using reporting functionality should be realized, a threshold value (which could be for example 80% of the Cap amount) can be specified here. The field is not visible by default and it can be added using table setting button.For your information: if not changed, P002 is used as the default material ID for Time and Expenses. If not changed, the profit center chosen when creating a new customer project on information level is shown as defaulted. In addition, if the profit center is changed on information level, it doesn't update the ones in billing item automatically.Note The non-billable service assigned in work packages is relevant for contract type Time and Expense and doesn't contribute to the calculation of planned revenues. | The Billing Item for Time and Expenses is created.Note There is a CDS view Engagement Project Time and Expense Billing which can be used by the project manager to monitor the cap consumption.More information can be found here:CDS View Information:Open [Engagement Project Time and Expense Billing](https://help.sap.com/viewer/DRAFT/0f69f8fb28ac4bf48d2b57b9637e81fa/latest/en-US/f94a9ee7af6a4601b0a8c0b75ff62054.html).How to Create Your Own Report and Save it as a Tile:Open [SAP S/4HANA Cloud Public Edition Help](https://help.sap.com/viewer/p/SAP_S4HANA_CLOUD) to visit Product Assistance. Choose English and navigate by: Professional Services > Customer and Internal Project Management > Plan Customer Projects > Analyze Time and Expense Billing. |  |
| 6 | Create Billing Item for Periodic Services | To create another billing item, choose Create Billing Item.Make the following entries and press Enter:Contract Type: Periodic ServiceDescription: <Description>Assigned Work Packages: MaintenanceProfit Center: <Select profit center by your requirement>Amount to be billed:For your information: if not changed, P003 is used as the default material ID for Periodic Services. In this case, the profit center is selected when creating a new customer project on information level is shown by default. Additionally, if the profit center is changed on information level, it doesn't update the ones in billing item automatically.Note To test the bundling functionality in the context of IFRS15, use material ID PIF3 and enter a value for the standalone selling price (Total SSP). | The Billing Item for Periodic Services is created.In this example, the Periodic Services item reflects the fixed maintenance fee. |  |
| 7 | Create Billing Item for Usage-based Billing | To create another billing item, choose Create Billing Item.Make the following entries and press Enter:Contract Type: Usage BasedDescription:<Description>Material ID: P002Assigned Work Packages: LicensesProfit Center: <Select profit center by your requirement>Amount to be billed:For your information: this usage-based item will be used to collect the number of licenses sold to the customer. In this scenario, Material IDP002 is used. If not changed, the profit center is selected when creating a new customer project on information level is shown by default. Additionally, if the profit center is changed on information level, it doesn't update the ones in billing item automatically.Note Kindly be aware that the P-material you have used won't appear on the invoice. Due to the design of resource-related billing, the used material is replaced by the captured service units (see [Capture Service Units (Optional)](#unique_23) [page ] 54). P004 is not available in your system, but instead, material P002 will be selected automatically. In this case, it is highly recommended to create your own sales material (for example, P004 through copying material P002) and follow the same Revenue-Recognition SSCUI instructions as stated in Event-Based Revenue Recognition – Project-Based Services (1IL) test script. | The Billing Item for Usage-based Billing is created. |  |
| 8 | Save | Choose Save.Close the message and choose Back icon. | A sales order is created without a billing plan. Work package Business Blueprint (BBP) is assigned to the Billing Item for Fixed Price; work packages Realization and Test are assigned to the Billing Item for Time and Expenses; work package Maintenance is assigned to the Billing Items for Periodic Services. Work package licenses is assigned to the Billing Items for Usage Based.Under the General, the sales order number displays. The Amount To Be Billed (Total) is the sum of the Amount to be billed for the different Contract types. This is the value of the sales order (contracted revenue) and can differ from the project planned revenues. |  |
| 9 | Create Billing Plan for Fixed Price | To create billing plan for Fixed Price, choose the billing item for Fixed Price, make the following entries, and go back:Billing Due Date: <Billing due date>, for example, <today - 8 days>Item Usage: Down Payment Request (optional, and must not be used together with Payment on Account)Amount: for example,Billing Due Date: <Billing due date>, for example, <today – 7days>Note: First billAmount:Billing Due Date: <Billing due date>, for example, <today>Note: Second billAmount:Billing Due Date: <Billing due date>, for example, today + 7 daysNote: Third billAmount: | A billing plan is created for Fixed Price.Another row is added automatically when previous row has been filled with no errors. |  |
| 10 | Create Billing Plan for Time and Expense | To create billing plan for Time and Expense, choose the billing item for Time and Expense, make the following entries, and go back:Billing Due Date: <today>Item Usage: Time and ExpensesBilling Due Date: <Billing due date>, for example, <today – 9 days>Item Usage: Down Payment Request (optional, and must not be used together with Payment on Account)Amount: for example, | A billing plan is created for Time and Expenses. |  |
| 11 | Create Another Billing Plan for Time and Expense | To create another billing plan for Time and Expense, choose the billing item for Time and Expense, make the following entries, and go back:Billing Due Date: <today>Item Usage: Time and ExpensesBilling Due Date: <Billing due date>, for example, <today – 7 days>Item Usage: Payment on Account (optional and must not be used together with down payment request)Amount: for example, | Another billing plan is created for Time and Expenses. |  |
| 12 | Create Billing Plan for Periodic Services | To create billing plan for Periodic Services, choose the billing item for Periodic Services, make the following entries, and go back:Billing Due Date: <Billing due date>, for example, todayItem Usage: Periodic ServiceAmount:Service Start Date: <Service start date>, for example, <today>Service End Date: <Service end date>, for example, <end of the current month>Billing Due Date: <Billing due date>, for example, <beginning of next month>Item Usage: Periodic ServiceAmount:Service Start Date: <Service start date>, for example, <beginning of next month>Service End Date: <Service end date>, for example, <end of next month>Go back and save.For your information: You can also use the copy function to create the billing plan.Select the billing date, select Copy, and enter the periodicity (for example, every month) and the start/end dates. | A billing plan is created for the fixed maintenance fee (Periodic Services). |  |
| 13 | Create Billing Plan for Usage-Based Billing | To create billing plan for usage-based billing, choose the billing item for Usage-based billing, make the following entries, and go back:Billing Due Date: <Billing due date>, for example, <today>Billing Due Date: <Billing due date>, for example, <today + 1 month>Go back and save. | A billing plan is created for collecting the number of licenses sold to the customer in a certain period. |  |
| 14 | Maintain Project-Specific Price per Hour for Services | Under the General section, choose Manage Prices. On the Manage Prices-Sales screen, there are some entries set by default:Editing Status: AllFilter Method: Filter with Applicable Criteria OnlyProject ID: I3300Condition Type: PCP0To create a new project-specific condition record, choose Create and enter the following entries:Condition Type: PCP0Condition Table: 4PBProduct: for example, T001Customer Project ID: I3300Valid From: <today – 2 days>Valid To: <today + 4 months>Condition Amount or Ratio: for example, 100.00 AEDPricing Unit: for example, 1 HourCalculation Type: CChoose Save.Note With managed prices, the project-specific service price can be defined and used to recalculate planned revenue based on new condition records. Condition type PCP0 is set by default for project price. Apart from 4PB, other condition tables can be chosen and used by entering the required entries. | The message Condition record displays. |  |
| 15 | Change the Project Status | On the Customer Projects screen, choose the Information view. From the Stage dropdown list, select In Execution and choose Save. | The system displays the messages:Project updatedBaseline version createdThe project is in execution phase now. A baseline version is automatically created. All the initial planned data including the cost details will be pushed to Finance ACDOCP automatically.Once the project is in execution phase, when creating a new work package without assigning a billing plan, you will get the warning message: "Please ensure that you assign the work package to a billing plan. Revenue recognition will be incomplete as long as you do not assign this to a billing item." It is recommended to assign the work package to a billing item immediately, but it can also be corrected later by performing two steps in the following order:Run repricing job of project billing, which also triggers an update to Event-Based Revenue Recognition (app Schedule Repricing for Projects (F4422)).Run realignment to repost profitability attributes (app Run Realignment - Profitability Analysis (KEND)). |  |
| 16 | Update Baseline Version (Optional) | On the Customer Projects screen, choose the Versions view, and the default view displays a comparison of work packages that are different from the baseline version. However, you can also switch the view to display all work packages.You can do the following:Update the baseline version with the current plan of one or more work packages.Synchronize key figures and values in the current project plan to enable financial reporting for projects.When you use the Update Baseline or Sync with Finance button, a copy of the information is also transferred to finance, to enable management reporting based on plan and actual data for projects. The values from the current version are transferred to the plan category CPM Ongoing (PRO02), whereas the baseline values are transferred to the plan category CPM Baseline (PRO01). Hence it is recommended to periodically update and synchronize the relevant versions. | The Version details screen displays. The baseline version can be compared with the actual version.You can always update the baseline version using Update Baseline. All the current updated planned data including the cost will be pushed to Finance ACDOCP again.During the update, only the version of those work packages that are selected will be updated. The versions of work packages that are not selected will be kept unchanged. |  |
| 17 | Confirm the Staffing (without Scope Item 6JO) | Go back and choose the Work Packages view. Choose a work package to display the staffed employees' details.Switch On the button in the Confirmed column to confirm the staffing and choose Save. | Once all Employees are successfully staffed to a work package, the Staffing Status for the work package changes to Staffed (green) or Partially Staffed (yellow). |  |

### Capture Service Units (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

This optional step shows you how to capture the usage-based services in a project as a base for billing.

The possible use cases are:

- Billing of licenses over a time period
- Billing of support tickets raised by the customer
- Billing of calls to a support hotline

The calls and tickets might be related to a maintenance contract with a base amount of support services. Services exceeding the base amount are additionally billed to the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Direct Activity Allocation (F3697A). | The Manage Direct Activity Allocation screen displays. |  |
| 3 | Capture Service Unit | On the Manage Direct Activity Allocation screen, choose Create to create a new activity allocation.Make the following entries.In the Header Information section:Journal Entry Date: <Doc. Date>, for example, <Today>Posting Date: <Posting Date>, for example, <Today>In the Allocation Items section:Note To show and maintain additional items, choose Settings and select corresponding items.Allocation Item 1:Send. Cost Center: 33101902Sender Activity Type: U001Receiver WBS element: For example, <I1000.1.4(Licenses)>Total Quantity: 10 PCAllocation Item 2:Sender Cost Center: 33101902Sender Activity Type: U002Receiver WBS element: For example, <I1000.1.4(Licenses)>Total Quantity: 5 PCChoose Create. | The document is posted, and service units (number of licenses sold to the customer in a certain period) are captured. |  |

### Create Billing Document Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a billing document request.

Prerequisites

The following Business Processes must be run before this step:

- Time Recording – Project-Based Services (J12)
- Service and Material Procurement – Project-Based Services (J13)
- Consumable Purchasing (BNX) (Optional)

Procedure

To create a billing document request, please refer to Project Billing – Project-Based Services ([4E9](https://me.sap.com/processnavigator/SolS/SolS-013/2508/SolP/4E9)).

|  |
| --- |
| Note For the fixed price, periodic services, downpayment, and payment on account billing items, the billing amount is the value of the sales order billing plan (see chapter [Maintain Customer Project Billing](#unique_22) [page ] 47).For the time and expense billing item, the billing amount is calculated based on the actual costs posted on the project. A list of service/expense items are display with costs coming from the following business processes: Time Recording – Project-Based Services (J12) and/or Service and Material Procurement – Project-Based Services (J13) and/or Consumable Purchasing (BNX).For the usage-based billing item, the billing amount is the quantity posted in the Manage Direct Activity Allocation (F3697A) app multiplied by the sales price (see section [Capture Service Units (Optional)](#unique_23) [page ] 54).For the time and expense billing item, the non-billable service will be indicated via a new column and the amount to be billed will be automatically written off for the same. This can't be changed by the project manager later. |

### Review Customer Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to analyze the customer project KPIs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Project Control - Professional Services Projects (F6869).Note You can also use the app Review Customer Projects (F1659) directly. | The Project Control - Professional Services Projects screen displays. |  |
| 3 | Check Customer Projects | Choose Project I-3300, choose Review Customer Projects, and navigate to the Review Customer Projects screen.On the Review Customer Projects screen, you can analyze the current situation of the customer project. | The Review Customer Projects screen displays with projects In Execution. |  |
| 4 | Choose a Customer Project and View Monitoring Details | Check Forecast Month for your project. If necessary, choose Set Forecast Month to set the review period to the current month, and then choose the > icon to start monitoring this project. With the setting of the forecast month, the system will plug in any variances between the plan and actual efforts from the past month to the forecast month. Also, any variances in the plan and actual expenses before the forecast month are plugged into the forecast month.On the Review Customer Projects screen, the core KPIs for project monitoring are available for detailed analyses.The analysis per work package is available; the remaining effort for Work Item and Resource and/or the remaining costs for Expense types can be updated.When saving, the PoC is being recalculated.Once the review is completed, set the Forecast Status to Completed and Save. | The core KPIs for project monitoring display. |  |
| 5 | Maintain Project Status for the Customer Project | On the Review Customer Projects screen, choose the project you want to maintain, then choose the Project Status tab.Choose Create Status. In the New Status dialog box, maintain the status and choose Save.Enter today's status for the following KPIs: Overall Status, Budget, Staffing, and Execution. | The status is maintained. |  |
| 6 | Compare Versions | On the Review Customer Project screen, select Version Folder. | The comparison between the actual version and the baseline version is available. |  |

### Set Project Status (Completed)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to set the customer project to Completed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Project Control - Professional Services Projects (F6869).Note You can also use the app Plan Customer Projects (F0719) directly. | The Project Control - Professional Services Projects screen displays. |  |
| 3 | View Projects Header Data and Choose a Customer Project to Edit | Choose Project I-3300, choose Plan Customer Projects, and navigate to the Plan Customer Projects screen. | Project I-3300 displays. |  |
| 4 | Change the Project Status | Choose Edit to manage project information. In the Information section, make the following entry and choose Save.Stage: Completed | The project stage is updated accordingly.This stage indicates that work has been completed and delivered, but financial settlements (customer/supplier invoices) are still pending. |  |

### Close Customer Projects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to close the customer project.

The following Business Processes must be run before this step:

- Event-Based Revenue Recognition – Project-Based Services ([1IL](https://me.sap.com/processnavigator/SolS/SolS-013/2508/SolP/1IL))

For example, chapter Monitor Revenue Recognition (Event-Based): Projects, Run Revenue Recognition: Projects, and other chapters based on the needs.

- Margin Analysis ([J55](https://me.sap.com/processnavigator/SolS/SolS-013/2508/SolP/J55))

For example, chapter Project Profitability Overview, Project Profitability, and other chapters based on the needs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Project Control - Professional Services Projects (F6869).Note You can also use the app Plan Customer Projects (F0719) directly. | The Project Control - Professional Services Projects screen displays. |  |
| 3 | View Projects Header Data and Choose a Customer Project to Edit | Choose Project I-3300, choose Plan Customer Projects, and navigate to the Plan Customer Projects screen. | Project I-3300 displays. |  |
| 4 | Change the Project Status | Choose Edit to manage project information. In the Information section, make the following entry and choose Save.Stage: Closed | The project stage is updated accordingly. When a project is closed, financial postings are no longer possible. |  |

### Reset Project Status to Completed (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This optional process step shows you how to set the customer project to Complete again.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Project Control - Professional Services Projects (F6869).Note You can also use the app Plan Customer Projects (F0719) directly. | The Project Control - Professional Services Projects screen displays. |  |
| 3 | View Projects Header Data and Choose a Customer Project to Edit | Choose Project I-3300, choose Plan Customer Projects, and navigate to the Plan Customer Projects screen. | Project I-3300 displays. |  |
| 4 | Change the Project Status | Choose Edit to manage project information. In the Information section, make the following entry and choose Save.Stage: Completed |  |  |

### Situation Handling (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This optional process step shows you how to check whether a situation has been created for a project and how to close it. You can follow the steps below to check the use case: The project end date was reached, but the project is not set to ‘Completed’.

Procedure

|  |
| --- |
| Note Before checking, make sure you have created a project that has an end date in the previous month (within the past 30 days). |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Check the Situation | Check either one of the following situations:On the My Home screen, choose the bell icon in the upper right corner of the screen. A notification is displayed for the project that is created together with the situation.On the My Home screen, choose the Situations tab under To-Dos. A situation is displayed for the project. | The situation displays. |  |
| 3 | Change the Project Status | On the My Home screen, choose the relevant situation tile of the project and navigate to the Situation Page. Then choose the link Project Control – Professional Services under the Related Apps section, and navigate to the Project Control - Professional Services Projects (F6869).On the right side of the Project Control – Professional Services Projects screen, choose Plan Customer Projects in the upper right corner to navigate to the Create Customer Projects (F0719) app.On the Plan Customer Projects screen, choose Edit, change the Stage to Completed, and choose Save. | The stage of the project is set to ‘Completed’. |  |
| 4 | Close the Situation | On the My Home screen, navigate to the Situations tab, and choose the situation of the corresponding project.Choose Close Situation in the upper right corner of the screen.In the Close Situation pop-up dialog, select a reason for closing the situation and choose Confirm. | The situation is closed. |  |

## Appendix

This chapter provides the procedure to import workers (employees and contingent workers).

To monitor and analyze projects, you can use the Query Browser (F1068) app to display analytical queries that are related to Customer Project Management.

The processes J11 and J14 can be a part of the two-tier scenario “Procurement of Project Services from Subsidiaries by Headquarter”, in which a headquarter can procure project services from a subsidiary. Details on this scenario can be found within Customer Guide "S4CLDXXXX_Two Tier ERP_Project Services Procurement.docx", which can be found in the folder "Procurement" of the downloaded package [https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2Tier_ERP_TechnicalContent_EN_XX.zip](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2Tier_ERP_TechnicalContent_EN_XX.zip)

### Import Worker Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Service Level Agreements (F6183A). | The Manage Workforce screen displays.The app is used to create and update workers (employees and contingent workers), including work agreements and change employment situations. |  |
| 3 | Import Worker Data | Refer to the following document to create a worker or perform mass import of worker data:[How to Import Worker Data](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0bebd08dffca45afa67b1f751199afd0/dca109e887a745e0ba61593b230e4f20.html)More details about managing workforce can be found at [Manage Workforce](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0bebd08dffca45afa67b1f751199afd0/bcbc2126696f422f844d5c631ff9cc03.html) |  |  |

### Report Project Performance

Purpose

To monitor and analyze projects, you can use the  Query Browser (F1068) app to display analytical queries that are related to Customer Project Management.

Procedure

Access the Query Browser (F1068) app and search for the queries by using the technical names given below.

Further Query Browser (F1068) app information can be found at [https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/3a24b854ee8f8d21e10000000a44176d.html](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/3a24b854ee8f8d21e10000000a44176d.html).

| Serial No # | Analytical Asset Name | Purpose | Type | Technical Name and Link to Documentation |
| --- | --- | --- | --- | --- |
| 1 | Planning, Staffing & Time Recording | Analyze customer project staffing and time recording by projects. | Multi-dimensional report | C_EngmntProjStaffingAnlysQuery[Planning, Staffing & Time Recording](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/9c2497b6557a45788a1efdc151758c75.html?locale=en-US) |
| 2 | Costs & Revenues (Plan / Actual) | Monitor actual costs and revenues for project-based services regarding ongoing plan and baseline. | Multi-dimensional report | C_EngmntProjCostQuery[Costs & Revenues (Plan / Actual)](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/ddb0b54fb9774a15a6802dd78d6e923c.html?locale=en-US) |
| 3 | Billing & Receivables | Monitor billed and overdue amounts for project-based services. | Multi-dimensional report | C_EngmntProjBillgAndRblsQry[Billing & Receivables](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/37d3c785388c4e5b906871138b86d651.html?locale=en-US) |
| 4 | Unbilled Amount | Monitor unbilled amount for project-based services. | Multi-dimensional report | C_EngmntProjUnbilledRevenueQry[Unbilled Revenue](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/726a7b7c67744ee6b6d9f153f9426348.html?locale=en-US) |
| 5 | Time and Expense Billing | Monitor the percentage of Time & Expense billing, and whether it has reached the threshold. | Multi-dimensional report | C_EngmntProjTmeExpnBillgQ[Time and Expense Billing](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/f94a9ee7af6a4601b0a8c0b75ff62054.html?locale=en-US) |
| 6 | Estimate at Completion Costs and Percentage of Completion | Monitor estimate at completion costs and percentage of completion. | Multi-dimensional report | C_EngmntProjFcstQuery_2[Estimated at Completion and Percentage of Completion](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/f32f4360f8274f6e83c660a520020007.html?locale=en-US) |

### Using Scope Item J11 in a 2-Tier Scenario

The Customer Project Management – Project-Based Services (J11) and Sales Order Processing – Project-Based Services (J14) scope items can be a part of the two-tier scenario Procurement of Project Services from Subsidiaries by Headquarter, in which a headquarter can procure project services from a subsidiary.

Details on this scenario can be found within Customer Guide "S4CLDXXXX_Two Tier ERP_Project Services Procurement.docx", which can be found in the folder "Procurement" of the downloaded package [https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2Tier_ERP_TechnicalContent_EN_XX.zip](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2Tier_ERP_TechnicalContent_EN_XX.zip)

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
- related-to :: [[10-procurement/test-script-service-and-material-procurement-project-based-services-j1]]
- related-to :: [[14-maintenance-service-and-projects/test-script-time-recording-project-based-services-j12-ae-1297]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J11_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 106,731 chars in the whole document
