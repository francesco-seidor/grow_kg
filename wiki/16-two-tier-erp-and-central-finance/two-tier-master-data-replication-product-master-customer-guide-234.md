---
id: 16-two-tier-erp-and-central-finance/two-tier-master-data-replication-product-master-customer-guide-234
title: "Two-Tier: Master Data Replication - Product Master (Customer Guide) (S4CLD2608_2T_Product Master)"
description: "Two-Tier ERP guide for replicating Product Master data from headquarter S/4HANA Cloud Private Edition to subsidiary SAP Cloud ERP via DRF, with test script (scope 1RO)."
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/product-and-bom-replication]
aliases: [S4CLD2608_2T_Product Master]
keywords: [Two-Tier Product Master and BOM Replication, product master replication, two-tier erp, data replication framework, test procedures, master data governance integration, idoc matmas, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Master data/S4CLD2608_2T_Product Master.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-234
topic: 16-two-tier-erp-and-central-finance/product-and-bom-replication
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Two-Tier: Master Data Replication - Product Master (Customer Guide) (S4CLD2608_2T_Product Master)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Master data/S4CLD2608_2T_Product Master.docx`, extracted with `mammoth`. Grouped under **Two-Tier Product Master and BOM Replication** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP Cloud ERP June 2026English |  |
|  | Two-Tier: Master Data Replication- Product Master |
|  | Customer Guide |

Copyright

© 2020 SAP SE or an SAP affiliate company. All rights reserved.

No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE. The information contained herein may be changed without prior notice.

Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors.

National product specifications may vary.

These materials are provided by SAP SE and its affiliated companies ("SAP Group") for informational purposes only, without representation or warranty of any kind, and SAP Group shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP Group products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty.

SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE in Germany and other countries. Please see http://www.sap.com/corporate-en/legal/copyright/index.epx#trademark for additional trademark information and notices.

| Revision | Change Date | Description |
| --- | --- | --- |
| 0 | 01.09.2017 | Initial version of document |
| 1 | 20.05.2020 | Reviewed |
| 2 | 31.03.2021 | Review of Document |

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

[1 Purpose 6](#_Toc40956844)

[2 Value Proposition 6](#_Toc40956845)

[2.1 Business Requirements 6](#_Toc40956846)

[2.2 Two-Tier Solution 6](#_Toc40956847)

[3 Business Process Details 6](#_Toc40956848)

[3.1 Prerequisites 6](#_Toc40956849)

[3.2 Process Flow with Technical Details 7](#_Toc40956853)

[4 Technical Requirement 7](#_Toc40956854)

[4.1 Integration Requirements by using API 7](#_Toc40956855)

[4.2 Integration Requirements by using EDI/IDOC 7](#_Toc40956856)

[4.3 Reporting Requirements by using Analytical CDS Views 7](#_Toc40956857)

[4.4 Reporting Requirements by using Analytical API 8](#_Toc40956858)

[5 Test Script 8](#_Toc40956859)

[5.1 Prerequisites 8](#_Toc40956860)

[5.1.1 System Access and Roles 8](#_Toc40956861)

[5.1.2 Master Data, Organizational Data, and Other Data 8](#_Toc40956862)

[5.2 Business Conditions 8](#_Toc40956863)

[5.3 Overview Table 9](#_Toc40956864)

[5.4 Test Procedures 9](#_Toc40956865)

[5.4.1 Create Product Master Data in Headquarter 9](#_Toc40956866)

[5.4.2 Check Product Master Replication in Subsidiary 10](#_Toc40956867)

[5.4.3 Change Product Master Replication in Headquarter 11](#_Toc40956868)

[5.4.4 Check Product Master change Replication in Subsidiary 11](#_Toc40956869)

[6 Appendix 12](#_Toc40956870)

[6.1 Relevant Scope ID’s 12](#_Toc40956871)

**Two-Tier-Master Data Replication: Product Master**

## Purpose

This document provides the detailed process for Product Master Data replication in a Two-Tier ERP setup with process flow, technical requirements and test procedure.

## Value Proposition

### Business Requirements

The Product Master Data created at the SAP Cloud ERP Private of the Headquarter needs to be replicated to the SAP Cloud ERP system at the Subsidiary.

### Two-Tier Solution

The Two-Tier Solution provides the integration between SAP Cloud ERP at the subsidiary and SAP S/4HANA Cloud Private Edition/SAP ERP at Headquarter using SAP Data Replication Framework (DRF).

## Business Process Details

This scenario describes all the activities for replication of Material Master Data from S/4HANA Cloud Private Edition to SAP Cloud ERP in real time. The business process encompasses the following scope:

- Create a new Product in SAP S/4HANA Cloud Private Edition
- Review the Product replicated as a Product master in SAP Cloud ERP
- Change a new Product in SAP S/4HANA Cloud Private Edition
- Review the changed Product replicated as a Product master in SAP Cloud ERP

### Prerequisites

The following list of prerequisites are to be in place to realize the business process

- Integration between Headquarter and Subsidiary system using SAP Data Replication Framework (DRF)
- Activate the Scope ID 1RO at the Subsidiary’s SAP Cloud ERP system

### Process Flow with Technical Details

<!-- image omitted: unnamed -->

## Technical Requirement

Refer the technical set-up guide for the SAP Best Practice Scope ID 1RO.

### Integration Requirements by using API

None.

### Integration Requirements by using EDI/IDOC

The required IDOC for Product Master Data replication is MATMAS.

### Reporting Requirements by using Analytical CDS Views

None.

### Reporting Requirements by using Analytical API

None.

## Test Script

### Prerequisites

This section summarizes all prerequisites to conduct the test in terms of systems, users, master data, organizational data, and other test data and business conditions.

#### System Access and Roles

The test is conducted in the following systems:

| System | Details |
| --- | --- |
| SAP Cloud ERP Private | S4HANA 1909 |
| SAP Cloud ERP system | Release 2005 |

Use the following standard test users or assign roles to testers, respectively:

| Business Role | Business Role Description | Business Role ID | Log On |
| --- | --- | --- | --- |
| Master Data Specialist If business role is the same for all process steps | In the SAP Cloud ERP Private create/edit Product Master data.Describe the responsibilities and key tasks of the role |  |  |
| Master Data Specialist | In the SAP S/4HANA Fiori Launchpad, the Master Data Specialist reviews the data replicated from Headquarter. | SAP_BR_BUPA_MASTER_SPECIALIST | Test user: BUPA_MASTER_SPECALISTPassword: <Welcome1> |

#### Master Data, Organizational Data, and Other Data

The master data to be used as per the standard of the Headquarter. The same has to be mapped with the SAP Cloud ERP system at the Subsidiary.

### Business Conditions

Optional – delete this section if not needed!

Describe the conditions as a state that has been met.

Before the testing of the scope-item, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 1RO - Integration of SAP Cloud ERP to SAP Master Data Governance | Please refer to the Set-Up Instructions for 1RO.Please make sure the Pre-configuration in this Set-Up Instructions is completed before data replication |

We need to schedule a job for automatic replication of master data from S/4HANA Cloud Private Edition to SAP Cloud ERP.

### Overview Table

| Process Step | Business Role | UI Type | Expected Results |
| --- | --- | --- | --- |
| Create Product Master Data | Master Data Specialist | S/4HANA Cloud Private Edition | Product Master Data is created |
| Review Product Master Data | Master Data Specialist (SAP Cloud ERP) | SAP Cloud ERP UI | Review the newly created Product Master Data replicated in SAP Cloud ERP |
| Edit Product Master Data | Master Data Specialist | S/4HANA Cloud Private Edition | Product Master Data is edited |
| Review Product Master Data | Master Data Specialist (SAP Cloud ERP) | SAP Cloud ERP UI | Review the edited Product Master Data replicated in SAP Cloud ERP |

### Test Procedures

This section describes the test procedures for each process step that belongs to this scope item.

#### Create Product Master Data in Headquarter

Test Administration

Customer project: Fill in the project-specific parts (highlighted).

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Click here to enter a date. |
| Business Role(s) | Master Data Specialist (in S/4HANA Cloud Private Edition) |  |  |  |  |
| Responsibility | <Creator of Product master data> | Duration | 10 Minutes |  |  |

Purpose

In this activity, you create a Product master in the S/4HANA Cloud Private Edition.

Procedure

Create a Product in the S/4HANA Cloud Private Edition. It is automatically replicated to the SAP Cloud ERP.

#### Check Product Master Replication in Subsidiary

Test Administration

Customer project: Fill in the project-specific parts (highlighted).

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Click here to enter a date. |
| Business Role(s) | Master Data Specialist (in SAP Cloud ERP) |  |  |  |  |
| Responsibility | <Review Product Master Data> | Duration | 5 Minutes |  |  |

Purpose

In this activity, you review the Product master created in SAP Cloud ERP Private.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch Home Page | Access the SAP Cloud ERP system using URL and log on with the appropriate user and password.For example,User: PRODMASTER_SPECIALISTPassword: Welcome1 | Successful login. |  |
| 2 | **Access Product master** | Open Product Master tile under Product Master section | Product Master search screen opens. |  |
| 3 | **Review the replicated Product from S/4HANA Cloud Private Edition** | Enter the Material Number created in Step 5.4.1 and press Search. | The Product Master data is displayed. The replicated data is displayed. |  |
| 4 | **Review the Data for the Product** | Navigate to the respective tabs for reviewing the replicated data.Verify that Data for example old product data is replicated successfully | Data is replicated successfully |  |

.

#### Change Product Master Replication in Headquarter

Test Administration

Customer project: Fill in the project-specific parts (highlighted).

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Click here to enter a date. |
| Business Role(s) | Master Data Specialist (in SAP Cloud ERP) |  |  |  |  |
| Responsibility | <Review Product Master Data> | Duration | 5 Minutes |  |  |

Purpose

In this activity, you change the Product master created in SAP Cloud ERP Private.

Procedure

Change a Product in the S/4HANA Cloud Private Edition. It is automatically replicated to the SAP Cloud ERP.

#### Check Product Master change Replication in Subsidiary

Test Administration

Customer project: Fill in the project-specific parts (highlighted).

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Click here to enter a date. |
| Business Role(s) | Master Data Specialist (in SAP Cloud ERP) |  |  |  |  |
| Responsibility | <Review Product Master Data> | Duration | 5 Minutes |  |  |

Purpose

In this activity, you review the Product master created in SAP Cloud ERP Private.

.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch Home Page | Access the SAP Cloud ERP system using URL and log on with the appropriate user and password.For example,User: PRODMASTER_SPECIALISTPassword: Welcome1 | Successful login. |  |
| 2 | **Access Product master** | Open Manage Product Master tile under Product Master section | Product Master search screen opens. |  |
| 3 | **Review the replicated Product from S/4HANA Cloud Private Edition** | Enter the Material Number created in Step 4.1 and press Search. | The Product Master data is displayed. The replicated data is displayed. |  |
| 4 | **Review the Data for the Product** | Navigate to the respective tabs for reviewing the changed data that has been replicated. | Changed Data is replicated successfully |  |

## Appendix

### Relevant Scope ID’s

1RO- Integration of SAP Cloud ERP to SAP Master Data Governance

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Test systems listed (S4HANA 1909, release 2005) and 2017-2021 revision history look outdated versus the 2608/June 2026 library release

> [!warning] Conflict
> Flagged while digesting this document, not verified: Test step 3 refers to material number 'created in Step 5.4.1' while the change check refers to 'Step 4.1' - internal reference inconsistency

## Connections
- part-of :: [[_cluster]]
- related-to :: [[16-two-tier-erp-and-central-finance/two-tier-erp-bill-of-material-integration-using-cloud-integration-236]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Master data/S4CLD2608_2T_Product Master.docx` — full document · extracted with `mammoth` · 13,148 chars in the whole document
