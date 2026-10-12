---
id: 16-two-tier-erp-and-central-finance/two-tier-multi-level-project-scenario-eppm-customer-guide-243
title: "Two-Tier: Multi-Level Project Scenario - EPPM (Customer Guide) (S4CLD2608_2T__Multilevel_Project)"
description: Conceptual customer guide on integrating headquarters (S/4HANA On-Premise) and subsidiary SAP Cloud ERP via APIs for multi-level portfolio and enterprise project management; no out-of-box…
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/project-based-eto-and-eppm]
aliases: [S4CLD2608_2T__Multilevel_Project]
keywords: [Two-Tier Engineer-to-Order and Multi-Level Projects, two-tier erp, enterprise project management, multi-level projects, api integration, portfolio management, enterprise project service, badi and bapi, integration test procedure, project scope items]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/PLM_EPPM/S4CLD2608_2T__Multilevel_Project.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-243
topic: 16-two-tier-erp-and-central-finance/project-based-eto-and-eppm
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Two-Tier: Multi-Level Project Scenario - EPPM (Customer Guide) (S4CLD2608_2T__Multilevel_Project)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/PLM_EPPM/S4CLD2608_2T__Multilevel_Project.docx`, extracted with `mammoth`. Grouped under **Two-Tier Engineer-to-Order and Multi-Level Projects** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP Cloud ERP June 2026English |  |
|  | Two-Tier: Multi-Level Project Scenario - EPPM |
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
| 0 | 01.09.2020 | Initial version of document |
| 1 | 20.10.2020 | Reviewed |

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

[1 Purpose 6](#_Toc52964883)

[2 Value Proposition 6](#_Toc52964884)

[2.1 Business Requirements 6](#_Toc52964885)

[2.2 Two-Tier Solution 6](#_Toc52964886)

[3 Business Process Details 6](#_Toc52964887)

[3.1 Prerequisites 7](#_Toc52964888)

[3.2 Process Flow with Technical Details 8](#_Toc52964892)

[4 Technical Requirement 8](#_Toc52964893)

[4.1 Integration Requirements by using API 8](#_Toc52964894)

[5 Test Procedure 9](#_Toc52964895)

[5.1 Prerequisites 9](#_Toc52964896)

[5.1.1 System Details 9](#_Toc52964897)

[5.1.2 Creation of custom development based 9](#_Toc52964898)

[5.2 Overview Table 9](#_Toc52964899)

[6 Appendix 10](#_Toc52964900)

[6.1 Relevant Scope ID’s 10](#_Toc52964901)

**Two-Tier: Multi-Level Project Scenario**

## Purpose

This document provides a conceptual overview of utilizing EPPM in a Two-Tier deployment for SAP Cloud ERP. This document explains how a multi-level project scenario can work in a Two-Tier setup between SAP S/4HANA On Premise and SAP Cloud ERP. The API’s referred to in this document are available for consumption from api.sap.com and will have to be adopted to suit customer business processes.

This document does not provide any out of the box functionality but only guidance on how the existing API’s can be leveraged to fulfil such a scenario in the Two-Tier context.

## Value Proposition

### Business Requirements

The need to have an integrated end-to-end business process setup for project, starting from ideation to project closure.

With the introduction of Project based read and write APIs, integration capabilities can now be built between SAP S/4HANA On-Premise / SAP Cloud ERP (Private) Edition and SAP Cloud ERP, resulting in information flow from the master project down to the sub-project(s) and information roll-up from the sub-project(s) back up into the master projects becoming a possibility.

### Two-Tier Solution

The Two-Tier Solution provides the API based integration between SAP Cloud ERP system at the subsidiary and SAP S/4HANA On-Premise / SAP Cloud ERP (Private) system at Headquarter

## Business Process Details

A simple Multi-level project requires the following key capabilities:

- Portfolio Management
- Scoring Models and What-if scenario Analysis
- Proposal Management
- Project Structuring and Scheduling
- Progress Tracking
- Time Entry
- Billing and Invoicing
- Project Based Procurement
- Actual Cost Reporting

The following sketch visualizes a Process flow for Two-Tier Multi-level Portfolio and Project Management. The functionalities for both Tier 1 (Headquarters) and Tier 2 (Affiliate or Subsidiary) are highlighted as well:

<!-- image omitted: unnamed -->

**Tier1**

- Portfolio Manager prepares portfolio forecast and allocates budget per bucket
- Program manager and steering committee members evaluate and finalize potential projects
- Project manager prepares project plan and identifies subsidiary projects
- Periodically, project progress can be pulled from the subsidiary project via the [Read API](https://api.sap.com/api/API_ENTERPRISE_PROJECT_SRV/resource) and rolled back up into the master project.

**Tier2**

- Subsidiary project managers prepare detailed project plan for their specific subsidiary project

Project managers allocate budget to lower level work packages / WBS elements

### Prerequisites

The following list of prerequisites are to be in place to realize the business process

- Integration between Headquarter and Subsidiary system
- Creation of suitable development to call the SAP Cloud ERP API for creating and reading project information
- Creating of suitable authentication processes to ensure secure connections from SAP S/4HANA On-Premise to SAP Cloud ERP

### Process Flow with Technical Details

<!-- image omitted: unnamed -->

## Technical Requirement

### Integration Requirements by using API

The following diagram shows an example of how these API’s can be called from SAP S/4HANA On-Premise.

<!-- image omitted: unnamed -->

The following BADI’s and API’s can be used to build this solution:

**On-Premise:**Handle Headquarters Project Data

BADI:

- /RPM/OBJECT_SERVICES (Portfolio Item save) – Portfolio Item Data
- DPR_ATTRIBUTES – cProjects Data

BAPI:

- BAPI_PROJECTDEF_GETDETAIL – Project Systems Project Data

**Cloud:**Handle Subsidiary Project Data

- [Enterprise Project Service](https://api.sap.com/api/API_ENTERPRISE_PROJECT_SRV_0002/overview)
- [Read Project API](https://api.sap.com/api/API_ENTERPRISE_PROJECT_SRV_0002/overview)
- [Create, Update and Read operations](https://help.sap.com/docs/SAP_S4HANA_CLOUD/988903b47d7040f6ac4ec02e44bb58e4/35f5f46c6bb14edead3851c8ecfde7a0.html) for enterprise projects

## Test Procedure

### Prerequisites

This section summarizes all prerequisites to conduct the test in terms of systems, users, master data, organizational data, and other test data and business conditions.

#### System Details

The test is conducted in the following systems:

| System | Details |
| --- | --- |
| On-Premise System - Headquarters | SAP S/4HANA 1709 or Higher |
| SAP Cloud ERP System - Subsidiary | Release 2005 or Higher |

#### Creation of custom development based

Based on the design explained in this document, the custom development has been created to ensure the following:

- Integration between Headquarter and Subsidiary system
- Creation of suitable development to call the SAP Cloud ERP API for creating and reading project information
- Creating of suitable authentication processes to ensure secure connections from SAP S/4HANA On-Premise to SAP Cloud ERP

### Overview Table

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Create Headquarters Project | On the Headquarters system, create a portfolio item and maintain the required information and save. | Portfolio item is saved. |
| 2 | Trigger creation of Subsidiary Project on save of headquarters project | On save of portfolio item, the create API is triggered to create a subsidiary project is created on SAP Cloud ERP EPPM system. | The subsidiary project is successfully created on the SAP Cloud ERP EPPM system. |
| 3 | Edit and change details in subsidiary project | On the SAP Cloud ERP EPPM UI, open the newly created subsidiary project and change the dates and status. And Save. | The new changes are saved. |
| 4 | Check changes are visible on headquarters project screen | On the headquarters portfolio item, navigate to the appropriate screen to see that the project dates and status are reflecting the changes. | The new changes are visible on the headquarters side. |

## Appendix

### Relevant Scope ID’s

The Cloud API’s are relevant for the following scope item ID’s in EPPM.

[Project Financial Control (1NT)](https://rapid.sap.com/bp/#/scopeitems/1NT)

[Project Review (1YF)](https://rapid.sap.com/bp/#/scopeitems/1YF)

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Title page says SAP Cloud ERP June 2026 but revision history ends 2020 and copyright reads 2025

## Connections
- part-of :: [[_cluster]]
- related-to :: [[16-two-tier-erp-and-central-finance/two-tier-scenario-project-based-engineer-to-order-customer-guide-241]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/PLM_EPPM/S4CLD2608_2T__Multilevel_Project.docx` — full document · extracted with `mammoth` · 9,854 chars in the whole document
