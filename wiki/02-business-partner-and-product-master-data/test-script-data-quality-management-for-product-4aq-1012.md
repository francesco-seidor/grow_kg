---
id: 02-business-partner-and-product-master-data/test-script-data-quality-management-for-product-4aq-1012
title: "Test Script: Data Quality Management for Product (4AQ) (4AQ_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script (4AQ) for product data quality: rule mining, validation rules, quality scores, evaluation runs and overview."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/data-quality-management]
aliases: [4AQ_S4CLD2608_BPD_EN_XX]
keywords: [Data Quality Management for Products and Business Partners, data quality management, rule mining, validation rules, data quality scores, data quality evaluation, product master, business roles, feature activation, master data governance]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4AQ_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1012
topic: 02-business-partner-and-product-master-data/data-quality-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Data Quality Management for Product (4AQ) (4AQ_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4AQ_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Data Quality Management for Products and Business Partners** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Data Quality Management for Product (4AQ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232839442)

[2 Prerequisites 3](#_Toc232839443)

[2.1 System Access 3](#_Toc232839444)

[2.2 Roles 3](#_Toc232839445)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232839446)

[2.4 Business Conditions 4](#_Toc232839447)

[3 Overview Table 5](#_Toc232839448)

[4 Test Procedures 6](#_Toc232839449)

[4.1 Discover Validation Rules by Using Rule Mining 6](#_Toc232839450)

[4.1.1 Create Rule Mining for Product 6](#_Toc232839451)

[4.1.2 Process Rules from Rule Mining Run 7](#_Toc232839452)

[4.2 Master Data Quality Management 8](#_Toc232839453)

[4.2.1 Create Validation Rule 8](#_Toc232839454)

[4.2.2 Configure Data Quality Scores 10](#_Toc232839455)

[4.2.3 Evaluation Data Quality for Products 12](#_Toc232839456)

[4.2.4 Data Quality Evaluation Overview 13](#_Toc232839457)

## Purpose

Overview

This scope item enables you to define data quality rules and KPIs for product master data. You can evaluate the quality of product master data according these rules and monitor the current state of the data quality as well as its trend.

To define rules, you can use machine learning capabilities and detect patterns with rule mining. These patterns from rule mining can be transferred to data quality rules.

By analyzing the evaluation results, you can identify areas of data with errors and potential reasons for data with errors, and you can then initiate the correction. Furthermore, you can use the data quality rules to validate data in Master Data Consolidation for Product (‏1N1‏) and Central Governance for Product (‏1N5‏).

Several business catalogs can be assigned to a business role to perform various functional needs. For more information on the business catalog details, see the test script.

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

For more information, refer to How to Create a Business Role from a Template in the product assistance for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Master Data Steward - Product Data | SAP_BR_PRODMASTER_STEWARD | Product Governance | SAP_CMD_SPT_PR_GOV_PC |  |

The following are the business catalogs that can be assigned to a business role to perform various functional needs.

Administration/Manage Rules ( SAP_CMD_BC_PR_QLTY_MNG_PC ) : Manages data quality rules and derivation scenarios, schedule data quality evaluations, and configure data quality scores.

Analytics ( SAP_CMD_BC_PR_QLTY_ANA_PC ) : Analyzes data quality evaluations.

Manage Rule Mining ( SAP_CMD_BC_QLTY_PR_MINING_PC ) : Execute mining run to get system proposed rules.

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

### Business Conditions

Activate Features

In a software update, SAP delivers certain features that could have an impact on your implemented solution initially in an inactive state. You can choose to already activate these features before they become available by default in a later release.

The test procedures in this document describe the software behavior when all features have been activated. It is a prerequisite for testing that you have activated all of the following features in each of your systems using the configuration activity Activate Features. For more information about this activity, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/3e94fcc37b42433b97d6aef0c830dc52.html) for SAP S/4HANA Cloud Public Edition.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

- Configure Your Solution:

Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

Navigate to Manage your Solution > Configure Your Solution. Search for Activate Features. In the search result, select the configuration activity and go to the next screen. Select the configuration step and choose Configure.

- SAP Central Business Configuration:

Log on to the project experience in SAP Central Business Configuration.

Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Features. Choose the link to navigate directly to the target system of SAP S/4HANA Cloud Public Edition. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

| Feature ID | Feature Title |
| --- | --- |
| MDC_PRODUCT_GOVERNANCE | Successor MDG Apps for Product - Cloud-Ready Mode in MDG |

## Overview Table

The scope item Data Quality Management for Product s (4AQ) consists of several process steps provided in the table below.

|  |
| --- |
| Note Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder . |

| Choose the appropriate entity: Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Rule Mining for Product](#unique_8) [page ] 6 | Master Data Steward - Product Data | SAP Fiori: Manage Rule Mining - Products (F4085) | With this app, you can create and start a rule mining run to discover business rules for your master data records. In a mining run, you can define the focus for a mining run and specify the fields that could be potential condition fields and checked fields for your new rules. When you start the mining run, the system uses a machine-learning algorithm to propose a list of potential rules based on your input. This app assists the master data steward in uncovering potential rules for their master data and so shortens the preparation time of rule definition. |
| [Process Rules from Rule Mining Run](#unique_9) [page ] 7 | Master Data Steward - Product Data | SAP Fiori: Process Rules from Rule Mining - Products (F4071) | With this app, you can review and manage rules generated from rule-mining runs for Products. You can decide to accept the rules or set them for review by others from this app. You can either create a new validation rule directly from the accepted mined rules or link the mined rules to existing validation rules. |
| Create Validation Rule [page ] 7[Create Validation Rule](#unique_10) [page ] 8 | Master Data Steward - Product Data | SAP Fiori: Validation Rules - Products (F4083A) | This app enables you to describe, catalog, implement, and simulate validation rules using a central rule repository. These validation rules can be used for data quality evaluation for Products and to validate products in mass processing and consolidation. |
| [Configure Data Quality Scores](#unique_11) [page ] 10 | Master Data Steward - Product Data | SAP Fiori: Configure Data Quality Scores for Products (Version 2) (F4090A) | With this app you can configure how a data quality score is calculated, based on the evaluation of Product data in combination with validation rules. You can create data quality dimensions, categories of data quality dimensions, and assign rules to these data quality dimensions. This results in a hierarchy with data quality categories at the top, data quality dimensions at the next level, and assigned rules at the lower level. The system calculates scores for dimensions and categories based on this information. |
| [Evaluation Data Quality for Products](#unique_12) [page ] 12 | Master Data Steward - Product Data | SAP Fiori: Evaluate Data Quality - Products (F9311) | With this app you can create, execute, and schedule data quality evaluations runs. You can also delete entire existing runs or choose to delete the results of evaluations and keep their aggregated data to use in score calculation. |
| [Data Quality Evaluation Overview](#unique_13) [page ] 13 | Master Data Steward - Product Data | SAP Fiori: Data Quality Evaluation Overview - Products (F3260) | This app provides dashboards showing a high-level overview of your data quality and data quality trends across an entire business object. This data is always based on the default category Global. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Discover Validation Rules by Using Rule Mining

#### Create Rule Mining for Product

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
| 2 | Access App | Open App Manage Rule Mining - Products (F4085) under group Data Quality Management for Products | The Manage Rule Mining - Products (F4085) screen displays |  |
| 3 | Create a new Mining Run | Choose Create to create a new Mining Run. Enter the following data:Description:Goal:In the section of Tables, choose Add, choose the table from the popup. For example, MARA. Then choose Select and a new sub screen Basic Data will be displayed on the right.In the Focus Area section under Basic Data:Choose Add in the popup select the field you need, for example: Material Type (MTART).Set the value to the field you choose: for example, set the field Material Type (MTART) with the value HALB (Semifinished Product).In the Fields section under Basic Data:Choose Add in the popup, select the field you need, and choose Select. For example, select the fields: Weight Unit (GEWEI), Material Group (MATKL), Base Unit of Measure (MEINS).In the result list of selected fields, keep the checkbox of Condition of Rule for each field selected and select at least one checkbox of Checked by Rules.Choose Apply, then choose Create. | A new rule mining run has been created |  |

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
| 1 | Start Rule Mining Run | Open App Manage Rule Mining - Products (F4085), select the rule mining run you created in part Create Rule Mining for Product, choose Start.In the popup, choose OK to confirm the start action. | A mining run starts, and the status is Running. |  |
| 2 | Complete the Rule Mining Run | Refresh until the status changed to Completed. | The status of rule mining run is Completed. |  |
| 3 | Process Rules from Rule Mining Run | Choose the number of Total Rules. You are navigated to the app Process Rules from Rule Mining for Product. Select one rule from the list and choose Accept | The rule status is changed from Initial to Accepted. |  |
| 4 | Link Mining Rule to Validation Rule | Select the accepted rule. Choose Link to Validation Rule. In the dropdown list, choose Link to New Rule.In the popup, enter the ID and Description of your New Validation Rule.ID:Description:Choose Save. | In the column Linked Validation Rule, a new Validation Rule has been linked. |  |
| 5 | Review the Validation Rule | Choose the Rule ID under the column Linked Validation Rule. In the popup, choose Validation Rules for Products. You are navigated to the app Validation Rules for Products, and the rule which you created in the step 4 is displayed. | In the section Rules from Rule Mining, one mining rule which you selected in step 3 has been linked. |  |
| 6 | Rule Mining Implementation | In the Section Usage, choose Add and select one or more usages from the dropdown list. For example, select Check in Consolidation.Choose the button Send for Implementation. Then choose Prepare for this usage, in the popup, choose Prepare Usage. | In the section Rule Mining Implementation, the Decision Tables for Scope and Condition have been created and status are Active. |  |

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
| 2 | Access App | Open the Validation Rules - Products (F4083A) app. | The Validation Rules for Products screen is displayed. |  |
| 3 | Create new rule | Choose Create to create a new rule. Enter the following data:Rule ID :Rule name :Base Table: Select the table that you want to check with this rule, for example, Basic Data (MARA).Checked Field: Enter the field that you want to check with this rule, for example, MARA -MTART.Choose Create. | The system creates a new rule. The status of the rule is New. |  |
| 4 | Change Status for Implementation | Choose Send for Implementation. | The rule status has been changed to To Be Implemented. |  |
| 5 | Prepare Usage | Choose Edit, then in the Usage section, choose Create, and then select Data Quality Evaluation from the drop-down list. Choose Save.Choose the radio button for this record. In Usage Action, choose Prepare. In the pop-up screen, choose Base Table as default, and choose Prepare Usage in the pop-up screen. | The Usage has changed to Disabled, and the Usage Action is Enable. |  |
| 6 | Implemented BRF+ Rule | Search the rule created in step 3.In the Implementation section, choose the link under Scope Expression. The system opens the BRFplus Workbench. Choose Edit to maintain the expression.The same step for the link under Condition Expression.Here's an example:Scope: MTART is equal to FERT, Condition: Gross weight is greater than Net Weight:Scope:Choose Edit:Operand -> Use Direct Value Range From -> Context -> More-> Material Type MTARTIs equal toFERTChoose Save -> Activate Condition:Choose Edit Operand -> Use Direct Value Range From -> Context -> More->Gross WeightIs greater thanNet WeightChoose Save -> Choose Activate. | The status under Scope and Condition has changed to Active. |  |
| 7 | Simulate Validation Rule | In the Simulations section, select Create.In the pop-up screen, enter a description in the Description field, then choose Save.The Simulate Validation Rule process is created. Define select types and field values to determine the range of records to be simulated.Choose Start, and wait until the process is Stopped for Review.Choose the back arrow button of the process and navigate back to the rule repository. | The created Simulation with process ID is displayed in the Simulations section. The status and other fields contain the simulation result. |  |
| 8 | Change Status to Send for testing | Choose Send for Testing for this rule. | The rule status has changed to To Be Tested. |  |
| 9 | Change Status to Approve | Select the rule created in step 3. Choose Approve. | The rule status has changed to Approved. |  |
| 10 | Enable Usage | Select the rule created in step 3.In the Usage section, choose Enable for Usage Data Quality Evaluation. | The Usage status has changed to Enabled and the Usage Action is Disable. |  |

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
| 1 | Create new category | Start the launchpad and open the app Configure Data Quality Scores for Products (Version 2) (F4090A)Choose Create to create a new dimension categoryIn the Header section, enter the following information:Category name:TargetWarningCriticalFor Example:Target : 99Warning : 90Critical : 80Note If you cannot find the app Configure Data Quality Scores for Products (Version 2) (F4090A) on your home page, go to the User icon-> Setting-> Spaces->set the user spaces to be closed ->Save. |  |  |
| 2 | Create new Dimension | In the Dimension section, choose Add Dimension to create a new dimension:Dimension name:TargetWarningCriticalFor Example:Target : 95Warning : 88Critical : 80Choose Save. | A new Category with Dimension has been created |  |
| 3 | Assign the newly created rule to your new dimension | Choose Edit in the Category screen. Choose the dimension that you created in step 2. The system goes to the screen of Rule assignment.Choose AddSearch the rule you have created before, choose Select,Enter an impact value from the dropdown menuChoose Apply.Choose Save. | The rule assignment is saved. |  |

#### Evaluation Data Quality for Products

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
| 1 | Create Process for Evaluation Run | Start the launchpad and open the app Evaluate Data Quality - Products (F9311).Choose Create :Description :Process template : SAP: Data Quality Evaluation for ProductChoose Create . | New process has been created. |  |
| 2 | Start Evaluation Process | Choose Start to run the evaluation process manually. | The evaluation process is started. The progress bar eventually reaches 100%. The status is set to Completed. |  |
| 3 | Analyze Result | Choose Analyze Results . | The system shows the results in the app Evaluation Results - Products (F3262) . |  |

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
| 1 | Analyze Data Quality Evaluation Result | Start launchpad and open the app Data Quality Evaluation Overview - Products (F3260) |  |  |
| 2 | Check | Check the score of data quality in the card Latest Data Quality Score |  |  |

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
- related-to :: [[02-business-partner-and-product-master-data/data-quality-management-for-business-partner-4ap-test-script-1011]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4AQ_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 24,326 chars in the whole document
