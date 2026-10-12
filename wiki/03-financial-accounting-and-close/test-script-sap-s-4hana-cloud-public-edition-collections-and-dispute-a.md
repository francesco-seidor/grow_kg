---
id: 03-financial-accounting-and-close/test-script-sap-s-4hana-cloud-public-edition-collections-and-dispute-a
title: Test Script SAP S/4HANA Cloud Public Edition - Collections and Dispute Automation (7MA_AE) (7MA_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 7MA (AE): setup, dispute creation and processing, collections worklist, background jobs."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/collections-and-dispute-management]
aliases: [7MA_S4CLD2608_BPD_EN_AE]
keywords: [Collections and Dispute Management, collections and dispute automation, dispute creation, dispute processing, collections management, collections worklist, prioritization rules, brf+ rules, background jobs, initial configuration]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7MA_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1218
topic: 03-financial-accounting-and-close/collections-and-dispute-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Collections and Dispute Automation (7MA_AE) (7MA_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7MA_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Collections and Dispute Management** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 06-09-26 |
| --- | --- |
|  | Collections and Dispute Automation (7MA_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc241658569)

[2 Prerequisites 4](#_Toc241658570)

[2.1 System Access 4](#_Toc241658571)

[2.2 Roles 5](#_Toc241658572)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc241658573)

[2.4 Business Conditions 6](#_Toc241658574)

[2.5 Preliminary Steps 7](#_Toc241658575)

[2.5.1 Maintain Current Settings in Collection and Dispute Automation via Report 7](#_Toc241658576)

[2.5.2 Define Company Codes for Collections and Dispute Automation 9](#_Toc241658577)

[2.5.3 Map FI Company Codes to Company Codes in Collections and Dispute Automation 10](#_Toc241658578)

[2.5.4 Copy Rules in BRF+ 11](#_Toc241658579)

[2.5.4.1 Copy Dispute Management Rules in BRF+ 11](#_Toc241658580)

[2.5.4.2 Copy Collections Management Rules in BRF+ 12](#_Toc241658581)

[2.5.5 BRF+ Settings for Process Automation 13](#_Toc241658582)

[2.5.5.1 BRF+ Settings for Process Automation 13](#_Toc241658583)

[2.5.5.2 BRF+ Settings for Process Automation in Collections Processes 14](#_Toc241658584)

[2.5.6 Activate Transfer of Receivable/Payable Items 15](#_Toc241658585)

[2.5.7 Schedule Initial Load for Receivable/Payable Items 16](#_Toc241658586)

[2.5.8 Activate Collections and Dispute Automation 17](#_Toc241658587)

[2.5.9 Transfer Receivable/Payable Items 18](#_Toc241658588)

[2.5.10 Schedule Build Receivable Items Job 19](#_Toc241658589)

[2.5.11 Migrate Legacy Objects 20](#_Toc241658590)

[3 Overview Table 22](#_Toc241658591)

[4 Test Procedures 24](#_Toc241658592)

[4.1 Organizational Structure 24](#_Toc241658593)

[4.1.1 Define Collection Segments 24](#_Toc241658594)

[4.1.2 Define Segment Groups 25](#_Toc241658595)

[4.1.3 Manage Prioritization Rules 26](#_Toc241658596)

[4.1.4 Define Teams 28](#_Toc241658597)

[4.1.5 Manage Master Data in Collections and Dispute Automation 29](#_Toc241658598)

[4.2 Dispute Creation 31](#_Toc241658599)

[4.2.1 Create Dispute via Manage Disputes 31](#_Toc241658600)

[4.2.2 Create Dispute via Manage Receivable Items 32](#_Toc241658601)

[4.2.3 Create Dispute via Underpayment with Reason (Optional) 33](#_Toc241658602)

[4.3 Dispute Processing 35](#_Toc241658603)

[4.3.1 Classify and Assign Disputes 35](#_Toc241658604)

[4.3.2 Evaluate Dispute 36](#_Toc241658605)

[4.3.3 Decide Dispute 37](#_Toc241658606)

[4.3.4 Finalize Dispute 39](#_Toc241658607)

[4.4 Collections Management 40](#_Toc241658608)

[4.4.1 Call Worklist 40](#_Toc241658609)

[4.4.2 Create Promise to Pay 41](#_Toc241658610)

[4.4.3 Create Task 42](#_Toc241658611)

[4.4.4 Create Dispute 44](#_Toc241658612)

[4.4.5 Create Activity 45](#_Toc241658613)

[4.5 Schedule Background Jobs 46](#_Toc241658614)

[4.5.1 Schedule Jobs for Collections Automation 46](#_Toc241658615)

[4.5.2 Schedule Jobs for Dispute Resolution 48](#_Toc241658616)

## Purpose

Overview

This scope item streamlines collections activities for accounts receivable, supports resolution of customer invoice disputes, and manages overdue items efficiently. It helps reduce exposure to potential write-offs through earlier, targeted follow-ups.

With tools in the dispute resolution process, processors can efficiently manage disputes, as well as proactively manage and collect overdue receivables. Specialists have all the information and support they need to collect payments faster and provide improved customer service.

Collection specialists can proactively manage and collect overdue receivables with receivables collections tools and dunning integration. The specialists have all the information and support they need to collect payments faster and provide improved customer service. They can identify bad debt risk potential and take preventative steps to reduce further exposure.

|  |
| --- |
| Caution SAP provides two scope items related to dispute resolution: Collections and Dispute Management (BFC) and Collections and Dispute Automation (7MA). Before you make the choice to use the dispute resolution process of 7MA, please read the [Integration with Other Components](https://help.sap.com/docs/SAP_S4HANA_CLOUD/918bca53037f408f91a2295d04ac16bc/8613c1d67fed4fdbb9118859cfc3c285.html) topic on SAP Help Portal for more information. |

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

To perform the steps in this test script:

- Customer master data exists
- Invoices are created and posted to Account Receivable accounting
- You’ve activated the Collections and Dispute Automation (7MA) scope item
    - If 7MA isn't on the activation list, you must create a ticket on component XX-S4C-OPR-SRV to the CBC Operations Team to add it.
- Current settings are maintained as described in the Preliminary Steps section
- All Collection, Dispute and Receivable Item customizing activities are completed
- Optional: BRF+ rules are maintained
- RPI integration is active and initial data load is performed

|  |
| --- |
| Note BRF+ rules are required to automate determination of dispute attributes and control process integration with FI-A/R (block/unblock items for dunning and/or payments, automatically create disputes). |

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/7MA_S4CLD2602_BPD_EN_DE.docx) ). |

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
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |
| Accounts Receivable Manager | SAP_BR_AR_MANAGER | Accounts Receivable | SAP_BR_AR_MANAGER |  |
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices Package, you can use the following Package scenario data:

| Master Data Name | Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Controlling Area | A000 |  |  |
| Customer | S331002513310000133100002 |  |  |
| House Bank | AEBK1AEBK2 |  |  |
| Bank G/L Account | 6100700011002000 |  |  |
| Cost Center | 33101101 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNM | Create Cost Center and Cost Center Group - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BD9 - Sell from Stock | Run before this test script. Invoices are created and posted to accounting. Instructions on how to cancel a billing document are included. |
| J14 - Sales Order Processing – Project-Based Services | Run before this test script. Invoices are created and posted to accounting. |
| J59 - Accounts Receivable | Posting accounting data for customers in Accounts Receivable. |
| J78 - Advanced Cash Operations | Run this test script to upload bank statements. |

Optional: You can configure the following functionality to test this scope item.

Table 2: Integration to Other Applications

| Functionality | Application Name | Details |
| --- | --- | --- |
| Bank connectivity | Financial Services Network | Must send payment instructions to the bank and receive bank statements from the bank. |
| Load electronic bank statements |  | Bank statements should be loaded into Financials automatically through a standard interface to banks. Customers shouldn't be requested to set up the interface to the banks first.They should be able to adjust the reconciliation rules for the bank statement, but the interface should be part of the service that’s available with the Public Cloud solution. |

### Preliminary Steps

#### Maintain Current Settings in Collection and Dispute Automation via Report

Purpose

In this activity, you maintain current settings in collection and dispute automation via report. The report fills the tables behind the following current settings apps:

- Define FI company codes
- Define Payment Difference Reasons
- Define Posting Classifications
- Define Posting Subclassifications

For more details on maintaining the current settings, see [Transfer Current Settings from Finance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/918bca53037f408f91a2295d04ac16bc/15e76abe309347b5b54a73fa137d1c46.html?version=LATEST) on the SAP Help Portal.

Prerequisites

FI customizing is complete.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Integration Jobs for Collections and Dispute Automation (F8377). | The Schedule Integration Jobs view is displayed. |  |
| 3 | Create Job | Choose Create. | The New Job view is displayed. |  |
| 4 | Enter Job Details | Make the following entries and choose Step 2:Job Template: Transfer Current Settings from FinanceJob Name: Transfer Current Settings from Finance |  |  |
| 5 | Maintain Job Details | Make the following entries and choose Step 3:Start Immediately: SelectedRecurrence Pattern: Single Run |  |  |
| 6 | Maintain Parameters | Make the following entries and choose Schedule:Create FI-Company Codes: SelectedCreate Posting Classifications: SelectedCreate Posting Subclassificatn: SelectedCreate Payment Difference Reasons: Selected | The job is scheduled. |  |
| 7 | Verify FI Company Code Transfer | Open Define FI Company Codes for Collections and Dispute Automation (/DCO/V_CCODE_FI).Verify that the company code entries are listed and the logical system is assigned. | Company code entries are present with a logical system assigned.Caution If entries are present, continue with the [Define Company Codes for Collections and Dispute Automation](#unique_8) [page ] 9 step. If entries are missing, perform the activities in the Troubleshooting table below. |  |

Table 3: Troubleshooting - Define FI Company Codes for Collections and Dispute Automation

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Caution Only perform this activity if the company code entries are missing per the Verify step above.Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Define FI Company Codes for Collections and Dispute Automation (/DCO/V_CCODE_FI). |  |  |
| 3 | New Entries | Choose New Entries. |  |  |
| 4 | Enter Company Code | Enter the Company Code (FI System) (for example, 3310). |  |  |
| 5 | Select Logical System | In the Logical System field, use the value help button and select the correct logical system for the tenant. |  |  |
| 6 | Save | Choose Save. | You saved the FI Company Code entry. |  |

#### Define Company Codes for Collections and Dispute Automation

Purpose

In this activity, you define the debt collections company codes. The company codes in Collections and Dispute Automation represent organizational units that define how collections activities are structured internally.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Collections Management

1. For the row with Item Name of Organizational Setup in Collections and Dispute Automation, choose Details (>).
2. For the Define Company Codes for Collections and Dispute Automation row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Company Codes for Collections and Dispute Automation.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Change | Choose Display > Change to go into change mode. |  |  |
| 2 | New Entries | Choose New Entries. |  |  |
| 3 | Enter Details | Make the following entries and choose Save:Comp. Code (C. and D. Autom.) : <company code>, for example, 3310Company Code Description: <description>, for example, Company Code 3310Company Code Currency : <currency>, for example, AED | The debt collections company code is defined. |  |

#### Map FI Company Codes to Company Codes in Collections and Dispute Automation

Purpose

In this activity, you define mappings of FI company codes to debt collections company codes. This is required to complete the integration of Collections and Dispute Automation with Financial Accounting. If this isn't configured, you will encounter errors when performing the test procedures.

Prerequisites

The company codes are created in the Finance area.

Debt Collections company codes are defined in Dispute Management.

Procedure

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Map Company Codes for Collections and Dispute Automation (/DCO/V_CCODE_M).
3. Choose New Entries.
4. Choose Company Code (FI System). The Logical System is set automatically according to settings in the Define FI Company Codes for Collections and Dispute Automation (/DCO/V_CCODE_FI) app.
5. Maintain the corresponding Company Code (C. and D. Autom.).
6. Save your entries.

#### Copy Rules in BRF+

##### Copy Dispute Management Rules in BRF+

Purpose

In this activity, you create the application in BRF+. You then define rules for process automation in Dispute Management.

Prerequisites

All activities are performed in the order described above.

Procedure

| Test Step # | Test Step Name | Instructions | Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Jobs for Dispute Resolution in Collections and Dispute Automation (F8713). |  |  |
| 3 | Create | Choose Create. | The New Job view is displayed. |  |
| 4 | Job Template | Make the following entries and choose Step 2:Job Template: Copy Rules for Dispute ResolutionJob Name: Copy Rules for Dispute ResolutionNote: If you are unable to select the job template, you may need to first remove the defaulted job template. |  |  |
| 5 | Default Values | Keep the default values and choose Step 3. |  |  |
| 6 | Schedule | Choose Schedule. | The job's initial status is In Progress. |  |
| 7 | Check Log | To refresh the status, choose Go.When the Status changes to Finished, you can choose the button for that job in the Log column to review the job details. |  |  |

##### Copy Collections Management Rules in BRF+

Purpose

In this activity, you create the application in BRF+. You then define rules for process automation in Collections Management.

Prerequisites

All activities are performed in the order described above.

Procedure

| Test Step # | Test Step Name | Instructions | Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Jobs for Collections and Dispute Automation (F8376). |  |  |
| 3 | Create | Choose Create. | The New Job view is displayed. |  |
| 4 | Job Template | Make the following entries and choose Step 2:Job Template: Copy Rules for the Collections ProcessJob Name: Copy Rules for the Collections ProcessNote If you can't select the job template, you may need to first remove the defaulted job template. |  |  |
| 5 | Default Values | Keep the default values and choose Step 3. |  |  |
| 6 | Schedule | Choose Schedule. | The job's initial status is In Progress. |  |
| 7 | Check Log | To refresh the status, choose Go.When the Status changes to Finished, you can choose the button for that job in the Log column to review the job details. |  |  |

#### BRF+ Settings for Process Automation

##### BRF+ Settings for Process Automation

Purpose

In this activity, you define BRF+ rules for process automation in the dispute resolution process. The rules configured in BRF+ enable the automation of the following actions:

- Dispute creation
- Determination of responsible parties
- Determination of attributes on dispute level
- Escalation process control
- Update on processing blocks on receivable items

Prerequisites

All previous steps are successfully completed.

Procedure

|  |
| --- |
| Note The steps are explained using the example of the rule for dispute creation. Values used in the description are example values; adjust them to real customer values and demands. For more information, see the [Dispute Resolution in Collections and Dispute Automation](https://help.sap.com/docs/SAP_S4HANA_CLOUD/918bca53037f408f91a2295d04ac16bc/a38fee2b0a024ee48d86d58b258e4dd1.html?version=LATEST) topic on the SAP Help Portal. |

1. Log on to the SAP Fiori launchpad as an Accounts Receivable Manager.
2. Open Manage Rules for Dispute Resolution (WDA0483).
3. In My Applications, expand Dispute Rules > Expression > Decision Table and choose Automatically Create Dispute with Reason.
4. In the Decision Table: /DCO/DISPUTE_REASON_CODE, Automatically Create Dispute with Reason view, choose Edit.
5. In the Table Content section, choose + (Insert New Row).
6. Select Company Code (FI System), then choose the condition Is Equal To, and enter a value (for example, 3310) and choose OK.
7. Maintain Payment Difference Reason (for example, 060) as described in the previous step.
8. Maintain a Reason (for example, 006) as described in step 6.
9. Save your entries.
10. Choose Activate. Confirm the activation.

##### BRF+ Settings for Process Automation in Collections Processes

Purpose

In this activity, you define BRF+ rules for process automation in the dispute resolution process. The rules configured in BRF+ enable the automation of the following actions:

- Determination of Collector Groups
- Determination of AR Accountant Groups
- Determination of Prioritization Rules
- Update on processing blocks on receivable items

Prerequisites

You have performed all previous steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Rules for Collections Processes (WDA0483). |  |  |
| 3 | Expand Menu | In My Applications, expand Collections Rules > Expression > Decision Table and choose Automatically Create Dispute with Reason. | The Decision Table: /DCO/ACCT_PRIORITIZATION_RULE, Account Prioritization Rule view is displayed. |  |
| 4 | Edit | Choose Edit. |  |  |
| 5 | Insert New Row | In the Table Content section, choose + (Insert New Row). |  |  |
| 6 | Enter Condition | Select Direct Value Input for Debt Collections Segment, then choose the condition Is Equal To, and enter a value (for example, 3310) and choose OK. |  |  |
| 7 | Maintain Rule | Maintain an Account Prioritization Rule (for example, defined in Manage Teams step) as described in the previous step. |  |  |
| 8 | Save | Save your entries. |  |  |
| 9 | Activate | Choose Activate. Confirm the activation. |  |  |

#### Activate Transfer of Receivable/Payable Items

Purpose

In this activity, you activate the replication of Accounts Payable and Accounts Receivable items for the Collections and Dispute Automation.

Prerequisites

The company code is created.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Dispute Resolution

1. For the row with Item Name of Dispute Resolution in Collections and Dispute Automation, choose Details (>).
2. For the Define Company Codes for Receivables Items/Payables Items row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Company Codes for Receivables Items/Payables Items.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Change | Choose Display > Change to go into change mode. |  |  |
| 2 | New Entries | Choose New Entries. |  |  |
| 3 | Enter Details | Make the following entries and choose Save:Appl: FI-APARCoCd: <company code> | The company code is activated to transfer Receivable/Payable Items. |  |

#### Schedule Initial Load for Receivable/Payable Items

Purpose

In this activity, you schedule the initial load for receivable/payable items and review the job log.

Procedure

| Test Step # | Test Step Name | Instructions | Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Receivable/Payable Item Jobs (F8418). |  |  |
| 3 | Create | Choose Create. | The New Job: APAR Receivable Payable Initial Load view is displayed. |  |
| 4 | Job Template | Make the following entries and choose Step 2:Job Template: APAR Receivable Payable Initial LoadJob Name: APAR Receivable Payable Initial Load |  |  |
| 5 | Default Values | Keep the default values and choose Step 3. |  |  |
| 6 | Company Codes | For the initial load, select the company codes you used in the Activate RPI step and choose Schedule.Note If you select a company code that isn't active in the system, you receive an error message in the log. | The Schedule Jobs for Receivable Items/Payable Items view is displayed. |  |
| 7 | Check Log | The job's initial status is In Progress. To refresh the status, choose Go.When the Status changes to Finished, you can choose the button for that job in the Log column to review the job details. | For active company codes that weren't loaded, the log displays success messages. For company codes that are active and are already loaded, the log displays an information message. For company codes that aren't active, the log displays an error message that the company code isn’t defined for receivable/payable items.Caution If the log shows an error that reprocessing is required, run this transaction again, but use the APAR Receivable Payable Reprocess Exception Load Job template and job name. There are no parameters to maintain; the job runs for all failed company codes. Once the job is run, you can review the log. |  |

#### Activate Collections and Dispute Automation

Purpose

In this activity, you activate company codes for the collections and dispute automation process. Disputes can only be created for receivable items posted in an active company code.

Prerequisites

The company code is created.

Procedure

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Activate Debt Collections Management (DCO_ACTIVATION).
3. Choose New Entries.
4. Select a CoCd (for example, 3310).
5. For the relevant company codes, select the Collections and Dispute Autom. Is Active checkboxes.
6. Save your entries.

#### Transfer Receivable/Payable Items

Purpose

In this activity, you schedule the job to transfer receivable and payable items from FI into the Collections and Dispute Automation system.

Procedure

| Test Step # | Test Step Name | Instructions | Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Integration Jobs for Collections and Dispute Automation (F8377). | The Schedule Integration Jobs view is displayed. |  |
| 3 | Create | Choose Create. | The New Job: Transfer Receivable/Payble Items view is displayed. |  |
| 4 | Job Template | Make the following entries and choose Step 2:Job Template: Transfer Receivable/Payable ItemsJob Name: Transfer Receivable/Payable Items |  |  |
| 5 | Default Values | Keep the default values and choose Step 3. |  |  |
| 6 | Company Codes | Select the company codes you used in the prior step and choose Schedule.Note If you select a company code that isn't active in the system, you receive an error message in the log. | The job is created with In Progress status. |  |
| 7 | Check Log | To refresh the status, choose Go.When the Status changes to Finished, choose the button for that job in the Results column to review the job results. |  |  |

#### Schedule Build Receivable Items Job

Purpose

In this activity, you schedule the job to build receivable items.

Procedure

| Test Step # | Test Step Name | Instructions | Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Jobs for Dispute Resolution in Collections and Dispute Automation (F8713). |  |  |
| 3 | Create | Choose Create. | The New Job view is displayed. |  |
| 4 | Job Template | Make the following entries and choose Step 2:Job Template: Build Receivable ItemsJob Name: Build Receivable ItemsNote If the job template isn't shown, you may need to remove the defaulted template from the field. |  |  |
| 5 | Default Values | Keep the default values and choose Step 3. |  |  |
| 6 | Company Codes | Make the following entries and choose Schedule:Company Code (FI System): <company code> (from the [Activate Collections and Dispute Automation](#unique_16) [page ] 17 step)Percentage of Occupied Tasks: 100Package Size: 10Number of Parallel Tasks: 10Note If you select a company code that isn't active in the system, you receive an error message in the log. |  |  |

#### Migrate Legacy Objects

Purpose

In this activity, you schedule jobs to migrate legacy business objects from collections management. This step is relevant only for customers transitioning from applications in the Collections and Dispute Management (BFC) scope item to applications in the Collections and Dispute Automation (7MA) scope item.

Procedure

| Test Step # | Test Step Name | Instructions | Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Integration Jobs for Collections and Dispute Automation (F8377). |  |  |
| 3 | Create | Choose Create. | The New Job view is displayed. |  |
| 4 | Job Template | Make the following entries and choose Step 2:Job Template: Migrate Master Data for Collections and Dispute AutomationJob Name: Migrate Master Data for Collections and Dispute AutomationNote If the job template isn't shown, you may need to remove the defaulted template from the field. |  |  |
| 5 | Default Values | Keep the default values and choose Step 3. |  |  |
| 6 | Parameters | Make the following entries and choose Schedule:Percentage of Occupied Tasks: 15Package Size: 500Number of Parallel Tasks: 10Test run: Deselected |  |  |

If needed, repeat steps 3 - 6 for the following jobs:

- SAP_DCO_ACTIVITY_MIGRATION
- SAP_DCO_MIGRATE_DISPUTES
- SAP_DCO_P2P_MIGRATION
- SAP_DCO_TASK_MIGRATION

## Overview Table

This scope item consists of several process steps provided in the following tables.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 4: Organizational Structure

| Process Step, Report, or Item | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Define Collection Segments](#unique_21) [page ] 24 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) or SAP CBC Project Experience | You defined collection segments. |
| [Define Segment Groups](#unique_22) [page ] 25 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) or SAP CBC Project Experience | You defined segment groups. |
| [Manage Prioritization Rules](#unique_23) [page ] 26 | Accounts Receivable Manager | Manage Account Prioritization Rules (F8833) | You defined prioritization rules. |
| [Define Teams](#unique_24) [page ] 28 | Configuration Expert - Business Process Configuration | Manage Teams and Responsibilities (F2412) | You defined teams. |
| [Manage Master Data in Collections and Dispute Automation](#unique_25) [page ] 29 | Accounts Receivable Manager | Manage Master Data in Collections and Dispute Automation (F8606) | You created master data. |

Table 5: Dispute Creation

| Process Step, Report, or Item | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create Dispute via Manage Disputes](#unique_26) [page ] 31 | Accounts Receivable Accountant | Manage Disputes (F7876) | You created the dispute manually. |
| [Create Dispute via Manage Receivable Items](#unique_27) [page ] 32 | Accounts Receivable Accountant | Manage Receivable Items (F7877) | You created the dispute manually. |
| [Create Dispute via Underpayment with Reason (Optional)](#unique_28) [page ] 33 | Cash Management Specialist | Reprocess Bank Statement Items (F1520) | You created the dispute manually. |

Table 6: Dispute Processing

| Process Step, Report, or Item | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Classify and Assign Disputes](#unique_29) [page ] 35 | Accounts Receivable Accountant | Manage Disputes (F7876) | You assigned the dispute. |
| [Evaluate Dispute](#unique_30) [page ] 36 | Accounts Receivable Accountant | Manage Disputes (F7876) | You evaluated the dispute. |
| [Decide Dispute](#unique_31) [page ] 37 | Accounts Receivable Accountant | Manage Disputes (F7876) (F7876) | The dispute is decided. |
| [Finalize Dispute](#unique_32) [page ] 39 | Accounts Receivable Accountant | Manage Disputes (F7876) | The dispute is finalized. |

Table 7: Collections Management

| Process Step, Report, or Item | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Call Worklist](#unique_33) [page ] 40 | Accounts Receivable Accountant | Process Worklist in Collections and Dispute Automation (F8832) | You reviewed your worklist |
| [Create Promise to Pay](#unique_34) [page ] 41 | Accounts Receivable Accountant | Process Accounts in Collections and Dispute Automation (F8607) | You created a promise to pay. |
| [Create Task](#unique_35) [page ] 42 | Accounts Receivable Accountant | Process Accounts in Collections and Dispute Automation (F8607) | You created a task. |
| [Create Dispute](#unique_36) [page ] 44 | Accounts Receivable Accountant | Process Accounts in Collections and Dispute Automation (F8607) | You created a dispute case. |
| [Create Activity](#unique_37) [page ] 45 | Accounts Receivable Accountant | Process Accounts in Collections and Dispute Automation (F8607) | You created an activity. |

Table 8: Scheduling Background Jobs

| Process Step, Report, or Item | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Schedule Jobs for Collections Automation](#unique_38) [page ] 46 | Accounts Receivable Accountant | Schedule Jobs for Collections and Dispute Automation (F8376) | You ran background jobs to trigger generation and refresh of the Collections Worklist. |
| [Schedule Jobs for Dispute Resolution](#unique_39) [page ] 48 | Accounts Receivable Accountant | Schedule Jobs for Dispute Resolution in Collections and Dispute Automation (F8713) | You ran background jobs to escalate disputes. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Organizational Structure

#### Define Collection Segments

Purpose

In this activity, you define segments for Collections Management.

Prerequisites

The company code is created.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Collections Management

1. For the row with Item Name of Collections Processes in Collections and Dispute Automation, choose Details (>).
2. For the Maintain Segments for Collections Automation row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Maintain Segments for Collections Automation.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Change | Choose Display > Change to go into change mode. |  |  |
| 2 | New Entries | Choose New Entries. |  |  |
| 3 | Enter Details | Make the following entries and choose Save:Debt Collections Segment: 3310Debt Collections Segment Name: Local 3310 | The segment is created. |  |
| 4 | Assign | Select your entry and choose Assign Company Codes to Segments.Make the following change and choose Save:Comp.Code: 3310 | The company code is assigned to the segment. |  |

#### Define Segment Groups

Purpose

In this activity, you define segment groups for Collections and Dispute Automation.

Prerequisites

The company code is created.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Collections Management

1. For the row with Item Name of Collections Processes in Collections and Dispute Automation, choose Details (>).
2. For the Maintain Segment Groups for Collections Automation row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Maintain Segment Groups for Collections Automation.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Change | Choose Display > Change to go into change mode. |  |  |
| 2 | New Entries | Choose New Entries. |  |  |
| 3 | Enter Details | Make the following entries and choose Save:Segment Group: ZLOCALSegment Group Name: Local Segment GroupingSegment Group is Default: Selected | The segment group is created. |  |
| 4 | Assign | Select your entry and choose Assign Segments to Segment Groups.Make the following change and choose Save:Comp.Code: 3310 | The segment is assigned to the segment group. |  |

#### Manage Prioritization Rules

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define prioritization rules for Collections Worklist generation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Account Prioritization Rules (F8833). |  |  |
| 3 | Create | Choose Create. | The New Object dialog box is displayed. |  |
| 4 | Define | Make the following entries and choose Continue:Account Prioritization Rule: ZRULE_1 |  |  |
| 5 | Enter Details | Make the following entries:Currency: AEDAutomatic Valuation: Selected |  |  |
| 6 | Add | In the Collections Rules section, choose Create | The New Object dialog box is displayed. |  |
| 7 | Define | Enter the following data and choose Continue:Collections Rule: TOTAL_AMT |  |  |
| 8 | Enter Details | Make the following entries:Valuation: 25 |  |  |
| 9 | Add | In the Basic Rules section, choose Create | The Create dialog box is displayed. |  |
| 10 | Create | Select the following from value help and choose Create:Basic Rule: S_BR_00001Note The rule has no parameter limits. Choose > to open the detailed view and refine the parameters. When done, choose Apply. |  |  |
| 11 | Confirm | Choose Apply to finalize the definition. | The Account Prioritization Rule view is displayed. |  |
| 12 | Define | Repeat steps 6 – 11 to add further rules:Collection Rule SINGLE_AMT with Basic Rule S_BR_00003Collection Rule DISP with. Basic Rule S_BR_00009Collection Rule OPEN_TASK with Basic Rule S_BR_00006 |  |  |
| 13 | Save | Choose Create. | The prioritization rule is created. |  |

#### Define Teams

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you configure a collector group for handling assigned accounts, following up actions, and closing tasks.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access the SAP Fiori App | Open Manage Teams and Responsibilities (F2412). |  |  |
| 3 | Create | Choose Create. |  |  |
| 4 | Enter Details | Make the following entries and choose Create:In the Team Information section:Name: <Collector group name>Description: <Collector group description>Status: EnabledType: S_DCO_COLLECTOR_GROUPIn the Team Owner section, choose Create and make the following entry:Business Partner: <User business partner ID>In the Team Members section, choose Create and make the following entry:Business Partner: <User business partner ID> |  |  |

#### Manage Master Data in Collections and Dispute Automation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create master data in Collections and Dispute Automation.

Prerequisite

A business partner master record in roles FLCU00 and UDM0000 exists.

Company code data for company code 3310 exists for the business partner (the company code used for definition of collections segments in the [Define Collection Segments](#unique_21) [page ] 24 topic.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Master Data in Collections and Dispute Automation (F8606). |  |  |
| 3 | Select Customer | Make the following entries and choose Go:Business Partner: <business partner>, for example, S33100251 | The business partner is displayed in the Collections Business Partners pane. |  |
| 4 | Details | For the business partner, choose Details (>). | The Collections Business Partner view is displayed. |  |
| 5 | Edit | Choose the Edit button. | The Collections Business Partner is displayed in editable mode. |  |
| 6 | Maintain Segment Group | Choose Change Segment Group. | The Change Segment Group dialog box is displayed. |  |
| 7 | Define | From the value help, choose the Segment Group that you defined in the [Define Segment Groups](#unique_22) [page ] 25 activity. Choose Change Segment Group. | The Segment Group is changed. |  |
| 8 | Check Collection Segments | If no collection segments are displayed, choose Determine > Determine Segments . | Collection segments are assigned. |  |
| 9 | Check Company Codes | If no company codes are displayed, choose Determine > Determine Company Codes . | Company codes are assigned. |  |
| 10 | Enter Details | Make the following entries and choose Save:Category: <category>, for example, 002 (Corporate)Account Classification: <classification>, for example, 01 (A-Customer)For each Debt Collections Segment, set the Account Prioritization Rule to the prioritization rule you defined in the [Manage Prioritization Rules](#unique_23) [page ] 26 topic. Do the same with the Collector Group from the [Define Teams](#unique_24) [page ] 28topic. |  |  |

### Dispute Creation

#### Create Dispute via Manage Disputes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a dispute for a receivable item.

Prerequisite

An open Financial Accounting (FI) customer invoice exists.

Ensure that you have completed all Preliminary Steps topics in the Prerequisites section. If the preliminary steps (such as [Map FI Company Codes to Company Codes in Collections and Dispute Automation](#unique_9) [page ] 10) are not performed, you will encounter errors.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Disputes (F7876). |  |  |
| 3 | Create | Choose Create. |  |  |
| 4 | Enter Details | Make the following entries where your receivables item is posted to and press Enter:Business Partner: <business partner>Company Code: <company code> | You're redirected to the object page of the dispute (draft) created. |  |
| 5 | Add Receivables | Choose Add Receivables. | The Add Receivable Items dialog box is displayed. |  |
| 6 | Enter Details | Make the following entries and choose Go:Receivables Item: <receivables item ID> |  |  |
| 7 | Select | Select the receivables item and choose Add Receivables Items. | You're redirected back to the dispute object page.The receivable item is now listed in the Disputed Receivables Items section.Dispute attributes are determined according to the BRFplus rules. |  |
| 8 | Save | Choose Create to save the Dispute. | The dispute was saved. |  |

#### Create Dispute via Manage Receivable Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a dispute.

Prerequisite

Open Financial Accounting (FI) items exist.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Receivable Items (F7877). |  |  |
| 3 | Search | Make the following entries and choose Go:Receivables Item: <receivables item> |  |  |
| 4 | Create | Select the receivables item in the result list and choose Create Dispute Action. | The Dispute Created dialog box is displayed. |  |
| 5 | Navigate | Choose Navigate. | The new dispute opens in the Manage Disputes app. |  |
| 6 | Save | Choose Create to save the dispute. |  |  |

#### Create Dispute via Underpayment with Reason (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a dispute from different, manual FI-AR clearing transactions where an underpayment becomes visible (for example, a residual item).

|  |
| --- |
| Note For more information about uploading a bank statement, see the Basic Cash Operations (BFB) test script. |

Prerequisite

Open Financial Accounting (FI) items exist.

A bank statement item is uploaded that isn't automatically cleared with an underpayment of the invoice to be cleared.

|  |
| --- |
| Caution The Reprocess Bank Statement Items (F1520) isn't assigned to the Cash Management Specialist role by default. To use the app with that role (or another role of your choosing), you must update the role. To do so, log in as Administrator, access the Maintain Business Roles (F1492) app, and assign Dispute* related catalogs to the desired user/role. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Reprocess Bank Statement Items (F1520). |  |  |
| 3 | Search | Make the following entries and choose Go:Company Code: 3310House Bank: AEBK1House Bank Account: AEAC1 | A filtered list of bank statement items is displayed. |  |
| 4 | Select Bank Statement Item | Select a row to process, and in the Reprocess column, choose > (Details). | A detailed view of the select bank statement is displayed. |  |
| 5 | Enter Details | In the Details section, verify or enter the following:Account type: Customer and <Customer number>Posting Date: <Today’s date>Payment Amount: <amount lower than the invoice to be paid>Journal Entry Type: DZ | A list of invoices displays at the bottom half of the view in the Open Items section. |  |
| 6 | Clear Item | In the Open Items section, select the invoice to create a dispute case. The amount of the invoice must be larger than the amount paid. Choose Clear for the selected invoice. | The invoice transfers to Items to Be Cleared. The Balance amount on the header must be zero to post. |  |
| 7 | Reprocessing Reason | Verify that the amount in the Allocated amount column is equal to the bank statement item amount in the Details section. Ensure that the balance amount on the header is zero. |  |  |
| 8 | Post | Choose Post. | The Success view is displayed, showing the journal entry number posted. The document created can be displayed. |  |
| 9 | Display Receivable item | Open Manage Receivable Items (F7877). |  |  |
| 10 | Display Receivable Item | Search for the newly created residual item.Choose the receivables item shown in the result list to navigate to the detail page. | Receivable item object page is displayed. |  |
| 11 | Display dispute | In the Related Disputes section, navigate to the dispute and check the attributes set automatically. | The dispute object page is displayed. |  |

### Dispute Processing

#### Classify and Assign Disputes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you assign a dispute to a processor or processor group (such as if the dispute is not assigned, or input is required from a person to resolve the dispute).

Prerequisite

A dispute exists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Disputes (F7876). |  |  |
| 3 | Perform Query | Leave all fields blank. Choose Go. | A list of all disputes is displayed. Unassigned disputes have no entries in the Processor and Processor Group column. |  |
| 4 | Select Dispute | Select the row for a specific dispute and choose Details (>). | The dispute details are displayed. |  |
| 5 | Edit Case | Choose Edit. | You're now in Edit mode. |  |
| 6 | Change Processor | In the Assignments and Agreements section, choose Reassign and Change Process Assignees .Make the following entry and choose Change Process Assignees:Processor: <user ID>Note If you're changing the processor and don't know the User ID, choose the help icon in the Processor field. A search dialog box displays, allowing you to search by name (Description) or User ID. Enter your search and choose Go. Double-click the correct result. | The system displays the message Dispute was reassigned. The dispute is assigned. |  |
| 7 | Enter a Note | In the Notes section, choose New Object and Internal Note, then add the following:Enter Note: <note>, for example, explaining the assignment to the processor |  |  |
| 8 | Save | At the bottom of the view, choose Save. | The dispute updates and saves. |  |

#### Evaluate Dispute

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, as a processor, you search for disputes that are assigned to you.

Prerequisite

A dispute exists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Disputes (F7876). |  |  |
| 3 | Select Processor | Make the following entries and choose Go:Processor: <your User ID> | The list of all disputes assigned to the selected processor is displayed. |  |
| 4 | Select Dispute | Select the row of a specific dispute and choose > (Details). | The new view is displayed with all the details of the dispute. |  |
| 5 | Change Processing Step and Status | Choose the Evaluate processing step.Select Processing Step Status003 (In Process).Choose Change Status. |  |  |
| 6 | Enter Note | Choose Edit.Choose New Object and Internal Note in the Notes section. Enter a comment:Enter Note: <Enter a note> |  |  |
| 7 | Return Dispute to Coordinator | In the Assignments and Agreements section, choose Reassign and Change Process Assignees.Make the following entries:Processor: <coordinator user ID>Note If you don't know the coordinator’s user ID, use the search help in the Processor field. The dialog box lets you search by name (Description) or User ID. Enter your search and choose Go. Double-click on the correct result.By entering the coordinator as the new processor, the dispute is returned to the coordinator for investigation. | The system displays the message Dispute was reassigned. |  |
| 8 | Save | From the bottom of the view, choose Save. | A dispute was saved. |  |

#### Decide Dispute

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, as a processor, you decide if the customer complaint is justified.

Prerequisite

A dispute exists that is linked with a receivable item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Disputes (F7876). |  |  |
| 3 | Select Processor | Make the following entries and choose Go:Processor: <your User ID> | The list of all disputes assigned to the selected Processor is displayed. |  |
| 4 | Select Dispute | Select the row of a specific dispute and choose > (Details). | The new view is displayed with all the details of the dispute. |  |
| 5 | Start decision process | Choose the Decide processing step.Choose Start Decision. |  |  |
| 6 | Set Decision | In the Disputed Receivable Items section, select the disputed receivable item and choose Change Decision. | The Change Decision dialog box is displayed. |  |
| 7 | Set Decision | Make the following entry and choose Change Decision:Decision: Justified | The decision value is changed for the receivable item.The Amount to Be Corrected field is set equal to the Disputed Amount. |  |

#### Finalize Dispute

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, as a processor, you finalize the decision process.

Prerequisite

A dispute exists in status Evaluated .

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Disputes (F7876) |  |  |
| 3 | Select Processor | Make the following entries and choose Go:Processor: <your User ID> | The list of all disputes assigned to the selected Processor is displayed. |  |
| 4 | Select Dispute | Select the row of a specific dispute and choose > (Details). | The new view is displayed with all the details of the dispute. |  |
| 5 | Finalize | Choose the Finalize processing step.Choose Finalize Decision. | The system displays the Decision Process was finalized message.The dispute status is changed to Decided. |  |

### Collections Management

|  |
| --- |
| Note This step verifies the creation of business objects as they would typically be created during a customer contact. The final step consolidates and records the outcomes of the contact in an Activity. For efficiency – and to ensure the Activity correctly links all information about any created promises to pay, disputes, and tasks – complete all activities in this chapter in one pass to avoid reopening the SAP Fiori app Process Accounts in Collections and Dispute Automation (F8607). |

#### Call Worklist

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you call the worklist in your role as collections agent. The worklist is created by a job, which reviews the customer situation against the rules in the assigned prioritization rule. The worklist contains an entry for all customers to be contacted. Customers are already prioritized according to the score assigned by the prioritization rule.

Prerequisite

A segment group is assigned to a business partner.

A prioritization rule is assigned on the segment level.

The assignment was created in the [Manage Master Data in Collections and Dispute Automation](#unique_25) [page ] 29 procedure.

A worklist is created. The worklist is created as a job. For more information on executing this job, see the [Schedule Jobs for Collections Automation](#unique_38) [page ] 46 topic.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
|  | Access the SAP Fiori App | Open Process Worklist in Collections and Dispute Automation (F8832). | The list report displays. |  |
|  | Select Customer | Choose Go.All business partners on the current worklist are displayed on the Open tab.Choose Start Activity for the worklist entry for a business partner to process. For example:Business Partner: S33100251 | The Process Accounts in Collections and Dispute Automation app is displayed. |  |

#### Create Promise to Pay

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You create a promise to pay for open invoices when the customer promises to pay on the invoice. The created promise to pay records the amounts and date promised. The system automatically tracks and updates the state of the promise to pay as kept or broken using the integration between SAP Collections and Dispute Automation and SAP Accounts Receivable (SAP FI-AR).

Prerequisite

An open Financial Accounting (FI) customer invoice exists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Process Accounts in Collections and Dispute Automation (F8607). |  |  |
| 3 | Select | Make the following entries and choose Go:Business Partner: For example, S33100251 | A Business Partners row is displayed. |  |
| 4 | Select Customer | Select the desired Business Partner row and choose Details (>):Business Partner: For example, S33100251 | The business partner details view is displayed with a list of invoices showing outstanding amount for the invoice, total outstanding amount for all invoices, and other information. |  |
| 5 | Select Invoice | Select an open invoice from the Invoices tab. | An invoice is selected. |  |
| 6 | Create Resubmission | Choose Create Promise to Pay. | The Promise to pay Created dialog box is displayed. |  |
| 7 | Navigate | Choose Navigate. | The new promise to pay opens in the Manage Promises to Pay app. |  |
| 8 | Enter and Save Promise to pay data | Make the following entries and choose Create:Promised For Date: <Actual Date + 2 days>Notes: OptionalAttachment: Optional | The promise to pay for the customer is created.The created promise to pay now displays on the Promises To Pay tab on the Process Accounts view. |  |

#### Create Task

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a task. In your role as a collections specialist, you create a task to record operational work in Collections and Dispute Automation when neither a promise to pay nor a dispute applies, but an action is still required. When creating a task, you can choose to exclude the customer from the worklist until the task’s due date is reached.

Prerequisite

An open Financial Accounting (FI) customer invoice exists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Process Accounts in Collections and Dispute Automation (F8607). |  |  |
| 3 | Select | Make the following entries and choose Go:Business Partner: For example, S33100251 | A Business Partners row is displayed. |  |
| 4 | Select Customer | Select the desired Business Partner row and choose Details (>):Business Partner: For example, S33100251 | The business partner details view is displayed with a list of invoices showing outstanding amount for the invoice, total outstanding amount for all invoices, and other information. |  |
| 5 | Select Invoice | Select an open invoice from the Invoices tab. | An invoice is selected. |  |
| 6 | Create | Choose Create Task. | The Task Created dialog box is displayed. |  |
| 7 | Navigate | Choose Navigate. | The new task opens in the Manage Tasks app. |  |
| 8 | Enter and Save Task Data | Make the following entries and choose Create:Task Due Date: <Actual Date + 2 days>Task Reason: Select a reason from the dropdown list, for example, Clarify OpenBalanceNotes: OptionalAttachment: Optional | The task for the customer is created.The created task now displays on the Tasks tab on the Process Accounts view. |  |

#### Create Dispute

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a dispute.

Prerequisite

An open Financial Accounting (FI) customer invoice exists.

Procedure - SAP Fiori

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant |  |  |
| 2 | Access the SAP Fiori App | Open Process Accounts in Collections and Dispute Automation (F8607). |  |  |
| 3 | Select | Make the following entries and choose Go:Business Partner: For example, S33 100251 | A Business Partners row is displayed. |  |
| 4 | Select Customer | Select the desired Business Partner row and choose Details (>):Business Partner: For example, S33 100251 | The business partner details view is displayed with a list of invoices showing outstanding amount for the invoice, total outstanding amount for all invoices, and other information. |  |
| 5 | Select Invoice | Select an open invoice from the Invoices tab. | An invoice is selected. |  |
| 6 | Create Dispute | Choose Create Dispute. | The Dispute Created dialog box is displayed. |  |
| 7 | Navigate | Choose Navigate. | The new dispute opens in the Manage Disputes app. |  |
| 8 | Create | Select the receivables item in the result list and choose Create Dispute Action. | The Dispute Created dialog box is displayed. |  |
| 9 | Navigate | Choose Navigate. | The new dispute opens in the Manage Disputes app. |  |
| 10 | Save | Choose Create to save the dispute. |  |  |

#### Create Activity

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity you document results of collection activity. Additionally, a default activity note is prepopulated with details of any promises-to-pay, tasks, and disputes created during the activity. You can add additional text into the note and then the text saves with the activity and is available in the Activities tab.

Prerequisite

A worklist is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad an Accounts Receivable Accountant |  |  |
| 2 | Access the SAP Fiori App | Open Process Accounts in Collections and Dispute Automation (F8607). |  |  |
| 3 | Select | Make the following entries and choose Go:Business Partner: For example, S33100251 | A Business Partners row is displayed. |  |
| 4 | Select Customer | Select the desired Business Partner row and choose Details (>):Business Partner: For example, S33100251 | The business partner details view is displayed with a list of invoices showing outstanding amount for the invoice, total outstanding amount for all invoices, and other information. |  |
| 5 | Create Activity | Choose the message An Activity is unfinalized. Click here to finalize it. | The activity opens in the Manage Activities in Collections and Dispute Automation (F8610) app. |  |
| 6 | Maintain Collections Activity | Make the following entries and choose Create:Activity Direction: Outbound CallActivity Results: Select a result from the dropdown list, for example, Reached - Successful.Activity Type: Select a result from the dropdown list, for example, Call.Notes: OptionalAttachment: Optional | The activity for the customer is created.The created activity now displays on the Activities tab on the Process Accounts view. |  |

### Schedule Background Jobs

#### Schedule Jobs for Collections Automation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run a background job to trigger generation and refresh of the Collections Worklist on a defined schedule.

From the same app you can also run the following jobs on demand:

- /DCO/BUILD_REC_ITEM
- /DCO/CALC_PAYMENT_BEHAVIOR
- /DCO/ADJUST_MD_COMP_CODE
- /DCO/ADJUST_MD_GENERAL
- /DCO/ADJUST_MD_SEGMENT
- /DCO/COPY_BRF_APPLICATION
- /DCO/DELETE_RBL_PYBL_ITEM
- /DCO/DELETE_TASKS
- /DCO/WORKLIST_ITEM_DELETE
- /DCO/P2P_JUDGE

Prerequisite

There are business partners that fulfill the conditions defined in the prioritization rule(s).

Procedure

| Test Step # | Test Step Name | Instructions | Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Jobs for Collections and Dispute Automation (F8376). |  |  |
| 3 | Create | Choose Create. | The New Job: Build Receivable Items view is displayed. |  |
| 4 | Job Template | Make the following entries and choose Step 2:Job Template: Create WorklistJob Name: Create WorklistNote If you can't select the job template, you may need to remove the default value first. |  |  |
| 5 | Default Values | Keep the default values and choose Step 3. |  |  |
| 6 | Schedule | Make the following entries and choose Schedule:Collections Segment: <collections segment that you want to run the job for>Test Run: Deselected |  |  |
| 7 | Check Log | The job's initial status is In Progress. To refresh the status, choose Go.When the Status changes to Finished, you can choose the button for that job in the Log column to review the job details. |  |  |

#### Schedule Jobs for Dispute Resolution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run a background job to trigger the escalation process for disputes to be escalated according to the BRF+ rules (see preliminary steps).

From the same app you can also run the following jobs on demand:

- /DCO/BUILD_REC_ITEM
- /DCO/DISPUTE_COPY_BRF_APPL
- /DCO/DELETE_RBL_PYBL_ITEM

Prerequisite

There are disputes that fulfill the conditions for escalation according to your BRF+ rules (see Preliminary Steps)

Procedure

| Test Step # | Test Step Name | Instructions | Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Jobs for Dispute Resolution in Collections and Dispute Automation (F8713). |  |  |
| 3 | Create | Choose Create. | The New Job: Escalate Disputes view is displayed. |  |
| 4 | Job Template | Make the following entries and choose Step 2:Job Template: Escalate DisputesJob Name: Escalate DisputesNote You may need to remove the default Job Template value first if you can’t select the proper job template. |  |  |
| 5 | Default Values | Keep the default values and choose Step 3. |  |  |
| 6 | Schedule | Enter the Debt Collections Company Code that you want to run the job for and choose Schedule. |  |  |
| 7 | Check Log | The job's initial status is In Progress. To refresh the status, choose Go.When the Status changes to Finished, you can choose the button for that job in the Log column to review the job details. |  |  |

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
- related-to :: [[03-financial-accounting-and-close/collections-and-dispute-management-bfc-ae-test-script-1264]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7MA_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 80,492 chars in the whole document
