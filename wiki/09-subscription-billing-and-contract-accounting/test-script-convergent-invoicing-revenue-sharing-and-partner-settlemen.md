---
id: 09-subscription-billing-and-contract-accounting/test-script-convergent-invoicing-revenue-sharing-and-partner-settlemen
title: "Test Script: Convergent Invoicing – Revenue Sharing and Partner Settlement (42L_AE) (42L_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 42L: revenue sharing and partner settlement in Convergent Invoicing, from billable items to partner invoicing."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/revenue-sharing-and-partner-settlement]
aliases: [42L_S4CLD2608_BPD_EN_AE]
keywords: ["Revenue Sharing, Partner and Intercompany Settlement", partner settlement, revenue sharing, billable items, convergent invoicing, partner settlement rule, billing process, invoicing process, release partner items, billable item reversal]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/42L_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-996
topic: 09-subscription-billing-and-contract-accounting/revenue-sharing-and-partner-settlement
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Convergent Invoicing – Revenue Sharing and Partner Settlement (42L_AE) (42L_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/42L_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Revenue Sharing, Partner and Intercompany Settlement** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Convergent Invoicing – Revenue Sharing and Partner Settlement (42L_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232854257)

[2 Prerequisites 4](#_Toc232854258)

[2.1 System Access 4](#_Toc232854259)

[2.2 Roles 4](#_Toc232854260)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232854261)

[2.4 Business Conditions 5](#_Toc232854262)

[2.5 Preliminary Steps 6](#_Toc232854263)

[2.5.1 Contract Accounting - Master Data and Basic Functions (2AR) 6](#_Toc232854264)

[2.5.2 Assign Partner Settlement Rule to Contract Account of Partner 6](#_Toc232854265)

[2.5.3 Maintain Amount Calculation Key 7](#_Toc232854266)

[2.5.4 Maintain Master Data ID 10](#_Toc232854267)

[2.5.5 Assign Master Data IDs 11](#_Toc232854268)

[3 Overview Table 14](#_Toc232854269)

[4 Test Procedures 16](#_Toc232854270)

[4.1 Create Billable Items of Customer 16](#_Toc232854271)

[4.1.1 Option 1: Upload Billable Items 16](#_Toc232854272)

[4.1.2 Option 2: Invoke Create Billable Items SOAP API 18](#_Toc232854273)

[4.2 Perform Billing Process for Customer 19](#_Toc232854274)

[4.2.1 Option 1: Perform Billing Process (Mass Run) 20](#_Toc232854275)

[4.2.2 Option 2: Perform Billing Process (Individual Run) 21](#_Toc232854276)

[4.3 Perform Invoicing Process for Customer 22](#_Toc232854277)

[4.3.1 Option 1: Perform Invoicing Process (Mass Run) 22](#_Toc232854278)

[4.3.2 Option 2: Perform Invoicing Process (Individual Run) 23](#_Toc232854279)

[4.4 Partner Billing and Settlement 24](#_Toc232854280)

[4.4.1 Display Billable Item of Partner 24](#_Toc232854281)

[4.4.2 Release Partner Items for Settlement 25](#_Toc232854282)

[4.4.2.1 Option 1: Release Partner Items (Mass Run) 25](#_Toc232854283)

[4.4.2.2 Option 2: Release Partner Items (Individual Run) 27](#_Toc232854284)

[4.4.3 Perform Billing Process for Partner 28](#_Toc232854285)

[4.4.3.1 Option 1: Perform Billing Process (Mass Run) 28](#_Toc232854286)

[4.4.3.2 Option 2: Perform Billing Process (Individual Run) 29](#_Toc232854287)

[4.4.4 Perform Invoicing Process for Partner 30](#_Toc232854288)

[4.4.4.1 Option 1: Perform Invoicing Process (Mass Run) 30](#_Toc232854289)

[4.4.4.2 Option 2: Perform Invoicing Process (Individual Run) 31](#_Toc232854290)

[4.5 Reverse Billable Item of Customer (Optional) 32](#_Toc232854291)

[5 Appendix 34](#_Toc232854292)

[5.1 Process Integration 34](#_Toc232854293)

[5.1.1 Preceding Processes 34](#_Toc232854294)

[5.2 CSV Template Creation 34](#_Toc232854295)

[5.2.1 Data Item Selection for Paid and Unpaid Service of Customer 34](#_Toc232854296)

## Purpose

Overview

This process supports multi-sided business models such as revenue sharing and partner settlement. Based on defined criteria, a consumption or billable item with a specific revenue share can be created and paid to a partner.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data, and business conditions.

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
| Invoicing Specialist (Convergent Invoicing) | SAP_BR_INVOICING_SPEC_CINV | Convergent Invoicing / Subscription Billing | SAP_BR_INVOICING_SPECIALIST_CINV / SAP_CEC_SPT_SUBSCR_BILLG_SPCLST_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Administrator (Convergent Invoicing) | SAP_BR_INVOICING_ADMIN_CINV | Administration - Convergent Invoicing | SAP_BR_INVOICING_ADMIN_CINV |  |
| Accounts Payable and Receivable Accountant (FI-CA) | SAP_BR_APR_ACCOUNTANT_FICA | Contract Accounting | SAP_BR_APR_ACCOUNTANT_FICA |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 2AR- Contract Accounting – Master Data and Basic Functions | Must be run before this test script. Business Partner and Contract Account must be created. |
| 2BG- Convergent Invoicing – Invoice Creation for Usage and Service | Must be deployed before running this test script. |

### Preliminary Steps

#### Contract Accounting - Master Data and Basic Functions (2AR)

Context

This scope item descripts the steps on how to create business partner, contract account, provider contract for Contract Accounts Receivable and Payable (FI-CA). Furthermore, you can create and print correspondence.

Procedure

Complete all the activities descripted in Contract Accounting - Master Data and Basic Functions (2AR) to create master data for customer and partner as below:

Customer:

- Business Partner
- Contract Account

Partner:

- Business Partner
- Contract Account

#### Assign Partner Settlement Rule to Contract Account of Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you assign the Partner Settlement Rule to the contract account of partner you created at previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as a Accounts Payable and Receivable Accountant (FI-CA) | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the SAP Fiori App | Open Maintain Contract Account (CAA3). | The Contract Account Display: Initial Screen displays. |  |
| 3 | Change a Contract Account | Choose Change.Or select menu Menu > Contract Account > Change . | The Contract Account Change: Initial Screen displays. |  |
| 4 | Enter Basic Data | Make the following entries:Contract Acct: <the contract account of partner you created at previous step>Business Partner: <the business partner of partner you created at previous step >Cont. Acct. Cat.: Y1Valid From: <Today’s Date>Choose Continue | The Contract Account Change: General Data screen displays. |  |
| 5 | Assign Partner Settlement Rule | Choose Convergent Invoicing tab and make the entry as below:Partner Settlement Rule: <the partner settlement rule >, for example, S001Choose Save. | The partner settlement rule has been assigned to contract account of partner you created at previous step. |  |

#### Maintain Amount Calculation Key

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you enhance the amount calculation key of S0SAPPSH.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Configuration Expert.. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access App | Open Manage Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution .Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Maintain Calculation Key | On the Configure Your Solution: Realize Phase screen, search Maintain Amount Calculation Key and then choose Enter.Select the line of the item Dependent Items/Partner Settlement and go to the next screen.On the Configuration Your Solution – Cost Posting screen,choose Configure for configuration step Maintain Amount Calculation Key. |  |  |
| 5 | Make Parameters to maintain calculation key | On the Maintain Amount Calculation Key": Change screen, choose the line with the calculation key S0SAPPSH, and then choose Validity.Choose New Entries and make the entries as below:Crcy: <your currency>Valid From: <today’s date>Choose Save to save the validity.Choose the newly added validity and choose Calculation Rules.Confirm the information dialog with message “Entries are not added individually to the change request”.Choose New Entries, on the New Entries: Details of Added Entries screen, make the entries as below:Base Amt Limit: <lower limit for base amount>, for example, 0.Debit/Credit: <Debit or Credit> for example, Debit.Percentage: <your percentage>, for example, 5.Choose Save. | The calculation key S0SAPPSH is enhanced.Note The amount of dependent item will be determined as:Based on the given example, the amount of dependent item = Customer Amount * Percentage. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Maintain Calculation Key | Go to the Business Processes Configuration app and search for the following activity: Maintain Calculation Key(ID 103231).Choose Open Documentation for the line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Make Parameters to create calculation key | On the "Maintain Amount Calculation Key": Change screen, choose the line with the calculation key S0SAPPSH, and then choose Validity.Choose New Entries and make the entries as below:Crcy: <your currency>Valid From: <today’s date>Choose Save to save the validity.Choose the newly added validity and choose Calculation Rules.Confirm the information dialog with message “Entries are not added individually to the change request”.Choose New Entries, on the New Entries: Details of Added Entries screen, make the entries as below:Base Amt Limit: <lower limit for base amount>, for example, 0.Debit/Credit: <Debit or Credit> for example, Debit.Percentage: <your percentage>, for example, 5.Choose Save. | The calculation key S0SAPPSH is enhanced.Note The amount of dependent item will be determined as:Based on the given example, the Amount of Dependent Item = Customer Amount * Percentage. |  |

#### Maintain Master Data ID

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you maintain the Master Data ID.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access App | Choose the Maintain Master Data ID tile. | The Maintain Master Data ID page is displayed. |  |
| 3 | Create Master Data ID | On Maintain Master Data ID screen, choose Create. |  |  |
| 4 | Make Parameters | On the Master Data ID screen, make the entries as below:Description: <the description>Business Partner: <business partner of partner>Contract Account: <contract account of partner>Choose Create.. | The master data ID for partner is created. |  |

#### Assign Master Data IDs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you assign the Master Data IDs.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Configuration Expert. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access App | Open Manage Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution .Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Assign Master Data IDs | On the Configure Your Solution: Realize Phase screen, search Assign Master Data IDs, and then choose Enter.Select the line of the item and go to the next screen.On the Configuration Your Solution – Dependent Items/Partner Settlement screen, choose Configure on the line of configuration step with name Assign Master Data IDs. |  |  |
| 5 | Maintain Parameters | On the Maintain Determine Master Data ID for Dependent Items: Overview screen, choose Create and make the entries as below:Dependent Item Type: <the dependent item type>, for example SPSHAREDep. Item Reason: <the dependent item reason>, for example SROYALTYBillable Item Type: <the billable item type>, for example SPRSCons.Item Type: <the consumption item> , for example: leave it emptyChoose Continue.Master Data ID: <the master data id you created in the previous setup>Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Assign Master Data IDs | Go to the Business Processes Configuration app and search for the following activity: Assign Master Data IDs.Choose the line item in the search result to see more details about this configuration activity.Choose Go to Activity to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Maintain Parameters | On the Maintain Determine Master Data ID for Dependent Items: Overview screen, choose Create and make the entries as below:Dependent Item Type: <the dependent item type>, for example SPSHAREDep. Item Reason: <the dependent item reason>, for example SROYALTYCons.Item Type: <the consumption item> , for example: leave it emptyBillable Item Type: SPRSChoose Continue.Master Data ID: <the master data id you created in the previous setup>Choose Save. |  |  |

## Overview Table

This scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Create Billable Items of Customer |  |  |  |
| [Option 1: Upload Billable Items](#unique_13) [page ] 16 | Invoicing Specialist (Convergent Invoicing) | Upload Billable Items (F4664) | Billable Item of Customer is created. |
| [Option 2: Invoke Create Billable Items SOAP API](#unique_14) [page ] 18 | N/A | N/A | Billable Item of Customer is created. |
| Perform Billing Process for Customer |  |  |  |
| [Option 1: Perform Billing Process (Mass Run)](#unique_15) [page ] 20 | Administrator (Convergent Invoicing) | Execute Billing - Mass Run (F3525) | The billing document of customer is created. |
| [Option 2: Perform Billing Process (Individual Run)](#unique_16) [page ] 21 | Invoicing Specialist (Convergent Invoicing) | Execute Billing - Business Partner (FKKBIX_S) | The billing document of customer is created. |
| Perform Invocing Process for Customer |  |  |  |
| [Option 1: Perform Invoicing Process (Mass Run)](#unique_17) [page ] 22 | Administrator (Convergent Invoicing) | Execute Invoicing - Mass Run (F3524) | The invoicing document of customer is created. |
| [Option 2: Perform Invoicing Process (Individual Run)](#unique_18) [page ] 23 | Invoicing Specialist (Convergent Invoicing) | Execute Invoicing - Business Partner (FKKINV_S) | The invoicing document of customer is created. |
| Partner Billing and Settlement |  |  |  |
| [Display Billable Item of Partner](#unique_19) [page ] 24 | Invoicing Specialist (Convergent Invoicing) | Manage Billable Items (F2621) | The corresponding billable item of partner is displayed. |
| Release Partner Items for Settlement |  |  |  |
| [Option 1: Release Partner Items (Mass Run)](#unique_20) [page ] 25 | Administrator (Convergent Invoicing) | Release Partner Items - Mass Run (F7153) | The partner items were released. Log of application job is displayed. From the log, you can see the result of application job. |
| [Option 2: Release Partner Items (Individual Run)](#unique_21) [page ] 27 | Invoicing Specialist (Convergent Invoicing) | Release Partner Items (FPPARTREL) | The partner item that has billing lock was released. |
| Perform Billing Process for Partner |  |  |  |
| [Option 1: Perform Billing Process (Mass Run)](#unique_22) [page ] 28 | Administrator (Convergent Invoicing) | Execute Billing - Mass Run (F3525) | The billing document of partner is created. |
| [Option 2: Perform Billing Process (Individual Run)](#unique_23) [page ] 29 | Invoicing Specialist (Convergent Invoicing) | Execute Billing - Business Partner (FKKBIX_S) | The billing document of partner is created. |
| Perform Invoicing Process for Partner |  |  |  |
| [Option 1: Perform Invoicing Process (Mass Run)](#unique_24) [page ] 30 | Administrator (Convergent Invoicing) | Execute Invoicing - Mass Run (F3524) | The invoicing document of partner is created. |
| [Option 2: Perform Invoicing Process (Individual Run)](#unique_25) [page ] 31 | Invoicing Specialist (Convergent Invoicing) | Execute Invoicing - Business Partner (FKKINV_S) | The invoicing document of partner is created. |
| [Reverse Billable Item of Customer (Optional)](#unique_26) [page ] 32 | Invoicing Specialist (Convergent Invoicing) | Manage Billable Items (F2621) | The customer billable item is reversed. |

## Test Procedures

This section describes the test procedures for each process step that belongs to this scope item.

### Create Billable Items of Customer

#### Option 1: Upload Billable Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you upload csv file based on the selected main items to generate the billable item of customer, and the billable item of partner which is derived from billable item of customer is created automatically.

|  |
| --- |
| Note Please use the master data of customer to generate the csv file. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad asInvoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose the Upload Billable Items (F4664) tile. | The Upload Billable Items page is displayed. |  |
| 3 | Create Template | In the Upload Billable Items screen, make the following entries as below and choose Create Template.Upload Schema: CSV File for Billable Items |  |  |
| 4 | Choose Billable Item Class | In the Create Template screen, make the entry as below:Choose Billable Item Class: Services |  |  |
| 5 | Choose Record Type | Based on the different service you want to create, please choose corresponding record typeFor unpaid service, you only need to choose Main ItemsFor paid service, you should choose Main Items and Payment Data Items |  |  |
| 6 | Choose Fields for Record Types | Based on the different service you want to create, please choose corresponding fields for Record Type.Please refer to Data Item Selection in the Appendix to choose fields of record type based on the service you want to create.Choose Download Template. | The items were chosen and saved successfully.Note The CSV file template can be created based on paid service and unpaid service.To paid service, the payment data item should be chosen besides main items.Based on the different payment data item selected, the payment card information can be retrieved through CSV file or business partner master data. |  |
| 7 | Edit the local CSV file | Open and edit the copy at your native file system and add value to it accordingly. | Based on the given sequence of main item, payment data item, the values were filled into csv file.Option 1: Add value for unpaid serviceNote There is no need to specify the ContractAccount (Contract Account) if the given business partner contains only one contract account.If you don’t specify CABllbleItmSourceTransId (Source Transaction ID) in the csv file, system will assign one for it.Option 2: Add value for paid serviceNote There is no need to specify the ContractAccount (Contract Account) if the given business partner contains only one contract account.CABllbleItmSourceTransId (Source Transaction ID) is mandatory to be filled at CSV file if Payment Data is used. The Source Transaction ID in Main Item and Payment Data Item should be the same.The payment card must be maintained at business partner if you want to use payment card of business partner for paid service. |  |
| 8 | Import CSV File | In the Upload Billable Items screen, make the entries as below:File Source: Choose Browse and find the file you edited.Choose Open to close the popup dialog of File Upload and upload the file you edited at step6 from native file system to SAP file system. | The file you edited at step 7 was uploaded to SAP system. |  |
| 9 | Read CSV File | Choose Read. | Log is provided to identify the csv file read error.If there is no error, the field and filed value of CSV file can be displayed at Preview section. You also can choose Edit to modify the value as your demands. |  |
| 10 | Load CSV File | Choose the entries you want to upload then choose Upload. | Before load data, you can make the modification to the individual field based on your request. |  |
| 11 | Display Log | In Upload Messages dialog, choose Show Application Log to display log. | From the log, you will see the billable item is created or not. |  |

#### Option 2: Invoke Create Billable Items SOAP API

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create the billable items of customer by invoking the SOAP API of convergent invoicing, and the billable item of partner which is derived from billable item of customer is created automatically.

|  |
| --- |
| Note Before you invoke crate billable items SOAP API. Please make sure the setup guide of Convergent Invoicing: Invoice Creation for Usage and Service (2BG) has been implemented. Please use the master data of Customer to invoke the SOAP API. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Navigate to SAP API HUB | Open web browser and navigate to [https://api.sap.com](https://api.sap.com) | The SAP API hub home page is displayed. |  |
| 2 | Locate API package in SAP S/4HANA Cloud Public Edition | Choose SAP S/4HANA Cloud Public Edition and choose APIs tab. | The API package from SAP S/4HANA Cloud Public Edition is located. |  |
| 3 | Search out create billable items SOAP API | Choose SOAP and search for Convergent Invoicing Billable Items - Create. | The create billable items SOAP API is displayed. |  |

### Perform Billing Process for Customer

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

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Administrator (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose the Execute Billing - Mass Run (F3525) tile. | The Execute Billing - Mass Run page is displayed. |  |
| 3 | Create Application Job | Choose Create to create a new application job. | The New Job: Billing (Mass Creation) page is displayed. |  |
| 4 | Select Template | Make the following entries as below:Job Template: Billing (Mass Creation)Job Name: <job name>Choose Step 2. |  |  |
| 5 | Maintain Schedule Options | Make the following entries as below:Start Immediately: chooseRecurrence Pattern: Single RunChoose Step3. |  |  |
| 6 | Maintain Parameters | Make the following entries as below:Prefix of Run ID: <Prefix of Run ID>Billing Process: <Y001>Contract Account: <The Required Contract Account of Customer>Simulation Run: <Don’t Choose>Billing Date: <The Current Date>Problem Class: <problem class> |  |  |
| 7 | Execute | Choose Schedule. | The job is running immediately. |  |
| 8 | Locate the job from application job list | In the Execute Billing - Mass Run screen, make the following entries as below:Date From-To:: <Today -1/+1 day>Choose Go. | The application job you want to find was located in the application jobs list. |  |
| 9 | Check Log | Choose Image of Log to access located the application job log. | The log of application job is displayed. From the log, you can see the result of application job. |  |

#### Option 2: Perform Billing Process (Individual Run)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing) | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Execute Billing - Business Partner (FKKBIX_S) tile. | The Billing (Individual Creation) page is displayed. |  |
| 3 | Maintain Parameters | In the Billing (Individual Creation), make the following entries as below:Billing Process: <Y001>Billing Date: <The Current Date>Contract Account: <The Required Contract Account of Customer> |  |  |
| 4 | Execute | Choose Execute. |  |  |
| 5 | Choose Billable Item and Create Billing Units | In the Choose Billable Items and Creation of Billing Units dialog, choose Save, until you see the dialog Billing Ended. | A dialog Billing Ended is displayed. |  |
| 6 | Check Billing Document | Choose Continue (Enter) to leave the dialog. |  |  |

### Perform Invoicing Process for Customer

#### Option 1: Perform Invoicing Process (Mass Run)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Administrator (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose app Execute Invoicing - Mass Run (F3524) | The Execute Invoicing - Mass Run page is displayed |  |
| 3 | Create Application Job | Choose Create to create a new application job. | The New Job page is displayed |  |
| 4 | Select Template | Make the following entries as below:Job Template: Invoicing (Mass Creation)Job Name: <job name>Choose Step 2. |  |  |
| 5 | Maintain Schedule Options | Make the following entries as below:Start Immediately: chooseRecurrence Pattern: Single RunChoose Step 3. |  |  |
| 6 | Maintain Parameters | Make the following entries as below:Prefix of Run ID: <Prefix of Run ID>Invoicing Process: Y1Business Partner: <The Required Business Partner of Customer>Contract Account:<The Required Contract Account of Customer>Simulation Run: <Don’t Choose>Document Date: <The Current Date>Posting Date:<The Current Date>Problem Class: <problem class> |  |  |
| 7 | Execute | Choose Schedule. | The job is running immediately. |  |
| 8 | Locate the job from application job list | In the Execute Invoicing - Mass Run screen, make the following entries as below:Date From-To:: <Today -1/+1 day>Choose Go. |  |  |
| 9 | Check Log | Choose Image of Log to locate the application job log. | The log of application job is displayed. From the log, you can see the result of application job. |  |

#### Option 2: Perform Invoicing Process (Individual Run)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Execute Invoicing - Business Partner (FKKINV_S) tile. | The Invoicing (Individual Creation) page is displayed. |  |
| 3 | Maintain Parameters | In the Invoicing (Individual Creation), make the following entries as below:Invoicing Process: Y1Document Date: <The Current Date>Posting Date: <The Current Date>Business Partner: <The Required Business Partner of Customer>Contract Account: <The Required Contract Account of Customer> |  |  |
| 4 | Execute | Choose Execute. | A dialog Selection of Source Documents is displayed. |  |
| 5 | Select Source Documents | On the Selection of Source Documents dialog choose Save. | A dialog Creation of Invoicing Units is displayed if there are more than one source documents to be invoiced. You can choose All Together or All Individually, then choose Save to continue. |  |
| 6 | Post Invoicing Document | In the Save invoicing document? dialog, chooseYes, until you see the dialog Invoicing Ended. If you choose Document, you can check the documents before posting. | A dialog Invoicing Ended is displayed.The invoicing document is posted. |  |
| 7 | Check Invoicing Document | Choose Continue (Enter) to leave the dialog. |  |  |

### Partner Billing and Settlement

Context

Using the partner settlement rule, you specify at what point in time the partner shares can be settled. The system supports the following three options:

1. The time of settlement of the partner items is independent of the time of the creation of the customer invoice.
2. Partner items are not allowed to be settled before the customer invoice is created.
3. Partner items are not allowed to be settled before the due date of the customer invoice.

If you use option 2 and 3, partner items are automatically locked for billing when they are created, by means of the system setting that their target date for billing is set to 12/31/9999. When the customer invoice is created, an order for release of these partner items is created.

You release partner items that have a billing lock through Fiori App of Release Partner Items for Settlement. It sets the target date of billing, depending on the option, to the date the customer invoice was created or to the due date of the customer invoice.

|  |
| --- |
| Note Partner Settlement Rule of S001 (Payment after Customer Invoice + Adjustments) which is using Option2 has been used at this testing script. So, the Billing From of partner billable items will be set to the customer invoicing date after releasing corresponding partner items. |

#### Display Billable Item of Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can display the corresponding billable item of partner that is derived from billable item of customer and the Bill Starting From field is set to 12/31/9999.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the SAP Fiori App | Choose the Manage Billable Items (F2621) tile. |  |  |
| 3 | Maintain Parameters | In the Manage Billable Items screen, make the following entries as below:Business Partner: <the business partner of Partner |  |  |
| 4 | Execute | Choose Go . |  |  |
| 5 | Display Billable item | Choose the search out item. | The billable item is displayed and its Bill Starting From field is set to 12/31/9999. |  |

#### Release Partner Items for Settlement

Purpose

In this step, you release partner items that have a billing lock. You can use Manage Billable Items (F2621) to check the billing date of billable items.

##### Option 1: Release Partner Items (Mass Run)

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
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as an Administrator (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose app Release Partner Items - Mass Run (F7153). | The Release Partner Items - Mass Run screen is displayed. |  |
| 3 | Create Application Job | Choose Create to create a new application job. | The New Job: Release of Partner Items screen is displayed. |  |
| 4 | Select Template | Make the following entries as below:Job Template: Release of Partner ItemsJob Name: <the job name>Choose Step 2. |  |  |
| 5 | Maintain Schedule Options | Make the following entries as below:Start Immediately: chooseRecurrence Pattern: Single RunChoose Step 3. |  |  |
| 6 | Maintain Parameters | Make the following entries as below:Prefix of Run ID: <Prefix of Run ID>Sel.Using Customer: ChooseBPartner: <The Required Business Partner of Customer>Cont.Account: <The Required Contract Account of Customer>Simulation Run: <Don’t Choose>Invoic.Doc.: <the customer invoicing document you created at the previous chapter Perform Invoicing Process for Customer> |  |  |
| 7 | Execute | Choose Schedule. |  |  |
| 8 | Locate the job from application job list | In the Release Partner Items - Mass Run screen, make the following entry:Date From-To:: <Today -1/+1 day>Choose Go. |  |  |
| 9 | Check Log | Choose Image of Log to locate the application job log. | The log of application job is displayed. From the log, you can see the result of application job.You can also check the ready partner items via app Manage Billable Items (F2621). |  |

##### Option 2: Release Partner Items (Individual Run)

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
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as an Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose app Release Partner Items (FPPARTREL). | The Release of Partner Items for Partner Settlement screen is displayed. |  |
| 3 | Maintain Parameters | In the Release of Partner Items for Partner Settlement screen, make the following entries as below:Customer Invoice: ChooseBusiness Partner: <the business partner of customer>Contract Account: <the contract account of customer>Invoicing Document: <the customer invoicing document you created at Perform Invoicing Process for Customer>Simulation Run: <Don't Choose> |  |  |
| 4 | Execute | Choose Execute. | The partner item that has billing lock was released.You can check the ready partner items via app Manage Billable Items (F2621). |  |

#### Perform Billing Process for Partner

##### Option 1: Perform Billing Process (Mass Run)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Administrator (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose the Execute Billing - Mass Run (F3525) app. | The Execute Billing - Mass Run page is displayed. |  |
| 3 | Create Application Job | Choose Create button to create a new application job. | The New Job: Billing (Mass Creation) page is displayed. |  |
| 4 | Select Template | Make the following entries as below:Job Template: Billing (Mass Creation)Job Name: <job name>Choose Step 2. |  |  |
| 5 | Maintain Schedule Options | Make the following entries as below:Start Immediately: chooseRecurrence Pattern: Single RunChoose Step 3. |  |  |
| 6 | Maintain Parameters | Make the following entries as below:Prefix of Run ID: <Prefix of Run ID>Billing Process: SP01Contract Account: <The Required Contract Account of Partner>Simulation Run: <Don’t Choose>Billing Date: <The Current Date>Problem Class: <problem class> |  |  |
| 7 | Execute | Choose Schedule. | The job is running immediately. |  |
| 8 | Locate the job from application job list | In the Execute Billing - Mass Run screen, make the following entries as below:Date From-To:: <Today -1/+1 day>Choose Go. | The application job you want to find was located in the application jobs list. |  |
| 9 | Check Log | Choose Image of Log to access located the application job log. | The log of application job is displayed. From the log, you can see the result of application job. |  |

##### Option 2: Perform Billing Process (Individual Run)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing) | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Execute Billing - Business Partner (FKKBIX_S) app. | The Billing (Individual Creation) page is displayed. |  |
| 3 | Maintain Parameters | In the Billing (Individual Creation), make the following entries as below:Billing Process: SP01Billing Date: <The Current Date>Contract Account: <The Required Contract Account of Partner> |  |  |
| 4 | Execute | Choose Execute. |  |  |
| 5 | Choose Billable Item and Create Billing Units | In the Choose Billable Items and Creation of Billing Units dialog, choose Save, until you see the dialog Billing Ended. | A dialog Billing Ended is displayed. |  |
| 6 | Check Billing Document | Choose Continue (Enter) to leave the dialog. |  |  |

#### Perform Invoicing Process for Partner

##### Option 1: Perform Invoicing Process (Mass Run)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Administrator (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Execute Invoicing - Mass Run (F3524) | The Execute Invoicing - Mass Run page is displayed |  |
| 3 | Create Application Job | Choose Create to create a new application job. | The New Job: Invoicing (Mass Creation) page is displayed |  |
| 4 | Select Template | Make the following entries as below:Job Template: Invoicing (Mass Creation)Job Name: <job name>Choose Step 2. |  |  |
| 5 | Maintain Schedule Options | Make the following entries as below:Start Immediately: chooseRecurrence Pattern: Single RunChoose Step 3. |  |  |
| 6 | Maintain Parameters | Make the following entries as below:Prefix of Run ID: <Prefix of Run ID>Invoicing Process: SPBusiness Partner: <The Required Business Partner of Partner>Contract Account:<The Required Contract Account of Partner>Simulation Run: <Don’t Choose>Document Date: <The Current Date>Posting Date:<The Current Date>Problem Class: <problem class> |  |  |
| 7 | Execute | Choose Schedule. | The job is running immediately. |  |
| 8 | Locate the Job from Application Job List | In the Execute Invoicing - Mass Run screen, make the following entry as below:Date From-To:: <Today -1/+1 day>Choose Go. |  |  |
| 9 | Check Log | Choose Image of Log to locate the application job log. | The log of application job is displayed. From the log, you can see the result of application job. |  |

##### Option 2: Perform Invoicing Process (Individual Run)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Execute Invoicing - Business Partner (FKKINV_S) tile. | The Invoicing (Individual Creation) page is displayed. |  |
| 3 | Maintain Parameters | In the Invoicing (Individual Creation), make the following entries as below:Invoicing Process: SPDocument Date: <The Current Date>Posting Date: <The Current Date>Business Partner: <The Required Business Partner of Partner>Contract Account: <The Required Contract Account of Partner> |  |  |
| 4 | Execute | Choose Execute. | A dialog Selection of Source Documents is displayed. |  |
| 5 | Select Source Documents | On the Selection of Source Documents dialog choose Save. | A dialog Creation of Invoicing Units is displayed if there are more than one source documents to be invoiced. You can choose All Together or All Individually, then choose Save to continue. |  |
| 6 | Post Invoicing Document | In the Save invoicing document? dialog, chooseYes, until you see the dialog Invoicing Ended. If you choose Document, you can check the documents before posting. | A dialog Invoicing Ended is displayed.The invoicing document is posted. |  |
| 7 | Check Invoicing Document | Choose Continue (Enter) to leave the dialog. |  |  |

### Reverse Billable Item of Customer (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you reverse the customer billable item to reverse the customer consumption and partner revenue sharing. The corresponding write-off customer billable item and partner has been generated by system. User can choose to do billing and invoicing against the write-off billable items to write off the customer consumption and partner sharing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose the Manage Billable Items (F2621) tile. |  |  |
| 3 | Maintain Parameters | In the Manage Billable Items screen, make the following entries and choose Go.Source Transaction ID: <the business tranction ID of customer>Business Partner: <the business partner of customer>Contract Account: <the contract account of customer> | The billable item of customer has been located in the list. |  |
| 4 | Reverse Billable Item | In the Manage Billable Items screen, choose the billable item of customer then choose Reverse.In the Reverse screen, make the following entry:Reversal Reason: <the reversal reason>, for example, Reverse Items including Dependent Items (S1)Choose Reverse. | The write-off billable item of customer can be located via Manage Billable Items (F2621).The write-off billable item of partner can be located via Manage Billable Items (F2621). |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can proceed this process.

| Process | Business Condition |
| --- | --- |
| 2AR- Contract Accounting: Business Partner and Contract Account master data | Must be run before the test script. Business Partner and Contract Account must be created. |

### CSV Template Creation

#### Data Item Selection for Paid and Unpaid Service of Customer

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Item of Main Items | Global Field Name | Unpaid Service | Paid Service (Payment Card Data from CSV) | Paid Service(Payment Card Data from Standard Payment Card of business partner) | Paid Service (Payment Card Data from Payment Card of business partner) | Comments |
| BIT_AMOUNT | CABllbleItmAmount | X | X | X | X | Billable Item Amount |
| BIT_CURR | CABllbleItmCurrency | X | X | X | X | Currency |
| GPART | BusinessPartner | X | X | X | X | Business Partner |
| SRCTAID | CABllbleItmSourceTransId | X | X | X | X | Source Transaction ID |
| VKONT | ContractAccount | X | X | X | X | Contract Account |
| DITTYPE | CADependentItemType | X | X | X | X | Dependent Item Type |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Item of Payment Data Items | Global Field Name | Unpaid Service | Paid Service (Payment Card Data from CSV) | Paid Service(Payment Card Data from Standard Payment Card of business partner) | Paid Service (Payment Card Data from Payment Card of business partner) | Comments |
| CCINS | PaymentCardType |  | X |  |  | Payment Card Type |
| CCNUM | PaytCardByPaytServiceProvider |  | X |  |  | Card Number |
| DATAB | CardValidFrom |  | X |  |  | Card valid from |
| DATBI | CardValidTo |  | X |  |  | Card Valid To |
| SRCTAID | CABllbleItmSourceTransId |  | X | X | X | Source Transaction ID |
| PYMET | CAPaymentMethod |  |  | X |  | Payment Method |
| CCARD_ID | CCARD_ID |  |  |  | X | Payment Card ID |

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
- related-to :: [[09-subscription-billing-and-contract-accounting/convergent-invoicing-intercompany-settlement-6wc-ae-1197]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/42L_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 55,466 chars in the whole document
