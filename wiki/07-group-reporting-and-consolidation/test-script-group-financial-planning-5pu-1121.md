---
id: 07-group-reporting-and-consolidation/test-script-group-financial-planning-5pu-1121
title: "Test Script: Group Financial Planning (5PU) (5PU_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 5PU: group financial planning (P&L, balance sheet, by partner) in SAP Analytics Cloud, plus S/4HANA data load."
cluster: 07-group-reporting-and-consolidation
tags: [kb/group-reporting-and-consolidation, topic/group-financial-planning]
aliases: [5PU_S4CLD2608_BPD_EN_XX]
keywords: [Group Financial Planning in SAP Analytics Cloud, group financial planning, target planning, bottom up planning, planning administration, planning reports, planning analytics, s/4hana data integration, sap analytics cloud, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5PU_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1121
topic: 07-group-reporting-and-consolidation/group-financial-planning
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Group Financial Planning (5PU) (5PU_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5PU_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Group Financial Planning in SAP Analytics Cloud** in Group Reporting and Consolidation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Group Financial Planning (5PU) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232841181)

[2 Prerequisites 3](#_Toc232841182)

[2.1 Business Content Activation and Integration Setup 3](#_Toc232841183)

[2.2 System Access 3](#_Toc232841184)

[2.3 Roles 3](#_Toc232841185)

[2.4 Master Data, Organizational Data, and Other Data 4](#_Toc232841186)

[2.5 Additional Manual Configuration 4](#_Toc232841187)

[3 Overview Table 5](#_Toc232841188)

[4 Test Procedures 6](#_Toc232841189)

[4.1 Group Financial Planning 6](#_Toc232841190)

[4.1.1 Landing Page 6](#_Toc232841191)

[4.1.2 Perform Planning Admin Tasks 7](#_Toc232841192)

[4.1.3 Perform Group Financial Target Planning 8](#_Toc232841193)

[4.1.4 Perform Group Financial Bottom Up Planning 9](#_Toc232841194)

[4.1.5 Review Group Financial Planning Reports 11](#_Toc232841195)

[4.1.6 Review Group Financial Planning Analytics 12](#_Toc232841196)

[4.2 Integration into SAP S/4HANA 12](#_Toc232841197)

[4.2.1 Group Financial Planning 13](#_Toc232841198)

[4.2.1.1 Load Master and Actual Data from SAP S/4HANA 13](#_Toc232841199)

## Purpose

Overview

This process supports detailed group financial planning. It includes P&L planning, P&L planning by partner, balance sheet planning, and balance sheet planning by partner.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Business Content Activation and Integration Setup

Perform the following Getting Started activities for SAP Analytics Cloud:

[Importing SAP Business Content: Group Financial Planning for SAP S/4HANA Cloud Public Edition](https://help.sap.com/viewer/1cbcff7ccd35405ab445b223c1ab1588/latest/en-US/3fd7ba64d0e44fc89d1bbfd7dd44f564.html)

[Integrating SAP Analytics Cloud with SAP S/4HANA Cloud Public Edition](https://help.sap.com/viewer/1cbcff7ccd35405ab445b223c1ab1588/latest/en-US/79fab594ccdf4667a1e493411d8428db.html) (only required for the [Integration into SAP S/4HANA](#unique_4) [page ] 12 section)

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

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | <company code>, for example, <1710> |  |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/f1202adfd396277bca5a620096867f18)

## Overview Table

This scope item consists of several processes provided in this table.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Group Financial Planning | Admin, Planner | SAP Analytics Cloud | Profit and loss and balance sheet planning. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Group Financial Planning

#### Landing Page

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
| 1 | Access the Story Page | Open the Files in the Main Menu. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_GFP_IM_LandingPage | The Story SAP_FI_GFP_IM_LandingPage is displayed. |  |
| 3 | Use the Navigation | Use the links in the lower section to open the Target Planning story to any of the named tabs. | The named story and tab are opened in a new browser tab. |  |
| 4 | Use the Navigation | Use the links in the lower section to open the Bottom Up Planning story to any of the named tabs. | The named story and tab are opened in a new browser tab. |  |
| 5 | Use the Navigation | Use the links in the lower section to open the Analytics story to any of the named tabs. | The named story and tab are opened in a new browser tab. |  |
| 6 | Use the Navigation | Use the links in the lower section to open the Reports story and show any of the named tabs. | The named story and tab are opened in a new browser tab. |  |
| 7 | Use the Navigation | Use the links in the lower section to open the Admin story and show any of the named tabs. | The named story and tab are opened in a new browser tab. |  |

#### Perform Planning Admin Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you perform the planning administration tasks.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Story Page | From the main menu, open Browse > Files. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_GFP_IM_GroupFinance_Admin. | The story SAP_FI_GFP_IM_GroupFinance_Admin is displayed. |  |
| 3 | Create Sample Data | Choose the Create Sample Data tab. |  |  |
| 4 | Create Sample Data | Run the Create Sample Data for Actuals data action. | Sample actuals data are displayed. |  |
| 5 | Optional: Execute Planning Functions | Choose the Planning Functions tab. |  |  |
| 6 | Optional: Execute Planning Functions | Execute the data actions. | Resulting plan data are displayed. |  |
| 7 | Publish Actual and Plan Data | Choose Publish Data. |  |  |
| 8 | Publish Actual and Plan Data | Choose Publish All. | A success message is displayed. |  |

#### Perform Group Financial Target Planning

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
| 1 | Access the Story Page | Open the Browse ® Files in the Main Menu. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_GFP_IM_GroupFinance_TargetPlanning | The story SAP_FI_GFP_IM_GroupFinance_TargetPlanning is displayed. |  |
| 3 | Select Profit Center(s) | On the FS Item by PC tab, use the page filter to select profit centers. | Filtered data are displayed. |  |
| 4 | Copy Net Income Actual Data to Plan | On the FS Item by PC tab, use data action Copy P&L and Balance Sheet from Actuals | Resulting plan data are displayed. |  |
| 5 | Review and Adjust Profit and Loss Amounts | On the FS Item by PC tab, adjust the financial statement item amounts. | Entered amounts are accepted. |  |
| 6 | Select Financial Statement Items(s) | On the PC by FS Item tab, use the page filter to select financial statement items. | Filtered data are displayed. |  |
| 7 | Review and Adjust Profit and Loss Amounts by Profit Center | On the PC by FS Item tab, adjust the financial statement item amounts. | Entered amounts are accepted. |  |
| 8 | Select Consolidation Unit(s) | On the FS Item by ConsUnit tab, use the page filter to select Consolidation Unit(s). | Filtered data are displayed. |  |
| 9 | Review and Adjust Profit and Loss Amounts | On the FS Item by ConsUnit tab, adjust the financial statement item amounts. | Entered amounts are accepted. |  |
| 10 | Select Financial Statement Items(s) | On the Cons Unit by FS Item tab, use the page filter to select financial statement items. | Filtered data are displayed. |  |
| 11 | Review and Adjust Profit and Loss Amounts by Consolidation Unit | On the Cons Unit by FS Item tab, adjust the financial statement item amounts. | Entered amounts are accepted. |  |
| 12 | Select Financial Statement Items(s) | On the Matrix by FS Item tab, use the page filter to select financial statement items. | Filtered data are displayed. |  |
| 13 | Review and Adjust Profit and Loss Amounts by Profit Center and Consolidation Unit | On the Matrix by FS Item tab, adjust the financial statement item amounts. | Entered amounts are accepted. |  |
| 14 | Select Consolidation Unit(s) | On the Balance Sheet - Changing tab, use the page filter to select consolidation units. | Filtered data are displayed. |  |

#### Perform Group Financial Bottom Up Planning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you perform the group financial bottom up planning.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Story Page | Open the Browse ® Files in the Main Menu. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_GFP_IM_GroupFinance_BottomUpPlanning | The story SAP_FI_GFP_IM_GroupFinance_BottomUpPlanning is displayed. |  |
| 3 | Copy Net Income Actual Data to Plan | On the P&L w/Hierarchy tab use data action Copy P&L and Balance Sheet from Actuals . | Resulting plan data are displayed. |  |
| 4 | Review and Adjust Profit and Loss Amounts | On the P&L w/Hierarchy tab, adjust the financial statement item amounts. | Entered amounts are accepted. |  |
| 5 | Review and Adjust Profit and Loss Amounts by Partner | On the P&L by Partner tab, adjust the financial statement item amounts. | Entered amounts are accepted. |  |
| 6 | Plan Balance Sheet Changing Balance | On the Balance Sheet - Changing tab, adjust the changing amounts and first period opening amount. | Entered amounts are accepted. |  |
| 7 | Carryforward Balance Amounts | On the Balance Sheet - Changing tab use data action Calculate Balance Sheet for Closing . | Resulting plan data is adjusted. |  |
| 8 | Plan Balance Sheet Closing Balance | On the Balance Sheet - Closing tab, adjust the closing amounts and first period opening amount. | Entered amounts are accepted. |  |
| 9 | Carryforward Balance Amounts | On the Balance Sheet - Closing tab use data action Calculate Balance Sheet for Changing . | Resulting plan data is adjusted. |  |
| 10 | Plan Balance Sheet Changing Balance by Partner | On the BS – Changing by Partner tab, adjust the changing amounts and first period opening amount. | Entered amounts are accepted. |  |
| 11 | Carryforward Balance Amounts | On the BS – Changing by Partner tab use data action Calculate Balance Sheet for Closing . | Resulting plan data is adjusted. |  |
| 12 | Plan Balance Sheet Closing Balance by Partner | On the BS Closing by Partner tab, adjust the closing amounts and first period opening amount. | Entered amounts are accepted. |  |
| 13 | Carryforward Balance Amounts | On the BS Closing by Partner tab use data action Calculate Balance Sheet for Changing . | Resulting plan data is adjusted. |  |
| 14 | Review Financial Statement Item Report | On the Financial Statement Item Report tab, review the resulting plan data. | Resulting plan data are displayed. |  |

#### Review Group Financial Planning Reports

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you review the group financial planning reports.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Story Page | From the main menu, open Browse > Files. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_GFP_IM_GroupFinance_Reports | The story SAP_FI_GFP_IM_GroupFinance_Reports is displayed. |  |
| 3 | Adjust Story Filters | Adjust story filters for Consolidation Unit , Partner Consolidation Unit, and Functional Area as necessary. | Displayed data are filtered. |  |
| 4 | Review Plan Data | On each tab, review the plan data. | Plan data are displayed. |  |

#### Review Group Financial Planning Analytics

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
| 1 | Access the Story Page | Open the Browse > Files in the Main Menu. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_GFP_IM_GroupFinance_Analytics . | The story SAP_FI_GFP_IM_GroupFinance_Analytics is displayed. |  |
| 3 | Adjust Story Filters | Adjust story filters for Plan Year and Consolidation Unit as necessary. | Displayed data are filtered. |  |
| 4 | Profit & Loss Overview | Choose the Profit & Loss Overview tab. Review the plan data. Adjust the Select KPI input control. | Plan data are displayed. |  |
| 5 | Select Balance Sheet Overview tab | Choose the Balance Sheet Overview tab. Review the plan data. Adjust the Select KPI input control. | Plan data are displayed. |  |

### Integration into SAP S/4HANA

In this section, you test the master data integration, transaction data integration, and export to SAP S/4HANA.

#### Group Financial Planning

##### Load Master and Actual Data from SAP S/4HANA

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you load master and actual data from SAP S/4HANA to SAP Analytics Cloud.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open SAP Analytics Cloud | Use the URL and credentials provided by the system administrator to access SAP Analytics Cloud. | The Home - Welcome to SAP Analytics Cloud screen is displayed. |  |
| 2 | Go to the Consolidation Unit dimension | From the main menu, open Browse > Dimensions .Search for and open SAP_ FI _ GFP _ CONSUNIT. | The public dimension is displayed. |  |
| 3 | Data Management | Choose the Data Management tab. | The Data Management tab is displayed. |  |
| 4 | Refresh the Job | Choose Refresh at the right side of the job. | The system displays a message stating number of rows imported. |  |
| 5 | Repeat for Three Dimensions | Repeat steps 2 to 4 for the following dimensions:SAP_FI_GFP_TRANSACTIONTYPESAP_FI_GFP_FSITEMSAP_FI_GFP_PRTNCONSUNITSAP_FI_GFP_FUNCTIONALAREA | The system displays a message stating number of rows imported. |  |
| 6 | Go to the group reporting planning model | In the Main Menu, choose Browse > Files . Search for and open SAP_FI_GFP_IM_GroupFinance. | The model SAP_FI_GFP_IM_GroupFinance is displayed. |  |
| 7 | Data Management | Choose the Data Management tab. | The Data Management tab is displayed. |  |
| 8 | Refresh Job to Load Actual Bottom Up Data | Under Import Jobs, choose Refresh at the right of the job.[Bottom Up] GRTransactionData | The system displays a message stating number of rows imported. |  |
| 9 | Refresh Job to Load Actual Target Data | Under Import Jobs, choose Refresh at the right of the job.[Target] GRTransactionData | The system displays a message stating number of rows imported. |  |

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
- related-to :: [[06-management-accounting/test-script-sap-s-4hana-cloud-public-edition-integrated-financial-plan]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5PU_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 21,185 chars in the whole document
