---
id: 14-maintenance-service-and-projects/test-script-credit-and-debit-memo-processing-for-service-management-4g
title: "Test Script: Credit and Debit Memo Processing for Service Management (4GG_AE) (4GG_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 4GG_AE: credit/debit memo requests, approval, rework and billing for service processes."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/service-order-management-and-billing]
aliases: [4GG_S4CLD2608_BPD_EN_AE]
keywords: [Service Order Management and Billing, credit memo processing, debit memo processing, credit memo requests, debit memo requests, memo request approval, service management, scope item testing, request rework, billing creation job]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4GG_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1023
topic: 14-maintenance-service-and-projects/service-order-management-and-billing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Credit and Debit Memo Processing for Service Management (4GG_AE) (4GG_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4GG_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Service Order Management and Billing** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Credit and Debit Memo Processing for Service Management (4GG_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232854576)

[2 Prerequisites 4](#_Toc232854577)

[2.1 System Access 4](#_Toc232854578)

[2.2 Roles 4](#_Toc232854579)

[2.3 Master Data, Organizational Data, and Transactional Data 5](#_Toc232854580)

[2.4 Additional Manual Configuration 6](#_Toc232854581)

[2.4.1 Enable Invoice Correction for NORM Materials 6](#_Toc232854582)

[2.5 Business Conditions 9](#_Toc232854583)

[3 Overview Table 10](#_Toc232854584)

[4 Test Procedures 11](#_Toc232854585)

[4.1 Create Credit Memo with Reference to Invoice for Service Contract, Service Order, or Service Confirmation 11](#_Toc232854586)

[4.1.1 Create Credit Memo Request for corrected amount 11](#_Toc232854587)

[4.1.2 Create Credit Memo Request for corrected and actual amount 13](#_Toc232854588)

[4.1.3 Credit Memo Request Approval (Optional) 15](#_Toc232854589)

[4.1.3.1 Rework Credit Memo Request 17](#_Toc232854590)

[4.1.3.1.1 Check the Notifications 17](#_Toc232854591)

[4.1.3.1.2 Change Credit Memo Request 18](#_Toc232854592)

[4.1.4 Create Credit Memo 19](#_Toc232854593)

[4.2 Create Debit Memo with Reference to Invoice for Service Contract, Service Order, or Service Confirmation 21](#_Toc232854594)

[4.2.1 Create Debit Memo Request 21](#_Toc232854595)

[4.2.2 Create Debit Memo Request for Corrected and Actual Amount 22](#_Toc232854596)

[4.2.3 Debit Memo Request Approval (Optional) 24](#_Toc232854597)

[4.2.3.1 Rework Debit Memo Request 26](#_Toc232854598)

[4.2.3.1.1 Check the Notifications 26](#_Toc232854599)

[4.2.3.1.2 Change Debit Memo Request 27](#_Toc232854600)

[4.2.4 Create Debit Memo 28](#_Toc232854601)

[5 Appendix 30](#_Toc232854602)

[5.1 Process Integration 30](#_Toc232854603)

[5.1.1 Preceding Processes 30](#_Toc232854604)

[5.1.2 Succeeding Processes 30](#_Toc232854605)

## Purpose

Overview

A credit and a debit memo request is created against a service process (such as a service contract) with the amount to be credited or debited. The request is placed for approval. Once reviewed and approved, a credit or debit memo is created, sent to the customer, and posted to a journal entry.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data, and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Customer Service Manager | SAP_BR_CUSTOMER_SRVC_MGR | Service Management / Service Management – SAP Field Service and Asset Management | SAP_BR_CUSTOMER_SRVC_MGR / SAP_S4CRM_SPT_FSM_PC | Your system administrator provides the user and password information. |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK | Your system administrator provides the user and password information. |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC | Your system administrator provides the user and password information. |
| Sales Manager | SAP_BR_SALES_MANAGER | Sales Management / Internal Sales / Billing for Sales Manager / Customer Returns for Sales Manager | SAP_BR_SALES_MANAGER / SAP_SD_SPT_INT_SALES_SALES_MGR_PC / SAP_SD_SPT_BILLING_SALES_MGR_PC / SAP_SD_SPT_RETURNS_SALES_MGR_PC | Your system administrator provides the user and password information. |

### Master Data, Organizational Data, and Transactional Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials and customers.

|  |
| --- |
| Note The sample customer and sales organization mentioned below are available in your system if you have activated the US scope. For other country versions, use the master data available for your country. You can find an overview of sample master data here: [SAP Signavio Process Navigator](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/latest) → Accelerators → Reference: Master data overview. |

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Customer | 33100001 | Domestic UAE Customer 1 | Make sure that the customer you use for this process has either assigned the customer pricing procedure 01 (Procedure 01) or no procedure.to check the assignment, use Business Role SAP_BR_BUPA_MASTER_SPECIALIST - tile Manage Customer Master Data in the Sales Area Data. |
| Employee | - | < Use your own employee ID that is assigned to your user ID.> |  |
| Service product (services) | SRV_01SRV_CONTRACT | ServicesService Contract Product |  |
| Sales Organization | 3310 | Dom. Sales Org |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| 3KV | Create Service Product for Service Processes - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/12e989806107f75efee4881e1c494055)

#### Enable Invoice Correction for NORM Materials

In order to support stock service part materials with the item category group NORM in invoice correction (sales document types CBII and RK), execute the below steps.

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The Fiori Launchpad is displayed. |  |
| 2 | Access the Manage Your Solution App | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Configure pricing for customers and materials in sales | Search with following criteria:Application Area: SalesSub Application Area: Sales Order Management and ProcessingChoose Configure for Assign Item Categories. | The Assign Item Categories: Change is displayed. |  |
| 4 | Entry changes | In the Assign Item Categories: Change screen, search for the following procedure:SaTy: CBIIItCGr: NORMUsge: <empty>HLevItCa: <empty>DfItC: G2NMItCa: L2NEdit the entry according to the below mentioned values:MItCa: <SG2N>MItCa: <SL2N>Search for the following procedure:SaTy: RKItCGr: NORMUsge: <empty>HLevItCa: <empty>DfItC: G2NMItCa: L2NEdit the entry according to the below mentioned values:MItCa: <SG2N>MItCa: <SL2N>Choose SaveThe new entries are saved to Assign Item Categories. | The Assign Item Categories entries are maintained. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The Fiori Launchpad is displayed. |  |
| 2 | Open Assign Item Categories | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Item Categories.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Item Categories screen is displayed. |  |
| 3 | Configure pricing for customers and materials in sales | Search with following criteria:Application Area: SalesSub Application Area: Sales Order Management and ProcessingChoose Configure for Assign Item Categories. | The Assign Item Categories: Change is displayed. |  |
| 4 | Entry changes | In the Assign Item Categories: Change screen, search for the following procedure:SaTy: CBIIItCGr: NORMUsge: <empty>HLevItCa: <empty>DfItC: G2NMItCa: L2NEdit the entry according to the below mentioned values:MItCa: <SG2N>MItCa: <SL2N>Search for the following procedure:SaTy: RKItCGr: NORMUsge: <empty>HLevItCa: <empty>DfItC: G2NMItCa: L2NEdit the entry according to the below mentioned values:MItCa: <SG2N>MItCa: <SL2N>Choose SaveThe new entries are saved to Assign Item Categories. | The Assign Item Categories entries are maintained. |  |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 3D2 - Service Order Management and Monitoring | An invoice is created for a service order or service confirmation |
| 3MO - Service Contract Management | An invoice is created for a billing request line of a service contract |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Create Credit Memo Request for corrected amount | Internal Sales Representative | Manage Credit Memo Requests (F1989) | Credit memo request is created. |
| Create Credit Memo Request for corrected and the actual amount | Internal Sales Representative | Manage Credit Memo Requests (F1989) | Credit memo request is created. |
| Credit Memo Request Approval | Sales Manager | My Inbox - All Items (F0862) | Credit memo request is approved. |
| Create Credit Memo | Billing Clerk | Create Billing Documents (F0798) | Credit memo is created. |
| Create Debit Memo Request for corrected and the actual amount | Internal Sales Representative | Manage Debit Memo Requests (F1988) | Debit memo request is created. |
| Debit Memo Request Approval | Sales Manager | My Inbox - All Items (F0862) | Debit memo request is approved. |
| Create Debit Memo | Billing Clerk | Create Billing Documents (F0798) | Debit memo is created. |

## Test Procedures

This section describes the test procedures for each process step that belongs to this scope item.

### Create Credit Memo with Reference to Invoice for Service Contract, Service Order, or Service Confirmation

You can create a credit memo request in the following ways:

1. [Create Credit Memo Request for corrected amount](#unique_12) [page ] 11
2. [Create Credit Memo Request for corrected and actual amount](#unique_13) [page ] 13

#### Create Credit Memo Request for corrected amount

Purpose

The internal sales representative creates a credit memo request with reference to an invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Credit Memo Requests | Choose the Manage Credit Memo Requests (F1989) application tile. | The Manage Credit Memo Requests screen is displayed. |  |
| 3 | Navigate to Create Credit Memo Request | Choose Create Credit Memo Request. | The Create Sales Documents screen is displayed. |  |
| 4 | Create Credit Memo | Make the following entries:Order Type: SCR (Cre.Memo Req.f.Service)Choose Create with Reference.In field Billing Document, enter the invoice number which have been created in chapter ‘Create Billing Document’ of test script 3D2 or 3MO.Choose Item Selection.Choose Copy.Choose Enter. | The Create Credit Memo Request Overview screen is displayed. |  |
| 5 | Optional: Change Quantity | Change the following entry and choose Enter:Target Quantity: <For example, 0.5 HR>Note Reduce the original quantity, for example from 1.0 HR to 0.5 HR or 1 PC to 0.5 PC. | The quantity that shall be credited is entered. |  |
| 6 | Enter Order Reason | On the Sales tab, enter an order reason, for example, Poor Quality. | The order reason is recorded. |  |
| 7 | Remove Billing Block | On the Sales tab, remove the default billing block by selecting a Blank billing block. | The billing block is removed from credit memo request. |  |
| 8 | Save | Choose Save.Note the ID of the credit memo request. | The Credit Memo Request is created.Note If Credit Memo request needs an approval then follow the steps mentioned in [Credit Memo Request Approval (Optional)](#unique_14) [page ] 15, otherwise proceed with the steps mentioned in [Create Credit Memo](#unique_15) [page ] 19. |  |
| 9 | Check Transaction History in Service Contract | Log on to the SAP Fiori launchpad using the role Customer Service Manager. | The Fiori Launchpad with access to the Manage Service Contracts application is displayed. |  |
| 10 | Open Manage Service Contracts application | Choose the Manage Service Contracts application tile. | The list report page is displayed. |  |
| 11 | Search for the Service Contract | To find the service contract use the available filters, for example Service Contract:Choose Go. | The searched service contract is displayed in the result list. |  |
| 12 | Select Service Contract | Select the Service Contract for which a credit memo request was created. | The Service Contract Details screen is displayed. |  |
| 13 | Check Transaction History | Scroll to section Transaction History. | The Transaction ID for the credit memo request is displayed in the list. |  |
| 14 | Check Transaction History in Service Order | Log on to the SAP Fiori launchpad using the role Customer Service Manager. | The Fiori Launchpad with access to the Manage Service Orders application is displayed. |  |
| 15 | Open Manage Service Orders application | Choose the Manage Service Orders application tile. | The list report page is displayed. |  |
| 16 | Search for the Service Order | To find the service order use the available filters, for example Service Order:Choose Go. | The searched service order is displayed in the result list. |  |
| 17 | Select Service Order | Select the Service Order for which a credit memo request was created | The Service Order Details screen is displayed. |  |
| 18 | Check Transaction History | Scroll to section Transaction History. | The Transaction ID for the credit memo request is displayed in the list. |  |

#### Create Credit Memo Request for corrected and actual amount

Purpose

The internal sales representative creates a credit memo request with reference to an invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Credit Memo Requests | Choose the Manage Credit Memo Requests (F1989) application tile. | The Manage Credit Memo Requests screen is displayed. |  |
| 3 | Navigate to Create Credit Memo Request | Choose Create Credit Memo Request. | The Create Sales Documents screen is displayed. |  |
| 4 | Create Credit Memo | Make the following entries:Order Type: RK (Invoice Correction Req.)Choose Create with Reference.In field Billing Document, enter the invoice number which have been created in chapter ‘Create Billing Document’ of test script 3D2 or 3MO.Choose Item Selection.Choose Copy.Choose Enter. | The Create Credit Memo Request Overview screen is displayed. |  |
| 5 | Optional: Change Quantity | Change the second entry and choose Enter:Target Quantity: <For example, 0.5 HR>Note Reduce the original quantity, for example from 1.0 HR to 0.5 HR or 1 PC to 0.5 PC. | The quantity that shall be credited is entered. |  |
| 6 | Enter Order Reason | On the Sales tab, enter an order reason, for example, Poor Quality. | The order reason is recorded. |  |
| 7 | Remove Billing Block | On the Sales tab, remove the default billing block by selecting a Blank billing block. | The billing block is removed from credit memo request. |  |
| 8 | Save | Choose Save.Note the ID of the credit memo request. | The Credit Memo Request is created.Note If Credit Memo request needs an approval then follow the steps mentioned in [Credit Memo Request Approval (Optional)](#unique_14) [page ] 15, otherwise proceed with the steps mentioned in [Create Credit Memo](#unique_15) [page ] 19. |  |
| 9 | Check Transaction History in Service Contract | Log on to the SAP Fiori launchpad using the role Customer Service Manager. | The Fiori Launchpad with access to the Manage Service Contracts application is displayed. |  |
| 10 | Open Manage Service Contracts application | Choose the Manage Service Contracts application tile. | The list report page is displayed. |  |
| 11 | Search for the Service Contract | To find the service contract use the available filters, for example Service Contract.Choose Go. | The searched service contract is displayed in the result list. |  |
| 12 | Select Service Contract | Select the Service Contract for which a credit memo request was created. | The Service Contract Details screen is displayed. |  |
| 13 | Check Transaction History | Scroll to section Transaction History. | The Transaction ID for the credit memo request is displayed in the list. |  |

#### Credit Memo Request Approval (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the sales manager approves the credit memo request.

Prerequisite

Approval status of the Credit Memo Request is In Approval.

For the automatic creation of a Credit Memo a billing creation job should be scheduled.

Follow the below steps to schedule a billing creation job for the automatic creation of a Credit Memo.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Billing Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Schedule Billing Creation app. | The Schedule Billing Creation screen displayed. |  |
| 3 | Create Job | Choose Create. | The New Job: Schedule Billing Creation screen displayed. |  |
| 4 | Select Template | Make the following entries:Job Template: Schedule Billing CreationJob Name: Schedule Billing Creation for Credit MemoChoose Step 2. |  |  |
| 5 | Maintain Schedule Options | Make the following entries:Choose Start ImmediatelyRecurrence Pattern: Single RunChoose Step 3. |  |  |
| 6 | Maintain Parameters | In Documents to be selected section in the Parameters step, make the following entries :Choose No Docs with Billing BlockChoose Order-Related |  |  |
| 7 | Execute Job | Choose Schedule. | The job is executed and Credit memo is created. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Sales Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Receive Notification | Open My Inbox - All Items.You can also choose the Notifications icon on the top right corner to navigate to the My Inbox screen. | The Inbox screen is displayed. |  |
| 3 | Refresh | Choose Refresh, if necessary. | Inbox is refreshed. |  |
| 4 | Approve | You receive the notification of the credit memo request. Choose one of the options from the bottom bar.Option 1: ReleaseOption 2: RejectOption 3: Request Rework | The Submit Decision dialog box is displayed. |  |
| 5 | Submit | Enter some comments and choose Submit. | Based on the above selections, follow the next steps accordingly:Release: the whole process ends, no subsequent step is needed and Credit Memo is created.Note Credit memo will be created automatically, if the Schedule Billing Creation job is scheduled.For manual creation of Credit Memo proceed to [Create Credit Memo](#unique_15) [page ] 19.Reject: the whole process ends, no subsequent step is needed.Request Rework: go to [Rework Credit Memo Request](#unique_16) [page ] 17. |  |

##### Rework Credit Memo Request

|  |
| --- |
| Note Only relevant, if the workflow is set as Request Rework by the sales manager previously. |

###### Check the Notifications

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, internal sales representative check the notifications.

Prerequisite

Approval status of the sales order is To be reworked.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Receive Notification | Open My Inbox - All Items (F0862).You can also choose the Notifications icon on the top right corner to navigate to the My Inbox screen. | The Inbox screen is displayed. |  |
| 3 | Refresh | Choose Refresh, if necessary. | Inbox is refreshed. |  |
| 4 | Check Inbox | Check the inbox items with relative Credit Memo Request. | Orders which need to be reworked are displayed.If rework is not required, the sales representative can set the status to Rework not Required in the inbox.If rework is required, follow the steps in [Change Credit Memo Request](#unique_18) [page ] 18. |  |

###### Change Credit Memo Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, internal sales representative change the credit memo request.

Prerequisite

Approval status of the credit memo request is rework.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Billing Documents application | Choose the Manage Credit Memo Requests application tile. | The Credit Memo Request Overview screen is displayed. |  |
| 3 | Navigate to Manage Credit Memo document | In the field Credit Memo Request enter the respective credit memo request document ID created in [Check the Notifications](#unique_17) [page ] 17.Choose Go.Choose the row in the search result list containing the ID you are searching for to navigate to the credit memo request. |  |  |
| 4 | Change Credit Memo Request | On the Change Credit Memo Request Overview screen, make some changes, for example:Valid to: <Enter a date> | The approval status is changed to In Approval.Sales Manager will receive a task in the mailbox. Follow the steps in [Credit Memo Request Approval (Optional)](#unique_14) [page ] 15. |  |

#### Create Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to generate a billing document as a result of an approved credit memo request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Billing Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen is displayed. |  |
| 3 | Define Billing Setting | Choose Billing Setting.You can make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing document after creation: ON |  |  |
| 4 | Find Credit Memo Request in Search | Maintain the following search criteria:SD Document Category: <Credit Memo Request>In addition, you can enter the number of your credit memo request as search term. | Your credit memo request is displayed in the list. |  |
| 5 | Choose Credit Memo Request | Select your credit memo request in the list.Choose Create Billing Documents. | The Create Billing Documents screen is displayed. |  |
| 6 | Maintain Billing Date | Choose billing type Credit Memo (G2) and maintain billing date, for example, <current date>.Choose OK. |  |  |
| 7 | Display Billing Document after Creation | On the Billing Document (F1901) screen, choose Save.The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. | The credit memo is created. |  |

### Create Debit Memo with Reference to Invoice for Service Contract, Service Order, or Service Confirmation

#### Create Debit Memo Request

Purpose

This process step shows you how to generate a billing document as a result of a debit memo request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Debit Memo Requests | Choose the Manage Debit Memo Requests application tile. | The Manage Debit Memo Requests screen is displayed. |  |
| 3 | Navigate to Create Sales Document Screen | Choose Create Debit Memo Request. |  |  |
| 4 | Enter Sales Document Type | Make the following entries:Order Type: SDR (Deb. MemoReq. F. Srv) |  |  |
| 5 | Enter Order Details | Choose Create with reference. | The Create with Reference screen is displayed. |  |
| 6 | Choose the Reference Document | Enter the invoice number and choose Copy.Note If you are referencing a billing with related batch materials, after inputting the billing number, choose Item selection. Choose the item with open quantity and choose Copy. |  |  |
| 7 | Enter Order Reason | Choose the Sales tab. Enter an order reason (for example, 007 Fast Delivery). |  |  |
| 8 | Remove Billing Block | On the Sales tab, remove the default billing block by selecting Blank billing block. | Billing block removed from debit memo request. |  |
| 9 | Save | Choose Save. | The Debit Memo Request is created.Note If Debit Memo request needs an approval then follow the steps mentioned in [Debit Memo Request Approval (Optional)](#unique_20) [page ] 24. |  |
| 10 | Check Transaction History in Service Contract | Log on to the SAP Fiori launchpad using the role Customer Service Manager. | The Fiori Launchpad with access to the Manage Service Contracts application is displayed. |  |
| 11 | Open Manage Service Contracts application | Choose the Manage Service Contracts application tile. | The list report page is displayed. |  |
| 12 | Search for the Service Contract | To find the service contract use the available filters, for example Service Contract:Choose Go. | The searched service contract is displayed in the result list. |  |
| 13 | Select Service Contract | Select the Service Contract for which a debit memo request was created. | The Service Contract Details screen is displayed. |  |
| 14 | Check Transaction History | Scroll to section Transaction History. | The Transaction ID for the debit memo request is displayed in the list. |  |

#### Create Debit Memo Request for Corrected and Actual Amount

Purpose

When the customer receives a debit for incorrect charges, a debit memo request has to be created. This process step shows you how to create a debit memo request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Debit Memo Requests (F1988). | The Manage Debit Memo Requests screen is displayed. |  |
| 3 | Navigate to Create Sales Document Screen | Choose Create Debit Memo Request. |  |  |
| 4 | Enter Sales Document Type | Make the following entries:Order Type: CBII Invoice Increase Req |  |  |
| 5 | Enter Order Details | Choose Create with reference. | The Create with Reference screen is displayed. |  |
| 6 | Choose the Reference Document | Enter the invoice number and choose Copy.Note If you are referencing a billing with related batch materials, after inputting the billing number, choose Item selection. Choose the item with open quantity and choose Copy. |  |  |
| 7 | Enter Order Reason | Choose the Sales tab. Enter an order reason (for example, 200 Price Difference: Price was too low). |  |  |
| 8 | Remove Billing Block | On the Sales tab, remove the default billing block by selecting Blank billing block. | Billing block removed from debit memo request. |  |
| 9 | Choose item | Select the second item, and choose Display Item Details. | The Create Debit Memo Request: Item Data screen displays. |  |
| 10 | Adjust the Amount for PPR0 | On the Conditions tab, adjust the amount for condition PSI1. |  |  |
| 11 | Adjust Tax Rate | On the Billing Document (F1901) tab, adjust the item tax classification in the Tax. classific. field, if required. |  |  |
| 12 | Save | Choose Save. | The Debit Memo Request is created.Note If Debit Memo request needs an approval then follow the steps mentioned in [Debit Memo Request Approval (Optional)](#unique_20) [page ] 24 otherwise proceed with the steps mentioned in [Create Debit Memo](#unique_22) [page ] 28. |  |
| 13 | Check Transaction History in Service Contract | Log on to the SAP Fiori launchpad using the role Customer Service Manager. | The Fiori Launchpad with access to the Manage Service Contracts application is displayed. |  |
| 14 | Open Manage Service Contracts application | Choose the Manage Service Contracts application tile. | The list report page is displayed. |  |
| 15 | Search for the Service Contract | To find the service contract use the available filters, for example Service Contract.Choose Go. | The searched service contract is displayed in the result list. |  |
| 16 | Select Service Contract | Select the Service Contract for which a debit memo request was created | The Service Contract Details screen is displayed. |  |
| 17 | Check Transaction History | Scroll to section Transaction History. | The Transaction ID for the debit memo request is displayed in the list. |  |

#### Debit Memo Request Approval (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the sales manager approves the Debit memo request.

Prerequisite

Approval status of the Debit Memo Request is In Approval.

For the automatic creation of a Debit Memo a billing creation job should be scheduled.

Follow the below steps to schedule a billing creation job for the automatic creation of a Debit Memo.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Billing Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Schedule Billing Creation app. | The Schedule Billing Creation screen displayed. |  |
| 3 | Create Job | Choose Create. | The New Job: Schedule Billing Creation screen displayed. |  |
| 4 | Select Template | Make the following entries:Job Template: Schedule Billing CreationJob Name: Schedule Billing Creation for Debit MemoChoose Step 2. |  |  |
| 5 | Maintain Schedule Options | Make the following entries:Choose Start ImmediatelyRecurrence Pattern: Single RunChoose Step 3. |  |  |
| 6 | Maintain Parameters | In Documents to be selected section in the Parameters step, make the following entries :Choose No Docs with Billing BlockChoose Order-Related |  |  |
| 7 | Execute Job | Choose Schedule. | The job is executed and Debit memo is created. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Sales Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Receive Notification | Open My Inbox - All Items.You can also choose the Notifications icon on the top right corner to navigate to the My Inbox screen. | The Inbox screen is dispalyed. |  |
| 3 | Refresh | Choose Refresh, if necessary. | Inbox is refreshed. |  |
| 4 | Approve | You receive the notification of the debit memo request. Choose one from the options on the bottom bar.Option 1 : ReleaseOption 2 : RejectOption 3 : Request Rework | The Submit Decision dialog box is displayed. |  |
| 5 | Submit | Enter some comments and choose Submit. | Based on above decisions, follow the next steps accordingly:Release: the whole process ends, no subsequent step is needed and the Debit Memo is created.Note Debit memo will be created automatically, if the Schedule Billing Creation job is scheduled.For manual creation of Debit Memo please proceed to [Create Debit Memo](#unique_22) [page ] 28.Reject: the whole process ends, no subsequent step is needed.Request Rework: go to [Rework Debit Memo Request](#unique_23) [page ] 26. |  |

##### Rework Debit Memo Request

|  |
| --- |
| Note Only relevant if the workflow is set as Request Rework by the sales manager previously. |

###### Check the Notifications

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, internal sales representative check the notifications.

Prerequisite

Approval status of the sales order is To be reworked.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Receive Notification | Open My Inbox - All Items (F0862).You can also choose the Notifications icon on the top right corner to navigate to the My Inbox screen. | The Inbox screen is displayed. |  |
| 3 | Refresh | Choose Refresh, if necessary. | Inbox is refreshed. |  |
| 4 | Check Inbox | Check the inbox items with relative Debit Memo Request. | Orders which need to be reworked are displayed.If rework is not required, the sales representative can set the status to Rework not Required in the inbox.If rework is required, follow the steps in [Change Debit Memo Request](#unique_25) [page ] 27. |  |

###### Change Debit Memo Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity the Internal Sales Representative changes the debit memo request.

Prerequisite

The approval status of the debit memo request is rework.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Internal Sales Representative. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Manage Billing Documents application | Choose the Manage Debit Memo Requests application tile. | The Debit Memo Request Overview screen is displayed. |  |
| 3 | Navigate to Manage Credit Memo document | In the field Debit Memo Request, enter the respective debit memo request document ID created in [Check the Notifications Debit](#unique_24) [page ] 26.Choose Go.Choose the row in the search result list containing the ID you are searching for to navigate to the debit memo request. |  |  |
| 4 | Change Debit Memo Request | On the Change Debit Memo Request Overview screen, make some changes, for example:Valid to: <Enter a date> | The approval status is changed to In Approval.Sales Manager will receive a task in their Inbox. Follow the steps in [Debit Memo Request Approval (Optional)](#unique_20) [page ] 24. |  |

#### Create Debit Memo

Purpose

This process step shows you how to generate a debit memo and debit the customer's account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Billing Clerk. | The SAP Fiori launchpad is displayed. |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen is displayed. |
| 3 | Define Billing Setting | Choose Billing Setting.You can make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing document after creation: ONChoose delivery items to be billed and select quantities: OFF |  |
| 4 | Search Billing Due Items | In the search condition, use criteria if necessary. | Sales document(s) displays in the result. |
| 5 | Select Billing Item(s) | Select row(s) of a sales document created previously, and choose Create Billing Documents. | The Billing Documents screen displays. |
| 6 | Maintain Billing Date | Choose billing type Debit Memo (L2) and maintain billing date, for example, <current date>, and then choose OK. | The new billing document is created. |
| 7 | Save Billing Document | On the Manage Billing Documents screen, choose Save.The draft version billing document turns into a saved billing document with ID xxxxxxxx.Make a note of the billing document number: __________. | The system generates an invoice for billing. |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions are prerequisites for this process.

| Process | Business Condition |
| --- | --- |
| 3D2 | Service Order Management |
| 3MO | Service Contract Management |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| J59 | Accounts Receivables |
| 3M3 | Event -Based Revenue Recognition - Service Documents |
| 3M4 | Event -Based Revenue Recognition - Service Documents- IFRS |
| 3M5 | Event -Based Revenue Recognition - Service Documents - US GAAP |

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
> Flagged while digesting this document, not verified: Debit memo request for corrected and actual amount, step 10 is titled 'Adjust the Amount for PPR0' but the instruction says to adjust the amount for condition PSI1; unclear which pricing condition type is intended.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/intercompany-billing-for-service-documents-53y-ae-test-script-1064]]
- related-to :: [[10-procurement/test-script-procurement-for-service-management-3ni-ae-964]]
- related-to :: [[14-maintenance-service-and-projects/test-script-service-order-management-and-monitoring-3d2-ae-927]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4GG_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 45,683 chars in the whole document
