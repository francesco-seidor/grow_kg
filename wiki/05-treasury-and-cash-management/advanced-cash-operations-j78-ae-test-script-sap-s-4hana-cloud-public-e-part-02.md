---
id: 05-treasury-and-cash-management/advanced-cash-operations-j78-ae-test-script-sap-s-4hana-cloud-public-e-part-02
title: Advanced Cash Operations (J78_AE) Test Script - SAP S/4HANA Cloud Public Edition (J78_S4CLD2608_BPD_EN_AE) — part 2 of 2
description: "SAP S/4HANA Cloud 2608 (AE) test script J78, part 2: step-by-step Fiori tests for bank balances, reconciliation, snapshots, monitors and cash reports."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/cash-operations]
aliases: []
keywords: [Cash Operations and Cash Positioning, bank account balances, cash flow reconciliation, cash snapshots, instant balances, liquidity item transfer, situation handling, bank statement monitor, intraday bank statements, short-term cash positioning]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J78_S4CLD2608_BPD_EN_AE.docx#lines-3313-4596"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1309
topic: 05-treasury-and-cash-management/cash-operations
language: EN
part: 2/2
created: 2026-10-12
updated: 2026-10-12
---

# Advanced Cash Operations (J78_AE) Test Script - SAP S/4HANA Cloud Public Edition (J78_S4CLD2608_BPD_EN_AE) — part 2 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J78_S4CLD2608_BPD_EN_AE.docx`, part 2 of 2 (lines 3313–4596 of the extracted text), extracted with `mammoth`. Grouped under **Cash Operations and Cash Positioning** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| Note For current release, this step is only for Cash Trade Request for FX. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Memo Records (F2986). |  |  |
| 3 | Search Cash Trade Request | Make the following entries and choose Go.Company Code: 3310Certainty Level: Cash Trade RequestCash Trade Request Status: T(In Process)/ F(Completed)Note Choose Adapt Filters to add the fields as filter if needed. | The cash trade requests are displayed. |  |
| 4 | Check Cash Trade Request | Select a cash trade request to check. | The cash trade request status is updated as In Process or Completed. |  |
| 5 | Check Trade Request | Click Trade Request number which is highlighted with Blue. | Trade Request detailed information is displayed. |  |

### Manage Bank Account Balances

Purpose

You can manually enter or import balances for bank accounts and monitor the balance changes of these accounts.

The Manage Bank Account Balances app is able to receive bank account balance data from imported end-of-day bank statements. In addition to bank accounts managed in remote systems, now you can also use this app to manage bank account balances for bank accounts that are managed in your central system.

|  |
| --- |
| Note Bank account balances received from imported bank statements are displayed with the Update Method of Electronic Bank Statements. The balances are stored by the bank statement dates contained in the bank statements. For each date, if there is already a balance entry updated by electronic bank statements, the balance is not allowed to be updated via spreadsheet import or manual entry. |

Prerequisite

To display bank account balances from imported bank statements, the bank accounts must be defined with one of the following transfer modes:

- Balance Only
- Balance and Bank Statement Items

If you want to manually enter bank account balances or import bank account balances via a spreadsheet, in the next steps, you need to enable Balance from Manual Entry and Balance from spreadsheet Import.

For more information about this setting, see step Define Bank Account Settings – Bank Statements or Integrate with End-of-Day Bank Statements in the Basic Bank Account Management ([BFA](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/BFA)) test script.

#### Schedule Jobs for Bank Account Balance Initialization (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Some bank account balances may not show up in cash management, for example the Short-Term Cash Positioning (F5380) app, even though bank statements have been imported. With this app, you can schedule jobs to identify these bank accounts and replicate bank account balances from their latest end-of-day bank statements to cash management. You are recommended to use this app to initialize bank account balances for bank accounts to ensure the accuracy of short-term cash positions.

Procedure

Balance initialization can only be performed for bank accounts for which the transfer mode is defined as Balance Only or Balance and Bank Statement Items. For more information about this setting, see step Define Bank Account Settings – Bank Statements in the Basic Bank Account Management ([BFA](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/BFA)).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist . |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Jobs for Bank Account Balance Initialization (F7146). |  |  |
| 3 | Create a New Application Job | On the current view, choose Create to create an application job. | The Application Jobs view displays. |  |
| 4 | Choose Job Template | In the Template Selection section, make following entries:Job Template: Bank Account Balance InitializationJob Name: Bank Account Balance Initialization |  |  |
| 5 | Maintain Scheduling Options | Choose Step 2. In the Scheduling Options section, make the following entries:Start Immediately: <Selected or deselected>Note If you choose star immediately, other parameter do not need to maintain.Start: <current time or any future time as needed>Time Zone: <time zone>For Recurrence Pattern, choose Define Recurrence Pattern.In the Scheduling Information dialog box, the additional scheduling options are available.Recurrence Pattern: for example, WeeklyEvery: for example, 1On: for example, MondayEnd: OptionalOn Non-Working Day: OptionalCalendar: for example, Germany(Standard)Choose OK. | If you would like to run this job immediately, the check-box of Start Immediately should be selected.If you schedule this job at some time in the future, the Start and Time Zone should be defined. |  |
| 6 | Maintain Parameter | Choose Step 3. In Parameter section and make the following entries:Selection Parameters section:Free Selection: <Selected>Company Code: For example: 3310Account Type: <empty>Note You can select Free Selection or Cash Position Profile.Date section:Last Bank Statement Before: current dateAdjust Balance for Past: for example, 14Processing Option section:Test Run : <deselected> | Parameters are maintained. |  |
| 7 | Check | Choose Check. |  |  |
| 8 | Run this Application Job | Choose Schedule to run this application job. |  |  |
| 9 | Check Application Jobs Log | Choose Go to update the job status. When your job’s status change to Finished, you choose Log icon to navigate to the job details. | The log details display.Note After application job is executed , check the Warning/Error message and correct your customizing or house bank master data accordingly. |  |
| 10 | Check Jobs Result | Choose Result to navigate to the job results. | The job result displays. |  |
| 11 | Check Balance | Open Manage Bank Account Balances (F5175) to check balances generatedby this report. | The balance channel of these balance is marked as Initial Load from EBS. |  |

#### Create Bank Account Balances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can manually enter balances for bank accounts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Account Balances (F5175). | The Manage Bank Account Balance view displays. |  |
| 3 | Create Bank Account Balance | Choose Create. In the Enter Balance for Bank Account dialog box, make the following entries and choose Create:Technical ID: <choose a house bank via value help>Statement Date: <current date>Balance Amount: 3500.00 | The balance of bank account is created. |  |
| 4 | Check in Cash Flow Analyzer | Use your bank account and refer to procedure Cash Flow Analyzer. |  |  |
| 5 | Check in Short Term Cash Position | Use your bank account and refer to procedure Short Term Cash Position. | The balance of your bank account displays. |  |

#### Import Bank Account Balances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can upload Excel file for Balance of Bank Accounts, so that the Balance of relevant Bank Accounts can be updated massively.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Account Balances (F5175). | The Manage Bank Account Balances view displays. |  |
| 3 | Navigate to Import Bank Account Balances | Choose Import. | The Import Bank Account Balances view displays. |  |
| 4 | Download Template | Choose Download Template. | The template is download in your local PC. |  |
| 5 | Edit Template file | Open the template file in your local PC and maintain the value per your bank account. |  |  |
| 6 | Import Bank Account Balances | Select above excel file from your local PC to import. | The balance of bank account imported. |  |
| 7 | Check in Cash Flow Analyzer | Refer to procedure Cash Flow Analyzer. |  |  |
| 8 | Check in Short Term Cash Position | Refer to procedure Short Term Cash Position. | The balance of your bank account displays. |  |

#### Edit Bank Account Balances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can edit bank account balances for a bank account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Account Balances (F5175). | The Manage Bank Account Balance view displays. |  |
| 3 | Check Bank Account Balance list | Make the following entries and choose Go:Account Number: <choose a bank account via value help>Company Code: <your company code> | The balance of bank account list displays. |  |
| 4 | Check Bank Account | Choose > to navigate to check balance history. |  |  |
| 5 | Edit Bank Account Balance | Choose Edit. Change Closing Balance as needed and choose Save. | The balance of your bank account edited. |  |

#### Check Bank Account Balances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can show the difference between ledger balance and value date balance.

There are three kinds of balance types supported in the Manage Bank Account Balance app: Ledger balance, value date balance, available balance.

