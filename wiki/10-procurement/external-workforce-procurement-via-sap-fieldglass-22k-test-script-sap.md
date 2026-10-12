---
id: 10-procurement/external-workforce-procurement-via-sap-fieldglass-22k-test-script-sap
title: "External Workforce Procurement via SAP Fieldglass (22K) - Test Script, SAP S/4HANA Cloud Public Edition (22K_S4CLD2608_BPD_EN_XX)"
description: "Test script for scope item 22K: SAP Fieldglass to S/4HANA Cloud Public Edition integration for work orders, statements of work, time sheets, invoices, ERS; dated 19-06-26."
cluster: 10-procurement
tags: [kb/procurement, topic/service-procurement-fieldglass]
aliases: [22K_S4CLD2608_BPD_EN_XX]
keywords: [Service Procurement with SAP Fieldglass and Business Network, external workforce procurement, sap fieldglass integration, work order, job posting, statement of work, time sheets, service entry sheets, supplier invoices, evaluated receipt settlement]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/22K_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-800
topic: 10-procurement/service-procurement-fieldglass
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# External Workforce Procurement via SAP Fieldglass (22K) - Test Script, SAP S/4HANA Cloud Public Edition (22K_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/22K_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Service Procurement with SAP Fieldglass and Business Network** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | External Workforce Procurement via SAP Fieldglass (22K) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232852360)

