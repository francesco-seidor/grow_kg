---
id: 01-solution-foundation-and-platform/test-script-integration-of-external-output-management-solution-7dj-120
title: "Test Script: Integration of External Output Management Solution (7DJ) (7DJ_S4CLD2608_BPD_EN_XX)"
description: SAP S/4HANA Cloud Public Edition test script (scope item 7DJ) for creating an output queue and test item and verifying transmission to an external output management target.
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/output-management]
aliases: [7DJ_S4CLD2608_BPD_EN_XX]
keywords: [Output Management and External Output Systems, external output management, output queues, test item, target system check, test scripts, business roles, manual configuration, fiori launchpad, 7DJ]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7DJ_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1208
topic: 01-solution-foundation-and-platform/output-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Integration of External Output Management Solution (7DJ) (7DJ_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7DJ_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Output Management and External Output Systems** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Integration of External Output Management Solution (7DJ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232827553)

[2 Prerequisites 3](#_Toc232827554)

[2.1 System Access 3](#_Toc232827555)

[2.2 Roles 3](#_Toc232827556)

[2.3 Additional Manual Configuration 3](#_Toc232827557)

[3 Overview Table 4](#_Toc232827558)

[4 Test Procedures 5](#_Toc232827559)

[4.1 Create Output Queue 5](#_Toc232827560)

[4.2 Create Test Item 6](#_Toc232827561)

[4.3 Check Test Item in Target System 6](#_Toc232827562)

## Purpose

Overview

This scope item enables the integration of SAP S/4HANA Cloud Public Edition with external output management solutions, helping business applications meet advanced output needs. You can enable this functionality at the application level to support the diverse requirements of different applications. By default, the output solution offered by SAP S/4HANA Cloud Public Edition is used.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| SAP S/4HANA Cloud Public Edition | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Administrator | SAP_BR_ADMINISTRATOR | Output Management - Output Queues | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/f650acadb00f4e16741b516132761d0d)

## Overview Table

This scope item consists of several process steps, provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Create Output Queue | Administrator | Manage Output Queues | You create an output queue. |
| Create Test Item | Administrator | Manage Output Queues | You create a test item. |
| Check Test Item in Target System | Administrator | Target system on customer side | You check whether or not the test item was retrieved. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Output Queue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You set up an output queue that serves as target for applications creating XML output data. Managing the output queue, you can then send your data to an external system of your choice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Administrator. |  |  |
| 2 | Access App | Open the Manage Output Queues app. |  |  |
| 3 | Create Output Queue | Choose Create to add a new output queue.Enter a queue name and description and choose Continue. | A new queue draft is created. You get to the details screen to enter more information for the output queue. |  |
| 4 | Add Queue Settings | On the Queue Settings, enter the following:Transfer Type: Single TransferRetention Period (Days): 30Queue Owner: Enter the communication user that you have assigned to your communication arrangement during the set-up of the scope item.Choose Create. | The output queue is created. |  |

### Create Test Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You create a test item with sample XML content to later check the connection to the output queue server.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Administrator. |  |  |
| 2 | Access App | Open the Manage Output Queues app and open the output queue you’ve just created. |  |  |
| 3 | Create Test Item | Choose Create Test Item to create a new test item with sample XML content. | A new test item is added to the output queue. |  |

### Check Test Item in Target System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Check in the specified target system on the partner side to see if the test item has been retrieved. As there can be various systems on partner side, it's not possible to provide general testing steps for the target system.

In your SAP S/4HANA Cloud Public Edition system, you can check the item status in the Manage Output Queues app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Administrator. |  |  |
| 2 | Access App | Open the Manage Output Queues app and open the output queue you’ve just created. |  |  |
| 3 | Check Item Status | Check the Item Status for the test item you've created. | The Item Status shows Transmitted. |  |

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
- related-to :: [[01-solution-foundation-and-platform/bp-cld-entpr-2608-forms-list-en-ae-134]]
- related-to :: [[01-solution-foundation-and-platform/test-script-output-management-1lq-733]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7DJ_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 10,751 chars in the whole document
