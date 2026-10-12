---
id: 05-treasury-and-cash-management/bond-management-3wy-ae-test-script-sap-s-4hana-cloud-public-edition-26-part-02
title: Bond Management (3WY_AE) Test Script - SAP S/4HANA Cloud Public Edition 2608 (3WY_S4CLD2608_BPD_EN_AE) — part 2 of 2
description: "SAP Best Practices 2608 (AE) TRM test script, second part: bond payment, period-end, repayment, reports, and appendix job scheduling, output management, market risk and credit risk steps."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/bond-management]
aliases: []
keywords: [Bond Management, payment requests, automatic payment run, post to general ledger, key date valuation, coupon interest, valuation class transfer, bond sale, bond repayment, treasury reports]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3WY_S4CLD2608_BPD_EN_AE.docx#lines-2912-4949"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-981
topic: 05-treasury-and-cash-management/bond-management
language: EN
part: 2/2
created: 2026-10-12
updated: 2026-10-12
---

# Bond Management (3WY_AE) Test Script - SAP S/4HANA Cloud Public Edition 2608 (3WY_S4CLD2608_BPD_EN_AE) — part 2 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3WY_S4CLD2608_BPD_EN_AE.docx`, part 2 of 2 (lines 2912–4949 of the extracted text), extracted with `mammoth`. Grouped under **Bond Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows view, enter the following data, and choose Run:Securities: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Send for Approval: <select this indicator>Test Run: <select>Note If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows view, enter the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by choosing Display payment log. |  |

##### Option 2: Generate and Process Payment Request

###### Generate Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Each financial transaction contains flows that need to be paid. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment in practice). Treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows which require payment requests. It will not create posting in financial accounting.

In the case that the payment is initiated by the financial partner, skip the current step and the next step [Process Payment Request](#unique_71) [page ] 149, and continue with the step [Post to General Ledger](#unique_73) [page ] 152.

|  |
| --- |
| Note You can also schedule a background job for this step. Please see the corresponding step in the Appendix section. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Securities: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>On the Payment Control area:Schedule Auto Payment Run: <deselect this indicator>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>Test Run: <select>Pay Only: <select this indicator>Note If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. | Screen Payment Log - Test Run displays, you can check the payment information on this screen. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Payment Log displays, payment request has been generated, make a note of the key number displayed on this screen. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows view, enter the following data, and choose Run:Securities: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>On the Payment Control area:Schedule Auto Payment Run: <deselect this indicator>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>Test Run: <select>Note If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. | The Payment Log - Test Run view displays. Review the payment information on this view. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows screen, enter the following data, and choose Run:Test Run: <deselect> | The Payment Log view displays. A payment request is generated.Make a note of the key number: __________ |  |

###### Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the Automatic Payment Transactions for Payment Requests (F111) app to start the Payment Program for Payment Requests. The payment program for payment requests is an additional automatic payment option in the SAP system. Unlike the standard payment program, the payments are not based on open items (vendor/customer items), but on payment requests.

Prerequisite

Payment request has been generated in the previous procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests screen is displayed. |  |
| 3 | Enter Run Date and Identification | On the Automatic Payment Transactions for Payment Requests screen, enter the following data and choose Parameters:Run Date: for example, <current date>Identification: for example, TRM01 | The Automatic Payment Transactions: Parameters view displays. |  |
| 4 | Enter Parameters | Enter the following data:Posting Date: for example, <current date>Next payment run on: for example, <current date + 3 days>Company Code: for example, 3310Payment Methods: for example, TFChoose Dynamic selections, on the dialog box Free Selection for payment run, enter the following data and choose Save:Key number: <the key number you noted down in previous step>Choose Additional Log, on the dialog box Additional Log, enter the following data and choose Continue:Payment method selection in all cases: <select this indicator>Line items of the payment documents: <select>Due date check: <select>If information Log created for all accounts displays, choose Continue.Choose Save on view Automatic Payment Transactions: Parameters. | The system displays the message Parameters have been entered . |  |
| 5 | Schedule Proposal | Choose Proposal.On the dialog box Schedule Proposal, choose Start Immediat, and choose Schedule Job to confirm this dialog box.Message Proposal is running displays in the status bar with yellow traffic light.Choose Status, until message Payment proposal has been created appears in the status bar with green traffic light. | Payment proposal has been generated. |  |
| 6 | Schedule Payment | Choose Pmnt run.On the dialog box Schedule Payment, choose Start Immediat., and choose Create Payment Medium, then choose Schedule Job to confirm the dialog box.Message Payment run is running displays in the status bar with yellow traffic light.Choose Status, until message Payment run has been carried out appears with green traffic light. | The payment document has been created.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, choose Payments to check the payment log.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media, then a BCM batch is supposed to be created after payment run, please see next test step. |  |
| 7 | Cross-Payment Run Payment Media (Create BCM Batch) | On the Automatic Payment Transactions for Payment Requests view, choose Menu > Environment > Payment medium > Cross-Payment Run Payment Medium > Create Payment Medium .On the Creation of Cross-Payment Run Payment Media view, enter the following data and choose Run:Run Date: for example, <current date>Identification: for example TRM01R | Dialog box Creation of Cross-Payment Run Payment Media appears, and states that Collector XX/XX/20XX XXXXXX was created or updated, that means, the BCM batch has been created.A batch may need additional approvals before payment medium is finally created. For details refer to test script Advanced Cash Operations(J78). |  |

##### Send Payment Medium File

Purpose

In this activity, you send the payment medium file to your house bank to facilitate the payment.

Procedure

If Bank Communication Management (BCM) is not implemented in your system, the payment medium file will be generated upon completion of the payment run in the previous step, provided that the relevant payment method uses the PMW format.

If BCM is implemented in your system, additional approvals may be required for a BCM batch before the payment medium file can be generated. For the approval process, please refer to the section Outgoing Payment with BCM Approval Process in the test script Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/J78)).

After payment medium file is created, there are two ways for sending the payment medium file to your house bank:

- If Multi-Bank Connectivity (MBC) is not enabled, please use app Manage Payment Media (F1868) to check and download the payment medium file, and send the file to the bank via the previously agreed-upon method. Further details are provided in test script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/1EG)).
- If MBC is enabled and the relevant PMW format uses the alternative format type designated for MBC, then the payment medium file can be automatically sent to MBC. Bank will then retrieve the payment medium file from MBC and execute the payment. Further details are provided in test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/16R)).

#### Bank Initiated Payment

Purpose

If the outgoing payment is initiated by bank, it is not necessary to run previous steps Generate Payment Request and Process Payment Request, because the outgoing payment is initiated by bank.

Procedure

This step doesn‘t require any operation in system.

#### Post to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. There are two apps are available for posting flows:

- Fix, Pay and Post Flows (TBB1): you use this app to generate the posting for incoming payment. Please note that when using this app in current step, it will not create posting for outgoing payment which has been processed in previous step Generate Payment Request with the Pay Only option.
- Process Business Transactions (TPM10): You use this app to generate the posting for outgoing payment which has been processed in previous step Generate Payment Request with the Pay Only option.

|  |
| --- |
| Note You can also schedule background job for this step, please see corresponding step in Appendix. |

Prerequisite

The outgoing payment which should be handled via payment request (if there is) for this transaction has been processed in previous step Generate Payment Request with the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Execute:Securities: <select this checkbox>Company Code: for example 3310Transaction: <The transaction number you created in previous step>Sec. Class ID Number: <The Sec. Class ID Number you entered in previous step,for example, BD_ AE 3 or BD_ AE 4 or BD_ AE 5 or BD_ AE 04>Up to and Including Due Date: enter date on which the flow of financial transaction should be posted, for example, <current date>Test Run: <select this checkbox>Post Operational Only: <select this indicator> | Screen Posting Log: Posted Business Transactions is displayed. You can check the simulated posting information for local GAAP (valuation area AE0) on this screen. Please note there is no posting created because it is test run.If message No flows exist for processing is displayed, that means there is no posting needed for your selection criteria, you can skip the current test step and continue the test step with the Process Business Transactionsapp. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Execute:: <unselect this checkbox>Test Run | Screen Posting Log: Posted Business Transactions is displayed, and the accounting document has been created for incoming payment in local GAAP (valuation area AE0). |  |
| 5 | Access another SAP Fiori app | Open Process Business Transactions (TPM10). | The Process Business Transactions screen is displayed. |  |
| 6 | Enter Selection Criteria for Test Run | On the Process Business Transactions screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC Transactions: <unselect this checkbox>Company code: for example, 3310Valuation Area: for example AE0Limit by Subledger Pos.: <select this checkbox>ID Number: <the Security ID you created in previous step>Test Run: <select this checkbox>Test Run: <select this checkbox> | The Test Run: Post/Reverse Business Transactions screen is displayed.If message You have not selected any business transactions is displayed, that means there is no posting needed for your selection criteria, you can skip current step. |  |
| 7 | Check Test Run Result | On the screen Test Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.Screen Test Run: Display Posted/Reversed Business Transactions displays, choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, you can check the simulated posting information for local GAAP (valuation area AE0) on this screen. Please note there is no posting created because it is test run. |  |
| 8 | Enter Selection Criteria for Production Run | Choose Back.On the Process Business Transactions screen, change the following data and choose Execute:Test Run: <unselect this checkbox> | The Update Run: Post/Reverse Business Transactions screen is displayed. |  |
| 9 | Production Run | On the screen Update Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.Screen Update Run: Display Posted/Reversed Business Transactions displays, choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, and the accounting document has been created for outgoing payment in local GAAP (valuation area AE0). |  |

#### Period-end Closing

This section describes activities for period-end closing (usually executed at month end), including:

