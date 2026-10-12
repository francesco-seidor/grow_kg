---
id: 16-two-tier-erp-and-central-finance/two-tier-scenario-managing-intercompany-professional-services-projects
title: "Two-Tier scenario: Managing Intercompany Professional Services Projects (S4CLD2608_2T_Managing PFS Projects)"
description: "Customer guide for the two-tier headquarters/subsidiary scenario for intercompany professional services projects: process flows, communication arrangements, prerequisites, scope items."
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/two-tier-professional-services-projects]
aliases: [S4CLD2608_2T_Managing PFS Projects]
keywords: [Two-Tier Professional Services Projects, two-tier erp, intercompany projects, professional services projects, communication arrangements, assembly processing, sap cloud integration, scope items, system landscape, intercompany billing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/PLM_EPPM/S4CLD2608_2T_Managing PFS Projects.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-242
topic: 16-two-tier-erp-and-central-finance/two-tier-professional-services-projects
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Two-Tier scenario: Managing Intercompany Professional Services Projects (S4CLD2608_2T_Managing PFS Projects)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/PLM_EPPM/S4CLD2608_2T_Managing PFS Projects.docx`, extracted with `mammoth`. Grouped under **Two-Tier Professional Services Projects** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP S/4HANA CloudPublic Edition June 2026English |  |
|  | Two -Tier scenario: Managing Intercompany Professional Services Projects |
|  | Customer Guide |

Copyright

© 2025 SAP SE or an SAP affiliate company. All rights reserved.

No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE. The information contained herein may be changed without prior notice.

Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors.

National product specifications may vary.

These materials are provided by SAP SE and its affiliated companies ("SAP Group") for informational purposes only, without representation or warranty of any kind, and SAP Group shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP Group products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty.

SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE in Germany and other countries. Please see http://www.sap.com/corporate-en/legal/copyright/index.epx#trademark for additional trademark information and notices.

| Revision | Change Date | Description |
| --- | --- | --- |
| 0 | 26-05-2026 | Initial version of document |
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

[1 Purpose 6](#_Toc291629414)

[2 Value Proposition 6](#_Toc492119162)

[2.1 Business Requirements 6](#_Toc1636320779)

[2.2 Two-Tier Solution 6](#_Toc1030449371)

[3 Business Process Details 6](#_Toc1287441995)

[3.1 Prerequisites 7](#_Toc236512094)

[3.2 Process Flow with Technical Details 7](#_Toc1217688350)

[4 Technical Requirement 9](#_Toc881853751)

[5 Test Procedure 9](#_Toc1346401973)

[5.1 Prerequisites 10](#_Toc144872431)

[5.1.1 System Details 10](#_Toc2120832255)

[5.1.2 Creation of custom development-based integration 10](#_Toc2064356439)

[6 Appendix 10](#_Toc500091755)

[6.1 Relevant Scope ID’s 10](#_Toc363119893)

**Two-Tier-Transportation planning of external requirements**

## Purpose

This accelerator document covers the two-tier headquarters and subsidiary scenario Managing Intercompany Professional Services Projects with headquarters and subsidiary between SAP Cloud ERP and SAP Cloud ERP (Private). The APIs referred in this document are available for consumption from api.sap.com.

## Value Proposition

### Business Requirements

The need to have an integrated end-to-end business process set up for Intercompany Professional Services Projects.

With project and sales order based read and write APIs, helps the required Project, Workpackage, Role, Customer Invoice and the sales order information flow from headquarters to subsidiary and the confirmation back from subsidiary to headquarters.

### Two-Tier Solution

The Two -Tier Solution provides the API based direct integration between SAP Cloud ERP system at the subsidiary and SAP Cloud ERP (Private) system at headquarters or vice-versa.

## Business Process Details

The purchase order creation in tier 1 (headquarters) initiates the process of creating Customer project and Work package in tier 2 (subsidiary).

<!-- image omitted: unnamed -->

***Process flow case 1*:**

The Integration can be setup with SAP Cloud Integration for data services and best practice explorer Scope Item 2EL. The following steps elaborate end-to-end flow when headquarters is on SAP Cloud ERP (Private) / S/4HANA On premise and subsidiary is on SAP Cloud ERP system:

1. The headquarters creates a purchase order in SAP S/4HANA On Premise / SAP Cloud ERP (Private) system.
2. The purchase order in the headquarters SAP S/4HANA On Premise system creates an IDOC which triggers API in subsidiary running on SAP Cloud ERP system.
3. The API Commercial Project - Create, Update is triggered in batch requests to create Customer Project, WorkPackage and the Role’s required to execute the project in subsidiary SAP Cloud ERP system.
4. Upon successful execution of the project create API, cloud integration triggers the creation of the sales order using API “Commercial Project - Create, Update”.
5. The fields required for creation of Customer Project, Workpackage, Role’s and sales order can be derived by maintaining mapping in SAP cloud integration, the mapping will be maintained between the headquarter purchase order fields and the subsidiary Project, Workpackage and Sales order fields.
6. The flow of customer invoice raised in subsidiary will be interfaced to headquarters via SAP cloud integration.

<!-- image omitted: unnamed -->

***Process flow case 2*:**

The Integration utilizes the best practice explorer Scope Item 2EL. This Intergration focusses on Standardized projects executed in headquarters. Assembly processing is leveraged to automatically create projects and WBS elements out of the box similar to ETO process. For assembly processing, Material master needs to be replicated between headquarters and subsidiary. The following steps elaborate end-to-end flow when headquarters is on SAP Cloud ERP and subsidiary is on SAP S/4HANA On-Premise system:

1. The headquarters creates a purchase order in the SAP Cloud ERP system.
2. The purchase order in the headquarters SAP Cloud ERP system automatically creates a sales order in the subsidiary SAP S/4HANA On-Premise system.
3. In subsidiary SAP S/4HANA On-Premise system, the material has be linked to a standard network and standard Work breakdown structure in CN09 to follow the [Assembly processing](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/feded183701e4ba0b42bc4fc31ad7a12/bc31bf53d25ab64ce10000000a174cb4.html).
4. The sales order will trigger creation of an operational network and operational project in subsidiary SAP S/4HANA On-Premise system.
5. Project manager can be assigned to the project in subsidiary who can go ahead and create a detailed project plan and assign the resources working in the Project.
6. 6. The services can be delivered from the subsidiary SAP S/4HANA on premise system to the customer(headquarters) and the same can be recorded in project as timesheets
7. Based on the type of invoicing, subsidiary can proceed with the resource related billing for time and material project execution between headquarters and subsidiary. Fixed price billing can be also processed appropriately.
8. The billing and invoicing can be proceeded in the approach as per 2EL.

<!-- image omitted: unnamed -->

The Project execution between headquarters and subsidiary can be integrated as per the process flow mentioned above,

### Prerequisites

The following list of prerequisites are to be in place to realize the business process,

- Integration setup between headquarter and subsidiary with SAP Cloud Integration.
- Replicate the material master data between headquarters and subsidiary.
- If subsidiaries are on SAP Cloud ERP, set up [2EL](https://rapid.sap.com/bp/#/browse/categories/sap_s%254hana/areas/cloud/packageversions/BP_CLD_ENTPR/S4CLD/2208/US/28/EN/scopeitems/2EL) scope to automate exchange of sales documents and the follow-on messages.
- If headquarters are on SAP Cloud ERP, set up [2EJ](https://rapid.sap.com/bp/#/browse/categories/sap_s%254hana/areas/cloud/packageversions/BP_CLD_ENTPR/S4CLD/2208/US/28/EN/scopeitems/2EJ) scope to automate exchange of procurement documents and the follow-on messages.

### Process Flow with Technical Details

***Process flow case 1*:**When headquarters is on SAP Cloud ERP (Private) and subsidiary is on SAP Cloud ERP system:

<!-- image omitted: unnamed -->

***Process flow case 2*:**When headquarters is on SAP Cloud ERP and subsidiary is on SAP Cloud ERP (Private) system:

<!-- image omitted: unnamed -->

## Technical Requirement

Communication scenarios are set up using communication arrangements tool for respective data as follows:

| Communication arrangement ID | Name |
| --- | --- |
| SAP_COM_0054 | Commercial Project Integration |
| SAP_COM_0A11 | Resource Management in SAP Project and Resource Management - API Integration |
| SAP_COM_0109 | Sales Order Integration |

Help documentation reference Commercial Project - Create, Update API: [https://api.sap.com/api/_CPD_SC_PROJ_ENGMT_CREATE_UPD_SRV/overview](https://api.sap.com/api/_CPD_SC_PROJ_ENGMT_CREATE_UPD_SRV/overview)

## Test Procedure

### Prerequisites

This section summarizes all prerequisites to conduct the test in terms of systems, users, master data, organizational data, and other test data and business conditions.

#### System Details

The test scenario can be built in the following two-tier system landscape:

| System | Details |
| --- | --- |
| SAP Cloud ERP (Private) | SAP Cloud ERP (Private) version 1909 or higher |
| SAP Cloud ERP | SAP Cloud ERP, 2208 release or higher |

#### Creation of custom development-based integration

- There is no custom development needed to be implemented to realize this integration.

## Appendix

### Relevant Scope ID’s

The Cloud APIs are relevant for the following scope item IDs in PFS (Professional Services) and Two-Tier.

[Internal Project Management – Project-Based Services (1A8)](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2602/SolP/1A8?region=DE)

[Customer Project Management – Project-Based Services (J11)](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2602/SolP/J11?region=DE)

[Resource Management for Projects (6JO)](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2602/SolP/6JO?region=DE)

[Integration of Sales with External Buyers (2EL)](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2602/SolP/2EL?region=DE)

[Integration of Procurement with External Suppliers (2EJ)](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/2602/SolP/2EJ?region=DE)

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Process flow case labelling in the Technical Details section (case 1 HQ Private / subsidiary Cloud) differs from case 2 description in text where subsidiary is described as S/4HANA On-Premise versus SAP Cloud ERP (Private).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[16-two-tier-erp-and-central-finance/two-tier-project-based-services-procurement-between-headquarter-and-su]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/PLM_EPPM/S4CLD2608_2T_Managing PFS Projects.docx` — full document · extracted with `mammoth` · 11,380 chars in the whole document
