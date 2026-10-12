---
id: 05-treasury-and-cash-management/test-script-letter-of-credit-management-49d-ae-sap-s-4hana-cloud-publi-part-02
title: "Test Script: Letter of Credit Management (49D_AE) - SAP S/4HANA Cloud Public Edition (49D_S4CLD2608_BPD_EN_AE) — part 2 of 2"
description: "SAP S/4HANA Cloud 2608 (AE) test script, Letter of Credit Management (49D): payments, standby L/C receive/rollover/terminate, treasury reports, alerts."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/letters-of-credit]
aliases: []
keywords: [Letter of Credit Management, standby letter of credit, payment request, payment medium file, treasury posting, settlement status, letter of credit rollover, letter of credit termination, treasury reports, financial positions]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/49D_S4CLD2608_BPD_EN_AE.docx#lines-2871-3595"]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1002
topic: 05-treasury-and-cash-management/letters-of-credit
language: EN
part: 2/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Letter of Credit Management (49D_AE) - SAP S/4HANA Cloud Public Edition (49D_S4CLD2608_BPD_EN_AE) — part 2 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/49D_S4CLD2608_BPD_EN_AE.docx`, part 2 of 2 (lines 2871–3595 of the extracted text), extracted with `mammoth`. Grouped under **Letter of Credit Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

Each financial transaction contains flows that must be paid. When creating the transaction, the payment request is selected as required (usually only for outgoing payment, in practice). The treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows that require payment request, it does not create posting in financial accounting.

When payment is initiated by the financial partner, skip this procedure and the [Process Payment Request](#unique_82) [page ] 142 procedure and continue with the [Bank Initiated Payment](#unique_83) [page ] 146 procedure.

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <transaction number you noted from the previous procedure>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <latest payment Date you noted in previous procedure or current date + 2 years>Test Run: <select>Pay Only: <select>Note The first payment date is normally the same as current date. | The Payment Log - Test Run screen is displayed. Review the payment information on this view.If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to [Post to General Ledger](#unique_84) [page ] 146 procedure. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Payment Log displays, and a payment request is generated.Make a note of the key number displayed on this view as the number is required for other procedures. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows view, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <the transaction number you noted down from the previous procedure>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <latest payment Date you noted in previous procedure or current date + 2 years>Test Run: <select>Note The first payment date is normally the same as current date. | The Payment Log - Test Run view displays. Review the payment information on this view.If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows view, change the following data and choose Run:Test Run: <deselect> | Payment Log displays, and a payment request is generated.Note Make a note of the key number displayed on this view as the number is required for other procedures. |  |

###### Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you use the Automatic Payment Transactions for Payment Requests (F111) app to start the Payment Program for Payment Requests. The payment program for payment requests is an additional automatic payment option in the SAP system. Unlike the standard payment program, the payments are not based on open items (vendor/customer items) but on payment requests.

Prerequisite

You have generated payment request in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests view is displayed. |  |
| 3 | Enter Run Date and Identification | On the Automatic Payment Transactions for Payment Requests view, enter the following data, and choose Maintain payment run parameters:Run Date: for example, <current date>Identification: for example, TRM03 | The Automatic Payment Transactions: Parameters view is displayed. |  |
| 4 | Enter Parameters | On the Automatic Payment Transactions: Parameters view, enter the following data:Posting Date: for example, <current date>Next payment run on: for example, <current date + 12 months>Company Code: for example, 3310Payment Methods: for example, TFChoose Dynamic selectionsOn the Free Selection for payment run dialog box, enter the following data, and choose Save:Key Number: <the four key numbers you noted from the previous procedure>Choose Additional Log. On the Additional Log dialog box, enter the following data:Payment method selection in all cases: <select this indicator>Line items of the payment documents: <select>Due date check: <select>and choose Continue.Note If the Log created for all accounts message displays, choose Continue.Choose Save on the Automatic Payment Transactions: Parameters view. | The Parameters have been entered message is displayed on the Automatic Payment Transactions for Payment Requests view. |  |
| 5 | Schedule Proposal | Choose Schedule proposal..On the Schedule Proposal dialog box, choose Start Immediate and choose Schedule Job to confirm this dialog box.The Proposal is running message is displayed in the status bar with a yellow traffic light status.Choose Update status, until the Payment proposal has been created message is displayed in the status bar with green traffic light status.NoteIf you choose Edit Proposal, and choose Continue on the Accounting clerk view, the Edit Payment Proposal: Payments view is displayed.You should see one line with green light on the Edit Payment Proposal: Payments view.If there is only one line with red light or even other error messages display, then the payment proposal is not successful. In this case, you need to check and correct the error so that you can continue to do the next step of this test. | Payment proposal is generated. |  |
| 6 | Schedule Payment | Choose Schedule payment.On the Schedule Payment dialog box, choose Start Immediat. and choose Create Payment Medium, then choose Schedule Job to confirm the dialog box.The Payment run is running message is displayed in the status bar with yellow traffic light status.Choose Update status, until the Payment run has been carried out message is displayed with green traffic light status. | The payment document is created.If SAP Bank Communication Management is not implemented in your system, the payment medium created uses the PMW format. To review the payment log, select the Display payment log.If SAP Bank Communication Management is implemented in your system, in the Display payment log and the Payment run XX/XX/20XX TRM03R is intended for cross-payment run payment media message is displayed, then a SAP Bank Communication Management batch is created after the payment run. Proceed to the following step. |  |
| 7 | Cross-Payment Run Payment Media (Create SAP Bank Communication Batch) | The following step only applies if SAP Bank Communication Management is implemented in your system,On the Automatic Payment Transactions for Payment Requests view, choose Environment > Payment medium > Cross-Payment Run Payment Medium > Create Payment Medium .On the Creation of Cross-Payment Run Payment Media view, enter the following data, and choose Run:Run Date: for example <current date>Identification: for example TRM03R | The Creation of Cross-Payment Run Payment Media dialog box is displayed and states that Collector XX/XX/20XX XXXXXX was created or updated confirming the SAP Bank Communication Management batch is created.Note A batch may require additional approvals before payment medium is finally created. For more information, refer to the Basic Cash Operations (BFB) test script. |  |

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

When the outgoing payment is initiated by the bank, skip the [Generate Payment Request](#unique_81) [page ] 140 and [Process Payment Request](#unique_82) [page ] 142 procedures because no requests are required.

Procedure

When the bank initiates payment skip to the [Post to General Ledger](#unique_84) [page ] 146 procedure.

##### Post to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. There are two SAP Fiori apps available for posting flows:

- Fix, Pay and Post Flows (TBB1): Use this SAP Fiori app supports to generate posting for incoming payment and outgoing payment without payment request. You can not use this app to generate postings for outgoing payments that have been processed in the previous Generate Payment Request step with the Pay Only option.
- Process Business Transactions (TPM10): You use this SAP Fiori app to generate postings for outgoing payments that have been processed in the previous Generate Payment Request step with the Pay Only option.

Prerequisites

Outgoing payments handled using payment request were processed in the previous Generate Payment Request procedure with the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data:Trade Finance: <select>Company Code: For example, 3310Transaction: <transaction number with inflow or outflow which was created in previous steps>Up to and Including Due Date: Enter date on which the flow of financial transaction should be posted, for example, <current date + 2 years>Test Run: <select>Post Operational Only: <select>and choose Execute: | The Posting Log: Posted Business Transactions view is displayed. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting created during a test run.If the No flows exist for processing message is displayed, no posting is needed for your selection criteria.You can skip the next steps and continue with step 6, using the Process Business Transactions (TPM10) app. |  |
| 4 | Back | Choose Back. | The Treasury: Post Flows view is displayed. |  |
| 5 | Production Run | Make the following entries and choose Execute:Test Run: <deselect> | The Posting Log: Posted Business Transactions view is displayed. The accounting document is created for incoming payment in the local GAAP (valuation area AE0). |  |
| 6 | Access another SAP Fiori app | Return to the SAP Fiori launchpad and open Process Business Transactions (TPM10). | The Process Business Transactions view is displayed. |  |
| 7 | Enter Selection Criteria for Test Run | Enter the following data, and choose Execute.:OTC Transactions: <select>Company Code: For example, 3310Valuation Area: For example, AE0Limit by Transaction Number: <deselect this checkbox>Limit by Subledger Pos.: <select>Transaction: <transaction number with outflow, and its payment request has been generated in step Generate Payment Request>Test Run: <select> | The Test Run: Post/Reverse Business Transactions view displays.If the You have not selected any business transactions message is displayed, no postings are needed for your selection criteria. You can skip the current step. |  |
| 8 | Check Test Run Result | Choose Select All.Choose Choose Those to Post.Choose Execute. | The Test Run: Display Posted/Reversed Business Transactions view is displayed. |  |
| 9 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions view is displayed. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting is created during a test run. |  |
| 10 | Back | Choose Back. | The Process Business Transactions view is displayed. |  |
| 11 | Deselect Test Run | Make the following change:Test Run: <deselect>and choose Execute. | The Update Run: Post/Reverse Business Transactions view is displayed. |  |
| 12 | Production Run | Choose Select All.Choose Choose Those to Post.Choose Execute. | The Update Run: Display Posted/Reversed Business Transactions view is displayed. |  |
| 13 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions view is displayed. The accounting document is created for outgoing payment in the local GAAP (valuation area AE0). |  |

### Receive Standby Letter of Credit

#### Receive Standby Letter of Credit

Purpose

In this section, you manage Standby Letter of Credit lifecycle from the exporter perspective.

##### Generate Limit Utilization

Purpose

In this step, you perform end-of-day process during which the system determines and updates limit utilizations

Procedure

Perform the following steps in the Debt and Investment Management (1WV) test script.

- Generate Limit Utilization

##### Check Limit Utilization Report(Optional)

Purpose

In this step, you check the limit utilization report in the system.

Procedure

Perform the following steps in the Debt and Investment Management (1WV) test script.

- Check Limit Utilization Report

##### Receive Standby Letter of Credit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once you receive a Standby Letter of Credit, you need to enter the Standby Letter of Credit information into SAP S/4HANA Cloud Public Edition system. Normally, as the receiver or beneficiary of a Standby Letter of Credit, you don't need to pay any cash collateral. And also, the issuing bank won't charge you. So normally there won't be any outgoing or incoming payments to be done. However, in some special cases, for example back to back Standby Letter of Credits, there could be payments coming with receiving Standby Letter of Credits. SAP S/4HANA Cloud Public Edition system can fully support these business processes.

This section describes what you need to maintain in the system when receiving a Standby Letter of Credit.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Letter of Credit (FTRTLC01). | The Create Letter of Credit: Initial Screen is displayed. |  |
| 3 | Enter Data on Initial View | On the Create Letter of Credit: Initial Screen, enter the following data and choose Enter:Company Code: for example, 3310Product Type: for example, 85BTransaction Type: for example, 200Partner: for example, 33537001 | The data is entered and Create Letter of Credit: Structure screen is displayed. |  |
| 4 | Enter Data on Structure tab | On the Create Letter of Credit: Structure, enter the following data, and choose Save:Flow Type: 1860Amount: for example, 1MStart: for example, <Current Date>End: for example, <Current Date + 1 year>L/C Number: for example, SLC201909150002, which should be unique in the systemApplicant: for example, <search for a customer with BP role FLCU00 or FLCU01>.Issuing Bank: 33537001If the following messages is displayed, choose Continue.No limits were exceededMM/DD/YYYY is not a working dayIf there are incoming or outgoing payments coming with the Standby Letter of Credit, you can also enter those fees in the Free Conditions or Other Flows tab. In this case, you can refer to the Issue Standby Letter of Credit section to enter these data.If there is no customer master data with BP role FLCU00 or FLCU01, then you can either enter 33537001 or refer to the Create Customer Master - MDS (BND) master data script to create a customer. | The Standby Letter of Credit is saved.The following message is displayed:Financial transaction saved under number 100000000XXXX.Note Write down this transaction number. |  |

##### Set Settlement Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After you create the transaction in the system, you need to settle the transaction before you can proceed with further processes. Normally this needs to be done once you receive the Standby Letter of Credit from the bank.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a SAP_BR_TREASURY_SPECIALIST_BOE | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing view displays. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing view, enter the following data and choose Run.Company Code: for example, 3310Transaction: for example, <Transaction number wrote down in previous step>Note Keep the default values for all the other fields. | The transaction is displayed on Trade Finance: Collective Processing view. |  |
| 4 | Settle the Transaction | On the Trade Finance: Collective Processing view, choose the checkbox before the transaction created in previous step, and choose Settle.On the Settle Standby Letter of Credit : Structure view, choose Save.Note If the following messages are displayed, choose Continue:No limits were exceededMM/DD/YYYY is not a working dayFor receiving Standby Letter of Credits without incoming or outgoing payments, once the transaction is settled, the whole process is done.If you've already entered incoming or outgoing payments in the previous step, then you need also to finish the whole payment process by referring to the whole [Standby Letter of Credit Fees and Cash Collateral Payment](#unique_63) [page ] 103 process under the Issue Standby Letter of Credit section. | The Standby Letter of Credit transaction is settled. The following message is displayed:Financial transaction saved under number 100000000XXXX.Note If you choose Display on the Trade Finance: Collective Processing view, you should see the transaction is now in the Rollover Settlement status. |  |

#### Roll Over Standby Letter of Credit

##### Rollover Standby Letter of Credit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the you receive the Standby Letter of Credit, in case the amount or validity term of the Standby Letter of Credit is changed, you can roll over the Standby Letter of Credit in the SAP S/4HANA Cloud Public Edition system by changing the Standby Letter of Credit amount or end of term.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing view is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing view, enter the following data:Company Code: for example, 3310Transaction: for example, <transaction number you noted from the previous procedure>Term End: for example, <current date>Accept default values for other parameters and choose Run. | The transaction is displayed on the Trade Finance: Collective Processing view. |  |
| 4 | Roll over the Transaction | On the Trade Finance: Collective Processing view, select the checkbox before the transaction, and choose Roll Over.On the Roll Over Standby Letter of Credit: Structure view, enter following data, and choose Save:Amount: for example, 2MEnd: for example, <current date + 2 years>Note If the following messages are displayed, choose Continue:No limits were exceededMM/DD/YYYY is not a working day | The transaction has been rolled over successfully.The following message is displayed on Trade Finance: Collective Processing view:Financial transaction saved under number 100000000XXXX |  |

##### Set Settlement Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you settle the rolled-over transaction in the system before you can proceed with further processes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing view is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing view, enter the following data and choose Run:Company Code: for example, 3310Transaction: for example, <Transaction number you noted down in previous step>Note Keep the default values for all the other fields. | The transaction is displayed on the Trade Finance: Collective Processingview. |  |
| 4 | Settle the Transaction | On the Trade Finance: Collective Processing view, choose the checkbox before the transaction created in previous step, and choose Settle.On the Settle Letter of Credit : Structure view, choose Save.Note If the following messages are displayed, choose Continue:No limits were exceededMM/DD/YYYY is not a working day | The Letter of Credit transaction is settled, and the following message is displayed:Financial transaction saved under number 100000000XXXX.Note If you choose Display on the Trade Finance: Collective Processing view, you should see the transaction is now in the Rollover Settlement status. |  |

#### Terminate Standby Letter of Credit

During the validity period of a Standby Letter of Credit, if the Standby Letter of Credit is not needed or the related duties have been performed, then you need to terminate the Standby Letter of Credit.

##### Terminate Standby Letter of Credit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you terminate a Standby Letter of Credit.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing view is displayed. |  |
| 3 | Enter Data on Initial View | On the the Trade Finance: Collective Processing view, enter the following data:Company code: for example, 3310Transaction: for example, <transaction number you noted from the previous procedure>Term End: for example, <current date>Accept default values for other parameters and choose Run. | The transaction is displayed on the Trade Finance: Collective Processing view. |  |
| 4 | Terminate the Transaction | On Trade Finance: Collective Processing view, select the checkbox before the transaction, and choose Terminate.On Terminate Standby Letter of Credit : Structure view, enter following data, and choose Save:Terminate: for example, <current date + 1 year and 6 months>Note If the following messages are displayed, choose Continue:No limits were exceededMM/DD/YYYY is not a working day | The transaction has been rolled over successfully.The following message is displayed on the Trade Finance: Collective Processing view:Financial transaction saved under number 100000000XXXX |  |

##### Set Settlement Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you settle the terminated standby letter of credit in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing view is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing view, enter the following data and choose Run:Company Code: for example, 3310Transaction: for example, <Transaction number you noted down in previous step>Note Keep the default values for all the other fields. | The transaction is displayed on the Trade Finance: Collective Processing view. |  |
| 4 | Settle the Transaction | On the Trade Finance: Collective Processing view, choose the checkbox before the transaction, and choose Settle.On the Settle Standby Letter of Credit: Structure view, choose Save.Note If the following messages are displayed, choose Continue:No limits were exceededMM/DD/YYYY is not a working dayFor receiving Standby Letter of Credits without incoming or outgoing payments, once the transaction is settled, the whole process is done.If you've already entered incoming or outgoing payments in previous step, then you need also to finish the whole payment process by referring to the whole [Standby Letter of Credit Fees and Cash Collateral Payment](#unique_78) [page ] 135 process under the Issue Standby Letter of Credit section. | The Standby Letter of Credit transaction is settled, and the following message is displayed:Financial transaction saved under number 100000000XXXX. |  |

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

In this activity, you define a set of key figures to be displayed on the Financial Status - Book Value and Financial Status - Nominal Amount screens.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Risk Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Define Financial Positions (FTR_FP_DEF). | The "Maintain Financial Position Groups": Change screen is displayed. |  |
| 3 | Maintain Key Figure Groups | Choose New Entries.Make the following entries and choose Save:Financial Position Group: for example, FPG_A0001Financial Position Group Description: for example, Bank accounts and Short term investAssets/Liabilities: for example, Assets | The data is saved. |  |
| 4 | Maintain Key Figures | Choose the Maintain Financial Positions tab.Choose New Entries.Make the following entries and choose Save:Financial Position: for example, FP_A0001Financial Position Description: for example, Bank accountsFinancial Position Group: for example, FPG_A0001Data Source: for example, Treasury Position Management | The data is saved. |  |
| 5 | Maintain Selections | Select the financial position above, and choose Back, then choose Maintain Selections.Make the following entries, then choose Back:Product Type = 85A to 85BTransaction Type = 100 to 200Valuation Class = 71Valuation Class = 43Choose Save. | The data is saved. |  |

#### Financial Status (Nominal Amount)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check the financial status of a nominal amount.

Prerequisites

You have defined financial positions.

Refer to the [Define Financial Positions](#unique_141) [page ] 157 step for more details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Risk Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Financial Status (FTR_FPM_FINANCIAL_STATUS (FTR_FPM_FS_NOMAMT)). | The Financial Status - Nominal Amount screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Go:Key Date: for example, <Current Date>Display Currency: for example, AEDExchange Rate Type: for example, MCompany Code: for example, 3310 | The data is displayed per the selection criteria. |  |

#### Display Treasury Alerts - Settlement, Payment, Release, Correspondence and Interest Rates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check treasury alerts for various type of transactions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Alerts - Settlement (F4979) | The Display Treasury Alerts screen is displayed. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Issue Message For: SettlementCompany code: 3310 | Alerts data is displayed per the filter values. |  |
| 4 | Confirm Alerts for Other Transactions | Select other values in the Issue Message For field. |  |  |
| 5 | Select Display Treasury Alerts Tiles with Release | Open Display Treasury Alerts - Release (F4980). | The Display Treasury Alerts screen is displayed, with the issue message For: Release. |  |
| 6 | Select Display Treasury Alerts Tiles with Payment | Open Display Treasury Alerts - Payment (F4981). | The Display Treasury Alerts screen is displayed, with the issue message For: Payment. |  |
| 7 | Select Display Treasury Alerts Tiles with Correspondence | Open Display Treasury Alerts - Correspondence (F4983). | The Display Treasury Alerts screen is displayed, with the issue message For: Correspondence. |  |

#### Display Treasury Payments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check all payment journals for review.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Payments (TPM20A). | The Payment Journal screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Execute:Company Code: for example, 3310Product Type: for example, 85A/85B | The payment journals display. |  |
| 4 | Review data | Review the data displayed on the screen. You can also choose Original business transaction or Details to drill down for more details. |  |  |

#### Display Treasury Posting Journal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display posting journals for review.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Posting Journal (F1755). | The Display Treasury Posting Journal screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Go:Product Group: for example, OTC TransactionsCompany Code: for example, 3310 | The posting journals display per the filter values. |  |

#### Display Treasury Posting Flows

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the position flows.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Accountant | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Position Flows (F1754). | The Display Treasury Position Flows screen displays. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Go:Product Group: for example, OTC TransactionsCompany code: for example, 3310 | The position Flow data displays per the filter values. |  |

#### Display Treasury Position Values

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display treasury position values.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Position Values (F1867). | The List Report screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Go:Key Date: for example, <Current Date>Product Group: for example, OTC TransactionsCompany Code: for example, 3310 | The position values data displays per the filter values. |  |

#### Display Treasury Alerts - Posting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display treasury alerts for posting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Alerts - Posting (F4984) | The Display Treasury Alerts screen displays. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Go:Issue Message For: PostingCompany code: for example, 3310 | Alerts data displays per the filter values. |  |

## Appendix

### Notification for Managing Financial Transactions

Situation handling is a framework provided by SAP S/4HANA that could increase the quality and efficiency of business processes by signaling exceptional information. Notification for Manage Financial Transactions (F6157) is enabled in Treasury and Risk Management. For example, if a foreign exchange option expires today and needs to be exercised, a notification will be sent. And if a trade finance contract is going to be expired, a notification will also be sent to the responsible person. There are several channels for notification, including the notification area on the SAP Fiori launchpad and email.

|  |
| --- |
| Note Make sure scope item Situation Handling (31N) is activated in your system before you use this functionality. |

To integrate with situation handling, Treasury and Risk Management provides the following:

- Situation Template: FIN_TRM_FINTRANS_PROCG
- Standard Team Category: FSCM_TRM

There are some customizing configurations needed. In SAP S/4HANA Cloud Public Edition, the following best practice customizing configurations are pre-delivered.

Table 2: Predefined Entities

| Entity | Definition | Description |
| --- | --- | --- |
| Functions | STRM_FT_FO | Front Office Employee for Financial Transactions |
|  | STRM_FT_BO | Back Office Employee for Financial Transactions |
| Function Profiles | STRM_FP | Function Profile for Treasury and Risk Management |
| Team Types | STRM_FOE | Treasury Specialist - Front Office |
|  | STRM_BOE | Treasury Specialist - Back Office |

You need the following business roles to do the test.

| Business Role | Business Role ID | Application |
| --- | --- | --- |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Manage Teams and Responsibilities (F2412)Manage Situation Types (F2947) |
| Treasury Specialist - Front Office | SAP_BR_TREASURY_SPECIALIST_FOE | My Situations (F4537) |
| Treasury Specialist - Back Office | SAP_BR_TREASURY_SPECIALIST_BOE | My Situations (F4537) |

#### Create Teams and Responsibilities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a team and maintain the general information and responsibility definitions for the team.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Teams and Responsibilities (F2412). | The Manage Teams and Responsibilities screen displays. |  |
| 3 | Create Team | Choose Create. | The Team screen displays. |  |
| 4 | Maintain Team General Information | In the General Information section, enter the following data:Name: for example, Z_TEST_01Type: for example, STRM_FOE or STRM_BOEDescription: for example, <TRM Test Description for Situation Handling>Status: Enabled | The Global ID will be generated automatically. |  |
| 5 | Maintain Responsibility Definitions | In the Responsibility Definitions section, enter the following data:Company Code: 3310Transaction Type: <leave blank>Product Type: 85APortfolio: <leave blank>Note You can create your own Portfolio in Manage Your Solution in S/4 HANA or Central Business Configuration in Central Business Configuration using the Define Portfolio configuration activity, so only the transaction assigned with your own portfolio will trigger the notification process. |  |  |
| 6 | Maintain Team Members | In the Team Members section, enter the following data and choose Create:Business Partner: <Choose the user you want to get the notification or email in F4 help>Note To get email notifications, you need to maintain the user's email correctly.Functions: STRM_FT_FO |  |  |
| 7 | Save the Team | Choose Save. | The Team is created successfully. |  |

#### Enable Situation Types

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the situation type for your teams.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Situation Types (F2947). | The Manage Situation Types screen displays. |  |
| 3 | Search the Standard Situation Template | Enter FIN_TRM_FINTRANS_PROCG in the search box and Choose Go. | The Situation Template FIN_TRM_FINTRANS_PROCG shows up in the result. |  |
| 4 | Create New Situation Type via Copy | Select the template and choose Copy. | 1 Situation Type or Types Copied.The Situation Type screen displays. |  |
| 5 | Maintain Situation Type Admin Information | On the Situation Type screen, enter the following data:ID: <A unique id with Z_ as prefix>, for example, Z_TRM_ST01Name: Processing of Financial Transactions |  |  |
| 6 | Maintain Conditions | In the Conditions section, enter the following data:Set to Status: OpenSend Notification: <check>In the All Filters section, enter the following data:Company Code: 3310Product Type: 85ATransaction Type: 200Term End: NEXT14DAYS |  |  |
| 7 | Maintain Batch Job Scheduling | In the Batch Job Scheduling section, enter the following data:Time Zone: UTC+08Start Batch Job At: 12:00 |  |  |
| 8 | Maintain Situation Display | In the Situation Display section, you can insert variables if you want to receive detailed information for the notification and email.Enter the following data, and choose Insert Variables:Company Code: <COMPANYCODE>Product Type: <FINANCIALINSTRUMENTPRODUCTTYPE>Transaction: <FINANCIALTRANSACTION>Letter of Credit No.: <LETTEROFCREDIT>In the Notification section, make the following settings：Aggregate Notifications: <check>Resend Notifications: <check> |  |  |
| 9 | Check Recipients | In the Recipients section, make sure the team to receive notifications is listed in the Number of Teams. |  |  |
| 10 | Maintain Situation Monitoring | In the Situation Monitoring section, enter the following data, and choose Create:Monitor Instances: <select>Note Choose Yes in the dialog box to enable the situation type. | The situation type is created. |  |

#### Create a Normal Letter of Credit

Purpose

In this step, you create a normal letter of credit that terminates in 14 days.

Procedure

Refer to [Receive Normal Letter of Credit](#unique_46) [page ] 76 to create a normal letter of credit with receive process, and make sure the end term is within 14 days as of the current date.

#### Trigger and Schedule the Notifications

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you trigger the notification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Situation Types (F2947). | The Manage Situation Types screen displays. |  |
| 3 | Search the Standard Situation Template | Enter FIN_TRM_FINTRANS_PROCG in the search box and choose Go. | The Situation Template FIN_TRM_FINTRANS_PROCG shows up in the result. |  |
| 4 | Find the Situation Type | Select the template and switch to the Situation Types tab. | All the situation types under the TRM situation template is displayed. |  |
| 5 | Go to the Detail of the Situation Type | Select the situation type you create in [Enable Situation Types](#unique_144) [page ] 167, double click the selected situation type. | The Situation Type detail screen is displayed. |  |
| 6 | Trigger the Notification | Choose Trigger Now on the Situation Type detail screen. | The Information message The background process for creating situation instances has been triggered is displayed. |  |
| 7 | Check the Triggered Objects List in Situation Instances List | Check OK in the dialog box. | You will go to the Situation Instances screen.Check the letter of credit you created in [Create a Normal Letter of Credit](#unique_145) [page ] 169 on the result list. |  |

#### User Setting for Notification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you enable the notifications for your user.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your own user. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open profile of the logged-on user in the right corner. |  |  |
| 3 | Find the Notifications Setting | Choose Notifications in Settings. | The Notifications screen is displayed. |  |
| 4 | Enable the Email and Notification Alert in Launchpad | On the Notifications screen, enter the following data, and choose Save:Email: <select>High Priority: <check>Enable: Enabled |  |  |

#### Check the Notification in Fiori Launchpad and E-Mail

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the notification in Fiori Launchpad and email notification in Outlook.

Procedure

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Test Step # | Test Step Name | Instruction | Expected Result |  |
| 1 | Log On | Log on to the SAP Fiori launchpad with your own user. | The SAP Fiori launchpad displays. |  |
| 2 | Check Notification Area | Choose the red exclamation mark in the Notification Area. | You will see Notification Msg By Date, By Type, By Priority in the Notification Area. |  |
| 3 | Check Detail Message | Choose Show More. | Notification detail is displayed. |  |
| 4 | Check My Situations | Open My Situations (F4537). | Your open situations are displayed. |  |
| 5 | Check Email | Check email notifications in Outlook.Note The batch job will trigger when you define the Situation Type. | You will receive email notifications in the email address you maintained in your user account. |  |

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
- related-to :: [[05-treasury-and-cash-management/test-script-letter-of-credit-management-49d-ae-sap-s-4hana-cloud-publi-part-01]]
- related-to :: [[05-treasury-and-cash-management/letter-of-credit-management-group-ledger-ifrs-49e-ae-1003]]
- related-to :: [[05-treasury-and-cash-management/letter-of-credit-management-group-ledger-us-gaap-49f-ae-1004]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/49D_S4CLD2608_BPD_EN_AE.docx` — lines 2871–3595 of the extracted text · extracted with `mammoth` · 304,091 chars in the whole document
