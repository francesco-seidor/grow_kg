---
id: 05-treasury-and-cash-management/test-script-debt-and-investment-management-1wv-ae-sap-s-4hana-cloud-pu-part-02
title: "Test Script: Debt and Investment Management (1WV_AE) - SAP S/4HANA Cloud Public Edition (1WV_S4CLD2608_BPD_EN_AE) — part 2 of 2"
description: "Test script 1WV (S/4HANA Cloud 2608, AE), part 2: TRM payment posting, reports, background jobs, output management, reversals, valuation, notifications."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/debt-and-investment-management]
aliases: []
keywords: [Debt and Investment Management, post to general ledger, treasury reports, financial positions, background job scheduling, market risk key figures, value at risk, output management, accrual and valuation reversal, interest rate adjustment]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1WV_S4CLD2608_BPD_EN_AE.docx#lines-3002-4975"]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-773
topic: 05-treasury-and-cash-management/debt-and-investment-management
language: EN
part: 2/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Debt and Investment Management (1WV_AE) - SAP S/4HANA Cloud Public Edition (1WV_S4CLD2608_BPD_EN_AE) — part 2 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1WV_S4CLD2608_BPD_EN_AE.docx`, part 2 of 2 (lines 3002–4975 of the extracted text), extracted with `mammoth`. Grouped under **Debt and Investment Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

If Bank Communication Management (BCM) is not implemented in your system, the payment medium file will be generated upon completion of the payment run in the previous step, provided that the relevant payment method uses the PMW format.

If BCM is implemented in your system, additional approvals may be required for a BCM batch before the payment medium file can be generated. For the approval process, please refer to the section Outgoing Payment with BCM Approval Process in the test script Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/J78)).

After payment medium file is created, there are two ways for sending the payment medium file to your house bank:

- If Multi-Bank Connectivity (MBC) is not enabled, please use app Manage Payment Media (F1868) to check and download the payment medium file, and send the file to the bank via the previously agreed-upon method. Further details are provided in test script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/1EG)).
- If MBC is enabled and the relevant PMW format uses the alternative format type designated for MBC, then the payment medium file can be automatically sent to MBC. Bank will then retrieve the payment medium file from MBC and execute the payment. Further details are provided in test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/16R)).

#### Bank Initiated Payment

Purpose

If the outgoing payment is initiated by bank, it is not necessary to run previous steps Generate Payment Request and Process Payment Request, because the outgoing payment is initiated by bank.

Procedure

This step doesn't require any operation in system.

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

- Fix, Pay and Post Flows (TBB1): you use this app to generate posting for incoming payments. Please note that when using this app in the current step, it will not create posting for the outgoing payment which has been processed in the previous step Generate Payment Request with the Pay Only option.
- Process Business Transactions: You use this app to generate the posting for the outgoing payment which has been processed in the previous step Generate Payment Request with the Pay Only option.

|  |
| --- |
| Note You can also schedule a background job for this step. Please see corresponding step in the Appendix. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Execute:Money Market: <select this checkbox>Company code: for example 3310Transaction: <transaction number with inflow which was created in previous steps>Up to and Including Due Date: enter date on which the flow of financial transaction should be posted, for example, <current date>Test Run: <select this checkbox>Post Operational Only: <select this indicator> | Screen Posting Log: Posted Business Transactions displays, you can check the simulated posting information for local GAAP (valuation area AE0) on this screen, please note there is no posting created because it is test run.If message No flows exist for processing displays, that means there is no posting are needed for your selection criteria, you can skip current test step and continue the test step with app Process Business Transactions. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Execute:Test Run: <deselect this checkbox> | Screen Posting Log: Posted Business Transactions displays, accounting document has been created for incoming payment in local GAAP (valuation area AE0). |  |
| 5 | Access another SAP Fiori App | Open Process Business Transactions (TPM10). | The Process Business Transactions screen displays. |  |
| 6 | Enter Selection Criteria for Test Run | On the Process Business Transactions screen, enter the following data and choose Execute:OTC Transactions: <select this checkbox>Company Code: for example, 3310Valuation Area: for example AE0Limit by Subledger Pos.: <select this checkbox>Under the OTC Transactions screen group:Transaction: <transaction number with outflow, and its payment request has been generated in step Generate Payment Request>Test Run: <select this checkbox> | Screen Test Run: Post/Reverse Business Transactions displays.If message You have not selected any business transactions displays, that means there is no posting are needed for your selection criteria, you can skip current step. |  |
| 7 | Check Test Run Result | On the screen Test Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.Screen Test Run: Display Posted/Reversed Business Transactions displays, choose Log and Messages. | Screen Posting Log: Posted Business Transactions displays, you can check the simulated posting information for local GAAP (valuation area AE0) on this screen. Please note there is no posting created because it is test run. |  |
| 8 | Enter Selection Criteria for Production Run | Choose Back.On the Process Business Transactions screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | Screen Update Run: Post/Reverse Business Transactions displays. |  |
| 9 | Production Run | On the screen Update Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.Screen Update Run: Display Posted/Reversed Business Transactions displays, choose Log and Messages. | Screen Posting Log: Posted Business Transactions displays, accounting document has been created for outgoing payment in local GAAP (valuation area AE0). |  |

#### Post Realized Profit and Loss

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you fix and post derived business transactions (usually it is realized profit and loss when a deal is mature) if there is.

|  |
| --- |
| Note You can also schedule a background job for this step. Please see corresponding step in the Appendix. |

Prerequisite

The maturity date of the transaction has been reached, and the financial transaction has been created, settled, and posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Post Derived Business Transactions (TPM18). | The Fix and Post Derived Business Transactions screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Fix and Post Derived Business Transactions screen, enter the following data and choose Execute:OTC Transactions: <select this checkbox>Company code: for example, 3310Valuation Area: for example AE0OTC Transactions: <transaction number(s) which are mature>TRL Date: <maturity date of transaction>Test Run: <select this checkbox>Confirm the Are you sure that you want to select future business transactions message by choosing Enter. | New screen Fix and Post Derived Business Transactions displays.If No scheduled derived business transactions were found for the selection displays, then there is no derived transaction available for your selection, you can skip the current step. |  |
| 4 | Fix and Post for Test run | On the Fix and Post Derived Business Transactions screen, choose Fix. | New screen Posting Log: Posted Business Transactions displays, you can see the simulated posting information for local GAAP (valuation area AE0), please note there is no posting created because it is test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until the initial screen of this app, change the following data and choose Execute:Test Run: <deselect this checkbox>Confirm the message Are you sure that you want to select future business transactions by choosing Enter | New screen Fix and Post Derived Business Transactions displays. |  |
| 6 | Fix and Post for Production run | On the Fix and Post Derived Business Transactions screen, choose Fix. | New screen Posting Log: Posted Business Transactions displays, you can see the posting information for local GAAP (valuation area AE0), this time, accounting document has been created in local GAAP (valuation area AE0). |  |

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

Display posting journals for review.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as aTreasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Posting Journal (F1755). | The Display Treasury Posting Journal (F1755) screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select Go.Product Group: for example, OTC TransactionsCompany Code: for example, 3310 | The posting journals display per the filter values. |  |

#### Treasury Position Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the treasury position analysis report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Treasury Position Analysis (W0049). | The Treasury Position Analysis screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select Go.Key Date: for example, <the current date>Include Planned Data: for example, 1Valuation Area: for example, AE0Company Code: for example, 3310Product Type: for example, <choose the proper product type(s)>Note You can enter multiple product types by pressing Enter in between. | The position analysis data displays per the filter values. |  |

#### Treasury Position History

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the treasury position history.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Treasury Position History (F3966) | The Treasury Position History screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select Go.Key Date: for example, <the current date>Period: for example, <Year to Date>Display Currency: for example, AEDExchange Rate Type: for example, MValuation Area: for example, AE0Company Code: for example, 3310. | The data is displayed per the filter values. |  |

#### Display Treasury Position Values

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the treasury position values.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Position Values (F1867). | The Display Treasury Position Values screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select Go.Key Date: for example, <the current date>Product Group: for example, OTC TransactionsCompany Code: for example, 3310Note You may need to make filters available by adapting filters, for example, enable the Product Group filter in the Position Values filter group. | The position values data is displayed per the filter values. |  |

#### Define Financial Positions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define a set of key figures to be displayed in Financial Status - Book Value and Financial Status - Nominal Amount screens.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Risk Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Define Financial Positions (FTR_FP_DEF). | The "Maintain Financial Position Groups": Change screen displays. |  |
| 3 | Maintain Key Figure Groups | Select New Entries.Enter data for a record of new entry and select Save.Financial Position Group: for example, FPG_MM_A0001Financial Position Group Description: for example, <Bank accounts and Short term invest>Assets/Liabilities: for example, Assets | The data is saved. |  |
| 4 | Maintain Key Figures | Switch to Maintain Financial Positions tab.Enter data and choose Save.Financial Position: for example, FP_MM_A0001Financial Position Description: for example, Bank accountsFinancial Position Group: for example, FPG_MM_A0001Data Source: for example, One Exposure | The data is saved. |  |
| 5 | Maintain Selections | Choose Back to display all financial postions. Select one financial position and select Maintain Selections.House Bank: for example, AEBK1Choose Back and choose Save. | The data is saved. |  |
| 6 | Enter More Data | Enter more financial positions data as below tables. |  |  |

| Financial Position Group | Financial Position Group Description | Assets/Liabilities |
| --- | --- | --- |
| FPG_MM_A0001 | Bank accounts and short term invest. | Assets |
| FPG_MM_A0002 | Long term invest. and other assets | Assets |
| FPG_MM_L0001 | Short term debt | Liabilities |
| FPG_MM_L0002 | Long term debt and other liabilities | Liabilities |

| Financial Position | Financial Position Description | Financial Position Group | Data Source | Maintain Selection |
| --- | --- | --- | --- | --- |
| FP_MM_A0001 | Bank accounts | FPG_MM_A0001 | One exposure | House Bank: for example, AEBK1 |
| FP_MM_A0002 | short term investments | FPG_MM_A0001 | Treasury position management | Product Type = 51A to 55ATransaction Type = 100 to 199Valuation Class = 20 to 29Valuation Area = AE0Posting Status = 2 |
| FP_MM_A0003 | g term investments | FPG_MM_A0002 | Treasury position management | Product Type = 51A to 55ATransaction Type = 100 to 199Valuation Class = 10 to 19Valuation Area = AE0Posting Status = 2 |
| FP_MM_A0004 | Other assets | FPG_MM_A0002 | One document balances | Account Number = 12041000 to 1204199912042000 to 1204299912701000 to 12701999Chart of Account = YCOALedger = 0L |
| FP_MM_L0001 | Short term debt | FPG_MM_L0001 | Treasury position management | Product Type = 51A to 55ATransaction Type = 200 to 299Valuation Class = 20 to 29Valuation Area = AE0Posting Status = 2 |
| FP_MM_L0002 | Long term debt | FPG_MM_L0002 | Treasury position management | Product Type = 51A to 55ATransaction Type = 200 to 299Valuation Class = 10 to 19Valuation Area = AE0Posting Status = 2 |
| FP_MM_L0003 | Other liabilities | FPG_MM_L0002 | One document balances | Account Number = 22541000 to 2254199922542000 to 22542999Chart of Account = YCOALedger = 0L |

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

Refer to [Define Financial Positions](#unique_78) [page ] 148 for more details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Risk Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Financial Status (F2136). | The Financial Status - Book Value screen displays. |  |
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

Refer to [Define Financial Positions](#unique_78) [page ] 148 for more details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Risk Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Financial Status (FTR_FPM_FINANCIAL_STATUS (FTR_FPM_FS_NOMAMT)). | The Financial Status - Nominal Amount screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Go:Key Date: for example, <Current Date>Display Currency: for example, AEDExchange Rate Type: for example, MCompany Code: for example, 3310 | The data displays per the filter values. |  |

#### Display Treasury Payments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can display all payment journals for review.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Payments (TPM20A). | The Payment Journal screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Run.Company Code: for example: 3310Product Type: 51A,53A,54A and 55A | The payment journals display. |  |
| 4 | Review data | Review the data displayed on the screen. You can also choose Original business transaction or Details to drill down for more details. |  |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Position Flows (F1754). | The Display Treasury Position Flows view displays. |  |
| 3 | Enter Selection Criteria | On the Display Treasury Position Flows view, enter following data:Product Group: for example: OTC TransactionsCompany code: for example, 3310and choose Go. | Position Flow data displays according to the filter values. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Treasury Alerts - Posting (F4984). | The Display Treasury Alerts - Posting screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Display Treasury Alerts screen, enter following data, and choose Go:Issue Message For: PostingCompany Code: for example, 3310 | Alerts data is displayed per the filter values. |  |

#### Display Treasury Alerts- Settlement, Release, Payment, Correspondence and Interest Rates

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Treasury Alerts - Settlement (F4979). | The Display Treasury Alerts - Settlement view displays with Issue Message For: Settlement. |  |
| 3 | Enter Selection Criteria | Enter following data, and choose Go:Issue Message For: SettlementCompany Code: for example, 3310 | Alerts data displays per the filter values. |  |
| 4 | Confirm Alerts for Other Transactions | In the following steps, you display treasury alert results by selecting other SAP Fiori apps:ReleasePaymentCorrespondenceInterest Rates |  |  |
| 5 | Select Display Treasury Alerts Tiles with Release | Return to the Home view and open Display Treasury Alerts - Release (F4980). | The Display Treasury Alerts view is displayed, with Issue Message For:Release. |  |
| 6 | Select Display Treasury Alerts Tiles with Payment | Return to the Home view and open Display Treasury Alerts - Payment (F4981). | The Display Treasury Alerts view is displayed, with Issue Message For:Payment. |  |
| 7 | Select Display Treasury Alerts Tiles with Correspondence | Return to the Home view and open Display Treasury Alerts - Correspondence (F4983). | The Display Treasury Alerts view is displayed, with Issue Message For:Correspondence. |  |
| 8 | Select Display Treasury Alerts Tiles with Interest Rates | Return to the Home view and open Display Treasury Alerts - Interest Rates (F4982). | The Display Treasury Alerts view is displayed, with Issue Message For:Interest Rates. |  |

#### Display Payment Schedules

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Payment Schedules (TJ04). | The Treasury: Payment Schedules view displays. |  |
| 3 | Enter Selection Criteria | Enter the following data:OTC Transactions: <select this checkbox>Company code: for example, 3310End of Term in the Future: <select this checkbox>End of Term Lapsed: <select this checkbox>Payment Period: for example, <Current Date to Current Date + 5 days>Payment Status: for example, 1Output Error Log: <select this checkbox>and choose Run. | Review the check payment schedule report. |  |

#### Analyze Net Present Value (NPV)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you calculate and display Net Present Value (NPV) result.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Analyze NPV (JBRX). | The NPV Analysis: Display of Single Values view displays. |  |
| 3 | Enter Selection Criteria of Gen. Selection | Enter the following data:Evaluation Currency: for example, AEDEvaluation Type: for example, Y001Evaluation Date: for example, <Current Date>Horizon: for example, <Current Date>Portfolio Hierarchy: for example, 100 | The system calculates the net present value as on the horizon date, but selects the transaction data and market data for the evaluation date.Note If transaction end date is before evaluation date, there is no output. |  |
| 4 | Enter Selection Criteria of Characteristics | Choose the Characteristics tab and enter the following data, and then choose Run:Company Code: for example, 3310Product Type: for example, <product type of the transaction number you noted down in the previous procedure>and then choose Run. | The NPV Result displays based on the portfolio hierarchy. |  |

#### Calculate Market Risk Key Figures

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you calculate and display the key figures for the Net Present Value (NPV) analysis and the sensitivity key figures for selected transactions. You can use the key figures as the basis for defining formula-based key figures and display them with the NPV and sensitivity key figures.

Prerequisite

Report Layout for key figure should be maintained. For more information, see the [Defining Report Layout for Calculate Market Risk Key Figures](#unique_122) [page ] 212 in the Appendix.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Calculate Market Risk Key Figures (AISGENKF). | The Single Value Analysis for Generic Key Figures view displays. |  |
| 3 | Enter Selection Criteria of Gen. Selection | Enter the following data:Evaluation Currency: for example, AEDEvaluation Type: for example, Y001Evaluation Date: for example, <Current Date>Horizon: for example, <Current Date>Report Layout: for example, <Y01 or any other Report Layout you created>Portfolio Hierarchy: for example, 100 | The system calculates the net present value as on the horizon date, but selects the transaction data and market data for the evaluation date.Note If transaction end date is before/on evaluation date, there is no output. |  |
| 4 | Enter Selection Criteria | Choose the Characteristics tab and enter the following data and then choose Run:Company Code: for example, 3310Product Type: for example, 86A | The Single Value Analysis for the assigned report layout displays. |  |

#### Sensitivity Key Figures

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you process sensitivity key figures.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Sensitivity Key Figures - Single Analysis (AISS). | The Sensitivity Key Figures - Single Analysis (AISS) view displays. |  |
| 3 | Enter Selection Criteria of Gen. Selection | Enter the following data:Display Currency: for example, AEDEvaluation Type: for example, Y001Evaluation Date: for example, <Current Date>Horizon: for example, <End Date of Current Month>Portfolio Hierarchy: for example, 100 | The system calculates the net present value as on the horizon date, but selects the transaction data and market data for the evaluation date.Note If transaction end date is before/on evaluation date, there is no output. |  |
| 4 | Enter Selection Criteria | Choose the Characteristics tab, enter the following data:Company Code: for example, 3310Product Type: for example, 86Aand then choose Run. | The Sensitivity Key Figures - Single Analysis (AISS) report displays based on the portfolio hierarchy. |  |

#### Review Limit Utilization Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to Review Limit Utilization Report.

Prerequisite

The limit master records of your company is maintained in the system.

You successfully completed the processing in the previous test procedure Generate Limit Utilizations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Review Limit Utilizations (TBLB). | The Overview of Utilizations - Selection Using all Characteristics screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data, and choose Run:Limit Type: for example, Y01 or Y07Limit Utilization Base: for example, 1Determination Date: for example, <the current date>Limits Valid From: for example, <the current date> | An overview of the limit utilization in accordance with your selection criteria is displayed. |  |

#### Review Maturity Profile

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to display the Debt and Investment Maturity Profile.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Debt and Investment Maturity Profile (F3130). | The Debt and Investment Maturity Profile (F3130) view displays. |  |
| 3 | Enter Selection Criteria | On the Debt and Investment Maturity Profile (F3130) dialog box, enter the following selection criteria:Key Date: for example, <Current Date>Display Currency: for example, AEDExchange Rate Type: for example, MNumber of Years: for example, 3and select Go. | The profile displays. |  |

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
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Front Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Interest Rate Overview (F3098). | The Interest Rate Overview screen displays. |  |
| 3 | Navigate Interest Rate Overview | On the Interest Rate Overview (F3098) screen, enter the following data and choose Go:Key Date: for example, TodayReference Date: for example, First Day in This MonthDisplay Currency: for example, AEDExchange Rate Type: for example, MNumber of Years: for example, 5Yield Curve Type: for example, 0001 | Multiple cards are displayed, such as Interest Rate, Yield Curves, etc. |  |

#### Debt and Investment Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to process Debt and Investment Analysis.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Debt and Investment Analysis (F3450). | The Adapt Filters dialog box displays. |  |
| 3 | Enter Selection Criteria | Enter the following data:Key Date: for example, <Current Date>Display Currency: for example, AEDExchange Rate Type: for example, MDebt/Investment: for example, Debt/InvestmentInterest Category: for example, Alland choose Go: | The Debt and Investment Analysis (F3450) view displays. |  |

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

In this step, you can update planned records that are relevant for your debt and investment transactions, to update the future interest payments transferred to Cash Management so that the liquidity status is correct and up to date.

Prerequisite

You have updated the reference interest rate value table.

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

#### Generate Cash Flow – Money Market

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you update the planned cash flow by running a background job to regenerate the cash flows.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Treasury Back Office Jobs (F2771). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | On the Application Jobs view, choose Create. | The Template Selection area is displayed. |  |
| 4 | Enter General Information | In the Template Selection area, enter the following data, and choose Step 2:Job Template: Generate Cash Flow - Money MarketJob Name: for example, Generate Cash Flow - Money Market | You've chosen the template and are navigated to the Scheduling Options area. |  |
| 5 | Enter Scheduling Options | In the Scheduling Options area, choose Define Recurrence Pattern, and in the Scheduling Information dialog box, enter the following data:Start Immediately: <deselect this checkbox>Job Start: for example, <the first day of the next month, 12:00:00 AM>Time Zone: <select a time zone or use default>Recurrence Pattern: for example, MonthlyEvery: for example, 1 Month(s)On: for example, Beginning of Month, 1st DayEnd: for example, select After and then enter 12 occurrence(s)On Non-Working Days: for example No RestrictionChoose OK, and choose Step 3.Note If you would rather to start job at once, select Start Immediately checkbox. | You've defined the recurrence pattern and are navigated to the Parameters area. |  |
| 6 | Enter Parameters | In the Parameters area,In the General Selection sub-area, enter the following data:Company Code: for example, 3310Transaction: <enter transaction numbers if you'd like to limit transactions>Note You can also limit transactions through other selections like Product Category, Product Types, etc.In the Further Selections sub-area,Derivation Procedure: <specify if you'd like to limit transactions by derivation procedure>In the Control sub-area,Test Run: <deselect this checkbox> |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Review Results | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details view displays. |  |

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

With SAP S/4HANA a new output management approach is in place. By design, the new output management includes cloud qualities such as extensibility enablement, multi tenancy enablement and modification free configuration. Therefore, the complete configuration differs from the configuration that is used when output management is based on NAST. The configuration is based on BRF+ which is accessible for customers. In SAP S/4 HANA, the target architecture is based on Adobe Document Server and Adobe Forms only. for the form determination rules (along with other output parameters) BRF+ functionality is used (in this sense in combination with the message determination).

For TRM, SAP has redelivered an application object type ‘Treasury and Risk Management’. All the pre-delivered output determination rules are maintained under this application object type. SAP provides several apps with which you can manage your output easily.

#### Output Parameter Determination

Purpose

In this activity, you manage the determination rules for the output. The following determination steps apply to Treasury and Risk Management:

- Output Type

SAP delivers necessary configurations. Don't change this setting.

- Receiver

SAP delivers necessary configurations. Don't change this setting.

- Channel

SAP delivers necessary configurations. Don't change this setting.

- Printer Settings

SAP delivers necessary configurations. You can change this setting.

- Email Recipient

You must maintain email recipients for outgoing correspondence objects in the email channel.

|  |
| --- |
| Caution This setting overwrites the email address for business partner master data. |

- Email Settings

You specify the email template and the sender email address in this procedure. Although SAP delivers email templates, you create your own email templates using the Maintain Email Template SAP Fiori app.

- Form Template

You specify the PDF form template and number of copies in this step. SAP delivers PDF form templates. You create your own form templates using the Maintain Form Template SAP Fiori app.

- Output relevance

SAP has set all output types as output-relevant. Don't change this setting.

The operations to change these settings are similar. This procedure describes the steps to change the email address for recipients and senders as an example.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). | The Output Parameter Determination view displays. |  |
| 3 | Display Email Recipients | Select the following:Show Rules for: select Treasury and Risk Management CorrespondenceDetermination Step: select Email Recipient .Note By default, no email recipients are maintained by SAP. | The default email recipient rule displays. |  |
| 4 | Maintain Email Recipient for Internal Counterparty | On the Maintain Business Rules section, choose Edit.Select the + (Insert New Row) icon and select the following:Output Type: select Direct Value Input from the dropdown list and an Output Type details view displays.Select the overlapping boxes icon in the Output typefield.A Select: Output Type dialog box displays.From the list, locate and select the row with TRM_DEAL_SLIP.The value is added to the initial Output Type details view. Choose OK and the value is added to the next entry.Repeat this step for the additional columns and enter following data:Role : INEmail Type Code: To, CC, or BCCE-Mail Address: <email address of the recipient>Tip Add additional condition columns by choosing Table Settings. For example, add a BusPartner column to maintain different email recipients for different Business Partners. | The internal recipient email address is maintained. |  |
| 5 | Maintain Email Recipient for External Counterparty | To maintain email for an external recipient, select the + (Insert New Row) icon and repeat the previous step using the following data:Output Type: select TRM_TRANSACTION_CONFIRMATION (Transaction Confirmation)Role : INEmail Type Code: To, CC, or BCCE-Mail Address: <email address of recipient> | The external recipient Email address is maintained. |  |
| 6 | Activate | Under the Maintain Business Rules section, choose Activate.On the Confirmation Activation dialog box, choose Yes. | An Objects saved and activated notification displays. The email addresses are saved and activated. |  |
| 7 | Settings for Sender Email Address and Email Template | Under the Select Business Rules section of the view, make the following changes:Determination Step: select Email Settings | The default email settings are displayed. |  |
| 8 | Change Email Settings | On the Maintain Business Rules section, choose Edit, and enter following data:Sender Email column: select Direct Value Input, and enter <email address> and choose OK.Note Use the Maintain Email TemplateSAP Fiori app to create a new email template. | Email settings are changed. |  |
| 9 | Activate | On the Maintain Business Rulessection, choose Activate.On theConfirmation Activation dialog box, choose Yes, | An Objects saved and activated notification appears. Email settings are saved and activated. |  |

#### Manage Output Items

Purpose

Once output correspondence objects are generated, in this activity you track the status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Output Items (F2279) | The Manage Output Items (F2279) view displays. |  |
| 3 | Application Object Type Filter | On the Manage Output Items (F2279) view, choose the overlapping boxes icon in the Application Object Type filter field. | The Application Object Type dialog box displays. |  |
| 4 | Application Object Type Search | On the Application Object Type dialog box, select the overlapping boxes icon in the Appl. Object Type field. | Define Conditions: Appl. Object Type dialog box displays. |  |
| 5 | Select Criteria | Select the overlapping boxes icon in the Appl. Object Type field, and enter the following:In the first field: select Appl.Object TypeIn the second field: select containsIn the third field: enter TRMand choose OK to close dialog box. | You return to the Application Object Type dialog box. |  |
| 6 | Confirm Search Criteria | On the Application Object Type dialog box, choose Go.The dialog box returns the values:TRM_CORRESPONDENCE Treasury and Risk Management CorrespondenceSelect the checkbox for the row and choose OK | You return to the Manage Output Items (F2279) view. |  |
| 7 | Repeat | Repeat the previous steps to add your transaction number as a filter in Application Object ID.Choose Go.Note When you enter the data in the input field, an input help automatically displays the possible entries for you. You can choose from the list instead of enter the whole words. |  |  |
| 8 | Review | Correspondence objects have following status:In PreparationCompletedIn pendingErrorIf you want to check the detailed log, select the correspondence object and choose Show Application Log.If you want to resend a correspondence object even it has Completed status, select the correspondence object and choose Resend. | The status of the output correspondence objects is listed. You can search for your transaction and check the status. |  |

#### Maintain Print Queues

Purpose

In this activity, you review the outgoing correspondence objects in the PRINT channel .

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Maintain Print Queues (F1260) | The Maintain Print Queues (F1260) view displays. |  |
| 3 | Display the Status of the TRM Print Queue | Locate the TRM print queue and choose the TRM_DEFAULT Print Queue to display.Locate the transaction number you created in the previous procedure and select the line for that transaction number and a PDF file downloads.Note By default, SAP provides following print queue: TRM_DEFAULT | All the TRM outgoing correspondence objects in channel PRINT are displayed with latest status. |  |

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

Purpose

In this activity, you create your own email templates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Maintain Email Templates - Deprecated (F1306) | The Maintain Email Template view displays. |  |
| 3 | Copy a Predelivered Email Template | Choose Predelivered, which results in the display of all the predelivered email templates.Locate an email template to copy, for example, FTR_CORR_EMAIL_TEMPLATE_CNFSelect the checkbox and choose Copy. A Copy Template FTR_CORR_EMAIL_TEMPLATE_CNF dialog box displays.Enter following data:Name: for example, TRM Transaction Confirmation Customer Email TemplateNote Your email template must have YY1_ as the prefix for the technical name. | A Template has been copied notification displays. |  |
| 4 | Modify the Email Template | On the Maintain Email Templates - Deprecated (F1306) view, scroll and locate an email template, for example, YY1_FTR_CORR_EMAIL_TEMPLATE_CN. Select that template and the name of the template displays on the view.Choose Change Details and the Change Template YY1_FTR_CORR_EMAIL_TEMPLATE_CN dialog box displays.Enter following data:Description: TRM Transaction Confirmation Customer Email TemplateChoose Change Details to close the dialog box.On the Email Template view, in the Available Languages subarea, choose a language version, for example, English, by selecting the line.On the Email Template Content view, enter your modifications for the email subject and email body.Choose Save.Note SAP provides predefined variables for your use in email templates. Choosing Show Data Fields displays the variables list. | You successfully modified an email template. |  |

#### Maintain Form Templates

Purpose

In this activity, you create your own form templates.

Prerequisites

Adobe LiveCycle Designer has been installed to edit the form templates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Maintain Form Templates (F1434) | The Maintain Form Templates (F1434) view displays. |  |
| 3 | Download a Predelivered Form template | Choose Predelivered, which results in the display of all of the predelivered form templates.Locate a form template, for example, FDP_TRM_CONF_DE,and select to view the details of this form.Choose download, and a Download Language dialog box displays. Choose OK. | The form template is downloaded successfully. |  |
| 4 | Change the customer Form template file | Open the form using Adobe LiveCycle Designer to make your adjustments and then save the form template. |  |  |
| 5 | Upload the customer Form template file | Open Maintain Form Templates (F1434) and choose Customer Templates. Choose New and a Create Form Template dialog box displays. Enter following data:Form Template Name: for example, CUST_TRM_CONF_DELanguage: for example, EnglishSelect Form Template File: choose Browse and choose your modified file from its location.Data Provider: for example, FDP_TR_CORR_SRVForm Type: ContentChoose OK. | The your customized form template is created successfully. |  |

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

The accrual of the deal has been posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Reverse Accrual/Deferral (TPM45). | The Reverse Accrual/Deferral of Expenses and Revenues screen displays. |  |
| 3 | Test Run | On the Reverse Accrual/Deferral of Expenses and Revenues screen, enter the following data and choose Execute:OTC Transactions: <select this checkbox>Company code: for example, 3310Valuation Area: leave bank, or enter specific valuation are, for example AE0Transaction: <transaction number(s) for which accrual has been executed>Accrual/Deferral Key Date: for example, <date on which the reversal of accrual should take place>Test Run: <select this checkbox>Reasons for Reversal: for example, 04 Other reasonsImmediate Posting: <select this checkbox>Choose Logs and Messages. You can see the simulated reversal posting information. Please note there is no posting created because it is test run. | New screen Reverse Accrual/Deferral of Expenses and Revenues displays. |  |
| 4 | Production Run | Choose Back until the initial screen of this app, change the following data and choose Execute:Test Run: <unselect this checkbox>Choose Logs and Messages. You can see the posting information for reversal. This time, accounting document is created. | New screen Execute Accrual/Deferral of Expenses and Revenues displays. |  |

#### Reverse Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you reverse posted period end valuation for the deal.

For example, when you have finished the period-end valuation with an incorrect currency rate or an incorrect evaluation type. In this activity, you reverse the valuation to prevent incorrect accounting results.

Prerequisite

The period end valuation of the deal has been posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Reverse Valuation (TPM2). | The Reverse Valuation (TPM2) view displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data:OTC Transactions: select this checkboxCompany code: for example, 3310Valuation Area: leave blank or enter a specific valuation area, for example AE0Transaction: <transaction numbers of valuations to be reversed>Key Date for Valuation: for example, < reversal date>Reasons for Reversal: for example, 04 Other reasonsTest Run: select this checkboxand choose Execute. | The Display Positions to be Reversed view displays. |  |
| 4 | Reverse Valuation for Test Run | Choose Reverse Valuation (TPM2). | The Reversal Log: Reversed Business Transactions view displays.A Valuation (test run) has been successfully reversed notification displays.You review the simulated reversal posting information on this view.Note No posting creates during a test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back to return to the initial view of this app.Make the following changes:Test Run: unselect this checkboxand choose Execute. | The Display Positions to be Reversed view displays. |  |
| 6 | Reverse Valuation for Production Run | On the Display Positions to be Reversed view, choose Reverse Valuation (TPM2). | The Reversal Log: Reversed Business Transactions view displaysA Valuation has been successfully reversed notification displays.You review the posting on this view.With this operation, the accounting document for reversal creates. |  |

#### Reversal Valuation Class Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you reverse a valuation class transfer.

For example, when you choose a deal to be incorrectly reclassified from long term to short term, in this activity, you reverse that reclassification.

Prerequisite

The valuation class transfer of the deal has been posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Reverse Valuation Class Transfer (TPM16M). | The Reversal of Valuation Class Transfer view displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data:OTC Transactions: select this checkboxCompany code: for example, 3310Transaction: <transactions for the valuation class transfer to be reversed>Key Date: for example, <date for the valuation class transfer>Reasons for Reversal: for example, 04 Other reasonsTest Run: select this checkboxand choose Execute. | The Edit Selected Positions view displays. |  |
| 4 | Execute Test Run and Check Result | On the Edit Selected Positions view, select the transactions you want to reverse, and choose Execute. | The Test Run: Reverse Transfer view displays, |  |
| 5 | Review Log | Choose Messages and Log.On the Information Overview dialog box , choose Reversal Log. | The Reversal Log: Reversed Business Transactions view displays.Review the simulated reversal postings on this view. |  |
| 6 | Production Run | Go back to return to the initial view of this app. Deselect the Test Run checkbox and repeat the previous steps for a production run. | The production run succeeds, reversal postings are created. |  |

#### Account Assignment Reference Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An account assignment reference is assigned to each position. In this activity, you transfer positions with their book value from one account assignment reference to another, that is, a transfer of the financial positions to the General Ledger (G/L) accounts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Transfer Account Assignment Reference (TPM28). | The Execute Account Assignment Reference Transfer view displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data:OTC Transactions: <select this checkbox>Company Code: for example, 3310Valuation Area: leave bank, or enter specific valuation are, for example AE0Transaction: <transaction numbers for which account assignment references to be transferred>Posting Date: <the date on which account assignment reference transfer takes place>New Acct Assignment Ref.: <choose an appropriate new account assignment reference>Test Run: <select this checkbox>and choose Execute. | The Display Positions to be Transferred view displays. |  |
| 4 | Execute Transfer for Test Run | Choose Carry out transfer posting. | The Posting Log: Posted Business Transactions view displays.A Transfer posting (in test run) was successful notification displays.You review the simulated postings for account assignment reference transfer on this view.Note No posting created duirng a test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until you return to the initial view of this app.Make the following change:Test Run: <deselect this checkbox>and choose Execute. | The Display Positions to be Transferred view displays. |  |
| 6 | Execute Transfer for Production Run | Choose Carry out transfer posting. | The Posting Log: Posted Business Transactions view displays.A Transfer posting was successful notification displays.You review the postings for account assignment reference transfer on this view.In this operation, the accounting documents are created. |  |

#### Reverse Account Assignment Reference Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you reverse an account assignment reference transfer after the transfer has been updated.

Prerequisite

The account assignment reference transfer has been posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Reverse Account Assignment Reference Transfer (TPM29). | The Reverse Account Assignment Reference Transfer (TPM29) view displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data:OTC Transactions: <select this checkbox>Company code: for example, 3310Valuation Area: leave blankTransaction: <transaction numbers for account assignment reference transfers to be reversed>Reasons for Reversal: for example, 04 Other reasonsTest Run: <select this checkbox>and choose Execute. | The Display Positions to be Reversed view displays. |  |
| 4 | Reverse Transfer for Test Run | Select the items to be reversed, and choose Cancel transfer. | The Reversal Log: Reversed Business Transactions view displays.A Transfers reversed successfully (test run) notification displays.You review the simulated postings for reversal of account assignment reference transfer on this view.Note No posting created during a test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until your return to the initial view of this app.Make the following change:Test Run: <deselect this checkbox>and choose Execute. | The Display Positions to be Reversed view displays. |  |
| 6 | Reverse Transfer for Production Run | On the Display Positions to be Reversed view, select the items to be reversed, and choose Cancel transfer. | The Reversal Log: Reversed Business Transactions view displays.A Transfers reversed successfully notification displays.You review the postings for reversal of account assignment reference transfer on this view.With this operation, the accounting documents are created. |  |

### Cash Flow

#### Update Cash Flow for Deposit at Notice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you update the cash flow for a deposit at notice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Update Cash Flow - Deposit at Notice (TM21). | The Deposits at Notice: Cash Flow Update view displays. |  |
| 3 | Access Report Layout Definition view | Enter the following data:Test Run: <deselect the checkbox>and choose Execute. | The updated cash flow result displays. |  |

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

The adjustment of interest rate has been created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Change Adjustment - Rates/Prices (TI11). | The Change Last Interest/Price Adjustment view displays. |  |
| 3 | Enter Selection Criteria | Enter the following data:Company Code: for example, 3310Transaction: <transaction number with Adjust Interest Rate created in previous procedures>and choose Enter. | The Change Interest Rate/Price Adjustment view displays. |  |
| 4 | Enter New Interest Rate | Enter the following data:Interest Rate: for example, 3and then choose Save. | Manual rate/price adjustment changes. |  |

#### Display Adjustment (Interest Rates/Prices)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the adjustment of the interest rate.

Prerequisite

The adjustment of interest rate has been created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Adjustment - Rates/Prices (TI12). | The Display Rate/Price Adjustment screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data,and choose Enter:Company Code: for example, 3310Transaction: <transaction number with Adjust Interest Rate created in previous procedure> |  |  |

#### Reverse Automatic Adjustments (Interest Rates/Prices)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you reverse the automatic adjustment of the interest rate.

Prerequisite

The automatic adjustment of interest rate has been executed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Reverse Automatic Adjustments - Rates/Prices (TJ05_REV). | The Reverse Automatic Interest Rate/Price Adjustment screen is displayed. |  |
| 3 | Enter Reverse Criteria | Enter the following data, and choose Execute:Company Code: for example, 3310Fixing Date: for example, <the last automatic adjustment date>Test Run: <deselect the checkbox> | The reverse result is displayed. |  |

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

The manual adjustment of interest rate has been executed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Reverse Adjustment - Rates/Prices (TI37) | The Reverse Last Interest/Price Adjustment screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data, and choose Enter:Company Code: for example, 3310Transaction: <transaction number with Adjust Interest Rate created in previous procedure> | The Reverse Last Interest/Price Adjustment screen is displayed. |  |
| 4 | Reverse Interest Rate Adjustment | On the Reverse Last Interest/Price Adjustment screen, choose Save. | Manual rate/price adjustment is reversed. |  |

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

In this activity, you create market data shifts to be able to analyze key figures with modified market data. Your results are used in the succeeding procedure, Defining Report Layout for Calculate Market Risk Key Figures.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Market Data Shift (JBR0). | The Edit Market Data Shifts view displays. |  |
| 3 | Enter Market Data Shifts Name | Enter the following data:Market Data Shift: for example, 1and choose Create. | The Define Market Data Shifts view displays. |  |
| 4 | Define Market Data Shift | Enter the following data:Short Name: for example, Market Data Shift 0001 |  |  |
| 5 | Maintain Yield Curves of Market Data Shift | On the Define Market Data Shifts view, choose the Yield Curves tab and then choose the Insert Row button.Enter the following data:Short Name: for example, Euro Depo ShiftCurrency: for example, AEDYC. Type: for example, 0001Ref.Int.Rate: for example, AEDM03EIBPercentage: for example, 2and choose Save. | The market data shift is saved. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Limit Overview (TBL3). | The Overview of Limits view displays. |  |
| 3 | Enter Selection Criteria | Enter the following data :Limit Type: for example, Y01 to Y09Company Code: for example, 3310and choose Execute. | The Display Limits for Limit Types: Overview view displays. |  |

### Change Counterparty

#### Change Counterparty of Financial Transactions

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

You have created a Treasury and Risk Management Business Partner, 33537002, in advance. For more information, see the Create Business Partner for Treasury and Risk Management - MDS(22G) master data script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Change Counterparty - Financial Transaction (TRTM_CHG_PARTNER) | The Change Counterparty of a Financial Transaction view displays. |  |
| 3 | Test Run | Enter the following data:Company Code: for example: 3310New Partner: for example, 33537002Change Effective From: enter the effective date for the change. For example, <current date>Test Run: <select this checkbox>and select Execute. | The Change Counterparty of a Financial Transaction view displays with Test Run: List of Successfully Changed Financial TransactionsNote If the period specified includes any non-working days, a message indicating non-work days displays. |  |
| 4 | Production Run | Select Exit, deselect Test Run and select ExecuteTest Run: <deselect this checkbox> | The Change Counterparty of a Financial Transaction view displays with List of Successfully Changed Financial Transactions. |  |

#### Display Financial Transactions with Changed Counterparty

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the list of financial transactions for changed counterparty.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Transactions - Changed Counterparty (TRTM_CHG_PARTNER_DIS). | The Display Financial Transactions With Changed Counterparty view displays. |  |
| 3 | Enter Selection Criteria | Enter criteria and choose Execute.Company Code: for example, 3310 | The Display Financial Transactions With Changed Counterparty view displays with List of Financial Transactions with Changed Partner. |  |

### Copy Existing Transaction

#### Copy Debt/Investment Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a debt/investment transaction by copying an existing transaction. Currently, transactions with product type 51A/55A are supported.

|  |
| --- |
| Note You can only copy transactions under the stauts of Contract or Contract Settlement. |

Prerequisite

You have already created a transaction with product type 51A or 55A.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Manage Financial Transactions screen, enter the following data, and then choose Go:Key Date: <the current date>Company Code: for example, 3310Transaction: <transaction number with product type 51A/55A which was created in the previous step>Term End: for example, <delete the default value>Note The copy function mentioned within 1WV only works with product type 51A/55A. | The transactions you selected displays. |  |
| 4 | Copy the TRM Transaction | On the Manage Financial Transactions screen, select the IR instrument transaction to copy and then choose Copy.Note Only transaction with activity as 1=Contract or 2=Contract Settlement could be copied. | The Check parameters screen displays. |  |
| 5 | Enter Copy or Change Data | Enter the following data and choose Copy:Company Code: for example, 3310Partner: for example, 33537001Choose Continue further process further. | The Copy interest rate instrument: Structure screen displays. |  |
| 6 | Maintain Structure of New Deal | On the Copy interest rate instrument: Structure view, check and modify data:Payment Amount: for example, 10MStart: for example, <Current Date>End: for example, <Current Date + 3 years>Interest Category: for example, VariableRef.Int.Rate: for example, AEDM03AED +/- 11st Int. Rate: for example, 3.0000000Int. Calc. Method: for example, Act/360Frequency: for example, MonthlyContract Date: for example, <Current Date/Current Time> |  |  |
| 7 | Maintain Administration of New Deal | Choose Administr. screen, , check and modify data:Portfolio: for example, Y000Gen. Valn Class: <select proper Gen. Valn Class for transaction>, for example, Long term investment (non-current asset): Amortized cost |  |  |
| 8 | Maintain Payment Details of New Deal | Choose the Payment Details tab, In the payment Details tab, you can find the Incoming line with Direction of flow "+" and outgoing row with Direction of flow "-". Double-click the outgoing row, confirm the assignments are identical, check and modify data:Payment Request, With: <select this checkbox>House Bank: for example, AEBK1Account ID: for example, AEAC1Payer/Payee: for example, 33537001Partner Bank: for example, AED1Payment methods: for example, T | Interest rate instrument is created.Note Please check and further verify data input into the Structure/Administration/Other flows/Payment Details/Cash flows/Interest Rate Adjustments/Memos tab before saving. |  |

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

You have created a money market transaction according to the following section of this test script:

- [Create Debt or Investment Contract](#unique_96) [page ] 46

NPV values need to be stored in advance of the valuation of Treasury positions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Simulate Period-End Closing (TPM_SIM_VAL). | The Simulate Period-End Closing screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Simulate Period-End Closing screen, enter the following data and choose Execute:Securities: <deselect this checkbox>OTC Transactions: <select this checkbox>Company Code: for example, 3310Valuation Area: for example, AE0Product Type: for example,55ATransaction Number: for example, <the transaction number created in the previous steps>Recalculate Outdated Sim.Val.: <deselect this checkbox>Note If you set this indicator, you can recalculate the outdated simulation resultsSimulation Date: for example, <the current date>Key Date Valuation: <select this checkbox>Accrual/Deferral: <select this checkbox>Note If you set this indicator, the accrual/deferral of expenses and revenues for the selected treasury positions is simulated, and Accrual/Deferral Parameter is displayed.Test Run: <select this checkbox> | The following message is displayed:Processed xx positions; xx successful, 0 failed.If Recalculate Outdated Simulation Results has been executed, the following message is displayed:xx simulated results deleted for key date, Processed xx positions; xx successful, 0 failed. |  |
| 4 | Execute Simulated Valuation | The dialog Message shows up, and choose Continue. | The Simulate Period-End Closing screen is displayed.You can check the simulated valuation information for local GAAP (valuation area AE0). Please note there is no simulated valuation created because it is test run. |  |
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
| 3 | Enter Selection Criteria for Test Run | On the Delete Results of Simulated Period-End Closing screen, enter the following data and choose Execute:Securities: <deselect this checkbox>OTC Transactions: <select this checkbox>Company Code: for example, 3310Valuation Area: leave bank, or enter specific valuation are, for example, AE0Product Type: for example,55ATransaction: for example, <the transaction number created in the previous steps>Simulation Date: for example, <the date on which the reversal should takes place>Test Run: <select this checkbox> | The following message is displayed:xx simulated results deleted for key date (the date on which the reversal should takes place). |  |
| 4 | Enter Selection Criteria for Production Run | Go back to the initial screen of this app.On the Delete Results of Simulated Period-End Closing screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The following message is displayed:XX simulated results deleted for key date (the date on which the reversal should takes place). |  |

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
| STRM_FT_BO | Back Office Employee for Financial Transactions |  |
| Function Profiles | STRM_FP | Function Profile for Treasury and Risk Management |
| Team Types | STRM_FOE | Treasury Specialist - Front Office |
| STRM_BOE | Treasury Specialist - Back Office |  |

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
| 2 | Access the SAP Fiori App | Open Manage Teams and Responsibilities (F2412). | The Manage Teams and Responsibilities screen is displayed. |  |
| 3 | Create Team | Choose Create. | The Team screen is displayed. |  |
| 4 | Maintain Team General Information | In the General Information section, enter the following data:Name: for example, Z_TEST_01Type: for example, STRM_FOE or STRM_BOEDescription: for example, <TRM Test Description for Situation Handling>Status: Enabled | The Global ID will be generated automatically. |  |
| 5 | Maintain Responsibility Definitions | In the Responsibility Definitions section, enter the following data:Company Code: 3310Transaction Type: <leave blank>Product Type: 51APortfolio: <leave blank>Note You can create your own Portfolio in Manage Your Solution in S/4 HANA or Central Business Configuration in Central Business Configuration using the Define Portfolio configuration activity, so only the transaction assigned with your own portfolio will trigger the notification process. |  |  |
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
| 2 | Access the SAP Fiori App | Open Manage Situation Types (F2947). | The Manage Situation Types screen is displayed. |  |
| 3 | Search the Standard Situation Template | Enter FIN_TRM_FINTRANS_PROCG in the search box and Choose Go. | The Situation Template FIN_TRM_FINTRANS_PROCG shows up in the result. |  |
| 4 | Create New Situation Type via Copy | Select the template and choose Copy. | 1 Situation Type or Types Copied.The Situation Type screen is displayed. |  |
| 5 | Maintain Situation Type Admin Information | On the Situation Type screen, enter the following data:ID: <A unique id with Z_ as prefix>, for example, Z_TRM_ST01Name: Processing of Financial Transactions |  |  |
| 6 | Maintain Conditions | In the Conditions section, enter the following data:Set to Status: OpenSend Notification: <check>In the All Filters section, enter the following data:Company Code: 3310Product Type: 51ATransaction Type: 100Term End: NEXT14DAYS |  |  |
| 7 | Maintain Batch Job Scheduling | In the Batch Job Scheduling section, enter the following data:Time Zone: UTC+08Start Batch Job At: 12:00 |  |  |
| 8 | Maintain Situation Display | In the Situation Display section, you can insert variables if you want to receive detailed information for the notification and email.Enter the following data, and choose Insert Variables:Company Code: <COMPANYCODE>Product Type: <FINANCIALINSTRUMENTPRODUCTTYPE>Transaction: <FINANCIALTRANSACTION>Letter of Credit No.: <LETTEROFCREDIT>In the Notification section, make the following settings：Aggregate Notifications: <check>Resend Notifications: <check> |  |  |
| 9 | Check Recipients | In the Recipients section, make sure the team to receive notifications is listed in the Number of Teams. |  |  |
| 10 | Maintain Situation Monitoring | In the Situation Monitoring section, enter the following data, and choose Create:Monitor Instances: <select>Note Choose Yes in the dialog box to enable the situation type. | The situation type is created. |  |

#### Create Fixed Term Deposit

Purpose

In this step, you create a fixed term deposit transaction.

Procedure

Refer to [Create Fixed Term Deposit](#unique_31) [page ] 46 to create a fixed term deposit, and make sure the end term is within 14 days as of the current date.

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
| 5 | Go to the Detail of the Situation Type | Select the situation type you create in [Enable Situation Types](#unique_166) [page ] 229, double click the selected situation type. | The Situation Type detail screen is displayed. |  |
| 6 | Trigger the Notification | Choose Trigger Now on the Situation Type detail screen. | The Information message The background process for creating situation instances has been triggered is displayed. |  |
| 7 | Check the Triggered Objects List in Situation Instances List | Check OK in the dialog box. | You will go to the Situation Instances screen.Check the transaction you created in [Create Fixed Term Deposit](#unique_167) [page ] 231 on the result list. |  |

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
- related-to :: [[05-treasury-and-cash-management/test-script-debt-and-investment-management-1wv-ae-sap-s-4hana-cloud-pu-part-01]]
- related-to :: [[05-treasury-and-cash-management/test-script-debt-and-investment-management-group-ledger-ifrs-1x7-ae-77]]
- related-to :: [[05-treasury-and-cash-management/test-script-debt-and-investment-management-group-ledger-us-gaap-34c-ae]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1WV_S4CLD2608_BPD_EN_AE.docx` — lines 3002–4975 of the extracted text · extracted with `mammoth` · 396,646 chars in the whole document
