---
id: 05-treasury-and-cash-management/test-script-interest-rate-derivatives-management-1x3-ae-sap-s-4hana-cl-part-02
title: "Test Script: Interest Rate Derivatives Management (1X3_AE) - SAP S/4HANA Cloud Public Edition (1X3_S4CLD2608_BPD_EN_AE) — part 2 of 2"
description: "Treasury test script (S/4HANA Cloud 2608, AE), part 2: swaption lifecycle, reports, and appendices on jobs, output, accounting, market/credit risk, simulation."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/interest-rate-derivatives]
aliases: []
keywords: [Interest Rate Derivatives Management, swaption lifecycle, payment requests, treasury correspondence, key date valuation, net present value, treasury reports, background jobs, output management, accounting reversals]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1X3_S4CLD2608_BPD_EN_AE.docx#lines-3128-5563"]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-775
topic: 05-treasury-and-cash-management/interest-rate-derivatives
language: EN
part: 2/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Interest Rate Derivatives Management (1X3_AE) - SAP S/4HANA Cloud Public Edition (1X3_S4CLD2608_BPD_EN_AE) — part 2 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1X3_S4CLD2608_BPD_EN_AE.docx`, part 2 of 2 (lines 3128–5563 of the extracted text), extracted with `mammoth`. Grouped under **Interest Rate Derivatives Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

Each financial transaction contains flows that must be paid. When creating the transaction, select the payment request as required (usually only for outgoing payment). The treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows that require payment request. It does not create posting in financial accounting.

|  |
| --- |
| Remember When the payment is initiated by the financial partner, skip this procedure and the Process Payment Request procedure. Continue with the Bank Initiated Payment procedure. |

|  |
| --- |
| Note To schedule a background job for this procedure, see the corresponding step in the Appendix. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <transaction number you noted in previous procedure>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <Payment Date you created in previous procedure>Test Run: <select>Pay Only: <select> | The Payment Log - Test Run view displays, . Check the payment information.If the No flows exist for processing message displays, no payment with payment request is required for your selection criteria. You can skip to the Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back.Change the following data and choose Run.Test Run: <deselect> | The Payment Log view displays. The payment request is generated. Make a note of the key number displayed on this view: __________ |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | Enter the following data, and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <transaction number you noted from the previous procedure>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <Payment Date you noted in previous procedure>Test Run: <select> | The Payment Log - Test Run view displays. Review the payment information on this view.If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back. | The Fix and Pay Flows view displays. |  |
| 5 | Production Run | Enter the following data, and choose Run:Test Run: <deselect> | The Payment Log view displays and a payment request is generated.Note Make note of the key number displayed on this view as the number is required for other procedures. |  |

###### Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use the Automatic Payment Transactions for Payment Requests (F111) app to start the Payment Program for Payment Requests. The payment program for payment requests is an additional automatic payment option in the SAP system. Unlike the standard payment program, the payments are not based on open items (vendor/customer items) but on payment requests.

Prerequisite

Payment request is generated, from the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests view displays. |  |
| 3 | Enter Run Date and Identification | On the Automatic Payment Transactions for Payment Requests view, enter the following data:Run Date: for example, <current date>Identification: for example, TRM01and choose Parameters. | The Automatic Payment Transactions: Parameters view displays. |  |
| 4 | Enter Parameters | On the Automatic Payment Transactions: Parameters view, enter the following data:Posting Date: for example, <current date>Next payment run on: for example, <current date + 12 Months>Company Code: for example 3310Payment Methods: for example, TFChoose Dynamic selections, on the Free Selection for payment run dialog box, enter the following data:Key number: <the key number you noted from the previous procedure>and choose Save.Choose Additional Log, on the Additional Log dialog box, enter the following data:Payment method selection in all cases: <select>Line items of the payment documents: <select>Due date check: <select>and choose Continue.Note If the Log created for all accounts message displays, choose Continue.Choose Save on the Automatic Payment Transactions: Parameters view. | The Parameters have been entered message displays on Automatic Payment Transactions for Payment Requests view. |  |
| 5 | Schedule Proposal | Choose Proposal.On the Schedule Proposal dialog box, choose Start Immediat. and choose Schedule Job to confirm this dialog box.The Proposal is running message displays in the status bar with a yellow traffic light status.Choose Status, until the Payment proposal has been created message appears in the status bar with green traffic light status. | Payment proposal is generated. |  |
| 6 | Schedule Payment | Choose Pmnt run.On the Schedule Payment dialog box, choose Start Immediat. and choose Create Payment Medium, then choose Schedule Job to confirm the dialog box.The Payment run is running message displays in the status bar with yellow traffic light status.Choose Status, until the Payment run has been carried out message appears with green traffic light status. | The payment document is created.If SAP Bank Communication Management is not implemented in your system, the payment medium created uses the PMW format. To review, select the Display payment log.If SAP Bank Communication Management is implemented in your system, in the Display payment log and the Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media message appears, then a bank communication management batch must be created after the payment run. Proceed to the following step. |  |
| 7 | Cross-Payment Run Payment Media (Create Bank Communication Batch) | The following step only applies if SAP Bank Communication Management is implemented in your system,On the Automatic Payment Transactions for Payment Requests view, choose Menu > Environment > Payment medium > Cross-Payment Run Payment Medium > Create Payment Medium .On the Creation of Cross-Payment Run Payment Media view, enter the following data:Run Date: for example, <current date>Identification: for example, TRM01Rand choose Run. | The Creation of Cross-Payment Run Payment Media dialog box appears and states that Collector XX/XX/20XX XXXXXX was created or updated confirming the bank communication management batch is created.Note A batch may require additional approvals before payment medium is finally created. For more information, see the Advanced Cash Operations(J78) scope item. |  |

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

When the outgoing payment is initiated by the bank, skip the Generate Payment Request and Process Payment Request procedures. No requests are required.

Procedure

When the bank initiates payment skip to the Post to General Ledger procedure.

##### Post to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the posting functionalities, the posting-related cash flows are transferred to the FI interface. This generates the relevant postings in financial accounting. Two apps are available for posting flows:

- Fix, Pay and Post Flows (TBB1): Use this app to generate the posting for incoming payment. When using this app for this procedure, it does not create posting for the outgoing payment that you processed in the previous Generate Payment Request procedure using the Pay Only option.
- Process Business Transactions: Use this app to generate the posting for outgoing payment that you processed in the previous Generate Payment Request procedure using the Pay Only option.

|  |
| --- |
| Note To schedule a background job for this procedure, see the corresponding step in the Appendix. |

Prerequisite

The outgoing payment handled by the payment request for this transaction is processed in previous Generate Payment Request procedure using the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data and choose Execute:Derivatives: SelectedCompany code: for example, 3310Transaction: <transaction number with inflow created in previous procedure>Up to and Including Due Date: enter date the flow of the financial transaction is posted, for example, <current date>Test Run: SelectedPost Operational Only: Selected | The Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note There is no posting created since this is a test run.If the system displays the message No flows exist for processing, no posting is required for your selection criteria. Skip the Production Run step and continue the test step using theProcess Business Transactions app. |  |
| 4 | Production Run | Choose Back.Change the following data and choose Execute:Test Run: Deselected | The Posting Log: Posted Business Transactions view displays. An accounting document is created for incoming payment in local GAAP (valuation area AE0). |  |
| 5 | Access another SAP Fiori app | Open Process Business Transactions (TPM10). | The Process Business Transactions view displays. |  |
| 6 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Transactions: SelectedCompany Code: for example, 3310Valuation Area: for example, AE0Limit by Subledger Pos.: SelectedTransaction: <transaction number with outflow, and payment request been generated with Generate Payment Request procedure>Test Run: Selected | The Test Run: Post/Reverse Business Transactions view displays.Note If the You have not selected any business transactions message displays, no posting are required for your selection criteria, you can skip the current step. |  |
| 7 | Check Test Run Result | Choose Select All, choose Choose Those to Post, and choose Execute.Choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note There is no posting created since this is a test run. |  |
| 8 | Enter Selection Criteria for Production Run | Choose Back.Change the following data and choose Execute:Test Run: Deselected | The Update Run: Post/Reverse Business Transactions view displays. |  |
| 9 | Production Run | Choose Select All, choose Choose Those to Post, and choose Execute.Choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. The accounting document is created for outgoing payment in local GAAP (valuation area AE0). |  |

#### Post Realized Profit and Loss

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you fix and post derived business transactions. Usually this occurs for realized profit and loss when a deal is mature.

|  |
| --- |
| Note To schedule a background job for this procedure, see the corresponding step in the Appendix. |

Prerequisite

The maturity date of transaction has been reached and the financial transaction has been created, settled, and posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Post Derived Business Transactions (TPM18). | The Post Derived Business Transactions view displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Transactions: <select>Company code: for example 3310Valuation Area: for example, AE0OTC Transactions: <transaction numbers that are mature>TRL Date: <maturity date of transaction>Test Run: <select>Note If the Are you sure that you want to select future business transactions message displays, confirm the message by choosing Enter.Note If the No scheduled derived business transactions were found for the selection message displays, no derived transaction is available for your selection. Skip this step. |  |  |
| 4 | Fix and Post for Test run | Choose Fix. | The Post Derived Business Transactions view displays.Note Review the simulated posting information for local GAAP (valuation area AE0).Note No posting is created since this is a test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until you return to the initial view of this app.Change the following data and choose Execute:Test Run: <deselect>Note If the Are you sure that you want to select future business transactions message displays, confirm the message by choosing Enter. | The Post Derived Business Transactions view displays. |  |
| 6 | Fix and Post for Production Run | Choose Fix. | An information dialog box displays.The posting information for local GAAP (valuation area AE0) and the accounting document are created in local GAAP (valuation area AE0). |  |

### Swaption

Purpose

This section describes how to create swaptions and the subsequent procedures to settle and execute the contract until completion (either exercise or expire).

Swaptions are options on a Swap, which you can exercise on a certain date or within a certain period. As the buyer, you can choose whether to pay fixed interest rates or whether to receive fixed interest rates after the option has been exercised. You pay a premium to the seller for this right upon conclusion of the transaction.

#### Market Data

Purpose

In this step, you enter market data (such as foreign currency exchange spot rates, swap rates, reference interest rates, and so on). The data provides default values when creating new transactions.

Procedure

Complete all steps in the Market Rates Management – Manually via Upload (1XN) scope item before proceeding.

#### Check Limit Utilization Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the limit utilization report.

Prerequisite

The limit master records of your company are maintained in the system.

|  |
| --- |
| Note NPV calculation doesn’t support swaptions right now. Value of swaption deals will not be counted in limit management and if you run End-of-Day Processing (KLNACHT), error messages will pop up. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Review Limit Utilizations (TBLB). | The Overview of Utilizations - Selection Using all Characteristics screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Execute:Limit Type: for example, Y01 or Y07Limit Utilization Base: for example, 1Determination Date: for example, <Current Date>Limits Valid From: for example, <Current Date> | The system displays an overview of the limit utilizations in accordance with your selection criteria. |  |

#### Create Swaption Contract

Purpose

In this step, you create swaption contracts with underlyings on interest rate swap and cross-currency interest rate swap.

##### Create Interest Rate Swaption

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create an interest rate swaption transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create OTC Option (TI71). | The Create OTC Option: Initial Screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and press Enter:Company Code: for example, 3310Product Type: for example, 76TTransaction Type: for example, 100Partner: for example, 33537001 | The OTC Option: Create Contract: Structure screen is displayed. |  |
| 4 | Enter Structure | Enter data in the following groups:Option group:Expiry Date: for example, ++6 (6 months later)Expiry Time: for example, Frankfurt 15:00Exercise Type: for example, EuropeanSettlement: for example, Physical ExerciseTerm group:Start: for example, 0 (same date as Expiry Date)End: for example, ++12 (12 months later)Business Calendar group:Calendar 2: for example, <leave blank>Outcoming Interest group:Nominal Amount: for example, 1m EUR,(1,000,000.00 EUR)Note The nominal amount is only for testing purpose. You can change it according to your real business transaction.Effective From: for example, <Start Date>1st Due Date: for example, ++3, <Start Date + 3 months>Freq.Month: for example, 3Fix.Rate: for example, 3.5Int. Calc.Method: for example, chooseIncoming Interest group:Nominal Amount: for example, 1m (1,000,000.00)Effective From: for example, <Start Date>1st Due Date: for example, ++3, <Start Date + 3 months>Freq.Month: for example, 3Var.Interest: for example, AEDM03EIBInt. Calc.Method: for example, 2 act/360Premium group:Flow Type: for example, 1300 Optional Premium - Profit/LossCurrency: for example, AED 100Contract Conclusion group:Contract Date: for example, <Current Date>Stay in this screen for the following step. |  |  |
| 5 | Enter First Period Interest Rate for Variable Leg of Underlying IRS | Incoming Interest group:Choose Conditions. | The Overview of Conditions screen is displayed. |  |
| 6 | Interest Rate | Double click on CTyp 1200 Interest.Make the following entries:Int calc.type: 5 Comound Interest CalculationFirst Int Rate: for example, 3.2Choose Back to return to the Overview of Conditions screen. | The first period initial interest rate is entered. The OTC Option: Create Contract: Structure screen is displayed. |  |
| 7 | Interest Rate Adjustment | Double click on CTyp 1210 Interest rate adjustment.Make the following entries:Interest Rate Adjustment: 1 Regular 1 Calendar DaysIR Adj.Date: <effective date>, for example, <start date>Calendar rule: 3 Previous Working DayInterest Rate Fixing Date: <leave blank>Lockout Period: 2 Working DaysChoose Back twice to return to the Create Swap: Structure screen. | The Interest Rate Adjustments Tab under Condition Type 1210 is displayed. |  |
| 8 | Check Outgoing Interest Flows | Outgoing Interest group:Choose Underlying.In the Create Swap: Structure screen, choose the Outgoing tab, and review the outgoing interest flows.Choose Back to return to the OTC Option: Create Contract: Structure screen. | The outgoing interest flows are reviewed. |  |
| 9 | Check Incoming Interest Flows | Incoming Interest group:Choose Underlying.In the Create Swap: Structure screen, choose the Incoming tab, and review the incoming interest flows.Choose Back to return to the OTC Option: Create Contract: Structure screen. | The incoming interest flows are reviewed. |  |
| 10 | Enter Administration Data | Choose Administration to enter the following data and choose Save:Risk Mitigation: <deselect>Note Check the Risk Mitigation field if this transaction is intended for a risk mitigation context. If so, this transaction is excluded from the Clearing Threshold Report calculation. | The data is saved and the transaction number is generated. |  |

##### Create Cross-Currency Interest Rate Swaption

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a cross-currency interest rate swaption transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create OTC Option (TI71). | The Create OTC Option: Initial Screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and press Enter:Company Code: for example, 3310Product Type: for example, 76VTransaction Type: for example, 100Partner: for example, 33537001 | The OTC Option: Create Contract: Structure screen is displayed. |  |
| 4 | Enter Structure | Enter data in the following groups:Option group:Expiry Date: for example, ++6 (6 months later)Expiry Time: for example, Frankfurt 15:00Exercise Type: for example, EuropeanSettlement: for example, Physical ExerciseTerm group:Start: for example, 0 (same date as Expiry Date)End: for example, ++12, (12 months later)Business Calendar group:Calendar 2: for example, <leave blank>Outcoming Interest group:Nominal amount: for example, 1m EUR, (1,000,000.00 EUR)Note The nominal amount is only for testing purpose. You can change it according to your real business transaction.Effective From: for example, <Start Date>1st Due Date: for example, ++3, <Start Date + 3 months>Freq.Month: for example, 3Fix.Rate: for example, 3.5Int. Calc.Method: for example, selectIncoming Interest group:Nominal amount: for example, 1m USD, (1,000,000.00 USD)Effective From: for example, <Start Date>1st Due Date: for example, ++3, <Start Date + 3 months>Freq.Month: for example, 3Var.Interest: for example, AEDM03EIBInt. Calc.Method: for example, 2 act/360Premium group:Flow Type: for example, 1300 Optional Premium - Profit/LossCurrency: for example, AED 100Contract Conclusion group:Contract Date: for example, <Current Date>Stay in this screen for the following step. |  |  |
| 5 | Enter First Period Interest Rate for Variable Leg of Underlying IRS | Incoming Interest group:Choose Conditions. | The Overview of Conditions screen is displayed. |  |
| 6 | Interest Rate | Double click on CTyp 1200 Interest.Make the following entries:Int calc.type: 5 Comound Interest CalculationFirst Int Rate: for example, 3.2Choose Back to return to the Overview of Conditions screen. | The first period initial interest rate is entered. The OTC Option: Create Contract: Structure screen is displayed. |  |
| 7 | Interest Rate Adjustment | Double click on CTyp 1210 Interest rate adjustment.Make the following entries:Interest Rate Adjustment: 1 Regular 1 Calendar DaysIR Adj.Date: <effective date>, for example, <start date>Calendar rule: 3 Previous Working DayInterest Rate Fixing Date: <leave blank>Lockout Period: 2 Working DaysChoose Back twice to return to the Create Swap: Structure screen. | The Interest Rate Adjustments Tab under Condition Type 1210 is displayed. |  |
| 8 | Check Outgoing Interest Flows | Outgoing Interest group:Choose Underlying.In the Create Swap: Structure screen, choose the Outgoing tab, and review the outgoing interest flows.Choose Back to return to the OTC Option: Create Contract: Structure screen. | The outgoing interest flows are reviewed. |  |
| 9 | Check Incoming Interest Flows | Incoming Interest group:Choose Underlying.In the Create Swap: Structure screen, choose the Incoming tab, and review the incoming interest flows.Choose Back to return to the OTC Option: Create Contract: Structure screen. | The incoming interest flows are reviewed. |  |
| 10 | Enter Administration Data | Choose Administration to enter the following data and choose Save:Risk Mitigation: <deselect>Note Check the Risk Mitigation field if this transaction is intended for a risk mitigation context. If so, this transaction is excluded from the Clearing Threshold Report calculation. | The data is saved and the transaction number is generated. |  |

#### Correspondence

Purpose

SAP Treasury Risk Management provides standard correspondence functionality. With this correspondence functionality, whenever a treasury risk management transaction is saved, you designate whether the system sends an e-mail to the business partner or automatically prints out a form to a printer.

To use this correspondence functionality, the following data must be assigned to business partner:

- Business Partner Profile
- Business Partner Group
- Swift/BIC Code

##### Set Settlement Status (Manual)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once a treasury risk management transaction is recorded and saved, the transaction must be settled before further activities. After you get counterparty confirmation, you can settle the transaction in one of two ways:

- Manual settlement: For example, if you receive counterparty confirmation email, then you can use the following app to settle the transaction manually:
    - Manage Financial Transactions (F6157)
- Automatic settlement via correspondence process: For example, when a transaction has all the outgoing correspondence objects and incoming correspondence objects matched and set to completed status, the financial transactions will be set to settlement status automatically.

The following procedure describes settling the treasury risk management transaction manually.

Prerequisite

A treasury risk management transaction is created and available for this procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157) | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria and Execute | Enter the following data and choose Go:Company Code: for example, 3310Transaction: <Transaction Number created previously> | The transaction is displayed on the screen. |  |
| 4 | Settle the Transaction | Select the checkbox at the beginning of the transaction line and choose Settle. | The transaction data is displayed on the OTC Option: Settle Contract: Structure screen. |  |
| 5 | Save the Change | Choose Save. | The transaction is settled and saved. |  |
| 6 | Check the Status of the Transaction | Select the checkbox and choose Details at the end of the transaction line. | The OTC Option Display: Structure screen is displayed. |  |
| 7 | Check Status | Verify that the Activity field is in Contract Settlement status. | The transaction has Contract Settlement status. |  |

##### Correspondence with PDF Form

Purpose

E-mail and print are both PDF form-related outputs. By default, SAP provides business profiles for several PDF forms (for example, PR_PRINT and PR_EMAIL).

- For any business partner assigned the profile PR_PRINT, when a financial transaction is created, a PDF form is sent to predefined print queue. You can view and print the PDF file via the Maintain Print Queues (F1260) SAP Fiori app. Once you verify that the transaction information on the form is correct, you can send the paper copy of the form to the business partner.
- For any business partner assigned profile PR_EMAIL, when a transaction is created, SAP automatically sends e-mails to the Business Partner.

Once you receive the counterparty confirmation about the transaction from your Business Partner, you can settle all the correspondence objects of the transaction. Once all the correspondence objects are settled, the transaction status changes to Contract Settlement status.

Use the following apps to maintain your own settings for output:

- Output Parameter Determination. You maintain your own rules for the output. For example, you can maintain e-mail address of recipients. This rule overwrites the e-mail address of the Business Partner for an external counterparty, or it overwrites the e-mail address of User IDs for an internal counterparty.
- Maintain Email Templates - Deprecated (F1306). You maintain your own e-mail template with this app.
- Maintain Form Templates (F1434). You maintain your own form template with this app.

In the procedures in this section, you settle the treasury risk management transaction via the correspondence processing automatically.

Prerequisites

A new treasury risk management transaction must be created, as described in the previous step, since the transaction is manually settled.

###### Send Confirmation Email/Print

Purpose

SAP provides the best practices business partner group, BPG_DEFAULT. By default, if any business partner is assigned to this group, correspondence objects are automatically sent when a financial transaction is saved. As described in the Preliminary Steps section, the best practices business partner, 33537001, is assigned to BPG_GROUP, so the correspondence objects are sent automatically. However, if you use configuration step Define Business Partner Group to create new business partner groups and then do not assign the auto-send attribute, you must send those correspondence objects manually using the Send Correspondence (FTR_COSEND) app.

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Procedure

The automated procedure does not require you to do any operation in-system.

###### Check Correspondence Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you verify the status of the correspondence objects for a transaction.

|  |
| --- |
| Note For zero/low cost collar FX option (cylinder FX option), please check the status for both legs. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Correspondence - Monitor (FTR_COMONI). | The Correspondence Monitor screen is displayed. |  |
| 3 | Enter Selection Criteria on the Initial Screen | Make the following entries and choose Execute:Correspondence tab:Company Code: for example, 3310In the Financial Transaction subarea,Company Code: for example, 3310Deal Number: for example, <Transaction Number> | The Correspondence monitor - Standard View screen is displayed. |  |
| 4 | Check the Correspondence Status | All correspondence objects are displayed.Note One financial transaction can have one or more correspondence objects depending on the BP profiles and BP groups assignment.In the status column:If the channel is Email, Delivered status, the system sent an email to the email address maintained in the business partner master data. However, this email address could also be overwritten if you maintained an Email Recipient rule with the Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN) app. Use the Monitor Email Transmissions (F5442) app to verify the actual email status.If the channel is Print, the form is sent to the print queue. You can also print out the form with the Maintain Print Queues (F1260) app.Maintain your own email template with the Maintain Email Templates - Deprecated (F1306) app.Maintain your own form template with the Maintain Form Templates (F1434) app. | Correspondence objects are in Delivered status. |  |
| 5 | Display the Transaction Details | Select the checkbox for COUNTERPARTY EMAIL and choose Show Underlying.Verify the following values:Recpt/Send Type: COUNTERPARTYChannel: EMAILChoose Back. | The transaction details are displayed.The Correspondence monitor - Standard View screen is displayed. |  |
| 6 | Display the Form of the Correspondence Object | Select the checkbox for the line with the following data, then choose View Message:Recpt/Send Type: COUNTERPARTYChannel: EMAILA dialog box displays the form of the correspondence object. Choose Continue. | The form of the correspondence object displays. |  |

###### Receive Incoming Confirmation

Purpose

In the prior procedure, an outbound email is sent to the business partner. Typically, you receive counterparty confirmation from the business partner via email, phone, or other channels. This procedure takes place outside of the system.

Procedure

This procedure does not require any operation from the system.

###### Find Deal and Match Deal Details

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You have received counterparty confirmation in the previous procedure. In this procedure, you create an inbound correspondence object and match it with all the outgoing correspondence objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Correspondence - Monitor (FTR_COMONI). | The Correspondence Monitor screen is displayed. |  |
| 3 | Enter Selection Criteria on the Initial Screen | Enter the following data and choose Execute:Correspondence group:Company Code: for example, 3310Deal group:Company Code: for example, 3310Deal Number: for example, <Transaction Number>Note Make a note of the correspondence key for a COUNTERPARTY correspondence object. | Please note down the correspondence key numbers for COUNTERPARTY PRINT and COUNTERPARTY EMAIL. |  |
| 4 | Create | Choose Create. | The Options for Creating Correspondence Objects screen is displayed. |  |
| 5 | Create an Incoming Correspondence Object Referring to the Outgoing Correspondence Object | Enter the following data for groups and press Enter:Display Options group:Corresp. Category: 01 Transaction ActivitiesTransaction Details group:Company Code: for example, 3310Product Type: for example, <Product type you entered in the transaction>Incoming/Outgoing: I IncomingEntry Options: 05 Correspondence object as templateTemplate for Correspondence Object Data group:Correspondence Key: for example, <Enter the correspondence key number for COUNTERPARTY PRINT from the previous step> |  |  |
| 6 | Save | Choose Save.Note If the Automatic matching proposal screen is displayed, choose Cancel. | The incoming correspondence object is created successfully and displayed on Correspondence monitor - Standard View screen. |  |
| 7 | Match the Incoming Correspondence Object with the Outgoing Correspondence Objects for channel PRINT | Select the checkbox for the incoming correspondence object and choose Status Functions > Automatic Match . | The Automatic matching proposal screen is displayed. |  |
| 8 | Outgoing Correspondence | On the left-side of the screen, expand the incoming correspondence key. All outgoing correspondence objects of the transaction are displayed.Select all the checkboxes of the outgoing correspondence objects and choose Enter. | All the outgoing COUNTERPARTY PRINT correspondence objects of the transaction now have status completed.All the INTERNAL outgoing correspondence objects remain in Delivered status. |  |
| 9 | Match the Incoming Correspondence Object with the Outgoing Correspondence Objects for channel EMAIL | Repeat the above steps to create an incoming correspondence object for COUNTERPARTY EMAIL and match it with outgoing correspondence for channel EMAIL. |  |  |

###### Set Settlement Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the previous procedure, all the correspondence objects of the transaction are successfully matched. The standard functionality provides that the transaction is settled automatically.

In this step, you verify that the transaction has been settled automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Correspondence - Monitor (FTR_COMONI). | The Correspondence Monitor screen is displayed. |  |
| 3 | Enter Selection Criteria on the Initial Screen | Make the following entries and choose Execute:Correspondence group:Company Code: for example, 3310Deal tab:Company Code: for example, 3310Deal Number: for example, <Transaction Number> | The Correspondence monitor - Standard View screen is displayed. |  |
| 4 | Display Transaction History | Select the checkbox of the incoming correspondence object and choose Show Underlying. | The OTC Option Display: Issue Structure screen is displayed. The second line shows Activity 2 Contract Settlement. |  |

#### Premium Payment

##### Option 1: Generate and Automatically Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Each financial transaction contains flows that need to be paid. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment in practice). Treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows. Within these two apps, if you select the ‘Schedule Auto Payment Run’ option, system will automatically process the automatic payment run for payment requests.

|  |
| --- |
| Note You can also schedule a background job for this step. Please see the corresponding step in the Appendix section. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date + 2 working days>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Pay Only: <select this indicator>Test Run: <select>Note If the No flows exist for processing message displays, no payment is required for the payment request per your selection criteria and you can skip to the Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows screen, enter the following data, and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date + 2 working days>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Test Run: <select>Note If the No flows exist for processing message displays, no payment is required for the payment request per your selection criteria and you can skip to the Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by choosing Display payment log. |  |

##### Option 2 : Generate and Process Payment Request

###### Generate Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Each financial transaction contains flows that must be paid. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment). The treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows requiring a payment request. The request does not create a posting in financial accounting.

When payment is initiated by the financial partner, skip this procedure and the Process Payment Request procedure and continue with the Bank Initiated Payment procedure.

|  |
| --- |
| Note To schedule a background job for this procedure, see the corresponding procedure in Appendix. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Treasury: Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous procedure>Up to and Including Due Date: Enter date when the flow of financial transaction should be posted, for example, <current date + 2 working days>Test Run: <select>Pay Only:<select> | The Payment Log - Test Run screen is displayed. Review the payment information on this screen.If the system displays the message No flows exist for processing, no payment with payment request is required for your selection criteria. Skip to the [Post to General Ledger](#unique_94) [page ] 173 procedure. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | The Payment Log screen is displayed. The payment request is generated.Note Make note of the key number displayed on this view for use in the following procedures. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | Enter the following data, and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous procedure>Up to and Including Due Date: enter date when the flow of financial transaction should be posted, for example, <current date + 2 working days>Test Run: <select> | The Payment Log - Test Run view displays. Review the payment information on this view.If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows screen, change the following data and choose Run:Test Run: <deselect> | The Payment Log screen is displayed. The payment request is generated.Note Make note of the key number displayed on this view for use in the following procedures. |  |

###### Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use the Automatic Payment Transactions for Payment Requests (F111) app to start the Payment Program for Payment Requests. The payment program for payment requests is an additional automatic payment option in the SAP system. Unlike the standard payment program, the payments are not based on open items (vendor/customer items) but on payment requests.

Prerequisite

Payment request is generated from the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests screen is displayed. |  |
| 3 | Enter Run Date and Identification | On the Automatic Payment Transactions for Payment Requests screen, enter the following data, and choose Parameters:Run Date: for example, <Current date>Identification: for example, TRM01 | The Automatic Payment Transactions: Parameters screen is displayed. |  |
| 4 | Enter Parameters | Enter the following data, and choose Dynamic selections:Posting Date: for example, <Current date>Next payment run on: for example, <Current date + 3 days>Company Code: for example 3310Payment Methods: for example, TF | The Free Selection for payment run dialog box is displayed. |  |
| 5 | Key Number | Enter the following data, and choose Save:Key number: <the key number you noted from the previous procedure> | The Automatic Payment Transactions: Parameters screen is displayed. |  |
| 6 | Additional Log | Choose Additional Log. | The Additional Log dialog box is displayed. |  |
| 7 | Enter Parameters | Make the following settings and choose Continue:Payment method selection in all cases: <select>Line items of the payment documents: <select>Due date check: <select>Note If the Log created for all accounts message displays, choose Continue.Choose Save on the Automatic Payment Transactions: Parameters screen. | The system displays the message Parameters have been entered displays on the Automatic Payment Transactions for Payment Requests screen. |  |
| 8 | Schedule Proposal | Choose Proposal. | The Schedule Proposal dialog box is displayed. |  |
| 9 | Schedule Job | Choose Start Immediat. and choose Schedule Job. | The system displays the message Proposal is running with a yellow traffic light status. |  |
| 10 | Update Status | Choose Status, until the Payment proposal has been created message appears in the status bar with green traffic light status. | Payment proposal is generated. |  |
| 11 | Schedule Payment | Choose Pmnt run. | The Schedule Payment dialog box display is displayed. |  |
| 12 | Schedule Job | Choose Start Immediat.. Choose Create Payment Medium and choose Schedule Job. | The Payment run is running message is displayed in the status bar with a yellow traffic light status. |  |
| 13 | Update Status | Choose Status, until the Payment run has been carried out message appears with green traffic light status. | The Automatic Payment Transactions for Payment Requests (F111) screen is displayed.The payment document is created.If SAP Bank Communication Management is not implemented in your system, the payment medium created uses the PMW format. To review, select the Display payment log.If SAP Bank Communication Management is implemented in your system, in the Display payment log and the Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media message appears, then a bank communication management batch must be created after the payment run. Proceed to the following step. |  |
| 14 | Cross-Payment Run Payment Media (Create Bank Communication Management Batch) | The following step only applies if SAP Bank Communication Management is implemented in your system,On the Automatic Payment Transactions for Payment Requests screen, choose Menu > Environment > Payment Medium > Cross-Payment Run Payment Medium > Create Payment Medium . | The Creation of Cross-Payment Run Payment Media screen is displayed. |  |
| 15 | Enter Data | Enter the following data and choose Execute:Run Date: for example, <Current date>Identification: for example, TRM01 | The Creation of Cross-Payment Run Payment Media dialog box appears and states that Collector XX/XX/20XX XXXXXX was created or updated confirming the bank communication management batch is created.Note A batch may require additional approvals before payment medium is finally created. For more information, see the Advanced Cash Operations(J78) scope item. |  |

##### Send Payment Medium File

Purpose

In this activity, you send the payment medium file to your house bank to facilitate the payment.

Procedure

If Bank Communication Management (BCM) is not implemented in your system, the payment medium file will be generated upon completion of the payment run in the previous step, provided that the relevant payment method uses the PMW format.

If BCM is implemented in your system, additional approvals may be required for a BCM batch before the payment medium file can be generated. For the approval process, please refer to the section Outgoing Payment with BCM Approval Process in the test script Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/J78)).

After payment medium file is created, there are two ways for sending the payment medium file to your house bank:

- If Multi-Bank Connectivity (MBC) is not enabled, please use app Manage Payment Media (F1868) to check and download the payment medium file, and send the file to the bank via the previously agreed-upon method. Further details are provided in test script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/1EG)).
- If MBC is enabled and the relevant PMW format uses the alternative format type designated for MBC, then the payment medium file can be automatically sent to MBC. Bank will then retrieve the payment medium file from MBC and execute the payment. Further details are provided in test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/16R)).

##### Bank-Initiated Payment

Purpose

When the outgoing payment is initiated by the bank, skip the Generate Payment Request and Process Payment Request procedures because no requests are required.

Procedure

When the bank initiates payment, skip to the Post to General Ledger procedure.

##### Post to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. There are two apps available for posting flows:

- Fix, Pay and Post Flows (TBB1): Use this app to generate the posting for incoming payment. When using this app for this procedure, it does not create posting for outgoing payment that you processed in previous Generate Payment Request procedure using the Pay Only option.
- Process Business Transactions (TPM10): Use this app to generate the posting for outgoing payment that you processed in previous Generate Payment Request procedure using the Pay Only option.

|  |
| --- |
| Note To schedule a background job for this procedure, see the corresponding step in the Appendix. |

Prerequisite

The outgoing payment handled by the payment request for this transaction was processed in the previous Generate Payment Request procedure using the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data and choose Execute:Derivatives: <select>Company Code: for example, 3310Transaction: <transaction number with inflows created in previous procedure>Up to and Including Due Date: enter date on which the flow of the financial transaction is posted, for example, <current date>Test Run: <select>Post Operational Only: <select> | Note The Posting Log: Posted Business Transactions screen is displayed. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note There is no posting created since this is a test run.If the No flows exist for processing message displays, no posting is required for your selection criteria. Skip the Production Run step and continue the test step using the Process Business Transactions (TPM10) app. |  |
| 4 | Back | Choose Back. | The Fix, Pay and Post Flows screen is displayed. |  |
| 5 | Production Run | Enter the following data and choose Execute:Test Run: <deselect> | The Posting Log: Posted Business Transactions screen is displayed. An accounting document is created for incoming payment in local GAAP (valuation area AE0). |  |
| 6 | Access another SAP Fiori App | Open Process Business Transactions (TPM10). | The Process Business Transactions screen is displayed. |  |
| 7 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Transactions: <select>Company Code: for example, 3310Valuation Area: for example, AE0Limiting by Transaction Number: <deselect>Limit by Subledger Pos.: <select>Transaction: <transaction number with outflow and payment request generated with Generate Payment Request procedure>Test Run: <select> | The Test Run: Post/Reverse Business Transactions screen is displayed.Note If the You have not selected any business transactions message displays, no posting is required for your selection criteria. Skip the current step. |  |
| 8 | Check Test Run Result | Choose Select All. Choose Choose Those to Post, and choose Execute. | The Test Run: Display Posted/Reversed Business Transactions screen is displayed. |  |
| 9 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting is created since this is a test run. |  |
| 10 | Back | Choose Back. | The Process Business Transactions screen is displayed. |  |
| 11 | Deselect Test Run | Enter the following data and choose Execute:Test Run: <deselect> | The Update Run: Post/Reverse Business Transactions screen is displayed. |  |
| 12 | Production Run | Choose Select All. Choose Choose Those to Post, and choose Execute. | The Update Run: Display Posted/Reversed Business Transactions screen is displayed. |  |
| 13 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed. The accounting document is created for outgoing payment in local GAAP (valuation area AE0). |  |

#### Period-End Closing

##### Maintain Fair Value of Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you maintain the fair values, net present value (NPV) of financial transactions.

|  |
| --- |
| Note The net present values can not be calculated automatically by the Market Risk Analyzer (MRA) for swaption. Please maintain the relevant net present value manually for accounting valuation. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Net Present Values (F7601). | The Manage Net Present Values screen displays. |  |
| 3 |  | Choose Create. | The Net Present Value Data screen displays. |  |
| 4 | Enter Header | Make the following entries:Transaction: <transaction numbers created in previous steps>Company Code: for example, 3310Price / NPV Type: 001Effective from: for example, <last date of current month> |  |  |
| 5 | Enter Net Present Value Details | Make the following entries and choose Create:NPV Currency: for example, AEDNet Present Value: <the value of (risk-based) NPV>Risk-Free Net Present Value: <the value of risk-free NPV>CVA: <the value of CVA>DVA: <the value of DVA>Note To reflect credit spreads for accounting valuation, maintain the risk-based NPV in the Net Present Value field, then enter CVA/DVA, which is the difference between risk-free NPV and risk-based NPV, Net Present Value (NPV) = risk-free NPV - CVA - DVA. Otherwise, also enter the value of risk-free NPV in the Net Present Value field, and leave fields CVA and DVA blank. | Manually maintained NPV is saved. |  |

|  |
| --- |
| Note You can also use SAP Fiori app Enter Net Present Values (JBNPV) to maintain NPV manually. |

##### Perform Key Date Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The valuation function values the positions of financial instruments - based on historical cost or fair value for a given key date - and transfers results to financial accounting.

|  |
| --- |
| Note To schedule a background job for this step, see the corresponding step in the Appendix section. |

Prerequisite

Fair values (Net Present Values (NPV)) are maintained for financial transactions that are evaluated at fair value (NPV) according to accounting principles.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Run Valuation (TPM1). | The Run Valuation screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:In the Product Groups area,OTC Transactions: <select>In the General Selections area,Company Code: for example, 3310Valuation Area: for example, AE0Transaction: <Transaction numbers created in previous procedures>In the Valuation Parameters area,Key Date for Valuation: for example, <last date of current month>Valuation Category: for example, Mid-year Valuation with ResetNote When the Period End is also the Year End, use the Valuation Category of Year End ValuationTest Run: <select> | The Display Selected Treasury Positions for Valuation screen is displayed. |  |
| 4 | Execute Test Run Valuation | Choose Run Valuation.Note If the Message dialog box displays, choose Continue. | The Valuation Log screen is displayed.If an entry has a red traffic light status, select and review the error message. Correct the issue and perform test run again, until the error is resolved.To review the simulated posting information for local GAAP (valuation area AE0), choose Logs + Messages. No posting is created because this is a test run.Note If there is no simulated posting, your selected transaction does not require valuation. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until your return to the Run Valuation screen.Change the following data and choose Execute:Test Run: <deselect> | The Display Selected Treasury Positions for Valuation screen is displayed. |  |
| 6 | Execute Valuation for Production Run | Choose Run Valuation. | The Valuation Log screen is displayed.To review the simulated posting information for local GAAP (valuation area AE0), choose Logs + Messages. No posting is created because this is a test run.Because this is a production run, the accounting document is created in local GAAP (valuation area AE0). |  |

#### Transaction is Mature

Purpose

This section describes the required operations when the option transaction is mature. You may decide whether to exercise or expire the option and conduct the following operations.

##### Review Swaption Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the status of the transactions and conduct operations accordingly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157) | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Go:Company Code: for example, 3310Transaction: <Numbers of Maturing transactions> | The transaction is displayed on the screen. |  |

###### Decide to Exercise

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you perform the operations to exercise a matured interest rate swaption.

Prerequisites

An interest rate swaption transaction exists and is updated to contract settlement status, reaching its maturity.

Enter the Manage Financial Transactions screen as described in [Review Swaption Status](#unique_152) [page ] 179.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157) | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Go:Company Code: for example, 3310Transaction: <the number of maturing interest rate swaption transaction> | The transaction is displayed on the screen. |  |
| 4 | Select a Transaction and Exercise | Select a transaction with the following criteria and choose Exercise:Activity Cat. Name: Contract Settlement | The Exercise OTC Option: Structure screen is displayed. |  |
| 5 | Enter Data and Save | Enter the following criteria and choose Save:Confirm the Exercise Date:If Exercise Type is European, the Exercise Date should be equal to Exercise Period.If Exercise Type is American, the Exercise Date should be earlier than or equal to Exercise Period.Note Make sure the Contract Date is earlier than the Exercise Period. | The data is saved without error. |  |

###### Create Interest Rate Swap Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you perform operations after exercising a interest rate swaption to create an inerest rate swap transaction.

|  |
| --- |
| Note Refer to the steps under the [Interest Rate Swap](#unique_118) [page ] 38 section for subsequent operations, such as correspondence and period-end closing. |

Prerequisites

An interest rate swaption transaction is exercised.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157) | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Go:Company Code: for example, 3310Transaction: <the number of maturing interest rate swaption transaction> | The transaction is displayed on the screen. |  |
| 4 | Select a Transaction and Settle | Select a transaction that matches the following criteria and choose Settle:Activity Cat. Name: Exercise | The OTC Option: Settle Exercise: Structure screen is displayed. |  |
| 5 | Enter Data and Save | Choose Save. | The Create Swap: Structure screen is displayed. |  |
| 6 | Confirm Data and Save | Confirm the following data and choose Save.Transaction Type: 303 IRS for SwaptionEditable fields are initialized with the value from the exercised swaption transaction. Confirm them and choose Save. | The data is saved and the new transaction number is generated. |  |

###### Decide to Expire

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you perform the operations to expire a matured cross-currency interest rate swaption.

Prerequisites

An Interest Rate Swaption transaction exists, updated to contract settlement status, reaching its maturity.

Enter the Manage Financial Transactions screen as described in [Review Swaption Status](#unique_152) [page ] 179.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Go:Company Code: for example, 3310Transaction: <the number of maturing cross-currency interest rate swaption transaction> | The transaction is displayed on the screen. |  |
| 4 | Select a Transaction and Exercise | Choose a transaction that meets the following criteria, click  , and choose Expiration from the dropdown list.Activity Cat. Name: Contract Settlement | The Exercise OTC Option: Structure screen is displayed. |  |
| 5 | Enter Data and Save | Enter data and choose Save.Note Make sure the Contract Date is earlier than the Exercise Period. | The data is saved without error. |  |

##### Post Realized Profit and Loss

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you fix and post derived business transactions. Usually this occurs for realized profit and loss when a deal is mature.

|  |
| --- |
| Note To schedule a background job for this procedure, see the corresponding step in the Appendix. |

Prerequisite

The maturity date of transaction is reached.

The financial transaction is created, settled, and posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Post Derived Business Transactions (TPM18). | The Fix and Post Derived Business Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Transactions: <select>Company Code: for example, 3310Valuation Area: for example, AE0OTC Transactions: <transaction numbers which are mature>TRL Date: <maturity date of transaction>Test Run: <select>If the system displays the message Are you sure that you want to select future business transactions, choose Enter. | The Fix and Post Derived Business Transactions screen is displayed.Note If the No scheduled derived business transactions were found for the selection message displays, no derived transaction is available for your selection. You can skip this step. |  |
| 4 | Fix and Post for Test Run | Choose Fix. | The Post Derived Business Transactions screen is displayed.Note Review the simulated posting information for local GAAP (valuation area AE0).Note No posting is created since this is a test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until you return to the initial screen of this app. Change the following data and choose Execute:Test Run: <deselect>If the system displays the message Are you sure that you want to select future business transactions, choose Enter. | The Fix and Post Derived Business Transactions screen is displayed. |  |
| 6 | Fix and Post for Production Run | Choose Fix. | The Posting Log: Posted Business Transactions screen is displayed.The posting information for local GAAP (valuation area AE0) and the accounting document are created in local GAAP (valuation area AE0). |  |

### Reports

#### Display Treasury Posting Journal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the posting journals for review.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Accountant | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Posting Journal (F1755). | The Display Treasury Posting Journal view displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Go:Product Group: for example, OTC TransactionsCompany Code: for example, 3310 | The posting journals display with filtered values. |  |

#### Treasury Position Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the treasury position analysis for review.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Treasury Position Analysis | The Treasury Position Analysis view displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Go:Key Date: for example, <Current Date>Include Planned Data: for example, 1Valuation Area: for example, AE0Company Code: for example, 3310Product Type: for example, 62A, 62BNote When entering multiple product types, use the Enter key. For example, enter 62A and press Enter. Then, enter 62B and press Enter again. | The position analysis data displays filtered values. |  |

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
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Position Values (F1867). | The List Report view displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Key Date: for example, <Current Date>Product Group: for example, OTC TransactionsCompany Code: for example, 3310 | The position values data displays filtered values. |  |

#### Define Financial Positions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define a set of key figures to be displayed in the Financial Status - Book Value and the Financial Status - Nominal Amount views.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Risk Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Define Financial Positions (FTR_FP_DEF). | The "Maintain Financial Position Groups": Change screen is displayed. |  |
| 3 | Maintain Key Figure Groups | Choose New Entries. |  |  |
| 4 | Maintain Key Figure Groups | Make the following entries and choose Save:Financial Position Group: for example, FPG_DE_A0001Financial Position Group Description: for example, Bank accounts and Short term investAssets/Liabilities: for example, Assets | The data is saved. |  |
| 5 | Maintain Key Figures | Double click the Maintain Financial Positions folder tab. |  |  |
| 6 | Maintain Key Figures | Choose New Entries. | The New Entries: Overview of Added Entries view is displayed. |  |
| 7 | Maintain Key Figures | Make the following entries and choose Save:Financial Position: for example, FP_DE_A0001Financial Position Description: for example, Bank accountsFinancial Position Group: for example, FPG_DE_A0001Data Source: for example, Treasury Position Management | The data is saved. |  |
| 8 | Maintain Selections | Select the financial position from the prior step, choose Back, and choose Maintain Selections. |  |  |
| 9 | Maintain Selections | Make the following entry:Product Type = 62A to 62BTransaction Type = 300 to 302Valuation Class = 40 to 43Valuation Area = AE0Posting Status = 2Choose Back and then choose Save. | The data is saved. |  |

#### Financial Status (Book Value)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display financial status of book values.

Prerequisite

Financial positions are defined. For more information , see the previous procedure, [Define Financial Positions](#unique_104) [page ] 187.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Risk Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Financial Status (F2136). | The Financial Status - Book Value view displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Key Date: for example, <Current Date>Display Currency: for example, AEDExchange Rate Type: for example, MCompany Code: for example, 3310 | The data displays the filtered values. |  |

#### Financial Status (Nominal Amount)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display financial status of a nominal amount.

Prerequisite

Financial positions are defined. For more information , see the previous procedure, [Define Financial Positions](#unique_104) [page ] 187.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Risk Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Financial Status (FTR_FPM_FINANCIAL_STATUS (FTR_FPM_FS_NOMAMT)). | The Financial Status - Nominal Amount view displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Key Date: for example, <Current Date>Display Currency: for example, AEDExchange Rate Type: for example, MCompany Code: for example, 3310 | The data displays the filtered values. |  |

#### Display Treasury Payments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display all payment journals for review.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Treasury Payments (TPM20A). | The Payment Journal view displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Execute:Company Code: for example, 3310Product Type: for example, 62A | The payment journals display. |  |
| 4 | Review Data | Review the data displayed on the view. You can also select Original business transaction or Details to drill down for additional details. | Data is reviewed. Choosing Original business transaction will open the History Swap: Structure view. |  |

#### Display Treasury Position Flows

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
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Position Flows (F1754). | The Display Treasury Position Flows view displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Product Group: for example, OTC TransactionsCompany Code: for example, 3310 | Position Flow data displays filtered values |  |

#### Display Treasury Alerts - Posting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the treasury alerts for various types of transactions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Treasury Alerts - Posting (F4984). | The Display Treasury Alerts - Posting screen is displayed. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Issue Message For: PostingCompany Code: for example, 3310 | Alerts data is displayed. |  |

#### Display Treasury Alerts - Settlement, Release, Correspondence, and Interest Rates

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
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Treasury Alerts - Settlement (F4979). | The Display Treasury Alerts - Settlement view is displayed. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Issue Message For: SettlementCompany Code: for example, 3310 | Alerts data displays filtered values |  |
| 4 | Confirm Alerts for Other Transactions | Select other values in the Issue Message For field:ReleasePaymentPostingCorrespondenceInterest Rates |  |  |
| 5 | Select Display Treasury Alerts Tiles with Release | Open Display Treasury Alerts - Release (F4980). | The Display Treasury Alerts - Release view displays, with Issue Message for Release. |  |
| 6 | Select Display Treasury Alerts Tiles with Payment | Open Display Treasury Alerts - Payment (F4981). | The Display Treasury Alerts - Payment view displays, with Issue Message for Payment. |  |
| 7 | Select Display Treasury Alerts Tiles with Correspondence | Open Display Treasury Alerts - Correspondence (F4983). | The Display Treasury Alerts - Correspondence view displays, with Issue Message for Correspondence. |  |
| 8 | Select Display Treasury Alerts Tiles with Interest Rates | Open Display Treasury Alerts - Interest Rates (F4982). | The Display Treasury Alerts - Interest Rates view displays, with Issue Message for Interest Rates. |  |

#### Display Payment Schedule

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the payment schedule for interest flows due.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Payment Schedules (TJ04). | The Treasury: Payment Schedule view displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Execute:OTC Transactions: SelectedCompany Code: for example, 3310End of Term in the Future: SelectedEnd of Term Lapsed: SelectedPayment Period: for example, <Current Date> to <Current Date + 5 days>Payment Status: for example, 1Output Error Log: Selected | You can check the payment schedule report. |  |

#### Analyze NPV

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you calculate and display the Net Present Value (NPV) result.

|  |
| --- |
| Note The Net Present Value (NPV) caculcation doesn’t support swaption right now. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Analyze NPV (JBRX). | The NPV Analysis: Display of Single Values view displays. |  |
| 3 | Enter Selection Criteria of Gen. Selection | Make the following entries:Evaluation Currency: for example, AEDEvaluation Type: for example, Y001Evaluation Date: for example, <Current Date>Horizon: for example, <End Date of Current Month>Portfolio Hierarchy: for example, 100 | Note The system calculates the net present value for the horizon date, but selects the transaction data and market data for the evaluation date. |  |
| 4 | Enter Selection Criteria of Characteristics | Choose the Characteristics tab. |  |  |
| 5 | Enter Selection Criteria of Characteristics | Make the following entries and choose Execute:Company Code: for example, 3310 | The NPV result displays based on portfolio hierarchy. |  |

#### Calculate Market Risk Key Figures

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use this function to calculate and display online the key figures for Net Present Value (NPV) analysis and sensitivity key figures for a selection of transactions. You use the calculated key figures for defining formula-based key figures and display them with the NPV and sensitivity key figures.

|  |
| --- |
| Note This function doesn’t support swaption right now. |

Prerequisite

The Report Layout for the key figure must be maintained. For more information, see the Defining Report Layout for Calculate Market Risk Key Figures procedure under the Market Risk Analyzer topic in the Appendix.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Calculate Market Risk Key Figures (AISGENKF). | The Calculate Market Risk Key Figures view displays. |  |
| 3 | Enter Selection Criteria of Gen. Selection | Make the following entries:Evaluation Currency: for example, AEDEvaluation Type: for example, Y001Evaluation Date: for example, <Current Date>Horizon: for example, <Current Date>Report Layout: for example, Y01 or other Report Layout you createdPortfolio Hierarchy: for example, 100 | Note The system calculates the net present value as on the horizon date, but selects the transaction data and market data for the evaluation date. |  |
| 4 | Enter Selection Criteria | Choose the Characteristic tab. |  |  |
| 5 | Enter Selection Criteria | Make the following entries and choose Execute:Company Code: for example, 3310Product Type: for example, 62A | The Single Value Analysis for Report Layout view displays the NPV result based on portfolio hierarchy. |  |

#### Sensitivity Key Figures

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you check sensitivity key figures.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Sensitivity Key Figures - Single Analysis (AISS) | The Sensitivity Key Figures view displays. |  |
| 3 | Enter Selection Criteria of Gen. Selection | Make the following entries:Display Currency: for example, AEDEvaluation Type: for example, Y001Evaluation Date: for example, <Current Date>Horizon: for example, <End Date of Current Month>Portfolio Hierarchy: for example, 100 | Note The system calculates the net present value based on the horizon date, but selects the transaction data and market data for the evaluation date. |  |
| 4 | Enter Selection Criteria | Choose the Chars tab. |  |  |
| 5 | Enter Selection Criteria | Make the following entries and choose Execute:Company Code: for example, 3310 | The sensitivity key figures display based on portfolio hierarchy. |  |

#### Review Limit Utilization Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you review the limit utilization report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Review Limit Utilizations (TBLB). | The Overview of Utilizations - Selection Using all Characteristics view displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Execute:Limit type: for example, Y01Limit Utilization Base: for example, 1Determination Date: for example, <Current Date>Limits Valid From: for example, <Current Date> | The system displays an overview of the limit utilizations with your selection criteria. |  |

#### Review Interest Rate Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this report, you can get an overview of interest rates levels for multiple currencies across different tenors, as well as the corresponding yield curves.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Interest Rate Overview (F3098). | The Interest Rate Overview screen displays. |  |
| 3 | Navigate Interest Rate Overview | On the Interest Rate Overview screen, enter the following data and choose Go:Key Date: for example, TodayReference Date: for example, First Day in This MonthDisplay Currency: for example, AEDExchange Rate Type: for example, MNumber of Years: for example, 5Yield Curve Type: for example, 0001 | Multiple cards are displayed, such as Net Changes in Reference Interest Rate, Reference Interest Rate: Table View, Yield Curves, etc.Check the IR Swaps Nominal Amount in Disp.Crcy in IR Swaps by Key Date card. |  |

## Appendix

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

#### Send Correspondence

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a background job to send correspondence objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Treasury Back Office Jobs (F2771). | The Application Jobs screen displays. |  |
| 3 | Create New Job | On the Application Jobs screen, choose Create. | The Template Selection area is displayed. |  |
| 4 | Enter General Information for New Job | In the Template Selection area, enter the following data, and choose Step 2:Job Template: <Send Correspondence>Job Name: for example, <Send Correspondence> | You've chosen the job template and are navigated to the Scheduling Options area. |  |
| 5 | Enter Scheduling Options for New Job | In the Scheduling Options subarea, choose Define Recurrence Pattern, and enter the following data in the Scheduling Information dialog box:Start Immediately: <deselect this checkbox>Job Start: for example, <current date 09:00:00>Time Zone: <choose a time zone>Recurrence Pattern: for example, DailyEvery: for example, 1 Day(s)End: for example, After 7 Occurrence(s)On Non-Working Day: Run on next Working DayChoose OK, and choose Step 3.Note If you would like to start job at once, select checkbox Start Immediately. | You've defined the time recurrence pattern and are navigated to the Parameters area. |  |
| 6 | Enter Parameters for New Job | In the Correspondence subarea, enter the following data:Company Code: for example, 3310Correspondence Key: <enter correspondence keys if you'd like to limit correspondence objects>Message Status: for example, InitiatedProfile: for example, PR_EMAILRecipient Type: for example, COUNTERPARTYCorrespondence Class: for example, enter DEAL_DER, DEAL_FX, DEAL_MMDirection: for example, OutgoingIn the Deal subarea, enter the following data:Transaction Number: <enter transaction numbers if you'd like to limit transactions>Product Type: <enter product types if you'd like to limit product types>Transaction Type: <enter transaction types if you'd like to limit transaction types>Business Partner: <enter business partners if you'd like to limit business partners> | The New Job: Send Correspondence view displays. |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Check Result | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details screen is displayed. |  |

#### Adjust Interest Rate

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a background job to adjust interest rate automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Schedule Treasury Back Office Jobs (F2771). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | On the Application Jobs screen, choose Create. | The New Job screen is displayed. |  |
| 4 | Enter General Information for New Job | In the Template Selection area, enter the following data, and choose Step 2:Job Template: <Run Automatic Adjustment - Interest Rate/Price>Job Name: for example, <Run Automatic Adjustment - Interest Rate/Price> | You've chosen the template and are navigated to the Scheduling Options area. |  |
| 5 | Enter Scheduling Options for New Job | In the Scheduling Options area, choose Define Recurrence Pattern, and enter the following data in the Scheduling Information dialog box:Start Immediately: <deselect this checkbox>Job Start: for example, <current date 09:00:00>Time Zone: <choose a time zone>Recurrence Pattern: for example, DailyEvery: for example, 1 Day(s)End: for example, After 7 Occurrence(s)On Non-Working Day: Run on next Working DayChoose OK, and choose Step 3Note If you would like to start job at once, select Start Immediately. | You've defined the time recurrence pattern and are navigated to the Parameters area. |  |
| 6 | Enter Parameters for New Job | In the Parameters area, enter the following data:Interest Rate Adjustment: <select>Company Code: for example, 3310Product Type: for example, <select proper product types>In the Specific Reference Interest Rate subarea, enter the following data:Reference Interest Rate: for example, AEDM03EIBIn the Specific Transactions subarea, enter the following data:All Transactions: <select this checkbox>In the Control Parameters subarea, enter the following data:Test Run: <deselect this checkbox>Display Errors Only: <deselect this checkbox>Save Log: <select this checkbox> |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Check Result | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details screen is displayed. |  |

#### Update Planned Records

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can update planned records that are relevant for your interest rate derivatives transactions, to update the future interest payments transferred to Cash Management so that the liquidity status is correct and up to date.

Prerequisite

You have updated the reference interest rate value and currency exchange rates tables.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Treasury Back Office Jobs (F2771). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | On the Application Jobs view, choose Create. | The Template Selection area is displayed. |  |
| 4 | Enter General Information | In the Template Selection area, enter the following data, and choose Step 2:Job Template: Update Planned RecordsJob Name: for example, Update Planned Records | You've chosen the template and are navigated to the Scheduling Options area. |  |
| 5 | Enter Scheduling Options | In the Scheduling Options area, enter the following data and choose Step 3:Start Immediately: for example, <select this checkbox>Job Start (Local Time): for example, <the current date and time> | You've defined the scheduling option and are navigated to the Parameters area. |  |
| 6 | Enter Parameters | In the Parameters area,In the Kind of Adjustment subarea, select the Interest Rate Adjustment radio button.In the General Selection subarea, enter the following data:Company Code: for example, 3310Update All Planned Records: for example, <select the radio button>Reference Interest Rate: for example, <enter the reference interest rate adopted by the transactions>Transaction: <enter transaction numbers if you'd like to limit transactions>Note You can also select by Product Types.Test Run: <deselect this checkbox> |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Review Results | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details view displays. |  |
| 9 | Repeat to Adjust Exchange Rate | In case of a cross currency swap, you can also adjust the exchange rate adopted by the future cash payments, by selecting the Foreign Exch. Rate Adjustment radio button in the Kind of Adjustment subarea. | The cash flows are updated by the latest exchange rate. |  |

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

#### Run Accrual

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you schedule a background job to accrue interest expenses and interest income based on existing financial instruments.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Treasury Accountant Jobs (F2770). | The Application Jobs view is displayed. |  |
| 3 | Create New Job | Choose Create. | The New Job screen is displayed. |  |
| 4 | Enter General Information for New Job | In the Template Selection area, enter the following data, and choose Step 2:Job Template: Run Accrual/DeferralJob Name: for example, Run Accrual/Deferral | You've chosen the template and are navigated to the Scheduling Options area. |  |
| 5 | Enter Scheduling Options for New Job | In the Scheduling Options area, enter the following data, and choose Step 3:Start Immediately: <deselect this checkbox>Start: for example, <first day of next month of this year at time 01:00> | You've defined the scheduling option and are navigated to the Parameters area. |  |
| 6 | Enter Parameters for New Job | In the Parameters area, enter the following data:In the Product Groups sub-area, select a product group, for example, select the OTC Transactions checkbox.In the General Selections sub-area,Company Code: for example, 3310Valuation Area: for example, AE0,or leave it blank (run for all valuation areas)Product Type: <enter product types if you'd like to limit product types>Transaction: <enter transaction numbers if you'd like to limit transactions>In the Selection Parameters sub-area, enter the following data:Accrual/Deferral Key Date: for example, <last day of current month>Including Key Date: for example, <select this checkbox>Test Run: <deselect this checkbox>In the Posting Control sub-area, make the following selection:Immediate Posting: <select this checkbox> |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Check Result | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details screen is displayed. |  |

#### Calculate Fair Value of Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you schedule a background job to calculate fair values using Net Present Values (NPV) of the financial transactions.

Prerequisite

Before scheduling the background job, ensure that relevant market data (that is, interest rates, foreign exchange rates, credit spreads, and so on) are maintained for the evaluation date. For more details about market data maintenance, see the Market Rates Management – Manually via Upload(1XN) test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Treasury Back Office Jobs (F2771). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | Choose Create. | The New Job screen is displayed. |  |
| 4 | Enter General Information | In the Template Selection area, enter the following data, and choose Step 2:Job Template: Calculate Net Present Value - With CVA and DVAJob Name: for example, Calculate Net Present Value - With CVA and DVA | You've chosen the template and are navigated to the Scheduling Options area in the New Job: Calculate Net Present Value - With CVA and DVA view. |  |
| 5 | Enter Scheduling Options | In the Scheduling Options area, enter the following entries, and choose Step 3:Start Immediately: <deselect>Start: for example, <first day of next month for this year at time 02:00> | You've defined the scheduling option and navigated to the Parameters area. |  |
| 6 | Enter Parameters for New Job | In the Parameters area, enter the following data:In the Selection Mode sub-area,Evaluation Parameter Derivatn: <do not select this checkbox>Select OTC Transactions: <select>Market Value Decomposition: <do not select this checkbox>In the Common Selection Criteria sub-area, enter the following data:Company Code: for example 3310In the Single OTC Transaction Selection Criteria sub-area, enter the following data:Product Type: <enter product types if you'd like to limit product types>Transaction: <enter transaction numbers if you'd like to limit transactions>In the Evaluation Parameters sub-area, enter the following data:Evaluation Date (Dynamic): for example <last date of current month>CVD/DVA Type: To calculate risk-free NPV, leave blank. To calculate risk-based NPV and CVA/DVA, enter Y01Evaluation Type: To calculate risk-free NPV, enter Y001. To calculate risk-based NPV and CVA/DVA, enter Y002In the Save Results sub-area, enter the following data:Test Run: <deselect this checkbox>Price/NPV Type: 001Save Values with Warnings: <select>Detail Log: <select> |  |  |
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

#### Post Realized Profit and Loss

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you schedule a background job to fix and post derived business transactions (usually for realized profit and loss when deal is mature).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Schedule Treasury Accountant Jobs (F2770). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | Choose Create. | The Template Selection area is displayed. |  |
| 4 | Enter General Information | In the Template Selection area, enter the following data, and choose Step 2:Job Template: Post Derived Business TransactionsJob Name: for example, Post Derived Business Transactions |  |  |
| 5 | Enter Scheduling Options | In the Scheduling Options area, enter the following data, and choose Step 3:Start Immediately: <select this checkbox>Note You can define recurrence pattern by choosing Define Recurrence Pattern, if you don't want to start the job immediately. | You've defined the scheduling option and are navigated to the Parameters area |  |
| 6 | Enter Parameters for New Job | In the Parameters areas, enter the following data:Company Code: for example 3310Valuation Area: for example, AE0,or leave it blank (run for all valuation areas)In the OTC Transactions sub-area, enter the following data:OTC Transactions: <enter transaction numbers if you'd like to limit transactions>In the Selections for Fixing Derived Business Transactions sub-area, enter the following data:TRL Date: for example, <current date>In the Posting Control subarea, make the following selection:Test Run: <deselect this checkbox> |  |  |
| 7 | Schedule the New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
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

Table 6: Determination Steps

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

### Accounting

Purpose

This section described accounting-relevant activities that are not described in the Test Procedures.

#### Reverse Accrual

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure allows you to reverse accruals posted for the deal.

For example, if you executed the accrual on an incorrect date, you would reverse it.

Prerequisite

The accrual of the deal is posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Reverse Accrual/Deferral (TPM45). | The Reverse Accrual/Deferral of Expenses and Revenues view displays. |  |
| 3 | Test Run | Enter the following data and choose Execute.OTC Transactions: SelectedCompany Code: for example, 3310Valuation Area: <leave blank or enter specific valuation area, for example, AE0>Transaction: <transaction numbers for executed accruals>Accrual/Deferral Key Date: for example, <date to reverse accrual>Test Run: SelectedReasons for Reversal: for example, 04 Other reasonsImmediate Posting: Selected | The Reverse Accrual/Deferral of Expenses and Revenues view displays.Choose Logs and Messages. The simulated reversal posting information is shown. No posting is created because it is a test run. |  |
| 4 | Production Run | Choose Back until you return to the initial view of this app.Change the following data and choose Execute.Test Run: Deselected | The Execute Accrual/Deferral of Expenses and Revenues view displays.Choose Logs and Messages. The posting information for reversal is shown. An accounting document is created. |  |

#### Reverse Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step allows you to reverse the posted period-end valuation for the deal.

For example, you would want to reverse the valuation if you performed it with incorrect currency rates or incorrect evaluation type. This would lead to wrong accounting results that require reversal.

Prerequisite

The period end valuation of the deal is posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Reverse Valuation (TPM2). | The Reverse Valuation view displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Transactions: SelectedCompany Code: for example, 3310Valuation Area: <leave blank or enter specific valuation area, for example, AE0>Transaction: transaction numbers for valuation to reverseKey Date for Valuation: <Date for reversal>Reasons for Reversal: for example, 04 Other reasonsTest Run: Selected | The Display Positions to be Reversed view displays. |  |
| 4 | Reverse Valuation for Test Run | Choose Reverse Valuation (TPM2). | The Reversal Log: Reversed Business Transactions view displays the message Valuation (test run) has been successfully reversed.You can check the simulated reversal posting information on this view. No posting is created because it is a test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until you return to the initial view of this app.Change the following data and choose Execute:Test Run: Deselected | The Display Positions to be Reversed view displays. |  |
| 6 | Reverse Valuation for Production Run | Choose Reverse Valuation (TPM2). | The Reversal Log: Reversed Business Transactions view displays the message Valuation has been successfully reversed.You can check the posting in this view. An accounting document for reversal is created. |  |

#### Account Assignment Reference Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An account assignment reference is assigned to each position. In this activity, you transfer positions with their book value from one account assignment reference to another (a transfer of the financial positions to the G/L accounts).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Transfer Account Assignment Reference (TPM28). | The Execute Account Assignment Reference Transfer view displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Trans.: <selected>Company Code: 3310Valuation Area: <leave blank or enter specific valuation area, for example, AE0>Transaction: transaction numbers for account assignment references to transferPosting Date: <Date to transfer account assignment reference>New Acct Assignment Ref.: <New account assignment reference>Test Run: <selected> | The Display Positions to be Transferred view displays. |  |
| 4 | Execute Transfer for Test Run | Choose Carry out transfer posting. | The Posting Log: Posted Business Transactions view displays the message Transfer posting (in test run) was successful.The simulated postings for account assignment reference transfer are shown. No posting is created because it is a test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until you return to the initial view of this app.Change the following data and choose Execute:Test Run: <deselected> | The Display Positions to be Transferred view displays. |  |
| 6 | Execute Transfer for Production Run | Choose Carry out transfer posting. | The Posting Log: Posted Business Transactions view displays the message Transfer posting was successful.The postings for account assignment reference transfer are shown. Accounting documents are created. |  |

#### Reverse Account Assignment Reference Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you reverse the account assignment reference transfer after the transfer is updated.

Prerequisite

The account assignment reference transfer is posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Reverse Account Assignment Reference Transfer (TPM29). | The Reverse Account Assignment Reference Transfer view displays. |  |
| 3 | Enter Selection Criteria for Test Run | Make the following entries and choose Execute:OTC Transactions: <selected>Company Code: 3310Valuation Area: <leave blank>Transaction: transaction numbers for account assignment reference transfers to reverseReasons for Reversal: for example, 04 Other reasonsTest Run: <selected> | The Display Positions to be Reversed view displays. |  |
| 4 | Reverse Transfer for Test Run | Select the items to be reversed and choose Cancel transfer. | The Reversal Log: Reversed Business Transactions view displays the message Transfers reversed successfully (test run).The simulated postings for reversal of account assignment reference transfer are displayed. No posting is created because it is a test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until you return to the initial view of this app.Change the following data and choose Execute:Test Run: <deselected> | The Display Positions to be Reversed view displays. |  |
| 6 | Reverse Transfer for Production Run | Select the items to be reversed and choose Cancel transfer. | The Reversal Log: Reversed Business Transactions view displays the message Transfers reversed successfully.The postings for reversal of account assignment reference transfer are shown. Accounting documents are created. |  |

### Interest Rate Adjustment

#### Change Adjustment (Interest Rates/Prices)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you change the adjustment of the interest rate.

Prerequisite

The adjustment of interest rate is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Change Adjustment - Rates/Prices (TI11). | The Change Last Interest/Price Adjustment view displays. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Enter:Company Code: for example, 3310Transaction: transaction number with Adjust Interest Rate created in previous steps | The Change Interest Rate/Price Adjustment view displays. |  |
| 4 | Enter New Interest Rate | Enter the following data and choose Save:Interest Rate: for example, 3 | The manual rate/price adjustment is changed. |  |

#### Display Adjustment (Interest Rates/Prices)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the adjustment of the interest rate.

Prerequisite

You have adjusted the rate or price.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Adjustment - Rates/Prices (TI12). | The Display Rate/Price Adjustment screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data, and choose Enter:Company Code: for example, 3310Transaction: <the transaction number you noted down in the Adjust Interest Rate step> |  |  |

#### Reverse Automatic Adjustmests (Interest Rates/Prices)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you reverse the automatic adjustment of the interest rate.

Prerequisites

The automatic adjustment of interest rate is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Reverse Automatic Adjustments - Rates/Prices (TJ05_REV) | The Reverse Automatic Interest Rate or Price Adjustment view displays. |  |
| 3 | Enter Reverse Criteria | Enter the following data and choose Execute:Company Code: for example, 3310Fixing Date: for example, Last automatic Adjustment DateTest Run: Deselected | The reverse result displays. |  |

#### Reverse Adjustment (Interest Rates/Prices)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you reverse the manual adjustment of the interest rate.

Prerequisite

The manual adjustment of interest rate is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Reverse Adjustment - Rates/Prices (TI37). | The Reverse Last Interest/Price Adjustment view displays. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Enter:Company Code: 3310Transaction: Transaction number with Adjust Interest Rate created in previous steps | The Reverse Last Interest/Price Adjustment view displays. |  |
| 4 | Reverse Interest Rate Adjustment | Choose Save. | The manual rate/price adjustment is reversed. |  |

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

In this activity, you create market data shifts to analyze key figures with modified market data. This is used in the Defining Report Layout for Calculate Market Risk Key Figures step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Market Data Shift (JBR0). | The Edit Market Data Shifts view displays. |  |
| 3 | Enter Market Data Shifts Name | Enter the following data and choose Create:Market Data Shift: for example, 1 | The Define Market Data Shifts view displays. |  |
| 4 | Define Market Data Shift | Enter the following data and choose the Yield Curves tab:Short Name: for example, Market Data Shift 0001 |  |  |
| 5 | Maintain Yield Curves of Market Data Shift | Choose Insert Row.Enter the following data and choose Save:Short Name: for example, Euro Depo ShiftCurrency: for example, AEDYC. Type: for example, 0001Ref.Int.Rate: for example, EURM01EURPercentage: for example, 2 | The Market Data Shift is saved. |  |

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

In this activity, you display the limit overview.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Limit Overview (TBL3). | The Overview of Limits view displays. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Execute:Limit Type: for example, Y01 to Y09Company Code: for example, 3310 | The Display Limits for Limit Types: Overview view displays. |  |

### Change Counterparty

#### Change Counterparty of Financial Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you change the counterparty of financial transactions.

Prerequisite

Ensure that the 33537001 partner is created. For more information, see the Create Business Partner for Treasury and Risk Management - MDS (22G) master data script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Change Counterparty - Financial Transaction (TRTM_CHG_PARTNER). | The Change Counterparty of a Financial Transaction view displays. |  |
| 3 | Test Run | Make the following entries and choose Execute:Company Code: for example, 3310New Partner: for example, 33537001Change Effective From: enter the date from which the change will be effective. For example, current dateTest Run: Selected | The Change Counterparty of a Financial Transaction view displays with Test Run: List of Successfully Changed Financial TransactionsNote If the period specified included a non-working day, a message displays indicating that. |  |
| 4 | Production Run | Choose Exit.Make the following entries and choose Execute:Test Run: Deselected | The Change Counterparty of a Financial Transaction view displays with List of Successfully Changed Financial Transactions. |  |

#### Display Financial Transactions with Changed Counterparty

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the list of financial transactions for the changed counterparty.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Transactions - Changed Counterparty (TRTM_CHG_PARTNER_DIS). | The Display Financial Transactions With Changed Counterparty view displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Execute:Company Code: 3310 | The Display Financial Transactions With Changed Counterparty view displays a list of financial transactions with changed partner. |  |

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

You have created and settled an interest rate swap or cross currency swap.

NPV values need to be stored in advance of the valuation of Treasury positions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Simulate Period-End Closing (TPM_SIM_VAL). | The Simulate Period-End Closing screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Simulate Period-End Closing screen, enter the following data and choose Execute:Securities: <deselect this checkbox>OTC Transactions: <select this checkbox>Company Code: for example, 3310Valuation Area: for example, AE0Product Type: for example, 62ATransaction Number: for example, <the transaction number created in the previous steps>Recalculate Outdated Sim. Res.: <deselect this checkbox>Note If you set this indicator, you can recalculate the outdated simulation results.Simulation Date: for example, <the current date>Key Date Valuation: <select this checkbox>Accrual/Deferral: <deselect this checkbox>Note If you set this indicator, the accrual/deferral of expenses and revenues for the selected treasury positions is simulated, and Accrual/Deferral Parameter is displayed.Test Run: <select this checkbox> | The following message is displayed:Processed xx positions; xx successful, 0 failed.If Recalculate Outdated Simulation Results has been executed, the following message is displayed:xx simulated results deleted for key date, Processed xx positions; xx successful, 0 failed. |  |
| 4 | Execute Simulated Valuation | The dialog Message shows up, and choose Continue. | The screen Simulate Period-End Closing is displayed.You can check the simulated valuation information for local GAAP (valuation area AE0).Note that there is no simulated valuation created because it is test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back to the initial screen of this app.On the initial screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The Messages dialog box is displayed. |  |
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
| 3 | Enter Selection Criteria for Test Run | On the Delete Results of Simulated Period-End Closing screen, enter the following data and choose Execute:Securities: <deselect this checkbox>OTC Transactions: <select this checkbox>Company Code: for example, 3310Valuation Area: leave bank, or enter specific valuation are, for example, AE0Product Type: for example,62ATransaction: for example, <the transaction number created in the previous steps>Simulation Date: for example, <the date on which the reversal should takes place>Test Run: <select this checkbox> | The following message is displayed:xx simulated results deleted for key date (the date on which the reversal takes place). |  |
| 4 | Enter Selection Criteria for Production Run | Go back to the initial screen of this app.On the Delete Results of Simulated Period-End Closing screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The following message is displayed:XX simulated results deleted for key date (the date on which the reversal takes place). |  |

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
- related-to :: [[05-treasury-and-cash-management/test-script-interest-rate-derivatives-management-1x3-ae-sap-s-4hana-cl-part-01]]
- related-to :: [[05-treasury-and-cash-management/interest-rate-derivatives-management-group-ledger-ifrs-1xb-ae-test-scr]]
- related-to :: [[05-treasury-and-cash-management/interest-rate-derivatives-management-group-ledger-us-gaap-34e-ae-test]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1X3_S4CLD2608_BPD_EN_AE.docx` — lines 3128–5563 of the extracted text · extracted with `mammoth` · 440,263 chars in the whole document
