---
id: 12-production-and-manufacturing/test-script-sap-s-4hana-cloud-public-edition-from-planning-to-fulfillm-part-03
title: Test Script SAP S/4HANA Cloud Public Edition - From Planning to Fulfillment - Consumer Products (6AA_AE) (6AA_S4CLD2608_BPD_EN_AE) — part 3 of 3
description: "SAP Fiori test script 6AA_AE (UAE); this part: subcontracting inspection and invoicing, sell from stock/in transit, customer returns, billing jobs."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/end-to-end-produce-and-sell]
aliases: []
keywords: [End-to-End Produce-and-Sell Scenarios, quality inspection, usage decision, supplier invoice, batch traceability, sell from stock, sales orders, outbound delivery, picking and goods issue, billing documents]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6AA_S4CLD2608_BPD_EN_AE.docx#lines-6069-7533"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1156
topic: 12-production-and-manufacturing/end-to-end-produce-and-sell
language: EN
part: 3/3
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - From Planning to Fulfillment - Consumer Products (6AA_AE) (6AA_S4CLD2608_BPD_EN_AE) — part 3 of 3

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6AA_S4CLD2608_BPD_EN_AE.docx`, part 3 of 3 (lines 6069–7533 of the extracted text), extracted with `mammoth`. Grouped under **End-to-End Produce-and-Sell Scenarios** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, you can display an overview of open inspection lots via the overview page for quality technicians.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Technician Overview (F2361). | The Quality Technician Overview screen displays.You can get an overview of the inspection lots with open results recording and the inspection lots without an inspection plan.Choose card Inspection Lots with Open Results Recording, No Inspection Points if you want to record results for this goods receipt inspection lot. |  |

##### Display Open Inspection Lots (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection lot is used to record the results of the inspection operation. In this optional step, the references to the goods receipt and purchase order are verified as well as the sample size used for quality inspection reviewed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose GO.Plant: 3310Material: FG0502Inspection Lot Status: OutstandingInspection Lot Origin: Goods Receipt (01) | Alternatively, you can search for the Purch.Doc <purchase order ID> (from previous step).If purchase order is not displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, select Purchasing Document and choose Ok. Choose Go. |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot with column equals to the Purch.Doc <purchase order> (from previous steps). | The Purchase Order number assigned with Inspection Lot is displayed.If the Purchase Order column does not appear, please choose the button Settings. In the View Settings dialog box, select Purchasing Document and choose OK.Note down the inspection lot ____.Note down the batch number ____. |  |
| 5 | Check Inspection Lot | Under Origin, verify the referenced purchase order and material document. | The purchase order number and material document number from which the inspection lot originates are displayed. |  |
| 6 | Choose Operation (Optional) | In Result, choose operation GR Subcontracting. |  |  |
| 7 | Choose Characteristic (Optional) | Click Visual Pack Check in the Characteristics column. | A dialog box appears with the Characteristics Details. |  |
| 8 | Choose Characteristic (Optional) | Click Label Check in the Characteristics column. | A dialog box appears with the Characteristics Details. |  |

##### Record Inspection Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the quality technician performs the quality inspection and records the inspection result(s) for operation 0010 (GR Subcontracting). The result is recorded in the inspection lot according to the defined inspection parameters in the inspection plan.

Prerequisite

The inspection is processed based on inspection lot. In this scope item, the inspection lot is automatically created upon goods receipt for purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results - Hierarchical Worklist (QE51N). | The Results Recording screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Execute.Plant: 3310Insp. Lot Origin： 01(Goods Receipt)Material: FG0502Batch: <Batch ID> from previous stepLot Created: <choose one week ago until today> | The Results Recording Worklist Screen displays.Caution In Cloud system, Dynamic Selection (e.g. for Purchase order) is not offered.Alternatively you can search for the <Batch ID> or <Inspection Lot ID> from previous step. |  |
| 4 | Select the Corresponding Inspection Lot | On the left pane, expand the corresponding inspection lot which you want to record a result. | If a dialogue appears asking to Save, choose Cancel. |  |
| 5 | Choose the Characteristic | Select the characteristic which is under the activity 0010 GR Subcontracting Work Center Quality Check Point with a click (or use icon Select a Characteristic). | When the characteristic is selected Record Results for XXXX TEST : Classes for Characteristic page opens, where the class size can be recorded. |  |
| 6 | Enter Inspection Result for Characteristic | Depending on the inspection result, classify the no. of inspected displays and then confirm with Save.Positive ResultVisual Pack Check: <enter no. of displays in class size> of class NOKLabel Check: <enter no. of displays in class size> of class OKNegative ResultVisual Pack Check: <enter no. of displays in class size> of class OKLabel Pack Check: <enter no. of displays in class size> of class NOK | For both qualitative characteristics a 100% check is performed, assigning the no. of displays to the corresponding class OK or NOK.Auto Valuation is done by the system.The status is set to 5 Processing is completed. |  |

##### Display Quality Engineer Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the inspection lot depending on the inspection result. As an optional entry point for making this usage decision, you can use the app Quality Engineer Overview (F2360). Furthermore, the Quality Engineer Overview (F2360) app displays inspection lots without an inspection plan (e.g. if automatic assignment of an inspection plan is not set up in the material master or if automatic assignment failed), inspection lots without usage decision, inspection lots ready for usage decision.

If negative inspection results are recorded, you can check the defect details in app Manage Defects (F2649) directed from the app Quality Engineer Overview (F2360) via the cards Inspection Lots with Defects, Top Defective Materials, or Top Defects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Engineer Overview (F2360). | The Quality Engineer Overview screen displays. |  |
| 3 | In Card: Inspection Lots without Inspection Plan choose one entry (Optional) |  | To assign missing data and ensure automatic inspection plan determination for further usage. |  |
| 4a | In Card: Select Inspection Lots Without Usage Decision (Optional) | Choose card Inspection Lots Without Usage Decision. | You can process further as described in Make Usage Decision Chapter. |  |
| 4b | Select the Corresponding Inspection Lot you have created before (Optional) | In the inspection lot list, select the inspection lot. | The Manage Usage Decisions screen displays. Alternative Entry to Chapter Manage Usage Decision. |  |
| 4c | Select one of the Inspection Lot by Results Recording Status (Optional) | Select one of the Inspection Lot by Results Recording Status (Optional). | Alternative Entry to Chapter Manage Usage Decision. |  |
| 5 | Select Card Inspection Lots Ready for Usage Decision (Optional) |  | All inspection lots with positive results get collectively an accepted usage decision (e.g. defaulted by A1) when pressing button Make Quick Usage Decision. |  |
| 6 | In Card: Inspection Lots with Defects (Optional) | (In case negative inspection results have been recorded and auto-defect recording has been defined) Select one of the inspection lot origins, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 7 | In Card: Top Defective Materials (Optional) | (In case failed inspection results have been recorded and auto-defect recording has been defined) Select one of the materials inspected, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 8 | In Card: Top Defects (Optional) | (In case negative inspection results have been recorded and auto-defect recording has been defined) Select one of the defect codes recorded, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |

##### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Inspection is done, and the Inspection result is recorded. You must decide whether or not to accept the material coming back from subcontractor depending on the Inspection result. If you do not want to use the Quality Engineer Overview, you can open the Manage Usage Decisions app directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Usage Decisions (F2345). | The Manage Usage Decisions screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Purch.Doc: <Purchase Order> (from Previous steps). | If Purchase Document is not displayed in the filters, choose Adapt Filters. On the dialog box Adapt Filters, Select Purchasing Document and choose OK. Choose GO.Alternatively, you can search for the <batch ID> or <Inspection lot ID> from previous step.If batch is not displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, select Batch and choose Ok, Choose Go. |  |
| 4 | Select Corresponding Inspection Lot | In the Inspection lot list, select the corresponding Inspection lot. | The Inspection Lot screen displays. |  |
| 5 | Display Defects | Scroll down to the Defects area. Check the details of Defects. | Only available when you have recorded a negative result. For a visual pack check rejection, there will be a packaging defect, for label check rejection, there will be a labeling defect displayed. |  |
| 6 | Choose Edit and Add Document | Choose Edit In the Document section Choose Upload, select the path and add the document. | For example, to upload pictures to visualize the defect. |  |
| 7 | Enter UD code | Depending on the inspection result, select one of the following options and then confirm with Save.Positive ResultUD code:A1 (Accepted–unrestricted stock)A2 (Accepted-unrestricted –minor quality)A3 (Accepted-unrestricted-sample consumption)Negative Result:UD code: R1 (Rejected–blocked stock)Choose Yes if dialog Confirmation Prompt appears. | Note The corresponding Stock Posting is processed automatically in the background for the complete quantity for Usage Decision codes A1, A2, R1.Note Please do not use R210 (Return to Supplier w/o Delivery) and R220 (Return to Supplier with Delivery) for this scenario, because in case of deviations, the subcontracted material would be reworked in the current plant but not sent back to subcontractor. |  |
| 8 | Modify Stock Posting (Optional) | In the Inspection Lot Stock section, enter the quantities to be posted in different stock posting proposals. |  |  |
| 9 | Save Usage Decision | Choose Save. | The usage decision is made for the material from subcontractor. The system automatically triggers the material movements associated with the usage decision code. |  |

##### Display Material Stock after Usage Decision (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, we now verify the material movement done based on the usage decision codes by looking again at the material stock.

Procedure

Dependent on the usage decision of the previous steps, the quantity of the material is posted differently.

- Positive Result (A1, A2): quantity is increased in Unrestricted Use Stock and quantity is reduced in Quality Inspection Stock
- Positive Result for ‘sample consumption’ (A3): partial quantity is increased in Unrestricted Stock, inspected quantity is consumed and therefore not in stock anymore, and full quantity is reduced in Quality Inspection Stock
- Negative Result ‘Blocked Stock’ (R1) : quantity is increased in Blocked Stock and quantity is reduced in Quality Inspection Stock
- Negative Result ‘Return to Supplier w/o Delivery’ (R210): Do not use for this scenario
- Negative Result ‘Return to Supplier with Delivery’ (R220): Do not use for this scenario

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076) | The Stock – Single Material screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and press Enter.Material: FG0502 |  |  |
| 4 | Check Stock Quantity | Check the changed quantities of the Quality Inspection Stock, Unrestricted Use Stock (in case of positive usage decision) or Blocked storage location 331A. | The stock quantities for material FG0502 are updated based on the quality inspection and respective usage decision of the previous steps. |  |

#### Invoicing

##### Create Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform the invoice verification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Accounts Payable Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Create Supplier Invoice (F0859). | The Create Supplier Invoice screen displays. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Reference: <xxx> (reference invoice number from invoicing party)Gross Invoice Amount : <XXX>Invoice Date: <Today>Currency: AEDPosting Date: <Today>Invoicing Party: 33305001 | The Create Supplier Invoices screen displays. |  |
| 4 | Enter Purchase Order References | In Purchase Document References make the following entries (use a PO you created previously) and choose Enter.Make the following entries (use a PO you created previously).Reference Document Category: Purchase Order/ Scheduling AgreementPurchase Order: <PO number> | The Purchase Order References screen displays. |  |
| 5 | Select Purchase Order Items | Check the selection of the Purchase Order Items.Confirm the warning messages. | All items of the selected Purchase Order are added to the Purchase Order Item table.You should see material items which refer to the entered purchase order document. |  |
| 6 | Check the Invoice Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Purchase Order Item's table displays. |  |
| 7 | Check Tax Date | In case the time dependent tax is activated, in the section Tax, the Tax Date indicates the tax calculation date according to the tax rates settings in the prerequisites.Make the following entries.Tax Reporting Date: <Today>Tax Date: <Today>Note The Tax Date is the key date for calculating tax, please maintain it carefully according to your financial business requirements. |  |  |
| 8 | Check Tax Code | In the section Tax check if there is tax code information. | In the Tax tab, you should see the same tax codes as in the items.If there is no tax, specify the tax code <Input Tax Code>. |  |
| 9 | Check the Balance | Calculate the tax amount from the item amount multiplied by the tax value. | The balance should be zero (or within the defined tolerance). |  |
| 10 | Simulate Supplier Invoice and Check Messages | Choose Simulate.If there are no differences (or if the value is within the defined tolerance), a new screen Simulation appears. You can check the simulation results in Simulation Overview and Simulation Details area.The Supplier Invoice is complete to post. Check the Gross Invoice Amount against the items plus tax amount (if tax code is, <Input Tax Code> you do not have any tax amount). | The supplier invoice is complete to post. |  |
| 11 | Post Invoice | Choose Post. | The invoice is posted. |  |

##### Review Supplier Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The invoice verification is done in this activity using the list overview on invoice documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as an Accounts Payable Accountant. | The Fiori Launchpad is displayed. |  |
| 2 | Open the Fiori App | Open Supplier Invoices List (F1060A). |  |  |
| 3 | Enter General Data | Make the following entries:Invoicing Party: 33305001Company Code: 3310Choose Go. |  |  |
| 4 | Check invoice | Check Display to check the invoice. |  |  |

#### Batch Traceability

##### Batch Information Cockpit - Top-Down and Bottom-Up Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this functionality you can identify which batches are delivered to which customer and which raw material batches are used for the production of which finished product. You can adapt the selection in the Batch Information Cockpit to customer-specific requirements by creating user-specific groups. You can get additional information by using subsequent actions.

In this case the evaluation is limited to the production process. As soon as you have purchased the raw materials and/or delivered the finished good FG0502 to a customer the evaluation is automatically enhanced with these information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto the SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad using the Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Batch Information Cockpit (BMBC). | The Batch Information Cockpit screen displays. |  |
| 3 | Select batches | On the Batch Information Cockpit screen, make the following entries.Go to Material tab.Material : FG0502Plant: 3310Choose Execute Selection. | One or multiple batches are displayed in the left screen area Selection Result for Batches. The standard sorting is done per material number. |  |
| 4 | Expand selection | In the section Selection Result for Batches select Checkbox for FG0502 and then choose Expand subtree or Expand node. | The selection result is analyzed and a batch for further investigation is identified. |  |
| 5 | Start Analysis | Right click on one selected batch and choose either Usage (Top-Down) or Usage (Bottom-up). | The batch where used list displays. |  |
| 6 | Analyze the batch where used list | The usage of the batch can be analyzed and the specific documents (such as batch master record, production orders and sales order) can be accessed via double click. |  |  |
| 7 | Analyze assigned Inspection lots | Mark one line in the Details (Usage) table and choose button Inspection Lots to review inspection lots assigned to the selected element. |  |  |
| 8 | Analyze Batch Master | Choose Details in the header area and select Batch Master. | The batch master screen displays. |  |
| 9 | Analyze material document | Choose Details again and choose Usage.Select one document and choose Documents. | The usage displays again and after selecting documents the respective material document display. |  |
| 10 | Go to the material document | Select the material document in the pop up and choose Choose (F2).To display the material document, you need further authorizations that are granted by your company, for example, SAP_BR_INVENTORY_MANAGER. | The material document displays.Note Your user has to have the appropriate authorizations. |  |

### Sell from Stock - Consumer Products (5HL)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The process starts with the creation of a customer standard sales orders. When the inventory is decided, the shipping specialist releases the inventory. The inventory is shipped to the customer, and the actual recording of the physical quantity is recorded.

When the goods issue is posted, cost of goods sold is recorded in Financial Accounting.

Once goods are delivered, you can invoice the delivery. When the invoices are created, an invoice list is created for the central payer for both customers. An EDI invoice message is sent to the buyer when the billing document is saved.

#### Sell from Stock

##### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create three sales orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Create, then select Create Sales Order-VA01. |  |  |
| 4 | Enter Order Details | On the Create Standard Order: Initial screen, make the following entries and choose Continue:Order Type: ORSales organization: 3310Distribution channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and choose Continue:Sold-To Party: 33105001Ship-To Party: 33105001Customer Reference: <Reference number> Enter a customer purchase order number as reference.Customer Reference Date: <today>Incoterms: CFRGo to item Overview TabProduct: FG0502Order Quantity: 2Optional: Create additional line item with trading material TG0501.Optional: Add additional main line items with FG0511 or FG0512 if you want to sell these products individually. | Together with the order line for FG0502 there are two sub items for FG0511 and FG0512. The sub items only serve as explanation for the content of the display. |  |
| 6 | Check Customer Hierarchy (optional) | Go to Menu > Goto > Header > Additional Functions > Customer Hierarchy . | The screen with the Customer Hiererchy Root node and its sub nodes relevant for this customer are displayed. |  |
| 7 | Check Pricing (optional) | In the overview screen select the item containing the material you entered and select button Item Conditions. | The condition DCH1 is part of the pricing calculation with the rate you have entered earlier. |  |
| 8 | Save | Choose Save. Make a note of the sales order number:___________. | Sales order with customer 33105001 is created. |  |
| 9 | Create More Sales Orders | Repeat above steps from 1 to 6 to create 1 more sales orders: with Sold-to party 33105002 & 33105005.Make a note of the sales order numbers:___________. | Sales orders are created respectively for customers 33105002 & 33105005. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders - Version 2 (F3893). | The Manage Sales Orders - Version 2 screen displays. |  |
| 3 | Search For Sales Order | Enter search term(s) in filter bar and choose Go, for example, enter sales order number in field Sales Order. | Sales order displays in result list. |  |
| 4 | Navigate to Sales Order Screen | Choose > on the right of the Sales Order item and navigate to Display Standard Orders xxx: Overview screen. | The Display Standard Orders xxx: Overview screen displays. |  |
| 5 | Check Output Condition | On the Display Standard Order xxx: Overview screen, choose Header Output Preview. |  |  |
| 6 | Display Print Preview | On the Display Standard Order xxx: Output screen, select the line already created for the print output and choose Display Document. | Preview for PDF document displays. |  |

|  |
| --- |
| Note It can also be navigated to a factsheet screen in app Manage Sales Orders - Version 2 (F3893):On the Manage Sales Orders (Original) screen, enter search terms in filter bar and choose Go.In search result, choose your Sales Order Number and choose More Links. |

##### Review and Release or Reject a Sales Order (Optional)

Context

The sales order failed the credit check. In the following procedures, you review blocked sales orders and resolve any credit issues.

Prerequisites

Sales orders exceeding the credit limit settings are blocked due to credit check block.

Credit case has been assigned to a Credit Analyst or Person Responsible.

###### Review Sales Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The sales order failed the credit check. In this activity, you review blocked sales orders.

Prerequisites

Sales orders exceeding the credit limit settings are blocked due to a credit check block.

The Documented credit decision has been assigned to a Credit Analyst.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Documented Credit Decision - New Version (F5587A). | The Manage Documented Credit Decision (New Version) view is displayed. |  |
| 3 | Select Documented Credit Decision - Search | Make the following entries and choose Go:Business Partner: 33105005Credit Segment: 1000Note Use appropriate filter to get documents. | A list of documented credit decisions is displayed. |  |
| 4 | Select | Select the row of the documented credit decision you generated in the previous step. | The Document with Credit Block view is displayed. |  |
| 5 | Enable Editing | Choose Edit. | Updates data. |  |
| 6 | Update | Update the DCD fields.Credit Analyst: <Your user with HR Master Record created> | The DCD data is changed. |  |
| 7 | Save | Save your entries. | The changes are saved. |  |
| 8 | Set In Process | Choose Set To In Process | Status changed to In Process. |  |

###### Release Sales Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The sales order failed the credit check. In this activity, you release the sales orders.

Prerequisites

Sales orders exceeding the credit limit settings are blocked due to credit check block.

The Documented credit decision has been assigned to a Credit Analyst.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Documented Credit Decision - New Version (F5587A). | The Manage Documented Credit Decision (New Version) view displays. |  |
| 3 | Select Documented Credit Decision - Search | Make the following entries and choose Go:Business Partner: <your business partner>Credit Segment: 1000 | A list of documented credit decisions is displayed. |  |
| 4 | Select | Select the row of the documented credit decision you generated in the previous step. |  |  |
| 5 | Release | Choose Release. On the Release dialog box, enter an approval note and choose Release. | The log is displayed and under the Classification and Changes facet, the Last Action is Release. |  |

###### Reject Sales Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The sales order failed the credit check. In this activity, you reject the sales orders.

Prerequisites

Sales orders exceeding the credit limit settings are blocked due to credit check block.

The documented credit decision is assigned to a Credit Analyst.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Documented Credit Decision - New Version (F5587A). | The Manage Documented Credit Decision view displays. |  |
| 3 | Select Documented Credit Decision - Search | Make the following entries and choose Go:Business Partner: 33105005Credit Segment: 1000 | A list of documented credit decisions is displayed. |  |
| 4 | Select Case | Select the row of the documented credit decision you generated in the previous step.Choose Details (>). | The Document with Credit Block view displays. |  |
| 5 | Reject | Choose Reject. | The Reject dialog box displays. |  |
| 6 | Select Rejection Reason | Make the following entry and choose Reject:Rejection Reason: for example, Rejected by ApproverRejection Note: <any note> | The sales order/service order/service contract is rejected and the DCD Status changes to Closed and the Notes are updated with the note of type Rejection Reason. |  |

##### Advanced Available-to-Promise Processing (Optional)

Purpose

Follow the procedures in the Basic Available-to-Promise Processing (2LN) and Advanced Available-to-Promise Processing (1JW) scope item. This scope item describes the optional process for Advanced Available-to-Promise Processing.

1. From 2LN, the user can Trigger / Schedule BOP, execute a BOP Run and Monitor BOP Run.
2. From 1JW, the user can execute Release for Delivery.

Procedure

Complete all the activities described in the test script of Advanced Available-to-Promise Processing (1JW) scope item.

##### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create three deliveries from three sales orders created previously.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries - From Sales Orders (F0869A) screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 3310Planned Creation Date: <Delivery selection date>Order: Sales order number created previously |  |  |
| 4 | Create Delivery | Select your sales orders and choose Create Deliveries. | Deliveries are triggered to create. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays. The failed entries will display in Messages tab. The delivery number will display in the Deliveries tab.Three deliveries are created, for customer 33105001, 33105002 and 33105005. |  |

|  |
| --- |
| Note At delivery creation, the scope item settings for check availability use available inventory and replenishment lead time. Without sufficient stock, the created delivery has no confirmed quantities and does not start the warehouse management picking process. As soon as there is sufficient stock at delivery creation, the system creates a delivery with further picking process in warehouse management. To avoid open deliveries, ensure that there is sufficient inventory quantity at delivery creation. Additionally, you have the following options to restrict the creation of deliveries with no confirmed quantities.- You may increase replenishment lead time that is used during the availability check (must be larger than the selection period used for delivery creation).- You may change the customizing settings for the incompleteness procedure for delivery creation, so that only complete deliveries may be saved.- You may change the customizing settings for the used delivery item category.The Check quantity 0 field must be adapted to B = Situation rejected with an error message. |

|  |
| --- |
| Note With the Analyze Outbound Delivery Logs app you can display an overview about the logs of all the deliveries which have been created in your system. You can filter by, for example, created by and Additional settings. If you select the arrow on the right of each delivery log entry you can display the exact message type and text and also the related sales document. |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery (VL02N) screen displays. |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery (VL02N) screen, enter the delivery number and choose Continue. From the Delivery xxxxxxxx Change: Overview screen, choose Menu > Extras > Delivery Output > Output Control . | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery_Pick_List and choose Display Document. | A preview of the print document displays. |  |
| 5 | Print Delivery Pick List | From the preview of the document, choose Print. | The delivery pick list is printed. |  |

##### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to pick deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries, and choose Execute:Shipping Point: 3310Under the Picking Data tab, selectOnly Picking Without WM: X |  |  |
| 5 | Change Outbound Deliveries | Choose your delivery number, and choose Change Outbound Deliveries. |  |  |
| 6 | Check Batch Split | Choose the Picking tab, check if batch split exists in the Batch Split Indicator column. |  |  |
| 7 | Enter Picked Quantity | If batch spilt exists, choose Batch Split Exists to expand sub item(s), enter <quantity equal to Deliv. Qty> in Picked Qty field for sub item.Note Sales BOM sub item materials are not relevant for the logistics process i.e. batch or picking quantity update.If batch split doesn't exist, enter <quantity equal to Deliv. Qty> in Picked Qty field for picking related item(s). |  |  |
| 8 | Choose Enter | Choose Enter. |  |  |
| 9 | Save | Choose Save. | The delivery has been decided. |  |
| 10 | Repeat | Repeat step 4 to 9 for other deliveries (if any). |  |  |

##### Check Batches (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the batch number assigned to the material.

Prerequisites

Execute this step for batch managed products like FG0512.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3 | Enter Outbound Delivery Number | In the Outbound Delivery field, enter <outbound delivery number>, and choose Continue. |  |  |
| 4 | Check Batch Number Assignment | If Expand Batch Split exists, go to the Batch field, and check the batch number assignment. | Batch numbers are assigned to the materials. |  |
| 5 | Save Document | Choose Save. |  |  |

##### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods issues for delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entries and choose Execute.Shipping Point: 3310 |  |  |
| 4 | Post Good Issue | Mark the relevant delivery and choose Post Goods Issue. Select today’s date from the dialog box and choose Continue. | The goods issues are posted for three deliveries. |  |

Financial Postings:

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 51600000Consptn Trde Gds | 13600000Inventory TradingGd | none |
| Finished Goods (FERT) | 54083000Inv Chg COGS w/CE | 13400000Inventory FinishedGd | none |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). |  |  |
| 3 | Issue Delivery Output | On the Display Outbound Delivery screen, enter the delivery number and choose Continue.On the Delivery xxxxxxxx Display: Overview screen, choose Menu > Extras > Delivery Output > Output Control. | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Delivery Note Output Type and choose Display Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

##### Confirm Proof of Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to confirm proof of delivery. Either the customers sends you a confirmation that the goods were actually received or you assume it after a certain period for example two working days after goods issue. Only if you have the proof of delivery confirmed the invoice can be created.

|  |
| --- |
| Tip This step is necessary depending on the business partner data for this customer. In the shipping data you can see if a Proof of Delivery is expected or not. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Deliveries Worklist - Proof of Delivery (VLPODL). | The Deliveries for Proof of Delivery screen displays. |  |
| 3 | Select the Delivery | No entries necessary. Choose Execute. | The list of deliveries relevant for POD-confirmation is displayed. Status for your delivery is red (POD confirmation Status). |  |
| 4 | Confirm Proof of Delivery | Mark the delivery you posted Goods Issue in the previous step.Choose Confirm.On the Confirmation Prompt choose Continue. | The POD Confirmation Log displays with a message that Proof of Delivery for your delivery has been confirmed.If you return to the worklist the status of your delivery is now green. |  |

##### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to handle the billing: Create three billing documents referring to the deliveries created in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using Role Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents (F0798) screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings. You can make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities：OFF |  |  |
| 4 | Search for Billing Due List | In the search condition, use criteria if necessary. | Sales document(s) will display in the result. |  |
| 5 | Select Item(s) for Billing | Select row(s) of sales document created previously and choose button Create Billing Document. | There is one window Creating Billing Documents displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date. For example: current date, then choose OK. | The draft billing document with ID TMPxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Billing Document (F1901) screen, choose Save. The draft version billing document with ID TMPxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | The system generates an invoice for billing. |  |

|  |
| --- |
| Note After this step, the Electronic Nota Fiscal must be handled. This is part of scope item 1J5_BR (section Electronic Fiscal Documents). |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Finished Good (FERT) | Enter G/L Acc 1210000012100000 Description. | 41000000 Rev Domestic Prod22000000 Output tax (MWS) | none |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Documents screen displays. |  |
| 2 | Search the Billing Document Created in Previous Step | In the billing document number recorded in previous step, choose Enter. | The billing document created in previous step displays. |  |
| 3 | Display the Billing Document | Select the billing document item and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, choose the last assignment block - Output Items. | There is one entry in the item and output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document (F1901) screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | Select certain Billing document and choose Cancel Billing Document. | Billing Document Canceled log displays. |  |
| 7 | Update New Attachment (Optional) | In the Edit mode, add, delete and update the attachments. Save your changes by pressing the button Save in the footer bar. |  |  |
| 8 | Update New Text (Optional) | In the Edit mode, add, delete and update the text. Save your changes by pressing the button Save in the footer bar. |  |  |

##### Send Invoice - EDI Relevant

Purpose

This process step shows you how to send invoice to the Buyer system.

Prerequisites

Billing Document must have been created in the SAP S/4HANA system (supplier side).

Procedure

This step is automatically generated.

##### Check Invoice in AIF (Message Dashboard) - EDI relevant

Purpose

The customer invoice is sent via EDI to the Buyer. They are automatically processed if no error occurs. This process step shows you how to check the message status.

Prerequisites

The billing document has been created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the App | Open Message Dashboard - SAP Application Interface Framework (/AIFX/WDA0005). |  |  |
| 3 | Choose Date and Namespace/Interface | On the Interface Monitor screen, choose correct time period entries and choose Search. In the Result List, choose the line of /SDEDI, Outbound Invoice Processing and choose All Messages. |  |  |
| 4 | Check Detail Messages | On the Monitoring and Error Handling screen, expend the messages in the left side of the screen, and choose the corresponding billing number created in previous step.Double click the message to see the detail information on the right side of the screen. |  |  |
| 5 | Reprocess Messages | Choose Reprocess if needed. |  |  |

##### Create Invoice List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create invoice list.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Invoice Lists (F2740). | The Manage Invoice Lists (F2740) screen displays. |  |
| 3 | Navigate to Edit Worklist for Invoice Lists Screen | Choose Create. | The Edit Worklist for Invoice Lists screen displays. |  |
| 4 | Search Billing Documents | Make the following data in section Customer Data and choose Display Worklist for Invoice Lists:Payer: 33105010 | Billing documents displays in the result. |  |
| 5 | Select item(s) for Invoice List | Select the rows of Billing documents created previously and choose Collective Billing Document. | The system generates an invoice list for billing. |  |
| 6 | Check Invoice List Document | On the Edit Worklist for Invoice Lists screen, choose Log Display. And then choose Documents, make a note of the invoice list document number in SD Document column: __________. | Invoice list document number displays. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Finished Good (FERT) | 44002000 Sales Disc Domestic22000000 Output tax (MWS) | Enter G/L Acc 1210000012100000 Description. | none |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Invoice Lists (F2740). |  |  |
| 3 | Search for Invoice List | Enter search term(s) in filter bar and choose Go:For example, enter invoice list number in field Invoice List. | The invoice list is displayed in result list. |  |
| 4 | Navigate to Invoice List Overview Screen | Click invoice list number 9XXXXXXX and choose Display Invoice Lists (VF23). | The Invoice List Display: Invoice List Items Overview screen displays. |  |
| 5 | Check Output Condition | Choose Output. | The Invoice List Display: Output screen displays. |  |
| 6 | Display Print Preview | Select the line already created for the print output and choose Display Document. | The printing form is displayed. |  |

|  |
| --- |
| Note The invoice list can consolidate a list of billing documents: Not only standard invoices with type F2 as above, but also debit memos, credit memos, and convergent billing types (CBD1, CBD2 and CBC1). To simulate invoice lists from debit memo，credit memo, or convergent billing, firstly complete all activities till debit memo/credit memo / convergent billing generation in the following scope item(s) using the data listed in chapter Master Data, Organizational Data, and Other Data:1F1 - Debit Memo Processing1IU - Customer ConsignmentBDD - Lean Customer ReturnsBKP - Customer Returns1EZ - Credit Memo Processing1MC - Omnichannel Convergent Billing |

#### Sell from Valuated Stock in Transit

Sell from Valuated Stock in Transit is triggered by the attributes, which are set in the configuration (chapter 2.7.6). Based on the Item Category, the Sales Organization, the Plant and the Incoterms used, the process is triggered successfully.

##### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create three sales orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Create, then select Create Sales Order - VA01. |  |  |
| 4 | Enter Order Details | On the Create Sales Document screen, make the following entries and choose Continue:Order Type: ORSales organization: 3310Distribution channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and choose Continue:Sold-To Party: 33105001Ship-To Party: 33105001Customer Reference: <Reference number> Enter a customer purchase order number as reference.Customer Reference Date: <today>Go to item Overview TabProduct: FG0512Order Quantity: 2Incoterms: DAPOptional: Create additional line item with trading material TG0501.Optional: Add additional main line items with FG0511. |  | The Business Partner used for this scenario needs to be configured for Incoterm = DAP |
| 6 | Check Customer Hierarchy (optional) | Go to Menu > Goto > Header > Additional Functions > Customer Hierarchy . | The screen with the Customer Hiererchy Root node and its sub nodes relevant for this customer are displayed. |  |
| 7 | Check Pricing (optional) | In the overview screen select the item containing the material you entered and select button Item Conditions. | The condition DCH1 is part of the pricing calculation with the rate you have entered earlier. |  |
| 8 | Save | Choose Save. Make a note of the sales order number:___________. | Sales order with customer 33105001 is created. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders (F1873) screen displays. |  |
| 3 | Search For Sales Order | Enter search term(s) in filter bar and choose Go, for example, enter sales order number in field Sales Order. | Sales order displays in result list. |  |
| 4 | Navigate to Sales Order Screen | Choose > on the right of the Sales Order item and navigate to Display Standard Orders xxx: Overview screen. | The Display Standard Orders xxx: Overview screen displays. |  |
| 5 | Check Output Condition | On the Display Standard Order xxx: Overview screen choose Menu > Extras > Output > Header > Edit . |  |  |
| 6 | Display Print Preview | On the Display Standard Order xxx: Output screen, select the line already created for the print output and choose Display Document. | Preview for PDF document displays. |  |

|  |
| --- |
| Note It can also be navigated to a factsheet screen in app Manage Sales Orders (F1873):On the Manage Sales Orders (Original) screen, enter search terms in filter bar and choose Go.In search result, choose your Sales Order Number and choose More Links. |

##### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create three deliveries from three sales orders created previously.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries - From Sales Orders (F0869A) screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 3310Planned Creation Date: <Delivery selection date>Order: Sales order number created previously |  |  |
| 4 | Create Delivery | Select your sales orders and choose Create Deliveries. | Deliveries are triggered to create. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays. The failed entries will display in Messages tab. The delivery number will display in the Deliveries tab. |  |

|  |
| --- |
| Note At delivery creation, the scope item settings for check availability use available inventory and replenishment lead time. Without sufficient stock, the created delivery has no confirmed quantities and does not start the warehouse management picking process. As soon as there is sufficient stock at delivery creation, the system creates a delivery with further picking process in warehouse management. To avoid open deliveries, ensure that there is sufficient inventory quantity at delivery creation. Additionally, you have the following options to restrict the creation of deliveries with no confirmed quantities.- You may increase replenishment lead time that is used during the availability check (must be larger than the selection period used for delivery creation).- You may change the customizing settings for the incompleteness procedure for delivery creation, so that only complete deliveries may be saved.- You may change the customizing settings for the used delivery item category.The Check quantity 0 field must be adapted to B = Situation rejected with an error message. |

|  |
| --- |
| Note With the Analyze Outbound Delivery Logs app you can display an overview about the logs of all the deliveries which have been created in your system. You can filter by, for example, created by and Additional settings. If you select the arrow on the right of each delivery log entry you can display the exact message type and text and also the related sales document. |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery (VL02N) screen displays. |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery (VL02N) screen, enter the delivery number and choose Continue. From the Delivery xxxxxxxx Change: Overview screen, choose Menu > Extras > Delivery Output > Output Control . | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery_Pick_List and choose Display Document. | A preview of the print document displays. |  |
| 5 | Print Delivery Pick List | From the preview of the document, choose Print. | The delivery pick list is printed. |  |

##### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to pick deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries, and choose Execute:Shipping Point: 3310Under the Picking Data tab, selectOnly Picking Without WM: X |  |  |
| 5 | Change Outbound Deliveries | Choose your delivery number, and choose Change Outbound Deliveries. |  |  |
| 6 | Check Batch Split | Choose the Picking tab, check if batch split exists in the Batch Split Indicator column. |  |  |
| 7 | Enter Picked Quantity | If batch spilt exists, choose Batch Split Exists to expand sub item(s), enter <quantity equal to Deliv. Qty> in Picked Qty field for sub item.Note Sales BOM sub item materials are not relevant for the logistics process i.e. batch or picking quantity update.If batch split doesn't exist, enter <quantity equal to Deliv. Qty> in Picked Qty field for picking related item(s). |  |  |
| 8 | Choose Enter | Choose Enter. |  |  |
| 9 | Save | Choose Save. | The delivery has been decided. |  |
| 10 | Repeat | Repeat step 4 to 9 for other deliveries (if any). |  |  |

##### Check Batches (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the batch number assigned to the material.

Prerequisites

Execute this step for batch managed products like FG0512.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3 | Enter Outbound Delivery Number | In the Outbound Delivery field, enter <outbound delivery number>, and choose Continue. |  |  |
| 4 | Check Batch Number Assignment | If Expand Batch Split exists, go to the Batch field, and check the batch number assignment. | Batch numbers are assigned to the materials. |  |
| 5 | Save Document | Choose Save. |  |  |

##### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods issues for delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entries and choose Execute.Shipping Point: 3310 |  |  |
| 4 | Post Good Issue | Mark the relevant delivery and choose Post Goods Issue. Select today’s date from the dialog box and choose Continue. | 1 successful and 0 incorrect goods movements. |  |

Financial Postings:

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 51600000Consptn Trde Gds | 13600000Inventory TradingGd | none |
| Finished Goods (FERT) | 54083000Inv Chg COGS w/CE | 13400000Inventory FinishedGd | none |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). |  |  |
| 3 | Issue Delivery Output | On the Display Outbound Delivery screen, enter the delivery number and choose Continue.On the Delivery xxxxxxxx Display: Overview screen, choose Menu > Extras > Delivery Output > Output Control. | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Delivery Note Output Type and choose Display Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

##### Confirm Proof of Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to confirm proof of delivery. Either the customers sends you a confirmation that the goods were actually received or you assume it after a certain period for example two working days after goods issue. Only if you have the proof of delivery confirmed the invoice can be created.

|  |
| --- |
| Tip This step is necessary depending on the business partner data for this customer. In the shipping data you can see if a Proof of Delivery is expected or not. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Deliveries Worklist - Proof of Delivery (VLPODL). | The Deliveries for Proof of Delivery screen displays. |  |
| 3 | Select the Delivery | No entries necessary. Choose Execute. | The list of deliveries relevant for POD-confirmation is displayed. Status for your delivery is red (POD confirmation Status). |  |
| 4 | Confirm Proof of Delivery | Mark the delivery you posted Goods Issue in the previous step.Choose Confirm.On the Confirmation Prompt choose Continue. | The POD Confirmation Log displays with a message that Proof of Delivery for your delivery has been confirmed.If you return to the worklist the status of your delivery is now green. |  |

##### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to handle the billing: Create three billing documents referring to the deliveries created in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using Role Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents (F0798) screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings. You can make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities：OFF |  |  |
| 4 | Search for Billing Due List | In the search condition, use criteria if necessary. | Sales document(s) will display in the result. |  |
| 5 | Select Item(s) for Billing | Select row(s) of sales document created previously and choose button Create Billing Document. | There is one window Creating Billing Documents displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date. For example: current date, then choose OK. | The draft billing document with ID TMPxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Billing Document (F1901) screen, choose Save. The draft version billing document with ID TMPxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | The system generates an invoice for billing. |  |

|  |
| --- |
| Note After this step, the Electronic Nota Fiscal must be handled. This is part of scope item 1J5_BR (section Electronic Fiscal Documents). |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Finished Good (FERT) | Enter G/L Acc 1210000012100000 Description. | 41000000 Rev Domestic Prod22000000 Output tax (MWS) | none |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Documents screen displays. |  |
| 2 | Search the Billing Document Created in Previous Step | In the billing document number recorded in previous step, choose Enter. | The billing document created in previous step displays. |  |
| 3 | Display the Billing Document | Select the billing document item and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, choose the last assignment block - Output Items. | There is one entry in the item and output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document (F1901) screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | Select certain Billing document and choose Cancel Billing Document. | Billing Document Canceled log displays. |  |
| 7 | Update New Attachment (Optional) | In the Edit mode, add, delete and update the attachments. Save your changes by pressing the button Save in the footer bar. |  |  |
| 8 | Update New Text (Optional) | In the Edit mode, add, delete and update the text. Save your changes by pressing the button Save in the footer bar. |  |  |

### Customer Returns Management – Consumer Products (61V)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Return to Seller process for a customer return scenario is also covered.

A return order is created in reference to the original billing document. Once saved, a return delivery is automatically generated. The goods, once received, are inspected at the warehouse.

The user can influence when the refunding documents are created: either directly, when releasing a return order, or after the inspection. Finally, the user can decide on the compensation for the customers: full or partial refund.

The progress of the return process can be monitored using a returns overview.

#### Goods are Returned to Seller

##### Create Returns Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a returns order.

|  |
| --- |
| Note This chapter mainly introduces follow-up activity 0001 - Receive into Plant after which material inspection needs to be performed for further inventory movement of returned materials. If you can specify the final destination of the returned materials when creating returns order and expect to skip subsequent material inspection chapter, just choose one alternatively from below:* 0002 - Immediately Move to Free Available Stock* 0003 - Immediately Move to Scrap* 0014 - Immediately Move to Specified StockWith above follow-up activities 0002 or 0003, it is mandatory to maintain inspection result in returns order. Once returns order is saved, returns delivery, picking and goods receipt will be generated automatically in background, next run the refund relevant steps:[Determine Refund](#unique_205)[Display Return Overview](#unique_206)Refund Customer with Credit Memo |

Prerequisite

You must have billing document, pro-froma invoice or sales order as reference (refer to [Business Conditions](#unique_209))

|  |
| --- |
| NoteGenerally, you take over the product ownership from the customer and the product is valuated when you refund a customer with either a replacement or a credit memo. There may be scenarios where you want to refund the customer but do not expect the refund to signal the decision on the ownership because the product inspection has not been completed yet. In such cases, perform the following steps to suspend product valuation until final logistical follow-up activity is confirmed in product inspection.Depending on your environment in SAP S/4HANA Cloud Public Edition, use SSCUI 106396 in SAP Fiori Launchpad or configuration activity Configure Returns Order Type for Standard Return in SAP Central Business Configuration to activate the function of suspending product valuation.Check the checkbox Suspend Valuation of the returns item of CBAR order which is created via app Manage Customer Returns - Version 2 (F4832) |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns (F1708).Note Alternatively, SAP system supports creating returns order without reference using app Manage Customer Returns - Version 2 (F4832). On the Manage Customer Returns - Version 2 (F4832) screen, choose Create > Create Returns Order - VA01. After manually entering order type CBAR and other necessary data, choose Save to create returns order without reference. | The Manage Customer Returns screen displays. |  |
| 3 | Create Returns Order | Choose Create. | The Create Returns Order from Reference Document screen displays. |  |
| 4 | Enter Data | Use Adapt Filters to add Reference Document field if it is hidden.Enter the following selection criteria in the filter bar and choose Go:Reference Document:: <billing document number, which is created previously> | Billing (sales) documents are displayed in the Reference Documents table. |  |
| 5 | Choose Create | Choose Create in the billing (sales) document entry. | The dialog box Create Returns Order from Invoice (Sales) appears. |  |
| 6a | Option 1: Enter Data for normal return | Enter the following data and choose CreateReturn Reason: for example, Customer ordered too muchQuantity: <quantity to be returned> | Returns order is created.System navigates to Edit Returns Order screen. |  |
| 6b | Option 2: Enter Data for delivery Refusal | Enter the following data and choose Create:• Return Reason: for example, Delivery RefusalChoose Auto Fill to copy the items and quantities from the referenced invoice. | returns order is created with open quantitySystem navigates to Edit Returns Order screen. |  |
| 8 | Navigate to Follow-up Activities Screen | On the top right corner of the screen, choose Followup Activities. | The Follow-up Activities screen displays. |  |
| 9 | Check Follow-up Activity | Check Receive into Plant (0001) is maintained in the Follow-Up Activity column.Choose Back. | The Edit Returns Order screen displays. |  |
|  |  | The user can influence the point in time when the refunding document must be created: Either immediately when the returns order is saved and released or at a later point of time. Combination of the refund setting determines follow-up document creation. Choose one among the following options to continue: |  |  |
| 11 | Option 1: Execute Refund with Credit Memo Request Immediately | In the Refund section, enter the following data or action, then choose Apply:Refund Type: Credit MemoRefund Code: <select one from down-drop list>, for example, 10%.Note Refund deduction (condition type DRE1) is determined automatically based on the refund code entered.The following steps guides you how to define more refund codes and related condition records:Define returns refund codes via SSCUI 104235Maintain condition records for DRE1 using the Set Material Prices – Sales app. For more details, refer to master data script Create Sales Pricing Condition - MDS (BET).Refund Control: Create Credit Memo RequestChoose Save and Release. | returns order is created.Note Returns delivery and credit memo request are generated automatically. |  |
|  | Option 2: Execute Refund with Credit Memo | On the top right corner of the screen, choose Follow-up Activities, maintain the following data and choose Back:Follow-up Activity: Receive into Plant (0001)Product Received: XOn the Edit Returns Order screen, in the Item area, in the Refund Details column, enter the following data or action:Refund Type: Credit MemoRefund Code: 10% (select from dropdown list)Refund Control: Create Credit MemoChoose Save and Release. | Returns order is created.Note Subsequent documents are generated in background including:Returns deliveryGoods receipt of returns deliveryCredit memo |  |
| 13 | Check Process Flow | On the Manage Customer Returns screen, choose arrow at the end of the item. In the Process flow area, check dependent documents in process flow. Make a note of the follow-up document numbers for further use.Note If you need to delete returns order, execute below steps after its subsequent documents are deleted: On the Manage Customer Returns screen, select your returns order and choose Delete. | The Display Returns Order screen displays and the dependent document(s) display(s). |  |

|  |
| --- |
| Note If freight was maintained in previous delivery document header and material was partly returned regarding billing document, please check (or change if necessary) freight amount for condition type YBHD in the header(s) of returns order (and credit memo request document if it is generated automatically) using the role Internal Sales Representative (SAP_BR_INTERNAL_SALES_REP) and the Change Sales Order tile.If requested delivery date is reached and delivery document has not been created, warning information delivery issue will show in process flow as a reminder. Once delivery document is generated later, such alert will disappear. |

##### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, picking is done for returns delivery created previously. This process step shows you how to perform picking.

In Case of Refund Control: Create Credit Memo, picking quantity is not applicable.

If batch managed material, enter the batch number as well (batch number can be referred from original Delivery document).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries and choose Execute:Shipping Point: 331R |  |  |
| 5 | Change Outbound Deliveries | On the Day’s Workload for Picking screen, select your delivery number and choose Change Outbound Deliveries. |  |  |
| 6 | Enter Picked Quantity | On the Picking tab, input quantity equal to delivery quantity in the Picked Qty field.Enter batch number in the Batch field if the material is batch managed.Note In case the return delivery contains product FG0502, the BOM-sub items are as well shown in the picking overview. They are logistically not relevant and can be ignored. |  |  |
| 7 | Choose Enter | Press Enter. |  |  |
| 8 | Save | Choose Save. | The delivery is picked. |  |

##### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the returned material is received, goods receipt is posted for returns delivery. This process step shows you how to post a goods receipt.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Goods Issue | Choose For Goods Issue. |  |  |
| 4 | Enter Shipping Point | Make the following entries and choose Execute:Shipping Point: 331R. |  |  |
| 5 | Post Goods Receipt | Mark the relevant delivery and choose Post Goods Issue. Choose date of today from the dialog box. | The goods receipt is posted. |  |

##### Perform Material Inspection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The material inspection takes place after the returned goods have been received in the warehouse. The further handling of the returned goods is decided. This process step shows you how to perform material inspection.

Prerequisite

The returned goods are received.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Enter Inspection Results - From Warehouse (MSR_INSPWH). | The Worklist Selection of Deliveries screen displays. |  |
| 3 | Maintain Selection Criteria | Enter the following entries and choose Execute:Delivery Items Waiting for Inspection: <select>Delivery: <enter returns delivery number> | The Change: Material Inspection in Warehouse for Delivery screen displays. |  |
| 4 | Choose Item Tab | Choose Item tab. |  |  |
|  | Inspection Split (Optional) | If different inspection results need to be recorded for the same delivery item, perform below actions, otherwise you can directly skip this step.Select the delivery item and choose Create Split Item, then run steps 5-6 for all inspection items. |  |  |
| 5 | Maintain Inspection Result | In the Inspection Result subarea, enter the following data, and press Enter:Inspection Code: <enter inspection code>Inspected Quantity: <enter inspected quantity>If the Confirmation of Redetermination dialog box appears, choose Yes to confirm. |  |  |
| 6 | Maintain Follow-up Activity | In the Logistical Follow-up subarea, enter the following data and press Enter:Follow-up Activity: <enter follow-up activity>Note Choose appropriate follow-up activity according to inspection code. For example, choose follow-up activity Transfer to Free Available Stock responding to inspection code 0001.Choose suitable Follow-Up Activity from below options according to your subsequent scenarios:0011 Transfer to Free Available Stock0012 Transfer to Scrap0015 Transfer to Specified Stock0018 Transfer to Scrap for Customer0021 Send Back to Customer0023 goods receipt quantity correction |  |  |
| 7 | Check Inspection Status | On the Header tab, in the Basic Data subarea, Inspection Status shows Inspected, which means all received materials are inspected completely. | All received materials are inspected completely. |  |
| 8 | Save and Confirm | In menu bar at the top of screen, choose Save and Confirm.Note Do not choose Save Inspection Results at the bottom right of the screen, as subsequent material documents will not be automatically generated. | Inspection result is recorded, and goods movement is posted accordingly. |  |

##### Determine Refund

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, refund decision is made.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Search for Returns Order | Choose Adapt Filters to add Returns Order field, if it is hidden. Enter the following data and choose Go:Returns Order : <returns order number 6XXXXXXX> | Returns order is found and displayed. |  |
| 4 | Navigate to Determine Refund Screen | Select the returns order entry and choose Determine Refund. | The Determine Refund screen displays. |  |
| 5 | Check Refund Progress | In the upper area, check percentage number in the field Refund Progress and then take next action accordingly:<100%: Refund determination is not completed. Go to Section A and then Section B.100%: Refund determination is completed. Skip Section A and go to Section B. |  |  |
| Section A: Refund is determined with reference to product inspection results | Option 1: Credit Memo | On the Items to Be Refunded tab, choose Change Refund in the Refund Details column for the return item.Enter the following data:Refund Type: Credit MemoExtent of Refund: <a percentage number>, for example, 10% RefundChoose OK.Select the item and choose Release Selected Items.Note For send back to customer scenario, enter the following data:Refund Type: No RefundCMR Rejection Reason: 59 Damaged by customer | Refund setting is maintained, and credit memo request document is created in background. |  |
| Section B: Check refund determination result | Check refund results | On the Completed Items tab, refund result is displayed. Follow-up document number is shown in Refund Details column. Make a note of document number for further use. You can click the created document number to check detailed information. | The refund result displays. |  |

##### Display Returns Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the progress of returns process. All dependent documents are available in process flow.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns (F1708). | The Manage Customer Returns screen displays. |  |
| 3 | Search for returns Order | Choose Adapt Filters if Returns Order field is hidden. Enter the following data and choose Go:Returns Order: <returns order number 6XXXXXXX> | Returns order is found and displayed. |  |
| 4 | Order Overview | Click the created returns order number 6XXXXXXX and choose Display Customer Return. | The Display Standard Return 6XXXXXXX: Overview screen displays. |  |
| 5 | Document Flow | On Returns tab, choose Returns Overview in Returns Control area. | The Returns Overview for Returns Order 6XXXXXXX - 10 screen displays. |  |
| 6 | Check Document Flow | In Document Number column, make a note of follow-up document number(s) of credit memo request for further use. |  |  |

|  |
| --- |
| Note After you have completed this activity:Option A: If credit memo request is generated, go to the Refund Customer with Credit Memo chapter. |

##### Credit Memo

###### Create Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a credit memo.

Applicable in case where Refund Control: Create Credit Memo Request

Procedure

Table 2: Create Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Document screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings.Maintain settings as below.Set Billing Data and type before billing: ONCreate separate Billing Documents for Each item of Billing Due List: ON.Automatically Post Billing Documents: ONDisplay Billing Document after creation: ON.Choose delivery item to be billed and select quantities: OFF. |  |  |
| 4 | Search for Billing List | In the search condition, enter criteria if necessary. | SD document(s) display(s) in the result. |  |
| 5 | Choose SD Document | Select the row of credit memo request document recorded previously and choose Create Billing Documents. | The Create Billing Documents (F0798) screen displays. |  |
| 6 | Maintain Billing Type and Date | Choose billing type Credit Memo (G2) and maintain billing date, such as the current date, and then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Manage Billing Documents screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Final credit memo is generated. |  |

Table 3: Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Documents screen displays. |  |
| 2 | Search Billing Document | Enter the billing document number recorded previously, and press Enter. | The billing document which is created previously displays. |  |
| 3 | Display Billing Document | Select the billing document item, and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, go to the last assignment block, Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | On the Billing Document screen, select a certain billing document and choose Cancel Billing Document. | A log displays the following message: Billing Document Canceled. |  |
| 7 | Update new Attachment (Optional) | In the Edit mode, you can add, delete, and update the attachments. Save your changes by choosing Save in the footer bar. |  |  |
| 8 | Update new Text (Optional) | In the Edit mode, you can add, delete, and update the texts. Save your changes by choosing Save in the footer bar. |  |  |

#### Scheduling Job (Alternative)

##### Job Scheduling for Goods Issue Deliveries (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for goods issue posting with reference to outbound deliveries.

This app can be used as an alternative instead of the manual goods issue posting for outbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Goods Issue for Deliveries (F2259). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Goods Issue Deliveries Schedule | Choose Create to define a new job. | The New Job screen displays. The Job Template should be defaulted as Schedule goods issue for Deliveries. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A schedule goods issue for deliveries job is scheduled. The screen goes back to Application Jobs. |  |
| 6 | Check Goods Issue Deliveries Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Status symbol in the Log column.Note Choose the Magnifier, and the job list will refresh. | The job log details are displayed. |  |

##### Job Scheduling for Billing Creation (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for creation billing documents.

This app can be used as an alternative instead of the manual creation of billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Creation (F1519). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Creation Schedule | Choose Create to define a new job for billing creation. | The New Job screen displays. Job Template should default as Schedule Billing Creation. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing creation job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Billing Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose the Magnifier, and the job list will refresh. | The log details display. |  |

##### Job Scheduling for Billing Release (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for release billing documents to accounting.

This app can be used as an alternative instead of the manual release to accounting for billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Release (F1518). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Release Schedule | Choose Create to define a new job for billing creation. | The New Job screen displays. Job Template defaultly should be Schedule Billing Release. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled. Return to Application Jobs. |  |
| 6 | Check Billing Release Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose Magnifier, and the job list will refresh. | The log details displays. |  |

##### Job Scheduling for Billing Output (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for when and how billing documents are sent to customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Output (F1510). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Output Schedule | Choose Create to define a new job for billing creation. | The New Job screen displays. Job Template should default as Schedule Billing Output. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled. Return to Application Jobs. |  |
| 6 | Check Billing Output Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose Magnifier, and the job list will refresh. | The log details display. |  |

## Appendix

### Succeeding Processes

The following processes and conditions can succeed this process.

| Process | Business Condition |
| --- | --- |
| 6A6 - Vendor Performance – Consumer Products | You can evaluate your company’s suppliers to obtain a basis for your business relationship with them and to optimize your supply base. |
| 61W - Product Cost Related Master Data Changes – Consumer Products | This scope item gives you an example of possible handling options for updating standard costs outside of the annual operations planning. |

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
> Flagged while digesting this document, not verified: Record Inspection Results step 6 lists the Positive Result with Visual Pack Check assigned to class NOK and the Negative Result with Visual Pack Check assigned to class OK, while Label Check is the reverse; the positive/negative class assignments look internally inconsistent.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/test-script-sap-s-4hana-cloud-public-edition-from-planning-to-fulfillm-part-02]]
- related-to :: [[08-sales-order-management/customer-returns-management-consumer-products-61v-ae-test-script-sap-s]]
- related-to :: [[12-production-and-manufacturing/produce-and-sell-standard-products-warehouse-managed-54v-ae-test-scrip]]
- related-to :: [[12-production-and-manufacturing/production-capacity-evaluation-and-leveling-consumer-products-5oi-ae-t]]
- related-to :: [[10-procurement/test-script-procurement-of-production-components-consumer-products-5w3]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6AA_S4CLD2608_BPD_EN_AE.docx` — lines 6069–7533 of the extracted text · extracted with `mammoth` · 604,664 chars in the whole document
