---
id: 06-management-accounting/test-script-overhead-cost-accounting-j54-ae-sap-s-4hana-cloud-public-e
title: "Test Script: Overhead Cost Accounting (J54_AE) - SAP S/4HANA Cloud Public Edition (J54_S4CLD2608_BPD_EN_AE)"
description: "Test script for SAP S/4HANA Cloud scope item J54 Overhead Cost Accounting (AE, 2608): prerequisites, cost center postings, allocations, reports, budgeting."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/overhead-cost-accounting]
aliases: [J54_S4CLD2608_BPD_EN_AE]
keywords: [Overhead Cost Accounting, cost centers, overhead allocation, direct activity allocation, statistical key figures, profit center distribution, cost reassignment, cost center reporting, commitment management, cost center budgeting]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J54_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1302
topic: 06-management-accounting/overhead-cost-accounting
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Overhead Cost Accounting (J54_AE) - SAP S/4HANA Cloud Public Edition (J54_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J54_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Overhead Cost Accounting** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Overhead Cost Accounting (J54_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232863026)

[2 Prerequisites 4](#_Toc232863027)

[2.1 System Access 4](#_Toc232863028)

[2.2 Roles 4](#_Toc232863029)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232863030)

[2.4 Preliminary Steps 7](#_Toc232863031)

[2.4.1 User Settings - Set Controlling Area 7](#_Toc232863032)

[2.4.2 Set Report Relevancy 7](#_Toc232863033)

[2.4.3 Replicate Runtime Hierarchy 8](#_Toc232863034)

[2.4.4 Maintain Currency Exchange Rate to Global Currency 9](#_Toc232863035)

[2.4.5 Open Cost Accounting Period 10](#_Toc232863036)

[2.4.6 Create a Statistical Key Figure 11](#_Toc232863037)

[2.4.7 Optional: Posting Scheme for Intercompany Clearing 11](#_Toc232863038)

[2.4.8 Optional: Map CO Intercompany Accounts 13](#_Toc232863039)

[2.4.9 Optional: Updating Cost Center Budget Profiles (Only Required When Using Cost Center Budget Functionality) 14](#_Toc232863040)

[2.4.10 Optional: Currency Conversion Settings for Activity Allocation 16](#_Toc232863041)

[3 Overview Table 18](#_Toc232863042)

[4 Test Procedures 21](#_Toc232863043)

[4.1 Record Cost 21](#_Toc232863044)

[4.1.1 General Entries With Cost Center 21](#_Toc232863045)

[4.2 Transaction Based Allocations/Periodic Postings 23](#_Toc232863046)

[4.2.1 Direct Activity Allocation 23](#_Toc232863047)

[4.2.2 Post Statistical Key Figures 24](#_Toc232863048)

[4.2.3 View Posted Statistical Key Figures 26](#_Toc232863049)

[4.3 Repost Line Items - Cost Accounting 26](#_Toc232863050)

[4.4 Reassign Costs and Revenues 27](#_Toc232863051)

[4.5 Execute Overhead Allocation Cycle 29](#_Toc232863052)

[4.6 Allocation Results 31](#_Toc232863053)

[4.7 Allocation Flow 32](#_Toc232863054)

[4.8 Execute Profit Center Distribution 33](#_Toc232863055)

[4.9 Analytics 35](#_Toc232863056)

[4.9.1 Cost Centers Actual Data Reporting 35](#_Toc232863057)

[4.9.2 Cost Center Comparisons - Review Booklet 36](#_Toc232863058)

[4.9.3 Commitments by Cost Center 37](#_Toc232863059)

[4.9.4 Where-Used List - Cost Centers Actual 38](#_Toc232863060)

[4.9.5 Where-Used List - Statistical Key Figures 39](#_Toc232863061)

[4.9.6 Display Line Items in Controlling 40](#_Toc232863062)

[4.9.7 View Profit Center Distribution 40](#_Toc232863063)

[4.10 OPTIONAL: Commitment Management and Cost Center Budgeting 41](#_Toc232863064)

[4.10.1 Commitment Management Cost Centers Actual Data Reporting 41](#_Toc232863065)

[4.10.1.1 Exclude Cost Center Data for Commitment Management 42](#_Toc232863066)

[4.10.1.2 Create Purchase Order 43](#_Toc232863067)

[4.10.1.3 Commitment Management by Cost Center 44](#_Toc232863068)

[4.10.2 Cost Center Budgeting 45](#_Toc232863069)

[4.10.2.1 Set Cost Center Master Budgeting Parameters 46](#_Toc232863070)

[4.10.2.2 Upload Financial Data 47](#_Toc232863071)

[4.10.2.2.1 Template for File Upload 47](#_Toc232863072)

[4.10.2.2.2 Import Financial Data 48](#_Toc232863073)

[4.10.2.3 Create Purchase Order 50](#_Toc232863074)

[4.10.2.4 View Budget by Cost Center 51](#_Toc232863075)

[4.10.2.5 Transfer Cost Center Budgets 52](#_Toc232863076)

[5 Appendix 54](#_Toc232863077)

[5.1 Cost Center Replication from SAP S/4HANA Cloud Public Edition to SAP Master Data Integration (Optional) 54](#_Toc232863078)

## Purpose

Overview

This scope item covers transaction-based actual postings that are used in overhead cost controlling. The purpose of overhead cost controlling is the planning, allocation, control, and monitoring of overhead costs.

Cost center accounting takes the costs incurred in a company and allocates them to the actual subareas that caused them. During period-end closing, these costs are distributed to cost centers through automatic allocation. By allocating the cost elements to cost centers in overhead cost controlling, you can control your costs and compare plan and actual costs. The plan/actual comparison at the end of the period helps you to plan, control, and monitor cost behavior. Overhead cost controlling is also a prerequisite for further allocating overhead costs to cost objects (CO-PC), which enables you to conduct a period-specific profitability analysis.

|  |
| --- |
| Note Intercompany overhead calculation, settlement, and manual re-postings are supported. Intercompany allocation via Universal Allocation is currently supported with some limitations. |

Overhead cost controlling is also a prerequisite for further allocating overhead costs to cost objects (CO-PC), which enables you to conduct a period-specific profitability analysis.

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log on |
| --- | --- | --- | --- | --- |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Cost Accountant - Sales | SAP_BR_SALES_ACCOUNTANT | Sales Accounting | SAP_BR_SALES_ACCOUNTANT |  |
| Divisional Accountant | SAP_BR_DIVISION_ACCOUNTANT | Divisional Accounting | SAP_BR_DIVISION_ACCOUNTANT |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| OPERATING CONCERN | A000 |  |  |
| CONTROLLING AREA | A000 |  |  |
| COMPANY CODE | 3310 |  |  |
| G/L ACCOUNT | 1100100029500000 |  | G/L account for bank account.A G/L account for allocation clearing must be available. Use your specific clearing GL or create demo data 29500000 per instructions in Create G/L Account and Cost Element - MDS (BNG) script. |
| COST CENTER | 33101902,33101101,33101321,33101301,33101750,33101401,33101601 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDSNote As of the 2502 edition, the standard hierarchy set-based group 0001 has been replaced with global hierarchy 1~ for new installations. See the Create Cost Center and Cost Center Group - MDS (BNM) script for more details. |
| BNG | Create G/L Account and Cost Element - MDS |
| BNN | Create Activity Type and Activity Type Hierarchy - MDS |
| 2US | Create Universal Allocation Master Data - MDS |
| 3KW | Create CO Cost Rates - MDS |

### Preliminary Steps

#### User Settings - Set Controlling Area

Purpose

The controlling area must be set before you carry out the first steps in controlling.

Procedure

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Choose User Preferences | Choose the user icon on the top right corner of the screen, and choose Settings.Choose Default Values. | The Default Values dialog box displays. |  |
| 3 | Enter Data | On the CO Area field,enter the following value: A000.Choose Save. | Controlling area A000 is set for your user. |  |

#### Set Report Relevancy

Purpose

The first time you execute a design studio report. you must set report relevancy. If you make a subsequent change in cost center, profit center, or G/L hierarchy, perform this step again to get the latest information.

Also, you must manually replicate set-based hierarchies (such as Cost Center Group or Profit Center Group) and financial statement hierarchies to the backend database hierarchy tables. Normally, this is created as a periodic job that runs in the background.

Procedure

| Step # | Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Set Report Relevancy - Set-Based Hierarchies (F5295). | The Set Report Relevancy for Set-Based Hierarchies screen displays. |  |
| 3 | Enter Header Data | In the header area, make the following entries and choose Go:Set Class: <For example, 0101 for the cost center group>Organizational Unit: A000Set Name: A000Include Subnodes: YesNote This step is mandatory for budget use. |  |  |
| 4 | Mark as Report-Relevant | Select the row and choose Edit. In Report-Relevant, select Yes and choose Save. |  |  |
| 5 | Enter Data for another Set Class | Repeat steps 3 and 4 using the following values:Set Class: <For example, 0102 for the cost element group>Organizational Unit: YCOASet Name: YBA000_CEInclude Subnodes: Yes |  |  |

#### Replicate Runtime Hierarchy

Purpose

You must manually replicate set-based hierarchies (such as Cost Center Group or Profit Center Group) and financial statement hierarchies to the backend database hierarchy tables. Normally, this would be created as a periodic job that would run in the background.

Procedure

| Step # | Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Overhead Accounting Jobs (F3767). | The Application Jobs screen displays. |  |
| 3 | Create | Choose the Create button. | The New Job: Replicate Runtime Hierarchy (SAP) view displays. |  |
| 4 | Header Data for Hierarchy ID 0101/A000/A000 | In the header area, make the following entries and choose Schedule:Job Template: Replicate Runtime Hierarchy (SAP)Job Name: <Enter a text>Choose the Step 2 button.Start Immediately: SelectChoose the Step 3 button.In the Create Hierarchy area, make the following entry:Hierarchy ID: 0101/A000/A000Note If you are using the optional procedure Commitment Management and Cost Center Budgeting, follow steps 1-4, but make the following entries instead:Job Template: Manually Replicate Runtime HierarchyHierarchy ID: 0102/YCOA/YBA000_CE |  |  |
| 5 | Hierarchy ID YPS2 | Repeat the above steps using hierarchy ID YPS2. |  |  |

#### Maintain Currency Exchange Rate to Global Currency

Use

In this activity, you can maintain currency exchange rate to global currency.

You can maintain currency exchange rates for the following:

- Primary Posting: From company code currencies to global currency (M rate)
- Secondary Posting: From global currency to company code currencies (P rate)

The M and P rates must be entered for the controlling area and all company codes' currency combinations. Note that any additional company currencies must also be maintained via the Currency Exchange Rate app.

Prerequisite

Ensure that exchange rates are maintained for both M and P rates for the controlling area and all company codes' currency combinations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Currency Exchange Rates (F3616). | The Currency Exchange Rates view displays. |  |
| 3 | Add an Exchange Rate Entry | Choose Create. | The right pane expands to show the entry fields. |  |
| 4 | Enter Data | Make the following entries and choose Create:Company Code: 3310Fiscal Year: <current fiscal year> | You entered a new exchange rate. |  |

|  |
| --- |
| Note Currency exchange rates can also be uploaded via the Import Foreign Exchange Rates (F2092). For more details, see the scope item Accounting and Financial Close (J58). |

#### Open Cost Accounting Period

Use

The posting period for cost accounting must be open.

Prerequisites

Check and ensure that the cost accounting period is open for the period you are working.

|  |
| --- |
| Note For more details on this step, see the Manage Posting Periods step in Accounting and Financial Close (J58) script. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Posting Periods - Cost Accounting (F4684). | The Manage Posting Periods - Cost Accounting view displays. |  |
| 3 | Check/Open Period | Make the following entries and choose Go:Company Code: 3310Fiscal Year: <current fiscal year> | Controlling posting period is now open. |  |

#### Create a Statistical Key Figure

Purpose

Statistical key figures are measurable values or weighting factors which can be applied to cost centers, profit centers, internal orders or business processes. SAP statistical key figures are also used for analysis purposes like calculation of rent cost per employee of a company.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Statistical Key Figures (F1603A). | The Manage Statistical Key Figures view displays. |  |
| 3 | Create Statistical Key Figure | Choose Create. Make the following entries and choose Create:Statistical Key Figure: Z10, for exampleQuantity Unit: PC, for exampleStatistical Key Figure Name: <Enter a text>Category: 1 | The statistical key figure is created. |  |

#### Optional: Posting Scheme for Intercompany Clearing

Purpose

With this configuration setting, you can choose whether P&L accounts or Balance Sheet accounts are utilized for Intercompany (ICO) clearing. This setting is relevant for ICO postings such as activity allocation/time recording, universal allocation, travel expenses (including Concur postings and supplier invoices), and CO reporting.

|  |
| --- |
| Note If this setting is not enabled, the default P&L logic applies, which uses the non-operating G/L. |

Prereqisite

G/L accounts and the corresponding clearing accounts must be maintained.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Search for Intercompany Clearing Accounts (107107).
6. For the displayed row, choose Details (>).
7. For the Define Posting Scheme for Intercompany Clearing Accounts row, choose Configure.
8. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Define Posting Scheme for Intercompany Clearing Accounts activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entry | Scheme: <Select X B/S Account or N P&L Account (Non operating)> |  |  |
| 2 | Alternative Scheme for Selected Company Codes | You can also specify the account type to be used based on the company code. Choose Review and then Save.If you select the P&L account, follow the procedure from the next topic [Optional: Map CO Intercompany Accounts](#unique_13) [page ] 13.ORIf you select the balance sheet account, use the Automatic Account Determination SSCUI to map G/L account:Area: Financial AccountingSub Area: General Ledger AccountingProcess: Prepare Intercompany TransactionsChoose Step 2.Transaction Key: BULPosting Between: <Select a company code>And: <Select a company code that is different from the above> |  |  |

#### Optional: Map CO Intercompany Accounts

Purpose

Intercompany controlling postings are supported.

|  |
| --- |
| Note This step should only be used if you need to do intercompany allocations or posting. You must map the accounts you are using and assign a relevant clearing account. |

Prereqisite

G/L accounts and the corresponding clearing accounts must be maintained.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: General Ledger

1. For the row with Item Name of Chart of Accounts, choose Details (>).
2. For the displayed row, choose Details (>).
3. For the Automatic Account Determination row, choose Configure.
4. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Automatic Account Determination activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Step 1: Area | Make the following etries and choose Step 2:Area: ControllingSubarea: Cost Center AccountingProcess: Assign Intercompany Clearing Accounts for Actual Postings |  |  |
| 2 | Step 2: Parameters | Make the following entry and choose Step 3:Chart of Accounts: YCOA |  |  |
| 3 | Step 3: Account Assignments | Select for example, the line containing the GL 65000000 and map the GL account 68888800 to the Clearing Account - Debit and to the Clearing Account - Credit.Choose Review and then Save. |  |  |

#### Optional: Updating Cost Center Budget Profiles (Only Required When Using Cost Center Budget Functionality)

Purpose

- The default content comes with budget profile CC001- Cost Center Budget and mapped to sample groups for travel cost and material. The customer must either adopt this profile or create new as per your requirement.

|  |
| --- |
| Caution Adjustments to the budget profile CC001 has to be adapted for your specific company requirements prior to any budget-relevant postings. Retroactively capturing budget-relevant postings is not possible. |

1. Cost Center Budget availability control is at G/L account group (unlike Project this is not linked to FSV and semantic Tags)
2. G/L account group can be created either via the Edit Cost Element Groups app or the Manage Global Accounting Hierarchies - GL Account Hierarchy app.
3. All the G/L account group assigned to a particular budget profile should be part of same G/L account Hierarchy (top node of groups).
4. To actively use hierarchy created via Edit Cost Element Groups app in customizing, the prerequisites to set report relevancy via Set Report Relevancy - Set-Based Hierarchies (F5295) app (for example, for default content set class 0102, org YCOA, set name YBA000-CE and Include sub-node), and replicate runtime hierarchy (example for default content 0102/YCOA/YBA000_CE) must be carried out. The default content comes with GL Hierarchy YBA000_CE and customer can assign any groups to this as per their requirements and edit the predefined profile CC001- Cost Center Budget.

|  |
| --- |
| Note Make sure to always replicate runtime hierarchy after any change to the existing hierarchy to reflect the change and before mapping the groups in this step. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Overhead Cost Management

1. For the row with Item Name of Budget Management, choose Details (>).
2. For the displayed row, choose Details (>).
3. For the Maintain Budget Availability Control Profile for Cost Centers row, choose Configure.
4. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Maintain Budget Availability Control Profile for Cost Centers activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Change Entry of the Identified combination | Select the entry with profile CC001 and double-click Account Group. Go to New Entries on the top menu and add the cost element groups and hierarchy. | All the G/L account groups assigned to a particular budget profile should be part of the same G/L account hierarchy (top node of groups). |  |
| 2 | Change/Add Tolerance Limits for Each Group | Choose the G/L Account Hierarchy line and double-click Tolerance Limit and make the entry as per your requirements.You can delete the tolerance limits that you created. |  |  |
| 3 | Save | Save the entries. |  |  |

#### Optional: Currency Conversion Settings for Activity Allocation

Purpose

This configuration setting provides flexible options for currency conversion in direct activity allocation. By default, the system uses the P‑rate and the exchange rate valid on the first day of the fiscal year. However, using this SSCUI, you can adjust the setting so that the current exchange rate at the time the activity is posted is applied. This ensures that acitivty postings follow the same exchange-rate logiv used in regular financial transactions.

Prerequisite

G/L accounts and the corresponding clearing accounts must be maintained.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Search for Intercompany Clearing Accounts (107337).
6. For the displayed row, choose Details (>).
7. For the Currency Conversion Settings for Activity Allocation row, choose Configure.
8. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Automatic Account Determination activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entry | Select G/L conversion. | With this change, the exchange rate applicable at the posting time is used. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Record Costs

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [General Entries With Cost Center](#unique_17) [page ] 21 | General Ledger Accountant | Post General Journal Entries (F0718) | General Ledger Account Document is entered and saved. |

Transaction Based Allocations/Periodic Postings

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Direct Activity Allocation](#unique_18) [page ] 23 | Cost Accountant - Overhead | Manage Direct Activity Allocation (F3697A) | Direct activity allocations are posted. |
| [Post Statistical Key Figures](#unique_19) [page ] 24 | Cost Accountant - Overhead | Manage Statistical Key Figure Values - New Version (F3915A) | Statistical transaction-based key figures are posted. |
| [View Posted Statistical Key Figures](#unique_20) [page ] 26 | Cost Accountant - Overhead | Manage Statistical Key Figure Values - New Version (F3915A) |  |

| Process Step | Business role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Repost Line Items - Cost Accounting](#unique_21) [page ] 26 | Cost Accountant - Overhead | Repost Line Items - Cost Accounting (F5549) | The posting is complete. |
| [Reassign Costs and Revenues](#unique_22) [page ] 27 | Cost Accountant - Overhead | Reassign Costs and Revenues (F2009A) | Costs are reassigned to another cost center. |
| [Execute Overhead Allocation Cycle](#unique_23) [page ] 29 | Cost Accountant - Overhead | Run Allocations (F3548) | General Ledger Account Document is entered and saved. |
| [Allocation Results](#unique_24) [page ] 31 | Cost Accountant - Overhead | Allocation Results (F4363) | The existing allocation results can be reviewed after a successful run. |
| [Allocation Flow](#unique_25) [page ] 32 | Cost Accountant - Overhead | Allocation Flow (F4022) | Allocation flow diagram is displayed. |
| [Execute Profit Center Distribution](#unique_26) [page ] 33 | Divisional Accountant | Manage Allocations (F3338A) | Balance sheet account balances to and from various profit centers are distributed. |

Analytics

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Cost Centers Actual Data Reporting](#unique_27) [page ] 35 | Cost Accountant - Overhead | Cost Centers - Actuals (F0963) | Actual figures for cost centers can be displayed in the reporting with different dimensions for navigation. |
| [Cost Center Comparisons - Review Booklet](#unique_28) [page ] 36 | Cost Accountant - Overhead | Cost Centers - Review Booklet (F7763) | A report showing year-to-date comparison for selected company code, cost center hierarchy, and G/L account hierarchy combination displays. |
| [Commitments by Cost Center](#unique_29) [page ] 37 | Cost Accountant - Overhead | P&L - Plan/Actual/Committed (W0170) | A report showing plan, actual, and commitments for the cost object displays. |
| [Where-Used List - Cost Centers Actual](#unique_30) [page ] 38 | Cost Accountant - Overhead | Manage Cost Centers - New Version (F1443B) | A report showing where cost centers are currently used is displayed. |
| [Where-Used List - Statistical Key Figures](#unique_31) [page ] 39 | Cost Accountant - Overhead | Where-Used List - Statistical Key Figures (F4078) | A report showing where the statistical key figures are currently used is displayed. |
| [Display Line Items in Controlling](#unique_32) [page ] 40 | Cost Accountant - Overhead | Display Line Items - Cost Accounting (F4023) | A report showing the posting details is displayed. |
| [View Profit Center Distribution](#unique_33) [page ] 40 | Divisional Accountant | Profit Centers - Plan/Actual (W0079) | Using the report filters on profit centers, you can see the allocations. |

Table 2: OPTIONAL: Commitment Management and Cost Centers Budgeting

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Exclude Cost Center Data for Commitment Management](#unique_34) [page ] 42 | Cost Accountant - Overhead | Manage Cost Centers - New Version (F1443B) | Includes cost center data for commitment management reporting. |
| [Create Purchase Order](#unique_35) [page ] 43 | Purchaser | Create Purchase Order - Advanced (ME21N) | Creates the demo data to view the commitments in reporting. |
| [Commitment Management by Cost Center](#unique_36) [page ] 44 | Cost Accountant - Overhead | Commitments by Cost Center (F3016) | Allows visibility of purchase order commitments to be viewed by cost center and cost elements. |
| [Set Cost Center Master Budgeting Parameters](#unique_37) [page ] 46 | Cost Accountant - Overhead | Manage Cost Centers - New Version (F1443B) | Includes cost center data for budgeting. |
| [Template for File Upload](#unique_38) [page ] 47 | Cost Accountant - Sales | Import Financial Plan Data (F1711) | Downloads the template and prepare your plan data for upload. |
| [Import Financial Data](#unique_39) [page ] 48 | Cost Accountant - Sales | Import Financial Plan Data (F1711) | Opens the Import P&L Plan Data app and select a source file. |
| [Create Purchase Order](#unique_40) [page ] 50 | Purchaser | Create Purchase Order - Advanced (ME21N) | Creates the demo data to view the commitments in reporting. |
| [View Budget by Cost Center](#unique_41) [page ] 51 | Cost Accountant - Overhead | Cost Center Budget Report (F3871) | Allows visibility of purchase order commitments to be viewed by cost center and cost elements. |
| [Transfer Cost Center Budgets](#unique_42) [page ] 52 | Cost Accountant - Overhead | Manage Cost Center Budgets (F4307) | Transfers cost center budget from one general ledger/cost center combination. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Record Cost

#### General Entries With Cost Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To successfully demonstrate assessments there must be accounting documents posted directly on the sender cost center account to allocate values to the receiver cost center account. Therefore, G/L accounting documents must be posted in the SAP system prior to executing the assessment cycles.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a General Ledger Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Post General Journal Entries (F0718). | The Post General Journal Entries screen displays. |  |
| 3 | Enter Header Data | In the header area, make the following entries:Journal Entry Date: <Current Date>Posting Date: <Current Date>Period: <current period>, for example, 03Journal Entry Type: SA (G/L Account Document)Company Code: 3310Transaction Currency: AED | The account document is posted. The system automatically adds the input tax amount. |  |
| 4 | Enter Data | In Line Items (2), make the following entries and press Enter:Company Code: 3310G/L Account: 63005000Debit: <amount> for example, 10000Note Make the entry in the debit or credit column as appropriate.Tax Code: <Input Tax Code>Cost Center: 33101750 |  |  |
| 5 | Enter Second Line Item Detail | In Line Items (2), add another line by selecting the Add Line Item icon at the bottom right and press Enter:Company Code: 3310G/L Account: 11001000Credit: <amount> for example, 10000Note Total Debit amount shown (that is, Debit Amount + Tax Rate amount, based on the tax code entered)Next, make the following entries:Value date: <Current date>House Bank: AEBK1House Bank Account: AEAC1Note The value date is required for cash accounts. |  |  |
| 6 | Save | Choose Post. Make a note of the document number: __________ |  |  |
| 7 | New Cost Center and Amount | Repeat steps 3 to 8 with cost center 33101201 and credit/debit amount 2000. |  |  |

### Transaction Based Allocations/Periodic Postings

#### Direct Activity Allocation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Direct activity allocations can also be done instead of assessments depending on your business needs. The following steps create an activity reallocation directly from one cost center to another with the document posted in the SAP system. Additionally, you can also repost, copy, and reverse activity allocation postings.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Direct Activity Allocation (F3697A). | The Manage Direct Activity Allocation view displays. |  |
| 3 | Create Object | Choose the Create button. | The New Object view displays.Note If you wish to perform a posting correction with reference prior to selecting create, first enter the reference journal entry number in the Journal Entry field of the Header section. Choose Go and then Repost. |  |
| 4 | Enter Header Information | In the Header Information area, make the following entries and press Enter:Document Header Text: <Enter some text>Journal Entry Date: <Current date>Posting Date: <Current date>Journal Entry Type: CO |  |  |
| 5 | Enter Allocation Items | In the Allocation Items area, make the following entries and choose Create:Sender Cost Center: 33101321Sender Activity Type: 8Receiver Cost Center: 33101301Quantity: 5Note If these fields are not already displayed, choose the Additional Options (…) button, and then use the dropdown to select Show More per Row. |  |  |
| 6 | Document number | Write down the document number for the subsequent transactions.Note To view more details and review the postings, see Display Line Items - Cost Accounting app. | The documents are posted. |  |

|  |
| --- |
| Tip To reverse activity allocations, use the Reverse button, and choose Create to post. |

|  |
| --- |
| Note For details on activity types, refer to Create Activity Type and Activity Type Hierarchy - MDS (BNN). |

#### Post Statistical Key Figures

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can post statistical key figures. You can enter statistical key figures for use in reporting or as tracing factors for period-based allocations. This also occurs within a transaction-based allocation in Controlling.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Statistical Key Figure Values - New Version (F3915A). | The Manage Statistical Key Figure Values screen displays. |  |
| 3 | Enter Actual Data | Choose Create and make the following entries:Document Header Text: <any>Document date: <Current date>Posting date: <Current date>Item section: Line 1Receiver Cost Center: 33101902Statistical Key Figure: 1002Statistical Quantity: 100Choose Add and make the following entries:Item section: Line 2Receiver Cost Center: 33101901Statistical Key Figure: 1002Statistical Quantity: 50Note If you have no service scope installed, and cost centers are not available, you can use cost centers 33101201 and 33101302.Note To upload supporting documents for Statistical Key Figure posting for cost centers, use the Attachments tab. |  |  |
| 4 | Save | Choose Create. | Statistical key figures are posted. Note the document number is listed on top of the window. |  |

#### View Posted Statistical Key Figures

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can view your posted statistical key figures.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Statistical Key Figure Values - New Version (F3915A). | The Manage Statistical Key Figure Values screen displays. |  |
| 3 | View Statistical Key Figures | Make the following entries and choose Go:Posting Date: <Choose a time period>Fiscal Year: <Current year> | The Statistical Key Figure Values appear. |  |

|  |
| --- |
| Tip To reverse statistical key figure postings or view posted documents, use the Manage Statistical Key Figure Values - Deprecated (F3915) app. Only category type 2 (totals value) SKF postings can be reversed. |

### Repost Line Items - Cost Accounting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity demonstrates how to repost line items within a company code. There will be a connection created between the original FI document and the correction made in this CO posting. No cancellation of the original FI document is needed.

Prerequisites

Initial posting must exist on the G/L account and cost center. Therefore, perform the steps in the Record Cost section and make a note of the document number.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Repost Line Items - Cost Accounting (F5549). | The Repost Line Items - Cost Accounting view displays. |  |
| 3 | Select Document | In the Standard section, make the following entries and choose Go:Journal Entry: <enter the document number created via the Record Cost Section>Select the document number and choose Repost. | The Repost Line Items - Cost Accounting screen displays. |  |
| 4 | Repost Line Item | In the Items section, select the Account for Allocation line.In the Cost Center field, enter any other cost center than the one already posted. | The cost center assignment is changed. |  |
| 5 | Create | Choose Create. | The posting is complete. |  |

### Reassign Costs and Revenues

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity demonstrates how to reassign costs and revenues within a company code. The reassignment only occurs within controlling and is not directly tied to a specific FI document posting.

Prerequisites

Initial posting must exist on the G/L account and cost center. Therefore, the steps from Record Cost section must be done first. Repeat the steps with G/L 61003000 and cost center 10101101.

|  |
| --- |
|  |

To prevent errors during ICO (intercompany) postings, ensure the maintenance of the ICO clearing account for ICO transactions such as reassign cost and revenues, activity allocation/time recording, universal allocation, and travel expenses (including Concur postings and supplier invoices). This can be done by assigning intercompany clearing accounts for actual postings via SSCUI 100297. To decide whether ICO clearing occurs via a P&L account (default is non-operating G/L) or Balance Sheet, and map CO intercompany accounts accordingly., refer to the [Optional: Posting Scheme for Intercompany Clearing](#unique_12) [page ] 11 step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reassign Costs and Revenues (F2009A). | The Reassign Costs and Revenues view displays. |  |
| 3 | Input Initial Screen | Choose Create and in the Header Information section, make the following entries:Document Header Text: <any>Journal Entry Date: <today’s date>Posting Date: <today’s date>Translation Date: <today’s date>In the Assignment Items section, make the following entries:Account for Allocation: <for example, 61003000>Sender Cost Center: for example, 33101101Receiver Cost Center: for example, 33101750Amount in Transaction Currency: <for example, 1000>Note If the field is not in view, choose the Show more per row button located in the upper right corner.Translation Currency: AEDDocument Header Text: <any>Choose Create. | Costs are reassigned to another cost center. |  |

### Execute Overhead Allocation Cycle

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you execute an assessment cycle (Cost Center). Both cost centers and work breakdown structure elements can be used as receivers in the assessment cycle. In this example, cost center as receiver is demonstrated.

Prerequisite

Plan and actual assessment cycle demo data has been created for testing. For details on how to create your own plan and actual assessment cycle defining senders and receivers, see the Create Universal Allocation Master Data - MDS(2US) script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Run Allocations (F3548). | The Run Allocations view displays. |  |
| 3 | Manage Allocations | Choose the Manage Allocations button. | The Manage Allocations view displays. |  |
| 4 | Input Initial Screen | Make the following entries and choose Go:Allocation Context: Cost CentersAllocation Cycle: OA33200Note If you created alternative manufacturing-based statistical key figures in the previous step, run allocation cycle OA33300.Company Code: 3310Allocation Type: Overhead AllocationLedger: 0L | The assessment is done. |  |
| 5 | Select Allocation Cycle | Select the allocation cycle row and choose the Run button. | The Run Allocations screen displays. |  |
| 6 | Test Run | Select the allocation cycle row and choose the Test Run button. | The Run Allocation(s) - Test Run screen displays. You get a success message. If everything looks correct, you can repeat the steps above and choose Run instead of Test Run. |  |
| 7 | Input Values | Make the following entries, choose Validate and then Run.Test Run Name: <enter your desired value>Ledger: 0LFiscal Period From: <current period and year>Fiscal Period To: <curent period and year>Note To review the results, choose the Display Run Result link in the following dialog box for the related run. You can alternatively choose Close, and then choose the Allocation Results button to check the related results. | If you wish to view this posted allocation in the Allocation Flow process step, repeat step 5. Select the allocation cycle row and choose the Run button. |  |

|  |
| --- |
| Tip To reverse an assessment posting, use the app Allocation Results (F4363), enter the search criteria and choose Go. Select the allocation cycle job and choose Reverse Run. |

### Allocation Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, existing allocation results can be reviewed after a successful run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Allocation Results (F4363). | The Allocation Result view displays. |  |
| 3 | Enter Values in Search | Make the following entries and choose the Go button:View Type: Run |  |  |
| 4 | Select the Run | Select the allocation you had executed in the previous step and choose the Details button on the right of the screen. | An overview detail of the allocation executed can be seen via the various tabs. |  |
| 5 | View Network Graph | In the same view, choose the Network Graph button on the right of the screen. | The graphical view of the data displays. |  |
| 6 | Change Grouping View | To further refine the views, choose the Group By button.For example, in the Group by window, make the following entry:First Level: Functional Area |  |  |

### Allocation Flow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can review the overhead allocation flows from a single cost center or see the accounts from a T account point of view.

Prerequisites

- The assessment cycle demo data has been created for testing. For details on how to create your own plan assessment cycle defining senders and receivers, see the Create Universal Allocation Master Data - MDS (2US) script.
- The related postings have been made.
- The cycle must be successfully run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Allocation Flow (F4022). | The Allocation Flow view displays. |  |
| 3 | Input Initial Screen | Make the following entries and choose the Go button:View Type: Cost CenterCompany Code: 3310> Cost Center: 33101750Fiscal Period: <current period, for example 09>Fiscal Year: <Current year>Actual/Plan: ActualLedger: 0L | The flow diagram is displayed. Alternatively, you can select the T icon to see the T account point of view. |  |

### Execute Profit Center Distribution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Using profit center distribution, it is possible to distribute balance sheet account balances to and from various profit centers.

Prerequisites

1. A G/L account for allocation clearing must be available. Create G/L 29500000 CO Allocation Clearing using the GL 29500100 as reference. For details on how to create the G/L, refer to Create G/L Account and Cost Element - MDS (BNG) script.
2. Assign splitting rule via configuration activity Define Document Splitting Characteristics for Controlling for copying values from 29500100 to 29500000.
3. Plan and actual assessment cycle demo data has been created for testing. For details on how to create your own plan and actual assessment cycle defining senders and receivers, see the Create Universal Allocation Master Data - MDS (2US) script. You can do a mass upload of allocation cycles for creation of new allocations and/or new segments via Manage Allocations - Deprecated (F3338) app and use Upload Cycles button. You can either download a blank template or select an existing allocation cycle to download as template.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Divisional Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Allocations (F3338A). | The Manage Allocations view displays. |  |
| 3 | Input Initial Screen | Make the following entries and choose the Go button:Allocation Context: Profit CentersAllocation Cycle: OAPCD33Company Code: 3310Allocation Type: DistributionLedger: 0L | The assessment is shown. |  |
| 4 | Review Allocation Cycle | Do the following:Select the allocation cycle row and choose the > sign.In the Manage Allocations view, choose the Segments tab and choose Edit.Select the segment row and choose the > sign. Review segment tabs (Rules, Senders).Choose the Sender Basis tab and change the amount to 1000.Choose the Check Segment button.Choose the Save button. |  |  |
| 5 | Run Allocation | Select the allocation cycle row and choose the Run button. | The Run Allocations screen displays. |  |
| 6 | Test Run | Select the allocation cycle row and choose the Test Run button. | The Run Allocation(s) - Test Run screen displays. |  |
| 7 | Input Values | Make the following entries, choose the Validate button, and then choose the Run button.Test Run Name: <enter your desired value>Ledger: 0LFiscal Period From: <current period and year>Fiscal Period To: <curent period and year>Note When you are ready to do the actual (live) run, in the Journal Entry Type, enter SA. | To review the results, choose the Display Run Result link in the following dialog box for the related run. You can alternatively choose Close, and then choose the Allocation Results button to check the related results. |  |

|  |
| --- |
| Tip To reverse an assessment posting, use the app Allocation Results (F4363), enter the search criteria and choose Go. Select the allocation cycle job and choose Reverse Run. |

|  |
| --- |
| Tip Allocation runs can be scheduled in advance or based on regular intervals. See the Schedule Allocation Run in Universal Allocation (2QL). |

### Analytics

#### Cost Centers Actual Data Reporting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the cost centers actual data reporting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Cost Centers - Actuals (F0963). | The Prompts dialog box displays. |  |
| 3 | Selection Criteria | Make the following entries:Ledger:<0L>Ledger Fiscal Year :<Current year>Company Code: 3310Key Date: <today's date> |  |  |
| 4 | Go | Choose Go. | A report showing actual costs for the cost centers is displayed.Note If you encounter an error stating Chart cannot be rendered: Multiple units for measure REF_QV_CELL_4, refer the SAP Knowledge Base Article [3331443](https://userapps.support.sap.com/sap/support/knowledge/en/3331443). This is a known issue and can be ignored. |  |

#### Cost Center Comparisons - Review Booklet

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can run reports to view year over year comparisons for selected company codes, cost center hierarchy, and G/L account hierarchy combinations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Cost Centers - Review Booklet (F7763). | The Cost Center - Review Booklet dialog box displays. |  |
| 3 | Selection Criteria | Make the following entries and choose Go:Ledger:<0L>Reporting Date: <today's date>Company Code: 3310Cost Center Hierarchy: <use the dropdown to select 0101/A000/A000>Tip To view both the key and description, select the dropdown menu in the field and change the Display setting to ID and Description.G/L Account Hierarchy: <use the dropdown to select 0102/YCOA/YBA000_CE> | A report showing year-to-date comparison for selected company code, cost center hierarchy, and G/L account hierarchy combination displays.Note The Review Booklet includes reports on cost center actuals, plan vs. actuals, and budgets. |  |

#### Commitments by Cost Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This report shows the plan, actual, and committed data to be viewed by cost center and cost elements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open P&L - Plan/Actual/Committed (W0170). | The P&L - Plan/Actual/Committed screen displays. |  |
| 3 | Selection Criteria | Make the following entries and choose Go:Key Date: <today's date>Ledger:0LPlan Category: PLNFiscal Year of Ledger: <Current fiscal year>G/L Account Hierarchy: 0102/YCOA/YBA000_CECompany Code: 3310Cost Center: <enter your desired cost center> | A report showing plan, actual, and commitments for the cost object displays. |  |

#### Where-Used List - Cost Centers Actual

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity allows you to see where the cost centers are used in other master data such as activity type, profit centers, and actual cost allocations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Cost Centers - New Version (F1443B). | The Manage Cost Centers screen displays. |  |
| 3 | Selection Criteria | Make the following entry and choose Go:Cost Center: <your cost center> |  |  |
| 4 | Where Used | Select the desired cost center and choose Where Used.Select one option from the dropdown list. For example, In All Objects. | A report showing where the cost centers are currently used displays. For details, you can select the master data object type and drill in further. |  |

|  |
| --- |
| Note The Where-Used List - Cost Centers (F3549) app can also be used to determine where the cost centers are currently used. |

#### Where-Used List - Statistical Key Figures

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity allows you to see where the statistical key figures are used.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Where-Used List - Statistical Key Figures (F4078). | The Where-Used List - Statistical Key Figures view displays. |  |
| 3 | Selection Criteria | Make the following entry and choose Go:Statistical Key Figure : <your statistical key figure> | A report showing where the statistical key figures are currently used displays. For details, you can select the relevant master data object type and drill in further. |  |

#### Display Line Items in Controlling

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity allows you to view various postings in controlling.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Line Items - Cost Accounting (F4023) app. | The Display Line Items view displays. |  |
| 3 | Selection Criteria | Make the following entry and choose Go:Ledger : <Enter your ledger, for example 0L>Company Code: 3310Posting Date: <This Year> or choose Adapt Filters to include the Fiscal Year field into the filter bar and enter the current year. | A report showing the posting details display. |  |

#### View Profit Center Distribution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you view the profit center distribution.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Divisional Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Profit Centers - Plan/Actual (W0079). | The Profit Center - Plan/Actual view displays. |  |
| 3 | Selection Criteria | Make the following entries:Ledger: <0L>Fiscal Year of Ledger: <Current year>Plan Category: ACT01Key Date: <Current date>Company Code: 3310 |  |  |
| 4 | Choose | Choose Go. | Using the report filters on profit centers, you can see the allocations. |  |

### OPTIONAL: Commitment Management and Cost Center Budgeting

#### Commitment Management Cost Centers Actual Data Reporting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note This section is only applicable if you select the non-standard scope item 2I3 - Predictive Commitments Management. You have additional features in cost centers to view commitment which comes via purchasing.Commitment management is part of the cost monitoring process. Commitment management line items are triggered by stock and non-stock expense purchase requisitions and/or purchase orders that utilize cost centers. These commitments are updated in Extension Ledger 0E (predelivered) in ACDOCA table. Commitments are reduced by various business transactions such as goods receipt. |

Prerequisites

- To use commitment management functions, a nonstandard scope item 2I3 - Predictive Commitments Management must be selected and activated. Once activated, commitment management ledger 0E is active and applicable for all company codes and countries.
- Master Data requirement: Specific cost centers relevant for your commitment tracking must be unlocked. See the procedure on [Exclude Cost Center Data for Commitment Management](#unique_34) [page ] 42.
- To view commitments in the report, an open purchase order and/or requisition must exist. For details on creating purchase orders, refer to Consumable Purchasing (BNX).

##### Exclude Cost Center Data for Commitment Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to exclude cost center data from commitment management reporting. If you select the lock on the cost center master data, consumable purchases that utilize the cost center are excluded from the report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Open Manage Cost Centers | Open Manage Cost Centers - New Version (F1443B). | The Manage Cost Centers view displays. |  |
| 3 | Cost Center | Make the following entry and choose Go:Cost Center: 33101501Select the line item with Cost Center and choose the (>) Details button. |  |  |
| 4 | Lock Commitment Updates | Choose the Edit button on the top row. In the Control section, select the Lock Commitment Updates to see the ON sign.Choose the Save button on the bottom right of your view. | When the Lock Commitment Updates is set to On, no further updates for this cost center would be shown in the commitment report. |  |

##### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This prerequisite activity creates the demo data to view the commitments in reporting.

|  |
| --- |
| Note For details on consumable purchasing, refer to Consumable Purchasing (BNX), steps Create Purchase Requisition or Create Purchase Order. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Purchase Order | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order view displays. |  |
| 3 | Start Purchase Order creation | Make the following entries and choose Enter:Supplier : 33300001 | The Create Purchase Order view displays. |  |
| 4 | Enter Purchase Order data | Make the following entries and choose Enter.Org. Data:Purch. Org.:3310Purch. Group:001Company Code: 3310 | The Create Purchase Order view displays. |  |
| 5 | Enter Additional Details | Make the following entries and choose Enter:A: (Account Assessment Category): K (Cost center)Material: TG0011PO Quantity:1Net Price: 450Plnt: 3310Stor. Location: 331AIn the next section, enter the following and choose Enter:Cost Center:33101401 | The Create Purchase Order view displays. |  |
| 6 | Save the entries | Choose the Save button to save the purchase order. | The Purchase Order is created. |  |

##### Commitment Management by Cost Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This report allows visibility of purchase order commitments to be viewed by cost center and cost elements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Commitments by Cost Center (F3016). | The Commitments by Cost Center (F3016) view displays. |  |
| 3 | Selection Criteria | Make the following entries and choose Go:Ledger: 0LPlan Category: PLNCompany Code: 3310Fiscal Year: <Current year> | A report showing commitments on the purchasing side for the cost centers is displayed. |  |

#### Cost Center Budgeting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note This section is applicable only if you select non-standard scope item Predictive Commitments Management (2I3), which is also a prerequisite for budgeting. With this feature, you gain additional capabilities in cost centers for viewing commitments and budgets, allowing you to effectively monitor your expenses.Budgeting is a part of the cost monitoring process. Commitment management line items in SAP S/4HANA Cloud Public Edition are triggered by expense purchase requisitions and/or purchase orders that utilize cost centers and a material master. These commitments are updated in the Extension Ledger 0E (predelivered) in the ACDOCA table. Commitments are reduced by various business transactions, such as goods receipts.Cost Center Budget availability control is managed at the G/L account group level (unlike Projects, this is not linked to FSV and semantic tags). Cost Center Budgeting utilizes profile CC001, which allows you to assign a G/L account hierarchy and G/L account group to specify the general ledger accounts applicable for your cost center budgets. The default content utilizes G/L account hierarchy YBA000_CE and two G/L account groups: 1200_CE Production Costs Materials and 1900_CE Travel Costs.Once you create your G/L account hierarchy and G/L account groups, you must perform the Set Report Relevancy and Replicate Runtime Hierarchy steps as covered in the Preliminary Steps section of this document. |

Prerequisites

- To use cost center budgeting functions, you must select and activate the nonstandard scope item Predictive Commitments Management (2I3). Once activated, the commitment management ledger 0E becomes active and applicable for all company codes and countries.
- You must perform the Set Report Relevancy and Replicate Runtime Hierarchy steps as mentioned in the Preliminary Steps section of this document.
- To view commitments in the report, an open purchase order or requisition must exist. For details on creating purchase orders, refer to the Consumable Purchasing (BNX) test script.

##### Set Cost Center Master Budgeting Parameters

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to include cost center data for budgeting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Cost Centers - New Version (F1443B). | The Manage Cost Centers view displays. |  |
| 3 | Cost Center 33101601 | Make the following entry and choose Go:Cost Center: 33101601Select the line item with Cost Center and choose the (>) Details button. |  |  |
| 4 | Save the Entries | In the Control section, under Budget Availability Control, choose the Edit button and then make the following entries:Budget-Carrying Cost Center: 33101601Budget Availability Control Profile: CC001Budget Availability Control is Active: ONChoose the Save button on the bottom of the view. |  |  |
| 5 | Cost Center 33101202 | Repeat steps 3 and 4 using cost center 33101202. |  |  |

##### Upload Financial Data

###### Template for File Upload

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity helps you download the template and prepare your plan data for upload. Depending on the scope of your solution, the plan data you fill the template with will differ. You can use the sample data to populate the template. If you have plan data already in your system and would like to copy the data to a new Plan Category, application Copy Financial Plan Data (F3396) can achieve this without the need to manually upload the data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Import Financial Plan Data (F1711). | The Import Financial Plan Data (F1711) view displays. |  |
| 3 | Select Template | Choose the Download Templates button.In the Download Templates view, select the comma as separator and then the Cost Center Budgeting template.Open the downloaded CSV template.Enter the field values as listed in the table below this table. |  |  |
| 4 | Save Template | Save the file in the CSV format. |  |  |

Field Value Table

| CATEGORY | RYEAR | POPER | RBUKRS | RCNTR | RACCT | HSL | RHCUR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Category | General Ledger Fiscal Year | Posting Period | Company Code | Cost Center | Account Number | Amount in Local Currency | Local Currency |
| X | X |  | X | X |  |  |  |
| BUDGET02 | (Current Year) | 3 (Current Period) | 3310 | 33101601 | 61007000 | 1000 | AED |
| BUDGET02 | (Current Year) | 3 (Current Period) | 3310 | 33101601 | 65000500 | 1000 | AED |
| BUDGET02 | (Current Year) | 3 (Current Period) | 3310 | 33101202 | 51600000 | 500 | AED |

###### Import Financial Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once the plan data file is saved in the template, open the Import P&L Plan Data app and select a source file.

The app performs the following checks:

1. The app checks whether the values in the source file are valid. If required, it returns a list of error messages. You must correct the values in the source file until they are all valid before you can proceed.

2. If all values are valid, the app selects the distinct values for all characteristics of the plan data scope (as defined in the third row of the source file).

- If no plan data exists in the system for any combination of these characteristic values, you can directly import the plan data.
- If plan data exists in the system for any combination of these characteristic values, the app displays the affected values. It assumes that you want to completely replace the existing plan data by the new plan data import.

|  |
| --- |
| Note One source file must therefore always contain full plan data sets for a certain combination of the characteristics you specified in the third row (the plan data scope). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Import Financial Plan Data (F1711). | The Import Financial Plan Data (F1711) view displays. |  |
| 3 | Cost Center | Use the Browse button to select the CSV extension file you wish to upload and choose Enter.Make the following entry:Source File: Your .CSV file that contains your plan |  |  |
| 4 | File Check | The upload performs a check to ensure that the format is correct. Correct any error message that appears.To review the data, choose Preview List, and then choose Back. | You are going to see the messages in the upper part of your view. |  |
| 5 | Import Source File | Choose Import Source File. To view the data, choose Display Financial Plan Data. | Import successful message appears. |  |

##### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This prerequisite activity creates the demo data to view the commitments in reporting.

|  |
| --- |
| Note For details on consumable purchasing, refer to Consumable Purchasing (BNX), steps Create Purchase Requisition or Create Purchase Order. |

|  |
| --- |
| Note Purchase line items without a material master using material group are currently not included in Commitments. But during actual posting (goods receipts) the amounts are checked and included in Bugeting. This is shown in the example below. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Purchase Order | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order view displays. |  |
| 3 | Start Purchase Order creation | Make the following entries and choose Enter:Supplier : 33300001 | The Create Purchase Order view displays. |  |
| 4 | Enter Purchase Order data | Make the following entries and choose Enter.Org. Data:Purch. Org.:3310Purch. Group:001Company Code: 3310 |  |  |
| 5 | Enter Additional Details | Make the following entries and choose Enter:A: (Account Assessment Category): K (Cost center)Material: TG0011PO Quantity:1Net Price: 450Plnt: 3310Stor. Location: 331AIn the next section, enter the following and choose Enter:Cost Center:33101601 |  |  |
| 6 | Enter Additional Details in the Next Line | Enter the following:A: (Account Assessment Category): K (Cost center)Description:Office EquipmentMaterial Group: L005OUn: EAPO Quantity:1Net Price: 1000Plnt: 3310Stor. Location: 331AIn the next section, make the following and choose Enter:G/L Account: 61007000Cost Center:33101202 |  |  |
| 7 | Save the entries | Choose the Save button. | The Purchase Order is created. |  |

##### View Budget by Cost Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This report allows visibility of purchase order commitments to be viewed by cost center and cost elements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Cost Center Budget Report (F3871). | The Cost Center Budget Report (F3871) view displays. |  |
| 3 | Selection Criteria | Make the following entries:Plan Category: BUDGET02Company Code: 3310Fiscal Year: <Current year> |  |  |
| 4 | Commit for the Cost Centers | Choose Go. |  |  |

##### Transfer Cost Center Budgets

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity transfers cost center budget from one general ledger/cost center combination.

Prerequisites

- Cost center must have a budgeting profile assigned.
- Cost center budgeting data must be available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Cost Center Budgets (F4307). | The Manage Cost Center Budgets view displays. |  |
| 3 | Initial Entries | Choose Create and from the dropdown, select Budget Transfer.Note Budget Return option can decrease an existing budget and Budget Supplement option can increase an existing budget. | The Budget Document view displays. |  |
| 4 | Create Budget Transfer | Choose the Create button and make the following entries:Posting Date: <enter current date>Plan Category: BUDGET02Document Type: S_BTIn the Sender Items section, make the following entries:Cost Center: 33101601Account Number: 65000500Amount in Company Code Currency: 500In the Receiver Items section, make the following entries:Cost Center: 33101202Account Number: 51600000Amount in Company Code Currency: 500Choose Create. | The budget transfer has now been posted. Note your document number for the next step. |  |
| 5 | Reverse Posting | Go back to the Transfer Cost Center Budgets view. Make the following entry and choose Go:Document Number: <as created in the previous step>On the Budget Transfer Document view, choose Reverse and make the following entries:Document Description: <optional>Reversal Reason: <choose one, for example, wrong posting>Choose Create. | The reversal is successful. The status of the initial posting document changes to Reversed.Additionally, a new document is generated with the status Reversal.The two documents (Reversed and Reversal) should reference each other in the Reversal Reference Number field. |  |

## Appendix

### Cost Center Replication from SAP S/4HANA Cloud Public Edition to SAP Master Data Integration (Optional)

This link describes replication of SAP S/4HANA Cloud Public Edition cost center master data via SAP Master Data Integration to other Cloud applications such as SAP SuccessFactors:[https://help.sap.com/viewer/6b39bd1d0e5e4099a5b65d835c29c696/LATEST/en-US/decbb94c95fa421ead9101e4c43683f7.html](https://help.sap.com/viewer/6b39bd1d0e5e4099a5b65d835c29c696/LATEST/en-US/decbb94c95fa421ead9101e4c43683f7.html).

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
- see-also :: [[06-management-accounting/stammdatenskript-kostenstelle-und-kostenstellengruppe-anlegen-bnm-634]]
- see-also :: [[06-management-accounting/stammdaten-fur-universelle-verrechnung-anlegen-sds-2us-286]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J54_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 89,006 chars in the whole document
