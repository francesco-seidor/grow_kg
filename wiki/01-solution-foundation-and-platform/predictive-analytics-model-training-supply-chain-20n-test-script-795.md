---
id: 01-solution-foundation-and-platform/predictive-analytics-model-training-supply-chain-20n-test-script-795
title: Predictive Analytics Model Training – Supply Chain (20N) Test Script (20N_S4CLD2608_BPD_EN_XX)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 20N: train and activate predictive models and check overdue stock in transit and demand-driven replenishment."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/predictive-model-training]
aliases: [20N_S4CLD2608_BPD_EN_XX]
keywords: [Predictive Analytics Model Training for Sales and Supply…, predictive analytics, intelligent scenario management, model training, model version activation, overdue stock in transit, demand-driven replenishment, defect code proposal, business roles, test scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/20N_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-795
topic: 01-solution-foundation-and-platform/predictive-model-training
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Predictive Analytics Model Training – Supply Chain (20N) Test Script (20N_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/20N_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Predictive Analytics Model Training for Sales and Supply Chain** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Predictive Analytics Model Training – Supply Chain (20N) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232848408)

[2 Prerequisites 3](#_Toc232848409)

[2.1 System Access 3](#_Toc232848410)

[2.2 Roles 3](#_Toc232848411)

[2.3 Business Conditions 4](#_Toc232848412)

[3 Overview Table 5](#_Toc232848413)

[4 Test Procedures 6](#_Toc232848414)

[4.1 Intelligent Scenario Management 6](#_Toc232848415)

[4.1.1 Train Model 6](#_Toc232848416)

[4.1.2 Set a Model Version to Active 7](#_Toc232848417)

[4.2 Overdue - Stock in Transit 8](#_Toc232848418)

[4.3 Demand-Driven Replenishment 9](#_Toc232848419)

## Purpose

Overview

This scope item allows customers to use the embedded predictive analytics functionality in various supply chain scenarios, including production, manufacturing, inventory management, and logistics execution. It enables users to select parameters for training and activating predictive models. Currently, the following use case leverages embedded predictive modeling:

- Tracking materials in transit or open stock transport orders that have exceeded the estimated time in transit but haven't had a goods receipt posted by the receiving plant

The document is aimed to provide description on how to use the prediction scenarios in supply chain area. There are three user cases covered in the scope item, overdue - stock in transit, demand-driven replenishment, and defect code proposal.

Overdue - stock in transit consists of analyzing whether a purchase order is delayed according to the scheduled delivery date. Based on historical data, the system tries to predict whether the stock in transit order will be delayed.

Demand-driven replenishment provides an additional way to calculate the lead time in the production area with the help of machine learning models.

Defect code proposal makes defect code proposal based on the title of the defect and historical defect recordings.

With this scope item, the first step is to train the predictive model by the analytics specialist. Then other professional roles could improve their efficiency and productivity with the help of these machine learning models.

This document provides a detailed procedure for testing the scope item after solution deployment, reflecting the predefined scope of the solution. Each process step is covered in its own section, providing the system interactions (that is, test steps) in a list view.

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

If you want to train the model, the Analytics Specialist role must have been assigned to your user to be able to work with predictive models. If you want to check the business results, the Inventory Manager role must have been assigned to your user to run the Overdue Materials - Stock in Transit application or Production Planner in the demand-driven replenishment case.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Analytics Specialist | SAP_BR_ANALYTICS_SPECIALIST | Analytics / Analytics | SAP_CA_SPT_ANALYTICS_PC / SAP_CORE_SPT_ANALYTICS_PC | Please ask your system administrator to assign to the testers. |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER | Please ask your system administrator to assign to the testers. |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR | Please ask your system administrator to assign to the testers. |
| Quality Technician | SAP_BR_QUALITY_TECHNICIAN | Quality Inspection | SAP_BR_QUALITY_TECHNICIAN | Please ask your system administrator to assign to the testers. |

### Business Conditions

Follow the procedures described in the following scope items for creating the corresponding business data if needed.

| Scope Item | Business Condition |
| --- | --- |
| BMH - Stock Transfer Without Delivery | Follow the scope item to create the corresponding business data. |
| BME - Stock Transfer with Delivery | Follow the scope item to create the corresponding business data. |
| 1P9 - Intercompany Stock Transfer | Follow the scope item to create the corresponding business data. |
| 1Y2 - Demand-Driven Buffer Level Management | Follow the scope item to create the corresponding business data. |

## Overview Table

This scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Intelligent Scenario Management](#unique_7) [page ] 6 | Analytics Specialist | Intelligent Scenario Management (F4470) | The model is trained successfully. |
| [Overdue - Stock in Transit](#unique_8) [page ] 8 | Inventory Manager | Overdue Materials - Stock in Transit (F2139) | After having trained the model, the inventory manager can monitor the overdue stock in transit |
| [Demand-Driven Replenishment](#unique_9) [page ] 9 | Production Planner | Mass Maintenance of Products (DD) (F2825) | After having trained the model, Production Planner can apply the lead time calculation change |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Intelligent Scenario Management

Purpose

SAP S/4HANA Cloud Public Edition is shipped with preconfigured intelligent scenarios. Depending on your use case, you can choose a intelligent scenario to train your models based on your system data.

Intelligent Scenario Management (F4470) app allows you to operate on the published intelligent scenario. You can train the model of an intelligent scenario, deploy, and activate for a specific business domain. Also, you can deactivate the deployed versions or undeploy if you no longer need.

Please refer to the documentation on SAP Help Portal to perform the steps and gain more detailed information.

[SAP S/4HANA Cloud Public Edition](https://help.sap.com/s4hanacloud)> English (under Product Assistance) > Manage Your SAP S/4HANA Cloud Public Edition > Process Management > Intelligent Scenario Lifecycle Management > Intelligent Scenario Management .

#### Train Model

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

Your modeling context has been created. You would like to create a model from the existing template based on the predictive scenario options defined by the application developer. Choose the corresponding predictive scenario and perform the following test steps for each application.

Overdue - Stock in Transit - MATERIAL_OVERDUE_SIT

Demand-Driven Replenishment - INDIV_LEADTIME_STO2

Defect Code Proposal - QM_DEF_CODE_PRPSL

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Analytics Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Intelligent Scenario Management (F4470) app. | The app is displayed. |  |
| 3 | Select Intelligent Scenarios | Under Intelligent Scenario, choose MATERIAL_OVERDUE_SIT. | The Intelligent Scenario screen is displayed. |  |
| 4 | Choose Model | Under Models, select DEFAULT. | The Train button is enabled. |  |
| 5 | Train the Model | Choose Train. | The model version is added to the model list with the status Training. |  |

#### Set a Model Version to Active

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

The active model version is the version that is used to generate predictions when the modeling context is queried.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Analytics Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Intelligent Scenario Management (F4470) app. | The app is displayed. |  |
| 3 | Select Version | Select the relevant model version from the models list. | The model version is selected. |  |
| 4 | Activate | Choose Activate. | The model version status changes to Active.The procedure is updated with this model version associated with its modeling context. |  |

### Overdue - Stock in Transit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

You can check the predicted differences between the planned and the predicted delivery date in the Overdue Materials - Stock in Transit app. With the following steps, you can check the results of the prediction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Overdue Materials - Stock in Transit (F2139) app. | The Overdue Materials - Stock in Transit app screen is displayed. |  |
| 3 | Get the List View for all Available Line Items | Choose Go to get a list view of the line items. You can use filters here as well. | A list view of the line items is displayed. |  |
| 4 | Add Predicted Deviation (if it is not available in the line items view) | On the right side of the screen, in the Line Items list view, there is a setting to choose which fields should be displayed. Select Predicted Deviation. | The Predicted deviation field is displayed in the Line Items list view. You can check the value of the field for each stock. |  |

### Demand-Driven Replenishment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

You can check the lead time calculated based on prediction. For details, refer to Demand-Driven Buffer Level Management (1Y2) scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Calculate Lead Time by Machine Learning Training Model | To see how to apply the training result to a lead time calculation, refer to the test procedures in the Demand-Driven Buffer Level Management (1Y2) scope item. | The lead time is calculated with the training model result. |  |

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
- related-to :: [[01-solution-foundation-and-platform/predictive-analytics-model-training-sales-2yj-888]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/20N_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 14,825 chars in the whole document
