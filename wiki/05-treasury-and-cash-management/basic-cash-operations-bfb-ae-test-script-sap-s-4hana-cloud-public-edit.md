---
id: 05-treasury-and-cash-management/basic-cash-operations-bfb-ae-test-script-sap-s-4hana-cloud-public-edit
title: "Basic Cash Operations (BFB_AE) Test Script, SAP S/4HANA Cloud Public Edition (BFB_S4CLD2608_BPD_EN_AE)"
description: "Test script for scope item BFB (UAE/AE, company code 3310, AED): cash operations setup, bank statements, memo records, cash reports, One Exposure and Flow Builder jobs."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/cash-operations]
aliases: [BFB_S4CLD2608_BPD_EN_AE]
keywords: [Cash Operations and Cash Positioning, cash operations, manual bank statement, memo records, memo records 2.0, cash flow analyzer, cash register, one exposure, flow builder, value date correction]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BFB_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1263
topic: 05-treasury-and-cash-management/cash-operations
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Basic Cash Operations (BFB_AE) Test Script, SAP S/4HANA Cloud Public Edition (BFB_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BFB_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Cash Operations and Cash Positioning** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Basic Cash Operations (BFB_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Basic Cash Operations (BFB_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232861464)

[2 Prerequisites 5](#_Toc232861465)

[2.1 System Access 5](#_Toc232861466)

[2.2 Roles 5](#_Toc232861467)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232861468)

[2.4 Business Conditions 6](#_Toc232861469)

[2.5 Preliminary Steps 8](#_Toc232861470)

[2.5.1 Enable Cash Register (Optional) 8](#_Toc232861471)

[2.5.2 Define Start Date for One Exposure 10](#_Toc232861472)

[2.5.3 Define Planning Level 12](#_Toc232861473)

[2.5.4 Define Memo Record Types 14](#_Toc232861474)

[2.5.5 Define Planning Levels for Bank Statements 17](#_Toc232861475)

[2.5.6 Define Condition for Value Date Correction 21](#_Toc232861476)

[2.5.7 Disable/Enable Additional Bank Account Derivation Model (Optional) 23](#_Toc232861477)

[2.5.8 Define Default Bank Accounts for One Exposure (Optional) 25](#_Toc232861478)

[3 Overview Table 27](#_Toc232861479)

[4 Test Procedures 31](#_Toc232861480)

[4.1 Outgoing Payment Without BCM Approval Process 31](#_Toc232861481)

[4.1.1 Accounts Payable and Bank Integration 31](#_Toc232861482)

[4.1.1.1 Bank Integration 32](#_Toc232861483)

[4.1.1.1.1 Option 1: Bank Integration with SAP Multi-Bank Connectivity (16R) (Outgoing Integration) 32](#_Toc232861484)

[4.1.1.1.2 Option 2: Bank Integration with File Interface (1EG) (Outgoing Integration) 32](#_Toc232861485)

[4.1.1.2 Cash Position 32](#_Toc232861486)

[4.2 Cash Operations - Common Steps 34](#_Toc232861487)

[4.2.1 Bank Statements Generation 34](#_Toc232861488)

[4.2.1.1 Option 1: Bank Integration with SAP Multi-Bank Connectivity (16R) (Incoming Integration) 34](#_Toc232861489)

[4.2.1.2 Option 2: Bank Integration with File Interface (1EG) (Incoming Integration) 35](#_Toc232861490)

[4.2.1.3 Option 3: Manual Input Bank Statement 35](#_Toc232861491)

[4.2.1.4 Review Cash Position 39](#_Toc232861492)

[4.2.1.5 Reverse Bank Statement 40](#_Toc232861493)

[4.2.2 Memo Record 41](#_Toc232861494)

[4.2.2.1 Create Memo Record 42](#_Toc232861495)

[4.2.2.2 Copy Memo Record 44](#_Toc232861496)

[4.2.2.3 Distribute Memo Record 45](#_Toc232861497)

[4.2.2.4 Memo Record List 47](#_Toc232861498)

[4.2.3 Memo Record 2.0 48](#_Toc232861499)

[4.2.3.1 Create Memo Record 49](#_Toc232861500)

[4.2.3.2 Import Memo Records 50](#_Toc232861501)

[4.2.3.3 Schedule Jobs for Deactivating Memo Records 2.0 54](#_Toc232861502)

[4.2.4 Correct Value Date 56](#_Toc232861503)

[4.2.5 Cash Reports 57](#_Toc232861504)

[4.2.5.1 Cash Flow Analyzer 58](#_Toc232861505)

[4.2.6 Cash Tools 59](#_Toc232861506)

[4.2.6.1 Schedule Jobs for Cash Register (Optional) 59](#_Toc232861507)

[4.2.6.1.1 Initialize Cash Register 60](#_Toc232861508)

[4.2.6.1.2 Run Cash Register 62](#_Toc232861509)

[4.2.6.2 Create Initial Balance Adjustment with Reference 65](#_Toc232861510)

[4.2.6.3 Schedule Job for Initialize One Exposure Data 67](#_Toc232861511)

[4.2.6.4 Aggregate Flows 69](#_Toc232861512)

[4.2.6.5 Display Cash Management Logs 70](#_Toc232861513)

[4.2.6.6 Schedule Jobs for Health Check 71](#_Toc232861514)

[4.2.6.7 Schedule Jobs for Health Check - with Free Selections 73](#_Toc232861515)

[4.2.6.8 Bank Account Balance Reconciliation 76](#_Toc232861516)

[4.2.6.9 Bank Account Balance Reconciliation with Drill Down 77](#_Toc232861517)

[4.2.6.10 Schedule Job for Rebuild Flow Type of Accounting Documents 79](#_Toc232861518)

[4.2.6.11 Rebuild House Banks and Account IDs in Accounting Documents 81](#_Toc232861519)

[4.2.6.12 Transfer Open Item Accounts to Cash Management 83](#_Toc232861520)

[4.2.6.13 Schedule Jobs for Flow Builder 84](#_Toc232861521)

[4.2.6.14 Schedule Jobs for Flow Builder Utility Toolset 86](#_Toc232861522)

[4.2.6.15 Schedule Jobs for Planning Fields Rebuilding 89](#_Toc232861523)

[4.2.6.16 Delete Data from One Exposure 91](#_Toc232861524)

[4.2.6.17 Schedule Job to Delete Data from One Exposure 92](#_Toc232861525)

[4.2.6.18 Delete Bank Statement Flow from One Exposure 94](#_Toc232861526)

[5 Appendix 96](#_Toc232861527)

[5.1 Process Integration 96](#_Toc232861528)

[5.1.1 Succeeding Processes 96](#_Toc232861529)

## Purpose

Overview

Basic Cash Operations helps you to manage daily cash operations and provides general information of your current cash position and liquidity forecast.

You can get a midterm liquidity forecast based on the projected incoming and outgoing payments and manually entered planning items.

Payment medium files can either be downloaded and sent to the banks manually or automatically sent to the banks via Multi-Bank Connectivity. This scope item supports handling bank statement manually.

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
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |
| Cash Manager | SAP_BR_CASH_MANAGER | Cash Management | SAP_BR_CASH_MANAGER |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Accounts Payable Manager | SAP_BR_AP_MANAGER | Accounts Payable | SAP_BR_AP_MANAGER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. These master data represent materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Currency | AED |  |  |
| House Bank | AEBK1, AEBK2 |  |  |
| House Bank Account ID | AEAC1, AEAC2 |  |  |

### Business Conditions

Before this test script can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BD9 - Sell from Stock orJ14 - Sales Order Processing – Project-Based Services | Before the test step Manually Input Bank Statement ensure that either:Another tester has created a billing document, and its customer item is open (uncleared). You can find open customer items in the app Manage Customer Line Items; in order to run this app, add accounts receivable related roles to your user, you may find these roles in the Accounts Receivable (J59) test scriptIf you cannot find an existing open customer item, create a billing document. You can use the Sell from Stock (BD9) or Sales Order Processing – Project-Based Services (J14) test script or any other test script that creates a customer invoice.Make a note of the amount and Reference Document Number (XBLNR in the header) of this customer invoice. This information is required when simulating a manual bank statement. In the bank statement, a credit item can be reconciled with customer invoice. |
| J60 - Accounts Payable | Perform the relevant steps of payment run to vendors in Accounts Payable (J60) test script, this is the prerequisite of section Accounts Payable Bank Integration in current test script. |
| 16R - Bank Integration with SAP Multi-Bank Connectivity | As part of the process flow for the Accounts Payable Bank Integration section in this test script, perform the procedures in the Outgoing Integration section of the Bank Integration with SAP Multi-Bank Connectivity (16R) test script, as indicatedAs part of the Bank Statement section in this test script, perform the procedures in the Incoming Integration section of the Bank Integration with SAP Multi-Bank Connectivity (16R) test script, as indicated. |
| 1EG - Bank Integration with File Interface | As part of the process flow for the Accounts Payable Bank Integration section in this test script, perform the procedures in the Outgoing Integration section of the Bank Integration with File Interface (1EG) test script, as indicated.As part of the process flow for the Bank Statement section in this test script, perform the procedures in the Incoming Integration section of the Bank Integration with File Interface (1EG) test script, as indicated. |
| J59 - Accounts Receivable | As part of the process flow for the Bank Statement section in this test script, perform the procedures in the Reprocess Bank Statement Items section of the Accounts Receivable (J59) test script, as indicated.As part of the process flow, perform the procedures in the Enter Invoice without Sales Order section of the Accounts Receivable (J59) test script, as indicated. |

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

### Preliminary Steps

#### Enable Cash Register (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Cash register enhances and modernizes SAP S/4HANA Cloud Public Edition Cash Management solutions, providing greater flexibility and comprehensive cash flow integration. Cash register gathers and stores all cash-related source data from components such as Treasury and Materials Management. It can decouple Cash Management from Accounting by using a decoupling approach to streamline processes and reduce dependencies. You do not need to derive or update Cash Management fields during or after posting. As of now, it is supported to import local accounting data source for cash register, except payment order, promise to pay, and parked documents.

|  |
| --- |
| Note If you want to use the cash register, you can enable it in this step. |

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
| 6 | Define Basic Settings | From the Configuration Steps area, on the Define Basic Settings step, choose Configure. | The Change View "Basic Settings": Details view displays. |  |
| 7 | Enable Cash Register | In the Data Model section, enter the following data:Enable Cash Register: <Selected> |  |  |
| 8 | Save | Choose Save. | The cash register is enabled. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Basic Settings | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Basic Settings.Choose Open Document for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Basic Settings": Details screen displays. |  |
| 3 | Enable Cash Register | In the Data Model section, enter the following data:Enable Cash Register: <Selected> |  |  |
| 4 | Save | Choose Save. | The cash register is enabled. |  |

|  |
| --- |
| Remember Basic Settings must be reviewed following any system upgrade or improvement before continuing any business operation in the system. When differences are found from previous activations, you must correct them in the configuration activity Define Basic Settings. |

#### Define Start Date for One Exposure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You defines the start date of One Exposure. Actual flows cannot be generated before the start date. Both the start posting date and start value date can be defined in the configuration. Value Date is mandatory, and it should be filled.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241) . |  |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Application Area | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management |  |  |
| 5 | Cash Operations | Choose the arrow button at the right of the Cash Operations row. |  |  |
| 6 | Define Start Date for One Exposure | Find the Define Start Date for One Exposure row and choose the Configure button. | The Define Start Date for One Exposure:Change screen displays. |  |
| 7 | New Entry | Choose New Entries.Make the following entries and choose Save:CoCd: For example, 3310Note Company code which is defined as blank means that it is the default entry for all company codes.Value Date: For example, the first date of last yearPstng Date: For example, the first date of last year | The start date for one exposure is defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Start Date for One Exposure | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Start Date for One Exposure.Choose Open Document for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Start Date for One Exposure:Change screen displays. |  |
| 3 | New Entry | Choose New Entries.Make the following entries and choose Save:CoCd: For example, 3310Note Company code which is defined as blank means that it is the default entry for all company codes.Value Date: For example, the first date of last yearPstng Date: For example, the first date of last year | The start date for one exposure is defined. |  |

#### Define Planning Level

Purpose

In this activity, you define planning levels for end-of-day, intraday bank statements and Initial Balance Flows.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Search | Choose Configure Your Solution. |  |  |
| 4 | Application and Subapplication Area | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the following row:Item Name: Cash Operations | Configuration steps are displayed for the selected row. |  |
| 6 | Select Configuration Steps | Choose Configure to configure the following row:Step Name: Define Planning Levels | The “Define Planning Levels”: Change view displays. |  |
| 7 | New Entries | Choose New Entries. |  |  |
| 8 | Define Planning Level | Make the following entries and choose Save:Item 1) Planning level for Intraday Bank StatementLevel : for example, INSC: for example, <blank>Source: for example, BNKShort Text: for example, Intra.BSPlanning Level Long Text: for example, Intraday Bank StatementItem 2) Planning level for EoD Bank StatementLevel: for example, EDSC: for example, <blank>Source: for example, BNKShort Text: for example, EoD BSPlanning Level Long Text: for example, End of Day Bank StatementItem 3) Planning level for Initial Balance FlowsLevel: for example, IFSC: for example, <blank>Source: for example, BNKShort Text: for example, IBUPlanning Level Long Text: for example, Initial Balance Flows | The planning level is defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Planning Levels | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Planning Levels.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The “Define Planning Levels”: Change view displays. |  |
| 3 | New Entries | Choose New Entries. |  |  |
| 4 | Define Planning Level | Make the following entries and choose Save:Item 1) Planning level for Intraday Bank StatementLevel : for example, INSC: for example, <blank>Source: for example, BNKShort Text: for example, Intra.BSPlanning Level Long Text: for example, Intraday Bank StatementItem 2) Planning level for EoD Bank StatementLevel: for example, EDSC: for example, <blank>Source: for example, BNKShort Text: for example, EoD BSPlanning Level Long Text: for example, End of Day Bank StatementItem 3) Planning level for Initial Balance FlowsLevel: for example, IFSC: for example, <blank>Source: for example, BNKShort Text: for example, IBUPlanning Level Long Text: for example, Initial Balance Flows | The planning level is defined. |  |

#### Define Memo Record Types

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define memo record types and assign planning levels for intrady bank statement and Initial Balance Flows.

|  |
| --- |
| Note If you work with memo records 2.0, you must specify a memo record category for your memo record type. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241) . |  |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Application Area | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management |  |  |
| 5 | Cash Operations | Choose the arrow button at the right of the Cash Operations row. |  |  |
| 6 | Define Memo Record Types | Find the Define Memo Record Types row and choose the Configure button. | The Change View “Define Memo Record Types”: Overview screen displays. |  |
| 7 | Maintain Memo Record Category | Add memo record category for the Memo Record Types as needed and choose Save.For example:Memo Record Type AU with Memo Record Category Payment AdviceMemo Record Type DI with Memo Record Category Planned ItemAuto.Expiration: <as needed>NoteFor memo records 2.0, specify whether you want to enable the automatic expiration for memo records that have the memo record category Planned Item or Payment Advice.To enable automatic expiration for these memo records, select the Auto Expiration checkbox.The availability of the field Expiration Time also depends on the settings in the configuration activity Manage Field Status Groups for Memo Records. If you want to use the automatic expiration function, make sure the Expiration Time field is not set to suppressed. | The memo record categories are maintained for the Memo Record Types.Note You can also create new Memo Record Types as needed. |  |
| 8 | Create Memo Record Type | Choose New entries, enter the following data and choose Save:Item1) Memo record type for Intraday Bank StatementMemoTp: for example, INPlan.Lvl: for example, INMemo Type Description: for example, Intraday BSMemo Record Category: for example, Intraday Bank StatementItem 2 ) Memo record type for Initial Balance FlowsMemo Tp: for example, IFPlan.Lvl: for example, IFMemo Record Type Description: for example, Initial Balance FlowsMemo Record Category: for example, IBU Initial Balance Flows | The memo record types are defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Memo Record Types | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Memo Record Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View “Define Memo Record Types”: Overview screen displays. |  |
| 3 | Maintain Memo Record Category | Add memo record category for the Memo Record Types as needed and choose Save.For example:Memo Record Type AU with Memo Record Category Payment AdviceMemo Record Type MP with Memo Record Category Planned ItemAuto.Expiration: <as needed>NoteFor memo records 2.0, specify whether you want to enable the automatic expiration for memo records that have the memo record category Planned Item or Payment Advice.To enable automatic expiration for these memo records, select the Auto Expiration checkbox.The availability of the field Expiration Time also depends on the settings in the configuration activity Manage Field Status Groups for Memo Records. If you want to use the automatic expiration function, make sure the Expiration Time field is not set to suppressed. | The memo record categories are maintained for the Memo Record Types.Note You can also create new Memo Record Types as needed. |  |
| 4 | Create Memo Record Type | Choose New entries, enter the following data and choose Save:Item1) Memo record type for Intraday Bank StatementMemoTp: for example, INPlan.Lvl: for example, INMemo Type Description: for example, Intraday BSMemo Record Category: for example, Intraday Bank StatementItem 2 ) Memo record type for Initial Balance FlowsMemo Tp: for example, IFPlan.Lvl: for example, IFMemo Record Type Description: for example, Initial Balance FlowsMemo Record Category: for example, IBU Initial Balance Flows | The memo record types are defined. |  |

#### Define Planning Levels for Bank Statements

Purpose

In this activity, you define planning levels for end-of-day and intraday bank statements.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

You can choose to activate the New Integration Strategy for Bank Statements and Cash Mgmt feature.

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Search | Choose Configure Your Solution. |  |  |
| 4 | Application and Subapplication Area | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the following row:Item Name: Cash Operations | Configuration steps are displayed for the selected row. |  |
| 6 | Select Configuration Steps | Choose Configure to configure the following row:Step Name: Define Planning Levels for Bank Statements | The Define Planning Levels for Bank Statements: Change: Details view displays. |  |
| 7 | Define Planning Level for Bank Statements | Choose New Entries, make the following entries and choose Save:Planning Level for EoD Bank Statements section:Default Planning Level for EoD Bank Statements: for example, EDFirst Derivation Source: for example, External Transaction Type ConfigurationNote The memo record types are defined in the configuration activity Make Global Settings for Electronic Bank Statement (ID 101024). You can search for this configuration activity in your configuration environment.Second Derivation Source: for example, Default Planning LevelNote The default planning level defined in this activity is used when this source is selected.Whether to Include All Bank Statement items: for example, <seleted>Planning Level for Intraday Bank Statements section:Default Memo Record Type for Intraday Bank Stmnt: for example, INNote Depending on your configuration, intraday memo records can be automatically generated from intraday bank statements to represent the bank statement line items.Default Planning Level for Intraday Bank Stmnt: <automatically derived>First Derivation Source: for example, External Transaction Type ConfigurationNote The memo record types are defined in the configuration activity Make Global Settings for Electronic Bank Statement (ID 101024). You can search for this configuration activity in your configuration environment.Second Derivation Source: for example, Default Memo Record TypeNote The default memo record type defined in this activity is used when this source is selected.Whether to Include All Bank Statement items: for example, <seleted> |  |  |
| 8 | Save | Choose Save. | The planning levels for end-of-day and intraday bank statements are defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Open | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Planning Levels for Bank Statements.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration. | The Define Planning Levels for Bank Statements: Change: Details view displays. |  |
| 3 | Define Planning Level for Bank Statements | Choose New Entries, make the following entries and choose Save:Planning Level for EoD Bank Statements section:Default Planning Level for EoD Bank Statements: for example, EDFirst Derivation Source: for example, External Transaction Type ConfigurationNote The memo record types are defined in the configuration activity Make Global Settings for Electronic Bank Statement (ID 101024). You can search for this configuration activity in your configuration environment.Second Derivation Source: for example, Default Planning LevelNote The default planning level defined in this activity is used when this source is selected.Whether to Include All Bank Statement items: for example, <seleted>Planning Level for Intraday Bank Statements section:Default Memo Record Type for Intraday Bank Stmnt: for example, INNote Depending on your configuration, intraday memo records can be automatically generated from intraday bank statements to represent the bank statement line items.Default Planning Level for Intraday Bank Stmnt: <automatically derived>First Derivation Source: for example, External Transaction Type ConfigurationNote The memo record types are defined in the configuration activity Make Global Settings for Electronic Bank Statement (ID 101024). You can search for this configuration activity in your configuration environment.Second Derivation Source: for example, Default Memo Record TypeNote The default memo record type defined in this activity is used when this source is selected.Whether to Include All Bank Statement items: for example, <seleted> |  |  |
| 4 | Save | Choose Save. | The planning levels for end-of-day and intraday bank statements are defined. |  |

#### Define Condition for Value Date Correction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can define the date difference tolerance between the value date and the posting date to decide whether the value date of an accounting document line item needs to be reviewed and corrected. For a given line item, if the difference between the value date and its posting date exceeds the tolerance, the value date will be corrected into the posting date in BSEG. You can use the Value Date Correction (FCLM_VALUT_CORR) app to check the list of value dates to be corrected and correct the incorrect value dates and planning dates of the selected document items.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Step # | Test Step Name |  | Instruction | Expected Result | Pass / Fail / Comment |
| 1 | Log On |  | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App |  | Open Manage Your Solution (F1241) . |  |  |
| 3 | Configure Your Solution |  | Choose Configure Your Solution. |  |  |
| 4 | Application Area |  | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management |  |  |
| 5 | Cash Operations |  | Choose the arrow button at the right of the Cash Operations row. |  |  |
| 6 | Define Condition for Value Date Correction |  | Find the Define Condition for Value Date Correction row and choose the Configure button. | The “Define Condition for Value Date Correction”: Change screen displays. |  |
| 7 | Add New Entries |  | Choose New Entries.Make the following entries and choose Save:CoCd: For example, 3310House Bk: For example, AEBK1Tolerance: For example, 30 | The condition for value date correction is defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Condition for Value Date Correction | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition for Value Date Correction.Choose Open Document for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Define Condition for Value Date Correction | Find the Define Condition for Value Date Correction row and choose the Configure button. | The "Define Condition for Value Date Correction": Change screen displays. |  |
| 4 | Add New Entries | Choose New Entries.Make the following entries and choose Save:CoCd: For example, 3310House Bk: For example, AEBK1Tolerance: For example, 30 | The condition for value date correction is defined. |  |

#### Disable/Enable Additional Bank Account Derivation Model (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

For actual cash flow, by default, the system applies an additional bank account derivation logic for the accounting flows that are lacking in the bank account information, for example the bank account, house bank, and house bank account information. You can disable additional Bank Acct Derivation Model for actual flow, the system suspends the additional bank account derivation logic.

For forecasted cash flow, you can enable bank account derivation model to update default bank account.

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
| 6 | Define Basic Settings | From the Configuration Steps area, on the Define Basic Settings step, choose Configure. | The Change View "Basic Settings": Details view displays. |  |
| 7 | Disable Additional Bank Account Derivation Model Actual Cash Flow | In the Data Model section, enter the following data:Disable Addi Bank Acct Deriv Model Actual Cash Flow: <as needed> |  |  |
| 8 | Enable Bank Account Derivation Model Forecast Cash Flow | Enter the following data:Enable Bank Account Derivation Model Forecast Cash Flow: <Selected>Reuse Setting Maintain Payment Program Forecast Cash Flow: <Selected>Set Addit. Bank Account Derivation Rule "Forecast Cash Flow": <Selected>NoteIf ‘Set Addition Bank Account Derivation Rule Forecast Cash Flow’ is selected, Flow Builder will derive BAM technical ID according to the master data ‘Default Bank Accounts for One Exposure’.'Set Addition Bank Account Derivation Rule Forecast Cash Flow’ will not only work for FI but also for all other data sources like TRM, MM, SD and the like. |  |  |
| 9 | Save | Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Basic Settingst | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Basic Settings.Choose Open Document for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Basic Settings": Details screen displays. |  |
| 3 | Disable Additional Bank Account Derivation Model Actual Cash Flow | In the Data Model section, enter the following data:Disable Addi Bank Acct Deriv Model Actual Cash Flow: <as needed> |  |  |
| 4 | Enable Bank Account Derivation Model Forecast Cash Flow | Enter the following data:Enable Bank Account Derivation Model Forecast Cash Flow: <Selected>Reuse Setting Maintain Payment Program Forecast Cash Flow: <Selected>Set Addit. Bank Account Derivation Rule "Forecast Cash Flow": <as needed>NoteIf ‘Set Addition Bank Account Derivation Rule Forecast Cash Flow’ is selected, Flow Builder will derive BAM technical ID according to the master data ‘Default Bank Accounts for One Exposure’.'Set Addition Bank Account Derivation Rule Forecast Cash Flow’ will not only work for FI but also for all other data sources like TRM, MM, SD and the like. |  |  |
| 5 | Save | Choose Save. |  |  |

|  |
| --- |
| Remember Basic Settings must be reviewed following any system upgrade or improvement before continuing any business operation in the system. When differences are found from previous activations, you must correct them in the SSCUI Define Basic Settings. |

#### Define Default Bank Accounts for One Exposure (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can define default bank accounts for One Exposure. If no bank account ID exists in a cash flow, a default bank account ID can be obtained. According to the bank account ID, the house bank and house bank account can be obtained, and they can be used and replace the original ones in the cash flow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Define Default Bank Accounts for One Exposure (FCLM_DEF_BNK_ID). | The Change View “Default Bank Accounts for One Exposure”: Overview displays. |  |
| 3 | Create New Entry | Choose New Entries and create entries as needed.Note Company Code, Currency, Source Application, Cash Direction, Payment Method, Planning Level, Planning GroupThese fields are the control fields that determine how to get the corresponding bank.Bank Country / Region Key, Bank Key, Account Number, Bank Control KeyThese fields are the result fields and are used to get the corresponding bank account technical ID, house bank and house bank account.The validity check will be performed when you save the entry. If the corresponding bank ID cannot be found in the app for the entered bank combination, an error will be reported.When a bank is generated in a flow, if the corresponding bank cannot be found according to the data in the configuration, no bank will be generated and the empty value will be used. |  |  |
| 4 | Save | Choose Save. |  |  |

## Overview Table

The Basic Cash Operations (BFB) test script consists of several process steps and reports provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Outgoing Payment Without BCM Approval Process

Table 1: Accounts Payable Bank Integration

| Process Step, Report or Item | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| Bank Integration | Role dependent upon procedure | Transaction/App dependent upon procedure | Results dependent upon procedure |
| [Cash Position](#unique_16) [page ] 32 | Cash Management Specialist | Cash Flow Analyzer (F2332) | The outflow of outgoing payment is reflected in cash position. |

Cash Operations - Common Steps

Table 2: Bank Statement

| Process Step, Report or Item | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Option 1: Bank Integration with SAP Multi-Bank Connectivity (16R) (Incoming Integration)](#unique_17) [page ] 34 | Role dependent upon procedure | Transaction/App dependent upon procedure | Results dependent upon procedure |
| [Option 2: Bank Integration with File Interface (1EG) (Incoming Integration)](#unique_18) [page ] 35 | Role dependent upon procedure | Transaction/App dependent upon procedure | Results dependent upon procedure |
| [Option 3: Manual Input Bank Statement](#unique_19) [page ] 35 | Cash Management Specialist | Manage Bank Statements (F1564) | A manual bank statement is created. |
| [Review Cash Position](#unique_20) [page ] 39 | Cash Management Specialist | Cash Flow Analyzer (F2332) | Bank statement data is reflected in cash position. |
| [Reverse Bank Statement](#unique_21) [page ] 40 | Cash Management Specialist | Manage Bank Statements (F1564) | Bank statement is reversed. |

Table 3: Memo Record

| Process Step, Report or Item | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Memo Record](#unique_22) [page ] 42 | Cash Management Specialist | Manage Memo Records (F2986) | You created the memo record. |
| [Copy Memo Record](#unique_23) [page ] 44 | Cash Management Specialist | Manage Memo Records (F2986) | You copied the memo record. |
| [Distribute Memo Record](#unique_24) [page ] 45 | Cash Management Specialist | Manage Memo Records (F2986) | You distributed the memo record. |
| [Memo Record List](#unique_25) [page ] 47 | Cash Management Specialist | Manage Memo Records (F2986) | Memo records are displayed in memo record list, memo record can be archived. |

Table 4: Memo Record 2.0

| Process Step, Report or Item | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Memo Record](#unique_26) [page ] 49 | Cash Management Specialist | Manage Memo Records 2.0 (F2986A) | You created the memo record. |
| [Import Memo Records](#unique_27) [page ] 50 | Cash Management Specialist | Import Memo Records 2.0 (F6124) | You copied the memo record. |
| [Schedule Jobs for Deactivating Memo Records 2.0](#unique_28) [page ] 54 | Cash Management Specialist | Schedule Jobs for Deactivating Memo Records 2.0 (F8915) | Use filters to select memo records and set their status to Deactivated in one go. |

| Process Step, Report or Item | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Correct Value Date](#unique_29) [page ] 56 | Cash Management Specialist | Value Date Correction (FCLM_VALUT_CORR) | You correct value date. |

Table 5: Cash Reports

| Process Step, Report or Item | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Cash Flow Analyzer](#unique_30) [page ] 58 | Cash Manager | Cash Flow Analyzer (F2332) | Cash Flow report created. |

Table 6: Cash Tools

| Process Step, Report or Item | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Schedule Jobs for Cash Register (Optional) |  |  |  |
| [Initialize Cash Register](#unique_31) [page ] 60 | Cash Manager | Schedule Job for Cash Register (F8948) | Replicate data to Cash Register and the FQM_FLOW table in One Exposure. |
| [Run Cash Register](#unique_32) [page ] 62 | Cash Manager | Schedule Job for Cash Register (F8948) | Build cash related data to Cash Register and the FQM_FLOW table in One Exposure. |
| [Create Initial Balance Adjustment with Reference](#unique_33) [page ] 65 | Cash Manager | Create Initial Balance and Balance Adjustment with Reference (FQM_INTBAL_AUTOCRT) | The initial balance data are created. |
| [Schedule Job for Initialize One Exposure Data](#unique_34) [page ] 67 | Cash Manager | Schedule Jobs for Flow Builder (F3804) | Jobs are scheduled for initialize one exposure data. |
| [Aggregate Flows](#unique_35) [page ] 69 | Cash Manager | Aggregate Flows (FQM_AGGREGATE_FLOWS) | Aggregate flows verified. |
| [Display Cash Management Logs](#unique_36) [page ] 70 | Cash Manager | Application Log (F1487) | The application log is verified. |
| [Schedule Jobs for Health Check](#unique_37) [page ] 71 | Cash Management Specialist | Schedule Jobs for Health Check (F3030) | The application jobs are executed. |
| [Schedule Jobs for Health Check - with Free Selections](#unique_38) [page ] 73 | Cash Management Specialist | Schedule Jobs for Health Check (F5285) | You can schedule Health Check for Cash Management with free selection. |
| [Bank Account Balance Reconciliation](#unique_39) [page ] 76 | Cash Management Specialist | Bank Account Balance Reconciliation with Drill Down (FCLM_BANK_RECONCIL) | The Bank Account Balance Reconciliation is reviewed. |
| [Bank Account Balance Reconciliation with Drill Down](#unique_40) [page ] 77 | Cash Management Specialist | Bank Account Reconciliation with Drill Down | The bank account reconciliation displays. |
| [Schedule Job for Rebuild Flow Type of Accounting Documents](#unique_41) [page ] 79 | Cash Management Specialist | Schedule Job for Rebuild Flow Type of Accounting Documents | Rebuild flow type in accounting document. |
| [Rebuild House Banks and Account IDs in Accounting Documents](#unique_42) [page ] 81 | Cash Management Specialist | Schedule Job for Insert House Bank and House Bank Account Data in Table BSEG (F7188) | Schedule jobs to insert house bank data to table BSEG. |
| [Transfer Open Item Accounts to Cash Management](#unique_43) [page ] 83 | Cash Management Specialist | Planning Correction (OT30) | Rebuild planning levels and planning groups for open item in accounting documents. |
| [Schedule Jobs for Flow Builder](#unique_44) [page ] 84 | Cash Manager | Schedule Jobs for Flow Builder (F3804) | Derived cash flows will be stored to the One Exposure from Operation hub for analytical purposes. |
| [Schedule Jobs for Flow Builder Utility Toolset](#unique_45) [page ] 86 | Cash Manager | Application Jobs (F8949) | Schedule jobs for Flow Builder/Cash Register Utility Toolset using the template. |
| [Schedule Jobs for Planning Fields Rebuilding](#unique_46) [page ] 89 | Cash Manager | Schedule Jobs for Flow Builder (F3804) | Schedule jobs for planning correction for one exposure data. |
| [Delete Data from One Exposure](#unique_47) [page ] 91 | Cash Manager | Delete Data from One Exposure (FQM_DELETE) | Delete transactional data in One Exposure from Operations to ensure data protection and privacy. |
| [Schedule Job to Delete Data from One Exposure](#unique_48) [page ] 92 | Cash Manager | Schedule Job for Delete Data from One Exposure from Operation Hub (F5936) | Schedule job to delete data from one exposure. |
| [Delete Bank Statement Flow from One Exposure](#unique_49) [page ] 94 | Cash Management Specialist | Delete Data from One Exposure (FQM_DELETE) | Delete bank statement flow from one exposure. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Outgoing Payment Without BCM Approval Process

#### Accounts Payable and Bank Integration

Purpose

This section describes how the outgoing payment to vendors is integrated with a bank, that is, how will payment medium files be provided to the bank.

|  |
| --- |
| Caution The following procedures are only for when the outgoing payment is without BCM approval process. Using additional functionality requires an extra license for SAP Cash Management powered by SAP HANA, and outgoing payment with BCM approval process will require that extra license. If you have extra license and require outgoing payment with the BCM approval process, skip this entire section and go to the Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J78) ) test script and execute the Outgoing Payment with BCM Approval Process procedure. |

The payment medium file is usually created automatically after an automatic payment run to vendors (For more information, see the Accounts Payable ([J60](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J60)) test script.) There are two formats available for each DMEE tree, both formats can be used by one payment method:

- Format for Multi-Bank Connectivity (MBC) connectivity: They support MBC connectivity. MBC forwards the payment medium file to an SFTP server directly as a pass-through gateway.
- Format for File Download: They support file download via the Manage Payment Media app.

Prerequisites

Test the relevant steps of payment run to vendors in the Accounts Payable (J60) test script.

##### Bank Integration

###### Option 1: Bank Integration with SAP Multi-Bank Connectivity (16R) (Outgoing Integration)

Purpose

With SAP Multi-Bank Connectivity (MBC), SAP establishes connections with your banks to automatically send payment instructions, receive status notifications, receive bank statements, and receive lockbox messages.

|  |
| --- |
| Note Only the house bank with Alternative Format Type 90 (SAP Multi-Bank Connectivity) can be used in Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/16R)) test script. You can check this customizing via configuration activity: 101972 (Set Up Payment Methods for Each Country/Region for Payment Transactions). |

Procedure

The step is mentioned in the Outgoing Integration test procedure of the Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/16R)) test script.

###### Option 2: Bank Integration with File Interface (1EG) (Outgoing Integration)

Purpose

You download the payment files for outgoing payments, which are generated by SAP S/4HANA Cloud Public Edition to your computer. You can then upload these payment files to your banking portal or treasury workstation for payment processing.

Procedure

The step is mentioned in the Outgoing Integration test procedure of the Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/1EG)) test script.

##### Cash Position

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the payment run to vendors is completed as described in the Accounts Payable ([J60](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J60)) test script and the journal entry is created, the self-initiated payment will be reflected in the Cash Flow Analyzer report.

Prerequisite

Test the relevant steps for payment run to vendors in Accounts Payable (J60) test script, by using either payment medium format for Multi-Bank Connectivity (MBC) or payment medium format for file download.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Cash Flow Analyzer (F2332). |  |  |
| 3 | Enter Criteria | To review the cash position relevant to subaccounts, enter the following selection criteria and choose Go.Company Code: for example, 3310Time Period: For example, D14Date: <current date>Reconciliation Status: Unreconciled Intrady Bank Statements & Unreconciled Forecasted Cash FlowsDate Indicator: for example, <value date>Note Choose Adapt Filters if the filter selection fields are hidden. | A Cash Flows table displays with the filtered results.Note Based on the predelivered configuration, the bank transfer payment is credited on bank subaccount 11001020; the B2 planning level is assigned to these two G/L accounts. If the bank subaccount determination is changed, or planning level of G/L account is changed, the amount could also be reflected with another planning level. |  |

### Cash Operations - Common Steps

#### Bank Statements Generation

Purpose

The section describes how to handle the bank statement in SAP S/4HANA Cloud Public Edition.

Prerequisite

- Prepare a customer invoice
- As already described in Business Conditions section, find a customer invoice created by another tester (the customer line item must be open), or perform Sell from Stock (BD9) or Sales Order Processing - Project-Based Services (J14) or any other test scripts that creates a customer invoice. Make a note of the amount and the Reference Document Number (XBLNR in the header) of the customer invoice document.

When creating an incoming payment item in manual bank statement, if you enter the Reference Document Number in this bank statement item, then the system will find the open customer line item and clear it based on interpretation algorithm assigned to manual transaction (in our example, its manual transaction F001 with interpretation algorithm 001).

- Prepare an outgoing payment document

Perform the procedure Payment run in the Accounts Payable ([J60](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J60)) test script. Make a note of the outgoing payment amount. Payment medium generated by the payment program are grouped by means of a DME (data medium exchange) Reference Number.

-
    - When the payment run is executed and the paying house bank uses the payment medium format of MBC connectivity for the payment run, ensure to record the DME Reference Number (Payment Information ID) as described in step Pull Status Message from MBC of the Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/16R)) test script
    - When the payment run is executed and the paying house bank uses a payment medium format for file download (not for MBC connectivity) for the payment run, ensure to record the DME Reference Number as described in the Download File procedure of Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/1EG)) test script.
    - For creating an outgoing payment item in manual bank statement, if you enter the DME Reference Number in the bank statement item, the system finds the open item of bank subaccount in payment document created via payment run, and then clears it based on interpretation algorithm assigned to manual transaction (in our example, its manual transaction F004 with interpretation algorithm 019).

##### Option 1: Bank Integration with SAP Multi-Bank Connectivity (16R) (Incoming Integration)

Purpose

If the SAP S/4HANA Cloud Public Edition is connected to Multi-Bank Connectivity (MBC), the electronic bank statement file provided by bank is stored in an SFTP folder, MBC retrieves the electronic bank statement file from SFTP, and then does validation and mapping.

The SAP S/4HANA Cloud Public Edition schedules a background every 10 minutes to retrieve the bank statement file from MBC, and the file is automatically imported into the SAP S/4HANA Cloud Public Edition.

|  |
| --- |
| Note Because the simulated bank statement file must be stored in the SFTP folder, contact your system administrator or the testing organizer for information to access the SFTP folder, as different testing systems/clients may have different SFTP folders. |

|  |
| --- |
| Note Only the house bank with Alternative Format Type 90 (SAP Multi-Bank Connectivity) can be used in Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/16R)) test script. You can check this customizing via configuration activity: 101972 (Set Up Payment Methods for Each Country/Region for Payment Transactions). |

Procedure

The step is mentioned in the Incoming Integration test procedure of the Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/16R)) test script.

##### Option 2: Bank Integration with File Interface (1EG) (Incoming Integration)

Purpose

You get bank statement file from bank, and import this electronic bank statement file in SAP S/4HANA Cloud Public Edition system manually.

Procedure

The step is mentioned in the Incoming Integration test procedure of the Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/1EG)) test script.

##### Option 3: Manual Input Bank Statement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to create a manual bank statement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Statements (F1564). |  |  |
| 3 | Get Latest Bank Statement Number | To get the latest imported bank statement number, make the following entries and choose Go.Editing Status: AllLatest Statements: select the checkbox Latest OnlyCompany Code: 3310House Bank: AEBK1House Bank Account: AEAC1Note If any selection criteria is invisible, choose Adapt Filter to add it to filter bar. | The latest bank statement number of the specified bank account displays on the Manage Bank Statements view.The next bank statement number is one greater than the latest bank statement number. For example, if the latest bank statement number is 5, the next number is 6. If no latest bank statement found, the next number should be 1. |  |
| 4 | Get Closing Balance of Latest Bank Statement | Make note of the closing balance of the specified bank account, it can be found on the Manage Bank Statements view. | The closing balance of the latest bank statement should be the opening balance of the next bank statement.If no latest bank statement found, the opening balance of the next bank statement should be zero. |  |
| 5 | Create New Bank Statement | Choose Create.On the Bank Statement view, make the following entries:House Bank Account: AEAC1House Bank: AEBK1Company Code: 3310Bank Statement Number: the next Bank Statement Number, for example, 6Bank Statement Date: for example, <Current Date>Payment Transaction Type Group: for example, <Blank>Note You can either use manual transaction or external transactions to create a manual bank statement.For manual transaction: just leave Payment Transaction Type Group empty.For external transaction: if you want to use an existing external transaction type from a group which was created for a bank statement format of the electronic bank statement (for example, MT940). You need to enter the relevant transaction type group (for example, XXMT). Then external transaction can be used later.Choose Enter to determine the currency of this house bank before entering opening or closing balances.Opening Balance: for example, 5002.00Closing Balance: for example, 4019.00 | The data of bank statement header is entered.The opening balance is the closing balance of latest imported bank statement, for example, 5002.00.The closing balance = opening balance - debit amount + credit amount, for example,4019.00=5002.00+208.00-1191.00. |  |
| 6 | Create First Bank Statement Item | In the Bank Statement Items area, make the following entries:Manual Transaction: F001Note This field only for Manual Transaction. If you use external transaction, you should enter in field External Transaction.Value Date: for example, <current date>Amount: enter the receivable amount of customer invoice as described in Prerequisites, for example, 208.00Customer Ref No: enter the Reference Document Number of customer invoice as described in Prerequisites, for example, SDTESTChoose Apply. | The first bank statement item with manual transaction is entered, and go back to the previous view Bank Statement automatically. |  |
| 7 | Create Second Bank Statement Item | Choose Create in Bank Statement Items area, and make the following entries:Manual Transaction: F004Note As alternative to the DME Reference Number you can also refer to a payment document created with the payment run. Enter the following: External Transaction: for example F003, then enter in the field Payment Reference the payment document number.Value Date: for example, <current date>Amount: enter the outgoing payment amount created via payment run as described in Prerequisites, for example, -1191.00Memo Line: enter the DME Reference Number as described in Prerequisites, for example,1000004611Choose Apply. | The second bank statement item with manual transaction is entered, and go back to the previous view Bank Statement automatically. |  |
| 8 | Create the Bank Statement | On the Bank Statement view, choose Create. | The statement status should be Created. |  |
| 9 | Post the Bank Statement | On the Bank Statement view, choose Post.The Information dialog box displays the Statement posted: all items completed message. Choose Close. | The statement status should be changed from Saved to Completed.The first bank statement item has reconciled with an open customer line item in an invoice, and the customer line item has been cleared.Journal Entries are:Posting Area 1 - Bank Accounting:Dr: Bank main accountCr: Bank subaccountPosting Area 2 - Sub ledger Accounting:Dr: Bank subaccountCr: Accounts receivable - customer (with clearing).The second bank statement item has reconciled with payment document created by payment run, and the bank subaccount in the payment document is cleared.Journal Entries are:Posting Area 1 - Bank Accounting:Dr: Bank technical accountCr: Bank main accountPosting Area 2 - Subledger Accounting:Dr: Bank subaccount (with clearing)Cr: Bank technical accountNote If the bank statement cannot be posted and shows status ‘7 (Not completed)’, you need to reprocess the bank statement. Use app Reprocess Bank Statement Items (F1520) to complete the posting.Note If the bank accounts are defined with 'Posting Category - No Posting Processing', then no FI posting is generated.For more information about this setting, see step Define Bank Account Settings – Bank Statements or Define Settings for Bank Statements in Basic Bank Account Management (BFA) test script. |  |

##### Review Cash Position

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the cash position report after bank statement is imported or manually created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Cash Flow Analyzer (F2332). |  |  |
| 3 | Review Cash Position Relevant to Bank Subaccounts | Choose Adapt Filters if the filter selection fields are hidden.Maintain selection criteria and choose Go.Company Code: for example, 3310Time Period: For example, D14Date: <Today>Reconciliation Status: Unreconciled Intrady Bank Statements & Unreconciled Forecasted Cash FlowsDate Indicator: for example, Value DateBank Account: for example, 0000000693123456 | The amount of the bank statement line item is reflected on the F0 planning level, in the lowest level of hierarchy.Note Based on the predelivered master data, the bank main account is 11001000. If the planning level of the G/L account is changed, the amount could also be reflected with another planning level. |  |

##### Reverse Bank Statement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you reverse imported or manually created bank statements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Statements (F1564). | The Manage Bank Statements (F1564) view displays. |  |
| 3 | Enter Criteria | Enter the following selection criteria and choose Go.Editing Status: AllHouse Bank Account: For example, AEAC1House Bank: For example, AEBK1Company Code: For example, 3310Note If any selection criterion is missing, choose Adapt Filter and from the dialog box that displays, add the criteria and choose Go. | A list of bank statements display. |  |
| 4 | Select Bank Statement | Double-click the statement to be reversed. | The details view of the bank statement displays. |  |
| 5 | Reverse the Bank Statement | Choose Reverse. | A Reverse Bank Statement dialog box displays. |  |
| 6 | Confirm the Reversal | Enter the following data and choose Reverse:Reversal Reason: For example, Wrong PostingPosting Date: For example, <today's date> | A notification confirms that reversing of bank statement started successfully. |  |
| 7 | Confirm | Choose OK to confirm the dialog box. | The bank statement status is changed to Reversed. |  |
| 8 | Check Reversal Log | Choose Reversal log on upper-right corner. Choose Information under Log and Results section. | The Reversal Log for your bank statement is displayed. The relevant posting documents are reversed successfully. The open items are reopened. |  |

#### Memo Record

Purpose

You can manually enter incoming and outgoing payments in the planning that are not transferred to the SAP Cash Management System during actual postings.

With app Manage Memo Records (F2986), you can create memo records centrally for expected cash flows that are not yet generated in the system. The memo records are then displayed in the cash management apps, such as Cash Flow Analyzer and Check Cash Flow Items. You can also use this app to view, change, and delete the intraday memo records that are generated automatically from imported intraday bank statements.

You differentiate between the payment advices relevant to the cash position and the planned items relevant to the liquidity forecast.

Payment Advices:

You can enter the following as memo records of payment advices in the system:

- Confirmed payment advices (planning level AB),
- Unconfirmed payment advices (planning level AU),
- Fixed-term deposits (planning level TD),
- Loans revenue (planning level DE),
- All bank fields (planning level ZB)
- and so on…

Payment advices is relevant to Cash Position.

Planned Items:

You can enter the following as memo records of planned items in the system:

- Noted items (planning level MP)
- General planning (planning level DI)
- All sub ledger fields (planning level ZP).

Planned items is relevant to Liquidity Forecast.

##### Create Memo Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You create a memo record.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cash Management Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Memo Records (F2986). |  |  |
| 3 | Enter Header Data | Choose Create Memo Record/... and choose Create Memo Record.Make the following entries and choose Enter.Company Code: 3310Amount: for example, 16000Currency: AEDPlanning Level: for example, AU or MPNote In the field Planning Level, you can open the value help and choose on upper left corner either Planning Level for Bank Accounting or Planning Level for Subledger Accounting.For example: Planning Level: AU for Planning Level for Bank AccountingFor example: Planning Level: MP for Planning Level for Subledger Accounting |  |  |
| 4 | Enter General Data | On the General Data section, make the following entries and choose Enter.Value Date: for example, <current date>Expiration Date: for example, <current date+ n days>Note Expiration date shall be later than the value date. If value date is earlier than current date, and expiration date is also earlier than current date, system will prompt warning message accordingly while saving a memo record, plus the memo record generated will be with inactive status.Bank Account: Use Search Help (F4) to find the bank account.Planning Group: for example, A6Note In case of Planning Level for Bank Accounting Bank the field Bank Account is mandatory.In case of Planning Level for Subledger Accounting the field Planning Group is mandatory. If the field Planning Group is not displayed on the screen, you choose Enter.House Bank: <keep empty or maintain as needed>House Bank Account: <keep empty or maintain as needed>Note If only one connectivity path is maintained in bank account master, they shall be auto-filled (company code herein is the one in the connectivity path) after bank account determination. If multiple connectivity paths are maintained, you can specify one via manual filling or F4 with the bank account tech ID. |  |  |
| 5 | Enter Additional Data (Optional) | Make the following entries and choose Enter:Offsetting Company Code: 3310Offsetting Bank Account: <maintain as needed>Offsetting Value Date: <current date>Offsetting House Bank: <maintain as needed>Offsetting House Bank Account: <maintain as needed>Note These fields are only relevant to Planning Level for Bank Accounting Bank. |  |  |
| 6 | Create | Choose Create.Choose Close to confirm the further information screen. | A new memo record is successfully created.Make a note of the memo record ID. |  |
| 7 | Account Transfer (Optional) | Choose Account Transfer to create a new memo record for offsetting bank account if you have maintained offsetting bank account in last step.Note Specify offsetting information before you perform the account transfer. | A new memo record is created for the offsetting bank account. |  |

##### Copy Memo Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can copy the memo record.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Memo Records (F2986). |  |  |
| 3 | Enter Search Criteria | Make the following entries and choose Go:Company Code: for example, 3310Planning Level: for example, AUStatus: Active | A list of memo records are displayed. |  |
| 4 | Check Memo Record Details | Choose one Memo record to display. |  |  |
| 5 | Copy Memo Record | Choose Copy. Make the following entries in the dialog box and choose Copy:Number of Copies (Including Original Memo Record): for example, 3Recurrence Pattern: for example: Every 10 Day(s)Note Determines the increment in days, weeks or months for the memo record copy function.On Non-Working Days: <No Restriction> or change it per your needs | The memo record gets copied based on the specified conditions. The amount of each of the memo record copies is identical with the original memo record amount. |  |

##### Distribute Memo Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can distribute the memo record.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Memo Records (F2986). |  |  |
| 3 | Enter Search Criteria | Make the following entries and choose Go:Company Code: for example, 3310Planning Level: for example, AUStatus: Active | A list of memo records is displayed. |  |
| 4 | Check Memo Record Details | Choose one Memo record to display. |  |  |
| 5 | Distribute Memo Record | Choose Distribute. Make the following entries in the dialog box and choose Distribute:Number of Copies (Including Original Memo Record): for example, 3Recurrence Pattern: for example: Every 4 daysNote Determines the increment in days, weeks or months for the memo record copy function.On Non-Working Days: <No restriction> or other value per your needs | The memo record gets copied based on the specified conditions. The amount of each of the memo record copies is equal to the distributed amount in terms of the original memo record amount and increments defined. |  |

##### Memo Record List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you manage the memo records of the cash position and the liquidity forecast. The system displays the memo records in a list. You can select an individual record for the following actions, for example, Display, Edit, Delete and Deactivate.

In the list, you can select memo records to transfer them afterward into an archive. After they are archived, the records are no longer relevant to the cash position and liquidity forecast, and the status of these records changes to Inactive.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Memo Records (F2986). |  |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Company Code: for example 3310Planning Level: for example, AUStatus: Active | A list of memo records are displayed. You can find the memo records you created in the previous steps. |  |
| 4 | Display | Choose a memo record from this list. The detailed information of this memo record are displayed on the next view.Choose Back. |  |  |
| 5 | Edit | Choose a memo record in this list. The detailed information of this memo record will be displayed on the next view. Choose Edit. You can change the following editable values, for example, Amount, Expiration Date and so on.Choose Save.Choose Back. | The memo record is changed. |  |
| 6 | Deactivate | Choose one or more memo record with status Active, then choose Deactivate. | Thee memo records are deactivated. The status of the memo records change to Inactive. |  |
| 7 | Activate | On the Manage Memo Records view, make the following entries and choose Go:Status: InactiveChoose one or more memo records in this list and choose Activate. | Thee memo records are activated. The status of the memo records change to Active. |  |
| 8 | Delete | On the Manage Memo Records view and make the following entries and choose Go:Status: ActiveChoose a memo record from the list. Choose Delete. On the Delete object?, choose Delete. | You deleted the memo record. The memo record shall disappear from the list of memo records. |  |

#### Memo Record 2.0

Purpose

With the App Manage Memo Records 2.0 (F2986A), you can create memo records for actual and forecasted cash flows that are not yet generated in the system. The memo records are then displayed in the cash management apps to provide an up-to-date and accurate view of your organization's cash position, such as Short-Term Cash Positioning, Cash Flow Analyzer, and Check Cash Flow Items.

Prerequisite

To use this app, make sure you have made the following settings in your configuration environment:

- Define Memo Record Types: Define memo record types and assign these types to predefined memo record categories. You can refer to the [Define Memo Record Types](#unique_10) [page ] 14 procedure in the Preliminary Steps.
- (Optional) Manage Field Status Groups for Memo Records: You can use configuration activity Manage Field Status Groups for Memo Record Imports to create field status groups for different types of memo record.

|  |
| --- |
| Note In cash flow reconciliation, you can create memo records of the category Residual Forecast to represent residual flows that need to be considered in the next round of cash flows reconciliation. For more information, see Reconcile Cash Flows - Intraday procedure in the Advanced Cash Operations (J78) test script. |

##### Create Memo Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create memo records.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cash Management Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Memo Records 2.0 (F2986A). |  |  |
| 3 | Create Memo Record | Choose Create. In the dialog box, make the following entries and choose Continue.Company Code: 3310Memo Record Type: for example, AU or MPNote The memo record type without category is not allowed. |  |  |
| 4 | Enter General Information | Make the following entries:Value Date: for example, <current date>Bank Account ID: Use Search Help (F4) to find the bank accountAmount in Transaction Currency: for example, 1600 AEDPlanning Group: for example, A6Note In case of Payment Advice or Actual Flow Memo category, the field Bank Account ID is mandatory.In case of Planned Item category, the field Planning Group is mandatory. | The memo record is created. |  |
| 5 | Enter Additional Data (Optional) | Make the following entries and choose Enter:Offsetting Company Code: 3310Offsetting Bank Account ID: <as needed>Offsetting Value Date: <current date>Offsetting House Bank: <as needed>Offsetting House Bank Account: <as needed>Note These fields are only relevant to Planning Level for Bank Accounting Bank. |  |  |
| 6 | Create | Choose Create. |  |  |
| 7 | Account Transfer (Optional) | Choose Account Transfer to create a new memo record for offsetting bank account if you have maintained offsetting bank account in last step.Note Specify offsetting information before you perform the account transfer. |  |  |

##### Import Memo Records

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can import the memo records 2.0 into the system.

|  |
| --- |
| Note You must use the predefined template to prepare the memo record data you are about to import. To import memo records, you now have the following 2 templates:Download Template by Type: With this option, you can download a template specific to a particular memo record type and upload memo records for this memo record type.Download Generic Template: With this option, you can download a generic template that accommodates multiple memo record types. With this template, you can easily view the defined memo record types in your system along with the current field status settings for each of them. It helps you prepare data for multiple memo record types in one file, so that you can upload memo records with different types in one go. |

|  |
| --- |
| Note The migration object SIF_MEMO_RECORD has deprecated. Please use the Import Memo Records 2.0 (F6124) app to migrate memo records. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Import Memo Records 2.0 (F6124). |  |  |
| 3 | Opton1) Download Template with Single Memo Record Type | Choose Download Template by Type. On the Download Template dialog box, enter the specific one memo record type (for example, AU or MP), then choose Download.Note Specify a valid memo record type for the memo records to be imported.Note down the XLSX file name, for example, MemoRecord_Template_E.xlsx. | The template is downloaded with the specific one memo record type and the file is saved on your local PC. We will upload this file later. |  |
| 4 | Opton2) Download Template with Multiple Memo Record Types | Choose Download Generic Template. Note down the XLSX file name, for example, MemoRecord_Template_E.xlsx. | The template is downloaded with all valid memo record types and the file is saved on your local PC. We will upload this file later. |  |
| 5 | Edit Excel File | Find the excel file downloaded in previous step on your local PC.For example, file name MemoRecord_Template_E.xlsx.Open the excel file with Excel and enter the value for the fields.For example,Option1 ) Template by Type:Template by Type: <the memo record type mentioned in previous step>, for example, AU or MPOnly list one memo record type to be uploaded. All memo records can be created for the same memo record type.Edit the following mandatory fields for each item:Company Code: 3310Amount in Transaction Currency: <as needed>Value Date: <Value Date>Bank Account ID: <Bank Account ID>Planning Group: for example, E2 Domestic customersMaintain other fields as needed.Note You can unhide row to display technical names.Make sure you enter valid values for all mandatory fields.In case of Payment Advice or Actual Flow Memo category, the field Bank Account ID is mandatory. In case of Planned Item category, the field Planning Group is mandatory.Option2) Generic TemplateIn row 2, enter memo record type as following:Memo Record Type: <all memo record types for the memo records to be imported>Note You must enter all memo record types that you plan to upload in the designated cell first. Make sure the memo record types are separated by commas without spaces.Edit the following mandatory fields for each item starting from Row 23:For example,Company Code: 3310Amount in Transaction Currency: <as needed>Value Date: <Value Date>Bank Account ID: <Bank Account ID>Planning Group: for example, E2 Domestic customersMaintain other fields as needed.NoteWhen you input data for different memo record types, check the field status settings for the memo record types relevant to your import. Make sure mandatory fields are entered for each memo record type.The system lists each memo record type as separate entries, each associated with an import batch ID. The import of a file will only succeed if all data is imported successfully. |  |  |
| 6 | Upload File | Choose Upload File. In the Upload File dialog box, select above excel file from your local PC and choose Import. | The memo records are uploaded successfully. The status of memo should be Uploaded Successfully. |  |
| 7 | Check Log Details | Choose > to check log details. | The log details displays.Note If any memo record in the file encounters a problem during the import, the entire upload will fail, and no memo records will be imported. The result of the import will be either Uploaded Successfully or Upload Failed for all memo records in the file. Even if an error affects just one memo record type, it will appear in the import log for all memo record types, helping users easily identify and resolve issues. |  |
| 8 | Back | Choose Back. |  |  |
| 9 | Check Memo Records | Choose View Memo Records for the relevant item to check memo uploaded. |  |  |

##### Schedule Jobs for Deactivating Memo Records 2.0

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this app, you can use filters to select memo records and set their status to Deactivated in one go. This feature helps manage memo records more efficiently, especially when you need to replicate memo records across system. For example, you might have enabled the automatic expiration function for memo records in your current system. However, when these records are replicated to other systems through the Cash Flow - Inbound Service API (CASHFLOW_IN), the expiration information is not transferred. This app allows you to deactivate expired memo records, preventing them from being considered valid in the target system. This feature reduces manual effort in deactivating invalid memo records and mitigates risks associated with handling them in interconnected systems.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Jobs for Deactivating Memo Records 2.0 (F8915). |  |  |
| 3 | Create a New Application Job | On the current view, choose Create to create an application job. | The New Job: Deactivation of Memo Records view displays. |  |
| 4 | Choose Job Template | In the Template Selection section, make the following entries:Job Template: Deactivation of Memo RecordsJob Name: Deactivation of Memo Records |  |  |
| 5 | Maintain Scheduling Options | Choose Step 2. In the Scheduling Options section, make the following entries:Start Immediately: <Selected or deselected>Note If you choose start immediately, you don't need to maintain other parameters.Start: <current time or any future time as needed>Time Zone: <time zone>For Recurrence Pattern, choose Define Recurrence Pattern.In the Scheduling Information dialog box, the additional scheduling options are available.Recurrence Pattern: for example, WeeklyEvery: for example, 1On: for example, MondayEnd: <Optional>On Non-Working Day: <Optional>Calendar: for example, Germany(Standard)Choose OK. | If you would like to run this job immediately, the checkbox of Start Immediately should be selected.If you schedule this job at some time in the future, the Start and Time Zone should be defined. |  |
| 6 | Enter Control Parameters | Choose Step 3. In the Parameter section, make the following entries:General Selections sectionCompany Code: for example, 3310Memo Record Category: <select as needed>Memo Record Type: <enter specific memo records type>Value Date: <enter specific value date>Expired By SectionDate: <select as needed>Time: <select as needed>Time Zone: <select as needed>Note This allows you to select memo records that are expired by the specified date and time.Processing Option sectionTest Run: <Deselected> | Parameters are maintained. |  |
| 7 | Check | Choose Check. |  |  |
| 8 | Run this Application Job | Choose Schedule to run this application job. |  |  |
| 9 | Check Application Jobs Log | Choose Go to update the job status. When your job’s status change to Finished, you choose Log to navigate to the log details. | Job log displays.Note You check the logs and correct it as needed. |  |
| 10 | Check Results | Choose Back. Then choose Results > Preview , check the output results. | All relevant memo records are listed. |  |

#### Correct Value Date

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can check the list of value dates to be corrected and correct the incorrect value dates and planning dates of the selected document items. By selecting the Automatic Correction function, you can automatically correct the incorrect value dates and planning dates of all the selected document items. By selecting the Display Log function, you can display the application log. By selecting the Persist Log function, you can save the application log.

Prerequisites

Please make sure the relevant condition for value date correction is defined in the preliminary step.

|  |
| --- |
| Note If you want to trigger the correction. Please make sure you have posted a FI cash flow for which the difference between the posting date and the value date has exceeded the defined tolerance.For example, in our testing case, tolerance is greater than 30 days for house bank AEBK1 under company code 3310. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Value Date Correction (FCLM_VALUT_CORR). | The Value Date Correction view is displayed. |  |
| 3 | Enter Parameter | Make the following entries and choose Run:SelectionsCompany Code: 3310Fiscal Year: <current fiscal Year>Posting period: <empty>Posting Date: <empty>G/L Account: <empty>House Bank: AEBK1Account ID:<empty>ControlAutomatic Correction: <selected>Message LoggingDisplay Log: <selected>Persist Log: <as needed> | The Display logs screen displays. You can check which items are included for the value date correction.Note You can also correct value date via App Schedule Job for Value Date Correction (F6679). |  |

#### Cash Reports

Context

The section centrally introduces how to execute reports Cash Position and Liquidity Forecast.

##### Cash Flow Analyzer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After payments are executed, you can view the aggregated amounts and line item details of cash position, medium-and-long term liquidity forecast, and actual cash flows. You can analyze cash flows over days. The data presented in the app can be used to give a high-level overview and detailed insight into the cash flow status to the management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Cash Flow Analyzer (F2332). | The Cash Flow Analyzer view displays. |  |
| 3 | Maintain User Setting | On the upper right corner, choose your user, choose User Settings. On the dialog box, maintain your user setting and choose OK. |  |  |
| 4 | Enter Selection Criteria | Choose Adapt Filters if the filter selection fields are hidden.Maintain selection criteria and choose Go.Company Code: for example, 3310Time Period: for example, D14Currency: for example, AEDDate: <Today>Date Indicator: for example, Value DateBank Account: for example, bank account with house bank/Account ID:AEBK1/AEAC1Note Select the default report between Cash Position, Liquidity Forecast and Actual Cash Flows, or create your own variant. | The list is filtered and displays all related entries for the time period. |  |
| 5 | Switch Views | Choose Switch Views and from the dropdown select Delta View and choose OK.Repeat this step to return to the Balance View.Remember Balance View displays opening balance, outflows & inflows, and closing balance. Delta View displays only outflows & inflows. | The view switches.Note For this test script, no hierarchy can be displayed. The Display Hierarchy function is only available for Advanced Cash Operations(J78) test script. |  |
| 6 | Expand Hierarchy | On the Cash Flows table, expand the hierarchy Currency > Company Code > Bank Account. | Display a list of cash flows in the View Settings variant in the structure of Currency > Company Code > Bank Account, or create your own variant. |  |
| 7 | Display Cash Flow Items | Select an amount highlighted in blue, choose Display Cash Flow Items view. Then you can also navigate to Check Cash Flow Items by choosing > (Details).Note In Balance View, only In/Out Flows can do Display Cash Flow Items navigation; Balance flows can’t navigate. | The Cash Flow Items view displays. |  |
| 8 | Adjust Layout. | Select the Settings icon.On the View Settings dialog box, select additional columns.and choose OK. | The table updates with the additional selections. |  |
| 9 | Export to Spreadsheet | Choose the Export to Spreadsheet icon. | All of the current table contents are exported to a spreadsheet. |  |

#### Cash Tools

##### Schedule Jobs for Cash Register (Optional)

Purpose

In this step, you can schedule jobs for cash register using the template and scheduling options provided. There are two job templates: Initialize Cash Register and Run Cash Register. When you first select Enable Cash Register in the Define Basic Settings configuration activity, it’s suitable for you to use the Initialize Cash Register job template to replicate data to Cash Register and the FQM_FLOW table in One Exposure. After you have initialized Cash Register for a certain company code, you can use the Run Cash Register job template to build cash related data to Cash Register and the FQM_FLOW table in One Exposure.

Prerequisites

You need to enable cash register in the Preliminary Steps.

###### Initialize Cash Register

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Job for Cash Register (F8948). |  |  |
| 3 | Create a New Application Job | On the current view, choose Create to create an application job. | The New Job: Flow Builder view displays. |  |
| 4 | Choose Job Template | In the Template Selection section, make the following entries:Job Template: Initialize Cash RegisterJob Name: Initialize Cash RegisterNote When you first select Enable Cash Register in the Define Basic Settings configuration activity, it’s suitable for you to use the Initialize Cash Register job template to replicate data to Cash Register and the FQM_FLOW table in One Exposure. |  |  |
| 5 | Maintain Scheduling Options | Choose Step 2. In the Scheduling Options section, make the following entries:Start Immediately: <Selected or deselected>Note If you choose start immediately, you don't need to maintain other parameters.Start: <current time or any future time as needed>Time Zone: <time zone>For Recurrence Pattern, choose Define Recurrence Pattern.In the Scheduling Information dialog box, the additional scheduling options are available.Recurrence Pattern: for example, WeeklyEvery: for example, 1On: for example, MondayEnd: OptionalOn Non-Working Day: OptionalCalendar: for example, Germany(Standard)Choose OK. | If you would like to run this job immediately, the check box of Start Immediately should be selected.If you schedule this job at some time in the future, the Start and Time Zone should be defined. |  |
| 6 | Enter Control Parameters | Choose Step 3. In the Parameter section, make the following entries:General Selections sectionCash Reg Running Type: for example, Cash Position:Mass Run for Financial AccountingNote Different running types correspond to different sets of fields.Test Run: for example, <deselected>Build Flows in One Exposure: for example, <selected>Derive sectionDerive from Paramter Config: <select as needed>Derive Flow Type in Cash Reg: <select as needed>Derive Plng Data in Cash Reg: <select as needed>Derive Lqdy Item in Cash Reg: <select as needed>Derive Bk Acct Dta in Cash Reg: <select as needed>Technical Option sectionPackage Size: <change as needed>Log Level: <change as needed>Parallel Run: <selected as needed>FI Selection Criteria sectionCompany Code: <as needed> | Parameters are maintained. |  |
| 7 | Check | Choose Check. | Note If the error message Cash Register has been activated, but all compan ies have been initialized appears, it means you do not need to initialize the cash register again. |  |
| 8 | Run this Application Job | Choose Schedule to run this application job. |  |  |
| 9 | Check Application Jobs Log | Choose Go to update the job status. When your job’s status change to Finished you choose Log status to navigate to the Job Log. | Job log displays.Note You check the logs and correct it as needed. |  |

###### Run Cash Register

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Job for Cash Register (F8948). |  |  |
| 3 | Create a New Application Job | On the current view, choose Create to create an application job. | The New Job: Flow Builder view displays. |  |
| 4 | Choose Job Template | In the Template Selection section, make the following entries:Job Template: Run Cash RegisterJob Name: Run Cash RegisterNote After you have initialized Cash Register for a certain company code, you can use the Run Cash Register job template to build cash related data to Cash Register and the FQM_FLOW table in One Exposure. |  |  |
| 5 | Maintain Scheduling Options | Choose Step 2. In the Scheduling Options section, make the following entries:Start Immediately: <Selected or deselected>Note If you choose start immediately, you don't need to maintain other parameters.Start: <current time or any future time as needed>Time Zone: <time zone>For Recurrence Pattern, choose Define Recurrence Pattern.In the Scheduling Information dialog box, the additional scheduling options are available.Recurrence Pattern: for example, WeeklyEvery: for example, 1On: for example, MondayEnd: OptionalOn Non-Working Day: OptionalCalendar: for example, Germany(Standard)Choose OK. | If you would like to run this job immediately, the check box of Start Immediately should be selected.If you schedule this job at some time in the future, the Start and Time Zone should be defined. |  |
| 6 | Enter Control Parameters | Choose Step 3. In the Parameter section, make the following entries:General Selections sectionRunning Type: for example, Cash Position: Mass Run for Financial AccountingNote Different running types correspond to different sets of fields.Test Run: for example, <deselected>Enable Expert Mode: <selected>Expert Mode section:Replicate from Accounting: <selected>Derive from Paramter Config:<selected>Technical Option sectionPackage Size: <change as needed>Log Level: <change as needed>Parallel Run: <selected as needed>FI Selection Criteria sectionCompany Code: <as needed>Fiscal Year: <as needed>Document Number: <as needed>G/L Account: <as needed>Document Date: <as needed>Posting Date: <as needed>Document Type: <as needed> | Parameters are maintained. |  |
| 7 | Check | Choose Check. | Note If the error message Cash Register has been activated, but all compan ies have been initialized appears, it means you do not need to initialize the cash register again. |  |
| 8 | Run this Application Job | Choose Schedule to run this application job. |  |  |
| 9 | Check Application Jobs Log | Choose Go to update the job status. When your job’s status change to Finished, you choose Log status to navigate to the Job Log. | Job log displays.Note You check the logs and correct it as needed. |  |

##### Create Initial Balance Adjustment with Reference

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Create Initial Balance and Balance Adjustment with Reference (FQM_INTBAL_AUTOCRT) app can be used to support automatic creation of initial balance data. The initial balance data can be set from different sources (closing bank statement, G/L account and FQM Balance Table). On the other hand, more filter fields will be provided to create initial balance data with different dimension.

Prerequisites

You need to create actual cash memo in the Preliminary Steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP App | Open Create Initial Balance and Balance Adjustment with Reference (FQM_INTBAL_AUTOCRT). |  |  |
| 3 | Maintain Control Parameter | In the Control section, make the following entries:Flow Creation Mode: for example, Create Initial BalanceDate Dimension: for example, Transaction Date & FI Posting DateMemo Record Type: for example, IFNote Only memo record type with category Initial Balance Flows can be used.In the Technical Control section, make the following entries:Test Run: <Deselected>Show Result: Show Appliation Log |  |  |
| 4 | Maintain Selection Criteria | In the Selection Criteria section, make the following entries:Company Code: 3310Bank Key: <as needed>Country/Region Key: AEBank Account Technical ID: <as needed>Bank Account Number:<as needed>Bank Account Type:<as needed>Bank Account Status:<as needed>House Bank: for example AEBK1House Bank Account ID: for example AEAC1Bank Account Currency:<as needed>Note Search criteria depends on the account dimension selected in the above step. |  |  |
| 5 | Choose Balance | In the Balance From section, select one balance and choose Run:Bank Statement: <as needed>G/L Account Balance:<as needed>Value Date Balance in FQM Bal: <as needed>Ledger Balance in FQM Bal: <as needed>Note Value Date Balance in FQM balance not supported for posting date. | Logs are displayed for initial balance data creation. |  |

##### Schedule Job for Initialize One Exposure Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this app, you can schedule jobs for Program Initialize One Exposure Data using the template and scheduling options provided. You can define the scheduling options and parameters for initializing One Exposure Data and check the results of the job.

With this job, you can load transaction data from source applications into One Exposure from Operations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Jobs for Flow Builder (F3804). |  |  |
| 3 | Create a New Application Job | On the current view, choose Create to create an application job. | The New Job:Flow Builder view displays. |  |
| 4 | Choose Job Template | In the Template Selection section, make the following entries:Job Template: Schedule Job for Initialize One Exposure DataJob Name: Schedule Job for Initialize One Exposure Data |  |  |
| 5 | Maintain Scheduling Options | Choose Step 2. In the Scheduling Options section, make the following entries:Start Immediately: <Selected or deselected>Note If you choose star immediately, other parameter do not need to maintain.Start: <current time or any future time as needed>Time Zone: <time zone>For Recurrence Pattern, choose Define Recurrence Pattern.In the Scheduling Information dialog box, the additional scheduling options are available.Recurrence Pattern: for example, WeeklyEvery: for example, 1On: for example, MondayEnd: OptionalOn Non-Working Day: OptionalCalendar: for example, Germany(Standard)Choose OK. | If you would like to run this job immediately, the check-box of Start Immediately should be selected.If you schedule this job at some time in the future, the Start and Time Zone should be defined. |  |
| 6 | Enter Control Parameters | Choose Step 3. In the Parameter section, make the following entries:General Selections sectionCompany Code: for example, 3310Source Application Selections sectionNote At least one source application should be selected in the following options:TreasuryContract AccountingLiquidity Item TransferCustomer and Mortgage LoansPayment RequestReal EstateSales and Distribution OrderTechnical Setting sectionTest Run: <Deselected>Specific Selections sectionIn this section, according to the source application selections, enter the value for the specific fields per your requiremen. | Parameters are maintained. |  |
| 7 | Check | Choose Check. |  |  |
| 8 | Run this Application Job | Choose Schedule to run this application job. |  |  |
| 9 | Check Application Jobs Log | Choose Go to update the job status. When your job’s status change to Finished, you choose Log to navigate to the Job Log. | Job log displays.Note You check the logs and correct it as needed. |  |

##### Aggregate Flows

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Aggregate Flows (FQM_AGGREGATE_FLOWS) app serves a data privacy protection purpose. To simplify the blocking and deletion of personal data, you can delete flows in One Exposure from Operations. You can delete flows with ACTUAL certainty level in One Exposure and substitute them with aggregation flows that do not contain any person-related information. In addition, you can also physically delete all flows that are marked as deleted (FQM_FLOW-DELETED ='X'). As a result, the data volume in One Exposure is further reduced.

Prerequisite

You have defined start date for one exposure in the Define Start Date for One Exposure procedure in the Preliminary Steps section of the [Prerequisites](#unique_2) [page ] 5.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Aggregate Flows (FQM_AGGREGATE_FLOWS). | The Aggregate Flows by Start Date screen displays. |  |
| 3 | Enter Criteria | Make the following entries and choose Run:Company Code: 3310Aggregate Period: <Selected>In the Aggregation Period Ahead of Start Date section:Number of Period: for example: 15Aggregation Frequency: for example: DailyChoose Yes to confirm the dialog box if needed. | Logs are displayed. |  |

##### Display Cash Management Logs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The application log is a tool that collects messages, exceptions, and errors. This information is organized and displayed in a log.

When you update information from source applications into One Exposure, the One Exposure from Operations application log collects errors that occurred during these updates. System administrators can review and evaluate these application logs by source application for a specific time period. After error resolution, the business users reload data into the One Exposure from Operations hub.

However, if the application log shows an error message, you need to contact the system administrator to correct the root cause and then trigger the update of One Exposure again.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Display Cash Management Logs (F4991). |  |  |
| 3 | Enter Selection Criteria | From the current view, make the following entries and choose Go:Severity: OptionalDate From -To: <the current date>Category: for example, FQM_CORENote The Category FQM_CORE indicates a financial accounting related transaction.Subcategory: for example, TRANSFER,LOADNote If Category ID and Subcategory ID are not in the current view, change the layout by choosing Settings. | The application logs are displayed with the selected categories. |  |
| 4 | View the Detailed Logs | Use Creation Date and Created By to filter the log to review, and then select that line in the application log to view the details. | The Log Details view displays. |  |

##### Schedule Jobs for Health Check

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can use this app to schedule the health check jobs for cash management applications.

The report shows the validation results of checks on data that are consumed by cash management applications, including configuration settings, master data, and transactional data. You can then correct the settings or data entries as necessary.

- Configuration settings, such as planning levels and planning groups
- Master data, such as bank accounts and house bank accounts
- Transactional data stored in the One Exposure from Operations hub

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist . |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Jobs for Health Check (F3030). |  |  |
| 3 | Create a New Application Job | On the current view, choose Create to create an application job. | The New Job: Health Check view displays. |  |
| 4 | Choose Job Template | In the Template Selection section, make the following entries:Job Template: Health CheckJob Name: Health Check |  |  |
| 5 | Maintain Scheduling Options | Choose Step 2. In the Scheduling Options section, make the following entriesStart Immediately: <Selected or deselected>Note If you choose star immediately, other parameter do not need to maintain.Start: <current time or any future time as needed>Time Zone: <time zone>For Recurrence Pattern, choose Define Recurrence Pattern.In the Scheduling Information dialog box, the additional scheduling options are available.Recurrence Pattern: for example, WeeklyEvery: for example, 1On: for example, MondayEnd: OptionalOn Non-Working Day: OptionalCalendar: for example, Germany(Standard)Choose OK. | If you would like to run this job immediately, the check-box of Start Immediately should be selected.If you schedule this job at some time in the future, the Start and Time Zone should be defined. |  |
| 6 | Check Parameter | Choose Step 3, check profile as following:Profile: 0FULL |  |  |
| 7 | Check | Choose Check. |  |  |
| 8 | Run this Application Job | Choose Schedule to run this application job. |  |  |
| 9 | Check Application Jobs Log | Choose Go to update the job status. When your job’s status change to Finished, you choose Log to navigate to the Job Log. | Job log displays.Note After application job is executed successfully, some Error, Information or Success messages display in the job log. Check the error message and correct your customizing or house bank master data accordingly. |  |

##### Schedule Jobs for Health Check - with Free Selections

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can schedule health check jobs to check data related to cash management, including configuration data, master data, and transaction data. With the health check results, you can then correct configuration settings and clean up inconsistencies in master data and transaction data to ensure your cash management applications run correctly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist . |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Jobs for Health Check (F5285). |  |  |
| 3 | Create a New Application Job | On the current view, choose Create to create an application job. | The New Job: Schedule Health Check for Cash Management – With Free Selection view displays. |  |
| 4 | Choose Job Template | In the Template Selection section, make following entries:Job Template: Health Check for Cash Management – With Free SelectionJob Name: Health Check for Cash Management - With Free Selection |  |  |
| 5 | Maintain Scheduling Options | Choose Step 2. In the Scheduling Options section, make the following entriesStart Immediately: <Selected or deselected>Note If you choose star immediately, other parameter do not need to maintain.Start: <current time or any future time as needed>Time Zone: <time zone>For Recurrence Pattern, choose Define Recurrence Pattern.In the Scheduling Information dialog box, the additional scheduling options are available.Recurrence Pattern: for example, WeeklyEvery: for example, 1On: for example, MondayEnd: OptionalOn Non-Working Day: OptionalCalendar: for example, Germany(Standard)Choose OK. | If you would like to run this job immediately, the check-box of Start Immediately should be selected.If you schedule this job at some time in the future, the Start and Time Zone should be defined. |  |
| 6 | Maintain Parameter | Choose Step 3. In Parameter section and make the following entries:General Information:Company code: For example: 3310House Bank Account: For example: AEAC1House Bank: For example: AEBK1Note If you keep parameters empty, that means all cases will be included in the job.Configurations:Planning Levels and Groups: <selected>House Banks and Bank Accounts: <selected>Master Data:House Bank Accounts in G/L: <selected>Planning Levels and Groups: <selected>Bank Account Assignment to G/L: <selected>Transaction Data:Bank Accts in Bank Statements: <selected>Bank Accounts in One Exposure: <selected>Note You can select or deselect check points as needed. | Parameters are maintained. |  |
| 7 | Check | Choose Check. |  |  |
| 8 | Run this Application Job | Choose Schedule to run this application job. |  |  |
| 9 | Check Application Jobs Log | Choose Go to update the job status. When your job’s status change to Finished, you choose Log to navigate to the Job Log. | Job log displays.Note After application job is executed or Success messages display, check the Error message and correct your customizing or house bank master data accordingly. |  |
| 10 | Create and Schedule Application Job of Health Check for Bank Accounts | Repeat steps from 3-9, make following entries to create and schedule application job of health check for bank accounts:Template Selection section:Job Template: Health Check for Bank AccountsJob Name: Health Check for Bank AccountsParameters section:General Information:Company code: For example: 3310House Bank Account: For example: AEAC1House Bank: For example: AEBK1Bank Account Contract Type: <empty>Note If you want to select Bank Account Contract Type, you need to enable bank account contract type first. You can refer to the Enable Bank Account Contract Types procedure of the scope item J77 Advanced Bank Account Management.Master Data:Bank Accounts: <selected> | Application job for health check for bank accounts is scheduled. |  |

##### Bank Account Balance Reconciliation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can identify differences between the bank account balance, the G/L account balance, and the balance in One Exposure from Operations, in order to process necessary corrections.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist . |  |  |
| 2 | Access the SAP Fiori App | Open Bank Account Balance Reconciliation (FCLM_BNK_AC_RECONCIL). | The Bank Account Balance Reconciliation view displays. |  |
| 3 | Enter Selection Criteria | On the current page, make the following entries and choose Run:GeneralCompany Code: 3310Reconciliation Date: <current date>Accounting ScopeAccounting Scope: Cash PositionBankHouse Bank: for example, AEBK1House Bank Acc Id: AEAC1OutputDisplay Currency: AEDExchange Rate Type: MConversion Date: <current date>Differences Only: <as needed>Absolute Delta: <Selected> | The comparison result displays according to the selected data sources. |  |

##### Bank Account Balance Reconciliation with Drill Down

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can identify differences between the bank account balance, the G/L account balance, and the balance in One Exposure from Operations, in order to process necessary corrections.

You can also use the drill down function by selecting the balance, which shows the detail content from document line items (table BSEG) and cash flows (table FQM_FLOW).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Bank Account Balance Reconciliation with Drill Down (FCLM_BANK_RECONCIL). | The Bank Account Balance Reconciliation With Drill Down view displays. |  |
| 3 | Enter Selection Criteria | On the current page, make the following entries and choose Run:OptionsAccount Dimension: for example Bank Account(House Bank/House Bank Account)Reconciliation Date: <current date>Calc. Date as per One Expos.: <as needed>Only Show Difference: <as needed>Max.Rows on Details Page: <default value>Search CriteriaCompany Code: 3310Note Maintain other fields as needed.Data Source SelectionBank Statement: <Selected>G/L Account Balance: <Selected>Acct Bal in Cash Pos(Post Dt) :<Selected>Acct Bal in Cash Pos(Tran Dt) : <Deselect>Acct Bal in Liq .Anly(Post Dt) : <Selected>Acct Bal in Liq.Anly (Tran Dt) : <Deselect>BSEG+Cash Pos – Post.Date : <Deselect>BSEG+Liq.Anlys – Post.Date : <Deselect>Acct Bal. in FQM Balance: <as needed>Risk Management: <Deselect>Note Select or deselect the fields as needed. | The result displays according to the selected data sources. |  |
| 4 | Drill Down to details | Choose one item and double click the item. | The details screen displays |  |
| 5 | Navigate to Document | Choose one item and double click the item. | The document displays. |  |

##### Schedule Job for Rebuild Flow Type of Accounting Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can schedule job for rebuild flow types in accounting documents (BSEG), the purpose is to get the cash related field inserted or updated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist . |  |  |
| 2 | Schedule Job for Rebuild Flow Type of Accounting Documents | Open Schedule Job for Rebuild Flow Type of Accounting Documents (F6799). |  |  |
| 3 | Create a New Application Job | On the current view, choose Create to create an application job. | The New Job: Schedule view displays. |  |
| 4 | Choose Job Template | In the Template Selection section, make following entries:Job Template: Rebuild Flow Types in Accounting DocumentsJob Name: for example：Rebuild Flow Types in Accounting Documents |  |  |
| 5 | Maintain Scheduling Options | Choose Step 2. In the Scheduling Options section, make the following entriesStart Immediately: <Selected or deselected>If you choose star immediately, other parameter do not need to maintain.Start: <current time or any future time as needed>Time Zone: <time zone>For Recurrence Pattern, choose Define Recurrence Pattern.In the Scheduling Information dialog box, the additional scheduling options are available.Recurrence Pattern: for example, WeeklyEvery: for example, 1On: for example, MondayEnd: OptionalOn Non-Working Day: OptionalCalendar: for example, Germany(Standard)Choose OK. | If you would like to run this job immediately, the check-box of Start Immediately should be selected.If you schedule this job at some time in the future, the Start and Time Zone should be defined. |  |
| 6 | Maintain Parameter | Choose Step 3. In Parameter section and make the following entries:Accounting Document section:Company code: For example: 3310Fiscal Year: <current year>Note Maintain other fields as needed.Control Parameters section:Rebuild Flows for Chged Items: <selected>Test Run: <as needed>Display Changed Items Only: <as needed>Technical Setting section:Package Size: <change as needed>Parallel Run: <as needed> | Parameters are maintained. |  |
| 7 | Check | Choose Check. |  |  |
| 8 | Run this Application Job | Choose Schedule to run this application job. |  |  |
| 9 | Check Application Jobs Log | Choose Go to update the job status. When your job’s status change to Finished, you choose Log navigate to the Job Log. | Job log displays. |  |

##### Rebuild House Banks and Account IDs in Accounting Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this app, you can schedule jobs for the program Insert House Bank and House Bank Account Data to Table BSEG using the template and scheduling options provided. If you want to use historical cash management data in the Cash Management applications, you need to run the program to insert house bank and house bank account data into table BSEG before you use the applications. You only have to run this program once for inserting the house bank and bank account data from historical transactions. After the program finishes, it displays the number of the rows that are updated.

|  |
| --- |
| Note If the house bank and house bank account are not updated according to the sources: bank statements, payments for open items, payments for payment requests, the app will derive the house bank and house bank account according to the G/L account when Addit. Bank Account Derivation is enabled. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Jobs for Flow Builder (F3804). |  |  |
| 3 | Create a New Application Job | On the current view, choose Create to create an application job. | The New Job:Flow Builder view displays. |  |
| 4 | Choose Job Template | In the Template Selection section, make the following entries:Job Template: Rebuild House Bank and Account IDs in Accounting DocumentsJob Name: Rebuild House Bank and Account IDs in Accounting Documents |  |  |
| 5 | Maintain Scheduling Options | Choose Step 2. In the Scheduling Options section, make the following entries:Start Immediately: <Selected or deselected>Note If you choose star immediately, other parameter do not need to maintain.Start: <current time or any future time as needed>Time Zone: <time zone>For Recurrence Pattern, choose Define Recurrence Pattern.In the Scheduling Information dialog box, the additional scheduling options are available.Recurrence Pattern: for example, WeeklyEvery: for example, 1On: for example, MondayEnd: OptionalOn Non-Working Day: OptionalCalendar: for example, Germany(Standard)Choose OK. | If you would like to run this job immediately, the check-box of Start Immediately should be selected.If you schedule this job at some time in the future, the Start and Time Zone should be defined. |  |
| 6 | Maintain Parameters | Choose Step 3. In Parameter section and make the following entries:Accounting Document:Company Code: 3310G/L Account: <empty>Fiscal Year: <empty>Note Maintain other fields as needed.Sources:Payment Request (PAYRQ): <selected>Settlement Data from Paymt Prg: <selected>Bank Statement (FEBKO, FEBEP): <selected>Addit. Bank Account Derivation: <keep default>Technical Settings:Test Run: <deselected>Rebuild Flows for Changed Item: <keep default>Note If you select the checkbox Rebuild Flows for Changed Item, the program will add eligible FI documents into FI staging table. Flow Builder will update the house bank and house bank account for related FI flows according to the staging table. | Parameters are maintained. |  |
| 7 | Check | Choose Check. |  |  |
| 8 | Run this Application Job | Choose Schedule to run this application job. |  |  |
| 9 | Check Application Jobs Log | Choose Go to update the job status. When your job’s status change to Finished, you choose Log to navigate to the Job Log. | Job log displays.Note You check the logs and correct it as needed. |  |

##### Transfer Open Item Accounts to Cash Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can rebuild planning levels and planning groups for open item in accounting documents .

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist . |  |  |
| 2 | Access the SAP App | Open Planning Correction (OT30). | The Planning Correction view displays. |  |
| 3 | Maintain Selections | Make the following entries as needed and choose Run.Selection Criteria sectionCompany Code: for example: 3310Fiscal Year: <current year>Account Type: <as needed>Note Maintain other fields as needed.Control Parameters sectionTest Run: <as needed>Rebuild Flows for Changed Item: <selected>Package Size: <change as needed>Show Result: <change as needed>Persist Log: <as needed> | The open item accounts is transferred to cash management. |  |

##### Schedule Jobs for Flow Builder

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this app, you can schedule jobs for the cash flow builder using the template and scheduling options provided. Normally, the flow builder runs automatically to derive cash flows and relevant information from accounting line items (Financial Operations) and Material Management (MM) and store the results to the One Exposure from Operations hub for analytical purposes. You only need to use this app to rebuild cash flows after flow builder upgrades

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Jobs for Flow Builder (F3804). |  |  |
| 3 | Create a New Application Job | On the current view, choose Create to create an application job. | The New Job:Flow Builder view displays. |  |
| 4 | Choose Job Template | In the Template Selection section, make the following entries:Job Template: Flow BuilderJob Name: Flow Builder |  |  |
| 5 | Maintain Scheduling Options | Choose Step 2. In the Scheduling Options section, make the following entriesStart Immediately: <Selected or deselected>Note If you choose star immediately, other parameter do not need to maintain.Start: <current time or any future time as needed>Time Zone: <time zone>For Recurrence Pattern, choose Define Recurrence Pattern.In the Scheduling Information dialog box, the additional scheduling options are available.Recurrence Pattern: for example, WeeklyEvery: for example, 1On: for example, MondayEnd: OptionalOn Non-Working Day: OptionalCalendar: for example, United Arab EmiratesChoose OK. | If you would like to run this job immediately, the check-box of Start Immediately should be selected.If you schedule this job at some time in the future, the Start and Time Zone should be defined. |  |
| 6 | Enter Control Parameters | Choose Step 3. In Parameter section and make the following entries:Control ParametersRunning Type: for example, Cash Position:Delta Run from StagingNote Running Type defines how Flow Builder processes the data from source applications. Different Running Type will require different fields to maintain.Package Size: for example, 200,000Log Level: for example, NormalParallel Run: <deselected>Test Run: <deselected> | Parameters are maintained. |  |
| 7 | Check | Choose Check. |  |  |
| 8 | Run this Application Job | Choose Schedule to run this application job. |  |  |
| 9 | Check Application Jobs Log | Choose Go to update the job status. When your job’s status change to Finished, you choose Log to navigate to the Job Log. | Job log displays.Note You check the logs and correct it as needed. |  |

##### Schedule Jobs for Flow Builder Utility Toolset

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can schedule jobs for Flow Builder/Cash Register Utility Toolset using the template and scheduling options provided.

It contains the following action items to assist Flow Builder/Cash Register main functionalities:

- Find Missing Cash Flow Items

With this function, you can find missing cash flow items that are supposed to be in One Exposure. If you enable the Cash Register, this tool will also identify the missing documents for Cash Register. In the Activate Individual Source Applications configuration activity, if your company code is not activated as Source Application: Accounting, the missing cash flow items or documents will not be considered. In the Define Source Application Accounting configuration activity, if your company code's Update Mode is set to Deferred - No Delta Table Update, the missing cash flow items or documents will not be considered.

- Find Unexpected Cash Flow Items

With this function, you can find the unexpected cash flow items that appear in One Exposure but should not be there. In the Activate Individual Source Applications configuration activity, if your company code is not activated as Source Application: Accounting, the unexpected cash flow items will not be considered. In the Define Source Application Accounting configuration activity, if your company code's Update Mode is set to Deferred - No Delta Table Update, the unexpected cash flow items will not be considered.

- Delete Invalid Delta Entries

Identify and remove invalid FI staging entries based on the Flow Builder configuration.

- Delete Invalid Cash Register Entries

Identify and remove invalid cash register entries based on Flow Builder configuration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Jobs for Flow Builder Utility Toolset (F8949). |  |  |
| 3 | Create a New Application Job | On the current view, choose Create to create an application job. | The New Job: Flow Builder view displays. |  |
| 4 | Choose Job Template | In the Template Selection section, make the following entries:Job Template: Flow Builder Utility ToolsetJob Name: Flow Builder Utility Toolset |  |  |
| 5 | Maintain Scheduling Options | Choose Step 2. In the Scheduling Options section, make the following entries:Start Immediately: <Selected or deselected>Note If you choose start immediately, you don't need to maintain other parameters.Start: <current time or any future time as needed>Time Zone: <time zone>For Recurrence Pattern, choose Define Recurrence Pattern.In the Scheduling Information dialog box, the additional scheduling options are available.Recurrence Pattern: for example, WeeklyEvery: for example, 1On: for example, MondayEnd: OptionalOn Non-Working Day: OptionalCalendar: for example, Germany(Standard)Choose OK. | If you would like to run this job immediately, the check box of Start Immediately should be selected.If you schedule this job at some time in the future, the Start and Time Zone should be defined. |  |
| 6 | Enter Control Parameters | Choose Step 3. In the Parameter section and make the following entries:Toolset sectionFind Missing Cash Flow Items: for example, <selected>Find Unexpected Cash Flow Itms: <selected as needed>Delete Invalid Delta Entries: <selected as needed>Delete Invalid Cash Reg.Entr.: <selected as needed>Note Different Tool will require different fields to maintain.Selection Option sectionCompany Code: for example, 3310Fiscal Year: for example, <Current Year>Document Number: <as needed>G/L Account: <as needed>Entry Date: <as needed>Check Account: <selected as needed> | Parameters are maintained. |  |
| 7 | Check | Choose Check. |  |  |
| 8 | Run this Application Job | Choose Schedule to run this application job. |  |  |
| 9 | Check Application Jobs Log | Choose Go to update the job status. When your job’s status change to Finished, you choose Log status to navigate to Job Log. | Job log displays. |  |

##### Schedule Jobs for Planning Fields Rebuilding

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this app, you can schedule jobs for Program Planning Correction using the template and scheduling options provided. You can update the planning fields of accounting documents, payment requests and payment orders. It contains updates of Planning Group, Planning Level, and Planning Date.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Jobs for Flow Builder (F3804). |  |  |
| 3 | Create a New Application Job | On the current view, choose Create. | The New Job:Flow Builder view displays. |  |
| 4 | Choose Job Template | In the Template Selection section, make the following entries:Job Template: SAPJ Template for planning correctionJob Name: SAPJ Template for planning correction |  |  |
| 5 | Maintain Scheduling Options | Choose Step 2. In the Scheduling Options section, make the following entriesStart Immediately: <Selected or deselected>Note If you choose star immediately, other parameter do not need to maintain.Start: <current time or any future time as needed>Time Zone: <time zone>For Recurrence Pattern, choose Define Recurrence Pattern.In the Scheduling Information dialog box, the additional scheduling options are available.Recurrence Pattern: for example, WeeklyEvery: for example, 1On: for example, MondayEnd: OptionalOn Non-Working Day: OptionalCalendar: for example, United Arab EmiratesChoose OK. | If you would like to run this job immediately, the check-box of Start Immediately should be selected.If you schedule this job at some time in the future, the Start and Time Zone should be defined. |  |
| 6 | Enter Control Parameters | Choose Step 3. In the Parameter section and make the following entries:Company Code:for example: 3310Fisical Year: <as needed>Account Type: <keep default>Posting Date.: <as needed>Note In the Selection Criteria section, maintain criteria fields as needed.Test Run: <as needed>Rebuild Flows for Changed Item: <selected>Package Size: for example, 200.000 | Parameters are maintained. |  |
| 7 | Check | Choose Check. |  |  |
| 8 | Run this Application Job | Choose Schedule to run this application job. |  |  |
| 9 | Check Application Jobs Log | Choose Go to update the job status. When your job’s status change to Finished, you choose Log to navigate to the Job Log. | Job log displays.Note Note You check the logs and correct it as needed. |  |

##### Delete Data from One Exposure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can delete transactional data in One Exposure from Operations to ensure data protection and privacy. The deleted data will no longer be displayed in cash management apps which consume data stored in One Exposure from Operations. You can use different deletion types.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP App | Open Delete Data from One Exposure (FQM_DELETE). | The Delete Data from One Exposure from Operations Hub view displays. |  |
| 3 | Maintain Deletion Type | In the Deletion Type section, make the following entries:Delete: <as needed>Delete Flagged Entries Only: <as needed>Snapshot Cleanup: <as needed>Mass Delete Memo Records: <as needed>Delete IBU flows: <as needed> |  |  |
| 4 | Maintain Selections | In the Selections section, make the following entries:Source Application (Group): <as needed>Source Application: <as needed>Company Code: 3310Transaction Date: <as needed>G/L Account: <as needed>Note The selection fields will be changed according to deletion type.Test Run: <selected> |  |  |
| 5 | Message Logging | Display Log: <as needed> |  |  |
| 6 | Run | Choose Run. | The data is deleted according to the selected deletion type. |  |

##### Schedule Job to Delete Data from One Exposure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this app, you can also schedule job to delete data from one exposure.

|  |
| --- |
| Note Another daily scheduled background job SAP_FQM_DELETE_REGULAR (configured by variant) also will automatically delete the flagged entries which has not been updated for at least 14 days. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Job for Delete Data from One Exposure (F5936). | The Schedule Jobs for FQM_DELETE view displays. |  |
| 3 | Create a New Application Job | On the current view, choose Create to create an application job. | The New Job: Schedule job for FQM_DELETE template view displays. |  |
| 4 | Choose Job Template | In the Template Selection section, make the following entries:Job Template: Schedule job for FQM_DELETE templateJob Name: Schedule job for FQM_DELETE template |  |  |
| 5 | Maintain Scheduling Options | Choose Step 2. In the Scheduling Options section, make the following entries：Start Immediately: <Selected or deselected>Note If you choose start immediately, other parameter do not need to maintain.Start: <current time or any future time as needed>Time Zone: <time zone>For Recurrence Pattern, choose Define Recurrence Pattern.In the Scheduling Information dialog box, the additional scheduling options are available.Recurrence Pattern: for example, WeeklyEvery: for example, 1On: for example, MondayEnd: OptionalOn Non-Working Day: OptionalCalendar: for example, United Arab EmiratesChoose OK. | If you would like to run this job immediately, the check-box of Start Immediately should be selected.If you schedule this job at some time in the future, the Start and Time Zone should be defined. |  |
| 6 | Maintain Deletion Type | In the Deletion Type section, make the following entries:Delete Flagged Entries Only: <as needed>Snapshot Cleanup: <as needed> | Parameters are maintained. |  |
|  | Maintain Selections | In the Selections section, make the following entries:Source Application (Group): <as needed>Source Application: <as needed>Company Code: 3310Transaction Date: <as needed>G/L Account: <as needed>Test Run: <selected>Note The selection fields will be changed according to deletion type. |  |  |
| 7 | Check | Choose Check. |  |  |
| 8 | Run this Application Job | Choose Schedule to run this application job. |  |  |
| 9 | Check Application Jobs Log | Choose Go to update the job status. When your job’s status change to Finished, you choose Log to navigate to the Job Log. | Job log displays.Note You check the logs and correct it as needed. |  |

##### Delete Bank Statement Flow from One Exposure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can delete transactional data of bank statement flows in One Exposure from Operations to ensure data protection and privacy. The deleted data of bank statement flows will no longer be displayed in Cash Management reports that consume data stored in One Exposure from Operations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP App | Open Delete Data from One Exposure (FQM_DELETE). |  |  |
| 3 | Choose Special Deletion for Bank Statement Flow | Choose Special Deletion for BS Flow. | The Delete Bank Statement Flows from One Exposure view displays. |  |
| 4 | Maintain Selection | Make the following entries and choose Run:From Bank Statement and One Exposure sectionCompany Code: 3310Short Key: <as needed>House Bank: <as needed>Account ID: <as needed>G/L Account: <as needed>From Bank Statement sectionBank Statement Number: <as needed>Statement Date: <as needed>From Bank sectionBank Country/Region: for example: AEBank Key: <as needed>Technical Settings sectionTest Run: <deselected> | The relevant bank statement flow is deleted from one exposure. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following test scripts:

| Process | Business Condition |
| --- | --- |
| Accounts Receivable (J59) | After a bank statement is imported and posted , though not absolutely necessary, you may find that you have to post process a bank statement. This occurs when not all statement items are cleared by the system automatically. Post processing can occur when the customer has not paid the total amount, or has quoted the wrong reference. When these happen, no clearing posting is carried out and, consequently, reprocessing is necessary.Follow the steps in the Reprocess Bank Statement Items procedure. |

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
- related-to :: [[05-treasury-and-cash-management/advanced-cash-operations-j78-ae-test-script-sap-s-4hana-cloud-public-e-part-01]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BFB_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 157,063 chars in the whole document
