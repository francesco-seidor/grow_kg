---
id: 05-treasury-and-cash-management/advanced-cash-operations-j78-ae-test-script-sap-s-4hana-cloud-public-e-part-01
title: Advanced Cash Operations (J78_AE) Test Script - SAP S/4HANA Cloud Public Edition (J78_S4CLD2608_BPD_EN_AE) — part 1 of 2
description: "Test script for SAP scope item J78 Advanced Cash Operations (AE, co. code 3310): cash config, BCM payment approval, bank transfers, cash trade requests."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/cash-operations]
aliases: []
keywords: [Cash Operations and Cash Positioning, cash management full scope, liquidity items, liquidity item derivation, flow builder, payment approval, bcm payment batches, bank transfers, cash position profile, cash flow reconciliation]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J78_S4CLD2608_BPD_EN_AE.docx#lines-1-3312"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1309
topic: 05-treasury-and-cash-management/cash-operations
language: EN
part: 1/2
created: 2026-10-12
updated: 2026-10-12
---

# Advanced Cash Operations (J78_AE) Test Script - SAP S/4HANA Cloud Public Edition (J78_S4CLD2608_BPD_EN_AE) — part 1 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J78_S4CLD2608_BPD_EN_AE.docx`, part 1 of 2 (lines 1–3312 of the extracted text), extracted with `mammoth`. Grouped under **Cash Operations and Cash Positioning** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Advanced Cash Operations (J78_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Advanced Cash Operations (J78_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 6](#_Toc232864308)

