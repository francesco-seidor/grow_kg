---
id: 03-financial-accounting-and-close/test-script-machine-learning-for-monitoring-of-goods-and-invoice-recei
title: "Test Script: Machine Learning for Monitoring of Goods and Invoice Receipts (2ZS_AE) (2ZS_S4CLD2608_BPD_EN_AE)"
description: "Test script for scope item 2ZS: training, deploying and activating the GR/IR prediction ML model (FI_GRIR_RECONCILE) and scheduling the DAR status prediction job."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/gr-ir-monitoring]
aliases: [2ZS_S4CLD2608_BPD_EN_AE]
keywords: [GR/IR Account Monitoring and Reconciliation, gr/ir prediction, intelligent scenarios, model training, model deployment, deployment activation, dar prediction job, goods and invoice receipts, business roles, test scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2ZS_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-890
topic: 03-financial-accounting-and-close/gr-ir-monitoring
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Machine Learning for Monitoring of Goods and Invoice Receipts (2ZS_AE) (2ZS_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2ZS_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **GR/IR Account Monitoring and Reconciliation** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Machine Learning for Monitoring of Goods and Invoice Receipts (2ZS_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232851202)

[2 Prerequisites 3](#_Toc232851203)

[2.1 System Access 3](#_Toc232851204)

[2.2 Roles 3](#_Toc232851205)

[2.3 Business Conditions 3](#_Toc232851206)

[2.4 Preliminary Steps 4](#_Toc232851207)

[2.4.1 Additional Manual Configuration 4](#_Toc232851208)

[3 Overview Table 5](#_Toc232851209)

[4 Test Procedures 6](#_Toc232851210)

[4.1 Train GR/IR Prediction Model 6](#_Toc232851211)

[4.1.1 Train Model 6](#_Toc232851212)

[4.1.2 Deploy Training 7](#_Toc232851213)

[4.1.3 Activate Deployment 8](#_Toc232851214)

[4.2 Prepare GR/IR Status Predictions - DAR Model 9](#_Toc232851215)

## Purpose

Overview

A machine learning feature of the GR/IR application makes a prediction of the next status based on the history of processing goods and invoices received. The predictions are provided by a Machine Learning (ML) service that runs on the SAP Cloud. This communication scenario is related to the connection of the SAP S/4HANA Cloud Public Edition and the ML service. This scope item is deployed in conjunction with the Goods Receipt / Invoice Receipt monitor.

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
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Analytics Specialist | SAP_BR_ANALYTICS_SPECIALIST | Analytics / Analytics | SAP_CA_SPT_ANALYTICS_PC / SAP_CORE_SPT_ANALYTICS_PC |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 2V7 - Monitoring of Goods and Invoice Receipts | Must be in scope as prerequisite |

### Preliminary Steps

#### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/b9007316190afaaf7375d58f58eefc2d)

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Train Model](#unique_8) [page ] 6 | Analytics Specialist | Intelligent Scenario Management (F4470) | You train the model for the intelligent scenario. |
| [Deploy Training](#unique_9) [page ] 7 | Analytics Specialist | Intelligent Scenario Management (F4470) | You deploy the training. |
| [Activate Deployment](#unique_10) [page ] 8 | Analytics Specialist | Intelligent Scenario Management (F4470) | You activate the deployment of the model. |
| [Prepare GR/IR Status Predictions - DAR Model](#unique_11) [page ] 9 | General Ledger Accountant | Schedule General Ledger Jobs (F1927) | You set up a background process to receive proposals from the prediction model. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

|  |
| --- |
| Note Before using the machine learning feature, you must have sufficient training data. Ensure you have modified at least 100 GR/IR reconciliation items before training the model.You can refer to Reconcile GR/IR Accounts in the test script of prerequisite scope item Monitoring of Goods and Invoice Receipts (2V7) for details on how to process an item. |

### Train GR/IR Prediction Model

#### Train Model

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you train the model for intelligent scenairo FI_GRIR_RECONCILE.

|  |
| --- |
| Note For more information about intelligent scenarios, see [Intelligent Scenario Lifecycle Management](https://help.sap.com/docs/SAP_S4HANA_CLOUD/6aa39f1ac05441e5a23f484f31e477e7/3fa32d7a1e21465f8d9696f6b8cb6ee9.html?version=latest). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Analytics Specialist. |  |  |
| 2 | Access App | Open Intelligent Scenario Management (F4470). | The Intelligent Scenarios Management screen displays. |  |
| 3 | Choose Intelligent Scenario | Under Intelligent Scenarios, choose > for intelligent scenario FI_GRIR_RECONCILE to navigate to the intelligents scenario's details. | The details of the intelligent scenario are displayed. |  |
| 4 | Train Model | Under Models, select FI_GRIR_RECONCILE.Choose Train. | The Train window displays. |  |
| 5 | Train Model | Make the following entries:Version: <version>Package Size: for example, 1000To apply a filter to the training data, choose Add Filter in the Training Filters section and make the following entries:Name: for example, COMPANYCODEOption: for example, Equal toLow: for example, 3310In the Training Details section, make the following entries:Training Description: <description>Targets:GRIRCLEARINGPROCESSSTATUSGRIRCLEARINGPROCESSPRIORITYGRIRCLEARINGPROCESSROOTCAUSERESPONSIBLEDEPARTMENTRESPONSIBLEPERSONChoose Train. | A training is started and added to the training list. |  |

#### Deploy Training

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you deploy the model for intelligent scenario FI_GRIR_RECONCILE.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Analytics Specialist. |  |  |
| 2 | Access App | Open Intelligent Scenario Management (F4470). | The Intelligent Scenarios Management screen displays. |  |
| 3 | Choose Intelligent Scenario | Under Intelligent Scenarios, choose > for intelligent scenario FI_GRIR_RECONCILE to navigate to the intelligents scenario's details. | The details of the intelligent scenario are displayed. |  |
| 4 | Display Trainings | Under Models, select FI_GRIR_RECONCILE.Choose > to navigate to the model's trainings and deployments. |  |  |
| 5 | Deploy Training | Under Trainings, select the training that you want to deploy.Note Ensure that the selected training is in the completed status.Choose Deploy.Make the following entries and choose Deploy:Deployment Description: <description> | The model is deployed. |  |

#### Activate Deployment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you activate the model for intelligent scenario FI_GRIR_RECONCILE.

|  |
| --- |
| Note Make sure that the deployment is in the deployed status. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Analytics Specialist. |  |  |
| 2 | Access App | Open Intelligent Scenario Management (F4470). | The Intelligent Scenarios Management screen displays. |  |
| 3 | Choose Intelligent Scenario | Under Intelligent Scenarios, choose > for intelligent scenario FI_GRIR_RECONCILE to navigate to the intelligents scenario's details. | The details of the intelligent scenario are displayed. |  |
| 4 | View Deployment | Under Models, select FI_GRIR_RECONCILE.Choose > to navigate to the model's trainings and deployments. |  |  |
| 5 | Activate Deployment | Under Deployments, select the deployment that you want to activate.Choose Activate > For All or Activate > For MeNote You can view the active deployment only in the relevant deployment list. Also, in the Active column, you can check whether the deployment is active for all users, your user, or other users. | The deployment is activated. |  |

### Prepare GR/IR Status Predictions - DAR Model

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you set up a background process to receive goods receipts and invoice receipt processing proposals from the prediction model.

Prerequisite

The Train GR/IR DAR Prediction Model on Historical Data job must be finished before this job can be run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Schedule General Ledger Jobs (F1927). | The Application Jobs screen displays. |  |
| 3 | Create a Job | Choose Create. | The New Job screen displays. |  |
| 4 | Enter Job Data | Make the following entries:Template Selection section:Job Template: Prepare GR/IR Status Predictions (DAR ML model)Name: Prepare GR/IR Status Predictions (DAR ML model)Choose Step 2.Scheduling Options section:Choose Define Recurrence Pattern.Make the following entries:Recurrence Pattern: Single RunStart Immediately: SelectedChoose OK.Choose Step 3. | The Scheduling Information dialog box displays. |  |
| 5 | Schedule Job | Choose Schedule. |  |  |
| 6 | Check Logs | Monitor the job status for the Prepare GR/IR Status Predictions (DAR ML model) job. When the job is processed, the status displays as Finished.When the job status shows Finished, choose the Log icon and review the log details. |  |  |

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
- related-to :: [[03-financial-accounting-and-close/test-script-monitoring-of-goods-and-invoice-receipts-2v7-ae-876]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2ZS_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 15,300 chars in the whole document
