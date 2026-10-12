---
id: 03-financial-accounting-and-close/collections-and-dispute-management-bfc-ae-test-script-1264
title: Collections and Dispute Management (BFC_AE) Test Script (BFC_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for Collections and Dispute Management (BFC_AE): prerequisites, roles, Fiori apps and step-by-step test procedures."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/collections-and-dispute-management]
aliases: [BFC_S4CLD2608_BPD_EN_AE]
keywords: [Collections and Dispute Management, collections management, dispute management, dispute case creation, collection strategies, collection groups, dunning notices, dispute reporting, collections reporting, background jobs]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BFC_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1264
topic: 03-financial-accounting-and-close/collections-and-dispute-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Collections and Dispute Management (BFC_AE) Test Script (BFC_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BFC_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Collections and Dispute Management** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Collections and Dispute Management (BFC_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Collections and Dispute Management (BFC_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232861530)

[2 Prerequisites 4](#_Toc232861531)

[2.1 System Access 4](#_Toc232861532)

[2.2 Roles 4](#_Toc232861533)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232861534)

[2.4 Business Conditions 6](#_Toc232861535)

[3 Overview Table 8](#_Toc232861536)

[4 Test Procedures 11](#_Toc232861537)

[4.1 Maintain Business Partner 11](#_Toc232861538)

[4.1.1 Define Accounting Clerk 11](#_Toc232861539)

[4.1.2 Maintain Business Partner 12](#_Toc232861540)

[4.1.3 Manage Collections Master Data 14](#_Toc232861541)

[4.2 Organizational Structure 16](#_Toc232861542)

[4.2.1 Manage Collection Strategies 16](#_Toc232861543)

[4.2.2 Define Collection Groups 19](#_Toc232861544)

[4.2.3 Assign Collection Groups to Collection Segments 21](#_Toc232861545)

[4.3 Dispute Case Opening 22](#_Toc232861546)

[4.3.1 Create Dispute Case from Process Receivables 22](#_Toc232861547)

[4.3.2 Create Dispute from Underpayment with Reason 23](#_Toc232861548)

[4.3.3 Create Dispute by Automatic Dispute Creation Job (Optional) 25](#_Toc232861549)

[4.4 Dispute Case Management 27](#_Toc232861550)

[4.4.1 Assign Dispute Cases 27](#_Toc232861551)

[4.4.2 Process Dispute Case 28](#_Toc232861552)

[4.4.3 Send Correspondence 29](#_Toc232861553)

[4.4.4 Execute Correction Activities 30](#_Toc232861554)

[4.4.5 Start Receivables Collection 31](#_Toc232861555)

[4.5 Reporting Disputes 33](#_Toc232861556)

[4.5.1 Disputes 33](#_Toc232861557)

[4.5.2 Open Disputes 35](#_Toc232861558)

[4.5.3 Monitor Overdue Receivables in Dispute 37](#_Toc232861559)

[4.5.4 Monitor Solved Disputes 38](#_Toc232861560)

[4.5.5 Monitor Created Versus Solved Disputes 39](#_Toc232861561)

[4.5.6 Monitor Processing Days of Open Disputes 40](#_Toc232861562)

[4.6 Collections Management 42](#_Toc232861563)

[4.6.1 Call Worklist 42](#_Toc232861564)

[4.6.2 Manage Collection Contacts 44](#_Toc232861565)

[4.6.3 Create Promise to Pay 45](#_Toc232861566)

[4.6.4 Create Resubmission 47](#_Toc232861567)

[4.6.5 Create Dispute Case 48](#_Toc232861568)

[4.6.6 Prepare Customer Contact 49](#_Toc232861569)

[4.6.7 Send Correspondence 51](#_Toc232861570)

[4.6.8 Create Dunning Notice 52](#_Toc232861571)

[4.7 Reporting Collections 53](#_Toc232861572)

[4.7.1 Collections Management Reporting 53](#_Toc232861573)

[4.7.2 Collection Progress 55](#_Toc232861574)

[4.7.3 Promises to Pay 56](#_Toc232861575)

[4.7.4 Display Dunning History 57](#_Toc232861576)

[4.7.5 Supervise Collections Worklist 58](#_Toc232861577)

[4.7.6 Cash Collection Tracker 59](#_Toc232861578)

[4.8 Schedule Background Jobs (Optional) 60](#_Toc232861579)

[4.8.1 Schedule Background Job to Create Dispute Cases Automatically (Optional) 60](#_Toc232861580)

[4.8.2 Schedule Background Jobs to Write Off Dispute Cases Automatically 61](#_Toc232861581)

[4.8.3 Schedule Background Job to Assign a Collection Profile (Optional) 62](#_Toc232861582)

[4.8.4 Schedule Background Job to Change Segment Data (Optional) 64](#_Toc232861583)

[4.8.5 Schedule Background Job for Assigning/Replacing a Collection Specialist (Optional) 66](#_Toc232861584)

[4.8.6 Schedule Background Job to Delete Transactional Data in Collections Management (Optional) 68](#_Toc232861585)

## Purpose

Overview

This scope item helps you to streamline debt collection processes, resolve customer invoice disputes, and manage overdue receivables. You can also reduce your exposure to the risks and costs of bad debt.

Dispute management provides dispute managers with tools to process disputes centrally and protect customer relationships. They can effectively manage disputes by using dispute resolution tools, dunning integration, and workflow integration.

Collection specialists can proactively manage and collect overdue receivables by using receivables collections tools and dunning integration. The specialists have all the information and support they need to collect payments faster and provide improved customer service. They can identify bad debt risk potential and take preventative steps to reduce further exposure.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

To execute Collections Management steps:

- Customer Master Data exists.
- Invoices have been created and posted to accounting.
- A specialist has been assigned to a collection group.
- A collection profile and a collection specialist have been assigned to a customer.
- Sending of FI-AR-Relevant Data to Collection Management has been executed.
- A worklist has been created.

|  |
| --- |
| Note A worklist created is the last step executed by the Collections Management. |

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
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Accounts Receivable Manager | SAP_BR_AR_MANAGER | Accounts Receivable | SAP_BR_AR_MANAGER |  |
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices Package, you can use the following Package scenario data:

Accounting

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Controlling Area | A000 |  |  |
| Customer | S331002513310000133100002 |  |  |
| House Bank | AEBK1AEBK2 |  |  |
| Bank GL Account | 6100700011002000 |  |  |
| Cost Center | 33101101 |  |  |
| Dunning Procedure | 1001 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNM | Create Cost Center and Cost Center Group - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BD9 - Sell from Stock | Run before this test script. Invoices are created and posted to accounting. Instructions how to cancel a billing document are included. |
| J14 - Sales Order Processing – Project-Based Services | Must be run before this test script. Invoices have been created and posted to accounting. |
| J59 - Accounts Receivable | Posting accounting data for customers in Accounts Receivable. |
| J78 - Advanced Cash Operations | Execute to upload bank statements. |

You can optionally configure the following functionalities to test this scope item.

Integration to Other Applications

| Functionality | Application Name | Details |
| --- | --- | --- |
| Bank connectivity | Financial Services Network | Must send payment instructions to the bank and receive bank statements from the bank. |
| Load electronic bank statements |  | Bank statements should be loaded into Financials automatically through a standard interface to banks. Customers should not be requested to set up the interface to the banks first.They should be able to adjust the reconciliation rules for the bank statement, but the interface should be part of the service that is available with the Public Cloud solution. |

## Overview Table

This scope item consists of several process steps provided in the following tables.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 2: Maintain Business Partner

| Process Step, Report or Item | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Define Accounting Clerk](#unique_8) [page ] 11 | Accounts Receivable Manager | Define Accounting Clerks (S_ALR_87003335) | Accounting Clerk created |
| [Maintain Business Partner](#unique_9) [page ] 12 | Accounts Receivable Accountant | Maintain Business Partner (BP) | Collections management is added to the business partner. |
| [Manage Collections Master Data](#unique_10) [page ] 14 | Accounts Receivable Manager | Manage Collections Master Data (F5400) | You updated collections master data for the business partner. |

Table 3: Organizational Structure

| Process Step, Report or Item | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Manage Collection Strategies](#unique_11) [page ] 16 | Accounts Receivable Manager | Manage Collection Strategies (F2946) | A collection strategy is added. |
| [Define Collection Groups](#unique_12) [page ] 19 | Accounts Receivable Manager | Manage Collection Groups (UDM_GROUP) | Specialists assigned to Groups. |
| [Assign Collection Groups to Collection Segments](#unique_13) [page ] 21 | Accounts Receivable Manager | Assign Collection Groups to Segments (UDM_GROUP2SGMT) | Groups assigned to Segments. |

Table 4: Dispute Case Opening

| Process Step, Report or Item | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create Dispute Case from Process Receivables](#unique_14) [page ] 22 | Accounts Receivable Accountant | Process Receivables (F0106A) | Dispute Case created manually. |
| [Create Dispute from Underpayment with Reason](#unique_15) [page ] 23 | Cash Management Specialist | Reprocess Bank Statement Items (F1520) | Dispute Case created manually. |
| [Create Dispute by Automatic Dispute Creation Job (Optional)](#unique_16) [page ] 25 | Accounts Receivable Accountant | Schedule Dispute Management Jobs (F3578) | Dispute Case items created. |

Table 5: Dispute Case Management

| Process Step, Report or Item | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Assign Dispute Cases](#unique_17) [page ] 27 | Accounts Receivable Accountant | Manage Dispute Cases - As Coordinator (F0702A) | The dispute case is assigned. |
| [Process Dispute Case](#unique_18) [page ] 28 | Accounts Receivable Accountant | Manage Dispute Cases - As Coordinator (F0702A) | The dispute case is processed. |
| [Send Correspondence](#unique_19) [page ] 29 | Accounts Receivable Accountant | Manage Dispute Cases - As Coordinator (F0702A) | An email is sent to the customer. |
| [Execute Correction Activities](#unique_20) [page ] 30 | Accounts Receivable Accountant | Manage Dispute Cases - As Coordinator (F0702A) | The dispute case is accepted and a credit memo is issued to customer. |
| [Start Receivables Collection](#unique_21) [page ] 31 | Accounts Receivable Accountant | Manage Dispute Cases - As Coordinator (F0702A) | The dispute case is forwarded to collections management. |

Table 6: Reporting Disputes

| Process Step, Report or Item | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Disputes](#unique_22) [page ] 33 | Accounts Receivable Manager | Dispute Management Reporting - Open Today (F4370) | You monitored disputes in different categories. |
| [Open Disputes](#unique_23) [page ] 35 | Accounts Receivable Manager | Open Disputes - Today (F1752) | Open Disputes is displayed. |
| [Monitor Overdue Receivables in Dispute](#unique_24) [page ] 37 | Accounts Receivable Manager | Overdue Receivables - In Dispute (F2540) | Monitors Disputes in Receivables. |
| [Monitor Solved Disputes](#unique_25) [page ] 38 | Accounts Receivable Manager | Solved Disputes - Last 12 Months (F2521) | Monitors Solved Disputes. |
| [Monitor Created Versus Solved Disputes](#unique_26) [page ] 39 | Accounts Receivable Manager | New Versus Solved Disputes - Today (F2523) | Monitors Created/Solved Disputes. |
| [Monitor Processing Days of Open Disputes](#unique_27) [page ] 40 | Accounts Receivable Manager | Processing Days of Open Disputes - Average Today (F2522) | Monitors Processing Days of Open Disputes. |

Table 7: Collections Management

| Process Step, Report or Item | Business Role | Transaction/App Name | Expected Result |
| --- | --- | --- | --- |
| [Call Worklist](#unique_28) [page ] 42 | Accounts Receivable Accountant | Process Collections Worklist (F0380) | Worklist is called. |
| [Manage Collection Contacts](#unique_29) [page ] 44 | Accounts Receivable Accountant | Process Receivables (F0106A) | Customer contact is prepared. |
| [Create Promise to Pay](#unique_30) [page ] 45 | Accounts Receivable Accountant | Process Receivables (F0106A) | Promise-to-Pay is created. |
| [Create Resubmission](#unique_31) [page ] 47 | Accounts Receivable Accountant | Process Receivables (F0106A) | Resubmission is created. |
| [Create Dispute Case](#unique_32) [page ] 48 | Accounts Receivable Accountant | Process Receivables (F0106A) | Creates a dispute case out of SAP Collections Management. |
| [Prepare Customer Contact](#unique_33) [page ] 49 | Accounts Receivable Accountant | Process Receivables (F0106A) | Customer Contact is documented. |
| [Send Correspondence](#unique_34) [page ] 51 | Accounts Receivable Accountant | Process Receivables (F0106A) | Correspondence is sent. |
| [Create Dunning Notice](#unique_35) [page ] 52 | Accounts Receivable Accountant | My Dunning Proposals (F2435) | Dunning notice is compiled, updated and printed. |

Table 8: Reporting Collections

| Process Step, Report or Item | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Collections Management Reporting](#unique_36) [page ] 53 | Accounts Receivable Manager | Collections Management Reporting - Collection Progress (F4495) | The collection progress and promise to pay are displayed. |
| [Collection Progress](#unique_37) [page ] 55 | Accounts Receivable Manager | Collection Progress - Current Run (F1738) | Collection Progress is displayed. |
| [Promises to Pay](#unique_38) [page ] 56 | Accounts Receivable Manager | Promise To Pay - Today (F1753) | Promised to Pay is displayed. |
| [Display Dunning History](#unique_39) [page ] 57 | Accounts Receivable Accountant | Display Dunning History (F2328) | Dunning History is displayed. |
| [Supervise Collections Worklist](#unique_40) [page ] 58 | Accounts Receivable Manager | Supervise Collections Worklist (F2375) | Collection Worklist is reviewed. |
| [Cash Collection Tracker](#unique_41) [page ] 59 | Accounts Receivable Manager | Cash Collection Tracker - Collections Management (F3182) | Cash Collection Tracker is displayed. |

Table 9: Scheduling Background Jobs (Optional)

| Process Step, Report or Item | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Schedule Background Job to Create Dispute Cases Automatically (Optional)](#unique_42) [page ] 60 | Accounts Receivable Accountant | Schedule Dispute Management Jobs (F3578) | You scheduled a background job to automatically create dispute cases. |
| [Schedule Background Jobs to Write Off Dispute Cases Automatically](#unique_43) [page ] 61 | Accounts Receivable Accountant | Schedule Dispute Management Jobs (F3578) | You scheduled a background job to automatically write off dispute cases. |
| [Schedule Background Job to Assign a Collection Profile (Optional)](#unique_44) [page ] 62 | Accounts Receivable Accountant | Schedule Collections Management Jobs - Mass Changes (F3918) | Collection Profile assigned. |
| [Schedule Background Job to Change Segment Data (Optional)](#unique_45) [page ] 64 | Accounts Receivable Accountant | Schedule Collections Management Jobs - Mass Changes (F3918) | Segment data changed. |
| [Schedule Background Job for Assigning/Replacing a Collection Specialist (Optional)](#unique_46) [page ] 66 | Accounts Receivable Accountant | Schedule Collections Management Jobs - Mass Changes (F3918) | Collection specialist updated. |
| [Schedule Background Job to Delete Transactional Data in Collections Management (Optional)](#unique_47) [page ] 68 | Accounts Receivable Accountant | Schedule Collections Management Jobs - Mass Changes (F3918) | The transactional data is deleted. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Maintain Business Partner

#### Define Accounting Clerk

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you add, change, or remove accounting clerks.

Add the user testing this script as an accounting clerk or define the Accounts Receivable Accountant as the accounting clerk. The user must be an accounting clerk to execute dunning notice creations.

Prerequisite

The user ID is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Define Accounting Clerks (S_ALR_87003335). | The Change View "Accounting Clerks": Overview view is displayed. |  |
| 3 | Add Clerk | Choose New Entries. | The New Entries: Overview of Added Entries view is displayed. |  |
| 4 | Enter Accounting Clerk Data | Make the following entries and choose Save:CoCd: 3310Clerk: 01 or Any 2 alphanumeric charactersName of Accounting Clerk: Any DescriptionOffice User: Your User ID or User ID of Accounts Receivable Accountant.Note To find a user, choose the icon in the field. On the Name of Office User dialog box, in the Search field, enter the name of user. Choose the row and the ID populates the Office User column. | An Entry created notification appears. The Define Accounting Clerk view is displayed. |  |
| 5 | Edit Clerk | Select the row of Clerk 01, Company Code xxxx (where xxxx is the number of company code to be tested) to change. | The accounting clerk details are displayed, with Edit buttons at the bottom of the view for editing, copying or deleting. |  |
| 6 | Edit | Choose Edit.Make the following entries and choose Save:Name: Any DescriptionUser ID: User IDof the Accounts Receivable Accountant role.To find a user, choose the icon in the field. On the Name of Office User dialog box, in the Search field, enter the name of user to display results. Choose the row and the ID populates the Office User column. Choose the row and the user ID populates the Details view. | An Entry created notification appears. The Define Accounting Clerk view is displayed.The accounting clerk is saved. |  |

#### Maintain Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To execute the Collections Management procedures, you must first assign the Collection Profile to the Business Partner Collections Management role. The Collection Profile is used to derive the priority of the customer open receivables in the process collection worklist.

In this activity, you assign the Collection Profile to a Business Partner that isn't assigned yet. You also assign accounting and dunning clerks to the Business Partner to enable dunning notice processing.

Prerequisite

The customer master record is created.

The accounting clerk is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). |  |  |
| 3 | Select Customer | Enter or verify the following:Find: Business PartnerBy: Customer NumberEnter the following data:Customer Number: For example, 33100001and choose Enter.Double-click the row of the Business Partner to open the details view. | The Display Organization: 33100001 view is displayed. |  |
| 4 | Change Role | To change the BP Role, make the following selection:Display in BP role: Customer (Fin.Accounting)(defined) | The Display Organization: 33100001, role Customer (Fin.Accounting) view is displayed. |  |
| 5 | Edit | Choose the Switch between Display and Change button to change the data to update.The Customer Master Data can now be edited. | The Change Organization: 33100001, role Customer (Fin.Accounting) view is displayed. |  |
| 6 | Company Code data | Choose Company Code. Choose the Customer: Correspondence tab. |  |  |
| 7 | Accounting Clerk | In the Correspondence section, make the following entries:Accounting Clerk: 01Note The person testing the script (Tester) is an accounting clerk. For testing, we recommend assigning the account receivable accountant as the accounting clerk). | Accounting clerk is changed. |  |
| 8 | Dunning | In the Dunning Data section, make the following entries:Dunning Procedure: 1001Dunning Block: Not blockedDunning Clerk: 01Note The person testing the script (Tester) is the dunning clerk. For testing, we recommend assigning the account receivable accountant as the dunning clerk. | Dunning Procedure is assigned. |  |
| 9 | Save | Choose Save. |  |  |
| 10 | Navigation | Change the Display in BP Role to Collections Management.Choose the Collection Profile tab and verify the value:Collection Prof.: YT_PRF_01To add or modify that value, choose the Switch Between Display and Change to enable editing.Enter YT_PRF_01 in the Collection Prof. field and choose Save from the bottom of the view.To change or display other master data settings, change the BP role, and navigate through the available tabs.Different setting display according to the chosen BP role. Edit to your requirements. |  |  |
| 11 | Save | Choose the Save button after completing your changes. | The changes to Customer Master Data are saved. |  |

#### Manage Collections Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you add or change business partner parameters related to collections management.

Prerequisite

The customer master record is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Collections Master Data (F5400). |  |  |
| 3 | Select Customer | Make the following entries and choose Go:Business Partner: <business partner>, for example, S33100251 | The business partner is displayed in the Business Partner pane. |  |
| 4 | Details | For the business partner, choose Details (>). | The Collections Master Data view is displayed. |  |
| 5 | Collection Profile | Choose the Change Collection Profile button. | The Change Collection Profile dialog box is displayed. |  |
| 6 | Collection Profile Data | In the Collection Profile field, select a collection profile and choose Change Collection Profile. | The collection segment belonging to the collection profile is automatically assigned. The collection group is displayed with default values.The Collections Master Data view is displayed. |  |
| 7 | Edit | Choose Edit. | Details for the collection segment are displayed. |  |
| 8 | Collection Group | If you want to change the collection group, select another collection group in the Collection Group field. | The collection group is updated. |  |
| 9 | Collection Specialist | Assign a collection specialist in the Specialist field. | The collection specialist is assigned. |  |
| 10 | Save | Choose Save. | The changes to the customer collection master data are saved. |  |

### Organizational Structure

#### Manage Collection Strategies

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a collection strategy in addition to the existing collection strategies used in SAP Collections and Dispute Management. You select collection rules and additional parameters to the collection strategies.

Collection strategies are used to:

- Prioritize business partners on the worklist
- Define the currency of amounts to be displayed in the worklist
- Determine the time intervals with which the business partner payables are to be sorted
- Define the type of integration with dunning in Accounts Receivable Accounting
- Determine the influence of the terms of payment on Collections Management (proactive receivables processing)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Collection Strategies (F2946).Note By choosing Go, a list of Collections Strategies that exist in the system display in the view. Use the filter at the top of the view to restrict which Collections Strategies display. | The Manage Collection Strategies (F2946) view is displayed |  |
| 3 | Create Collections Strategy - Initial | Choose Create. | The Unnamed Collection Strategy view is displayed |  |
| 4 | Create Collections Strategy - Header | Make the following entries and choose Create:Collection Strategy: <any strategy name>, for example, YT_ST#### (#### is the company code number)Collection Strategy Name: <description of collection strategy>Strategy Currency: AEDMaximum Valuation: 0 (so far) | The Collections Strategy is created with Inactive status and the details view displays the Collection Strategy you created. |  |
| 5 | Modify Newly Created Collections Strategy - Collections Rules | At the top right of the details view, choose Edit.In the Collection Rules section, choose Add Rule. | The Add Rule dialog box is displayed. |  |
| 6 | Add Rule | Make the following entries and choose Add Rule:Collection Rule <existing collection rule>, for example, CR00000002Valuation: <number>, for example, 15 | A CR0000002 details column is displayed. |  |
| 7 | Modify New Rule - Choose Conditions | In the CR00000002 details column, choose Conditions.Make the following entries and choose Apply:Item Total: Use condition Greater than with a value of 1500Days Overdue: 5 (Use the defaulted Included and Equals conditions) | Collection rule conditions applied. |  |
| 8 | Save | In the Collection Strategy column, choose Create. | The system displays an Object Saved notification and the Collections Rule is updated in the Collections Strategy details view. |  |
| 9 | Add Another Condition Rule | Repeat steps 5 through 8 using the following values for the entries:Collection Rule: CR00000003Valuation: Any number, for example, 10When the new rule details column appears, add the following values for Conditions:Item Amount: Select Greater Than and enter 5000Days Overdue: 5 (use the defaulted Included and Equals conditions).After you choose Apply and Save, continue to the next step. |  |  |
| 10 | Add Another Condition Rule | Repeat steps 5 through 8 using the following values for the entries:Collection Rule CR00000013Valuation: 10When the new rule details column appears, add the following values for Conditions:Total Promised: Select Greater Than and enter 500Promise Level: Select Equals and leave the field <blank>After you choose Apply and Save, continue to the next step. |  |  |
| 11 | Add Another Condition Rule | Repeat steps 5 through 8 using the following values for the entries:Collection Rule: CR00000019Valuation: 5When the new rule details column appears, add the following values for Conditions:Contact Type: <leave blank>Days Since Last Contact: 10 (use the defaulted Included and Equals values)Choose Apply and then choose Save to save your strategy. | The additional collection rules are updated in the Collections Strategy |  |
| 12 | Modify Newly Created Collections Strategy - Aging Periods | On the right side of the Manage Collections Strategies view, choose the Aging Periods tab.The following default data can be modified, if required, by using “-“ and “+” buttons. Or you can enter a number for the days in the field :Overdue Period 1: 1 To 30 DaysOverdue Period 2: 31 To 60 DaysOverdue Period 3: 61 To 90 DaysOverdue Period 4: 91 DaysDue Date Period 1: 0 To 30 DaysDue Date Period 2: 31 To 60 DaysDue Date Period 3: 61 To 90 Days | Aging Periods are maintained in the Collections Strategy. |  |
| 13 | Save Newly Created Collections Strategy | Choose Save. | The newly created Collections Strategy saves. |  |
| 14 | Collection Strategy - Show Assignment (optional) | On the top right of the view, choose Show Assignment. | Change View "Define Groups and Assign Strategy": Overview is displayed |  |
| 15 | Review Collection Strategy - Show Assignment (optional) | Verify that the new strategy isn't yet assigned to any of the groups. No action on your part is required.Choose Cancel to exit the view.Note The strategy is assigned to a group in the following Define Collection Groups procedure. Once the strategy is assigned to a group displays as Active. |  |  |

#### Define Collection Groups

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you add, change, or remove collection groups.

In this procedure, you define the groups of collection specialists that can contact customers in SAP Collections Management. You assign collection specialists to each group using their usernames. Each collection specialist can add a temporary substitute (for example, to be assigned during vacation or sick leave of the collection specialist). When the specialist is absent, the system assigns the worklist items to the temporary substitute.

All specialists in a collection group collect open receivables from business partners with the same strategy. Assign a collection strategy to each group.

Prerequisite

User ID is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Collection Groups (UDM_GROUP). | The Change View "Define Groups and Assign Strategy": Overview view is displayed. |  |
| 3 | Define Group and Assign Strategy | Note If the Display View... appears rather than the Change View.., choose Edit to switch the view.Choose New Entries at the top left of the view. | View New Entries: Overview of Added Entries is displayed. |  |
| 4 | Enter Group and Strategy Data | Make the following entries:Group: Any group name, for example, YT_GR####, where #### is the company code number)Group Name: <Any Description>Strategy: <Strategy>, the name of the strategy you created in the previous Manage Collection Strategies procedure. |  |  |
| 5 | Save | Choose Save. | A new Collection Group is created. |  |
| 6 | Assign Processor to Collection Group | Choose the checkbox of the row of a new group you just created.From the Dialog Structure column, double-click the Assign Processor to Collection Group. | View Cluster Editing: Initial Screen is displayed. |  |
| 7 | Edit | Choose New Entries and make the following entries:Specialist: <User ID> of an accounting clerk with the role of Accounts Receivable Accountant.Note As you enter an ID, search results appear in a User Name table by logon names. Select the row of the name to add it to Specialist field. | A specialist is added. |  |
| 8 | Assign Processor to Collection Group | Repeat steps 6 and 7 for the YT_GR01 collection group and assign the same user ID.Note In this scenario, as there was no direct assignment of a collection specialist in the Business Partner master data (from the previous Complete Customer Master Data procedure). The Collections Management Collections Worklist Items of this Business Partner is added to the pool of worklist items, which is then equally distributed among all members of the Collection Group assigned by the Collection Strategy.Remember In this scenario for the following procedure, YT_ST_01 is used for Collection Strategy and YT_GR01 is used for Collection Group. |  |  |
| 8 | Save | Choose Save. | The specialist is assigned as a Processor to the new Collection Group. |  |

#### Assign Collection Groups to Collection Segments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define the contact groups that can contact business partners in the respective collection segments.

You designate one group as the default group. The system then proposes the default group for related segments when you enter a profile in the business partner master record. Defining contact groups ensures that - in each segment - a group of collection specialists is responsible for the customer.

Prerequisite

The Collection Segment is created.

The Collection Group is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. | . |  |
| 2 | Access the SAP Fiori app | Open Assign Collection Groups to Segments (UDM_GROUP2SGMT). | The Change View "List of Collection Segments": Overview view is displayed. |  |
| 3 | Assign Collection Group to Segments | Choose the checkbox of the row for the YT_SEGMT01 segment. From the Dialog Structure column, double-click Assign Collection Group to Segments. | The Change View "Assign Collection Groups to Segment": Overview view is displayed. |  |
| 4 | Edit | Choose New Entries.Make the following entries:Group: <Group name> you created in the previous procedure. (For example, YT_GR####, where #### is the company code number).Default Group: Deselected |  |  |
| 5 | Save | Choose Save after completing your changes. | Assignment of the Collection Group to a Segment is complete. |  |

### Dispute Case Opening

#### Create Dispute Case from Process Receivables

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a dispute case and add an invoice as a customer-disputed object.

Prerequisite

An open Financial Accounting (FI) customer invoice exists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Process Receivables (F0106A). |  |  |
| 3 | Select | Make the following entries and choose Go:Search: *Select the desired business partner from the list by choosing Details (>) for that row:Business Partner: For example, S33100251 | The business partner details are displayed. |  |
| 4 | Select Invoice | To create a dispute case, select the checkbox in the first column of the appropriate invoice row. | The Create Dispute Case button is enabled. |  |
| 5 | Create Dispute | Choose Create Dispute Case. | The Create Dispute Case dialog box displays. |  |
| 6 | Enter Dispute Data | Make the following entries:Case Title: <enter a meaningful title>Reason: Select a reason from the dropdown list, for example, Price DifferencesPriority: Select a priority from the dropdown list, for example, HighProcessor: <User ID>Contact Person: <contact>Notes: <any>Attachment: Optional | The Manage Dispute Cases - As Coordinator (F0702A) app is linked. |  |
| 7 | Confirm Data | Choose Save. | A Dispute Created notification is displayed. |  |

#### Create Dispute from Underpayment with Reason

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a dispute case from different, manual FI-AR clearing transactions where an underpayment becomes visible (for example, a residual item).

|  |
| --- |
| Note For more information about uploading a bank statement, see the Basic Cash Operations (BFB) test script. |

Prerequisite

Open Financial Accounting (FI) items exist.

A bank statement item is uploaded that isn't automatically cleared with less amount (underpayment) of the invoice to be cleared.

|  |
| --- |
| Caution The Reprocess Bank Statement Items (F1520) app isn't assigned to the Cash Management Specialist role by default. To use the app with that role (or another role of your choosing), you must update the role. To do so, log in as Administrator, access the Maintain Business Roles (F1492) app, and assign Dispute* related catalogs to the desired user/role. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Reprocess Bank Statement Items (F1520). | The Reprocess Bank Statement Items (F1520) view displays. |  |
| 3 | Search | Make the following entries and choose Go:Company Code: 3310House Bank: AEBK1House Bank Account: AEAC1 | Bank statement items of the filter criteria display. |  |
| 4 | Select Bank Statement Item | Select a row to process from the Bank Statement Item list and in the Reprocess column, choose the > arrow button. | A details view of the select bank statement displays. |  |
| 5 | Enter Details | In the Details section, verify or enter the following:Account type: Customer and <Customer number>Review the following fields:Posting Date: <Today’s date>Payment Amount: Enter an amount lower than the invoice to be paidJournal Entry Type: DZ | A list of invoices displays at the bottom half of the view in the Open Items section. |  |
| 6 | Clear Item | In the Open Items section, select the invoice to create a dispute case. The amount of the invoice must be larger than the amount paid. Choose Clear in the selected invoice. | The invoice transfers to Items to Be Cleared. The Balance amount on the header must be zero to post. |  |
| 7 | Reprocessing Reason | Verify that the amount in the Allocated amount column is equal to the bank statement item amount in the Details section. Ensure that the balance amount on the header is zero. |  |  |
| 8 | Enter Dispute Details | Choose Create Dispute and make the following entries:Title: <Any description>Reason: Select any reasonPriority: For example, MediumProcessor: <User ID of Cash Management Specialist or your User ID >Fill any other available fields, if required. Any required attachments can be uploaded.Choose OK. | The Dispute view displays and a dispute case is created. New options to Update Dispute and Remove Dispute become available. |  |
| 9 | Post | Choose Post. | The Success view displays, showing the journal entry number posted. The document created can be displayed. |  |

#### Create Dispute by Automatic Dispute Creation Job (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional activity, you create a dispute case using an automatic dispute case creation job.

Prerequisite

An open Financial Accounting (FI) customer invoice exists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Dispute Management Jobs (F3578). |  |  |
| 3 | Create New Job | On the right of the view, choose Create. | The New Job view is displayed. |  |
| 4 | Create New Job – Information and Parameters | Make the following entries and choose Step 2:Job Template: Automatic Creation of Dispute CasesNote Use the Search function to locate the template and choose Enter. | The Application Jobs view is displayed. The new job displays the In Process status. |  |
| 5 | Create New Job – Information and Parameters | Make the following entries and choose Step 3:Start Immediately: selected |  |  |
| 6 | Create New Job – Information and Parameters | Make the following entries and choose Schedule:Open Items: selectedTest Run: selectedNote The Test Run allows you to review items that are relevant for the dispute case creation. In productive use, these items would be transferred to the dispute case, though that isn't in scope of this test scenario.Company Code: 3310Posting Date: <date> For example, a day between a month ago and today (ensuring that the open items exist on that date) | When your job run completes, the status changes to Finished. |  |
| 7 | Review Job Log | Choose the document icon in the Results column.Note If a dialog box displays, choose Continue. | The Document view is displayed |  |
| 8 | Review Job Log - Details | Review the list. Verify that the recently created open items were chosen for dispute case creation and if any items were not chosen. |  |  |

### Dispute Case Management

#### Assign Dispute Cases

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you assign a dispute case to a processor. For example, the dispute case is unassigned or input is required from another person, you assign as processor, to resolve the dispute case.

Prerequisite

Dispute case exists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Dispute Cases - As Coordinator (F0702A). |  |  |
| 3 | Execute Query | Leave all fields blank. Choose Go. | A list of all disputed cases is displayed. Unassigned dispute cases have no entries in the Processor column. |  |
| 4 |  | Ensure that you are in the Open Dispute Cases tab.Select the row for a specific case and choose Details (>). | The case details are displayed. |  |
| 5 | Edit Case | Choose Edit. | You are now in Edit mode. |  |
| 6 | Change Processor | Make the following entry and choose Save:Processor: <user ID>Note If you are changing the processor and do not know the User ID, choose the help icon in the Processor field. A search dialog box displays, allowing you to search by name (Description) or User ID. Enter your search and choose Go. Select the checkbox next the correct result and choose OK. | The processor has been changed successfully notification displays and the dispute case is assigned. |  |
| 7 | Enter a Note | In the Notes section, add the following:Enter Note: <Enter a note> . for example explaining the assignment to the processor. |  |  |
| 8 | Save | At the bottom of the view, choose Save. | The dispute case updates and saves. |  |

#### Process Dispute Case

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, as a processor, you search for dispute cases that are assigned to you.

|  |
| --- |
| Note After investigating the dispute case, the next activity depends on the results of the investigation:Option A: If the customer complaint is justified and is accepted, continue with the following Close Dispute Case procedure.Option B: If the customer complaint isn't justified and the outstanding receivables must be collected, continue with the following Start Receivables Collection procedure. |

Prerequisite

A dispute case exists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Dispute Cases - As Coordinator (F0702A) | The Manage Dispute Cases (Version 2) (F0702A) view is displayed. |  |
| 3 | Select Processor | Make the following entries and choose Go:Processor: <your User ID> | The list of all dispute cases assigned to the selected Processor is displayed. |  |
| 4 | Select Case | Select the row of a specific case and choose the > arrow button to access details of the dispute case. | The new view is displayed with all the details of the case, which can be edited. |  |
| 5 | Enter Note | Enter a comment:Enter Note: <Enter a note>. |  |  |
| 6 | Enter Status | In the General Data section, make the following entries:Status: In Process |  |  |
| 7 | Return Dispute Case to Coordinator | In the Processor dialog box, make the following entries:Processor: <coordinator user ID>Note If you do not know the User ID for the coordinator, choose the help icon in the Processor field. A search dialog box displays, allowing you to search by name (Description) or User ID. Enter your search and choose Go. Select the checkbox next the correct result and choose OK. By entering the coordinator as the new processor, the dispute case is returned to the coordinator for investigation. | The system displays the message The processor has been changed successfully. The dispute case is transferred to the coordinator. |  |
| 8 | Save | From the bottom of the view, choose Save. | A Dispute case saved successfully notification displays and your entry is saved. |  |

#### Send Correspondence

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you send an email to an individual customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Dispute Cases - As Coordinator (F0702A). |  |  |
| 3 | Select Case | Select a Case ID row and choose Details (>). | The dispute case details are displayed. |  |
| 4 | Create Email | Choose E-mail. |  |  |
| 5 | Enter Details and Send Email | Enter the email details, then send your email. | The e-mail is successfully sent. |  |

#### Execute Correction Activities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After investigating the dispute case, you determine that the customer complaint is justified. In this activity the dispute case is marked as accepted and a credit memo (for the full invoice amount) is issued to the customer.

As soon as the invoice is cleared with the credit note, the case is automatically closed. No further steps in closing the dispute case are necessary.

However, if it is determined during processing that the case creation for this FI document line item was an error, you can execute correction activities. The steps required to void a dispute case are described below.

Prerequisite

A dispute case exists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Dispute Cases - As Coordinator (F0702A). | The Manage Dispute Cases (Version 2) (F0702A) view is displayed. |  |
| 3 | Execute Query | Leave all fields blank and choose Go. | The list of all dispute cases is displayed. Unassigned dispute cases have no entry in the Processor column. |  |
| 4 | Select Case | Ensure that you are on the Open Dispute Cases tab. Select the row of a specific case and choose Details (>) to access details of the dispute case. | The new view shows all case details. |  |
| 5 | Void Dispute Case | Choose Void Dispute Case. | The dispute case is closed. |  |
| 6 | Back | Choose the < back arrow button at top of the view to return to the initial view. |  |  |

#### Start Receivables Collection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After investigating a dispute case, you determine that the customer complaint isn't justified. Collection of the outstanding receivables uses (SAP Collections and Dispute Management, if implemented or) your company-specific collections process. In this activity the dispute case is marked as ready for the receivables collection.

Prerequisite

A dispute case exists.

A specialist is assigned to a collection group.

A collection profile and a collection specialist are assigned to a customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Dispute Cases - As Coordinator (F0702A). |  |  |
| 3 | Select Processor | Enter the following:Processor: <your User ID>and choose Go: | The list of all dispute cases assigned to the selected Processor is displayed. |  |
| 4 | Select Dispute Case | Select the row of a specific case and choose the > arrow button to access details of the dispute case. |  |  |
| 5 | Reject Dispute | In the General Data section, make the following entry.Status: Not justified |  |  |
| 6 | Save | Choose Save. | A Dispute case saved successfully notification appears.By changing the status into Not Justified, the dispute case is reclassified and forwarded to Collections Management. |  |

### Reporting Disputes

#### Disputes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this analytic activity, you monitor disputes in different categories, such as new, open and solved ones.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Dispute Management Reporting - Open Today (F4370). | The Disputes view directly displays information to existing dispute cases. |  |
| 3 | Open Disputes | Choose the Open Disputes tab. | The system displays existing open disputes. |  |
| 4 | Open Disputes | You can select any Dimension to change the view by:PriorityReasonCompany CodeCountryRegionCoordinatorStatusAdditionally you can set a filter:PriorityReasonCustomerCompany CodeProcessorRegionCoordinatorStatusYou can also change the currency. |  |  |
| 5 | Processing Days | Choose the Processing Days tab. | The system displays info regarding processing days. |  |
| 6 | Processing Days | You can set a filter:PriorityReasonCustomerCompany CodeProcessorCoordinatorStatusYou can also change the currency. |  |  |
| 7 | New and Solved | Choose the New and Solved tab. | The system displays info regarding new and solved disputes. |  |
| 8 | New and Solved | You can select any Dimension to change the view by:PriorityReasonRoot CauseCompany CodeProcessorCoordinatorStatusAdditionally you can set a filter:PriorityReasonRoot Cause CodeCustomerCompany CodeProcessorCoordinatorStatusYou can also change the currency |  |  |
| 9 | Solved Disputes | Choose the Solved Disputes tab. | The system displays info regarding solved disputes. |  |
| 10 | Solved Disputes | You can select any Dimension to change the view by:PriorityReasonRoot CauseCompany CodeProcessorCoordinatorStatusAdditionally you can set a filter:PriorityReasonRoot Cause CodeCustomerCompany CodeProcessorCoordinatorYou can also change the currency. |  |  |

#### Open Disputes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you monitor open disputes.

Prerequisite

Dispute Cases exist that are not closed, not confirmed, and not voided, deleted, or canceled.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Open Disputes - Today (F1752). |  |  |
| 3 | Explore and Review | Overdue Disputes displays a chart or table. To change the view or the parameters of the view, choose from the available options to filter the report.You can filter the open disputes by:Company CodeReasonAnd so on.Note The Case ID field may be shown twice in the filter list. If this occurs, you can choose either of them, as they are functionally identical.Choose the Reset Filters icon to the right of the view to return to default.Use the dropdown menu to filter:By ProcessorBy Customer (Top 10 Disputed Amounts)By Dispute ReasonBy Dispute Case (Top 200 Disputed Amount)Additional buttons allow you to change the chart type, toggle between chart and tabular view, and so on. |  |  |

#### Monitor Overdue Receivables in Dispute

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you monitor overdue receivables in dispute.

Prerequisite

Dispute Cases exist that are not closed, not confirmed, and not voided, deleted, or canceled.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Overdue Receivables - In Dispute (F2540). | The Overdue Receivables in Dispute (F2540) view is displayed. |  |
| 3 | Explore and Review | The view is displayed a chart or table. To change the view or the parameters of the view, choose from the available options to filter the report.You can filter the open disputes by:ReasonCompany codeCountry KeyProcessorCustomerChoose the Reset Filters icon to the right of the view to return to default.Use the dropdown menu to filter:By Company CodeBy Country KeyBy CustomerBy ReasonBy ProcessorBy Person ResponsibleBy Root CauseBy CoordinatorBy Due PeriodAdditional buttons allow you to change the chart type, toggle between chart and tabular view, and so on. |  |  |

#### Monitor Solved Disputes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the amounts and numbers of solved disputes over a selected time range. On the Solved Disputes - Last 12 Months (F2521) app, the amount solved in the last 12 months is displayed in currency. The different filtering options display the following information (chart and table) by processor or coordinator:

- Number of solved disputes in current month or last month or current year or last 12 months
- The average resolution time of these disputes within the defined time frame

Additional filters are added to show the top 10 solved amounts by customer in the last 12 months and in the current year. Filtering can be done, for example, by reason, company code, customer, processor, coordinator.

Prerequisite

Closed and confirmed Dispute Cases exist.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Solved Disputes - Last 12 Months (F2521). | The Solved Disputes (F2521) view is displayed. |  |
| 3 | Explore and Review | To change the view, choose the drill-down button or other buttons in the report.You can view the Solved Disputes in different periods according to:ReasonCompany codeRoot Cause CodeYou can view the Solved Disputes in a chart or a table, and you can drill-down by:Processor (Average Resolution Current Months)Processor (Average Resolution Last Months)Customer (Top 10 Solved Amount Last 12 Months)Customer (Top 10 Solved Amount Current Year)Additional buttons allow you to change the chart type, toggle between chart and tabular view, and so on. |  |  |

#### Monitor Created Versus Solved Disputes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the amounts and numbers of new, open, and solved disputes over a selected time range. For your convenience, the number of new disputes minus the number of solved disputes of today displays on New Versus Solved Disputes - Today (F2523) app. The initial view is displayed a chart of new disputes, sorted by status. Additional filtering options are available to display the a chart and table based on your criteria.

Prerequisite

Created and Solved Dispute Cases exist.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open New Versus Solved Disputes - Today (F2523). |  |  |
| 3 | Explore and Review | To change the view, choose the drill-down button or other buttons in the report.You can filter the view of the Created Versus Solved Disputes according to:StatusReasonCompany codeProcessorRoot Cause CodeCustomerCoordinatorYou can drill-down by:StatusProcessorCustomerDispute CaseAdditional buttons allow you to change the chart type, toggle between chart and tabular view, and so on. | Views of chosen criteria are displayed. |  |

#### Monitor Processing Days of Open Disputes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

In this activity, you review dispute cases that are not closed, confirmed, voided, deleted, or canceled.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Processing Days of Open Disputes - Average Today (F2522). | The Processing Days of Open Disputes (F2522) view is displayed. |  |
| 3 | Explore and Review | The view is displayed a chart or table. To change the view or the parameters of the view, choose from the available options to filter the report.A set of buttons at the top of the view allow you to filter the chart or a table by :StatusReasonCompany codeProcessorRoot Cause CodeCustomerCoordinatorChoose the Reset Filters button to the right of the view to return to default.Change the view by using the drill-down menu, providing additional filtering options:In Days (Amount and Number)By CoordinatorBy CustomerBy StatusBy Dispute Case (as either chart or table)Additional buttons allow you to change the chart type, toggle between chart and tabular view, and so on. |  |  |

### Collections Management

#### Call Worklist

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you call the worklist in your role as collection specialist. Your worklist is automatically created by reviewing the customer situation against the rules in the assigned collection strategy. The worklist for each collection specialist contains an entry for all customers to be contacted. Customers are already prioritized according to the score assigned by the Collection Strategy. The worklist only displays for the user assigned as a Processor to a Collection Group from the Collection Segment of the customer master. Within the worklist, you have the ability for mass correspondence creation for multiple customers.

Prerequisite

Invoices are past due.

A specialist is assigned to a collection group. This assignment is completed using the Define Collections Group procedure.

A collection profile is assigned to a customer. The profile assignment was created in the previous, Complete Customer Master Data procedure.

The Sending of FI-AR-Relevant Data to Collection Management and worklist are executed as batch jobs: These daily batch jobs, schedule automatically and are monitored by the cloud operator to guarantee that the collections worklists regenerate every day.

A worklist is created.

The worklist creation is executed as a batch job. These daily batch jobs schedule automatically and are monitored by the cloud operator to guarantee that the collections worklists regenerate every day.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Process Collections Worklist (F0380). | A worklist with the customers to contact displays. |  |
| 3 | Select Customer | The My Open Items tab displays your open items by Customer Number. Double-click a customer number to process. For example:Customer Name: S33100251 | A dialog box with customer details displays with address,contact information, and activity links. |  |
| 4 | Actions | On the customer details dialog box, to take any of the following actions, choose the link for the options:Clear Incoming PaymentsDisplay Customer BalancesManage Customer Line ItemsPost Incoming PaymentsProcess ReceivablesSelecting an option opens a new view. After completing your review, return to My Open Items, use the Back button. | A new view is displayed with information related to the option selected. After completing your review, you return to the My Open Items view. |  |
| 5 | Other Worklists | To display worklists assigned to other users choose Assigned To Others. | The Select Specialist view is displayed. |  |
| 6 | Display Other Worklists | From the Select Specialist screen, choose a User ID. | The worklist of selected User ID displays. |  |
| 7 | Mass Correspondence Creation - Selection | From the Process Collections Worklist view, choose multiple customer names and select Create Correspondences. | Create Correspondences displays. |  |
| 8 | Mass Correspondence Creation - Parameters Setting | Choose a Correspondence Type, Document Date, Email Template and select Confirm.Note On the field, choose the right corner to display a dropdown menu of Correspondence Type and Email Template choices. | Correspondence Items List and Correspondence Item view is displayed. |  |
| 9 | Mass Correspondence Creation - Preview and Confirm | You may Preview the correspondence created in both areas of the Correspondence Items List and Correspondence Item and then select Confirm button at the bottom right of the Correspondence Items List view and then Confirm the message of mass email. | Correspondence is created. |  |
| 10 | Mass Correspondence Creation - Review Status Change | In the Process Collections Worklist view, the customers for whom you created correspondence move from the My Open Item tab to the My Completed Item tab. The Result of Customer Contact field has the Correspondence Sent value. | Review of status update is complete. |  |

#### Manage Collection Contacts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you prepare the Collection Contact.

Prerequisite

A worklist is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Process Receivables (F0106A) |  |  |
| 3 | Select | Make the following entries and choose Go:Search: * | A list of business partners is displayed. |  |
| 4 | Select Customer | Select the desired Business Partner row and choose Details (>):Business Partner: For example, S33100251 | The customer details view is displayed with a list of invoices showing outstanding amount for the invoice, total outstanding amount for all invoices, and other information. |  |
| 5 | Collection Contacts | Choose the Collection Contacts tab. |  |  |
| 6 | Create Contact | Choose Create. | The system opens the Manage Collection Contact Persons (F4708) app. |  |
| 7 | Edit Collection Contact Person (Optional) | Enter a Contact Person, Telephone, and Email address for the contact.Note When you select a Contact name using a name value already available in the system, the phone and email address automatically populate from the data associated with the name. If you enter a Contact name as free text, you must manually enter the phone and email data. | The customer contact data is updated. |  |
| 8 | Save | Choose Create. | The collections contact is updated and saved. |  |

#### Create Promise to Pay

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You create a promise to pay for open invoices when the customer promises to pay on the invoice. The created promise to pay records the amounts and date promised. The system automatically tracks and updates the state of the promise to pay as kept or broken using the integration between SAP Collections Management and SAP Accounts Receivable (SAP FI-AR). The state of the promise to pay is visible in the worklist that is then used for your collections strategy (for example, placing the customer on the worklist for a later date when the customer breaks their promise to pay).

Prerequisite

A worklist is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Process Receivables (F0106A). |  |  |
| 3 | Select | Make the following entries and choose Go:Search: * | A list of Business Partners display. |  |
| 4 | Select Customer | Select the desired Business Partner row and choose Details (>):Business Partner: For example, S33100251 | The customer details view is displayed with a list of invoices showing outstanding amount for the invoice, total outstanding amount for all invoices, and other information. |  |
| 5 | Select Invoice | Select an open invoice from the Invoices tab. | An invoice is selected. |  |
| 6 | Create Promise to Pay | Choose Create Promise to Pay. | The Manage Promises to Pay (F4710) app opens. |  |
| 7 | Enter Promise Data | Make the following entries and choose Save:Promised Amount: <Full amount of invoice is default amount>Promised For: <Date>Notes: OptionalAttachments: OptionalRestriction For each invoice, there's only one active promise to pay level. To change an existing promise to pay, open the invoice and update the information to create a new promise to pay. | A Promise to Pay Created notification displays.The State of Promise column displays Open status.The created promise to pay now appears in the Promises tab on the Process Receivables view. |  |
| 8 | Withdraw Promise | To cancel a promise to pay, choose the Promises to Pay tab.Select the invoice and choose Withdraw Promise to Pay. | The selected promise to pay has been withdrawn notification is displayed. |  |

#### Create Resubmission

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a resubmission. You, in the role of the collection specialist, create a resubmission to interrupt the automatically created worklist. By creating a resubmission, the customer is suppressed from the worklist until after the resubmission date is reached.

Prerequisite

A worklist is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Process Receivables (F0106A). |  |  |
| 3 | Select Customer | Select the desired Business Partner row and choose Details (>):Business Partner: For example, S33100251 | The customer details view is displayed with a list of invoices showing outstanding amount for the invoice, total outstanding amount for all invoices, and other information. |  |
| 4 | Select Invoice | Select an open invoice from the Invoices tab. | An invoice is selected. |  |
| 5 | Create Resubmission | Choose Create Resubmission. | The Manage Resubmissions (F4709) app displays. |  |
| 6 | Enter and Save Resubmission Data | Make the following entries and choose Save:Resubmission Date: <Actual Date + 2 days>Resubmission Reason: Select a reason from the dropdown list, for example, Contact Person Requests CallbackNotes: OptionalAttachment: Optional | A Resubmission Created notification is displayed.The resubmission for the customer is created.The created resubmission now displays on the Resubmissions tab on the Process Receivables view. |  |

#### Create Dispute Case

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a dispute case and add an invoice as a customer-disputed object.

Prerequisite

An open Financial Accounting (FI) customer invoice exists.

Procedure - SAP Fiori

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad an Accounts Receivable Accountant |  |  |
| 2 | Access the SAP Fiori App | Open Process Receivables (F0106A). |  |  |
| 3 | Search Customer | Make the following entries and choose Go:Search: * | A list of customers is displayed. |  |
| 4 | Select Customer | Select the desired business partner from the list and choose Details (>):Business Partner: For example, S33100251 | The business partner details are displayed. |  |
| 5 | Select Invoice and Create Dispute | To create a dispute case, select the checkbox for an invoice and choose Create Dispute. | The Create Dispute Case dialog box is displayed. |  |
| 6 | Enter Dispute Case Details and Confirm Data | Make the following entries and choose Save:Case Title: <Enter a meaningful title>Reason: reason, for example, Price DifferencePriority: priority, for example, HighProcessor: <User ID>Contact Person: <contact person>Notes: <Enter any additional notes>Attachment: <optional> | You are linked to the Manage Dispute Cases - As Coordinator (F0702A) app. |  |

#### Prepare Customer Contact

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity you document customer contact. When closing or saving the customer contact, as a Collection Specialist, you record a number of details to summarize the contact. Additionally, a default contact note is prepopulated with details of any promises-to-pay, resubmissions, and dispute cases created during the contact. You can add additional text into the note and then the text saves with the contact and is available in the Contact History tab.

Prerequisite

A worklist is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Process Receivables (F0106A). |  |  |
| 3 | Search Customer | Make the following entries and choose Go:Search: * | A list of business partners is displayed. |  |
| 4 | Select Customer | Select a business partner from the list and choose Details (>):Business Partner: For example, S33100251 | The customer details view is displayed with a list of invoices, showing outstanding amount for the invoice, total out-standing amount for all invoices, and other information. |  |
| 5 | Customer Views | Choose any of the following to view more information about the invoices and status:Invoices (default)Dispute CasesPromises to PayResubmissionsCollection Contacts | Different views are displayed, depending on your selection. |  |
| 6 | Edit Contact (Optional) | Choose Finish Customer Contact. | The Manage Customer Contacts (F4707) app is displayed. |  |
| 7 | Edit Contact (Optional) | Enter the Contact Person name, Telephone number, and Email address of the contact. Enter the Result of Contact.Note When you select a Contact name using a name value already available in the system, the phone and email address automatically populate from the data associated with the name. If you enter a Contact name as free text, you must manually enter the phone and email data. | The customer contact data is updated. |  |
| 8 | Save Contact (Optional) | If you do not want to send correspondence, choose Save. If you do, continue with the [Send Correspondence](#unique_34) [page ] 51 topic. | The customer contact is updated and saved. |  |

#### Send Correspondence

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you send an email out of process receivables.

Prerequisite

An open Financial Accounting (FI) customer invoice exists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Starting Point (Optional) | You are still in the app from the [Prepare Customer Contact](#unique_33) [page ] 49 step. |  |  |
| 2 | Email Preparation (Optional) | Choose Create Email. |  |  |
| 3 | Email Preparation(Optional) | Choose Show Email. |  |  |
| 5 | Email Preparation(Optional) | Choose Change Email Template.Select the Customer Contact Recap email template, select a Language Key (for example, English) and choose Change Email Template. | The email template is entered in the message text. |  |
| 6 | Finish Customer Contact | Choose Create. |  |  |
| 7 | Send Email (Optional) | Choose Send. | You sent an email to the customer. |  |

#### Create Dunning Notice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure describes the creation and scheduling of a dunning run, as well as printing dunning notices to customers.

This activity finds items to dun for all customers assigned to a dunning clerk, an accounting clerk, and a dunning procedure.

Two dunning procedures are provided:

- 1001 - Dunning notice every 14 days, 4 dunning levels
- 1002 - Dunning notice in conjunction, 30 days after the invoice is created.

Prerequisite

Maintain customer master data:

- Assign the dunning procedure and accounting clerk
- Maintain customer master data: assign the accounting clerk and dunning clerk (if different, Dunning Clerk has higher priority)

Invoices are past due and at least one invoice has no dispute case registered on it and no promise to pay.

Dunning block isn't set.

|  |
| --- |
| Note Invoices won't be processed in the dunning run if an open dispute case is registered or a promise to pay isn't broken. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open My Dunning Proposals (F2435) | A view is displayed with a list of all the dunning proposals. |  |
| 3 | Dunning | Choose the Create Dunning Proposal button from the bottom of the view and in the New Dunning Proposal dialog box that opens, choose Create. | Two notifications displays, the first that the dunning proposal is being created displays and the second notification confirms that the dunning is created. |  |
| 4 | Preview Notice | To preview the dunning notice, in the Preview Notice column, select the PDF button for that row.The dunning notice displays in a PDF format. Additional options to download, print, zoom, or set a dunning block are available.When you complete your review of the notice, choose Close at the bottom of the notice view. | The Dunning Notice displays. |  |
| 5 | Printing | Choose the checkbox of the row to print and choose the Send Dunning Notices option in the bottom of the view.A Send Dunning Notices dialog box opens, showing options to send the dunning notice via email or to send the dunning notice to the printer. For a printed notice you additionally enter a Unique ID of a Queue. Make your selection and choose Send. | Dunning is sent and Dunning Notice list items are cleared. |  |

### Reporting Collections

#### Collections Management Reporting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this analytic activity, you monitor the collection progress and promise to pay.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Collections Management Reporting - Collection Progress (F4495). | The Collections Management Reporting view is displayed the two respective tabs for you to monitor Collections Progress and Promise to Pay. |  |
| 3 | Collection Progress | Choose the Collection Progress tab. | The system displays collections progress. |  |
| 4 | Collection Progress | Select any dimension to change the view by, for example:PrioritySpecialistCollection GroupCollection Segment |  |  |
| 5 | Collection Progress | You can set a filter, for example:PrioritySpecialistCollection GroupCollection Segment |  |  |
| 6 | Promise to Pay | Choose the Promise to Pay tab. | The system displays promise to pay. |  |
| 7 | Promise to Pay | You can select any Dimension to change the view by, for example:Company CodeCountryRegionCollection SegmentSpecialist |  |  |
| 8 | Promise to Pay | You can set a filter, for example:Company CodeCountrySpecialistCustomer |  |  |

#### Collection Progress

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the collection progress.

Prerequisite

A collection worklist has been generated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Collection Progress - Current Run (F1738). | The Collection Progress (S/4HANA) (F1738) view is displayed. |  |
| 3 | Explore and Review | To change the view, select from the dropdown menu or adapt the filters for the report.The overall progress for collecting payments from the customers and the collection progress for different collection specialists and collection groups displays.The results can be displayed as a table or as different charts. |  |  |

#### Promises to Pay

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the promises to pay report.

Prerequisite

A collection worklist is generated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Promise To Pay - Today (F1753) . |  |  |
| 3 | Explore and Review | To change the view, you can use the drop-down menu to display by:By DaysBy Customer (Top 10 Open Promised Amounts)By Customer and Days (Top 10 Open Promised Amounts)By Broken Promises (Created in Last 12 Months)By Collection SpecialistThe view provides choices for filtering the results. These include filters for:Company CodeCustomerCountry, State, and Region of the customerSpecialistand moreThere are options for viewing as a table or as different types of charts. The view can then be exported to a spreadsheet. |  |  |

#### Display Dunning History

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the dunning history.

Prerequisite

A collection worklist has been generated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Dunning History (F2328). | The Display Dunning History (F2328) view is displayed. |  |
| 3 | Review | Enter the following:Company code: 3310and choose GOIn the Dunning Notices list, expand the entries to view details. |  |  |

#### Supervise Collections Worklist

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Collection worklists are created automatically on a daily basis.

Worklists ensure evaluation, identification, stratification and periodization of Business Partners according to collection strategies. The collection worklist displays Business Partners with their past due amounts. It is a tool for the AR accountant to monitor the collection process by collection specialist, to assign or unassign Business Partners to collection specialists. From the worklist, the user can also drill down to Business Partner opens items and to details of the journal entry.

From the Business Partner open items, the user can edit line items, create correspondence, block/unblock items for dunning, and block/unblock items for payment.

Prerequisite

You ran the scheduled job to transfer data from Accounts Receivable.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Supervise Collections Worklist (F2375). | The app displays a list of all business partners with the overdue receivables. |  |
| 3 | Assign Specialist | From the list of Business Partners, find one item with no specialist assigned and choose Assign to Specialist. From the dialog box, choose a specialist. | An Assignment Successful notification displays. The specialist is assigned in the Specialist field. |  |
| 4 | Drill Down | Review Business Partner and select the business partner number to review business partner open items. | From the dialog box, choose Manage Customer line items. |  |
| 5 | Block for Dunning | Review the line item and select the block for dunning.From dialog box, enter text providing a reason and additional notes.Choose OK. | Dunning block is set for the line item. |  |

#### Cash Collection Tracker

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the overall progress in collecting payments from customers.

Prerequisite

A Collection Worklist has been generated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Cash Collection Tracker - Collections Management (F3182). | The Cash Collection Tracker (F3182) view is displayed. |  |
| 3 | Enter Criteria | To change the view, choose the drill-down button or other buttons in the report.You can view the overall progress in collecting payments from the customers and the collection progress for different collection specialists and collection groups.Choose the Toggle Filter and make the following entries:As of Date: <Today’s date>Period Type: <Period Type> for example, MDisplay Currency: <Company Code currency>Exchange Rate Type: Mand choose Go. | A list of results, based on the filtering criteria displays. |  |
| 4 | Review the Data | Review the data by selecting any of the available views:By CustomerBy Collections GroupBy Collections SpecialistBy Collections ProfileBy Collections SegmentBy Collections Strategy | The list updates and displays according to the selected view. |  |

### Schedule Background Jobs (Optional)

#### Schedule Background Job to Create Dispute Cases Automatically (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule a background job to create dispute cases for residual items that arise during automatic incoming payments (such as account statement or lockbox), during check presentation, or in postprocessing. The following procedure executes the job as a single run.

Prerequisite

The subledger accounting document is posted. It must contain one or more residual items so that you can create dispute cases.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Dispute Management Jobs (F3578). | The Schedule Dispute Management Jobs view is displayed. |  |
| 3 | Create Job | Choose Create. | The New Job view is displayed. |  |
| 4 | Enter Job Details | Make the following entries and choose Schedule:General Information section:Job Template: Automatic Creation of Dispute CasesJob Name: Automatic Creation of Dispute CasesScheduling Options section:Start Immediately: SelectedRecurrence Pattern: Single RunNote To schedule a recurrence pattern, choose the Define Recurrence Pattern button and in the Scheduling Information dialog box, enter your parameters and choose OK. | The job is scheduled. |  |

#### Schedule Background Jobs to Write Off Dispute Cases Automatically

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule a background job to start the automatic write-off of all disputed items for the selected dispute cases. The program only processes dispute cases that you have previously escalated. The following procedure executes the job as a single run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Dispute Management Jobs (F3578). | The Schedule Dispute Management Jobs view is displayed. |  |
| 3 | Create Job | Choose + (New). | The New Job view is displayed. |  |
| 4 | Enter Job Details | Make the following entries and choose Step 2:Job Template: Automatic Write-Off of Dispute CasesJob Name: Automatic Write-Off of Dispute Cases |  |  |
| 5 | Enter Job Details | Make the following entries and choose Step 3:Start Immediately: SelectedRecurrence Pattern: Single RunNote To schedule a recurrence pattern, choose the Define Recurrence Pattern button and in the Scheduling Information dialog box, enter your parameters and choose OK. |  |  |
| 6 | Enter Job Details | Make the following entries and choose Schedule:Case Type: <case type>, for example, YT01Escalation Reason: <escalation reason>Case ID: <enter a single case ID or a range of case IDs> | The job is scheduled. |  |

#### Schedule Background Job to Assign a Collection Profile (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule a background job assigning a collection profile to business partners. You start the functions with the following modes:

- Create Collections Management role: If you start the program in this mode, the business partners selected are created for the Collections Management role, when they do not yet exist for this role. When the business partners are created, a collection profile is assigned. You use this mode to prepare the business partners replicated from the customers of financial accounting for Collections Management.
- Replace Collection Profile: In this mode, the collection profile is replaced for the selected business partners.

When data volume is very large, you distribute the data over several background jobs and application servers. This procedure is described as parallel processing.

Features

You influence the assignment of profiles as follows:

- You use selection criteria for the business partner number, date of creation, business partner category, and business partner grouping.
- If you start the program in Replace Collection Profile mode, you can also select by the collection profile.
- If you use SAP Credit Management, you can also further restrict the resulting list using criteria specific to Credit Management, such as the risk class and score.

Examples for practical use:

- Assign a collection profile to newly created business partners to let them take part in the collection process.
- When SAP Credit Management is in scope: Only assign a collection profile to business partners for certain, critical credit risk classes. Then, business partners with non-critical credit risk classes do not take part in the collection process.

|  |
| --- |
| Note In the following procedure, the job is executed as a single run. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Collections Management Jobs - Mass Changes (F3918). | The Schedule Collection Management Jobs view is displayed. |  |
| 3 | Create Job | Choose Create. | The New Job view is displayed. |  |
| 4 | Add General Information | Make the following entries and choose Step 2:Job Template: Assignment of Collection Profiles to Business PartnersJob Name: Assign Collection Profile to Business Partners |  |  |
| 5 | Scheduling Options | Make the following entries and choose Step 3:Start Immediately: SelectedRecurrence Pattern: Single RunNote To schedule a recurrence pattern, choose the Define Recurrence Pattern button and in the Scheduling Information dialog box, enter your parameters and choose OK. |  |  |
| 6 | Parameter Section | Make the following entries and choose Schedule:Business Partner: <select Business Partner>Created On: MM/DD/YYYYBusiness Partner Grouping: select on <Business Partner Grouping > if applicableCollection Profile to Be Entered: For example, YT_PRF:01Note You can choose to do a Test Run to verify the result. You can then remove the test flag and schedule the run. | The job is scheduled. |  |

#### Schedule Background Job to Change Segment Data (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule a background job assigning change to the segment data in the business partner master data. You can change collection groups for each segment and control, whether the collection specialist is to be swapped in this segment, retained, or deleted.

Features

For the selection criteria, in addition to specific details for Collections Management, such as the collection segment and collection group, you can also use business partner criteria such as: the ID, date of creation, business partner category, and business partner grouping.

If you use SAP Credit Management, you can also further restrict the resulting hit list by criteria specific to Credit Management, such as the risk class and score.

|  |
| --- |
| Tip Example for practical use: In case SAP Credit Management is in scope: Assign a dedicated collection group to business partners that are considered as particularly risky in SAP Credit Management. |

In the following procedure mentioned, the job is executed as a single run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Accounts Receivable Accountant |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Collections Management Jobs - Mass Changes (F3918). | The Schedule Collection Management Jobs view is displayed. |  |
| 3 | Create Job | Select + (New). | The New Job view is displayed. |  |
| 4 | Add General Information | Make the following entries and choose Step 2:Job Template: Change Collection Segment Data for Business PartnersJob Name: Change Collection Segment Data for Business Partners |  |  |
| 5 | Scheduling Options | Make the following entries and choose Step 3:Start Immediately: SelectedRecurrence Pattern: Single RunNote To schedule a recurrence pattern, choose the Define Recurrence Pattern button and in the Scheduling Information dialog box, enter your parameters and choose OK. |  |  |
| 6 | Parameter Section | Make the following entries and choose Schedule:Business Partner Selection section:Collection Segment: For example, YT_SEGMT01Collection Group: For example, YT_GR01Business Partner: <select Business Partner>Created On: MM/DD/YYYYBusiness Partner Grouping: select <Business Partner Grouping >, if applicableSegment Data to Be Entered section:Collection Group: For example, YT_GR01As optional you may chooseForce Update of Collection Specialist: <mark>By entering additionallyCollection Specialist: < Collection Specialist>Note You can decide if you want to do a Test Run first to verify the result. you can then remove the test flag and schedule the run. | The job is scheduled. | . |

#### Schedule Background Job for Assigning/Replacing a Collection Specialist (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule a background job for assigning or replacing a collection specialist.

For the selection, you can use the collection group to replace the collection specialist in the specified collection groups of all business partners.

|  |
| --- |
| Tip Example for practical use:You run this report when a collection specialist leaves your team and is replaced by a new colleague. You start the report in test mode and, in the log, check the changes that the system would carry out based on your selection. |

|  |
| --- |
| Note In the following procedure, the job is executed as a single run. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Collections Management Jobs - Mass Changes (F3918). | The Schedule Collection Management Jobs view is displayed. |  |
| 3 | Create Job | Choose + (New). | The New Job view is displayed. |  |
| 4 | Add General Information | Make the following entries and choose Step 2:Job Template: Replace Collection SpecialistsJob Name: Replace Collection Specialists |  |  |
| 5 | Scheduling Options | Make the following entries and choose Step 3:Start Immediately: SelectedRecurrence Pattern: Single RunNote To schedule a recurrence pattern, choose the Define Recurrence Pattern button and in the Scheduling Information dialog box, enter your parameters and then choose OK. |  |  |
| 6 | Parameter Section | Make the following entries and choose Schedule:To be Replaced section, enter the following:Collection Specialist: <Collection Specialist to be replaced>Collection Group: <Collection Group>Replace With section, enter the following:Collection Specialist: <new Collection Specialist>Note An option is to first choose the Test Run to verify the result. Next, remove the test flag and schedule the run. | The job is scheduled. |  |

#### Schedule Background Job to Delete Transactional Data in Collections Management (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule a background job deleting transactional data for certain business partners. You execute the job as a single run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Collections Management Jobs - Mass Changes (F3918). |  |  |
| 3 | Create Job | Choose + (New). |  |  |
| 4 | Add General Information | Make the following entries and choose Step 2:Job Template: Delete Transactional Data in Collections ManagementJob Name: Delete Transactional Data in Collections Management |  |  |
| 5 | Scheduling Options | Make the following entries and choose Step 3:Start Immediately: SelectedRecurrence Pattern: Single RunNote To schedule a recurrence pattern, choose the Define Recurrence Pattern button and in the Scheduling Information dialog box, enter your parameters and choose OK. |  |  |
| 6 | Parameter Section | Make the following entries and choose Schedule:Company Code: 3310Business Partner: <select one or more business partners>Test Run: SelectedNote Do a test run first. Check the result. If you are satisfied with the result, select the Test Run checkbox to do a real run. | The job is scheduled. |  |

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
- related-to :: [[03-financial-accounting-and-close/test-script-sap-s-4hana-cloud-public-edition-collections-and-dispute-a]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BFC_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 112,814 chars in the whole document
