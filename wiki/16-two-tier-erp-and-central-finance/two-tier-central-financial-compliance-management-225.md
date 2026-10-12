---
id: 16-two-tier-erp-and-central-finance/two-tier-central-financial-compliance-management-225
title: "Two-Tier: Central Financial Compliance Management (S4CLD2608_2T_Central Financial Compliance Management)"
description: "Customer guide for connecting SAP Cloud ERP and on-premise/private S/4HANA systems to SAP Financial Compliance Management in a Two-Tier setup, with test steps and use cases."
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/central-financial-compliance-management]
aliases: [S4CLD2608_2T_Central Financial Compliance Management]
keywords: [Central Financial Compliance Management, financial compliance management, two-tier erp, automated procedures, compliance use cases, sap business technology platform, connectivity setup, additional software and services, controls and work packages]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Finance/S4CLD2608_2T_Central Financial Compliance Management.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-225
topic: 16-two-tier-erp-and-central-finance/central-financial-compliance-management
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Two-Tier: Central Financial Compliance Management (S4CLD2608_2T_Central Financial Compliance Management)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Finance/S4CLD2608_2T_Central Financial Compliance Management.docx`, extracted with `mammoth`. Grouped under **Central Financial Compliance Management** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP Cloud ERP June 2026English |  |
|  | Two-Tier: Central Financial Compliance Management |
|  | Customer Guide |

Copyright

© 2024 SAP SE or an SAP affiliate company. All rights reserved.

No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE. The information contained herein may be changed without prior notice.

Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors.

National product specifications may vary.

These materials are provided by SAP SE and its affiliated companies ("SAP Group") for informational purposes only, without representation or warranty of any kind, and SAP Group shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP Group products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty.

SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE in Germany and other countries. Please see http://www.sap.com/corporate-en/legal/copyright/index.epx#trademark for additional trademark information and notices.

| Revision | Change Date | Description |
| --- | --- | --- |
| 0 | 05.04.2021 | Initial version of document |

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

[1 Purpose 6](#_Toc123734674)

[2 Value Proposition 6](#_Toc123734675)

[2.1 Business Requirements 6](#_Toc123734676)

[2.2 Two-Tier Solution 6](#_Toc123734677)

[3 Business Process Details 6](#_Toc123734678)

[3.1 Prerequisites 7](#_Toc123734679)

[The following list of prerequisites are to be in place to realize the business process 7](#_Toc123734680)

[3.2 Process Flow with Technical Details 7](#_Toc123734681)

[4 Technical Requirements 7](#_Toc123734682)

[1 Prerequisites 7](#_Toc123734683)

[4.1 Subscribe to *SAP Financial Compliance Management* 7](#_Toc123734684)

[4.2 Additional Software and Services 8](#_Toc123734685)

[4.3 Connectivity 8](#_Toc123734686)

[Set Up Connections 8](#_Toc123734687)

[5 Test Procedure 8](#_Toc123734688)

[5.1 Prerequisites 9](#_Toc123734689)

[5.1.1 System Details 9](#_Toc123734690)

[5.2 Overview Table 9](#_Toc123734691)

[6 Appendix 10](#_Toc123734692)

[6.1 Relevant Scope ID’s 10](#_Toc123734693)

**Two-Tier-Master Data Replication: Product Master**

## Purpose

This document provides a conceptual overview of Central Financial Compliance Management in a Two-Tier deployment for SAP Cloud ERP. This document explains how a Financial Compliance Management can be centralized in a Two-Tier setup between SAP S/4HANA On Premise or SAP Cloud ERP Private and SAP Cloud ERP.

## Value Proposition

### Business Requirements

The need to have a Central Financial Compliance management system for end to end financial compliance. The need to have a Central system for continuous monitoring & detection of anomalies causing financial losses for multiple connected SAP S/4HANA systems.

### Two-Tier Solution

The Two-Tier Solution provides set-up instructions to connect SAP Cloud ERP & On Premise or SAP Cloud ERP Private with SAP Financial Compliance Management which is built on SAP Business Technology Platform (formerly known as SAP Cloud Platform) and provides end-to-end financial compliance.

## Business Process Details

SAP Cloud ERP & On Premise solution can connect to SAP Financial Compliance Management which is built on SAP Business Technology Platform and thus leverage one platform for many use cases across the enterprise.

<!-- image omitted: unnamed -->

SAP Financial Compliance Management provides a common platform for detection of anomalies, investigation, remediation, and reporting.

### Prerequisites

The following list of prerequisites are to be in place to realize the business process

1. Additional manual configurations as detailed in Technical requirements
2. Set-Up Instructions, system access, roles as detailed in scope item 3KY.

### Process Flow with Technical Details

<!-- image omitted: unnamed -->

<!-- image omitted: unnamed -->

## Technical Requirements

### 1 Prerequisites

-
    - You have set up your global account and subaccount. For more information, see [Managing Global Accounts Using the Cockpit](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/667f34ba9222450491c2b848cd17e189.html) and [Managing Subaccounts Using the Cockpit](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/55d0b6d8b96846b8ae93b85194df0944.html).
    - You are assigned the **Administrator** role for the global account.

### Subscribe to *SAP Financial Compliance Management*

-
    - To use SAP Financial Compliance Management, you need to subscribe to the application in your subaccount.
    - Follow the guide [Subscribe to Multitenant Business Applications in the Cloud Foundry Environment Using the Cockpit](https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/7a3e39622be14413b2a4df7c02ca1170.html)

### Additional Software and Services

-
    - The following software and services need to be enabled for SAP Financial Compliance Management to run.

| **Software/Service** | **Purpose** | **Required/Optional** | **Use** |
| --- | --- | --- | --- |
| SAP Identity Authentication Service | Provision business user data for the microservice **Manage Controls**. | Required | [See the IAS help documentation](https://help.sap.com/viewer/product/IDENTITY_AUTHENTICATION/Cloud/en-US) |
| SAP Cloud Connector | Connect SAP Financial Compliance Management to on-premise systems, such as S/4 HANA. | Required only when you need to connect to on-premise systems | [See Connectivity for more information.](https://help.sap.com/viewer/dc9590073546445684529f40040a2f2b/1.0/en-US/03506f9a82584a0bbbf0e057e5c7a93a.html) |
| Data Retention Manager | Manage the protection and privacy of the personal data processed by the microservices **Manual Procedures** and **Automated Procedures**. | Required | Subscribe to it in your subaccount. |
| Personal Data Manager | Show the personal data processed by the microservices **Manual Procedures** and **Automated Procedures** per data subject. | Required | Subscribe to it in your subaccount. |

### Connectivity

-
    - You can connect SAP Financial Compliance Management to remote services that run on the SAP Cloud ERP or on-premise.

### Set Up Connections

-
    - In your subaccount, choose **Connectivity** in the navigation pane and configure the destinations that refer to the on-premise or cloud systems you want to connect. For detailed instructions, see [Managing Destinations](https://help.sap.com/viewer/cca91383641e40ffbe03bdc78f00f681/Cloud/en-US/84e45e071c7646c88027fffc6a7bb787.html).

For setting up the connection to your SAP Cloud ERP system, please follow the document [Setting Up Financial Operation Monitoring with SAP Financial Compliance (3KY)](https://support.sap.com/content/dam/SAAP/Sol_Pack/Library/Setup/3KY_Set-Up_EN_XX.pdf)

To connect on-premise systems, you need to install and configure the [Cloud Connector](https://help.sap.com/viewer/cca91383641e40ffbe03bdc78f00f681/Cloud/en-US/e6c7616abb5710148cfcf3e75d96d596.html).

For the specific requirements in configuring destinations for automated procedures, see [Connectivity for Automated Procedures](https://help.sap.com/viewer/dc9590073546445684529f40040a2f2b/1.0/en-US/390f81c90bf0495db537ad7297ecc842.html).

## Test Procedure

### Prerequisites

This section summarizes all prerequisites to conduct the test in terms of systems, users, master data, organizational data, and other test data and business conditions.

#### System Details

The test is conducted in the following systems:

| System |
| --- |
| SAP S/4HANA On-Premise System |
| SAP Cloud ERP |
| SAP Financial Compliance Management |

### Overview Table

| Process Step | Business Role | System | App/Transaction | Expected Results |
| --- | --- | --- | --- | --- |
| Option One: Create Standard Automated Procedure | Compliance Specialist | SAP Financial Compliance | Manage Automated Procedures | Automated Procedure for is created. |
| Option Two: Create Your Own Automated Procedure | Compliance Specialist | SAP Financial Compliance | Manage Automated Procedures | Automated Procedure for is created. |
| Create Control and Assign Automated Procedure | Compliance Manager | SAP Financial Compliance | Manage Controls | Controls with Automated Procedures assigned is created. |
| Create Work Package and Assign Control | Compliance Manager | SAP Financial Compliance | Manage Work Packages | Work Package with Controls/ Automated Procedures is created. |
| Display Procedure Run Results | Compliance Manager | SAP Financial Compliance | Display Automated Procedure Runs | Procedure Run results shows correctly. |

**Use Cases**

Below use cases are pre-delivered together with the SAP Financial Compliance Management solution. You can refer the Set-up Instruction in the Technical Requirement (section 4) for how to set it up. They are used as a quick start of your business.

| No. | Use Case | Automated Procedure Name | OData Service Name | Entity Set |
| --- | --- | --- | --- | --- |
| 1 | To detect list of suspicious GL entries which entered on weekends | Journal Entry over the weekend | /sap/opu/odata/sap/C_JRNLENTRITMWEEKENDPOSTG_CDS | C_JrnlEntrItmWeekendPostgSet |
| 2 | To detect list of GL accounts created in the selected period | GL Accounts Created in the Selected Period | /sap/opu/odata/sap/C_GENERALLEDGERACCOUNT_CDS | C_GeneralLedgerAccount |
| 3 | To detect list of general journals posted to the prior fiscal period | General Journals Posted to the Prior Fiscal Period | /sap/opu/odata/sap/C_JRNLENTRITMPRIORFSCLPERD_CDS | C_JrnlEntrItmPriorFsclPerd |
| 4 | To detect list of duplicate Invoices in the selected period | Duplicate Invoices in the Selected Period | /sap/opu/odata/sap/UI_DUPLICATESUPPLIERINV | DuplicateSupplierInvoiceSet |
| 5 | To detect list of blocked sales documents which released manually | Release Blocked Sales Documents Manually | /sap/opu/odata/sap/C_GRC_RELDCRDTDCSNDOCUMENT_CDS | C_GRC_ReldCrdtDcsnDocumentSet |

## Appendix

### Relevant Scope ID’s

[Financial Operation Monitoring with SAP Financial Compliance (‏3KY‏)](https://rapid.sap.com/bp/#/browse/categories/sap_s%254hana/areas/cloud/packageversions/BP_CLD_ENTPR/S4CLD/2102/GB/23/EN/scopeitems/3KY)

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Cover says SAP Cloud ERP June 2026 but revision history shows only 05.04.2021 initial version and copyright 2024; currency unclear

## Connections
- part-of :: [[_cluster]]
- related-to :: [[01-solution-foundation-and-platform/test-script-continuous-control-monitoring-with-sap-process-control-2oh]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Finance/S4CLD2608_2T_Central Financial Compliance Management.docx` — full document · extracted with `mammoth` · 12,010 chars in the whole document