If the bank account balance is imported from a bank statement, then the value date balance is calculated based on the ledger balance from the bank statement. For a bank statement item whose value date is greater than the bank statement date, the amount will not be considered. It means the formula is: value date balance + predated flow = ledger balance. However, if there is no future date item, then value date balance = ledger balance. Therefore, the display predated flows will help the customer better understand how the value date balance is calculated.

If the bank account balance is manually entered via Manage Bank Account Balance, then only the value date balance and the available balance will be created, and the amount will be the same.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Account Balances (F5175). | The Manage Bank Account Balance view displays. |  |
| 3 | Check Bank Account Balance list | Make the following entries and choose Go:Account Number: <choose a bank account via value help>Company Code: <your company code> | The balance of bank account list displays.Note There are two tabs named End of Day and Intraday. The table buttons will change based on the tab. The End of Day will be shown by default. |  |
| 4 | Check Intraday balance for Bank Account (Optional) | Choose tab Intraday. | Note Intraday balances can only be checked if intraday or instant balances have been uploaded for the bank account. For upload instructions, see the Upload Intraday Bank Statement procedure in Bank Integration with File Interface (1EG) for instant balance updates, refer to the [Instant Balances (Optional)](#unique_137) [page ] 176 procedure in this document. | The latest intraday balances of bank accounts will be displayed. You can navigage to App Monitor Instant Balances (F7804). |
| 5 | Check Balance History | Choose > to check balance history. |  |  |
| 6 | Check Balance History Details | Select one balance item, choose > to check balance history details. | Three balance types displays. The ledger balance and value date balance, and the difference between ledger balance and value date balance may display. |  |
| 7 | Check Details for Value Date Balance | Choose value date balance, chose choose > to check value date balance details.Note Detailed information is available for value date balances only. | The value date balance details displays. |  |

### Cash Flows Reconciliation

Purpose

You can manually reconcile bank statement flows with forecasted cash flows. This feature enables you to compare your intraday or end-of-day bank statements with your forecasts before end of business. This way, you can easily identify unfinished and unknown payments in time. It also helps you eliminate duplicate items in forecasts to gain a more accurate account of your cash positions. In addition, you can leverage the automatic reconciliation app, Schedule Jobs for Cash Flow Reconciliation (F5283), prior to performing manual reconciliation. This combination simplifies and accelerates your reconciliation tasks, reducing the manual effort required and enhancing overall productivity.

Check the reconciliation result in the Short-Term Cash Positioning (F5380) app.

|  |
| --- |
| Note Cash flows with the following certainty levels are considered forecasted cash flows in reconciliation with end-of-day bank statements:General memo records 2.0 (certainty level MEMO, source application MRMM2)Residual flows (certainty level RFC)Self-initiated cash in transit (certainty level SI_CIT, source application BSEGV)Regular receivables (certainty level REC_N, source application BSEGV)Regular payables (certainty level PAY_N, source application BSEGV)End-of-day bank statements::Forecasted FI flows have the prerequisite that accounting scope should be Cash Position Only or Cash Position & Liquidity Analysis. But memo records 2.0 and residual forecast still can be used even when the scope is liquidity analysis only.The reconciliation results for both end-of-day reconciliation and intraday reconciliation are consumed by the following apps:Short-Term Cash Positioning (F5380)In the Define Cash Position Profiles (F5399) app, you can use the options Consider End-of-Day Recon. Result and Consider Intraday Recon. Result to decide whether to exclude reconciled forecasted flows from the Short-Term Cash Positioning (F5380) app.When the reconciliation result is considered, reconciled forecasted flows are excluded from the Short-Term Cash Positioning (F5380) app because they have already been reconciled by bank statement flows and should not be considered in cash positioning.Check Cash Flow Items (F0735)In this app, you can use the filters Consider End-of-Day Recon. Result and Consider Intraday Recon. Result to hide or display reconciled forecasted flows.When the reconciliation result is considered, reconciled forecasted flows are hidden from the Check Cash Flow Items (F0735) app because they have already been reconciled by bank statement flows.Manage Cash Concentration (F3265) & Schedule Jobs for Cash Concentration (F3688)Reconciled forecasted flows are automatically excluded from these apps to avoid duplicate flows. |

Prerequisite

Before testing this step, ensure that you have completed the following steps. Some steps that must be completed as prerequisites are described in other test scripts.

- Preliminary Steps

You have completed the steps in the Cash Flow Reconciliations procedure in the Preliminary Steps section.

- Define Planning Levels for Bank Statements

Make sure you have defined the planning level for end-of-day and intraday bank statements in procedure Define Planning Levels for Bank Statements of the Basic Cash Operations test script.

- Create Forecast Cash Flows (Optional)

Ensure open forecast cash flows exist. One Exposure derives cash forecasts for items representing receivables, payables, or cash in transit, memo record 2.0 and so on.

- Upload Intraday Bank Statement and Generated Intraday Memo Record

The relevant intraday memo records are automatically generated after importing intraday bank statements.

You can follow the Upload Intraday Bank Statement procedure in the Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/1EG)).

|  |
| --- |
| Note Only Camt.052 format is supported to generate intraday memo record. |

|  |
| --- |
| Note If the default Memo Record Type is not assigned for Intraday Bank Statement in preliminary step Define Planning Levels for Bank Statements, the intraday memo record will not be created. You can update cash position via Manage Bank Statements (F1564) later. |

|  |
| --- |
| NoteAfter a new intraday bank statement is imported for a certain bank account, the system generates an intraday memo record. If there is already an active intraday memo record that was generated before the current date under this bank account, the system automatically deactivates the old intraday memo record into the inactive status to eliminate duplicate data.When an end of day bank statement is imported for a certain bank account, any active intraday memo record under this bank account before the current date, the system automatically will deactivate the old intraday memo record into the inactive status to eliminate duplicate data. |

- Upload EoD Bank Statement and Transfer Bank Statement Items to Cash Management (Optional)

You can follow the Upload Bank Statement procedure in the Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/1EG)).

|  |
| --- |
| Note Make sure the transfer mode is set as Balance and Bank Statement Items. |

#### Schedule Automated Cash Flow Reconciliation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can schedule jobs to perform automatic reconciliation between bank statement flows and forecasted cash flows. This feature enables you to compare your intraday or end-of-day bank statements with your forecasts, allowing you easily identify unfinished and unknown payments in time and gain a more accurate view of your cash positions. In addition, you can use this app together with the manual reconciliation app Reconcile Cash Flows (F3418A), to check the results of automatic reconciliation and make corrections and updates if necessary. This combination speeds up the reconciliation process while ensuring the accuracy of reconciliation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Jobs for Cash Flow Reconciliation (F5283). | The Schedule Jobs for Cash Flow Reconciliation view displays. |  |
| 3 | Create a New Application Job | On the current view, choose Create to create an application job. |  |  |
| 4 | Choose Job Template | In the Template Selection section, make following entries:Job Template: Schedule New Cash ReconciliationJob Name: Schedule New Cash Reconciliation (Intraday BS) |  |  |
| 5 | Maintain Scheduling Options | Choose Step 2. In the Scheduling Options section, make the following entries:Start Immediately: <Selected or deselected>Note If you select Start Immediately, you don't need to maintain other parameters.Start: <current time or any future time as needed>Time Zone: <time zone>For Recurrence Pattern, choose Define Recurrence Pattern.In the Scheduling Information dialog box, the additional scheduling options are available.Recurrence Pattern: for example, WeeklyEvery: for example, 1On: for example, MondayEnd: OptionalOn Non-Working Day: OptionalCalendar: for example, Germany(Standard)Choose OK.Note If you would like to run this job immediately, the checkbox of Start Immediately should be selected.If you schedule this job at some time in the future, the Start and Time Zone should be defined. |  |  |
| 6 | Maintain Parameter | Choose Step 3. In Parameter section and make the following entries:Reconciliation Rules sectionReconciliation Profile: For example, INTRA_PROFReconciliation Strategy: <display only>Exchange Rate Type: For example, MReconciliation Step 1: For example, Match by Company Code, Bank Account, Value Date, Doc. AmountReconciliation Step 2: <As needed>Reconciliation Step 3: <As needed>Note You can also choose customer rule. You can use the BAdI Custom Rules for Automatic Cash Flow Reconciliation (the extension point ID: BADI_FCLM_RCN_AUTOMATIC_MATCH) to design your own custom rules for automatic cash flow reconciliation between bank statement flows and forecasted cash flows. The custom rules can be used in this app.Selection Criteria sectionCompany Code: For example: 3310House Bank: <house bank>NoteMaintain other fields as needed.Document Range is a required field for reconciliation rule Document Number Search Based on Note to Payee.Reference Document Range is a required field for reconciliation rule Reference Document Number Search Based on Note to Payee.If you keep parameters empty, that means all cases will be included in the job.Processing Option sectionTest Run: <deselected> | Parameters are maintained. |  |
| 7 | Check | Choose Check. |  |  |
| 8 | Run this Application Job | Choose Schedule to run this application job. |  |  |
| 9 | Check Application Jobs Log | Choose Go to update the job status. When your job’s status changes to Finished, you choose Log to check job log. | The job log displays. |  |
| 10 | Cash Reconciliation for EoD Bank Statement | Repert step 3 – 9, schedule jobs for cash reconciliation for EoD Bank Statement as following:1. Template SelectionJob Template: Schedule New Cash ReconciliationJob Name: Schedule New Cash Reconciliation(EoD BS)2. Schedule Options: same as step 53. ParametersReconciliation Rules sectionReconciliation Profile: For example, EoD_PROFReconciliation Strategy: <display only>Exchange Rate Type: For example, MReconciliation Step 1: For example, Match by Company Code, Bank Account, Value Date, Doc. AmountReconciliation Step 2: <As needed>Reconciliation Step 3: <As needed>Selection Criteria sectionCompany Code: For example: 3310House Bank: <house bank>Value Date From(Forecasts): Start Date - 15 Day(s)Value Date To(Forecasts): Start Date + 15 Day(s)Note Maintain other fields as needed.Processing Option sectionTest Run: <deselected> | The job for cash reconciliation for EoD Bank Statement is scheduled. |  |

