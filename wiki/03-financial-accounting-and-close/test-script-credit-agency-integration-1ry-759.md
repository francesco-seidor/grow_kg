---
id: 03-financial-accounting-and-close/test-script-credit-agency-integration-1ry-759
title: "Test Script: Credit Agency Integration (1RY) (1RY_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 1RY: importing external credit agency reports and viewing the updated credit profile."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/credit-management]
aliases: [1RY_S4CLD2608_BPD_EN_XX]
keywords: [Credit Management and Credit Agency Integration, credit agency integration, external credit reports, credit management jobs, credit profile, credit controller role, advanced credit management, business partner credit role, test scripts, business catalogs]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1RY_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-759
topic: 03-financial-accounting-and-close/credit-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Credit Agency Integration (1RY) (1RY_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1RY_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Credit Management and Credit Agency Integration** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Credit Agency Integration (1RY) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232880729)

[2 Prerequisites 3](#_Toc232880730)

[2.1 Additional Manual Configuration 3](#_Toc232880731)

[2.2 System Access 3](#_Toc232880732)

[2.3 Roles 3](#_Toc232880733)

[2.4 Master Data, Organizational Data, and Other Data 4](#_Toc232880734)

[2.5 Business Conditions 4](#_Toc232880735)

[3 Overview Table 5](#_Toc232880736)

[4 Test Procedures 6](#_Toc232880737)

[4.1 Schedule Credit Management Jobs 6](#_Toc232880738)

[4.2 Access External Credit Reports 7](#_Toc232880739)

[4.3 Acquire External Credit Report 8](#_Toc232880740)

[4.3.1 Search for Business Partner ID in Credit Agency Database 8](#_Toc232880741)

[4.3.2 Assign ID to Business Partner and Import Credit Report 9](#_Toc232880742)

[4.4 View Updated Credit Profile 10](#_Toc232880743)

[5 Appendix 12](#_Toc232880744)

[5.1 Process Integration 12](#_Toc232880745)

[5.1.1 Preceding Processes 12](#_Toc232880746)

## Purpose

Overview

This scope item connects to various third-party credit agencies. External credit information can be imported automatically into your SAP S/4HANA Cloud system, assisting you in making better credit decisions.

For additional information, see the user guide for [SAP S/4HANA Finance Cloud for Credit Integration](https://help.sap.com/docs/SAP_S4HANA_FINANCE_CLOUD_FOR_CREDIT_INTEGRATION/59309636eb7f46688cbe3ccaadace5ab/1576da61c5b145dba73c7a4f2079ea77.html).

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/9d912e7717b71f1927e3f9980f21148f)

### System Access

The test should be conducted with the following system:

| System | Details |
| --- | --- |
| SAP S/4HANA Fiori launchpad | Accessible via the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Credit Controller | SAP_BR_CREDIT_CONTROLLER | Credit Management | SAP_BR_CREDIT_CONTROLLER |  |

|  |
| --- |
| Caution To ensure that the required apps are visible on your SAP Fiori launchpad, add the following business catalogs to your Credit Controller role:Credit Management - External Credit Information (SAP_FIN_BC_CR_CAI_PC)Credit Management - Configuration of External Credit Information Providers (SAP_FIN_BC_CR_CAI_CONF_PC)For more information, see the [Assign Business Catalogs](https://help.sap.com/docs/SAP_S4HANA_FINANCE_CLOUD_FOR_CREDIT_INTEGRATION/8a4f4cf501494f9bbf2c5d5df913f950/8af282c564d9498baddc075e0e59200e.html?version=FOUNDRY) topic on the SAP Help Portal. |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company is created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices Baseline Package, you can use the following Baseline Package scenario data:

| Master Data | Value | Details | Comments |
| --- | --- | --- | --- |
| Customer | For example, 17100011 |  |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 1QM - Advanced Credit Management | Complete the steps described in the Advanced Credit Management (1QM) scope item. 1QM requires a separate license. |

## Overview Table

The scope item Credit Agency Integration consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/ App | Expected Results |
| --- | --- | --- | --- |
| [Schedule Credit Management Jobs](#unique_9) [page ] 6 | Credit Controller | Schedule Credit Management Jobs (F3748) |  |
| [Access External Credit Reports](#unique_10) [page ] 7 | Credit Controller | Manage Credit Accounts (F4596) | Access existing external credit reports on HCP the app. |
| [Search for Business Partner ID in Credit Agency Database](#unique_11) [page ] 8 | (customer using supplied credentials) | Manage Credit Reports for Business Partner in BTP | The credit report is imported into SAP S/4HANA Cloud Public Edition. |
| [Assign ID to Business Partner and Import Credit Report](#unique_12) [page ] 9 | Credit Controller | Manage Credit Accounts (F4596) | Business partner's ID assigned. Credit reports imported. |
| [View Updated Credit Profile](#unique_13) [page ] 10 | Credit Controller | Manage Credit Accounts (F4596) | The credit controller views the updated credit profile. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Schedule Credit Management Jobs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule the credit management jobs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Credit Management Jobs (F3748). |  |  |
| 3 | Create Job | Choose Create. | The New Job view is displayed. |  |
| 4 | Enter Job Template | General Information section:Job Template: Update External Credit InformationJob Name: Update External Credit InformationChoose Step 2 | The Update External Credit Information screen displays. |  |
| 5 | Enter Scheduling | After making the following entries and choose Schedule:Scheduling Options section:Start Immediately: SelectedRecurrence Pattern: Single RunNote Step 3, Parameters is optional. |  |  |

### Access External Credit Reports

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you access existing external credit reports on the SAP Business Technology Platform app for a business partner you choose.

Prerequisite:

The business partner for which you want to access credit reports in the Manage Credit Reports for Business Partner app on SAP Business Technology Platform must fulfill the following criteria:

- The business partner must be of type Organization.
- The SAP Credit Management role must be available for the business partner.

|  |
| --- |
| Note If the role isn’t available for the business partner, in the Maintain Business Partner (BP) app, choose Switch Between Display and Change (F6) to enter edit mode, then select the BP role SAP Credit Management. Alternatively, you can use the Assign Credit Management Role to Business Partners job template in the Schedule Credit Management Jobs (F3748) app. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Credit Accounts (F4596). |  |  |
| 3 | Select Customer | Make the following entries and choose Go:Business Partner: <customer>, for example, 10100011 | The Manage Credit Accounts - Credit Profile view is displayed. |  |
| 4 | Edit | Choose Details > Edit. |  |  |
| 5 | Scoring | Choose the Scoring tab. |  |  |
| 6 | Choose Calculation Rule | Enter or review the following information:Calculation Rule: SAP_ALL - All External Agencies & Int. Scoring & Limit rule |  |  |
| 7 | Save | Save your entries. |  |  |
| 8 | Manage Credit Reports on SAP BTP App | Choose Manage Ext. Credit Information. If a dialog box is displayed, choose Allow. | The Manage External Credit Information for Business Partner app on the SAP Business Technology Platform is displayed in your browser. Because this is a new customer, no credit reports are available. |  |

### Acquire External Credit Report

In this step, you can import a credit report for your business partner. The step is divided into two substeps.

#### Search for Business Partner ID in Credit Agency Database

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you search for the business partner’s ID in the credit agency database.

For detailed instructions, see the Find Business Partner section in the SAP Business Technology Platform (BTP) user guide. To navigate to this user guide, go to the [SAP Help Portal](https://help.sap.com/viewer/index), enter SAP S/4HANA Finance Cloud for Credit Integration. Choose the link in the Product Pages area and choose User Guide. The information should be under App Descriptions > Apps for Credit Controllers in the user guide.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Search for Business Partner in Credit Agency's Database | On the SAP Business Technology Platform, in the Manage External Credit Information for Business Partner app, choose Find Company ID in the top-right corner of the screen. |  |  |
| 2 | Choose External Credit Agency | In the drop-down list of credit agencies, choose an external credit agency and a country/region. | Matching search results of business partner are shown. |  |
| 3 | Choose Matching Search Result | Choose the business partner. | The selected entry is highlighted. |  |

#### Assign ID to Business Partner and Import Credit Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you assign a business partner’s ID that was found in the database of the credit agency to a business partner, and you import the credit reports from the credit agency. Optionally, you can also display the report in PDF format.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Credit Accounts (F4596). |  |  |
| 3 | Select Customer | Make the following entries and choose Go:Business Partner: <customer> | The Manage Credit Accounts - Credit Profile view is displayed. |  |
| 4 | Choose Business Partner Details | Choose Details > for your Business Partner. |  |  |
| 5 | Manage Credit Reports on SAP BTP App | Go to the External Ratings section and choose Manage External Credit Information.If a dialog box displays, make your selection to Save, Keep Draft or Discard Draft and choose OK. If authentication is required, enter your authentication information. | The Manage External Credit Information app opens. |  |
| 6 | Find Business Partner | Choose Find Company ID. | The Find Business Partner app opens. |  |
| 7 | Make Selection | Make the following entries and choose Go:Country/Region of Business Partner: for example, <country code>/<customer ID>Credit Agency |  |  |
| 8 | Assign and Order | Select the right entry in the list of results and choose Assign ID and Order Product.In the dialog box, select your credit products and choose Order. |  |  |

### View Updated Credit Profile

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you access the business partner in SAP S/4HANA Cloud Public Edition and view the updated credit profile, which includes the credit rating, risk class, recalculated credit limit, and the imported credit report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Credit Accounts (F4596). |  |  |
| 2 | Select Customer | Make the following entries and choose Go:Business Partner: <customer>, for example, 10100011 |  |  |
| 3 | Edit | Choose Edit. |  |  |
| 4 | Scoring | Choose the Scoring tab. |  |  |
| 5 | Check Updated External Credit Information | In the External Ratings area, view the External Credit Information section. | There should be entries in this section that show rating and other information. |  |
| 6 | Check Updates in Scoring | View the Scoring section of the screen. | Updated risk class score can be viewed. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can proceed this process:

| Process | Business Condition |
| --- | --- |
| 1QM - Advanced Credit Management |  |

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
- related-to :: [[03-financial-accounting-and-close/advanced-credit-management-1qm-ae-test-script-sap-s-4hana-cloud-public]]
- related-to :: [[03-financial-accounting-and-close/test-script-basic-credit-management-bd6-ae-sap-s-4hana-cloud-public-ed]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1RY_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 18,928 chars in the whole document
