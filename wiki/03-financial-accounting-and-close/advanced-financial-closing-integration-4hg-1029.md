---
id: 03-financial-accounting-and-close/advanced-financial-closing-integration-4hg-1029
title: Advanced Financial Closing Integration (4HG) (4HG_S4CLD2608_BPD_EN_XX)
description: "SAP S/4HANA Cloud test script for scope item 4HG: connecting to SAP Advanced Financial Closing on BTP, managing closing task lists and processing closing tasks."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/advanced-financial-closing]
aliases: [4HG_S4CLD2608_BPD_EN_XX]
keywords: [SAP Advanced Financial Closing Integration, advanced financial closing, closing task lists, closing tasks, communication systems, financial close, sap btp, business roles, additional configuration, test scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4HG_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1029
topic: 03-financial-accounting-and-close/advanced-financial-closing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Advanced Financial Closing Integration (4HG) (4HG_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4HG_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **SAP Advanced Financial Closing Integration** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Advanced Financial Closing Integration (4HG) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232837650)

[2 Prerequisites 3](#_Toc232837651)

[2.1 System Access 3](#_Toc232837652)

[2.2 Roles 3](#_Toc232837653)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232837654)

[2.4 Additional Manual Configuration 4](#_Toc232837655)

[3 Overview Table 6](#_Toc232837656)

[4 Test Procedures 7](#_Toc232837657)

[4.1 Monitor Communication Systems 7](#_Toc232837658)

[4.2 Manage Closing Task Lists 8](#_Toc232837659)

[4.3 Process Closing Tasks 10](#_Toc232837660)

## Purpose

Overview

SAP Advanced Financial Closing is a standalone public cloud solution delivered on SAP BTP to orchestrate the financial close process. The solution supports the planning, execution, monitoring, and analysis of recurring financial tasks for all entities of a corporation. You can define closing task lists, assign responsibilities, parameters, and dependencies. Besides embedded workflows and approval functionality, the cockpit also contains detailed analytical apps and KPIs to monitor the closing process in real time.

This scope item provides connection setup between SAP S/4HANA Cloud and SAP Advanced Financial Closing, and the steps on SAP Advanced Financial Closing to orchestrate the financial closing activities.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |
| --- |
| Note The SAP Fiori launchpad for AFC is on SAP BTP. |

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

SAP BTP

Assign static role templates for SAP Advanced Financial Closing to your test users. For more information, refer to [How to Manage Static Role Templates](https://help.sap.com/docs/advanced-financial-closing/administration/how-to-manage-static-role-templates). For an overview of available role templates, refer to [Static Roles for SAP Advanced Financial Closing](https://help.sap.com/docs/advanced-financial-closing/administration/static-roles-for-advanced-financial-closing).

For the steps described in this document, authorizations within [Task List Creation Scope](https://help.sap.com/docs/advanced-financial-closing/administration/task-list-creation-scope) and [Task Processing Scope](https://help.sap.com/docs/advanced-financial-closing/administration/task-processing-scope) are required.

SAP S/4HANA Cloud Public Edition

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log on |
| --- | --- | --- | --- | --- |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

Default Values

The organizational structure and master data of your company was created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

The business process is enabled with this organization-specific master data, examples are provided in the next section.

Using Your Own Master Data

You can also use customized values for any material or organizational data for which you have created master data. For more information on how to create master data, see the Master Data Procedures documentation.

Use the following master data in the process steps described in this document:

| Master Data | Sample Value | Details | Comment |
| --- | --- | --- | --- |
| Company Code | <company code> |  |  |
| Chart of Accounts | YCOA |  |  |
| Controlling Area | A000 |  |  |
| Cost Center | <cost center> |  |  |

For more information about creating master data objects, see the following Master Data Scripts (MDS):

| Master Data ID | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNH | Create Profit Center - MDS |

### Additional Manual Configuration

You must have completed the configuration steps outlined in the [Administration Guide](https://help.sap.com/products/AFC/b021b34a2c2d4943abc3a31008c7bdfc/6e1af2743721420782fcb82472c9ce86.html) for AFC on SAP BTP.

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/f2a9aaa5720f14ec79b27380813908d6)

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Monitor Communication Systems](#unique_8) [page ] 7 | General Ledger Accountant | Monitor Communication Systems | The connection status of the communication system is OK. |
| [Manage Closing Task Lists](#unique_9) [page ] 8 | General Ledger Accountant | Manage Closing Task Lists | The task list is released and tasks are sent for processing to the responsible processors. |
| [Process Closing Tasks](#unique_10) [page ] 10 | General Ledger Accountant | Process Closing Tasks | The task is completed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Monitor Communication Systems

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you confirm that your communication system is connected.

Prerequisite

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Manage Advanced Financial Closing. | You are navigated to the launchpad on SAP BTP. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad for AFC as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Monitor Communication Systems. |  |  |
| 3 | Check Status | From the table, open the system details of a communication system.In the Status section, check the Connection Check tile for more details. | The Status of the connection is OK. |  |

### Manage Closing Task Lists

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define a template with the respective closing tasks and generate a task list for processing by the responsible users.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad for AFC as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Manage Closing Task Lists | The Manage Closing Task Lists screen displays. |  |
| 3 | Create Template | Choose Create. |  |  |
| 4 | Enter Template Details | Make the following entries and choose Create:Template ID: for example, 0001Task List Default Description: for example, Month-End ClosingOwner Type: for example, UserOwner: for example, GL_ACCOUNTANTResponsible User Type: UserEmail Notification Configuration: <notification configuration>Time Zone: <time zone> |  |  |
| 5 | Add Communication System | Choose Open Closing Structure.Select your template and choose Add System.Make the following entries and choose Next Step:Communication System: <your S/4HANA Cloud system>Folder Default Description: <description>Factory Calendar ID: <ID>Ledger: for example, 0LAccounting Principal: <accounting principle>Fiscal Year Variant: <fiscal year variant> | The Define Closing Structure screen displays.Note The Communication System governs the basic settings for the task list. |  |
| 6 | Add Organizational Units | Select Add organizational units now.Make the following entries:Hierarchy Type: for example, Company CodeSelect your organizational units and choose Review.Choose Finish. | The organizational units are added. |  |
| 7 | Assign Task List Model | On the Define Closing Structure screen, select an organizational unit and choose Assign Task List Model.Select the task list model and choose Select.Choose OK. | The task list model is assigned to the organizational unit. |  |
| 8 | Assign Processing User (Optional) | Drill down to a task folder under one organizational unit and choose >.Select a task and choose Edit.Assign a user to the Processing User field and choose Apply. | Note To do a mass change of a field value, you can expand the hierarchy, select multiple tasks, and then choose Change. You can also choose As Flat List to view, search or sort by the task name you would like to change. |  |
| 9 | Release Task List | On the Manage Closing Task Lists screen, select your template and choose Generate Task List.Make the following entries and choose Generate Task List:Closing Key Date: <key date>Fiscal Year: <year>Posting Period: <period>Task List Default Description: <description>Closing Type: for example, Month-End ClosingRelease Task List: Selected | The task list is generated. |  |

### Process Closing Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you process closing tasks. You are shown a detailed overview of the tasks. You verify that the integration to AFC is configured correctly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad for AFC as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Process Closing Tasks. | The Process Closing Tasks screen displays. |  |
| 3 | Display Closing Tasks List | Make the following selections and choose Go:Closing Type: for example, Month-End ClosingTask List Status: Released and Active | The tasks and the overall progress for each task are displayed in a list form. |  |
| 4 | View Task List Details | Choose a Task List. | The Task List screen displays.Note On the Task List screen, you can filter the tasks with standard filters (for example, Tasks for which I'm the processing user). |  |
| 5 | Process Closing Task | Select a Fiori type task and choose Process | The system opens a new browser tab which navigates to the respective Fiori app. Complete the task as needed, then return to the browser tab of the AFC system to continue processing AFC tasks |  |
| 6 | Select Task | Select the checkbox for a task and choose Change Status. | The Change Status dialog box is displayed. |  |
| 7 | Change Task Status | Make the following entries and choose OK:Change Status: Completed Without ErrorsStatus Change Reason: Already completed | The task status is updated. |  |
| 8 | Select Job | Select a task of type Job and choose Schedule. |  |  |
| 9 | Schedule Closing Task | Select Start Immediately and choose OK. | The status of the task changes first to scheduled and then to completed. |  |
| 10 | Display Task Details | Select a Job and choose Details. | The Task screen displays.Note The Task screen displays the following information:Details: general information regarding the task such as processor, responsible, approval statusStatus Change: includes job logs, spoolsDependencies: displays any task that precedes or follows the current task being displayed. It also shows the Critical Path, meaning tasks that need to be completed in order to complete the current task. |  |

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
- see-also :: [[03-financial-accounting-and-close/test-script-accounting-and-financial-close-group-ledger-ifrs-1ga-ae-sa]]
- see-also :: [[03-financial-accounting-and-close/test-script-account-reconciliation-sap-solution-extensions-by-blacklin]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4HG_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 17,240 chars in the whole document
