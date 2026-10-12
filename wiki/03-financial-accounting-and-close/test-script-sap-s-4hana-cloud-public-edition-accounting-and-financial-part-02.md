---
id: 03-financial-accounting-and-close/test-script-sap-s-4hana-cloud-public-edition-accounting-and-financial-part-02
title: Test Script SAP S/4HANA Cloud Public Edition - Accounting and Financial Close (J58_AE) (J58_S4CLD2608_BPD_EN_AE) — part 2 of 2
description: "SAP Fiori test script, company code 3310 (UAE): FX valuation, currency adjustments, impairment, reclassification, period close, tax, reporting, validation."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/general-ledger-accounting-and-financial-close]
aliases: []
keywords: [General Ledger Accounting and Financial Close, foreign currency valuation, advanced foreign currency valuation, currency adjustments, journal entry verification, credit-risk-based impairment, balance sheet reclassification, posting periods, tax reconciliation, withholding tax]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J58_S4CLD2608_BPD_EN_AE.docx#lines-3739-5034"]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1304
topic: 03-financial-accounting-and-close/general-ledger-accounting-and-financial-close
language: EN
part: 2/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Accounting and Financial Close (J58_AE) (J58_S4CLD2608_BPD_EN_AE) — part 2 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J58_S4CLD2608_BPD_EN_AE.docx`, part 2 of 2 (lines 3739–5034 of the extracted text), extracted with `mammoth`. Grouped under **General Ledger Accounting and Financial Close** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

You must post a Credit and Debit position to an open item-managed account using a foreign currency for which the exchange rate at the time of the posting is different from the exchange rate at the month end (when you execute the foreign currency valuation). Open items must be available in a foreign currency, posted with a higher or lower exchange rate than the one that is currently applicable. To post a customer invoice in a foreign currency, use the Create Outgoing Invoices (FB70) app, changing the exchange rate in the document header.

To see the exchange rates, you may either use the Maintain Exchange Rates(OB08) app or enter the exchange rate manually in the document you’re posting. For more information about posting general journal entries, see the [Post General Journal Entries](#unique_61) [page ] 86 step.

Procedure - Option 1

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Perform Foreign Currency Valuation (FAGL_FCV). |  |  |
| 3 | Enter Data | Make the following entries and choose Execute:General SelectionsCompany Code: 3310Valuation Key Date: <Current date>Valuation Area: AEPosting ModeTest Run (No Database Update) SelectedNote If you do not want to execute a test run, you can post the valuation immediately.Posting ParametersDetermine Automatically: SelectedOpen items: SubledgerValuate Vendors: SelectedValuate Customers: SelectedOpen items: G/L AccountsValuate G/L Accounts: Selected | Foreign currency postings in the system are represented in the financial statements with current date valuation. Two types of documents are posted:Reporting period documents to represent revaluationNext period documents to reverse the first postings.The system generates a Foreign Currency Valuation report showing the details of what accounts, by document, were revaluated. The document data includes Amount in FC, Amount in loc. cur., Exch.rate (original), Exch.rate (new), Posting Date and New Difference.The Gain/Loss Unrealized Foreign Currency Revaluation account gets debits and credits based on gain or loss determination. The Adjustment accounts for AR and AP (Domestic, Foreign, and Intercompany) get the off-set amount posted to the Gain/Loss account.Caution If the currency valuation program displays an error message saying Acct. determination is incorrect: Company Code XXXX Valuation area XX – Account XXXXXXXX, you must maintain the relevant account determination using the Automatic Account Determination configuration step (accessible by Manage Your Solution or the SAP CBC Project Experience). For example, for G/L account 21900000, currency valuation is posted on the following accounts:Loss 72010000 Loss from Exchange Rate DifferencesGain 72510000 Gain from exchange rate differencesVal.Loss 1 72040000 Loss from currencies valuationVal.Gain 1 72540000 Gain from currencies valuationBS Adjustment 21720200 Other Payable Adjustment |  |

Procedure - Option 2

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule General Ledger Jobs (F1927). | The Application Jobs view is displayed. |  |
| 3 | Create a new job | Choose Create. | The New Job: Advanced Foreign Currency Valuation view is displayed. |  |
| 4 | Enter Data | Make the following entries and choose Step 2:Template Selection:Job Template: Foreign currency valuationJob Name: Foreign currency valuation | The job is created and started immediately. |  |
| 5 | Enter Data | Make the following entries and choose Step 3:Scheduling OptionsStart immediately: Make the following entries and choose Selected |  |  |
| 6 | Enter Data | Make the following entries and choose Schedule:Parameters - General Selections:Company Code: 3310Valuation Key Date: <date>Valuation area:Postings area:Update Run: SelectedDetermine Automatically: SelectedOpen Items: Subledger area:Valuate Vendors: SelectedValuate Customers: SelectedOpen Items: G/L Accounts area:Valuate G/L Accounts: Selected Choose Schedule. |  |  |
| 7 | Check Job Status | After the job is finished, choose Details (>) for the row of your completed job. | The job log is displayed. |  |

### Post Currency Adjustments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you adjust account balances in foreign currencies. The app is useful in environments with volatile exchange rates, for example. You adjust the account balances by entering amounts for each currency directly.

|  |
| --- |
| Note If needed, you can find a parallel workflow for currency adjustments in the Appendix. For more information, see the subtopics there under Parallel Workflow - Currency Adjustment. |

Prerequisite

You posted journal entries in foreign currency (for example, to the foreign currency bank account 10010000) previously.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post Currency Adjustments (F1606). |  |  |
| 3 | Enter Document Data | Make the following entries and choose Post:HeaderJournal Entry Date: <Current date>Company Code: 3310Posting Date: <Current date>Transaction Currency: a foreign currency, for example, USDJournal Entry Type: SADebits/Credits Cur.: Company Code Currency (10)Line items 1G/L Account: <account number>, for example, 11001000Debit/Credit amount (Company Code Currency): <amount>, for example, 10 in the Debit fieldCaution You may need to press Enter after entering a value in the Debit or Credit fields to access the remaining fields.House Bank /House Bank Account: <house bank> and <house bank account>, for example, AEBK1 / USDACLine items 2G/L account: <account number>, for example, 21720200Debit/Credit amount (Company Code Currency): <amount>, for example, credit 10Tax code (If required): <tax code> for example, <Input Tax Code> | The document shows a zero amount in foreign currency and your entered amount in local currency. |  |

### Verify Currency Adjustments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

As a daily transaction requester, you verify the currency adjustments made in the [Post Currency Adjustments](#unique_97) [page ] 140 step. After you verify the adjustments, another user approves or rejects the currency adjustments.

Prerequisites

Execute the following two procedures.

Table 8: Manage Workflows

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access SAP Fiori App | Open Manage Workflows for Journal Entry Verification - In General Ledger (F2720) | The Manage Workflow view displays. |  |
| 3 | Choose Workflow Type | In the Workflows field, select Currency Adjustment Verification. |  |  |
| 4 | Create Workflow | Choose Create. | The new workflow view displays. |  |
| 5 | Enter Workflow Details | Make the following entries and choose Save:Header tab:Workflow Name: for example, Currency adjustment verificationProperties tab:Description: For example, Company code = 3310Start Conditions tab: (add the following preconditions)Company Code: 3310Journal Entry Type: For example, SAAccount Group: For example, FINStep tab: (choose Add/Create to add the first sequence step)Step Name: Verify Currency AdjustmentStep Type: Verify Currency AdjustmentRecipients tab:Role: for example, Group 1 for Verifying Currency AdjustmentChoose Add/Create.Add a second sequence step.Step Name: Post Currency AdjustmentChoose Add/Create. | You saved the workflow. |  |
| 6 | Activate Rule | Choose Save, then choose Activate. | The currency adjustment verification is activated. |  |

Table 9: Manage Teams and Responsibilities

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access SAP Fiori App | Open Manage Teams and Responsibilities For Journal Entry Verification - In General Ledger (F3932). |  |  |
| 3 | Create Team | Choose Create. | The Team view displays. |  |
| 4 | Enter Team Details | Make the following entries:General Information tab:Name: for example, Currency Adjustment VerifierGlobal ID: for example, 123Status: EnabledType: FGCAV (FI Verify Currency Adjustment Team) |  |  |
| 5 | Enter Team Details | Choose the Team Members tab. |  |  |
| 6 | Enter Team Details | Choose Create. | A blank field displays below Business Partner. |  |
| 7 | Enter Team Details | Make the following entries and choose Save:Business Partner: For example, the local gl_accountant userFunction: FGCAV_L1 (Group 1 for Verifying Currency Adjustment) | The responsibility for the general journal entries approval workflow is defined. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Verify Currency Adjustments - For Requester (F4670A). | The Verify Currency Adjustments view is displayed. |  |
| 3 | Create Adjustment Posting (Optional) | If an adjustment posting doesn't exist, you can create one. To do so, choose Create. | The Post Currency Adjustment app is opened. For more information on this activity, see the [Post Currency Adjustments](#unique_97) [page ] 140 step in this test script. |  |
| 4 | Enter Details | Make the following entries and choose Go:Company Code: 3310 | The Journal Entries pane shows a list of currency adjustment workflows. You can see the status of the entries in the Status column. |  |
| 5 | View History | To show the history for a journal entry, choose the clock button in the History column for that entry. A dialog box is displayed with the workflow history. If a workflow is rejected, you can choose the Comments tab in the dialog box to see the reason entered by the user who rejected it.You can also view the processors. To do so, choose the processor button the Processor column. |  |  |

#### Withdraw Verify Currency Adjustments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can withdraw the currency adjustments with Submitted and Approved status. You only can withdraw the entries that you submitted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Verify Currency Adjustments - For Requester (F4670A). | The Verify Currency Adjustments view is displayed. |  |
| 3 | Create Adjustment Posting (Optional) | If an adjustment posting doesn't exist, you can create one. To do so, choose Create. | The Post Currency Adjustment app is opened. For more information on this activity, see the [Post Currency Adjustments](#unique_97) [page ] 140 step in this test script. |  |
| 4 | Enter Details | Make the following entries and choose Go:Company Code: 3310 | The Journal Entries pane shows a list of currency adjustment workflows. You can see the status of the entries in the Status column. |  |
| 5 | Select and Withdraw | In the Journal Entries table, for the document you want to withdraw, click the empty cell to the left of the row and choose Withdraw. | The system displays a Confirmation dialog box. |  |
| 6 | Confirm Withdrawal | To withdraw your document, choose Withdraw. | The system displays the message You have withdrawn a journal entry. It might take some time to see the new status. Try refreshing the page.Upon refreshing the page, the status changes to Withdrawn. |  |

### Approve Verify Currency Adjustments (for Processor- Inbox)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You receive currency adjustments that must be checked before final posting. After checking the currency adjustments, you can either approve or reject with a comment/ reason. Once you select and approve an adjustment, it disappears from the list. If a document is approved, posting of the adjustment is automatically triggered.

|  |
| --- |
| Note You can enable the approval authorization check with the Activate Authorization Check for Approval configuration step. Once this is activated, the system has the posting authorization check for the processor to approve the document. For more information, see the [Activate Authorization Check for Approval](#unique_9) [page ] 11 step in the Preliminary Steps section of this document. |

Prerequisites

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Administrator role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Users (F1303). |  |  |
| 3 | Search User | Make the following entry and choose Go:User name: GL_ACCOUNTANT_AE | The system displays a list of matching user names. |  |
| 4 | Choose User | Select the checkbox next to the user name from the search result and choose Edit. | The Business User view is displayed. |  |
| 5 | Add Role to User | In the Assigned business roles section choose Add. | The Add Business Roles view is displayed. |  |
| 6 | Choose Role to be Added | On the Add Business Roles screen search for the SAP_BR_GL_ACCOUNTANT role, select it and then choose OK.Caution After you complete this section, unassign the SAP_BR_GL_ACCOUNTANT role from the user you chose in this step. | The role is added in the Assigned Business Roles section. |  |
| 7 | Save | Save your entries. | The system confirms that the changes have been saved. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for United Arab Emirates General Ledger Accountant role. |  |  |
| 2 | Access the SAP Fiori App | Open Verify Journal Entries in General Ledger - For Processor (Inbox) (F2728). |  |  |
| 3 | Approve Documents | Select the Verify Currency Adjustments document to be approved.Choose Approve. | The document is approved and posted.Note All approved documents are displayed in the Verify Journal Entries in General Ledger - For Processor (Inbox) (F2728) app as well as in the Verify Currency Adjustments - For Requester (F4670A) app. |  |
| 4 | Display Posted Document | Access the Manage Journal Entries (F0717A) app, make the following selections and choose GO:Company Code: 3310Ledger Group: <empty>Journal Entry Type (optional): for example, SAJournal Entry:Document Date: (optional): <date>Period (optional): <period>Fiscal Year: <year of posting document>Posting Date (optional): <date> | The approved document is listed. |  |

### Forward Verify Currency Adjustments (for Processor- Inbox)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You receive currency adjustment documents that must be checked before final posting. After checking, you can forward the currency adjustment documents to another processor to approve with a comment. The system checks the new processor's posting authorization for the company code. Once a document is forwarded, it leaves your list and goes to the new processor's inbox.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for United Arab Emirates . |  |  |
| 2 | Access the SAP Fiori App | Open Verify Journal Entries in General Ledger - For Processor (Inbox) (F2728). | The My Inbox view displays. |  |
| 3 | Forward Documents | Select the document to be forwarded and choose Forward. | The Forward dialog box is displayed. |  |
| 4 | Add Recipient | Enter the name of the recipient and choose Search. | The dialog box shows a list of matching names. |  |
| 5 | Select Recipient | Choose the name of the recipient. | The Forward dialog box changes to show the recipient name and a new field. |  |
| 6 | Add Reason | Make the following entries and choose Forward:Forward Note: <reason for forwarding, such as changing a G/L account> | The document is forwarded. |  |

### Reject Verify Currency Adjustments (for Processor- Inbox)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You receive currency adjustments that must be checked before final posting. After checking the adjustments, you can either approve or reject them with a comment or reason. When you select and reject an adjustment, it's removed from the list and sent back to the requester.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using the General Ledger Accountant for United Arab Emirates role. |  |  |
| 2 | Access the SAP Fiori App | Open Verify Journal Entries in General Ledger - For Processor (Inbox) (F2728). | The My Inbox view displays. |  |
| 3 | Reject Documents | Select the document to be rejected.Choose Reject and enter the reason for rejection, for example,change G/L 10010000 to 12540000 | The document is rejected. |  |

### Edit a Rejected Verify Currency Adjustment (Requester)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The currency adjustments must be checked before final posting. The adjustment you submitted is rejected. For it to be approved and posted, you must make the changes requested by the approver.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Verify Currency Adjustments - For Requester (F4670A). |  |  |
| 3 | Select Journal Entry | Make the following entry and choose Go.Company Code: 3310 | The journal entries are listed. |  |
| 4 | Edit Rejected Journal Entry | Click the desired rejected journal entry number.Select the journal entry to be edited.Choose Edit.Change the journal entry based on the comments entered, for example, change G/L account 10010000 to 12540200.Choose Submit. | The changed journal entry is resubmitted for approval. |  |

### Verify Data Flow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use error suspense handling when a direct posting through the Perform Foreign Currency Valuation (FAGL_FCV) app fails.

Prerequisite

You executed the Perform Foreign Currency Valuation (FAGL_FCV) app, but a posting indicates an error (such as a missing cost center).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Verify Data Flow (ACC_ECS_MAINTAIN). | The Error Correction and Suspense Accounting Selection Screen is displayed. |  |
| 3 | Make Entries | Make the following entries and choose Execute.Co. Code of Pstd Doc.: 3310 | If there are no documents with errors, the system displays an empty list. |  |
| 4 | Process Error | Select a line with an error and choose Start Processing. | The Error Correction and Suspense Accounting: Processing of ECS Items view is displayed. |  |
| 5 | Show Detail | Select the line and choose Detail Screen. | The ECS Item: Detail View view displays. |  |
| 6 | Correct Additional Fields | Choose Additional Input Fields. Make any necessary corrections. |  |  |
| 7 | Post | Choose Save. |  |  |

### Perform Advanced Foreign Currency Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform advanced foreign currency valuation.

|  |
| --- |
| Note If there are no postings in the productive system, you can deactivate Advanced Foreign Currency Valuation. |

|  |
| --- |
| Note To run advanced foreign currency valuation for a different ledger (such as 2L (IFRS) or 3L (USGP)), you must create a financial statement version for IFRS/USGP (based on YCOA) first, then assign it and YCOA to the IFRS/USGP accounting principle together. |

Prerequisites

Ensure that you've maintained the following settings in the Preliminary Steps section:

- [Define Rules for Advanced Foreign Currency Valuation](#unique_21) [page ] 20
- [Assign Rules for Foreign Currency Valuation to Accounting Principles](#unique_22) [page ] 23
- [Assign Semantic Tags to Financial Statement Versions](#unique_20) [page ] 19
    - Only the G/L accounts assigned to the semantic tag; FX is included in the foreign currency valuation run.

Ensure that a different exchange rate is maintained for each period to test the foreign currency valuation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule General Ledger Jobs (F1927). | The Application Jobs view is displayed. |  |
| 3 | New Job | Choose Create. | The New Job: Advanced Foreign Currency Valuation view is displayed. |  |
| 4 | Selection Criteria for Step 1 | Make the following entries and choose Step 2:Job Template: Advanced Foreign Currency ValuationJob Name: Advanced Foreign Currency Valuation |  |  |
| 5 | Selection Criteria for Step 2 | Make the following entries and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Selection Criteria for Step 3 | Make the following entries and choose Schedule:Company Code: 3310Ledger: 0LValuation Key Date: <last day of the current month>Update Run: SelectedNote If Update Run is selected, the run is done as a productive run. If it's deselected, the run is done as a test run. | The run is scheduled.Note If you want to use a different ledger (such as 2L or 3L), see the Note in the Purpose statement above for more information. |  |
| 7 | Review Results | To review details of the foreign currency valuation, choose Log or Results. |  |  |

### Analyze Closing Run Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the results of the closing run.

|  |
| --- |
| Note For more information on this app, see [this page](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/372bd396f8684a0aa642dd40ea5d67bd.html?version=LATEST) on the SAP Help Portal. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Analyze Closing Run Results (F3753). |  |  |
| 3 | Enter Details | Make the following entries and choose Go:Job Template: Advanced Foreign Currency Valuation (SAP_FIN_GL_FOR_CURR_VAL_ADV)Note Optionally, enter additional filter values to shorten the results list. | The system displays a list of results. |  |
| 4 | Details | For one of the rows in the Closing Runs pane, choose > (Details). | The system displays details of the selected closing run. |  |
| 5 | Review | Review the data shown, which includes target currency roles, G/L accounts, group IDs, document numbers, amounts in source and target currencies, and differences. |  |  |
| 6 | Quick Filter | You can use the All, Failed, or Successful buttons at the top of the pane to quickly view items meeting those criteria. |  |  |
| 7 | Messages | You can choose the Messages tab to view related messages. You can use theSeverity and search fields to filter the messages. |  |  |
| 8 | More Filtering | To perform further filtering of the items (for example, for a specific currency role), choose the Settings button. On the dialog box, choose the Filter tab. Define your field and value to filter on and choose OK. |  |  |

### Credit-Risk-Based Impairment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Due to the new impairment model of IFRS 9, expected credit losses (ECL) on trade receivables are calculated using a provision matrix. This matrix applies fixed provision rates based on the number of days the receivable is outstanding. To calculate the provisioned amounts, you can periodically perform a valuation run to calculate the bad debt expense posting for overdue item.

Prerequisites - Configuration Activities

Execute the following prerequisites in the Preliminary Steps section:

- [Activate Advanced Valuation](#unique_12) [page ] 12
- [Define Aging Increments for Advanced Valuation](#unique_24) [page ] 24
- [Assign Risk Class in Business Partner Master Data](#unique_26) [page ] 25
- [Assign Semantic Tags to Financial Statement Versions](#unique_27) [page ] 26
- [Define Rules for Impairment](#unique_28) [page ] 27
- [Assign Rules for Impairment to Accounting Principles](#unique_29) [page ] 30
- Write-off functionality is currently not supported.

Prerequisite – Open Customer Invoice

Open receivables exist in the system that satisfy the risk class requirements, based on number of days overdue.

|  |
| --- |
| Note To determine if the impairment calculation is based on the net or gross amount of the receivable, we deliver a configuration step: Country/Region-Specific Settings for Impairment: Net or Gross.If you access this configuration step via the Manage Your Solution (F1241) app, you can find it in Application Area Finance, Sub Application Area General Ledger. Choose Ledgers and Valuation. In the right pane, choose Configure for the Country/Region-Specific Settings for Impairment: Net or Gross.If you access this configuration step via the project experience in SAP Central Business Configuration, Go to the Business Processes Configuration app. Search for Country-Specific Settings for Impairment: Net or Gross and choose Go to Activity. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |

Procedure

| Process Step# | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Schedule General Ledger Jobs (F1927). |  |  |
| 3 | Create Impairment Run | Choose Create. |  |  |
| 4 | Template Selection | Make the following entries and choose Step 2:Job Template: Post Credit-Risk-Based ImpairmentJob Name: Post Credit-Risk-Based Impairment |  |  |
| 5 | Scheduling Options | Make the following entries and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Parameters | Make the following entries and choose Schedule:Selection Parameters section:Company Code: 3310Ledger: 0LKey Date Parameters section:Key Date: Selected (only if you use it)Valuation Key Date: Last day of previous monthDynamic Key Date: Selected (only if you use it)Dynamic Valuation Key Date : Last day of previous monthProcessing Options section:Test Run: Selected (to run in test mode)Update Run: Selected (to run in update mode) | The log is created, and the result of the process is displayed. |  |

### Balance Sheet Reclassification

#### Post B/S Reclassification - Master Data Change

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can reclassify payables and receivables when the associated business partner or reconciliation account changes. This feature updates amounts according to the modified data, ensuring accurate financial records.

|  |
| --- |
| Note If your system is configured with Balance Sheet Reclassification with delta posting logic and you want to migrate to Balance Sheet Reclassification with reversal posting logic, see the following pages on the SAP Help Portal for more information on reversal logic:[Post B/S Reclassification](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/98d060a69b8a47e6a83e60104943d756.html?version=LATEST)[Migrate B/S Reclassification Postings to Reversal Posting Logic](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/3a550616fb564c08b368573671714d8c.html?version=LATEST) |

|  |
| --- |
| Caution If you are performing balance sheet reclassification by master data change as well as maturity, perform the balance sheet reclassification by master data change first, then perform the balance sheet reclassification by maturity afterward. |

Prerequisites

Ensure that you've executed the following preliminary steps and test procedure steps:

- [Activate Advanced Valuation](#unique_12) [page ] 12 (mandatory)
- [Define Financial Statement Versions](#unique_19) [page ] 63
- [Assign Semantic Tags to Financial Statement Versions](#unique_34) [page ] 35
- [Assign Financial Statement Versions to Accounting Principles](#unique_14) [page ] 14
- [Define Aging Increments for Advanced Valuation](#unique_37) [page ] 37 (optional)
- [Define Rules for Balance Sheet Reclassification by Maturity](#unique_32) [page ] 39 (mandatory for G/L accounts and Reclassification Method assignment)
- [Define Rules for Determining Account Assignments in G/L Processes](#unique_16) [page ] 15
- [Define Rules for B/S Reclassification by Master Data Change](#unique_33) [page ] 33
- [Assign Reclassification Rules to Accounting Principles](#unique_39) [page ] 42 (optional)
- Ensure that you have met the prerequisites listed on [this page](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/98d060a69b8a47e6a83e60104943d756.html?version=latest) on the SAP Help Portal.

You should have receivables and payables invoices that should be reclassified based on credit/ debit balance available in the system.

Procedure

| Process Step# | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Schedule General Ledger Jobs (F1927). |  |  |
| 3 | Create New Run for Reclassification | Choose Create. | The New Job view is displayed. |  |
| 4 | Create New Run for Reclassification | Make the following entries and choose Step 2:Job Template: Post B/S Reclassification - Master Data ChangeJob Name: Post B/S Reclassification - Master Data Change |  |  |
| 5 | Scheduling Options | Make the following entries and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Selection Criteria and Schedule Job | Make the following entries and choose Schedule:Company Code: 3310Ledger: 0LKey Date Parameter section:Note Select either Key Date or Dynamic Key Date per your use case.Reversal Key Date: Selected (only if you use it)Balance Key Date: <last day of previous month>Dynamic Calendar Year/Period: Selected (only if you use it)Dynamic Reversal Key Date: <last day of previous month>Reversal Date Parameters section:Note Select either Reversal Date for Valuation Run or Dynamic Date per your use case.Reversal Date for Valuation Run: Selected (per your use case)Reversal Date: <reversal date>Dynamic Date: Selected (per your use case)Dynamic Reversal Date for Reclassification: <reversal date>Process Options section:Note Select either Test Run or Update Run per your use case.Test Run: Selected (to run in test mode)Update Run: Selected (to run in update mode) | When the job is complete, the output contains administrative information along with the reclassification results (valuation in functional currency, company code currency and/or group currency). You can also review logs if needed. |  |

#### Post B/S Reclassification - Maturity

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the balance sheet reclassification for maturity.

|  |
| --- |
| Note If your system is configured with Balance Sheet Reclassification with delta posting logic and you want to migrate to Balance Sheet Reclassification with reversal posting logic, see the following pages on the SAP Help Portal for more information on reversal logic:[Post B/S Reclassification](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/98d060a69b8a47e6a83e60104943d756.html?version=LATEST)[Migrate B/S Reclassification Postings to Reversal Posting Logic](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/3a550616fb564c08b368573671714d8c.html?version=LATEST) |

Prerequisites

Ensure that you've executed the following preliminary steps:

- [Activate Advanced Valuation](#unique_12) [page ] 12 (mandatory)
- [Define Aging Increments for Advanced Valuation](#unique_37) [page ] 37 (optional)
- [Define Rules for Balance Sheet Reclassification by Maturity](#unique_32) [page ] 39 (mandatory for G/L accounts and Reclassification Method assignment)
- [Assign Reclassification Rules to Accounting Principles](#unique_39) [page ] 42 (optional)
- Ensure that you have met the prerequisites listed on [this page](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/98d060a69b8a47e6a83e60104943d756.html?version=latest) on the SAP Help Portal.

You should have receivables and payables invoices that should be reclassified based on credit/ debit balance available in the system.

Procedure

| Process Step# | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Schedule General Ledger Jobs (F1927). |  |  |
| 3 | Create New Run for Reclassification | Choose Create. | The New Job view is displayed. |  |
| 4 | Create New Run for Reclassification | Make the following entries and choose Step 2:Job Template: Post B/S Reclassification - MaturityJob Name: Post B/S Reclassification - Maturity |  |  |
| 5 | Scheduling Options | Make the following entries and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Selection Criteria and Schedule Job | Make the following entries and choose Schedule:Company Code: 3310Ledger: 0LKey Date Parameter section:Note Select either Key Date or Dynamic Key Date per your use case.Key Date: Selected (only if you use it)Balance Key Date: <last day of previous month>Dynamic Calendar Year/Period: Selected (only if you use it)Dynamic Balance Key Date: <last day of previous month>Reversal Date Parameters section:Note Select either Reversal Date for Valuation Run or Dynamic Date per your use case.Reversal Date for Valuation Run: Selected (per your use case)Reversal Date: <reversal date>Dynamic Date: Selected (per your use case)Dynamic Reversal Date for Reclassification: <reversal date>Process Options section:Note Select either Test Run or Update Run per your use case.Test Run: Selected (to run in test mode)Update Run: Selected (to run in update mode) |  |  |

### Manage Posting Periods

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you close the posting periods and open the new accounting periods. Usually, only the current posting period is open for posting. All other posting periods are closed. At the end of this posting period, the period is closed and the next posting period is opened. You should specify at least one account type (Valid for all account types) for each open posting period. You can exercise more detailed control by specifying further account types.

|  |
| --- |
| Note You have two options for the SAP Fiori app. Procedure - Option 1 shows the steps for Manage Posting Periods - Cost Accounting (F4684)). Procedure - Option 2 shows the steps for ( Manage Posting Periods (F2293)). |

Procedure - Option 1

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Posting Periods - Cost Accounting (F4684). |  |  |
| 3 | Enter Details | Make the following entries and choose Go:Company Code: 3310Fiscal Year: <current fiscal year>Fiscal Period: <fiscal period>Ledger: <ledger>Bus. Transac. Type: <transaction type>Note You may need to choose Adapt Filters to display some fields. | The lower pane displays a filtered list. |  |
| 4 | Open or Close Period | If necessary, expand the nodes to view the subobjects. Use the > buttons to do this.When you find the period, select the checkbox for its row.To open the period, choose the Open button.To close the period, choose the Close button. |  |  |

Procedure - Option 2

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Posting Periods (F2293). |  |  |
| 3 | Enter Details | Make the following entries and choose Go:Posting Period Variant: 3310Fiscal Year Variant: K4 | The list shows entries for the posting period and fiscal year variants. |  |
| 4 | CO Period Status | Select the checkbox for the row that contains the Valid for All Account Types value and choose CO Period Status. | The Manage Posting Periods - Cost Accounting view is displayed. |  |
| 5 | Fiscal Year | Make the following entries and choose Go:Fiscal Year: <fiscal year> | The lower pane displays the posting period data. |  |
| 6 | Display Controlling Period Status | Review the status. When you are done, choose Back. | The CO period status is displayed. |  |
| 7 | Select Period | Note If the Items pane is empty when you return from the prior step, choose Go again to redo the search.Select a line from the Posting Periods pane and choose Set Posting Periods > Open Periods . | The Set Posting Periods - Open Periods view is displayed. |  |
| 8 | Set Period | Enter the period and year information and choose OK. | Your setting is saved. |  |

### Post Tax Payables

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can't normally post directly to the output tax account, meaning that you can't make a transfer posting for the account balance directly to the tax payable account. Use this app to pay tax amounts by posting the balances of input and output tax accounts to a tax payable account. The app doesn't require entry of a tax code, so you can make manual adjustments to tax accounts directly. You can make these postings in all relevant ledgers for your accounts.

|  |
| --- |
| Note For some countries/regions that have applicable reports, if you activated Compliance Formats – Support Preparation (1J2), you may have the option to execute the Post Tax Payables step through Document and Reporting Compliance instead of using this procedure. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post Tax Payables (F1597). |  |  |
| 3 | Enter Header Details | Make the following entries and press Enter:Company Code: 3310Journal Entry Date: <Current date>Posting Date: <Current date>Transaction Currency: AEDJournal Entry Type: <document type>, for example, SA |  |  |
| 4 | Enter Line Item Details | Make the following entries and press Enter:G/L Account: for example, 22000000Debit/Credit: <amount> | The Post Tax Payable view is displayed. |  |
| 5 | New Line | Make the following entries and press Enter:G/L Account: For example, 21503000Debit/Credit: <amount> |  |  |
| 6 | Post | Choose Post. | You posted the tax amounts to a tax payable account manually. |  |

### General Ledger - Periodic Activities

#### Tax Reconciliation Account Balance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check that the tax-relevant G/L accounts are posted with tax. Additionally, you compare if there are differences between the calculated tax and posted tax.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Tax Reconciliation Account Balance (F2095). |  |  |
| 3 | Enter Data | Make the following entries and choose Go:Company Code: 3310Fiscal Year: <Fiscal year>Tax Code: <Tax code>G/L Account: <Account number> | The Account Balances for Journal Entries with Tax Codes list is created. Look at the Difference Amount column, where the differences between Tax Amount (posted) and Calculated Tax are displayed. |  |
| 4 | Drilldown | To navigate to Information on line item level for one journal entry, choose one G/L account, then choose one Tax Code and select a Journal Entry. | When you choose the G/L account you can switch to other reports, for example, Display G/L Line Items. |  |
| 5 | Change Layout | Choose Settings.Select the Profit Center and Business Place and choose OK. | The new columns Profit Center and Business Place display. |  |

#### Tax Declaration Reconciliation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check that the tax base and reported (posted) tax per tax code are correct. The tax code is assigned to a tax box.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Tax Declaration Reconciliation (F2096). |  |  |
| 3 | Enter Data | Make the following entries and choose Go:Company Code: for example, 3310Tax Code: <Tax Code>Posting Period: <Posting period>Fiscal Year: <Fiscal year> | The Tax Boxes and Tax Codes list is created. Check the Difference Amount column, where the differences between LC tax amount (posted) and Tax Calculated are displayed. |  |
| 4 | Drilldown | To view the posting document numbers, for a line item, choose Show Details (>). | The Tax Box and Tax Code view is displayed. The journal entry numbers are shown in the lower pane. |  |

### Withholding Tax Calculation Analysis Report (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform the withholding tax calculation analysis report. The app shows how the withholding tax is calculated based on the transactional and master data.

There are three scenarios you can use the app for:

- Review the calculation of the witholding tax at the time of invoice
- Review the calcluation of the withholding tax at time of payment
- Review when parameters aren't maintained for withholding tax

|  |
| --- |
| Note For more information on the app, see [this page](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/efd4dba63cb04ac19b3059d7a7859208.html?version=latest) on the SAP Help Portal. |

Prerequisites

Ensure that you have an invoice posted or payment document created. For more information, see the following:

- Accounts Payable (J60)
    - Invoice - See the Enter Invoice Without Sales Order topic
    - Payment - See the Payment Plans topic
- Accounts Receivable (J59)
    - Invoice - See the Enter Invoice Without Sales Order topic
    - Payment - See the Incoming Payments section

Procedure - Review at Time of Invoice

| Test Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Withholding Tax Calculation Analysis (F7977). |  |  |
| 3 | Enter Details | Make the following entries and choose Go:Company Code: 3310Journal Entry: <journal entry number>Fiscal Year: <fiscal year> | The system displays a withholding tax document item in the lower pane. |  |
| 4 | Details | For the item, choose Details (>). | The Withholding Tax Calculation view is displayed. |  |
| 5 | Review | The General Information pane shows general information for the chosen journal entry, such as withholding tax type, withholding tax code, when it was posted, the region, and so on. For this journal entry, the Withhholding Tax Posting Time field shows that it's posted at the time of invoicing.Review the Formula, Basic Information, and Rules Applied panes. The Formula pane shows the calculation of the base amount and withholding tax amount. The Basic Information pane shows obligated period, valid period, and so on. The Rules Applied pane shows the rules that are applied for the chosen journal entry. | You can use the information gained here on this screen if you need to perform any necessary corrections. |  |
| 6 | Back | Choose Back. |  |  |

Procedure - Review at Time of Payment

| Test Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Withholding Tax Calculation Analysis (F7977). |  |  |
| 3 | Enter Details | Make the following entries and choose Go:Company Code: 3310Journal Entry: <journal entry number>Fiscal Year: <fiscal year> | The system displays a list of withholding tax document items in the lower pane. Two line items are displayed (an invoice and a payment document). The Clearing Journal Entry field of both line items references the journal entry number of the other line item (payment document). |  |
| 4 | Details | For the invoice item, choose Details (>). | The Withholding Tax Calculation view is displayed. |  |
| 5 | Review | The General Information pane shows general information for the chosen journal entry, such as withholding tax type, withholding tax code, when it was posted, the region, and so on. For this journal entry, the Withhholding Tax Posting Time field shows that it's posted at the time of payment. The Clearing Journal Entry field shows the journal entry number of the clearing document.Review the Formula, Basic Information, and Rules Applied panes. The Formula pane shows the calculation of the base amount and withholding tax amount. The Basic Information pane shows obligated period, valid period, and so on. The Clearing Posting Date field shows the date of the clearing post.The Rules Applied pane shows the rules that are applied for the chosen journal entry. | You can use the information gained here on this screen if you need to perform any necessary corrections. |  |
| 6 | Back | Choose Back. |  |  |

Procedure - Review when Witholding Tax Parameters aren't Maintained

| Test Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Withholding Tax Calculation Analysis (F7977). |  |  |
| 3 | Enter Details | Make the following entries and choose Go:Company Code: 3310Journal Entry: <journal entry number>Fiscal Year: <fiscal year> | The system displays a message Withholding tax has not been calculated for certain items due to current configuration settings. For more information, please click here. |  |
| 4 | View Message | Click the link in the message. | The system display a message dialog box stating No withholding tax type assigned to BP. |  |
| 5 | Choose OK | Choose OK. |  |  |

### Regroup Receivables/Payables

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You must carry out adjustment postings in the following cases:

- Sorted list according to remaining terms
- Vendors with a debit balance and customers with a credit balance
- Modified reconciliation accounts or partners (VBUND)

The system processes all accounts that are maintained by open item management. For each transfer posting created, a reset posting is also included in the session. For customer or vendor reconciliation accounts, the system posts to an adjustment account.

The report regroups the receivables and payables in accordance with the required sort method (SAP, for example) and performs transfer postings.

|  |
| --- |
| Note If Advanced Valuation is activated (the system displays an error message Advanced valuation active; you can no longer use the old report. Message no. FINS_FI_CLS023 is raised) and as long as there is no posting in the P system, you can deactivate this. To deactivate this, use the Activate Advanced Valuation configuration step (available in the Manage Your Solution (F1241) app (for more information on accessing the configuration step, see the [Activate Advanced Valuation](#unique_12) [page ] 12 topic). Now, you can run Regroup Receivables / Payables (FAGLF101). |

Prerequisites

You posted open items to customers and vendors. At the end of a fiscal year (period), you noticed that some customers have a credit balance and some vendors have a debit balance. During the posting period, the reconciliation account of some customers or some vendors or their status (affiliated, associated, or third party) has changed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Regroup Receivables / Payables (FAGLF101). | The Balance Sheet Supplement - OI - Analysis view is displayed. |  |
| 3 | Enter Selection Criteria | Make the following entries:Company Code: 3310Balance Sheet Key Date: <date, such as 12/31/CurrentFY>Sort method: SAP (EU 93 fin. stat guidelines)Valuation Area: AE for local GAAPPostings tab:Generate Postings: SelectedUse Batch Input Instead of ECS: selected (a batch input session FAGL_CL_REGR is automatically created)Document date: <date, such as 12/31/CurrentFY>Journal Entry Type: SAPosting date: <date, such as 12/31/CurrentFY>Posting Period: 12Reversal Document Type: SAReversal posting date: <date, such as 01/01/<current fiscal year + 1>>Reverse Posting Period: 01Selections tab:Account Type: D to KSupplier: <supplier ID>Customer: <customer ID> |  |  |
| 4 | Execute | Choose Execute. | The receivables and payables are regrouped.If a batch input session is created, process it as described in the section Process Batch Input Session. |  |

### Process Batch Input Session

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity runs the batch input session.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Batch Input Sessions in My Area (SM35SA). | The Batch Input: Session Overview view is displayed. |  |
| 3 | Select and Process Session | Select the session to execute and choose Process. | The Process Session XXXXX dialog box is displayed. |  |
| 4 | Selection Criteria | Select one of the following options and choose Process:Processing Mode: Select one of the optionsNote If you select Process/foreground, you must press Enter until the batch input session is completely processed.Additional functions: Select one or more of the options | Journal entries are posted and recurring documents are updated with processing data (next run on and number of runs).Note You can filter the list of batch input sessions by choosing the tabs above the list. |  |

### Import Financial Plan Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you plan the balance sheet and P&L accounts.

|  |
| --- |
| Caution After running this process, if you want to upload a second Excel file, exit the app and refresh your browser cache before you run the process again with the second file. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Import Financial Plan Data (F1711). |  |  |
| 3 | Download Template | Choose Download Templates. | The Download Templates dialog box displays. |  |
| 4 | File Parameters | Make the following entries, then choose P&L Statement Planning:Separator for .csv file: <select a separator character>Note Once you click the template link, the file is downloaded to your PC. Choose Close on the dialog box.Note Repeat this step with Balance Sheet Planning. | The Excel template file is downloaded.Note The P&L Statement Planning and Balance Sheet Planning templates are downloaded. |  |
| 5 | Prepare the P&L Statement Planning Template | Open the P&L Statement Planning template file in Excel, make the following changes, and save it locally:Plan Category; PLNGeneral Ledger Fiscal Year: <Current year>Posting Period: for example 4Company Code: 3310Account Number: for example, 63003000Amount in Global Currency: amountGlobal Currency: for example, USDNote Although this is a P&L plan figures upload, the template doesn't cater for cost centers or profit centers. Uploaded plan data doesn't contain these dimensions. Use the relevant templates to enable posting with Cost Centers/Profit Centers such as Cost Center Planning/Profit Center Planning, for example – or upload plan data for balance sheet accounts. |  |  |
| 6 | Prepare the Balance Sheet Planning Template | Open the Balance Sheet Planning template file in Excel, make the following entries in the Balance Sheet Planning template file, and save it locally:Plan Category: PLNGeneral Ledger Fiscal Year: <Current year>Posting Period: for example, 4Company Code: 3310Account Number: for example, 10010000Amount in Company Code Currency: amountCompany Code Currency: for example, AED |  |  |
| 7 | Upload Excel File | In the Source File field, choose the Browse .csv files button and choose the prepared Excel files. Afterward, choose Open.Choose Import Source File. | The Excel file is uploaded and you can see data entered in the app.Note The uploaded plan data can be displayed using the Balance Sheet/Income Statement (F0708) app. |  |

### Balance Sheet / Income Statement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the financial statement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Balance Sheet/Income Statement (F0708). |  |  |
| 3 | Enter Details | Make the following entries and choose Go:Company Code: 3310Ledger: 0LStatement version: 33 10Statement Type: for example, Normal (Actual - Actual)End Period: <current period>Comparison End Period: <same period from previous year>Currency: AED | The financial statement for the selected company code displays. |  |
| 4 | Display Financial Statement for Multiple Company Codes | Repeat the test by entering more than one company code into the Company Code field. | The financial statement for multiple company codes displays. |  |
| 5 | Balance Sheet | Choose the Balance Sheet tab. |  |  |
| 6 | Export to PDF | Choose the Create PDF Preview button. | The financial statement is exported to PDF. |  |

#### Financial Statement Download and Printing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you download and print the financial statement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Balance Sheet/Income Statement - Multidimensional (W0161). |  |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Ledger: For example, 0L for Leading LedgerCompany Code: 3310Hierarchy ID: 3310From period: For example, 1To period: For example, 10Fiscal Year: <Current year>Comparison ledger: For example, 0L for Leading LedgerComparison From Period: For example, 1Comparison To Period: For example, 10Comparison Fiscal Year: <Previous year>Currency Type: 10 (Company Code Currency)Plan Category: ACT01, Actual | The Financial Statement - Grid-based screen displays. |  |
| 4 | Export to Excel | In the upper right corner, choose Export as. Ensure you export the file as an Excel file. | The financial statement is exported locally as an Excel file. |  |

#### Financial Statements Review Booklet

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the financial statements with this new app. Presently, you can review the Balance Sheet, Profit & Loss, Cash Flow Statement, and Statement of Changes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Financial Statements - Review Booklet (F8587). |  |  |
| 3 | Enter Details | Make the following entries and choose Go:Ledger: <ledger>Company Code: 3310Fiscal Year: <fiscal year>Financial Statement Version: <financial statement version>From Fiscal Period: <start period>To Fiscal Period: <end period>Comparison Fiscal Year: <fiscal year>Comparison From Period: <start period>Comparison To Period: <end period>Currency Type: <company code currency> | The lower pane is displayed. Separate tabs are available. Additional actions are available on the right side of the pane. |  |
| 4 | Review | Expand and review the displayed content.You can select the Columns dropdown to switch between Comparison Type and Reporting Year vs. Previous Year.You can also select the Rows dropdown to switch between Reporting Level, FSV Node ID (by itself or with functional area or GL account), or GL Account View.You can also right-click the column headers to change the amount of hierarchy displayed, among other options.The action buttons in the right pane can be used to apply page filters, change layout or formatting, provide context information, or export information. |  |  |

### Trial Balance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the trial balance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Trial Balance (F0996). | A dialog box is displayed. |  |
| 3 | Enter Details | Make the following entries and choose OK:Ledger: 0L for leading ledger with local GAAPCompany Code: 3310Posting Date From: for example, <First day of current period>Posting Date To: for example, <Last day of current period>Note To display a readable amount of data in the chart, you can apply additional filters in the filter bar for G/L Account. This ensures that a reasonable data set is selected for graphical display. | The trial balance is shown. |  |

### Year-to-Date Balances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you view the year-to-date account balances.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Year-to-Date Balances (W0177). |  |  |
| 3 | Enter Details | Make the following entries and choose Go:Ledger: <ledger> for example, 0LLedger Fiscal Year: for example, <current year>Company Code: <company code>Posting Date: <posting date> | The Data Analysis pane shows a list of matching account balances. |  |
| 4 | Navigation Panel | In the top left of the view, choose Navigation Panel. | The Navigation Panel pane is shown on the left side of the screen. |  |
| 5 | Profit Center | In the Available Fields section of the Navigation Panel pane, for the Profit Center field, choose the Add field to rows axis button to the left of the field name. | The Profit Center field is added to the Rows section of the Navigation Panel and is added to the data view in the right pane. |  |
| 6 | Reorganize Fields | In the Navigation Panel pane, in the Rows section, drag and drop Profit Center above G/L Account. | The data view in the right pane is updated to reflect the order change. The grouping is now organized by profit centers. |  |

### Balance Carryforward Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can view the status of the balance carryforward jobs.

The balance carryforward run (which carries forward account balances for all currencies into the new fiscal year) is automatically scheduled two weeks before the start of a new fiscal year and opening balance for a fiscal year are made available. Balances are also automatically updated whenever postings are made to the previous fiscal year. To handle postings that are made while a balance carryforward run is in process, balances are carried forward one day after the automatic balance carryforward is activated. Carryforward to current year isn't possible if the previous year is closed in Asset Accounting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Balance Carryforward Status (F4683). |  |  |
| 3 | Enter Details | Make the following entries and choose Go:To Fiscal Year: <fiscal year to which balances are carried forward>Company Code: For example, 3310 | The Balance Carryforward Status pane shows a list of results. |  |
| 4 | Review Log | Analyze the Status column for the jobs. To view detailed status for a particular job, click the status message for that job. | The Log Details view displays the detailed status for the selected job. |  |

### Display Journal Entries - in T-Account View

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This app uses t-account visualization control to help accountants to better understand the impact of a selected set of accounting documents that are typically related (such as originating from the same business process).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Journal Entries - In T-Account View (F3664). |  |  |
| 3 | Enter Accounting Document | Make the following entries and choose Go:Journal Entry: <accounting document number> | The system displays the accounting document details in the left pane, and shows the affected accounts in the right pane. The required fields are automatically populated based on the journal entry. |  |

### Statement of Changes in General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you examine general ledger account postings by transaction type.

The Statement of Changes in General Ledger (W0162) app shows G/L accounts in combination with transaction types, letting you analyze account balance movements in more detail. The accounts and transaction types used in the app depend on the selected type of statement of changes. The type collects all settings for a specific statement of change (for example, for statement of changes in equity or provisions or others).

The statement of changes type is defined in the system configuration. It includes the assignment of relevant G/L accounts via semantic tags and the relevant transaction types. These relevant accounts aren't directly assigned to the statement of changes type. A semantic tag is used instead. The semantic tag must first be defined and assigned to one or several nodes or accounts in an account hierarchy.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Statement of Changes in General Ledger (W0162). | The Statement of Changes view is displayed. |  |
| 3 | Enter Details | Make the following entries and choose Go:Statement of Changes Type: <statement of changes type> for example, SOCLedger: <ledger>, for example, 0LCompany Code: 3310Fiscal Year: <current year>To Period: for example, 012Currency Type: for example, 10 | The Data Analysis pane shows the relevant data, including G/L accounts, transaction types, and amounts. This corresponds to the structure defined in the Preliminary Steps section. Transaction types and accounts are displayed in the table. |  |
| 4 | Review Data | Review the statement of changes.Note To display additional fields, you can choose Drilldown and select the additional fields (such as Profit Center, Controlling Area, and so on) to display.Note If you want to analyze content in a different app, select a row in the Data Analysis pane and choose Jump to in the upper right corner of the pane. From the Jump to menu, choose the desired app to view and analyze the content. |  |  |

### General Ledger Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the General Ledger Overview report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Set Default Value for SAP Fiori Launchpad User Settings (Optional) | On the SAP Fiori launchpad, go to User > Settings > Default Values . | The following input fields are available:Display CurrencyFin. Statement Vers.LedgerCompany CodeYou can enter and save default values. |  |
| 3 | Access the App | Open General Ledger Overview (F2445). |  |  |
| 4 | Filter | Fill out the following required fields on the filter bar:Display CurrencyKey DateStatement VersionLedgerCompany CodeChoose Go.If a default value is set in the SAP Fiori launchpad user settings, the previous filters have been automatically populated with the default values. | The overview page launches successfully and the following cards are displayed (the exact names may vary):Recognized RevenueRecognized Cost of SalesJournal Entries to be VerifiedG/L Account BalanceVerified Journal EntriesQuick LinksMy InboxTax Reconciliation Account BalanceG/L item ChangesDays Payable Outstanding IndirectDays Sales Outstanding |  |
| 5 | Set Global Filters | The global filters can be changed in the global filter bar. Set the values in the fields of the global filter. Choose Go to refresh the content that is displayed on the overview page. | The global filter applies to the results of the cards on the overview page. |  |
| 6 | Manage Cards | To customize the cards on the overview page, choose the user icon on the screen, choose Manage Cards, make the settings of your choice, and then choose OK. | The cards on the overview page can be rearranged, hidden, and displayed again. |  |
| 7 | Navigate from Card G/L Account Balance | Navigate from G/L Account Balance.Choose the header (or line point) of the card to get further information. | The overview page navigates you to the target apps. The global filter and header (or line item) information is carried over.The card navigates you to the Balance Sheet/Income Statement - Multidimensional SAP Fiori app.If you choose one line item, you are directly navigated to the selected account group. |  |
| 8 | Navigate from Card Journal Entries to Be Verified | Navigate from Journal Entries to Be Verified.Choose the header (or line point) of the card to get further information. | The overview page navigates you to the target apps. The global filter and header (or line item) information is carried over.The card navigates you to the Verify General Journal Entries SAP Fiori app.If you choose one line item, you are directly navigated to the selected Journal Entry. |  |
| 9 | Navigate from Card Quick Links | Navigate from Quick Links.Choose the following links in the card to get further information:Display Line Items in General Ledger (F2217)Manage Journal Entries (F0717A)Post General Journal Entries (F0718)Post Cash Journal Entries (FBCJ)Clear G/L Accounts - Manual Clearing (F1579) | The overview page navigates you to the target apps.If you choose each item, the card navigates you to the corresponding SAP Fiori app. |  |
| 10 | Navigate from Card Verified Journal Entries | Navigate from Verified Journal Entries.Choose the header (or line point) of the card to get further information. | The overview page navigates you to the target apps. The global filter and header (or line item) information is carried over.The card navigates you to the Verify General Journal Entries SAP Fiori app.If you choose one line item, you are directly navigated to the selected Journal Entry. |  |
| 11 | Navigate from Card Tax Reconciliation Account Balance | Navigate from Tax Reconciliation Account Balance.Choose the line item of the card to get further information. | The overview page navigates you to the target apps. The global filter and header (or line item) information is carried over.The card navigates you to the Tax Reconciliation Account Balance SAP Fiori app.If you select one line item, you are directly navigated to the selected G/L account. |  |
| 12 | Navigate from Card G/L Item Changes | Navigate from G/L Item Changes.Choose the header (or line point) of the card to get further information. | The overview page navigates you to the target apps. The global filter, header, or line item information is carried over.The card navigates you to the Audit Journal (F0997) SAP Fiori app.If you select one line item, you are directly navigated to the selected journal entry. |  |
| 13 | Navigate from Card Days Payable Outstanding Indirect | Navigate from Days Payable Outstanding Indirect.Choose the header (or each item) of the card to get further information.Note Extra SAP_BR_AP_MANAGER role is required for your user to navigate from this card. | The overview page navigates you to the target apps. The global filter and header (and each item) information is carried over.The card navigates to the Days Payable Outstanding Indirect SAP Fiori app. |  |
| 14 | Navigate from Card Days Sales Outstanding | Navigate from Days Sales Outstanding.Choose the header (or each item) of the card to get further information.Note Extra SAP_BR_AR_MANAGER role is required for your user to navigate from this card. | The overview page navigates you to the target apps. The global filter and header (and each item) information is carried over.The card navigates to the Days Sales Outstanding SAP Fiori app. |  |

### Balance Validation

#### Schedule Balance Validation Jobs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule a balance validation job.

Prerequisites

You must ensure that you defined rule groups using Manage Balance Validation Rules and Groups (F6386) as described in [Define Balance Validation Rules and Groups - Upload Rules](#unique_43) [page ] 46.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Schedule Balance Validation Jobs - Accounting (F7470). | The Application Jobs view is displayed. |  |
| 3 | Create Job | Choose Create. | The New Job: Balance Validation for G/L Accounting view is displayed. |  |
| 4 | Template Selection | Make the following entries and choose Step 2:Job Template: Balance Validation for G/L AccountingJob Name: Balance Validation for G/L Accounting |  |  |
| 5 | Scheduling Options | Make the following entries and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Parameters | Make the following entries and choose Schedule:Rule Group: <rule group>Ledger: <ledger>Currency: <currency code>Fiscal Year: <fiscal year>Fiscal Period: <fiscal period>Note In the Entity Selection area, you can select the relevant radio button to run the rules by Company Code, Profit Center, or Cost Center. | The balance validation job is scheduled. |  |

#### View Balance Validation Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you view the results of the balance validation job.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access App | Open View Balance Validation Results (F6387). |  |  |
| 3 | Enter Details | Make the following entries and choose Go:Company Code: 3310Ledger: <ledger you used in prior step>Enter additional fields as needed to filter the results. | The Validation Results pane displays a list of job results. |  |
| 4 | View Details | Click anywhere in the row for one of the job results. | The View Balance Validation Results view is displayed. |  |
| 5 | View Results | Rules that ran successfully are hidden by default. In the Result filter above the Result pane, choose the Success checkbox to view rules that ran successfully. | The Result pane shows the details of the balance validation job. |  |
| 6 | Details | For one of the rows, choose > (Details) at the right of the row. | The right pane opens and displays results for that specific rule. |  |
| 7 | Back | Choose Back. |  |  |

## Appendix

### Display Tax Information Per Country/Region

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity displays the tax information for the selected country/region per each tax code and tax type.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Display Tax Information per Country (S_ALR_87012365). | The Tax information (Country) view is displayed. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Execute:Country ID: AEChart of accounts: YCOADisplay details immediately: Selected | The tax information for the selected country/region is displayed per each tax code. |  |

### User Specific Settings for Alternative Chart of Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity displays the user specific options for journal entries Use Alternative Chart of Account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Edit Options for Journal Entries - My Settings (F2130). | The Edit User-Specific Options for Journal Entries screen displays. |  |
| 3 | Enter Selection Criteria | Select the Use alternative Acct checkbox. |  |  |
| 4 | Choose Close | Choose Close .Note After you make the setting, you can use the Post General Journal Entries (F0718) app to verify the effectiveness. | This change can take several minutes. |  |

### Schedule General Ledger Jobs - Carry Forward Balances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you confirm that Balance Carry Forward has been run for the current fiscal year.

Balance Carry Forward is an automated process (executed automatically by the system on a predefined schedule) without any customer interaction, performed at year end. However, if you want to perform the balance carry forward earlier than the automated process, you can use this application job.

Prerequisites

Before executing this step, check that the Confirm Takeover Date Information step in the Asset Accounting (J62) test script is completed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Schedule General Ledger Jobs (F1927). | The Application Jobs view is displayed. |  |
| 3 | Create | Choose Create. |  |  |
| 4 | Enter Details | Make the following entries and choose Step 2:Job Template: Balance CarryforwardJob Name: Balance Carryforward |  |  |
| 5 | Enter Details | Make the following entries and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Details | Make the following entries and choose Schedule:Ledger: <ledger>, for example, 0LCompany Code: 3310Carry Forward to Fiscal Year: <fiscal year>Test Run: Selected | You scheduled the job run as a test run. |  |
| 7 | Review Results | To review the results of your test run, find your run in the Jobs pane and choose the arrow button to the right of its row. |  |  |
| 8 | Run Details | Choose the Run Details tab. Review the log status. |  |  |
| 9 | Productive Run | To perform a productive run, repeat this process, but deselect Test Run. | You scheduled the job run as a productive run. |  |

### Review Verify General Journal Entries (Optional)

Purpose

In this activity, you set up and execute the workflow to review the verify general journal entries process.

|  |
| --- |
| Note Before you execute the process, you must set up the workflows and teams. |

Prerequisite – Manage Workflows

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Manage Workflows for Journal Entry Verification - In General Ledger (F2720). |  |  |
| 3 | Copy Existing Workflow | Select the General Journal Entry Verification workflow radio button and choose Copy. | The Copy Workflow view is displayed. |  |
| 4 | Name Copied Workflow | Change the Workflow Name field as needed (for example Review General Journal Entry Verification). |  |  |
| 5 | Enter Details | Make the following entries:Description: Review General Journal Entries - CoCd xx10 Amount >=100 Acct Group= FINStart Conditions tab:Company Code: 3310Threshold Amount in Company Code Currency: <threshold amounts>, for example, 100Account Group: FINJournal Entry Type: SA |  |  |
| 6 | Add Reviewer Step | In the Steps pane, in the Review Steps area, choose Create. | The New Step view is displayed. |  |
| 7 | Add Reviewer Step | Make the following entries and choose Create:Step Name: <step name>Step Type: Review General Journal EntryRole: <reviewer's role> |  |  |
| 8 | Save | Choose Save. |  |  |
| 9 | Activate | Choose Activate. |  |  |

Prerequisite – Manage Teams

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Manage Teams and Responsibilities For Journal Entry Verification - In General Ledger (F3932). |  |  |
| 3 | Create Team | Choose Create. |  |  |
| 4 | Enter Team Details | Make the following entries:Team Information tab:Name: <name>, for example, General Journal Entry Verify ReviewerGlobal ID: <global identifier>Type: FGLVG (FI general journal entry verification)Status: Enabled |  |  |
| 5 | Enter Team Details | Choose the Team Members tab. |  |  |
| 6 | Enter Team Details | Choose Create (located above the Team Members area). | The Select: Business User dialog box is displayed. |  |
| 7 | Enter Team Details | Make the following entries and choose OK:Business Partner: For example, the local gl_accountant userFunctions: <function for reviewing the verify general journal entries> |  |  |
| 8 | Create Team | At the bottom of the view, choose Create. | The responsibility for the reviewer is defined. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the user from the Business Partner field in the Manage Teams prerequisite above. |  |  |
| 2 | Access App | Open Verify Journal Entries in General Ledger - For Processor (Inbox) (F2728). | The My Inbox view is displayed. |  |
| 3 | Review | In the left pane, select an inbox item to review. | The item displays in the right pane. |  |
| 4 | Review | Review the verify general journal entry item. When you are done, exit the app. |  |  |

### Manage Finance Notifications

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can monitor the status of the finance notification from In-House Banking. You can view journal entries in the detail page of a finance notification and navigate to the original document in the sender components.

Prerequisites

You enabled the In-House Banking (6BP) scope item in your system and performed the relevant steps based on your needs.

Before testing, ensure that you process the following steps:

1. Create a correction for an In-House Bank Account by following the steps mentioned in the In-House Banking (6BP) test script: End Of Day Process - Create Correction (Optional).
2. Run the application job with job template In-House Bank - G/L Transfer by following the steps mentioned in the In-House Banking (6BP) test script: End Of Day Process - Manage In-House Bank Application Jobs.
3. Run the Manage In-House Bank Account Balances app and make a note of the Finance Notification Number of the Correction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Finance Notifications (F8825). |  |  |
| 3 | Maintain Filter | Make the following entries and choose Go:Reference Document Display ID: <finance notification number; see prerequisites above> | The list is filtered. |  |
| 4 | Details | Select the filtered notification and choose > (Details). | The status should be Successful. The view displays details including bank account information, transaction details, currency information, and so on. |  |
| 5 | Journal Entry Information | Under Process Information, choose > (Details) to check the journal entry information. |  |  |
| 6 | More Links | Select the journal entry ID, then choose More Links to access other apps, such as Display Journal Entries - New Version. |  |  |

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
- related-to :: [[03-financial-accounting-and-close/test-script-sap-s-4hana-cloud-public-edition-accounting-and-financial-part-01]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J58_S4CLD2608_BPD_EN_AE.docx` — lines 3739–5034 of the extracted text · extracted with `mammoth` · 345,315 chars in the whole document
