---
id: 06-management-accounting/predictive-accounting-for-service-contract-management-4v7-ae-test-scri
title: Predictive Accounting for Service Contract Management (4V7_AE) - Test Script (4V7_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 4V7_AE: predictive accounting for service contracts, margin analysis line items and revenue recognition run."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/predictive-accounting]
aliases: [4V7_S4CLD2608_BPD_EN_AE]
keywords: ["Predictive Accounting for Sales Orders, Service Contracts…", predictive accounting, service contract management, margin analysis, revenue recognition, test scripts, business roles, sample master data, business conditions, predictive quality monitor]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4V7_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1051
topic: 06-management-accounting/predictive-accounting
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Predictive Accounting for Service Contract Management (4V7_AE) - Test Script (4V7_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4V7_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Predictive Accounting for Sales Orders, Service Contracts and Travel** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Predictive Accounting for Service Contract Management (4V7_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Predictive Accounting for Service Contract Management (4V7_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232854990)

[2 Prerequisites 3](#_Toc232854991)

[2.1 System Access 3](#_Toc232854992)

[2.2 Roles 3](#_Toc232854993)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232854994)

[2.4 Business Conditions 4](#_Toc232854995)

[3 Overview Table 5](#_Toc232854996)

[4 Test Procedures 6](#_Toc232854997)

[4.1 Display Line Items - Margin Analysis 6](#_Toc232854998)

[4.2 Run Revenue Recognition: Service Document (Period-End Activity) 7](#_Toc232854999)

[4.3 Display Line Items - Margin Analysis 8](#_Toc232855000)

[5 Appendix 10](#_Toc232855001)

[5.1 Monitor Predictive Accounting - Predictive Quality 10](#_Toc232855002)

## Purpose

Overview

This scope item provides a more comprehensive overview of all service contracts including future postings for recognized, deferred, and accrued revenues resulting from the billing plan and regardless of their billing status. When a service contract is created, revenue postings reflecting the billing plan of a service contract are created in extension ledger 0E.

The Display Line Items – Margin Analysis app displays prediction journal entries along with actuals and allows users to analyze the expected results at period or quarter end.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data, and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible via SAP Analytics Cloud. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Cost Accountant - Sales | SAP_BR_SALES_ACCOUNTANT | Sales Accounting | SAP_BR_SALES_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Operating Concern | A000 |  |  |
| Controlling Area | A000 | Controlling Area A000 |  |
| Company Code | 3310 | Company Code 3310 |  |

### Business Conditions

Before this step can be run, the following business conditions must be met:

| Scope Item | Business Condition |
| --- | --- |
| 3MO - Service Contract Management | The service contract must be created and a periodic billing plan assigned. The service contract also must be in status released. |
| 3M3 - Event-Based Revenue Recognition – Service Documents or3M4 - Event-Based Revenue Recognition – Service Documents – IFRS or3M5 - Event-Based Revenue Recognition – Service Documents – US GAAP | Any one of the three scope items must be activated in the system. |

## Overview Table

This scope item consists of several process steps provided in the following table.

| ID (Role Template) | Name (Role Template) | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Display Line Items - Margin Analysis](#unique_8) [page ] 6 | Cost Accountant - Sales | Display Line Items - Margin Analysis (F4818) | Detailed analysis can be done by line item. |
| [Run Revenue Recognition: Service Document (Period-End Activity)](#unique_9) [page ] 7 | Cost Accountant - Sales | Run Revenue Recognition - Service Documents (F4278) | Values for real-time revenue for service contracts are posted. |
| [Display Line Items - Margin Analysis](#unique_8) [page ] 6 | Cost Accountant - Sales | Display Line Items - Margin Analysis (F4818) | Detailed analysis can be done by line item. |

## Test Procedures

### Display Line Items - Margin Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This report allows a user view the detail documents and predictive margin associated with the contract for any given selection criteria such as by Customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2. | Access the SAP Fiori app | Open Display Line Items - Margin Analysis (F4818). | The Display Line Items - Margin Analysis screen displays. |  |
| 3. | Adapt Filters | Make the following entries and choose Go:Ledger: 0EFiscal Year Period : <Recent fiscal periods (MMM/YYYY)>Source Reference Document : <your document or leave open>Note If the filter option is not available, select Adapt Filters and use the search feature. | The application retrieves the financial data for the chosen filters based on the information from the commitment ledger. |  |

### Run Revenue Recognition: Service Document (Period-End Activity)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is a period-end activity and is performed as part of scope item 3M3:Event-Based Revenue Recognition – Service Documents, 3M4: Event-Based Revenue Recognition – Service Documents – IFRS or 3M5: Event-Based Revenue Recognition – Service Documents – US GAAP. Performing this step again and checking the line items, you can observe the impact of both period-end event-based revenue recognition for service documents (the accured revenue is reversed) and predictive revenue (revenue prediction is reduced). The assumption is that you are running this step during a true period end which is at a different point in time than the service document creation and postings. Based on the scope selected, this step may need to be run for all ledgers involved (0L, 2L, 3L).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Run Revenue Recognition - Service Documents (F4278). | The Application Jobs view displays. |  |
| 3 | New Job | Choose the Create button. | The New Job: Run Revenue Recognition - Service Documents view displays. |  |
| 4 | Enter Selection Criteria | Make the following entries:Job Template: Run Revenue Recognition – Service DocumentsJob Name: <Enter a description or leave the default description>Choose Step 2.Start Immediately: <checked>Choose Step 3.To Fiscal Year Period: <mm/yyyy>Company Code: 3310Ledger: 0LChoose the Schedule button. | The new job is executed.Note If you get an error "Solve the 1 real-time issues before executing the revenue recognition run," go to the Manage Real-Time Revenue Recognition Issues (F4101) app and fix the error or reprocess and skip. |  |

### Display Line Items - Margin Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This report allows a user view the detail documents and predictive margin associated with the contract for any given selection criteria such as by Customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2. | Access the SAP Fiori app | Open Display Line Items - Margin Analysis (F4818). | The Display Line Items - Margin Analysis screen displays. |  |
| 3. | Adapt Filters | Make the following entries and choose Go:Ledger: 0EFiscal Year Period : <Recent fiscal periods (MMM/YYYY)>Source Reference Document : <your document or leave open>Note If the filter option is not available, select Adapt Filters and use the search feature. | The application retrieves the financial data for the chosen filters based on the information from the commitment ledger. |  |

## Appendix

### Monitor Predictive Accounting - Predictive Quality

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This monitor shows an overall view of order status, and provides the detail source documents for review.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2. | Access the SAP Fiori app | Open Monitor Predictive Accounting - Predictive Quality (F3828). | The Monitor Predictive Accounting screen displays. |  |
| 3. | Adapt Filters | Adapt filters as required. | The monitor provides you an overview of errors that need to be addressed. |  |

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
- related-to :: [[06-management-accounting/predictive-accounting-for-sales-orders-2fd-ae-test-script-824]]
- related-to :: [[06-management-accounting/predictive-accounting-for-travel-and-expense-management-4q0-ae-1042]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4V7_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 15,214 chars in the whole document
