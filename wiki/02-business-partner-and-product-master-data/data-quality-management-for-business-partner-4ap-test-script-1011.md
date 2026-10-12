---
id: 02-business-partner-and-product-master-data/data-quality-management-for-business-partner-4ap-test-script-1011
title: Data Quality Management for Business Partner (4AP) Test Script (4AP_S4CLD2608_BPD_EN_XX)
description: "Test script for scope item 4AP in SAP S/4HANA Cloud Public Edition: rule mining, validation rules, data quality scores and evaluation for business partner master data."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/data-quality-management]
aliases: [4AP_S4CLD2608_BPD_EN_XX]
keywords: [Data Quality Management for Products and Business Partners, business partner data quality, rule mining, validation rules, data quality scores, data quality evaluation, data quality overview, business catalogs, business roles, demo data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4AP_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1011
topic: 02-business-partner-and-product-master-data/data-quality-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Data Quality Management for Business Partner (4AP) Test Script (4AP_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4AP_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Data Quality Management for Products and Business Partners** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Data Quality Management for Business Partner (4AP) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232839180)

[2 Prerequisites 3](#_Toc232839181)

[2.1 System Access 3](#_Toc232839182)

[2.2 Roles 3](#_Toc232839183)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232839184)

[3 Overview Table 5](#_Toc232839185)

[4 Test Procedures 6](#_Toc232839186)

[4.1 Discover Validation Rules by Using Rule Mining 6](#_Toc232839187)

[4.1.1 Create Rule Mining for Business Partners 6](#_Toc232839188)

[4.1.2 Process Rules from Rule Mining Run 7](#_Toc232839189)

[4.2 Master Data Quality Management 8](#_Toc232839190)

[4.2.1 Create Validation Rule 8](#_Toc232839191)

[4.2.2 Configure Data Quality Scores 10](#_Toc232839192)

[4.2.3 Evaluate Data Quality for Business Partners 12](#_Toc232839193)

[4.2.4 Data Quality Evaluation Overview 12](#_Toc232839194)

## Purpose

Overview

This scope item enables you to define data quality rules and KPIs for business partner master data. You can evaluate the quality of business partner data according to these rules and monitor the current state of the data quality as well as its trend.

To define rules, you can use machine learning capabilities and detect patterns with rule mining. These patterns can be transferred to data quality rules.

By analyzing the evaluation results, you can identify areas of data with errors and potential reasons for errors and initiate the corrections. You can also use the data quality rules to validate data in Master Data Consolidation for Business Partner (‏1N3‏) and Central Governance for Business Partner (‏1N7‏).

You can assign several business catalogs to a business role for various functional needs. For more information on the business catalog details, see the test script.

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
| Master Data Steward - Business Partner Data | SAP_BR_BUPA_MASTER_STEWARD | Business Partner Governance / Business Partner Governance | SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_GOV_PC |  |

Below are the Business catalogs which can be assigned to a Business role to perform various functional needs.

Administration (SAP_CMD_BC_QLTY_BP_ADM_PC) : Performs,schedules,monitors data quality evaluations.

Analytics (SAP_CMD_BC_QLTY_BP_ANA_PC) : Analyzes data quality evaluations.

Rule Display (SAP_CMD_BC_QLTY_BP_RL_DSP_PC) : Display data quality rules.

Implement Rules (SAP_CMD_BC_QLTY_BP_RL_IMP_PC) : Implements data quality rules.

Manage Rules (SAP_CMD_BC_QLTY_BP_RL_MNG_PC) : Manages data quality rules and their use in processes.

Manage Rule Mining (SAP_CMD_BC_QLTY_BP_MINING_PC) : Execute mining run to get system proposed rules.

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

## Overview Table

This scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Choose the appropriate entity: Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Rule Mining for Business Partners](#unique_7) [page ] 6 | Master Data Steward - Business Partner Data | SAP Fiori: Manage Rule Mining - Business Partners (F4084) | With this app, you can create and start a rule mining run to discover business rules for your master data records. In a mining run, you can define the focus for a mining run and specify the fields that could be potential condition fields and checked fields for your new rules. When you start the mining run, the system uses a machine-learning algorithm to propose a list of potential rules based on your input. This app assists the master data steward in uncovering potential rules for their master data and so shortens the preparation time of rule definition. |
| [Process Rules from Rule Mining Run](#unique_8) [page ] 7 | Master Data Steward - Business Partner Data | SAP Fiori: Process Rules from Rule Mining - Business Partners (F4070) | With this app, you can review and manage rules generated from rule-mining runs for Business Partners. You can decide to accept the rules or set them for review by others from this app. You can either create a new validation rule directly from the accepted mined rules or link the mined rules to existing validation rules. |
| [Create Validation Rule](#unique_9) [page ] 8 | Master Data Steward - Business Partner Data | SAP Fiori: Validation Rules - Business Partners (F4082A) | This app enables you to describe, catalog, implement, and simulate validation rules using a central rule repository. These validation rules can be used for data quality evaluation for Business Partners and to validate products in mass processing and consolidation. |
| [Configure Data Quality Scores](#unique_10) [page ] 10 | Master Data Steward - Business Partner Data | SAP Fiori: Configure Data Quality Scores - Business Partners (F4091A) | With this app, you can configure how a data quality score is calculated, based on the evaluation of Business Partner data in combination with validation rules. You can create data quality dimensions, categories of data quality dimensions, and assign rules to these data quality dimensions. This results in a hierarchy with data quality categories at the top, data quality dimensions at the next level, and assigned rules at the lower level. The system calculates scores for dimensions and categories based on this information. |
| [Evaluate Data Quality for Business Partners](#unique_11) [page ] 12 | Master Data Steward - Business Partner Data | SAP Fiori: Evaluate Data Quality - Business Partners (F6450A) | With this app, you can create, execute, and schedule data quality evaluations runs. You can also delete entire existing runs or choose to delete the results of evaluations and keep their aggregated data to use in score calculation. |
| [Data Quality Evaluation Overview](#unique_12) [page ] 12 | Master Data Steward - Business Partner Data | SAP Fiori: Data Quality Evaluation Overview - Business Partners (F3900)home page | This app provides dashboards showing a high-level overview of your data quality and data quality trends across an entire business object. This data is always based on the default category Global. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Discover Validation Rules by Using Rule Mining

#### Create Rule Mining for Business Partners

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
| 1 | Log On | Log on to the SAP Fiori launchpad with user and password | The SAP Fiori launchpad displays |  |
| 2 | Access App | Open App Manage Rule Mining - Business Partners (F4084) under group Data Quality Management for Business Partners | The Manage Rule Mining Business Partners screen displays |  |
| 3 | Create a new Mining Run | Choose Create to create a new Mining Run. Enter the following data:Description:Goal:In the section of Tables, choose Add, choose the table from the popup window. For example, BUT000. Then choose Select and a new sub screen General will be displayed on the right.In the Focus Area section under General:Choose Add, in the popup window select the field you need, for example Business Partner Category (TYPE).Set the value to the field that you choose: for example, set the field Business Partner Category (TYPE) with a value of 2 (Organization).In the Fields section under General:Choose Add in the popup window select the field you need and choose Select. For example, select the fields: Business Partner Type (BPKIND), Business Partner Grouping (BU_GROUP), and Form-of-Address Key(TITLE).In the result list of selected fields, keep the checkbox of Condition of Rule for each field be selected and set at least one checkbox of Checked by Rules be selected.Choose Apply, then choose Create.Note As Business Partner data are not the same in the different systems, You may get different result of rule mining run in different system, even based on the same fields. You can adjust the fields for the different testing purpose. | A new rule mining run has been created |  |

#### Process Rules from Rule Mining Run

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
| 1 | Start Rule Mining Run | Open the app Manage Rule Mining - Business Partners (F4084), select the rule mining run you created in part Create Rule Mining for Business Partner, choose Start.In the popup window, choose OK to confirm the start action. | A mining run starts and the status is Running. |  |
| 2 | Complete the Rule Mining Run | Choose Refresh until the status changed to Completed. | The status of rule mining run is Completed. |  |
| 3 | Process Rules from Rule Mining Run | Choose the number of Total Rules and you are navigated to the app Process Rules from Rule Mining - Business Partners (F4070). Select one rule from the list and choose Accept | The rule status is changed from Initial to Accepted. |  |
| 4 | Link Mining Rule to Validation Rule | Select the accepted rule and choose Link to Validation Rule. In the dropdown list, choose Link to New Rule.In the popup window, enter the ID and description of your new validation rule.ID:Description:Choose Save. | In the column Linked Validation Rule, a new Validation Rule has been linked. |  |
| 5 | Review the Validation Rule | Choose the Rule ID under the column Linked Validation Rule. In the popup window, choose Validation Rules for Products. You are navigated to the Validation Rules - Business Partners (F4082A) app, and the rule which you created in the step 4 is displayed. | In the section Rules from Rule Mining, one mining rule which you selected in step 3 has been linked. |  |
| 6 | Rule Mining Implementation | Choose Send for Implementation.Choose Edit. Then, in the Usage section, choose Create. Select Data Quality Evaluation from the dropdown list. Choose Not ready as the usage status.In Usage Action, choose Prepare. In the popup dialog, choose Prepare Usage.After the generation has concluded, the BRF+ expressions have been prepared. | In the section Rule Mining Implementation, the Decision Tables for Scope and Condition have been created and status are Active. |  |

### Master Data Quality Management

#### Create Validation Rule

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
| 1 | Log On | Log on to the SAP Fiori launchpad with user and password. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Validation Rules - Business Partners (F4082A) app. | The Validation Rules for Business Partners screen is displayed. |  |
| 3 | Create new rule | Choose Create to create a new rule. Enter the following data:Rule ID:Rule name:Base Table: Select the table that you want to check with this rule, for example, Customer General (KNA1).Checked Field: Enter the field that you want to check with this rule, for example, KNA1-SPRAS.Choose Create. | The system creates a new rule. The status of the rule is New. |  |
| 4 | Change Status for Implementation | Choose Send for Implementation. | The rule status has changed to To Be Implemented. |  |
| 5 | Prepare Usage | Choose Edit, then in the Usage section, choose Create, select Data Quality Evaluation from the drop-down list. Choose Not ready as the usage status.In Usage Action, choose Prepare. In the popup dialog, choose Prepare Usage. | The Usage status has changed to Disabled, and the Usage Action is Enable. |  |
| 6 | Implemented BRF+ Rule | In the Implementation section, choose the link under Scope Expression. The system opens the BRFplus Workbench. Choose Edit to maintain the expression.The same step for the link under Condition Expression.Here is an example:Scope: Country/Region is equal to DE; Condition: Language SPRAS is equal to DE.Scope:Choose Edit Operand -> Use Direct Value Range From -> Context -> More-> Country/RegionIs equal toDEChoose Save -> Choose ActivateCondition:Choose Edit Operand -> Use Direct Value Range From -> Context -> More->SPRASIs equal toDEChoose Save -> Choose Activate. | The status under Scope and Condition has changed to Active. |  |
| 7 | Simulate Validation Rule | In the Simulations section, select Create.On the popup screen, enter a description in the Description field, then choose Save.The Simulate Validation Rule process is created. Define select types and field values to determine the range of records to be simulated.Choose Start, and wait until the process is Stopped for Review.Choose the back arrow button of the process and navigate back to the rule repository. | The created Simulation with process ID is displayed in the Simulations section. The status and other fields contain the simulation result. |  |
| 8 | Change Status to Send for testing | Choose Send for Testing for this rule. | The rule status has changed to To Be Tested. |  |
| 9 | Change Status to Approve | Choose the rule created in step 3. Choose Approve. | The rule status has changed to Approved. |  |
| 10 | Enable the Usage | Choose the rule created in step 3.In the Usage section, choose Enable for usage Data Quality Evaluation. | The Usage status has changed to Enabled, and the Usage Action is Disable. |  |

#### Configure Data Quality Scores

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
| 1 | Create new category | Start the launchpad and open the app Configure Data Quality Scores - Business Partners (F4091A).Choose Create to create a new dimension category.In the Header section, enter the following information:Category name:TargetWarningCriticalFor Example:Target : 99Warning : 90Critical : 80 | A new Category has been created. |  |
| 2 | Create new Dimension | In the Dimension section, choose Add Dimension to create a new dimension:Dimension name:TargetWarningCriticalFor Example:Target : 95Warning : 88Critical : 80Choose Create. | A new Dimension has been created. |  |
| 3 | Assign the newly created rule to your new dimension | Choose Edit in the Category screen. Choose the dimension that you created. The system goes to the screen for Rule assignment.Choose Add.Type the rule you have created before, choose Select.Enter an impact value from the dropdown menuChoose Apply.Choose Save. | The rule assignment is saved. |  |

#### Evaluate Data Quality for Business Partners

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
| 1 | Create Process for Evaluation Run | Start launchpad and open the app Evaluate Data Quality - Business Partners (F6450A).Choose Create Process:Description:Process template: SAP: Data Quality Evaluation for BP.choose Save. | New process has been created. |  |
| 2 | Start Evaluation Process | Choose Start to run the evaluation process manually | The evaluation process is started and the progress bar eventually reaches 100%. The status is set to Completed. |  |
| 3 | Analyze Result | Choose Analyze Results | The system shows the results in the app Evaluation Results - Business Partners (F3905). |  |

#### Data Quality Evaluation Overview

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
| 1 | Analyze Data Quality Evaluation Result | Start launchpad and open the app Data Quality Evaluation Overview - Business Partners (F3900). |  |  |
| 2 | Check | Check the score of data quality in the card Latest Data Quality Score. |  |  |

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
- related-to :: [[02-business-partner-and-product-master-data/test-script-data-quality-management-for-product-4aq-1012]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4AP_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 23,917 chars in the whole document
