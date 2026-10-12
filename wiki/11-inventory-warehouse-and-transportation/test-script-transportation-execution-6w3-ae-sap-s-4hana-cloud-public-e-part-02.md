---
id: 11-inventory-warehouse-and-transportation/test-script-transportation-execution-6w3-ae-sap-s-4hana-cloud-public-e-part-02
title: "Test Script: Transportation Execution (6W3_AE) - SAP S/4HANA Cloud Public Edition (6W3_S4CLD2608_BPD_EN_AE) — part 2 of 3"
description: "Test script for scope item 6W3 Transportation Execution: ocean, air, stock transfer and advanced intercompany freight steps in SAP Fiori (TM/EWM)."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/transportation-planning-and-execution]
aliases: []
keywords: [Transportation Planning and Execution, transportation execution, freight order execution, ocean freight, air freight, freight cost accruals, advanced intercompany sales, advanced intercompany stock transfer, warehouse loading, radio frequency devices]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6W3_S4CLD2608_BPD_EN_AE.docx#lines-2770-5533"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1195
topic: 11-inventory-warehouse-and-transportation/transportation-planning-and-execution
language: EN
part: 2/3
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Transportation Execution (6W3_AE) - SAP S/4HANA Cloud Public Edition (6W3_S4CLD2608_BPD_EN_AE) — part 2 of 3

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6W3_S4CLD2608_BPD_EN_AE.docx`, part 2 of 3 (lines 2770–5533 of the extracted text), extracted with `mammoth`. Grouped under **Transportation Planning and Execution** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| 10. | Choose Execution Status (Destination) Set to Checked In | Choose Execution Status (Destination ) > Set to Checked In | The following system message appears: Check-In at stop SP_3310 was reported |  |
| 11. | Choose Save. | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

|  |
| --- |
| Note You can revoke the arrival and check-in events by setting the status to Set to Not Arrived and Set to Not Checked In |

##### Set Ready for Warehousing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck is unloaded, the Dispatcher (TM) sets the execution status to Set Ready for Warehouse Processing (Destination).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order for delivery> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Edit Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order screen, choose Edit. | The Edit Road Freight Order screen appears. |  |
| 7. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Set Execution Status | Choose Warehouse Processing Status > Set to Ready for Warehouse Processing (Destination) . | The following system message appears:Warehouse processing status updated for Freight Unit <your freight unit number>. |  |
| 10. | Choose Save | Choose Save and go back. | The following system message appears:Data saved successfully |  |

##### Set Truck Checked Out and Departed at Receiving Point Location (Delivery)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck has left the receiving point location, the Dispatcher (TM) sets the execution status to Set to Checked Out and Set to Departed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order for delivery> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Delivery screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Delivery screen, choose Edit. | The Edit Road Freight Order for Delivery screen appears. |  |
| 7. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Set Execution Status | Choose Execution Status (Destination) > Set to Checked Out . | The following system message appears: Checkout at stop SP_3310 and required preceding events were reported. |  |
| 10. | Set Execution Status | Choose Execution Status (Destination) > Set to Departed . | The following system message appears: Departure at stop SP_3310 was reported |  |
| 11. | Choose Save | Choose Save and go back. | The following system message appears:Data saved successfullyPlease continue with Succeeding Processes in the Appendix Process Integration. |  |

|  |
| --- |
| Note You can revoke the check-out and departed event by setting the status to Set to Not Checked Out and Set to Not Departed |

#### Stock Transfer

##### Set Truck Arrived and Checked In at Shipping Point Location (Pick-Up)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck has arrived at the shipping point, the Dispatcher (TM) sets the execution status to Set to Arrived and Set to Checked In in the freight order for pick-up.

In the freight order, the execution status is set to In Execution and the logistical execution status is set to Checked In in the shipping point. The status is also updated in the corresponding freight booking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order for pick up created in scope item 6W2 manual transportation planning> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Pick-Up screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Pick-Up screen, choose Edit. | The Edit Road Freight Order for Pick-Up screen appears. |  |
| 7. | Choose Execution Status Set to Ready for Transportation Execution | Choose Execution Status > Set to Ready for Transportation Execution. | The following system messages appear:Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Pick-Up <your freight order number> set to "Ready for Transportation Execution" |  |
| 8. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 9. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 10. | Choose Execution Status (Source) Set to Arrived | Choose Execution Status (Source) > Set to Arrived . | The following system message appears: Arrival at stop SP_3320 was reported |  |
| 11. | Choose Execution Status (Source) Set to Checked In | Choose Execution Status (Source) > Set to Checked In . | The following system message appears: Check-In at stop SP_3320 was reported |  |
| 12. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfullyCharge calculation completedCost distribution completed |  |

##### Loading

|  |
| --- |
| Note Only carry out this chapter if you have processed scope item 6W2 - Manual Transportation Planning with business condition 3BS - Warehouse Outbound Processing. Otherwise, you can skip this chapter. |

Purpose

In this step, you process loading activities in the warehouse with either the Fiori app or a Radio Frequency Device.

The Advanced Shipping and Receiving process is based on the TM freight order (FO). A prerequesite is an outbound delivery order with the transportation planning type ‘F’ and status ‘Ready for Shipping’. (Refer to scope item 3BS, step Set Deliveries to Ready for Shipping (Optional).)

|  |
| --- |
| Note Before loading steps are performed in the warehouse, the status of the freight order has to be set as ‘Ready for Transportation Execution’ ( refer to chapters Set Truck Arrived and Checked In at Shipping Point Location or Set Railcar Arrived and Checked In at Shipping Point Location). |

###### Variant 1: With Fiori App

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
| 1 | Log on | Open the SAP Fiori Launch Pad with the Warehouse Clerk (EWM) role. | The SAP Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Fiori app Load or Unload Freight Orders (/SCMTMS/ASR). | The Load or Unload Freight Orders (/SCMTMS/ASR) screen displays. |  |
| 3 | Find Freight Order | On the Load or Unload Freight Orders screen, make the following entries:Freight Order: <your freight order number>.Warehouse No: <your warehouse number, for example 3350>.Choose Go. |  |  |
| 4 | Assign Door (Optional) | Note You can skip this step, if you have done the following steps described in the Preliminary Steps chapter in Scope Item 3BS. A door has been assigned to the freight order automatically, based on those settings:Create loading pointAssign door to loading pointDetermine Staging Area – OutboundOn the Edit Freight Orders screen, select the level of loading stops and then choose Door Assignment > Assign Door.On the Assign Door screen, make the following entries:Loading/Unloading Point: <your loading point>.Warehouse Door: <your warehouse door>.Choose OK. | The following system message appears:Loading or unloading point XXXX and door XXXX of whse XXXX assigned to itemsWith the door assignment, a new loading stop is created for the combination of warehouse, door, and loading point. |  |
| 5 | Arrive at Door | Select the level of the stop and then choose Warehouse Door Status > Set to Arrived at Door.Choose Save. | The following messages appear:Status is set to Arrived at DoorWarehouse door status successfully updated for WH Loading Stop <Loading Stop> / <Whse No.> / <Door> |  |
| 6 | Perform Loading | Select the loading stop and then choose Execution Status > Set Items to Loaded.Choose Save. | The following system message appears:Event Loading End for Item successfully reportedThe loading status for the items under the stop is set to green. |  |
| 7 | Set Stop to Loading Finished (Optional) | Select the loading stop and then choose Execution Status > Set Stop to Loading Completed.Choose Save. |  |  |
| 8 | Departure from Door | Select the loading stop and then choose Warehouse Door StatusSet to Departed from Door .Choose Save. | The following system message appears:Warehouse door status successfully updated for WH Loading Stop <Loading Stop> / <Whse No.> / <Door>.Status is set to Departed from Door. |  |

###### Variant 2: With Radio Frequency Devices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) performs the loading activity in the system with a mobile Radio Frequency device.

|  |
| --- |
| Note For working with mobile RF devices, make sure all the steps as described in the Set-up Instruction guide for scope item 63V - Mobile RF Devices in Warehousing have been performed. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Test RF Environment (/SCWM/RFUI).Note Here the app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP note [3048632](https://me.sap.com/notes/3048632). |  |  |
| 3 | Enter Data for RFUI | Whse No: 3350Resource: SHA1-1 or SHR1-1DefPresDvc: SE01Choose Enter. |  |  |
| 4 | Choose Menu | Choose 04 Outbound Process > 03 Loading > 01 Loading by Delivery. |  |  |
| 5 | Enter Outbound Delivery Order Number | In the Del. No. field, enter <Outbound Delivery Order number>.Choose Enter. |  |  |
| 6 | Check HU List | Choose F1 to view the HU List. |  |  |
| 7 | Load HU | Make the following entries:HU: <one of the HUs from the list>Choose Enter.The HU has been loaded. |  |  |
| 8 | Load Remaining HUs | Repeat step 7 until all the HUs are loaded. |  |  |
| 9 | Confirm Loading Completion | In the Complete Loading dialog box, choose Yes. |  |  |
| 10 | Log off from RFUI | You can choose Back to return to the previous screens.Choose Logoff.Choose Save. |  |  |

##### Set Truck Checked Out and Departed at Shipping Point Location (Pick-Up)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once the truck is loaded, the Dispatcher (TM) sets the execution status in the freight order to Set to Checked Out. After the truck has left the shipping plant, the status is Set to Departed.

Besides the changes of the execution status and the logistical execution status in the freight order, the status is also updated in the corresponding freight booking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders(F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order for pick up> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Pick-Up screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Pick-Up screen, choose Edit. | The Edit Road Freight Order for Pick-Up screen appears. |  |
| 7. | Scroll down to the Items sub section | Scroll down to the Items sub section. |  |  |
| 8. | Select Item | In the Items table, select the line with the container by selecting the respective checkbox. |  |  |
| 9. | Navigate to the Quantities tab | Navigate to the Quantities tab. |  |  |
| 10. | Enter Verified Gross Mass | Under Verified Gross Mass make the following entries:Weight: <gross weight for container item + 100> KGWeighing Method: Weighing the Packed ContainerWeighing Date/Time: <today>Person Responsible for Weighing: <name of person responsible>Partner Function: ShipperWeighing Location: <enter your location of location type loading point> |  |  |
| 11. | Choose Save | Choose Save. | The following system message appears:Data saved successfully |  |
| 12. | Navigate to the Seals tab | Navigate to the Seals tab. |  |  |
| 13. | Enter Seals Information | Under Seals make the following entries:Seal Number: ANZ4711815Sealing Date: <today> |  |  |
| 14. | Choose Save | Choose Save. | The following system message appears:Data saved successfully |  |
| 15. | Print / Display a preview of Shipment Documents (optional) | Navigate to the Output Request tab.In the output request table, choose Display of any print document in column display.Note The system creates the output requests for the respective print documents automatically after the freight order is saved.Printing is done when the checkout event is reported, also automatically.Additional output requests can be created manually by choosing Insert. Enter the following data per table row:Output Type: <output type>Role: <carrier>Recipient: <carrier number>Form Country/Region: <source country>Form Language: <carrier language>Form Template: <form template>For triggering the printing of output requests manually, select it and choose Send Output. | The print document is opened as a PDF through the Adobe Document Service. |  |
| 16. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 17. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 18. | Choose Execution Status (Source) Set to Checked Out | Choose Execution Status (Source) > Set to Checked Out . | The following system message appears: Checkout at stop SP_3320 was reported |  |
| 19. | Choose Execution Status (Source) Set to Departed | Choose Execution Status (Source) > Set to Departed . | The following system message appears: Departure at stop SP_3320 was reported |  |
| 20. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

|  |
| --- |
| Note You can revoke the check-out and departed event by setting the status to Set to Not Checked Out and Set to Not Departed. |

##### Post Goods Issue for Stock Transport Order

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
| 1 | Log On | Log ont o the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad appears. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen appears. |  |
| 3 | Enter Delivery Number | On the Change Outbound Delivery screen, enter the delivery document number from the earlier section and choose Continue. | The Replenishment Dlv. <your Outbound Delivery Number> Change: Overview screen appears. |  |
| 4 | Post Goods Issue | On the Change Outbound Delivery screen, choose Post Goods Issue. |  |  |

##### Arrival of Truck at Port of Loading (Pick-Up)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck has arrived at the port of loading, the Dispatcher (TM) sets the execution status to Set to Arrived.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order for pick up> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Pick-Up screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Pick-Up screen, choose Edit. | The Edit Road Freight Order for Pick-Up screen appears. |  |
| 7. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Choose Execution Status (Destination) Set to Arrived | Choose Execution Status (Destination ) > Set to Arrived . | The following system message appears:Arrival at stop PORT_AESID was reported |  |
| 10. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

##### Departure of Vessel from Port of Loading (Main Leg)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the vessel departed, the Dispatcher (TM) sets the execution status to Set to Shipped on Board.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Manage Ocean Freight Bookings (F6213). | The Manage Ocean Freight Bookings (F6213) screen is displayed. |  |
| 3. | Filter Ocean Freight Booking | On the Manage Ocean Freight Bookings screen, make the following entries:Ocean Freight Booking: <freight booking number created in scope item 6W2 step perform manual transportation planning> |  |  |
| 4. | Choose Go | On the Manage Ocean Freight Bookings screen, choose Go. | Ocean freight booking matching the selection criteria is listed. |  |
| 5. | Navigate to Ocean Freight Booking | In the Ocean Freight Bookings table, select one Ocean Freight Booking. | The Display Ocean Freight Booking screen appears. |  |
| 6. | Edit Ocean Freight Booking | On the Display Ocean Freight Booking screen, choose Edit. | The Edit Ocean Freight Booking screen appears. |  |
| 7. | Choose Execution Status Set to Loaded at Port of Loading. | Choose Execution Status > Set to Loaded at Port of Loading. | The following system message appears:Loading end at stopPORT_AESIDwas reported |  |
| 8. | Set Execution Status to Shipped on Board | Choose Execution Status > Set to Shipped on Board . |  |  |
| 9. | Choose Ok | In the Set to Shipped on Board dialog box, choose OK | The following system message appears:Departure at stop PORT_AESID was reported |  |
| 10. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

##### Confirm Freight Costs for Accrual Postings

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step the Transportation Buyer monitors the freight documents (freight orders or freight bookings) and posts accruals.

The Transportation Buyer reviews these freight documents prior to posting the freight cost accruals, to ensure that they correspond to the provided transportation services of the freight forwarder or carrier. This ensures a good data quality for the financial department.

The overall freight costs of the freight documents are allocated to the respective transportation requirements, for example sales order or delivery based on gross weight. On the Cost Distribution tab, it is shown how the freight costs are broken down by sales order item or delivery item reference.

As a final step, the freight document can be confirmed for accrual postings. The system automatically posts the freight costs to financial accounting as accruals and creates a freight cost allocation document, a service purchase order and a service entry sheet. Financial postings are created depending on the business scenario to either expenses for an outbound process or to material accounts for an inbound process.

|  |
| --- |
| Note If the automatic freight cost confirmation and posting is activated as described in chapter Automate Confirmation and Posting of Freight Costs (Optional), the freight order is automatically confirmed for accrual posting. Alternatively, the Transportation Buyer can confirm selected freight orders for accrual posting manually as described below.If you performed Confirm Freight Cost for Accruals Postings in 6W3, you can skip this process and proceed with Monitor Freight Cost Allocation Documents.You only need to perform this process once for each freight document. |

Procedure

Table 13:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Transportation Buyer. | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Accrual Postings (F4329). | The Monitor Accruals Postings screen appears. |  |
| 3. | Enter Selection Criteria | On the Monitor Accrual Postings screen, make the following entry:Purchasing Organization: 3310Freight Document: Optionally <Enter your freight order or freight booking number>Note Example:For advanced intercompany sales or advanced intercompany stock transfer in case of an ocean freight booking, enter company code 1710.For advanced intercompany sales or advanced intercompany stock transfer in case of the freight order on-carriage, enter company code 3310.For all other scenarios, use company code 3310. |  |  |
| 4. | Choose Go | Choose Go. | The freight documents are displayed in the Monitor Accrual Postings table. |  |
| 5. | Navigate to the For Confirmation Tab | Navigate to the For Confirmation tab. | The freight documents for confirmation are displayed in the Monitor Accrual Postings table. |  |
| 6. | Freight Order / Freight Booking Details | Select the freight document row in the Monitor Accruals Posting table. | The Road Freight Order <your freight order number> - Process Accruals screen appears.orThe Rail Freight Order <your freight order number> - Process Accruals screen appears.orThe Ocean Freight Booking <your freight booking number> - Process Accruals screen appears.orThe Air Freight Booking <your freight booking number> - Process Accruals screen appears. |  |
| 7. | Display General Data (Optional) | Navigate to the General Data tab to review the header information. |  |  |
| 8. | Display Charges (Optional) | Scroll down to the Charges section to review the detailed information. | The charge item for the carrier or freight forwarder is displayed. |  |
| 9. | Display Charges (Optional) | In the Charge Hierarchy expand the node TM Carrier | The charge lines are displayed. |  |
| 10. | Display Charges Details (Optional) | Choose Show/Hide Details.Note Make sure that only one line is selected | The charge line details are displayed. |  |
| 11. | Display Stages (Optional) | Navigate to the Stages tab to review the stage details. |  |  |
| 12. | Display Business Partners (Optional) | Navigate to the Business Partner tab to review the parties involved. |  |  |
| 13. | Display Cost Distribution (Optional) | Navigate to the Cost Distribution tab to review the parties involved. | In the Distribution Hierarchy table it is shown how the freight costs are broken down by a sales order item or delivery item reference. |  |
| 14. | Confirm Freight Order or Confirm Freight Booking | Choose Confirm for Posting. | The following system message appears: Freight document <your freight order or freight booking> for <Your carrier or freight forwarder> confirmed for postingNote After confirming the freight order or freight booking for accruals posting, a service purchase order and a service entry sheet is created automatically in a background process. These documents are the basis for the invoice verification.Additionally, freight cost allocation documents (except for scope item BMY - Subcontracting purchase order with TM integration) are created as follows:Freight Cost Allocation (Expense) in all the legal ledgers for outbound transportation scenario (sell from stock, customer consignment fill-up/pickup, freight costs in the delivering company for ICO stock transport order and ICO intercompany sales process)Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario (procurement of material, inbound transport costs related to the ICO Stock transport order by the receiving company)If group valuation is activated, in case of ICO STO, the freight costs in the delivering company, Freight Cost Allocation (ML-Account), are posted in the group valuation ledger.For scope item BMY – Subcontracting purchase order with TM integration, freight cost allocation documents are created as follows:Freight Cost Allocation (ML-Account) in all the legal ledgers for outbound transportation scenario is only created when the goods receipt is performed for the inbound delivery of subcontracting purchase order. In case the confirming of freight document is done after goods receipt, the freight cost allocation (ML-Account) in all legal is created during confirming the freight document itself as done during usual freight cost confirming process.Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario.To see the details of the freight cost allocation document, follow the steps mentioned in the Monitor Freight Cost Allocation documents. |  |
| 15. | Navigate Back | Navigate back |  |  |

|  |
| --- |
| Note To confirm multiple freight documents simultaneously, choose multiple freight document checkboxes on the Monitor Accrual Postings overview page (under the For Confirmation tab) and choose Confirm for Posting. |

In case the posting result is an error, follow the steps below to check the error details and repost.

If, for example, the posting date is in a closed period, the posting date needs to be changed prior to posting of the freight document. You need to scroll down to the Charges section, navigate to the Posting Date tab, and change the accrual posting date in column Posting Date.

Table 14:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access App | Open Monitor Accrual Postings - Freight Documents (F4329). | The Monitor Accruals Postings screen appears. |  |
| 2 | Enter Selection Criteria | On the Monitor Accrual Postings screen, make the following entry:Purchasing Organization: 3310Freight Document: Optionally <Enter your freight order or freight booking number>Note Example:For advanced intercompany sales or advanced intercompany stock transfer in case of an ocean freight booking, enter company code 1710.For advanced intercompany sales or advanced intercompany stock transfer in case of the freight order on-carriage, enter company code 3310.For all other scenarios, use company code 3310. |  |  |
| 3 | Choose Go | Choose Go. | The freight documents are displayed in the Monitor Accrual Posting table. |  |
| 4 | Navigate to the Errors Tab | Navigate to the Errors tab | The freight documents with errors are displayed in the Monitor Accrual Postings table. |  |
| 5 | Show the Error Description | Navigate to the corresponding line and choose Show Errors. | The Application Log appears, containing a detailed description of the errors. |  |
| 6 | Show the Error Details | Select the error details by selecting the error link in the Description column. | The message details are shown containing a diagnosis and guidance on possible solutions. |  |
| 7 | Correct the Errors | Correct the errors according to the message details. |  |  |
| 8 | Select the Freight Order or Freight Booking in the Freight Document Table | Select the Freight Document checkbox. |  |  |
| 9 | Post Accruals | Choose Post. | The following system message appears: Freight document <your freight order or freight booking> for <Your carrier or freight forwarder> confirmed for postingNote After confirming the freight order or freight booking for accruals posting, a service purchase order and a service entry sheet is created automatically in a background process. These documents are the basis for the invoice verification.Additionally, freight cost allocation documents (except for scope item BMY - Subcontracting purchase order with TM integration) are created as follows:Freight Cost Allocation (Expense) in all the legal ledgers for outbound transportation scenario (sell from stock, customer consignment fill-up/pickup, freight costs in the delivering company for ICO stock transport order and ICO intercompany sales process)Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario (procurement of material, inbound transport costs related to the ICO Stock transport order by the receiving company)If group valuation is activated, in case of ICO STO, the freight costs in the delivering company, Freight Cost Allocation (ML-Account), are posted in the group valuation ledger.For scope item BMY – Subcontracting purchase order with TM integration, freight cost allocation documents are created as follows:Freight Cost Allocation (ML-Account) in all the legal ledgers for outbound transportation scenario is only created when the goods receipt is performed for the inbound delivery of subcontracting purchase order. In case the confirming of freight document is done after goods receipt the freight cost allocation (ML-Account) in all legal is created during confirming, the freight document itself as done during usual freight cost con-firming process.Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario.To see the details of the freight cost allocation document, follow the steps mentioned in the Monitor Freight Cost Allocation documents. |  |

##### Arrival of Vessel at Port of Discharge (Main Leg)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the vessel has arrived, the Dispatcher (TM) sets the execution status to Set to Arrived at Final Port of Discharge.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Launch App | Open Manage Ocean Freight Bookings (F6213). | The Manage Ocean Freight Bookings (F6213) screen is displayed. |  |
| 3. | Filter Ocean Freight Booking | On the Manage Ocean Freight Bookings screen, make the following entries:Ocean Freight Booking: <your freight booking number> |  |  |
| 4. | Choose Go | On the Manage Ocean Freight Bookings screen, choose Go. | Ocean freight booking matching the selection criteria is listed. |  |
| 5. | Navigate to Ocean Freight Booking | In the Ocean Freight Bookings table, select one Ocean Freight Booking. | The Display Ocean Freight Booking screen appears. |  |
| 6. | Edit Ocean Freight Booking | On the Display Ocean Freight Booking screen, choose Edit. | The Edit Ocean Freight Booking screen appears. |  |
| 7. | Set Execution Status to Arrived at Final Port of Discharge | Choose Execution Status > Set to Arrived at Final Port of Discharge . |  |  |
| 8. | Choose OK | In the Set to Shipped on Board dialog box, choose OK. | The following system message appears:Arrival at stop PORT_AEYAS was reported |  |
| 9. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

##### Departure of Truck at Port of Discharge (Delivery)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck is loaded and has left the port of discharge, the status of the freight order is set to Set to Departed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order for delivery created in scope item 6W2 manual transportation planning> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Delivery screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Delivery screen, choose Edit. | The Edit Road Freight Order for Delivery screen appears. |  |
| 7. | Choose Execution Status Set to Ready for Transportation Execution | Choose Execution Status > Set to Ready for Transportation Execution. | The following system messages appear:Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Delivery <your freight order number> set to "Ready for Transportation Execution" |  |
| 8. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 9. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 10. | Choose Execution Status (Source) Departed | Choose Execution Status (Source) > Departed . | The following system message appears:Departure at stop PORT_AEYAS was reported |  |
| 11. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

|  |
| --- |
| Note You can revoke the departed event by setting the status to Set to Not Departed. |

##### Set Truck Arrived and Checked In at Receiving Point Location (Delivery)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

After the truck has arrived at the destination location the Dispatcher (TM) sets execution status to Set to Arrived and Set to Checked In.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM) | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order for delivery> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Delivery screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Orderfor Delivery screen, choose Edit. | The Edit Road Freight Order for Delivery screen appears. |  |
| 7. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Set Execution Status | Choose Execution Status (Destination ) > Set to Arrived . | The following system message appears: Arrival at stop SP_3310 was reported |  |
| 10. | Set Execution Status | Choose Execution Status (Destination ) > Set to Checked In . | The following system message appears: Check-In at stop SP_3310 was reported |  |
| 11. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

##### Set Ready for Warehousing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck is unloaded, the Dispatcher (TM) sets the execution status to Set Ready for Warehouse Processing (Destination).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order for delivery> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Edit Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Delivery screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Delivery screen, choose Edit. | The Edit Road Freight Order for Delivery screen appears. |  |
| 7. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Choose Set Ready for Warehouse Processing | Choose Warehouse Processing Status > Set to Ready for Warehouse Processing (Destination) . |  |  |
| 10. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

##### Set Truck Checked Out and Departed at Receiving Point Location (Delivery)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck has left the receiving point location, the Dispatcher (TM) sets the execution status to Checked Out and Set to Departed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders(F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order for delivery> |  |  |
| 4. | Choose Go | Choose Go . | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Delivery screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Delivery screen, choose Edit. | The Edit Road Freight Order for Delivery screen appears. |  |
| 7. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Choose Execution Status (Destination) Set to Checked Out | Choose Execution Status (Destination) > Set to Checked Out . | The following system message appears: Checkout at stop SP_3310 was reported. |  |
| 10. | Choose Execution Status (Destination) Set to Departed | Choose Execution Status (Destination) > Set to Departed . | The following system message appears: Departure at stop SP_3310 was reported |  |
| 11. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfullyPlease continue with Succeeding Processes in the Appendix Process Integration. |  |

|  |
| --- |
| Note You can revoke the check-out and departed event by setting the status to Set to Not Checked Out and Set to Not Departed |

### Air

#### Outbound

##### Set Truck Arrived and Checked In at Shipping Point Location (Pick-Up)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck has arrived at the shipping point, the Dispatcher (TM) sets the execution status to Set to Arrived and Set to Checked In in the freight order for pick-up.

In the freight order, the execution status is set to In Execution and the logistical execution status is set to Checked In in the shipping point. The status is also updated in the corresponding freight booking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order for pick up created in scope item 6W2 manual transportation planning> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Pick-Up screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Pick-Up screen, choose Edit. | The Edit Road Freight Order for Pick-Up screen appears. |  |
| 7. | Set Execution Status | Choose Execution Status > Set to Ready for Transportation Execution. | The following system messages appear:Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Pick-Up <your freight order number> set to "Ready for Transportation Execution" |  |
| 8. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 9. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 10. | Choose Execution Status (Source) Set to Arrived | Choose Execution Status (Source) > Set to Arrived . | The following system message appears: Arrival at stop SP_3310 was reported |  |
| 11. | Set Execution Status | Choose Execution Status (Source) > Set to Checked In . | The following system message appears: Check-In at stop SP_3310 was reported |  |
| 12. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfullyCharge calculation completedCost distribution completed |  |

##### Loading

|  |
| --- |
| Note Only carry out this chapter if you have processed scope item 6W2 - Manual Transportation Planning with business condition 3BS - Warehouse Outbound Processing. Otherwise, you can skip this chapter. |

Purpose

In this step, you process loading activities in the warehouse with either the Fiori app or a Radio Frequency Device.

The Advanced Shipping and Receiving process is based on the TM freight order (FO). A prerequesite is an outbound delivery order with the transportation planning type ‘F’ and status ‘Ready for Shipping’. (Refer to scope item 3BS, step Set Deliveries to Ready for Shipping (Optional).)

|  |
| --- |
| Note Before loading steps are performed in the warehouse, the status of the freight order has to be set as ‘Ready for Transportation Execution’ ( refer to chapters Set Truck Arrived and Checked In at Shipping Point Location or Set Railcar Arrived and Checked In at Shipping Point Location). |

###### Variant 1: With Fiori App

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
| 1 | Log on | Open the SAP Fiori Launch Pad with the Warehouse Clerk (EWM) role. | The SAP Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Fiori app Load or Unload Freight Orders (/SCMTMS/ASR). | The Load or Unload Freight Orders (/SCMTMS/ASR) screen displays. |  |
| 3 | Find Freight Order | On the Load or Unload Freight Orders screen, make the following entries:Freight Order: <your freight order number>.Warehouse No: <your warehouse number, for example 3350>.Choose Go. |  |  |
| 4 | Assign Door (Optional) | Note You can skip this step, if you have done the following steps described in the Preliminary Steps chapter in Scope Item 3BS. A door has been assigned to the freight order automatically, based on those settings:Create loading pointAssign door to loading pointDetermine Staging Area – OutboundOn the Edit Freight Orders screen, select the level of loading stops and then choose Door Assignment > Assign Door.On the Assign Door screen, make the following entries:Loading/Unloading Point: <your loading point>.Warehouse Door: <your warehouse door>.Choose OK. | The following system message appears:Loading or unloading point XXXX and door XXXX of whse XXXX assigned to itemsWith the door assignment, a new loading stop is created for the combination of warehouse, door, and loading point. |  |
| 5 | Arrive at Door | Select the level of the stop and then choose Warehouse Door Status > Set to Arrived at Door.Choose Save. | The following messages appear:Status is set to Arrived at DoorWarehouse door status successfully updated for WH Loading Stop <Loading Stop> / <Whse No.> / <Door> |  |
| 6 | Perform Loading | Select the loading stop and then choose Execution Status > Set Items to Loaded.Choose Save. | The following system message appears:Event Loading End for Item successfully reportedThe loading status for the items under the stop is set to green. |  |
| 7 | Set Stop to Loading Finished (Optional) | Select the loading stop and then choose Execution Status > Set Stop to Loading Completed.Choose Save. |  |  |
| 8 | Departure from Door | Select the loading stop and then choose Warehouse Door StatusSet to Departed from Door .Choose Save. | The following system message appears:Warehouse door status successfully updated for WH Loading Stop <Loading Stop> / <Whse No.> / <Door>.Status is set to Departed from Door. |  |

###### Variant 2: With Radio Frequency Devices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) performs the loading activity in the system with a mobile Radio Frequency device.

|  |
| --- |
| Note For working with mobile RF devices, make sure all the steps as described in the Set-up Instruction guide for scope item 63V - Mobile RF Devices in Warehousing have been performed. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Test RF Environment (/SCWM/RFUI).Note Here the app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP note [3048632](https://me.sap.com/notes/3048632). |  |  |
| 3 | Enter Data for RFUI | Whse No: 3350Resource: SHA1-1 or SHR1-1DefPresDvc: SE01Choose Enter. |  |  |
| 4 | Choose Menu | Choose 04 Outbound Process > 03 Loading > 01 Loading by Delivery. |  |  |
| 5 | Enter Outbound Delivery Order Number | In the Del. No. field, enter <Outbound Delivery Order number>.Choose Enter. |  |  |
| 6 | Check HU List | Choose F1 to view the HU List. |  |  |
| 7 | Load HU | Make the following entries:HU: <one of the HUs from the list>Choose Enter.The HU has been loaded. |  |  |
| 8 | Load Remaining HUs | Repeat step 7 until all the HUs are loaded. |  |  |
| 9 | Confirm Loading Completion | In the Complete Loading dialog box, choose Yes. |  |  |
| 10 | Log off from RFUI | You can choose Back to return to the previous screens.Choose Logoff.Choose Save. |  |  |

##### Set Truck Checked Out and Departed at Shipping Point Location (Pick-Up)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck is loaded, the Dispatcher (TM) sets the execution status in the freight order to Set to Checked Out. After the truck has left the shipping plant, the status is Set to Departed.

Besides the changes of the execution status and the logistical execution status in the freight order, the status is also updated in the corresponding freight booking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders(F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order for pick up> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Pick-Up screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Pick-Up screen, choose Edit. | The Edit Road Freight Order for Pick-Up screen appears. |  |
| 7. | Print / Display a Preview of Shipment Documents (Optional) | Navigate to tab Output Request.In the output request table, choose Display of any print document in column display.Note The system creates the output requests for the respective print documents automatically after the freight order is saved.Printing is done when the check-out event is reported, also automatically.Additional output requests can be created manually by choosing Insert. Enter the following data per table row:Output Type: <output type>Role: <carrier>Recipient: <carrier number>Form Country/Region: <source country>Form Language: <carrier language>Form Template: <form template>For triggering the printing of output requests manually, select it and choose Send Output. | The print document is opened as a PDF through the Adobe Document Service. |  |
| 8. | Scroll to the Stages Sub Section | Scroll to the Stages sub section. |  |  |
| 9. | In the Stages table, select the Stage Checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 10. | Choose Execution Status (Source) Set to Checked Out. | Choose Execution Status (Source) > Set to Checked Out . | The following system message appears: Checkout at stop SP_3310 was reported |  |
| 11. | Choose Execution Status (Source) Set to Departed | Choose Execution Status (Source) > Set to Departed . | The following system message appears: Departure at stop SP_3310 was reported |  |
| 12. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

|  |
| --- |
| Note You can revoke the check-out and departed event by setting the status to Set toNot Checked Out and Set toNot Departed. |

##### Post Goods Issue

Purpose

This process step shows you how to post goods issues for the delivery. Execute this process step for all delivery documents.

Depending on the baseline scenario (BD9, 3NR, BMY, 1IU or 3BS) execute one of the following procedures.

Procedure

In case of BD9, BMY, 1IU, and 3NR, execute the following steps:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entries and choose Execute:Shipping Point: 3310Note In the case of Advanced Intercompany Sales or Advanced Intercompany Stock Transfer, the shipping point should be 1710. |  |  |
| 4 | Post Good Issue | Select your outbound delivery note, and choose Post Goods Issue.Select today’s date from the dialog box, and choose Continue. | A message confirms the goods issue has been posted.Advanced shipping notification has been automatically sent to the ship-to party via EDI based on the consignment order document.Note Open the consignment order from the Document Flow and navigate to Output Request or the Communication History tab to see the advanced shipping notification. |  |

In case of 3BS, execute the following steps:

|  |
| --- |
| Note If you triggered the goods movement posting in step Loading (Optional) of scope item Warehouse Outbound Processing (3BS), you can skip the Post Goods Issue step. |

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Delivery Orders (F6498) . | The Manage Outbound Delivery Orders (F6498) screen appears. |  |
| 3 | Enter Warehouse Number | Make the following entries:Warehouse No:3350 |  |  |
| 4 | Set Departure Date/Time | Make the following entries:Departure Date/Time: <Departure Date/Time Range> |  |  |
| 5 | Choose Go | Choose Go. | The Outbound Delivery Order screen appears. |  |
| 6 | WM: Post Good Issue | Select your outbound delivery order, and choose Post Goods Issue. | A message confirms the goods issue has been posted.The Warehouse Material Document has been created. |  |

##### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A billing document is created that contains, besides the charges for goods, the transportation costs to be billed to the customer.

Procedure

Table 3: Overview

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents (F0798) screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings, you can make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for billing due list | In the search condition, use criteria if necessary. | Sales document(s) display in the result. |  |
| 5 | Select item(s) for billing | Select row(s) of SD Document created previously and choose Create Billing Documents. | The Create Billing Document screen displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, for example current date, then choose OK. | The draft billing document with TMP xxxxxx displays. |  |
| 7 | Save Billing Document | On the Manage Billing Document screen, choose Save.The draft version billing document with TMP xxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | The system generates an invoice for billing. |  |

##### Arrival of Truck at Airport of Departure (Pick-Up)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck has arrived at the airport of departure, the Dispatcher (TM) sets the execution status in the freight order to Set to Arrived.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori Launchpad opens. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Order screen, make the following entries:Freight Order: <your freight order for pick up> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order for Pick-Up | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight for Pick-Up screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Pick-Up screen, choose Edit. | The Edit Road Freight Order for Pick-Up screen appears. |  |
| 7. | Scroll to the Stages Subsection | Scroll down to the Stages sub section. |  |  |
| 8. | Select Stage | In the Stages table, select the Stage 1. |  |  |
| 9. | Choose Execution Status (Destination) Set to Arrived | Choose Execution Status (Destination) > Set to Arrived . | The following system message appears:Arrival at stop AIRPORT_DXB and required preceding events were reported |  |
| 10. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

##### Departure of Airplane at Airport of Departure (Main Leg)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the airplane has departed, the Dispatcher (TM) sets the execution status in the freight booking to Set to Uplift Confirmed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Manage Air Freight Bookings (F6535). | The Manage Air Freight Bookings (F6535) screen appears. |  |
| 3. | Enter Air Freight Booking | On the Manage Air Freight Bookings screen, make the following entries:Air Freight Booking: <air freight booking number created in scope item 6W2 step perform manual transportation planning> |  |  |
| 4. | Choose Go | Choose Go. | Air freight booking matching the selection criteria is listed. |  |
| 5. | Navigate to Air Freight Booking | In the Air Freight Bookings table, select one air freight booking. | The Display Air Freight Booking screen appears. |  |
| 6. | Choose Edit | On the Display Air Freight Booking screen, choose Edit. | The Edit Air Freight Booking screen appears. |  |
| 7. | Set to Uplift Confirmed | Choose Execution Status > Set to Uplift Confirmed . | The Set to Uplift Confirmed dialog box appears. |  |
| 8. | Enter Uplift Date and Shipped-On Board Time | In the Set to Uplift Confirmed dialog box, make the following entries:Uplift Date: <today’s date>Shipped-on Board Time: <time of day> |  |  |
| 9. | Choose OK | Choose OK. | The following system message appears:Departure at stop AIRPORT_DXB was reported |  |
| 10. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

##### Confirm Freight Costs for Accrual Postings

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step the Transportation Buyer monitors the freight documents (freight orders or freight bookings) and posts accruals.

The Transportation Buyer reviews these freight documents prior to posting the freight cost accruals, to ensure that they correspond to the provided transportation services of the freight forwarder or carrier. This ensures a good data quality for the financial department.

The overall freight costs of the freight documents are allocated to the respective transportation requirements, for example sales order or delivery based on gross weight. On the Cost Distribution tab, it is shown how the freight costs are broken down by sales order item or delivery item reference.

As a final step, the freight document can be confirmed for accrual postings. The system automatically posts the freight costs to financial accounting as accruals and creates a freight cost allocation document, a service purchase order and a service entry sheet. Financial postings are created depending on the business scenario to either expenses for an outbound process or to material accounts for an inbound process.

|  |
| --- |
| Note If the automatic freight cost confirmation and posting is activated as described in chapter Automate Confirmation and Posting of Freight Costs (Optional), the freight order is automatically confirmed for accrual posting. Alternatively, the Transportation Buyer can confirm selected freight orders for accrual posting manually as described below.If you performed Confirm Freight Cost for Accruals Postings in 6W3, you can skip this process and proceed with Monitor Freight Cost Allocation Documents.You only need to perform this process once for each freight document. |

Procedure

Table 15:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Transportation Buyer. | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Accrual Postings (F4329). | The Monitor Accruals Postings screen appears. |  |
| 3. | Enter Selection Criteria | On the Monitor Accrual Postings screen, make the following entry:Purchasing Organization: 3310Freight Document: Optionally <Enter your freight order or freight booking number>Note Example:For advanced intercompany sales or advanced intercompany stock transfer in case of an ocean freight booking, enter company code 1710.For advanced intercompany sales or advanced intercompany stock transfer in case of the freight order on-carriage, enter company code 3310.For all other scenarios, use company code 3310. |  |  |
| 4. | Choose Go | Choose Go. | The freight documents are displayed in the Monitor Accrual Postings table. |  |
| 5. | Navigate to the For Confirmation Tab | Navigate to the For Confirmation tab. | The freight documents for confirmation are displayed in the Monitor Accrual Postings table. |  |
| 6. | Freight Order / Freight Booking Details | Select the freight document row in the Monitor Accruals Posting table. | The Road Freight Order <your freight order number> - Process Accruals screen appears.orThe Rail Freight Order <your freight order number> - Process Accruals screen appears.orThe Ocean Freight Booking <your freight booking number> - Process Accruals screen appears.orThe Air Freight Booking <your freight booking number> - Process Accruals screen appears. |  |
| 7. | Display General Data (Optional) | Navigate to the General Data tab to review the header information. |  |  |
| 8. | Display Charges (Optional) | Scroll down to the Charges section to review the detailed information. | The charge item for the carrier or freight forwarder is displayed. |  |
| 9. | Display Charges (Optional) | In the Charge Hierarchy expand the node TM Carrier | The charge lines are displayed. |  |
| 10. | Display Charges Details (Optional) | Choose Show/Hide Details.Note Make sure that only one line is selected | The charge line details are displayed. |  |
| 11. | Display Stages (Optional) | Navigate to the Stages tab to review the stage details. |  |  |
| 12. | Display Business Partners (Optional) | Navigate to the Business Partner tab to review the parties involved. |  |  |
| 13. | Display Cost Distribution (Optional) | Navigate to the Cost Distribution tab to review the parties involved. | In the Distribution Hierarchy table it is shown how the freight costs are broken down by a sales order item or delivery item reference. |  |
| 14. | Confirm Freight Order or Confirm Freight Booking | Choose Confirm for Posting. | The following system message appears: Freight document <your freight order or freight booking> for <Your carrier or freight forwarder> confirmed for postingNote After confirming the freight order or freight booking for accruals posting, a service purchase order and a service entry sheet is created automatically in a background process. These documents are the basis for the invoice verification.Additionally, freight cost allocation documents (except for scope item BMY - Subcontracting purchase order with TM integration) are created as follows:Freight Cost Allocation (Expense) in all the legal ledgers for outbound transportation scenario (sell from stock, customer consignment fill-up/pickup, freight costs in the delivering company for ICO stock transport order and ICO intercompany sales process)Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario (procurement of material, inbound transport costs related to the ICO Stock transport order by the receiving company)If group valuation is activated, in case of ICO STO, the freight costs in the delivering company, Freight Cost Allocation (ML-Account), are posted in the group valuation ledger.For scope item BMY – Subcontracting purchase order with TM integration, freight cost allocation documents are created as follows:Freight Cost Allocation (ML-Account) in all the legal ledgers for outbound transportation scenario is only created when the goods receipt is performed for the inbound delivery of subcontracting purchase order. In case the confirming of freight document is done after goods receipt, the freight cost allocation (ML-Account) in all legal is created during confirming the freight document itself as done during usual freight cost confirming process.Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario.To see the details of the freight cost allocation document, follow the steps mentioned in the Monitor Freight Cost Allocation documents. |  |
| 15. | Navigate Back | Navigate back |  |  |

|  |
| --- |
| Note To confirm multiple freight documents simultaneously, choose multiple freight document checkboxes on the Monitor Accrual Postings overview page (under the For Confirmation tab) and choose Confirm for Posting. |

In case the posting result is an error, follow the steps below to check the error details and repost.

If, for example, the posting date is in a closed period, the posting date needs to be changed prior to posting of the freight document. You need to scroll down to the Charges section, navigate to the Posting Date tab, and change the accrual posting date in column Posting Date.

Table 16:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access App | Open Monitor Accrual Postings - Freight Documents (F4329). | The Monitor Accruals Postings screen appears. |  |
| 2 | Enter Selection Criteria | On the Monitor Accrual Postings screen, make the following entry:Purchasing Organization: 3310Freight Document: Optionally <Enter your freight order or freight booking number>Note Example:For advanced intercompany sales or advanced intercompany stock transfer in case of an ocean freight booking, enter company code 1710.For advanced intercompany sales or advanced intercompany stock transfer in case of the freight order on-carriage, enter company code 3310.For all other scenarios, use company code 3310. |  |  |
| 3 | Choose Go | Choose Go. | The freight documents are displayed in the Monitor Accrual Posting table. |  |
| 4 | Navigate to the Errors Tab | Navigate to the Errors tab | The freight documents with errors are displayed in the Monitor Accrual Postings table. |  |
| 5 | Show the Error Description | Navigate to the corresponding line and choose Show Errors. | The Application Log appears, containing a detailed description of the errors. |  |
| 6 | Show the Error Details | Select the error details by selecting the error link in the Description column. | The message details are shown containing a diagnosis and guidance on possible solutions. |  |
| 7 | Correct the Errors | Correct the errors according to the message details. |  |  |
| 8 | Select the Freight Order or Freight Booking in the Freight Document Table | Select the Freight Document checkbox. |  |  |
| 9 | Post Accruals | Choose Post. | The following system message appears: Freight document <your freight order or freight booking> for <Your carrier or freight forwarder> confirmed for postingNote After confirming the freight order or freight booking for accruals posting, a service purchase order and a service entry sheet is created automatically in a background process. These documents are the basis for the invoice verification.Additionally, freight cost allocation documents (except for scope item BMY - Subcontracting purchase order with TM integration) are created as follows:Freight Cost Allocation (Expense) in all the legal ledgers for outbound transportation scenario (sell from stock, customer consignment fill-up/pickup, freight costs in the delivering company for ICO stock transport order and ICO intercompany sales process)Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario (procurement of material, inbound transport costs related to the ICO Stock transport order by the receiving company)If group valuation is activated, in case of ICO STO, the freight costs in the delivering company, Freight Cost Allocation (ML-Account), are posted in the group valuation ledger.For scope item BMY – Subcontracting purchase order with TM integration, freight cost allocation documents are created as follows:Freight Cost Allocation (ML-Account) in all the legal ledgers for outbound transportation scenario is only created when the goods receipt is performed for the inbound delivery of subcontracting purchase order. In case the confirming of freight document is done after goods receipt the freight cost allocation (ML-Account) in all legal is created during confirming, the freight document itself as done during usual freight cost con-firming process.Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario.To see the details of the freight cost allocation document, follow the steps mentioned in the Monitor Freight Cost Allocation documents. |  |

##### Arrival of Airplane at Airport of Destination (Main Leg)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the airplane has arrived at the airport of destination, the Dispatcher (TM) sets the execution status to Set to Arrived at Final Airport of Destination.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Manage Air Freight Bookings (F6535). | The Manage Air Freight Bookings (F6535) screen appears. |  |
| 3. | Enter Air Freight Booking | On the Manage Air Freight Bookings screen, make the following entries:Air Freight Booking: <your air freight booking number> |  |  |
| 4. | Choose Go | Choose Go. | Air freight booking matching the selection criteria is listed. |  |
| 5. | Navigate to Air Freight Booking | In the Air Freight Bookings table, select one air freight booking. | The Display Air Freight Booking screen appears. |  |
| 6. | Choose Edit | On the Display Air Freight Booking screen, choose Edit. | The Edit Air Freight Booking screen appears. |  |
| 7. | Set Execution Status | Choose Execution Status > Set to Arrived at Final Airport of Destination. | The Set to Arrived at Final Airport of Destination dialog box appears. |  |
| 8. | Enter Dates for Freight Booking | In the Set to Arrived at Final Airport of Destination dialog box, make the following entries:Arrival Date at Final Destination: <today’s date>Shipped-on Board Time: <time of day> |  |  |
| 9. | Choose OK | Choose OK. | The following system message appears:Arrival at stop <AIRPORT> was reported |  |
| 10. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

##### Departure of Truck at Airport of Destination (Delivery)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck is loaded and has left the airport of destination, the status of the freight order is set to Set to Departed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad opens. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Order screen appears. |  |
| 3. | Enter Selection Criteria | On the Monitor Execution of Freight Order screen, make the following entries:Freight Order: <your freight order for delivery created in scope item 6W2 manual transportation planning> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Delivery screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Delivery screen, choose Edit. | The Edit Road Freight Order for Delivery screen appears. |  |
| 7. | Set Execution Status | Choose Execution Status > Set to Ready for Transportation Execution. | The following system messages appear:Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Delivery <freight order number for delivery from previous step> set to "Ready for Transportation Execution" |  |
| 8. | Scroll Down to the Stages Table | Scroll down to the Stages table. |  |  |
| 9. | Select Stage | In the Stages table, select the Stage 1. |  |  |
| 10. | Choose Execution Status (Source) Set to Departed | Choose Execution Status (Source) > Set to Departed. | The following system messages appear:Handling execution status for AIRPORT_AUH set to "Departed" |  |
| 11. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

##### Set Truck Arrived at Customer Location (Delivery)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the arrival at the customer location is reported.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori Launchpad opens. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Order screen appears. |  |
| 3. | Enter Selection Criteria | On the Monitor Execution of Freight Order screen, make the following entries:Freight Order: <your freight order for delivery> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Delivery screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Delivery screen, choose Edit. | The Edit Road Freight Order screen appears. |  |
| 7. | Scroll down to the Stages sub section | Scroll down to the Stages sub section. |  |  |
| 8. | Select Stage | In the Stages table, select the Stage 1. |  |  |
| 9. | Choose Execution Status (Destination) Set to Arrived | Choose Execution Status (Destination) > Set to Arrived. | The following system message appears: Arrival at stop 33186002 and required preceding events were reported |  |
| 10. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfullyPlease continue with Succeeding Processes in the Appendix Process Integration. |  |

#### Inbound

##### Arrival of Truck at Airport of Departure (Pick-Up)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck has arrived at the airport of departure, the Dispatcher (TM) sets the execution status in the freight order to Set to Arrived.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad opens. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen appears. |  |
| 3. | Enter Selection Criteria | On the Monitor Execution of Freight Order screen, make the following entries:Freight Order: <your freight order for pick up created in scope item 6W2 manual transportation planning> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Navigate to Freight Order for Pick-Up | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Pick-Up <freight order number for pick-up from previous step> screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Pick-Up screen, choose Edit. | The Edit Road Freight Order for Pick-Up <freight order number for pick-up from previous step> screen appears. |  |
| 7. | Choose Execution Status Set to Ready for Transportation Execution | Choose Execution Status > Set to Ready for Transportation Execution. | The following system messages appear:Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Pick-Up <your freight order number> set to "Ready for Transportation Execution" |  |
| 8. | Scroll Down to Stages sub section | Scroll down to the Stages sub section. |  |  |
| 9. | Select Stage | In the Stages table, select the Stage 1. |  |  |
| 10. | Choose Execution Status (Destination) Set to Arrived | Choose Execution Status (Destination) > Set to Arrived . | The following system message appears:Arrival at stop AIRPORT_AUH and required preceding events were reported |  |
| 11. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

##### Departure of Airplane at Airport of Departure (Main Leg)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the airplane has departed, the Dispatcher (TM) sets the execution status in the freight booking to Set to Uplift Confirmed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Manage Air Freight Bookings (F6535). | The Manage Air Freight Bookings (F6535) screen appears. |  |
| 3. | Enter Air Freight Booking | On the Manage Air Freight Bookings screen, make the following entries:Air Freight Booking: <air freight booking number created in scope item 6W2 step perform manual transportation planning> |  |  |
| 4. | Choose Go | Choose Go. | Air freight booking matching the selection criteria is listed. |  |
| 5. | Navigate to Air Freight Booking | Choose your air freight booking. | The Display Air Freight Booking screen appears. |  |
| 6. | Choose Edit | On the Display Air Freight Booking screen, choose Edit. | The Edit Air Freight Booking screen appears. |  |
| 7. | Choose Execution Status Set to Uplift Confirmed | Choose Execution Status > Set to Uplift Confirmed . | The Set to Uplift Confirmed dialog box appears. |  |
| 8. | Enter Uplift Date and Shipped-On Board Time | In the Set to Uplift Confirmed dialog box, make the following entries:Uplift Date: <today’s date>Shipped-on Board Time: <time of day> |  |  |
| 9. | Chose OK | Chose OK. | The following system message appears:Departure at stop AIRPORT_AUH was reported |  |
| 10. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

##### Confirm Freight Costs for Accrual Postings

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step the Transportation Buyer monitors the freight documents (freight orders or freight bookings) and posts accruals.

The Transportation Buyer reviews these freight documents prior to posting the freight cost accruals, to ensure that they correspond to the provided transportation services of the freight forwarder or carrier. This ensures a good data quality for the financial department.

The overall freight costs of the freight documents are allocated to the respective transportation requirements, for example sales order or delivery based on gross weight. On the Cost Distribution tab, it is shown how the freight costs are broken down by sales order item or delivery item reference.

As a final step, the freight document can be confirmed for accrual postings. The system automatically posts the freight costs to financial accounting as accruals and creates a freight cost allocation document, a service purchase order and a service entry sheet. Financial postings are created depending on the business scenario to either expenses for an outbound process or to material accounts for an inbound process.

|  |
| --- |
| Note If the automatic freight cost confirmation and posting is activated as described in chapter Automate Confirmation and Posting of Freight Costs (Optional), the freight order is automatically confirmed for accrual posting. Alternatively, the Transportation Buyer can confirm selected freight orders for accrual posting manually as described below.If you performed Confirm Freight Cost for Accruals Postings in 6W3, you can skip this process and proceed with Monitor Freight Cost Allocation Documents.You only need to perform this process once for each freight document. |

Procedure

Table 17:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Transportation Buyer. | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Accrual Postings (F4329). | The Monitor Accruals Postings screen appears. |  |
| 3. | Enter Selection Criteria | On the Monitor Accrual Postings screen, make the following entry:Purchasing Organization: 3310Freight Document: Optionally <Enter your freight order or freight booking number>Note Example:For advanced intercompany sales or advanced intercompany stock transfer in case of an ocean freight booking, enter company code 1710.For advanced intercompany sales or advanced intercompany stock transfer in case of the freight order on-carriage, enter company code 3310.For all other scenarios, use company code 3310. |  |  |
| 4. | Choose Go | Choose Go. | The freight documents are displayed in the Monitor Accrual Postings table. |  |
| 5. | Navigate to the For Confirmation Tab | Navigate to the For Confirmation tab. | The freight documents for confirmation are displayed in the Monitor Accrual Postings table. |  |
| 6. | Freight Order / Freight Booking Details | Select the freight document row in the Monitor Accruals Posting table. | The Road Freight Order <your freight order number> - Process Accruals screen appears.orThe Rail Freight Order <your freight order number> - Process Accruals screen appears.orThe Ocean Freight Booking <your freight booking number> - Process Accruals screen appears.orThe Air Freight Booking <your freight booking number> - Process Accruals screen appears. |  |
| 7. | Display General Data (Optional) | Navigate to the General Data tab to review the header information. |  |  |
| 8. | Display Charges (Optional) | Scroll down to the Charges section to review the detailed information. | The charge item for the carrier or freight forwarder is displayed. |  |
| 9. | Display Charges (Optional) | In the Charge Hierarchy expand the node TM Carrier | The charge lines are displayed. |  |
| 10. | Display Charges Details (Optional) | Choose Show/Hide Details.Note Make sure that only one line is selected | The charge line details are displayed. |  |
| 11. | Display Stages (Optional) | Navigate to the Stages tab to review the stage details. |  |  |
| 12. | Display Business Partners (Optional) | Navigate to the Business Partner tab to review the parties involved. |  |  |
| 13. | Display Cost Distribution (Optional) | Navigate to the Cost Distribution tab to review the parties involved. | In the Distribution Hierarchy table it is shown how the freight costs are broken down by a sales order item or delivery item reference. |  |
| 14. | Confirm Freight Order or Confirm Freight Booking | Choose Confirm for Posting. | The following system message appears: Freight document <your freight order or freight booking> for <Your carrier or freight forwarder> confirmed for postingNote After confirming the freight order or freight booking for accruals posting, a service purchase order and a service entry sheet is created automatically in a background process. These documents are the basis for the invoice verification.Additionally, freight cost allocation documents (except for scope item BMY - Subcontracting purchase order with TM integration) are created as follows:Freight Cost Allocation (Expense) in all the legal ledgers for outbound transportation scenario (sell from stock, customer consignment fill-up/pickup, freight costs in the delivering company for ICO stock transport order and ICO intercompany sales process)Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario (procurement of material, inbound transport costs related to the ICO Stock transport order by the receiving company)If group valuation is activated, in case of ICO STO, the freight costs in the delivering company, Freight Cost Allocation (ML-Account), are posted in the group valuation ledger.For scope item BMY – Subcontracting purchase order with TM integration, freight cost allocation documents are created as follows:Freight Cost Allocation (ML-Account) in all the legal ledgers for outbound transportation scenario is only created when the goods receipt is performed for the inbound delivery of subcontracting purchase order. In case the confirming of freight document is done after goods receipt, the freight cost allocation (ML-Account) in all legal is created during confirming the freight document itself as done during usual freight cost confirming process.Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario.To see the details of the freight cost allocation document, follow the steps mentioned in the Monitor Freight Cost Allocation documents. |  |
| 15. | Navigate Back | Navigate back |  |  |

|  |
| --- |
| Note To confirm multiple freight documents simultaneously, choose multiple freight document checkboxes on the Monitor Accrual Postings overview page (under the For Confirmation tab) and choose Confirm for Posting. |

In case the posting result is an error, follow the steps below to check the error details and repost.

If, for example, the posting date is in a closed period, the posting date needs to be changed prior to posting of the freight document. You need to scroll down to the Charges section, navigate to the Posting Date tab, and change the accrual posting date in column Posting Date.

Table 18:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access App | Open Monitor Accrual Postings - Freight Documents (F4329). | The Monitor Accruals Postings screen appears. |  |
| 2 | Enter Selection Criteria | On the Monitor Accrual Postings screen, make the following entry:Purchasing Organization: 3310Freight Document: Optionally <Enter your freight order or freight booking number>Note Example:For advanced intercompany sales or advanced intercompany stock transfer in case of an ocean freight booking, enter company code 1710.For advanced intercompany sales or advanced intercompany stock transfer in case of the freight order on-carriage, enter company code 3310.For all other scenarios, use company code 3310. |  |  |
| 3 | Choose Go | Choose Go. | The freight documents are displayed in the Monitor Accrual Posting table. |  |
| 4 | Navigate to the Errors Tab | Navigate to the Errors tab | The freight documents with errors are displayed in the Monitor Accrual Postings table. |  |
| 5 | Show the Error Description | Navigate to the corresponding line and choose Show Errors. | The Application Log appears, containing a detailed description of the errors. |  |
| 6 | Show the Error Details | Select the error details by selecting the error link in the Description column. | The message details are shown containing a diagnosis and guidance on possible solutions. |  |
| 7 | Correct the Errors | Correct the errors according to the message details. |  |  |
| 8 | Select the Freight Order or Freight Booking in the Freight Document Table | Select the Freight Document checkbox. |  |  |
| 9 | Post Accruals | Choose Post. | The following system message appears: Freight document <your freight order or freight booking> for <Your carrier or freight forwarder> confirmed for postingNote After confirming the freight order or freight booking for accruals posting, a service purchase order and a service entry sheet is created automatically in a background process. These documents are the basis for the invoice verification.Additionally, freight cost allocation documents (except for scope item BMY - Subcontracting purchase order with TM integration) are created as follows:Freight Cost Allocation (Expense) in all the legal ledgers for outbound transportation scenario (sell from stock, customer consignment fill-up/pickup, freight costs in the delivering company for ICO stock transport order and ICO intercompany sales process)Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario (procurement of material, inbound transport costs related to the ICO Stock transport order by the receiving company)If group valuation is activated, in case of ICO STO, the freight costs in the delivering company, Freight Cost Allocation (ML-Account), are posted in the group valuation ledger.For scope item BMY – Subcontracting purchase order with TM integration, freight cost allocation documents are created as follows:Freight Cost Allocation (ML-Account) in all the legal ledgers for outbound transportation scenario is only created when the goods receipt is performed for the inbound delivery of subcontracting purchase order. In case the confirming of freight document is done after goods receipt the freight cost allocation (ML-Account) in all legal is created during confirming, the freight document itself as done during usual freight cost con-firming process.Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario.To see the details of the freight cost allocation document, follow the steps mentioned in the Monitor Freight Cost Allocation documents. |  |

##### Arrival of Airplane at Airport of Destination (Main Leg)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the airplane has arrived at the airport of destination, theDispatcher (TM) sets the execution status to Set to Arrived at Final Airport of Destination.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Launch App | Open Manage Air Freight Bookings (F6535). | The Manage Air Freight Bookings (F6535) screen appears. |  |
| 3. | Enter Air Freight Booking | On the Manage Air Freight Bookings screen, make the following entries:Air Freight Booking: <your air freight booking number> |  |  |
| 4. | Choose Go | Choose Go. | Air freight booking matching the selection criteria is listed. |  |
| 5. | Navigate to Air Freight Booking | Choose your air freight booking. | The Display Air Freight Booking screen appears. |  |
| 6. | Choose Edit | On the Display Air Freight Booking screen, choose Edit. | The Edit Air Freight Booking screen appears. |  |
| 7. | Choose Execution Status Set to Arrived at Final Airport of Destination | Choose Execution Status > Set to Arrived at Final Airport of Destination. | The Set to Arrived at Final Airport of Destination dialog box appears. |  |
| 8. | Enter Dates for Freight Booking | In the Set to Arrived at Final Airport of Destination dialog box, make the following entries:Arrival Date at Final Destination: <today’s date>Shipped-on Board Time: <time of day> |  |  |
| 9. | Chose OK | Chose OK. | The following system message appears:Arrival at stop AIRPORT_DXB was reported |  |
|  | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

##### Departure of Truck at Airport of Destination (Delivery)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck is loaded and has left the airport of destination, the status of the freight order is Set to Departed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad opens. |  |
| 2. | Launch App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Order screen appears. |  |
| 3. | Enter Selection Criteria | On the Monitor Execution of Freight Order screen, make the following entries:Freight Order: <your freight order for delivery created in scope item 6W2 manual transportation planning> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Delivery <freight order number for delivery from previous step> screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Delivery <freight order number for delivery from previous step> screen, choose Edit. | The Edit Road Freight Order for Delivery <freight order number for delivery from previous step> screen appears. |  |
| 7. | Choose Execution Status Set to Ready for Transportation Execution | Choose Execution Status > Set to Ready for Transportation Execution. | The following system messages appear:Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Delivery <freight order number for delivery from previous step> set to "Ready for Transportation Execution" |  |
| 8. | Scroll down to the Stages Subsection | Scroll down to the Stages subsection. |  |  |
| 9. | Select Stage | In the Stages table, select the Stage 1. |  |  |
| 10. | Choose Execution Status (Source) Set to Departed | Choose Execution Status (Source) > Set to Departed. | The following system messages appear:Departure at stop AIRPORT_DXB and required preceding events were reported |  |
| 11. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

##### Set Truck Arrived and Checked In at Receiving Point Location (Delivery)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

After the truck has arrived at the destination location the Dispatcher (TM) sets the execution status to Set to Arrived and Set to Checked In.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM) | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order for delivery> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Delivery screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Delivery screen, choose Edit. | The Edit Road Freight Order for Delivery screen appears. |  |
| 7. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Choose Execution Status (Destination) Set to Arrived | Choose Execution Status (Destination ) > Set to Arrived . | The following system message appears: Arrival at stop SP_3310 was reported |  |
| 10. | Choose Execution Status (Destination) Set to Checked In | Choose Execution Status (Destination ) > Set to Checked In . | The following system message appears: Check-In at stop SP_3310 was reported |  |
| 11. | Choose Save | Choose Save and go back | The following system messages appear:Data saved successfully |  |

|  |
| --- |
| Note You can revoke the arrival and check-in events by setting the status to Set to Not Arrived and Set to Not Checked In |

##### Set Ready for Warehousing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck is unloaded, the Dispatcher (TM) sets the execution status to Set Ready for Warehouse Processing (Destination).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Air Freight Booking: <your Freight Order for Delivery> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Edit Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Delivery screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Delivery screen, choose Edit. | The Edit Road Freight Order for Delivery screen appears. |  |
| 7. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Choose Set Ready for Warehouse Processing (Destination) | Choose Warehouse Processing Status > Set to Ready for Warehouse Processing (Destination) . |  |  |
| 10. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

##### Set Truck Checked Out and Departed at Receiving Point Location (Delivery)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck has left the receiving point location, the Dispatcher (TM) sets the execution status to Set to Checked Out and Set to Departed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders(F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order for delivery> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Delivery screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Delivery screen, choose Edit. | The Edit Road Freight Order for Delivery screen appears. |  |
| 7. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages Table, Select the Stage Checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Choose Execution Status (Destination) Set to Checked Out | Choose Execution Status (Destination) > Set to Checked Out . | The following system message appears: Checkout at stop SP_3310 was reported |  |
| 10. | Choose Execution Status (Destination) Set to Departed | Choose Execution Status (Destination) > Set to Departed . | The following system message appears: Departure at stop SP_3310 was reported |  |
| 11. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfullyPlease continue with Succeeding Processes in the Appendix Process Integration. |  |

|  |
| --- |
| Note You can revoke the checkout and departed event by setting the status to Set to Not Checked Out and Set to Not Departed. |

#### Stock Transfer

##### Set Truck Arrived and Checked In at Shipping Point Location (Pick-Up)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck has arrived at the shipping point, the Dispatcher (TM) sets the execution status to Set to Arrived and Set to Checked In in the freight order for pick-up.

In the freight order, the execution status is set to In Execution and the logistical execution status is set to Checked In in the shipping point. The status is also updated in the corresponding freight booking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order for pick up created in scope item 6W2 manual transportation planning> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Pick-Up screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Pick-Up screen, choose Edit. | The Edit Road Freight Order for Pick-Up screen appears. |  |
| 7. | Choose Execution Status Set to Ready for Transportation Execution | Choose Execution Status > Set to Ready for Transportation Execution. | The following system messages appear:Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Pick-Up <your freight order number> set to "Ready for Transportation Execution" |  |
| 8. | Scroll to the Stages Sub Section | Scroll to the Stages sub section. |  |  |
| 9. | In the Stages table, Select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 10. | Choose Execution Status (Source) Set to Arrived | Choose Execution Status (Source) > Set to Arrived . | The following system message appears: Arrival at stop SP_3320 was reported |  |
| 11. | Choose Execution Status (Source) Set to Checked In | Choose Execution Status (Source) > Set to Checked In . | The following system message appears: Check-In at stop SP_3320 was reported |  |
| 12. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfullyCharge calculation completedCost distribution completed |  |

|  |
| --- |
| Note You can revoke the arrival and check-in events by setting the status to Set to Not Arrived and Set to Not Checked In. |

##### Loading

|  |
| --- |
| Note Only carry out this chapter if you have processed scope item 6W2 - Manual Transportation Planning with business condition 3BS - Warehouse Outbound Processing. Otherwise, you can skip this chapter. |

Purpose

In this step, you process loading activities in the warehouse with either the Fiori app or a Radio Frequency Device.

The Advanced Shipping and Receiving process is based on the TM freight order (FO). A prerequesite is an outbound delivery order with the transportation planning type ‘F’ and status ‘Ready for Shipping’. (Refer to scope item 3BS, step Set Deliveries to Ready for Shipping (Optional).)

|  |
| --- |
| Note Before loading steps are performed in the warehouse, the status of the freight order has to be set as ‘Ready for Transportation Execution’ ( refer to chapters Set Truck Arrived and Checked In at Shipping Point Location or Set Railcar Arrived and Checked In at Shipping Point Location). |

###### Variant 1: With Fiori App

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
| 1 | Log on | Open the SAP Fiori Launch Pad with the Warehouse Clerk (EWM) role. | The SAP Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Fiori app Load or Unload Freight Orders (/SCMTMS/ASR). | The Load or Unload Freight Orders (/SCMTMS/ASR) screen displays. |  |
| 3 | Find Freight Order | On the Load or Unload Freight Orders screen, make the following entries:Freight Order: <your freight order number>.Warehouse No: <your warehouse number, for example 3350>.Choose Go. |  |  |
| 4 | Assign Door (Optional) | Note You can skip this step, if you have done the following steps described in the Preliminary Steps chapter in Scope Item 3BS. A door has been assigned to the freight order automatically, based on those settings:Create loading pointAssign door to loading pointDetermine Staging Area – OutboundOn the Edit Freight Orders screen, select the level of loading stops and then choose Door Assignment > Assign Door.On the Assign Door screen, make the following entries:Loading/Unloading Point: <your loading point>.Warehouse Door: <your warehouse door>.Choose OK. | The following system message appears:Loading or unloading point XXXX and door XXXX of whse XXXX assigned to itemsWith the door assignment, a new loading stop is created for the combination of warehouse, door, and loading point. |  |
| 5 | Arrive at Door | Select the level of the stop and then choose Warehouse Door Status > Set to Arrived at Door.Choose Save. | The following messages appear:Status is set to Arrived at DoorWarehouse door status successfully updated for WH Loading Stop <Loading Stop> / <Whse No.> / <Door> |  |
| 6 | Perform Loading | Select the loading stop and then choose Execution Status > Set Items to Loaded.Choose Save. | The following system message appears:Event Loading End for Item successfully reportedThe loading status for the items under the stop is set to green. |  |
| 7 | Set Stop to Loading Finished (Optional) | Select the loading stop and then choose Execution Status > Set Stop to Loading Completed.Choose Save. |  |  |
| 8 | Departure from Door | Select the loading stop and then choose Warehouse Door StatusSet to Departed from Door .Choose Save. | The following system message appears:Warehouse door status successfully updated for WH Loading Stop <Loading Stop> / <Whse No.> / <Door>.Status is set to Departed from Door. |  |

###### Variant 2: With Radio Frequency Devices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) performs the loading activity in the system with a mobile Radio Frequency device.

|  |
| --- |
| Note For working with mobile RF devices, make sure all the steps as described in the Set-up Instruction guide for scope item 63V - Mobile RF Devices in Warehousing have been performed. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Test RF Environment (/SCWM/RFUI).Note Here the app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP note [3048632](https://me.sap.com/notes/3048632). |  |  |
| 3 | Enter Data for RFUI | Whse No: 3350Resource: SHA1-1 or SHR1-1DefPresDvc: SE01Choose Enter. |  |  |
| 4 | Choose Menu | Choose 04 Outbound Process > 03 Loading > 01 Loading by Delivery. |  |  |
| 5 | Enter Outbound Delivery Order Number | In the Del. No. field, enter <Outbound Delivery Order number>.Choose Enter. |  |  |
| 6 | Check HU List | Choose F1 to view the HU List. |  |  |
| 7 | Load HU | Make the following entries:HU: <one of the HUs from the list>Choose Enter.The HU has been loaded. |  |  |
| 8 | Load Remaining HUs | Repeat step 7 until all the HUs are loaded. |  |  |
| 9 | Confirm Loading Completion | In the Complete Loading dialog box, choose Yes. |  |  |
| 10 | Log off from RFUI | You can choose Back to return to the previous screens.Choose Logoff.Choose Save. |  |  |

##### Set Truck Checked Out and Departed at Shipping Point Location (Pick-Up)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once the truck is loaded, the Dispatcher (TM) sets the execution status in the freight order to Set to Checked Out. After the truck has left the shipping plant, the status is set to Set to Departed.

Besides the changes of the execution status and the logistical execution status in the freight order, the status is also updated in the corresponding freight booking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | Monitor Execution of Freight Orders (F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order for pick up> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Pick-Up screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Pick-Up screen, choose Edit. | The Edit Road Freight Order for Pick-Up screen appears. |  |
| 7. | Print / Display a preview of Shipment Documents (optional) | Navigate to tab Output Request.In the output request table, choose Display of any print document in column display.Note The system creates the output requests for the respective print documents automatically after the freight order is saved.Printing is done when the check out event is reported, also automatically.Additional output requests can be created manually by choosing Insert. Enter the following data per table row:Output Type: <output type>Role: <carrier>Recipient: <carrier number>Form Country/Region: <source country>Form Language: <carrier language>Form Template: <form template>For triggering the printing of output requests manually, select it and choose Send Output. | The print document is opened as a PDF through the Adobe Document Service. |  |
| 8. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 9. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 10. | Choose Execution Status (Source) Set to Checked Out | Choose Execution Status (Source) > Set to Checked Out . | The following system message appears: Checkout at stop SP_3320 was reported |  |
| 11. | Choose Execution Status (Source) Set to Departed | Choose Execution Status (Source) > Set to Departed . | The following system message appears: Departure at stop SP_3320 was reported |  |
| 12. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

|  |
| --- |
| Note You can revoke the check-out and departed event by setting the status to Set to Not Checked Out and Set to Not Departed |

##### Post Goods Issue for Stock Transport Order

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
| 1 | Log On | Log ont o the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad appears. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen appears. |  |
| 3 | Enter Delivery Number | On the Change Outbound Delivery screen, enter the delivery document number from the earlier section and choose Continue. | The Replenishment Dlv. <your Outbound Delivery Number> Change: Overview screen appears. |  |
| 4 | Post Goods Issue | On the Change Outbound Delivery screen, choose Post Goods Issue. |  |  |

##### Arrival of Truck at Airport of Departure (Pick-Up)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck has arrived at the airport of departure, the Dispatcher (TM) sets the execution status in the freight order to Set to Arrived.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad opens. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Order screen, make the following entries:Freight Order: <your freight order for pick up> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order for Pick-Up | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight for Pick-Up screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Pick-Up screen, choose Edit. | The Edit Road Freight Order for Pick-Up screen appears. |  |
| 7. | Scroll to the Stages sub section | Scroll down to the Stages sub section. |  |  |
| 8. | Select Stage | In the Stages table, select the Stage 1. |  |  |
| 9. | Choose Execution Status (Destination) Set to Arrived | Choose Execution Status (Destination) > Set to Arrived . | The following system message appears:Arrival at stop AIRPORT_AUH and required preceding events were reported |  |
| 10. | Choose Save | Choose Save and go back. | The following system message appears:Data saved successfully |  |

##### Departure of Airplane at Airport of Departure (Main Leg)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the airplane has departed, the Dispatcher (TM) sets the execution status in the freight booking to Set to Uplift Confirmed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Manage Air Freight Bookings (F6535). | The Manage Air Freight Bookings (F6535) screen appears. |  |
| 3. | Enter Air Freight Booking | On the Manage Air Freight Bookings screen, make the following entries:Air Freight Booking: <air freight booking number created in scope item 6W2 step perform manual transportation planning> |  |  |
| 4. | Choose Go | Choose Go. | Air freight booking matching the selection criteria is listed. |  |
| 5. | Navigate to Air Freight Booking | Choose your air freight booking. | The Display Air Freight Booking screen appears. |  |
| 6. | Choose Edit | On the Display Air Freight Booking screen, choose Edit. | The Edit Air Freight Booking screen appears. |  |
| 7. | Choose Execution Status Set to Uplift Confirmed | Choose Execution Status > Set to Uplift Confirmed . | The Set to Uplift Confirmed dialog box appears. |  |
| 8. | Enter Uplift Date and Shipped-On Board Time | In the Set to Uplift Confirmed dialog box, make the following entries:Uplift Date: <today’s date>Shipped-on Board Time: <time of day> |  |  |
| 9. | Choose OK | Choose OK. | The following system message appears:Departure at stop AIRPORT_AUH was reported |  |
| 10. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

##### Confirm Freight Costs for Accrual Postings

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step the Transportation Buyer monitors the freight documents (freight orders or freight bookings) and posts accruals.

The Transportation Buyer reviews these freight documents prior to posting the freight cost accruals, to ensure that they correspond to the provided transportation services of the freight forwarder or carrier. This ensures a good data quality for the financial department.

The overall freight costs of the freight documents are allocated to the respective transportation requirements, for example sales order or delivery based on gross weight. On the Cost Distribution tab, it is shown how the freight costs are broken down by sales order item or delivery item reference.

As a final step, the freight document can be confirmed for accrual postings. The system automatically posts the freight costs to financial accounting as accruals and creates a freight cost allocation document, a service purchase order and a service entry sheet. Financial postings are created depending on the business scenario to either expenses for an outbound process or to material accounts for an inbound process.

|  |
| --- |
| Note If the automatic freight cost confirmation and posting is activated as described in chapter Automate Confirmation and Posting of Freight Costs (Optional), the freight order is automatically confirmed for accrual posting. Alternatively, the Transportation Buyer can confirm selected freight orders for accrual posting manually as described below.If you performed Confirm Freight Cost for Accruals Postings in 6W3, you can skip this process and proceed with Monitor Freight Cost Allocation Documents.You only need to perform this process once for each freight document. |

Procedure

Table 19:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Transportation Buyer. | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Accrual Postings (F4329). | The Monitor Accruals Postings screen appears. |  |
| 3. | Enter Selection Criteria | On the Monitor Accrual Postings screen, make the following entry:Purchasing Organization: 3310Freight Document: Optionally <Enter your freight order or freight booking number>Note Example:For advanced intercompany sales or advanced intercompany stock transfer in case of an ocean freight booking, enter company code 1710.For advanced intercompany sales or advanced intercompany stock transfer in case of the freight order on-carriage, enter company code 3310.For all other scenarios, use company code 3310. |  |  |
| 4. | Choose Go | Choose Go. | The freight documents are displayed in the Monitor Accrual Postings table. |  |
| 5. | Navigate to the For Confirmation Tab | Navigate to the For Confirmation tab. | The freight documents for confirmation are displayed in the Monitor Accrual Postings table. |  |
| 6. | Freight Order / Freight Booking Details | Select the freight document row in the Monitor Accruals Posting table. | The Road Freight Order <your freight order number> - Process Accruals screen appears.orThe Rail Freight Order <your freight order number> - Process Accruals screen appears.orThe Ocean Freight Booking <your freight booking number> - Process Accruals screen appears.orThe Air Freight Booking <your freight booking number> - Process Accruals screen appears. |  |
| 7. | Display General Data (Optional) | Navigate to the General Data tab to review the header information. |  |  |
| 8. | Display Charges (Optional) | Scroll down to the Charges section to review the detailed information. | The charge item for the carrier or freight forwarder is displayed. |  |
| 9. | Display Charges (Optional) | In the Charge Hierarchy expand the node TM Carrier | The charge lines are displayed. |  |
| 10. | Display Charges Details (Optional) | Choose Show/Hide Details.Note Make sure that only one line is selected | The charge line details are displayed. |  |
| 11. | Display Stages (Optional) | Navigate to the Stages tab to review the stage details. |  |  |
| 12. | Display Business Partners (Optional) | Navigate to the Business Partner tab to review the parties involved. |  |  |
| 13. | Display Cost Distribution (Optional) | Navigate to the Cost Distribution tab to review the parties involved. | In the Distribution Hierarchy table it is shown how the freight costs are broken down by a sales order item or delivery item reference. |  |
| 14. | Confirm Freight Order or Confirm Freight Booking | Choose Confirm for Posting. | The following system message appears: Freight document <your freight order or freight booking> for <Your carrier or freight forwarder> confirmed for postingNote After confirming the freight order or freight booking for accruals posting, a service purchase order and a service entry sheet is created automatically in a background process. These documents are the basis for the invoice verification.Additionally, freight cost allocation documents (except for scope item BMY - Subcontracting purchase order with TM integration) are created as follows:Freight Cost Allocation (Expense) in all the legal ledgers for outbound transportation scenario (sell from stock, customer consignment fill-up/pickup, freight costs in the delivering company for ICO stock transport order and ICO intercompany sales process)Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario (procurement of material, inbound transport costs related to the ICO Stock transport order by the receiving company)If group valuation is activated, in case of ICO STO, the freight costs in the delivering company, Freight Cost Allocation (ML-Account), are posted in the group valuation ledger.For scope item BMY – Subcontracting purchase order with TM integration, freight cost allocation documents are created as follows:Freight Cost Allocation (ML-Account) in all the legal ledgers for outbound transportation scenario is only created when the goods receipt is performed for the inbound delivery of subcontracting purchase order. In case the confirming of freight document is done after goods receipt, the freight cost allocation (ML-Account) in all legal is created during confirming the freight document itself as done during usual freight cost confirming process.Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario.To see the details of the freight cost allocation document, follow the steps mentioned in the Monitor Freight Cost Allocation documents. |  |
| 15. | Navigate Back | Navigate back |  |  |

|  |
| --- |
| Note To confirm multiple freight documents simultaneously, choose multiple freight document checkboxes on the Monitor Accrual Postings overview page (under the For Confirmation tab) and choose Confirm for Posting. |

In case the posting result is an error, follow the steps below to check the error details and repost.

If, for example, the posting date is in a closed period, the posting date needs to be changed prior to posting of the freight document. You need to scroll down to the Charges section, navigate to the Posting Date tab, and change the accrual posting date in column Posting Date.

Table 20:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access App | Open Monitor Accrual Postings - Freight Documents (F4329). | The Monitor Accruals Postings screen appears. |  |
| 2 | Enter Selection Criteria | On the Monitor Accrual Postings screen, make the following entry:Purchasing Organization: 3310Freight Document: Optionally <Enter your freight order or freight booking number>Note Example:For advanced intercompany sales or advanced intercompany stock transfer in case of an ocean freight booking, enter company code 1710.For advanced intercompany sales or advanced intercompany stock transfer in case of the freight order on-carriage, enter company code 3310.For all other scenarios, use company code 3310. |  |  |
| 3 | Choose Go | Choose Go. | The freight documents are displayed in the Monitor Accrual Posting table. |  |
| 4 | Navigate to the Errors Tab | Navigate to the Errors tab | The freight documents with errors are displayed in the Monitor Accrual Postings table. |  |
| 5 | Show the Error Description | Navigate to the corresponding line and choose Show Errors. | The Application Log appears, containing a detailed description of the errors. |  |
| 6 | Show the Error Details | Select the error details by selecting the error link in the Description column. | The message details are shown containing a diagnosis and guidance on possible solutions. |  |
| 7 | Correct the Errors | Correct the errors according to the message details. |  |  |
| 8 | Select the Freight Order or Freight Booking in the Freight Document Table | Select the Freight Document checkbox. |  |  |
| 9 | Post Accruals | Choose Post. | The following system message appears: Freight document <your freight order or freight booking> for <Your carrier or freight forwarder> confirmed for postingNote After confirming the freight order or freight booking for accruals posting, a service purchase order and a service entry sheet is created automatically in a background process. These documents are the basis for the invoice verification.Additionally, freight cost allocation documents (except for scope item BMY - Subcontracting purchase order with TM integration) are created as follows:Freight Cost Allocation (Expense) in all the legal ledgers for outbound transportation scenario (sell from stock, customer consignment fill-up/pickup, freight costs in the delivering company for ICO stock transport order and ICO intercompany sales process)Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario (procurement of material, inbound transport costs related to the ICO Stock transport order by the receiving company)If group valuation is activated, in case of ICO STO, the freight costs in the delivering company, Freight Cost Allocation (ML-Account), are posted in the group valuation ledger.For scope item BMY – Subcontracting purchase order with TM integration, freight cost allocation documents are created as follows:Freight Cost Allocation (ML-Account) in all the legal ledgers for outbound transportation scenario is only created when the goods receipt is performed for the inbound delivery of subcontracting purchase order. In case the confirming of freight document is done after goods receipt the freight cost allocation (ML-Account) in all legal is created during confirming, the freight document itself as done during usual freight cost con-firming process.Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario.To see the details of the freight cost allocation document, follow the steps mentioned in the Monitor Freight Cost Allocation documents. |  |

##### Arrival of Airplane at Airport of Destination (Main Leg)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the airplane has arrived at the airport of destination, the Dispatcher (TM) sets the execution status to Set to Arrived at Final Airport of Destination.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Manage Air Freight Bookings (F6535). | The Manage Air Freight Bookings (F6535) screen appears. |  |
| 3. | Enter Air Freight Booking | On the Manage Air Freight Bookings screen, make the following entries:Air Freight Booking: <your air freight booking number> |  |  |
| 4. | Choose Go | Choose Go. | Air freight booking matching the selection criteria is listed. |  |
| 5. | Navigate to Air Freight Booking | Choose your air freight booking. | The Display Air Freight Booking screen appears. |  |
| 6. | Choose Edit | On the Display Air Freight Booking screen, choose Edit. | The Edit Air Freight Booking screen appears. |  |
| 7. | Choose Execution Status Set to Arrived at Final Airport of Destination | Choose Execution Status > Set to Arrived at Final Airport of Destination. | The Set to Arrived at Final Airport of Destination dialog box appears. |  |
| 8. | Enter Dates for Freight Booking | In the Set to Arrived at Final Airport of Destination dialog box, make the following entries:Arrival Date at Final Destination: <today’s date>Shipped-on Board Time: <time of day> |  |  |
| 9. | Chose OK | Chose OK. | The following system message appears:Arrival at stop AIRPORT_DXB was reported |  |
| 10. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

##### Departure of Truck at Airport of Destination (Delivery)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck is loaded and has left the airport of destination, the status of the freight order is set to Set to Departed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad opens. |  |
| 2. | Launch App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Order screen appears. |  |
| 3. | Enter Selection Criteria | On the Monitor Execution of Freight Order screen, make the following entries:Freight Order: <your freight order for delivery created in scope item 6W2 manual transportation planning> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Navigate to Freight Order | Choose <freight order number for delivery from previous step>. | The Display Road Freight Order for Delivery <freight order number for delivery from previous step> screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Delivery screen, choose Edit. | The Edit Road Freight Order for Delivery screen appears. |  |
| 7. | Choose Execution Status Set to Ready for Transportation Execution | Choose Execution Status > Set to Ready for Transportation Execution. | The following system messages appear:Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Delivery <freight order number for delivery from previous step> set to "Ready for Transportation Execution" |  |
| 8. | Scroll down to the Stages sub section | Scroll down to the Stages sub section. |  |  |
| 9. | Select Stage | In the Stages table, select the Stage 1. |  |  |
| 10. | Choose Execution Status (Source) Set to Departed | Choose Execution Status (Source) > Set to Departed. | The following system messages appear:Departure at stop AIRPORT_DXB and required preceding events were reported |  |
| 11. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

##### Set Truck Arrived and Checked In at Receiving Point Location (Delivery)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Set Truck Arrived and Checked In at Receiving Point Location (Delivery)

Procedure

After the truck has arrived at the destination location the Dispatcher (TM) sets the execution status to Set to Arrived and Set to Checked In.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order for delivery> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Delivery screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Delivery screen, choose Edit. | The Edit Road Freight Order for Delivery screen appears. |  |
| 7. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Choose Execution Status (Destination) Set to Arrived | Choose Execution Status (Destination ) > Set to Arrived . | The following system message appears: Arrival at stop SP_3310 was reported |  |
| 10. | Choose Execution Status (Destination) Set to Checked In | Choose Execution Status (Destination ) > Set to Checked In . | The following system message appears: Check-In at stop SP_3310 was reported |  |
| 11. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

|  |
| --- |
| Note You can revoke the arrival and check-in events by setting the status to Set to Not Arrived and Set to Not Checked In. |

##### Set Ready for Warehousing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck is unloaded, the Dispatcher (TM) sets the execution status to Set Ready for Warehouse Processing (Destination).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Air Freight Booking: <your Freight Order for Delivery> | The filter for the Monitor Execution of Freight Orders worklist is set. |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Edit Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Delivery screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Delivery screen, choose Edit. | The Edit Road Freight Order for Delivery screen appears. |  |
| 7. | Scroll to the Stages sub section. | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Choose Set Ready for Warehouse Processing (Destination) | Choose Warehouse Processing Status > Set to Ready for Warehouse Processing (Destination) . | The following system message appears:Warehouse processing status updated for Freight Unit <corresponding freight unit of freight order> |  |
| 10. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

##### Set Truck Checked Out and Departed at Receiving Point Location (Delivery)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck has left the receiving point location, the Dispatcher (TM) sets the execution status to Set to Checked Out and Set to Departed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders(F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order for delivery> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Delivery screen appears. |  |
| 6. | Choose Edit. | On the Display Road Freight Order for Delivery screen, choose Edit. | The Edit Road Freight Order for Delivery screen appears. |  |
| 7. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Choose Execution Status (Destination) Set to Checked Out | Choose Execution Status (Destination) > Set to Checked Out . | The following system message appears: Checkout at stop SP_3310 was reported |  |
| 10. | Choose Execution Status (Destination) Set to Departed | Choose Execution Status (Destination) > Set to Departed . | The following system message appears: Departure at stop SP_3310 was reported |  |
| 11. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfullyPlease continue with Succeeding Processes in the Appendix Process Integration. |  |

|  |
| --- |
| Note You can revoke the check-out and departed event by setting the status to Set to Not Checked Out and Set to Not Departed. |

### Advanced Intercompany Sales

#### Set Truck Arrived and Checked In at Shipping Point Location (Pick-Up)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The process for advanced intercompany sales provides functions that allow two affiliated companies to participate in a single intercompany process.

A sales organization assigned to the selling company creates a standard sales order and orders goods from a plant that is assigned to another company code that acts as the delivering company. To keep financial and material ledger postings in sync, a purchase order is created in the selling company that triggers the creation of an intercompany sales order in the delivering company. The delivering company delivers the goods to the customer. The delivering company invoices the selling company, and the selling company invoices the customer.

A standard sales order can initiate the entire process, which is integrated into value chain monitoring. For the transfer of control of goods between the affiliated companies and to the customer, the system uses valuated stock in transit.

After the truck has arrived at the shipping point, the Dispatcher (TM) sets the execution status to Set to Arrived and Set to Checked In in the freight order for pick-up.

In the freight order, the execution status is set to In Execution and the logistical execution status is set to Checked In in the shipping point. The status is also updated in the corresponding freight booking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order for pick up created in scope item 6W2 manual transportation planning> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Pick-Up screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Pick-Up screen, choose Edit. | The Edit Road Freight Order for Pick-Up screen appears. |  |
| 7. | Choose Execution Status Set to Ready for Transportation Execution | Choose Execution Status > Set to Ready for Transportation Execution. | The following system messages appear:Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Picl-Up <your freight order number> set to "Ready for Transportation Execution" |  |
| 8. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 9. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 10. | Choose Execution Status (Source) Set to Arrived | Choose Execution Status (Source) > Set to Arrived . | The following system message appears: Arrival at stop SP_1710 was reported |  |
| 11. | Choose Execution Status (Source) Set to Checked In | Choose Execution Status (Source) > Set to Checked In . | The following system message appears: Check-In at stop SP_1710 was reported |  |
| 12. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfullyCharge calculation completedCost distribution completed |  |

|  |
| --- |
| Note The following scope items are combined in one integrated process:5D2 - Advanced Intercompany Sales6W2 - Manual Transportation Planning3BS - Warehouse Outbound Processing6W3 - Transportation ExecutionEnsure that you perform the steps in chapter [Loading](#unique_12) [page ] 26 after you complete [Set Truck Arrived and Checked In at Shipping Point Location (Pick-Up)](#unique_138) [page ] 224 and before you start chapter [Set Truck Checked Out and Departed at Shipping Point Location (Pick-Up)](#unique_139) [page ] 226. |

#### Set Truck Checked Out and Departed at Shipping Point Location (Pick-Up)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once the truck is loaded, the Dispatcher (TM) sets the execution status in the freight order to Set to Checked Out. After the truck has left the shipping plant, the status is Set to Departed.

Besides the changes of the execution status and the logistical execution status in the freight order, the status is also updated in the corresponding freight booking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | Monitor Execution of Freight Orders (F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order number> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Pick-Up screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Pick-Up screen, choose Edit. | The Edit Road Freight Order for Pick-Up screen appears. |  |
| 7. | Scroll down to the Items sub section | Scroll down to the Items sub section. |  |  |
| 8. | In the Items table, select the line with the container by selecting the respective checkbox | In the Items table, select the line with the container by selecting the respective checkbox. |  |  |
| 9. | Navigate to the Quantities tab | Navigate to the Quantities tab. |  |  |
| 10. | Enter Verified Gross Mass | Under Verified Gross Mass make the following entries:Weight: <gross weight for container item + 100> KGWeighing Method: Weighing the Packed ContainerWeighing Date/Time: <today>Person Responsible for Weighing: <name of person responsible>Partner Function: ShipperWeighing Location: <enter your location of location type loading point> |  |  |
| 11. | Choose Save | Choose Save. | The following system message appears:Data saved successfully |  |
| 12. | Navigate to the Seals tab | Navigate to the Seals tab. |  |  |
| 13. | Enter Seals Information | Under Seals make the following entries:Seal Number: ANZ4711815Sealing Date: <today> |  |  |
| 14. | Choose Save | Choose Save. | The following system message appears:Data saved successfully |  |
| 15. | Print / Display a Preview of Shipment Documents (optional) | Navigate to the Output Request tab.In the output request table, choose Display of any print document in column display.Note The system creates the output requests for the respective print documents automatically after the freight order is saved.Printing is done when the check out event is reported, also automatically.Additional output requests can be created manually by choosing Insert. Enter the following data per table row:Output Type: <output type>Role: <carrier>Recipient: <carrier number>Form Country/Region: <source country>Form Language: <carrier language>Form Template: <form template>For triggering the printing of output requests manually, select it and choose Send Output. | The print document is opened as a PDF through the Adobe Document Service. |  |
| 16. | Navigate to General Data | Navigate to the General Data tab. |  |  |
| 17. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 18. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 19. | Choose Execution Status (Source) Set to Checked Out | Choose Execution Status (Source) > Set to Checked Out . | The following system message appears: Checkout at stop SP_1710 was reported |  |
| 20. | Choose Execution Status (Source) Set to Departed | Choose Execution Status (Source) > Set to Departed . | The following system message appears: Departure at stop SP_1710 was reported |  |
| 21. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

|  |
| --- |
| Note You can revoke the check-out and departed event by setting the status to Set to Not Checked Out and Set to Not Departed. |

#### Post Goods Issue

Purpose

This process step shows you how to post goods issues for the delivery. Execute this process step for all delivery documents.

Depending on the baseline scenario (BD9, 3NR, BMY, 1IU or 3BS) execute one of the following procedures.

Procedure

In case of BD9, BMY, 1IU, and 3NR, execute the following steps:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entries and choose Execute:Shipping Point: 3310Note In the case of Advanced Intercompany Sales or Advanced Intercompany Stock Transfer, the shipping point should be 1710. |  |  |
| 4 | Post Good Issue | Select your outbound delivery note, and choose Post Goods Issue.Select today’s date from the dialog box, and choose Continue. | A message confirms the goods issue has been posted.Advanced shipping notification has been automatically sent to the ship-to party via EDI based on the consignment order document.Note Open the consignment order from the Document Flow and navigate to Output Request or the Communication History tab to see the advanced shipping notification. |  |

In case of 3BS, execute the following steps:

|  |
| --- |
| Note If you triggered the goods movement posting in step Loading (Optional) of scope item Warehouse Outbound Processing (3BS), you can skip the Post Goods Issue step. |

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Delivery Orders (F6498) . | The Manage Outbound Delivery Orders (F6498) screen appears. |  |
| 3 | Enter Warehouse Number | Make the following entries:Warehouse No:3350 |  |  |
| 4 | Set Departure Date/Time | Make the following entries:Departure Date/Time: <Departure Date/Time Range> |  |  |
| 5 | Choose Go | Choose Go. | The Outbound Delivery Order screen appears. |  |
| 6 | WM: Post Good Issue | Select your outbound delivery order, and choose Post Goods Issue. | A message confirms the goods issue has been posted.The Warehouse Material Document has been created. |  |

#### Arrival of Truck at Port of Loading (Pick-up)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck has arrived at the port of loading, the Dispatcher (TM) sets the execution status to Set to Arrived.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Launch App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen is displayed. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order for pick up> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Pick-Up screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Pick-Up screen, choose Edit. | The Edit Road Freight Order for Pick-Up screen appears. |  |
| 7. | Scroll to the Stages Subsection | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages Table, Select the Stage Checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Choose Execution Status (Destination) Set to Arrived | Choose Execution Status (Destination) > Set to Arrived . | The following system message appears:Arrival at stop PORT_USLAX was reported |  |
| 10. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

#### Departure of Vessel from Port of Loading (Main Leg)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the vessel departed, the Dispatcher (TM) sets the execution status to Set to Shipped on Board.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Manage Ocean Freight Bookings (F6213). | The Manage Ocean Freight Bookings (F6213) screen is displayed. |  |
| 3. | Filter Ocean Freight Booking | On the Manage Ocean Freight Bookings screen, make the following entries:Ocean Freight Booking: <freight booking number created in scope item 6W2 step perform manual transportation planning> |  |  |
| 4. | Choose Go | On the Manage Ocean Freight Bookings screen, choose Go. | Ocean freight booking matching the selection criteria is listed. |  |
| 5. | Navigate to Ocean Freight Booking | In the Ocean Freight Bookings table, select one Ocean Freight Booking. | The Display Ocean Freight Booking screen appears. |  |
| 6. | Edit Ocean Freight Booking | On the Display Ocean Freight Booking screen, choose Edit. | The Edit Ocean Freight Booking screen appears. |  |
| 7. | Choose Execution Status Set to Loaded at Port of Loading | Choose Execution Status > Set to Loaded at Port of Loading. | The following system message appears:Loading End at stop PORT_USLAX was reported |  |
| 8. | Choose Execution Status Set to Shipped on Board | Choose Execution Status > Set to Shipped on Board . |  |  |
| 9. | Choose Ok | In the Set to Shipped on Board dialog box, choose OK | The following system message appears:Departure at stop PORT_USLAX was reported |  |
| 10. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

#### Display Internal Transfer of Control Date for Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the actual date for internal transfer of control. Based on the internal incoterm CIF used in this scenario, the transfer of control for the transport takes place after the execution status is Set to Loaded at Port of Loading in the process step before.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Fiori app Manage Outbound Deliveries (F0867A). | The Manage Outbound Deliveries screen displays. |  |
| 3 | Open Outbound Delivery Monitor | Choose List Outbound Deliveries.Make the following entries and choose Execute.Shipping Point/Receiving Pt: 1010 | List of Outbound Deliveries screen displays. |  |
| 4 | Change Outbound Deliveries | Mark the relevant delivery and choose Change Outbound Deliveries. | The Outbound Delivery <Outbound Delivery> Change: Overview screen displays. |  |
| 5 | Confirm Internal Transfer of Control Dates and Times | On the top menu, choose Menu > Goto > Header > Shipment . Check the fields Planned Dates and Time. Also check the fields Actual Date and Time at the screen block Internal Transfer of Control Dates.Note This field controls, when the goods movement is posted from Stock in Transit of the delivering company to the selling company. If the Planned Date and Time or the Actual Date and Time are earlier than the System Date and Time, the system posts the goods movement immediately when the goods issue is posted on the outbound delivery. If the Planned Date and Time or the Actual Date and Time are in the future, the system posts the goods movement one day later than this date and time. | The Internal Transfer of Control Dates are confirmed. |  |

#### Arrival of Vessel at Port of Discharge (Main Leg)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the vessel has arrived, the Dispatcher (TM) sets the execution status to Set to Arrived at Final Port of Discharge.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Launch App | Open Manage Ocean Freight Bookings (F6213). | The Manage Ocean Freight Bookings (F6213) screen is displayed. |  |
| 3. | Filter Ocean Freight Booking | On the Manage Ocean Freight Bookings screen, make the following entries:Ocean Freight Booking: <your freight booking number> |  |  |
| 4. | Choose Go | On the Manage Ocean Freight Bookings screen, choose Go. | Ocean freight booking matching the selection criteria is listed. |  |
| 5. | Navigate to Ocean Freight Booking | In the Ocean Freight Bookings table, select one Ocean Freight Booking. | The Display Ocean Freight Booking screen appears. |  |
| 6. | Edit Ocean Freight Booking | On the Display Ocean Freight Booking screen, choose Edit. | The Edit Ocean Freight Booking screen appears. |  |
| 7. | Choose Execution Status Set to Arrived at Final Port of Discharge | Choose Execution Status > Set to Arrived at Final Port of Discharge . |  |  |
| 8. | Choose OK | In the Set to arrived at final port of discharge dialog box, choose OK. | The following system message appears:Arrival at stop PORT_AESID was reported |  |
| 9. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

#### Confirm Freight Costs for Accrual Postings

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step the Transportation Buyer monitors the freight documents (freight orders or freight bookings) and posts accruals.

The Transportation Buyer reviews these freight documents prior to posting the freight cost accruals, to ensure that they correspond to the provided transportation services of the freight forwarder or carrier. This ensures a good data quality for the financial department.

The overall freight costs of the freight documents are allocated to the respective transportation requirements, for example sales order or delivery based on gross weight. On the Cost Distribution tab, it is shown how the freight costs are broken down by sales order item or delivery item reference.

As a final step, the freight document can be confirmed for accrual postings. The system automatically posts the freight costs to financial accounting as accruals and creates a freight cost allocation document, a service purchase order and a service entry sheet. Financial postings are created depending on the business scenario to either expenses for an outbound process or to material accounts for an inbound process.

|  |
| --- |
| Note If the automatic freight cost confirmation and posting is activated as described in chapter Automate Confirmation and Posting of Freight Costs (Optional), the freight order is automatically confirmed for accrual posting. Alternatively, the Transportation Buyer can confirm selected freight orders for accrual posting manually as described below.If you performed Confirm Freight Cost for Accruals Postings in 6W3, you can skip this process and proceed with Monitor Freight Cost Allocation Documents.You only need to perform this process once for each freight document. |

Procedure

Table 21:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Transportation Buyer. | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Accrual Postings (F4329). | The Monitor Accruals Postings screen appears. |  |
| 3. | Enter Selection Criteria | On the Monitor Accrual Postings screen, make the following entry:Purchasing Organization: 3310Freight Document: Optionally <Enter your freight order or freight booking number>Note Example:For advanced intercompany sales or advanced intercompany stock transfer in case of an ocean freight booking, enter company code 1710.For advanced intercompany sales or advanced intercompany stock transfer in case of the freight order on-carriage, enter company code 3310.For all other scenarios, use company code 3310. |  |  |
| 4. | Choose Go | Choose Go. | The freight documents are displayed in the Monitor Accrual Postings table. |  |
| 5. | Navigate to the For Confirmation Tab | Navigate to the For Confirmation tab. | The freight documents for confirmation are displayed in the Monitor Accrual Postings table. |  |
| 6. | Freight Order / Freight Booking Details | Select the freight document row in the Monitor Accruals Posting table. | The Road Freight Order <your freight order number> - Process Accruals screen appears.orThe Rail Freight Order <your freight order number> - Process Accruals screen appears.orThe Ocean Freight Booking <your freight booking number> - Process Accruals screen appears.orThe Air Freight Booking <your freight booking number> - Process Accruals screen appears. |  |
| 7. | Display General Data (Optional) | Navigate to the General Data tab to review the header information. |  |  |
| 8. | Display Charges (Optional) | Scroll down to the Charges section to review the detailed information. | The charge item for the carrier or freight forwarder is displayed. |  |
| 9. | Display Charges (Optional) | In the Charge Hierarchy expand the node TM Carrier | The charge lines are displayed. |  |
| 10. | Display Charges Details (Optional) | Choose Show/Hide Details.Note Make sure that only one line is selected | The charge line details are displayed. |  |
| 11. | Display Stages (Optional) | Navigate to the Stages tab to review the stage details. |  |  |
| 12. | Display Business Partners (Optional) | Navigate to the Business Partner tab to review the parties involved. |  |  |
| 13. | Display Cost Distribution (Optional) | Navigate to the Cost Distribution tab to review the parties involved. | In the Distribution Hierarchy table it is shown how the freight costs are broken down by a sales order item or delivery item reference. |  |
| 14. | Confirm Freight Order or Confirm Freight Booking | Choose Confirm for Posting. | The following system message appears: Freight document <your freight order or freight booking> for <Your carrier or freight forwarder> confirmed for postingNote After confirming the freight order or freight booking for accruals posting, a service purchase order and a service entry sheet is created automatically in a background process. These documents are the basis for the invoice verification.Additionally, freight cost allocation documents (except for scope item BMY - Subcontracting purchase order with TM integration) are created as follows:Freight Cost Allocation (Expense) in all the legal ledgers for outbound transportation scenario (sell from stock, customer consignment fill-up/pickup, freight costs in the delivering company for ICO stock transport order and ICO intercompany sales process)Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario (procurement of material, inbound transport costs related to the ICO Stock transport order by the receiving company)If group valuation is activated, in case of ICO STO, the freight costs in the delivering company, Freight Cost Allocation (ML-Account), are posted in the group valuation ledger.For scope item BMY – Subcontracting purchase order with TM integration, freight cost allocation documents are created as follows:Freight Cost Allocation (ML-Account) in all the legal ledgers for outbound transportation scenario is only created when the goods receipt is performed for the inbound delivery of subcontracting purchase order. In case the confirming of freight document is done after goods receipt, the freight cost allocation (ML-Account) in all legal is created during confirming the freight document itself as done during usual freight cost confirming process.Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario.To see the details of the freight cost allocation document, follow the steps mentioned in the Monitor Freight Cost Allocation documents. |  |
| 15. | Navigate Back | Navigate back |  |  |

|  |
| --- |
| Note To confirm multiple freight documents simultaneously, choose multiple freight document checkboxes on the Monitor Accrual Postings overview page (under the For Confirmation tab) and choose Confirm for Posting. |

In case the posting result is an error, follow the steps below to check the error details and repost.

If, for example, the posting date is in a closed period, the posting date needs to be changed prior to posting of the freight document. You need to scroll down to the Charges section, navigate to the Posting Date tab, and change the accrual posting date in column Posting Date.

Table 22:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access App | Open Monitor Accrual Postings - Freight Documents (F4329). | The Monitor Accruals Postings screen appears. |  |
| 2 | Enter Selection Criteria | On the Monitor Accrual Postings screen, make the following entry:Purchasing Organization: 3310Freight Document: Optionally <Enter your freight order or freight booking number>Note Example:For advanced intercompany sales or advanced intercompany stock transfer in case of an ocean freight booking, enter company code 1710.For advanced intercompany sales or advanced intercompany stock transfer in case of the freight order on-carriage, enter company code 3310.For all other scenarios, use company code 3310. |  |  |
| 3 | Choose Go | Choose Go. | The freight documents are displayed in the Monitor Accrual Posting table. |  |
| 4 | Navigate to the Errors Tab | Navigate to the Errors tab | The freight documents with errors are displayed in the Monitor Accrual Postings table. |  |
| 5 | Show the Error Description | Navigate to the corresponding line and choose Show Errors. | The Application Log appears, containing a detailed description of the errors. |  |
| 6 | Show the Error Details | Select the error details by selecting the error link in the Description column. | The message details are shown containing a diagnosis and guidance on possible solutions. |  |
| 7 | Correct the Errors | Correct the errors according to the message details. |  |  |
| 8 | Select the Freight Order or Freight Booking in the Freight Document Table | Select the Freight Document checkbox. |  |  |
| 9 | Post Accruals | Choose Post. | The following system message appears: Freight document <your freight order or freight booking> for <Your carrier or freight forwarder> confirmed for postingNote After confirming the freight order or freight booking for accruals posting, a service purchase order and a service entry sheet is created automatically in a background process. These documents are the basis for the invoice verification.Additionally, freight cost allocation documents (except for scope item BMY - Subcontracting purchase order with TM integration) are created as follows:Freight Cost Allocation (Expense) in all the legal ledgers for outbound transportation scenario (sell from stock, customer consignment fill-up/pickup, freight costs in the delivering company for ICO stock transport order and ICO intercompany sales process)Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario (procurement of material, inbound transport costs related to the ICO Stock transport order by the receiving company)If group valuation is activated, in case of ICO STO, the freight costs in the delivering company, Freight Cost Allocation (ML-Account), are posted in the group valuation ledger.For scope item BMY – Subcontracting purchase order with TM integration, freight cost allocation documents are created as follows:Freight Cost Allocation (ML-Account) in all the legal ledgers for outbound transportation scenario is only created when the goods receipt is performed for the inbound delivery of subcontracting purchase order. In case the confirming of freight document is done after goods receipt the freight cost allocation (ML-Account) in all legal is created during confirming, the freight document itself as done during usual freight cost con-firming process.Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario.To see the details of the freight cost allocation document, follow the steps mentioned in the Monitor Freight Cost Allocation documents. |  |

#### Departure of Truck at Port of Discharge (On-Carriage)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck is loaded and has left the port of discharge, the status of the freight order is set to Set to Departed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2 | Launch App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders worklist is displayed. |  |
| 3 | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your road freight order number for on-carriage> |  |  |
| 4 | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5 | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order screen appears. |  |
| 6 | Choose Edit | Choose Edit. | The Edit Road Freight Order screen appears |  |
| 7 | Set Execution Status | Choose Execution Status > Set to Ready for Transportation Execution. | The following system messages appear:Ready for execution check completed without errorsExecution status of doc. Road Freight Order <your freight order number> set to "Ready for Transportation Execution" |  |
| 8 | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 9 | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 10 | Choose Execution Status (Source) Set to Departed | Choose Execution Status (Source) > Set to Departed . | The following system message appears:Departure at stop PORT_AESID was reported |  |
| 11 | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

#### Confirm Freight Costs for Accrual Postings

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step the Transportation Buyer monitors the freight documents (freight orders or freight bookings) and posts accruals.

The Transportation Buyer reviews these freight documents prior to posting the freight cost accruals, to ensure that they correspond to the provided transportation services of the freight forwarder or carrier. This ensures a good data quality for the financial department.

The overall freight costs of the freight documents are allocated to the respective transportation requirements, for example sales order or delivery based on gross weight. On the Cost Distribution tab, it is shown how the freight costs are broken down by sales order item or delivery item reference.

As a final step, the freight document can be confirmed for accrual postings. The system automatically posts the freight costs to financial accounting as accruals and creates a freight cost allocation document, a service purchase order and a service entry sheet. Financial postings are created depending on the business scenario to either expenses for an outbound process or to material accounts for an inbound process.

|  |
| --- |
| Note If the automatic freight cost confirmation and posting is activated as described in chapter Automate Confirmation and Posting of Freight Costs (Optional), the freight order is automatically confirmed for accrual posting. Alternatively, the Transportation Buyer can confirm selected freight orders for accrual posting manually as described below.If you performed Confirm Freight Cost for Accruals Postings in 6W3, you can skip this process and proceed with Monitor Freight Cost Allocation Documents.You only need to perform this process once for each freight document. |

Procedure

Table 23:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Transportation Buyer. | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Accrual Postings (F4329). | The Monitor Accruals Postings screen appears. |  |
| 3. | Enter Selection Criteria | On the Monitor Accrual Postings screen, make the following entry:Purchasing Organization: 3310Freight Document: Optionally <Enter your freight order or freight booking number>Note Example:For advanced intercompany sales or advanced intercompany stock transfer in case of an ocean freight booking, enter company code 1710.For advanced intercompany sales or advanced intercompany stock transfer in case of the freight order on-carriage, enter company code 3310.For all other scenarios, use company code 3310. |  |  |
| 4. | Choose Go | Choose Go. | The freight documents are displayed in the Monitor Accrual Postings table. |  |
| 5. | Navigate to the For Confirmation Tab | Navigate to the For Confirmation tab. | The freight documents for confirmation are displayed in the Monitor Accrual Postings table. |  |
| 6. | Freight Order / Freight Booking Details | Select the freight document row in the Monitor Accruals Posting table. | The Road Freight Order <your freight order number> - Process Accruals screen appears.orThe Rail Freight Order <your freight order number> - Process Accruals screen appears.orThe Ocean Freight Booking <your freight booking number> - Process Accruals screen appears.orThe Air Freight Booking <your freight booking number> - Process Accruals screen appears. |  |
| 7. | Display General Data (Optional) | Navigate to the General Data tab to review the header information. |  |  |
| 8. | Display Charges (Optional) | Scroll down to the Charges section to review the detailed information. | The charge item for the carrier or freight forwarder is displayed. |  |
| 9. | Display Charges (Optional) | In the Charge Hierarchy expand the node TM Carrier | The charge lines are displayed. |  |
| 10. | Display Charges Details (Optional) | Choose Show/Hide Details.Note Make sure that only one line is selected | The charge line details are displayed. |  |
| 11. | Display Stages (Optional) | Navigate to the Stages tab to review the stage details. |  |  |
| 12. | Display Business Partners (Optional) | Navigate to the Business Partner tab to review the parties involved. |  |  |
| 13. | Display Cost Distribution (Optional) | Navigate to the Cost Distribution tab to review the parties involved. | In the Distribution Hierarchy table it is shown how the freight costs are broken down by a sales order item or delivery item reference. |  |
| 14. | Confirm Freight Order or Confirm Freight Booking | Choose Confirm for Posting. | The following system message appears: Freight document <your freight order or freight booking> for <Your carrier or freight forwarder> confirmed for postingNote After confirming the freight order or freight booking for accruals posting, a service purchase order and a service entry sheet is created automatically in a background process. These documents are the basis for the invoice verification.Additionally, freight cost allocation documents (except for scope item BMY - Subcontracting purchase order with TM integration) are created as follows:Freight Cost Allocation (Expense) in all the legal ledgers for outbound transportation scenario (sell from stock, customer consignment fill-up/pickup, freight costs in the delivering company for ICO stock transport order and ICO intercompany sales process)Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario (procurement of material, inbound transport costs related to the ICO Stock transport order by the receiving company)If group valuation is activated, in case of ICO STO, the freight costs in the delivering company, Freight Cost Allocation (ML-Account), are posted in the group valuation ledger.For scope item BMY – Subcontracting purchase order with TM integration, freight cost allocation documents are created as follows:Freight Cost Allocation (ML-Account) in all the legal ledgers for outbound transportation scenario is only created when the goods receipt is performed for the inbound delivery of subcontracting purchase order. In case the confirming of freight document is done after goods receipt, the freight cost allocation (ML-Account) in all legal is created during confirming the freight document itself as done during usual freight cost confirming process.Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario.To see the details of the freight cost allocation document, follow the steps mentioned in the Monitor Freight Cost Allocation documents. |  |
| 15. | Navigate Back | Navigate back |  |  |

|  |
| --- |
| Note To confirm multiple freight documents simultaneously, choose multiple freight document checkboxes on the Monitor Accrual Postings overview page (under the For Confirmation tab) and choose Confirm for Posting. |

In case the posting result is an error, follow the steps below to check the error details and repost.

If, for example, the posting date is in a closed period, the posting date needs to be changed prior to posting of the freight document. You need to scroll down to the Charges section, navigate to the Posting Date tab, and change the accrual posting date in column Posting Date.

Table 24:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access App | Open Monitor Accrual Postings - Freight Documents (F4329). | The Monitor Accruals Postings screen appears. |  |
| 2 | Enter Selection Criteria | On the Monitor Accrual Postings screen, make the following entry:Purchasing Organization: 3310Freight Document: Optionally <Enter your freight order or freight booking number>Note Example:For advanced intercompany sales or advanced intercompany stock transfer in case of an ocean freight booking, enter company code 1710.For advanced intercompany sales or advanced intercompany stock transfer in case of the freight order on-carriage, enter company code 3310.For all other scenarios, use company code 3310. |  |  |
| 3 | Choose Go | Choose Go. | The freight documents are displayed in the Monitor Accrual Posting table. |  |
| 4 | Navigate to the Errors Tab | Navigate to the Errors tab | The freight documents with errors are displayed in the Monitor Accrual Postings table. |  |
| 5 | Show the Error Description | Navigate to the corresponding line and choose Show Errors. | The Application Log appears, containing a detailed description of the errors. |  |
| 6 | Show the Error Details | Select the error details by selecting the error link in the Description column. | The message details are shown containing a diagnosis and guidance on possible solutions. |  |
| 7 | Correct the Errors | Correct the errors according to the message details. |  |  |
| 8 | Select the Freight Order or Freight Booking in the Freight Document Table | Select the Freight Document checkbox. |  |  |
| 9 | Post Accruals | Choose Post. | The following system message appears: Freight document <your freight order or freight booking> for <Your carrier or freight forwarder> confirmed for postingNote After confirming the freight order or freight booking for accruals posting, a service purchase order and a service entry sheet is created automatically in a background process. These documents are the basis for the invoice verification.Additionally, freight cost allocation documents (except for scope item BMY - Subcontracting purchase order with TM integration) are created as follows:Freight Cost Allocation (Expense) in all the legal ledgers for outbound transportation scenario (sell from stock, customer consignment fill-up/pickup, freight costs in the delivering company for ICO stock transport order and ICO intercompany sales process)Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario (procurement of material, inbound transport costs related to the ICO Stock transport order by the receiving company)If group valuation is activated, in case of ICO STO, the freight costs in the delivering company, Freight Cost Allocation (ML-Account), are posted in the group valuation ledger.For scope item BMY – Subcontracting purchase order with TM integration, freight cost allocation documents are created as follows:Freight Cost Allocation (ML-Account) in all the legal ledgers for outbound transportation scenario is only created when the goods receipt is performed for the inbound delivery of subcontracting purchase order. In case the confirming of freight document is done after goods receipt the freight cost allocation (ML-Account) in all legal is created during confirming, the freight document itself as done during usual freight cost con-firming process.Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario.To see the details of the freight cost allocation document, follow the steps mentioned in the Monitor Freight Cost Allocation documents. |  |

#### Set Truck Arrived at Customer Location (On-Carriage)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck has arrived at the customer location, the Dispatcher (TM) sets the execution status to Set to Arrived.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori Launchpad opens. |  |
| 2. | Launch App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Order screen appears. |  |
| 3. | Enter Selection Criteria | On the Monitor Execution of Freight Order screen, make the following entries:Freight Order: <your road freight order number for on-carriage> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order screen appears. |  |
| 6. | Edit Freight Order | On the Display Road Freight Order screen, choose Edit. | The Edit Road Freight Order screen appears. |  |
| 7. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Choose Execution Status (Destination) Set to Arrived | Choose Execution Status (Destination) > Set to Arrived . | The following system message appears: Arrival at stop 33186005 and required preceding events were reported |  |
| 10. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

#### Display External Transfer of Control Date for Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the actual date for external transfer of control. Based on the external incoterm DDP used in this scenario, the transfer of control for the transport takes place after the cargo has arrived at the customer location.

The actual date for external transfer of control is automatically set with the arrival of the truck at customer location (performed in previous process step).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries screen displays. |  |
| 3 | Open Outbound Delivery Monitor | Choose List Outbound Deliveries.Make the following entries and choose Execute.Shipping Point/Receiving Pt: 1010 | List of Outbound Deliveries screen displays. |  |
| 4 | Change Outbound Deliveries | Mark the relevant delivery and choose Change Outbound Deliveries. | Outbound Delivery <Outbound Delivery> Change: Overview screen displays. |  |
| 5 | Confirm External Transfer of Control Dates | On the top menu, choose Menu > Goto > Header > Shipment , check the field Planned Dates and Time. Also check the Actual Date and Time at the screen block External Transfer of Control Dates.Note This field controls when the goods movement is posted from Stock in Transit of the selling company to customer. If the Planned Date and Time or Actual Planned Date and Time is earlier than the System Date and Time, the system posts the goods movement immediately, when the goods issue is posted on the outbound delivery. If the Planned Date and Time or Actual Planned Date and Time is in the future, system posts the goods movement one day later than this date and time. | External Transfer of Control Dates are confirmed.Please continue with Succeeding Processes in the Appendix Process Integration. |  |

### Advanced Intercompany Stock Transfer

#### Set Truck Arrived and Checked In at Shipping Point Location (Pick-Up)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A purchasing organization assigned to the receiving company code creates an intercompany purchase order and orders goods from a plant assigned to another company code.

The plant in the delivering company code delivers the goods to the plant for which the purchasing organization ordered the goods.

The delivering company must bill the receiving company for the goods, because the two companies codes balance their accounts independently and have to fulfill legal requirements. This internal billing transaction is carried out by means of an intercompany billing document, that is, an intercompany customer invoice. Based on the intercompany customer invoice, the system automatically posts an intercompany supplier invoice.

After the truck has arrived at the shipping point, the Dispatcher (TM) sets the execution status to Set to Arrived and Set to Checked In in the freight order for pick-up.

In the freight order, the execution status is Set to In Execution and the logistical execution status is set to Set to Checked In in the shipping point. The status is also updated in the corresponding freight booking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order for pick up created in scope item 6W2 manual transportation planning> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Pick-Up screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Orderfor Pick-Up screen, choose Edit. | The Edit Road Freight Order for Pick-Up screen appears. |  |
| 7. | Choose Execution Status Set to Ready for Transportation Execution | Choose Execution Status > Set to Ready for Transportation Execution. | The following system messages appear:Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Pick-Up <your freight order number> set to "Ready for Transportation Execution" |  |
| 8. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 9. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 10. | Choose Execution Status (Source) Set to Arrived | Choose Execution Status (Source) > Set to Arrived . | The following system message appears: Arrival at stop SP_1710 was reported |  |
| 11. | Choose Execution Status (Source) Set to Checked In | Choose Execution Status (Source) > Set to Checked In . | The following system message appears: Check-In at stop SP_1710 was reported |  |
| 12. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfullyCharge calculation completedCost distribution completed |  |

|  |
| --- |
| Note You can revoke the arrival and check-in events by setting the status to Set to Not Arrived and Set to Not Checked In. |

#### Set Truck Checked Out and Departed at Shipping Point Location (Pick-Up)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once the truck is loaded, the Dispatcher (TM) sets the execution status in the freight order to Set to Checked Out. After the truck has left the shipping plant, the status is Set to Departed.

Besides the changes of the execution status and the logistical execution status in the freight order, the status is also updated in the corresponding freight booking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders(F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order for pick up> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Pick-Up screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Pick-Up screen, choose Edit. | The Edit Road Freight Order for Pick-Up screen appears. |  |
| 7. | Scroll down to the Items sub section | Scroll down to the Items sub section. |  |  |
| 8. | Enter Verified Gross Mass | In the Items table, select the line with the container by selecting the respective checkbox. |  |  |
| 9. | Navigate to the Quantities tab | Navigate to the Quantities tab. |  |  |
| 10. | Enter Verified Gross Mass | Under Verified Gross Mass make the following entries:Weight: <gross weight for container item + 100> KGWeighing Method: Weighing the Packed ContainerWeighing Date/Time: <today>Person Responsible for Weighing: <name of person responsible>Partner Function: ShipperWeighing Location: <enter your location of location type loading point> |  |  |
| 11. | Choose Save | Choose Save. | The following system message appears:Data saved successfully |  |
| 12. | Navigate to the Seals tab | Navigate to the Seals tab. |  |  |
| 13. | Enter Seals Information | Under Seals make the following entries:Seal Number: ANZ4711815Sealing Date: <today> |  |  |
| 14. | Choose Save | Choose Save. | The following system message appears:Data saved successfully |  |
| 15. | Print / Display a preview of Shipment Documents (optional) | Navigate to the Output Request tab.In the output request table, choose Display of any print document in column display.Note The system creates the output requests for the respective print documents automatically after the freight order is saved.Printing is done when the checkout event is reported, also automatically.Additional output requests can be created manually by choosing Insert. Enter the following data per table row:Output Type: <output type>Role: <carrier>Recipient: <carrier number>Form Country/Region: <source country>Form Language: <carrier language>Form Template: <form template>For triggering the printing of output requests manually, select it and choose Send Output. | The print document is opened as a PDF through the Adobe Document Service. |  |
| 16. | Scroll to the Stages sub section. | Scroll to the Stages sub section. |  |  |
| 17. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 18. | Choose Execution Status (Source) Set to Checked Out | Choose Execution Status (Source) > Set to Checked Out . | The following system message appears: Checkout at stop SP_1710 was reported |  |
| 19. | Choose Execution Status (Source) Set to Departed | Choose Execution Status (Source) > Set to Departed . | The following system message appears: Departure at stop SP_1710 was reported |  |
| 20. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

|  |
| --- |
| Note You can revoke the checkout and departed event by setting the status to Set to Not Checked Out and Set to Not Departed. |

#### Post Goods Issue

Purpose

This process step shows you how to post goods issues for the delivery. Execute this process step for all delivery documents.

Depending on the baseline scenario (BD9, 3NR, BMY, 1IU or 3BS) execute one of the following procedures.

Procedure

In case of BD9, BMY, 1IU, and 3NR, execute the following steps:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entries and choose Execute:Shipping Point: 3310Note In the case of Advanced Intercompany Sales or Advanced Intercompany Stock Transfer, the shipping point should be 1710. |  |  |
| 4 | Post Good Issue | Select your outbound delivery note, and choose Post Goods Issue.Select today’s date from the dialog box, and choose Continue. | A message confirms the goods issue has been posted.Advanced shipping notification has been automatically sent to the ship-to party via EDI based on the consignment order document.Note Open the consignment order from the Document Flow and navigate to Output Request or the Communication History tab to see the advanced shipping notification. |  |

In case of 3BS, execute the following steps:

|  |
| --- |
| Note If you triggered the goods movement posting in step Loading (Optional) of scope item Warehouse Outbound Processing (3BS), you can skip the Post Goods Issue step. |

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Delivery Orders (F6498) . | The Manage Outbound Delivery Orders (F6498) screen appears. |  |
| 3 | Enter Warehouse Number | Make the following entries:Warehouse No:3350 |  |  |
| 4 | Set Departure Date/Time | Make the following entries:Departure Date/Time: <Departure Date/Time Range> |  |  |
| 5 | Choose Go | Choose Go. | The Outbound Delivery Order screen appears. |  |
| 6 | WM: Post Good Issue | Select your outbound delivery order, and choose Post Goods Issue. | A message confirms the goods issue has been posted.The Warehouse Material Document has been created. |  |

#### Arrival of Truck at Port of Loading (Pick-Up)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck has arrived at the port of loading, the Dispatcher (TM) sets the execution status to Set to Arrived.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order for pick up> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Pick-Up screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Pick-Up screen, choose Edit. | The Edit Road Freight Order for Pick-Up screen appears. |  |
| 7. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Choose Execution Status (Destination) Set to Arrived | Choose Execution Status (Destination) > Set to Arrived . | The following system message appears:Arrival at stop PORT_USLAX was reported |  |
| 10. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

#### Departure of Vessel from Port of Loading (Main Leg)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the vessel has departed, the Dispatcher (TM) sets the execution status to Set to Shipped on Board.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Manage Ocean Freight Bookings (F6213). | The Manage Ocean Freight Bookings (F6213) screen is displayed. |  |
| 3. | Filter Ocean Freight Booking | On the Manage Ocean Freight Bookings screen, make the following entries:Ocean Freight Booking: <freight booking number created in scope item 6W2 step perform manual transportation planning> |  |  |
| 4. | Choose Go | On the Manage Ocean Freight Bookings screen, choose Go. | Ocean freight booking matching the selection criteria is listed. |  |
| 5. | Navigate to Ocean Freight Booking | In the Ocean Freight Bookings table, select one Ocean Freight Booking. | The Display Ocean Freight Booking screen appears. |  |
| 6. | Edit Ocean Freight Booking | On the Display Ocean Freight Booking screen, choose Edit. | The Edit Ocean Freight Booking screen appears. |  |
| 7. | Choose Execution Status Set to Loaded at Port of Loading | Choose Execution Status > Set to Loaded at Port of Loading. | The following system message appears:Loading End at stop PORT_USLAX was reported |  |
| 8. | Choose Execution Status Set to Shipped on Board | Choose Execution Status > Set to Shipped on Board . |  |  |
| 9. | Choose OK | In the Set to Shipped on Board dialog box, choose OK | The following system message appears:Departure at stop PORT_USLAX was reported |  |
| 10. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

#### Display Internal Transfer of Control Date for Goods in Transit (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the actual date for internal transfer of control for goods in transit. Based on the internal incoterm CIF used in this scenario, the transfer of control for the transport takes place after shipped on board (after loading the vessel).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The Fiori launch Pad displays. |  |
| 2 | Access the App | Open the Fiori app Display Outbound Delivery (VL03N). | The Display Outbound Delivery (VL03N) screen appears. |  |
| 3 | Change Outbound Deliveries | On the Display Outbound Delivery screen, enter the delivery document number from the earlier section and choose Continue. | The Replen.Adv.CC STO XXXXXXXX: Display Overview screen displays. |  |
| 4 | Confirm Internal Transfer of Control Dates and Times | On the top menu, choose Menu > Goto > Header > Shipment and check the fields Planned Dates and Time . Also check the Actual Date and Time at the screen block Internal Transfer of Control Dates.Note This field controls, when the goods movement is posted from Stock in Transit of the delivering company to the ordering company. If the Planned Date and Time or the Actual Planned Date and Time are earlier than the System Date and Time, the system posts the goods movement immediately when the the goods issue is posted on the outbound delivery. If the Planned Date and Time or the Actual Planned Date and Time are in the future, the system posts the goods movement it reaches on that date and time. | The internal transfer of control dates are confirmed. |  |

#### Confirm Freight Costs for Accrual Postings

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step the Transportation Buyer monitors the freight documents (freight orders or freight bookings) and posts accruals.

The Transportation Buyer reviews these freight documents prior to posting the freight cost accruals, to ensure that they correspond to the provided transportation services of the freight forwarder or carrier. This ensures a good data quality for the financial department.

The overall freight costs of the freight documents are allocated to the respective transportation requirements, for example sales order or delivery based on gross weight. On the Cost Distribution tab, it is shown how the freight costs are broken down by sales order item or delivery item reference.

As a final step, the freight document can be confirmed for accrual postings. The system automatically posts the freight costs to financial accounting as accruals and creates a freight cost allocation document, a service purchase order and a service entry sheet. Financial postings are created depending on the business scenario to either expenses for an outbound process or to material accounts for an inbound process.

|  |
| --- |
| Note If the automatic freight cost confirmation and posting is activated as described in chapter Automate Confirmation and Posting of Freight Costs (Optional), the freight order is automatically confirmed for accrual posting. Alternatively, the Transportation Buyer can confirm selected freight orders for accrual posting manually as described below.If you performed Confirm Freight Cost for Accruals Postings in 6W3, you can skip this process and proceed with Monitor Freight Cost Allocation Documents.You only need to perform this process once for each freight document. |

Procedure

Table 25:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Transportation Buyer. | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Accrual Postings (F4329). | The Monitor Accruals Postings screen appears. |  |
| 3. | Enter Selection Criteria | On the Monitor Accrual Postings screen, make the following entry:Purchasing Organization: 3310Freight Document: Optionally <Enter your freight order or freight booking number>Note Example:For advanced intercompany sales or advanced intercompany stock transfer in case of an ocean freight booking, enter company code 1710.For advanced intercompany sales or advanced intercompany stock transfer in case of the freight order on-carriage, enter company code 3310.For all other scenarios, use company code 3310. |  |  |
| 4. | Choose Go | Choose Go. | The freight documents are displayed in the Monitor Accrual Postings table. |  |
| 5. | Navigate to the For Confirmation Tab | Navigate to the For Confirmation tab. | The freight documents for confirmation are displayed in the Monitor Accrual Postings table. |  |
| 6. | Freight Order / Freight Booking Details | Select the freight document row in the Monitor Accruals Posting table. | The Road Freight Order <your freight order number> - Process Accruals screen appears.orThe Rail Freight Order <your freight order number> - Process Accruals screen appears.orThe Ocean Freight Booking <your freight booking number> - Process Accruals screen appears.orThe Air Freight Booking <your freight booking number> - Process Accruals screen appears. |  |
| 7. | Display General Data (Optional) | Navigate to the General Data tab to review the header information. |  |  |
| 8. | Display Charges (Optional) | Scroll down to the Charges section to review the detailed information. | The charge item for the carrier or freight forwarder is displayed. |  |
| 9. | Display Charges (Optional) | In the Charge Hierarchy expand the node TM Carrier | The charge lines are displayed. |  |
| 10. | Display Charges Details (Optional) | Choose Show/Hide Details.Note Make sure that only one line is selected | The charge line details are displayed. |  |
| 11. | Display Stages (Optional) | Navigate to the Stages tab to review the stage details. |  |  |
| 12. | Display Business Partners (Optional) | Navigate to the Business Partner tab to review the parties involved. |  |  |
| 13. | Display Cost Distribution (Optional) | Navigate to the Cost Distribution tab to review the parties involved. | In the Distribution Hierarchy table it is shown how the freight costs are broken down by a sales order item or delivery item reference. |  |
| 14. | Confirm Freight Order or Confirm Freight Booking | Choose Confirm for Posting. | The following system message appears: Freight document <your freight order or freight booking> for <Your carrier or freight forwarder> confirmed for postingNote After confirming the freight order or freight booking for accruals posting, a service purchase order and a service entry sheet is created automatically in a background process. These documents are the basis for the invoice verification.Additionally, freight cost allocation documents (except for scope item BMY - Subcontracting purchase order with TM integration) are created as follows:Freight Cost Allocation (Expense) in all the legal ledgers for outbound transportation scenario (sell from stock, customer consignment fill-up/pickup, freight costs in the delivering company for ICO stock transport order and ICO intercompany sales process)Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario (procurement of material, inbound transport costs related to the ICO Stock transport order by the receiving company)If group valuation is activated, in case of ICO STO, the freight costs in the delivering company, Freight Cost Allocation (ML-Account), are posted in the group valuation ledger.For scope item BMY – Subcontracting purchase order with TM integration, freight cost allocation documents are created as follows:Freight Cost Allocation (ML-Account) in all the legal ledgers for outbound transportation scenario is only created when the goods receipt is performed for the inbound delivery of subcontracting purchase order. In case the confirming of freight document is done after goods receipt, the freight cost allocation (ML-Account) in all legal is created during confirming the freight document itself as done during usual freight cost confirming process.Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario.To see the details of the freight cost allocation document, follow the steps mentioned in the Monitor Freight Cost Allocation documents. |  |
| 15. | Navigate Back | Navigate back |  |  |

|  |
| --- |
| Note To confirm multiple freight documents simultaneously, choose multiple freight document checkboxes on the Monitor Accrual Postings overview page (under the For Confirmation tab) and choose Confirm for Posting. |

In case the posting result is an error, follow the steps below to check the error details and repost.

If, for example, the posting date is in a closed period, the posting date needs to be changed prior to posting of the freight document. You need to scroll down to the Charges section, navigate to the Posting Date tab, and change the accrual posting date in column Posting Date.

Table 26:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access App | Open Monitor Accrual Postings - Freight Documents (F4329). | The Monitor Accruals Postings screen appears. |  |
| 2 | Enter Selection Criteria | On the Monitor Accrual Postings screen, make the following entry:Purchasing Organization: 3310Freight Document: Optionally <Enter your freight order or freight booking number>Note Example:For advanced intercompany sales or advanced intercompany stock transfer in case of an ocean freight booking, enter company code 1710.For advanced intercompany sales or advanced intercompany stock transfer in case of the freight order on-carriage, enter company code 3310.For all other scenarios, use company code 3310. |  |  |
| 3 | Choose Go | Choose Go. | The freight documents are displayed in the Monitor Accrual Posting table. |  |
| 4 | Navigate to the Errors Tab | Navigate to the Errors tab | The freight documents with errors are displayed in the Monitor Accrual Postings table. |  |
| 5 | Show the Error Description | Navigate to the corresponding line and choose Show Errors. | The Application Log appears, containing a detailed description of the errors. |  |
| 6 | Show the Error Details | Select the error details by selecting the error link in the Description column. | The message details are shown containing a diagnosis and guidance on possible solutions. |  |
| 7 | Correct the Errors | Correct the errors according to the message details. |  |  |
| 8 | Select the Freight Order or Freight Booking in the Freight Document Table | Select the Freight Document checkbox. |  |  |
| 9 | Post Accruals | Choose Post. | The following system message appears: Freight document <your freight order or freight booking> for <Your carrier or freight forwarder> confirmed for postingNote After confirming the freight order or freight booking for accruals posting, a service purchase order and a service entry sheet is created automatically in a background process. These documents are the basis for the invoice verification.Additionally, freight cost allocation documents (except for scope item BMY - Subcontracting purchase order with TM integration) are created as follows:Freight Cost Allocation (Expense) in all the legal ledgers for outbound transportation scenario (sell from stock, customer consignment fill-up/pickup, freight costs in the delivering company for ICO stock transport order and ICO intercompany sales process)Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario (procurement of material, inbound transport costs related to the ICO Stock transport order by the receiving company)If group valuation is activated, in case of ICO STO, the freight costs in the delivering company, Freight Cost Allocation (ML-Account), are posted in the group valuation ledger.For scope item BMY – Subcontracting purchase order with TM integration, freight cost allocation documents are created as follows:Freight Cost Allocation (ML-Account) in all the legal ledgers for outbound transportation scenario is only created when the goods receipt is performed for the inbound delivery of subcontracting purchase order. In case the confirming of freight document is done after goods receipt the freight cost allocation (ML-Account) in all legal is created during confirming, the freight document itself as done during usual freight cost con-firming process.Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario.To see the details of the freight cost allocation document, follow the steps mentioned in the Monitor Freight Cost Allocation documents. |  |

#### Arrival of Vessel at Port of Discharge (Main Leg)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the vessel has arrived, the Dispatcher (TM) sets the execution status to Set to Arrived at Final Port of Discharge.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Launch App | Open Manage Ocean Freight Bookings (F6213). | The Manage Ocean Freight Bookings (F6213) screen is displayed. |  |
| 3. | Filter Ocean Freight Booking | On the Manage Ocean Freight Bookings screen, make the following entries:Ocean Freight Booking: <your freight booking number> |  |  |
| 4. | Choose Go | On the Manage Ocean Freight Bookings screen, choose Go. | Ocean freight booking matching the selection criteria is listed. |  |
| 5. | Navigate to Ocean Freight Booking | In the Ocean Freight Bookings table, select one Ocean Freight Booking. | The Display Ocean Freight Booking screen appears. |  |
| 6. | Edit Ocean Freight Booking | On the Display Ocean Freight Booking screen, choose Edit. | The Edit Ocean Freight Booking screen appears. |  |
| 7. | Choose Execution Status Set to Arrived at Final Port of Discharge | Choose Execution Status > Set to Arrived at Final Port of Discharge . |  |  |
| 8. | Choose OK | In the Set to arrived at final port of discharge dialog box, choose OK | The following system message appears:Arrival at stop PORT_AESID was reported |  |
| 9. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

#### Departure of Truck at Port of Discharge (On-Carriage)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck is loaded and has left the port of discharge, the status of the freight order is set to Set to Departed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Launch App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen is displayed. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your road freight order number for on-carriage> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order screen appears. |  |
| 6. | Choose Edit | Choose Edit. | The Edit Road Freight Order screen appears |  |
| 7. | Choose Execution Status Set to Ready for Transportation Execution | Choose Execution Status > Set to Ready for Transportation Execution. | The following system messages appear:Ready for execution check completed without errorsExecution status of doc. Road Freight Order <your freight order number> set to "Ready for Transportation Execution" |  |
| 8. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 9. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 10. | Choose Execution Status (Source) Set to Departed | Choose Execution Status (Source) > Set to Departed . | The following system message appears:Departure at stop PORT_AESID was reported |  |
| 11. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

|  |
| --- |
| Note You can revoke the departed event by setting the status to Set to Not Departed |

#### Set Truck Arrived and Checked In at Receiving Point Location (On-Carriage)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

After the truck has arrived at the destination location the Dispatcher (TM) sets the execution status to Set to Arrived and Set to Checked In.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your road freight order number for on-carriage> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order screen, choose Edit. | The Edit Road Freight Order screen appears. |  |
| 7. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. | Execution Status is set to Arrived. |  |
| 9. | Choose Execution Status (Destination) Set to Arrived | Choose Execution Status (Destination ) > Set to Arrived . | The following system message appears: Arrival at stop SP_3310 was reported |  |
| 10. | Choose Execution Status (Destination) Set to Checked In | Choose Execution Status (Destination ) > Set to Checked In . | The following system message appears: Check-In at stop SP_3310 was reported |  |
| 11. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

|  |
| --- |
| Note You can revoke the arrival and check-in events by setting the status to Set to Not Arrived and Set to Not Checked In |

#### Set Ready for Warehousing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck is unloaded, the Dispatcher (TM) sets the execution status to Set Ready for Warehouse Processing (Destination).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your road freight order number for on-carriage> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Edit Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order screen, choose Edit. | The Edit Road Freight Order screen appears. |  |
| 7. | Scroll to the Stages sub section. | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages Table, Select the Stage Checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Choose Set Ready for Warehouse Processing (Destination) | Choose Warehouse Processing Status > Set to Ready for Warehouse Processing (Destination) . |  |  |
| 10. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

#### Set Truck Checked Out and Departed at Receiving Point Location (On-Carriage)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck has left the receiving point location, the Dispatcher (TM) sets the execution status to Set to Checked Out and Set to Departed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders(F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your road freight order number for on-carriage> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order screen, choose Edit. | The Edit Road Freight Order screen appears. |  |
| 7. | Scroll to the Stages sub section. | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Choose Execution Status (Destination) Set to Checked Out | Choose Execution Status (Destination) > Set to Checked Out . | The following system message appears: Checkout at stop SP_3310 was reported |  |
| 10. | Choose Execution Status (Destination) Set to Departed | Choose Execution Status (Destination) > Set to Departed . | The following system message appears: Departure at stop SP_3310 was reported |  |
| 11. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfullyPlease continue with Succeeding Processes in the Appendix Process Integration. |  |

|  |
| --- |
| Note You can revoke the check-out and departed event by setting Set to Not Checked Out and Set to Not Departed. |

#### Confirm Freight Costs for Accrual Postings

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step the Transportation Buyer monitors the freight documents (freight orders or freight bookings) and posts accruals.

The Transportation Buyer reviews these freight documents prior to posting the freight cost accruals, to ensure that they correspond to the provided transportation services of the freight forwarder or carrier. This ensures a good data quality for the financial department.

The overall freight costs of the freight documents are allocated to the respective transportation requirements, for example sales order or delivery based on gross weight. On the Cost Distribution tab, it is shown how the freight costs are broken down by sales order item or delivery item reference.

As a final step, the freight document can be confirmed for accrual postings. The system automatically posts the freight costs to financial accounting as accruals and creates a freight cost allocation document, a service purchase order and a service entry sheet. Financial postings are created depending on the business scenario to either expenses for an outbound process or to material accounts for an inbound process.

|  |
| --- |
| Note If the automatic freight cost confirmation and posting is activated as described in chapter Automate Confirmation and Posting of Freight Costs (Optional), the freight order is automatically confirmed for accrual posting. Alternatively, the Transportation Buyer can confirm selected freight orders for accrual posting manually as described below.If you performed Confirm Freight Cost for Accruals Postings in 6W3, you can skip this process and proceed with Monitor Freight Cost Allocation Documents.You only need to perform this process once for each freight document. |

Procedure

Table 27:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Transportation Buyer. | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Accrual Postings (F4329). | The Monitor Accruals Postings screen appears. |  |
| 3. | Enter Selection Criteria | On the Monitor Accrual Postings screen, make the following entry:Purchasing Organization: 3310Freight Document: Optionally <Enter your freight order or freight booking number>Note Example:For advanced intercompany sales or advanced intercompany stock transfer in case of an ocean freight booking, enter company code 1710.For advanced intercompany sales or advanced intercompany stock transfer in case of the freight order on-carriage, enter company code 3310.For all other scenarios, use company code 3310. |  |  |
| 4. | Choose Go | Choose Go. | The freight documents are displayed in the Monitor Accrual Postings table. |  |
| 5. | Navigate to the For Confirmation Tab | Navigate to the For Confirmation tab. | The freight documents for confirmation are displayed in the Monitor Accrual Postings table. |  |
| 6. | Freight Order / Freight Booking Details | Select the freight document row in the Monitor Accruals Posting table. | The Road Freight Order <your freight order number> - Process Accruals screen appears.orThe Rail Freight Order <your freight order number> - Process Accruals screen appears.orThe Ocean Freight Booking <your freight booking number> - Process Accruals screen appears.orThe Air Freight Booking <your freight booking number> - Process Accruals screen appears. |  |
| 7. | Display General Data (Optional) | Navigate to the General Data tab to review the header information. |  |  |
| 8. | Display Charges (Optional) | Scroll down to the Charges section to review the detailed information. | The charge item for the carrier or freight forwarder is displayed. |  |
| 9. | Display Charges (Optional) | In the Charge Hierarchy expand the node TM Carrier | The charge lines are displayed. |  |
| 10. | Display Charges Details (Optional) | Choose Show/Hide Details.Note Make sure that only one line is selected | The charge line details are displayed. |  |
| 11. | Display Stages (Optional) | Navigate to the Stages tab to review the stage details. |  |  |
| 12. | Display Business Partners (Optional) | Navigate to the Business Partner tab to review the parties involved. |  |  |
| 13. | Display Cost Distribution (Optional) | Navigate to the Cost Distribution tab to review the parties involved. | In the Distribution Hierarchy table it is shown how the freight costs are broken down by a sales order item or delivery item reference. |  |
| 14. | Confirm Freight Order or Confirm Freight Booking | Choose Confirm for Posting. | The following system message appears: Freight document <your freight order or freight booking> for <Your carrier or freight forwarder> confirmed for postingNote After confirming the freight order or freight booking for accruals posting, a service purchase order and a service entry sheet is created automatically in a background process. These documents are the basis for the invoice verification.Additionally, freight cost allocation documents (except for scope item BMY - Subcontracting purchase order with TM integration) are created as follows:Freight Cost Allocation (Expense) in all the legal ledgers for outbound transportation scenario (sell from stock, customer consignment fill-up/pickup, freight costs in the delivering company for ICO stock transport order and ICO intercompany sales process)Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario (procurement of material, inbound transport costs related to the ICO Stock transport order by the receiving company)If group valuation is activated, in case of ICO STO, the freight costs in the delivering company, Freight Cost Allocation (ML-Account), are posted in the group valuation ledger.For scope item BMY – Subcontracting purchase order with TM integration, freight cost allocation documents are created as follows:Freight Cost Allocation (ML-Account) in all the legal ledgers for outbound transportation scenario is only created when the goods receipt is performed for the inbound delivery of subcontracting purchase order. In case the confirming of freight document is done after goods receipt, the freight cost allocation (ML-Account) in all legal is created during confirming the freight document itself as done during usual freight cost confirming process.Freight Cost Allocation (ML-Account) in all legal ledgers for inbound transportation scenario.To see the details of the freight cost allocation document, follow the steps mentioned in the Monitor Freight Cost Allocation documents. |  |
| 15. | Navigate Back | Navigate back |  |  |

|  |
| --- |
| Note To confirm multiple freight documents simultaneously, choose multiple freight document checkboxes on the Monitor Accrual Postings overview page (under the For Confirmation tab) and choose Confirm for Posting. |

In case the posting result is an error, follow the steps below to check the error details and repost.

If, for example, the posting date is in a closed period, the posting date needs to be changed prior to posting of the freight document. You need to scroll down to the Charges section, navigate to the Posting Date tab, and change the accrual posting date in column Posting Date.

Table 28:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access App | Open Monitor Accrual Postings - Freight Documents (F4329). | The Monitor Accruals Postings screen appears. |  |
| 2 | Enter Selection Criteria | On the Monitor Accrual Postings screen, make the following entry:Purchasing Organization: 3310Freight Document: Optionally <Enter your freight order or freight booking number>Note Example:For advanced intercompany sales or advanced intercompany stock transfer in case of an ocean freight booking, enter company code 1710.For advanced intercompany sales or advanced intercompany stock transfer in case of the freight order on-carriage, enter company code 3310.For all other scenarios, use company code 3310. |  |  |
| 3 | Choose Go | Choose Go. | The freight documents are displayed in the Monitor Accrual Posting table. |  |
| 4 | Navigate to the Errors Tab | Navigate to the Errors tab | The freight documents with errors are displayed in the Monitor Accrual Postings table. |  |

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Future-dated internal transfer of control: Advanced Intercompany Sales says the goods movement posts one day later than the planned/actual date and time, while Advanced Intercompany Stock Transfer says it posts when that date and time is reached.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Advanced Intercompany scenarios: Post Goods Issue says the shipping point should be 1710, but the transfer-of-control display steps filter Shipping Point/Receiving Pt on 1010.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-transportation-execution-6w3-ae-sap-s-4hana-cloud-public-e-part-01]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-transportation-execution-6w3-ae-sap-s-4hana-cloud-public-e-part-03]]
- related-to :: [[11-inventory-warehouse-and-transportation/manual-transportation-planning-6w2-ae-test-script-sap-s-4hana-cloud-pu]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-sap-s-4hana-cloud-public-edition-external-transportation-p]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6W3_S4CLD2608_BPD_EN_AE.docx` — lines 2770–5533 of the extracted text · extracted with `mammoth` · 505,382 chars in the whole document
