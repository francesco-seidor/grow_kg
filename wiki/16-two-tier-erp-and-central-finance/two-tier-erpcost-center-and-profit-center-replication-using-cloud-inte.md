---
id: 16-two-tier-erp-and-central-finance/two-tier-erpcost-center-and-profit-center-replication-using-cloud-inte
title: Two Tier ERP–Cost center and Profit center replication using Cloud Integration (S4CLD2608_2T_CC_PC_Replication_Guide)
description: "Customer guide for replicating cost center and profit center master data from HQ (ECC/Private) to S/4HANA Cloud public edition via Cloud Integration iFlows, with mapping and test script."
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/cost-and-profit-center-replication]
aliases: [S4CLD2608_2T_CC_PC_Replication_Guide]
keywords: [Two-Tier Cost Center and Profit Center Replication, cost center replication, profit center replication, two-tier erp, financial master data, cloud integration iflow, idoc configuration, field mapping, error monitoring, test procedure]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Master data/Fin Master Data Sync/S4CLD2608_2T_CC_PC_Replication_Guide.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-239
topic: 16-two-tier-erp-and-central-finance/cost-and-profit-center-replication
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Two Tier ERP–Cost center and Profit center replication using Cloud Integration (S4CLD2608_2T_CC_PC_Replication_Guide)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Master data/Fin Master Data Sync/S4CLD2608_2T_CC_PC_Replication_Guide.docx`, extracted with `mammoth`. Grouped under **Two-Tier Cost Center and Profit Center Replication** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP Cloud ERP June 2026English |  |
|  | Two Tier ERP–Cost center and Profit center replication using Cloud Integration |
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
| 0 | 12.09.2018 | Initial version of document |
|  | 02.06.2026 | Updated |

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

[1 Purpose 6](#_Toc524526974)

[2 Business Requirements 6](#_Toc524526975)

[3 Technical Details 6](#_Toc524526976)

[3.1 Prerequisites 6](#_Toc524526977)

[3.2 Mapping Prerequisites 9](#_Toc524526978)

[3.3 Error Handling & Monitoring 10](#_Toc524526979)

[4 Test Script 12](#_Toc524526980)

[4.1 Purpose 12](#_Toc524526981)

[4.2 Prerequisites 12](#_Toc524526982)

[4.2.1 System Access 12](#_Toc524526983)

[4.2.2 Roles 13](#_Toc524526984)

[4.2.3 Master Data, Organizational Data and Other Data 13](#_Toc524526985)

[4.3 Overview Table 13](#_Toc524526986)

[4.4 Test Procedure 13](#_Toc524526987)

## Purpose

This document will provide the sample integration content required to replicate cost center and profit center mater data from HQ running SAP ECC or SAP Cloud ERP Private to S/4HANA Cloud, public edition in a two-tier scenario.

In a similar way, cost center hierarchy and profit center hierarchies can also be handled.

## Business Requirements

In a Two-Tier ERP model, SAP Cloud ERP and SAP S/4HANA Cloud -Private Edition systems can support the organization and subsidiaries to run in an independent yet integrated fashion.

In such landscape the requirement is to have a central master data at HQ, wherein the master data for the entire enterprise is created at HQ and shared with relevant subsidiaries to optimize the data consistency between headquarters and subsidiaries.

## Technical Details

The main steps in the scenario:

1. Creation of master data from SAP ECC or SAP S/4HANA Cloud -Private Edition to S/4HANA Cloud, Public Edition.
2. Update the master data fields from SAP ECC or SAP Cloud ERP Private, SAP Cloud ERP -private edition to S/4HANA Cloud public edition.

Note:

Master data here is cost center and profit center.

Important: Rename “2Tier_FIN_Master_Data_Integration.dat” as “2Tier_FIN_Master_Data_Integration.zip” and import

### Prerequisites

The following list of prerequisite configurations are to be in place to realize the integration process.

***Configuration in SAP Cloud ERP:***

1. Create a Communication User in SAP Cloud ERP system. This user credential will be used in calling the API for data replication in SAP Cloud ERP.
2. Maintain a Communication System to specify the host details.
3. Maintain a Communication Arrangement to facilitate the usage of API. The Communication Scenario used for replication is SAP_COM_0179.

<!-- image omitted: cid:image004.png@01D44A8D.4F048F10 -->

<!-- image omitted: cid:image005.png@01D44A8D.4F048F10 -->

Figure 1 – Communication Arrangement

***Note –****The outbound services for profit center or cost center confirmation has to be activated for this to work.*

***Configuration in SAP SAP Cloud ERP Private/ SAP Cloud ERP -private edition or SAP ERP*:**

The outgoing IDOC (COSMAS01 and PRCMAS02) needs to be processed and converted to a cost center/profit center master data. We need to maintain the following configurations.

1. Maintain the RFC Connection in SM59 to target URL to Cloud Integration.
2. Create Port & Partner Profile in WE21 & WE20. Add the message id for COSMAS/PRCMAS in outbound message types.
3. Generate model view in BD64.

***Creation of SAP Cloud Integration iFlow:***

Cost center

<!-- image omitted: cid:image001.png@01D4179C.218442C0 -->

Profit center

<!-- image omitted: cid:image003.png@01D4179C.382A72B0 -->

Figure 2.0

This sample iFlow implementation is a part of the accelerator.

### Mapping Prerequisites

The Customer specific field mappings are suggested below for the target structure. However, the fields might not be limited to the ones given and the Customer needs to take care of the same during implementation. Some constant or logic must be set against these fields.

Cost center

| **Target structure field name** | **Description** | **Mapping Logic/ Constant** |
| --- | --- | --- |
| /ns2:CostCentreReplicationBulkRequest/CostCentreReplicationRequestMessage/CostCentre/ID | CONTROLLING AREA + COST CENTER | Use value mapping table “FI_CONTROLLINGAREA_VALUEMAP” to update CONTROLLING AREA |
| /ns2:CostCentreReplicationBulkRequest/CostCentreReplicationRequestMessage/CostCentre/Attributes/CompanyFinancialAccountingEntityID | Company Code | Use value mapping table “FI_COMPANYCODE_VALUEMAP” to update Company Code |

Profit center

| **Target structure field name** | **Description** | **Mapping Logic/ Constant** |
| --- | --- | --- |
| /ns3:ProfitCentreReplicationBulkRequest/ProfitCentreReplicationRequestMessage/ProfitCentre/ID | CONTROLLING AREA + PROFIT CENTER | Use value mapping table “FI_CONTROLLINGAREA_VALUEMAP” to update CONTROLLING AREA |
| /ns3:ProfitCentreReplicationBulkRequest/ProfitCentreReplicationRequestMessage/ProfitCentre/Name/Name/@languageCode | Language Code | Use value mapping table “FI_LANGCODE_VALUEMAP” to update Language Code |
| /ns3:ProfitCentreReplicationBulkRequest/ProfitCentreReplicationRequestMessage/ProfitCentre/SegmentAssignment/SegmentID | Segment ID | Use value mapping table “FI_PROFITCTR_SEG_VALUEMAP” to update SEGMENT ID |
| /ns3:ProfitCentreReplicationBulkRequest/ProfitCentreReplicationRequestMessage/ProfitCentre/CompanyAssignment/CompanyID | Company Code | Use value mapping table “FI_COMPANYCODE_VALUEMAP” to update Company Code |

### Error Handling & Monitoring

Message Monitoring in SAP Cloud Integration can be used for Error Handling & Monitoring Error/Success Messages.

”Monitor Message Processing / Message Processing Details“ Provides the Log, Payload & S4Response Messages as below.

1. Log (figure 3.1 and 3.4) : Shows the Status of the message
2. Payload (figure 3.2 and 3.5) : Shows the Source Idoc xml Payload
3. S4Response(figure 3.3 and 3.6): Shows the S4C Response message with details of “Profit center/Cost center ID “created in S4HC.

We can use the Source & Response Payload to verify & correlate the cost center/profit center Created in S4HC

Profit Center

<!-- image omitted: cid:image001.png@01D44A8E.D16FE610 -->

Figure 3.1(Log)

<!-- image omitted: cid:image002.png@01D44A8E.D16FE610 -->

Figure 3.2 (source payload)

<!-- image omitted: cid:image009.png@01D44AA5.773F8DA0 -->

Figure 3.3 (response payload)

Cost center

<!-- image omitted: cid:image004.png@01D44A8E.D16FE610 -->

Figure 3.4(Log)

<!-- image omitted: cid:image006.png@01D44A8E.EE62C990 -->

Figure 3.5 (source payload)

<!-- image omitted: cid:image008.png@01D44AA5.773F8DA0 -->

Figure 3.6 (response payload)

## Test Script

### Purpose

In 2 Tier deployment, where S4HANA Cloud runs in the subsidiary and the headquarter is running OP, there is a need to maintain consistent Master data from the headquarter to the subsidiary t*o*achieve harmonized master data across HQ and Subsidiary. To achieve this, with 1808 release, we provide standard iflows to achieve this integration.

This section provides a detailed procedure for testing the scope item after solution deployment. Each process step is covered in its own section, providing the system interactions in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly.

### Prerequisites

This section summarizes all prerequisites needed to conduct the test in terms of system, users, master data, organizational data, and other test data and business conditions.

**Note:**

The process to be tested in this test script is for Subsidiary side regarding a two-tier scenario. Hence integration between Subsidiary system (SAP Cloud ERP) and Headquarter system (SAP Cloud ERP Private or SAP ERP) shall be set up in advance. You will be able to process the test steps only after the headquarters system has sent the required messages.

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
| Overhead Accountant | SAP_BR_OVERHEAD_ACCOUNTANT |  |

#### Master Data, Organizational Data and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data to go through the test procedure.

Make sure that the proper mappings are maintained between the cost center created in OP and cost center in SAP Cloud ERP.

### Overview Table

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Create a cost center in SAP SAP Cloud ERP Private or SAP ERP |  |  | Cost center is created with all the relevant details |
| Check for cost center in SAP Cloud ERP | SAP_BR_OVERHEAD_ACCOUNTANT | Manage cost center | Cost center created with relevant details |
| Create a profit center in SAP SAP Cloud ERP Private or SAP ERP |  |  | Profit center is created with all the relevant details |
| Check for profit center in SAP Cloud ERP | SAP_BR_OVERHEAD_ACCOUNTANT | Manage profit center | Profit center created with relevant details |

### Test Procedure

This section describes test procedures for each process step that belongs to this scope item.

Cost center creation

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on to SAP SAP Cloud ERP Private or SAP ERP | Create Cost center. Note the cost center. | IDoc Triggered in SAP SAP Cloud ERP Private or SAP ERP |
| 2 | Log on to SAP Cloud ERP. | Check cost center created using “Manage cost center” app. | Cost center is displayed. |

Profit center creation

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on to SAP SAP Cloud ERP Private or SAP ERP | Create Profit center. Note the profit center. | IDoc Triggered in SAP SAP Cloud ERP Private or SAP ERP |
| 2 | Log on to SAP Cloud ERP. | Check profit center created using “Manage profit center” app. | Profit center is displayed. |

## Connections
- part-of :: [[_cluster]]
- see-also :: [[16-two-tier-erp-and-central-finance/two-tier-erp-integration-setup-document-230]]
- see-also :: [[06-management-accounting/stammdatenskript-kostenstelle-und-kostenstellengruppe-anlegen-bnm-634]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Master data/Fin Master Data Sync/S4CLD2608_2T_CC_PC_Replication_Guide.docx` — full document · extracted with `mammoth` · 13,604 chars in the whole document