- [Import Securities Price](#unique_74) [page ] 155
- [Perform Key Date Valuation](#unique_75) [page ] 155

##### Import Securities Price

Purpose

By entering the latest price of a bond into SAP system as securities price, the system can recognize its latest position value and perform the relevant journal posting when running key date valuation.

Procedure

Refer to the Update Securities Price section of the Market Rates Management – Manually via Upload(1XN) for detailed procedures.

##### Import Reference Interest Rate

Purpose

In this step, you adjust the interest rate for the reference interest rate.

Prerequisite

Reference interest rate has been maintained on the fixing date.

Procedure

Follow instructions in the Enter Interest Rates step of the Market Rates Management – Manually via Upload(1XN) test script.

|  |
| --- |
| Note The example data in 1XN might not contain the necessary interest rates for your test. If you are using SOFR / ESTER / SONIA / SARON / TONAR / CORRA / SORA / HONIA, please make sure that you've entered interest from 1st day to end date of current month when you are doing test for this test script. |

##### Perform Key Date Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the valuation function to value the positions of securities based on amortized cost or security price imported via Update Securities Price section of the Market Rates Management – Manually via Upload(1XN), as well as to reflect latest foreign currency exchange rate for the investments other than the company reporting currency.

You can also use configuration step Assign Update Types for Accrual/Deferral to define your own accrual/deferral postings, such as aggregated accrual/deferral flow or not. In the case of a compound interest calculation, a grouping term has to be defined.

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

|  |
| --- |
| Note You can also schedule background job for this step. Please see corresponding step in the Appendix section. |

Prerequisite

You have entered latest security price for the security ID in section [Import Securities Price](#unique_74) [page ] 155.

You have performed following sections of this test script for bond 04A:

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Run Valuation (TPM1). | The Run Valuation screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Run Valuation screen, enter the following data and choose Execute:In the Product Groups area,Securities: <select this checkbox>In the General Selections area,OTC Transactions: <deselect this checkbox>Company Code: for example, 3310Valuation Area: for example, AE0Product Type: for example, 04ASec. Class ID Number: for example, <Security Class ID Number(s) created in previous steps>Security Account: for example, BOND_INVSTIn the Valuation Parameters area,Key Date for Valuation: for example, <last date of current month>Valuation Category: for example, Mid-year Valuation with ResetWhen the Period End is also the Year End, the Valuation Category Year End Valuation should be used.Test Run: <select this checkbox>Amortization Log: <select this checkbox> | The Display Selected Treasury Positions for Valuation screen is displayed. |  |
| 4 | Execute Valuation for Test Run | On the Display Selected Treasury Positions for Valuation screen, choose Run Valuation.If dialog Message shows up, choose Continue. | The screen Valuation Log is displayed. If red traffic light exists, click on it and check the error message. Solve the issue and perform test run again until there is no error.You can check the simulated posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. Please note there is no posting created because it is test run.Note Sometime there is no simulated posting because your selected security class position in security account may not need valuation. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until the Run Valuation screen is displayed.On the initial screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The Display Selected Treasury Positions for Valuation screen is displayed. |  |
| 6 | Execute Valuation for Production Run | On the Display Selected Treasury Positions for Valuation screen, choose Run Valuation. | The Valuation Log screen is displayed, you can check the posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. Then, the accounting document has been created in local GAAP (valuation area AE0). |  |

#### Interest Rate/Index Value Fixing Date

Purpose

This section describes activities for Interest Rate Adjustment and includes the following steps:

- [Import Reference Interest Rate](#unique_76) [page ] 158
- [Import Price Index Values](#unique_140) [page ] 158
- [Update Planned Records for Securities](#unique_77) [page ] 159

##### Import Reference Interest Rate

Purpose

In this step, you adjust the interest rate for the reference interest rate.

Prerequisite

Reference interest rate has been maintained on the fixing date.

Procedure

Follow instructions in the Enter Interest Rates step of the Market Rates Management – Manually via Upload(1XN) test script.

|  |
| --- |
| Note The example data in 1XN might not contain the necessary interest rates for your test. If you are using SOFR / ESTER / SONIA / SARON / TONAR / CORRA / SORA / HONIA, please make sure that you've entered interest from 1st day to end date of current month when you are doing test for this test script. |

##### Import Price Index Values

Purpose

In this step, you adjust the interest rate for the reference interest rate.

Prerequisite

Reference interest rate has been maintained on the fixing date.

Procedure

Follow instructions in the Enter Price Index Values step of the Market Rates Management – Manually via Upload(1XN) test script.

##### Update Planned Records for Securities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step provides instructions on how to update planned records for securities.

Prerequisite

The dividend factors are already entered.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Update Planned Records for Securities (FWUP). | The Update Planned Records for Securitiesscreen is displayed. |  |
| 3 | Enter Selection Criteria | On the Update Planned Records for Securities screen, enter the following data and choose Execute:Company Code: for example, 3310Security ID: for example, <Security Class ID Number(s) created in previous steps> | Update was completed successfully. |  |

#### Coupon Date

Purpose

The following steps in this section describes activities for interest payable of issued bond:

- [Recognize Interest Receivable](#unique_78) [page ] 160
- [Post Incoming Interest Payment](#unique_79) [page ] 162

##### Recognize Interest Receivable

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can process interest receivable.

|  |
| --- |
| Note You can also schedule a background job for Automatic Debit Position. For more information, see the corresponding step in the Appendix. |

Procedure

Table 4: Option 1

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Execute Debit Position - Manual Debit Position (FWZE). | The Manual Debit Position: Initial screen is displayed. |  |
| 3 | Enter Parameters | On the Manual Debit Position: Initial Screen, enter the following data and choose Enter:Company Code: for example, 3310Security ID: for example, <Security Class ID Number(s) created in previous steps>Security Account: for example, BOND_INVST | A list of positions is displayed. |  |
| 4 | Select a Flow and Proceed | On the list of positions that displayed on the Manual Debit Position: Initial Screen, select the top flow with update type SAM5000 and choose Post business transaction. | Manual Debit Position screen is displayed. |  |
| 5 | Enter Details for the Interest Payment | On the Manual Debit Position screen, double click on the record should be received:The Incoming Payments:Process Flow dialog box is displayed.Verify below data and choose Copy:Payment Amount: for example, <the total amount of the interest to be received>. | flow has been processed in the Flows tab. |  |
| 6 | Post | Confirm the data and choose Post. | Screen with Posting Log displays. The interest receivable has been generated. |  |

Table 5: Option 2

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Automatic Debit Position and Posting - Security Accounts (FWSO) | The Securities: Automatic Debit Position screen is displayed. |  |
| 3 | Enter Parameters and Test Run | On the Securities: Automatic Debit Position Screen, enter the following data and choose Execute:Company Code: for example, 3310Product Type: for example, 04ASecurity ID: for example, <Security Class ID Number(s) created in previous steps>Security Account: for example, BOND_INVSTUpdate Type: for example, SAM5000Up to an Including Pos. Date: for example, <end date of current month>Document Date: for example, <end date of current month>Up to an Including Pos. Date: for example, end of term you entered in step Create Security ClassDocument Date: for example, end of term you entered in step Create Security ClassTest Run: for example, <select> | A list of messages indicating the flow were fixed. |  |
| 4 | Production Run | Confirm the messages and go back to previous screen, enter the following data and choose ExecuteTest Run: for example, <deselect> | A list of messages indicating the flow were fixed. |  |

##### Post Incoming Interest Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can post incoming interest payment.

|  |
| --- |
| Note You can also schedule a background job for Automatic Debit Position. For more information, see the corresponding step in the Appendix |

Procedure

Option 1

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Execute Debit Position - Manual Debit Position (FWZE). | The Manual Debit Position: Initial screen is displayed. |  |
| 3 | Enter Parameters | On the Manual Debit Position: Initial Screen, enter the following data and choose Enter:Company Code: for example, 3310Security ID: for example, <Security Class ID Number(s) created in previous steps>Security Account: for example, BOND_INVST | A list of positions is displayed. |  |
| 4 | Select a Flow and Proceed | On the list of positions that displayed on the Manual Debit Position: Initial Screen, select the top flow with update type SAM6000 and choose Post business transaction. | Manual Debit Position screen is displayed. |  |
| 5 | Enter Details for the Interest Payment | On the Manual Debit Position screen, double click on the record should be received:The Incoming Payments:Process Flow popup window is displayed.Verify below data and choose Copy:Payment Amount: for example, the total amount of the interest to be received. | flow has been processed in the Flows tab. |  |
| 6 | Post | Confirm the data and choose Post. | Screen with Posting Log is displayed. The incoming interest payment has been generated.Note Make a note of the key number displayed on this screen. |  |

Table 6: Option 2

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Automatic Debit Position and Posting - Security Accounts (FWSO) | The Securities: Automatic Debit Position screen is displayed. |  |
| 3 | Enter Parameters and Test Run | On the Securities: Automatic Debit Position Screen, enter the following data and choose Execute:Company Code: for example, 3310Product Type: for example, 04ASecurity ID: for example, <Security Class ID Number(s) created in previous steps>Security Account: for example, BOND_INVSTUpdate Type: for example, SAM6000Up to an Including Pos. Date: for example, <end date of current month>Document Date: for example, <end date of current month>Up to an Including Pos. Date: for example, end of term you entered in step Create Security ClassDocument Date: for example, end of term you entered in step Create Security ClassTest Run: for example, <select> | A list of messages indicating the flow were fixed. |  |
| 4 | Production Run | Confirm the messages and go back to previous screen, enter the following data and choose ExecuteTest Run: for example, <deselect> | A list of messages indicating the flow were fixed. |  |

|  |
| --- |
| Note You can use the transaction Post General Journal Entries (F0718) as described in General Ledger Accounting (058) script to move the bond proceeds to Other Financiang Soures. Use the ledger group specific posting to post this for modified accrual ledger only. |

#### Reclassification

##### Perform Valuation Class Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, valuation class transfer are executed from long term to short term and reflected in financial accounting.

Prerequisite

The maturity date of transactions is within one year and the position values are not zero.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Execute Valuation Class Transfer (TPM15M). | The Valuation Class Transfer view displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Valuation Class Transfer view, enter the following data:Securities: <select this checkbox>Company Code: for example, 3310Security ID: for example, <Security Class ID Number(s) created in previous steps>Security Account: for example, BOND_INVSTGeneral Valuation Class (in subarea Specific Selection for Outgoing Position): <select this indicator>Key Date: for example <last date of current month>Test Run: <select this checkbox>and choose Execute. | The Edit Selected Positions view displays. |  |
| 4 | Execute Test Run and Check Result | On the Edit Selected Positions view, select the transactions you want to transfer and enter the new General Valuation Class in field New Valuation Class.Rule of new General Valuation Class:switch the first digit of original General Valuation Class from 1 (long term) to 2 (short term) to change to the new General Valuation Class. For example, if the original General Valuation Class is 12, then the new General Valuation Class is 22.Choose Execute. | The Test Run: Transfer view displays, |  |
| 5 | Review Logs | Choose Messages and Log.On Information Overview dialog box, choose Posting Log.On Posting Log: Posted Business Transactions view, you review the simulated postings. | Logs are reviewed. |  |
| 6 | Production Run | Go back to the initial view of this app. Deselect the Test Run checkbox and repeat the previous steps for production run. | Production run successful, postings are created. |  |

#### Sell Bond before Maturity

##### Create Bond Sale Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After sale transaction has concluded in the real world, an entry into the system is required to update the securities position.

Prerequisite

- The Securities position on hand must be greater than or equal to the position to be sold.
- You've run the Enter Interest Rates step of the Market Rates Management – Manually via Upload(1XN) test script.

|  |
| --- |
| Note The example data in 1XN might not contain the necessary interest rates for your test. If you are using SOFR / ESTER / SONIA / SARON / TONAR / CORRA / SORA / HONIA, please make sure that you've entered interest from 1st day to end date of current month when you are doing test for this test script. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Securities Transaction (TS01). | The Create Security Transaction: Initial screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Security Transaction: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security ID: for example, <Security Class ID Number(s) created in previous steps>Transaction Type: 200Partner: for example, 33537001 | The Create Security Transaction: Structure screen is displayed. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:Securities Account: for example, BOND_INVSTGeneral Valuation Class: click on Display Quantity Position to figure out the GVC should be used < for example, use the same General Valuation Class as purchase transaction for this security class ID>Note If you have performed Valuation Class Transfer step, use the new GVC transferred.Position Value Date: for example, <the first day of next month>Calculation Date: for example, <The second day of next month>Payment Date: for example, <the first day of next month>Incl.: for example, <deselected>Nominal Amount: for example, 100,000,000.00 AEDPrice (%): 100Coupon : 1 Next coupon will be delivered(plus accrued interest)Please switch to the Other flows tab | The Create Security Transaction: Other Flows screen is displayed.Note Make sure that there is no condition-based business transactions posted after position value date. |  |
| 5 | Enter Data on Other flows | On the tab Other flows, add a flow row by entering the following data:Flow type: 0315 Charge not capitalizedPayment Amount: 500.00Payment Currency: AED | All data are entered. |  |
| 6 | Save the Transaction | Choose Save. | The data is saved |  |

##### Set Settlement Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once a securities transaction is recorded and saved in SAP, the transaction must be settled before you perform further activities. This section describes how to set the settlement status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria and Execute | Enter the following data and choose Go:Key Date: <the current date>Company Code: for example, 3310Transaction: <transaction you created in the previous step> | The transaction is displayed. |  |
| 4 | Settle the TRM Transaction | On the Manage Financial Transactions screen, select the checkbox at the head of the transaction line and choose Settle. | You are directed to the screen for settling the transaction.Note The view title will be different according to product type of transaction. |  |
| 5 | Save the Change | On the Settle Security Contract: Structure screen, the value of field Activity in header is 2 - Contract Settlement.Choose Save.If dialog Document lines: Display messages displays, choose Continue (Enter). | The transaction is saved with status Contract Settlement. |  |

##### Corporate Initiated Payment

Purpose

This section describes how to handle the payment for securities purchase transaction which are initiated by corporate via payment requests.

There are two options to process the payment for the purchase:

1. Process the payment with the ‘Auto. Payment Run’ function.
2. Process the payment without the ‘Auto. Payment Run’ function.

Prerequisites

You have settled the contract in the previous step.

###### Option 1: Generate and automatically process payment request

###### Process the Payment with the ‘Auto. Payment Run’ Function

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Each financial transaction contains flows that need to be paid. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment in practice). Treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows.

Within these two apps, if you select the ‘Schedule Auto Payment Run’ option, system will automatically process the automatic payment run for payment requests.

|  |
| --- |
| Note You can also schedule a background job for this step. Please see the corresponding step in the Appendix section. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Securities: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Send for Approval: <select this indicator>Pay Only: <select this indicator>Test Run: <select>Note If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows view, enter the following data, and choose Run:Securities: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Send for Approval: <select this indicator>Test Run: <select>Note If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows view, enter the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by choosing Display payment log. |  |

###### Option 2: Generate and Process Payment Request

###### Generate Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Each financial transaction contains flows that need to be paid. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment in practice). Treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows which require payment requests. It will not create posting in financial accounting.

In the case that the payment is initiated by the financial partner, skip the current step and the next step [Process Payment Request](#unique_71) [page ] 149, and continue with the step [Post to General Ledger](#unique_73) [page ] 152.

|  |
| --- |
| Note You can also schedule a background job for this step. Please see the corresponding step in the Appendix section. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Securities: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>On the Payment Control area:Schedule Auto Payment Run: <deselect this indicator>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>Test Run: <select>Pay Only: <select this indicator>Note If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. | Screen Payment Log - Test Run displays, you can check the payment information on this screen. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Payment Log displays, payment request has been generated, make a note of the key number displayed on this screen. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows view, enter the following data, and choose Run:Securities: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>On the Payment Control area:Schedule Auto Payment Run: <deselect this indicator>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>Test Run: <select>Note If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. | The Payment Log - Test Run view displays. Review the payment information on this view. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows screen, enter the following data, and choose Run:Test Run: <deselect> | The Payment Log view displays. A payment request is generated.Make a note of the key number: __________ |  |

###### Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the Automatic Payment Transactions for Payment Requests (F111) app to start the Payment Program for Payment Requests. The payment program for payment requests is an additional automatic payment option in the SAP system. Unlike the standard payment program, the payments are not based on open items (vendor/customer items), but on payment requests.

Prerequisite

Payment request has been generated in the previous procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests screen is displayed. |  |
| 3 | Enter Run Date and Identification | Enter the following data and choose Parameters:Run Date: for example, <current date>Identification: for example, TRM01 | The Automatic Payment Transactions: Parameters screen is displayed. |  |
| 4 | Enter Parameters | On the Automatic Payment Transactions: Parameters screen, enter the following data:Posting Date: for example, <current date>Next payment run on: for example, <current date + 3 days>Company Code: for example, 3310Payment Methods: for example, TFChoose Dynamic selections, on the dialog box Free Selection for payment run, enter the following data and choose Save:Key Number: <the key numbers you noted down in previous step>Choose Additional Log, on the dialog box Additional Log, enter the following data and choose Continue:Payment method selection in all cases: <select this indicator>Line items of the payment documents: <select>Due date check: <select>If information Log created for all accounts displays, choose Continue.Choose Save on screen Automatic Payment Transactions: Parameters. | Message Parameters have been entered displays on the Automatic Payment Transactions for Payment Requests screen. |  |
| 5 | Schedule Proposal | Choose Proposal.On the dialog box Schedule Proposal, choose Start Immediat., and choose Schedule Job to confirm this dialog box.Message Proposal is running displays in the status bar with yellow traffic light.Choose Status, until message Payment proposal has been created appears in the status bar with green traffic light. | Payment proposal has been generated. |  |
| 6 | Schedule Payment | Choose Pmnt run.On the dialog box Schedule Payment, choose Start Immediat., and choose Create Payment Medium, then choose Schedule Job to confirm the dialog box.Message Payment run is running displays in the status bar with yellow traffic light.Choose Status, until message Payment run has been carried out appears with green traffic light. | The payment document has been created.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, choose Payments to check the payment log.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media, then a BCM batch is supposed to be created after payment run, please see next test step. |  |
| 7 | Cross-Payment Run Payment Media (Create BCM Batch) | On the Automatic Payment Transactions for Payment Requests screen, choose Menu > Environment > Payment medium > Cross-Payment Run Payment Medium > Create Payment Medium .On the Creation of Cross-Payment Run Payment Media view, enter the following data and choose Run:Run Date: for example, <current date>Identification: for example TRM01R | Dialog box Creation of Cross-Payment Run Payment Media appears, and states that Collector XX/XX/20XX XXXXXX was created or updated, that means, the BCM batch has been created.A batch may need additional approvals before payment medium is finally created. For details refer to test script Advanced Cash Operations(J78). |  |

###### Send Payment Medium File

Purpose

In this activity, you send the payment medium file to your house bank to facilitate the payment.

Procedure

If Bank Communication Management (BCM) is not implemented in your system, the payment medium file will be generated upon completion of the payment run in the previous step, provided that the relevant payment method uses the PMW format.

If BCM is implemented in your system, additional approvals may be required for a BCM batch before the payment medium file can be generated. For the approval process, please refer to the section Outgoing Payment with BCM Approval Process in the test script Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/J78)).

After payment medium file is created, there are two ways for sending the payment medium file to your house bank:

- If Multi-Bank Connectivity (MBC) is not enabled, please use app Manage Payment Media (F1868) to check and download the payment medium file, and send the file to the bank via the previously agreed-upon method. Further details are provided in test script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/1EG)).
- If MBC is enabled and the relevant PMW format uses the alternative format type designated for MBC, then the payment medium file can be automatically sent to MBC. Bank will then retrieve the payment medium file from MBC and execute the payment. Further details are provided in test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/16R)).

##### Bank Initiated Payment

Purpose

If the outgoing payment is initiated by bank, it is not necessary to run the previous steps Generate Payment Request and Process Payment Request, because the outgoing payment is initiated by bank.

Procedure

This step doesn't require any operation in system.

##### Post to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. There are two apps are available for posting flows:

- Fix, Pay and Post Flows (TBB1): you use this app to generate the posting for incoming payment. Please note that when using this app in current step, it will not create posting for outgoing payment which has been processed in previous step Generate Payment Request with the Pay Only option.
- Process Business Transactions (TPM10) You use this app to generate the posting for outgoing payment which has been processed in previous step Generate Payment Request with the Pay Only option.

|  |
| --- |
| Note You can also schedule background job for this step, please see corresponding step in Appendix. |

Prerequisite

The outgoing payment which should be handled via payment request (if there is) for this transaction has been processed in previous step Generate Payment Request with the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Execute:Securities: <select this checkbox>Company code: for example 3310Transaction: <The transaction number you entered in previous step>Sec. Class ID Number: <The Sec. Class ID Number you entered in previous step,for example, BD_ AE 3>Up to and Including Due Date: enter date on which the flow of financial transaction should be posted, for example, <current date>Test Run: <select this checkbox>Post Operational Only: <select this indicator> | Screen Posting Log: Posted Business Transactions is displayed. You can check the simulated posting information for local GAAP (valuation area AE0) on this screen. Please note there is no posting created because it is test run.If message No flows exist for processing is displayed, that means there is no posting needed for your selection criteria, you can skip the current test step and continue the test step with the Process Business Transactionsapp. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Execute:Test Run: <unselect this checkbox> | Screen Posting Log: Posted Business Transactions is displayed, and the accounting document has been created for incoming payment in local GAAP (valuation area AE0). |  |
| 5 | Access another SAP Fiori app | Open Process Business Transactions (TPM10). | The Process Business Transactions screen is displayed. |  |
| 6 | Enter Selection Criteria for Test Run | On the Process Business Transactions screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC Transactions: <unselect this checkbox>Company Code: for example, 3310Valuation Area: for example AE0Limit by Subledger Pos.: <select this checkbox>Transaction: <The Security ID you entered in previous step, for example, BD_AE3Test Run: <select this checkbox> | The Test Run: Post/Reverse Business Transactions screen is displayed.If message You have not selected any business transactions is displayed, that means there is no posting needed for your selection criteria, you can skip current step. |  |
| 7 | Check Test Run Result | On the screen Test Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.Screen Test Run: Display Posted/Reversed Business Transactions displays, choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, you can check the simulated posting information for local GAAP (valuation area AE0) on this screen. Please note there is no posting created because it is test run. |  |
| 8 | Enter Selection Criteria for Production Run | Choose Back.On the Process Business Transactions screen, change the following data and choose Execute:Test Run: <unselect this checkbox> | The Update Run: Post/Reverse Business Transactions screen is displayed. |  |
| 9 | Production Run | On the screen Update Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.Screen Update Run: Display Posted/Reversed Business Transactions displays, choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, and the accounting document has been created for outgoing payment in local GAAP (valuation area AE0). |  |

#### Repayment Date

Purpose

This section describes activities for principal repayment at maturity date of invested bond includes:

- [Recognize Redemption Receivable](#unique_88) [page ] 180
- [Post Incoming Principal Repayment](#unique_89) [page ] 182

##### Recognize Redemption Receivable

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step provides instructions on how to post redemption receivable.

|  |
| --- |
| Note You can also schedule a background job for Automatic Debit Position. For more information, see the corresponding step in the Appendix. |

Prerequisite

You have executed all the steps and performed all the transactions which should be occurred and posted before scheduled repayment date.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Execute Debit Position - Manual Debit Position (FWZE) | The Manual Debit Position: Initial screen is displayed. |  |
| 3 | Enter Parameters | On the Manual Debit Position: Initial Screen, enter the following data and choose Enter:Company Code: for example, 3310Security ID: for example, <Security Class ID Number(s) created in previous steps>Security Account: for example, BOND_INVST | A list of positions is displayed. |  |
| 4 | Select a Flow and Proceed | On the list of positions that displayed on the Manual Debit Position: Initial Screen, select the top flow with update type SAM1104 and choose Post business transaction. | Manual Debit Position screen is displayed. |  |
| 5 | Enter Details for the Interest Payment | On the Manual Debit Position screen, double click on the record should be paid:The Incoming Payments:Process Flow dialog box is displayed.Verify below data and choose Copy:Payment Amount: for example, the total amount of the principal to be repaid. | flow has been processed in the Flows tab. |  |
| 6 | Post | Confirm the data and choose Post. | Screen with Posting Log is displayed. Payment request has been generated.Note Make a note of the key number displayed on this screen. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Automatic Debit Position and Posting - Security Accounts (FWSO) | The Securities: Automatic Debit Position screen is displayed. |  |
| 3 | Enter Parameters and Test Run | On the Securities: Automatic Debit Position Screen, enter the following data and choose Execute:Company Code: for example, 3310Product Type: for example, 04ASecurity ID: for example, <Security Class ID Number(s) created in previous steps>Security Account: for example, BOND_INVSTUpdate Type: for example, SAM1104Up to an Including Pos. Date: for example, end of term you entered in step Create Security ClassDocument Date: for example, end of term you entered in step Create Security ClassTest Run: for example, <select> | A list of messages indicating the flow were fixed. |  |
| 4 | Production Run | Confirm the messages and go back to previous screen, enter the following data and choose ExecuteTest Run: for example, <deselect> | A list of messages indicating the flow were fixed. |  |

##### Post Incoming Principal Repayment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step provides instructions on how to post incoming principal repayment.

|  |
| --- |
| Note You can also schedule a background job for Automatic Debit Position. For more information, see the corresponding step in the Appendix |

Prerequisite

The principal repayment has been processed in previous step [Recognize Redemption Receivable](#unique_88) [page ] 180.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Execute Debit Position - Manual Debit Position (FWZE) | The Manual Debit Position: Initial screen is displayed. |  |
| 3 | Enter Parameters | On the Manual Debit Position: Initial Screen, enter the following data and choose Enter:Company Code: for example, 3310Security ID: for example, <Security Class ID Number(s) created in previous steps>Security Account: for example, BOND_INVST | A list of positions is displayed. |  |
| 4 | Select a Flow and Proceed | On the list of positions that displayed on the Manual Debit Position: Initial Screen, select the top flow with update type SAM6104 and choose Post business transaction: | Manual Debit Position screen is displayed. |  |
| 5 | Enter Details for the Interest Payment | On the Manual Debit Position screen, double click on the record should be paid:The Incoming Payments:Process Flow dialog box is displayed.Verify below data and choose Copy:Payment Amount: for example, the total amount of the principal to be repaid. | flow has been processed in the Flows tab. |  |
| 6 | Post | Confirm the data and choose Post. | Screen with Posting Log and Payment Log displays. Payment request has been generated.Note Make a note of the key number displayed on this screen. |  |

### Reports

#### Define Financial Positions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Define a set of key figures to be displayed in Financial Status - Book Value and Financial Status - Nominal Amount screens.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Risk Manager. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Define Financial Positions (FTR_FP_DEF). | The "Maintain Financial Position Groups": Change screen is displayed. |  |
| 3 | Maintain Key Figure Groups | Select New Entries.Enter data for a record of new entry and select Save.Financial Position Group: for example, FPG_BD_A0001Financial Position Group Description: for example, Bank accounts and Short term investAssets/Liabilities: for example, Assets | The data is saved.Note If FPG_BD_A0001 is already created for the same purpose, you can skip this step and use the existing record. |  |
| 4 | Maintain Key Figures | Switch to Maintain Financial Positions tab.Enter data and choose Save.Financial Position: for example, FP_BD_A1001Financial Position Description: for example, Bank AccountsFinancial Position Group: for example, FPG_BD_A0001Data Source: for example, One Document Balances | The data is saved. |  |
| 5 | Maintain Selections | Choose Back to display all financial postions. Select one financial position and select Maintain Selections.Account Number: for example, 19999000Chart of Accounts: for example, YCOALedger: for example, 0LChoose Back and choose Save. | The data is saved. |  |
| 6 | Enter More Data | Enter more financial positions data as below tables. |  |  |

Below are examples for financial position groups and financial positions. You may create your own financial position gourps and financial positions per your needs.

Table 7: Financial Position Groups

| Financial Position Group | Financial Position Group Description | Assets/Liabilities |
| --- | --- | --- |
| FPG_BD_A0001 | Bank accounts | Assets |
| FPG_BD_A0002 | Bond Investment | Assets |
| FPG_BD_L0001 | Bond Issuance | Liabilities |

|  |
| --- |
| Note You may create your own Financial Position Groups and Financial Positions per your request. |

Table 8: Financial Positions

| Financial Position | Financial Position Description | Financial Position Group | Data Source | Maintain Selection |
| --- | --- | --- | --- | --- |
| FP_BD_A0001 | Bank accounts | FPG_BD_A0001 | One exposure | House bank |
| FP_BD_A0002 | Bond Investment | FPG_BD_A0001 | Treasury position management | Product Type = 04AValuation Class = 10 to 15 and 20 to 25Valuation Area = AE0Posting Status = 2 |
| FP_BD_L0001 | Bond Issuance | FPG_BD_L0001 | Treasury position management | Product Type = 04AValuation Class = 15 to 20 and 25 to 30Valuation Area = AE0Posting Status = 2 |

#### Financial Status (Book Value)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Display financial status on book values.

Prerequisite

Financial positions are already defined.

Refer to [Define Financial Positions](#unique_90) [page ] 183 for more details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Risk Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Financial Status (F2136). | The Financial Status - Book Value screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select Go.Key Date: for example, <Current Date>Display Currency : for example, AEDExchange Rate Type: for example, MCompany Code: for example, 3310 | The data displays per the filter values. |  |

#### Financial Status (Nominal Amount)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the financial status of the nominal amount.

Prerequisite

Financial positions are defined.

Refer to [Define Financial Positions](#unique_90) [page ] 183 for more details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Risk Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Financial Status (FTR_FPM_FINANCIAL_STATUS (FTR_FPM_FS_NOMAMT)). | The Financial Status - Nominal Amount screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Go:Key Date: for example, <Current Date>Display Currency: for example, AEDExchange Rate Type: for example, MCompany Code: for example, 3310 | The data displays per the filter values. |  |

#### Display Treasury Alerts - Posting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the treasury alerts for posting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Alerts - Posting (F4984). | The Display Treasury Alerts - Posting screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Display Treasury Alerts screen, enter following data and choose Go:Issue Message For: PostingCompany Code: for example, 3310 | Alerts data is displayed per the filter values |  |

#### Display Treasury Alerts- Settlement, Release and Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display treasury alerts for various type of transactions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Alerts - Settlement (F4979). | The Display Treasury Alerts - Settlement view displays with Issue Message For: Settlement. |  |
| 3 | Enter Selection Criteria | On the Display Treasury Alerts - Posting screen and enter following data:Issue Message For: SettlementCompany Code: for example, 3310and choose Go. | Alerts data displays per the filter values. |  |
| 4 | Confirm Alerts for Other Transactions | Select other values in the Issue MessageFor field.ReleasePaymentCorrespondenceInterest Rates |  |  |
| 5 | Select Display Treasury Alerts Tiles with Release | Return to the Home view and open Display Treasury Alerts - Release (F4980). | The Display Treasury Alerts - Release view displays, with Issue Message For:Release. |  |
| 6 | Select Display Treasury Alerts Tiles with Payment | Return to the Home view and open Display Treasury Alerts - Payment (F4981). | The Display Treasury Alerts - Payment view displays, with Issue Message For:Payment. |  |
| 7 | Select Display Treasury Alerts Tiles with Interest Rates | Return to the Home view and open Display Treasury Alerts - Interest Rates (F4982). | The Display Treasury Alerts - Interest Rates view displays, with Issue Message For:Interest Rates. |  |

#### Display Treasury Posting Journal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Display posting journals for review.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Posting Journal (F1755). | The Display Treasury Posting Journal screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select Go.Product Group: for example, SecuritiesCompany Code: for example, 3310 | The posting journals display per the filter values. |  |

#### Display Treasury Position Flows

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to display the position flows.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Position Flows (F1754). | The Display Treasury Position Flowsscreen is displayed. |  |
| 3 | Enter Selection Criteria | On the Display Treasury Position Flows screen, enter following data and choose Go:Product Group: for example: SecuritiesCompany code: for example, 3310 | Position Flow data is displays according to the filter values. |  |

#### Display Treasury Position Values

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Display treasury position values.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Position Values (F1867). | The Display Treasury Position Values screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select GoKey Date: for example, Current DateProduct Group: for example, SecuritiesNote You may have to adapt filter to make the Product Group filter available. The Product Group is in the Position Values filter group.Company Code: for example, 3310Valuation Area: for example, AE0 | The position values data displays per the filter values. |  |

#### Treasury Position Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Display treasury position analysis for review.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Treasury Position Analysis. | The Treasury Position Analysis screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select Go.Key Date: for example, Current DateInclude Planned Data: for example, 1Valuation Area: for example, AE0Company Code: for example, 3310Product Type: for example, 04A and 04A | The position analysis data displays per the filter values. |  |

#### Display Securities Account Class Positions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to display securities account class position list.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Securities Account Class Positions (TPM40A). | The Display Securities Account Class Position List screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Display Securities Account Class Position List screen, enter the following data and choose Execute:Company Code: for example, 3310Sec. Class ID Number: for example, <Security class ID number(s) for which has been created>Securities account: for example, <Security account for which has been created>Position Value Date: for example, <Current date> | The position is displayed. |  |

#### Analyze NPV

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to calculate and display NPV result.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Analyze NPV (JBRX). | The NPV Analysis: Display of Single Values screen is displayed. |  |
| 3 | Enter Selection Criteria of Gen. Selection | On the NPV Analysis: Display of Single Values screen, enter the following data:Evaluation Currency: for example, AEDEvaluation Type: for example, Y001Evaluation Date: for example, <current date>Horizon: for example, <end date of current month>Portfolio Hierarchy: for example, 100 |  | The system calculates the net present value as on the horizon date, but selects the transaction data and market data for the evaluation date. |
| 4 | Enter Selection Criteria of Characteristics | Choose the Characteristics tap, enter the following data then choose Execute:Company Code: for example, 3310Product Type: for example, 04A | The NPV Result displays based on Portfolio Hierarchy. |  |

#### Calculate Market Risk Key Figures

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can use this function to calculate online and display the key figures for NPV analysis and sensitivity key figures for a selection of transactions. You can also use the key figures that have been calculated as the basis for defining formula-based key figures, and display them with the NPV and sensitivity key figures.

Prerequisite

Report Layout for key figure should be maintained. See [Defining Report Layout for Calculate Market Risk Key Figures](#unique_145) [page ] 230 in the Appendix of this document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Calculate Market Risk Key Figures (AISGENKF). | The Single Value Analysis for Generic Key Figures screen is displayed. |  |
| 3 | Enter Selection Criteria of Gen. Selection | On the Single Value Analysis for Generic Key Figures screen, enter the following data:Evaluation Currency: for example, AEDEvaluation Type: for example, Y001Evaluation Date: for example, <current date>Horizon: for example, <end date of current month>Report Layout: for example, Y01 or other Report Layout you createdPortfolio Hierarchy: for example, 100 |  | The system calculates the net present value as on the horizon date, but selects the transaction data and market data for the evaluation date. |
| 4 | Enter Selection Criteria | Choose the Characteristics tap, enter the following data then choose Execute:Company Code: for example, 3310Product Type: for example, 04A | The Single Value Analysis for assigned Report Layout is displayed. |  |

## Appendix

### Position Indicator

#### Change Position Indicator

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step describes how to change position indicator.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Position Indicator (TPM57A). | The Display Position Indicator screen is displayed. |  |
| 3 | Enter Parameters | On the Display Position Indicator screen, enter following data then choose Enter:Product Group: for example, SecuritiesCompany Code: for example, 3310ID Number: for example, <Security class ID number(s) you have created>Securities account: for example, <Security account you have created> | The Securities Account Position Indicator and Subledger Position Indicator tabs are displayed.If you would like to make a change, please make following operation at the Parameter screen.Click on More / Position Indicator / Change. |  |

### Job Scheduling

#### Generate Limit Utilizations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you schedule a background job to generate limit utilizations.

Prerequisite

You have imported the market data.

If security exists, the spot price needs to be maintained for the current date. Refer to the Update Securities Price section of the Market Rates Management – Manually via Upload(1XN) for detailed procedures.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Schedule Treasury Middle Office Jobs (F2772). | The Application Jobs screen is displayed. |  |
| 3 | Create A New Job | On the Application Jobs screen, choose Create. | The Template Selection area is displayed. |  |
| 4 | Enter General Information for New Job | On the Template Selection area, enter following data then choose Step 2:Job Template: for example, <End of Day Processing>Job Name: for example, <End of Day Processing> | You've chosen the job template, and are navigated to the Scheduling Options area. The New Job: Calculate Market Risk Key Figures view displays. |  |
| 5 | Enter Scheduling Options for New Job | In the Scheduling Options area, enter the following data then choose Step 3:For Start Immediately case:Start Immediately: <select>For Recurrence case:Start Immediately: <deselect>Choose Define Recurrence Pattern to define the recurrence pattern in the Scheduling Information dialog box.Start: for example, <Current Date/Current Time>Recurrence Pattern: for example, DailyEvery: for example, 1End: for example, after 7 Occurrence(s)On Non-Working Day: Run on next Working DayNote Schedule this job after back office's job for generating payment request by using the same job template. | You've enter the scheduling recurrence pattern, and are navigated to the Parameters area. |  |
| 6 | Enter Parameters | In the Parameters area, enter the following data and choose Schedule:Company Code: 3310Determination Procedure: <select 10 and 20 from the F4 help input> |  |  |
| 7 | Check Result | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The result is displayed in the Job Details screen. |  |

#### Generate Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a background job to generate the payment requests for flows.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Treasury Back Office Jobs (F2771). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | On the Application Jobs view, choose Create. | The Template Selection area is displayed. |  |
| 4 | Enter General Information | In the Template Selection area, enter the following data, and choose Step 2:Job Template: Fix, Pay and Post FlowsJob Name: for example, <Generate Payment Request> | You've chosen the template and are navigated to the Scheduling Options area. |  |
| 5 | Enter Scheduling Options | In the Scheduling Options area, choose Define Recurrence Pattern, and in the Scheduling Information dialog box, enter the following data:Start Immediately: <deselect this checkbox>Job Start: for example, <current date and time default>Time Zone: <select a time zone or use default>Recurrence Pattern: for example, DailyEvery: for example, 1Day(s)End: for example, select After and then enter 7 occurrence(s)On Non-Working Days: for example No RestrictionChoose OK, and choose Step 3.Note If you would rather to start job at once, select Start Immediately checkbox. | You've defined the recurrence pattern and are navigated to the Parameters area. |  |
| 6 | Enter Parameters | In the Parameters area,In the Application sub-area, select one or more proper product groupIn the General Selection sub-area, enter the following data:Company Code: for example, 3310Transaction: <enter transaction numbers if you'd like to limit transactions>Product Type: <enter product types if you'd like to limit product types>Due Date (Dynamic): for example, 0On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.In the Posting Control sub-area,Test Run: <deselect>Pay Only: <select>Note You can also choose the Post All Valuation Areas radio button, if you want to post to all valuation areas |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Review Results | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details view displays. |  |

#### Post Flows to General Ledger

##### Template - Fix, Pay and Post Flows

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you schedule a background job to generate the posting for incoming payment without a payment request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Treasury Accountant Jobs (F2770). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | Choose Create. | The Template Selection area is displayed. |  |
| 4 | Enter General Information for New Job | In the Template Selection area, enter the following data, and choose Step 2:Job Template: Fix, Pay and Post FlowsJob Name: Post Flows | The New Job: Post Flows screen is displayed. |  |
| 5 | Enter Scheduling Options for New Job | In the Scheduling Options area, choose Define Recurrence Pattern, and enter the following data in the Scheduling Information dialog box :Start Immediately:Job Start: for example, <current date and time><deselect this checkbox>Time zone: <<choose a time zone>Recurrence Pattern: for example, DailyEvery: for example, 1 Day(s)End: for example, After7 Occurrence(s):for example, Run on next Working DayChoose OK, and choose Step 3.Note If you would like to start job at once, select the Start Immediately checkbox.Remember Schedule this job after the back office job for generating payment request by using the same job template. |  |  |
| 6 | Enter Parameters for New Job | In the Parameters area, enter the following data:In the Application sub-area, select a proper Application.In the General Selection sub-area, enter the following data:Company Code: for example, 3310Transaction: <enter transaction numbers if you'd like to limit transactions>Product Type: <enter product types if you'd like to limit product types>Due Date (Dynamic): for example, 0In the Posting Control sub-area, make the following selections:Test Run: <deselect this checkbox>Post Operational Only: <Choose this radio button>Note You can also choose Post All Valuation Areas (instead of Post Operational Only) to post flows to all valuation areas. |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Review Results | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details view displays. |  |

##### Template - Process Business Transactions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you schedule a background job to fix and post the outgoing payment, which was processed in the previous Generate Payment Request step with the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Treasury Accountant Jobs (F2770). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | On the Application Jobs view, choose Create. | The Template Selection area is displayed. |  |
| 4 | Enter General Information | In the Template Selection area, enter the following data, and choose Step 2:Job Template: Process Business TransactionsJob Name: for example, Process Business Transactions |  |  |
| 5 | Enter Scheduling Options | In the Scheduling Options area, choose Define Recurrence Pattern, and enter the following data in the Scheduling Information the dialog box:Start Immediately: <deselect this checkbox>Job Start: for example, <current date and time 11:00>Time zone: <choose a time zone>Recurrence Pattern: for example, DailyEvery: for example, 1 Day(s)End: for example, After7 Occurrence(s)On Non-Working Day: for example, Run on next Working DayChoose OK and choose Step 3.Note If you would like to start job at once, select checkbox Start Immediately.Remember Schedule this job after the back office job for generating payment request by using the same job template. |  |  |
| 6 | Enter Parameters for New Job | In the Parameters area, enter the following data:In the Product Groups sub-area, select one or more product groups.Company Code: for example, 3310Valuation Area: for example, AE0, or leave it blank (run for all valuation areas)In the Limit by Transaction Number sub-area, make the following selection:Limit by Transaction Number: <deselect this checkbox>In the Limit by Subledger Positions sub-area, make the following selection:Limit by Subledger Pos.: <select this checkbox>Product Type: <enter product types if you'd like to limit product types>Transaction: <enter transaction numbers if you'd like to limit transactions>In the Limit by Business Transactions sub-area, make the following selection:Trans. to Be Fixed/Posted: <select this checkbox>In the Posting Control sub-area, make the following selection:Test Run: <deselect this checkbox> |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Review Results | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details screen is displayed. |  |

#### Key Date Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you schedule a background job to value the positions of financial instruments, based on historical cost or fair value for a given key date, and transfer results to financial accounting.

Prerequisite

Fair values using Net Present Value (NPV) have been calculated or maintained for financial transactions which are evaluated at fair value (NPV) according to accounting principles.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Treasury Accountant Jobs (F2770). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | Choose Create. | The New Job screen is displayed. |  |
| 4 | Enter General Information | In the Template Selections area, enter the following data, and choose Step 2:Job Template: Run ValuationJob Name: for example, Run Valuation | You've chosen the template and are navigated to the Scheduling Options area. |  |
| 5 | Enter Scheduling Options | In the Scheduling Options area, enter the following data, and choose Step 3:Start Immediately: <unselect this checkbox>Start: for example, <first day of next month for this year and at time 03:00>Note Schedule your run time to be later than the Treasury - Calculate Net Present Value - With CVA and DVA job. | You've defined the scheduling option and are navigated to the Parameters area. |  |
| 6 | Enter Parameters for New Job | In the Parameters area, enter the following data:Company Code: for example 3310Valuation Area: for example, AE0,or leave it blank (run for all valuation areas)In the OTC Transactions sub-area, enter the following data:Transaction: <enter transaction numbers if you'd like to limit transactions>In the Valuation Parameters sub-area, enter the following data:Key Date for Val. (Dynamic): for example, <last date of current month>Valuation Category: for example, select <Mid-year Valuation with Reset>Note When the Period End is also the Year End, the Valuation Category Year End Valuation is used.In the Posting Control sub-area, make the following data:Test Run: <deselect this checkbox> |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Check Result | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details screen is displayed. |  |

#### Update Security Cash Flow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you schedule a background job to update security cash flow on a regular basis.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Schedule Treasury Back Office Jobs (F2771). | The Application Jobs screen is displayed. |  |
| 3 | Create A New Job | On the Application Jobs screen, choose Create. | The Template Selection area is displayed. |  |
| 4 | Choose Job Template | In the Template Selection area, enter following data then choose Step 2:Job Template: for example, Update Securities Account Cash FlowJob Name: for example, Update Securities Account Cash Flow | The Scheduling Options area is displayed |  |
| 5 | Enter Scheduling Options for New Job | In the Scheduling Options area, choose Define Recurrence Pattern, and enter the following data in the Scheduling Information the dialog box:Start Immediately: <deselect this checkbox>Job Start: for example, <current date and time 11:00>Time zone: <choose a time zone>Recurrence Pattern: for example, DailyEvery: for example, 1 Day(s)End: for example, After7 Occurrence(s)On Non-Working Day: for example, Run on next Working DayChoose OK and choose Step 3.Note If you would like to start job at once, select checkbox Start Immediately. | You've defined the recurrence pattern and are navigated to the Parameters area。 |  |
| 6 | Enter Parameters | In the Parameters area, enter the following data:Company Code: for example, 3310Product Type: for example, 04A |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Check Result | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details screen is displayed. |  |

#### Post Debit Position

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you schedule a background job to post Debit Position.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Schedule Treasury Accountant Jobs (F2770). | The Application Jobs screen is displayed. |  |
| 3 | Create A New Job | On the Application Jobs screen, choose Create. | The Template Selection area is displayed. |  |
| 4 | Choose Job Template | On the Template Selection area, enter following data and then choose Step 2:Job Template: for example, Post Debit PositionJob Name: for example, Post Debit Position | The Scheduling Options area is displayed |  |
| 5 | Enter Scheduling Options for New Job | In the Scheduling Options area, choose Define Recurrence Pattern, and enter the following data in the Scheduling Information the dialog box:Start Immediately: <deselect this checkbox>Job Start: for example, <current date and time 11:00>Time zone: <choose a time zone>Recurrence Pattern: for example, DailyEvery: for example, 1 Day(s)End: for example, After7 Occurrence(s)On Non-Working Day: for example, Run on next Working DayChoose OK and choose Step 3.Note If you would like to start job at once, select checkbox Start Immediately. | The Parameters area is displayed |  |
| 6 | Enter Parameters | In the Parameters area, enter the following data:In the General Selection sub-area,Company Code: for example, 3310Product Type: for example, 04ASecurity Account: for example, <Security class ID number(s) you've created>Sec. Class ID Number: for example, <Security class ID number(s) you've created>Update Type: for example, SAM5000In the Debit Position Parameter sub-area,Up to and Including Pos. Date: for example, <the end date of current month>In the Posting Control sub-area,Document Date: for example, <the end date of current month> |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Check Result | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details screen is displayed. |  |

#### Calculate Market Risk Key Figures

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you schedule a background job to calculate market risk key figures, including the key figure Value at Risk. The result of calculation is persisted in the database for analysis with the SAP Analytics Cloud. The calculation risk keys are defined in the market risk key figure set.

This step is different from the Calculate Market Risk Key Figures step in the Reports section, which is a real-time calculation for the risk keys in the defined report layout.

|  |
| --- |
| Note There are three methods to calculate the Value at Risk key figure, the historical simulation, the Monte Carlo simulation and a parametric method (variance-covariance approach).For the historical simulation, the daily market data of past 250 days needs to be maintained.For the Monte Carlo simulation and the variance-covariance approach, the statistical data of volatility or correlation is required. The calculation is based on the historical daily market data. You need to maintain the daily market data of past 113 days. |

Prerequisites

You have maintained the market risk key figure set, as described in the Manage Market Risk Key Figure Sets step in the Appendix section.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Schedule Treasury Middle Office Jobs (F2772). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | On the Application Jobs screen, choose Create. | The New Job screen is displayed. |  |
| 4 | Enter General Information for New Job | In the Template Selection sub-area, enter the following data, and choose Step 2:Job Template: Calculate Market Risk Key FiguresJob Name: for example, Calculate Market Risk Key FiguresNote You can delete the existing market risk key figure values on the specified evaluation date by the Delete Market Risk Key Figures job template. |  |  |
| 5 | Enter Parameters for New Job | In the Scheduling Options area, enter the following data, and choose Step 3:Start Immediately: <select this checkbox> |  |  |
| 6 | Enter Selection Data for New Job | In the General sub-area, enter the following data:Basic Run: <select this checkbox>Adjustment Run: <deselect this checkbox>Note The adjustment run processes new financial objects and financial objects for which errors have occurred in the base run.In the Evaluation Parameters sub-area, enter the following data:Market Risk Key Figure Set: for example, <MRK01, and MRK02, the key figure set you maintained>Evaluation Date (Dynamic): for example, <the current date, or enter the evaluation date>Volas + Correlations: <deselect this checkbox, determine whether calculate statistical figure as volatilities or correlations> |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are back to the initial screen, and the job you just scheduled is displayed in the result area. |  |
| 8 | Check Result | Choose  at the end of the row for the job you just scheduled. | The Job Details screen is displayed.If it is in status Finished (depends on parameters you entered for Scheduling Options), click on the icon beside Results, a new window will open and you can check the result of this finished job. |  |

### Output Management

SAP S/4HANA introduces a new output management approach. This new output management includes cloud qualities, such as:

- Extensibility enablement
- Multi-tenancy enablement
- Modification-free configuration

The complete configuration differs from the configuration that is used when output management is based on NAST. The configuration is based on BRF+, which is accessible for customers. In SAP S/4HANA, the target architecture is based only on Adobe Document Server and Adobe Forms. BRF+ functionality (in this case, in combination with message determination) is used for the form determination rules (along with other output parameters). For TRM, we deliver an application object type Treasury and Risk Management. All the predelivered output determination rules are maintained under this application object type. We provide several apps to let you easily manage your output.

#### Output Parameter Determination

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the Output Parameter Determination app to manage the determination rules for the output. The following determination steps are under Treasury and Risk Management:

Table 9: Determination Steps

| Step | Information | Comments about settings |
| --- | --- | --- |
| Output type | SAP predelivers necessary configurations | Do not change this setting |
| Receiver | SAP predelivers necessary configurations | Do not change this setting |
| Channel | SAP predelivers necessary configurations | Do not change this setting |
| Printer Settings | SAP predelivers necessary configurations | You can change this setting |
| Email Recipient | Maintain e-mail recipients for outgoing correspondence objects in the e-mail channel | This setting overwrites the e-mail address in Business partner master data |
| Email Settings | Specify the e-mail template and sender e-mail address. SAP predelivers PDF form templates. | Create your own forms with the Maintain Email Template app |
| Form Template | Specify the PDF form template and number of copies. SAP predelivers PDF form templates. | Create your own forms with the Maintain Form Template app |
| Output Relevance | SAP sets all output types as output relevant | Do not change this setting |

|  |
| --- |
| Note The operations to change these settings are similar. This section describes the steps to change the e-mail recipients and sender's e-mail address as an example. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). | The Output Parameter Determination view displays. |  |
| 3 | Display current Email recipients | Enter the following data and press Enter:Show Rules for: Treasury and Risk Management CorrespondenceDetermination Step: Email RecipientNote By default, no e-mail recipients are maintained by SAP. | The default e-mail recipient rule displays. |  |
| 4 | Maintain Email recipient for Internal Counterparty | In the Maintain Business Rules section, choose Edit. |  |  |
| 5 | Maintain Email recipient for Internal Counterparty | Choose Insert New Row. |  |  |
| 6 | Maintain Email recipient for Internal Counterparty | Make the following entries:Output Type: TRM_DEAL_SLIPNote To enter the value, from the dropdown list, choose Direct Value Input. In the field to the right of the is equal to value, enter TRM_DEAL_SLIP and choose OK. Use this method for the remaining field entries in this step.Role: INEmail Type Code: To, CC, or BCCE-Mail Address: for example, <Email address>Note To add more condition columns, choose Table Settings and make the necessary changes. For example, you can add another condition column (BusPartner) to maintain different e-mail recipients for different business partners. | The internal recipient e-mail address is maintained. |  |
| 7 | Maintain Email recipient for external counterparty | Repeat steps 5 to 6 with the following data:Output Type: TRM_TRANSACTION_CONFIRMATION (Transaction Confirmation)Role: INEmail Type Code: To, CC, or BCCE-Mail Address: for example, <Email address> | The external recipient Email address is maintained. |  |
| 8 | Activate Email Addresses | Choose Activate. | The Confirmation Activation dialog box displays. |  |
| 9 | Activate Email Addresses | Choose Yes. | The system displays the message Objects saved and activated. The e-mail addresses are saved and activated. |  |
| 10 | Display Email settings for Sender Email address and Email template | Enter the following data and press Enter:Determination Step: Email Settings | The default e-mail settings are displayed. |  |
| 11 | Change Email settings for Sender Email address and Email template | Choose Edit. |  |  |
| 12 | Change Email settings for Sender Email address and Email template | Make the following entries:Sender Email: for example, <Email address>.Note To create a new e-mail template, use the Maintain Email Template app. | Email settings are changed. |  |
| 13 | Activate Email Settings | Choose Activate. | The Confirmation Activation dialog box displays. |  |
| 14 | Activate Email Settings | Choose Yes. | The system displays the message Objects saved and activated. The e-mail settings are saved and activated. |  |

#### Manage Output Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once the output correspondence objects are generated, you can use this app to track the status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Output Items (F2279). | The Manage Output Items view displays. |  |
| 3 | Enter filter criteria and execute the report | Make the following entries and choose Go:Application Object ID: <Transaction number>Application Object Type: TRM_CORRESPONDENCENote If the Application Object ID field is not displayed, choose Adapt Filters. Choose More Filters. Select Application Object ID and choose OK.Note When you enter the data in the input field, an input help automatically displays the possible entries for you. You can choose from the list instead of enter the whole words.Correspondence objects could have following status:In PreparationCompletedIn pendingErrorTo check the detailed log, select the correspondence and choose Show Application Log.To resend a correspondence object even it has completed status, you can select the correspondence object and choose Resend. | The status of the output correspondence objects is listed. You can search for your transaction and check the status. |  |

#### Maintain Print Queues

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check the outgoing correspondence objects in the Print channel.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Print Queues (F1260). | The Maintain Print Queues view displays. |  |
| 3 | Display TRM Print Queue Status | Scroll down and choose a TRM print queue (for example, Default). | The Print Queue view displays. |  |
| 4 | Display TRM Print Queue Status | Select a line with the transaction number you noted in a prior step. Click the text of the print name to download a PDF file.Note By default, SAP provides the following print queue for TRM:DEFAULT | All the TRM outgoing correspondence objects in channel Print display with latest status. |  |

#### Display Email Transmissions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

For the e-mail channel, you can check if the e-mail is successfully sent.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Monitor Email Transmissions (F5442). | The Monitor Email Transmissions view displays. |  |
| 3 | Display Email Transmission Status | Use the Status dropdown list to filter for Error, Sent or Waiting.Use the Created At field to search within a specific date range and choose Go.Note If an e-mail status is Transmitted, the e-mail is sent out to the recipient.If an e-mail status is Sent, the system tried to send the e-mail. However, the user is not guaranteed to receive the e-mail. | All the outgoing e-mails for selected correspondences are displayed. |  |

#### Maintain Email Template

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create your own e-mail templates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Email Templates - Deprecated (F1306). | The Maintain Email Template view displays. |  |
| 3 | Copy a Predelivered Email Template to a Custom Email Template | Choose the Predelivered tab. | The predelivered e-mail templates are displayed. |  |
| 4 | Copy a Predelivered Email Template to a Custom Email Template | Use the Search field to find an email template to copy (for example, FTR_CORR_EMAIL_TEMPLATE_CNF), select the checkbox and choose Copy. | The Copy Template FTR_CORR_EMAIL_TEMPLATE_CNF dialog box displays. |  |
| 5 | Copy a Predelivered Email Template to a Custom Email Template | Make the following entries:Name: for example, TRM Transaction Confirmation Customer Email TemplateNote The new copied e-mail template is prefixed with YY1_. | The system displays the message Template has been copied. |  |
| 6 | Change Customer Email template | Locate and choose your copied e-mail template within the Custom tab view, in this example: YY1_FTR_CORR_EMAIL_TEMPLATE_CN. |  |  |
| 7 | Change Customer Email template | Choose Change Details. | The TRM Transaction Confirmation Default Email Template dialog box displays. |  |
| 8 | Change Customer Email template | Make the following entries and choose Change Details:Description: TRM Transaction Confirmation Customer Email Template | The Email Template view displays. |  |
| 9 | Change Customer Email template | In the Available Languages pane, select a language version, for example, English. Click the name itself. | The Email Template Content view displays. |  |
| 10 | Change Customer Email template | Adjust the e-mail subject and body as needed. When done, choose Save.Note SAP defines variables that you can use in e-mail templates. To view the variable list, choose Show Data Fields. | The custom e-mail template is adjusted successfully. |  |

#### Maintain Form Template

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create your own form templates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Form Templates (F1434). | The Output Management Form Template view displays. |  |
| 3 | Download a Predelivered Form Template | Choose the Predelivered Templates tab. All the pre-delivered form templates display. | Predelivered templates are displayed. |  |
| 4 | Download a Predelivered Form Template | Select a form template (for example, FDP_TRM_CONF_DE) | The details of the form template are displayed. |  |
| 5 | Download a Predelivered Form Template | Choose Download. | The Download Template dialog box displays. |  |
| 6 | Download a Predelivered Form Template | Choose OK. | The form template is downloaded successfully. |  |
| 7 | Change the customer Form template file | Using Adobe LiveCycle Designer, adjust and save the form template.Note You must install Adobe LiveCycle Designer to edit the form template. |  |  |
| 8 | Upload Customer Form Template | Open Maintain Form Templates (F1434). | The Output Management Form Template view displays. |  |
| 9 | Upload Customer Form Template | Choose the Custom Templates tab. |  |  |
| 10 | Upload Customer Form Template | Choose New. | The Create Form Template dialog box displays. |  |
| 11 | Upload Customer Form Template | Make the following entries and choose OK:Form Template Name: for example, CUST_TRM_CONF_DELanguage: for example, EnglishSelect Form Template File: select Browse and choose the file.Data Source: for example, FDP_TR_CORR_SRVForm Type:Content | The customer form template is created successfully. |  |

### Reconciliation of External Securities Account Statements

Purpose

This section described the reconciliation of external securities account statements activities which are not described in the Test Procedures section.

#### Create the Statements of External Securities Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create the statement of external securities account manually.

If the treasury correspondence integration with SWIFT Network is set up, and the statement is generated from the incoming MT535 message automatically, the step can be skipped. Refer to the test script Treasury Correspondence Integration with SWIFT Network3QM for details.

Prerequisite

The External Securities Account ID is maintained for the security account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Statements - External Securities Account (RECON4). | The Select External Securities Account Statement of Processing screen is displayed. |  |
| 3 | Enter Parameters | On the Select External Securities Account Statement of Processing screen, enter the following data and choose Enter:Company Code: for example, 3310Securities Account ID: for example, <External Securities Account ID you have created>, for example, 123XXXX567 | The External Securities Account Statements: Display screen is displayed. |  |
| 4 | Create New Statement | Choose Create external securities account statement screen, enter the following data and choose Save:Company Code: for example, 3310External Sec. Acct ID: for example, <External Securities Account ID you have created>, for example, BD_AE3Key Date: for example, <Current Date>Date Category: for example, Position DateStatus: for example, SOPENDescription: for example, External Statement | New statement is created. |  |
| 5 | Create External Position | On the tab Pos., choose Create Position. New screen External Position : Create is displayed. Enter the following data, and choose Save:ID Number: for example, <the security class you have created> , for example, BD_04External Nominal Amount: for example, 100,000,000.00 | New external position is created. |  |

#### Reconciliation of External Securities Account Statements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you reconcile the statement of external securities account with internal position.

Prerequisite

The statement of external securities is uploaded.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Reconcile Statement - External Securities Account (RECON5). | The Reconciliation of External Securities Account Statements Using Sec. Acct ID screen is displayed. |  |
| 3 | Enter Parameters | On the Reconciliation of External Securities Account Statements Sec. Acct ID screen, enter the following data and choose Execute:Company Code: for example, 3310Securities Account ID: for example, <External Securities Account ID you have created>, for example, 123XXXX567Key Date: for example, <Current Date>Status: for example, SOPEN | The Reconciliation of External Securities Account Statements Using Sec. Acct ID screen is displayed. |  |
| 4 | Check the Reconciliation Report | On the Reconciliation of External Securities Account Statements Using Sec. Acct ID screen, check the reconciliation report. | If there is a difference between the internal and external nominal, an error message will occur. |  |

### Accounting

Purpose

This section described some accounting relevant activities which are not described in the Test Procedures section.

#### Reverse Accrual

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step allows you to reverse accrual posted for the deal.

For example, you executed the accrual on an incorrect date, you would like to reverse it.

Prerequisite

The accrual of the position has been posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Reverse Accrual/Deferral (TPM45). | The Reverse Accrual/Deferral of Expenses and Revenues screen is displayed. |  |
| 3 | Test Run | On the Reverse Accrual/Deferral of Expenses and Revenues screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC Transactions: <unselect this checkbox>Company code: for example, 3310Valuation Area: leave bank, or enter specific valuation are, for example, AE0Sec. Class ID Number: <Security class ID number(s) for which accrual has been executed>Securities Account: <Securities account(s) for which accrual has been executed>Accrual/Deferral Key Date: for example, <date on which the reversal of accrual should take place>Test Run: <select this checkbox>Reasons for Reversal: for example, 04 Other reasonsImmediate Posting: <select this checkbox> | New screen Reverse Accrual/Deferral of Expenses and Revenues is displayed.Choose Logs and Messages, you can see the simulated reversal posting information, please note there is no posting created because it is test run. |  |
| 4 | Production Run | Choose Back until the initial screen of this app, change the following data and choose Execute:Test Run: <unselect this checkbox> | New screen Execute Accrual/Deferral of Expenses and Revenues is displayed.Choose Logs and Messages, you can see the posting information for reversal, this time, accounting document has been created. |  |

#### Reverse Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step allows you to reverse posted period end valuation for the deal.

For example, if you have done the period end valuation with incorrect currency rates or incorrect evaluation type. This would lead to wrong accounting results which need to be reversed.

Prerequisite

The period end valuation of the deal has been posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Reverse Valuation (TPM2). | The Reverse Valuation screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Reverse Valuation screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC Transactions: <unselect this checkbox>Company code: for example, 3310Valuation Area: leave bank, or enter specific valuation are, for example AE0Sec. Class ID Number: <Security class ID number(s) for which valuation has been executed>Securities Account: <Securities account(s) for which valuation has been executed>Key Date for Valuation: for example, <the date on which the reversal should take place>Reasons for Reversal: for example, 04 Other reasonsTest Run: <select this checkbox> | The Display Positions to be Reversed screen is displayed. |  |
| 4 | Reverse Valuation for Test Run | On the Display Positions to be Reversed screen, choose Reverse Valuation. | The screen Reversal Log: Reversed Business Transactions is displayed, and message Valuation (test run) has been successfully reversed shows up.Note You can check the simulated reversal posting information on this screen, please note there is no posting created because it is test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until initial screen of this app.On the initial screen, change the following data and choose Execute:Test Run: <unselect this checkbox> | The Display Positions to be Reversed screen is displayed. |  |
| 6 | Reverse Valuation for Production Run | On the Display Positions to be Reversed screen, choose Reverse Valuation(TPM2). | The screen Reversal Log: Reversed Business Transactions is displayed, and message Valuation has been successfully reversed shows up.Note You can check the posting on this screen, this time, accounting document for reversal has been created. |  |

#### Reverse Debit Position

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If you need to reverse the debit position after posting, you can use the app Reverse Debit Position (FWOEZ).

Prerequisite

A previous debit position has been posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Reverse Debit Position (FWOEZ). | The Manual Posting / Debit Position: Reverse screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Manual Posting / Debit Position: Reverse screen, enter the following data and choose Enter:Company Code: for example, 3310ID Number: for example, <Security class ID number(s) for which debit position has been executed>Securities account: for example, <Security account for which debit position has been executed> | A list of fixed debit positions is displayed. |  |
| 4 | Reverse Debit Position(FWOEZ) | On the Manual Posting / Debit Position: Reverse screen, select a record to reverse and choose Reverse business transaction: | The Reverse Business Transaction screen is displayed. |  |
| 5 | Process the Reversal | On the Reverse Business Transaction screen, enter the following data and choose Reverse:Reason for Reversal: for example, Process. errorFI Rversal Date: for example, <original posted date> |  |  |

### Market Risk Analyzer

#### Manage Market Data Shift

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can create market data shifts to analyze key figures with modified market data, which will be used in the Defining Report Layout for Calculate Market Risk Key Figures step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Market Data Shift (JBR0) | The Edit Market Data Shifts screen is displayed. |  |
| 3 | Enter Market Data Shifts Name | On the Edit Market Data Shifts screen, enter the following data and choose Create:Market Data Shift: for example, 1 | The Define Market Data Shifts screen is displayed. |  |
| 4 | Define Market Data Shift | On the Edit Market Data Shifts screen, enter the following dataShort Name: for example, <Market Data Shift 0001> |  |  |
| 5 | Maintain Yield Curves of Market Data Shift | On the Edit Market Data Shifts screen, choose the Yield Curves tab, choose the Insert Row button, then enter the following data and choose SaveShort Name: for example, Euro Depo ShiftCurrency: for example, AEDYC. Type: for example, 0001Ref.Int.Rate: for example, AEDM03EIBPercentage: for example, 2 | Market Data Shift is saved |  |

#### Maintain Scenarios

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a scenario. A scenario is a market data record which can contain current market data, exchange rates, exchange rate volatilities, yield curves, interest rate volatilities, e.g. you can create scenarios, which represent market situations you consider possible or probable (for example, a high interest rate scenario with an inverted yield curve).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Middle Office | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Scenarios (TV21) | The Scenario Admin: Initial Screen screen is displayed. |  |
| 3 | Enter Scenario Name | On the Scenario Admin: Initial Screen screen, enter the following data and choose Create:Scenario: for example, 1 | The Create Scenario 1 screen is displayed. |  |
| 4 | Maintain Scenario | On the Create Scenario 1 screen, enter the following dataScenario: Full Name: for example, Scenario 1Scenario: Short Name: for example, Scenario 1 |  |  |
| 5 | Maintain Exch. Rates of Scenario | On the Create Scenario 1 screen, choose the Exchange Rates tab, then enter the following data:Reference Currency: for example, AEDIn the Other Currencies area, choose Insert Row, enter the following data:Currency: for example, USDBid Rate: for example, 1.2Ask Rate: for example, 1.2Then choose Save.Note Market Data Shift is parameter shifts based on market data imported; for scenario, you can maintain parameters without reference. | Scenario is saved |  |

#### Defining Report Layout for Calculate Market Risk Key Figures

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the report layout for market risk key figures report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Calculate Market Risk Key Figures (AISGENKF). | The Calculate Market Risk Key Figures screen is displayed. |  |
| 3 | Access Report Layout Definition screen | On the Calculate Market Risk Key Figures screen, enter the Evaluation Currency and Evaluation Type, and choose Define Report Layout. | The "Key Figure Layout": Change screen is displayed. | . |
| 4 | Create Layout-ID entries | On the "Key Figure Layout": Change screen, Choose New Entries, then insert the following data in the Key Figure Layout form and Save:ROW1Layout-ID: for example, Y01Short Name: for example, NPV/BPV/DurationLong Name: for example, NPV/BPV/DurationROW2Layout-ID: for example, Y02Short Name: for example, NPV + Market Data shiftsLong Name: for example, NPV + Market Data shifts | Two new entries have been created. |  |
| 5 | Access Key Figures Maintain screen | On the "Key Figure Layout": Change screen, select the checkbox of Layout-ID Y01, then double click Key Figures folder in the Dialog Structure panel. | The Change View "Key Figures": Overview screen is displayed in the main area. |  |
| 6 | Maintain Key Figures of Layout | On the "Key Figure Layout": Change screen, choose New Entries and then insert the following data in the Key Figures form:ROW1Key Figure Name: for example, BARWERTPos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, NPVShort Name: for example, NPVShift Rule: for example, 1 or Market Data Shift Rule you createdDec.Places: for example, 0ROW2Key Figure Name: for example, BPVPos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, SKF_BASE_POINTShort Name: for example, BPVShift Rule: for example, 0Dec.Places: for example, 0ROW3Key Figure Name: for example, CRFNPVPos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, RISK_FREE_NPVShort Name: for example, Current Risk Free NPVShift Rule: for example, 0Dec.Places: for example, 0ROW4Key Figure Name: for example, DURATION1Pos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, SKF_FWDURATIONShort Name: for example, Modified DurationShift Rule: for example, 0Dec.Places: for example, 0ROW5Key Figure Name: for example, DURATION2Pos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, SKF_MACAULAYShort Name: for example, Macaulay DurationShift Rule: for example, 0Dec.Places: for example, 0and Save. | The New Entries: Overview of Added Entries screen displays allowing entry of the Key Figures name and configuration settings. |  |
| 7 | Access Key Figures Maintain screen | Go back to the New Entries: Added Entries screen, select the checkbox of Layout-ID Y02, then double click on the Key Figures folder in the Dialog Structure panel. |  |  |
| 8 | Maintain Key Figures of Layout | On the "Key Figure Layout": Change screen, Choose New Entries, then insert the following data in Key Figures form and Save:Key Figure Name: for example, NPVPos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, NPVShort Name: for example, NPVShift Rule: for example, 1 or Market Data Shift Rule you createdDecimal Places: for example, 0 |  |  |

#### Manage Market Risk Key Figure Sets

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the parameters for the market risk key figures calculation, including evaluation currency, evaluation type, scenario, and market data shift rule.

The market risk key figures calculation is processed as a scheduled background job, the result of which is recorded in the database for analysis.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Market Risk Key Figure Sets (AFWKF_SET) | The "Market Risk Key Figure Set": Change screen is displayed. |  |
| 3 | Define Risk Factor Set | On the "Market Risk Key Figure Set": Changescreen, double click on the Risk Factor Set folder in the Dialog Structure panel on the left side. Choose New Entries, insert the following data in the Risk Factor Setform:RiskF. Set: for example, R01Description: for example, Risk Factor Set with FX Rate and Yld CurvesFX Risk: <select the checkbox>IR Risk: <select the checkbox>Then select the created entry, double click on the Risk Currency folder in the Dialog Structure panel on the left side. Choose New Entries, insert the following data in the Risk Currency form:Row 1Currency: for example, USDlR Risk: <select the checkbox>Then double click on the Interest Rate Term folder in the Dialog Structure panel on the left side. Choose New Entries,insert the following data in the Interest Rate Term form and choose Save:Row 1Term: for example, 1Time Unit: for example, MonthRow 2Term: for example, 3Time Unit: for example, MonthRow 3Term: for example, 6Time Unit: for example, MonthRow 4Term: for example, 1Time Unit: for example, Year | A new risk factor set is created. |  |
| 4 | Maintain Market Risk Key Set | Double click on the Market Risk Key Figure Set folder in the Dialog Structure panel on the left side. Choose New Entries, insert the following data in the Market Risk Key Figure Set form and choose Save:row 1MR Key Figure Set: for example, MRK01Description: for example, Market Key Figure Set without VaREvaluation Currency: for example, AEDEval. Type: for example, Y001Calc. VaR: <deselect>RT Update: <select>Note If the UpdUponChg checkbox is selected, once a new financial object is created or changed, an automatic calculation of the market risk key figure set is triggered. The calculation only covers the updated object. The adjustment run is based on the basic run of same date that is processed by scheduled job.Row 2MR Key Figure Set: for example, MRK02Description: for example, Market Key Figure Set (VaR Hist.Sim.)Evaluation Currency: for example, AEDEval. Type: for example, Y001Calc. VaR: <select>VaRTyp: for example, SV1RiskF. Set: for example, R01Row 3MR Key Figure Set: for example, MRK03Description: for example, Market Key Figure Set (VaR MonteCarloSim.)Evaluation Currency: for example, AEDEval. Type: for example, Y001Calc. VaR: <select>VaRTyp: for example, SV2RiskF. Set: for example, R01Row 4MR Key Figure Set: for example, MRK04Description: for example, Market Key Figure Set (VaR Variance/Covariance)Evaluation Currency: for example, AEDEval. Type: for example, Y001Calc. VaR: <select>VaRTyp: for example, SV3RiskF. Set: for example, R01Note If the Calc. VaR checkbox is selected, the parameters of the VaR type and the risk factor set need to be assigned; the market data scenario or market data shift should be blank. | Market Risk Key Set is savedThe VaR type SV1 is for the VaR calculation method as historical simulation;The VaR type SV2 is for the VaR calculation method as Monte Carlo simulation;The VaR type SV3 is for the VaR calculation method as variance-covariance approach. |  |

### Credit Risk Analyzer

#### Display Limit Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to display limit overview.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Limit Overview (TBL3). | The Overview of Limits screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Overview of Limits screen, enter the following data and choose Execute:Limit Type: for example, Y01 to Y09Company Code: for example, 3310 | The Display Limits for Limit Types: Overview screen is displayed. |  |

### Simulated Valuation

#### Run Simulated Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Simulated valuation key figures are used to verify how balance and P&L figures have been developing since last period end.

The simulated key figures cover all relevant valuation figures which are usually generated within the period end closing process.

Simulated valuation processing covers:

- Valuation of Treasury Positions
- Accrual calculation of interest payables/receivables

Prerequisite

You have created a bond transaction.

NPV values need to be stored in advance of the valuation of Treasury positions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Simulate Period-End Closing (TPM_SIM_VAL). | The Simulate Period-End Closing screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Simulate Period-End Closing screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC Transactions: <deselect this checkbox>Company Code: for example, 3310Valuation Area: for example, AE0Product Type: for example,04ASecurity ID: for example, <Security Class ID Number(s) created in previous steps>, for example, BD_AE3Security Account: for example, BOND_INVSTRecalculate Outdated Sim.Val.: <deselect this checkbox>Note If you set this indicator, you can recalculate the outdated simulation resultsSimulation Date: for example, <the current date>Key Date Valuation: <select this checkbox>Accrual/Deferral: <deselect this checkbox>Note If you set this indicator, the accrual/deferral of expenses and revenues for the selected treasury positions is simulated, and Accrual/Deferral Parameter is displayed.Test Run: <select this checkbox> | The following message is displayed:Processed xx positions; xx successful, 0 failed.If Recalculate Outdated Simulation Results has been executed, the following message is displayed:xx simulated results deleted for key date, Processed xx positions; xx successful, 0 failed. |  |
| 4 | Execute Simulated Valuation | The dialog Message shows up, and choose Continue. | The screen Simulate Period-End Closing is displayed.You can check the simulated valuation information for local GAAP (valuation area AE0). Please note there is no simulated valuation created because it is test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back to the initial screen of this app.On the initial screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The dialog Messages screen is displayed. |  |
| 6 | Execute Simulated Valuation for Production Run | The dialog Message shows up, and choose Continue. | The screen Simulate Period-End Closing is displayed.You can check the simulated valuation information for local GAAP (valuation area AE0). |  |

#### Delete Simulated Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you reverse the simulated valuation you've just run.

Prerequisite

You've executed the simulated valuation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Delete Results of Simulated Period-End Closing (TPM_SIM_VAL_DEL). | The Delete Results of Simulated Period-End Closing screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Delete Results of Simulated Period-End Closing screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC Transactions: <deselect this checkbox>Company Code: for example, 3310Valuation Area: leave bank, or enter specific valuation are, for example, AE0Product Type: for example,04ASecurity ID: for example, <Security Class ID Number(s) created in previous steps>, for example, BD_AE3Security Account: for example, BOND_INVSTSimulation Date: for example, <the date on which the reversal should takes place>Test Run: <select this checkbox> | The following message is displayed:xx simulated results deleted for key date (the date on which the reversal takes place). |  |
| 4 | Enter Selection Criteria for Production Run | Go back to the initial screen of this app.On the Delete Results of Simulated Period-End Closing screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The following message is displayed:xx simulated results deleted for key date (the date on which the reversal takes place). |  |

### Security Account Transfer

#### Security Account Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you transfer the bond position to the new security account.

Prerequisite

You have purchased a bond transaction.

You've created a new security account Bond_ISSUE1 by referring to the[Create Security Account for Issuance](#unique_27) [page ] 40 step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Execute Securities Account Transfer (FWDU). | The Securities Account Transfer: Initial screen is displayed. |  |
| 3 | Enter Selection Criteria for Securities Account Transfer | On the Securities Account Transfer: Initial screen, enter the following data and choose Execute:Company Code: for example, 3310Security ID: for example, for example, BD_AE1Source Sec. Account: for example, for example, BOND_ISSUEPos. Value Date: for example, <the current date> | The Securities Account Transfer: Edit screen is displayed. |  |
| 4 | Enter Detailed Data for Securities Account Transfer | On the Securities Account Transfer: Edit screen, enter the following data and choose Save:Target Sec.Acct: for example, BOND_ISSUE1Nominal Amount: for example, 100000Pos. Value Date: for example, <the current date>Calc. Date: for example, <the current date>Document Date: for example, <the current date> | The screen Information Overview is displayed. If red traffic light exists, click on it and check the error message. Solve the issue and perform test run again until there is no error.You can check the posting information by choosing Logs + Messages. |  |
| 5 | Review logs | Choose Messages and Log.On Information Overview dialog box, choose Posting Log.On Posting Log: Posted Business Transactions view, you review the postings. | Logs are reviewed. |  |

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
> Flagged while digesting this document, not verified: Import Price Index Values purpose text duplicates the reference interest rate wording (apparent copy-paste in source).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Maintain Email Template step uses app F1306 labelled Deprecated, while Output Parameter Determination refers to a Maintain Email Template app.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Payment-run examples use differing identifiers (BD_AE3, BD_AE 3, BD_04) across steps, possibly inconsistent example data.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[05-treasury-and-cash-management/bond-management-3wy-ae-test-script-sap-s-4hana-cloud-public-edition-26-part-01]]
- related-to :: [[05-treasury-and-cash-management/bond-management-group-ledger-ifrs-3wz-ae-test-script-982]]
- related-to :: [[05-treasury-and-cash-management/test-script-bond-management-group-ledger-us-gaap-3x0-ae-983]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3WY_S4CLD2608_BPD_EN_AE.docx` — lines 2912–4949 of the extracted text · extracted with `mammoth` · 413,538 chars in the whole document
