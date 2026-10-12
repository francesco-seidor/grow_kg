---
id: 16-two-tier-erp-and-central-finance/two-tier-erp-scenario-refurbishment-with-service-customer-guide-224
title: "Two-Tier ERP scenario: Refurbishment with Service (Customer Guide) (S4CLD2608_2T_Refurbishment with Service)"
description: "Customer guide for Two-Tier ERP equipment refurbishment with service between HQ (Tier 1) and subsidiary on SAP Cloud ERP (Tier 2), with event-based integration and test steps."
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/equipment-calibration-and-refurbishment]
aliases: [S4CLD2608_2T_Refurbishment with Service]
keywords: [Two-Tier Equipment Calibration and Refurbishment, equipment refurbishment, two-tier erp, lease and rental contracts, event mesh integration, communication arrangements, maintenance orders, subcontracting, api integration, consignment]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Asset Management/S4CLD2608_2T_Refurbishment with Service.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-224
topic: 16-two-tier-erp-and-central-finance/equipment-calibration-and-refurbishment
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Two-Tier ERP scenario: Refurbishment with Service (Customer Guide) (S4CLD2608_2T_Refurbishment with Service)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Asset Management/S4CLD2608_2T_Refurbishment with Service.docx`, extracted with `mammoth`. Grouped under **Two-Tier Equipment Calibration and Refurbishment** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP Cloud ERP June 2026EnglishEnglish |  |
|  | Two -Tier ERP scenario: Refurbishment with Service |
|  | Customer Guide |

Copyright

© 2023 SAP SE or an SAP affiliate company. All rights reserved.

No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE. The information contained herein may be changed without prior notice.

Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors.

National product specifications may vary.

These materials are provided by SAP SE and its affiliated companies ("SAP Group") for informational purposes only, without representation or warranty of any kind, and SAP Group shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP Group products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty.

SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE in Germany and other countries. Please see http://www.sap.com/corporate-en/legal/copyright/index.epx#trademark for additional trademark information and notices.

| Revision | Change Date | Description |
| --- | --- | --- |
| 0 | 16-06-2025 | Initial version of document |
| 0.1 | 25-05-2026 | Update product names/process flows according to L3 |

Icons

| Icon | Meaning |
| --- | --- |
| <!-- image omitted: unnamed --> | Caution |
| <!-- image omitted: unnamed --> | Example |
| <!-- image omitted: unnamed --> | Note |
| <!-- image omitted: unnamed --> | Recommendation |
| <!-- image omitted: unnamed --> | Syntax |

Typographic Conventions

| Type Style | Description |
| --- | --- |
| Example text | Words or characters that appear on the screen. These include field names, screen titles, pushbuttons as well as menu names, paths and options.Cross-references to other documentation. |
| Example text | Emphasized words or phrases in body text, titles of graphics and tables. |
| EXAMPLE TEXT | Names of elements in the system. These include report names, program names, transaction codes, table names, and individual key words of a programming language, when surrounded by body text, for example, SELECT and INCLUDE. |
| Example text | Screen output. This includes file and directory names and their paths, messages, source code, names of variables and parameters as well as names of installation, upgrade and database tools. |
| EXAMPLE TEXT | Keys on the keyboard, for example, function keys (such as F2) or the ENTER key. |
| Example text | Exact user entry. These are words or characters that you enter in the system exactly as they appear in the documentation. |
| <Example text> | Variable user entry. Pointed brackets indicate that you replace these words and characters with appropriate entries. |

Content

[1 Purpose 5](#_Toc1370974302)

[2 Value Proposition 5](#_Toc44653241)

[2.1 Business Requirements 5](#_Toc42458831)

[2.2 Two-Tier Solution 6](#_Toc1865169671)

[3 Business Process Details 6](#_Toc1001392179)

[3.1 Prerequisites 10](#_Toc1962205967)

[3.2 Process Flow with Technical Details 10](#_Toc374211422)

[4 Technical Requirement 10](#_Toc636143946)

[4.1 Communication arrangements 11](#_Toc641173716)

[4.2 Integration Requirements by using API’s 11](#_Toc1779655975)

[5 Test Procedure 12](#_Toc435033476)

[5.1 Prerequisites 13](#_Toc2121476936)

[5.1.1 System Details 13](#_Toc1442709348)

[5.1.2 Creation of custom development-based integration 13](#_Toc1609831200)

[5.2 Overview Table 13](#_Toc1432372977)

[6 Appendix 15](#_Toc1997599202)

[6.1 Relevant Scope ID’s 15](#_Toc107084266)

**Integrated Multiple Specification Inspection in Two-Tier ERP**

## Purpose

Two-Tier ERP solution for the process of Equipment Refurbishment with sales & services integration in SAP S/4HANA Cloud from headquarters to subsidiary which run on two different instances of SAP

There are two scenarios-One is, where the equipment is owned by headquarters and is leased out to the subsidiary for usage and maintenance, is sent to Headquarters in case of refurbishment. Second scenario is where a customer has rented the equipment, and servicing

happens at the subsidiary and in case the equipment needs to be refurbished it is sent to headquarters for refurbishment. This scenario supports organizations running on Two-Tier setup to have better coverage on Refurbishment process between Tier 1 and Tier 2 systems.

## Value Proposition

### Business Requirements

In an ever-evolving business model Customer or Supplier require equipment for usage or manufacturing activities from specific Machine Manufactures for long term on rent /Lease basis to avoid capital expenditure.  Hence OEMs or headquarters provide equipment on rental basis for a particular lease duration. Since the machine is owned by the headquarter periodic maintenance must be ensured.

Scenario 1:

Headquarters leases out a high value equipment to the subsidiary on lease basis for a particular time with subsidiary paying monthly rents and spending on equipment maintenance. There is an equivalent lease-in contract at the subsidiary with automatic creation of asset master and manual creation of Equipment master. During Asset maintenance in case the equipment needs refurbishment, it is sent to headquarters for Refurbishment

Scenario 2:

To understand better, customer places a contract with the subsidiary for an equipment. Equipment is delivered to the customer as a consignment and updated in master as equipment at customer location. The parameters or indicators are maintained in the equipment master. The subsidiary is informed of the repair or service required with the customer and equipment details. Monthly rentals are charged against the contracts for the period equipment is at customer location. Between the customer and subsidiary, vendor invoicing is done for the service or repair carried out on the equipment. The subsidiary decides if the equipment needs repair or refurbishment during annual equipment maintenance through service order. In case of repair, in-house repair is carried out at subsidiary and in case of refurbishment, the damaged equipment is sent to headquarters for Refurbishment with headquarters sending the replaced equipment back to customer via subsidiary.

Business Enterprises implemented with Two-Tier ERP scenario involving Equipment refurbishment and setup wherein the subsidiary runs on SAP Cloud ERP acting as Tier 2 and the Headquarter running on any deployments such as SAP Cloud ERP Private, SAP S/4HANA, or SAP ECC or any other ERP system acting as Tier 1 which can cater to refurbishment of Leased/Rented equipment.

SAP Cloud ERP system plans the refurbishment schedule for the equipment and notifies the Headquarter whenever the equipment is due for refurbishment. The Headquarter on the other hand refurbishes the equipment.

### Two-Tier Solution

To achieve the above s requirement, SAP’s Two -Tier Solution provides the SAP MDI,Event based direct integration between SAP Cloud ERP system at the subsidiary and SAP S/4HANA / SAP Cloud ERP / SAP ECC/other ERP system at the Headquarter.

## Business Process Details

The process flow for the Refurbishment with Service in Two-Tier ERP is as below,

**Scenario 1**

To achieve the above requirement, SAP’s Two -Tier ERP Solution provides direct integration between SAP Cloud ERP system at the subsidiary and SAP S/4HANA / SAP Cloud ERP / SAP ECC/other ERP system at the Headquarter.

Let’s see the process flow,

Maintenance Order for Refurbishment

Tier 1

Tier 2

Equipment for Refurbishment

Replacement Equipment

Lease contract

<!-- image omitted: unnamed -->

**Tier-2**

- An equivalent leased in contract is created at subsidiary along with an asset master. An equipment created manually referencing to the asset.
- In due course if the maintenance team sees a need that requires the equipment to be refurbished a maintenance order for refurbishment is created at subsidiary.
- This maintenance order will create an event. This event is sent to Event Mesh and is replicated to Tier 1. The data replication is done by capturing the event using an AMQP adapter in an integration flow and then replicating the maintenance order to Tier 1 via an OData service to create the Refurbishment order
- At subsidiary, with reference to maintenance order a subcontracting Purchase requisition and purchase order is created for replacement material and material to be refurbished as a component
- A transfer posting is done to transfer the damaged material to Vendor stock
- On Goods Receipt of Purchase order will move the damaged material out of vendor stock and receipt of replacement material
- The lease on damaged material can be ended and lease can be created for replacement material.
- The maintenance order will be completed and settled.

**Tier-1**

Let’s see here the activities at Tier 1 system which is notified of the equipment that is due for refurbishment.

- Tier 1 system receives the notification with maintenance order that the damaged material has to be refurbished
- Now, a refurbishment order is created by the Headquarters to carry out the in house refurbishment process for the equipment.
- Refurbishment process in carried out and refurbished material is maintained at the stock.

This way we can cater to refurbishment services provided by Headquarters for the Leased/Rented equipment with Two-Tier scenario.

**Scenario 2**:

In this scenario we have a rented equipment at customers location and the servicing happens at subsidiary that is on SAP Cloud ERP and refurbishment happens at headquarters which is on SAP Cloud ERP Private.

Your Customer

Tier 1

Tier 2

Place Order

Consignment pick-up /Return

Replacement equipment

Maintenance order for Refurbishment

Equipment for Refurbishment

Type of Service?

3XK- In House Repair

Refurbishment

Repair

<!-- image omitted: unnamed -->

**Tier 2**

- Customer places an order and rental contract is created with the material, contract duration and monthly rental to be paid as a periodic plan.
- Consignment Fill-up order is created against the rental contract. Delivery Document is created for shipping the material to the customer. During PGI serial number is added.
- Post PGI, equipment status for the serial number is updated to customer location with the customer details.
- An annual maintenance plan is created that creates the periodic service orders
- For servicing of the equipment through consignment pick up the equipment is moved to the subsidiary and in case of repair a repair order is created and if it needs a refurbishment, a maintenance order for refurbishment is created.
- This maintenance order will create an event. This event is sent to Event Mesh and is replicated to Tier 1. The data replication is done by capturing the event using an AMQP adapter in an integration flow and then replicating the maintenance order to Tier 1 via an OData service to create the Refurbishment order
- At subsidiary, with reference to maintenance order a subcontracting Purchase requisition and purchase order is created for replacement material and material to be refurbished as a component
- A transfer posting is done to transfer the damaged material to Vendor stock
- On Goods Receipt of Purchase order will move the damaged material out of vendor stock and receipt of replacement material
- This replacement material will be sent back to the Customer via consignment return with respect to service order which was created earlier.
- With respect to replaced material a new rental contract will be created and the rental contract for damaged material will be terminated.

**Tier-1**

Let’s see here the activities at Tier 1 system which is notified of the equipment that is due for refurbishment.

- Tier 1 system receives the notification with maintenance order that the damaged material must be refurbished
- Now, a refurbishment order is created by the Headquarters to carry out the in-house refurbishment process for the equipment.
- Refurbishment process in carried out and refurbished material is maintained at the stock.

When implementing Equipment Refurbishment as a process across a Two-Tier ERP architecture, especially with sales & services integration between headquarters and a subsidiary running different ERP instances, there are several strategic and operational benefits.

- End-to-End Process Visibility: Integration between HQ and subsidiary ERPs ensures real-time tracking of equipment
- Optimized Refurbishment Workflow: Refurbishment requests can be initiated at the subsidiary (where equipment is handled) and approved/tracked by HQ.
- Seamless Sales & Service Integration
- Process Automation & Reduced Manual Errors: With API /Advanced event mesh technology data is exchanged automatically:
- Reduces manual data entry and errors common in disconnected systems.
- Efficient Inventory & Logistics Coordination: Minimizes downtime and maximizes refurbishment throughput

### Prerequisites

The following list of prerequisites are to be in place to realize the business process:

- Integration between Headquarter and Subsidiary system: With communications scenarios and events, API services enabled.
- Creating suitable authentication processes to ensure secure connections from SAP S/4HANA on-premises to SAP Cloud ERP system and vice-versa.
- Access to BTP and subscription to CI and Event Mesh.

### Process Flow with Technical Details

Following flow chart provides details of the process with integration scenario and role of

On-Premises and Cloud system in execution of the steps involved,

**SAP Cloud ERP to SAP S/4HANA**

Post Maintenance Order

Maintenance Order Event

<!-- image omitted: unnamed -->

<!-- image omitted: unnamed -->

Leverage SAP Event Mesh to replicate data from Subsidiary which is on SAP Cloud ERP to Headquarter on SAP S/4HANA and vice versa. Events can be utilized to trigger the document creation here creation of maintenance order in the corresponding SAP S/4HANA system which can be captured using the Advanced Message Queuing Protocol (AMQP) adapter in SAP Cloud Integration. Details of the events can then be read using OData APIs and can be replicated in Two-Tier landscape. SAP Event Mesh allows scalable, flexible, reliable data transmission with improved performance and monitoring capabilities for extension and integration scenarios.

## Technical Requirement

This section covers the process of setting up integration between the SAP Cloud ERP and SAP S/4HANA On-Premises system/SAP Cloud ERP Private covering the prerequisites such as Cloud connector, Communication arrangements and API’s (Application programming interface) required to enable the direct integration between the system.

### Communication arrangements

To allow direct data communication between SAP Cloud ERP and SAP S/4HANA On-Premises system/SAP Cloud ERP Private, a communication arrangement is created. The communication arrangement defines which system (communication system) and which user can call which APIs (communication scenarios).

The below service in enabled on Headquarter to create Maintenance Order in Headquarter

<!-- image omitted: unnamed -->

The Below communication arrangement is enabled on Subsidiary to get the Maintenance Order Data

[https://api.sap.com/api/CE_API_MAINTENANCEORDER_0002/overview](https://api.sap.com/api/CE_API_MAINTENANCEORDER_0002/overview)

| Communication arrangement ID | Name |
| --- | --- |
| SAP_COM_0397 | Maintenance Processing Integration |

Cloud connector: To enable communication between SAP Cloud ERP and SAP S/4HANA On-Premises system/SAP Cloud ERP Private using Remote Function Calls (RFC) and HTTP calls, you need to enable Cloud Connector in your SAP S/4HANA Cloud environment.

Please follow the below blog steps

[https://blogs.sap.com/2022/07/05/analytics-in-two-tier-scenario/](https://blogs.sap.com/2022/07/05/analytics-in-two-tier-scenario/)

The blog explains in detail how the set up can be done between Tier 1 and Tier 2

Cloud Integration: In Cloud Integration , create iFlows to fetch the data of maintenance order based on the event received from the SAP Cloud ERP Edition and do the mappings to post the data in SAP Cloud ERP.

### Integration Requirements by using API’s

The following diagram and table below show an example of how the API’s (Application programming Interfaces) can be called between the systems

<!-- image omitted: unnamed -->

<!-- image omitted: unnamed -->

Following table explain integration design with API’s,

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Material Planning Data - Read** |  |  |  |  |  |
| Interaction | Direction in system | Authentication | Format | Business Object | Protocol |
| Read data from Subsidiary for Maintenance Order | Inbound | User/Password or Certificate | ODATA | Maintenance Order | HTTPS |
| Post Data in Headquarter for Maintenance Order | Inbound | User/Password or Certificate | ODATA | Maintenance Order | HTTPS |

## Test Procedure

### Prerequisites

This section summarizes all prerequisites to conduct the test in terms of systems, users, master data, organizational data, and other test data and business conditions.

#### System Details

The test scenario can be built in the following Two-Tier system landscape:

| System | Details |
| --- | --- |
| SAP S/4HANA On-Premise /Private Cloud System/Headquarters | SAP S/4HANA On-Premise /SAP Cloud ERP Pvt Edition |
| SAP Cloud ERP - Subsidiary | SAP Cloud ERP (Any Version) |

#### Creation of custom development-based integration

- No custom development as such

### Overview Table

**Scenario 1**

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Create Lease out contract on Tier 1 | In Tier 1 System, go to Recn transaction to create a lease out contract | Lease out contract is created |
| 2 | Create a lease in contract in Tier 2 | In Tier 2 System, go to Recn transaction to create a lease in contract | Lease in contract created with asset master |
| 3 | Create an equipment master in tier2 | Using create technical object an equipment master created linking the lease in contract and serialized material | Equipment master created with required details |
| 4 | Create a maintenance notification and relevant reactive maintenance order for refurbishment in Tier2 | Create a maintenance notification and relevant reactive maintenance order for refurbishment | Maintenance order is created with maintenance activity type indicating external refurbishment which is replicated to Tier 1 |
| 5 | Create a subcontracting PR/PO on tier 2 | For the material to be replaced/refurbished create a subcontracting PR/PO with relevant type of subcontracting and component details | Subcontracting PR/PO created |
| 6 | Transfer posting on subcontracting PO tier2 | In Tier2 do a transfer posting to move the damaged material to vendor stock | Transfer posting completed |
| 7 | On Tier 2 system, do a Goods receipt on subcontracting PO | A Goods receipt of subcontracting PO moves out the damaged material and brings in the replaced material | Goods receipt on subcontracting PO completed |
| 8 | On Tier1, create a suborder of type refurbishment and add the damaged material | Create suborder of type Refurbishment and add material | Refurbishment order created |
| 9 | Move material to damaged stock in tier1 | In Tier1 system, move damaged material to stock with 262 movement | Damage material moved to stock |
| 10 | Carry out refurbishment and move the refurbished material to stock | In tier1, after refurbishment move refurbished part to stock | Refurbished part move to stock for HQ usage |

**Scenario 2**

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Create Rental contract on Tier 2 | In Tier 1 System, go to Recn transaction to create a rental contract | Rental contract is created |
| 2 | Create consignment fill up order against rental contract in Tier 2 | In Tier 2 System, create a consignment fill up order against delivery | Consignment fill up order created |
| 3 | Create Delivery Document in Tier 2 | Create Delivery Document for shipping the material to the customer | Delivery Document is created for shipping the material to the customer |
| 4 | Post Goods Issue | Post goods issue | Goods issue posted |
| 5 | Create Annual maintenance plan in tier2 | Create Annual maintenance plan in tier2 | Maintenance plan is created |
| 6 | Schedule maintenance plan in tier 2 | Schedule maintenance plan in tier 2 | Due service order created by system |
| 7 | Create a consignment pickup order in tier 2 | Create a consignment pickup order in tier 2 to pickup the material under service from customer location | Consignment pick up order created |
| **Refurbishment** |  |  |  |
| 1 | Create a maintenance notification and relevant reactive maintenance order for refurbishment in Tier2 | Create a maintenance notification and relevant reactive maintenance order for refurbishment | Maintenance order is created with maintenance activity type indicating external refurbishment which is replicated to Tier 1 |
| 2 | Create a subcontracting PR/PO on tier 2 | For the material to be replaced/refurbished create a subcontracting PR/PO with relevant type of subcontracting and component details | Subcontracting PR/PO created |
| 3 | Transfer posting on subcontracting PO tier2 | In Tier2 do a transfer posting to move the damaged material to vendor stock | Transfer posting completed |
| 4 | On Tier 2 system, do a Goods receipt on subcontracting PO | A Goods receipt of subcontracting PO moves out the damaged material and brings in the replaced material | Goods receipt on subcontracting PO completed |
| 5 | On Tier1, create a suborder of type refurbishment and add the damaged material | Create suborder of type Refurbishment and add material | Refurbishment order created |
| 6 | Move material to damaged stock in tier1 | In Tier1 system, move damaged material to stock with 262 movement | Damage material moved to stock |
| 7 | Carry out refurbishment and move the refurbished material to stock | In tier1, after refurbishment move refurbished part to stock | Refurbished part moves to stock for HQ usage |
| 8 | Create a consignment return at tier 2 | At tier 2 create consignment return order to hand the replacement material to customer | Consignment return order created. |
| **Repair** |  |  |  |
| In case of Repair follow in house repair process 3XK |  |  |  |

## Appendix

### Relevant Scope ID’s

The Cloud APIs,events are relevant for the following scope item IDs in Asset Management/sales

[**3D2**](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2502/SolP/3D2?region=DE)**,**[**4HH**](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2502/SolP/4HH?region=DE)**,**[**3XK**](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2502/SolP/3XK?region=DE)

**Links**

[SAP Event Mesh](https://help.sap.com/docs/SAP_EM?locale=en-US)

[Events in SAP Cloud ERP](https://api.sap.com/products/SAPS4HANACloud/events/events)

[Events in SAP S/4HANA](https://api.sap.com/products/SAPS4HANA/events/events)

## Connections
- part-of :: [[_cluster]]
- related-to :: [[16-two-tier-erp-and-central-finance/equipment-calibration-in-two-tier-erp-223]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Asset Management/S4CLD2608_2T_Refurbishment with Service.docx` — full document · extracted with `mammoth` · 23,407 chars in the whole document