#### Review Reconciliation Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You review reconciliation results.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Reconcile Cash Flows (F3418A). | The Reconcile Cash Flows view displays. |  |
| 3 | Selection Criteria | Choose Adapt Filters if selection fields are hidden.Make the following entries and choose Go:Reconciliation Profile: for example, INTRA_PROF or EoD_PROFExchange Rate Type: MValue Date(Bank Stmt Flows): <value date for bank statement>Value Date (Forecasts): Today -7/+2 DaysAccount Number: For example, 2580061Company Code: 3310Reconciliataion Status: <as needed> | The reconciliation status of all relevant bank accounts is monitored.NoteReconciled: The bank statement flows of this bank account are completely reconciled with forecasted cash flows.Unreconciled: Some bank statement flows of this bank account are not yet reconciled.Not Applicable: The bank account has not been reconciled and currently no bank statement flows are available for reconciliation. |  |
| 4 | Choose Details | Choose > (Details). |  |  |
| 5 | Review Reconciliation Results | Choose the Reconciliation Bundles tab to verify the reconciled pairs. | The Bank statement flows and the forecasted cash flows are reconciled. |  |

#### Undo Reconciliation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can undo reconciliations for selected items and reset them to the open status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Reconcile Cash Flows (F3418A). | The Reconcile Cash Flows view displays. |  |
| 3 | Selection Criteria | Choose Adapt Filters if selection fields are hidden.Make the following entries and choose Go:Reconciliation Profile: for example, INTRA_PROF or EoD_PROFExchange Rate Type: MValue Date: <value date for bank statement>Value Date (Forecasts): This MonthAccount Number: For example, 2580061Company Code: 3310Reconciliataion Status: For example, Reconciled | Bank accounts with status reconciled are listed. |  |
| 4 | Choose Details | Choose > (Details). |  |  |
| 5 | Unreconcile | In the Reconciliation Bundles tab, select any items that are not matched together and choose Undo Reconciliation at up-right corner. | The reconciliation chains are broken and any of those items of this reconciliation group are reset to open, making them available for further matching.Note If it is relevant to residual cash flow, residuals also are updated. |  |
| 6 | Verify Unreconciliation | Choose the Unreconciled Cash Flows tab to verify the items are reset to open to reconcile. | Unreconciled bank statement flows and unreconciled forecasted flows display. |  |

#### Reconcile Unmatched Transactions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can manually reconcile intraday or end-of-day bank statement flows with forecasted cash flows.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Reconcile Cash Flows (F3418A). | The Reconcile Cash Flows view displays. |  |
| 3 | Selection Criteria | Choose Adapt Filters if selection fields are hidden.Make the following entries and choose Go:Reconciliation Profile: for example, INTRA_PROF or EoD_PROFExchange Rate Type: MValue Date(Bank Stmt Flows): <value date for bank statement>Value Date (Forecasts): Today -7/+2 DaysAccount Number: For example, 2580061Company Code: 3310Reconciliataion Status: For example, Unreconciled | The reconciliation status of all relevant bank accounts is monitored.NoteReconciled: The bank statement flows of this bank account are completely reconciled with forecasted cash flows.Unreconciled: Some bank statement flows of this bank account are not yet reconciled.Not Applicable: The bank account has not been reconciled and currently no bank statement flows are available for reconciliation. |  |
| 4 | Choose Details | Choose > (Details). |  |  |
| 5 | Select Bank Statement Flows | Choose Unreconciled Cash Flows tab, in the Unreconciled Bank Statement Flows area on the right side of the page, select one or more items. |  |  |
| 6 | Select Forecasted Flows | In the Unreconciled Forecasted Flows area on the left side of the page, choose the relevant forecast cash flows. |  |  |
| 7 | Perform Reconciliation with Residual(option1) | Choose Reconcile. In the Reconcile popup screen Residual Amount is calculated and displayed. You can manually change it and add comment. Then choose Confirm.Note The Proposed amount is generated as residual cash flow which is considered in next reconciliation exection. |  |  |
| 8 | Perform Reconciliation without Residual(option 2) | Or choose Reconcile Without Residual. In the Reconcile Without Residual popup screen, no Proposed Amount is calculated. Then choose Confirm. |  |  |
| 9 | Verify Reconciliation | Choose the Reconciliation Bundles tab to verify the reconciled pairs. | The Bank statement flows and the forecasted cash flows are reconciled. |  |

#### Analyze Cash Position

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After cash flow reconciliation, you can analyze the cash positions.

Procedure

