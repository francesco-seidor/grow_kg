---
id: 11-inventory-warehouse-and-transportation/test-script-batch-management-blf-ae-sap-s-4hana-cloud-public-edition-2
title: "Test Script: Batch Management (BLF_AE) - SAP S/4HANA Cloud Public Edition 2608 (BLF_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for the Batch Management scope item (UAE localization): prerequisites, sample materials and step-by-step Fiori tests for batch creation, change, search and where-used."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/batch-management-master-data]
aliases: [BLF_S4CLD2608_BPD_EN_AE]
keywords: [Batch Management Master Data, batch management, batch creation, batch master records, batch search, batch where-used, batch information cockpit, test scripts, business roles, master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BLF_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1283
topic: 11-inventory-warehouse-and-transportation/batch-management-master-data
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Batch Management (BLF_AE) - SAP S/4HANA Cloud Public Edition 2608 (BLF_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BLF_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Batch Management Master Data** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Batch Management (BLF_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232862187)

[2 Prerequisites 4](#_Toc232862188)

[2.1 System Access 4](#_Toc232862189)

[2.2 Roles 4](#_Toc232862190)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232862191)

[2.4 Business Conditions 6](#_Toc232862192)

[2.5 Preliminary Steps 7](#_Toc232862193)

[3 Overview Table 9](#_Toc232862194)

[4 Test Procedures 10](#_Toc232862195)

[4.1 Batch Creation 10](#_Toc232862196)

[4.1.1 Optional 1: Create Batches via Manage Batches App 10](#_Toc232862197)

[4.1.2 Optional 2: Create Batches via Create Batch App 11](#_Toc232862198)

[4.2 Batch Master Change 12](#_Toc232862199)

[4.2.1 Option 1: Maintain Batch Master Record via Manage Batches App 12](#_Toc232862200)

[4.2.2 Option 2: Maintain Batch Master Record via Change Batch App 14](#_Toc232862201)

[4.2.3 Display Change 15](#_Toc232862202)

[4.2.3.1 Option 1: Search Batch via Launchpad Search 15](#_Toc232862203)

[4.2.3.2 Option 2: Search Batch via Manage Batches App 17](#_Toc232862204)

[4.3 Batch Where-Used 18](#_Toc232862205)

[4.3.1 Batch Information Cockpit - Batch Selection 18](#_Toc232862206)

[4.3.2 Batch Information Cockpit - Change Batch Selection 19](#_Toc232862207)

[4.3.3 Batch Information Cockpit - Top-Down and Bottom-Up Analysis 21](#_Toc232862208)

## Purpose

Overview

Batch Management incorporates the entire logistics process, from procurement to sales. It's closely linked with classification, but can also be used without classification.

Batch Management is defined as tagging a produced or procured material with a unique 10-digit alphanumeric code. Every batch number can have an inventory quantity associated with it.

The batch number generated for the material quantity helps with uniquely sorting the material inventory and stores the characteristics values or the chemical composition or the product specifications at the time of its production or procurement.

A configuration activity Specify Batch Management Default by Plant is available, which enables you to specify whether batch management is used by default in Material Master for each plant.

If the Not Batch Managed column of a plant is selected, the plant won't use batch management by default when a new material is set as batch managed. You can still overwrite this setting later by maintaining Material Master with plant data.

Batch derivation configuration activities are available. You can use batch derivation scenario after finishing the configuration. Batch derivation enables you to do the following for batch master data and classification data of the component batches of produced batches:

- Transfer
- Display for selection
- Display

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites needed to conduct the test in terms of system, user, master data, organizational data, and other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

|  |
| --- |
| Note The display of some objects, e.g. material documents, is handled more strictly. You have to check with your company policy, and assign one or more of the mentioned roles below to your user to work with all objects described in this test script. |

| Name (Role Template) | Description | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- | --- |
| Quality Technician |  | SAP_BR_QUALITY_TECHNICIAN | Quality Inspection | SAP_BR_QUALITY_TECHNICIAN |  |
| Warehouse Clerk |  | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Inventory Manager |  | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFOBatch Class: YB_BATCH Batch FIFO (first-in-first-out)Characteristic 1: Batch NumberCharacteristic 2: Vendor Batch Number | See [Business Conditions](#unique_6) [page ] 6 and [Preliminary Steps](#unique_7) [page ] 7 sections. |
| Material | TG22 | Trad.Good 22,Reorder Point,Batch-ExpDBatch Class: YB_EXP_DATE_001 Products with expiration dateCharacteristic: Expiration date, shelf life. | See [Business Conditions](#unique_6) [page ] 6 and [Preliminary Steps](#unique_7) [page ] 7 sections. |
| Material | FG29 | FIN29,MTS-PI,PD,Batch-ExpirationDateBatch Class: YB_EXP_DATE_001 Products with expiration dateCharacteristic: Expiration date, shelf life. | See [Business Conditions](#unique_6) [page ] 6 and [Preliminary Steps](#unique_7) [page ] 7 sections. |
| Material | RM09 | RAW09,PD,Batch-FifoBatch Class: YB_BATCH Batch FIFO (first-in-first-out)Characteristic 1: Batch NumberCharacteristic 2: Vendor Batch Number |  |
| Material | RM19 | RAW19,PD,Batch-Fifo,LeanQMBatch Class: YB_BATCH Batch FIFO (first-in-first-out)Characteristic 1: Batch NumberCharacteristic 2: Vendor Batch Number |  |
| Material | RM30 | RAW30,VB,Batch-FifoBatch Class: YB_BATCH Batch FIFO (first-in-first-out)Characteristic 1: Batch NumberCharacteristic 2: Vendor Batch Number |  |
| Material | RM122 | RAW122,PD,Batch-Fifo,ProcureImportBatch Class: YB_BATCH Batch FIFO (first-in-first-out)Characteristic 1: Batch NumberCharacteristic 2: Vendor Batch Number |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| 2ZW | Create Batch Management Master Data - MDS |

### Business Conditions

Before this test script can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BJ8 - Make-to-Stock – Process Manufacturing Based on Process Order | If you use finished goods (FERT) you can either:Go through Make-to-Stock – Process Manufacturing Based on Process Order business process (for material FG29) or create initial stock (refer to Preliminary Steps section for more details). |
| J45 - Procurement of Direct Materials | If you use trading materials, you can either:Go through Procurement of Direct Materials business process or create initial stock (refer to Preliminary Steps section for more details). |

### Preliminary Steps

Purpose

The purpose of this activity is to post initial stock for materials in case there is not sufficient material on stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Receipt Other screen displays. | It only displays it that way if it was your last transaction. So the action for the User should be to select field Reference Document for Transaction Other |
| 3 | Input Movement Type | On the initial screen, make the following entries and press Enter:Trans./Event: Goods ReceiptReference Document: OtherMovement Type: 561 (Init.entry of stBal.) |  |  |
| 4 | Input on the Goods Receipt Other Screen: Material Tab | On the Goods Receipt Other screen, go to the Material tab, make the following entry and press Enter:Material: TG22 |  |  |
| 5 | Input on the Goods Receipt Other Screen: Quantity Tab | On the Goods Receipt Other screen, go to the Quantity tab, make the following entries and press Enter:Qty in Unit of Entry: Qty in UOMUnit of Entry: PC |  |  |
| 6 | Input on the Goods Receipt Other Screen: Where Tab | On the Goods Receipt Other screen, go to the Where tab, make the following entries and press Enter.Plant: 3310Storage Location: 331A |  |  |
| 7 | Input on the Goods Receipt Other Screen: Batch Tab | On the Goods Receipt Other screen, go to the Batch tab, make the following entries and press Enter.Batch: enter external batch number or leave empty for internal number assignmentDate of Manufacture: Maintain the date when necessary. |  | The field of Date of Manufacture is used for the app: Stock Champion in Scope Item: 1JR. |
| 8 | Save Your Entries | Select Item OK and then choose Post. | The system displays the message: Material document 5xxxxxxxxx posted. |  |

Result

You have posted a material to stock and created a batch record.

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction | Expected Results |
| --- | --- | --- | --- |
| Batch Creation |  |  |  |
| [Optional 1: Create Batches via Manage Batches App](#unique_9) [page ] 10 | Quality Technician | Manage Batches (F2462) |  |
| [Optional 2: Create Batches via Create Batch App](#unique_10) [page ] 11 | Quality Technician | Create Batch (MSC1N) |  |
| Batch Master Change |  |  |  |
| [Option 1: Maintain Batch Master Record via Manage Batches App](#unique_11) [page ] 12 | Quality Technician | Manage Batches (F2462) |  |
| [Option 2: Maintain Batch Master Record via Change Batch App](#unique_12) [page ] 14 | Quality Technician | Change Batch (MSC2N) |  |
| Display Change |  |  |  |
| [Option 1: Search Batch via Launchpad Search](#unique_13) [page ] 15 | Quality Technician | Enterprise Search for Batches |  |
| [Option 2: Search Batch via Manage Batches App](#unique_14) [page ] 17 | Quality Technician | Manage Batches (F2462) |  |
| Batch Where-Used |  |  |  |
| [Batch Information Cockpit - Batch Selection](#unique_15) [page ] 18 | Quality Technician | Batch Information Cockpit (BMBC) |  |
| [Batch Information Cockpit - Change Batch Selection](#unique_16) [page ] 19 | Quality Technician | Batch Information Cockpit (BMBC) |  |
| [Batch Information Cockpit - Top-Down and Bottom-Up Analysis](#unique_17) [page ] 21 | Quality Technician | Batch Information Cockpit (BMBC) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

The test should take around <Enter a duration, e.g. 60 minutes>.

### Batch Creation

#### Optional 1: Create Batches via Manage Batches App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Even most batches are automatically created during goods receipt it's also necessary to create batches manually. The DRAFT framework enables the creation of a draft instance that can be converted to an active instance at any point in time.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment. |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Batches (F2462). | The Manage Batches screen displays. |  |
| 3 | Create a Draft Version of a Master Batch Record | Choose Create in the header area. | The Batch screen displays and a new draft master batch record is created. |  |
| 4 | Maintain the Master Batch Record | Make following entries in the header data section and press Enter:Material: TG22Date of Manufacture: <Current date>Supplier Batch: <Supplier Batch Number>Country/Region of Origin: AE | The classification of the batch displays when the material field valuted.When you select enter the draft version of the master batch record is saved and the respective information displays in the bottom status bar.Depending on the configuration of the classification the characteristics can be valuated or are displayed as read-only fields. |  |
| 5 | Leave the Page | Leave the page without choosing Create.Choose Back. | The Home screen displays. |  |
| 6 | Access the App | Open Manage Batches (F2462). | The Manage Batches screen displays. |  |
| 7 | Search the Draft Master Batch Record | Make following entries:Material Number: TG22Editing Status: Own DraftChoose Go. | The list of suitable draft Master Batch Records displays. You should also find the one created in step 4. |  |
| 8 | Save the Daft Master Batch Record | Choose the line with the draft master batch record and choose Create on the Batch screen. | The draft master batch record is opened and is converted to a persistent one. If the batch number is configured to be assigned automatically, it will be populated.The batch fact sheet is shown in display mode.Make a note of the batch number ____________________. |  |

#### Optional 2: Create Batches via Create Batch App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Even most batches are automatically created during goods receipt it's also necessary to create batches manually. The DRAFT framework enables the creation of a draft instance that can be converted to an active instance at any point in time.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |
| 2 | Access the App | Open Create Batch (MSC1N). | The Create Batch screen displays. |
| 3 | Maintain the Master Batch Record | Make the following entry in the header data section and press Enter:Material: TG22 | The Automatic batch number assignment dialog box displays |
| 4A | Option 1 Maintain Batch Number Automatically | Choose OK. | The Create Batch screen displays. The batch number is created automatically. |
| 4B | Option 2 Maintain Batch Number Manually | Choose Cancel.Make the following entry in the header data section and press Enter:Batch: <Batch Number>, for example, 0000000002 |  |
| 5 | Save the Master Batch Record | Choose Save on the Create Batch screen. | The batch fact sheet is shown in display mode.Make a note of the batch number ____________________. |

### Batch Master Change

#### Option 1: Maintain Batch Master Record via Manage Batches App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Manual adjustment is needed for batch master data. The batch master is created during goods receipt.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Batches (F2462). | The Manage Batches screen displays. |  |
| 3 | Search a Batch Master Record | Restrict the search with the appropriate criteria, for example:Material Number: TG22Choose Go. | The list of suitable batch master records displays. If you don’t restrict the search, all batches are displayed. |  |
| 3 | Select a Batch Master Record | On the search result list, choose an entry created in the previous section under Batch Creation.Choose Edit on the fact sheet. | The fact sheet for the selected batch is opened and switched to change mode.A new draft version is created. |  |
| 4 | Change the Batch Master Record | On the fact sheet screen, change one or more entries or complete missing ones, for example:Date of Manufacture: Current dateSupplier Batch: Supplier Batch NumberCountry/Region of Origin: AE | If you change the date of manufacture, a pop up is opened that the Best-Before Date is recalculated. Confirm that the new best-before date should be adopted in the item. |  |
| 5 | Leave the Page | Leave the page without choosing Save.Choose Back. | The Home screen displays. |  |
| 6 | Access the SAP Fiori App | Open Manage Batches (F2462). | The Manage Batches screen displays. |  |
| 7 | Search the Draft Batch Master Record | Restrict the search with the appropriate criteria, for example:Material Number: TG22Editing Status: Own DraftChoose Go. | The list of suitable draft batch master records displays. You should also find the one created in step 4. |  |
| 8 | Save the Draft Batch Master Record | Choose the line with the draft batch master record and choose Save on the batch fact sheet.Note If the batch is changed by a different user before the draft is reopened, a warning displays. | The draft batch master record is opened and is converted to a persistent one. The changes are saved on the database.The batch fact sheet is shown in display mode. |  |

#### Option 2: Maintain Batch Master Record via Change Batch App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Manual adjustment is needed for batch master data. The batch master is created during goods receipt.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Batch (MSC2N). | The Change Batch screen displays. |  |
| 3 | Select a Batch | On the Change Batch screen, make the following entries.Material : TG22Batch: Batch Number, e.g. 0000000002Plant: 3310If the batch number is not known search via the search help in the batch number field.Choose Continue. | The batch master of batch number for material TG22 displays. |  |
| 4 | Change the Batch Master Record | On the Change Batch screen, make the following entries.Go to Basic Data 1 tab:Date of Manufacture: Current dateSupplier Batch: Supplier Batch NumberPress Enter.A pop up is opened that the Best-Before Date is recalculated. Confirm that the new best-before date should be adopted in the item.Choose Yes.Go to Basic Data 2 tab:Short Text: TEXT | The batch master record has been changed. |  |
| 5 | Add Batch to Worklist | Choose Add batch to worklist.The system have a pop-up information Batch was copied to the standard folder in the worklist.Choose Continue. | The batch has been assigned to the standard folder in the worklist for later processing. |  |
| 6 | Save Your Entries | Choose Save. | Changing batch 0000000XXX. |  |
| 7 | Display Stock Overview (Original) | Choose Menu > Environment > Current Stock .To display the Stock Overview, you need further authorizations that should be granted by your company, e.g. the SAP_BR_INVENTORY_MAN AGER. | The stock overview for the given batch displays. |  |

#### Display Change

##### Option 1: Search Batch via Launchpad Search

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When materials are sold, when they are produced or when they are on stock it is sometimes necessary to do a quick review on certain batches. The batch fact sheet displays the most recent information on a given batch and links directly to further transactions. The enterprise search capability of SAP S/4HANA Cloud Public Edition enables an easy possibility to find distinct batches.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Enterprise Search | On the Home screen, choose the Search icon and select Batches from the dropdown list. |  |  |
| 3 | Select a Batch | Enter an existing batch number for material TG22 or the material number:Batches: <Batch Number>, for example, 0000000002Press Enter. | The batch search displays possible entries for the given batch number. |  |
| 4 | Choose the Batch | Choose a batch by choosing the batch number hyperlink. | The fact sheet for the batches displays. |  |
| 5 | Analyze the Batch | Investigate the information on the fact sheet. | The fact sheet displays the header - the header section with some of information. For example: batch number, status, Shelf Life Expiration Date and material number:the general information with basic datathe classification with valuated characteristicsinspection lots with links to existing inspection lotsthe history with all documents the batch was used in |  |
| 6 | Analyze the History | Choose the table line in the History section and choose Back when finished. | The details pane of the object opens, e.g. the Sales Order detail. Go back to the fact sheet by choosing Back. |  |
| 7 | Add a Column in the History Section | Choose the Settings icon at the top of the History section, select checkbox and add columns of your interest, e.g. the sales order. Choose OK and save the settings.Choose Back when finishing this step. | An additional column displays in the history section, e.g. the sales order number enabling the user to quickly analyze the respective documents without branching into the detail screen. |  |

##### Option 2: Search Batch via Manage Batches App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Manage Batches (F2462) tile leads to a search page where a number of batches displays based on a number of selection criteria. The criteria can be personalized via the settings on the batch list page.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Batches (F2462). | The Manage Batches screen displays. |  |
| 3 | Search for Batches | Make the following entries:Editing Status: UnchangedMaterial: TG22Plant: 3310Choose Go. | A list of batches displays. |  |
| 4 | Analyze the Batch | Choose one line.Investigate the information on the fact sheet | The batch fact sheet displays.The fact sheet displays the header - the header section with batch number, status, shelf life expiration date and material name:the general information with basic datathe classification with valuated characteristicsinspection lots with links to existing inspection lotsthe history of all documents where the batch was used |  |
| 5 | Analyze the History | Choose the table line in the History section and choose Back when finished. | The detail screen of the object opens, e.g. the Sales Order detail. You can go back to the fact sheet by choosing Back. |  |
| 6 | Add a Column in the History Section | Choose the Settings icon at the top of the History section, select checkbox and add columns of your interest, e.g. the sales order. Choose OK and save the settings. | An additional column displays in the history section, e.g. the sales order number enabling the user to quickly analyze the respective documents without branching into the detail screen. |  |

### Batch Where-Used

#### Batch Information Cockpit - Batch Selection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this functionality you can search for batches according to different selection criteria, like material data, classification, best-before date, … You can adapt the selection in the Batch Information Cockpit to customer-specific requirements by creating user-specific groups. You can get additional information by using subsequent actions.

|  |
| --- |
| Note You can use each batch managed material that is delivered to a customer. If you do not have an adequate material, run test script (Make-to-Order Production – Finished Goods Sales and Final Assembly) BJE. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Batch Information Cockpit (BMBC). | The Batch Information Cockpit screen displays. |  |
| 3 | Select BatchesSelect Batches for semifinished materials | On the Batch Information Cockpit screen, make the following entries.Go to the Material tab:Material: TG22Plant: 3310Go to the Classification tab.Batch Class: YB_EXP_DATE_001OrGo to Search with Characteristics area.Selection Class: YB_EXP_DATE_001Choose Create values.Enter Characteristics value.Note Batch Class and Characteristics relevant for material please refer to [Master Data, Organizational Data, and Other Data](#unique_5) [page ] 4Choose Execute Selection. | One or multiple batches are displayed in the left screen area Selection Result for Batches. The standard sorting is done per material number. |  |
| 4 | Display Stock Information | Choose Display Selection Result for Stock. | A new screen section on the left hand panel is opened, displaying the selected batches sorted by plant and storage location. |  |
| 5 | Display Worklist | Choose Display Worklist. | A new screen section on the left hand panel is opened, displaying the batches for later processing. Also batches from previous assignments are displayed. |  |

#### Batch Information Cockpit - Change Batch Selection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this functionality, you can restart the batch selection and adapt the search by changing the general layout to predefined variants.

|  |
| --- |
| Note You can use each batch managed material that is delivered to a customer. If you do not have an adequate material, run Make-to-Order Production – Finished Goods Sales and Final Assembly (BJE) test script. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Batch Information Cockpit (BMBC). | The Batch Information Cockpit screen displays. |  |
| 3 | Select Batches | On the Batch Information Cockpit screen, make the following entries:Go to the Material tab.Material: TG22Plant: 3310Go to the Classification tab.Batch Class: YB_EXP_DATE_001OrGo to Search with Characteristics area.Selection Class: YB_EXP_DATE_001Choose Create values.Enter Characteristics value.Note For batch class and characteristics relevant materials, refer to section [Master Data, Organizational Data, and Other Data](#unique_5) [page ] 4.Choose Execute Selection. | One or multiple batches are displayed in the left screen area Selection Result for Batches. The standard sorting is done per material number. |  |
| 4 | Display Stock Information | Choose Display Selection Result for Stock. | A new screen section on the left hand panel is opened, displaying the selected batches sorted by plant and storage location. |  |
| 5 | Restart Selection | Choose Restart > SAP Standard . | The selection screen displays and all entries are cleared. The selection can be re-executed with different values. |  |
| 6 | Restart Selection with Different Variant (Optional) | Choose RestartChoose a different entry from the dropdown menu. (If there are not any other entries, this means your admin did not configure the value. In this case, you can skip this step.) | The selection screen displays a different subset of tab pages and selection fields that has been configured by the system administrator. The selection can be executed with different values. |  |

#### Batch Information Cockpit - Top-Down and Bottom-Up Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this functionality you can identify which batches are delivered to which customer and which raw material batches are used for the production of which finished product. You can adapt the selection in the Batch Information Cockpit to customer-specific requirements by creating user-specific groups. You can get additional information by using subsequent actions.

|  |
| --- |
| Note You can use each batch managed material that is delivered to a customer. If you do not have an adequate material, run Make-to-Order Production – Finished Goods Sales and Final Assembly (BJE) test script. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Batch Information Cockpit (BMBC). | The Batch Information Cockpit screen displays. |  |
| 3 | Select Batches | On the Batch Information Cockpit screen, make the following entries.Go to the Material tab.Material : TG22Plant: 3310Go to the Classification tab.Batch Class: YB_EXP_DATE_001OrGo to Search with Characteristics area.Selection Class: YB_EXP_DATE_001Choose Create values.Enter Characteristics value. e.g. <SLED/BBD from previous step>Note For batch class and characteristics relevant materials, refer to [Master Data, Organizational Data, and Other Data](#unique_5) [page ] 4.Choose Execute Selection. | One or multiple batches are displayed in the left screen area Selection Result for Batches. The standard sorting is done per material number. |  |
| 4 | Expand Selection | In the section Selection Result for Batches. Select the checkbox for TG22 and then choose Expand subtree or Expand node. | The selection result is analyzed and a batch for further investigation is identified. |  |
| 5 | Start Analysis | Right-click on one selected batch and choose either Usage(Top-Down) or Usage(Bottom-up). | The batch where-used list displays. |  |
| 6 | Analyze the Batch Where Used List | The usage of the batch can be analyzed and the specific documents (such as batch master record, sales order) can be accessed via double click. |  |  |
| 7 | Analyze Batch Master | Choose Details in the header area and select Batch Master. | The batch master screen displays. |  |
| 8 | Analyze Material Document | Choose Details again and select Usage.Select one document and choose Documents. | The usage displays again and after selecting documents the respective material document display. |  |
| 9 | Go to the Material Document | Choose the material document in the pop up dialog and choose Choose (F2).To display the material document, you need further authorizations that are granted by your company, for example, SAP_BR_INVENTORY_MANAGER. | The material document displays.Note that your user has to have the appropriate authorizations. |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/batch-derivation-consumer-products-77g-ae-1204]]
- related-to :: [[11-inventory-warehouse-and-transportation/master-data-script-create-batch-management-master-data-mds-2zw-299]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-2zw-301]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-2zw-303]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BLF_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 38,639 chars in the whole document
