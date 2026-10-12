---
id: 16-two-tier-erp-and-central-finance/two-tier-master-data-replication-supplier-master-235
title: "Two-Tier: Master Data Replication - Supplier Master (S4CLD2608_2T_Supplier Master)"
description: "Customer guide for replicating supplier master data from headquarter S/4HANA Cloud Private Edition to a subsidiary's Public Edition via DRF, with test script."
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/business-partner-replication]
aliases: [S4CLD2608_2T_Supplier Master]
keywords: [Two-Tier Customer and Supplier Replication, two-tier erp, master data replication, supplier master, data replication framework, scope item 1ro, idoc integration, replication test procedures, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Master data/S4CLD2608_2T_Supplier Master.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-235
topic: 16-two-tier-erp-and-central-finance/business-partner-replication
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Two-Tier: Master Data Replication - Supplier Master (S4CLD2608_2T_Supplier Master)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Master data/S4CLD2608_2T_Supplier Master.docx`, extracted with `mammoth`. Grouped under **Two-Tier Customer and Supplier Replication** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP S/4HANA CloudPublic Edition June 2026English |  |
|  | Two-Tier: Master Data Replication- Supplier Master |
| SAP SE Dietmar-Hopp-Allee 16 69190 Walldorf Germany | Customer Guide |

Copyright

© 2020 SAP SE or an SAP affiliate company. All rights reserved.

No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE. The information contained herein may be changed without prior notice.

Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors.

National product specifications may vary.

These materials are provided by SAP SE and its affiliated companies ("SAP Group") for informational purposes only, without representation or warranty of any kind, and SAP Group shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP Group products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty.

SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE in Germany and other countries. Please see http://www.sap.com/corporate-en/legal/copyright/index.epx#trademark for additional trademark information and notices.

| Revision | Change Date | Description |
| --- | --- | --- |
| 1 | 31/03/2021 | Final Version |
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

[1 Purpose 6](#_Toc493065091)

[2 Value Proposition 6](#_Toc493065092)

[2.1 Business Requirements 6](#_Toc493065093)

[2.2 Two-Tier Solution 6](#_Toc493065094)

[3 Business Process Details 6](#_Toc493065095)

[3.1 Prerequisites 6](#_Toc493065096)

[3.2 Process Flow with Technical Details 7](#_Toc493065100)

[4 Technical Requirement 7](#_Toc493065101)

[4.1 Integration Requirements by using API 7](#_Toc493065102)

[4.2 Integration Requirements by using EDI/IDOC 7](#_Toc493065103)

[4.3 Reporting Requirements by using Analytical CDS Views 7](#_Toc493065104)

[4.4 Reporting Requirements by using Analytical API 8](#_Toc493065105)

[5 Test Script 8](#_Toc493065106)

[5.1 Prerequisites 8](#_Toc493065107)

[5.1.1 System Access and Roles 8](#_Toc493065108)

[5.1.2 Master Data, Organizational Data, and Other Data 8](#_Toc493065109)

[5.2 Business Conditions 8](#_Toc493065110)

[5.3 Overview Table 9](#_Toc493065111)

[5.4 Test Procedures 9](#_Toc493065112)

[5.4.1 Create Supplier Master Data in Headquarter 9](#_Toc493065113)

[5.4.2 Check Business Partner Replication in Subsidiary 10](#_Toc493065114)

[5.4.3 Change Supplier Master Data in Headquarter 11](#_Toc493065115)

[3.1 Check Business Partner Replication in Subsidiary 11](#_Toc493065116)

[6 Appendix 12](#_Toc493065117)

[6.1 Relevant Scope ID’s 12](#_Toc493065118)

**Two-Tier-Master Data Replication: Supplier Master**

## Purpose

This document provides the detailed process for Supplier Master Data replication in a Two-Tier ERP setup with process flow, technical requirements and test procedure.

## Value Proposition

### Business Requirements

The Supplier Master Data created at the S/4HANA Cloud Private Edition system of the Headquarter needs to be replicated to the SAP S/4HANA Cloud Public Edition system at the Subsidiary.

### Two-Tier Solution

The Two-Tier Solution provides the integration between SAP S/4HANA Cloud Public Edition at the subsidiary and SAP S/4HANA Cloud Private Edition/SAP ERP at Headquarter using SAP Data Replication Framework (DRF).

## Business Process Details

This scenario describes all the activities for replication of Supplier Master Data from S/4HANA Cloud Private Edition ERP at Headquarter to SAP S/4HANA Cloud Public Edition in real time. The business process encompasses the following scope:

- Create a new Supplier in the S/4HANA Cloud Private Edition System at Headquarter
- Review the Supplier replicated as a Business Partner in SAP S/4HANA Cloud Public Edition
- Change an existing Supplier in S/4HANA Cloud Private Edition System at Headquarter
- Review the changed Supplier Master Data in SAP S/4HANA Cloud Public Edition

### Prerequisites

The following list of prerequisites are to be in place to realize the business process

- Integration between Headquarter and Subsidiary system using SAP Data Replication Framework (DRF)
- Activate the Scope ID 1RO at the Subsidiary’s SAP S/4HANA Cloud Public Edition system

### Process Flow with Technical Details

<!-- image omitted: unnamed -->

## Technical Requirement

Refer the technical set-up guide for the SAP Best Practice Scope ID 1RO.

### Integration Requirements by using API

None.

### Integration Requirements by using EDI/IDOC

The required IDOC for Supplier Master Data replication is CREMAS.

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
| S/4HANA Cloud Private Edition System | SAP S/4HANA 2021 |
| SAP S/4HANA Cloud Public Edition system | Release 2102 |

Use the following standard test users or assign roles to testers, respectively:

| Business Role | Business Role Description | Business Role ID | Log On |
| --- | --- | --- | --- |
| Master Data Specialist If business role is the same for all process steps | In the S/4HANA Cloud Private Edition system create/edit Supplier Master data.Describe the responsibilities and key tasks of the role |  |  |
| Master Data Specialist | In the SAP S/4HANA Fiori Launchpad, the Master Data Specialist reviews the data replicated from Headquarter. | SAP_BR_BUPA_MASTER_SPECIALIST |  |

#### Master Data, Organizational Data, and Other Data

The master data to be used as per the standard of the Headquarter. The same has to be mapped with the SAP S/4HANA Cloud Public Edition system at the Subsidiary.

### Business Conditions

Optional – delete this section if not needed!

Describe the conditions as a state that has been met.

Before the testing of the scope-item, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 1RO - Integration of SAP S/4HANA Cloud Public Edition to SAP Master Data Governance | Please refer to the Set-Up Instructions for 1RO.Please make sure the Pre-configuration in this Set-Up Instructions is completed before data replication |

We need to schedule a job for automatic replication of master data from S/4HANA Cloud Private Edition to SAP S/4HANA Cloud Public Edition.

### Overview Table

| Process Step | Business Role | UI Type | Expected Results |
| --- | --- | --- | --- |
| Create Supplier Master Data | Master Data Specialist | S/4HANA Cloud Private Edition | Supplier Master Data is created |
| Review Supplier Master Data | Master Data Specialist (SAP S/4HANA Cloud Public Edition) | SAP S/4HANA Cloud Public Edition UI | Review the newly created Supplier Master Data replicated in SAP S/4HANA Cloud Public Edition |
| Edit Supplier Master Data | Master Data Specialist | S/4HANA Cloud Private Edition | Supplier Master Data is edited |
| Review Supplier Master Data | Master Data Specialist (SAP S/4HANA Cloud Public Edition) | SAP S/4HANA Cloud Public Edition UI | Review the edited Supplier Master Data replicated in SAP S/4HANA Cloud Public Edition |

### Test Procedures

This section describes the test procedures for each process step that belongs to this scope item.

#### Create Supplier Master Data in Headquarter

Test Administration

Customer project: Fill in the project-specific parts (highlighted).

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Click here to enter a date. |
| Business Role(s) | Master Data Specialist (in S/4HANA Cloud Private Edition) |  |  |  |  |
| Responsibility | <Creator of Supplier master data> | Duration |  |  |  |

Purpose

In this activity, you create a Supplier in the S/4HANA Cloud Private Edition System at the Headquarter.

Procedure

Create Supplier Master data in the S/4HANA Cloud Private Edition system at the Headquarter and send the same to the SAP S/4HANA Cloud Public Edition at the subsidiary for replication. Master Data script ID “BNE“ – Create Supplier Master“ can be referred for Supplier Master Data creation steps

#### Check Business Partner Replication in Subsidiary

Test Administration

Customer project: Fill in the project-specific parts (highlighted).

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Click here to enter a date. |
| Business Role(s) | Master Data Specialist (in SAP S/4HANA Cloud Public Edition) |  |  |  |  |
| Responsibility | <Review Business Partner Master Data> | Duration |  |  |  |

Purpose

In this activity, you review the Supplier replicated from the S/4HANA Cloud Private Edition System at the Headquarter.

.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch Home Page | Access the SAP S/4HANA Cloud Public Edition system using URL and log on with the appropriate user and password.For example,User: BUPA_MASTER_SPECIALISTPassword: <…> | Successful login. |  |
| 2 | **Access Business Partner** | Open Maintain Business Partner. | Business Partner maintenance screen opens. |  |
| 3 | **Review the replicated Supplier from Headquarter** | Enter the Supplier Number created in STEP 4.1 in the Business Partner field and choose Next. | The Business Partner data is displayed. The replicated data is displayed. |  |
| 4 | **Review the Accounting Info for the Supplier** | Select the Display in BP Role field as Supplier. Then choose Accounting tab from the top. Navigate to the respective tabs for reviewing the replicated data. | The Reconciliation Account data is replicated/converted. |  |

Note

As per the business requirement, supplier master can be enriched in S/4HANA Cloud system to be able to run end to end process.

.

#### Change Supplier Master Data in Headquarter

Test Administration

Customer project: Fill in the project-specific parts (highlighted).

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Click here to enter a date. |
| Business Role(s) | Master Data Specialist (in S/4HANA Cloud Private Edition) |  |  |  |  |
| Responsibility | <Creator of Supplier master data> | Duration |  |  |  |

Purpose

In this activity, you edit a Supplier in the S/4HANA Cloud Private Edition System at the Headquarter.

Procedure

Edit the Supplier Master data created in STEP 4.1 in the S/4HANA Cloud Private Edition system at the Headquarter and send the same to the SAP S/4HANA Cloud Public Edition at the subsidiary for replication.

### Check Business Partner Replication in Subsidiary

Test Administration

Customer project: Fill in the project-specific parts (highlighted).

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Click here to enter a date. |
| Business Role(s) | Master Data Specialist (in SAP S/4HANA Cloud Public Edition) |  |  |  |  |
| Responsibility | <Review Business Partner Master Data> | Duration | 5 Minutes |  |  |

Purpose

In this activity, you review the Supplier created in Headquarter.

.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Launch Home Page | Access the SAP S/4HANA Cloud Public Edition system using URL and log on with the appropriate user and password.For example,User: BUPA_MASTER_SPECIALISTPassword: Welcome1 | Successful login. |  |
| 2 | **Access Business Partner** | Open Maintain Business Partner. | Business Partner maintenance screen opens. |  |
| 3 | **Review the replicated Supplier from Headquarter** | Enter the Supplier Number created in STEP 4.1 in the Business Partner field and choose Next. | The Business Partner data is displayed. The changed data has been replicated. |  |

## Appendix

### Relevant Scope ID’s

1RO- Integration of SAP S/4HANA Cloud Public Edition to SAP Master Data Governance

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Cover says June 2026 / 2608 but test systems listed are S/4HANA 2021 and Public Edition release 2102 with revision dated 2021; possibly stale content

> [!warning] Conflict
> Flagged while digesting this document, not verified: Contains a test user with a hard-coded example password

## Connections
- part-of :: [[_cluster]]
- related-to :: [[16-two-tier-erp-and-central-finance/contentmetadata-240]]
- related-to :: [[16-two-tier-erp-and-central-finance/two-tier-master-data-replication-business-partner-master-customer-233]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Master data/S4CLD2608_2T_Supplier Master.docx` — full document · extracted with `mammoth` · 13,976 chars in the whole document