Run the [Short Term Cash Positioning](#unique_121) [page ] 195 step using the Short-Term Cash Positioning (F5380) app.

### Cash Snapshot Management

Purpose

You can manage cash snapshots using the new app Manage Cash Snapshots (F8962) and Schedule Jobs for Cash Snapshots (F8945). A cash snapshot is a set of cash-related data marked with a specific timestamp, capturing details such as cash flows and bank account balances. It can be used to track and analyze your historical cash data.

You can load captured snapshots for analysis using the Short-Term Cash Positioning (F5380) app.

|  |
| --- |
| Note In the configuration activity Define Basic Settings (101025), check the setting Days for Recorded Snapshot.This setting defines the retention period for cash flow snapshots, including the current date. A technical background job automatically deletes cash flows that fall outside this period. Once the associated cash flows are deleted, the related cash snapshot will be changed to the status Invalid and it will no longer be displayable. Therefore, please consider this setting carefully when defining the retention period for cash flow snapshots. |

#### Analyze Cash Position

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Before capturing the cash snapshot, analyze the cash position.

Procedure

Run the [Short Term Cash Positioning](#unique_121) [page ] 195 step using the Short-Term Cash Positioning (F5380) app.

#### Schedule Cash Snapshots Capture

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can schedule jobs for capturing or deleting cash snapshots using the template and scheduling options provided. You can also view the status and results of your jobs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Jobs for Cash Snapshots (F8945). | The Schedule Jobs for Cash Snapshots view displays. |  |
| 3 | Create a New Application Job | On the current view, choose Create to create an application job. |  |  |
| 4 | Choose Job Template | In the Template Selection section, make the following entries:Job Template: Capture Cash SnapshotsJob Name: Capture Cash Snapshots for <current date> |  |  |
| 5 | Maintain Scheduling Options | Choose Step 2. In the Scheduling Options section, make the following entries:Start Immediately: <Selected or deselected>Note If you select Start Immediately, you don't need to maintain other parameters.Start: <current time or any future time as needed>Time Zone: <time zone>For Recurrence Pattern, choose Define Recurrence Pattern.In the Scheduling Information dialog box, the additional scheduling options are available.Recurrence Pattern: for example, WeeklyEvery: for example, 1On: for example, MondayEnd: OptionalOn Non-Working Day: OptionalCalendar: for example, Germany (Standard)Choose OK.Note If you would like to run this job immediately, the checkbox of Start Immediately should be selected.If you schedule this job at some time in the future, the Start and Time Zone should be defined. |  |  |
| 6 | Maintain Parameter | Choose Step 3. In the Parameter section and make the following entries:Selection Criteria sectionCash Position Profile: For example, <CPP_01, defined in preliminary steps>Snapshot Purpose: <Cash Position or Liquidity Analysis>Snapshot Description Definition sectionSegment Type 1: For example, AttributeAttribute 1: For example, Cash Position ProfileSegment Type 2: For example, AttributeAttribute 2: For example, Key DateSegment Type 3: For example, Free Input TextText 3: <your free text>Note For snapshots that were captured through scheduled jobs, the descriptions are generated based on job settings, which may include the cash position profile, key date, or user-defined texts. | Parameters are maintained. |  |
| 7 | Check | Choose Check. |  |  |
| 8 | Run this Application Job | Choose Schedule to run this application job. |  |  |
| 9 | Check Application Jobs Log | Choose Go to update the job status. When your job’s status changes to Finished, you choose Log to check job log. | The job log displays. The cash snapshot should be created. |  |
| 10 | Check Cash Snapshot | Open Manage Cash Snapshots (F8962) to check the created cash snapshot. |  |  |

#### Capture Cash Snapshots

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can manually capture cash snapshots. You can centrally manage all cash snapshots that are captured manually or via scheduled jobs. In addition, you can delete cash snapshots that are no longer needed. A cash snapshot is a set of cash-related data marked with a specific timestamp, capturing details such as cash flows and bank account balances. It can be used to track and analyze your historical cash data.

Prerequisites

Make sure you have defined the cash position profiles that will be used to calculate cash position data in the Short-Term Cash Positioning (F5380) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Cash Snapshots (F8962). | The Manage Cash Snapshots view is displayed. |  |
| 3 | Capture Cash Snapshot | Choose Capture, on the dialog box Capture Snapshot, enter the following data and choose Create:Snapshot Description: <Description of a cash snapshot>Note Specify a meaningful description for your cash snapshot when you capture snapshots manually.Cash Position Profile: <CPP_01, defined in preliminary steps>Snapshot Purpose: <Cash Position or Liquidity Analysis> | The new Snapshot ID is generated. |  |
| 4 | Delete Cash Snapshot (Optional) | Select one or more Snapshots, then choose Delete. Choose Delete in the dialog box. | The selected snapshots are deleted. |  |

#### Request Investment or Funding

##### Initiate Bank Transfer

Procedure

Run the steps in the previous Initiate Bank Transfer procedure by using the Make Bank Transfers (F0691) app.

##### Cash Concentration (2U8)

Procedure

Follow the steps in the Intercompany Process for Cash Concentration (2U8) test script.

##### Initiate Cash Trade Request

Procedure

Run the steps in the previous Cash Trade Request procedure.

### Instant Balances (Optional)

Purpose

You can retrieve current available balances for selected bank accounts directly from the associated banks' APIs through SAP Multi-Bank Connectivity. Instant balances provide the current available balance for the selected bank accounts at the time of the balance update request.

|  |
| --- |
| Note Only selected member banks of SAP Multi-Bank Connectivity (MBC) are supported. |

Prerequisite

To be able to monitor instant balances, you first have to define the following settings:

- Activate the scope item Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/16R)), and complete the required configurations.
- In the Manage Banks - Cash Management (F1574A) app, find the relevant house bank and enable instant balances for the house bank.
- In the Define Bank Accounts Settings - Instant Balances (F7805) app, select the bank accounts you want to monitor instant balances for and choose Switch On to enable instant balances for the selected bank accounts.

For details, you can refer to the Set Up Instant Balances procedure of the scope item Advanced Bank Account Management ([J77](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J77)) .

#### Monitor Instant Balances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can use this app to monitor and update instant balances for bank accounts that are enabled for instant balances.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Monitor Instant Balances (F7804). | The Monitor Instant Balances view displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:House Bank: <house bank>Company Code: 3310 | The bank account list displays. |  |
| 4 | Check Bank Account | Choose > to navigate to check instant balances history. |  |  |
| 5 | Update Balance | Choose Update Balance. | An update request is sent to the corresponding bank and the Update Status field is set to In Process. |  |
| 6 | Check Instant Balances | Choose Full Screen, and refresh the screen to see the latest status. | When the update is completed, the status is changed to Completed and the instant balance is displayed in the Available Balance field. |  |

#### Manage Bank Message

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can check bank message for instant balance request and response.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Integration Specialist - Bank Integration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Messages (F4385). |  |  |
| 3 | Enter Selection Criteria | In the upper area, make the following entries and choose Go:Message Type: BALANCE_REQUEST & BALANCE_RESPONSE | The MBC messages are displayed in respective tabs. |  |
| 4 | Check Incoming Message | Choose All tab, select a inbound message, and choose >. | Details screen of message displays. |  |
| 5 | Display Message Content | Choose View Payload in the detail screen of message. | The message content is displayed. |  |
| 6 | Navigation to Application Log | Choose Log in the detail screen of message. | The detail log of the message processing is listed. |  |
| 7 | Check Related Message | Choose Related Message ID, and navigate to the related outbound message. | The outbound message with message type BALANCE_REQUEST displays. |  |

### Manage Liquidity Item Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can process lifecycles of liquidity item transfer documents like Create, Change, Copy, and Delete.

|  |
| --- |
| Note The Manage Liquidity Item Transfer is integrated with the Blocked Date Range, Start Date for One Exposure features. Value date or posting date should be later than both dates. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Liquidity Item Transfer (F6385). | The Manage Liquidity Item Transfer screen displays. |  |
| 3 | Enter Company Code and Currency | Choose Create, make the following entries in the Create dialog box and choose Continue:Company Code: 3310Transfer Currency: <for example EUR> | The Liquidity Item Transfer screen displays. |  |
| 4 | Maintain Description in header level | Make the following entries:Description: <your description> |  |  |
| 5 | Maintain Liquidity item transfer items – item 1 | In the Line Items section, choose Create to add a new items, and make the following entries:1) Transfer Item ID: for example the original liquidity item you want to tranferTransfer Item Desc: <your description>Liquidity Item: <for example, the oringal liquidity item which you want to tranfer>Amount: <transfer amount, for example -1000.00>Value Date: <Value Date>Posting Date: <Posting Date>Note You can add more fields in the line item using the Setting function. |  |  |
| 6 | Maintain Liquidity item transfer items – item 2 | In the Line Items section, choose Create to add another item, and make the following entries:2) Transfer Item ID: for example the target liquidity item you want to tranfer.Transfer Item Desc: <your description>Liquidity Item: <for example, the target li-quidity item you want to tranfer>Amount: <transfer amount, for example 1000.00>Value Date: <Value Date>Posting Date: <Posting Date>Note Total balance for the transfer must be zero. |  |  |
| 7 | Save | At the bottom of the view, choose Create. | All the items will generate actual One Exposure flows. During the liquidity item transfer, the original liquidity items will not necessarily be changed, and the shifts between liquidity items will be documented.Note You can check the tranfer liquidity items with App Check Cash Flow Items (F0735), Short-Term Cash Positioning (F5380) or Cash Flow Analyzer (F2332). |  |

### Situation Handling: Date Difference Warning for FI Flows

#### Monitor Situations

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

You have performed the procedure Situation Handling for Cash and Liquidity Management in the Preliminary Step.

In order to trigger notification and check it, please make sure you have created the relevant transaction data.

Template FIN_FQM_FIDATE_DIFFERENCE is used for situation handling that informs specific users when the system detects an FI cash flow for which the difference between the posting date and the value date does not meet the defined condition.

In our case, when the difference in days between the posting date and value date is greater than or equal to 30 days, the notification can be triggered and sent to the recipients. You can refer to the step Post General Journal Entries in Test Script Accounting and Financial Close ([J58](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J58)) to create a document and set the value date as posting date + 30 days.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Monitor Situations (F3264). |  |  |
| 3 | Maintain Filter | Make the following entries:Situation Type ID: ZFIN_FQM_FIDATE_DIFFERENCEYear: <current year> |  |  |
| 4 | Check Instance Details | In the Instance Details section, check detailed information for your situation type. | The batch job is executed per one hour.Note You need to check the result after one hour of creating the test data. |  |

#### Check Notification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the notification is checked by the recipient who is assigned to team members in the Preliminary Steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a recipient (for example, Cash Manager). |  |  |
| 2 | Check Notification | On the home page, choose Notifications in the upper right corner.Choose By Type, under type Situation Date Difference Warning for FI Flows has been identified, choose Expand Group. |  |  |
| 3 | Check Details | Choose one item with Date difference in FI flow is too large and navigate to App Display Line Item Entry (F2218). |  |  |

