---
id: 14-maintenance-service-and-projects/test-script-sap-maintenance-assistant-4rv-sap-s-4hana-cloud-public-edi
title: "Test Script: SAP Maintenance Assistant (4RV) - SAP S/4HANA Cloud Public Edition (4RV_S4CLD2608_BPD_EN_XX)"
description: "Test script for SAP S/4HANA Cloud scope item 4RV (SAP Maintenance Assistant mobile app): prerequisites, roles, test data and procedures for MT, FST, FSM, forms."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/field-service-and-mobile-maintenance]
aliases: [4RV_S4CLD2608_BPD_EN_XX]
keywords: [Field Service Management and Mobile Maintenance, sap maintenance assistant, maintenance technician persona, field service technician persona, fsm integration, smartforms, dynamic forms, maintenance requests, maintenance operations, service orders]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4RV_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1050
topic: 14-maintenance-service-and-projects/field-service-and-mobile-maintenance
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: SAP Maintenance Assistant (4RV) - SAP S/4HANA Cloud Public Edition (4RV_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4RV_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Field Service Management and Mobile Maintenance** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | SAP Maintenance Assistant (4RV) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232832613)

[2 Prerequisites 5](#_Toc232832614)

[2.1 System Access 5](#_Toc232832615)

[2.2 Roles 5](#_Toc232832616)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232832617)

[2.4 Additional Manual Configuration 7](#_Toc232832618)

[2.5 Business Conditions 7](#_Toc232832619)

[2.6 Preliminary Steps 8](#_Toc232832620)

[2.6.1 Initial Device Setup 8](#_Toc232832621)

[3 Overview Table 10](#_Toc232832622)

[4 Test Procedures 14](#_Toc232832623)

[4.1 Maintenance Technician Persona Test Procedures 14](#_Toc232832624)

[4.1.1 List of Maintenance Orders 14](#_Toc232832625)

[4.1.2 List of Maintenance Operations 15](#_Toc232832626)

[4.1.3 Create Attachments for Maintenance Operations 16](#_Toc232832627)

[4.1.4 Enter Time Confirmation 17](#_Toc232832628)

[4.1.5 Complete Maintenance Operation Assigned To The Technician 18](#_Toc232832629)

[4.1.6 Complete Maintenance Operaation Assigned to the Work Center 19](#_Toc232832630)

[4.1.7 Create Maintenance Request 20](#_Toc232832631)

[4.1.8 Change Maintenance Request 21](#_Toc232832632)

[4.1.9 Report Malfunction Details 22](#_Toc232832633)

[4.1.10 Complete Maintenance Request for Minor Work 23](#_Toc232832634)

[4.1.11 Take Measurement Readings 24](#_Toc232832635)

[4.1.12 Create Attachment for Technical Object 25](#_Toc232832636)

[4.1.13 Create Follow-On Maintenance Request 26](#_Toc232832637)

[4.1.14 Issue an Unplanned Part 27](#_Toc232832638)

[4.1.15 Receive a Push Notification for an Operation 28](#_Toc232832639)

[4.1.16 Receive a Push Notification for a Maintenance Request with Action Required 29](#_Toc232832640)

[4.1.17 Create an Emergency Work Request 30](#_Toc232832641)

[4.1.18 Edit an Attachment 31](#_Toc232832642)

[4.1.19 Clear Reservations on Final Confirmation of an Operation 32](#_Toc232832643)

[4.1.20 Complete Operations Using the Consolidated Completion Flow 34](#_Toc232832644)

[4.1.21 Assign Operations as a Supervisor 35](#_Toc232832645)

[4.2 Field Service Technician Persona Test Procedures 36](#_Toc232832646)

[4.2.1 View the List of Service Orders 36](#_Toc232832647)

[4.2.2 View the List of Service Items 37](#_Toc232832648)

[4.2.3 View the List of Service Confirmations 37](#_Toc232832649)

[4.2.4 Create a Service Order 38](#_Toc232832650)

[4.2.5 Add a Service Order Item 39](#_Toc232832651)

[4.2.6 Create a Service Confirmation 40](#_Toc232832652)

[4.2.7 Add a Confirmation Item 42](#_Toc232832653)

[4.2.8 Complete a Service Confirmation 43](#_Toc232832654)

[4.2.9 Complete a Service Item 44](#_Toc232832655)

[4.2.10 Complete a Service Order 45](#_Toc232832656)

[4.2.11 View the List of Service Quotations 46](#_Toc232832657)

[4.2.12 View the List of Service Quotation Items 47](#_Toc232832658)

[4.2.13 Create a Service Quotation 48](#_Toc232832659)

[4.2.14 Add a Service Quotation Item 49](#_Toc232832660)

[4.2.15 Set the Assignment Type for Service Orders 50](#_Toc232832661)

[4.2.16 FSM Integration - Download Service Technician Assignments from FSM to SAP Maintenance Assistant 51](#_Toc232832662)

[4.2.17 FSM Integration - Download Smartforms Attached to an Activity from FSM to SAP Maintenance Assistant 53](#_Toc232832663)

[4.2.18 FSM Integration - Edit Smartforms Downloaded from FSM 54](#_Toc232832664)

[4.2.19 FSM Integration - Complete Smartforms Downloaded from FSM 55](#_Toc232832665)

[4.2.20 FSM Integration - Mobile Status Updates from SAP Maintenance Assistant to FSM 56](#_Toc232832666)

[4.2.21 FSM Integration - Location Tracking Updates from SAP Maintenance Assistant to FSM 57](#_Toc232832667)

[4.3 Dynamic Forms Test Procedures 58](#_Toc232832668)

[4.3.1 Publish Form, Create Form Instances, and Fetch Forms to the Mobile Application 58](#_Toc232832669)

[4.3.2 Complete Forms 60](#_Toc232832670)

[4.3.3 Required Forms 61](#_Toc232832671)

[4.3.4 Open, Update, and Save Form 62](#_Toc232832672)

[5 Appendix 63](#_Toc232832673)

[5.1 Process Integration 63](#_Toc232832674)

[5.1.1 Preceding Processes 63](#_Toc232832675)

## Purpose

Overview

This scope item enables a maintenance technician to improve workplace safety, optimize asset life, and ensure reliability. It also helps to streamline processes by eliminating paperwork. The mobile app accesses asset management in SAP S/4HANA Cloud Public Edition and empowers the workforce to inspect, maintain, and repair assets in the field from their mobile devices.

In SAP Maintenance Assistant, the Field Service Technician persona empowers technicians to deliver efficient and reliable service. It streamlines task execution, optimizes resource utilization, and improves the technician's work experience. This new persona enables technicians to access service orders, update service tasks, capture and update critical data, and collaborate on their mobile devices. SAP Maintenance Assistant also supports the SAP S/4HANA Service Quotation feature. Users can create service quotations and service quotation items from the mobile application.

Integration with SAP Field Service Management (FSM) for dispatching and planning helps to reduce manual processes and enhance field productivity and operational efficiency. With this release, SAP Maintenance Assistant supports FSM integration with the Maintenance Technician persona. The SmartForms feature is now supported for both Maintenance Technician and Field Service Technician personas.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/4RV_S4CLD2602_BPD_EN_XX.docx)). |

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | The SMA app can be installed either on an IOS or Android device. The system administrator will provide a link to the app and an onboarding URL or QR code to install the app |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

The SAP Maintenance Assistant app will use the same set of roles as defined in the SAP S/4HANA Cloud Public Edition system. Therefore, it is assumed that the back end business user is already set up before using the app.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Maintenance Technician | SAP_BR_MAINTENANCE_TECHNICIAN | Maintenance Execution | SAP_EAM_SP_MAINT_TECHNICIAN |  |
| Employee | SAP_BR_EMPLOYEE | Self Services / Self Services / Employee Overview Space | SAP_HCM_SP_EMPLOYEE |  |
| Customer Service Manager (Customer Management) | SAP_BR_CUSTOMER_SRVC_MGR | Customer Service Manager | SAP_BR_CUSTOMER_SRVC_MGR |  |
| Service Technician - Customer Service | SAP_BR_CUSTOMER_SRVC_TEC | Service Processing | SAP_BR_CUSTOMER_SRVC_TEC |  |
| Configuration Expert (Maintenance Assistant) | SAP_BR_MAIF_CONFIG_EXPERT | MAO - Configuration for SMA | SAP_MAO_SPT_MAIF_MOBILE_CONFIG_PC |  |
| Administrator (Maintenance Assistant) | SAP_BR_MAIF_MOBILE_ADMIN | Administration - Mobile Integration | SAP_EAM_PGT_MAIF_MBL_ADMIN_PC |  |
| Maintenance Supervisor | SAP_BR_MAINT_SUPERVISOR | Maintenance Supervision | SAP_BR_MAINTENANCE_SUPERVISOR |  |

To access the SAP Maintenance Assistant app with the Field Service Technician persona, you must also create a custom business role. For more information, refer to procedure Create a New Business Role to Access the Field Service Technician Persona found in the Set-Up Instructions for the 4RV scope item.

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Equipment | 211100091 | Cooling Water Circulation Pump |  |
| Equipment | 211100093 | Cooling Water Circulation Pump |  |
| Spare Parts Material | SP001 | Bearing |  |
| Spare Parts Material | SP002 | Coupling |  |
| Spare Parts Material | SP003 | Shaft |  |
| Spare Parts Material | SP004 | Gaskets 1mm |  |
| Spare Parts Material | SP005 | Mechanical Seal |  |
| Spare Parts Material | SP006 | Spur gear IS651 |  |
| Plant | 1110 | Plant 1 GB |  |
| Storage Location | 111B | Std. storage 2 |  |

Use the Fiori Personalization app to specify the following properties for your user. Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Planning Plant | 1710 | Plant 1 US |  |
| Main Work Center | RES-0200 / 1710 | Electric |  |

Field Service Technician Persona

For the Field Service Technician user case, you can set a default value in Fiori by logging in with the business user that has S/4 service with the Field Service Technician role assigned (see the [Roles](#unique_4) [page ] 5 topic). Click on the Profile icon of the user in the top right corner of Fiori, then navigate to Default Values. Specifiy the Sales Org value under the Sales and Billing section.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Sales Org | 1710 | Dom, Sales Org US |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/049e55cd74a754b0774275593221e973)

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 4HH – Reactive Maintenance | The steps executed by the maintenance technician role in the Reactive Maintenance process flow must be configured and working correctly in the SAP S/4HANA Cloud Public Edition system |
| 4HI – Proactive Maintenance | The steps executed by the maintenance technician role in the Proactive Maintenance process flow must be configured and working correctly in the SAP S/4HANA Cloud Public Edition system |
| 4VT – Improvement Maintenance | The steps executed by the maintenance technician role in the Improvement Maintenance process flow must be configured and working correctly in the SAP S/4HANA Cloud Public Edition system |
| 4WM – Operational and Overhead Maintenance | The steps executed by the maintenance technician role in the Operational and Overhead Maintenance process flow must be configured and working correctly in the SAP S/4HANA Cloud Public Edition system |
| Field Service Techncian Persona | Note The following business conditions must be met only if you are testing the scope item with the Field Service Technician persona. |
| 3D2 - Service Order Management and Monitoring | The steps executed by the service technician / service manager role in the Service Order Management and Monitoring process flow must be configured and working correctly in the SAP S/4HANA Cloud Public Edition system |
| 49X - Service Order Processing with SAP Field Service Management | The steps executed by the FSM dispatcher / service technician in the Service Order Processing with SAP Field Service Management process flow must be configured and working correctly in the SAP S/4HANA Cloud Public Edition system |

### Preliminary Steps

#### Initial Device Setup

Use

This step is used to set up the device and perform the initial synchronization. An iOS and/or Android device can be used.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Install app | Use the link provided by the system administrator to install the app on the device.Note that different links will be provided for iOS and Android devices | The app is installed on the device |  |
| 2 | Access the App | Option 1: Using On-boarding URLClick on the On-boarding URL provided by your system administrator. When prompted, click on Open. This will launch the app. Then perform the following steps:Confirm EULA / Privacy StatementProactively trigger Start.Select Use current application.Supply valid User ID and PasswordChoose and confirm a User PasscodeVerify that the initial sync process is initiatedOption 2: Using On-boarding QR codeLaunch the appConfirm EULA / Privacy StatementUse the <Scan>button to scan the QR code providedIn the pop-up to allow camera access, click OK.In the pop-up, select your preference.After the scan is successful, click Continue.Supply valid User ID and PasswordChoose and confirm a User PasscodeVerify that the initial sync process is initiated | After the sync completes, the initial screen of the app is displayed |  |
| 3 | Switch the persona | From the side navigation panel, go to Profile Settings.Use the dropdown Switch Persona to switch between the Maintenance Service Technician persona and the Field Service Technician persona. The default persona selected is Maintenance Technician.Note Be sure that the required roles are assigned per the [Roles](#unique_4) [page ] 5 topic. | The persona on the device is switched from the default Maintenance Technician persona to the Field Service Technician persona |  |

Result

The SAP Maintenance Assistant app is initialized and ready to use.

## Overview Table

This scope item consists of several process steps provided in the table below.

| ID (Role Template) | Name (Role Template) | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| List of Maintenance Orders | Maintenance Technician | SAP Maintenance Assistant | List of Maintenance Orders for the Operations of the users’ WorkCenter are downloaded to the SMA app |
| List of Maintenance Operations | Maintenance Technician | SAP Maintenance Assistant | List of Maintenance Operations for the users’ WorkCenter are downloaded to the SMA app |
| Create Attachment for Maintenance Operations | Maintenance Technician | SAP Maintenance Assistant | An attachment is created for the Maintenance Order operation |
| Enter Time Confirmation | Maintenance Technician | SAP Maintenance Assistant | A PM confirmation is created for the Maintenance Operation |
| Complete Maintenance Operation assigned to the technician | Maintenance Technician | SAP Maintenance Assistant | The Maintenance operation assigned to the technician in Completed |
| Complete Maintenance Operation assigned to the Work Center | Maintenance Technician | SAP Maintenance Assistant | The Maintenance operation assigned to the technician’s Work Center in Completed |
| Create Maintenance Request | Maintenance Technician | SAP Maintenance Assistant | A new Maintenance Request is created |
| Change Maintenance Request | Maintenance Technician | SAP Maintenance Assistant | A Maintenance Request is modified |
| Report Malfunction Details | Maintenance Technician | SAP Maintenance Assistant | The Maintenance Operation is completed, and Malfunction details for the corresponding Maintenance Notification are saved |
| Complete Maintenance Request for Minor work | Maintenance Technician | SAP Maintenance Assistant | A Maintenance Request is created and then completed |
| Take Measurement Readings | Maintenance Technician | SAP Maintenance Assistant | A Measurement Document is created for each Measurement point that is read |
| Create Attachment for Technical Object | Maintenance Technician | SAP Maintenance Assistant | An attachment is created for the Technical Object |
| Create Follow-On Maintenance Request | Maintenance Technician | SAP Maintenance Assistant | A follow-on maintenance request is created |
| Issue an Unplanned Part | Maintenance Technician | SAP Maintenance Assistant | An unplanned part is issued for an operation |
| Receive a Push Notification for an Operation | Maintenance TechnicianMaintenance Planner | SAP Maintenance AssistantMaintenance Scheduling Board | When an operation on a Very High work order is dispatched, a push notification is received on the SAP Maintenance Assistant client with the new operation. |
| Receive a Push Notification for a Maintenance Request with Action Required | Maintenance TechnicianMaintenance Supervisor | SAP Maintenance AssistantScreen Maintenance Requests | When a reactive maintenance request with a Very High priority is set to the Action Required state, a push notification is received on the SAP Maintenance Assistant client with the updated maintenance request. |
| Create a Minor Work Request | Maintenance Supervisor | SAP Maintenance AssistantCreate Maintenance Request | A minor work request is created and automatically approved. It can be completed from the SAP Maintenance Assistant application. |
| Set Assignment Type for Service Orders | Configuration Expert (Maintenance Assistant) | Manage Mobile App Configurations (for SAP Maintenance Assistant) | Assignment Type is for fetching service data |
| List of Service Orders | Service Technician - Customer ServiceCustomer Service Manager | SAP Maintenance Assistant | List of service orders that match the assignment type criteria are downloaded to the SAP Maintenance Assistant appllication |
| List of Service Items | Service Technician - Customer ServiceCustomer Service Manager | SAP Maintenance Assistant | List of service items that match the assignment type criteria are downloaded to the SAP Maintenance Assistant appllication |
| List of Service Confirmations | Service Technician - Customer ServiceCustomer Service Manager | SAP Maintenance Assistant | List of service confirmations for the service orders are downloaded to the SAP Maintenance Assistant application |
| List of Service Quotations | Service Technician - Customer ServiceCustomer Service Manager | SAP Maintenance Assistant | List of service quotations that match the assignment type criteria are downloaded to the SAP Maintenance Assistant application |
| List of Service Quotation Items | Service Technician - Customer ServiceCustomer Service Manager | SAP Maintenance Assistant | List of service quotation items that match the assignment type criteria are downloaded to the SAP Maintenance Assistant application |
| Creating a Service Quotation | Customer Service Manager | SAP Maintenance Assistant | A new service quotation is created |
| Adding a Service Quotation | Customer Service Manager | SAP Maintenance Assistant | A new service quotation item is created |
| Creating a Service Order | Customer Service Manager | SAP Maintenance Assistant | A new service order is created |
| Adding a Service Order Item | Customer Service Manager | SAP Maintenance Assistant | A new service item is added |
| Creating a Confirmation | Service Technician - Customer ServiceCustomer Service Manager | SAP Maintenance Assistant | A new service confirmation is created |
| Adding a Confirmation Item | Service Technician - Customer ServiceCustomer Service Manager | SAP Maintenance Assistant | A new confirmation item is added |
| Completing a Service Confirmation | Service Technician - Customer ServiceCustomer Service Manager | SAP Maintenance Assistant | A service confirmation is set to Completed and removed from the client |
| Completing a Service Item | Customer Service Manager | SAP Maintenance Assistant | A service item is set to Completed and removed from the client |
| Completing a Service Order | Customer Service Manager | SAP Maintenance Assistant | A service order is set to Completed and removed from the client. This will also set any Open service items to Completed. |
| Setting the Assignment Type for Service Orders | Service Technician - Customer Service | SAP Maintenance AssistantManage Mobile Application Configuration (for SAP Maintenance Assistant) | An assignment type is set for fetching service orders and items |
| Download Service Technician assignments from FSM to SAP Maintenane Assistant | Service Technician - Customer ServiceCustomer Service Manager | SAP Maintenance AssistantFSM Planning and Dispatching Board | Assigned techncian in FSM should be replicated as Exec Service Employee in SAP Maintenance Assistant |
| Download Smartforms attached to an activity or service call from FSM to SAP Maintenance Assistant | Service Technician - Customer ServiceCustomer Service Manager | SAP Maintenance AssistantFSM Planning and Dispatching Board | Smartforms attached to an activity or service call in FSM are downloaded to the corresponding maintenance or service object in SAP Maintenance Assistant |
| Edit Smartforms downloaded from FSM | Service Technician - Customer ServiceCustomer Service Manager | SAP Maintenance AssistantFSM Planning and Dispatching Board | Smartforms downloaded to SAP Maintenance Assistant should be editable provided they're not in a Completed status and are assigned to a logged-in technician user |
| Complete Smartforms downloaded from FSM | Service Technician - Customer ServiceCustomer Service Manager | SAP Maintenance AssistantFSM Planning and Dispatching Board | Smartforms on service or maintenance objects can be completed and synced to FSM Planning and Dispatching Board |
| Mobile status updates from SAP Maintenance Assistant to FSM | cCustomer Service Manager | SAP Maintenance AssistantFSM Planning and Dispatching Board | Mobile status updates on service items are replicated from SAP Maintenance Assistant to FSM Activities |
| Location tracking updates from SAP Maintenance Assistant to FSM | Service Technician - Customer ServiceCustomer Service ManagerConfiguration Expert (Maintenance Assistant) | SAP Maintenance AssistantFSM Planning and Dispatching BoardManage Mobile Application Configuration | Technician location updates are replicated from SAP Maintenance Assistant to FSM Service Map |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Maintenance Technician Persona Test Procedures

#### List of Maintenance Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used by the Maintenance Technician to review the list of Maintenance Orders for the Operations of the users’ Work Center

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SMA app | Launch the SMA app and logon using the passcode or touch id | The Overview page is displayed |  |
| 2 | Review Maintenance Order List | Tap on Work Orders from the Overview page | The list of Work Orders assigned to the logged in Maintenance Technician are displayed |  |
| 3 | Review Maintenance Order Details | Tap on any Work Order in the ListIn the Work Order Details screen, review the order details by tapping on the following sections:OperationsMaintenance RequestTechnical ObjectsPartsDocumentsNotes | The Work Order details screen is displayed with the following information:OperationsMaintenance Request assigned to the orderTechnical ObjectsParts / Components assigned to the orderDocuments attached to the orderLong Text / Notes |  |

#### List of Maintenance Operations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used by the Maintenance Technician to review the list of Maintenance Operations of the users’ Work Center

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SMA app | Launch the SMA app and logon using the passcode or touch id | The Overview page is displayed |  |
| 2 | Review Maintenance Operation List | Tap on Operations from the Overview page | The list of Operations for the users’ Work Center are displayed |  |
| 3 | Review Maintenance Order Details | Tap on any Operation in the ListIn the Operation Details screen, review the operation details by tapping on each of the following sections:Work Order (Maintenance Order)Technical ObjectPartsDocumentsNotesRelated Maintenance Requests | The Operation details screen is displayed with the following information:Work Order (Maintenance Order)Technical ObjectParts / ComponentsDocumentsLong Text / NotesRelated Maintenance Requests |  |

#### Create Attachments for Maintenance Operations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used by the Maintenance Technician add attachments to the Operations of a Maintenance Order

Procedure

Table 1:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SMA app | Launch the SMA app and logon using the passcode or touch id | The Overview page is displayed |  |
| 2 | Add attachment(s) to the Maintenance Operations | Tap on Work Orders from the Overview pageTap on any Order in the ListIn the Work Order Details screen, tap on the Operations section to go to the Operation List screenIn the Operations List screen tap on a specific Operation to go to the Operations Details screenTap on the Documents section in the Operations Details screenAdd the attachment by tapping on the + button and add the Attachment Description and then tap on the Done buttonTap on the Sync button on the top right of the pageIt is also possible to navigate directly to the Operation via Operations on the Overview page as explained in Section 4.2 | The attachments added to the Maintenance Operations are posted to the backend during the sync |  |

#### Enter Time Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used by the Maintenance Technician to enter the Time Confirmations for a Maintenance Order or Operation

Procedure

Table 2:

| Test Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SMA app | Launch the SMA app and logon using the passcode or touch id | The Overview page is displayed |  |
| 2 | Enter Time Confirmation | Tap on Work Orders from the Overview pageTap on any Work Order in the ListIn the Maintenance Order Details screen, tap on the Operations section to go to the Operation List screenIn the Operations List screen tap on a specific Operation to go to the Operations Details screenIn the Maintenance Operation Details screen, tap on the Ready for Execution and then the Start button at the bottom of the screenTap on the Work Paused and then the Hold button at the bottom of the screenThe Confirm Status Change pop-up appears. Tap on OK.The Time Confirmation screen is displayed – enter the relevant data and tap on DoneTap on the Sync button on the top right of the pageNote It is also possible to navigate directly to the Operation via Operations on the Overview page as explained in Section 4.3 | The time confirmation is posted to the backend during the sync |  |

#### Complete Maintenance Operation Assigned To The Technician

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used by the Maintenance Technician to complete a Maintenance Operation assigned to them

Procedure

Table 3:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SMA app | Launch the SMA app and log on using the passcode or touch ID | The Overview page is displayed |  |
| 2 | Start and complete the operation | Tap on Maintenance Operations from the Overview pageFrom the Maintenance Operations list, tap on the operation assigned to the technicianIn the Maintenance Operation Details screen, tap on the Ready for Execution button and then the Start Operation button at the bottom of the screenTap on the Work in Execution button and then the End Operation button at the bottom of the screenOptional: Enter Malfunction detailsOptional: Enter time confirmationTap on the Sync button on the top right of the page | The Maintenance Operation is posted to the back end with CNF status during the sync |  |

#### Complete Maintenance Operaation Assigned to the Work Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used by the Maintenance Technician to complete a Maintenance Operation assigned to them

Procedure

Table 4:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SMA app | Launch the SMA app and log on using the passcode or Touch ID | The Overview page is displayed |  |
| 2 | Start and Complete the operation | Tap on Maintenance Operations from the Overview pageFrom the Maintenance Operations list, tap on any operation that is unassignedIn the Maintenance Operation Details screen, tap on the Ready for Execution button and then the Start button at the bottom of the screenTap on the Work in Execution button and then the End Operation button at the bottom of the screenOptional: Enter Malfunction detailsOptional: Enter time confirmationTap on the Sync button on the top right of the page | The Maintenance Operation is posted to the back end with CNF status during the sync |  |

#### Create Maintenance Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used by the technician to create a Maintenance Request

Procedure

Table 5:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SMA app | Launch the SMA app and log on using the passcode or Touch ID | The Overview page is displayed |  |
| 2 | Create a maintenance request without minor work | Navigate to the Maintenance Requests List page by tapping on Maintenance Requests in the Overview pageTap on the + button on the top right corner of the pageEnter all the details on the page.The fields are either free text or drop-down fields which depend on other fields on the screen.Do not select the Minor Work optionPriority can either be entered manually or using the Assess Priority option – Tap on the Assess Priority button. This option is only relevant when a Technical Object is selected and the Notification Type is Y1. Tap on the Assess Priority button and enter details for this operation.Long text can be entered using free text or using the Long Text template – Tap on the Use Template button for this optionAttachments can also be added by clicking on the + button in the Attached Files section and adding an Attachment DescriptionAfter entering all the fields, tap on the Done buttonTap on the Sync button on the top right of the page | A local maintenance request is created on the SMA application and posted to the back end during the sync |  |

#### Change Maintenance Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used by the technician to change a Maintenance Request

Procedure

Table 6:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SMA app | Launch the SMA app and log on using the passcode or Touch ID | The Overview page is displayed |  |
| 2 | Change Maintenance Request | Navigate to the Maintenance Requests List page by tapping on Maintenance Requests in the Overview pageTap on a Maintenance Request to navigate to the details pageTap on the Edit button on the top right corner of the pageChange the required details and tap on the Done buttonTap on the Sync button on the top right of the page | The changes to the maintenance request are posted to the back end during sync |  |

#### Report Malfunction Details

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used by the Maintenance Technician to complete a Maintenance Operation and enter Malfunction Details as part of the Completion process

Procedure

Table 7:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SMA app | Launch the SMA app and log on using the passcode or Touch ID | The Overview page is displayed |  |
| 2 | Start, Complete, and enter malfunction details on an operation | Tap on Maintenance Operations from the Overview pageFrom the Maintenance Operations list, tap on any operationIn the Maintenance Operation Details screen, tap on Ready for Execution button and then the Start Operation button at the bottom of the screenTap on the Work in Execution button and then the End Operation button at the bottom of the screenWhen prompted, enter the Malfunction details for the Maintenance RequestOptional: Enter time confirmation as part of complete Maintenance OrderTap on the Sync button on the top right of the page | The Maintenance Operation is posted to the back end with CNF status during the sync. An item is added to the corresponding Maintenance Request |  |

#### Complete Maintenance Request for Minor Work

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used by the technician to create and complete a Maintenance Request for Minor Work

Procedure

Table 8:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SMA app | Launch the SMA app and log on using the passcode or Touch IDLog in with a user that has the Maintenance Supervisor role (SAP_BR_MAINT_SUPERVISOR) assigned. | The Overview page is displayed |  |
| 2 | Create Maintenance Request for Minor Work | Navigate to the Maintenance Requests List page by tapping on Maintenance Requests in the Overview pageTap on the + button on the top right corner of the pageEnter all the details on the page.The fields are either free text or drop-down fields which depend on other fields on the screen.Select the Minor Work option.Priority can either be entered manually or using the Assess Priority option (this option is only relevant when a technical object is selected and the Notification Type is Y1). Tap on the Assess Priority button and enter the details for this optionLong text can be entered using free text or using the Long Text template – Tap on the Use Template button for this optionAttachments can also be added by clicking on the + button in the Attached Files section and adding an Attachment DescriptionAfter entering all the fields, tap on the Done button | A local maintenance report is created on the SMA app |  |
| 3 | Complete the Maintenance Request | Select the newly created Maintenance Request from the Maintenance Requests List screen and tap on it.Tap on the Complete Maintenance Request button at the bottom of the screen.Tap OK on the pop-up screen to confirm the status change.Tap on the Sync button on the top right of the page | The status of the maintenance request is set to Completed. The local Maintenance Request is posted to the back end during the sync. The system status of the notification is set to NICO in the back end. |  |

#### Take Measurement Readings

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used by the Maintenance Technician to take Measurement Readings for Technical Objects

Procedure

Table 9:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SMA app | Launch the SMA app and log on using the passcode or Touch ID | The Overview page is displayed |  |
| 2 | Take Measurement Readings | Tap on Technical Objects from the Overview pageTap on any Technical Object in the ListTap on the … button on the top right corner and then tap on theTake Readings option in the MenuEnter the Measurement Readings for all the points. TheSkip option can be set in case the points don’t need to be read.After entering the readings tap on the Done buttonTap on the Sync button on the top right of the page | The Measurement documents are saved locally and posted to the back end during sync |  |

#### Create Attachment for Technical Object

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used by the Maintenance Technician to attach a document to a Technical object

Procedure

Table 10:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SMA app | Launch the SMA app and log on using the passcode or Touch ID | The Overview page is displayed |  |
| 2 | Create Attachment for Technical Object | Tap on Technical Objects from the Overview pageTap on any Technical Object in the ListTap on the Edit button on the top right cornerAdd the attachment by tapping on the + button and enter the Attachment Description and then tap on the Done buttonTap on the Sync button on the top right of the page | The attachment is added to the equipment in the back end during the sync. |  |

#### Create Follow-On Maintenance Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used by the Maintenance Technician to create a follow-on maintenance request.

Procedure

Table 11:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SMA app | Launch the SMA app and log on using the passcode or Touch ID | The Overview page is displayed |  |
| 2 | Create Attachment for Technical Object | Tap on Work Orders from the Overview pageTap on any work order in the listTap the + button and choose Add Follow-On Request.Enter all the details on the page:The fields are either free text or drop-down fields. Drop-down field choices can vary depending on previous field entries.Priority can either be entered manually or by using the Assess Priority option. The Assess Priority option is only relevant when a technical object is selected and the Notification Type is Y1. Enter any details for this option.Long text can be entered using free text or by using the long text template. Tap on the Use Template button for this option.Attachments can be added by clicking on the + button in the Attached Files section and adding an attachment description.After entering all the fields, tap on the Done buttonTap on the Sync button on the top right of the page | A follow-on maintenance request is created and posted to the back end after syncing. |  |

#### Issue an Unplanned Part

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used by the Maintenance Technician to create a follow-on maintenance request.

Procedure

Table 12:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SMA app | Launch the SMA app and log on using the passcode or Touch ID | The Overview page is displayed |  |
| 2 | Create Attachment for Technical Object | Tap on Operations from the Overview pageTap on any operation in the listTap the + button and choose Issue Unplanned Part.Enter a Plant and Storage Location.Press the Online Search button.Search for a material by entering a material number or description.Select a material from the list.Enter a Unit of Measure and Quantity.Tap on the Done button. You will see the unplanned part added to the Unplanned Parts list.Tap on the Sync button on the top right of the page | An unplanned part is issued for an operation. |  |

#### Receive a Push Notification for an Operation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used to notify the Maintenance Technician when a Very High priority operation has been dispatched.

Procedure

Table 13:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SMA app | Launch the SMA app and log on using the passcode or Touch IDWhen prompted to allow push notifications, choose Yes. | The Overview page is displayed |  |
| 2 | Log on to the SAP S/4HANA Cloud Public Edition tenant | Log on to the SAP Fiori launchpad as a user with the business role Maintenance Planner | The SAP Fiori launchpad is displayed |  |
| 3 | Create an operation in Fiori | In the SAP Fiori launchpad, create an operation on a work order with priority Very High.Assign the operation to the user you logged in to the SAP Maintenance Assistant application with. | An operation is created |  |
| 4 | Dispatch the operation | In the SAP Fiori launchpad, open the Maintenance Scheduling Board (F2603) application.Find the operation you created.Dispatch the operation. | The operation is dispatched |  |
| 5 | Receive the push notification | On the device running SAP Maintenance Assistant, you should receive a push notification informing you of the new work order / operation.When prompted, choose to download the new data. | New data is downloaded to the SAP Maintenance Assistant application. The operation you created in the SAP Fiori launchpad is now present on the application. |  |

#### Receive a Push Notification for a Maintenance Request with Action Required

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used to notify the Maintenance Technician when a Very High priority maintenance request has been set to the Action Required state.

Procedure

Table 14:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SMA app | Launch the SMA app and log on using the passcode or Touch IDWhen prompted to allow push notifications, choose Yes. | The Overview page is displayed |  |
| 2 | Create a Maintenance Request | In the SAP Maintenance Assistant application, create a maintenance request of type Y1 - Reactive Work with a priority of Very High.Perform a sync. | A new maintenance request is created. |  |
| 3 | Screen the Maintenance Request | Log in to your S/4 tenant as a user with the assigned business role Maintenance SupervisorOpen the application Screen Maintenance Requests (F4072).Find the maintenance request you created and select it.Click the Action Required button in the top right corner.Provide a reason and description and click the Action Required button. | The maintenance request is set to Action Required |  |
| 4 | Receive the Push Notification | On the device running SAP Maintenance Assistant, you should receive a push notification informing you of the maintenance request.When prompted, choose to download the updated maintenance request. | The updated maintenance request is downloaded to the device. |  |

#### Create an Emergency Work Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used to create a maintenance request for emergency work so that the request is submitted and work is scheduled in expedited mode.

Procedure

Table 15:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SMA app | Launch the SMA app and log on using the passcode or Touch IDLog in with a user that has the Maintenance Supervisor role (SAP_BR_MAINT_SUPERVISOR) assigned. | The Overview page is displayed |  |
| 2 | Create an Emergency Work Request | Navigate to the Maintenance Requests List page by tapping on Maintenance Requests in the Overview pageTap on the + button on the top right corner of the pageUnder Processing Context choose Emergency Work.Fill out the rest of the maintenance request details and tap on the Done button. | An emergency maintenance request is created with the status Accepted. The maintenance request has a maintenance order attached. |  |
| 3 | Sync the Emergency Work Request | Press the Sync button on the top right corner of the screen. | An emergency maintenance request and maintenance order are created on the back end. |  |

#### Edit an Attachment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used to edit or annotate an image or document

Procedure

Table 16:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SMA app | Launch the SMA app and log on using the passcode or Touch ID. | The Overview page is displayed |  |
| 2 | Add an Attachment to an Operation | Open an operation.Press Edit.Scroll down to Attached Files and press the + button.Select a photo from your photo library, or take a photo. Press Done. | An attachment is added to the operation. |  |
| 3 | Open the Attachment | Scroll down in the Operation screen and click the Documents tab.Click the Open button to open your attachment. | The photo you attached is displayed. |  |
| 4 | Edit the Attachment | Press the Edit button in the top right corner.Edit the attachment by using the paintbrush. Add text to the image.Press the Save button on the top right corner. Choose Save.Open the attachment and confirm that your changes are there. | The attachment is edited and the edits are displayed. |  |
| 5 | Sync the Attachment | Return to the Overview page and tap the sync button. | The attachment is saved on the SAP back end and no errors are returned. |  |
| 6 | Edit the Downloaded Attachment | Repeat steps 3 - 5 with the attachment you created. | Edits to the downloaded attachment are displayed in the app and saved successfully on the SAP back end. |  |

#### Clear Reservations on Final Confirmation of an Operation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used to clear the reservations for unused materials upon the completion of an operation.

Procedure

Table 17:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SMA app | Launch the SMA app and log on using the passcode or Touch ID. | The Overview page is displayed |  |
| 2 | Open an Operation with Parts Assigned | Tap on Maintenance Operations from the Overview screen.From the Maintenance Operations list, tap on an operation. Make sure that the operation has unissued parts assigned to it. | The Operations Detail page is displayed. |  |
| 3 | Complete the Operation and Add a Confirmation | End the operation and choose to add confirmation time when prompted.Scroll down and toggle the Clear Reservations switch.Press the Done button. | A confirmation is created for the operation. |  |
| 4 | Observe the Current Material Stock | Log in to your S/4 Cloud tenant as a user with the business role SAP_BR_INVENTORY_MANAGER assigned.Open the Display Stock Overview app.Enter your material, plant, storage location, and batch of a part from your operation. Press Execute.Take note of the reserved quantity for the material and keep this window open. |  |  |
| 5 | Sync the Confirmation from SAP Maintenance Assistant | Press the Sync button on the SAP Maintenance Assistant application. | Data is transmitted to the SAP system. |  |
| 6 | Confirm the Reserved Quantity is Adjusted | In the Display Stock Overview application, press the Refresh button.Confirm that the reserved quantity has been adjusted by the amount reserved for your operation. | The reserved stock quantity has decreased by the amount of stock reserved for the completed operation. |  |

#### Complete Operations Using the Consolidated Completion Flow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used to simultaneously complete multiple operations, add time, and update the related maintenance request.

Procedure

Table 18:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SMA app | Launch the SMA app and log on using the passcode or Touch ID. | The Overview page is displayed |  |
| 2 | Select Multiple Operations for Completion | On the Overview page, under My Operations, tap See All.On the top right, tap Select.Select multiple operations and tap Confirm. | The consolidated completion screen displays. |  |
| 3 | Enter Confirmation and Damage Information | For each operation in the list, enter confirmation details and update the maintenance request details.After updating the information, press Done. | Confirmations are created or the selected operations and related maintenance request details are updated. |  |
| 4 | Sync Your Changes | Navigate back to the Overview screen and press the Sync button.Log in to your S/4 Cloud system and confirm that your changes are saved. | Changes made in the SAP Maintenance Assistant app are saved in the S/4 Cloud system. |  |

#### Assign Operations as a Supervisor

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used by the maintenance supervisor to assign operations to other technicians.

Prerequisites

The user must have business catalog SAP_EAM_BC_ORD_MNG_PC assigned. This buisness catalog is included in the Maintenance Supervisor business role template SAP_BR_MAINT_SUPERVISOR.

Procedure

Table 19:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SMA app | Launch the SMA app and log on using the passcode or Touch ID. | The Overview page is displayed |  |
| 2 | Open the Operations List | Open the side navigation menu and select Operations | The Operations list screen displays. |  |
| 3 | Assign Operations | Press the ... button in the upper right hand cornerSelect Assign from the listOpen the operations picker and select one or more operationsOpen the Assigned To picker and select an employeePress the Assign buttonConfirm that the operations are assigned to the selected user and this is synced with the back end | Operations are assigned to the selected user |  |

### Field Service Technician Persona Test Procedures

#### View the List of Service Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used by a customer service technician or a customer service manager to view the list of service orders.

Procedure

Table 20:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SMA app | Launch the SMA app and log on using the passcode or Touch ID. | The Overview page is displayed |  |
| 2 | Switch to the Field Service Technician persona | From the side navigation panel, tap Profile Settings.Switch to the Field Service Technician persona using the Switch Persona dropdown menu.Tap Done. | The app is reloaded with the Overview page for the Field Service Technician persona |  |
| 3 | Review the list of service orders | Tap on Service Orders from the side menu. | Based on the assignment type, the list of service orders assigned to the logged-in service user are displayed. |  |

#### View the List of Service Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used by a customer service technician or a customer service manager to view the list of service items.

Procedure

Table 21:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Maintenance Assistant app | Launch the SMA app and log on using the passcode or Touch ID. | The Overview page is displayed |  |
| 2 | Switch to the Field Service Technician persona | From the side navigation panel, tap Profile Settings.Switch to the Field Service Technician persona using the Switch Persona dropdown menu.Tap Done. | The app is reloaded with the Overview page for the Field Service Technician persona |  |
| 3 | Review the list of service items | Tap on Items from the side menu. | Based on the assignment type, the list of service items assigned to the logged-in service user are displayed. |  |

#### View the List of Service Confirmations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used by a customer service technician or customer service manager to view the list of service confirmations.

Procedure

Table 22:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Maintenance Assistant app | Launch the SAP Maintenance Assistant app and log on using the passcode or Touch ID. | The Overview page is displayed |  |
| 2 | Switch to the Field Service Technician persona | From the side navigation panel, tap Profile SettingsSwitch to the Field Service Technician persona using the Switch Persona dropdownTap Done | The app is reloaded with the Overview page of the Field Service Technician persona |  |
| 3 | Review the list of service confirmations | Tap on Confirmations from the side menu | The list of service confirmations for the service orders are displayed |  |

#### Create a Service Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used by a customer service manager to create a service order.

Procedure

Table 23:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Maintenance Assistant app | Launch the SMA app and log on using the passcode or Touch ID. | The Overview page is displayed |  |
| 2 | Switch to the Field Service Technician persona | From the side navigation menu, click Profile SettingsSwitch to the Field Service Technician persona using the Switch Persona dropdownTap Done | The app is reloaded with the Overview page of the Field Service Technician persona |  |
| 3 | Create a service order | Click the Create Service Order quick action button on the Overview page to launch the Add Service Order dialog. Alternatively, you can navigate to Service Orders from the side menu and tap the + button.Enter the following details on the dialog:Provide a DescriptionService order process types (SV01 - Service Order and SV02 - Fixed Price Service Order) supported in S/4 cloud are displayed in the Process Type picker. The default value is SV01.Adjust the Priority as neededChoose a Sold-to party from the picker in the Organizational Data section. The selected value will filter the Sales Organization Scenario and Bill to Party pickers. Choose the required values.If the Bill to Party picker displays no values, specify a bill-to party relationship (CRMH04) between corresponding business partners through the Manage Business Partner Master Data Fiori app.Provide values in the Main Reference Object section as neededProvide a note type, long text, and attachments in the respective sections as neededAfter entering all the fields, tap on the Done button. You're then navigated to the Add Service Order Item page. Follow the [Add a Service Order Item](#unique_39) [page ] 39 procedure, then tap Done.Tap the Sync button on the top right of the page. | The newly-created service order is posted to the back end |  |

#### Add a Service Order Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure is used by a customer service manager to add a service item to a service order.

Procedure

Table 24:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Maintenance Assistant app | Launch the SMA app and log on using the passcode or Touch ID. | The Overview page is displayed |  |
| 2 | Switch to the Field Service Technician persona | From the side navigation menu, click Profile SettingsSwitch to the Field Service Technician persona using the Switch Persona dropdownTap Done | The app is reloaded with the Overview page of the Field Service Technician persona |  |
| 3 | Add a service item | Click the Create Service Order quick action button on the Overview page to launch the Add Service Order dialog. Alternatively, you can navigate to Service Orders from the side menu and tap the + button.Enter the following details on the dialog:Provide a DescriptionSelect Service Order from the picker if not already selectedAdjust the Priority as neededChoose a Product ID from the picker. Note that UOM is populated based on this selection.Once the Product ID is selected, the Item Category picker is enabled. Provide a selection.Provide values for the Account Indicator and Service Contract sections as neededProvide a note type and attachments in the respective sections as neededTap Done once all details are provided.Tap the Sync button on the top right of the page. | The newly-created service item is added to the service order in the back end |  |

#### Create a Service Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure is used by a customer service manager or customer service technician to create a service confirmation.

|  |
| --- |
| Note Confirmations can only be created for service orders in the Released state that contain no errors. |

Procedure

Table 25:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Maintenance Assistant app | Launch the SMA app and log on using the passcode or Touch ID. | The Overview page is displayed |  |
| 2 | Switch to the Field Service Technician persona | From the side navigation menu, click Profile SettingsSwitch to the Field Service Technician persona using the Switch Persona dropdownTap Done | The app is reloaded with the Overview page of the Field Service Technician persona |  |
| 3 | Create a service confirmation | Click the Create Service Confirmation quick action button on the Overview page to launch the Add Confirmation dialog. Alternatively, if a confirmation does not exist already, you can use the Confirm Item quick action button or the Add Confirmation Item menu option in the service order detail screen.Enter the following details on the dialog:Provide a DescriptionSelect Service Order for which you are creating the confirmationToggle Set as Final Confirmation if no further confirmations will be created. Note that setting a final confirmation automatically sets the service order to Completed.Provide values in the Reference Object and Notes section as needed.Tap Next and select for the following:Select the Service Item for which the confirmation will be createdSelect the Item Category from the picker provided. Add other values on the Add Confirmation Item screen.Specify the Actual Duration. If you fill out this field, a partial confirmation of a portion of the service order item is specified.Tap Done once all details are provided.Tap the Sync button on the top right of the page. | The newly-created service confirmation is saved to the back end |  |

#### Add a Confirmation Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure is used by a customer service manager or customer service technician to create a service confirmation item.

Procedure

Table 26:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Maintenance Assistant app | Launch the SAP Maintenance Assistance app and log on using the passcode or Touch ID. | The Overview page is displayed |  |
| 2 | Switch to the Field Service Technician persona | From the side navigation menu, click Profile SettingsSwitch to the Field Service Technician persona using the Switch Persona dropdownTap Done | The app is reloaded with the Overview page of the Field Service Technician persona |  |
| 3 | Add a service confirmation item | Click the Confirm Item quick action button on the Service Order detail screen. Alternatively, you can use the quick action button Add Confirmation Item.Enter the following details on the dialog:Select Service Order ItemThe Description from the selected service order item is automatically populatedSelect Item Category from the picker..Specify Actual Duration. If specified, this creates a partial confirmation of the specified portion of the service order item.Tap Done once all details are provided.Tap the Sync button on the top right of the page. | The newly-created service confirmation item is saved to the back end |  |

#### Complete a Service Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used by a customer service manager or customer service technician to complete a service confirmation.

Procedure

Table 27:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Maintenance Assistant app | Launch the SAP Maintenance Assistant app and log on using the passcode or Touch ID. | The Overview page is displayed |  |
| 2 | Switch to the Field Service Technician persona | From the side navigation menu, click Profile SettingsSwitch to the Field Service Technician persona using the Switch Persona dropdownTap Done | The app is reloaded with the Overview page of the Field Service Technician persona |  |
| 3 | Completing the service confirmation | From the Confirmations screen, select and tap a confirmation to navigate to the Confirmation Items detail screen.Select and tap on a confirmation item. Then use the Complete Confirmation Item button to set the confirmation item to Completed.Once all confirmation items are set to Completed, tap on the Complete Confirmation button to complete the confirmation.Tap on the Sync button on the top right of the page. | The confirmation status is posted to the back end |  |

#### Complete a Service Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure is used by a customer service manager to complete a service item.

Procedure

Table 28:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Maintenance Assistant app | Launch the SAP Maintenance Assistant app and log on using the passcode or Touch ID. | The Overview page is displayed |  |
| 2 | Switch to the Field Service Technician persona | From the side navigation menu, click Profile SettingsSwitch to the Field Service Technician persona using the Switch Persona dropdownTap Done | The app is reloaded with the Overview page of the Field Service Technician persona |  |
| 3 | Completing a service item | From Items, navigate to a service item detail of an order that is in the Started status.Tap on the Complete and Confirm button to complete the serice item.If this is the last service item, a prompt displays to complete the service order. If Yes is selected, a popup appears to create the confirmation item and add notes. A prompt also displays for signature capture of the assignment type is set to 2.Tap on the Done button. The service item and service order are set to Completed.Tap on the Sync button on the top right of the page. | The service item is set to Completed, which is posted to the back end and removed from the client |  |

#### Complete a Service Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure is used by a customer service manager to complete a service order

Procedure

Table 29:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Maintenance Assistant app | Launch the SAP Maintenance Assistant app and log on using the passcode or Touch ID. | The Overview page is displayed |  |
| 2 | Switch to the Field Service Technician persona | From the side navigation menu, click Profile SettingsSwitch to the Field Service Technician persona using the Switch Persona dropdownTap Done | The app is reloaded with the Overview page of the Field Service Technician persona |  |
| 3 | Completing a service order | From Service Orders navigate to the service order detail with a status of either Started or On HoldTap on the Complete button to complete the service orderCreate a confirmation item and notes from the popup dialog. There will be a prompt for a digital signature capture if the assignment type for service orders is set to 1Tap on the Done button. The service order is set to Completed, which also sets the associated service items to CompletedTap on the Sync button on the top right of the page | The service order and items are set to Completed, which is posted to the back end and are removed from the client |  |

#### View the List of Service Quotations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure is used by a customer service manager to view the list of S/4HANA service quotations

Procedure

Table 30:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Maintenance Assistant app | Launch the SAP Maintenance Assistant app and log on using the passcode or Touch ID. | The Overview page is displayed |  |
| 2 | Switch to the Field Service Technician persona | From the side navigation menu, click Profile SettingsSwitch to the Field Service Technician persona using the Switch Persona dropdownTap Done | The app is reloaded with the Overview page of the Field Service Technician persona |  |
| 3 | View the list of service quotations | Tap on Service Quotations from the side menu | Based on the assignment type, the list of service quotations assigned to the logged-in service user are displayed |  |

#### View the List of Service Quotation Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure is used by a customer service manager to view the list of S/4HANA service quotation items.

Procedure

Table 31:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Maintenance Assistant app | Launch the SAP Maintenance Assistant app and log on using the passcode or Touch ID. | The Overview page is displayed |  |
| 2 | Switch to the Field Service Technician persona | From the side navigation menu, click Profile SettingsSwitch to the Field Service Technician persona using the Switch Persona dropdownTap Done | The app is reloaded with the Overview page of the Field Service Technician persona |  |
| 3 | View the list of service quotations | Tap on Service Quotation Items from the side menu | Based on the assignment type, the list of service quotation items assigned to the logged-in service user are displayed |  |

#### Create a Service Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure is used by a customer service manager to create an S/4HANA service quotation.

Procedure

Table 32:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Maintenance Assistant app | Launch the SAP Maintenance Assistant app and log on using the passcode or Touch ID. | The Overview page is displayed |  |
| 2 | Switch to the Field Service Technician persona | From the side navigation menu, click Profile SettingsSwitch to the Field Service Technician persona using the Switch Persona dropdownTap Done | The app is reloaded with the Overview page of the Field Service Technician persona |  |
| 3 | Create a service quotation | Click the Create Service Quotation quick action button on the Overview page to launch the Add Service Quotation dialog. Alternatively, navigate to Service Quotations from the side menu and tap the + icon. Enter the following details:Provide a DescriptionAdjust the Priority as neededThe Process Type picker displays the supported service order process types (SVQ1 - Service Quotation and SVQ2 - Fixed Price Service Quotation). The default value of SVQ1 is selected.Choose a Sold-to party from the picker in the Organizational Data section. The selected value filters the Sales Organization Scenario and Bill-to Party pickers. Choose the required values.Note If the Bill-to Party picker displays no values, specify a Bill-to Party relationship (CRMH04) between corresponding business partners through the Manage Business Partner Master Data Fiori app.Provide a note type, long text, and attachments in the respective sections as neededTap the Done button. You're navigated to the Add Service Quotation Item page. Follow the test case , located in this document, to fill the page. Then tap on Done.Tap the Sync button on the top right of the page. | The newly-created service quotation is posted to the back end sytem. |  |

#### Add a Service Quotation Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure is used by a customer service manager to add a service quotation item to a service quotation.

Procedure

Table 33:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Maintenance Assistant app | Launch the SAP Maintenance Assistant app and log on using the passcode or Touch ID. | The Overview page is displayed |  |
| 2 | Switch to the Field Service Technician persona | From the side navigation menu, click Profile SettingsSwitch to the Field Service Technician persona using the Switch Persona dropdownTap Done | The app is reloaded with the Overview page of the Field Service Technician persona |  |
| 3 | Create a service quotation | Click the Add Quotation Item quick action button on the Service Quotation detail page. Alternatively, navigate to Service Quotations from the side menu and tap the + icon and click Add Quotation Item. Enter the following details:Provide a DescriptionChoose Product ID from the picker.Note UOM is populated based on this section.After Product ID is chosen, the Item Category picker is enabled. Provide a selection.Specify values for Account Indicator, Service Contract, and Quantity as neededProvide a note type and attachments in the respective sections as neededTap the Done button. You're navigated to the Add Service Quotation Item page. Follow the test case , located in this document, to fill the page. Then tap on Done.Tap the Sync button on the top right of the page. | The newly-created service quotation item is added to the service quotation on the back end system |  |

#### Set the Assignment Type for Service Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure is used by a configuration expert (SAP Maintenance Assistant) to set the assignment type for service orders.

Procedure

Table 34:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the Fiori app for the Mobile Application Configuration | Log on to the Fiori app Manage Mobile Application Configuration for SAP Maintenance Assistant. Use the business user that has the role SAP_BR_MAIF_CONFIG_EXPERT assigned. | The Fiori application is launched |  |
| 2 | Switch the assignment type for service orders | Go to the Application Control facetIn Edit mode, use the dropdown Service Order Assignment Type to switch assignment type between 1 for Header Level Business Partner assignment and 2 for Item Level Business Partner assignment.Save the changes | The assignment type for service orders is set |  |
| 3 | Log on to SAP Maintenance Assistant | Log on to the SAP Maintenance Asssistant application and switch to the Field Service Technician persona.Review the list of service orders and service items displayed for the logged-in user. | If the assignment type is set to 1, service orders assigned to the logged-in user are displayed under Service Orders and items that belong to these orders are displayed under ItemsIf the assignment type is set to 2, items that are assigned to the logged-in user are displayed under Items. Service orders that contain these items are displayed in the Service Orders section. |  |

#### FSM Integration - Download Service Technician Assignments from FSM to SAP Maintenance Assistant

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure is used by a dispatcher to assign a service technciian to an activity in the FSM Planning and Dispatching board. This assignment is then replicated to SAP Maintenance Assistant..

Procedure

Table 35:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the FSM Planning and Dispatching board | Open the FSM Planning and Dispatching board with Dispatcher | The Planning and Dispatching board is displayed |  |
| 2 | Assign an activity to the service technician | Drag and drop a service call or activity against the service technician (that you will use to log on to SAP Maintenance Assistant) on the FSM Planning board.Select the activity on the planning board and click on the Release Assignments button at the top right of the board | The service call or activity is assigned to the service technician and is synced to the SAP S/4HANA Cloud Public Edition system |  |
| 3 | Log on to the SAP Maintenance Assistant app with a service techncian user | Set the Service Order Assignment Type to 2. See [Set the Assignment Type for Service Orders](#unique_49) [page ] 50 for more details.Launch the SAP Maintenance Assistant app and log on using the Service Technician user | The Overview page is displayed |  |
| 4 | Switch to the Field Service Technician persona | From the side navigation panel, tap Profile SettingsSwitch to the Field Service Technician persona using the Switch Persona dropdownTap Done | The app is reloaded with the Overview page of the Field Service Technician persona |  |
| 5 | Verify assignment to the service techncian | From Items on the side menu, navigate to the Service Item detail of the assigned activity in FSMGo to the Business Partners facet to verify if a new function Exec. Service Employee has been added and assigned to the service technician user in the app | The service technician assigned to the activity in FSM should be replicated to SAP Maintenance Assistant on the service item after sync |  |

#### FSM Integration - Download Smartforms Attached to an Activity from FSM to SAP Maintenance Assistant

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure is used by an FSM dispatcher to assign a Smartform to an activity in FSM. This assignment is then replicated to SAP Maintenance Assistant..

Procedure

Table 36:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the FSM Planning and Dispatching board | Open the FSM Planning and Dispatching board with Dispatcher | The Planning and Dispatching board is displayed |  |
| 2 | Attach a Smartform to an activity | Navigate to Activities from the side menuSelect an activity that's synced to SAP Maintenance Assistant and go to the activity detail.Switch to the Smartforms tab and attach a Smartform using the Create button.Click on the Smartform added to fill in the questionaire or click on the Close button. | The Smartform is added on the FSM Planning and Dispatching board |  |
| 3 | Log on to the SAP Maintenance Assistant app with a service techncian user | Launch the SAP Maintenance Assistant app and log on using the Service Technician user | The Overview page is displayed |  |
| 4 | Switch to the Field Service Technician persona | From the side navigation panel, tap Profile SettingsSwitch to the Field Service Technician persona using the Switch Persona dropdownTap Done | The app is reloaded with the Overview page of the Field Service Technician persona |  |
| 5 | Verify the Smartform is downloaded from FSM | Sync on the SAP Maintenance Assistant app. Then open Smartforms from the side menu. Alternatively, you can navigate to Items and open the activity or item. Then navigate to the Smartforms section.Verify that the Smartform added in the FSM Dispatching and Planning board is downloaded to the service item in the SAP Maintenance Assistant app. | The Smartform added in FSM is downloaded to the app and can be edited |  |

#### FSM Integration - Edit Smartforms Downloaded from FSM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure is used by a service technician to edit Smartforms on a service item. This should be replicated to the FSM Planning and Dispatching board.

|  |
| --- |
| NoteA Smartform can be edited provided the form is not in the Completed status.The service item you're using in this procedure should be assigned to the logged-in technician user so that it is editable. |

Procedure

Table 37:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Maintenance Assistant app with the Service Technician user | Ensure the Service Order Assignment is set to 2 by following the [Set the Assignment Type for Service Orders](#unique_49) [page ] 50 procedureLaunch the SAP Maintenance Assistant app and log on using your passcode or Touch ID | The Overview page is displayed |  |
| 2 | Switch to the Field Service Technician persona | From the side navigation menu, tap Profile SettingsSwitwch to the Field Service Technician persona using the Switch Persona dropdown. Tap Done. | The app is reloaded with the Overview page of the Field Service Technician persona |  |
| 3 | Edit a Smartforms on a service item | Open Smartforms from the side navigation menu. Alternatively, navigate to Items and open the activity or item that's used in the FSM board and go to the Smartforms section.Provide input for the form. Once complete, submit or save the draft changes using the buttons in the dialog.Tap on the Sync button on the top right of the page. | The Smartform changes are saved. |  |
| 4 | Log on to the FSM Planning and Dispatching board | Open the FSM Planning and Dispatching board with Dispatcher | The Planning and Dispatching board is displayed |  |
| 5 | Verify the changes on the Smartform | From the Activities section on the side menu, select the activity which has been changed in the SAP Maintenance Asssistance app. Alternatively, the Activity page can be displayed from the Service Calls section or from the Planning and Dispatching board.Switch to the Smartforms tab on the Activity detail, and open the Smartform.Verity the Smartform is in the Open statu and the changes performed in the SAP Maintenance Asssistant app are synced to FSM. | The Smartform changes from SAP Maintenance Assistant are synced to FSM |  |

#### FSM Integration - Complete Smartforms Downloaded from FSM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure is used by a service technician to complete Smartforms on a service item. This should be replicated to the FSM Planning and Dispatching board.

|  |
| --- |
| Note A Smartform can be edited provided the form is not in the Completed status. |

Procedure

Table 38:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Maintenance Assistant app with the Service Technician user | Ensure the Service Order Assignment is set to 2 by following the [Set the Assignment Type for Service Orders](#unique_49) [page ] 50 procedureLaunch the SAP Maintenance Assistant app and log on using your passcode or Touch ID | The Overview page is displayed |  |
| 2 | Switch to the Field Service Technician persona | From the side navigation menu, tap Profile SettingsSwitwch to the Field Service Technician persona using the Switch Persona dropdown. Tap Done. | The app is reloaded with the Overview page of the Field Service Technician persona |  |
| 3 | Complete a Smartforms on a service item | Open Smartforms from the side navigation menu. Alternatively, navigate to Items and open the activity or item that's used in the FSM board and go to the Smartforms section.Provide input for the form. Once complete, submit the changes using the buttons in the bottom right of the dialog. Note that mandatory questions must be filled to complete the form.Tap on the Sync button on the top right of the page. | The Smartform is completed and removed from the device after the sync. |  |
| 4 | Log on to the FSM Planning and Dispatching board | Open the FSM Planning and Dispatching board with Dispatcher | The Planning and Dispatching board is displayed |  |
| 5 | Verify the changes on the Smartform | From the Activities section on the side menu, select the activity which has been changed in the SAP Maintenance Asssistance app. Alternatively, the Activity page can be displayed from the Service Calls section or from the Planning and Dispatching board.Switch to the Smartforms tab on the Activity detail, and open the Smartform.Verity the Smartform is in the Closed statu and the changes performed in the SAP Maintenance Asssistant app are synced to FSM. | The Smartform changes from SAP Maintenance Assistant are synced to FSM and is set to a Closed status. |  |

#### FSM Integration - Mobile Status Updates from SAP Maintenance Assistant to FSM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure is used by a service technician to update the mobile status of a service item. This should be replicated to the FSM Planning and Dispatch board.

Procedure

Table 39:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Maintenance Assistant app with the Service Technician user | Ensure the Service Order Assignment is set to 2 by following the [Set the Assignment Type for Service Orders](#unique_49) [page ] 50 procedureLaunch the SAP Maintenance Assistant app and log on using your passcode or Touch ID | The Overview page is displayed |  |
| 2 | Switch to the Field Service Technician persona | From the side navigation menu, tap Profile SettingsSwitwch to the Field Service Technician persona using the Switch Persona dropdown. Tap Done. | The app is reloaded with the Overview page of the Field Service Technician persona |  |
| 3 | Update the status of a service item in SAP Maintenance Assistant | Navigate to a service item detail from the Items section on the side menuSet the status of the service item using the buttons in the bottom right of the details page.Tap on the Sync button on the top right of the page. | The mobile status of the service item is updated. |  |
| 4 | Log on to the FSM Planning and Dispatching board | Open the FSM Planning and Dispatching board with Dispatcher | The Planning and Dispatching board is displayed |  |
| 5 | Verify the changes on the Smartform | From the Activities section on the side menu, select the activity whose status has been changed in the SAP Maintenance Asssistance app. Alternatively, the Activity page can be displayed from the Service Calls section or from the Planning and Dispatching board.From the details section of the activity, verify that the status has been updated. | The mobile status from the SAP Maintenance Assistant app has been posted as a Workflow step in FSM. |  |

#### FSM Integration - Location Tracking Updates from SAP Maintenance Assistant to FSM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure is used by a service technician to update the technician's location from SAP Maintenance Assistant to FSM so it can be viewed on the FSM service map.

Procedure

Table 40:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Verify mobile application configuration | Launch the Manage Mobile Application Configuration Fiori app by logging in with Configuration Expert.Verify that FSM Integration and Allow Override under location tracking control are set to Active.Ensure the Service Order Assignment is set to 2 by following the procedure located in this guide. | The configuration for SAP Maintenance Assistant is adjusted |  |
| 2 | Log on to the SAP Maintenance Assistant app with the Service Technician user | Launch the SAP Maintenance Assistant app and log on using your passcode or Touch IDEnsure Location Tracking is enabled by verifying from the Profile settings. | The Overview page is displayed and location tracking is enabled |  |
| 3 | Update the status of a service item in SAP Maintenance Assistant | Update the mobile status on a service item by following the procedure located in this guide.Set the status of the service item and it will trigger a location update in the back end. | The mobile status of the service item and technician location are updated. |  |
| 4 | Log on to the FSM Planning and Dispatching board | Open the FSM Planning and Dispatching board with Dispatcher | The Planning and Dispatching board is displayed |  |
| 5 | Verify location update on the service map | From the side menu, launch Service MapVerify the technician location captured and plotted on the service map. | Location update is verified. |  |

### Dynamic Forms Test Procedures

#### Publish Form, Create Form Instances, and Fetch Forms to the Mobile Application

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is to create the necessary data for further testing and to ensure that it is available on the mobile application.

Procedure

Table 41:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the Dynamic Forms BTP application | Open the Dynamic Forms launchpad and log on using your BTP credentials.Open the Form Builder application. | The Form Builder application is displayed. |  |
| 2 | Publish the Demo form | Select the form with the application name Demo and the form name of MeterSwapClick the Publish buttonSelect a version option from the dropdown and click Publish | The form is published |  |
| 3 | Create form instances | Log in to the SAP S/4HANA Cloud Public Edition system as the Mobile Administrator and open the Manage Dynamic Forms applicationPress Go to load the list of form definitions and select the demo form you published in the previous step.Note It can take up to an hour for the published form to become available.Press the Edit button, then click CreateNext to Assigned Objects, click CreateSelect Work Order and choose an object key that corresponds to a work order on your mobile application. Then click Continue.Choose the technical entity type WOOPERATION. Select the technical entity key and click Apply.Press Save to save the form instanceRepeat Steps 3 - 7 in this list for EQUIPMENT, FUNCLOC, and NOTIFICATION | Form instances are created |  |
| 4 | Sync the form instances to the mobile application | Launch the SAP Maintenance Assistant application and log on using your passcode or Touch IDPress the Sync buttonOnce the sync is complete, open the objects you created form instances for and confirm that the forms are displayed | The forms are present on the device |  |

#### Complete Forms

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is used by a technician to complete and submit a form.

Procedure

Table 42:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Maintenance Assistant app | Launch the SAP Mainteanance Assistant app and log on using the passcode or Touch ID | The Overview page is displayed |  |
| 2 | Complete the form for a work order operation | Navigate to a work order operation and open the formFill out the form and click the Complete buttonVerify that the form is saved and set to status CompletedVerify that the form can no longer be edited without reopening the formSync the applicationConfirm that the completed form is no longer on the work order | The form is completed |  |
| 3 | Complete the form for equipment | Navigate to an equipment and open the formRepeat steps 2 - 6 in Step 2 for the form on the equipment | The form is completed |  |
| 4 | Complete the form for a functional location | Navigate to an equipment and open the formRepeat steps 2 - 6 in Step 2 for the form on the functional location | The form is completed |  |
| 5 | Complete the form for a maintenance request | Navigate to an equipment and open the formRepeat steps 2 - 6 in Step 2 for the form on the maintenance request | The form is completed |  |

#### Required Forms

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is to test the functionality of required forms in the mobile application.

Procedure

Table 43:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Add a form to an operation | Log in to your SAP S/4HANA Cloud Public Edition system system as the mobile administrator and open the Manage Dynamic Forms applicationSelect the Demo form, click Edit, then CreateNext to Assigned Objects, click CreateSelect Work Order and choose an object key that corresponds to a work order on your mobile application. Press Continue.Select Technical Entity type WOOPERATION and select the key of an operation that is on your mobile device and is assigned to your user.Click the Required flag and Save | The Form Builder application is displayed |  |
| 2 | Attempt to complete the operation | Launch the SAP Maintenance Assistant app and log on using the passcode or Touch IDOpen the operation that you attached the required form to in the previous stepPress the Start button, then press the Complete buttonConfirm that the Complete Operation screen shows that there is a required formPress the Done button and confirm that the app prevents you from completing the operationPress the Cancel button to return to the operation | The operation cannot be completed |  |
| 3 | Complete the form and the operation | Open the form and fill it outPress Save, then press Complete to complete the formPress the Complete button on the operation, then press DoneConfirm that the operation is successfully completed | The form and operation are completed |  |

#### Open, Update, and Save Form

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is to test the functionality of opening, updating, and saving a form in the SAP Maintenance Assistant application.

Procedure

Table 44:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open a form | Launch the SAP Maintenance Assistant application and log on using the passcode or Touch IDNavigate to an object that you have attached a form to and open the form | The form is displayed in the mobile application |  |
| 2 | Update a form | Edit the form you opened and press Save. Then close the formReopen the form and confirm that your changes are still thereMake more changes to the form and press the Close buttonConfirm that you are prompted to save your changes before closing the form | The proper validations are displayed and the changes to the form are saved |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can proceed this process.

| Process | Business Condition |
| --- | --- |
| Assign and Release Maintenance Order | The Maintenance Order must be assigned and released |

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
> Flagged while digesting this document, not verified: The overview table lists the 'Set Assignment Type for Service Orders' step under Configuration Expert (Maintenance Assistant) and again as 'Setting the Assignment Type for Service Orders' under Service Technician - Customer Service, while the procedure itself is performed by the Configuration Expert (SAP_BR_MAIF_CONFIG_EXPERT).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/maintenance-order-processing-with-sap-field-service-management-7z2-ae]]
- related-to :: [[14-maintenance-service-and-projects/service-order-processing-with-sap-field-service-management-49x-ae-test]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4RV_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 109,210 chars in the whole document
