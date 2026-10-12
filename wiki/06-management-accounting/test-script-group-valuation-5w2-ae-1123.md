---
id: 06-management-accounting/test-script-group-valuation-5w2-ae-1123
title: "Test Script: Group Valuation (5W2_AE) (5W2_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 5W2 Group Valuation: prerequisites, configuration, costing run, cost estimates, actual costing for ledger 4G."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/group-valuation]
aliases: [5W2_S4CLD2608_BPD_EN_AE]
keywords: [Group Valuation, costing run, execute costing run, material cost estimates, group valuation ledger, actual costing, costing variants, intercompany clearing, intercompany sales, scope item activation]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5W2_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1123
topic: 06-management-accounting/group-valuation
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Group Valuation (5W2_AE) (5W2_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5W2_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Group Valuation** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Group Valuation (5W2_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232857045)

[2 Prerequisites 3](#_Toc232857046)

[2.1 System Access 3](#_Toc232857047)

[2.2 Roles 3](#_Toc232857048)

[2.3 Business Conditions 3](#_Toc232857049)

[2.4 Preliminary Steps 4](#_Toc232857050)

[2.4.1 Assign Accounting Principle to the Group Valuation Ledger 4](#_Toc232857051)

[2.4.2 Product Cost Planning Configuration for Group Valuation 5](#_Toc232857052)

[2.4.3 Optional: Update Group Costing Variant with Reference Variant 5](#_Toc232857053)

[2.4.4 Mandatory: Configure Clearing Between Company Codes 6](#_Toc232857054)

[3 Overview Table 8](#_Toc232857055)

[4 Test Procedures 9](#_Toc232857056)

[4.1 Create Costing Run 9](#_Toc232857057)

[4.2 Execute Costing Run 10](#_Toc232857058)

[4.3 Manage Material Cost Estimates 12](#_Toc232857059)

[4.4 Intercompany Sales and Stock Transfer Process 13](#_Toc232857060)

[4.5 Actual Costing for Group Ledger 13](#_Toc232857061)

## Purpose

Overview

This scope item activates an additional ledger to store a consolidated view of intercompany business transactions. These transactions occur in line with the Advanced Intercompany Sales (5D2) and Advanced Intercompany Stock Transfer (5HP) scope items. It extends the Standard Cost Calculation (BEG) scope item to support standard cost calculations across different plants and company codes. It also delivers a consolidated view of standard costs and actual costing, as detailed in the Actual Costing (33Q) scope item, to provide a comprehensive view of actual costs across the value chain.

This scope item must be activated during the scoping phase of the initial implementation project if it’s required for customer business today or in the future.

You can't activate this scope item beyond the first scope activation in subsequent implementations due to data logic.

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
| System | Accessible via SAP Analytics Cloud. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Assign the following roles to your individual test users.

|  |
| --- |
| Note These roles are examples provided by SAP. You can use them as templates to create your own roles.For more information about roles, refer to Assigning Roles to Users and Teams in the [SAP Analytics Cloud Help](https://help.sap.com/doc/00f68c2e08b941f081002fd3691d86a7/2020.15/en-US/dbcf41a0ac6d472b99fc3634a5eed600.html). |

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Cost Accountant - Inventory | SAP_BR_INVENTORY_ACCOUNTANT | Inventory Accounting | SAP_BR_INVENTORY_ACCOUNTANT |  |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |

### Business Conditions

|  |
| --- |
| Caution This scope item can be activated only during initial scoping or when adding a new country, but not via scope extension, hence it is important to know whether this scope is required at the outset.The following supported scope items can be activated at a later point via scope extension. |

| Scope Item | Business Condition |
| --- | --- |
| 5D2 - Advanced Intercompany Sales | Required for business reasons |
| 5HP - Advanced Intercompany Stock Transfer | Required for business reasons |

|  |
| --- |
| Note To activate and use this scope item, make sure that none of the following scope items are active/selected. Check SAP note [3093830](https://me.sap.com/notes/3093830) for the latest information on incompatible scope items.Classic Intercompany Stock Transfer Scope Items:1P9 - Intercompany Stock Transfer2TS - Intercompany Stock Transfer Returns1HO - Intercompany Sales Order Processing – Domestic1MX - Intercompany Sales Order Processing – International1WO - Extended Intercompany Processes for Sales2F4 - Intercompany Process for Customer Returns |

### Preliminary Steps

#### Assign Accounting Principle to the Group Valuation Ledger

Purpose

This activity lets you assign accounting principle to the group valuation ledger. This is a mandatory step as for group valuation, the standard ledger 4G is predelivered without any accounting principle.

Procedure

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Assign Accounting Principles to Ledgers and Company Codes activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Assign accounting principle to ledger 4G/company codes.

#### Product Cost Planning Configuration for Group Valuation

Purpose

This activity lets you update the product costing-related setting for group valuation.

Procedure

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following:
    - Define Costing Sheets
    - Define Valuation Variants per Plant
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Provide valuation variant 4GL for group cost estimate, and create your own costing sheet and assign, if required.
6. For sales order group, cost estimate the valuation variant SGR that can be updated as per your business requirement.

#### Optional: Update Group Costing Variant with Reference Variant

Purpose

This step is required if you have to use the same quantity structure for group valuation as legal valuation. This is only possible with the functionality of reference calculation. Predelivered reference variants are provided.

|  |
| --- |
| Note Execution of the legal costing is a prerequisite for the group costing with reference calculation. |

Based on the costing variant used for legal costing, the following reference costing variants are available for group costing variant 4GL1.

Table 1:

| Group Costing Variant | Reference Costing Variant |
| --- | --- |
| 4GL1 | 10-PYC1 Cost Estimate Standard |
| 4GL1 | 11-PPC1 Standard Cost Est (Mat) |
| 4GL1 | 12-PYC2 Cost Estimate Plan |
| 4GL1 | 13-P00L Legal Mat Cst Est Ldgr-0L |
| 4GL1 | 14-P02L Legal Mat Cst Est Ldgr-2L |
| 4GL1 | 15-P03L Legal Mat Cst Est Ldgr-3L |

Procedure

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Define Costing Variants activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Update costing variant 4GL1 with required reference costing variant (see table above).

#### Mandatory: Configure Clearing Between Company Codes

Purpose

This configuration is required when posting cross-company code transactions between two company codes.

Procedure

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Automatic Account Determination activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Select the following and choose Step 2:
    - Area: Financial Accounting
    - Subarea: General Ledger Accounting
    - Process: Define Clearing Account for Multiple Valuation
6. In the Posted in company code dialog box, enter 3310 and choose Step 3.
7. In the Display View "Acct determination for charging off valuati..": Overview, choose Change to maintain the settings for company code, and trading partners associated with the company code.

|  |
| --- |
| Note Use GL 97777600-ICO - Group Valuation Clearing Account for mapping, which is created specifically for this scope. |

1. Choose Review and save the entries.
2. Confirm the dialog boxes, if any.

## Overview Table

This scope item consists of several process steps as provided in the table below:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Costing Run](#unique_11) [page ] 9 | Cost Accountant - Inventory | Manage Costing Runs - Estimated Costs (F1865) | The Manage Costing Runs Estimated Costs view displays, and costing run is created for group estimate. |
| [Execute Costing Run](#unique_12) [page ] 10 | Cost Accountant - Inventory | Manage Costing Runs - Estimated Costs (F1865) | The Manage Costing Runs Estimated Costs view displays and costing run is created for group leadger 4L. |
| [Manage Material Cost Estimates](#unique_13) [page ] 12 | Cost Accountant - Inventory | Manage Material Cost Estimates (F7650) | This activity lists material cost estimates across all costing variants. |
| [Intercompany Sales and Stock Transfer Process](#unique_14) [page ] 13 |  | Follow the test procedures in Advanced Intercompany Sales (5D2) and Advanced Intercompany Stock Transfer (5HP) to review the effects of group valuation, where intercompany profits between trading partners are eliminated in real time. |  |
| [Actual Costing for Group Ledger](#unique_15) [page ] 13 | Cost Accountant - Inventory | Edit Actual Costing Runs (CKMLCP) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Costing Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you create a costing run.

| Costing Type | Ledger | Costing Variant | Valuation Variant | Costing Sheet | Impact |
| --- | --- | --- | --- | --- | --- |
| 4G | 4G - Group Valuation | 4GL1 - Group Valuation | 4GL | Blank - you can create own costing sheet and assign | Updates Ledger 4G only |
| 4G | 4G - Group Valuation for sales order | PB4G - Group SO Cost Est Ldgr-4G | SGR | Blank - you can create own costing sheet and assign | Updates Ledger 4G only for sales order costing |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Costing Runs - Estimated Costs (F1865). | The Manage Costing Runs Estimated Costs view displays. |  |
| 3 | Creating Costing Run | Choose the Create button. | The Create New Costing Run view displays. |  |
| 4 | Enter Parameters for Costing Run | Make the following entries and choose Enter.Costing Run: Test1Costing Run Date: <Enter the current date>Description: Costing Run Test1Costing Variant: 4GL1Note Ledger is updated based on costing type mapped to costing variant. Select appropriate for group ledger.Costing Version: 1Controlling Area: A000Company Code: 3310Costing Date From: <Enter the current date>Costing Date To: <Adopt the default value>Qty Structure Date: <Enter the current date>Valuation Date: <Enter the current date> |  |  |
| 5 | Save Costing Run | Choose the Save button. |  |  |

### Execute Costing Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you execute the costing run. Configured materials are not included.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Costing Runs - Estimated Costs (F1865). | The Manage Costing Runs Estimated Costs view displays. |  |
| 3 | Select Costing Run | Search for the costing run created in the previous step.Select the costing run and choose Edit. | The Edit Costing Run view displays. |  |
| 4 | Edit Costing Run | Make the desired changes and choose Continue. Save the changes as required. |  |  |
| 5 | Create Cost Estimates | Choose the Processing icon to open the Process section. On the Flow Step row selection, choose the Parameters icon. In the Create Cost Estimate table, for each row, there is a Change Parameterbutton in the Parameters column. Choose the one in the selection row and make the following entries:Material Type : HALB, ROH, FERTPlant: 3310Select option Explode Multilevel Structure.Deselect Background Processing indicator and then choose Save.Choose Back and save the entries as required.Choose Execute, which displays in the Execute column, and the status light for the Selection row turns green. | The selection is executed. |  |
| 6 | Create Cost Estimates - Selection | For the Costing row, choose the Change Parameter button. On the Costing Run: Cost Estimate – Change Parameters, deselect Background Processing indicator and then choose Save.Choose Back.Choose Execute, which displays in the Execute column and the status light for the Costing row turns green. | Costing Run is executed. |  |
| 7 | Create Cost Estimates - Costing | From the menu, choose Edit > Costing Results.If the status light for this row is red, review the Costing levels report. Correct errors in the report. To re-run the costing (if necessary), repeat steps for Struct. Explosion and Costing Rows. | Costing Run is executed. |  |
| 8 | Create Cost Estimates - Analysis | On the Analysis row, choose the Change Parameter button. Select SAP&11 for the parameter setting and then select Choose. On the Costing Run: Analysis – Change Parameters, deselect Background Processing indicator and then choose Save.Choose Back.Choose Execute, which displays in the Execute column. | Costing Run is executed. |  |
| 9 | Create Cost Estimates - Marking | On the Marking row, choose the Lock button.Note The allowance must be set for the period for which the price update is scheduled.On the Price Update: Organizational Measure screen, select the 3310 row.In the dialog box that appears, choose the Issue marking allowance button. Enter the costing variant of PYC1 and the costing version of 1, and then choose Issue allowance for marking. The status light of the row turns green.Choose Back.Choose Change Parameter and deselect Test Run and Background Processing.Choose Save.Choose Back, and choose Execute. | Costing Run is executed.Note Check the log and resolve error messages. Warning messages may also be potential problems later on in the process, so those need to be resolved as well.The following is an excerpt of potential messages:The messages Costing error for material SGPI*1 to 10: no BOM and routing and Costing error for material FG_FL*0 to FG_FL*2 : no BOM and routing are ok. These materials are sample master data for additional processes. |  |
| 10 | Create Cost Estimates - Release | On the Release row, choose Change Parameter and deselect Test Run and Background Processing.Choose Save.Choose Back, and choose Execute.Note The new standard price cannot be updated before the first day of the validity of the costing run. For example, if costing run is valid from 01/01/<planning year>, then releasing the standard price is possible on 01/01/<planning year> at the earliest. | The current prices will be updated in the material master data. |  |

### Manage Material Cost Estimates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

This activity lists material cost estimates across all costing variants. Without switching between local and group currencies, you can display all currencies as separate columns. It also enables navigation to view the cost estimate for an individual material and allows you to create a material cost estimate.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Material Cost Estimates (F7650). | The Manage Material Cost Estimates view displays. |  |
| 3 | Execute Report | Make the following entries and choose GoMaterial: <for example, FG126>Plant: 3310Costing Variant: PYC1Costing Status: <leave the field blank>Note The material must have a valid costing run executed for the costing variant. | The screen displays an itemization breakdown of product costs. You can switch to Display mode or use the Create button to create a material cost estimate. |  |

### Intercompany Sales and Stock Transfer Process

Follow the test procedures in Advanced Intercompany Sales (5D2) and/or Advanced Intercompany Stock Transfer (5HP) to review the effects of group valuation, where intercompany profits between trading partners are eliminated in real time.

### Actual Costing for Group Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, edits to actual costing run are executed.

Procedure

Follow the Actual Costing Ledger Run procedure in Actual Costing (33Q) script using ledger 4G.

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
- see-also :: [[06-management-accounting/product-cost-related-master-data-changes-consumer-products-61w-ae-test]]
- see-also :: [[08-sales-order-management/intercompany-sales-order-processing-domestic-1ho-ae-724]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5W2_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 22,962 chars in the whole document
