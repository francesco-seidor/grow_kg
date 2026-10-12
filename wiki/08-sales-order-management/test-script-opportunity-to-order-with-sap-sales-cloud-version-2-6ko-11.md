---
id: 08-sales-order-management/test-script-opportunity-to-order-with-sap-sales-cloud-version-2-6ko-11
title: "Test Script: Opportunity to Order with SAP Sales Cloud Version 2 (6KO) (6KO_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 6KO: integration of SAP Sales Cloud V2 with S/4HANA, from master data replication to quote and order."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/crm-opportunity-to-order]
aliases: [6KO_S4CLD2608_BPD_EN_XX]
keywords: [Opportunity to Order with SAP Sales Cloud and Cloud for…, sales cloud integration, test procedures, business partner replication, material replication, sales quotes, sales orders, pricing simulation, pricing configuration import, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6KO_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1176
topic: 08-sales-order-management/crm-opportunity-to-order
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Opportunity to Order with SAP Sales Cloud Version 2 (6KO) (6KO_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6KO_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Opportunity to Order with SAP Sales Cloud and Cloud for Customer** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Opportunity to Order with SAP Sales Cloud Version 2 (6KO) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232826464)

[2 Prerequisites 4](#_Toc232826465)

[2.1 System Access and Roles 4](#_Toc232826466)

[2.2 Master Data, Organizational Data, and Other Data 5](#_Toc232826467)

[2.3 Business Conditions 6](#_Toc232826468)

[3 Overview Table 8](#_Toc232826469)

[4 Test Procedures 9](#_Toc232826470)

[4.1 Create and Change Material in SAP S/4HANA Cloud Public Edition System 9](#_Toc232826471)

[4.2 Create and Change Business Partner in SAP S/4HANA Cloud Public Edition System 11](#_Toc232826472)

[4.3 Create Business Partner Relationship in SAP S/4HANA Cloud Public Edition 14](#_Toc232826473)

[4.4 Create Business Partner Relationship Hierarchy in SAP S/4HANA Cloud Public Edition 15](#_Toc232826474)

[4.5 Create and Change Accounts in SAP Sales Cloud Version 2 System 16](#_Toc232826475)

[4.6 Create Contact (with Relationship) in SAP Sales Cloud Version 2 System 19](#_Toc232826476)

[4.7 Retrieve Price Customization from SAP S/4HANA 20](#_Toc232826477)

[4.8 Create Follow Up Sales Quote from Opportunity in SAP Sales Cloud Version 2 System 21](#_Toc232826478)

[4.9 Sales Quote Simulation in SAP Sales Cloud Version 2 23](#_Toc232826479)

[4.10 Create Follow Up Sales Order from Sales Quote in SAP Sales Cloud Version 2 System 24](#_Toc232826480)

[4.11 Capture Sales Order Changes in SAP Sales Cloud Version 2 25](#_Toc232826481)

[4.12 Review Sales Order History in SAP Sales Cloud Version 2 26](#_Toc232826482)

[4.13 Delete Sales Quote Reference in SAP Sales Cloud Version 2 27](#_Toc232826483)

[4.14 Delete Sales Order Reference in SAP Sales Cloud Version 2 28](#_Toc232826484)

[4.15 Create am Employee (Worker) in SAP S/4HANA Cloud Public Edition 29](#_Toc232826485)

[5 Appendix 31](#_Toc232826486)

[5.1 Process Integration 31](#_Toc232826487)

## Purpose

Overview

This scope item enables the process integration of SAP Sales Cloud Version 2 with SAP S/4HANA Cloud Public Edition.

After implementing the steps in the set-up instructions guide, you synchronize business partner information and replicate additional master data, such as materials, company code, and sales area data such from SAP S/4HANA Cloud Public Edition to SAP Sales Cloud Version 2. Sales quotes can be created from opportunities in SAP Sales Cloud Version 2 and the follow-up document once triggered from the Sales Quote, creates a sales order in SAP S/4HANA Cloud Public Edition.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access and Roles

The test should be conducted with the following system:

| System | Details |
| --- | --- |
| SAP Sales Cloud Version 2 | Provide details on how to access system, for example, system client or URL |
| SAP S/4HANA Cloud Public Edition system | Provide details on how to access system, for example, system client or URL |

Roles in SAP Sales Cloud Version 2

The business role assigned to the test user needs to contain business services that are activated based on the business object that is in scope for testing.

The business services can be added when creating or editing the business role. Apps that need to be accessible can be activated under the App List section when creating or editing the business roles. For more information on how to add the business services, refer to the setup guide.

To have access to the business services and apps for a specific business object, use following table and assign the following business services and activate the apps with the Enable App switch for the test user in the business role in addition to the defaults:

| Business Object | Business Service ID | App Name |
| --- | --- | --- |
| Account | sap.crm.md.service.accountService | sap.crm.md.accountservice.uiapp.accountApp |
| Employee (required to add owner to account) | sap.crm.md.service.employeeService | sap.crm.md.employeeservice.uiapp.employeeNonAdminApp |
| Contact | sap.crm.md.service.contactPersonService | sap.crm.md.contactpersonservice.uiapp.contactApp |
| Product | sap.crm.md.service.productService | Product |
| Sales Quote | sap.crm.service.salesQuoteService | sap.crm.salesquoteservice.uiapp.salesQuoteAdminApp |
| Guided Selling | sap.crm.service.guidedSellingService | Guided Selling Administration |
| Opportunity | sap.crm.service.opportunityService | - |

Roles in SAP S/4HANA Cloud Public Edition system

|  |
| --- |
| Note Role templates such as Maintenance Planner is not required if your integration is set up by SAP. |

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

For more information, refer to How to Create a Business Role for the Administrator in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/8fa28e0107984d42a99b9eea67856cea.html) for SAP S/4HANA Cloud Public Edition.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Name (Role Template) | Description | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) |  |
| Administrator - Data Replication | On the SAP Fiori launchpad, the internal sales representative with this role has access to perform data replication from SAP S/4HANA Cloud Public Edition system. | SAP_BR_ADMINISTRATOR_DATA_REPL |  | SAP_BR_ADMINISTRATOR_DATA_REPL | Test user: INTERNAL_SALES_REP |
| Master Data Specialist - Business Partner Data | In the SAP Sales Cloud Version 2 system, the field sales representative creates a follow up. On the SAP Fiori launchpad, the internal sales representative with this role has access to view and create business partner data. | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST | Test user: INTERNAL_SALES_REP |
| Master Data Specialist - Product Data | On the SAP Fiori launchpad, the internal sales representative with this role has access to view and create product master data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST | Test user: INTERNAL_SALES_REP |
| Consolidation Specialist Consolidation Specialist | On the SAP Fiori launchpad, the internal sales representative with this role has access to maintain exchange rate tile. | SAP_BR_CONSLDTN_SPECIALIST | Consolidation Specialist | SAP_BR_CONSLDTN_SPECIALIST |  |
| Maintenance Planner | On the SAP Fiori launchpad, the internal sales representative with this role has access to create, change, and display the technical objects. | SAP_BR_MAINTENANCE_PLANNER | Maintenance Planning | SAP_BR_MAINTENANCE_PLANNER |  |
| Internal Sales Representative | On the SAP Fiori launchpad, the internal sales representative with this role has access to create, change, and display the technical objects. | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents, for example, materials, customers, and vendors, depending on the operational focus of your company.

Use your own master data to perform the test procedure. If you’ve installed an SAP Best Practices baseline package, you can use the following sample data from the baseline package:

|  |
| --- |
| Note Currently, the SAP_COM_0008 communication scenario doesn’t support a third-party item category group for product replication. Use a product with a standard item category for your testing. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)no batch |  |
| Material | TG12 | Trading Good for Reg. Trading (reorder point planning)no batch |  |
| Sold-to party | 1710000317100005 | Customer domestic 03Customer domestic 05 | You can test the scope item using another domestic customer.17100005 is for credit management. |
| Ship-to Party | 1710000317100005 | Customer domestic 03Customer domestic 05 |  |
| Payer | 1710000317100005 | Customer domestic 03Customer domestic 05 |  |
| Company Code | 1710 |  |  |
| Sales Organization | 1710 |  |  |
| Distribution Channel | 10 |  |  |
| Division | 00 |  |  |
| Sales Office | 170 |  |  |
| Sales Group | 170 |  |  |

|  |
| --- |
| Note Ensure the System Filter field is set to X before you proceed for the transactional data replication in the communication arrangements SAP_COM_0008 and SAP_COM_0009. |

### Business Conditions

Before testing the scope item, the following business conditions needs to be met:

| Scope Item | Business Condition |
| --- | --- |
| BD9 - Sell from Stock | All relevant steps described in the business conditions and preliminary steps chapters are completed. |

|  |
| --- |
| Note Some of the fields might not be visible in the default SAP Sales Cloud Version 2. In this case, you need to customize the screens according to your requirements. |

## Overview Table

The integration of SAP Sales Cloud Version 2 with SAP S/4HANA Cloud Public Edition consists of several process steps which are listed in this table:

| Process Step | Business Role | UI Type | Expected Results |
| --- | --- | --- | --- |
| [Create and Change Material in SAP S/4HANA Cloud Public Edition System](#unique_7) [page ] 9 | Internal Sales Representative | SAP S/4HANA Cloud Public Edition Fiori UI | Material will be replicated to SAP Sales Cloud Version 2 |
| [Create and Change Business Partner in SAP S/4HANA Cloud Public Edition System](#unique_8) [page ] 11 | Internal Sales Representative | SAP S/4HANA Cloud Public Edition Fiori UI | Business Partner will be replicated to SAP Sales Cloud Version 2 system |
| [Create Business Partner Relationship in SAP S/4HANA Cloud Public Edition](#unique_9) [page ] 14 | Internal Sales Representative | SAP S/4HANA Cloud Public Edition Fiori UI | Business Partner Relationship will be replicated to SAP Sales Cloud Version 2 system |
| [Create and Change Accounts in SAP Sales Cloud Version 2 System](#unique_10) [page ] 16 | Field Sales Representative (CRM) | SAP Sales Cloud Version 2 UI | Account overview page is displayed after searching the right account to be viewed. Select the account to see the details of the account. Account team is displayed, new member can be added to the account team. |
| [Create Contact (with Relationship) in SAP Sales Cloud Version 2 System](#unique_11) [page ] 19 | Field Sales Representative (CRM) | SAP Sales Cloud Version 2 UI | A new contact is created and it can be viewed and assigned under an account. |
| [Create Follow Up Sales Quote from Opportunity in SAP Sales Cloud Version 2 System](#unique_12) [page ] 21 | Field Sales Representative (CRM) | SAP Sales Cloud Version 2 UI | Follow up Sales Quote will be replicated to SAP S/4HANA Cloud Public Edition (Out of scope for Integration set up by SAP) |
| [Create Follow Up Sales Order from Sales Quote in SAP Sales Cloud Version 2 System](#unique_13) [page ] 24 | Field Sales Representative (CRM) | SAP Sales Cloud Version 2 UI | Sales Order creation in SAP S/4HANA Cloud Public Edition is triggered from a Sales Quote from SAP Sales Cloud Version 2 |

## Test Procedures

This section describes the test procedures for each process step that belongs to this scope item.

### Create and Change Material in SAP S/4HANA Cloud Public Edition System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create and change a material in the SAP S/4HANA Cloud Public Edition system.

Create Material (Optional):

Complete all activities described in the master data script Create Product Master of type Trading Good - MDS.

For more information on creating master data objects, see the following [Create Material (Product) Master Data - Basic Data](https://help.sap.com/docs/s4hana-best-practices/s4cld2502-master-data).

|  |
| --- |
| Note It's also possible to create a copy of an existing material from the SAP S/4HANA Cloud Public Edition system. |

Change Material

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch Your SAP S/4HANA Cloud Public Edition System | Enter the SAP S/4HANA Cloud Public Edition system URLIn your browser, enter the User ID and Password, and choose Log On. | Successful logon |  |
| 2 | Open App | Open the Change Material (MM02) app. | Change Material page is opened. |  |
| 3 | Search Material With Specific Detail | To search for a material, in the Find field, enter any keyword or field value.For example:Material: TG11Description: TRAD.GOOD 11,PD,REG.TRADING | A list of accounts with details is displayed. |  |
| 4 | Choose Continue | To select this material, choose Continue. | Select View page appears. |  |
| 5 | Select Views | Select the required or All Views and choose Continue. | The Home page appears. The details of the team account are displayed. |  |
| 6 | Select Organization Levels | Select the Sales Org details as required and choose Continue.Example Plant: 1710Stor. Location:171ASales Org. :1710Distr. Channel:10 | A new screen for selected material opens. |  |
| 7 | Change Material | Maintain the required changes for the material. |  |  |
| 8 | Save Material | On the Material Change Screen, choose Save. | The changes to material are saved and are replicated to the SAP Sales Cloud Version 2 system. |  |
| 9 | Launch SAP Sales Cloud Version 2 | Enter the SAP Sales Cloud Version 2 system URL https://<tenantID>.crm.ondemand.com.In your browser, enter the User ID and Password, and click Log On. | Successful logon |  |
| 10 | Choose Product Work Center View | On the top navigation bar, go to PRODUCTS > PRODUCTS.In the menu bar, from the dropdown box, choose the option All. | All products are displayed. |  |
| 11 | Search for Your Product | In the Search field, search for the product that you recently changed in the SAP S/4HANA Cloud Public Edition system. | The relevant product is displayed. |  |
| 12 | Check the Product | Open the product to verify that the changes are updated in the SAP Sales Cloud Version 2 system.Note When you open a product, the SAP Sales Cloud Version 2 displays the available information such as details, sales data, and stock information (if maintained). To view stock information specifically, scroll down to the Plant section and select Stock Information. This will trigger the iFlow, and the stock details will be shown if they are maintained in the S/4 system.The Stock Information button will only be available once the configuration is set up. For guidance, refer to the setup guide. | All changes are updated and verified for the product. |  |

### Create and Change Business Partner in SAP S/4HANA Cloud Public Edition System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create and change a business partner in the SAP S/4HANA Cloud Public Edition system.

Create Business Partner (Optional)

Complete all activities described in the master data script Create Customer Master - MDS. Follow this link for more information about the [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .

Create Business Partner Account or Contact

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Test Step # | Test Step Name |  | Expected Result | Pass / Fail / Comment |
| 1 | Launch SAP S/4HANA Cloud Public Edition system | Enter the SAP S/4HANA Cloud Public Edition system URL.In your browser, enter the User ID and the Password, and choose Log On. | Successful logon |  |
| 2 | Open App | Open the Maintain Business Partner (BP) app. | The Maintain Business Partner screen is displayed. |  |
| 3 | Create a BP Account | Choose Organization (for account creation).OrChoose Person (for contact creation). | The Create Organization page opens. |  |
| 4 | Choose the Role Customer | In Create in BP role, choose FLCU01 Customer (for Sales).OrIn Create in BP role choose BUP001 Contact Person (for contact).In the dialog box, choose Create. | The account with the BP role FLCU01 (customer) is selected for creation.OrThe contact of the BP role BUP001 is selected for creation. |  |
| 5 | Provide the Mandatory Data | To create an account, fill in the mandatory fields: Name Country/RegCity LanguageOrTo create a contact, fill in the mandatory fields: Last Name Correspondence Lang | All the required data related to the BP account is filled in.OrAll the required data related to the BP contact is filled in. |  |
| 6 | Provide Sales Area Information | Choose the Sales and Distribution tab and in the section Sales Areas, fill in the data for Sales Organization, Distribution Channel and Division. | The sales area data is saved.Note This information is necessary when processing sales documents for this business partner |  |
| 7 | Save the Business Partner | Choose Save. | The business partner account or contact data is saved and a business partner ID is generated.The changes are saved to the SAP Sales Cloud Version 2 system depending on the replication model settings. |  |
| 8 | Launch SAP Sales Cloud Version 2 | Enter the SAP Sales Cloud Version 2 system URL https://<tenantID>.crm.ondemand.com.In your browser, enter the User ID and Password, and select Log On. | Successful logon |  |
| 9 | Choose Customers Work center view | On the navigation bar, go to ACCOUNTS >.OrOn the navigation bar, go to CONTACTS.In the menu bar, from the dropdown box, choose the option All. | All accounts or contacts are displayed. |  |
| 10 | Search for Your Business partner | In the Search field, search for the business partner that you recently created in the SAP S/4HANA Cloud Public Edition system. | The relevant business partner account or contact is displayed. |  |

Change Business Partner

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch SAP S/4HANA Cloud Public Edition system | Enter the SAP S/4HANA Cloud Public Edition system URL.In your browser, enter the User ID and Password and choose Log On. | Successful login |  |
| 2 | Access app | Open Maintain Business Partner(BP). | The Maintain Business Partner screen is displayed. |  |
| 3 | Search Business Partner with specific detail | In the Find field enter any keyword or field value to search for a Business Partner.For example:Business Partner: 17100003Name: Domestic Customer US 3 | A list of accounts with details is displayed. |  |
| 4 | Open Business Partner overview page | Choose the Business Partner name | The Business Partner overview page is displayed. |  |
| 5 | Change Mode | Choose Switch Between Display and Change to enable change mode | Business Partner Overview page with change mode is displayed. |  |
| 6 | Change Business Partner | Maintain the required changes for the Business Partner |  |  |
| 7 | Save the Business Partner | On the Account Screen, choose Save | The changes are saved to SAP Sales Cloud Version 2 system. |  |
| 8 | Launch SAP Sales Cloud Version 2 | Enter the SAP Sales Cloud Version 2 system URL https://<tenantID>.crm.ondemand.com.In your browser, enter the User ID and Password, and click Log On. | Successful login. |  |
| 9 | Choose Customers Work center view | On the navigation bar, go to ACCOUNTSChoose the option All from the dropdown box in the menu bar | All accounts are displayed. |  |
| 10 | Search your Account | In the Search field, search the account which you recently changed in SAP S/4HANA Cloud Public Edition system | The relevant account is displayed. |  |
| 11 | Check the Account | Open the account to validate the changes are updated in SAP Sales Cloud Version 2 system. | All changes are updated and verified for the account. |  |

### Create Business Partner Relationship in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch SAP S/4HANA Cloud Public Edition System | Enter the SAP S/4HANA Cloud Public Edition system URL.In your browser, enter the User ID and Password, and choose Log On. | Successful logon. |  |
| 2 | Open App | Open the Maintain Business Partner (BP) app. | The Maintain Business Partner screen is displayed. |  |
| 3 | Search for Business Partner with Specific Detail | In the Find field, enter any keyword or field value to search for a business partner. | A list of accounts with details is displayed. |  |
| 4 | Open the Business Partner Overview Page | Choose the business partner (account) name | The Business Partner Overview page opens. |  |
| 5 | Change Mode | Choose Switch Between Display and Change to enable change mode | The Business Partner Overview page with change mode is displayed. |  |
| 6 | Create Relationship | Choose Relationships. | The Maintain Relationships opens. |  |
| 7 |  | Choose Relationship Cat as FBUR001 – Has Contact Person. |  |  |
| 8 |  | In the field Relationship, choose a business partner contact and choose Create.Select the checkbox Standard and choose continue. | A success message appears. The relationship was applied. |  |
| 9 | Save the Relationship | Choose Save. | Changes have been saved. |  |
| 10 | Launch SAP Sales Cloud Version 2 | Enter the SAP Sales Cloud Version 2 system URL https://<tenantID>.crm.ondemand.com.In your browser, enter the User ID and Password, and click Log On. | Successful logon |  |
| 11 | Choose Customers Work Center View | On the navigation bar, go to ACCOUNTS.In the menu bar, from the dropdown box, choose All. | All accounts are displayed. |  |
| 12 | Search for Your Account | In the Search field, search the account that you recently changed in SAP S/4HANA Cloud Public Edition system | The relevant account is displayed. |  |
| 13 | Check the Account | Open the account to validate the relationship changes are updated in the SAP Sales Cloud Version 2 system. The contact appears on the account page under Main Contact. | All relationship changes are updated and verified for the account. |  |

### Create Business Partner Relationship Hierarchy in SAP S/4HANA Cloud Public Edition

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
| 1 | Launch SAP S/4HANA Cloud Public Edition System | Enter the SAP S/4HANA Cloud Public Edition system URL.In your browser, enter the User ID and Password, and choose Log On. | Successful log on. |  |
| 2 | Open app. | Open the Maintain Business Partner (BP) app. | The Maintain Business Partner screen is displayed. |  |
| 3 | Search for Business Partner with Specific Detail | In the Find field, enter any keyword or field value to search for a business partner. | A list of accounts with details is displayed. |  |
| 4 | Open the Business Partner Overview Page | Choose the business partner (account) name | The Business Partner Overview page opens. |  |
| 5 | Change Mode | Choose Switch Between Display and Change to enable change mode. | The Business Partner Overview page with change mode is displayed. |  |
| 6 | Create Relationship | Choose Relationships. | Maintain Relationships opens. |  |
| 7 |  | Choose Relationship Cat as FFSB002 – Is subsidiary of. |  |  |
| 8 |  | In the field Relationship, choose a business partner account (Organization) and choose Create. | A success message is displayed. The relationship was applied. |  |
| 9 | Save the Relationship | Choose Save. | Changes have been saved. |  |
| 10 | Launch SAP Sales Cloud Version 2 | Enter the SAP Sales Cloud Version 2 system URL https://<tenantID>.crm.ondemand.com.In your browser, enter the User ID and Password, and Log On. | Successful logon |  |
| 11 | Choose Customers Work Center View | On the navigation bar, go to ACCOUNTS.In the menu bar, from the dropdown box, choose All. | All accounts are displayed. |  |
| 12 | Search for Your Account | In the Search field, search the account that you recently changed in SAP S/4HANA Cloud Public Edition system. | The relevant account is displayed. |  |
| 13 | Check the Account | Open the account to validate the relationship changes are updated in the SAP Sales Cloud Version 2 system. The hierarchical relationship appears on the account page under Account Hierarchy. | All relationship changes are updated and verified for the account. |  |

### Create and Change Accounts in SAP Sales Cloud Version 2 System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create and change an account in the SAP Sales Cloud Version 2 system.

Procedure

1. Create an account:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch SAP Sales Cloud Version 2 | Enter the SAP Sales Cloud Version 2 system URL https://tenantID.crm.ondemand.com.In your browser, enter the User ID and Password and choose Log On. | Successful logon |  |
| 2 | Choose Customers Work Center View | In the top navigation bar, go to ACCOUNTS. | All accounts are displayed. |  |
| 3 | Create Account With Specific Detail | On the Account list screen, choose Create (+). | Account Create opens. |  |
| 4 | Provide the Following Account Information | On the Account Create screen, enter the required dataName: Enter name For example: Test AccountRole: Enter a role, for example: CustomerCountry/Region: Enter country/regionCity: Enter cityState: Enter state | The data is accepted by the system.Note If you select the role Prospect, the account is blocked from replicating to the SAP S/4HANA Cloud Public Edition system. |  |
| 5 | Save the Account | On the Create Account screen, choose Save. | An account is created in the SAP Sales Cloud Version 2 system and replicated to the SAP S/4HANA Cloud Public Edition system. |  |
| 6 | Launch SAP S/4HANA Cloud Public Edition System | Enter the SAP S/4HANA Cloud Public Edition system URL.In your browser, enter the User ID and Password, and choose Log On. | Successful logon |  |
| 7 | Open App | Maintain Business Partner (BP) | The Maintain Business Partner page is opened. |  |
| 8 | Search for Business Partner With Specific Detail | In the Find field, search for Business Partner from the dropdown. In the By field, search for the Name/Number from the dropdown. For example:Find*: Business Partner/Person:By*: Name/Number: | A list of business partners with details is displayed. |  |
| 9 | Open Business Partner Overview Page | Select the business partner's name. | The account created in SAP Sales Cloud Version 2 system is displayed. |  |

1. Change an account:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch SAP Sales Cloud Version 2 | Enter the SAP Sales Cloud Version 2 system URL https://tenantID.crm.ondemand.com.In your browser, enter the User ID and Password and choose Log On. | Successful login |  |
| 2 | Choose Customers Work center view | In the navigation bar, go to ACCOUNTS.Choose the option All from the dropdown box in the menu bar | All accounts are displayed. |  |
| 3 | Search Account with specific detail | In the Find field, enter any keyword or field value to search for an account.For example:Account: 17100003Name: Domestic Customer US 3(This is optional. Either SAP S/4HANA Cloud Public Edition customer ID or SAP Sales Cloud Version 2 account ID can be used for the search.) | A list of accounts with details is displayed |  |
| 4 | Open Account overview page | Select the account name. | The account overview page is displayed. |  |
| 5 | Change Account | Select the action icon () to edit the details. Maintain the changes for this account. |  |  |
| 6 | Save the Account | Choose Save. | Your changes are saved in SAP Sales Cloud Version 2 system. The changes are replicated to SAP S/4HANA Cloud Public Edition System. |  |
| 7 | Launch SAP S/4HANA Cloud Public Edition system | Enter the SAP S/4HANA Cloud Public Edition system URLIn your browser, enter the User ID and Password, and choose Log On. | Successful login. |  |
| 8 | Access app | Choose the Maintain Business Partner (BP) | Maintain Business Partner page is opened. |  |
| 9 | Search Business Partner with specific detail | In the Find field, search for Business Partner from the dropdown. In the By field, search for the Name/Number from the dropdown. For example:Find*: Business Partner/Person:By*: Name/Number: | A list of Business Partner with details is displayed. |  |
| 10 | Open Business Partner overview page | Select the Business Partner name | The Business Partner overview page is displayed. |  |
| 11 | Check Business Partner | Check the Business Partner for your changes | The changes are visible for this Business Partner. |  |

### Create Contact (with Relationship) in SAP Sales Cloud Version 2 System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a new contact for an account from the account overview page.

|  |
| --- |
| Note Avoid creating a new contact person and assigning the contact person to an account in a single step. This could lead to an error during the data replication in SAP S/4HANA Cloud Public Edition. To avoid errors, follow these steps: |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | View Contacts | From the SAP Sales Cloud Version 2 home page, choose CONTACTS.In the menu bar, from the dropdown box, choose the All option. | A list of contacts is displayed. |  |
| 2 | Create Contact | Choose Create (+).Enter the following details:First Name: first nameLast Name: last nameAccount: Enter account created in [Create and Change Accounts in SAP Sales Cloud Version 2 System](#unique_10) [page ] 16.Language: Enter a language.Choose Save | A contact is successfully created in SAP Sales Cloud Version 2 system. The contact is replicated to the SAP S/4HANA Cloud Public Edition system.The new contact is displayed on the Overview page. |  |
| 3 | Launch SAP S/4HANA Cloud Public Edition System | Enter the SAP S/4HANA Cloud Public Edition system URL.In your browser, enter the User ID and Password, and choose Log On. | Successful logon |  |
| 4 | Open App | Open Maintain Business Partner (BP). | Maintain Business Partner page opens. |  |
| 5 | Search for Business Partner With Specific Detail | In the Find field, enter any keyword or field value to search for a business partner.Example Person: 17100003Name: Domestic Customer US 3 | A list of business partner with details is displayed |  |
| 6 | Open Business Partner Overview Page | Choose the business partner's name. | The Business Partner overview page opens. |  |
| 7 | Check Relationship | Go to the Relationship tab. | The related account is displayed in the relationship list. |  |

### Retrieve Price Customization from SAP S/4HANA

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
| 1 | Launch SAP Sales Cloud Version 2 | Enter the SAP Sales Cloud Version 2 system URL https://<tenantID>.crm.ondemand.com.In your browser, enter the User ID and Password, and Log On. | Successful log on. |  |
| 2 | Navigate to the user menu and select Settings | Select All Settings > Pricing > Pricing Configuration |  |  |
| 3 | Select Import Pricing Components | From the options displayed, select the option SAP ERP (SAP S/4HANA), then select confirm. | Define Field Mappings will sppear, no action is required at this step, simply select Next to continue. |  |
| 4 |  | A dropdown list of Pricing Procedure will appear (containing all procedures available in SAP S/4HANA). Select the required one and then Import Configuration Data. | The Pricing Procedure has now been imported.Note To verify the import status, refer to Import Logs. |  |

|  |
| --- |
| Note To review the Pricing Procedure that you have imported, refer to Pricing Components. There, select External to view all imported external Pricing Procedure entries. |

### Create Follow Up Sales Quote from Opportunity in SAP Sales Cloud Version 2 System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note This test case is not applicable for Integration set up by SAP. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch SAP Sales Cloud Version 2 | Enter the SAP Sales Cloud Version 2 system URL https://tenantID.crm.ondemand.com.In your browser, enter the User ID and Password and choose Log On. | Successful log in |  |
| 2 | View Opportunities | From the SAP Sales Cloud Version 2 home page, choose Guided Selling.Choose the All option from the dropdown box in the menu bar. | List of Opportunities is displayed. |  |
| 3 | Create Opportunity | Choose Create (+)Enter the following details:Name: Opportunity NameAccount : Account<17100005>Choose SaveNote The Account used here must be already present in the SAP Sales Cloud Version 2 system - replicated from SAP S/4HANA Cloud Public Edition. | A Opportunity is created successfully in SAP Sales Cloud Version 2 system. The new Opportunity is displayed in the Overview page. |  |
| 4 | Add product | Open the opportunity and scroll to the bottom of the page.Choose Products. In the dialog box, choose product by selecting Plus (+) , then click outside the window to accept.Note The product used here must be already present in the SAP Sales Cloud Version 2 system - replicated from SAP S/4HANA Cloud Public Edition.Stock Information details will be displayed if available. | New Section – Products appear with one product |  |
| 5 | Creating Sales Quote or External Sales Quote | Select the Sales Quotes and choose Create External Quote.In the new view, select Submit.Note A standard Sales Quote is created in the SAP Sales Cloud Version 2 system and the external quote is created in the SAP S/4HANA Cloud Public Edition system. | The message Quote Creation Triggered appears |  |
| 6 | Check Quote Card | Under section Sales Quote a card appears.Note The External Link setting allows for direct navigation to the Sales document within the SAP S/4HANA Cloud Public Edition system simply by selecting the External ID. | The Sales Quote Card has all the details of the Quote created in Step 5 |  |
| 7 | Launch SAP S/4HANA Cloud Public Edition | Once the external Sales Quote appears in the card, an external reference number is generated. The Quote name is clickable and provides direct navigation to the corresponding Sales Quote in the SAP S/4HANA Cloud Public Edition system.Note Please ensure that the External Navigation Link for Sales Document is properly configured as described in the corresponding section of the setup guide for scope item 6KO. | Successful log in to the created quotation |  |

### Sales Quote Simulation in SAP Sales Cloud Version 2

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
| 1 | Launch SAP Sales Cloud Version 2 | Enter the SAP Sales Cloud Version 2 system URL https://<tenantID>.crm.ondemand.com.In your browser, enter the User ID and Password, and Log On. | Successful log on. |  |
| 2 | Choose Sales Quotes Work center view |  | Sales Quotes are displayed. |  |
| 3 | Create Sales Quote | Select the  (add) icon. | Sales Quote Creation screen is displayed |  |
| 4 | Fill Quote Details | Document Type: <Standard Quote External Pricing>Account: <Search with S/4HANA ID eg. 17100003>Sales Organisation: <Search with S/4HANA ID in Ex-ternal ID eg. 1710>Distribution: <Direct Sales>Division: <Product Division 00> | Basic Details were entered |  |
| 5 | Enter Product | In the Products Table, select the  (add) icon and fill in the following fields:Product ID: <TG11>Quantity: <1>Confirm by selecting Actions. | Product was added |  |
| 6 | Save and Open Quotation | Select Save and Open. | Quotation details are displayed.The Pricing Status in totals is NOT CALCULATED. |  |
| 7 | Trigger Simulation | From the More menu (  more icon), select Simulate. | Following changes are visible on the screen:Pricing Status (totals): CALCULATED SUC-CESSFULLYNet Value (totals): <value fetched from backend>Gross Value (totals): <value fetched from backend>Net Value (Product): <value fetched from backend>Price (Product): <value fetched from backend> |  |

### Create Follow Up Sales Order from Sales Quote in SAP Sales Cloud Version 2 System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch SAP Sales Cloud Version 2 | Enter the SAP Sales Cloud Version 2 system URL https://<tenantID>.crm.ondemand.com.In your browser, enter the User ID and Password and choose Log On. | Successful login |  |
| 2 | View Sales Quotes | From the SAP Sales Cloud Version 2 home page, choose Sales Quotes. | List of Sales Quotes is displayed. |  |
| 3 | Create a Standard Sales Quote | From the SAP Sales Cloud Version 2 home page, choose Sales Quotes. Create a standard sales quote, and add business partners and products. Choose Save and Open. |  |  |
| 4 | Create Sales Order or External Sales Order | Choose Create (  ) under Sales Order, then select ERP Sales order to create an external sales order.Note A standard Sales Order is created in the SAP Sales Cloud Version 2 system and the external sales order is created in the SAP S/4HANA Cloud Public Edition system. |  |  |
| 5 | Check Sales Order Card | Under section Sales Order a card appears. | The Sales Order Card has all the details of the Sales Order created in Step 5 |  |
| 6 | Launch SAP S/4HANA Cloud Public Edition | Once the external Sales Order appears in the card, an external reference number is generated. The Sales Order is clickable and enables direct navigation to the corresponding sales order in the SAP S/4HANA Cloud Public Edition system.Note Please ensure that the External Navigation Link for Sales Document is properly configured as described in the setup guide. | Successful log in to the created Sales Order |  |

### Capture Sales Order Changes in SAP Sales Cloud Version 2

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch SAP Sales Cloud Version 2 | Enter the SAP Sales Cloud Version 2 system URL [https://tenantID.crm.ondemand.com](https://tenantID.crm.ondemand.com).In your browser, enter the User ID and Password and choose Log On. | Successful login |  |
| 2 | Pricing Simulation and Order Creation | After simulating the pricing as described in test step [Sales Quote Simulation in SAP Sales Cloud Version 2](#unique_17) [page ] 23 and creating an External Sales Order as described in test step [Create Follow Up Sales Order from Sales Quote in SAP Sales Cloud Version 2 System](#unique_13) [page ] 24. | The External Sales Order is successfully created in SAP Sales Cloud Version 2. |  |
| 3 | Navigate to the Sales Order in SAP S/4HANA Cloud Public Edition | A card is displayed under section Sales Order.Click on the External ID in the Sales Order card. This navigates you to the Sales Order in SAP S/4HANA Cloud Public Edition. | You are redirected to the corresponding Sales Order in the SAP S/4HANA Cloud Public Edition system. |  |
| 4 | Edit Sales Order in SAP S/4HANA Cloud Public Edition | In SAP S/4HANA Cloud Public Edition, choose Edit to make changes to the Sales Order.For example: You can change the Requested Quantity. Choose Save after completing you changes. | The updated Sales Order data is saved in SAP S/4HANA Cloud Public Edition. |  |
| 5 | Synchronization Confirmation | In the SAP Sales Cloud Version 2 system, navigate to the Sales Order tab and search for the sales order with the same External ID. Open the Sales Order; the updated quantity is reflected in the Products section. | Changes made in SAP S/4HANA Cloud Public Edition are automatically and instantly updated in SAP Sales Cloud Version 2. |  |

### Review Sales Order History in SAP Sales Cloud Version 2

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch SAP Sales Cloud Version 2 | Enter the SAP Sales Cloud Version 2 system URL https://<tenantID>.crm.ondemand.com.In your browser, enter the User ID and Password and choose Log On. | Successful login |  |
| 2 | Open the Sales Order Account | To follow up on the created Sales Order in the previous step, click on the account associated with the order. In the Account view, navigate to the available tabs (such as General, Product Tracking & Lists, etc.). | The account details page is opened. |  |
| 3 | Open Sales History tab | Select the Sales History tab. | The Sales Order history is displayed. |  |
| 4 | Review the Sales History | Review the Sales history, where all previously created Sales Orders for the account are displayed. | All previously created Sales Orders for the selected account are visible. |  |

### Delete Sales Quote Reference in SAP Sales Cloud Version 2

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Launch SAP Sales Cloud Version 2 | Enter the SAP Sales Cloud Version 2 system URL https://tenantID.crm.ondemand.com.In your browser, enter the User ID and Password and choose Log On. | Successful log in |
| 2 | View Opportunities | From the SAP Sales Cloud Version 2 home page, choose Guided Selling.Choose the All option from the dropdown box in the menu bar. | List of Opportunities is displayed. |
| 3 | Check Quote Card | Open an opportunity you’ve created and under the Sales Quote section a card appears.Note The External Link setting allows for direct navigation to the Sales document within the SAP S/4HANA Cloud Public Edition system by selecting the External ID. | The Quote Card has all the details of the External Quote created in [Create Follow Up Sales Quote from Opportunity in SAP Sales Cloud Version 2 System](#unique_12) [page ] 21 |
| 4 | Launch the SAP S/4HANA Cloud Public Edition system by entering the URL. | In your browser, enter the User ID and Password, and select Log On. | Successful log in |
| 5 | Access app | Open Display Sales Quotations application | Display Quotations page application is opened. |
| 6 | Find Replicated Quotation | In Quotation input field start typing name of the opportunity. Select the replicated opportunity | The ID has been displayed in Quotation input field |
| 7 | Open Quotation | Select Continue. | The replicated quotation is opened |
| 8 | Select Menu | Choose Sales document. Select Change, then Delete. | The external Sales Quote reference will be deleted immediately from the SAP Sales Cloud Version 2 system |

### Delete Sales Order Reference in SAP Sales Cloud Version 2

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch SAP Sales Cloud Version 2 | Enter the SAP Sales Cloud Version 2 system URL [https://tenantID.crm.ondemand.com](https://tenantID.crm.ondemand.com).In your browser, enter the User ID and Password and choose Log On. | Successful login |  |
| 2 | View Sales Quotes | From the SAP Sales Cloud Version 2 home page, choose Sales Quotes. The External Link setting allows for direct navigation to the Sales document within the SAP S/4HANA Cloud Public Edition system simply by clicking the External ID | List of Sales Quotes is displayed. |  |
| 3 | Check Order Card | Open a Sales Quote you’ve created, and a card will appear under the Sales Order section.Note The External Link setting allows for direct navigation to the Sales document within the SAP S/4HANA Cloud Public Edition system by selecting the External ID. | The Order Card has all the details of the external Order created in [Create Follow Up Sales Order from Sales Quote in SAP Sales Cloud Version 2 System](#unique_13) [page ] 24. |  |
| 4 | Launch SAP S/4HANA Cloud Public Editionsystem. | Enter the SAP S/4HANA Cloud Public Edition system URL.In your browser, enter the User ID and Password, and select Log On. | Successful login |  |
| 5 | Access app | Open Display Sales Orders application. | Display Sales Documents page is opened. |  |
| 6 | Find Replicated Order | Enter Order or enter the Customer Reference and Search for the order. | The order has been displayed in Order input field |  |
| 7 | Open Order | Select Continue. | The replicated order is opened. |  |
| 8 | Select Menu | Choose Sales document and select Change. Then, select Delete. | The external Sales Order reference will be deleted immediately from the SAP Sales Cloud Version 2 system |  |

### Create am Employee (Worker) in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch SAP S/4HANA Cloud Public Edition | Enter the SAP S/4HANA Cloud Public Edition system URLIn your browser, enter the User ID and Password, and choose Log On. | Successful logon |  |
| 2 | Open App | Open the Manage Workforce app. | The Manage Workforce screen is displayed. |  |
| 3 | Create a Worker | Click on Create to create a new worker. | The New: Worker screen is displayed. |  |
| 4 | Provide Mandatory Personal Information | In the General Information section, enter the Last Name, Email, and Worker ID. | All the required data related to the general information is filled in. |  |
| 5 | Provide Worker Type, Start Date, and End Date | Ensure that the Worker Type is Employee (BUP003) and adjust the Start Date and End Date according to your requirements. |  |  |
| 6 | Create Work Agreement | In the Work Agreements section, choose Create. | The Work Agreement screen is displayed. |  |
| 7 | Provide Company Code | Enter the Company Code and click on Apply. | The Work Agreement is created and available in the Work Agreement section. |  |
| 8 | Save the worker | Click on Create to save the worker. | The Employee (Worker) is created. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

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
- related-to :: [[08-sales-order-management/test-script-opportunity-to-order-with-sap-cloud-for-customer-1vp-765]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6KO_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 54,748 chars in the whole document
