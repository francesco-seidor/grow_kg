---
id: 05-treasury-and-cash-management/test-script-foreign-currency-risk-management-1x1-ae-sap-s-4hana-cloud-part-02
title: "Test Script: Foreign Currency Risk Management (1X1_AE) - SAP S/4HANA Cloud Public Edition 2608 (1X1_S4CLD2608_BPD_EN_AE) — part 2 of 2"
description: "Test script 1X1 Foreign Currency Risk Management, S/4HANA Cloud 2608 (AE), part 2: option maturity, payments, valuation, reporting, jobs, netting, termination."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/foreign-currency-risk-management]
aliases: []
keywords: [Foreign Currency Risk Management (FX Deals), fx option maturity, trm correspondence, payment requests, general ledger posting, net present value, key date valuation, treasury reporting, exposure management, background job scheduling]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1X1_S4CLD2608_BPD_EN_AE.docx#lines-3642-6660"]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-774
topic: 05-treasury-and-cash-management/foreign-currency-risk-management
language: EN
part: 2/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Foreign Currency Risk Management (1X1_AE) - SAP S/4HANA Cloud Public Edition 2608 (1X1_S4CLD2608_BPD_EN_AE) — part 2 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1X1_S4CLD2608_BPD_EN_AE.docx`, part 2 of 2 (lines 3642–6660 of the extracted text), extracted with `mammoth`. Grouped under **Foreign Currency Risk Management (FX Deals)** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| 7 | Save the Cylinder Option (Both Legs) | Choose Save. | If dialog box Document lines: Display messagesAfter the zero/low cost collar FX option (cylinder FX option) is created, you can logon as Treasury Specialist - Middle Office and open app displays, make sure no error message is there (otherwise please correct data and save again), and choose Continue (Enter).Message Options number 1 and number 2 created in company code company code displays.Two legs of cylinder option have been saved, the reference for them has been created.Note down the transaction numbers of these two legs. |  |

|  |
| --- |
| Note After the zero/low cost collar FX option (cylinder FX option) is created, you can log on as Treasury Specialist - Middle Office and open app Hedge Management Cockpit (TOENE) to check the net open exposure again.In app Hedge Management Cockpit (TOENE), the amount of long leg will be reflected in corresponding cells for Key Figure Name Net Hedges and relevant company code, risk currency and period; Net Open Exposure should be reduced accordingly. |

#### (BFB) Basic Cash Operations

Purpose

After the deal is created (in Contractstatus) but before payment is executed, the future cash flows of this deal is reflected in liquidity forecast reports. If basic cash management is implemented in your system, use the Cash Flow Analyzer (F2332) app to check the liquidity forecast.

|  |
| --- |
| Note This step can be executed during the whole lifecycle of the treasury deal. Different results under liquidity forecast reports are shown in the different processing phases of the transaction (for example, before transaction is created, after transaction is created, and after payment is posted). |

Procedure

If basic cash management is implemented in your system, you can use the Cash Flow Analyzer (F2332) app to check the liquidity forecast change. For more information, see the Basic Cash Operations (BFB) test script.

Treasury relevant cash flows are reflected in treasury specific planning levels. For example:

- MM - Money Market Deals
- NM - MM Deals (Bank unknown)
- FX - Foreign Exchange Deals
- FO - Foreign Exchange Options
- NF - Forex Deals (Bank unknown)
- DR - Derivative Deals
- ND - Derivative Deals(Bank unknown)

#### (J78) Advanced Cash Operations

Purpose

After the deal is created (in Contract status) but before payment is executed, the future cash flows of this deal is reflected in liquidity forecast reports. If full cash management is implemented in your system, use the Cash Flow Analyzer (F2332) or Check Cash Flow Items (F0735) apps to check the liquidity forecast.

|  |
| --- |
| Note This step can be executed during the whole lifecycle of the treasury deal. Different results under liquidity forecast reports are shown in the different processing phases of the transaction (for example, before transaction is created, after transaction is created, and after payment is posted). |

Procedure

If full cash management is implemented in your system, you can use the Cash Flow Analyzer or Cash Flow Analyzer (F2332) apps to check the liquidity forecast change. For more information, see the Advanced Cash Operations (J78) test script.

Treasury relevant cash flows are reflected in treasury specific planning levels. For example:

- MM - Money Market Deals
- NM - MM Deals (Bank unknown)
- FX - Foreign Exchange Deals
- FO - Foreign Exchange Options
- NF - Forex Deals (Bank unknown)
- DR - Derivative Deals
- ND - Derivative Deals(Bank unknown)

In addition, in full cash management apps, you can also select treasury specific cash flows by filtering certainty levels:

- TRM_D - Financial Instrument
- TRM_O - Optional Financial Instrument

#### Correspondence

Purpose

SAP TRM provides the standard correspondence functionality. With this correspondence functionality, whenever a TRM transaction is saved, SAP either sends an email to the Business Partner, or automatically prints a form.

To use this correspondence functionality, the following data must be assigned to the Business Partner:

- Business Partner Profile
- Business Partner group
- Swift/BIC code

##### Set Settlement Status (Manual)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once a TRM transaction is recorded and saved in the SAP system, the transaction must be settled before you perform further activities. You can settle the transaction via one of two methods once you get counterparty confirmation:

- Manual settlement

For example, if you receive a counterparty confirmation e-mail, use following apps to settle the transaction manually.

-
    - Manage Financial Transactions
- Automatic settlement via correspondence process

For example, for one transaction, once all the outgoing and incoming correspondence objects are matched and set to completed status, the financial transactions are set to settlement status automatically.

You settle the TRM transaction manually in this step.

Prerequisite

A TRM transaction is created successfully in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria and Go | Enter the following data and choose Go:Company Code: for example, 3310Transaction: <the transaction number created in the previous step> | The transaction is displayed on the screen. |  |
| 4 | Settle the TRM transaction | Select the checkbox at the beginning of the transaction line and choose Settle. | The OTC Option: Settle Contract : Structure screen displays with the transaction data. |  |
| 5 | Save the change | Choose Save. | The transaction is settled and saved. |  |
| 6 | Check the status of the TRM transaction | Select the checkbox and choose Details at the end of the transaction line. | The OTC Option: Display: Structure screen is displayed. |  |
| 7 | Check Status | Choose ... > Status.The Activity Cat field is in Contract Settlement status. | The transaction has the Contract Settlement status. |  |

|  |
| --- |
| Note For zero/low cost collar FX option (cylinder FX option), please set the Contract Settlement status for both legs. |

##### Correspondence with PDF Form

Purpose

Email/Print are all PDF form-related output. By default, SAP provides business profiles for several PDF forms (for example, PR_PRINT and PR_EMAIL).

- For any Business Partner assigned to profile PR_PRINT, when a financial transaction is created, a PDF form is sent to a predefined print queue. To view and print the PDF file, use the SAP Fiori app Maintain Print Queues (F1260). Once you check and confirm that the transaction information on the form is correct, you may then send the paper copy of the form to the Business Partner.
- For any Business Partner assigned profile PR_EMAIL, when a transaction is created, SAP automatically sends emails to the Business Partner.

Once you receive the counterparty confirmation about the transaction from your Business Partner, you can settle all the correspondence objects of the transaction. Once all the correspondence objects are settled, the transaction status changes to Contract Settlement status.

|  |
| --- |
| NoteYou can use the following apps to maintain your own settings for output:Output Parameter DeterminationYou maintain your own rules for the output. For example, you can maintain email addresses of recipients. This rule overwrites the email address of the Business Partner for an external counterparty, or it overwrites the email address of User IDs for an internal counterparty.Maintain Email Templates - Deprecated (F1306). You maintain your own email template with this app.Maintain Form Templates (F1434). You maintain your own form template with this app.In this step, you settle the TRM transaction via the correspondence processing automatically. |

Prerequisites

You've created a TRM transaction which has not been settled.

###### Send Confirmation Email / Print

Purpose

SAP provides Business partner group BPG_DEFAULT. By default, if any business partner is assigned to this group, correspondence objects are automatically sent when a financial transaction is saved. As described in the preliminary steps, the Business Partner 33537001 is assigned to BPG_DEFAULT, so the correspondence objects are sent automatically. However, if you create a new business partner group via configuration stepDefine Business Partner Group and do not assign the auto-send attribute, you may need to send those correspondence objects manually via the Send Correspondence (FTR_COSEND) app.

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Procedure

This step does not require any operation in the system.

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

In the prior step, for Email channel, an outbound email is sent to the Business Partner. Normally, you receive counterparty confirmation from the Business Partner via Email, phone, and so on. This step is performed outside of the SAP system.

Procedure

This step does not require any operation in system.

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
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Correspondence - Monitor (FTR_COMONI). | The Correspondence Monitor view displays. |  |
| 3 | Enter Selection Criteria on the Initial View | Enter the following data and choose Execute:Correspondence group:Company Code: for example, 3310Financial Transaction group:Company Code: for example, 3310Transaction Number: for example, <Transaction Number>Note Make a note of the correspondence key for a COUNTERPARTY correspondence object. | Please note down the correspondence key numbers for COUNTERPARTY PRINT and COUNTERPARTY EMAIL. |  |
| 4 | Create | Choose Create. | The Options for Creating Correspondence Objects view displays. |  |
| 5 | Create an Incoming Correspondence Object Referring to the Outgoing Correspondence Object | Enter the following data for groups and press Enter:Display Options group:Corresp. Category: 01 Transaction ActivitiesTransaction Details group:Company Code: for example, 3310Product Type: for example, <Product type you entered in the transaction>Incoming/Outgoing: I IncomingEntry Options: 05 Correspondence object as templateTemplate for Correspondence Object Data group:Correspondence Key: for example, <Enter the correspondence key number for COUNTERPARTY PRINT from the previous step> |  |  |
| 6 | Save | Choose Save.Note If the Automatic matching proposal view displays, choose Cancel. | The incoming correspondence object is created successfully and displayed on Correspondence monitor - Standard View view. |  |
| 7 | Match the Incoming Correspondence Object with the Outgoing Correspondence Objects for channel PRINT | Select the checkbox for the incoming correspondence object and choose Status Functions > Automatic Match. | The Automatic matching proposal view displays. |  |
| 8 | Outgoing Correspondence | On the left-side of the view, expand the incoming correspondence key. All outgoing correspondence objects of the transaction are displayed.Select all the checkboxes of the outgoing correspondence objects and choose Enter. | All the outgoing COUNTERPARTY PRINT correspondence objects of the transaction now have status completed.All the INTERNAL outgoing correspondence objects remain in Delivered status. |  |
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

In the previous step, all correspondence objects of the transaction are matched successfully. As the standard functionality, the transaction is settled automatically.

In this step, you only check if the transaction has been settled automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Correspondence - Monitor (FTR_COMONI). | The Correspondence Monitor screen displays. |  |
| 3 | Enter selection criteria on the initial screen | Enter the following data and choose Execute:Correspondence tab:Company Code: for example, 3310Deal tab:Company Code: for example, 3310Deal Number: for example, <Transaction Number> | The Correspondence monitor - Standard View screen displays. |  |
| 4 | Display the transaction history | Select the checkbox of the incoming correspondence object and choose Show Underlying. | The OTC Option Display: Issue Structure screen displays. The second row shows Activity 2 Contract Settlement. |  |

For zero/low cost collar FX option (cylinder FX option), please check settlement status for both legs.

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

Each financial transaction contains flows that need to be paid. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment in practice). Treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows.

Within these two apps, if you select the ‘Schedule Auto Payment Run’ option, system will automatically process the automatic payment run for payment requests.

|  |
| --- |
| Note You can also schedule a background job for this step. Please see the corresponding step in the Appendix section. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data, and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps, for zero/low cost collar FX option (cylinder FX option), it is the long leg>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date + 2 working days>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Pay Only: <select this indicator>Test Run: <select>Pay Only: <select> | Screen Logs and Messages displays, you can check the payment information via the Payment Log.Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | Enter the following data, and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps, for zero/low cost collar FX option (cylinder FX option), it is the long leg>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date + 2 working days>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Test Run: <select> | Screen Logs and Messages displays, you can check the payment information via the Payment Log.Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows screen, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
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

Each financial transaction contains flows that must be paid. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment in practice). The treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows that require payment request. It does not create postings in financial accounting.

If the payment is initiated by the financial partner, skip this procedure and the following [Process Payment Request](#unique_84) [page ] 165 procedure and continue with the [Bank-Initiated Payment](#unique_155) [page ] 168 procedure.

|  |
| --- |
| Note A background job can be scheduled for this step. For more information, see the Generate Payment Request procedure in the Job Scheduling section of the Appendix. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data and choose Run:Derivatives: <select>Company code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps, for zero/low cost collar FX option (cylinder FX option), it is the long leg>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date + 2 working days>Test Run: <select>Pay Only: <select> | The Payment Log - Test Run screen displays. Review the payment information on this view.If the system displays the No flows exist for processing notification, no payment with payment request is needed for your selection criteria. Go to the succeeding Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows screen, change the following data, and choose Run:Test Run: <deselect> | The Payment Log view displays. The payment request is generated.Make a note of the key number displayed on this screen: __________ |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows screen displays. |  |
| 3 | Test Run | Enter the following data, and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps, for zero/low cost collar FX option (cylinder FX option), it is the long leg>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <current date + 2 working days>Test Run: <select> | The Payment Log - Test Run view displays. Review the payment information on this view.If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows screen, change the following data, and choose Run:Test Run: <deselect> | The Payment Log view displays. A payment request is generated.Make a note of the key number: __________ |  |

###### Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use this app to start the Payment Program for Payment Requests. The payment program for payment requests app provides another automatic payment option in the SAP system. Unlike the standard payment program, the payments are based on payment requests, not on open items (vendor/customer items).

Prerequisites

A payment request is generated in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests screen displays. |  |
| 3 | Enter Run Date and Identification | Enter the following data and choose Parameters:Run Date: For example, <current date>Identification: For example,TRM01 | The Automatic Payment Transactions: Parameters screen displays. |  |
| 4 | Enter Parameters | Enter the following data and choose Dynamic selections:Posting Date: For example, <current date>Next payment run on: For example, <current date + 3 days>Company Code: For example, 3310Payment Methods: For example, TF | The Free Selection for payment run dialog box displays. |  |
| 5 | Key Number | Enter the following data and choose Save:Key Number: <the key number you noted down in previous step> | The Automatic Payment Transactions: Parameters screen displays. |  |
| 6 | Additional Log | Choose Additional Log. | The Additional Log dialog box displays. |  |
| 7 | Enter Parameters | Make the following entries and choose Continue:Payment method selection in all cases: <select>Line items of the payment documents: <select>Due date check: <select>If the system displays the message Log created for all accounts displays, choose Continue.Choose Save on the Automatic Payment Transactions: Parameters screen. | The system displays the message Parameters have been entered displays on the Automatic Payment Transactions for Payment Requests screen. |  |
| 8 | Schedule Proposal | Choose Proposal. | The Schedule Proposal dialog box displays. |  |
| 9 | Schedule Job | Select Start Immediat. and choose Schedule Job. | The system displays the message Proposal is running with a yellow traffic light. |  |
| 10 | Update Status | Choose Status until the message Payment proposal has been created displays in the status bar with green traffic light. | The payment proposal is generated. |  |
| 11 | Schedule Payment | Choose Pmnt run. | The Schedule Payment dialog box displays. |  |
| 12 | Schedule Job | Select Start Immediat., select Create Payment Medium and choose Schedule Job. | The message Payment run is running displays in the status bar with a yellow traffic light. |  |
| 13 | Update Status | Choose Status until the message Payment run has been carried out displays with a green traffic light. | The Automatic Payment Transactions for Payment Requests screen displays.The payment document is created.If Bank Communication Management (BCM) is not implemented in your system, the payment medium is created if it uses PMW format. You can check log by clicking Display payment log.If BCM is implemented in your system, in Display payment log, you see the message Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media. A BCM batch is created after the payment run. For more information, see the next test step. |  |
| 14 | Cross-Payment Run Payment Media (Create BCM Batch) | Choose Menu > Environment > Payment Medium > Cross-Payment Run Payment Medium > Create Payment Medium . | The Creation of Cross-Payment Run Payment Media screen displays. |  |
| 15 | Enter Data | Enter the following data and choose Run:Run Date: For example, <current date>Identification: For example, TRM01R | The Creation of Cross-Payment Run Payment Media dialog box displays with the message Collector XX/XX/20XX XXXXXX was created or updated. The BCM batch is created.A batch may need additional approvals before the payment medium is finally created. For more information, see the Advanced Cash Operations(J78) test script. |  |

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

If the outgoing payment is initiated by bank, it is not necessary to run the previous steps Generate Payment Request for Mature Transaction and Process Payment Request, because the outgoing payment is initiated by the bank.

Procedure

This step does not require any steps in the SAP system.

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

- Fix, Pay and Post Flows (TBB1): This SAP Fiori app supports to generate posting for incoming payment and outgoing payment without payment request. You can not use this app to generate postings for outgoing payments that have been processed in the previous Generate Payment Request for Mature Transaction step with the Pay Only option.
- Process Business Transactions (TPM10): You use this SAP Fiori app to generate postings for outgoing payments that have been processed in the previous Generate Payment Request for Mature Transaction step with the Pay Only option.

|  |
| --- |
| Note A background job can be scheduled for this procedure, please see the Job Scheduling section in the Appendix. |

Prerequisites

Outgoing payments handled using payment request were processed in the previous Generate Payment Request for Mature Transaction procedure with the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data:Foreign Exchange: SelectedCompany Code: For example, 3310Transaction: <transaction number with inflow created in previous steps, for zero/low cost collar FX option (cylinder FX option), it is the short leg>Up to and Including Due Date: Enter date on which the flow of financial transaction should be posted, for example, <current date>Test Run: SelectedPost Operational Only: Selectedand choose Run: | The Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting created during a test run.If the system displays the No flows exist for processing notification, no posting is needed for your selection criteria.You can skip the next steps and continue with step 6, using the Process Business Transactions (TPM10) app. |  |
| 4 | Back | Choose Back. | The Fix, Pay and Post Flows screen is displayed. |  |
| 5 | Production Run | Make the following entries and choose Execute:Test Run: Deselected | The Posting Log: Posted Business Transactions view displays. The accounting document is created for incoming payment in local GAAP (valuation area AE0). |  |
| 6 | Access Another SAP Fiori App | Return to the SAP Fiori launchpad and open Process Business Transactions (TPM10). | The Process Business Transactions view displays. |  |
| 7 | Enter Selection Criteria for Test Run | Enter the following data:OTC Transactions: SelectedCompany Code: For example, 3310Valuation Area: For example, AE0Limit by Transaction Number: Deselect this checkboxLimit by Subledger Pos.: SelectedTransaction: <transaction number with outflow and its payment request that you generated in the previous Generate Payment Request procedure, for zero/low cost collar FX option (cylinder FX option), it is the long leg>Test Run: Selectedand choose Run. | The Test Run: Post/Reverse Business Transactions view displays.If the system displays the You have not selected any business transactions notification, no postings are needed for your selection criteria. You can skip the current step. |  |
| 8 | Check Test Run Result | Choose Select All.Choose Choose Those to Post.Choose Run. | The Test Run: Display Posted/Reversed Business Transactions view displays. |  |
| 9 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting is created during a test run. |  |
| 10 | Back | Choose Back. | The Process Business Transactions view displays. |  |
| 11 | Deselect Test Run | Make the following change:Test Run: Deselectedand choose Run. | The Update Run: Post/Reverse Business Transactions view displays. |  |
| 12 | Production Run | Choose Select All.Choose Choose Those to Post.Choose Run. | The Update Run: Display Posted/Reversed Business Transactions view displays. |  |
| 13 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. The accounting document is created for outgoing payment in local GAAP (valuation area AE0). |  |

#### Period end has been reached

##### Calculate or Maintain Fair Value of Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you determine the fair values (NPV - net present values) of financial transactions.

The net present values can be calculated automatically by the Market Risk Analyzer (MRA) and saved to table VTVBAR. These values can then be used for the accounting valuation. In addition, you can also maintain the relevant net present value manually.

Predelivered configuration in MRA provides three options when calculating NPV automatically via app Calculate Net Present Values - With CVA and DVA (TPM60CVA):

- Risk-free NPV: using the evaluation type that doesn't contain basis spread curve or credit spread curve, system only calculates the risk-free NPV.
- Risk-based NPV with credit spread curve: using the evaluation type that contains credit spread curve, system calculates risk-free NPV by using risk-free yield curve, and calculates the (risk-based) NPV, which also accounts for credit spreads.
- Risk-based NPV with basis spread curve and credit spread curve: using the evaluation type that contains basis spread curve and credit spread curve, system calculates risk-free NPV by using risk-free yield curve and basis spreads curve, and calculates the (risk-based) NPV, which also accounts for credit spreads.

There are two kinds of calculation method for CVA and DVA:

- Based on Expected Exposures
- Difference method

The formula for NPV is: NPV = risk-free NPV - CVA - DVA.

Prerequisites

Before calculating NPV via the Calculate Net Present Values - with CVA and DVA app, ensure that relevant market data (interest rates, foreign exchange rates, credit spreads, and so on) are maintained for the evaluation date. For details of market data maintenance, see the Market Rates Management – Manually via Upload(1XN) test script.

If you want to calculate NPV for your option with implied volatilies, please assign Currency Pairs for Volatilities with Moneyness and enter Values for Volatilities with Moneyness. For details, please refer to the Market Rates Management – Manually via Upload(1XN) test script. If you don't assign Currency Pairs for Volatilities with Moneyness or enter Values for Volatilities with Moneyness, then system calculates option with historical volatilities.

Procedure

Option 1: Calculate NPV Automatically

|  |
| --- |
| Note You can also schedule the background job for the first option. For more information, see the corresponding step in the Appendix. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Calculate Net Present Values - With CVA and DVA (TPM60CVA). | The Determine NPVs Including Credit and Debit Value Adjustments screen is displayed. |  |
| 3 | Enter Selection Criteria and Execute | Enter the following data and choose Execute:Evaluation Parameter Derivatn: <deselect>Select OTC Transaction: <select>Company Code: for example, 3310Transaction: <transaction number from previous steps, for zero/low cost collar FX option (cylinder FX option), enter the transaction numbers of both legs>Evaluation Date: for example, <last date of current month>CVD/DVA Type: To calculate risk-free NPV, enter nothing. To calculate risk-based NPV and CVA/DVA, enter Y01.Evaluation Type: To calculate risk-free NPV, enter Y001. To calculate risk-based NPV and CVA/DVA, enter Y002.Test Run: <deselect>Price/NPV Type: 001Save Values with Warnings: <select>Detail Log (Other Calc. Steps): <select> | The NPVs including CVA/DVA from the Market Risk Analyzer screen displays, the NPV, risk-free NPV, CVA, DVA of each transaction.To check other information, you can use the following buttons:Single Transaction:CVA/DVA Key FiguresDetailed LogCalculation BasesError Log |  |

Option 2: Maintain NPV Manually

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Net Present Values (F7601). | The Manage Net Present Values screen displays. |  |
| 3 |  | Choose Create. | The Net Present Value Data screen displays. |  |
| 4 | Enter Header | Make the following entries:Transaction: <transaction numbers created in previous steps, for zero/low cost collar FX option (cylinder FX option), enter the transaction numbers of both legs>Company Code: for example, 3310Price / NPV Type: 001Effective from: for example, <last date of current month> |  |  |
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

You use the valuation function to value the positions of financial instruments based on historical cost or fair value for a given key date, and transfer results to financial accounting.

|  |
| --- |
| Note You can also schedule background job for this step. For more information, see the corresponding step in the Appendix section. |

Prerequisites

Fair values (NPV) are calculated or maintained for financial transactions, which are evaluated at fair value (NPV) according to accounting principles.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Run Valuation (TPM1). | The Run Valuation screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:In the Product Groups area,OTC Transactions: <Select this checkbox>In the General Selections area,Company Code: for example, 3310Valuation Area: for example, AE0Transaction: <transaction number(s) created in previous steps, for zero/low cost collar FX option (cylinder FX option), enter the transaction numbers of both legs>In the Valuation Parameters area,Key Date for Valuation: for example, <last date of current month>Valuation Category: for example, Mid-year Valuation with ResetNote When the period end is also the year end, use the Valuation Category Year End Valuation.Test Run: <selected> | The Display Selected Treasury Positions for Valuation screen displays. |  |
| 4 | Execute Valuation for Test Run | Choose Run Valuation.If a Message dialog box displays, choose Continue. | The Valuation Log screen displays. If a red traffic light is shown, click it and check the error message. Solve the issue and perform a test run again until you resolve the error.You can check the simulated posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. There is no posting created because it is a test run.Note Sometimes, there is no simulated posting because your selected transaction may not need valuation. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until you return to the Run Valuation screen.Change the following data and choose Execute:Test Run: <deselect> | The Display Selected Treasury Positions for Valuation screen displays. |  |
| 6 | Execute Valuation for Production Run | Choose Run Valuation. | The Valuation Log screen displays. Check the posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. The accounting document is created in the local GAAP (valuation area AE0). |  |

#### Transaction is Mature

Purpose

This section describes the required operations when the option transaction is mature. User must decide whether to exercise or expire the option and conduct the following operations.

##### Check the Manage Financial Transactions Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the status of the transactions and conduct operations accordingly.

|  |
| --- |
| Note If it is zero/low cost collar FX option (cylinder FX option), please perform following steps (exercise or expire) for long leg.If the long leg is in-the-money when maturity, usually the company will exercise the long leg and counterparty will expire the short leg.If the long leg is out-of-the-money when maturity, usually the company will expire the long leg and counterparty will exercise the short leg. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Go:Company Code: for example,3310Transaction: <the number of maturing transaction, for zero/low cost collar FX option (cylinder FX option), enter the maturing transaction numbers of long leg> | The option transactions are displayed on the screen. |  |

###### Decide to Exercise

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform the operation to exercise a matured FX option.

Prerequisites

- An FX option transaction exists, updated to Contract Settlement status, and reaching its maturity.
- Enter the Manage Financial Transactions screen as described in the [Check the Manage Financial Transactions Report](#unique_161) [page ] 176.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Go:Company Code: for example,3310Transaction: <the number of maturing transaction, for zero/low cost collar FX option (cylinder FX option), enter the maturing transaction numbers of long leg> | The option transactions are displayed on the screen. |  |
| 4 | Select a Transaction and Exercise | Select a transaction with the following criteria and choose Exercise:Activity Cat. Name: Contract Settlement | The OTC Option: Add Activity screen is displayed, with the Company Code and Transaction on the screen. |  |
| 5 | Proceed | Press Enter. | The OTC Option Add Activity: Issue Structure screen is displayed. |  |
| 6 | Enter Data and Save | Enter data and choose Save.Confirm the Exercise Date:If Exercise Type is European, the Exercise Date should be equal to Exercise Period.If Exercise Type is American, the Exercise Date should be earlier than or equal to Exercise Period.Note Make sure the Contract Date is earlier than the Exercise Period. | The data is saved without error. |  |

###### Create FX Spot Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform operations after exercising a currency option to create an FX Spot transaction.

Prerequisites

An FX option transaction is exercised.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Go:Company Code: for example,3310Transaction: <the number of maturing transaction, for zero/low cost collar FX option (cylinder FX option), enter the maturing transaction numbers of long leg> | The option transactions are displayed on the screen. |  |
| 4 | Select a Transaction and Settle | Select a transaction that matches the following criteria and choose Settle:Activity Cat. Name: Exercise | The OTC Option: Settle Exercise: Structure screen is displayed. |  |
| 5 | Enter Data and Save | Choose Save. | The FX Transaction: Structure screen is displayed. |  |
| 6 | Confirm Data and Save | Confirm the following data and choose Save.Transaction Type: 107 Spot Transaction from OptionEditable fields are initialized with the value from the exercised option transaction. Confirm them, then choose Save. | The data is saved and the new transaction number is generated. |  |

|  |
| --- |
| Note Refer to the previous steps for subsequent operations (such as Cash Operations, Correspondence, Period end has been reached).All steps including and after Basic Cash Operations(BFB) under the Foreign Currency Risk Management and Accounting - Without Options section. |

###### Decide to Expire

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform the operation to expire a matured FX option.

Prerequisites

- An FX option transaction exists, updated to Contract Settlement status, and reaching its maturity.
- Enter the Manage Financial Transactions screen as described in the Check the Manage Financial Transactions Report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office。 | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Go:Company Code: for example,3310Transaction: <the number of maturing transaction, for zero/low cost collar FX option (cylinder FX option), enter the maturing transaction numbers of short leg> | The option transactions are displayed on the screen. |  |
| 4 | Select a Transaction and Exercise | Select a transaction that meets the following criteria and choose Expiration:Activity Cat. Name: Contract Settlement | The OTC Option: Expired: Structurescreen is displayed. |  |
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

In this step, you fix and post derived business transactions (usually realized profit and loss when a deal is mature).

|  |
| --- |
| Note You can also schedule a background job for this step. For more information, see the corresponding step in the Appendix. |

Prerequisites

The maturity date of transaction is reached.

The financial transaction is created, settled, and posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Post Derived Business Transactions (TPM18). | The Fix and Post Derived Business Transactions screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Transactions: SelectedCompany Code: For example, 3310Valuation Area: For example, AE0OTC Transactions: <transaction number(s) that are mature, for zero/low cost collar FX option (cylinder FX option), enter the transaction numbers of both legs>TRL Date: <maturity date of transaction>Test Run: SelectedConfirm the message Are you sure that you want to select future business transactions by pressing Enter | The Fix and Post Derived Business Transactions screen displays.If the No scheduled derived business transactions were found for the selection message displays, no derived transaction is available for your selection. You can skip the current step. |  |
| 4 | Fix and Post for Test run | Choose Fix. | The Posting Log: Posted Business Transactions screen displays. You can see the simulated posting information for local GAAP (valuation area AE0). There is no posting created because it is test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until you return to the initial screen of this app.Change the following data and choose Execute:Test Run: DeselectConfirm the message Are you sure that you want to select future business transactions by pressing Enter | The Fix and Post Derived Business Transactions screen displays. |  |
| 6 | Fix and Post for Production run | Choose Fix. | The Posting Log: Posted Business Transactions screen displays. You can see the posting information for local GAAP (valuation area AE0). An accounting document is created in the local GAAP (valuation area AE0). |  |

### Reporting

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
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Accountant |  |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Position Flows (F1754). | The Display Treasury Position Flows (F1754) screen displays. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Go:Product Group: for example,OTC TransactionsCompany code: for example, 3310 | The position Flow data displays per the filter values. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Treasury Alerts - Posting (F4984) | The Display Treasury Alerts - Posting screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Go:Issue Message For: PostingCompany Code: for example, 3310 | Alerts data is displayed per the filter values. |  |

#### Display Treasury Alerts - Settlement, Release, Payment and Correspondence

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
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Alerts - Settlement (F4979) | The Display Treasury Alerts - Settlement screen displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Issue Message For: SettlementCompany Code: for example, 3310 | Alerts data displays per the filter values. |  |
| 4 | Confirm Alerts for Other Transactions | Select other values in the Issue Message For field. |  |  |
| 5 | Select Display Treasury Alerts Tiles with Release | Open Display Treasury Alerts - Release (F4980). | The Display Treasury Alerts - Release screen displays, with the issue message For: Release. |  |
| 6 | Select Display Treasury Alerts Tiles with Payment | Open Display Treasury Alerts - Payment (F4981). | The Display Treasury Alerts - Payment screen displays, with the issue message For: Payment. |  |
| 7 | Select Display Treasury Alerts Tiles with Correspondence | Open Display Treasury Alerts - Correspondence (F4983). | The Display Treasury Alerts - Correspondence screen displays, with the issue message For: Correspondence. |  |

#### Display Payment Schedule

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the payment schedule for outgoing cash flows due.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Payment Schedules (TJ04). | The Treasury: Payment Schedules screen displays. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Execute:OTC Transactions: SelectedCompany code: for example, 3310End of Term in the Future:SelectedEnd of Term Lapsed: SelectedPayment Period: for example, <Current Date> to <Current Date + 5 days>Payment Status: for example, 1Output Error Log: Selected | You can check the payment schedule report. |  |

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
| 2 | Access the SAP Fiori app | Open Display Treasury Posting Journal (F1755). | The Display Treasury Posting Journal (F1755)screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Go:Product Group: for example, OTC TransactionsCompany Code: for example, 3310 | The posting journals display per the filter values. |  |

#### Treasury Position Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display treasury position analysis for review.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Treasury Position Analysis. | The Treasury Position Analysis screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select GoKey Date: for example, <Current Date>Include Planned Data: for example, 1Valuation Area: for example, AE0Company Code: for example, 3310Product Type: for example, 60A, 60B and 76AWhen entering multiple Product Type, you can use Enter key. For example, enter 60A, press Enter key. Then, enter 60B and press Enter key. | The position analysis data displays per the filter values. |  |

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
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Position Values (F1867). | The List Report screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Go:Key Date: for example, <Current Date>Product Group: for example, OTC TransactionsCompany Code: for example, 3310 | The position values data displays per the filter values. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Risk Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Define Financial Positions (FTR_FP_DEF). | The "Maintain Financial Position Groups": Change screen is displayed. |  |
| 3 | Maintain Key Figure Groups | Choose New Entries.Make the following entries and choose Save:Financial Position Group: for example, FPG_FX_A0001Financial Position Group Description: for example, Foreign Exchange AccountAssets/Liabilities: for example, Not Specified | The data is saved. |  |
| 4 | Maintain Key Figures | Choose the Maintain Financial Positions tab.Choose New Entries.Make the following entries and choose Save:Financial Position: for example, FP_FX_A0001Financial Position Description: for example, Foreign Exchange AccountFinancial Position Group: for example, FPG_FX_A0001Data Source: for example, Treasury Position Management | The data is saved. |  |
| 5 | Maintain Selections | Select the financial position above, and choose Back, then choose Maintain Selections.Make the following entries, then choose Back:Product Type = 60A to 76ATransaction Type = 100 to 110Valuation Class = 40 to 45Valuation Area = 002Posting Status = 2Choose Save. | The data is saved. |  |

#### Financial Status (Book Value)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the financial status on book values.

|  |
| --- |
| Note The app only shows book value amounts in position currency converted in display currency. For FX Spots/Forwards, there is no book value amount in the position currency. FX Spots/Forwards have got book value amount in valuation currency only. Hence amount in display currency is zero. |

Prerequisites

Financial positions are already defined. For more information, see [Define Financial Positions](#unique_94) [page ] 188.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Risk Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Financial Status (F2136). | The Financial Status - Book Value screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Go:Key Date: for example, <Current Date>Display Currency: for example, AEDExchange Rate Type: for example, MCompany Code: for example,3310 | The data displays per the filter values. |  |

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
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Payments (TPM20A). | The Payment Journal screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Execute:Company Code: for example, 3310Product Type: 60A | The payment journals display. |  |
| 4 | Review data | Review the data displayed on the screen. You can also choose Original business transaction or Details to drill down for more details. |  |  |

#### Analyze NPV

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you calculate and display the NPV result.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Analyze NPV (JBRX). | The NPV Analysis: Display of Single Values screen displays. |  |
| 3 | Enter Selection Criteria of Gen. Selection | Enter the following data:Evaluation Currency: for example, AEDEvaluation Type: for example, Y001Evaluation Date: for example, <Current Date>Horizon: for example, <End Date of Current Month>Portfolio Hierarchy: for example, 100 | The system calculates the net present value as on the horizon date, but selects the transaction data and market data for the evaluation date. |  |
| 4 | Enter Selection Criteria of Characteristics | Choose the Characteristics tab. |  |  |
| 5 | Enter Selection Criteria of Characteristics | Enter the following data and choose Execute:Company Code: for example, 3310Product Type: for example, 60A | The NPV result displays based on Portfolio Hierarchy. |  |

#### Calculate Market Risk Key Figures

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can use this function to calculate online and display the key figures for NPV analysis and sensitivity key figures for a selection of transactions. You can also use the key figures that are calculated as the basis for defining formula-based key figures, and display them with the NPV and sensitivity key figures.

Prerequisite

Maintaining the report layout for key figure. Follow the [Defining Report Layout for Calculate Market Risk Key Figures](#unique_163) [page ] 242 procedure in the Appendix section.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Calculate Market Risk Key Figures (AISGENKF). | The Calculate Market Risk Key Figures screen displays. |  |
| 3 | Enter Selection Criteria of Gen. Selection | Enter the following data:Evaluation Currency: for example, AEDEvaluation Type: for example, Y001Evaluation Date: for example, <Current Date>Horizon: for example, <Current Date>Report Layout: for example, <Y01 or other Report Layout you created>Portfolio Hierarchy: for example, 100 | The system calculates the net present value as on the horizon date, but selects the transaction data and market data for the evaluation date. |  |
| 4 | Enter Selection Criteria | Choose the Characteristics tab. |  |  |
| 5 | Enter Selection Criteria | Enter the following data then choose Execute:Company Code: for example, 3310Product Type: for example, 60A To: for example, 60B | The Single Value Analysis for assigned Report Layout display. |  |

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
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Sensitivity Key Figures - Single Analysis (AISS). | The Sensitivity Key Figures screen displays. |  |
| 3 | Enter Selection Criteria of Gen. Selection | Enter the following data:Display Currency: for example, AEDEvaluation Type: for example, Y001Evaluation Date: for example, <Current Date>Horizon: for example, <End Date of Current Month>Portfolio Hierarchy: for example, 100 | The system calculates the net present value as on the horizon date, but selects the transaction data and market data for the evaluation date. |  |
| 4 | Characteristics | Choose the Characteristics tab. |  |  |
| 5 | Enter Selection Criteria | Enter the following data then choose Execute:Company Code: for example, 3310Product Type: for example, 60A | The Sensitivity Key Figures displays based on portfolio hierarchy. |  |

#### Review Limit Utilization Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the Limit Utilization Report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Review Limit Utilizations (TBLB). | The Overview of Utilizations - Selection Using all Characteristics screen displays. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Execute:Limit type: for example, Y01Limit Utilization Base: for example, 1Determination Date: for example, <Current Date>Limits Valid From: for example, <Current Date> | The system displays an overview of the limit utilizations in accordance with your selection criteria. |  |

## Appendix

### Exposure Management

#### Overview of Raw Exposures

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review and collectively process the raw exposures.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Raw Exposures - Collective Processing (FTREX2). | The Raw Exposures : Overview screen displays. |  |
| 3 | Enter Selection Criteria | Choose Execute.Note If necessary, you can also enter criteria to filter the raw exposures. | The Raw Exposures : Overview screen displays with raw exposure records. |  |

#### Process Exposure Positions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review and process the exposure positions on a given key date.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Exposure Positions (FTREX12). | The Raw Exposure Positions screen displays. |  |
| 3 | Enter Selection Criteria | Enter the following data and select Execute.Key Date: for example, <Current date> | The Exposure Positions as of screen displays with the exposure positions on the given date. |  |

#### Display Exposure Position Flows

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review and process the exposure position flows.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Exposure Position Flows (FTREX13). | The Exposure Position Flows screen displays. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Execute:Exposure Position Type: for example, YFX | The Exposure Positions as of screen displays. |  |

#### Description on the Template for Import Raw Exposures

| Fieldname | Description |
| --- | --- |
| External Document Number | A parameter for transferring the external document number for the BAPI methods of the business object Raw Exposure in New Exposure Management (BUS5990). This parameter represents the reference document number to which the raw exposure refers and forms the key along with exposure origin and logical system to uniquely identify a raw exposure. |
| Exposure Origin | A parameter for transferring the exposure origin for the BAPI methods of the business object Raw Exposure in New Exposure Management (BUS5990). This parameter represents the origin of the raw exposure (MM, SD, and so on) and forms the key along with external document number and logical system to uniquely identify a raw exposure. |
| Logical System | In the SAP System the client corresponds to a logical system. The distribution of data between systems requires that each system in the network has a unique identification. The logical system is used for this purpose. |
| Exposure Activity Type | The exposure activity type encapsulates an exposure category for foreign exchange (FX) and an exposure category for a commodity. It also identifies whether the commodity risk is of Classical (Pricing Risk only) or it is a new approach Pricing and Delivery Risks based.The exposure activity type gives semantic meaning to an exposure. It is also the anchor for the dynamic field selection feature. A raw exposure is always created with an exposure activity type. |
| Exposure Category of Raw Exposure | A raw exposure can be categorized using exposure categories such as Forecasted Transaction, Firm Commitment Transaction, or Asset/Liability Transaction.The exposure category is used as one of the criteria for differentiating exposure positions, because hedge accounting rules are different for these categories. |
| Country Key | The country key contains information that the system uses to check entries such as the length of the postal code or bank account number. The two-character ISO code in accordance with ISO 3166, which is delivered by SAP as a default, is usually used. It can also be the vehicle license plate country-code or a typical country key (for example, in Germany, the Federal statistics office key). The country keys are determined during system installation in the global settings. The definition of the country key in the SAP system does not have to match political or government entities. Because the country key does not have to correspond to the ISO code in all installations, programs that differ according to certain values of the country key cannot query the country key T005-LAND1, but must program based on the ISO code T005 INTCA. |
| ISO code | International standardized country key in accordance with ISO 3166.The entry is used in countries of the European Community to check the VAT registration number (VAT reg.no.). You can store the VAT registration number in the master record of a customer or vendor, or for the company code. The ISO code is used as the country key when exchanging information via EDI. You must therefore specify the ISO code for each country in this field if you use Edythe ISO code also controls which additional specifications are relevant for a company code. You can always only enter the additional details that are relevant for the company code country or for all countries. The assignment to the country takes place via the ISO code.Procedure: Enter the ISO code for each country. This is important:If the country belongs to the European CommunityIf you exchange information via EDIIf company-code specific additional specifications are to be limited by country. |
| Company Code | The company code is an organizational unit within financial accounting. |
| Value of Free Attribute (Char4) |  |
| Value of Free Attribute (Char4) |  |
| Free Attribute (Char20) |  |
| Free Attribute (Date) |  |
| Valid From | Raw Exposure Valid From dateDetermines the validity of a raw exposure and the exposure position flows created on release of a raw exposure. |
| Release Status | Release status of a raw exposurePossible values include:Editable - This means the raw exposure can be edited.Initiated - This means the release workflow for a raw exposure has been initiated.Released- This means the raw exposure has been released to exposure positions. |
| External Item Number | This field can be used to link the line items in raw exposures with line items in operational documents such as sales orders or purchase orders. |
| Profit Center | Along with controlling area, this key uniquely identifies a profit center. |
| Exposure Amount | Exposure amount |
| Exposure Amount Currency | Currency of the exposure amount |
| ISO Code Exp.Amt.Curr | Currency key (standard worldwide).Procedure: Enter the ISO code if you do not already use the global standard currency key as the currency key.If you use the EDI application, the ISO code is used for exchanging information. |
| Target Currency of Raw Exposure | Target currency of a raw exposure line itemUse: In an FX line item, the target currency is the risk currency. |
| ISO Code (Target Curr) | Currency key (standard worldwide).Procedure: Enter the ISO code if you do not already use the global standard currency key as the currency key. If you use the EDI application, the ISO code is used for exchanging information. |
| Period | Example: Planning PeriodsJanuaryFebruaryMarchApril |
| Planning Year | The planning period together with the planning year defines the period when the raw exposure expires.Use: Enter the year when the raw exposure expires. |
| Exposure Due Date | Date on which the raw exposure is due or expires.Use: This date is sent to Hedge Accounting for Exposures as the end date or the expiry date of the exposure. This field cannot be edited if the due date is added as a differentiating parameter to the exposure position type. |
| Free Attribute (Char20) |  |
| Free Attribute (Char20) |  |
| Free Attribute (Char20) |  |
| Free Attribute (Char20) |  |
| Value of Free Attribute (Char10) |  |
| Value of Free Attribute (Char10) |  |
| Value of Free Attribute (Char4) |  |
| Free Attribute (Date) |  |
| External Item ID | External item IDUse: This field can link the line items in raw exposures with line items in operational documents (such as sales orders or purchase orders). |
| Portfolio | A portfolio is an organizational element to group together various treasury transactions for reporting purposes. |
| Cost Center | Key uniquely identifying a cost center. |
| Business Area | Key identifying a business area. |
| WBS Element | Key identifying a WBS element. |
| Segment | Segment for Segmental Reporting |
| On Behalf of Company Code | When you create a financial transaction on behalf of another company code, you can enter the company code on the Administration tab in the financial transaction data. Additionally, in Exposure Management 2.0, this attribute can be filled for raw exposure line items, and can be used as a differentiation criterion for exposure positions. Within a hedging area, you can use this attribute as a differentiation criterion for the analysis items.Example: Within a group of companies, the corporate headquarters and the affiliated companies have different company codes. When the corporate headquarters hedges on behalf of one of the affiliated companies, this can be visualized by entering the company code of the affiliated company on the Administration tab page in the financial transaction data of the hedging instrument. In addition, you add the relevant company code to the raw exposure line items and use it as a differentiation criterion for exposure positions and in the hedging area. |

#### Sample Data for Import Raw Exposures

You may be able to download an Excel temple with four records of sample data in it, depending on the document format.

If the Excel template is available for you, you should see the [link](https://help.sap.com/docs/SAP_S4HANA_CLOUD/e5ec5859d8e54df98492d80564a734c0/3b6e1b283ba3418ebee02820889bcb0c.html?version=2508.500) to download it here.

If you do not see the link, the document you are using does not support the Excel template download. In that case, create an Excel template using the instructions and sample data below.

To fit the following table in this document, the table is transposed. Copy the data (except for the Field, Record 1, Record 2 row) into Excel and transpose the columns and rows to create your importable template file. Ensure that you renamed the spreadsheet tab to Main.

Pay attention to the number type and text type columns while creating your template.

| Field | Record 1 | Record 2 | Record 3 | Record 4 |
| --- | --- | --- | --- | --- |
| External Document Number | 2021 | 2022 | 2023 | 2024 |
| Exposure Origin | ABR | ABR | ABR | ABR |
| Logical System | 099TTUG | 099TTUG | 099TTUG | 099TTUG |
| Exposure Activity Type | YFXO | YFXO | YFXO | YFXO |
| Exposure Category of Raw Exposure | 01 | 01 | 01 | 01 |
| Country/Region Key |  |  |  |  |
| Country/Region ISO Code |  |  |  |  |
| Company Code | 1310 | 1310 | 1310 | 1310 |
| Value of Free Attribute (Char4) | FX | FX | FX | FX |
| Value of Free Attribute (Char4) | OUT | OUT | OUT | OUT |
| Free Attribute (Char20) |  |  |  |  |
| Free Attribute (Date) |  |  |  |  |
| Valid From | 8/30/2016 | 8/30/2016 | 8/30/2016 | 8/30/2016 |
| Release Status |  |  |  |  |
| External Item Number | 1 | 2 | 1 | 2 |
| Profit Center |  |  |  |  |
| Exposure Amount | 5,000,000.00 | 5,000,000.00 | 10,000.00 | 10,000.00 |
| Exposure Amount Currency | USD | USD | USD | USD |
| ISO Code Exp.Amt.Curr |  |  |  |  |
| Target Currency of Raw Exposure | EUR | EUR | EUR | EUR |
| ISO Code ( Target Curr) |  |  |  |  |
| Period | M08 | M08 | M08 | M08 |
| Planning Year | 2017 | 2017 | 2017 | 2017 |
| Exposure Due Date | 8/30/2017 | 8/30/2017 | 8/30/2017 | 8/30/2017 |
| Free Attribute (Char20) |  |  |  |  |
| Free Attribute (Char20) |  |  |  |  |
| Free Attribute (Char20) |  |  |  |  |
| Free Attribute (Char20) |  |  |  |  |
| Value of Free Attribute (Char10) |  |  |  |  |
| Value of Free Attribute (Char10) |  |  |  |  |
| Value of Free Attribute (Char4) |  |  |  |  |
| Free Attribute (Date) |  |  |  |  |
| External Item ID | 1 | 2 | 1 | 2 |
| Portfolio | Y000 | Y000 | Y000 | Y000 |
| Cost Center |  |  |  |  |
| Business Area |  |  |  |  |
| WBS Element |  |  |  |  |
| Segment |  |  |  |  |
| On Behalf of Company Code |  |  |  |  |

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

With SAP S/4HANA, a new output management approach is in place. By design, the new output management includes cloud qualities such as extensibility enablement, multitenancy enablement, and modification-free configuration. Therefore, the complete configuration differs from the configuration that is used when output management is based on NAST. The configuration is based on BRF+, which is accessible for customers. In SAP S/4HANA, the target architecture is based on Adobe Document Server and Adobe Forms only. For the form determination rules (along with other output parameters), BRF+ functionality is used (in this sense, in combination with the message determination).

For TRM, SAP has predelivered the Treasury and Risk Management application object type. All the predelivered output determination rules are maintained under this application object type. SAP provides several apps to allow you to easily manage your output.

#### Output Parameter Determination

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you manage the determination rules for the output. Under Treasury and Risk Management, you have the following determination steps:

| Determination Step | Description |
| --- | --- |
| Output Type | SAP predelivers the necessary configurations. Do not change this setting. |
| Receiver | SAP predelivers the necessary configurations. Do not change this setting. |
| Channel | SAP predelivers the necessary configurations. Do not change this setting. |
| Printer Settings | SAP predelivers the necessary configurations. You can change this setting. |
| E-mail Recipient | Maintain e-Email recipients for outgoing correspondence objects in the e-mail channel. This setting overwrites the e-mail address in Business partner master data. |
| E-mail Settings | Specify the e-mail template and the sender e-mail address in this step. SAP predelivers e-mail templates. To create your own, use the Maintain Email Template app. |
| Form Template | Specify the PDF form template and number of copies in this step. SAP predelivers PDF form templates. To create your own, use the Maintain Form Template app. |
| Output relevance | SAP has set all output types as output-relevant. Do not change this setting. |

The operations to change these settings are similar. This section describes the steps to change the e-mail recipients and sender's e-mail address as an example.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). | The Output Determination screen displays. |  |
| 3 | Display current e-mail recipients | Enter the following data and choose Enter:Show Rules for: Treasury and Risk Management CorrespondenceDetermination Step:<select Email Recipient>.Note By default, no e-mail recipients are maintained by SAP. | The default e-mail recipient rule displays. |  |
| 4 | Maintain e-mail recipient for internal counterparty | Enter the following data and choose Edit.Choose Insert New Row.Make the following entries:Output Type: TRM_DEAL_SLIPNote If necessary, you can search for this value via F4 help.Role: INEmail Type Code: To, CC, or BCCE-Mail Address: for example, <Email address>Note You can also add more condition columns by choosing Table Settings and making necessary changes. For example, you can add a BusPartner condition column to maintain different e-mail recipients for different business partners. | The internal recipient e-mail address is maintained. |  |
| 5 | Maintain e-mail recipient for external counterparty | Repeat the prior step to add a new row and enter the following data:Output Type: TRM_TRANSACTION_CONFIRMATIONRole: INEmail Type Code: To, CC, or BCCE-Mail Address: for example, <Email address> | The external recipient e-mail address is maintained. |  |
| 6 | Activate the e-mail addresses | Choose Activate.On the Confirmation Activation dialog box, choose Yes. | The system displays the message Objects saved and activated. The e-mail addresses are saved and activated. |  |
| 7 | Display e-mail settings for Sender e-mail address and e-mail template | Enter following data and choose Enter.Determination Step: Email Settings | The default e-mail settings are displayed. |  |
| 8 | Change e-mail settings for Sender e-mail address and e-mail template | Choose Edit. Make the following entries:Sender Email: EMAILNote To create an e-mail template, use the Maintain Email Template app. | E-mail settings are changed. |  |
| 9 | Activate the e-mail settings | Choose Activate.On the Confirmation Activation dialog box, choose Yes. | The system displays the message Objects saved and activated. E-mail settings are saved and activated. |  |

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
| 1 | Log on | Log onto the SAP Fiori launchpad as an Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Output Items (F2279). | The Manage Output Items (F2279) screen displays. |  |
| 3 | Enter filter criteria and execute the report | Make the following entries:Application Object Type: TRM_CORRESPONDENCE (see note)Note In the Application Object Type field, press F4. On the Application Object Type dialog box, in the Appl. Object Type field, press F4. On the Define Conditions: Appl. Object Type dialog box, make the following entries and choose +:First field: Appl. Object TypeSecond field: containsThird field: TRMChoose OK. On the Application Object Types dialog box, choose Go.Select the checkbox for TRM_CORRESPONDENCE and choose OK.Repeat these steps to add your transaction number as a filter in the Application Object ID column.Choose Go.Note When you enter the data in the input field, an input help automatically displays the possible entries for you. You can choose from the list instead of entering the entire word or phrase.Correspondence objects can have the following status:In PreparationCompletedIn pendingErrorIf you want to resend a correspondence object even it has completed status, you can select the correspondence object and choose Resend.Note If you want to check the detailed log , you can select the correspondence and choose Show Application Log. | The status of the output correspondence objects is listed. You can search for your transaction and check the status. |  |

#### Maintain Print Queues

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check the outgoing correspondence objects in the PRINT channel.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as an Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Maintain Print Queues (F1260) | The Maintain Print Queues (F1260)screen displays. |  |
| 3 | Display the status of the TRM Print queue | Scroll down and choose a TRM print queue (for example, TRM_DEFAULT). | The Print Queue screen displays. |  |
|  |  | Choose the line with the transaction number from previous steps to download a PDF file.Note By default, SAP provides the following print queue for TRM:TRM_DEFAULT | All the TRM outgoing correspondence objects in channel PRINT are displayed with latest status. |  |

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
| 1 | Log on | Log onto the SAP Fiori Launchpad as an Administrator. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Maintain Email Templates - Deprecated (F1306) | The Maintain Email Template screen displays. |  |
| 3 | Copy Predelivered Template to Customer Template | Choose Predelivered. | All predelivered e-mail templates are displayed. |  |
| 4 | Copy Predelivered Template to Customer Template | Locate the e-mail template to copy, for example, FTR_CORR_EMAIL_TEMPLATE_CNF.Select the radio button to the left of the template name and choose Copy. | The Copy TemplateFTR_CORR_EMAIL_TEMPLATE_CNF dialog box displays. |  |
| 5 |  | Make the following entries:Name: for example, TRM Transaction Confirmation Customer Email TemplateNote The new copied e-mail template uses YY1_ as a prefix. | The system displays the message Template has been copied. |  |
| 6 | Change Customer E-mail Template | Locate the copied e-mail template, for example, YY1_FTR_CORR_EMAIL_TEMPLATE_CN. Choose the template. | The Email Template screen displays. |  |
| 7 | Change Customer E-mail Template | Choose Change Details. | The Change Template YY1_FTR_CORR_EMAIL_TEMPLATE_CN dialog box displays. |  |
| 8 | Change Customer E-mail Template | Make the following entries and choose Change Details:Description: TRM Transaction Confirmation Customer Email Template | The Email Template screen displays. |  |
| 9 | Change Customer E-mail Template | In the Available Languages subarea, choose a language version, for example, English. | The Email Template Content screen displays. |  |
| 10 | Change Customer E-mail Template | Adjust the e-mail subject and body accordingly, then choose Save.Note SAP has predefined variables which you can use in Email templates. You can choose Show Data Fields to display the variables list. | The customer Email template is adjusted successfully. |  |

#### Maintain Form Templates

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
| 1 | Log on | Log onto the SAP Fiori launchpad as an Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Maintain Form Templates (F1434) | The Maintain Form Templates (F1434) screen displays. |  |
| 3 | Download a Predelivered Form Template | Choose Predelivered.Scroll down and find one form template, for example, , | All predelivered form templates are displayed. |  |
| 4 | Download a Predelivered Form Template | Locate and choose a form template (for example, FDP_TRM_CONF_DE). | Details for the form template are displayed. |  |
| 5 | Download a Predelivered Form Template | Choose Download. On the Download Language dialog box, choose OK. | The form template is downloaded successfully. |  |
| 6 | Change the Customer Form Template File | Using Adobe LiveCycle Designer, adjust and save the form template.Note You must have Adobe LiveCycle Designer installed to edit the template. |  |  |
| 7 | Upload Customer Form Template File | Open Maintain Form Templates (F1434). | The Maintain Form Templates (F1434) screen displays. |  |
| 8 | Upload Customer Form Template File | Choose Customer Templates. |  |  |
| 9 | Upload Customer Form Template File | Choose New. | The Create Form Template dialog box displays. |  |
| 10 | Upload Customer Form Template File | Make the following entries and choose OK:Form Template Name: for example, CUST_TRM_CONF_DELanguage: for example, EnglishSelect Form Template File: choose Browse and choose the fileData Provider: for example, FDP_TR_CORR_SRVForm Type: Content | The customer form template is created successfully. |  |

### Accounting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes additional accounting-relevant activities.

#### Reverse Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you reverse the posted period end valuation for the deal (for example, if you have done the period end valuation with incorrect currency rates or incorrect evaluation type; this can result in incorrect accounting results that must be reversed).

Prerequisites

The period end valuation of the deal is posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Reverse Valuation (TPM2). | The Reverse Valuation (TPM2) screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Transactions: SelectedCompany code: for example, 3310Valuation Area: leave blank, or enter specific valuation are, for example, AE0Transaction: <transaction numbers for valuation to be reversed>Key Date for Valuation: for example, <the date on which the reversal should take place>Reasons for Reversal: for example 04 Other reasonsTest Run: Selected | The Display Positions to be Reversed screen displays. |  |
| 4 | Reverse Valuation for Test Run | Choose Reverse Valuation (TPM2). | The Reversal Log: Reversed Business Transactions screen displays. The system displays the message Valuation (test run) has been successfully reversed.Simulated reversal posting information are shown on this screen. No posting is created, because it is a test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until you return to the initial screen of this app.Change the following data and choose Execute:Test Run: Deselected | The Display Positions to be Reversed screen displays. |  |
| 6 | Reverse Valuation for Production Run | Choose Reverse Valuation (TPM2). | The Reversal Log: Reversed Business Transactions screen displays. The system displays the message Valuation has been successfully reversed.You can check the posting on this screen. The accounting document for reversal is created. |  |

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
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Transfer Account Assignment Reference (TPM28). | The Execute Account Assignment Reference Transfer screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Trans MM, Forex, OTC Derivatives: SelectedCompany code: for example, 3310Valuation Area: leave blank, or enter a specific valuation area, for example, AE0Transaction: <transaction numbers for account assignment reference to be transferred>Posting Date: <the date on which account assignment reference transfer should take place>New Acct Assignment Ref.: <choose a new account assignment reference>Test Run: Selected | The Display Positions to be Transferred screen displays. |  |
| 4 | Execute Transfer for Test Run | Choose Carry out transfer posting. | The Posting Log: Posted Business Transactions screen displays. The system displays the message Transfer posting (in test run) was successful.Simulated postings for account assignment reference transfer are shown on this screen. No posting is created, because it is test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until you return to the initial screen of this app.Change the following data and choose Execute:Test Run: Deselected | The Display Positions to be Transferred screen displays. |  |
| 6 | Execute Transfer for Production Run | Choose Carry out transfer posting. | The Posting Log: Posted Business Transactions screen displays. The system displays the message Transfer posting was successful.The postings for account assignment reference transfer are shown on this screen. Accounting documents are created. |  |

#### Reverse Account Assignment Reference Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To reverse the account assignment reference transfer after the transfer is updated, you can use the Reverse Account Assignment Reference Transfer (TPM29) app.

Prerequisites

The account assignment reference transfer is posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reverse Account Assignment Reference Transfer (TPM29). | The Reverse Account Assignment Reference Transfer screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | Make the following entries and choose Execute:OTC Transactions Money Market, Forex, Derivatives:SelectedCompany code: for example, 3310Valuation Area: leave blankTransaction: <transaction numbers for account assignment reference transfer to be reversed>Reasons for Reversal: for example, 04 Other reasonsTest Run: Selected | The Display Positions to be Reversed screen displays. |  |
| 4 | Reverse Transfer for Test Run | Select the items to be reversed and choose Cancel transfer. | The Reversal Log: Reversed Business Transactions screen displays. The system displays the message Transfers reversed successfully (test run).Simulated postings for reversal of account assignment reference transfer are displayed. No posting is created because you performed a test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until you return to the initial screen of this app.Change the following data and choose Execute:Test Run: Deselected | The Display Positions to be Reversed screen displays. |  |
| 6 | Reverse Transfer for Production Run | Select the items to be reversed and choose Cancel transfer. | The Reversal Log: Reversed Business Transactions screen displays. The system displays the message Transfers reversed successfully.Postings for reversal of account assignment reference transfer are shown. Accounting documents are created. |  |

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

In this activity, you change the adjustment of interest rate.

Prerequisites

The adjustment of interest rate is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Change Adjustment - Rates/Prices (TI11) | The Change Last Interest/Price Adjustment screen displays. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Enter:Company Code: for example, 3310Transaction: <transaction number with Adjust Interest Rate created in previous steps> | The Change Interest Rate/Price Adjustment screen displays. |  |
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

In this activity, you display adjustment of interest rate.

Prerequisites

The adjustment of interest rate is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Adjustment - Rates/Prices (TI12) | The Display Interest/Price Adjustment screen displays. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Enter:Company Code: for example, 3310Transaction: <transaction number with Adjust Interest Rate created in previous steps> | The Display Interest/Price Adjustment screen displays. |  |

#### Reverse Automatic Adjustments (Interest Rates/Prices)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you reverse the automatic adjustment of interest rate.

Prerequisites

The automatic adjustment of interest rate is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Reverse Automatic Adjustments - Rates/Prices (TJ05_REV) | The Reverse Automatic Interest Rate or Price Adjustment screen displays. |  |
| 3 | Enter Reverse Criteria | Enter the following data and choose Execute:Company Code: for example, 3310Fixing Date: for example, <Last automatic Adjustment Date>Test Run: Deselected | The Reverse result displays. |  |

#### Reverse Adjustment (Interest Rates/Prices)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you reverse the manual adjustment of interest rate.

Prerequisites

The manual adjustment of interest rate has been created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Reverse Adjustment - Rates/Prices (TI37) | The Reverse Last Interest/Price Adjustment screen displays. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Enter:Company Code: for example, 3310Transaction: <transaction number with Adjust Interest Rate created in previous steps> | The Reverse Last Interest/Price Adjustment screen displays. |  |
| 4 | Reverse Interest Rate Adjustment | Choose Save: | The manual rate/price adjustment is reversed. |  |

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
| 2 | Access the SAP Fiori app | Open Manage Market Data Shift (JBR0). | The Edit Market Data Shifts screen displays. |  |
| 3 | Enter Market Data Shifts Name | Enter the following data and choose Create:Market Data Shift: for example, 1 | The Define Market Data Shifts screen displays. |  |
| 4 | Define Market Data Shift | Enter the following data and choose the Yield Curves tab:Short Name: for example, Market Data Shift 0001 |  |  |
| 5 | Maintain Yield Curves of Market Data Shift | Choose Insert Row.Make the following entries and choose Save:Short Name: for example, Euro Depo ShiftCurrency: for example, AEDYC. Type: for example, 0001Ref.Int.Rate: for example, EURM01EURPercentage: for example, 2 | The market data shift is saved. |  |

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

#### Defining Report Layout for Calculate Market Risk Key Figures

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define the report layout for market risk key figures report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Calculate Market Risk Key Figures (AISGENKF). | The Calculate Market Risk Key Figures screen displays. |  |
| 3 | Access Report Layout Definition screen | On the Calculate Market Risk Key Figures screen, enter the evaluation currency and evaluation type, and choose Define Report Layout. | The ChangeView "Key Figure Layout": Overview screen displays. | . |
| 4 | New Entries | Choose New Entries. |  |  |
| 5 | Create Layout-ID entries | In the Key Figure Layout form, make the following entries and choose Save:ROW1Layout-ID: for example, Y01Short Name: for example, NPV/BPV/DurationLong Name: for example, NPV/BPV/DurationROW2Layout-ID: for example, Y02Short Name: for example, NPV + Market Data shiftsLong Name: for example, NPV + Market Data shifts | Two new entries are created. |  |
| 6 | Access Key Figures Maintain screen | Select the checkbox for Layout-ID Y01, then in the Dialog Structure pane, double-click Key Figures. | The Key Figures screen displays in the main area. |  |
| 7 | Maintain Key Figures of Layout | Choose New Entries. |  |  |
| 8 | Maintain Key Figures of Layout | In the Key Figures form, make the following entries and choose Save:Key Figure Name: for example, BARWERTPos. Area: for example, select this checkboxPH-Area: for example, select this checkboxKey Figure Category: for example, NPVShort Name: for example, NPVShift Rule: for example, 1 or Market Data Shift Rule you createdDecimal Places: for example, 0 | The ChangeView "Key Figure Layout": Overview screen displays. |  |
| 9 | Access Key Figures Maintain screen | Select the checkbox for Layout-ID Y02, then in the Dialog Structure pane, double-click Key Figures. | The ChangeView "Key Figure Layout": Overview screen displays. |  |
| 10 | Maintain Key Figures of Layout | Choose New Entries. |  |  |
| 11 | Maintain Key Figures of Layout | In the Key Figures form, make the following entries and choose Save:Key Figure Name: for example, NPVPos. Area: for example, select this checkboxPH-Area: for example, select this checkboxKey Figure Category: for example, NPVShort Name: for example, NPVShift Rule: for example, 1 or Market Data Shift Rule you createdDecimal Places: for example, 0 |  |  |

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
| 2 | Access the SAP Fiori app | Open Display Limit Overview (TBL3) | The Overview of Limits screen displays. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Execute:Limit Type: for example, Y01 to Y09Company Code: for example, 3310 | The Display Limits for Limit Types: Overview screen displays. |  |

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

Prerequisites

Create a partner 33537002 in advance by referring to the Create Business Partner for Treasury and Risk Management - MDS (22G) master data script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Change Counterparty - Financial Transaction (TRTM_CHG_PARTNER). | The Change Counterparty of a Financial Transaction screen displays. |  |
| 3 | Test Run | Make the following entries and choose Execute:Company Code: for example, 3310New Partner: for example, 33537002Change Effective From: enter the date from which the change will be effective. For example, <current date>Test Run: Selected | The Change Counterparty of a Financial Transaction screen displays with Test Run: List of Successfully Changed Financial TransactionsNote If the period specified included any non-working day, a message displays indicating the same. |  |
| 4 | Production Run | Choose Exit.Make the following entries and choose Execute:Test Run: Deselected | The Change Counterparty of a Financial Transaction screen displays with List of Successfully Changed Financial Transactions |  |

#### Display Financial Transactions With Changed Counterparty

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
| 2 | Access the SAP Fiori app | Open Display Transactions - Changed Counterparty (TRTM_CHG_PARTNER_DIS). | The Display Financial Transactions With Changed Counterparty screen displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Execute:Company Code: for example, 3310 | The Display Financial Transactions With Changed Counterparty screen displays with List of Financial Transactions with Changed Partner. |  |

### Analytical Apps

#### Define Display Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step provides instructions on changing the display order for currency pairs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Risk Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Define Display Order - Currency Pairs (FXM_CURR_DISP). | The Display View "Define Display Order for Currency Pairs": Overview screen displays. |  |
| 3 | Maintain Key Figure Groups | Choose Edit. |  |  |
| 4 | Maintain Key Figure Groups | Locate the entries to change. Make the changes and choose Save.Note For example, find the following currency pairs, then change the Display Order column.Record 1Leading Currency:AEDFollowing Currency:USDDisplay Order: 10Record 2Leading Currency:AEDFollowing Currency:BRLDisplay Order: 20 | The data is saved. |  |

#### Analytical Apps

Purpose

This step provides instructions on usage of some SAP Fiori Analytical apps for Treasury & Risk Management.

Procedure

For more information, see the SAP Fiori Analytical Apps for Treasury and Risk Management (1MN) test script.

### FX Netting

The FX Netting function lets you group together transactions from the Foreign Exchange areas and pay them collectively. This can simplify payment processing. Situations happen where several financial transactions must be paid collectively, especially in the case of transactions with business partners that are not house banks (payments must be exchanged).

When you roll over an FX Forward transaction, SAP creates two transactions. One is the netting transaction to offset the original transaction and the other one is the new rollover transaction with new value date and conditions. A netting group can be created for the original FX Forward transaction and the netting transaction.

In this section, you create an FX Forward transaction, then roll over the transaction. You then create a netting group for the original FX Forward transaction and the netting transaction. Afterward, you process all outgoing and incoming payment requests in the netting group. The outgoing payments and incoming payments balance out to zero.

|  |
| --- |
| Note When doing Rollover or Premature Settlement for an FX transaction, you also have the option to adjust the exchange rate of the netting transaction according to your business requirement. In such case, the outgoing payments and incoming payments will not balance out to zero. |

#### Create a FX Forward Transaction

Purpose

In this activity, you create a Foreign Exchange Forward transaction for hedging or non-hedging purpose.

Procedure

Perform the following step in the Foreign Currency Risk Management (1X1) test script to create an FX Forward Transaction.

- Create FX Spot/Forward (TX01)

|  |
| --- |
| NoteYou must create an FX Forward Transaction (transaction type 102).For Value date, enter Current Date + 1 Month.Make a note of the transaction number: __________ |

#### Manual Settlement

Purpose

The TRM transactions must be settled before further processing.

Procedure

Perform the following steps in the Foreign Currency Risk Management (1X1) test script:

- Set Settlement Status (Manual)

#### Roll Over the FX Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When rolling over a FX forward transaction, SAP automatically creates a netting transaction to offset the original FX forward transaction. In this step, you roll over the FX transaction you just created and settled in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Parameters | Make the following entries and choose Execute:Company Code: 3310Transaction: Transaction number from previous step | The transaction is displayed on the screen. |  |
| 4 | Roll Over the Transaction | Select the checkbox (first column) and choose Roll Over. | The Rollover on Previous Basis: Structure screen displays. |  |
| 5 | Roll Over the Transaction | Make the following entries and choose Save:1st Transaction:Rate: For example, 1.2Value Date: Current Date + 2 MonthsNote You may also adjust the rate of the second transaction (netting) according to your business requirement. | The following message is displayed:Transactions 100000000XXXX and 100000000XXXX were created and transaction 1010/100000000XXXX was settled.NoteThe transaction types of these 2 transactions are 104 Roll Over and 103 Netting.Make a note of the two transaction numbers: __________ __________ |  |

#### Edit Payment Details of the FX Transactions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

For FX netting function to work properly, you must set the Generate Payment Request checkbox for both the outgoing and incoming payments for the FX transactions.

Procedure

Table 11: Change Payment Details for Original FX Forward Transaction

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter parameters in the initial screen | Make the following entries and choose Go:Company Code: 3310Transaction: Three transaction numbers created in previous steps | The transactions are displayed on the screen. |  |
| 4 | Change the payment details setting for the original FX transaction | Scroll to the right to locate the Transaction Type column.Select the checkbox of the row with Transaction Type 102 and choose Edit. | The Change Forex Transaction: Structure screen displays. |  |
| 5 | Change the payment details setting for the original FX transaction | Choose Payment Details. | The Change Forex Transaction: Payment Details screen is displayed. |  |
| 6 | Change the payment details setting for the original FX transaction | Select the checkbox for the row with the + sign and choose Payment Details. |  |  |
| 7 | Change the payment details setting for the original FX transaction | Make the following entries and choose Save:Payment Request: <select>Payer/Payee: 33537001Payment Methods: FPartner Bank: USD1 | The system displays the following message: Forex transaction saved under number 100000000XXXX. |  |

Table 12: Change Payment Details for FX Netting Transaction

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Parameters | Make the following entries and choose Go:Company Code: 3310Transaction: <three transaction numbers created in previous steps> | The transactions are displayed on the screen. |  |
| 4 | Change Payment Details for Netted FX Transaction | Scroll to the right to locate the Transaction Type column.Select the checkbox of the row with Transaction Type 103 and choose Edit. | The Change Forex Transaction: Structure screen displays. |  |
| 5 | Change Payment Details for Netted FX Transaction | Choose Payment Details. | The Change Forex Transaction: Payment Details screen displays. |  |
| 6 | Change Payment Details for Netted FX Transaction | Select the checkbox for the row with the + sign and choose Payment Details. |  |  |
| 7 | Change Payment Details for Netted FX Transaction | Make the following entries and choose Save:Payment Request: <select>Payer/Payee: 33537001Payment Methods: TPartner Bank: AED1 | The system displays the following message: Forex transaction saved under number 100000000XXXX. |  |

#### Propose Netting List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once you have created the FX transactions to be netted, you may create the netting group via the Create Netting (TBR1) app. SAP Treasury and Risk Management can also automatically propose the netting list for FX transactions. In this step, you create the netting list. You may also display, undo, or change the netting group after creation. The following apps are relevant for FX Netting:

- Create Netting (TBR1)
- Change Netting (TBR2)
- Display Netting (TBR3)
- Undo Netting (TBR4)
- Display Netting Proposals (TBR5)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Display Netting Proposals (TBR5). | The Proposal List for Netting view is displayed. |  |
| 3 | Enter parameters in the initial view | Make the following entries and choose Execute:Company Code: 3310Transaction: Three transaction numbers created in previous step | The Proposal List for Netting view displays the transactions.Note The transactions are grouped into two groups. |  |
| 4 | Create the Netting List | The two transactions with transaction types 102 and 103 are grouped together.Select the two checkboxes before the two transactions under the first group, then choose Save. | The Proposal List for Netting view displays the message Netting X created.Note Make a note of the Netting Number: __________ |  |

#### Display Netting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once a netting number is created, you may display, change, or undo the netting number if necessary. In this step, you display the netting group created in the prior step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Display Netting (TBR3). | The Display Netting: Initial Screen is displayed. |  |
| 3 | Enter parameters in the initial screen | Make the following entries and choose Execute:Netting: Netting number from previous step | The Display Netting: Data screen displays the netting number.Note Make a note of the two transaction numbers: __________ __________ |  |

#### Generate Payment Request for the Netted Transactions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you generate the payment requests for the netted transactions.

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Make the following entries and choose Execute:Foreign Exchange: SelectedCompany code: 3310Transaction: Two transaction numbers from previous stepUp to and Including Due Date: Date to post flow of financial transaction, for example, Current date + 1 monthTest Run: SelectedPay Only: Selected | In the Information Overview screen, both Payment Log and Messages have green light status. |  |
| 4 | Production Run | Choose Back. | The Fix, Pay and Post Flows screen is displayed. |  |
| 5 | Production Run | Change the following data and choose Execute:Test Run: Deselected | In the Information Overview screen, both Payment Log and Messages have green light status. |  |
| 6 | Payment Log | Choose Payment Log. | The Payment Log screen displays the keys. Make a note of the payment request key numbers: __________ __________ __________ |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | Enter the following data, and choose Execute:Foreign Exchange: <select>Company Code: for example, 3310Transaction: <Two transaction numbers from previous step>Up to and Including Due Date: Date to post flow of financial transaction, for example, <Current date + 1 month>Test Run: <select> | In the Information Overview screen, both Payment Log and Messages have green light status. |  |
| 4 | Production Run | Choose Back. | The Fix and Pay Flows view displays. |  |
| 5 | Production Run | Change the following data, and choose Execute:Test Run: <deselect> | In the Information Overview screen, both Payment Log and Messages have green light status. |  |
| 6 | Payment Log | Choose Payment Log. | The Payment Log screen displays the keys.Make a note of the payment request key numbers: __________ |  |

#### Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you start the payment program for payment requests. The payment program for payment requests is an additional automatic payment option in the SAP system. Unlike the standard payment program, the payments are not based on open items (vendor/customer items) but on payment requests.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests (F111) screen displays. |  |
| 3 | Enter Run Date and Identification | Enter the following data and choose Parameters:Run Date: for example, Current dateIdentification: for example, TRM01Note If the system displays the message Parameters have been entered, use another identification (such as TRM02). | The Automatic Payment Transactions: Parameters screen displays. |  |
| 4 | Enter Parameters | Enter the following data and choose Dynamic selections:Posting Date: for example, Current dateNext payment run on: for example, Current date+2 monthsCompany Code: for example, 3310Payment Methods: for example, TF | The Free Selection for payment run dialog box displays. |  |
| 5 | Enter Parameters | Enter the following data and choose Save:Key Number: All key numbers from previous stepNote Include all the payment request key numbers in one payment run. If you do not, the outgoing and incoming payments do not balance out to zero. |  |  |
| 6 | Enter Parameters | Choose Additional Log. | The Additional Log dialog box displays. |  |
| 7 | Enter Parameters | Enter the following data and choose Continue:Payment method selection in all cases: SelectedLine items of the payment documents: SelectedDue date check: SelectedNote If the system displays the message Log created for all accounts, choose Continue. | The Automatic Payment Transactions: Parameters screen displays. |  |
| 8 | Enter Parameters | Choose Save. | The system displays the message Parameters have been entered displays. |  |
| 9 | Schedule Proposal | Choose Proposal. | The Schedule Proposal dialog box displays. |  |
| 10 | Schedule Proposal | Select Start Immediat and choose Schedule Job. | The system displays the message Proposal is running with a yellow traffic light status. |  |
| 11 | Schedule Proposal | Choose Status, until the system displays the message Payment proposal has been created with green traffic light staus. | The payment proposal is generated.NOTEIf you choose Display proposal log, you should see the message Following payment orders balance out to zero and are cleared. |  |
| 12 | Schedule Payment | Choose Pmnt run. | The Schedule Payment dialog box displays. |  |
| 13 | Schedule Payment | Select Start Immediat., select Create Payment Medium, and choose Schedule Job. | The system displays the message Payment run is running with yellow traffic light status. |  |
| 14 | Schedule Payment | Choose Status, until the system displays the message Payment run has been carried out with green traffic light status. | The payment document is created.If Bank Communication Management (BCM) is not implemented in your system, the payment medium is created if it uses PMW format. To check the log, choose Display payment log.If BCM is implemented in your system, in Display payment log, if you see the message Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media, a BCM batch should be created after payment run. For more information, see the next test step.NOTEIf you check the payment run log, you should see the message Document 10000XXXX company code XXXX currency XXX payment method.The Automatic Payment Transactions for Payment Requests (F111) screen displays. |  |
| 15 | Cross-Payment Run Payment Media (Create BCM Batch) | Choose Menu > Environment > Payment medium > Cross-Payment Run Payment Medium > Create Payment Medium . | The Creation of Cross-Payment Run Payment Media screen displays. |  |
| 16 | Cross-Payment Run Payment Media (Create BCM Batch) | Enter the following data and choose Execute:Run Date: for example, Current dateIdentification: for example, TRM01R | The Creation of Cross-Payment Run Payment Media dialog box displays a message Collector XX/XX/20XX XXXXXX was created or updated. The BCM batch is created.A batch may require additional approvals before the payment medium is finally created. For more information, see the Advanced Cash Operations(J78) test script. |  |

#### Send Payment Medium File

Purpose

In this activity, you send the payment medium file to your house bank to facilitate the payment.

Procedure

If Bank Communication Management (BCM) is not implemented in your system, the payment medium file will be generated upon completion of the payment run in the previous step, provided that the relevant payment method uses the PMW format.

If BCM is implemented in your system, additional approvals may be required for a BCM batch before the payment medium file can be generated. For the approval process, please refer to the section Outgoing Payment with BCM Approval Process in the test script Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/J78)).

After payment medium file is created, there are two ways for sending the payment medium file to your house bank:

- If Multi-Bank Connectivity (MBC) is not enabled, please use app Manage Payment Media (F1868) to check and download the payment medium file, and send the file to the bank via the previously agreed-upon method. Further details are provided in test script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/1EG)).
- If MBC is enabled and the relevant PMW format uses the alternative format type designated for MBC, then the payment medium file can be automatically sent to MBC. Bank will then retrieve the payment medium file from MBC and execute the payment. Further details are provided in test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/16R)).

### Copy Existing Transaction

The Copy Existing Transaction function lets you create a new transaction by duplicating existing transaction with some limited modification, for example FX Spot Rates, Traded Amount and Value Date.

Duplicate transaction only applies to product categories 600, and doesn’t support FX Swap.

#### Copy FX Spot/Forward

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a Foreign Exchange Spot or Forward transaction by copying an existing FX Spot/Forward.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Go:Company Code: for example, 3310Transaction: <FX Spot/Forward Transaction Number created in previous step> | The transaction is displayed on the screen. |  |
| 4 | Settle the TRM Transaction | Select the checkbox at the beginning of the transaction line and choose Copy. | The Copy Forex Transaction: Structure screen displays with the transaction data. |  |
| 5 | Update data | Update data and choose the Administr. tab:Rate: For example, AED/USD 1.2Traded Amt: For example, USD0.5MValue Date: +2Note You can enter a Value Date greater than +2 days for forward transactions no matter existing transaction is Spot or Forward | The Administr. tab displays. |  |
| 6 | Enter Data in Administration tab | Enter data and choose Save:Hdg Classific.: For example: Y0Risk Mitigation: <select> | Transaction is saved and a transaction number is generated. |  |

#### Copy Nondeliverable Forward

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a foreign exchange nondeliverable-forward transaction by copying an existing NDF.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Go:Company Code: for example, 3310Transaction: <FX NDF Transaction Number created in previous step> | The transaction is displayed on the screen. |  |
| 4 | Settle the TRM Transaction | Select the checkbox at the beginning of the transaction line and choose Copy. | The Copy Forex Transaction: Structure screen displays with the transaction data. |  |
| 5 | Update data | Update data and choose the Administr. tab:Rate: For example, AED/BRL3.3Traded Amt: For example, BRL10MValue Date: ++6+2Fixing Date: ++6Settlement Currency: AED | The Administr. tab displays. |  |
| 6 | Enter Data in Administration tab | Enter data and choose Save:Hdg Classific.: For example, Y0Risk Mitigation: <Select> | Transaction is saved and a transaction number is generated. |  |

### Termination of Foreign Exchange Transaction

#### Create, Submit and Release Termination Request for a Forward

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In some cases, for example, when a long FX forward transaction (or FX spot, FX Swap, NDF) is over-hedged, you may need to terminate the transaction after aligning with your counterparty.

In this step, in the hedge management cockpit you select the FX transaction that shall be terminated, create and then submit a termination request. Then the request will be released.

Prerequisites

You have created and settled an FX forward transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Hedge Management Cockpit (TOENE) |  |  |
| 3 | Enter Selection Criteria | Make the following entries, and choose Start:Hedging Area: For example, AE0001Layout ID: 2R_TQ_CHNote Please refer to step [Generate Hedge Request](#unique_43) [page ] 69 for details | The Hedge Management Cockpit for Hedging Area AE0001 is displayed with Net Hedges |  |
| 4 | Create Termination Request | Double click on key figure Net Hedges in the period of the value date of the forward transaction you just created as prerequisite.Select the transaction you just created, click Hedge Request and choose Termination Request in the dropdown list | The Create Hedge Request screen is displayed. |  |
| 5 | Submit Termination Request | Enter description for hedge request: terminate forwardEnter the following data on the General tab, and choose Submit:Hedge Request Reason: Choose S003 Overhedge Processing - TerminationNote Overruling not allowed | Terminate Request is submitted with termination request ID.Remember Note down the ID. |  |
| 6 | Access the SAP Fiori app | Open Process Hedge Requests (TOEHREQO) | The Process Hedge Requests screen is displayed. |  |
| 7 | Enter Selection Criteria | Enter the following data, and choose Start:Hedging Area: for example, AE0001 | Hedge requests that match the filter criteria are displayed. |  |
| 8 | Release Termination Request | Select the row of the Termination Request you just submitted and choose Process and then select Release from the dropdown list. | Log is displayed that the termination request was released. |  |

#### Terminate Foreign Exchange Forward

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you terminate a FX forward transaction in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Financial Transactions (F6157) | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Go:Company Code: for example, 3310Transaction: <the FX transaction number to be terminated> | A list of FX transactions is displayed on the screen. |  |
| 4 | Terminate the Transaction | Select the checkbox of the transaction to be terminated, and choose Terminate. | The Terminate Forex Transaction: Structure screen is displayed. |  |
| 5 | Save the Termination | On the Terminate Forex Transaction: Structure screen, the value of field Activity in header is 3 - Termination.Enter the following data in the Termination sub-area:Date: <the termination date, it should between contract date and value date>Note the termination date should between posting date and value date if period end valuation and posting has run.Payment Date: for example, <termination data + 2 days>Entry Type: for example, RateRate: for example, 1.16Choose Save.If the Document lines: Display messages dialogue box is displayed, choose Continue (Enter). | The payment amount for termination is calculated and the transaction is saved with status Termination. |  |
| 6 | Access the SAP Fiori App | Open Process Hedge Requests (TOEHREQO) | The Process Hedge Requests screen is displayed. |  |
| 7 | Enter Selection Criteria | Enter the following data, and choose Start.:Hedging Area: for example, AE0001 | hedge requests that match the filter criteria are displayed. |  |
| 8 | Check Termination Request Status | Status of the termination request is Completed. |  |  |

#### Set Termination Settlement Status for Foreign Exchange Forward

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After you terminate an FX forward transaction in the system, you need to change its status to Termination Settlement before you can create postings for termination flow. Usually you should set the status after you receive the incoming confirmation about the termination from your counterparty.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Financial Transactions (F6157) | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Go:Company Code: for example, 3310Transaction: <the FX transaction number in status Termination> | A list of FX transactions is displayed on the screen. |  |
| 4 | Settle the Termination | Select the checkbox of the transaction to be settled, and choose Settle. | The Settle Forex Transaction: Structure screen is displayed. |  |
| 5 | Save the Termination Settlement | On the Settle Forex Transaction: Structure screen, the value of field Activity in header is 4 - Termination Settlement.Choose Save.If the Document lines: Display messages dialogue is displayed, choose Continue (Enter). | The transaction is saved with status Termination Settlement. |  |

#### Post Flows for Termination

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Post operative flow and derived flows at payment date of termination.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1) | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Fix, Pay and Post Flows view, enter the following data, and choose Execute:Company Code: for example, 3310Transaction: <the FX transaction number terminated>Up to and Including Due Date: <the payment date of termination>Test Run: for example, <deselect this checkbox>Post All Valuation Areas: for example, Selected | The Information Overview dialog box is displayed. |  |
| 4 | Check Posting Log | In the Information Overview dialog box, choose Posting Log. | Posting journals are displayed. |  |

|  |
| --- |
| Note If termination results in outgoing payment with a payment request, please refer to Generate Payment Request for Mature Transaction and Process Payment Request. |

#### Create, Submit and Release Termination Request for Option

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In some cases, for example, if a long-run plain vanilla FX option or zero/low cost collar FX option is over-hedged, you may need to terminate it after aligning with your counterparty.

In this step, in the hedge management cockpit the risk manager selects the FX transaction which shall be terminated and creates a termination request and submits it. Then the request will be released.

Prerequisites

You have created and settled an FX option transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Hedge Management Cockpit (TOENE) |  |  |
| 3 | Enter Selection Criteria | Make the following entries, and choose Start:Hedging Area: For example, AE0001Layout ID: 2R_TQ_CHNote Please refer to step [Generate Hedge Request](#unique_43) [page ] 69 for details | The Hedge Management Cockpit for Hedging Area AE0001 is displayed with Net Hedges |  |
| 4 | Create Termination Request | Double click on key figure Net Hedges in the period of the value date of the option transaction you just created as prerequisite.Select the transaction you just created, click Hedge Request and choose Termination Request in the dropdown list | The Create Hedge Request screen is displayed. |  |
| 5 | Submit Termination Request | Enter description for edge request: terminate optionEnter the following data on the General tab, and choose Submit:Hedge Request Reason: Choose S003 Overhedge Processing - TerminationNote Overruling not allowed | Terminate Request is submitted with termination request ID.Remember Note down the ID. |  |
| 6 | Access the SAP Fiori app | Open Process Hedge Requests (TOEHREQO) | The Process Hedge Requests screen is displayed. |  |
| 7 | Enter Selection Criteria | Enter the following data, and choose Start:Hedging Area: for example, AE0001 | Hedge requests that match the filter criteria are displayed. |  |
| 8 | Release Termination Request | Select the row of the Termination Request you just submitted and choose Process and then select Release from the dropdown list. | Log is displayed that the termination request was released. |  |

#### Terminate Foreign Exchange Option

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you terminate a plain vanilla option, or one leg of the zero/low cost collar FX option. In case that both legs of zero/low cost collar FX option should be terminated, terminate them one by one.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Go:Company Code: for example, 3310Transaction: <the FX option transaction number to be terminated> | The list of FX Option transaction(s) is displayed on the screen. |  |
| 4 | Terminate the Transaction | Select the checkbox of the transaction to be terminated, and choose Terminate. | The Terminate OTC Option: Structure screen is displayed. |  |
| 5 | Save the Termination | On the Terminate OTC Option: Structure screen, the value of field Activity in header is 3 - Termination.Enter the following data in the Termination sub-area:Term.Date: <the termination date, it should bebetween contract date and Expiry date>Note the termination date should between posting date and value date if period end valuation and posting has run.Payment Date: for example, <termination data + 2 days>Amount: for example, -100Choose Save.If the Document lines: Display messages dialogue box is displayed, choose Continue (Enter). | The transaction is saved with status Termination. |  |
| 6 | Access the SAP Fiori App | Open Process Hedge Requests (TOEHREQO) | The Process Hedge Requests screen is displayed. |  |
| 7 | Enter Selection Criteria | Enter the following data, and choose Start.:Hedging Area: for example, AE0001 | hedge requests that match the filter criteria are displayed. |  |
| 8 | Check Termination Request Status | Status of the termination request is complete. |  |  |

#### Set Termination Settlement Status for Foreign Exchange Option

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once FX option transaction is terminated in the system, the status of transaction needs to be set to Termination Settlement before you can create postings for termination flow. Usually it is done after you receive the incoming confirmation about the termination from your counterparty.

In this step you settle the termination for a plain vanilla option, or one leg of the zero/low cost collar FX option. In case that both legs of zero/low cost collar FX option should be terminated, settle their termination one by one.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Go:Company Code: for example, 3310Transaction: <the FX option transaction number in status Termination> | The list of FX Option transaction(s) is displayed on the screen. |  |
| 4 | Settle the Termination | Select the checkbox of the transaction to be settled, and choose Settle. | The OTC Option: Settle Termination: Structure screen is displayed. |  |
| 5 | Save the Termination Settlement | On the OTC Option: Settle Termination: Structure screen, the value of field Activity in header is 4 - Termination Settlement.Choose Save.If the Document lines: Display messages dialogue box is displayed, choose Continue (Enter). | The transaction is saved with status Termination Settlement. |  |

#### Post Flows for Termination

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post operative flows and derived flows on the payment date of termination.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1) | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Fix, Pay and Post Flows view, enter the following data, and choose Execute:Company Code: for example, 1010Transaction: <the FX option transaction number(s) terminated>Up to and Including Due Date: <the payment date of termination>Test Run: for example, <deselect this checkbox>Post All Valuation Areas: for example, Selected | The Information Overview dialog box is displayed. |  |
| 4 | Check Posting Log | In the Information Overview dialog box, choose Posting Log. | Posting journals are displayed. |  |

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

Prerequisite

You have performed one of following sections of this test script:

- [Create Foreign Exchange Contract](#unique_111) [page ] 76
- [Create FX Option Contract](#unique_145) [page ] 141

NPV values need to be stored in advance of the valuation of Treasury positions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Simulate Period-End Closing (TPM_SIM_VAL). | The Simulate Period-End Closing screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Simulate Period-End Closing screen, enter the following data and choose Execute:Securities: <deselect this checkbox>OTC Transactions: <select this checkbox>Company Code: for example, 3310Valuation Area: for example, AE0Product Type: for example,60ATransaction Number: for example, <the transaction number created in the previous steps>Recalculate Outdated Sim.Val.: <deselect this checkbox>Note If you set this indicator, you can recalculate the outdated simulation results.Simulation Date: for example, <the current date>Key Date Valuation: <select this checkbox>Accrual/Deferral: <deselect this checkbox>Test Run: <select this checkbox> | The following message is displayed:Processed xx positions; xx successful, 0 failed.If Recalculate Outdated Simulation Results has been executed, the following message is displayed:xx simulated results deleted for key date, Processed xx positions; xx successful, 0 failed. |  |
| 4 | Execute Simulated Valuation | The dialog Message shows up, and choose Continue. | The Simulate Period-End Closing screen is displayed.You can check the simulated valuation information for local GAAP (valuation area AE0). Please note there is no simulated valuation created because it is test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back to the initial screen of this app.On the initial screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The Messages dialog box is displayed. |  |
| 6 | Execute Simulated Valuation for Production Run | The dialog Message shows up, and choose Continue. | The Simulate Period-End Closing screen is displayed.You can check the simulated valuation information for local GAAP (valuation area AE0). |  |

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
| 3 | Enter Selection Criteria for Test Run | On the Delete Results of Simulated Period-End Closing screen, enter the following data and choose Execute:Securities: <deselect this checkbox>OTC Transactions: <select this checkbox>Company Code: for example, 3310Valuation Area: leave blank, or enter specific valuation are, for example, AE0Product Type: for example,60ATransaction: for example, <the transaction number created in the previous steps>Simulation Date: for example, <the date on which the reversal should take place>Test Run: <select this checkbox> | The following message is displayed:xx simulated results deleted for key date (the date on which the reversal takes place). |  |
| 4 | Enter Selection Criteria for Production Run | Go back to the initial screen of this app.On the Delete Results of Simulated Period-End Closing screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The following message is displayed:XX simulated results deleted for key date (the date on which the reversal takes place). |  |

### Notification for Managing Financial Transactions

Situation handling is a framework provided by SAP S/4HANA that could increase the quality and efficiency of business processes by signaling exceptional information. Notification for Manage Financial Transactions (F6157) is enabled in Treasury and Risk Management. For example, if a foreign exchange option expires today and needs to be exercised, a notification will be sent. And if a trade finance contract is going to be expired, a notification will also be sent to the responsible person. There are several channels for notification, including the notification area on the SAP Fiori launchpad and email.

|  |
| --- |
| Note Make sure scope item Situation Handling (31N) is activated in your system before you use this functionality. |

To integrate with situation handling, Treasury and Risk Management provides the following:

- Situation Template: FIN_TRM_FINTRANS_PROCG
- Standard Team Category: FSCM_TRM

There are some customizing configurations needed. In SAP S/4HANA Cloud Public Edition, the following best practice customizing configurations are pre-delivered.

Table 13: Predefined Entities

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
| 5 | Maintain Responsibility Definitions | In the Responsibility Definitions section, enter the following data:Company Code: 3310Transaction Type: <leave blank>Product Type: 76APortfolio: <leave blank>Note You can create your own Portfolio in Manage Your Solution in S/4 HANA or Central Business Configuration in Central Business Configuration using the Define Portfolio configuration activity, so only the transaction assigned with your own portfolio will trigger the notification process. |  |  |
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
| 6 | Maintain Conditions | In the Conditions section, enter the following data:Set to Status: OpenSend Notification: <check>In the All Filters section, enter the following data:Company Code: 3310Product Type: 76ATransaction Type: 100Term End: NEXT14DAYS |  |  |
| 7 | Maintain Batch Job Scheduling | In the Batch Job Scheduling section, enter the following data:Time Zone: UTC+08Start Batch Job At: 12:00 |  |  |
| 8 | Maintain Situation Display | In the Situation Display section, you can insert variables if you want to receive detailed information for the notification and email.Enter the following data, and choose Insert Variables:Company Code: <COMPANYCODE>Product Type: <FINANCIALINSTRUMENTPRODUCTTYPE>Transaction: <FINANCIALTRANSACTION>Letter of Credit No.: <LETTEROFCREDIT>In the Notification section, make the following settings：Aggregate Notifications: <check>Resend Notifications: <check> |  |  |
| 9 | Check Recipients | In the Recipients section, make sure the team to receive notifications is listed in the Number of Teams. |  |  |
| 10 | Maintain Situation Monitoring | In the Situation Monitoring section, enter the following data, and choose Create:Monitor Instances: <select>Note Choose Yes in the dialog box to enable the situation type. | The situation type is created. |  |

#### Create a FX Option Contract

Purpose

In this step, you create a FX option contract.

Procedure

Refer to [Create FX Option Contract](#unique_145) [page ] 141 to create a FX option contract, and make sure the end term is within 14 days as of the current date.

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
| 2 | Access the SAP Fiori App | Open Manage Situation Types (F2947). | The Manage Situation Types screen is displayed. |  |
| 3 | Search the Standard Situation Template | Enter FIN_TRM_FINTRANS_PROCG in the search box and choose Go. | The Situation Template FIN_TRM_FINTRANS_PROCG shows up in the result. |  |
| 4 | Find the Situation Type | Select the template and switch to the Situation Types tab. | All the situation types under the TRM situation template is displayed. |  |
| 5 | Go to the Detail of the Situation Type | Select the situation type you create in [Enable Situation Types](#unique_225) [page ] 281, double click the selected situation type. | The Situation Type detail screen is displayed. |  |
| 6 | Trigger the Notification | Choose Trigger Now on the Situation Type detail screen. | The Information message The background process for creating situation instances has been triggered is displayed. |  |
| 7 | Check the Triggered Objects List in Situation Instances List | Check OK in the dialog box. | You will go to the Situation Instances screen.Check the letter of credit you created in [Create a FX Option Contract](#unique_226) [page ] 282 on the result list. |  |

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
- related-to :: [[05-treasury-and-cash-management/test-script-foreign-currency-risk-management-1x1-ae-sap-s-4hana-cloud-part-01]]
- related-to :: [[05-treasury-and-cash-management/foreign-currency-risk-management-group-ledger-ifrs-1x9-ae-777]]
- related-to :: [[05-treasury-and-cash-management/foreign-currency-risk-management-group-ledger-us-gaap-34d-ae-908]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1X1_S4CLD2608_BPD_EN_AE.docx` — lines 3642–6660 of the extracted text · extracted with `mammoth` · 475,815 chars in the whole document
