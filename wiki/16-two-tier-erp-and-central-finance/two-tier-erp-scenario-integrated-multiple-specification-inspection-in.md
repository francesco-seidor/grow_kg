---
id: 16-two-tier-erp-and-central-finance/two-tier-erp-scenario-integrated-multiple-specification-inspection-in
title: "Two-Tier ERP scenario: Integrated Multiple Specification Inspection in Two-Tier ERP (S4CLD2608_2T_Int Multi_Spec Insp)"
description: Customer guide for a Two-Tier ERP scenario where a subsidiary on SAP Cloud ERP orders from a headquarter that produces and inspects against country-specific quality standards via APIs.
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/multiple-specification-inspection]
aliases: [S4CLD2608_2T_Int Multi_Spec Insp]
keywords: [Two-Tier Multiple Specification Inspection, two-tier erp, multiple specification inspection, quality certificates, communication arrangements, api integration, supplier batch, inbound delivery, scope items, batch classification]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Manufacturing/S4CLD2608_2T_Int Multi_Spec Insp.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-231
topic: 16-two-tier-erp-and-central-finance/multiple-specification-inspection
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Two-Tier ERP scenario: Integrated Multiple Specification Inspection in Two-Tier ERP (S4CLD2608_2T_Int Multi_Spec Insp)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Manufacturing/S4CLD2608_2T_Int Multi_Spec Insp.docx`, extracted with `mammoth`. Grouped under **Two-Tier Multiple Specification Inspection** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP Cloud ERP June 2026EnglishEnglish |  |
|  | Two -Tier ERP scenario: Integrated Multiple Specification Inspection in Two-Tier ERP |
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

[1 Purpose 6](#_Toc138874010)

[2 Value Proposition 6](#_Toc138874011)

[2.1 Business Requirements 6](#_Toc138874012)

[2.2 Two-Tier ERP Solution 6](#_Toc138874013)

[3 Business Process Details 6](#_Toc138874014)

[3.1 Prerequisites 8](#_Toc138874015)

[3.2 Process Flow with Technical Details 8](#_Toc138874019)

[4 Technical Requirement 9](#_Toc138874020)

[4.1 Communication arrangements 9](#_Toc138874021)

[4.2 Integration Requirements by using API’s 10](#_Toc138874022)

[5 Test Procedure 11](#_Toc138874023)

[5.1 Prerequisites 11](#_Toc138874024)

[5.1.1 System Details 11](#_Toc138874025)

[5.1.2 Creation of custom development-based integration 12](#_Toc138874026)

[5.2 Overview Table 12](#_Toc138874027)

[6 Appendix 13](#_Toc138874028)

[6.1 Relevant Scope ID’s 13](#_Toc138874029)

**Integrated Multiple Specification Inspection in Two-Tier ERP**

## Purpose

This document outlines the Two-Tier scenario, which involves integrating multiple specification inspections between a Headquarter and Subsidiary, using two distinct instances of SAP. This scenario is particularly beneficial for organizations operating in a two-tier structure, where the subsidiary interacts directly with customers by receiving demand and subsequently shares it with the Headquarters. The Headquarters is responsible for manufacturing and inspecting the products, ensuring compliance with country-specific quality standards.

## Value Proposition

### Business Requirements

Business Enterprises operating in a Two-Tier setup have implemented a system where the subsidiary utilizes SAP Cloud ERP as Tier 2, while the headquarter runs on either of the various deployments such as SAP Cloud ERP Private, SAP S/4HANA, ECC systems, acting as Tier 1. The objective is to manufacture products in accordance with country-specific standards.

In this setup, the subsidiary, operating on SAP Cloud ERP, sends assembly demands to the headquarter. The headquarter, functioning as a production and inspection unit, receives the demand, plans, produces, inspects, and delivers the requested products back to the subsidiary. In this process, the subsidiary acts as a customer, while the headquarter fulfils the role of the production and inspection entity.

This scenario allows subsidiaries to leverage the standard capabilities at headquarters to conduct quality inspections with multiple specifications based on the country-specific quality standards to ensure compliance with the customer requirement.

### Two-Tier ERP Solution

The Two-Tier Solution facilitates direct API-based integration between the SAP Cloud ERP system deployed at the subsidiary and the SAP Cloud ERP Private /SAP S/4HANA/SAP ECC system utilized at the Headquarters. This integration ensures that the manufacturing process meets the necessary standards required for specific countries, thereby enabling the production of products that comply with country-specific requirements.

## Business Process Details

The process flow for the Two-Tier scenario Integrated Multiple Specification Inspection in Two-Tier ERP is as below,

- The process starts with the creation of purchase order at Tier 2 system and the demand ie a Purchase order detail flows to Tier 1 system via API to trigger automatic creation of sales order at Tier 1 and sends back the purchase order confirmation to Tier 2 system. Also, the sales order number will be updated in the purchase order document at Tier 2.
- Once the sales order created in Tier 1, production planner perform the MRP run to generate the planned order against the customer sales requirement. Followed by that planned order will be converted to Production order to proceed with the production activities to manufacture batch managed product.
- In Tier 1, Quality Inspector completes the Multiple specification Inspection by recording results for each characteristic which updates the batch classification characteristics automatically. After the completion of usage decision, stock will be received into unrestricted use.
- Once the manufacturing and Multiple specification inspection completes, Shipping specialist at Tier 1, creates Outbound delivery and complete the Post Goods Issue (PGI) against the sales requirement. Upon saving the outbound delivery, Quality Certificate will be generated. Download the Quality Certificate and the PDF document of the certificate is shared from Tier 1 to Tier 2 via email.
- PGI at Tier 1 triggers the shipping notification and automatic creation of inbound delivery with supplier batch at Tier 2. Copy the supplier batch to material batch via BAdI “LE_SHP_SAVE_DOCUMENT_PREPARE (Modify Standard and Custom Fields for Delivery Header and Items)”.
- Receiving Specialist at Tier 2 completes Post Goods Receipt (PGR) against the Inbound delivery which generates the receiving inspection lot and certificate receipt document.
- Quality Inspector at Tier 2, attach the Quality Certificate document received from Tier 1 system (in step 4) and change the status of certificate receipt document to ‘Checked and Stored’ which confirm the certificate receipt in the receiving inspection lot by changing the status from CTCM to CORK.
- In Tier 2, Quality Inspector completes the result recording by referring the Quality Certificate received from Tier 1 and uploaded in Certificate receipt document of Tier 2. After the completion of usage decision in the receiving inspection lot, the batch classified product will be received into the unrestricted use.
- In Tier 1, Account Receivable Accountant generates the invoice and billing documents which in turn will be received into the Tier 2 system.
- Subsequently, in Tier 2, the product that meets the specific requirements of the country will be delivered to the external customer located in that respective country.

<!-- image omitted: unnamed -->

### Prerequisites

The following list of prerequisites are to be in place to realize the business process:

- Integration between Headquarter and Subsidiary system: With communications scenarios and API services enabled.
- Creating suitable authentication processes to ensure secure connections from SAP S/4HANA on premises/ SAP Cloud ERP Private to SAP Cloud ERP system and vice-versa.
- Publish custom logic in BADI “LE_SHP_SAVE_DOCUMENT_PREPARE (Modify Standard and Custom Fields for Delivery Header and Items)” to copy the supplier batch received from Tier 1 to material batch of inbound delivery created in Tier 2.

Published code to copy Supplier batch to Material batch is as below,

<!-- image omitted: unnamed -->

### Process Flow with Technical Details

Following flow chart provides details of the process with integration scenario and role of

On-Premises and Cloud system in execution of the steps involved,

<!-- image omitted: unnamed -->

## Technical Requirement

This section covers the process of setting up integration between the SAP Cloud ERP and SAP S/4 HANA system/ SAP Cloud ERP Private Edition covering the prerequisites such as Cloud connector, Communication arrangements and API’s (Application programming interface) required to enable the direct integration between the system.

### Communication arrangements

To allow direct data communication between SAP Cloud ERP and SAP S/4 HANA system/ SAP Cloud ERP Private, a communication arrangement is created. The communication arrangement defines which system (communication system) and which user can call which APIs (communication scenarios).

Sales with Buyers Integration (SAP_COM_0223):

Communication Scenario for Communication Arrangement: SAP_COM_0223

Inbound Services:

<!-- image omitted: unnamed -->

Outbound Services:

<!-- image omitted: unnamed -->

Sourcing and Procurement with Suppliers Integration (SAP_COM_024):

Inbound Services:

<!-- image omitted: unnamed -->

Outbound services:

<!-- image omitted: unnamed -->

### Integration Requirements by using API’s

The following diagram and table below show an example of how the API’s (Application programming Interfaces) can be called between the systems,

<!-- image omitted: unnamed -->

Following table explain integration design with API’s,

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Tier1** |  |  |  |  |  |
| Interaction | Direction in system | Authentication | Format | Business Object | Protocol |
| Trigger automatic creation of sales order | Inbound | User/Password or Certificate | SOAP | Sales Order | HTTPS |
| Send Purchase order confirmation | Outbound | User/Password or Certificate | SOAP | Purchase Order | HTTPS |
| Send Shipping Notification | Outbound | User/Password or Certificate | SOAP | Purchase Order | HTTPS |
| Send Customer Invoice | Outbound | User/Password or Certificate | SOAP | Billing Document | HTTPS |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Tier2** |  |  |  |  |  |
| Interaction | Direction in system | Authentication | Format | Business Object | Protocol |
| Send Purchase Order data | Outbound | User/Password or Certificate | SOAP | Purchase Order | HTTPS |
| Receive Purchase order confirmation | Inbound | User/Password or Certificate | SOAP | Purchase Order | HTTPS |
| Trigger automatic creation of Inbound Delivery with Supplier Batch | Inbound | User/Password or Certificate | SOAP | Inbound Delivery | HTTPS |
| Trigger creation of Supplier Invoice | Inbound | User/Password or Certificate | SOAP | Billing Document | HTTPS |

## Test Procedure

### Prerequisites

This section summarizes all prerequisites to conduct the test in terms of systems, users, master data, organizational data, and other test data and business conditions.

#### System Details

The test scenario can be built in the following Two-Tier system landscape:

| System | Details |
| --- | --- |
| SAP S/4HANA System/ SAP Cloud ERP Private - Headquarters | SAP S/4HANA System/ SAP Cloud ERP Private (Any Version) |
| SAP Cloud ERP - Subsidiary | SAP Cloud ERP (Any Version) |

#### Creation of custom development-based integration

- Since the data is available and can be accessed via API, the customers can develop their own reports and analytics using Business Application Studio.

### Overview Table

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Generate Quality Certificate for inspection with multiple specification in Tier1 | After completing multiple specification inspection, suitable country will be updated in Batch classification data. While saving Outbound delivery at Tier1, Quality Certificate will be generated. Download the quality certificate | Quality certificate for multiple specification inspection generated. |
| 2 | Generate Material Batch by Copying Supplier Batch | Upon completing PGI at Tier1, triggers Inbound delivery creation with supplier batch at Tier2. Copy supplier batch to material batch using BADI. Batch master record will be created while saving the Inbound delivery (IBD) | Material batch copied from supplier batch and Batch master record generated |
| 3 | Upload Quality Certificate | After completing IBD, inspection lot and Certificate Receipt document generated. Upload Quality certificate received from Tier1 and complete result recording by referring the uploaded certificate | Quality Certificate uploaded |
| 4 | Generate Quality Certificate for batch | Inspection lot Recorded values copied to the Batch classification. Configure Certificate profile and Assignments. Generate quality certificate for batches and send it along with the delivery of product to the customer. | Quality Certificate for Batch generated |

## Appendix

### Relevant Scope ID’s

The Cloud APIs are relevant for the following scope item IDs in Manufacturing.

[Master Data Integration (1RO)](https://rapid.sap.com/bp/#/scopeitems/1RO)

[Integration of Procurement with External Suppliers (2EJ)](https://rapid.sap.com/bp/#/browse/categories/sap_s%254hana/areas/cloud/packageversions/BP_CLD_ENTPR/S4CLD/2302/US/29/EN/scopeitems/2EJ)

[Integration of Sales with External Buyers (2EL)](https://rapid.sap.com/bp/#/browse/categories/sap_s%254hana/areas/cloud/packageversions/BP_CLD_ENTPR/S4CLD/2302/US/29/EN/scopeitems/2EL)

[Quality Management in Discrete Manufacturing (1E1)](https://rapid.sap.com/bp/#/browse/categories/sap_s%254hana/areas/cloud/packageversions/BP_CLD_ENTPR/S4CLD/2302/US/29/EN/scopeitems/1E1)

[Quality Management in Procurement (1FM)](https://rapid.sap.com/bp/#/browse/categories/sap_s%254hana/areas/cloud/packageversions/BP_CLD_ENTPR/S4CLD/2302/US/29/EN/scopeitems/1FM)

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Header says SAP Cloud ERP June 2026 but copyright and revision date are 2023; scope item links reference 2302 package

## Connections
- part-of :: [[_cluster]]
- see-also :: [[13-quality-ehs-and-compliance/stammdatenskript-qualitatsprufplan-anlegen-sds-bnq-652]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Manufacturing/S4CLD2608_2T_Int Multi_Spec Insp.docx` — full document · extracted with `mammoth` · 15,519 chars in the whole document
