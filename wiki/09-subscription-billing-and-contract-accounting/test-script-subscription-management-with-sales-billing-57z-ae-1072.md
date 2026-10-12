---
id: 09-subscription-billing-and-contract-accounting/test-script-subscription-management-with-sales-billing-57z-ae-1072
title: "Test Script: Subscription Management with Sales Billing (57Z_AE) (57Z_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 57Z: subscriptions in SAP Subscription Billing, pre-bill, billing document, credit and debit memos."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/subscription-management-sales-billing]
aliases: [57Z_S4CLD2608_BPD_EN_AE]
keywords: [Subscription Management with Sales Billing, subscription billing, subscription management, provider contract, pre-bill, billing documents, credit memos, debit memos, solution orders, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/57Z_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1072
topic: 09-subscription-billing-and-contract-accounting/subscription-management-sales-billing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Subscription Management with Sales Billing (57Z_AE) (57Z_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/57Z_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Subscription Management with Sales Billing** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Subscription Management with Sales Billing (57Z_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232856265)

[2 Prerequisites 4](#_Toc232856266)

[2.1 Additional Manual Configuration 4](#_Toc232856267)

[2.2 System Access 4](#_Toc232856268)

[2.3 Roles 5](#_Toc232856269)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232856270)

[2.5 Business Conditions (Optional) 6](#_Toc232856271)

[3 Overview Table 7](#_Toc232856272)

[4 Test Procedures 8](#_Toc232856273)

[4.1 Manage Subscription Billing 8](#_Toc232856274)

[4.1.1 Create Subscriptions in SAP Subscription Billing 8](#_Toc232856275)

[4.1.2 Display Subscription in SAP Subscription Billing 9](#_Toc232856276)

[4.1.3 Display Provider Contract 11](#_Toc232856277)

[4.1.4 Display Pre-Bill in SAP Subscription Billing 12](#_Toc232856278)

[4.2 Manage Billing Document 13](#_Toc232856279)

[4.2.1 Create Billing Document 13](#_Toc232856280)

[4.2.2 Display Billing Document 15](#_Toc232856281)

[4.3 Create Credit Memo with Reference to Invoice 16](#_Toc232856282)

[4.4 Create Debit Memo with reference to Invoice 16](#_Toc232856283)

[5 Appendix 18](#_Toc232856284)

## Purpose

Overview

SAP Subscription Billing provides a simplified, automated approach to manage and bill your subscriptions. SAP S/4HANA Cloud Public Edition offers innovative financial processes for invoicing, accounting, and controlling. The scenario unites the capabilities of both solutions to establish an integrated subscription management process.

Subscriptions are created via a user-interface or as part of an SAP S/HANA Cloud solution order in SAP Subscription Billing. SAP Subscription Billing manages the subscription life cycle, charges recurring rates, prices usage data, and prepares the billing data at the end of each billing cycle. The billing data is forwarded to SAP S/4HANA Cloud Public Edition sales billing where tax amounts are added and the invoice is created.

The invoiced amounts are then available in receivable management, accounts receivable, event-based revenue recognition and controlling.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/57Z_S4CLD2602_BPD_EN_AE.docx) ). |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/ce94397783772ce7b4625bcc48d89fce)

### System Access

The test should be conducted with the following system:

|  |
| --- |
| Note For system details, you must contact your system administrator. |

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP Cloud Platform | Your system administrator should provide you with a URL and the login details. |
| SAP Subscription Billing Tenant | Your system administrator should provide you with a URL and the login details. |

### Roles

Use the following standard test users or assign roles to testers, respectively for S/4 HANA Cloud System:

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Solution Order Specialist | SAP_BR_SOLN_ORDER_SPCLST | Solution Order Management | SAP_BR_SOLN_ORDER_SPCLST | Your system administrator provides the user and password information. |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK | Your system administrator provides the user and password information. |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | Your system administrator provides the user and password information. |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Customer | Customer:17100065 | 65 | Make sure that the customer you use for this process has either assigned the customer pricing procedure 01 (Procedure 01) or no procedure.to check the assignment, use Business Role SAP_BR_BUPA_MASTER_SPECIALIST - tile Manage Customer Master Data in the Sales Area Data. |
| Self Services / Self Services / Employee Overview Space | - | < Use your own employee ID that is assigned to your user ID.> |  |
| Subscription Product | Non-PCS Product: P-CLOUD_STORAGEPCS Product: P-CLOUD_STORAGE_PC | Cloud Storage |  |
| Rate Elements | R-ONETIME | One-Time Activation Fee |  |
| Rate Elements | R-SEATS | Seat-Based Monthly Fee |  |
| Rate Elements | R-TRAFFIC | Traffic-Based Usage Fee |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Company code | 3310 | Company Code 3310 |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| 5BD | Create Subscription Product Sales Billing - MDS |

### Business Conditions (Optional)

|  |
| --- |
| Note These business conditions are only relevant if you test this scenario with a solution order. They do not apply for a stand-alone scenario. |

| Scope Item | Business Condition |
| --- | --- |
| 4GT - Solution Order Management | If you are testing this scenario with a solution order, you must run the test script for scope item [4GT](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/4GT) before going through the test script for scope item 57Z. |

## Overview Table

This process variant starts with the creation of a solution order or creation of Subscription directly in the Subscription tenant.

| Process step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Subscriptions in SAP Subscription Billing](#unique_9) [page ] 8 |  | Manage Subscriptions | Subscriptions are created |
| [Display Subscription in SAP Subscription Billing](#unique_10) [page ] 9 | Solution Order Specialist | Manage Solution Order | Subscription is displayed |
| [Display Provider Contract](#unique_11) [page ] 11 | Solution Order Specialist | Manage Solution Order | Provider Contract is displayed |
| [Display Pre-Bill in SAP Subscription Billing](#unique_12) [page ] 12 | Solution Order Specialist | Manage Solution Order | Pre-Bill is displayed |
| [Create Billing Document](#unique_13) [page ] 13 | Billing Clerk | Create Billing Document | Invoice is created for Solution Order |
| [Display Billing Document](#unique_14) [page ] 15 | Billing Clerk | Display Billing Document | Invoice is displayed |
| [Create Credit Memo with Reference to Invoice](#unique_15) [page ] 16 |  | Create Credit Memo With Reference To Invoice | Credit memo is created |
| [Create Debit Memo with reference to Invoice](#unique_16) [page ] 16 |  | Create Debit Memo With Reference To Invoice | Debit memo is created |
|  |  |  |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Manage Subscription Billing

#### Create Subscriptions in SAP Subscription Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create subscriptions either via the solution order or directly from the SAP Subscription Billing UI.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Subscription Billing launchpad. | The Fiori Launchpad is displayed. |  |
| 2 | Navigate to Subscriptions | Choose the Manage Subscriptions app. | Manage Subscriptions page is displayed. |  |
| 3 | Create Subscriptions | Choose Create. | The Create Subscription pop up is displayed. |  |
| 4 | Enter Subscription Details | Enter the following details on the pop up screen:Customer : 33100001Product: P-CLOUD_STORAGENote If you are using the price calculation scenario, you can use P-CLOUD_STORAGE_PC as the Main Product.Valid From: The current date is set automatically.Initial Fixed Term: This is available only if the Main Product is left blank.Subscription Profile: Example, S/4 IntegrationChoose Continue. | The subscription is created successfully. |  |
| 6 | Choose Item Instructions | Choose Item List > Product > Subscription Parameters > Seat-Based Monthly Fee and enter a value, for example, 2.If you are using the PCS product (P-CLOUD_STORAGE_PC), you must verify the One-Time Net Charges, Recurring Net Charges, and Usage-Based Charges.Verify the Net Amount and choose Apply.Choose Create.Note Note the Subscription ID for the pre-bill process. |  |  |

#### Display Subscription in SAP Subscription Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to view the subscription in the Subscription Billing tenant and to verify the details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist, if the subscription is created via a Solution Order. | The Fiori Launchpad is displayed. |  |
| 2 | Navigate to Manage Solution Orders | Choose the Manage Solution Orders tile.Note For creating subscriptions via solution orders, refer to the test script for Solution Order Management (4GT). | Manage Solution Orders page is displayed. |  |
| 3 | Search for Solution Order | In the search area enter the Solution Order ID in the Solution Order field.Choose Go. | The solution order is displayed in the search result. |  |
| 4 | Open Solution Order | Choose the solution order from the result list. | Solution Order details is displayed in the Display Solution Order Page. |  |
| 5 | View Progress | In the Solution Order, choose View Progress. | Solution Order Progress is displayed. |  |
| 6 | Navigate to Subscription | In the Solution Order Progress. go to section Solution Order Progress.In the Subscription section, choose Subscription Billing.Note User can navigate to the subscription billing via the transaction history in Solution Order.Alternatively, log on to Subscription Billing > Subscriptions and search for the created subscriptions using the Subscription ID. |  |  |
| 7 | Check Subscription Header Details | Check the following subscription header details at the top:Customer : 33100001Status : ActiveValid From – XXX XX, XXXXExpires OnMarket : US EastTime Zone : Etc/GMTNote Note down the provider contract ID mentioned in the Processing data tab for further steps. | All the details are rightly available in Subscription Billing.Provider Contract ID is provided. |  |
| 8 | Check Subscription item details | In the Processing Data , check for the details like:Subscription ProfilesRelated DocumentsSubscription DatesSnapshot DataIn the Item List, choose Subscription Item, to view the complete details of the transaction.Details like Billing, Subscription Parameter, Pricing can be viewed.Note If you are using a Price Calculation Services product such as P-CLOUD_STORAGE_PC, you must verify some details under Item List > Pricing . For example, the One-Time charges, Discount1, Discount2, and Recurring Net Charges. | All the item details of the Subscription Item can be viewed. |  |

#### Display Provider Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to view the provider contract created by Subscription and to verify the details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist. | The Fiori Launchpad is displayed. |  |
| 2 | Navigate to Display Provider Contract for Sales Billing | Choose the Display Provider Contract for Sales Billing app. | Provider Contract Display screen is displayed. |  |
| 3 | Display Provider Contract | In Sales Billing Provider Contract enter the Provider Contract ID.Choose Continue.NoteProvider Contract can also be viewed from Subscription node in Solution Order Progress as described in Subscription Billing section.Provider Contract can also be viewed under Processing Data of each Subscription item created. | Details of the Provider Contract is displayed. |  |

#### Display Pre-Bill in SAP Subscription Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to view the Pre-Bill which gets generated in Subscription Billing at the end of the Billing Period.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to Subscription Launchpad: [https://revenue.cloud.sap/](https://revenue.cloud.sap/)Click on Sign in | Subscription Home page is displayed. |  |
| 2 | Open Bills | Choose Bills under Subscriptions and Billing catalog. | The list of available bills is displayed. |  |
| 3 | Search for Bill Corresponding to Subscription | Enter the following search criteria:Subscription ID: Subscription ID eg SBXXX | The bill corresponding to the subscription is displayed. |  |
| 4 | View the Bill details | In the Bill screen the following details can be viewed:Bill Status: X days until closedTransfer Status: Not Transferred | Bill details are displayed. |  |
| 5 | Check Bill Items and Charge Details of the Bill Item | Choose Bill Item under Item List to view the details of the Bill List Item.Bill Item and Charge Details can be viewed:Product Name: P-CLD_STORAGE_PCS product for Pricing SchemesBilling Cycle: MonthlyNet Bill Amount: example 200 EUR/USD*100 EUR/USD Activation fee (ONETIME)100 EUR/USD Monthly SEAT Fee (10 x 10 EUR/USD)0 EUR/USD Usage Fee (if no usage has been posted) | Bill Item and Charge Details are displayed. |  |
| 6 | Close Bill to prepare for transfer | Choose Change Status and Choose Close Bill Immediately.Choose Close Bill in the Warning dialog box.Bill Status changes to Manually Closed. | Bill Status changed to Manually Closed. |  |
| 7 | Display and Verify Billing Doc Request | Verify if the Transfer Status is changed to Transferred and the Billing Document request ID is created under the Transfer tab as Successor Documents.In the Billing Doc Request section, Choose Node Details to view the Billing Document Request ID.Note Make a note of Billing Document request ID.User can also navigate to S4 HANA via theSubscription Billing Document Request under Transfer (Sucessor Documents). | Billing Document request ID is displayed. |  |

### Manage Billing Document

#### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity the billing clerk creates an invoice for the solution order items that was released for billing in the previous step. The billing document is created by the billing clerk.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Billing Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Billing Documents(F0798)Billing Due List Items. | The Create Billing Documents screen is displayed. |  |
| 3 | Define Billing Settings | Choose Billing Settings , you can make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ON | The Billing Settings dialog window is displayed.You have maintained the required settings for billing. |  |
| 4 | Search for billing due list | In search filters , provide the BDR ID in SD Document field.Choose Go. | All billing due list items belonging to Solution order should be displayed: |  |
| 5 | Select item(s) for billing | Select row(s) in the Billing Due List created previously and choose Create Billing Documents.Note It is possible to combine all the items in the solution order and create a single invoice, at the same time individual invoice can be created for different items in solution order by choosing the individual billing due list items. | The Create Billing Document pop up is displayed. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, for example current date, then choose OK. | The draft billing document with ID Sxxxxxxxx is displayed. |  |
| 7 | Save Billing Document | On the Manage Billing Document screen, choose Save.Invoice ID xxxxxxxx is displayed , make a note of Invoice ID: __________.Note In case the Billing Due List cannot be combined into a single invoice a Split Analysis button will be displayed. In that case you will have to create individual billing documents. | The system generates an invoice for billing.Billing status of the individual items in the Solution order is updated. |  |

#### Display Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step displays the sales order billing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The Fiori Launchpad is displayed. |  |
| 2 | Access the App | OpenManage Billing Documents (F0797) | The Display Billing Documents screen is displayed. |  |
| 3 | Search the Billing Document Created in Previous Step | Enter <the Billing document number recorded in Create Billing Document step>.Choose GO.Note User can navigate to subscription billing via the Source document in Invoice/Billing Document request. | The billing document is displayed. |  |
| 4 | Display Output | On the Invoice XXXXXXXX: Manage Billing Documents screen, choose Preview. | The Invoice XXXXXXXX screen is displayed. |  |
| 5 | Display Print Preview | Select the output line and choose Display Document. | Print preview for PDF file is displayed. The Solution Order is available on the print form. |  |

### Create Credit Memo with Reference to Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

There are two ways to create a credit memo with reference to an invoice:

- Create a credit memo with reference to the invoice with the corrected amount.
- Create a credit memo with reference to the invoice with the corrected amount and the actual amount.

Procedure

- To create credit memo for an invoice with the corrected amount created in Create Billing Document , refer the instructions provided in 1EZ - Credit Memo Processing scope item.
- To create credit memo for an invoice with the corrected and actual amount created in Create Billing Document, refer the instructions provided in BKL - Invoice Correction Process with Credit Memo scope item.

### Create Debit Memo with reference to Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

There are two ways to create a debit memo with reference to an invoice:

- Create a debit memo with reference to the invoice with the corrected amount.
- Create a debit memo with reference to the invoice with the corrected amount and the actual amount.

Procedure

- To create Debit memo for an invoice with corrected amount created in Create Billing Document, refer the instructions provided in 1F1 - Debit Memo Processing scope item.
- To create Debit memo for an invoice with the corrected and actual amount created in Create Billing Document, refer the instructions provided in BDQ - Invoice Correction Process with Debit Memo scope item.

## Appendix

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
- see-also :: [[09-subscription-billing-and-contract-accounting/test-script-subscription-management-for-software-5sw-ae-sap-s-4hana-cl-part-01]]
- see-also :: [[06-management-accounting/event-based-revenue-recognition-subscription-billing-5dq-ae-test-scrip]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/57Z_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 29,135 chars in the whole document
