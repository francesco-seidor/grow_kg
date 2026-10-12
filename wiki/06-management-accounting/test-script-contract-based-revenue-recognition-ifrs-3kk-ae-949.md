---
id: 06-management-accounting/test-script-contract-based-revenue-recognition-ifrs-3kk-ae-949
title: "Test Script: Contract-Based Revenue Recognition – IFRS (3KK_AE) (3KK_S4CLD2608_BPD_EN_AE)"
description: "S/4HANA Cloud 2608 (AE) test script, scope item 3KK: Universal and Contract-Based Revenue Recognition (IFRS 15), prerequisites and Fiori test steps."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/contract-based-revenue-recognition]
aliases: [3KK_S4CLD2608_BPD_EN_AE]
keywords: [Contract-Based Revenue Recognition (Universal Revenue…, revenue recognition, universal revenue recognition, contract-based revenue recognition, event-based revenue recognition, revenue accounting items, revenue contracts, account determination, contract attributes, scope item prerequisites]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3KK_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-949
topic: 06-management-accounting/contract-based-revenue-recognition
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Contract-Based Revenue Recognition – IFRS (3KK_AE) (3KK_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3KK_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Contract-Based Revenue Recognition (Universal Revenue Recognition)** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Contract-Based Revenue Recognition – IFRS (3KK_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232853081)

[2 Prerequisites 4](#_Toc232853082)

[2.1 System Access 4](#_Toc232853083)

[2.2 Roles 4](#_Toc232853084)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232853085)

[2.4 Additional Manual Configuration 6](#_Toc232853086)

[2.4.1 Contract Attributes Configuration 6](#_Toc232853087)

[2.4.2 Account Determination Configuration 7](#_Toc232853088)

[2.4.3 Universal Revenue Recognition Settings 8](#_Toc232853089)

[2.5 Business Conditions 8](#_Toc232853090)

[2.5.1 Integration with FI-CA 9](#_Toc232853091)

[2.5.2 Integration with Sell from Stock (Universal Revenue Recognition) 9](#_Toc232853092)

[2.5.3 Integration with Project Based Services (Universal Revenue Recognition) 9](#_Toc232853093)

[2.5.4 Integration with Service Documents (Universal Revenue Recognition) 10](#_Toc232853094)

[2.5.5 Integration with Provider Contracts for Sales Billing (Universal Revenue Recognition) 10](#_Toc232853095)

[3 Overview Table 11](#_Toc232853096)

[4 Test Procedures 13](#_Toc232853097)

[4.1 Universal Revenue Recognition 13](#_Toc232853098)

[4.1.1 Manage Revenue Accounting Items (Error Handling) 13](#_Toc232853099)

[4.1.2 Manage Revenue Contracts 14](#_Toc232853100)

[4.1.3 Check Event-Based Revenue Recognition Data 15](#_Toc232853101)

[4.1.3.1 Check Data of Event-Based Revenue Recognition – Sales Orders (APP Version2) 15](#_Toc232853102)

[4.1.3.2 Check Data of Event-Based Revenue Recognition – Projects 16](#_Toc232853103)

[4.1.3.3 Check Data of Event-Based Revenue Recognition – Service Documents 17](#_Toc232853104)

[4.1.3.4 Check Data of Event-Based Revenue Recognition – Provider Contracts 18](#_Toc232853105)

[4.1.4 Combine Revenue Contracts (Optional) 19](#_Toc232853106)

[4.1.5 Manage Real-Time Revenue Recognition Issues 20](#_Toc232853107)

[4.1.6 Run Revenue Recognition – Revenue Contracts 21](#_Toc232853108)

[4.1.7 Manage Revenue Recognition Issues – Revenue Contract (Optional) 22](#_Toc232853109)

[4.1.8 Display Line Items in General Ledger (Optional) 23](#_Toc232853110)

[4.1.9 Check Document Flow (Optional) 24](#_Toc232853111)

[4.2 Contract Based Revenue Recognition 25](#_Toc232853112)

[4.2.1 Open and Close Revenue Accounting Period 25](#_Toc232853113)

[4.2.2 Manage Revenue Accounting Items 26](#_Toc232853114)

[4.2.3 Overview, Monitor and Manage Revenue Contracts 27](#_Toc232853115)

[4.2.4 Error Handling 29](#_Toc232853116)

[4.2.5 Manual Processing (Optional) 32](#_Toc232853117)

[4.2.6 Verification and Explanation 34](#_Toc232853118)

[4.2.7 Periodic Activities – Revenue Administrator 36](#_Toc232853119)

[4.2.8 Disclosures and Analytics 38](#_Toc232853120)

## Purpose

Overview

The scope item enables you to manage revenue recognition in accordance with IFRS 15, applying the five-step model. It forms the foundation of Universal Revenue Recognition, which integrates the Event-Based Revenue Recognition and Contract-Based Revenue Recognition functionalities.

With Universal Revenue Recognition activated, in scenarios where bundles of customer projects, sales orders, or service contracts are sold, revenue contracts are automatically created from the objects deemed relevant for revenue accounting and corresponding performance obligations in each revenue contract are generated based on the items within these relevant objects. In addition, the revenue contracts generated automatically can be combined together according to the business requirements. Revenue is allocated across the performance obligations based on the standalone selling price and contractual price. As costs are posted, such as through goods issue posting, the matching revenue is recognized in real time, taking advantage of existing Event-Based Revenue Recognition capabilities.

In scenarios where Contract Accounting – Contract-Based Revenue Recognition (3L3) is operational, it aids in revenue accounting for revenue contracts and performance obligations that are created based on provider contracts. Furthermore, it supports the integration with external operational systems, using an API to create and update revenue contracts.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data, and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/3KK_S4CLD2602_BPD_EN_AE.docx) ). |

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
| Revenue Accountant | SAP_BR_REV_ACCOUNTANT | Revenue Accounting / Sales and Balancing | SAP_BR_REV_ACCOUNTANT / SAP_OILPRA_SPT_SABL_PC |  |
| Administrator - Revenue Accounting | SAP_BR_REV_ADMIN | Administration - Revenue Accounting | SAP_BR_REV_ADMIN |  |
| Cost Accountant - Sales | SAP_BR_SALES_ACCOUNTANT | Sales Accounting | SAP_BR_SALES_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Material | URR_MAT1_NORM | URR Test Material 1 NORM | This material is used in URR Sell from Stock integration scenario |
| Material | URR_MAT2_NORM | URR Test Material 2 NORM | This material is used in URR Sell from Stock integration scenario |
| Material | URR_MAT1_NORM | URR Test Material 1 NORM | This material is used in URR Sell from Stock integration scenario |
| Material | URR_MAT1_SERV | URR Test Material1 TAD | This material is used in URR Sell from Stock integration scenario |
| Material | URR_FPPRJ_1 | URR Test Material Fix Price Customer Proj. | This material is used in URR Customer Project integration scenario |
| Material | URR_SRVCONT1 | URR Test Material Service Contract | This material is used in URR Service Contract integration scenario |
| Plant | 3310 |  |  |
| Sales Organization | 3310 |  |  |
| Distribution Channel | 10 |  |  |
| Division | 00 |  |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| 7R8 | Create Material Master for Universal Revenue Recognition |

### Additional Manual Configuration

Before you can test this scope item, you need to have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item (refer to the link below) and the manual configuration tasks described in this section. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you.

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/c9bfc55036e51297c4f31f7bd42bc2b9)

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

For more information, please refer to the guide document of this scope item:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/c9bfc55036e51297c4f31f7bd42bc2b9)

#### Universal Revenue Recognition Settings

If you are going to use function Universal Revenue Recognition, please access following URL for Product Assistant document and follow the instructions in the document for manual configurations:

[Configuration Activities](https://help.sap.com/docs/SAP_S4HANA_CLOUD/89d896ca9cd64318b1667df5ec00e4b2/c0617e6a13df49c291420ab8098a1060.html?version=latest)

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 1GA - Accounting and Financial Close – Group Ledger IFRS | The test script must be executed in its entirety to set up the Group Ledger IFRS. |
| 2VA - Accounting and Financial Close – Group Ledger US GAAP | The test script must be executed in its entirety to set up the Group Ledger US GAAP. |

Contract-Based Revenue Recognition can be integrated with following source components:

- FI-CA (Contract Accounting and Invoicing)
- Generic Enterprise Services of Optimized Inbound Processing (integration with remote system)
- Sell from Stock (Universal Revenue Recogntion)
- Project based Services (Universal Revenue Recogntion)
- Service Documents (Universal Revenue Recogntion)

Additional scope items will be required to enable the integration. However these scope items are not the prerequisite of activation of 3KK, but are the prerequisite to enable the integration with source components.

#### Integration with FI-CA

Prerequisite Scope Item for integration:

- 2AR - Contract Accounting – Master Data and Basic Functions
- 2T3 - Convergent Invoicing – Recurring and One-Off Items
- 3L3 - Contract Accounting – Contract-Based Revenue Recognition

#### Integration with Sell from Stock (Universal Revenue Recognition)

Prerequisite Scope Item for integration:

- BD9 - Sell from Stock
- 1K2 - Event-Based Revenue Recognition – Sell from Stock
- 33M - Event-Based Revenue Recognition – Sell from Stock – IFRS
- 1F1 - Debit Memo Processing
- 1EZ - Credit Memo Processing

#### Integration with Project Based Services (Universal Revenue Recognition)

Prerequisite Scope Item for integration:

- J11 - Customer Project Management – Project-Based Services
- 4E9 - Project Billing – Project-Based Services
- 1IL - Event-Based Revenue Recognition – Project-Based Services
- 1P0 - Event-Based Revenue Recognition – Project-Based Services – IFRS

#### Integration with Service Documents (Universal Revenue Recognition)

Prerequisite Scope Item for integration:

- 3MO - Service Contract Management
- 4GG - Credit and Debit Memo Processing for Service Management
- 3M3 - Event-Based Revenue Recognition – Service Documents
- 3M4 - Event-Based Revenue Recognition – Service Documents – IFRS

#### Integration with Provider Contracts for Sales Billing (Universal Revenue Recognition)

Prerequisite Scope Item for integration:

- 57Z - Subscription Management with Sales Billing
- 5DQ - Event-Based Revenue Recognition – Subscription Billing
- 5DR - Event-Based Revenue Recognition – Subscription Billing – IFRS

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 2: Universal Revenue Recognition

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Manage Revenue Accounting Items (Error Handling)](#unique_17) [page ] 13 | Administrator - Revenue Accounting | Manage Revenue Accounting Items (F4270) | Revenue Accounting Items are checked and reviewed. |
| [Manage Revenue Contracts](#unique_18) [page ] 14 | Revenue Accountant | Manage Revenue Contracts - Old Version (F3883) | Revenue Contracts aree manully fulfilled and combined. |
| [Check Event-Based Revenue Recognition Data](#unique_19) [page ] 15 | Cost Accountant - Sales | Event-Based Revenue Recognition - Sales Orders (F2441A)Event-Based Revenue Recognition - Projects (F4767)Event-Based Revenue Recognition - Service Documents (F6007) | The data of Event-Based Revenue Recognition are checked. |
| [Combine Revenue Contracts (Optional)](#unique_20) [page ] 19 | Revenue Accountant | Combine Revenue Contracts (F4069) | Revenue Contracts are combined. |
| [Manage Real-Time Revenue Recognition Issues](#unique_21) [page ] 20 | Cost Accountant - Sales | Manage Real-Time Revenue Recognition Issues (F4101) | All errors are addressed prior to the month end revenue recognition month end process. |
| [Run Revenue Recognition – Revenue Contracts](#unique_22) [page ] 21 | Cost Accountant - Sales | Run Revenue Recognition - Revenue Contracts (F7347) | Event-based revenue recognition for Revenue Contracts are run. |
| [Display Line Items in General Ledger (Optional)](#unique_23) [page ] 23 | Cost Accountant - Sales | Event-Based Revenue Recognition - Sales Orders (F2441A)Event-Based Revenue Recognition - Projects (F4767)Event-Based Revenue Recognition - Service Documents (F6007) | Line Items in General Ledger are displayed. |
| [Check Document Flow (Optional)](#unique_24) [page ] 24 | Revenue Accountant | Document Flow - Performance Obligations (F4423) | Document flow is displayed. |

Table 3: Contract Based Revenue Recognition

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Open and Close Revenue Accounting Period](#unique_25) [page ] 25 | Revenue Accountant | Open and Close Revenue Accounting Period (S_RGK_10000007) | Revenue accounting periods are open. |
| [Manage Revenue Accounting Items](#unique_26) [page ] 26 | Administrator - Revenue Accounting | Manage Revenue Accounting Items (F4270) | Revenue Accounting Items are error-free. |
| [Overview, Monitor and Manage Revenue Contracts](#unique_27) [page ] 27 | Revenue Accountant | Revenue Accounting Overview (F4067) | Revenue Contracts details are displayed. |
| [Error Handling](#unique_28) [page ] 29 | Administrator - Revenue Accounting | Clean Up Productive Data (F5728) | Errors in Contract Based Revenue Recognition are handled. |
| [Manual Processing (Optional)](#unique_29) [page ] 32 | Revenue Accountant | Manual Fulfillment (F3881) | POB is fulfilled manually. |
| [Verification and Explanation](#unique_30) [page ] 34 | Revenue Accountant | Revenue Schedule (F3882) | Revenue explanation is displayed. |
| [Periodic Activities – Revenue Administrator](#unique_31) [page ] 36 | Administrator - Revenue Accounting | Transfer Revenue (F3879) | Contract asset, contract liability, recognized revenue, revenue allocation and acquisition cost are calculated and posted to GL. |
| [Disclosures and Analytics](#unique_32) [page ] 38 | Revenue Accountant | Disaggregation of Recognizable Revenue (FARR_DIS_REC_REVENUE (FARR_DIS_REC_REVENUE)) | Analytical report is deispalyed. |

## Test Procedures

This section describes the test procedures for each process step that belongs to this scope item.

### Universal Revenue Recognition

This section describes the test procedures for Universal Revenue Recognition. Before start the test procedures of this section, please ensure integration with Sales & Distribution – URR, integration with Projects – URR and integration with Provider Contract has been enabled, transactions (eg: shipments, invoices) has been completed and relevant documents have been created.

#### Manage Revenue Accounting Items (Error Handling)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Revenue Administrator will check Revenue Accounting Items generated in Revenue Accounting after receiving the data from source component and will perform error handling if there is any issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Administrator - Revenue Accounting (REV_ADMIN). |  |  |
| 2 | Access App | Open Manage Revenue Accounting Items (F4270). | The user enters the initial screen of the APP. |  |
| 3 | Input values for search criteria in filter to search items to be processed | In the initial screen of the Manage Revenue Accounting Items app, enter values for search criteria :For example:Item Status: PostponedCompany Code: 3310Click Go to search the items with the search criteria. | The user will get the list of items which meats the search criteria. |  |
| 4 | Select the item(s) and check the Application Log | Select the item(s) by checking the box of the line item and click “Application Log” on the title of the list to display the Application Log which provides the details of the error analysis (such as “Error in receivables account determination”,etc).Solve the issue according to the detail information provided by the Application Log. | Issue of the incorrect Revenue Accounting Items has been solved. |  |
| 5 | Select the item(s) and reprocess the Revenue Accounting Item(s) | Select the item(s) by checking the box of the line item and click “Process” to reprocess the Revenue Accounting Item(s) with error previously. If issue has been solved in last test step, the revenue accounting item(s) will be processed successfully and the status of the item will be change to “Processed”. | Revenue Accounting Items with error have been reprocessed successfully and the status of the items are changed to “Processed”. |  |

#### Manage Revenue Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Revenue Accountant will check revenue contract details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Revenue Accountant (REV_ACCOUNTANT). |  |  |
| 2 | Access App | Open Manage Revenue Contracts - Old Version (F3883). | The user enters the initial screen of the APP. |  |
| 3 | Input Selection Criteria and Search Revenue Contract | Input following selection criteria and choose Go:Company Code: 3310Revenue Contract ID: <Leave blank> | Line item for the Revenue Contract will be displayed in section Result List. |  |
| 4 | Enter Detailed Screen of the Revenue Contract | Click a line item of the Revenue Contracts list. | The user enters the detailed screen of Revenue Contract. |  |
| 5 | Review Contract Detailed Info | Review the Revenue Contract detailed information. The user will need to take a note of the Revenue Contract ID and the Performance Obligation ID for the check in follow-on testing steps. | Revenue Contract detailed information is displayed. |  |

#### Check Event-Based Revenue Recognition Data

For different source component integrated with Universal Revenue Recognition, user will need to run different APP to check the data of Event-Based Revenue Recognition

##### Check Data of Event-Based Revenue Recognition – Sales Orders (APP Version2)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Cost Accountant - Sales will check the URR data of event-based revenue recognition for sales orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales (SALES_ACCOUNTANT). | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Event-Based Revenue Recognition - Sales Orders (F2441A) (Version 2) . | The user enters the initial screen of the APP. |  |
| 3 | Search the Sales Order to be checked | In the initial screen of the app, enter values for search criteria :For example:Company Code: 3310Revenue Recognition Key: SFSEPClick Go to search the Sales Order with the search criteria. | Sales Order will be displayed in a list. |  |
| 4 | Check data created in EBRR (Event-Based Revenue Recognition) | Click the line item to select the Sales Order. Click on “Set Parameters” and in the popup window input the current period/fiscal year and input “2L” for Ledger, then click Apply.Check the header for the Revenue Contract ID and the Performance Obligation ID, make sure they are consistent with the data got in previous test step ([Manage Revenue Contracts](#unique_18) [page ] 14 step 5). | Data created in EBRR is displayed correctly and is consistent. |  |

##### Check Data of Event-Based Revenue Recognition – Projects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Cost Accountant - Sales will check the URR data of event-based revenue recognition for projects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales (SALES_ACCOUNTANT). | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Event-Based Revenue Recognition - Projects (F4767). | The user enters the initial screen of the APP. |  |
| 3 | Enter selection criteria and search Projects | In the initial screen of the app, enter values for search criteria :For example:Company Code: 3310Click Go to search the Projects with the search criteria. | Projects will be displayed in a list. |  |
| 4 | Check data created in EBRR (Event-Based Revenue Recognition) | Click the line item to select the Project Billing Element. Click on “Set Parameters” and in the popup window input the current period/fiscal year and input “2L” for Ledger, then click Apply.Check the header for the Revenue Contract ID and the Performance Obligation ID, make sure they are consistent with the data got in previous test step ([Manage Revenue Contracts](#unique_18) [page ] 14 step 5). | Data created in EBRR is displayed correctly and is consistent. |  |

##### Check Data of Event-Based Revenue Recognition – Service Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Cost Accountant - Sales will check the data of event-based revenue recognition for Service Contracts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales (SALES_ACCOUNTANT). |  |  |
| 2 | Access App | Open Event-Based Revenue Recognition - Service Documents (F6007). | The user enters the initial screen of the APP. |  |
| 3 | Enter Search Criteria to Search the Service Contracts | In the initial screen of the app, enter values for search criteria :For example:Company Code: 3310Service Document Type: SC1Click Go to search the Sales Order with the search criteria. | Service Contracts will be displayed in a list. |  |
| 4 | Check Data Created in EBRR (Event-Based Revenue Recognition) | Click the line item to select the Service Contract. Click on “Set Parameters” and in the popup window input the current period/fiscal year and input “2L” for Ledger, then click Apply.Check the header for the Revenue Contract ID and the Performance Obligation ID, make sure they are consistent with the data got in previous test step ([Manage Revenue Contracts](#unique_18) [page ] 14 step 5). | Data created in EBRR is displayed correctly and is consistent. |  |

##### Check Data of Event-Based Revenue Recognition – Provider Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Cost Accountant - Sales will check the data of event-based revenue recognition for Provider Contracts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales (SALES_ACCOUNTANT). |  |  |
| 2 | Access App | Open Event-Based Revenue Recognition – Provider Contracts(F5406). | The user enters the initial screen of the APP. |  |
| 3 | Enter Search Criteria to Search the Provider Contract | In the initial screen of the app, enter values for search criteria :For example:Company Code: 3310Click Go to search the provider contract with the search criteria. | Service Contracts will be displayed in a list. |  |
| 4 | Check Data Created in EBRR (Event-Based Revenue Recognition) | Click the line item to select the Provider Contract item. Click on “Set Parameters” and in the popup window input the current period/fiscal year and input “2L” for Ledger, then click Apply.Check the header for the Revenue Contract ID and the Performance Obligation ID, make sure they are consistent with the data got in previous test step [Manage Revenue Contracts](#unique_18) [page ] 14 step 5). | Data created in EBRR is displayed correctly and is consistent. |  |

#### Combine Revenue Contracts (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Revenue Accountant will perform revenue contracts combination.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Revenue Accountant (REV_ACCOUNTANT). |  |  |
| 2 | Access App | Open Combine Revenue Contracts (F4069). | The user enters the initial screen of the APP.This step is optional. Perform revenue contracts combination if necessary. |  |
| 3 | Input Selection Criteria and Search Revenue Contract | Input selection criteria or leave blank to select all, then choose Go. | Revenue Contracts are listed. |  |
| 4 | Combine Revenue Contract | Select the revenue contracts to be combined and then choose Combine Contracts. In the pop-up window, enter the target Revenue Contract (the main contract you want to combine other contracts to), and enter the business change reason and effective data, then choose Save. | Revenue Contracts are combined. |  |

#### Manage Real-Time Revenue Recognition Issues

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

During cost or revenue posting on the cost object, errors that stop real time revenue postings can occur. This activity allows you to review these posting entries where no corresponding real time revenue recognition posting exists and make the necessary corrections. All errors must be addressed prior to the month end revenue recognition month end process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. (SALES_ACCOUNTANT). |  |  |
| 2 | Access App | Open Manage Real-Time Revenue Recognition Issues (F4101). |  |  |
| 3 | Enter Selection Criteria | Make the following entries:Fiscal Year Period: <mm.yyyy>Company Code: 3310Choose the Adapt Filters button and in the dialog box that appears, choose Go. | No data found indicates that there are no issues. If issues are shown, review and process corrections.Tip To download the issue list, make your filter selections and select Show Error Summary. From the list, you can choose the Download button. |  |

#### Run Revenue Recognition – Revenue Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Cost Accountant – Sales will run the event-based revenue recognition for Revenue Contracts generated by Universal Revenue Recognition integration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales (SALES_ACCOUNTANT). | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Run Revenue Recognition - Revenue Contracts (F7347). | The Run Revenue Recognition – Revenue Contracts view displays. |  |
| 3 | New Job | Choose the Create button. | The New Job view displays. |  |
| 4 | Enter Selection Criteria | Make the following entries and choose the Schedule button:Job Template: Run Revenue Recognition – Revenue ContractJob Name: <Enter a description or leave the default description> | Section step 2 “Schedule Options” is displayed |  |
| 5 | Input data in step 2 “Schedule Options” | Enter parameters as following in Step 2:Start Immediately: <Checked>Job Start (Local Time): <defaulted by system and not editable>Click Step 3 to continue. | Section step 3 “Parameters” is displayed. |  |
| 6 | Input data in step 3 “Parameters” | Enter parameters as following in Step 3:Select Fixed Period. In To Fiscal Period/Year, enter <mm/yyyy>Or select Dynamic Period. In To Dynamic Fiscal Period/Year, select from drop down, for example CURRENT (Current Fiscal Period).Company Code: 3310Ledger: 2LClick Schedule to create the job.Note This program records all events, such as errors and warnings, in an application log. The application log is displayed each time when the program finishes. | Job is created.The effective changes for assigning general ledger accounts to revenue accounting contracts are saved in the database after the accounts have been redetermined for the revenue accounting contract. |  |

#### Manage Revenue Recognition Issues – Revenue Contract (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Cost Accountant – Sales will check and reprocess revenue recognition issues of revenue contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales (SALES_ACCOUNTANT). | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Revenue Recognition Issues - Revenue Contracts (F7557). | The Manage Revenue Recognition Issues - Revenue Contracts initial screen displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose the Go button:To Fiscal Period/Year: <ppp/yyyy>Company Code: 3310Ledger: 2L | List of Revenue Recognition Issues is displayed . |  |
| 4 | Display Error Summary | Click Error(x) of a line item in column Status to display the error summary. | Error summary is displayed. |  |
| 5 | Simulate Reprocessing the Revenue Recognition Issues | Select a line item and choose Simulate to simulate reprocessing the revenue recognition issues. | Reprocessing is simulated. |  |
| 6 | Reprocess the Revenue Recognition Issues | Select a line item and choose “Reprocess” to reprocess the revenue recognition issues. | Revenue recognition issues are reprocessed. |  |

#### Display Line Items in General Ledger (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Cost Accountant – Sales will display and check the GL documents related to the Revenue Contracts generated by Univesial Revenue Recognition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. (SALES_ACCOUNTANT). |  |  |
| 2 | Access App | Open Event-Based Revenue Recognition - Sales Orders (F2441A) or open Event-Based Revenue Recognition - Projects (F4767) or open Event-Based Revenue Recognition - Service Documents (F6007). | The user enters the initial screen of the APP. |  |
| 3 | Enter Selection Criteria | Input selection criteria and choose Go:For example:Company Code: 3310 |  |  |
| 4 | Select Line Item and Navigate to GL Document Line Items View | Select a line item and choose Related Apps and from the drop down list select GL Account Line Items. | System will navigate the user to the screen of Display Line Items in General Ledger. |  |

#### Check Document Flow (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Revenue Accountant will check document flow for revenue contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Revenue Accountant (REV_ACCOUNTANT). |  |  |
| 2 | Access App | Open Document Flow - Performance Obligations (F4423). | The user enters the initial screen of the APP. |  |
| 3 | Input Selection Criteria | Input selection criteria and choose Go:Company Code: 3310Account Principle: IFRS | Line item for the Performance Obligations will be displayed. |  |
| 4 | Select Line Item and display the document flow | Click Line Item to display the document flow. | Document flow is displayed. |  |

### Contract Based Revenue Recognition

#### Open and Close Revenue Accounting Period

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Revenue Accountant will open/close revenue accounting period and check revenue contract details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Revenue Accountant (REV_ACCOUNTANT). |  |  |
| 2 | Access App | Open Open and Close Revenue Accounting Period (S_RGK_10000007). | The user enters the initial screen of the APP. |  |
| 3 | Close Old Period in Revenue Accounting | In the initial screen of the Open and Close Revenue Accounting Period app, change the line item as following and choose Save:Company Code: 3310Account Principle (AccP): IFRSFrom Fiscal Year (Fr. F. Year): <Fiscal Year to be tested (eg:2024)>From Period (Fr. Period): <Period to be tested (eg:3)>Status: OpenAfter data has been saved successfully, quit this app by choosing Exit. | You will open the period (eg: 2024.3) and all the periods after are also opened.All periods before are closed. |  |

#### Manage Revenue Accounting Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Revenue Administrator will check Revenue Accounting Items generated in Revenue Accounting after receiving the data from source component and will perform error handling if there is any issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Revenue Accounting (REV_ADMIN). |  |  |
| 2 | Access App | Open Manage Revenue Accounting Items (F4270). | The user enters the initial screen of the APP. |  |
| 3 | Input Values for Search Criteria in Filter to Search items to be Processed | In the initial screen of the Manage Revenue Accounting Items app, enter values for search criteria :For example:Item Status: PostponedCompany Code: 3310Click Go to search the items with the search criteria. | The user will get the list of items which meats the search criteria. |  |
| 4 | Select the item(s) and Check the Application Log | Select the item(s) by checking the box of the line item and click Application Log on the title of the list to display the Application Log which provides the details of the error analysis (such as “Error in receivables account determination”,etc).Solve the issue according to the detail information provided by the Application Log. | Issue of the incorrect Revenue Accounting Items has been solved. |  |
| 5 | Select the Item(s) and Reprocess the Revenue Accounting Item(s) | Select the item(s) by checking the box of the line item and click Process to reprocess the Revenue Accounting Item(s) with error previously. If issue has been solved in last test step, the revenue accounting item(s) will be processed successfully and the status of the item will be change to Processed. | Revenue Accounting Items with error have been reprocessed successfully and the status of the items are changed to Processed. |  |

#### Overview, Monitor and Manage Revenue Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Revenue Accountant will have a overview on Revenue Accounting, monitor Revenue Contracts and manage Revenue Contracts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Revenue Accountant (REV_ACCOUNTANT). |  |  |
| 2 | Access App | Open Revenue Accounting Overview (F4067). |  |  |
| 3 | Input Selection Criteria and Run Overview | Input following selection criteria and choose Go:Display Currency: AEDCompany Code: 3310Accounting Principle: IFRSFiscal Year: <Fiscal Year to be tested (eg:2024)> | Overview report is displayed.Record the AED. |  |
| 4 | Access App | Open Monitor Revenue Contracts (F5014). |  |  |
| 5 | Input Selection Criteria and Run Overview | Input following selection criteria and choose Go:Company Code: 3310Accounting Principle: IFRS | Revenue Contract list is displayed. |  |
| 6 | Click on the Line Item to Enter the Screen of Revenue Contract Details | Click on the line item to enter the detailed screen of the Revenue Contract. | System navigate the user to the detailed screen of the Revenue Contract. |  |
| 7 | Check Revenue Contract details and perform Revenue Contract Related Activities (Edit, Period Activities and Related Apps) | User can check the detail of the Revenue Contract in this screen.If necessary, user can edit the Revenue Contract or perform Periodic Activities or jump to Related Apps. | Revenue Contract detail is displayed correctly. User is able to jump to periodic activities or related apps by select Periodic Activities or Related Apps |  |
| 8 | Access App | Open Manage Revenue Contracts - Old Version (F3883). | The user enters the initial screen of the APP. |  |
| 9 | Input Selection Criteria and Search Revenue Contract | Input following selection criteria and choose Go:Company Code: 3310Revenue Contract ID: <Leave blank> | Line item for the provider contract will be displayed in section Result List. |  |
| 10 | Enter Detailed Screen of the Revenue Contract | Click the Revenue Contract line item. | Enter the detailed screen of Provider Contract. |  |
| 11 | Review Contract Detailed Info | Review the Revenue Contract detailed information. | Provider Contract detailed information is displayed. |  |

#### Error Handling

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity shows what the user can do for error handling in Contract Based Revenue Recognition.

The error handling includes:

- Clean Up Productive Data

You can clean up and reverse the productive data if it’s necessary according to the business needs.

- Process Conflicted Revenue Contracts

A conflict may then occur because the system cannot determine whether the manual or operational value should be used. For example, this may occur when a change is made to the corresponding provider contract. If you and the back-end system have changed the same attribute, a conflict occurs. In this scenario, the system puts the contract with conflicting changes on the Conflicted Revenue Contracts Worklist user interface. You can review the list and resolve the conflicts on the UI.

- Reprocess Account Determination

Revenue Accounting allows you to reprocess account determination to apply a new assignment of general ledger accounts to revenue accounting contracts. This way, the accounts that are based on the latest account determination settings are retrieved and updated in the corresponding revenue accounting contracts.

- Reprocess Contracts

If some configuration attributes or business rules were not correctly configured when the contracts and POBs were created, you need to reprocess those contracts using the revised determination rules. Reprocess Contracts allows you to redetermine attributes of existing contracts and performance obligations (POBs), based on business rules and configuration attributes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Administrator - Revenue Accounting (REV_ADMIN). |  |  |
| 2 | Access App | Open Clean Up Productive Data (F5728). |  |  |
| 3 | Create Job for Clean Up Productive Data and input data in step 1 “Template Selection”. | Choose Create and enter parameters as following in Step 1:1. Template SelectionJob Template: Clean Up and Reverse the Productive DataJob Name: Clean Up and Reverse the Productive DataClick Step 2 to continue. | Step 2 “Schedule Options” is displayed. |  |
| 4 | Input data in step 2 “Schedule Options” | Enter parameters as following in Step 2:Check Box Start Immediately: <Checked>Job Start (Local Time): <defaulted by system and not editable>Click Step 3 to continue. | Section step 3 “Parameters” is displayed. |  |
| 5 | Input data in step 3 “Parameters” | Enter parameters as following in Step 3:Company Code: 3310Posting Date : <Posting Data to be tested>Sender Component: <Sender Component to be tested, eg: GEN>Order Header ID: <Order Header ID to be tested>Click Schedule to create the job. | Job is created. |  |
| 6 | Log On | Log on to the SAP Fiori launchpad as a Revenue Accountant (REV_ACCOUNTANT). |  |  |
| 7 | Access App | Open Conflicted Revenue Contracts Worklist (F4271). | App initial screen is displayed |  |
| 8 | Input Selection Criteria and Search Conflicted Revenue Contract | Input following selection criteria and choose Go:Company Code: 3310Account Principle: IFRS | List of conflicted revenue contract is displayed. |  |
| 9 | Resolving Conflicts | Click on a revenue contract to view the next page with details about the conflicted attributes.Click Edit in the upper right corner to enter edit mode.When you choose to accept either of the following, please make sure you always choose the desired value for all POBs in a contract as the system will not accept partial conflict resolution:Value from the Operational DocumentValue from Manual ChangeClick Resolve Conflicts to now save your changes and after your selection below, the POB status and revenue contract status will be set to In Process.If you choose a value from the manual change, then you have the option to select a Business Change Reason within the Confirmation pop-up window. The effective date remains the same as the effective date from the last contract change that was performed. If you do not select any Business Change Reason from the confirmation pop-up window, the Business Change Reason is taken from the last contract change instead.If you choose all values from operational document, then you will solve the conflict directly without providing any Business Change Reason. This is because you accept the current attributes of all performance obligations (POBs) without making any contract change. | Conflicts is solved. |  |
| 10 | Access App | Open Reprocess Account Determination (F4187). |  |  |
| 11 | Create Job for Reprocess Contracts and Input Data in Step 1 “Template Selection”. | Choose Create and enter parameters as following in Step 1:1. Template SelectionJob Template: Reprocess Account DeterminationJob Name: Reprocess Account DeterminationClick Step 2 to continue. | Step 2 “Schedule Options” is displayed. |  |
| 12 | Input Data in Step 2 “Schedule Options” | Enter parameters as following in Step 2:Check Box Start Immediately: <Checked>Job Start (Local Time): <defaulted by system and not editable>Click Step 3 to continue. | Section step 3 “Parameters” is displayed. |  |
| 13 | Input Data in Step 3 “Parameters” | Enter parameters as following in Step 3:Revenue Accounting Contract: <Revenue Contract ID>Click Schedule to create the job.Note This program records all events, such as errors and warnings, in an application log. The application log is displayed each time when the program finishes reprocessing the account determination. | Job is created.The effective changes for assigning general ledger accounts to revenue accounting contracts are saved in the database after the accounts have been redetermined for the revenue accounting contract. |  |
| 14 | Access App | Open Reprocess Contracts (F5237).This function allows you to redetermine attributes of existing contracts and performance obligations (POBs) based on business rules and configuration attributes with a background scheduled job. |  |  |
| 15 | Create Job for Reprocess Account Determination and Input Data in Step 1 “Template Selection”. | Choose Create and enter parameters as following in Step 1:1. Template SelectionJob Template: Reprocess Contracts in BackgroundJob Name: Reprocess Contracts in BackgroundClick Step 2 to continue. | Step 2 “Schedule Options” is displayed. |  |
| 16 | Input Data in Step 2 “Schedule Options” | Enter parameters as following in Step 2:Check Box Start Immediately: CheckedJob Start (Local Time): <defaulted by system and not editable>Click Step 3 to continue. | Section step 3 “Parameters” is displayed. |  |
| 17 | Input Data in Step 3 “Parameters” | Enter parameters as following in Step 3:Accounting Principle: IFRSCompany Code : 3310Click Schedule to create the job.Note This program records all events, such as errors and warnings, in an application log. The application log is displayed each time when the program finishes reprocessing the contracts. You can access the application logs stored by this program in the Reprocess Contracts (F5237) app. | Job is created.Revenue Contract is reprocessed after job is completed. |  |

#### Manual Processing (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Revenue Accountant will perform manual processing of POB which include manual fulfillment and revenue contracts combination.

For a POB to be fulfilled manually, the fulfillment type is either event-based (E) or the percentage of completion (O) and the event type is Manual Fulfillment (MA). You can make the settings of POB in configuration activity Maintain Contract Attribute Business Rules. Then select POB Attributes for the field Determination Rules for.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Revenue Accountant (REV_ACCOUNTANT). |  |  |
| 2 | Access App | Open Manual Fulfillment (F3881). | The user enters the initial screen of the APP.This step is optional. Perform revenue contracts combination if necessary. |  |
| 3 | Input Selection Criteria | Input following selection criteria and choose Go:Company Code: 3310Accounting Principle: IFRS | POBs meet the selection criteria and can be manually fulfilled are displayed. |  |
| 4 | Select POB and Perform Manual Fulfillment | Select a line item from the list and perform manual fulfillment of POB.If the fulfillment type of a POB is Event-Based, you can manually fulfill the POB by a delta quantity using a special fulfillment date.If the fulfillment type of the POB is Percentage of Completion, you can only manually fulfill the POB by using cumulative percentage.You can perform reverse fulfillment of a POB to deduct a quantity from the completely fulfilled quantity for a POB whose fulfillment type is Event-Based. | Manual fulfillment is completed successfully. |  |
| 5 | Access App | Open Combine Revenue Contracts (F4069). | The user enters the initial screen of the APP.This step is optional. Perform revenue contracts combination if necessary. |  |
| 6 | Input Selection Criteria and Search Revenue Contract | Input selection criteria or leave blank to select all, then choose Go. | Revenue Contracts are listed. |  |
| 7 | Combine Revenue Contract | Select the revenue contracts to be combined and then choose Combine Contracts. In the pop-up window, enter the target Revenue Contract (the main contract you want to combine other contracts to), and enter the business change reason and effective data, then choose Save. | Revenue Contracts are combined. |  |

#### Verification and Explanation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Revenue Accountant will perform the activities for verification and explanation which include: Review Revenue Schedule, Revenue Explanation, Allocated Amount Explanation, Document Flow and Review Change History.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Revenue Accountant (REV_ACCOUNTANT). |  |  |
| 2 | Access App | Open Revenue Schedule (F3882). | The user enters the initial screen of the APP. |  |
| 3 | Input Selection Criteria | Input following selection criteria and choose Go:Company Code: 3310Accounting Principle: IFRS | Revenue Contract list is displayed. |  |
| 4 | Select line item from Revenue Contract List and check revenue schedule | Select a line item from the list of Revenue Contract and system will navigate to the detail screen of the revenue schedule of the revenue contract.Check the revenue schedule. | Manual fulfillment is completed successfully. |  |
| 5 | Access App | Open Revenue Explanation (F4272). | The user enters the initial screen of the APP. |  |
| 6 | Input Selection Criteria and Search Revenue Contract | Input selection criteria or leave blank to select all, then choose Go. | Performance of Obligations are listed. |  |
| 7 | Check Revenue Explanation for POB | Select a line item from the list of Performance of Obligations and system will navigate to the detail screen of the revenue explanation.Check the revenue explanation for the Performance of Obligation. | Revenue explanation is displayed. |  |
| 8 | Access App | Open Allocated Amount Explanation (F4424). | The user enters the initial screen of the APP. |  |
| 9 | Input Selection Criteria and Search Revenue Contract | Input selection criteria or leave blank to select all, then choose Go. | Revenue Contract list is displayed. |  |
| 10 | Check Allocated Amount | Select a line item from the list of Revenue Contract and system will navigate to the detail screen of the allocated amount explanation of the revenue contract.Check the allocated amount for each POB in the revenue contract.. | Detail of allocated amount is displayed. |  |
| 11 | Access App | Open Document Flow - Performance Obligations (F4423). | The user enters the initial screen of the APP. |  |
| 12 | Input Selection Criteria | Input selection criteria and choose Go:Company Code: 3310Account Principle: IFRS | Line item for the Performance Obligations will be displayed. |  |
| 13 | Select Line Item and display the document flow | Click Line Item to display the document flow. | Document flow is displayed. |  |
| 14 | Access App | Open Display Change History - Revenue Contracts (F4273).. | The user enters the initial screen of the APP. |  |
| 15 | Input Selection Criteria | Input selection criteria or leave blank to select all, then choose Go. | List of Events (of changes) will be displayed |  |
| 16 | Check the change history | List of Events (of changes) will be displayed with change document number and line item details of each change document. You can check the detail of the change history. | Change history is checked. |  |

#### Periodic Activities – Revenue Administrator

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Revenue Administrator will perform period end activities for Revenue Accounting. By period end activities, contract asset, contract liability, recognized revenue, revenue allocation and acquisition cost will be calculated and posted to GL.

With the Business Reconciliation app, the Revenue Administrator can check the validity of data in a revenue contract and identify the revenue contracts that have inconsistencies between sender components with SAP and Contract-Based Revenue Recognition. Alternatively, with Run Business Reconciliation in Background (F4841), the Revenue Administrator can schedule a recurring job to identify inconsistent data between the sender components of SAP and Contract-Based Revenue Recognition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Administrator - Revenue Accounting (REV_ADMIN). |  |  |
| 2 | Access App | Open Transfer Revenue (F3879). | The user enters the initial screen of the app. |  |
| 3 | Create a New Transfer Job | In the initial screen, click + to create a new job for transfer.In screen New Job, enter following data:Company Code: 3310Fiscal Year: <the fiscal year you want to perform the period end activities>Period: <the period you want to perform the period end activities>Contract: <this is optional, enter a specific revenue contract number if you only want to process a single contract, otherwise leave it blank to run a massive run>Choose Schedule. | Transfer job is created and executed successfully. |  |
| 4 | Access App | Open Calculate Contract Liabilities and Contract Assets (F3875). | The user enters the initial screen of the app. |  |
| 5 | Calculate Contract Liabilities and Contract Assets | In the initial screen, click + to create a new job for transfer.In screen New Job, enter following data:Company Code: 3310Fiscal Year: <the fiscal year you want to perform the period end activities>Posting Period: <the period you want to perform the period end activities>Contract: <this is optional, enter a specific revenue contract number if you only want to process a single contract, otherwise leave it blank to run a massive run>Choose Schedule. | Job for Contract Liability and Contract Assets calculation is created and executed successfully. |  |
| 6 | Access App | Open Run Business Reconciliation in Background |  |  |
| 7 | Create Job for Business Reconciliation and input data in step 1 “Template Selection”. | Click Create to start creating a new job for Business Reconciliation.Job Template is defaulted as Run Reconciliation in Background by system. Do not change it.Job Name is also defaulted as “Run Reconciliation in Background” and change it if necessary.Click Step 2 to proceed. | The user enters the screen of step 2. |  |
| 8 | Input data in step 2 “Schedule Options” | Enter parameters as following in Step 2:Check Box Start Immediately: CheckedJob Start (Local Time): <defaulted by system and not editable>Click Step 3 to continue. | Section step 3 “Parameters” is displayed. |  |
| 9 | Input data in step 3 “Parameters” | Enter parameters as following in Step 3:Accounting Principle : IFRSCompany Code : 3310Click Schedule to create the job.Note This program records all events, such as errors and warnings, in an application log. The application log is displayed each time when the program finishes Business Reconciliation. | Job is created.Business Reconciliation is performed after job is completed. |  |
| 10 | Access App | Open Business Reconciliation (F4830). |  |  |
| 11 | Run App with Run Method “Display Background Check Results” | Select Display Background Check Results from the drop down list of Run MethodInput selection criteria and choose Go:Company Code: 3310Account Principle: IFRS | The reconciliation data is displayed and it results come from the Run Business Reconciliation in Background Fiori app which is executed in previous test steps. |  |
| 12 | Run App with Run Method “Run Reconciliation Now” | Select Run Reconciliation Now from the drop down list of Run MethodInput selection criteria and choose Go:Company Code: 3310Account Principle: IFRSOperational Document: Operational Document Number to be testedRevenue Contract: Revenue Contract Number to be tested | Revenue Contract is listed. |  |
| 13 | Check Reconciliation Results | Click on the line item of the Revenue Contract to display the detail of Reconciliation Results. | Reconciliation results detail is displayed. |  |

#### Disclosures and Analytics

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Revenue Accountant will perform activities for disclosures and analytics.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Revenue Accountant (REV_ACCOUNTANT). |  |  |
| 2 | Access App | Open Disaggregation of Recognizable Revenue (W0156). |  |  |
| 3 | Input Selection Criteria | Input selection criteria and choose Go:Company Code: 3310Account Principle: IFRSDisplay Currency: AEDFiscal Year: <Fiscal Year to be tested>Fiscal Period: <Fiscal Period to be tested> | Analytical report is displayed. |  |
| 4 | Check Disaggregation of Recognizable Report | Check the analytical report for disaggregation of recognizable revenue.You can drag dimensions and measures to various rows and columns.You can display the report using different formats; this includes charts, tables, or a combination of both.This report also provides other additional functions such as Navigate To which enables you to quickly switch to another Fiori application. |  |  |
| 5 | Access App | Open Contract Balance (W0155). |  |  |
| 6 | Input Selection Criteria | Input selection criteria and choose Go:Company Code: 3310Account Principle: IFRSFiscal Year: <Fiscal Year to be tested>From Fiscal Period: <Fiscal Period to be tested>To Fiscal Period: <Fiscal Period to be tested>Display Currency: AEDExchange Rate Type: MExchange Rate Date: <Current Date>Display Mode: By Quarter | Analytical report is displayed. |  |
| 7 | Check Contract Balance Report | Check the analytical report for Contract Balance.You can drag dimensions and measures to various rows and columns.You can display the report using different formats; this includes charts, tables, or a combination of both.This report also provides other additional functions such as Navigate To which enables you to quickly switch to another Fiori application. |  |  |
| 8 | Access App | Open Contract Balance Movements (W0154). |  |  |
| 9 | Input Selection Criteria | Input selection criteria and choose Go:Company Code: 3310Account Principle: IFRSFiscal Year: <Fiscal Year to be tested>From Fiscal Period: <Fiscal Period to be tested>To Fiscal Period: <Fiscal Period to be tested>Display Currency: AEDExchange Rate Type: MExchange Rate Date: <Current Date>Display Mode: By Quarter | Analytical report is displayed. |  |
| 10 | Check Contract Balance Movement Report | Check the analytical report for Contract Balance Movement.You can drag dimensions and measures to various rows and columns.You can display the report using different formats; this includes charts, tables, or a combination of both.This report also provides other additional functions such as Navigate To which enables you to quickly switch to another Fiori application. |  |  |
| 11 | Access App | Open Disaggregation of Revenue (W0157). |  |  |
| 12 | Input Selection Criteria | Input selection criteria and choose Go:Company Code: 3310Account Principle: IFRSFiscal Year: <Fiscal Year to be tested> | Analytical report is displayed. |  |
| 13 | Check the Report of Disaggregation of Revenue | Check the analytical report for disaggregation of revenue.You can drag dimensions and measures to various rows and columns.You can display the report using different formats; this includes charts, tables, or a combination of both.This report also provides other additional functions such as Navigate To which enables you to quickly switch to another Fiori application. |  |  |
| 14 | Access App | Open Remaining Performance Obligations - Total Open Revenue (W0159). |  |  |
| 15 | Input Selection Criteria | Input selection criteria and choose Go:Company Code: 3310Account Principle: IFRSFiscal Year: <Fiscal Year to be tested>Fiscal Period: <Fiscal Period to be tested>Display Currency: AEDExchange Rate Type: MExchange Rate Date: <Current Date> | Analytical report is displayed. |  |
| 16 | Check the Report of Remaining Performance Obligations – Total Open Revenue | Check the analytical report for Remaining Performance Obligations - Total Open Revenue.You can drag dimensions and measures to various rows and columns.You can display the report using different formats; this includes charts, tables, or a combination of both.This report also provides other additional functions such as Navigate To which enables you to quickly switch to another Fiori application. |  |  |
| 17 | Access App | Open Calculate Revenue Catch-up (F5052). |  |  |
| 18 | Create Job for Calculate Revenue Catch-up and input data in step 1 “Template Selection”. | Click Create to start creating a new job for Business Reconciliation.Job Template is defaulted as Calculate Quarterly and Yearly Revenue Catch-up by system. Do not change it.Job Name is also defaulted as Calculate Quarterly and Yearly Revenue Catch-up and change it if necessary.Click Step 2 to proceed. | The user enters the screen of step 2. |  |
| 19 | Input data in step 2 “Schedule Options” | Enter parameters as following in Step 2:Check Box Start Immediately: <Check>Job Start (Local Time): <defaulted by system and not editable>Click Step 3 to continue. | Section step 3 “Parameters” is displayed. |  |
| 20 | Input data in step 3 “Parameters” | Enter parameters as following in Step 3:Company Code : 3310Accounting Principle : IFRSFrom Fiscal Year: <Fiscal Year to be tested>To Fiscal Year: <Fiscal Year to be tested>Radio Button Calculate Revenue Catch-up: <Select>Click Schedule to create the job.Note This program records all events, such as errors and warnings, in an application log. The application log is displayed each time when the program finishes reprocessing the contracts. | Job is created.Calculate Revenue Catch-up is performed after job is completed. |  |
| 21 | Access App | Open Revenue Catch-Up (W0169). |  |  |
| 22 | Input Selection Criteria | Input selection criteria and choose Go:Company Code: 3310Account Principle: IFRSFiscal Year: <Fiscal Year to be tested>From Fiscal Period: <Fiscal Period to be tested>To Fiscal Period: <Fiscal Period to be tested>Display Currency: AEDExchange Rate Type: MExchange Rate Date: <Current Date>Display Mode: By Quarter | Analytical report is displayed.If you would like to analyze the revenue catch-up by quarter and by year, you must first prepare the quarterly or yearly revenue catch-up. You can use the Calculate Revenue Catch-up application job to complete data preparation (refer to previous test steps for detail). |  |
| 23 | Check the Report of Revenue Catch-up | Check the analytical report for Remaining Performance Obligations - Total Open Revenue.You can drag dimensions and measures to various rows and columns.You can display the report using different formats; this includes charts, tables, or a combination of both.This report also provides other additional functions such as Navigate To which enables you to quickly switch to another Fiori application. |  |  |
| 24 | Access App | Open Contract Balance Reclassification (W0176). |  |  |
| 25 | Input Selection Criteria | Input selection criteria and choose Go:Company Code: 3310Account Principle: IFRSFiscal Year: <Fiscal Year to be tested>Fiscal Period: <Fiscal Period to be tested>Aging: SGLOBRCL | Analytical report is displayed. |  |
| 26 | Check the Report of Contract Balance Reclassification | Check the analytical report for Contract Balance Reclassification.You can drag dimensions and measures to various rows and columns.You can display the report using different formats; this includes charts, tables, or a combination of both.This report also provides other additional functions such as Navigate To which enables you to quickly switch to another Fiori application. |  |  |

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
- related-to :: [[06-management-accounting/test-script-contract-based-revenue-recognition-us-gaap-3vs-ae-976]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3KK_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 82,369 chars in the whole document
