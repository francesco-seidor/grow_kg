---
id: 06-management-accounting/predictive-accounting-for-sales-orders-2fd-ae-test-script-824
title: Predictive Accounting for Sales Orders (2FD_AE) - Test Script (2FD_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 2FD: sales accounting overview, incoming sales orders and presumed/actual gross margin reports."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/predictive-accounting]
aliases: [2FD_S4CLD2608_BPD_EN_AE]
keywords: ["Predictive Accounting for Sales Orders, Service Contracts…", predictive accounting, incoming sales orders, gross margin, sales accounting overview, test scripts, situation handling, business roles, business conditions, demo data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2FD_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-824
topic: 06-management-accounting/predictive-accounting
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Predictive Accounting for Sales Orders (2FD_AE) - Test Script (2FD_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2FD_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Predictive Accounting for Sales Orders, Service Contracts and Travel** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Predictive Accounting for Sales Orders (2FD_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232849477)

[2 Prerequisites 3](#_Toc232849478)

[2.1 System Access 3](#_Toc232849479)

[2.2 Roles 3](#_Toc232849480)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232849481)

[2.4 Business Conditions 4](#_Toc232849482)

[3 Overview Table 6](#_Toc232849483)

[4 Test Procedures 7](#_Toc232849484)

[4.1 Sales Accounting Overview 7](#_Toc232849485)

[4.2 Review Incoming Sales Orders Report 8](#_Toc232849486)

[4.3 Gross Margin Presumed/Actual 9](#_Toc232849487)

[5 Appendix 11](#_Toc232849488)

[5.1 Using Situation Template (Optional) 11](#_Toc232849489)

## Purpose

Overview

This scope item provides a more comprehensive overview of all orders and their values for the period regardless of billing status. When a sales order is created, a revenue posting is created in extension ledger 0E.

A report displays all incoming sales orders for a given fiscal period. The Presumed Gross Margin app displays prediction journal entries along with actuals, and allows you to analyze the expected results at the end of a period/quarter.

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
| Cost Accountant - Sales | SAP_BR_SALES_ACCOUNTANT | Sales Accounting | SAP_BR_SALES_ACCOUNTANT |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Operating Concern | A000 |  |  |
| Controlling Area | A000 |  |  |
| Company Code | 3310 |  |  |

### Business Conditions

Before this step can be run, the following business conditions must be met:

| Scope Item | Business Condition |
| --- | --- |
| BKP - Customer Returns | Perform all steps in the test script. |
| 1EZ - Credit Memo Processing | Perform all steps in the test script. |
| 1F1 - Debit Memo Processing | Perform all steps in the test script. |
| 1WO - Extended Intercompany Processes for Sales | Perform all steps in the test script. |
| BKA - Free Goods Processing | Perform all steps in the test script. |
| BDA - Free of Charge Delivery | Perform all steps in the test script. |
| 1HO - Intercompany Sales Order Processing – Domestic | Perform all steps in the test script. |
| 1MX - Intercompany Sales Order Processing – International | Perform all steps in the test script. |
| BKL - Invoice Correction Process with Credit Memo | Perform all steps in the test script. |
| BDQ - Invoice Correction Process with Debit Memo | Perform all steps in the test script. |
| BDH - Sales Order Entry with One-Time Customer | Perform all steps in the test script. |
| BKX - Sales Order Processing – SEPA Direct Debit Handling | Perform all steps in the test script. |
| BKZ - Sales Order Processing with Invoice List and Collective Billing | Perform all steps in the test script. |
| BD3 - Sales Processing using Third-Party with Shipping Notification | Perform all steps in the test script. |
| BDK - Sales Processing Using Third-Party Without Shipping Notification | Perform all steps in the test script. |
| BDN - Sales of Non-Stock Item with Order-Specific Procurement | Perform all steps in the test script. |
| BD9 - Sell from Stock | Perform all steps in the test script. |
| 1BM - Make-to-Order Production – Semifinished Goods Planning and Assembly | Perform all steps in the test script. |
| 1YT - Make-to-Order Production with Variant Configuration | Perform all steps in the test script. |

|  |
| --- |
| Note Predictive Accounting for Sales Orders (2FD) has to be activated to enable travel request simulation. If you want to see commitment reports, Project Control – Finance (1NT) and/or Overhead Cost Accounting (J54) have to be scoped. |

|  |
| --- |
| Note The following item categories are covered for this scope: TAQ, TANN, TAN, LAN, L2W, L2N, GAN2, G2W, G2N, CBXN, CBTC, CBTA, CBNF, CBLN, CBEN, CBAO, CBAB, CB4, CB3, CB2, CB10, CB1, TAD, CBTD, and CTAD. If any of this item category is missing, you can add it via the configuration activity Activate Predictive Accounting for Sales Order Item Categories. |

## Overview Table

The scope item Accounting for Incoming Sales Orders consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report or Item | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Sales Accounting Overview](#unique_8) [page ] 7 | Cost Accountant - Sales | Sales Accounting Overview (F3228) | The cards on the screen are updated with the data for the given selection criteria. |
| [Review Incoming Sales Orders Report](#unique_9) [page ] 8 | Cost Accountant - Sales | Incoming Sales Orders - Predictive Accounting (F2964) | All incoming sales orders for the selected period are displayed. |
| [Gross Margin Presumed/Actual](#unique_10) [page ] 9 | Cost Accountant - Sales | Gross Margin - Presumed/Actual (F3417) | The application retrieves the financial data for the chose filters. Additional key figures can be displayed by selecting the Settings button. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Sales Accounting Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This application displays key KPIs that are important in the area of Sales Accounting. The available data include Incoming Sales orders - Selected Period, Incoming Sales orders - Previous 6 Periods, Revenue Variance, Sales Revenue Benchmark - Top 5 by Amount, Monthly Sales Revenue - Fiscal Year to Period, and Sales Volume Per Material - Top 10 by Difference. Quick Links to other relevant applications also are available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2. | Access the SAP Fiori app | Open Sales Accounting Overview (F3228). | The Sales Accounting Overview (F3228) screen displays |  |
| 3. | Adapt Filters | Make the following entries and choose Go:Company Code:3310Display Currency:AEDPlanning Category : PLNFiscal Year Period : <enter any period and the current year>Statement Version: YPS2Note If the filter option is not available, select Adapt Filters and use the search feature.Ledger: 0E | The cards on the screen are updated with the data for the given selection criteria. |  |

### Review Incoming Sales Orders Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step utilizes an analytical app that allows you to evaluate incoming sales orders. The app uses predictive postings from the journal entry database. It creates these predictive postings by using data from sales orders and goods issue to simulate the respective invoices. Available view variants include Cost of Sales Split and Sales Deductions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Cost Accountant - Sales. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Incoming Sales Orders - Predictive Accounting (F2964). | The Incoming Sales Orders - Predictive Accounting (F2964) screen displays. |  |
| 3 | Input Criteria | In the Adapt Filters screen, make the following entries and choose OK.Company Code: 3310FSV: YPS2Sales Order Selection: All Incoming OrdersSales Organization: 3310Note Choose the Compact Filter button if fields do not display.Sales Order: <Use one of the orders you've created from running the prerequisite business conditions>Note This field is available under the Pred.Analysis based on Inc. Orders section. |  |  |
| 4 | Execute | Choose Go. | The application displays the results of the search. |  |

### Gross Margin Presumed/Actual

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This report allows a user to compare the presumed margin of sales orders, which is calculated at the time of order entry, against actual margin for any given selection criteria such as by Customer Group.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Gross Margin - Presumed/Actual (F3417). | The Gross Margin - Presumed/Actual (F3417) screen displays. |  |
| 3 | Adapt Filters | In the Adapt Filters screen, make the following entries and choose OK.FSV: YPS2Ledger: 0ESales Organization: 3310Note If the filter option is not available, select Adapt Filters and use the search feature. |  |  |
| 4 | Execute | Choose Go. | The application retrieves the financial data for the chosen filters. To display additional key figures, choose the Settings button. |  |

## Appendix

### Using Situation Template (Optional)

Purpose

This template is used for situation handling that informs specific users when the percentage of successfully processed source documents included in predictive accounting falls below a defined threshold. You want the sales accountants in your company to be informed automatically when the percentage of successfully simulated data in predictive accounting falls below a defined threshold. The sales accountants can use the Monitor Predictive Accounting - Predictive Quality app to navigate to the individual errors, and can then inform other users to correct errors, for example, in configuration settings. For information on the Situation Template for Predictive Accounting, see [https://help.sap.com/viewer/bd39d476d1e34b48afed98759286efd6/LATEST/en-US/0f2a694e8ed740a4947eb7c404c23ea5.html](https://help.sap.com/viewer/bd39d476d1e34b48afed98759286efd6/LATEST/en-US/0f2a694e8ed740a4947eb7c404c23ea5.html). In this example the user, Sales Accountant, will receive a notification (icon located in the upper right side the window) when the situation triggers the execution of the Predictive Quality report when sales order prediction success percentage falls below 70%.

|  |
| --- |
| Note This requires the configuration expert role for business processes. |

For additional information on situation handling, see the generic setup documentation for object-based Situation Type [https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/19460b5cabb746b0b5198fc82f14335a.html](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/19460b5cabb746b0b5198fc82f14335a.html).

|  |
| --- |
| Note Though you may be able to set up the alerts, there is no error test data provided and therefore notification may not be triggered during testing. |

Prerequisite

Ensure that Situation Handling (31N) scope item is installed before you execute this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Situation Types (F2947) . | The Manage Situation Types view displays. |  |
| 3 | Copy the Situation Template | In the Search field, enter FIN_PRDTVACCTGSUCCESSRATEWARNINGand choose Go.Select the checkbox for the row FIN_PRDTVACCTGSUCCESSRATEWARNING, and theen choose Copy. | A New Situation Type view displays. |  |
| 4 | Maintain Admin Information | Make the following entries and choose Create (accept all warning and enable messages):ID: <enter your template name>Name: <enter your template description>Conditions:Send Notification: <selected>Predictive Accounting Success Rate: <70Batch Job Scheduling:Time Zone: CETStart Batch Job At: 05:00Situation Monitoring:Monitor Instances: <selected> | The initial situation type for Predictive Accounting success rate with specific threshold of below 70% is created. |  |

Setting up Responsibilities

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Teams and Responsibilities.Select any Manage Teams and Responsibilities app, and remove any preset category filters.In Category, enter FIPRA and choose Go.If no results exist, go the next step to create a new team. | The Manage Teams and Responsibilities view displays. |  |
| 3 | Manage Teams and Responsibilites | Choose Create.Make the following entries and choose Create (accept all warning and enable messages):Name: <Team Name>Global ID: <Global ID name>Type: Finance Predictive Accounting (SFIPRA)Team OwnerBusiness Partner: <BPC expert ID>Team MembersBusiness Partner: <Sales Accountant user ID>Note To find the sales accountant user ID, use the search function with:First name: JohnLast name: SalesAccountant | A New Situation Type view displays. |  |

Finishing up the Situation Type

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Situation Types (F2947) . | The Manage Situation Types view displays. |  |
| 3 | Assign Responsibility to the Template | Select Situation Types and using the filter function enter the situation type name you created in the previous step and choose Go.Select the situation type and choose the > sign on the right of the page.In the Recipients section, under Responsibility by Teams, choose Add Team Category, make the following entries and choose Save:ID: <FIPRA>Filter by Member Function: <Monitor Predictive Accounting> |  |  |
| 4 | Manual Trigger of the Situation Type | Open Manage Situation Types (F2947) app. Select Situation Types and using the search function, enter the situation type name you created in the previous step and choose Go.Select your situation type, choose the > sign on the right of the page and choose Trigger Now. | If you log in a separate session as Sales Accountant, if Predictive Accounting Success Rate is under 70%, you should see the notification under the notification icon. |  |
| 5 | Deactivate the Situation Type | Go back to the Manage Situation Types (F2947) app. Select Situation Types and using the search function, enter the situation type name you created in the previous step and choose Go.Select your situation Type and choose Disable. | After receiving a notification, you can disable the template to avoid performance issues on the test systems. |  |

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
- related-to :: [[06-management-accounting/predictive-accounting-for-service-contract-management-4v7-ae-test-scri]]
- related-to :: [[06-management-accounting/predictive-accounting-for-travel-and-expense-management-4q0-ae-1042]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2FD_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 22,693 chars in the whole document