### Situation Handling: Bank Account Balance Threshold Exceeded

#### Monitor Situations

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

You have performed the procedure Situation Handling for Cash and Liquidity Management in the Preliminary Step.

In order to trigger notification and check it, please make sure you have created the relevant transaction data.

Template FIN_CLM_BKACCTBAL_THLDEXCEEDED is used to notify bank account supervisors when the balance of a bank account falls short of or exceeds the defined threshold so that the account supervisors can consider taking appropriate actions.

In our case, when the balance of a bank account is less than zero, the notification can be triggered and sent to the recipients. You can refer to the step Outgoing Integration in Test Script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/1EG)) to import a bank statement and set the closing balance below zero.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Monitor Situations (F3264). |  |  |
| 3 | Maintain Filter | Make the following entries:Situation Type ID: ZFIN_CLM_BKACCTBAL_THLDEXCEEDEDYear: <current year> |  |  |
| 4 | Check Instance Details | In the Instance Details section, check detailed information for your situation type. |  |  |

#### Check Notification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the notification is checked by the recipient who is assigned to team members in the Preliminary Steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a recipient (for example, Cash Manager). |  |  |
| 2 | Check Notification | On the home page, choose Notifications in the upper right corner.Choose By Type, under type Situation Date Difference Warning for FI Flows has been identified, choose Expand Group. |  |  |
| 3 | Check Details | Choose one item with Balance Threshold Alert for Bank Account and navigate to App Short-Term Cash Positioning (F5380). |  |  |

### Cash Reports

Purpose

This section describes all of the frequently used reports for cash daily operation.

#### Schedule Jobs for Bank Statement Monitor

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you schedule jobs using the provided template. Based on the job parameters you specify, the system calculates the results for specific bank accounts in the background. Because of this, when you open the bank statement monitor, you'll be able to display the monitoring results for your bank accounts in a more efficient manner.

Prerequisite

Ensure that fields related to the bank statement monitor are fully populated under the Bank Relationship tab in bank account master data. For more information, see the Advanced Bank Account Management ([J77](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J77)) test script.

Fields related to the bank statement monitor:

Processing Status: Yes

Interval: for example, 10

Interval Unit: for example, Calendar Days

Factory Calendar ID: for example, 01

Difference Status: Yes

Serial Number Status: Yes

Reconciliation Status: Yes

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Accounts Receivable Accountant . |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Jobs for Bank Statement Monitor (F6866). |  |  |
| 3 | Create a New Application Job | On the current view, choose Create to create an application job. | The Application Jobs view displays. |  |
| 4 | Choose Job Template | In the Template Selection section, make following entries:Job Template: Determine Status of End-of-Day Bank StatementsJob Name: Determine Status of End-of-Day Bank Statements |  |  |
| 5 | Maintain Scheduling Options | Choose Step 2. In the Scheduling Options section, make the following entriesStart Immediately: <Selected or deselected>Note If you choose star immediately, other parameter do not need to maintain.Start: <current time or any future time as needed>Time Zone: <time zone>For Recurrence Pattern, choose Define Recurrence Pattern.In the Scheduling Information dialog box, the additional scheduling options are available.Recurrence Pattern: for example, WeeklyEvery: for example, 1On: for example, MondayEnd: OptionalOn Non-Working Day: OptionalCalendar: for example, Germany(Standard)Choose OK. | If you would like to run this job immediately, the check-box of Start Immediately should be selected.If you schedule this job at some time in the future, the Start and Time Zone should be defined. |  |
| 6 | Maintain Parameter | Choose Step 3. In Parameter section and make the following entries:General Parameters:Key Date (Job Start Date +/- X Days): 7Company Code: For example: 3310House Bank: <empty>House Bank Account : <empty>Other Parameters:Send Email for Jobs with Status Failed and Canceled: <deselected>Email Recipients (Separated by Semicolon): <empty>Email Language: <empty> | Parameters are maintained. |  |
| 7 | Check | Choose Check. |  |  |
| 8 | Run this Application Job | Choose Schedule to run this application job. Choose Yes to confirm the dialog box. |  |  |
| 9 | Check Application Jobs Log | Choose Go to update the job status. When your job’s status change to Finished, you choose Details to navigate to the job details. In Log and Results section, choose Log status (Error, Information or Success…) to check Job Log. | Job log displays.Note After application job is executed or Success messages display, check the Error message and correct your customizing or house bank master data accordingly. |  |

#### Bank Statement Monitor

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Cash Manager can use this app to monitor the status of end-of-day bank statements from individual bank accounts. In addition to checking the status of end-of-day bank statements for a specific date, you also get an overview of the records over the last 14 days starting from the date you specified. Based on your bank account settings, you can efficiently identify problematic bank statements for your bank accounts and track if there is any missing statement page, any difference between the bank statement balance and the G/L account balance, any items that are not posted.

|  |
| --- |
| Note You're recommended to schedule jobs before using the bank statement monitor. If you access the bank statement monitor directly without scheduling any jobs, it initially shows no monitoring results. In this case, you have the option to choose the Update Results button to generate monitoring results immediately. You'll then receive a notification message via the bell icon and need to choose Go to display the results. |

Prerequisite

Ensure that fields related to the bank statement monitor are fully populated under the Bank Relationship tab in bank account master data. For more information, see the Advanced Bank Account Management ([J77](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J77)) test script.

Fields related to the bank statement monitor:

Processing Status: Yes

Interval: for example, 10

Interval Unit: for example, Calendar Days

Factory Calendar ID: for example, 01

Difference Status: Yes

Serial Number Status: Yes

Reconciliation Status: Yes

Also ensure that you have performed the procedures in the Incoming Integration section of the Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/1EG)) test script or the Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/16R)) test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Bank Statement Monitor (F6388). |  |  |
| 3 | Edit Header Data | Make the following entries and choose Go:Key Date: TodayCompany Code: 3310House Bank: <empty>House Bank Account: <empty> | Processing Status,Difference Status,Serial Number Status and Reconciliation Status are listed for monitored bank accounts. |  |
| 4 | Check Details | In the End of Day – Single Day tab, choose one item and choose >. | All status in detailed information display. |  |
| 5 | Back | Choose Back. |  |  |
| 6 | Check Status for End of Day – Last 14 Days | Choose End of Day – Last 14 Days tab, choose an option from the list (for example, Processing Status, Difference Status, Serial Number Status or Reconciliation Status).Note Choose Settings to select column Bank Statement Forwarding. | End of Day bank statement status for last 14 days display.NoteIf the bank statement is relevant to Advanced Payment Management, Manage Payment smart link will show at Processing Application which can be navigated to the corresponding object page. If the role does not include Payment_Specialist, the navigation will fail.If the bank statement is relevant to Forwarding of Advanced Payment Management, Bank Statement Forwarding is set as Forwarding. |  |

#### Intraday Bank Statement Monitor

Purpose

The Cash Management Specialist or Cash Manager can monitor the import status of intraday bank statements for the bank accounts selected for monitoring. They can compare the expected number of imports with the actual number, and view the import schedule and status for bank accounts in a timeline that can be zoomed in or out.

##### Define Monitoring Rules for Intraday Bank Statement Monitor

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you define the monitoring rules with frequency for the intraday bank statement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Define Monitoring Rules - Intraday Statements (FCLM_BRM_RULE). | The Define Monitoring Rules for Intraday Bank Statements screen displays. |  |
| 3 | Edit Rule | Choose Edit. | The Define Monitoring Rules for Intraday Bank Statements view displays. |  |
| 4 | Generate Rule with Frequency | Choose Create Rule with Frequency. | The Generate Rule with Frequency screen displays. |  |
| 5 | Enter Rule Data | Make the following entries and choose Generate Rule and Save:Rule ID: for example, R01Description: Rule for intraday bank statement monitorTime Zone: <your time zone>Import Frequency (In Minutes): 60 |  |  |
| 6 | Continue | Choose Continue to confirm the dialog box. | Rule generated and saved. |  |

##### Assign Monitoring Rule to Bank (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

At the bank level, you can use this process to assign a monitoring rule that applies to all the bank accounts in this bank, if there are no other rules specified for individual bank accounts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Banks - Cash Management (F1574A). |  |  |
| 3 | Set Up Bank for Intraday Bank Statement | Make the following entry and choose Go:Bank Number: for example, 18121976 |  |  |
| 4 | Choose Bank | Choose > for Bank Number18121976. | The Display Bank view displays. |  |
| 5 | Edit Bank | Choose Edit. |  |  |
| 6 | Enter Data | Make the following entries and choose Save:Intraday Statements Rule (Bank Level): for example, R01 | The bank is updated with the rule. |  |

