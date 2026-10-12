---
id: 14-maintenance-service-and-projects/sales-order-processing-project-based-services-j14-ae-test-script-1299
title: Sales Order Processing – Project-Based Services (J14_AE) Test Script (J14_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item J14_AE: billing, credit/debit memo requests and scheduled billing jobs for project-based services (UAE)."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/project-based-services-sales-orders]
aliases: [J14_S4CLD2608_BPD_EN_AE]
keywords: [Sales Order Processing for Project-Based Services, project-based services billing, customer invoices, credit memo requests, debit memo requests, preliminary billing documents, billing approval workflow, billing job scheduling, billing document cancellation, pro forma invoice]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J14_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1299
topic: 14-maintenance-service-and-projects/project-based-services-sales-orders
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Sales Order Processing – Project-Based Services (J14_AE) Test Script (J14_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J14_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Sales Order Processing for Project-Based Services** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Sales Order Processing – Project-Based Services (J14_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Sales Order Processing – Project-Based Services (J14_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232862812)

[2 Prerequisites 4](#_Toc232862813)

[2.1 System Access 4](#_Toc232862814)

[2.2 Roles 4](#_Toc232862815)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232862816)

[2.4 Business Conditions 7](#_Toc232862817)

[2.5 Preliminary Steps 8](#_Toc232862818)

[2.5.1 Create Condition Records (Optional) 8](#_Toc232862819)

[3 Overview Table 9](#_Toc232862820)

[4 Test Procedures 11](#_Toc232862821)

[4.1 Billing 11](#_Toc232862822)

[4.1.1 Processing of Existing Billing Document Requests 11](#_Toc232862823)

[4.1.1.1 Create Pro Forma for Order (Optional) 11](#_Toc232862824)

[4.1.1.2 Create Customer Invoices 12](#_Toc232862825)

[4.1.1.3 Manage Customer Invoices (Optional) 14](#_Toc232862826)

[4.1.1.4 Create Preliminary Billing Documents (Optional) 15](#_Toc232862827)

[4.1.1.5 Process Preliminary Billing Document Approval (Optional) 16](#_Toc232862828)

[4.1.1.5.1 Approve Preliminary Billing Document 17](#_Toc232862829)

[4.1.2 Processing of Manual Credit Memo Requests 18](#_Toc232862830)

[4.1.2.1 Create a Manual Credit Memo Request with App Manage Credit Memo Requests – Version 2 18](#_Toc232862831)

[4.1.2.2 Check Billing Block Status 20](#_Toc232862832)

[4.1.2.3 Process Credit Memo Request Approval (Optional) 20](#_Toc232862833)

[4.1.2.3.1 Approve/Reject a Credit Memo Request 21](#_Toc232862834)

[4.1.2.4 Create a Manual Credit Memo 22](#_Toc232862835)

[4.1.2.5 Manage Manual Credit Memos (Optional) 23](#_Toc232862836)

[4.1.3 Processing of Manual Debit Memo Requests 24](#_Toc232862837)

[4.1.3.1 Create a Manual Debit Memo Request with App Manage Debit Memo Requests – Version 2 24](#_Toc232862838)

[4.1.3.2 Manage Debit Memo Requests (Optional) 26](#_Toc232862839)

[4.1.3.3 Create Customer Invoices 27](#_Toc232862840)

[4.1.3.4 Manage Customer Invoices (Optional) 28](#_Toc232862841)

[4.2 Auxiliary Processes (Optional) 29](#_Toc232862842)

[4.2.1 Schedule Job (Optional) 29](#_Toc232862843)

[4.2.1.1 Schedule Billing Creation (Optional) 29](#_Toc232862844)

[4.2.1.2 Job Scheduling for Preliminary Billing Documents Creation (Alternative) 30](#_Toc232862845)

[4.2.1.3 Schedule Billing Release (Optional) 31](#_Toc232862846)

[4.2.1.4 Schedule Billing Output (Optional) 32](#_Toc232862847)

[4.2.2 Billing Processing (Optional) 33](#_Toc232862848)

[4.2.2.1 Cancel Billing Document(Optional) 33](#_Toc232862849)

[5 Appendix 35](#_Toc232862850)

## Purpose

Overview

This scope item outlines the sales order maintenance and billing process within a project-based services scenario. It covers the creation of billing documents, including invoices, credit memos, manual credit memo requests, manual debit memos, and debit memo requests.

In the invoicing subprocess, the customer project management process initiates a billing document request, which is then converted into a customer invoice.

In the credit memo subprocess, a credit memo can be generated with or without referencing an existing customer invoice. A credit memo is subsequently created from a credit memo request.

In the manual debit memo subprocess, a debit memo request is manually created and sent to billing, where it results in a customer invoice.

Finally, these processes transfer to the Accounts Receivable process.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/J14_S4CLD2602_BPD_EN_AE.docx) ). |

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
| Internal Sales Representative - Professional Services | SAP_BR_INTERNAL_SALES_REP_PRSV | Internal Sales - Professional Services | SAP_BR_INTERNAL_SALES_REP_PRSV | Suggested sample user INTERNAL_SALES_REP_PRSV representing the business role Internal Sales Representative - Professional Services. |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK | Suggested sample user BILLING_CLERK representing the business role Billing Clerk. |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC | Suggested sample user BUSINESS_PROCESS_SPEC representing the business role Business Process Specialist. |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | Suggested sample user BPC_EXPERT representing the business role Configuration Expert - Business Process Configuration. |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers and vendors, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices Baseline Package, you can use the following Baseline Package scenario data :

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | P001 | Project-Based Service: Fixed Price | Material which will be used in order to describe different services being provided to the customer |
| Material | P002 | Project-Based Service: Time & Expenses | Material which will be used in order to describe different services being provided to the customer |
| Material | P003 | Periodic Service | Material which will be used in order to describe different services being provided to the customer |
| Material | H001 | Hardware 001 |  |
| Material | H002 | Hardware 002 |  |
| Material | T001 | Junior Consultant |  |
| Material | T002 | Senior Consultant |  |
| Materials | T003 to T020 | Time Recording: Rate Type 03 to 20 |  |
| Material | E001 | Accommodation |  |
| Material | E002 | Airfare |  |
| Material | E003 | Ground Transportation |  |
| Material | E004 | Miscellaneous |  |
| Materials | E005 to E040 | Billable Expenses 05 to 40 |  |
| Materials | L001 | License 001 |  |
| Material | U001 | Cloud Sales Licences |  |
| Material | U002 | Service Center Tickets |  |
| Material | U003 to U010 | Incidents Monitoring |  |

Allowed changes to the above listed service-related materials are limited to descriptions and some attributes, since they are provided with DIP-Profile, a technical object necessary for selling of project-based services.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Sold-to party | 33100001 | Domestic UAE Customer 1 |  |
| Ship-to party | 33100001 | Domestic UAE Customer 1 |  |
| Payer | 33100001 | Domestic UAE Customer 1 |  |
| Sales organization | 3310 | Dom. Sales Org |  |
| Distribution channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Scripts Reference

| Master Data ID | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| 31X | Create Product Master of type "Service Product" - MDS |

### Business Conditions

Before testing this scope item, you must meet either of following business conditions.

| Scope Item | Business Condition |
| --- | --- |
| J11 - Customer Project Management – Project-Based Services | Must be run before this test script. A project must be created and the employee must be assigned to a project. |
| 1A8 - Internal Project Management – Project-Based Services | Must be run before this test script. A project must be created and the employee must be assigned to a project. |

### Preliminary Steps

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BET | Create Sales Pricing Condition - MDS |

## Overview Table

This scope item consists of several process steps provided in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/Apps | Expected Results |
| --- | --- | --- | --- |
| Billing |  |  |  |
| Processing of Existing Billing Document Requests |  |  |  |
| [Create Pro Forma for Order (Optional)](#unique_9) [page ] 11 | Billing Clerk | Create Billing Documents (F0798) | The system generates a Pro Forma for Order. |
| [Create Customer Invoices](#unique_10) [page ] 12 | Billing Clerk | Create Billing Documents (F0798) | Invoice and Journal Entry are created. |
| [Manage Customer Invoices (Optional)](#unique_11) [page ] 14 | Billing Clerk | Manage Billing Documents (F0797) | Customer invoices are displayed/changed/canceled. |
| [Create Preliminary Billing Documents (Optional)](#unique_12) [page ] 15 | Billing Clerk | Create Preliminary Billing Documents (F2876) |  |
| [Process Preliminary Billing Document Approval (Optional)](#unique_13) [page ] 16 |  |  |  |
| [Approve Preliminary Billing Document](#unique_14) [page ] 17 | Billing approver you set in preliminary step | My Inbox (F2097) |  |
| Processing of Manual Credit Memo Requests |  |  |  |
| [Create a Manual Credit Memo Request with App Manage Credit Memo Requests – Version 2](#unique_15) [page ] 18 | Internal Sales Representative - Professional Services | Manage Credit Memo Requests - Version 2 (F1989A) | A credit memo request is created. |
| [Check Billing Block Status](#unique_16) [page ] 20 | Internal Sales Representative - Professional Services | Manage Credit Memo Requests (F1989) |  |
| [Process Credit Memo Request Approval (Optional)](#unique_17) [page ] 20 |  |  |  |
| [Approve/Reject a Credit Memo Request](#unique_18) [page ] 21 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Create a Manual Credit Memo](#unique_19) [page ] 22 | Billing Clerk | Create Billing Documents (F0798) |  |
| [Manage Manual Credit Memos (Optional)](#unique_20) [page ] 23 | Billing Clerk | Create Billing Documents (F0798)-Billing Due List Items. | The credit memo is changed. |
| Processing of Manual Debit Memo Requests |  |  |  |
| [Create a Manual Debit Memo Request with App Manage Debit Memo Requests – Version 2](#unique_21) [page ] 24 | Internal Sales Representative - Professional Services | Manage Debit Memo Requests - Version 2 (F1988A) | A debit memo request is created. |
| [Manage Debit Memo Requests (Optional)](#unique_22) [page ] 26 | Internal Sales Representative - Professional Services | Manage Debit Memo Requests (F1988) | Debit memo requests are displayed/changed/canceled. |
| [Create Customer Invoices](#unique_23) [page ] 27 | Billing Clerk | Create Billing Documents (F0798). | Debit memo and Journal Entry are created. |
| [Manage Customer Invoices (Optional)](#unique_24) [page ] 28 | Billing Clerk | Manage Billing Documents (F0797) | The debit memo is updated. |
| Auxiliary Processes (Optional) |  |  |  |
| Schedule Job (Optional) |  |  |  |
| [Schedule Billing Creation (Optional)](#unique_25) [page ] 29 | Billing Clerk | Schedule Billing Creation | Billing creation jobs are scheduled. |
| [Job Scheduling for Preliminary Billing Documents Creation (Alternative)](#unique_26) [page ] 30 | Billing Clerk | Schedule Creation of Preliminary Billing Documents (F4563). |  |
| [Schedule Billing Release (Optional)](#unique_27) [page ] 31 | Billing Clerk | Schedule Billing Release (F1518) | Billing release jobs are scheduled. |
| [Schedule Billing Output (Optional)](#unique_28) [page ] 32 | Billing Clerk | Schedule Billing Output (F1510) | Billing output jobs are scheduled. |
| Billing Processing (Optional) |  |  |  |
| [Cancel Billing Document(Optional)](#unique_29) [page ] 33 | Billing Clerk | Manage Billing Documents (F0797) | The billing document is canceled. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Billing

#### Processing of Existing Billing Document Requests

##### Create Pro Forma for Order (Optional)

Purpose

This process step shows you how the billing clerk creates Pro Forma for Order for services which have been executed. The Pro Forma for Order is printed and can be sent to the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings at the right top of the items table.There are five settings in the Billing Settings dialog box. Turn the last setting to OFF and other four settings to ON as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: ONAutomatically post billing documents: ONDisplay billing document after creation: ONChoose delivery items to be billed and select quantities: OFFChoose OK. |  |  |
| 4 | Search for Billing Due Items | In the search condition, use criteria if necessary.For example, SD Document Category: Billing Document Request | Sales documents are displayed in the result. |  |
|  | Note Before doing the next step, the customer billing document request must be created. This is part of the Project Billing – Project-Based Services(4E9) scope item. |  |  |  |
| 5 | Create Pro Forma for Order | Select the document and choose Create Billing Documents. | The Create Billing Documents dialog displays. |  |
| 6 | Enter Billing Details | Choose Billing Type Pro Forma for Order (F5) and maintain Billing Date, for example, <current date>, and then choose OK. | The draft billing document with ID TMPxxxxxxxx displays. |  |
| 7 | Check the Draft | On the Manage Billing Documents screen:On the Items tab, check the items are copied right from the bill document request.On the Process Flow tab, check the process flow. | The items are with right quantity and price. |  |
| 8 | Save Pro Forma for Order | On the Manage Billing Documents screen, choose Save. The draft version billing document with ID TMPxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the number : __________. | The system generates a Pro Forma for Order. |  |

##### Create Customer Invoices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how the billing clerk to create invoices for services which have been executed. The invoice is printed and can be sent to the customer. A journal entry created in finance becomes the basis for incoming payments which clear the open items in customer accounts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings at the right top of the items table.There are five settings in the Billing Settings dialog box. Turn the last setting to OFF and other four settings to ON as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: ONAutomatically post billing documents: ONDisplay billing document after creation: ONChoose delivery items to be billed and select quantities: OFFChoose OK. |  |  |
| 4 | Search for Billing Due Items | In the search condition, use criteria if necessary. | Sales documents are displayed in the result. |  |
|  | Note Before doing the next step, the customer billing document request must be created. This is part of the Project Billing – Project-Based Services (4E9) scope item.Note If you would like to check the billing information from the preliminary billing documents functionality based on these billing due list items, details please refer to chapter 5.14 of Sales Scheduling Agreements (3NR) scope item.You can also test the convergent billing scenario in 4.2 Creating a Billing Document Combining External Billing Data and Data from Professional Services and 4.4 Create a Billing Document Combining External Data, Data from Sell from Stock and Data from Professional Service of the Omnichannel Convergent Billing (1MC) scope item. |  |  |  |
| 5 | Create Customer Invoice | Select the document and choose Create Billing Documents. | The Create Billing Documents dialog displays. |  |
| 6 | Enter Billing Details | Choose Billing TypeInvoice (CI01) and maintain Billing Date, for example, <current date>, and then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Manage Billing Documents screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number : __________. | The system generates an invoice for billing. |  |

##### Manage Customer Invoices (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to list the customer invoices which have been created. From this list, invoices can be canceled or posted to accounting. Depending on system configuration, billing documents are automatically transferred to accounting or they are blocked for automatic posting and will be manually released to accounting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Billing Documents (F0797) |  |  |
| 3 | Select Document | Make the following entries:Billing Document: <previously created billing document> | The relevant invoice document is selected. |  |
| 4 | Display Invoice Details | Select the row of your billing document and choose Display. | Invoice document details display. |  |
| 5 | Preview Output | Choose Preview. | A PDF document of the invoice printout displays. |  |
| 6 | Post Invoice (Optional) | Go back to the Billing Document screen.Depending on system configuration, billing documents are automatically transferred to accounting or they are blocked for automatic posting and will be manually released to accounting. In case the billing document has not yet been posted to accounting, choose Post Billing Document to create a journal entry. | The invoice is transferred to Accounting. The system displays Billing documents posted message. |  |

##### Create Preliminary Billing Documents (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create preliminary billing documents based on these billing due list items as well as how to create preliminary down payment request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Preliminary Billing Documents (F2876). | The Create Preliminary Billing Documents screen displays. |  |
| 3 | Search for Billing Due List Items | To enable a filter, type a value directly to trigger autosuggest and press Enter, or use the input help to choose a value (such as a SD document category: Debit Memo Request). | Debit memo request(s) will display in the result. |  |
| 4 | Define Preliminary Billing Settings | Choose Preliminary Billing Settings in the top-right corner, and make the following settings:Set billing date and type before creating preliminary billing document - OFFCreate separate preliminary billing document for each item of billing due list - OFFDisplay preliminary billing documents after creation - ONAutomatically finalize preliminary billing documents after creation - ON |  |  |
| 5 | Select an Item to Create Preliminary Billing Document | Select the document and choose Create Preliminary Billing Documents. | The Manage Preliminary Billing Documents screen displays. |  |
| 6 | In the Manage Preliminary Billing Documents App | The preliminary billing document with ID PBDxxxxxxxx has been created. | The system generates a preliminary billing document for billing. |  |

##### Process Preliminary Billing Document Approval (Optional)

|  |
| --- |
| Note Only relevant if below conditions are fulfilled:Approval reason is defined and assigned. For details refer to the chapter 2.6.7.1 Define and Assign Approval Reasons in scope item Sell from Stock (BD9).The Cloud BADI that returns an approval reason is implemented. For details refer to the Chapter 2.6.7.2 Implement Cloud BADI in scope item Sell from Stock(BD9).Total amount of the order is more than 500. |

###### Approve Preliminary Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to make approval decision to release the preliminary billing documents. This step also applies to preliminary down payment request.

Prerequisites

1. Ensure all the workflow relevant preliminary steps which mentioned in chapter 2.6.7 of scope item Sell from Stock (BD9) have been done successfully.
2. Approval status of the preliminary billing document is In Approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing approver you set in preliminary step. | The SAP Fiori launchpad displays. |  |
| 2 | Receive Notification | Open My Inbox (F2097).You can also choose the Notifications icon in the top right corner to navigate to My Inbox screen. | The Inbox screen displays. |  |
| 3 | Refresh | Choose Refresh if necessary. | Inbox is refreshed. |  |
| 4 | Approve Preliminary Billing Document | You receive the notification of the preliminary billing. Choose Release from the options on the bottom bar. | The Submit Decision dialog box displays. |  |
| 5 | Submit | Add comments (optional) and choose Submit. | Release: the whole process ends; no subsequent step is needed. |  |

#### Processing of Manual Credit Memo Requests

##### Create a Manual Credit Memo Request with App Manage Credit Memo Requests – Version 2

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a manual credit memo request with and without reference to preceding document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Create a Credit Memo Request without Reference | Log on to the SAP Fiori launchpad as an Internal Sales Representative - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Credit Memo Requests - Version 2 (F1989A).Choose Create.In the Create pop-up dialog, make the following entry:Credit Memo Request Type: Credit MemReq Manual (CMR4)Choose Continue. |  |  |
| 3 | Enter Sold-to-Party Data | On the New: Credit Memo Request screen, enter the sold-to-party data:Sold-to Party: 33100001 |  |  |
| 4 | Enter Billing Date | In the Pricing and Billing area, enter a billing date:Billing Date: <today's date> |  |  |
| 5 | Enter Product | In the Items list, make the following entries:Product: P001Target Quantity: <any>Press Enter or choose Add Row to add new items.Choose the arrow button > (Details) at the end of the line to go to the detailed page.In the Advanced Data section, choose the WBS Element using the value help.Choose Apply. |  |  |
| 6 | Enter Manual Price | Go back to the first item row and choose the Details icon to open the item details.Choose the Prices tab. It goes to Prices Basic Data.Choose Create. Make the following entry in the Create dialog:Condition Type: PMP0Choose Create.Condition type PMP0 is added to Price Elements list.Maintain a manual price for the item:Condition Type: PMP0Condition Amount or Ratio: <any>Pricing Unit: <any>Choose Apply.Repeat above steps to create multiple items if needed. | Net Value is maintained for items P001. |  |
| 7 | Create a Credit Memo Request | Choose Create. Make a note of the credit memo request ___________________ . | A credit memo request is created. |  |
| 8 | Create a Credit Memo Request with Reference | Open Manage Credit Memo Requests - Version 2 (F1989A).Choose Create with Reference and select From Invoice from the dropdown list.In the From Invoice dialog, make the following entries:Credit Memo Request Type: Credit MemReq Manual (CMR4)Invoice: <invoice of Billing Type CI01>Choose Continue. |  |  |
| 9 | Create a Credit Memo Request with Reference | On the New: Credit Memo Request screen, all the information is replicated from the reference invoice.You can change the items by adding new items, changing Target Quantity, etc.Choose Create. Make a note of the credit memo request ___________________ . | A credit memo request is created. |  |

##### Check Billing Block Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the credit memo request status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Credit Memo Requests (F1989). | The Manage Credit Memo Request screen displays. |  |
| 3 | Set Windows | Choose Settings and select the Billing Status and Billing Block Status. And choose OK.Choose Go. | Set view settings. |  |
| 4 | Check the Credit Memo Request Status | Check the credit memo request that you created in previous steps.Billing Status: not invoicedBilling Block Status: Blocked/Not BlockedFor credit memo workflow net value over 500 (then go to the Approve Credit Memo Request step).For credit memo workflow net value not exceeding 500 Not Blocked (then go to the [Create a Manual Credit Memo](#unique_19) [page ] 22 step). | Credit memo request status displays. |  |

##### Process Credit Memo Request Approval (Optional)

|  |
| --- |
| Note Only relevant if below conditions are fulfilled:1. Approval reason is defined and assigned. For details refer to the Chapter2.4.3.1 Define and Assign Approval Reasons in Credit Memo Processing (1EZ) scope item.2. The Cloud BADI that returns an approval reason is implemented. For details refer to the Chapter2.4.3.2 Implement Cloud BADI in Credit Memo Processing (1EZ) scope item3. Total amount of the order is more than 500. |

###### Approve/Reject a Credit Memo Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to makes approval decision: release or reject.

Prerequisite

1.Please ensure all the workflow relevant preliminary steps which mentioned chapter 2.4.3 in Credit Memo Processing (1EZ) scope item have been done successfully.

2.Approval status of the Credit Memo Request is In Approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862).You can also choose the Notifications icon on the top right corner to navigate to the My Inbox screen. | The Inbox screen displays. |  |
| 3 | Refresh | Choose Refresh if necessary. | Inbox is refreshed. |  |
| 4 | Approve/Reject | You receive the notification of the credit memo request. Choose one from the options on the bottom bar.Option 1: ReleaseOption 2: Reject | The Submit Decision dialog box displays. |  |
| 5 | Submit | Enter some comments and choose Submit. | Based on above decisions, choose next steps accordingly:Release: the whole process ends, and no subsequent step is needed.Reject: the whole process ends, and no subsequent step is needed. |  |

##### Create a Manual Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a credit memo for a credit memo request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798)-Billing Due List Items. | The Billing Due List Items screen displays. |  |
| 3 | Select the Credit Memo Request to be Invoiced | Select the credit memo request you have created before and choose Create Billing Documents. | The Create Billing Documents screen displays. |  |
| 4 | Enter Billing Details | Choose billing type Credit Memo Project Services (CM01) and maintain billing date, for example, current date, then select OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 5 | Save Billing Document | On the Billing Document screen, choose Save.The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | The system generates an invoice for billing. |  |

##### Manage Manual Credit Memos (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to change a debit memo.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Documents screen displays. |  |
| 3 | Search the Credit Memo Created in Previous Steps | Enter the credit memo number recorded in previous step.Choose Enter. | The credit memo document created in previous step will display. |  |
| 4 | Select Line Item | Select a line item and choose Display. In the new window, choose Edit, and then navigate to tab Texts. | The item details display. |  |
| 5 | Enter Item Texts | In the Texts section, choose Add Text. In the New Text dialog box, select a language in Language and a text type in Text Types Available for Language, enter text and choose OK. |  |  |
| 6 | Save Billing Document | Choose Save. | Billing document is saved. |  |

#### Processing of Manual Debit Memo Requests

##### Create a Manual Debit Memo Request with App Manage Debit Memo Requests – Version 2

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a manual debit memo request with and without reference to preceding document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Create a Debit Memo Request without Reference | Log on to the SAP Fiori launchpad as an Internal Sales Representative - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Debit Memo Requests - Version 2 (F1988A).Choose Create.In the Create pop-up dialog, make the following entry:Debit Memo Request Type: Debit MemReq Manual (DMR4)Choose Continue. |  |  |
| 3 | Enter Sold-to-Party Data | On the New: Debit Memo Request screen, enter the sold-to-party data:Sold-to Party: 33100001 |  |  |
| 4 | Enter Billing Date | In the Pricing and Billing area, enter a billing date:Billing Date: <today's date> |  |  |
| 5 | Enter Product | In the Items list, make the following entries:Product: P001Target Quantity: <any>Press Enter or choose Add Row to add new items.Choose the arrow button > (Details) at the end of the line to go to the detailed page.In the Advanced Data section, choose the WBS Element using the value help.Choose Apply. |  |  |
| 6 | Enter Manual Price | Go back to the first item row and choose the Details icon to open the item details.Choose the Prices tab. It goes to Prices Basic Data.Choose Create. Make the following entry in the Create dialog:Condition Type: PMP0Choose Create.Condition type PMP0 is added to Price Elements list.Maintain a manual price for the item:Condition Type: PMP0Condition Amount or Ratio: <any>Pricing Unit: <any>Choose Apply.Repeat above steps to create multiple items if needed. | Net Value is maintained for items P001. |  |
| 7 | Create a Debit Memo Request | Choose Create. Make a note of the debit memo request ___________________ . | A debit memo request is created. |  |
| 8 | Create a Debit Memo Request with Reference | Open Manage Debit Memo Requests - Version 2 (F1988A).Choose Create with Reference and select From Invoice from the dropdown list.In the From Invoice dialog, make the following entries:Debit Memo Request Type: Debit MemReq Manual (DMR4)Invoice: <invoice of Billing Type CI01>Choose Continue. |  |  |
| 9 | Create a Debit Memo Request with Reference | On the New: Debit Memo Request screen, all the information is replicated from the reference invoice.You can change the items by adding new items, changing Target Quantity, etc.Choose Create. Make a note of the debit memo request ___________________ . | A debit memo request is created. |  |

##### Manage Debit Memo Requests (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display, change and cancel a manual debit memo request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Debit Memo Requests (F1988). | The Manage Debit Memo Requests screen displays. |  |
| 3 | Enter Document Number | In the search field, enter the Debit Memo Request number you created previously, and choose Go. | The Sales Document with all items is displayed in a list. |  |
| 4 | Change Document | Choose the Debit Memo Request number you created. In the dialog box, choose Change Debit Memo Request. | The Change Debit Memo Request screen displays. |  |
| 5 | Change Item | Double click a line item. Change the quantity of the item.Target Quantity: <qty> | Item quantity is changed. |  |
| 6 | Save Document | Choose Save. | Debit memo request is saved with changes. |  |

##### Create Customer Invoices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how the Billing Clerk to create an invoice for a debit memo request and for services which have been executed. The invoice is printed and can be sent to the customer. A journal entry is created in finance is then the basis for incoming payments which clear the open items in customer accounts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Select Debit Memo Request for Invoicing | Select the debit memo request you created previously and choose Create Billing Documents. | The Create Billing Documents screen displays. |  |
| 4 | Enter Billing Details | Enter the following :Billing type: Invoice(CI01)Billing date, choose OK. | The draft billing document with ID Sxxxxxxxx display. |  |
| 5 | Save Billing Document | In the Billing Document screen, select Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________.. | The system generates an invoice for billing. |  |

##### Manage Customer Invoices (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This optional process step shows you how to change a debit memo.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Document screen displays. |  |
| 3 | Search the Debit Memo Created in Previous Steps | Enter the debit memo number recorded in previous steps.Choose Enter. | The debit memo document created in previous steps display. |  |
| 4 | Select Line Item | Select a line item and choose Display. In the new window, choose Edit, and then navigate to tab Texts. | The item details are displayed. |  |
| 5 | Enter Item Texts | In the Texts section, choose Add Text. In the New Text dialog box, select a language in Language and a text type in Text Types Available for Language, enter text and choose OK. |  |  |
| 6 | Save Billing Document | Choose Save. | The billing document is saved. |  |

### Auxiliary Processes (Optional)

#### Schedule Job (Optional)

##### Schedule Billing Creation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to define the creation of billing documents according to a schedule.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Creation. | A list of application jobs displays. |  |
| 3 | Create Billing Creation Schedule | Choose New to define a new billing job. | A new screen displays. |  |
| 4 | Job Parameters | Define parameters for the billing items to be included in the batch job and the start time of the job, then choose Check. | The system displays the messageGo ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing creation job is scheduled. |  |
| 6 | Check Billing Creation Job Log | Go back to the list of application jobs where the new job displays. |  |  |

##### Job Scheduling for Preliminary Billing Documents Creation (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for creating preliminary billing documents.

This app can be used as an alternative instead of the manual creation of preliminary billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Creation of Preliminary Billing Documents (F4563). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Preliminary Billing Creation Schedule | Choose New to define a new job for preliminary billing creation. | The New Job screen displays. Job Template should default as Preliminary Billing Document Creation. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the messageYou can go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A preliminary billing creation job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Preliminary Billing Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose the Go, and the job list will refresh. | The log details display. |  |

##### Schedule Billing Release (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This optional process step shows you how to define the release of billing documents according to a schedule.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Release (F1518). | A list of application jobs appears. |  |
| 3 | Create New Billing Release Schedule | Choose New to define a new billing release job. | A new screen displays. |  |
| 4 | Job Parameters | Define parameters for the billing items to be included in the batch job and the start time of the job, then choose Check. | The system displays the messageGo ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled. |  |
| 6 | Check Billing Release Job Log | Go back to the list of application jobs where the new job is displayed. |  |  |

##### Schedule Billing Output (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This optional process step shows you how to define when and how customer invoices are sent to the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Output (F1510). | A list of application jobs displays. |  |
| 3 | Billing Output | Choose New to define a new billing output job. |  |  |
| 4 | Job Parameters | Define parameters for the billing items to be included in the batch job and the start time of the job, then choose Check. | The system displays the messageGo ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing output job has been scheduled. |  |
| 6 | Check Billing Output Job Log | Go back to the list of application jobs where the new job is displayed. |  |  |

#### Billing Processing (Optional)

##### Cancel Billing Document(Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to cancel a billing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Billing Documents (F0797). | List of billing documents displays. |  |
| 3 | Select Billing Document to be Cancelled | Select a billing document in status Completed and choose Cancel Billing Docs. | A cancellation confirmation dialog box is displayed. Make a note of the billing document number___________________ |  |
| 4 | Confirm Cancellation of Billing Document | Choose OK. | System confirms cancellation with messageBilling documents canceled. |  |

## Appendix

The Processes J14 can be a part of the two-tier scenario "Procurement of Project Services from Subsidiaries by Headquarter", in which a headquarter can procure project services from a subsidiary.

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
- see-also :: [[14-maintenance-service-and-projects/project-billing-project-based-services-4e9-ae-test-script-1021]]
- see-also :: [[14-maintenance-service-and-projects/test-script-time-recording-project-based-services-j12-ae-1297]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J14_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 56,985 chars in the whole document
