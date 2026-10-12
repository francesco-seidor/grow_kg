---
id: 12-production-and-manufacturing/test-script-sap-s-4hana-cloud-public-edition-from-planning-to-fulfillm-part-02
title: Test Script SAP S/4HANA Cloud Public Edition - From Planning to Fulfillment - Consumer Products (6AA_AE) (6AA_S4CLD2608_BPD_EN_AE) — part 2 of 3
description: "SAP S/4HANA Cloud 6AA_AE Consumer Products test script, part 2: raw-material QM, 5HK QM in discrete manufacturing, start of 5W4 subcontracting; Fiori steps."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/end-to-end-produce-and-sell]
aliases: []
keywords: [End-to-End Produce-and-Sell Scenarios, quality inspection, inspection results recording, usage decision, in-process quality control, early goods receipt inspection, production order processing, production order confirmation, material requirements planning, subcontracting]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6AA_S4CLD2608_BPD_EN_AE.docx#lines-3042-6068"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1156
topic: 12-production-and-manufacturing/end-to-end-produce-and-sell
language: EN
part: 2/3
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - From Planning to Fulfillment - Consumer Products (6AA_AE) (6AA_S4CLD2608_BPD_EN_AE) — part 2 of 3

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6AA_S4CLD2608_BPD_EN_AE.docx`, part 2 of 3 (lines 3042–6068 of the extracted text), extracted with `mammoth`. Grouped under **End-to-End Produce-and-Sell Scenarios** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| 3 | Search for Goods Receipts Material Document | Make the following entries and choose Go:Plant: 3310Material Document: <Material Document> | On the Material Documents Overview screen, the relevant Material Documents / Material Document items are shown. |  |
| 4 | Select Material Document for Goods Receipt | Select the row for which you would like to see the material documents. | The list of the Material Documents is displayed.The Goods Receipts Details are shown. |  |
| 5 | Check Goods Receipts Details | Check the General Information, and the Material Document Items. | In the General Data section, the correct Posting Date, Document Date, and the Delivery Note are shown. |  |
| 6 | Display Document Flow | Switch to the section Process Flow. | The Process Flow shows the Purchase Order and the Material Document as a flow chart. |  |
| 7 | Back to Launchpad | Choose Home to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

#### Quality Inspection (Goods Receipt Inspection)

##### Display Material Stock Before Quality Inspection (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, a review of the raw material stock is done. Due to quality inspection, the material isn't available for other processing.

Prerequisite

The goods receipt from purchase order was posted for the raw material directly to quality inspection stock. This is caused by material master settings for inspection type 01 Goods Receipt Inspection for Purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori Launchpad as a Inventory Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material screen displays. |  |
| 3 | Enter Material | Make the following entries and choose Enter:Material: RM0501 | Stock for the material is displayed. |  |
| 4 | Check Stock Quantity | Check the Quality Inspection Stock under the plant 3310 and storage location 331C for your batch <Batch ID>. | Stock for the material, batch, and storage location is checked. |  |

##### Display Inspection Plan for Inspection Characteristics (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you display the inspection plan that is related to the raw material. The inspection plan defines all inspection characteristics used later in the quality inspection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment. |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Inspection Plan (QP03). | The Display Inspection Plan: Initial Screen screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Continue.Material: RM0501Plant: 3310 |  |  |
| 4 | Select Entry Instruction | In the Inspection Plan Display: Task List Overview, choose Inspection Plan with Group Counter GrC 1. In Task List Overview screen, select the row with Raw Coffee Beans Arabica and then choose Operations. | Only needed, if more than one inspection plan is assigned to the plan group. |  |
| 5 | Go to Inspection Characteristics Overview Screen | Select the entry for Operation 0010 and choose Inspection Characteristics.Note If you couldn't find Inspection Characteristics in your screen, choose Menu > Inspection Characteristics. | The Display Inspection Plan: Characteristic Overview screen displays. |  |
| 6 | Review the Inspection Characteristics | There are two Master Inspection Characteristics:One is Quantitative – Relative Humidity (%).The other one is Qualitative – Defect Grade Raw Coffee Beans (NYBOT) with inspection method Defect Grade (NYBOT).For all, sample size 1 is to be inspected.Auto-defect recording is defined if characteristic Relative Humidity is rejected. | You've now reviewed the inspection characteristics for which data has to be maintained later. |  |
| 7 | Go to Inspection Characteristics Overview Screen | Select the entry for Operation 0020 and choose Inspection Characteristics.Note If you couldn't find Inspection Characteristics in your screen, choose Menu > Inspection Characteristics. | The Display Inspection Plan: Characteristic Overview screen displays. |  |
| 8 | Review the Inspection characteristics | There's one Master Inspection Characteristic:It's Qualitative – Sensory Raw Coffee Beans (SCAA) with inspection method Sensory of Raw Coffee Beans (SCAA).Sample size 1 is to be inspected. | You've now reviewed the inspection characteristic for which data has to be maintained later. |  |

##### Display Quality Technician Overview (Optional)

Test Administration

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

The inspection lot is used to record the results of the inspection operation. In this optional step, the references to the goods receipt and purchase order are verified as well as assigned inspection methods with long texts used for quality inspection.

Prerequisite

In this scope item, the inspection lot is created automatically upon goods receipt for the purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Material: RM0501Inspection Lot Status: OutstandingInspection Lot Origin: Goods Receipt | Alternatively, you can search for the Purch.Doc <Purchase Order ID> (from previous step)If purchase order is not displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, select Purchasing Document and choose OK. Choose Go. |  |
| 4 | Select Inspection Lot | In the inspection lot list, select the inspection lot with column equals to the Purchasing Document: <purchase order> (from previous steps) | The Purchase Order number assigned with Inspection Lot is displayed.If the Purchase Order column does not appear, please choose the button Settings. In the View Settings dialog box, select Purchasing Document and choose OK.Note down the inspection lot ____________________Note down the batch number ____________________ |  |
| 5 | Check Inspection Lot by Selecting the Line | Under Origin, verify the referenced purchase order and material document. | The purchase order number and material document number from which the inspection lot originates are displayed. |  |
| 6 | Choose Operation (optional) | In Result, choose operation Physical Inspection. | Inspection Characteristics Relative Humidity and Defect Grade Raw Beans (NYBOT) can be reviewed with their specifications and calculated sample sizes. |  |
| 7 | Choose Characteristic (optional) | Click Defect Grade Raw Coffee Beans (NYBOT) in the characteristics column. | A dialog box appears with the Characteristics Details with the link to the Inspection Method. |  |
| 8 | Display Text | In General, Long Text is displayed. |  |  |
| 9 | Choose Operation (optional) | In Result, choose operation Sensory Inspection (Coffee Cupping). | Inspection Characteristic Sensory Raw Coffee Beans (SCAA) can be reviewed with their specifications and calculated sample sizes. |  |
| 10 | Choose Characteristic (optional) | Click Sensory Raw Coffee Beans (SCAA) in the characteristics column. | A dialog box appears with the Characteristics Details with the link to the Inspection Method. |  |
| 11 | Display Text | In General, Long Text is displayed. |  |  |

##### Record Inspection Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the quality technician performs the quality inspection and records the inspection result(s) by selecting the relevant work center.

The result is recorded in the inspection lot according to the defined inspection parameters in the inspection plan.

Prerequisite

The inspection is processed based on inspection lot. In this scope item, the inspection lot is automatically created upon goods receipt for purchase order.

Procedure

Record Inspection Results for one Inspection Lot

If inspection results shall be recorded for one or only a few inspection lots, execute the following process flow:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A). | The Record Inspection Results screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Purchase Order: <Purchase Order ID> (from previous step). | If purchase order isn't displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, select Purchase Order and choose OK. Choose Go.Alternatively, you can search for the batch <Batch ID> or <Inspection Lot ID> (from previous step). |  |
| 4 | Display the Corresponding Operations | Switch from Inspection Lots list to the Operations list. | Both Inspection lot operations with relevant work center are offered. |  |
| 5 | Enter Additional Filter Fields | Expand Header for additional filter, make the following entry and choose Go.Work Center: QMLABS | If Work Center is not displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, select Work Center and choose OK. Choose Go.Only Inspection lot operations and master characteristics for filtered work center will be offered for results recording. |  |
| 6 | Choose Record Results | Choose Record Multiple Results in the right bottom. |  |  |
| 7 | Enter Inspection Result | Depending on the inspection result, select one of the following two options:Positive ResultRelative Humidity : Mean Value (%): 11Defect Grade Raw Coffee Beans (NYBOT): Code Group - Code: GRADE-RB 2 (Premium Grade)Negative ResultRelative Humidity : Mean Value (%): 13 | For qualitative characteristic (Defect Grade Raw Coffee Beans (NYBOT)) the search help is needed to select a value. For the quantitative characteristic (Relative Humidity) a number can be entered directly.The default number of inspected objects is calculated based on the sample size reviewed in an earlier step. |  |
| 8 | Save Inspection Lot | Choose Save. After success message, choose Back | The inspection lot is saved. QM Inspection for work center QMLABS has been performed and results recorded. |  |
| 9 | Change Filter Fields | Expand Header for additional filter, make the following entry and choose Go.Work Center: QMSENS | If Work Center is displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, select Work Center and choose OK. Choose Go.Only Inspection lot operations and master characteristics for filtered work center will be offered for results recording. |  |
| 10 | Choose Record Results | Choose Record Multiple Results in the right bottom. |  |  |
| 11 | Enter Inspection Result | Select one entry: e.g.Sensory Raw Coffee Beans (SCAA): Code Group - Code: SENS2_RB 0020 (Excellent) | For qualitative characteristic (Sensory Raw Coffee Beans (SCAA)) the search help is needed to select a value.The default number of inspected objects is calculated based on the sample size reviewed in an earlier step. |  |
| 12 | Save Inspection Lot | Choose Save. | The inspection lot is saved. QM Inspection for work center QMSENS has been performed and results recorded. |  |

Optional: Process-Optimized Results Recording for Multiple Inspection Lots

If inspection results shall be recorded for multiple inspection lots at the same time (mass processing), execute the following process flow.

|  |
| --- |
| Caution Note that this app can only be used for quality inspections with master inspection characteristics. It is not possible to capture inspection results for inspections with plan characteristics. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results in Table Form (F3365). | The Record Inspection Results in Table Form screen displays. |  |
| 3 | Enter Filter Fields | Maintain filter values and choose Go. | A list of inspection lots is displayed. |  |
| 4 | Select Inspection Lots and Inspection Characteristics | Select the inspection lots for which inspection results shall be recorded and choose Record Multiple Results.In the pop-up window Select Characteristics for Result Recording, select the master inspection characteristics for which inspection results shall be recorded and choose button OK. | The Record Inspection Results in Table Form screen displays.Note The system creates one table line item per inspection lot operation. Each master inspection characteristic is displayed in a separate column. The valuation of the inspection characteristic is displayed in a separate adjacent column. If a master inspection characteristic is assigned to another inspection operation, the respective table field is grayed out. |  |
| 5 | Show Inspection Details (Optional) | Click one inspection characteristic in the table and choose Show Details. | The side panel opens and detailed inspection data are displayed (e.g. inspection specifications, master inspection characteristic, inspection method, test equipment, and inspection remarks). |  |
| 6 | Show Work Center (Optional) | Choose Settings button in the upper right corner of the table. In the Define Column Properties popup, select Work Center and choose OK. | An additional Work Center column is displayed. |  |
| 7 | Enter Inspection Results | Enter inspection results. See above for example data. | For qualitative results, a corresponding value help is provided. Quantitative inspection results can be entered directly.Note Depending on the defined valuation mode (check inspection method details), the valuation is either done automatically by the system or must be done manually by the user.If an inspection result requires an inspection remark (check master inspection characteristic settings), it is possible to navigate to the next inspection result. Open Details side panel and maintain the inspection remark in section Remarks. |  |
| 8 | Save Inspection Data | Choose Save. | Inspection results are saved and a success message is displayed. |  |

##### Display Quality Engineer Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the inspection lot depending on the inspection result. As an optional entry point for making this usage decision, you can use the app Quality Engineer Overview (F2360). Furthermore, the Quality Engineer Overview (F2360) app displays inspection lots without an inspection plan (e.g. if automatic assignment of an inspection plan is not set up in the material master or if automatic assignment failed), inspection lots without usage decision, inspection lots ready for usage decision. If negative inspection results are recorded, you can check the detect details in app Manage Defects (F2649) directed from the app Quality Engineer Overview (F2360) via the cards Inspection Lots with Defects, Top Defective Materials, or Top Defects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Engineer Overview (F2360). | The Quality Engineer Overview (F2360) screen displays. |  |
| 3 | In Card: Inspection Lots without Inspection Plan choose one entry (Optional) |  | To assign missing data and ensure automatic inspection plan determination for further usage. |  |
| 4 | In Card: Select Inspection Lots Without Usage Decision (Optional) | Choose card Inspection Lots Without Usage Decision | You can process further as described in the chapter [Make Usage Decision](#unique_77) [page ] 135. |  |
| 5 | Select the Corresponding Inspection Lot you have created before (Optional) | In the inspection lot list, select the inspection lot. | The Manage Usage Decisions screen displays. Alternative Entry to chapter [Make Usage Decision](#unique_77) [page ] 135. |  |
| 6 | Select one of the Inspection Lot by Results Recording Status (Optional) | Select one of the Inspection Lot by Results Recording Status (Optional) | Alternative Entry to chapter [Make Usage Decision](#unique_77) [page ] 135. |  |
| 7 | Select Card Inspection Lots Ready for Usage Decision (Optional) |  | All inspection lots with positive results get collectively an accepted usage decision (e.g. defaulted by A1) when pressing button Make Quick Usage Decision. |  |
| 8 | In Card: Inspection Lots with Defects (Optional) | (In case negative inspection results have been recorded and auto-defect recording has been defined). Select one of the inspection lot origins, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 9 | In Card: Top Defective Materials (Optional) | (In case failed inspection results have been recorded and auto-defect recording has been defined). Select one of the materials inspected, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 10 | In Card: Top Defects (Optional) | (In case negative inspection results have been recorded and auto-defect recording has been defined). Select one of the defect codes recorded, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |

##### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the goods receipt depending on the inspection result. If you don't want to use the Quality Engineer Overview (F2360), you can open the Manage Usage Decisions (F2345) app directly.

|  |
| --- |
| Note In case of positive recorded results (in previous step), immediate auto-usage decision with "Accepted-unrestricted stock (A1)" is performed in background if respective plant specific settings are prepared in customizing. In this case, you can skip this chapter. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Usage Decisions (F2345). | The Manage Usage Decisions screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Purchasing Document: <Purchase Order> (from previous steps). | If Purchase Document isn't displayed in the filters, choose Adapt Filters. On the dialog box Adapt Filters, select Purchase Document and choose OK. Choose Go.Alternatively, you can search for the batch <Batch ID> or <Inspection Lot ID> (from previous step). |  |
| 4 | Select Corresponding Inspection Lot | In the inspection lot list, select the corresponding inspection lot. | The Inspection Lot screen displays. |  |
| 5 | Display Defects | Scroll down to the Defects area. Check the details of Defects. | Only available when you have recorded a negative result with defect. For a pest control rejection, a pest infestation type defect will be displayed. |  |
| 6 | Choose Edit and Add Document (Optional) | Choose Edit. In the Document section choose Upload, select the path and add the document. | For example, to upload pictures to visualize the defect. |  |
| 7 | Enter UD code | Go to Usage Decision tab.Depending on the inspection result, select one of the following two options and then confirm with Save.UD code: A1 (Accepted – unrestricted stock)A2 (Accepted-unrestricted – minor quality)A3 (Accepted-unrestricted-sample consumption)Negative ResultUD code: R1 (Rejected – blocked stock)R210 (Rejected-return supplier w/o delivery)R220 (Rejected-return supplier with delivery)Choose Yes if dialog Confirmation Prompt appears. | Note For source inspection, you can use the same UD codes as for inspection lots which are created from goods receipt posting.Because source inspection lots are not stock relevant, the follow-up-action behind the codes are not relevant.Note If the material is batch managed, you must assign a batch to the inspection lot before saving.One way is described in this test script by preparing a batch for assignment.Another way of working with source inspection, the batch can be prepared due to close alignments with supplier. In this case, the batch can be assigned to the purchase order during purchase order creation or by changing the purchase order ideally when the tanker leaves the supplier side respective latest when the tanker arrives at customer side. |  |
| 8 | Save Usage Decision | Choose Save. | The usage decision is made with regard to the raw material. |  |

##### Display Material Stock after Quality Inspection (Optional)

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
- Negative Result ‘Return to Supplier w/o Delivery’ (R210): quantity is reduced in Quality Inspection Stock
- Negative Result ‘Return to Supplier with Delivery’ (R220): quantity is increased in return storage location Blocked Stock and quantity is reduced in Quality Inspection Stock

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock – Single Material screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and press Enter.Material:RM0501 |  |  |
| 4 | Check Stock Quantity | Check the changed quantities of the Quality Inspection Stock, Unrestricted Use Stock (in case of positive usage decision) or Blocked storage location 331C/331R (in case of negative usage decision). | The stock quantities for raw material RM0501 and <Batch ID> are updated based on the quality inspection and respective usage decision of the previous steps. |  |

##### Display Inspection Results History (Optional)

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Results History (F2428). |  |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Aggregation Level: Master Inspection Characteristic | A list of inspection characteristics displays. |  |
| 4 | Select Inspection Characteristics | Select an Inspection Characteristics, for example, YQM00006 Relative Humidity. | Some information is shown about the selected characteristics for process control, for example:A diagram displays the development of the recorded results for this characteristic with lower and upper limit.Statistical Values for Control Chart and Process Capability. E.g: Mean Value. |  |
| 5 | Change Filter Fields | Make the following entries and choose Go.Aggregation Level: Inspection Plan Characteristic | A list of inspection characteristics displays.If master characteristics are used in different plans, you can select them (plan specific) by using the filter Inspection Plan Characteristic. |  |

#### Procurement of Stock Material without QM – Packaging

##### Create Purchase Requisition

The components which need to be purchased in this process are packaging components for the production of the finished materials FG0502, FG0511 or FG0512. The MRP run done earlier for material FG0502 has resulted in requirements for the packaging materials PK0501, PK0502, PK0507, PK0508 and PK0504 which need to be purchased.

The creation of purchase requisitions can be done either via MRP run (option 1) or manually (option 2).

Option 1 is already covered by previous steps and can be checked in the Stock-/Requirements List (logon as production planner and choose app Monitor Stock / Requirements List (MD04). If a purchase requisition is available in the stock-/requirements list, note down the purchase requisition number. This one can be used to approve a purchase requisition in the overnext section.

Option 2 can be used independently from the creation of purchase requsition by MRP.

###### Option 1: Create Purchase Requisition via MRP run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step you create purchase requisitions by MRP run. This process step can be executed when scope item 5HK (Quality Management in Discrete Manufacturing – Consumer Products) or 5OI (Production Capacity Evaluation and Leveling – Consumer Products) is activated in the system.

The components which need to be purchased in this scope item are components for the production of the finished materials FG0502, FG0511 or FG0512. The creation of PIRs for material FG0502 will result in requirements for the components which need to be purchased.

Prerequisite

The scope item 5HK (Quality Management in Discrete Manufacturing – Consumer Products) or 5OI (Production Capacity Evaluation and Leveling – Consumer Products) must be activated in the system.

Procedure

If you use 5HK scope item, follow the steps described in the following sections:

Chapter “Anonymous Forecast and MRP”

- Create Planned Independent Requirements
- Material Requirements Planning at Plant Level
- Evaluate Stock / Requirements Situation

If you use 5OI scope item, follow the steps described in the following sections:

- Create Planned Independent Requirements
- Material Requirements Planning at Plant Level

|  |
| --- |
| Note If no purchase requisitions are created for the materials, either the available stock of the raw and packaging materials is sufficient for the planned production volume or a production version is automatically selected during MRP run which does not require the respective material. In that case use “[Option 2: Create Purchase Requsition manually](#unique_91)” to be able to run through the test case. |

###### Option 2: Create Purchase Requisition manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Purchase Requisition can be created manually.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Purchase Requisitions - Professional (F2229). | The Manage Purchase Requisitions – Professional screen displays. |  |
| 3 | Create Purchase Requisition | Choose Create. | The Purchase Requisition screen displays. |  |
| 4 | Enter Document Type | Enter Document Type: Pur. Requisition (NB) and select Automatic Source Determination. |  |  |
| 5 | Add Item | In the Items section, choose Create, then choose Material to add new items to Purchase Requisitions. | The Purchase Requisition Item screen appears. |  |
| 6 | Enter detail data | Enter the following values in General Information section:Item Category: StandardMaterial: PK0502Plant: 3310Enter the following values in Quantity and Date section:Quantity: 10.000,00Delivery Date: <default value>Requisition Date: <default value>Release Date: <default value>Enter the following values in Contact Information section:Purchasing Organization: 3310, and choose Enter.Purchasing Group: 002, and choose Enter.Go to Source of Supply area and make sure one source has been assigned. If no Source of Supply is assigned, choose button Assign Source of Supply.Choose Apply. |  |  |
| 7 | Save your entries | Choose Create and confirm the popup message. | The Purchase Requisition is created. |  |
| 8 | Repeat Steps | Repeat steps for PK0501, PK0507, PK0508 and PK0504. |  |  |

Result

The Purchase Requisition is created.

##### Approve Purchase Requisition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you release a purchase requisition. If the total amount of PR > 500 AED and purchase group is 002, then the purchase requisitions should be approved. To decide which PRs need approval, please refer to [Configure Flexible Workflow for Purchase Order](#unique_18) [page ] 32 in Preliminary step.

Prerequisite

A purchase requisition must exist for release.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Manager - Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F5331). | A list of all items in the inbox is displayed. |  |
| 3 | Search for Purchase Requisition Status | Make the following entry and choose Enter:Search: <Purchase Requisition number> | The Purchase Requisition is displayed. |  |
| 4 | Approve Purchase Requisition Item | Select the Purchase Requisition Item on the left side of the screen and choose Approve at the bottom right. | The Submit Decision screen is displayed. |  |
| 5 | Enter Approval Reason | Enter the approval reason if necessary, and then choose Submit. | The Purchase Requisition Item is approved. |  |

|  |
| --- |
| Note If an attachment is uploaded during purchase requisition creation, in My Inbox App, the attachment can be found under Attachments tab of the purchase requisition item. |

##### Automatic Conversion of Purchase Requisition to Purchase Order

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Schedule Purchasing Jobs - Advanced (F1702). | The Application Jobs screen displays |  |
| 3 | Create Job | Choose Create. | The New Job screen displays. |  |
| 4 | Define a Job | On the New Job: Automatic Creation of Purchase Orders from Requisitions screen, make the following entries:Choose 1 Template Selection and go to 1. Template Selection area to make the following entries:Job Template: <Job Template>, for example, Automatic Creation of Purchase Orders from RequisitionsJob Name: <Job Name>, for example, Automatic Creation of Purchase Orders from RequisitionsChoose Step 2 and go to 2. Scheduling Options area to make the following entries:Start Immediately : <selected>Start: <Current Time>Note If the job needs to be run on a regular basis, choose Define Recurrence Pattern.Choose Step 3 and go to 3. Parameters area to make the following entries:Per Requisition:<selected>Per Company Code: <selected>Per Contract: <selected>Purchase Requisition: <Created PR Number>Note Set Parameter settings according to your needs.Choose Schedule. | The job is created. |  |
| 5 | Convert Purchase Requisition to Purchase Order | On the Application Jobs screen.Go to Jobs (X) area and check the status until it changes to Finished. | The Job automatically converts Purchase Requisition to Purchase Order. |  |
| 6 | Check Result | Choose Result.Choose Preview. | The Purchase Order is created. |  |

|  |
| --- |
| Note You may go to the Fiori Launchpad main screen. On the Fiori Launchpad main screen, choose Search button on the top. Choose Purchase Order from the drop-down box, and enter the Purchase Order number in the field Search In: Purchase Orders. Select the Purchase Order you want to display on the Search screen. |

##### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you release a purchase order. If the total amount of PO > 500 AED and purchase group is 001, then the purchase orders should be approved. To decide which POs need approval, please refer to Configure Flexible Workflow for Purchased Order in Preliminary step.

Prerequisite

A purchase order must exist for release.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862) . | A list of existing Purchase Orders is displayed. |  |
| 3 | Search for Purchase Order Status | Make the following entry and choose Enter:Search: <Purchase Order number> | The Purchase Order is displayed. |  |
| 4 | Approve Purchase Order | Select the Purchase Order on the left side of the screen and choose Approve at the bottom right. | The Submit Decision screen is displayed. |  |
| 5 | Enter Approval Reason | Enter the approval reason if necessary, and then choose Submit. | The Purchase Order is approved. |  |

|  |
| --- |
| Note If an attachment is uploaded during purchase order creation, in My Inbox App, the attachment can be found under Attachments tab of the purchase order. |

##### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity posts the receipt of goods with reference to an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Post Goods Receipt for Purchasing Document (F0843). | The Post Goods Receipt for Purchasing Document screen is displayed. |  |
| 3 | Search for Purchase Order | Enter your Purchase Order number in the search field and choose Enter. | A list of Purchasing Documents displays. |  |
| 4 | Select Item | Select your line item for which goods receipt is to be posted. Inside the item view, ensure Storage Location is 331C and select Apply at the bottom. | The system displays the data for the goods receipt on the Goods Receipt screen. |  |
| 5 | Enter Delivery Note | On the main screen, enter a Delivery Note on the header. | The Post Goods Receipt screen displays. |  |
| 6 | Post | Choose Post. | The system displays the message Material Document <Document No> posted. |  |

#### Evaluations

##### Batch Information Cockpit – Top-Down and Bottom-Up Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this functionality you can identify which batches are delivered to which customer and which raw material batches are used for the production of which finished product. You can adapt the selection in the Batch Information Cockpit to customer-specific requirements by creating user-specific groups. You can get additional information by using subsequent actions.

In this case the evaluation is limited to the purchasing process. As soon as you have purchased the raw materials RM0501 and/or delivered the finished good to a customer the evaluation is automatically enhanced with these information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto the SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad using the Quality Technician role. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Batch Information Cockpit (BMBC). | The Batch Information Cockpit screen displays. |  |
| 3 | Select batches | On the Batch Information Cockpit screen, make the following entries.Go to Material (Original) tab.Material (Original): RM0501Plant: 3310For batch class and characteristics relevant materials, refer to Master Data, Organizational Data, and Other Data section.Choose Execute Selection. | One or multiple batches are displayed in the left screen area Selection Result for Batches. The standard sorting is done per material number. |  |
| 4 | Expand Selection | In the section Selection Result for Batches, select checkbox for RM0501 and then choose Expand subtree or Expand node. | The selection result is analyzed and a batch for further investigation is identified. |  |
| 5 | Start Analysis | Right click on one selected batch and choose either Usage (Top-Down) or Usage (Bottom-up). | The batch where-used list displays. |  |
| 6 | Analyze the batch where used list | The usage of the batch can be analyzed and the specific documents (such as batch master record, production orders and sales order) can be accessed via double click. |  |  |
| 7 | Analyze assigned Inspection lots | Mark one line in the Details (Usage) table and choose button Inspection Lots to review inspection lots assigned to the selected element. |  |  |
| 8 | Analyze material document | Select one document and choose Documents. | The usage displays again and after selecting documents the respective material document display. |  |
| 9 | Go to the material document | Select the material document in the pop up and choose Choose (F2).Note To display the material document, you need further authorizations that are granted by your company, for example, SAP_BR_INVENTORY_MANAGER. | The material document displays.Note Your user should have the appropriate authorizations. |  |

|  |
| --- |
| Note The materials PK0501, PK0502 and PK0504 are also batch managed. You can execute the steps mentioned above for these materials but need to skip the inspection lot analysis as these packaging materials are not subject to Quality Management during procurement process. |

### Quality Management in Discrete Manufacturing - Consumer Products (5HK)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

As soon as the capacity planning and leveling process and also the procurement of production components is completed, the production process with full integration of Quality Management into discrete manufacturing is executed. The process is realized as a Make-to-stock scenario for batch-managed goods with QM integration for in-process control and (early) goods receipt inspection.

The process describes a two-stage production process for coffee displays. The first stage reflects the roasting and packaging process of medium respective dark roasted beans under consideration of a fixed capacity of the roasting drums. During the roasting, cooling and packaging steps, the process is permanently monitored by quality inspection. During roasting process, the temperature, browning of the beans and other parameters are permanently checked by QM until all parameters are ful-filled.

Moreover, the functionality of an early goods receipt inspection is used to handle the End-Product Control of the unpacked, finished product as flexible as possible. This means that the end-product control can be started during the production pro-cess, or alternatively after goods receipt into quality stock.

The second stage reflects a display packaging process where two different finished products (bags of medium and dark roasted coffee beans) are packed into a display. In this second process step, a quality inspection after goods receipt from production with quality inspection stock is set up.

The production process covers the conversion of planned orders to production orders, order release, material staging and picking, confirmation of order operations or complete orders, and goods receipt posting. Order-based targets and actual costs are created to ensure fully integrated material and value streams.

#### Anonymous Forecast and MRP

##### Option 1: Create Planned Independent Requirements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create Planned Independent Requirements (PIRs). PIRs are used to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split according to dates. In Option 1 these PIRs will be loaded by manually.

|  |
| --- |
| Note Instead of creating a single requirement, sometimes one or more planned independent requirements can be maintained and included in a requirement plan for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries and choose Go:Plant: 3310Period Indicator: Weekly(W)Version Active: Select all optionsMaterial: FG0502 | The searched material item displays. If the material filter is not directly available choose Adapt Filters, select the Material Filter, enter the desired material and choose OK.Note If no PIRs for FG0502 have been maintained in the system before, the selection is empty in the app. In that case please leave this app and access the app Create PIRs (MD61), make the following entries on the Create Planned Independent Requirements: Initial Screen and choose Continue:Plant: 3310Period Indicator: Weekly (W)Version: 00Material: FG0502Choose Save and restart with step 1. |  |
| 5 | Edit PIRs. | Select the material item and choose Edit in the upper right corner of the screen.On the Edit PIRs screen, enter quantities per week, for example:Week 1 (current week + 1 week): 40 PCWeek 2 (current week + 2 weeks): 80 PCWeek 3 (current week + 3 weeks): 80 PCWeek 4 (current week + 4 weeks): 100 PCWeek 5 (current week + 5 weeks): 80 PCWeek 6 (current week + 6 weeks): 80 PCVersion is Active: YES | Note If already stock for FG0502 is available, increase the quantity for PIR of current week + 1 for the stock already available. As an alternative, remove the stock to get planned orders in next step. |  |
| 6 | Save PIR's Draft | Choose Save in the bottom right corner of the screen. | The PIRs draft is saved. |  |

##### Option 2: Create Planned Independent Requirements by Upload File

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use planned independent requirements to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split over time according to dates. In Option 2, these PIRs will be loaded by Upload File.

|  |
| --- |
| Note Instead of creating a single requirement, sometimes a requirements plan that includes one or more planned independent requirements can be maintained for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Weekly(W)Version Active: Select all optionsMaterial: FG0502 | Note If no PIRs for FG0502 have been maintained in the system before, the selection is empty in the app. In that case please leave this app and access the app Create PIRs (MD61), make the following entries on the Create Planned Independent Requirements: Initial screen and choose Continue:Plant: 3310Period Indicator: Weekly (W)Version Active: 00Search: FG0502Choose Save and restart with step 4. |  |
| 5 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 6 | Download Template | Select the material item and choose Edit in the upper right.Choose button Download to Spreadsheet to download the template to your local work space.Then choose Back without saving. |  |  |
| 7 | Edit PIRs. | Open the Spreadsheet in an adequate program and enter quantities per period, for example:In the upcoming several weeks, enter following values for PIR:Week 1 (current week + 2 weeks): 40 PCWeek 2 (current week + 3 weeks): 80 PCWeek 3 (current week + 4 weeks): 80 PCWeek 4 (current week + 5 weeks): 100 PCWeek 5 (current week + 6 weeks): 80 PCWeek 6 (current week + 7 weeks): 80 PCVersion is Active: YESSave your PIRs in the spreadsheet. | Note We recommend to check the stock for finished material before entering the PIRs (see prerequisites). If there is still stock available for FG0502, enhance the first PIR for the stock already available to generate a reproducable capacity situation (e.g. actual stock plus 250 PC). To check the stock, you can Log on to the SAP Fiori Launchpad as a Production Planner and Open the app Manage Material Coverage - New Version (F0251A). |  |
| 8 | Upload PIRs. | On the Maintain PIRs screen, choose button Upload and Edit. On the Pop Up select the file you adjusted in previous step and choose Continue. Review the uploaded data. |  |  |
| 9 | Save PIRs Draft | Choose Save at bottom right. | The PIRs are saved |  |

##### Material Requirements Planning at Plant Level

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use Material Requirement Planning (MRP) to tailor available capacities and receipts on time to suit requirement quantities. As a result, single-item multi-level requirement planning is performed for plant 3310.

Prerequisite

The Make-to-Stock finished goods are planned at plant level. There is now a requirement for FG0502 in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirements Planning (MRP)Job Name: MRP for FG0502Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: <select>Recurrence Pattern: Single RunChoose OK.Choose Step 3.For 3. Parameters section:Plant: 3310Material: FG0502Changed BOM Components: <select>Stock Transfer Materials: <select>Scheduling: 2Planning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG0502 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

##### Evaluate Stock/Requirements Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock/requirements situation for Make-to-Stock finished goods (FG0502) and the components relevant for production (finished, packaging and raw materials) in the stock/requirements list after the requirement planning is performed.

Prerequisite

Requirement planning is carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments (F2101A) screen displays. |  |
| 3 | Check Default Setting | Choose the user icon and select App Settings.In the MRP Settings dialog box, check Manage Material Coverage - New Version (F0251A) that if toggle button is ON. | If the toggle button is ON, in following steps, it will be navigated to Manage Material Coverage - New Version (F0251A).If the toggle button is OFF, in following steps, it will be navigated to Check Material Coverage - Old Version (F0251).In following steps, we describe the steps with the toggle button is ON. |  |
| 4 | Check Area of Responsibility | Choose the user icon and select App Settings. In the MRP Settings dialog box, choose Area of Responsibility.Check if only this entry displays, and choose OK:Plant 1 AE 3310MRP Controller (001)Choose + to select this entry if not displayed; choose the Delete icon to remove any other plant entries and then choose OK. |  |  |
| 5 | Select Material | Search in the Material bar, select the following materials and then choose Go.Material: FG0502Material: FG0511Material: FG0512Material: PK0501Material: PK0502Material: PK0504Material: PK0507Material: PK0508Material: RM0501 | The Materials screen displays. |  |
| 6 | Review Stock / Requirements List | Select the following materials on the screen and choose Manage Materials.Material: FG0502Material: FG0511Material: FG0512 | The detailed stock / requirements list for each material displays. |  |
| 7 | Display Planned Order | From the list of materials on the screen, select the material for which you want to check for the planned order.Material: FG0502Material: FG0511Material: FG0512On the Material Details subscreen, choose PldOrd XXX in the MRP Element column.Note The BOM explosion during the MRP run has generated dependent requirements for the demand-driven planned components. If there is not enough inventory to fulfill the requirements, planned orders and purchase requisitions are created for both inhouse-produced and externally-procured materials. | The selected planned order displays.Note The planned order is generated only when there is storage for these materials.If you want to display more information of the planned order, choose Document Info at the bottom of the dialog box. |  |
| 8 | Rescheduling Check (Optional) | On the Stock/Requirements List tab, the Rescheduling column displays the rescheduling status of the following MRP elements.PurReqPurchase OrdersPlanned OrdersProduction OrdersProcess OrdersIf needed, you can choose the following icons in Rescheduling column for corresponding functions:Reschedule in (bring operation forward if the receipt element lies after the requirement date)Reschedule out (postpone operation, if the receipt element lies before the requirement date)Plan Process according to scheduleCancel ProcessExcess StockExcess in individual segment |  |  |
| 9 | Display Stock situation of Raw and Packaging Materials | Return to the Manage Material Coverage - Net and Individual Segments screen, select following materials and choose Manage MaterialsMaterial: PK0501Material: PK0502Material: PK0504Material: PK0507Material: PK0508Material: RM0501 |  |  |
| 10 | Simulation and solving shortage situations (Optional) | If a shortage situation for components exists, the number in the Available column is marked in red and an arrow is visible next to the amount. Click on that arrow and you will be guided to a simulation section. In this section you get provided different solutions how to overcome the corresponding shortage situation. Choose Simulate in the Actions column to simulate your preferred option. Afterwards, you can either choose Cancel in the Actions column to return to previous planning situation or choose Apply to take over the proposed simulation in the operative Stock/Requirements List. |  |  |

#### Production Order Conversion and Available-to-Promise Check for Packed Roasted Coffee Beans

After planning process for the finished material FG0502 (Display consisting of medium and dark roasted Coffee Beans Bags) and purchasing of the relevant components the production process starts with the production of the components for the display. Two finished materials FG0511 (Carton 12 x 1kg Bags Medium Beans Arabica) and FG0512 (Carton 12 x 1kg Bags Dark Beans Arabica) are needed for the production of the finished material FG0502 (Display Med + Dark 48 * 1kg Arabica), that combines these two finished materials into one display. The production process for the finished material FG0511 (Carton 12 x 1kg Bags Medium Beans Arabica) with full integration into Quality Management is described in the next sections.

The production process consists of three operations: Roasting (of the beans), Cooling and Packaging (in 1 kg bags / 12 bags in one carton). In-process quality inspection is relevant for the roasting and packaging process. Moreover, a goods receipt inspection (as early goods receipt inspection) is part of this process.

##### Convert Planned Orders to Production Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Daily MRP run creates planned orders for goods to be produced internally. This process step shows you how to convert the planned orders to production orders for finished materials when reached the planned start date.

Prerequisite

The MRP run has generated planned orders for FG0511 (finished material).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A). | The Manage Material Coverage screen displays. |  |
| 3 | Select Material | On the Manage Material Coverage screen, enter the following data and choose Go.Material: FG0511Plant: 3310Shortage Definition: MRP StandardChoose the row of the filtered material to check more details. | The Manage Material Coverage screen displays with more details. |  |
| 4 | Find Planned Order | Check the generated planned orders.If no planned orders are generated, it could be because FG0511 has sufficient amount of stock in store. In this case, remove some stock or enhance the amount for PIRs for FG0502 and run MRP again to generate planned orders. |  |  |
| 5 | Add Planned Order Long Text (Optional) | Click on the planned order number (PldOrd XXXX) under column MRP Element. In the pop-up dialog PldOrd XXXX, choose Change Planned Order.On the Change Planned Order screen, choose tab Long Text, enter the text, and choose Save. | The long text maintained here can be later copied to the converted production order. |  |
| 6 | Convert Planned Order to Production Order | Select Convert from Edit dropdown list in the Actions column for a planned order (PldOrd XXX).In the Convert Planned Order XXX dialog box, choose Convert to Production Order, confirm Delivery Date and Quantity. Choose Convert.Choose the Refresh button on the top of the material overview section, scroll to the created production order and note down the production order number for material FG0511. | The production order is created.Production Order Number ___________________. |  |
| 7 | Convert Planned Order to Production Order for Semifinished Goods (Optional) | Open Manage Planned Orders (F4170). | The Manage Planned Orders screen displays. |  |
| 8 | Filter Planned Orders (Optional) | On the Manage Planned Orders screen, enter the following data and choose Go.Material: FG0511In the Planned Orders area, you can check the generated planned orders.Select Convert from Edit drop down list in the Actions column for a planned order (PldOrd XXX) .In the Convert Planned Order XXXX dialog box, choose Production Order, confirm Delivery Date and Quantity. Choose Convert.You can also perform mass conversion for production order/process order/purchase requisition by selecting multiple planned orders and choosing Convert to. The system then performs a check to validate if the selected planned orders can be converted to the designated order types.A success dialog box pops up if all planned orders are validated successfully. Choose OK and the message is displayed: Planned order converted successfully. The successful message is displayed at the bottom left.A warning dialog box pops up to prompt the number of failed orders and possible reasons if failed orders exist. Choose Convert to XXX, and the failed messages and successful messages are displayed at the bottom left. | If no planned orders are generated, please first ensure if AOR is maintained correctly for plant 3310 and MRP controller 001.Check the message:Planned Order XXX converted to Production order XXX |  |

##### Review Material Availability Status for Production Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review material availability status for production orders.

Prerequisite

Production orders are created for semifinished material FG0511.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). |  |  |
| 3 | Check Default Area of Responsibility (Supervisor) | Choose the user icon and select App Settings. In the Area of Responsibility dialog box, choose Production Supervisor.Check if only this entry displays, and choose OK:Plant 1 AE 3310MTS DI - Valuated (YB1)Choose + to select this entry if not displayed; choose the Delete icon to remove any other plant entries and then choose OK. | The Manage Production Order screen displays. |  |
| 4 | Select Production Order | On the Manage Production Orders (F2336) screen, choose Adapt Filters to display more filter options.In the Adapt Filters dialog box, choose More Filters. Select Material and Production Plant and choose OK. Choose Go.Status: CreatedMaterial: FG0511Production Plant: 3310 | The Material and Production Plant fields are added to the filter bar.The searched orders are displayed. |  |
| 5 | Review Material Availability Status | In the Issues column, check the Component Issue icon to the right of the order to display the missing components. | For FG0511, the expected missing components in storage location 331B are RM0501, PK0501, PK0504 and PK0507. The raw and packaging materials are supplied after the Material Staging for Finished Materials Step.For FG0512, the expected missing components in storage location 331B are RM0501, PK0502, PK0504 and PK0507. The raw and packaging materials are supplied after the Material Staging for Finished Materials Step.Note However, it’s also possible that the components mentioned above are not a missing component. This happens when you have supplied the components already or if an overstaging has happened for previous orders and these quantities are not reserved, yet. |  |

#### Production Order Processing for Packed Roasted Coffee Beans

##### Execute Material Staging

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to stage materials for finished material production.

|  |
| --- |
| Note If there is sufficient amount of stock available in the production storage location, then no line items are generated. In this case, you can skip this step and proceed onward. |

Prerequisite

Stock must be available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stage Materials for Production (MF60). | The Material Staging for Planned Orders screen displays. |  |
| 3 | Enter Details | Make the following entries and choose Execute.In the Staging Types section:SLoc Level: <select>Plant: 3310Selection Horizon for Reqmts: <date must be in the future - after scheduled start date of production order created>On the Production/Process Orders tab:Order: <Production Order Number for Finished Material> | The Pull List: Storage Location Level screen displays. |  |
| 4 | Choose Replenishment Elements | In the Total Reqmts table, select the line items and choose Replenishment Proposal on the top of the screen.Review staged quantities and choose Replenishment Elements. |  |  |
| 5 | Enter Replenishment Storage Location and Stage Material | In the Replen. Element table, in the RepLoc column, enter 331C for staged materials.In the Batch field, select an appropriate batch available in storage location 331C for the corresponding material and press Enter. Select all entries.Choose Stage. |  |  |
| 6 | Save | Save your entries.Missing materials are transferred to the shop floor from the designated storage area.With this step, the shortage of material RM0501, PK0501, PK0504 and PK0507 for the finished production order of FG0511 is supplied. | Materials are staged for production. |  |

##### Release Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to release the order at header level, which releases the entire order and all its operations. The order and the operations receive the REL (released) status.

Prerequisite

The production order created by the MRP controller is assigned a release date in accordance with the scheduling margin key.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). | The Manage Production Order screen displays. |  |
| 3 | Check Default Area of Responsibility (Supervisor) | Choose the user icon and select App Settings. In the Area of Responsibility dialog box, choose Production Supervisor, check if this entry displays and choose OK:Plant 1 AE (3310)MTS DI - Valuated (YB1)Choose + to select this entry if not displayed; choose the Delete icon to remove any other plant entries. Choose OK. |  |  |
| 4 | Select Production Order | On the Manage Production Orders screen, choose Adapt Filters to display more filter options. In the Adapt Filters dialog box, choose More filters. Select Material and Production Plant and choose OK. Choose Go.Enter the following filter criteria, and choose Go:Status: CreatedMaterial: FG0511Production Plant: 3310 | The Material and Production Plant fields are added to filter bar.The searched order displays. |  |
| 5 | Assign Batch Number to Production Order before Order Release | Select the order you want to release and choose Edit.In the Production Order Change header move to the tab Goods Receipt.Either click on the Create button next to the Batch field to create an automatic batch number or enter a batch number in the field Batch manually.Choose Save. Confirm the popup for the creation of a new batch number. | Make a note of the batch number.Batch: __________Note By adopting the customizing settings, an automatic creation of batch number either during production order creation or production order release is possible. |  |
| 6 | Execute Release | Select the searched order once again. Choose Release. |  |  |

Result

The production order is released. With release of the production order, an inspection lot is created for material FG0511 that contains quality inspections for operations 0010 (Roasting) and 0030 (Packaging) which are performed within the production process (In-Process Control).

At the same time, an inspection lot for the goods receipt inspection is created. Thus, the early End Product Control for material FG0511 can be started in parallel to the running production process and before goods receipt for production order is posted.

##### Goods Issue of Batch-Managed Raw Materials via Pick List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The withdrawal of the raw materials is used for the order. This withdrawal can be done by using the picking list.

|  |
| --- |
| Note If the material is set for backflush (in material master or resource), the withdrawing is done automatically after you confirm the operation or the whole order. Backflushing should not be used for batch-managed components (to ensure that the physically picked and consumed batch is the same as the recorded batch). |

|  |
| --- |
| Note In this scope item the packaging materials PK0501 and PK0504 are (even though it is batch managed) subject to backflush due to process requirements and hence picking will only be executed for RM0501. |

Prerequisites

Ensure that sufficient material is present on stock. If not enough stock is present, execute Create Initial Material Stock in the preliminary steps of this scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Pick Components for Production Orders (CO27). | The Picking List: Initial Screen displays. |  |
| 3 | Enter Restriction and Run | Make the following entries and choose Execute:Profile: 000002Production Order: <Order ID> (from previous steps)Plant: 3310 | The Order Information System: Detail List of Components screen displays. |  |
| 4 | Picking Raw Materials | Select the relevant reservations for RM0501 and choose the upper left Picking. | The Picking list screen displays. On this screen, a list of all the selected reservations is displayed. |  |
| 5 | Batch Determination | RM0501 is managed by batches.You have two options:Manually enter the relevant batch number.Execute a Batch Determination by selecting the line for RM0501 and choose button Batch Determination. The Batch determination result is displayed. You can either do changes in the proposed selection or directly accept the proposal. Choose Copy. The number of line items available now in the Picking list corresponds to the number of selected batches. | Back to Picking list screen.If multiple line items were selected in this step, the Picking list screen is displayed after completion of the last line item. |  |
| 6 | Post | Choose Post to post the goods movements. | The goods movements have been posted. |  |

#### Quality Management – Overview Inspection Lots for Packed Roasted Coffee Beans

##### Display Open Inspection Lots

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection lots are used to record the results for In-Process Control and the early Goods Receipt Inspection (End-Product Control), In this step, the references to production order are verified as well as the inspection lot quantities, sample sizes and postings can be reviewed.

The early goods receipt inspection can be started after Cooling (operation 0020) and while Packaging (operation 0030). Thus, dependent from capacity in the laboratory, the results recording can be started before goods receipt for production order is done.

Prerequisite

In this scope item, two inspection lots with different inspection lot origins are created automatically upon release of previous production order. Due to material master settings, the goods receipt inspection can be performed early.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots (F2343) screen displays. |  |
| 3 | Filter Fields | Make the following entries and choose Go:Plant: 3310Material: FG0511Inspection Lot Status: Outstanding | Alternatively, you can search for the batch <Batch ID> (from previous step). |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot with column Production Order equals to the Production Order: <Order ID> (from previous step). | The Production Order number assigned with Inspection lot is displayed.If the Production Order column does not appear, please choose the button Settings. In the View Settings dialog box, select Production Order and choose OK. |  |
| 5 | Check Inspection Lot | Under Inspection Type, check the different inspection types.Under Batch, check the batch from previous step. | Make a note of the inspection lot IDs:Inspection Lot ______________ with inspection type 03 (In-process insp. for production order).Inspection Lot ______________ with inspection type 04 (Goods receipt inspection from production). |  |
| 6 | Check First Inspection Lot by Selecting the Line | In the Origin tab, verify the referenced production order and inspection lot origin. | The production order number from which the inspection lot originates is displayed.Origin: Production |  |
| 7 | Check Inspection Lot Quantities | In the Origin tab, check the Lot Quantities, Sample Size and Postings. | The quantities according to the released production order quantity are displayed. The calculated sample size is displayed. Posting = 0 (not relevant). |  |
| 8 | Check Second Inspection Lot by Selecting the Line | In the Origin tab, verify the referenced production order and inspection lot origin. | The production order number from which the inspection lot originates is displayed.Origin: Goods Receipt from Production |  |
| 9 | Check Inspection Lot Quantities | In the Origin tab, check the Lot Quantities, Sample Size and Postings. | The quantities according to the released production order quantity are displayed. The calculated sample size is displayed. Posting = 0 (not yet started). |  |

#### Quality Inspection – In-Process Control (Operation Roasting) for Packed Roasted Coffee Beans

##### Display Routing for Inspection Characteristics

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An inspection during production (In-Process Control) is triggered by the release of a production order. When you release the production order, an inspection lot is generated, containing the inspection characteristics for operation 0010 (Roasting) and 0030 (Packaging). This inspection lot offers inspection points for repeating the inspections several times, until the expected results are reached (e.g. roast color of coffee beans). With inspection point Y01 in the routing header, only the last sample is valid for usage decision.

In this step, you display the routing (group counter 1 or 2) that is related to the finished good. The difference between the routings are only different drum roasting lines (Drum Roasting Line 1 and 2) used for production. Regarding quality inspection, it is exactly the same.

The routing defines all inspection characteristics used later in the quality inspection. As well you can review the inspection points definition for operation 0010 and 0030.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Routing (CA03). | The Display Routing: Initial Screen displays. |  |
| 3a | Enter Selection Fields | Make the following entries and choose Continue.Material: FG0511Plant: 3310 | The Display Routing: Overview displays.There are two routings (Drum Roasting Line 1 and Drum Roasting Line 2) with respective work centers in PP. The QM data remains the same. |  |
| 3b | Select Group Counter | Select Group Counter: e.g. 1 and choose Operations | The Display Routing: Operation Overview displays. |  |
| 4 | Review the Inspection Points Setting (operation 0010) | Double-click Operation 0010.Scroll down to the Quality Management: Inspection Points section.After reviewing, choose Back. | A No Reference inspection point is defined for this operation in the routing.Insp. point Completion is: Automatic valuation based on insp. Point definition |  |
| 5 | Review the Inspection Points Setting (operation 0030) | Repeat step 4.Double-click Operation 0030. |  |  |
| 6 | Review the Inspection Characteristics (operation 0010) | Select Operation 0010 and choose Inspection Characteristics.There are two Master Inspection Characteristics:One is Qualitative - Roast Color (medium) with Inspection MethodColor Check of Roasted Beans.The other is Quantitative - Temperature.For both, sample size 1 is to be inspected. | The Display Routing: Characteristics Overview displays.If Inspection Characteristics is not displayed, choose More. In the dialogue box, find Inspection Characteristics. |  |
| 7 | Review the Inspection Characteristics (operation 0030) | Repeat step 6.Select Operation 0030 and choose Inspection Characteristics.There is one Master Inspection Characteristic, which is Quantitative - Weight with 3 samples to be inspected. | You have now reviewed the inspection characteristics for which results have to be maintained within a later step.The sampling procedure can be displayed in detail with app Display Sampling Procedures (F2255) (optional). |  |

##### Display Quality Technician Overview (Optional)

Test Administration

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
| 2 | Access the App | Open Quality Technician Overview (F2361). | The Quality Technician Overview (F2361) screen displays.You can get an overview of the inspection lots with open results recording and the inspection lots without an inspection plan.Choose card Inspection Lots with Open Results Recording for Inspection Points if you want to record results for the In-Process Control inspection lot. |  |

##### Display Open Inspection Lots (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The In-Process Control inspection lot is used to record the results during production. In this optional step, the operations and characteristics are reviewed as well as assigned inspection methods with attachments used for quality inspection.

Prerequisite

In this scope item, the inspection lot is created automatically upon release of production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Material: FG0511Inspection Lot Status: OutstandingInspection Lot Origin: Production | Alternatively, you can search for the batch <Batch ID> (from previous step). |  |
| 4 | Select the corresponding Inspection Lot | In the inspection lot list, select the inspection lot with column Production Order equals to the Production Order: <Order ID> (from previous step) | The Production Order number assigned to Inspection Lot is displayed.If the Production Order column does not appear, please choose the button Settings. In the View Settings dialog box, select Production Order and choose OK.If needed, press button Show Details to make the column visible. |  |
| 5 | Choose Operation (optional) | In Result, choose operation Roasting (Medium). | Inspection Characteristics Roast Color and Temperature can be reviewed with their specifications and calculated sample sizes. |  |
| 6 | Choose Characteristic (optional) | Click Roast Color in the characteristics column. | For checking the attachment in the inspection method:If you have attached a document in the inspection method as described in the Preliminary Steps, the Quality Technician can review the attachment referring to step 6 to 8.A dialog box appears with the Characteristics Details with the link to the Inspection Method. |  |
| 7 | Display the Attachment (optional) | Under Documents, the attachment for an illustration of the Roast Color of coffee beans is displayed. |  |  |
| 8 | Display Text | In General, Long Text is displayed. |  |  |
| 9 | Choose next Operation (optional) | In Result, choose operation Packaging | Inspection Characteristic Weight can be reviewed with its specification and calculated sample size. |  |

##### Execute Quality Inspection with Inspection Points for Operation Roasting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the quality technician performs the quality inspection and records the inspection result(s) for operation 0010 (Roasting) in order to decide whether the next operation of the production order can be executed. The result is recorded in the inspection lot according to the defined inspection parameters in the routing. Here, free inspection points are used for result recording. Leveraging inspection points, you can have several inspections and can record multiple sets of characteristic results for a single operation. Each inspection point is valuated separately with a coded valuation.

Using Inspection point identifier Y01, only the last sample results are valid.

Prerequisite

The inspection is processed based on inspection lot. In this scope item, the inspection lot is automatically created upon release of the production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Record Results for Inspection Points (F2689). | The Record Results for Inspection Points screen displays. |  |
| 3 | Execute Search | If not already shown, expand search header, make the following entries and choose Go:Order: <Order ID>Work Center: DR050001 or DR050002 | Selected Order and Work Centers (Drum Roasting Machine 1 or Drum Roasting Machine 2) are displayed in the result list. |  |
| 4 | Open Inspection Points | Click on the line item of the search result. | A list of inspection points is displayed. If inspection point data have not been captured, continue with step 5. |  |
| 5 | Create New Inspection Point | Click On request to create a new inspection point. | Record Results for Inspection Points screen is displayed. |  |
| 6 | Maintain Inspection Results | Maintain the following inspection results and choose Save.a) Negative ResultRoast Color: 10 – Light brownTemperature:Valuation: Rejected (R) | Inspection point data is saved and the system displays the list of inspection points. |  |
| 7 | Create Next Inspection Point and Maintain Inspection Results (Optional) | Create a new inspection point as described in step 5 and maintain inspection results as follows:a) Negative ResultRoast Color: 20 – Moderate Light brownTemperature:Valuation: Rejected (R) | Further inspection point with inspection results is captured. |  |
| 8 | Create Last Inspection Point and Maintain Inspection Results | Create a new inspection point as described in step 5 and maintain inspection results as follows:a) Positive ResultRoast Color: 30 – Medium shade of brownTemperature:Valuation: Accepted (A) | Last inspection point is recorded. Only last sample is valid.Temperature and Roast Color of coffee beans are reached and roasting process can be finished. |  |

##### Display Inspection Results History (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, an overview about the history of inspection result is shown. For each quantitative Inspection Characteristic several statistical values and the development for recorded results are illustrated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Results History (F2428). | The Results History screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Aggregation Level: Master Inspection Characteristic |  |  |
| 4 | Select Inspection Characteristic | Select an Inspection Characteristic, for example Temperature. | Information is provided about the selected characteristics for process control, for example:A diagram displays the development of the recorded results for this characteristic with lower and upper limit.Statistical Values for Control Chart and Process Capability, for example Mean Value. |  |

#### Production Order Confirmation of Roasting and Cooling Process for Packed Roasted Coffee Beans

##### Confirm Production for Operation Roasting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the Consumer Products Industry, goods receipt and goods issue postings are usually done immediately during the physical movements of the materials to ensure batch traceability and data consistency. Order confirmations with backflush are done either at shift end or day end. The sum of the GI and GR quantity for the given order is then recorded within the confirmation and scrap quantities (optional). The time ticket confirmation allows recording either the default times for machine and labor usage, or record actual times for major deviations.

Prerequisite

The production order for the finished material FG0511 has been released and material staging has been carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). | The Enter Order and Operation screen displays. |  |
| 3 | Enter Order Number and Operation | On the Enter Order and Operation screen, make the following entries, and choose Go:Order: <Order ID> (from previous steps)Operation: 0010 | The Confirm Production Operation (F3069) screen displays. |  |
| 4 | Enter Fields in Quantities Section | In the Quantities section, check the following entries and make changes if required:Yield: <enter the amount you want to confirm>Scrap: <enter the amount you want to scrap> |  |  |
| 5 | Check Material Movements | The system shows you an overview table of all materials for which the withdrawal is done automatically with operation 0010 with the confirmation of the operation.Note All materials assigned to operation 0010 are not subject to backflush and the list is empty. |  |  |
| 6 | Enter Fields in Activities Section | In the Activities section, make the following entries:Setup: <setup time>Machine: <machine time>Labor: <labor time> | Confirmation is made. |  |
| 7 | Save your Entries | Choose Post and Complete to make final confirmation for this operation. | Confirmation has been created.Note For partial confirmation choose Post instead of Post and Complete. |  |

##### Confirm Production for Operation Cooling

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the Consumer Products Industry, goods receipt and goods issue postings are usually done immediately during the physical movements of the materials to ensure batch traceability and data consistency. Order confirmations with backflush are done at shift end or day end. The sum of the GI and GR quantity for the given order is then recorded within the confirmation and scrap quantities (optional). The time ticket confirmation allows recording either the default times for machine and labor usage, or record actual times for major deviations.

Prerequisite

The production order for the seminfinished material FG0511 has been released and material staging has been carried out. The operation 0010 of the production order has already been confirmed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). | The Enter Order and Operation screen displays. |  |
| 3 | Enter Order Number and Operation | On the Enter Order and Operation screen, make the following entries, and choose Go:Order: <Order ID> (from previous steps)Operation: 0020 | The Confirm Production Operation (F3069) screen displays. |  |
| 4 | Enter Fields in Quantities Section | In the Quantities section, check the following entries and make changes if required:Yield: <enter the amount you want to confirm>Scrap: <enter the amount you want to scrap> |  |  |
| 5 | Check Material Movements | In the Material Movements section, check the material list.Note For operation 0020 no components relevant to backflush are assigned. Hence the list is empty. | The system shows you an overview table of all materials for which the withdrawing is done automatically with the confirmation of the operation. |  |
| 6 | Enter Fields in Activities Section | In the Activities section, make the following entries:Machine: <enter the setup time you want to confirm for this operation> |  |  |
| 7 | Save your Entries | Choose Post and Complete to make final confirmation for this operation. | Confirmation has been created.Note For partial confirmation choose Post instead of Post and Complete. |  |

##### Monitor Order Progress (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the release or (partial) confirmation of finished goods orders is performed, the production supervisor could display and check the order using the app Manage Production Orders for the finished material FG0511.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). | The Manage Production Orders (F2336) screen displays. |  |
| 3 | Select Production Order | On the Manage Production Orders (F2336) screen, make the following entries:To check default Area of Responsibilities (supervisor), select the user (from the top left corner), App Settings > Area of Responsibility Production Supervisor. Check only this entry is displayed.Plant 1 AE (3310)MTS DI - Valuated (YB1)Click Adapt Filters to display more selection filter. Select the checkboxes for Material and Production Plant and click OK.Material: FG0511Production Plant: 3310Click Go to execute. | Selected order displays. |  |
| 4 | Check detailed operations status | Check detailed information for selected production operations.Issues:Empty, if there is no issue for production orderDelay or Missing Components / PRT issue or Quantity Deviation / Quality Issue information shows if relevant issue existsComponents:Material, total quantity and issued / open quantity information for order components is displayedOrder Schedule:Detailed operation information with relevant work center, confirmed quantity, start and end time is displayedWork Center Schedule:The relevant order covering the same work center capacity (operation is partially confirmed) is displayedOperations not Started:The relevant order that would cover the same work center capacity (operation is released) is displayedConfirmation:Detailed confirmation information with Yield, Scrap, Rework quantity displays if confirmation executedInspection:Detailed inspection lots information displays if existed | Detailed operations status displays. |  |

|  |
| --- |
| Note To display the inspection lots, you need further authorizations of SAP_BR_QUALITY_TECHNICIAN (transaction QA03). Ensure that your user has the appropriate authorizations if you want to review the inspection lots. Else this section is empty even though inspection lots are available. |

#### Quality Inspection – Early Goods Receipt Inspection/End-Product-Control (Before Goods Receipt)

##### Display Inspection Plan for Inspection Characteristics

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

By the release of the production order, the early goods receipt inspection is triggered as well. While inspection lot creation the relevant inspection plan is assigned to the inspection lot.

In this step, you display the inspection plan that is related to the finished good. The inspection plan defines all inspection characteristics used later in the quality inspection (End-Product Control).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Inspection Plan (QP03). | The Display Inspection Plan: Initial Screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Continue.Material: FG0511Plant: 3310 |  |  |
| 4 | Go to Inspection Characteristics Overview Screen | Select the entry for Operation 0010 and choose Inspection Characteristics.Note If you could not find Inspection Characteristics in your screen, choose Menu > Inspection Characteristics . | The Display Inspection Plan: Characteristic Overview screen displays. |  |
| 5 | Review the Inspection Characteristics | There are three Master Inspection Characteristics:One is Qualitative – Sensory Roasted Beans with inspection method Sensory of Roasted Coffee Beans.Two others are Quantitative – Relative Humidity and Rebrand.For all, sample size 1 is to be inspected.Auto-defect recording is defined if characteristics are rejected. | You have now reviewed the inspection characteristics for which data has to be maintained later. |  |

##### Display Quality Technician Overview (Optional)

Test Administration

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
| 2 | Access the App | Open Quality Technician Overview (F2361). | The Quality Technician Overview (F2361) screen displays.You can get an overview of the inspection lots with open results recording and the inspection lots without an inspection plan.Choose card Inspection Lots with Open Results Recording, No Inspection Points if you want to record results for the early goods receipt inspection lot. |  |

##### Display Open Inspection Lots (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The early goods receipt inspection lot is used to start the End-Process Control already before goods receipt. In this optional step, the operations and characteristics are reviewed as well as assigned inspection methods with attachments used for quality inspection.

Prerequisite

In this scope item, the inspection lot is created automatically upon release of production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Material: FG0511Inspection Lot Status: OutstandingInspection Lot Origin: Goods Receipt from Production | Alternatively, you can search for the batch <Batch ID> (from previous step). |  |
| 4 | Select the corresponding Inspection Lot | In the inspection lot list, select the inspection lot with column Production Order equals to the Production Order: <Order ID> (from previous step) | The Production Order number assigned to Inspection Lot is displayed.If the Production Order column does not appear, please choose the button Settings. In the View Settings dialog box, select Production Order and choose OK.If needed, press button Show Details to make the column visible. |  |
| 5 | Choose Operation (optional) | In Result, choose operation End-Product-Control. | Inspection Characteristics Sensory Roasted Beans, Relative Humidity and Rebrand can be reviewed with their specifications and calculated sample sizes. |  |
| 6 | Choose Characteristic (optional) | Click Sensory Roasted Beans in the characteristics column. | For checking the attachment in the inspection method:If you have attached a document in the inspection method as described in the Preliminary Steps, the Quality Technician can review the attachment referring to step 6 to 8.A dialog box appears with the Characteristics Details with the link to the Inspection Method. |  |
| 7 | Display the Attachment (optional) | Under Documents, the attachment for an illustration of the Roast Color of coffee beans is displayed. |  |  |
| 8 | Display Text | In General, Long Text is displayed. |  |  |

##### Record Inspection Results (Option 1: Before Goods Receipt)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the quality technician performs the quality inspection and records the inspection results for operation 0010 (End-Product Control).

After Cooling, the Quality Technician takes a sample of unpacked Roasted Beans and starts with quality inspection. This step can be performed alternatively before goods receipt (Option 1) or after goods receipt (Option 2).

It´s also possible to record results for some MICs earlier (e.g. rebrand and relative humidity), for others later (e.g. sensory), dependent from capacity in the laboratory.

Procedure

Record Inspection Results for one Inspection Lot

If inspection results shall be recorded for one or only a few inspection lots, execute the following steps:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log Onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A) | The Results Recording screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Material: FG0511Order: <Order ID> from previous step. | If Order is not displayed in the Filters, please choose Filters. On the popup screen Filters, select Order and choose OK. Choose Go. |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot.Choose Record Multiple Results. |  |  |
| 5 | Enter Inspection Result | Choose EditDepending on the inspection result, select one of the following two options:Positive ResultSensory: OKRelative Humidity: Mean Value (%): 4,0Rebrand: Mean Value (%): 14Negative ResultSensory: NOKRelative Humidity: Mean Value (%): 5,2Rebrand: Mean Value (%): 18 | For the qualitative characteristic (Sensory) the search help is needed to select a value. For the quantity characteristic (Relative Humidity and Rebrand) a number can be entered directly.The valuation and close are performed automatically, and the status is set to Valuated.The default number of inspected objects is calculated based on the sample size reviewed in an earlier step. The number of inspected objects can be manually changed. As well a number of nonconforming objects can be maintained directly in the respective fields for every inspection characteristic. |  |
| 6 | Save Inspection Lot | Choose Save. | The inspection lot is saved. QM Inspection for finished material has been performed and result recorded. |  |

Optional: Process-Optimized Results Recording for Multiple Inspection Lots

If inspection results shall be recorded for several inspection lots at the same time, execute the following steps.

|  |
| --- |
| Caution Note that this app can only be used for quality inspections with master inspection characteristics. It is not possible to capture inspection results for inspections with plan characteristics. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log Onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results in Table Form (F3365) | The Record Inspection Results in Table Form screen displays. |  |
| 3 | Enter Filter Fields | Maintain filter values and choose Go. | A list of inspection lots is displayed. |  |
| 4 | Select Inspection Lots and Inspection Characteristics | Select the inspection lots for which inspection results shall be recorded and choose Record Multiple Results.In the dialogue box Select Characteristics for Result Recording, select the master inspection characteristics for which inspection results shall be recorded and choose button OK. | The Record Inspection Results in Table Form screen displays.Note The system creates one table line item per inspection lot operation. Each master inspection characteristic is displayed in a separate column. The valuation of the inspection characteristic is displayed in a separate adjacent column. If a master inspection characteristic is assigned to another inspection operation, the respective table field is grayed out. |  |
| 5 | Show Inspection Details (Optional) | Click one inspection characteristic in the table and choose Show Details. | The side panel opens and detailed inspection data are displayed (e.g. inspection specifications, master inspection characteristic, inspection method, test equipment, and inspection remarks). |  |
| 6 | Show Work Center (Optional) | Choose Settings button in the upper right corner of the table. In the Define Colunm Properties dialogue box, select Work Center and choose OK. | An additional Work Center column is displayed. |  |
| 7 | Enter Inspection Results | Enter inspection results. See above for example data. | For qualitative results, a corresponding value help is provided. Quantitative inspection results can be entered directly.Depending on the defined valuation mode (check inspection details), the valuation is either done automatically by the system or must be done manually by the user.If a inspection result requires an inspection remark (check master inspection characteristic settings), it is not possible to navigate to the next inspection result. Open Details side panel and maintain the inspection remark in section Remarks. |  |
| 8 | Save Inspection Data | Choose Save. | Inspection results are saved and a success message is displayed. |  |

##### Display Inspection Results History (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, an overview about the history of inspection result is shown. For each quantitative Inspection Characteristic several statistical values and the development for recorded results are illustrated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Results History (F2428). | The Results History screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Aggregation Level: Master Inspection Characteristic |  |  |
| 4 | Select Inspection Characteristic | Select an Inspection Characteristic, for example, Relative Humidity and Rebrand. | Information is provided about the selected characteristics for process control, for example:A diagram displays the development of the recorded results for this characteristic with lower and upper limit.Statistical Values for Control Chart and Process Capability, for example Mean Value. |  |

#### Quality Inspection – In-Process Control (Operation Packaging) and Usage Decision for Packed Roasted Coffee Beans

##### Record Inspection Results (Hierarchical Worklist)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the quality technician performs the quality inspection and records the inspection result(s) for last operation 0030 (Packaging) within the production process.

The result is recorded in the inspection lot according to the defined inspection parameters in the routing. Here, free inspection points are used for result recording. Leveraging inspection points, you can have several inspections and can record multiple sets of characteristic results for a single operation. Each inspection point is valuated separately with a coded valuation.

Using Inspection point identifier Y01, only the last sample results are valid.

Prerequisite

The inspection is processed based on inspection lot. In this scope item, the inspection lot is automatically created upon release of the production order.

Production order operations 0010 (Roasting) and 0020 (Cooling) have already been confirmed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results - Hierarchical Worklist (QE51N). | The Results Recording Worklist screen displays.Note The app Record Results for Inspection Points (F2689) can be used as an alternative to capture inspection results for inspection points. However, recording of different single values currently causes an issue. Therefore, use app Record Inspection Results - Hierarchical Worklist (QE51N). |  |
| 3 | Enter Selection Fields | Make the following entries and choose Execute.Plant: 3310Insp. Lot Origin: 03 (Production)Material: FG0511Batch: <Batch ID> from previous stepLot Created: <choose one week ago until today>Work Center: PM050001 or PM050002 | The Results Recording Worklist screen displays.Caution In Cloud system, Dynamic Selection (e.g. for production order) is not offered.Alternatively you can search for the <Batch ID> or <Inspection Lot ID> from previous step.Selected work centers (Packaging Machine 1 or Packaging Machine 2) are displayed in the result list. |  |
| 4 | Select the Corresponding Inspection Lot | On the left pane, expand the corresponding inspection lot which you want to record a result. | If a dialogue appears asking to save, choose Cancel. |  |
| 5 | Choose the First Inspection Point | Choose the first inspection point Further Inspection which is under the activity 0030 Packaging 1 KG Work Center Packaging Machine with a click. | When the work center is selected, the cursor jumps automatically to the result. |  |
| 6 | Enter Inspection Result for the First Inspection Point | Depending on the inspection result, enter your values: e.g.Negative ResultWeight – Result: 1048, 1049, 1050 | For the quantitative characteristic Weight, three independent values need to be entered and the system will calculate the mean value. |  |
| 7 | Close and Save the First Inspection Point | Choose Enter.Choose Save. | Auto Valuation Rejected is done by the system.The status is set to 5 Processing is completed.Note If you want to run a rework process for material FG0511 due to failed quality inspection, you can follow the test script 6A9 (Rework with Quality Management – Consumer Products). You need to execute preliminary step “Assign Reference Operation Set and Order Type to Routing” of 6A9 test script and then follow the test steps “Execute Partial Production Order Confirmation for Operation Roasting” until “Analyze Event-based Order Costs“ within section “Rework Production Orders within Production Execution”. Afterwards you continue in this test script with chapter “Production Order Processing and Quality Inspection for Packed Roasted Coffee Beans (Dark)”. |  |
| 8 | Create the Next Inspection Point | Choose Further Inspection which is under the activity 0030 Packaging 1 KG Work Center Packaging Machine with a click. | The next inspection point is created with current Date/Time.A dialogue appears asking to save data for operation 0030, Choose Yes. |  |
| 9 | Enter Inspection Result for the Next Inspection Point | Depending on the inspection result, enter your values: e.g.Positive ResultWeight – Result: 1050, 1051, 1052 | For the quantitative characteristic Weight, three independent values need to be entered and the system will calculate the mean value. |  |
| 10 | Close and Save the Next Inspection Point | Choose Enter.Choose Save. | Auto Valuation Accepted is done by the system.The status is set to 5 Processing is completed. |  |

##### Display Inspection Results History (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, an overview about the history of inspection result is shown. For each quantitative Inspection Characteristic, several statistical values and the development for recorded results are illustrated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Results History (F2428). | The Results History screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Aggregation Level: Master Inspection Characteristic |  |  |
| 4 | Select Inspection Characteristic | Select an Inspection Characteristic, for example, Weight. | Information is provided about the selected characteristics for process control, for example:A diagram displays the development of the recorded results for this characteristic with lower and upper limit.Statistical Values for Control Chart and Process Capability, for example Mean Value and Variance. |  |

##### Display Quality Engineer Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the inspection lot depending on the inspection result. As an optional entry point for making this usage decision, you can use the app Quality Engineer Overview (F2360). Furthermore, the Quality Engineer Overview (F2360) app displays inspection lots without an inspection plan (e.g. if automatic assignment of an inspection plan is not set up in the material master or if automatic assignment failed), inspection lots without usage decision and inspection lots ready for usage decision.

|  |
| --- |
| Caution For this scope item example, auto-defect recording has not been performed in quality inspection within production (In-Process Control) because deviations are expected during the production process and shall not be tracked as defects later. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Engineer Overview (F2360). | The Quality Engineer Overview (F2360) screen displays. |  |
| 3 | In Card: Inspection Lots without Inspection Plan choose one entry (optional) |  | To assign missing data and ensure automatic inspection plan determination for further usage. |  |
| 4a | In Card: Select Inspection Lots Without Usage Decision (Optional) | Choose card Inspection Lots Without Usage Decision. | You can process further as described in Make Usage Decision Chapter. |  |
| 4b | Select the Corresponding Inspection Lot you have created before (optional) | In the inspection lot list, select the inspection lot. | The Manage Usage Decisions screen displays. Alternative entry to chapter Manage Usage Decision. |  |
| 4c | Select one of the Inspection Lot by Results Recording Status (Optional) | Select one of the Inspection Lot by Results Recording Status (Optional). | Alternative entry to chapter Manage Usage Decision. |  |
| 5 | Select Card Inspection Lots Ready for Usage Decision (optional) |  | All inspection lots with positive results get collectively an accepted usage decision (e.g. defaulted by A1) when pressing button Make Quick Usage Decision will be renamed soon. |  |
| 6 | In Card: Inspection Lots with Defects (optional) | (In case negative inspection results have been recorded and auto-defect recording has been defined) Select one of the inspection lot origins, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 7 | In Card: Top Defective Materials (optional) | (In case failed inspection results have been recorded and auto-defect recording has been defined) Select one of the materials inspected, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 8 | In Card: Top Defective Codes (optional) | (In case negative inspection results have been recorded and auto-defect recording has been defined) Select one of the defect codes recorded, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. |  |  |

##### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspections within production (operation Roasting and Packaging) are done and the inspection results are recorded. The Production Operator - Discrete Manufacturing was informed about the inspection results and can confirm last production order operation 0030 Packaging.

After recording of the inspection results by the quality technician, the quality engineer can now make a usage decision.

In order to close the inspection lot, the quality engineer makes a usage decision. As the inspection lot of origin 03 is not stock-relevant, there is no follow-up action assigned to the usage decision code that triggers a goods movement.

|  |
| --- |
| Caution In this example, the In-Process Control is performed as long as the relevant process parameters are reached. Thus, the last sample will always be accepted and because with inspection point Y01 only the last sample is valid, the UD can always be made with UD03 A (Accepted). For performing the UD you can either edit the inspection lot after checking the inspection data or you can perform the Quick Usage decision immediately after inspection lot selection. |

Procedure: Usage Decision after checking inspection data

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Usage Decisions (F2345). | The Manage Usage Decisions (F2345) screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Material: FG0511Inspection Lot Origin: ProductionUsage Decision Made: No | Alternatively you can search for the <Order ID> or <Batch ID> from previous steps.If Production Order is not displayed in the Filters, choose Adapt Filters. On the popup screen Adapt Filters, find Production and choose More Filters. Select Production Order and choose OK. Choose Go.If Batch is not displayed in the Filters, choose Adapt Filters. On the popup screen Adapt Filters, find Material and choose More Filters. Select Batch and choose OK. Choose Go. |  |
| 4 | Click the Corresponding Inspection Lots | In the inspection lot list, select the inspection lot with column Production Order equals to the Production Order: <Order ID> (from previous step). | The Production Order number is assigned to Inspection Lot.If the Production Order column does not appear, please choose the button Settings. In the View Settings dialog box, select Production Order and choose OK. |  |
| 5 | Review of Inspection Points | Select the tab Inspection Points, and review the detailed inspection results recorded previously. (From previous steps – Inspection Operations Roasting and Packaging) |  |  |
| 6 | Enter UD code | Choose Edit and select the tab Usage Decision. The UD code you select depends on the Inspection Result. Please select the following option,Positive ResultUD code: UD03 A (Accepted) |  |  |
| 7 | Save Usage Decision | Choose Save. | Usage decision has been made for In-process control inspection lot.Following a positive usage decision, you can now confirm the operation Packaging of the production order. |  |

Procedure: Quick Usage Decision

Alternatively, you can perform the Quick Usage decision immediately after inspection lot selection (without inspection data check).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Usage Decisions (F2345). | The Manage Usage Decisions (F2345) screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Material: FG0511Inspection Lot Origin: ProductionUsage Decision Made: No |  |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot with column Production Order equals to the Production Order: <Order ID> from previous step. | If the Production Order column does not appear, please choose the Settings button. In the View Settings dialog box, select Production Order and choose OK. |  |
| 5 | Make Quick Usage Decision | Press Button Make Quick Usage Decision | Usage decision with UD code: UD03 A (Accepted) has been made for In-process control inspection lot.Following a positive usage decision, you can now confirm the operation Packaging of the production order. |  |

#### Production Order Confirmation for Packaging Process of Packed Roasted Coffee Beans

##### Confirm Production incl. Component-Backflush for Operation Packaging

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the Consumer Products Industry, Goods receipt and Goods Issue postings are usually done immediately during the physical movements of the materials to ensure batch traceability and data consistency. Order confirmations with backflush are done at shift end or day end. The sum of the GI and GR quantity for the given order is then recorded within the confirmation and scrap quantities (optional). The time ticket confirmation allows recording either the default times for machine and labor usage, or record actual times for major deviations.

In this scope item the goods issue of packaging material is confirmed together with the operation confirmation even though the packaging materials are managed in batches due to machine design.

Prerequisite

The production order for the seminfinished material FG0511 has been released and Material Staging has been carried out. The operations 0010 and 0020 of the production order have already been confirmed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment. |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App. | Open Confirm Production Operation (F3069). | The Enter Order and Operation screen displays. |  |
| 3 | Enter Order Number and Operation. | On the Enter Order and Operation screen, make the following entries, and choose Go:Order: <Order ID> (from previous steps)Operation: 0030 | The Confirm Production Operation (F3069) screen displays. |  |
| 4 | Enter Fields in Quantities Section. | In the Quantities section, make the following entries:Yield: <enter the amount you want to Confirm>Scrap: <enter the amount you want to Scrap> |  |  |
| 5 | Check Material Movements. | In the Material Movements section, check the material list.Materials PK0501, PK0504 and PK0507 are subject to backflush and partly managed by batches (PK0501 and PK0504).Choose the Edit button on the right side of the material.Enter the relevant batch number and choose Save. | The system shows you an overview table of all materials for which the withdrawing is done automatically with the confirmation of the operation.The materials PK0501, PK0504 and PK0507 are set for backflush (in material master) and assigned to operation 0030 in the routing of FG0511 so that the withdrawing is done automatically after you confirm the operation. |  |
| 6 | Enter Fields in Activities Section. | In the Activities section, make the following entries:Machine: <enter the setup time you want to confirm for this operation>Labor: <enter the setup time you want to confirm for this operation> |  |  |
| 7 | Save your Entries. | Choose Post and Complete to make final confirmation for this operation. | Confirmation has been created.Note For partial confirmation, choose Post instead of Post and Complete. |  |

##### Post Goods Receipt for Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods receipt for the production order. You may post goods receipt for the total quantity, but if already partial quantities of the products are required for further processing, for example for further production or subsequent deliveries for sales orders, you can also execute partial confirmation during production process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Receipt for Production Order (F3110). | The Post Goods Receipt for Production Order (F3110) screen displays. |  |
| 3 | Enter Details | On the Post Goods Receipt for Production Order (F3110) screen, make the following entries and choose Enter:Order: <Order ID> (from previous steps) |  |  |
| 4 | Select the Item | In the Items section, select the item. | The Goods Receipt Item screen displays. |  |
| 5 | Input Production Date | In the Production and Shelf Life Expiration Date section, make the following entries and choose Apply:Production Date: <Current Date> | The Goods Receipt screen displays. |  |
| 6 | Post | Choose Post. | Goods receipt for production order has been done. |  |

##### Evaluate Stock/Requirements Situation after Goods Receipt for Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock/requirements situation for the finished good (FG0511) in the stock/requirements list after goods receipt for the production order is executed.

Prerequisite

Goods Receipt for the production order of the finished material is executed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments (F2101A) screen displays. |  |
| 3 | Check Default Setting | Choose the user icon and select App Settings.In the MRP Settings dialog box, check Manage Material Coverage - New Version (F0251A) that if toggle button is ON. | If the toggle button is ON, in following steps, it will be navigated to Manage Material Coverage - New Version (F0251A).If the toggle button is OFF, in following steps, it will be navigated to Manage Material Coverage - New Version (F0251A).In following steps, we describe the steps with the toggle button is ON. |  |
| 4 | Select Material | Search in the Material bar, select the following materials and then choose Manage Materials:Material: FG0511 | The Manage Material Coverage screen displays. |  |
| 5 | Review Stock / Requirements List | Select the corresponding material on the screen on the left side. | The detailed stock / requirements list for each material displays. |  |
| 6 | Check Inspection Lot | From the list on the screen, select the material for which you want to check for the inspection lot.Material: FG0511On the screen, you can review the Stock / Requirements Situation.Due to the final confirmation of the production order in previous step the production order isn't relevant for disposition anymore and hence removed from the list.However, due to the goods receipt from production, the early goods receipt inspection lot becomes disposition relevant and visible. You can check for the inspection lot number <Inspection Lot ID> noted down in previous steps. | If you want to display more detailed information of the disposition elements, choose Open > Stock/Requirements List and navigate to the corresponding disposition element. |  |

#### Quality Inspection – Early Goods Receipt Inspection/ End-Product-Control and Usage Decision (After Goods Receipt)

##### Display Material Stock Before Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, a review of finished material stock is done. Due to quality inspection, the material is not available for other processing.

Prerequisite

The goods receipt from production order was posted for the finished material directly to quality inspection stock. This is caused by material master settings for inspection type 04 Goods Receipt Inspection from production.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Inventory Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material (F1076) screen displays. |  |
| 3 | Enter Material | Make the following entries and choose Enter.FG0511 | Stock for the material is displayed. |  |
| 4 | Check Stock Quantity | Check the Quality Inspection Stock under the plant 3310 and for your batch <Batch ID>. | Stock for the material, batch and storage location is checked. |  |

##### Display Open Inspection Lots

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection lot is used to record the results of the End-Product Control. In this step, the references to the production order and material document (after goods receipt) are verified as well as the inspection lot quantities and postings can be reviewed.

Prerequisite

In this scope item, two inspection lots are created automatically upon goods receipt for the production order.

The In-Process Control (inspection within production) is completed. Production order confirmation is done. Goods receipt is posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots (F2343) screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Material: FG0511Inspection Lot Status: Outstanding | Alternatively, you can search for the batch <Batch ID> (from previous step) |  |
| 4 | Select the Corresponding Inspection Lots | In the inspection lot list, select the inspection lot with column Production Order equals to the Production Order: <Order ID> (from previous step). | The Production Order number assigned to Inspection Lot is displayed.If the Production Order column does not appear, please choose the button Settings. In the View Settings dialog box, select Production Order and choose OK. |  |
| 5 | Check Inspection Lot | Under Inspection Type, check the open inspection lot. Press button Show details in the top of the list to watch the progress of characteristics. | Inspection Lot (from previous step) with inspection type 04 is displayed. Progress is dependent from results recording performed in the previous step (Option 1: Before goods receipt) |  |
| 6 | Check progress of characteristics | In the Result tab, verify the already completed characteristics as well as the still open ones. |  |  |
| 7 | Check Inspection Lot by Selecting the Line | In the Origin tab, verify the referenced production order and Inspection Lot Origin.With goods receipt the material document is also assigned to the existing inspection lot. Verify the material document. | The production order from which the inspection lot originates is displayed.Origin: Goods Receipt from Production.Material Document (from previous step). |  |
| 8 | Check Inspection Lot Quantities | In the Origin tab, check the Lot Quantities, Sample Size and Postings. | The Lot Quantity and the calculated sample size are displayed as after release of production order.Actual Lot Quantity and Postings have changed according goods receipt quantity from previous step. |  |
| 9 | Check Material Document (Optional) | In the Stock Postings tab, check details of the assigned Material Document, which made the inspection lot disposition relevant. | Movement Type of this material document is 101 GR goods receipt.Quantity is as posted in the previous step. |  |

##### Record Inspection Results (Option 2: After Goods Receipt)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With early goods receipt inspection it´s possible to start the inspection in parallel to the running production process (Option 1), because the inspection lot is created already with release of the production order.

You can also start or complete the inspection after goods receipt (Option 2) in the existing inspection lot, dependent from capacity in the laboratory.

In this step, the quality technician performs the quality inspection and records the inspection result(s) for operation 0010 (End-Product Control).

Procedure

If there are open inspection characteristics, refer to:

Chapter “Quality Inspection – Early Goods Receipt Inspection (Before Goods Receipt)”

- [Record Inspection Results (Option 1: Before Goods Receipt)](#unique_118)

##### Display Quality Engineer Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the inspection lot depending on the inspection result. As an optional entry point for making this usage decision, you can use the app Quality Engineer Overview (F2360). Furthermore, the Quality Engineer Overview (F2360) app displays inspection lots without an inspection plan (e.g. if automatic assignment of an inspection plan is not set up in the material master or if automatic assignment failed), inspection lots without usage decision and inspection lots ready for usage decision. If negative inspection results are recorded, you can check the defect details in app Manage Defects (F2649) directed from the app Quality Engineer Overview (F2360) via the cards Inspection Lots with Defects, Top Defective Materials, or Top Defects.

|  |
| --- |
| Caution For this scope item example, auto-defect recording is performed in quality inspection for goods receipt (End-Product Control) because deviations shall be tracked as defects later. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Engineer Overview (F2360). | The Quality Engineer Overview (F2360) screen displays. |  |
| 3 | In Card: Inspection Lots without Inspection Plan choose one entry (optional) |  | Assign missing data and ensure automatic inspection plan determination for further usage. |  |
| 4a | In Card: Select Inspection Lots Without Usage Decision (Optional) | Choose card Inspection Lots Without Usage Decision. | You can process further as described in Make Usage Decision. |  |
| 4b | Select the Corresponding Inspection Lot you have created before (optional) | In the inspection lot list, select the inspection lot. | The Usage Decisions screen displays. Alternative entry to Make Usage Decision. |  |
| 4c | Select one of the Inspection Lot by Results Recording Status (Optional) | Select one of the Inspection Lot by Results Recording Status (Optional). | Alternative entry to Make Usage Decision. |  |
| 5 | Select Card Inspection Lots Ready for Usage Decision (optional) |  | All inspection lots with positive results get collectively an accepted usage decision (e.g. defaulted by A1) when pressing button Make Quick Usage Decision. |  |
| 6 | In Card: Inspection Lots with Defects (optional) | (In case negative inspection results have been recorded and auto-defect recording has been defined). Select one of the inspection lot origins, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 7 | In Card: Top Defective Materials (optional) | (In case negative inspection results have been recorded and auto-defect recording has been defined). Select one of the materials inspected, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 8 | In Card: Top Defects (optional) | (In case negative inspection results have been recorded and auto-defect recording has been defined). Select one of the defect codes recorded, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. |  |  |

##### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the finished material depending on the inspection result. If you do not want to use the Quality Engineer Overview(F2360), you can open the Manage Usage Decisions(F2345) app directly.

In order to close the inspection lot, the quality engineer makes a usage decision. As the inspection lot of origin 04 is stock-relevant, there is a follow-up action assigned to the usage decision code that triggers a goods movement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Usage Decisions (F2345). | The Manage Usage Decisions (F2345) screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go:Plant: 3310Material: FG0511Inspection Lot Origin: Goods Receipt From ProductionUsage Decision Made: No | Alternatively you can search for the <Order ID> or <Batch ID> from previous steps.If Production Order is not displayed in the Filters, choose Adapt Filters. On the popup screen Adapt Filters, find Production and choose More Filters. Select Production Order and choose OK. Choose Go.If Batch is not displayed in the Filters, choose Adapt Filters. On the popup screen Adapt Filters, find Material and choose More Filters. Select Batch and choose OK. Choose Go |  |
| 4 | Click the Corresponding Inspection Lots | In the inspection lot list, select the inspection lot with column Production Order equals to the Production Order: <Order ID> (from previous step). | The Production Order number assigned to Inspection lot is displayed.If the Production Order column does not appear, please choose the button Settings. In the View Settings dialog box, select Production Order and choose OK. |  |
| 5 | Display Defects | Scroll down to the Defects area. Check the details of defects. | Only available if you have recorded a Negative result. For a sensory rejection, there will be a sensory defect, for a relative humidity or rebrand rejection, there will be a tolerance defect displayed. |  |
| 6 | Enable Edit | Choose Edit. In the Document section choose Add, select the path and add the document. | For example, you can upload pictures to visualize the defect. |  |
| 7 | Enter UD code | Go to tab Usage Decision.Depending on the inspection result, select one of the following two options via search help and confirm with Choose.Positive ResultUD code: UD04 A1 (Accepted - unrestricted stock)Negative ResultUD code: UD04 R1 (Rejected-blocked Stock)UD code: UD04 R320 Rejected–scrap (complete quantity) | If the dialogue Some required characteristics are still open. Do you want to force inspection completion? appears, choose Yes.The corresponding stock posting is processed automatically in background for the complete quantity for Usage Decision codes A1, R1, and R320. |  |
| 8 | Modify Stock Posting (Optional) | In the Inspection Lot Stock section, enter the quantities to be posted to different stock types. | Note If you want to scrap a partial quant with UD code R310, you can split the quantity and post to To Unrestricted Use and To Scrap, respectively. It is also possible to transfer the (partial or full) quantity to a different material if, for example, inspection results show that the product is of higher/lower quality than initially planned in the production order and the higher/lower quality corresponds to different materials. |  |
| 9 | Save Usage Decision | Choose Save. | The usage decision is made with regard to the finished material.The system automatically triggers the material movements if associated with the usage decision code.Positive Result: The usage decision made for the inspection is Quality Inspection Passed. A goods movement is posted automatically from quality inspection stock to unrestricted use stock for the finished material FG0511.Negative Result: The usage decision made for the inspection is Quality Inspection Failed. A goods movement is posted automatically from quality inspection stock to blocked stock for the finished material FG0511. |  |

##### Display Material Stock after Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, we now verify the material movement done based on the usage decision codes by looking again at the material stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material (F1076) screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Enter.Material: FG0511 |  |  |
| 4 | Check Stock Quantity | Check the changed quantities of the Quality Inspection Stock, Unrestricted Use Stock (in case of positive usage decision) or Blocked Stock (in case of negative usage decision). | The stock quantities for finished material FG0511 and <Batch ID> are updated based on the quality inspection and respective usage decision of the previous steps. |  |

#### Production Order Processing and Quality Inspection for Packed Roasted Coffee Beans (Dark)

After production of the first component FG0511 (Carton 12 x 1kg Bags Medium Beans Arabica) for the display FG0502 (Display Med + Dark 48 x 1kg Arabica), the second component FG0512 (Carton 12 x 1kg Bags Dark Beans Arabica) needs to be produced as well. The production process for FG0512 (Carton 12 x 1kg Bags Dark Beans Arabica) also comes with full integration into Quality Management.

The production process for FG0512 is quite similar to the one already executed for FG0511. To shorten the process, you can execute [Option 1: Create Initial Material Stock for Finished Material FG0512](#unique_133). If you want to execute all production steps for FG0512 as well, use [Option 2: Execute Process Steps described for Finished Material FG0511](#unique_134) also for Finished Material FG0512.

##### Option 1: Create Initial Material Stock for Packed Roasted Coffee Beans (Dark)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To shorten the scenario, you can execute an initial stock posting for finished material FG0512.

|  |
| --- |
| Note We recommend that you check stock level for material FG0512 first. To do that, log onto the SAP Fiori launchpad as a Production Planner, and open Manage Material Coverage - New Version (F0251A) app. If the stock is sufficient, you can skip this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Post Goods Movement (MIGO) screen displays. |  |
| 3 | Choose Document Type | Choose Goods Receipt and Other. Select for Init.entry of stBal. 561 without any stock indicator and press Enter. |  |  |
| 4 | Enter Data | In the Detail Data section, make the following entries and press Enter:On the Where tab:Goods Movement Type: 561Plant: 3310Storage Location: 331AOn the Quantity tab:Quantity: <Quantity>, for example, <1000>On the Material tab:Material: FG0512On the Batch tab:Date of Manufacture: <today>Ensure that Item OK is selected. |  |  |
| 5 | Check | Choose Check. | The document is ready to be posted. |  |
| 6 | Post | Choose Post. | Material document XXX is posted and materials are available in stock. |  |

##### Option 2: Execute Process Steps described for Packed Roasted Coffee Beans (Medium) also for Packed Dark Roasted Coffee Beans (Dark)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step you execute the steps already processed for FG0511 for finished material FG0512.

Prerequisite

A planned order is available for material FG0512.

Procedure

Follow the steps described in the following sections and exchange material FG0511 by material FG0512.

Chapter “Production Order Conversion and Available-to-Promise Check for Packed Roasted Coffee Beans”

- Convert Planned Orders to Production Orders
- Review Material Availability Status for Production Orders

Chapter “Production Order Processing for Packed Roasted Coffee Beans”

- Execute Material Staging
- Release Production Order
- Goods Issue of Batch-Managed Raw Materials via Pick-List

Chapter “Quality Management – Overview Inspection Lots for Packed Roasted Coffee Beans”

- Display Open Inspection Lots

Chapter “Quality Inspection – Within Production (Roasting) for Packed Roasted Coffee Beans"

- Display Routing for Inspection Characteristics

|  |
| --- |
| Caution For material FG0512, routings contain material-specific catalogs and limits, which are different to material FG0511 |

- Display Quality Technician Overview (Optional)
- Display Open Inspection Lots (Optional)
- Execute Quality Inspection with Inspection Points for Operation Roasting

|  |
| --- |
| Caution Starting with inspection points with negative results, ending with positive results (only last sample is valid). |

- Display Inspection Results History (Optional)

Chapter “Production Order Confirmation of Roasting and Cooling Process for Packed Roasted Coffee Beans”

- Confirm Production for Operation Roasting
- Confirm Production for Operation Cooling
- Monitor Order Progress (Optional)

Chapter “Quality Inspection – Early Goods Receipt Inspection (Before Goods Receipt)”

- Display Inspection Plan for Inspection Characteristics

|  |
| --- |
| Caution For material FG0512, the inspection plan contains material-specific catalogs and limits (different to material FG0511) |

- Display Quality Technical Overview (Optional)
- Display Open Inspection Lots (Optional)
- Record Inspection Results (Option 1: Before Goods Receipt)

|  |
| --- |
| Caution For material FG0512 and for inspection characteristic Rebrand, positive result is 14-17%, negative result is, for example, 21%. |

- Display Inspection Results History (Optional)

Chapter “Quality Inspection and Usage Decision – Within Production (Packaging) for Packed Roasted Coffee Beans”

- Record Inspection Results for Operation Packaging

|  |
| --- |
| Caution Starting with inspection points with negative results, ending with positive results (only last sample is valid) |

- Display Inspection Results History (Optional)
- Display Quality Engineer Overview (Optional)
- Make Usage Decision

Chapter “Production Order Confirmation for Packaging Process of Packed Roasted Coffee Beans”

- Confirm Production of Operation Packaging
- Post Good Receipt for Production Order of Finished Material
- Evaluate Stock/Requirements Situation after Goods Receipt of Finished Material

Chapter”Quality Inspection and Usage Decision – Early Goods Receipt Inspection/ End-Product-Control and Usage Decision (After Goods Receipt)"

- Display Material Stock Before Usage Decision
- Display Open Inspection Lots
- Record Inspection Results (Option 2: After Goods Receipt)
- Display Quality Engineer Overview (Optional)
- Make Usage Decision
- Display Material Stock after Usage Decision

#### Production Order Conversion for Coffee Display

After finishing the production of the components FG0511 and FG0512, the production for the coffee display FG0502 can be executed. In addition to the two components produced, a packaging material (PK0508) and a label (PK0504) are needed which should be available in stock. While the two finished materials and the label are batch managed, the packaging material PK0508 (Display Carton Coffee Beans 48 x 1 kg) isn't in direct contact to the coffee, hence not managed in batches and subject to backflush during production process.

The Quality Inspection will be triggered by an inspection lot created during goods receipt of the production order (goods receipt inspection).

|  |
| --- |
| Note Even though the display packaging process is often executed in the storage location area, it nevertheless is handled as production step to be able to monitor the packaging times and costs. |

##### Create and Release Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create production orders. Because the order release is executed automatically, production can start immediately.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Convert Planned Orders - to Production Orders (CO41) | The Collective Conversion of Planned Orders: Initial screen displays. |  |
| 3 | Enter Restriction | Make the following entries and choose Run Selection:Planning Plant: 3310Production Plant: 3310Prodn. Supervisor: YB5Order Type: YBM5Material: FG0502 | The system displays a list of all planned orders, which match the restriction. |  |
| 4 | Convert Planned Order to Production Order | Select the planned order for conversion for following material, and then choose Convert.Material: FG0502Note It is possible to change order quantities (such as merging the quantities of 2 planned orders into one order or reducing the quantity of an order). For this scope item reduce the amount of one order to a maximum of 10 PC. | Planned orders are converted to production orders. Make a note of one production order number ____________________.You may then delete the obsolete planned orders from the selection list before executing order conversion. Run MRP to delete the obsolete planned orders from the database (the planned orders must not be firmed, otherwise MRP would leave them untouched). |  |

#### Production Order Processing for Coffee Displays

##### Goods Issue of Batch-Managed Components

###### Option 1: Goods Issue of Batch-Managed Components via Pick List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The withdrawal of the raw materials is used for the order. This withdrawal can be done by using the picking list (see production order process for finished materials) or doing a manual goods issue.

|  |
| --- |
| Note If the material is set for backflush (in material master or resource), the withdrawing is done automatically after you confirm the operation or the whole order. Backflushing should not be used for batch-managed components (to ensure that the physically picked and consumed batch is the same as the recorded batch). |

Prerequisites

Ensure that sufficient material is present on stock. If not enough stock is present, execute step Create Initial Material Stock in the preliminary steps of this scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Pick Components for Production Orders (CO27). | The Picking List: Initial Screen displays. |  |
| 3 | Enter Restriction and Execute | Make the following entries and choose Run:Profile: 000002Production Order: <Order ID> (from previous steps)Plant: 3310 | The Order Information System: Detail List of Components screen displays. |  |
| 4 | Picking Raw Materials | Select the relevant reservations and choose the upper left Picking. | The Picking list screen displays. On this screen, a list of all the selected reservations is displayed. |  |
| 5 | Batch Determination | Some materials are management by batch (for example FG0511 and FG0512). Select corresponding line item(s) and choose Batch Determination.Click on Copy. | The Batch Determination MM: Select Batches screen displays. |  |
| 6 | Split position into more batches (optional) | Mark one or more lines of the batch managed materials and Choose Split.Make the following entries and choose Copy:Split quantity: <add the split Quantity>.Back in the Picking list screen you can adopt the batch number in the newly created line. | Back to Picking list screen.If multiple line items were selected in step 5, the Picking list screen is displayed after completion of the last line item. |  |
| 7 | Post | Choose Post to post the goods movements. | The goods movements have been posted. |  |

###### Option 2: Manual Goods Issue (Instead of Picking List)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how the system performs a goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Initial screen displays. |  |
| 3 | Enter Production Order Number | Make the following entries and choose Enter:Trans./Event: Goods IssueReference Document: OrderOrder number: <Order ID> (from previous steps)Movement Type: 261 | The screen name adapts after entries are made. |  |
| 4 | Check Each Item | For each item shown, select Item OK. | Ensure that detail data is expanded. |  |
| 5 | Perform Batch Determination | Choose Stock Determ. for All. | The Batch Determination MM: Select Batches screen displays. |  |
| 6 | Copy Batch Determination Result | Check the required batch and choose Copy. Repeat this step for all the materials you selected. | The Goods Issue Order XXX screen displays. In addition, the batch numbers have been determined. |  |
| 7 | Post Goods Movements | Choose Post. | The goods movements have been posted. |  |

##### Review Production Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display and check the production order for finished goods after its release or confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Operations (F2335). | The Manage Production Operations screen displays. |  |
| 3 | Check Default Area of Responsibility (Supervisor) | Choose the user icon and select App Settings. In the Area of Responsibility dialog box, choose Production Supervisor.Check if only this entry displays, and choose OK:Plant 1 AE 3310MTS DI- Valuated -Process (YB5).Choose + to select this entry if not displayed; choose the Delete icon to remove any other plant entries and then choose OK. | The Manage Production Operations screen displays. |  |
| 4 | Select Production Order | On the Manage Production Operations screen, choose Adapt Filters to display more filter options.In the Adapt Filters dialog box, choose More Filters. Select Material and Plant and choose OK. Choose Go.Enter the following filters criteria and choose Go.Material: FG0502Plant: 3310Status: Released | The Material and Plant fields are then added to filter bar.Selected order displays. |  |
| 5 | Check Detailed Operations Status | Check detailed information for selected production operations.Operation Issue:Empty if there is no production order issue.Delay or Missing Components / PRT issue or Quantity Deviation / Quality Issue information shows if relevant issue exists.Components:Material, total quantity and issued / open quantity information for order components displays.Order Schedule:Detailed operation information with relevant work center, confirmed quantity, start and end time displays.Work Center Schedule:The relevant order covering the same work center capacity (operation is partially confirmed) displays.Operations not Started:The relevant order that would cover the same work center capacity (operation is released) displays.Confirmation:Detailed confirmation information with Yield, Scrap, Rework quantity displays if confirmation has been executed.Inspection:Detailed inspection lots information displays if existing.Note To display the inspection lots, you need further authorizations of SAP_BR_QUALITY_TECHNICIAN (transaction QA03). Ensure that your user has the appropriate authorizations if you want to review the inspection lots. Else this section is empty even though inspection lots are available. | Detailed operations status displays.Note The Quality Inspection Lot will be created during goods receipt of production order. Hence there is no QM inspection lot visible at that time. |  |

##### Confirm Production Order and Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to confirm the complete production order with all operations and post the Goods Receipt from Production in one step for the Finished Material FG0502.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Order (CO15). | The Enter Production Order Confirmation: Initial Screen displays. |  |
| 3 | Enter Production Order Number | Enter the Production Order <Order ID> noted down in previous step and choose Enter. | The Confirmation of Production Order Enter: Actual Data Screen is displayed. |  |
| 4 | Check Confirmation Type | Review the confirmation type. Per defauIt Final Confirmation and Clear Open Reservations is flagged.If you want to execute only partial confirmation change radio button and unflag Clear Open Reservations. |  |  |
| 5 | Enter Fields in Actual Data Section | In the Actual Data section, make the following entries:Yield Quantity : <enter the amount you want to Confirm>Scrap: <enter the amount you want to Scrap> |  |  |
| 6 | Enter Production Date | Choose Goods Movements Overview button. A pop up is displayed. Due to the fact that the finished product has an expiration date (which will be calculated according to the production date you enter) make the following entries and choose OK.Expiry date/Manu.date: <today´s date> | The finished product has an expiration date which will be calculated according to the production date you entered during goods receipt. |  |
| 7 | Enter Batch for Finished Material | On the Confirmation of Production Order Enter: Goods Movements screen make the following entries:Batch: <manually enter a new batch number> (for FG0502 manually enter a new batch number, for PK0504 select an appropriate one) | Note If you have already done a partial confirmation before, choose the batch number already created during first partial confirmation for FG0502 from the drop-down menu so that only one batch number is available per production order.Note down the batch number ___________________. |  |
| 8 | Save your Entries | Choose Post to execute the partial respective final confirmation for this order. | Confirmation has been created.Note If you have executed only a partial confirmation you can repeat steps 1 to 7 with the settings for partial or final confirmation. |  |

If customer complaints about product quality are raised, these complaints are normally either raised with respect to a batch number or the expiration date. To figure out the expiration date for the batch created during goods receipt, access the app Display Batch Changes, enter material FG0502, batch number created in this step and the plant 3310. Choose enter and press the button Display in the top section and afterwards the tab Basic Data 1. Note down the SLED/BBD for the corresponding batch _____________________. You will use the SLED/BBD date as an option to execute batch analysis later on in this test script.

Result

With goods receipt for production order, an inspection lot is created for material FG0502. With this inspection lot the End-Product Control is performed with 100 % visual check of each packed and labeled display.

#### Quality Inspection – Goods Receipt Inspection and Usage Decision for for Coffee Displays

##### Display Material Stock Before Quality Inspection (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, a review of the finished material stock is done. Due to quality inspection, the material is not available for other processing.

Prerequisite

The goods receipt from production order was posted for the finished material directly to quality inspection stock. This is caused by material master settings for inspection type 04 Goods Receipt Inspection from Production.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Inventory Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material (F1076) screen displays. |  |
| 3 | Enter Material | Make the following entries and press Enter.Material: FG0502 | Stock for the material is displayed. |  |
| 4 | Check Stock Quantity | Check the Quality Inspection Stock under the plant 3310 and batch <Batch ID> from previous step. | Stock for the material, batch and storage location is checked. |  |
| 5 | Check Inspection Lots | Choose Manage Stock on the bottom of the screen. Then choose Manage Inspection Lots on the bottom of the screen.Note Ensure your user has necessary authorization to view Manage Inspection Lots. | The Inspection Lots for the selected material are displayed. |  |

##### Display Inspection Plan for Inspection Characteristics

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you display the inspection plan that is related to the finished goods. The inspection plan defines all inspection characteristics used later in the quality inspection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Inspection Plan (QP03). | The Display Inspection Plan: Initial Screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Continue.Material: FG0502Plant: 3310 |  |  |
| 4 | Go to Inspection Characteristics Overview Screen | Choose Inspection Plan with Group Counter GrC 1 and choose Operations.Select the entry for Operation 0010 and choose Inspection Characteristics.Note If you could not find Inspection Characteristics in your screen, choose Menu > Goto > Inspection Characteristic Overview . | The Display Inspection Plan: Characteristic Overview screen displays. |  |
| 5 | Review the Inspection Characteristics | There is one Master Inspection Characteristics: it is Qualitative – Visual Pack Check.Sample size is 100% to be inspected.Auto-defect recording is defined if charac. is rejected. | You have now reviewed the inspection characteristics for which data has to be maintained later. |  |

##### Display Quality Technician Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, you can display an overview of open inspection lots via the overview page for quality technicians.

Prerequisite

The goods receipt from production order was posted for the finished material directly to quality inspection stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Technician Overview (F2361). | The Quality Technician Overview (F2361) screen displays.You can get an overview of the inspection lots with open results recording and the inspection lots without an inspection plan.Choose card Inspection Lots with Open Results Recording, No Inspection Points if you want to record results for the goods receipt inspection lot. |  |

##### Display Open Inspection Lots

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
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots (F2343) screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Material: FG0502Inspection Lot Status: Outstanding | Alternatively, you can search for the batch <Batch ID> (from previous step). |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot with column Production Order equals to the Production Order : <Order ID> (from previous step). | The Production Order number assigned with Inspection lot is displayed.If the Production Order column does not appear, please choose the button Settings. In the View Settings dialog box, select Production Order and choose OK. |  |
| 5 | Check Inspection Lot | In the inspection lot list you can watch the progress of characteristics. | Make a note of the inspection lot:Inspection Lot ______________ with inspection type 04 (Goods Receipt from Production). Progress is 0%. |  |
| 6 | Check Inspection Lot | In the Origin tab, verify the referenced production order and material document. | The production order and material document from which the inspection lot originates are displayed. |  |
| 7 | Check Inspection Lot Quantities | In the Origin tab, check the Lot Quantities, Sample Size and Postings. | The size of the sample for quality inspection is displayed (100% of inspection lot quantity).Actual Lot Quantity and Postings are according to goods receipt quantity from previous step. |  |
| 8 | Check Material Document | In the Stock Postings tab, check details of the assigned material document, which has created the inspection lot. | Movement Type of this material document is 101 GR goods receipt.Quantity is as posted in the previous step. |  |

##### Record Inspection Results (Hierarchical Worklist)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the quality technician performs the quality inspection and records the inspection result(s) for operation 0010 (Display Packaging Check). The result is recorded in the inspection lot according to the defined inspection parameters in the inspection plan.

Prerequisite

The inspection is processed based on inspection lot. In this scope item, the inspection lot is automatically created upon goods receipt for production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results - Hierarchical Worklist (QE51N). | The Results Recording Worklist screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Execute.Plant： 3310Insp. Lot Origin： 04 (Goods Receipt from Production)Material: FG0502Batch: <Batch ID> from previous stepLot Created: <choose one week ago until today>> | The Results Recording Worklist Screen displays.Caution In Cloud system, Dynamic Selection (e.g. for production order) is not offered.Alternatively you can search for the <Batch ID> or <Inspection Lot ID> from previous step. |  |
| 4 | Select the Corresponding Inspection Lot | On the left pane, expand the corresponding inspection lot which you want to record a result. | If a dialogue appears asking to save, choose Cancel. |  |
| 5 | Choose the Characteristic | Select the characteristic which is under the activity 0010 Display Pack-Control Work Center Quality Check Point with a click (or use icon Select a Characteristic). | When the characteristic is selected, Record Results for XXXX: Characteristic Single Screen, opens where the class size can be recorded. |  |
| 6 | Enter Inspection Result for Characteristic | Depending on the inspection result, classify the no. of inspected displays and then confirm with Save.Positive ResultVisual Pack Check: <enter no. of displays in class size> of class OKNegative ResultVisual Pack Check: <enter no. of displays in class size> of class NOK | For the qualitative characteristic Visual Check a 100% check is performed, assigning the no. of displays to the corresponding class OK or NOK.Auto Valuation is done by the system.The status is set to 5 Processing is completed. |  |

##### Display Quality Engineer Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the inspection lot depending on the inspection result. As an optional entry point for making this usage decision, you can use the app Quality Engineer Overview (F2360). Furthermore, the Quality Engineer Overview (F2360) app displays inspection lots without an inspection plan (e.g. if automatic assignment of an inspection plan is not set up in the material master or if automatic assignment failed), inspection lots without usage decision and inspection lots ready for usage decision. If negative inspection results are recorded, you can check the defect details in app Manage Defects (F2649) directed from the app Quality Engineer Overview (F2360) via the cards Inspection Lots with Defects, Top Defective Materials, or Top Defects.

|  |
| --- |
| Caution For this scope item example, auto-defect recording is performed in quality inspection for goods receipt (End-Product Control) because deviations shall be tracked as defects later. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Engineer Overview (F2360). | The Quality Engineer Overview (F2360) screen displays. |  |
| 3 | In Card: Inspection Lots without Inspection Plan choose one entry (optional) |  | Assign missing data and ensure automatic inspection plan determination for further usage. |  |
| 4a | In Card: Select Inspection Lots Without Usage Decision (Optional) | Choose card Inspection Lots Without Usage Decision. | You can process further as described in Make Usage Decision. |  |
| 4b | Select the Corresponding Inspection Lot you have created before (optional) | In the inspection lot list, select the inspection lot. | The Usage Decisions screen displays. Alternative entry to Make Usage Decision. |  |
| 4c | Select one of the Inspection Lot by Results Recording Status (Optional) | Select one of the Inspection Lot by Results Recording Status (Optional). | Alternative entry to Make Usage Decision. |  |
| 5 | Select Card Inspection Lots Ready for Usage Decision (optional) |  | All inspection lots with positive results get collectively an accepted usage decision (e.g. defaulted by A1) when pressing button Make Quick Usage Decision. |  |
| 6 | In Card: Inspection Lots with Defects (optional) | (In case negative inspection results have been recorded and auto-defect recording has been defined). Select one of the inspection lot origins, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 7 | In Card: Top Defective Materials (optional) | (In case negative inspection results have been recorded and auto-defect recording has been defined). Select one of the materials inspected, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 8 | In Card: Top Defects (optional) | (In case negative inspection results have been recorded and auto-defect recording has been defined). Select one of the defect codes recorded, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. |  |  |

##### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the finished material depending on the inspection result. If you do not want to use the Quality Engineer Overview (F2360), you can open the Manage Usage Decisions (F2345) app directly.

In order to close the inspection lot, the quality engineer makes a usage decision. As the inspection lot of origin 04 is stock-relevant, there is a follow-up action assigned to the usage decision code that triggers a goods movement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Usage Decisions (F2345). | The Manage Usage Decisions (F2345) screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go:Plant: 3310Material: FG0502Usage Decision Made: No | Alternatively you can search for the <Order ID> or <Batch ID> from previous steps.If Production Order is not displayed in the Filters, choose Adapt Filters. On the popup screen Adapt Filters, find Production and choose More Filters. Select Production Order and choose OK. Choose Go.If Batch is not displayed in the Filters, choose Adapt Filters. On the popup screen Adapt Filters, find Material and choose More Filters. Select Batch and choose OK. Choose Go. |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot. |  |  |
| 5 | Display Defects | Scroll down to the Defects area. Check the details of Defects. | Only available if you have recorded a Negative result. For a visual check rejection, there will be a packaging defect. |  |
| 6 | Enable Edit | Choose Edit. In the Document section choose Upload, select the path and add the document. | For example, you can upload pictures to visualize the defect. |  |
| 7 | Enter UD code | Depending on the inspection result, select one of the following two options via search help and confirm with Choose.Positive ResultUD code: UD04 A1 (Accepted - unrestricted stock)Negative ResultUD code: UD04 R1 (Rejected-blocked Stock)UD code: UD04 R320 Rejected–scrap (complete quantity) | If the dialogue 'Some required characteristics are still open. Do you want to force inspection completion?' appears, choose Yes.The corresponding stock posting is processed automatically in background for the complete quantity for Usage Decision codes A1, R1, and R320.Note If you want to run a rework process for material FG0502 due to failed quality inspection, you can follow the test script 6A9 (Rework with Quality Management – Consumer Products). You need to follow all test steps described in the section “Rework Production Order of Stock Manufactured Material with Quality Management”. |  |
| 8 | Modify Stock Posting (Optional) | In the Inspection Lot Stock section, enter the quantities to be posted to different stock types. | Note If you want to scrap a partial quantity with UD code R310, you can split the quantity and post to To Unrestricted Use and To Scrap, respectively. It is also possible to transfer the (partial or full) quantity to a different material if, for example, inspection results show that the product is of higher/lower quality than initially planned in the production order and the higher/lower quality corresponds to different materials. |  |
| 9 | Save Usage Decision | Choose Save. | The usage decision is made with regard to the manufactured goods. The system automatically triggers the material movements if associated with the usage decision code.Positive Result: The usage decision made for the inspection is Quality Inspection Passed. A goods movement is posted automatically from quality inspection stock to unrestricted use stock for the finished material FG0502.Negative Result: The usage decision made for the inspection is Quality Inspection Failed. A goods movement is posted automatically from quality inspection stock to blocked stock for the finished material FG0502. |  |

##### Display Material Stock After Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, we now verify the material movement done based on the usage decision codes by looking again at the material stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material (F1076) screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Enter.Material: FG0502 |  |  |
| 4 | Check Stock Quantity | Check the changed quantities of the Quality Inspection Stock, Unrestricted Use Stock (in case of positive usage decision) or Blocked Stock (in case of negative usage decision). | The stock quantities for finished material FG0502 and <Batch ID> are updated based on the quality inspection and respective usage decision of the previous steps. |  |

#### Evaluations

##### Review Scrap Report (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review the scrap report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Material Scrap - Maximum Deviation (F2035). | The Material Scrap screen displays. |  |
| 3 | Investigate Scrap | Materials Scrap can be displayed by various filters.You could choose the corresponding material in Chart to display the details. |  |  |

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
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Batch Information Cockpit (BMBC). | The Batch Information Cockpit screen displays. |  |
| 3 | Select Batches | On the Batch Information Cockpit screen, make the following entries.Go to the Material tab.Material : FG0502Plant: 3310Go to the Classification tab.Batch Class: YB_EXP_DATE_001OrGo to Search with Characteristics area.Selection Class: YB_EXP_DATE_001Choose Create values.Enter Characteristics value. e.g. <SLED/BBD from previous step>Note For batch class and characteristics relevant materials, refer to Master Data, Organizational Data, and Other Data.Choose Execute Selection. | One or multiple batches are displayed in the left screen area Selection Result for Batches. The standard sorting is done per material number. |  |
| 4 | Expand Selection | In the section Selection Result for Batches. Select the checkbox for FG0502 and then choose Expand subtree or Expand node. | The selection result is analyzed and a batch for further investigation is identified. |  |
| 5 | Start Analysis | Right-click on one selected batch and choose either Usage(Top-Down) or Usage(Bottom-up). | The batch where-used list displays. |  |
| 6 | Analyze the Batch Where Used List | The usage of the batch can be analyzed and the specific documents (such as batch master record, production orders and sales order) can be accessed via double click. |  |  |
| 7 | Analyze Assigned Inspection Lots | Mark one line in the Details (Usage) table and choose button Inspection Lots to review inspection lots assigned to the selected element. |  |  |
| 8 | Analyze Material Document | Choose Details again and select Usage.Select one document and choose Documents. | The usage displays again and after selecting documents the respective material document display. |  |
| 9 | Go to the Material Document | Choose the material document in the pop up dialog and choose Choose (F2).To display the material document, you need further authorizations that are granted by your company, for example, SAP_BR_INVENTORY_MANAGER. | The material document displays.Note that your user has to have the appropriate authorizations. |  |

### Subcontracting - Consumer Products (5W4)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The display packaging can either be done in-house (see previous scope item 5HK) or by a subcontractor, e.g. because of machine break down or limited capacity. A typical display packaging process executed by a subcontractor with the provision of components is realized including the usage of subcontracting MRP areas for disposition.

The MRP run has created planned orders that can either be converted to a production order (see previous scope item 5HK) or to a purchase requisition. The purchase requisition is converted into a subcontract purchase order. As an alternative the purchase order can be created manually by a requestor. The purchase order is subject to approval based on predefined parameters before being issued to the subcontractor.

The outbound delivery is created and the materials are picked and shipped to the subcontractor. The picking process results in a transfer of the components to the Subcontracting MRP Area indicating that the components are still owned by the company but currently located at the subcontractor site.

The consumption of the sent components from the subcontracting MRP Area is recorded upon the receipt of the value-added finished material. Moreover, with the supply of the finished material the goods receipt is created. Subsequently, the invoicing process is triggered.

As a process variant, inbould deliveries can be created to be able to monitor the delivery date. In that case, the goods receipt will be executed with relation to the inbound delivery and not to the purchase order.

The components send to the subcontractor and the subcontracted material are batch-managed, which might cause difficulties with the batch confirmation of the installed components, especially when several components are consumed by producing the subcontracted material. The subcontractor to whom several component batches have been send to, cannot always guarantee that they can record which component batch was consumed in which subcontracted material batch. This can be for organizational, personnel, or cost reasons.

To ensure traceability nonetheless, the component batches are partially anonymized before they are sent to the subcontractor. This means that several component batches of a product are combined into one anonynmous delivery batch by transferring the batch to batch of the component. It is easier for the subcontractor to report back the delivery batch of the components that hase been included in a subcontracted material batch.

With, the goods-receipt posting of the subcontracted finished good the components are automatically posted and the component stock at the subcontractor is decreased. The finished material itself is posted to quality inspection stock and an inspection lot is created based on an inspection plan. The quality technician records the inspection results. Based on the results, the quality engineer makes a usage decision, such as accepting or rejecting the material, posting the material to unrestricted or blocked stock. For the rejected results, a defect is automatically recorded.

#### Anonymous Forecast and MRP

##### Option 1: Create Planned Independent Requirements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create Planned Independent Requirements (PIRs). PIRs are used to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split according to dates. In Option 1 these PIRs will be loaded by manually.

|  |
| --- |
| Note Instead of creating a single requirement, sometimes one or more planned independent requirements can be maintained and included in a requirement plan for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries and choose Go:Plant: 3310Period Indicator: Weekly(W)Version Active: Select all optionsMaterial: FG0502 | The searched material item displays. If the material filter is not directly available choose Adapt Filters, select the Material Filter, enter the desired material and choose OK.Note If no PIRs for FG0502 have been maintained in the system before, the selection is empty in the app. In that case please leave this app and access the app Create PIRs (MD61), make the following entries on the Create Planned Independent Requirements: Initial Screen and choose Continue:Plant: 3310Period Indicator: Weekly (W)Version: 00Material: FG0502Choose Save and restart with step 1. |  |
| 5 | Edit PIRs. | Select the material item and choose Edit in the upper right corner of the screen.On the Edit PIRs screen, enter quantities per week, for example:Week 1 (current week + 1 week): 40 PCWeek 2 (current week + 2 weeks): 80 PCWeek 3 (current week + 3 weeks): 80 PCWeek 4 (current week + 4 weeks): 100 PCWeek 5 (current week + 5 weeks): 80 PCWeek 6 (current week + 6 weeks): 80 PCVersion is Active: YES | Note If already stock for FG0502 is available, increase the quantity for PIR of current week + 1 for the stock already available. As an alternative, remove the stock to get planned orders in next step. |  |
| 6 | Save PIR's Draft | Choose Save in the bottom right corner of the screen. | The PIRs draft is saved. |  |

##### Option 2: Create Planned Independent Requirements by Upload File

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use planned independent requirements to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split over time according to dates. In Option 2, these PIRs will be loaded by Upload File.

|  |
| --- |
| Note Instead of creating a single requirement, sometimes a requirements plan that includes one or more planned independent requirements can be maintained for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Weekly(W)Version Active: Select all optionsMaterial: FG0502 | Note If no PIRs for FG0502 have been maintained in the system before, the selection is empty in the app. In that case please leave this app and access the app Create PIRs (MD61), make the following entries on the Create Planned Independent Requirements: Initial screen and choose Continue:Plant: 3310Period Indicator: Weekly (W)Version Active: 00Search: FG0502Choose Save and restart with step 4. |  |
| 5 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 6 | Download Template | Select the material item and choose Edit in the upper right.Choose button Download to Spreadsheet to download the template to your local work space.Then choose Back without saving. |  |  |
| 7 | Edit PIRs. | Open the Spreadsheet in an adequate program and enter quantities per period, for example:In the upcoming several weeks, enter following values for PIR:Week 1 (current week + 2 weeks): 40 PCWeek 2 (current week + 3 weeks): 80 PCWeek 3 (current week + 4 weeks): 80 PCWeek 4 (current week + 5 weeks): 100 PCWeek 5 (current week + 6 weeks): 80 PCWeek 6 (current week + 7 weeks): 80 PCVersion is Active: YESSave your PIRs in the spreadsheet. | Note We recommend to check the stock for finished material before entering the PIRs (see prerequisites). If there is still stock available for FG0502, enhance the first PIR for the stock already available to generate a reproducable capacity situation (e.g. actual stock plus 250 PC). To check the stock, you can Log on to the SAP Fiori Launchpad as a Production Planner and Open the app Manage Material Coverage - New Version (F0251A). |  |
| 8 | Upload PIRs. | On the Maintain PIRs screen, choose button Upload and Edit. On the Pop Up select the file you adjusted in previous step and choose Continue. Review the uploaded data. |  |  |
| 9 | Save PIRs Draft | Choose Save at bottom right. | The PIRs are saved |  |

##### Material Requirements Planning at Plant Level

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use Material Requirement Planning (MRP) to tailor available capacities and receipts on time to suit requirement quantities. As a result, single-item multi-level requirement planning is performed for plant 3310.

Prerequisite

The Make-to-Stock finished goods are planned at plant level. There is now a requirement for FG0502 in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirements Planning (MRP)Job Name: MRP for FG0502Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: <select>Recurrence Pattern: Single RunChoose OK.Choose Step 3.For 3. Parameters section:Plant: 3310Material: FG0502Changed BOM Components: <select>Stock Transfer Materials: <select>Scheduling: 2Planning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG0502 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

##### Evaluate Stock/Requirements Situation and Prepare Planned Order for Subcontracting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock/requirements situation for Make-to-Stock finished goods (FG0502). The material FG0502 is mainly used for inhouse production but subcontracting is also possible, for example due to machine breakdown. Therefore you prepare a planned order for subcontracting.

Prerequisite

Requirement planning is carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Monitor Stock / Requirements List - Old Version (MD04). | The Monitor Stock / Requirements List screen displays. |  |
| 3 | Maintain Data | On the Stock/Requirements List: Initial Screen make the following entries and choose Continue :Material: FG0502Plant: 3310 | The Stock/Requirements List as of xxx hrs is displayed. |  |
| 4 | Review Stock / Requirements Situation | On the Stock/Requirements List as of xxx hrs check the planned orders created by the MRP run for material FG0502. | The planned orders created by MRP run are displayed. |  |
| 5 | Prepare Planned Order | Double Click on one of the planned orders you want to use for Subcontracting.On the Additional Data for MRP Element Screen Choose Change Element.Change the Production Version to 0003 and choose Save.Afterwards choose Refresh to update the Stock-/Requirements List.Make a note of the Planned Order Number ______. | The Production version is changed to 0003. |  |

##### Convert Planned Order to Purchase Requisiton

Purpose

This process step shows you how to convert the planned order relevant to subcontracting into a purchase requisition.

Prerequisite

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Convert Planned Orders - to Purchase Requisitions (MD15). | The Monitor Stock / Requirements List: Initial Screen is displayed. |  |
| 3 | Maintain Data | On the Collective Conversion of PlndOrd. To Pur.Req.: Initial Screen Screen make the following entries and choose Continue.Select radio button for MaterialMaterial: FG0502Plant: 3310Procurement Type: X | The planned orders created by MRP run are displayed. |  |
| 4 | Select Planned Order | Select the Planned Order noted in previous step and choose Convert Online. |  |  |
| 5 | Adopt Purchase Requisiton | On the Convert Planned Order into Purchase Req Details Screen make the following Entry:Item Category: LChoose button Assign Source of Supply.Choose button Process Components. The list of components which will be delivered to the subcontractor is shown.Choose Menu – Component List – Component Availability to check if all components are available.Choose Back twice. |  |  |
| 6 | Save your Entries | Choose Save. |  |  |

#### Subcontracting

##### Create Purchase Order

###### Option 1: Convert Purchase Requisition to Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, a purchase requisition for planned subcontracting is assigned and a corresponding purchase order is created. In the purchase order the batch number which was created in the preliminary steps is maintained.

|  |
| --- |
| Note If you want to use the Save Draft feature in this app, you have to use a personalized user. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the Purchaser role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Create Purchase Order via Purchase Requisition Assignment List (ME58). | A selection screen is displayed. |  |
| 3 | Select Purchase Requisition | Search for all Purchase Requisition for material which are assigned to the subcontractingSupplier: 33305001Click on Execute. | The Assign and Process Purchase Requisitions screen is displayed. |  |
| 4 | Transfer Purchase Requisitions with assignment | Mark the Supplier in the Assignments register tab and click on Create Purchase Order. | The Purchase Requisitions list is displayed in screen Create Purchase Order. |  |
| 5 | Prepare the Purchase Order | Select the purchase requisition which was converted from Planned Order to Purchase Requisition.Click on Adopt to move the selected Purchase requisition to the shopping cart.A pop up might come up. In that case click on Re-Explode in the pop-up to reexplode the Bill Of Material. | The Purchase Order screen is prepared and maintained with the data from the Purchase Requisition. |  |
| 6 | Enter Batch | Under Item Detail Select the Material Data and make the following entry:Batch Number: <Batch number from preliminary steps> |  |  |
| 7 | Check the component list | Check the exploded component list in the detail data in register tab Select Material Data.Click on Components top-right corner in Material Data to display the list of components for the main line item FG0502.Note In case no batch number is automatically assigned to the PO, the batch number should be maintained manually in the PO. | Components are maintained from the Bill Of Material. |  |
| 8 | Maintain Tax Code | Click on register tab Invoice and enter the Tax Code for the line item.Tax Code: <Input Tax Code> |  |  |
| 9 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A Purchase Order is created. |  |

###### Option 2: Create Purchase Order manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity creates a purchase order for subcontract material. This activity is only required if you do not convert an existing purchase requisition as described in the section ”Convert Purchase Requisition to Purchase Order”.

|  |
| --- |
| Note You can store purchase order data as template for frequently used data. To save the data to a template, choose Save as Template. To load data from a template, choose Load from Template. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad Purchaser . | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order screen is displayed with a list of existing Purchasing Document Items. |  |
| 3 | Create Purchase Order data | Enter the following data :Enter Supplier : 33305001 and choose EnterPurchasing Org: 3310Purchasing Group: 001Company Code: 3310Currency: AEDEnter the below Items sectionItem Category: Subcontracting (L)Material (Original): FG0502Quantity: x PCDelivery Date: <enter Date>Plant: 3310Storage Location: 331ABatch: <batch number> and choose EnterIn the Item Details section open the tab InvoiceTax Code: <Input Tax Code> |  |  |
| 5 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A Purchase Order is created. Make a note of the purchase order number ________. |  |

###### Option 3 : Create Purchase Order manually with Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity creates a purchase order for subcontracting material. This activity is only required if you do not convert an existing purchase requisition as described in the section ”Convert Purchase Requisition to Purchase Order”. In addition to option 2, this purchasing order requires the creation of an inbound delivery afterward. The goods receipt will not be posted with respect to the purchase order but the inbound delivery.

|  |
| --- |
| Note You can store purchase order data as a template for frequently used data. To save the data to a template, choose Save as Template. To load data from a template, choose Load from Template |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad Purchaser . | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order screen is displayed with a list of existing Purchasing Document Items. |  |
| 3 | Create Purchase Order data | Enter the following data :Enter Supplier : 33305001choose Enter and make the following entries:Purchasing Org: 3310Purchasing Group: 001Company Code: 3310Currency: AEDEnter the below Items sectionItem Category: Subcontracting (L)Material : FG0502Quantity: x PCDelivery Date: <enter Date>Plant: 3310Storage Location: 331AIn the Item Details section, open the tab Material Data.Press Create Batch and confirm the popup with Enter. A batch number is populated in the Batch Number text box.In the Item Details section, open the tab Invoice and enter the following values.Tax Code: <Input Tax Code>In the Item Details section, open the tab Confirmations and enter the following values.Conf. control: 0004 Inbound Delivery |  |  |
| 5 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A Purchase Order is created. Make a note of the purchase order number ________. |  |

##### Approve Purchase Orders (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

All the purchase orders that require release by an authorized person are listed and must be approved. About the PO approve user setting, please refer to the step Configure Your Release Conditions for PO Approval (Only for SAP S/4HANA Enterprise Management Cloud) in J45.

|  |
| --- |
| Note Only POs with a value higher than 500.00 AED and Purchasing Group 001 have to be released in this transaction. POs with a value under this amount do not need to be released. For POs under this amount, this step can be skipped. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on the SAP Fiori Launchpad with the Purchasing Manager role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Approve Purchase Order | Open My Inbox - All Items (F0862). | A list of already created Purchase Orders is displayed. |  |
| 3 | Check Purchase Order Status | Click on Filter. In the pop-up, filter by Status, select statuses Ready and In Progress. Click on OK. | The Purchase Orders without follow-on documents (w/o status Follow-On Documents) and a net value of 500 AED or more have the status In Approval. |  |
| 4 | Release Purchase Order | Select the Purchase order in left of the screen and click Approve in bottom right. | The Submit Decision dialog box is displayed. |  |
| 5 | Enter Release Reason | Enter the approval reason if needed, then choose Submit. | The Purchase Order is approved. |  |
| 6 | Back to Fiori Launchpad | Choose the Home button to go back to the Fiori Launchpad. | The Fiori Launchpad is displayed. |  |

##### Monitor Subcontracting Documents (Optional)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the Fiori App | Open Monitor Subcontracting Documents (F3095). | The Monitor Subcontracting Documents screen displays. |  |
| 3 | Monitor Subcontracting Document | Enter the following data:Subcontractor: 33305001Choose Go.Note If the subcontractor field does not appear on the screen, select the field on Adapt Filter. |  |  |
| 5 | Manage Purchase Order | Check the details of your subcontracting document by clicking the item. |  |  |

##### Material Requirements Planning at Plant Level

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use Material Requirement Planning (MRP) to tailor available capacities and receipts on time to suit requirement quantities. As a result, single-item multi-level requirement planning is performed for plant 3310.

Prerequisite

The Make-to-Stock finished goods are planned at plant level. There is now a requirement for FG0502 in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirements Planning (MRP)Job Name: MRP for FG0502Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: <select>Recurrence Pattern: Single RunChoose OK.Choose Step 3.For 3. Parameters section:Plant: 3310Material: FG0502Changed BOM Components: <select>Stock Transfer Materials: <select>Scheduling: 2Planning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG0502 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

##### Evaluate Stock/Requirements Situation (Optional)

Purpose

This process step shows you how to display the stock/requirements situation for the Finished and packaging materials which will be provided to the subcontractor during subcontracting process.

In this step, you can check the stock transfer elements created during MRP run for components provided to the subcontractor.

Prerequisite

Requirement planning is carried out after subcontracting purchase order creation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Monitor Stock / Requirements List - Old Version (MD04). | The Stock / Requirements List: Initial Screen is displayed. |  |
| 3 | Select Material | On the Stock / Requirements List: Initial Screen make the following entries and choose Continue.Material: FG0511Plant: 3310 | The Stock/Requirements List as of xxx hrs is displayed. |  |
| 4 | Review Stock / Requirements Situation for Components to be provided to the MRP area of the subcontractor | On the Stock/Requirements List as of xxx hrs check the stock transfer elements created during MRP run.For the plant MRP Area 3310 a material reservation has been created for material FG0511. Double click on the reservation for more details.In the Stock/Requirements List, change from the plant MRP area to the subcontractor MRP area, make the following entries and choose the button Refresh.MRP Area: 3310SUB051The MRP Run in previous step has now created Transport Reservations to the Subcontracting MRP Area 3310SUB051. |  |  |
| 5 | Review Intra-Plant View | To be able to better monitor planning situations where more than one MRP Area is involved, two additional tabs are provided for the Stock/Requirements List.To see the planning situation for all MRP areas in one plant, choose the tab Intra-Plant View. Click on the button Vendor on top of the Intra-Plant View list to see the vendor linked to the corresponding MRP area.The elements in the Intra-Plant View are basically sorted according to the planning date. Choose button Separate MRP Areas to see the MRP elements separated for each of the MRP Areas.Check the Stock for both MRP Areas, 3310 and 3310SUB051. |  |  |
| 6 | Check other Subcontracting Components (Optional) | If you want to check the other subcontracting components, repeat steps #3 to #5 for materials FG0512, PK0504 and PK0508. |  |  |

##### Transfer Components to the Subcontractor

Purpose

This process step shows how to transfer components to the subcontractor.

Prerequisite

Requirement planning is carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Inventory Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Subcontracting Cockpit (F2948). | The Subcontracting Cockpit Screen is displayed. |  |
| 3 | Search for Component or Assembly | Set values to some filters to search ComponentsSubcontractor: 33305001Plant: 3310Choose GO.Note If no components are displayed please check the filter for the ‘Shipping Date’. In SAP standard the filter is restricted from -15 days to +15 days. If the shipping date is outside this time frame the number of days has to be changed in the filter criterias. | The search results show the details with the respective filter Criteria. Following columns must contain relevant data:ComponentPlantSubcontractorStock Balance |  |
| 4 | Display Purchase Order Item for a component | Choose small Arrow next to Component to expand the details. | All purchase order with items number corresponding to the component must be displayed in Document Item column.. |  |
| 5 | Post Goods Issue | Choose all PO Items from your purchase order and then choose Post Goods Issue. | There will be navigation to the Post Goods Issue (MIGO_GI). |  |
| 6 | Enter Detail Data | Check the following entries:Component: <Component which was chosen>Movement Type: 541Plant: 3310Storage Location: 331A (for FGXXXX materials) or 331C (for PKXXXX materials)Pending Quantity: <Depending on component>Base Unit of Measure: PCPlease make sure the components have stock in the storage location. If not, please do initial stock for them.If the component is batch managed in the system search the batch numbers via the search help and choose the correct batch from the list.It's also possible to post goods issue towards reservation if there's any. |  |  |
| 7 | Item OK | Check if the processing status is valid. |  |  |
| 8 | Post | Select all the items and Post Goods Issue. | The system displays the message Document 49XXXXXXXX posted with X item(s). |  |

##### Batch Transfer Posting

Purpose

The batches delivered to the subcontractor are in the special stock of subcontracting stock. These batches must now be transferred to the delivery batch number.

Prerequisite

The goods issue for the delivery of the component batch has taken place.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Post Goods Movement Tile | Open Post Goods Movement (MIGO). | The Goods Movement screen displays. |  |
| 3 | Screen Settings | In the upper area, enter the following data and choose Enter.Trans./ Event: Transfer PostingReference Document: OtherMovement Type: 309Special Stock Indicator: O | Entries are made. |  |
| 4 | Enter Material Data | Choose the tab Transfer Posting, enter the following data and choose Enter.From Material:< batch managed component from previous step> e.g. FG0511Destination Material: <same value as in the field before>From Plant: 3310Destination Plant: 3310From Batch: <batch used in chapter before>Destination batch: ddmmyyyySupplier: 33305001Follow above steps for FG0512 material as well. | dd=day, mm=month, yyyy=yearUnder the field "Special stock“. |  |
| 5 | Enter Material Data | Enter the following data on the tab Quantity and choose Enter.Quantity: <Qty in Unit of Entry from previous step> | Entries are made. |  |
| 6 | Enter Organization Data | Enter the following data on the tab where and choose Enter.Movement type: 309 OPlant: 3310Item Ok: <select> | Entries are made. |  |
| 7 | Check | Check if the processing status is valid. |  |  |
| 8 | Post | Choose Post. | Material document 49XXXXX posted. |  |

##### Batch Traceability

Purpose

In this step you check which batches are transferred to the subcontracting batch number.

Prerequisite

A batch transfer posting has been executed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad using the Quality Technician. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Batch Information Cockpit (BMBC). | The Batch Information Cockpit screen displays. |  |
| 3 | Screen Settings | In the Material, enter the following data and choose Execute Selection.Material: Material of batch componentPlant: 3310 | Entries are recorded. |  |
| 4 | Selection Results | Look for the delivery batch choose Display Batch. | dd=day, mm=month, yyyy=yearDetails of the delivery batch appears in the right detail screen. |  |
| 5 | Menu Bar | In the menu bar expand Details and open Usage. | In the lower area you can see the top-down analysis that shows you which batches were included in the delivery batch. |  |

|  |
| --- |
| Note You can proceed in the same way by selecting the component batch instead of the delivery batch. In this case, select the "Bottom-up" function. |

##### Evaluate Stock/Requirements Situation

Purpose

This process step shows you how to display the stock/requirements situation for Make-to-Stock finished goods (FG0502) and the components relevant for delivery to the subcontractor (finished and packaging materials) in the stock/requirements list after delivery of components to the subcontractor.

Prerequisite

Requirement planning is carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Monitor Stock / Requirements List - Old Version (MD04). | The Monitor Stock / Requirements List: Initial Screen is displayed. |  |
| 3 | Select Material | On the Monitor Stock / Requirements List: Initial Screen make the following entries and choose Continue.Material: FG0511Plant: 3310 | The Stock/Requirements List as of xxx hrs is displayed. |  |
| 4 | Review Stock / Requirements Situation for Subcontracting Component | On the Stock/Requirements List as of xxx hrs choose tab Intra-Plant View and press button Separate MRP Areas.The stock where the goods issue has been booked for has been automatically moved from the plant MRP Area 3310 to the MRP Area 3310SUB051 from the subcontractor.You can check directly which materials are currently on subcontractor site. The stock has been removed from the plant MRP area and is not considered in the plant MRP run anymore but in the MRP run for the subcontracting MRP Area 3310SUB051.You can also review for the other subcontracting components FG0512, PK0504 and PK0508. | The detailed Stock / Requirements List is displayed. |  |

##### Create Inbound Delivery for Subcontracting Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create an inbound delivery for a subcontracting purchase order.

|  |
| --- |
| Note This step is only possible if you executed option 3 for purchase order creation earlier: [Option-3 Create Purchase Order manually with Inbound Delivery](#unique_157) |

Prerequisite

Subcontracting purchase order (Option 3 from purchase order creation alternatives) created and approved.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Receiving Specialist. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open App | Open Create Inbound Delivery (VL31N). | The Create Inbound Delivery screen is displayed. |  |
| 3 | Enter Purchase Order | In the field Purchase order enter the subcontracting purchase order and choose Continue.Purchase Order: <Purchase Order from previous step> | The Inbound Delivery Create: Overview screen is displayed. |  |
| 4 | Select the tab Stock Placement | On the tab Stock Placement, enter in the field Putaway Qty the quantity equal to the delivery quantity and choose Save. | Inbound Delivery XXX has been saved message is displayed. |  |

##### Goods Receipt for Subcontracting Purchase Order

###### Option 1: Receive Goods for Subcontracting Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post the goods receipt for the material against the subcontracting PO.

|  |
| --- |
| Note This step is only possible if you executed option 1 or 2 for purchase order creation earlier(see 4.2.1.1: Option 1: Convert Purchase Requisition to Purchase Order or 4.2.1.2: Create Purchase Oder manually with inbound delivery) |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Post Goods Movement Tile | Open Post Goods Movement (MIGO). | The Goods Receipt Purchase Order - <User name> screen is displayed (or the name of the last process step which was executed in this app). |  |
| 3 | Select Goods Receipt Purchase Order Screen | Enter your PO number or search your subcontracting purchase order. | The items of the selected Purchase Order are displayed. |  |
| 4 | Check Quantity | Check the quantity of the Purchase Order and correct it in the detail data register tab Quantity, if needed. |  |  |
| 5 | Mark Item OK | Mark item OK in detail data in register tab Quantity. |  |  |
| 6 | Check Item | Click on Check to check the line item. | Note An Error message Enter the date of production and information ‘Batch XXX created’ might appear in a pop-up. In that case make the necessary entries. |  |
| 7 | OK | Accept the messages by clicking ENTER. |  |  |
| 8 | Check Batch Data | In the detail data in register tab Batch the information from the procured batch number is displayed. Please check the data. |  |  |
| 9 | Expand the Line Item | Click on the expand icon next to the line 1 item and the components are displayed.Note The quantities are corrected due to the BOM. If the quantity is changed after the expansion the quantities are not automatically recalculated. | The system displays all components and the quantities. |  |
| 10 | Maintain Components | Enter the batch numbers for the components if they are batch managed. | Batches are maintained on detail data. |  |
| 11 | Post | Choose Post. | The system displays the message Material document 5000000XX 202X posted. |  |

###### Option 2: Receive Goods from Subcontracting Purchase Order with Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post the goods receipt for the material against an Inbound Delivery.

|  |
| --- |
| Note This step is only possible if you executed option 3 for purchase order creation earlier: [Create Purchase Order manually with Inbound Delivery](#unique_157). |

Prerequisite

Inbound Delivery was created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Receiving Specialist. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Change Inbound Delivery (VL32N). | The The Change inbound delivery Initial screen is displayed. |  |
| 3 | Enter Inbound Delivery | In the field Inbound delivery enter the Inbound Delivery number and choose Continue. | The item overview of the inbound delivery is displayed. |  |
| 4 | Select the item on the Item Overview | Select the item Item overview tab. Mark one line and choose Item Detail. | The item detailed List is displayed. |  |
| 5 | Enter Shelf life and Batch for Subcontracted Material | Select the Material tab, make the following entries:Shelf Life Expiration or Date of ManufactureBatch numberChoose Back. | The Shelf Life Expiration or Date of Manufacture will be determined depending what you have entered. |  |
| 6 | Enter Batch Number for Component | Select the item Item overview tab and press SC Components. The pop up Edit components appears.Enter for each component where it is required a batch number and choose Confirm. |  |  |
| 7 | Post Goods Receipt | When you are back on the Item Overview tab, choose Post Goods Receipt. | The system saves Inbound Delivery. |  |

##### Evaluate Stock/Requirements Situation

Purpose

This process step shows you how to display the stock/requirements situation for Make-to-Stock finished goods (FG0502) and the components relevant for delivery to the subcontractor (finished and packaging materials) in the stock/requirements list after Goods receipt of components to the subcontractor.

Prerequisite

Requirement planning is carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Monitor Stock / Requirements List - Old Version (MD04). | The Monitor Stock / Requirements List: Initial Screen is displayed. |  |
| 3 | Select Material | On the Monitor Stock / Requirements List: Initial Screen make the following entries and choose Continue.Material: FG0502Plant: 3310 | The Stock/Requirements List as of xxx hrs is displayed. |  |
| 4 | Review Stock / Requirements Situation for Subcontracting Material | On the Stock/Requirements List as of xxx hrs review the stock listed for material FG0502.The unrestricted stock has not been increased, yet. This is attributed to the fact that only free available Stock is visible in the Stock/Requirements list. The material FG0502 is subject to quality inspection during goods receipt inspection and hence posted into quality inspection stock first. A disposition relevant quality Inspection Lot with the amount of posted goods receipt has been created. After quality inspection and accepted usage decision the inspection lot disappears, and the quantity is available in the unrestricted stock. | The detailed stock / requirements list is displayed. |  |
| 5 | Review Stock / Requirements Situation for Subcontracting Component | On the Monitor Stock/Requirements List Screen make the following entries and choose Refresh.Material: FG0511Plant: 3310Choose tab Intra-Plant view and press button Separate MRP Areas. Review the stock in the subcontracting area 3310SUB051 The stock has been reduced for the amount the components that has been booked during goods receipt of subcontracting material.Repeat the review for material FG0512, PK0504 and PK0508. |  |  |

#### Quality Inspection

Purpose

The material from subcontractor undergoes a quality inspection to ensure that it meets the predefined quality requirements. In this step, the quality technician records the inspection result for the required inspection characteristics. Afterwards, the quality engineer completes the inspection with a usage decision.

Prerequisite

The inspection is processed based on inspection lot. In this business process, the inspection lot has been created automatically upon goods receipt for the purchase order.

##### Display Material Stock Before Quality Inspection (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, a review of the material stock is done. Due to quality inspection, the material is not available for other processing.

Prerequisite

The goods receipt from purchase order was posted for the subcontracting material to quality inspection stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Inventory Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material screen displays. |  |
| 3 | Enter Material | Make the following entries and choose Enter:Material: FG0502 | Stock for the material and batch (from previous step) is displayed. |  |
| 4 | Check Stock Quantity | Check the Quality Inspection Stock under the plant 3310 and storage location 331A. | Quantity received is posted in quality stock. |  |
| 5 | Check Inspection Lots (Optional) | Choose Manage Stock on the bottom of the screen. Choose then Manage Inspection Lots on the bottom of the screen. | Inspection Lots for the selected material are displayed if you have further QM authorizations. |  |

##### Display Inspection Plan for Inspection Characteristics (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the inspection plan is related to the subcontracted material. The inspection plan defines all inspection characteristics used later in the quality inspection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Inspection Plan (QP03). | The Display Inspection Plan screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Continue.Material: FG0502Plant: 3310 |  |  |
| 4 | Select Entry Instruction | In the Inspection Plan Display: Task List Overview screen, select the row with GR Subcontracting Display and then choose Operations. | Only needed, if more than one inspection plan is assigned to the plan group. |  |
| 5 | Go to Inspection Characteristics Overview Screen | Select the operation 0010 and Choose either Inspection Characteristics or Menu > Inspection Characteristics . | The Display Inspection Plan: Characteristics Overview screen displays. |  |
| 6 | Review the Inspection Characteristics | There are two qualitative Master Inspection Characteristics:One is Visual Pack CheckOne is Label Check | You have now reviewed the inspection characteristics for which data has to be maintained within a later step.The sampling procedures and characteristics can be reviewed in detail. |  |

##### Display Quality Technician Overview (Optional)

Test Administration

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Approve Purchase Orders in the subcontracting section: the note says only POs with a value higher than 500.00 AED need release, but step 3 says POs with a net value of 500 AED or more have status In Approval (boundary differs).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Check Default Setting for Manage Material Coverage: the first Evaluate Stock/Requirements Situation says toggle OFF navigates to the old version (F0251), while the one after goods receipt for FG0511 says OFF also navigates to F0251A.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/test-script-sap-s-4hana-cloud-public-edition-from-planning-to-fulfillm-part-01]]
- related-to :: [[12-production-and-manufacturing/test-script-sap-s-4hana-cloud-public-edition-from-planning-to-fulfillm-part-03]]
- related-to :: [[08-sales-order-management/customer-returns-management-consumer-products-61v-ae-test-script-sap-s]]
- related-to :: [[12-production-and-manufacturing/produce-and-sell-standard-products-warehouse-managed-54v-ae-test-scrip]]
- related-to :: [[12-production-and-manufacturing/production-capacity-evaluation-and-leveling-consumer-products-5oi-ae-t]]
- related-to :: [[10-procurement/test-script-procurement-of-production-components-consumer-products-5w3]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6AA_S4CLD2608_BPD_EN_AE.docx` — lines 3042–6068 of the extracted text · extracted with `mammoth` · 604,664 chars in the whole document
