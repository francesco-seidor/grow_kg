---
id: 08-sales-order-management/test-script-opportunity-to-order-with-sap-cloud-for-customer-1vp-765
title: "Test Script: Opportunity-to-Order with SAP Cloud for Customer (1VP) (1VP_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1VP: C4C-to-S/4HANA master data replication, opportunity, quote, sales order, equipment and BP blocking."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/crm-opportunity-to-order]
aliases: [1VP_S4CLD2608_BPD_EN_XX]
keywords: [Opportunity to Order with SAP Sales Cloud and Cloud for…, opportunity-to-order, test procedures, master data replication, business partner, sales quotes, opportunity management, equipment and functional location, business partner blocking, sap cloud for customer]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1VP_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-765
topic: 08-sales-order-management/crm-opportunity-to-order
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Opportunity-to-Order with SAP Cloud for Customer (1VP) (1VP_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1VP_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Opportunity to Order with SAP Sales Cloud and Cloud for Customer** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Opportunity-to-Order with SAP Cloud for Customer (1VP) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232853040)

[2 Prerequisites 4](#_Toc232853041)

[2.1 System Access and Roles 4](#_Toc232853042)

[2.2 Master Data, Organizational Data, and Other Data 5](#_Toc232853043)

[2.3 Business Conditions 6](#_Toc232853044)

[3 Overview Table 7](#_Toc232853045)

[4 Test Procedures 9](#_Toc232853046)

[4.1 Create and Change Material in SAP S/4HANA Cloud Public Edition System 9](#_Toc232853047)

[4.2 Request Material Stock 11](#_Toc232853048)

[4.3 Create and Change Business Partner in SAP S/4HANA Cloud Public Edition System 12](#_Toc232853049)

[4.4 Create Business Partner Relationship in SAP S/4HANA Cloud Public Edition 15](#_Toc232853050)

[4.5 Create and Change Accounts in SAP Cloud for Customer System 17](#_Toc232853051)

[4.6 Create New Contacts and Relationship in SAP Cloud for Customer System 20](#_Toc232853052)

[4.7 Create Opportunity 21](#_Toc232853053)

[4.8 Maintain Opportunity and Request Pricing from SAP S/4HANA Cloud Public Edition 23](#_Toc232853054)

[4.9 Create Follow up Sales Quote 24](#_Toc232853055)

[4.10 Create External Follow-Up Document for Sales Quote 25](#_Toc232853056)

[4.11 Create External Follow-Up Document for Opportunity 26](#_Toc232853057)

[4.12 Review Opportunity 28](#_Toc232853058)

[4.13 Sales Order Processing in SAP S/4HANA Cloud Public Edition (Optional) 29](#_Toc232853059)

[4.14 Customer Insights View (Optional) 30](#_Toc232853060)

[4.15 Create and Change Equipment and Functional Location 31](#_Toc232853061)

[4.16 Create and Change Equipment and Functional Location in SAP Cloud for Customer 34](#_Toc232853062)

[4.17 End of Purpose (Blocking) of Business Partner and Customer Master Data 36](#_Toc232853063)

[5 Appendix 38](#_Toc232853064)

[5.1 Process Integration 38](#_Toc232853065)

[5.1.1 Succeeding Processes 38](#_Toc232853066)

## Purpose

Overview

After implementing the steps in the Set up guide, you replicate master data from SAP S/4HANA Cloud Public Edition to SAP Sales Cloud. You can also create or change accounts and contacts in SAP Cloud for Customer, which are replicated to the SAP S/4HANA Cloud Public Edition.

In SAP Sales Cloud, you can leverage this data to create new opportunities and quotes. While doing so, prices can be calculated in the SAP S/4HANA Cloud Public Edition and sent back to SAP Sales Cloud. Sales orders in SAP S/4HANA can be created as a follow-up document from the SAP Sales Cloud quote.

Once the sales order is in SAP S/4HANA Cloud Public Edition, the sales order ID is sent back to SAP Sales Cloud. In the SAP Sales Cloud, you can check your sales documents for the sales order ID from SAP S/4HANA Cloud Public Edition. You may open and manage the sales order by accessing the SAP S/4HANA UI from your SAP Sales Cloud system via UI mashup.

Additionally, Equipment and Functional location can be replicated in both the directions. This requires additional license for SAP Event Mesh Service on BTP.

After implementing the steps in the setup guide, you replicate master data from SAP S/4HANA Cloud Public Edition to SAP Sales Cloud. You can also create or change accounts and contacts in SAP Cloud for Customer, which are replicated to the SAP S/4HANA Cloud Public Edition. Also, you can create or change accounts and contacts in SAP Cloud for Customer, which are replicated to the SAP S/4HANA Cloud Public Edition.

In SAP Sales Cloud, you can leverage this data to create new opportunities and quotes. While doing so, prices can be calculated in the SAP S/4HANA Cloud Public Edition and sent back to SAP Sales Cloud. Sales orders in SAP S/4HANA Cloud Public Edition can be created as a follow-up document from the SAP Sales Cloud quote.

Once the sales order is in SAP S/4HANA Cloud Public Edition, the sales order ID is sent back to SAP Sales Cloud. In the SAP Sales Cloud, you can check your sales documents for the SAP S/4HANA Cloud Public Edition sales order ID. You may open and manage the sales order by accessing the SAP S/4HANA Cloud Public Edition UI from your SAP Sales Cloud system via UI mashup.

Additionally, Equipment and Functional location can be replicated in both directions. This requires additional license for SAP Event Mesh Service on BTP.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access and Roles

The test should be conducted with the following system:

|  |
| --- |
| Note For system details contact your System Administrator. |

| System | Details |
| --- | --- |
| SAP Cloud for Customer System | Provide details on how to access system, for example, system client or URL |
| SAP S/4HANA Cloud Public Edition system | Provide details on how to access system, for example, system client or URL |

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Name (Role Template) | Description | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) |  |
| Field Sales Representative (CRM) | Description | SAP_CRM_BCR_SALESREPMentioned in Setting Up Integration Guide |  |  | Test user: FIELD_SALES_REP |
| Internal Sales Representative | On the SAP Fiori launchpad, the Internal Sales Representative with this role has access to view Sales Order and perform message monitoring | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / BillingMentioned in Setting Up Integration Guide | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC | Test user: INTERNAL_SALES_REP |
| Administrator - Data Replication | On the SAP Fiori launchpad, the Internal Sales Representative with this role has access to perform data replication from SAP S/4HANA Cloud Public Edition system. | SAP_BR_ADMINISTRATOR_DATA_REPL |  |  | Test user: INTERNAL_SALES_REP |
| Master Data Specialist - Business Partner Data | In the SAP Cloud for Customer system the Field Sales Representative creates a follow-up. On the SAP Fiori launchpad, the Internal Sales Representative with this role has access to view and create business partner data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC | Test user: INTERNAL_SALES_REP |
| Master Data Specialist - Product Data | On the SAP Fiori launchpad, the Internal Sales Representative with this role has access to view and create Product master data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC | Test user: INTERNAL_SALES_REP |
| Consolidation Specialist | On the SAP Fiori launchpad, the Internal Sales Representative with this role has access to maintain exchange rate tile | SAP_BR_CONSLDTN_SPECIALIST_POC |  |  |  |
| Maintenance Planner | On the SAP Fiori launchpad, the Internal Sales Representative with this role has access to Create, Change, and Display the technical objects. | SAP_BR_MAINTENANCE_PLANNER | Maintenance Planning | SAP_BR_MAINTENANCE_PLANNER |  |
| Data Privacy Specialist | On the SAP Fiori launchpad, the Internal Sales Representative with this role has access to blocking a business partner. | SAP_BR_DATA_PRIVACY_SPECIALIST | Data Protection and Privacy - Master Data / Data Protection and Privacy | SAP_CA_SPT_DPP_PC / SAP_BR_DATA_PRIVACY_SPECIALIST |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data to go through the test procedure. If you’ve installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

|  |
| --- |
| Note Currently SAP_COM_0008 Communication Scenario doesn’t support Third-Party Item Category Group for Product Replication. Please use product with standard Item Category for your testing. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)no batch |  |
| Material | TG12 | Trading Good for Reg. Trading (reorder point planning)no batch |  |
| Sold-to party | 1710000317100005 | Customer domestic 03Customer domestic 05 | You can test the scope item using another domestic customer.17100005 is for credit management. |
| Ship-to party | 1710000317100005 | Customer domestic 03Customer domestic 05 |  |
| Payer | 1710000317100005 | Customer domestic 03Customer domestic 05 |  |
| Plant | 1710 |  |  |
| Storage Location | 171A |  |  |
| Shipping Point | 1710 |  |  |
| Sales organization | 1710 |  |  |
| Distribution channel | 10 |  |  |
| Division | 00 |  |  |

|  |
| --- |
| Note Ensure the System Filter field is set to X before you proceed for the transactional data replication in the communication arrangements SAP_COM_0008 and SAP_COM_0009. |

### Business Conditions

Before the testing of the scope item, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BD9-Sell from Stock | All relevant steps described in the business conditions and preliminary steps chapters are completed. |

|  |
| --- |
| Note Some of the fields might not be visible in the default SAP Cloud for customer UI. You would need to adapt the screens as per your requirement. |

## Overview Table

The scope item Integration with SAP Cloud for Customer: Opportunity-to-Order consists of several process steps. They are listed in the table below.

Example

| Process Step | Business Role | UI Type | Expected Results |
| --- | --- | --- | --- |
| [Create and Change Material in SAP S/4HANA Cloud Public Edition System](#unique_7) [page ] 9 | Internal Sales Representative | SAP S/4HANA Cloud Public Edition Fiori UI | Material will be replicated to SAP Cloud for Customer |
| [Request Material Stock](#unique_8) [page ] 11 | Field Sales Representative | SAP Cloud for Customer | The material stock details are displayed. |
| [Create and Change Equipment and Functional Location](#unique_9) [page ] 31 | Maintenance Planner | SAP S/4HANA Cloud Public Edition Fiori UI | Equipment and Functional Location will be replicated to SAP Cloud for Customer |
| [Create and Change Business Partner in SAP S/4HANA Cloud Public Edition System](#unique_10) [page ] 12 | Internal Sales Representative | SAP S/4HANA Cloud Public Edition Fiori UI | Business Partner will be replicated to SAP Cloud for Customer system |
| [Create and Change Accounts in SAP Cloud for Customer System](#unique_11) [page ] 17 | Field Sales Representative | SAP Cloud for Customer UI | Account overview page is displayed after searching the right account to be viewed. Select the account to see the details of the account. Account team is displayed, new member can be added to the account team. |
| [Create New Contacts and Relationship in SAP Cloud for Customer System](#unique_12) [page ] 20 | Field Sales Representative | SAP Cloud for Customer UI | A new contact is created and it can be viewed and assigned under an account. |
| [Create Opportunity](#unique_13) [page ] 21 | Field Sales Representative | SAP Cloud for Customer UI | Opportunity is created in SAP Cloud for Customer |
| [Maintain Opportunity and Request Pricing from SAP S/4HANA Cloud Public Edition](#unique_14) [page ] 23 | Field Sales Representative | SAP Cloud for Customer UI | Pricing is received from SAP S/4HANA Cloud Public Edition system |
| [Create Follow up Sales Quote](#unique_15) [page ] 24 | Field Sales Representative | SAP Cloud for Customer UI | Sales Quote with external pricing is created as follow up to the opportunity |
| [Create External Follow-Up Document for Sales Quote](#unique_16) [page ] 25 | Field Sales Representative | SAP Cloud for Customer UI | Sales Order is created in the follow-up system |
| [Review Opportunity](#unique_17) [page ] 28 | Field Sales Representative | SAP Cloud for Customer UI | Review the Opportunity with Document Flow in SAP Cloud for Customer |
| [Sales Order Processing in SAP S/4HANA Cloud Public Edition (Optional)](#unique_18) [page ] 29 | Internal Sales Representative | SAP Fiori launchpad UI | Review the Sales Order Created in SAP S/4HANA Cloud Public Edition system. |
| [Create and Change Equipment and Functional Location in SAP Cloud for Customer](#unique_19) [page ] 34 | Field Sales Representative | SAP Cloud for Customer UI | Create and change an equipment and functional location in the SAP Cloud for Customer. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

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

Complete all activities described in the master data script Create Product Master of type Trading Good . You can find the [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) in the SAP Help Portal.

|  |
| --- |
| Note It's also possible to create a copy of an existing material from the SAP S/4HANA Cloud Public Edition system. |

Change Material

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch SAP S/4HANA Cloud Public Edition system | Enter the SAP S/4HANA Cloud Public Edition system URLIn your browser, enter the User ID and Password, and choose Log On. | You’ve successfully logged on. |  |
| 2 | Open App | Open Change Material (MM02). | Change Material page is opened. |  |
| 3 | Search Material with specific detail | In the Find field, enter any keyword or field value to search for a Material.For example:Material: TG11Description: TRAD.GOOD 11,PD,REG.TRADING | A list of accounts with details is displayed. |  |
| 4 | Choose Continue | Choose Continue to select this Material | Select View page appears. |  |
| 5 | Select Views | Select the required or All Views and choose Continue. | The Home page appears. The details of account team are displayed. |  |
| 6 | Select Organization Levels | Select the Sales Organizational Levels details if the pop up appears and choose Continue.If pop up does not appear, maintain this information under the header Sales TextFor example:Plant: 1710Sales Org. :1710Distr. Channel:10 | A new screen for selected material opens. |  |
| 7 | Change Material | Maintain the required changes for the Material. |  |  |
| 8 | Save the Material | On the Material Change Screen, choose Save. | The changes to Material are saved and is replicated to SAP Cloud for Customer system.Note It is possible that there are data replication filters applied for this replication. In which case you need to log in with the role SAP_BR_ADMINISTRATOR_DATA_REPL and use the app Replicate by replication Model to initiate a replication. Refer to the set-up instruction guide, topic Master Data Replication or contact your integration administrator for more details. |  |
| 9 | Launch SAP Cloud for Customer | Enter the SAP Cloud for Customer system URL https://<tenantID>.crm.ondemand.com.In your browser, enter the User ID and Password, and click Log On. | Successful login |  |
| 10 | Choose Product Work center view | On the top navigation bar, go toPRODUCTS > PRODUCTS.Choose the option All from the dropdown box in the menu bar | All products are displayed. |  |
| 11 | Search your Product | In the Search field, search the product which you recently changed in the SAP S/4HANA Cloud Public Edition system. | The relevant product is displayed. |  |
| 12 | Check the product | Open the product to validate if the changes are updated in SAP Cloud for Customer system. | All changes are updated and verified for the product. |  |

### Request Material Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can perform a stock request for a product in SAP Cloud for Customer from the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch SAP Cloud for Customer | Enter the SAP Cloud for Customer system URL https://<tenantID>.crm.ondemand.com.In your browser, enter the User ID and Password, and click Log On. | Successful login |  |
| 2 | Open the Products | On the Products list screen, choose the products to which you want to request stock. | The Products Overview screen is displayed. |  |
| 3 | Navigate to the Stock Overview tab | Navigate to the Stock Overview tab. | The stock details are displayed. |  |

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

Complete all activities described in the master data script Create Customer Master. You can find the [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) in the SAP Help Portal.

Create Business Partner Account or Contact

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch SAP S/4HANA Cloud Public Edition system | Enter the SAP S/4HANA Cloud Public Edition system URL.In your browser, enter the User ID and Password and choose Log On. | You’ve successfully logged on. |  |
| 2 | Access App | Open Maintain Business Partner(BP). | The Maintain Business Partner screen is displayed. |  |
| 3 | Create a BP account | Choose Organization. (for Account creation)OrChoose Person (for Contact creation) | Create Organization Page opens. |  |
| 4 | Choose the Role Customer | In Create in BP role choose FLCU01 Customer (for Sales).OrIn Create in BP role choose BUP001 Contact (for Contact).Then, choose Create in the pop-up. | Account of BP role FLCU01 (Customer) is chosen for creation.OrContact of BP role BUP001 is chosen for creation. |  |
| 5 | Give the mandatory data | Enter data in the mandatory fields for creation of Account: Name Country/RegCity LanguageOrEnter data in the mandatory fields for creation of Contact: Last Name Correspondence Lang | All the required data related to the BP account is filled.OrAll the required data related to the BP Contact is filled. |  |
| 6 | Save the Business Partner | Choose Save. | Business partner Account or Contact data is saved and a Business Partner ID is generated.Note It is possible that there are data replication filters applied for this replication. In which case you need to log in with the role SAP_BR_ADMINISTRATOR_DATA_REPL and use the app Replicate by replication Model to initiate a replication. Refer to the set-up instruction guide, topic Master Data Replication or contact your integration administrator for more details.The changes are saved to SAP Cloud for Customer system depending on the replication model settings. |  |
| 7 | Launch SAP Cloud for Customer | Enter the SAP Cloud for Customer system URL https://<tenantID>.crm.ondemand.com.In your browser, enter the User ID and Password, and select Log On. | Successful login. |  |
| 8 | Choose Customers Work center view | On the navigation bar, go to CUSTOMERS > ACCOUNTS >orOn the navigation bar, go to CUSTOMERS > CONTACTSChoose the option All from the dropdown box in the menu bar | All accounts or contacts are displayed. |  |
| 9 | Search your Business partner | In the Search field, search the business partner which you recently created in SAP S/4HANA Cloud Public Edition system | The relevant business partner account or contact is displayed. |  |

Change Business Partner

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch SAP S/4HANA Cloud Public Edition system | Enter the SAP S/4HANA Cloud Public Edition system URL.In your browser, enter the User ID and Password and choose Log On. | Successful login |  |
| 2 | Access App | Open Maintain Business Partner (BP). | The Maintain Business Partner screen is displayed. |  |
| 3 | Search Business Partner with specific detail | In the Find field enter any keyword or field value to search for a Business Partner.For example:Business Partner: 17100003Name: Domestic Customer US 3 | A list of accounts with details is displayed. |  |
| 4 | Open Business Partner overview page | Choose the Business Partner name | The Business Partner overview page is displayed. |  |
| 5 | Change Mode | Choose Switch Between Display and Change to enable change mode | Business Partner Overview page with change mode is displayed. |  |
| 6 | Change Business Partner | Maintain the required changes for the Business Partner |  |  |
| 7 | Save the Business Partner | On the Account Screen, choose Save | The changes are saved to SAP Cloud for Customer system. |  |
| 8 | Launch SAP Cloud for Customer | Enter the SAP Cloud for Customer system URL https://<tenantID>.crm.ondemand.com.In your browser, enter the User ID and Password, and click Log On. | Successful login. |  |
| 9 | Choose Customers Work center view | On the navigation bar, go to CUSTOMERS > ACCOUNTSChoose the option All from the dropdown box in the menu bar | All accounts are displayed. |  |
| 10 | Search your Account | In the Search field, search the account which you recently changed in the SAP S/4HANA Cloud Public Edition system | The relevant account is displayed. |  |
| 11 | Check the Account | Open the account to validate the changes are updated in SAP Cloud for Customer system. | All changes are updated and verified for the account. |  |

### Create Business Partner Relationship in SAP S/4HANA Cloud Public Edition

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch SAP S/4HANA Cloud Public Edition system | Enter the SAP S/4HANA Cloud Public Edition system URL.In your browser, enter the User ID and Password and choose Log On. | Successful login. |  |
| 2 | Access App | Open Maintain Business Partner(BP). | The Maintain Business Partner screen is displayed. |  |
| 3 | Search Business Partner with Specific Detail | In the Find field, enter any keyword or field value to search for a business partner. | A list of accounts with details is displayed. |  |
| 4 | Open the Business Partner Overview page | Choose the Business Partner (Account) name | The Business Partner Overview page is displayed. |  |
| 5 | Change mode | Choose Switch Between Display and Change to enable change mode | The Business Partner Overview page with change mode is displayed. |  |
| 6 | Create relationship | Choose Relationships | Maintain Relationships page is opened. |  |
| 7 |  | Choose Relationship Cat as FBUR001 – Has Contact Person |  |  |
| 8 |  | Choose a business partner contact in the field Relationship to BP and choose Create.Select the check box Standard and choose Continue | A success message appears. Relationship was applied. |  |
| 9 | Save the relationship | Choose Save. | Changes have been saved.Note It is possible that there are data replication filters applied for this replication. In which case you need to log in with the role SAP_BR_ADMINISTRATOR_DATA_REPL and use the app Replicate by replication Model to initiate a replication. Refer to the set-up instruction guide, topic Master Data Replication or contact your integration administrator for more details. |  |
| 10 | Launch SAP Cloud for Customer | Enter the SAP Cloud for Customer system URL https://<tenantID>.crm.ondemand.com.In your browser, enter the User ID and Password, and click Log On. | Successful login. |  |
| 11 | Choose Customers Work Center view | On the navigation bar, go to CUSTOMERS > ACCOUNTSChoose the option All from the dropdown box in the menu bar | All accounts are displayed. |  |
| 12 | Search your Account | In the Search field, search the account that you recently changed in SAP S/4HANA Cloud Public Edition system | The relevant account is displayed. |  |
| 13 | Check the Account | Open the account to validate the relationship changes are updated in SAP Cloud for Customer system and the contact appears on the account page. | All relationship changes are updated and verified for the account. |  |

### Create and Change Accounts in SAP Cloud for Customer System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create and change an account in the SAP Cloud for Customer system.

Procedure

1. Create Account.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch SAP Cloud for Customer | Enter the SAP Cloud for Customer system URL https://tenantID.crm.ondemand.com.In your browser, enter the User ID and Password and choose Log On. | Successful login |  |
| 2 | Choose Customers Work center view | In the top navigation bar, go to CUSTOMERS > ACCOUNTS.Choose the option All from the dropdown list in the menu bar. | All accounts are displayed. |  |
| 3 | Create Account with specific detail | On the Account list screen, choose Create (+) | Account Create page is opened. |  |
| 4 | Provide the following Account information | On the Account Create Screen, enter the required dataName: enter name For example: Test AccountRole: enter a role, for example: CustomerCountry/Region: enter Country/RegionCity: enter CityState: enter state | Data is accepted by the system.Note In case you select the role Prospect, the account is blocked from replicating to SAP S/4HANA Cloud Public Edition system. |  |
| 5 | Save the Account | On the Account create screen, choose Save | Account is created in the SAP Cloud for Customer system and replicated to SAP S/4HANA Cloud Public Edition system.Note It is possible that there are data replication filters applied for this replication. In which case you need to log in with the role SAP_BR_ADMINISTRATOR_DATA_REPL and use the app Replicate by replication Model to initiate a replication. Refer to the set-up instruction guide, topic Master Data Replication or contact your integration administrator for more details. |  |
| 6 | Launch SAP S/4HANA Cloud Public Edition system | Enter the SAP S/4HANA Cloud Public Edition system URLIn your browser, enter the User ID and Password, and chooseLog On | Successful login |  |
| 7 | Access App | Choose the Maintain Business Partner (BP) App | Maintain business partner page is opened. |  |
| 8 | Search Business Partner with specific detail | In the Find field, enter any keyword or field value to search for a Business Partner.For example:Name : Test Account | A list of Business Partner with details is displayed. |  |
| 9 | Open Business Partner overview page | Select the Business Partner name | The account created in SAP Cloud for Customer system is displayed. |  |

2. Change Account

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch SAP Cloud for Customer | Enter the SAP Cloud for Customer system URL https://tenantID.crm.ondemand.com.In your browser, enter the User ID and Password and choose Log On. | Successful login |  |
| 2 | Choose Customers Work center view | In the navigation bar, go to CUSTOMERS > ACCOUNTS.Choose the option All from the dropdown box in the menu bar | All accounts are displayed. |  |
| 3 | Search Account with specific detail | In the Find field, enter any keyword or field value to search for an account.For example:Account: 17100003Name: Domestic Customer US 3(This is optional. Either SAP S/4HANA Cloud Public Edition customer ID or SAP Cloud for Customer account ID can be used for the search.) | A list of accounts with details is displayed |  |
| 4 | Open Account overview page | Select the account name. | The account overview page is displayed. |  |
| 5 | Change Account | Maintain the change for this account. |  |  |
| 6 | Save the Account | Choose Save. | Your changes are saved in SAP Cloud for Customer system. The changes are replicated to SAP S/4HANA Cloud Public Edition System. |  |
| 7 | Launch SAP S/4HANA Cloud Public Edition system | Enter the SAP S/4HANA Cloud Public Edition system URLIn your browser, enter the User ID and Password, and choose Log On. | Successful login. |  |
| 8 | Access App | Choose the Maintain Business Partner (BP) App. | Maintain Business Partner page is opened. |  |
| 9 | Search Business Partner with specific detail | In the Find field, enter any keyword or field value to search for a Business Partner.For example:Business Partner: 17100003Name : Domestic Customer US 3 | A list of Business Partner with details is displayed. |  |
| 10 | Open Business Partner overview page | Select the Business Partner name | The Business Partner overview page is displayed. |  |
| 11 | Check Business Partner | Check the Business Partner for your changes | The changes are visible for this Business Partner. |  |

### Create New Contacts and Relationship in SAP Cloud for Customer System

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
| Note Avoid creating a new contact person and assigning the contact person to an account in a single step. This could lead to an error during the data replication in SAP S/4HANA Cloud Public Edition. Follow the following steps to avoid error. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | View contacts | From the SAP Cloud for Customer home page, choose CUSTOMERS > CONTACTS.Choose the All option from the dropdown box in the menu bar. | List of contacts is displayed. |  |
| 2 | Create contact | Choose Create (+)Enter the following details:First Name: first nameLast Name: last nameAccount: <select an account from the help Eg: 17100003 (Name: Domestic Customer US 3)>Choose Save | A contact is created successfully in SAP Cloud for Customer system. The contact is replicated to SAP S/4HANA Cloud Public Edition system.The new contact is displayed in the Overview page.Note It is possible that there are data replication filters applied for this replication. In which case you need to log in with the role SAP_BR_ADMINISTRATOR_DATA_REPL and use the app Replicate by replication Model to initiate a replication. Refer to the set-up instruction guide, topic Master Data Replication or contact your integration administrator for more details. |  |
| 3 | Launch SAP S/4HANA Cloud Public Edition system. | Enter the SAP S/4HANA Cloud Public Edition system URL.In your browser, enter the User ID and Password, and click Log On. | Successful login |  |
| 4 | Access App | Open Maintain Business Partner (BP). | Maintain Business Partner page is opened. |  |
| 5 | Search Business Partner with specific detail | In the Find field, enter any keyword or field value to search for a business partner.For example:Business Partner: 17100003Name: Domestic Customer US 3 | A list of business partner with details is displayed |  |
| 6 | Open Business Partner overview page | Click the business partner name. | The Business Partner overview page is displayed. |  |
| 7 | Check business partner relationship | Choose Relationship tab to check the business partner relationship | The Contact created in SAP Cloud for Customer system is visible as a relationship. |  |

### Create Opportunity

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create an opportunity in SAP Cloud for Customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch Home Page | Access the SAP Cloud for Customer system using URL https://tenantID.crm.ondemand.com and log on with the appropriate user and password.For example,User: DOMDIRECTSALESPassword: Enter the password. | Successful login |  |
| 2 | Choose Opportunities Work Center View | Choose Sales in the navigation bar and then choose Opportunities. | Opportunities Work Center is opened, and the list screen is shown. |  |
| 3 | Create New Opportunity | On the Opportunities list screen, choose Create (+) | Opportunity Create page is opened. |  |
| 4 | Provide the following opportunity information | On the Opportunity Create screen, enter the required dataName: Enter nameAccount: 17100003Primary Contact: Enter primary contactExpected Value: Enter expected valueStart Date: Enter a dateClose Date: Enter a dateProbability: Enter probabilityOwner: Enter Owner | Data is accepted by the system. |  |
| 5 | Save the Opportunity | On the Opportunity Create screen, choose Save. | Opportunity is saved in the SAP Cloud for Customer system. |  |
| 6 | Open the Account | Click on Account.For Example,Account: Domestic Customer US 3 | Account with details is displayed. |  |
| 7 | Open Customer 360 View | From the Actions dropdown menu, choose Customer 360 View. | The Customer 360 View opens in a new window.Note If you have configured Single Sign-On for your user in SAP Cloud for Customer and SAP S/4HANA system, the system authenticates the user in SAP Cloud Identity provider. If the SSO isn’t configured, then you have to log on manually to open the customer 360 view. |  |

### Maintain Opportunity and Request Pricing from SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can perform a pricing request for Opportunity in SAP Cloud for Customer from the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open the opportunity | On the Opportunities list screen, choose the opportunity to which you want to add a product. | Opportunity overview page is displayed. |  |
| 2 | Edit the opportunity | Choose Edit.Change the distribution channel.Distribution Channel: Direct SalesChoose Save. |  |  |
| 3 | Add product | On the top navigation bar, choose Products tab and choose Add on the top-right corner of the products screen.On the window, enter the following details:Product: Enter MaterialQuantity: Enter QuantityNotes: enter NotesChoose Add.Choose Save. | A window is displayed to add the products. |  |
| 4 | Request pricing | Select the product on the top-right corner of the products screen, choose More and choose Request Pricing. | Note Based on a sales order simulation in the SAP S/4HANA Cloud Public Edition backend, the price for the product is displayed on the products screen in the SAP Cloud for Customer application.Opportunity data is saved. |  |

### Create Follow up Sales Quote

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a Sales Quote and submit your Sales Quote for approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open the opportunity | On the Opportunities list screen, choose the opportunity to which you want to create a follow-up quote. | Opportunity overview page is displayed. |  |
| 2 | Edit the opportunity | Choose Edit on the SALES DOCUMENT page |  |  |
| 3 | Create a new sales quote | Select New from the SALES QUOTES section. | New Quote Create page is opened. Personalize the Create screen to show the Document Type field. |  |
| 4 | Verify the following information | On the New Quote screen, data is auto filled. Verify the following data:Document Type: Sales quote with external pricingAccount: 17100003Primary Contact: enter primary contactExternal Reference: enter any text for your referenceDate: enter valueOwner: Enter OwnerSales Unit: Choose Sales Unit | Data is accepted by the system. |  |
| 5 | Save and open the new quote | On the New Quote screen, choose Save and Open. | Sales quote is saved in the SAP Cloud for Customer system and overview page is opened. |  |
| 6 | Maintain product data | Product maintained in the opportunity is auto filled. |  |  |
| 7 | Enter product pricing | Choose Actions -> Request External Pricing from external system. | Price is fetched from the external system and displayed on the page. |  |
| 8 | Choose save | Choose Save. | Sales quote is saved in the SAP Cloud for Customer system. |  |
| 9 | Submit | From the Actions dropdown menu, choose Submit. | Sales Quotation is saved. |  |

### Create External Follow-Up Document for Sales Quote

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a follow-up document for sales quote in SAP Cloud for Customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch Home Page | Access the SAP Cloud for Customer system using URL https://tenantID.crm.ondemand.com and log on with the appropriate user password. | Successful login |  |
| 2 | Choose sales quotes work center view | Choose Sales in the navigation bar and then choose Sales Quotes. | Sales Quotes Work Center is opened, and the list screen is shown. |  |
| 3 | Open sales quote | Select the ID of the Sales Quote created in the previous step. | Sales Quote overview page is displayed. |  |
| 4 | Create external follow-up document for sales quote | Choose the Actions dropdown and then choose Create External Follow-up Document. | External follow-up document to this sales quote (for example, Sales Order) is saved in the SAP S/4HANA backend system. |  |

### Create External Follow-Up Document for Opportunity

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a follow-up document for sales quote in SAP Cloud for Customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch Home Page | Access the SAP Cloud for Customer system using URL https://tenantID.crm.ondemand.com and log on with the appropriate user and password.For example,User: DOMDIRECTSALESPassword: Enter the password. | Successful login |  |
| 2 | Choose Opportunities Work Center View | Choose Sales in the navigation bar and then choose Opportunities. | Opportunities Work Center is opened, and the list screen is shown. |  |
| 3 | Create New Opportunity | On the Opportunities list screen, choose Create (+) | Opportunity Create page is opened. |  |
| 4 | Provide the following opportunity information | On the Opportunity Create screen, enter the required dataName: Enter nameAccount: 17100003Primary Contact: Enter primary contactExpected Value: Enter expected valueStart Date: Enter a dateClose Date: Enter a dateProbability: Enter probabilityOwner: Enter Owner | Data is accepted by the system. |  |
| 5 | Save the Opportunity | On the Opportunity Create screen, choose Save. | Opportunity is saved in the SAP Cloud for Customer system. |  |
| 2 | Edit the opportunity | Choose Edit.Change the distribution channel.Distribution Channel: Direct SalesChoose Save. |  |  |
| 7 | Add product | On the top navigation bar, choose Products tab and choose Add on the top-right corner of the products screen.On the window, enter the following details:Product: Enter MaterialQuantity: Enter QuantityNotes: enter NotesChoose Add.Choose Save. | A window is displayed to add the products. |  |
| 8 | Create follow up Sales order | Choose Actions and select Create ERP Sales Order | A message on the UI displays “Action triggered successfully” |  |

### Review Opportunity

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the opportunity with the related sales documents in SAP Cloud for Customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch Home Page | Access the SAP Cloud for Customer system using URL https://tenantID.crm.ondemand.com and log on with the appropriate user and password. | Successful login |  |
| 2 | Choose Opportunities Work Center View | Choose Sales in the navigation bar and then choose Opportunities. | Opportunities Work Center is opened, and the list screen is shown. |  |
| 3 | Choose the Opportunity | From the Opportunities list screen, choose the opportunity you’ve created in step Create Opportunity. | Opportunity overview page is displayed. |  |
| 4 | Display Sales Documents | On the top-right corner of the Opportunity screen, choose Sales Documents from the Show tab menu. | Sales Quote or Sales Order is displayed in the list screen. |  |
| 5 | Choose Sales Quote | Choose the ID for Sales Quote or Sales Order. | Sales Quote or Sales Order overview page is displayed. |  |
| 6 | Display Documents Flow | Choose Document Flow tab. | Sales Order is displayed in the list screen. |  |
| 7 | Display Sales Order | In the Document Flow screen, choose Sales Order IDIn the SAP S/4HANA UI screen, log on with your INTERNAL_SALES_REP. | A separate screen opens with Sales Order in SAP S/4HANA UI. |  |

### Sales Order Processing in SAP S/4HANA Cloud Public Edition (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This scenario describes the entire process sequence for a standard sales process (sale from stock) with a customer. The business process encompasses all steps from creating an order to the clearing of a customer account after the payment is received.

Procedure

Complete all activities described in the test script of the scenario: Sell from Stock (BD9).

|  |
| --- |
| Note For any message processing error in SAP S/4HANA Cloud Public Edition system, check the message monitoring tile in the SAP S/4HANA Cloud Public Edition FLP system. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch Home Page | Access the SAP Cloud for Customer system using URL https://tenantID.crm.ondemand.com and log on with the appropriate user and password. | Successful login |  |
| 2 | Choose Sales Quote Work Center View | Choose Sales in the navigation bar and then choose Sales Quote. | Sales Quote Work Center is opened, and the list screen is shown. |  |
| 3 | Choose Sales Quote | Choose the ID for Sales Quote. | Sales Quote overview page is displayed. |  |
| 4 | Display Documents Flow | Choose Document Flow tab. | Sales Order and corresponding document flow (Outbound Delivery, Picking Request, Goods issue and Invoice) are displayed in the list screen. |  |

### Customer Insights View (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This scenario describes the entire process sequence for a standard sales process (sell from stock) with a customer. The business process encompasses all steps from creating an order to the clearing of a customer account after the payment is received.

Procedure

Complete all activities described in the test script of the scenario: Sell from Stock (BD9).

|  |
| --- |
| Note For any message processing error in SAP S/4HANA Cloud Public Edition system, check the message monitoring tile in the SAP S/4HANA Cloud Public Edition FLP system. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch Home Page | Access the SAP Cloud for Customer system using URL https://tenantID.crm.ondemand.com and log on with the appropriate user and password. | Successful login |  |
| 2 | Choose Customers Work center view | On the navigation bar, go to CUSTOMERS > ACCOUNTS,choose the option All from the dropdown box on the menubar. | All accounts are displayed. |  |
| 3 | Search Account with specific detail | In the Find field, enter any keyword or field value to search for an account.For example:Account: 17100003Name: Domestic Customer US 3(This is optional. You can use either SAP S/4HANA Cloud Public Edition customer ID or SAP Cloud for Customer account ID for the search.) | A list of accounts with details is displayed |  |
| 4 | Open Account overview page | Select the account name. | The account overview page is displayed. |  |
| 5 | Navigate to Customer Insight | Select the Customer Insight tab to open the overview | Customer Insight Overview is displayed. |  |

|  |
| --- |
| Note Credit Utilization and Recent Invoices details are only fetched from SAP S/4HANA Cloud Public Edition system. Make sure the data to be fetched exists in the S4 system. |

Display Credit Account Data chapter from BD6 scope item allows you to verify the existing data for Credit Utilization. Manage Billing Documents app can be used to check recent invoices of a customer. Only completed invoices are displayed on the Customer Insights Overview Tab.

### Create and Change Equipment and Functional Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create and change an Equipment and Functional Location in the SAP S/4HANA Cloud Public Edition system.

|  |
| --- |
| Note It’s mandatory that the material and business partner master data that is used in the creation of the technical objects (equipment and functional location) are already replicated to the SAP Cloud for Customer system before the technical objects equipment and functional location are replicated. |

Create Equipment and Functional Location:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch SAP S/4HANA Cloud Public Edition system | Enter the system URL in yourSAP S/4HANA Cloud Public Edition.In your browser, enter the User ID and Password, and choose Log On. | You’ve successfully logged on. |  |
| 2 | Open App | Open Create Technical Object. | Change Technical Object page is opened. |  |
| 3 | Create an Equipment or Functional Location. | Choose Technical Object Type as Equipment or Functional Location from the dropdown.Enter Technical Object Category, for example: as S (Customer Equipment) or M (Machine), and choose Continue. | CreateTechnical Object overview page is opened. |  |
| 4 | Enter equipment or Functional Location data. | The mandatory data is as follows:General Data: Description.Organizational Data: Partner Function (for example: <17100003>).Sales and Distribution: Sales Organization (for example: <1710> or <1010>), Distribution Channel, Division.(Only in case of Equipment) Additional Function > Show Serial Number Data: Material (for example: <TG11>), Serial Number. | Technical object is selected. |  |
| 5 | Choose Save | Technical Object (Equipment or Functional Location) is created. | A data is saved message appears. |  |

|  |
| --- |
| Note It's also possible to create a copy of an existing Technical Object - Equipment and Functional Location from the SAP S/4HANA Cloud Public Edition system. |

Change Equipment and Functional Location

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch SAP S/4HANA Cloud Public Edition system | Enter the SAP S/4HANA Cloud Public Edition system URLIn your browser, enter the User ID and Password, and choose Log On. | You’ve successfully logged on. |  |
| 2 | Open App | Open Change Technical Object. | Open Change Technical Object. |  |
| 3 | Search Technical Object with specific detail | Select the F4 help, enter any keyword or field value to search for an equipment or a functional location.For example:Equipment: 217100073Functional Location: 1710-SPA-SAC-PLAR4-INLT | A list of accounts with details is displayed. |  |
| 4 | Choose Select this result item | Choose Select this result item to select the Equipment or Functional Location | Technical Objects details page opens. |  |
| 5 | Choose Continue | Select on Continue to navigate into the details page | Technical Objects details page opens. |  |
| 6 | Change Technical Object (Equipment or Functional Location) | Maintain the required changes for the Technical Object (Equipment or Functional Location). |  |  |
| 7 | Save the Technical Object (Equipment or Functional Location) | On the Technical Object Change Screen, choose Save. | The changes to Technical Object (Equipment or Functional Location) are saved and is replicated to SAP Cloud for Customer system. |  |
| 8 | Launch SAP Cloud for Customer | Enter the SAP Cloud for Customer system URL https://<tenantID>.crm.ondemand.com.In your browser, enter the User ID and Password, and select Log On. | Successful login |  |
| 9 | Choose Installed Base Work center view | For Registered Product (Equipment):On the top navigation bar, go to Installed Base > Registered Product (also called Equipment in S4HCE).For Installation Point (Functional Location):On the top navigation bar, go to Installed Base > Installation Point (also called Equipment in S4HCE).Choose the option All from the dropdown box in the menu bar | All Installation points/ Registered products are displayed. |  |
| 10 | Search your Registered Product/Installation Points | In the Search field, search the registered product/installation points which you recently changed in SAP S/4HANA Cloud Public Edition system. | The relevant registered product/installation points are displayed. |  |
| 11 | Check the Registered Product/Installation Points | Open the registered product/installation points to validate if the changes are updated in SAP Cloud for Customer system. | All changes are updated and verified for the registered product/installation points. |  |

### Create and Change Equipment and Functional Location in SAP Cloud for Customer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create and change an equipment and functional location in the SAP Cloud for Customer system.

Prerequisites

It’s mandatory that the material and business partner master data that is used in the creation of the technical objects (equipment and functional location) are already replicated to the C4C system before the technical objects equipment and functional location are replicated.

Procedure

Create Equipment and Functional Location

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch Cloud for Customer system | Enter the SAP Cloud for Customer system URL [https://tenantID.crm.ondemand.com](https://tenantID.crm.ondemand.com).In your browser, enter the User ID and Password and choose Log On. | Successful login |  |
| 2 | Choose Installed Base Work center view | In the top navigation bar, go to Installed Base > Registered Product if you want to create and replicate an Equipment.In the top navigation bar, go to Installed Base > Installation Point if you want to create and replicate a Functional location.Choose the option All from the dropdown list in the menu bar. | All Registered Products/Installation Points are displayed. |  |
| 3 | Create an Equipment or Functional Location | Choose Create. | New Functional Location or New Registered product Page is opened. |  |
| 4 | Enter equipment or Functional Location data | The Mandatory data is as follows:General Data: Description.Customer: (for example: <17100003>).(Only in case of Equipment) Serial ID and Product.After entering the data, choose Save. | A new Equipment or Functional Location is created. |  |

Change Equipment and Functional Location

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch Cloud for Customer system | Enter the SAP Cloud for Customer system URL [https://tenantID.crm.ondemand.com](https://tenantID.crm.ondemand.com).In your browser, enter the User ID and Password and choose Log On. | Successful login |  |
| 2 | Choose Installed Base Work center view | In the top navigation bar, go to Installed Base > Registered Product if you want to create and replicate an Equipment.In the top navigation bar, go to Installed Base > Installation Point if you want to create and replicate a Functional location.From the dropdown list in the menu bar, select All. | All Registered Products/Installation Points are displayed. |  |
| 3 | Choose the Registered Product or Installation Point to be changed. | Search the equipment or functional location that you want to change, then choose it by clicking on the ID. | The registered product or installation point page opens. |  |
| 4 | Change the Registered Product or Installation Point. | Choose the edit icon.Make the necessary changed.Choose Save. | The registered product or installation point is successfully saved. |  |
| 5 | Logon to SAP S/4HANA Cloud Public Edition. | Enter the SAP S/4HANA Cloud Public Edition system URLIn your browser, enter the User ID and Password, and choose Log On. | You’ve successfully logged on. |  |
| 6 | Access App | Open the Change Technical Object (W0029) app. | The Change Technical Object screen is displayed. |  |
| 7 | Search your Registered Product or Installation Point with specific detail | Click on F4 help. To search for an equipment or a functional location, enter the required search criteria, for example a keyword or a value:Equipment: 217100073Functional Location: 1710-SPA-SAC-PLAR4-INLT | A list of technical objects with details is displayed. |  |
| 8 | Check the Registered Product/Installation Points | Open the Equipment/Functional Location to validate if the changes are updated in SAP S/4HANA Cloud Public Edition system. | All changes are updated and verified for the registered product/installation points. |  |

### End of Purpose (Blocking) of Business Partner and Customer Master Data

Purpose

In this activity, you can block Business Partner master data for which the associated customer data is blocked. The business partner will consider all residence periods of linked customer master data Personal data collected in master data can be blocked as soon as business activities for which this data was collected are completed and the residence period for this data has elapsed.

Prerequisites

It’s mandatory that you've assigned the relevant ILM objects to audit areas and set policies that include residence and retention rules. A business user with a business role template SAP_BR_DATA_PRIVACY_SPECIALIST (Configuration Expert - Business Process Configuration) containing the business catalog for information LifeCycle Man-agement (SAP_CORE_BC_ILM).

A BAdI needs to be implemented on the SAP Cloud for Customer system in order to execute business partner blocking (for more information on this, refer to the set instructions).

Procedure

Blocking a Contact Person

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch SAP S/4HANA Cloud Public Edition system | Enter the SAP S/4HANA Cloud Public Edition system URLIn your browser, enter the User ID and Password, and choose Log On. | You’ve successfully logged on. |  |
| 2 | Enter Business Partner ID | Open Block Master Data Business Partner (BP). | The Blocking of Business Partner Data screen is displayed. |  |
| 3 | EoP Check Execution Mode | Enter the Business Partner ID of the contact that you would like to block in the Business Partner Details. |  |  |
| 4 | Blocking Options | Choose Overall under End of Purpose Check Execution Mode. |  |  |
| 5 | Processing Options | Choose Consider Next Check Date under Options |  |  |
| 6 | Access App | Choose Production Mode under Processing Options. |  |  |
| 7 | Logs | Choose Complete from the drop down of Detail Log under Logs. |  |  |
| 8 | Execute Blocking | Choose Execute to execute blocking of business partner. | You see a successful message that the business partner is successfully blocked. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Sales Order Processing: Sell from Stock | Once the Sales Order is created in SAP S/4 HANA Cloud system, you can review it in SAP S/4HANA Fiori Launchpad |

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
- related-to :: [[08-sales-order-management/test-script-opportunity-to-order-with-sap-sales-cloud-version-2-6ko-11]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1VP_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 64,818 chars in the whole document
