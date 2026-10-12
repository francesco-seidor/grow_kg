---
id: 09-subscription-billing-and-contract-accounting/test-script-sap-fiori-analytical-apps-for-convergent-invoicing-special
title: "Test Script: SAP Fiori Analytical Apps for Convergent Invoicing Specialist (2KF) (2KF_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud 2608 test script for scope item 2KF: analyzing unbilled items (F1427) and unrated items (F1977) as Convergent Invoicing Specialist."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/convergent-invoicing-analytics]
aliases: [2KF_S4CLD2608_BPD_EN_XX]
keywords: [Convergent Invoicing Analytical Apps, convergent invoicing, unbilled items analysis, unrated items analysis, preliminary steps, business conditions, billable items, consumption items, invoicing specialist role, 2KF]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2KF_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-828
topic: 09-subscription-billing-and-contract-accounting/convergent-invoicing-analytics
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: SAP Fiori Analytical Apps for Convergent Invoicing Specialist (2KF) (2KF_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2KF_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Convergent Invoicing Analytical Apps** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | SAP Fiori Analytical Apps for Convergent Invoicing Specialist (2KF) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232843774)

[2 Prerequisites 3](#_Toc232843775)

[2.1 System Access 3](#_Toc232843776)

[2.2 Roles 3](#_Toc232843777)

[2.3 Business Conditions 3](#_Toc232843778)

[2.4 Preliminary Steps 4](#_Toc232843779)

[2.4.1 Preliminary Steps for Analyze Unbilled Items 4](#_Toc232843780)

[2.4.1.1 Create Business Data for Receivable 4](#_Toc232843781)

[2.4.1.1.1 Upload Billable Items 4](#_Toc232843782)

[2.4.1.1.2 Perform Billing Process (Optional) 4](#_Toc232843783)

[2.4.1.2 Create Business Data for Debit/Credit Memo 5](#_Toc232843784)

[2.4.1.2.1 Create Billing Request 5](#_Toc232843785)

[2.4.1.2.2 Perform Billing Process (Optional) 5](#_Toc232843786)

[2.4.2 Preliminary Steps for Analyze Unrated Item 5](#_Toc232843787)

[2.4.2.1 Create Business Data for Receivable 5](#_Toc232843788)

[2.4.2.1.1 Upload Consumption Items 5](#_Toc232843789)

[2.4.2.1.2 Perform Rating (Optional) 5](#_Toc232843790)

[3 Overview Table 7](#_Toc232843791)

[4 Test Procedures 8](#_Toc232843792)

[4.1 Analyze Unbilled Items 8](#_Toc232843793)

[4.2 Analyze Unrated Items 9](#_Toc232843794)

## Purpose

Overview

This process allows you to analyze unrated and unbilled items. The Convergent Invoicing Specialist can change the analytic view based on different dimensions such as amount, quantity, billable item types, status, dates, and processes. Analyses can be saved as new tiles in the SAP Fiori launchpad and are updated on request.

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
| Invoicing Specialist (Convergent Invoicing) | SAP_BR_INVOICING_SPEC_CINV | Convergent Invoicing / Subscription Billing | SAP_BR_INVOICING_SPECIALIST_CINV / SAP_CEC_SPT_SUBSCR_BILLG_SPCLST_PC |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 2BG - Convergent Invoicing – Invoice Creation for Usage and Service | Must be run before this test script. Billable Item must be created and don’t perform billing process. |
| 2BE - Convergent Invoicing – Invoice Correction Processing | Must be run before this test script. Billing Request must be created and don’t perform billing process. |
| 2T3 - Convergent Invoicing – Recurring and One-Off Items | Must be run before this test script. Billing Plan must be required and don’t perform billing process. |
| 3DX - Convergent Invoicing – Management and Rating of Consumption Items | Must be run before this test script. Billing Plan must be required and don’t perform billing process. |

### Preliminary Steps

#### Preliminary Steps for Analyze Unbilled Items

##### Create Business Data for Receivable

###### Upload Billable Items

External Process

For this activity, run the following steps from the Convergent Invoicing – Invoice Creation for Usage and Service (2BG) to upload billable items.

- Upload Billable Items

###### Perform Billing Process (Optional)

External Process

For this activity, run the following steps from the Convergent Invoicing – Invoice Creation for Usage and Service (2BG) to perform billing process to billable items.

- Perform Billing Process

##### Create Business Data for Debit/Credit Memo

###### Create Billing Request

External Process

For this activity, run the following steps from the Convergent Invoicing – Invoice Correction Processing (2BE) to create billing request.

- Create Billing Request

###### Perform Billing Process (Optional)

External Process

For this activity, run the following steps from the Convergent Invoicing – Invoice Correction Processing (2BE) to perform billing progress to billable items.

- Perform Billing Process

#### Preliminary Steps for Analyze Unrated Item

##### Create Business Data for Receivable

###### Upload Consumption Items

External Process

For this activity, run the following steps from the Convergent Invoicing – Management and Rating of Consumption Items (3DX) to upload consumption item.

- Upload Consumption Items

###### Perform Rating (Optional)

External Process

For this activity, run the following steps from the Convergent Invoicing – Management and Rating of Consumption Items (3DX) to perform rating to consumption items.

- Perform Rating

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/ Transaction | Expected Results |
| --- | --- | --- | --- |
| [Analyze Unbilled Items](#unique_13) [page ] 8 | Invoicing Specialist (Convergent Invoicing) | Analyze Unbilled Items (F1427) | You have SAP Fiori app running correctly |
| [Analyze Unrated Items](#unique_14) [page ] 9 | Invoicing Specialist (Convergent Invoicing) | Analyze Unrated Items (F1977) | You have SAP Fiori app running correctly |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Analyze Unbilled Items

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
| 1 | Log On | Log onto the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access App | Choose the Analyze Unbilled Items (F1427) tile. | The Analyze Unbilled Items screen displays. |  |
| 3 | Open Application Settings | Choose Settings at the diagram area. | The Set Settings dialog pops up. |  |
| 4 | Make the Settings | In the Set Settings screen, make the following entries as below:Display Currency: currencyNumber of Intervals: number of intervalsOne Interval Contains: one interval containsChoose Apply. | The application settings are updated. |  |
| 5 | Display Unbilled Items | Choose different value of drop down list to change the display criteria. | The unbilled items are displayed based on the given display criteria. |  |

### Analyze Unrated Items

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
| 1 | Log On | Log onto the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access App | Choose the Analyze Unrated Items (F1977) tile. | The Analyze Unrated Items screen displays. |  |
| 3 | Open Application Settings | Choose Settings at the diagram area. | The Set Settings dialog pops up. |  |
| 4 | Make the Settings | In the Set Settings screen, make the following entries as below:Number of Intervals: number of intervalsOne Interval Contains: one interval containsChoose Apply. | The application settings are updated. |  |
| 5 | Display Unrated Items | Choose different value of drop down list to change the display criteria. | The unrated items are displayed based on the given display criteria. |  |

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
- see-also :: [[09-subscription-billing-and-contract-accounting/serviceartbasierte-preiskondition-anlegen-sds-3gd-316]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2KF_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 12,557 chars in the whole document
