---
id: 01-solution-foundation-and-platform/test-automation-tool-for-sap-s-4hana-public-cloud-86c-test-script-1246
title: Test Automation Tool for SAP S/4HANA Public Cloud (86C) - Test Script (86C_S4CLD2608_BPD_EN_XX)
description: "Test script for the Test Automation Tool (86C) in SAP S/4HANA Cloud Public Edition 2608: test processes, plans, test data, post-upgrade tests and results."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/test-automation-tool]
aliases: [86C_S4CLD2608_BPD_EN_XX]
keywords: [Test Automation Tool, test processes, test plans, test data container, post-upgrade tests, execution variants, intelligent test scoper, test results analysis, business roles, preliminary steps]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/86C_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1246
topic: 01-solution-foundation-and-platform/test-automation-tool
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Automation Tool for SAP S/4HANA Public Cloud (86C) - Test Script (86C_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/86C_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Test Automation Tool** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Test Automation Tool for SAP S/4HANA Public Cloud (86C) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232793023)

[2 Prerequisites 3](#_Toc232793024)

[2.1 System Access 3](#_Toc232793025)

[2.2 Roles 3](#_Toc232793026)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232793027)

[2.4 Preliminary Steps 4](#_Toc232793028)

[3 Overview Table 5](#_Toc232793029)

[4 Test Procedures 6](#_Toc232793030)

[4.1 Create a Test Process 6](#_Toc232793031)

[4.2 Create and Execute a Test Plan 6](#_Toc232793032)

[4.3 Create Reusable Test Data 7](#_Toc232793033)

[4.4 Prepare Scope for Post-Upgrade Tests 7](#_Toc232793034)

[4.5 Optimize Post-Upgrade Test Scope 8](#_Toc232793035)

[4.6 Trigger Post-Upgrade Tests 8](#_Toc232793036)

[4.7 View Results of Post-Upgrade and Customer Test Plan Executions 8](#_Toc232793037)

## Purpose

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

This chapter talks about prerequisites for the scope item.

### System Access

The test automation tool of the SAP S/4HANA Public Cloud enables you to automate and accelerate all business process tests in SAP S/4HANA Cloud Public Edition. The business process tests can be a part of test strategy during the implementation phase, user acceptance tests, or regression tests after upgrades.

The test automation tool is a part of the SAP S/4HANA Cloud Public Edition subscription and is provisioned only in the Q/T tenant by default. The tool is not available on the Starter and Production (P) environments. You can start using the Test Automation Tool from the Realize phase (SAP Activate Methodology). Test Automation Tool is also used during the regression testing after you go live.

For more information, refer [SAP Note 2129147](http://launchpad.support.sap.com/#/notes/2129147).

### Roles

You must have the SAP_BR_ADMIN_TEST_AUTOMATION business role assigned. This role is associated with the SAP_CA_BC_AUTO_TEST_PC catalog.

Make sure your SAP S/4HANA Cloud Public Edition Q/T tenant is up and running. Logon to SAP Fiori Launchpad. Navigate to the Automated Testing tab. All the Test Automation Tool applications are available. Choose the relevant tile based on your requirement. The application will open.

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

For more information, refer to [How to Create a Business Role from a Template](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html?state=latest) for SAP S/4HANA Cloud Public Edition.

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data or the SAP-provided sample data to go through the test procedure.

### Preliminary Steps

A test user must be set up as a prerequisite for test script execution. To find more information on maintaining business roles, refer [Maintain Roles for Test Execution](https://help.sap.com/docs/SAP_S4HANA_CLOUD/2ab07d21f68c41109a2eef21b8fd8466/5d867592753c465aadb81115de672f91.html?state=latest#loio8d7366f28407470eae8f1fb156bb112c). More information on additional set up you must perform to set the business role can be found in [Roles Required for a Business User](https://help.sap.com/docs/SAP_S4HANA_CLOUD/2ab07d21f68c41109a2eef21b8fd8466/5d867592753c465aadb81115de672f91.html?state=latest#loio8d7366f28407470eae8f1fb156bb112c). If you wish to understand the steps to configure conditional authentication, refer[Configure Conditional Authentication](https://help.sap.com/docs/SAP_S4HANA_CLOUD/2ab07d21f68c41109a2eef21b8fd8466/5d867592753c465aadb81115de672f91.html?state=latest#loio8d7366f28407470eae8f1fb156bb112c).

## Overview Table

This scope item consists of several process steps that are listed in the following table:

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create a Test Process](#unique_8) [page ] 6 | SAP_BR_ADMIN_TEST_AUTOMATION | Manage Your Test Processes | A test process has been created. |
| [Create and Execute a Test Plan](#unique_9) [page ] 6 | SAP_BR_ADMIN_TEST_AUTOMATION | Test Your Processes | A test plan is created and execution logs are viewed. |
| [Create Reusable Test Data](#unique_10) [page ] 7 | SAP_BR_ADMIN_TEST_AUTOMATION | Test Data Container | A test data container is created with the required, reusable test data. |
| [Prepare Scope for Post-Upgrade Tests](#unique_11) [page ] 7 | SAP_BR_ADMIN_TEST_AUTOMATION | Manage Upgrade Tests | An execution variant is created and chosen for post-upgrade test execution. |
| [Optimize Post-Upgrade Test Scope](#unique_12) [page ] 8 | SAP_BR_ADMIN_TEST_AUTOMATION | Intelligent Test Scoper | Post-upgrade test scope is proposed based on the standard code changes. |
| [Trigger Post-Upgrade Tests](#unique_13) [page ] 8 | SAP_BR_ADMIN_TEST_AUTOMATION | Post-Upgrade Tests | Post-upgrade test is triggered in SAP S/4HANA Cloud Public Edition Q/T tenant. |
| [View Results of Post-Upgrade and Customer Test Plan Executions](#unique_14) [page ] 8 | SAP_BR_ADMIN_TEST_AUTOMATION | Analyze Automated Test Results | View the results of the executed post-upgrade and customer test plans. |

## Test Procedures

### Create a Test Process

To create a test process effectively, first, you define the full testing scope by identifying all modules and integrations for your SAP S/4HANA Cloud Public Edition system. Within the Manage Your Test Processes application, you initiate this by selecting Create test process. You must provide a name for your test process and, optionally, set a scope restriction to align it with standard test scope items, which can help filter and define relations in future releases. After clicking Save, the application creates your new test process with a default New Process Step.

Next, build your test process by adding and customizing process steps. A test process consists of one or more process steps, each being a series of actions. You can add a new test process directly, create a copy of an existing standard or custom one, or upload a test process from your local device. To add a new process step, you select an existing step and choose to insert a UI or API step before or after it. You can also record user actions on an application, such as inputting data or clicking buttons, to automatically generate custom process steps within the application.

You manage your test process by editing its general information, such as its name, application area, or associated scope items. You can also modify existing process steps by changing their names, replacing them, converting standard steps into custom ones, or assigning different roles to them. It is crucial to set the test process as Visible in Test Plan so that it becomes available for creating test plans in the Test Your Processes application .

The Manage Your Test Processes application also supports recording and executing tests in different languages, along with options to upload, download, and manage multiple test processes, especially in a 3-system landscape.

For more information on creating test proceses, refer [Manage Your Test Processes](https://help.sap.com/docs/SAP_S4HANA_CLOUD/1e9ba004e0504506a135afda960e9495/b076dd00e70b4b30b1c250be655d45d2.html).

### Create and Execute a Test Plan

Create a test plan to test end-to-end business scenarios within SAP S/4HANA Cloud Public Edition. A test plan organizes one or more test processes, each representing a distinct business process. You can generate a test plan in one of two primary ways: by adding a new test plan from scratch or by copying an existing one. Additionally, you can utilize the Adapt Test Process function within the Manage Your Test Processes application to facilitate test plan creation.

To add a new test plan, navigate to the Test Your Processes home page and select the Add test plan icon. A pane will appear where you enter a unique name for your new test plan. Following this, you select the test processes you wish to include, arranging them in the precise sequence for execution. It is important to note that you cannot alter this sequence once the test plan is executed. If you select a deprecated test process, the system will prompt you for consent to proceed.

You manage the selection of test processes by using search, sort, and filter functions. You can search test processes by their name or associated scope items. The View Settings option allows you to sort processes by name, scope item, type, application area, or country. Additionally, you can filter the list of test processes by application area, type, change status (Standard or Post-Upgrade Test), or deprecation status. After confirming your selections, select Save to create the test plan with a default global variant.

For more information, refer [Test Your Processes](https://help.sap.com/docs/SAP_S4HANA_CLOUD/2ab07d21f68c41109a2eef21b8fd8466/ddd0a0cf45964225bff64c10e8de8e38.html).

### Create Reusable Test Data

Create reusable test data using the Test Data Container app in SAP S/4HANA Cloud Public Edition. This app serves as a central repository for reusable test data templates and holds multiple datasets, acting as a single source of truth for your test data needs. There, you choose Create, enter all necessary information, and then proceed to select a template.

Next, you define the structure of your test data container by selecting a template. Currently, templates are available for areas like Sales, Finance, Manufacturing, and Sourcing and Procurement. After choosing a template, you can view its fields and select the specific ones you wish to include in your test data container. You can also filter fields by scope items and optionally duplicate fields to maintain different values or add custom fields you have created. Once you confirm your selections, the test data container is created.

After creating the container, you add variants to it, as a container without variants offers no associated data values for testing. You can create variants in two ways: individually or using a spreadsheet. For individual variants, you enter details and provide values for all functional fields, which the system automatically validates. For multiple variants, you download a spreadsheet, specify the number of variants, and provide details like Variant Name, Description, Region/Country, and Company Code. You can also add common fields that apply to all variants in the spreadsheet.

Finally, you manage your test data containers and variants. You can edit a container to modify its details, templates, or fields. You can also copy a container, choosing whether to include all its variants. Variants themselves can be edited to change details or field values, or copied to create new variants. You cannot delete standard test data containers, but you can delete custom ones if they are not associated with any test plan. These reusable test data containers then integrate with the Manage Your Test Processes and Test Your Processes applications for testing and automation activities.

For more information, refer [Test Data Container](https://help.sap.com/docs/SAP_S4HANA_CLOUD/1c73afbf7d154fcf9b5ec127d1793ffa/70e4bb5e3875480ea15a033d943e4ecf.html?state=latest).

### Prepare Scope for Post-Upgrade Tests

Create execution variants using the Manage Upgrade Tests application, a tool designed specifically for scoping upgrade tests in SAP S/4HANA Cloud Public Edition. This application allows you to define a specific set of post-upgrade test processes, customer test plans, and ABAP objects to be executed together. The execution variants serve as a blueprint for your upgrade test runs, enabling you to manage and organize your testing efforts efficiently.

To create an execution variant, you first identify the test processes, test plans, or ABAP objects you want to include. In the PUT Processes, Customer Test Plans, or ABAP Unit Tests tabs, you select the checkboxes corresponding to your desired items. Then, you click the Add to Execution Variant button. The system prompts you to either select an Existing Execution Variant to update it or choose New Execution Variant to create a fresh one. If creating a new one, you provide a name and description, then save it. The selected items are then added to your chosen execution variant.

You can manage your execution variants by editing, copying, or deleting them. To edit, select an execution variant, click Edit, and update its description or mark it as the default variant. To copy, select an existing variant, click Copy, and provide a name and description for the new variant; the original variant’s scope is then duplicated. You can delete an execution variant, but you cannot delete one that is currently marked as default or has been executed previously. The Execution Variants tab displays details like name, description, creator, and last changed date.

To update the execution variant, navigate to the details page and select the checkboxes corresponding to the test processes, test plans (with or without variants), or ABAP objects and select the Remove from list button.

Finally, these execution variants are crucial for triggering actual post-upgrade test executions. When you trigger post-upgrade tests, you select the desired execution variant from a dropdown in the Test Your Processes application. The system then performs checks, such as a Role Catalog Check, before submitting the test processes and test plans for execution. You can also push optimized scopes from the Intelligent Test Scoper application directly into Manage Upgrade Tests to create a new execution variant, ensuring your upgrade tests are efficient and relevant to SAP’s standard code changes.

For more information, refer [Manage Upgrade Tests](https://help.sap.com/docs/SAP_S4HANA_CLOUD/9f3351bbe2f04b42bb29f690886a6f54/dd1dc59e34364a26b1c6183a1369612b.html?state=latest).

### Optimize Post-Upgrade Test Scope

Optimize your post-upgrade test scope using the Intelligent Test Scoper (i-TS) application. This smart tool leverages real-time analysis of SAP’s standard code changes to propose an optimized Post-Upgrade Test (PUT) scope. It helps you save effort without compromising quality, significantly reducing your test cycle time. Remember, this optimization applies only to standard test processes, not to custom ones.

To view the optimized scope, you access the i-TS application and select the Go button on the homepage. The application then displays all active scope items it proposes based on standard code changes under the Intelligent Test Scope tab. You can further refine this optimized scope by applying filters based on Test Process, Associated Scope Items, or Application Area to narrow down the displayed listings according to your preferences.

Once you have the optimized scope, you push it to the Manage Upgrade Tests application to create an execution variant. You select the Push to Manage Upgrade Tests button, which activates only when you apply an Application Area filter or no filters at all. In the pop-up window, you provide a name and description for the execution variant and choose Push. A success message confirms the transfer, and you can then navigate to Manage Upgrade Tests to view and edit this newly created variant.

You can also assess the efficiency gain by viewing the Scope Efficiency. On the i-TS homepage, select the View Scope Efficiency button. A popover appears, showing a PUT Scope Analysis chart that compares the count of processes in your Standard PUT Scope with the Optimized PUT Scope. An Overall Efficiency donut chart visually represents the percentage of efficiency gain. You can also view finer details of this scope split and efficiency gain according to specific application areas.

For more information, refer [Intelligent Test Scoper](https://help.sap.com/docs/SAP_S4HANA_CLOUD/d72d7bb74cf043a58474f0c2d76e857d/5d5d6bfa02c24adf8e12d272d93acaef.html?state=latest).

### Trigger Post-Upgrade Tests

Trigger upgrade test execution in SAP S/4HANA Cloud Public Edition through a dedicated application and by using external services for automation. To initiate a test within the Post-Upgrade Tests application, navigate to the Trigger tab. Here, select your desired execution variant from the available list and then choose the Execute button to trigger the post-upgrade test. If you need to define or modify the scope for an execution variant, go to the Scope tab, which redirects you to the "Manage Upgrade Tests" application. Pre-checks for upgrade-relevant processes, smoke tests, and start-up tests run before the main post-upgrade test plans execute.

If this is the first execution for a release after an upgrade, the tests trigger immediately. If you trigger tests after a previous execution has completed for the same release, or while another execution is in progress, the system will prompt you to confirm whether you wish to start a new execution or stop the current one.

When triggering tests, several scenarios apply: the execution triggers immediately for the first run after an upgrade. If you trigger tests after a release’s post-upgrade tests are complete, the system asks if you want a new execution. If another execution is in progress, the system asks if it should stop the current execution to start a new one. Additionally, you can provide consent for SAP to automatically trigger post-upgrade tests in your Quality/Test (Q/T) tenants during major release upgrades, which you manage in the Consent tab of the application.

On triggering execution, you can keep a track of execution status updates, such as the status of system readiness checks, smoke test, and more in the Track tab.

For more information, refer [Post-Upgrade Tests](https://help.sap.com/docs/SAP_S4HANA_CLOUD/e819bb97e28648ea949ac9b4eebcd8ca/cf701680a0a14613bb1cb6732224a6b6.html?state=latest).

### View Results of Post-Upgrade and Customer Test Plan Executions

View the results of your post-upgrade and customer test plans using the Analyze Automated Test Results application. This tool displays the outcomes of the latest test executions conducted via the Test Automation Tool, helping you assess business process testing. Its primary functions include presenting reports for both post-upgrade and customer test results, as well as showing the total number of executed processes.

Upon accessing the application, you will see Test Execution Status cards, one each for post-upgrade and customer tests. These cards show results in doughnut charts, categorizing them by status such as Canceled, Failed, Success, In Process, Untested, or Not Executable. You can hover your mouse over a bar on a chart to see the process type and the number of test processes it represents. Selecting on a chart element or the total number of executed processes takes you to the Test Results page, where you can examine the detailed execution results.

To refine your view of the test results, utilize the filtering options available. You can filter by criteria like Test Plan Name, Test Plan Type (choosing between Post-Upgrade Tests, Customer Tests, or ABAP Unit Tests), Created in Release, Application Area, Status, Process Type, or a date range for when the tests were last executed. Apply these filters and then select Go to display the results in a tabular format on the same screen. The displayed columns provide detailed information, including the test plan’s name, its type, the execution status, the timestamp of the last execution, and, for failed tests, the reason and category of failure.

Finally, the application offers several functionalities to manage and act on these results. You can export the summary of your test execution results to an Excel file directly from the Analyze Automated Test Result Details page for further analysis or documentation. Additionally, if test plans have failed, you can re-execute them using the Re-Execute button, which allows you to filter and select specific failed test plans for re-execution. From the Test Results page, you can also navigate directly to the Test Plan Details and Log Details pages within the Test Your Processes application for a more in-depth view of individual test plans and their execution logs.

For more information, refer [Analyze Automated Test Results](https://help.sap.com/docs/SAP_S4HANA_CLOUD/7ce8f79186e1445ab82e37439eba795c/a4a4c6e62b894d5a88d0d8300620e278.html?state=latest).

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
- see-also :: [[01-solution-foundation-and-platform/readme-2608]]
- see-also :: [[01-solution-foundation-and-platform/test-script-data-migration-to-sap-s-4hana-from-sap-bh3-1268]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/86C_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 24,243 chars in the whole document
