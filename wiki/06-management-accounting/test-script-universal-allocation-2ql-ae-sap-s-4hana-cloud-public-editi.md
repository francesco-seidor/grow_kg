---
id: 06-management-accounting/test-script-universal-allocation-2ql-ae-sap-s-4hana-cloud-public-editi
title: "Test Script: Universal Allocation (2QL_AE) - SAP S/4HANA Cloud Public Edition (2QL_S4CLD2608_BPD_EN_AE)"
description: "S/4HANA Cloud Public Edition 2608 test script for Universal Allocation (2QL_AE): plan data upload, allocation cycles and runs, profit center, intercompany."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/universal-allocation]
aliases: [2QL_S4CLD2608_BPD_EN_AE]
keywords: [Universal Allocation Cycles, universal allocation, test scripts, plan data import, statistical key figures, plan allocation cycles, plan profit center distribution, intercompany allocation, allocation scheduling, allocation groups]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2QL_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-850
topic: 06-management-accounting/universal-allocation
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Universal Allocation (2QL_AE) - SAP S/4HANA Cloud Public Edition (2QL_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2QL_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Universal Allocation Cycles** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Universal Allocation (2QL_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232849848)

[2 Prerequisites 4](#_Toc232849849)

[2.1 System Access 4](#_Toc232849850)

[2.2 Roles 4](#_Toc232849851)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232849852)

[2.4 File Format Requirements 6](#_Toc232849853)

[2.5 Preliminary Steps 8](#_Toc232849854)

[2.5.1 User Settings - Set Controlling Area 8](#_Toc232849855)

[2.5.2 Set Report Relevancy 9](#_Toc232849856)

[2.5.3 Replicate Runtime Hierarchy 10](#_Toc232849857)

[2.5.4 Open Cost Accounting Period 11](#_Toc232849858)

[3 Overview Table 12](#_Toc232849859)

[4 Test Procedures 14](#_Toc232849860)

[4.1 Import Financial Plan Data 14](#_Toc232849861)

[4.1.1 Template for File Upload 14](#_Toc232849862)

[4.1.2 Import File 15](#_Toc232849863)

[4.2 Import Statistical Key Figure Plan Data 17](#_Toc232849864)

[4.2.1 Template for File Upload 17](#_Toc232849865)

[4.2.2 Import Statistical Key Figure Plan Data 18](#_Toc232849866)

[4.3 Execute Cost Center Plan Assessment Cycle of Shared Expenses 19](#_Toc232849867)

[4.4 Allocation Results 21](#_Toc232849868)

[4.5 Allocation Flow 22](#_Toc232849869)

[4.6 Download and Import Allocation Cycles 23](#_Toc232849870)

[4.7 Optional: Simulate Run 24](#_Toc232849871)

[4.8 Execute Plan Profit Center Distribution 25](#_Toc232849872)

[4.9 Optional: Intercompany Allocation 27](#_Toc232849873)

[4.9.1 Record Costs 27](#_Toc232849874)

[4.9.2 Create Allocation Cycle 30](#_Toc232849875)

[4.9.3 Execute Allocation Cycle 32](#_Toc232849876)

[4.10 Optional: Schedule Allocation Run 33](#_Toc232849877)

[4.11 Optional: Working with Allocation Groups 35](#_Toc232849878)

[4.11.1 Create Allocations in Groups 35](#_Toc232849879)

[4.11.2 Run Allocation Groups 36](#_Toc232849880)

[4.12 Optional: Manage Cycle Run Groups 38](#_Toc232849881)

[4.13 Optional: Manage Allocation Changes 39](#_Toc232849882)

[4.14 Analytics 40](#_Toc232849883)

[4.14.1 Allocation Tags 40](#_Toc232849884)

[4.14.1.1 Create Allocation Tags 40](#_Toc232849885)

[4.14.1.2 Assign Allocation Tags 41](#_Toc232849886)

[4.14.2 Plan Data Reporting for Cost Centers 42](#_Toc232849887)

[4.14.3 View Plan Profit Center Distribution 43](#_Toc232849888)

[5 Appendix 44](#_Toc232849889)

[5.1 Situation Handling 44](#_Toc232849890)

[5.1.1 Manage Situation Types 44](#_Toc232849891)

[5.1.2 Manage Teams and Responsibilities 45](#_Toc232849892)

[5.1.3 Finishing Up the Situation Type 46](#_Toc232849893)

## Purpose

|  |
| --- |
| Note Intercompany overhead calculation, settlement, and manual re-postings are supported. Intercompany allocation via Universal Allocation is currently supported with some limitations. |

Overview

The Universal Allocation scope item covers plan and actual allocations. For plan allocations of cost centers in overhead cost controlling, it covers the upload of cost center plan data and the execution of the plan allocation cycles. Annual planning is supported via cost redistribution through defined allocation cycles, by definition of sender and receiver rules by fixed amount and percentage. You can control your costs and compare plan and actual costs by allocating the cost elements to cost centers in overhead cost controlling. For examples of actual allocations, see the Overhead Cost Accounting (J54) test script. Profit centers are also covered.

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
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| Divisional Accountant | SAP_BR_DIVISION_ACCOUNTANT | Divisional Accounting | SAP_BR_DIVISION_ACCOUNTANT |  |
| Cost Accountant - Sales | SAP_BR_SALES_ACCOUNTANT | Sales Accounting | SAP_BR_SALES_ACCOUNTANT |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |

For details about the business role content, refer to the Maintenance of SAP Fiori Artefacts for SAP S/4HANA section in the Check S/4HANA Technical Settings (BG0) configuration guide.

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| OPERATING CONCERN | A000 |  |  |
| CONTROLLING AREA | A000 |  |  |
| COMPANY CODE | 3310 |  |  |
| G/L ACCOUNT | 942010002950000063005000, 63004000, 94222000,94201000 |  | Cost Element used for Buildings & Periodic Service Allocation.A G/L account for allocation clearing must be available. Use your specific clearing GL or use the demo data 29500000.For optional intercompany. |
| COST CENTER | 33101902,33101101,33101301,33101750,33101401,33101601 |  |  |
| PLAN ALLOCATION CYCLE | OP3310 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| 2US | Create Universal Allocation Master Data - MDS |

### File Format Requirements

Format Values:

Plan data must be formatted as a comma separated values file (CSV file).

All organizational units and all master data for which you want to plan must exist in the system.

For the time-dependent organizational units or master data, the following applies :

- It must exist in the period specified in the same data row
- If period 0 is specified, the master data must exist in period 1
- If a special period is specified, the master data must exist in the last normal period of the fiscal year
- If only the fiscal year is provided, the master data must exist at some time during the fiscal year

The source files in this example should use the following values :

- Category, use PLN as default
- Company Code
- Controlling Area
- Ledger
- Cost Center
- Customer Group
- Account Number
- Fiscal Year
- Posting Period (values defined by fiscal year variant)
- Amount in Global Currency
- Global Currency

Decimal Digits :

The amounts may have a currency sign (for example, €). The import cuts it off and reads the currency code from the next column.

The upload accepts only two decimal digits.

The following decimal marks or thousands indicators may be used :

European format:

- Comma (,) as decimal mark
- Point (.) as thousands indicator

For example, 1.234.567,89

US format:

- Point (.) as decimal mark
- Comma (,) as thousands indicator

For example 1,234,567.89

No decimal mark and no thousands indicator (for example, 12345)

Currency As used by the system, for example, EUR instead of €

CSV Files :

The csv-upload supports the following separators :

- , (comma)
- ; (semi colon)
- . (period)
- | (pipe)

If you use Microsoft Excel to create the CSV file, you can specify the separator in your Microsoft Windows control panel by choosing Region and Language Formats.

The source CSV files must have the following structure :

1. Row: The technical name of the field for which you want to import data.
2. Row: Any explanatory text, for example, the field description.
3. Row: The characteristics defining the plan data scope of the source file flagged by an X (capitalized or non capitalized). For the values of these characteristics, the plan data from the source file overwrites the existing plan data.

To prevent the plan data scope of a source file becomes too big, the app expects a minimal set of characteristics defining the plan data scope.

You must at least flag the following characteristics :

-
    - Category (CATEGORY)
    - Company Code (RBUKRS) or Controlling Area (KOKRS)
    - Fiscal year (RYEAR)

The app reads the plan data starting from the fourth line.

|  |
| --- |
| Note If the third row contains other characters than X, the system assumes that the third row contains plan data and starts reading from there. In this case, the system uses the following default set of characteristics defining the plan data scope :Category (CATEGORY)Company Code (RBUKRS)Fiscal year (RYEAR) |

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

Report relevancy must be done when you execute any reports for the first time. If you make a subsequent change in cost center, profit center, or G/L hierarchy, perform this step again to get the latest information.

Also, you must manually replicate set-based hierarchies (such as Cost Center Group or Profit Center Group) and financial statement hierarchies to the backend database hierarchy tables. Normally, this would be created as a periodic job that would run in the background.

Procedure

| Step # | Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Set Report Relevancy - Set-Based Hierarchies (F5295). | The Set Report Relevancy for Set-Based Hierarchies screen displays. |  |
| 3 | Enter Header Data | Make the following entries and choose Go:Set Class: For example,0101, for the cost center groupOrganizational Unit: A000Set Name: A000Include Subnodes: Yes |  |  |
| 4 | Mark as Report Relevant | In the Set Report Relevancy section, select the row and choose Edit. In the dialog box, make the following entries:Report Relevant: Yes |  |  |
| 5 | Save | Choose Save.Note If you are using the optional procedure Commitment Management and Cost Center Budgeting, repeat steps 1-5 with the following entries instead:Set Class: 0102Organizational Unit: YCOASet Name: YBA000_CEInclude Subnodes: <Select> | Set updated message displays. |  |

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

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Import Financial Data

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Template for File Upload](#unique_13) [page ] 14 | Cost Accountant - Overhead | Import Financial Plan Data (F1711) | Predelivered template file is prepared for upload. |
| [Import File](#unique_14) [page ] 15 | Cost Accountant - Overhead | Import Financial Plan Data (F1711) | File is imported. |

Upload Statistical Key Figure Plan Data

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Template for File Upload](#unique_15) [page ] 17 |  |  | This procedure occurs outside the system. |
| [Import Statistical Key Figure Plan Data](#unique_16) [page ] 18 | Cost Accountant - Overhead | Import Statistical Key Figure Plan Data (F3779) | Statistical key figure plan data file imports successfully. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Execute Cost Center Plan Assessment Cycle of Shared Expenses](#unique_17) [page ] 19 | Cost Accountant - Overhead | Manage Allocations (F3338A) | Assessment cycle is executed. |
| [Allocation Results](#unique_18) [page ] 21 | Cost Accountant - Overhead | Allocation Results (F4363) | The existing allocation results can be reviewed after a successful run. |
| [Allocation Flow](#unique_19) [page ] 22 | Cost Accountant - Overhead | Allocation Flow (F4022) | Allocation flow diagram is displayed. |
| [Download and Import Allocation Cycles](#unique_20) [page ] 23 | Cost Accountant - Overhead | Manage Allocations (F3338A) | The existing allocation cycles can be downloaded, changed and re-imported. |
| [Optional: Simulate Run](#unique_21) [page ] 24 | Cost Accountant - Overhead | Manage Allocations (F3338A) | The simulation run shows how many postings would occur based on the cycle's definition. |
| [Execute Plan Profit Center Distribution](#unique_22) [page ] 25 | Divisional Accountant | Manage Allocations (F3338A) | The profit center distribution is executed. |
| [Record Costs](#unique_23) [page ] 27 | General Ledger Accountant | Post General Journal Entries (F0718) | The journal entry is posted. |
| [Create Allocation Cycle](#unique_24) [page ] 30 | Cost Accountant - Overhead | Manage Allocations (F3338A) | The allocation cycle is created. |
| [Execute Allocation Cycle](#unique_25) [page ] 32 | Cost Accountant - Overhead | Run Allocations (F3548) | The allocation cycle is executed and documents are posted. |
| [Optional: Schedule Allocation Run](#unique_26) [page ] 33 | Cost Accountant - OverheadDivisional AccountantCost Accountant - Sales | Schedule Overhead Accounting Jobs (F3767).Schedule Division Accounting Jobs (F5288).Schedule Sales Accounting Jobs (F1483) | You can schedule allocation cycles based on a schedule or set time. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Allocations in Groups](#unique_27) [page ] 35 | Cost Accountant - Overhead | Manage Global Hierarchies (F2918) | The hierarchy is now active. |
| [Run Allocation Groups](#unique_28) [page ] 36 | Cost Accountant - Overhead | Run Allocations (F3548) | The run is created. |
| [Optional: Manage Cycle Run Groups](#unique_29) [page ] 38 | Cost Accountant - Overhead | Manage Cycle Run Groups (F4935). | A cycle group is created. |
| [Optional: Manage Allocation Changes](#unique_30) [page ] 39 | Cost Accountant - Overhead | Manage Allocation Changes (F7272) | You can view the version history of a cycle. |

Analytics

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Allocation Tags](#unique_31) [page ] 40 | Cost Accountant - Overhead | Manage Allocation Tags (F4523) | Allocation tags are created. |
| [Assign Allocation Tags](#unique_32) [page ] 41 | Cost Accountant - Overhead | Manage Allocation Tags (F4523) | Allocation tags are assigned. |
| [Plan Data Reporting for Cost Centers](#unique_33) [page ] 42 | Cost Accountant - Overhead | Cost Centers - Plan/Actual (W0081) | The newly allocated plan data displays. |
| [View Plan Profit Center Distribution](#unique_34) [page ] 43 | Divisional Accountant | Profit Centers - Plan/Actual (F2889) | The profit center distribution plan displays. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Import Financial Plan Data

#### Template for File Upload

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you download the predelivered Cost Center Planning template and prepare your plan data for upload.

|  |
| --- |
| Note Planning for cost centers, internal orders, and WBS elements automatically derive the Profit Center and Segment organizational fields that are reflected in the corresponding Plan/Actual report. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead . | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Import Financial Plan Data (F1711) . | The Import Financial Plan Dataview displays. |  |
| 3 | Select Template | Choose the Download Templates button. In the Download Templates view, select the template file by placing the cursor directly on the line Cost Center Planning and choose Close.Open the csv file. |  |  |
| 4 | Save Template | Save the file in the CSV format on your desktop. |  |  |
| 5 | Update Template | Open the template and maintain the following data listed below. |  |  |

|  |
| --- |
| Note Maintain the following cost center plan data. Note that this is an example and adjust the values as necessary. |

| CATEGORY | RYEAR | POPER | RBUKRS | RCNTR | RACCT | KSL | RKCUR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Plan Category | General Ledger Fiscal Year | Posting Period | Company Code | Cost Center | Account Number | Amount in Global Currency | Global Currency |
| X | X | X | X | X |  |  |  |
| PLN | <Enter the current fiscal year> | 09 | 3310 | 33101750 | 61003000 | 100000 | USD |
| PLN | <Enter the current fiscal year> | 10 | 3310 | 33101750 | 61003000 | 200000 | USD |
| PLN | <Enter the current fiscal year> | 11 | 3310 | 33101750 | 61003000 | 300000 | USD |

#### Import File

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The app performs the following checks:

1.The app checks whether the values in the source file are valid. If required, it returns a list of error messages.

You must correct the values in the source file until they are all valid before you can proceed.

2. If all values are valid, the app checks all versions, fiscal years, posting periods, and company codes that are contained in the source file.

- If no plan data exists in the system for any combination of these four characteristics, you can directly import the plan data.
- If plan data exists in the system for any combination of these four characteristics, the app displays the affected values. It assumes that you want to completely replace the existing plan data by the new plan data import.

|  |
| --- |
| Note One source file should therefore always contain full plan data sets for a certain combination of version, company code, and fiscal year (including all posting periods). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Import Financial Plan Data (F1711) . |  |  |
| 3 | Enter Source File | Enter the following values:Source File:<Your .CSV file that contains your plan>Choose Enter. | The Block Asset Processing view displays. |  |
| 4 | File Check | The upload performs a check to ensure the format is correct.Correct any error message that appears. | The selected file contains data replacing or deleting the data message that appears. |  |
| 5 | Review | Note the informational messages.Your plan data import will incorporate X lines from CSV file. For more information, go to the Preview List.Select the links in the messages to review data, and choose the Back button. | The list of the data uploaded appears. |  |
| 6 | Import | Choose Import Source File. | Import successfulmessage appears. |  |

### Import Statistical Key Figure Plan Data

Context

Plan statistical key figures are used to create relative weighted values for use in allocations like overhead. Common statistical key figures include headcount and square footage.

#### Template for File Upload

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you download the predelivered Cost Center Statistical Key Figures template and prepare your data for upload.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Import Statistical Key Figure Plan Data (F3779). | The Import Financial Plan Dataview displays. |  |
| 3 | Select Template | Choose the Download Templates button. In the Download Templates view, select the template file by placing the cursor directly on the line Cost Center Statistical Key Figures and choose Close.Open the csv file. |  |  |
| 4 | Save Template | Save the file in the CSV format on your desktop. |  |  |
| 5 | Update Template | Open the template and maintain the following data listed below. |  |  |

|  |
| --- |
| Note Maintain the following statistical key figure plan data. Note that this is an example and adapt the values as necessary. |

| CATEGORY | RYEAR | POPER | RBUKRS | RCNTR | STAGR | MSL | RUNIT |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Plan Category | General Ledger Fiscal Year | Posting Period | Company Code | Cost Center | Statistical Key Figure | Quantity | Quantity Unit |
| X | X | X | X | X | X |  |  |
| PLN | <Enter the current fiscal year> | 11 | 3310 | 33101101 | 1001 | 100 | PC |
| PLN | <Enter the current fiscal year> | 11 | 3310 | 33101301 | 1001 | 50 | PC |

#### Import Statistical Key Figure Plan Data

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Import Statistical Key Figure Plan Data (F3779). | The Import Statistical Key Figure Plan Data (F3779) screen displays. |  |
| 3 | Enter Source File | Use the Browse button to select the CSV extension file you wish to upload.Enter the following Field Value:Source File :Your .CSV file that contains your planChoose Enter | The Plan Data Scope for the CSV file uploads.The upload performs a check to ensure that the format is correct.Corrections can be made if any error messages appear. |  |
| 4 | Import | Choose Import Source File. | The file import is successful. |  |

### Execute Cost Center Plan Assessment Cycle of Shared Expenses

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you execute a plan assessment cycle (cost center). Both cost centers and wbs elements can be used as receivers in the plan assessment cycle. In this example, cost center as receiver is demonstrated.

Prerequisites

The plan assessment cycle demo data has been created for testing.

For details on how to create your own plan assessment cycle defining senders and receivers, see the Create Universal Allocation Master Data - MDS (2US) master data script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Allocations (F3338A). | The Manage Allocations screen displays. |  |
| 3 | Input Initial Screen | Make the following entries and choose the Go button:Allocation Context: Cost CentersAllocation Cycle: OP3310Company Code: 3310Allocation Type: Overhead AllocationLedger : 0L | The Allocation Cycles view displays. |  |
| 4 | Select Allocation Cycle | Select the allocation cycle row and then choose the > to the right of the allocation cycle row. | The Manage Allocations view displays. |  |
| 5 | Edit Allocation Cycle | Do the following:Under Segments, select the segment and choose the > to the right of the segment row.Choose the Receiver Basis tab.Make the following entries (choose the Edit button if you need to make any changes):Var. Portion Type: Stat. Key Figures - Plan (SKF-1)Selection Criteria:Plan CategoryValue Type: Single ValueSingle Entry/From: PLNStat. key figureValue Type: Single ValueSingle Entry/From: 1001Save the entries. | Note Selection criteria for statistical key figures can be single values, ranges or groups. Groups of statistical key figures can be created using the Manage Global Hierarchies (F2918) app. |  |
| 6 | Select Allocation Cycle | Go back to the Allocation Cycles section. Select the allocation cycle row and choose the Run button. | The Run Allocations screen displays. |  |
| 7 | Test Run | Select the allocation cycle row and choose the Test Run button. | The Run Allocation(s) - Test Run screen displays. |  |
| 8 | Input Values | Make the following entries and choose Validate.Test Run Name: <enter your desired value>Ledger: 0LFiscal Period From: <current period and year>Fiscal Period To: <curent period and year>To review the results, choose Go. Viewing the completed run, you can further drill into the report to view specific senders and receivers, and values. | You get a success message. If everything looks correct, you can repeat the steps above and choose Run instead of Test Run. |  |
| 9 | Check for Notifications | While in the Overhead Accountant overhead window, check if a notification is generated (icon located on the upper right side the window). | The allocation run triggers a warning or error in the execution of universal allocation run. If no notification, the run had no error. |  |

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

### Download and Import Allocation Cycles

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, existing allocation cycles can be downloaded, changed and re-imported.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Allocations (F3338A). | The Manage Allocations view displays. |  |
| 3 | Input Initial Screen | Make the following entry and choose the Go button:Allocation Cycle: OP3310 | The Allocation Cycles view displays. |  |
| 4 | Allocation Cycle | Select the allocation cycle row. |  |  |
| 5 | Download Allocation Cycle | Choose the Upload/Download Template button. In the Upload new values window, select Download Template with Selected Data and save to your local drive. |  |  |
| 6 | Change Value | On your desktop, open the file and replace the cycle value from OP3310 to ZXXXX. Do this for all tabs in the Excel sheet where OP3310 is present (Cycle, Segment, Senders, Receivers, Receiver Basis). |  |  |
| 7 | Manage Allocations app | Go back to Manage Allocations - Deprecated (F3338) app. | The Manage Allocations view displays. |  |
| 8 | Upload Cycles | Choose the Upload/Download Template button. In the Upload new values window, choose Upload. |  |  |
| 9 | Upload Excel | In your local file open window, select your Excel file created in the previous step and choose Open. Choose Confirm. |  |  |
| 10 | Postpending | During postpending, you can make additional corrections or changes to the file.Choose the Senders tab and choose Edit. |  |  |
| 11 | Update Sender Cost center | Make the following entries and choose Save:Replace the cost center 33101750 with another cost center within the same company code, for example 33101301. |  |  |
| 12 | Submit New Allocation Cycle | Choose Apply and exit the screen. | New allocation is created. |  |

|  |
| --- |
| Note You can also import values via the Import Allocation Data - Values (F5596) app. |

### Optional: Simulate Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Allocations can be complex and have long runtimes and dumps. The simulation run shows how many postings would occur based on the cycle's definition derived from the actual or planned data. If several potential records exist, you may want to adjust the cycle or the run parameters.

Prerequisite

An existing allocation cycle.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Allocations (F3338A). | The Manage Allocations screen displays. |  |
| 3 | Select Allocation | Using the Search field, enter the recently uploaded allocation and choose Go. Select the checkbox next to the allocation and choose Details. | The Detail screen of the Manage Allocations displays. |  |
| 4 | Input Initial Screen | Choose the Run button. On the Create new run screen, choose Test Run. Make the following entries and choose Validate and Run:Ledger: 0LFiscal Period From: for example, 005.2022Fiscal Period To: for example, 005.2022 | The simulation run shows how many postings would occur based on the cycle's definition. |  |

### Execute Plan Profit Center Distribution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Using plan profit center distribution, it is possible to distribute balance sheet account balances to and from various profit centers.

Prerequisites

1. A G/L account for allocation clearing must be available. Create G/L 29500000 CO Allocation Clearing using GL 29500100 as a reference. For details on how to create the G/L, refer to Create G/L Account and Cost Element - MDS (BNG) test script.
2. Assign splitting rule via configuration activity Define Document Splitting Characteristics for Controlling for copying values from 29500100 to 29500000.
3. The plan assessment cycle demo data has been created for testing and is ready to use. For details on how to create your own plan assessment cycle defining senders and receivers, see the Create Universal Allocation Master Data - MDS (2US) test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Divisional Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Allocations (F3338A). | The Manage Allocations view displays. |  |
| 3 | Input Initial Screen | Make the following entries and choose the Go button:Allocation Context: Profit CentersAllocation Type: DistributionLedger: 0LCompany Code: 3310Allocation Cycle: OPPCD33 | The assessment is done. |  |
| 4 | Review Allocation Cycle | Do the following:Select the allocation cycle row and choose the > sign.In the Manage Allocations view, choose the Segments tab and select Edit.Select the segment row and choose the > sign. Review segment tabs (Rules, Senders).Choose the Sender Basis tab and change the amount to 1000.Choose the Check Segment button.Choose the Save button. |  |  |
| 5 | Run Allocation | Select the allocation cycle row and choose the Run button. | The Run Allocations screen displays. |  |
| 6 | Test Run | Select the allocation cycle row and choose the Test Run button. | The Run Allocation(s) - Test Run screen displays. |  |
| 7 | Input Values | Make the following entries and choose Validate and Run.Test Run Name: <enter your desired value>Ledger: 0LFiscal Period From: <current period and year>Fiscal Period To: <curent period and year> | A success log displays. To review the results, choose the Display Run Result button. |  |

|  |
| --- |
| Tip To reverse an assessment posting, use the app Run Allocations (F3548) and choose Go. Select the allocation cycle job and choose Reverse. |

### Optional: Intercompany Allocation

#### Record Costs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Intercompany allocations are possible by creating an allocation using a settlement or an allocation structure. This example uses an allocation structure.

|  |
| --- |
| Note Currently allocations for cost centers on actual data utilized the leading ledger is supported. Receivers can be either cost centers, WBS elements. |

Also note the new intercompany (ICO) allocations behave differently compared to the cost center allocations in Universal Allocation: The ICO allocations calculate values from the data in the leading ledger and post the same results to all ledgers, thus acting somehow like a prima-nota posting. In contrast, regular cost center allocations in the Universal Allocation operate for each ledger explicitly.

The following limitations currently apply:

• Intercompany cycles must not be defined as iterative or cumulative cycles.

• Cannot explicitly include transaction amounts or transaction quantities.

• Each segment, exactly one sender company code must be specified.

Prerequisites

The following demo data is already provided for creating the intercompany universal allocation with the allocation structure based on the script.

Allocation structures, cost element groups, and intercompany settings must be maintained based on your specific business needs and are described below:

Allocation Structure: Universal Allocation structure shell is delivered as standard content and must be modified based on your specific user requirements via the configuration activity Maintain Allocation Structures.

Allocation Structure: UA Universal Allocation Structure:

| Line | Description | Source Cost Element Group | Assessment Cost Element |
| --- | --- | --- | --- |
| 10 | Rents | UA100 | 94201000 |
| 20 | Other costs | UA200 | 94222000 |

Two empty cost element groups UA100 and UA200 are also delivered in standard content with no G/L accounts assigned and can be maintained via the Edit Cost Element Group app to suit your requirements. For the demo/test purposes we have assigned two GL accounts listed below:

| Cost Element Groups | GL Assignment | Description |
| --- | --- | --- |
| UA100 | 63005000 | Office/Building Rent |
| UA200 | 63004000 | Insurance |

Intercompany Clearing must also be maintained via configuration activity Automatic Account Determination.

For demo/test purposes, we have maintained the following:

| Costs/Rev Account | Cost/Rev Account to | Description | Source Cost Element Group | Assessment Cost Element |
| --- | --- | --- | --- | --- |
| 94201000 |  | Buildings & Periodic Service | 70030000 | 70030000 |
| 94220000 |  | COPA Assessment | 70030000 | 70030000 |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post General Journal Entries (F0718). | The Post General Journal Entries view displays. |  |
| 3 | Enter Journal Entries Header Data | In the Header pane, make the following entries and choose the Go button:Journal Entry Date: <current date>Posting Date: <current date>Period: <current period, for example, 05>Journal Entry Type: SACompany Code: 3310Transaction Currency: AED |  |  |
| 4 | Enter Line Item Data | In Line Items (2), make the following entries and press Enter:Company Code: 3310G/L Account: For example, 63005000Debit: amount, for example, 100000>Note Make the entry in the debit or credit column as appropriate.Tax Code: V0Cost Center: 33101750 | An overview detail of the allocation executed can be see via the various tabs. |  |
| 5 | Enter Second Line Detail | In Line Items (2), to add another line, select the Add Line Item button at the bottom right and press Enter:Company Code: 3310G/L Account: For example, 11001000Credit: <amount, for example, 100000>Note Total debit amount shown (that is, Debit Amount + Tax Rate amount, based on the tax code entered).Next, make the following entries:Value date: <Current date>House Bank: DEBK1House Bank Account: DEAC1Note The value date is required for cash accounts. | The graphical view of the data is displayed. |  |
| 6 | Post | Choose Post. Make a note of the document number. | The journal entry is posted. |  |
| 7 | Create a Second Posting with G/L | Repeat steps 3 to 6 with G/L Account 63004000, cost center 10101750, and credit/debit amount 2000. |  |  |

#### Create Allocation Cycle

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity creates the allocation cycles incorporating the allocation structure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Allocations (F3338A). | The Manage Allocations screen displays. |  |
| 3 | Create Cycle Header | Choose the Create button and select Create New Cycle. |  |  |
| 4 | Input Initial Screen | Make the following entries and choose the Create button:Allocation Cycle: <enter a cycle ID beginning with Z>Allocation Context: Cost CentersAllocation Type: Intercompany AllocationLedger : 0LValid From: 01/01/2021Valid To: 12/31/9999Cycle description: <enter a cycle description>Actual/Plan: Actual | The Allocation: Create Plan Overhead Allocation Cycle: Header Data view displays. |  |
| 5 | Change Value | In the Segments tab, choose Create and make the following entries:Segment Name: <any>Segment Description: <any>Choose OK.In the Rules section, make the following entries:Sender Rule: Posted amountsAllocation Structure: UAReceiver Rule: Fixed percentagesIn the Senders section, make the following entries:Company Code:Value Type: Single ValueSingle Entry/From: 3310Choose the Add button. Select Account Number and choose Add.Account Number:Value Type: GroupGroup: <use search help to select UA100 (Group ID 0102YCOAUA100)>Cost Center:Value Type: Single ValueSingle Entry/From: 33101750In the Receivers section, choose Add. In the following dialog box, select Cost Center and choose Add.Cost Center: <see the note below>Note This value must be the receiving company code’s cost center. Though company codes are not entered directly, they are inferred via the cost center.In the Receiver Basis tab, make the following entry.Percentage: 100Save the entries. | Allocation cycle is created. Make note of the name as it will be required in the next step. |  |

#### Execute Allocation Cycle

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity executes the allocation cycle created in the previous step.

Prerequisite

Universal allocation is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Run Allocations (F3548). | The Run Allocations screen displays. |  |
| 3 | Allocation and Cycle | In the Select: Allocation Cycles for the Run view, enter the recently created allocation in the search field and choose Go.Note If this view does not display, choose the Add button to show the Select: Allocation Cycles for the Run view.Select the cycle from the list and choose OK. |  |  |
| 4 | Run | Choose the Run button. On the Run Allocation(s) - Live Run screen, make the following entries and choose Validate and Run.Test Run Name: <enter your desired value>Ledger: 0LFiscal Period From: <current period and year>Fiscal Period To: <curent period and year> | The cycle is then executed and documents are posted. |  |

### Optional: Schedule Allocation Run

Purpose

In addition to running a single allocation, it is possible to schedule allocation cycles based on a schedule or set time.

Procedure

| Step # | Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as either Cost Accountant - Overhead, Divisional Accountant, or Cost Accountant - Sales. | The role and app used depends on the actual type of allocation that is run. |  |
| 2 | Access the SAP Fiori App | For overhead allocations, open Schedule Overhead Accounting Jobs (F3767).For Profit Center allocations, open Schedule Division Accounting Jobs (F5288).For Profitability (COPA) allocations, open Schedule Sales Accounting Jobs (F1483). | The Application Jobs screen displays. |  |
| 3 | Create | Choose the Create button. | The New Job: Actual Cost Rate Calculation screen displays. |  |
| 4 | Template Selection | In the header area, make the following entries and choose Step 2:Job Template: <Based on the respective roles, select the desired template, for example, Universal Allocation Run - Cost Centers (SAP), or Universal Allocation Run - Profit Centers (SAP) or Universal Allocation Run - Margin Analysis (SAP)>Tip Delete the entry to see all the job templates available.Job Name: <Enter a text> |  |  |
| 5 | Scheduling Options | Make the following entries and choose Step 3:Start Immediately: SelectNote You can also select the Define Recurrence Pattern to schedule in advance or on a regular schedule.Start: <Accept the default> |  |  |
| 6 | Parameters | Make the following entries and choose Check to validate your entries:Cycle ParametersLedger: For example, 0LAllocation Type: <Choose a valid type based on the cycle chosen>Actual/Plan: <Select based on the cycle chosen>Cycle/GroupUse Cycle: For example, Test RunMaster DataCycle Selection: <Your cycle>Run ParametersRun Type: For example, Test RunRun Name: <Any>Run Ledger: For example, 0LFiscal Year: <current year>Fiscal Period From: <current period>Fiscal Period To: <current period> | A message that you can go ahead and schedule the job appears if the check is successful, else make the required corrections. |  |
| 7 | Schedule | Once the check is successful, choose Schedule. | The job is scheduled.Note After the job is scheduled, to immediately navigate to the Allocation Results app, choose the Log button. |  |

### Optional: Working with Allocation Groups

#### Create Allocations in Groups

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you group allocation cycles together to run in a specific sequence using groups. The first step is create a hierarchy sequence. Once created, this sequence can be maintained and adjusted within the allocation run.

Prerequisite

Planned allocation cycles must be created in the system to view sender and receiver information. Planned cost center data and planned statistical key figures must be posted in the SAP system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Global Hierarchies (F2918). | The Manage Global Hierarchies view displays. |  |
| 3 | Input Initial Screen | Choose the Create button. | The Create New Hierarchy dialog box displays. |  |
| 4 | New Hierarchy | Make the following entries and choose the Create button:Type: Universal Allocations HierarchyHierarchy ID: <any ID>Hierarchy Description: <enter a description>Allocation Context: Cost CentersAllocation Type: Overhead AllocationLedger : 0LActual/Plan. Indicator: Plan |  |  |
| 5 | Select Hierarchy | Select the newly created hierarchy row and choose the > button. | The Universal Allocations Hierarchy view displays. |  |
| 6 | Adding Allocations | Choose the Edit button and then choose the + button. In the Add Node dialog box, make the following entries and choose OK:Select Allocation CycleAllocation Cycle: <select an allocation cycle>Note This step can repeat to add as many allocation cycles in your desired sequence run. |  |  |
| 7 | Save and Activate | Choose the Save button and then choose the Activate button. | The hierarchy is now active. |  |

#### Run Allocation Groups

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, this sequence can be maintained and adjusted within the allocation run.

Prerequisite

Planned cost center data and planned statistical key figures must be posted in the SAP system. A Universal Allocation Hierarchy must exist.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Run Allocations (F3548). | The Run Allocations screen displays. |  |
| 3 | Add Hierarchy | Choose the Add Hierarchy tab. Make the following entries and choose the Go button:Allocation Context: Cost CentersLedger : 0LAllocation Type: Overhead AllocationActual/Plan: Plan | The Run Allocations screen displays. |  |
| 4 | Select Hierarchy | Select your recently created hierarchy and choose OK. |  |  |
| 5 | Making Sequence Changes | In the Run Allocations view, you can select individual allocation cycles and move them. To move an allocation cycle, select an allocation within your hierarchy and choose the Move up or Move down arrows. | The sequence is changed. |  |
| 6 | Run Hierarchy | Select the Cycle/Group checkbox to select all allocations. Choose the Test Run button. Make the following entries and choose Validate.Test Run Name: <enter your desired value>Ledger: 0LFiscal Period From: <current period and year>Fiscal Period To: <curent period and year>Note If the test run is successful, you can then choose the Run button. | The run is created. |  |

### Optional: Manage Cycle Run Groups

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When cycles are initially created, they are assigned to a generic default processing group. If multiple allocation cycles are chosen in a run execution, they are run one cycle at a time (one after the other). This optional step allows the parallel processing of cycles via groups which reduces the time to run all the cycles requested. Cycles that are assigned to a different group would always be processed in parallel, thus reducing the run time. The example below describes how to create these assigned cycles to parallel processing groups.

Prerequisite

Universal allocation is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Cycle Run Groups (F4935). | The Manage Cycle Run Groups view displays. |  |
| 3 | Create Group | Choose Create. Make the following entries and choose Create:Cycle Run Group: <any 4 characters>Object Description: <any>Ledger: 0LAllocation Context: Cost CentersAllocation Type: Overhead AllocationActual/Plan: Plan | The allocation cycle group is created. |  |
| 4 | Add Allocation Cycles to Group | Select the cycle run group recently created and choose Assign.In the Select: Allocation Cycles for Group XXX dialog box, use the search function to find the desired allocation cycles you want run together as a group and choose Assign. | Allocation cycle group is created. |  |

### Optional: Manage Allocation Changes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When cycles are initially created, the version is set. Versions are generated either through a live run (provided there have been changes made between live runs) or upon deletion of a cycle.

Prerequisite

Allocation cycles must exist.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Allocation Changes (F7272). | The Manage Allocation Changes view displays. |  |
| 3 | Enter Data | Make the following entry and choose Go:Company Code: 3310 | The list of allocation cycles display. |  |
| 4 | Select your Allocation Cycle | Select your allocation cycle, and choose the Select Version button. | You can view the version history of a cycle. |  |

### Analytics

#### Allocation Tags

##### Create Allocation Tags

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, allocation tags are used to label allocation cycles with tags. Allocation tags can be used for better organization of allocation process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Allocation Tags (F4523). | The Allocation Tag view displays. |  |
| 3 | Enter Values | Choose the Create button. In the dialog box, make the following entries and choose the Create button:Allocation Tag: <enter an ID beginning with Z>Description: <enter a tag description> | The newly created tag is ready to use. |  |

##### Assign Allocation Tags

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can use allocation tags to label allocation cycles with tags. Allocation tags can be used for better organization of allocation process. They are used as selection criteria for various reports making it easier to view them collectively.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Allocation Tags (F4523). | The Manage Allocation Tags view displays. |  |
| 3 | Enter Values | Make the following entry and choose Go:Allocation Tag: <enter an ID that has been previously created> |  |  |
| 4 | Assign Allocation Tag | Select the allocation tag row and choose Assign. | The Assign Allocation Tag window displays. |  |
| 5 | Assign Allocation Cycles | Select the company code-specific allocation cycles you want to tag and choose Assign. | Tags are now assigned and are used as selection criteria in various reports. |  |

#### Plan Data Reporting for Cost Centers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run the actual data reporting for cost centers.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Cost Centers - Plan/Actual (W0081). | The Cost Centers - Plan/Actual screen displays. |  |
| 3 | Selection Criteria | Make the following entries and choose Go:Ledger: 0LFiscal Year of Ledger: <Current year>Plan Category: PLNKey Date: <Current date>Company Code: 3310 | Scroll to the Plan Amount in CC Crcy and you can see the newly allocated plan data. |  |

#### View Plan Profit Center Distribution

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
| 2 | Access the SAP Fiori App | Open Profit Centers - Plan/Actual (F2889). | The Prompts dialog box displays. |  |
| 3 | Selection Criteria | Make the following entries:Ledger: 0LLedger Fiscal Year: <Current year>Planning Category: PLNCompany Code: 3310Key Date: <Current date> |  |  |
| 4 | Choose | Choose OK. | Using the report filters on profit centers, you can see the allocations. |  |

## Appendix

### Situation Handling

#### Manage Situation Types

Purpose

This template is used for situation handling that informs specific users when a condition is met. In this example the user, Overhead Accountant, receives a notification (icon located in the upper right side the window) when the allocation run triggers a warning or error in the execution of universal allocation run. For information on the Situation Template for Allocation Runs, see [https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/e929d26943b34cc889681e8f9eaadc77.html](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/e929d26943b34cc889681e8f9eaadc77.html).

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Situation Types (F2947). | The Manage Situation Types view displays. |  |
| 3 | Copy the Situation Template | In the Search field, enter FIN_ALLOCATION_RUN_WARNING_ERROR and choose Go.Select the checkbox for the row FIN_ALLOCATION_RUN_WARNING_ERROR, and then choose Copy. |  |  |
| 4 | Maintain Admin Information | Make the following entries and choose Create (accept all warning and enable messages):ID: <enter your template name>Name: <enter your template description>Situation Monitoring:Monitor Instances: <selected> | The initial situation type for allocation run warning or error message is created. |  |

#### Manage Teams and Responsibilities

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Teams and Responsibilities (F2412). | The Manage Teams and Responsibilities view displays. |  |
| 3 | Category | Remove any preset category filters.In Category, enter UNIVALLOC and choose Go.If no results exist, go the next step to create a new team. |  |  |
| 4 | Manage Teams and Responsibilites | Choose Create.Make the following entries and choose Create (accept all warning and enable messages):Name: <Team Name>Global ID: <Global ID name>Type: Universal Allocations (UNIVALLOC)Responsibility DefinitionsAllocationContext: ACDOC_CC (Cost Centers)AllocationType: U (Overhead Allocation)Team OwnersBusiness Partner: <BPC expert ID>Team MembersBusiness Partner: <Overhead Accountant user ID>Note To find the overhead accountant user ID, use the search function with:Last name: OverheadAccountantFunctions: <Cost center run>Confirm and save the entries. | A New Situation Type view displays. |  |

#### Finishing Up the Situation Type

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Situation Types (F2947). | The Manage Situation Types view displays. |  |
| 3 | Assign Responsibility to the Template | Using the search function, enter the newly created situation type and choose the Situation Types tab. Choose Go.Select the situation type and choose the > sign on the right of the page. Choose Edit.In the Recipients section, under Responsibility by Teams, choose Add Team Category, make the following entries and choose Save:Filter by Member Function: Cost center run | The initial situation type for allocation run warning or error message is created. |  |

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
- related-to :: [[06-management-accounting/create-universal-allocation-master-data-mds-2us-287]]
- related-to :: [[06-management-accounting/mds-2us-289]]
- related-to :: [[06-management-accounting/mds-2us-291]]
- related-to :: [[06-management-accounting/script-de-dados-mestre-criar-dados-mestre-de-alocacao-universal-mds-2u]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2QL_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 73,460 chars in the whole document
