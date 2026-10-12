---
id: 11-inventory-warehouse-and-transportation/manual-transportation-planning-6w2-ae-test-script-sap-s-4hana-cloud-pu
title: "Manual Transportation Planning (6W2_AE) - Test Script, SAP S/4HANA Cloud Public Edition (6W2_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 6W2 (AE): manual transportation planning in TM for road, rail, ocean, air and advanced intercompany, with prerequisites, sample data, steps."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/transportation-planning-and-execution]
aliases: [6W2_S4CLD2608_BPD_EN_AE]
keywords: [Transportation Planning and Execution, manual transportation planning, road freight orders, rail freight orders, ocean freight bookings, air freight bookings, advanced intercompany transportation, carrier subcontracting, delivery creation from freight documents, test data prerequisites]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6W2_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1194
topic: 11-inventory-warehouse-and-transportation/transportation-planning-and-execution
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Manual Transportation Planning (6W2_AE) - Test Script, SAP S/4HANA Cloud Public Edition (6W2_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6W2_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Transportation Planning and Execution** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Manual Transportation Planning (6W2_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232859207)

[2 Prerequisites 4](#_Toc232859208)

[2.1 System Access 4](#_Toc232859209)

[2.2 Roles 4](#_Toc232859210)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232859211)

[2.4 Additional Manual Configuration 8](#_Toc232859212)

[2.5 Business Conditions 8](#_Toc232859213)

[2.6 Preliminary Steps 23](#_Toc232859214)

[2.6.1 Schedule Job - Create Deliveries (Optional) 23](#_Toc232859215)

[2.6.2 Create a Foreign Customer (Optional) 25](#_Toc232859216)

[2.6.3 Create a Foreign Supplier (Optional) 25](#_Toc232859217)

[2.6.4 Create a Foreign Location (Optional) 26](#_Toc232859218)

[2.6.5 Complete and Create Freight Agreement - MDS 26](#_Toc232859219)

[3 Overview Table 28](#_Toc232859220)

[4 Test Procedures 31](#_Toc232859221)

[4.1 Manual Transportation Planning Road Freight Order 31](#_Toc232859222)

[4.1.1 Perform Manual Transportation Planning for Road Freight Order 31](#_Toc232859223)

[4.1.2 Perform Subcontracting for Road Freight Order 34](#_Toc232859224)

[4.1.3 Receive Confirmation for Road Freight Order 36](#_Toc232859225)

[4.1.4 Trigger Delivery Creation and Monitor Road Freight Order 37](#_Toc232859226)

[4.2 Manual Transportation Planning Rail Freight Order 39](#_Toc232859227)

[4.2.1 Perform Manual Transportation Planning for Rail Freight Order 39](#_Toc232859228)

[4.2.2 Perform Subcontracting for Rail Freight Order 41](#_Toc232859229)

[4.2.3 Receive Confirmation for Rail Freight Order 43](#_Toc232859230)

[4.2.4 Trigger Delivery Creation and Monitor Rail Freight Order 44](#_Toc232859231)

[4.3 Manual Transportation Planning Ocean Freight Booking 45](#_Toc232859232)

[4.3.1 Perform Manual Transportation Planning for Ocean Freight Booking 45](#_Toc232859233)

[4.3.2 Perform Subcontracting for Ocean Freight Booking 48](#_Toc232859234)

[4.3.3 Receive Confirmation for Ocean Freight Booking 50](#_Toc232859235)

[4.3.4 Create Freight Orders for Pick-up and Delivery for Ocean Freight Booking 53](#_Toc232859236)

[4.3.5 Display Pick-up and Delivery Freight Order (Optional) 54](#_Toc232859237)

[4.3.6 Trigger Delivery Creation and Monitor Ocean Freight Booking 55](#_Toc232859238)

[4.4 Manual Transportation Planning Air Freight Booking 57](#_Toc232859239)

[4.4.1 Perform Manual Transportation Planning for Air Freight Booking 57](#_Toc232859240)

[4.4.2 Perform Subcontracting for Air Freight Booking 60](#_Toc232859241)

[4.4.3 Receive Confirmation for Air Freight Booking 61](#_Toc232859242)

[4.4.4 Create Freight Orders for Pick-up and Delivery for Air Freight Booking 63](#_Toc232859243)

[4.4.5 Display Pick-up and Delivery Freight Order (Optional) 65](#_Toc232859244)

[4.4.6 Trigger Delivery Creation and Monitor Air Freight Booking 66](#_Toc232859245)

[4.5 Perform Manual Transportation Planning for Advanced Intercompany Business Processes 67](#_Toc232859246)

[4.5.1 Perform Manual Transportation Planning Pick-Up and Main Stages for Advanced Intercompany Business Processes 67](#_Toc232859247)

[4.5.2 Perform Subcontracting Pick-Up and Main Stage for Advanced Intercompany Business Processes 70](#_Toc232859248)

[4.5.3 Receive Booking Confirmation Pick-Up and Main Stage for Advanced Intercompany Business Processes 72](#_Toc232859249)

[4.5.4 Create Freight Order for Pick-Up for Advanced Intercompany Business Processes 74](#_Toc232859250)

[4.5.5 Display Freight Order for Pick-Up for Advanced Intercompany Business Processes (Optional) 76](#_Toc232859251)

[4.5.6 Trigger Delivery Creation and Monitor Ocean Freight Booking Advanced Intercompany Business Processes 77](#_Toc232859252)

[4.5.7 Perform Manual Transportation Planning Delivery Stage for Advanced Intercompany Business Processes 78](#_Toc232859253)

[4.5.8 Perform Subcontracting Delivery Stage for Advanced Intercompany Business Processes 81](#_Toc232859254)

[4.5.9 Receive Freight Order Confirmation Delivery Stage for Advanced Intercompany Business Processes 83](#_Toc232859255)

[5 Appendix 84](#_Toc232859256)

[5.1 Process Integration 84](#_Toc232859257)

[5.1.1 Preceding Processes 84](#_Toc232859258)

[5.1.2 Succeeding Processes 85](#_Toc232859259)

## Purpose

Overview

Manual planning allows you to create or change a transportation plan. To create a transportation plan, you assign transportation demands (such as freight unit stages) to transportation capacities (such as equipment types, for example, truck types, railcar types, or container types). The system creates capacity documents (freight orders or freight bookings). Scheduling runs automatically after you perform a planning activity for a road freight order. Manual planning is done in the Transportation Cockpit app. You can then create deliveries for these freight documents.

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
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)No serial number, no batch | Used for outbound processes and Advanced Intercompany Stock Transfer |
| Material | TG0011 | Trading Good 0011,PD,Regular Proc. (PD planning)No serial number; no batch | Used for inbound processes |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad. | Used for advanced intercompany sales |
| Material | SG23 | SEMI23, PD, Subcontracting | Material received from subcontractor |
| Material | RM13 | RAW13, PD, Subcontracting | Material provided to subcontractor |
| Material | RM14 | RAW14, PD, Subcontracting | Material provided to subcontractor |
| Customer | 33186001 | TM Domestic UAE Customer 1 |  |
| Location | 33186001 | Location for TM Domestic AE Customer 1 | Location Type 1021 Business Partner |
| Customer | 33186002 | TM Domestic UAE Customer 2 |  |
| Location | 33186002 | Location for TM Domestic AE Customer 2 | Location Type 1021 Business Partner |
| Customer | 33186005 | TM Domestic AE Customer 5 |  |
| Location | 33186005 | TM Domestic AE Customer 5 | Location Type 1021 Business Partner |
| Customer | 33100006 | Domestic UAE Customer 6 |  |
| Location | 33100006 | Location for Domestic Customer 6 |  |
| Supplier | 33300001 | Domestic Supplier 1 |  |
| Location | 0033300001 | Location for Domestic AE Supplier 1Location for Domestic US Supplier 1 | Location Type 1021 Business Partner |
| Customer | 17100003 | Domestic US Customer 3 |  |
| Location | 0017100003 | Location for Domestic Customer 3 | Location Type 1021 Business Partner |
| Supplier | 33300006 | Domestic UAE Supplier 6 |  |
| Carrier | 33386001 | TM Road Carrier AE 1 | Road carrier used for invoice verification |
| Carrier | 33386002 | TM Road Carrier AE 1 | Road carrier used for self-billing and evaluated receipt settlement |
| Carrier | 33386201 | TM Rail Carrier AE 1 |  |
| Carrier | 33386202 | TM Rail Carrier Self-Billing AE |  |
| Carrier | 33386301 | TM Ocean Carrier AE 1 |  |
| Carrier | 33386302 | TM Ocean Carrier Self-Billing AE |  |
| Carrier | 33386501 | TM Airline AE 1 |  |
| Carrier | 33386502 | TM Airline Self-Billing AE 2 |  |
| Carrier | 33386401 | TM Freight Forwarder AE 1 |  |
| Carrier | 33386402 | TM Freight Forwarder Self-Billing AE |  |
| Supplier/Subcontractor | 33318607 | Domestic AE Subcontractor TM | Used in integration with scope item BMY - Subcontracting |
| Location | 0033318607 | Location for Domestic AE Subcontractor TM |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 007 | TM Purchasing group for Materials (used in Material PO) |  |
| Shipping Point | 331R | Shipping Point 331R | Shipping point for returns |
| Location | SP_3310 | Shipping Point Location 3310Location Type 1003 Shipping Point | Shipping point outboundReceiving point in stock transfer, advanced intercompany stock transfer, and inbound |
| Location | SP_3320 | Shipping Point Location 3320Location Type 1003 Shipping Point | Shipping point stock transfer |
| Location | SP_331R | Shipping point location SP_331R (used for customer returns)Location Type 1003 Shipping Point | Receiving point customer returns |
| Location | PORT_AESID | Seaport 1Port LocationLocation Type 1100 Port | Port of discharge sales outboundPort of loading customer returnsPort of loading procurement inboundPort of loading stock transferPort of discharge advanced intercompany salesPort of discharge advance intercompany stock transfer |
| Location | PORT_AEYAS | Seaport 2Port LocationLocation Type 1100 Port | Port of loading sales outboundPort of discharge customer returnsPort of discharge procurement inboundPort of discharge stock transfer |
| Location | AIRPORT_DXB | Dubai International AirportLocation Type 1110 Airport | Airport of departure outboundAirport of destination inbound and stock transfer |
| Location | AIRPORT_AUH | Abu Dhabi International AirportLocation Type 1110 Airport | Airport of destination outboundAirport of departure inbound and stock transfer |
| Company Code | 3310 | Company Code 3310 | Company code of the receiving company in Advanced Intercompany Business Processes |
| Location | SP_1710 | Shipping Point Location 1710 (supplying shipping point location)Location Type 1003 Shipping Point | Shipping point delivering company in Advanced Intercompany Business Processes |
| Company Code | 1710 | Company code 1710 (supplying / delivering company) | Company code of the delivering company in Advanced Intercompany Sales and receiving company in Advanced Intercompany Stock Transfer |
| Carrier | 17386401 | TM Freight Forwarder US 1 | Carrier used by the delivering company in Advanced Intercompany Business Processes for invoice verification |
| Carrier | 17386402 | TM Freight Forwarder Self-Billing US | Carrier used by the delivering company in Advanced Intercompany Business Processes used for self-billing and evaluated receipt settlement |
| Purchasing Organization | 1710 | Purchasing organization 1710 (supplying / delivering plant) | Purchasing organization used by the delivering company in Advanced Intercompany Business Processes |
| Location | PORT_USLAX | Location PORT_USLAX Port of Los AngelesLocation Type 1100 Port | Port of Loading used by the delivering company in Advanced Intercompany Business Processes |

You can find general information on how to create master data objects in the following Master Data Scripts (MDS) :

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |
| BNE | Create Supplier Master - MDS |
| 4DE | Create Carrier Master - MDS |
| 3TL | Create Freight Agreement - MDS |
| 7E9 | Manage Locations - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/42dd4339cfe4da162ff8853b143d0b96)

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BD9 - Sell from Stock | Create a sales order as described in step Create Sales Order. Use the app Manage Sales Orders (F1873). On the Manage Sales Order screen, and choose Create > Create Sales Orders - VA01.In addition to the data described in BD9 - Sell from Stock enter the following TM-specific data:For Road Scenarios:On the Create Standard Order: Overview screen, enterSold-to Party/Ship-to Party: 33186001 or 33186002Cust. Reference: <customer reference number>On the Sales tab, enterReq. Deliv.Date: <today + 6 working days>On the Create Standard Order: Overview screen, choose Display header details.On the Create Standard Order: Header Data screen, navigate to the Shipping tab and enterShipping Condition: 06 - TM - Int. PlanningShipping Type: 01 - RoadGo back.On the Create Standard Order: Overview screen, enterMaterial: TG11Quantity: 150 PCChoose Display Item Details.On the Create Standard Order: Item Data screen, navigate to the Schedule Lines tab and choose Shipping.On the Create Standard Order: Schedule Line Data screen, enterGoods issue date: <today + 5 working days>Loading date: <today + 4 working days>Material avail.date: <today + 1 working day>Transportation Plan. Date: <today + 1 working day>For use case consignment order, create three sales orders as follows:Sales Order 1Sold-to Party/Ship-to Party: 33186001Order Quantity: 40 PCSales Order 2Sold-to Party/Ship-to Party: 33186001Order Quantity: 50 PCSales Order 3Sold-to Party/Ship-to Party: 33186002Order Quantity: 60 PCFor Rail Scenarios:On the Create Standard Order: Overview screen, enterSold-to Party/Ship-to Party: 33186001 or 33186002Cust. Reference: <customer reference number>On the Sales tab, enterReq. Deliv. Date: <today + 7 working days>On the Create Standard Order: Overview screen, choose Display header details.On the Create Standard Order: Header Data screen, navigate to the Shipping tab and enterShipping Condition: TM - Int. PlanningShipping Type: 03 - RailGo back.On the Create Standard Order: Overview screen, enterMaterial: TG11Order Quantity: 150 PCChoose Display Item Details.On the Create Standard Order: Item Data screen, navigate to the Schedule Lines tab and choose Shipping.On the Create Standard Order: Schedule Line Data screen, enterGoods issue date: <today + 5 working days>Loading date: <today + 4 working days>Material avail.date: <today + 1 working day>Transportation Plan. Date: <today + 1 working day>For Ocean Scenarios:On the Create Standard Order: Overview screen, enterSold-to Party/Ship-to Party: 33186002Cust. Reference: <customer reference number>On the Sales tab, enterReq. Delivery Date: <today + 4 weeks>On the Create Standard Order: Overview screen, choose Display header details.On the Create Standard Order: Header Data screen, navigate to the Shipping tab and enterShipping Condition: TM - Int. PlanningShipping Type: 04 – SeaNavigate to the Billing Document tab and enterIncoterms: DDPIncoterm Loc. 1 ID: 33186002Go back.On the Create Standard Order: Overview screen, enterMaterial: TG11Order Quantity: 150 PCChoose Display Item Details.On the Create Standard Order: Item Data screen, navigate to the Schedule Lines tab and choose Shipping.On the Create Standard Order: Schedule Line Data screen, enterGoods issue date: <today + 5 working days>Loading date: <today + 4 working days>Material avail.date: <today + 1 working day>Transportation Plan. Date: <today + 1 working day>For Air Scenarios:On the Create Standard Order: Overview screen, enterSold-to Party/Ship-to Party: 33186002Cust. Reference: <customer reference number>On the Sales tab, enterReq. Deliv. Date: <today + 7 working days>On the Create Standard Order: Overview screen, choose Display header details.On the Create Standard Order: Header Data screen, navigate to the Shipping tab and enterShipping Condition: TM - Int. PlanningShipping Type: 05 – AirNavigate to the Billing Document tab and enterIncoterms: DDPIncoterm Loc. 1 ID: 33186002Go back.On the Create Standard Order: Overview screen, enterMaterial: TG11Order Quantity: 150 PCChoose Display Item Details.On the Create Standard Order: Item Data screen, navigate to the Schedule Lines tab and choose Shipping.On the Create Standard Order: Schedule Line Data screen, enterGoods issue date: <today + 5 working days>Loading date: <today + 4 working days>Material avail.date: <today + 1 working day>Transportation Plan. Date: <today + 1 working day>Note When you combine BD9, 6W2, and 3BS, make the following changes: At the Create Sales Order step, before saving, select the order item and then choose Go to > Item > Shipping . In the Shipping section, enter the Stor.Location value of the warehouse-managed storage location (for example, storage location 335W).Note To view the freight unit number after the creation of the sales order, open Display Sales Orders VA03.On the Display Sales Documents screen, make the following entries:Order: your sales order numberChoose Display Document Flow.Whenever transportation-relevant information is changed in the sales order, it leads to an update of the freight unit.Go back.On the Display Sales Documents screen, choose Continue.On the Display Standard Order: Overview screen, navigate to the TM Status tab.Select SD Document.Choose Document Flow.On the TM Document Flow for Sales Order screen, you can see the freight unit and the freight unit item.Note You can create more sales orders to test the assignment of unplanned freight units from different sales orders to a freight order or freight booking. |
| 3NR – Sales Scheduling Agreements | Create a sales scheduling agreement as described in step Create Sales Scheduling Agreement.In addition to the data described in 3NR – Sales Scheduling Agreements, enter the following TM-specific data:For Road Scenarios:On the Create Sched. Agr. w/Rel: Overview screen, enterSold-to Party/Ship-to Party: 33186001 or 33186002Cust. Reference: <customer reference number>Navigate to the Sales tab and enterReq. Deliv. Date: <today + 6 working days>On the Create Sched. Agr. w/Rel: Overview screen, choose Display header details.On the Create Sched. Agr. w/Rel: Header Data screen, navigate to the Shipping tab and enterShipping Condition: TM - Int. PlanningShipping Type: 01 - RoadGo back.On the Create Sched. Agr. w/Rel: Overview screen, enterMaterial: TG11Customer material number: RM129For Rail Scenarios:On the Create Sched. Agr. w/Rel: Overview screen, enterSold-to Party/Ship-to Party: 33186001 or 33186002Cust. Reference: <customer reference number>Navigate to the Sales tab and enterReq. Delivery Date: <today + 7 working days>On the Create Sched. Agr. w/Rel: Overview screen, choose Display header details.On the Create Sched. Agr. w/Rel: Header Data screen, navigate to the Shipping tab and enterShipping Condition: TM - Int. PlanningShipping Type: 03 - RailGo back.On the Create Sched. Agr. w/Rel: Overview screen, enterMaterial: TG11Customer material number: RM129For Ocean Scenarios:On the Create Sched. Agr. w/Rel: Overview screen, enterSold-to Party/Ship-to Party: 33186002Cust. Reference: <customer reference number>Navigate to the Sales tab and enterReq. Delivery Date: <today + 4 weeks>On the Create Sched. Agr. w/Rel: Overview screen, choose Display header details.On the Create Sched. Agr. w/Rel: Header Data screen, navigate to the Shipping tab and enterShipping Condition: TM - Int. PlanningShipping Type: 04 – SeaNavigate to the Billing Document tab and enterIncoterms: DDPIncoterm Loc. 1 ID: 33186002Go back.On the Create Sched. Agr. w/Rel: Overview screen, enterMaterial: TG11Customer material number: RM129For Air Scenarios:On the Create Sched. Agr. w/Rel: Overview screen, enterSold-to Party/Ship-to Party: 33186002Cust. Reference: <customer reference number>Navigate to the Sales tab and enterReq. Deliv.Date: <today + 7 working days>On the Create Sched. Agr. w/Rel: Overview screen, choose Display header details.Shipping Condition: TM - Int. PlanningShipping Type: 05 – AirNavigate to the Billing Document tab and enterIncoterms: DDPIncoterm Loc. 1 ID: 33186002Go back.On the Create Sched. Agr. w/Rel: Overview screen, enterMaterial: TG11Customer material number: RM129For All Scenarios:For all mode of transports described above create schedule lines as described in step Update Scheduling Agreement for Forecast Delivery Schedule Manually (Optional), enter the Forecast Delivery Schedule in addition to the data described in 3NR – Sales Scheduling Agreements, enter the following TM-specific data:Note Make sure to create schedule lines with dates corresponding to Requested Delivery Date entered above.On the Change Sched.Agr.w/ Rel. XXXXXXXX: Item Data screen, enterDlv. Schedule: 0Dlv. Sched. Date: <today>Date Type: DDate: <Select Req. Delivery Date entered above>Order Quantity: 150Select first schedule line created and choose Sched. Line detail.On the Change Sched.Agr.w/ Rel. XXXXXXXX: Schedule Line Data screen, navigate to the Shipping tab and enterGoods issue date: <today + 5 working days>Loading date: <today + 4 working days>Material avail.date: <today + 1 working day>Transportation Plan. Date: <today + 1 working day>Perform the following process steps:Maintain Planning Delivery Schedule Instruction (Optional)Update Scheduling Agreement for Forecast Delivery Schedule Manually (Optional)Generate Planning Delivery Schedule (Optional)Note When using ccc, at the Create Sales Scheduling Agreement step, before saving the Sales Scheduling Agreement, select the item and then choose Goto > Item > Shipping . In the Shipping section, enter the Stor.Loc. value of the warehouse-managed Storage Location (for example, Storage Location 335W). |
| 2TX - Direct Procurement with Inbound Delivery | Create a purchase order as described in process step Option B: Create Purchase Order with Inbound Delivery:Note Caution: Use app Create Purchase Order - Advanced (ME21N) .In addition to the data described in 2TX - Direct Procurement with Inbound Delivery, enter the following TM-specific data:Purchasing Group: 007 (TM - Int. Planning)Navigate to the Delivery/Invoice tab and enterShipping Type: 01 Road or 03 RailMaterial: TG11Quantity: 150 PCDelivery Date: <today + 6 working days>orShipping Type: 04 - SeaMaterial: TG11Quantity: 150 PCDelivery Date: <today + 4 weeks>orShipping Type: 05 – AirMaterial: TG11Quantity: 150 PCReq. Delivery Date: <today + 7 working days>Note You can create more purchase orders to test the assignment of unplanned freight units from different purchase orders to a freight order or freight booking. |
| BME - Stock Transfer with Delivery | Create a stock transport order as described in step Create Stock Transport Order (without MRP).In addition to the data described in BME - Stock Transfer with Delivery, enter the following TM-specific data:Purchasing Group: 007 (TM - Int. Planning)Navigate to the Delivery/Invoice tab and enterShipping Type: 01 Road or 03 RailMaterial: TG11Quantity: 150 PCDelivery Date: <today + 6 working days>orShipping Type: 04 – SeaMaterial: TG11Quantity: 150 PCDelivery Date: <today + 4 weeks>orShipping Type: 05 – AirMaterial: TG11Quantity: 150 PCDelivery Date: <today + 7 working days>For all shipping types select the purchase order item and choose PO Item.Navigate to Delivery Schedule tab and enterMat. Staging Date: <today + 1 working day>Transptn Plang Date: <today + 1 working day>Loadg Date: <today + 4 working days>Goods Issue: <today + 5 working days>Change the confirmation control for inbound delivery as described in step Change Confirmation Control for Inbound Delivery.Note If you use the scope item BME combined with 6W2 and 3BS, enter the following data for plants:In the Header area:Suppyling Plant: 3310In the Item Overview area:Plant: 3320Storage Location: 332ANote When you combine BD9, 6W2, and 3BS, make the following changes: At the Create Sales Order step, before saving, choose Go to > Item > Shipping . In the Shipping section, enter the Stor. Location value for the warehouse-managed storage location (for example, storage location 335W).Note You can create more stock transport orders to test the assignment of unplanned freight units from different stock transport orders to a freight order or freight booking. |
| BDD - Lean Customer Returns | PrerequisitesYou must have a reference invoice number and a billing document according to Sell from Stock (BD9).Create a returns order as described in step Create Returns Order.In addition to the data described in BDD - Lean Customer Returns, enter the following TM-specific data:On the Sales tab, enterReq. Delivery Date: <today + 6 or 7 working daysOn the Create Lean Return: Overview screen, choose Display header details.On the Create Lean Return: Header Data screen, navigate to the Shipping tab and enterShipping Condition: 06 - TM - Int. PlanningShipping Type: 01 Road or 03 Rail,Go back.Choose Display Item Details.On the Create Lean Return: Item Data screen, navigate to the Shipping tab and enterShipping Point: 331ROn the Create Lean Return: Item Data screen, navigate to the Schedule Lines tab and choose Shipping.On the Create Lean Return: Schedule Line Data screen, enterGoods issue date: <today + 5 working days>Loading date: <today + 4 working days>Material avail.date: <today + 1 working day>Transportation Plan. Date: <today + 1 working day>Req. Delivery Date: <today + 6 or 7 working days>orShipping Type: 04 - SeaChoose Display Item Details.On the Create Lean Return: Item Data screen, navigate to the Shipping tab and enterShipping Point: 331ROn the Create Lean Return: Item Data screen, navigate to the Schedule Lines tab and choose Shipping.On the Create Lean Return: Schedule Line Data screen, enterGoods issue date: <today + 5 working days>Loading date: <today + 4 working days>Material avail.date: <today + 1 working day>Transportation Plan. Date: <today + 1 working day>Req. Delivery Date: <today + 4 weeks>orShipping Type: 05 – AirChoose Display Item Details.On the Create Lean Return: Item Data screen, navigate to the Shipping tab and enterShipping Point: 331ROn the Create Lean Return: Item Data screen, navigate to the Schedule Lines tab and choose Shipping.On the Create Lean Return: Schedule Line Data screen, enterGoods issue date: <today + 5 working days>Loading date: <today + 4 working days>Material avail.date: <today + 1 working day>Transportation Plan. Date: <today + 1 working day>Req. Delivery Date: <today + 7 working days> |
| BMK - Return to Supplier | Create a return purchase order as described in step Create Returns Purchase Order.In addition to the data described in BMK - Return to Supplier enter the following TM specific data:Purchasing Group: 007 (TM - Int. Planning)Navigate to the Delivery/Invoice tab and enterShipping Type: 01 RoadDelivery Date: <today + 6 Working days>Note To view the freight unit number after the creation of the Returns Purchase Order, open Display Purchase Order - Advanced (ME23N).On the Display Purchase Order screen, select Other Purchase Documents and make the following entries:Pur. Order: your returns purchase order numberSelect Pur. OrderChoose Other Document.Open the Header section, and navigate to the TM Status tab.Choose Document Flow.On the TM Document Flow for Purchase Document screen, you can see the freight unit and the freight unit item.We only describe an example with shipping type 01 – Road transportation. However, shipping types 02 – Rail, 04 – Sea or 05 – Air are possible for rail, sea and air transportation respectively. |
| 5D2 - Advanced Intercompany Sales | In our example, the sales organization 3310 is selling the product TG12 to a domestic customer. The goods are directly shipped to the customer from the plant 1710, which is owned by the delivering company 1710.Create sales order as described in step Create Sales Order.Note If you run 3BS - Warehouse Outbound Processing together with 5D2 - Advanced Intercompany Sales, ensure the warehouse-managed storage location is filled in on the sales order before you save it:In the Create Sales Order step, select the item.Choose Goto > Item > Shipping .In the Shipping section, enter the warehouse-managed storage location in the Stor. Location field (for example, 335W).In addition to the data described in 5D2 - Advanced Intercompany Sales, enter the following TM-specific data:Sold-to Party/Ship-to Party: 33186005Cust. Reference: <customer reference number>On the Sales tab, enterReq. Delivery Date: <today + 4 weeks>On the Create Standard Order: Overview screen, choose Display header details.Shipping Condition: 06 - TM - Int. PlanningShipping Type: 04 – SeaOn the Create Standard Order: Header Data screen, navigate to the Billing Document tab and enterIncoterms Version: 2020Incoterms: DDPIncoterm Loc. 1 ID: 33186005Tax Departure C/R: AEGo back.On the Create Standard Order: Overview screen, enterMaterial: TG12Quantity: 150 PCChoose Display Item Details.On the Create Standard Order: Item Data screen, navigate to the Schedule Lines tab and choose Shipping.Goods Issue Date: <today + 5 working days>Loading date: <today + 4 working days>Material Avail. Date: <today + 1 working day>Transportation Plan. Date: <today + 1 working day>Note For a transport between countries separated by an ocean, only shipping types 04 – Sea or 05 – Air are possible. If you are using a delivering company, plant and shipping point from a country that has a land border, you can also use shipping type 01 Road or 03 Rail. We only describe an example with shipping type 04 – Sea. |
| 5HP - Advanced Intercompany Stock Transfer | Create intercompany stock transfer order as described in step Create Intercompany Stock Transfer Order.In addition to the data described in 5HP - Advanced Intercompany Stock Transfer enter the following TM specific data:Purchasing Group: 007 (TM - Int. Planning)Navigate to the Delivery/Invoice tab and enter Shipping Type: 04 - Sea.Material: TG11Quantity: 150 PCSelect the purchase order item and choose PO Item.Navigate to the Delivery Schedule tab and enterDelivery Date: <today + 4 weeks>Mat. Staging Date: <today + 1 working day>Transptn Plang Date: <today + 1 working day>Loadg Date: <today + 4 working days>Goods Issue: <today + 5 working days>Note When you combine 5HP, 6W2, and 3BS, make the following changes: After the Trigger Delivery Creation for the transportation mode, open the delivery in edit mode. In the Item Overview, change the Stor. Loc value of the warehouse-manage storage location (for example storage location 335W).Note For a transport between countries separated by an ocean only shipping types 04 – Sea or 05 – Air are possible. If you are using a supplier from a country that has a land border, you can also use shipping type: 01 Road or 03 Rail. We only describe an example with shipping type 04 – Sea. |
| BMY - Subcontracting | Create a subcontracting purchase order as described in step Create Purchase Order in scope item BMY – Subcontracting.Note Caution: Use app Create Purchase Order - Advanced(ME21N) .In addition to the data described in BMY – Subcontracting, enter the following TM-specific data:Supplier: 33318607Purchasing Group: 007 (TM – Int. Planning)Navigate to the Delivery/Invoice tab and enterShipping Type: 01 (Road)Item Category: L (Subcontracting)Material: SG23Quantity: 150 PCDelivery Date: <today + 6 working days>Net Price: 10Plant: 3310Choose Expand Item Details.Navigate to the Confirmations tab.Make the following entry:Confirmation Control: Inbound DeliveryNote After creating the subcontracting purchase order, a freight unit for the inbound delivery will be created automatically.To display the freight unit, open app Display Purchase Order – Advanced.Choose Expand Header.Navigate to the TM Status tab.Choose Document Flow.Continue with step Create Outbound DeliveryCreate Outbound DeliveryCreate an outbound delivery as described in scope item BMY – Subcontracting in step Option 1 : Outbound Delivery Create Outbound Delivery.In addition to the data described in BMY – Subcontracting, enter the following TM-specific data to create the delivery:Subcontractor: 33318607Before proceeding, ensure that you select the raw materials associated with the previously created purchase order.Open app Change Outbound Delivery as a Shipping Specialist.In the Header Data navigate to the Shipment tab.Make the following entry:Shp. Cond.: 06 (TM – Int. Planning)Shipping Type: 01 (Road)Incoterms Version: 2020Incoterms: DDPIncoterm Loc. 1 ID: 0033318607Note When combining BMY, 6W2, and 3BS, make the following changes: After creating the outbound delivery for the transportation mode, open the outbound delivery in edit mode. In the Item Overview, update the Stor. Loc. value to the warehouse-managed storage location (for example, storage location 335W).Note After saving the outbound delivery, the freight unit for the outbound delivery will be created automatically.To display the freight unit, open app Display Outbound Delivery.Navigate to the TM Status tab, choose Document Flow to display the freight unit items.Note Ensure that you complete the planning process for both outbound deliveries and purchase orders that have been created. |
| 1IU – Customer Consignment | Customer Consignment Fill-Up OrderCreate a Consignment Fill-Up Order as described in step Create Consignment Fill-Up Order in 1IUIn addition to the data described in 1IU – Customer Consignment, enter the following TM specific data:In the Sales tab, enterReq. Deliv.Date: <today + 6 working days>In the Header Data navigate to ths Shipping tabShp. Cond.: 06 TM – Int. PlanningShipping Type: 01 – RoadNavigate to the Billing Document tab and enterIncoterms: DDPIncoterm Loc. 1 ID: 0033100003Customer Consignment Pick-Up OrderCreate a Consignment Pick-Up Order as described in step Create Consignment Pick-Up Order in 1IUIn addition to the data described in 1IU – Customer Consignment, enter the following TM specific data:In the Sales tab, enterReq. Deliv.Date: <today + 6 working days>In the Header Data navigate to ths Shipping tabShp. Cond.: 06 TM – Int. PlanningShipping Type: 01 – RoadNote To view the freight unit number after the creation of the sales order, open Display Sales Orders VA03.On the Display Sales Documents screen, make the following entries:Order: your Fill-UP or Pick-Up order numberChoose Display Document Flow.Whenever transportation-relevant information is changed in the sales order, it leads to an update of the freight unit.Go back.On the Display Sales Documents screen, choose Continue.On the Display Standard Order: Overview screen, navigate to the TM Status tab.Select SD Document.Choose Document Flow.On the TM Document Flow for Sales Order screen, you can see the freight unit and the freight unit item. |
| 46P - Determination of Geocoordinates, Distances and Durations | To schedule road freight orders the Determination of Geocoordinates, Distances and Durations (46P) scope item must be activated and set up. |

### Preliminary Steps

#### Schedule Job - Create Deliveries (Optional)

Use

You can schedule the creation of deliveries. Deliveries can be created for planned freight units only.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Dispatcher (TM). |  |  |
| 2 | Access App | Open Create Deliveries - From Freight Documents(F3662). | The Application Jobs screen appears. |  |
| 3 | Choose Create | On the Application Jobs screen, choose Create. | The New Job: Create Deliveries from Freight Documents screen appears. |  |
| 4 | Enter Job Name | On the New Job: Create Deliveries from Freight Documents screen, check or make the following entries:Job Template: Create Deliveries from Freight DocumentsJob Name: <Create Deliveries from Freight Documents> |  |  |
| 5 | Choose Step 2 | Choose Step 2. | The 2.Scheduling Options step appears. |  |
| 6 | Choose Define Recurrence Pattern | Choose Define Recurrence Pattern. | The Scheduling Information dialog box appears. |  |
| 7 | Enter Scheduling Information | In the Scheduling Information dialog box, check or make the following entries:Start Immediately: XJob Start (Local Time): <time>Recurrence Pattern: <Minutes>Every :<30 Minute(s)>End: <None>On Non-Working Day: <No restriction>Calendar: <Calendar> |  |  |
| 8 | Choose OK | Choose OK. |  |  |
| 9 | Choose Step 3 | On the New Job: Create Deliveries from Freight Documents screen, choose Step 3. | The 3. Parameters step appears. |  |
| 10 | Enter Shipping Condition: TM – Int. Planning (06) | Make the following entries:Shipping Condition: TM – Int. Planning (06) |  |  |
| 11 | Choose Schedule | Choose Schedule. | The following system message appears: Job Create Deliveries from Freight Documents has been scheduled.The job is displayed in the Jobs table. |  |

#### Create a Foreign Customer (Optional)

Purpose

You can create a customer in a foreign country.

|  |
| --- |
| Note Note Caution: Export taxes content is not delivered with SAP Best Practices for Transportation Management. Follow the instructions to configure tax solution in SAP Activate for SAP S/4HANA Cloud Public Edition. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Create a Foreign Customer | For more information on creating the foreign customer, see the https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/982e94d5f072f9a0ade948ef90c00af1/01d2de3fc8e1421ebf6248769f0d0a7c.html (BND) master data script. | Customer master data is created. |  |
| 2 | Create Location from Customer | For more information on creating a location for the foreign customer, see the set-up instructions https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/Setup/6W2_Set-Up_EN_XX.pdf (6W2), chapter Create Locations from Shipping Points and Customers. | Location for customer master data is created. |  |

#### Create a Foreign Supplier (Optional)

Purpose

You can create a supplier in a foreign country.

|  |
| --- |
| Note Note Caution: Import taxes content is not delivered with SAP Best Practices for Transportation Management. Follow the instructions how to configure the tax solution in SAP Activate for SAP S/4HANA Cloud Public Edition. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Create a Foreign Supplier | For more information on creating the foreign supplier, see the https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/56ccaf9fbaf5bc19a4cd462421191488/bb4b6e5f9e664663bec683b8b5b9793c.html (BNE) master data script. | Supplier master data is created. |  |

#### Create a Foreign Location (Optional)

Purpose

You can create a foreign location such as a seaport or an airport.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Create a Foreign Location | For more information on creating the foreign location, see the https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/397b21b0d6b5855e244d41c2aba6208f/466f871f764b4cad845fb90928f56998.html (7E9) master data script. | Location master data is created. |  |

#### Complete and Create Freight Agreement - MDS

Purpose

Before testing the integration to the following predecessor scope items listed in the business conditions, you must complete the freight agreements which were created as demo data with automatic activation. You also must create a new freight agreements:

- BME - Stock Transfer with Delivery
- 5D2 - Advanced Intercompany Sales
- 5HP -Advanced Intercompany Stock Transfer
- BMK -Return to Supplier

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Complete and Create Freight Agreement - MDSs in General | For more information on how to complete or Create Freight Agreement - MDSs, see master data script 3TL Create Freight Agreement - MDS. |  |  |
| 2 | Complete Freight Agreements for Scope Item BME - Stock Transfer with Delivery | Follow the instructions in master data script 3TL Create Freight Agreement - MDS where stock transport order scenarios are mentioned. | Freight agreements are enhanced with data for scope item BME - Stock Transfer with Delivery. |  |
| 3 | Complete Freight Agreements for Scope Items 5D2 and 5HP:5D2 - Advanced Intercompany Sales5HP - Advanced Intercompany Stock Transfer | Follow the instructions in chapter Create Freight Agreement - MDS for Freight Forwarder1 (Invoice Verification) – Ocean (Intercompany Scenarios). | Freight agreement for intercompany scenarios is created. |  |
| 4 | Complete Freight Agreements for Scope Item:BMK -Return to Supplier | Follow the instructions in master data script 3TL Create Freight Agreement - MDS - MDS where the return to supplier scenario is mentioned. | Freight agreements are enhanced with data for scope item BMK– Return to Supplier. |  |

## Overview Table

This scope item consists of several <choose the appropriate entity: process steps, reports, items> provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

|  |  |  |  |
| --- | --- | --- | --- |
| <Choose the appropriate entity: Process Step, Report or Item> | Business Role | App/Transaction | Expected Results |
| [Manual Transportation Planning Road Freight Order](#unique_15) [page ] 31 |  |  |  |
| [Perform Manual Transportation Planning for Road Freight Order](#unique_16) [page ] 31 | Dispatcher (TM) | Transportation Cockpit (/SCMTMS/PLN) | The system creates capacity documents, that is, road freight orders. |
| [Perform Subcontracting for Road Freight Order](#unique_17) [page ] 34 | Dispatcher (TM) | Manage Freight Orders (F3635) | Freight order sent to carrier |
| [Receive Confirmation for Road Freight Order](#unique_18) [page ] 36 | Dispatcher (TM) | Manage Freight Orders (F3635) | Confirmation status from the carrier is stored in the freight order document. |
| [Trigger Delivery Creation and Monitor Road Freight Order](#unique_19) [page ] 37 | Dispatcher (TM) | Manage Freight Orders (F3635) | Delivery creation for freight order(s). |
| [Manual Transportation Planning Rail Freight Order](#unique_20) [page ] 39 |  |  |  |
| [Perform Manual Transportation Planning for Rail Freight Order](#unique_21) [page ] 39 | Dispatcher (TM) | Transportation Cockpit (/SCMTMS/PLN) | The system creates capacity documents, that is, rail freight orders. |
| [Perform Subcontracting for Rail Freight Order](#unique_22) [page ] 41 | Dispatcher (TM) | Manage Freight Orders (F3635) | Freight order sent to carrier |
| [Receive Confirmation for Rail Freight Order](#unique_23) [page ] 43 | Dispatcher (TM) | Manage Freight Orders (F3635) | Confirmation status from the carrier is stored in the freight order document. |
| [Trigger Delivery Creation and Monitor Rail Freight Order](#unique_24) [page ] 44 | Dispatcher (TM) | Manage Freight Orders (F3635) | Delivery creation for freight order(s). |
| [Manual Transportation Planning Ocean Freight Booking](#unique_25) [page ] 45 |  |  |  |
| [Perform Manual Transportation Planning for Ocean Freight Booking](#unique_26) [page ] 45 | Dispatcher (TM) | Transportation Cockpit (/SCMTMS/PLN) | The system creates capacity documents, that is, freight orders or freight bookings. |
| [Perform Subcontracting for Ocean Freight Booking](#unique_27) [page ] 48 | Dispatcher (TM) | Manage Ocean Freight Bookings (F6213) | Freight booking sent to carrier |
| [Receive Confirmation for Ocean Freight Booking](#unique_28) [page ] 50 | Dispatcher (TM) | Manage Ocean Freight Bookings (F6213) | Confirmation status from the carrier is stored in the freight booking document. |
| [Create Freight Orders for Pick-up and Delivery for Ocean Freight Booking](#unique_29) [page ] 53 | Dispatcher (TM) | Manage Ocean Freight Bookings (F6213) | Ocean freight booking assigned to road freight order for pick-upOcean freight booking assigned to road freight order for deliveryRoad freight order for pick-up savedRoad freight order for delivery saved |
| [Display Pick-up and Delivery Freight Order (Optional)](#unique_30) [page ] 54 | Dispatcher (TM) | Manage Freight Orders (F3635) | Freight order for pick-up displayedFreight order for delivery displayed |
| [Trigger Delivery Creation and Monitor Ocean Freight Booking](#unique_31) [page ] 55 | Dispatcher (TM) | Manage Ocean Freight Bookings (F6213) | Delivery creation for freight order(s). |
| [Manual Transportation Planning Air Freight Booking](#unique_32) [page ] 57 |  |  |  |
| [Perform Manual Transportation Planning for Air Freight Booking](#unique_33) [page ] 57 | Dispatcher (TM) | Transportation Cockpit (/SCMTMS/PLN) | The system creates capacity documents, that is, freight orders or freight bookings. |
| [Perform Subcontracting for Air Freight Booking](#unique_34) [page ] 60 | Dispatcher (TM) | Manage Air Freight Bookings (F6535) | Freight booking sent to carrier |
| [Receive Confirmation for Air Freight Booking](#unique_35) [page ] 61 | Dispatcher (TM) | Manage Air Freight Bookings (F6535) | Confirmation status from the carrier is stored in the freight booking document. |
| [Create Freight Orders for Pick-up and Delivery for Air Freight Booking](#unique_36) [page ] 63 | Dispatcher (TM) | Manage Air Freight Bookings (F6535) | Air freight booking assigned to road freight order for pick-upAir freight booking assigned to road freight order for deliveryRoad freight order for pick-up savedRoad freight order for delivery saved |
| [Display Pick-up and Delivery Freight Order (Optional)](#unique_37) [page ] 65 | Dispatcher (TM) | Manage Freight Orders (F3635) | Freight order for pick-up displayedFreight order for delivery displayed |
| [Trigger Delivery Creation and Monitor Air Freight Booking](#unique_38) [page ] 66 | Dispatcher (TM) | Manage Air Freight Bookings (F6535) | Delivery creation for freight order(s). |
| [Perform Manual Transportation Planning for Advanced Intercompany Business Processes](#unique_39) [page ] 67 |  |  |  |
| [Perform Manual Transportation Planning Pick-Up and Main Stages for Advanced Intercompany Business Processes](#unique_40) [page ] 67 | Dispatcher (TM) | Transportation Cockpit (/SCMTMS/PLN) | The system creates capacity documents, that is, freight orders or freight bookings. |
| [Perform Subcontracting Pick-Up and Main Stage for Advanced Intercompany Business Processes](#unique_41) [page ] 70 | Dispatcher (TM) | Manage Ocean Freight Bookings (F6213) | Freight booking sent to carrier |
| [Receive Booking Confirmation Pick-Up and Main Stage for Advanced Intercompany Business Processes](#unique_42) [page ] 72 | Dispatcher (TM) | Manage Ocean Freight Bookings (F6213) | Confirmation status from the carrier is stored in the freight booking document. |
| [Create Freight Order for Pick-Up for Advanced Intercompany Business Processes](#unique_43) [page ] 74 | Dispatcher (TM) | Manage Ocean Freight Bookings (F6213) | Ocean freight booking assigned to road freight order for pick-upRoad freight order for pick-up saved |
| [Display Freight Order for Pick-Up for Advanced Intercompany Business Processes (Optional)](#unique_44) [page ] 76 | Dispatcher (TM) | Manage Freight Orders (F3635) | Freight order for pick-up displayed |
| [Trigger Delivery Creation and Monitor Ocean Freight Booking Advanced Intercompany Business Processes](#unique_45) [page ] 77 | Dispatcher (TM) | Manage Ocean Freight Bookings (F6213) | Delivery creation for freight order(s). |
| [Perform Manual Transportation Planning Delivery Stage for Advanced Intercompany Business Processes](#unique_46) [page ] 78 | Dispatcher (TM) | Transportation Cockpit (/SCMTMS/PLN) | The system creates capacity documents, that is, road freight orders. |
| [Perform Subcontracting Delivery Stage for Advanced Intercompany Business Processes](#unique_47) [page ] 81 | Dispatcher (TM) | Manage Freight Orders (F3635) | Freight order sent to carrier |
| [Receive Freight Order Confirmation Delivery Stage for Advanced Intercompany Business Processes](#unique_48) [page ] 83 | Dispatcher (TM) | Manage Freight Orders (F3635) | Confirmation status from the carrier is stored in the freight order document. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Manual Transportation Planning Road Freight Order

#### Perform Manual Transportation Planning for Road Freight Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Manual planning allows you to create or change a transportation plan. To create a transportation plan, you assign transportation demands, that is, freight unit stages, to transportation capacities, that is, equipment types, such as truck types. The system creates capacity documents, that is, road freight orders.

Scheduling runs automatically after you perform a planning activity for a road freight order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Dispatcher (TM). |  |  |
| 2 | Access App | Open Transportation Cockpit (/SCMTMS/PLN). | The Transportation Cockpit: Selection Criteria screen appears. |  |
| 3 | Enter: Selection Criteria | On the Transportation Cockpit: Selection Criteria screen, make the following entries:Freight Unit StagesBoth Locations - equal to - Select the checkbox (Both Locations)Source Location – equal to – <enter your source location>Note Example:SP_3310 (outbound, fill-up consignment order, outbound to subcontractor, stock transport order when BME is combined with 6W2 and 3BS)0033300001 (inbound)SP_3320 (stock transport order)33186001 or 33186002 (customer returns)SP_331R (Returns to Supplier)0033100003 (pick-up consignment order)0033318607(inbound from subcontractor)Note Choose Insert New Row to add a new row for a new selection criterion.Destination Location – equal to – <your destination location>Note Example:33186001 or 33186002 (outbound, fill-up consignment order)33186001 and 33186002 (use case consignment order outbound)SP_3310 (inbound, stock transport order and inbound from subcontracting, Pick-Up Consignment Order)SP_3320 (stock transport order with BME, 6W2, and 3BS)SP_331R (customer returns)0033100006 (Returns to Supplier)0033318607 (outbound to subcontractor)Planning Status of Freight Unit Stage – equal to: U (Unplanned)Transportation Mode equal to: 01 (Road)Vehicle TypesVehicle Type – equal to: STR400 (Vehicle 40.0 t)SettingsPage Layout for Transportation Cockpit - equal to: SAP Simplified TC |  |  |
| 4 | Choose Continue | Choose Continue. | The Transportation Cockpit screen appears. |  |
| 5 | Select Freight Unit | On the Transportation Cockpit screen, select your freight unit(s) in the Freight Unit Stages section. |  |  |
| 6 | Select the Equipment Group Row | On the Trucks table, select the Equipment Group row. |  |  |
| 7 | Choose Assign Selected Items | Choose Assign Selected Items at the top of the screen.Caution If the following system message appears, Freight Unit <your freight unit>: Acceptable times for pickup/del. at <your source location> at <date and time> is outside plan. horizon. adapt the planning horizon by choosing Change Planning Settings. | The following system messages appear:Freight Unit <your freight unit> assigned to Road Freight OrderLocal consignment order <your consignment order number> createdMessages for Freight Order $1 :Freight order Road Freight Order createdFor the use case consignment order outbound, the following additional system messages appear:Number of requirement documents assigned: 3Local consignment order <your consignment order number1> createdLocal consignment order <your consignment order number2> created |  |
| 8 | Save Your Entries | Save your entries. | The following system messages appear:Data saved successfullyMessages for Freight Order <your freight order number>:Business document with temporary number $1 saved as business doc. <your freight order number> |  |
| 9 | Note Down Your Freight Order Number | Note down your freight order number. |  |  |
| 10 | Open Freight Order (Optional) | For use case consignment order outbound, choose <your freight order number> in the Road Freight Orders section to open the just created freight order.Scroll down to section Items: In the Item Hierarchy of the vehicle, two consignment orders and the assigned freight units are displayed.Scroll further down to section Stages. The following stages are displayed:Stage 1 from shipping point location to location of customer 1Stage 2 from location of customer 1 to location of customer 2 | The Display Road Freight Order <your freight order number> screen appears. |  |

#### Perform Subcontracting for Road Freight Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Perform subcontracting and communicate the freight order details to the carrier.

You can send the freight order to the carrier by choosing Subcontracting > Send to Carrier.

Then, an EDI message is sent to the carrier, and you can't change the carrier anymore.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). |  |  |
| 2 | Access App | Open Manage Freight Orders (F3635). | The Manage Freight Orders (F3635) screen appears. |  |
| 3 | Enter Freight Order | On the Manage Freight Orders screen, make the following entries:Freight Order: <your freight order number> |  |  |
| 4 | Choose Go | Choose Go. | The freight order is displayed in the Freight Orders table. |  |
| 5 | Select the Freight Order | Select the freight order row in the Freight Orders table. | The Display Road Freight Order <your freight order number> screen appears. |  |
| 6 | Choose Edit | Choose Edit. | The Edit Road Freight Order <your freight order number> screen appears. |  |
| 7 | Navigate to the General Data Tab | Navigate to the General Data tab. |  |  |
| 8 | Enter Carrier, Purchasing Organization and Purchasing Group | On the Edit Road Freight Order <your freight order number> screen, make the following entries:Carrier: 33386001 or 33386002Purchasing Organization: 3310Purchasing Group: 005 |  |  |
| 9 | Save your Entries | Save your entries. | The following system messages appear:Data saved successfullyCharge calculation completedCost distribution completed |  |
| 10 | Choose Subcontracting Send to Carrier | On the Edit Road Freight Order <your freight order number> screen, choose Subcontracting > Send to Carrier. | The Warning dialog box appears. |  |
| 11 | Choose Ok | In the Warning dialog box, choose Ok. | The following system messages appear:Data saved successfullyFreight order sent to carrierCharge calculation completedCost distribution completed |  |
| 12 | Navigate to the Communication History Tab | Navigate to the Communication History tab. |  |  |
| 13 | Choose Refresh | Choose Refresh. | A line in the table with Outbound Document, Request to Carrier appears. |  |
| 14 | Select Request to Carrier line | In the table select the line Outbound Document, Request to Carrier | The Details: Outbound Document, Request to Carrier appear. |  |

#### Receive Confirmation for Road Freight Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If you receive a confirmation message via EDI from the carrier, this information is also stored in the freight order document and is constantly updated. Alternatively, you can set the confirmation status manually by choosing Subcontracting > Set to Confirmed by Carrier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). |  |  |
| 2 | Access App | Open Manage Freight Orders(F3635). | The Manage Freight Orders(F3635) screen appears. |  |
| 3 | Enter Freight Order | On the Manage Freight Orders screen, make the following entries:Freight Order: <your freight order number> |  |  |
| 4 | Choose Go | Choose Go. | The freight order is displayed in the Freight Orders table. |  |
| 5 | Select the Freight Order | Select the freight order row in the Freight Orders table. | The Display Road Freight Order <your freight order number> screen appears. |  |
| 6 | Choose Edit | Choose Edit. | The Edit Road Freight Order <your freight order number> screen appears. |  |
| 7 | Choose Subcontracting Set to Confirmed by Carrier | On the Edit Road Freight Order <your freight order number> screen, choose Subcontracting > Set to Confirmed by Carrier. | Navigate to the Statuses tab.Check the following entries:Subcontracting Status: Sent.Confirmation Status: Confirmed. |  |
| 8 | Save your Entries | Save your entries. | The following system messages appear:Data saved successfullyCharge calculation completedCost distribution completed |  |
| 9 | Navigate to the Communication History Tab | Navigate to the Communication History tab. |  |  |
| 10 | Choose Refresh | Choose Refresh. | A line in the table with Inbound Document, Confirmation by Carrier appears. |  |
| 11 | Select Confirmation by Carrier line | In the table select the line Inbound Document, Confirmation by Carrier. | The Details: Inbound Document, Confirmation by Carrier appear. |  |

#### Trigger Delivery Creation and Monitor Road Freight Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create deliveries from the list view for selected freight orders. You can check the deliveries that have been created on the Document Flow tab. You can also navigate to the different business documents that are related to the freight document from this tab.

|  |
| --- |
| Note Skip this step in case of the subcontracting outbound process, because the outbound delivery was already created in scope item BMY – Subcontracting in step Option 1 : Outbound Delivery Create Outbound Delivery. |

|  |
| --- |
| Note If the application job Schedule Batch Job - Create Deliveries is scheduled as described in chapter Preliminary Steps Schedule Batch Job - Create Deliveries (Optional), the deliveries are created automatically. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). |  |  |
| 2 | Access App | Open Manage Freight Orders (F3635). | The Manage Freight Orders (F3635) screen appears. |  |
| 3 | Enter Carrier and Execution Status | On the Manage Freight Orders screen, make the following entries:Carrier: 33386001 or 33386002Execution Status: Not Started |  |  |
| 4 | Choose Go | Choose Go. | The freight orders are displayed in the Freight Orders table. |  |
| 5 | Select the Freight Order Checkbox | Select the Freight Order checkbox. |  |  |
| 6 | Choose Create Deliveries | Choose Create Deliveries. | The following system message appears:Delivery creation triggered for <number> freight order(s) |  |
| 7 | Select the Freight Order (Optional) | Select the freight order row in the Freight Orders table. | The Display Road Freight Order <your freight order number> screen appears. |  |
| 8 | Check Delivery in the Document Hierarchy (Optional) | Navigate to the Document Flow tab. | The delivery documents are displayed in the Document Hierarchy.Please continue with Succeeding Processes in the Appendix > Process Integration. |  |

### Manual Transportation Planning Rail Freight Order

#### Perform Manual Transportation Planning for Rail Freight Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Manual planning allows you to create or change a transportation plan. To create a transportation plan, you assign transportation demands, that is, freight unit stages, to transportation capacities, that is, equipment types, such as railcar types. The system creates capacity documents, that is, rail freight orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori Launchpad as a Dispatcher (TM). |  |  |
|  | Access App | Open Transportation Cockpit(/SCMTMS/PLN). | The Transportation Cockpit: Selection Criteria screen appears. |  |
|  | Enter: Selection Criteria | On the Transportation Cockpit: Selection Criteria screen, make the following entries:Freight Unit StagesBoth Locations - equal to - Select the checkbox (Both Locations)Source Location – equal to – <enter your source location>Note Note Example:SP_1710 (outbound)0017300001 (inbound)SP_1720 (stock transport order)0017186002 (customer returns)SP_171R (Returns to Supplier)Note Note Choose Insert New Row to add a new row for a new selection criterion.Destination Location – equal to – <your destination location>Note Note Example:0017186002 (outbound)SP_1710 (inbound, stock transport order)SP_171R (customer returns)0017100006 (Returns to Supplier)Planning Status of Freight Unit Stage – equal to: U (Unplanned)SettingsTransportation Mode equal to: 02 (Rail)Vehicle TypesVehicle Type - equal to: SA806 (Equipped Box Car, Inside Length:79'-Over)Page Layout for Transportation Cockpit - equal to: SAP Simplified Rail |  |  |
|  | Choose Continue | Choose Continue. | The Transportation Cockpit screen appears. |  |
|  | Select Freight Unit | On the Transportation Cockpit screen, select your freight unit in the Freight Unit Stages section. |  |  |
|  | Select the Equipment Group row | In the Railcars table select the Railcar Type row. |  |  |
|  | Choose Assign Selected Items | Choose Assign Selected Items at the top of the screen. | The following system messages appear:Freight Unit <your freight unit> assigned to Rail Freight Order (Carload)Messages for Freight Order $1 :Freight order Rail Freight Order (Carload) Order created |  |
|  | Save your entries | Save your entries. | The following system messages appear:Data saved successfullyMessages for Freight Order <your freight order number> :Business document with temporary number $1 saved as business doc. <your freight order number> |  |
|  | Note Down Your Freight Order Number | Note down your freight order number. |  |  |

#### Perform Subcontracting for Rail Freight Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Perform subcontracting and communicate the freight order details to the carrier.

You can send the freight order to the carrier by choosing Subcontracting > Send to Carrier.

Then, an EDI message is sent to the carrier, and you can't change the carrier anymore.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). |  |  |
|  | Access App | Open Manage Freight Orders(F3635). | The Manage Freight Orders(F3635) screen appears. |  |
|  | Enter Freight Order | On the Manage Freight Orders screen, make the following entries:Freight Order: <your freight order number> |  |  |
|  | Choose Go | Choose Go. | The freight order is displayed in the Freight Orders table. |  |
|  | Select the Freight Order | Select the freight order row in the Freight Orders table. | The Display Rail Freight Order (Carload) <your freight order number> screen appears. |  |
|  | Choose Edit | Choose Edit. | The Edit Rail Freight Order (Carload) <your freight order number> screen appears. |  |
|  | Navigate to the General Data Tab | Navigate to the General Data tab. |  |  |
|  | Enter Carrier, Purchasing Organization and Purchasing Group | On the Edit Rail Freight Order <your freight order number> screen, make the following entries:Carrier: 17386201 or 17386202Purchasing Organization: 1710Purchasing Group: 005Departure Date: today + 4 working daysArrival Date: today + 7 working days |  |  |
|  | Save your Entries | Save your entries. | The following system messages appear:Data saved successfullyCharge calculation completedCost distribution completed |  |
|  | Choose Subcontracting Send to Carrier | On the Edit Rail Freight Order <your freight order number> screen, choose Subcontracting > Send to Carrier . | The Warning dialog box appears. |  |
|  | Choose Ok | In the Warning dialog box, choose Ok. | The following system messages appear:Data saved successfullyFreight order sent to carrierCharge calculation completedCost distribution completed |  |

#### Receive Confirmation for Rail Freight Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If you receive a confirmation message via EDI from the carrier, this information is also stored in the freight order document and is constantly updated. Alternatively, you can set the confirmation status manually by choosing Subcontracting > Set to Confirmed by Carrier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). |  |  |
|  | Access App | Open Manage Freight Orders(F3635). | The Manage Freight Orders(F3635) screen appears. |  |
|  | Enter Freight Order | On the Manage Freight Orders screen, make the following entries:Freight Order: <your freight order number> |  |  |
|  | Choose Go | Choose Go. | The freight order is displayed in the Freight Orders table. |  |
|  | Select the Freight Order | Select the freight order row in the Freight Orders table. | The Display Rail Freight Order (Carload) <your freight order number> screen appears. |  |
|  | Choose Edit | Choose Edit. | The Edit Rail Freight Order (Carload) <your freight order number> screen appears. |  |
|  | Choose Subcontracting Set to Confirmed by Carrier | On the Edit Rail Freight Order <your freight order number> screen, choose Subcontracting > Set to Confirmed by Carrier . | Navigate to the Statuses tab.Check the following entries:Subcontracting Status: SentConfirmation Status: Confirmed |  |
|  | Save your Entries | Save your entries. | The following system messages appear:Data saved successfullyCharge calculation completedCost distribution completed |  |

#### Trigger Delivery Creation and Monitor Rail Freight Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create deliveries from the list view for selected freight orders. You can check the deliveries that have been created on the Document Flow tab. You can also navigate to the different business documents that are related to the freight document from this tab.

|  |
| --- |
| Note Note If the application job Schedule Batch Job - Create Deliveries is scheduled as described in chapter Preliminary Steps Schedule Batch Job - Create Deliveries (Optional), the deliveries are created automatically. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). |  |  |
|  | Access App | Open Manage Freight Orders(F3635). | The Manage Freight Orders(F3635) screen appears. |  |
|  | Enter Carrier and Execution Status | On the Manage Freight Orders screen, make the following entries:Carrier: 17386201 or 17386202Execution Status: Not Started |  |  |
|  | Choose Go | Choose Go. | The freight orders are displayed in the Freight Orders table. |  |
|  | Select the Freight Order Checkbox | Select the Freight Order checkbox. |  |  |
|  | Choose Create Deliveries | Choose Create Deliveries. | The following system message appears:Delivery creation triggered for <number> freight order(s) |  |
|  | Select the Freight Order (Optional) | Select the freight order row in the Freight Orders table. | The Display Rail Freight Order (Carload) <your freight order number> screen appears. |  |
|  | Check Delivery in the Document Hierarchy (Optional) | Navigate to the Document Flow tab. | The delivery document is displayed in the Document Hierarchy.Please continue with Succeeding Processes in the Appendix > Process Integration |  |

### Manual Transportation Planning Ocean Freight Booking

#### Perform Manual Transportation Planning for Ocean Freight Booking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Manual planning allows you to create or change a transportation plan. To create a transportation plan, you assign transportation demands, that is, freight unit stages, to transportation capacities, that is, equipment types, such as truck types, railcar types, or container types. The system creates capacity documents, that is, freight orders or freight bookings.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori Launchpad as a Dispatcher (TM). |  |  |
|  | Access App | Open Transportation Cockpit(/SCMTMS/PLN). | The Transportation Cockpit: Selection Criteria screen appears. |  |
|  | Enter: Selection Criteria | On the Transportation Cockpit: Selection Criteria screen, make the following entries:Freight Unit StagesBoth Locations - equal to - Select the checkbox (Both Locations)Source Location – equal to – <enter your source location>Note Note Example:SP_1710 (outbound)0017300001 (inbound)SP_1720 (stock transport order)0017186002 (customer returns)SP_171R (Returns to Supplier)Note Note Choose Insert New Row to add a new row for a new selection criterion.Destination Location – equal to – <your destination location>Note Note Example:0017186002 (outbound)SP_1710 (inbound, stock transport order)SP_171R (customer returns)0017100006 (Returns to Supplier)Planning Status of Freight Unit Stage – equal to: U (Unplanned)Transportation Mode equal to: 03 (Sea)Container TypesContainer Type – equal to: 22G0 (20 ft GP Container 20x8.6)SettingsPage Layout for Transportation Cockpit - equal to: SAP Simplified Ocean |  |  |
|  | Choose Continue | Choose Continue. | The Transportation Cockpit screen appears. |  |
|  | Select Freight Unit | On the Transportation Cockpit screen, select your freight unit in the Freight Unit Stages section. |  |  |
|  | Select the Equipment Group Row | In the Container table select the container with the container type 22G0. |  |  |
|  | Choose Assign Selected Items | Choose Assign Selected Items at the top of the screen. | The following system messages appear:Freight Unit <your freight unit> assigned to Ocean Freight BookingMessages for Freight Booking $1 :Freight booking Ocean Freight Booking created |  |
|  | Save Your Entries | Save your entries. | The following system messages appear:Data saved successfullyMessages for Freight Booking <your freight booking number> :Business document with temporary number $1 saved as business doc. <your freight order number> |  |
|  | Note Down your Ocean Freight Booking Number | Note down your ocean freight booking number. |  |  |
|  | Display Freight Booking | In the Ocean Freight Bookings table in the Freight Booking column, choose <your freight booking number>. | The Display Ocean Freight Booking <your freight booking number> screen appears. |  |
|  | Choose Edit | Choose Edit. | The Edit Ocean Freight Booking <your freight booking number> screen appears. |  |
|  | Navigate to the General Data Tab | Navigate to the General Data tab. |  |  |
|  | Enter General Data | On the General Data tab, make the following entries:TransportationCarrier:17386401 for invoice verificationor17386402 for self-billing and evaluated receipt settlementFreight Booking DataShipping Type: FCL (Full Container Load)Organizational Data:Purchasing Organization: 1710Purchasing Group: 005Pick-Up LocationDeparture Date:< today +4 working days>Delivery LocationArrival Date: <today + 4 weeks> |  |  |
|  | Choose Save and Go Back | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

#### Perform Subcontracting for Ocean Freight Booking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Perform subcontracting and communicate the freight booking details to the carrier.

You can subcontract the ocean freight booking to the carrier by choosing Subcontracting > Send Booking .

Then, an EDI message is sent to the carrier, and you can't change the carrier anymore.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). |  |  |
| 2 | Access App | Open Manage Ocean Freight Bookings (F6213) | The Manage Ocean Freight Bookings (F6213) screen appears. |  |
| 3 | Enter Freight Booking | On the Manage Ocean Freight Bookings screen, make the following entries:Ocean Freight Booking: <your freight booking number> |  |  |
| 4 | Choose Go | Choose Go. | The ocean freight booking is displayed in the Ocean Freight Bookings table. |  |
| 5 | Select the Freight Booking | Select the ocean freight booking row in the Ocean Freight Bookings table. | The Display Ocean Freight Booking <your freight booking number> screen appears. |  |
| 6 | Choose Edit | Choose Edit. | The EditOcean Freight Booking <your freight booking number> screen appears. |  |
| 7 | Choose Subcontracting Send to Carrier | On the EditOcean Freight Booking <your freight booking number> screen, choose Subcontracting > Send Booking . | The Warning dialog box appears. |  |
| 8 | Choose Ok | In the Warning dialog box, choose Ok. | The following system messages appear:Data saved successfullyFreight booking sent to carrier |  |

#### Receive Confirmation for Ocean Freight Booking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If you receive a confirmation message via EDI from the carrier, this information is also stored in the freight booking document and is constantly updated. Alternatively, you can set the confirmation status manually by choosing Subcontracting > Set to Confirmed by Carrier .

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). |  |  |
| 2 | Access App | Open Manage Ocean Freight Bookings (F6213) | The Manage Ocean Freight Bookings (F6213) screen appears. |  |
| 3 | Enter Freight Booking | On the Manage Ocean Freight Bookings screen, make the following entries:Ocean Freight Booking: <your freight booking number> |  |  |
| 4 | Choose Go | Choose Go. | The ocean freight booking is displayed in the Ocean Freight Bookings table. |  |
| 5 | Select the Freight Booking | Select the ocean freight booking row in the Ocean Freight Bookings table. | The Display Ocean Freight Booking <your freight booking number> screen appears. |  |
| 6 | Choose Edit | Choose Edit. | The EditOcean Freight Booking <your freight booking number> screen appears. |  |
| 7 | Choose Subcontracting Send to Carrier | On the Edit Ocean Freight Booking <your freight booking number> screen, choose Subcontracting > Set to Confirmed by Carrier . |  |  |
| 8 | Navigate to the General Data Tab | Navigate to the General Data tab. |  |  |
| 9 | Enter General Data | On the General Data tab, make the following entries:VoyageVoyage: <voyage number>Note Example: SAP1234567Vessel: <vessel name>Note Example: SAP CONTAINER SHIPPort of LoadingPort of Loading: <your port of loading>Note Example:Sailing Date: Departure Date + 2 working daysCargo Cut-Off Date: Departure Date +1 working dayDocument Cut-Off Date: <departure date>Port of DischargePort of Discharge: <your port of discharge>Note Example:Expected Arrival Date: Arrival Date – 2 working daysPort Pick-Up Date: Arrival Date – 1 working days |  |  |
| 10 | Scroll Down to the Items Tab | Scroll down to the Items tab. |  |  |
| 11 | Select the Container Item Checkbox | On the Freight Booking Item View in the Item Hierarchy select the container item checkbox. | The container details screen section appears below the Freight Booking Item View. |  |
| 12 | Enter Container Number | On the container details screen section, make the following entries:General DataContainer Number: <Container Number>Caution The container number needs to comply with the ISO 6346 standard.Note Example: Container Number: ANZU1234565 or ANZU6543211 |  |  |
| 13 | Scroll Down to the Stages Tab | Scroll down to the Stages tab. |  |  |
| 14 | Select the Pre-Carriage Row | In the Stages table, select the Pre-Carriage row. | The Stage Details screen section appears. |  |
| 15 | Enter Pre-CarriageTransportation ModeExecuting Carrier | In the Stages table in the Pre-Carriage row, make the following entries:Transportation Mode: RoadExecuting Carrier: 33386001 |  |  |
| 16 | Select the Main Carriage Row | In the Stages table select the Main Carriage row. | The Stage Details screen section appears. |  |
| 17 | Enter Main CarriageExecuting Carrier | In the Stages table in the Main Carriage row, make the following entries:Executing Carrier: 33386301 or 33386302 |  |  |
| 18 | Select the Radio Button in the On-Carriage Row | In the Stages table select the On-Carriage row. | The Stage Details screen section appears. |  |
| 19 | Enter On-CarriageTransportation ModeExecuting Carrier | In the Stages table in the On-Carriage row, make the following entries:Transportation Mode: 01 - RoadExecuting Carrier: 33386001 |  |  |
| 20 | Save your Entries | Save your entries. | The following system messages appear:Data saved successfullyCharge calculation completedCost distribution completed. |  |

#### Create Freight Orders for Pick-up and Delivery for Ocean Freight Booking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create freight orders for pick-up in order to transport containers from the supplier or shipping point to the loading port. Create freight orders for delivery in order to transport containers from the unloading port to the customer or receiving point. You can also select the freight order type, for example, road or rail, when you create the freight orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). |  |  |
| 2 | Access App | Open Manage Ocean Freight Bookings (F6213) | The Manage Ocean Freight Bookings (F6213) screen appears. |  |
| 3 | Enter Freight Booking | On the Manage Ocean Freight Bookings screen, make the following entries:Ocean Freight Booking: <your freight booking number> |  |  |
| 4 | Choose Go | Choose Go. | The ocean freight booking is displayed in the Ocean Freight Bookings table. |  |
| 5 | Select the Freight Booking | Select the ocean freight booking row in the Ocean Freight Bookings table. | The Display Ocean Freight Booking <your freight booking number> screen appears. |  |
| 6 | Choose Edit | Choose Edit. | The EditOcean Freight Booking <your freight booking number> screen appears. |  |
| 7 | Scroll Down to the Items Tab | Scroll down to the Items tab. |  |  |
| 8 | Select the Container Item Checkbox | On the Freight Booking Item View in the Item Hierarchy select the container item checkbox. | The container details screen section appears below the Freight Booking Item View. |  |
| 9 | Create Freight Order for Pick-Up | Choose Create > Freight Order for Pick-Up . | The following system message appears:Ocean Freight Booking <your freight booking number> assigned to Road Freight Order for Pick-Up $1 |  |
| 10 | Create Freight Order for Delivery | Choose Create > Freight Order for Delivery | The following system message appears:Ocean Freight Booking <your freight booking number> assigned to Road Freight Order for Delivery $2 |  |
| 11 | Save your Entries | Save your entries. | The following system messages appear:Data saved successfullyCharge calculation completedCost distribution completedMessages for Freight Order <your road freight order for pick-up number> :Business document with temporary number $1 saved as business doc. <your road freight order for pick-up number>Messages for Freight Order <your road freight order for delivery number> :Business document with temporary number $2 saved as business doc. <your road freight order for delivery number> |  |
| 12 | Note Down the Freight Order Numbers for Pick-up and Delivery | Note down the freight order numbers for pick-up and delivery. |  |  |

#### Display Pick-up and Delivery Freight Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Display freight orders for pick-up in order to transport containers from the supplier or shipping point to the loading port.

Display freight orders for delivery in order to transport containers from the unloading port to the customer or receiving point.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). |  |  |
| 2 | Access App | Open Manage Freight Orders (F3635). | The Manage Freight Orders (F3635) screen appears. |  |
| 3 | Enter Freight Order | On the Manage Freight Orders screen, make the following entries:Freight Order: <your freight order for pick-up number> or <your freight order for delivery number> |  |  |
| 4 | Choose Go | Choose Go. | The freight order is displayed in the Freight Orders table. |  |
| 5 | Select the Freight Order | Select the freight order row in the Freight Orders table. | The Display Road or Rail Freight Order <your freight order number> screen appears. |  |

#### Trigger Delivery Creation and Monitor Ocean Freight Booking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create deliveries for a selected ocean freight booking.

|  |
| --- |
| Note If the application job Schedule Batch Job - Create Deliveries is scheduled as described in chapter Preliminary Steps Schedule Batch Job - Create Deliveries (Optional), the deliveries are created automatically. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). |  |  |
| 2 | Access App | Open Manage Ocean Freight Bookings (F6213). | The Manage Ocean Freight Bookings (F6213) screen appears. |  |
| 3 | Enter Freight Booking | On the Manage Ocean Freight Bookings screen, make the following entries:Ocean Freight Booking: <your freight booking number> |  |  |
| 4 | Choose Go | Choose Go. | The ocean freight booking is displayed in the Ocean Freight Bookings table. |  |
| 5 | Select the Ocean Freight Booking Checkbox | Select the Ocean Freight Booking checkbox. |  |  |
| 6 | Choose Create Deliveries | Choose Create Deliveries. | The following system message appears:Delivery creation triggered for <number> freight order(s) |  |
| 7 | Select the Ocean Freight Booking (Optional) | Select the Ocean Freight Booking row in the Ocean Freight Booking table. | The Display Ocean Freight Booking <your freight booking number> screen appears. |  |
| 8 | Check Delivery in the Document Hierarchy (Optional) | Navigate to the Document Flow tab. | The delivery document is displayed in the Document Hierarchy.Please continue with Succeeding Processes in the Appendix > Process Integration |  |

### Manual Transportation Planning Air Freight Booking

#### Perform Manual Transportation Planning for Air Freight Booking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Manual planning allows you to create or change a transportation plan. To create a transportation plan, you assign transportation demands, that is, freight unit stages, to transportation capacities, that is, equipment types, such as truck types, railcar types, or container types. The system creates capacity documents, that is, freight orders or freight bookings.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Dispatcher (TM). |  |  |
| 2 | Access App | Open Transportation Cockpit (/SCMTMS/PLN). | The Transportation Cockpit: Selection Criteria screen appears. |  |
| 3 | Enter: Selection Criteria | On the Transportation Cockpit: Selection Criteria screen, make the following entries:Freight Unit StagesBoth Locations - equal to - Select the checkbox (Both Locations)Source Location – equal to – <enter your source location>Note Example:SP_3310 (outbound)0033300001 (inbound)SP_3320 (stock transport order)33186002 (customer returns)SP_331R (Returns to Supplier)Note Choose Insert New Row to add a new row for a new selection criterion.Destination Location – equal to – <your destination location>Note Example:33186002 (outbound)SP_3310 (inbound, stock transport order)SP_331R (customer returns)33100006 (Returns to Supplier)Planning Status of Freight Unit Stage – equal to: U (Unplanned)Transportation Mode equal to: 05 (Air)SettingsPage Layout for Transportation Cockpit - equal to: SAP Simplified Air |  |  |
| 4 | Choose Continue | Choose Continue. | The Transportation Cockpit screen appears. |  |
| 5 | Select Freight Unit | On the Transportation Cockpit screen, select your freight unit in the Freight Unit Stages section. |  |  |
| 6 | Create Air Freight Booking | Choose Create Air Freight Booking. | The following system messages appear:Freight Unit <your freight unit> assigned to Air Freight BookingMessages for Freight Booking $1 :Freight booking Air Freight Booking created |  |
| 7 | Save your Entries | Save your entries. | The following system messages appear:Data saved successfullyMessages for Freight Booking <your freight booking number> :Business document with temporary number $1 saved as business doc. <your freight order number> |  |
| 8 | Note Down your Air Freight Booking Number | Note down your air freight booking number. |  |  |
| 9 | Display Freight Booking | In the Air Freight Bookings table in the Freight Booking column, choose <your freight booking number>. | The Display Air Freight Booking <your freight booking number> screen appears. |  |
| 10 | Choose Edit | Choose Edit. | The Edit Air Freight Booking <your freight booking number> screen appears. |  |
| 11 | Navigate to the General Data Tab | Navigate to the General Data tab. |  |  |
| 12 | Enter General Data | On the General Data tab, make the following entries:TransportationCarrier:33386401 for invoice verificationor33386402 for self-billing and evaluated receipt settlementOrganizational Data:Purchasing Organization: 3310Purchasing Group: 005Pick-Up LocationDeparture Date:<today +4 working days>Delivery LocationArrival Date: <today + 7 working days> |  |  |
| 13 | Choose Save and Go Back | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

#### Perform Subcontracting for Air Freight Booking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Perform subcontracting and communicate the freight booking details to the carrier.

You can subcontract the air freight booking to the carrier by choosing Subcontracting > Send Booking .

Then, an EDI message is sent to the carrier, and you can't change the carrier anymore.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). |  |  |
| 2 | Access App | Open Manage Air Freight Bookings (F6535). | The Manage Air Freight Bookings (F6535) screen appears. |  |
| 3 | Enter Freight Booking | On the Manage Air Freight Bookings screen, make the following entries:Air Freight Booking: <your freight booking number> |  |  |
| 4 | Choose Go | Choose Go. | The air freight booking is displayed in the Air Freight Bookings table. |  |
| 5 | Select the Freight Booking | Select the air freight booking row in the Air Freight Bookings table. | The Display Air Freight Booking <your freight booking number> screen appears. |  |
| 6 | Choose Edit | Choose Edit. | The EditAir Freight Booking <your freight booking number> screen appears. |  |
| 7 | Choose Subcontracting Send to Carrier | On the Edit Air Freight Booking <your freight booking number> screen, choose Subcontracting > Send Booking . | The Warning dialog box appears. |  |
| 8 | Choose Ok | In the Warning dialog box, choose Ok. | The following system messages appear:Data saved successfullyFreight booking sent to carrier |  |

#### Receive Confirmation for Air Freight Booking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If you receive a confirmation message via EDI from the carrier, this information is also stored in the freight booking document and is constantly updated. Alternatively, you can set the confirmation status manually by choosing Subcontracting > Set to Confirmed by Carrier .

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). |  |  |
| 2 | Access App | Open Manage Air Freight Bookings (F6535) | The Manage Air Freight Bookings (F6535) screen appears. |  |
| 3 | Enter Freight Booking | On the Manage Air Freight Bookings screen, make the following entries:Air Freight Booking: <your freight booking number> |  |  |
| 4 | Choose Go | Choose Go. | The air freight booking is displayed in the Air Freight Bookings table. |  |
| 5 | Select the Freight Booking | Select the air freight booking row in the Air Freight Bookings table. | The Display Air Freight Booking <your freight booking number> screen appears. |  |
| 6 | Choose Edit | Choose Edit. | The Edit Air Freight Booking <your freight booking number> screen appears. |  |
| 7 | Choose Subcontracting Send to Carrier | On the Edit Air Freight Booking <your freight booking number> screen, choose Subcontracting > Set to Confirmed by Carrier . |  |  |
| 8 | Navigate to the General Data Tab | Navigate to the General Data tab. |  |  |
| 9 | Enter General Data | On the General Data tab, make the following entries:Note The Arrival Date is displayed in the Delivery Location section.Airport of Departure: <your airport of departure>Expected Departure Date: <Arrival Date - 1 day>Expected Departure Time: 12:00:00 AMCargo Cut-Off Date: <Arrival Date - 2 days>Airport of DestinationAirport of Destination: <your airport of destination>Expected Arrival Date: <Arrival Date – 1 day>Expected Arrival Time: 13:30:00Availability Date: <Arrival Date> |  |  |
| 10 | Choose Enter | Choose Enter. |  |  |
| 11 | Scroll Down to the Stages Tab | Scroll down to the Stages tab. |  |  |
| 12 | Select the Radio Button in the Pre-Carriage Row | In the Stages table, select the radio button in the Pre-Carriage row. | The Stage Details screen section appears. |  |
| 13 | Enter Pre-Carriage, Transportation Mode and Executing Carrier | In the Stages table in the Pre-Carriage row, make the following entries:Transportation Mode: RoadExecuting Carrier: 33386001 |  |  |
| 14 | Select the Radio Button in the Main Carriage Row | In the Stages table, select the radio button in the Main Carriage row. | The Stage Details screen section appears. |  |
| 15 | Enter Main Carriage and Executing Carrier | In the Stages table in the Main Carriage row, make the following entries:Executing Carrier: 33386501 or 10386502 |  |  |
| 16 | Select the Radio Button in the On-Carriage Row | In the Stages table select the radio button in the On-Carriage row. | The Stage Details screen section appears. |  |
| 17 | Enter On-Carriage, Transportation Mode, and Executing Carrier | In the Stages table in the On-Carriage row, make the following entries:Transportation Mode: RoadExecuting Carrier: 33386001 |  |  |
| 18 | Save your Entries | Save your entries. | The following system messages appear:Data saved successfullyCharge calculation completedCost distribution completed |  |

#### Create Freight Orders for Pick-up and Delivery for Air Freight Booking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create freight orders for pick-up in order to transport loose cargo from the supplier or shipping point to the airport of departure or airport of destination.

Create freight orders for delivery in order to transport loose cargo from the airport of destination to the customer or receiving point.

You can select the freight order type, for example, road or rail, when you create the freight orders for pick-up and delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). |  |  |
| 2 | Access App | Open Manage Air Freight Bookings (F6535) | The Manage Air Freight Bookings (F6535) screen appears. |  |
| 3 | Enter Freight Booking | On the Manage Air Freight Bookings screen, make the following entries:Air Freight Booking: <your freight booking number> |  |  |
| 4 | Choose Go | Choose Go. | The air freight booking is displayed in the Air Freight Bookings table. |  |
| 5 | Select the Freight Booking | Select the air freight booking row in the Air Freight Bookings table. | The Display Air Freight Booking <your freight booking number> screen appears. |  |
| 6 | Choose Edit | Choose Edit. | The EditAir Freight Booking <your freight booking number> screen appears. |  |
| 7 | Scroll Down to the Items Tab. | Scroll down to the Items tab. |  |  |
| 8 | Select the Product Item Checkbox | On the Freight Booking Item View in the Item Hierarchy select the product item checkbox. | The product details screen section appears below the Freight Booking Item View. |  |
| 9 | Create Freight Order for Pick-Up | Choose Create > Freight Order for Pick-Up . | The following system message appears:Air Freight Booking <your freight booking number> assigned to Road Freight Order for Pick-Up $1 |  |
| 10 | Create Freight Order for Delivery | Choose Create > Freight Order for Delivery | The following system message appears:Air Freight Booking <your freight booking number> assigned to Road Freight Order for Delivery $2 |  |
| 11 | Save your Entries | Save your entries. | The following system messages appear:Data saved successfullyCharge calculation completedCost distribution completedMessages for Freight Order <your road freight order for pick-up number> :Business document with temporary number $1 saved as business doc. <your road freight order for pick-up number>Messages for Freight Order <your road freight order for delivery number> :Business document with temporary number $2 saved as business doc. <your road freight order for delivery number> |  |
| 12. | Note Down the Freight Order Numbers for Pick-up and Delivery. | Note down the freight order numbers for pick-up and delivery. |  |  |

#### Display Pick-up and Delivery Freight Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Display freight orders for pick-up in order to transport loose cargo from the supplier or shipping point to the airport of departure.

Display freight orders for delivery in order to transport loose cargo from the airport of destination to the customer or receiving point.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). |  |  |
| 2 | Access App | Open Manage Freight Orders (F3635). | The Manage Freight Orders (F3635) screen appears. |  |
| 3 | Enter Freight Order | On the Manage Freight Orders screen, make the following entries:Freight Order: <your freight order for pick-up number> or <your freight order for delivery number> |  |  |
| 4 | Choose Go | Choose Go. | The freight order is displayed in the Freight Orders table. |  |
| 5 | Select the Freight Order | Select the freight order row in the Freight Orders table. | The Display Road or Rail Freight Order <your freight order number> screen appears. |  |

#### Trigger Delivery Creation and Monitor Air Freight Booking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create deliveries for selected air freight booking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). |  |  |
| 2 | Access App | Open Manage Air Freight Bookings (F6535) | The Manage Air Freight Bookings (F6535) screen appears. |  |
| 3 | Enter Freight Booking | On the Manage Air Freight Bookings screen, make the following entries:Air Freight Booking: <your freight booking number> |  |  |
| 4 | Choose Go | Choose Go. | The air freight booking is displayed in the Air Freight Bookings table. |  |
| 5 | Select the Air Freight Booking Checkbox | Select the Air Freight Booking checkbox. |  |  |
| 6 | Choose Create Deliveries | Choose Create Deliveries. | The following system message appears:Delivery creation triggered for <number> freight order(s) |  |
| 7 | Select the Air Freight Booking (Optional) | Select the Air Freight Booking row in the Air Freight Booking table. | The Display Air Freight Booking <your freight booking number> screen appears. |  |
| 8 | Check Delivery in the Document Hierarchy (Optional) | Navigate to the Document Flow tab. | The delivery document is displayed in the Document Hierarchy.Please continue with Succeeding Processes in the Appendix > Process Integration |  |

### Perform Manual Transportation Planning for Advanced Intercompany Business Processes

#### Perform Manual Transportation Planning Pick-Up and Main Stages for Advanced Intercompany Business Processes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Manual planning allows you to create or change a transportation plan. To create a transportation plan, you assign transportation demands, that is, freight unit stages, to transportation capacities, that is, equipment types, such as truck types, railcar types, or container types. The system creates capacity documents, that is, freight orders or freight bookings.

Advanced Intercompany Sales (Scope Item 5D2)

The process for advanced intercompany sales provides functions that allow two affiliated companies to participate in a single intercompany process.

A sales organization assigned to the selling company creates a standard sales order, ordering goods from a plant assigned to another company code, which acts as the delivering company. The delivering company delivers the goods to the customer.

The pick-up and main stages are planned by the person with the Dispatcher (TM) role in the delivering company.

The delivery stage is planned by the person with the Dispatcher (TM) role in the selling company.

Advanced Intercompany Stock Transfer (Scope Item 5HP)

A purchasing organization assigned to the receiving company code creates an intercompany purchase order, ordering goods from a plant assigned to another company code.

The plant in the delivering company code delivers the goods to the plant for which the purchasing organization ordered the goods.

During manual planning Advanced Intercompany Business Processes, the system makes sure that two freight unit stages with different paying company codes are not planned on the same freight document.

The pick-up and main stages are planned by the person with the Dispatcher (TM) role in the delivering company.

The delivery stage is planned by the person with the Dispatcher (TM) role in the selling / receiving company.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Dispatcher (TM). |  |  |
| 2 | Access App | Open Transportation Cockpit (/SCMTMS/PLN). | The Transportation Cockpit: Selection Criteria screen appears. |  |
| 3 | Enter: Selection Criteria | On the Transportation Cockpit: Selection Criteria screen, make the following entries:Freight Unit StagesSource Location – equal to – SP_1710Paying Company Code: 1710Note Choose Insert New Row to add a new row for a new selection criterion.Planning Status of Freight Unit Stage – equal to: U (Unplanned)Note Alternatively, you can add the following filter criteria to make a unique selection:Freight Unit equal to: <freight unit number created before>.Container TypesContainer Type – equal to – 22G0 (20 ft GP Container 20x8.6)SettingsPage Layout for Transportation Cockpit - equal to: SAP Simplified Ocean |  |  |
| 4 | Choose Continue | Choose Continue. | The Transportation Cockpit screen appears. |  |
| 5 | Select Freight Unit | On the Transportation Cockpit screen, select your freight unit in the Freight Unit Stages section. |  |  |
| 6 | Select the Equipment Group Row | In the Container table select the container with the container type 22G0. |  |  |
| 7 | Choose Assign Selected Items | Choose Assign Selected Items at the top of the screen. | The following system messages appear:Freight Unit <your freight unit> assigned to Ocean Freight BookingMessages for Freight Booking $1 :Freight booking Ocean Freight Booking created |  |
| 8 | Save your Entries | Save your entries. | The following system messages appear:Data saved successfullyMessages for Freight Booking <your freight booking number> :Business document with temporary number $1 saved as business doc. <your freight order number> |  |
| 9 | Note Down your Ocean Freight Booking Number | Note down your ocean freight booking number. |  |  |
| 10 | Display Freight Booking | In the Ocean Freight Bookings table in the Freight Booking column, choose <your freight booking number>. | The Display Ocean Freight Booking <your freight booking number> screen appears. |  |
| 11 | Choose Edit | Choose Edit. | The Edit Ocean Freight Booking <your freight booking number> screen appears. |  |
| 12 | Navigate to the General Data Tab | Navigate to the General Data tab. |  |  |
| 13 | Enter General Data | On the General Data tab, make the following entries:TransportationCarrier:17386401 for invoice verificationNote Here a carrier which is assigned to the delivering company’s purchasing organization is used.Freight Booking DataShipping Type: FCL (Full Container Load)Organizational Data:Purchasing Organization: 1710Note Here the delivering company’s purchasing organization is used.Purchasing Group: 005Pick-Up LocationDeparture Date:< today +4 working days>Port of DischargeExpected Arrival Date: <requested start date (destination) of your freight unit minus 2 working days> |  |  |
| 14 | Choose Save and Go Back. | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

#### Perform Subcontracting Pick-Up and Main Stage for Advanced Intercompany Business Processes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Perform subcontracting and communicate the freight booking details to the carrier.

The pick-up and main stages for Advanced Intercompany Business Processes are planned by the person with theDispatcher (TM) role in the delivering company.

You can subcontract the ocean freight booking to the carrier by choosing Subcontracting > Send Booking .

Then, an EDI message is sent to the carrier, and you can't change the carrier anymore.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). |  |  |
| 2 | Access App | Open Manage Ocean Freight Bookings (F6213) | The Manage Ocean Freight Bookings (F6213) screen appears. |  |
| 3 | Enter Freight Booking | On the Manage Ocean Freight Bookings screen, make the following entries:Ocean Freight Booking: <your freight booking number> |  |  |
| 4 | Choose Go | Choose Go. | The ocean freight booking is displayed in the Ocean Freight Bookings table. |  |
| 5 | Select the Freight Booking | Select the ocean freight booking row in the Ocean Freight Bookings table. | The Display Ocean Freight Booking <your freight booking number> screen appears. |  |
| 6 | Choose Edit | Choose Edit. | The EditOcean Freight Booking <your freight booking number> screen appears. |  |
| 7 | Choose Subcontracting Send to Carrier | On the EditOcean Freight Booking <your freight booking number> screen, choose Subcontracting > Send Booking . | The Warning dialog box appears. |  |
| 8 | Choose Ok | In the Warning dialog box, choose Ok. | The following system messages appear:Data saved successfullyFreight booking sent to carrier |  |

#### Receive Booking Confirmation Pick-Up and Main Stage for Advanced Intercompany Business Processes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If you receive a confirmation message via EDI from the carrier, this information is also stored in the freight booking document and is constantly updated. Alternatively, you can set the confirmation status manually by choosing Subcontracting > Set to Confirmed by Carrier .

The pick-up and main stages for Advanced Intercompany Business Processes are planned by the person with theDispatcher (TM) role in the delivering company.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). |  |  |
| 2 | Access App | Open Manage Ocean Freight Bookings (F6213). | The Manage Ocean Freight Bookings (F6213) screen appears. |  |
| 3 | Enter Freight Booking | On the Manage Ocean Freight Bookings screen, make the following entries:Ocean Freight Booking: <your freight booking number> |  |  |
| 4 | Choose Go | Choose . | The ocean freight booking is displayed in the Ocean Freight Bookings table. |  |
| 5 | Select the Freight Booking | Select the ocean freight booking row in the Ocean Freight Bookings table. | The Display Ocean Freight Booking <your freight booking number> screen appears. |  |
| 6 | Choose Edit | Choose Edit. | The EditOcean Freight Booking <your freight booking number> screen appears. |  |
| 7 | Choose Subcontracting Send to Carrier | On the Edit Ocean Freight Booking <your freight booking number> screen, choose Subcontracting > Set to Confirmed by Carrier . |  |  |
| 8 | Navigate to the General Data Tab | Navigate to the General Data tab. |  |  |
| 9 | Enter General Data | On the General Data tab, make the following entries:VoyageVoyage: <voyage number>Note Example: SAP1234567Vessel: <vessel name>Note Example: SAP CONTAINER SHIPPort of LoadingNote The sea voyage starts in a port which can be reached by a truck form the delivering plant of the delivering company code.Sailing Date: Departure Date + 2 working daysCargo Cut-Off Date: Departure Date +1 working dayDocument Cut-Off Date: <departure date>Port of DischargeExpected Arrival Date: Arrival Date – 2 working daysPort Pick-Up Date: Arrival Date – 1 working days |  |  |
| 10 | Scroll Down to the Items Tab | Scroll down to the Items tab. |  |  |
| 11 | Select the Container Item Checkbox | On the Freight Booking Item View in the Item Hierarchy select the container item checkbox. | The container details screen section appears below the Freight Booking Item View. |  |
| 12 | Enter Container Number | On the container details screen section, make the following entries:General DataContainer Number: <Container Number>Caution The container number needs to comply with the ISO 6346 standard.Note Example: Container Number: ANZU1234565 or ANZU6543211 |  |  |
| 13 | Scroll Down to the Stages Tab | Scroll down to the Stages tab. |  |  |
| 14 | Select the Radio Button in the Pre-Carriage Row | In the Stages table select the Pre-Carriage row. | The Stage Details screen section appears. |  |
| 15 | Enter Pre-Carriage, Transportation Mode, and Executing Carrier | In the Stages table in the Pre-Carriage row, make the following entries:Transportation Mode: RoadExecuting Carrier: 17386001Note Here a carrier which is assigned to the delivering company’s purchasing organization is used. |  |  |
| 16 | Select the Radio Button in the Main Carriage Row | In the Stages table select the Main Carriage row. | The Stage Details screen section appears. |  |
| 17 | Enter Main CarriageExecuting Carrier | In the Stages table in the Main Carriage row, make the following entries:Executing Carrier: 17386301Note Here a carrier which is assigned to the delivering company’s purchasing organization is used. |  |  |
| 18 | Save your Entries | Save your entries.Note The on-carriage stage is planned later by the receiving company’s dispatcher. | The following system messages appear:Data saved successfully.Charge calculation completed. |  |

#### Create Freight Order for Pick-Up for Advanced Intercompany Business Processes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create freight orders for pick-up in order to transport containers from the supplier or shipping point to the loading port. You can also select the freight order type, for example, road or rail, when you create the freight orders.

The pick-up and main stages for Advanced Intercompany Business Processes are planned by the person with the Dispatcher (TM) role in the delivering company.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). |  |  |
| 2 | Access App | Open Manage Ocean Freight Bookings (F6213). | The Manage Ocean Freight Bookings (F6213) screen appears. |  |
| 3 | Enter Freight Booking | On the Manage Ocean Freight Bookings screen, make the following entries:Ocean Freight Booking: <your freight booking number> |  |  |
| 4 | Choose Go | Choose Go. | The ocean freight booking is displayed in the Ocean Freight Bookings table. |  |
| 5 | Select the Freight Booking | Select the ocean freight booking row in the Ocean Freight Bookings table. | The Display Ocean Freight Booking <your freight booking number> screen appears. |  |
| 6 | Choose Edit | Choose Edit. | The EditOcean Freight Booking <your freight booking number> screen appears. |  |
| 7 | Scroll Down to the Items tab | Scroll down to the Items tab. |  |  |
| 8 | Select the Container Item Checkbox | On the Freight Booking Item View in the Item Hierarchy select the container item checkbox. | The Container Details screen section appears below the Freight Booking Item View. |  |
| 9 | Create Freight Order for Pick-Up | Choose Create > Freight Order for Pick-Up . | The following system message appears:Ocean Freight Booking <your freight booking number> assigned to Road Freight Order for Pick-Up $1 |  |
| 10 | Save your Entries | Save your entries. | The following system messages appear:Data saved successfullyCharge calculation completedCost distribution completedMessages for Freight Order <your road freight order for pick-up number> :Business document with temporary number $1 saved as business doc. <your road freight order for pick-up number> |  |
| 11 | Note Down the Freight Order Numbers for Pick-up. | Note down the freight order numbers for pick-up. |  |  |

#### Display Freight Order for Pick-Up for Advanced Intercompany Business Processes (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Display freight orders for pick-up in order to transport containers from the supplier or shipping point to the loading port.

The pick-up and main stages for Advanced Intercompany Business Processes are planned by the person with the Dispatcher (TM) role in the delivering company.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). |  |  |
| 2 | Access App | Open Manage Freight Orders (F3635). | The Manage Freight Orders (F3635) screen appears. |  |
| 3 | Enter Freight Order | On the Manage Freight Orders screen, make the following entries:Freight Order: <your freight order for pick-up number> |  |  |
| 4 | Choose Go | Choose Go. | The freight order is displayed in the Freight Orders table. |  |
| 5 | Select the Freight Order | Select the freight order row in the Freight Orders table. | The Display Road or Rail Freight Order <your freight order number> screen appears. |  |

#### Trigger Delivery Creation and Monitor Ocean Freight Booking Advanced Intercompany Business Processes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create deliveries for selected ocean freight bookings.

|  |
| --- |
| Note If the application job Schedule Batch Job - Create Deliveries is scheduled as described in chapter Schedule Batch Job - Create Deliveries (Optional), the deliveries are created automatically. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). |  |  |
| 2 | Access App | Open Manage Ocean Freight Bookings (F6213). | The Manage Ocean Freight Bookings (F6213) screen appears. |  |
| 3 | Enter Freight Booking | On the Manage Ocean Freight Bookings screen, make the following entries:Ocean Freight Booking: <your freight booking number> |  |  |
| 4 | Choose Go | Choose Go. | The ocean freight booking is displayed in the Ocean Freight Bookings table. |  |
| 5 | Select the Ocean Freight Booking Checkbox | Select the Ocean Freight Booking checkbox. |  |  |
| 6 | Choose Create Deliveries | Choose Create Deliveries. | The following system message appears:Delivery creation triggered for <number> freight order(s) |  |
| 7 | Select the Ocean Freight Booking (Optional) | Select the Ocean Freight Booking row in the Ocean Freight Booking table. | The Display Ocean Freight Booking <your freight booking number> screen appears. |  |
| 8 | Check Delivery in the Document Hierarchy (Optional) | Navigate to the Document Flow tab. | The delivery document is displayed in the Document Hierarchy. |  |

#### Perform Manual Transportation Planning Delivery Stage for Advanced Intercompany Business Processes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Manual planning allows you to create or change a transportation plan. To create a transportation plan, you assign transportation demands, that is, freight unit stages, to transportation capacities, that is, equipment types, such as truck types, railcar types, or container types. The system creates capacity documents, that is, freight orders or freight bookings.

During manual planning Advanced Intercompany Business Processes, the system makes sure that two freight unit stages with different paying company codes are not planned on the same freight document.

The pick-up and main stages for Advanced Intercompany Business Processes are planned by the person with the Dispatcher (TM) role in the delivering company.

The delivery stage for Advanced Intercompany Business Processes is planned by the person with the Dispatcher (TM) role in the selling company.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Dispatcher (TM). |  |  |
| 2 | Access App | Open Transportation Cockpit (/SCMTMS/PLN). | The Transportation Cockpit: Selection Criteria screen appears. |  |
| 3 | Enter: Selection Criteria | On the Transportation Cockpit: Selection Criteria screen, make the following entries:Freight Unit StagesPaying Company Code: 3310Note Choose Insert New Row to add a new row for a new selection criterion.Planning Status of Freight Unit Stage – equal to: U (Unplanned)Note Alternatively, you can add the following filter criteria to make a unique selection:Freight Unit equal to: <freight unit number created before>.Vehicle TypesVehicle Type – equal to - STR400 (Vehicle 40.0 t)SettingsPage Layout for Transportation Cockpit - equal to: SAP Simplified TC |  |  |
| 4 | Choose Continue | Choose Continue. | The Transportation Cockpit screen appears. |  |
| 5 | Select Freight Unit | On the Transportation Cockpit screen, select your freight unit in the Freight Unit Stages section. |  |  |
| 6 | Select the Equipment Group row | In the Trucks table select the Equipment Group row. |  |  |
| 7 | Choose Assign Selected Items | Choose Assign Selected Items at the top of the screen.Caution If the following system message appears: Freight Unit <your freight unit>: Acceptable times for pickup/del. at <your source location> at <date and time> is outside plan. horizon. adapt the planning horizon by choosing Change Planning Settings | The following system messages appear:Freight Unit <your freight unit> assigned to Road Freight OrderMessages for Freight Order $1 :Freight order Road Freight Order created |  |
| 8 | Save your Entries | Save your entries. | The following system messages appear:Data saved successfullyMessages for Freight Order <your freight order number> :Business document with temporary number $1 saved as business doc. <your freight order number> |  |
| 9 | Note Down your Freight Order Number | Note down your freight order number. |  |  |
| 10 | Choose <your Freight Order Number> | In the Road Freight Orders table in the Freight Order column choose <your freight order number>. | The Display Road Freight Order <your freight order number> screen appears. |  |
| 11 | Choose Edit | Choose Edit. | The Edit Road Freight Order <your freight order number> screen appears. |  |
| 12 | Navigate to the General Data tab | Navigate to the General Data tab. |  |  |
| 13 | Enter General Data | On the General Data tab, make the following entries:TransportationCarrier: 33386001 or 33386002.Note Here a carrier which is assigned to the receiving company’s purchasing organization is used.Organizational DataPurchasing Organization: 3310Note Here the receiving company’s purchasing organization is used.Purchasing Group: 005 |  |  |
| 14 | Scroll Down to the Items Tab | Scroll down to the Items tab. |  |  |
| 15 | Choose Insert Container | In the Insert: drop down list box choose Insert Container. | A container item is displayed in the Item Hierarchy column. |  |
| 16 | Enter Container Details | Select the container item.On the Details tab, make the following entries (as maintained in the freight booking):Container Number: ANZU1234565 or ANZU6543211Equipment Group: SCNEquipment Type: 22G0 |  |  |
| 17 | Select the Freight Unit | Select the Freight Unit <your freight unit number> checkbox. |  |  |
| 18 | Drag and Drop the Freight Unit onto the Container Item | Drag and drop the freight unit onto the container item. | The freight unit is now displayed within the hierarchy of the container item. |  |
| 19 | Choose Save and Go Back | Choose Save and go back. | The following system messages appear:Data saved successfullyCharge calculation completedCost distribution completed |  |

#### Perform Subcontracting Delivery Stage for Advanced Intercompany Business Processes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Perform subcontracting and communicate the freight order details to the carrier.

You can send the freight order to the carrier by choosing Subcontracting > Send to Carrier.

Then, an EDI message is sent to the carrier, and you can't change the carrier anymore.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). |  |  |
| 2 | Access App | Open Manage Freight Orders (F3635). | The Manage Freight Orders (F3635) screen appears. |  |
| 3 | Enter Freight Order | On the Manage Freight Orders screen, make the following entries:Freight Order: <your freight order number> |  |  |
| 4 | Choose Go | Choose Go. | The freight order is displayed in the Freight Orders table. |  |
| 5 | Select the Freight Order | Select the freight order row in the Freight Orders table. | The Display Road Freight Order <your freight order number> screen appears. |  |
| 6 | Choose Edit | Choose Edit. | The Edit Road Freight Order <your freight order number> screen appears. |  |
| 7 | Choose Subcontracting Send to Carrier | On the Edit Road Freight Order <your freight order number screen, choose Subcontracting > Send to Carrier. | The Warning dialog box appears. |  |
| 8 | Choose Ok | In the Warning dialog box, choose Ok. | The following system messages appear:Data saved successfullyFreight order sent to carrierCharge calculation completedCost distribution completed |  |

#### Receive Freight Order Confirmation Delivery Stage for Advanced Intercompany Business Processes

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). |  |  |
| 2. | Access App | Open Manage Freight Orders (F3635). | The Manage Freight Orders (F3635) screen appears. |  |
| 3. | Enter Freight Order | On the Manage Freight Orders screen, make the following entries:Freight Order: <your freight order number> |  |  |
| 4. | Choose Go | Choose Go. | The freight order is displayed in the Freight Orders table. |  |
| 5. | Select the Freight Order | Select the freight order row in the Freight Orders table. | The Display Road Freight Order <your freight order number> screen appears. |  |
| 6. | Choose Edit | Choose Edit. | The Edit Road Freight Order <your freight order number> screen appears. |  |
| 7. | Choose Subcontracting Set to Confirmed by Carrier | On the Edit Road Freight Order <your freight order number> screen, choose Subcontracting > Set to Confirmed by Carrier. | Navigate to the Statuses tab.Check the following entries:Subcontracting Status: SentConfirmation Status: Confirmed. |  |
| 8. | Save your Entries | Save your Entries. | The following system messages appear:Data saved successfullyCharge calculation completedCost distribution completedContinue with the Succeeding Processes in the Appendix > Succeding Processes. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can proceed this process.

| Process | Business Condition |
| --- | --- |
| BD9 - Sell from Stock | Create a sales order |
| 3NR – Sales Scheduling Agreements | Create a sales scheduling agreementUpdate the scheduling agreement for forecast delivery schedule manuallyGenerate the planning delivery schedule |
| 2TX - Direct Procurement with Inbound Delivery | Create a purchase order |
| BME - Stock Transfer with Delivery | Create a stock transport order |
| BDD - Lean Customer Returns | Create a returns order |
| 3BS - Warehouse Outbound Processing | Create a sales order for warehouse-managed storage location 335W |
| 5D2 - Advanced Intercompany Sales | Create an intercompany sales order |
| 5HP - Advanced Intercompany Stock Transfer | Create an intercompany stock transfer order |
| BMK - Return to Supplier | Create a return purchase order |
| BMY - Subcontracting | Create subcontracting purchase orderCreate Outbound Delivery |
| 1IU - Customer Consignment | Create Customer Fill-Up OrderCreate Customer Pick-Up Order |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| BD9 - Sell from Stock | Execute picking after delivery creation triggered by freight document (for all delivery documents created).Continue with executing the test procedure for outbound process with used mode of transport in scope item 6W3 - Transportation Execution. |
| 3NR – Sales Scheduling Agreements | Execute picking after delivery creation triggered by freight document.Continue with executing the test procedure for outbound process with used mode of transport in scope item 6W3 - Transportation Execution. |
| 6W3 - Transportation Execution | Continue with executing the test procedure for the inbound process with the used mode of transport from 6W2 in scope item 6W3 - Transportation ExecutionInbound process predecessor scope items are:2TX - Direct Procurement with Inbound DeliveryBDD - Lean Customer ReturnsBMY - Subcontracting InboundContinue with executing the test procedure for inbound process with used mode of transport in scope item 6W3 - Transportation Execution. |
| BME - Stock Transfer with Delivery | Pick and post goods issue for stock transport order after delivery creation triggered by freight document.Execute the test steps 1 to 4 (Picking) and save your changes.Continue with executing the test procedure for stock transfer process with the used mode of transport in scope item 6W3 -Transportation Execution. |
| 3BS - Warehouse Outbound Processing | Perform the Set to Arrived and Check In at the Shipping Point steps in scope item 6W3 - Transportation Execution.Perform test procedures Create Pick Warehouse Tasks until Print Loading Instruction (Optional) after delivery creation triggered by freight document.Continue with executing in the test procedure for outbound process from the Loading step with the mode of transport used in scope item 6W3 - Transportation Execution. |
| 5D2 - Advanced Intercompany Sales | Perform picking after delivery creation triggered by freight document.Continue with executing the test procedure for advanced intercompany sales process in scope item 6W3 - Transportation Execution. |
| 5HP - Advanced Intercompany Stock Transfer | Perform picking in pick and post goods issue for outbound delivery after delivery creation triggered by freight document.Continue with executing the test procedure for advanced intercompany stock transfer process in scope item 6W3 - Transportation Execution. |
| BMK - Return to Supplier | Execute picking after delivery creation triggered by freight document.Continue with executing the test procedure for outbound process with used mode of transport in scope item 6W3 - Transportation Execution. |
| BMY - Subcontracting | Outbound: Execute the test steps 1 to 4 (picking) as described in chapter Pick and Post Goods Issue in scope item BMY - Subcontracting. Goods issue will be described in scope item 6W3 - Transportation Execution.Continue with executing the test procedure for outbound process with mode of transport Road in scope item 6W3 - Transportation Execution.Make sure to perform the planning for both outbound and inbound processes. |
| 1IU - Customer Consignment | Consignment Fill-Up Order:Execute Pick Goods after delivery creation triggered by freight document.Continue executing the test procedure for outbound process with used mode of transport in scope item 6W3 - Transportation Execution.Consignment Pick-Up Order:Continue executing the test procedure for inbound process with used mode of transport in scope item 6W3 - Transportation Execution. |

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
> Flagged while digesting this document, not verified: The AE script's rail and ocean planning sections use US sample data (source SP_1710, carriers 17386xxx, purchasing org 1710) while road and air use AE data (SP_3310, 33386xxx, org 3310); air main carriage lists carrier 10386502 versus 33386502 in the master data table.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-sap-s-4hana-cloud-public-edition-external-transportation-p]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-transportation-execution-6w3-ae-sap-s-4hana-cloud-public-e-part-01]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6W2_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 140,547 chars in the whole document
