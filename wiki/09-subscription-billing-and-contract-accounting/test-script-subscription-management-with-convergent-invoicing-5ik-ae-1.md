---
id: 09-subscription-billing-and-contract-accounting/test-script-subscription-management-with-convergent-invoicing-5ik-ae-1
title: "Test Script: Subscription Management with Convergent Invoicing (5IK_AE) (5IK_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5IK (AE): subscriptions in SAP Subscription Billing, provider contract, pre-bill and convergent invoicing."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/subscription-management-convergent-invoicing]
aliases: [5IK_S4CLD2608_BPD_EN_AE]
keywords: [Subscription Management with Convergent Invoicing, subscription billing, convergent invoicing, create subscriptions, provider contract, pre-bill, test scripts, billable items, test prerequisites, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5IK_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1103
topic: 09-subscription-billing-and-contract-accounting/subscription-management-convergent-invoicing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Subscription Management with Convergent Invoicing (5IK_AE) (5IK_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5IK_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Subscription Management with Convergent Invoicing** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Subscription Management with Convergent Invoicing (5IK_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232856691)

[2 Prerequisites 3](#_Toc232856692)

[2.1 System Access 3](#_Toc232856693)

[2.2 Roles 3](#_Toc232856694)

[2.3 Master Data, Organization Data, and Other Data 3](#_Toc232856695)

[2.4 Additional Manual Configuration 5](#_Toc232856696)

[2.5 Business Conditions 5](#_Toc232856697)

[2.6 Preliminary Steps 5](#_Toc232856698)

[3 Overview Table 7](#_Toc232856699)

[4 Test Procedures 8](#_Toc232856700)

[4.1 Manage Subscription Billing 8](#_Toc232856701)

[4.1.1 Create Subscriptions in SAP Subscription Billing 8](#_Toc232856702)

[4.1.2 Display Subscriptions in SAP Subscription Billing 9](#_Toc232856703)

[4.1.3 Display Provider Contract 11](#_Toc232856704)

[4.1.4 Display Pre-Bill in SAP Subscription Billing 11](#_Toc232856705)

[4.2 Manage Billable Items for Invoicing 12](#_Toc232856706)

[4.2.1 Manage Billable Items 12](#_Toc232856707)

[5 Appendix 14](#_Toc232856708)

## Purpose

Overview

SAP Subscription Billing offers a simplified, automated approach to manage and bill your subscriptions. SAP S/4HANA Cloud Public Edition provides advanced financial processes for invoicing, accounting, and controlling. The scenario combines the capabilities of both solutions to create an integrated subscription management process.

Subscriptions are created via API in SAP Subscription Billing. SAP Subscription Billing manages the subscription lifecycle, charges recurring rates, prices usage data, and prepares the billing data at the end of each billing cycle. The system forwards the billing data to SAP S/4HANA Cloud Public Edition Convergent Invoicing where tax amounts are added and the invoice is created. The invoiced amounts are then available in receivable management, contract accounting, contract-based revenue recognition (CBRR), and controlling.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

The test should be conducted with the following system:

|  |
| --- |
| Note For system details, contact your System Administrator. |

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition System | Accessible via SAP Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP Subscription Billing Tenant | Your system administrator should provide you with a URL and the login details. |

### Roles

You can either use the following standard test users or assign the roles to testers, respectively for the SAP S/4HANA Cloud Public Edition system:

| Business Role | Business Role ID as Delivered by SAP | Log On |
| --- | --- | --- |
| Invoicing Specialist (Convergent Invoicing) | SAP_BR_INVOICING_SPEC_CINV | Your system administrator provides the user and password information. |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Your system administrator provides the user and password information. |
| Accounts Payable and Receivable Accountant (FI-CA) | SAP_BR_APR_ACCOUNTANT_FICA | Your system administrator provides the user and password information. |

### Master Data, Organization Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Business Partner | Sample Customer AE 72 | 33100072 |  |
| Contract Account | CA_AE_72 |  |  |
| Subscription Product | P-CLOUD_COMM | Subscription Product |  |
| Subscription Product | P-CLOUD_SUPPORT | Subscription Product |  |
| Subscription Product | R-ONETIME | Subscription Product |  |
| Subscription Product | R-SEATS | Subscription Product |  |
| Subscription Product | R-TICKETS | Subscription Product |  |
| Sales Organization | 3310 | (Dom. Sales Org AE) |  |
| Company code | 3310 | Company Code 3310 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Reference

| Master Data ID | Description |
| --- | --- |
| 5LP | Create Subscription Product Convergent Invoicing - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/aa533dc467da35b2870faa9ebe1ffec0)

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 2AR - Contract Accounting – Master Data and Basic Functions | Must be run before this test script. |
| 2BG - Convergent Invoicing – Invoice Creation for Usage and Service | Must be run before this test script. |
| 2T3 - Convergent Invoicing – Recurring and One-Off Items | Must be run before this test script. |

### Preliminary Steps

Before you display the Provider Contract, you must ensure that the Profit Center is maintained using the following procedure. Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Table 2: Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The Fiori Launchpad is displayed. |  |
| 2 | Access the Manage Your Solution App | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Configure Define Specifications for Derivation of Standard Account Assignment | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose the Provider Contract group.Choose Configure Define Specifications for Derivation of Standard Account Assignment.Choose Configure. | The Maintain Contract: Determine Standard Account Assignment: Overview screen is displayed. |  |
| 4 | Add Entries for Profit Center | Make the following entries for Sales Org 3310.Profit Center: for example, YB900Segment: for example, 1000_CSave the entry. | The Profit Center is maintained. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The Fiori Launchpad is displayed. |  |
| 2 | Open Define Specification for Derivation of Standard Account Assignment | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Specifications for Derivation of Standard Account Assignment.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Maintain Contract: Determine Standard Account Assignment: Overview screen is displayed. |  |
| 3 | Input parameters | Enter the following information:Sales Org.:3310Profit Center: YB900 (for example)Segment: 1000_C (for example)Save the entry. |  |  |

## Overview Table

This process variant starts with the creation of a subscription.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Subscriptions in SAP Subscription Billing](#unique_10) [page ] 8 |  | Manage Subscriptions | Subscription is created |
| [Display Subscriptions in SAP Subscription Billing](#unique_11) [page ] 9 |  | Subscription | Subscription is displayed |
| [Display Provider Contract](#unique_12) [page ] 11 | Accountant - FICA | Display Provider Contract Display | Provider Contract is displayed |
| [Display Pre-Bill in SAP Subscription Billing](#unique_13) [page ] 11 |  | Subscription | Pre-Bill is displayed |
| [Manage Billable Items](#unique_14) [page ] 12 | Invoicing Specialist | Execute Billing | Invoice is displayed |

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
| 2 | Navigate to Manage Subscriptions | Choose the Manage Subscriptions tile. | Manage Subscriptions page is displayed. |  |
| 3 | Create Subscriptions | Choose Create. | The Create Subscriptions pop up is displayed. |  |
| 4 | Enter Subscription Details | Enter the following details on the pop up screen:Customer: Example, 33100072Product: P-CLOUD_COMMNote If you are using the price calculation scenario, you can use P-CLOUD_STORAGE_PC as the Main Product.Valid From: The current date is set automatically.Initial Fixed Term: This is available only if the Main Product is left blank.Subscription Profile: Example, CI IntegrationChoose Continue. | The subscription is created successfully. |  |
| 6 | Choose Item Instructions | Choose Item List > Product > Subscription Parameters > Seat-Based Monthly Fee and enter a value, for example, 2.If you are using the PCS product (P-CLOUD_STORAGE_PC), you must verify the One-Time Net Charges, Recurring Net Charges, and Usage-Based Charges.Verify the Net Amount and choose Apply. |  |  |

#### Display Subscriptions in SAP Subscription Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to view the subscription created from subscription API and to verify the details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log On to Subscription Launchpad: [https://revenue.cloud.sap/](https://revenue.cloud.sap/)Enter the Tenant , for example, revcloud-dev-eu10-integration-temp18Click on Sign in | Subscriptions home page is displayed. |  |
| 2 | Navigate to Subscriptions | Choose the Subscriptions tile. | Subscriptions page is displayed. |  |
| 3 | Find and display subscription | Choose Subscriptions and Billing Catalog > Subscription :In the search area, enter the Subscription ID in the filter field.Click Go.Choose the relevant the subscription from search result. | The Subscription will be displayed in the search result. |  |
| 4 | Check Subscription header details | Check the following subscription header details at the top :Customer - for example, 33100001Status - ActiveValid From - XXX XX, XXXXExpires On - XXX XX, XXXX | All the details are available in Subscription Billing |  |
| 5 | Check Subscription item details | In the Processing Data list, check for details such as:Subscription ProfilesRelated DocumentsSubscription DatesSnapshot DataIn the Item Details, click on the subscription item to view the complete details of the transaction.Note Note the provider contract ID for further steps.Details like Recurring Charges, Subscription Parameter, and Pricing can be viewed.If you are using a product for Price Calculation Services such as P-CLD_STORAGE_PCS, you must verify some details under the Pricing Item List. For example, the one-time charges, discount1, discount2, and recurring net charges. | All the item details of the subscription item can be viewed. |  |

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

Table 3: Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role FICA Accountant. | The Fiori Launchpad is displayed. |  |
| 2 | Navigate to Manage Provider Contract | Choose Maintain Provider Contract tile | Provider contract display screen is displayed. |  |
| 3 | Display Provider Contract | In Provider Contract, enter the Provider Contract IDChoose Continue | Details of the provider contract is displayed |  |

#### Display Pre-Bill in SAP Subscription Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to view the pre-bill which gets generated in Subscription Billing at the end of the billing period.

Table 4: Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to Subscription Launchpad. Click on Sign in | Subscription Home page is displayed. |  |
| 2 | Open Bills | Choose Manage Billing Data under Subscriptions and Billing catalog. | The list of available bills is displayed |  |
| 3 | Search for Bill Corresponding to Subscription | Enter the following search criteria:Subscription ID: Subscription ID eg SBXXX | The bill corresponding to the subscription is displayed |  |
| 4 | View the Bill Details | On the Manage Billing Data screen, the following details can be viewed:Bill Status: X days until closedBill Transfer Status: Not Transferred | The basic details on the bill is displayed |  |
| 5 | Check Bill Items and Charge Details of the Bill Item | Go to Item List > > Bill Item to view the details of the bill list item:Bill Item and Charge DetailsProduct Name: P-Cloud_COMMBilling Cycle: Monthly on first day of monthNet Item Amount: 200 EUR/USD*100 EUR/USD Activation fee (ONETIME)100 EUR/USD Monthly SEAT Fee (10 x 10 EUR/USD)0 EUR/USD Usage Fee (if no usage has been posted) | Bill Item and Charge Details are displayed |  |
| 6 | Close Bill to Prepare for Transfer | Choose Change Status > Close Bill ImmediatelyChoose Close Bill in the Warning the dialog boxBill status changes to Manually Closed | Bill Status changed to Manually Closed |  |

### Manage Billable Items for Invoicing

#### Manage Billable Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Refer to the following chapters in the test script of scope item [2BG](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/2BG) (Convergent Invoicing – Invoice Creation for Usage and Service) for the detailed billing process:

- Perform Invoicing Process
- Display Invoicing Document (Optional)
- Print Invoicing Document (Optional)

## Appendix

Table 5: Typographic Conventions

| Type Style | Description |
| --- | --- |
| Example | Words or characters quoted from the screen.These include field names, screen titles, pushbuttons labels, menu names, menu paths, and menu options.Textual cross references to other documents. |
| Example | Emphasized words or expressions. |
| Example | Technical names of system objects.These include report names, program names, transaction codes, table names, and key concepts of a programming language when they are surrounded by body text, for example, SELECT and INCLUDE. |
| Example | Output on the screen.This includes file and directory names and their paths, messages, names of variables and parameters, source text, and names off installation, upgrade, and database tools. |
| Example | Exact user entry.These are words or characters that you enter in the system exactly as they appear in the documentation. |
| <Example> | Variable user entry.Angle brackets indicate that you replace these words and characters with appropriate entries to make entries in the system. |
| Example | Keys on the keyboard, for example, F2 or ENTER. |

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
- see-also :: [[09-subscription-billing-and-contract-accounting/convergent-invoicing-invoice-correction-processing-2be-ae-test-script]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5IK_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 22,524 chars in the whole document