[2 Prerequisites 5](#_Toc232852361)

[2.1 Additional Manual Configuration 5](#_Toc232852362)

[2.2 System Access 5](#_Toc232852363)

[2.3 Roles 5](#_Toc232852364)

[2.4 Master Data, Organizational Data, and Other Data 6](#_Toc232852365)

[2.5 Business Conditions 7](#_Toc232852366)

[2.6 Preliminary Steps 8](#_Toc232852367)

[2.6.1 Check Business Unit Availability 8](#_Toc232852368)

[2.6.2 Check Site Availability 9](#_Toc232852369)

[2.6.3 Check Cost Center Availability 10](#_Toc232852370)

[2.6.4 Check WBS Element Availability 11](#_Toc232852371)

[2.6.5 Invite Supplier 12](#_Toc232852372)

[2.6.6 Assign Cost Centers and General Ledger Accounts to Task Code 14](#_Toc232852373)

[2.6.7 Set Up Release Strategy for Purchase Requisition Approval 15](#_Toc232852374)

[2.6.8 Set Up Release Strategy for Purchase Order Approval 15](#_Toc232852375)

[2.6.9 Activate Flexible Workflow 16](#_Toc232852376)

[2.6.10 SAP Task Center (Optional) 16](#_Toc232852377)

[3 Overview Table 17](#_Toc232852378)

[4 Test Procedures 21](#_Toc232852379)

[4.1 Service Procurement for Work Order 21](#_Toc232852380)

[4.1.1 Create and Submit Job Posting 21](#_Toc232852381)

[4.1.2 Approve Job Posting 25](#_Toc232852382)

[4.1.3 Submit Job Seeker to Job Posting 25](#_Toc232852383)

[4.1.4 Hire Job Seeker 27](#_Toc232852384)

[4.1.5 Complete and Submit Work Order 28](#_Toc232852385)

[4.1.6 Approve Work Order 29](#_Toc232852386)

[4.1.7 Check Purchase Requisition in SAP S/4HANA Cloud Public Edition 30](#_Toc232852387)

[4.1.8 Check Updated Work Order Status 31](#_Toc232852388)

[4.1.9 Accept Work Order 32](#_Toc232852389)

[4.1.10 Check Purchase Order in SAP S/4HANA Cloud Public Edition 33](#_Toc232852390)

[4.1.11 Activate Work Order 33](#_Toc232852391)

[4.1.12 Register Worker 34](#_Toc232852392)

[4.1.13 Revise Work Order (Optional) 35](#_Toc232852393)

[4.1.14 Submit Time Sheet 38](#_Toc232852394)

[4.1.15 Check Generation of Service Entry Sheet in SAP S/4HANA Cloud Public Edition (Optional) 39](#_Toc232852395)

[4.1.16 Post Periodic Accruals in SAP S/4HANA Cloud Public Edition (Optional) 40](#_Toc232852396)

[4.1.17 Approve Time Sheet 40](#_Toc232852397)

[4.1.18 Reject Time Sheet (Optional) 41](#_Toc232852398)

[4.1.19 Check Approval Status of Service Entry Sheet in SAP S/4HANA Cloud Public Edition 42](#_Toc232852399)

[4.1.20 Approve Invoice 43](#_Toc232852400)

[4.1.21 Check Invoice in SAP S/4HANA Cloud Public Edition 44](#_Toc232852401)

[4.1.22 Revise Time Sheet (Optional) 45](#_Toc232852402)

[4.1.23 Pay the Invoice in SAP S/4HANA Cloud Public Edition 47](#_Toc232852403)

[4.1.24 Check Updated Invoice Status 49](#_Toc232852404)

[4.1.25 Close Work Order 50](#_Toc232852405)

[4.2 Service Procurement for Statement of Work (SOW) 51](#_Toc232852406)

[4.2.1 Manage Supplier Classification 52](#_Toc232852407)

[4.2.2 Associate Classification to Supplier 52](#_Toc232852408)

[4.2.3 Associate Business Units to SOW Template 53](#_Toc232852409)

[4.2.4 Associate Classification to SOW Template 54](#_Toc232852410)

[4.2.5 Create Statement of Work 55](#_Toc232852411)

[4.2.6 Approve Statement of Work 57](#_Toc232852412)

[4.2.7 Check Purchase Requisition in SAP S/4HANA Cloud Public Edition 58](#_Toc232852413)

[4.2.8 Check Updated Statement of Work Status 59](#_Toc232852414)

[4.2.9 Accept Statement of Work 60](#_Toc232852415)

[4.2.10 Check Purchase Order in SAP S/4HANA Cloud Public Edition 61](#_Toc232852416)

[4.2.11 Revise Statement of Work (Optional) 62](#_Toc232852417)

[4.2.12 Mark Work Item as Complete 64](#_Toc232852418)

[4.2.13 Check Generation of Service Entry Sheet in SAP S/4HANA Cloud Public Edition (Optional) 65](#_Toc232852419)

[4.2.14 Post Periodic Accruals in SAP S/4HANA Cloud Public Edition (Optional) 66](#_Toc232852420)

[4.2.15 Approve Transaction 67](#_Toc232852421)

[4.2.16 Reject Transaction (Optional) 67](#_Toc232852422)

[4.2.17 Check Approval Status of Service Entry Sheet in SAP S/4HANA Cloud Public Edition 68](#_Toc232852423)

[4.2.18 Approve SOW Invoice 69](#_Toc232852424)

[4.2.19 Check Invoice in SAP S/4HANA Cloud Public Edition 70](#_Toc232852425)

[4.2.20 Pay the Invoice in SAP S/4HANA Cloud Public Edition 71](#_Toc232852426)

[4.2.21 Check Updated Invoice Status 73](#_Toc232852427)

[4.2.22 Close Statement of Work 74](#_Toc232852428)

[4.3 Evaluated Receipt Settlement (ERS) Invoice 76](#_Toc232852429)

[4.3.1 Check Required Settings for ERS Supplier Invoice in SAP S/4HANA Cloud Public Edition 76](#_Toc232852430)

[4.3.2 Create and Approve Service Entry Sheet in SAP S/4HANA Cloud Public Edition 77](#_Toc232852431)

[4.3.3 Create and Run ERS Supplier Invoice Job in SAP S/4HANA Cloud Public Edition (Optional) 77](#_Toc232852432)

[4.3.4 Check ERS Supplier Invoice in SAP S/4HANA Cloud Public Edition 79](#_Toc232852433)

[4.3.5 Check ERS Supplier Invoice in SAP Fieldglass 79](#_Toc232852434)

## Purpose

Overview

Integrate SAP Fieldglass with SAP S/4HANA Cloud Public Edition through SAP Cloud Integration and SAP Master Data Integration service to support, automate, and extend the processes for hiring external workers and managing statements of work.

This integration benefits you when you digitize the processing of job postings and proofs of employment. After hiring an external resource, a work order is created in SAP Fieldglass. In SAP S/4HANA Cloud Public Edition, a purchase requisition and a purchase order are automatically created. When the project manager approves the external worker's submitted time, a service entry sheet is created in SAP S/4HANA Cloud Public Edition. Finally, a supplier invoice is generated in SAP Fieldglass based on the purchase order and the service entry sheet. Once the supplier accepts this invoice, it's posted to SAP S/4HANA Cloud Public Edition for the accounts payable accountant to process.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/74e84460c2ab08f9e1959d58334339be)

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP Fieldglass | Access on [https://www.fieldglass.net/](https://www.fieldglass.net/). Your system administrator provides you with logon data. |

### Roles

Assign the following business roles to your individual test users in SAP S/4HANA Cloud Public Edition:

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC | Test user: useridPassword: password |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC | Test user: useridPassword: password |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC | Test user: useridPassword: password |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC | Test user: useridPassword: password |

Use the following standard test users to run test procedures in SAP Fieldglass:

| Name | Description | Log On |
| --- | --- | --- |
| Buyer/Administrator | This user has administrator rights, can create job postings, view job seekers, and hire job sseekers to create work orders. | Test user: useridPassword: password |
| Supplier | This user can manage the sites they can service, and view job postings. This user is responsible for submitting job seekers, and can accept work orders. | Test user: useridPassword: password |
| Approver | This user is authorized to be notified when SAP Fieldglass work items are created, and approve these submitted items. | Test user: useridPassword: password |
| Program Office (PMO) | This user can manage onboarding task, for example, background checks, and activate worker. | Test user: useridPassword: password |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company is created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data to go through the test procedure.

| SAP Fieldglass Object | SAP S/4HANA Cloud Public Edition Object | Code | Name |
| --- | --- | --- | --- |
| Legal Entity | Company Code | 1010 | 1010 |
| Business Unit | Purchasing Organization | 1010 | Purch.Org. 1010 |
| Site | Plant | 1010 | Plant 1 DE |
| Cost Center | Cost Center | 10101101 (SAP S/4HANA Cloud Public Edition) | Financials (DE) |
|  |  | A0000010101101 (SAP Fieldglass) |  |
|  | WBS Element | PFCProject1 |  |
|  |  | PFCProject11 |  |
| Supplier | Vendor | 10300080 | DE Supplier for Fieldglass |
| General Ledger Account | General Ledger Account | 65100000 | Purchased Services |
| Task Code |  |  | TC |
| Invoice Adjustment |  |  | V0 |
|  | Purchasing Group | 001 | Group 001 |
|  | Material Group | YBMM00 | Non-sto Mat. w/o ID |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 22Z - Procurement of Services | You’ve completed the preliminary steps as described in chapter Configure Flexible Workflow for Service Entry Sheets and Configure Flexible Workflow for Supplier Invoice. |
| 18J - Requisitioning | You’ve completed the preliminary steps as described in chapter Configure Flexible Workflow for Purchase Requisition and Configure Flexible Workflow for Purchase Order. |
| 63L - Service Entry Sheet Based Accruals | If you want to use post periodic accruals, you need to complete the preliminary steps as described in the test script of [Service Entry Sheet Based Accruals (63L)](https://me.sap.com/processnavigator/SolP/63L). |
|  | If you want to replicate workforce person data and work assignment data from HR source systems to SAP S/4HANA Cloud Public Edition using the SAP Master Data Integration service, refer to [Inbound Replication](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/d9e300b90f024162b8f267373435cf5c.html). |

### Preliminary Steps

#### Check Business Unit Availability

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you check whether the business unit from previous master data table is available in stock in the SAP Fieldglass system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as an Buyer/Administrator. | The Home screen is displayed. |  |
| 2 | Access Admin Screen | Choose Maintain, and access the Admin screen. | The Admin screen is displayed. |  |
| 3 | Access Business Unit Screen | In the Company Structure section, choose Business Unit, and navigate to the Business Units screen. |  |  |
| 4 | Search Business Unit | Enter the company code, for example, 1010 (DE) of the business unit from the previous master data table, and choose Filter to find this business unit. | The item 1010 (DE) is displayed.Note If you’ve completed the master data replication, this business unit should be available in SAP Fieldglass. If you haven’t completed the master data replication, follow the Configuration Guide to replicate this business unit from the SAP S/4HANA Cloud Public Edition system to the SAP Fieldglass system. |  |

#### Check Site Availability

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you check whether the site from previous master data table is available in stock in the SAP Fieldglass system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as an Buyer/Administrator. | The Home screen is displayed. |  |
| 2 | Access Admin Screen | Choose Maintain, and access the Admin screen. | The Admin screen is displayed. |  |
| 3 | Access Site Screen | In the Company Structure section, choose Site, and go to the Sites screen. |  |  |
| 4 | Search Site | Enter the company code, for example, 1010 (DE) of the site from the previous master data table, and choose Filter to find this site. | The item 1010 (DE) is displayed.Note If you’ve completed the master data replication, this site should be available in SAP Fieldglass. If you haven’t completed the master data replication, follow the Configuration Guide to replicate this site from the SAP S/4HANA Cloud Public Edition system to the SAP Fieldglass system. |  |

#### Check Cost Center Availability

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you check whether the cost center from previous master data table is available in stock in the SAP Fieldglass system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass System as an Buyer/Administrator. | The Home screen is displayed. |  |
| 2 | Access Admin Screen | Choose Maintain, and access the Admin screen. | The Admin screen is displayed. |  |
| 3 | Access Cost Center Screen | In the Company Structure section, choose Cost Center, and go to the Cost Center screen. |  |  |
| 4 | Search Cost Center | Enter the code, for example, 10101101 of the cost center from the previous master data table, and choose Filter to find this cost center. | The item 10101101 (DE) is displayed.Note If you’ve completed the master data replication, this cost center should be available in SAP Fieldglass. If you haven’t completed the master data replication, follow the Configuration Guide to replicate this cost center from the SAP S/4HANA Cloud Public Edition system to the SAP Fieldglass system. |  |

#### Check WBS Element Availability

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you check whether the WBS element from previous master data table is available in stock in the SAP Fieldglass system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass System as an Buyer/Administrator. | The Home screen is displayed. |  |
| 2 | Access Admin Screen | Choose Maintain, and access the Admin screen. | The Admin screen is displayed. |  |
| 3 | Access WBS Element Screen | In the Company Structure section, choose Cost Center, and go to the Cost Centers screen. |  |  |
| 4 | Search WBS Element | Enter the code PFCProject1 of the WBS element from the previous master data table, and choose Filter to find this WBS element. | The item PFCProject1 is displayed.Note If you’ve completed the master data replication, this WBS element should be available in SAP Fieldglass. If you haven’t completed the master data replication, follow the Configuration Guide to replicate this WBS element from the SAP S/4HANA Cloud Public Edition system to the SAP Fieldglass system. |  |

#### Invite Supplier

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this procedure, you create a supplier account for the business partner replicated from the SAP Fieldglass system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as an Buyer/Administrator. | The Home screen is displayed. |  |
| 2 | Access Admin Screen | Choose Maintain, and access the Admin screen. | The Admin screen is displayed. |  |
| 3 | Access Vendor Master Screen | In the Supplier section, choose Vendor Master, and go to the Vendor Masters screen. |  |  |
| 4 | Search Vendor Master | Enter the code of supplier from the previous master data table, and choose Filter to find this supplier.Supplier Name: 10300090 | The item 10300090 is displayed.Note If you’ve completed the master data replication, this vendor master should be available in SAP Fieldglass. If you haven’t completed the master data replication, follow the Configuration Guide to replicate this vendor master from the SAP S/4HANA Cloud Public Edition system to the SAP Fieldglass system. |  |
| 5 | Invite Supplier | On the Details screen, choose Invite.In the Invite To Apply dialog box, choose the invited. | An invitation email is sent to the contact person.In case the email address isn’t maintained, choose the action Resend Invitation, and enter your email address in the field Supplier Email. |  |
| 6 | Check Invitation Email | Check your email inbox for the item Invitation to join the SAP Fieldglass system.Navigate to the registration screen by selecting the link Click here within the invitation email. | The Welcome to SAP Fieldglass screen opens. |  |
| 7 | Create Account | On the Welcome to SAP Fieldglass screen, below the question Do you have an existing SAP Fieldglass account that you would like to link to SAP Test?, choose No > Continue. | The Create a New SAP Fieldglass Account screen is displayed. |  |
| 8 | Complete Registration Details | In the Company Address field and Company Preferences field, enter the following data:Country: Germany(DEU)Time Zone: Europe/BerlinIn the Security Details field, enter the mandatory data.Choose Next. | The Contractor Access Agreement screen is displayed. |  |
| 9 | Accept and Continue | On the Contractor Access Agreement screen, review the Contractor Access Agreement (CAA), indicate that you have read and understood the agreement, and sign the declaration.Choose Accept and Continue. | The Home screen of the registered supplier is displayed. |  |

#### Assign Cost Centers and General Ledger Accounts to Task Code

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to assign cost centers and general ledger accounts to a task code.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as an Buyer/Administrator. | The Home screen is displayed. |  |
| 2 | Access Admin Screen | Choose Maintain, and access the Admin screen. | The Admin screen is displayed. |  |
| 3 | Access Task Code Screen | In the Financial Data section, choose Task Code, and go to the Task Codes screen. |  |  |
| 4 | Create Task Code | To add a new task code, choose New, and enter the following data:Code: TC_testName: TC_testSystem ID: <System ID>Click Add.Navigate back to the Task Code screen. |  |  |
| 5 | Associate Cost Center to Task Code | To associate cost centers to the task code, on the Task Code screen, choose Cost Centers > Add . | The Associate Cost Centers to Task Code dialog box is displayed. |  |
| 6 | Select Cost Center for Task Code | In the Associate Cost Centers to Task Code dialog box, select cost center A0000010101101.Choose Add.Navigate back to the Task Code screen. |  |  |
| 7 | Associate General Ledger Accounts to Task Code | To associate general ledger accounts to the task code, on the Task Code screen, choose General Ledger Accounts > Add . | The Associate General Ledger Account to Task Code dialog box is displayed. |  |
| 8 | Select General Ledger Accounts for Task Code | In the Associate General Ledger Account to Task Code dialog box, select general ledger account 65100000.Choose Add. |  |  |

#### Set Up Release Strategy for Purchase Requisition Approval

Make sure to activate the default workflow Automatic Approval for Purchase Requisition Item in the Manage Workflows for Purchase Requisitions (F2705A) app.

For more information about Configuration steps to set up Release Strategy and to use Manage Workflows for Purchase Requisition app using Fiori in S/4HANA, refer to SAP Note[2331693](https://me.sap.com/notes/2331693).

#### Set Up Release Strategy for Purchase Order Approval

Make sure to activate the default workflow Automatic Approval for Purchase Order Item in the Manage Workflows for Purchase Orders (F2872) app.

For more information, refer to scope item [Procurement of Services (22Z)](https://me.sap.com/processnavigator/SolP/22Z).

#### Activate Flexible Workflow

To activate the flexible workflow, complete the following:

- Activate the default workflow Automatic Approval for Purchase Requisition Items in the Manage Workflows for Purchase Requisitions (F2705A) app.

For more information, refer to scope item [Requisitioning (18J)](https://me.sap.com/processnavigator/SolP/18J)

- Activate the default workflow Automatic Approval for Purchase Orders in the Manage Workflows for Purchase Orders (F2872) app.

For more information, refer to scope item [Requisitioning (18J)](https://me.sap.com/processnavigator/SolP/18J)

- Activate the default workflow Automatic Approval for Service Entry Sheets in the Manage Workflows for Service Entry Sheets (F3173) app.

For more information, refer to scope item [Procurement of Services (22Z)](https://me.sap.com/processnavigator/SolP/22Z)

- Activate the default workflow Automatic Approval for Supplier Invoices in the Manage Workflows for Supplier Invoices (F2873) app.

For more information, refer to scope item [Procurement of Services (22Z)](https://me.sap.com/processnavigator/SolP/22Z)

#### SAP Task Center (Optional)

The approval workflow tasks in SAP S/4HANA Cloud Public Edition are optional, but can be set to automatic, because SAP Fieldglass is the main system of engagement for users.

For more information about the workflow setup, see scope item [Procurement of Services (22Z)](https://me.sap.com/processnavigator/SolP/J11https:/me.sap.com/processnavigator/SolP/22Z), and SAP Note [2331693](https://me.sap.com/notes/2331693).

The SAP Fieldglass approval workflow tasks can be accessed through SAP Task Center as well. SAP Task Center is an SAP Business Technology Platform (SAP BTP) service that provides a single entry point for business users to access all of their assigned workflow items, to-do lists, and approvals across SAP solutions for cloud and on-premise. For more information, see [What Is SAP Task Center?](https://help.sap.com/viewer/08cbda59b4954e93abb2ec85f1db399d/LATEST/en-US/9693186f1fe54cbe801085d6bdfe8287.html) on SAP Help Portal.

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

The scope of the section Service Procurement for Work Order consists of several process steps provided in the following table.

| Process Step | Business Role | Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create and Submit Job Posting](#unique_19) [page ] 21 | Buyer/Administrator in SAP Fieldglass |  | The job posting is created and submitted and routed to the status Pending Approval. |
| [Approve Job Posting](#unique_20) [page ] 25 | Approver in SAP Fieldglass |  | The job posting is approved and routed to the status Pending Distribution. |
| [Submit Job Seeker to Job Posting](#unique_21) [page ] 25 | Supplier in SAP Fieldglass |  | A job seeker is submitted by the supplier and the job posting is routed to the next step. |
| [Hire Job Seeker](#unique_22) [page ] 27 | Buyer/Administrator in SAP Fieldglass |  | The job seeker, who was shortlisted by the Program Office (PMO) User, is hired and a work order is created. |
| [Complete and Submit Work Order](#unique_23) [page ] 28 | Buyer/Administrator in SAP Fieldglass |  | The work order is completed, submitted, and routed to the status Pending Approval. |
| [Approve Work Order](#unique_24) [page ] 29 | Approver in SAP Fieldglass |  | The work order is approved and needs to be accepted by the supplier. |
| [Check Purchase Requisition in SAP S/4HANA Cloud Public Edition](#unique_25) [page ] 30 | Purchaser | Manage Purchase Requisitions (F2229) | The purchase requisition is generated, and approved. |
| [Check Updated Work Order Status](#unique_26) [page ] 31 | Buyer/Administrator in SAP Fieldglass |  | The status of the work order is Created. |
| [Accept Work Order](#unique_27) [page ] 32 | Supplier in SAP Fieldglass |  | The work order is accepted by the supplier, and needs to be activated by the Program Office (PMO) user, who would receive a work item to respond to. |
| [Check Purchase Order in SAP S/4HANA Cloud Public Edition](#unique_28) [page ] 33 | Purchaser | Manage Purchase Orders (Version 2) (F0842A) | The purchase order is generated, and approved. |
| [Activate Work Order](#unique_29) [page ] 33 | Program Office (PMO) User in SAP Fieldglass |  | The work order is activated and a registration email would be sent to worker’s email address. |
| [Register Worker](#unique_30) [page ] 34 | Worker in SAP Fieldglass |  | A worker is registered in the SAP Fieldglass system. |
| [Submit Time Sheet](#unique_31) [page ] 38 | Worker in SAP Fieldglass |  | The time sheet is submitted by worker and routed to the step Pending Approval. |
| [Check Generation of Service Entry Sheet in SAP S/4HANA Cloud Public Edition (Optional)](#unique_32) [page ] 39 | Purchaser | Manage Service Entry Sheets (F2027) | The service entry sheet was generated, and is in status In External Approval. |
| [Post Periodic Accruals in SAP S/4HANA Cloud Public Edition (Optional)](#unique_33) [page ] 40 | General Ledger Accountant | Schedule Accruals Jobs (F3778) | The job to automatically post the accrued purchase orders is created and started immediately. |
| [Approve Time Sheet](#unique_34) [page ] 40 | Buyer/Administrator in SAP Fieldglass |  | The time sheet is approved and an invoice is automatically generated, waiting to be approved. |
| [Reject Time Sheet (Optional)](#unique_35) [page ] 41 | Supplier in SAP Fieldglass |  | The time sheet is rejected. |
| [Check Approval Status of Service Entry Sheet in SAP S/4HANA Cloud Public Edition](#unique_36) [page ] 42 | Purchaser | Manage Service Entry Sheets (F2027) | The service entry sheet was generated, and is in status Approved or Rejected. |
| [Approve Invoice](#unique_37) [page ] 43 | Approver in SAP Fieldglass |  | The invoice is approved. |
| [Check Invoice in SAP S/4HANA Cloud Public Edition](#unique_38) [page ] 44 | Accounts Payable Accountant | Supplier Invoices List (Version 2) (F1060A) | The invoice is generated. |
| [Revise Time Sheet (Optional)](#unique_39) [page ] 45 | Worker in SAP Fieldglass |  | The time sheet is revised in SAP Fieldglass. |
|  | Purchaser | Manage Service Entry Sheets - Lean Services (F2027) | The changes are reflected in SAP S/4HANA Cloud Public Edition and can be reviewed. |
|  | Accounts Payable Accountant | Supplier Invoices List (F1060A) | The changes are reflected in SAP S/4HANA Cloud Public Edition and can be reviewed. |
| [Pay the Invoice in SAP S/4HANA Cloud Public Edition](#unique_40) [page ] 47 | Accounts Payable Accountant | Post Outgoing Payments (F1612) | The payment for the invoice transferred from SAP Fieldglass to SAP S/4HANA Cloud Public Edition is posted. |
| [Check Updated Invoice Status](#unique_41) [page ] 49 | Buyer/Administrator in SAP Fieldglass |  | The status of the invoice in SAP Fieldglass is changed to Paid. |
| [Close Work Order](#unique_42) [page ] 50 | Buyer/Administrator in SAP Fieldglass |  | The work order is closed in SAP Fieldglass. |
|  | Purchaser | Manage Purchase Orders (F0842A) | The changes are reflected in SAP S/4HANA Cloud Public Edition and can be reviewed. |

The scope of the section Service Procure for Statement of Work consists of several steps provided in the following table.

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Manage Supplier Classification](#unique_43) [page ] 52 | Buyer/Administrator in SAP Fieldglass |  | A supplier classification is created. |
| [Associate Classification to Supplier](#unique_44) [page ] 52 | Buyer/Administrator in SAP Fieldglass |  | The newly added classification is associated to a supplier. |
| [Associate Business Units to SOW Template](#unique_45) [page ] 53 | Buyer/Administrator in SAP Fieldglass |  | The desired business unit is associated to the SOW template to be used. |
| [Associate Classification to SOW Template](#unique_46) [page ] 54 | Buyer/Administrator in SAP Fieldglass |  | The newly added classification is associated to the SOW template to be used. |
| [Create Statement of Work](#unique_47) [page ] 55 | Buyer/Administrator in SAP Fieldglass |  | A statement of work is created. |
| [Approve Statement of Work](#unique_48) [page ] 57 | Approver in SAP Fieldglass |  | The statement of work is approved, and routed to the step Pending Response. |
| [Check Purchase Requisition in SAP S/4HANA Cloud Public Edition](#unique_49) [page ] 58 | Purchaser | Manage Purchase Requisitions (F2229) | The purchase requisition is generated, and approved. |
| [Check Updated Statement of Work Status](#unique_50) [page ] 59 | Buyer/Administrator in SAP Fieldglass |  | The status of the statement of work is Pending Response. |
| [Accept Statement of Work](#unique_51) [page ] 60 | Supplier in SAP Fieldglass |  | The statement of work is accepted by the supplier. |
| [Check Purchase Order in SAP S/4HANA Cloud Public Edition](#unique_52) [page ] 61 | Purchaser | Manage Purchase Orders (Version 2) (F0842A) | The purchase order is generated, and approved. |
| [Mark Work Item as Complete](#unique_53) [page ] 64 | Supplier in SAP Fieldglass |  | The work item is marked as complete, and needs to be approved by Buyer/Administrator. |
| [Check Generation of Service Entry Sheet in SAP S/4HANA Cloud Public Edition (Optional)](#unique_54) [page ] 65 | Purchaser | Manage Service Entry Sheets (F2027) | The service entry sheet was generated, and is in status In External Approval. |
| [Post Periodic Accruals in SAP S/4HANA Cloud Public Edition (Optional)](#unique_55) [page ] 66 | General Ledger Accountant | Schedule Accruals Jobs (F3778) | The job to automatically post the accrued purchase orders is created and started immediately. |
| [Approve Transaction](#unique_56) [page ] 67 | Buyer/Administrator in SAP Fieldglass |  | The completed transaction is approved, and is available to be invoiced. |
| [Check Approval Status of Service Entry Sheet in SAP S/4HANA Cloud Public Edition](#unique_57) [page ] 68 | Purchaser | Manage Service Entry Sheets (F2027) | The service entry sheet was generated, and is in status Approved or Rejected. |
| [Approve SOW Invoice](#unique_58) [page ] 69 | Approver in SAP Fieldglass |  | The invoice is approved. |
| [Check Invoice in SAP S/4HANA Cloud Public Edition](#unique_59) [page ] 70 | Accounts Payable Accountant | Supplier Invoices List (Version 2) (F1060A) | The invoice is generated. |
| [Pay the Invoice in SAP S/4HANA Cloud Public Edition](#unique_60) [page ] 71 | Accounts Payable Accountant | Post Outgoing Payments (F1612) | The payment for the invoice transferred from SAP Fieldglass to SAP S/4HANA Cloud Public Edition is posted. |
| [Check Updated Invoice Status](#unique_61) [page ] 73 | Buyer/Administrator in SAP Fieldglass |  | The status of the invoice in SAP Fieldglass is changed to Paid. |
| [Close Statement of Work](#unique_62) [page ] 74 | Buyer/Administrator in SAP Fieldglass |  | The statement of work is closed in SAP Fieldglass. |
|  | Purchaser | Manage Purchase Orders (F0842A) | The changes are reflected in SAP S/4HANA Cloud Public Edition and can be reviewed. |

The scope of the section Evaluated Receipt Settlement (ERS) Invoice consists of several steps provided in the following table.

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Check Required Settings for ERS Supplier Invoice in SAP S/4HANA Cloud Public Edition](#unique_63) [page ] 76 | Accounts Payable Accountant | Maintain Business Partner (BP) | Check in SAP S/4HANA Cloud Public Edition if the required settings GR-Based Invoice Verif. and Eval. Receipt Settlement are activated for the ERS supplier. |
| [Create and Run ERS Supplier Invoice Job in SAP S/4HANA Cloud Public Edition (Optional)](#unique_64) [page ] 77 | Accounts Payable Accountant | Schedule Supplier Invoice Jobs (F1683) | Create an ERS supplier invoice job and run it immediately in SAP S/4HANA Cloud Public Edition. |
| [Check ERS Supplier Invoice in SAP S/4HANA Cloud Public Edition](#unique_65) [page ] 79 | Accounts Payable Accountant | Supplier Invoices List (F1060A) | Check the ERS supplier invoice in SAP S/4HANA Cloud Public Edition. |
| [Check ERS Supplier Invoice in SAP Fieldglass](#unique_66) [page ] 79 | Buyer/Administrator in SAP Fieldglass |  | Check in SAP Fieldglass whether the invoice is automatically generated. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

|  |
| --- |
| Note In SAP Fieldglass, the vertical navigation and graphical view are expanded by default.The vertical navigation bar now displays expanded by default. Use the menu icon (hamburger icon) at the top of the navigation bar to collapse the bar, if desired. The setting you choose is sticky and will remain until you change it.For more information, refer to [What's New in SAP Fieldglass](https://help.sap.com/whats-new/0c2fc99f5fd34e8e8662fbdff4cbbb0d). |

### Service Procurement for Work Order

This section describes test procedures for each process step that belongs to the case Service Procurement for Work Order.

#### Create and Submit Job Posting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to create a job posting by selecting a well-defined job posting template.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as a Buyer. | The Home screen is displayed. |  |
| 2 | Access Job Posting Creation | In the Contingent Labor section, choose Create Job Posting. | In the Create Job Posting screen is displayed. |  |
| 3 | Select a Job Posting Owner | Select the correct job posting owner.Note The job posting may be routed for approval based on the owner selected. |  |  |
| 4 | Search for Job Posting Template | Search for a specific template or an existing job posting. Enter or select the desired information in the search fields, and choose Filter to narrow the list.Enter the following data:Billing Currency: (for example) EURSource: Job Posting Templates | A list of possible templates is displayed. |  |
| 5 | Select Job Posting Template | Choose the Title of the desired template.Title: Billing Analyst | The Setup screen is displayed. |  |
| 6 | Enter Start Date and End Date | Enter Start Date and End Date for the job posting (for example July 1st 2016 – September 30th 2016). |  |  |
| 7 | Enter Number of Positions | Enter the Number of Positions as 1. |  |  |
| 8 | Select Travel Requirement | In the Is travel required for position? field, select the value No. |  |  |
| 9 | Select Legal Entity, Site, and Business | Select the desired Legal Entity, Site, and Business Unit. Enter the following data:Legal Entity: (for example) Company Code 1010 (DE)Site(Plant): (for example) Plant 1 (DE)Business Unit (Purch. Org.): (for example) Purch.Org.1010 (DE)Note Locations are associated with specific sites. The correct value is automatically displayed in the Location field. There’s no need to change it. |  |  |
| 10 | Select Cost Center and General Ledger Account | Select Cost Center and General Ledger Account from the dropdown list.Cost Center: (for example) A0000010101101 Financials (DE)General Ledger Account: (for example) 65100000Note If the expected cost center isn’t on the list, choose the Add or remove Cost Centers link. Check the option Unused, select the desired cost center, and choose Add Selected. To return to the setup screen, choose Update. |  |  |
| 11 | Continue Job Posting Creation | Choose Continue.Note If Continue doesn’t exist, choose Submit, and go to the Job Posting Details screen. To recontinue the job posting creation, choose Edit. | The Augment screen is displayed. |  |
| 12 | Enter Posting Information (Optional) | If desired, enter Posting Information.Note The Buyer reference field is optional. You can enter information, such as an internal reference number, that can then be used to search for this job posting.Based on company configuration, you may be required to enter a Coordinator. The coordinator is typically a member of the program office, who is responsible for assisting with this job posting. |  |  |
| 13 | Enter Qualifications | Skip this field, and leave it as No Qualifications specified.Note To enter or update desired qualifications, use the Add or remove Qualifications link. Suppliers rate the job seekers on the listed qualifications. |  |  |
| 14 | Enter Time and Expense Sheet Settings | Enter or update Time Sheet; Expense Sheet Settings. Depending on the job posting template configuration, default values are displayed. There’s no need to change it.Time Sheet Type: StandardHours per Day: 8Hours per Week: 40 |  |  |
| 15 | Enter Accounting Information | Enter or update Accounting information as required. Depending on the job posting template configuration, default values are displayed. There’s no need to change it. |  |  |
| 16 | Enter Distribution Information | Select the correct Distributor from the dropdown list.Note Based on the job posting template configuration, the Distribution list is automatically assigned.The Maximum Submissions per Supplier field is optional.The Supplier Respond By Date field is also optional. If populated, it triggers a notification to the job posting owner, that the supplier should have responded by this date. |  |  |
| 17 | Add Attachments | Skip this field, leave it as No Attachments Defined.Note If desired, use the Add Attachments link, to add an attachment such as job description to the job posting. |  |  |
| 18 | Enter Rules | Enter or update the Rules. Depending on the company configuration and job posting template, default values are displayed.In the Job Seeker Rate/Salary can exceed Requested Rate/Salary field, select No.Note For both job posting and work order, the bill rate and salary can always be lowered but can only be increased, if the rule Job Seeker Rate / Salary can exceed Requested Rate / Salary is selected.If you select No, the supplier wouldn’t be able to submit a job seeker with a bill rate or salary exceeding the requested bill rate or salary.Choose Continue. | The Review and Submit screen is displayed. |  |
| 19 | Submit Job Posting | On the Review and Submit screen, review the details, and apply changes if necessary.Note To save the job posting as a draft, choose Complete Later. You can return to it later for review, completion, and submittal.When all data has been reviewed, choose Submit. | The job posting is saved, submitted, and routed to the next step Pending Approval in the workflow.Note The job posting is assigned a unique ID, which is displayed at the top of the screen, above the title. |  |

#### Approve Job Posting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to review the job posting for accuracy, make edits if necessary, and approve the job posting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as Approver. | Job postings that require review and approval appear in your My Work Items menu. |  |
| 2 | Access Work Item | From the My Work Items menu, select Approve in the Job Posting section. |  |  |
| 3 | Approve Job Posting | Choose the ID of the posting you created, and select Approve.Tip You can also access the job postings by selecting Job Posting from the View menu. | The job posting is submitted, and routed to the next step Pending Distribution in the workflow. |  |

#### Submit Job Seeker to Job Posting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to submit a job seeker to a job posting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as a Supplier. |  |  |
| 2 | Access and Review Job Posting | From the My Work Items menu, select Respond in the Job Posting section.Choose the ID of the job posting desired. |  |  |
| 3 | Submit New Job Seeker | Choose Submit Job Seeker. | The Setup screen is displayed. |  |
| 4 | Complete Required Details | Enter the mandatory data in the Details field, including First Name, Last Name, Security ID, and Available Date.To attach a Resume or a CV, choose Attach.Note Depending on your Fieldglass configuration, the Security ID element can, for example, match the format FFMMDDZZZZ, which means: FF/First two letters of worker's name, MM/Month (of birthday – The value can be made up.), DD/Day (of birth – The value can be made up.), ZZZZ/Year (of birth – The value can be made up.).Choose Continue. | The Rates screen is displayed. |  |
| 5 | Enter Rate | Enter a Pay Rate (for example: 20), and if desired, a Markup.To view the Final Bill Rate, choose Calculate.Choose Continue. | The Review and Submit screen is displayed. |  |
| 6 | Submit Job Seeker To Job Posting | On the Review and Submit screen, review the details, and apply changes, if necessary.Note To save the submission of the job seeker to the job posting as a draft, choose Complete Later. You can return to it at a later time for review, completion, and submittal.When all data has been reviewed, choose Submit. | The job posting is routed to the next step Requestor reviews Job Seekers in the workflow.Tip To view the job seeker submitted, choose the Job Seekers tab. |  |

#### Hire Job Seeker

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to hire a job seeker shortlisted by Program Office (PMO).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as Buyer/Administrator. |  |  |
| 2 | Access Job Posting | In the Contingent Labor section, select Job Posting.Choose the ID of the job posting desired. | The job posting screen is displayed. |  |
| 3 | View Job Seekers | To view the job seekers submitted to the job posting, choose the Job Seekers tab. |  |  |
| 4 | Hire Job Seeker | Select the checkbox of a job seeker, and choose Hire. | The Create Work Order screen is displayed and lists the terms requested on the original job posting. |  |

#### Complete and Submit Work Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to complete and submit a work order to finalize the terms of the position.

Prerequisites

To complete and submit a work order, you need to hire a job seeker first. For more information, see [Hire Job Seeker](#unique_22) [page ] 27.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Complete Work Order | On the Create Work Order screen, review the data and enter any additional data according to your business requirements:Goods Receipt Is Expected: YesInvoice Is Goods Receipt Based: YesItem Category: ENote If you've selected multiple cost centers for the newly created job posting in chapter [Create and Submit Job Posting](#unique_19) [page ] 21, the value of Item Category is N/A.Material Group: YBMM00Product type: 2Purchase Group: 001Choose Continue.Note If the warning message Job Seeker is a Possible Match to one or more Master Worker Records is displayed, select Create new Master Worker Record, and choose Continue. | The Review and Submit screen is displayed. |  |
| 2 | Submit Work Order | On the Review and Submit screen, review the details, and apply changes if necessary.Note To save the submission of the job seeker to the job posting as a draft, choose Complete Later. You can return to it at a later time for review, completion, and submittal.When all data has been reviewed, choose Submit. | The job posting is routed to the next step Pending Approval in the workflow.Note The work order is assigned a unique ID, which is displayed at the top of the screen, above the title. |  |

#### Approve Work Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to approve the work order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as Approver. | Work Orders that require review and approval appear in your Work Items menu. |  |
| 2 | Access Work Item | From the My Work Items menu, select Approve in the Work Order section. |  |  |
| 3 | Approve Work Order | Choose the ID of the work order you submitted, and select Approve.Tip You can also access the work orders by selecting Work Order from the View menu. | The work order is approved, and routed to the next step Accept in the workflow, waiting for the supplier to accept the work order. |  |

#### Check Purchase Requisition in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to check whether the purchase requisition is generated and approved automatically in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad displayed. |  |
| 2 | Access App | Open the Manage Purchase Requisitions (F2229) app. | The Manage Purchase Requisitions – Professional screen is displayed. |  |
| 3 | Search for Purchase Requisition | To search for a purchase requisition sent from the SAP Fieldglass system, set the relevant filters:Editing StatusPurchase RequisitionDocument TypeChoose Go. | A list of purchase requisitions is displayed.The purchase requisition is generated and approved automatically. |  |

#### Check Updated Work Order Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to check the updated work order status in SAP Fieldglass.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as a Buyer/Administrator. |  |  |
| 2 | Access Work Order | From the View menu, select Work Order in the Worker section.Choose the ID of the work order desired. |  |  |
| 3 | Verify Status | Around 2-5 minutes after the last procedure, the Status of the work order has changed to Created.On the Details tab, in the Work Order Details section, the status of the PR Ref ID field, and the PR Status Flag field are updated. | The status of work order is Approved. |  |

#### Accept Work Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to accept the work order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as Supplier. |  |  |
| 2 | Access Work Order | From the My Work Items menu, select Accept in the Worker Order section.Choose the ID of the work order desired. | The Work Order screen is displayed. |  |
| 3 | Accept Work Order | Choose Accept. | The Accept Work Order screen is displayed. |  |
| 4 | Complete Posting Information | Complete the fields Worker Email and Auto Invoice Type. The invitation for the worker to register in SAP Fieldglass is sent to this email address.Auto Invoice Type: Both |  |  |
| 5 | Complete Adjustments | In the Adjustment Type field, choose V1 (Invoice) from the dropdown list.Choose Continue. | The Review and Submit page displays. |  |
| 6 | Finalize Work Order Acceptance | Verify the work order details, and choose Accept. | The work order is accepted, and routed to the next step Activate (by Buyer). A notification is sent to the Program Office (PMO) to activate the work order. |  |

#### Check Purchase Order in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to check the purchase order in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders (Version 2) (F0842A) app. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Search for Purchase Order Status | To search for a purchase order sent from the SAP Fieldglass system, set the relevant filters.Choose Go. | A list of purchase orders is displayed.The purchase order is generated, and automatically approved. |  |

#### Activate Work Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to verify the completed activity requirements and activate the work order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as Program Office (PMO). |  |  |
| 2 | Access Work Order | From the My Work Items menu, select Activate in the Worker Order section.Choose the ID of the work order desired. | The work order screen is displayed. |  |
| 3 | Activate Work Order | Choose Activate. | The Activate Work Order dialog box is displayed. |  |
| 4 | Confirm Activation | In the Activate Work Order dialog box, choose OK. | The work order is activated.A registration email is sent to the worker's email address.Note The registration email is time sensitive, and expires after 21 days. If the registration code expires or the worker has misplaced the email, you can send the worker a new email. Choose Actions, and select Resend Invitation. |  |

#### Register Worker

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create your account in SAP Fieldglass after receiving a registration invite.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Check Registration Invite | Check your email inbox for the item Invitation to join the SAP Fieldglass system. To go to the registration site, choose the link Create Your Account in the invitation email. | The SAP Fieldglass Create Your Account screen is displayed. |  |
| 2 | Complete Basic Information | Enter the worker's Security ID, identical to what the supplier has entered when submitting this worker. |  |  |
| 3 | Complete Login Details | Enter the mandatory information in the Login Details field, including Desired Username and Password. |  |  |
| 4 | Complete Password Recovery | Choose one question from the Secret Question dropdown list, and enter an Answer to Secret Question, with which you can recover your username and password in case you lost your logon information. |  |  |
| 5 | Sign In | To complete the registration, choose Sign In. | The worker's username is displayed on the Welcome screen. |  |

#### Revise Work Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to revise a work order in SAP Fieldglass, and how to review the changes in SAP S/4HANA Cloud Public Edition.

Prerequisites

You can only revise a work order that is in status Confirmed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon in SAP Fieldglass (Buyer) | Log on in the SAP Fieldglass system as Buyer. |  |  |
| 2 | Access and Select Work Order | In the Worker section, select Work Order.In the Work Orders table, select a Work Order ID. | The Work Orders screen of the selected work order ID is displayed. |  |
| 3 | Revise Work Order | Choose Action > Revise. | The Create Work Order Revision screen is displayed. |  |
| 4 |  | In the Work Order Dates section, adjust the following data according to your business requirements:Start/Effective Date of Revision: Enter a new date.End Date: Enter a new date.In the Accounting section, adjust the following data according to your business requirements:For a Rate Category / UOM, enter a new amount in the Base Rate field, for example, 50.In the Cost Allocation section, choose Add or Remove Cost Centers.In the Add or Remove Cost Centers dialog box, search for a Cost Center, for example, 0010101901. Choose Add Selected. In the Selected Cost Centers section, remove the original cost center. Choose Update.For the newly added cost center, add a general ledger account, for example, 65301000.Note Don't remove the cost center to which the time sheet or invoice was posted.If you added multiple cost centers, ensure that all add up to 100% and that the Item Category is changed to N/A.Choose Continue > Submit. |  |  |
| 5 | Logon in SAP Fieldglass (Approver) | Log on in the SAP Fieldglass system as Approver. |  |  |
| 6 | Access and Select Revised Work Order | In the My Work Items section, choose Work Order Revision > Approve. | The Work Orders screen of the selected work order revision is displayed. |  |
| 7 | Approve Work Order Revision | Choose Approve. | The approved work order revision is in status Created. |  |
| 8 | Logon in SAP Fieldglass (Supplier) | Log on in the SAP Fieldglass system as Supplier. |  |  |
| 9 | Access and Select Work Order | In the My Work Items section, choose Work Order > Accept. | The Work Orders screen of the selected work order is displayed. |  |
| 10 | Accept Work Order Revision | Choose Accept. | The accepted work order revision is in status Pending External Acceptance. |  |
| 11 | Log on to SAP S/4HANA Cloud Public Edition (Purchaser) | Log on to the SAP Fiori launchpad as Purchaser. |  |  |
| 12 | Access App | Open the Manage Purchase Orders (Version 2) (F0842A) app. | The Manage Purchase Orders screen is displayed. |  |
| 13 | Search for Purchase Order | To search for a purchase order revised in the SAP Fieldglass system, set the relevant filters.Choose Go. | A list of purchase orders is displayed.The Net Order Value of the changed purchase order is update to the new amount revised in step 4. |  |
| 14 | Review Purchase Order Revision | To review the revised purchase order, select the revised purchase order. Select the Limit Item tab. | On the Limit Items tab, the Expected Value of the Purchase Order Item is updated to the new amount revised in step 4. |  |
| 15 |  | Select the Items tab. To review the revised purchase order items, select the purchase order item. | The Purchase Order Item screen is displayed.On the Schedule Lines tab, the data of the Start of Performance Period field, and the End of Performance Period field is updated to the new date revised in step 4.On the Account Assignment tab, the G/L Account is updated to the new account, for example 65301000, revised in step 4. |  |
| 16 | Logon in SAP Fieldglass (Approver) | Log on in the SAP Fieldglass system as Approver. |  |  |
| 17 | Check Updated Work Order Revision Status in SAP Fieldglass | Wait 2-5 minutes for the status replication.From the View menu, select Work Order in the Worker section.In the Work Orders table, select a Work Order ID. | The work order revision is in status Confirmed. |  |

#### Submit Time Sheet

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to complete a draft time sheet and submit it.

Prerequisites

|  |
| --- |
| Note The worker needs to be assigned to a task code before entering the time sheet. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system with the worker account you created in [Register Worker](#unique_30) [page ] 34. |  |  |
| 2 | Access Time Sheet | In the Work Items to Act Upon section, select the range of dates, for which you want to create a time sheet, and choose Complete Time Sheet. | The Enter Time Sheet screen is displayed. |  |
| 3 | Complete Timesheet | Enter hours in the Time Worked field.Note If the cost center defined in the job posting is associated with several task codes, there are multiple lines available to record your working hours. In this case, just enter hours into the line below the desired task code. |  |  |
| 4 | Submit Time Sheet | Choose Submit.Note If the Submit Time Sheet? dialog box is displayed, choose OK. | The time sheet submitted is routed to the next step Pending Approval in the workflow.Note In case no approval group is defined for the time sheet, an invoice is automatically generated. Then the next process is skipped. |  |

#### Check Generation of Service Entry Sheet in SAP S/4HANA Cloud Public Edition (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to check whether the service entry sheet is automatically generated in SAP S/4HANA Cloud Public Edition.

|  |
| --- |
| Note If accruals are not relevant for your business scenario, you can skip this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Service Entry Sheets (F2027) app. | The Manage Service Entry Sheets screen is displayed. |  |
| 3 | Search for Service Entry Sheet | To search for a service entry sheet sent from the SAP Fieldglass system, set the relevant filters.Choose Go. | A list of service entry sheets is displayed. |  |
| 4 | Select Service Entry Sheet | Select a service entry sheet. | The Service Entry Sheet screen is displayed.The service entry sheet was generated, and is in status In External Approval. |  |

#### Post Periodic Accruals in SAP S/4HANA Cloud Public Edition (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

This step is optional. For more information about the procedure, refer to the test script of the [Service Entry Sheet Based Accruals (63L)](https://me.sap.com/processnavigator/SolP/63L) scope item.

#### Approve Time Sheet

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to complete a draft time sheet, and submit it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as an Approver. |  |  |
| 2 | Access Work Item | From the My Work Items menu, go to the Time Sheet section. | The Time Sheet Approval screen is displayed. |  |
| 3 | Locate Time Sheet | To choose a specific time sheet, select the respective checkbox, and choose Approve. | The Approve Time Sheet dialog box is displayed. |  |
| 4 | Approve Time Sheet | In the Approve Time Sheet dialog box, choose Approve. | An invoice is automatically generated, and waiting for approval.Note ERS invoice won't be automatically generated after the ERS-related timesheet approval.Note In case no approval group is defined for the invoice, the invoice is automatically approved. Then the next process is skipped. |  |

#### Reject Time Sheet (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to reject a time sheet in SAP Fieldglass.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as an Approver. |  |  |
| 2 | Access Time Sheet | From the My Work Items menu, go to the Time Sheet section and choose Approve. | The My Work Items screen is displayed. |  |
| 3 | Select Time Sheet | To choose a specific time sheet, select the respective checkbox. Choose Reject. | The Reject Time Sheet dialog box is displayed. |  |
| 4 | Approve Time Sheet | In the Time Sheet Approval dialog box, choose Reject. | The time sheet is rejected.Note After the time sheet was rejected, you can ignore the invoice steps. |  |

#### Check Approval Status of Service Entry Sheet in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to check whether the service entry sheet is approved or rejected.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Service Entry Sheets (F2027) app. | The Manage Service Entry Sheets screen is displayed. |  |
| 3 | Search for Service Entry Sheet | To search for a service entry sheet sent from the SAP Fieldglass system, set the relevant filters.Choose Go. | A list of service entry sheets is displayed. |  |
| 4 | Select Service Entry Sheet | Select a service entry sheet. | The Service Entry Sheet screen is displayed.The service entry sheet was generated, and is in status Approved or Rejected. |  |

#### Approve Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to approve the invoice generated from the submitted and approved timesheet.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as Approver. | Invoices that require review and approval are displayed in the My Work Items area. |  |
| 2 | Access Invoice | In the My Work Items area, select Approve in the Invoice section. |  |  |
| 3 | Choose Invoice | Choose the ID of the invoice desired, and select Approve. | The Approve Invoice dialog box is displayed. |  |
| 4 | Approve Invoice | In the Approve Invoice dialog box, choose Approve. | An invoice request message is sent from the SAP Fieldglass system to the SAP S/4HANA Cloud Public Edition system. |  |

#### Check Invoice in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to check whether the invoice is generated, and automatically approved in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Supplier Invoices List (Version 2) (F1060A) app. | The Supplier Invoices List screen is displayed. |  |
| 3 | Search for the Invoice | To search for a invoice sent from the SAP Fieldglass system, set the relevant filters.Choose Go. | A list of invoices is displayed.The invoice is generated, and automatically approved. |  |

#### Revise Time Sheet (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to revise a time sheet in SAP Fieldglass, and how to review the changes in SAP S/4HANA Cloud Public Edition.

Prerequisites

The related invoice has to be in status Payment Pending or Paid.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon in SAP Fieldglass (Worker) | Log on to the SAP Fieldglass system as Worker. |  |  |
| 2 | Access Time Sheet | In the Worker section, select Time Sheet. | The Time Sheets screen is displayed. |  |
| 3 | Select and Revise Time Sheet | Choose the ID of an approved time sheet, and choose Actions > Revise.Maintain the work hours, for example 10 hrs, and choose Submit.From the dropdown list, select a reason for the revision, and choose Submit > Submit. | The revised time sheet is submitted. |  |
| 4 | Approve Time Sheet (Optional) | Optionally, approve the time sheet.Note For periodic accruals, ignore this step. | The time sheet is approved. |  |
| 5 | Log on to SAP S/4HANA Cloud Public Edition (Purchaser) | Log on to the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 6 | Access App | Open the Manage Service Entry Sheets - Lean Services (F2027) app. | The Manage Service Entry Sheets screen is displayed. |  |
| 7 | Search for Corresponding Service Entry Sheet | To search for the service entry sheet that corresponds with the original time sheet in SAP Fieldglass, choose Go. | The original service entry sheet is displayed and in status Deleted. |  |
|  |  | To search for the service entry sheet that corresponds with the approved time sheet in SAP Fieldglass, go to the Approval Status search filter field. From the dropdown list, choose Approved > Go. | A list of approved service entry sheets with revised working hours is displayed. |  |
| 9 | Log on to SAP S/4HANA Cloud Public Edition (Accounts Payable Accountant) | Log on to SAP Fiori launchpad as Accounts Payable Accountant. | SAP Fiori launchpad is displayed. |  |
| 10 | Access App | Open the Supplier Invoices List (F1060A) app. | The Supplier Invoices List screen is displayed. |  |
| 11 | Search for Supplier Invoice | To search for the original supplier invoice that was created in SAP Fieldglass, set specific search filters, for example Invoicing Party: 10300080. Choose Go. | The original supplier invoice and credit supplier invoice have the same reference number and are displayed in the supplier invoices list.In the Invoices table, you can check the values for both supplier invoices in the Gross Invoice Amount column, which reflects the difference of both statuses:ExampleGross invoice amount of original supplier invoice: 50 EURGross invoice amount of credit supplier invoice: -50 EUROn the Credit Supplier Invoice Detail screen, the credit memo is displayed as Transaction in the General Information section. |  |

#### Pay the Invoice in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to post and clear a single outgoing payment for the invoice transferred from the SAP Fieldglass system to the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Post Outgoing Payments (F1612) app. | The Post Outgoing Payments screen is displayed. |  |
| 3 | Enter Payment Data | In the General Information section, enter the following data:ExampleCompany Code: 1010 (DE)Posting Date: <today's date>Journal Entry Date: <today's date>Value Date: <today's date>Journal Entry Type: KZIn the Bank Data section, enter the following data:ExampleHouse Bank/Account: DEBK1/DEAC1 (DE)G/L Account: 11001000Amount: <amount to pay on existing invoice>In the Open Item Selection section, enter the following data:ExampleAccount Type: SupplierAccount ID: 10300080Choose Show Items. | In the Open Items/Standard section, a list of open items is displayed. |  |
| 4 | Select Item | To select the retrieved invoice to pay, choose Clear. | The invoice to pay is transferred to the Items to the Cleared (Standard) section. |  |
| 5 | Post Item | Choose Post. | The system message Journal entry xxxxxxxxxx (Year, Company Code) posted is displayed. |  |
| 6 | Confirm | To confirm the Information dialog box, choose OK. |  |  |
| 7 | Navigate Back | Choose Back. | The system message Journal entry has already been posted. You can now post a new payment. is displayed. |  |
| 8 | Dismiss Message | To dismiss the message, choose OK. |  |  |

#### Check Updated Invoice Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to check the updated invoice status in SAP Fieldglass.

Context

An invoice can have different statuses. The following statuses for an invoice can be displayed in SAP Fieldglass:

- Approval Paused
- Approved
- Consolidated
- Paid
- Payment Pending
- Payment Review
- Pending Approval
- Pending Consolidation
- Rejected

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as Buyer/Administrator. |  |  |
| 2 | Access Invoice and Display Updated Invoice Status | In the Payments section, select Invoice.Choose the ID of the invoice desired. | In the Status column, the updated status of the invoice is displayed. |  |

#### Close Work Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to close the work order in SAP Fieldglass, and how to review the changes in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon in SAP Fieldglass | Log on to the SAP Fieldglass system as Buyer/Administrator. |  |  |
| 2 | Access Work Order | In the Worker section, select Work Order. | The Work Orders screen is displayed. |  |
| 3 | Select and Close Work Order | Choose the ID of a work order, and choose Actions > Close Work Order. | The Close Worker pop-up window is displayed. |  |
| 4 | Confirm to Close Worker | In the Close Worker pop-up window, enter the following data:ExampleReason: closedActual End Date: 09/02/2020Note Set the actual end date to today or any day before.Allow Further Invoicing (Optional): NoChoose Close Worker. | The system message Work order Status is changed to Confirmed (Worker Closed) is displayed. |  |
| 5 | Logon in SAP S/4HANA Cloud Public Edition | Log on to the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 6 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen is displayed. |  |
| 7 | Search Corresponding Purchase Order | To search for the purchase order that corresponds with the revised, and closed work order in SAP Fieldglass, set the relevant search filters, and choose Go. | A list of purchase orders is displayed.In the Purchase Orders table, the value for the purchase order in the Net Order Value column is 0.00. |  |
| 8 | Select Purchase Order | Select the purchase order that is relevant for the work order, which was created in SAP Fieldglass. | The Purchase Order XXX screen is displayed. |  |
| 9 | Review Purchase Order | Review the details of the purchase order. | On the Purchase Order XXX screen, in the Limit Items section, the Purchase Order Item is in state Marked for Deletion. |  |

### Service Procurement for Statement of Work (SOW)

This section describes test procedures for each process step that belongs to the case Service Procurement for Statement of Work.

#### Manage Supplier Classification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In SAP Fieldglass, classifications are used to organize Statement of Work (SOW) templates and the suppliers that provide services. Before an SOW can be created, a classification must be selected. When creating an SOW, only the suppliers and SOW templates that are associated to the selected classification will be available.

Purpose

This procedure describes, how to create a new classification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as Buyer/Administrator. |  |  |
| 2 | Access Admin Configuration | Choose  Settings . | The Admin Configuration screen is displayed. |  |
| 3 | Access Classification List | In the Configuration section, choose Classification. | The Classifications List screen is displayed. |  |
| 4 | Create Classification | Choose New. Enter the required data, and choose Add. |  |  |

#### Associate Classification to Supplier

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to associate the newly added classification to a supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as Buyer/Administrator. |  |  |
| 2 | Access Admin Configuration | Choose  Settings . | The Admin Configuration screen is displayed. |  |
| 3 | Access Classification List | In the Configuration section, choose Classification. | The Classifications List screen is displayed. |  |
| 4 | Select Classification | On the Classification List screen, select a classification. | A detailed overview of the selected classification is displayed. |  |
| 5 | Associate Supplier | To associate suppliers to the selected classification, choose Suppliers > Add . | The Associate Suppliers to Classification dialog box is displayed. |  |
| 6 | Continue Association of Suppliers | In the Associate Suppliers to Classification dialog box, select supplier Name: 10300080.Choose Add. | The classification is associated to a supplier. |  |

#### Associate Business Units to SOW Template

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to associate a business unit to a statement of work (SOW) template.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as Buyer/Administrator. |  |  |
| 2 | Access Admin Configuration | Choose  Settings . | The Admin Configuration screen is displayed. |  |
| 3 | Access SOW Template List | In the Services section, choose SOW Template. | The SOW Template List screen is displayed. |  |
| 4 | Select SOW Template | On the SOW Template List screen, select a SOW template, for example Generic Use SOW Template. | A detailed overview of the selected SOW template is displayed. |  |
| 5 | Associate Business Unit | To associate business units to the selected SOW template, choose Business Units > Add . | The Associate Business Units to SOW Template dialog box is displayed. |  |
| 6 | Continue Association of Business Units | In the Associate Business Units to SOW Template dialog box, select business unit 1010.Choose Add. | The SOW template is associated to a business unit. |  |

#### Associate Classification to SOW Template

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to associate a classification to a statement of work (SOW) template.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as Buyer/Administrator. |  |  |
| 2 | Access Admin Configuration | Choose  Settings . | The Admin Configuration screen is displayed. |  |
| 3 | Access SOW Template List | In the Services section, choose SOW Template. | The SOW Template List screen is displayed. |  |
| 4 | Select SOW Template | On the SOW Template List screen, select a SOW template, for example Generic Use SOW Template. | A detailed overview of the selected SOW template is displayed. |  |
| 5 | Associate Classification | To associate a classification to the selected SOW template, choose Classification > Add . | The Associate Classification to SOW Template dialog box is displayed. |  |
| 6 | Continue Association of Classification | In the Associate Classification to SOW Template dialog box, select the classification, which you added in section [Associate Classification to Supplier](#unique_44) [page ] 52.Choose Add. | The SOW template is associated to a classification. |  |

#### Create Statement of Work

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to create a statement of work (SOW) by selecting a well-defined SOW template.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as Buyer/Administrator. |  |  |
| 2 | Access SOW Creation | From the Service section, choose Create Statement of Work. | The Create Statement of Work screen is displayed. |  |
| 3 | Select Classification of Statement of Work and SOW Owner | In the Create Statement of Work screen, select a classification for the statement of work and the SOW owner from the dropdown list. Choose Next Step. | Based on the selected SOW owner the statement of work may be routed for approval. |  |
| 4 | Select Source | To select a source, choose one of the following options:In the Cards view, select a recently used SOW template, and choose Select.In the List view, select a supplier and a SOW template, and choose Continue. | The Create Statement of Work screen is displayed. |  |
| 5 | Enter Detail Information | Enter the required data in all mandatory fields.In the Posting Information section, enter the following data:Legal Entity. Company Code DE (1010)Site: Plant 1 DE (1010)Note Locations are associated with specific sites. The correct value is automatically displayed in the Location field. There’s no need to change it.Business Unit: Purch. Org. 1010 (1010)Goods Receipt Is Expected: YesInvoice Is Goods Receipt Based: YesItem Category: EMaterial Group: YBMM00Product Type: 2Purchase Group: 001In the Cost Allocation section, enter the following data:Cost Center: 10101101Note If the expected cost center doesn’t exist in the list, choose the Add or remove Cost Centers link. In the Add or remove Cost Centers dialog box, check the option Unused. In the Search Cost Centers field, enter the name PFCProject1, and choose Apply Filters. Select the cost center, and choose Add Selected. To return to the Create Statement of Work screen, choose Update.General Ledger Account: 65100000Task Code: TCChoose Continue. | The Clauses screen is displayed. |  |
| 6 | Skip Clauses Entry | Clauses are defined as optional in the SOW template. To skip the clauses definition, choose Continue. | The Characteristics screen is displayed. |  |
| 7 | Select Characteristics Type | In the Type fields, select the Events checkbox. | The Fee Response field is displayed. |  |
| 8 | Add Event | Choose Add Event.Enter the name of the fee (for example: Analysis Deliverables), and enter appropriate data in the Amount field.Choose Add > Continue . | The SOW Workers screen is displayed. |  |
| 9 | Skip SOW Workers Entry | SOW Workers are defined as optional in the SOW template. To skip the SOW workers definition, choose Continue. | The Review and Submit screen is displayed. |  |
| 10 | Submit Statement of Work | Review the statement of work details on the Review and Submit screen. If necessary, apply changes.When all data has been reviewed, choose Submit. | The statement of work is saved, and routed to the next step Pending Approval in the workflow.Note The statement of work is assigned a unique ID. The ID is located at the top of the page above the title. |  |

#### Approve Statement of Work

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to review the statement of work for accuracy, if necessary apply changes, and approve it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as Approver. | The statement of work that requires review and approval is displayed in your Work Items menu. |  |
| 2 | Access Work Item | From the My Work Items menu, select Accept in the Statement of Work section. |  |  |
| 3 | Approve Statement of Work | Select the ID of the statement of work, and choose Approve.Note You can also access the statement of work by selecting Statement of Work from the View menu. | The statement of work is routed to the next step Pending Response in the workflow. |  |

#### Check Purchase Requisition in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to check whether the purchase requisition is generated and approved automatically in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad displayed. |  |
| 2 | Access App | Open the Manage Purchase Requisitions (F2229) app. | The Manage Purchase Requisitions – Professional screen is displayed. |  |
| 3 | Search for Purchase Requisition | To search for a purchase requisition sent from the SAP Fieldglass system, set the relevant filters:Editing StatusPurchase RequisitionDocument TypeChoose Go. | A list of purchase requisitions is displayed.The purchase requisition is generated and approved automatically. |  |

#### Check Updated Statement of Work Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to check the updated statement of work status in SAP Fieldglass.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as a Buyer/Administrator. |  |  |
| 2 | Access Statement of Work | From the View menu, select Statement of Work in the Services section.Choose the ID of the statement of work desired. |  |  |
| 3 | Verify Status | Around 2-5 minutes after the last procedure, the Status of the statement of work has changed to Created.On the Details tab, in the Statement of Work Details section, the status of the PR Ref ID field, and the PR Status Flag field are updated. | The status of the statement of work is Approved. |  |

#### Accept Statement of Work

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to accept the statement of work.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as Supplier. |  |  |
| 2 | Access Statement of Work | From the View menu, select Statement of Work in the Services section.Choose the ID of the statement of work desired. | The Statement of Work screen is displayed. |  |
| 3 | Accept Statement of Work | Choose Accept. | The Create SOW Response screen is displayed. |  |
| 4 | Review Statement of Work Details | Review the statement of work details, and choose Continue. | The Characteristics screen is displayed. |  |
| 5 | Submit Statement of Work Response | Choose Submit. | The statement of work response has been submitted.The statement of work is routed to the next step Response Pending Approval of the workflow. |  |

#### Check Purchase Order in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to check the purchase order in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders (Version 2) (F0842A) app. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Search for Purchase Order Status | To search for a purchase order sent from the SAP Fieldglass system, set the relevant filters.Choose Go. | A list of purchase orders is displayed.The purchase order is generated, and automatically approved. |  |

#### Revise Statement of Work (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to revise a statement of work (SOW) in SAP Fieldglass, and how to review the changes in SAP S/4HANA Cloud Public Edition.

Prerequisites

You can only revise a SOW that is in status Approved.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon in SAP Fieldglass (Buyer) | Log on in the SAP Fieldglass system as Buyer. |  |  |
| 2 | Access and Select SOW | In the Services section, choose Statement of Work.In the Statement of Work table, select a Statement of Work ID. | The Statement of Work screen of the selected statement of work ID is displayed. |  |
| 3 | Revise SOW | Choose Action > Revise. | The Create SOW Revision screen is displayed. |  |
| 4 |  | Choose Continue.In the Statement of Work section, adjust the following data according to your business requirements:End Date: Enter a new date.In the Cost Allocation section, choose Add or remove Cost Centers.In the Add or Remove Cost Centers dialog box, search for a Cost Center, for example, 0010101901. Choose Add Selected. In the Selected Cost Centers section, remove the original cost center. Choose Update.For the newly added cost center, add a general ledger account, for example, 65301000.Note Don't remove the cost center to which the invoice was posted.Ensure that the newly added cost center covers 100%.If you've added multiple cost centers, change the Item Category to N/A. |  |  |
| 5 |  | Choose Continue.On the Characteristics tab, you can add existing or new management events.Choose Continue > Submit. | The SOW revision is submitted. |  |
| 6 | Logon in SAP Fieldglass (Approver) | Log on in the SAP Fieldglass system as Approver. |  |  |
| 7 | Access and Select Revised SOW | In the My Work Items section, choose SOW Revision > Approve. | The Work Orders screen of the selected work order revision is displayed. |  |
| 8 | Approve SOW Revision | Choose Approve. | The approved SOW revision is in status Created. |  |
| 9 | Logon in SAP Fieldglass (Supplier) | Log on in the SAP Fieldglass system as Supplier. |  |  |
| 10 | Access and Select SOW | In the My Work Items section, choose SOW > Accept. | The Statement of Work screen of the selected work order is displayed. |  |
| 11 | Accept SOW Revision | Choose Accept. | The accepted SOW revision is in status Response Pending Approval. |  |
| 12 | Logon in SAP S/4HANA Cloud Public Edition (Purchaser) | Log on to the SAP Fiori launchpad as Purchaser. |  |  |
| 13 | Access App | Open the Manage Purchase Orders (Version 2) (F0842A) app. | The Manage Purchase Orders screen is displayed. |  |
| 14 | Search for Purchase Order | To search for a purchase order revised in the SAP Fieldglass system, set the relevant filters.Choose Go. | A list of purchase orders is displayed.The Net Order Value of the changed purchase order is update to the new amount revised in step 4. |  |
| 15 | Review Purchase Order Revision | To review the revised purchase order, select the revised purchase order. Select the Limit Item tab. | On the Limit Items tab, the Expected Value of the Purchase Order Item is updated to the new amount revised in step 4. |  |
| 16 |  | Select the Items tab. To review the revised purchase order items, select the purchase order item. | The Purchase Order Item screen is displayed.On the Schedule Lines tab, the data of the Start of Performance Period field, and the End of Performance Period field is updated to the new date revised in step 4.On the Account Assignment tab, the G/L Account is updated to the new account, for example 65301000, revised in step 4. |  |
| 17 | Logon in SAP Fieldglass (Approver) | Log on in the SAP Fieldglass system as Approver. |  |  |
| 18 | Check Updated Work Order Revision Status in SAP Fieldglass | Wait 2-5 minutes for the status replication.From the View menu, select Statement of Work in the Services section.In the Statement of Work table, select a Statment of Work ID. | The SOW revision is in status Approved. |  |

#### Mark Work Item as Complete

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to mark a work item as complete.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as Supplier. |  |  |
| 2 | Access SOW Line Item | In the Services section, choose SOW Line Item.Choose the Line Item ID of the event added in the statement of work. | The Event screen is displayed. |  |
| 3 | Mark Work Item as Complete | Choose Mark as Complete. | The Setup screen is displayed. |  |
| 4 | Enter Complete Date | Enter the Complete Date (for example: today), and choose Continue. | The Review screen is displayed. |  |
| 5 | Review and Submit | Review the event details, and choose Submit. | The event is marked as complete, and routed to next step Pending Approval in the workflow. |  |

#### Check Generation of Service Entry Sheet in SAP S/4HANA Cloud Public Edition (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to check whether the service entry sheet is automatically generated in SAP S/4HANA Cloud Public Edition.

|  |
| --- |
| Note If accruals are not relevant for your business scenario, you can skip this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Service Entry Sheets (F2027) app. | The Manage Service Entry Sheets screen is displayed. |  |
| 3 | Search for Service Entry Sheet | To search for a service entry sheet sent from the SAP Fieldglass system, set the relevant filters.Choose Go. | A list of service entry sheets is displayed. |  |
| 4 | Select Service Entry Sheet | Select a service entry sheet. | The Service Entry Sheet screen is displayed.The service entry sheet was generated, and is in status In External Approval. |  |

#### Post Periodic Accruals in SAP S/4HANA Cloud Public Edition (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

This step is optional. For more information about the procedure, refer to the test script of the [Service Entry Sheet Based Accruals (63L)](https://me.sap.com/processnavigator/SolP/63L) scope item.

#### Approve Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to review the event for accuracy, if necessary apply changes, and approve the transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as Buyer/Administrator. |  |  |
| 2 | Access Work Item | In the My Work Items area, select Approve in the Event section. |  |  |
| 3 | Approve Event | Choose the ID of the event, and select Approve. | The Approve Event dialog box is displayed. |  |
| 4 | Continue Approval of Event | In the Approve Time Sheet dialog box, maintain different amounts/percentages according to the different G/L accounts, enter comments, and choose Approve. | The event is approved.A Service Entry Sheet Request message is sent from the SAP Fieldglass system to SAP S/4HANA Cloud Public Edition. |  |

#### Reject Transaction (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to review a transaction that was made in a statement of work (SOW) and reject this transaction, if required.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as Buyer/Administrator. |  |  |
| 2 | Access Work Item | In the My Work Items area, choose Approve in the Event section. | The Your Work Items \| Event screen is displayed. |  |
| 3 | Select Statement of Work | Select a SOW and choose Reject. | The Reject Event dialog box is displayed. |  |
| 4 | Reject Event | In the Reject Event dialog box, select a reason for rejection from the dropdown list. Optionally, provide comments about the rejection. Choose Reject. | The transaction is rejected. |  |

#### Check Approval Status of Service Entry Sheet in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to check whether the service entry sheet is approved or rejected.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Service Entry Sheets (F2027) app. | The Manage Service Entry Sheets screen is displayed. |  |
| 3 | Search for Service Entry Sheet | To search for a service entry sheet sent from the SAP Fieldglass system, set the relevant filters.Choose Go. | A list of service entry sheets is displayed. |  |
| 4 | Select Service Entry Sheet | Select a service entry sheet. | The Service Entry Sheet screen is displayed.The service entry sheet was generated, and is in status Approved or Rejected. |  |

#### Approve SOW Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to approve the SOW invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as Approver. | Invoices that require review and approval are displayed in the My Work Items area. |  |
| 2 | Access SOW Invoice | In the My Work Items area, select Approve in the SOW Invoice section. |  |  |
| 3 | Choose SOW Invoice | Choose the ID of the SOW invoice desired, and select Approve. | The Approve SOW Invoice dialog box is displayed. |  |
| 4 | Approve SOW Invoice | In the Approve SOW Invoice dialog box, choose Approve. | An invoice request message is sent from the SAP Fieldglass system to the SAP S/4HANA Cloud Public Edition system. |  |

#### Check Invoice in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to check whether the invoice is generated, and automatically approved in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Supplier Invoices List (Version 2) (F1060A) app. | The Supplier Invoices List screen is displayed. |  |
| 3 | Search for the Invoice | To search for a invoice sent from the SAP Fieldglass system, set the relevant filters.Choose Go. | A list of invoices is displayed.The invoice is generated, and automatically approved. |  |

#### Pay the Invoice in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to post and clear a single outgoing payment for the invoice transferred from the SAP Fieldglass system to the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Post Outgoing Payments (F1612) app. | The Post Outgoing Payments screen is displayed. |  |
| 3 | Enter Payment Data | In the General Information section, enter the following data:ExampleCompany Code: 1010 (DE)Posting Date: <today's date>Journal Entry Date: <today's date>Value Date: <today's date>Journal Entry Type: KZIn the Bank Data section, enter the following data:ExampleHouse Bank/Account: DEBK1/DEAC1 (DE)G/L Account: 11001000Amount: <amount to pay on existing invoice>In the Open Item Selection section, enter the following data:ExampleAccount Type: SupplierAccount ID: 10300080Choose Show Items. | In the Open Items/Standard section, a list of open items is displayed. |  |
| 4 | Select Item | To select the retrieved invoice to pay, choose Clear. | The invoice to pay is transferred to the Items to the Cleared (Standard) section. |  |
| 5 | Post Item | Choose Post. | The system message Journal entry xxxxxxxxxx (Year, Company Code) posted is displayed. |  |
| 6 | Confirm | To confirm the Information dialog box, choose OK. |  |  |
| 7 | Navigate Back | Choose Back. | The system message Journal entry has already been posted. You can now post a new payment. is displayed. |  |
| 8 | Dismiss Message | To dismiss the message, choose OK. |  |  |

#### Check Updated Invoice Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to check the updated invoice status in SAP Fieldglass.

Context

An invoice can have different statuses. The following statuses for an invoice can be displayed in SAP Fieldglass:

- Approval Paused
- Approved
- Consolidated
- Paid
- Payment Pending
- Payment Review
- Pending Approval
- Pending Consolidation
- Rejected

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as Buyer/Administrator. |  |  |
| 2 | Access Invoice and Display Updated Invoice Status | In the Payments section, select Invoice.Choose the ID of the invoice desired. | In the Status column, the updated status of the invoice is displayed. |  |

#### Close Statement of Work

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to close the statement of work in SAP Fieldglass, and how to review the changes in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon in SAP Fieldglass | Log on to the SAP Fieldglass system as Buyer/Administrator. |  |  |
| 2 | Access Statement of Work | In the Services section, choose Statement of Work. | The Statement of Work screen is displayed. |  |
| 3 | Select and Close Statement of Work | Choose the ID of a statement of work, and choose Actions > Close Statement of Work. |  | The Close Statement of Work pop-up window is displayed. |
| 4 | Confirm to Close Statement of Work | In the Close Statement of Work pop-up window, enter the following data:ExampleReason: closedActual End Date: 09/02/2020Note Set the actual end date to today or any day before.Allow Further Invoicing (Optional): NoChoose Close Statement of Work. | The system message Statement of Work Status is changed to Confirmed (Worker Closed) is displayed. |  |
| 5 | Logon in SAP S/4HANA Cloud Public Edition | Log on to the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 6 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen is displayed. |  |
| 7 | Search Corresponding Purchase Order | To search for the purchase order that corresponds with the revised, and closed work order in SAP Fieldglass, set the relevant search filters, and choose Go. | A list of purchase orders is displayed.In the Purchase Orders table, the value for the purchase order in the Net Order Value column is 0.00. |  |
| 8 | Select Purchase Order | Select the purchase order that is relevant for the work order, which was created in SAP Fieldglass. | The Purchase Order XXX screen is displayed. |  |
| 9 | Review Purchase Order | Review the details of the purchase order. | On the Purchase Order XXX screen, in the Limit Items section, the Purchase Order Item is in state Marked for Deletion. |  |

### Evaluated Receipt Settlement (ERS) Invoice

#### Check Required Settings for ERS Supplier Invoice in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check in SAP S/4HANA Cloud Public Edition if the required settings GR-Based Invoice Verif. and Eval. Receipt Settlement are activated for the ERS supplier.

|  |
| --- |
| Note This procedure is a prerequisite for the ERS supplier invoice scenario. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Maintain Business Partner (BP) app. | The Maintain Business Partner screen is displayed. |  |
| 3 | Select Business Partner | In the Find field, select Business Partner from the dropdown list. In the Business Partner field, enter 10300003 (DE). Choose Start.From the search result list, double-click the business partner 10300003. | The Display Organization : 10300003 screen is displayed.In the Display in BP role field, select Supplier from the dropdown list. |  |
| 4 | Select Supplier View | In the Display in BP role field, select Supplier from the dropdown list. | The Display Organization: 10300003, role Supplier screen is displayed. |  |
| 5 | Check Required Settings for ERS Supplier Invoice Scenario | Select the Purchasing tab (Ctrl + F2).In the Purchasing Organization section, navigate to the Purchasing Data tab and do the following:To check, if the GR-Based Invoice Verif. checkbox is selected, navigate to the Control Data section.To check, if the Eval. Receipt Settlement checkbox is selected, navigate to the Additional Purchasing Data section. | The required settings GR-Based Invoice Verif. and Eval. Receipt Settlement are activated. |  |

#### Create and Approve Service Entry Sheet in SAP S/4HANA Cloud Public Edition

Use ERS Supplier, for example 10300003, to create the service entry sheet.

- Create and Approve Service Entry Sheet from Work Order

To create a timesheet in SAP Fieldglass and check whether the service entry sheet is approved in SAP S/4HANA Cloud Public Edition, repeat chapter [Create and Submit Job Posting](#unique_19) [page ] 21 to chapter [Check Generation of Service Entry Sheet in SAP S/4HANA Cloud Public Edition (Optional)](#unique_32) [page ] 39.

- Create and Approve Service Entry Sheet from Statement of Work

To submit a work item in SAP Fieldglass and check whether the service entry sheet is approved in SAP S/4HANA Cloud Public Edition, repeat chapter [Manage Supplier Classification](#unique_43) [page ] 52 to chapter [Check Generation of Service Entry Sheet in SAP S/4HANA Cloud Public Edition (Optional)](#unique_32) [page ] 39.

#### Create and Run ERS Supplier Invoice Job in SAP S/4HANA Cloud Public Edition (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to create an ERS supplier invoice job and run it immediately in SAP S/4HANA Cloud Public Edition.

|  |
| --- |
| Note This procedure is only relevant for you, if you've not yet configured the ERS invoice job as a batch job. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Schedule Supplier Invoice Jobs (F1683) app. | The Application Jobs screen is displayed. |  |
| 3 | Create and Run ERS Invoice Job | To create an ERS invoice job and run it immediately, complete the following steps:Choose Create.The Template Selection section is displayed.In the Template Selection section, enter the following data according to your business requirements:Job Template: Evaluated Receipt Settlement (ERS)You can use the Value Help (), to search for a specific template.Job Name: EW - Evaluated Receipt Settlement (ERS) (for example)Choose Step 2.The Scheduling Options section is displayed.In the Scheduling Options section, select the Start Immediately checkbox.Choose Step 3.The Parameters section is displayed.In the Parameters section, enter the following data:You can use the Value Help (), to search for specific values.Company Code: 1010Supplier: 10300003Document Selection: 4Test Run: Do not select the checkbox.Choose Schedule. | The ERS invoice job is running immediately.After 2 -5 minutes, the invoice job is in status Finished. |  |

#### Check ERS Supplier Invoice in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to check the ERS supplier invoice in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Supplier Invoices List (F1060A) app. | The Supplier Invoices List screen is displayed. |  |
| 3 | Search for the Invoice | To search for the invoice created, set the relevant filters.Choose Go. | A list of invoices is displayed. |  |

#### Check ERS Supplier Invoice in SAP Fieldglass

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check in SAP Fieldglass whether the invoice is automatically generated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fieldglass system as Buyer/Administrator. |  |  |
| 2 | Access Invoice and Display Updated Invoice Status | In the Payments section, choose Invoice.Choose the ID of the invoice desired. | In the Status column, the updated status of the invoice is displayed. |  |
| 3 | Check Invoice | 2–3 minutes after the invoice was created in SAP S/4HANA Cloud Public Edition, the new invoice related to the timesheet is created. The status of this invoice is Paid. | The invoice is automatically generated. |  |

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
> Flagged while digesting this document, not verified: Invite Supplier step searches supplier 10300090 while the master data table and other steps use supplier 10300080.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Invoice adjustment type is V0 in the master data table but the Accept Work Order step selects V1 (Invoice).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/test-script-service-procurement-with-sap-business-network-and-sap-fiel]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/22K_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 126,719 chars in the whole document
