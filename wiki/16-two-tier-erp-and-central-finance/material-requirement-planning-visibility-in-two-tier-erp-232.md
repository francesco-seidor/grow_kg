---
id: 16-two-tier-erp-and-central-finance/material-requirement-planning-visibility-in-two-tier-erp-232
title: Material Requirement Planning Visibility in Two-Tier ERP (S4CLD2608_2T_MRP_Analytics)
description: "Customer guide for the Two-Tier ERP scenario giving headquarters and subsidiary API-based visibility of each other's MRP supply and demand results."
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/supply-and-demand-planning]
aliases: [S4CLD2608_2T_MRP_Analytics]
keywords: [Two-Tier MRP Visibility and Demand Planning, mrp visibility, two-tier erp, mrp results view, communication arrangements, api integration, business application studio, cloud connector, test procedure, manufacturing scope items]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Manufacturing/S4CLD2608_2T_MRP_Analytics.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-232
topic: 16-two-tier-erp-and-central-finance/supply-and-demand-planning
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Material Requirement Planning Visibility in Two-Tier ERP (S4CLD2608_2T_MRP_Analytics)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Manufacturing/S4CLD2608_2T_MRP_Analytics.docx`, extracted with `mammoth`. Grouped under **Two-Tier MRP Visibility and Demand Planning** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP Cloud ERPJune 2026EnglishEnglish |  |
|  | Two -Tier ERP scenario: Material Requirement Planning Visibility in Two-Tier ERP |
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
| 0 | 07-12-2022 | Initial version of document |
|  |  |  |

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

[3.1 Prerequisites 8](#_Toc122457821)

[3.2 Process Flow with Technical Details 9](#_Toc122457825)

[4 Technical Requirement 10](#_Toc122457826)

[4.1 Communication arrangements 10](#_Toc122457827)

[4.2 Integration Requirements by using API’s 11](#_Toc122457828)

[5 Test Procedure 12](#_Toc122457829)

[5.1 Prerequisites 12](#_Toc122457830)

[5.1.1 System Details 12](#_Toc122457831)

[5.1.2 Creation of custom development-based integration 12](#_Toc122457832)

[5.2 Overview Table 12](#_Toc122457833)

[6 Appendix 13](#_Toc122457834)

[6.1 Relevant Scope ID’s 13](#_Toc122457835)

**Material Requirement Planning Visibility in Two-Tier ERP**

## Purpose

This accelerator document describes the Two-Tier scenario MRP Visibility between Headquarter and Subsidiary which runs on two different instances of SAP. Headquarters are expected to have better visibility on the MRP results generated at Subsidiary end and vice versa. This scenario supports the organizations running on Two-Tier setup with crucial scenarios of material demand and supply elements and calls for better control and visibility on the material demand and supply planning between Tier 1 and Tier 2 systems.

## Value Proposition

### Business Requirements

Business Enterprises implemented on Two-Tier setup where in the subsidiary runs on SAP Cloud ERP acting as Tier 2 and the headquarter running on any deployments such as SAP Cloud ERP Private, SAP S/4HANA, ECC acting as Tier 1 would like to communicate the product demand, planning and execution status between the systems.

SAP Cloud ERP deployed at subsidiary sends the demand for assembly to headquarter and in turn the headquarter receives the demand, plan, produce and deliver the same product back to subsidiary. Here, the subsidiary acts as a customer whereas the headquarter acts like a production unit and internal supplier. In this business use case, subsidiary and headquarters are not having the visibility on the material coverage between the Two-Tier companies.

Subsidiaries are expected to have better visibility on the MRP planning results of the production materials at headquarters and the headquarters are expected to access the demand planned for the materials at the Subsidiary end.

.

### Two-Tier Solution

The Two -Tier Solution provides the API based direct integration between SAP Cloud ERP system at the subsidiary and SAP Cloud ERP Private /SAP S/4HANA/SAP ECC system at Headquarters.

## Business Process Details

The process flow for the Two-Tier scenario MRP Visibility in Two-Tier ERP is as below,

**Tier-2**

- The process starts with the creation of purchase order at Tier 2 system and the demand flows to Tier 1 system via API to trigger automatic creation of sales order at Tier 1 and sends back the purchase order confirmation to Tier 2 system. Also, the sales order number will be updated in the purchase order document at Tier 2.
- Once the sales order created in Tier 1, production planner perform the MRP run to generate the planned order against the customer sales requirement. Followed by that planned order will be converted to Production order to proceed with the production activities.
- Now, Tier 2 system can access the MRP Results View app to check the status of production planning by entering the material number/sales order/MRP Element category/plant and it displays the list of replenishment elements along with stock availability for the given material/sales order number using which Tier 2 entity can act proactively to fulfil the customer requirement on time without any delay.

<!-- image omitted: unnamed -->

**Tier-1**

Let’s see here the activities at Tier 1 system which receives procurement request for the product as dependent demand from Tier 2 system where customer order is received.

- Tier 2 system receives the demand from external customer and creates customer sales order manually. Planner performs the MRP run which generates Procurement proposals at Tier 2. These procurement proposals will flow as demand to the Tier 1 system, and the production planning process follows as said above.
- Now, Tier 1 system can access the MRP Results view app by entering the material number/MRP Element category/plant and it displays the list of demands with the required stock for the given material using which Tier 1 entity can act proactively by planning for the underlying components required to produce the assembly on time.

<!-- image omitted: unnamed -->

**Fiori Application**

<!-- image omitted: unnamed -->

<!-- image omitted: unnamed -->

### Prerequisites

The following list of prerequisites are to be in place to realize the business process:

- Integration between Headquarter and Subsidiary system: With communications scenarios and API services enabled.
- Creating suitable authentication processes to ensure secure connections from SAP Cloud ERP Private to SAP Cloud ERP system and vice-versa.
- Access to BTP and subscribe the below service.

<!-- image omitted: unnamed -->

- Dev space is created in BAS (Business Application Studio)

<!-- image omitted: unnamed -->

- Connect to External Data Sources with SAP Business Application Studio. In this case we have connected Tier 1 which is an SAP S/4HANA On-premise system/ SAP Cloud ERP Private to Tier 2 which is SAP Cloud ERP.

<!-- image omitted: unnamed -->

### Process Flow with Technical Details

Following flow chart provides details of the process with integration scenario and role of

On-Premises and Cloud system in execution of the steps involved,

<!-- image omitted: unnamed -->

SAP Business Application Studio provides a tailor-made development environment for various development scenarios, such as SAP Fiori, SAP S/4HANA/ SAP Cloud ERP Private extension, and Workflow. With each of these scenarios, we can create different types of applications. It is important for both the tiers to efficiently share data between each other.

- The IDE is pre-loaded with the recommended set of extensions required for that specific scenario.
- The dev space is equipped with high-productivity development tools for the relevant business scenario e.g., wizards and templates, graphical editors, and more.
- Additional generic tools required for developing, testing running the solution are also included in the dev space – e.g., mock servers, run-time environments

## Technical Requirement

This section covers the process of setting up integration between the SAP Cloud ERP and SAP S/4 HANA system/ SAP Cloud ERP Private covering the prerequisites such as Cloud connector, Communication arrangements and API’s (Application programming interface) required to enable the direct integration between the system.

### Communication arrangements

To allow direct data communication between SAP Cloud ERP and SAP S/4 HANA system/ SAP Cloud ERP Private, a communication arrangement is created. The communication arrangement defines which system (communication system) and which user can call which APIs (communication scenarios).

The below service in enabled on Tier 1 to get the MRP results from Tier 1 and display on Tier 2.

<!-- image omitted: unnamed -->

The Below communication arrangement is enabled on Tier 2 to get the MRP data and display on Tier 1

[https://api.sap.com/api/API_MRP_MATERIALS_SRV_01/overview](https://api.sap.com/api/API_MRP_MATERIALS_SRV_01/overview)

<!-- image omitted: unnamed -->

| Communication arrangement ID | Name |
| --- | --- |
| SAP_COM_0104 | Production Planning Integration |

Cloud connector: To enable communication between SAP Cloud ERP and SAP S/4HANA system/ SAP Cloud ERP Private using Remote Function Calls (RFC) and HTTP calls, you need to enable Cloud Connector in your SAP Cloud ERP environment.

Please follow the below blog steps

[https://blogs.sap.com/2022/07/05/analytics-in-two-tier-scenario/](https://blogs.sap.com/2022/07/05/analytics-in-two-tier-scenario/)

The blog explains in detail how the set up can be done between Tier 1 and Tier 2

### Integration Requirements by using API’s

The following diagram and table below show an example of how the API’s (Application programming Interfaces) can be called between the systems,

<!-- image omitted: unnamed -->

Following table explain integration design with API’s,

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Material Planning Data - Read** |  |  |  |  |  |
| Interaction | Direction in system | Authentication | Format | Business Object | Protocol |
| Read data from Tier 1 for supply and demand information over a certain time. | Inbound | User/Password or Certificate | ODATA | Material Supply and Demand View | HTTPS |
| Read data from Tier 2 for supply and demand information over a certain time. | Inbound | User/Password or Certificate | ODATA | Material Supply and Demand View | HTTPS |

## Test Procedure

### Prerequisites

This section summarizes all prerequisites to conduct the test in terms of systems, users, master data, organizational data, and other test data and business conditions.

#### System Details

The test scenario can be built in the following Two-Tier system landscape:

| System | Details |
| --- | --- |
| SAP S/4HANA System/ SAP Cloud ERP Private - Headquarters | SAP S/4HANA On-Premise System/ SAP Cloud ERP Private (Any Version) |
| SAP Cloud ERP - Subsidiary | SAP Cloud ERP (Any Version) |

#### Creation of custom development-based integration

- Since the data is available and can be accessed via API, the customers can develop their own reports and analytics using Business Application Studio.

### Overview Table

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | MRP supply and Demand view on Tier 1 | In Tier 1 system, access the report created to fetch the MRP supply and Demand view data. Enter Filter values such as MRPElementCategory, Material and MRPPlanningSegment | Status of Production planning is available |
| 2 | MRP supply and Demand view on Tier 2 | In Tier 2 system, access the report created to fetch the MRP supply and Demand view data. Enter Filter values such as MRPElementCategory, Material and MRPPlanningSegment | List of demands with the required stock for the given material is available |

## Appendix

### Relevant Scope ID’s

The Cloud APIs are relevant for the following scope item IDs in Manufacturing.

[Make-to-Stock Production - Discrete Manufacturing(BJ5)](https://rapid.sap.com/bp/#/scopeitems/BJ5)

[Make-to-Stock - Process Manufacturing Based on Process Order (BJ8)](https://rapid.sap.com/bp/#/scopeitems/BJ8)

[Material Requirements Planning(J44)](https://rapid.sap.com/bp/#/scopeitems/J44)

[Material Requirements Planning(O44)](https://rapid.sap.com/bp/#/scopeitems/O44)

## Connections
- part-of :: [[_cluster]]
- related-to :: [[16-two-tier-erp-and-central-finance/demand-planning-with-sap-ibp-for-headquarter-subsidiary-model-252]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Manufacturing/S4CLD2608_2T_MRP_Analytics.docx` — full document · extracted with `mammoth` · 13,917 chars in the whole document
