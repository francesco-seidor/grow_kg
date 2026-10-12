---
id: 06-management-accounting/test-script-project-control-resourcing-and-procurement-4rf-ae-1049
title: "Test Script: Project Control – Resourcing and Procurement (4RF_AE) (4RF_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 4RF_AE: project demands for materials, services and resources, with roles, apps and sample data."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/project-control-enterprise-projects]
aliases: [4RF_S4CLD2608_BPD_EN_AE]
keywords: ["Project Control for Finance, Capital, R&D and Sales Projects", project demand, non-stock material demand, project stock procurement, preliminary procurement, project stock reservation, service demand, resource demand, demand request, demand monitoring]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4RF_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1049
topic: 06-management-accounting/project-control-enterprise-projects
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Project Control – Resourcing and Procurement (4RF_AE) (4RF_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4RF_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Project Control for Finance, Capital, R&D and Sales Projects** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Project Control – Resourcing and Procurement (4RF_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Project Control – Resourcing and Procurement (4RF_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232855491)

[2 Prerequisites 4](#_Toc232855492)

[2.1 System Access 4](#_Toc232855493)

[2.2 Roles 4](#_Toc232855494)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232855495)

[2.4 Business Conditions 6](#_Toc232855496)

[2.5 Preliminary Steps 7](#_Toc232855497)

[2.5.1 Manage Situation Types for Project Demand Close Failed (Optional) 7](#_Toc232855498)

[2.5.2 Manage Situation Types for Project Demand Request Failed (Optional) 9](#_Toc232855499)

[3 Overview Table 11](#_Toc232855500)

[4 Test Procedures 12](#_Toc232855501)

[4.1 Material Demand 12](#_Toc232855502)

[4.1.1 Define Demand for Non-Stock Materials 12](#_Toc232855503)

[4.1.1.1 Request Demand 16](#_Toc232855504)

[4.1.1.1.1 Request Immediately 16](#_Toc232855505)

[4.1.1.1.2 Request on WBS Element Release 17](#_Toc232855506)

[4.1.1.2 Consumable Purchasing 18](#_Toc232855507)

[4.1.2 Define Demand for Direct Procurement 19](#_Toc232855508)

[4.1.2.1 Request Demand 22](#_Toc232855509)

[4.1.2.1.1 Request Immediately 22](#_Toc232855510)

[4.1.2.1.2 Request on WBS Element Release 23](#_Toc232855511)

[4.1.2.2 Convert Purchase Requisition to Purchase Order for Project Stock 24](#_Toc232855512)

[4.1.2.3 Goods Receipt for Project Stock 25](#_Toc232855513)

[4.1.2.4 Goods Issue from Project Stock 26](#_Toc232855514)

[4.1.3 Define Demand for Preliminary Procurement 27](#_Toc232855515)

[4.1.3.1 Request Demand 30](#_Toc232855516)

[4.1.3.1.1 Request Immediately 30](#_Toc232855517)

[4.1.3.1.2 Request on WBS Element Release 31](#_Toc232855518)

[4.1.3.2 Make-to-Stock Production – Discrete Manufacturing 32](#_Toc232855519)

[4.1.4 Define Demand for Project Stock, Reservation 33](#_Toc232855520)

[4.1.4.1 Request Demand 36](#_Toc232855521)

[4.1.4.1.1 Request Immediately 36](#_Toc232855522)

[4.1.4.1.2 Request on WBS Element Release 37](#_Toc232855523)

[4.1.4.2 Goods Issue from Project Stock 38](#_Toc232855524)

[4.2 Monitor Demand (Optional) 39](#_Toc232855525)

[4.3 Close Demand (Optional) 41](#_Toc232855526)

[4.4 Check and Return Extra Project Stock (Optional) 42](#_Toc232855527)

[4.5 Service Demand 44](#_Toc232855528)

[4.5.1 Define Demand for Services 44](#_Toc232855529)

[4.5.2 Request Demand 47](#_Toc232855530)

[4.5.2.1 Request Immediately 47](#_Toc232855531)

[4.5.2.2 Request on WBS Element Release 48](#_Toc232855532)

[4.5.3 Procurement of Services 49](#_Toc232855533)

[4.5.4 Monitor Demand (Optional) 50](#_Toc232855534)

[4.5.5 Close Demand (Optional) 51](#_Toc232855535)

[4.6 Resource Demand 53](#_Toc232855536)

[4.6.1 Define Demand for Resources 53](#_Toc232855537)

[4.6.2 Request Demand 55](#_Toc232855538)

[4.6.2.1 Request Immediately 55](#_Toc232855539)

[4.6.2.2 Request on WBS Element Release 56](#_Toc232855540)

[4.6.3 Assign Resource (Optional) 57](#_Toc232855541)

[4.6.3.1 Time Recording 58](#_Toc232855542)

[4.6.4 Monitor Demand (Optional) 59](#_Toc232855543)

[4.6.5 Close Demand (Optional) 61](#_Toc232855544)

[5 Appendix 62](#_Toc232855545)

[5.1 Prepare Employee CSV File for Upload 62](#_Toc232855546)

[5.2 Process Integration 68](#_Toc232855547)

[5.2.1 Preceding Processes 68](#_Toc232855548)

[5.2.2 Succeeding Processes 68](#_Toc232855549)

## Purpose

Overview

A successful project execution requires that the right resources, services, and materials are available. With this scope item, project demands can be used to manage that, beginning from early planning stages, when some details are not yet known. You can then assign people to project demands to fill their timesheet, or trigger and monitor the procurement of services and materials.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

Testing in a 3-System Landscape

In a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [https://help.sap.com/viewer/b249d650b15e4b3d9fc2077ee921abd0/latest/en-US/6c398c4ae7364af69d3edffe7fdc39f2.html](https://help.sap.com/viewer/b249d650b15e4b3d9fc2077ee921abd0/latest/en-US/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal

Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Assign the following business roles to your individual test users.

The following roles are provided as example roles from SAP. You can use these as templates for your own roles.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Project Financial Controller | SAP_BR_PROJ_FIN_CONTROLLER | Project Control - Finance | SAP_BR_PROJ_FIN_CONTROLLER |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Project Controller - Resourcing and Procurement | SAP_BR_PROJ_PROC_CONTROLLER | Project Control – Resourcing and Procurement | SAP_BR_PROJ_PROC_CONTROLLER |  |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Employee | SAP_BR_EMPLOYEE | Self Services / Self Services / Employee Overview Space | SAP_BR_EMPLOYEE / SAP_CA_SPT_EMPLOYEE_CROSS_PC / SAP_EAM_SPT_EMPLOYEE_PC |  |
| Project Manager - Professional Services | SAP_BR_PROJECT_MANAGER_PROF | Project Manager - Professional Services | SAP_BR_PROJECT_MANAGER_PROF |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | NS0001 | Non-Stock Goods for Consumption |  |
| Material | SM0001 | Service Material 01 |  |
| Material | SG124 | SEMI124,PD,Subassembly | Material used in Project Stock scenario. |
| Material | FG0611 | Finished Product with Serial number on Project stock.MRP Planned and Produced internally with project related manufacturing. | Material used in Project Stock-.Reservation scenario |
| Purchasing group | 001 | Group 001 |  |
| Purchasing group | 003 | Group 003 |  |
| Receiver Cost Center | 33101601 | Marketing Cost Center |  |
| Sender Cost Center | 33101101 | Financials (AE) |  |
| Activity Type | 8 | Consulting |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 1NT - Project Control – Finance | To execute the project creation /execution related activities, the 1NT - Project Control – Finance scope item must be activated. |
| 22Z - Procurement of Services | To execute the procurement process for services related to the project, the 22Z - Procurement of Services test script must be activated. |
| BNX - Consumable Purchasing | To execute the Consumable purchasing related to the project, the BNX - Consumable Purchasing test script must be activated. |
| J45 - Procurement of Direct Materials | To execute the procurement of project stock activities for the project, the J45- Procurement of Direct Materials scope item must be activated. |
| BMC - Core Inventory Management | To execute the inventory management process for project stock material related to the project, the Core Inventory Management scope item must be activated. |
| BMH - Stock Transfer Without Delivery | To execute the process of cross plant stock transfer without delivery within the same company code, the BMH- Stock Transfer Without Deliveryscope item must be activated. |
| BME - Stock Transfer with Delivery | To execute the process of cross plant stock transfer with delivery within the same company code, BME- Stock Transfer with Delivery must be activated. |
| 1Q4 - Time Recording | To execute the time sheet booking process, the 1Q4 - Time Recording test script must be activated. |
| 31N - Situation Handling | You can opt to receive notifications in cases of a failure during the project demand close or project demand request by configuring the situation type using a template. To be able to do the configuration, the Situation Handling (31N) scope item must be activated. |
| BJ5 - Make-to-Stock Production – Discrete Manufacturing | To execute the reservation created out of project stock-reservation, the Make-to-Stock Production – Discrete Manufacturing (BJ5) (BJ5) scope item must be activated. |
| 6JO - Resource Management for Projects | If External Staffing is activated in the system, to assign external resources Resource Management for Projects (6JO) (6JO) scope item must be activated and configured. |

### Preliminary Steps

A project must be created and preliminary costing has been done on the project as per the steps mentioned in the scope item 1NT- Project Control – Finance.

#### Manage Situation Types for Project Demand Close Failed (Optional)

Purpose

In this procedure, you configure the situation type by using template.

|  |
| --- |
| Note For details on situations and the process to set up situation types, see the Setting Up Situation Handling (31N) guide. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist |  |  |
| 2 | Open Manage Situation Types | Open Manage Situation Types (F2947) app. | The Manage Situation Types screen is displayed. |  |
| 3 | Select the Template to Copy | In the Situation Templates section, enter the ID EPPM_PROJ_DEMAND_CLOSE_FAILED and then choose Go.Select the latest version of EPPM_PROJ_DEMAND_CLOSE_FAILED, then choose Copy. | The Situation Type screen is displayed. |  |
| 4 | Maintain the Situation | Make the following entries and choose Save:Admin InformationID: <ID Name>Name: <ID Description>Example ID: Z_DEMAND_CLOSE_FAILEDName: Demand CloseSituation DisplayShort Description:Message Details:Notification:Resend Notifications: SelectedConditionsMaintain the values against the corresponding attributes/ filters to configure the conditions and use this function.RecipientsResponsibility by teams: Choose Add Team Category and maintain the team created through the 'Manage Teams and Responsibilities' app and maintain the value Project Procurement Controller in the field Filter by Member Function if you intend to send notifications triggered by the situation Management to the Project Procurement Controller, who is part of central project management team responsible for multiple projects.Responsibility Rules: Choose and select "Get the Project Responsible users (Project Financial Controller and Project Manager)" shown in the Rule list if you intend to trigger notifications to the project specific team defined in the project brief application. | The situation type is maintained |  |
| 5 | Enable The Situation Type | Choose Enable, it will change from NO to YES. |  |  |

#### Manage Situation Types for Project Demand Request Failed (Optional)

Purpose

In this procedure, you configure the situation type by using template.

|  |
| --- |
| Note For details on situations and the process to set up situation types, see the Setting Up Situation Handling (31N) guide. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist |  |  |
| 2 | Open Manage Situation Types | Open Manage Situation Types (F2947) app. | The Manage Situation Types screen is displayed. |  |
| 3 | Select the Template to Copy | In the Situation Templates section, enter the ID EPPM_PROJ_DEMAND_REQUEST_FAILED and choose Go.Select the latest version of EPPM_PROJ_DEMAND_REQUEST_FAILED, then choose Copy. | The Situation Type screen is displayed. |  |
| 4 | Maintain the Situation | Make the following entries and choose Save:Admin InformationID: <ID Name>Name: <ID Description>Example ID: Z_DEMAND_REQUEST_FAILEDName: Demand RequestSituation DisplayShort Description:Message Details:Notification:Resend Notifications: YESConditionsMaintain the values against the corresponding attributes/ filters to configure the conditions and use this function.RecipientsResponsibility by teams: Choose Add Team Category and maintain the team created through the 'Manage Teams and Responsibilities' app and maintain the value Project Procurement Controller in the field Filter by Member Function if you intend to send notifications triggered by the situation Management to the Project Procurement Controller, who is part of central project management team responsible for multiple projects.Responsibility Rules: Choose and select "Get the Project Responsible users (Project Financial Controller and Project Manager)" shown in the Rule list if you intend to trigger notifications to the project specific team defined in the Project Brief application. | The situation type is maintained |  |
| 5 | Enable The Situation Type | Choose Enable, it will change from NO to YES. |  |  |

## Overview Table

This scope item consists of several process steps provided in the table below:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Assign Resource (Optional)](#unique_11) [page ] 57 | Project Controller - Resourcing and Procurement | Manage Project Demand (F4562) |  |
| [Time Recording](#unique_12) [page ] 58 | See the Time Recording (1Q4) test script. | See the Time Recording (1Q4) test script. | See the Time Recording (1Q4) test script. |
| [Procurement of Services](#unique_13) [page ] 49 | Purchaser | See the test script. | See the test script. |
| [Consumable Purchasing](#unique_14) [page ] 18 | Purchaser | See the test script. | See the test script. |
| [Convert Purchase Requisition to Purchase Order for Project Stock](#unique_15) [page ] 24 | Purchaser | Process Purchase Requisitions - Deprecated (F1048) |  |
| [Goods Receipt for Project Stock](#unique_16) [page ] 25 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) |  |
| [Goods Issue from Project Stock](#unique_17) [page ] 26 | Warehouse Clerk | Post Goods Issue (MIGO_GI) |  |
| [Make-to-Stock Production – Discrete Manufacturing](#unique_18) [page ] 32 | Production Planner | See the scope item BJ5- Make-to-Stock Production – Discrete Manufacturing |  |
| [Monitor Demand (Optional)](#unique_19) [page ] 50 | Project Controller - Resourcing and Procurement | Manage Project Demand (F4562) |  |
| [Close Demand (Optional)](#unique_20) [page ] 51 | Project Controller - Resourcing and Procurement | Manage Project Demand (F4562) |  |
| [Check and Return Extra Project Stock (Optional)](#unique_21) [page ] 42 | Warehouse Clerk | Stock - Multiple Materials (F1595)Transfer Stock - In-Plant (F1061) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Material Demand

#### Define Demand for Non-Stock Materials

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define a demand which helps to plan, trigger and monitor procurement of Non-stock materials for enterprise projects. A demand represents a certain need of a WBS element at a certain time and a certain location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Controller - Resourcing and Procurement. |  |  |
| 2 | Access App | Open Manage Project Demand (F4562) | The Manage Project Demand screen with the following four tabs are displayed:All DemandsServicesMaterialsResources |  |
| 3 | Create Demand for Non-Stock Materials | Select the Materials tab and choose CreateMake the following entries in the Demand section:Demand Name:Example New Demand for Non-Stock MaterialWBS Element: <Project ID or WBS Element ID created in1NT - Project Control – Finance.Demand ID: <Incremental Demand ID is automatically generated>Example MATDMND1Note The Demand ID field is a free text field. Any value can be maintained, but duplicate values under same WBS element are not allowed.Only demand name, ID and WBS element are mandatory to create a new demand. Additional attributes only become mandatory once you want to trigger follow up processes. This way you can create first demand placeholders without details during the early stage of project planning.Demand Type: < Non-Stock Material >Material:Example NS0001Note : You can either maintain a material number or a material group. In case you maintain a material group, additional demand attributes need to be maintained.Quantity:Example 10Plant:3310(automatically derived from the WBS Element)Date Alignment: <Example : Align with WBS Element start date or Align with WBS Element finish date or No Alignment>Demand Date: <Automatically determined from WBS ElementNote Based on the date alignment selected, the demand date gets automatically selected from the WBS Element.Demand Status: CreatedMake the following entries in the Procurement section:Material Group: <Example: YBMM01, this gets automatically derived from the material>Purchasing Group: 001Purchasing Organisation: 3310Supplier: Example: 33300001Choose CreateYou can skip the following step if you do not want to create demand for Non-Stock Materials with limits. | The following demands are created with provided definition parameters.Material Demand: MATDMND1 |  |
| 4 | Create Demand for Non-Stock Materials with Limit | Select the Materials tab and choose CreateMake the following entries in the Demand section:Demand Name:Example : Demand for Non-Stock Material with LimitWBS Element: <Project ID or WBS Element ID created in1NT - Project Control – Finance.Demand ID: <Incremental Demand ID is automatically generated>Example MATDMND2Demand Type: < Non-Stock Material with Limit>Date Alignment: <Example : Align with WBS Element start and end date or No AlignmentDemand Start Date: <Automatically determined from WBS Element>Demand End Date: <Automatically determined from WBS Element>Plant:3310(automatically selected from the WBS Element)Expected Value: <Example: 100>Currency: <automatically derived from the WBS Element>Overall Limit: <Example: 100>Currency: <automatically derived from the WBS Element>Note The Expected Value can never be more than the overall limit, it should always be less than or equal to the overall limit.Demand Status: CreatedMake the following entries in the Procurement section:Material Group: Example: <YBMM00>Purchasing Group: 001Purchasing Organisation: 3310Supplier: Example: 10300001Choose Create | The following demands as are created with provided definition parameters.Material Demand: MATDMND2 |  |
| 5 | Create Demand (By Using Copy Functionality) | In the Standard section enter the following details and choose GODemand ID:Example MATDMND1Navigate to the Material tab, from the Worklist displayed, choose the line item displayed and choose Copy icon on the top of the demand list view to navigate to the Demand Object page.Maintain the following details and choose SaveDemand Name:Example Test Project Non-Stock Material DemandDemand ID:Example MATDMND3Date Alignment : No AlignmentDemand Start Date: <MM/DD/YYYY>Demand End Date: <MM/DD/YYYY>Note You will be able to change the demand dates and demand quantity of service / non-stock demands even after a demand was requested.If PO item already exists , it is not possible to decrease the demand quantity to make it less than the ordered quantity. | A new material demand MATDMND3 is created |  |

##### Request Demand

###### Request Immediately

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you request the procurement for the demands of your WBS Element. The demands can be requested immediately on saving by setting the demand status to Request on Save in the Demand Overview page. You can also request multiple demands at the same time with the demand list report. All service or material demands of the same WBS element that are requested at the same time will be grouped in the same purchase requisition. Purchase requisition items are generated for the released demands.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Controller - Resourcing and Procurement. |  |  |
| 2 | Access App | Open Manage Project Demand (F4562) | The Project Demand screen is displayed. |  |
| 3 | Choose Project Demands | In the Standard section, enter the following details and choose GO.WBS Element: <Project ID or WBS Element ID maintained during the Demand creationAll the demands created for the WBS Element are shown in Demand List view. | The created Project Demands are displayed in the demand list report. |  |
| 4 | Request Demand - Immediately | If you want the purchase requisition to be automatically created, navigate to the Material tab and from the Demand List view, select all the Demands listed for the given WBS Elements and navigate to their respective demand type tabs and choose Change Demand Status on the top of the list view.From the drop down list, select Request on Save.You can skip the following test step if all demands are already requested by following the processNote All service or material demands of the same WBS element that are requested at the same time will be grouped in the same purchase requisition. | PR Items get generated for all the Demands if no errors occur and the ID is shown in the Purchase Requisition Item column. |  |

###### Request on WBS Element Release

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you request the procurement for the demands of your WBS Elements. The demands can be requested with the release of the WBS Elements by setting the demand status to “Request on WBS Element Release” in the Demand Overview page. Purchase requisitions are generated automatically for the demands upon release of the WBS Element.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Controller - Resourcing and Procurement. |  |  |
| 2 | Access App | Open Manage Project Demand (F4562) | The Manage Project Demandscreen is displayed. |  |
| 3 | Choose Project Demands | In the Standard section, enter the following details and choose GO.WBS Element: <Project ID or WBS Element ID maintained during the Demand creationAll the demands created for the WBS Element are shown in Demand List view. | The created Project Demands are displayed in the demand list report. |  |
| 4 | Request Demand on WBS Element Release | If you want the purchase requisition to be created when the relevant WBS Element is released, navigate to the Material tab and from the Demand List view, select all the Demands listed for the given WBS Element and choose Change Demand Status on the top of the list view.From the drop down list, select Request on WBS Element Release.Note All service or material demands of the same WBS element that are requested at the same time will be grouped in the same purchase requisition.In case you assign resources to a resource demand tool and set the demand to requested, it results in pre-filled task in the time sheet.A situation is triggered in case the automatic request on WBS element release fails and it is sent to the team mentioned in [Manage Situation Types for Project Demand Request Failed (Optional)](#unique_9) [page ] 9. | All the Demands are set to Request on WBS Element Release status |  |

##### Consumable Purchasing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the requested non-stock materials are externally procured. This can start with an approval of the purchase requisition item that was generated for the project demand.

Procedure

To execute this activity, run steps starting from Convert Purchase Requisition to Purchase Order of the

BNX - Consumable Purchasing scope item to create and process your purchase order for consumables.

|  |
| --- |
| Note While converting the Purchase Requisition, use the PR generated from Material Demand created in the above steps. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Purchase Requisition Item | <PR ID genrated> | PR ID generated in step Request Demand |  |

#### Define Demand for Direct Procurement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define demand for material in project stock which helps to plan, trigger and monitor procurement of stock materials for enterprise projects. A demand represents a certain need of a WBS element at a certain time and a certain location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Controller - Resourcing and Procurement. |  |  |
| 2 | Access App | Open Manage Project Demand (F4562) | The Manage Project Demand screen with the following four tabs are displayed:All DemandsServicesMaterialsResources |  |
| 3 | Create Demand for Stock Materials | Select the Materials tab and choose CreateMake the following entries in the Demand section:Demand Name: <Example: New Demand For Stock Material>WBS Element: <Project ID or WBS Element ID of Investment project created in 1NT- Project Control – Finance>Demand ID: <Incremental Demand ID is automatically generated>Example MATDMND1Note The Demand ID field is a free text field. Any value can be maintained, but duplicate values under same WBS element are not allowed.You can create demands only for projects which support project stock (In CE2108, only projects with the profile "investment project"). You can also only use materials which support this process.Demand Type: < Project Stock, Direct Purchasing >Material:Example SG124Quantity:Example 10Note You will be able to change the demand dates and demand quantity of service / non-stock demands even after a demand was requested.If PO item already exists , it is not possible to decrease the demand quantity to make it less than the ordered quantity.Plant:3310(automatically derived from the WBS Element)Date Alignment: <Example : Align with WBS Element start date Or Align with WBS Element finish date>Demand Date: <Automatically determined from WBS element>Based on the date alignment selected, the demand date gets automatically selected from the WBS element.Demand Status: CreatedMake the following entries in the Procurement section:Purchasing Group: 001Purchasing Organisation: 3310Supplier: Example: 33300001Choose Create. | The following demands are created with the provided definition parameters.Material Demand: MATDMND1 |  |
| 4 | Create Demand (By Using Copy Functionality) | In the Standard section, enter the following details and choose GODemand ID:Example MATDMND1Navigate to the Material tab, from the Worklist displayed, choose the line item displayed and choose Copy icon on the top of the demand list view to navigate to the Demand Object page. Maintain the following details and choose Create.Demand Name:Example Test Project Stock Material DemandWBS Element: <Project ID or WBS Element ID of Investment project created in 1NT- Project Control – Finance>Demand ID:Example MATDMND2Demand Type: Project Stock, Direct PurchasingMaterial: : SG124Quantity: < Example: 10 >Plant: 3310Date Alignment : No AlignmentDemand Start Date: <MM/DD/YYYY>Demand End Date: <MM/DD/YYYY> | A new material demand MATDMND2 is created. |  |

##### Request Demand

###### Request Immediately

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you request the procurement for the demands of your WBS Element. The demands can be requested immediately on saving by setting the demand status to Request on Save in the Demand Overview page. You can also request multiple demands at the same time with the demand list report. All service or material demands of the same WBS element that are requested at the same time will be grouped in the same purchase requisition. Purchase requisition items are generated for the released demands.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Controller - Resourcing and Procurement. |  |  |
| 2 | Access App | Open Manage Project Demand (F4562) | The Project Demand screen is displayed. |  |
| 3 | Choose Project Demands | In the Standard section, enter the following details and choose GO.WBS Element: <Project ID or WBS Element ID maintained during the Demand creationAll the demands created for the WBS Element are shown in Demand List view. | The created Project Demands are displayed in the demand list report. |  |
| 4 | Request Demand - Immediately | If you want the purchase requisition to be automatically created, navigate to the Material tab and from the Demand List view, select all the Demands listed for the given WBS Elements and navigate to their respective demand type tabs and choose Change Demand Status on the top of the list view.From the drop down list, select Request on Save.You can skip the following test step if all demands are already requested by following the processNote All service or material demands of the same WBS element that are requested at the same time will be grouped in the same purchase requisition. | PR Items get generated for all the Demands if no errors occur and the ID is shown in the Purchase Requisition Item column.Note If With Reservation flag is enabled for Demand then the Reservation Item ID also gets generated along with Purchase Requisition item. |  |

###### Request on WBS Element Release

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you request the procurement for the demands of your WBS Elements. The demands can be requested with the release of the WBS Elements by setting the demand status to “Request on WBS Element Release” in the Demand Overview page. Purchase requisitions are generated automatically for the demands upon release of the WBS Element.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Controller - Resourcing and Procurement. |  |  |
| 2 | Access App | Open Manage Project Demand (F4562) | The Manage Project Demandscreen is displayed. |  |
| 3 | Choose Project Demands | In the Standard section, enter the following details and choose GO.WBS Element: <Project ID or WBS Element ID maintained during the Demand creationAll the demands created for the WBS Element are shown in Demand List view. | The created Project Demands are displayed in the demand list report. |  |
| 4 | Request Demand on WBS Element Release | If you want the purchase requisition to be created when the relevant WBS Element is released, navigate to the Material tab and from the Demand List view, select all the Demands listed for the given WBS Element and choose Change Demand Status on the top of the list view.From the drop down list, select Request on WBS Element Release.Note All service or material demands of the same WBS element that are requested at the same time will be grouped in the same purchase requisition.In case you assign resources to a resource demand tool and set the demand to requested, it results in pre-filled task in the time sheet.A situation is triggered in case the automatic request on WBS element release fails and it is sent to the team mentioned in [Manage Situation Types for Project Demand Request Failed (Optional)](#unique_9) [page ] 9. | All the Demands are set to Request on WBS Element Release status.Note If With Reservation flag is enabled for Demand then the Reservation Item ID also gets generated along with Purchase Requisition item. |  |

##### Convert Purchase Requisition to Purchase Order for Project Stock

Purpose

In this activity, requested materials for project stock are externally procured. This can start with an approval of the purchase requisition item that was generated for the project demand for stock materials.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Access App | Open Process Purchase Requisitions - Deprecated (F1048) | The Process Purchase Requisition screen is displayed. |  |
| 3 | Convert Purchase Requisitions to Purchase Orders | Fill in the following information in the Standard section and choose GoRequisition ID: <Requisition ID generated in the Request Demand>Plant: 3310Purchasing Group:Purchase Organisation: 3310Select the purchase requisition item from the list displayed and choose Create Purchase OrderFill in the following information and choose SavePurchase Order Type: NBChoose Save. | The purchase order is created. |  |

##### Goods Receipt for Project Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you deal with creation of goods receipt for project stock related to the project.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. |  |  |
| 2 | Access App | Open Post Goods Receipt for Purchasing Document (F0843) | The Post Goods Receipt for Purchasing Document screen is displayed. |  |
| 3 | Enter Purchasing Document Number | Enter the following values:Purchasing Document: Purchase Order created in the step [Convert Purchase Requisition to Purchase Order for Project Stock](#unique_15) [page ] 24 | The Item Details screen is displayed. |  |
| 4 | Select Material | Select the check box for material SG124 | Line item is selected. |  |
| 5 | Post Goods Receipt | Choose Post. | Material document(s) is posted: xxx |  |

##### Goods Issue from Project Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you issue goods from project stock in a warehouse to project for consumption.

Stock transfer for Project Stock is enabled within the same company code.

To execute stock without delivery, refer scope item BMH- Stock Transfer Without Delivery .

To execute stock delivery with delivery, refer scope item BME- Stock Transfer with Delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. |  |  |
| 2 | Access App | Open Post Goods Issue (MIGO_GI). | The Goods Issue screen is displayed. |  |
| 3 | Enter Goods Movement Details | Enter the following values in fields:Transaction Type: Goods IssueReference Document Type: OtherGoods Movement Type: 221/Q (GI project for proj).Press Enter | The Goods Issue screen is modified to enter project stock relevant details. |  |
| 4 | Enter Material and Project Details | Enter the details under the following tabs:MaterialMaterial: SG124QuantityQty in Unit of Entry:< Quantity of material to be withdrawn for consumption in Project>WherePress EnterWBS Element: <Created in the test procedure [Define Demand for Direct Procurement](#unique_27) [page ] 19>`Plant: 3310Storage Location: 331A |  |  |
| 7 | Post Goods Issue | Choose Post. | Material document(s) xx is created. |  |

#### Define Demand for Preliminary Procurement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you define demand for material in project stock which helps in planning, triggering, and monitoring preliminary procurement of long lead stock materials for enterprise projects. This process step results in the creation of Planned Independent Requirements (PIR). A demand represents a certain need of a WBS element at a certain time and at a certain location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Controller - Resourcing and Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Project Demand (F4562). | The Manage Project Demand screen is displayed. The screen has the following four tabs:All DemandsServicesMaterialsResources |  |
| 3 | Create Demand for Stock Materials | Select the Materials tab and choose Create.Make the following entries in the Demand section:Demand Name: <Example: New Demand For Stock Material>WBS Element: Project ID or WBS Element ID of Investment project created in 1NT- Project Control - Finance.Demand ID: Incremental Demand ID is automatically generated.Example MATDMND1Note The Demand ID field is a free text field. Any value can be maintained, but duplicate values under the same WBS element are not allowed.You can create demands only for projects which support project stock such as the Profile Investment Project and Project with Revenue. You can also only use materials which support this process.Demand Type: Project Stock, Preliminary ProcurementMaterial:Example SG124Quantity:Example 10Note You can change the demand dates and demand quantity of service or non-stock demands even after a demand was requested.Plant: Automatically derived from the WBS Element.Example 1710Date Alignment: Align with WBS Element start date Or Align with WBS Element finish dateDemand Date: Automatically determined from WBS elementBased on the date alignment selected, the demand date gets automatically selected from the WBS element.Demand Status: CreatedMake the following entries in the Procurement section:Requirement Plan: <Automatically populated>Note In case the requirement plan is a duplicate ID, please manually enter a unique requiremt plan ID.Choose Create. | The following demands are created with the provided definition parameters.Material Demand: MATDMND1 |  |
| 4 | Create Demand using the copy Functionality | In the Standard section, enter the following details and choose GO.Demand ID:Example MATDMND1From the Worklist displayed, choose the line item displayed and choose Copy icon on the top of the demand list view to navigate to the Demand Object page. Maintain the following details and choose Create.Demand Name:Example Test Project Stock Material DemandWBS Element: <Project ID or WBS Element ID of Investment project created in 1NT- Project Control - Finance>Demand ID:Example MATDMND2Demand Type: Project Stock, Preliminary ProcurementMaterial: : SG124Quantity:Example 10Plant: 1710Date Alignment : No AlignmentDemand Start Date: <MM/DD/YYYY>Demand End Date: <MM/DD/YYYY> | A new material demand MATDMND2 is created. |  |

##### Request Demand

###### Request Immediately

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you request the procurement for the demands of your WBS Element. The demands can be requested immediately on saving by setting the demand status to Request on Save in the Demand Overview page. You can also request multiple demands at the same time with the demand list report. All service or material demands of the same WBS element that are requested at the same time will be grouped in the same purchase requisition. Purchase requisition items are generated for the released demands.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Controller - Resourcing and Procurement. |  |  |
| 2 | Access App | Open Manage Project Demand (F4562) | The Project Demand screen is displayed. |  |
| 3 | Choose Project Demands | In the Standard section, enter the following details and choose GO.WBS Element: <Project ID or WBS Element ID maintained during the Demand creationAll the demands created for the WBS Element are shown in Demand List view. | The created Project Demands are displayed in the demand list report. |  |
| 4 | Request Demand - Immediately | If you want the Planned Independent Requirement (PIR) to be automatically created, navigate to the Material tab and from the Demand List view, select all the Demands listed for the given WBS Elements and navigate to their respective demand type tabs and choose Change Demand Status on the top of the list view.From the drop down list, select Request on Save.You can skip the following test step if all demands are already requested by following the processNote All service or material demands of the same WBS element that are requested at the same time will be grouped in the same Planned Independent Requirement (PIR). | Planned Independent Requirement (PIR) Plan gets generated for all the Demands if no errors occur and the ID is shown in the Purchase Requisition Item column. |  |

###### Request on WBS Element Release

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you request the procurement for the demands of your WBS Elements. The demands can be requested with the release of the WBS Elements by setting the demand status to “Request on WBS Element Release” in the Demand Overview page. Purchase requisitions are generated automatically for the demands upon release of the WBS Element.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Controller - Resourcing and Procurement. |  |  |
| 2 | Access App | Open Manage Project Demand (F4562) | The Manage Project Demandscreen is displayed. |  |
| 3 | Choose Project Demands | In the Standard section, enter the following details and choose GO.WBS Element: <Project ID or WBS Element ID maintained during the Demand creationAll the demands created for the WBS Element are shown in Demand List view. | The created Project Demands are displayed in the demand list report. |  |
| 4 | Request Demand on WBS Element Release | If you want the purchase requisition to be created when the relevant WBS Element is released, navigate to the Material tab and from the Demand List view, select all the Demands listed for the given WBS Element and choose Change Demand Status on the top of the list view.From the drop down list, select Request on WBS Element Release.Note All service or material demands of the same WBS element that are requested at the same time will be grouped in the same purchase requisition.In case you assign resources to a resource demand tool and set the demand to requested, it results in pre-filled task in the time sheet.A situation is triggered in case the automatic request on WBS element release fails and it is sent to the team mentioned in [Manage Situation Types for Project Demand Request Failed (Optional)](#unique_9) [page ] 9. | All the Demands are set to Request on WBS Element Release status |  |

##### Make-to-Stock Production – Discrete Manufacturing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the planned independent requirements created for the project are processed by Material Requirement Planning (MRP) run which results into Planned Orders. If the material needs to be external procured, the planned orders are converted to purchase requisitions. If the material needs to be internally produced, the planned orders are converted to production orders.

Procedure

To execute this activity, run steps starting from Material Requirements Planning at Plant Level of the BJ5 -Make-to-Stock Production – Discrete Manufacturing scope item to create and process your planned independent requirements.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Planned Independent Requirement Item | < Planned Independent Requirement Item ID generated> | PIR Item ID generated in step Request Demand. |  |

#### Define Demand for Project Stock, Reservation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can simplify and accelerate the goods issue process by requesting the warehouse to reserve materials for the project, to be withdrawn later as per the project's requirements. These reservations are taken into account by Material Requirements Planning (MRP), ensuring that the required materials are procured in time if they are out of stock. A demand represents a specific need of a WBS element at a certain time and location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Controller - Resourcing and Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Project Demand (F4562). | The Manage Project Demand screen is displayed. The screen has the following four tabs:All DemandsServicesMaterialsResources |  |
| 3 | Create Demand for Stock Materials | Select the Materials tab and choose Create.Make the following entries in the Demand section:Demand Name: <Example: New Demand For Stock Material>WBS Element: Project ID or WBS Element ID of Investment or Revenue Project (Created from 1NT or 35F with Investment or Revenue Profile).Demand ID: Incremental Demand ID is automatically generated.MATDMND1Note The Demand ID field is a free text field. Any value can be maintained, but duplicate values under the same WBS element are not allowed.You can create demands only for projects which support project stock such as Investment and Revenue. You can also only use materials which support this process.Demand Type: Project Stock, ReservationMaterial:Example FG0611Quantity:Example 10Note You can change the demand dates and demand quantity of service or non-stock demands even after a demand was requested.Plant: Automatically derived from the WBS Element.Example 1710Date Alignment: Align with WBS Element start date Or Align with WBS Element finish dateDemand Date: Automatically determined from WBS elementBased on the date alignment selected, the demand date gets automatically selected from the WBS element.Demand Status: CreatedChoose Create. | The following demands are created with the provided definition parameters.Material Demand: MATDMND1 |  |
| 4 | Create Demand using the copy Functionality | In the Standard section, enter the following details and choose GO.Demand ID:Example MATDMND1Note If theDemand ID field is missing in UI, choose Adapt Filters and select the Demand ID field and choose OK.Navigate to the Material tab, from the Worklist displayed, choose the line item displayed and choose Copy icon on the top of the demand list view to navigate to the Demand Object page. Maintain the following details and choose Create.Demand Name:Example Test Project Stock Material DemandWBS Element: Project ID or WBS Element ID of Investment or Revenue Project (Created from 1NT or 35F with Investment or Revenue Profile).Demand ID:Example MATDMND2Demand Type: Project Stock, ReservationMaterial: : FG0611Quantity:Example 10Plant: 1710Date Alignment : No AlignmentDemand Start Date: <MM/DD/YYYY>Demand End Date: <MM/DD/YYYY> | A new material demand MATDMND2 is created. |  |

##### Request Demand

###### Request Immediately

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you request the reservation for the demands of your WBS Element. The demands can be requested immediately on saving by setting the demand status to Request on Save in the Demand Overview page. You can also request multiple demands at the same time with the demand list report. All service or material demands of the same WBS element that are requested at the same time will be grouped in the same purchase requisition. Reservation Items are generated for the released demands.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Controller - Resourcing and Procurement. |  |  |
| 2 | Access App | Open Manage Project Demand (F4562) | The Project Demand screen is displayed. |  |
| 3 | Choose Project Demands | In the Standard section, enter the following details and choose GO.WBS Element: <Project ID or WBS Element ID maintained during the Demand creationAll the demands created for the WBS Element are shown in Demand List view. | The created Project Demands are displayed in the demand list report. |  |
| 4 | Request Demand - Immediately | If you want the reservation item to be automatically created, navigate to the Material tab and from the Demand List view, select all the Demands listed for the given WBS Elements and navigate to their respective demand type tabs and choose Change Demand Status on the top of the list view.From the drop down list, select Request on Save.You can skip the following test step if all demands are already requested by following the process. | A Reservation Item ID is generated for all demands if no errors occur, and the ID is shown in the Reservation Item field. Make a note of this Reservation Item ID as it will be used in the goods issue.Note MRP does not read this reservation and would not create requirements. |  |

###### Request on WBS Element Release

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you request the reservation for the demands of your WBS Elements. The demands can be requested with the release of the WBS Elements by setting the demand status to “Request on WBS Element Release” in the Demand Overview page. Reservation Items are generated automatically for the demands upon release of the WBS Element.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Controller - Resourcing and Procurement. |  |  |
| 2 | Access App | Open Manage Project Demand (F4562) | The Manage Project Demandscreen is displayed. |  |
| 3 | Choose Project Demands | In the Standard section, enter the following details and choose GO.WBS Element: <Project ID or WBS Element ID maintained during the Demand creationAll the demands created for the WBS Element are shown in Demand List view. | The created Project Demands are displayed in the demand list report. |  |
| 4 | Request Demand on WBS Element Release | If you want the reservation item to be created when the relevant WBS Element is released, navigate to the Material tab and from the Demand List view, select all the Demands listed for the given WBS Element and choose Change Demand Status on the top of the list view.From the drop down list, select Request on WBS Element Release. | All the Demands are set to Request on WBS Element Release status.A Reservation Item ID is generated for all demands if no errors occur, and the ID is shown in the Reservation Item field. Make a note of this Reservation Item ID as it will be used in the goods issue.Note MRP does not read this reservation and would not create requirements. |  |

##### Goods Issue from Project Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you issue goods against reservation item id from project stock in a warehouse to project for consumption.

Stock transfer for Project Stock is enabled within the same company code.

To execute stock without delivery, refer scope item BMH- Stock Transfer Without Delivery .

To execute stock delivery with delivery, refer scope item BME- Stock Transfer with Delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. |  |  |
| 2 | Access App | Open Post Goods Issue (MIGO_GI). | The Goods Issue screen is displayed. |  |
| 3 | Enter Goods Movement Details | Enter the following values in fields:Transaction Type: Goods IssueReference Document Type: ReservationReference Document ID: Reservation Item IDGoods Movement Type: 221/Q (GI project for proj).Choose Enter | The Goods Issue screen is modified to enter project stock relevant details. |  |
| 4 | Enter/Verify Material and Project Details | Enter/Verify the details under the following tabs:Material:FG0611QuantityQty in Unit of Entry:< Quantity of material to be withdrawn for consumption in Project>WherePress EnterWBS Element: <As used in the test procedure [Define Demand for Project Stock, Reservation](#unique_35) [page ] 33>`Plant: 3310Storage Location: 331A<From which the stock needs to be issued>Item OK: Select |  |  |
| 7 | Post Goods Issue | Choose Post. | Material document(s) xx is created. |  |

### Monitor Demand (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you monitor the demand of enterprise project WBS Elements.

You can navigate to the Monitor Project Procurement app from the Manage Project Demand screen to get more information about the related PR / PO.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a . Project Control – Resourcing and Procurement . |  |  |
| 2 | Access App | Open Manage Project Demand (F4562) | The Manage Project Demand screen is displayed. |  |
| 3 | Monitor Demand | In the Standard section, enter the following details and choose Go.WBS Element: <Project ID or WBS Element ID maintained during the Demand creation>In the Worklist displayed, you can see the following procurement related information such as:Delivered/ Not Delivered/ Not OrderedNet Order Value/ InvoicePurchase Requisition ItemPurchase Requisition release statusFirst planned deliveryLast planned deliveryChoose Purchase Requisition Item to navigate to the Purchase Requisition page to check the complete procurement related information. | All the Purchase Requisitions linked to the Project as shown in the Worklist are displayed |  |
| 4 | Monitor Resource Demands | In the Standard section, enter the following details and choose Go.Project: <Project ID maintained during the Demand creation> OrWBS Element : <WBS Element ID maintained during the De-mand creation>Under Resources tab, in the Worklist displayed, you can see the following resource staffing related information in the coloumns such as:Activity Type:Planned / Staffed / Actual:Assigned Resources:Choose the Resource Demand listed to navigate to the Resource Demand page | All the Resource Demands linked to the Project as shown in the Worklist are displayed. |  |

### Close Demand (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you have the option to close the project demand manually before the project closure. The system will also attempt to automatically close demands when the parent WBS element is completed. If there is an issue, a situation is sent to the team specified in [Manage Situation Types for Project Demand Close Failed (Optional)](#unique_8) [page ] 7

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Control – Resourcing and Procurement . |  |  |
| 2 | Access App | Open Manage Project Demand (F4562) | The Manage Project Demand screen is displayed. |  |
| 3 | Choose Project Demand - Consumables | In the Standard section enter the following details and choose GoWBS Element: <Project ID or WBS Element ID maintained during the Demand creation>All the demands created for the workpackage are shown in Worklist tabular view. | The created Project Demands are displayed in the demand list report |  |
| 4 | Close Demand | Navigate to the Material tab and from the Demand List report, select all the Demands listed for the given WBS Element and choose Change Demand Status on the top of the list view.From the drop-down list, select CloseNote A warning message is shown in case you close a demand which still has ongoing purchasing.The demands can be set closed manually only from the demand list report. | The Demands are set to closed. |  |

### Check and Return Extra Project Stock (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Before the project/ WBS element can be closed, the project/ wbs element should not be holding any project stock. This step helps in monitoring the project stock still being held under a project/wbs element and move the excess project stock from a wbs element before closing the wbs element. In this step, the stock is being moved from project stock to plant stock.

|  |
| --- |
| Note You can create demands only for projects which support project stock (In CE2108, only projects with the profile 'Investment project'). You can also only use materials which support this process. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Warehouse Clerk. |  |  |
| 2 | Access App | Open Stock - Multiple Materials (F1595). | The Stock - Mutiple Materials screen is displayed. |  |
| 3 | Check Extra Project Stock | Make the following entries in the search criteria and press Enter. (Adapt the filter criteria in case WBS element is not displayed by default)WBS Element: <Enter the WBS Element that was used in the previous Define Demand steps.>Choose Go. | Stock for all the material(s) held under WBS is displayed. |  |
| 4 | Return Extra Project Stock -Access App | Open Transfer Stock - In-Plant (F1061) | The Transfer Stock - In-Plant screen is displayed. |  |
| 5 | Return Extra Project Stock - Open Stock Overview | Enter the following data:Plant : 3310Material:<Enter the Material value that was used in the previous step> |  |  |
| 6 | Return Extra Project Stock - Select Transfer from Stock | In the column Unrestricted - Use Stock, select the icon next to the stock against the storage location 331A.Choose Project Stock.Note Before you execute this step ensure that the material used in the demand creation step is extended to the storage location 331A. For details, see the One step stock transfer step of the Core Inventory Management test script. | A pop-up screen with selectable stock appears |  |
| 7 | Return Extra Project Stock - Select Transfer to Stock | Re-select the same icon as in the earlier step.Choose Unrestricted-Use Stock. | A pop-up screen with selectable stock appearsA pop-up screen Transfer Stock - In-Plant appears. |  |
| 8 | Return Extra Project Stock - Transfer Stock | Enter the following details:WBS Element: <Enter the WBS Element that was used in the previous Define Demand step.>Special Stock Type: Standard StockQuantity: XChoose Post. | A system message tells you that the material document is created. |  |

### Service Demand

#### Define Demand for Services

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define a demand which helps to plan, trigger and monitor procurement of services for enterprise projects. A demand represents a certain need of a WBS element at a certain time and a certain location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Controller - Resourcing and Procurement. |  |  |
| 2 | Access App | Open Manage Project Demand (F4562) | The Manage Project Demand screen with the following four tabs are displayed:All DemandsServicesMaterialsResources |  |
| 3 | Create Demand for Services | Select the Services tab and choose CreateMake the following entries in the Demand section:Demand Name: <Example: New Demand for Services>WBS Element: <Project ID or WBS Element ID created in1NT - Project Control – Finance.Demand ID: <Incremental Demand ID is automatically generated>Example SERDMND1Note The Demand ID field is a free text field. Any value can be maintained, but duplicate values under same WBS element are not allowed.Only demand name, ID and WBS element are mandatory to create a new demand. Additional attributes only become mandatory once you want to trigger follow up processes. By this you can create first demand placeholders without details during the early stage of project planning.Demand Type: <Service >Material:Example SM0001Note You can either maintain a material number or a material group. In case you maintain a material group, additional demand attributes need to be maintained.Quantity:Example :10Plant:3310(automatically derived from the WBS Element)Date Alignment: <Example: No Alignment>Demand Start Date: <MM/DD/YYYY>Demand End Date: <MM/DD/YYYY>Demand Status: CreatedMake the following entries in the Procurement section:Purchasing Group: 001Purchasing Organisation: 3310 for ServicesChoose Create.You can skip the following step if you do not want to create service with limits. | The following demands are created with provided definition parameters.Service Demand: SERDMND1 |  |
| 4 | Create Demand for Service with Limit | Select the Services tab and choose CreateMake the following entries in the Demand section:Demand Name: <Example: Test Project Service Demand 2>WBS Element: <Project ID or WBS Element ID created in 1NT- Project Control – FinanceDemand ID: <Incremental Demand ID is automatically generated>Example : SERDMND2Demand Type: <Service with Limit>If the Demand Type is selected as Service with Limit, the following additional fields need to be maintained:Expected Value: <Example: 100>Currency: <automatically derived from the WBS Element>Overall Limit: <Example: 100>Currency: <automatically derived from the WBS Element>Note The Expected Value can never be more than the Overall limit, it should always be less than the overall limit or equal to the overall limit.Plant:3310(automatically derived from the WBS Element)Date Alignment: <Example: Align with WBS Element start and end date>Demand Start Date: <Automatically determined from WBS element>Demand End Date: <<Automatically determined from WBS element>>Demand Status: CreatedMake the following entries in the Procurement section:Material Group: < Example: P001 >Purchasing Group: 001Purchasing Organisation: 3310 for ServicesChoose Create. | The following demands are created with provided definition parameters.Service Demand: SERDMND2 |  |
| 5 | Create Demand (By Using Copy Functionality) | In the Standard section enter the following details and choose GODemand ID:Example SERDMND1Navigate to the Services tab and from the Worklist displayed, select the line item and choose Copy to navigate to the Demand Object page. Maintain the following details and choose Save.Demand Name:Example Test Project Service Demand 3Demand ID:Example SERDMND3Date Alignment : No AlignmentDemand Start Date: <MM/DD/YYYY>Demand End Date: <MM/DD/YYYY>Note You will be able to change the demand dates and demand quantity of service / non-stock demands even after a demand was requested.If PO item exists already, it will not be possible to decrease the demand quantity to less than the ordered quantity. | A new service demand SERDMND3 is created |  |

#### Request Demand

##### Request Immediately

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you request the procurement for the demands of your WBS Element. The demands can be requested immediately on saving by setting the demand status to Request on Save in the Demand Overview page. You can also request multiple demands at the same time with the demand list report. All service or material demands of the same WBS element that are requested at the same time will be grouped in the same purchase requisition. Purchase requisition items are generated for the released demands.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Controller - Resourcing and Procurement. |  |  |
| 2 | Access App | Open Manage Project Demand (F4562) | The Project Demand screen is displayed. |  |
| 3 | Choose Project Demands | In the Standard section, enter the following details and choose GO.WBS Element: <Project ID or WBS Element ID maintained during the Demand creationAll the demands created for the WBS Element are shown in Demand List view. | The created Project Demands are displayed in the demand list report. |  |
| 4 | Request Demand - Immediately | If you want the purchase requisition to be automatically created, navigate to the Service tab and from the Demand List view, select all the Demands listed for the given WBS Elements and navigate to their respective demand type tabs and choose Change Demand Status on the top of the list view.From the drop down list, select Request on Save.You can skip the following test step if all demands are already requested by following the processNote All service or material demands of the same WBS element that are requested at the same time will be grouped in the same purchase requisition. | PR Items get generated for all the Demands if no errors occur and the ID is shown in the Purchase Requisition Item column. |  |

##### Request on WBS Element Release

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you request the procurement for the demands of your WBS Elements. The demands can be requested with the release of the WBS Elements by setting the demand status to “Request on WBS Element Release” in the Demand Overview page. Purchase requisitions are generated automatically for the demands upon release of the WBS Element.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Controller - Resourcing and Procurement. |  |  |
| 2 | Access App | Open Manage Project Demand (F4562) | The Manage Project Demandscreen is displayed. |  |
| 3 | Choose Project Demands | In the Standard section, enter the following details and choose GO.WBS Element: <Project ID or WBS Element ID maintained during the Demand creationAll the demands created for the WBS Element are shown in Demand List view. | The created Project Demands are displayed in the demand list report. |  |
| 4 | Request Demand on WBS Element Release | If you want the purchase requisition to be created when the relevant WBS Element is released, navigate to the Service tab and from the Demand List view, select all the Demands listed for the given WBS Element and choose Change Demand Status on the top of the list view.From the drop down list, select Request on WBS Element Release.Note All service or material demands of the same WBS element that are requested at the same time will be grouped in the same purchase requisition.In case you assign resources to a resource demand tool and set the demand to requested, it results in pre-filled task in the time sheet.A situation is triggered in case the automatic request on WBS element release fails and it is sent to the team mentioned in [Manage Situation Types for Project Demand Request Failed (Optional)](#unique_9) [page ] 9. | All the Demands are set to Request on WBS Element Release status |  |

#### Procurement of Services

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, requested services are externally procured. This can start with an approval of the purchase requisition item that was generated for the project demand.

Procedure

To execute this activity, run steps from starting from Option A: Convert Purchase Requisition to Purchase Order of the scope item

22Z - Procurement of Services to create and process your purchase order for services.

|  |
| --- |
| Note While converting the Purchase Requisition, use the PR generated from Service Demand created in the above steps. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Purchase Requisition Item | <PR ID generated> | PR ID generated in step Request Demand. |  |

#### Monitor Demand (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you monitor the demand of enterprise project WBS Elements.

You can navigate to the Monitor Project Procurement app from the Manage Project Demand screen to get more information about the related PR / PO.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Controller - Procurement. |  |  |
| 2 | Access App | Open Manage Project Demand (F4562) | The Manage Project Demand screen is displayed. |  |
| 3 | Monitor Demand | In the Standard section, enter the following details and choose Go.WBS Element: <Project ID or WBS Element ID maintained during the Demand creation>In the Worklist displayed, you can see the following procurement related information such as:Delivered/ Not Delivered/ Not OrderedNet Order Value/ InvoicePurchase Requisition ItemPurchase Requisition release statusFirst planned deliveryLast planned deliveryChoose Purchase Requisition Item to navigate to the Purchase Requisition page to check the complete procurement related information. | All the Purchase Requisitions linked to the Project as shown in the Worklist are displayed |  |
| 4 | Monitor Resource Demands | In the Standard section, enter the following details and choose Go.Project: <Project ID maintained during the Demand creation> OrWBS Element : <WBS Element ID maintained during the De-mand creation>Under Resources tab, in the Worklist displayed, you can see the following resource staffing related information in the coloumns such as:Activity Type:Planned / Staffed / Actual:Assigned Resources:Choose the Resource Demand listed to navigate to the Resource Demand page | All the Resource Demands linked to the Project as shown in the Worklist are displayed. |  |

#### Close Demand (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you have the option to close the project demand manually before the project closure. The system will also attempt to automatically close demands when the parent WBS element is completed. If there is an issue, a situation is sent to the team specified in [Manage Situation Types for Project Demand Close Failed (Optional)](#unique_8) [page ] 7

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Control – Resourcing and Procurement . |  |  |
| 2 | Access App | Open Manage Project Demand (F4562) | The Manage Project Demand screen is displayed. |  |
| 3 | Choose Project Demand - Consumables | In the Standard section enter the following details and choose GoWBS Element: <Project ID or WBS Element ID maintained during the Demand creation>All the demands created for the workpackage are shown in Worklist tabular view. | The created Project Demands are displayed in the demand list report |  |
| 4 | Close Demand | Navigate to the Service tab from the Demand List report and select all the Demands listed for the given WBS Element and choose Change Demand Status on the top of the list view.From the drop-down list, select CloseNote A warning message is shown in case you close a demand which still has ongoing purchasing.The demands can be set closed manually only from the demand list report. | The Demands are set to closed. |  |

### Resource Demand

#### Define Demand for Resources

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define a demand which helps to plan, staff and monitor resources for enterprise projects. A demand represents a certain need of a wbs element at a certain time and a certain location.

|  |
| --- |
| Note If you have enabled External Staffing using Activate External Staffing for Enterprise Projects SSCUI then skip below procedure and assign external resources by following below sections from Resource Management for Projects (6JO) test script.Manage Resource Requests and Staffing as a Resource ManagerManage My Assignments and My Project Experience as a Project Team Member |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Controller - Resourcing and Procurement |  |  |
| 2 | Access App | Open Manage Project Demand (F4562) | The Manage Project Demand screen with the following four tabs are displayed:All DemandsServicesMaterialsResources |  |
| 3 | Create Demand for Resources | Select the Resources tab and choose CreateMake the following entries in the Demand section:Demand Name: <Example: New Demand For Resource>WBS Element: <Project ID or WBS Element ID created in1NT - Project Control – Finance.Demand ID: <Incremental Demand ID is automatically generated>Example RESDMND1Note The Demand ID field is a free text field. Any value can be maintained, but duplicate values under same WBS element are not allowed.Activity Type: <Example: 8>Planned Effort: <Example: 10 H>Cost Center : < Automatically derived from the WBS Element >Date Alignment: <Example : Align with WBS Element start & end date>Based on the date alignment selected, the demand date gets automatically selected from the WBS element.Demand Status: CreatedChoose Create | The following demands are created with provided definition parameters.Resource Demand: RESDMND1 |  |
| 4 | Create Demand (By Using Copy Functionality) | In the Standard section enter the following details and choose GODemand ID: If the Demand ID field is missing in UI, choose the Adapt Filters and 'select the Demand ID field and select OK.Example RESDMND1Navigate to the Resources tab, from the Worklist displayed, choose the line item displayed and choose Copy icon on the top of the demand list view to navigate to the Demand Object page.Maintain the following details and choose Create.Demand Name: <Example: Test Project Resource Demand>WBS Element: <Project ID or WBS Element ID created in1NT - Project Control – Finance.Demand ID: <Example RESDMND3>Activity Type:Planned Effort:Date Alignment : No AlignmentDemand Start Date: <MM/DD/YYYY>Demand End Date: <MM/DD/YYYY> | A new resource demand RESDMND3 is created. |  |

#### Request Demand

##### Request Immediately

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you request the procurement for the demands of your WBS Element. The demands can be requested immediately on saving by setting the demand status to Request on Save in the Demand Overview page. You can also request multiple demands at the same time with the demand list report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Controller - Resourcing and Procurement. |  |  |
| 2 | Access App | Open Manage Project Demand (F4562) | The Project Demand screen is displayed. |  |
| 3 | Choose Project Demands | In the Standard section, enter the following details and choose GO.WBS Element: <Project ID or WBS Element ID maintained during the Demand creationAll the demands created for the WBS Element are shown in Demand List view. | The created Project Demands are displayed in the demand list report. |  |
| 4 | Request Demand - Immediately | If you want the purchase requisition to be automatically created, navigate to the Resource tab and from the Demand List view, select all the Demands listed for the given WBS Elements and navigate to their respective demand type tabs and choose Change Demand Status on the top of the list view.From the drop down list, select Request on Save.You can skip the following test step if all demands are already requested by following the process . | Resource demand ID gets generated for all the Demands if no errors occur. |  |

##### Request on WBS Element Release

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you request the procurement for the demands of your WBS Elements. The demands can be requested with the release of the WBS Elements by setting the demand status to “Request on WBS Element Release” in the Demand Overview page. Purchase requisitions are generated automatically for the demands upon release of the WBS Element.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Controller - Resourcing and Procurement. |  |  |
| 2 | Access App | Open Manage Project Demand (F4562) | The Manage Project Demandscreen is displayed. |  |
| 3 | Choose Project Demands | In the Standard section, enter the following details and choose GO.WBS Element: <Project ID or WBS Element ID maintained during the Demand creationAll the demands created for the WBS Element are shown in Demand List view. | The created Project Demands are displayed in the demand list report. |  |
| 4 | Request Demand on WBS Element Release | If you want the purchase requisition to be created when the relevant WBS Element is released, navigate to the Material tab and from the Demand List view, select all the Demands listed for the given WBS Element and choose Change Demand Status on the top of the list view.From the drop down list, select Request on WBS Element Release.Note All service or material demands of the same WBS element that are requested at the same time will be grouped in the same purchase requisition.In case you assign resources to a resource demand tool and set the demand to requested, it results in pre-filled task in the time sheet.A situation is triggered in case the automatic request on WBS element release fails and it is sent to the team mentioned in [Manage Situation Types for Project Demand Request Failed (Optional)](#unique_9) [page ] 9. | All the Demands are set to Request on WBS Element Release status |  |

#### Assign Resource (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you assign resources to the demand created in the [Define Demand for Resources](#unique_46) [page ] 53 step.

|  |
| --- |
| Note If you have enabled External Staffing using "Activate External Staffing for Enterprise Projects" SSCUI then below procedure for Internal Staffing will not work. You can assign external resources by following the below sections from 6JO - Resource Management for Projects test script.Manage Resource Requests and Staffing as a Resource ManagerManage My Assignments and My Project Experience as a Project Team Member |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Control – Resourcing and Procurement . |  |  |
| 2 | Access App | Open Manage Project Demand (F4562) | The Manage Project Demand screen is displayed. |  |
| 3 | Choose Project Demand - Resources | In the Standard section, enter the following details and choose GO.Project : <Project ID maintained during the Resource Demand creation> orWBS Element: <WBS Element ID maintained during the Resource Demand creation>All the demands created for the WBS element are shown under the Resources Tab in Worklist tabular view. | The created project demands are displayed in the demand list report. |  |
| 4 | Assign Resource | From the Demand List report, select the demands listed for the given WBS element to navigate to the Resource Demand page.Choose Edit to update the Assignments (by default the demand will be in the display mode)Scroll down to the Assignments sections and choose CreateName : <Example: Employee>Note Only Resources who have an 'active employee work agreement', with a cost center same as that of the project demand cost center, will be displayed and can be staffed in the resource demand.Staffed Effort :Staffed Effort Unit :Choose Save | The resources have been assigned to resource demand defined for the WBS element. |  |

##### Time Recording

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the resource assigned to the project demand enters the time recording for WBS Element they are assigned to using the Manage My Timesheet (F1823) application.

Procedure

To execute this activity, execute the step Record Working Time- create new time entry under Record Actual Working Time step of the

1Q4 - Time Recording scope item, using the task already created for the WBS Element used in the Define Demand for Resources step from this document.

|  |
| --- |
| Note The tasks would be automatically created for the WBS Element with the Activity Type used during resource demand creation. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| WBS Element ID | <WBS Element ID maintained during the Resource Demand creation> | <WBS Element ID maintained during the Resource Demand creation> |  |

#### Monitor Demand (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you monitor the demand of enterprise project WBS Elements.

You can navigate to the Monitor Project Procurement app from the Manage Project Demand screen to get more information about the related PR / PO.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Control – Resourcing and Procurement |  |  |
| 2 | Access App | Open Manage Project Demand (F4562) | The Manage Project Demand screen is displayed. |  |
| 3 | Monitor Demand | In the Standard section, enter the following details and choose Go.WBS Element: <Project ID or WBS Element ID maintained during the Demand creation>In the Worklist displayed, you can see the following procurement related information such as:Delivered/ Not Delivered/ Not OrderedNet Order Value/ InvoicePurchase Requisition ItemPurchase Requisition release statusFirst planned deliveryLast planned deliveryChoose Purchase Requisition Item to navigate to the Purchase Requisition page to check the complete procurement related information. | All the Purchase Requisitions linked to the Project as shown in the Worklist are displayed |  |
| 4 | Monitor Resource Demands | In the Standard section, enter the following details and choose Go.Project: <Project ID maintained during the Demand creation> OrWBS Element : <WBS Element ID maintained during the De-mand creation>Under Resources tab, in the Worklist displayed, you can see the following resource staffing related information in the coloumns such as:Activity Type:Planned / Staffed / Actual:Assigned Resources:Choose the Resource Demand listed to navigate to the Resource Demand page | All the Resource Demands linked to the Project as shown in the Worklist are displayed. |  |

#### Close Demand (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you have the option to close the project demand manually before the project closure. The system will also attempt to automatically close demands when the parent WBS element is completed. If there is an issue, a situation is sent to the team specified in [Manage Situation Types for Project Demand Close Failed (Optional)](#unique_8) [page ] 7

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Control – Resourcing and Procurement |  |  |
| 2 | Access App | Open Manage Project Demand (F4562) | The Manage Project Demand screen is displayed. |  |
| 3 | Choose Project Demand - Consumables | In the Standard section enter the following details and choose GoWBS Element: <Project ID or WBS Element ID maintained during the Demand creation>All the demands created for the workpackage are shown in Worklist tabular view. | The created Project Demands are displayed in the demand list report |  |
| 4 | Close Demand | Navigate to the Resource tab, from the Demand List report, select all the Demands listed for the given WBS Element and choose Change Demand Status on the top of the list view.From the drop-down list, select CloseNote A warning message is shown in case you close a demand which still has ongoing purchasing.The demands can be set closed manually only from the demand list report. | The Demands are set to closed. |  |

## Appendix

### Prepare Employee CSV File for Upload

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a HR Information Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Import Employees. | The Import Employees screen displays.The App is used to create users and upload employees, employment, and Service Cost Level information. |  |
| 3 | Check Contents of the Screen | Check the following two parts in the screen:The first part is used to download the template and the second part to import data.Drag the Import Type drop box. There are four options:Employee and Employment ImportService Cost LevelBasic Employee ImportEmployee Skill Tag Import |  |  |
| 4 | Choose Delimiters | Choose Delimiters between comma and semicolon. | The CSV files are created or stored based on the List Separator settings (subject to your computer settings).For example, in India, the default separator is comma (,) and in Germany, the default separator is semicolon (;). |  |
| 5 | Download Templates | Choose Download Templates. | The templates are downloaded based on the selection of the delimiter.For example, if the user selects comma (,) then the templates are downloaded with comma as a separator.Download Complete Notification screen displays the message You can find the downloaded templates in the Downloads folder : Employee Data and Employment Data. For more information, please refer to the app description in the help.sap.com. |  |
| 6 | Use the Template to Customize | Use the templates (as covered in the following sections) to prepare your customized employee/employment and Service Cost Level csv file.Save the customized file and copy the path where the customized file is stored.Note Do not log off from the SAP S/4HANA system as you would need to resume once you are done with adapting the templates. |  |  |

|  |
| --- |
| Note The Adapt the employee data template, Adapt the employment data template, and Adapt the service cost level template steps are not performed in the SAP S/4HANA system. |

Adapt the Employee Data Template

In case you cannot download the template, a template table is provided below for your reference. All mandatory fields are with asterisk (*) and sample values. All required formats of the input data and constant options of the field are maintained in the column header.

You can create a customized file for upload.

Note that you can create employees from scratch or you can also update the data such as phone number and e-mail of the existing employee. If the user name field is empty for the uploading employees, the employee can not be created.

For existing employee, you can maintain the Employee Skill Tag. If Resource Management function is activated, system can match resource requests with resource automatically by considering his/her skills.

|  |
| --- |
| Note For contingent worker, you would need to fill some payment data in the import file in order to have the Vendor generated. Even if you prefer not to maintain bank information for vendors because you would be paying through check/cash, still you would need to maintain the payment method.Additionally you will need to fill the Language field, if not already done. |

Here is the Employee data template:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| *PersonExternalID | UserName | * *BusinessPartnerRole (BUP003[Employee]/BBP005[Service Performer]/BBP010[Freelancer]) | Supplier[*for BBP005] | *FirstName | *LastName | PersonFullName | GenderCode(1/2) | EmailAddress | PhoneNumber | MobilePhoneNumber | Language | BankCountry/Region | Bank | SWIFTCode | BankAccount | IBAN | PaymentMethod(T[Bank Transfer]/C[Cheque]/X[Cash]) | PaymentCurrency | BankAccountHolderName | BankControlKey | SkillTags (comma separated.Eg:SkillTag1,SkillTag2,SkillTag3) |
| INTSERVPERF 33 10 | INTSERVPERF 33 10 | BUP003 |  | AN | LI |  |  | an.li@sap.com |  |  | EN |  |  |  |  |  |  |  |  |  |  |
| EXTSERVPERF 33 10 | EXTSERVPERF 33 10 | BBP005 | 33300001 | LI | AN |  |  | li.an@sap.com |  |  | EN |  |  |  |  |  |  |  |  |  |  |

Adapt the Employment Data Template

In case you cannot download the template, a template table is provided below for your reference. All mandatory fields are with asterisk (*) and sample values. All required formats of the input data and constant options of the field are maintained in the column header.

You can create a customized file for upload.

|  |
| --- |
| Note The PersonExternalID here must be the same as maintained in the Employee Data file. |

Here is the Employment data template:

| *PersonExternalID | *StartDate(YYYYMMDD) | *EndDate(YYYYMMDD) | *WorkAgreementStatus(0[Inactive],1[Active]) | CompanyCode | CostCenter | WorkingTimePercentage | WeeklyWorkingHours(hh) | WeeklyWorkDays | ServiceCostLevel | ManagerPersonExternalID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| INTSERVPERF 33 10 | 20000805 | 99991231 | 1 | 3310 | 33101902 | 100 | 30 | 5 |  | Manager_HRINFO |
| EXTSERVPERF 33 10 | 20000805 | 99991231 | 0 | 3310 | 33101902 | 100 | 30 | 5 |  | Manager_HRINFO |

Adapt the Service Cost Level Template

|  |
| --- |
| NoteField ManagerPersonExternalID must be maintained if for example Line Manager is the approver for non-project related time recording.When you upload employment data for line manager, please make sure the manager's employment start date should be earlier than employee's employment start date.Field CostCenter should also be maintained. |

In case you cannot download the template, a template table is provided below for your reference. All mandatory fields are with asterisk (*) and sample values. All required formats of the input data and constant options of the filed are maintained in the column header.

You can create a customized file for upload. The PersonExternalID here must be the same as maintained in Employee and Employment Data file. The Service Cost Level can only be uploaded after a successful Employee/Employment data upload.

| *PersonExternalID | PersonWorkAgreementExternalID | CompanyCode | StartDate(YYYYMMDD) | *ServiceCostLevel |
| --- | --- | --- | --- | --- |
| INTSERVPERF 33 10 | INTSERVPERF 33 10 | 3310 |  | 5 |
| INTSERVPERF 33 10 | INTSERVPERF 33 10 | 3310 |  | 3 |

Adapt Employee Skill Tag Import Template

For existing employees, you can upload templates with import type Employee Skill Tag Import. To add a new skill, in column *Operation(A-Append/O-Overwrite), please choose A. To overwrite, please choose O.

Table 1:

| *PersonExternalID | SkillTags(comma separated.Eg:SkillTag1,SkillTag2,SkillTag3) | *Operation(A-Append/O-Overwrite) |
| --- | --- | --- |
| EXTSERVPERF3310 | ABAP,FI,LOGISTICS | A |
| EXTSERVPERF3310 | ABAP,FI,LOGISTICS | A |
| INTSERVPERF3310 | JAVA,CO | A |
| INTSERVPERF3310 | JAVA,CO | A |

Continue with the following steps in the SAP S/4HANA system:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 7 | Import Customized Employee/Employment Data | Choose Import Type=Employee and Employment Import. In Import Data(.csv), choose Browse under Employee Data and Employment Data to upload customized Employee data with the path copied in step 5 (path to store the customized file).In Import Name, enter the import name and then choose Import. | Based on the selected delimiter, the user has to upload the files.For example, if the user selects the comma (,) as delimiter and tries to upload the semicolon (;) separated template, you would see an error in the log.Once the upload is done, an appropriate message displays in the message box. |  |
| 8 | Monitor Employee Imports | After importing, the system directs you to the Monitor Employee Imports screen from where you can monitor whether the upload is in process or completed. |  |  |
| Set the filter to filter out the import result.Under variant Standard, for Severity, check the following status:CanceledErrorWarningInformationSuccessFor calendar Date From-To, choose the date when the import happens. The first click in calendar is Date from, the second click is Date To.Choose Go in the right upper menu. |  |  |  |  |
| Check the Application Log. | Depending on the import status, below status is shown under Severity field.CanceledErrorWarningInformationSuccessYou can select and double-click your import name row to check the log. |  |  |  |
| 9 | Import Customized Service Cost Level File and Employee Skill Tag Import | In the SAP launch pad, open Import Employees.Choose Import Type=Employee and Employment Import. In Import Data(.csv), choose Browse under Service Cost Level to upload customized Service Cost Level file with the path copied in step 5 (path to store the customized file).Input Import name in the box under Import Name, then choose Import.Choose Import Type=Employee Skill Tag Import, then in Import Data(.csv), choose Browse under Employee Skill Tag Import to upload customized Employee Skill Tag Import file with the path copied in step 5 (path to store the customized file).Enter Import name in the box under Import Name, then choose Import. |  |  |
| 10 | Monitor Imports for Service Cost Level and Employee Skill Tag Import | After importing, the system directs you to the Application Logs screen from where you can monitor whether the upload is in process or completed. |  |  |
| Set the filter to filter out the import result. Under variant Standard, for Severity, check all the status:CanceledErrorWarningInformationSuccessFor calendar Date From-To, choose the date when the import happens. The first click in calendar is Date from, the second click is Date To.Choose Go in the upper-right menu. |  |  |  |  |
| Check the Application Log. | Depending on the import status, one of the following displays in the Severity field.CanceledErrorWarningInformationSuccessYou can select and double-click your import name row to check the log. |  |  |  |
| 11 | Log On to SAP S/4HANA System with the Newly Created Employee ID to Check if Employee Upload is Executed Successfully. | Log on to the SAP Fiori Launchpad.User: <PersonalExternalID>Password: Initial1!Note Initial1! is the initial password for the newly created employee.Caution You must change this password for security reasons. | 1. The created/updated information of the employees and contingent workers/external consultant must be visible in the respective employee Factsheet.2. The user created from the CSV upload must be able to log on to the launchpad successfully. |  |

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

Complete the following processes and conditions before you start with the test steps:

| Process | Business Condition |
| --- | --- |
| 1NT - Project Control – Finance | Creation of Project |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
|  |  |

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
> Flagged while digesting this document, not verified: The Reservation section's purpose says reservations 'are taken into account by Material Requirements Planning (MRP)', while the Request steps' expected results say 'MRP does not read this reservation and would not create requirements'.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Project-stock demands are said to need project profile 'Investment project' only (In CE2108) under Direct Procurement and Check and Return Extra Project Stock, but 'Investment Project and Project with Revenue' under Preliminary Procurement and 'Investment and Revenue' under Reservation.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Sample plant differs within the same flows: preliminary procurement and reservation demands use example plant 1710, while the reservation goods issue uses Plant 3310 / storage location 331A for the same WBS element and material FG0611.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[06-management-accounting/period-end-closing-projects-bna-ae-test-script-sap-s-4hana-cloud-publi]]
- related-to :: [[06-management-accounting/test-script-project-control-capital-projects-35f-ae-sap-s-4hana-cloud]]
- related-to :: [[06-management-accounting/test-script-project-control-finance-1nt-ae-sap-s-4hana-cloud-public-ed]]
- related-to :: [[06-management-accounting/test-script-project-control-research-and-development-projects-35e-ae-9]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4RF_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 112,668 chars in the whole document
