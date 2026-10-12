---
id: 16-two-tier-erp-and-central-finance/two-tier-erp-pricing-master-integration-using-cloud-integration-237
title: Two Tier ERP – Pricing Master Integration using Cloud Integration (S4CLD2608_2T_Pricing Master_Userguide)
description: "Customer guide for replicating SD pricing condition records (IDoc COND_A04) from HQ SAP Cloud ERP Private/SAP ERP to a subsidiary SAP Cloud ERP via Cloud Integration, with test script."
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/pricing-replication-and-harmonization]
aliases: [S4CLD2608_2T_Pricing Master_Userguide]
keywords: [Two-Tier Pricing Replication and Harmonization, centralized pricing, two-tier erp, pricing condition integration, idoc mapping, communication arrangement, error monitoring, integration test script]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Master data/Centralized Pricing/S4CLD2608_2T_Pricing Master_Userguide.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-237
topic: 16-two-tier-erp-and-central-finance/pricing-replication-and-harmonization
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Two Tier ERP – Pricing Master Integration using Cloud Integration (S4CLD2608_2T_Pricing Master_Userguide)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Master data/Centralized Pricing/S4CLD2608_2T_Pricing Master_Userguide.docx`, extracted with `mammoth`. Grouped under **Two-Tier Pricing Replication and Harmonization** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP Cloud ERP June 2026English |  |
|  | Two Tier ERP – Pricing Master Integration using Cloud Integration |
| SAP SE Dietmar-Hopp-Allee 16 69190 Walldorf Germany | Customer Guide |

Copyright

© 2017 SAP SE or an SAP affiliate company. All rights reserved.

No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE. The information contained herein may be changed without prior notice.

Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors.

National product specifications may vary.

These materials are provided by SAP SE and its affiliated companies ("SAP Group") for informational purposes only, without representation or warranty of any kind, and SAP Group shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP Group products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty.

SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE in Germany and other countries. Please see http://www.sap.com/corporate-en/legal/copyright/index.epx#trademark for additional trademark information and notices.

| Revision | Change Date | Description |
| --- | --- | --- |
| 0 | 15.04.2020 | Initial version of document |
| 1 | 31.03.2021 | Review of Document |

Only add a revision when corrections are made to a published document. Do not change the original published date. Set back to revision 0 after a full upgrade of the Customer Guide.

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

[1 Purpose 6](#_Toc523736066)

[2 Business Requirements 6](#_Toc523736067)

[3 Technical Details 6](#_Toc523736068)

[3.1 Prerequisites 6](#_Toc523736069)

[3.2 Mapping Prerequisites 7](#_Toc523736070)

[3.3 Error Handling & Monitoring 9](#_Toc523736071)

[4 Test Script 10](#_Toc523736072)

[4.1 Purpose 10](#_Toc523736073)

[4.2 Prerequisites 10](#_Toc523736074)

[4.2.1 System Access 11](#_Toc523736075)

[4.2.2 Roles 11](#_Toc523736076)

[4.2.3 Master Data, Organizational Data and Other Data 11](#_Toc523736077)

[4.3 Overview Table 11](#_Toc523736078)

[4.4 Test Procedure 12](#_Toc523736079)

## Purpose

This document will provide the steps for Pricing Master integration in a 2-Tier scenario. The condition Pricing for Sales created at the HQ (SAP Cloud ERP Private or SAP ERP) will be replicated to the subsidiary (SAP Cloud ERP).

Centralized Pricing required for companies who would like to have faster decision-making, have strict policy and compliance requirements in managing their prices centrally at their Headquarters for all their subsidiaries. This accelerator helps organization in reducing their implementation timeline.

This Interface development we would only carry out for SD pricing Condition

## Business Requirements

In a two-tier model, SAP Cloud ERP and Private Edition systems can support the organization and subsidiaries to run in an independent yet integrated fashion. The Pricing master is created in SAP Cloud ERP Private (headquarters) and sent to S4HANA Cloud Public Edition

Technical Details

Important: Rename the file -“OP2S4HC_PricingMaster.dat” as “OP2S4HC_PricingMaster.zip”

The main steps in the scenario:

1. Pricing Condition IDoc COND_A04 is created in SAP Cloud ERP Private or SAP ERP.

2. The IDOCs are sent from SAP Cloud ERP Private or SAP ERP system to SAP Cloud Integration and mapped to OData API (SALES_PRICING_CONDITION_RECORD).

3. The Pricing Condition Master is created by BTP Integration using OData API in SAP Cloud ERP System.

### Prerequisites

The following list of prerequisite configurations are to be in place to realize the integration process.

***Configuration in SAP Cloud ERP:***

1. Create a Communication User in SAP Cloud ERP system. This user credential will be used in OData adapter in SAP Cloud Integration tenant.
2. Maintain a Communication System to specify the host details.
3. Maintain a Communication Arrangement to facilitate the usage of API. The Communication Scenario used is SAP_COM_0294 for Pricing Data Integration.

***Configuration in SAP Cloud ERP Private or SAP ERP*:**

The outgoing IDOC (COND_A04) needs to be processed and sent to Cloud integration. We need to maintain the following configurations.

1. Maintain the RFC Connection in SM59 to target URL to BTP Integration.
2. Create Port & Partner Profile in WE21 & WE20.
3. Generate model view in BD64.

**Creation of SAP Cloud Integration iFlow:**

<!-- image omitted: unnamed -->

Figure 1.0

### Mapping Prerequisites

The Customer specific field mappings are suggested below for the target structure. However, the fields might not be limited to the ones given and the Customer needs to take care of the same during implementation. Some constant or logic has to be set against these fields.

The business data of condition records for pricing that are used in Sales. The following table lists the node's fields and subnodes.

To View SalesPricingConditionRecord: Fields and Subnodes

[https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/df8dc95360267214e10000000a174cb4.html?locale=en-US&version=2022.000](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/df8dc95360267214e10000000a174cb4.html?locale=en-US&version=2022.000" \t "_blank" \o "https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/df8dc95360267214e10000000a174cb4.html?locale=en-US&version=2022.000)

IDOC Message Type to be used : COND_A / Basic type : COND_A04

Segment Wise Field Mapping to be considered as per attached Excel Sheet

<!-- image omitted: unnamed -->

### Error Handling & Monitoring

Message Monitoring in SAP Cloud Integration can be used for Error Handling & Monitoring Error/ Success Messages.

”Monitor Message Processing / Message Processing Details“ Provides the Log, Payload & S4Response Messages as below.

## Test Script

### Purpose

This section provides a detailed procedure for testing the scope item after solution deployment. Each process step is covered in its own section, providing the system interactions in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly.

### Prerequisites

This section summarizes all prerequisites needed to conduct the test in terms of system, users, master data, organizational data, and other test data and business conditions.

**Note:**

The process to be tested in this test script is for Subsidiary side regarding a two-tier scenario. Hence integration between Subsidiary system (SAP Cloud ERP) and Headquarter system (SAP Cloud ERP Private or SAP ERP) shall be set up in advance. You will be able to process the test steps only after the corresponding ERP system has sent the required messages.

#### System Access

The test is conducted in the following systems:

| System | Details |
| --- | --- |
| System | Access using the SAP Fiori® Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

#### Roles

Assign the following business roles to your individual test users.

Note The following roles are provided as example roles from SAP. You can use these as templates for your own roles.

| Business Role | Business Role ID as Delivered by SAP | Log On |
| --- | --- | --- |
|  |  |  |

#### Master Data, Organizational Data and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data to go through the test procedure.

Make sure that the proper mappings are maintained between the process objects in SAP Cloud ERP and Sales Order in SAP Cloud ERP Private or SAP ERP.

### Overview Table

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |

### Test Procedure

This section describes test procedures for each process step that belongs to this scope item.

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on to SAP Cloud ERP Private or SAP ERP | Create Pricing Condition | IDoc Triggered in SAP Cloud ERP Private or SAP ERP |
| 2 | Log on to SAP Cloud ERP. | Check Pricing Condition created using “Manage Prices” app. | . |

<!-- image omitted: unnamed -->

## Connections
- part-of :: [[_cluster]]
- related-to :: [[16-two-tier-erp-and-central-finance/two-tier-erp-product-centric-pricing-harmonization-customer-guide-238]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Master data/Centralized Pricing/S4CLD2608_2T_Pricing Master_Userguide.docx` — full document · extracted with `mammoth` · 10,228 chars in the whole document
