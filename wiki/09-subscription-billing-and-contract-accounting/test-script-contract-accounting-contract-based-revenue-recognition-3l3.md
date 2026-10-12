---
id: 09-subscription-billing-and-contract-accounting/test-script-contract-accounting-contract-based-revenue-recognition-3l3
title: "Test Script: Contract Accounting – Contract-Based Revenue Recognition (3L3_AE) (3L3_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 3L3 (AE): integrating contract accounting with contract-based revenue recognition, with prerequisites and steps."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/fi-ca-contract-based-revenue-recognition]
aliases: [3L3_S4CLD2608_BPD_EN_AE]
keywords: [Contract Accounting with Contract-Based Revenue Recognition, contract-based revenue recognition, contract accounting, provider contracts, revenue accounting transfer, account determination, contract attributes, business roles, convergent invoicing, contract change scenarios]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3L3_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-952
topic: 09-subscription-billing-and-contract-accounting/fi-ca-contract-based-revenue-recognition
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Contract Accounting – Contract-Based Revenue Recognition (3L3_AE) (3L3_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3L3_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Contract Accounting with Contract-Based Revenue Recognition** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Contract Accounting – Contract-Based Revenue Recognition (3L3_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232853121)

[2 Prerequisites 4](#_Toc232853122)

[2.1 System Access 4](#_Toc232853123)

[2.2 Roles 4](#_Toc232853124)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232853125)

[2.4 Business Conditions 6](#_Toc232853126)

[2.5 Additional Manual Configuration 7](#_Toc232853127)

[2.5.1 Contract Attributes Configuration 7](#_Toc232853128)

[2.5.2 Account Determination Configuration 7](#_Toc232853129)

[3 Overview Table 9](#_Toc232853130)

[4 Test Procedures 11](#_Toc232853131)

[4.1 Create Provider Contract with Service Based Product 11](#_Toc232853132)

[4.2 Create Invoicing Documents 12](#_Toc232853133)

[4.3 Transfer Revenue Accounting Items to Revenue Accounting 13](#_Toc232853134)

[4.4 Update Provider Contract (Optional) 14](#_Toc232853135)

[4.5 Transfer Revenue Accounting Items to Revenue Accounting 15](#_Toc232853136)

[4.6 Display Transfer Records 15](#_Toc232853137)

[5 Appendix 17](#_Toc232853138)

[5.1 Process Integration 17](#_Toc232853139)

[5.1.1 Preceding Processes 17](#_Toc232853140)

[5.1.2 Succeeding Processes 17](#_Toc232853141)

## Purpose

Overview

In this process, you integrate contract-based revenue recognition with contract accounting. You can create provider contracts with service-based products and invoice documents. A back-end service transfers revenue accounting items to contract-based revenue recognition. In addition, you can make a change scenario to provider contracts such as upsell, cross sell, down sell, renewal, and so on.

This scope item is used to Integrate Revenue Accounting and Contract Accounting , it can carry out the following activities

- Create Provider Contract with service-based product
- Create invoice document
- Update Provider Contract
- Transfer revenue accounting items to Revenue Accounting
- Display revenue accounting items

The entire end to end process is from 2AR Contract Accounting – Master Data and Basic Functions to create Business Partner/Contract Account (preceding step) to 3KK Contract-Based Revenue Recognition – IFRS to view revenue recognition (succeeding step) .

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
| Administrator (Convergent Invoicing) | SAP_BR_INVOICING_ADMIN_CINV | Administration - Convergent Invoicing | SAP_BR_INVOICING_ADMIN_CINV |  |
| Invoicing Specialist (Convergent Invoicing) | SAP_BR_INVOICING_SPEC_CINV | Convergent Invoicing / Subscription Billing | SAP_BR_INVOICING_SPECIALIST_CINV / SAP_CEC_SPT_SUBSCR_BILLG_SPCLST_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Administrator - Revenue Accounting | SAP_BR_REV_ADMIN | Administration - Revenue Accounting | SAP_BR_REV_ADMIN |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

Table 1: Organizational Data

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  | Company code |
| Company Code Group | 3310 |  |  |

Table 2: Other Data

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Account Determination ID | Y1 |  |  |
| Planning Group / Level | Domestic customers |  |  |
| Material Master | CBPTS001 | Consume-Based Power Tools Subscription |  |
| Material Master | CBPTS003 | CBP Tools Subscr. Lean-relevant for RAR |  |
| Business Partner | BP_AE_99 |  |  |
| Contract Account | CA_AE_99 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 3: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| 31X | Create Product Master of type "Service Product" - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 2AR - Contract Accounting – Master Data and Basic Functions | Must be run before this test script. Business Partner and Contract Account must be created. |
| 2T3 - Convergent Invoicing – Recurring and One-Off Items | The invoice document created by running this test script. |
| 2AR - Setting Up Contract Accounting - Master Data and Basic Functions | Must done before this test script. Communication Arrangement SAP_COM_0167 must be set up. (see details in step Create Communication Arrangement for Finance - Contract Accounting Integration) |
| 3KK - Setting Up Contract-Based Revenue Recognition – IFRS | Must done before the step Transfer Revenue Accounting Items to Revenue Accounting. Communication Arrangement SAP_COM_0701 (Revenue Accounting Integration) must be set up. (see details in step Create Communication Arrangement for Revenue Accounting Integration) |

### Additional Manual Configuration

#### Contract Attributes Configuration

Contract Attributes Configuration is required for all integration scenarios of Revenue Accounting. You need to complete all the configuration steps below in all cases.

To access the configuration activity Contract Attributes Determination:

- If your system is on SAP Central Business Configuration, please log on Project Experience UI and then follow the path Accounting > Sales and Service Accounting > Provider Contracts > Contract-Based Revenue Recognition > Maintain Contract Attribute Business Rules in activity Business Processes. You can also search the configuration activity with ID 105700.
- If your system is not on SAP Central Business Configuration, please log on as BPC_EXPERT and find the configuration activity in app Manage Your Solution (F1241).

After accessing the configuration activity successfully, perform the following configurations:

1. Set up Contract Attributes

This step sets up the Contract Category and Description for Revenue Accounting.

1. Set up Receivable Accounts

This step sets up the receivable account for RAI if the receivable account cannot be retrieved from source component (eg. FI-CA). According to the standard content delivered by SAP, account 12100200 should be assigned to each company which has activated RAR. If account mapping has been performed, then the account which is mapped to 12100200 should be entered here.

1. Set up Revenue Accounts

This step sets up the revenue account for RAI if the revenue account cannot be retrieved from source component (eg: FI-CA). According to the standard content delivered by SAP, account 41005100 should be assigned to each company which has activated RAR. If account mapping has been performed, then the account which is mapped to 41005100 should be entered here.

1. Set up POB Attributes

This step sets up POB Attributes (POB type, Event type, etc.)

1. Set up Standalone Selling Price Attributes

This step sets up Standalone Selling Price for Products.

1. Set up Account Assignments

This step sets up default account assignment.

#### Account Determination Configuration

Account Determination Configuration is only required for the integration scenario of FI-CA. For Universal Revenue Recognition (integration with Sell from Stock, integration with Project and integration with Service Contract) it’s not required.

To access the configuration activity Account Determination:

- If your system is on SAP Central Business Configuration, please log on Project Experience UI and then follow the path Accounting > Sales and Service Accounting > Provider Contracts > Contract-Based Revenue Recognition > Maintain Account Determination Business Rules in activity Business Processes. You can also search the configuration activity with ID 105701.
- If your system is not on SAP Central Business Configuration, please log on as BPC_EXPERT and find the configuration activity in app Manage Your Solution (F1241).

After accessing the configuration activity successfully, perform the following configurations:

1. Set up Account Determination for Accrued Cost

Currently SAP Standard Content has not delivered any GL account for Accrued Cost. If the scenario of Cost Recognition is required, create your own GL account set up the account here.

1. Set up Account Determination for Contract Asset

This step sets up the Contract Asset account for RAR period end posting of revenue recognition. According to the standard content delivered by SAP, account 13711400 should be assigned to each company which has activated RAR. If account mapping has been performed, then the account which is mapped to 13711400 should be entered here.

1. Set up Account Determination for Contract Liability

This step sets up the Contract Liability account for RAR period end posting of revenue recognition. According to the standard content delivered by SAP, account 13701400 should be assigned to each company which has activated RAR. If account mapping has been performed, then the account which is mapped to 13701400 should be entered here.

1. Set up Account Determination for Deferred Cost

Currently SAP Standard Content has not delivered any GL account for Deferred Cost. If the scenario of Cost Recognition is required, create your own GL account set up the account here.

1. Set up Account Determination for Deferred Revenue

Currently there is no standard function delivered by SAP, it's not necessary to set up any accounts here.

1. Set up Account Determination for Early Termination Expense of Cost

Currently SAP Standard Content has not delivered any GL account for Early Termination Expense of Cost. If the scenario of Early Termination is required, create your own GL account set up the account here.

1. Set up Account Determination for Early Termination Expense of Revenue

Currently SAP Standard Content has not delivered any GL account for Early Termination Expense of Revenue. If the scenario of Early Termination is to required, create your own GL account set up the account here.

1. Set up Account Determination for Receivable Adjustment

This step sets up the Receivable Adjustment account for RAR period end posting of revenue recognition. According to the standard content delivered by SAP, account 12102100 should be assigned to each company which has activated RAR. If account mapping has been performed, then the account which is mapped to 12102100 should be entered here.

1. Set up Account Determination for Recognized Cost

Currently SAP Standard Content has not delivered any GL account for Recognized Cost. If the scenario of Cost Recognition is required, create your own GL account set up the account here.

1. Set up Account Determination for Recognized Revenue

This step sets up the Recognized Revenue account for RAR period end posting of revenue recognition. According to the standard content delivered by SAP, account 44420000 should be assigned to each company which has activated RAR. If account mapping has been performed, then the account which is mapped to 44420000 should be entered here.

1. Set up Account Determination for Revenue for Allocation

This step sets up the Revenue for Allocation account for RAR period end posting of revenue recognition. According to the standard content delivered by SAP, account 44421000 should be assigned to each company which has activated RAR. If account mapping has been performed, then the account which is mapped to 44421000 should be entered here.

1. Set up Account Determination for Revenue Adjustment for Linked POB

Currently there is no standard function delivered by SAP, it's not necessary to set up any accounts here.

1. Set up Account Determination for Revenue Adjustment for Unbilled Receivables

Currently there is no standard function delivered by SAP, it's not necessary to set up any accounts here.

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Create a Business Partner [2AR] | Accounts Payable and Receivable Accountant (FI-CA) | Maintain Business Partner (BP) | Business partner can be created with BP role MKK (contract partner). |
| Create a Contract Account [2AR] | Accounts Payable and Receivable Accountant (FI-CA) | Maintain Contract Account (CAA3) | Contract account can be created. |
| Create Provider Contract |  |  | Provider Contract can be created. |
| Option 1: Request Billing Plan Items (Mass Run) [2T3] | Invoicing Specialist (Convergent Invoicing) | Request Billing Plan Items (F3530) | Billable item is created |
| Option 2: Request Billing Plan Items (Individual Run) [2T3] | Invoicing Specialist (Convergent Invoicing) | Request Billing Plan Items - Mass Run (FKKBIXBIP_MA) | Billable item is created |
| Option1: Perform Billing Process (Mass Run) [2T3] | Invoicing Specialist (Convergent Invoicing) | Execute Billing (F3525) | Billing Document is created |
| Option 2: Perform Billing Process (Individual Run) [2T3] | Invoicing Specialist (Convergent Invoicing) | Reverse Billing Plan Item - Business Partner (FKKBIXBIP_REV_S) | Billing Document is created |
| Display Billing Document (Optional) [2T3] | Invoicing Specialist (Convergent Invoicing) | Manage Billing Documents (F2250) | Billing Document is displayed |
| Option 1: Perform Invoicing Process (Mass Run) [2T3] | Invoicing Specialist (Convergent Invoicing) | Execute Invoicing - Business Partner (FKKINV_S) | Invoicing Document is created. |
| Option 2: Perform Invoicing Process (Individual Run) [2T3] | Invoicing Specialist (Convergent Invoicing) | Execute Invoicing - Business Partner (FKKINV_S) | Invoicing Document is created |
| Display Invoicing Document (Optional) [2T3] | Invoicing Specialist (Convergent Invoicing) | Manage Invoicing Documents (F2048) | Invoicing Document is displayed |
| Option 1: Request Billing Plan Items (Mass Run) [2T3] | Invoicing Specialist (Convergent Invoicing) | Execute Billing (F3525) | Billable item is created |
| Option 2: Request Billing Plan Items (Individual Run) [2T3] | Invoicing Specialist (Convergent Invoicing) | Request Billing Plan Items - Business Partner (FKKBIXBIP_S) | Billable item is created |
| [Transfer Revenue Accounting Items to Revenue Accounting](#unique_10) [page ] 13 | Administrator (Convergent Invoicing) | Transfer to Revenue Accounting (F3819) | Transfers revenue accounting items to Revenue Accounting |
| [Display Transfer Records](#unique_11) [page ] 15 | Invoicing Specialist (Convergent Invoicing) | Monitor Transfer Records - Revenue Accounting (F7988) | Display Revenue Accounting Items |

## Test Procedures

In order to create service based product, you need refer to 31X Create Product Master of type "Service Product" - MDS for material CBPTS003.

### Create Provider Contract with Service Based Product

Context

In this activity, you can create provider contract with service-based product.

Prerequisite

Before you run Transfer to Revenue Accounting, make sure that Profit Center is maintained by following these steps:

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Make Specifications | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose the group Provider Contract.Choose the Configuration Step Define Specifications for Derivation of Standard Account Assignment. | The Maintain Contract: Determine Standard Account Assignment: Overview screen is displayed. |  |
| 4 | Add Entry for Profit Center | Make the following entry for Sale Org 3310.Profit Center: YB900 (For example)Save the entry. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Specifications for Derivation of Standard Account Assignment | Go to the Business Processes Configuration app and search for the following activity: Define Specifications for Derivation of Standard Account Assignment.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Maintain Contract: Determine Standard Account Assignment: Overview screen is displayed. |  |
| 3 | Input Parameters | Make the following entry for Sale Org 3310.Profit Center: YB900 (For example)Save the entry. | Entry for Profit Center is added. |  |

Procedure

Refer to step Create Provider Contract in scope item 2AR Contract Accounting – Master Data and Basic Functions for the creation of provider contract with service based product.

### Create Invoicing Documents

Context

In this activity, you can create invoice document with the following items:

- One-off items
- Recurring items

Procedure

Refer to scope item 2T3 Convergent Invoicing – Recurring and One-Off Items, start from step: Request billing plan items to step: Perform invoicing process for the recurring and one-off items and consequent billing and invoicing.

### Transfer Revenue Accounting Items to Revenue Accounting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

Before you run this step, please complete the required set up in Business Conditions and Additional Manual Configuration sections.

Context

In this activity, you can transfer revenue accounting items to Revenue Accounting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Administrator (Convergent Invoicing) role assigned. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Transfer to Revenue Accounting (F3819). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Basic Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Transfer Data to Revenue AccountingJob Name: FI-CA: Transfer Data to Revenue Accounting |  |  |
| 5 | Enter Basic Parameters | Make the following entry and choose Step 3:Start Immediately: <Selected> |  |  |
| 6 | Enter Basic Parameters | In the Running Settings section:Prefix of Run ID: For example, ID0Simulation Run: <not selected>In the Selections Criteria section:Business Partner: <Select Business Partner number>Provider Contract : <Select Contract number>CoCd: 3310 |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, navigate to the new application job by choosing the information icon. | The Job Log screen is displayed. The log should show no errors.The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

### Update Provider Contract (Optional)

Context

In this activity, you can update provider contract with the following change reasons:

- Up-sell

Increase of transaction price and standalone selling price

- Down-sell

Decrease of transaction price and standalone selling price

- Cross sell

Addition of new product that were not included on the initial contract

- Renewal

Extension of the initial contract's end date

- Termination

Could be a partial or full termination, validity or timeslice of products will be updated with termination date

Also, you could update provider contract with up-sell using Postman.

Procedure

Refer to scope item 2AR Contract Accounting – Master Data and Basic Functions for the creation of provider contract.

### Transfer Revenue Accounting Items to Revenue Accounting

Context

In this activity, you can transfer revenue accounting items to Revenue Accounting. To do so, refer to the chapter [Transfer Revenue Accounting Items to Revenue Accounting](#unique_10) [page ] 13.

### Display Transfer Records

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can display revenue accounting items.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Invoicing Specialist (Convergent Invoicing) role assigned. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Monitor Transfer Records - Revenue Accounting (F7988). | The Monitor Transfer Records - Revenue Accounting screen displays. |  |
| 3 | Enter Required Parameters | Make the following entries:Transfer Status: <Choose the status based on your requirement>Business Partner: <Select Business Partner number>Cont.Account: <Select Contract Account number>Contract: <Provider contract> |  |  |
| 4 | Execute | Choose Go. | The Monitor Transfer Records - Revenue Accounting screen displays. The revenue accounting items are listed. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

You may first have completed the following processes and conditions before you start with the test steps:

| Process | Business Condition |
| --- | --- |
| 2AR Contract Accounting – Master Data and Basic Functions | Must be run before the test script. Business Partner and Contract Account must be created. |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 3KK Contract-Based Revenue Recognition – IFRS | Group Ledger IFRS has been setup for the 3310 |
| 3VS Contract-Based Revenue Recognition – US GAAP | Group Ledger US GAAP has been setup for the 3310 |

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
- see-also :: [[06-management-accounting/event-based-revenue-recognition-subscription-billing-5dq-ae-test-scrip]]
- see-also :: [[09-subscription-billing-and-contract-accounting/test-script-contract-accounting-integration-with-sales-documents-43y-a]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3L3_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 30,053 chars in the whole document
