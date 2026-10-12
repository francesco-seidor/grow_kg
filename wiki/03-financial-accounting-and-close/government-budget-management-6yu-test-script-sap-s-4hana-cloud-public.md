---
id: 03-financial-accounting-and-close/government-budget-management-6yu-test-script-sap-s-4hana-cloud-public
title: "Government Budget Management (6YU) - Test Script, SAP S/4HANA Cloud Public Edition (6YU_S4CLD2608_BPD_EN_XX)"
description: "Test script for SAP scope item 6YU Government Budget Management (S/4HANA Cloud Public Edition 2608): prerequisites and Fiori steps for budgeting, RIB, AVC."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/government-budget-planning-and-management]
aliases: [6YU_S4CLD2608_BPD_EN_XX]
keywords: [Government Budget Planning and Budget Management, government budget management, budget upload, budget supplements, budget transfers, budget release, budget approval workflow, revenues increasing the budget, availability control, avc exceptions]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6YU_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1199
topic: 03-financial-accounting-and-close/government-budget-planning-and-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Government Budget Management (6YU) - Test Script, SAP S/4HANA Cloud Public Edition (6YU_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6YU_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Government Budget Planning and Budget Management** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Government Budget Management (6YU)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Government Budget Management (6YU) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232841769)

[1.1 Budget 3](#_Toc232841770)

[1.2 Availability Control 4](#_Toc232841771)

[1.3 Situation Handling and Responsibility Management (31N, 1NJ) 4](#_Toc232841772)

[2 Prerequisites 5](#_Toc232841773)

[2.1 System Access 5](#_Toc232841774)

[2.2 Roles 5](#_Toc232841775)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232841776)

[2.4 Additional Manual Configuration 8](#_Toc232841777)

[2.5 Business Conditions 8](#_Toc232841778)

[2.6 Preliminary Steps 8](#_Toc232841779)

[2.6.1 Check Assigned RIB Profile 8](#_Toc232841780)

[2.6.2 Check Assigned AVC Profile 11](#_Toc232841781)

[2.6.3 Maintain Situation Type for Budget Threshold Exceeded 14](#_Toc232841782)

[2.6.4 Define the Team Who Is to Monitor the Budget Consumption and Receive Notifications 15](#_Toc232841783)

[3 Overview Table 17](#_Toc232841784)

[4 Test Procedures 19](#_Toc232841785)

[4.1 Upload Budget 19](#_Toc232841786)

[4.2 Create Budget Supplement Document 20](#_Toc232841787)

[4.3 Create Budget Supplement Document for Project/WBS Element (optional) 23](#_Toc232841788)

[4.4 Create Budget Transfer Document 25](#_Toc232841789)

[4.5 Release Budget 27](#_Toc232841790)

[4.6 Approve Budget via Workflow 29](#_Toc232841791)

[4.6.1 Define the Budget Workflow 29](#_Toc232841792)

[4.6.2 Create Original Budget Document with Approval 30](#_Toc232841793)

[4.7 Revenues Increasing the Budget (RIB) 32](#_Toc232841794)

[4.7.1 Define RIB Check Level Using Global Hierarchies 32](#_Toc232841795)

[4.7.2 Create RIB Rules 33](#_Toc232841796)

[4.7.3 Create Revenue Posting (Actuals) 35](#_Toc232841797)

[4.7.4 Start RIB Run 37](#_Toc232841798)

[4.8 Display Budget Document 39](#_Toc232841799)

[4.9 Check Budget Availability 40](#_Toc232841800)

[4.10 Define AVC Exception 43](#_Toc232841801)

[4.11 Automatic Account Assignment Distribution 46](#_Toc232841802)

[4.12 Periodic Commitment Adjustments 49](#_Toc232841803)

[4.13 Residual Budget Processing 50](#_Toc232841804)

[4.14 Budget Consumption Dashboard 52](#_Toc232841805)

## Purpose

Overview

Budgetary accounting is an accounting method for recording financial resources that are limited by a governing agency, authority, or by law. It places emphasis on accountability and control of budgetary resources instead of on profitability. The budget is a legal compliance standard against which the operations for funds are evaluated.

This process showcases the budgeted master data objects and the relationship to general ledger accounts and controlling objects. The approved budget is uploaded using the defined master data. Budget transfers are executed throughout the year as business is transacted and budget is consumed. In this fully integrated solution, all budget-relevant financial and commitment postings automatically check for available budget and communicate the status (success, warning, or error) according to the tolerance settings. Users are assured both an exact control of financial resources and accuracy in managerial and statutory reporting.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

### Budget

Budgetary accounting is an accounting method used to record financial resources that are limited by a government agency, authority or by law. The focus here is on accountability and control of budgetary resources, as opposed to profitability. The budget is a legal estimate of income and expenditure for a set period of time against which the operations of funds are evaluated.

This document contains a description of the following procedures:

- How to upload and manage budget transactional data for your SAP S/4HANA Cloud Public Edition system. A budget upload record, which you create as described here, can be used to process a budget upload.
- How to manage budget supplements and transfers for your SAP S/4HANA Cloud Public Edition system. A budget supplement or transfer record, which you create as described here, can be used to control budget execution using an active availability control.
- How to display a budget transfer document.
- How budgets can be released.
- How budget documents can be approved
- How to increase expenditure budgets based on revenues
- How rules can be set up to distribute account assignments, such as funds or the functional area automatically when budget consumptions are posted.
- How open commitments are closed or transferred to a new budget period.
- How AVC exceptions can be set up.

The description includes those data segments that are relevant to the SAP S/4HANA Cloud Public Edition application. Fields that are not included in the scope of the SAP S/4HANA Cloud Public Edition content as delivered by SAP Best Practices are not described in this document.

### Availability Control

The availability control with [Budgeting](https://help.sap.com/saphelp_globext607_10/helpdata/en/4f/19f53b5415f249e10000000a11402f/content.htm) is a flexible tool that you can use to check consumable budget against consumed amounts (commitment or actual postings) within a budget execution process. If budget consumption reaches one of the tolerance limits specified in Customizing, this can trigger system activities, such as those that prevent additional postings from being made. Availability control checks the posting procedures and the posting data in the integrated components (FI, CO, MM and so on).

### Situation Handling and Responsibility Management (31N, 1NJ)

Situation handling recognizes business situations by evaluating conditions (rules) on the basis of business facts. In this document, a business situation occurs in a SAP S/4HANA Cloud Public Edition system when a KPI (such as budget) passes a threshold.

For more information about situation handling, see the scope item 31N (Situation Handling) and 1NJ (Responsibility Management).

## Prerequisites

### System Access

The test should be conducted in the following system:

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

For more information, see How to Create a Business Role for a Key User in the [product assistance](https://help.sap.com/viewer/a630d57fc5004c6383e7a81efee7a8bb/latest/en-US/8fa28e0107984d42a99b9eea67856cea.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Budget Specialist - Funds Management | SAP_BR_BUDGET_SPECIALIST | Budgeting | SAP_BR_BUDGET_SPECIALIST |  |
| Budget Responsible - Funds Management | SAP_BR_BUDGET_RESPONSIBLE | Budgeting | SAP_BR_BUDGET_RESPONSIBLE |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Employee | SAP_BR_EMPLOYEE | Self Services / Self Services / Employee Overview Space | SAP_BR_EMPLOYEE / SAP_CA_SPT_EMPLOYEE_CROSS_PC / SAP_EAM_SPT_EMPLOYEE_PC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, according to the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | <company code, for example, 1710> |  | Replace 1710 with your company code xxxx. See also the note below in the cost center section. |
| Fund | <fund, for example, G1100> | Mandatory |  |
| Functional Area | <functional area, for example, 1000> | Optional for budgetingMandatory for postings |  |
| Budget Period | <current year> | Mandatory |  |
| Cost Center | <cost center, for example, 17101202 and 17101801> | Mandatory | Replace with the cost center in your company code, such as xxxx1202 and xxxx1801 |
| Account Number | <account number, for example, 61100000 and 41090000> | Mandatory |  |
| Grant | NRG |  | Delivered |
| WBS Element |  | Optional | To be created |
| Profit Center |  | Optional | Derived automatically |

You can find general information about creating master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNH | Create Profit Center - MDS |
| 47C | Create Fund - MDS |
| 47D | Create Budget Period - MDS |
| 47E | Create Functional Area - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/c25b58c9c21993254dd05c2c69d34d74)

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| J59 - Accounts Receivable | The steps executed by the accounts receivable accountant to create customer invoices used in Revenues Increasing the Budget (RIB). |
| J60 - Accounts Payable | The steps executed by the accounts payable to consume budget using supplier invoices. |
| BNX - Consumable Purchasing | The steps executed by the purchaser to consume budget using purchase orders. |

### Preliminary Steps

#### Check Assigned RIB Profile

Purpose

In this activity, you check that the budget account hierarchy has been maintained correctly in the system for the RIB profile S_PSM2.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad appears. |  |
| 2 | Open the Manage Your Solution (F1241) app | Frontend Fiori App:Open Manage Your Solution (F1241). | The Manage Your Solution (F1241)screen appears. |  |
| 3 | Open the Configure Your Solution app | Frontend Fiori App:Open the Configure Your Solution app (F2962). | The Configure Your Solution screen appears. |  |
| 4 | Configure RIB Profile | Search with the following criteria:Application Area: Public SectorSub Application Area: Budget ExecutionClick on the configuration item: Public Sector Budget Management and locate the Define RIB Profile configuration step.Click Configure in the configuration step: Define RIB Profile. | The configuration: Define RIB Profile appears. |  |
| 5 | Configure Journal Field Dependencies | Select the RIB profile ID S_PSM2 and open the sub tree: Journal Field Dependencies | The Journal Field Dependencies information for the S_PSM2 RIB profile opens. |  |
| 6 | Check Hierarchy for Budget Account | Check the following:For BDGT_ACCOU Budget Account, check that the RIB relationship type is H Hierarchy and the hierarchy ID is H115/YCOA/SPSMBA.For PS_POSID WBS Element, check that the RIB relationship type is N Not Relevant.For RCNTR Cost Center, check that the RIB relationship type is O One to One.For RFAREA Functional Area, check that the RIB relationship type is N Not Relevant.For RFUND Fund, check that the RIB relationship type is O One to One. | The hierarchy information is maintained for BDGT_ACCOU Budget Account.The RIB relationship type is not found in the hierarchy for the others. |  |
| 7 | Configure Assign RIB Profile to Company Code and Fiscal year | Exit the Define RIB Rules configuration step.Click on Configure for the configuration step: Assign RIB Profile to Company Code and Fiscal Year | The Assign RIB Profile to Company Code and Fiscal Year configuration opens. |  |
| 8 | Check RIB Profile Assignment | Check the following:CoCd: <company code, for example, 1710>Fiscal Year From: <current year>Scenario for Budgeting: PSM Budget ManagementRIB Profile ID: S_PSM2 | The specified assignments are found here. |  |
| 9 | Log out | Log out from the SAP Fiori session. | The SAP Fiori launchpad appears. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad appears. |  |
| 2 | Configure RIB Profile | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define RIB ProfileChoose Open Documentation for the line item found to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define RIB Profile screen appears. |  |
| 3 | Configure Journal Field Dependencies | Select the RIB profile ID S_PSM2 and open the sub tree: Journal Field Dependencies | The Journal Field Dependencies information for S_PSM2 RIB Profile opens. |  |
| 4 | Check Hierarchy for Budget Account | Check the following:For BDGT_ACCOU Budget Account, check that the RIB relationship type is H Hierarchy and the hierarchy ID is H115/YCOA/SPSMBA.For PS_POSID WBS Element, check that the RIB relationship type is N Not Relevant.For RCNTR Cost Center, check that the RIB relationship type is O One to One.For RFAREA Functional Area, check that the RIB relationship type is N Not Relevant.for RFUND Fund, check that the RIB relationship type is O One to One. | The hierarchy information is maintained for BDGT_ACCOU Budget Account.The RIB relationship type is not found in the hierarchy for the others. |  |
| 5 | Configure Assign RIB Profile to Company Code and Fiscal year | Exit the Define RIB Rules configuration step.Click on Configure in the configuration step: Assign RIB Profile to Company Code and Fiscal Year | Assign RIB Profile to Company Code and Fiscal Year configuration opens. |  |
| 6 | Check RIB Profile Assignment | Check the following:CoCd: <company code, for example, 1710>Fiscal Year From: <current year>Scenario for Budgeting: PSM Budget ManagementRIB Profile ID: S_PSM2 | The specified assignments are found here. |  |
| 7 | Log out | Log out from the SAP Fiori session. | The SAP Fiori launchpad appears. |  |

#### Check Assigned AVC Profile

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check whether the AVC profile is correctly assigned to your company code / budget consumption year and whether notifications are active.

Procedure

Choose one of the following options, according to your configuration environment for SAP S/4HANA Cloud Public Edition:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution(F1241). |  |  |
| 3 | Go to Configure Your Solution | Choose Configure Your SolutionConfigure Your Solution. |  |  |
| 4 | Go to Define Availability Control Profile | On the Configure Your SolutionConfigure Your Solution screen, search for the following configuration step: Define Availability Control Profile. Choose Go.In the search result, select the configuration activity and go to the next screen.On the Configure Your Solution – Define Availability Control Profile screen, go to the configuration step Define Availability Control Profile and choose Configure. | The Define Availability Control Profile screen appears. |  |
| 5 | Check AVC profile | Choose Profile: S_PSM1Click on the folder AVC Profiles.Check whether the notification is active: field % increment for further Notification must contain a percentage.This entry should exist by default. If not enter 5% and Save.NoteIn the folder Journal Field Dependencies the following fields are predefined:Field Name in Journal: Budget Period, Cost Center and FundAVC Relation Type: One to one for the budget period and fund hierarchy for the cost centerClick back twice. | Notification is active. |  |
| 6 | Go to Assign AVC Profile to Company Code/Budget Consumption Year | On the Configure Your Solution screen, search for the following configuration step: Assign AVC Profile to Company Code/Budget Consumption Year. Choose Go.In the search result, select the configuration activity and go to the next screen.On the Configure Your Solution – Assign AVC Profile to Company Code/Budget Consumption Year screen, go to the configuration step Assign AVC Profile to Company Code/Budget Consumption Year and choose Configure. | The <Title of configuration step (SSCUI)> screen appears. |  |
| 7 | Check Profile Assignment | Step Name: Assign AVC Profile to Company Code/Budget Consumption YearClick on configure:Additionally, (if no corresponding entry exists) enterCompany Code: 1710From Year of Budget Consumption: <earlier or the same as the current year>Profile: S_PSM1Save. | All assignments have been made. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Define Availability Control Profile | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Availability Control Profile.Choose Open Documentation for the line item found to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Availability Control Profile screen appears. |  |
| 3 | Check AVC profile | Choose Profile: S_PSM1Click on the folder AVC Profiles.Check whether the notification is active: the field % increment for further Notification must contain a percentage.This entry should exist by default. If not enter 5% and Save.NoteIn the folder Journal Field Dependencies the following fields are predefined:Field Name in Journal: Budget Period, Cost Center and FundAVC Relation Type: One to One for the budget period and fund Hierarchy for the cost center.Click back twice. | Notification is active. |  |
| 4 | Assign AVC Profile to Company Code/Budget Consumption Year | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign AVC Profile to Company Code/Budget Consumption Year.Choose Open Documentation for the line item found to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign AVC Profile to Company Code/Budget Consumption Year screen appears. |  |
| 5 | Check Profile Assignment | Step Name: Assign AVC Profile to Company Code/Budget Consumption YearClick on Configure:Additionally, (if no corresponding entry exists) enterCompany Code: 1710From Year of Budget Consumption : <earlier or the same as the current year>Profile: S_PSM1Save . | All assignments have been made. |  |

#### Maintain Situation Type for Budget Threshold Exceeded

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step you use the situation type to define when notifications are triggered if a specific budget threshold is exceeded.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Business Process Specialist.. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Situation Types (F2947). | The Manage Situation Types view is displayed. |  |
| 3 | Select the Template to Copy | In the Standard section, enter the ID PSM_BM_BudgetThresholdExceeded and choose Go.Select the latest version of PSM_BM_BudgetThresholdExceeded, and then choose Copy. | The Situation Type screen appears. |  |
| 4 | Maintain the Situation Type | Make the following entries:Facet Admin InformationID: Z_BUDGET_THRESHOLDName: Budget Threshold ExceededFacet Situation DisplayShort Description: Budget Threshold ExceededDetails:Notification :Resend Notifications: YESFacet ConditionsMaintain the values for the corresponding attributes/ filters to configure the conditions and use this function. In Processing Order 1:The column Set to status is openSend notification is yesSection Conditions (enter the following if no default is shown):Current Budget Threshold: >70Previous Budget Threshold: <=70In Processing Order 2:Column Set to status is openSend notification is yesSection Conditions (enter the following if no default is shown):Current Budget Threshold: >70Previous Budget Threshold: >70For Processing Order 3 and 4 please check that in the column send notification the values are no.Facet RecipientsResponsibility by teams: Choose + and maintain the Budget Management Availability Control team category created using the Manage Teams and Responsibilities (F2412) app. Maintain the value Monitor Budget in the field Member Functions if necessary.No responsibility rules need to be maintained. Choose Create. On the dialog box (do you want to enable the situation type?) click Yes to confirm the dialog box. | The situation type is enabled.A notification is triggered if 70% of the budget consumption is exceeded.The notification text is defaulted. The user can change the notification text.Note: the notification text (see preview) refers to all budget management-relevant account assignments, but the control of available budget only takes the fund into account. The text can be adjusted. |  |

#### Define the Team Who Is to Monitor the Budget Consumption and Receive Notifications

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define a team who is to receive notifications if a budget consumption threshold is reached.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Business Process Specialist. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open the Manage Teams and Responsibilities (F2412) Fiori app. |  |  |
| 3 | Change Team | Search for the category: BMAVCClick create. On the General Information tab:Name: Team_<n>_PSM BMDescription: Team_<n>_PSM BMGlobal ID: <any>Type: S_PSMBMAVCStatus: enabledIn Responsibility Definitions:Control Object for Fund: G2200Control Object Budget Period: <current year>Control Object Cost Center : <OSPSM12>In Team Member:Add your personalized user that is linked to the following roles:SAP_BR_EMPLOYEE and SAP_BR_BUDGET_SPECIALIST.Ensure that the function Monitor Budget is set.Save. | Your personalized user is part of the team who is to receive notifications. |  |

## Overview Table

This scope item consists of several process steps.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Upload Budget](#unique_16) [page ] 19 | Budget Specialist - Funds Management | Import Financial Plan Data (F1711) |  |
| [Create Budget Supplement Document](#unique_17) [page ] 20 | Budget Specialist - Funds Management | Manage Budget Documents - PSM (F4173) |  |
| [Create Budget Supplement Document for Project/WBS Element (optional)](#unique_18) [page ] 23 | Budget Specialist - Funds Management | Manage Budget Documents - PSM (F4173) |  |
| [Create Budget Transfer Document](#unique_19) [page ] 25 | Budget Specialist - Funds Management | Manage Budget Documents - PSM (F4173) |  |
| [Release Budget](#unique_20) [page ] 27 | Budget Specialist - Funds Management | Manage Budget Documents - PSM (F4173) |  |
| [Define the Budget Workflow](#unique_21) [page ] 29 | Configuration Expert - Business Process Configuration | Manage Workflows for Budget Documents (F7308) |  |
| [Create Original Budget Document with Approval](#unique_22) [page ] 30 | Budget Responsible - Funds Management | My Inbox (F0862) |  |
| [Define RIB Check Level Using Global Hierarchies](#unique_23) [page ] 32 | Budget Specialist - Funds Management | Manage Global Hierarchies (F8220) |  |
| [Create RIB Rules](#unique_24) [page ] 33 | Budget Specialist - Funds Management | Manage RIB Rules (F6621) |  |
| [Create Revenue Posting (Actuals)](#unique_25) [page ] 35 | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | Create Outgoing Invoices (FB70) |  |
| [Start RIB Run](#unique_26) [page ] 37 | Budget Specialist - Funds Management | Application Jobs - Public Sector (F4519) |  |
| [Display Budget Document](#unique_27) [page ] 39 | Budget Specialist - Funds Management | Manage Budget Documents - PSM (F4173) |  |
| [Check Budget Availability](#unique_28) [page ] 40 | Budget Specialist - Funds Management | Budget AVC Overview (F2163) |  |
| [Define AVC Exception](#unique_29) [page ] 43 | Budget Specialist - Funds Management | Manage AVC Exceptions (F5372) |  |
| [Automatic Account Assignment Distribution](#unique_30) [page ] 46 | Budget Specialist - Funds Management | Manage Automatic Account Distribution Rule (F5600) |  |
| [Periodic Commitment Adjustments](#unique_31) [page ] 49 | Budget Specialist - Funds Management | Periodic Commitment Adjustments (F4345) |  |
| [Residual Budget Processing](#unique_32) [page ] 50 | Budget Specialist - Funds Management | Application Jobs - Public Sector (F4519) |  |
| [Budget Consumption Dashboard](#unique_33) [page ] 52 | Budget Specialist - Funds Management | Budget Consumption Dashboard (F6088) |  |

## Test Procedures

This section describes procedures that apply to each process step associated with this scope item. You can also use these procedures to test master data creation.

### Upload Budget

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Implementation Type

The following section is ONLY relevant for SAP S/4HANA Cloud Public Edition.

Procedure: SAP Fiori

Access the activity as follows:

Use the attached Excel sheet for this scope item called BUDGETUPLOAD_XX.csv (section Accelerators/Configuration).. Edit the file and adjust the following data:

- Column RYEAR: Replace ???? with the current fiscal year.
- Column RBUDGET_PD: Replace ???? with the current fiscal year.
- Column RBUKRS: Replace ???? with the company code you are testing (such as 1010 for Germany).
- Column RCNTR: Replace ???? with the company code you are testing (such as 1010 for Germany).
- Column RKCUR: Replace ??? with the global currency used in our test system (such as EUR for Germany).

Save your file.

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the budget specialist. | The SAP Fiori launchpad appears. |  |
| 2 | Open "Import Financial Plan Data" | Frontend Fiori App:Open Import Financial Plan Data (F1711). | The Import Financial Plan Data (F1711) screen appears. |  |
| 3 | Browse a CSV File | On the Import Financial Plan Data screen, choose Browse .csv Files and select the file that includes your budget (see above). | The selected data is proposed in the Source File field. |  |
| 4 | Import Data | Click on Test Import Source File and identify potential errors by clicking on Show Details.Click Import Source File. | The budget data from the file has been imported successfully. |  |
| 5 | Check Financial Plan Data | Click on Check Financial Plan Data. | The report for PlanAmountInGlobalCurrency (Plan Amount in Global Crcy) appears with the correct values. |  |

|  |
| --- |
| Note Please note that after you've imported budget, there are no budget documents in the “Manage Budget Documents" app. You can generate budget documents in the "Application Jobs --Public Sector" app using the job template “Automatic Budget Document Header Creation.” |

### Create Budget Supplement Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Implementation Type

The following section is ONLY relevant for SAP S/4HANA Cloud Public Edition.

Procedure: SAP Fiori

Access the activity as follows:

Prerequisities

You have executed the master data script Create Fund Master Data and the scope item procedure Upload Budget.

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the budget specialist. | The SAP Fiori launchpad appears. |  |
| 2 | Open Manage Budget Transfer | Frontend Fiori App:Open Manage Budget Documents - PSM (F4173). | The Budget Documents screen appears. |  |
| 3 | Create Budget Supplement | On the Budget Document screen, choose Create->Supplement).Copy or reversal: If you want to copy or reverse a budget document, select the existing document from the Budget Documents list and choose Copy (= Copy Budget Document) or Reverse (= Reverse Budget Document).Note You can only execute and choose Delete for draft budget document headers and/or items (these are documents that have not been saved to the database). | The Budget Document Header screen opens in the editing mode. |  |
| 4 | Enter General Information | The system derives field values for the fields described based on your entries, (display mode) However, these are only mentioned here for the sake of com-pleteness.Make the following entries manually:The system derives field values for the fields described based on your entries, (display mode) However, these are only mentioned here for the sake of completeness.Fiscal Year: (Display Mode) (Calculated based on the posting data and the fiscal year variant for the controlling area)Document Number: (Display Mode) (Number is derived from the system)Plan Category: Choose from the dropdown list <Budget03>Document Type: Choose from the dropdown list <Budget Document (S_BT)>Document Header Text: <Budget Supplement>Document Date: <Choose the current date from calender>Posting Date: <Choose the current date from calender> | The general information is entered in the Budget Document Header. |  |
| 5 | Enter a Budget Item for Budget Account (Released Budget) | In the Budget line item section, make the following entries manually (some values are optional):Company Code: <company code, for example, 1710>Fund: <fund, for example, G2200>Budget Period: <current year>Cost Center: <cost center, for example, 17101202>Account Number: 61100000WBS Element: (Optional) <Enter a specific ID>Grant: <NRG>Amount in Glob. Crcy: <$5000.00>Budget Type: <Released Budget (S_SCAT1)>Copy or reversal: Overwrite the entries from the copied document. Retain the entries in a reversal document. The system automatically defines the reversal amount value. | The Budget Item screen appears in the editing mode. |  |
| 6 | Enter a Budget Item for Budget Account (Released Budget) | On the Budget Document item section, make the following entries manually (some values are optional):Company Code: <company code, for example, 1710>Fund: <fund, for example, G2200>Budget Period: <current year>Cost Center: <cost center, for example, 17101202>Account Number: 61100000Amount in Glob. Crcy: <$5000.00>Budget Type: <Released Budget (S_SCAT1)>Copy or reversal: Overwrite the entries from the copied document. Retain the entries in a reversal document. The system automatically defines the reversal amount value. | The Budget Document Item screen appears in the editing mode. |  |
| 7 | Enter a Budget Item for Budget Account (Unreleased Budget) | In the Budget Document item section, make the following entries manually (some values are optional):Company Code: <company code, for example, 1710>Fund: <fund, for example, G2200>Budget Period: <current year>Cost Center: <cost center, for example, 17101202>Account Number: 61100000Amount in Glob. Crcy: <$1000.00>Budget Type: <Unreleased Budget (S_SCAT2)>Copy or reversal: Overwrite the entries from the copied document. Retain the entries in a reversal document. The system automatically defines the reversal amount value. | The Budget Document Item screen appears in the editing mode. |  |
| 8 | Save the Budget Transfer Document | Click on Create. | A system message appears informing you that the budget document (including the budget items) has been saved. |  |

### Create Budget Supplement Document for Project/WBS Element (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Implementation Type

The following section is ONLY relevant for SAP S/4HANA Cloud Public Edition.

Procedure: SAP Fiori

Access the activity as follows:

Prerequisities

You have executed the master data script Create Fund Master Data and the scope item procedure Upload Budget.

You have created a project/WBS element, for example with the corresponding instructions in the scope item Project Control – Finance(ONT). Please enter a fund and a responsible cost center in the project.

Now you enter budget for the project/WBS element in this step. This is needed to post costs to the WBS element.

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the Budget Specialist - Funds Management. | The SAP Fiori launchpad appears. |  |
| 2 | Open Manage Budget Transfer | Frontend Fiori App:Open Manage Budget Documents - PSM (F4173). | The Budget Documents screen appears. |  |
| 3 | Create Budget Supplement | On the Budget Document screen, choose Create > Budget Supplement).Copy or reversal: If you want to copy or reverse a budget document, select the existing document from the Budget Documents list and choose Copy (= Copy Budget Document) or Reverse (= Reverse Budget Document).Note You can only execute and choose Delete for draft budget document headers and/or items (these are documents that have not been saved to the database). | The Budget Document Header screen opens in the editing mode. |  |
| 4 | Enter General Information | The system derives field values for the fields described based on your entries, (display mode) However, these are only mentioned here for the sake of completeness.Make the following entries manually:The system derives field values for the fields described based on your entries, (display mode) However, these are only mentioned here for the sake of completeness.Fiscal Year: (Display Mode) (Calculated based on the posting data and the fiscal year variant for the controlling area)Document Number: (Display Mode) (Number is derived from the system)Plan Category: Choose from the dropdown list <Budget03>Document Type: Choose from the dropdown list <Budget Transfer (S_BT)>Document Header Text: <Budget Supplement>Document Date: <Choose the current date from calender>Posting Date: <Choose the current date from calender> | The general information is entered in the Budget Document Header. |  |
| 5 | Enter a Budget Item for Budget Account (Released Budget) | In the Budget line item section, make the following entries manually (some values are optional):Company Code: <company code, for example, 1710>Fund: <fund entered in WBS element>Budget Period: <current year>Cost Center: <responsible cost center of the WBS element>Account Number: 61100000WBS Element: <WBS element>Grant: <NRG>Amount in Glob. Crcy: <$50000.00>Budget Type: <Released Budget (S_SCAT1)>Copy or reversal: Overwrite the entries from the copied document. Retain the entries in a reversal document. The system automatically defines the reversal amount value. | The Budget Item screen appears in the editing mode. |  |
| 6 | Save the Budget Transfer Document | Click on Create. | A system message appears informing you that the budget document (including the budget items) has been saved. |  |

### Create Budget Transfer Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Implementation Type

The following section is ONLY relevant for SAP S/4HANA Cloud Public Edition.

Procedure: SAP Fiori

Access the activity as follows:

Prerequisities

You have executed the master data script Create Fund Master Data and the scope item procedure Upload Budget.

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the budget specialist. | The SAP Fiori launchpad appears. |  |
| 2 | Open Manage Budget Transfer | Frontend Fiori App:Open Manage Budget Documents - PSM (F4173). | The Budget Documents screen appears. |  |
| 3 | Create Budget Transfer | On the Budget Documents screen, choose Create > Transfer.Copy or reversal: If you want to copy or reverse a budget transfer, select the existing document from the Budget Documents list and choose Copy (= Copy Budget Documents) or Reverse (= Reverse Budget Document).Delete: You can only execute and choose Delete for draft budget document headers and/or items (these are documents that have not been saved to the database). | The Budget Transfer Header screen opens in the editing mode. |  |
| 4 | Enter General Information | Based on your entries, field values for with the text (Display Mode) behind them are derived and only mentioned here for the sake of completenessMake the following entries manually:Fiscal Year: (Display Mode) (Calculated based on the posting data and the fiscal year variant for the controlling area)Document Number: (Display Mode) (Number is derived from the system)Plan Category: Choose from the dropdown list <Budget03>Document Type: Choose from the dropdown list <S_BT (Budget Document)>Document Header Text: <Budget Transfer>Document Date: <Choose the current date from calender>Posting Date: <Choose the current date from calender> | The general information is entered in the Budget Transfer Header. |  |
| 5 | Enter Budget Item for Sender Budget Account | In the Budget Sender item section, make the following entries manually (some values are optional):Company Code: <company code, for example, 1710>Fund: <fund, for example, G2200>Budget Period: <current year>Cost Center: cost center, for example, 17101202>Account Number: 61100000Amount in Glob. Crcy: <$5000.00>Budget Type: <S_SCAT1>Copy or reversal: Overwrite the entries from the copied document. Retain the entries in a reversal document. The system automatically sets the reversal amount value. | The Budget Transfer Item screen appears in the editing mode. |  |
| 6 | Enter Budget Item for Receiver Budget Account | Make the following entries manually (some values are optional):Company Code: <company code, for example, 1710>Fund: <fund, for example, G1190>Budget Period: <current year>Cost Center: <cost center, for example, 17101202>Account Number: <61100000>Amount in Glob. Crcy: <$5000.00>Budget Type: <S_SCAT1> | The Budget Transfer Item screen opens in the editing mode. |  |
| 7 | Save the Budget Transfer Document | Click on Create. | A system message appears informing you that the budget document (including the budget items) has been saved. |  |

### Release Budget

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Implementation Type

The following section is ONLY relevant for SAP S/4HANA Cloud Public Edition.

Procedure: SAP Fiori

Access the activity as follows:

Prerequisities

You have executed the master data script Create Fund Master Data and the scope item procedure Upload Budget. You need budget with the budget type <Unreleased Budget (S_CAT2)>.

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the budget specialist. | The SAP Fiori launchpad appears. |  |
| 2 | Open the Manage Budget Document app | Frontend Fiori App:Open Manage Budget Documents - PSM (F4173). | The Budget Documents screen appears. |  |
| 3 | Create Budget Release | On the Budget Documents screen, choose Create-> Release.Copy or reversal: If you want to copy or reverse a budget transfer, select the existing document from the Budget Documents list and choose Copy (= Copy Budget Documents) or Reverse (= Reverse Budget Document).Delete: You can only execute and choose Delete for draft budget document headers and/or items (these are documents that have not been saved to the database). | The Budget Document Header screen opens in the editing mode. |  |
| 4 | Enter General Information | Based on your entries, field values for fields described as (display mode) are derived and only mentioned here for the sake of completeness.Make the following entries manually:Fiscal Year: (Display Mode) (Calculated based on the posting data and the fiscal year variant for the controlling area)Document Number: (Display Mode) (Number is derived from the system)Plan Category: Choose from the dropdown list <Budget03>Document Type: Choose from the dropdown list <S_BT (Budget Document)>Document Header Text: <Budget Release>Document Date: <Choose the current date from calender>Posting Date: <Choose the current date from calender> | The general information is entered in the Budget Document Header. |  |
| 5 | Enter Budget Item for Sender (Unreleased) Budget Account | In the Budget Sender item section make the following entries manually (some values are optional):Company Code: <company code, for example, 1710>Fund: <fund, for example, G2200>Budget Period: <current year>Cost Center: <cost center, for example, 17101202>Account Number: 61100000Amount in Glob. Crcy: <$500.00>Budget Type: <Unreleased Budget (S_SCAT2)>Copy or reversal: Overwrite the entries from the copied document. Keep the entries in a reversal document. The system automatically sets the reversal amount value. | The Budget Document Item screen appears in the editing mode |  |
| 6 | Enter Budget Item for Receiver (Released) Budget Account | Make the following entries manually (some values are optional/most values are copied automatically from the sender line item):Company Code: <company code, for example, 1710>Fund: <fund, for example, G1190>Budget Period: <current year>Cost Center: <cost center, for example, 17101202>Account Number: <61100000>Amount in Glob. Crcy: <$500.00>Budget Type: <Released Budget (S_SCAT1)> | The Budget Document Item screen opens in the editing mode. |  |
| 7 | Save the Budget Transfer Document | Click on Create. | A system message appears informing you that the budget document (including the budget items) has been saved. |  |

### Approve Budget via Workflow

#### Define the Budget Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the user Configuration Expert - Business Process Configuration |  |  |
| 2 | Access the SAP Fiori App | Open Manage Workflows for Budget Documents(F7308). | The Manage Workflows for Budget Documents(F738) view appears showing the existing list of workflows. |  |
| 3 | Workflows | Choose Create | The dialog for the New Workflow appears |  |
| 4 | New Workflow | Enter the following data:Workflow Name: “New Workflow for Budget”Start Condition: Select “Receiver Expense Amount for Budget is greater than” from the dropdown in the first field and enter <10000> in the second fieldChoose Create in the Steps section | The new step dialog appears |  |
| 5 | New Step | Enter the following data:Header Section:Step Type: Approve Budget DocumentRecipient Section:Assignment By: RoleRole: User with role Budget ResponsibleChoose Create and then Save in the New Workflow dialog | A success message appears. The workflow is saved. |  |
| 6 | Activate Workflow | Choose Activate | The new workflow appears in the list of workflows with the status Active. |  |
| 7 | Change Workflow Order | Choose Define Order.The Define Order dialog appears.Select your Workflow and choose Move to move the selected workflow to the top.Choose Save . | Your workflow appears as the first workflow in the list with Order 1. |  |

#### Create Original Budget Document with Approval

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Implementation Type

The following section is ONLY relevant for SAP S/4HANA Cloud Public Edition.

Procedure: SAP Fiori

Access the activity as follows:

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the budget specialist. | The SAP Fiori launchpad appears. |  |
| 2 | Open Manage Budget Transfer | Frontend Fiori App:Open Manage Budget Documents - PSM(F4173). | The Budget Documents screen appears. |  |
| 3 | Create Budget Document | On the Budget Document screen, choose Create->Original .Note You can only execute and choose Delete for draft budget document headers and/or items (these are documents that have not been saved to the database). | The Budget Document Header screen opens in the editing mode. |  |
| 4 | Enter General Information | The system derives field values for the fields described based on your entries, (display mode) However, these are only mentioned here for the sake of completeness.Make the following entries manually:The system derives field values for the fields described based on your entries, (display mode) However, these are only mentioned here for the sake of completeness.Fiscal Year: (Display Mode) (Calculated based on the posting data and the fiscal year variant for the controlling area)Document Number: (Display Mode) (Number is derived from the system)Plan Category: Choose from the dropdown list <Budget03>Document Type: Choose from the dropdown list <Budget Document (S_BT)>Document Header Text: <Budget >Document Date: <Choose the current date from calender>Posting Date: <Choose the current date from calender> | The general information is entered in the Budget Document Header. |  |
| 5 | Enter a Budget Item for Budget Account (Released Budget) | In the Budget line item section, make the following entries manually (some values are optional):Company Code: <company code, for example, 1710>Fund: <fund, for example, G2200>Budget Period: <current year>Cost Center: <cost center, for example, 17101202>Account Number: 61100000WBS Element: (Optional) <Enter a specific ID>Grant: <NRG>Amount in Glob. Crcy: <$15000.00>Budget Type: <Released Budget (S_SCAT1)>Copy or reversal: Overwrite the entries from the copied document. Retain the entries in a reversal document. The system automatically defines the reversal amount value. | The Budget Item screen appears in the editing mode. |  |
| 6 | Save the Budget Transfer Document | Click on Create. | A system message appears informing you that the budget document (including the budget items) has been saved. The document status is “Waiting for Approval” |  |
| 7 | Log On | Log on to the SAP Fiori launchpad as the budget responsible. | The SAP Fiori launchpad appears. |  |
| 8 | Open My Inbox. | Frontend Fiori App:Open My Inbox(F0862) | The My Inbox(F0862) screen appears. |  |
| 9 | Select Workflow Item | The Budget Document appears on the left hand side of the screen under All Tasks.Click on the task | The details of the budget document appear on the right hand side of the screen |  |
| 10 | Approve the reservation | Choose Approve .Enter a Decision Note and choose Submit . | The budget document is approved and the workflow task disappears from the inbox. |  |

### Revenues Increasing the Budget (RIB)

#### Define RIB Check Level Using Global Hierarchies

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can define revenues increasing the budget check levels for various control objects using global hierarchies in the system.

Implementation Type

The following section is ONLY relevant for SAP S/4HANA Cloud Public Edition.

Procedure: SAP Fiori

Access the activity as follows:

Prerequisites

You have executed the preliminary step Check Budget Account Hierarchy for RIB Profile.

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as the Budget Specialist - Funds Management. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Global Hierarchies - Public Sector (F8220). | The Global Hierarchies view is displayed. |  |
| 3 | Apply filter for the type and hierarchy ID | In the filters, select the Budget Account Hierarchy type and the SPSMBA hierarchy ID and choose Go. | The budget account hierarchy SPSMBA is filtered. |  |
| 4 | Define the RIB check level for the budget account hierarchy SPSMBA | Click on Edit.In the nodes hierarchy for the budget account, expand SPSMBA; expand SPSMBA20 (Revenues) and click on SPSM41 (Revenues).Click on the RIB Check Level checkbox on the Change Node dialog box and click on OK. | The budget account hierarchy node SPSM41(Revenues) is marked as RIB Check Level. |  |
| 5 | Save and Activate | Click on Save.Click on Activate. |  |  |

#### Create RIB Rules

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create new RIB rules for a specified control object starting from a specified year for the RIB profile: See [Check Assigned RIB Profile](#unique_11) [page ] 8.

Implementation Type

The following section is ONLY relevant for SAP S/4HANA Cloud Public Edition.

Procedure: SAP Fiori

Access the activity as follows:

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the Budget Specialist - Funds Management. | The SAP Fiori launchpad appears. |  |
| 2 | Open the Manage RIB Rules (F6621) app | Front End Fiori App:Open Manage RIB Rules (F6621). | The RIB Rules screen appears. |  |
| 3 | Create RIB Rule | On the RIB Rules screen, choose Create.Copy: If you want to copy a RIB rule, select the existing rule from the RIB Rules list and choose Copy (= Copy RIB Rules).Delete: You can only execute and choose Delete for inactive RIB rules to which no open documents are associated. | The New Rule screen opens in the editing mode. |  |
| 4 | Enter General Information | Make the following entries manually:Valid from Fiscal Year: Choose from the drop-down list <current year>Company Code: Choose from the drop-down list <company code, for example, 1710>(Company Code <company code, for example, 1710> )Plan Category: Choose from the drop-down list Budget03 (Public Sector Budgeting)Control Object for Fund: Choose from the drop-down list <fund, for example, G2100> (Special revenue fund)Control Object for Cost Center: Choose from the drop-down list <cost center, for example, 17101801> (Other Inc.&Expense (US))Control Object for Budget Account: Choose from the drop-down list 0SPSM41(Only the nodes for which the RIB check level is defined in the global hierarchies app are visible).Rule Description: (e.g.) Service RevenuesActivation Status: Choose from the drop-down list ActiveFilter Profile: Choose from the drop-down list, Revenues and Revenue TransfersCalculation Formula: Choose from the drop-down list S_NO_LIM (PSM Sample Calc. Prof. No Limits)Use Surplus Amount: unchecked (NO)) | The general information is entered in the RIB Rule Header. |  |
| 5 | Enter Sender Revenue Budget Address | In the Sender Revenue Budget Address section, make the following entries manually (Some fields described as (display mode) are taken from the RIB control object because the profile setting for these is identical and are only mentioned here for the sake of completeness.):Fund: <fund, for example, G2100>(Display Mode)Cost Center: <cost center, for example, 17101801>(Display Mode)Budget Account: Choose from the drop-down list 41090000(Please note: the budget account - 41090000 is part of the same hierarchy node chosen for the Control Object for Budget Account - OSPSM41 in the General Information Section) | The Sender Revenue Budget Address screen appears in the editing mode. |  |
| 6 | Enter Receiver Expenditure Budget Address | In the Receiver Expenditure Budget Address section, make the following 2 entries manually:Fund: Choose from the drop-down list <fund, for example, G2100> (Special revenue fund)Cost Center: Choose from the drop-down list <cost center, for example, 17101801> (Other Inc.&Exp (US))Budget Account: Choose from the drop-down list <budget account, for example, t 65008300> (Services - General)Percentage: 50Fund: Choose from the drop-down list <fund, for example, G2100> (Special revenue fund)Cost Center: Choose from the drop-down list <cost center, for example, 17101801> (Other Inc.&Exp (US))Budget Account: Choose from the drop-down list 65001000 (Purchased Services)Percentage: 50 | The Receiver Expenditure Budget Address screen opens in the editing mode. |  |
| 7 | Save the New RIB Rule | Click on Create. | A system message appears informing you that the RIB rule has been saved. |  |

#### Create Revenue Posting (Actuals)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create an actual revenue posting to a posting address that belongs to the RIB control object shown above. For more information, see the test script Accounts Receivable (J59).

Implementation Type

The following section is ONLY relevant for SAP S/4HANA Cloud Public Edition.

Procedure: SAP Fiori

Access the activity as follows:

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Create Outgoing Invoices(FB70). | The Enter Customer Invoice: Company Code # view appears. |  |
| 3 | Basic Data | Choose Company Code.On the dialog box that appears, enter or verify your company code (<company code, for example, 1710>) and choose Continue.Make the following entries:Customer: <customer number>Invoice Date: <Today’s date>Reference: <any>Posting Date: <Today’s date>Amount: <any> and <currency code, for example, USD>.Currency Key : <co.code currency>Calculate Tax : Selected |  |  |
| 4 | Payment Tab | Choose the Payment tab and enter the following:Bline Date : Today’s datePayt Terms: 0001Payt Meth. : <optional> |  |  |
| 5 | Line Items | Scroll down and enter the following in the line item table:G/L Acct : 41090000Cost Center: <cost center, for example, 17101801>Note This master data should be derived (if not, enter manually):Fund: <fund, for example, G2100>Functional Area: <functional area, for example, 1000>Grant: NRGBudget Period: <current year>D/C : CreditAmount in doc. curr.: <enter amount that was entered in the basic data>Tax Code : <Sales Tax Code>Tax jurisdictn.code: <Value is automatically taken from BP master data> |  |  |
| 6 | Profitability Segment | The profitability segment is automatically derived. |  |  |
| 7 | Post | Choose Post to save. | The journal entry is posted. |  |

#### Start RIB Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule a background job for RIB to read the postings created above and distribute the revenue to the corresponding receiving addresses as maintained in the RIB rule.

Implementation Type

The following section is ONLY relevant for SAP S/4HANA Cloud Public Edition.

Procedure: SAP Fiori

Access the activity as follows:

Prerequisites

You have executed the preliminary step [Check Assigned RIB Profile](#unique_11) [page ] 8.

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the Budget Specialist - Funds Management. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Application Jobs - Public Sector (F4519) . | The Application Jobs (F4519) view appears. |  |
| 3 | Create Job | Choose Create. | The New Job view appears. |  |
| 4 | Template Selection | Make the following entries:Job Template: Revenues Increasing the BudgetJob Name: Revenues Increasing the BudgetChoose Step 2 |  |  |
| 5 | Scheduling Options | Make the following entries :Start Immediately: SelectedChoose Step 3 |  |  |
| 6 | Parameters | Make the following entries:Company Code: <company code, for example, G2100>Plan Category: BUDGET03Budget Type (Sender): S_SCAT1Budget Type (Receiver): S_SCAT1Budget Document Type: S_BTDocument Date: <Today’s Date>Posting Date: <Today’s Date>Budget Account: 0SPSM41Cost Center: <cost center, for example, 17101801>Fund: <fund, for example, P1220>Test Run: Selected if you want to perform a test run; Deselected if you want to perform an update runChoose Schedule. | The Application Jobs view appears. |  |
| 7 | View Report | To refresh the review, choose Go . When the report status is Finished, choose the document button in the Results column for the job you scheduled.Note Note You can also choose Log in the scheduled job row. When you do so, the job log appears, showing the Log Details. | The Document (ID xxxxxxx) view appears. The report shows the details of the RIB run, and shows information, such as the revenue amount that was distributed from the sender address (SRIB) to the receiver addreses (RRIB), corresponding funds, cost center, and account information. |  |
| 8 | View Report | Review the document and then choose Back. |  |  |
| 9 | Run Actual Report | If you performed a test run in step 6, repeat steps 2–8 with Test Run deselected to perform an update run. |  |  |

### Display Budget Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Implementation Type

The following section is ONLY relevant for SAP S/4HANA Cloud Public Edition.

Procedure: SAP Fiori

Access the activity as follows:

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the budget specialist. | The SAP Fiori launchpad appears. |  |
| 2 | Open „Manage Budget Transfer“ | Frontend: Fiori App:Open Manage Budget Documents - PSM (F4173). | The Budget Documents screen appears. |  |
| 3 | Display Budget Transfer Document list | Click on Go. | A list of budget transfer documents opens. |  |
| 4 | Use the Search Function | In the Search field, enter the document to be displayed: *<document number>*. or make other field selections for the documents you are searching for here, such as the. Document Status. | The documents for the selected search appear. | You can also check the document created by RIB run. |
| 5 | Display a Budget Transfer Document | Click on the document to be displayed to see the document details on the tabs General Information and Budget Items. | The tab General Information appears. |  |
| 6 | Display Budget Item Data | Click on the tab Budget Items. | The tab Budget Items appears. |  |
| 7 | Display Line Item Data. | Click on one budget line item to see the details of a budget transfer at line item level. | The line item data appears. |  |

### Check Budget Availability

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you use the Active Availability Control (AVC) feature to have the system determine consumable and consumed budget and warn or stop users from proceeding with processing where the available budget is not sufficient.

Using Situation Handling, you can also enable notifications to the budget responsible user before the available budget reaches critical low levels.

Implementation Type

The following section is only relevant for SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the budget specialist. | The SAP Fiori launchpad appears. |  |
| 2 | Check Available Budget | Run the Budget AVC Overview (F2163) Fiori appSelect the following master data (collapse header and add filter):Control Object Fund: <fund, for example, G2200>Control Object Budget Period: <current year>Control Object Cost Center: <OSPSM12>Make a note of the following figures: Consumable amount, consumed amount and available amount.Note: if another user posts to the same master data, the available budget could change. | The budget report is displayed. |  |
| 3 | Log On | Log on to the SAP Fiori launchpad as a generic Accounts Payable Accountant. |  |  |
| 4 | Access the SAP Fiori App | Open Create Supplier Invoice (F0859). | The Manage Supplier Invoices (F0859) view appears. |  |
| 5 | Dialog Box | If the Data from Previous Invoice Entry Exists dialog box appears, choose No. |  |  |
| 6 | General Information | In the Basic Data section, enter the following data:Transaction: InvoiceCompany Code <company code, for example, 1710>Invoicing Party: 17100001Gross Invoice Amount: <higher than the available budget identified above>Currency: <currency code, for example, USD>Invoice Date: <Today's date>Posting Date: <Today's date>Reference: <any> |  |  |
| 7 | G/L Account Items | In the G/L Account Items section, choose + to add a new item.Make the following entries:Debit/Credit: DebitG/L Account: For example, 61061000Amount: <higher than the available budget identified above> |  |  |
| 8 | Account Assignment | Under G/L Accounts, choose > (Expand/Collapse) to expand the selection, make the following entries:Cost Center: <cost center, for example, 17101202>Fund: <fund, for example, G2200>Budget Period: <current year>Grant: for example, NRGFunctional Area: <functional area, for example, 1000>If the general ledger account is tax-relevant, in the Tax section, select Propose Tax.Payment area:Baseline Payment Dte: <enter today's date>Choose Post . | The system shows an error message informing you that not enough budget is available.Posting is not possible. |  |
| 9 | Change Amount inGeneral Information | In the Basic Data section, change the following data:Gross Invoice Amount: <lower than the available budget identified above> - minimum 71%, to trigger the notification.Currency: <currency code, for example, USD> |  |  |
| 10 | Change Amount inG/L Account Items | In the G/L Account Items section, change the following entries:Amount: <lower than the available budget identified above> minimum 71%, to trigger the notification. |  |  |
| 11 | Post Invoice | Choose Post .The supplier invoice number generated is a logistics document number. To find or review the finance document number (Journal Entry), see the Invoice Payment Preparation > View Supplier Line Items task. | The invoice is posted. The system displays the message that the invoice xxx has been posted and the document number. |  |
| 12 | Log On | Log on to the SAP Fiori launchpad with your personalized user (the one you added before as a team member). | The SAP Fiori launchpad appears. |  |
| 13 | Notification | Click on the bell icon (notifications).As a result of the situation handling, a message is sent to you as a responsible team member. | Pre-defined message details are delivered.Note: the notification text refers to all budget management-relevant account assignments, but the control of available budget only takes the fund into account. |  |
| 14 | Check Budget Consumption | Click into the notification text.The system will navigate to Budget AVC Overview (F2163) app. | The budget report shows a budget consumption of over 70%. |  |

### Define AVC Exception

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you use the Active Availability Control (AVC) exception feature to define special rules that overwrite the normal setting of the AVC tolerance profiles. You can for example set up an exception to allow an overrun of your budget up to 150% for a certain user or budget addresses.

Implementation Type

The following section is only relevant for SAP S/4HANA Cloud Public Edition.

Procedure: SAP Fiori

Access the activity as follows:

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the budget specialist. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Run Manage AVC Exceptions (F5372) Fiori app. |  |  |
| 3 | Create AVC Exception | Choose Create and enter the following data:ID: ZAVCEXCPTNDescription: AVC ExceptionAVC Profile: S_PSM1AVC Tolerance Profile: S_PSM2Valid From: <first day of current year>Valid To: <last day of current year>Business User: Select AP_Accountant (using value help)Control Object for Fund from: <fund, for example, G2200>Control Object for Fund to: <fund, for example, G2200> | The New Exception view appears |  |
| 4 | Save AVC Exception | Choose Create. | The AVC exception is saved (currently inactive). A message informs the user that the data is saved. |  |
| 5 | Activate the Exception | Choose Activate. | The activation status of the AVC exception changes from inactive to active. You can test the exception in the next steps by posting an invoice that would exceed the budget by 120%. Determine the available budget as described earlier in this text script using the “My Budget Overview” Fiori app. |  |
| 6 | Log on | Log on to the SAP Fiori launchpad as a generic Accounts Payable Accountant. |  |  |
| 7 | Access the SAP Fiori App | Open Create Supplier Invoice (F0859). | The Create Supplier Invoice (F0859) view displays. |  |
| 8 | Dialog Box | If the Data from Previous Invoice Entry Exist dialog box displays, choose No. |  |  |
| 9 | General Information | In the Basic Data section, enter the following data:Transaction: InvoiceCompany Code: <company code, for example, 1710>Invoicing Party: 17300001Gross Invoice Amount: <20% higher than the available budget identified above>Currency: <currency code, for example, USD>Invoice Date: <Today's date>Posting Date: <Today's date>Reference: <any> |  |  |
| 10 | G/L Account Items | In the G/L Account Items section, choose + to add a new item.Make the following entries:Debit/Credit: DebitG/L Account: For example, 61061000Amount: <20% higher than the available budget identified above> |  |  |
| 11 | Account Assignment | Under G/L Accounts, choose > (Expand/Collapse) to expand the selection, make the following entries:Cost Center: <cost center, for example, 17101101>Fund: <fund, for example, G2200>Budget Period: <current year>Grant: for example, NRGFunctional Area: <functional area, for example, 1000>If the general ledger account is tax-relevant, in the Tax section, select Propose Tax.Payment area:Baseline Payment Date: enter <today's date> | Posting is possible. |  |
| 12 | Post invoice | Choose Post .The supplier invoice number generated is a logistics document number. To find or review the finance document number (Journal Entry), see the Invoice Payment Preparation > View Supplier Line Items task. | The invoice is posted. The system displays the message that the invoice xxx has been posted and document no. |  |
| 13 | Log on | Log on to the SAP Fiori launchpad as the budget specialist. | The SAP Fiori launchpad appears. |  |
| 14 | Access the SAP Fiori App | Run Manage AVC Exceptions (F5372) Fiori app and choose Go . | All AVC exceptions are listed. The AVC expection ZAVCEXCPTN shows now an increased Number of Uses |  |
| 15 | Deactivate the AVC exception. | Select the AVC exception ZAVCEXCPTN and choose Deactivate. |  |  |

### Automatic Account Assignment Distribution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you use the Automatic Account Assignment Distribution to set up rules to derive account assignments - including splitting document line items - when posting budget consumption.

Implementation Type

The following section is only relevant for SAP S/4HANA Cloud Public Edition.

Procedure: SAP Fiori

Access the activity as follows:

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as the budget specialist. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori app | Run the Manage Automatic Account Distribution Rule (F5600) Fiori app |  |  |
| 3 | Create distribution rule | Choose Create and enter the following data:Distribution Rule: <ZDRULE1> |  |  |
| 4 | Enter distribution rule attributes | Rule Group: Select <SPS1>Rule Name: <Any>Field Profile: Select <SFPPS00001>Action Profile: Select <SAP00001>Binding Rule: Select <Results Can Be Changed by Authorized Users>Remainder Handling: Select <Allocate to Original Account Assignment> |  |  |
| 5 | Enter rule items | Choose Create on the facet Distribution Items and enter the following data.Group Number: 1Sequence Number: 1Distribution Method: <Percentage>Start Date: <first day of current year>End Date: <last day of current year>Percentage: 80Fund: fund, for example, G2200>Functional Area: <2000>Choose Apply. Choose Create on the facet Distribution Items and enter the following data for the second line.Group Number: 1Sequence Number: 2Distribution Method: <Percentage>Start Date: <first day of current year>End Date: <last day of current year>Percentage: 20Fund: <fund, for example, G1100>Functional Area: 3000Choose Apply. |  |  |
| 6 | Save the rule | Choose Create on the lower left half of the screen to save the rule. | The distribution rule has been created |  |
| 7 | Activate the rule | Choose Activate. | The distribution rule has been activated |  |
| 8 | Log on | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad appears. |  |
| 9 | Manage substitution/validation | Frontend SAP Fiori app:Open Manage Substitution and Validation Rules (F7603). | The Manage Substitution and Validation for Public Sector (F7603) screen appears. |  |
| 10 | Start creation of the substitution rule | Choose Create Rule. | The dialog box Create Rule appears. |  |
| 11 | Enter values in the dialog box | Choose Public Sector Automatic Account Assignment Distribution Rule in the drop-down list for the Business Context.The event is filled automatically.Choose the rule type Substitution Rule .Choose Create. | The dialog box disappears and the rule maintenance screen appears. |  |
| 12 | Enter the required information for the rule | Enter the following manually:Rule Name: <D_RULE>Description: <Any>In section Precondition:Position the cursor in the field Field. A dialog box appears to select the field. Expand the node PSM_S4C_SPLIT_SUBSTN_RULE and choose the field <Costcenter>.Enter <17101202> in the field ValueIn the section Substitution:Position the cursor in the field Target Field. A dialog box appears to select the field. Choose the field <SplitRule>.Choose <Substitution with constant> as the Substitution Type in the drop-down list for that field.Enter <ZDRULE1> in the Source field.Click Save. | The rule is saved, and the rule maintenance screen appears in the display mode. |  |
| 13 | Activate rule | Choose Activate. | The message Rule Activated appears. |  |
| 14 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad appears. |  |
| 15 | Access app | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen appears. |  |
| 16 | Start purchase order creation | Without making any selection, choose Create. | The New Purchase Order screen appears. |  |
| 17 | Enter purchase order data | Make the following entries:In the Basic Data area:PO Type: Standard PO (NB)Supplier: <supplier, for example, 17300001>Currency: currency code, for example, USD>Purchasing Group: <purchasing group, for example, 001>Purchasing Organization: <purchasing organization, for example, 1710>Company Code: <company code, for example, 1710>Choose the Notes tab at header level. Choose > or < to search for header text. In the Header text column, enter the free text: xxx for testing. |  |  |
| 18 | Purchase material without a material number | In the Items area:Choose Create and enter the following values:Item Category: StandardShort Text: Enter an appropriate description, for example, <office supplies>Material Group: YBMM00Plant: <plant, for example, 1710>Order Quantity: <XX PC >Net Order Price: <XX>Acct Assignment Cat.: Cost Center(K)Go to the Purchase Order item view.Go to the Process Control section: Goods Receipt <empty> (no flag)Go to the Tax section and enter:Tax Code: <tax code, for example, I0>Go to the Account Assignment section and enter:G/L Account 51600000 for a material without a material number. (The G/L account is determined automatically.)Cost Center: <cost center, for example, 17101202>on the screen that appears.Choose Apply and the account assignments are split according to the 80%/20% distribution rule. |  |  |
| 19 | Save purchase order | Choose Apply to return to the purchase order screen. Choose Order to save the purchase order. | The purchase order has been created. |  |

### Periodic Commitment Adjustments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you use the periodic commitment adjustment feature to complete the carryforward of an open commitment document. To perform this test, at least one commitment (such as a purchase requisition, purchase order or earmarked fund) needs to be open. As the commitments are carried forward and the budget period is changed to <current year+1>, you need to create budget for the budget period <current year+1>. Please repeat the step [Create Budget Supplement Document](#unique_17) [page ] 20 with budget period <current year+1>. Please make sure you have enough budget and the budget document is approved.

Implementation Type

The following section is only relevant for SAP S/4HANA Cloud Public Edition.

Procedure: SAP Fiori

Access the activity as follows:

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as the budget specialist. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Run Periodic Commitment Adjustments (F4345) Fiori app |  |  |
| 3 | Select open commitments for budget period | Enter the budget period: <current year> and choose Go. | A list of open commitments is displayed |  |
| 4 | Mark open commitments for carry forward for reassigning the budget period | Mark one or more commitments and choose Reassign . | The system creates a job to reassign commitment from the budget period <current year> to the budget period <current year+1>. The job status changes in the overview list. |  |
| 5 | Access the job and verify the results | Open Application Jobs - Public Sector (F4519) Fiori app and choose Go. In the table you find the last jobs executed. Jobs triggered by the Periodic Commitment Adjustment app have the job name Reassign Account Assignment for Commitments. | The reassigned commitment documents are shown with a success message. |  |

### Residual Budget Processing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you use the job template Automatic Residual Budget Processing to carry residual budget into the next year. To perform this test, some budget needs to remain on the budget account from the chapter [Create Budget Supplement Document](#unique_17) [page ] 20 in the current fiscal year. If this is not the case, please supplement your budget.

Implementation Type

The following section is only relevant for SAP S/4HANA Cloud Public Edition.

Procedure: SAP Fiori

Access the activity as follows:

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the budget specialist. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Run the Application Jobs - Public Sector (F4519) Fiori app | The Application Jobs overview page appears |  |
| 3 | Select the Job Template | Choose CreateSelect the template Automatic Residual Budget Processing and choose a Job Name of your choice.Choose Step 2. | The parameter section screen appears |  |
| 4 | Scheduling Options | Make the following entries :Start Immediately: SelectedChoose Step 3 |  |  |
| 5 | Parameter | Make the following entries:Mode: Fiscal Year Carry ForwardBudget Type (Sender): S_CAT5Budget Type (Receiver): S_CAT6Company Code: <company code, for example, 1710>Fiscal Year: <current fiscal year>Budget Document Type: S_BTFund: <fund, for example, G2200>Percentage: 10Test Run: DeselectedChoose Schedule. | The Application Jobs view appears. |  |
| 6 | View Report | To refresh the review, choose Go . Once the report status is Finished, choose the Log or Result to see the residual budget documents that have been created. |  |  |

### Budget Consumption Dashboard

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The budget consumption dashboard includes analytical tabs from different perspectives for the budget specialist and budget responsible users. Please note that many charts need comprehensive postings with different values (such as different budget types/amount types/…) .

Table 1: The following tabs are available with the Budget Consumption Dashboard.

| Tab# | Tab Name |
| --- | --- |
| 1 | Budget |
| 2 | Budget Consumption |
| 3 | Budget Availability |

Implementation Type

The following section is only relevant for SAP S/4HANA Cloud Public Edition.

Procedure: SAP Fiori

Access the activity as follows:

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as the budget specialist. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Run Budget Consumption Dashboard (F6088) Fiori app. |  |  |
| 3 | Access the relevant tab | Based on the tab you want to view; you can choose from one of the following tabs:BudgetBudget ConsumptionsBudget Availability | The respective tab appears, and the charts are loaded with the data you have selected. |  |

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
> Flagged while digesting this document, not verified: Create Revenue Posting (Actuals): the Overview Table assigns business role Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice, but the procedure logs on as an Accounts Receivable Accountant (and refers to Accounts Receivable J59).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[03-financial-accounting-and-close/test-script-government-budget-planning-6uc-sap-s-4hana-cloud-public-ed]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6YU_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 91,116 chars in the whole document
