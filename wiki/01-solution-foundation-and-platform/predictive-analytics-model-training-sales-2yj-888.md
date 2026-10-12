---
id: 01-solution-foundation-and-platform/predictive-analytics-model-training-sales-2yj-888
title: Predictive Analytics Model Training – Sales (2YJ) (2YJ_S4CLD2608_BPD_EN_XX)
description: "SAP S/4HANA Cloud 2608 test script 2YJ: train and activate predictive models and test Quotation Conversion Rates, Sales Performance and Predicted Delivery Delay apps."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/predictive-model-training]
aliases: [2YJ_S4CLD2608_BPD_EN_XX]
keywords: [Predictive Analytics Model Training for Sales and Supply…, predictive analytics, intelligent scenario management, model training, model activation, quotation conversion rates, sales performance predictions, predicted delivery delay, business roles, test scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2YJ_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-888
topic: 01-solution-foundation-and-platform/predictive-model-training
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Predictive Analytics Model Training – Sales (2YJ) (2YJ_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2YJ_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Predictive Analytics Model Training for Sales and Supply Chain** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Predictive Analytics Model Training – Sales (2YJ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232838205)

[2 Prerequisites 3](#_Toc232838206)

[2.1 System Access 3](#_Toc232838207)

[2.2 Roles 3](#_Toc232838208)

[2.3 Business Conditions 3](#_Toc232838209)

[3 Overview Table 5](#_Toc232838210)

[4 Test Procedures 6](#_Toc232838211)

[4.1 Intelligent Scenario Management 6](#_Toc232838212)

[4.1.1 Train a Model 6](#_Toc232838213)

[4.1.2 Set a Model Version to Active 7](#_Toc232838214)

[4.2 Quotation Conversion Rates – Predicted 8](#_Toc232838215)

[4.3 Sales Performance – Predictions 9](#_Toc232838216)

[4.4 Predicted Delivery Delay 11](#_Toc232838217)

## Purpose

Overview

With this scope item, you can utilize the embedded predictive analytics functionality in the sales business processes available in SAP S/4HANA Cloud Public Edition.

The scope item provides the following functionalities in different business scenarios:

The Quotation Conversion Rates scenario provides reliable predictions for the sales manager or sales representative to monitor the probability of a sales quotation being converted to a sales order, assisting the sales manager to plan more reliably.

The Sales Performance app allows the sales manager to forecast the achievable sales volumes and develop the sales plans periodically.

With the SAP Fiori app Predicted Delivery Delay, a sales representative can monitor the current delivery performance situation, and instantly recognize the effect of the delivered-as-requested ratio of sales orders, to prevent a critical delay of delivered goods, and thus increase customer satisfaction.

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
| Analytics Specialist | SAP_BR_ANALYTICS_SPECIALIST | Analytics / Analytics | SAP_CA_SPT_ANALYTICS_PC / SAP_CORE_SPT_ANALYTICS_PC |  |
| Sales Manager | SAP_BR_SALES_MANAGER | Sales Management / Internal Sales / Billing for Sales Manager / Customer Returns for Sales Manager | SAP_BR_SALES_MANAGER / SAP_SD_SPT_INT_SALES_SALES_MGR_PC / SAP_SD_SPT_BILLING_SALES_MGR_PC / SAP_SD_SPT_RETURNS_SALES_MGR_PC |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |

### Business Conditions

Follow the procedures described in the scope following items to create corresponding business data if needed.

| Scope item | Business Condition |
| --- | --- |
| BD9 - Sell from Stock | Follow the scope item to create the corresponding business data. |
| BDG - Sales Quotation | Follow the scope item to create the corresponding business data. |
| 1O0 - Planning Apps for Sales | Follow the scope item to create the corresponding business data. |
| J58 - Accounting and Financial Close | Follow test procedure Currency Exchange Rates to maintain exchange rates if needed or issue met. |

## Overview Table

This scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Intelligent Scenario Management](#unique_7) [page ] 6 | Analytics Specialist | Intelligent Scenario Management (F4470) | The model is trained successfully. |
| [Quotation Conversion Rates – Predicted](#unique_8) [page ] 8 | Sales Manager | Quotation Conversion Rates - Valid/Not Completed (F1904) | The app is running correctly. |
| [Sales Performance – Predictions](#unique_9) [page ] 9 | Sales Manager | Sales Performance - Predictions (F3304) | The app is running correctly. |
| [Predicted Delivery Delay](#unique_10) [page ] 11 | Internal Sales Representative | Predicted Delivery Delay - No. of Order Items (F3408) | The app is running correctly. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Intelligent Scenario Management

Purpose

Intelligent Scenario Management (F4470) app allows you to operate on the published intelligent scenario. You can train the model of an intelligent scenario, deploy, and activate for a specific business domain. Also, you can deactivate the deployed versions or undeploy if you no longer need.

Please refer to the documentation on SAP Help Portal to perform the steps and gain more detailed information.

[SAP S/4HANA Cloud Public Edition](https://help.sap.com/s4hanacloud)> English (under Product Assistance) > Manage Your SAP S/4HANA Cloud Public Edition > Process Management > Intelligent Scenario Lifecycle Management > Intelligent Scenario Management .

#### Train a Model

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Your modeling context has been created. You would like to create a model from the existing template based on the intelligent scenario options defined by the application developer. Each application has a specific intelligent scenario. Choose the corresponding intelligent scenario and perform the following test steps for each application.

- Quotation Conversion Rates – Predicted: SLSQTANPREDICTION
- Sales Performance – Predictions: SALESVOLUME001
- Predicted Delivery Delay: PRDTDDELIVCRTNDELAY

|  |
| --- |
| Note When training the predictive model, there are recommendations for different scenario. Please refer to the help document and find more details for each application:[https://help.sap.com/viewer/product/SAP_S4HANA_CLOUD/](https://help.sap.com/viewer/product/SAP_S4HANA_CLOUD/) > English (under Product Assistance) > Sales > Order and Contract Management > Sales Monitoring and Analytics . |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Analytics Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Intelligent Scenario Management (F4470) app. | The app is displayed. |  |
| 3 | Select Intelligent Scenario | Select the Intelligent Scenario (for example, SLSQTANPREDICTION).Note For the Intelligent Scenario selection, refer to the list under Purpose. | The Intelligent Scenario has been selected. |  |
| 4 | Choose Model | Choose the default model and select the radio button. | The Train button is enabled. |  |
| 5 | Train the Model | Choose Train.On the Train Model screen, make the necessary entries and choose Train.To go to the model version list, choose the model. | A new model version with status Training has been added. |  |

#### Set a Model Version to Active

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The active model version is the version that is used to generate predictions when the modeling context is queried.

|  |
| --- |
| Note You can only activate a model version with the status Ready. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Analytics Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Intelligent Scenario Management (F4470) app. | The app is displayed. |  |
| 3 | Select Model Version | Select the corresponding intelligent scenario and model. In the model version list, select the checkbox of the model version. | The model version is selected. |  |
| 4 | Activate | Choose Activate. | The model version status changes to Activating and after some time changes to Active.The procedure is updated with the model version associated with its modeling context. |  |

### Quotation Conversion Rates – Predicted

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can compare the actual and predicted conversion rates only when the predictive model has been successfully trained and set to active.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Quotation Conversion Rates - Valid/Not Completed (F1904) app. | The app is displayed. |  |
| 3 | Display the Association Tile | Choose Show Mini Tiles on the screen. | The association tile is displayed. |  |
| 4 | Access the Prediction Tile | Choose Quotation Conversion Rates – Predicted. | The app is displayed. |  |
| 5 | Select the View | Choose Drill Down icon and select one analysis dimension, for example Sold-To Party. | The data displayed in the graph is changed accordingly. |  |
| 6 | Drill Down to Further Dimension | Choose one Sold-To Party and drill down with another dimension. For example, in the dialog box, choose List of quotations. | The data displayed in the graph is changed accordingly. |  |
| 7 | Navigate to Jump To Target App | In the List of Quotations view, select one quotation and choose Jump To. Select one of the options for further action, for example Sales Quotation. | The target app is displayed and further action can be taken. |  |

### Sales Performance – Predictions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can compare the actual, predicted, and planned sales value only when a sales plan has been released, the predictive model has been successfully trained and set to Active.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Set User Default Values | Choose the user icon and select Settings. On the Settings screen, choose Default Values. Maintain values for your user. For example, Exchange Rate Type, Display Currency. Save your changes. | The user default values have been set. |  |
| 3 | Access the App | Open the Sales Performance - Predictions (F3304) app. | The app is displayed. |  |
| 4 | Display Planned Value | Choose Compact Filter, and then select a sales plan (which is planned for sales volume) in the system.Note For more information about sales plan management, please refer to the Planning Apps for Sales (1O0) scope item. | The planned value is displayed for comparison. |  |
| 5 | Display Value of Previous Year | Choose Settings icon in the chart, on View Settings screen, tab Chart, select the checkbox before Value of Pre. Year and choose OK. | Actual value of previous year is displayed for comparison. |  |
| 6 | Apply Filter | Set the filter in Compact Filter and switch to Visual Filter. | The filters have been set and app has been refreshed accordingly. Compact Filter and Visual Filter are consistent and reflect each other. |  |
| 7 | Drill Down | Choose View By in the chart to select more dimensions for analysis. For example, choose Sales Organization. | The chart has been refreshed accordingly. |  |
| 8 | Navigation | Choose Actions in the chart and choose the smart link for navigating to the target apps for further analysis. For example, choose Show Quotation Conversion Rates. | The target apps are displayed for further analysis. |  |
| 9 | View Management | Navigate back to the Sales Performance - Predictions (F3304) app, apply some filters, and choose the Select View icon. On the My Views screen, choose Save As. On the Save View screen, enter the view name and select the necessary checkbox, for example, Set as Default, and then choose Save. Alternatively, you can manage the view by choosing Manage on the My Views screen. | The views can be managed for the app. |  |

### Predicted Delivery Delay

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An internal sales representative is enabled to monitor the predicted delay of the planned delivery to the customer in the context of the sales order fulfillment. An internal sales representative is also enabled to recognize issues and trigger the appropriate actions instantly. The ranges from in-time supply of procurement processes to the creation of outbound deliveries as follow-ups to sales orders, across transportation planning, picking, packing, and shipping in the delivery process to transportation processes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Predicted Delivery Delay - No. of Order Items (F3408). |  |  |
| 3 | Apply Filter | Apply some filter criteria and check if the chart and list are filtered accordingly.Additional fields can be added or removed via Adapt Filters. | The filter is applied to the app. |  |
| 4 | Toggle Filter | Choose Compact Filter or Visual Filter at the top right of the screen for toggling the filter mode. | The filter mode is changed. |  |
| 5 | Verify Chart | Selecting items or legend in the chart should update the data displayed in the table.Choose View By in the chart. Select one dimension to drill down to a more detailed data level. | The chart is working properly. |  |
| 6 | Verify Table | Choose Settings in the table. The output configuration can be changed in the View Settings. For example, uncheck Sales Document Item in the Columns tab and choose OK. A higher aggregated level result set is shown,Select one of the smart links in the table to get more detailed information and navigate to the smart links available. | The table is working properly. |  |
| 7 | Toggle to Different View on Content Part | Choose Chart and Table View, Chart View, and Table View at the top right of the page. | Check whether the table view and chart view are displayed. |  |
| 8 | View Management | Apply some filters in the filter bar and choose the Select View icon. On the My Views screen, choose Save As. On the Save View screen, enter the view name and select the necessary checkbox. Then choose Save. You can also manage the view by choosing Manage on the My Views screen. | The views can be managed for the app. |  |
| 9 | Share the App | Choose the Share icon at the right top of the screen for sharing the app for quick and easy accessibility. The following options are possible:Send emailSave as Tile | Tile sharing with an email or as a tile on the SAP Fiori launchpad is possible. |  |

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
- related-to :: [[01-solution-foundation-and-platform/predictive-analytics-model-training-supply-chain-20n-test-script-795]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2YJ_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 20,686 chars in the whole document
