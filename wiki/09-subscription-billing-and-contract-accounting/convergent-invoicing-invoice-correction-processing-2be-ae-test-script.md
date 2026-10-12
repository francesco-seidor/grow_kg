---
id: 09-subscription-billing-and-contract-accounting/convergent-invoicing-invoice-correction-processing-2be-ae-test-script
title: Convergent Invoicing – Invoice Correction Processing (2BE_AE) – Test Script (2BE_S4CLD2608_BPD_EN_AE)
description: "S/4HANA Cloud test script, scope item 2BE_AE: invoice correction via credit/debit memo billing requests, optional approval workflow, billing, invoicing, print."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/recurring-and-one-off-billing]
aliases: [2BE_S4CLD2608_BPD_EN_AE]
keywords: ["Convergent Invoicing: Recurring, One-Off and Usage…", invoice correction processing, credit and debit memos, billing requests, billing request approval, flexible workflow, convergent invoicing, billing process, invoicing process, scope item testing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2BE_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-809
topic: 09-subscription-billing-and-contract-accounting/recurring-and-one-off-billing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Convergent Invoicing – Invoice Correction Processing (2BE_AE) – Test Script (2BE_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2BE_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Convergent Invoicing: Recurring, One-Off and Usage Billing, Invoice Correction** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Convergent Invoicing – Invoice Correction Processing (2BE_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Convergent Invoicing – Invoice Correction Processing (2BE_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232849045)

[2 Prerequisites 4](#_Toc232849046)

[2.1 System Access 4](#_Toc232849047)

[2.2 Roles 4](#_Toc232849048)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232849049)

[2.4 Business Conditions 5](#_Toc232849050)

[2.5 Preliminary Steps 6](#_Toc232849051)

[2.5.1 Preliminary Step Relevant to Flexible Workflow for Release of Billing Request (Optional) 6](#_Toc232849052)

[2.5.1.1 Implement Cloud BAdI 6](#_Toc232849053)

[2.5.1.2 Manage Teams and Responsibilities 8](#_Toc232849054)

[2.5.1.3 Define and Activate Workflow 9](#_Toc232849055)

[3 Overview Table 11](#_Toc232849056)

[4 Test Procedures 12](#_Toc232849057)

[4.1 Create Billing Request 12](#_Toc232849058)

[4.2 Approve Billing Request Release (Optional) 15](#_Toc232849059)

[4.3 Perform Billing Process 16](#_Toc232849060)

[4.3.1 Option 1: Perform Billing Process (Mass Run) 17](#_Toc232849061)

[4.3.2 Option 2: Perform Billing Process (Individual Run) 18](#_Toc232849062)

[4.4 Display Billing Document (Optional) 19](#_Toc232849063)

[4.5 Perform Invoicing Process 20](#_Toc232849064)

[4.5.1 Option 1: Perform Invoicing Process (Mass Run) 20](#_Toc232849065)

[4.5.2 Option 2: Perform Invoicing Process (Individual Run) 22](#_Toc232849066)

[4.6 Display Invoicing Document (Optional) 23](#_Toc232849067)

[4.7 Print Invoicing Document (Optional) 24](#_Toc232849068)

[5 Appendix 26](#_Toc232849069)

[5.1 Process Integration 26](#_Toc232849070)

[5.1.1 Preceding Processes 26](#_Toc232849071)

## Purpose

Overview

Invoice correction processing lets you correct existing invoices using billing requests. You can create debit and credit memos correcting line item amounts or billable item amounts.

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
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Invoicing Specialist (Convergent Invoicing) | SAP_BR_INVOICING_SPEC_CINV | Convergent Invoicing / Subscription Billing | SAP_BR_INVOICING_SPECIALIST_CINV / SAP_CEC_SPT_SUBSCR_BILLG_SPCLST_PC |  |
| Administrator (Convergent Invoicing) | SAP_BR_INVOICING_ADMIN_CINV | Administration - Convergent Invoicing | SAP_BR_INVOICING_ADMIN_CINV |  |
| Extensibility Specialist | SAP_BR_EXTENSIBILITY_SPEC | Extensibility / Extensibility | SAP_BR_EXTENSIBILITY_SPEC / SAP_CA_SPT_EXT_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 2AR - Contract Accounting – Master Data and Basic Functions | Must be run before the test script. The business partner and contract account must be created. |
| 2BG - Convergent Invoicing – Invoice Creation for Usage and Service | Must be run before this test script. The invoicing document must be created. |

### Preliminary Steps

#### Preliminary Step Relevant to Flexible Workflow for Release of Billing Request (Optional)

Context

Flexible Workflow for Release of Billing Request enables the approval processing of releasing Billing Request. If a Billing Request meets conditions set in Manage Workflows for Contract Accounting (F5135), it is automatically blocked and routed to approver for action (Release/Reject/Discard).

During the workflow:

- Approvers receive workflows in "My Inbox for Convergent Invoicing" and can release/reject/discard the Billing Request.
- After the Billing Request is released, the corresponding Billable Item has been generated for further processing.
- If the Billing Request is discarded by Approver, the status of the corresponding credit memo/debit memo is set to Discarded and the workflow completes.
- If the Billing Request is rejected by Approver, the corresponding credit memo/debit memo status is set to Open. The requestor can accept the rejection event of the Billing Request or resend it for approval.
- If the Billing Request is resent to approver, the approval cycle will restart.

(For SAP internal test purposes, please execute this test script in an extensibility test environment.)

##### Implement Cloud BAdI

Purpose

This Business Add-In (BAdI) FKK_EVENT_8300 is used in the Convergent Invoicing (FI-CA-INV) component. You can use this BAdI to activate the billing request release approval workflow. This BAdI is called when a billing request is sent for checking. The workflow only runs when this Cloud BAdI Implementation returns for parameter IsWorkflowActive = abap_true.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Extensibility Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Custom Logic (F6957). | The Custom Logic screen displays. |  |
| 3 | Create Enhancement Implementation | Choose Create.Make the following entry to filter the extension point.Business Context: Convergent Invoicing: Billing RequestChoose the entry with ID FKK_EVENT_8300.Choose Step 2. | The Extension Points are filtered. |  |
| 4 | Fill Implementation ID | Make the following entries and choose Review.Description: for example, Billing request release approvalImplementation ID: for example, YY1_BILLINGREQUESTAPPROVAL | The New Implementation screen displays. |  |
| 5 | Save and Publish | Choose Create.Choose Publish. | The custom logic is created with status Published. |  |
| 6 | Add Coding | Choose Open Code Editor.Choose Edit.Implement your logic in Draft Logic section.Sample Code IF cabillgreqheader-cabillgreqtotalamount > 100. isworkflowactive = abap_true. ENDIF. |  |  |
| 6 | Save and Publish | Choose Save and Publish. | The custom logic is published with sample code. |  |

##### Manage Teams and Responsibilities

Purpose

In this procedure, you define Responsibility for Rules Used in Workflow Steps and assign Users to Responsibilities. This Is only relevant to Flexible Workflow. If Flexible Workflow is out of scope, you can skip this step.

|  |
| --- |
| Note The approver(s) and requester(s) must be different business users. In this test script, we use the business user of Invoicing Specialist as the requester and the business user of the Administration - Convergent Invoicing as the approver. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration.. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Teams and Responsibilities - Contract Accounting (F5134).Choose Create. | The Team screen displays. |  |
| 3 | Maintain the Team Details | Make the following entries and choose Save:In the General Information tabName: Team of Billing RequestGlobal ID:<any ID>Description: Team of Billing RequestStatus: EnabledType: SCINVBREQWFIn the Team Owners tab:Choose Create, and maintain the below values:Business Partner: <Select Business Partner>In the Team Members tab:Choose Create, and maintain the below values:Business Partner: <Administrator (Convergent Invoicing)>Functions: SCINVWF01(Function for Approving - Level 1) |  |  |
| 4 | Save the Team | Choose Create. | The team is created |  |

##### Define and Activate Workflow

Purpose

You can create a new workflow by copying the standard template or create a new entry directly. In this step, you create the Workflow for Release of Billing Request by copying the standard template, and then activate it. This Is only relevant to Flexible Workflow. If Flexible Workflow is out of scope, you can skip this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Contract Accounting (F5135). | The Manage Workflows screen displays. |  |
| 3 | Select Workflow | Select Workflow for Release of Billing Request from the Workflows dropdown list. |  |  |
| 4 | Choose Template | Choose Workflow Template – Billing Request. |  |  |
| 5 | Copy Workflow | Choose Copy. | The Copy Workflow screen displays. |  |
| 6 | Enter Workflow Details | Make the following entries and choose Save:Choose the Header tab:Workflow Name: for example, Billing Request Approval workflowChoose the Properties tab:Description: for example, Billing Request Approval workflowValid From: <Today’s date>Valid To: 12/31/9999Choose the Start Conditions tab:Only start the workflow if all of the following preconditions are met:For example, Billing Request Total Amount is greater than or equal to 100.Choose the Steps tab.Choose 1. Approve the release of the Billing Request and Navigation:Choose the Header tab:Step Name: for example, Approve the release of the Billing RequestChoose the Recipients tab:Assignment By: TeamTeam: <the team you created at previous step>Step to be completed by: One of the recipients.Choose the Exception Handling tab:Required Action: Do NothingAction result: Cancel workflow |  |  |
| 7 | Activate Rule | Choose Apply, then choose Save and Activate.Note The template workflow is delivered by default as active with no preconditions defined, which means this workflow will always start. Make sure you've deactivated the standard template if you don’t want to use it before you start to release your billing request. | The workflow for Release of Billing Request is activated. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/ Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Billing Request](#unique_12) [page ] 12 | Invoicing Specialist (Convergent Invoicing) | Manage Credit/Debit Memos (F2389) | The billing request of credit/ debit is released. The billable item of credit/ debit Memo is created. |
| [Approve Billing Request Release (Optional)](#unique_13) [page ] 15 | Administrator (Convergent Invoicing) | My Inbox for Convergent Invoicing - All Items (F7031) | Billing Request Release is approved. The relevant Billable Items are created. |
| [Option 1: Perform Billing Process (Mass Run)](#unique_14) [page ] 17 | Administrator (Convergent Invoicing) | Execute Billing - Mass Run (F3525) | The billing document is created. |
| [Option 2: Perform Billing Process (Individual Run)](#unique_15) [page ] 18 | Invoicing Specialist (Convergent Invoicing) | Execute Billing - Business Partner (FKKBIX_S) | The billing document is created. |
| [Display Billing Document (Optional)](#unique_16) [page ] 19 | Invoicing Specialist (Convergent Invoicing) | Manage Billing Documents (F2250) | The billing document is displayed. |
| [Option 1: Perform Invoicing Process (Mass Run)](#unique_17) [page ] 20 | Administrator (Convergent Invoicing) | Execute Invoicing - Mass Run (F3524) | The invoicing document is created. |
| [Option 2: Perform Invoicing Process (Individual Run)](#unique_18) [page ] 22 | Invoicing Specialist (Convergent Invoicing) | Execute Invoicing - Business Partner (FKKINV_S) | The invoicing document is created. |
| [Display Invoicing Document (Optional)](#unique_19) [page ] 23 | Invoicing Specialist (Convergent Invoicing) | Manage Invoicing Documents (F2048) | The invoicing document is displayed. |
| [Print Invoicing Document (Optional)](#unique_20) [page ] 24 | Administrator (Convergent Invoicing) | Print Correspondence (F3537) | The invoicing document is printed out |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Billing Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

After completing the prerequisite steps relevant to Flexible Workflow for Release of Billing Request and setting the start conditions with Billing Request Total Amount is greater than or equal to 100 for example in the Define and Activate Your Approval Workflows step, you can send the Release of Billing Request by pressing. For checking at Manage Credit/Debit Memos (F2389) to trigger the workflow, once the start conditions of the Release of Billing Request are met, the workflow starts, and a new item is sent to the the approver 's Inbox. The approver can decide to approve/reject the Billing Request Release for further processing.

If you don’t enable Flexible Workflow for Release of Billing Request or the start conditions of workflow don’t meet, Invoicing Specialist can directly release the Billing Request without any approval.

Purpose

In this step, you create and release the billing request of credit /debit. The billable item of credit memo /debit memo is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Manage Credit/Debit Memos (F2389) tile. | The Manage Credit/Debit Memos page is displayed. |  |
| 3 | Create Billing Request | In Manage Credit/Debit Memos screen, choose Create . |  |  |
| 4 | Maintain Parameters | In Add Credit/Debit Memo screen, make the following entries as below:Invoicing Document: <the invoicing document number>Reason: <the billing request reason>Choose OK to close Add Credit/Debit Memo screen. | The Process Credit/Debit Memo page is displayed. |  |
| 5 | Create Billing Request Line Item |  |  |  |
| 5.1 | Option 1: Create Billing Request Line Item from Invoicing Header | In Process Credit/Debit Memo, choose Add Overall Debit button if you are creating Debit Memo and make the following entries as below:Debit Memo Amount: <the amount>In Process Credit/Debit Memo, choose Add Overall Credit button if you are creating Credit Memo and make the following entries as below:Credit Memo Amount:<the amount>Choose OK button |  |  |
| 5.2 | Option 2: Create Billing Request Line Item from Invoicing document item | In Process Credit/Debit Memo, choose Add Debit for Invoice Items button if you are creating Debit Memo and make the following entries as below:Debit Memo Amount: <the amount>In Process Credit/Debit Memo, choose Add Credit for Invoice Items button if you are creating Credit Memo and make the following entries as below:Credit Memo Amount: <the amount>Select the checkbox in the front of the line item and choose Add to close the popup window. |  |  |
| 5.3 | Option 3: Create Billing Request Line Item from Billable Item | In Process Credit/Debit Memo, choose Add Debit for Billable Items button if you are creating Debit Memo and make the following entries as below:Debit Memo Amount: <the amount>In Process Credit/Debit Memo, choose Add Credit for Billable Items button if you are creating Credit Memo and make the following entries as below:Credit Memo Amount: <the amount>Select the checkbox in the front of the line item Choose Add to close the popup window. |  |  |
| 6 | Save Billing Request | Choose Create. |  |  |
| 7 | Locate Billing Request | Choose back button to navigate to Manage Credit/Debit Memo screen. |  |  |
| 8 | Make Parameters | In the Manage Credit/Debit Memo screen, make the following entries as below to search out the billing request you created at last step.Credit/Debit Memo: <the number of your credit memo or debit memo>Choose Go . |  |  |
| 9 | Check Billing Request | Choose the debit memo or credit memo you search out and choose For Checking. | The billing request is released for checking.Note If you have enabled Workflow for Release of Billing Request and the start conditions of workflow have been met, the approval document has been sent to the recipient for approval. You can’t release the Billing Request before getting approval. Please come to Approve Billing Request Release to execute the approval process.If you don’t enable Workflow for Release of Billing Request or start conditions don’t meet, you can release the Billing Request directly. |  |
| 10 | Release Billing Request | Choose Release and choose OK to close the popup window. | The billing request is released. The billable item is created. |  |
| 11 | Display Billable item | Choose Display Billable Items to monitor newly created debits or credits. |  |  |

### Approve Billing Request Release (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you approve the Billing Request Release. The relevant Billable Items are created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Administrator (Convergent Invoicing) . | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose the appMy Inbox for Convergent Invoicing - All Items (F7031) tile. | The My Inbox page is displayed. |  |
| 3 | Locate the inbox item of Billing Request Release | On the My Inbox screen, make the entries as below:Search Panel: <the Billing Request ID >Choose Search and choose the searched-out Inbox item. | The inbox item named Approve the release of Billing Request <Billing Request Number> is located. (The Billing Request is the one you created at previous steps.) |  |
| 4 | Approve the Billing Request Release | On the Approve the release of the billing request screen, choose Release.On the Submit Decision screen, make the entries as below:Decision Note: <your decision note>Choose Submit. | The Billing Request has been approved. |  |
| 5 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Invoicing Specialist. | The page containing the Fiori apps associated with your role is displayed. |  |
| 6 | Access the App | Choose the Manage Credit/Debit Memos tile. | The Manage Credit/Debit Memo page is displayed. |  |
| 7 | Locate Credit/Debit Memo | In the Manage Credit/Debit Memo screen, make the following entries as below to search out the billing request you created at last step.Credit/Debit Memo: <the number of your credit memo or debit memo>Choose Go button. | The status of the Credit/Debit Memo is Release. |  |
| 8 | Display Billable item | Choose Display Billable Items to monitor newly created debits or credits. |  |  |

### Perform Billing Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you start up the billing process to create the billing document. You can process with mass run or individual creation.

|  |
| --- |
| Note If you enabled Clarification at 2BG-Convergent Invoicing: Invoicing creation for Usage and Service, please follow the Perform Billing Process of 2BG-Convergent Invoicing: Invoicing creation for Usage and Service to perform Billing.If the clarification case is created when perform billing, please follow the Clarify Clarification Case Relevant to Billing Document (Optional) of 2BG-Convergent Invoicing: Invoicing creation for Usage and Service to perform Billing |

#### Option 1: Perform Billing Process (Mass Run)

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
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Administrator (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Execute Billing - Mass Run (F3525) tile. | The Execute Billing - Mass Run page is displayed. |  |
| 3 | Create Application Job | Choose Create button to create a new application job. | The New Job: Billing (Mass Creation) page is displayed. |  |
| 4 | Select Template | Make the following entries as below:Job Template; Billing (Mass Creation)Job Name; <job name>Choose Step2. |  |  |
| 5 | Maintain Schedule Options | Make the following entries as below:Start Immediately: chooseRecurrence Pattern: Single RunChoose Step3. |  |  |
| 6 | Maintain Parameters | Make the following entries as below:Prefix of Run ID: <Prefix of Run ID>Billing Process: Y001Contract Account: <the required contract account>Simulation Run: <don’t choose>Billing Date: <the current date>Problem Class: <problem class> |  |  |
| 7 | Execute | Choose Schedule. | The job is running immediately. |  |
| 8 | Locate the job from application job list | In the Execute Billing - Mass Run screen, make the following entries as below:Date From-To:: <Today -1/+1 day>Choose Go button. | The application job you want to find was located in the application jobs list. |  |
| 9 | Check Log | Choose Image of Log to locate the application job log. | The log of application job is displayed. From the log, you can see the result of application job. |  |

#### Option 2: Perform Billing Process (Individual Run)

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
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Execute Billing - Business Partner (FKKBIX_S) tile. | The Billing (Individual Creation) page is displayed. |  |
| 3 | Maintain Parameters | In the Billing (Individual Creation), make the following entries as below:Billing Process: Y001Billing Date: <the current date>Contract Account: <the required contract account> |  |  |
| 4 | Execute | Choose Execute. |  |  |
| 5 | Choose Billable Item and Create Billing Units | In the Choose Billable Items and Creation of Billing Units dialog, choose Save, until you see the dialog Billing Ended. | A dialog Billing Ended is displayed. |  |
| 6 | Check Billing Document | Choose Continue (Enter) to leave the dialog. |  |  |

### Display Billing Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can display the billing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Manage Billing Documents (F2250) tile. | The Manage Billing Documents page is displayed. |  |
| 3 | Maintain Parameters | In the Manage Billing Documents screen, make the following entries as below:Billing Document: <the billing document you want to display>. |  |  |
| 4 | Execute | Choose Go. |  |  |
| 5 | Display Billing Document | Choose the item searched out. | The billing document is displayed. |  |

### Perform Invoicing Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create invoice document based on the billing document you created at previous step. You can proceed with mass run or individual creation

|  |
| --- |
| Note If you enabled Clarification at 2BG-Convergent Invoicing: Invoicing creation for Usage and Service, please follow the Perform Invoicing Process of 2BG-Convergent Invoicing: Invoicing creation for Usage and Service to perform Billing.If the clarification case is created when perform invoicing, please follow the Clarify Clarification Case Relevant to Invoicing Document (Optional) of 2BG-Convergent Invoicing: Invoicing creation for Usage and Service to perform Billing |

#### Option 1: Perform Invoicing Process (Mass Run)

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
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Administrator (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Execute Invoicing - Mass Run (F3524) tile. | The Execute Invoicing (Mass Creation) page is displayed. |  |
| 3 | Create Application Job | Choose Create button to create a new application job. | The New Job: Invoicing (Mass Creation) page is displayed. |  |
| 4 | Select Template | Make the following entries as below:Job Template; Invoicing (Mass Creation)Job Name; <job name>Choose Step2. |  |  |
| 5 | Maintain Schedule Options | Make the following entries as below:Start Immediately: chooseRecurrence Pattern: Single RunChoose Step3. |  |  |
| 6 | Maintain Parameters | Make the following entries as below:Prefix of Run ID: <Prefix of Run ID>Invoicing Process: Y1Business Partner: <the required business partner>Contract Account: <the required contract account>Simulation Run: <don’t choose>Document Date: <the current date>Posting Date: <the current date>Problem Class: <problem class> |  |  |
| 7 | Execute | Choose Schedule. | The job is running immediately. |  |
| 8 | Locate the job from application job list | In the Execute Invoicing (Mass Creation) screen, make the following entries as below:Date From-To: <Today -1/+1 day>Choose Go button. |  |  |
| 9 | Check Log | Choose Image of Log to locate the application job log. | The log of application job is displayed. From the log, you can see the result of application job. |  |

#### Option 2: Perform Invoicing Process (Individual Run)

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
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Execute Invoicing - Business Partner (FKKINV_S) tile. | The Invoicing (Individual Creation) page is displayed. |  |
| 3 | Maintain Parameters | In the Invoicing (Individual Creation), make the following entries as below:Invoicing Process: Y1Document Date: <the current date>Posting Date: <the current date>Business Partner: <the required business partner>Contract Account: <the required contract account> |  |  |
| 4 | Execute | Choose Execute. | A dialog Selection of Source Documents is displayed. |  |
| 5 | Select Source Documents | On the Selection of Source Documents dialog, choose Save. | A dialog Creation of Invoicing Units is displayed if there are more than one source documents to be invoiced. You can choose All Together or All Individually, then click Save to continue. |  |
| 6 | Post Invoicing Document | In the Save invoicing document dialog choose Yes, until you see the dialog Invoicing Ended. If you choose Document, you can check thedocuments before posting. | A dialog Invoicing Ended is displayed.Invoicing document is posted. |  |
| 7 | Check Invoicing Document | Choose Continue (Enter) to leave the dialog. |  |  |

### Display Invoicing Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you display the created invoicing document

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Manage Invoicing Documents (F2048) tile. | The Manage Invoicing Documents page is displayed. |  |
| 3 | Maintain Parameters | In the Manage Invoicing Documents screen, make the following entries as below:Invoicing Document: <the invoicing document you want to display> |  |  |
| 4 | Execute | Choose Go. |  |  |
| 5 | Display Invoicing Document | Choose the Search Out Item. | The invoicing document is displayed. |  |

### Print Invoicing Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you print the invoicing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad with your user credentials as Administrator (Convergent Invoicing). | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Choose Print Correspondence (F3537). | The Print Correspondence screen displays. |  |
| 3 | Create Job | On the Print Correspondence screen, choose Create. | The New Job: FI-CA: Print Correspondence screen displays. |  |
| 4 | Select Template | Make the following entries as below:Job Template: <FI-CA: Print Correspondence>Job Name: <FI-CA: Print Correspondence>Choose Step 2. |  |  |
| 5 | Maintain Schedule Options | Make the following entries as below:Start Immediately: chooseRecurrence Pattern: Single RunChoose Step3. |  |  |
| 6 | Maintain Parameters | In the New Job: FI-CA: Print Correspondence screen, make the entries as below:Prefix of Run ID: <Prefix of Run ID>Business Partner: <Select Business Partner number>Contract Account: <Select Contract Account number>Company Code: <company code>Correspondence Type: 0042Print Queue Name: <Select Print Queue ID>Actual Print: Selected |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job displays. |  |
| 8 | Execute Job | Choose Schedule. | The Print Correspondence screen displays.One new application job is created with a status. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

You may first have completed the following processes and conditions before you start with the test steps:

| Process | Business Condition |
| --- | --- |
| 2AR- Contract Accounting – Master Data and Basic Functions | Must be run before the test script. The business partner and contract account must be created. |
| 2BG- Convergent Invoicing – Invoice Creation for Usage and Service | Must be run before the test script. The invoicing document must be created. |

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
> Flagged while digesting this document, not verified: Example approval threshold is inconsistent within the document: the BAdI sample code triggers the workflow when total amount is greater than 100, while the example workflow start condition is greater than or equal to 100 (differs at exactly 100).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[09-subscription-billing-and-contract-accounting/convergent-invoicing-recurring-and-one-off-items-2t3-ae-test-script-86]]
- related-to :: [[09-subscription-billing-and-contract-accounting/test-script-convergent-invoicing-invoice-creation-for-usage-and-servic]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2BE_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 41,027 chars in the whole document
