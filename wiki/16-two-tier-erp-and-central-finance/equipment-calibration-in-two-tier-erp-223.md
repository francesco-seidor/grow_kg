---
id: 16-two-tier-erp-and-central-finance/equipment-calibration-in-two-tier-erp-223
title: Equipment Calibration in Two-Tier ERP (S4CLD2608_2T_Equip_Calibration)
description: "Customer guide for the Two-Tier ERP equipment calibration scenario between subsidiary (SAP Cloud ERP) and headquarters, with event-based integration and test steps."
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/equipment-calibration-and-refurbishment]
aliases: [S4CLD2608_2T_Equip_Calibration]
keywords: [Two-Tier Equipment Calibration and Refurbishment, equipment calibration, two-tier erp, calibration process flow, maintenance notification replication, event mesh integration, communication arrangements, api integration, test procedure, proactive maintenance]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Asset Management/S4CLD2608_2T_Equip_Calibration.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-223
topic: 16-two-tier-erp-and-central-finance/equipment-calibration-and-refurbishment
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Equipment Calibration in Two-Tier ERP (S4CLD2608_2T_Equip_Calibration)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Asset Management/S4CLD2608_2T_Equip_Calibration.docx`, extracted with `mammoth`. Grouped under **Two-Tier Equipment Calibration and Refurbishment** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP Cloud ERP June 2026English |  |
|  | Two -Tier ERP scenario: Equipment Calibration in Two-Tier ERP |
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
| 0 | 16-06-2023 | Initial version of document |
| 0.1 | 25-05-2026 | Update product names/ process flows according to L3 |

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

[1 Purpose 6](#_Toc122457816)

[2 Value Proposition 6](#_Toc122457817)

[2.1 Business Requirements 6](#_Toc122457818)

[2.2 Two-Tier Solution 6](#_Toc122457819)

[3 Business Process Details 6](#_Toc122457820)

[3.1 Prerequisites 9](#_Toc122457821)

[3.2 Process Flow with Technical Details 9](#_Toc122457825)

[4 Technical Requirement 19](#_Toc122457826)

[4.1 Communication arrangements 19](#_Toc122457827)

[4.2 Integration Requirements by using API’s 20](#_Toc122457828)

[5 Test Procedure 20](#_Toc122457829)

[5.1 Prerequisites 20](#_Toc122457830)

[5.1.1 System Details 21](#_Toc122457831)

[5.1.2 Creation of custom development-based integration 21](#_Toc122457832)

[5.2 Overview Table 21](#_Toc122457833)

[6 Appendix 22](#_Toc122457834)

[6.1 Relevant Scope ID’s 22](#_Toc122457835)

**Equipment Calibration in Two-Tier ERP**

## Purpose

This document outlines the Two-Tier scenario of Equipment calibration between headquarters and subsidiary which run on two different instances of SAP. This scenario is beneficial in case of calibration, where the test equipment is owned and is sent to Headquarters for calibration and is leased/rented out to subsidiary. Subsidiaries are expected to gain better visibility on the Calibration results generated at Headquarter end and vice versa. This scenario supports organizations running on Two-Tier setup to have better coverage on Calibration process between Tier 1 and Tier 2 systems.

## Value Proposition

### Business Requirements

Business Enterprises implemented with Two-Tier scenario involving Equipment calibration and setup wherein the subsidiary runs on SAP Cloud ERP acting as Tier 1 and the Headquarter running on any deployments such as SAP Cloud ERP Private, SAP S/4HANA, or SAP ECC system acting as Tier 2 which can cater to calibration of Leased/Rented Test equipment.

SAP Cloud ERP system plans the calibration schedule for the test equipment and notifies the Headquarter whenever the equipment is due for calibration. The Headquarter on the other hand calibrates the equipment, captures the values for Master Inspection characteristics and generates the calibration label and certificate. Headquarter can share the certificate for calibration and the in the subsidiary SAP Cloud ERP system this quality certificate can be attached to the maintenance order created for calibration. This is how the process concludes.

### Two-Tier Solution

To achieve the above s requirement, SAP’s Two -Tier Solution provides direct integration for transactions between SAP Cloud ERP system at the subsidiary and SAP S/4HANA / SAP Cloud ERP / SAP ECC/other ERP system at the Headquarters.

## Business Process Details

The process flow for the Equipment Calibration in Two-Tier ERP is as below,

**Tier-2**

- The Test equipment in Tier 2 will have a Time-based Maintenance plan created with required details linking the equipment and task list and scheduled accordingly. Based on the schedule the maintenance Plan will generate notification for the due calibration tasks.
- This due notification will create an event. This event is sent to Event Mesh and is replicated to Tier 1. The data replication is done by capturing the event using an AMQP adapter in an integration flow and then replicating the notification to Tier 1 via an OData service to create the notification.
- A maintenance order with activity type as calibration is created.
- Once Headquarters provide the quality certificate, it is attached to the maintenance order.

**Tier-1**

Let’s see here the activities at Tier 1 system which is notified of the equipment that is due for calibration.

- Tier 1 system receives the notification that the test equipment is due for calibration.
- Now, a calibration order is created by the Headquarters to carry out the calibration process for the test equipment. A designated task list is added at the order creation.
- Inspection lot is generated at the order release and Result recording, usage decision is carried out on the inspection lot.
- Subsequently calibration label and certificate are generated.
- In case of failure on the result recording the test, equipment is recalibrated.
- Headquarters also provides the calibration certificate.

This way we can cater to calibration services provided by Headquarters for the Leased/Rented test equipment with Two-Tier scenario

Generate Quality Certificate

and Label

**Tier 1**

**Subsidiary**

**Headquarters**

Calibration Notification/

Calibration Order

Maintenance plan & Due Calibration Notification

Attach Quality Certificate

Usage Decision on Inspection Lot

Result Recording on Inspection Lot

**Tier 2**

Create Maintenance Order

<!-- image omitted: unnamed --><!-- image omitted: unnamed -->

<!-- image omitted: unnamed -->

### Prerequisites

The following list of prerequisites are to be in place to realize the business process:

- Integration between Headquarter and Subsidiary system: With communications scenarios and events, API services enabled.
- Creating suitable authentication processes to ensure secure connections from SAP S/4HANA on-premises to SAP Cloud ERP system and vice-versa.
- Access to BTP and subscribe the below services.

<!-- image omitted: unnamed --> <!-- image omitted: unnamed -->

<!-- image omitted: unnamed -->

- Provision an instance of Cloud Integration in Integration Suite
- Subscribe to the event “sap/s4/beh/maintenancenotification/v1/MaintenanceNotification/Created/*” as an outbound topic in the application “Enterprise Event Enablement” in SAP Cloud ERP
- Activate Scope item INN

### Process Flow with Technical Details

Following flow chart provides details of the process with integration scenario and role of

On-Premises and Cloud system in execution of the steps involved,

**SAP Cloud ERP to SAP S/4HANA**

<!-- image omitted: unnamed -->

<!-- image omitted: unnamed -->

The below document explains how maintenance notification can be replicated from SAP Cloud ERP to SAP S/4HANA using event mesh.

<!-- image omitted: unnamed -->

## Technical Requirement

This section covers the process of setting up integration between the SAP Cloud ERP and SAP S/4 HANA On-Premises system/SAP Cloud ERP Private covering the prerequisites such as Cloud connector, Communication arrangements and API’s (Application programming interface) required to enable the direct integration between the system.

### Communication arrangements

To allow direct data communication between SAP Cloud ERP and SAP S/4 HANA On-Premises system/SAP Cloud ERP Private, a communication arrangement is created. The communication arrangement defines which system (communication system) and which user can call which APIs (communication scenarios).

The below service in enabled on Tier 1 read and create the maintenance notification in Tier 1 based on events created in Tier2.

<!-- image omitted: unnamed -->

The Below communication arrangement is enabled on Tier 2

<!-- image omitted: unnamed -->

| Communication arrangement ID | Name |
| --- | --- |
| SAP_COM_0397 | Maintenance Processing Integration |

Cloud connector: To enable communication between SAP Cloud ERP and SAP S/4 HANA On-Premises system/SAP Cloud ERP Private using Remote Function Calls (RFC) and HTTP calls, you need to enable Cloud Connector in your SAP S/4HANA Cloud environment.

### Integration Requirements by using API’s

The following diagram and table below show an example of how the API’s (Application programming Interfaces) can be called between the systems,

<!-- image omitted: unnamed -->

<!-- image omitted: unnamed -->

Following table explain integration design with API’s,

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Maintenance Notification Data - Read** |  |  |  |  |  |
| Interaction | Direction in system | Authentication | Format | Business Object | Protocol |
| Read data from Tier 2 for maintenance Notification. | Inbound | User/Password or Certificate | ODATA | Maintenance Notification | HTTPS |

## Test Procedure

### Prerequisites

This section summarizes all prerequisites to conduct the test in terms of systems, users, master data, organizational data, and other test data and business conditions.

#### System Details

The test scenario can be built in the following Two-Tier system landscape:

| System | Details |
| --- | --- |
| SAP S/4HANA On-Premise System/SAP Cloud ERP Private - Headquarters | SAP S/4HANA On-Premise System/SAP Cloud ERP Private (Any Version) |
| SAP Cloud ERP - Subsidiary | SAP S/4 HANA Cloud ERP(Any Version) |

#### Creation of custom development-based integration

- No custom development as such

### Overview Table

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Create Task list (Optional)and Maintenance Plan for the Test equipment in Tier 2 System | In Tier 2 system, Create a task list or only time-based maintenance plan | List of demands with the required stock for the given material is available |
| 2 | Schedule Maintenance plan in Tier 2 | Schedule Maintenance plan in Tier2 System, which triggers a maintenance notification | Maintenance Notification replicated to Tier 1 system |
| 3 | Create manual calibration order in Tier 1 System | In Tier1 system create a calibration order with respect to above replicated notification and release (Automatic Task list is added-Enhancement/ add Task list manually) | Inspection lot generated on Order release |
| 4 | Result Recording and Usage Decision | For the above Inspection lot, carry out Result recording and Usage Decision | Result Recording and usage decision done |
| 5 | Print calibration Certificate and Label | In Tier1 system print calibration certificate and Label | Certificate and label printed |
| 6 | On Tier 2 system ,create a maintenance order | On Tier 2 system ,create a maintenance order manually with respect to Maintenance notification generated out of maintenance Plan | Maintenance Order created |
| 7 | Attach Quality certificate | In Tier2 system, attach the quality certificate provided to the Maintenance Order | Quality Certificate attached |

## Appendix

### Relevant Scope ID’s

The Cloud APIs,events are relevant for the following scope item IDs in Asset Management

[Proactive Maintenance (‏4HI‏)](https://rapid.sap.com/bp/#/browse/categories/sap_s%254hana/areas/cloud/packageversions/BP_CLD_ENTPR/S4CLD/2302/US/29/EN/scopeitems/4HI)

[Preventive Maintenance (‏BJ2‏)](https://rapid.sap.com/bp/#/browse/categories/sap_s%254hana/areas/cloud/packageversions/BP_CLD_ENTPR/S4CLD/2302/US/29/EN/scopeitems/BJ2)

## Connections
- part-of :: [[_cluster]]
- related-to :: [[16-two-tier-erp-and-central-finance/two-tier-erp-scenario-refurbishment-with-service-customer-guide-224]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Asset Management/S4CLD2608_2T_Equip_Calibration.docx` — full document · extracted with `mammoth` · 13,609 chars in the whole document
