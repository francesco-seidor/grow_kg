---
id: 14-maintenance-service-and-projects/internal-project-management-project-based-services-1a8-ae-test-script
title: "Internal Project Management – Project-Based Services (1A8_AE) – Test Script, SAP S/4HANA Cloud Public Edition 2608 (1A8_S4CLD2608_BPD_EN_AE)"
description: "SAP Best Practices test script for scope item 1A8_AE: create, plan, staff, settle, complete and close internal projects in S/4HANA Cloud Public Edition 2608."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/internal-and-collaborative-projects]
aliases: [1A8_S4CLD2608_BPD_EN_AE]
keywords: [Internal and Collaborative Project Management, internal project management, internal project creation, work packages, settlement rules, work package staffing, project stage status, project settlement, project closing, situation handling]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1A8_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-708
topic: 14-maintenance-service-and-projects/internal-and-collaborative-projects
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Internal Project Management – Project-Based Services (1A8_AE) – Test Script, SAP S/4HANA Cloud Public Edition 2608 (1A8_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1A8_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Internal and Collaborative Project Management** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Internal Project Management – Project-Based Services (1A8_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Internal Project Management – Project-Based Services (1A8_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232846497)

[2 Prerequisites 4](#_Toc232846498)

[2.1 System Access 4](#_Toc232846499)

[2.2 Roles 4](#_Toc232846500)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232846501)

[2.4 Preliminary Steps 7](#_Toc232846502)

[2.4.1 Check Worker Details 7](#_Toc232846503)

[2.4.2 Check and Maintain Cost Rates 7](#_Toc232846504)

[2.4.3 Check and Maintain Service Organizations 9](#_Toc232846505)

[2.4.4 Define Expense 10](#_Toc232846506)

[2.4.5 Map Resources to Resource Types 12](#_Toc232846507)

[2.4.6 Define Work Items and Groups 13](#_Toc232846508)

[2.4.7 Create Material Master Data 15](#_Toc232846509)

[2.4.8 Manage Situation Types (Optional) 21](#_Toc232846510)

[3 Overview Table 23](#_Toc232846511)

[4 Test Procedures 25](#_Toc232846512)

[4.1 Maintain Internal Project 25](#_Toc232846513)

[4.1.1 Create a New Internal Project 25](#_Toc232846514)

[4.1.2 Project Control 28](#_Toc232846515)

[4.2 Maintain Work Packages and Time-Based Planning 29](#_Toc232846516)

[4.3 Maintain Settlement Rules 33](#_Toc232846517)

[4.4 Maintain Work Package Staffing (Without Scope Item 6JO: Resource Management for Projects) 34](#_Toc232846518)

[4.5 Maintain Work Package Staffing (With Scope Item 6JO: Resource Management for Projects) (Optional) 36](#_Toc232846519)

[4.6 Change the project Status (In Execution) and Confirmation of the staffing 37](#_Toc232846520)

[4.7 Project-Level Mass Editing Functionality 38](#_Toc232846521)

[4.8 Run Settlement 40](#_Toc232846522)

[4.9 Set Project Status (Completed) 41](#_Toc232846523)

[4.10 Close Internal Projects 42](#_Toc232846524)

[4.11 Reset Project Status to Completed (Optional) 43](#_Toc232846525)

[4.12 Situation Handling (Optional) 44](#_Toc232846526)

[5 Appendix 46](#_Toc232846527)

[5.1 Import Worker Data 46](#_Toc232846528)

## Purpose

Overview

Internal Project Management manages the complete end-to-end process of project-based services inside the company. This scope item realizes the main steps of the end-to-end scenario for Project-Based Services focusing on internal project management and costs. It integrates project planning and staffing with core project management functionalities, procurement processes for materials and services, and time recording against the project work items. During period-end closing activities, accounting and financial close activities can be performed. This scope item also supports the analysis of project key figures.

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

|  |
| --- |
| Note The role template Project Manager - Commercial Services and generic role SAP_BR_PROJ_MANAGE_COMM are deprecated from CE2202 and deleted in CE2502. Use the successor role template Project Manager - Professional Services and generic role SAP_BR_PROJECT_MANAGER_PROF. For more details, refer to SAP Note [3121435](https://me.sap.com/notes/3121435). |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company are created in your system during implementation. The organizational structure reflects the structure of your company. The master data depends on the operational focus of your company and represents, for example, materials, customers, and vendors.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices package, you can use the following scenario data:

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Service Organization / Delivery Organization | Service Organization – Company AE | The following Enterprise Structures are assigned to the Service Organization:Controlling Area A000Company Code 3310Cost Center 33101902, 33101903, 33101904Plant 1 AEDistribution Channel 10Division 00Sales Organization 3310 | The service organization Service Organization – Company AE is also defined as a delivery organization. |
| Cost Center | Csltg Unit A, Csltg Unit B, Customer Dev | 33101902, 33101903, 33101904 |  |
| Activity Types | T001 Junior ConsultantT002 Senior ConsultantT003 Platinum ConsultantT004 TrainerT005 Project ManagerT006 $ Time / Fee type 6T007 $ Time / Fee type 7T008 $ Time / Fee type 8T009 $ Time / Fee type 9T010 $ Time / Fee type 10T011 $ Time / Fee type 11T012 $ Time / Fee type 12T013 $ Time / Fee type 13T014 $ Time / Fee type 14T015 $ Time / Fee type 15 |  | CO Activity Types are used to manage CPM Roles |
| Cost Rate | Actual and planned cost rates are maintained for the following combination of cost centers / activity types:Cost centers: 33101902, 33101903, 33101904Activity types: T001 - T015 |  |  |
| Daily Availability Data | Eight working hours on DATE of INTSERVPERF1010 |  | Information about resources and their availability must be available per day for all relevant resources. If the integration with SuccessFactors Employee Central (SF EC) is in place, resource data, such as work schedule, holiday calendar, and time profile is created in SF EC during the hiring process. If the integration with SF EC has not been set up, you can use the API Manage Workforce Availability (API_MANAGE_WF_AVAILABILITY) to maintain resource data. For more information, go to [link](https://api.sap.com/) and search for the API name. |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNN | Create Activity Type and Activity Type Hierarchy - MDS |

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

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check and maintain the actual and planned cost rates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Cost Rates - Services (F3161). | The Manage Service Cost Rates screen displays. |  |
| 3 | Check Cost Rate with Selection Criteria | Make the following entries:Company Code:<Company for which you want to enter rates>Valid On: <Current Date or start of a period> |  |  |
| 4 | Maintain Additional Cost Rates | Select Add. | Pop-up of create cost rate(s)-company code, for example, 3310 |  |
| 5 | Enter Cost Rates | Make the following entries:Company Code: <Company for which you want to enter rates>Cost Center: for example, 33101902Activity Type: for example, T002Service Cost Levels: optionalWork item ID: optionalPersonal Number: optionalWBS Element: optionalFrom Fiscal Year: Current YearFrom Period: Current PeriodVariable Amount: for example, <100>Currency: for example, your company code currency AEDPer: 1Activity Unit: for example, <H> | Cost rates have to be as per customer business requirements.This step uses content sample master data.Some hints:At least one of the fields: Activity Type, Service Cost Levels, or Personnel Number must be filled.Personnel Number and Cost Center exclude each other as key fields for one price.Personnel Number and Service Cost Levels exclude each other as key fields for one price.Company Code to be billed shall be filled when WBS Element is filled. |  |
| 6 | Save | Choose Save. | Additional cost rates are created. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Access Configuration Steps | On the Manage Your Solution screen, choose Configure Your Solution.Use Adapt Filters to choose Professional Services under Application Area, then choose Go. | The Configure Your Solution - Customer and Internal Project Management screen displays. |  |
| 4 | Map Resources to Resource Types | On the Configure Your Solution - Customer and Internal Project Management screen, choose Map Resources to Resource Types under configuration steps.In the Select Resource Type: Overview view, you can assign resources to one of the following resource types according to your requirements:0ACT - human resources and staffing in work packages0EXP - expenses in work packages0SRV - services in work packages0ADL - additional resources that support the activities in a work packageChoose Save and the Back icon in the top left corner. | Note This assignment is mandatory to enable the planning of the resources in customer and internal projects.The existing customization is only for demo purposes.The deletion of resource assignments is allowed only if the resource has not been used in project planning. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Configuration Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Map Resources to Resource Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Map Resources to Resource Types | In the Select Resource Type: Overview view, you can assign resources to one of the following resource types according to your requirements:0ACT - human resources and staffing in work packages0EXP - expenses in work packages0SRV - services in work packages0ADL - additional resources that support the activities in a work packageChoose Save and the Back icon in the top left corner. | Note This assignment is mandatory to enable planning of resources in customer and internal projects.The existing customization is only for demo purposes.Deletion of resource assignments is allowed only if the resource has not been used in project planning. |  |

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

Internal Projects

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Maintain Internal Project |  |  |  |
| [Create a New Internal Project](#unique_15) [page ] 25 | Project Manager - Professional Services | Project Control - Professional Services Projects (F6869) | The Project Control - Professional Services Projects app displays. |
| [Project Control](#unique_16) [page ] 28 | Project Manager - Professional Services | Project Control - Professional Services Projects (F6869) | The Project Control - Professional Services Projects app displays. |
| [Maintain Work Packages and Time-Based Planning](#unique_17) [page ] 29 | Project Manager - Professional Services | Project Control - Professional Services Projects (F6869) | The Project Control - Professional Services Projects screen displays. |
| [Maintain Settlement Rules](#unique_18) [page ] 33 | Project Manager - Professional Services | Project Control - Professional Services Projects (F6869) | The Project Control - Professional Services Projects screen displays. |
| [Maintain Work Package Staffing (Without Scope Item 6JO: Resource Management for Projects)](#unique_19) [page ] 34 | Project Manager - Professional Services | Project Control - Professional Services Projects (F6869) | The Project Control - Professional Services Projects screen displays. |
| [Maintain Work Package Staffing (With Scope Item 6JO: Resource Management for Projects) (Optional)](#unique_20) [page ] 36 | Refer to Scope Item 6JO. | Refer to Scope Item 6JO. |  |
| [Change the project Status (In Execution) and Confirmation of the staffing](#unique_21) [page ] 37 | Project Manager - Professional Services | Project Control - Professional Services Projects (F6869) | The Project Control - Professional Services Projects screen displays. |
| [Project-Level Mass Editing Functionality](#unique_22) [page ] 38 | Project Manager - Professional Services | Manage Projects - Professional Services Projects (F8336) | The Manage Projects - Professional Services Projects screen displays. |
| [Run Settlement](#unique_23) [page ] 40 | Cost Accountant - Overhead |  |  |
| [Set Project Status (Completed)](#unique_24) [page ] 41 | Project Manager - Professional Services | Project Control - Professional Services Projects (F6869) | The Project Control - Professional Services Projects screen displays. |
| [Close Internal Projects](#unique_25) [page ] 42 | Project Manager - Professional Services | Project Control - Professional Services Projects (F6869) | The Project Control - Professional Services Projects screen displays. |
| [Reset Project Status to Completed (Optional)](#unique_26) [page ] 43 | Project Manager - Professional Services | Project Control - Professional Services Projects (F6869) | The Project Control - Professional Services Projects screen displays. |
| [Situation Handling (Optional)](#unique_27) [page ] 44 | Project Manager - Professional Services |  |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Maintain Internal Project

#### Create a New Internal Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a new internal project.

|  |
| --- |
| Note It is recommended to create internal projects using the Project Control - Professional Services Projects/Manage Projects - Professional Services Projects. If the projects are created using Plan internal projects app please follow the steps in the link - [https://help.sap.com/docs/s4hana-best-practices/internal-project-management-project-based-services-1a8-de-3f6a6e75177778b4acbf6f2f100a0cdb/purpose?state=DRAFT&version=2602](https://help.sap.com/docs/s4hana-best-practices/internal-project-management-project-based-services-1a8-de-3f6a6e75177778b4acbf6f2f100a0cdb/purpose?state=DRAFT&version=2602) |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Project Control - Professional Services Projects (F6869).Note You can also use the app Manage Projects - Professional Services Projects (F8336) directly. Once navigated to the manage projects – Professional Services screen, click on create button and choose the project type as Internal Project.The Plan Internal Projects - Old Version (F1656) will be deprecated going forward. The tentative timeline is 2708 release. | The Project Control - Professional Services Projects screen displays. |  |
| 3 | Maintain Internal Project Information | Under Create, select Internal Project (New) from the dropdown list, and then you are navigated to the Create Internal Project screen.Make the following entries:Description : This is a test project that has been created for a duration of 4 monthsProject: Your name, for example INT1000.Note Project is only alphanumericProject Name: Test ProjectStage: is set to do In Planning by defaultStart Date: today (Auto Populated)End Date: Enter the value today + 4 monthsDescription: The project is an internal test project.Service Organization: Service Organization – Company AE (Auto Populated)Cost Center: Csltg Unit A (Auto Populated)Profit Center: Consulting Unit A (YB101) (Auto Populated)Currency: AED - UAE DirhamProject Type: Internal project is set by default.In the settings tab Choose the following as per your requirementPrivate ProjectNote Private project: Project will be visible only to Roles/ Persons tagged to the project in the responsibility section.Enable time posting without staffing: Check/Uncheck based on the staffing requirementNote If the Enable Time Posting without Staffing checkbox is not enabled, the time recording can only be performed by the employee who has been assigned to this project.If the checkbox is enabled, the time recording can be performed by an employee whether he or she has been assigned to this project or not. | The default project ID can be replaced with a project specific ID. |  |
| 4 | Maintain Project Roles/Responsibilities | On the Responsibilities tab, choose Create and make the following entries in the Project Roles field:Project Partner: <Business partner>Project Controller: <Business partner>Project Accountant: <Business partner>Note You can define other needed roles and assign them to the project types by SSCUI with the Define Role Types app. By default the Project Manager role is added and it cannot be deleted. The corresponding worker can be assigned.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |  |  |
| 5 | Save Your Entries - Draft version | Once the above details are filled and if we click on the back arrow without creating a project,a warning pop-up comes with the following options.CreateKeep DraftDiscard Draft.If the create button is clicked, the project is created. If the Keep Draft button is clicked, the project will be saved in draft version, which can be later modified via the Manage Project – Professional Services app, and the icon will appear that the project is in draft state. If the discard button is clicked, the project will not be saved. |  |  |
| 6 | Save Your Entries | Choose Create. If the project is not required to be created, click on discard draft.Note When each action is performed on the screen, the draft version is updated which can be viewed in Manage Projects Professional Services app. | Project is created and saved.Note App Manage Projects - Professional Services Projects (F8336) provides an alternative way to access internal projects. You can view a list of projects with the details, such as general information, staffing, and time recording based on your authorizations. By default, this app displays all projects that are not closed. For detailed information about the app, see [Manage Projects – Professional Services Projects](https://help.sap.com/docs/SAP_S4HANA_CLOUD/29cf986299714386847f4d4c9bb86994/47ca6aee5bc042d1862abe57a5f92918.html). |  |

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

This process step shows you how to update the project with work packages and time-based planning information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Projects - Professional Services Projects (F8336).Note Draft versions of projects are available in Manage Projects - Professional Services Projects (F8336). | The Manage Project Control - Professional Services screen displays. |  |
| 3 | Choose an Internal Project to Edit | You can view different projects on the Manage Projects – Professional Services screen.Use the drop down and change the Editing Status as "All".You may search for your project with the Project ID.Specify INT3300 in the Project field, and choose Go. The project is listed.Choose the project, and the detailed information is displayed on the right-hand side.Click on edit and make the necessary changes, if any.Once changes are made, click on the save button. | Project INT3300 is available for further editing. |  |
| 4 | Creation of work packages | Choose Manage Work Packages (F8337) on the top right corner and navigate to the Manage Work Packages screen.Note Manage work packages app (F8337) is accessible only if a project is created.Click on edit.Click on Create Resource Based Work Package.Enter the following entries:Work package name: WP1Start Date: todayEnd Date: today + 1 monthWhen there is a change in the dates (either the start date ahead of the project start date or the end date after the project end date) of the work package, the distribution type is allowed to be changed. It is enabled with two options:Retain Planned efforts and quantitiesRetain Planned efforts and quantities for overlapping monthChoose the distribution type accordingly and save the entries. | The new work package is updated and displayed on the details screen. |  |
| 5 | Save Your Entries – Draft version | Once the above details are filled and if we click on the back arrow without creating a work package, a warning pop-up comes with the following options:SaveKeep DraftDiscard Draft.If the save button is clicked, the work package is created. If the Keep Draft button is clicked, the work package will be saved in draft version. If the discard button is clicked, the work package will not be saved. |  |  |
| 6 | Delete work packages | To delete a work package, choose the work package which needs to be deleted and click on the delete icon.Confirm the deletion on the pop-up.Save the entries. | The work package is deleted and the project is saved.Note The deletion of work package is not possible when the actuals are posted for a resource or to the WBS element. |  |
| 7 | Create Further Work Packages | To create a new work package, repeat step 4.Make the following entries and choose OK:Name: WP2Start Date: today + 1 monthEnd Date: today + 4 monthsSave the entries.Repeat this step to create multiple work packages. | The message Work Package update successful displays. |  |
| 8 | Add Description to the work package | To add the description to the work package, choose the work package and click on edit. Navigate to the information tab.Enter the description for the work package. Click on apply and save the entries. | The description of the work package is updated. |  |
| 9 | Assign work items to the work package | To assign work items to an existing work package, choose the work package. Click on edit and navigate to the work items tab.There are two options:Assign Standard Work ItemCreate User Defined Work ItemClick on Assign Standard Work Item / Create User Defined Work Item based on the requirement.Note If Assign Standard Work Item is selected, select P001 (Documentation) or whichever is applicable as per the requirement.If Create User Defined Work Item is selected by default the work item name is updated as USR1 and the value changes to USR2/USR3 based on the user defined work items created. In addition, you can enter a description in the work item name.Choose Apply at the bottom right of the screen and save the entries.Repeat this step to assign work items to the relevant work packages.In order to delete a work item, select the work item and click on the delete button. | You can review the assigned work items by selecting Assigned. A dialog box appears. Choose Edit to add additional work items. |  |
| 10 | Add Teams/Roles to the Work Package | Select the work package to display the Details screen. Click on Edit and navigate to the Teams tab.Choose Create in the top right corner to add a new role. Click on show more per row.Enter the following data:Role: Project ManagerWork Item: Enter the value which was assigned to the work package.Delivery Organization: Service Organization - Company DEEffort (Planned): 100Role: Senior ConsultantWork Item: Select the value which was assigned to the work item (from the previous step) in the work package.Delivery Organization: Service Organization – Company DEEffort (Planned): 350Choose Apply and go back.Click on save.Repeat this step to assign roles/team to the other work packages. | Assigned roles are listed for the work package.Planned costs are automatically calculated from the planned effort.Planned revenues are calculated based on the Service Price List.Note The business process Intercompany Processes – Project-Based Services (16T) is triggered if you choose a service organization with a different country/region. For more information, refer to the related test script. |  |
| 11 | Add Additional Resources to the work packages | Select the work package to display the Details screen. Click on Edit and navigate to the Additional Resources tab.Choose Create in the top right corner to add additional resources and select show more per row.Enter the following entries:Type: Select the type using the F4 help. (Example (UBB-type 6 (U006)) )Work Item: Select the work items from the assigned work items.Delivery Organization: Service Organization - Company DE (1010)Quantity Planned: 10Choose Apply and Save. | Additional resources are added to the work package. |  |
| 12 | Add Expense Type to the Work Package | Select the work package to display the Details screen. Click on Edit.Navigate to the Expenses tab and click on show more per row.Click on create and make the following entries:Expense Type: AccommodationCost (planned): 100 EURChoose Apply and Save. | Expenses are added to the work package.Planned costs are recalculated.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration.For details, refer to SAP Product Assistance: [https://help.sap.com/viewer/product/SAP_S4HANA_CLOUD](https://help.sap.com/viewer/product/SAP_S4HANA_CLOUD). |  |
| 13 | Select Block Functions (optional) | Select a work package to display the Details screen. Click on Edit.Navigate to the blocked functions tab.The following Blocked Functions are visible that can be checked or unchecked based on the project requirement:Time RecordingActivity AllocationConcur Expense PostingPurchasingOther Expense PostingChoose Apply and save. |  |  |
| 14 | Navigate to Details of Work Packages | Choose the work package to display the Details screen. | The staffed roles, planned effort, planned costs, and planned revenues are displayed. |  |

### Maintain Settlement Rules

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to maintain settlement rules at work-package level.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Projects - Professional Services Projects (F8336). | The Manage Projects - Professional Services Projects screen displays. |  |
| 3 | Choose an Internal Project to Edit | Filter the Project by entering INT3300 is the Project field selection.Navigate to the details of the project by clicking on the arrow at the right hand side. | Project INT3300 is chosen and available for further editing. |  |
| 4 | Choose Work Packages View | Choose Manage Work Packages. | The Manage Work Package details page displays. |  |
| 5 | Maintain Settlement Rules | Choose the work package WP1 to maintain the settlement rules.Click on the maintain settlement rule button on the top right corner.On the Maintain Settlement Rule: Overview screen, make the following entries:Cat: CTRSettlement Receiver, for example, 33101601%: 100Settlement Type: PERChoose Save and close the window.Repeat the step for the work package WP2 and for further work packages if created. | Settlement rules are maintained. |  |

### Maintain Work Package Staffing (Without Scope Item 6JO: Resource Management for Projects)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once the roles have been assigned to the work packages, the project team can be staffed to specific work packages. This process step shows you how to maintain work package staffing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Projects - Professional Services Projects (F8336). | The Manage Project Control - Professional Services screen displays. |  |
| 3 | View My Projects Header Data and Choose an Internal Project to Edit | Choose Project INT3300 (created in an earlier step), choose Manage Work Packages, and navigate to the Manage Work Packages screen.Choose Edit on the top of the screen. | Project INT3300 is chosen and available for further editing. |  |
| 4 | Choose the Work Packages View | Click on the Work Package and navigate to the teams tab. Choose show more per row. | The Work Package details page displays. |  |
| 5 | Employee Staffing – Add Employee Assignment to Role in a Work Package | For each role, to staff an employee, choose the click on the value help of the Requested Worker under the Teams tab.Make the following entries:Work Package: WP1Role: Project ManagerRequested worker: Click on F4 help and select the worker (Example - Employee).Work Package: WP2Role: Project ManagerRequested worker: Click on F4 help and select the worker (Example - Employee).Note The worker can be a employee or Service Performer.Choose Apply and Save.Repeat this step to staff workers to the roles created. | The system displays a list of employees based on the suitability matching results. Suitability matching is performed automatically and is based on the availability and skills of the employees.Note Once the value help is clicked, The search result lists only employees belonging to company code of the delivery organization. Note that if no delivery organization is selected in the plan, then the company code of the project's service organization is applied. If the current employment of a business partner ends before the end of the work package, a warning icon is displayed in the Availability column.Availability is not based on a specific number of working days. Available hours in a month is calculated as (Weekly working hours / 7) * Calendar days per month.Once the project is set to the execution stage, the staffing confirmation can be done.Project Manager is staffed. |  |

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
| Note Once the integration with the external resource management system is activated, project manager cannot staff an employee ("Requested Resource" is for planning purposes) in the Manage Projects - Professional Services Projects (F8336) / Plan Internal Projects - Old Version (F1656) app. Staffing assignments must be made from the external system only. |

### Change the project Status (In Execution) and Confirmation of the staffing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to change the project status to In Execution and confirm staffing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Projects - Professional Services Projects (F8336). | The Manage Projects – Professional Services (F8336) screen displays. |  |
| 3 | Choose an Internal Project to Edit | Choose Project INT3300 and open it. | Project INT3300 is chosen and available for further editing. |  |
| 4 | Choose the project status | Go to "Set Stage" Tab & choose the option "In Execution". | Project Status is set to " In Execution". |  |
| 5 | Confirm the Staffing | Choose Manage work packages button and click on edit.Choose a work package for which the staffing confirmation needs to be done and navigate to the Teams tab of that work package. To confirm the staffing, select the check box for the confirmed field and click on apply and save.Note Staffing confirmation cannot be done during In planning stage | The confirmed status changes to yes and the staffed resources are displayed |  |
| 6 | Update Baseline and Finance Sync | By default, a baseline version is automatically created. All the initial planned data including the cost details will be pushed to Finance ACDOCP automatically.The sync with finance and update baseline is done via the app - Transfer Project Plan to Finance (F7293). It is a background job. Open the app Transfer Project Plan to Finance (F7293) and click on the create button. By default, the job template and job name is updated. You can change the name of the job, if required.Click on step 2. You will reach the scheduling option section. By default, the start immediately check box is enabled. If the job needs to be run at a certain time, uncheck the start immediately check box and select the date for which the job needs to be scheduled. Also, if the job needs to be scheduled on a regular basis, we can use the define recurrence pattern button to schedule it on hourly/daily/weekly/monthly basis considering it from the starting date. You can also use the define notification options to update the status of job via email to the respective recipients. Click on step 3 once the job is scheduled.You will reach the parameters section. There are two options available.Note A project should be created with the work packages, and it should be in execution stage.To update the baseline version, choose the radio button update baseline. Enter the following information:1. Project: INT10002. Work package (optional): WP1The project manager can always update the baseline by choosing Update baseline. During the update, only the version of those work packages that are entered will be updated. The versions of work packages that are not entered will be kept unchanged. If the work package details are not entered, during the update all the work packages versions will be updated.To sync the data with finance, choose the radio button sync with finance. Enter the following information:1. Service Organization: Service Organization - Company DE (1010)2. Customer3. Project Manager: Example ProjectManagerProf (PROJECT_MANAGER_PROF)4. Engagement Project: INT1000Click on schedule button. | The baseline version will be updated after the job gets completed.All the current updated planned data including the cost will be pushed to Finance ACDOCP again after the job gets completed. |  |

### Project-Level Mass Editing Functionality

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This optional step shows you how to edit/delete multiple projects at a time.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Projects - Professional Services Projects (F8336). | The Manage Projects – Professional Services (F8336) screen displays. |  |
| 3 | Display Project Details | You can view a list of projects with the details, such as project name, editing status of the project, service organization, start date, end date, customer name, project manager and stage. | The projects are listed with details. |  |
| 4 | Edit Multiple Projects | In order to edit multiple projects at a time, select the relevant project for which the details need to be changed and click on edit button.Note When a project A is in edit/draft mode by user A and if another user B is trying to select the project A and clicks on edit from the Manage Projects - Professional Services Projects, the user B will not be allowed to edit. | The relevant projects are selected for further editing |  |
| 5 | Input the values | For the projects selected, enter the manger, start date and end date which needs to be changed and click on save. We can either keep the existing field values or change it as per our requirement.Note Project Manager field is mandatory.In order to edit additional fields apart from the existing ones and select the settings button (near the edit button) and choose the fields for which the values need to be changed. Once the project is selected and edit button is clicked, the fields chosen in the previous step will be visible to make changes. | The selected projects are updated with the relevant information. |  |
| 6 | Delete multiple projects | In order to delete multiple projects at a time, select the relevant project for which the details needs to be changed and click on delete button.Note Projects under the In planning stage cannot be deleted |  |  |

### Run Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Costs are collected in projects only temporarily. They are settled to one or more receivers as part of period-end processing. This process shows you how to run the settlement.

Prerequisites

The following business processes must be run before continuing with the procedure below:

- Time Recording – Project-Based Services (J12)
- Service and Material Procurement – Project-Based Services (J13)
- Consumable Purchasing (BNX) (Optional)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Overhead Accounting Jobs (F3767). | The Schedule Overhead Accounting Jobs screen displays. |  |
| 3 | Enter Processing Data | To create a new job for the internal project, choose Create. Make the following entries:Job Template: Actual Settlement: Projects (SAP)Job Name: Actual Settlement: Projects (SAP)Then go to Step 2, under Scheduling Options:Select Start Immediately.Then go to Step 3, under Parameter Section:Settlement Period: for example, 12Fiscal Year: for example, 2020Ledger: for example, 0lProcessing Type: for example, By Period (or Automatic)Project Definition: for example, INT1000Actual Settlement: SelectTest Run: DeselectChoose Schedule.Note To display the settlement document and check the settlement amount in detail, go to the app Display Settlement Documents (F4597). | The work packages are settled to the cost center. |  |

### Set Project Status (Completed)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the status of the internal project is set to Completed. This process step shows you how to set project status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Projects - Professional Services Projects (F8336). | The Manage Projects – Professional Services (F8336) screen displays. |  |
| 3 | View Projects Header Data and Choose an Internal Project to Edit | Choose Project INT3300 | Project INT3300 displays. |  |
| 4 | Change the Project Status | Choose Set Stage and select Completed. Click ok to confirm. | The Completed status means no booking of further costs, no changes to the structure, and no effort on posting and planning possible. |  |

### Close Internal Projects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisites

The following Business Processes must be run before this step:

- Event-Based Revenue Recognition – Project-Based Services (1IL)
- Margin Analysis (J55)

Purpose

This process step shows you how to close internal projects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Projects - Professional Services Projects (F8336). | The Manage Projects – Professional Services (F8336) screen displays. |  |
| 3 | View Projects Header Data and Choose an Internal Project to Edit | Choose Project INT3300. | Project INT3300 displays. |  |
| 4 | Change the Project Status | Choose Set Stage and select Closed. Click ok to confirm. | When a project is closed, postings are no longer possible. |  |

### Reset Project Status to Completed (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to reset the internal project to Completed again.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Projects - Professional Services Projects (F8336). | The Manage Projects – Professional Services (F8336) screen displays. |  |
| 3 | View Projects Header Data and Choose a Customer Project to Edit | Choose Project INT3300. | Project INT3300 displays. |  |
| 4 | Change the Project Status | Choose Set Stage and select Closed. Click ok to confirm. |  |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Check the Situation | Check either one of the following situations:On the My Home screen, choose the bell icon in the upper right corner of the screen. A notification is displayed for the project that is created together with the situation.On the My Home screen, choose the Situations tab under To-Dos. A situation is displayed for the project. | The situation displays. |  |
| 3 | Change the Project Status | On the My Home screen, choose the relevant situation tile of the project and navigate to the Situation Page. Then choose the link Manage Projects - Professional Services Projects (F8336) under the Related Apps section, and navigate to the Manage Projects - Professional Services Projects (F8336) screen.Choose Set Stage and select Completed. Click ok to confirm. | The stage of the project is set to ‘Completed’. |  |
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
> Flagged while digesting this document, not verified: Master data and prerequisites describe Service Organization – Company AE (company code 3310, currency AED), but the work package, baseline and finance sync steps use Service Organization - Company DE (1010) and EUR amounts; project IDs also vary between INT1000, INT10002 and INT3300 across steps.

> [!warning] Conflict
> Flagged while digesting this document, not verified: The section 'Reset Project Status to Completed (Optional)' states its purpose is to reset the project to Completed but its only change step says to choose Set Stage and select Closed.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/collaborative-project-management-6jn-test-script-sap-s-4hana-cloud-pub]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1A8_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 77,027 chars in the whole document
