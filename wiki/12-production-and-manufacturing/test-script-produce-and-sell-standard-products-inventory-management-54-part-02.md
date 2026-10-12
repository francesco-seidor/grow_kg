---
id: 12-production-and-manufacturing/test-script-produce-and-sell-standard-products-inventory-management-54-part-02
title: "Test Script: Produce and Sell Standard Products – Inventory Management (54U_AE), SAP S/4HANA Cloud Public Edition (54U_S4CLD2608_BPD_EN_AE) — part 2 of 2"
description: "SAP S/4HANA Cloud 2608 test script 54U (AE), part 2: usage decision, outbound delivery, rejected stock, billing, customer/supplier payments."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/end-to-end-produce-and-sell]
aliases: []
keywords: [End-to-End Produce-and-Sell Scenarios, usage decision, outbound delivery, goods issue, proof of delivery, rejected material handling, blocked stock posting, delivery update, billing documents, incoming payments]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/54U_S4CLD2608_BPD_EN_AE.docx#lines-3192-3552"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1066
topic: 12-production-and-manufacturing/end-to-end-produce-and-sell
language: EN
part: 2/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Produce and Sell Standard Products – Inventory Management (54U_AE), SAP S/4HANA Cloud Public Edition (54U_S4CLD2608_BPD_EN_AE) — part 2 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/54U_S4CLD2608_BPD_EN_AE.docx`, part 2 of 2 (lines 3192–3552 of the extracted text), extracted with `mammoth`. Grouped under **End-to-End Produce-and-Sell Scenarios** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| 6 | Enter Inspection Results | Click Edit. Depending on the inspection result, select one of the following two options:Positive ResultSurface: Code Group – Code SURFACE 0020 (Smooth)Negative ResultSurface: Code Group – Code SURFACE 0010 (Rough) | For qualitative characteristic (Surface) the search help is required to select a value.The default number of inspected objects is calculated based on the sample size reviewed in an earlier step. The number of inspected objects can be manually changed. As well as a number of nonconforming objects can be maintained directly in the respective fields for every inspection characteristic.With the App: Record Results – Hierarchical View.A user can exceptionally overrule the automatic evaluation, for example, to document that the tolerance is always at the upper border, then the generic defect ‘tolerance issue’ will be used. |  |
| 7 | Save Inspection Lot | Choose Save. |  |  |

Optional: Process-Optimized Results Recording for Multiple Inspection Lots

If inspection results shall be recorded for several inspection lots at the same time, use the SAP Fiori App: Record Inspection Results in Table Form (F3365). If you want to use this Fiori App, refer to best practice scope item 1MP to view the detailed steps on using this SAP Fiori App.

|  |
| --- |
| Caution Note that this app can only be used for quality inspections with master inspection characteristics. It is not possible to capture inspection results for inspections with plan characteristics. |

#### Display Quality Engineer Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

As an optional entry point for making this usage decision, you can use the app Manage Usage Decisions. This optional process step shows you how to display the open inspection lot regarding the usage decision.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Quality Engineer Overview (F2360). | The Quality Engineer Overview screen displays. |  |
| 3 | Select Inspection Lots Without Usage Decision | Click the card Inspection Lots Without Usage Decision. | A list of inspection lots without usage decisions displays. For this selection of complete inspection lots without deviations, you can use Make Quick Usage Decision to close the inspection lot with an accepted code. |  |
| 4 |  | Continue with chapter Make Usage Decision. | The Manage Usage Decisions screen displays. |  |

#### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the material depending on the inspection result. This process step shows you how to make usage decision.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Usage Decision (QA11). | The Record Usage Decision: Initial screen displays. |  |
| 3 | Enter Inspection Lot number | On the Record Usage Decision: Initial Screen, make the following entry:Inspection Lot: <your Inspection Lot number from previous step>Choose Continue. | The Record Usage Decision: Characteristic Overview screen appears, and your inspection lot is displayed. |  |
| 4 | Display Defects | Check the details of defects on the Defects tab. | Only available if you have recorded a Negative result. |  |
| 5 | Attach a Document | On the Documents tab, choose Add, select the path and add the document. | For example, to upload pictures to visualize the defect. |  |
| 6 | Enter Usage Decision Code | On the Characteristics tab, in the Usage Decision section, depending on the inspection result, select one of the following entries as the UD code:Positive ResultA1 - AcceptedNegative ResultR1 - Rejected |  |  |
| 7 | Save Usage Decision | Choose Save. |  |  |

### Outbound Delivery Processing

#### Material Accepted

##### Post Goods Issue for Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If the material is accepted, you can post the goods issue for outbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries (F0867A). | Screen: Manage Outbound Deliveries (F0867A)is displayed. |  |
| 3. | Selection Criteria | Make the following entries and choose Go.Shipping point: 3310Overall Status: Ready for GI | List of outbound deliveries displayed on the screen as per selection criteria. |  |
| 4. | Select Outbound Delivery for picking | Select the outbound delivery used in previous step and click on Post GIIn the pop-up screen, enter the goods issue date and click Post GI. | Goods issue for outbound delivery document is posted. |  |
| 5. | End of process step | Click on SAP Icon to navigate to home screen | SAP Fiori launchpad home screen is displayed. |  |

The process has been completed with this step. You can proceed with the step Display in this scope item.

##### Proof of Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you record the quantities as confirmed by the respective customer after physical arrival of goods delivered. Thus document the right quantities that should become subject to billing to this customer.

This is only possible for Outbound Deliveries if the customer master data have been maintained in a way that this customer is "POD-relevant" (on sales area level).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Change Outbound Delivery - Proof of Delivery (VLPOD). |  |  |
| 3 | Enter Outbound Delivery | On the same screen, make the following entry, and choose Continue:Outbound Delivery: <your Outbound Delivery Document Number> | The selected Outbound Delivery Document screen displays, and Overview POD tab becomes active. |  |
| 4 | Quantity Difference | If there is a quantity difference between shipping and receiving, go to step 5 and 6. |  |  |
| 5 | Enter POD Delivery Reason (Optional) | In the line with the item for which a differing quantity was reported by the customer, make the following entry or select the following value from the list:Reason: <DFG2(Underdelivery, reason unknown)> |  |  |
| 6 | Enter Deviation (Optional) | In the Quantity Difference field, go to Sales Unit (Qty Diffin Sales Un), enter <respective quantity (differs from the expected Delivery Quantity as per the Outbound Delivery Item)>, and choose Enter. | The quantity displayed for the respective item in the POD quantity field has been recalculated (Quantity Difference subtracted from Delivery Quantity).The value for POD Status field has changed to B (Differences Reported). |  |
| 7 | Confirm Delivery Proof | Choose Confirm Proof of Delivery. | The POD Date field has been filled with the current date.The value for the POD Status field has changed to C (Confirmed). |  |
| 8 | Save | Choose Save. | The Outbound Delivery document is saved with confirmation for actually delivered quantities.These will be used for the consecutive billing step. |  |

#### Material Rejected

##### Post Unrestricted Stock to Blocked Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If the material is rejected, post the material from unrestricted stock to blocked stock.

Procedure

Follow the steps described:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open Transaction | Log on to the SAP Fiori Launchpad as a Warehouse Clerk . | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Post Goods Movement(MIGO) . | The Transfer Stock screen displays. |  |
| 3 | Select criteria. | In the drop down of first field, select Transfer Posting, and in the drop down of second field, select Other and in movement type field enter 344 and hit enter. | Entries are made. |  |
| 4 | Enter Stock Transfer Posting Details | In screen Transfer Posting Other – Name enter the following data:In Tab Transfer Posting, enter values in the fields:Material: FG011Plant: 3310Storage Location: 331AIn Tab: Quantity, enter values in the fields:Qty in Unit of Entry: 2 PCIn Tab: Serial NumbersEnter the serial numbers in column Serial Number: < Serial numbers used in outbound delivery document in earlier steps must be used here>Select Item OK.Choose Check. | System displays message:Document is OK |  |
| 5 | Post | Choose Post. | The system displays a message Material document xxx Posted. |  |

##### Update Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you delete the rejected material from the delivery.

Procedure

If there is enough or partial stock on inventory, a new line item can be created (with reference to the sales order item).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entries and Choose Execute.Shipping Point: 3310 |  |  |
| 4 | Change Outbound Delivery | Mark the relevant delivery and choose Change Outbound Deliveries. | The Delivery XXXXX Change: Overview screen displays. |  |
| 5 | Delete Delivered Quantity and Picked Quantity | Select the delivery line item and click on Menu > Extras > Serial numbers .System gives a pop-up screen Maintain Serial Numbers. In this screen Maintain Serial Numbers, delete all the serial numbers displayed on the screen. After deleting the serial numbers, click on continue. Upon click of Continue, system gives a pop-up screen Confirmation Prompt. Click YesOn the Picking tab, delete the Deliv. Qty and Picked Qty.. |  |  |
| 6 | Save the Delivery | Choose Save. | If the Warning Message Delivery quantity must be entered for the itemappears, choose Enter to confirm. |  |
| 7 | Change Outbound Delivery | Mark the relevant delivery again and choose Change Outbound Deliveries. | The Delivery XXXXX Change: Overview screen displays. |  |
| 8 | Reopen the Delivery | Choose Menu > Outbound Delivery > Deliver Sales Order .In the pop-up screen Delivery Sales Order, enter the following entries and then choose Continue.Order: Obtained from previous step | A new line item is created with reference to the sales order item. |  |
| 9 | Save the Delivery Again | Choose Save. | For the new line item another inspection lot is created; the process continues with section Maintain Serial Numbers. After Record Inspection Results is checked OK, the goods issue can be posted later. |  |

#### Display Inspection Results History (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This optional process step shows you how to display inspection results history.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Results History (F2428). | The Results History screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Aggregation Level: Master Inspection Characteristics | A list of inspection characteristics displays. |  |
| 4 | Select an Inspection Characteristics | Select an Master Inspection Characteristics, for example, Surface. | Several information shows about the selected characteristics for process control.For example,A diagram displays the development of the recorded results for this characteristic with lower and upper limit.Statistical Values for Control Chart and Process Capability. For example, Variance. |  |

### Accounts Receivable

#### Create Billing Document

Purpose

In this activity, you handle the billing.

Procedure

Table 2: Overview

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents (F0798) screen is displayed. |  |
| 3 | Define Billing Settings | Choose Billing Settings and make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for billing due list | In the search condition, use criteria if necessary. | Sales document(s) display in the result. |  |
| 5 | Select item(s) for billing | Select row(s) of SD Document (Outbound delivery) created previously and choose button Create Billing Documents. | The Create Billing Document screen displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, for example current date, then press button OK. | The draft billing document with ID TMPxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Manage Billing Documents screen, choose Save.The draft version billing document with ID TMPxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | The system generates an invoice for billing. |  |
| 8 | ODN Number | Check whether the ODN number is generated for the billing document. | ODN number is generated in the Reference field. |  |

#### Post Incoming Payments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the incoming payments from the customer. For a payment of an invoice where a down payment is applied, the incoming payment amount should be the remainder invoice balance (the remainder invoice balance is the invoice value less the down payment to be applied).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post Incoming Payments (F1345) | The Post Incoming Payments view displays. |  |
| 3 | Enter General Information | Make the following entries in the General Information area:Company Code: 3310Posting date: dateJournal Entry date: dateValue date: today’s dateJournal Entry Type: DZ (Customer Payment) |  |  |
| 4 | Enter Bank Data | Make the following entries in the Bank data area.House Bank/Account ID: AEBK1/AEAC1G/L Account: <account (not a bank subaccount)> (see note)Note To determine the account value, log in as a Cash Management Specialist and open Manage Bank Accounts (F1366A). Enter your Company Code, House Bank, and House Bank Account and choose Go. Choose Details for the row. Choose House Bank Account Connectivity, then in the House Bank Account Data section, make a note of the value in the G/L Account field. Use this value for the G/L Account field above.Amount: customer invoice amountNote If the incoming payment is part of a down payment, enter the remainder invoice balance amount, which is the invoice value less the down payment amount to be applied.Currency: AED |  |  |
| 5 | Enter Open Items | Make the following entries:Customer Account: 33100001 \| 33100050Choose the Propose Items button. | The open items are displayed in the bottom half of the view. |  |
| 6 | Clear Items | Choose Items to Clear by choosing the Clear button in last item column. | The selected item is transferred to view Items to be Cleared. |  |
| 7 | Post Entries | Choose Post. | The Activated dialog box displays details of document number generated. |  |

### Accounts Payable

#### Create Supplier Invoice with PO/GR relation

Purpose

In this activity, you perform the invoice verification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Accounts Payable Accountant role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Supplier Invoice (F0859). | The Create Supplier Invoice screen displays. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Reference: Enter the reference document number of the supplier for example: 33300001Gross Invoice Amount : XXXCurrency: AEDInvoice Date: TodayPosting Date:TodayBaseline Date: Today (in Payment tab)Invoice Party: 33300001 |  |  |
| 4 | Enter Purchase Order References | In Purchase Order References, make the following entries (use a PO you created previously) and Press Enter key.Make the following entries (use a PO you created previously for procuring RM011).References Document Category: Purchase Order/ Scheduling AgreementPurchase Order: PO number (Used to procure RM011 ) | The Purchase Order References screen displays. |  |
| 5 | Select Purchase Order Items | Check the selection of the Purchase Order Items.Confirm the warning messages. | All items of the selected Purchase Order are added to the Purchase Order Item table.You should see material items and delivery costs items which refer to the entered purchase order document. Check if items for planned delivery costs have an item text. |  |
| 6 | Check the Purchase Order Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Purchase Order Item's table displays. |  |
| 7 | Check Tax code | In the section Tax check if there is tax code information and enter the tax amount.when the tax code value is greater than zero | In the Tax tab, you should see the same tax codes as in the items.If there is no tax, specify the tax code <Input Tax Code>. |  |
| 8 | Check the balance | Calculate the tax amount from the item amount multiplied by the tax value. Check the balance (difference between the calculated amount and the gross Amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 9 | Simulate Supplier Invoice and Check Messages | Choose the Simulate button.You can check the simulation results in Simulation Overview and Simulation Details area. Choose Back. | The supplier invoice is simulated. |  |
| 10 | Save as Completed Invoice | Choose Post. | The invoice is posted. The system message is shown. |  |
| 11 | Repeat the steps for creating invoice for the second Purchase Order | Repeat the steps 3 to 10 for creating invoice for the purchase order used for procuring the material: RM012. While doing this, in step 3, it is important to key in the correct invoice party as 33300002 and in step 4, enter the purchase order of RM012. | Invoice posted. |  |
| 12 | Repeat the steps for creating invoice for the Scheduling Agreement | Repeat the steps 3 to 10 for creating invoice for the scheduling agreement used for procuring the material: RM013. While doing this, in step 3, it is important to key in the correct invoice party as 33300001 and in step 4, enter the scheduling agreement of RM013. | Invoice posted |  |
| 13 | Repeat the steps for creating invoice for the Third Purchase Order | Repeat the steps 3 to 10 for creating invoice for the purchase order used for procuring the material: RM018. While doing this, in step 3, it is important to key in the correct invoice party as 33300002 and in step 4, enter the scheduling agreement of RM018. | Invoice posted. |  |
| 14 | Repeat the steps for creating invoice for the Subcontracting Purchase Order | Repeat the steps 3 to 10 for creating invoice for the purchase order used for procuring the material: SG022. While doing this, in step 3, it is important to key in the correct invoice party as 33300007 and in step 4, enter the scheduling agreement of SG022. |  |  |

#### Post Outgoing Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can post outgoing payments either manually or automatically. The manual posting process is described in the following example. The manual outgoing payment generated in this step does not go through an approval process and does not create a payment medium.

When an invoice is paid and the supplier is subject to withholding tax, the tax is withheld from the total invoice amount when the payment is posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Post Outgoing Payments (F1612). | The Post Outgoing Payments (F1612) view displays. |  |
| 3 | General Information | Make the following entries:General Information sectionCompany Code: 3310Posting Date: <Today's date>Journal Entry Date: <Today's date>Value Date: <Today's date>Reference (optional): <reference>Journal Entry Type: KZHeader Text: <header text>Bank Data sectionG/L Account: 11001000House Bank / Account: AEBK1/AEAC1 or AEBK2/AEAC2.Note If the above mentioned options aren't available, choose one from the list of available options from value help.Note Note For invoices in USD, use account USDAC.Amount / Currency: <amount to pay on existing invoice>, for example, 60AEDFees: OptionalAssignment: OptionalExchange Rate: OptionalAmount / CCode Currency: Optional | A list of open items is displayed in the Open Items \| Standard section. |  |
| 4 | Open Item Selection | In the Open Item Selection section, make the following entries:Supplier Account: 33300001and choose the Show Items button.This is used for doing the payment for RM011. |  |  |
| 5 | Select/Deselect | Select an item to pay, and in the Clear column, choose Clear. | The item to pay transfers to the Items to be Cleared / Standard section. |  |
| 6 | Post | Choose Post.Note The generated payment does not require approval. | The system displays Journal entry xxxxxxxxxx was successfully posted in company code1010 notification. |  |
| 7 | Display | To view the posted document, choose Display. | The posted document is displayed. |  |
| 8 | Back | Choose the Back button. | The system displays Journal entry has already been posted. You can now post a new payment notification. |  |
| 9 | Dismiss notification | Choose OK to dismiss the notification. |  |  |
| 10 | Repeat steps to do the payment for other invoices | Repeat the steps 3 to 9 to do the payment for invoice of purchase order for material: RM012, RM017, RM018. While repeating the steps, in step number 4, it is important to use supplier account: 33300002. | Outgoing payment is successfully posted for the purchase order of the RM012, RM017 and RM018 material. |  |
| 11 | Repeat steps to do the payment for the scheduling agreement | Repeat the steps 3 to 9 to do the payment for invoice of scheduling agreement for material: RM013. While repeating the steps, in step number 4, it is important to use supplier account: 33300001. | Outgoing payment is successfully posted for the scheduling agreement of the RM013 material. |  |
| 12 | Repeat steps to do the payment for the invoice of Subcontracting PO | Repeat the steps 3 to 9 to do the payment for invoice of scheduling agreement for material: SG022. While repeating the steps, in step number 4, it is important to use supplier account: 33300007. | Outgoing payment is successfully posted for the purchase order of the SG022 material. |  |

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

Table 3:

| Process | Business Condition |
| --- | --- |
| Technical Completion of Production Order (Optional) | You can access Schedule Order Technical Completion Run (F3841) app as a Production Supervisor - Discrete Manufacturing to schedule a job to set production orders as Technical Completion.If you need to set a production order as Technical Completion separately, you can access Manage Material Coverage - New Version (F0251A) app as a Production Planner, find your production order and select Delete. |
| BEI - Period-End Closing - Plant (Optional) | These are executed collectively as a part of month-end closing. For more information on the month-end closing procedures, refer to Period-End Closing – Plant (BEI) test script.Note Month-end closing can only be executed once a month. |
| Close Confirmed Production/Process Orders (Optional) | Search for Schedule Order Closing Runs - Close Production/Process Orders (F4305) app as a Production Supervisor - Discrete Manufacturing to schedule a job to set orders as Closed (CLSD). |

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
> Flagged while digesting this document, not verified: Post Outgoing Payment step 6 expected result cites 'company code1010' although the same procedure uses Company Code 3310.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Post Outgoing Payment step 10 pays invoices for RM012, RM017 and RM018 but the Create Supplier Invoice steps in this part cover RM011, RM012, RM013, RM018 and SG022 only (no RM017); RM017 may be invoiced in the earlier part of the document.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/test-script-produce-and-sell-standard-products-inventory-management-54-part-01]]
- related-to :: [[08-sales-order-management/customer-returns-management-consumer-products-61v-ae-test-script-sap-s]]
- related-to :: [[12-production-and-manufacturing/produce-and-sell-standard-products-warehouse-managed-54v-ae-test-scrip]]
- related-to :: [[12-production-and-manufacturing/production-capacity-evaluation-and-leveling-consumer-products-5oi-ae-t]]
- related-to :: [[10-procurement/test-script-procurement-of-production-components-consumer-products-5w3]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/54U_S4CLD2608_BPD_EN_AE.docx` — lines 3192–3552 of the extracted text · extracted with `mammoth` · 280,122 chars in the whole document
