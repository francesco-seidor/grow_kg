---
id: 13-quality-ehs-and-compliance/quality-management-in-stock-handling-1mr-ae-test-script-739
title: Quality Management in Stock Handling (1MR_AE) - Test Script (1MR_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1MR_AE: posting stock to quality inspection, usage decisions, and storage location changes."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/quality-in-stock-handling]
aliases: [1MR_S4CLD2608_BPD_EN_AE]
keywords: [Quality Management in Stock Handling, quality inspection stock, usage decisions, storage location change, inspection lots, test scripts, business roles, master data, inspection type setup, raw material stock]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1MR_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-739
topic: 13-quality-ehs-and-compliance/quality-in-stock-handling
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Quality Management in Stock Handling (1MR_AE) - Test Script (1MR_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1MR_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Quality Management in Stock Handling** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Quality Management in Stock Handling (1MR_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232847323)

[2 Prerequisites 4](#_Toc232847324)

[2.1 System Access 4](#_Toc232847325)

[2.2 Roles 4](#_Toc232847326)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232847327)

[2.4 Business Conditions 5](#_Toc232847328)

[2.5 Preliminary Steps 6](#_Toc232847329)

[2.5.1 Create Raw Material Stock 6](#_Toc232847330)

[2.5.2 Define Inspection Type for Available Stock in Quality Inspection 7](#_Toc232847331)

[3 Overview Table 8](#_Toc232847332)

[4 Test Procedures 9](#_Toc232847333)

[4.1 Posting Unrestricted or Blocked Stock into Quality Inspection Stock 9](#_Toc232847334)

[4.1.1 Display Material Stock Before Goods Posting (Optional) 9](#_Toc232847335)

[4.1.2 Post Material from Unrestricted/Blocked Stock to Quality Inspection Stock 10](#_Toc232847336)

[4.1.3 Display Material Stock Before Quality Inspection (Optional) 11](#_Toc232847337)

[4.1.4 Quality Inspection: Make Usage Decision 11](#_Toc232847338)

[4.1.5 Display Material Stock After Quality Inspection (Optional) 13](#_Toc232847339)

[4.2 Posting Quality Inspection Stock to Different Storage Location 14](#_Toc232847340)

[4.2.1 Use Existing Inspection Lot (Or Create a New) 14](#_Toc232847341)

[4.2.2 Display Quality Inspection Stock Before Change of Storage Location (Optional) 14](#_Toc232847342)

[4.2.3 Change Storage Location for Quality Stock with Reference to Inspection Lot 15](#_Toc232847343)

[4.2.4 Display Quality Inspection Stock After Change of Storage Location (Optional) 16](#_Toc232847344)

## Purpose

Overview

This scope item manages quality inspection activities in stock handling processes. Quality inspection activities may be relevant for materials during the storage of goods.

During the storage of goods, a warehouse clerk may identify damage that must be checked and investigated. To follow up, the material is posted to quality inspection stock and an inspection lot is created automatically. The quality engineer inspects the material and makes a usage decision that triggers the posting of the material, for example, to unrestricted stock, to blocked stock, or to scrap. Additionally, the quality inspection stock may be moved from one storage location to another, for example, if a specific check can only be done at one location in the plant where the equipment is available.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

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
| Quality Technician | SAP_BR_QUALITY_TECHNICIAN | Quality Inspection | SAP_BR_QUALITY_TECHNICIAN |  |
| Quality Engineer | SAP_BR_QUALITY_ENGINEER | Quality Engineering | SAP_BR_QUALITY_ENGINEER |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | QM001 | QM RegularTrading Good for Regular Procurement (PD planning) |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BMC - Core Inventory Management | Complete all steps in the test script. |
| BNY - Create Quality Management Attributes for Material/Product Master - MDS | Complete all steps in the master data script for inspection type 08. |

### Preliminary Steps

#### Create Raw Material Stock

To run through this scope item, the materials must be available in stock. Stock can be available after a goods receipt of a purchasing process. In this case you do not need this preliminary step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Inventory Manager。 | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Input Material | Make the following entries and Choose Enter:Plant: 3310Material: QM001 | The Stock Overview for the material displays. |  |
| 4 | Select Stock | Select the icon beside the stock that you want to add initial stock, for example:Storage Location: 331AUnrestricted-Use Stock | A dialog box opens. The Storage Location, Stock Type, and Current Quantity display according to your entries in the previous steps. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Document Date: Enter today's datePosting Date: Enter today's dateStock Change: Initial EntryQuantity: Enter a number, for example 10 | The system displays Material document XXX created. The stock has been added. |  |

|  |
| --- |
| Note Serial number is enabled. You can plan and perform inspections for serialized materials in the Quality Management component. As a prerequisites, a serial number profile with the procedure QMSL must be entered in the material master record and the indicator for serial number management must be set in the inspection setup in the material master record. During inspection lot processing, you can:Enter results for original values with reference to serial numbers.Make a usage decision and perform inventory postings with reference to serial numbers. |

#### Define Inspection Type for Available Stock in Quality Inspection

You may want to activate a stock-relevant inspection type for a material for which there is stock in quality inspection that is not managed by inspection lots. For this case, you must define an inspection type via one of the following options:

Manage Your Solution:

In the SAP S/4HANA Cloud Public Edition system, in the SAP Fiori launchpad, open the Manage Your Solution (F1241) app and go to Configure Your Solution. From Application Area, choose Quality Management, and from Sub Application Area, choose Basic Settings.

In the configuration step Maintain Settings at Plant Level, you must define an inspection type in the detail view. Double click the plant and go to the tab Insp. Lot Creation, maintain inspection type 0800 in the field InspTypeForInspStock.

SAP Central Business Configuration:

Log on to the project experience in SAP Central Business Configuration. Go to the Business Processes Configuration app and search for the following configuration activity: Maintain Settings at Plant Level.

Choose the Go to Activity button to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. In this configuration activity, you must define inspection type 0800 in the field InspTypeForInspStock for the plant.

Later when activating the inspection type using the app Change QM Inspection Setup - Collective Processing (QA08), inspection lots are created in the background that manage the already available inspection stock. The parameters to control inspection lot processing are copied from the default values of the inspection type entered here.

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | TransactionApp | Expected Results |
| --- | --- | --- | --- |
| [Display Material Stock Before Goods Posting (Optional)](#unique_10) [page ] 9 | Warehouse Clerk | Stock - Single Material (F1076) |  |
| [Post Material from Unrestricted/Blocked Stock to Quality Inspection Stock](#unique_11) [page ] 10 | Warehouse Clerk | Transfer Stock - In-Plant (F1061) | An inspection lot is created |
| [Display Material Stock Before Quality Inspection (Optional)](#unique_12) [page ] 11 | Warehouse Clerk | Stock - Single Material (F1076) |  |
| [Quality Inspection: Make Usage Decision](#unique_13) [page ] 11 | Quality Engineer | Manage Usage Decisions (F2345) | A goods movement is posted automatically according to the usage decision made |
| [Display Material Stock After Quality Inspection (Optional)](#unique_14) [page ] 13 | Warehouse Clerk | Stock - Single Material (F1076) |  |

Posting Quality Inspection Stock to Different Storage Location

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Use Existing Inspection Lot (Or Create a New)](#unique_15) [page ] 14 | Warehouse Clerk | Transfer Stock - In-Plant (F1061) | An inspection lot is created |
| [Display Quality Inspection Stock Before Change of Storage Location (Optional)](#unique_16) [page ] 14 | Warehouse Clerk | Stock - Single Material (F1076) |  |
| [Change Storage Location for Quality Stock with Reference to Inspection Lot](#unique_17) [page ] 15 | Quality Technician | Manage Inspection Lots (F2343) | The storage location is changed |
| [Display Quality Inspection Stock After Change of Storage Location (Optional)](#unique_18) [page ] 16 | Warehouse Clerk | Stock - Single Material (F1076) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Posting Unrestricted or Blocked Stock into Quality Inspection Stock

#### Display Material Stock Before Goods Posting (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Stock - Single Material (F1076). | The Stock - Single Material (F1076) screen displays. |  |
| 3 | Enter Material | Make the following entries and press Enter.Material: QM001 | Stock for the material is displayed. |  |
| 4 | Check Stock Quantity | Check the Quality Inspection Stock for plant 3310. |  |  |

#### Post Material from Unrestricted/Blocked Stock to Quality Inspection Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Transfer Stock - In-Plant (F1061) | The Transfer Stock - In-Plant (F1061) screen displays. |  |
| 3 | Open Stock Overview | Enter the following data:Plant 1 AE: (3310 )Material: QM001 |  |  |
| 4 | Select Transfer from Stock | In the column Blocked Stock or Unrestricted - Use Stock, select the icon next to the stock you want to transfer from. | The icon changes. |  |
| 5 | Select Transfer to Stock | In the column Stock in Quality Inspection, select the icon next to the stock you want to transfer to. | A dialog box opens. Storage Locations and Stock Types are selected according to your entries in the previous steps. |  |
| 6 | Transfer Stock | Enter the quantity you want to transfer.Choose Post. | The system displays a message Material document xxx created.The goods stock status is switched from Blocked or Unrestricted-Use to Quality Inspection Stock.An inspection lot is created.Remember the document number for the next steps. |  |

#### Display Material Stock Before Quality Inspection (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, you verify the stock transfer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material (F1076) screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and press Enter.Material: QM001 |  |  |
| 4 | Check Stock Quantity | Check the changed quantities of the Quality Inspection Stock. |  |  |

#### Quality Inspection: Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the quality engineer decides if the material shall be transferred to free or blocked stock or scraped.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Manage Usage Decisions (F2345). | The Manage Usage Decisions (F2345) screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Material Document: obtained from previous step | If Material Document is not displayed in the Filters, choose Adapt Filters. On the pop-up screen Adapt Filters, find Inventory Management and choose More Filters. Select Material Document and choose OK. Choose Go. |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, click the inspection lot. |  |  |
| 5 | Display Defects (Optional) | Scroll down to the Defects area. Check the details of Defects. | Only available you have recorded a Negative result. For a surface rejection, there will be a surface defect. For a length rejection, there will be a tolerance defect displayed. |  |
| 6 | Enable Edit Instruction | Choose Edit. |  |  |
| 7 | Enter UD Code | Depending on the inspection result, select one of the following two options via search help and then confirm with ChoosePositive ResultUD code: UD08 A1 (Accepted – unrestricted stock)Negative ResultUD code: UD08R1 (Rejected – blocked stock)R310 Rejected-scrap (partial quan-tity)R320 Rejected – scrap (complete quantity)(info)Cost Center 33101201 (was automatically determined) | The corresponding stock posting is processed automatically in background for the complete quantity for Usage Decision codes A1, R1, and R320. |  |
| 8 | Modify Stock Posting (Optional) | In the Inspection Lot Stock section, enter the quantities to be posted to different stock types. | Note If you want to scrap a partial quant with UD code R310, you can split the quantity and post to To Unrestricted Use and To Scrap, respectively. It is also possible to transfer the (partial or full) quant to a different material if, for example, the product is of higher/lower quality and the higher/lower quality corresponds to different material. |  |
| 9 | Save Usage Decision | Choose Save. | The system automatically triggers the material movements íf associated with the usage decision code.Positive Result: A goods movement is posted automatically from quality inspection stock to unrestricted use stock.Negative Result: A goods movement is posted automatically from quality inspection stock to blocked stock or scraped. |  |

#### Display Material Stock After Quality Inspection (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, you now verify the material movement done based on the usage decision codes by looking again at the material stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Stock - Single Material (F1076) | The Stock - Single Material (F1076) screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and press Enter.Material: QM001 |  |  |
| 4 | Check Stock Quantity | Check the changed quantities of the Quality Inspection Stock. | The stock quantities for material QM001 are updated based on the quality inspection and respective usage decision of the previous steps. |  |

### Posting Quality Inspection Stock to Different Storage Location

#### Use Existing Inspection Lot (Or Create a New)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

Follow the process steps as described in chapter Post Material from Unrestricted or Blocked Stock into Quality Inspection Stock.

|  |
| --- |
| Note The inspection lot can be created through QM in procurement, QM in manufacturing. Note that, as this procedure describes a stock posting in quality inspection stock from one storage location to another, the final stock posting via usage decision must not have occoured. |

#### Display Quality Inspection Stock Before Change of Storage Location (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Stock - Single Material (F1076). | The Stock - Single Material (F1076) screen displays. |  |
| 3 | Enter Material | Make the following entries and press Enter.Material: QM001 | Stock for the material is displayed. |  |
| 4 | Check Stock Quantity | Check the Quality Inspection Stock for Plant3310 with regards to the storage locations 331A and 331B |  |  |

#### Change Storage Location for Quality Stock with Reference to Inspection Lot

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots (F2343) screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go:Material Document： Obtained from previous stepOr Inspection Lot: Obtained from QM in procurement or QM in manufacturingNote If Material Document is not displayed in the Filters, choose Adapt Filters. On the pop-up dialog Adapt Filters, select Material Document and choose OK. | A list of inspection lots displays. |  |
| 4 | Select Inspection Lot | In the Inspection Lot column of the inspection lots list, click on the link of the inspection lot number created from the previous step. A list of smart links displays on the context menu.Choose Transfer Inspection Stock. | The Transfer Inspection Lot Quantities screen displays. |  |
| 5 | Change Storage Location | On the tab Stock Transfer, in section Stock Transfer Based On make the following entries:StLoc.ILotStock: 331B |  |  |
| 6 | Save Data | Choose Save. | The Storage Location is changed. |  |

#### Display Quality Inspection Stock After Change of Storage Location (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Stock - Single Material (F1076). | The Stock - Single Material screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Material: QM001 | Stock for the material is displayed. |  |
| 4 | Check Stock Quantity | Check the Quality Inspection Stock for plant 3310 with regard to the storage locations 331A and 331B. | The stock quantities for material QM001 are updated for the different storage locations. |  |

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
- see-also :: [[11-inventory-warehouse-and-transportation/test-script-warehouse-internal-inspections-5ok-ae-sap-s-4hana-cloud-pu]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1MR_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 28,286 chars in the whole document
