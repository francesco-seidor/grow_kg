---
id: 11-inventory-warehouse-and-transportation/test-script-transportation-execution-6w3-ae-sap-s-4hana-cloud-public-e-part-01
title: "Test Script: Transportation Execution (6W3_AE) - SAP S/4HANA Cloud Public Edition (6W3_S4CLD2608_BPD_EN_AE) — part 1 of 3"
description: "Test script for SAP S/4HANA Cloud Public Edition scope item 6W3 Transportation Execution (AE): road, rail, ocean, air and advanced intercompany test steps."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/transportation-planning-and-execution]
aliases: []
keywords: [Transportation Planning and Execution, transportation execution, freight order execution status, warehouse loading, post goods issue, freight cost accruals, ocean freight bookings, rail freight orders, road freight orders, radio frequency devices]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6W3_S4CLD2608_BPD_EN_AE.docx#lines-1-2769"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1195
topic: 11-inventory-warehouse-and-transportation/transportation-planning-and-execution
language: EN
part: 1/3
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Transportation Execution (6W3_AE) - SAP S/4HANA Cloud Public Edition (6W3_S4CLD2608_BPD_EN_AE) — part 1 of 3

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6W3_S4CLD2608_BPD_EN_AE.docx`, part 1 of 3 (lines 1–2769 of the extracted text), extracted with `mammoth`. Grouped under **Transportation Planning and Execution** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Transportation Execution (6W3_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 6](#_Toc232859825)

[2 Prerequisites 7](#_Toc232859826)

[2.1 System Access 7](#_Toc232859827)

[2.2 Roles 7](#_Toc232859828)

[2.3 Master Data, Organizational Data, and Other Data 8](#_Toc232859829)

[2.4 Additional Manual Configuration 9](#_Toc232859830)

[2.5 Business Conditions 9](#_Toc232859831)

[3 Overview Table 11](#_Toc232859832)

[4 Test Procedures 24](#_Toc232859833)

[4.1 Road 24](#_Toc232859834)

[4.1.1 Outbound 24](#_Toc232859835)

[4.1.1.1 Set Truck Arrived and Checked In at Shipping Point Location 24](#_Toc232859836)

[4.1.1.2 Loading 26](#_Toc232859837)

[4.1.1.2.1 Variant 1: With Fiori App 27](#_Toc232859838)

[4.1.1.2.2 Variant 2: With Radio Frequency Devices 28](#_Toc232859839)

[4.1.1.3 Set Truck Checked Out and Departed at Shipping Point Location 30](#_Toc232859840)

[4.1.1.4 Post Goods Issue 32](#_Toc232859841)

[4.1.1.5 Confirm Freight Costs for Accrual Postings 33](#_Toc232859842)

[4.1.1.6 Set Truck Arrived at Destination Location 39](#_Toc232859843)

[4.1.2 Inbound 40](#_Toc232859844)

[4.1.2.1 Set Truck Arrived and Checked In at Receiving Point Location 40](#_Toc232859845)

[4.1.2.2 Set Ready for Warehousing 42](#_Toc232859846)

[4.1.2.3 Set Truck Checked Out and Departed at Receiving Point Location 44](#_Toc232859847)

[4.1.3 Stock Transfer 45](#_Toc232859848)

[4.1.3.1 Set Truck Arrived and Checked In at Shipping Point Location 45](#_Toc232859849)

[4.1.3.2 Loading 47](#_Toc232859850)

[4.1.3.2.1 Variant 1: With Fiori App 47](#_Toc232859851)

[4.1.3.2.2 Variant 2: With Radio Frequency Devices 49](#_Toc232859852)

[4.1.3.3 Set Truck Checked Out and Departed at Shipping Point Location 50](#_Toc232859853)

[4.1.3.4 Post Goods Issue for Stock Transport Order 52](#_Toc232859854)

[4.1.3.5 Set Truck Arrived and Checked In at Receiving Point Location 53](#_Toc232859855)

[4.1.3.6 Set Ready for Warehousing 55](#_Toc232859856)

[4.1.3.7 Set Truck Checked Out and Departed at Receiving Point Location 56](#_Toc232859857)

[4.1.3.8 Confirm Freight Costs for Accrual Postings 57](#_Toc232859858)

[4.2 Rail 64](#_Toc232859859)

[4.2.1 Outbound 64](#_Toc232859860)

[4.2.1.1 Set Railcar Arrived and Checked In at Shipping Point Location 64](#_Toc232859861)

[4.2.1.2 Loading 65](#_Toc232859862)

[4.2.1.2.1 Variant 1: With Fiori App 66](#_Toc232859863)

[4.2.1.2.2 Variant 2: With Radio Frequency Devices 67](#_Toc232859864)

[4.2.1.3 Set Railcar Checked Out and Departed at Shipping Point Location 69](#_Toc232859865)

[4.2.1.4 Post Goods Issue 71](#_Toc232859866)

[4.2.1.5 Confirm Freight Costs for Accrual Postings 72](#_Toc232859867)

[4.2.1.6 Set Railcar Arrived at Customer Location 78](#_Toc232859868)

[4.2.2 Inbound 79](#_Toc232859869)

[4.2.2.1 Set Railcar Arrived and Checked-In at Receiving Point Location 79](#_Toc232859870)

[4.2.2.2 Set Ready for Warehousing 81](#_Toc232859871)

[4.2.2.3 Set Railcar Checked-Out and Departed at Receiving Point Location 82](#_Toc232859872)

[4.2.3 Stock Transfer 83](#_Toc232859873)

[4.2.3.1 Set Railcar Arrived and Checked In at Shipping Point Location 83](#_Toc232859874)

[4.2.3.2 Loading 85](#_Toc232859875)

[4.2.3.2.1 Variant 1: With Fiori App 85](#_Toc232859876)

[4.2.3.2.2 Variant 2: With Radio Frequency Devices 87](#_Toc232859877)

[4.2.3.3 Set Railcar Checked Out and Departed at Shipping Point Location 89](#_Toc232859878)

[4.2.3.4 Post Goods Issue for Stock Transport Order 90](#_Toc232859879)

[4.2.3.5 Set Railcar Arrived and Checked In at Receiving Point Location 91](#_Toc232859880)

[4.2.3.6 Set Ready for Warehousing 92](#_Toc232859881)

[4.2.3.7 Set Railcar Checked Out and Departed at Receiving Point Location 94](#_Toc232859882)

[4.2.3.8 Confirm Freight Costs for Accrual Postings 95](#_Toc232859883)

[4.3 Ocean 101](#_Toc232859884)

[4.3.1 Outbound 101](#_Toc232859885)

[4.3.1.1 Set Truck Arrived and Checked In at Shipping Point Location (Pick-Up) 101](#_Toc232859886)

[4.3.1.2 Loading 102](#_Toc232859887)

[4.3.1.2.1 Variant 1: With Fiori App 103](#_Toc232859888)

[4.3.1.2.2 Variant 2: With Radio Frequency Devices 105](#_Toc232859889)

[4.3.1.3 Set Truck Checked Out and Departed at Shipping Point Location (Pick-Up) 106](#_Toc232859890)

[4.3.1.4 Post Goods Issue 109](#_Toc232859891)

[4.3.1.5 Create Billing Document 110](#_Toc232859892)

[4.3.1.6 Arrival of Truck at Port of Loading (Pick-Up) 111](#_Toc232859893)

[4.3.1.7 Departure of Vessel from Port of Loading (Main Leg) 112](#_Toc232859894)

[4.3.1.8 Confirm Freight Costs for Accrual Postings 114](#_Toc232859895)

[4.3.1.9 Arrival of Vessel at Port of Discharge (Main Leg) 119](#_Toc232859896)

[4.3.1.10 Departure of Truck at Port of Discharge (Delivery) 121](#_Toc232859897)

[4.3.1.11 Set Truck Arrived at Customer Location (Delivery) 122](#_Toc232859898)

[4.3.2 Inbound 123](#_Toc232859899)

[4.3.2.1 Arrival of Truck at Port of Loading (Pick-up) 123](#_Toc232859900)

[4.3.2.2 Departure of Vessel from Port of Loading (Main Leg) 125](#_Toc232859901)

[4.3.2.3 Confirm Freight Costs for Accrual Postings 126](#_Toc232859902)

[4.3.2.4 Arrival of Vessel at Port of Discharge (Main Leg) 132](#_Toc232859903)

[4.3.2.5 Departure of Truck at Port of Discharge (Delivery) 134](#_Toc232859904)

[4.3.2.6 Set Truck Arrived and Checked-In at Receiving Point Location (Delivery) 135](#_Toc232859905)

[4.3.2.7 Set Ready for Warehousing 136](#_Toc232859906)

[4.3.2.8 Set Truck Checked Out and Departed at Receiving Point Location (Delivery) 138](#_Toc232859907)

[4.3.3 Stock Transfer 139](#_Toc232859908)

[4.3.3.1 Set Truck Arrived and Checked In at Shipping Point Location (Pick-Up) 139](#_Toc232859909)

[4.3.3.2 Loading 141](#_Toc232859910)

[4.3.3.2.1 Variant 1: With Fiori App 141](#_Toc232859911)

[4.3.3.2.2 Variant 2: With Radio Frequency Devices 143](#_Toc232859912)

[4.3.3.3 Set Truck Checked Out and Departed at Shipping Point Location (Pick-Up) 144](#_Toc232859913)

[4.3.3.4 Post Goods Issue for Stock Transport Order 147](#_Toc232859914)

[4.3.3.5 Arrival of Truck at Port of Loading (Pick-Up) 147](#_Toc232859915)

[4.3.3.6 Departure of Vessel from Port of Loading (Main Leg) 149](#_Toc232859916)

[4.3.3.7 Confirm Freight Costs for Accrual Postings 150](#_Toc232859917)

[4.3.3.8 Arrival of Vessel at Port of Discharge (Main Leg) 155](#_Toc232859918)

[4.3.3.9 Departure of Truck at Port of Discharge (Delivery) 157](#_Toc232859919)

[4.3.3.10 Set Truck Arrived and Checked In at Receiving Point Location (Delivery) 158](#_Toc232859920)

[4.3.3.11 Set Ready for Warehousing 159](#_Toc232859921)

[4.3.3.12 Set Truck Checked Out and Departed at Receiving Point Location (Delivery) 161](#_Toc232859922)

[4.4 Air 162](#_Toc232859923)

[4.4.1 Outbound 162](#_Toc232859924)

[4.4.1.1 Set Truck Arrived and Checked In at Shipping Point Location (Pick-Up) 162](#_Toc232859925)

[4.4.1.2 Loading 164](#_Toc232859926)

[4.4.1.2.1 Variant 1: With Fiori App 164](#_Toc232859927)

[4.4.1.2.2 Variant 2: With Radio Frequency Devices 166](#_Toc232859928)

[4.4.1.3 Set Truck Checked Out and Departed at Shipping Point Location (Pick-Up) 167](#_Toc232859929)

[4.4.1.4 Post Goods Issue 169](#_Toc232859930)

[4.4.1.5 Create Billing Document 171](#_Toc232859931)

[4.4.1.6 Arrival of Truck at Airport of Departure (Pick-Up) 172](#_Toc232859932)

[4.4.1.7 Departure of Airplane at Airport of Departure (Main Leg) 173](#_Toc232859933)

[4.4.1.8 Confirm Freight Costs for Accrual Postings 175](#_Toc232859934)

[4.4.1.9 Arrival of Airplane at Airport of Destination (Main Leg) 180](#_Toc232859935)

[4.4.1.10 Departure of Truck at Airport of Destination (Delivery) 182](#_Toc232859936)

[4.4.1.11 Set Truck Arrived at Customer Location (Delivery) 183](#_Toc232859937)

[4.4.2 Inbound 185](#_Toc232859938)

[4.4.2.1 Arrival of Truck at Airport of Departure (Pick-Up) 185](#_Toc232859939)

[4.4.2.2 Departure of Airplane at Airport of Departure (Main Leg) 186](#_Toc232859940)

[4.4.2.3 Confirm Freight Costs for Accrual Postings 188](#_Toc232859941)

[4.4.2.4 Arrival of Airplane at Airport of Destination (Main Leg) 193](#_Toc232859942)

[4.4.2.5 Departure of Truck at Airport of Destination (Delivery) 195](#_Toc232859943)

[4.4.2.6 Set Truck Arrived and Checked In at Receiving Point Location (Delivery) 196](#_Toc232859944)

[4.4.2.7 Set Ready for Warehousing 198](#_Toc232859945)

[4.4.2.8 Set Truck Checked Out and Departed at Receiving Point Location (Delivery) 199](#_Toc232859946)

[4.4.3 Stock Transfer 200](#_Toc232859947)

[4.4.3.1 Set Truck Arrived and Checked In at Shipping Point Location (Pick-Up) 200](#_Toc232859948)

[4.4.3.2 Loading 202](#_Toc232859949)

[4.4.3.2.1 Variant 1: With Fiori App 202](#_Toc232859950)

[4.4.3.2.2 Variant 2: With Radio Frequency Devices 204](#_Toc232859951)

[4.4.3.3 Set Truck Checked Out and Departed at Shipping Point Location (Pick-Up) 206](#_Toc232859952)

[4.4.3.4 Post Goods Issue for Stock Transport Order 207](#_Toc232859953)

[4.4.3.5 Arrival of Truck at Airport of Departure (Pick-Up) 208](#_Toc232859954)

[4.4.3.6 Departure of Airplane at Airport of Departure (Main Leg) 209](#_Toc232859955)

[4.4.3.7 Confirm Freight Costs for Accrual Postings 211](#_Toc232859956)

[4.4.3.8 Arrival of Airplane at Airport of Destination (Main Leg) 216](#_Toc232859957)

[4.4.3.9 Departure of Truck at Airport of Destination (Delivery) 218](#_Toc232859958)

[4.4.3.10 Set Truck Arrived and Checked In at Receiving Point Location (Delivery) 219](#_Toc232859959)

[4.4.3.11 Set Ready for Warehousing 221](#_Toc232859960)

[4.4.3.12 Set Truck Checked Out and Departed at Receiving Point Location (Delivery) 222](#_Toc232859961)

[4.5 Advanced Intercompany Sales 224](#_Toc232859962)

[4.5.1 Set Truck Arrived and Checked In at Shipping Point Location (Pick-Up) 224](#_Toc232859963)

[4.5.2 Set Truck Checked Out and Departed at Shipping Point Location (Pick-Up) 226](#_Toc232859964)

[4.5.3 Post Goods Issue 229](#_Toc232859965)

[4.5.4 Arrival of Truck at Port of Loading (Pick-up) 230](#_Toc232859966)

[4.5.5 Departure of Vessel from Port of Loading (Main Leg) 231](#_Toc232859967)

[4.5.6 Display Internal Transfer of Control Date for Delivery (Optional) 233](#_Toc232859968)

[4.5.7 Arrival of Vessel at Port of Discharge (Main Leg) 234](#_Toc232859969)

[4.5.8 Confirm Freight Costs for Accrual Postings 235](#_Toc232859970)

[4.5.9 Departure of Truck at Port of Discharge (On-Carriage) 241](#_Toc232859971)

[4.5.10 Confirm Freight Costs for Accrual Postings 242](#_Toc232859972)

[4.5.11 Set Truck Arrived at Customer Location (On-Carriage) 247](#_Toc232859973)

[4.5.12 Display External Transfer of Control Date for Delivery (Optional) 249](#_Toc232859974)

[4.6 Advanced Intercompany Stock Transfer 250](#_Toc232859975)

[4.6.1 Set Truck Arrived and Checked In at Shipping Point Location (Pick-Up) 250](#_Toc232859976)

[4.6.2 Set Truck Checked Out and Departed at Shipping Point Location (Pick-Up) 252](#_Toc232859977)

[4.6.3 Post Goods Issue 254](#_Toc232859978)

[4.6.4 Arrival of Truck at Port of Loading (Pick-Up) 256](#_Toc232859979)

[4.6.5 Departure of Vessel from Port of Loading (Main Leg) 257](#_Toc232859980)

[4.6.6 Display Internal Transfer of Control Date for Goods in Transit (Optional) 259](#_Toc232859981)

[4.6.7 Confirm Freight Costs for Accrual Postings 260](#_Toc232859982)

[4.6.8 Arrival of Vessel at Port of Discharge (Main Leg) 265](#_Toc232859983)

[4.6.9 Departure of Truck at Port of Discharge (On-Carriage) 267](#_Toc232859984)

[4.6.10 Set Truck Arrived and Checked In at Receiving Point Location (On-Carriage) 268](#_Toc232859985)

[4.6.11 Set Ready for Warehousing 270](#_Toc232859986)

[4.6.12 Set Truck Checked Out and Departed at Receiving Point Location (On-Carriage) 271](#_Toc232859987)

[4.6.13 Confirm Freight Costs for Accrual Postings 272](#_Toc232859988)

[5 Appendix 279](#_Toc232859989)

[5.1 Process Integration 279](#_Toc232859990)

[5.1.1 Preceding Processes 279](#_Toc232859991)

[5.1.2 Succeeding Processes 279](#_Toc232859992)

## Purpose

Overview

With this process, you execute and track the transportation process for your freight documents. You can set the relevant statuses to track the arrival and departure at your locations and set the checkout status to enable freight cost confirmation. You can set statuses for the entire document, as well as for individual stages and locations.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/6W3_S4CLD2602_BPD_EN_AE.docx) ). |

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Dispatcher (TM) | SAP_BR_DISPATCHER | Dispatching | SAP_BR_DISPATCHER |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Transportation Buyer | SAP_BR_TRANSP_BUYER | Transportation Procurement | SAP_TM_SPT_TRANSPBUYER_PC |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Warehouse Operative (EWM) | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Warehouse Floor | SAP_BR_WAREHOUSE_OPERATIVE_EWM |  |
| Warehouse Clerk (EWM) | SAP_BR_WAREHOUSE_CLERK_EWM | Warehouse Office | SAP_BR_WAREHOUSE_CLERK_EWM |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Location | SP_3310 | Shipping Point Location 3310Location Type 1003 Shipping Point | Shipping point outboundReceiving point in stock transfer, advanced intercompany stock transfer, and inbound |
| Location | SP_3320 | Shipping Point Location 3320Location Type 1003 Shipping Point | Shipping point stock transfer |
| Location | SP_1710 | Shipping Point Location 1710 (supplying shipping point location)Location Type 1003 Shipping Point | Shipping point advanced intercompany sales and stock transfer |
| Location | 33186001 | Location for TM Domestic AE Customer 1Location Type 1021 Business Partner | Customer location in outbound and advanced intercompany sales |
| Location | PORT_AESID | Seaport 1Port LocationLocation Type 1100 Port | Port of discharge sales outboundPort of discharge customer returnsPort of discharge procurement inboundPort of loading stock transferPort of discharge advanced intercompany salesPort of discharge advanced intercompany stock transfer |
| Location | PORT_AEYAS | Seaport 1Port LocationLocation Type 1100 Port | Port of loading sales outboundPort of discharge customer returnsPort of loading procurement inboundPort of discharge stock transfer |
| Location | AIRPORT_DXB | Location Type 1110 Airport | Airport of departure outboundAirport of destination inbound and stock transfer |
| Location | AIRPORT_AUH | Location Type 1110 Airport | Airport of departure stock transfer |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/8d580236a54a9c1b5f71f0b61d1a2531)

### Business Conditions

Before you can test this scope item, at least one of the following business conditions for transportation planning (6W1 or 6W2) must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 6W1 - External Transportation Planning | This business condition is a prerequisite only in the case of external transportation planning.Create Deliveries Based on Freight Orders |
| 6W2 - Manual Transportation Planning | This business condition is a prerequisite only in the case of internal transportation planning.Depending on your scenario and mode of transport, complete one of the following process steps:Trigger Delivery Creation and Monitor Road Freight OrderTrigger Delivery Creation and Monitor Rail Freight OrderTrigger Delivery Creation and Monitor Ocean Freight BookingTrigger Delivery Creation and Monitor Air Freight BookingReceive Freight Order Confirmation Delivery Stage for Advanced Intercompany Business Processes |
| BD9 - Sell from Stock | Execute Picking for outbound scenarios |
| 3BS - Warehouse Outbound Processing | Execute Picking for outbound scenarios |
| 3NR - Sales Scheduling Agreements | Execute Picking for outbound scenarios |
| BME - Stock Transfer with Delivery | Pick Stock Transport Order for stock transfer scenarios |
| 5D2 - Advanced Intercompany Sales | Perform Picking for advanced intercompany sales scenario |
| 5HP - Advanced Intercompany Stock Transfer | Pick and Post Goods Issue for Outbound Delivery for advanced intercompany stock transfer scenario |
| BMK - Return to Supplier | Business Condition: Execute picking for the outbound delivery created in the preceding process. |
| BMY - Subcontracting | Execute picking for the outbound delivery.Note Make sure to perform the execution for both outbound and inbound processes. |

## Overview Table

This scope item consists of several <choose the appropriate entity: process steps, reports, items> provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Road](#unique_9) [page ] 24 |  |  |  |
| [Outbound](#unique_10) [page ] 24 |  |  |  |
| [Set Truck Arrived and Checked In at Shipping Point Location](#unique_11) [page ] 24 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Ready for execution check completed without errors.Execution status of doc. Road Freight Order <your freight order number> set to Ready for Transportation Execution.Arrival at shipping point was reported.Check-in at shipping point was reported. |
| [Loading](#unique_12) [page ] 26 |  |  |  |
| [Variant 1: With Fiori App](#unique_13) [page ] 27 | Warehouse Clerk (EWM) | Load or Unload Freight Orders (/SCMTMS/ASR) |  |
| [Variant 2: With Radio Frequency Devices](#unique_14) [page ] 28 | Warehouse Operative (EWM) | Test RF Environment (/SCWM/RFUI) |  |
| [Set Truck Checked Out and Departed at Shipping Point Location](#unique_15) [page ] 30 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Checkout at shipping point was reported.Departure at shipping point was reported. |
| [Post Goods Issue](#unique_16) [page ] 32 | Shipping Specialist | Monitor Accrual Postings - Freight Documents (F4329) |  |
| [Confirm Freight Costs for Accrual Postings](#unique_17) [page ] 33 | Transportation Buyer | Monitor Accrual Postings - Freight Documents (F4329) |  |
| [Set Truck Arrived at Destination Location](#unique_18) [page ] 39 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Arrival at customer location and required preceding events were reported. |
| [Inbound](#unique_19) [page ] 40 |  |  |  |
| [Set Truck Arrived and Checked In at Receiving Point Location](#unique_20) [page ] 40 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Ready for execution check completed without errors.Execution status of doc. Road Freight Order <your freight order number> set to Ready for Transportation Execution.Arrival at receiving point and required preceding events were reported.Check-In at receiving point was reported. |
| [Set Ready for Warehousing](#unique_21) [page ] 42 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) |  |
| [Set Truck Checked Out and Departed at Receiving Point Location](#unique_22) [page ] 44 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Checkout at receiving point was reported.Departure at receiving point was reported. |
| [Stock Transfer](#unique_23) [page ] 45 |  |  |  |
| [Set Truck Arrived and Checked In at Shipping Point Location](#unique_24) [page ] 45 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Ready for execution check completed without errorsExecution status of doc. Road Freight Order <your freight order number> set to Ready for Transportation Execution.Arrival at shipping point was reported.Check-In at shipping point was reported. |
| [Loading](#unique_25) [page ] 47 |  |  |  |
| [Variant 1: With Fiori App](#unique_26) [page ] 47 | Warehouse Clerk (EWM) | Load or Unload Freight Orders (/SCMTMS/ASR) |  |
| [Variant 2: With Radio Frequency Devices](#unique_27) [page ] 49 | Warehouse Operative (EWM) | Test RF Environment (/SCWM/RFUI) |  |
| [Set Truck Checked Out and Departed at Shipping Point Location](#unique_28) [page ] 50 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Checkout at shipping point was reported.Departure at shipping point was reported. |
| [Post Goods Issue for Stock Transport Order](#unique_29) [page ] 52 | Shipping Specialist | Change Outbound Delivery (VL02N) |  |
| [Set Truck Arrived and Checked In at Receiving Point Location](#unique_30) [page ] 53 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Arrival at receiving point was reported.Check-In at receiving point was reported. |
| [Set Ready for Warehousing](#unique_31) [page ] 55 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) |  |
| [Set Truck Checked Out and Departed at Receiving Point Location](#unique_32) [page ] 56 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Checkout at receiving point was reported.Departure at receiving point was reported. |
| [Confirm Freight Costs for Accrual Postings](#unique_33) [page ] 57 | Transportation Buyer | Monitor Accrual Postings - Freight Documents (F4329) |  |
| [Rail](#unique_34) [page ] 64 |  |  |  |
| [Outbound](#unique_35) [page ] 64 |  |  |  |
| [Set Railcar Arrived and Checked In at Shipping Point Location](#unique_36) [page ] 64 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Ready for execution check completed without errorsExecution status of doc. Rail Freight Order <your freight order number> set to "Ready for Transportation Execution".Arrival at shipping point was reported.Check-In at shipping point was reported. |
| [Loading](#unique_37) [page ] 65 |  |  |  |
| [Variant 1: With Fiori App](#unique_38) [page ] 66 | Warehouse Clerk (EWM) | Load or Unload Freight Orders (/SCMTMS/ASR) |  |
| [Variant 2: With Radio Frequency Devices](#unique_39) [page ] 67 | Warehouse Operative (EWM) | Test RF Environment (/SCWM/RFUI) |  |
| [Set Railcar Checked Out and Departed at Shipping Point Location](#unique_40) [page ] 69 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Checkout at shipping point was reported.Departure at shipping point was reported. |
| [Post Goods Issue](#unique_41) [page ] 71 | Shipping Specialist | Manage Ocean Freight Bookings (F6213) |  |
| [Confirm Freight Costs for Accrual Postings](#unique_42) [page ] 72 | Transportation Buyer | Monitor Accrual Postings - Freight Documents (F4329) |  |
| [Set Railcar Arrived at Customer Location](#unique_43) [page ] 78 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Arrival at customer location and required preceding events were reported. |
| [Inbound](#unique_44) [page ] 79 |  |  |  |
| [Set Railcar Arrived and Checked-In at Receiving Point Location](#unique_45) [page ] 79 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Ready for execution check completed without errorsExecution status of doc. Rail Freight Order <your freight order number> set to "Ready for Transportation Execution".Arrival at receiving point was reported.Check-In at receiving point was reported. |
| [Set Ready for Warehousing](#unique_46) [page ] 81 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) |  |
| [Set Railcar Checked-Out and Departed at Receiving Point Location](#unique_47) [page ] 82 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Checkout at receiving point was reported.Departure at receiving point was reported. |
| [Stock Transfer](#unique_48) [page ] 83 |  |  |  |
| [Set Railcar Arrived and Checked In at Shipping Point Location](#unique_49) [page ] 83 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Ready for execution check completed without errorsExecution status of doc. Rail Freight Order <your freight order number> set to "Ready for Transportation Execution".Arrival at shipping point was reported.Check-In at shipping point was reported. |
| [Loading](#unique_50) [page ] 85 |  |  |  |
| [Variant 1: With Fiori App](#unique_51) [page ] 85 | Warehouse Clerk (EWM) | Load or Unload Freight Orders (/SCMTMS/ASR) |  |
| [Variant 2: With Radio Frequency Devices](#unique_52) [page ] 87 | Warehouse Operative (EWM) | Test RF Environment (/SCWM/RFUI) |  |
| [Set Railcar Checked Out and Departed at Shipping Point Location](#unique_53) [page ] 89 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Checkout at shipping point was reported.Departure at shipping point was reported. |
| [Post Goods Issue for Stock Transport Order](#unique_54) [page ] 90 | Shipping Specialist | Monitor Accrual Postings - Freight Documents (F4329) |  |
| [Set Railcar Arrived and Checked In at Receiving Point Location](#unique_55) [page ] 91 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Arrival at receiving point was reported.Check-In at receiving point was reported. |
| [Set Ready for Warehousing](#unique_56) [page ] 92 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) |  |
| [Set Railcar Checked Out and Departed at Receiving Point Location](#unique_57) [page ] 94 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Checkout at receiving point was reported.Departure at receiving point was reported. |
| [Confirm Freight Costs for Accrual Postings](#unique_58) [page ] 95 | Transportation Buyer | Monitor Accrual Postings - Freight Documents (F4329) |  |
| [Ocean](#unique_59) [page ] 101 |  |  |  |
| [Outbound](#unique_60) [page ] 101 |  |  |  |
| [Set Truck Arrived and Checked In at Shipping Point Location (Pick-Up)](#unique_61) [page ] 101 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Pick-Up <your freight order number> set to "Ready for Transportation Execution".Arrival at shipping point was reported.Check-In at shipping point was reported. |
| [Loading](#unique_62) [page ] 102 |  |  |  |
| [Variant 1: With Fiori App](#unique_63) [page ] 103 | Warehouse Clerk (EWM) | Load or Unload Freight Orders (/SCMTMS/ASR) |  |
| [Variant 2: With Radio Frequency Devices](#unique_64) [page ] 105 | Warehouse Operative (EWM) | Test RF Environment (/SCWM/RFUI) |  |
| [Set Truck Checked Out and Departed at Shipping Point Location (Pick-Up)](#unique_65) [page ] 106 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Checkout at shipping point was reported.Departure at shipping point was reported. |
| [Post Goods Issue](#unique_66) [page ] 109 | Shipping Specialist | Manage Outbound Deliveries (F0867A) |  |
| [Create Billing Document](#unique_67) [page ] 110 | Billing Clerk | Create Billing Documents (F0798) |  |
| [Arrival of Truck at Port of Loading (Pick-Up)](#unique_68) [page ] 111 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Arrival at port of loading was reported. |
| [Departure of Vessel from Port of Loading (Main Leg)](#unique_69) [page ] 112 | Dispatcher (TM) | Manage Ocean Freight Bookings (F6213) | Loading End at port of loading was reported.Departure at port of loading was reported. |
| [Confirm Freight Costs for Accrual Postings](#unique_70) [page ] 114 | Transportation Buyer | Monitor Accrual Postings - Freight Documents (F4329) |  |
| [Arrival of Vessel at Port of Discharge (Main Leg)](#unique_71) [page ] 119 | Dispatcher (TM) | Manage Ocean Freight Bookings (F6213) | Arrival at port of discharge was reported. |
| [Departure of Truck at Port of Discharge (Delivery)](#unique_72) [page ] 121 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Delivery <your freight order number> set to "Ready for Transportation Execution".Departure at port of discharge and required preceding events were reported. |
| [Set Truck Arrived at Customer Location (Delivery)](#unique_73) [page ] 122 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Arrival at customer location and required preceding events were reported. |
| [Inbound](#unique_74) [page ] 123 |  |  |  |
| [Arrival of Truck at Port of Loading (Pick-up)](#unique_75) [page ] 123 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Pick-Up <your freight order number> set to "Ready for Transportation Execution".Arrival at port of loading and required preceding events were reported. |
| [Departure of Vessel from Port of Loading (Main Leg)](#unique_76) [page ] 125 | Dispatcher (TM) | Manage Ocean Freight Bookings (F6213) | Loading End at port of loading was reported.Departure at port of loading was reported. |
| [Confirm Freight Costs for Accrual Postings](#unique_77) [page ] 126 | Transportation Buyer | Monitor Accrual Postings - Freight Documents (F4329) |  |
| [Arrival of Vessel at Port of Discharge (Main Leg)](#unique_78) [page ] 132 | Dispatcher (TM) | Manage Ocean Freight Bookings (F6213) | Arrival at port of discharge was reported. |
| [Departure of Truck at Port of Discharge (Delivery)](#unique_79) [page ] 134 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Delivery <your freight order number> set to "Ready for Transportation Execution".Departure at port of discharge and required preceding events were reported. |
| [Set Truck Arrived and Checked-In at Receiving Point Location (Delivery)](#unique_80) [page ] 135 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Arrival at receiving point was reported.Check-In at receiving point was reported. |
| [Set Ready for Warehousing](#unique_81) [page ] 136 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) |  |
| [Set Truck Checked Out and Departed at Receiving Point Location (Delivery)](#unique_82) [page ] 138 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Checkout at receiving point and required preceding events were reported.Departure at receiving point was reported. |
| [Stock Transfer](#unique_83) [page ] 139 |  |  |  |
| [Set Truck Arrived and Checked In at Shipping Point Location (Pick-Up)](#unique_84) [page ] 139 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Pick-Up <your freight order number> set to "Ready for Transportation Execution".Arrival at shipping point was reported.Check-In at shipping point was reported. |
| [Loading](#unique_85) [page ] 141 |  |  |  |
| [Variant 1: With Fiori App](#unique_86) [page ] 141 | Warehouse Clerk (EWM) | Load or Unload Freight Orders (/SCMTMS/ASR) |  |
| [Variant 2: With Radio Frequency Devices](#unique_87) [page ] 143 | Warehouse Operative (EWM) | Test RF Environment (/SCWM/RFUI) |  |
| [Set Truck Checked Out and Departed at Shipping Point Location (Pick-Up)](#unique_88) [page ] 144 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Checkout at shipping point was reported.Departure at shipping point was reported. |
| [Post Goods Issue for Stock Transport Order](#unique_89) [page ] 147 | Shipping Specialist | Change Outbound Delivery (VL02N) |  |
| [Arrival of Truck at Port of Loading (Pick-Up)](#unique_90) [page ] 147 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Arrival at port of loading was reported. |
| [Departure of Vessel from Port of Loading (Main Leg)](#unique_91) [page ] 149 | Dispatcher (TM) | Manage Ocean Freight Bookings (F6213) | Loading End at port of loading was reported.Departure at port of loading was reported. |
| [Confirm Freight Costs for Accrual Postings](#unique_92) [page ] 150 | Transportation Buyer | Monitor Accrual Postings - Freight Documents (F4329) |  |
| [Arrival of Vessel at Port of Discharge (Main Leg)](#unique_93) [page ] 155 | Dispatcher (TM) | Manage Ocean Freight Bookings (F6213) | Arrival at port of discharge was reported. |
| [Departure of Truck at Port of Discharge (Delivery)](#unique_94) [page ] 157 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Delivery <your freight order number> set to "Ready for Transportation Execution".Departure at port of discharge and required preceding events were reported. |
| [Set Truck Arrived and Checked In at Receiving Point Location (Delivery)](#unique_95) [page ] 158 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Arrival at receiving point was reported.Check-In at receiving point was reported. |
| [Set Ready for Warehousing](#unique_96) [page ] 159 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) |  |
| [Set Truck Checked Out and Departed at Receiving Point Location (Delivery)](#unique_97) [page ] 161 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Checkout at receiving point was reported.Departure at receiving point was reported. |
| [Air](#unique_98) [page ] 162 |  |  |  |
| [Outbound](#unique_99) [page ] 162 |  |  |  |
| [Set Truck Arrived and Checked In at Shipping Point Location (Pick-Up)](#unique_100) [page ] 162 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Pick-Up <your freight order number> set to "Ready for Transportation Execution".Arrival at shipping point was reported.Check-In at shipping point was reported. |
| [Loading](#unique_101) [page ] 164 |  |  |  |
| [Variant 1: With Fiori App](#unique_102) [page ] 164 | Warehouse Clerk (EWM) | Load or Unload Freight Orders (/SCMTMS/ASR) |  |
| [Variant 2: With Radio Frequency Devices](#unique_103) [page ] 166 | Warehouse Operative (EWM) | Test RF Environment (/SCWM/RFUI) |  |
| [Set Truck Checked Out and Departed at Shipping Point Location (Pick-Up)](#unique_104) [page ] 167 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Checkout at shipping point was reported.Departure at shipping point was reported. |
| [Post Goods Issue](#unique_105) [page ] 169 | Shipping Specialist | Manage Outbound Deliveries (F0867A) |  |
| [Create Billing Document](#unique_106) [page ] 171 | Billing Clerk | Create Billing Documents (F0798) |  |
| [Arrival of Truck at Airport of Departure (Pick-Up)](#unique_107) [page ] 172 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Arrival at airport of departure and required preceding events were reported. |
| [Departure of Airplane at Airport of Departure (Main Leg)](#unique_108) [page ] 173 | Dispatcher (TM) | Manage Air Freight Bookings (F6535) | Departure at airport of departure was reported. |
| [Confirm Freight Costs for Accrual Postings](#unique_109) [page ] 175 | Transportation Buyer | Monitor Accrual Postings - Freight Documents (F4329) |  |
| [Arrival of Airplane at Airport of Destination (Main Leg)](#unique_110) [page ] 180 | Dispatcher (TM) | Manage Air Freight Bookings (F6535) | Arrival at airport of destination was reported. |
| [Departure of Truck at Airport of Destination (Delivery)](#unique_111) [page ] 182 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Delivery <freight order number for delivery from previous step> set to "Ready for Transportation Execution".Handling execution status for airport of destination set to "Departed". |
| [Set Truck Arrived at Customer Location (Delivery)](#unique_112) [page ] 183 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Arrival at customer location and required preceding events were reported. |
| [Inbound](#unique_113) [page ] 185 |  |  |  |
| [Arrival of Truck at Airport of Departure (Pick-Up)](#unique_114) [page ] 185 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Pick-Up <your freight order number> set to "Ready for Transportation Execution".Arrival at airport of departure and required preceding events were reported. |
| [Departure of Airplane at Airport of Departure (Main Leg)](#unique_115) [page ] 186 | Dispatcher (TM) | Manage Air Freight Bookings (F6535) | Departure at airport of departure was reported. |
| [Confirm Freight Costs for Accrual Postings](#unique_116) [page ] 188 | Transportation Buyer | Monitor Accrual Postings - Freight Documents (F4329) |  |
| [Arrival of Airplane at Airport of Destination (Main Leg)](#unique_117) [page ] 193 | Dispatcher (TM) | Manage Air Freight Bookings (F6535) | Arrival at airport of destination was reported. |
| [Departure of Truck at Airport of Destination (Delivery)](#unique_118) [page ] 195 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Delivery <freight order number for delivery from previous step> set to "Ready for Transportation Execution".Departure at airport of destination and required preceding events were reported. |
| [Set Truck Arrived and Checked In at Receiving Point Location (Delivery)](#unique_119) [page ] 196 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Arrival at receiving point was reported.Check-In at receiving point was reported. |
| [Set Ready for Warehousing](#unique_120) [page ] 198 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) |  |
| [Set Truck Checked Out and Departed at Receiving Point Location (Delivery)](#unique_121) [page ] 199 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Checkout at receiving point and required preceding events were reported.Departure at receiving point was reported. |
| [Stock Transfer](#unique_122) [page ] 200 |  |  |  |
| [Set Truck Arrived and Checked In at Shipping Point Location (Pick-Up)](#unique_123) [page ] 200 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Pick-Up <your freight order number> set to "Ready for Transportation Execution".Arrival at shipping point was reported.Check-In at shipping point was reported. |
| [Loading](#unique_124) [page ] 202 |  |  |  |
| [Variant 1: With Fiori App](#unique_125) [page ] 202 | Warehouse Clerk (EWM) | Load or Unload Freight Orders (/SCMTMS/ASR) |  |
| [Variant 2: With Radio Frequency Devices](#unique_126) [page ] 204 | Warehouse Operative (EWM) | Test RF Environment (/SCWM/RFUI) |  |
| [Set Truck Checked Out and Departed at Shipping Point Location (Pick-Up)](#unique_127) [page ] 206 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Checkout at shipping point was reported.Departure at shipping point was reported. |
| [Post Goods Issue for Stock Transport Order](#unique_128) [page ] 207 | Shipping Specialist | Change Outbound Delivery (VL02N) |  |
| [Arrival of Truck at Airport of Departure (Pick-Up)](#unique_129) [page ] 208 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Arrival at airport of departure and required preceding events were reported. |
| [Departure of Airplane at Airport of Departure (Main Leg)](#unique_130) [page ] 209 | Dispatcher (TM) | Manage Air Freight Bookings (F6535) | Departure at airport of departure was reported. |
| [Confirm Freight Costs for Accrual Postings](#unique_131) [page ] 211 | Transportation Buyer | Monitor Accrual Postings - Freight Documents (F4329) |  |
| [Arrival of Airplane at Airport of Destination (Main Leg)](#unique_132) [page ] 216 | Dispatcher (TM) | Manage Air Freight Bookings (F6535) | Arrival at airport of destination was reported. |
| [Departure of Truck at Airport of Destination (Delivery)](#unique_133) [page ] 218 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Delivery <freight order number for delivery from previous step> set to "Ready for Transportation Execution".Departure at airport of destination and required preceding events were reported. |
| [Set Truck Arrived and Checked In at Receiving Point Location (Delivery)](#unique_134) [page ] 219 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Arrival at receiving point was reported.Check-In at receiving point was reported. |
| [Set Ready for Warehousing](#unique_135) [page ] 221 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) |  |
| [Set Truck Checked Out and Departed at Receiving Point Location (Delivery)](#unique_136) [page ] 222 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Checkout at receiving point was reported.Departure at receiving point was reported. |
| [Advanced Intercompany Sales](#unique_137) [page ] 224 |  |  |  |
| [Set Truck Arrived and Checked In at Shipping Point Location (Pick-Up)](#unique_138) [page ] 224 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Pick-Up <your freight order number> set to "Ready for Transportation Execution".Arrival at shipping point was reported.Check-In at shipping point was reported. |
| [Set Truck Checked Out and Departed at Shipping Point Location (Pick-Up)](#unique_139) [page ] 226 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Checkout at shipping point was reported.Departure at shipping point was reported. |
| [Post Goods Issue](#unique_140) [page ] 229 | Shipping Specialist | Change Outbound Delivery (VL02N) |  |
| [Arrival of Truck at Port of Loading (Pick-up)](#unique_141) [page ] 230 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Arrival at port of loading was reported. |
| [Departure of Vessel from Port of Loading (Main Leg)](#unique_142) [page ] 231 | Dispatcher (TM) | Manage Ocean Freight Bookings (F6213) | Loading End at port of loading was reported.Departure at port of loading was reported. |
| [Display Internal Transfer of Control Date for Delivery (Optional)](#unique_143) [page ] 233 | Shipping Specialist | Manage Outbound Deliveries - VL06O(VL06O_CLOUD) |  |
| [Arrival of Vessel at Port of Discharge (Main Leg)](#unique_144) [page ] 234 | Dispatcher (TM) | Manage Ocean Freight Bookings (F6213) | Arrival at port of discharge was reported. |
| [Confirm Freight Costs for Accrual Postings](#unique_145) [page ] 235 | Transportation Buyer | Monitor Accrual Postings - Freight Documents (F4329) |  |
| [Departure of Truck at Port of Discharge (On-Carriage)](#unique_146) [page ] 241 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Ready for execution check completed without errorsExecution status of doc. Road Freight Order <your freight order number> set to "Ready for Transportation Execution".Checkout at port of discharge and required preceding events were reported.Departure at port of discharge was reported. |
| [Confirm Freight Costs for Accrual Postings](#unique_147) [page ] 242 | Transportation Buyer | Monitor Accrual Postings - Freight Documents (F4329) |  |
| [Set Truck Arrived at Customer Location (On-Carriage)](#unique_148) [page ] 247 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Arrival at customer location and required preceding events were reported. |
| [Display External Transfer of Control Date for Delivery (Optional)](#unique_149) [page ] 249 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Advanced Intercompany Stock Transfer](#unique_150) [page ] 250 |  |  |  |
| [Set Truck Arrived and Checked In at Shipping Point Location (Pick-Up)](#unique_151) [page ] 250 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Pick-Up <your freight order number> set to "Ready for Transportation Execution".Arrival at shipping point was reported.Check-In at shipping point was reported. |
| [Set Truck Checked Out and Departed at Shipping Point Location (Pick-Up)](#unique_152) [page ] 252 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Checkout at shipping point and required preceding events were reported.Departure at shipping point was reported. |
| [Post Goods Issue](#unique_153) [page ] 254 | Shipping Specialist | Manage Outbound Deliveries (F0867A) |  |
| [Arrival of Truck at Port of Loading (Pick-Up)](#unique_154) [page ] 256 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Arrival at port of loading was reported. |
| [Departure of Vessel from Port of Loading (Main Leg)](#unique_155) [page ] 257 | Dispatcher (TM) | Manage Ocean Freight Bookings (F6213) | Loading End at port of loading was reported.Departure at port of loading was reported. |
| [Display Internal Transfer of Control Date for Goods in Transit (Optional)](#unique_156) [page ] 259 | Shipping Specialist | Display Outbound Delivery (VL03N) |  |
| [Confirm Freight Costs for Accrual Postings](#unique_157) [page ] 260 | Transportation Buyer | Monitor Accrual Postings - Freight Documents (F4329) |  |
| [Arrival of Vessel at Port of Discharge (Main Leg)](#unique_158) [page ] 265 | Dispatcher (TM) | Manage Ocean Freight Bookings (F6213) | Arrival at port of discharge was reported. |
| [Departure of Truck at Port of Discharge (On-Carriage)](#unique_159) [page ] 267 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Ready for execution check completed without errorsExecution status of doc. Road Freight Order <your freight order number> set to "Ready for Transportation Execution".Checkout at port of discharge and required preceding events were reported.Departure at port of discharge was reported. |
| [Set Truck Arrived and Checked In at Receiving Point Location (On-Carriage)](#unique_160) [page ] 268 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Arrival at receiving point was reported.Check-In at receiving point was reported. |
| [Set Ready for Warehousing](#unique_161) [page ] 270 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) |  |
| [Set Truck Checked Out and Departed at Receiving Point Location (On-Carriage)](#unique_162) [page ] 271 | Dispatcher (TM) | Monitor Execution - Freight Orders (F4368) | Checkout at receiving point was reported.Departure at receiving point was reported. |
| [Confirm Freight Costs for Accrual Postings](#unique_163) [page ] 272 | Transportation Buyer | Monitor Accrual Postings - Freight Documents (F4329) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Road

#### Outbound

##### Set Truck Arrived and Checked In at Shipping Point Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck has arrived at the supplying plant, the Dispatcher (TM) sets the execution status Set to Arrived and Set to Checked In.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori Launchpad as a Dispatcher (TM). | The SAP Fiori Launchpad displays. |  |
| 2. | Access App | In the Transportation Order Management group, choose Monitor Execution - Freight Orders (F4368). | The Monitor Execution (F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order number created in scope item 6W2 manual transportation planning> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order screen appears.Note Depending on the planning (internal or external), the following screen names appear:Internal planning: Display Road Freight OrderExternal planning:Display External Road Freight Order |  |
| 6. | Choose Edit | On the Display Road Freight Order screen, choose Edit. | The Edit Road Freight Order screen appears. |  |
| 7. | Choose Execution Status Set to Ready for Transportation Execution | Choose Execution Status > Set to Ready for Transportation Execution. | The following system messages appear:Ready for execution check completed without errorsExecution status of doc. Road Freight Order <your freight order number> set to "Ready for Transportation Execution" |  |
| 8. | Scroll to the Stages sub section. | Scroll to the Stages sub section. |  |  |
| 9. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox | For use case consignment order outbound (Scope Item 6W2), select the checkbox for the first stage. |  |
| 10. | Choose Execution Status (Source) Set to Arrived | Choose Execution Status (Source) > Set to Arrived . | The following system message appears: Arrival at stop SP_3310 was reported |  |
| 11. | Choose Execution Status (Source) Set to Checked In | Choose Execution Status (Source) > Set to Checked In . | The following system message appears: Check-In at stop SP_3310 was reported |  |
| 12. | Choose Save. | Choose Save and go back. | The following system messages appear:Data saved successfullyCharge calculation completedCost distribution completedFor use case consignment order outbound (Scope Item 6W2), the following additional system messages appear:Consignment order <your consigment order 1> createdConsignment Order <your consigment order 2> createdNote Persistent consignment orders are created automatically. The qualifier (local) is removed for all consignment orders. Scroll down to the Items section and display the consignment order by selecting the respective hyperlink. Alternatively, you can access the business documents from the Document Flow. |  |

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

##### Set Truck Checked Out and Departed at Shipping Point Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck is loaded, the Dispatcher (TM) prints the shipment documents and sets the execution status to Set to Checked Out. After the truck has left the plant, the status of the freight order is set to Set to Departed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution (F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order number> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order screen appears.Note Depending on the planning (internal or external), the following screen names appear:Internal planning: Display Road Freight OrderExternal planning:Display External Road Freight Order |  |
| 6. | Choose Edit | On the Display Road Freight Order screen, choose Edit. | The Edit Road Freight Order screen appears. |  |
| 7. | Print / Display a preview of Shipment Documents (optional) | Navigate to the Output Request tab.In the output request table, choose Display of any print document in column display.Note The system creates the output requests for the respective print documents automatically after the freight order is saved.Printing is done when the checkout event is reported, also automatically.Additional output requests can be created manually by choosing Insert. Enter the following data per table row:Output Type: <output type>Role: <carrier>Recipient: <carrier number>Form Country/Region: <source country>Form Language: <carrier language>Form Template: <form template>For triggering the printing of output requests manually, select it and choose Send Output.For use case consignment order outbound (Scope Item 6W2):For consignment order-specific printing, the system automatically creates one print form per consignment order in one common output request. In our example with two consignment orders the system creates two waybills. | The print document is opened as a PDF through the Adobe Document Service. |  |
| 8. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 9. | Select Stage checkbox | In the Stages table, select the Stage checkbox. | For use case consignment order outbound (Scope Item 6W2), select the checkbox for the first stage. |  |
| 10. | Choose Execution Status (Source) Set to Checked Out | Choose Execution Status (Source) > Set to Checked Out . | The following system message appears: Checkout at stop SP_3310 and required preceding events reported |  |
| 11. | Choose Execution Status (Source) Set to Departed | Choose Execution Status (Source) > Set to Departed . | The following system message appears: Departure at stop SP_3310 was reported |  |
| 12. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

|  |
| --- |
| Note You can revoke the checkout and departed event by setting Set to Not Checked Out and Set to Not Departed. |

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

Table 1:

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

Table 2:

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

##### Set Truck Arrived at Destination Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck has arrived at the destination location, the Dispatcher (TM) sets the execution status to Set to Arrived.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | In the Transportation Order Management group, choose Monitor Execution - Freight Orders (F4368). | The Monitor Execution (F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order number> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order screen appears.Note Depending on the planning (internal or external), the following screen names appear:Internal planning: Display Road Freight OrderExternal planning:Display External Road Freight Order |  |
| 6. | Edit Freight Order | On the Display Road Freight Order screen, choose Edit. | The Edit Road Freight Order screen appears. |  |
| 7. | Scroll to the Stages Subsection | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages Table Select the Stage Checkbox | In the Stages table, select the Stage checkbox. | For use case Consignment order outbound (Scope Item 6W2), select the checkbox for the first stage. |  |
| 9. | Choose Execution Status (Destination) Set to Arrived | Choose Execution Status (Destination ) > Set to Arrived . | The following system message appears:Arrival at stop <your destination> and required preceding events were reported. |  |
| 10. | In the Stages Table Select the Stage Checkbox (Optional) | For use case consignment order outbound (Scope Item 6W2):In the Stages table, select the Stage checkbox for the second stage. |  |  |
| 11. | Choose Execution Status (Destination) Set to Arrived (Optional) | For use case consignment order outbound (Scope Item 6W2):Choose Execution Status (Destination ) > Set to Arrived . | The following system message appears:Arrival at stop <your customer number 2> and required preceding events were reported |  |
| 12. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfullyContinue with Succeeding Processes in the Appendix Process Integration. |  |

|  |
| --- |
| Note You can revoke the arrival event by setting Set to Not Arrived. |

#### Inbound

##### Set Truck Arrived and Checked In at Receiving Point Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck has arrived at the destination location the Dispatcher (TM) sets the execution status to Set to Arrived and Set to Checked In.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution (F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order number created in scope item 6W2 - Manual Transportation Planning or 6W1 - External Transportation Planning>. |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order screen appears.Note Depending on the planning (internal or external), the following screen names appear:Internal planning: Display Road Freight OrderExternal planning: Display External Road Freight Order |  |
| 6. | Choose Edit | On the Display Road Freight Order screen, choose Edit. | The Edit Road Freight Order screen appears. |  |
| 7. | Set Execution Status | Choose Execution Status > Set to Ready for Transportation Execution. | The following system messages appear:Ready for execution check completed without errorsExecution status of doc. Road Freight Order <your freight order number> set to "Ready for Transportation Execution" |  |
| 8. | Scroll to the Stages Sub Section | Scroll to the Stages sub section. |  |  |
| 9. | In the Stages table, select the Stage Checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 10. | Choose Execution Status (Destination) Set to Arrived | Choose Execution Status (Destination ) > Set to Arrived . | The following system message appears: Arrival at stop SP_3310 was reported |  |
| 11. | Choose Execution Status (Destination) Set to Checked In | Choose Execution Status (Destination ) > Set to Checked In . | The following system message appears: Check-In at stop SP_3310 was reported |  |
| 12. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

|  |
| --- |
| Note You can revoke the arrival and check-in events by setting the status to Set toNot Arrived and Set to Not Checked In. |

##### Set Ready for Warehousing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck is unloaded, the Dispatcher (TM) sets the execution status to ready for warehouse processing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution (F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order number> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Edit Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order screen appears.Note Depending on the planning (internal or external), the following screen names appear:Internal planning: Display Road Freight OrderExternal planning: Display External Road Freight Order |  |
| 6. | Choose Edit | On the Display Road Freight Order screen, choose Edit. | The Edit Road Freight Order screen appears. |  |
| 7. | Scroll to the Stages Sub Section | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages Table, Select the Stage Checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Choose Set Ready for Warehouse Processing (Destination) | Choose Warehouse Processing Status > Set to Ready for Warehouse Processing (Destination) .Note For scope item BMY – Subcontracting, after completing the previous process step, perform process step Receive Goods from Subcontracting PO corresponding to the inbound delivery. |  |  |
| 10. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

##### Set Truck Checked Out and Departed at Receiving Point Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck has left the receiving point location, the Dispatcher (TM) sets the execution status to Set to Checked and Set to Departed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution (F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order number> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order screen appears.Note Depending on the planning (internal or external), the following screen names appear:Internal planning: Display Road Freight OrderExternal planning: Display External Road Freight Order |  |
| 6. | Choose Edit. | Choose Edit. | The Edit Road Freight Order screen appears. |  |
| 7. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Choose Execution Status (Destination) Set to Checked Out | Choose Execution Status (Destination) > Set to Checked Out . | The following system message appears: Checkout at stop SP_3310 was reported |  |
| 10. | Choose Execution Status (Destination) Set to Departed | Choose Execution Status (Destination) > Set to Departed . | The following system message appears: Departure at stop SP_3310 was reported |  |
| 11. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfullyPlease continue with Succeeding Processes in the Appendix Process Integration. |  |

|  |
| --- |
| Note You can revoke the check-out and departed event by setting Set toNot Checked Out and Set to Not Departed. |

#### Stock Transfer

##### Set Truck Arrived and Checked In at Shipping Point Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck has arrived at the supplying plant, the Dispatcher (TM) sets the execution status Set to Arrived and Set to Checked In.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution (F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order number created in scope item 6W2 manual transportation planning> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order screen appears.Note Depending on the planning (internal or external), the following screen names appear:Internal planning: Display Road Freight OrderExternal planning: Display External Road Freight Order |  |
| 6. | Choose Edit | On the Display Road Freight Order screen, choose Edit. | The Edit Road Freight Order screen appears. |  |
| 7. | Choose Execution Status Set to Ready for Transportation Execution | Choose Execution Status > Set to Ready for Transportation Execution. | The following system messages appear:Ready for execution check completed without errorsExecution status of doc. Road Freight Order <your freight order number> set to "Ready for Transportation Execution" |  |
| 8. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 9. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 10. | Choose Execution Status (Source) Set to Arrived | Choose Execution Status (Source) > Set to Arrived . | The following system message appears: Arrival at stop SP_3320 was reported |  |
| 11. | Choose Execution Status (Source) Set to Checked In | Choose Execution Status (Source) > Set to Checked In . | The following system message appears: Check-In at stop SP_3320 was reported |  |
| 12. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfullyCharge calculation completedCost distribution completed |  |

|  |
| --- |
| Note You can revoke the arrival and check-in events by setting the status to Set toNot Arrived and Set toNot Checked In. |

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

##### Set Truck Checked Out and Departed at Shipping Point Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the truck is loaded, the Dispatcher (TM) prints the shipment documents and sets the execution status to Set to Checked Out. After the truck has left the plant, the status of the freight order is set to Set to Departed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution (F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order number> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order screen appears.Note Depending on the planning (internal or external), the following screen names appear:Internal planning: Display Road Freight OrderExternal planning:Display External Road Freight Order |  |
| 6. | Choose Edit | On the Display Road Freight Order screen, choose Edit. | The Edit Road Freight Order screen appears. |  |
| 7. | Print / Display a preview of Shipment Documents (optional) | Navigate to tab Output Request.In the output request table, choose Display of any print document in column display.Note The system creates the output requests for the respective print documents automatically after the freight order is saved.Printing is done when the checkout event is reported, also automatically.Additional output requests can be created manually by choosing Insert. Enter the following data per table row:Output Type: <output type>Role: <carrier>Recipient: <carrier number>Form Country/Region: <source country>Form Language: <carrier language>Form Template: <form template>For triggering the printing of output requests manually, select it and choose Send Output. | The print document is opened as a PDF through the Adobe Document Service. |  |
| 8. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 9. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 10. | Choose Execution Status (Source) Set to Checked Out | Choose Execution Status (Source) > Set to Checked Out . | The following system message appears: Checkout at stop SP_3320 was reported |  |
| 11. | Choose Execution Status (Source) Set to Departed | Choose Execution Status (Source) > Set to Departed. . | The following system message appears: Departure at stop SP_3320 was reported |  |
| 12. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

|  |
| --- |
| Note You can revoke the check-out and departed event by setting Set to Not Checked Out and Set to Not Departed. |

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

##### Set Truck Arrived and Checked In at Receiving Point Location

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
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution (F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order number> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order screen appears.Note Depending on the planning (internal or external), the following screen names appear:Internal planning: Display Road Freight OrderExternal planning:Display External Road Freight Order |  |
| 6. | Choose Edit | On the Display Road Freight Order screen, choose Edit. | The Edit Road Freight Order screen appears. |  |
| 7. | Scroll to the Stages sub section. | Scroll to the Stages sub section. |  |  |
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

After the truck is unloaded, the Dispatcher (TM) sets the execution status to ready for warehouse processing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order number> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Edit Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order screen appears.Note Depending on the planning (internal or external), the following screen names appear:Internal planning: Display Road Freight OrderExternal planning:Display External Road Freight Order |  |
| 6. | Choose Edit | On the Display Road Freight Order screen, choose Edit. | The Edit Road Freight Order screen appears. |  |
| 7. | Scroll to the Stages sub section. | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Choose Set Ready for Warehouse Processing | Choose Warehouse Processing Status > Set to Ready for Warehouse Processing (Destination) . |  |  |
| 10. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

##### Set Truck Checked Out and Departed at Receiving Point Location

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
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution (F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order number> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order screen appears.Note Depending on the planning (internal or external), the following screen names appear:Internal planning: Display Road Freight OrderExternal planning:Display External Road Freight Order |  |
| 6. | Choose Edit. | Choose Edit. | The Edit Road Freight Order screen appears. |  |
| 7. | Scroll to the Stages sub section. | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Choose Execution Status (Destination) Set to Checked Out | Choose Execution Status (Destination) > Set to Checked Out . | The following system message appears: Checkout at stop SP_3310 was reported |  |
| 10. | Choose Execution Status (Destination) Set to Departed | Choose Execution Status (Destination) > Set to Departed . | The following system message appears: Departure at stop SP_3310 was reported |  |
| 11. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfullyPlease continue with Succeeding Processes in the Appendix Process Integration. |  |

|  |
| --- |
| Note You can revoke the check-out and departed event by setting Set to Not Checked Out and Set to Not Departed. |

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

Table 3:

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

Table 4:

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

### Rail

#### Outbound

##### Set Railcar Arrived and Checked In at Shipping Point Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the railcar has arrived at the supplying plant, the Dispatcher (TM) sets the execution status Set to Arrived and Set to Checked In.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution (F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order number created in scope item 6W2 manual transportation planning> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Rail Freight Order screen appears. |  |
| 6. | Choose Edit | On the Display Rail Freight Order screen, choose Edit. | The Edit Rail Freight Order screen appears. |  |
| 7. | Set Execution Status | Choose Execution Status > Set to Ready for Transportation Execution. | The following system messages appear:Ready for execution check completed without errorsExecution status of doc. Rail Freight Order <your freight order number> set to "Ready for Transportation Execution" |  |
| 8. | Scroll to the Stages sub section. | Scroll to the Stages sub section. |  |  |
| 9. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 10. | Choose Execution Status (Source) Set to Arrived | Choose Execution Status (Source) > Set to Arrived . | The following system message appears: Arrival at stop SP_3310 was reported |  |
| 11. | Choose Execution Status (Source) Set to Checked In | Choose Execution Status (Source) > Set to Checked In . | The following system message appears: Check-In at stop SP_3310 was reported |  |
| 12. | Choose Save. | Choose Save and go back. | The following system messages appear:Data saved successfullyCharge calculation completedCost distribution completed |  |

|  |
| --- |
| Note You can revoke the arrival and check-in events by setting the status to Not Arrived and Not Checked In. |

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

##### Set Railcar Checked Out and Departed at Shipping Point Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the railcar is loaded, the Dispatcher (TM) prints the shipment documents and sets the execution status to Set to Checked Out. After the railcar has left the plant, the status of the freight order is set to Set to Departed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution (F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order number> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Rail Freight Order screen appears. |  |
| 6. | Choose Edit | On the Display Rail Freight Order screen, choose Edit. | The Edit Rail Freight Order screen appears. |  |
| 7. | Print / Display a preview of Shipment Documents (optional) | Navigate to tab Output Request.In the output request table, choose Display of any print document in column display.Note The system creates the output requests for the respective print documents automatically after the freight order is saved.Printing is done when the check out event is reported, also automatically.Additional output requests can be created manually by choosing Insert. Enter the following data per table row:Output Type: <output type>Role: <carrier>Recipient: <carrier number>Form Country/Region: <source country>Form Language: <carrier language>Form Template: <form template>For triggering the printing of output requests manually, select it and choose Send Output. | The print document is opened as a PDF through the Adobe Document Service. |  |
| 8. | Scroll to the Stages sub section. | Scroll to the Stages sub section. |  |  |
| 9. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 10. | Choose Execution Status (Source) Set to Checked Out | Choose Execution Status (Source) > Set to Checked Out . | The following system message appears: Checkout at stop SP_3310 was reported |  |
| 11. | Choose Execution Status (Source) Set to Departed. | Choose Execution Status (Source) > Set to Departed . | The following system message appears: Departure at stop SP_3310 was reported |  |
| 12. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

|  |
| --- |
| Note You can revoke the check-out and departed event by setting Not Checked Out and Not Departed. |

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

Table 5:

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

Table 6:

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

##### Set Railcar Arrived at Customer Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the railcar has arrived at the customer location, the Dispatcher (TM) sets the execution status to Set to Arrived.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution (F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order number> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Rail Freight Order screen appears. |  |
| 6. | Edit Freight Order | On the Display Rail Freight Order screen, choose Edit. | The Edit Rail Freight Order screen appears. |  |
| 7. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Choose Execution Status (Destination) Set to Arrived | Choose Execution Status (Destination ) > Set to Arrived . | The following system message appears: Arrival at stop 33186001 was reported. |  |
| 10. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfullyPlease continue with Succeeding Processes in the Appendix Process Integration. |  |

|  |
| --- |
| Note You can revoke the arrival event by setting the status to Set to Not Arrived. |

#### Inbound

##### Set Railcar Arrived and Checked-In at Receiving Point Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

After the railcar has arrived at the destination location the Dispatcher (TM) sets the execution status to Set to Arrived and Set to Checked In.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM) | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order number created in scope item 6W2 manual transportation planning> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Rail Freight Order screen appears. |  |
| 6. | Choose Edit | On the Display Rail Freight Order screen, choose Edit. | The Edit Rail Freight Order screen appears. |  |
| 7. | Choose Execution Status Set to Ready for Transportation Execution | Choose Execution Status > Set to Ready for Transportation Execution. | The following system messages appear:Ready for execution check completed without errorsExecution status of doc. Rail Freight Order <your freight order number> set to "Ready for Transportation Execution" |  |
| 8. | Scroll to the Stages sub section. | Scroll to the Stages sub section. |  |  |
| 9. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 10. | Choose Execution Status (Destination) Set to Arrived | Choose Execution Status (Destination ) > Set to Arrived . | The following system message appears: Arrival at stop SP_3310 was reported |  |
| 11. | Choose Execution Status (Destination) Set to Checked In | Choose Execution Status (Destination ) > Set to Checked In . | The following system message appears: Check-In at stop SP_3310 was reported |  |
| 12. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

|  |
| --- |
| Note You can revoke the arrival and check-in events by setting the status to Set toNot Arrived and Set to Not Checked In. |

##### Set Ready for Warehousing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the railcar is unloaded, the Dispatcher (TM) sets the execution status to Ready for Warehouse Processing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order number> | The filter for the Monitor Execution of Freight Orders worklist is set. |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Edit Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Rail Freight Order screen appears. |  |
| 6. | Choose Edit | On the Display Rail Freight Order screen, choose Edit. | The Edit Rail Freight Order screen appears. |  |
| 7. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Choose Set Ready for Warehouse Processing (Destination) | Choose Warehouse Processing Status > Set to Ready for Warehouse Processing (Destination) . |  |  |
| 10. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

##### Set Railcar Checked-Out and Departed at Receiving Point Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the railcar has left the receiving point location, the Dispatcher (TM) sets the execution status to Set to Checked Out and Set to Departed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution (F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order number> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Rail Freight Order screen appears. |  |
| 6. | Choose Edit | Choose Edit. | The Edit Rail Freight Order screen appears. |  |
| 7. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Choose Execution Status (Destination) Set to Checked Out | Choose Execution Status (Destination) > Set to Checked Out . | The following system message appears: Checkout at stop SP_3310 was reported |  |
| 10. | Choose Execution Status (Destination) Set to Departed | Choose Execution Status (Destination) > Set to Departed . | The following system message appears: Departure at stop SP_3310 was reported |  |
| 11. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfullyPlease continue with Succeeding Processes in the Appendix Process Integration. |  |

|  |
| --- |
| Note You can revoke the checkout and departed event by setting the status to Set to Not Checked Out and Set to Not Departed. |

#### Stock Transfer

##### Set Railcar Arrived and Checked In at Shipping Point Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the railcar has arrived at the supplying plant, the Dispatcher (TM) sets the execution status Set to Arrived and Set to Checked In.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution (F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order number created in scope item 6W2 manual transportation planning> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Rail Freight Order screen appears.Note Depending on the planning (internal or external), the following screen names appear:Internal planning: Display Rail Freight OrderExternal planning: Display External Rail Freight Order |  |
| 6. | Choose Edit | On the Display Rail Freight Order screen, choose Edit. | The Edit Rail Freight Order screen appears. |  |
| 7. | Choose Execution Status Set to Ready for Transportation Execution | Choose Execution Status > Set to Ready for Transportation Execution. | The following system messages appear:Ready for execution check completed without errorsExecution status of doc. Rail Freight Order <your freight order number> set to "Ready for Transportation Execution" |  |
| 8. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 9. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 10. | Choose Execution Status (Source) Set to Arrived | Choose Execution Status (Source) > Set to Arrived . | The following system message appears: Arrival at stop SP_3320 was reported |  |
| 11. | Choose Execution Status (Source) Set to Checked In | Choose Execution Status (Source) > Set to Checked In . | The following system message appears: Check-In at stop SP_3320 was reported |  |
| 12. | Choose Save. | Choose Save and go back. | The following system messages appear:Data saved successfullyCharge calculation completedCost distribution completed |  |

|  |
| --- |
| Note You can revoke the arrival and check-in events by setting the status to Set toNot Arrived and Set toNot Checked In. |

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

##### Set Railcar Checked Out and Departed at Shipping Point Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the railcar has arrived at the supplying plant, the Dispatcher (TM) sets the execution status to Set to Arrived and Set to Checked In.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution (F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order number created in scope item 6W2 manual transportation planning> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Rail Freight Order screen appears.Note Depending on the planning (internal or external), the following screen names appear:Internal planning: Display Rail Freight OrderExternal planning: Display External Rail Freight Order |  |
| 6. | Choose Edit | On the Display Rail Freight Order screen, choose Edit. | The Edit Rail Freight Order screen appears. |  |
| 7. | Scroll to the Stages sub section. | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Choose Execution Status (Source) Set to Checked Out | Choose Execution Status (Source) > Set to Checked Out . | The following system message appears: Checkout at stop SP_3320 was reported |  |
| 10. | Choose Execution Status (Source) Set to Departed | Execution Status (Source) > Set to Departed . | The following system message appears: Departure at stop SP_3320 was reported |  |
| 11. | Choose Save. | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

|  |
| --- |
| Note You can revoke the arrival and check-in events by setting the status to Set toNot Arrived and Set to Not Checked In. |

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

##### Set Railcar Arrived and Checked In at Receiving Point Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

After the railcar has arrived at the destination location the Dispatcher (TM) sets the execution status to Set to Arrived and Set to Checked In.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution (F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order number> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Rail Freight Order screen appears.Note Depending on the planning (internal or external), the following screen names appear:Internal planning: Display Rail Freight OrderExternal planning: Display External Rail Freight Order |  |
| 6. | Choose Edit | On the Display Rail Freight Order screen, choose Edit. | The Edit Rail Freight Order screen appears. |  |
| 7. | Scroll to the Stages sub section. | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Choose Execution Status (Destination) Set to Arrived | Choose Execution Status (Destination ) > Set to Arrived . | The following system message appears: Arrival at stop SP_3310 was reported |  |
| 10. | Choose Execution Status (Destination) Set to Checked In | Choose Execution Status (Destination ) > Set to Checked In . | The following system message appears: Check-In at stop SP_3310 was reported |  |
| 11. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

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

After the railcar is unloaded, the Dispatcher (TM) sets the execution status to Set Ready for Warehouse Processing (Destination).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution (F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order number> |  |  |
| 4. | Choose Go | Choose Go. | Freight orders matching the selection criteria are displayed. |  |
| 5. | Edit Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Rail Freight Order screen appears.Note Depending on the planning (internal or external), the following screen names appear:Internal planning: Display Rail Freight OrderExternal planning: Display External Rail Freight Order |  |
| 6. | Choose Edit | On the Display Rail Freight Order screen, choose Edit. | The Edit Rail Freight Order screen appears. |  |
| 7. | Scroll to the Stages sub section. | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox |  |  |
| 9. | Choose Set Ready for Warehouse Processing (Destination) | Choose Warehouse Processing Status > Set to Ready for Warehouse Processing (Destination) . |  |  |
| 10. | Choose Save. | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

##### Set Railcar Checked Out and Departed at Receiving Point Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the railcar has left the receiving point location, the Dispatcher (TM) sets the execution status to Set to Checked Out and Set to Departed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori launchpad displays. |  |
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution (F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order number> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Rail Freight Order screen appears.Note Depending on the planning (internal or external), the following screen names appear:Internal planning: Display Rail Freight OrderExternal planning: Display External Rail Freight Order |  |
| 6. | Choose Edit. | On the Display Rail Freight Order screen, choose Edit. | The Edit Rail Freight Order screen appears. |  |
| 7. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Choose Execution Status (Destination) Set to Checked Out | Choose Execution Status (Destination) > Set to Checked Out . | The following system message appears: Checkout at stop SP_3310 was reported |  |
| 10. | Choose Execution Status (Destination) Set to Departed | Choose Execution Status (Destination) > Set to Departed . | The following system message appears: Departure at stop SP_3310 was reported |  |
| 11. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfullyPlease continue with Succeeding Processes in the Appendix Process Integration. |  |

|  |
| --- |
| Note You can revoke the checkout and departed event by setting the status to Set to Not Checked Out and Set to Not Departed |

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

Table 7:

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

Table 8:

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

### Ocean

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
| 7. | Choose Execution Status Set to Ready for Transportation Execution | Choose Execution Status > Set to Ready for Transportation Execution. | The following system messages appear:Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Pick-Up <your freight order number> set to "Ready for Transportation Execution" |  |
| 8. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 9. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 10. | Choose Execution Status (Source) Set to Arrived | Choose Execution Status (Source) > Set to Arrived . | The following system message appears: Arrival at stop SP_3310 was reported |  |
| 11. | Choose Execution Status (Source) Set to Checked In | Choose Execution Status (Source) > Set to Checked In . | The following system message appears: Check-In at stop SP_3310 was reported |  |
| 12. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfullyCharge calculation completedCost distribution completed |  |

|  |
| --- |
| Note You can revoke the arrival and check-in events by setting the status to Not Arrived and Not Checked In. |

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
| 2. | Access App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution (F4368) screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order for pick up> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Orderfor Pick-Up screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Orderfor Pick-Up screen, choose Edit. | The Edit Road Freight Order for Pick-Up screen appears. |  |
| 7. | Scroll down to the Items sub section | Scroll down to the Items sub section. |  |  |
| 8. | Select Container | In the Items table, select the Container checkbox. |  |  |
| 9. | Navigate to the Quantities tab | Navigate to the Quantities tab. |  |  |
| 10. | Enter Verified Gross Mass | Under Verified Gross Mass make the following entries:Weight: <gross weight for container item + 100> KGWeighing Method: Weighing the Packed ContainerWeighing Date/Time: <today>Person Responsible for Weighing: <name of person responsible>Partner Function: ShipperWeighing Location: <enter your location of location type loading point> |  |  |
| 11. | Choose Save | Choose Save. | The following system message appears:Data saved successfully |  |
| 12. | Navigate to the Seals tab | Navigate to the Seals tab. |  |  |
| 13. | Enter Seals Information | Under Seals make the following entries:Seal Number: ANZ4711815Sealing Date: <today> |  |  |
| 14. | Choose Save | Choose Save. | The following system message appears:Data saved successfully |  |
| 15. | Print / Display a preview of Shipment Documents (optional) | Navigate to the Output Request tab.In the output request table, choose Display of any print document in column display.Note The system creates the output requests for the respective print documents automatically after the freight order is saved.Printing is done when the check out event is reported, also automatically.Additional output requests can be created manually by choosing Insert. Enter the following data per table row:Output Type: <output type>Role: <carrier>Recipient: <carrier number>Form Country/Region: <source country>Form Language: <carrier language>Form Template: <form template>For triggering the printing of output requests manually, select it and choose Send Output. | The print document is opened as a PDF through the Adobe Document Service. |  |
| 16. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 17. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 18. | Choose Execution Status (Source) Set to Checked Out | Choose Execution Status (Source) > Set to Checked Out . | The following system message appears: Checkout at stop SP_3310 was reported |  |
| 19. | Choose Execution Status (Source) Set to Departed | Choose Execution Status (Source) > Set to Departed . | The following system message appears: Departure at stop SP_3310 was reported |  |
| 20. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

|  |
| --- |
| Note You can revoke the check-out and departed event by setting the status to Set to Not Checked Out and Set to Not Departed. |

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

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. |  |  |
| 2 | Access the App | Open Create Billing Documents (F0798). |  |  |
| 3 | Define Billing Settings | Choose Billing Settings, you can make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for billing due list | In the search condition, use criteria if necessary. |  |  |
| 5 | Select item(s) for billing | Select row(s) of SD Document created previously and choose Create Billing Documents. |  |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, for example current date, then choose OK. |  |  |
| 7 | Save Billing Document | On the Manage Billing Document screen, choose Save.The draft version billing document with TMP xxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. |  |  |

|  |
| --- |
| Note Transportation costs are now part of the billing document and can be invoiced to the customer. You can check details in the Pricing Elements section while creating the billing document. Locate the condition type, which lists the freight costs. The amount shown there should be equal to the respective amount in the freight order under Cost Distribution > Distribution Items . |

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
| 9. | Choose Execution Status (Destination) Set to Arrived | Choose Execution Status (Destination ) > Set to Arrived . | The following system message appears:Departure at stop PORT_AEYAS was reported |  |
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
| 3. | Filter Ocean Freight Booking | On the Manage Ocean Freight Bookings screen, make the following entries:Ocean Freight Booking: <freight booking number created in scope item 6W2 step perform manual transportation planning>. |  |  |
| 4. | Choose Go | On the Manage Ocean Freight Bookings screen, choose Go. | Ocean freight booking matching the selection criteria is listed. |  |
| 5. | Navigate to Ocean Freight Booking | In the Ocean Freight Bookings table, select the Ocean Freight Booking. | The Display Ocean Freight Booking screen appears. |  |
| 6. | Edit Ocean Freight Booking | On the Display Ocean Freight Booking screen, choose Edit. | The Edit Ocean Freight Booking screen appears. |  |
| 7. | Set Execution Status to Loaded | Choose Execution Status > Set to Loaded at Port of Loading. | The following system message appears:Loading End at stop PORT_AEYAS was reported |  |
| 8. | Set Execution Status to Shipped on Board | Choose Execution Status > Set to Shipped on Board . |  |  |
| 9. | Choose OK | In the Set to Shipped on Board dialog box, choose OK. | The following system message appears:Departure at stop PORT_AEYAS was reported |  |
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

Table 9:

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

Table 10:

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
| 8. | Choose Ok | In the Set to Arrived at Final Port of Discharge dialog box, choose OK. | The following system message appears:Arrival at stop PORT_AESID was reported |  |
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
| 8. | Scroll to the Stages Sub Section | Scroll to the Stages sub section. |  |  |
| 9. | In the Stages table, Select the Stage Checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 10. | Choose Execution Status (Source) Set to Departed | Choose Execution Status (Source) > Set to Departed . | The following system message appears:Departure at stop PORT_AESID and required preceding events were reported |  |
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

After the truck has arrived at the customer location, the Dispatcher (TM) sets the execution status to Set to Arrived.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Dispatcher (TM). | The SAP Fiori Launchpad opens. |  |
| 2. | Launch App | Open Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Order screen appears. |  |
| 3. | Enter Selection Criteria | On the Monitor Execution of Freight Order screen, make the following entries:Freight Order: <your freight order for delivery> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Delivery screen appears. |  |
| 6. | Edit Freight Order | On the Display Road Freight Order for Delivery screen, choose Edit. | The Edit Road Freight Order for Delivery screen appears. |  |
| 7. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 8. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 9. | Choose Execution Status (Destination) Set to Arrived | Choose Execution Status (Destination) > Set to Arrived . | The following system message appears: Arrival at stop 33186002 and required preceding events were reported |  |
| 10. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfullyPlease continue with Succeeding Processes in the Appendix Process Integration. |  |

#### Inbound

##### Arrival of Truck at Port of Loading (Pick-up)

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
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order for pick up created in scope item 6W2 manual transportation planning> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Pick-Up screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Pick-Up screen, choose Edit. | The Edit Road Freight Order for Pick-Up screen appears. |  |
| 7. | Choose Execution Status Set to Ready for Transportation Execution | Choose Execution Status > Set to Ready for Transportation Execution. | The following system messages appear:Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Pick-Up <your freight order number> set to "Ready for Transportation Execution" |  |
| 8. | Scroll to the Stages Sub Section | Scroll to the Stages sub section. |  |  |
| 9. | In the Stages table, Select the Stage Checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 10. | Choose Execution Status (Destination) Set to Arrived | Choose Execution Status (Destination ) > Set to Arrived . | The following system message appears:Arrival at stop PORT_AEYAS and required preceding events were reported |  |
| 11. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

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
| 5. | Navigate to Ocean Freight Booking | In the Ocean Freight Bookings table, select one ocean freight booking. | The Display Ocean Freight Booking screen appears. |  |
| 6. | Choose Edit | On the Display Ocean Freight Booking screen, choose Edit. | The Edit Ocean Freight Booking screen appears. |  |
| 7. | Choose Execution Status Set to Loaded at Port of Loading | Choose Execution Status > Set to Loaded at Port of Loading. | The following system message appears:Loading End at stop PORT_AEYAS was reported |  |
| 8. | Set Execution Status to Shipped on Board | Choose Execution Status > Set to Shipped on Board . |  |  |
| 9. | Choose OK | In the Set to Shipped on Board dialog box, choose OK. | The following system message appears:Departure at stop PORT_AEYAS was reported |  |
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

Table 11:

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

Table 12:

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
| 8. | Choose Ok | In the Set to Shipped on Board dialog box, choose OK. | The following system message appears:Arrival at stop PORT_AESID was reported |  |
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
| 2. | Access App | In the Dispatching group, choose Monitor Execution - Freight Orders (F4368). | The Monitor Execution of Freight Orders screen appears. |  |
| 3. | Filter Freight Orders | On the Monitor Execution of Freight Orders screen, make the following entries:Freight Order: <your freight order for delivery created in scope item 6W2 manual transportation planning> |  |  |
| 4. | Choose Go | Choose Go. | Freight order matching the selection criteria is listed. |  |
| 5. | Navigate to Freight Order | In the Freight Orders - Execution View table, select one freight order. | The Display Road Freight Order for Delivery screen appears. |  |
| 6. | Choose Edit | On the Display Road Freight Order for Delivery screen, choose Edit. | The Edit Road Freight Order for Delivery screen appears. |  |
| 7. | Choose Execution Status Set to Ready for Transportation Execution | Choose Execution Status > Set to Ready for Transportation Execution. | The following system messages appear:Ready for execution check completed without errorsExecution status of doc. Road Freight Order for Delivery <your freight order number> set to "Ready for Transportation Execution" |  |
| 8. | Scroll to the Stages sub section | Scroll to the Stages sub section. |  |  |
| 9. | In the Stages table, select the Stage checkbox | In the Stages table, select the Stage checkbox. |  |  |
| 10. | Choose Execution Status (Source) Departed | Choose Execution Status (Source) > Departed . | The following system message appears:Departure at stop PORT_AESID and required preceding events were reported |  |
| 11. | Choose Save | Choose Save and go back. | The following system messages appear:Data saved successfully |  |

|  |
| --- |
| Note You can revoke the departed event by setting the status toSet to Not Departed. |

##### Set Truck Arrived and Checked-In at Receiving Point Location (Delivery)

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

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Overview Table lists a different app for Post Goods Issue than the procedures use: Road outbound shows Monitor Accrual Postings (F4329), Rail outbound shows Manage Ocean Freight Bookings (F6213), Rail stock transfer shows F4329, Ocean outbound shows Manage Outbound Deliveries (F0867A); the procedures use VL06O (VL06O_CLOUD), F6498 or VL02N.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Ocean outbound 'Arrival of Truck at Port of Loading (Pick-Up)' step 9 expects the message 'Departure at stop PORT_AEYAS was reported' although the Overview Table expects 'Arrival at port of loading was reported'.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-transportation-execution-6w3-ae-sap-s-4hana-cloud-public-e-part-02]]
- related-to :: [[11-inventory-warehouse-and-transportation/manual-transportation-planning-6w2-ae-test-script-sap-s-4hana-cloud-pu]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-sap-s-4hana-cloud-public-edition-external-transportation-p]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6W3_S4CLD2608_BPD_EN_AE.docx` — lines 1–2769 of the extracted text · extracted with `mammoth` · 505,382 chars in the whole document
