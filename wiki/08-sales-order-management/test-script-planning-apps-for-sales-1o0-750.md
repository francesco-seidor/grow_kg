---
id: 08-sales-order-management/test-script-planning-apps-for-sales-1o0-750
title: "Test Script: Planning Apps for Sales (1O0) (1O0_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1O0: Manage Sales Plans (F2512) and Sales Performance - Plan/Actual (F2941) as Sales Manager."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/sales-planning-and-performance]
aliases: [1O0_S4CLD2608_BPD_EN_XX]
keywords: [Sales Planning and Sales Performance, sales planning, manage sales plans, sales performance analysis, sales manager role, test prerequisites, business conditions, fiori launchpad access, 1O0]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1O0_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-750
topic: 08-sales-order-management/sales-planning-and-performance
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Planning Apps for Sales (1O0) (1O0_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1O0_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Sales Planning and Sales Performance** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Planning Apps for Sales (1O0) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232860593)

[2 Prerequisites 3](#_Toc232860594)

[2.1 Roles 3](#_Toc232860595)

[2.2 System Access 3](#_Toc232860596)

[2.3 Business Conditions 3](#_Toc232860597)

[3 Overview Table 5](#_Toc232860598)

[4 Test Procedures 6](#_Toc232860599)

[4.1 Manage Sales Plans 6](#_Toc232860600)

[4.2 Sales Performance - Plan/Actual 7](#_Toc232860601)

## Purpose

Overview

For sales and distribution scenarios, this scope item provides key information that a sales manager needs regarding the creation and maintenance of Sales planning apps, effectively handling the different stages in sales planning. The Sales Manager can also select some existing sales plans to compare with actual data. In addition to this, they can navigate to the corresponding app for further analysis.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Sales Manager | SAP_BR_SALES_MANAGER | Sales Management / Internal Sales / Billing for Sales Manager / Customer Returns for Sales Manager | SAP_BR_SALES_MANAGER / SAP_SD_SPT_INT_SALES_SALES_MGR_PC / SAP_SD_SPT_BILLING_SALES_MGR_PC / SAP_SD_SPT_RETURNS_SALES_MGR_PC |  |

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Business Conditions

Follow the procedures described in the following scope items for creating corresponding business data if needed.

| Scope item | Business Condition |
| --- | --- |
| BD9 - Sell from Stock | Follow the scope item to create the corresponding business data. |
| J58 - Accounting and Financial Close | Follow test procedure Currency Exchange Rates to maintain exchange rates if needed or issue met. |

## Overview Table

This scope item consists of several process steps provided in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Manage Sales Plans](#unique_7) [page ] 6 | Sales Manager | Manage Sales Plans (F2512) | The SAP Fiori app is running correctly. |
| [Sales Performance - Plan/Actual](#unique_8) [page ] 7 | Sales Manager | Sales Performance - Plan/Actual (F2941) | The SAP Fiori app is running correctly. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Manage Sales Plans

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the Manage Sales Plans app, you as a sales manager can

- create a sales plan
- edit a sales plan
- copy the sales plan to new version
- release the sales plan version
- search the sales plan in the list page

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Sales Plans (F2512) in the Sales Planning business group. | The app is displayed. |  |
| 3 | Get Search Results | Enter some search criteria in the filter bar or leave them empty. Choose Go. | The search result of sales plans is displayed. |  |
| 4 | Create a Sales Plan | ChooseCreate, then select Create Value Plan. Go to the Sales Plan screen.In the General Information section, enter and select data for the following attributes.Sales Plan: Enter the plan name.Plan description: Enter the plan description.Currency: Enter or select the plan currency.Planned For: Select Incoming Sales Orders or Sales Volume for the plan.Planned By: select Month, Quarter, or Year for the plan.Planned From: select the start date of the plan.Planned To: Select the end date of the plan.Version: Enter the plan version name.Version Description: Enter the plan version description.In the Dimensions section, choose Add. On the Select Dimensions screen, select the planning dimensions, then choose OK.In the Plan Data section, choose Download to download the planning excel. Maintain the planning data in the excel file. Choose Upload to upload the excel file to the system.After uploading the plan data into system, choose Chart View or Table View to view the data in different format. Chart type can also be customized. Choose Filter to check more detailed plan, for example, filter value for certain Sales Organization.Choose Create to save the sales plan. | A sales plan is created.Note If you get a time out error or a no selection is possible message, save the plan, reload App, then you can edit your sales plan. |  |
| 5 | Edit the Sales Plan | On the Sales Plan screen, choose Edit. In the edit mode, make the necessary changes and then choose Save to save the changes. | The sales plan is changed. |  |
| 6 | Copy the Sales Plan to a New Version | On the Sales Plan screen, choose Copy to New Version, change the new version and choose Create. | The sales plan is copied to a new version. |  |
| 7 | Release the Sales Plan Version | On the Sales Plan screen, choose Release to release the planning version. | The sales plan version is released. |  |

### Sales Performance - Plan/Actual

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this app, you as a sales manager can compare the plan data in the sales plan with the actual sales data. The comparisons gain insights into sales performance and effectiveness of sales planning. Additionally, you can do further actions using easy navigation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Set User Default Values | Choose the user icon and select Settings. On the Settings screen, choose Default Values. Maintain values for your user. For example, Exchange Rate Type, Display Currency. Choose Save. | The user default values are set. |  |
| 3 | Access the App | Open Sales Performance - Plan/Actual (F2941) in the Sales Planning business group. | The app opens. |  |
| 4 | Select Sales Plan and Version | Choose the icon on the right side of the Sales Plan input box. On the Select: Sales Plan screen, enter the information needed, then choose Go. In the result list, select one sales plan, and choose Go. | The plan and actual data are displayed in the app. |  |
| 5 | Select More Dimension | Choose View By in the chart to select More Dimension, which is available in the sales plan for analysis. For example, choose Sales Organization. | The Plan/Actual data is adjusted accordingly. |  |
| 6 | Navigate to Target Apps | Choose Actions in the chart and choose the smart link for navigating to the target apps for further analysis. For example, choose Show Quotation Conversion Rates. | The target apps open successfully. |  |
| 7 | View Management | Navigate back to the Sales Performance - Plan/Actual app, apply some filters in the filter bar, and choose the Select View icon. On the My Views screen, choose Save As. On the Save View screen, enter the view name and select the necessary checkbox, and then choose Save. You can also manage the view by choosing Manage on the My Views screen. | The views can be managed for the app. |  |

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
- see-also :: [[01-solution-foundation-and-platform/predictive-analytics-model-training-supply-chain-20n-test-script-795]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1O0_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 12,614 chars in the whole document
