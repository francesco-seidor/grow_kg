---
id: 16-two-tier-erp-and-central-finance/two-tier-erp-product-centric-pricing-harmonization-customer-guide-238
title: Two Tier ERP – Product-Centric Pricing Harmonization (Customer Guide) (S4CLD2608_2T_Product_Pricing Harmonization)
description: Customer guide and test script for replicating HQ sales pricing conditions to subsidiary purchasing info records in a Two-Tier ERP via Event Mesh and a custom iFlow.
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/pricing-replication-and-harmonization]
aliases: [S4CLD2608_2T_Product_Pricing Harmonization]
keywords: [Two-Tier Pricing Replication and Harmonization, pricing harmonization, two-tier erp, pricing condition replication, purchasing info records, communication arrangements, event mesh integration, error monitoring, test script, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Master data/Centralized Pricing/S4CLD2608_2T_Product_Pricing Harmonization.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-238
topic: 16-two-tier-erp-and-central-finance/pricing-replication-and-harmonization
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Two Tier ERP – Product-Centric Pricing Harmonization (Customer Guide) (S4CLD2608_2T_Product_Pricing Harmonization)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Master data/Centralized Pricing/S4CLD2608_2T_Product_Pricing Harmonization.docx`, extracted with `mammoth`. Grouped under **Two-Tier Pricing Replication and Harmonization** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP Cloud ERP June 2026English |  |
|  | Two Tier ERP – Product-Centric Pricing Harmonization |
|  | Customer Guide |

Copyright

© 2017 SAP SE or an SAP affiliate company. All rights reserved.

No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE. The information contained herein may be changed without prior notice.

Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors.

National product specifications may vary.

These materials are provided by SAP SE and its affiliated companies ("SAP Group") for informational purposes only, without representation or warranty of any kind, and SAP Group shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP Group products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty.

SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE in Germany and other countries. Please see http://www.sap.com/corporate-en/legal/copyright/index.epx#trademark for additional trademark information and notices.

| Revision | Change Date | Description |
| --- | --- | --- |
| 0 | 06.01.2025 | Initial version of document |

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

[1 Purpose 6](#_Toc187077254)

[2 Business Requirements 6](#_Toc187077255)

[2.1 Prerequisites 7](#_Toc187077256)

[2.2 Technical Set up 8](#_Toc187077257)

[2.3 Error Handling & Monitoring 8](#_Toc187077258)

[3 Test Script 9](#_Toc187077259)

[3.1 Purpose 9](#_Toc187077260)

[3.2 Prerequisites 9](#_Toc187077261)

[3.2.1 System Access 9](#_Toc187077262)

[3.2.2 Roles 9](#_Toc187077263)

[3.2.3 Master Data, Organizational Data and Other Data 9](#_Toc187077264)

[3.3 Overview Table 10](#_Toc187077265)

[3.4 Test Procedure 10](#_Toc187077266)

## Purpose

This document will provide the steps for Pricing Master integration in a Two-Tier scenario. The condition Pricing/Discounts condition for Sales created at the HQ (SAP Cloud ERP Private or SAP ERP) will be replicated to the subsidiary (SAP Cloud ERP) as Purchasing Info records/Discounts conditions.

## Business Requirements

Headquarter, the tier-1 establishes the pricing structure and discount terms for their products, ensuring uniformity across all the distribution organizations. These prices and discount structure are then required to be communicated automatically and applied as purchase pricing at the subsidiary, i.e. tier-2 system, to eliminate need for subsequent manual corrective reconciliation or adjustments.

This solution has a better fitment for the scenario for Sales office as a subsidiary and for the Distribution ecosystem scenario wherein prices, discounts are managed by the headquarter and are followed by the subsidiary and distributors who place orders with the headquarter.

**Capabilities**

Purchase Order (PO) at Subsidiary

At the tier-2 system sales office or a distributor creates a Purchase Order (PO) on the tier-1 system essentially for documenting the intent to buy goods from the headquarter at the agreed-upon terms (including pricing, quantity, delivery schedules, etc.). In this scenario, the PO would reflect the net price/discounts after applying the price and discount managed by the headquarter.

Sales Order (SO) at Headquarter

The tier-1 system sets the price and offers a sales discount, seasonal discounts to the sales office or distributors at the tier-2 system. This price schema would be reflected in the Sales order created against the PO at the tier-1 system.

<!-- image omitted: A diagram of a diagram of a cloud service

Description automatically generated with medium confidence -->

### Prerequisites

The following list of prerequisite configurations are to be in place to realize the integration process. The current set up is to replicate sales pricing condition to purchase info records.

Similarly for sales discounts/condition to pricing conditions we can use API Condition Record for Pricing in Purchasing.

***Configuration in SAP Cloud ERP Private:***

1. Sales Pricing Condition Record Events

[https://api.sap.com/event/OP_SALESPRICINGCONDITIONRECORDEVENTS/overview](https://api.sap.com/event/OP_SALESPRICINGCONDITIONRECORDEVENTS/overview)

[https://api.sap.com/api/OP_API_SLSPRCGCONDITIONRECORD_SRV_0001/overview](https://api.sap.com/api/OP_API_SLSPRCGCONDITIONRECORD_SRV_0001/overview)

1. Set up Communication Arrangement **SAP_COM_0294**
2. Maintain Event Channel Binding to the Events for Sales Pricing Condition records

***Configuration in SAP Cloud ERP*:**

1. Enable Communication arrangement SAP_COM_0145

Purchasing Info record: [https://api.sap.com/api/API_INFORECORD_PROCESS_SRV/overview](https://api.sap.com/api/API_INFORECORD_PROCESS_SRV/overview)

Condition Record for Pricing in Purchasing: SAP_COM_0294

[https://api.sap.com/api/API_PURGPRCGCONDITIONRECORD_SRV/overview](https://api.sap.com/api/API_PURGPRCGCONDITIONRECORD_SRV/overview)

***BTP set up***

1. Subscribe and Set up to Event Mesh in BTP
2. Create Queue for Events in Event Mesh
3. Set up Custom iFlow to replicate Pricing conditions

### Technical Set up

Technical Details

-
    1. Subscribe and Set up Event Mesh and create Queue in Event mesh

[https://help.sap.com/docs/subscription-billing/btp-configuration/set-up-sap-event-mesh?version=2024-12-16](https://help.sap.com/docs/subscription-billing/btp-configuration/set-up-sap-event-mesh?version=2024-12-16)

1. Queue should be subscribed to Sales Pricing Condition Record Events

[https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/19d48293097f4a2589433856b034dfa5/71703bca89464fa0a164163979327bf4.html?version=2023.002](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/19d48293097f4a2589433856b034dfa5/71703bca89464fa0a164163979327bf4.html?version=2023.002)

[https://api.sap.com/event/OP_SALESPRICINGCONDITIONRECORDEVENTS/overview](https://api.sap.com/event/OP_SALESPRICINGCONDITIONRECORDEVENTS/overview)

1. In SAP Cloud ERP Private subscribe to Maintain Event Channel Binding to the Events for Sales Pricing Condition records.
2. In SAP S/4HANA Private Cloud Edition maintain Set up Communication Arrangement **SAP_COM_0294**
3. Create an iFlow with AMQP Adaptor that gets triggered when message is received in Queue
4. The iFlow is custom and customer/partner can design the iFlow on the need. In this case to describe an event for create is triggered when sales pricing condition record is created in SAP S/4HANA Private cloud edition. Using this event the condition record is captured as part of event; we use this to do an API call in SAP S/4HANA Private cloud Edition to get all the pricing details. Then map this pricing details to make a post API call to SAP Cloud ERP for creating Purchasing info record. Then we use the Purchase Info record number to make another API post call to create Purchasing Info Record Purch. Org. Data with pricing details.
5. Before Making Post call to SAP Cloud ERP make sure communication arrangements SAP_COM_0145 are active.

### Error Handling & Monitoring

- Message Monitoring in SAP Cloud Integration can be used for Error Handling & Monitoring Error/ Success Messages.
- Fiori apps Message Monitoring and Enterprise Event Enablement - Event Monitor
- Transaction code /IWFND/ERROR_LOG or SRT_UTIL

## Test Script

### Purpose

This section provides a detailed procedure for testing the scope item after solution deployment. Each process step is covered in its own section, providing the system interactions in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly.

### Prerequisites

This section summarizes all prerequisites needed to conduct the test in terms of system, users, master data, organizational data, and other test data and business conditions.

**Note:**

The process to be tested in this test script is for the for-Pricing Master integration in a Two-Tier scenario. The condition Pricing/Discounts condition for Sales created at the HQ (SAP Cloud ERP Private or SAP ERP) will be replicated to the subsidiary (SAP Cloud ERP) as Purchasing Info records/Discounts conditions.

#### System Access

The test is conducted in the following systems:

| System | Details |
| --- | --- |
| System | Access using the SAP Fiori® Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

#### Roles

Assign the following business roles to your individual test users.

Note The following roles are provided as example roles from SAP. You can use these as templates for your own roles.

| Business Role ID as Delivered by SAP | Log On |
| --- | --- |
| SAP_BR_PRICING_SPECIALIST | SAP Cloud ERP Private |
| SAP_BR_PURCHASER | SAP Cloud ERP |

#### Master Data, Organizational Data and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data to go through the test procedure.

Make sure that the proper mappings are maintained between the process objects in SAP Cloud ERP and in SAP Cloud ERP Private or SAP ERP.

### Overview Table

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Create Pricing Condition | SAP_BR_PRICING_SPECIALIST | Set Material Price- Sales | Pricing Condition Created |
| Display Purchasing Info Record | SAP_BR_PURCHASER | Display Purchasing Info Record | Purchase Info record created |

### Test Procedure

This section describes test procedures for each process step that belongs to this scope item.

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on to SAP Cloud ERP Private | Create Pricing Condition via Set Material Price- Sales | Event Triggered |
| 2 | Log on to SAP Cloud ERP | Check Purchase Info record has been created with plant org data and price | . Purchase Info record created |
| 3 | Log on to SAP Cloud ERP Private | Change Pricing Condition via Set Material Price- Sales | Event Triggered |
| 4 | Log on to SAP Cloud ERP | Check Purchase Info record has been changed | . Purchase Info record changed |
| 5 | Log on to SAP Cloud ERP Private | Change Pricing Condition Validity, via Set Material Price- Sales | Event Triggered |
| 6 | Log on to SAP Cloud ERP | Check Purchase Info record has been changed | . Purchase Info record validity changed |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[16-two-tier-erp-and-central-finance/two-tier-erp-pricing-master-integration-using-cloud-integration-237]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Master data/Centralized Pricing/S4CLD2608_2T_Product_Pricing Harmonization.docx` — full document · extracted with `mammoth` · 12,285 chars in the whole document
