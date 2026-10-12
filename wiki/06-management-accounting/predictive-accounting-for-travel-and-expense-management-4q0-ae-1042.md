---
id: 06-management-accounting/predictive-accounting-for-travel-and-expense-management-4q0-ae-1042
title: Predictive Accounting for Travel and Expense Management (4Q0_AE) (4Q0_S4CLD2608_BPD_EN_AE)
description: "Test script for scope item 4Q0: commitments by cost center and project budget reporting from SAP Concur travel and expense, in S/4HANA Cloud Public Edition 2608."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/predictive-accounting]
aliases: [4Q0_S4CLD2608_BPD_EN_AE]
keywords: ["Predictive Accounting for Sales Orders, Service Contracts…", predictive accounting, travel and expense, commitment management, project budget report, budget availability control, business roles, demo data, business conditions, test procedures]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4Q0_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1042
topic: 06-management-accounting/predictive-accounting
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Predictive Accounting for Travel and Expense Management (4Q0_AE) (4Q0_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4Q0_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Predictive Accounting for Sales Orders, Service Contracts and Travel** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Predictive Accounting for Travel and Expense Management (4Q0_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232854944)

[2 Prerequisites 3](#_Toc232854945)

[2.1 System Access 3](#_Toc232854946)

[2.2 Roles 3](#_Toc232854947)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232854948)

[2.4 Business Conditions 4](#_Toc232854949)

[2.5 Preliminary Steps 4](#_Toc232854950)

[2.5.1 Predictive Accounting for Expense and Reimbursement Management 4](#_Toc232854951)

[3 Overview Table 5](#_Toc232854952)

[4 Test Procedures 6](#_Toc232854953)

[4.1 Analytics 6](#_Toc232854954)

[4.1.1 Commitment Management by Cost Center 6](#_Toc232854955)

[4.1.2 Monitor Projects via Project Budget Report 7](#_Toc232854956)

## Purpose

Overview

Use the integration between travel and expense management in SAP Concur and finance in SAP S/4HANA Cloud Public Edition to forecast the impact of your employees' business trips on the budget planned and allocated to cost centers or projects.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data, and business conditions.

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
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| Project Financial Controller | SAP_BR_PROJ_FIN_CONTROLLER | Project Control - Finance | SAP_BR_PROJ_FIN_CONTROLLER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Controlling Area | A000 | A000 |  |

### Business Conditions

Before this scope item can be tested, the following mandatory business condition must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 1M1 – Travel Expense Processing with SAP Concur |  |

### Preliminary Steps

#### Predictive Accounting for Expense and Reimbursement Management

You must configure the Activate Predictive Accounting configuration activity specifically for Time Expense Mgmnt.

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Valid cost objects in SAP S/4HANA is either a cost center (scope item J54: Overhead Cost Accounting) or WBS (scope item 1NT: Project Control – Finance or 35F: Project Control – Capital Projects) for cost recording. This scope item covers the commitment posting in Ledger 0E. You would need to additionally configure for budget and budgetary controls for travel expense via the configuration activity Maintain Budget Availability Control Profile for Cost Centers or Maintain Budget Availability Control Profile for Projects which is not covered in this scope item. You can also refer to the preliminary step (under Prerequisites) Optional: Updating Cost Center Budget Profiles (only required when using cost center budget functionality) in J54: Overhead Cost Accounting and 1NT: Project Control – Finance for budget settings.

## Overview Table

This scope item consists of several process steps provided in the table below:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Commitment Management by Cost Center](#unique_9) [page ] 6 | Cost Accountant - Overhead | Commitments by Cost Center (F3016) | Report showing commitments on the purchasing side for cost centers is displayed. |
| [Monitor Projects via Project Budget Report](#unique_10) [page ] 7 | Project Financial Controller | Project Budget Report (F3377) | Monitor Projects and view Project Budget Report. |

## Test Procedures

This section describes the test procedures for each process step that belongs to this scope item.

### Analytics

#### Commitment Management by Cost Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This report allows visibility of purchase order commitments from travel and expense management to be viewed by cost center and cost elements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Commitments by Cost Center (F3016). | The Commitments by Cost Center (F3016) screen displays. |  |
| 3 | Selection Criteria | Make the following entries:Ledger: 0LPlan Category: PLNCompany Code: 3310Fiscal Year: <Current year> |  |  |
| 4 | Choose | Choose Go. | A report showing commitments on the purchasing side for the cost centers is displayed. |  |

#### Monitor Projects via Project Budget Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can analyze the cost structure of your project and check planned budget.

Based on the budget availability profile selected during the project creation, you would be able to see the budget consumption report for a particular fiscal year or overall project duration.

Prerequisites

If you intend to use Project Budget, make sure that you activate the non-standard scope item Predictive Commitments Management (2I3) which is a prerequisite for budgeting. Once activated, commitment management ledger 0E is active and applicable for all company codes and countries. These commitments are updated in Extension Ledger 0E (predelivered) in ACDOCA table. Commitments are reduced by various business transactions such as goods receipt. The default content for Project Budgeting utilizes PS001 profile, and you can either update this profile or create your own profile via the configuration activity Maintain Budget Availability Control Profile for Projects.

Ensure that you perform the Preliminary Steps of this document to update the following:

- Maintain Financial statement YPS2
- Tag ACT_COST which is mandatory for G/Ls relevant for Budget check. Note that currently Commitment/Budget do not work for Purchase order without material.
- Maintain Financial Statement Versions (FSV)
- Assign Semantic Tags for FSV
- Set Report Relevancy
- Replicate Runtime Hierarchy. Make sure G/Ls relevant for Budget are part of this structure.

To view commitments in the report, an open purchase order and/or requisition must exist. For details on creating purchase orders, refer to Consumable Purchasing (BNX).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller . | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Project Budget Report (F3377). | The Project Budget Report - Overview screen displays. |  |
| 3 | Enter Selection Criteria | In the upper area, make the following entries and choose Go.Project : <Refer the respective project created in the Create Project section>Example O.000001 (for Overhead Project)I.000001 (for Investment Project)R.000001 (for Revenue Project)S.000001 (for Statistical Project)Planning Category: PlanFiscal Year: Current year | Details of the project structure and the corresponding planned budget are displayed.Note The aggregated and non- aggregated costs of the selected project are displayed. In the budget report, you would see the assigned value (Commitment +Actual) and available budget (Budget-Assigned Value) based on which you can analyze the project. |  |
| 4 | Navigation to Project Budget Report - Line items; view details of different cost | Select the project in the table, and choose View Details.On the Project Budget Report - Line items screen, check the financials using drilldown and filter possibilities.Note In the Standard section, the information is shown in the Compact Filter view by default.You can also change it to Visual Filter view to get an easy understanding of overall costs of the project. This visual depiction helps the stakeholders to get an overview of the project | All the plan, actual and budget costs are displayed. |  |
| 5 | Navigation to Project Budget Report- Line items: view graphical representation of different costs | In the Project Budget Report - Line items screen, you will see the different cost items recorded on the project as graphical representations, such as the bubble chart, bar graph and pie chart.Note You can see the details of the cost items by hovering the cursor on the graphs. | The cumulative actual costs, commitments, and budget posted on the project are displayed. |  |

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
- related-to :: [[06-management-accounting/predictive-accounting-for-service-contract-management-4v7-ae-test-scri]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4Q0_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 15,511 chars in the whole document