##### Define Bank Account to Monitor

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this section, you define the bank accounts to be monitored. Only bank accounts that are set to be monitored appear in this App Bank Statement Monitor - Intraday (F3671) app.

|  |
| --- |
| Note Bank accounts can be linked to multiple house bank accounts by using the House Bank Account Connectivity setting. However, only bank accounts that are linked to one house bank account can currently be monitored by the Bank Statement Monitor - Intraday (F3671) app. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Accounts (F1366A). | The Manage Bank Accounts screen displays. |  |
| 3 | Set Up Bank Account for Intraday Bank Statement | Make the following entry and choose Go:Account Number: for example, 0000000693123456 |  |  |
| 4 | Account Detail | Choose > for the Account Number 0000000693123456. | The Bank Account view displays. |  |
| 5 | Set Up Bank Account for Intraday Bank Statement | Choose Edit. |  |  |
| 6 | Enter Data | Choose the Bank Relationship tab.Make the following entries and choose Save:Upload of Intraday Statements: SelectedIntraday Statements Rule (Account Level): for example, R01Note If you maintained the rule at bank level in the prior step, you can keep the Intraday Statements Rule (Account Level) field blank. To use a specific rule, maintain it at the bank account level.Ensure that the house bank account exists in the selected bank account. |  |  |
| 7 | Save | If the general setting for cash management is Activate Directly, the button displays as Save. For Activate via Dual Control, the button displays as Submit for Activation. For Activate via Workflow, the button displays as Submit for Approval.Note The changes for the bank account have to be approved if the general setting for cash management is Activate via Dual Control or Activate via Workflow. For bank account approval process, see the Advanced Bank Account Management (J77) test script. |  |  |

##### Monitor Intraday Bank Statement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you monitor the intraday bank statement.

|  |
| --- |
| Note The appointment of importing intraday bank statements can be generated automatically once a day via technical job SAP_FIN_FCLM_BAM_GEN_APPTS. You must wait at least one day to monitor the bank account maintained in the previous steps. |

Prerequisite

The bank account is added into the intraday bank statement monitoring hierarchy. Intraday bank statements for this specific bank account are uploaded.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Bank Statement Monitor - Intraday (F3671). | The Bank Statement Monitor - Intraday screen displays. |  |
| 3 | Enter User Settings | Choose your user icon in the upper right corner, then select User Settings. Make the following entries on the Alert Setting dialog box and choose OK.Number of Warnings: for example 4Note this number is used to show an alert for consecutive warnings in this App. |  |  |
| 4 | Enter Criteria | Make the following entry and choose Go:Key Date: <today>Bank Country/Region: for example, AEBank Key: for example, 18121976Import Status of Bank Account: for example, <blank> | For the bank accounts added into the intraday bank statement monitor hierarchy, the status shows as Error/Warning/Success in the hierarchy according to the imported number of the intraday bank statement. |  |
| 5 | Check Status | Choose > (Expand Node) to check Status, Expected, Imported for the Bank Account. | For the bank accounts added into the intraday bank statement monitor hierarchy, the status shows as Alert/Warning/Success in the hierarchy according to the imported number of the intraday bank statement. |  |

#### Monitor Bank Account Balances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can monitor whether bank account balances have been imported or entered in time for bank accounts.

|  |
| --- |
| Note Before you monitor Bank Account Balances, make sure you have defined the following attributes for the bank accounts you want to monitor in the Bank Relationship tab of the Manage Bank Accounts app:Interval and Interval Unit: Together, the two attributes define the frequency of the expected bank account balance update, for example, one day or two weeks.Factory Calendar ID (optional): You can specify a factory calendar if you want to take it into consideration.You can refer to the step Create Bank Account in test script Advanced Bank Account Management ([J77](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J77)). |

Prerequisite

You have entered or imported balances for bank accounts in remote systems in the step [Manage Bank Account Balances](#unique_136) [page ] 154.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori app | Open Monitor Bank Account Balances (F5176). |  |  |
| 3 | Monitor Bank Account Balances | Maintain selection criteria and choose Go.Statement Date: <current date>Technical ID: <blank>Status: <blank>Company Code: 3310 | Bank account balances is displayed under different status.Note Note for Status:1) Not Applicable:Bank account opening date is later than selected date.Bank account closing date is earlier than selected dateInterval is not maintainedInterval is maintained and calculated next import date is later than selected date but it's never uploaded before2) MissingCalculated next import date is earlier than selected date3) UploadedCalculated next import date is later than selected date |  |

#### Short Term Cash Positioning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can view the cash positions by location, company, and currency. Cash position data is calculated based on the cash position profiles that are defined in the Define Cash Position Profiles (F5399) app.

You can simulate cash concentration for cash pools defined in the Manage Cash Pools (Version 2) (F3266A) app. You can see the Manage Cash Pools (Version2) procedure of scope item Intercompany Process for Cash Concentration (2U8).

- When the hierarchy source is defined as 03 (Derived from Cash Pool and Bank Account Master Data) in the cash position profile, bank accounts that are assigned to cash pools of the service provider Bank - Time Dependent and In-House Bank - Time - Dependent are displayed in the cash pool hierarchies.
- The balances of subaccounts will be automatically aggregated in the header account of the cash pools to simulate the cash concentration performed by banks.

Capture cash snapshots using the Capture Snapshot button and load cash snapshots for cash position analysis using the Snapshot filter.

A cash snapshot is a set of cash-related data marked with a specific timestamp, capturing details such as cash flows and bank account balances. It can be used to track and analyze your historical cash data. You could also use the new apps Manage Cash Snapshots (F8962) and Schedule Jobs for Cash Snapshots (F8945) to capture and manage your cash snapshots.

Prerequisites

Make sure you have defined the cash position profiles that will be used to calculate cash position data in the Short-Term Cash Positioning (F5380) app.

Make sure you have defined the bank account settings in the Define Bank Account Settings - Bank Statements app.

If needed, perform bank account balance initialization to ensure all bank accounts that have balances are shown in this app.

You can see the Schedule Jobs for Bank Account Balance Initialization procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Short-Term Cash Positioning (F5380). | The Short-Term Cash Positioning view is displayed. |  |
| 3 | Set Cash Position Profile | Enter the following data and choose Go:Cash Position Profile: <CPP_01, defined in preliminary steps>Note In this document, the example cash position profile is defined with hierarchy source Derived from Cash Pool and Bank Account Master Data.You can also choose not to specify any cash position profile, bank accounts will be displayed in a flat list with predefined settings. | In the display area, data is displayed in a structure per cash position profile. |  |
| 4 | Include Cash Snapshot (Optional) | Choose Adapt Filters, select Snapshot ID and choose OK in the dialog box. Then enter snapshot ID created in step Cash Snapshot Management. | Snapshot ID can be considered. |  |
| 5 | Review Details at Company Code Level | On the left navigation panel of Bank Account Hierarchy, expand and choose > (Details) against Company Code. | Cash Position Details and Cash Position Overview are shown on the right side. |  |
| 6 | Review Cash Position Overview | On the right side screen, choose the Cash Position Overview tab, choose > (Details) against Currency to check Cash Position Details by planning level.For example, Company code > Bank Account Currency | Cash Position Details by planning level are displayed. |  |
| 7 | Review Cash Position Details | On the right side screen, choose > (Details) against Planning Level to check Cash Position Details by Bank Account.For example, Company code > Bank Account Currency > Planning Level | Cash Position Details By Bank Account is displayed. |  |
| 8 | Check Cash Flow Item by Bank Account | On the right side screen, choose amount to check cash flow item by Bank Account.For example, Company code > Bank Account Currency > Planning Level > Bank Account | Check Cash Flow Item is displayed. |  |
| 9 | Check Cash Position Details at Bank Account Level | On the left navigation panel of Bank Account Hierarchy, choose > (Details) against one bank account. | Cash Position Details and General Information is displayed. |  |
| 10 | Check General Information | On the right side screen, choose the General Information tab, choose the highline date under Opening Balance Date to check Bank Account Opening Balance Details. | Actual Cash Flows for Bank Account Opening Balance is displayed. |  |
| 11 | Check Cash Pool Name (Optional) | On the left navigation panel of Bank Account Hierarchy, choose Expand All. At Bank Account level, check cash pool information under column Cash Pool Name. Multiple cash pool structure can be display on the left navigation panel.Note Choose Settings on the left navigation to select field Cash Pool Name.Then choose > (Details) against Bank account level to check a specific cash pool structure. | Cash Position Details and Cash Pool Structure is displayed.Note When the hierarchy source is defined as 03 (Derived from Cash Pool and Bank Account Master Data) in the cash position profile, bank accounts that are assigned to cash pools of the service provider Bank - Time Dependent are displayed in the cash pool hierarchies. |  |
| 12 | Check Cash Pool Structure (Optional) | On the right side screen, choose the Cash Pool Structure tab, you can check Cash Pool structure for all relevant bank accounts (include header account and subaccounts). | Cash Pool Structure is displayed. |  |
| 13 | Back | Choose Back. |  |  |
| 14 | Export to Spreadsheet | On the left navigation panel of Bank Account Hierarchy, choose the Export to Spreadsheet icon.Note Export of Spreadsheet (Ctrl + Shift + E). | All of the current table contents are exported to a spreadsheet. |  |
| 15 | Review Details by Other Hierarchy Level | On the left navigation panel of Bank Account Hierarchy, expand and choose > (Details) against other hierarchy level.Note You can repeat above steps to monitor cash position details again other hierarchy level. | The Cash position can be displayed by various analytical dimensions, such as country/region, company code, bank account, currency. |  |

