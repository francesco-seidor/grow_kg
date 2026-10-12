---
id: 11-inventory-warehouse-and-transportation/test-script-mobile-rf-devices-in-warehousing-with-quality-management-6
title: "Test Script: Mobile RF Devices in Warehousing with Quality Management (63X_AE) (63X_S4CLD2608_BPD_EN_AE)"
description: "Test script for scope item 63X (AE) on SAP S/4HANA Cloud Public Edition 2608: confirming warehouse tasks and creating inspection lots on mobile RF devices in EWM."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-mobile-rf-devices]
aliases: [63X_S4CLD2608_BPD_EN_AE]
keywords: [Mobile RF Devices in Warehousing, mobile rf devices, warehouse task confirmation, inspection lot, warehouse quality management, resource groups, warehouse queues, business roles, process integration, test scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/63X_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1146
topic: 11-inventory-warehouse-and-transportation/ewm-mobile-rf-devices
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Mobile RF Devices in Warehousing with Quality Management (63X_AE) (63X_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/63X_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Mobile RF Devices in Warehousing** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Mobile RF Devices in Warehousing with Quality Management (63X_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232858042)

[2 Prerequisites 3](#_Toc232858043)

[2.1 System Access 3](#_Toc232858044)

[2.2 Roles 3](#_Toc232858045)

[2.3 Master Data, Organization Data, and Other Data 3](#_Toc232858046)

[2.4 Additional Manual Configuration 4](#_Toc232858047)

[2.5 Business Conditions 4](#_Toc232858048)

[2.6 Preliminary Steps 5](#_Toc232858049)

[3 Overview Table 6](#_Toc232858050)

[4 Test Procedures 7](#_Toc232858051)

[4.1 Confirm Warehouse Task in RF Environment 7](#_Toc232858052)

[4.2 Create Inspection Lot with the Mobile RF Device 9](#_Toc232858053)

[5 Appendix 11](#_Toc232858054)

[5.1 Process Integration 11](#_Toc232858055)

[5.1.1 Preceding Processes 11](#_Toc232858056)

[5.1.2 Succeeding Processes 11](#_Toc232858057)

## Purpose

Overview

This scope item allows you to use mobile RF devices in warehouse processes with quality management. There's a set of out-of-the-box transactions available to perform different mobile warehouse activities, such as creating a product inspection. This process activates the necessary configuration to determine queues during warehouse task creation. Based on these queues, the workload can be distributed to multiple resources working in the warehouse. By setting up the relevant master data, resource groups can be assigned to resources and thus control the warehouse activity areas where a resource is active. Resource planners can choose to have the system guide them, or manually choose their next warehouse order. Using verification profiles, you can define which verification fields are mandatory and which can be skipped during the scanning process.

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
| Warehouse Operative (EWM) | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Warehouse Floor | SAP_BR_WAREHOUSE_OPERATIVE_EWM |  |

### Master Data, Organization Data, and Other Data

The following master data needs to be maintained to support working with RF Devices:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Presentation Devices | SE01 | Portrait Mode |  |
| Resource Group | SALLSHA1SHR1 | Access to all QueuesStandard Storage OperatingAll Except Standard Storage Operating |  |
| Queue Sequence for Resource Group | SI-001SI-820SI-970SI-001-820SS-820SS-970 |  | For the detailed list of Queue Sequences for Resource Groups, please refer to the Set-up Instruction guide mentioned below this table |
| Resource | SALL-1SHA1-1SHR1-1 | Access to all QueuesStandard Storage OperatingAll Except Standard Storage Operating |  |

For the detailed steps of how to create the master data for RF enablement, refer to the chapter Configuration with SAP Central Business Configuration > Starter System with Sample Master Data > Maintain Master Data in the respective Set-up Instruction Guide Setting Up Mobile RF Devices in Warehousing (63X).

For other Master Data and Organization Data , see the corresponding chapter in the referenced test scripts.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/ae167716e1c4d285f608c211dd2d0cab)

Before you start the testing, please make sure that the steps in the [Warehouse Management Setup Guide.docx (Public)](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_588%20Warehouse%20Management%20Setup.docx) published on SAP Activate Roadmap Viewer have been completed.

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 3M0 – Quality Management in Warehousing | To confirm Warehouse Tasks using the RF-Environment, perform all steps in 3M0 – Quality Management in Warehousing test script until you reach step Confirm Warehouse Tasks. Follow the procedure described in section Variant 2: With Radio Frequency Devices. |
| 3BR - Warehouse Inbound Processing | You have completed the step described in Warehouse Inbound Processing test script so that you have the stock to do the posting changes. |

### Preliminary Steps

See the preliminary steps in the referenced test scripts.

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

This scope item consists of several process steps provided in the table below.

| Process Step | Business Role | App / Transaction | Expected Results |
| --- | --- | --- | --- |
| [Confirm Warehouse Task in RF Environment](#unique_10) [page ] 7 | Warehouse Operative (EWM) | Test RF Environment (/SCWM/RFUI) |  |
| [Create Inspection Lot with the Mobile RF Device](#unique_11) [page ] 9 | Warehouse Operative (EWM) | Test RF Environment (/SCWM/RFUI) |  |

## Test Procedures

### Confirm Warehouse Task in RF Environment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) performs the warehouse tasks and confirm warehouse tasks in the RF environment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the SAP Fiori app Test RF Environment (/SCWM/RFUI)Note The app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP Note [3048632](https://me.sap.com/notes/3048632). |  |  |
| 3 | Enter Data for RFUI | Whse No: 3350Resource: SHA1-1 or SHR1-1Dflt Dvc.: SE01Choose Enter.Note Use resource SHA1-1 for putting away to S001.Use SHR1-1 for putting away to storage types other than S001. |  |  |
| 4 | Choose Menu | Choose 01 System-Guided > 02 SystemGuided Queue. |  |  |
| 5 | Enter Queue Name | In the Queue field, enter SI-001, SI-F01,SI-B01,SI-G01 or SI-970 |  |  |
| 6 | Verify Source Bin and Enter HU | Note This step is only relevant, if you create handling unit for a goods receipt.Verify the Src.Bin (Source Bin)HU: < Enter the HU ID from step Create Handling Unit (Optional)> |  |  |
| 7 | Verify the Source Information Fields | Verify the following fields, if they are required:Src.Bin (Source Bin)Prod. (Product)Srce Qty (Source Quantity)ChooseEnter . |  |  |
| 8 | Verify the Destination Information Fields | Verify the following fields, if they are required:Prod. (Product)ActQty (Quantity)Dest.Qty (Destination Quantity)DstBin (Destination Bin)ChooseEnter. |  |  |
| 9 | Repeat Steps | Repeat steps 6 to 8 until no suitable warehouse orders are found. |  | All putaway warehouse tasks have been confirmed. |
| 10 | Logoff RFUI | You can choose Back to go to the previous screens.Choose Logoff.Choose Save.Note If you have the two availability groups setup for your warehouse, as soon as the putaway warehouse tasks are confirmed, the system automatically posts the stock type for this stock from Unrestricted Use in Putaway (F0) to Unrestricted Use in Warehouse (F). |  |  |

### Create Inspection Lot with the Mobile RF Device

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) performs the warehouse tasks and confirms them in the RF environment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the SAP Fiori app Test RF Environment (/SCWM/RFUI)Note The app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP Note [3048632](https://me.sap.com/notes/3048632). |  |  |
| 3 | Enter Data for RFUI | Whse No: 3350Resource: SHA1-1 or SHR1-1DefPresDvc: SE01Choose Enter.Note Use resource SHA1-1 for putting away to S001.Use SHR1-1 for putting away to storage types other than S001. |  |  |
| 4 | Choose Menu | Choose 01 System-Guided > 02 SystemGuided Queue. |  |  |
| 5 | Enter Queue Name | In the Queue field, enter SI-001, SI-F01,SI-B01,SI-G01 or SI-970 |  |  |
| 6 | Verify Source Bin and Enter HU | Note This step is only relevant, if you create handling unit for a goods receipt.Verify the Src.Bin (Source Bin)HU: < Enter the HU ID from step Create Handling Unit (Optional)> |  |  |
| 7 | Verify the Source Information Fields | Verify the following fields, if they are required:Src.Bin (Source Bin)Prod. (Product)Srce Qty (Source Quantity)ChooseEnter . |  |  |
| 8 | Verify the Destination Information Fields | Verify the following fields, if they are required:Prod. (Product)ActQty (Quantity)Dest.Qty (Destination Quantity)DstBin (Destination Bin)ChooseEnter. |  |  |
| 9 | Repeat Steps | Repeat steps 6 to 8 until no suitable warehouse orders are found. |  |  |
| 10 | Logoff RFUI | You can choose Back to got to the previous screens.Choose Logoff.Choose Save. |  |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

You may first have completed the following processes and conditions before you start with the test steps.

| Scope Item ID | Business Condition |
| --- | --- |
| 3M0 – Quality Management in Warehousing | To confirm Warehouse Tasks using the RF-Environment, perform all steps in 3M0 – Quality Management in Warehousing test script until you reach step Confirm Warehouse Tasks. Follow the procedure described in section Variant 2: With Radio Frequency Devices. |
| 5OK – Warehouse Internal Inspections | To Create Inspection Lot with the Mobile RF Device, perform all steps in 5OK – Warehouse Internal Inspections test script until you reach step Create Inspection Lot. Follow the procedure described in section Alternative 2 – Create Inspection Lot with the Mobile RF Device.To confirm Warehouse Tasks using the RF-Environment, perform all steps in 5OK – Warehouse Internal Inspections test script until you reach step Confirm Warehouse Tasks. Follow the procedure described in section Variant 2: With Radio Frequency Devices. |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the business processes mentioned in the Preceding Processes chapter.

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
- related-to :: [[11-inventory-warehouse-and-transportation/mobile-rf-devices-in-warehousing-63v-ae-test-script-1144]]
- related-to :: [[11-inventory-warehouse-and-transportation/mobile-rf-devices-in-warehousing-with-production-integration-63w-ae-te]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/63X_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 16,241 chars in the whole document
