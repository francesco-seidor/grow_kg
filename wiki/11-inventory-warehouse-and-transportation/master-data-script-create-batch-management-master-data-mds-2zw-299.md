---
id: 11-inventory-warehouse-and-transportation/master-data-script-create-batch-management-master-data-mds-2zw-299
title: "Master Data Script: Create Batch Management Master Data - MDS (2ZW) (2ZW_S4CLD2608_Master_Data_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script (2ZW) for creating batch management master data: characteristics, classes, sort sequences, search and derivation strategies."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/batch-management-master-data]
aliases: [2ZW_S4CLD2608_Master_Data_EN_XX]
keywords: [Batch Management Master Data, batch management, batch characteristics, batch classes, sort sequences, batch search strategies, batch determination, batch derivation strategies, business roles, test procedures]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2ZW_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-299
topic: 11-inventory-warehouse-and-transportation/batch-management-master-data
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Batch Management Master Data - MDS (2ZW) (2ZW_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2ZW_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Batch Management Master Data** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Batch Management Master Data - MDS (2ZW) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904587)

[2 Prerequisites 3](#_Toc233904588)

[2.1 System Access 3](#_Toc233904589)

[2.2 Roles 3](#_Toc233904590)

[3 Overview Table 4](#_Toc233904591)

[4 Test Procedures 5](#_Toc233904592)

[4.1 Create Characteristic 5](#_Toc233904593)

[4.2 Create Class 6](#_Toc233904594)

[4.3 Create Sort Sequence 7](#_Toc233904595)

[4.4 Create Batch Search Strategy Records for Inventory Management 8](#_Toc233904596)

[4.5 Create Batch Search Strategy Records for Production 10](#_Toc233904597)

[4.6 Create Batch Search Strategy Records for Sales and Distribution 12](#_Toc233904598)

[4.7 Create Derivation Strategy for Sender Material 13](#_Toc233904599)

[4.8 Create Derivation Strategy for Receiver Material 15](#_Toc233904600)

## Purpose

Batch management master data includes batch specifications, sort sequences (sort rules) and batch search strategy records in batch determination.

Batch specifications describe the technical, physical and chemical properties of a batch. You store batch specifications, such as batch status or active ingredient potency, as characteristics in the Classification System.

You can use the classification system to assign the material specifications to the material of a batch. These material specifications are assigned to the same class as the batches of the materials. Thus, you can store the target values of a batch with the respective tolerance range. These target values are, for instance, used in quality inspection or during the goods receipt transaction, if it is necessary to immediately classify a batch. The values are also employed for the usability check.

In the material, you store the target ranges for all characteristics. As the batch belongs to the same class as the material, the batch automatically receives the characteristics of the material. For each individual batch, you enter the exact actual values.

Batch Determination happening in different processes (Inventory Management, Production, Sales and Distribution) have different criteria. Sort sequences and batch search strategy records are required to maintain the criteria.

The sort sequence tells you whether batches in the search result of the batch determination are sorted in ascending or descending order of characteristic values.

In a batch search strategy for batch determination, you can define the values according to which the system is to find batches, including attributes for process (e.g. movement type, order type or plant) and material number. Only when the condition records are satisfied can those batches be further sorted and determined based on sort sequences and batch specifications.

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| BOM Engineer | SAP_BR_BOM_ENGINEER | Bills Of Material | SAP_BR_BOM_ENGINEER |  |
| Master Data Specialist - Batch Data | SAP_BR_BATCH_MASTER_SPCLST | Master Data - Batch | SAP_BR_BATCH_MASTER_SPCLST |  |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Characteristic](#unique_6) [page ] 5 | BOM Engineer | Manage Characteristics (CT04) | Characteristic is created. |
| [Create Class](#unique_7) [page ] 6 | BOM Engineer | Manage Classes (CL02) | Class is created. |
| [Create Sort Sequence](#unique_8) [page ] 7 | Master Data Specialist - Batch Data | Create Sort Sequence (CU70) | Sort Sequence is created. |
| [Create Batch Search Strategy Records for Inventory Management](#unique_9) [page ] 8 | Master Data Specialist - Batch Data | Manage Search Strategies - Inventory Management (MBC2) | Batch Search Strategy Records are created. |
| [Create Batch Search Strategy Records for Production](#unique_10) [page ] 10 | Master Data Specialist - Batch Data | Manage Search Strategies - Production (COB2) | Batch Search Strategy Records are created. |
| [Create Batch Search Strategy Records for Sales and Distribution](#unique_11) [page ] 12 | Master Data Specialist - Batch Data | Manage Search Strategies - Sales and Distribution (VCH2) | Batch Search Strategy Records are created. |
| [Create Derivation Strategy for Sender Material](#unique_12) [page ] 13 | Master Data Specialist - Batch Data | Manage Derivation Strategies - Sender (DVS2) | Derivation Strategy for Sender Material is created. |
| [Create Derivation Strategy for Receiver Material](#unique_13) [page ] 15 | Master Data Specialist - Batch Data | Manage Derivation Strategies - Receiver (DVR2) | Derivation Strategy for Receiver Material is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Characteristic

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating characteristic.

Procedure

Use the following procedure when your user access presents you with the Manage Characteristics (CT04) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Characteristics (CT04). | The Characteristics screen displays.Note Common screen for create, change, and display mode. |  |
| 3 | Enter Characteristic Name | Enter the following and choose Create.Characteristic: <Your Characteristic Name> | The Basic data screen options display.Note The value in the Valid from field is auto-populated. |  |
| 4 | Enter Basic Data | Enter the following and choose Save:Basic data section:Description: <Enter your description>Status: Released (default)Format section:Data Type: <Choose a format>Value assignment section:Select the Single-value radio button. | Note Other fields for chosen format are required in the Format section. Maintain accordingly. |  |
| 5 | Enter Values for Check | On the Values tab, in the Allowed Values section, enter the values allowed for this characteristic. |  |  |
| 6 | Save the Characteristic | Choose Save. | The characteristic is created. |  |

### Create Class

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating class.

Prerequisite

You must complete the previous section, [Create Characteristic](#unique_6) [page ] 5, before you proceed with this section.

Procedure

Follow the following procedure when your user access presents you with the Manage Classes (CL02) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Classes (CL02). | The Class screen displays.Note It is a common screen for creation, change, and display mode. |  |
| 3 | Enter Class Name | Make the following entries and choose Create:Class: <Class name>Class Type: 023 | The Create Class screen displays.Note The Valid From field is automatically filled in with a value. |  |
| 4 | Enter Basic Data | On the Basic data tab, make the following entries:In the Basic data section:Description: <Class description>Status: Released |  |  |
| 5 | Enter Char. Tab | Select the Char. tab and make the following entry to assign characteristics you have created to this class, and then press Enter:In the Char. column:Char.: <Characteristic name> | The Description and Data Type fields of characteristics are automatically filled in with values. |  |

### Create Sort Sequence

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating sort sequences.

Prerequisite

You must complete the section Create Characteristic before you proceed with this section.

Procedure

Use the following procedure when your user access presents you with the Create Sort Sequence (CU70) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Batch Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Sort Sequence (CU70). | The Create Sort Sequence screen displays. |  |
| 3 | Enter Sort Sequence Name | Make the following entries and choose the Create icon:Sort Sequence: <Sort Sequence Name> | The Create Sort Sequence: Basic Data screen displays. |  |
| 4 | Enter Basic Data | Maintain the description beside the Sort Sequence Name, and choose Characteristics.Description: <Sort Sequence Description> | The Create Sort Sequence: Characteristics screen displays. |  |
| 5 | Enter Sort Sequence details | Choose New Entries to maintain the following columns, and choose Save:Characteristic: <Characteristic Name>Ascending: XDscending: ‘ ’ | The sort sequence is created.Note You can specify either ascending or descending order. |  |

### Create Batch Search Strategy Records for Inventory Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating search strategies for batch determination.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Batch Data. | The SAP Fiori launchpad displays. |  |
| 2 | The SAP Fiori launchpad displays. | Open Manage Search Strategies - Inventory Management (MBC2). | The Change Batch Search Strategy: Initial Screen displays. |  |
| 3 | Enter Strategy Type | Make the following entries and choose Change:Strategy Type: <Strategy Type, e.g. YB11>Note the Strategy Type is configurable by Self Service Configuration UI. | The pop-up Key Combination displays. |  |
| 4 | Choose Key Combination | In the pop-up Key Combination, select one from the following options, and choose Choose:Movement Type/Plant/MaterialPlant/MaterialMovement Type/MaterialMovement Type/PlantMovement Type | The Change BP: Batch number (YB11): Selection displays. | The Key Combinations are dependent to the Strategy Type you choose. If there is only one key combination in your selected strategy, the pop-up won't show up. |
| 5 | Enter your Selection | To specify your records, enter the following attributes that are displayed based on the chosen Key Combination, and choose Execute:Goods Movement Type: <Goods Movement Type>Plant: <Plant>Material: <Material Number> | The Change BP: Batch number (YB11) : Fast Entry displays. |  |
| 6 | Enter your Strategy Record in detail | To create a new record, you should enter the following entries, and choose Save:Material: <Material Number>If required, you can also specify the following attributes for each record:No. batch splitsChanges allowedDialog batch determinationDisplay UoMQuantity proposalOverdelivery allowedSelection type |  |  |
| 7 | Maintain Selection criteria (optional) | To further maintain the selection criteria for batch characteristic value of the material in a record, select the record and choose Selection Criteria. | The Change BP: Classification displays. |  |
| 8 | Maintain Sort Sequence (optional) | To maintain sort sequence for specific records, select the record and choose Sort. | The Change BP: Batch number (YB11) : Sort Rule displays. |  |

### Create Batch Search Strategy Records for Production

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating search strategies for batch determination.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Batch Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Search Strategies - Production (COB2). | The Change Batch Search Strategy: Initial Screen displays. |  |
| 3 | Enter Strategy Type | Make the following entries and choose Change:Strategy Type: <Strategy Type, e.g. YB11>Note The Strategy Type is configurable by Self Service Configuration UI. | The Change BP: Batch number (YB11): Selection displays.Note Key Combination is not shown as there is only one key combination configured for YB11 in production |  |
| 4 | Enter your Selection | To specify your records, enter the following attributes that are displayed based on the chosen Key Combination, and choose Execute:Order Type: <Order Type>Plant: <Plant>Material: <Material Number> | The Change BP: Batch number (YB11) : Fast Entry displays. | The Key Combinations are dependent to the Strategy Type you choose. If there is only one key combination in your selected strategy, the pop-up won't show up. |
| 5 | Enter your Strategy Record in detail | To create a new record, you should enter the following entries, and choose Save:Material: <Material Number>If required, you can also specify the following attributes for each record:No. batch splitsChanges allowedDialog batch determinationDisplay UoMQuantity proposalOverdelivery allowedSelection type |  |  |
| 6 | Maintain Selection criteria (optional) | To further maintain the selection criteria for batch characteristic value of the material in a record, select the record and choose Selection Criteria. | The Change BP: Classification displays. |  |
| 7 | Maintain Sort Sequence (optional) | To maintain sort sequence for specific records, select the record and choose Sort. | The Change BP: Batch number (YB11) : Sort Rule displays. |  |

### Create Batch Search Strategy Records for Sales and Distribution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating search strategies for batch determination.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Batch Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Search Strategies - Sales and Distribution (VCH2). | The Change Batch Search Strategy: Initial Screen displays. |  |
| 3 | Enter Strategy Type | Make the following entries and choose Change:Strategy Type: <Strategy Type, e.g. YB11>Note the Strategy Type is configurable by Self Service Configuration UI. | The pop-up Key Combination displays. |  |
| 4 | Choose Key Combination | In the pop-up Key Combination, select one from the following options, and choose Choose:Customer/MaterialMaterial | The Change BP: Batch number (YB11): Selection displays. | The Key Combinations are dependent to the Strategy Type you choose. If there is only one key combination in your selected strategy, the pop-up won't show up. |
| 5 | Enter your Selection | To specify your records, enter the following attributes that are displayed based on the chosen Key Combination, and choose Execute:Customer: <Customer ID>Material: <Material Number> | The Change BP: Batch number (YB11) : Fast Entry displays. |  |
| 6 | Enter your Strategy Record in detail | To create a new record, you should enter the following entries, and choose Save:Material: <Material Number>If required, you can also specify the following attributes for each record:No. batch splitsChanges allowedDialog batch determinationDisplay UoMQuantity proposalOverdelivery allowedSelection type |  |  |
| 7 | Maintain Selection criteria (optional) | To further maintain the selection criteria for batch characteristic value of the material in a record, select the record and choose Selection criteria. | The Change BP: Classification displays. |  |
| 8 | Maintain Sort Sequence (optional) | To maintain sort sequence for specific records, select the record and choose Sort. | The Change BP: Batch number (YB11) : Sort Rule displays. |  |

### Create Derivation Strategy for Sender Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating strategy records which are used to determine attributes for sender material during batch derivation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Batch Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Derivation Strategies - Sender (DVS2). | The Derivation - Change Search Strategy: Initial screen displays. |  |
| 3 | Enter Strategy Type | Make the following entry and choose Change:Strategy Type: <Strategy Type> | The pop-up Key Combination displays. | Before this step, you need to finish the following Configuration Steps based on your requirement:Number Ranges for Batch DerivationDetermine Sending Batches in Batch Derivation |
| 4 | Choose Key Combination | In the pop-up Key Combination, select one from the following options, and choose Choose:<Key Combination 1><Key Combination 2>… | The Change <Strategy Type>: Selection screen displays. | The Key Combinations are dependent to the Strategy Type you choose. |
| 5 | Enter Your Selection | To specify your records, enter the following attributes that are displayed based on the chosen Key Combination, and choose Execute:Sender Material:<Sender Material ID><Key Field>: <Key Value>… | The Change <Strategy Type>: Fast Entry screen displays. |  |
| 6 | Enter Your Strategy Record | To create a new record, you should enter the following entry, and choose Save:Sender Material: <Sender Material ID>To further maintain the details for the sender material, select one record and choose Details. | The Change <Strategy Type>: Details screen displays. |  |
| 7 | Maintain Strategy Record Details | In the Sent Attributes (Fields/Characteristics) section, make the following entries, and choose Save:Attribute: <Sender Material ID>Field: <Selected by default>Characteristic: <Unselected by default> |  |  |

### Create Derivation Strategy for Receiver Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating strategy records which are used to determine attributes for receiver material during batch derivation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Batch Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Derivation Strategies - Receiver (DVR2). | The Derivation - Change Search Strategy: Initial screen displays. |  |
| 3 | Enter Strategy Type | Make the following entry and choose Change:Strategy Type: <Strategy Type> | The pop-up Key Combination displays. | Before this step, you need to finish the following Configuration Steps based on your requirement:Number Ranges for Batch DerivationDetermine Receiving Batches in Batch Derivation |
| 4 | Choose Key Combination | In the pop-up Key Combination, select one from the following options, and choose Choose:<Key Combination 1><Key Combination 2>… | The Change <Strategy Type>: Selection screen displays. | The Key Combinations are dependent to the Strategy Type you choose. |
| 5 | Enter Your Selection | To specify your records, enter the following attributes that are displayed based on the chosen Key Combination, and choose Execute:Receiver Material: <Receiver Material ID><Key Field>: <Key Value>… | The Change <Strategy Type>: Fast Entry screen displays. |  |
| 6 | Enter Your Strategy Record | To create a new record, you should enter the following entry, and choose Save:Receiver Material: <Receiver Material ID>To further maintain the details for the receiver material, select one record and choose Details. | The Change <Strategy Type>: Details screen displays. |  |
| 7 | Maintain Strategy Record Details | Under the tab Attributes, in the Received Attributes (Fields/Characteristics) section, enter the following entries, and choose Save:Attribute: <Reciever Material ID>Field: <Selected by default>Characteristic: <Unselected by default>To maintain the rules for each attribute, select one attribute and choose the tab Rules, and then you can maintain the following rules:Rules for Controlling DerivationSender Field EmptyOverwrite ReceiverLevels in Batch Where-used ListReceiver does not sendRules for Value Selection if more than one SenderComparativeBooleanMultiple-Value Characteristics |  |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/mds-2zw-301]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-2zw-303]]
- related-to :: [[11-inventory-warehouse-and-transportation/script-de-dados-mestre-criar-dados-mestre-de-administracao-de-lotes-2z]]
- related-to :: [[11-inventory-warehouse-and-transportation/script-de-datos-maestros-crear-datos-maestros-de-gestion-de-lotes-mds]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2ZW_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 27,215 chars in the whole document