[2 Prerequisites 7](#_Toc232864309)

[2.1 System Access 7](#_Toc232864310)

[2.2 Roles 7](#_Toc232864311)

[2.3 Master Data, Organizational Data, and Other Data 8](#_Toc232864312)

[2.4 Business Conditions 10](#_Toc232864313)

[2.5 Additional Manual Configuration 11](#_Toc232864314)

[2.6 Preliminary Steps 11](#_Toc232864315)

[2.6.1 Maintain Full Scope for Cash Management 11](#_Toc232864316)

[2.6.2 Enable Snapshot (Optional) 13](#_Toc232864317)

[2.6.3 Define Runtime Parameters for Flow Builder 15](#_Toc232864318)

[2.6.4 Liquidity Items 17](#_Toc232864319)

[2.6.4.1 Define Source Application Accounting 17](#_Toc232864320)

[2.6.4.2 Define Basic Settings for Liquidity Analysis 19](#_Toc232864321)

[2.6.4.3 Define Derivation Rules – Query Sequence 21](#_Toc232864322)

[2.6.4.3.1 Define Query Sequences 21](#_Toc232864323)

[2.6.4.3.2 Define Queries for Liquidity Item Derivation 23](#_Toc232864324)

[2.6.4.3.3 Assign Queries to Query Sequences 24](#_Toc232864325)

[2.6.4.3.4 Assign Sequence to Company Codes 25](#_Toc232864326)

[2.6.4.4 Liquidity Calculation: Manage Query Sequences (Optional) 26](#_Toc232864327)

[2.6.4.5 Liquidity Calculation: G/L Classification 28](#_Toc232864328)

[2.6.4.6 Schedule Job for Rebuild Tool for Liquidity Item 35](#_Toc232864329)

[2.6.4.7 Define Liquidity Item Derivation Mode for Flow Builder 37](#_Toc232864330)

[2.6.4.8 Flow Builder: Stop Condition (Optional) 39](#_Toc232864331)

[2.6.4.8.1 Define Profile for Stop Condition 39](#_Toc232864332)

[2.6.4.8.2 Assign Flow Builder Profile to Company Code 40](#_Toc232864333)

[2.6.4.9 Manage Liquidity Items Hierarchies (Optional) 42](#_Toc232864334)

[2.6.4.10 Set Block Date for Actual Cashflows 44](#_Toc232864335)

[2.6.5 Payment Approval 45](#_Toc232864336)

[2.6.5.1 Maintain Payment Approver for Bank Accounts 45](#_Toc232864337)

[2.6.5.2 Specify Optional User Authentication (Optional) 46](#_Toc232864338)

[2.6.5.3 Define Automatic Approval/Rejection for Bank Account Master Data 47](#_Toc232864339)

[2.6.5.4 Fix Errors for Payment Batches (Optional) 49](#_Toc232864340)

[2.6.5.5 Define Planning Levels for Cash Flow Payment Approval 54](#_Toc232864341)

[2.6.5.6 Assign Planning Levels for Cash Flow Payment Approval 56](#_Toc232864342)

[2.6.6 Define Cash Position Profile 58](#_Toc232864343)

[2.6.7 Cash Flow Reconciliations 63](#_Toc232864344)

[2.6.7.1 Define Planning Level 63](#_Toc232864345)

[2.6.7.2 Define Memo Record Type 65](#_Toc232864346)

[2.6.7.3 Define Profiles for Cash Flow Reconciliation 67](#_Toc232864347)

[2.6.7.4 Activate Reconciliation for Bank Account 71](#_Toc232864348)

[2.6.8 Cash Trade Request 72](#_Toc232864349)

[2.6.8.1 Enable Cash Trade Requests 72](#_Toc232864350)

[2.6.8.2 Define Planning Level for Cash Request 74](#_Toc232864351)

[2.6.8.3 Assign Planning Level to Cash Request 77](#_Toc232864352)

[2.6.9 Automatically Reversing Rejected Payments 79](#_Toc232864353)

[2.6.9.1 Define Rules for Reversing Rejected Payments 79](#_Toc232864354)

[2.6.9.2 Create Team for Reversing Rejected Payments 81](#_Toc232864355)

[2.6.10 Situation Handling 82](#_Toc232864356)

[2.6.10.1 Situation Handling for Cash and Liquidity Management 82](#_Toc232864357)

[2.6.10.1.1 Manage Teams and Responsibilities 82](#_Toc232864358)

[2.6.10.1.2 Create Situation Types: Date Difference Warning for FI Flows 83](#_Toc232864359)

[2.6.10.1.3 Create Situation Types: Bank Account Balance Threshold Exceeded 84](#_Toc232864360)

[2.6.10.2 Situation Handling for Bank Communication Management 86](#_Toc232864361)

[2.6.10.2.1 Define Function 86](#_Toc232864362)

[2.6.10.2.2 Define Function Profiles 87](#_Toc232864363)

[2.6.10.2.3 Assign Function Profiles to Team Category 89](#_Toc232864364)

[2.6.10.2.4 Define Team Types 91](#_Toc232864365)

[2.6.10.2.5 Manage Teams and Responsibilities 92](#_Toc232864366)

[2.6.10.2.6 Create Situation Types: Payment Batch Partially Rejected 93](#_Toc232864367)

[2.6.10.2.7 Create Situation Types: Payment Batch Was Rejected 94](#_Toc232864368)

[2.6.10.2.8 Create Situation Types: Payment Batch Status Check 96](#_Toc232864369)

[2.6.11 Email Notification for Payment Approvers (Optional) 98](#_Toc232864370)

[2.6.11.1 Enable Email Notifications 98](#_Toc232864371)

[2.6.11.2 Maintain Email Templates 100](#_Toc232864372)

[3 Overview Table 102](#_Toc232864373)

[4 Test Procedures 109](#_Toc232864374)

[4.1 Outgoing Payment with BCM Approval Process 109](#_Toc232864375)

[4.1.1 Approval and Bank Integration 109](#_Toc232864376)

[4.1.1.1 BCM Batch Creation 110](#_Toc232864377)

[4.1.1.2 Monitor Payments 110](#_Toc232864378)

[4.1.1.3 Check Cash Flow Items (Before Approval) 112](#_Toc232864379)

[4.1.1.4 Approval of Bank Transfer 113](#_Toc232864380)

[4.1.1.4.1 Approval by First Approver 114](#_Toc232864381)

[4.1.1.4.2 Reject by First Approver (Optional) 115](#_Toc232864382)

[4.1.1.4.3 Process Rejected Payments (Optional) 117](#_Toc232864383)

[4.1.1.4.4 Approval by Second Approver 118](#_Toc232864384)

[4.1.1.5 Bank Integration 119](#_Toc232864385)

[4.1.1.5.1 Option 1: Bank Integration with SAP Multi-Bank Connectivity (16R) (Outgoing Integration) 119](#_Toc232864386)

[4.1.1.5.2 Option 2: Bank Integration with File Interface (1EG) (Outgoing Integration) 120](#_Toc232864387)

[4.1.1.6 Display Status of Payment Documents 120](#_Toc232864388)

[4.1.1.7 Situation Handling for Payment Batch 121](#_Toc232864389)

[4.1.1.7.1 Situation Handling: Payment Batch Partially Rejected 121](#_Toc232864390)

[4.1.1.7.2 Situation Handling: Payment Batch Was Rejected 123](#_Toc232864391)

[4.1.1.7.3 Situation Handling: Payment Batch Status Check 125](#_Toc232864392)

[4.1.1.8 Check Cash Flow Items (Check Status) 127](#_Toc232864393)

[4.2 Bank Transfer Actions 128](#_Toc232864394)

[4.2.1 Initiate Bank Transfer 129](#_Toc232864395)

[4.2.1.1 Option 1: Create, Release and Clear Payment Request in One Single Action 130](#_Toc232864396)

[4.2.1.2 Option 2: Create, Release, and Clear Payment Request in Separate Steps 133](#_Toc232864397)

[4.2.1.2.1 Create Bank Transfer 133](#_Toc232864398)

[4.2.1.2.2 Release Payment Request 135](#_Toc232864399)

[4.2.1.2.3 Pay Payment Request 136](#_Toc232864400)

[4.2.1.3 Option 3: Make Bank Transfer with Templates 137](#_Toc232864401)

[4.2.1.3.1 Define Bank Transfer Templates 138](#_Toc232864402)

[4.2.1.3.2 Create Bank Transfers with Templates 140](#_Toc232864403)

[4.2.1.3.3 Release Payment Request 141](#_Toc232864404)

[4.2.1.3.4 Pay Payment Request 142](#_Toc232864405)

[4.2.2 Approve and Bank Integration 142](#_Toc232864406)

[4.2.3 Short Term Cash Positioning 142](#_Toc232864407)

[4.3 Cash Trade Request 145](#_Toc232864408)

[4.3.1 Create and Submit Cash Trade Request for FX 145](#_Toc232864409)

[4.3.2 Create and Submit Cash Trade Request for Money Market 147](#_Toc232864410)

[4.3.3 Release Cash Trade Request 148](#_Toc232864411)

[4.3.4 Reject Cash Trade Request (Optional) 149](#_Toc232864412)

[4.3.5 Treasury Management Integration for Trading Platform 150](#_Toc232864413)

[4.3.6 Fulfill Cash Trade Request as Deal Done 151](#_Toc232864414)

[4.3.7 Cancel Cash Trade Request as Deal Cancel 152](#_Toc232864415)

[4.3.8 Check Partial Fulfill or Partial Decline Cash Trade Request Status 153](#_Toc232864416)

[4.4 Manage Bank Account Balances 154](#_Toc232864417)

[4.4.1 Schedule Jobs for Bank Account Balance Initialization (Optional) 154](#_Toc232864418)

[4.4.2 Create Bank Account Balances 157](#_Toc232864419)

[4.4.3 Import Bank Account Balances 158](#_Toc232864420)

[4.4.4 Edit Bank Account Balances 159](#_Toc232864421)

[4.4.5 Check Bank Account Balances 160](#_Toc232864422)

[4.5 Cash Flows Reconciliation 162](#_Toc232864423)

[4.5.1 Schedule Automated Cash Flow Reconciliation 163](#_Toc232864424)

[4.5.2 Review Reconciliation Results 167](#_Toc232864425)

[4.5.3 Undo Reconciliation 168](#_Toc232864426)

[4.5.4 Reconcile Unmatched Transactions 169](#_Toc232864427)

[4.5.5 Analyze Cash Position 171](#_Toc232864428)

[4.6 Cash Snapshot Management 171](#_Toc232864429)

[4.6.1 Analyze Cash Position 172](#_Toc232864430)

[4.6.2 Schedule Cash Snapshots Capture 172](#_Toc232864431)

[4.6.3 Capture Cash Snapshots 174](#_Toc232864432)

[4.6.4 Request Investment or Funding 176](#_Toc232864433)

[4.6.4.1 Initiate Bank Transfer 176](#_Toc232864434)

[4.6.4.2 Cash Concentration (2U8) 176](#_Toc232864435)

[4.6.4.3 Initiate Cash Trade Request 176](#_Toc232864436)

[4.7 Instant Balances (Optional) 176](#_Toc232864437)

[4.7.1 Monitor Instant Balances 177](#_Toc232864438)

[4.7.2 Manage Bank Message 178](#_Toc232864439)

[4.8 Manage Liquidity Item Transfer 179](#_Toc232864440)

[4.9 Situation Handling: Date Difference Warning for FI Flows 181](#_Toc232864441)

[4.9.1 Monitor Situations 181](#_Toc232864442)

[4.9.2 Check Notification 182](#_Toc232864443)

[4.10 Situation Handling: Bank Account Balance Threshold Exceeded 183](#_Toc232864444)

[4.10.1 Monitor Situations 183](#_Toc232864445)

[4.10.2 Check Notification 184](#_Toc232864446)

[4.11 Cash Reports 185](#_Toc232864447)

[4.11.1 Schedule Jobs for Bank Statement Monitor 185](#_Toc232864448)

[4.11.2 Bank Statement Monitor 187](#_Toc232864449)

[4.11.3 Intraday Bank Statement Monitor 189](#_Toc232864450)

[4.11.3.1 Define Monitoring Rules for Intraday Bank Statement Monitor 189](#_Toc232864451)

[4.11.3.2 Assign Monitoring Rule to Bank (Optional) 190](#_Toc232864452)

[4.11.3.3 Define Bank Account to Monitor 191](#_Toc232864453)

[4.11.3.4 Monitor Intraday Bank Statement 193](#_Toc232864454)

[4.11.4 Monitor Bank Account Balances 194](#_Toc232864455)

[4.11.5 Short Term Cash Positioning 195](#_Toc232864456)

[4.11.6 Cash Flow Analyzer 198](#_Toc232864457)

[4.11.7 Actual Liquidity Analysis 201](#_Toc232864458)

[4.11.8 Document Chain Tracing for Cash Flow 203](#_Toc232864459)

[4.11.9 Check Cash Position (Smart Business) 204](#_Toc232864460)

[4.11.10 Check Liquidity Items on G/L Accounts 205](#_Toc232864461)

[4.11.11 Check Cash Flow Items 206](#_Toc232864462)

[4.11.12 Cash Flow Comparison – By Date Range 207](#_Toc232864463)

[4.11.13 Cash Flow Comparison – By Timestamp 208](#_Toc232864464)

[5 Appendix 210](#_Toc232864465)

[5.1 Process Chains 210](#_Toc232864466)

## Purpose

Overview

Advanced Cash Operations offers a consistent view of your actual cash position and short/mid-term cash forecasts. Drill-down features are provided for the detailed transactions and rich dimensions are provided for the analysis. You can also compare the actual and forecasted cash flow with forecasted figures.

This scope item also allows you to make bank transfer and track its status, and to approve the bank payments and monitor the payment processing status.

|  |
| --- |
| Caution All of the procedures are only required if you have adopted Cash Management Full, which requires an additional license for SAP Cash Management. If you use Basic Cash Management, skip all steps in this document. |

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
| Cash Manager | SAP_BR_CASH_MANAGER | Cash Management | SAP_BR_CASH_MANAGER | Suggested sample user CASH_MANAGER representing the business role Cash Manager. |
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST | Suggested sample user CASH_SPECIALIST representing the business role Cash Management Specialist. |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC | Suggested sample user AP_ACCOUNTANT representing the business role Account Payable Accountant. |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT | Suggested sample user AR_ACCOUNTANT representing the business role Accounts Receivable Accountant. |
| Accounts Payable Manager | SAP_BR_AP_MANAGER | Accounts Payable | SAP_BR_AP_MANAGER | Suggested sample user AP_MANAGER representing the business role Accounts Payable Manager. |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | Suggested sample user BPC_EXPERT representing the business role Configuration Expert - Business Process Configuration. |
| Extensibility Specialist | SAP_BR_EXTENSIBILITY_SPEC | Extensibility Specialist | SAP_BR_EXTENSIBILITY_SPEC / SAP_CA_SPT_EXT_PC | Suggested sample user EXTENSIBILITY_SPEC representing the business role Extensibility Specialist. |
| Business Integration Specialist - Bank Integration | SAP_BR_BANK_INT_SPECIALIST | Business Integration Specialist - Bank Integration | SAP_BR_BANK_INT_SPECIALIST | Suggested sample user BANK_INT_SPECIALIST representing the business role Business Integration Specialist - Bank Integration. |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC | Suggested sample user BUSINESS_PROCESS_SPEC representing the business role Business Process Specialist. |

### Master Data, Organizational Data, and Other Data

Default Values

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. Depending on the operational focus of your company, the master data represents materials, customers, and vendors.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

The business process is enabled with this organization-specific master data, examples are provided in the next section.

Operational Focus

SAP Best Practices deliver standard values for more than one operational focus area, such as Services, Manufacturing, or Trade. This means that you may find more than one master data table. Use the master data that matches the operational focus of your company (Services, Manufacturing, or Trade).

|  |
| --- |
| Note Additional Default ValuesYou can test the scope item with other SAP Best Practices default values that have the same characteristics.Check your SAP ECC system to find out which other material master data exists. |

|  |
| --- |
| Note Using Your Own Master DataYou can also use customized values for any material or organizational data for which you have created master data. For more information on how to create master data, see the Master Data Procedures documentation. |

Use the following master data in the process steps described in this document:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Bank Key | 18121976 ,18121986 |  | Bank key |
| Country | AE |  | Country of bank key |
| Company Code | 3310 |  | Company code |
| G/L Account | 11001000, 11001020,11001080, and so on |  | G/L account for bank accounts |
| Chart of Accounts | YCOA |  | Chart of accounts |
| House Bank | AEBK1AEBK2 |  | House bank |
| House Bank Account | AEAC1 |  | House bank account is integrated in Bank account master data (BAM) |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) Scripts (MDS):

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BNG | Create G/L Account and Cost Element - MDS |

### Business Conditions

Before this test script can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J60 - Accounts Payable | Perform the relevant steps of payment run to vendors in the Accounts Payable (J60) test script. This is the prerequisite for the Outgoing Payment with BCM Approval Process section in this test script. |
| 16R - Bank Integration with SAP Multi-Bank Connectivity | This scope item Bank Integration with SAP Multi-Bank Connectivity(16R) is the prerequisite for the Instant Balances section in this test script. |
| 2F5 - Treasury Trading via Trading Platforms | This scope item Treasury Trading via Trading Platforms(2F5) is the prerequisite for the Cash Trade Request section in this test script. |
| J77 - Advanced Bank Account Management | This scope item Advanced Bank Account Management (J77) is the prerequisite for this test script. |

Activate Features

In a software update, SAP delivers certain features that could have an impact on your implemented solution initially in an inactive state. You can choose to already activate these features before they become available by default in a later release.

The test procedures in this document describe the software behavior when all features have been activated. It is a prerequisite for testing that you have activated all of the following features in each of your systems using the configuration activity Activate Features. For more information about this activity, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/3e94fcc37b42433b97d6aef0c830dc52.html) for SAP S/4HANA Cloud Public Edition.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

- Configure Your Solution:

Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

Navigate to Manage your Solution > Configure Your Solution. Search for Activate Features. In the search result, select the configuration activity and go to the next screen. Select the configuration step and choose Configure.

- SAP Central Business Configuration:

Log on to the project experience in SAP Central Business Configuration.

Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Features. Choose the link to navigate directly to the target system of SAP S/4HANA Cloud Public Edition. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

| Feature ID | Feature Title |
| --- | --- |
| FTGL_BS_CASH_SIMP_INTEGRATION | New Integration Strategy for Bank Statements and Cash Mgmt |

### Additional Manual Configuration

You have the option to enable two-factor authentication for the Approve Bank Payments app. If you enable two-factor authentication in the preliminary step Specify Optional User Authentication, you should completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you.

For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/526b9fb7b839fe7f50382bf3410568f2)

### Preliminary Steps

#### Maintain Full Scope for Cash Management

Use

In this activity, you maintain Full Scope for cash management.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Configure | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase view displays. |  |
| 4 | Filter List | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | A list of Configuration Items display with the filter criteria. |  |
| 5 | Select General Settings | Select the following row:Item Name: General Settings | The Configure Your Solution - General Settings view displays. |  |
| 6 | Define Basic Settings | From the Configuration Steps area, on the Define Basic Settings step, choose Configure. | The Change View "Define Basic Settings": Details view displays. |  |
| 7 | Select Full Scope | Make the following entries and choose Save.Cash Scope: Full Scope |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open General Settings for Cash Management | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Basic Settings.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Select Full Scope | Make the following entries and choose Save.Cash Scope: Full Scope |  |  |

|  |
| --- |
| Remember Basic Settings must be reviewed following any system upgrade or improvement before continuing any business operation in the system. When differences are found from previous activations, you must correct them in the configuration activity Define Basic Settings. |

#### Enable Snapshot (Optional)

Use

In this activity, you enable the snapshot feature. The snapshot feature allows the cash manager to see a past date cash position or forecast when testing the Check Cash Flow Items and Cash Flow Analyzer procedures. The difference between historical view and actual view can be analyzed and the cash flow forecast can be improved.

|  |
| --- |
| Caution If Basic Scope is adopted, enabling Snapshot produces an error. |

|  |
| --- |
| Caution If you enable Snapshot, it will consume quite a big database space. Please enable Snapshot only if it’s really needed.A daily scheduled background job SAP_FQM_DELETE_REGULAR (configured by variant) will automatically delete historical snapshot cash flows according to the setting maintained in configuration activity Define Basic Settings.You can also use the app Delete Data from One Exposure and choose Snapshot Cleanup to remove the old snapshot records. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Configure | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase view displays. |  |
| 4 | Filter List | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | A list of Configuration Items display with the filter criteria. |  |
| 5 | Select General Settings | Select the following row:Item Name: General Settings | The Configure Your Solution - General Settings view displays. |  |
| 6 | Define Basic Settings | From the Configuration Steps area, on the Define Basic Settings step, choose Configure. | The Define Basic Settings: Change: Details view displays. |  |
| 7 | Enable Snapshot | Select the Enable Snapshot checkbox. |  |  |
| 8 | Maintain Obsoleted Flows Processing Option | In the One Exposure Obsoleted Flows Processing Mechanism section, enter the following data:Obsoleted Flows Processing Option: System Default or Customer DefinedDays for Recorded Snapshot: <as needed>Note 30 days is set as system default value.Months for Specific Snapshots: <as needed>Note When snapshot is enabled, a daily scheduled background job SAP_FQM_DELETE_REGULAR (configured by variant) will automatically delete historical snapshot cash flows according to this system default setting or customer defined method. | One Exposure obsoleted flows processing option is defined. |  |
| 9 | Save | Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open General Settings for Cash Management | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Basic Settings.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Basic Settings": Details screen displays. |  |
| 3 | Enable Snapshot | Select the Enable Snapshot checkbox. |  |  |
| 4 | Maintain Obsoleted Flows Processing Option | In the One Exposure Obsoleted Flows Processing Mechanism section, enter the following data:Obsoleted Flows Processing Option: System Default or Customer DefinedDays for Recorded Snapshot: <as needed>Note 30 days is set as system default value.Months for Specific Snapshots: <as needed>Note When snapshot is enabled, a daily scheduled background job SAP_FQM_DELETE_REGULAR (configured by variant) will automatically delete historical snapshot cash flows according to this system default setting or customer defined method. | One Exposure obsoleted flows processing option is defined. |  |
| 5 | Save | Choose Save. |  |  |

|  |
| --- |
| Remember Define Basic Settings must be reviewed following any system upgrade or improvement before continuing any business operation in the system. When differences are found from previous activations, you must correct them in the configuration activity Define Basic Settings. |

#### Define Runtime Parameters for Flow Builder

Use

In this activity, you define runtime parameters for Flow Builder.

- If you enable the Apply Runtime Configuration function in Flow Builder, Flow Builder uses the runtime parameters you define in the configuration activity Define Runtime Parameters for Flow Builder for each company code individually.
- During Delta Run Mode, Flow Builder always uses the runtime parameters you have defined in the configuration activity Define Runtime Parameters for Flow Builder by company codes individually as the highest priority. If specific parameters can't be found for some company codes, Flow Builder uses the runtime parameters on the screen for these company codes.
- Flow Builder reads runtime parameters for given company codes from this configuration. If it doesn't find them, Flow Builder reads a default entry where the company code equals space.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Configure | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase view displays. |  |
| 4 | Filter List | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | A list of Configuration Items display with the filter criteria. |  |
| 5 | Select General Settings | Select the following row:Item Name: Cash Operations |  |  |
| 6 | Define Runtime Parameters for Flow Builder | From the Configuration Steps area, on the Define Runtime Parameters for Flow Builder step, choose Configure. | The Define Runtime Parameters for Flow Builder: Change view displays. |  |
| 7 | Maintain Parameters | Choose New Entries. Make the following entries and choose Save:CoCd: <company code>Merge Tax: <as needed>OvrActFlow : <as needed>Chain Step: <change as needed>Note The Flow Builder traces document chains step by step during flow generation. When the chain reaches the maximum number of steps for chain tracing, it stops, even if there are more document relationships. You can choose a value between 1 and 12 for the maximum number of steps. The default setting for chain tracing is 6 steps.Restriction of Clearing: <change as needed>Note The Flow Builder discards clearing relationships when clearing items exceed the value specified in the Restriction of Clearing function. You can set any value for the Restriction of Clearing. A value of 0 means no limitation, though this may affect performance. The default value is 200,000. | The runtime parameters for flow builder is maintained for the company code. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Runtime Parameters for Flow Builder | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Runtime Parameters for Flow Builder.Choose Open Documentation for the found line item to see more details about this configuration activity. |  |  |
| 3 | Maintain Parameters | Choose New Entries. Make the following entries and choose Save:CoCd: <company code>Merge Tax: <as needed>OvrActFlow : <as needed>Chain Step: <change as needed>Note The Flow Builder traces document chains step by step during flow generation. When the chain reaches the maximum number of steps for chain tracing, it stops, even if there are more document relationships. You can choose a value between 1 and 12 for the maximum number of steps. The default setting for chain tracing is 6 steps.Restriction of Clearing: <change as needed>Note The Flow Builder discards clearing relationships when clearing items exceed the value specified in the Restriction of Clearing function. You can set any value for the Restriction of Clearing. A value of 0 means no limitation, though this may affect performance. The default value is 200,000. | The runtime parameters for flow builder is maintained for the company code. |  |

#### Liquidity Items

##### Define Source Application Accounting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can make additional configuration for Financial Accounting (FI) in One Exposure.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution(F1241). |  |  |
| 3 | Filter List | Choose Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity ManagementItem Name: Cash Operations | The Change View “Source Application Accounting”: Overview screen is displayed. |  |
| 4 | Configuration | From the Configuration Steps area, on the Define Source Application Accounting step, choose Configure. |  |  |
| 5 | Define Source Application Accounting | Change the following entries for a specific company code per your requirement and choose Save:CoCd: 3310Accounting Scope: for example, Cash Position & Liquidity AnalysisCash Position Update Mode: for example, Deferred – Delta Table UpgradeNote You can configure update mode for cash position as needed.Liquidity Analysis Update Mode: for example, Close to Real Time | The source application accounting is defined for your company code. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Source Application Accounting | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Source Application Accounting.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View “Source Application Ac-counting”: Overview screen is displayed. |  |
| 3 | Define Source Application Accounting | Change the following entries for a specific company code per your requirement and choose Save:CoCd: 3310Accounting Scope: for example, Cash Position & Liquidity AnalysisCash Position Update Mode: for example, Deferred – Delta Table UpgradeNote You can configure update mode for cash position as needed.Liquidity Analysis Update Mode: for example, Close to Real Time | The source application accounting is defined for your company code. |  |

##### Define Basic Settings for Liquidity Analysis

Use

In this activity, you define basic settings for liquidity analysis, such as default liquidity Items & derivation tool for liquidity analysis.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution(F1241). |  |  |
| 3 | Configure | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase view displays. |  |
| 4 | Filter List | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | A list of Configuration Items display with the filter criteria. |  |
| 5 | Choose Configuration Items | Select the following row:Item Name: Cash Operations | The Configure Your Solution – Cash Operations view displays. |  |
| 6 | Define Basic Settings for Liquidity Analysis | From the Configuration Steps area, on the Define Basic Settings for Liquidity Analysis step, choose Configure. | The "General Settings for Liquidity Analysis" Details: Details view displays. |  |
| 7 | Default Liquidity item | Change the default liquidity item as needed. |  |  |
| 8 | Enable Query Evaluation from Bank Statement | Select Enable Query Evaluation from Bank Statement as needed.Note You can select this checkbox to evaluate query sequences from bank statement text information for liquidity item derivation for bank items in Flow Builder Plus. |  |  |
| 9 | Select Derivation Tool | Select the Derivation Tool as your needed and choose Save.For example: Q – Query Sequence. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Basic Settings for Liquidity Analysis | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Basic Settings for Liquidity Analysis.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The "General Settings for Liquidity Analysis" Details: Details view displays. |  |
| 3 | Default Liquidity item | Change the default liquidity item as needed. |  |  |
| 4 | Enable Query Evaluation from Bank Statement | Select Enable Query Evaluation from Bank Statement as needed.Note You can select this checkbox to evaluate query sequences from bank statement text information for liquidity item derivation for bank items in Flow Builder Plus. |  |  |
| 5 | Select Derivation Tool | Select the Derivation Tool as your needed and choose Save.For example: Q – Query Sequence. |  |  |

##### Define Derivation Rules – Query Sequence

###### Define Query Sequences

Use

In this activity, you can define query sequences.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution(F1241). |  |  |
| 3 | Configure | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase view displays. |  |
| 4 | Filter List | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | A list of Configuration Items display with the filter criteria. |  |
| 5 | Choose Configuration Items | Select the following row:Item Name: Cash Operations | The Configure Your Solution – Cash Operations view displays. |  |
| 6 | Define Query Sequences | From the Configuration Steps area, on the Define Query Sequences step, choose Configure. |  |  |
| 7 | Choose Origin | On the Determine Work Area:Entry popup screen, make the following entries and choose Continues(Enter).Origin: <as needed> | The "Define Query Sequences" Change view displays. |  |
| 8 | Create Query Sequence | Choose New Entries, make the following entries and choose Save.Query Sequence: <Query Sequence ID>Name: <Query Sequence Name>Description: <Query Sequence description> | The new query sequence is created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Define Query Sequences | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Query Sequences.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Choose Origin | On the Determine Work Area:Entry popup screen, make the following entries and choose Continues(Enter).Origin: <as needed> | The "Define Query Sequences" Change view displays. |  |
| 4 | Create Query Sequence | Choose New Entries, make the following entries and choose Save.Query Sequence: <Query Sequence ID>Name: <Query Sequence Name>Description: <Query Sequence description> | The new query sequence is created. |  |

###### Define Queries for Liquidity Item Derivation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define queries for liquidity item derivation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Define Queries for Liquidity Item Derivation (FLQQA1). | The Edit Query view displays. |  |
| 3 | Define Query | Make the following entries:Query ID: <Query ID>Name: <Query name>Description: <Query description>Liquidity Item: liquidity item |  |  |
| 4 | Maintain Conditions | Choose Conditions, make the conditions as needed. | The query is defined |  |

###### Assign Queries to Query Sequences

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you assign queries to query sequences.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Assign Queries to Query Sequence(FLQQA5). | The “Sequences”:Display view displays. |  |
| 3 | Choose Origin | Make the following entries:Origin: <C or D> |  |  |
| 4 | Select Sequence | Select a query sequence from sequence list, choose Queries under the left- side Dialog Structure. | The “Queries”:Change view displays. |  |
| 5 | Assign Query | Choose New Entries, make the following entries and Choose Save.No.: entry numberQuery ID: query IDLiquidity Item: liquidity item | The query is assigned to sequence. |  |

###### Assign Sequence to Company Codes

Use

In this activity, you can define the default derivation logic for liquidity items for company codes that have Cash Management activated. Each entry assigns a query sequence and a derivation function to a company code, which the system uses to derive liquidity items for that company code. For example, liquidity items can be determined based

on the accounts referenced by the line items in documents posted to ledgers (G/L, accounts receivable, or accounts payable).

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Configure | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase view displays. |  |
| 4 | Filter List | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | A list of Configuration Items display with the filter criteria. |  |
| 5 | Choose Configuration Items | Select the following row:Item Name: Cash Operations | The Configure Your Solution – Cash Operations view displays. |  |
| 6 | Assign Sequence to Company Codes | From the Configuration Steps area, on the Assign Sequences to Company Codes step, choose Configure. | The "Assign Sequences to Company Codes" Change view displays. |  |
| 7 | Create New Entry | Choose New Entries, make the following entries and choose Save.CoCd: 3310Origin: <as needed>Query Sequence: Query Sequence created in previous step | The query sequence is assigned to a company code. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Assign Sequence to Company Codes | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Sequences to Company Codes.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The "Assign Sequences to Company Codes" Change view displays. |  |
| 3 | Create New Entry | Choose New Entries, make the following entries and choose Save.CoCd: 3310Origin: <as needed>Query Sequence: Query Sequence created in previous step | The query sequence is assigned to a company code. |  |

##### Liquidity Calculation: Manage Query Sequences (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can manage query sequences to derive liquidity items by activating Cash Register in the configuration activity Define Basic Settings. The origin of liquidity item includes Origin C (From Clearing Information) and Origin D (From Invoices).

Prerequisites

Make sure you have enabled Cash Register in the Preliminary steps the Basic Cash Operations ([BFB](https://me.sap.com/processnavigator/SolS/SolS-013/2508/SolP/BFB)) test script.

Define the queries with liquidity item Origin C/D in the previous Define Queries for Liquidity Item Derivation procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Liquidity Calculation - Manage Query Sequences (FCLM_FLQGRP). | The Change View " Management Query Sequences ": Overview screen displays. |  |
| 3 | Create Query Sequence | Choose New Entries, make the following entries and choose Save:Query Sequence: for example, CQ1Origin: for example, From Clearing InformationName: <name for query sequence>Description: <description for query sequence> | The query sequence is created. |  |
| 4 | Assign Queries to Query Sequences | Select the query sequence created in previous step, then choose Queries for Sequence in left Dialog Structure.Choose New Entries, make the following entries and choose Save:No.: <entry number>Query ID: <Query ID created in previous step>Inactive: <deselected> | The query is assigned to sequence. |  |
| 5 | Assign Sequence to Company Codes | Choose New Entries, make the following entries and choose Save.Query Sequence: <Query Sequence created in previous step>Origin: <default>CoCd: 3310 | The query sequence is assigned to a company code. |  |

##### Liquidity Calculation: G/L Classification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can define a default liquidity item for each G/L Account and it introduces the function of G/L Account Classification. When you post a document or mass rebuild liquidity items, the configured liquidity items in this app are read in specific conditions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Liquidity Calculation: G/L Classification (FCLM_INFOACC). | The Change View "Liquidity Calculation:G/L Classification": Overview screen displays. |  |
| 3 | Create New Entries | Choose New Entries, make the following entries and choose Save:Chart of Accounts: YCOACompany Code: <your company code or empty>Account from: <account from>Account to: <account to>Note Account From and Account To are used in combination. If Account To is empty, it’s regarded as a single value. In this case, the symbol “+” can be used for fuzzy query. If the value of Account To is added, it’s an interval query. If the symbol “+” is used in this case, it’s regarded as an interval value rather than a fuzzy query. If there's a real G/L account that does contain "+" which needs to be operated, you need to fill in the same value with "+" in both Account From and Account To.Class: <as needed>Liquidity Item: <default liquidity item>For testing, refer to the example table below to classify the G/L account:Tip In the App Liquidity Calculation: G/L Classification (FCLM_INFOACC), you can use the Keyboard shortcut Copy/Paste to quickly add the following entries:Chart of AccountsCompany CodeAccount FromAccount ToClassification of G/L AccountLiquidity ItemYCOA121000003KB001YCOA121100003KB007YCOA121120003KB003YCOA121200003KB001YCOA123000003KB001YCOA123030000KB001YCOA124110003KB007YCOA124200003KB007YCOA125000003KB011YCOA125010000KB011YCOA125400000KB003YCOA125410000KB003YCOA125420000KB003YCOA125430000KB003YCOA125610000KB004YCOA131000000KB004YCOA135000000KB004YCOA136000000KB004YCOA141070003KB007YCOA152000000KB005YCOA153000000KB007YCOA160000000KB012YCOA160010000KB012YCOA160020000KB012YCOA160030000KB012YCOA160040000KB012YCOA160050000KB012YCOA160060000KB012YCOA160070000KB012YCOA160080000KB012YCOA160090000KB012YCOA180200000KB011YCOA193200000KB012YCOA211000003KB004YCOA211050003KB004YCOA211900003KB007YCOA212000003KB004YCOA213000003KB004YCOA213030000KB004YCOA215010000KB005YCOA215020000KB005YCOA215030000KB005YCOA215050000KB005YCOA215080000KB005YCOA215090000KB005YCOA217200000KB007YCOA217201003KB003YCOA225100000KB014YCOA225120000KB014YCOA310000000KB015YCOA320000000KB015YCOA321000000KB015YCOA410000000KB001YCOA410004000KB001YCOA410010000KB001YCOA410015000KB001YCOA410900000KB003YCOA525900000KB001YCOA610020000KB004YCOA610030000KB004YCOA610040000KB004YCOA610050000KB004YCOA610060000KB004YCOA610070000KB004YCOA610080000KB004YCOA610100000KB005YCOA610200000KB005YCOA610210000KB005YCOA610211000KB005YCOA610220000KB005YCOA610221000KB005YCOA610510000KB005YCOA610520000KB005YCOA610600000KB005YCOA610610000KB005YCOA610620000KB005YCOA610630000KB005YCOA611000000KB005YCOA611010000KB005YCOA611020000KB005YCOA611030000KB005YCOA611040000KB005YCOA612000000KB005YCOA612010000KB005YCOA614000000KB004YCOA614010000KB004YCOA615000000KB004YCOA630000000KB004YCOA630005000KB004YCOA630010000KB004YCOA630020000KB004YCOA630030000KB004YCOA630040000KB004YCOA630050000KB004YCOA630060000KB004YCOA630070000KB004YCOA630080000KB004YCOA630090000KB004YCOA650000000KB004YCOA650005000KB004YCOA650010000KB004YCOA650020000KB004YCOA650030000KB004YCOA650040000KB004YCOA650080000KB004YCOA650083000KB004YCOA650085000KB004YCOA650090000KB004YCOA650500000KB004YCOA651000000KB004YCOA651500000KB004YCOA652000000KB004YCOA653000000KB004YCOA653010000KB004YCOA654000000KB004YCOA659000000KB004YCOA660000000KB007YCOA660006000KB003YCOA700200000KB010YCOA700300000KB010YCOA701000000KB011YCOA703000000KB011YCOA703001000KB011YCOA711000000KB017YCOA713000000KB017YCOA750010000KB006YCOA750020000KB006YCOA750021000KB006YCOA750030000KB006YCOA750040003KB006YCOA750050003KB006YCOA750070000KB006YCOA942280000KB006 | G/L Classification for liquidity calculation is defined. |  |

##### Schedule Job for Rebuild Tool for Liquidity Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you rebuild liquidity item in accounting document .

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist . |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Job for Rebuild Tool for Liquidity Item (F6770). | The Application Jobs view displays. |  |
| 3 | Create a New Application Job | On the current view, choose Create to create an application job. | The New Job: Rebuild Liquidity Items in Accounting Documents view displays. |  |
| 4 | Choose Job Template | In the Template Selection section, make following entries:Job Template: Rebuild Liquidity Items in Accounting DocumentsJob Name: for example：Rebuild liquidity item in accounting document |  |  |
| 5 | Maintain Scheduling Options | Choose Step 2. In the Scheduling Options section, make the following entriesStart Immediately: <Selected or deselected>If you choose star immediately, other parameter do not need to maintain.Start: <current time or any future time as needed>Time Zone: <time zone>For Recurrence Pattern, choose Define Recurrence Pattern.In the Scheduling Information dialog box, the additional scheduling options are available.Recurrence Pattern: for example, WeeklyEvery: for example, 1On: for example, MondayEnd: OptionalOn Non-Working Day: OptionalCalendar: for example, Germany(Standard)Choose OK. | If you would like to run this job immediately, the check-box of Start Immediately should be selected.If you schedule this job at some time in the future, the Start and Time Zone should be defined. |  |
| 6 | Maintain Parameter | Choose Step 3. In Parameter section and make the following entries:Accounting Documents:Company code: For example: 3310Fiscal Year: For example: <current fiscal year>Journal Entry: <as needed>Journal Entry Type: <as needed>Posting Date: <as needed>Journal Entry Date: <as needed>Control Parameters sectionRebuild Flows for Chged Items: <Selected>Test Run: <Deselected>Display Changed Items Only: <as needed>Package Size: <change as needed>Parallel Run: <as needed>Note: If you keep parameters empty, that means all cases will be included in the job. | Parameters are maintained. |  |
| 7 | Check | Choose Check. |  |  |
| 8 | Run this Application Job | Choose Schedule to run this application job. |  |  |
| 9 | Check Application Jobs Log | Choose Go to update the job status. When your job’s status change to Finished, you choose Log navigate to the Job Log. | Job log displays. |  |

##### Define Liquidity Item Derivation Mode for Flow Builder

Use

In this activity, you can define the liquidity item derivation mode for liquidity analysis flows for Flow Builder.

You have two options for the liquidity item derivation mode:

- Derive Liquidity Item Online - Query sequences are evaluated during the chain tracing to derive liquidity items.
- Fetch Liquidity Item from Table BSEG - Liquidity items are directly fetched from BSEG which were derived when the accounting document is posted.

If you want to have liquidity items derived from the query sequences in real-time, choose Derive Liquidity Item Online. This mode only works when the liquidity analysis update mode of the corresponding company code is Deferred.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Configure | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase view displays. |  |
| 4 | Filter List | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | A list of Configuration Items display with the filter criteria. |  |
| 5 | Choose Configuration Items | Select the following row:Item Name: Cash Operations | The Configure Your Solution – Cash Operations view displays. |  |
| 6 | Define Liquidity Item Derivation Mode for Flow Builder | From the Configuration Steps area, on the Define Liquidity Item Derivation Mode for Flow Builder step, choose Configure. | The "Define Liquidity Item Derivation Mode for F.." Change view displays. |  |
| 7 | Create New Entry | Choose New Entries, make the following entries and choose Save.For example:Entry 1)CoCd: <empty>Liquidity Item Derivation Mode: for example: Fetch Liquidity Item from table BSEGEntry 2)CoCd: 3310Liquidity Item Derivation Mode: for example, Derive Liquidity Item Online | The liquidity item derivation mode for liquidity analysis flows for Flow Builder is defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Define Liquidity Item Derivation Mode for Flow Builder | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Liquidity Item Derivation Mode for Flow Builder.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The "Define Liquidity Item Derivation Mode for F.." Change view displays. |  |
| 3 | Create New Entry | Choose New Entries, make the following entries and choose Save.For example:Entry 1)CoCd: <empty>Liquidity Item Derivation Mode: for example: Fetch Liquidity Item from table BSEGEntry 2)CoCd: 3310Liquidity Item Derivation Mode: for example, Derive Liquidity Item Online | The liquidity item derivation mode for liquidity analysis flows for Flow Builder is defined. |  |

##### Flow Builder: Stop Condition (Optional)

Purpose

In Flow Builder, the technical concept for chain step is removed, now you can use stop condition to shorten/stop the chain on business purpose.

|  |
| --- |
| Note The flow builder’s profile for stop condition is used for Accounting Scope “Cash Position & Liquidity Analysis” or “Liquidity Analysis Only”. |

###### Define Profile for Stop Condition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define a profile for stop condition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Flow Builder: Stop Condition (S_ER9_11002333). | The Change View “Flow Builder: Stop Condition”: Overview screen displays |  |
| 3 | Create New Profile | Choose New Entries. Make the following entries and choose Save.Profile: <Profile Name>Profile Description: <Profile Description> | The New Entries: Overview of Added Entries screen displays. |  |
| 4 | Define Filter Conditions | Select the created profile and choose Define Filter Conditions. | The Maintain Stop Conditions For Flow Builder screen displays. |  |
| 5 | Maintain Stop Conditions For Flow Builder | Make the following entries per your business requirement and choose Save Stop Conditions.G/L Account: <per your requirement>Account Type: <per your requirement>Planning Level: <per your requirement>Supplier: <per your requirement>Customer: <per your requirement>Posting Key: <per your requirement>Choose Continue to confirm the Information popup screen. | The stop condition is maintained. |  |

###### Assign Flow Builder Profile to Company Code

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define the association between the company code and profile of stop conditions.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Search | Choose Configure Your Solution. |  |  |
| 4 | Application and Subapplication Area | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the following row:Item Name:Cash Operations | Configuration steps are displayed for the selected row. |  |
| 6 | Select Configuration Steps | Choose Configure to configure the following row:Step Name: Define Profile for Flow Builder:Stop Conditions | The "Define Profile for Flow Builder:Stop Condi..": Change displays. |  |
| 7 | Assign Profile to Company Code | Choose a company code and make the following entries and choose Save:For example:Cocd: 3310Profile: <the profile for flow builder’s stop condition created in previous step> | The profile for flow builder’s stop condition is assigned for a specific company code. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Profile for Flow Builder: Stop Conditions | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Profile for Flow Builder:Stop Conditions.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The "Define Profile for Flow Builder:Stop Condi..": Change displays. |  |
| 3 | Assign Profile to Company Code | Choose a company code and make the following entries and choose Save:For example:Cocd: 3310Profile: <the profile for flow builder’s stop condition created in previous step> | The profile for flow builder’s stop condition is assigned for a specific company code. |  |

##### Manage Liquidity Items Hierarchies (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create Liquidity Item Hierarchies.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Liquidity Item Hierarchies (F4966). | The Manage Liquidity Item Hierarchies view displays. |  |
| 3 | Create a New Hierarchy | Choose Create, make the following entries and choose Create in the New Hierarchy dialog box:Type: Liquidity Item HierarchyHierarchy ID: <your hierarchy ID>Hierarchy Description: <description for hierarchy>Valid From: <valid from date>Valid To: <default value>Note: <your note> | Create a new liquidity item hierarchy.Note If you have legacy liquidity item hierarchies, you can choose Import Hierarchy to migrate them one by one. |  |
| 4 | Navigate to Timeframe pane | Click your hierarchy to navigate to right pane. |  |  |
| 5 | Add New Subnode | Choose Edit. In the Nodes section of right pane, choose the highest node and choose +(Add) at the right side of the row. Make the following entries in the Add Node dialog box and choose OK.Subnode: SelectedNode:<select nodes(liquidity items) via search help F4>Note You can also choose Fast Entry (beside Add +) to assign liquidity items as subnode. | The liquidity items are assigned as nodes of liquidity item hierarchy. |  |
| 6 | Assign Liquidity Item to a Node | Choose the new subnode created in the previous step and choose +(Add) at the right side of the row. Make the following entries in the Add Node dialog box and choose OK.Liquidity Item: SelectedLiquidity Item:<select liquidity items via search help F4>Note You can also choose More (beside Add +), from the dropdown menu, choose Fast Entry to assign liquidity items. | The liquidity items are assigned to a node of liquidity hierarchy. |  |
| 7 | Save | Choose Save. | The liquidity item hierarchy is well structured and maintained. |  |
| 8 | Activate | Choose Activate. | The liquidity item hierarchy newly maintained is successfully activated. Its status has been converted into Active. |  |
| 9 | Export Liquidity Item Hierarchy to Spreadsheet | Choose Export to Spreadsheet from the dropdown menu. | A new excel spreadsheet containing the liquidity item hierarchy structure and contents is exported and generated in the specified folder path.Open the spreadsheet to go through the liquidity item hierarchy details. |  |

##### Set Block Date for Actual Cashflows

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can define blocking date range for actual flows in Liquidity Analysis.

The Blocked Date program determines whether FI documents with value or posting dates are blocked from generating into One Exposure. FI documents with dates prior to or equal to the blocking dates are blocked from generating level 3 actual flows in One Exposure.

|  |
| --- |
| Note Since the blocking date application only applies to level 3 cash flows in Liquidity Analysis, the account scope should be set as Cash Position & Liquidity Analysis or Liquidity Analysis Only via configuration activity (105487) Define Source Application Accounting.If you do not want to block level 3 actual flows generation in One Exposure, skip this procedure. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Set Block Date for Actual Cashflows | Open Set block date for actual cashflows (S_ER9_11002196). | The "Flow Builder:Blocked Date": Change view displays. |  |
| 3 | New Entry | Choose New Entries | The New Entries: Overview of Added Entries view displays. |  |
| 4 | Maintain Block Date Range | Make the following entriesCoCd: 3310Trans Date: <Transaction date>Posting Date: <Posting date> | The block date range for actual flows in liquidity analysis is maintained. |  |
| 5 | Save | Choose Save. |  |  |

#### Payment Approval

##### Maintain Payment Approver for Bank Accounts

Context

This activity describes how to maintain the payment approver for existing bank accounts as a prerequisite. Payment signatories work as approvers in the Approval and Bank Integration section of the scope item [J78 Advanced Cash Operations](https://me.sap.com/processnavigator/SolP/J78).

Procedure

Finish the Maintain Payment Approver for Multiple Bank Accounts procedure of the scope item [J77 Advanced Bank Account Management](https://me.sap.com/processnavigator/SolP/J77) for the following two existing bank accounts:

- Bank account 0000000693123456, bank key 18121976, country/region AE
- Bank account 0000000693123456, bank key 18121986, country/region AE

|  |
| --- |
| NoteIf the Unlimited Approval field is selected for the payment approvers, it won’t take the amount setting of this approver into consideration during BCM approval process.Please make sure you have assigned all payment approver groups of the approval pattern that you want to use in the payment approval process. If not, the payment approval pattern will be invalid, no payment approvers can be found during the BCM approval process, and the payment approval process will also fail. After you maintain the payment approver for the bank accounts, you can check if there are valid payment approval steps. To do so, open the Manage Bank Accounts (F1366A) app, choose the Payment Approvers tab, and choose Show Approval Steps. |

##### Specify Optional User Authentication (Optional)

Purpose

In this step, you have the option to enable two-factor authentication for the Approve Bank Payments app. If you enable two-factor authentication, the business user submitting payment batches for processing by the bank will be asked to authenticate their identity using SAP Cloud Platform Identity Authentication (IAS).

Note this functionality is only for approving outgoing payments using the Approve Bank Payments Fiori app.

Note that SAP Cloud Platform Identity Authentication are separate products. You must have an active account in SAP Cloud Platform Identity Authentication to use two-factor authentication as described in the Set-Up Instructions for this scope item.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Search | Choose Configure Your Solution. |  |  |
| 4 | Application and Sub-application area | Make the following entries:Application Area: FinanceSub Application Area: Bank Communication Management | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the following row:Item Name:Approve Bank Payments | Configuration steps are displayed for the selected row. |  |
| 6 | Select Configuration Steps | Choose Configure to configure the following row:Step Name: Specify Optional User Authentication | The Change View “Specify Optional User Authentication”: Overview displays. |  |
| 7 | Add New Entry | Choose New Entries and make the following entries and choose Save:Authentication Type: for example, <Authentication by IAS is on> | Two-factor authentication for the Approve Bank Payments app is enabled. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Specify Optional User Authentication | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Specify Optional User Authentication.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View “Specify Optional User Authentication”: Overview screen displays. |  |
| 3 | Add New Entry | Choose New Entries and make the following entries and choose Save:Authentication Type: for example, <Authentication by IAS is on> | Two-factor authentication for the Approve Bank Payments app is enabled. |  |

##### Define Automatic Approval/Rejection for Bank Account Master Data

Purpose

In this step, you can set what should be done in case of missing approvals. You will have 3 possible actions as following:

01: Auto-Rejection when Approval Pattern not Found or List Empty

02: Auto-Rejection when Approval List Empty

03: Auto-Approve when Approval List Empty

|  |
| --- |
| Note If no value is maintained for this customizing , default value 03 will be used for all payment batches. This means the payment batches are auto-approved in case the approval list for House Bank Account is empty.If your payment batch is automatically rejected, you might also reverse all payment documents related to this payment batch to be able to collect them as open items in another payment batch. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Search | Choose Configure Your Solution. |  |  |
| 4 | Application and Subapplication area | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the following row:Item Name:Bank Account Management | Configuration steps are displayed for the selected row. |  |
| 6 | Select Configuration Steps | Choose Configure to configure the following row:Step Name: Define Settings for Bank Account Master Data |  |  |
| 7 | Define Automatic Approval/Rejection | Double-click Define Automatic Approval/Rejection in the Dialog Structure of left side. | The Define Automatic Approval/Rejection displays. |  |
| 8 | Add New Entry | Choose New Entries and make the following entries and choose Save:For example:CoCd: 3310Appr/Rjct: eg: <Auto Rejection when Approval Pattern not Found or List Empty> | The Automatic Approval/Rejection setting for Bank account master data is defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Define Settings for Bank Account Master Data | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Settings for Bank Account Master Data.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Define Automatic Approval/Rejection | Double-click Define Automatic Approval/Rejection in the Dialog Structure of left side. | The Define Automatic Approval/Rejection view displays. |  |
| 4 | Add New Entry | Choose New Entries and make the following entries and choose Save:For example:CoCd: 3310Appr/Rejection: eg: <Auto Rejection when Approval Pattern not Found or List Empty> | The Automatic Approval/Rejection setting for Bank account master data is defined. |  |

##### Fix Errors for Payment Batches (Optional)

Purpose

In this step, you can enable fixing functionalities for payment batches in your batch and payment monitor. You can use these settings to enable several functionalities:

- Correct mismatch of statuses
- Set payment batches to status "Automatically Rejected" (IBC20)
- Mass reset and reverse of payment documents within payment batch items
- Add missing approvers to payment batches
- Retry payment medium creation

Prerequisites

You have maintained the proper authorizations including restriction type BNK_RMDT, which allows you to restrict authorizations for processing payment batches and payment batch remediations. It restricts the possible activities to Display, Execute and Read and the possible payment batch remediations to Mass Reset and Reverse, Set Status to Automatically Rejected and Retry Payment Medium Creation.

You have taken the required actions to enable fixing functionalities, for example, manually resetting and reversing several payment documents to enable the Mass Reset and Reverse functionality or rejecting or reversing all payment documents to enable setting the status Automatically Rejected (IBC20).

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Search | Choose Configure Your Solution. |  |  |
| 4 | Application and Subapplication Area | Make the following entries:Application Area: FinanceSub Application Area: Bank Communication Management | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the following row:Item Name: Approve Bank Payments | Configuration steps are displayed for the selected row. |  |
| 6 | Select Configuration Steps | Choose Configure to configure the following row:Step Name: Fix Errors for Payment Batches |  |  |
| 7 | Fix Errors for Payment Batches | Choose New Entries and make the following entries and choose Save:For example:Entry 1)CoCd: <empty>House Bk: <empty>Status: for example IBC01 Payment Batch CreatedAgentsFix: selectedAutoReject: selectedMassRstRev: selectedMinRvrdltm: for example, 03MassRevRsn: for example, 01Entry 2)CoCd: <empty>House Bk: <empty>Status: for example, IBC02 In ApprovalAgentsFix: selectedPayMCreate: selectedAutoReject: selectedMassRstRev: selectedMinRvrdltm: for example, 03MassRevRsn: for example, 01Entry 3)CoCd: <empty>House Bk: <empty>Status: for example,IBC03 Released in CompanyPayMCreate: selectedAutoReject: selectedMassRstRev: selectedMinRvrdltm: for example, 03MassRevRsn: for example, 01Entry 4)CoCd: <empty>House Bk: <empty>Status: for example, IBC15 Payment Medium CreatedAutoReject: selectedMassRstRev: selectedMinRvrdltm: for example, 03MassRevRsn: for example, 01Entry 5)CoCd: <empty>House Bk: <empty>Status: <empty>StatusFix: selectedEntry 6)CoCd: <empty>House Bk: <empty>Status: for example, IBC16 Released in CompanyPayMCreate: selected |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Fix Errors for Payment Batches | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Fix Errors for Payment Batches.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Add New Entry | Choose New Entries and make the following entries and choose Save:For example:Entry 1)CoCd: <empty>House Bk: <empty>Status: for example, IBC01 Payment Batch CreatedAgentsFix: selectedAutoReject: selectedMassRstRev: selectedMinRvrdltm: for example, 03MassRevRsn: for example, 01Entry 2)CoCd: <empty>House Bk: <empty>Status: for example, IBC02 In ApprovalAgentsFix: selectedPayMCreate: selectedAutoReject: selectedMassRstRev: selectedMinRvrdltm: for example, 03MassRevRsn: for example, 01Entry 3)CoCd: <empty>House Bk: <empty>Status: for example, IBC03 Released in CompanyPayMCreate: selectedAutoReject: selectedMassRstRev: selectedMinRvrdltm: for example, 03MassRevRsn: for example, 01Entry 4)CoCd: <empty>House Bk: <empty>Status: for example, IBC15 Payment Medium CreatedAutoReject: selectedMassRstRev: selectedMinRvrdltm: for example, 03MassRevRsn: for example, 01Entry 5)CoCd: <empty>House Bk: <empty>Status: <empty>StatusFix: selectedEntry 6)CoCd: <empty>House Bk: <empty>Status: for example, IBC16 Released in CompanyPayMCreate: selected |  |  |

##### Define Planning Levels for Cash Flow Payment Approval

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create the planning levels which are used for bank payment approval of cash flows.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Search | Choose Configure Your Solution. |  |  |
| 4 | Application and Subapplication Area | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the following row:Item Name: Cash Operations. | Configuration steps are displayed for the selected row. |  |
| 6 | Select Configuration Steps | Choose Configure to configure the following row:Step Name: Define Planning Levels. | The “Define Planning Levels”: Change view displays. |  |
| 7 | Create Planning Levels for Bank Payment Approval of Cash Flows | Choose New Entries and make the following entries and choose Save:For example:Item 1)Level: for example, PASource: BNKShort Text: PaytInApprPlanning Level Long Text: BCM In ApprovalItem 2)Level: for example, PBSource: BNKShort Text: PaytFinAppPlanning Level Long Text: BCM Final Approved | The planning levels for bank payment approval of cash flows is created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Planning Levels | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Planning Levels.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The “Define Planning Levels”: Change view displays. |  |
| 3 | Create Planning Levels for Bank Payment Approval of Cash Flows | Choose New Entries and make the following entries and choose Save:For example:Item 1)Level: for example, PASource: BNKShort Text: PaytInApprPlanning Level Long Text: BCM In ApprovalItem 2)Level: for example, PBSource: BNKShort Text: PaytFinAppPlanning Level Long Text: BCM Final Approved | The planning levels for bank payment approval of cash flows is created. |  |

##### Assign Planning Levels for Cash Flow Payment Approval

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you assign a planning level for bank payment approval of cash flows to a company code level. You can see cash flows for bank payment approval in different statuses by planning level.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Search | Choose Configure Your Solution. |  |  |
| 4 | Application and Subapplication area | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the following row:Item Name:Cash Operations | Configuration steps are displayed for the selected row. |  |
| 6 | Select Configuration Steps | Choose Configure to configure the following row:Step Name: Assign Planning Levels for Cash Flow Payment Approval | The Assign Planning Levels for Cash Flow Paymen..: Change screen displays. |  |
| 7 | Assign Planning Levels for Cash Flow Payment Approval | Choose New Entries and make the following entries and choose Save:For example:Item 1)CoCd: 3310Pmt Event: BCM In ApprovalLevel: for example, PAItem 2)CoCd: 3310Pmt Event: BCM Final ApprovedLevel: for example, PB | The planning levels is assigned for bank payment approval of cash flows.Note You can see cash flows for bank payment approval in different statuses by planning level in the Short-Term Cash Positioning (F5380), Check Cash Flow Items (F0735), Cash Flow Analyzer (F2332). |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Assign Planning Levels for Cash Flow Payment Approval | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Planning Levels for Cash Flow Payment Approval.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Planning Levels for Cash Flow Payment Approval..:Change screen displays. |  |
| 3 | Assign Planning Levels for Cash Flow Payment Approval | Choose New Entries and make the following entries and choose Save:For example:Item 1)CoCd: 3310Pmt Event: BCM In ApprovalLevel: for example, PAItem 2)CoCd: 3310Pmt Event: BCM Final ApprovedLevel: for example, PB | The planning levels is assigned for bank payment approval of cash flows.Note You can see cash flows for bank payment approval in different statuses by planning level in the Short-Term Cash Positioning (F5380), Check Cash Flow Items (F0735), Cash Flow Analyzer (F2332). |  |

#### Define Cash Position Profile

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can define profiles for any desired reporting structure to be used in short-term cash position. You can define the cash position hierarchy, balance period, the logic how bank account balance is shown and so forth in a specific profile based on your business scenario and requirement. You can also define filters and assign filters to your profile. With the predefined view, you can go through the balance data in the Short-Term Cash Positioning (F5380) app accordingly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Define Cash Position Profiles (F5399). | The Change View “Define Cash Position Profile’: Overview screen displays. |  |
| 3 | Create New Entry | Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 4 | Define Cash Position Profile | Make the following entries and choose Save:Cash Position Profile: for example, CPP_01Description: For example, CP Profile for short term CPHierarchy Settings section:Hierarchy Derivation: For example, Cash Pool and Bank Account Master DataNote You can define following hierarchy levels depending on the hierarchy derivation you choose.Hierarchy ID: <choose a bank account hierarchy via Value Help>Enable Top-Level Grouping: <No>Top-Level Group Name:: <n/a>Grouping Level 1: for example, <Company Code>Grouping Level 2: for example, <Bank Account Currency>Grouping Level 3: <n/a>NoteHierarchy Derivation - Bank Account Master DataYou can define up to three hierarchy levels. For each hierarchy level, you specify an attribute of the bank account master data that is used to group bank accounts, such as company code and currency.If you want to display all bank accounts in a flat list, leave the hierarchy level fields empty.Hierarchy Derivation - Cash Pool and Bank Account Master DataYou can organize your bank accounts using up to two hierarchy levels. The system then displays the bank accounts according to your defined hierarchy levels and the cash pool assignment of bank accounts. For bank accounts not assigned to any cash pool, only the defined hierarchy levels are considered.If you prefer to view bank accounts only by cash pool hierarchy, leave the hierarchy level fields empty. In this scenario, bank accounts assigned to cash pools are displayed according to the cash pool hierarchy, while bank accounts not assigned to cash pools are displayed in a flat list.Note Only Derived from Bank Account Hierarchy is chosen for hierarchy source, you need to fill in Hierarchy ID. The hierarchies were created in App Manage Bank Account Hierarchies (F4973), you can refer to the Manage Bank Account Hierarchies procedure of the scope item [J77 Advanced Bank Account Management](https://me.sap.com/processnavigator/SolP/J77).Display Options section:Report View: Balance View or Delta ViewBalance Overview: Showing Opening Balances or Showing Closing BalancesSource of Opening Balances: For example, Closing Value Date Balance (EoD)Note The value date balance is the interest-bearing balance for a particular day. It is calculated based on the ledger balance.The available balance indicates the funds available to the account holder for immediate use.Show Current Available Balance: <as needed>Show Overdue: For example, YesNote If selected Show Overdue checkbox, a separate overdue column will appear in short-term cash positioning for showing overdue amount.Include Overdue: For example, NoNote If selected Include Overdue checkbox, overdue amount will be added into the closing balance of the first period.Show Future: For example, YesHighlight in Red: Highlight Negative BalancesTime Settings section:Period Unit: For example, DaysIncrement: For example, 7Use Calendar Period: For example, NoShift Option: For example, Non-Working Day -> Next Working DayFactory Calendar ID: For example, 01Allow Key Date in the Past: For example, selectedCurrency and Conversion section:Enable Smart Currency: <as needed>Note With this function, the system can automatically decide the most appropriate currency to use for calculating aggregated balances for a hierarchy level in the Short-Term Cash Positioning (F5380) app.Display Currency: <as needed>Note In cases where neither the bank account currency nor the company code currency applies, the system resorts to the display currency. You are recommended to always specify a display currency for the hierarchy derivation for Bank Account Hierarchy.Exchange Rate Type: For example, MOverdraft Limits section:Show Granted Overdraft Limits: <as needed>Overnight Overdraft Type: <as needed>NoteShow Granted Overdraft Limits: By default, only the unused overdraft limits are displayed in the app. By setting this option, you can display the original overdraft limits granted by banks together with the unused overdraft limits.Overnight Overdraft Type: Specify an overdraft type that belongs to the Overnight Overdraft category. Then overdraft limits assigned to this overdraft type can be displayed in the Short-Term Cash Positioning (F5380) app when the profile is used.Note For existing customers before SAP S/4HANA Cloud Public Edition 2508, this feature will not automatically be available in your system but requires that you activate the feature Bank Account Overdraft Types in Cash Positioning (FTGL_BAM_BKACCT_OVERDRAFT_TYPE) in the configuration activity Activate Features.Reconciliation Settings section:Consider End-of-Day Reconciliation Result: For example, selectedConsider Intraday Reconciliation Result: For example, selected | A new Cash Position Profile is defined. |  |
| 5 | Define Filter (Option) | Steps from 5 to 11 are optional. You can define them as needed.Choose Define Filter in the left-side Dialog Structure. | The Change View “Define Filter”: Overview screen displays. |  |
| 6 | Maintain Filter Name | Choose New Entries. Make following entries and choose Save:Filter: CP_AFilter Description: Filter for cash position profile CPP_01 | Filter is created. |  |
| 7 | Define Filter Conditions | Select your filter, then choose Define Filter Conditions. | The Maintain Filter Conditions screen displays. |  |
| 8 | Maintain Parameter for Filter Condition | Maintain the following entries as needed and choose Save Filter Conditions. Choose Continue to confirm the Information popup screen.Bank Accounts:Company Code: 3310Bank Country/Region Key: <as needed>Bank Key: <as needed>Currency: <as needed>Technical ID: <as needed>Account Number: <enter an account number>Account Type: <as needed>Co Code Country/Region Key: <as needed>Contract Type: <as needed>Flows:Plng Lvl for Upcoming Flows: <as needed>Plng Lvl for Overdue Flows: <as needed>Overdue Days Considered: <as needed>Plng Lvl for Recent Flows: <as needed> | Filter conditions are created. |  |
| 9 | Back | Choose Back. |  |  |
| 10 | Assign Filter to Cash Position Profile | Choose Assign Filter to Cash Position Profile in the left-side dialog structure. Make the following entries in the popup screen and choose Enter.Cash Position Profile: CPP_01 | The Change View “Assign Filter to Cash Position Profile”: Overview screen displays. |  |
| 11 | Choose Filter to Assign | Choose New Entries. Enter your filter CP_A and choose Save. | Filter is assigned to the cash position profile. |  |

#### Cash Flow Reconciliations

Performing cash flow reconciliation between bank statement flows and forecasted cash flows helps you identify unfinished and unknown payments before end of business.

##### Define Planning Level

Purpose

In this activity, you define planning level for Residual Forecast.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Search | Choose Configure Your Solution. |  |  |
| 4 | Application and Subapplication Area | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the following row:Item Name: Cash Operations | Configuration steps are displayed for the selected row. |  |
| 6 | Select Configuration Steps | Choose Configure to configure the following row:Step Name: Define Planning Levels | The “Define Planning Levels”: Change view displays. |  |
| 7 | New Entries | Choose New Entries. |  |  |
| 8 | Define Planning Level | Make the following entries and choose Save:Planning level for Residual Forecast:Level: for example, RFSC : for example, <blank>Source: for example, BNKShort Text: for example, Res.Fore.Planning Level Long Text: for example, Residual Forecast | The planning level is defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Planning Levels | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Planning Levels.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The “Define Planning Levels”: Change view displays. |  |
| 3 | New Entries | Choose New Entries. |  |  |
| 4 | Define Planning Level | Make the following entries and choose Save:Planning level for Residual Forecast:Level: for example, RFSC: for example, <blank>Source: for example, BNKShort Text: for example, Res.Fore.Planning Level Long Text: for example, Residual Forecast | The planning level is defined. |  |

##### Define Memo Record Type

Purpose

In this activity, you define Memo record type Residual Forecast.

|  |
| --- |
| Note Ensure that you have defined the default memo record type for Intraday bank statement in procedure Define Memo Record of the Basic Cash Operations ([BFB](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/BFB)) test script.Also make sure you have defined planning levels for end-of-day and intraday bank statements in procedure Define Planning Levels for Bank Statements of the Basic Cash Operations ([BFB](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/BFB)) test script. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

You can choose to activate the New Integration Strategy for Bank Statements and Cash Mgmt feature.

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Search | Choose Configure Your Solution. |  |  |
| 4 | Application and Subapplication area | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the following row:Item Name: Cash Operations | Configuration steps are displayed for the selected row. |  |
| 6 | Select Configuration Steps | Choose Configure to configure the following row:Step Name: Define Memo Record Types | The Change View “Define Memo Record Types”: Overview view displays. |  |
| 7 | New Entries | Choose New Entries. |  |  |
| 8 | Define Memo Record Types | Make the following entries and choose Save:Memo record type for Residual Forecast:Memo Tp: for example, RFPlan.Lvl: for example, RFMemo Type Description: for example, Residual ForecastMemo Record Category: for example, Residual Forecast | The memo record types are defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Memo Record Types | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Memo Record Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View “Define Memo Record Types”: Overview screen displays. |  |
| 3 | New Entries | Choose New Entries. |  |  |
| 4 | Define Memo Record Types | Make the following entries and choose Save:Memo record type for Residual Forecast:Memo Tp: for example, RFPlan.Lvl: for example, RFMemo Type Description: for example, Residual ForecastMemo Record Category: for example, Residual Forecast | The memo record typs are defined. |  |

##### Define Profiles for Cash Flow Reconciliation

Purpose

In this step, you define profiles for performing cash flow reconciliation.

For each cash flow reconciliation profile, you define whether the profile is set to reconcile intraday bank statements or end-of-day bank statements, assign planning levels for bank statement flows and forecasted flows. You can also define a memo record type for creating memo records for residual flows and control whether residual flows should be automatically deactivated or manually deactivated.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Search | Choose Configure Your Solution. |  |  |
| 4 | Application and Subapplication Area | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the following row:Item Name: Cash Operations. | Configuration steps are displayed for the selected row. |  |
| 6 | Select Configuration Steps | Choose Configure to configure the following row:Step Name: Define Profiles for Cash Flow Reconciliation. | The “Define Profiles for Cash Flow Reconciliation ”: Change view displays. |  |
| 7 | New Entries | Choose New Entries. |  |  |
| 8 | Define Reconciliation Profile for Intraday Bank Statement | Make the following entries and choose Save:Reconciliation Profile: For example, INTRA_PROFReconciliation Profile Description: For example, <Intraday BS Reconciliation Profile>Reconciliation Strategy: Intraday Bank Statement ReconciliationEx.Rate Type: for example, MResidual Forecast: for example, RFNote Only the memo record types for residual flows can be used.Manual Residual Deactivation: <as needed>Note If you want to manually control the deactivation of residual flows, select the checkbox. | The reconciliation profile is defined. |  |
| 9 | Assign Planning Levels for Bank Statement Flows | Choose the profile, choose Assign Planning Levels for Bank Statement Flows in left dialog structure. |  |  |
| 10 | New Entry | Choose New Entry. Assign all relevant planning levels as needed, for example, INNote The planning level is used in intraday memo record. |  |  |
| 11 | Assign Planning Levels for Forecasted Flows | Choose Assign Planning Levels for Forecasted Flows in left dialog structure. |  |  |
| 12 | New Entry | Choose New Entry. Assign all relevant planning levels as needed. For example, AB,AU,CL,ZB,B2,B3,B5,B9,F1,RF and so on. |  |  |
| 13 | Save | Choose Save. |  |  |
| 14 | Back | Choose Back. |  |  |
| 15 | Define Reconciliation Profile for EoD Bank Statement | Repeat step from 7-13, define reconciliation profile for EoD Bank Statement as following:Reconciliation Profile: For example, EoD_PROFReconciliation Profile Description: For example, <EoD BS Reconciliation Profile>Reconciliation Strategy: EoD Bank Statement ReconciliationEx.Rate Type: for example, MResidual Forecast: for example, RFManual Residual Deactivation: <as needed>Assign Planning Levels for Bank Statement Flows: For example, EDNote The planning level is used for EoD bank statement.Assign Planning Levels for Forecasted Flows: Assign all relevant planning levels as needed. For example, AB, AU, F1, CL, ZB, RF and so on. | The reconciliation profile for EoD Bank Statement is defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Profiles for Cash Flow Reconciliation | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Profiles for Cash Flow Reconciliation.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The "Define Profiles for Cash Flow Reconciliation": Change screen displays. |  |
| 3 | New Entries | Choose New Entries. |  |  |
| 4 | Define Reconciliation Profile for Intraday Bank Statement | Make the following entries and choose Save:Reconciliation Profile: For example, INTRA_PROFReconciliation Profile Description: For example, Intraday BS Reconciliation ProfileReconciliation Strategy: Intraday Bank Statement ReconciliationEx.Rate Type: for example, MResidual Forecast: for example, RFNote Only the memo record types for residual flows can be used.Manual Residual Deactivation: <as needed>Note If you want to manually control the deactivation of residual flows, select the checkbox. | The reconciliation profile is defined. |  |
| 5 | Assign Planning Levels for Bank Statement Flows | Choose the profile, choose Assign Planning Levels for Bank Statement Flows in left dialog structure. |  |  |
| 6 | New Entry | Choose New Entry. Assign all relevant planning levels as needed, for example, INNote The planning level is used in intraday memo record. |  |  |
| 7 | Assign Planning Levels for Forecasted Flows | Choose Assign Planning Levels for Forecasted Flows in left dialog structure. |  |  |
| 8 | New Entry | Choose New Entry. Assign all relevant planning levels as needed. For example, AB,AU,CL,ZB,B2,B3,B5,B9,F1,RF and so on. |  |  |
| 9 | Save | Choose Save. |  |  |
| 10 | Back | Choose Back. |  |  |
| 11 | Define Reconciliation Profile for EoD Bank Statement | Repeat step from 6-9, define reconciliation profile for EoD Bank Statement as following:Reconciliation Profile: For example, EoD_PROFReconciliation Profile Description: For example, EoD BS Reconciliation ProfileReconciliation Strategy: EoD Bank Statement ReconciliationEx.Rate Type: for example, MResidual Forecast: for example, RFManual Residual Deactivation: <as needed>Assign Planning Levels for Bank Statement Flows: For example, ABNote The planning level is used for EoD bank statement.Assign Planning Levels for Forecasted Flows: Assign all relevant planning levels as needed. For example, AB, AU, CL, ZB, RF and so on. | The reconciliation profile for EoD Bank Statement is defined. |  |

##### Activate Reconciliation for Bank Account

Purpose

In this step, you make the reconciliation setting for bank accounts to include in cash flow reconciliations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Account Number: For example, 0000000693123456Bank Key: For example, 18121986Bank Country/Region: For example, AE |  |  |
| 4 | Navigation to Bank Account Details | Choose >. | The Bank Account view is displayed. |  |
| 5 | Edit | Choose Edit. |  |  |
| 6 | Activate Bank Statement Reconciliation | Choose the Bank Relationship tab, enter the following data and choose Save:Reconcile Bank Statements (End of Day): SelectedNote Include a bank account in cash flow reconciliation with end-of-day bank statements with forecasted cash flows.Reconcile Intraday Memo Records: SelectedNote Include a bank account in cash flow reconciliation with intraday bank statements. | Note When this change is relevant to dual control, the button is Submit for Activation. When this change is relevant to workflow, the button is Submit for Approval. |  |
| 7 | Activate Bank Account Change Request (Optional) | Note If Full Cash Management and Dual Control Revision Activate is applied in the basic settings, follow the Activate Bank Account Change Request procedure in the Advanced Bank Account Management(J77) test script. |  |  |
| 8 | Approve Bank Account Change Request (Optional) | Note If Full Cash Management and Workflow Revision Activate is applied in the basic settings, follow the Approve Bank Account Change Request procedure in the Advanced Bank Account Management (J77) test script. |  |  |

#### Cash Trade Request

##### Enable Cash Trade Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can enable the cash request functionality in the full scope of cash management. This functionality is integrated with Treasury and Risk Management (TRM).

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Search | Choose Configure Your Solution. |  |  |
| 4 | Application and Subapplication Area | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the following row:Item Name: General Settings | Configuration steps are displayed for the selected row. |  |
| 6 | Select Configuration Steps | Choose Configure to configure the following row:Step Name: Define Basic Settings | The Change View “Basic Settings”: Details view displays. |  |
| 7 | Enable Cash Trade Requests | Make the following entries and choose Save:Enable Cash Trade Requests: <selected> | The cash request functionality in the full scope of cash management is enabled. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Basic Settings | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Basic Settings.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View “Basic Settings”: Details screen displays. |  |
| 3 | Enable Cash Trade Requests | Make the following entries and choose Save:Enable Cash Trade Requests: <selected> | The cash request functionality in the full scope of cash management is enabled. |  |

##### Define Planning Level for Cash Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create the planning levels which are used for cash requests created, submitted and released.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Search | Choose Configure Your Solution. |  |  |
| 4 | Application and Subapplication area | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the following row:Item Name:Cash Operations | Configuration steps are displayed for the selected row. |  |
| 6 | Select Configuration Steps | Choose Configure to configure the following row:Step Name: Define Planning Levels | The "Define Planning Levels": Change view displays. |  |
| 7 | Create Planning Levels for Cash Requests | Choose New Entries and make the following entries and choose Save:For example:Planning level for cash request created:Level: C1Source: BNKShort Text: Created CRPlanning Level Long Text: Created Cash RequestPlanning level for cash request submitted:Level: C2Short Text: Submit. CRSource: BNKPlanning Level Long Text: Submitted Cash RequestPlanning level for cash request Released:Level: C3Source: BNKShort Text: Releas. CRPlanning Level Long Text: Released Cash Request | The planning levels for cash request are defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Planning Levels | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Planning Levels.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The "Define Planning Levels": Change screen displays. |  |
| 3 | Create Planning Levels for Cash Requests | Choose New Entries and make the following entries and choose Save:For example:Planning level for cash request created:Level: C1Source: BNKShort Text: Created CRPlanning Level Long Text: Created Cash RequestPlanning level for cash request submitted:Level: C2Short Text: Submit. CRSource: BNKPlanning Level Long Text: Submitted Cash RequestPlanning level for cash request Released:Level: C3Source: BNKShort Text: Releas. CRPlanning Level Long Text: Released Cash Request | The planning levels for cash request are defined. |  |

##### Assign Planning Level to Cash Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you assign the planning levels to cash requests with the status of created, submitted and released. You can see cash trade requests in different statuses by planning level.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Search | Choose Configure Your Solution. |  |  |
| 4 | Application and Subapplication area | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the following row:Item Name:Cash Operations | Configuration steps are displayed for the selected row. |  |
| 6 | Select Configuration Steps | Choose Configure to configure the following row:Step Name: Assign Planning Levels to Cash Trade Requests | The Change View “Assign Planning Levels to Cash Requests”: Overview displays. |  |
| 7 | Define Planning Levels for Cash Requests | Choose New Entries and make the following entries and choose Save:For example:Item 1:Original: <blank>Created: C1Submitted: C2Released: C3Item 2:Original: F0Created: C1Submitted: C2Released: C3 | The planning levels for cash request are defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Assign Planning Levels to Cash Trade Requests | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Planning Levels to Cash Trade Requests.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View “Assign Planning Levels to Cash Requests”: Overview screen displays. |  |
| 3 | Define Planning Levels for Cash Requests | Choose New Entries and make the following entries and choose Save:For example:Item 1:Original: <blank>Created: C1Submitted: C2Released: C3Item 2:Original: F0Created: C1Submitted: C2Released: C3 | The planning levels for cash request are defined. |  |

#### Automatically Reversing Rejected Payments

##### Define Rules for Reversing Rejected Payments

Purpose

In this step, you define rules that determine which reason should be automatically specified for reversing a rejected payment document and which payment block option should be automatically specified for blocking the reopened items.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Search | Choose Configure Your Solution. |  |  |
| 4 | Application and Subapplication area | Make the following entries:Application Area: FinanceSub Application Area: Bank Communication Management | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the following row:Item Name:Approve Bank Payments | Configuration steps are displayed for the selected row. |  |
| 6 | Select Configuration Steps | Choose Configure to configure the following row:Step Name: Define Rules for Reversing Rejected Payments | The Change View "Define Rules for Reversing Rejected Payments": Overview displays. |  |
| 7 | Specify Rule | Choose New Entries and make the following entries and choose Save:For example:Sequence Number: 1Paying Company Code: 3310Payment Method: <blank>House Bank: AEBK1Account ID: AEAC1Reversal Reason: 01Payment Block: A | The rule for Automatically Reversing Rejected Payments is defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Rules for Reversing Rejected Payments | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Rules for Reversing Rejected Payments.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View “Define Rules for Automatically Reversing Rejected Payments”: Overview screen displays. |  |
| 3 | Specify Rule | Choose New Entries and make the following entries and choose Save:For example:Sequence Number: 1Paying Company Code: 3310Payment Method: <blank>House Bank: AEBK1Account ID: AEAC1Reversal Reason: 01Payment Block: A | The rule for Automatically Reversing Rejected Payments is defined. |  |

##### Create Team for Reversing Rejected Payments

Purpose

In this activity, you create a team to specify responsibilities for reversing rejected payments.

Procedure

Execute the Create Team steps in the Responsibility Management ([1NJ](https://me.sap.com/processnavigator/SolP/1NJ)) test script with the following information:

Team Information tab

Name: Team for Reversing Payments

Description: Team for automatically reversing rejected payments

Global ID: PAYMENT_REVERSE

Status: Enabled

Type: SFSCM_BCMR (Category FSCM_BCM)

Responsibility Definition tab

Company Code: 3310

|  |
| --- |
| Note If fields are empty, the team is responsible for all company codes. |

Team Members tab

Business Partner: <user ID>, for example, AP_Accountant

Functions: SFSCM_BCMR

|  |
| --- |
| Note To display the connection between the business partner, AP accountant, and user ID, see the search help. Generic users are described in the Last Name field. |

#### Situation Handling

##### Situation Handling for Cash and Liquidity Management

###### Manage Teams and Responsibilities

Purpose

In this activity, you create a team to specify responsibilities for the review process.

Procedure

Execute the Create Team steps in the Responsibility Management ([1NJ](https://me.sap.com/processnavigator/SolP/1NJ)) test script with the following information:

Team Information tab:

Name: Team for Cash Management

Global ID: SFCLM1_A

Description: Situation team for cash and liquidity Management

Team Status: Enabled

Type: SFCLM1

Responsibility Definition tab:

Company Code: 3310

|  |
| --- |
| Note If fields are empty, the team is responsible for all company codes. |

Team Members tab:

Business Partner: <user ID>, for example, Cash Manager

Functions: SFCLM_TD (Check Transaction Data in One Exposure) & Functions: SFCLM_BAL (Check Bank Account Balance)

|  |
| --- |
| Note To display the connection between the business partner, cash manager, and user ID, see the search help. Generic users are described in the Last Name field. |

###### Create Situation Types: Date Difference Warning for FI Flows

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can use the situation template FIN_FQM_FIDATE_DIFFERENCE to create a situation type. The situation type is used to inform specific users when the system detects an FI cash flow for which the difference between the posting date and the value date does not meet the defined condition.

Prerequisite

If you want to trigger notification and check it. Please make sure you have posted a FI cash flow for which the difference between the posting date and the value date has exceeded the defined tolerance.

For example, in our testing case, tolerance is greater than or equal to 30 days under your company code.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Situation Types (F2947). |  |  |
| 3 | Copy Situation Types Template | Select the checkbox for standard template FIN_FQM_FIDATE_DIFFERENCE and choose Copy. | The Situation Type view is displayed.This standard template is used to inform specific users when the system detects an FI cash flow for which the difference between the posting date and the value date has exceeded the defined tolerance. |  |
| 4 | Define Condition | Make the following entries:Admin Information tab:ID: ZFIN_FQM_FIDATE_DIFFERENCEConditions tab:Company Code: 3310Date Difference (Days): greater than or equal to 30Fiscal Year: <current fiscal year> | The ZFIN_FQM_FIDATE_DIFFERENCE view displays. |  |
| 5 | Batch Job Scheduling | In Batch Job Scheduling Tab, make the following entries:Time Zone: for example UTCStart Batch Job At: for example <your time> |  |  |
| 6 | Add Team Category | In the Recipients area, choose Add Team Category. On the dialog box, select FCLM1 - Cash and Liquidity Management and choose Select. |  |  |
| 7 | Maintain Responsibility by Teams | For team category FCLM1 - Cash and Liquidity Management, make the following entries:Filter by Responsibility Definition: Company CodeFilter by Member Function: Check Transaction Data in One Exposure |  |  |
| 8 | Situation Monitoring | In the Situation Monitoring area, select checkbox for Monitor Instances. |  |  |
| 9 | Create | Choose Create. Choose Yes to confirm the message Enable Situation Type. | The situation type is created and enabled. |  |
| 10 | Trigger Now | Choose Trigger Now at the upper-right corner. | The notification is triggered immediately. Situation Instances is shown. |  |

###### Create Situation Types: Bank Account Balance Threshold Exceeded

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can use the situation template FIN_CLM_BKACCTBAL_THLDEXCEEDED to create a situation type. When the balance of a bank account falls short of or exceeds the defined threshold, bank account supervisors will get notified so that they can consider taking appropriate actions.

Prerequisite

If you want to trigger notification and check it, please make sure the relevant balance of bank account falls short of or exceeds the defined threshold.

|  |
| --- |
| NoteThe bank account balance can be imported from a bank statement. Follow the Upload Bank Statement procedure of the scope item Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/1EG)).Also the bank account balance can be manually entered via app Manage Bank Account Balances (F5175). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Situation Types (F2947). |  |  |
| 3 | Copy Situation Types Template | Select the checkbox for standard template FIN_CLM_BKACCTBAL_THLDEXCEEDED and choose Copy. | The Situation Type view is displayed. |  |
| 4 | Define Condition | Make the following entries:Admin Information tab:ID: ZFIN_CLM_BKACCTBAL_THLDEXCEEDEDName: for example, Bank Account Balance Threshold ExceededConditions tab:Balance Amount: for example, <0.00Balance Type: for example, Value Date BalanceNote Maintain other fields as needed. |  |  |
| 5 | Situation Monitoring | In the Situation Monitoring area, select checkbox for Monitor Instances. |  |  |
| 6 | Maintain Responsibility by Teams | For team category FCLM1 - Cash and Liquidity Management, make the following entries:Filter by Responsibility Definition: Company CodeFilter by Member Function: Check Bank Account Balance |  |  |
| 7 | Create | Choose Create. Choose Yes to confirm the message Enable Situation Type. | The situation type is created and enabled. |  |
| 8 | Delete Responsibility Rules (Optional) | If you do not want the default responsibility rule BKACCT_SUPVR, you can choose Delete(X).Note An internal bank account supervisor maintained in bank account master data also can be used as notification recipient via the default responsibility rule BKACCT_SUPVR. | The default responsibility rules are deleted. |  |

##### Situation Handling for Bank Communication Management

###### Define Function

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Search | Choose Configure Your Solution. |  |  |
| 4 | Application and Subapplication area | Application Area: Application Platform and InfrastructureSub Application Area: Responsibility Management |  |  |
| 5 | Select Configuration Item | Item Name:Functions |  |  |
| 6 | Select Configuration Steps | Choose Configure to configure the following row:Step Name: Define Functions | The "Define Functions": Change displays. |  |
| 7 | Create Function | Choose New Entries and make the following entries and choose Save:Function: for example, <BCM_FUNC>Function Description: for example, <Function for BCM batch> |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Functions | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Functions.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The "Define Functions": Change screen displays. |  |
| 3 | Create Function | Choose New Entries and make the following entries and choose Save:Function: for example, <BCM_FUNC>Function Description: for example, <Function for BCM batch> |  |  |

###### Define Function Profiles

Purpose

In this step, you can create function profiles and assign functions to a function profile. You can group similar functions for a business process in a function profile.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Search | Choose Configure Your Solution. |  |  |
| 4 | Application and Subapplication area | Make the following entries:Application Area: Application Platform and InfrastructureSub Application Area: Responsibility Management | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the following row:Item Name:Functions | Configuration steps are displayed for the selected row. |  |
| 6 | Select Configuration Steps | Choose Configure to configure the following row:Step Name: Define Function Profiles | The Change View “Function Profile”: Overview displays. |  |
| 7 | Create Function Profile | Choose New Entries and make the following entries and choose Save:For example:Profile: <BCM_PROF>Function Profile Description: for example, <Function Profile for BCM batch> | The function Profile is created for BCM Batch. |  |
| 8 | Assign Function to Function Profile | Choose Function Profile to Function Mapping in the left-side Dialog Structure. Enter following entries and Choose Save.Function: for example, <BCM_FUNC> | The function is assigned to the function profile. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Function Profiles | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Function Profiles.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View “Function Profile”: Overview screen displays. |  |
| 3 | Create Function Profile | Choose New Entries and make the following entries and choose Save:For example:Profile: for example, <BCM_PROF>Function Profile Description: for example, <Function Profile for BCM batch> | The function Profile is created for BCM Batch. |  |
| 4 | Assign Function to Function Profile | Choose Function Profile to Function Mapping in the left-side Dialog Structure. Enter following entries and Choose Save.Function: <BCM_FUNC> | The function is assigned to the function profile. |  |

###### Assign Function Profiles to Team Category

Purpose

In this step, you can assign a function profile to a standard team category.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution(F1241). |  |  |
| 3 | Search | Choose Configure Your Solution. |  |  |
| 4 | Application and Subapplication area | Make the following entries:Application Area: Application Platform and InfrastructureSub Application Area: Responsibility Management | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the following row:Item Name:Teams | Configuration steps are displayed for the selected row. |  |
| 6 | Select Configuration Steps | Choose Configure to configure the following row:Step Name: Assign Function Profiles to Team Category | The "Assign Function Profiles to Team Category": Change displays. |  |
| 7 | Map Function Profiles to Standard Team Category | Choose New Entries and make the following entries and choose Save:For example:Team Category: BCMProfile: for example, <BCM_PROF> | The function profile is mapped to standard Team Category. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Assign Function Profiles to Standard Team Category | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Function Profiles to Team Category.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The "Assign Function Profiles to Team Category": Change screen displays. |  |
| 3 | Map Function Profiles to Standard Team Category | Choose New Entries and make the following entries and choose Save:For example:Team Category: BCMProfile: for example, <BCM_PROF> | The function profile is mapped to standard Team Category. |  |

###### Define Team Types

Purpose

In this step, you can assign a function profile to a standard team category.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Search | Choose Configure Your Solution. |  |  |
| 4 | Application and Subapplication area | Make the following entries:Application Area: Application Platform and InfrastructureSub Application Area: Responsibility Management | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the following row:Item Name:Teams | Configuration steps are displayed for the selected row. |  |
| 6 | Select Configuration Steps | Choose Configure to configure the following row:Step Name: Define Team Types | The Change View “Team Type”: Overview displays. |  |
| 7 | Define Team Types | Choose New Entries and make the following entries and choose Save:For example:Team Type: for example, <BCM_TEAM>Team Category: BCMTeam Type Description: <Team Type for Bank Communication Management> | The team type is defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Team Types | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Team Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View “Team Type”: Overview screen displays. |  |
| 3 | Define Team Types | Choose New Entries and make the following entries and choose Save:For example:Team Type: for example, <BCM_TEAM>Team Category: BCMTeam Type Description: <Team Type for Bank Communication Management> | The team type is defined. |  |

###### Manage Teams and Responsibilities

Purpose

In this activity, you create a team to specify responsibilities for the review process.

Procedure

Execute the Manage Teams and Responsibilities steps in the Responsibility Management ([1NJ](https://me.sap.com/processnavigator/SolP/1NJ)) test script with the following information:

Team Information tab:

Name: Team for Bank Communication Management

Global ID: BCM_TEAM

Description: Situation team for Bank Communication Management

Team Status: Enabled

Type: SBCM

Responsibility Definition Tab:

Company Code: 3310

|  |
| --- |
| Note If fields are empty, the team is responsible for all company codes. |

Team Members tab:

Business Partner: <user ID>, for example, AP Accountant

Functions: S_BCMMON_F

|  |
| --- |
| Note To display the connection between the business partner, cash manager, and user ID, see the search help. Generic users are described in the Last Name field. |

###### Create Situation Types: Payment Batch Partially Rejected

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can use the situation template FIN_BCM_BATCH_PARTIALLY_REJECTED to create a situation type. The situation type is used for Situation Handling that informs specific members of your team about payment batches that were partially rejected.

|  |
| --- |
| Note This situation template is available for payment batches and navigates to the SAP Fiori app Monitor Payments. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Situation Types(F2947). | The Situation Type view displays. |  |
| 3 | Copy Situation Types template | Select the checkbox for standard template FIN_BCM_BATCH_PARTIALLY_REJECTED and choose Copy. | The situation type FIN_BCM_BATCH_PARTIALLY_REJECTED is used to inform specific users when the system detects the BCM batch is partially rejected by bank. |  |
| 4 | Define Condition | Make the following entries:Admin Information tab:ID: Z_FIN_BCM_BATCH_PART_REJECTEDName: Payment Batch Partially RejectedDisplay Sequence: MediumConditions tab:Paying Company Code: 3310You can maintain other filters per your requirement |  |  |
| 5 | Maintain Responsibility by Teams | For Team Category BCM Bank Communication Management, make the following entries:Filter by Responsibility Definition: Paying Company CodeFilter by Member Function: Bank Communication Monitoring （S_BCMMON_F) |  |  |
| 6 | Situation Monitoring | In Situation Monitoring, select the checkbox for Monitor Instances. |  |  |
| 7 | Create | Choose Create. Choose Yes to confirm the message Enable Situation Type. | The situation type is created and enabled. |  |

###### Create Situation Types: Payment Batch Was Rejected

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can use the situation template FIN_BCM_BATCH_REJECTED to create a situation type. The situation type is used for Situation Handling that informs specific members of your team about payment batches that were rejected.

|  |
| --- |
| Note This situation template is available for payment batches and navigates to the SAP Fiori app Monitor Payments. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Situation Types(F2947). |  |  |
| 3 | Copy Situation Types template | Select the checkbox for standard template FIN_BCM_BATCH_REJECTED and choose Copy. | The situation type FIN_BCM_BATCH_REJECTED is used to inform specific users when the system detects the BCM batch is fully rejected by bank. |  |
| 4 | Define Condition | Make the following entries:Admin Information tab:ID: Z_FIN_BCM_BATCH_REJECTEDName: Payment Batch Was RejectedDisplay Sequence: MediumConditions tab:Paying Company Code: 3310You can maintain other filters according to your requirement. |  |  |
| 5 | Maintain Responsibility by Teams | For team category BCM Bank Communication Management, make the following entries:Filter by Responsibility Definition: Paying Company CodeFilter by Member Function: Bank Communication Monitoring（S_BCMMON_F) |  |  |
| 7 | Situation Monitoring | In the Situation Monitoring tab, choose the Monitor Instances checkbox. |  |  |
| 8 | Create | Choose Create. Choose Yes to confirm the message in the Enable Situation Type dialog box. | The situation type is created and enabled. |  |

###### Create Situation Types: Payment Batch Status Check

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can use the situation template FIN_BCM_BATCH_STATUS_CHECK to create a situation type. The situation type is used for Situation Handling that informs specific members of your team about payment batches that are stuck in a defined status. The status check is triggered daily. It’s possible to define the statuses for which the notification is triggered and also for how many days the payment batch must be stuck in the defined status for a notification to be sent.

|  |
| --- |
| Note This situation template is available for payment batches and navigates to the SAP Fiori app Monitor Payments. |

Prerequisite

Please make sure the BCM batch is created with the relevant status, such as Payment Batch Created, Payment Medium Created… which is defined in your situation type.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Situation Types(F2947). |  |  |
| 3 | Copy Situation Types template | Select the checkbox for standard template FIN_BCM_BATCH_STATUS_CHECK and choose Copy. | The situation type is used to inform specific users when the system detects the specific BCM batch status which is defined in the situation type Z_FIN_BCM_BATCH_STATUS_CHECK. |  |
| 4 | Define Condition | Make the following entries:Admin Information tab:ID: Z_FIN_BCM_BATCH_STATUS_CHECKName: Payment Batch Status CheckDisplay Sequence: MediumConditions tab:Paying Company Code: 3310Status: for example, IBC01 (Payment batch created), IBC15 (Payment medium created)Batch Job Scheduling section:Time Zone: for example UTCStart Batch Job At: for example <your time> |  |  |
| 5 | Maintain Responsibility by Teams | For team category Bank Communication Management, make the following entries:Filter by Responsibility Definition: Paying Company CodeFilter by Member Function: Bank Communication Monitoring（S_BCMMON_F) |  |  |
| 7 | Situation Monitoring | In Situation Monitoring, select checkbox for Monitor Instances. |  |  |
| 8 | Create | Choose Create. Choose Yes to confirm the message Enable Situation Type. | The situation type is created and enabled. |  |
| 9 | Trigger Now | Choose Trigger Now at the upper-right corner.Note For batch/job situation, you can choose Trigger Now to trigger the notification immediately. | The notification is triggered immediately. Situation Instances is shown. |  |

#### Email Notification for Payment Approvers (Optional)

Purpose

When a payment batch requires approval, the payment batch approvers will be informed by email automatically.

Prerequisite

You need to configure valid email domains for email senders and receivers in the configuration for Output Management. Make the relevant settings in the following configuration steps:

- Define Allowed Email Sender Domains For Email Outbound
- Define Allowed Email Receiver Domains For Email Outbound

The Email is sent in the language which is defined as correspondence language in the user profile via app Manage Service Level Agreements (F6183A).

##### Enable Email Notifications

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
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Search | Choose Configure Your Solution. |  |  |
| 4 | Application and Subapplication Area | Application Area: FinanceSub Application Area: Bank Communication Management |  |  |
| 5 | Select Configuration Item | Item Name: Approve Bank Payments |  |  |
| 6 | Select Configuration Steps | Choose Configure to configure the following row:Step Name: Send Email to Payment Batch Approvers | The "Send Email to Payment Batch Approvers": Change displays. |  |
| 7 | Create Function | Choose New Entries and make the following entries and choose Save:Company code: 3310House Bank: AEBK1Email Template ID: for example, FSCM_BCM_PAYMENTBATCH_APPROVERSender Email Address: for example, donotreply@sap.comEnable Email : checkbox, XNote You need to at least enter an Email Template ID and Sender Email Address.You can differentiate the use of the email templates by company code and house bank if necessary.You need to change these default entries to match your preferences. | The email notification for payment batch approvers is enabled. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Configuration Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Send Email to Payment Batch Approvers.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The "Send Email to Payment Batch Approvers": Change screen displays. |  |
| 3 | Enable Email Notification | Choose New Entries and make the following entries and choose Save:Company code: 3310House Bank: AEBK1Email Template ID: for example, FSCM_BCM_PAYMENTBATCH_APPROVERSender Email Address: for example, donotreply@sap.comEnable Email : checkbox, XNote You need to at least enter an Email Template ID and Sender Email Address.You can differentiate the use of the email templates by company code and house bank if necessary.You need to change these default entries to match your preferences. | The email notification for payment batch approvers is enabled. |  |

##### Maintain Email Templates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can personalize the email body.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Extensibility Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Email Templates - Deprecated (F1306). |  |  |
| 3 | Select Tab | Select the Pre-delivered tab. |  |  |
| 4 | Search | Choose FSCM_BCM_PAYMENTBATCH_APPROVER. |  |  |
| 5 | Select Template | Choose FSCM_BCM_PAYMENTBATCH_APPROVER. | The "Email Template for Payment Batch Approver" detail page displays. |  |
| 6 | Select Language | Language: for example, <English> | The content "Email Template for Payment Batch Approver": in selected language displays. |  |
| 7 | Edit Email Template | Review email subject and body text.Note You can also use this app to create your own email templates. |  |  |

## Overview Table

This scope item consists of several procedures provided in the tables below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Outgoing Payment With BCM Approval

| Process Step, Report or Item | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Approval and Bank Integration |  |  |  |
| [BCM Batch Creation](#unique_58) [page ] 110 |  |  | This step is done automatically |
| [Monitor Payments](#unique_59) [page ] 110 | Accounts Payable Accountant | Monitor Payments (F2388) | Check status of payments. |
| [Check Cash Flow Items (Before Approval)](#unique_60) [page ] 112 | Cash Manager | Check Cash Flow Items (F0735) | Review detailed information of payment documents. |
| [Approval of Bank Transfer](#unique_61) [page ] 113 |  |  |  |
| [Approval by First Approver](#unique_62) [page ] 114 | Accounts Payable Manager | Approve Bank Payments (F0673A) | The batch status is In Approval. The next approvers is displayed. |
| [Reject by First Approver (Optional)](#unique_63) [page ] 115 | Accounts Payable Manager | Approve Bank Payments (F0673A) | A Bank Communication Management (BCM) batch is rejected during bank payment approval process by kind of reasons. |
| [Process Rejected Payments (Optional)](#unique_64) [page ] 117 | Accounts Payable Accountant | My Inbox - Process Rejected Payments (F4546) | The rejected payment is reversed. |
| [Approval by Second Approver](#unique_65) [page ] 118 | Cash Manager | Approve Bank Payments (F0673A) | The batch status is Payment Medium Created. The Reference Number is generated. |
| Bank Integration |  |  |  |
| [Option 1: Bank Integration with SAP Multi-Bank Connectivity (16R) (Outgoing Integration)](#unique_66) [page ] 119 | Role dependent upon procedure | Transaction/App dependent upon procedure | Results dependent upon procedure |
| [Option 2: Bank Integration with File Interface (1EG) (Outgoing Integration)](#unique_67) [page ] 120 | Role dependent upon procedure | Transaction/App dependent upon procedure | Results dependent upon procedure |
| [Display Status of Payment Documents](#unique_68) [page ] 120 | Accounts Payable Accountant | Display Status of Payment Documents (F7084) | Payment item status for batching process display. |
| Situation Handling for Payments Batch |  |  |  |
| Situation Handling: Payment Batch Partially Rejected |  |  |  |
| [Monitor Situations](#unique_69) [page ] 121 | Business Process Specialist | Monitor Situations (F3264) | You can monitor situations and check instance details. |
| [Check Notification](#unique_70) [page ] 122 | a recipient (for example, AP Accountant) |  | The detailed payment information is checked. |
| Situation Handling: Payment Batch Was Rejected |  |  |  |
| [Monitor Situations](#unique_71) [page ] 123 | Business Process Specialist | Monitor Situations (F3264) | You can monitor situations and check instance details. |
| [Check Notification](#unique_72) [page ] 124 | a recipient (for example, AP Accountant) |  | The notification is checked by the recipient who is assigned to team members in the preliminary step. |
| Situation Handling: Payment Batch Status Check |  |  |  |
| [Monitor Situations](#unique_73) [page ] 125 | Business Process Specialist | Monitor Situations (F3264) | You can monitor situations and check instance details. |
| [Check Notification](#unique_74) [page ] 126 | a recipient (for example, AP Accountant) |  | The notification is checked by the recipient who is assigned to team members in the preliminary step. |
| [Check Cash Flow Items (Check Status)](#unique_75) [page ] 127 | Cash Manager | Check Cash Flow Items (F0735) | Review detailed information of payment documents |

Bank Transfer Actions

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Initiate Bank Transfer |  |  |  |
| [Option 1: Create, Release and Clear Payment Request in One Single Action](#unique_76) [page ] 130 | Cash Management Specialist | Make Bank Transfers (F0691) | A payment request for bank transfer is created,released and paid in one step. |
| [Option 2: Create, Release, and Clear Payment Request in Separate Steps](#unique_77) [page ] 133 |  |  |  |
| [Create Bank Transfer](#unique_78) [page ] 133 | Cash Management Specialist | Make Bank Transfers (F0691) | A payment request via bank transfer is created. |
| [Release Payment Request](#unique_79) [page ] 135 | Cash Management Specialist | Make Bank Transfers (F0691) | The payment request is released. |
| [Pay Payment Request](#unique_80) [page ] 136 | Cash Management Specialist | Make Bank Transfers (F0691) | The payment request is paid. |
| Option 3: Make Bank Transfer with Templates |  |  |  |
| [Define Bank Transfer Templates](#unique_81) [page ] 138 | Cash Management Specialist | Define Bank Transfer Templates (F3759) | Bank transfer templates are created. |
| [Create Bank Transfers with Templates](#unique_82) [page ] 140 | Cash Management Specialist | Make Bank Transfers - Create with Templates (F3760) | A payment request for bank transfer is created with Templates. |
| [Release Payment Request](#unique_83) [page ] 141 | Cash Management Specialist | Make Bank Transfers (F0691) | The payment request is released. |
| [Pay Payment Request](#unique_84) [page ] 142 | Cash Management Specialist | Make Bank Transfers (F0691) | The payment request is paid. |
| [Approve and Bank Integration](#unique_85) [page ] 142 | Role dependent upon procedure | Transaction/App dependent upon procedure | Results dependent upon procedure |
| [Short Term Cash Positioning](#unique_86) [page ] 142 | Cash Manager | Short-Term Cash Positioning (F5380) | Check the cash position by country, currency, company code or bank. |

Cash Trade Request

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create and Submit Cash Trade Request for FX](#unique_87) [page ] 145 | Cash Management Specialist | Reconcile Cash Flows (F3418) | Cash trade request for FX is created and submitted |
| [Create and Submit Cash Trade Request for Money Market](#unique_88) [page ] 147 | Cash Management Specialist | Reconcile Cash Flows (F3418) | Cash trade request for MM is created and submitted |
| [Release Cash Trade Request](#unique_89) [page ] 148 | Cash Manager | Manage Memo Records (F2986) | Release Cash Trade Request |
| [Reject Cash Trade Request (Optional)](#unique_90) [page ] 149 | Cash Manager | Manage Memo Records (F2986) | Reject Cash Trade Request |
| [Treasury Management Integration for Trading Platform](#unique_91) [page ] 150 | Role dependent upon procedure | Follow the relevant procedure in the Treasury Trading via Trading Platforms test script. | Send cash trade request |
| [Fulfill Cash Trade Request as Deal Done](#unique_92) [page ] 151 | Cash Manager | Manage Memo Records (F2986) | Cash trade request fulfilled. |
| [Cancel Cash Trade Request as Deal Cancel](#unique_93) [page ] 152 | Cash Manager | Manage Memo Records (F2986) | Cash trade request canceled. |
| [Check Partial Fulfill or Partial Decline Cash Trade Request Status](#unique_94) [page ] 153 | Cash Manager | Manage Memo Records (F2986) | Cash trade requests are in process or completed. |

Manage Bank Account Balances

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Schedule Jobs for Bank Account Balance Initialization (Optional)](#unique_95) [page ] 154 | Cash Management Specialist | Schedule Jobs for Bank Account Balance Initialization (F7146) | Bank account balances are replicated from their latest end-of-day bank statements to cash management. |
| [Create Bank Account Balances](#unique_96) [page ] 157 | Cash Management Specialist | Manage Bank Account Balances (F5175) | Enter or upload the balances for bank accounts. You can also edit it. |
| [Import Bank Account Balances](#unique_97) [page ] 158 | Cash Management Specialist | Manage Bank Account Balances (F5175) | The Balance of relevant Bank Accounts is updated massively. |
| [Edit Bank Account Balances](#unique_98) [page ] 159 | Cash Management Specialist | Manage Bank Account Balances (F5175) | Bank Account Balances is edited. |
| [Check Bank Account Balances](#unique_99) [page ] 160 | Cash Management Specialist | Manage Bank Account Balances (F5175) | The difference between ledger balance and value date balance is showed. |

Cash Flows Reconciliation

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Schedule Automated Cash Flow Reconciliation](#unique_100) [page ] 163 | Cash Management Specialist | Schedule Jobs for Cash Flow Reconciliation (F5283) | The reconciliation of bank statement flows with forecasted cash flows is performed automatically. |
| [Review Reconciliation Results](#unique_101) [page ] 167 | Cash Management Specialist | Reconcile Cash Flows (F3418A) | Review reconciliation results. |
| [Undo Reconciliation](#unique_102) [page ] 168 | Cash Management Specialist | Reconcile Cash Flows (F3418A) | You can undo reconciliations for selected items and reset them to the open status. |
| [Reconcile Unmatched Transactions](#unique_103) [page ] 169 | Cash Management Specialist | Reconcile Cash Flows (F3418A) | You can manually reconcile intraday or end-of-day bank statement flows with forecasted cash flows. |
| [Analyze Cash Position](#unique_104) [page ] 171 | Role dependent upon procedure | Transaction/App dependent upon procedure | After cash flow reconciliation, you analyze the cash positions. |

Cash Snapshot Management

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Analyze Cash Position](#unique_105) [page ] 172 | Role dependent upon procedure | Transaction/App dependent upon procedure | Before capturing the cash snapshot, analyze the cash position. |
| [Schedule Cash Snapshots Capture](#unique_106) [page ] 172 | Cash Management Specialist | Schedule Jobs for Cash Snapshots (F8945) | Schedule jobs for capturing or deleting cash snapshots using the template and scheduling options provided. |
| [Capture Cash Snapshots](#unique_107) [page ] 174 | Cash Manager | Manage Cash Snapshots (F8962) | Manually capture cash snapshots. |
| Request Investment or Funding | Role dependent upon procedure | Transaction/App dependent upon procedure | Results dependent upon procedure |

Instant Balances (Optional)

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Monitor Instant Balances](#unique_108) [page ] 177 | Cash Management Specialist | Monitor Instant Balances (F7804) | Monitor and update instant balances for bank accounts that are enabled for instant balances. |
| [Manage Bank Message](#unique_109) [page ] 178 | Business Integration Specialist - Bank Integration | Manage Bank Messages (F4385) | Check bank messages for instant balance requests and response. |

Liquidity Item Transfer

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Manage Liquidity Item Transfer](#unique_110) [page ] 179 | Cash Manager | Manage Liquidity Item Transfer (F6385) | Process lifecycles of liquidity item transfer documents like Create, Change, Copy, and Delete. |

Situation Handling: Date Difference Warning for FI Flows

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Monitor Situations](#unique_111) [page ] 181 | Business Process Specialist | Monitor Situations (F3264) | You can monitor situations and check instance details. |
| [Check Notification](#unique_112) [page ] 182 | a recipient (for example, Cash Manager) |  | The notification is checked by the recipient who is assigned to team members in preliminary step. |

Cash Reports

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Schedule Jobs for Bank Statement Monitor](#unique_113) [page ] 185 | Accounts Receivable Accountant | Schedule Jobs for Bank Statement Monitor (F6866) | You can execute schedule jobs for bank statement monitor. |
| [Bank Statement Monitor](#unique_114) [page ] 187 | Cash Manager | Bank Statement Monitor (F6388) | Monitor the import status of end-of-day bank statements for all the bank accounts selected for monitoring. |
| [Intraday Bank Statement Monitor](#unique_115) [page ] 189 |  |  |  |
| [Define Monitoring Rules for Intraday Bank Statement Monitor](#unique_116) [page ] 189 | Cash Management Specialist | Define Monitoring Rules - Intraday Statements (FCLM_BRM_RULE) | The monitoring rules with frequency for the intraday bank statement is defined. |
| [Assign Monitoring Rule to Bank (Optional)](#unique_117) [page ] 190 | Cash Management Specialist | Manage Banks - Cash Management (F1574A) | Monitoring rule is assigned to bank. |
| [Define Bank Account to Monitor](#unique_118) [page ] 191 | Cash Management Specialist | Manage Bank Accounts (F1366A) | The bank account is set to be monitored by the Bank Statement Monitor - Intraday (F3671) App with monitoring rule |
| [Monitor Intraday Bank Statement](#unique_119) [page ] 193 | Cash Management Specialist | Bank Statement Monitor - Intraday (F3671) | Monitor the intraday bank statement. |
| [Monitor Bank Account Balances](#unique_120) [page ] 194 | Cash Manager | Monitor Bank Account Balances (F5176) | You can monitor whether bank account balances have been imported or entered in time for bank accounts. |
| [Short Term Cash Positioning](#unique_121) [page ] 195 | Cash Manager | Short-Term Cash Positioning (F5380) | The short-term cash position information per your predefined cash position profile can be checked. |
| [Cash Flow Analyzer](#unique_122) [page ] 198 | Cash Manager | Cash Flow Analyzer (F2332) | View the aggregated amounts and line item details of cash position, medium-and-long term liquidity forecast and actual cash flows. |
| [Actual Liquidity Analysis](#unique_123) [page ] 201 | Cash Manager | Actual Liquidity Analysis (F7923) | View the actual liquidity analysis of cash flows in bank accounts, identifying where cash comes from and how it is used. |
| [Document Chain Tracing for Cash Flow](#unique_124) [page ] 203 | Cash Management Specialist | Document Chain Tracing for Cash Flow (F7690) | Create traceability results for the specified accounting document which includes the flows and all intermediate flows in the document chain tracing when generating flows. |
| [Check Cash Position (Smart Business)](#unique_125) [page ] 204 | Cash Manager | Cash Position - Today (F1737) | Check the forecast cash positions for the current date by location, company, and currency. |
| [Check Liquidity Items on G/L Accounts](#unique_126) [page ] 205 | Cash Manager | Check Liquidity Items on G/L Accounts (F6459) | You can check liquidity items on G/L Accounts. |
| [Check Cash Flow Items](#unique_127) [page ] 206 | Cash Manager | Check Cash Flow Items (F0735) | Track and trace all the cash flow items from different source applications. Also check line items detailed of the original documents. |
| [Cash Flow Comparison – By Date Range](#unique_128) [page ] 207 | Cash Manager | Cash Flow Comparison (F3274) | Compare actual cash flows with your forecasts. |
| [Cash Flow Comparison – By Timestamp](#unique_129) [page ] 208 | Cash Manager | Cash Flow Comparison - By Timestamp (W0137) | Compare actual cash flows with your forecasts. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Outgoing Payment with BCM Approval Process

#### Approval and Bank Integration

Prerequisite

Before testing the steps under Approval and Bank Integration, ensure that at least one of the following procedures has been completed:

1. Maintain Payment Approver for Bank Accounts before Batch creation (refer to [Maintain Payment Approver for Bank Accounts](#unique_26) [page ] 45)
2. Batch is created successfully. Batch can be automatically generated via one of the following procedures:
    - Bank transfer (refer to the Bank Transfer Actions section).
    - Payment run using the Manage Automatic Payments (F0770), as described in Accounts Payable [J60](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J60) test script.
    - Free form payment is described in Accounts Payable (J60) test script.
    - Others.

|  |
| --- |
| Note If a payment falls under the payment business rules maintained in Basic Payment Management ([7MJ](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/7MJ)) test script, it is to be processed through the Functional Approval workflow, as described in Basic Payment Management ([7MJ](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/7MJ)) test script, skipping the [Approval of Bank Transfer](#unique_61) [page ] 113 process in this document. The BCM batchs can only be created after the Functional Approval process is completed. |

Purpose

This section provides procedures for how the outgoing payment of a bank transfer is approved, whether it comes from a payment run for vendor or an initiated bank transfer.

After payment approval, the payment medium file is created. If PMW Format’s Alternative Format Type is marked with 90 SAP Multi-Bank Connectivity, the payment medium files are automatically sent the house bank via SAP Multi-Bank Connectivity for further processing (as described in the Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/16R)) test script.)

Outgoing payments always updates the cash position, so the cash manager can review detailed cash position information, analyze the payment details or even verify the FI document.

After Approval and Bank Integration is processed, in the Cash Operations -Common Steps section (as described in the Basic Cash Operations ([BFB](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/BFB)) test script), the Bank Statement, Memo Record, and Cash Reports procedures can be tested.

|  |
| --- |
| Note You must create the BCM batch with the payment method using the Payment Medium Workbench (PMW) format, then approvals are possible for the BCM batch.When the payment methods for file downloading use the Classic Payment Medium Program in SAP S/4HANA Enterprise Management, use the Schedule Automatic Payments Periodically SAP Fiori app for payment runs. However no BCM batch can be created or approved for the Classic Payment Medium Program. |

|  |
| --- |
| Note Grouping of different bank accounts into one payment file is not possible. [KBA 3257630](https://launchpad.support.sap.com/#/notes/3257630) - Group different bank accounts into one payment file not possible created. |

##### BCM Batch Creation

Context

The creation of the cross-payment run in bank communication management (BCM Batch) is done automatically after the payment is initiated.

|  |
| --- |
| Note If the batch is not created successfully. You can use the App: Manage Automatic Payments (F0770) or Automatic Payment Transactions for Payment Requests (F111) to check application log for your payment run ID. |

|  |
| --- |
| Note If the approval list in the bank master data is empty, all payment will be rejected or approved depending on the value customized in preliminary step Define Automatic Approval/Rejection for Bank Account Master data. |

|  |
| --- |
| Note Please make sure the Basic Settings is set as Full Scope, you can check it via configuration activity 101025. If not, the batch can not be created. |

Procedure

This step is done automatically.

##### Monitor Payments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the Monitor Payments (F2388) app, you can display an overview of your payment batches. You can view the statuses of batches and individual payments at different processing stages.

In different stages of a BCM batch's lifecycle, the app displays different batch/batch item status.

- Payment Batch Created: Batch is created and waits for first approval.
- In Approval: Batch is approved at least once, though not final approval.
- Payment Medium Created: Batch successfully completes approval process and the payment medium is created.
- Accepted by Bank: The payment medium has been sent to the bank and the bank sends responds with a payment status message accepting the payment instruction. This can also be fulfilled through Multi-Bank Connectivity (MBC).
- Stmt. Received: Batch is reconciled by a bank statement.

|  |
| --- |
| Note The Monitor Payments app incorporates SWIFT gpi reason codes to indicate the status of payments. External entities, such as banks, use reason codes to communicate the status of SWIFT gpi payments. Your entity receives these external Status Reason Codes and translates them into internal reason codes. One internal reason code may be mapped to many external reason codes. You, as the key user for configuration, can create reason codes and map them to external reason codes. |

|  |
| --- |
| Note (Optional) You may use the configuration activities Fix Errors for Payment Batches to configure remediations in Preliminary Steps. You also have taken the required actions to enable fixing functionalities, for example, manually resetting and reversing several payment documents to enable the 'Mass Reset and Reverse' functionality or rejecting or reversing all payment documents to enable setting the status 'Automatically Rejected' (IBC20). Then you can find remediations on the Remediations tab on the batch details screen of the Monitor Payments (F2388) app. They are fixing functions you can use to correct common problems with payment batches. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Monitor Payments (F2388). |  |  |
| 3 | Find the Newly Created Batch | Maintain your filter and choose Go. Choose the New tab. | All newly created batches are displayed on the New tab. You can find the batch you created earlier in the process. |  |
| 4 | Verify the Batch Status | Verify the batch status in the Bank Status Text column. The status should be Payment Batch Created. | Note If the approval list in bank master data is empty, all payment will be rejected or approved depending on the value customized in the Define Automatic Approval/Rejection for Bank Account Master Data preliminary step in the Advanced Cash Operations (J78) test script. |  |
| 5 | Check Details | Select your cash flow item, and choose > (Details). | Detailed information for this batch is displayed. |  |
| 6 | Check Approver | In the header section, choose Approvers to check who are the first approvers for the batch. Close the dialog box when you're done. | All approvers used in the first approver step are shown (for example: Accounts Payable Manager). |  |

##### Check Cash Flow Items (Before Approval)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, the Cash Manager or Bank Accountant reviews the detailed information of payment documents before approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori app | Open Check Cash Flow Items (F0735). | The Check Cash Flow Item view displays. |  |
| 3 | Enter Selection Criteria | Choose Adapt Filters if selection fields are hidden.Make the following entries and choose Go.Exchange Rate Type: <M>Snapshot Time: <default value>Value Date: <Today>Company Code: 3310Certainty Level: <choose all certainty levels>Account Number: 0000000693123456Cash Flow View for Accounting: 2(Cash Position) or 3(Liquidity Analysis) | The list is filtered to show fewer entries. |  |
| 4 | Display Additional Payment Information | Select your cash flow item, and choose > (Details) to check details information. | More payment information is displayed.Note Different source applications display different payment information. |  |

##### Approval of Bank Transfer

Context

In the SAP S/4HANA system, a Bank Communication Management (BCM) batch should be approved by approvers according to the approval pattern in preconfiguration.

After the approval process is done, the payment medium is created automatically.

No matter the source of a BCM batch, payment run of vendors/customers,or payment run of bank transfer, the BCM batch should go through the approval process.

|  |
| --- |
| NoteThe 5 payment method IDs (E, Q, R, &, @) are marked as automatic payment (No Approval). No approval process is required.The approver for a payment cannot be its creator. Payments created by the approver do not appear in the app Approve Bank Payments (F0673A)If the payment or batch amount is greater than the Maximum amount maintained in the Bank Account Master, no payment approver can be found for the batch. The payments also do not appear in the app Approve Bank Payments (F0673A) |

|  |
| --- |
| Note You have the option to enable two-factor authentication using SAP Cloud Platform Identity Authentication (IAS) for the Approve Bank Payments app. See preliminary step Specify Optional User Authentication. If you enable two-factor authentication, the business user submitting payment batches for processing by the bank will be asked to authenticate their identity before the batches can be submitted. |

Prerequisites

Payment approver is maintained for bank accounts. BCM batches are created successfully.

###### Approval by First Approver

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Manager.Note The user assigned to Signatory Group G001 in the Prerequisites section, Maintain Payment Approver for Bank Accounts. |  |  |
| 2 | Access the SAP Fiori app | Open Approve Bank Payments (F0673A). |  |  |
| 3 | Maintain Filters | Make the following entries and choose Go.Paying Company Code: 3310 |  |  |
| 4 | Review Payment Batch and Items | Choose the For Review tab, review to ensure that the batches are correct. | All items are correct and the batches can be approved. |  |
| 5 | Select Batch to be Approved | Select the payment batch for approval.If more than one batch must be approved, select the checkbox for the batches to approve. |  |  |
| 6 | Approve | Choose Approve. Enter the note and choose OK to confirm the dialog box. | The payment is approved and appears on the Reviewed tab. |  |
| 7 | (Optional) Undo Approval | Choose the Reviewed tab and select the payments to be discarded.Choose Discard Changes from the top right of the view.To confirm the dialog box, choose Discard Changes.Note This optional step is only necessary when you want to undo the approval. | The payment is discarded. it displays on the For Review tab. |  |
| 8 | Submit Reviewed Batch | Choose the Reviewed tab and select the payments to be submitted. Choose the Approve and Submit button. To confirm the dialog box, choose Submit. | The batch is submitted. |  |
| 9 (Optional) | Submit Verification Token (Optional) | On the dialog box Confirm Submission of Reviewed Batches, make the following entry and choose Submit.VerificationToken: < Insert the Passcode from App SAP Authenticator on your mobile phone and insert it here>Note This step is only required when you enable two-factor authentication using SAP Cloud Identity Services - Identity Authentication (IAS) for the Approve Bank Payments (F0673A) app. | The payment is sent to the Second Approver and no longer appears on the Reviewed tab. |  |
| 10 | Check Batch Status and Next Approver | Check the batch status and next approvers via App Monitor Payments (F2388), see step Monitor Payments. | The batch status is In Approval. The next approvers are displayed. For example: Cash Manager. |  |

###### Reject by First Approver (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A Bank Communication Management (BCM) batch is rejected during bank payment approval process by kind of reasons.

|  |
| --- |
| Note If the Bank Communication Management (BCM) batch is rejected in this step, you can skip the next following step Approval by Second Approver. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Manager.Note The user assigned to Signatory Group G001 in the Prerequisites section, [Maintain Payment Approver for Bank Accounts](#unique_26) [page ] 45. |  |  |
| 2 | Access the SAP Fiori app | Open Approve Bank Payments (F0673A). |  |  |
| 3 | Maintain Filters | Make the following entries and choose Go.Paying Company Code: 3310 |  |  |
| 4 | Select Batch to be Rejected | Choose the For Review tab, select the payment batch for rejection.If more than one batch must be rejected, select the checkbox for the batches to reject. |  |  |
| 5 | Reject | Choose Reject. In the Confirm Reject dialog box, enter some reason in Note, and choose OK. | The payment is rejected and appears on the Reviewed tab. |  |
| 6 | Submit Reviewed Batch | Choose the Reviewed tab, choose the batch to reject, then choose Submit. To confirm the Submission of Reviewed Batches dialog box, choose Submit. | The batch is submitted. |  |
| 7 | Check Batch Status | Check the batch status and next approvers via App Monitor Payments (F2388), see step Monitor Payments. | The batch status is change to Automatic Rejection. The payment status is also change to Rejected by Approver.Note If the reversal reasons and payment block for the rejected payments is defined in configuration activity mentioned in the Preliminary Step Define Rules for Reversing Rejected Payments. the AP Accountant receives the rejected payment documents workflow in his My inbox app. You go on the next step Process Rejected Payments (Option).If not, skip next step and reverse it manually in the Reset Cleared Items app. |  |

###### Process Rejected Payments (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can reverse payment documents rejected in the approval process or by the bank. Possible actions for a rejected payment document include reversing it or keeping it rejected.

|  |
| --- |
| Note You can use this app My Inbox - Process Rejected Payments (F4546) for processing only rejected payment documents created for supplier and customer open items via an automatic payment program, such as the Manage Automatic Payments (F0770) app and the Create Single Payment (F0743) app. You cannot use this app for processing rejected payments documents created for payment requests. |

Prerequisite

The reversal reasons and payment block for the rejected payments is defined in the configuration activity mentioned in the Preliminary Step [Define Rules for Reversing Rejected Payments](#unique_41) [page ] 79.

A Bank Communication Management (BCM) batch is rejected during the bank payment approval process by kind of reasons in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant.Note The user assigned to the team for Reversing Rejected Payments which is defined in the Preliminary step. |  |  |
| 2 | Access the SAP Fiori app | Open My Inbox - Process Rejected Payments (F4546). |  |  |
| 3 | Process Rejected Payments | Double click your rejected payment batch in left side panel and choose Reverse. To confirm the dialog box, enter a note and choose Submit.NoteThis payment was rejected in the bank payment approval process. You can choose Reverse or Keep Rejected.If you keep the payment rejected, the payment will not be sent to the bank. If you later want to reverse the payment, you need to manually reverse it in the Reset Cleared Items app.The payment will be reversed using the automatically specified reason for the reversal. The cleared items in the payment will be reopened. If the automatically specified payment block option confirms a block, the reopened items will be blocked and cannot be paid in other payment runs.Whichever action you choose, the payment will then disappear from the list of rejected payments on the left. | Task successfully processed. The rejected payment is reversed. |  |

###### Approval by Second Approver

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager.Note The user assigned to Signatory Group G002 in the Prerequisites section, Maintain Payment Approver for Bank Accounts. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Approve Bank Payments (F0673A). | The Approve Bank Payments app displays. |  |
| 3 | Maintain Filters | Make the following entries and choose Go.Paying Company Code: 3310 |  |  |
| 4 | Review Payment Batch and Items | Choose the For Review tab to ensure if the batches are correct. | All items are correct and the batches can be approved. |  |
| 5 | Select Batch to be Approved | Select the payment batch for approval.If more than one batch must be approved, select the checkbox for the batches to approve. |  |  |
| 6 | Approve | Choose Approve.Choose OK to confirm the dialog box. | The global payment is approved and appears on the Reviewed tab. |  |
| 7 | Submit Reviewed Batch | Choose the Reviewed tab and select the payments to be submitted, choose Submit.On the dialog box, choose Submit. | The payment is submitted. |  |
| (Optional) | Submit Verification Token (Optional) | On the Confirm Submission of Reviewed Batches dialog box, make the following entries and choose Submit:VerificationToken: < Insert the Passcode from App SAP Authenticator on your mobile phone and insert it here>, make the following entry and chooseNote This step is only required when you enable two-factor authentication using SAP Cloud Platform Identity Authentication (IAS) for the Approve Bank Payments app. | The payment is finally approved and no longer appears on the Reviewed tab. |  |
| 8 | Check Batch Status | Check the batch status and next approvers via App Monitor Payments (F2388), see step Monitor Payments. | The batch status is Payment Medium Created. The Reference Number is generated. |  |

##### Bank Integration

###### Option 1: Bank Integration with SAP Multi-Bank Connectivity (16R) (Outgoing Integration)

Purpose

The BCM batch is approved, the payment medium file is created . With SAP Multi-Bank Connectivity (MBC), SAP establishes connections with your banks to automatically send payment instructions, receive status notifications, receive bank statements, and receive lockbox messages.

|  |
| --- |
| Note Only the house bank with Alternative Format Type 90 (SAP Multi-Bank Connectivity) can be used in Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/16R)) test script. You can check this customizing via configuration activity: 101972 (Set Up Payment Methods for Each Country/Region for Payment Transactions). |

|  |
| --- |
| Note Because the simulated bank statement file must be stored in the SFTP folder, contact your system administrator or the testing organizer for information to access the SFTP folder, as different testing systems/clients may have different SFTP folders. |

Procedure

Follow the steps in the Outgoing Integration test procedure of the Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/16R)) test script.

###### Option 2: Bank Integration with File Interface (1EG) (Outgoing Integration)

Purpose

The BCM batch is approved, the payment medium file is created. You download the payment files for outgoing payments, which are generated by SAP S/4HANA Cloud Public Edition to your computer. You can then upload these payment files to your banking portal or treasury workstation for payment processing.

Procedure

Follow the steps in the Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/1EG)) test script.

##### Display Status of Payment Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can display an overview of your payment documents and their statuses. You can view the statuses of individual payments and their payment batches.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Status of Payment Documents (F7084). |  |  |
| 3 | Maintain Filters | Make the one or all following entries and choose Go.Run Date: <run date for payment run>Payment Run ID: <ID for payment run>Paying Company Code: 3310 | Payment item status for batching process display.Payment Item not in batchPayment Item reversedPayment Item not in fileOther Exception Status |  |

##### Situation Handling for Payment Batch

###### Situation Handling: Payment Batch Partially Rejected

###### Monitor Situations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can monitor situations and check instance details.

Prerequisite

You have performed the procedure Situation Handling for Bank Communication Management in Preliminary Step.

In order to trigger notification and check it, please make sure you have created the relevant transaction data.

For Situation Template FIN_BCM_BATCH_PARTIALLY_REJECTED, please make sure the BCM batch is partially rejected by bank.

For example, the payment is partially rejected via pain.002 file. You can refer to the step Pull Status Message from MBC of Test Script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/16R)) .

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Monitor Situations (F3264). |  |  |
| 3 | Check Situation type for Payment Batch Partially Rejected | Make the following entries:Situation Type ID: Z_FIN_BCM_BATCH_PART_REJECTEDYear: <current year> |  |  |
| 4 | Check Instance Details | In the Instance Details section, check detailed information for your situation type. |  |  |

###### Check Notification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the notification is checked by the recipient who is assigned to team members in preliminary step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a recipient (for example, AP Accountant). |  |  |
| 2 | Check Notification for Situation Template FIN_BCM_BATCH_PARTIALLY_REJECTED | On home page, choose Notifications on the upper right corner.Choose By Type, under type Situation Payment Batch Partially Rejected has be…, choose Expand Group. |  |  |
| 3 | Check Details | Choose one item with Payment batch was partially rejected and navigate to App Monitor Payments (F2388). | The detailed payment information is checked. |  |

###### Situation Handling: Payment Batch Was Rejected

###### Monitor Situations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can monitor situations and check instance details.

Prerequisite

You have performed the procedure Situation Handling for Bank Communication Management in the Preliminary Step.

In order to trigger notification and check it, please make sure you have created the relevant transaction data.

For Situation Template FIN_BCM_BATCH_REJECTED, please make sure the BCM batch is fully rejected by the bank.

For example, the payment is fully rejected via pain.002 file. You can refer to the step Pull Status Message from MBC of Test Script Bank Integration with SAP Multi-Bank Connectivity (16R).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Monitor Situations (F3264). |  |  |
| 3 | Check Situation type for Payment Batch Fully Rejected | Make the following entries:Situation Type ID: Z_FIN_BCM_BATCH_REJECTEDYear: <current year> |  |  |
| 4 | Check Instance Details | In Instance Details section, check detailed information for your situation type. |  |  |

###### Check Notification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the notification is checked by the recipient who is assigned to team members in the preliminary step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a recipient (for example, AP Accountant). |  |  |
| 2 | Check Notification for Situation Template FIN_BCM_BATCH_REJECTED | On home page, choose Notifications on the upper right corner.Choose By Type, under type Situation Payment Batch Was Rejected has be…, choose Expand Group. |  |  |
| 3 | Check Details | Choose one item with Payment batch was rejected and navigate to App Monitor Payments (F2388). | The detailed payment information is checked. |  |

###### Situation Handling: Payment Batch Status Check

###### Monitor Situations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can monitor situations and check instance details.

Prerequisite

You have performed the procedure Situation Handling for Bank Communication Management in the Preliminary Step.

In order to trigger notification and check it, please make sure you have created the relevant transaction data.

For Situation Template FIN_BCM__BATCH_STATUS_CHECK, please make sure the BCM batch is created with the relevant status, such as ‘Payment Batch Created, Payment Medium Created…’ which is defined in your situation type.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Monitor Situations (F3264). |  |  |
| 3 | Check Situation type for Payment Batch Status Check | Make the following entries:Situation Type ID: Z_FIN_BCM_BATCH_STATUS_CHECKYear: <current year> |  |  |
| 4 | Check Instance Details | In Instance Details section, check detailed information for your situation type. |  |  |

###### Check Notification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the notification is checked by the recipient who is assigned to team members in the preliminary step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a recipient (for example, AP Accountant). |  |  |
| 2 | Check Notification for Situation Template FIN_BCM_BATCH_STATUS_CHECK | On home page, choose Notifications on the upper right corner.Choose By Type, under type Situation Payment Batch Status Check has be…, choose Expand Group. |  |  |
| 3 | Check Details | Choose one item with Payment batch is stuck and navigate to App Monitor Payments (F2388). | The detailed payment information is checked. |  |

##### Check Cash Flow Items (Check Status)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Within the Check Cash Flow Items app, the cash manager, bank accountant or AR/AP accountants can check the status of each single outgoing payment that is merged in a BCM batch.

In different stages of a BCM batch's lifecycle, different batch/batch item status is displayed in the Check Cash Flow Items app.

- Payment Batch Created: Batch is created and waits for first approval.
- In Approval: Batch is approved at least once, though not in final approval.
- Payment Medium Created: Batch successfully completes the approval process and the payment medium is created.
- Accepted by Bank: The payment medium has been sent to the bank and the bank responds with a payment status message accepting the payment instruction. This can also be fulfilled through Multi-Bank Connectivity (MBC).
- Stmt. Received: Batch is confirmed by a bank statement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Check Cash Flow Items (F0735). | The Check Cash Flow Item screen displays. |  |
| 3 | Search Criteria | Choose Adapt Filters if selection fields are hidden.Make the following entries and choose Go.Snapshot Time: <default value>Exchange Rate Type: <M>Value Date: <Today>Company Code: 3310Note Other fields keep default value, change it as needed. | The list is filtered to show fewer entries. |  |
| 4 | Check Batch and Batch Item Status | Choose either the Batch Item Status Code or the Batch Status Code columns (scroll right to last columns) and check their status.If you cannot find the Batch Item Status Code and the Batch Status Code column, please change the layout. | For the payment document with MBC payment medium format, after the steps in chapter Outgoing Integration of test script 16R - Bank Integration with SAP Multi-Bank Connectivity are executed successfully, its status should be Accepted by Bank.For the Payment document with a payment medium format for file download, after the steps in the chapter Outgoing Integration of test script 1EG - Bank Integration with File Interface are executed successfully, its status should be Payment Medium Created. |  |
| 5 | Take Action | The cash manager should take action for those batches or batch items with inappropriate status (such as a batch created 10 days ago that has not been approved or rejected). |  |  |

### Bank Transfer Actions

Purpose

This section describes the steps to make a bank transfer between two house bank accounts. For example, there is a deficit of a current bank account; the cash manager makes a decision to make a bank transfer from another bank account.

Example Data:

There are two sample bank accounts provided:

| Item | Bank Account | Bank Key | House Bank / Account ID |
| --- | --- | --- | --- |
| Account 1 | 0000000693123456 | 18121976 | AEBK1/AEAC1 |
| Account 2 | 0000000693123456 | 18121986 | AEBK2/AEAC2 |

You may make a bank transfer from bank account 0000000693123456 to bank account 0000000693123456, or from bank account 0000000693123456 to bank account 0000000693123456.

|  |
| --- |
| NoteCross-company code bank transfer is not supported in preconfigured content. You need to define a clearing account between company codes via configuration activity: 100297.Also cross countries with different withholding tax is not supported. |

Prerequisite

Make sure the relevant clearing accounts are maintained for your bank account. You can define the relevant clearing accounts via configuration activities: 102803, 102802.

#### Initiate Bank Transfer

Context

You can make transfers between bank accounts in your company. For each transfer, the system creates a payment request. Depending on your company's process, you can either create and clear the payment request in one single action, or create, release, and clear the payment request in separate steps.

You can also navigate from the Make Bank Transfers (F0691) app to the Make Bank Transfers - Create with Templates (F3760) app, to use repetitive codes to speed up internal work, create payment requests in batches, and proceed with payment program for payment requests.

You have three options for bank transfer:

1. Create, release, and clear the payment request in one single action by selecting the Release and Pay checkbox. See [Option 1: Create, Release and Clear Payment Request in One Single Action](#unique_76) [page ] 130 task.
2. Create, release, and clear the payment request in separate steps by deselecting the Release and Pay checkbox. See [Option 2: Create, Release, and Clear Payment Request in Separate Steps](#unique_77) [page ] 133 task.
3. Create a bank transfer with a template. For more information see the [Option 3: Make Bank Transfer with Templates](#unique_134) [page ] 137 task.

##### Option 1: Create, Release and Clear Payment Request in One Single Action

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create, release and clear the payment request in one single action.

Prerequisite

The sample bank accounts exist, with payment signatories assigned to them. For more information, see the [Maintain Payment Approver for Bank Accounts](#unique_26) [page ] 45 section.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Make Bank Transfers (F0691). |  |  |
| 3 | Create, Release and Pay Bank Transfer in one step (Option 1) | To trigger a new bank transfer, choose Create. Make the following entries and choose Create:Note Make a note of the payment request number: __________ (when you have done so, choose Close).Payer Information:Paying Bank Account: 0000000693123456Paying Company Code: 3310Paying House Bank: for example, AEBK1Paying House Bank Account: for example, AEAC1Payee Information:Receiving Bank Account: for example, 0000000693123456Receiving Company Code: 3310Receiving House Bank: for example, AEBK2Receiving House Bank Account: for example, AEAC2Note The descriptions for the two bank account fields are populated in display mode after determination.Transaction Information:Transfer Date: <current date>Payment Method: Choose an existing payment method for credit transfer.Note Only payment methods that are applicable to the paying bank account are listed.Amount: for example, 1000AEDRelease and Pay: SelectedNote Select Release and Pay checkbox, the system automatically releases the payment re-quest and starts the payment run.Payment Data: (option)Single Payment: <select per your request>Note If you want to designate instruction key for the payment re quests, enter following instruction key & instruction fields.Instruction Key: <via Value Help>Instruction 1: <via Value Help>Instruction 2: <via Value Help>Instruction 3: <via Value Help>Instruction 4: <via Value Help>Note The key is used as part of an argument when reading the information stored for an instruction key (incl. instructions, cost allocation key and payment method for DME, for example). Maintenance is done in configuration activity/customizing.Note Instructions can be defined 1) in document; 2) in master data record using an instruction key; 3) in the house bank DME data using an instruction key; The instructions from the document are used with higher priority, provided that one of the four fields has been filled out. | The Make Bank Transfer screen displays, and the relevant payment request is created.If the system does not find any configuration or input errors and the payment run is successfully triggered for the payment request, the new bank transfer payment request is successfully created and cleared.Otherwise, the payment request stays in Released status. |  |
| 4 | Search Bank Transfer | Make the following entries and choose Go:Payment Request: <payment request number>Note Choose Adapt Filters to show the Payment Request field. | The specified bank transfer entry with Cleared status is displayed in the Bank Transfer worklist. |  |
| 5 | Open Bank Transfer | Choose the bank transfer entry. | The bank transfer payment request is presented in the right side of the screen with Cleared status. The Clearing Document No. field displays the clearing document number automatically. |  |
| 6 | Check Application Log | In Application Log section, choose Search. | The payment request info is presented in log details.NoteIf the payment request is not cleared and stays in Released status or the batch is not created, you can read the message and also use the App: Automatic Payment Transactions for Payment Requests (F111) to check application log for your payment run ID.You can check your payment status via App: Monitor Payments (F2388). |  |

##### Option 2: Create, Release, and Clear Payment Request in Separate Steps

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create, release and clear the payment request in separate steps.

Prerequisite

The sample bank accounts exist, with payment signatories assigned to them. For more information, see the [Maintain Payment Approver for Bank Accounts](#unique_26) [page ] 45 section.

###### Create Bank Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a payment request via bank transfer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Make Bank Transfers (F0691). |  |  |
| 3 | Create New Bank Transfer | To trigger a new bank transfer, choose Create. Make the following entries and choose Create:Note Make a note of the payment request number: __________ (when you have done so, choose Close).Payer Information:Paying Bank Account: 0000000693123456Paying Company Code: 3310Paying House Bank: for example, AEBK1Paying House Bank Account: for example, AEAC1Payee Information:Receiving Bank Account: for example, 0000000693123456Receiving Company Code: 3310Receiving House Bank: for example, AEBK2Receiving House Bank Account: for example, AEAC2Transaction Information:Transfer Date: <current date>Payment Method: Choose an existing payment method for credit transfer.Amount: for example, 1000AEDRelease and Pay: DeselectedPayment Data: (option)Single Payment: <select per your request>Note If you want to designate instruction key for the payment request, enter following instruction key & instruction fields.Instruction Key: <via Value Help>Instruction 1: <via Value Help>Instruction 2: <via Value Help>Instruction 3: <via Value Help>Instruction 4: <via Value Help> | If the system does not encounter validation errors, the new bank transfer payment request is successfully created. The system displays a message indicating that a payment request is created with the payment request ID. |  |
| 4 | Check Application Log | In Application Log section, choose Search. | The payment request creation info is presented in log details. |  |

###### Release Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you release a payment request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Make Bank Transfers (F0691). |  |  |
| 3 | Search Bank Transfer | Make the following entries and choose Go:Payment Request: <payment request number>Note Choose Adapt Filters to show the Payment Request field. | The specified bank transfer entry with Created status is displayed in the Bank Transfer worklist. |  |
| 4 | Release Bank Transfer | At the right of the screen, choose Release.To confirm, on the dialog box, choose OK. | The bank transfer payment request is presented in the right side of the screen with 'Released' status. The Pay and Reverse buttons are shown for you to proceed with the next payment transactions. |  |
| 5 | Check Application Log | In Application Log section, choose Search. | The payment request release info is presented in log details. |  |
| 6 | Reverse Bank Transfer after being released(option) | At the right of the screen, choose Reverse.To confirm, on the dialog box, choose Reverse. | The bank transfer payment request status change to Reversed.If you reverse the payment request, go back to the prior step to create a bank transfer. |  |

###### Pay Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you pay a payment request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Make Bank Transfers (F0691). |  |  |
| 3 | Search Bank Transfer | Make the following entries and choose Go:Payment Request: <payment request number>Note Choose Adapt Filters to show the Payment Request field. | The specified bank transfer entry with Released status is displayed in the Bank Transfer worklist. |  |
| 4 | Pay Bank Transfer | At the right of the screen, choose Pay.To confirm, on the dialog box, choose OK. | The payment request is cleared. |  |
| 5 | Check Application Log | In Application Log section, choose Search. | The payment request cleared info is presented in the log details. |  |
| 6 | Search and Open Bank Transfer | To find your new payment request, run steps 3-4 above. Open the request. | The bank transfer payment request is presented in the right side of the screen with Cleared status. The Clearing Document No. field shows the clearing document number.Note If the payment request is not cleared and stays in Released status or the batch is not created, you can read the message and also use the App: Automatic Payment Transactions for Payment Requests (F111) to check the application log for your payment run ID. |  |

##### Option 3: Make Bank Transfer with Templates

Purpose

This section describes the process to make bank transfers with templates.

Prerequisite

The sample bank accounts exist, with payment signatories assigned to them. For more information, see the [Maintain Payment Approver for Bank Accounts](#unique_26) [page ] 45 section.

|  |
| --- |
| Note The app My Inbox - Process Rejected Payments (F4546) mentioned in step [Process Rejected Payments (Optional)](#unique_64) [page ] 117 cannot be used for processing rejected payments documents created for payment requests. |

###### Define Bank Transfer Templates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you maintain bank transfer templates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Define Bank Transfer Templates (F3759). |  |  |
| 3 | Create Bank Transfer Templates | To create a template, choose Create. Make the following entries and choose Create:Payer Information:Template: for example, RC001Paying Bank Account: for example, 0000000693123456Paying Company Code: 3310Paying House Bank: for example, AEBK1Paying House Bank Account: for example, AEAC1Payee Information:Receiving Bank Account: for example, 0000000693123456Receiving Company Code: 3310Receiving House Bank: for example, AEBK2Receiving House Bank Account: for example, AEAC2Transaction Information:Payment Method: <existing payment method for credit transfer>Note Only payment methods that are applicable to the paying bank account are listed.Currency: for example, AED | The Bank Transfer Template is successfully saved. The template is shown in display mode with all information filled.Note The system performs checks when saving the template, such as:bank account validation in current periodbank account with valid house bank and house bank account IDpayment method properly configured for the paying company code's countrypayment method configured for the selected currencyIf an error message occurs, read the message and take any required actions. |  |
| 4 | Close Bank Transfer Templates | To close the right panel, choose Close. | The Define Bank Transfer Templates screen displays. |  |
| 5 | Edit a Bank Transfer Template | Choose Edit on the top right corner. Make some changes and choose Save.Note Some fields cannot be changed, such asRepetitive CodePaying Bank AccountPaying Bank Account ID | The Bank Transfer Template is successfully saved. |  |
| 6 | Delete a Bank Transfer Template(option1) | Choose Delete on the top right corner. On the dialog box, choose Delete to confirm the interaction. | The bank transfer template is deleted.Note If you delete the bank transfer template, go back to the previous step to create a new bank transfer template. |  |
| 7 | Delete Multiple Bank Transfer Templates (option2) | Execute steps 3 - 5 to create multiple bank transfer templates. Search for the templates, select them, and choose Delete. On the dialog box, choose Delete to confirm the interaction. | The selected bank transfer templates are deleted.Note If you delete the bank transfer template, go back to the previous step to create a new bank transfer template. |  |

###### Create Bank Transfers with Templates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you make bank transfer with templates.

Prerequisite

The relevant bank transfer templates have been created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Make Bank Transfers - Create with Templates (F3760).Note Alternatively, you can open Make Bank Transfers (F0691), then choose Create with Templates to get into the Make Bank Transfers - Create with Templates (F3760) app. | The Make Bank Transfers – Create with Templates view displays. |  |
| 3 | Search Bank Transfer Templates | All available bank transfer templates are listed. Search for the specific bank transfer template created previously (searching for its repetitive code, paying company code or paying bank account). | All the bank transfer template records matching the search criteria are listed. |  |
| 4 | Create a Payment Request - New Bank Transfers（Option 1） | Select a bank transfer template.Choose Show More per Row at the right corner and make the following entries:Note choose Settings to open more fields.Transfer Date: <current date>Amount: <transfer amount>Currency: AED (change if required)Reference Text: <description>Release and Pay: <deselected>Note If you choose Release and Pay, you can skip further steps Release Payment Request and Pay Payment Request.Single Payment: <select per your request>Note If you want to designate instruction key for the payment re quests, enter following instruction key & instruction fields.Instruction Key: <via Value Help>Instruction 1: <via Value Help>Instruction 2: <via Value Help>Instruction 3: <via Value Help>Instruction 4: <via Value Help>Choose Create.Make a note of the payment request number: __________ | The Bank Transfers are created. Also a new payment request with Created status is created for the repetitive code. |  |
| 5 | Create Multiple Payment Requests - New Bank Transfers(Option 2) | Execute step 3-4, but choose several templates to maintain and Create.Choose Close to confirm the message" | The payment requests are listed.Note The Message pop up telling that payment request is created or not created for the repetitive codes. |  |

###### Release Payment Request

Purpose

In this activity, you release a payment request..

Procedure

Please refer to step [Release Payment Request](#unique_79) [page ] 135 in this document.

###### Pay Payment Request

Purpose

In this activity, you pay a payment request.

Procedure

Please refer to step [Pay Payment Request](#unique_80) [page ] 136 in this document.

#### Approve and Bank Integration

Purpose

After the bank transfer is executed, a Bank Communication Management (BCM) batch or several BCM batches are created automatically. The BCM batches are approved as described in this procedure.

After approval, if a MBC credit transfer payment medium format was used in bank transfer, the payment medium format file can be sent to Multi-Bank Connectivity (MBC) for bank payment processing, as described in Bank Integration with SAP Multi-Bank Connectivity (16R). If in the SAP S/4HANA Enterprise Management system the payment medium format for the file download was used in cash concentration, the payment medium format file can be downloaded manually, as described in Bank Integration with File Interface (1EG).

Procedure

Run the steps in the previous Approve and Bank Integration procedure for payment triggered by using the Make Bank Transfers (F0691) app.

|  |
| --- |
| Note The app My Inbox - Process Rejected Payments (F4546) mentioned in step [Process Rejected Payments (Optional)](#unique_64) [page ] 117 cannot be used for processing rejected payments documents created for payment requests. |

#### Short Term Cash Positioning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After a bank transfer is made, the positions of the paying bank and receiving bank are updated. The head of cash manager can analyze the cash positions by location, company, and currency. Cash position data is calculated based on the cash position profiles that are defined in the Define Cash Position Profiles (F5399) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Short-Term Cash Positioning (F5380). | The Short-Term Cash Positioning view is displayed. |  |
| 3 | Set Cash Position Profile | Enter the following data and choose Go:Cash Position Profile: <CPP_01, defined in preliminary steps>Note Display cash positions by various analytical dimensions, such as country/region, company code, bank account, currency.In this document, the example cash position profile is defined with hierarchy source Derived from Cash Pool and Bank Account Master Data. The short-term cash positioning is described according to the settings defined in the selected cash position profile. For example, Company code > Bank Account Currency > Bank Account .You can define the cash position profile as per your requirement. The steps may vary. | In the display area, data is displayed in a structure per cash position profile. |  |
| 4 | Review Details at Company Code Level | On the left navigation panel of Bank Account Hierarchy, expand and choose > (Details) against Company Code. | Cash Position Details and Cash Position Overview are shown on the right side. |  |
| 5 | Review Cash Position Overview | On the right side screen, choose the Cash Position Overview tab, choose > (Details) against Currency to check Cash Position Details by planning level.For example, Company code > Bank Account Currency | Cash Position Details by planning level are displayed. |  |
| 6 | Review Cash Position Details | On the right side screen, choose > (Details) against Planning Level to check Cash Position Details by Bank Account.For example, Company code > Bank Account Currency > Planning Level | Cash Position Details By Bank Account is displayed. |  |
| 7 | Check Cash Flow Item by Bank Account | On the right side screen, choose amount to check cash flow item by Bank Account.For example, Company code > Bank Account Currency > Planning Level > Bank Account | Check Cash Flow Item is displayed. |  |
| 8 | Check Cash Position Details at Bank Account Level | On the left navigation panel of Bank Account Hierarchy, choose > (Details) against one bank account. | Cash Position Details and General Information is displayed. |  |
| 9 | Check General Information | On the right side screen, choose the General Information tab, choose the highline date under Opening Balance Date to check Bank Account Opening Balance Details. | Actual Cash Flows for Bank Account Opening Balance is displayed. |  |
| 10 | Check Cash Pool Name (Optional) | On the left navigation panel of Bank Account Hierarchy, choose Expand All. At Bank Account level, check cash pool information under column Cash Pool Name. Multiple cash pool structure can be display on the left navigation panel.Note Choose Settings on the left navigation to select field Cash Pool Name.Then choose > (Details) against Bank account level to check a specific cash pool structure. | Cash Position Details and Cash Pool Structure is displayed.Note When the hierarchy source is defined as 03 (Derived from Cash Pool and Bank Account Master Data) in the cash position profile, bank accounts that are assigned to cash pools of the service provider Bank - Time Dependent are displayed in the cash pool hierarchies. |  |
| 11 | Check Cash Pool Structure (Optional) | On the right side screen, choose the Cash Pool Structure tab, you can check Cash Pool structure for all relevant bank accounts (include header account and subaccounts). | Cash Pool Structure is displayed. |  |
| 12 | Back | Choose Back. |  |  |
| 13 | Export to Spreadsheet | On the left navigation panel of Bank Account Hierarchy, choose the Export to Spreadsheet icon.Note Export of Spreadsheet (Ctrl + Shift + E). | All of the current table contents are exported to a spreadsheet. |  |
| 14 | Review Details by Other Hierarchy Level | On the left navigation panel of Bank Account Hierarchy, expand and choose > (Details) against other hierarchy level.Note You can repeat above steps to monitor cash position details again other hierarchy level. | The Cash position can be displayed by various analytical dimensions, such as country/region, company code, bank account, currency. |  |

### Cash Trade Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create, edit, and delete cash trade requests, which will then be submitted for approval. As a result of your submission, your requests can be released or rejected. The released cash trade requests will then automatically trigger the creation of trade requests in the Treasury and Risk Management (TRM).

Prerequisite

You need to manually enable the cash trade request functionality in the full scope of cash management. This functionality is integrated with Treasury and Risk Management (TRM). You also need to define planning levels for cash trade requests. You can follow the steps in Preliminary Steps section.

1. Enable Cash Request Integration
2. Define Planning Level for Cash Request
3. Assign Planning Level to Cash Request

#### Create and Submit Cash Trade Request for FX

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Cash Specialist create and submit Cash Trade Request for FX.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Memo Records (F2986). |  |  |
| 3 | Create Cash Trade Request (FX) | Choose Create Memo Record/... > Create Cash Trade Request (FX). | The Memo Record view displays.Note The certainty level for the new memo record is Cash Trade Request. |  |
| 4 | Enter Cash Trade Request Data | In the Cash Trade Request Data section, make following mandatory fields and choose Enter:Instrument Category: for example, FXFW (FX Forward)Value Date: <current date+3 months>Buy / Sell: BuyCompany Code: 3310Requested Amount: for example, 1000,000USDRequested Opposite Amount(Forecasted): <in the second field, enter the opposite currency, for exampleAED>Choose Enter, Opposite Amount is activated for input. Enter the Opposite Amount if needed.Note Use Adapt Filters to view any missing fields in the view. |  |  |
| 5 | Create Cash Trade Request | Choose Create.Note Before submitting, you can edit or delete the cash trade request via choose Edit or Delete. | The cash trade request is created with status Created. |  |
| 6 | Submit Cash Trade Request | Choose Submit.After Submitted, you can not edit or delete the cash trade request. | The cash trade request is submitted for approval and its status is also updated as Submitted. |  |
| 7 | Save and Submit Cash Trade Request in One Step (Optional) | Note You can also save and submit cash trade request in one step as following:Repeat steps 1-5, then choose Save and Submit. | The cash trade request is saved and submitted in one step. |  |

#### Create and Submit Cash Trade Request for Money Market

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Cash Specialist create and submit Cash Trade Request for Money Market.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Memo Records (F2986). |  |  |
| 3 | Create Money Market Request (MM) | Choose Create Memo Record/... and choose Create Cash Trade Request (MM) from dropdown list. | The Memo Record view displays.The certainty level for the new memo record is Cash Trade Request. |  |
| 4 | Enter Cash Trade Request Data | On the Cash Trade Request Data section, make following mandatory fields and choose Enter:Instrument Category: MM (Money Market Undefined)Invest / Borrow: <Invest or Borrow>Term Start Date: <current date>Term End Date: <current date+1 year>Company Code: 3310Requested Amount: for example, 1000,000AED |  |  |
| 5 | Cash Trade Request | Choose Create.Before submitting, you can edit or delete the cash trade request via choose Edit or Delete. | The Cash Trade Request is created with status Created. |  |
| 6 | Cash Trade Request | Choose Submit.After submitting, you can not edit or delete the cash trade request. | The cash trade request is submitted for approval and its status is also updated as Submitted. |  |
| 7 | Cash Trade Request in One Step (Optional) | You can also save and submit Cash Trade request in one step as following:Repeat steps 1-5, then choose Save and Submit. | The Cash Trade request is saved and submitted in one step. |  |

#### Release Cash Trade Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Cash Manager release the Cash Trade Request.

|  |
| --- |
| Note The other user is used to approve and release the cash trade request. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Memo Records (F2986). |  |  |
| 3 | Search Cash Trade Request | Make the following entries and choose Go.Company Code: 3310Certainty Level: Cash Trade RequestCash Trade Request Status:S(Submitted)Note Choose Adapt Filters to add the fields as filter if needed. | The cash trade requests are displayed. |  |
| 4 | Release Cash Trade Request | Select a cash trade request and choose Release.Note Follow the relevant procedure in the Treasury Trading via Trading Platforms (2F5) test script to send the trade request to trading platforms through SAP Cloud Platform. | The cash trade request is released, then automatically trigger the creation of trade requests in the Treasury and Risk Management (TRM).After the deal is performed in trading platform, cash trade request gets response from Trade Request and update the status. |  |
| 5 | Check Trade Request | In the General Information section, choose the highlighted number of trade request. The relevant trade request displays. |  |  |

#### Reject Cash Trade Request (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Cash Manager rejects a Cash Trade Request

|  |
| --- |
| Note The other user is used to reject the cash trade request. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Memo Records (F2986). |  |  |
| 3 | Search Cash Trade Request | Make the following entries and choose Go.Company Code: 3310Certainty Level: Cash Trade RequestCash Trade Request Status:S(Submitted)Note Choose Adapt Filters to add the fields as filter if needed. | The cash trade requests are displayed. |  |
| 4 | Reject Cash Trade Request | Select a cash trade request and choose Reject. | The cash trade request is rejected, and its status is updated as Created.Note The creator can adjust the cash trade request and submit again. |  |

#### Treasury Management Integration for Trading Platform

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you send the cash trade request to trading platforms through SAP Cloud Platform.

After a deal is performed in a trading platform, the cash trade request gets a response from the Trade Request and the status is updated accordingly.

- If the whole deal is fulfilled in the trading platform, the cash trade request is updated as Completed
- If the whole deal is canceled in the trading platform, the cash trade request status is updated as Canceled.
- If the deal is split and partial fulfilled(or partial declined) in the trading platform, the cash trade request status is updated as In Process. Then the remaining part is partial fulfilled (or partial declined) in the trading platform, the cash trade request status is finally updated as Completed.

Prerequisite

The cash trade request has been released.

Procedure

Follow the relevant procedure in the Treasury Trading via Trading Platforms ([2F5](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/2F5)) test script.

#### Fulfill Cash Trade Request as Deal Done

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Follow the relevant procedure in the Treasury Trading via Trading Platforms ([2F5](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/2F5)) test script to send the cash trade request to a trading platform through SAP Cloud Platform.

After the deal is done in the trading platform and the TR transaction was created, a cash trade request gets a response from the Trade Request and updates the status to Completed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Memo Records (F2986). |  |  |
| 3 | Search Cash Trade Request | Make the following entries and choose Go.Company Code: 3310Certainty Level: Cash Trade RequestCash Trade Request Status:F(Completed)Note Choose Adapt Filters to add the fields as filter if needed. | The cash trade requests are displayed. |  |
| 4 | Check Trade Cash Trade Request | Select a cash request to check. | The cash request status is updated as Completed. |  |
| 4 | Check Trade Request | Click Trade Request number which is highlighted with Blue. | Trade Request detailed information is displayed. |  |

#### Cancel Cash Trade Request as Deal Cancel

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Follow the relevant procedure in the Treasury Trading via Trading Platforms ([2F5](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/2F5)) test script to send the trade request to trading platforms through SAP Cloud Platform.

If deal is canceled in trading platform, cash trade request status is updated as Canceled.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Memo Records (F2986). |  |  |
| 3 | Search Cash Trade Request | Make the following entries and choose Go.Company Code: 3310Certainty Level: Cash Trade RequestCash Trade Request Status:X(Canceled)Note Choose Adapt Filters to add the fields as filter if needed. | The change requests are displayed. |  |
| 4 | Check Cash Trade Request | Select a cash trade request to check. | The cash trade request status is updated as Canceled. |  |
| 5 | Check Trade Request | Click Trade Request number which is highlighted with Blue. | Trade Request detailed information is displayed. |  |

#### Check Partial Fulfill or Partial Decline Cash Trade Request Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Follow the relevant procedure in the Treasury Trading via Trading Platforms ([2F5](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/2F5)) test script to send the cash trade request to trading platforms through SAP Cloud Platform.

If a deal is split and partial fulfilled(or partial declined) in a trading platform, the cash trade request status is updated as In Process. Then the remaining part is partial fulfilled (or partial declined) in a trading platform, the cash trade request status is finally updated as Completed.

|  |
| --- |

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Derive Liquidity Item Online is stated to work only with Deferred liquidity analysis update mode, yet the example for company code 3310 sets Liquidity Analysis Update Mode to Close to Real Time while also using Derive Liquidity Item Online for 3310.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Flow Builder runtime parameters still define a Chain Step maximum (1-12, default 6), while the Stop Condition section says the technical concept for chain step is removed in Flow Builder.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[05-treasury-and-cash-management/advanced-cash-operations-j78-ae-test-script-sap-s-4hana-cloud-public-e-part-02]]
- related-to :: [[05-treasury-and-cash-management/basic-cash-operations-bfb-ae-test-script-sap-s-4hana-cloud-public-edit]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J78_S4CLD2608_BPD_EN_AE.docx` — lines 1–3312 of the extracted text · extracted with `mammoth` · 349,191 chars in the whole document
