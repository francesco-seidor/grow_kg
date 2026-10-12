---
id: 03-financial-accounting-and-close/test-script-fund-accounting-7au-sap-s-4hana-cloud-public-edition-1206
title: "Test Script: Fund Accounting (7AU) - SAP S/4HANA Cloud Public Edition (7AU_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 7AU Fund Accounting: FSV configuration, semantic tags, financial positions, 0DFLT constant, Funds Overview app."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/public-sector-fund-accounting]
aliases: [7AU_S4CLD2608_BPD_EN_XX]
keywords: [Fund Accounting and Public Sector Setup, fund accounting, funds overview, financial statement versions, global hierarchies, semantic tags, financial positions, unassigned processes constant, business roles, test scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7AU_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1206
topic: 03-financial-accounting-and-close/public-sector-fund-accounting
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Fund Accounting (7AU) - SAP S/4HANA Cloud Public Edition (7AU_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7AU_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Fund Accounting and Public Sector Setup** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Fund Accounting (7AU) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232827635)

[2 Prerequisites 3](#_Toc232827636)

[2.1 System Access 3](#_Toc232827637)

[2.2 Roles 3](#_Toc232827638)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232827639)

[2.4 Business Conditions 4](#_Toc232827640)

[2.5 Preliminary Steps 5](#_Toc232827641)

[2.5.1 Relevant Configuration Steps for Fund Overview 5](#_Toc232827642)

[2.5.1.1 Define Financial Statement Version 5](#_Toc232827643)

[2.5.1.2 Migrate Financial Statement Versions to Global Hierarchies 7](#_Toc232827644)

[2.5.1.3 Assign Semantic Tag to Financial Statement Version Item 8](#_Toc232827645)

[2.5.1.4 Define Financial Positions (Optional) 10](#_Toc232827646)

[2.5.2 Relevant Configuration Steps for Unassigned Processes using Constant 0DFLT 13](#_Toc232827647)

[3 Overview Table 15](#_Toc232827648)

[4 Test Procedures 16](#_Toc232827649)

[4.1 Funds Overview 16](#_Toc232827650)

## Purpose

Overview

With this scope item, you can perform SAP Analytical Cloud reporting for Fund accounting.

Fund accounting involves recording, summarizing, reporting, analyzing, and interpreting the financial transactions of governments or non-profit organizations. It uses fiscal and accounting entities, such as a fund with a self-balancing set of accounts.

You can use this scope item to perform SAP Analytics Cloud reporting for Fund Accounting.

Fund accounting is the act of recording, summarizing, reporting, analyzing, and interpreting the financial transactions of governments or non-profit organizations by using fiscal and accounting entities, such as a fund with a self-balancing set of accounts.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| General Ledger Accountant - Public Sector | SAP_BR_GL_ACCOUNTANT_PSM | General Ledger - Fund Accounting |  |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |
| Treasury Risk Manager | SAP_BR_TREASURY_RISK_MANAGER | Treasury Analytics | SAP_BR_TREASURY_RISK_MANAGER |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 1710 |  | Replace 1710 with your company code ‘xxxx’ |
| Chart of Accounts | YCOA |  |  |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

Invoices to be paid must be available.

| Scope Item ID | Business Condition |
| --- | --- |
| 6YU - Government Budget Management | Master data must be available |
| J58 - Accounting and Financial Close | Journal entries have been posted |
| J60 - Accounts Payable | Invoices have been created |
| 1WV - Debt and Investment Management | Debt and investment contracts posted to the general ledger (optional) |

### Preliminary Steps

#### Relevant Configuration Steps for Fund Overview

##### Define Financial Statement Version

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you manage the financial statement version.

If you log onto the Q system as a general ledger accountant, you can use the Manage Financial Statement Versions (OB58) app to make changes to the financial statement version data. If you use this app, execute the steps in the table below, starting with step 3. In the P system, you can only display financial statement version data.

Caution If Q2P is turned off, the SSCUI is still available in the Manage Your Solution (F1241) app, but remains in the display mode.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: General Ledger

1. In the row with the item name of the Chart of Accounts, choose Details (>).
2. In the Define Financial Statement Versions row, choose Configure.
3. Continue with the procedure in the table below.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app.
3. You can search for the configuration activity Define Financial Statement Versions and navigate directly to the SAP S/4HANA Cloud Public Edition system.
4. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select Financial Statement Version | Select the following financial statement version for your country and choose Copy As. | The Change View "Financial Statement Versions": Overview view appears. |  |
| 2 | Copy Financial Statement Version | Make the following entries and choose Copy:FS Version: for example, FSV1Name: for example, Financial Statement Version (replace with a name of your country)Chart of Accounts: <for example, YC0A> | The template financial statement version is copied. |  |
| 3 | Select Financial Statement Version | Select the following financial statement version and choose Financial Statement Items.Financial Statement Version Name: FSV1 | The Change Financial Statement Version view appears. |  |
| 4 | Delete Accounts | Expand to the item that needs to be maintained, select the account and choose Delete. | The account is deleted from the financial statement. |  |
| 5 | Save | Save your entries. | The Financial Statement Version: Save & Activate dialog box appears. |  |
| 6 | Replicate FSV Hierarchy | Choose Activate. | The replication of the FSV hierarchy starts. |  |
| 7 | Replicate FSV Hierarchy | Choose Continue. | The FSV hierarchy is replicated. |  |
| 8 | Replicate FSV Hierarchy | Choose Continue. | Data is saved. |  |
| 9 | Assign Accounts | Select the item where the account should be added and choose Assign Accounts.The account cannot be found in multiple items. | The Change Accounts entry view appears. |  |
| 10 | Enter Account | Make the following entries and choose Continue.The account cannot be found in multiple rows.From Acct : <your account>To Acct : <your account>D: SelectedC: Selected | The account is assigned to the financial statement. |  |
| 11 | Save | Save your entries. | The Financial Statement Version: Save & Activate dialog box appears. |  |
| 12 | Replicate FSV Hierarchy | Choose Activate. | The replication of the FSV hierarchy starts. |  |
| 13 | Replicate FSV Hierarchy | Choose Continue. | The FSV hierarchy is replicated. |  |
| 14 | Replicate FSV Hierarchy | Choose Continue. | Data is saved. |  |

##### Migrate Financial Statement Versions to Global Hierarchies

Purpose

During this activity, you migrate financial statement versions (FSVs) to the global hierarchy.

You can also use this app to define FSVs as being not relevant for migration or undo a migration if you encountered an error.

Procedure

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:
6. Application Area: Finance
7. Sub Application Area: General Ledger
8. In the row with the Item Name of Chart of Accounts, choose Details (>).
9. In the Migrate Financial Statement Versions to Global Hierarchies row, choose Configure.
10. Continue with the procedure in the table below.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app.
3. You can search for the configuration activity Migrate Financial Statement Versions to Global Hierarchies and navigate directly to the SAP S/4HANA Cloud Public Edition system.
4. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail /Comment |
| --- | --- | --- | --- | --- |
| 1 | FSV Details | On the Hierarchy Types tab, for the Financial Statement Version hierarchy type, choose Details (>). | The view changes to display the financial statement version and the hierarchy items. |  |
| 2 | Item Details | For one of the items in the Items pane, choose Details(>). | The details for the selected hierarchy item are displayed in a new view. |  |
| 3 | Back | Choose Back. | You return to the previous screen. |  |
| 4 | Show Not Started | Above the list of items in the Items pane, choose Not Started from the dropdown.You can also filter by In Progress, Migrated, or Not Relevant. | The list is filtered to only show the hierarchy items that have not started migration. |  |
| 5 | Migrate FSVs | Select the checkbox for an item and choose Migrate. | A new view is displayed. The item is migrated. The system displays the list of hierarchy items, excluding the one you just migrated. |  |
| 6 | Show Migrated | Above the list of items in the Items pane, choose Migrated from the dropdown. | The item you migrated is shown in the filtered list along with other migrated items.To check this, you can use the Manage Global Hierarchies(F2918) app to search for the hierarchy item you migrated. |  |

##### Assign Semantic Tag to Financial Statement Version Item

Use

In this activity, you assign semantic tags to the financial statement version item. This is required for the key figures for Balances and P+L in the Fund Overview (F6173) app.

Caution This activity is only relevant if your financial statement version has been migrated to global hierarchies.

Procedure

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Global Hierarchies (F2918) and select your financial statement version. | The Define Financial Statement Versions in Global Hierarchies view appears. |  |
| 3 | Change to the Edit Mode | Choose Deactivate and Edit. |  |  |
| 4 | Expand Financial Statement Version to assign Semantic Tag | Select Financial Statement Version Item to Assign Semantic Tag. |  |  |
| 5 | Assign Semantic Tag | Assign the following semantic tags to an appropriate leaf in your version. You can also assign the same semantic tag more than once.CSH_CSHEQV - Cash & Cash EquivalentsFUND_BAL - Fund Balance (this represents your equity)GROSS_REV - Gross RevenuesTOTAL_EXP – Total Expenses | Semantic tags are assigned to the financial statement version item or to the G/L accounts. |  |
| 6 | Save | Choose Save and Activate. | The financial statement version and assignment of the semantic tag has been activated for use. |  |

SAP Central Business Configuration

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app.
3. You can search for the configuration activity Manage Global Accounting Hierarchy and navigate directly to the SAP S/4HANA Cloud Public Edition system.
4. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select Financial Statement Version | Select the financial statement version you created in the previous steps. | The Define Financial Statement Versions in Global Hierarchies view appears. |  |
| 2 | Change to the Edit Mode | Choose Deactivate and Edit. | The Define Financial Statement Versions in Global Hierarchies view appears. |  |
| 3 | Assign Semantic Tag | Assign the following semantic tags to an appropriate leaf in your version. You can also assign the same semantic tag more than once.CSH_CSHEQV - Cash & Cash EquivalentsFUND_BAL - Fund Balance (this represents your equity)GROSS_REV - Gross RevenuesTOTAL_EXP – Total Expenses | Semantic tags are assigned to the financial statement version item or to the G/L accounts. |  |
| 4 | Save | Choose Save and Activate. | The financial statement version and assignment of the semantic tag has been saved and activated for use. |  |

Result

Semantic tags are assigned to the financial statement version item or GL accounts.

##### Define Financial Positions (Optional)

Use

In this activity you define the financial positions that can be used for the Funds Overview and the tab for the Funded Treasury Overview.

Follow the steps as described in Debt and Investment Management (1WV) and other Treasury-related scope items that might be applicable, using the process step Reports > Define Financial Positions .

|  |
| --- |
| Note These steps are only relevant if you are using a Treasury and Risk Management scope item (such as 1WV). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Risk Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Define Financial Positions (FTR_FP_DEF). | The Maintain Financial Position Groups: Change screen displays. |  |
| 3 | Maintain Key Figure Groups | Select New Entries.Enter data for a record of new entry and select Save.Financial Position Group: for example, FPG_MM_A0001Financial Position Group Description: for example, <Short term investments>Assets/Liabilities: for example, Assets The data is saved. | The data is saved. |  |
| 4 | Maintain Key Figures | Switch to Maintain Financial Positions tab.Enter data and choose Save.Financial Position: for example, FP_MM_A0001Financial Position Description: for example, Short term investmentsFinancial Position Group: for example, FPG_MM_A0001Data Source: for example, Treasury and Position Management The data is saved. | The data is saved. |  |
| 5 | Maintain Selections | Select one financial position and select Maintain Selections.Product Type = 51A to 55ATransaction Type = 100 to 199Valuation Class = 20 to 29Valuation Area = <your valuation area>Posting Status = 2Choose Back and choose Save. | The data is saved. |  |
| 6 | Enter More Data | Enter more financial positions data as below tables. |  |  |

| Financial Position Group | Financial Position Group Description | Assets/Liabilities |
| --- | --- | --- |
| FPG_MM_A0001 | Short term investments | Assets |
| FPG_MM_A0002 | Long term investments and other assets | Assets |
| FPG_MM_L0001 | Short term debt | Liabilities |
| FPG_MM_L0002 | Long term debt and other liabilities | Liabilities |
| FPG_BD_A0002 | Bond investment | Assets |
| FPG_BD_L0001 | Bond issuance | Liabilities |

| Financial Position | Financial Position Description | Financial Position Group | Data Source | Maintain Selection |
| --- | --- | --- | --- | --- |
| FP_MM_A0001 | Short term investments | FPG_MM_A0001 | Treasury position management | Product type = 51A to 55ATransaction type = 100 to 199Valuation class = 20 to 29Valuation area = <your valuation area>Posting status = 2 |
| FP_MM_A0003 | Long term investments | FPG_MM_A0002 | Treasury position man-agement | Product type = 51A to 55ATransaction type = 100 to 199Valuation class = 10 to 19Valuation area = <your valuation area>Posting status = 2 |
| FP_MM_L0001 | Short term debt | FPG_MM_L0001 | Treasury position management | Product type = 51A to 55ATransaction type = 200 to 299Valuation class = 20 to 29Valuation area = <your valuation area>Posting status = 2 |
| FP_MM_L0002 | Long term debt | FPG_MM_L0002 | Treasury position management | Product type = 51A to 55ATransaction type = 200 to 299Valuation class = 10 to 19Valuation area = <your valuation area>Posting status = 2 |
| FP_BD_A0002 | Bond investment | FPG_BD_A0001 | Treasury position management | Product type = 04AValuation class = 10 to 15 and 20 to 25Valuation area =<your valuation area>Posting status = 2 |
| FP_BD_L0001 | Bond issuance | FPG_BD_L0001 | Treasury position management | Product type = 04AValuation class = 15 to 20 and 25 to 30Valuation area = <your valuation area>Posting atatus = 2 |

#### Relevant Configuration Steps for Unassigned Processes using Constant 0DFLT

Purpose

If non-budgetary lines are entered in a journal entry and the user (or interface) doesn't supply any account assignments, a constant (0DFLT) can be invoked for those lines.

Procedure - Edit Constant for Nonassigned Processes

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: General Ledger

1. For the row with Item Name of Document Splitting, choose Details (>).
2. For the Edit Constant for Nonassigned Processes row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Edit Constant for Nonassigned Processes.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Constant | Select the checkbox for the constant 0DFLT and choose Assignment of Values. | The Change View "Edit Constants for Nonassigned Processes": Details view is displayed. |  |
| 2 | Fields | Make the following new entries and choose Save:Segment: for example, 1000_CFund: for example, G1100Grant: for example, NRG | The default account assignments are maintained. |  |

Procedure - Edit Constant for Expense or Revenue Account

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Public Sector

Sub Application Area: Fund Accounting

1. For the row with Item Name of Fund Accounting, choose Details (>).
2. For the Edit Constant for Expense or Revenue Account row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Edit Constant for Expense or Revenue Account.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Constant | Verify or maintain the following:Constant: 0DFLTChart of Accounts: YCOAEx/Rev A/c: 8009000 |  |  |

## Overview Table

This scope item consists of several process steps.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Funds Overview](#unique_12) [page ] 16 |  | Fund Overview (F6173) | The charts are refreshed with the data selected. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Funds Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The funds overview includes analytic tabs from different perspectives for the G/L Accountant Public Sector user.

The following tab is available with the funds overview

| Tab# | Tab Name |
| --- | --- |
| 1 | Balances |
| 2 | P&L |
| 3 | Assets |
| 4 | Treasury |

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant - Public Sector.. |  |  |
| 2. | Access the SAP Fiori App | Open Funds Overview - Funds Overview KPIs (F6173). | The tab Fund Overview (F6173) appears. In the story, the Balances tab is displayed by default. |  |
| 3. | Switch Between Pages | Click between the pages Balances, P&L, Assets, Treasury | The charts are refreshed with the additional pages and data is displayed for each of them. |  |

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
- related-to :: [[03-financial-accounting-and-close/psm-preparation-guide-254]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7AU_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 28,824 chars in the whole document
