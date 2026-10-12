---
id: 11-inventory-warehouse-and-transportation/mobile-rf-devices-in-warehousing-63v-ae-test-script-1144
title: Mobile RF Devices in Warehousing (63V_AE) Test Script (63V_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 63V (AE): confirm warehouse tasks and physical inventory with mobile RF devices, referencing other scope items."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-mobile-rf-devices]
aliases: [63V_S4CLD2608_BPD_EN_AE]
keywords: [Mobile RF Devices in Warehousing, mobile rf devices, warehouse task confirmation, physical inventory, resource groups, warehouse queues, verification profiles, warehouse operative role, process integration, additional manual configuration]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/63V_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1144
topic: 11-inventory-warehouse-and-transportation/ewm-mobile-rf-devices
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Mobile RF Devices in Warehousing (63V_AE) Test Script (63V_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/63V_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Mobile RF Devices in Warehousing** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Mobile RF Devices in Warehousing (63V_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232857979)

[2 Prerequisites 3](#_Toc232857980)

[2.1 System Access 3](#_Toc232857981)

[2.2 Roles 3](#_Toc232857982)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232857983)

[2.4 Additional Manual Configuration 4](#_Toc232857984)

[2.5 Business Conditions 4](#_Toc232857985)

[2.6 Preliminary Steps 5](#_Toc232857986)

[3 Overview Table 6](#_Toc232857987)

[4 Test Procedures 7](#_Toc232857988)

[4.1 Confirm Warehouse Task in RF Environment 7](#_Toc232857989)

[4.2 Physical Inventory in RF Environment 7](#_Toc232857990)

[5 Appendix 8](#_Toc232857991)

[5.1 Process Integration 8](#_Toc232857992)

[5.1.1 Preceding Processes 8](#_Toc232857993)

## Purpose

Overview

This scope item allows you to use mobile RF devices in warehouse processes. There's a set of out-of-the-box transactions available to perform mobile warehouse activities in inbound, internal, and outbound processes such as put away, physical inventory counting and picking. This process activates the necessary configuration to determine queues during warehouse task creation. Based on these queues, the workload can be distributed to multiple resources working in the warehouse. Once you set up the relevant master data, you can assign resource groups to resources and thus control the activity areas of a warehouse where a resource is active. Resource planners can choose to have the system guide them, or manually choose their next warehouse order. Using verification profiles, you can define which verification fields are mandatory and which can be skipped during the scanning process.

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

### Master Data, Organizational Data, and Other Data

The following master data needs to be maintained to support working with RF devices:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Presentation Devices | SE01 | Portrait Mode |  |
| Resource Group | SALLSCNTSHA1SHR1 | Access to all QueuesPhysical InventoryStandard Storage OperationgAll Except Standard Storage Operating |  |
| Queue Sequence for Resource Group | SI-001SO-001And etc. |  | For the detailed list of Queue Sequences for Resource Groups, refer to the Set-up Instruction guide mentioned below this table. |
| Resource | SALL-1SCNT-1SHA1-1SHR1-1 | Access to all QueuesPhysical InventoryStandard Storage OperatingAll Except Standard Storage Operating |  |

For the detailed steps of how to create the master data for RF enablement, refer to the chapter Configuration with SAP Central Business Configuration > Starter System with Sample Master Data > Maintain Master Data in the respective Set-up Instruction Guide Setting Up Mobile RF Devices in Warehousing (63V).

For other Master Data and Organizational Data , see in the corresponding chapter in the referenced test scripts.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/ad27f6503263c30b71125c03596bc081)

Before you start the testing, please make sure that the steps in the [https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_588%20Warehouse%20Management%20Setup.docx](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_588%20Warehouse%20Management%20Setup.docx) (Public) published on SAP Activate Roadmap Viewer are completed.

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 3BR - Warehouse Inbound Processing | To confirm Warehouse Tasks using the RF-Environment, perform all steps until you reach step in 3BR - Warehouse Inbound Processing test script. Follow the procedure described in section Variant 2: With Radio Frequency Devices. |

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
| [Physical Inventory in RF Environment](#unique_11) [page ] 7 | Warehouse Operative (EWM) | Test RF Environment (/SCWM/RFUI) |  |

## Test Procedures

### Confirm Warehouse Task in RF Environment

To confirm warehouse tasks in the RF Environment, follow the steps described in the test script associated with the scope item you are testing.

Go to Test Procedures > Confirm Warehouse Task in the following scope items:

- Warehouse Inbound Processing (3BR)

You can find the document here: [3BR](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/latest/SolP/3BR?region=DE)

- Warehouse Inbound Processing with Synchronous Goods Receipt (5HN)

You can find the document here: [5HN](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/latest/SolP/5HN?region=DE)

- Warehouse Outbound Processing (3BS)

You can find the document here: [3BS](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/latest/SolP/3BS?region=DE)

- Warehouse Ad Hoc Goods Issue (3BT)

You can find the document here: [3BT](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/latest/SolP/3BT?region=DE)

Go to Test Procedures > Confirm Warehouse Task for Posting Changes in the following scope items:

Warehouse Posting Changes (3BU).

You can find the document here: [3BU](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/latest/SolP/3BU?region=DE)

Go to Test Procedures > Confirm Replenishment Warehouse Tasks in the following scope items:

Replenishment in Warehousing (4A2)

You can find the document here: [4A2](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/latest/SolP/4A2?region=DE)

### Physical Inventory in RF Environment

The Warehouse Operative (EWM) creates the ad-hoc physical inventory document for inventory counting with a mobile Radio Frequency device.

Go to Test Procedures > Variant 3: Create Counting Document with Radio Frequency in the following scope items:

Warehouse Physical Inventory (3BX).

The Warehouse Operative (EWM) enters the count result via mobile Radio Frequency device.

Go to Test Procedures > Enter Count Result > Variant 2: With Radio Frequency Device in the following scope items:

Warehouse Physical Inventory (3BX).

You can find the document here: [3BX](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/latest/SolP/3BX?region=DE).

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

You may first have completed the following processes and conditions before you start with the test steps.

| Scope Item ID | Business Condition |
| --- | --- |
| 3BR - Warehouse Inbound Processing | To confirm Warehouse Tasks using the RF-Environment, perform all steps until you reach step Confirm Warehouse Tasks in 3BR - Warehouse Inbound Processing test script. Follow the procedure described in section Variant 2: With Radio Frequency Devices. |
| 5HN - Warehouse Inbound Processing with Synchronous Goods Receipt | To confirm Warehouse Tasks using the RF-Environment, perform all steps until you reach step Confirm Warehouse Tasks in 5HN - Warehouse Inbound Processing with Synchronous Goods Receipt test script. Follow the procedure described in section Variant 2: With Radio Frequency Devices. |
| 3BS - Warehouse Outbound Processing | To confirm Warehouse Tasks using the RF-Environment, perform all steps until you reach step Confirm Pick Warehouse Tasks in 3BS - Warehouse Outbound Processing test script. Follow the procedure described in section Variant 2: With Radio Frequency Devices. |
| 3BT - Warehouse Ad Hoc Goods Issue | To confirm Warehouse Tasks using the RF-Environment, perform all steps until you reach step Confirm Warehouse Tasks in 3BT - Warehouse Ad Hoc Goods Issue test script. Follow the procedure described in section Variant 2: With Radio Frequency Devices. |
| 3BU - Warehouse Posting Changes | To confirm Warehouse Tasks using the RF-Environment, perform all steps until you reach step Confirm Warehouse Task for Posting Changes in 3BU - Warehouse Posting Changes test script. Follow the procedure described in section Variant 2: With Radio Frequency Devices. |
| 3BX - Warehouse Physical Inventory | To create counting document using RF-Environment, perform all preliminary steps in 3BX - Warehouse Physical Inventory test script. Follow the procedure described in section Variant 3: Create Counting Document with Radio Frequency.To enter count result using RF-Environment, perform all steps until you reach step Enter Count Result in 3BX - Warehouse Physical Inventory test script. Follow the procedure described in section Variant 2: With Radio Frequency Devices. |
| 4A2 - Replenishment in Warehousing | To confirm Warehouse Tasks using the RF-Environment, perform all steps until you reach step Confirm Replenishment Warehouse Tasks in 4A2 - Replenishment in Warehousing test script. Follow the procedure described in section Variant 2: With Radio Frequency Devices. |

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
- related-to :: [[11-inventory-warehouse-and-transportation/mobile-rf-devices-in-warehousing-with-production-integration-63w-ae-te]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-mobile-rf-devices-in-warehousing-with-quality-management-6]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/63V_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 14,727 chars in the whole document
