---
id: 02-business-partner-and-product-master-data/test-script-integration-of-core-master-data-1ro-ae-758
title: "Test Script: Integration of Core Master Data (1RO_AE) (1RO_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1RO: replicating material, customer and supplier master data from an SAP on-premise system."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/core-master-data-integration]
aliases: [1RO_S4CLD2608_BPD_EN_AE]
keywords: [Integration of Core Master Data from On-Premise, core master data integration, material master data, business partner customer, business partner supplier, master data replication, communication scenarios, key mapping, business roles, test user role assignment]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1RO_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-758
topic: 02-business-partner-and-product-master-data/core-master-data-integration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Integration of Core Master Data (1RO_AE) (1RO_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1RO_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Integration of Core Master Data from On-Premise** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Integration of Core Master Data (1RO_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232847534)

[2 Prerequisites 4](#_Toc232847535)

[2.1 Additional Manual Configuration 4](#_Toc232847536)

[2.2 System Access 4](#_Toc232847537)

[2.3 Roles 4](#_Toc232847538)

[2.4 Preliminary Steps 5](#_Toc232847539)

[2.4.1 Adding Roles to the Test User 5](#_Toc232847540)

[2.4.1.1 Add Business Roles 5](#_Toc232847541)

[3 Overview Table 7](#_Toc232847542)

[4 Test Procedures 9](#_Toc232847543)

[4.1 Product Master Data 9](#_Toc232847544)

[4.1.1 Creating Material Master Data in SAP On Premise 9](#_Toc232847545)

[4.1.2 Confirm Material Master Data in SAP S/4HANA Cloud Public Edition System 10](#_Toc232847546)

[4.1.3 Change Material Master Data in SAP On Premise 11](#_Toc232847547)

[4.1.4 Confirm Material Master Data in SAP S/4HANA Cloud Public Edition System 12](#_Toc232847548)

[4.2 Business Partner - Customer 13](#_Toc232847549)

[4.2.1 Create Business Partner – Customer Master Data in SAP On Premise 13](#_Toc232847550)

[4.2.2 Check Business Partner Replication in SAP S/4HANA Cloud Public Edition System 14](#_Toc232847551)

[4.2.3 Change Customer Master Data in SAP On Premise 15](#_Toc232847552)

[4.2.4 Check Business Partner Replication in SAP S/4HANA Cloud Public Edition System 16](#_Toc232847553)

[4.3 Business Partner – Supplier 17](#_Toc232847554)

[4.3.1 Create Supplier Master Data in SAP On Premise 17](#_Toc232847555)

[4.3.2 Check Business Partner Replication in SAP S/4HANA Cloud Public Edition System 18](#_Toc232847556)

[4.3.3 Change Vendor Master Data in the SAP On Premise 19](#_Toc232847557)

[4.3.4 Check Business Partner Replication in the SAP S/4HANA Cloud Public Edition system 19](#_Toc232847558)

## Purpose

Overview

In this scope item, you learn how to integrate your SAP S/4HANA Cloud Public Edition system with another SAP S/4HANA Cloud Public Edition system or SAP S/4HANA Cloud Private Edition system for the purpose of replicating core master data objects, such as Business Partner, Customer, Supplier, and Product. Also, you gain knowledge on how to integrate the key mapping hub and key mapping client.

In business landscapes, it is important to maintain and distribute centralized master data such as Business Partner or Product to attached satellite systems. The integration instructions mentioned in this document help you achieve the same by utilizing the predefined communication scenarios for Business Partner SAP_COM_0008 and Product SAP_COM_0009.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/dd7398708554240d292222cf02113769)

### System Access

The test is conducted in the following systems:

| System | Details |
| --- | --- |
| SAP On Premise | <Provide details on how to access system for example, system client or URL> |
| SAP S/4HANA Cloud Public Edition | <SAP Fiori launchpad URL> |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

This is required to have the necessary authorization to load a specific object and to validate the data in the Fiori Launchpad:

SAP S/4HANA Cloud Public Edition

| Business Object Name | ID (Role Template) | Name (Role Template) | ID (Launchpad Space) | Name (Launchpad Space) |
| --- | --- | --- | --- | --- |
| Products | SAP_BR_PRODMASTER_SPECIALIST | Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC | Master Data - Products / Product Governance |
| Business Partners | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance |

### Preliminary Steps

#### Adding Roles to the Test User

Purpose

In this step you assign the roles of chapter Roles to the test user that are necessary for data replication.

##### Add Business Roles

Procedure

1. Access the SAP Fiori launchpad in SAP S/4HANA Cloud Public Edition.
2. On the Home screen, choose tile Maintain Business Users:
3. Enter the User name given by your System Administrator.

| Field Name | Description | User Action and Values | Comment |
| --- | --- | --- | --- |
| User Name | Name of the test user | User name |  |

1. Choose Go
2. Select the User in the Users list
3. Choose Edit
4. Choose Add Business Roles
5. On Add Business Roles list fill the needed Business role into the Search field and choose Enter
6. Select the needed Business role(s) and choose OK
7. Choose Save
8. Go back to the SAP Home screen.
9. Go Back to the previous screen

Result

You have created added the necessary roles for the specific object for data replication.

## Overview Table

This scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Product Master Data

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Creating Material Master Data in SAP On Premise](#unique_9) [page ] 9 | Administrator | MM01 | You've created material master data in the SAP On Premise system. |
| [Confirm Material Master Data in SAP S/4HANA Cloud Public Edition System](#unique_10) [page ] 10 |  |  | You've confirmed material master data in the SAP S/4HANA Cloud Public Edition system. |
| [Change Material Master Data in SAP On Premise](#unique_11) [page ] 11 | Administrator | MM02 | You've changed material master data in the SAP On Premise system. |
| [Confirm Material Master Data in SAP S/4HANA Cloud Public Edition System](#unique_12) [page ] 12 |  |  | You've confirmed material master data in the SAP S/4HANA Cloud Public Edition system. |

Business Partner - Customer

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Business Partner – Customer Master Data in SAP On Premise](#unique_13) [page ] 13 |  | Maintain Business Partner (BP) | You've created material master data in the SAP On Premise system. |
| [Check Business Partner Replication in SAP S/4HANA Cloud Public Edition System](#unique_14) [page ] 14 |  | Maintain Business Partner (BP) | You've checked the replication of the business partner in the SAP S/4HANA Cloud Public Edition system. |
| [Change Customer Master Data in SAP On Premise](#unique_15) [page ] 15 |  |  | You've changed customer master data in the SAP On Premise system. |
| [Check Business Partner Replication in SAP S/4HANA Cloud Public Edition System](#unique_16) [page ] 16 |  | Maintain Business Partner (BP) | You've checked the replication of the business partner in the SAP S/4HANA Cloud Public Edition system. |

Business Partner - Supplier

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Supplier Master Data in SAP On Premise](#unique_17) [page ] 17 |  | Maintain Business Partner (BP) | You've created material master data in the SAP On Premise system. |
| [Check Business Partner Replication in SAP S/4HANA Cloud Public Edition System](#unique_18) [page ] 18 |  | Maintain Business Partner (BP) | You've checked the replication of the business partner in the SAP S/4HANA Cloud Public Edition system. |
| [Change Vendor Master Data in the SAP On Premise](#unique_19) [page ] 19 |  |  | You've changed vendor master data in the SAP On Premise system. |
| [Check Business Partner Replication in the SAP S/4HANA Cloud Public Edition system](#unique_20) [page ] 19 |  | Maintain Business Partner (BP) | You've checked the replication of the business partner in the SAP S/4HANA Cloud Public Edition system. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Product Master Data

This section describes test procedures for each process step that belongs to this scope item.

#### Creating Material Master Data in SAP On Premise

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create material including basic data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Create Material | In the SAP On Premise system, go to transaction MM01. | Initial screen to create material opens. |  |
| 2 | Enter Material Basic Data | On the Create Material (MM01) (Initial screen), make the following entries:Material: Material numberIndustry sector: Mechanical engineeringMaterial type: Raw materials | A new window opens, showing the Select Views. |  |
| 3 | Choose Views | In the Select Views window, select Basic data 1 and Basic data 2 and choose Continue. | A new window opens, showing the Create Material (Raw materials) screen. |  |
| 4 | Enter Basic Data | On the Create Material (Raw materials) screen, in the Basic data 1 tab, enter the Material description (short text) |  |  |
| 5 | Enter Basic Data | On the Basic data 1 tab, in the General Data section, make the following entries:Base Unit of Measure: AULab/Office: 001 | You are navigated to the next tab, Basic Data 2. | Please don’t maintain value for other fields, otherwise, an additional configuration should be completed in customer guide before data replication. |
| 6 | Enter Basic Data | In the Basic Data 2 tab, you do not have to make any entries. | A new window Last data screen reached, opens with the message: You are about to exit. Do you want to save your data first? |  |
| 7 | Save Your Data | Choose Save. | The Basic Data is created and saved. |  |

#### Confirm Material Master Data in SAP S/4HANA Cloud Public Edition System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to check completeness of the replication data in the target SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using your user credentials. | The Home page displays. |  |
| 2 | Open Product Master application | In Product Master section, choose Display Material (MM03). |  |  |
| 3 | Display Material Master Data | In Display Material (Initial Screen), input the material name you just created in the SAP On Premise, then choose Continue. | A new window opens, showing the Select Views. |  |
| 4 | Choose Views | In the Select Views window, select Basic data 1 and Basic data 2 and choose Continue. | A new window opens, showing the Display Material (Raw materials) screen. |  |
| 5 | Confirm Material Master Data | You can check if the material master data is same as the data in ERP/ MDG system. |  |  |

#### Change Material Master Data in SAP On Premise

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you change a material including basic data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Create Material | In the SAP On Premise system, go to transaction MM02. | The Initial screen to change material displays. |  |
| 2 | Enter Material Basic Data | On the Change Material (MM02) (Initial screen), make the following entries:Material: Material number | A new window opens, showing the Select Views. |  |
| 3 | Choose Views | In the Select Views window, select Basic data 1 and Basic data 2 and choose Continue. | A new window opens, showing the Change Material (Raw materials) screen. |  |
| 4 | Change Basic Data | On the Change Material (Raw materials) screen, on the Basic data 1 tab, change the Material description (short text), and choose Continue. |  | Please don’t maintain value for other fields, otherwise, an additional configuration should be completed in customer guide before data replication. |
| 5 | Change Basic Data | In the Basic Data 2 tab, you do not have to make any entries. | A new window Last data screen reached opens with the message: You are about to exit. Do you want to save your data first?. |  |
| 6 | Save Your Data | Choose Save. | The Basic Data is changed and saved. |  |

#### Confirm Material Master Data in SAP S/4HANA Cloud Public Edition System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to check completeness of the replication data in the target SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using your user credentials. | The Home page displays. |  |
| 2 | Open Product Master application | In Product Master section, choose Display Material (MM03). |  |  |
| 3 | Display Material Master Data | In Display Material (Initial Screen), Input the material name you just created in SAP On Premise system, then choose Continue. | A new window opens, showing Select Views. |  |
| 4 | Choose Views | In the Select Views window, select Basic data 1 and Basic data 2 and choose Continue. | A new window opens, showing the Display Material (Raw materials) screen. |  |
| 5 | Confirm Material Master Data | You can check if the material master data has been changed as the data in SAP On Premise system. |  |  |

### Business Partner - Customer

#### Create Business Partner – Customer Master Data in SAP On Premise

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a Business Partner as Customer role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Create Business Partner | In the SAP On Premise system, go to transaction bp. | Initial screen to create Business Partner opens. |  |
| 2 | Select the type of Business Partner. | On the Maintain Business Partner (BP) (Initial screen), select Person or Organization or Group. For example choose Person. | Create Business Partner screen appears. |  |
| 3 | Select Customer role. | Select Customer (FLCU01) in create in BP role dropdown. And click create. | Create Business Partner – Customer screen appears with all fields related to a Customer. |  |
| 4 | Enter Address & Sales and Distribution data. | On the Address tab, in the Name section, make the following entries:Title,First Name,Last Name, Search term, Address details,Click Sales and Distribution button and maintain the following fields.Sales Org: 001Distr. Channel: 01Division: 01 | Manadatory check will be made. So, Check all the mandatory data are filled. |  |
| 5 | Save Your Data | Choose Save. | The Basic Data is created and saved. Note down the Business Partner Id. |  |

#### Check Business Partner Replication in SAP S/4HANA Cloud Public Edition System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the Customer replicated from the SAP On-Premise System.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch Home Page | Access the SAP S/4HANA Cloud Public Edition system using URL and log on with the appropriate user and password.For example,User: BUPA_MASTER_SPECIALISTPassword: Welcome1 | Successful login. |  |
| 2 | Access Business Partner | Open Maintain Business Partner (BP). | Business Partner maintenance screen opens. |  |
| 3 | Review the replicated customer from the SAP On Premise system | Enter the Customer Number created in STEP 4.2.1 in the Business Partner field and choose Next. | The Business Partner data is displayed. The replicated data is displayed. |  |
| 4 | Review the Customer Data | Select the Display in BP Role field as Customer.Then choose Sales and Distribution from the top. Navigate to the respective tabs for reviewing the replicated data. | The Sales Area data is replicated. |  |

#### Change Customer Master Data in SAP On Premise

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you edit a Customer in the On-Premise System.

Procedure

Edit the Customer Master data created in STEP 4.2.1 in the On-Premise system, For example Change the address data and send the same to the SAP S/4HANA Cloud Public Edition system.

#### Check Business Partner Replication in SAP S/4HANA Cloud Public Edition System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Here, you review the Customer changed in the SAP On Premise System.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch Home Page | Access the SAP S/4HANA Cloud Public Edition system using URL and log on with the appropriate user and password. | Successful login. |  |
| 2 | Access Business Partner | Open Maintain Business Partner (BP). | Business Partner maintenance screen opens. |  |
| 3 | Review the replicated customer from the SAP On Premise system | Enter the Customer Number created in STEP 4.2.1 in the Business Partner field and choose Next. | The Business Partner data is displayed. The replicated data is displayed. |  |
| 4 | Review the Customer Data | Select the Display in BP Role field as Customer.Navigate to the respective tabs for reviewing the replicated data. | The Changed Customer data is replicated. |  |

### Business Partner – Supplier

#### Create Supplier Master Data in SAP On Premise

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a Business Partner as Supplier/Vendor role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Create Business Partner | In the SAP On Premise system, go to transaction bp. | Initial screen to create Business Partner opens. |  |
| 2 | Select the type of Business Partner. | On the Maintain Business Partner (BP) (Initial screen), select Person or Organization or Group. For example choose Person. | Create Business Partner screen appears. |  |
| 3 | Select Vendor role. | Select Vendor (FLVN01) in create in BP role dropdown. And click create. | Create Business Partner –screen appears with all fields related to a Vendor. |  |
| 4 | Enter Address | On the Address tab, in the Name section, make the following entries:Title,First Name,Last Name, Search term, Address details, any other Vendor data if needed.Click the button Purchsing and maintain the following fields,Purch.organization: 0001Order Currency: EUR | Manadatory check will be made. So, Check all the mandatory data are filled. |  |
| 5 | Save Your Data | Choose Save. | The Basic Data is created and saved. Note down the Business Partner Id. |  |

#### Check Business Partner Replication in SAP S/4HANA Cloud Public Edition System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the Vendor replicated from the On-Premise System.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch Home Page | Access the SAP S/4HANA Cloud Public Edition system using URL and log on with the appropriate user and password.For example,User: BUPA_MASTER_SPECIALISTPassword: Welcome1 | Successful login. |  |
| 2 | Access Business Partner | Open Maintain Business Partner (BP). | Business Partner maintenance screen opens. |  |
| 3 | Review the replicated Vendor from SAP On Premise system. | Enter the Business Partner Id created in STEP 4.3.1 in the Business Partner field and choose Next. | The Business Partner data is displayed. The replicated data is displayed. |  |
| 4 | Review the Vendor Data | Select the Display in BP Role field as Vendor.Then choose Purchasing from the top. Navigate to the respective tabs for reviewing the replicated data. | The Purchasing Org data is replicated. |  |

#### Change Vendor Master Data in the SAP On Premise

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you edit a customer in the SAP On-Premise System.

Procedure

Edit the Customer Master data created in STEP 4.3.1 in the SAP On-Premise system, for example Change the address data and send the same to the SAP S/4HANA Cloud Public Edition system.

#### Check Business Partner Replication in the SAP S/4HANA Cloud Public Edition system

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Here, you review the Vendor changed in the SAP On Premise System.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch Home Page | Access the SAP S/4HANA Cloud Public Edition system using URL and log on with the appropriate user and password. | Successful login. |  |
| 2 | Access Business Partner | Open Maintain Business Partner (BP). | Business Partner maintenance screen opens. |  |
| 3 | Review the replicated Vendor from SAP On Premise system. | Enter the Business Partner Id created in STEP 4.3.1 in the Business Partner field and choose Next. | The Business Partner data is displayed. The replicated data is displayed. |  |
| 4 | Review the Vendor Data | Select the Display in BP Role field as Vendor.Navigate to the respective tabs for reviewing the replicated data. | The Changed Vendor data is replicated. |  |

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
- see-also :: [[16-two-tier-erp-and-central-finance/two-tier-master-data-replication-business-partner-master-customer-233]]
- see-also :: [[16-two-tier-erp-and-central-finance/two-tier-master-data-replication-product-master-customer-guide-234]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1RO_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 29,569 chars in the whole document