#### Cash Flow Analyzer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can view the aggregated amounts and line item details of cash positions, medium and long-term liquidity forecasts, and actual cash flows. You can analyze cash flows over days, weeks, months, quarters, or years for all bank accounts and liquidity items. The data presented in the app can be used to provide managers with a high-level overview and detailed insights into the cash flow status.

|  |
| --- |
| Note The cash positions in this app are calculated based on data sources from the One Exposure from Operations hub. To view bank account balances based on bank statements, please use the Short-Term Cash Positioning (F5380) app. |

Prerequisites

Before checking the report at the Hierarchy level, you need to define the relevant hierarchies. You can define or check the hierarchies via the following Apps:

- Bank Account Group Hierarchy: Execute the Manage Bank Account Hierarchies (F4973) procedure in Advanced Bank Account Management (J77) to define/check bank account hierarchy.
- Liquidity Item Hierarchy: Execute the Manage Liquidity Item Hierarchies (F4966) procedure in Preliminary Steps to create your liquidity item hierarchies.
- Cash Pool Hierarchy: Execute the procedure in Intercompany Process for Cash Concentration (2U8) test script to define/check a cash pool hierarchy by assigning a header account and subaccounts to the cash pool.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Cash Flow Analyzer (F2332). | The Cash Flow Analyzer view displays. |  |
| 3 | Define User Settings | On the upper right corner, choose your user, choose User Settings. On the dialog box, define the Derive Currency setting and choose OK. |  |  |
| 4 | Select Default Variant | Select the default report between Cash Position, Liquidity Forecast and Actual Cash Flows, or create your own variant. |  |  |
| 5 | Selection Criteria | Choose Adapt Filters if the filter selection fields are hidden.Maintain selection criteria and choose Go.Company Code: 3310Currency: <leave blank>Time Period: D7Date: <current date>Cash Flow View for Accounting: <as needed>Note You can use this filter to decide whether to display cash positions cash flows or liquidity analysis cash flows when the accounting scope is set as Cash Position & Liquidity Analysis in the configuration activity Define Source Application Accounting (105487).If the accounting scope is set as Cash Position Only or Liquidity Analysis Only, corresponding cash flows are displayed in this app without considering the filter setting.Consider Intraday Recon.Result: YesConsider End-of-Day Recon.Re...: YesNote You can use both filters to exclude forecasted flows that have been reconciled with intraday bank statements and end-of-day bank statements. | The list is filtered and shows all related entries within the time period.Note The time period settings are by Unit: D (Day), W (Week), M (Month), Q (Quarter) or Y (Year).NoteTake a snapshot to analyze the cash flows on the Snapshot Date.By default, the snapshot functionality is not enabled. You need to manually enable it in the self-service configuration app Define Basic Settings. |  |
| 6 | Expand Hierarchy | Expand the hierarchy Currency > Company Code > Bank Account .Note Display a list of cash flows in the View Settings variant in the structure of Currency > Company Code > Bank Account , or create your own variant. | Rows for opening balance, inflow, outflow and closing balance display for a specific bank account when they exist. The amount of bank transfer is reflected in outflow/inflow. |  |
| 7 | Navigate to Other Apps | Navigate to the Check Cash Flow Items (F0735) app to display the line item details for each cash flow.Navigate to the Make Bank Transfers (F0691) app to make necessary transfers on your bank accounts. |  |  |
| 8 | Switch Views | Select View pulldown menu to display the My Views dialog box and select either Balance View or Delta View and choose Save As. | Balance View displays opening balance, outflows/inflows, and closing balance.Delta View displays outflows/inflows. |  |
| 9 | Adjust Layout | Select Settings to change the layout and include more fields, such as Liquidity Item. |  |  |
| 10 | Export to Spreadsheet | Choose the Export to Spreadsheet button. |  |  |
| 11 | Display Bank Account Hierarchy View (Optional) | Back arrow to the Cash Flow Analyzer view, and choose Display Hierarchy and on the Select Hierarchy dialog box, select Bank Account Hierarchy.Enter a Bank Account Hierarchy ID and choose OK.Note If large amounts of data and the multilevel hierarchy cause slow performance, use the Expand Level for Hierarchy in the Users Settings to limit the hierarchy to your current situation. For example, if you input 1 in the Expand Level for Hierarchy, the result is only the first level of hierarchy is expanded. | The Bank Account Group view displays.Note You can display the report in the bank accounts hierarchy. You can also display the report in cash pools. |  |
| 12 | Display Liquidity Item Hierarchy View (Optional) | Choose the back arrow, then choose Display Hierarchy again. On the Select Hierarchy dialog box, select Liquidity Item Hierarchy and enter the following data and choose OK:Liquidity Item Hierarchy ID: For example, LIQ_HIE_DEMODisplay Currency for Liquidity Item Hierarchy: For example, AEDNote You can choose Display Currency for Liquidity Item Hierarchy in User Settings. | The Liquidity Item Hierarchy view displays. |  |
| 13 | Display Cash Concentration Simulation View (Optional) | Choose Back and choose Display Hierarchy. In the Select Hierarchy dialog box, choose Cash Concentration Simulation and make the following entries and choose OK:Cash Pool Name: CP_1Display Currency for Cash Pool: AEDNote Before displaying the Cash Concentration Simulation view, ensure that you have completed the relevant steps in the Intercompany Process for Cash Concentration (2U8) test script.If you do NOT enable New Cash Concentration Model in the Define Settings for Cash Concentration configuration activity, the Cash Concentration Simulation node in the Select Hierarchy dialog box will be hidden. | The Cash Concentration Simulation view displays. |  |

#### Actual Liquidity Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can view the actual liquidity analysis of cash flows in bank accounts, identifying where cash comes from and how it is used. This process focuses on cash and liquidity planning and periodic reporting. It uses the Review Booklets for your analytical query.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Actual Liquidity Analysis (F7923). | The Actual Liquidity Analysis view displays. |  |
| 3 | Selection Criteria | Choose Adapt Filters if the filter selection fields are hidden.Maintain selection criteria and choose Go.Company Code: 3310From Fiscal Year Period: <current period - 6>To Fiscal Year Period: <current period + 6>Date Indicator: <Value Date>Liquidity Item Hierachy: <Hierarchy created in preliminary step>Note Liquidity item hierarchies are defined to structure liquidity items according to your business needs. The liquidity item hierarchies can then be used in analyzing and planning cash flows.Transaction C urrency: <as needed>Display Currency: for example, AEDExchange Rate Type: for example, MSpecific Snapshot: <as needed>Note There are two kinds of values it provided.One is from Manage Cash Snapshots (F8962) app or Schedule Jobs for Cash Snapshots (F8945) app.The other is from automatically generated by One Exposure Obsoleted Flows Processing Mechanism which is maintained in Preliminary Step Enable Snapshot (Optional). | In this report, the system assigns the opening balance and closing balance to specific liquidity items: Opening Balance (LA_OPEN_BAL) and Closing Balance (LA_CLOSE_BAL).Note You will see the node Not Assigned Liquidity Item(s) (REST_H) if liquidity items are not maintained in the hierarchy. This node always appears at the bottom of the hierarchy. You can place it in the flows block only if the balance category is visible.You can navigate to the Check Cash Flow Items (F0735) app to find detailed flow information. Navigation is enabled for the measures: Amount in Transaction Currency and Amount in Display Currency.When you navigate to the opening balance of a period, you will see all the flows before this period. When you navigate to the closing balance of a period, you will see all the flows until the end of this period. |  |
| 4 | Expand Hierarchy | Expand the hierarchy. |  |  |
| 5 | Adjust Layout | In the rightmost menu bar, choose Layout icon, change the layout and edit Measures and Dimensions. |  |  |

