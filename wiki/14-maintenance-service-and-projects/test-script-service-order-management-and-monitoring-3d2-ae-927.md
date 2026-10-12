---
id: 14-maintenance-service-and-projects/test-script-service-order-management-and-monitoring-3d2-ae-927
title: "Test Script: Service Order Management and Monitoring (3D2_AE) (3D2_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 3D2: prerequisites, config and step-by-step tests for service orders, confirmations and billing."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/service-order-management-and-billing]
aliases: [3D2_S4CLD2608_BPD_EN_AE]
keywords: [Service Order Management and Billing, service order management, service order templates, service confirmation, service billing, fixed price service orders, service bundles, ad hoc billing, service teams, overtime configuration]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3D2_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-927
topic: 14-maintenance-service-and-projects/service-order-management-and-billing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Service Order Management and Monitoring (3D2_AE) (3D2_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3D2_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Service Order Management and Billing** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Service Order Management and Monitoring (3D2_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232852313)

[2 Prerequisites 5](#_Toc232852314)

[2.1 System Access 5](#_Toc232852315)

[2.2 Roles 5](#_Toc232852316)

[2.3 Master Data, Organizational Data, and Transactional Data 6](#_Toc232852317)

[2.4 Additional Manual Configuration 8](#_Toc232852318)

[2.5 Preliminary Steps 8](#_Toc232852319)

[2.5.1 Create Employee via CSV File Upload 8](#_Toc232852320)

[2.5.2 Initialize Material Stock 8](#_Toc232852321)

[2.5.3 Configure Overtime 9](#_Toc232852322)

[2.5.4 Configure Overtime Category 11](#_Toc232852323)

[2.5.5 Maintain Service Cost Level for Worker 12](#_Toc232852324)

[2.5.6 Maintain Cost Rates 13](#_Toc232852325)

[2.5.7 Configure Service Teams 14](#_Toc232852326)

[2.5.7.1 Define Service Team Profile 14](#_Toc232852327)

[2.5.7.2 Assign Service Team Profile to Service Transactions 16](#_Toc232852328)

[2.5.7.3 Create a Service Team 18](#_Toc232852329)

[2.5.8 Configure Situation Handling (Optional) 19](#_Toc232852330)

[2.5.9 Configure Credit Check Management (Optional) 20](#_Toc232852331)

[2.5.10 Configure Simulative ATP Check (Optional) 22](#_Toc232852332)

[2.5.11 Manage Substitution/Validation Rules (Optional) 23](#_Toc232852333)

[2.5.12 Configure Lifecycle Status for Reservation Creation in Service Transaction (Optional) 24](#_Toc232852334)

[3 Overview Table 26](#_Toc232852335)

[3.1 Service Order Templates 26](#_Toc232852336)

[3.1.1 Service Order Template 26](#_Toc232852337)

[3.1.2 Fixed Price Service Order Template 26](#_Toc232852338)

[3.2 Service Order 27](#_Toc232852339)

[3.2.1 Service Items 27](#_Toc232852340)

[3.2.2 Fixed Price Service Bundle 28](#_Toc232852341)

[3.2.3 Service Bundle 28](#_Toc232852342)

[3.2.4 Service Bundle with Billing Request Lines (Ad Hoc Billing) 28](#_Toc232852343)

[3.3 Fixed Price Service Order 29](#_Toc232852344)

[3.3.1 Fixed Price Order 29](#_Toc232852345)

[3.3.2 Fixed Price Service Bundle 29](#_Toc232852346)

[3.3.3 Service Bundle with Billing Request Lines (Ad Hoc Billing) 30](#_Toc232852347)

[4 Test Procedures 31](#_Toc232852348)

[4.1 Service Order Templates 31](#_Toc232852349)

[4.1.1 Service Order Template 31](#_Toc232852350)

[4.1.1.1 Create Service Order Template 31](#_Toc232852351)

[4.1.1.2 Release Service Order Template 32](#_Toc232852352)

[4.1.1.3 Create Follow-Up Transaction for Service Order 33](#_Toc232852353)

[4.1.1.4 Create Follow-Up Transaction for Service Quotation 34](#_Toc232852354)

[4.1.2 Fixed Price Service Order Template 35](#_Toc232852355)

[4.1.2.1 Create Fixed Price Service Order Template 35](#_Toc232852356)

[4.1.2.2 Release Fixed Price Service Order Template 37](#_Toc232852357)

[4.1.2.3 Create Follow-Up Transaction for Fixed Price Service Order 37](#_Toc232852358)

[4.1.2.4 Create Follow-Up Transaction for Fixed Price Service Quotation 38](#_Toc232852359)

[4.2 Service Order 39](#_Toc232852360)

[4.2.1 Service Items 40](#_Toc232852361)

[4.2.1.1 Create Service Order 40](#_Toc232852362)

[4.2.1.2 Release Service Order Line Item 42](#_Toc232852363)

[4.2.1.3 Change Service Order 42](#_Toc232852364)

[4.2.1.4 Release Service Order 44](#_Toc232852365)

[4.2.1.5 Create Confirmation 45](#_Toc232852366)

[4.2.1.6 Cancel Service Confirmation (Optional) 47](#_Toc232852367)

[4.2.1.7 Release Confirmation for Billing 48](#_Toc232852368)

[4.2.1.8 Create Billing Document (Invoice) 49](#_Toc232852369)

[4.2.2 Fixed Price Service Bundle 50](#_Toc232852370)

[4.2.2.1 Create Service Order 50](#_Toc232852371)

[4.2.2.2 Create Confirmation 52](#_Toc232852372)

[4.2.2.3 Release Order for Billing 54](#_Toc232852373)

[4.2.2.4 Create Billing Document (Invoice) 54](#_Toc232852374)

[4.2.3 Service Bundle 56](#_Toc232852375)

[4.2.3.1 Create Service Order 56](#_Toc232852376)

[4.2.3.2 Create Confirmation 58](#_Toc232852377)

[4.2.3.3 Release Order for Billing 60](#_Toc232852378)

[4.2.3.4 Create Billing Document (Invoice) 61](#_Toc232852379)

[4.2.4 Service Bundle and Item with Billing Request Lines (Ad Hoc Billing) 62](#_Toc232852380)

[4.2.4.1 Create Service Order 62](#_Toc232852381)

[4.2.4.2 Schedule Job 65](#_Toc232852382)

[4.2.4.3 Create Billing Document (Invoice) 67](#_Toc232852383)

[4.3 Fixed Price Order 68](#_Toc232852384)

[4.3.1 Fixed Price Service Order 68](#_Toc232852385)

[4.3.1.1 Create Service Order 68](#_Toc232852386)

[4.3.1.2 Create Confirmation 70](#_Toc232852387)

[4.3.1.3 Release Order for Billing 71](#_Toc232852388)

[4.3.1.4 Create Billing Document (Invoice) 72](#_Toc232852389)

[4.3.2 Fixed Price Service Bundle 74](#_Toc232852390)

[4.3.2.1 Create Service Order 74](#_Toc232852391)

[4.3.2.2 Create Confirmation 75](#_Toc232852392)

[4.3.2.3 Release Order for Billing 77](#_Toc232852393)

[4.3.2.4 Create Billing Document (Invoice) 78](#_Toc232852394)

[4.3.3 Service Bundle and Item with Billing Request Lines (Ad Hoc Billing) 79](#_Toc232852395)

[4.3.3.1 Create Service Order 79](#_Toc232852396)

[4.3.3.2 Schedule Job 82](#_Toc232852397)

[4.3.3.3 Create Billing Document (Invoice) 84](#_Toc232852398)

[5 Appendix 86](#_Toc232852399)

[5.1 Process Integration 86](#_Toc232852400)

[5.1.1 Preceding Scope Items 86](#_Toc232852401)

[5.1.2 Succeeding Processes 86](#_Toc232852402)

## Purpose

Overview

This scope item covers service orders creation in SAP S/4HANA Cloud Public Edition. After planning, the service order is released for execution. Once the service order line items are released, a purchase requisition is created automatically for non-stock spare parts.

Service confirmations are posted against the service order line items. Based on the confirmation, time-sheet entries and expenses incurred are posted. Procurement costs can be copied into the confirmation from the supplier invoice or from the purchase order, so that the customer can be billed (Time & Material Service).

When a service order or confirmation is released for billing, a billing document request is created to invoice the customer.

The confirmation can be manually canceled, thus canceling the succeeding invoice and the billing document request (BDR).

Service orders can also be created automatically in the background as a follow-on from preceding processes, such as Service Quotations (4GA) or Recurring Services (4X5).

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/3D2_S4CLD2602_BPD_EN_AE.docx) ). |

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
| Customer Service Manager | SAP_BR_CUSTOMER_SRVC_MGR | Service Management / Service Management – SAP Field Service and Asset Management | SAP_BR_CUSTOMER_SRVC_MGR / SAP_S4CRM_SPT_FSM_PC |  |
| Service Technician - Customer Service | SAP_BR_CUSTOMER_SRVC_TEC | Service Processing | SAP_BR_CUSTOMER_SRVC_TEC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |

### Master Data, Organizational Data, and Transactional Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. Depending on the operational focus of your company, the master data represents materials, customers, and suppliers, for example.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Customer | 33100001 |  | You must either assign the customer pricing procedure 01 (Procedure 01) or ensure that the customer is not assigned to a pricing procedure.To check the assignment, use business role SAP_BR_BUPA_MASTER_SPECIALIST and access Manage Customer Master Data (F0850A). |
| Employee | <employee> | Use the employee ID that is assigned to your user. |  |
| Service product (service) | SRV_01 | Services | A service is usually performed by an internal employee. Alternatively, it can be procured from a third party (external workforce procurement). In that case, the scope item 3NI is required. |
| Service Product (Service Expense) | SRV_02 | Service Expenses |  |
| Service Part (Undefined) | SRV_03 | Service Part (Undefined) | Non-Stock MaterialNote If you want to test a spare part which is procured, scope item Procurement for Service Management (3NI) must be activated. |
| Service Part (Defined) | SRV_04 | Service Part (Defined) | Non-Stock MaterialNote If you want to test a spare part which is procured, scope item Procurement for Service Management (3NI) must be activated. |
| Service Product (Service Part Picked from Stock) | SRV_05 | Stock Service Part | Note If you want to test a spare part which is procured, refer to the materials Service Part (Undefined) or Service Part (Defined). |
| Sales Organization | 3310 |  |  |
| Material BOM, Equipment BOM | SRV_BOM_* |  | If you want to use product proposals, you must maintain the BOM items as described in Create Material and Equipment BOM for Service - MDS (63J). |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| 3KV | Create Service Product for Service Processes - MDS |
| 63J | Create Material and Equipment BOM for Service - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/b75c9118d5080ad9c43467e9fbd3b195)

### Preliminary Steps

#### Create Employee via CSV File Upload

Please refer to SAP Note [2555311](https://me.sap.com/notes/2555311) for details on how to create or update personal details, employment and service cost level data of an employee.

|  |
| --- |
| Note Please make sure to assign a cost center to your employee, for example, 33101902. This cost center will be used in the chapter Maintain Cost Rates. |

#### Initialize Material Stock

Purpose

It is required to have enough stock in the standard storage location of the plant.

If there is not enough stock, you must post initial stock directly to the storage location.

Prerequisite

The service product SRV_05 must have been created successfully as described in Master Data Script 3KV.

Furthermore, you may need to first complete Master Data Script Create New Open MM Posting Period (BNZ) to post stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Inventory Manager. |  |  |
| 2 | Access App | Open Manage Stock (F1062). | The Manage Stock screen appears. |  |
| 3 | Input Material | Make the following entries and press Enter:Plant: 3310Material: SRV_05 |  |  |
| 4 | Select Stock | Select the icon beside the stock to which you want to add initial stock.Storage Location: Std. storage 1 (331A)Unrestricted-Use Stock: <current stock quantity> | A dialog box opens. The Storage Location, Stock Type and Current Quantity are displayed according to your entries in the previous steps. |  |
| 5 | Add Initial Entry | If the existing quantity of Unrestricted-Use Stock is not sufficient, make the following entries and choose Post:Stock Change: Initial EntryQuantity: <enter a number>Document Date: for example, <today's date>Posting Date: for example, <today's date> | The stock has been added. |  |

#### Configure Overtime

Purpose

If you want to use overtime in the service scenario, you have to first switch on overtime. For the process described in this test script, this is mandatory. Do not forget to maintain the condition records as described in Set Prices for Overtime of Master Data Script 3KV afterwards.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: Human ResourcesSub Application Area: Time Sheet |  |  |
| 5 | Open | Open Time Recording. |  |  |
| 6 | Select Configuration Step | For the Maintain Data Entry Profiles (SAP S/4HANA Cloud Private Edition) step, choose Configure. | The Maintain Data Entry Profiles (SAP S/4HANA Cloud Private Edition): Change screen displays. |  |
| 7 | Select Data Entry Profile | Select the profile S4H_INT and choose Details. | The Maintain Data Entry Profiles (SAP S/4HANA Cloud Private Edition): Change: Details screen displays. |  |
| 8 | Select Overtime | Under General Settings, ensure that the flag for Overtime is selected.Choose Save. | Overtime is enabled. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad appears. |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain Data Entry Profiles (SAP S/4HANA).Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Maintain Data Entry Profiles (SAP S/4HANA Cloud Private Edition): Change screen displays. |  |
| 3 | Select Data Entry Profile | Select the profile S4H_INT and choose Details. | The Maintain Data Entry Profiles (SAP S/4HANA Cloud Private Edition): Change: Details screen displays. |  |
| 4 | Check Overtime | Under General Settings, ensure that Overtime is selected.Choose Save. | Overtime is enabled. |  |

#### Configure Overtime Category

Purpose

If you want to use overtime in the service scenario you have to switch on overtime. For the process described in this test script, it is mandatory.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: Human ResourcesSub Application Area: Time Sheet |  |  |
| 5 | Open | Open Time Recording. |  |  |
| 6 | Select Configuration Step | For the Maintain Overtime Categories step, choose Configure. | The Overtime Categories for Time Sheet screen displays. |  |
| 7 | Create Overtime Category | Check if there is at least one overtime category available.If not, create one or more new entries, for exampleOvertime Category: for example, OV01Description: for example, Overtime WeekdayOvertime Category: for example, OV02Description: for example, Overtime WeekendOvertime Category: for example, OV03Description: for example, Overtime Public Holiday | The overtime categorys are maintained. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad appears. |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain Overtime Categories.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Overtime Categories for Time Sheet screen displays. |  |
| 3 | Create Overtime Category | Check if there is at least one overtime category available.If not, create one or more new entries, for exampleOvertime Category: for example, OV01Description: for example, Overtime WeekdayOvertime Category: for example, OV02Description: for example, Overtime WeekendOvertime Category: for example, OV03Description: for example, Overtime Public Holiday | The overtime categorys are maintained. |  |

#### Maintain Service Cost Level for Worker

Purpose

The Administrator can assign a service cost level to a worker. This cost rate is used to determine the internal cost of a service in terms of an actual service order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Administrator. |  |  |
| 2 | Access App | Open Manage Service Level Agreements (F6183A). | The Manage Workforce screen displays. |  |
| 3 | Search for Worker | Make the following entries and choose Go:Worker ID: <ID>Select the worker from the list to access the Worker details. | The Worker screen displays. |  |
| 4 | Assign the Service Cost Level | Under the Work Agreements tab, select a Work Agreement to access the Work Agreement details.Choose Edit.If a service cost level is not already available, choose Create.Make the following entries:Service Cost Level: for example, 4 (SENIOR CONSULTANT (K4))Start Date: for example, <today's date>End Date: <future date>Select the service cost level and choose Apply.Choose Save. | The Work Agreement screen displays.The service cost level is assigned to the worker. |  |

#### Maintain Cost Rates

Purpose

This step describes how to maintain cost rates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Overhead Accountant. |  |  |
| 2 | Access App | Open Manage Cost Rates - Services (F3161) | The Manage Cost Rates - Services screen displays. |  |
| 3 | Maintain Cost Rates | Make the following entries and choose Go:Company Code: 3310Choose Add and make the following entries:Cost Center: <empty>Activity Type: for example, SV01From FY: <year>From Period: <period>Rate: for example, 50Currency: for example, AEDPer: for example, 1Activity Unit: for example, HIf not all fields are visible, choose Show more per row.Choose Save. | The cost rates are created. |  |

#### Configure Service Teams

This section is only relevant if you want to use the service team concept.

##### Define Service Team Profile

Purpose

A service team profile exists by default. It defines which determination rule is used and for which team types it is relevant. If you want to use a different profile, you can follow the procedure below to create a new entry.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: ServiceSub Application Area: Service Order Management |  |  |
| 5 | Open | Open Service Teams. |  |  |
| 6 | Select Configuration Step | For the Define Service Team Profile and Assign Service Team Types step, choose Configure. | The screen Define Service Team Profile and Assign Serv..: Change screen displays. |  |
| 7 | Define Team Profile | There should be at least one existing entry:Profile:SRV_FS_PDescription:Field Service Team ProfileDetermination Rule:SHIP_TODescription:Country and postal code of ship-to partyAuto Redetermine:-If you want to use another profile, you have to create a new entry here. | A valid service team profile exists. |  |
| 8 | Specify Allowed Team Types | Select an existing team profile and doublc-click Specify Allowed Team Types in the Dialog Structure.For the team profile SRV_FS_P, you should find the following entry:Team Type: SRV_FSDescription: Field ServiceIf you have created and selected a new profile, maintain the allowed team types here. | A valid service team profile including allowed team types exists. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Service Team Profile and Assign Service Team Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The screen Define Service Team Profile and Assign Serv..: Change screen displays. |  |
| 3 | Define Team Profile | There should be at least one existing entry:Profile:SRV_FS_PDescription:Field Service Team ProfileDetermination Rule:SHIP_TODescription:Country and postal code of ship-to partyAuto Redetermine:-If you want to use another profile, you have to create a new entry here. | A valid service team profile exists. |  |
| 4 | Specify Allowed Team Types | Select an existing team profile and doublc-click Specify Allowed Team Types in the Dialog Structure.For the team profile SRV_FS_P, you should find the following entry:Team Type: SRV_FSDescription: Field ServiceIf you have created and selected a new profile, maintain the allowed team types here. | A valid service team profile including allowed team types exists. |  |

##### Assign Service Team Profile to Service Transactions

Purpose

If you want to use the service team concept, you should assign at least a service team profile to a service transaction and to its related confirmation transaction.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: ServiceSub Application Area: Service Order Management |  |  |
| 5 | Open | Open Service Teams. |  |  |
| 6 | Select Configuration Step | For the Assign Service Team Profile to Service Transaction Type step, choose Configure. | The Assign Service Team Profile to Service Transaction screen displays. |  |
| 7 | Maintain Data | If you want to use the service team concept in the service order, make the following entries and choose Save:Trans.Type: SVO1Service Team Profile: SRV_FS_PTrans.Type: SVC1Service Team Profile: SRV_FS_P | The service team concept has been activated for the standard service order (SVO1) and its respective service confirmation (SVC1). |  |
| 8 | Maintain Data | If you want to use the service team concept in the service order, make the following entries and choose Save:Trans.Type: SVO2Service Team Profile: SRV_FS_PTrans.Type SVC2Service Team Profile: SRV_FS_P | The service team concept has been activated for the fixed price service order (SVO2) and its respective service confirmation (SVC2). |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Service Team Profile to Service Transaction Type.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Service Team Profile to Service Transaction screen displays. |  |
| 3 | Maintain Data | If you want to use the service team concept with service orders, make the following entries and choose Save:Trans.Type: SVO1Service Team Profile: SRV_FS_PTrans.Type: SVC1Service Team Profile: SRV_FS_P | The service team concept has been activated for the standard service order and its respective service confirmation. |  |
| 4 | Maintain Data | If you want to use the service team concept with fixed price service orders, make the following entries and choose Save:Trans.Type: SVO2Service Team Profile: SRV_FS_PTrans.Type SVC2Service Team Profile: SRV_FS_P | The service team concept has been activated for the fixed price service order and its respective service confirmation. |  |

##### Create a Service Team

Purpose

If you want to use the service team concept, you have to create at least one service team to run the service process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access App | Open Manage Teams and Responsibilities (F2412). | The Manage Teams and Responsibilities screen displays. |  |
| 3 | Create A New Team | Choose Create. | The Team screen displays. |  |
| 4 | Enter General Information | Make the following entries and press Enter:Name: Service_Team_AEDescription: Service Team AEType: SRV_FS |  |  |
| 5 | Enter Responsibility Definitions | Under Responsibility Definitions, make the following entries:Country/Region: AEPostal Code: <empty>Service Part Plant: 3310Service Part Storage Location: 331A |  |  |
| 6 | Enter Team Owner | It is recommended to leave the default team owner. |  |  |
| 7 | Enter Team Members | Choose Create.Choose Edit.Enter data for each team member of this service team:Business Partner: for example, 9980000XXXFull Name: <team member's name>User ID: for example, CB9980000XXXFunction: Executing Service Employee (SRVC_EMPL)Choose Save. | A service team has been created successfully. |  |

#### Configure Situation Handling (Optional)

Purpose

Situation handling recognizes business situations by evaluating conditions (rules) on business facts. A business situation occurs when a business object changes a status relevant to a user, for instance, when critical deadlines are passed, or a KPI passes a threshold.

Prerequisite

If you want to use situation handling with Service Order Management and Monitoring, Situation Handling (31N) must be in scope. You must carry out the steps that are described in the Situation Handling (31N) test script.

For more information, see [Setting Up Situation Handling (31N)](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/Setup/31N_Set-Up_EN_XX.pdf).

Procedure

To set up situation handling, create your ready-to-use situation type, maintain the message to be displayed, define the conditions to determine when the situation will be triggered, define recipient groups who will receive notifications, and monitor the instances.

The following standard situation templates are defined and delivered by SAP for Service Order Management and Monitoring:

- SRVC_DELAY_IN_SRVC_ORD_BILLING (Billing for Service Order Not Completed)
- SRVC_PENDING_SERVICECONFIRMATION (Service Confirmations Required)
- SRVC_SERV_ORDER_TRANSFER_ERROR (Transfer of Service Order Data Failed)
- SRVC_PLND_END_AFTER_DUE_DATE (Planned End Date Is After Due Date)
- SRVC_PLANNED_COST_POSTING_ERROR (Baseline Calculation Not Successful)
- SRVC_ORDER_MISSING_SERV_EMP (Executing Service Employee Missing

For more information and situation template details (default settings, conditions, notification recipients), see [Situation Templates in Service](https://help.sap.com/viewer/adbae5bcd5994f159bf2847a11397b61/LATEST/en-US/9d6cee508b2e44a39e93474ee68e6ba9.html) .

#### Configure Credit Check Management (Optional)

Purpose

You use Credit Management to minimize financial risks for your organization. It enables you to display a business partner's credit rating, or to perform a credit check when creating a transaction document. Credit management can be enabled for service orders to maintain and check credit of relevant business partners.

Follow the procedure below to set up credit management for service orders.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: ServiceSub Application Area: General Settings |  |  |
| 5 | Open | Open Credit Management. |  |  |
| 6 | Select Configuration Step | For the Activate Credit Management in Service Transactions step, choose Configure. | The Activate Credit Management in Transactions screen displays. |  |
| 7 | Maintain Data | To activate the credit management settings for service orders, make the following entires and choose Save:Trans. Type: SVO1Description: Service OrderCredit Management: SelectedTrans. Type: SVO2Description: Fixed Price Service OrderCredit Management: Selected | The credit management settings are saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Credit Management in Service Transactions.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Activate Credit Management in Transactions screen displays. |  |
| 3 | Maintain Data | To activate the credit management settings for service orders, make the following entires and choose Save:Trans. Type: SVO1Description: Service OrderCredit Management: SelectedTrans. Type: SVO2Description: Fixed Price Service OrderCredit Management: Selected | The credit management settings are saved. |  |

#### Configure Simulative ATP Check (Optional)

Purpose

You can enable simulative ATP checks for service part items in a service order. Once enabled, ATP checks can be performed for items in the service order to verify the availability of the service part item.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: ServiceSub Application Area: General Settings |  |  |
| 5 | Open | Open Activate ATP Check for Service Parts. |  |  |
| 6 | Select Configuration Step | For the configuration step Activate ATP Check for Service Parts, choose Configure. | The ATP Relevance for Item Categories screen displays. |  |
| 7 | Enable Check | You can select the ATP Relevant checkbox to activate the check for the specified item category.Choose Save. | The ATP check is enabled for the selected item categories. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate ATP Check for Service Parts.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The ATP Relevance for Item Categories screen displays. |  |
| 3 | Enable Check | You can select the ATP Relevant checkbox to activate the check for the specified item category.Choose Save. | The ATP check is enabled for the selected item categories. |  |

#### Manage Substitution/Validation Rules (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

With this app, you can display, change, and create substitution and validation rules for your selected business contexts and events for service document. These rules can be used in the respective business processes to validate, derive, or replace values at the time of entry for the relevant fields.

|  |
| --- |
| Note The system first determines the cost center of the employee responsible for the item and then the profit center that is defined for this cost center. If no profit center is defined for the cost center, the system uses the dummy profit center defined for the controlling area. You can also manually change the profit center assigned to a service transaction item. Once you have made such a manual change, the system no longer redetermines the profit center should you change the employee responsible. |

|  |
| --- |
| Note The rules must be activated. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Home screen appears. |  |
| 2 | Access App | Open Manage Substitution/Validation Rules - Service Documents (F7818). | The Manage Substitution and Validation Rules screen displays. |  |
| 3 | Check Rules | The following default settings are provided. You can adopt them according to your business needs:Costing Sheet Rule:/0SAP/SV_COSTING_SHEET-SAPThis rule derives costing sheet SV001.Functional Area Rule:/0SAP/SV_FUNCTIONAL_AREAThis rule uses the functional area YB25.You can create a new functional area by perfoming the configuration activity Define Functional Areas. You can add this functional area to the substitution rule if needed.Note No default rule is provided for profit center. You must maintain the rule. | The rules are defined. |  |

#### Configure Lifecycle Status for Reservation Creation in Service Transaction (Optional)

Purpose

You can use this configuration activity to control reservation creation at an item category level. The default status of the service item category added is Released.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: ServiceSub Application Area: General Settings |  |  |
| 5 | Open | Open Define Lifecycle Status for Reservation Creation in Service Transaction. |  |  |
| 6 | Select Configuration Step | For the configuration step Define Lifecycle Status for Reservation Creation in Service Transaction, choose Configure. | The Service: Cust. View to Maint. Stat. for Reservation Creation screen displays. |  |
| 7 | Define Lifecycle Status | You can set a status in the Status of Reservation Creation column for each combination of service transaction and item category. |  |  |
| 8 | Save | Choose Save. | The changes are saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Lifecycle Status for Reservation Creation in Service Transaction.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Service: Cust. View to Maint. Stat. for Reservation Creation screen displays. |  |
| 3 | Define Lifecycle Status | You can set a status in the Status of Reservation Creation column for each combination of service transaction and item category. |  |  |
| 4 | Save | Choose Save. | The changes are saved. |  |

## Overview Table

The scope item Service Order Management and Monitoring (‏3D2‏) encompasses the field services execution aspect of businesses. A service order is created from an external system. The subsequent service confirmation is received with simultaneous cost calculations. Finally, the customer is invoiced.

If contract management is required, consider the preceding process Service Contract Management (3MO).

If service parts are to be procured, consider the succeeding process Procurement for Service Management (3NI).

The scope item 3D2 differentiates between the scenario variants:

- Service Oder (Service Item, Service Bundle Fixed Price, and Service Bundle)
- Fixed Price Order (Fixed Price Item and Service Bundle Fixed Price)

### Service Order Templates

#### Service Order Template

This process covers the creation of a service order template. The template has the required details of a service item, expense item, or service part. And it is used to create a service order.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Service Order Template](#unique_24) [page ] 31 | Customer Service Manager | Manage Service Order Templates (F5007) | A service order template has been created. |
| [Release Service Order Template](#unique_25) [page ] 32 | Customer Service Manager | Manage Service Order Templates (F5007) | The service order template is released. |
| [Create Follow-Up Transaction for Service Order](#unique_26) [page ] 33 | Customer Service Manager | Manage Service Order Templates (F5007) | A follow-up service order is created. |
| [Create Follow-Up Transaction for Service Quotation](#unique_27) [page ] 34 | Customer Service Manager | Manage Service Order Templates (F5007) | A follow-up service quotation is created. |

#### Fixed Price Service Order Template

This process covers the creation of a fixed price service order template. Using this template, you can create a fixed price service order for fixed price items.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Fixed Price Service Order Template](#unique_29) | Customer Service Manager | Manage Service Order Templates (F5007) | A service order template has been created. |
| [Release Fixed Price Service Order Template](#unique_30) [page ] 37 | Customer Service Manager | Manage Service Order Templates (F5007) | The service order template is released. |
| [Create Follow-Up Transaction for Fixed Price Service Order](#unique_31) [page ] 37 | Customer Service Manager | Manage Service Order Templates (F5007) | A follow-up fixed price service order is created. |
| [Create Follow-Up Transaction for Fixed Price Service Quotation](#unique_32) [page ] 38 | Customer Service Manager | Manage Service Order Templates (F5007) | A follow-up fixed price service quotation is created. |

### Service Order

#### Service Items

The key characteristic of this process variant is that the total billed amount is calculated on the basis of a confirmed service item, an expense item, or a service part.

|  |
| --- |
| Note Optional follow-up steps for analyzing service fulfillment can be found in the test script for Service Monitoring and Analytics (43B). |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Service Order](#unique_34) [page ] 40 | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | A service order has been created. |
| [Release Service Order Line Item](#unique_35) [page ] 42 | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | The item of the service order has been released. |
| [Change Service Order](#unique_36) [page ] 42 | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | The service order has been changed. |
| [Release Service Order](#unique_37) [page ] 44 | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | The service order has been released. |
| [Create Confirmation](#unique_38) [page ] 45 | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | A follow-up service confirmation has been created. |
| [Cancel Service Confirmation (Optional)](#unique_39) [page ] 47 | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | The service confirmation has been cancelled. |
| [Release Confirmation for Billing](#unique_40) [page ] 48 | Customer Service Manager | Release For Billing (F3573) | The confirmation has been released for billing. |
| [Create Billing Document (Invoice)](#unique_41) [page ] 49 | Billing Clerk | Create Billing Documents (F0798) | An invoice (billing document) is created. |

#### Fixed Price Service Bundle

This scenario is a variant of a service order which uses a fixed price service bundle. A fixed price service bundle consists of a main item and one or more subitems. In the case of a fixed price service bundle, your customer receives a billing document for the main item; subitems are not invoiced separately.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Service Order](#unique_43) [page ] 50 | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | A service order has been created. |
| [Create Confirmation](#unique_44) [page ] 52 | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | A follow-up service confirmation has been created. |
| [Release Order for Billing](#unique_45) [page ] 54 | Customer Service Manager | Release For Billing (F3573) | The confirmation has been released for billing. |
| [Create Billing Document (Invoice)](#unique_46) [page ] 54 | Billing Clerk | Create Billing Documents (F0798) | An invoice (billing document) is created. |

#### Service Bundle

This scenario is a variant of service order which uses a service bundle. A service bundle consists of a main item and one or more subitems. The main purpose of a service bundle from a business perspective is to enable you to analyze the contribution margins of services rendered at the level of the main item.

|  |
| --- |
| Note Optional follow-up steps for analyzing service fulfillment can be found in the test script for Service Monitoring and Analytics (43B). |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Service Order](#unique_48) [page ] 56 | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | A service order has been created. |
| [Create Confirmation](#unique_49) [page ] 58 | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | A follow-up service confirmation has been created. |
| [Release Order for Billing](#unique_50) [page ] 60 | Customer Service Manager | Release For Billing (F3573) | The order has been released for billing. |
| [Create Billing Document (Invoice)](#unique_51) [page ] 61 | Billing Clerk | Create Billing Documents (F0798) | The billing document is created. |

#### Service Bundle with Billing Request Lines (Ad Hoc Billing)

This scenario is a variant of a service order which uses a Service Bundle (Ad Hoc Billing) or Service Product Item (Ad Hoc Billing). A service bundle consists of a main item and one or more subitems. The service bundle and product service item for ad hoc billing can have billing request lines which will result in billing document requests and invoice items

|  |
| --- |
| Note Optional follow-up steps for analyzing service fulfillment can be found in the test script for Service Monitoring and Analytics (43B). |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Service Order](#unique_53) [page ] 62 | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | A service order has been created. |
| [Schedule Job](#unique_54) [page ] 65 | Customer Service Manager | Schedule Order Billing Document Request Creation (F7257) | A job run has been scheduled to create billing document requests (BDRs) for the billing request lines. |
| [Create Billing Document (Invoice)](#unique_55) [page ] 67 | Billing Clerk | Create Billing Documents (F0798) | The billing document is created. |

### Fixed Price Service Order

#### Fixed Price Order

In this scenario, a fixed price is maintained in the service order. You can bill items of a fixed price order only after completion of the order.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Service Order](#unique_57) [page ] 68 | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | A fixed price service order has been created |
| [Create Confirmation](#unique_58) [page ] 70 | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | A follow-up service confirmation has been created |
| [Release Order for Billing](#unique_59) [page ] 71 | Customer Service Manager | Release For Billing (F3573) | The order has been released for billing |
| [Create Billing Document (Invoice)](#unique_60) [page ] 72 | Billing Clerk | Create Billing Documents (F0798) | The billing document is created. |

#### Fixed Price Service Bundle

This scenario is a variant of a service order which uses a fixed price service bundle. A fixed price service bundle consists of a main item and one or more subitems.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Service Order](#unique_62) [page ] 74 | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | A fixed price service order has been created. |
| [Create Confirmation](#unique_63) [page ] 75 | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | A follow-up service confirmation has been created. |
| [Release Order for Billing](#unique_64) [page ] 77 | Customer Service Manager | Release For Billing (F3573) | The order has been released for billing. |
| [Create Billing Document (Invoice)](#unique_65) [page ] 78 | Billing Clerk | Create Billing Documents (F0798) | The billing document is created. |

#### Service Bundle with Billing Request Lines (Ad Hoc Billing)

This scenario is a variant of a service order which uses a Service Bundle (Ad Hoc Billing) or Service Product Item (Ad Hoc Billing). A service bundle consists of a main item and one or more subitems. The service bundle and product service item for ad hoc billing can have billing request lines which will result in billing document requests and invoice items

|  |
| --- |
| Note Optional follow-up steps for analyzing service fulfillment can be found in the test script for Service Monitoring and Analytics (43B). |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Service Order](#unique_67) [page ] 79 | Customer Service Manager | Manage Service Orders - To-Do List (F3571A) | A service order has been created. |
| [Schedule Job](#unique_68) [page ] 82 | Customer Service Manager | Schedule Order Billing Document Request Creation (F7257) | A job run has been scheduled to create billing document requests (BDRs) for the billing request lines. |
| [Create Billing Document (Invoice)](#unique_69) [page ] 84 | Billing Clerk | Create Billing Documents (F0798) | The billing document is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Service Order Templates

Service order templates are used to define reusable sets of service-related data that minimize the amount of time required to create a service transaction. A service order template describes only the scope of planned services and not the actual execution (customer and time frame). The service order templates can then be used to create service orders.

#### Service Order Template

##### Create Service Order Template

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a service order template. The template has the required details of a service item, expense item, or service part. And it is used to create a service order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Acces App | Open Manage Service Order Templates (F5007). | The Manage Service Order Templates screen displays. |  |
| 3 | Create Service Order Template | Choose Create. | The Create Service Order Template window displays. |  |
| 4 | Maintain Data | Make the following entries:Template Type: Service Order TemplateDescription: <description>Employee Responsible: <employee>Product ID: for example, SRV_01Quantity: for example, 1Unit: for example, HRProduct ID: for example, SRV_02Quantity: for example, 1Unit: for example, EAPress Enter.Choose Save and Edit. |  |  |
| 5 | Maintain Additional Data | Under Organizational Data, make the following entries and choose Save:Sales Organization: for example, 3310Sales Office: for example, 330Sales Group: for example, 330Distribution Channel: for example, 10Division: for example, 00Note Service material SRV_01 is usually assumed to be performed by an internal employee. If it should be procured from a 3rd party, scope item 3NI must be in scope. And you must set the item category to STW1 (External Service SES). | A new service order template is created.Note down the service order template number.Your service order template is displayed in Manage Service Order Templates (F5007). |  |

##### Release Service Order Template

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release the service order template that you created in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Order Templates (F5007). | The Manage Service Order Templates screen displays. |  |
| 3 | Find Service Order Template | Make the following entries and choose Go:Template ID: <your template ID> | Your service order template is displayed in the report list. |  |
| 4 | Release Template | Choose your template.On the Service Order Template screen, choose Release. | The service order template is released. |  |

##### Create Follow-Up Transaction for Service Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a follow-up service order from the previously released service order template.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Order Templates (F5007). | The Manage Service Order Templates screen displays. |  |
| 3 | Find Service Order Template | Make the following entries and choose Go:Template ID: <your template ID> | Your service order template is displayed in the report list. |  |
| 4 | Create Follow-Up | Choose Create Follow-Up > Create Service Order . | The Create Service Order window displays. |  |
| 5 | Create a Service Order | Make the following entries:Sold-To Party: for example, 33100003Description: <your description>Requested Start Date - End Date: <date range>Life Cycle Status: OpenUnder Items, select the required items for the service order, for example, SRV_01.Choose Save. | A new service order is created.Note down the service order number.Your service order is displayed in Manage Service Orders - To-Do List (F3571A). |  |

##### Create Follow-Up Transaction for Service Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a follow-up service quotation from the previously released service order template.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |
| 2 | Access App | Open Manage Service Order Templates (F5007). | The Manage Service Order Templates screen displays. |
| 3 | Find Service Order Template | Make the following entries and choose Go:Template ID: <your template ID> | Your service order template is displayed in the report list. |
| 4 | Create Follow-Up | Choose Create Follow-Up > Create Service Quotation. | The Create Service Quotation window displays. |
| 5 | Create Service Quotation | Make the following entries:Sold-To Party: for example, 10100003Description: <your description>Requested Start Date - End Date: <date range>Life Cycle Status: OpenUnder Items, select the required items for the service order, for example, SRV_01.Choose Save. | A new service order is created.Note down the service order number.Your service order is displayed in Manage Service Orders - To-Do List (F3571A). |

#### Fixed Price Service Order Template

##### Create Fixed Price Service Order Template

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Key purpose of this step is to create a fixed price service order template which can be used for creating a follow up fixed price service order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Acces App | Open Manage Service Order Templates (F5007). | The Manage Service Order Templates screen displays. |  |
| 3 | Create Service Order Template | Choose Create. | The Create Service Order Template window displays. |  |
| 4 | Maintain Data | Make the following entries:Template Type: Fixed Price Service OrderDescription: <description>Employee Responsible: <employee>Product ID: for example, SRV_01Quantity: for example, 1Unit: for example, HRProduct ID: for example, SRV_02Quantity: for example, 1Unit: for example, EAPress Enter.Choose Save and Edit. |  |  |
| 5 | Maintain Additional Data | Under Organizational Data, make the following entries and choose Save:Sales Organization: for example, 3310Sales Office: for example, 330Sales Group: for example, 330Distribution Channel: for example, 10Division: for example, 00Note Service material SRV_01 is usually assumed to be performed by an internal employee. If it should be procured from a 3rd party, scope item 3NI must be in scope. And you must set the item category to STW1 (External Service SES). | A new service order template is created.Note down the service order template number.Your service order template is displayed in Manage Service Order Templates (F5007). |  |

##### Release Fixed Price Service Order Template

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release the fixed price service order template created in previous step to be able to convert it into a fixed price service order

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Order Templates (F5007). | The Manage Service Order Templates screen displays. |  |
| 3 | Find Service Order Template | Make the following entries and choose Go:Template ID: <your template ID> | Your service order template is displayed in the report list. |  |
| 4 | Release Template | Choose your template.On the Service Order Template screen, choose Release. | The service order template is released. |  |

##### Create Follow-Up Transaction for Fixed Price Service Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a follow-up service order from the previously released fixed price service order template.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Order Templates (F5007). | The Manage Service Order Templates screen displays. |  |
| 3 | Find Service Order Template | Make the following entries and choose Go:Template ID: <your template ID> | Your service order template is displayed in the report list. |  |
| 4 | Create Follow-Up | Choose Create Follow-Up > Create Service Order . | The Create Service Order window displays. |  |
| 5 | Create a Service Order | Make the following entries:Sold-To Party: for example, 33100003Description: <your description>Requested Start Date - End Date: <date range>Life Cycle Status: OpenUnder Items, select the required items for the service order, for example, SRV_01.Choose Save. | A new service order is created.Note down the service order number.Your service order is displayed in Manage Service Orders - To-Do List (F3571A). |  |

##### Create Follow-Up Transaction for Fixed Price Service Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a follow-up service quotation from the previously released fixed price service order template.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |
| 2 | Access App | Open Manage Service Order Templates (F5007). | The Manage Service Order Templates screen displays. |
| 3 | Find Service Order Template | Make the following entries and choose Go:Template ID: <your template ID> | Your service order template is displayed in the report list. |
| 4 | Create Follow-Up | Choose Create Follow-Up > Create Service Quotation. | The Create Service Quotation window displays. |
| 5 | Create a Service Order | Make the following entries:Sold-To Party: for example, 10100003Description: <your description>Requested Start Date - End Date: <date range>Under Items, select the required items for the service quotation, for example, SRV_01.Choose Save. | A new service quotation is created.Note down the service quotation number.Your service quotation is displayed in Manage Service Quotation. |

### Service Order

This section describes the test procedures for each manual step that belongs to the process variant, where the customer is billed the labor and materials required to provide the service.

It is about a typical service process from the perspective of the customer service manager, service employee (formerly:service technician) and billing clerk.

#### Service Items

##### Create Service Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a service order.

|  |
| --- |
| Note You don't have to create a new service order if you have completed the test script for Service Quotation (4GA). If you created a service quotation, then a service order has been generated automatically. |

|  |
| --- |
| Note You don't have to create a new service order if you have created a service order template. In that case, a service order has been generated automatically. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A). | The Manage Service Order screen displays. |  |
| 3 | Create Service Order | Choose Create Service Order → Quick Create. | The Create Service Order window displays. |  |
| 4 | Maintain Data | Make the following entries:Service Order Type: Service OrderSold-To Party: for example, 33100003Description: <your description>Requested Start Date - End Date: <date range>Product ID: for example, SRV_01Quantity: for example, 1Unit: for example, HRProduct ID: for example, SRV_02Quantity: for example, 1Unit: for example, EAChoose Save and Edit. | A new service order is created.Note down the service order number.Your service order is displayed in Manage Service Orders - To-Do List (F3571A).NoteIf your sold-to party is associated with one or more service contracts, a new popup window will appear and ask you to select a contract per item. Select No Assignment.If the service team concept has been enabled for the standard service order (SVO1), a popup window may appear and ask you to choose a service team. Select your service team. |  |
| 5 | Maintain Additional Data | Under Items, add an additional item for this service order:Product ID: for example, SRV_05Quantity: for example, 1Unit: for example, PCPress Enter.Choose Save. | The service order is saved.NoteService material SRV_01 is usually assumed to be performed by an internal employee. If it must be procured from a 3rd party, scope item 3NI must be in scope. And you have to set the item category to SEW1 (External Service Item)By default, service item SRV_01 is a T&M item with item category SVP1. If you would like to use a fixed price item instead of a time and materials item, you need to change the item category to SVP2 or SVP5 (Partial Billing).If you activated the simulative ATP check for SRV_05, you will be able to see the availability and the quantity of the required stock item when creating the service order.If you configured the reservation status for SRV_05, you will be able to see the reservation quantity while creating and releasing the service order.If you enabled credit check management for service orders and the service order is blocked by the credit, then please refer to scope item Advanced Credit Management (1QM) for information about resolving it.If you have entered a product ID or an equipment ID as reference objects in the service order, you can choose Product Proposal to select related service order items. |  |

##### Release Service Order Line Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release a line item of the service order. It is a prerequisite for a follow-up confirmation of the line item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A). | The Manage Service Order screen displays. |  |
| 3 | Find Service Order | Make the following entries and choose Go:Service Order: <ID> |  |  |
| 4 | Open Service Order | Choose your service order and choose Edit. | The Edit Service Order screen displays. |  |
| 5 | Release Service Order Item | Under Items, locate a service item, for example, SRV_01.Make the following entires and choose Save:Status: Released | The service order item is released. |  |

##### Change Service Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how you can change an existing service order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A). | The Manage Service Order screen displays. |  |
| 3 | Find Service Order | Make the following entries and choose Go:Service Order: <ID> |  |  |
| 4 | Open Service Order | Choose your service order and choose Edit. | The Edit Service Order screen displays. |  |
| 5 | View Details | Under Items, choose Edit for the line item which contains the expense item SRV_02. | The details view of the expense item is displayed. |  |
| 6 | Maintain Data | Make the following entries:Amount: for example, 80 AEDChoose Apply.Choose Save. | The changes are saved. |  |
| 7 | Check Profit Center | Under Items, you can view the profit center for each item in the field Profit Center. | The profit center is determined automatically and can be changed manually.Note The system determines a profit center for each service order item of a service order. The system first determines the cost center of the employee responsible for the item and then the profit center that is defined for this cost center. You can also manually change the profit center assigned to a service order item.For more information, see [Profit Center Determination for Service Transactions](https://help.sap.com/viewer/adbae5bcd5994f159bf2847a11397b61/latest/en-US/4d5e9cef91ef46ed8eb75c8d90f32e94.html). |  |
| 8 | Add Stock Service Part | If this service order has been generated from the creation of a service quotation or a service order template, choose Edit.Make the following entries and choose Save:Product ID: for example, SRV_05Quantity: for example, 1Unit: for example, PC | The service order is saved. |  |

##### Release Service Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

In this step, you release the service order. It is a prerequisite for a follow-up confirmation of this order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A). | The Manage Service Order screen displays. |  |
| 3 | Find Service Order | Make the following entries and choose Go:Service Order: <ID> |  |  |
| 4 | Open Service Order | Choose your service order. | The Service Order screen displays. |  |
| 5 | Release Service Order | Choose Release under Change statusCheck the values under Planned Cost and Revenue. | Your service order is released.There should be values displayed for planned cost and revenue.You can create follow-up confirmations for all items of this service order. |  |

##### Create Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a follow-up service confirmation. You set the confirmation to completed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A). | The Manage Service Order screen displays. |  |
| 3 | Find Service Order | Make the following entries and choose Go:Service Order: <ID> |  |  |
| 4 | Open Service Order | Choose your service order. | The Service Order screen displays. |  |
| 5 | Create Service Confirmation | Choose Create Follow-Up > Confirm Items . | The Create Service Confirmation window displays. |  |
| 6 | Maintain Data | Make the following entries:Final Confirmation: YesExec. Service Employee: for example, 9980000xxxProduct ID: for example, SRV_01Quantity: for example, 1Unit: for example, HRProduct ID: for example, SRV_02Quantity: for example, 1Unit: for example, EAProduct ID: for example, SRV_05Quantity: for example, 1Unit: for example, PCSelect the required items using check boxChoose Save and Edit. | A new confirmation is created.Note Complete Billing:By default, the confirmed items are set for Complete Billing item categories:SCP1Service ItemSCW1Ext. Service ItemSCE1Expense Item orSCS1Service PartYou will be able to bill any item once all items of the service confirmation are completed and all item statuses are set to completed.Partial Billing:Alternatively, you can change the item category in the confirmation to Partial Billing:SCP3SrvItem (PrtBll)SCW3Ext. SrvItm (PrtBll)SCE3ExpItem (PrtBll) orSCS3SrvPart (PrtBll)This will allow you to bill a single item if it has been completed, even if other items have not been completed.Note Stock Service Part:If you are using a material with the item category group Stock Service Part (SVST), for example SRV_05, this material will be taken from the default storage location of the plant, which in this example is Std. storage 1 (331A). |  |
| 7 | Add Unplanned Item (Optional) | Under Items, choose Add Unplanned Item.Make the following entries and choose Add:Reference Service Order Item ID: <Item Number in Doc. 00010>Product ID: for example, SRV_01Quantity: for example, 1Unit: for example, HR | You can add additional items in a confirmation to include service efforts that were unplanned when the service order was created. Unplanned items will be considered in timesheet and cost accounting processes. |  |
| 8 | View Details | Under Items, choose Edit for your line item. | The Service Confirmation Item displays. |  |
| 9 | Set Overtime Category | Make the following enrties:Overtime Category: for example, Overtime WeekdayChoose ApplyNavigate back to Service Order Details. | Check the price details for the Price Element Overtime.By setting the overtime option, the price for the service item should have increased. |  |
| 10 | Complete the Service Confirmation | Make the following entries and choose Save:Status: Completed | The confirmation is set to Completed.Note Once the status Completed is set, it can no longer be changed; it is only possible to cancel.Since the final confirmation is set, the life cycle status of the service order is automatically set to Completed. This is the prerequisite for the items to be released for billing. |  |
| 11 | Check Life Cycle Status | Navigate back to the Manage Service Order screen and locate your service order. | The Life Cycle Status is set to Completed. |  |

##### Cancel Service Confirmation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you cancel a service confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A). | The Manage Service Order screen displays. |  |
| 3 | Find Service Order | Make the following entries and choose Go:Service Order: <ID> |  |  |
| 4 | Open Service Order | Choose your service order. | The Service Order screen displays. |  |
| 5 | Cancel Confirmation | Under Items, choose Confirmations.To cancel the service confirmation, choose ... > Cancel Confirmation .Select the item and choose Cancel Confirmation. |  |  |
| 6 | Check Item Status | Choose the service item under Items. | The field Cancelled Internally is Yes. |  |

##### Release Confirmation for Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release service items for billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Release For Billing (F3573). | The Release for Billing screen displays. |  |
| 3 | Find Item | Enter your Service Confirmation ID in the Search field and choose Go. |  |  |
| 4 | Release Item | Select an item and choose Release for Billing. | The selected items are release for billing. |  |

##### Create Billing Document (Invoice)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create an invoice for the service confirmation items that were released for billing in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to The SAP Fiori launchpad as a Billing Clerk. |  |  |
| 2 | Access App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings.In the Billing Settings dialog box, maintain the following settings and choose OK:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ON | The Billing Settings dialog window displays.You maintained the required settings for billing. |  |
| 4 | Select Items for Billing | Maintain the following entries and choose Go:SD Document Category: Billing Document RequestChoose the Settings icon.In View Settings, select BDR Source Document and choose OKFind your items in the list by identifying your service confirmation in the field BDR Source Document.In the Billing Due List Items list, select your billing document requests and choose Create Billing Documents.Note If you don’t want to display all billing due list items, you can restrict the list display by applying search criteria such as Sold-Party or Billing Date To. | The Create Billing Documents dialog box displays. |  |
| 5 | Select Billing Type and Billing Date | In the Create Billing Documents dialog window, make the following entries:Billing Type: F2 Invoice (F2)Billing Date: <today’s date>Choose OK | The F2 Invoice screen appears. |  |
| 6 | Save Billing Document | On the F2 Invoice screen, choose Save. | The billing document with ID xxxxxxxx is created.Note down the billing document number for future reference. |  |

#### Fixed Price Service Bundle

##### Create Service Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a service order with service bundle.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A). | The Manage Service Order screen displays. |  |
| 3 | Create Service Order | Choose Create Service Order → Quick Create. | The Create Service Order window displays. |  |
| 4 | Maintain Data | Make the following entries:Service Order Type: Service OrderSold-To Party: for example, 33100003Service Bundle: SelectedDescription: <your description>Requested Start Date - End Date: <date range>Product ID: for example, SRV_BUNDLE_01Quantity: for example, 1Unit: for example, HRChoose Save and Edit. | A new service order is created.Note down the service order number.Note If the service team concept has been enabled for the standard service order (SVO1), a popup window may appear and ask you to choose a service team. Select your service team. |  |
| 5 | Maintain Additional Data | Under Items, add an additional item for this service order:Product ID: for example, SRV_01Higher-Level Item: <service bundle item number>Quantity: for example, 1Unit: for example, HRProduct ID: for example, SRV_02Higher-Level Item: <service bundle item number>Quantity: for example, 1Unit: for example, EAPress Enter.Choose Save. | The service order is saved.Note By default, the item category for a fixed price service bundle is Service Bundle (FP) (SVB4). This means that you can only bill the service bundle upon completion.If you want to use partial billing for a service bundle, you must use the item category SrvcBndl (FPrc/PBll) (SVB6). |  |
| 6 | Release Service Order | On the Service Order screen, choose Release under Change Status. | The service order is released.You can create follow-up confirmations for all items of this service order. |  |

##### Create Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a follow-up service confirmation. You set the confirmation to completed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A). | The Manage Service Order screen displays. |  |
| 3 | Find Service Order | Make the following entries and choose Go:Service Order: <ID> |  |  |
| 4 | Open Service Order | Choose your service order. | The Service Order screen displays. |  |
| 5 | Create Service Confirmation | Choose Create Follow-Up > Create Service Confirmation . | The Create Service Confirmation window displays. |  |
| 6 | Maintain Data | Make the following entries:Final Confirmation: YesExec. Service Employee: for example, 9980000xxxProduct ID: for example, SRV_01Quantity: for example, 1Unit: for example, HRProduct ID: for example, SRV_02Quantity: for example, 1Unit: for example, EASelect the required items using check boxChoose Save and Edit. | A new confirmation is created.Note You can only confirm subitems. |  |
| 7 | View Details | Under Items, choose Edit for the expense line item (SRV_02). | The Service Confirmation Item displays. |  |
| 8 | Maintain Data | Make the following entries:Amount: for example, 80 AEDChoose Apply.Choose Save. | The changes are saved. |  |
| 9 | Complete the Service Confirmation | Make the following entries and choose Save:Status: Completed | The confirmation is set to Completed.Note Once the status Completed is set, it can no longer be changed; it is only possible to cancel.Since the final confirmation is set, the life cycle status of the service order is automatically set to Completed. This is the prerequisite for the items to be released for billing. |  |
| 10 | Check Life Cycle Status | Navigate back to the Manage Service Order screen and locate your service order. | The Life Cycle Status is set to Completed. |  |

##### Release Order for Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release service items for billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Release For Billing (F3573). | The Release for Billing screen displays. |  |
| 3 | Find Item | Enter your Service Confirmation ID in the Search field and choose Go. |  |  |
| 4 | Release Item | Select your service bundle item and choose Release for Billing. | The selected items are release for billing. |  |

##### Create Billing Document (Invoice)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create an invoice for the service confirmation items that were released for billing in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to The SAP Fiori launchpad as a Billing Clerk. |  |  |
| 2 | Access App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings.In the Billing Settings dialog box, maintain the following settings and choose OK:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ON | The Billing Settings dialog window displays.You maintained the required settings for billing. |  |
| 4 | Select Items for Billing | Maintain the following entries and choose Go:SD Document Category: Billing Document RequestChoose the Settings icon.In View Settings, select BDR Source Document and choose OKFind your items in the list by identifying your service confirmation in the field BDR Source Document.In the Billing Due List Items list, select your billing document requests and choose Create Billing Documents.Note If you don’t want to display all billing due list items, you can restrict the list display by applying search criteria such as Sold-Party or Billing Date To. | The Create Billing Documents dialog box displays. |  |
| 5 | Select Billing Type and Billing Date | In the Create Billing Documents dialog window, make the following entries:Billing Type: F2 Invoice (F2)Billing Date: <today’s date> | The F2 Invoice screen appears. |  |
| 6 | Save Billing Document | On the F2 Invoice screen, choose Save. | The billing document with ID xxxxxxxx is created.Note down the billing document number for future reference. |  |

#### Service Bundle

##### Create Service Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a serive order containing a service bundle. The order includes time and materials subitems as well as fixed price subitems.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A). | The Manage Service Order screen displays. |  |
| 3 | Create Service Order | Choose Create Service Order → Quick Create. | The Create Service Order window displays. |  |
| 4 | Maintain Data | Make the following entries:Service Order Type: Service OrderSold-To Party: for example, 33100003Service Bundle: SelectedDescription: <your description>Requested Start Date - End Date: <date range>Product ID: for example, SRV_BUNDLE_02Quantity: for example, 1Unit: for example, EAChoose Save and Edit. | A new service order is created.Note down the service order number.Note If the service team concept has been enabled for the standard service order (SVO1), a popup window may appear and ask you to choose a service team. Select your service team. |  |
| 5 | Maintain Additional Data | Under Items, add additional items for this service order:Product ID: SRV_01Higher-Level Item: <service bundle item number>Quantity: 1Unit: for example, HRProduct ID: SRV_02Higher-Level Item: <service bundle item number>Quantity: 1Unit: for example, EAProduct ID: SRV_01Higher-Level Item: <service bundle item number>Quantity: 1Unit: for example, HRItem Category: SrvItem (FxPrc)Note The item category is set to fixed price service item.Press Enter.Choose Save. | A service order with a service bundle including sub-items is created.Note You can create fixed price subitems for service item SRV_01 by using the item category SrvItem (FxPrc).Note The fixed price item will be billed from the service order. |  |
| 6 | Release Service Order | On the Service Order screen, choose Release under Change Status. | The service order is released.You can create follow-up confirmations for all items of this service order. |  |

##### Create Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a follow-up service confirmation. You set the confirmation to completed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A). | The Manage Service Order screen displays. |  |
| 3 | Find Service Order | Make the following entries and choose Go:Service Order: <ID> |  |  |
| 4 | Open Service Order | Choose your service order. | The Service Order screen displays. |  |
| 5 | Create Service Confirmation | Choose Create Follow-Up > Create Service Confirmation . | The Create Service Confirmation window displays. |  |
| 6 | Maintain Service Confirmation Data | Make the following entries:Final Confirmation: YesExec. Service Employee: for example, 9980000xxxProduct ID: for example, SRV_01Quantity: for example, 1Unit: for example, HRProduct ID: for example, SRV_02Quantity: for example, 1Unit: for example, EAProduct ID: for example, SRV_01Quantity: for example, 1Unit: for example, HRItem Category: SrvItem (FxPrc)Note The item category is set to fixed price service item.Select the required items using check boxChoose Save and Edit. | A new confirmation is created.Note You can only confirm subitems.Note Complete Billing:By default, the confirmed items are set for Complete Billing item categories:SCP1Service ItemSCW1Ext. Service ItemSCE1Expense Item orSCS1Service PartYou will be able to bill any item once all items of the service confirmation are completed and all item statuses are set to completed.Partial Billing:Alternatively, you can change the item category in the confirmation to Partial Billing:SCP3SrvItem (PrtBll)SCW3Ext. SrvItm (PrtBll)SCE3ExpItem (PrtBll) orSCS3SrvPart (PrtBll)This will allow you to bill a single item if it has been completed, even if other items have not been completed. |  |
| 7 | View Details | Under Items, choose Edit for the fixed price line item. | The Service Confirmation Item displays. |  |
| 8 | Maintain Data | Make the following entries:Actual Duration: for example, 2.00Choose Apply.Choose Save. | The changes are saved. |  |
| 9 | View Details | Under Items, choose Edit for the expense line item (SRV_02). | The Service Confirmation Item displays. |  |
| 10 | Maintain Data | Make the following entries:Amount: for example, 80 AEDChoose Apply.Choose Save. | The changes are saved. |  |
| 11 | Complete the Service Confirmation | Make the following entries and choose Save:Status: Completed | The confirmation is set to Completed.Note Once the status Completed is set, it can no longer be changed; it is only possible to cancel.Since the final confirmation is set, the life cycle status of the service order is automatically set to Completed. This is the prerequisite for the items to be released for billing. |  |
| 12 | Check Life Cycle Status | Navigate back to the Manage Service Order screen and locate your service order. | The Life Cycle Status is set to Completed. |  |

##### Release Order for Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release service items for billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Release For Billing (F3573). | The Release for Billing screen displays. |  |
| 3 | Find Item | Enter your Service Confirmation ID in the Search field and choose Go. |  |  |
| 4 | Release Item | Select your service bundle item and choose Release for Billing. | The selected items are release for billing. |  |

##### Create Billing Document (Invoice)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create an invoice for the service confirmation items that were released for billing in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to The SAP Fiori launchpad as a Billing Clerk. |  |  |
| 2 | Access App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings.In the Billing Settings dialog box, maintain the following settings and choose OK:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ON | The Billing Settings dialog window displays.You maintained the required settings for billing. |  |
| 4 | Select Items for Billing | Maintain the following entries and choose Go:SD Document Category: Billing Document RequestChoose the Settings icon.In View Settings, select BDR Source Document and choose OKFind your items in the list by identifying your service confirmation in the field BDR Source Document.In the Billing Due List Items list, select your billing document requests and choose Create Billing Documents.Note If you don’t want to display all billing due list items, you can restrict the list display by applying search criteria such as Sold-Party or Billing Date To. | The Create Billing Documents dialog box displays. |  |
| 5 | Select Billing Type and Billing Date | In the Create Billing Documents dialog window, make the following entries:Billing Type: F2 Invoice (F2)Billing Date: <today’s date> | The F2 Invoice screen appears. |  |
| 6 | Save Billing Document | On the F2 Invoice screen, choose Save. | The billing document with ID xxxxxxxx is created.Note down the billing document number for future reference. |  |

#### Service Bundle and Item with Billing Request Lines (Ad Hoc Billing)

##### Create Service Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A service bundle or an item can have one or several billing request lines if it is an ad hoc billing bundle or an ad hoc billing item. The billing request lines are entered manually in the billing plan with the item details. Each billing request line defines the amount to be charged and and at what date it should be due. As soon as the bundle or the item with billing request lines has been released for confirmation, a billing document request job run can create the corresponding billing document requests for it.

|  |
| --- |
| Note The following test procedure will include the order creation, the job run, and the invoice creation. It will skip the step of confirmation creation since it is not a key part of a billing plan process. |

In this step, you create the service order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A). | The Manage Service Order screen displays. |  |
| 3 | Create Service Order | Choose Create Service Order → Quick Create. | The Create Service Order window displays. |  |
| 4 | Maintain Data | Make the following entries:Service Order Type: Service OrderSold-To Party: for example, 33100003Service Bundle: SelectedDescription: <your description>Requested Start Date - End Date: <date range>Product ID: for example, SRV_BUNDLE_01Quantity: for example, 1Unit: for example, HRChoose Save and Edit. | A new service order is created.Note down the service order number.Note If your sold-to party is associated with one or more service contracts, a new popup window will appear and ask you to select a contract per item. Select No Assignment.If the service team concept has been enabled for the standard service order (SVO1), a popup window may appear and ask you to choose a service team. Select your service team. |  |
| 5 | Switch Item Category | Under Items, make the following entries:Item Category: SrvBndl (Ad Hoc Bll)Press Enter. | Note Switching the item category from SVB4 Service Bundle (FP) to SVB7 SrvBndl (Ad Hoc Bll) will enable this bundle item for ad hoc billing. |  |
| 6 | Maintain Additional Data | Under Items, add additional items for this service order:Product ID: SRV_01Higher-Level Item: <service bundle item number>Quantity: for example, 1Unit: for example, HRProduct ID: SRV_02Higher-Level Item: <service bundle item number>Quantity: for example, 1Unit: for example, EAChoose Enter. | The service bundle ad hoc billing contains two sub items.Only the bundle itself will be charged to the customer. |  |
| 6 | Add Ad Hoc Billing Item | Under Items, add an additional item for this service order:Product ID: SRV_01Higher-Level Item: <empty>Quantity: for example, 1Unit: for example, HRItem Category: SVP6 SrvItm (Ad Hoc Bill)Press Enter. | A service item has been added to the service order.Note Switching the item category from SVP1 Service Item to SVP6 SrvItm (Ad Hoc Bill) will enable this item for ad hoc billing.Note If your sold-to party is associated with one or more service contracts, a new popup window will appear and ask you to select a contract per item. Select No Assignment. |  |
| 7 | View Details | Choose Edit for the line item which contains the service bundle item SRV_BUNDLE_01. | The details view of the service bundle item displays. |  |
| 8 | Maintain Billing Request Lines | Under Billing Plan, choose Insert to add a billing request line:Billing Date: for example, <today + 1 working day>Billing Value: for example, 100Currency: AEDPress Enter.Choose Insert to add another billing request line:Billing Date: for example, <today + 20 working days>Billing Value: for example, 50Currency: AEDPress Enter.Choose Apply. | The billing request lines are added to the service bundle. |  |
| 9 | View Details | Under Items, choose Edit for the line item which contains the ad hoc billing service item SRV_01.Note Ensure you do not mix up the subitems of the service bundle. | The details view of the ad hoc service item displays. |  |
| 10 | Maintain Billing Request Lines | Under Billing Plan, choose Insert to add a billing request line:Billing Date: for example, <today + 1 working day>Billing Value: for example, 75Currency: AEDPress Enter.Choose Insert to add another billing request line:Billing Date: for example, <today + 20 working days>Billing Value: for example, 30Currency: AEDPress Enter.Choose Apply.Choose Save | Two billing request lines have been maintained for the service item. |  |
| 11 | Release Service Order | On the Service Order screen, Choose Release under Change Status. | The service order is released.You can create follow-up confirmations for all items of this service order. |  |

##### Schedule Job

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you schedule a job run to create billing document requests (BDRs) for the billing request lines.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Schedule Creation of Billing Document Requests Service Orders (F7257). | The Schedule Creation of Bililng Document Requests Service Orders screen displays. |  |
| 3 | Create a New Job | Choose Create.Make the following entries:Job Template: Schedule Creation of Billing Document Requests for Service OrdersJob Name: Schedule Creation of Billing Document Requests for Service OrdersChoose Step 2.Make the following entries:Start Immediately: SelectedChoose Step 3.Make the following entries:Service Order ID: <your service order ID>Billing Date: for example, <today + 7 days>Choose Schedule. | The job is scheduled. |  |
| 4 | Check Result | On the Schedule Creation of Bililng Document Requests Service Orders screen, choose the icon in the Log column of your job. | The Job Log screen displays.The entries display Message Type Success.Note Each entry represents a created billing document request.Note If the suggested date range is used (today + 7 days), only the first billing request line of the service bundle is considered. |  |

##### Create Billing Document (Invoice)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create an invoice for the billing document requests.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to The SAP Fiori launchpad as a Billing Clerk. |  |  |
| 2 | Access App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings.In the Billing Settings dialog box, maintain the following settings and choose OK:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ON | The Billing Settings dialog window displays.You maintained the required settings for billing. |  |
| 4 | Select Items for Billing | Maintain the following entries and choose Go:SD Document Category: Billing Document RequestChoose the Settings icon.In View Settings, select BDR Source Document and choose OKFind your items in the list by identifying your service confirmation in the field BDR Source Document.In the Billing Due List Items list, select your billing document requests and choose Create Billing Documents.Note If you don’t want to display all billing due list items, you can restrict the list display by applying search criteria such as Sold-Party or Billing Date To. | The Create Billing Documents dialog box displays. |  |
| 5 | Select Billing Type and Billing Date | In the Create Billing Documents dialog window, make the following entries:Billing Type: F2 Invoice (F2)Billing Date: <today’s date> | The F2 Invoice screen appears. |  |
| 6 | Save Billing Document | On the F2 Invoice screen, choose Save. | The billing document with ID xxxxxxxx is created.Note down the billing document number for future reference. |  |

### Fixed Price Order

This process variant differs from the previous ones with a fixed price set in the service order.

The story is about a typical service process from the perspective of the customer service manager and billing clerk.

#### Fixed Price Service Order

##### Create Service Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a fixed price service order.

|  |
| --- |
| Note You don't have to create a new service order if you have completed the test script for Service Quotation (4GA). If you created a service quotation, then a service order has been generated automatically. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A). | The Manage Service Order screen displays. |  |
| 3 | Create Service Order | Choose Create Service Order → Quick Create. | The Create Service Order window displays. |  |
| 4 | Maintain Data | Make the following entries:Service Order Type: Fixed Price Service OrderSold-To Party: for example, 33100003Description: <your description>Requested Start Date - End Date: <date range>Product ID: for example, SRV_01Quantity: for example, 1Unit: for example, HRChoose Save and Edit. | A new service order is created.Note down the service order number.NoteIf your sold-to party is associated with one or more service contracts, a new popup window will appear and ask you to select a contract per item. Select No Assignment.If the service team concept has been enabled for the fixed price service order (SVO2), a popup window may appear and ask you to choose a service team. Select your service team.Service material SRV_01 is usually assumed to be performed by an internal employee. If it must be procured from a 3rd party, scope item 3NI must be in scope. And you have to set the item category to SEW2 (Fixed Price Ext. Service Item). |  |
| 5 | Maintain a Fixed Price | Under Price Details, choose Add to insert a new Price Element.Choose Manual Doc. Amount (PMV0).Make the following entries:Price: for example, 600Unit: AEDPress Enter.Choose Save. | A fixed price is maintained for the service order.Note The total price on document level is calculated based on the fixed price. Item prices will be automatically adapted to reflect the total price proportionally.This total document price of the service order is relevant for billing. Service confirmations have no effect on the billing. |  |
| 6 | Release Service Order | On the Service Order screen, choose Release under Change Status. | The service order is released.You can create follow-up confirmations for all items of this service order. |  |

##### Create Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a follow-up service confirmation. You set the confirmation to completed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A). | The Manage Service Order screen displays. |  |
| 3 | Find Service Order | Make the following entries and choose Go:Service Order: <ID> |  |  |
| 4 | Open Service Order | Choose your service order. | The Service Order screen displays. |  |
| 5 | Create Service Confirmation | Choose Create Follow-Up > Create Service Confirmation . | The Create Service Confirmation window displays. |  |
| 6 | Maintain Data | Make the following entries:Final Confirmation: YesExec. Service Employee: for example, 9980000xxxProduct ID: for example, SRV_01Quantity: for example, 1Unit: for example, HRChoose Save and Edit. | A new confirmation is created. |  |
| 7 | Complete the Service Confirmation | Make the following entries and choose Save:Status: Completed | The confirmation is set to Completed.Note Once the status Completed is set, it can no longer be changed; it is only possible to cancel.Since the final confirmation is set, the life cycle status of the service order is automatically set to Completed. This is the prerequisite for the items to be released for billing. |  |
| 8 | Check Life Cycle Status | Navigate back to the Manage Service Order screen and locate your service order. | The Life Cycle Status is set to Completed. |  |

##### Release Order for Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release service items for billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Release For Billing (F3573). | The Release for Billing screen displays. |  |
| 3 | Find Item | Enter your Service Confirmation ID in the Search field and choose Go. |  |  |
| 4 | Release Item | Select your service bundle item and choose Release for Billing. | The selected items are release for billing. |  |

##### Create Billing Document (Invoice)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create an invoice for the service confirmation items that were released for billing in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to The SAP Fiori launchpad as a Billing Clerk. |  |  |
| 2 | Access App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings.In the Billing Settings dialog box, maintain the following settings and choose OK:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ON | The Billing Settings dialog window displays.You maintained the required settings for billing. |  |
| 4 | Select Items for Billing | Maintain the following entries and choose Go:SD Document Category: Billing Document RequestChoose the Settings icon.In View Settings, select BDR Source Document and choose OKFind your items in the list by identifying your service confirmation in the field BDR Source Document.In the Billing Due List Items list, select your billing document requests and choose Create Billing Documents.Note If you don’t want to display all billing due list items, you can restrict the list display by applying search criteria such as Sold-Party or Billing Date To. | The Create Billing Documents dialog box displays. |  |
| 5 | Select Billing Type and Billing Date | In the Create Billing Documents dialog window, make the following entries:Billing Type: F2 Invoice (F2)Billing Date: <today’s date> | The F2 Invoice screen appears. |  |
| 6 | Save Billing Document | On the F2 Invoice screen, choose Save. | The billing document with ID xxxxxxxx is created.Note down the billing document number for future reference. |  |

#### Fixed Price Service Bundle

##### Create Service Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a service order with service bundle.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A). | The Manage Service Order screen displays. |  |
| 3 | Create Service Order | Choose Create Service Order → Quick Create. | The Create Service Order window displays. |  |
| 4 | Maintain Data | Make the following entries:Service Order Type: Service OrderSold-To Party: for example, 33100003Service Bundle: SelectedDescription: <your description>Requested Start Date - End Date: <date range>Product ID: for example, SRV_BUNDLE_01Quantity: for example, 1Unit: for example, HRChoose Save and Edit. | A new service order is created.Note down the service order number.Note If the service team concept has been enabled for the fixed price service order (SVO2), a popup window may appear and ask you to choose a service team. Select your service team. |  |
| 5 | Maintain Additional Data | Under Items, add an additional item for this service order:Product ID: for example, SRV_01Higher-Level Item: <service bundle item number>Quantity: for example, 1Unit: for example, HRProduct ID: for example, SRV_02Higher-Level Item: <service bundle item number>Quantity: for example, 1Unit: for example, EAPress Enter.Choose Save. | The service order is saved. |  |
| 6 | Release Service Order | On the Service Order screen, Choose Release under Change Status. | The service order is released.You can create follow-up confirmations for all items of this service order. |  |

##### Create Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a follow-up service confirmation. You set the confirmation to completed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A). | The Manage Service Order screen displays. |  |
| 3 | Find Service Order | Make the following entries and choose Go:Service Order: <ID> |  |  |
| 4 | Open Service Order | Choose your service order. | The Service Order screen displays. |  |
| 5 | Create Service Confirmation | Choose Create Follow-Up > Create Service Confirmation . | The Create Service Confirmation window displays. |  |
| 6 | Maintain Data | Make the following entries:Final Confirmation: YesExec. Service Employee: for example, 9980000xxxProduct ID: for example, SRV_01Quantity: for example, 1Unit: for example, HRProduct ID: for example, SRV_02Quantity: for example, 1Unit: for example, EASelect the required items using check boxChoose Save and Edit. | A new confirmation is created.Note You can only confirm subitems. |  |
| 7 | View Details | Under Items, choose Edit for the expense line item (SRV_02). | The Service Confirmation Item displays. |  |
| 8 | Maintain Data | Make the following entries:Amount: for example, 90 AEDChoose Apply.Choose Save. | The changes are saved. |  |
| 9 | Complete the Service Confirmation | Make the following entries and choose Save:Status: Completed | The confirmation is set to Completed.Note Once the status Completed is set, it can no longer be changed; it is only possible to cancel.Since the final confirmation is set, the life cycle status of the service order is automatically set to Completed. This is the prerequisite for the items to be released for billing. |  |
| 10 | Check Life Cycle Status | Navigate back to the Manage Service Order screen and locate your service order. | The Life Cycle Status is set to Completed. |  |

##### Release Order for Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release service items for billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Release For Billing (F3573). | The Release for Billing screen displays. |  |
| 3 | Find Item | Enter your Service Confirmation ID in the Search field and choose Go. |  |  |
| 4 | Release Item | Select your service bundle item and choose Release for Billing. | The selected items are release for billing. |  |

##### Create Billing Document (Invoice)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create an invoice for the service confirmation items that were released for billing in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to The SAP Fiori launchpad as a Billing Clerk. |  |  |
| 2 | Access App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings.In the Billing Settings dialog box, maintain the following settings and choose OK:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ON | The Billing Settings dialog window displays.You maintained the required settings for billing. |  |
| 4 | Select Items for Billing | Maintain the following entries and choose Go:SD Document Category: Billing Document RequestChoose the Settings icon.In View Settings, select BDR Source Document and choose OKFind your items in the list by identifying your service confirmation in the field BDR Source Document.In the Billing Due List Items list, select your billing document requests and choose Create Billing Documents.Note If you don’t want to display all billing due list items, you can restrict the list display by applying search criteria such as Sold-Party or Billing Date To. | The Create Billing Documents dialog box displays. |  |
| 5 | Select Billing Type and Billing Date | In the Create Billing Documents dialog window, make the following entries:Billing Type: F2 Invoice (F2)Billing Date: <today’s date> | The F2 Invoice screen appears. |  |
| 6 | Save Billing Document | On the F2 Invoice screen, choose Save. | The billing document with ID xxxxxxxx is created.Note down the billing document number for future reference. |  |

#### Service Bundle and Item with Billing Request Lines (Ad Hoc Billing)

##### Create Service Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A service bundle or an item can have one or several billing request lines if it is an ad hoc billing bundle or an ad hoc billing item. The billing request lines are entered manually in the billing plan with the item details. Each billing request line defines the amount to be charged and and at what date it should be due. As soon as the bundle or the item with billing request lines has been released for confirmation, a billing document request job run can create the corresponding billing document requests for it.

|  |
| --- |
| Note The following test procedure will include the order creation, the job run, and the invoice creation. It will skip the step of confirmation creation since it is not a key part of a billing plan process. |

In this step, you create the service order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Orders - To-Do List (F3571A). | The Manage Service Order screen displays. |  |
| 3 | Create Service Order | Choose Create Service Order → Quick Create. | The Create Service Order window displays. |  |
| 4 | Maintain Data | Make the following entries:Service Order Type: Fixed Price Service OrderSold-To Party: for example, 33100003Service Bundle: SelectedDescription: <your description>Requested Start Date - End Date: <date range>Product ID: for example, SRV_BUNDLE_01Quantity: for example, 1Unit: for example, HRChoose Save and Edit. | A new service order is created.Note down the service order number.Note If your sold-to party is associated with one or more service contracts, a new popup window will appear and ask you to select a contract per item. Select No Assignment.If the service team concept has been enabled for the standard service order (SVO1), a popup window may appear and ask you to choose a service team. Select your service team. |  |
| 5 | Switch Item Category | Under Items, make the following entries:Item Category: SrvBndl (Ad Hoc Bll)Press Enter. | Note Switching the item category from SVB4 Service Bundle (FP) to SVB7 SrvBndl (Ad Hoc Bll) will enable this bundle item for ad hoc billing. |  |
| 6 | Maintain Additional Data | Under Items, add additional items for this service order:Product ID: SRV_01Higher-Level Item: <service bundle item number>Quantity: for example, 1Unit: for example, HRProduct ID: SRV_02Higher-Level Item: <service bundle item number>Quantity: for example, 1Unit: for example, EAChoose Enter. | The service bundle ad hoc billing contains two sub items.Only the bundle itself will be charged to the customer. |  |
| 6 | Add Ad Hoc Billing Item | Under Items, add an additional item for this service order:Product ID: SRV_01Higher-Level Item: <empty>Quantity: for example, 1Unit: for example, HRItem Category: SVP6 SrvItm (Ad Hoc Bill)Press Enter. | A service item has been added to the service order.Note Switching the item category from SVP1 Service Item to SVP6 SrvItm (Ad Hoc Bill) will enable this item for ad hoc billing.Note If your sold-to party is associated with one or more service contracts, a new popup window will appear and ask you to select a contract per item. Select No Assignment. |  |
| 7 | View Details | Choose Edit for the line item which contains the service bundle item SRV_BUNDLE_01. | The details view of the service bundle item displays. |  |
| 8 | Maintain Billing Request Lines | Under Billing Plan, choose Insert to add a billing request line:Billing Date: for example, <today + 1 working day>Billing Value: for example, 100Currency: AEDPress Enter.Choose Insert to add another billing request line:Billing Date: for example, <today + 20 working days>Billing Value: for example, 50Currency: AEDPress Enter.Choose Apply. | The billing request lines are added to the service bundle. |  |
| 9 | View Details | Under Items, choose Edit for the line item which contains the ad hoc billing service item SRV_01.Note Ensure you do not mix up the subitems of the service bundle. | The details view of the ad hoc service item displays. |  |
| 10 | Maintain Billing Request Lines | Under Billing Plan, choose Insert to add a billing request line:Billing Date: for example, <today + 1 working day>Billing Value: for example, 75Currency: AEDPress Enter.Choose Insert to add another billing request line:Billing Date: for example, <today + 20 working days>Billing Value: for example, 30Currency: AEDPress Enter.Choose Apply.Choose Save | Two billing request lines have been maintained for the service item. |  |
| 11 | Release Service Order | On the Service Order screen, Choose Release under Change Status. | The service order is released.You can create follow-up confirmations for all items of this service order. |  |

##### Schedule Job

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you schedule a job run to create billing document requests (BDRs) for the billing request lines.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Schedule Creation of Billing Document Requests Service Orders (F7257) | The Schedule Creation of Bililng Document Requests Service Orders screen displays. |  |
| 3 | Create a New Job | Choose Create.Make the following entries:Job Template: Schedule Creation of Billing Document Requests for Service OrdersJob Name: Schedule Creation of Billing Document Requests for Service OrdersChoose Step 2.Make the following entries:Start Immediately: SelectedChoose Step 3.Make the following entries:Service Order ID: <your service order ID>Billing Date: for example, <today + 7 days>Choose Schedule. | The job is scheduled. |  |
| 4 | Check Result | On the Schedule Creation of Bililng Document Requests Service Orders screen, choose the icon in the Log column of your job. | The Job Log screen displays.The entries display Message Type Success.Note Each entry represents a created billing document request.Note If the suggested date range is used (today + 7 days), only the first billing request line of the service bundle is considered. |  |

##### Create Billing Document (Invoice)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create an invoice for the billing document requests.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to The SAP Fiori launchpad as a Billing Clerk. |  |  |
| 2 | Access App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings.In the Billing Settings dialog box, maintain the following settings and choose OK:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ON | The Billing Settings dialog window displays.You maintained the required settings for billing. |  |
| 4 | Select Items for Billing | Maintain the following entries and choose Go:SD Document Category: Billing Document RequestChoose the Settings icon.In View Settings, select BDR Source Document and choose OKFind your items in the list by identifying your service confirmation in the field BDR Source Document.In the Billing Due List Items list, select your billing document requests and choose Create Billing Documents.Note If you don’t want to display all billing due list items, you can restrict the list display by applying search criteria such as Sold-Party or Billing Date To. | The Create Billing Documents dialog box displays. |  |
| 5 | Select Billing Type and Billing Date | In the Create Billing Documents dialog window, make the following entries:Billing Type: F2 Invoice (F2)Billing Date: <today’s date> | The F2 Invoice screen appears. |  |
| 6 | Save Billing Document | On the F2 Invoice screen, choose Save. | The billing document with ID xxxxxxxx is created.Note down the billing document number for future reference. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Scope Items

The following processes and conditions can precede this process.

| Scope Item | Business Condition |
| --- | --- |
| 4GA - Service Quotation | Optional |
| 4GT - Solution Order Management | Optional |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 43B - Service Monitoring and Analytics | Optional |
| 4GG - Credit and Debit Memo Processing for Service Management | Optional |
| J59 - Accounts Receivable |  |
| 3M3 - Event-Based Revenue Recognition – Service Documents |  |
| 3M4 - Event-Based Revenue Recognition – Service Documents – IFRS |  |
| 3M5 -Event-Based Revenue Recognition – Service Documents – US GAAP |  |

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
- related-to :: [[14-maintenance-service-and-projects/intercompany-billing-for-service-documents-53y-ae-test-script-1064]]
- related-to :: [[14-maintenance-service-and-projects/test-script-credit-and-debit-memo-processing-for-service-management-4g]]
- related-to :: [[10-procurement/test-script-procurement-for-service-management-3ni-ae-964]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3D2_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 141,675 chars in the whole document
