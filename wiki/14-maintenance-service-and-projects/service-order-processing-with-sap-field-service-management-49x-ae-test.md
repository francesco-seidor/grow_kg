---
id: 14-maintenance-service-and-projects/service-order-processing-with-sap-field-service-management-49x-ae-test
title: "Service Order Processing with SAP Field Service Management (49X_AE) - Test Script, SAP S/4HANA Cloud Public Edition (49X_S4CLD2608_BPD_EN_AE)"
description: "S/4HANA Cloud Public Edition 2608 test script (49X_AE): service/repair order integration with SAP Field Service Management, prerequisites and E2E steps."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/field-service-and-mobile-maintenance]
aliases: [49X_S4CLD2608_BPD_EN_AE]
keywords: [Field Service Management and Mobile Maintenance, service order processing, field service management, integration test procedures, service contract synchronization, service order release, service dispatching, service confirmation, repair order processing, smartforms]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/49X_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1005
topic: 14-maintenance-service-and-projects/field-service-and-mobile-maintenance
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Service Order Processing with SAP Field Service Management (49X_AE) - Test Script, SAP S/4HANA Cloud Public Edition (49X_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/49X_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Field Service Management and Mobile Maintenance** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Service Order Processing with SAP Field Service Management (49X_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232854734)

[2 Prerequisites 4](#_Toc232854735)

[2.1 System Access 4](#_Toc232854736)

[2.2 Roles 4](#_Toc232854737)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232854738)

[2.3.1 Priority Value Mapping 7](#_Toc232854739)

[2.3.2 SAP Field Service Management Mobile Application 7](#_Toc232854740)

[2.4 Business Conditions 8](#_Toc232854741)

[2.5 Multiple Company Integration Scenario 8](#_Toc232854742)

[3 Overview Table 10](#_Toc232854743)

[4 Test Procedures 11](#_Toc232854744)

[4.1 E2E Scenario: Synchronize a Service Contract from S/4HANA Cloud to FSM 11](#_Toc232854745)

[4.1.1 Create a Service Contract and Release it to FSM 11](#_Toc232854746)

[4.1.2 Check Service Contract in FSM 11](#_Toc232854747)

[4.2 E2E Scenario: Create a Service Order in S/4HANA Cloud and Release it to FSM 12](#_Toc232854748)

[4.2.1 Create a Service Order with Line Items 12](#_Toc232854749)

[4.2.2 Release a Service Order 14](#_Toc232854750)

[4.3 E2E Scenario: Update a Released Service Order in S/4HANA Cloud and Re-release It 16](#_Toc232854751)

[4.3.1 Update a Service Order with Line Items 16](#_Toc232854752)

[4.4 E2E Scenario: Update Service Order in S/4HANA Cloud When Service Call or Activity is Updated in FSM 17](#_Toc232854753)

[4.4.1 Dispatch Plan and Release Activity 17](#_Toc232854754)

[4.4.2 Reassign Service Technician and Release Activity (Optional) 19](#_Toc232854755)

[4.4.3 Duplicate, Release, and Cancel Activity (Optional) 20](#_Toc232854756)

[4.4.4 Upload Attachment to a Service Call 21](#_Toc232854757)

[4.4.5 Upload Attachment to an Activity 22](#_Toc232854758)

[4.5 E2E scenario: Create Service Order with Items in S/4HANA Cloud when Service Call or Activity is Created in FSM 23](#_Toc232854759)

[4.5.1 Create Service Call 23](#_Toc232854760)

[4.5.2 Create Activity 26](#_Toc232854761)

[4.6 E2E Scenario: Create a Completed Service Confirmation in S/4HANA Cloud when Time Effort, Expense, or Material is Approved in FSM 28](#_Toc232854762)

[4.6.1 Technician Starts Working on Activity 28](#_Toc232854763)

[4.6.2 Updates Time, Use Reserved Material, and Add Expenses 29](#_Toc232854764)

[4.6.3 Finish Work and Close Activity 31](#_Toc232854765)

[4.6.4 Manager Approves Time Effort/Expense and Material 32](#_Toc232854766)

[4.7 E2E Scenario: Complete a Service Order in SAP S/4HANA Cloud Public Edition and Corresponding Service Call is Technically Completed in FSM 34](#_Toc232854767)

[4.8 E2E Scenario: Create a Service Order in S/4HANA Cloud, Release it to FSM, and Reject the Service Order 35](#_Toc232854768)

[4.8.1 Create a Service Order with Line Items 35](#_Toc232854769)

[4.8.2 Release a Service Order 37](#_Toc232854770)

[4.8.3 Reject a Service Order 38](#_Toc232854771)

[4.9 E2E Scenario: Create and Release a Repair Order in S/4HANA Cloud; Create and Approve a Time Effort in FSM 39](#_Toc232854772)

[4.9.1 Create and Release a Repair Order 39](#_Toc232854773)

[4.9.2 Create and Approve a Time Effort in FSM 41](#_Toc232854774)

[4.9.3 Check Confirmation in S/4HANA Cloud 43](#_Toc232854775)

[4.10 E2E Scenario: Create a Smartform Template and Instance in SAP FSM and visualize SAP SAP/S4HANA 44](#_Toc232854776)

[4.10.1 Create and Release a Smartform Template 44](#_Toc232854777)

[4.10.2 Create and Release a Smartform Instance 45](#_Toc232854778)

[5 Appendix 48](#_Toc232854779)

[5.1 Process Integration 48](#_Toc232854780)

[5.1.1 Preceding Processes 48](#_Toc232854781)

## Purpose

Overview

This scope item describes end-to-end business scenarios between SAP S/4HANA Cloud Public Edition service order or repair order processing and SAP Field Service Management.

Once a service or repair order is created and released in SAP S/4HANA Cloud Public Edition, a corresponding service call is created in SAP Field Service Management. An activity is created for each service item in the service or repair order, and spare part items are replicated as reserved materials.

An activity is assigned to a technician on the planning board in SAP Field Service Management. When the activity is released, the technician is automatically updated in the corresponding service/ repair order item in SAP S/4HANA Cloud Public Edition.

When confirmations such as efforts, expenses, or materials are approved in SAP Field Service Management, a service or repair confirmation is created and automatically completed in SAP S/4HANA Cloud Public Edition.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/49X_S4CLD2602_BPD_EN_AE.docx) ). |

### System Access

The test should be conducted with the following system:

Note For system details contact your System Administrator.

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP S4HC Service Order Integration with SAP Field Service Management - SAP FSM | Accessible via SAP FSM. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

|  |
| --- |
|  |

When creating the individual business role form the business role template, the assigned business catalogs only have read access but not write access. So it might be required to change the restrictions to allow unrestricted write access for the catalogs. After having created the business role, proceed as follows:

a. In app Maintain Business Roles, select the business role just created.

b. Select tab General Role Details.

c. In the screen area Access Categories, besides Write, Read, Value Help, select Unrestricted.

d. Choose Save and navigate back to Home screen.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Customer Service Manager | SAP_BR_CUSTOMER_SRVC_MANAGER | Service Management / Service Management – SAP Field Service and Asset Management | SAP_BR_CUSTOMER_SRVC_MGR / SAP_S4CRM_SPT_FSM_PC | Your system administrator provides the user and password information. |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT |  |  | Your system administrator provides the user and password information. |

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
| Note For every SAP S/4HANA Cloud Public Edition master data element used in your test procedure, the corresponding master data element with the proper External Id must exist in SAP Field Service Management. |

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Customer | 17100003 | for US (Domestic Customer US 3) | Make sure that the customer you use for this process has either assigned the customer pricing procedure 01 (Procedure 01) or no procedure.to check the assignment, use Business Role SAP_BR_BUPA_MASTER_SPECIALIST - tile Manage Customer Master Data in the Sales Area Data. |
| Employee | - | < Use your own employee ID that is assigned to your user ID.> |  |
| Service product (service) | SRV_01 | Services |  |
| Service Part (Defined) | SRV_04 | Service Part (Defined) | This spare part is of the material type non-stock, can be only be procured and will be used only in scope item 3NI. |
| Service Part (Undefined) | SRV_03 | Service Part (Undefined) |  |
| Service product (Expense Item) | SRV_02 | Expense Item | To create service expense products, use the Master Data script 3KV. |
| Unplanned Spare part | SRV_05 | Stock Service Part |  |
| Service Bundle | SRV_BUNDLE_01 | Service Bundle Fixed Price |  |
| Service Contract Product | SRV_CONTRACT | Service Contract Product | This service material can be only be used in scope item 3MO |
| Sales Organization | 1710 | (Dom. Sales Org US) |  |

You can find general information on how to create master data objects in the [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) 3KV (Create Service Product for Service Processes) and in the following Scope Items:

| Scope Item | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| 3KV | Create Service Product for Service Processes - MDS |
| 5LM | Create Functional Location - MDS |
| 5MF | Create Equipment - MDS |

|  |
| --- |
| Note Please take the steps for product SRV_02 in the master data script 3KV as the sample to create the following products.Product IDDescriptionCommentsEXP_FSM_ACCOMExpense Item for AccommodationEXP_FSM_MEALSExpense Item for MealsEXP_FSM_OTHERExpense Item for othersEXP_FSM_TRAVELExpense Item for Travel |

|  |
| --- |
| Note For more information about the Field Mapping between SAP S/4HANA Cloud Public Edition and SAP Field Service Management, see the guide Integration with SAP Field Service Management, section [Data Mapping](https://help.sap.com/viewer/6ef7f849fed34f95adfc449f29835255/latest/en-US/6cc6d51b7a99470e8378944d5a120585.html). |

#### Priority Value Mapping

| S/4HANA Cloud Priority | FSM Priority |
| --- | --- |
| Low | Low |
| Medium | Medium |
| High | High |
| Very High | High |

#### SAP Field Service Management Mobile Application

The SAP Field Service Management application can be downloaded on the mobile using the link, [Download Mobile App](https://help.sap.com/viewer/fsm_getting_started/Cloud/en-US/download-mobile-app.html). It can be downloaded for IOS, Android, and Windows.

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 3D2 - Service Order Management and Monitoring | The preliminary steps in the scope item 3D2 must be executed to ensure that service management processing can run successfully. |
| 3NI - Procurement for Service Management | If spare parts need to be procured externally, the preliminary steps in the scope item 3NI must be executed. |
| 3MO - Service Contract Management | If service contracts need to be synchronized to SAP Field Service Management, the preliminary steps in scope item 3MO must be executed. |

### Multiple Company Integration Scenario

We can replicate business objects from SAP S/4HANA Cloud Public Edition to one or more companies in SAP Field Service Management. For more information, see [Multiple Company Mapping for Data Integration Between SAP S/4HANA Cloud Public Edition and SAP Field Service Management](https://help.sap.com/docs/SAP_S4HANA_CLOUD/6ef7f849fed34f95adfc449f29835255/2122e26988184556b5409e6f2eddc5ec.html?locale=en-US). In the below table, you can find different business objects mapped to different FSM Companies based on specific rules.

| Business Object | Rule Type | Relevant Value | FSM Company |
| --- | --- | --- | --- |
| Customer (Sales) | Sales Area | 1710\|10\|00 | Company A |
| 5410\|10\|00 | Company B |  |  |
| Supplier (Purchasing) | Purchasing Org | 1710\|10\|00 | Company A |
| 5410\|10\|00 | Company B |  |  |
| Materials - Service Product | Sales Area | 1710\|10\|00 | Company A |
| 5410\|10\|00 | Company B |  |  |
| Materials - Spare Parts | Plant | 1710 | Company A |
| 5410 | Company B |  |  |
| Service Contract | Sales Area | 1710\|10\|00 | Company A |
| 5410\|10\|00 | Company B |  |  |
| Service Order | Sales Area | 1710\|10\|00 | Company A |
| 5410\|10\|00 | Company B |  |  |

To configure the replication of different business objects to multiple companies in SAP Field Service Management, proceed as described below.

1. Log in to the SAP Fiori launchpad in the SAP S/4HANA Cloud Public Edition system as Business Configuration Expert.
2. Open the Manage Your Solution app and click Configure Your Solution.
3. Search for the Integration with SAP Field Service Management item and select the item.
4. Click the Configure button next to Configure Multiple Company Replication.

For more information, see [Multiple Company Mapping Configuration in SAP S/4HANA Cloud Public Edition](https://help.sap.com/docs/SAP_S4HANA_CLOUD/6ef7f849fed34f95adfc449f29835255/6c9c8eb6dcc24e63b2697107b6fced4e.html?locale=en-US).

Once the mapping configuration is done in SAP S/4HANA Cloud Public Edition, the mapping data is synchronized to SAP Cloud Integration as a new value mapping artifact titled Value Mapping for Multiple Company determination in SAP Field Service Management from SAP S4HANA Cloud in the Integration of Service in SAP S/4HANA Cloud Public Edition with SAP Field Service Management package using the Synchronize Multiple Company Mapping Configuration integration artifact.

If the EnableMultiCompanyReplication parameter is set to true in the standard integrations of master and transactional data from SAP S/4HANA Cloud Public Edition to SAP Field Service Management, the integration flow will retrieve the mapping details of the multiple companies from the value mapping artifact instead of the default company and account that is configured.

## Overview Table

This process variant starts with the creation of a service order. The key characteristic is that total billed amount is calculated on the basis of time and material.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Create Service Contract | Customer Service Manager | Manage Service Contract | A standard service contract has been created. |
| Create Service Order | Customer Service Manager | Manage Service Order | A standard service order has been created. |
| Release Service Order Line Item (optional) | Customer Service Manager | Manage Service Order | An item of the service order has been released. |
| Change Service Order (optional) | Customer Service Manager | Manage Service Order | The service order has been changed. |
| Release Service Order | Customer Service Manager | Manage Service Order | The service order has been released. |
| FSM Dispatcher | Service Planner/Dispatcher | FSM | Dispatching of Service order. |
| Technician starts working | Service Technician - Customer Service | FSM Mobile App | Report the time and material spent on the activity. |
| Approve the Activities | Service Planner/Dispatcher | FSM | Service confirmation will be created accordingly. |
| Verify the Service order and Service confirmation | Customer Service Manager | Manage Service Order | Service confirmation is created automatically and reflected in the Transaction History Tab and lifecycle status of Service order should be Completed. |
| Release Confirmation for Billing | Customer Service Manager | Release for Billing | The confirmation has been released for billing. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### E2E Scenario: Synchronize a Service Contract from S/4HANA Cloud to FSM

#### Create a Service Contract and Release it to FSM

Purpose

The Service Manager creates and releases service contracts in the Fiori App “Manage Service Contract”

- Create a Service Contract and release it to FSM, please refer to the chapter Create Service Contract in 3MO Service Contract Management.

#### Check Service Contract in FSM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to check a Service Contract in SAP Field Service Management ().

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to FSM as Back Office Master Data Manger. | The screen Planning and Dispatching is refreshed.Note If the multiple company configuration is maintained for service contract, select the appropriate FSM Company. |  |
| 2 | Open Screen Master Data | In the drop-down field on the top left of the screen, select Master Data. | The screen Master Data is displayed. |  |
| 3 | Open Service Contract list | In the left navigation bar, choose Service Contract. | The Service Contract list is displayed. |  |
| 4 | Search Service Contract | In the search area, enter the code, description or ID of the service contract in S/4HANA. Choose a service contract in the result list. | The details of the service contract is displayed.Note If a service contract is set to Complete in S/4 HANA, the corresponding service contract in FSM will be set to Closed. | d |

### E2E Scenario: Create a Service Order in S/4HANA Cloud and Release it to FSM

#### Create a Service Order with Line Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to create a new service order in a standard scenario where items will be billed on the base of fixed price.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Customer Service Manager. | The Fiori Launchpad with access to the Manage Service Orders application is displayed. |  |
| 2 | Open Manage Service Orders application | Choose the Manage Service Orders application tile. | The list report page is displayed. |  |
| 3 | Open Create Service Order window | Choose Create from the Create Service Order options on the service order list page. | A Create Service Order window is displayed. |  |
| 4 | Maintain Service Order data | Enter the following data to create a service order:Service Order Type: Fixed Price OrderSold-To Party: for example, 17100003 for US (Domestic Customer US 3)Service Bundle: mark this optionDescription: your description of the service bundle orderAdd a service bundle as a main item:Product: for example, SRV_BUNDLE_01Quantity: for example, 1Unit: for example, EAChoose Save and Edit. | A new service order has been created.The edit view of the Service Order will be opened. |  |
| 5 | Add attachment to service order (optional) | On the Attachments tab, choose Add Attachment. Select the file you want to upload.Note Note that links cannot be added as attachments. | The file is added to the service order. |  |
| 6 | Maintain sub items under the service bundle item | Choose the Items tab or scroll down to the Items area.Add these items as sub items of the service bundle:Product ID: for example, SRV_01Higher-Level Item: Item No. of the service bundle, for example, 10Quantity: 1Unit: for example, HRChoose Enter.Product ID: for example, SRV_03Higher-Level Item: Item No. of the service bundle, for example,10Quantity: 1Unit: for example, EAChoose Enter.Choose Save.Note When service team is enabled in the S/4 Service, service team is mandatory for all the items. If multiple service teams meet the determination rule, please choose one entry in the pop-up window. | A service order with a service bundle including sub items has been created. |  |
| 7 | Add attachment to service item (optional) | In the Items screen area, go to the service item (For example, Product ID SRV_01) and choose Edit.On the Attachments tab, choose Edit. Select the file you want to upload.Return to the service order item list.Note Note that links cannot be added as attachments. | The file is added to the service order item. |  |

#### Release a Service Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step a line item of the previously created service order will be released. It is a prerequisite for a follow-up confirmation of that line item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Customer Service Manager. | The Fiori Launchpad with access to the Manage Service Order application is displayed. |  |
| 2 | Open Manage Service Order application | Choose the Manage Service Order application tile. | The list report page is displayed. |  |
| 3 | Find Service Order | In the search area on the top,enter <your description> in the filter Descriptionor enter the ID of your service order in the Search field.Choose Go. | Your service order is displayed in the report list within Manage Service Orders. |  |
| 4 | Open Service Order in the Edit mode | Choose Edit for your Service Order in the list | The edit view of the Service Order will be opened. |  |
| 5 | Release Service Order | In the tab area Service Order Details, change the Status from Open to ReleasedChoose Save. | Your service order has been released.A service call with an activity will be created in FSM.The FSM Service Call Id will be visible in the Service Order Header, tab Transaction History.The FSM Service Activity Ids will be visible in the Service Order Items, tab Transaction History. | Note down the Service Call number for later use.The Service Call Id can also be found on the Service Order → Transaction History → FSM Service Call. |
| 6 | Navigate to service call | Choose the Transaction History tab in your Service Order to see the FSM service call code.Click on the FSM service call code. | The corresponding Service Call is displayed.Note If the multiple company configuration is maintained for the service order, select the appropriate FSM Company. |  |

### E2E Scenario: Update a Released Service Order in S/4HANA Cloud and Re-release It

#### Update a Service Order with Line Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to update a released service order in a standard scenario.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Customer Service Manager. | The Fiori Launchpad with access to the Manage Service Orders application is displayed. |  |
| 2 | Open Manage Service Orders application | Choose the Manage Service Orders application tile.Search for your Service Order and select itChoose Edit | The App Manage Service Orders opens. |  |
| 3 | Edit and Change Service Order Header | Change the following properties of the service order header:DescriptionPriorityRequested End Date/TimeSection Notes: NoteSection Parties Involved: Employee Responsible. |  |  |
| 4 | Add attachment (optional) | On the Attachments tab, choose Upload. Select the file you want to upload.Note that links cannot be added as attachments. | The file is added to the service order. |  |
| 5 | Change Service Order Items | In the Section Items go to a replicated Service Item (Product ID SRV_01), press Edit, and change the existing item:QuantityRequested Start/Due date/timeProduct descriptionIn the section Notes: Change the noteIn the section Attachments: Upload an attachment (optional).Press BackIf the contract assignment dialog pops up, click No AssignmentGo back to the Service Order item list.Edit an item of Service part category (for example, SRV_03) and change the quantity.Go back to the Service order detail.Choose Save to save the Service Order. | Service Order is saved. Changes are replicated to FSM.In FSM, the Service Call displays all changed values correctly.The FSM Service Activity Ids will be visible correctly in the changed Service Order Items, tab Transaction History. | Changed properties are visible in FSM and iFlow processing is successful. |

### E2E Scenario: Update Service Order in S/4HANA Cloud When Service Call or Activity is Updated in FSM

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
| 3 | Assign Technician | In the Dispatching board there are list of Technicians with specific skill set. (place the cursor on technician name to know the skill set).Drag and drop the Service call on to the appropriate Technician based on the skill set required.Note Select today’s date in Planning board if not already updated.Select all the assignments relevant to Service call and then assign it to specific Technician.Currently, there is no mapping between S/4 Service and the FSM system for service teams. When dispatching a service technician to some activity in FSM, you must ensure that the service technician belongs to the service team assigned in the service order in S/4. Otherwise, a re-determination of the service team will be triggered in S/4. If the service technician belongs to multiple service teams, the automatic assignment in S/4 will lead to an error that has to be resolved manually. Consequently, it is preferable if you use a service technician that is assigned to exactly one service team in S/4. | Service call assigned to Technician is displayed on planning board. |  |
| 4 | Release assignment | On the Dispatching and Planning boardSelect all the assignments and choose Release Assignment (on the upper right side of the board). | The assignment is released. |  |
| 5 | Logon to S/4HANA | Log on to the SAP Fiori launchpad using the role Customer Service Manager. |  |  |
| 6 | Open Manage Service Orders application | Choose the Manage Service Orders application title.Search for your Service Order created above and open it.Open the that the following fields are filled correctly:Executing Service EmployeePlanned Start DatePlanned End DateCheck for both Items that you are not able to change the following fields via the UI:Executing Service Employee (change or add)Planned Start DatePlanned End DateCheck for both Items that the Execution Status is correct. “In Planning” for items successfully replicated to FSM. “In Execution” for items successfully released to a technician in FSM. | The App Manage Service Orders opens. |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to FSM as Planner/Dispatcher. | The screen Planning and Dispatching is displayed. |  |
| 2 | Find Activity | In the Dispatching dashboard, find the activity you have released by technician name. | The assigned activity is under the certain technician in the Dispatching dashboard. |  |
| 3 | Reassign Activity | In the Dispatching board, drag and drop the released activity on to the other appropriate Technician based on the skill set required. | The activity is assigned to the other technician. |  |
| 4 | Release Assignment | Select the reassigned activity, choose Release Assignment (on the upper right side of the board). | The assignment is released. |  |

#### Duplicate, Release, and Cancel Activity (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you duplicate the activity for another service technician and release the assignment

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to FSM as Planner/Dispatcher. | The screen Planning and Dispatching is displayed. |  |
| 2 | Find Activity | In the Dispatching dashboard, find the activity you have released by technician name. | The assigned activity is under the certain technician in the Dispatching dashboard. |  |
| 3 | Duplicate Activity | In the Dispatching board, select the activity and choose More on the upper right side of the pop-up window. Place your cursor onto Duplicate for and choose the other appropriate technician. | A new activity is created for the second technician. |  |
| 4 | Release Assignment | Select the new activity, choose Release Assignment (on the upper right side of the board).Note As for the new activity, a new service order line item in S4 system will be created with release status mapping to this new activity. | The assignment is released.The new FSM Service Activity Id will be visible in the Service Order Item, tab Transaction History. |  |
| 5 | Cancel Activity | In the Dispatching Board, find the Activity duplicated in the previous step and click it. In the popup, click on the 3-dot menu, then choose “cancel”. | In S/4HANA, search for your Service Order.Check for the cancelled Item that the Execution Status is “Cancelled” and the Life-Cycle Status is “Completed”.Check that the cancelled Item has the correct Rejection Reason Assigned by the System (Internal). |  |

#### Upload Attachment to a Service Call

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

It is possible to upload attachments to service calls. These attachments are replicated to service orders on S4 side.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to FSM as Service Planner/Dispatcher. | The screen Planning and Dispatching is displayed. |  |
| 2 | Find Service Call | In the Dispatching dashboard search for service call via <your description>. | Service call is displayed. |  |
| 3 | Upload Attachment | On the service call’s detail information, you find the area to upload an attachment. | Attachment is assigned to the service call and is replicated to SAP S/4HANA Cloud Public Edition.Check in SAP S/4HANA Cloud Public Edition if attachment is assigned to corresponding service order.Log on to the SAP Fiori launchpad using the role Customer Service Manager.Choose the Manage Service Order application tile.In the search area on the top, enter <your description> in the filter Description or enter the ID of your service order in the Search field.Choose Go. You find the attachment on the tab attachments. |  |
| 4 | Delete Attachment | Choose delete trash bin to delete the attachment and trigger deletion replication to SAP S/4HANA Cloud Public Edition. | Attachment is deleted on service call and deletion is replicated to SAP S/4HANA Cloud Public Edition.Check in SAP S/4HANA Cloud Public Edition if attachment has been deleted.Log on to the SAP Fiori launchpad using the role Customer Service Manager.Choose the Manage Service Order application tile.In the search area on the top, enter <your description> in the filter Description or enter the ID of your service order in the Search field.Choose Go. Attachment on the attachment tab is not available anymore. |  |

#### Upload Attachment to an Activity

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

It is possible to upload attachments to activities. These attachments are replicated to service order items on S4 side.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to FSM as Service Planner/Dispatcher. | The screen Planning and Dispatching is displayed. |  |
| 2 | Find Activity | In the Dispatching dashboard, find the activity you have released by technician name. | The assigned activity is under the certain technician in the Dispatching dashboard. |  |
| 3 | Upload Attachment | On the activity’s detail information you find the area to upload an attachment. | Attachment is assigned to the activity and is replicated to S4.Check on S/4HANA Cloud side if attachment is assigned to corresponding service order.Log on to the SAP Fiori launchpad using the role Customer Service Manager.Choose the Manage Service Order application tile.In the search area on the top, enter <your description> in the filter Description or enter the ID of your service order in the Search field.Choose Go. You find the attachment on the corresponding service order item on the tab attachments. |  |
| 4 | Delete Attachment | Choose delete trash bin to delete the attachment and trigger deletion replication to S/4HANA Cloud. | Attachment is deleted on service call and deletion is replicated to S/4HANA Cloud.Check on S/4HANA Cloud side if attachment is deleted.Log on to the SAP Fiori launchpad using the role Customer Service Manager.Choose the Manage Service Order application tile.In the search area on the top, enter <your description> in the filter Description or enter the ID of your service order in the Search field.Choose Go. Attachment on the attachment tab is not available anymore. |  |

### E2E scenario: Create Service Order with Items in S/4HANA Cloud when Service Call or Activity is Created in FSM

#### Create Service Call

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a new Service Activity in SAP FSM, which is then replicated to SAP S/4HANA Cloud Public Edition as new Service Order.

Procedure

| Test Step # | Test Step Name | Instruction | User Entries:Field Name: Value | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- | --- |
| 1 | Logon to FSM | a. Logon to the FSM System.b. Open View ‘Service Calls’.c. Press the Create Button in the bottom-right corner. |  |  |  |
| 2 | Create a new Service Call | a. Enter values for the following fields of the Service Call.- Customer- Contact Person- Subject- Priority- Earliest start date / time- Due date / time- Responsible- Service call remarks- Resolution- Equipment- Status: Ready-To-Planb. Press the Save Button: |  |  |  |
| 3 | Check the result in CPI Monitoring | a. Logon to the CPI.b. You should see a Message for the ‘Replicate Service Call from SAP Field Service Management to SAP S4HANA Cloud’.c. Check that the Message is in status ‘Completed’. |  | Message reaches SAP S/4HANA Cloud Public Edition successfully. |  |
| 4 | Check Result in SAP S/4HANA Cloud Public Edition. | a. Logon with your User to the corresponding SAP Fiori UIb. Click on tile Manage Service Order /Maintain Service Order.c. Search for your Service Order.d. Depending on Customizing and Test Data used the Service Order may have been created with Errors.e. In the Header Section.f. Check that the Sold To Party is correct.g. Check that the Description is correct.h. Check that the Contact is correct.i. Check that the Priority is correct (view section 2.3.2 for mapping details).j. Check that Requested Start is correct (Earliest start date / time).k. Check that Requested End is correct (Due date / time).l. Check that the Status is Open.m. Go to Section Parties Involved.n. Check that Employee Responsible is correct.o. Go to Section Reference Objects.p. Check that a Reference Object Entry with the chosen Equipment is available and flagged as Main.q. Go to Section Transaction History.r. Check that the FSM Service Call Entry has the correct Code assigned.s. Go to Section Notes.t. There should be two Notes available.u. Check that your Resolution Note is displayed as ‘Problem Description’.v. Check that your Service call remarks are displayed as Internal note. |  |  | When you create a new Service Call in FSM, is always implicitly an Activity created as well. Currently, this Activity is not being replicated to SAP S/4HANA Cloud Public Edition as there are still developments pending in FSM (Queuing Mechanism).For this test step, you should have no Items for the new Service Order.Note If multiple pieces of equipment are replicated from a Service Call to a Service Order in SAP S/4HANA Cloud Public Edition, the first piece of equipment (alphabetical order) is marked as main piece of equipment. |
| 5 | Check Result in FSM | a. Logon to the FSM System.b. Open View Service Calls.c. Open your Service Call.d. Check that the externalId of the Service Call is correct.e. Check that the Status of the Service Call is New (This is set by the flow for each new Service Call). |  |  |  |

#### Create Activity

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a new Service Activity in SAP FSM, which is then replicated to SAP S/4HANA Cloud Public Edition as new Service Order Item.

Procedure

| Test Step # | Test Step Name | Instruction | User Entries:Field Name: Value | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- | --- |
| 1 | Logon to FSM | a. Logon to the FSM Systemb. Open View ’Service Calls.c. Open your Service Call from the previous Test Step. |  |  |  |
| 2 | Create a new Activity | a. Enter values for the following fields of the Activity. For Test Data refer to the- Subject- Planned start date- Planned end date- Notes (for the technician)- Equipment- Original estimateb. Press the Save Button: |  |  | If original estimate is not filled, planned duration is mapped to SAP S/4HANA Cloud Public Edition Quantity as a fallback. |
| 3 | Check the result in CPI Monitoring | a. Logon to the CPI.b. You should see a Message for the ‘Replicate Service Call from SAP Field Service Management to SAP S4HANA Cloud’.c. Check that the Message is in status ‘Completed’. |  | Message reaches SAP S/4HANA Cloud Public Edition successfully. |  |
| 4 | Check Result in SAP S/4HANA Cloud Public Edition | a. Logon with your User to the corresponding SAP Fiori UI.b. Click on tile Search Service Order / Maintain Service Order.c. Search for your Service Order.d. Check that your Service Order has no Errors and is now in Status Released.e. Check that your Service Order Item was created in Status Released.f. Open your Item and go to section General Information.g. Check that the Description is correct.h. Check the Actual Duration and Quantity have the correct value.i. Go to Section Timeline.j. Check that Earliest Planned Start and Latest Planned End is correct.k. Go to Section Notes; your note should have be replicated as Item text.l. Got to Section Reference Objects.m. Check that the chosen Equipment is assigned and flagged as Main.n. Go to Section Transaction History.o. Check that the FSM Service Activity Entry has the correct Code assigned. |  |  |  |
| 5 | Check Result in FSM | a. Logon to the FSM System.b. Open View Service Calls.c. Open your Service Call.d. Check that the externalId of the Service Call is correct. |  |  |  |

### E2E Scenario: Create a Completed Service Confirmation in S/4HANA Cloud when Time Effort, Expense, or Material is Approved in FSM

#### Technician Starts Working on Activity

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity Technician starts working on the assigned activity.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to FSM as Service Technician - Customer Service on mobile application. | The message Change company is displayed. |  |
| 2 | Choose company | Choose the company you belong to, for example Company 3. | The messageCompany has never been synchronizedis displayed. |  |
| 3 | Sync | Choose Sync. | The screen showing all the Assignments assigned to technician is displayed. |  |
| 4 | Choose Activities | Choose assigned Activity from the list. | The screen Service call Description, Status, Customer, Address, Responsible, Reserved material, and Assignment details are displayed. |  |
| 5 | Choose travel | ChooseTravel. | The screen Are you ready to start traveling is displayed. |  |
| 6 | Start work | Choose Work (on the bottom-right side). | The messageI confirmis displayed. |  |
| 7 | Confirm | Choose Confirm. | The screen showing all the service details is displayed. |  |

#### Updates Time, Use Reserved Material, and Add Expenses

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
| 1 | Log on (optional) | Log on to FSM as Service Technician - Customer Service on mobile application. | The Message Change company is displayed. |  |
| 2 | Sync (Optional) | Choose the company you belong to and then choose Sync. | The screen showing all the assignments assigned to technician is displayed. |  |
| 3 | Choose Activities (optional) | Choose assigned Activities from the list. | The screen showing service call description, status, customer, address, Responsible, all Reserved material and assignment details are displayed. |  |
| 4 | Choose Reserved Material (Optional) | Choose Reserved materials > Use > Save. | The Reserved Material is updated.Note This step is mandatory only when the service call is derived from service orders that are created with spare part to be procured, for example SRV_04. |  |
| 5 | Choose Create | Choose Create (‘+’ symbol) at the bottom of screen. | The Screen showing Attachment, Checklist Expense, Effort, Feedback code, follow up material, and Mileage are displayed. |  |
| 6 | Choose Material | Choose Material from the list. | TheCreate Material screen is displayed. |  |
| 7 | Update Unplanned Material | Choose Item code, for example SRV_03, change Quantity if necessary, for example 2. Then choose Save.Note Please make sure the quantity in the individual stock for unplanned material in SAP S/4HANA system are enough, or it will cause error when creating confirmation. | The unplanned Material will be updated. |  |
| 8 | Choose Create | Choose Create (‘+’ symbol) at the bottom of screen. | The Screen showing Attachment, Checklist Expense, Effort, Feedback code, follow up material and Mileage are displayed. |  |
| 9 | Choose Effort | Choose Effort from the list. | The Screen showing New Effort is displayed. |  |
| 10 | Update Effort | Choose Time Entry - Choose Working time - update working time - Choose Effort Type - choose Save. | Time Effort will be updated. |  |
| 11 | Choose Create | Choose Create (‘+’ symbol) at the bottom of screen. | The Screen showing Attachment, Checklist Expense, Effort, Feedback code, Follow up material and Mileage are displayed. |  |
| 12 | Choose Expense | Choose Expense from the list. | The Screen showing Create Expense is displayed. |  |
| 13 | Update Expense | Choose Type -Choose Expense type - Choose Currency.Input amount in the field Internal Amount or External Amount.Choose Save. | Expense will be updated. |  |

#### Finish Work and Close Activity

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, Technician completes and confirms about the activity.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on (Optional) | Log on to FSM as Service Technician - Customer Service on mobile application. | The messageChange companyis displayed. |  |
| 2 | Sync (Optional) | Choose the company you belong to, then choose Sync. | The screen showing all the Assignments assigned to technician is displayed. |  |
| 3 | Choose Assignments (Optional) | Choose assigned Assignment from the list. | The screen showing Service call description, Status, Customer, Address, Responsible, Reserved material, and Assignment details are displayed. |  |
| 4 | Checkout | Choose Checkout – Choose Confirm – Efforts - Choose Save. | The Screen showing ‘Preview Report’ is displayed. |  |
| 5 | Choose Preview Report | Choose Preview Report – Choose Sync. | The Service Report is generated. |  |
| 6 | Sign | Choose CLICK TO SIGN HERE – Sign – update your name. | The screen showing Confirmed and closed is displayed. |  |
| 7 | Done | Choose Done. | The Screen with list of Activities is displayed. |  |
| 8 | Activity Status | Choose Activity from list of Activities.Check for the status of Activity. | The Screen Status – Closed is displayed. |  |

#### Manager Approves Time Effort/Expense and Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, planner approves the time effort, expenses and material used. Service Confirmation is automatically created in S/4HANA once the planner approves time and expenses in FSM.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to FSM as Service Planner/Dispatcher. | The screen Planning and Dispatching is displayed. |  |
| 2 | Navigate to time and expenses | Choose Time and Material journal . | The screen Time effort, Expense, Material, Mileage, and Overview are displayed. |  |
| 3 | Approve time effort | Choose Time effort on the top of the board.Choose your service call via Description from the list of Service calls and choose Approve. | The time effort added by Technician is approved.Once Time Effort is approved in FSM, a confirmation is created automatically in Service order. |  |
| 4 | Approve Expense | Choose Expense on the top of the board.Choose your service call via Description from the list of Service calls and choose Approve. | The Expense added by Technician is approved.Once Expenses are approved in FSM, the confirmation is created automatically in the Service order. |  |
| 5 | Approve Material | Choose Material on the top of the board.Choose your service call via Description from the list of Service calls and choose Approve. | The Material added by Technician is approved.Once Material is approved in FSM, the confirmation is created automatically in Service order. |  |
| 6 | Enter and approve unplanned mileage | Choose MILEAGE on the top of the board and click (add element) on the lower right corner.a. Enter the Service Call number you noted down earlier to find your Service Call.b. Select the Activity for Service A.c. Choose the corresponding Technician.d. Enter a distance, for example 100.e. Enter a comment in field Remarks.f. Choose Save. | The added Mileage is approved.Once Mileage is approved in FSM, the confirmation is created automatically in the S/4HANA Service Order. | Distance space or 0 leads to an erroneous message on CPI. |
| 7 | Log On | Log on to the SAP Fiori launchpad using the role Customer Service Manager. | The Fiori Launchpad with access to the Manage Service Order application is displayed. |  |
| 8 | Open Manage Service Order application | Choose the Manage Service Order application tile. | The list report page is displayed. |  |
| 9 | Find Service Order | In the search area on the top,enter <your description> in the filter Descriptionor enter the ID of your service order in the Search field.Choose Go. | Your service order is displayed in the report list within Manage Service Orders. |  |
| 10 | Service Confirmation | Choose the Items tab.Choose Confirmations to see the list of confirmed service order items; check the correct number of confirmation items in this list. | The completed Service Confirmation is displayed. |  |
| 11 | Service Confirmation Details | Compare the details with the values entered in FSM. | The Confirmation Items should show the values maintained in FSM. |  |

### E2E Scenario: Complete a Service Order in SAP S/4HANA Cloud Public Edition and Corresponding Service Call is Technically Completed in FSM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once Service confirmation is complete the corresponding Service items are completed and When all service items in a service order are completed in SAP S/4HANA Cloud Public Edition, the service order is completed automatically, and corresponding service call is automatically changed to Technically Complete in SAP Field Service Management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Customer Service Manager. | The Fiori Launchpad with access to the Manage Service Order application is displayed. |  |
| 2 | Open Manage Service Order application | Choose the Manage Service Order application tile. | The list report page is displayed. |  |
| 3 | Find Service Order | In the search area on the top,enter <your description> in the filter Descriptionor enter the ID of your service order in the Search field.Choose Go. | Your service order is displayed in the report list within Manage Service Orders. |  |
| 4 | Mark Service Order as Complete | Enter the found Service Order, choose buttonEdit , in the field Status, select Completed, and choose button Save. | The details of your Service Order are displayed as Completed. |  |
| 5 | Check service order | Check if the Service order is complete. | Once the Service order is complete in S4 HANA corresponding service call is Technically complete. |  |

### E2E Scenario: Create a Service Order in S/4HANA Cloud, Release it to FSM, and Reject the Service Order

#### Create a Service Order with Line Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to create a new service order in a standard scenario where items will be billed based on a fixed price.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Customer Service Manager. | The Fiori Launchpad with access to the Manage Service Orders application is displayed. |  |
| 2 | Open Manage Service Orders application | Choose the Manage Service Orders application tile. | The list report page is displayed. |  |
| 3 | Open Create Service Order window | Choose Create from the Create Service Order options on the service order list page. | A Create Service Order window is displayed. |  |
| 4 | Maintain Service Order data | Enter the following data to create a service order:Service Order Type: Fixed Price OrderSold-To Party: for example, 17100003 for US (Domestic Customer US 3)Service Bundle: mark this optionDescription: your description of the service bundle orderAdd a service bundle as a main item:Product: for example, SRV_BUNDLE_01Quantity: for example, 1Unit: for example, EAChoose Save and Edit. | A new service order has been created.The edit view of the Service Order is opened. |  |
| 5 | Maintain sub items under the service bundle item | Choose the Items tab or scroll down to the Items area.Add these items as sub items of the service bundle:Product ID: for example, SRV_01Higher-Level Item: Item No. of the service bundle, for example, 10Quantity: 1Unit: for example, HRChoose Enter.Product ID: for example, SRV_03Higher-Level Item: item number of the service bundle, for example,10Quantity: 1Unit: for example, EAChoose Enter.Choose Save.Note When service team is enabled in S/4 Service, service team is mandatory for all the items. If multiple service teams meet the determination rule, please choose one entry in the pop-up window. | A service order with a service bundle including sub items has been created. |  |

#### Release a Service Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step a line item of the previously created service order will be released. It is a prerequisite for a follow-up confirmation of that line item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Customer Service Manager. | The Fiori Launchpad with access to the Manage Service Order application is displayed. |  |
| 2 | Open Manage Service Order application | Choose the Manage Service Order application tile. | The list report page is displayed. |  |
| 3 | Find Service Order | In the search area on the top, enter <your description> in the filter Description or enter the ID of your service order in the Search field.Choose Go. | Your service order is displayed in the report list within Manage Service Orders. |  |
| 4 | Open Service Order in the Edit mode | Choose Edit for your Service Order in the list. | The edit view of the Service Order is opened. |  |
| 5 | Release Service Order | In the tab area Service Order Details, change the Status from Open to Released.Choose Save. | Your service order has been released.A service call with an activity will be created in SAP Field Service Management.The FSM Service Call ID will be visible on the Transaction History tab in the Service Order Header.The FSM Service Activity IDs will be visible on the Transaction History tab in the Service Order Items. | Note down the Service Call number for later use.The Service Call ID can also be found under Service Order > Transaction History > FSM Service Call . |
| 6 | Navigate to service call | Choose the Transaction History tab in your Service Order to see the FSM Service Call code.Click on the FSM Service Call code. | Corresponding Service Call is displayed.Note If the multiple company configuration is maintained for the service order, select the appropriate FSM Company. |  |

#### Reject a Service Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step a line item of the previously created service order will be cancelled.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Customer Service Manager. | The Fiori Launchpad with access to the Manage Service Order application is displayed. |  |
| 2 | Open Manage Service Order application | Choose the Manage Service Order application tile. | The list report page is displayed. |  |
| 3 | Find Service Order | In the search area on the top, enter <your description> in the filter Description or enter the ID of your service order in the Search field.Choose Go. | Your service order is displayed in the report list within Manage Service Orders. |  |
| 4 | Open Service Order | Click on your Service Order in the list. | The Service Order is opened. |  |
| 5 | Reject the Service Order | In the header area, click on three dots menu.In the Reject Service Order pop-up, select any Rejection Reason.Choose OK.Choose Save. | The status of the service order and line items are set to Completed. |  |
| 6 | Navigate to service call | Choose the Transaction History tab in your Service Order to see the FSM Service Call code.Click on the FSM Service Call code. Check the status of Service Call and Activities. | The corresponding Service Call is displayed and the status is set to Technically Completed.The Activities status is set to Cancelled.Note If the multiple company configuration is maintained for the service order, select the appropriate FSM Company. |  |

### E2E Scenario: Create and Release a Repair Order in S/4HANA Cloud; Create and Approve a Time Effort in FSM

#### Create and Release a Repair Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to create a new In-House Repair, add one Repair Object, create a Repair Order, and Release it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Repair Order Manager (CUST_SRVC_MGR_REPA).Note Ensure that the relevant employee is replicated as People in SAP Field Service Management. Otherwise, the replication of the repair order won't work. | The Fiori Launchpad with access to the Manage In-House Repairs application is displayed. |  |
| 2 | Open Manage In-House Repairs application | Choose the Manage In-House Repairs application tile. | The list report page is displayed. |  |
| 3 | Open Create In-House Repair window | On the worklist open link Create. | A simple Create In-House Repair window is displayed. |  |
| 4 | Create a new In-House Repair | On the create screen New In-House Repair enter the necessary field ‘Sold-to party’ = 17100001.The fields for Sales Org, Distribution Channel, and Division are filled automatically; if not, select one of the Sales Organizations from its value help.Choose Create. | A new In-House Repair has been created.Remember the In-House Repair ID. |  |
| 5 | Add Repair objects | In screen section Repair Objects, press button Add. Search and select an equipment that also exists in FSM and choose Add. | The Repair Object is added. |  |
| 6 | Confirm In-House Repair | Press button Confirm. | The In-House Repair is confirmed and is in status In Process. |  |
| 7 | Close application | Navigate to the Launchpad Home Page. |  |  |
| 8 | Start application Perform Prechecks | Click on Perform Prechecks. |  |  |
| 9 | Open details for Repair Object | In the worklist search for a previously created Repair object and navigate into the details. | The detail screen for the Repair Object is displayed. The Repair Object shall have status Precheck: Decision Pending. |  |
| 10 | Check Availability Status | In screen section General Information, there is a sub section Logistics. Check sub section Logistics. | The field Availability shall display the status ‘Not Tracked’. The field Customer RMA number shall be empty. |  |
| 11 | Check Transaction History | Scroll to screen section Transaction History. | The In-House Repair is in status In Process. |  |
| 12 | Create Repair Order | In screen section Decide, click on Create Repair Order. | The Repair Object shall have status Precheck: Order. |  |
| 13 | Navigate to Repair Order | Scroll to screen section Transaction History and click on item Repair Order; in the pop-up, click on Display Repair Order. | The detail screen for the Repair Order is displayed. |  |
| 14 | Add Repair Item | In screen section Items, choose Edit List.Insert the service SRV_01, a quantity, and status Released. | Repair Item added to the Repair Order. |  |
| 15 | Release the Repair Order | In the section Repair Order Details, click on Edit.Enter a Description, set the Repair Order Status to Released, and click on Save. | Remember your Repair Order ID. |  |
| 16 | Check status of replicated Repair Order in FSM | Logon to your FSM tenant and checkThe existence of the replicated Repair Order by its ID in Planning and Dispatching > Service Calls > External IDThe type of the replicated Repair Order.Note If the multiple company configuration is maintained for the service order, select the appropriate FSM Company. | The External ID should be the Repair Order ID above.The type can be found in Value Mapping between, ServiceOrder/TransactionType vs. ServiceCall/Type, mapped against ‘RPO1’ |  |

#### Create and Approve a Time Effort in FSM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step checks that the Repair Order is replicated to FSM as a Service Call; it creates and approves a Time Effort.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon to FSM tenant | Open FSM.If needed, choose the correct company via the user setting in the upper right corner. |  |  |
| 2 | Navigate to Service Calls | Select Planning and Dispatching from the drop-down list in the header bar.Select Service Calls. | You can see the list of Service Calls. |  |
| 3 | Check replicated Repair Order | Find the Service Call with the Repair Order ID remembered previously (visible in the field External ID). | The Service Call shall be available.Remember the Service Call ID. |  |
| 4 | Assign Activity to Technician | Navigate to Planning and Dispatching > Dispatching Board .Find the activity with the Service Call Code remembered above and assign it to one of the technicians.Select the activity in the Dispatching Board and choose RELEASE ASSIGNMENTS (1) in the top-right corner. | The details of your Service Order are displayed as Completed. |  |
| 5 | Create a Time Effort | Navigate to Planning and Dispatching > Time and Material Journal .Click on the + sign in the bottom-right corner.In the pop-up Add Effort, fill the fields Service Call, Activity, Technician and eventually some of the other fields.Click on Save. | The Time Effort shall be inserted in the list of efforts. |  |
| 6 | Approve the Time Effort | Select your Time Effort in the list of efforts by choosing the select button in the first column.Click on Approve (1) in the header row. | The Time Effort shall disappear from the list of efforts.A message that confirms the effort shall be sent to S/4HANA. |  |

#### Check Confirmation in S/4HANA Cloud

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step checks the results of the FSM Time Effort Approval in the S/4HANA Cloud Repair Order Confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Customer Service Manager. | The Fiori Launchpad with access to the Perform Prechecks application is displayed. |  |
| 2 | Start application Perform Prechecks | Choose the Perform Prechecks application tile. | You can see a list of Repair Objects. |  |
| 3 | Navigate to your In-House Repair | Enter the In-House Repair ID remembered above into selection field In-House Repair and choose Go.Select the remaining Repair Object in the list below. | You are in the screen Perform Precheck Details of your Repair Object. |  |
| 4 | Navigate to your Repair Confirmation | In the screen area Transaction History, choose Repair Confirmation.. | You can see the details of the Repair Confirmation. |  |

### E2E Scenario: Create a Smartform Template and Instance in SAP FSM and visualize SAP SAP/S4HANA

#### Create and Release a Smartform Template

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | State the Service Provider, Customer or Joint Service Provider and Customer |

Purpose

This step describes how to create a smartform template in SAP Field Service Management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon to FSM tenant | Open FSM.If needed, choose the correct company via the user setting in the upper right corner. |  |  |
| 2 | Navigate to Templates | Select Smartforms and Feedback from the drop-down list in the header bar.Select Templates. | You can see the list of categories containing Templates. |  |
| 3 | Create a new Category | Click on +, and select Create new category.Enter the category name and click on Create. | New Category should be created. |  |
| 4 | Create a new Template | Click on +, and select Create new template.Enter the template name.Select the category created in the previous step.Click on Create. | New Template should be created. |  |
| 5 | Add elements to the template | On the right side, we see the Elements section.From the list of elements, select Chapter by clicking on + icon.Add all the required elements for the template. | New elements should be added to the template. |  |
| 6 | Release the Template | Once all the elements are arranged and added, click on Status/Version drop down and select Released. | Template should be released in FSM. |  |
| 7 | Log On to S/4HANA system | Log on to the SAP Fiori launchpad using the role Customer Service Manager. | The Fiori Launchpad with access to the Smartform Template Viewer application is displayed. |  |
| 8 | Open Smartform Template Viewer application | Choose the Smartform Template Viewer application tile. | The list report page is displayed. |  |
| 9 | Find Smartform Template | In the search area on the top, enter <your description> in the filter Description, or choose the ID of your smartform template in the Search field.Choose Go. | Your Smartform Template is displayed in the report list within Smartform Template Viewer. |  |
| 100 | Open Smartform Template | Click on your Smartform Template in the list. | The Smartform Template is opened. |  |
| 11 | View Smartform Template details | Scroll to screen section Smartform Template and check if all the details displayed are correct.Scroll to screen section Smartform Template Category and check if all the category details displayed are correct.Scroll to screen section Smartform Template Text and check if all the details displayed are correct.Scroll to screen section Smartform Template Element and check if all the element details displayed are correct.Click on any element in the list and check if all the element & element text details displayed are correct. | Smartform Template details in SAP Field Service Management should match correctly. |  |

#### Create and Release a Smartform Instance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | State the Service Provider, Customer or Joint Service Provider and Customer |

Purpose

This step describes how to create a smartform instance in SAP Field Service Management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Logon to FSM tenant | Open FSM.If needed, choose the correct company via the user setting in the upper right corner. |  |
| 2 | Navigate to Instances | Select Smartforms and Feedback from the drop-down list in the header bar.Select Instances. | You can see the list of instances. |
| 3 | Create a new Instance | Click on + to create a new instance.Select the template created in previous procedure in Select Object Type.Select an element or activity which was replicated in previous procedure in Select Object.Enter the description in Create Smartform.Click on Save. | New Instance should be created. |
| 4 | Open the newly created Instance | Select the newly created instance from the list of instances displayed. | Newly created Instance should be displayed. |
| 5 | Add values in the fields | Add or select values based on the instance design. | Values should be added/selected in the Instance. |
| 6 | Close the Instance | Once values are added to the elements, click on Close. | Values should be saved and the Instance should be closed. |
| 7 | Log On to S/4HANA system | Log on to the SAP Fiori launchpad using the role Customer Service Manager. | The Fiori Launchpad with access to the Smartform Instance Viewer application is displayed. |
| 8 | Open Smartform Instance Viewer application | Choose the Smartform Instance Viewer application tile. | The list report page is displayed. |
| 9 | Find Smartform Instance | In the search area on the top, enter <your description> in the filter Description, or choose the ID of your smartform instance in the Search field.Choose Go. | Your Smartform Instance is displayed in the report list within Smartform Instance Viewer. |
| 10 | Open Smartform Instance | Click on your Smartform Instance in the list. | The Smartform Instance is opened. |
| 11 | View Smartform Instance details | Scroll to screen section Smartform Instance and check if all the details displayed are correct.Scroll to screen section Smartform Instance Text and check if all the details displayed are correct.Scroll to screen section Smartform Instance Value and check if all the element values details displayed are correct. | Smartform Instance details in SAP Field Service Management should match correctly. |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can proceed this process.

| Process | Business Condition |
| --- | --- |
| 3D2 - Service Order Management and Monitoring | The preliminary steps in the 3D2 should be executed, in order to make sure that service management process could be run successfully. |
| 3NI-Procurement for Service Management | If spare parts need to be procured outside, the preliminary steps in the 3NI should be executed. |
| 3MO-Service Contract Management | If Service Contract needs to be synchronized to FSM, the preliminary steps in 3MO should be executed. |

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
> Flagged while digesting this document, not verified: Overview Table says the key characteristic of this process variant is that total billed amount is calculated on time and material, while the service order test procedures create a 'Fixed Price Order' with items billed on a fixed price basis.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/maintenance-order-processing-with-sap-field-service-management-7z2-ae]]
- related-to :: [[14-maintenance-service-and-projects/test-script-sap-maintenance-assistant-4rv-sap-s-4hana-cloud-public-edi]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/49X_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 82,063 chars in the whole document
