---
id: 11-inventory-warehouse-and-transportation/test-script-sap-s-4hana-cloud-public-edition-external-transportation-p
title: Test Script SAP S/4HANA Cloud Public Edition - External Transportation Planning (6W1_AE) (6W1_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script, scope item 6W1_AE: monitor freight units and freight orders and create deliveries as Dispatcher (TM)."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/transportation-planning-and-execution]
aliases: [6W1_S4CLD2608_BPD_EN_AE]
keywords: [Transportation Planning and Execution, external transportation planning, freight units, blocked freight units, freight orders, delivery creation, manual transportation planning, business conditions, freight agreements, delivery creation job]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6W1_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1193
topic: 11-inventory-warehouse-and-transportation/transportation-planning-and-execution
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - External Transportation Planning (6W1_AE) (6W1_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6W1_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Transportation Planning and Execution** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | External Transportation Planning (6W1_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232859333)

[2 Prerequisites 4](#_Toc232859334)

[2.1 System Access 4](#_Toc232859335)

[2.2 Roles 4](#_Toc232859336)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232859337)

[2.4 Additional Manual Configuration 7](#_Toc232859338)

[2.5 Business Conditions 7](#_Toc232859339)

[3 Preliminary Steps 15](#_Toc232859340)

[3.1 Schedule Job - Create Deliveries (Optional) 15](#_Toc232859341)

[3.2 Complete and Create Freight Agreements 16](#_Toc232859342)

[4 Overview Table 17](#_Toc232859343)

[5 Test Procedures 18](#_Toc232859344)

[5.1 External Transportation Planning 18](#_Toc232859345)

[5.1.1 Monitor Freight Units (optional) 18](#_Toc232859346)

[5.1.1.1 Review Freight Unit Details 18](#_Toc232859347)

[5.1.1.2 Monitor Blocked Freight Units (Optional) 19](#_Toc232859348)

[5.1.2 Monitor Freight Orders 20](#_Toc232859349)

[5.1.3 Create Deliveries Based on Freight Orders 23](#_Toc232859350)

[6 Appendix 25](#_Toc232859351)

[7 Process Integration 26](#_Toc232859352)

[7.1 Preceding Processes 26](#_Toc232859353)

[7.2 Succeeding Processes 26](#_Toc232859354)

## Purpose

Overview

Manual planning allows you to create or change a transportation plan. To create a transportation plan, you assign transportation demands (such as freight unit stages) to transportation capacities (such as equipment types, for example, truck types, railcar types, or container types). The system creates capacity documents (freight orders or freight bookings). Scheduling runs automatically after you perform a planning activity for a road freight order. Manual planning is done in the Transportation Cockpit app. You can then create deliveries for these freight documents.

In this test script we assume you are using an SAP S/4HANA Cloud Private Edition system for External Planning and have activated scope item 4OZ (from SAP S/4HANA Cloud Private Edition) as a prerequisite.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

For more information, refer to How to Create a Business Role from a Template in the product assistance for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Dispatcher (TM) | SAP_BR_DISPATCHER | Dispatching | SAP_BR_DISPATCHER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)No serial number, no batch |  |
| Material | TG0011 | Trading Good 0011,PD,Regular Proc.(PD planning)no Serial no.; no batch |  |
| Material | SG23 | SEMI23,PD,Subcontracting | Material received from subcontractor |
| Material | RM13 | RAW13,PD,Subcontracting | Material provided to subcontractor |
| Material | RM14 | RAW14,PD,Subcontracting | Material provided to subcontractor |
| Customer | 33186001 | TM Domestic UAE Customer 1 |  |
| Location | 33186001 | Location for TM Domestic AE Customer 1Location Type 1021 Business Partner |  |
| Customer | 33186002 | TM Domestic UAE Customer 2 | Use this customer to create more sales orders and test the assignment of unplanned freight units from different sales orders to a freight order or freight booking. |
| Location | 33186002 | Location for TM Domestic AE Customer 2Location Type 1021 Business Partner |  |
| Supplier | 33300001 | Domestic Supplier 1 |  |
| Location | 0033300001 | Location for Domestic AE Supplier 1Location Type 1021 Business Partner |  |
| Carrier | 33386001 | TM Road Carrier AE 1 | Road carrier used for invoice verification |
| Carrier | 33386002 | TM Road Carrier Self-Billing AE | Road carrier used for self-billing and evaluated receipt settlement |
| Carrier | 33386201 | TM Rail Carrier AE 1 | Used for invoice verification |
| Carrier | 33386202 | TM Rail Carrier Self-Billing AE | Used for self-billing and evaluated receipt settlement |
| Supplier/Subcontractor | 33318607 | Domestic AE Subcontractor TM | Used in integration with scope item BMY - Subcontracting |
| Location | 00 33318607 | Location for Domestic AE Subcontractor TM |  |
|  |  |  |  |
| Purchasing group | 006 | TM Purchasing group for Materials (used in Material PO) |  |
| Location | SP_3310 | Shipping Point Location 3310Location Type 1003 Shipping Point | Outbound shipping |
| Location | SP_3320 | Shipping Point Location 3320Location Type 1003 Shipping Point | Stock transport shipping |
| Location | DNVR | Rail Junction DENVERLocation Type1190Rail Junction |  |

You can find general information on how to create master data objects in the following Master Data Scripts (MDS) :

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |
| BNE | Create Supplier Master - MDS |
| 4DE | Create Carrier Master - MDS |
| 3TL | Create Freight Agreement - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/1651842bf98e1812ff6e1bb01a51e00b)

### Business Conditions

In order to perform 6W1 - External Transportation Planning scope Item, one of the following scope items should be used as starting point. For the scope item selected, the Business Conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BD9 - Sell from Stock | Create a sales order as described in step Create Sales Order.In addition to the data described in BD9 - Sell from Stock with outbound delivery enter the following TM-specific data:For Road Scenarios:On the Create Standard Order: Overview screen, enterSold-to Party/Ship-to Party: 33186001 or 33186002Cust. Reference: <customer reference number>On the Sales tab, enterReq. Deliv.Date: <today + 6 working days>On the Create Standard Order: Overview screen, choose Display header details.On the Create Standard Order: Header Data screen, navigate to the Shipping tab and enterShipping Condition: 05 - TM - Ext. PlanningShipping Type: 01 - RoadGo back.On the Create Standard Order: Overview screen, enterMaterial: TG11Order Quantity: 150 PCChoose Display Item Details.On the Create Standard Order: Item Data screen, navigate to the Schedule Lines tab and choose Shipping.On the Create Standard Order: Schedule Line Data screen, enterGoods issue date: <today + 5 working days>Loading date: <today + 4 working days>Material avail.date: <today + 1 working days>Transportation Plan. Date: <today + 1 working days>For Rail Scenarios:On the Create Standard Order: Overview screen, enterSold-to Party/Ship-to Party: 33186001 or 33186002Cust. Reference: <customer reference number>On the Sales tab, enterReq. Deliv. Date: <today + 7 working days>On the Create Standard Order: Overview screen, choose Display header details.On the Create Standard Order: Header Data screen, navigate to the Shipping tab and enterShipping Condition: 05 - TM - Ext. PlanningShipping Type: 03 - RailGo back.On the Create Standard Order: Overview screen, enterMaterial: TG11Order Quantity: 150 PCChoose Display Item Details.On the Create Standard Order: Item Data screen, navigate to the Schedule Lines tab and choose Shipping.On the Create Standard Order: Schedule Line Data screen, enterGoods issue date: <today + 5 working days>Loading date: <today + 4 working days>Material avail.date: <today + 1 working days>Transportation Plan. Date: <today + 1 working days>Note When you combine BD9, 6W1, and 3BS, make the following changes: At the Create Sales Order step, before saving, select the order item and then choose Go to > Item > Shipping . In the Shipping section, enter the Stor.Location value of the warehouse-managed storage location (for example, storage location 335W).Note To view the freight unit number after the creation of the sales order, display your sales order. Go to TM Status and select SD Document, then choose on Document Flow to get the Freight Unit. |
| 3NR – Sales Scheduling Agreements | Create a sales scheduling agreement as described in step Create Sales Scheduling Agreement with the following values:In addition to the data described in 3NR – Sales Scheduling Agreements, enter the following TM-specific data:For Road Scenarios:On the Create Sched. Agr. w/Rel: Overview screen, enterSold-to Party/Ship-to Party: 33186001 or 33186002Cust. Reference: <customer reference number>Navigate to the Sales tab and enterReq. Deliv. Date: <today + 6 working days>On the Create Sched. Agr. w/Rel: Overview screen, choose Display header details.On the Create Sched. Agr. w/Rel: Header Data screen, navigate to the Shipping tab and enterShipping Condition: 05-TM - Ext. PlanningShipping Type: 01 - RoadGo back.On the Create Sched. Agr. w/Rel: Overview screen, enterMaterial: TG11Customer material number: RM129For Rail Scenarios:On the Create Sched. Agr. w/Rel: Overview screen, enterSold-to Party/Ship-to Party: 33186001 or 33186002Cust. Reference: <customer reference number>Navigate to the Sales tab and enterReq. Delivery Date: <today + 7 working days>On the Create Sched. Agr. w/Rel: Overview screen, choose Display header details.On the Create Sched. Agr. w/Rel: Header Data screen, navigate to the Shipping tab and enterShipping Condition: 05-TM - Ext. PlanningShipping Type: 03 - RailGo back.On the Create Sched. Agr. w/Rel: Overview screen, enterMaterial: TG11Customer material number: RM129For both scenarios:For both mode of transports described above, create schedule lines as described in step Update Scheduling Agreement for Forecast Delivery Schedule Manually (Optional). Enter the Forecast Delivery Schedule in addition to the data described in 3NR – Sales Scheduling Agreements and enter the following TM-specific data.Note Make sure to create schedule lines with dates corresponding to Requested Delivery Date entered above.On the Change Sched.Agr.w/ Rel. XXXXXXXX: Item Data screen, enterDlv. Schedule: 0Dlv. Sched. Date: <today>Date Type: DDate: <Select Req. Delivery Date entered above>Order Quantity: 150Select the first schedule line created and choose Sched. Line detail.On the Change Sched.Agr.w/ Rel. XXXXXXXX: Schedule Line Data screen, navigate to the Shipping tab and enterGoods issue date: <today + 5 working days>Loading date: <today + 4 working days>Material avail. date: <today + 1 working day>Transportation Plan. Date: <today + 1 working day>Perform the following process steps:Note When using 3BS - Warehouse Outbound Processing, at the Create Sales Scheduling Agreement step, before saving the sales scheduling agreement, select the item and then choose Goto > Item > Shipping . In the Shipping section, enter the Stor.Location value of the warehouse-managed storage location (for example, storage location 335W).Note To view the freight unit numbers after the creation of the scheduling agreement, display your scheduling agreement, go to TM Status tab and select SD Document, then choose on Document Flow to get the Freight Unit. |
| 2TX - Direct Procurement with Inbound Delivery | Create a purchase order as described in process step Option B: Create Purchase Order with Inbound Delivery.Note Caution: Use app Create Purchase Order - Advanced (ME21N).In addition to the data described in 2TX - Direct Procurement with Inbound Delivery, enter the following TM-specific data:Purchasing Group: 006 (TM - Ext. Planning)Navigate to the Delivery/Invoice tab and enterShipping Type: 01 Road or 03 Rail,Material: TG11Quantity: 150 PCReq. Delivery Date: <today + 6 working days>Note To view the freight unit after the creation of the purchasing order, display your purchase order, go to TM Status tab and choose Document Flow. |
| BME - Stock Transfer with Delivery | Create stock transport order as described in step Create Stock Transport Order (without MRP).In addition to the data described in BME - Stock Transfer with Delivery, enter the following TM-specific data:Purchasing Group: 006 (TM - Ext. Planning)Navigate to the Delivery/Invoice tab and enterShipping Type: 01 Road or 03 RailMaterial: TG11Quantity: 150 PCDelivery Date: <today + 6 working days>Navigate to the Delivery Schedule tab and enterMat. Staging Date: <today + 1 working days>Transptn Plang Date: <today + 1 working days>Loadg Date: <today + 4 working days>Goods Issue: <today + 5 working days>Change the confirmation control for inbound delivery as described in step Change Confirmation Control for Inbound Delivery.Note If you use the scope item BME combined with 6W1 and 3BS, enter the following data for plants:In the Header area:Suppyling Plant: 3310In the Item Overview area:Plant: 3320Storage Location: 332ANote When you combine BME, 6W1, and 3BS, make the following changes: At the Create Stock Transport Order step, before saving, select the order item and then choose Go to > Item > Shipping . In the Shipping section, enter the Stor.Location value of the warehouse-managed storage location (for example, storage location 335W).Note To view the freight unit after the creation of the stock transport order, display your sock transport order, go to TM Status tab and choose Document Flow. |
| BMY - Subcontracting | Create a subcontracting purchase order as described in step Create Purchase Order in scope item BMY – Subcontracting.Note Note Caution: Use app Create Purchase Order - Advanced(ME21N) .In addition to the data described in BMY – Subcontracting, enter the following TM specific data:Supplier: 33318607Purchasing Group: 006 (TM - Ext. Planning)Navigate to the Delivery/Invoice tab and enterShipping Type: 01 (Road)Item Category: L (Subcontracting)Material: SG23Quantity: 150 PCDelivery Date: <today + 6 working days>Net Price: 10Plant: 3310Choose Expand Item Details.Navigate to the Confirmations tab.Make the following entry:Confirmation Control: Inbound DeliveryNote Note: After creating the subcontracting purchase order, a freight unit for the inbound delivery will be created automatically.To display the freight unit, open app Display Purchase Order – Advanced.Choose Expand Header.Navigate to the TM Status tab.Choose Document Flow.Create Outbound DeliveryCreate an outbound delivery as described in scope item BMY – Subcontracting in step Option 1 : Outbound Delivery Create Outbound Delivery.In addition to the data described in BMY – Subcontracting, enter the following TM-specific data:Subcontractor: 33318607Open app Change Outbound Delivery as a Shipping Specialist.In the Header Data navigate to the Shipment tab.Make the following entry:Shp. Cond.: 05 (TM – Ext. Planning)Shipping Type: 01 (Road)Incoterms Version: 2020Incoterms: DDPIncoterm Loc. 1 ID: 0033318607Note When combining BMY, 6W1, and 3BS, make the following changes: After creating the Outbound Delivery for the transportation mode, open the Outbound Delivery in edit mode. In the Item Overview, update the Stor. Loc. value to the warehouse-managed storage location (e.g., storage location 335W).Note After saving the outbound delivery, the freight unit for the outbound delivery will be created automatically.To display the freight unit, open app Display Outbound Delivery.Navigate to the TM Status tab, choose Document Flow to display the freight unit items.Note Make sure to perform the planning for both outbound and inbound processes. |
| 1IU – Customer Consignment | Customer Consignment Fill-Up OrderCreate a Consignment Fill-Up Order as described in step Create Consignment Fill-Up Order in 1IUIn addition to the data described in 1IU – Customer Consignment, enter the following TM specific data:In the Sales tab, enterReq. Deliv.Date: <today + 6 working days>In the Header Data navigate to ths Shipping tabShp. Cond.: 05 TM – Ext. PlanningShipping Type: 01 – RoadNavigate to the Billing Document tab and enterIncoterms: DDPIncoterm Loc. 1 ID: 0033300007Customer Consignment Pick-Up OrderCreate a Consignment Pick-Up Order as described in step Create Consignment Pick-Up Order in 1IUIn addition to the data described in 1IU – Customer Consignment, enter the following TM specific data:In the Sales tab, enterReq. Deliv.Date: <today + 6 working days>In the Header Data navigate to ths Shipping tabShp. Cond.: 05 TM – Ext. PlanningShipping Type: 01 – RoadNote To view the freight unit number after the creation of the sales order, open Display Sales Orders VA03.On the Display Sales Documents screen, make the following entries:Order: your Fill-UP or Pick-Up order numberChoose Display Document Flow.Whenever transportation-relevant information is changed in the sales order, it leads to an update of the freight unit.Go back.On the Display Sales Documents screen, choose Continue.On the Display Standard Order: Overview screen, navigate to the TM Status tab.Select SD Document.Choose Document Flow.On the TM Document Flow for Sales Order screen, you can see the freight unit and the freight unit item. |

After the freight units for your freight orders have been created, they can be sent to a decentral transportation management system for planning. When you have finished planning in the decentral system, the planning result can be received in SAP S/4HANA Cloud Public Edition in the form of freight orders. If you are using SAP S/4HANA Cloud Private Edition system for External Planning, you have to activate scope item 4OZ. This is a prerequisite for the Monitor Freight Orders step.

## Preliminary Steps

### Schedule Job - Create Deliveries (Optional)

Use

You can schedule the creation of deliveries. Deliveries can be created for planned freight units only.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori Launchpad as a Dispatcher (TM). |  |  |
|  | Access App | Open Create Deliveries - From Freight Documents(F3662). | The Application Jobs screen appears. |  |
|  | Choose Create | On the Application Jobs screen, choose Create. | The New Job: Create Deliveries from Freight Documents screen appears. |  |
|  | Enter Job Name | On the New Job: Create Deliveries from Freight Documents screen, check or make the following entries:Job Template: Create Deliveries from Freight DocumentsJob Name: <Create Deliveries from Freight Documents> |  |  |
|  | Choose Step 2. | Choose Step 2. | The 2.Scheduling Options step appears. |  |
|  | Choose Define Recurrence Pattern. | Choose Define Recurrence Pattern. | The Scheduling Information dialog box appears. |  |
|  | Enter Scheduling Information | In the Scheduling Information dialog box, check or make the following entries:Start Immediately: XJob Start (Local Time): <time>Recurrence Pattern: <Minutes>Every :<30 Minute(s)>End: <None>On Non-Working Day: <No restriction>Calendar: <Calendar> |  |  |
|  | Choose OK | Choose OK. |  |  |
|  | Choose Step 3 | On the New Job: Create Deliveries from Freight Documents screen, choose Step 3. | The Step 3. Parameters step appears. |  |
|  | Enter Shipping Condition: TM – Ext. Planning (05) | Make the following entries:Shipping Condition: 05 - TM – Ext. Planning |  |  |
|  | Choose Schedule | Choose Schedule. | The following system message appears: Job Create Deliveries from Freight Documents has been scheduled.The job is displayed in the Jobs table. |  |

### Complete and Create Freight Agreements

Purpose

You must complete the freight agreement which was created as demo data with automatic activation before testing the integration to the following predecessor scope item listed in the business conditions:

- BME - Stock Transfer with Delivery

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Complete and Create Freight Agreement - MDSs in general | For more information on how to complete or Create Freight Agreement - MDSs, see master data script 3TL Create Freight Agreement - MDS - MDS. |  |  |
| 2 | Complete freight agreements for scope item BME - Stock Transfer with Delivery | Follow the instructions in master data script 3TL Create Freight Agreement - MDS - MDS where stock transport order scenarios are mentioned. | Freight agreements are enhanced with data for scope item BME - Stock Transfer with Delivery. |  |

## Overview Table

This scope item consists of several <choose the appropriate entity: process steps, reports, items> provided in the table below.

|  |
| --- |
| Note Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar (2434549).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [External Transportation Planning](#unique_11) [page ] 18 |  |  |  |
| [Monitor Freight Units (optional)](#unique_12) [page ] 18 | Dispatcher (TM) | Manage Freight Units (F3637) | A list of freight units is displayed. |
| [Review Freight Unit Details](#unique_13) [page ] 18 | Dispatcher (TM) | Manage Freight Units (F3637) | A list of freight units is displayed. |
| [Monitor Blocked Freight Units (Optional)](#unique_14) [page ] 19 | Dispatcher (TM) | Manage Freight Units (F3637) | A list of freight units is displayed. |
| [Monitor Freight Orders](#unique_15) [page ] 20 | Dispatcher (TM) | Manage Freight Orders (F3635) | A list of freight orders is displayed. |
| [Create Deliveries Based on Freight Orders](#unique_16) [page ] 23 | Dispatcher (TM) | Manage Freight Orders (F3635) | Delivery creation for freight order(s). |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### External Transportation Planning

#### Monitor Freight Units (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process consists of two steps. In the first step, the Dispatcher (TM) reviews the freight unit details of newly created freight units. In the second step, the Dispatcher (TM) monitors the blocked freight units.

##### Review Freight Unit Details

Purpose

The Dispatcher (TM) is responsible of monitoring the newly created freight units to ensure that they are consistent in terms of business context and that they are planned accordingly. The Dispatcher (TM) has to be able to timely react in case of planning backlog by contacting the responsible planning organization or the sales representative.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Freight Units (F3637). | Manage Freight Units (F3637) worklist opens. |  |
| 3 | Filter Freight Units | In the Manage Freight Units worklist, filter the freight units by:Planning Status: Not Planned (using the drop-down list)Planning Block: Not Blocked (using the drop-down list)Note To display the status value list, perform the search without parameters and mark the one corresponding to Not Planned.Optional:Mode of Transport: Road/RailPredecessor Document filter by using the sales or purchase order number.Use Adapt Filters to add the selection criteria on the screen. | Filters for Manage Freight Units worklist are set |  |
| 4 |  | Choose Go to filter the freight units. | Freight units with status Not Planned and Not Blocked are listed. |  |
| 5 | Freight Unit Details | Open the freight units by choosing the corresponding line to review the detailed information. | The freight unit-relevant information is displayed. |  |
| 6 |  | Navigate to the Freight Units Worklist. | Freight Units Worklist is displayed.Continue with Succeeding Processes in the Appendix Process Integration and execute scope item 4OZ - Planning of External Transportation Requirements. |  |

##### Monitor Blocked Freight Units (Optional)

Purpose

The Dispatcher (TM) is also responsible for monitoring newly created freight units that are blocked. He has to be able to timely react in case there are freight units that are blocked for planning. If needed, he contacts the responsible sales representative for clarification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Freight Units (F3637). | Manage Freight Units (F3637) worklist opens. |  |
| 3 | Filter Freight Units | In the Manage Freight Units worklist, filter the freight units by:Planning Status: Not Planned (using the drop-down list)Planning Block: Blocked (using the drop-down list)Note To display the status value list, perform the search without parameters and mark the one corresponding to Not Planned. | Filters for Manage Freight Units worklist are set. |  |
| 4 |  | Choose Go to filter the freight units. | Freight Units with Not Planned and Blocked are listed (for example the Freight Unit for Sales Order 5). |  |
| 5 | Freight Unit Details | Open the freight units by choosing the corresponding line to review the detailed information. | More detailed blocking information can be displayed in the Block Information tab. |  |
| 6 |  | Navigate to the Freight Units Worklist. | Freight Units Worklist is displayed.Continue with Succeeding Processes in the Appendix Process Integration and execute scope item 4OZ - Planning of External Transportation Requirements. |  |

#### Monitor Freight Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Dispatcher (TM) is responsible for monitoring incoming freight orders sent by the external transportation management system to react in a timely manner in case of an execution backlog by contacting the responsible execution organization. The Dispatcher (TM) is also responsible for reviewing that transportation charges are correctly calculated, and costs are distributed. Charge calculation and cost distribution are executed automatically right after the freight orders are received from the external transportation management system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Dispatcher (TM). | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Manage Freight Orders (F3635). | Manage Freight Orders (F3635) worklist opens. |  |
| 3 | Filter Freight Orders | In the Manage Freight Orders worklist, filter to select the newly replicated freight orders by using appropriate selection criteria, such as:Execution Status: Ready for Transportation ExecutionCharge Calculation Status: CalculatedOptional:Carrier: Trucking Company (33386001or33386002) or Railway Company (33386201or33386202)Freight Order Type: SFO1 (for External Road Freight Order)/SFR1 (for External Rail Freight Order)Mode of Transport: Road/RailPrerequisite is that the freight orders are set to Ready for Transportation Execution in the external transportation management system.Note You can add additional filter criteria:Choose Adapt Filters.Mark the corresponding checkbox.Choose OK. | Filters for Manage Freight Orders worklist are set. |  |
| 4 |  | Choose Go to filter the freight orders. | Freight orders matching the selection criteria are listed. |  |
| 5 | Freight Order Details | Open the created freight orders by choosing the corresponding line to review the detailed information. | The freight order information is displayed in different areas:In the different tabs in the header:General InformationBusiness PartnerChargesSubcontractingExecutionOutput RequestStatusesBlocking InformationDocument FlowAdministrative DataIn the Items and in the Stages. |  |
| 6 | General Data | Navigate to the General Data tab and verify transportation mode, shipping type, gross weight, volume, organizational data, source and destination location. | Relevant information is displayed. |  |
| 7 | Business Partner | Navigate to the Business Partner tab and verify different business partners like sold-to party, ship-to party etc. | Business partners are displayed. |  |
| 8 | Charges | Navigate to the Charges tab and verify charges like base flat rate, loading charges etc. | Charges-relevant information is displayed. |  |
| 9 | Execution | Navigate to the Execution tab.Status-related details are displayed on the Execution tab. | Execution status-relevant information is displayed. |  |
| 10 | Status | Navigate to the Statuses tab. The Dispatcher (TM) checks the execution status of the respective freight orders. |  |  |
| 11 | Document Flow | Navigate to the Document Flow tab, to verify the documents linked to the freight order. | The document flow is displayed. |  |
| 12 | Items | Navigate to Items and verify information related to product, quantity, and weight. | Items-related information is disaplayed. |  |
| 13 | Stages | Navigate to Stages and verify information related to source and destination location, planned and actual dates. | Stage-relevant information is displayed. |  |
| 14 |  | Navigate to the Manage Freight Orders worklist. |  |  |

|  |
| --- |
| Note Note In case of any changes to the freight agreement used in a freight order, charges for the freight order can be recalculated. You can do this either in the Manage Freight Orders worklist by selecting the respective freight order or directly within a freight order by choosing Calculate Charges. |

#### Create Deliveries Based on Freight Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Dispatcher (TM) triggers the delivery creation for selected freight orders manually in the freight orders list report as described below.

|  |
| --- |
| Note Note If the batch job "Schedule Batch Job - Create Deliveries” is scheduled as described in chapter Schedule Batch Job - Create Deliveries (Optional), the deliveries are created automatically. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2 | Access App | In the Transportation Order Management group, choose Manage Freight Orders (F3635). | Manage Freight Orders (F3635) worklist is displayed. |  |
| 3 | Filter Freight Orders | On the Manage Freight Orders screen, filter to select the newly replicated freight orders by using appropriate selection criteria, for example:Execution Status: Ready for Transportation ExecutionCharge Calculation Status: CalculatedOptional:Carrier: Trucking Company (33386001or33386002) or Railway Company (33386201or33386202).Freight Order Type: SFO1 (for External Road Freight Order)/SFR1 (for External Rail Freight Order)Mode of Transport: Road/RailNote You can add additional filter criteria:Choose Adapt Filters.Mark the corresponding checkbox.Choose OK. | The filter for the Manage Freight Orders worklist is set. |  |
| 4 |  | Choose Go to filter the freight orders. | Freight orders matching the selection criteria are listed. |  |
| 5 | Create Deliveries | Select the freight orders by marking the checkbox and choose Create Deliveries. | Deliveries are created. |  |
| 6 | Verify Created Delivery Numbers in the Freight Order | Open the freight orders for which you created deliveries by choosing the corresponding line item. Review the detailed information. | As soon as the updated message is received from the external transportation management system, the predecessor document gets replaced by the delivery number in the Item Information. |  |
| 7 |  | Navigate to the Manage Freight Orders Worklist. |  |  |

## Appendix

## Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

### Preceding Processes

The following processes and conditions can proceed this process.

| Process | Business Condition |
| --- | --- |
| BD9 - Sell from Stock | Create a sales order |
| 3NR – Sales Scheduling Agreements | Create a sales scheduling agreementUpdate the scheduling agreement for forecast delivery schedule manuallyGenerate the planning delivery schedule |
| 2TX - Direct Procurement with Inbound Delivery | Create a purchase order |
| BME - Stock Transfer with Delivery | Create a stock transport order |
| BMY – Subcontracting | Create subcontracting purchase orderCreate Outbound Delivery |
| 1IU – Customer Consignment | Create Customer Fill-Up OrderCreate Customer Pick-Up Order |

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 4OZ - Planning of External Transportation Requirements | Create a freight order after the freight units are created and monitored. |
| BD9 - Sell from Stock | Execute picking after outbound delivery creation triggered by a freight document.Continue with executing the test procedure for outbound process with used mode of transport in scope item 6W3 - Transportation Execution. |
| 3NR – Sales Scheduling Agreements | Execute picking after outbound delivery creation triggered by a freight document.Continue with executing the test procedure for outbound process with used mode of transport in scope item 6W3 - Transportation Execution. |
| 6W3 - Transportation Execution | After executing the preceding process 2TX- Transportation Execution, continue with executing the test procedure for inbound process with used mode of transport in scope item 6W3 - Transportation Execution.BMY – Subcontracting inbound |
| BME - Stock Transfer with Delivery | Pick and post goods issue for a stock transport order after the stock transport delivery creation triggered by freight document.Execute the test steps 1 to 4 (Picking) and save your changes.Continue with executing the test procedure for stock transfer process with the used mode of transport in scope item 6W3 -Transportation Execution. |
| BMY - Subcontracting | Outbound: Execute the test steps 1 to 4 (picking) as described in chapter Pick and Post Goods Issue in scope item BMY - Subcontracting. Goods issue will be described in scope item 6W3 – Transportation Execution.Continue with executing the test procedure for outbound process with mode of transport Road in scope item 6W3 - Transportation Execution.Make sure to perform the planning for both outbound and inbound processes. |
| 1IU – Customer Consignment | Consignment Fill-Up OrderExecute Pick Goods after delivery creation triggered by freight document.Continue executing the test procedure for outbound process with used mode of transport in scope item 6W3 - Transportation Execution.Consignment Pick-Up OrderContinue executing the test procedure for inbound process with used mode of transport in scope item 6W3 - Transportation Execution.. |

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
- related-to :: [[11-inventory-warehouse-and-transportation/manual-transportation-planning-6w2-ae-test-script-sap-s-4hana-cloud-pu]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-transportation-execution-6w3-ae-sap-s-4hana-cloud-public-e-part-01]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6W1_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 42,168 chars in the whole document
