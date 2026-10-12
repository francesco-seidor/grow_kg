---
id: 16-two-tier-erp-and-central-finance/two-tier-erp-bill-of-material-integration-using-cloud-integration-236
title: Two Tier ERP – Bill of Material Integration using Cloud Integration (S4CLD2608_2T_BoM_Int_User_Guide)
description: "Customer guide for replicating BOMs from HQ (Cloud ERP Private/SAP ERP) to a subsidiary SAP Cloud ERP via BOMMAT01 IDoc, Cloud Integration and OData, with field mapping and test script."
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/product-and-bom-replication]
aliases: [S4CLD2608_2T_BoM_Int_User_Guide]
keywords: [Two-Tier Product Master and BOM Replication, bill of material integration, two-tier erp, cloud integration iflow, bom field mapping, error handling monitoring, communication arrangement, test script, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Master data/Bill Of Material Integration/S4CLD2608_2T_BoM_Int_User_Guide.DOCX]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-236
topic: 16-two-tier-erp-and-central-finance/product-and-bom-replication
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Two Tier ERP – Bill of Material Integration using Cloud Integration (S4CLD2608_2T_BoM_Int_User_Guide)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Master data/Bill Of Material Integration/S4CLD2608_2T_BoM_Int_User_Guide.DOCX`, extracted with `mammoth`. Grouped under **Two-Tier Product Master and BOM Replication** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP Cloud ERP June 2026English |  |
|  | Two Tier ERP – Bill of Material Integration using Cloud Integration |
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
| 0 | 31.08.2018 | Initial version of document |
|  | 06.2026 | Update |

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

This document will provide the steps for Bill of Material integration in a 2-Tier scenario. The Bill of Material created at the HQ (SAP Cloud ERP Private or SAP ERP) will be replicated to the subsidiary (SAP Cloud ERP).

## Business Requirements

In a two-tier model, SAP Cloud ERP and SAP Cloud ERP Private systems can support the organization and subsidiaries to run in an independent yet integrated fashion. The engineering BOM is created in SAP Cloud ERP Private (headquarters) and sent to S4HANA Cloud for converting the engineering BOM to Manufacturing BOM.

## Technical Details

Important: Rename the file “2TIER INTEGRATION _ Product Lifecycle Management Master Data Integration.dat” as “2TIER INTEGRATION _ Product Lifecycle Management Master Data Integration.zip”

The main steps in the scenario:

1. Bill of Materials IDoc BOMMAT01 is created in SAP Cloud ERP Private or SAP ERP.

2. The IDOCs are sent from SAP Cloud ERP Private or SAP ERP system to SAP Cloud Integration and mapped to Bill of Material OData API (API_BILL_OF_MATERIAL_SRV).

3. The Bill of Material is created by Integration using OData API in SAP Cloud ERP System.

### Prerequisites

The following list of prerequisite configurations are to be in place to realize the integration process.

***Configuration in SAP Cloud ERP:***

1. Create a Communication User in SAP Cloud ERP system. This user credential will be used in OData adapter in SAP Cloud Integration tenant.
2. Maintain a Communication System to specify the host details.
3. Maintain a Communication Arrangement to facilitate the usage of API. The Communication Scenario used for Bill of Material is SAP_COM_0105.

***Configuration in SAP Cloud ERP Private or SAP ERP*:**

The outgoing IDOC (BOMMAT01) needs to be processed and sent to CPI. We need to maintain the following configurations.

1. Maintain the RFC Connection in SM59 to target URL to Cloud Integration.
2. Create Port & Partner Profile in WE21 & WE20.
3. Generate model view in BD64.

**Creation of SAP Cloud Integration iFlow:**

<!-- image omitted: unnamed -->

Figure 1.0

### Mapping Prerequisites

The Customer specific field mappings are suggested below for the target structure. However, the fields might not be limited to the ones given and the Customer needs to take care of the same during implementation. Some constant or logic has to be set against these fields.

**Bill of Material:**

| **Target structure field name** | **Description** | **Mapping Logic/ Constant** |
| --- | --- | --- |
| BOMGroup | BOM Group | STLNR |
| BOMHeaderBaseUnit | BOM Header Base Unit | BMEIN |
| BOMHeaderQuantityInBaseUnit | BOM Header Quantity In Base Unit | BMENG_C |
| BOMHeaderText | BOM Header Text | ZTEXT |
| BillOfMaterialCategory | Bill Of Material Category | STLTY |
| BOM Material Status | BOM Material Status | STLST |
| BillOfMaterialVariant | Bill Of Material Variant | STLAL |
| BillOfMaterialVariantUsage | Bill Of Material Variant Usage | STLAN |
| DocumentIsCreatedByCAD | Document Is Created By CAD | CADKZ |
| EngineeringChangeDocument | Engineering Change Document | AENNR |
| HeaderValidityStartDate | Header Validity Start Date | DATUV |
| IsMultipleBOMAlt | Multiple BOM Alt | STLAL |
| LastChangeDate | Last Change Date | STLDT |

**Bill of Material Item:**

| **Target structure field name** | **Description** | **Mapping Logic/ Constant** |
| --- | --- | --- |
| BillOfMaterialItemNumber | Bill Of Material Item Number | POSNR |
| BillOfMaterialItemCategory | Bill Of Material Item Category | POSTP |
| BillOfMaterialComponent | Bill Of Material Component | IDNRK |
| BOMItemDescription | BOM Item Description | POTXT1 |
| BillOfMaterialItemQuantity | Bill Of Material Item Quantity | ROMEN |
| BillOfMaterialItemUnit | Bill Of Material Item Unit | MEINS |
| IsAssembly | Is Assembly | STKKZ |
| ValidityStartDate | Validity Start Date | DATUV |
| EngineeringChangeDocument | Engineering Change Document | AENNR |
| DocumentIsCreatedByCAD | Document Is Created By CAD | CADPO |
| IsEngineeringRelevant | Is Engineering Relevant | SANKO |
| IsProductionRelevant | Is Production Relevant | SANFE |
| BOMItemIsCostingRelevant | BOM Item Is Costing Relevant | SANKA |
| OperationScrapInPercent | Operation Scrap In Percent | AVOAU |
| ComponentScrapInPercent | Component Scrap In Percent | AUSCH |
| IsBulkMaterial | Is Bulk Material | SCHGT |
| IsDeleted | Is Deleted | LKENZ |
| IsConfigurableBOM | Is Configurable BOM | CSLTY |
| DocumentType | Document Type | DOKAR |
| DocNumber | Doc Number | DOKNR |
| DocumentPart | Document Part | DOKTL |
| DocumentVersion | Document Version | DOKVR |
| BOMItemSorter | BOM Item Sorter | ID_SORT |
| Plant | Plant | WERKS |

### Error Handling & Monitoring

Message Monitoring in SAP Cloud Integration can be used for Error Handling & Monitoring Error/ Success Messages.

”Monitor Message Processing / Message Processing Details“ Provides the Log, Payload & S4Response Messages as below.

1. Log (figure 1.1) : Shows the Status of the message
2. Payload (figure 1.2) : Shows the Source Idoc xml Payload
3. S4Response(figure1.3): Shows the S4C Response message with details created in S4HC.

We can use the Source & Response Payload to verify & correlate the Bill of Material Created in S4HC.

<!-- image omitted: unnamed -->

Figure 1.1(Log)

<!-- image omitted: unnamed -->

Figure 1.2 (source payload)

<!-- image omitted: unnamed -->

Figure 1.3 (response payload)

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
| BOM Engineer | SAP_BR_BOM_ENGINEER |  |

#### Master Data, Organizational Data and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data to go through the test procedure.

Make sure that the proper mappings are maintained between the process objects in SAP Cloud ERP and Sales Order in SAP Cloud ERP Private or SAP ERP.

### Overview Table

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Create a Bill of Material Document in SAP Cloud ERP Private or SAP ERP |  |  | BOM IDoc is created with all the relevant items and other details |
| Check for Bill Of Material in SAP Cloud ERP | SAP_BR_BOM_ENGINEER | Display Bill of Material FIORI App | BOM created with relevant details |

### Test Procedure

This section describes test procedures for each process step that belongs to this scope item.

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log on to SAP Cloud ERP Private or SAP ERP | Create Bill of Material. Note the BOM number. | IDoc Triggered in SAP Cloud ERP Private or SAP ERP |
| 2 | Log on to SAP Cloud ERP. | Check Bill of Material created using “Display Bill of Material” app. The Bill of Material number will be displayed in the App. | BOM is displayed. |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[16-two-tier-erp-and-central-finance/two-tier-master-data-replication-product-master-customer-guide-234]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Master data/Bill Of Material Integration/S4CLD2608_2T_BoM_Int_User_Guide.DOCX` — full document · extracted with `mammoth` · 12,104 chars in the whole document
