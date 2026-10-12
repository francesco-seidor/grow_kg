---
id: 13-quality-ehs-and-compliance/transfer-of-bill-of-materials-for-sap-global-trade-services-24h-ae-805
title: Transfer of Bill of Materials for SAP Global Trade Services (24H_AE) (24H_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script 24H_AE for scheduling BOM transfer to SAP Global Trade Services, plus GTS configuration appendix."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/gts-master-data-transfer]
aliases: [24H_S4CLD2608_BPD_EN_AE]
keywords: [Transfer of Contact Persons and BOMs to SAP GTS, bill of materials transfer, global trade services, changed master data transfer, legal units, plant assignment, cross-plant bom evaluation, application jobs, business roles, demo data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/24H_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-805
topic: 13-quality-ehs-and-compliance/gts-master-data-transfer
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Transfer of Bill of Materials for SAP Global Trade Services (24H_AE) (24H_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/24H_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Transfer of Contact Persons and BOMs to SAP GTS** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Transfer of Bill of Materials for SAP Global Trade Services (24H_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Transfer of Bill of Materials for SAP Global Trade Services (24H_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232849006)

[2 Prerequisites 3](#_Toc232849007)

[2.1 System Access 3](#_Toc232849008)

[2.2 Roles 3](#_Toc232849009)

[2.3 Business Conditions 3](#_Toc232849010)

[2.4 Master Data, Organizational Data, and Other Data 4](#_Toc232849011)

[2.5 Additional Manual Configuration 5](#_Toc232849012)

[3 Overview Table 6](#_Toc232849013)

[4 Test Procedures 7](#_Toc232849014)

[4.1 Schedule Transfer of Bill of Materials 7](#_Toc232849015)

[4.2 Schedule Transfer of Changed Master Data (Optional) 8](#_Toc232849016)

[5 Appendix 10](#_Toc232849017)

[5.1 Additional Configurations in SAP Global Trade Services System 10](#_Toc232849018)

[5.1.1 Define Legal Units 10](#_Toc232849019)

[5.1.2 Assign Plant to Legal Unit 10](#_Toc232849020)

[5.1.3 Define Cross-Plant BOM Evaluation 11](#_Toc232849021)

## Purpose

Overview

You can integrate SAP Global Trade Services 11.0 on-premise with SAP S/4HANA Cloud Private Edition or SAP S/4HANA Cloud Public Edition to use existing rules in SAP Global Trade Services.

This scope item enables the communication scenario and the appropriate RFC calls for synchronizing the Bill of Material (BOM). Successful synchronization of BOMs requires that the relevant material masters already exist in the SAP Global Trade Services system.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

The test is conducted in the following systems:

| System | Details |
| --- | --- |
| SAP S/4HANA System | Accessible via FIORI Launchpad.Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Administrator - International Trade | SAP_BR_ADMINISTRATOR_SLL | International Trade Administration | SAP_BR_ADMINISTRATOR_SLL |  |

### Business Conditions

The business process described in this test script is part of a bigger chain of integrated business processes or scope items. As a consequence, you must have completed the following processes and fulfilled the following business conditions before you are able to start going through this scope item:

| Scope Item | Business Condition |
| --- | --- |
| 1WA - Transfer of Primary Master Data for SAP Global Trade Services | Every product in the bill of materials has been transferred into SAP Global Trade Services system. |

Additional configurations in SAP Global Trade Services system:

To make the master data transfer successful, additional configurations might be needed in SAP Global Trade Services system. These configurations depend on your SAP Global Trade Services system, and it's not covered in this document. List the minimum configurations which are needed:

- Defining and Assigning Legal Units
- Assigning Plants from Feeder System to Legal Units
- Defining Cross-Plant BOM Evaluation

|  |
| --- |
| Note When you assign the plants from the feeder system to the plant group, all the specified logical systems must belong to the same group of logical system. |

|  |
| --- |
| Note You can check the details by referring to [Additional Configurations in SAP Global Trade Services System](#unique_6) [page ] 10. |

If the transfer is not successful, you may check the application logs in SAP Global Trade Services system to get the error details and then fix it.

### Master Data, Organizational Data, and Other Data

SAP Best Practices Standard Values based on new global template will be used once available. In the table you still see the master data used for the current baseline.

Essential master and organizational data was created in your SAP S/4HANA Cloud Public Edition system in the implementation phase, such as the data that reflects the organizational structure of your company and master data that suits its operational focus, for example, master data for materials, vendors, and customers.

This master data usually consists of standardized SAP Best Practices default values, and enables you to go through the process steps of this scope item.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

|  |
| --- |
| Note Additional Master Data (Default Values)You can test the scope item with other SAP Best Practices default values that have the same characteristics.Check your SAP system to find out which other material master data exists. |

|  |
| --- |
| Note Using Your Own Master DataYou can also use customized values for any material or organizational data for which you have created master data. For more information about creating master data, see the Master Data Procedures documentation. |

Use the following master data in the process steps described in this document:

Table 1: Master Data Script Reference

| Data | Sample Value | Detail | Comment |
| --- | --- | --- | --- |
| Bill of Material | FG126 | Bill of material FG126 in plant 3310 with usage 1 |  |

For more information about creating master data, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) Script documentation.

Table 2: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNK | Create Material BOM for Production and Sales - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/ed154949a179181b2bd245f014a03d2d)

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Schedule Transfer of Bill of Materials](#unique_10) [page ] 7 | Administrator - International Trade | Schedule Transfer of Bill of Materials - Global Trade Services (F2807) | The selected bill of materials are transferred to the SAP Global Trade Services system. |
| [Schedule Transfer of Changed Master Data (Optional)](#unique_11) [page ] 8 | Administrator - International Trade | Schedule Transfer of Changed Master Data - Global Trade Services (F6041) | The application jobs of transfer changed master data are scheduled, and the changed master data is transferred by the scheduled application jobs. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Schedule Transfer of Bill of Materials

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Transfer the bill of material master data to SAP Global Trade Services system.

Prerequisites

|  |
| --- |
| Caution Before you start the test procedures, ensure that the Set-up Instruction Guide of this scope item is executed to ensure working connectivity between the SAP S/4HANA system and the SAP Global Trade Services system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad using the role Administrator - International Trade. |  |  |
| 2 | Access App | Open Schedule Transfer of Bill of Materials - Global Trade Services (F2807). | The Application Jobs screen is displayed. |  |
| 3 | Create Schedule Transfer of Bill of Materials Background Job | Choose Create. | The New Job view is displayed. |  |
| 4 | Template Selection | Make the following entries and choose Step 2:Job Template: Schedule Transfer of Bill of Materials - Global Trade ServicesJob Name: Schedule Transfer of Bill of Materials - Global Trade Services |  |  |
| 5 | Scheduling Options | Choose Define Recurrence Pattern. Make the following entries and choose OK. Then choose Step 3:Start Immediately: <Selected>Recurrence Pattern: Single Run |  |  |
| 6 | Schedule | Make the following entries and choose Schedule:Valid From: <choose today>Description: <enter the description>Material: FG126Plant: 3310 | The job is scheduled and shown in the list. |  |

### Schedule Transfer of Changed Master Data (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once the master data is updated, you can schedule application jobs to transfer changed master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Administrator - International Trade. |  |  |
| 2 | Access App | Choose Schedule Transfer of Changed Master Data - Global Trade Services (F6041). | The Application Jobs screen displays. |  |
| 3 | Create Schedule Transfer of Changed Master Data Application Jobs | Choose Create. | The New Job view displays. |  |
| 4 | Template Selection | Make the following entries and choose Step 2:Job Template: Schedule Transfer of Changed Master Data to Global Trade ServicesJob Name: Schedule Transfer of Changed Master Data to Global Trade Services | The application logs for the transfer of changed master data are checked. |  |
| 5 | Scheduling Options | Choose Define Recurrence Pattern. Make the following entries and choose OK. Then choose Step 3:Start Immediately: <Select>Recurrence Pattern: Single Run |  |  |
| 6 | Parameters | Make the following entries and choose Schedule:Message Type: /SAPSLL/BOMMAT_SLL | The job is scheduled and displayed in the list. |  |

## Appendix

### Additional Configurations in SAP Global Trade Services System

The following configurations depend on your SAP Global Trade Services system, and the steps and input values might be different in your system.

#### Define Legal Units

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to the SAP Global Trade Services system. | The SAP Easy Access page appears. |  |
| 2 | Transaction Code | In the Command field, enter SPRO and press Enter. |  |  |
| 3 | Access the IMG Activity | From the IMG, go to the following path: SAP Global Trade Services > General Settings > Organizational Structure > Define Legal Units. |  |  |
| 4 | Maintain Legal Units | Define the legal unit, for example LU_3310 and maintain the general data, for example name and address. | The legal unit is maintained or checked. |  |

#### Assign Plant to Legal Unit

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Transaction Code | In the Command field, enter SPRO and press Enter. |  |  |
| 3 | Access the IMG Activity | In the IMG, go to the following path: SAP Global Trade Services > General Settings > Organizational Structure > Assignment of Organizational Units from Feeder System to Legal Unit > Assign Plant at Feeder System Group Level. | The Choose Activity dialog box displays. |  |
| 4 | Assign Plant | Choose Manually Assign Plant. | The Change View “Mapping: Plant from Feeder System Group to Legal Unit” view displays. |  |
| 5 | New Entries | Choose New Entries. |  |  |
| 6 | Assign Plant to Legal Unit | If necessary, make the following entries and choose Save:Logical System group: <choose the logical system group>FS Organization: <your plant in SAP S/4HANA, for example, 3310>Legal Unit: <your created legal unit, for example, LU_3310>Choose Save. | The plant is assigned to the legal unit. |  |

#### Define Cross-Plant BOM Evaluation

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP GUI | Log on to the SAP Global Trade Services system. | The SAP Easy Access page is displayed. |  |
| 2 | Transaction Code | In the Command field, enter SPRO and press Enter. |  |  |
| 3 | Access the IMG Activity | From the IMG, go to the following path: SAP Global Trade Services > General Settings > Organizational Structure > Define Cross-Plant BOM Evaluation . | The Change View “Group for Cross-Plant Preference Determination”: Overview view displays. |  |
| 4 | Define Cross-Plant BOM Evaluation | Choose New Entries.If necessary, make the following entries and press Enter:Grouping of Org. Unit FS: <plant group name>Description: <description> |  |  |
| 5 | Define Cross-Plant BOM Evaluation | Select your entry and in the Dialog Structure pane, double-click Assignment of Plants.Choose New Entries.Make the following entries and choose Save:Logical System: <choose the logical system>Plant: <your SAP S/4HANA plant, for example,3310> | The cross-plant BOM evaluation is defined. |  |

Typographic Conventions

| Type Style | Description |
| --- | --- |
| Example | Words or characters quoted from the screen. These include field names, screen titles, pushbuttons labels, menu names, menu paths, and menu options.Textual cross-references to other documents. |
| Example | Emphasized words or expressions. |
| EXAMPLE | Technical names of system objects. These include report names, program names, transaction codes, table names, and key concepts of a programming language when they are surrounded by body text, for example, SELECT and INCLUDE. |
| Example | Output on the screen. This includes file and directory names and their paths, messages, names of variables and parameters, source text, and names of installation, upgrade and database tools. |
| Example | Exact user entry. These are words or characters that you enter in the system exactly as they appear in the documentation. |
| <Example> | Variable user entry. Angle brackets indicate that you replace these words and characters with appropriate entries to make entries in the system. |
| EXAMPLE | Keys on the keyboard, for example, F2 or ENTER. |

|  |
| --- |
|  |
| www.sap.com/contactsap |
| © 2026 SAP SE or an SAP affiliate company. All rights reserved.No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE or an SAP affiliate company. The information contained herein may be changed without prior notice. Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors. National product specifications may vary.These materials are provided by SAP SE or an SAP affiliate company for informational purposes only, without representation or warranty of any kind, and SAP or its affiliated companies shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP or SAP affiliate company products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty. SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE (or an SAP affiliate company) in Germany and other countries. All other product and service names mentioned are the trademarks of their respective companies. See [www.sap.com/copyright](http://www.sap.com/copyright) for additional trademark information and notices. |

<!-- image omitted: SAP Logo -->

## Connections
- part-of :: [[_cluster]]
- related-to :: [[13-quality-ehs-and-compliance/test-script-transfer-of-primary-master-data-for-sap-global-trade-servi]]
- related-to :: [[13-quality-ehs-and-compliance/transfer-of-contact-person-for-sap-global-trade-services-24f-test-scri]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/24H_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 19,399 chars in the whole document
