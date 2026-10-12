---
id: 07-group-reporting-and-consolidation/test-script-intercompany-reconciliation-process-40y-sap-s-4hana-cloud
title: "Test Script: Intercompany Reconciliation Process (40Y) - SAP S/4HANA Cloud Public Edition (40Y_S4CLD2608_BPD_EN_XX)"
description: "SAP test script for scope item 40Y Intercompany Reconciliation: prerequisites, roles and Fiori test steps from hierarchy setup to matrix reconciliation."
cluster: 07-group-reporting-and-consolidation
tags: [kb/group-reporting-and-consolidation, topic/intercompany-matching-and-reconciliation]
aliases: [40Y_S4CLD2608_BPD_EN_XX]
keywords: [Intercompany Matching and Reconciliation, intercompany reconciliation, test scripts, matching runs, reconciliation status, reconciliation balances, manage assignments, reconciliation close, matrix reconciliation, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/40Y_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-992
topic: 07-group-reporting-and-consolidation/intercompany-matching-and-reconciliation
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Intercompany Reconciliation Process (40Y) - SAP S/4HANA Cloud Public Edition (40Y_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/40Y_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Intercompany Matching and Reconciliation** in Group Reporting and Consolidation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Intercompany Reconciliation Process (40Y) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232841694)

[2 Prerequisites 3](#_Toc232841695)

[2.1 System Access 3](#_Toc232841696)

[2.2 Roles 3](#_Toc232841697)

[2.3 Business Conditions 4](#_Toc232841698)

[2.4 Additional Manual Configuration 4](#_Toc232841699)

[3 Overview Table 5](#_Toc232841700)

[4 Test Procedures 7](#_Toc232841701)

[4.1 Preparation for Intercompany Reconciliation 7](#_Toc232841702)

[4.2 Schedule Matching Run Jobs 10](#_Toc232841703)

[4.3 Check Reconciliation Status Overview 11](#_Toc232841704)

[4.4 Check Reconciliation Balances Report 13](#_Toc232841705)

[4.5 Manage Assignments 14](#_Toc232841706)

[4.6 Display Matching Items 17](#_Toc232841707)

[4.7 Manage Teams and Responsibilities (Optional) 17](#_Toc232841708)

[4.8 Approve Adjustment Postings by Workflow (Optional) 19](#_Toc232841709)

[4.9 Matrix Reconciliation (Optional) 19](#_Toc232841710)

## Purpose

Overview

This scope item covers the process of reconciling the accounting documents that describe the accounting transactions within a corporate group in accordance with the predefined matching method. It allows early analysis in the closing process to avoid differences altogether and to reduce the deadline pressure that normally arises during the end of a closing period.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| General Ledger Accountant - Intercompany | SAP_BR_RECON_ACCOUNTANT | Intercompany Reconciliation | SAP_BR_RECON_ACCOUNTANT | Use the generic user below.Generic User: RECON_ACCOUNTANT |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | Use the generic user below.Generic User: BPC_EXPERT |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT | Ask your system administrator to assign to the testers.Generic User: GL_ACCOUNTANT |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 1HO - Intercompany Sales Order Processing – Domestic or1MX - Intercompany Sales Order Processing – International or1WO - Extended Intercompany Processes for Sales or2F4 - Intercompany Process for Customer Returns or1P9 - Intercompany Stock Transfer or2TS - Intercompany Stock Transfer Returns or16T - Intercompany Processes – Project-Based Services or1GP - Intercompany Financial Posting | You have completed at least one of these intercompany scenarios and generated intercompany FI postings. |

|  |
| --- |
| Note If these scope items are not running in the system and you want to run the test script for testing purpose, you can log on as General Ledger Accountant and upload the [template](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/Others/JournalEntry_Template_40Y.xlsx) with app Upload General Journal Entries (F2548).Please replace "XXXX" and "YYYY" with your assigned company code before uploading the template.If you want the template in your language, you can also go to app Upload General Journal Entries (F2548) and choose Download Template on the lower right of the screen. |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/49aca346f385b32007a9598706d4630c)

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transction | Expected Results |
| --- | --- | --- | --- |
| [Preparation for Intercompany Reconciliation](#unique_8) [page ] 7 | General Ledger Accountant - Intercompany | Manage Global Hierarchies (F2918) |  |
| [Schedule Matching Run Jobs](#unique_9) [page ] 10 | General Ledger Accountant - Intercompany | Define Matching Methods (F3862) or Schedule Matching Run Jobs (F5011) |  |
| [Check Reconciliation Status Overview](#unique_10) [page ] 11 | Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:Configure Your Solution: Configuration Expert - Business Process ConfigurationSAP Central Business Configuration: Log on to the project experienceGeneral Ledger Accountant - Intercompany | Reconciliation Status Overview (F3865) |  |
| [Check Reconciliation Balances Report](#unique_11) [page ] 13 | General Ledger Accountant - Intercompany | Reconciliation Balances (F3865) |  |
| [Manage Assignments](#unique_12) [page ] 14 | General Ledger Accountant - Intercompany | Manage Assignments - By Reconciliation Case |  |
| [Display Matching Items](#unique_13) [page ] 17 | General Ledger Accountant - Intercompany | Display Matching Items - By Reconciliation Case (F3869) |  |
| [Manage Teams and Responsibilities (Optional)](#unique_14) [page ] 17 | General Ledger Accountant - Intercompany | Manage Teams and Responsibilities (Intercompany) |  |
| [Approve Adjustment Postings by Workflow (Optional)](#unique_15) [page ] 19 | General Ledger Accountant - Intercompany | Manage Assignments - By Reconciliation Case (F3870) |  |
|  | Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:Configure Your Solution: Configuration Expert - Business Process ConfigurationSAP Central Business Configuration: Log on to the project experienceGeneral Ledger Accountant - Intercompany | Manage Your Solution (F1241)Define Matching Methods (F3862) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Preparation for Intercompany Reconciliation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you prepare the master data.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant - Intercompany. |  |  |
| 2 | Access App | Open Manage Consolidation Hierarchies (F7995). |  |  |
| 3 | Define New Hierarchy | Choose Create.Make the following entries:Type: CompanyHierarchy ID: ZICA_COMPHierarchy Description: IC Company HierarchyValid From: 01/01/2010Choose Create. |  |  |
| 4 | Assign Company to the New Hierarchy | Choose > for the new hierarchy you created.Choose Edit. Then choose + Add).In the Add Note view, choose Company, add with ID, such as 1010, 1210, 1710. Then choose OK.After the units are added, choose Save button. And then choose Activate button to activate the hierarchy.The created hierarchy can be used in Define Reconciliation Cases (F3863) app for hierarchy display if you create your own reconciliation case. |  |  |
| 5 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 6 | Maintain Exchange Rate (Optional) | Open the app Currency Exchange Rates (F3616) and maintain the correct exchange rate for your source currency and target currency.Exchange Rate Type: MIn Currency Pair entry, enter following entries and choose OK:From Currency: <your company code currency>To Currency: <For test purpose, USD or EUR> |  |  |
| 7 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 8 | Assign Posting Rules | Choose Manage Your Solution (F1241).Choose Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Corporate CloseFor item Intercompany Matching and Reconciliation, choose >.Choose Configure for step Assign Posting Rules and choose New Entries if below entries don't exist:Matching Method: SF101 or SF102Reason Code: <Leave empty>Posting Rule: SA002Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Manage Consolidation Hierarchies (F7995). |  |  |
| 3 | Define New Hierarchy | Choose Create.Make the following entries:Type: CompanyHierarchy ID: ZICA_COMPHierarchy Description: IC Company HierarchyValid From: 01/01/2010Choose Create. |  |  |
| 4 | Assign Company to the New Hierarchy | Choose > for the new hierarchy you created.Choose Edit. Then choose + Add).In the Add Note view, choose Company, add with ID, such as 1010, 1210, 1710. Then choose OK.After the units are added, choose Save button. And then choose Activate button to activate the hierarchy.The created hierarchy can be used in Define Reconciliation Cases (F3863) app for hierarchy display if you create your own reconciliation case. |  |  |
| 5 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 6 | Maintain Exchange Rate (Optional) | Open the app Currency Exchange Rates (F3616) and maintain the correct exchange rate for your source currency and target currency.Exchange Rate Type: MIn the Currency Pair entry, enter following entries and choose OK:From Currency: <your company code currency>To Currency: <For test purpose, USD or EUR> |  |  |
| 7 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 8 | Open Assign Posting Rules | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Posting Rules.Choose Open Document for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Posting Rules screen displays. |  |
| 9 | Assign Posting Rules | Choose New Entries if below entries don't exist:Matching Method: SF101 or SF102Reason Code: <Leave empty>Posting Rule: SA002Choose Save. |  |  |

### Schedule Matching Run Jobs

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant - Intercompany. |  |  |
| 2 | Run Matching Job | Open Schedule Matching Run Jobs - By Company (F7669). |  |  |
| 3 | Enter Details | Choose Create. |  |  |
| 4 | Enter Details | Keep the default values in Step 1 and Step 2.Choose Step 3. Make the following entry and keep other filter fields empty:Method: SF101 or SF102Choose Schedule. | Matching logs are displayed. No errors appear. |  |

### Check Reconciliation Status Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Active Closing Process | Choose Manage Your Solution (F1241).Choose Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Corporate CloseChoose Intercompany Matching and Reconciliation > Activate Reconciliation Close Process.Add your reconciliation case and ensure:Active: <Checked>Reference GC Amount: KSL |  |  |
| 3 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant - Intercompany. |  |  |
| 4 | Access the SAP Fiori App | Open Reconciliation Status Overview (F3865). |  |  |
| 5 | Display Reconciliation Report | Make the following entries and choose Go:Reconciliation Case: <your reconciliation case>Company: <your assigned company code>Fiscal Year Period: <period, for example, 005/2019>If new documents are posted, the New Postings column shows Detected.Choose > to go to the Reconciliation Balances screen. The view shows the detail of how many partner companies are reconciled, reconciled within tolerance or not reconciled. | Initial reconciliation status of selected company is displayed. |  |
| 6 | On the Fly Translation | In the dropdown list, choose the converted measure to see the on the fly translation. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Activate Reconciliation Close Process | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Reconciliation Close Process.Choose Open Document for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Activate Reconciliation Close Process screen displays. |  |
| 3 | Activate Reconciliation Close Process | Add your reconciliation case and ensure:Active: <Checked>Reference GC Amount: KSL |  |  |
| 4 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant - Intercompany. |  |  |
| 5 | Access the SAP Fiori App | Open Reconciliation Status Overview (F3865). |  |  |
| 6 | Display Reconciliation Report | Make the following entries and choose Go:Reconciliation Case: <your reconciliation case>Company: <your assigned company code>Fiscal Year Period: <period, for example, 005/2019>If new documents are posted, the New Postings column shows Detected.Choose > to go to the Reconciliation Balances screen. The view shows the detail of how many partner companies are reconciled, reconciled within tolerance or not reconciled. | Initial reconciliation status of selected company is displayed. |  |
| 7 | On the Fly Translation | In the dropdown list, choose the converted measure to see the on the fly translation. |  |  |

### Check Reconciliation Balances Report

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant - Intercompany. |  |  |
| 2 | Check Reconciliation Balance Report | In the list view, select a Company line (using the parameters below) or you can open a new App Reconciliation Balances (F3865) to see the Reconciliation Balance.Select the parameters as follows:Reconciliation Case: <For example, SF101 or SF102>Display Group: <For example, Group 1010 (IC Trading All AR/AP Relevant Accounts)>Company: <Your assigned company code, for example, 1010>Fiscal Year Period: <For example, 005/2019>Choose Go. | Reconciliation balance for selected company and selected group is displayed. |  |
| 3 | Display Other Group and Switch View | Change to the other Display Group to display the Reconciliation Balance report.Change to the Netting View.Switch to other currencies (for example, choose Amount in Tran.Currency).To download the Excel, choose Export to Spreadsheet.To check the detailed documents list for an amount, right-click the amount and choose Show matching items. | Reconciliation balance for selected company and selected group is displayed. |  |
| 4 | Display Company Name | By default the company ID is displayed. You can right click the column Company and choose Show Description to display the description. | Company Description is displayed. |  |
| 5 | Scale on amount | By default the complete amount is displayed. If it's too long to display, you can choose button switch to short number format to display the number in short. | Number is displayed in short format. |  |
| 6 | Filter Amount | Right click column Difference and choose Non-Zero Differences. You can filter out zero rows.If you have defined tolerance in Define Reconciliation Cases (F3863) app for the display group, you can choose Difference Outside Tolerance to filter out the rows within tolerance. |  |  |
| 7 | Display layout (Optional) | With default configuration SF101 and SF102, four sections are displayed:Up to Now (YTD)Up to Last Matching (YTD)Up to Now (Period)Up to Last Matching (Period)If you want to focus on the specific section, you can achieve this via changing Display Option in Define Reconciliation Cases (F3863) app. |  |  |

### Manage Assignments

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant - Intercompany. |  |  |
| 2 | Manage Assignments | To manage assignments, choose the right arrow button for a reconciliation balance line item or you can open a new APP Manage Assignments - By Reconciliation Case.The parameters are set as follows :Reconciliation Case: <your reconciliation case ID>Display Group: <For example, All IC Accounts AR/AP>Company: <your assigned company code>Fiscal Year Period: <For example, 005/2019>Amount/Quantity Field: <keep current value, for example, WSL for transaction currency>Choose Go. | Details of reconciliation results are displayed. |  |
| 3 | Manage Assignments – Display Assigned Items | All the assigned items (by rule or by manual) are displayed in the lower part of the screen. From the middle tool bar, very right side, choose Change Layout > Lower Area Only .From the left filter bar, switch the filter to display the different groups of assignments.Select a line to check the assigned documents. The right pane expands to show additional details. To display the included documents, choose Expand.Hover over the reason code to display the description. You can sort or filter by value.Choose the Assignment Number link to display more details. To check the rule detail, choose the Rule number link.Check the matching result; the columns with color are fields used in the matching expression. Choose Back.Optionally, you can remove the assignment by selecting the assignment and choosing Unassign. | Details of assigned items are displayed. |  |
| 4 | Send Email for Query | Choose one assignment row, and then from dropdown list, choose Communicate > Send Email , you can send email to others for query. |  |  |
| 5 | Manage Assignment – Communication | Choose Only upper area to show the unassigned documents.In the left panel, the system displays the leading company unassigned documents.In the right panel, the system displays the partner company unassigned documents.From any panel, to search a document, choose Fuzzy Search and enter a keyword to search the documents.To add notes or send notifications, select one or more documents and choose Communication, then send a notification or add a note.The user can give a due date. If it is due, the documents in the left panel display a red bar to reminder user those documents are due for further action. To clear the due items display, select the items, and in Communication, choose Set to done. | Notification is sent without errors. |  |
| 6 | Manage Assignment – Manual Assign Documents | From the unassigned documents displayed, select documents to manually assign. For test perspective, please assign S15 for the reason code. | Documents are manually assigned. |  |
| 7 | Assignment for auto posting | Choose button Go again and then you can find the generated accounting document appears in the Unassigned panel.Choose button Auto Matching again and you can find the auto posting and previous postings are grouped together in one assignment document. |  |  |
| 8 | Trigger Auto Posting | For the newly assigned document, in column Adjustment Log, you can find log like Success (2) which means adjustment documents are successfully created.Click this hyperlink to see the detailed log description. You can get the generated jounal document number.Choose Back to back to Manage Assignment screen. |  |  |
| 9 | Manage Reconciliation Close with Workflow (Optional) | If you want to enable workflow for manage reconciliaiton status, following steps are needed:a. In Configuration Step Activate Reconciliation Close Process (103560), choose Always for Workflow option and WS78500026 for Workflow Scenario ID for your reconciliation caseb. create the team in the step Manage Teams and ResponsibilitiesNote Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration.Note Skip this step if no workflow is needed. |  |  |
| 10 | Manage Reconciliation Close | Make the following entries and choose Go:Reconciliation Case: SF101Fiscal Year Period: your periodCompany: company usedSelect Company and choose Close to close reconciliation in the period. |  |  |
| 11 | Approve Reconciliation Close with workflow (Optional) | Logon with the user defined in the team.Access Approve Reconciliation Close Requests and approve/reject the close request.Note Skip this step if no workflow is needed. |  |  |

### Display Matching Items

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
| 1 | Log on | Log on to the SAP Fiori launchpad as a General Ledger Accountant - Intercompany. | The SAP Fiori launchpad is displayed. |  |
| 2 | Display Matching Items | Choose the Balance button to go to the Display Matching Items - By Reconciliation Case (F3869) app or open a new App Display Matching Items - By Reconciliation Case (F3869).Select the parameters as follows :Matching Method: <For example, SF101 or SF102>Company: <Your assigned company codes>Fiscal Period/Year:<For example, 005/2019>Choose Go. | Matching items are displayed properly. |  |

### Manage Teams and Responsibilities (Optional)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant - Intercompany. |  |  |
| 2 | Access Fiori App | Open Manage Teams and Responsibilities (F6783). |  |  |
| 3 | Create New Team | Choose Create. Make the following entries and choose Save:Name: <input name>Type: ICAMTDescription: <input description> |  |  |
| 4 | Define Team Memebers | Choose Create in section Team Members, input User ID and choose OK. |  |  |
| 5 | Enter Function | In the section Team Members, for the line of new added team member, choose Functions, and check ICAM_COMM, ICAM_SP, ICAM_SV, and choose OK.Save and enable the entry. |  |  |
| 6 | Create New Team | Choose Create. Make the following entries and choose Save:Name: <input name>Type: ICAMT_RCADescription: <input description> |  |  |
| 7 | Define Team Memebers | Choose Create in section Team Members, input User ID and choose OK. |  |  |
| 8 | Enter Function | In the section Team Members, for the line of newly added team member, choose Functions, and check ICAM_RCA, ICAM_RCC, and choose OK.Save and enable the entry. |  |  |

### Approve Adjustment Postings by Workflow (Optional)

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
| 1 | Log on | Log on to the SAP Fiori launchpad as a General Ledger Accountant - Intercompany. | The SAP Fiori launchpad is displayed. |  |
| 2 | Manage Assignments – By Matching Method | Open Manage Assignments - By Reconciliation Case (F3870).From the screen lower part, all the assigned items (by rule or by manual) are displayed. Find one row with Proc. Status 20(Assigned) and choose >.In the matching detail screen, choose Reason Code S16 and then choose Process. | Now the Workflow Status is changed to In process. |  |
| 3 | Switch to approver role and log on to the SAP Fiori launchpad | Open App Verify Intercompany Variance Adjmt - Inbox (F5764).Select the item in the left side and check the details.Choose Approve at the bottom.Write notes if necessary and choose Submit. |  |  |
| 4 | Manage Assignments – By Matching Method | Open Manage Assignments - By Reconciliation Case (F3870).From the lower part of the screen, now Workflow Status has been changed to Completed, and Adjustment Log has been changed to Success. |  |  |

### Matrix Reconciliation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you set the global parameters for the integration.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail /Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Create Matrix Reconciliation Data Source | Choose Manage Your Solution (F1241).Choose Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Corporate CloseSelect Item Intercompany Matching and Reconciliation and choose >.For the step Maintain Data Sources, choose Configure.Select Data Source SF_JOURNAL_ENTRIES_01 and choose Copy As…. |  |  |
| 3 | Maintain Data Source Attribute | In the Change View "Data Source": Details of Selected Set view, make the following entries:Data Source: <input name>Description: <input description>Main CDS View: <keep default>Leading Unit Field: <keep default>Leading Unit Superordinate Field: <choose the value, for example, Profit Center>Partner Unit Field: <keep default>Partner Unit Superordinate Field: <corresponding Partner Superordinate Field selected before>Unit Entity CDS View: <from value help choose the correct CDS View>Authorization Object of Unit: <keep default or empty>And choose button Apply and Save. |  |  |
| 4 | Logon | Log on to the SAP Fiori launchpad as a General Ledger Accountant - Intercompany. |  |  |
| 5 | Create Matrix Matching Method | Open Define Matching Methods (F3862).Choose Create. |  |  |
| 6 | Maintain Matrix Matching Method | In the New Method view, make the following entries:Matching Method ID: <input ID>Description: <input Desc>Stored As: Master DataData Source: <choose the matrix data source>For other attributes, you can refer to SF101 and maintain exactly the same value for your method.Choose Save for your method. |  |  |
| 7 | Create Recon Case | Open Define Reconciliation Cases (F3863).Choose > for SF101 or SF102 and then choose button Copy. |  |  |
| 8 | Maintain Reconciliation Case | In the New Reconciliation Case view, make the following entries:Reconciliation Case ID: <input ID>Description: <input Desc>Stored As: Master DataMatching Method: <choose the matrix matching method>Other Settings: <If you have created Superordinate Unit Hierarchy or Unit Hierarchy, you can include the hierarchy here or leave empty.>Choose Save for your reconciliation case. |  |  |
| 9 | Run Matrix Reconciliation Process | With the data source, matching method and reconciliation case created, you can follow the previous sections to run matrix reconciliation.Please notice to run matrix reconciliation, you need to specify leading unit / superordinate leading unit combination. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail /Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Maintain Data Sources | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain Data Sources.Choose Open Document for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Maintain Data Sources screen displays. |  |
| 3 | Create Matrix Reconciliation Data Source | Select Data Source SF_JOURNAL_ENTRIES_01 and choose Copy As…. |  |  |
| 4 | Maintain Data Source Attribute | In the Change View "Data Source": Details of Selected Set view, make the following entries:Data Source: <input name>Description: <input description>Main CDS View: <keep default>Leading Unit Field: <keep default>Leading Unit Superordinate Field: <choose the value, for example, Profit Center>Partner Unit Field: <keep default>Partner Unit Superordinate Field: <corresponding Partner Superordinate Field selected before>Unit Entity CDS View: <from value help choose the correct CDS View>Authorization Object of Unit: <keep default or empty>And choose button Apply and Save. |  |  |
| 5 | Logon | Log on to the SAP Fiori launchpad as a General Ledger Accountant - Intercompany. |  |  |
| 6 | Create Matrix Matching Method | Open Define Matching Method.Choose Create. |  |  |
| 7 | Maintain Matrix Matching Method | In the New Method view, make the following entries:Matching Method ID: <input ID>Description: <input Desc>Stored As: Master DataData Source: <choose the matrix data source>For other attributes, you can refer to SF101 and maintain exactly the same value for your method.Choose Save for your method. |  |  |
| 8 | Create Recon Case | Open the activity Define Reconciliation Cases.Choose > for SF101 or SF102 and then choose button Copy. |  |  |
| 9 | Maintain Reconciliation Case | In the New Reconciliation Case view, make the following entries:Reconciliation Case ID: <input ID>Description: <input Desc>Stored As: Master DataMatching Method: <choose the matrix matching method>Other Settings: <If you have created Superordinate Unit Hierarchy or Unit Hierarchy, you can include the hierarchy here or leave empty.>Choose Save for your reconciliation case. |  |  |
| 10 | Run Matrix Reconciliation Process | With the data source, matching method and reconciliation case created, you can follow the previous sections to run matrix reconciliation.Please notice to run matrix reconciliation, you need to specify leading unit / superordinate leading unit combination. |  |  |

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

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: App references are inconsistent within the document: the Overview Table lists Manage Global Hierarchies (F2918) but the procedure opens Manage Consolidation Hierarchies (F7995); Overview lists Schedule Matching Run Jobs (F5011) but the procedure uses Schedule Matching Run Jobs - By Company (F7669); F3865 is given to both Reconciliation Status Overview and Reconciliation Balances.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[03-financial-accounting-and-close/journal-entry-template-40y-193]]
- related-to :: [[07-group-reporting-and-consolidation/test-script-sap-s-4hana-cloud-public-edition-group-reporting-financial-part-01]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/40Y_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 38,904 chars in the whole document
