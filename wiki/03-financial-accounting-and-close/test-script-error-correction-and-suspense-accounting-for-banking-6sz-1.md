---
id: 03-financial-accounting-and-close/test-script-error-correction-and-suspense-accounting-for-banking-6sz-1
title: "Test Script: Error Correction and Suspense Accounting for Banking (6SZ) (6SZ_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 6SZ: ECS configuration, journal entry upload/SOAP posting, error processing, workflow approval, and reversals."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/error-correction-and-suspense-accounting-banking]
aliases: [6SZ_S4CLD2608_BPD_EN_XX]
keywords: [Error Correction and Suspense Accounting for Banking, error correction and suspense accounting, ecs configuration, error categories, ecs environments, team management, approval workflow, journal entry posting, soap service posting, upload posting data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6SZ_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1188
topic: 03-financial-accounting-and-close/error-correction-and-suspense-accounting-banking
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Error Correction and Suspense Accounting for Banking (6SZ) (6SZ_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6SZ_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Error Correction and Suspense Accounting for Banking** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Error Correction and Suspense Accounting for Banking (6SZ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232826797)

[2 Overview Table 4](#_Toc232826798)

[3 Prerequisites 6](#_Toc232826799)

[3.1 System Access 6](#_Toc232826800)

[3.2 Roles 6](#_Toc232826801)

[3.3 Master Data, Organizational Data, and Other Data 7](#_Toc232826802)

[3.4 Business Conditions 7](#_Toc232826803)

[3.5 Preliminary Steps 7](#_Toc232826804)

[3.5.1 General Settings 8](#_Toc232826805)

[3.5.1.1 Define First-Level Checks 8](#_Toc232826806)

[3.5.1.2 Define ECS Environments 8](#_Toc232826807)

[3.5.1.3 Define Error Categories 10](#_Toc232826808)

[3.5.1.4 Assign Error Messages to Error Categories 11](#_Toc232826809)

[3.5.1.5 Assign Error Categories to Compound Error Categories 12](#_Toc232826810)

[3.5.1.6 Define More Fields 13](#_Toc232826811)

[3.5.1.7 Define Additional fields for Corrections to Line Items 14](#_Toc232826812)

[3.5.1.8 Define Custom fields for ECS Document Reference 15](#_Toc232826813)

[3.5.1.9 Create Number Ranges for ECS Run Identification 16](#_Toc232826814)

[3.5.1.10 Create Number Ranges for Document Numbers in ECS 17](#_Toc232826815)

[3.5.2 Workflow 18](#_Toc232826816)

[3.5.2.1 Define Functions 18](#_Toc232826817)

[3.5.2.2 Define Function Profiles 19](#_Toc232826818)

[3.5.2.3 Assign Function Profiles to Team Category 20](#_Toc232826819)

[3.5.2.4 Classify Functions for Team Category 21](#_Toc232826820)

[3.5.2.5 Define Team Types 22](#_Toc232826821)

[3.5.2.6 Manage Teams and Responsibilities 23](#_Toc232826822)

[3.5.2.7 Maintain Email Templates 25](#_Toc232826823)

[3.5.2.8 Manage Workflows for Error Documents 27](#_Toc232826824)

[4 Test Procedures 29](#_Toc232826825)

[4.1 Posting Journal Entries 29](#_Toc232826826)

[4.1.1 Post Journal Entries - SOAP Service 29](#_Toc232826827)

[4.1.2 Upload Posting Data 32](#_Toc232826828)

[4.2 Processing Errors in Journal Entries 35](#_Toc232826829)

[4.2.1 Process Error Documents (Deprecated) 35](#_Toc232826830)

[4.2.1.1 Team Management (Deprecated) 41](#_Toc232826831)

[4.2.1.1.1 Define Functions (Deprecated) 41](#_Toc232826832)

[4.2.1.1.2 Define Function Profiles (Deprecated) 42](#_Toc232826833)

[4.2.1.1.3 Assign Function Profiles to Team Category (Deprecated) 43](#_Toc232826834)

[4.2.1.1.4 Classify Functions for Team Category (Deprecated) 44](#_Toc232826835)

[4.2.1.1.5 Define Team Types (Deprecated) 45](#_Toc232826836)

[4.2.1.1.6 Manage Teams and Responsibilities (Deprecated) 46](#_Toc232826837)

[4.2.2 Error Correction - Without Worflow 49](#_Toc232826838)

[4.2.2.1 Process Error Documents (Workflow Not Enabled) 49](#_Toc232826839)

[4.2.3 Error Correction - With Worflow 54](#_Toc232826840)

[4.2.3.1 Process Error Documents (For Error Document Processors) 54](#_Toc232826841)

[4.2.3.2 My Inbox (For Error Document Approvers) 59](#_Toc232826842)

[4.3 Reversing Postings 61](#_Toc232826843)

[4.3.1 Reverse Posted Documents 61](#_Toc232826844)

[4.3.2 Reverse Posting Run 63](#_Toc232826845)

[5 Configuration Settings 66](#_Toc232826846)

## Purpose

Overview

You use Error Correction and Suspense Accounting (ECS) to monitor your general ledger (G/L) data quality and perform efficient error correction during the posting process in Financial Accounting (FI).

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Posting Journal Entries

| Process Step | App/Transaction/Service | Expected Results |
| --- | --- | --- |
| [Post Journal Entries - SOAP Service](#unique_3) [page ] 29 | SOAP Service - Journal Entry - Post (Asynchronous) | Uploads journal entries with the possible results:Uploaded without any error; no error document createdUploaded with hard errors/soft errors; error documents created |
| [Upload Posting Data](#unique_4) [page ] 32 | Upload Postings Data (F7319) | Uploads journal entries with the possible results:Uploaded without any error; no error document createdUploaded with hard errors/soft errors; error documents created |

Processing Errors in Journal Entries

| Process Step | App/Transaction | Expected Results |
| --- | --- | --- |
| [Process Error Documents (Deprecated)](#unique_5) [page ] 35 | Process Error Documents - Error Correction and Suspense Accounting (F7320) | To resolve soft and hard errors and create journal entries. |
| [Process Error Documents (Workflow Not Enabled)](#unique_6) [page ] 49 | Process Error Documents - Error Correction and Suspense Accounting (F7320A) | To resolve soft and hard errors and create journal entries. |
| [Process Error Documents (For Error Document Processors)](#unique_7) [page ] 54 | Process Error Documents - Error Correction and Suspense Accounting (F7320A) | To resolve soft and hard errors and submit error documents for approval. |
| [My Inbox (For Error Document Approvers)](#unique_8) [page ] 59 | My Inbox (F0862) | To approve/reject the error correction requests. |

Reversing Postings

| Process Step | App/Transaction | Expected Results |
| --- | --- | --- |
| [Reverse Posted Documents](#unique_9) [page ] 61 | Reverse Posted Documents (F7329) | To reverse error documents/posted documents (suspense postings, correction postings) |
| [Reverse Posting Run](#unique_10) [page ] 63 | Reverse Posting Run (F7496) | To reverse all documents created during an upload run or a SOAP call |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| General Ledger Accountant - Banks | SAP_BR_GL_ACCOUNTANT_BANKS | General Ledger | SAP_FIN_SPT_GL_ACCOUNTING_BNK_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Extensibility Specialist | SAP_BR_EXTENSIBILITY_SPEC | Extensibility / Extensibility | SAP_BR_EXTENSIBILITY_SPEC / SAP_CA_SPT_EXT_PC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Application Support Engineer - Banks | SAP_BR_APPL_SUPPORT_BANKS |  |  |  |
| Manager | SAP_BR_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |

The General Ledger Accountant - Banks (SAP_BR_GL_ACCOUNTANT_BANKS) role template will only be accessible if you have activated the Accounting Enhancements for Banking (5NU) scope item. If 5NU is not active for your account, please use the GL Enhancements: Error Correction and Suspense Accounting (SAP_FS_BC_GLE_ECS_PC) catalog when creating roles.

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | For example, 1710 for US |  |  |
| G/L Account | 10110101 | G/L Account - Banking |  |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| J58 - Accounting and Financial Close | Execute to create open posting periods. |

### Preliminary Steps

Execute the configuration activities described in the subtopics.

#### General Settings

##### Define First-Level Checks

Purpose

In this step, you define the first-level checks executed before auto-correction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define First-Level Checks | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define First-Level Checks. Choose Open Documentation for the found line item to see more details about this configuration activity. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define First-Level Checks activity is displayed. |  |
| 3 | Create First Level Checks | Choose New Entries and specify the following:1st LvlChk: <enter a value, for example, ECS1>Description: <enter a description, for example, ECS First Level Check> |  |  |
| 4 | Assign Fields for Check | Assign a field to the first level check that you defined in the previous step and choose Save:Field for First Level Check: <specify the field for first level check, for example, 'BUKRS'> |  |  |

##### Define ECS Environments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the ECS environment values. You can either use the default value or create your own value. Note that SAP delivered content cannot be edited or deleted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define ECS Environments activity | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define ECS Environments activity. Choose Open Documentation for the found line item to see more details about this configuration activity. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define ECS Environments activity is displayed. |  |
| 3 | Create Environment for Error Correction System | Choose New Entries and specify the following values:ECS Environment: <enter a value>Description: <enter a description>First-Level Check: <specify the first-level check that you defined in the Define First-Level Checks configuration activity>You can either create new entries or use the following test data provided by default:ECS Environment: SAPCLD_DFL (SAP Default ECS Environment for Cloud)First-Level Check: <specify the first-level check that you defined>The Process Sequence field is non editable and by default set to Post, Autocorrect, Post. |  |  |
| 4 | Assign Derivations | Select the environment variable, choose Assign Derivations folder, choose New Entries, specify the following values and choose Save:Strategy Category: <select a strategy category, for example, Validation and Substitution, Team Assignment>Sequence Number: <enter a sequence number, for example, 1001>Derivation Function: <specify the derivation function that needs to be mapped to the strategy category, for example, ECC_SUB> |  |  |
| 5 | Generate BRF Object | Select the relevant strategy category and choose Generate. | You are navigated to Business Rule Framework plus (BRFplus), where you can define rules for the strategy category you selectedThe following strategy categories are available:Validation and SubstitutionIf you select Validation and Substitution, the corresponding application ZECS_VALIDATION_SUBSTITUION gets generated in BRFplus. Search for this application and create rules for autocorrection and validation in the generated rule set.For more information on how to create rules, see the documentation for [Business Rule Framework plus (BRFplus)](https://help.sap.com/docs/SAP_S4HANA_CLOUD/8b78ae42ec1c4b75937806fcd4fd7d1c/9a6b67ce7c26446483af079719edf679.html?version=latest). |  |
| 6 | Assign additional strategy categories | Repeat steps 4 and 5 for each strategy category that you assign to the environment variable. |  |  |

##### Define Error Categories

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the error categories and can also assign fields from FI document line items to the error categories.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Error Categories | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Error Categories. Choose Open Documentation for the found line item to see more details about this configuration activity. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Error Categories activity is displayed. |  |
| 3 | Define Error Categories | Choose New Entries , specify the following, and chooseSave:Error Type: <enter a value for the error category, for example, AO>Short Description : <enter a description for the error category, for example, Account Error> |  |  |
| 4 | Assign Field Names | Assign a field to the error category that you defined in the step 3:Field Name: <select a field name, for example, HKONT> |  |  |

##### Assign Error Messages to Error Categories

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you assign error messages to the error categories that you defined. You can use the message class that you already created in your namespace by selecting it from the input help or entering it manually.

Message class GLE_ECS_MSG_S contains the messages provided by SAP. You cannot change these messages

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Assign Error Messages to Error Categories | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Assign Error Messages to Error Categories . Choose Open Documentation for the found line item to see more details about this configuration activity. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Error Messages to Error Categories activity is displayed. |  |
| 3 | Assign Error Message to Error Category | Choose New Entries make the following entries and choose Save:Message Class <select a message class, for example, F5>Message : <specify the message number, for example, 507>Error Type : <specify the error category for the message, for example, AO> |  |  |

##### Assign Error Categories to Compound Error Categories

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can define compound error categories and assign error categories to them.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Assign Error Categories to Compound Error Categories | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Assign Error Categories to Compound Error Categories. Choose Open Documentation for the found line item to see more details about this configuration activity. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Error Categories to Compound Error Categories activity is displayed. |  |
| 3 | Define Compound Error Category | Choose New Entries, specify values for the following fields, and choose Save:Cmpd Error: <enter a compound error category, for example, AO>Short Description: <enter a description for the compound error category, for example, Account Error> |  |  |
| 4 | Assign Error Category to Compound Error Category | Assign an error category that you defined in step 5 of [Define Error Categories](#unique_20) [page ] 10 to the compound error category that you defined in previous step, and choose Save:Error Type: <select an error category, for example, AO> |  |  |

##### Define More Fields

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the additional fields that you want to appear on the list table of the Process Error Documents - Error Correction and Suspense Accounting (F7320) app. For each field, you can specify whether the system is to display the original value, the posted value, or the correct value.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define More Fields. | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define More Fields. Choose Open Documentation for the found line item to see more details about this configuration activity. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define More Fields activity is displayed. |  |
| 3 | Define more fields | Choose New Entries, specify values for the following fields, and choose Save:Field Name: <enter a value, for example, HKONT>Orig Val: <select this checkbox if you want the app to display the original value of the field>Posted Val.: <select this checkbox if you want the app to display the posted value of the field>Corr. Val: <select this checkbox if you want the app to display the corrected value of the field>Sys.Field:Note that this field will be enabled automatically when we maintain the fields from the GLE_ECS_STR_DATE_TIME structure and the GLE_ECS_ITEM table. When this field is enabled, the values in Orig Val, Posted Val and Corr . Val fields will be cleared. |  |  |

##### Define Additional fields for Corrections to Line Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define which fields you want to edit before posting the error document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Additional fields for Corrections to Line Items . | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Additional fields for Corrections to Line Items . Choose Open Documentation for the found line item to see more details about this configuration activity. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Additional fields for Corrections to Line Items activity is displayed. |  |
| 3 | Define Editable Fields for Corrections to Line Items | Choose New Entries, specify values for the following fields, and choose Save:Severity of Error: <select hard/soft error>Field Name: <enter the name of the field that you want to edit>You can either create new entries or use the following test data provided by default:Severity of Error: AOField Name: PRCTR |  |  |

##### Define Custom fields for ECS Document Reference

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can define which custom fields the system fills with internal document references in ECS.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Custom fields for ECS Document Reference . | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Custom fields for ECS Document Reference . Choose Open Documentation for the found line item to see more details about this configuration activity. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Custom fields for ECS Document Reference activity is displayed. |  |
| 3 | Define Custom Fields | Choose New Entries, specify values for the following fields, and choose Save:Receiver Field : <enter a value, for example, XREF3> |  |  |

##### Create Number Ranges for ECS Run Identification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create number range intervals for generating run ID in ECS.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Create Number Ranges for ECS Run Identification. | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Create Number Ranges for ECS Run Identification. Choose Open Documentation for the found line item to see more details about this configuration activity. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Create Number Ranges for ECS Run Identification activity is displayed. |  |
| 3 | Create number ranges for ECS Run ID | Choose Change Intervals → Insert Line, specify the following values for the selected number range object GLE_ECS_RD, and choose Save:Number Range No: <enter a value>From No." <enter the lower limit of the interval>To Number: <enter the upper limit of the interval>External: <select internal/external>You can either create new entries or use the following test data provided by default:Number Range No : 01From No.: 0000000001To Number: 9999999999External : < deselected by default> |  |  |

##### Create Number Ranges for Document Numbers in ECS

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create number range intervals for the internal document numbers in ECS.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Create Number Ranges for Document Numbers in ECS | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Create Number Ranges for Document Numbers in ECS . Choose Open Documentation for the found line item to see more details about this configuration activity. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Create Number Ranges for Document Numbers in ECS activity. |  |
| 3 | Create Number Range | Choose Change Intervals → Insert Line, specify the following values for the selected number range object GLE_AWREF, and choose Save:Number Range No : <enter a value>Year:<enter the year>From No. <enter the lower limit of the interval>To Number <enter the upper limit of the interval>External : <select internal/external>You can either create new entries or use the following test data provided by default:Number Range No : 01Year:9999From No.0000000001To Number9999999999External : < deselected by default> |  |  |

#### Workflow

##### Define Functions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define functions that can be assigned to team members so that they can perform various tasks.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Functions | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Functions. Choose Open Documentation for the found line item to see more details about this configuration activity. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Functions activity is displayed. |  |
| 3 | Define Functions | Choose New Entries, specify the following, and choose Save:Function: <enter a value for the function>Function Description : <enter a description for the function>Note You must define two functions corresponding to the two function classifications delivered for ECS, one for the Ledger Oversight and Control (LOC) team and the other for the Line of Business (LOB) team.You can either create new entries or use the following test data provided by default:Function (LOC User): S_ECSADVNC (Ledger Oversight and Control User)Function (LOB User): S_ECSBASIC (Line of Business User) |  |  |

##### Define Function Profiles

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the function profiles and assigns functions to function profiles. You can group similar functions for a business process in a function profile.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Function Profiles | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Function Profiles. Choose Open Documentation for the found line item to see more details about this configuration activity. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Function Profiles activity is displayed. |  |
| 3 | Define Function Profiles | Choose New Entries , specify the following, and choose Save:Function Profile: <enter a value for the function profile>Function Profile Description : <enter a description for the function profile>You can either create new entries or use the following test data provided by default:Function Profile: S_GLE_ECS (Error Ownership Profile) |  |  |
| 4 | Map Functions to Function Profile | Select the function profile, choose Function Profile to Function Mapping folder, choose New Entries, select the functions that you created for error processing, and choose Save.You can either create new entries or use the following test data provided by default:Function Profile: S_GLE_ECS (Error Ownership Profile)The following functions are assigned by default to the GLE_ECS function profile:S_ECSADVNC (Ledger Oversight and Control User)S_ECSBASIC (Line of Business User) |  |  |

##### Assign Function Profiles to Team Category

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you assign a function profile to a team category.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Assign Function Profiles to Team Category | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Assign Function Profiles to Team Category. Choose Open Documentation for the found line item to see more details about this configuration activity. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Function Profiles to Team Category activity is displayed. |  |
| 3 | Assign Function Profiles to Team Category | Choose New Entries, select the team category GLE_ECS (Error Correction and Suspense Accounting), assign a function profile, and choose Save:Team Category: GLE_ECS (Error Correction and Suspense Accounting)Function Profile: <select the function profile that you newly created for error processing functions, or use the default function profile GLE_ECS (Error Ownership Profile)> |  |  |

##### Classify Functions for Team Category

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you classify functions for team categories.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Classify Functions for Team Category | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Classify Functions for Team Category. Choose Open Documentation for the found line item to see more details about this configuration activity. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Classify Functions for Team Category activity is displayed. |  |
| 3 | Classify Functions for Team Category | Choose New Entries, select the team category GLE_ECS, select the function and choose Save:Team Category: GLE_ECS (Error Correction and Suspense AccountingFunction: <select the function that you newly created for error processing>Function Classification: ECSADVNCD (Ledger Oversight and Control User) or ECSBASIC (Line of Business User) based on the function.Note You must define two entries corresponding to the two functions, one for the Ledger Oversight and Control (LOC) team and the other for the Line of Business (LOB) team.You can either create new entries or use the following test data provided by default:Table 1:Team CategoryFunctionFunction ClassificationGLE_ECSS_ECSADVNC (Ledger Oversight and Control User)ECSADVNCDGLE_ECSS_ECSBASIC (Line of Business User)ECSBASIC |  |  |

##### Define Team Types

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, can create and maintain team types for a standard team category.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Team Types | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Team Types. Choose Open Documentation for the found line item to see more details about this configuration activity. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Team Types activity is displayed. |  |
| 3 | Define Functions | Choose New Entries , specify the following, and choose Save:Team Type: <enter a value for the team type>Team Type Decsription: <enter a description for the team type>Team Category: GLE_ECS (Error Correction and Suspense Accounting)Note You must define two team types, one corresponding to the Ledger Oversight and Control (LOC) team and the other for the Line of Business team (LOB).You can either create new entries or use the following test data provided by default:The following team types are available and assigned by default to the GLE_ECS team category:S_ECS_ADVNCD (Ledger Oversight and Control Team)S_ECS_BASIC (Line of Business Team) |  |  |

##### Manage Teams and Responsibilities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the ledger oversight and control (LOC) team and line of business (LOB) teams for processing of error documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as Business Process Specialist. |  |  |
| 2 | Access App | Open Manage Teams and Responsibilities (F2412). | The Teams list page is displayed. |  |
| 3 | Create a new team | Choose Create.Note You can also copy teams from the existing team list. |  |  |
| 4 | Maintain General Information for the team | In the Team Information section, enter the following values:NameGlobal IDTypeDescriptionStatusYou can either create new entries or use the following test data provided by default:Name: <enter a name for the team, for example, Processor TeamType: S_ECS_ADVNCD (Ledger Oversight and Control Team) or S_ECS_BASIC (Line of Business Team)Status: <select Enabled>Note The Category: Error Correction and Suspense Accounting(GLE_ECS) is automatically populated when you select the team type. | New team is created. |  |
| 5 | Maintain Team Owner for the Team | The business process specialist can change or add team owners. If the business process specialist (who is creating the team) has a business user, this business process specialist is then defaulted as team ownerIn the Team Owners section, choose Create. Then either enter the business partner, or select one or more business partners. |  |  |
| 6 | Maintain Team Members for the New Team | In the Team Members section, choose Create. Then either enter the business partner, or select one or more business partners.Choose the relevant function value from F4 help for all business partners.Assign the functions to multiple business partners using Manage Functions.Then choose Create on the lower right.You can either create new entries or use the following test data provided by default:Business Partner: <select the user IDs of the members that you want to include in the team>Function: < select S_ECSADVNC (Ledger Oversight and Control User) as the function for each member> or S_ECSBASIC (Line of Business User | The ledger oversight and control team is created |  |
| 7 | Maintain Team Owner for the LOB team | The business process specialist can change or add team owners. If the business process specialist (who is creating the team) has a business user, this business process specialist is then defaulted as team ownerIn the Team Owners section, choose Create. Then either enter the business partner, or select one or more business partners. |  |  |
| 8 | Create Additional teams (if required) | Create more teams (for example, Approver team) by following the steps from 4 to 7. |  |  |

##### Maintain Email Templates

Purpose

In this activity, you create your own e-mail templates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to SAP Fiori launchpad as Business Process Specialist(SAP_BR_BUSINESS_PROCESS_SPEC) . | The SAP Fiori launchpad displays. |  |
| 2 | Open Maintain Email Templates | Open Maintain Email Templates(F1306). | The Maintain Email Templates is displayed. |  |
| 3 | Select Predelivered Template | On the Maintain Email Templates screen, choose the Predelivered (X) tab, and search for the template: GLE_ECS_WF_COMPLETE_NOTIFY.Select this email template, choose Copy then make below entries in the Copy Template dialog box:Prefix: <custom-prefix>_ for example, YY1_Email Template<Specify one of the following names based on the communication scenario for which you are creating the email template >:31000061_COMPLETE_POSITIVE(Email template for the completion of workflow)31000061_CRT_9 (Email template to inform that the error document is assigned to the processor)31000061_CRT_19 (Email template to inform that the error document is assigned to the approver)31000061_REJECTION (Email template to inform about the rejection of error document to the processor)31000061_RELEASE (Email template to inform about the assignment of the error document back to the processor group after release of error document)31000061_FAILED_POSTING (Email template to inform about the posting failure of the error document to the processor and the approver)31000061_WITHDRAW (Email template to inform about the withdrawal of the error document from the approver)Name: specify a description for the email templateChoose Copy.Note A custom email template gets created based on the<prefix>_<email template name>naming pattern and is available in the Custom (X)tab. For example, the custom template name for the complete positive workflow scenario will look as follows: YY1_31000061_COMPLETE_POSITIVE, where YY1 is the custom prefix and 31000061_COMPLETE_POSITIVE is the email template naming convention proposed for this scenario. | All predelivered e-mail templates are displayed. |  |
| 4 | Select Custom Template in Custom Tab | Locate the custom e-mail template in the Custom tab | The Email Template screen displays. |  |
| 5 | Change Customer E-mail Template | Choose Change Details. | The Change Template dialog box displays. |  |
| 6 | Change Customer E-mail Template | Adjust the e-mail subject and body accordingly, then choose Save. | The customer email template is adjusted successfully. |  |

##### Manage Workflows for Error Documents

Purpose

In this step, you can create and manage approval workflow scenarios in the Manage Workflows for Error Documents app.

|  |
| --- |
| Note When 6SZ is activated, the Error Document Verification and Approval (WS31000061) workflow scenario is automatically enabled, allowing you to create and manage workflows using this app. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Logon to SAP Fiori Launchpad as Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT) | The Fiori Launchpad is displayed. |  |
| 2 | Open Manage Workflow for Error Documents | Open Manage Workflows for Error Documents. | The Manage Workflows screen is dis played. |  |
| 3 | Create Workflow | Create a new workflow from scratch or copy the default workflow and modify it as requiredCopy the default template and adjust as required:Select the default workflow, Error Document VerificationChoose CopyCreate a new template from scratch, choose Create. | When copying the default template to create a new template, the Copy Workflow screen is displayed.If you create a new template from the scratch, then the New Workflow screen is dis played. |  |
| 4 | Create Manage Workflow | If you create a new template, by copying from the default template, then the Copy Workflow screen appears with preconfigured steps and other attributes. You only need to define the start conditions and other parameters. For more details, refer the steps below.If you create a new template from the scratch, proceed as follows:On the New Workflows screen, make the following entries and choose Save:HeaderIn this section, specify the name of the workflow.Start Conditions:In this section, select the applicable preconditions and specify their corresponding values. The workflow is triggered only when all defined preconditions are met. For example, if you are creating a workflow specifically for hard errors, you can set the Severity precondition to Hard Error.Steps:In this section create the workflow steps with their respective preconditions and recipients. You can define one or more steps and the steps are executed in the defined order. To create a new workflow step, refer the following step. | The Workflow for Error Correction is configured. |  |
| 5 | Create Step | On the New Step screen, make the following entries and choose Create:HeaderIn this section, specify the name of the workflow step.RecipientsIn this section, you can assign a recipient to the step and you can specify if the choice of recipients is role-based or team-based. If you assign a team as the recipient of a step, then all members of that team are assigned the responsibility of that step. Instead of you assign a role, then all users assigned to that role will be responsible for the completion of that step.Step ConditionsIn this section, select the applicable preconditions and specify their corresponding values. The workflow step is triggered only when all defined preconditions are met.Note Repeat this step to create individual steps that you want to configure in your workflow. For example, you can create a step for error correction, another step for correction approval and another one for document posting. |  |  |
| 6 | Configure Notifications | In this section, specify the email template and the recipient to whom the mail notifications are to be sent at the end of a workflow. |  |  |
| 7 | Activate Workflow Item | Select the workflow that you created and choose Activate. | The Workflow gets activated. |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Posting Journal Entries

#### Post Journal Entries - SOAP Service

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can post journal entries asynchronously from external systems via the error correction and suspense accounting gateway for error correction.

Prerequisites

Ensure that the following attributes are already configured and available:

- Communication user and password - using the Maintain Communication Users app
- Communication system with communication user linked to it - using the Communication Systems app
- Communication arrangement for the communication scenario SAP_COM_0002 with the communication system assigned - using the Communication Arrangements app. In the Inbound Services section of this app, choose the Journal Entry - Post (Asynchronous) inbound service and download the WSDL file corresponding to it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch Tool | Open an API platform tool. |  |  |
| 2 | Import WSDL | Import the WSDL file corresponding to the inbound service Journal Entry - Post (Asynchronous). |  |  |
| 3 | Log On | In the tool, maintain the communication user name and password for the Journal Entry - Post (Asynchronous) inbound service that you just imported. | The service URL gets autopopulated when you import the WSDL file. |  |
| 4 | Message GUID | Add the suffix "?MessageId={{$guid}}" to the service URL. |  |  |
| 3 | Post | Copy the following sample payload, update based on your scenario, and choose Send.Sample Code<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sfin="http://sap.com/xi/SAPSCORE/SFIN"> <soapenv:Header/> <soapenv:Body> <sfin:JournalEntryBulkCreateRequest> <MessageHeader> <CreationDateTime>2023-03-25T09:00:00Z</CreationDateTime> <ID>MSG_2023-03_25_01</ID> </MessageHeader> <JournalEntryCreateRequest> <MessageHeader> <CreationDateTime>2023-03-25T09:00:00Z</CreationDateTime> <ID>SUBMSG_2023-03-25_01</ID> </MessageHeader> <JournalEntry> <OriginalReferenceDocumentType>BKPFF</OriginalReferenceDocumentType> <OriginalReferenceDocument>00001</OriginalReferenceDocument> <OriginalReferenceDocumentLogicalSystem>TESTSYS</OriginalReferenceDocumentLogicalSystem> <BusinessTransactionType>RFBU</BusinessTransactionType> <AccountingDocumentType>SA</AccountingDocumentType> <DocumentReferenceID>Test CFIN</DocumentReferenceID> <DocumentHeaderText>Test Supplier Invoice</DocumentHeaderText> <CreatedByUser>CFIN_USER</CreatedByUser> <CompanyCode>1710</CompanyCode> <DocumentDate>2023-03-20</DocumentDate> <PostingDate>2023-03-20</PostingDate> <Reference1InDocumentHeader>TEST1</Reference1InDocumentHeader> <Reference2InDocumentHeader>TEST2</Reference2InDocumentHeader> <ECSEnvironment>SAPCLD_DFL</ECSEnvironment> <Item> <GLAccount>10110101</GLAccount> <AmountInTransactionCurrency currencyCode="USD">10</AmountInTransactionCurrency> <AmountInGroupCurrency currencyCode="USD">10</AmountInGroupCurrency> <DebitCreditCode>S</DebitCreditCode> <DocumentItemText>GL account item</DocumentItemText> <AccountAssignment> <CostCenter>17109000</CostCenter> </AccountAssignment> </Item> <Item> <GLAccount>10110401</GLAccount> <AmountInTransactionCurrency currencyCode="USD">-10</AmountInTransactionCurrency> <AmountInGroupCurrency currencyCode="USD">-10</AmountInGroupCurrency> <DebitCreditCode>H</DebitCreditCode> <DocumentItemText>GL account item</DocumentItemText> <AccountAssignment> <CostCenter>17109000</CostCenter> </AccountAssignment> </Item> </JournalEntry> </JournalEntryCreateRequest> </sfin:JournalEntryBulkCreateRequest> </soapenv:Body> </soapenv:Envelope> | The app creates entries in the target system. |  |
| 4 | Monitor Messages | Open the Message Dashboard app (on the SAP Fiori Launchpad) to view all messages related to the POST operation that you executed. |  |  |

#### Upload Posting Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can upload journal entries via the error correction and suspense accounting gateway for error correction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | If 5NU is activated, then, log on to the SAP Fiori launchpad as a General Ledger Accountant - Banks.If 5NU is not activated, then proceed as follows:Create a business role with the GL Enhancements: Error Correction and Suspense Accounting (SAP_FS_BC_GLE_ECS_PC) business catalog with dependencies. For more details, see How to Create a New Business Role topic in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html))Create a business user (see How to Maintain Business Users topic in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html))Log on to the SAP Fiori launchpad with the user you created in the previous step |  |  |
| 2 | Access App | Open Upload Posting Data - Error Correction and Suspense Accounting (F7319). |  |  |
| 3 | Download template file | On the entry screen, choose Download Template. | The template file is downloaded |  |
| 4 | Prepare the template file | Make the following entries in the template file and save it locally:ECS Environment Variable: for example, SAPCLD_DFL This is a mandatory field.External Run ID: enter a value to identify the upload runDecimal Format: specify the decimal format to identify the decimal separator for amount fields in the input fileHeader Information (Field Names with H_ as prefix)Company code: <enter a company code, for example, 1710>Document Type: <enter a document type, for example,SA>Document Date: <enter document date, for example, current date>Posting Date: <enter posting date, for example, current date>Posting Period: <enter posting period, for example, current month>Currency: USDLine-Item Information (Field Names with L_ as prefix)Posting Key: <enter posting key, for example, 40, 50>Amount: <enter amount>G/L Account: <enter G/L account, for example, 10110101>Data Source: <enter data source, for example, DEPOSIT01> |  |  |
| 5 | Upload the file | Drag and drop the CSV file with journal entries to the app center panelorChoose Upload button, select the CSV file and choose Open | The app displays an entry corresponding to each file that you upload, on the next screenAgainst each entry, you can view the following information:Last Edited OnStatusRun IDNote that this field will only be displayed for files with Posted status.If you specify Run ID in the input file, the same run ID is displayed against the file entry once the file is postedIf you do not specify the Run ID in the input file, the app automatically generates a run ID based on the number range that you configured and displays it against the file entry.You can select only one file for upload at a time. |  |
| 6 | Posting an uploaded file | Select an uploaded file and choose Post | Uploaded File with Validated StatusThe app does the following:Generates error documents in case of hard and soft errors in the uploaded fileCreates journal entries (intermediate, autocorrected) in case of soft errors in the uploaded fileCreates journal entries for entries posted without any errorsNote that you can post only one file at a time.Uploaded File with Error/Posted StatusYou cannot post an uploaded file with the following statuses:ErrorPosted |  |
| 7 | Deleting an uploaded file | Select an uploaded file and choose Remove | The selected file entry is removed from the app. |  |
| 8 | Displaying Log | Choose View Log | The app displays the application log, where you can search for messages, exceptions, and errors that occured during the upload. |  |

### Processing Errors in Journal Entries

#### Process Error Documents (Deprecated)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can process the soft errors and hard errors that occurred during the file upload.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | If 5NU is activated, then, log on to the SAP Fiori launchpad as a General Ledger Accountant - Banks.If 5NU is not activated, then proceed as follows:Create a business role with the GL Enhancements: Error Correction and Suspense Accounting (SAP_FS_BC_GLE_ECS_PC) business catalog with dependencies. For more details, see How to Create a New Business Role topic in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html))Create a business user (see How to Maintain Business Users topic in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html))Log on to the SAP Fiori launchpad with the user you created in the previous step |  |  |
| 2 | Access App | Open Process Error Documents - Error Correction and Suspense Accounting (F7320). |  |  |
| 3 | Start Selection | On the entry screen, specify values for one or more of the following fields and choose Go:Compound Category : <Compound error category, for example, AO>Status: <Status of error document, for example, New, In Process, Corrected>Severity: <Severity of error, for example, hard error/soft error>Posted Company Code: Company code associated with the posted document, for example, 1710>Error Document: <Error document number>Created On: <Date/date range of error document creation, for example, today or current week>Changed On: Date/date range of error document update, for example, today, current week, last month>You may need to choose Adapt Filters to show/hide some fields. | Case 1If your organization configures an ECS environment without activating the Team Assignment feature, you can view a list of all error documents.Case 2If your organization configures an ECS environment by activating the Team Assignment feature, your user can be classified as one of the following based on the team function assigned to you:LOC user: As an LOC user, you can view error documents assigned to all other LOC and LOB teamsLOB user: As an LOB user, you can view error documents assigned only to your teamCase 3If your organization configures multiple ECS environments, one with the Team Assignment feature active and the other without activating the Team Assignment featureFor the ECS environment for which the Team Assignment feature is not active, you can view a list of all error documents linked to that ECS environment. However, you cannot view any error documents belonging to the other ECS environment for which the Team Assignment feature is active.For the ECS environment for which the Team Assignment feature is active,your user is classified as one of the following based on the team function assigned to you:LOC user: As an LOC user, you can view error documents assigned to all other LOC and LOB teamsLOB user: As an LOB user, you can view error documents assigned only to your teamAs an LOB or an LOC user, you cannot view any error documents belonging to the other ECS environment for which the Team Assignment feature is not active. |  |
| 4 | View Error Details | Select an error document (hard error) and navigate to the detailed screen | Hard Error with New StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Corrected Values section contains the same values as that of the Original Values section.The Posted Values section contains no values. |  |
|  |  |  | Hard Error with In Process StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Corrected Values section contains the corrections made to the original values ( (but not posted).The Posted Values section contains no values. |  |
|  |  |  | Hard Error with Corrected StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Corrected Values section contains the the corrections made to the original values before posting.The Posted Values section contains the corrected values from the posted document. |  |
|  |  |  | Hard Error with Reversed StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Corrected Values section contains the the corrections made to the original values before posting.The Posted Values section contains the corrected values from the posted document. |  |
|  |  |  | Hard Error with Deleted StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Corrected Values contains either the original values or corrections made to the original values (but not posted).The Posted Values contains no values (only errors with New /In Process status can be deleted). |  |
|  |  | Select an error document (soft error) and navigate to the detailed screen. | Soft Error with New StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Posted Values section contains values from the autocorrected posted document, for example, suspense postings.The Corrected Values section contains the same values as that of the Posted Values section. |  |
|  |  |  | Soft Error with In Process StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Posted Values section contains values from the autocorrected posted document, for example, suspense postings.The Corrected Values section contains the corrections that you saved (but not posted). |  |
|  |  |  | Soft Error with Corrected StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Posted Values section contains values from the autocorrected posted document, for example, suspense postings.The Corrected Values section contains the manual corrections that you posted. |  |
|  |  |  | Soft Error with Reversed StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Posted Values section contains values from the autocorrected posted document, , for example, suspense postings.The Corrected Values section contains the manual corrections that you posted. |  |
| 13 | Selection of Error Documents for Correction | Select one or more error documents with the following statuses and choose Edit:NewIn Process | The app opens the Edit screen.Note that you cannot edit error documents with the following statuses:ReversedCorrectedDeleted |  |
| 14 | Correct Error Items | On the Edit screen, correct the field values with errors, and choose Save. | The app displays the updated values in the Corrected Values section on the detailed page.Note The Compound Error Category linked to the error messages displayed for an error document determines the fields that you can edit for an error document. See the Related Information section for more details.For New items, the status changes from New to In Process.For In Process items, the status remains the same. |  |
| 15 | Post after Error Correction | Select one or more error documents with the following statuses and choose Post:NewIn Process | The app posts the entries and changes the status of the error documents to Corrected.Note that you cannot edit/post error documents with the following statuses:ReversedCorrectedDeleted |  |
| 16 | Selection of Error Documents for Processor Assignment | Select one or more error documents with the following statuses and choose Assign Processor:NewIn Process | The app opens the Assign Processor screen. |  |
| 17 | Assign a Processor | Select the business partner ID of the processor to which you want to assign the error document, specify a comment, and choose Assign Processor. | The app does the following:Assigns the new processor to the selected error documents.Sends an email to the new processor. The email contains details of the error document that the new processor is responsible for.Records the messages, exceptions, and errors that occurred during the action in an application log. |  |
| 18 | Reject the Assigned Team | Select one or more error documents with the following statuses and choose Reject Team:NewIn ProcessNote This action can only be executed by an LOB user. | The app opens the Reject Team screen. |  |
| 19 |  | Specify a comment and choose Reject. | The app does the following:Removes the current team assignment of selected error documents and automatically assigns the LOC team to these documentsSends emails to all members of the LOC team. The email contains details of the error document that they are responsible for processing.Records the messages, exceptions, and errors that occurred during the action in an application log. |  |
| 20 | Selection of Error Documents for Team Assignment | Select one or more error documents with the following statuses and choose Reassign Team:NewIn ProcessNote This action can only be executed by an LOC user. | The app opens the Reassign Team screen. |  |
| 21 | Reassign a Team | Select the new team that you want to assign to the selected error documents, specify a comment, and choose Reassign. | The app does the following:Removes the current team assignment of selected error documents and assigns the newly selected team to these documentsSends emails to all members of the newly assigned team. The email contains details of the error document that they are responsible for processing.Records the messages, exceptions, and errors that occurred during the action in an application log. |  |
| 22 | Selection of Error Documents for Team Redetermination | Select one or more error documents with the following statuses and choose Redetermine Team:NewIn ProcessNote This action can only be executed by an LOC user. | The app opens the Redetermine Team screen. |  |
| 23 | Redetermine Team | Choose Redetermine Team after selecting the Simulate checkbox. | The app does the following:Redetermines the appropriate team using the rules defined the BRFplus framework, however does not assign the new team to the selected error documentsRecords the messages, exceptions, and errors that occurred during the action in an application log. |  |
| 24 |  | Choose Redetermine Team without selecting the Simulate checkbox. | The app does the following:Redetermines the appropriate team using the rules defined the BRFplus frameworkAutomatically assigns the newly determined team to the selected error documentsSends emails to all members of the newly determined team. The email contains details of the error documents that they are responsible for processing.Records messages, exceptions, and errors that occurred during the action in an application log. |  |
| 25 |  | Choose View Log | The app displays the application log, where you can search for messages, exceptions, and errors that occurred during the team assignment actions. |  |

##### Team Management (Deprecated)

###### Define Functions (Deprecated)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define functions that can be assigned to team members so that they can perform various tasks.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Functions | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Functions. Choose Open Documentation for the found line item to see more details about this configuration activity. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Functions activity is displayed. |  |
| 3 | Define Functions | Choose New Entries, specify the following, and choose Save:Function: <enter a value for the function>Function Description : <enter a description for the function>Note You must define two functions corresponding to the two function classifications delivered for ECS, one for the Ledger Oversight and Control (LOC) team and the other for the Line of Business (LOB) team.You can either create new entries or use the following test data provided by default:Function (LOC User): S_ECSADVNC (Ledger Oversight and Control User)Function (LOB User): S_ECSBASIC (Line of Business User) |  |  |

###### Define Function Profiles (Deprecated)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the function profiles and assigns functions to function profiles. You can group similar functions for a business process in a function profile.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Function Profiles | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Function Profiles. Choose Open Documentation for the found line item to see more details about this configuration activity. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Function Profiles activity is displayed. |  |
| 3 | Define Function Profiles | Choose New Entries , specify the following, and choose Save:Function Profile: <enter a value for the function profile>Function Profile Description : <enter a description for the function profile>You can either create new entries or use the following test data provided by default:Function Profile: S_GLE_ECS (Error Ownership Profile) |  |  |
| 4 | Map Functions to Function Profile | Select the function profile, choose Function Profile to Function Mapping folder, choose New Entries, select the functions that you created for error processing, and choose Save.You can either create new entries or use the following test data provided by default:Function Profile: S_GLE_ECS (Error Ownership Profile)The following functions are assigned by default to the GLE_ECS function profile:S_ECSADVNC (Ledger Oversight and Control User)S_ECSBASIC (Line of Business User) |  |  |

###### Assign Function Profiles to Team Category (Deprecated)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you assign a function profile to a team category.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Assign Function Profiles to Team Category | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Assign Function Profiles to Team Category. Choose Open Documentation for the found line item to see more details about this configuration activity. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Function Profiles to Team Category activity is displayed. |  |
| 3 | Assign Function Profiles to Team Category | Choose New Entries, select the team category GLE_ECS (Error Correction and Suspense Accounting), assign a function profile, and choose Save:Team Category: GLE_ECS (Error Correction and Suspense Accounting)Function Profile: <select the function profile that you newly created for error processing functions, or use the default function profile GLE_ECS (Error Ownership Profile)> |  |  |

###### Classify Functions for Team Category (Deprecated)

Purpose

In this step, you classify functions for team categories.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Classify Functions for Team Category | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Classify Functions for Team Category. Choose Open Documentation for the found line item to see more details about this configuration activity. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Classify Functions for Team Category activity is displayed. |  |
| 3 | Classify Functions for Team Category | Choose New Entries, select the team category GLE_ECS, select the function and choose Save:Team Category: GLE_ECS (Error Correction and Suspense AccountingFunction: <select the function that you newly created for error processing>Function Classification: ECSADVNCD (Ledger Oversight and Control User) or ECSBASIC (Line of Business User) based on the function.Note You must define two entries corresponding to the two functions, one for the Ledger Oversight and Control (LOC) team and the other for the Line of Business (LOB) team.You can either create new entries or use the following test data provided by default:Table 2:Team CategoryFunctionFunction ClassificationGLE_ECSS_ECSADVNC (Ledger Oversight and Control User)ECSADVNCDGLE_ECSS_ECSBASIC (Line of Business User)ECSBASIC |  |  |

###### Define Team Types (Deprecated)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, can create and maintain team types for a standard team category.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Team Types | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Team Types. Choose Open Documentation for the found line item to see more details about this configuration activity. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Team Types activity is displayed. |  |
| 3 | Define Functions | Choose New Entries , specify the following, and choose Save:Team Type: <enter a value for the team type>Team Type Decsription: <enter a description for the team type>Team Category: GLE_ECS (Error Correction and Suspense Accounting)Note You must define two team types, one corresponding to the Ledger Oversight and Control (LOC) team and the other for the Line of Business team (LOB).You can either create new entries or use the following test data provided by default:The following team types are available and assigned by default to the GLE_ECS team category:S_ECS_ADVNCD (Ledger Oversight and Control Team)S_ECS_BASIC (Line of Business Team) |  |  |

###### Manage Teams and Responsibilities (Deprecated)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the ledger oversight and control (LOC) team and line of business (LOB) teams for processing of error documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as Business Process Specialist. |  |  |
| 2 | Access App | Open Manage Teams and Responsibilities (F2412). | The Teams list page is displayed. |  |
| 3 | Create a new LOC team | Choose Create.Note You can also copy teams from the existing team list. |  |  |
| 4 | Maintain General Information for the LOC Team | In the Team Information section, enter the following values:NameGlobal IDTypeDescriptionStatusYou can either create new entries or use the following test data provided by default:Name: <enter a name for the LOC team, for example, Asset Class (Loans) Control team, Asset Class (Cash) Control team, GL IT team>Type: S_ECS_ADVNCD (Ledger Oversight and Control Team)Status: <select Enabled>Note The Category: Error Correction and Suspense Accounting(GLE_ECS) is automatically populated when you select the team type. | New team is created. |  |
| 5 | Maintain Team Owner for the LOC Team | The business process specialist can change or add team owners. If the business process specialist (who is creating the team) has a business user, this business process specialist is then defaulted as team ownerIn the Team Owners section, choose Create. Then either enter the business partner, or select one or more business partners. |  |  |
| 6 | Maintain Team Members for the LOC Team | In the Team Members section, choose Create. Then either enter the business partner, or select one or more business partners.Choose the relevant function value from F4 help for all business partners.Assign the functions to multiple business partners using Manage Functions.Then choose Create on the lower right.You can either create new entries or use the following test data provided by default:Business Partner: <select the user IDs of the members that you want to include in the LOC team>Function: < select S_ECSADVNC (Ledger Oversight and Control User) as the function for each member> | The ledger oversight and control team is created |  |
| 7 | Create the LOB Team | Choose Create Sub Team.In the Team Information section, enter the following values:NameGlobal IDTypeDescriptionStatusYou can either create new entries or use the following test data provided by default:Name: <enter a name for the line of business team, for example, Retail Business team>Type: S_ECS_BASIC (Line of Business Team)Status: <select Enabled>Note The Category: Error Correction and Suspense Accounting(GLE_ECS) is automatically populated when you select the team type. |  |  |
| 8 | Maintain Team Owner for the LOB team | The business process specialist can change or add team owners. If the business process specialist (who is creating the team) has a business user, this business process specialist is then defaulted as team ownerIn the Team Owners section, choose Create. Then either enter the business partner, or select one or more business partners. |  |  |
| 9 | Maintain Team Members of the LOB team | In the Team Members section, choose Create. Then either enter the business partner, or select one or more business partners.Choose the relevant function value from F4 help for all business partners.Assign the functions to multiple business partners using Manage Functions.Then choose Create on the lower right.You can either create new entries or use the following test data provided by default:Business Partner: <select the user IDs of the members that you want to include in the LOB team>Function: <select S_ECSBASIC (Line of Business User as the function for each member> | The team is created |  |
| 10 | Create Additional LOB Teams (If required based on your company structure) | Create more LOB teams (for example, Commercial Business team, Asset Management Business Team) by following the steps from 4 to 7. After saving the information for all subteams, choose Show Hierarchy to view the hierarchy of the teams created.Note Only one level of hierarchy is supported. |  |  |

#### Error Correction - Without Worflow

##### Process Error Documents (Workflow Not Enabled)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can process the soft errors and hard errors that occurred during the file upload.

Procedure

Error Correction - Without Workflow

Table 3: Error Correction - Workflow Not Active

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | If 5NU is activated, then, log on to the SAP Fiori launchpad as a General Ledger Accountant - Banks.If 5NU is not activated, then proceed as follows:Create a business role with the GL Enhancements: Error Correction and Suspense Accounting (SAP_FS_BC_GLE_ECS_PC) business catalog. For more details, see How to Create a New Business Role topic in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html))Create a business user (see How to Maintain Business Users topic in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html))Log on to the SAP Fiori launchpad with the user you created in the previous step |  |  |
| 2 | Access App | Open Process Error Documents - Error Correction and Suspense Accounting (F7320A). |  |  |
| 3 | Start Selection | On the entry screen, specify values for one or more of the following fields and choose Go:Error Document: <Error document number>Severity: <Severity of error, for example, hard error/soft error>Status: <Status of error document, for example, New, In Process, Corrected>Compound Category : <Compound error category, for example, AO>Posted Company Code: Company code associated with the posted document, for example, 1710>Original Posting Date: Company code associated with the original document, for example, 1710>Error in Line Item: Yes/NoCreated On: <Date/date range of error document creation, for example, today or current week>You may need to choose Adapt Filters to show/hide some fields. | You can view a list of all error documents |  |
| 4 | View Error Details | Select an error document (hard error) and navigate to the detailed screen | Hard Error with New StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Corrected Values section contains the same values as that of the Original Values section.The Posted Values section contains no values. |  |
|  |  |  | Hard Error with In Process StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Corrected Values section contains the corrections made to the original values ( (but not posted).The Posted Values section contains no values. |  |
|  |  |  | Hard Error with Corrected StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Corrected Values section contains the the corrections made to the original values before posting.The Posted Values section contains the corrected values from the posted document. |  |
|  |  |  | Hard Error with Reversed StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Corrected Values section contains the the corrections made to the original values before posting.The Posted Values section contains the corrected values from the posted document. |  |
|  |  |  | Hard Error with Deleted StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Corrected Values contains either the original values or corrections made to the original values (but not posted).The Posted Values contains no values (only errors with New /In Process status can be deleted). |  |
|  |  | Select an error document (soft error) and navigate to the detailed screen. | Soft Error with New StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Posted Values section contains values from the autocorrected posted document, for example, suspense postings.The Corrected Values section contains the same values as that of the Posted Values section. |  |
|  |  |  | Soft Error with In Process StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Posted Values section contains values from the autocorrected posted document, for example, suspense postings.The Corrected Values section contains the corrections that you saved (but not posted). |  |
|  |  |  | Soft Error with Corrected StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Posted Values section contains values from the autocorrected posted document, for example, suspense postings.The Corrected Values section contains the manual corrections that you posted. |  |
|  |  |  | Soft Error with Reversed StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Posted Values section contains values from the autocorrected posted document, , for example, suspense postings.The Corrected Values section contains the manual corrections that you posted. |  |
| 13 | Selection of Error Documents for Correction | Select one or more error documents with the following statuses and choose Edit:NewIn Process | The app opens the Edit screen.Note that you cannot edit error documents with the following statuses:ReversedCorrectedDeleted |  |
| 14 | Correct Error Items | On the Edit screen, correct the field values with errors, and choose Confirm. | The app displays the updated values in the Corrected Values section on the detailed page. |  |
| 15 | Post after Error Correction | Select one or more error documents with the following statuses and choose Submit:NewIn Process | The app posts the entries and changes the status of the error documents to Corrected.Note that you cannot edit/post error documents with the following statuses:ReversedCorrectedDeleted |  |
| 16 |  | Choose View Log | The app displays the application log, where you can search for messages, exceptions, and errors. |  |

#### Error Correction - With Worflow

##### Process Error Documents (For Error Document Processors)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can process the soft errors and hard errors that occurred during the file upload.

Procedure

Error Correction - With Workflow

Table 4: Processor Workflow

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | If 5NU is activated, then, log on to the SAP Fiori launchpad as a General Ledger Accountant - Banks.If 5NU is not activated, then proceed as follows:Create a business role with the GL Enhancements: Error Correction and Suspense Accounting (SAP_FS_BC_GLE_ECS_PC) business catalog. For more details, see How to Create a New Business Role topic in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html))Create a business user (see How to Maintain Business Users topic in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html))Log on to the SAP Fiori launchpad with the user you created in the previous step |  |  |
| 2 | Access Process Error Documents App | Open Process Error Documents - Error Correction and Suspense Accounting (F7320A). |  |  |
| 3 | Selection of Error Documents | On the entry screen, specify values for one or more of the following fields and choose Go:Error Document: <Error document number>Severity: <Severity of error, for example, hard error/soft error>Status: <Status of error document, for example, New, In Process, Corrected>Compound Category : <Compound error category, for example, AO>Posted Company Code: Company code associated with the posted document, for example, 1710>Original Posting Date: Company code associated with the original document, for example, 1710>Error in Line Item: Yes/NoCreated On: <Date/date range of error document creation, for example, today or current week>You may need to choose Adapt Filters to show/hide some fields. | You can view a list of all error documents that satisfies the filter criteria.NoteAll operations—such as claiming and forwarding—are available only if the error document is assigned to your processor team. Viewing error document details is the only action available to all users.The My Team column in the results table indicates whether an error document is assigned to your team. To view only those documents, add My Team as a filter and select Yes. |  |
| 4 | View Error Details | Select an error document (hard error) and navigate to the detailed screen | Hard Error with New StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Corrected Values section contains the same values as that of the Original Values section.The Posted Values section contains no values.The Workflow Log section displays detailed record of all activities during the execution of the workflowThe Workflow Recipient section displays details of the current processor and approver of the workflow |  |
|  |  |  | Hard Error with In Process StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Corrected Values section contains the corrections made to the original values ( (but not posted).The Posted Values section contains no values.The Workflow Log section displays detailed record of all activities during the execution of the workflowThe Workflow Recipient section displays details of the current processor and approver of the workflow |  |
|  |  |  | Hard Error with Corrected StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Corrected Values section contains the the corrections made to the original values before posting.The Posted Values section contains the corrected values from the posted document.The Workflow Log section displays detailed record of all activities during the execution of the workflowThe Workflow Recipient section displays details of the current processor and approver of the workflow |  |
|  |  |  | Hard Error with Reversed StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Corrected Values section contains the the corrections made to the original values before posting.The Posted Values section contains the corrected values from the posted document.The Workflow Log section displays detailed record of all activities during the execution of the workflowThe Workflow Recipient section displays details of the current processor and approver of the workflow |  |
|  |  |  | Hard Error with Deleted StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Corrected Values contains either the original values or corrections made to the original values (but not posted).The Posted Values contains no values (only errors with New /In Process status can be deleted).The Workflow Log section displays detailed record of all activities during the execution of the workflowThe Workflow Recipient section displays details of the current processor and approver of the workflow |  |
|  |  | Select an error document (soft error) and navigate to the detailed screen. | Soft Error with New StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Posted Values section contains values from the autocorrected posted document, for example, suspense postings.The Corrected Values section contains the same values as that of the Posted Values section.The Workflow Log section displays detailed record of all activities during the execution of the workflowThe Workflow Recipient section displays details of the current processor and approver of the workflow |  |
|  |  |  | Soft Error with In Process StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Posted Values section contains values from the autocorrected posted document, for example, suspense postings.The Corrected Values section contains the corrections that you saved (but not posted).The Workflow Log section displays detailed record of all activities during the execution of the workflowThe Workflow Recipient section displays details of the current processor and approver of the workflow |  |
|  |  |  | Soft Error with Corrected StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Posted Values section contains values from the autocorrected posted document, for example, suspense postings.The Corrected Values section contains the manual corrections that you posted.The Workflow Log section displays detailed record of all activities during the execution of the workflowThe Workflow Recipient section displays details of the current processor and approver of the workflow |  |
|  |  |  | Soft Error with Reversed StatusThe Error Messages section displays a list of error messages that gives you information about the error.The Original Values section contains actual values from the input file.The Posted Values section contains values from the autocorrected posted document, , for example, suspense postings.The Corrected Values section contains the manual corrections that you posted.The Workflow Log section displays detailed record of all activities during the execution of the workflowThe Workflow Recipient section displays details of the current processor and approver of the workflow |  |
| 13 | Claiming of Error Documents for Correction | Select one or more error documents with the following statuses and choose Claim:NewIn Process | The app disables the Claim option for the selected documents and enables the following options:EditSubmitReleaseForwardNote that you cannot claim error documents with the following statuses:ReversedCorrectedDeleted |  |
| 14 | Select Claimed Error Items for Editing | Select one or more claimed error documents with the following statuses and then choose Edit:NewIn Process | The app displays the Edit screen. |  |
| 15 | Edit Claimed Error Items | On the Editscreen, specify the corrected values for the relevant fields and choose Confirm.Note For New items, the status changes from New to In Process.For In Process items, the status remains the same. | The app displays the updated values in the Corrected Values section on the detailed page. |  |
| 16 | Submit after Error Correction | Select the error documents (one or more) updated/corrected in the previous step and then choose Submit:NewIn Process | The app forwards the submitted documents to the approver's inbox.An approver can log on to the My Inbox app and approve/reject your error correction request. |  |
| 17 | Forwarding of Error Documents | Select one or more claimed error documents and choose ForwardIn the Forward dialog box, enter the name of the recipient and choose Forward. | The app forwards the claimed error documents to another member. Forwarding will remove the current processor assignment and automatically assign the forwarded person as the new processor. |  |
| 18 | Withdrawing of Error Documents | Select one or more claimed error documents and choose Withdraw:NewIn Process | The app lets you withdraw the error documents that you submitted for approval if the approver has not already claimed them in the approver inbox. |  |
| 19 | Releasing of Claimed Error Documents | Select one or more claimed error documents and choose Release | Once the claimed error documents are released, it is available for the other members in the processor team. |  |

##### My Inbox (For Error Document Approvers)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, perform all tasks associated with the error document approver role.

Procedure

Error Correction - With Workflow

Table 5: Approver Workflow

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Logon to SAP Fiori Launchpad as Manager (SAP_BR_MANAGER) | You can view all error correction requests awaiting your approval in the To Dos tile on your SAP Fiori Launchpad.In addition, you can view notifications by clicking the bell icon located in the top-right corner of the SAP Fiori Launchpad screen.Selecting a relevant item from either location takes you to the My Inbox app, where the selected item remains highlighted for your review.You can also directly access the My Inbox app to view approval requests. |  |
| 2 | Access My Inbox App | Open My Inbox (F0862). | If you access the My Inbox app directly from the SAP Fiori Launchpad, you can view a list of all your approval requests in the left panel. Select the relevant request and perform the required action as described in the following steps.If you are navigated to the My Inbox app from SAP Fiori Launchpad notifications or from requests in the To Dos tile, the selected item is automatically highlighted. |  |
| 3 | Claiming of Tasks for Approval | Select one or more approval requests and choose Claim. | Once an approver claims an error document, no other members of the approver team can claim it for approval. Note that a request can be approved/rejected even without claiming. |  |
| 4 | Releasing a Claimed Task | Select one or more approval requests and choose Release | Once an approver releases a claimed error document, the item is available for other members of the approver team to claim. |  |
| 5 | Forwarding an Error Document | Select one or more approval requests that you have claimed and choose Forward. | Once an approver forwards a claimed error document, it will remove his assignment and automatically assign the forwarded person as the new approver. |  |
| 6 | Approving an Error Document | Select one or more approval requests and choose Approve | Once the document is approved, the system automatically posts a correction document, which can be viewed in the Process Error Documents appIf the approver approves the document but posting fails for any reason, the error document is reassigned to the owner who submitted the corrected document for approval. |  |
| 7 | Rejecting an Error Document | Select one or more tasks and choose Reject | If the approver rejects the document, it is reassigned to the owner who submitted the corrected document for approval. While rejecting, the approver should maintain a text specifying the reason for rejection. An owner can view the reason cited by the approver in the Workflow Log section of the Process Error Documents app |  |
| 8 | Show Log | Choose Show Log | You can also view the workflow log and the task log for the selected request. |  |

### Reversing Postings

#### Reverse Posted Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can reverse the journal entries/error documents created by the error correction system.

This includes:

- The error documents created by the error correction system when errors occur in the uploaded file
- The journal entries (autocorrected and manually corrected) created when errors occur in the uploaded file
- The journal entries created when no errors exist in the uploaded data

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | If 5NU is activated, then, log on to the SAP Fiori launchpad as a General Ledger Accountant - Banks.If 5NU is not activated, then proceed as follows:Create a business role with the GL Enhancements: Error Correction and Suspense Accounting (SAP_FS_BC_GLE_ECS_PC) business catalog with dependencies. For more details, see How to Create a New Business Role topic in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html))Create a business user (see How to Maintain Business Users topic in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html))Log on to the SAP Fiori launchpad with the user you created in the previous step |  |  |
| 2 | Access App | Open Reverse Posted Documents - Error Correction and Suspense Accounting (F7329). |  |  |
| 3 | Start Selection for Reversal | On the entry screen, specify values for one or more of the following fields and choose Go:Status: <Status of error document, for example, New/In Process>Error Document: <Error document number>Error Fiscal Year: <Fiscal year of error document, for example, current fiscal year>Journal Entry: <Posted document number>Company Code: <Company code of the posted document, for example, 1710>Fiscal Year: <Fiscal year of the posted document>You may need to choose Adapt Filters to show/hide some fields. | The app displays a list of all error documents that matches your search criteria.Note An error document may have one or more than one journal entry associated with it, for example, a soft error with Corrected status.With this app, you can view and reverse the journal entries created when no errors exist in the uploaded data. For such entries, there will be no associated error document. You can use the No Error status to filter such journal entries. |  |
| 4 | Document Reversal | Select a document and choose Reverse. | The app displays the Reversal Attributes dialog box. |  |
| 5 | Reversal Attributes | In the Reversal Attributes dialog box, specify the following and choose Reverse:Reversal Reason: <Reason for reversalPosting Date: <Reversal posting datePosting Period: <Reversal posting periodSimulation: <Yes or No, the default value is Yes> | Case 1: Simulation = YesThe app simulates the reversal process and displays all messages, exceptions, and errors in a log. However, no data is saved in any database and no reversal documents are generated.To see the messages, exceptions, and errors that occurred during the simulation of reversal run, choose View Log.Case 2: Simulation = NoThe app executes the actual reversal process:Reversal SuccessfulThe app:Reverses the journal entries associated with the selected document and generates corresponding reversal documentsNote In the case of a soft error with Corrected status, the same error document will be displayed twice in the list table, one entry pointing to the journal entry posted through autocorrection and the other entry pointing to the journal entry posted after manually-correcting the errors using the Process Error Documents - Error Correction and Suspense Accounting (F7320) app. If you select the error document entry pointing to the autocorrected document, the journal entry posted after manual correction also gets automatically reversed. However, if you select the error document entry pointing to the manually-corrected document, the app reverses only the selected document and will not reverse the autocorrected document.Changes the status of selected hard error document with New/In Process status to DeletedChanges the status of a selected soft error document with New/In Process status to ReversedChanges the status of selected hard error document with Corrected status to ReversedChanges the status of selected soft error document with Corrected status to Reversed if both the autocorrected and manually corrected journal entries associated with it are reversedChanges the status of selected soft error document with Corrected status to In Process if only the manually corrected journal entry associated with it is reversedError in ReversalThe system displays an error message.To see the messages, exceptions, and errors that occurred during the simulation of reversal run, choose View Log. |  |

#### Reverse Posting Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can reverse the entire set of journal entries/error documents created by the error correction system during an upload run. This includes:

- The error documents created by the error correction system when errors occur in the uploaded file
- The journal entries (autocorrected and manually corrected) created when errors occur in the uploaded file
- The journal entries created when no errors exist in the uploaded data

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Application Support Engineer - Banks |  |  |
| 2 | Access App | Open Reverse Posting Run - Error Correction and Suspense Accounting (F7496) |  |  |
| 3 | Start Selection for Reversal | On the entry screen, specify values for one or more of the following fields and choose Go:Run ID: <Run ID that you want to reverse>Created By: <User who created the run>Created At: <Date/ Date range of run ID creation, for example, Today, Last 7 days, Current week> | The app displays a list of all runs based on your selection criteria. |  |
| 4 | Run ID Selection | Select the run ID that you want to reverse and click on the navigation arrow. | The app displays a list of all error documents and journal entries created during the run, on the right side of the screen.An error document may have one or more than one journal entry associated with it. For example, in the case of a soft error with Corrected status, an error document points to two journal entries, the journal entry posted after autocorrection and the journal entry posted after manually-correcting the entries using the Process Error Documents - Error Correction and Suspense Accounting (F7320) app.This app also displays the journal entries created when no errors exist in the uploaded data. For such entries, there will be no associated error document and the status is No Error.Note You can only reverse one run ID at a time. |  |
| 5 | Reversal | Choose ReverseNote You can choose Reverse directly from the list page or you can click on the navigation arrow, view the run details and then choose the Reverse button on the detailed screen. | The app displays the Reversal Attributes dialog box. |  |
| 6 | Reversal Attributes | In the Reversal Attributes dialog box, specify the following and choose Reverse:Reversal Reason: <Reason for reversal>Posting Date: <Reversal posting date>Posting Period: <Reversal posting period>Simulation: <Yes or No, the default value is Yes> | Case 1: Simulation = YesThe app simulates the reversal process and displays all messages, exceptions, and errors in a log. However, no data is saved in any database and no reversal documents are generated.To see the messages, exceptions, and errors that occurred during the simulation of reversal run, choose View Log.Case 2: Simulation = NoThe app executes the actual reversal process:Reversal SuccessfulThe app:Reverses all journal entries associated with the specified run ID and generates corresponding reversal documentsChanges the status of all hard error documents with New/In Process status to DeletedChanges the status of all soft error documents with New/In Process status to ReversedChanges the status of all hard and soft error documents with Corrected status to ReversedError in ReversalThe system displays an error message.To see the messages, exceptions, and errors that occurred during the simulation of reversal run, choose View Log. |  |

## Configuration Settings

To use Business Rule Framework plus (BRFplus) in SAP S/4HANA Cloud Public Edition and to enable extensibility, ensure that you have assigned the following roles:

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) |
| --- | --- | --- | --- |
| Extensibility Specialist | SAP_BR_EXTENSIBILITY_SPEC | Extensibility / Extensibility | SAP_BR_EXTENSIBILITY_SPEC / SAP_CA_SPT_EXT_PC |

For more information, see the documentation for [Business Rule Framework plus (BRFplus)](https://help.sap.com/docs/SAP_S4HANA_CLOUD/8b78ae42ec1c4b75937806fcd4fd7d1c/9a6b67ce7c26446483af079719edf679.html?version=latest).

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
- see-also :: [[03-financial-accounting-and-close/average-daily-balances-for-banking-649-test-script-1148]]
- see-also :: [[03-financial-accounting-and-close/coa-overview-banking-180]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6SZ_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 117,305 chars in the whole document