#### Document Chain Tracing for Cash Flow

Purpose

In this step, you can create traceability results for the specified accounting document which includes the flows and all intermediate flows in the document chain tracing when generating flows.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Document Chain Tracing for Cash Flow (F7690). | The Document Chain Tracing view displays. |  |
| 3 | Create | Choose Create. In the dialog box, make the following entries and choose Create.Then refresh the screen until the status is updated with Finished.Company Code: 3310Fiscal Year: for example, current yearJournal Entry(Start Item): for example, a payment documentExpiration Time by Hours: <as needed> | The job is scheduled. The traceability result can display once the job is finished. |  |
| 4 | Expand All | Choose Expand All. | All items structure is expanded.Note Documents chain should trace to the 6th level at most. |  |
| 5 | Check Details | Choose > Navigation per item. | One item result and details display. |  |

#### Check Cash Position (Smart Business)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

The Cash Manager or bank accountant can use this app to check the forecasted cash positions for the current date by location, company, and currency. Cash position data is calculated based on memo records and various data sources from the One Exposure from Operations hub.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Cash Position - Today (F1737). |  |  |
| 3 | Review Cash Position | A bar chart displays the cash position information classified by bank country. | For each country, the blue bar represents the cash position in the banks of this country. The cash position amount is displayed in the top left of the view. |  |
| 4 | Display by other Options | From the drilldown list, By Bank Country is chosen by default, select another option, for example, By Company. | The bar charts are classified by the company code names. |  |
| 5 | Drill Down Using Bar | Choose the blue bar, choose an option from the list (for example, By Bank). | The bar charts are reclassified by bank names. |  |
| 6 | Shift to Form Display | Choose the Tabular View button. | The cash position data is displayed in a form format. |  |

#### Check Liquidity Items on G/L Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can check liquidity items on G/L Accounts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori app | Open Check Liquidity Items on G/L Accounts (F6459). | The Check Liquidity Items on G/L Accounts view displays. |  |
| 3 | Enter Selection Criteria | Choose Adapt Filters if selection fields are hidden.Make the following entries and choose Go:Company Code: 3310G/L Account: <empty>Chart of Accounts: <empty>Account Group: <empty> | The liquidity item on G/L accounts list displays.Note If you activate info account and define GL classification for liquidity calculation in procedure [Liquidity Calculation: G/L Classification](#unique_18) [page ] 28. GL Account Classification columns can be used for info account. |  |

#### Check Cash Flow Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Cash Manager, Bank Accountant, Accounts Receivable Accountant, or Accounts Payable Accountant can use this app to track and trace all the cash flow items from different source applications that are integrated with cash management. You can also see line item details of the original documents, such as journal entries, banks, and account assignments. This provides a comprehensive overview of the cash flow and liquidity status in your company.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori app | Open Check Cash Flow Items (F0735). | The Check Cash Flow Items view displays. |  |
| 3 | Enter Selection Criteria | Choose Adapt Filters if selection fields are hidden.Make the following entries and choose Go:Exchange Rate Type: <M>Snapshot Time: <default value>Value Date: <Today>Company Code: 3310Certainty Level: <choose all certainty levels>Account Number: 0000000693123456Cash Flow View for Accounting: 2 Cash Position or 3 (Liquidity Analysis) | The Payment Documents list is displayed.Note If Snapshot is enabled and the period of (Valid From to Valid To) includes cash flow time stamp, the data flow should be detected under the current selected timeslot. You can change default Snapshot Time.If Snapshot is not enabled and the period of (Valid From to Valid To) excludes cash flow time stamp, the data flow should not be detected under the current selected timeslot. |  |
| 4 | Display Additional Payment Information | Select your cash flow item, and choose > (Details) to check details information. | More payment information is displayed on the screen, such as:General InformationJournal Entry InformationBank InformationBank Communication Management InformationNote Different source applications display different payment information. |  |
| 5 | Display FI Document | Choose the blue link for a journal entry number, and navigate to Manage Journal Entries.Note Choose a line with Source Application such as Accounts Receivable, Accounts Payable, or Payment. | The Manage Journal Entries screen displays. |  |
| 6 | Go Back | Choose Back. | The Check Cash Flow Items view displays. |  |
| 7 | Make Manual Adjustment of the Cash Flow Items (Optional) | Choose Edit. In Account Assignments section, manually adjust the account assignments (such as liquidity item, transaction amount, cost center, and so on).NoteThis function only works for cash flows from accounting documents (journal entries).You can also choose Add to add one or more new items to split the Transaction Amount of the original item into different dimensions (such as liquidity item, transaction amount, cost center, and so on).The Transaction Amount of all items must equal the Transaction Amount of the original item. | The account assignments of the cash flow items is manually adjusted. |  |

#### Cash Flow Comparison – By Date Range

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

You can compare actual cash flows with your forecasts in the past as well as compare different forecast records that were made on different snapshot dates. It helps you understand the accuracy of your past forecast records and assists you in improving your cash flow forecasts continuously.

|  |
| --- |
| Note To view the forecast values in the past, make sure that you executed the [Enable Snapshot (Optional)](#unique_9) [page ] 13 step in the Preliminary Steps. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Cash Flow Comparison (F3274). | The Cash Flow Comparison – Actual/Forecast view is displayed. |  |
| 3 | Selection Criteria | Choose Adapt Filter Bar, if the filter selection fields are hidden.Maintain the following selection criteria and choose Go:Value Date From: For example, <the first date of current month>Value Date To: For example, <the last date of current month>Snapshot Date From: For example, <the first date of current month>Snapshot Date To: For example, <the last date of current month>Snapshot Time: For example, 23:59:59Display Currency: for example, AEDExchange Rate Type: for example, M | Acutal-to-forecast and forecast-to-forecast comparison for cash flows of the specified time range is displayed.Note The Actual Flows line displays the actual cash flow. The line with a specific date, displays the forecast cash flow data. |  |

#### Cash Flow Comparison – By Timestamp

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

You can select any two snapshot timestamps in the past and compare the forecasted cash flows as well as compare the forecasted flows with the actual flows. It helps you understand the accuracy of your past forecast records and assists you in improving your cash flow forecasts continuously.

|  |
| --- |
| NoteTo view the forecast values in the past, make sure that you executed the [Enable Snapshot (Optional)](#unique_9) [page ] 13 step in the Preliminary Steps. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Cash Flow Comparison - By Timestamp (W0137). | The Cash Flow Comparison - By Timestamp view is displayed. |  |
| 3 | Selection Criteria | Choose Adapt Filters, if the filter selection fields are hidden.Maintain the following selection criteria and choose Go:Value Date From: For example, <the first date of current month)Value Date To: For example, <the last date of current month)Snapshot Date A: For example, <the first date of current month)Snapshot Date B: For example, <the last date of current month)Snapshot time A: For example, 23:59:59Snapshot time B: For example, 23:59:59Display Currency: for example, AEDExchange Rate Type: for example, M | Forecast records that were made on different snapshot timestamps is compared. The forecast records is compared with the actual cash flows. |  |

## Appendix

### Process Chains

The process to be tested in this test case is part of a chain of integrated processes.

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
> Flagged while digesting this document, not verified: Check Notification under 'Situation Handling: Bank Account Balance Threshold Exceeded' tells the recipient to expand type 'Situation Date Difference Warning for FI Flows has been identified', but step 3 then expects an item 'Balance Threshold Alert for Bank Account' - the notification type looks copied from the date difference situation.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Short Term Cash Positioning purpose says hierarchy source 03 shows accounts assigned to cash pools of service provider 'Bank - Time Dependent' and 'In-House Bank - Time - Dependent', while the step 11 note mentions only 'Bank - Time Dependent'.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[05-treasury-and-cash-management/advanced-cash-operations-j78-ae-test-script-sap-s-4hana-cloud-public-e-part-01]]
- related-to :: [[05-treasury-and-cash-management/basic-cash-operations-bfb-ae-test-script-sap-s-4hana-cloud-public-edit]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J78_S4CLD2608_BPD_EN_AE.docx` — lines 3313–4596 of the extracted text · extracted with `mammoth` · 349,191 chars in the whole document
