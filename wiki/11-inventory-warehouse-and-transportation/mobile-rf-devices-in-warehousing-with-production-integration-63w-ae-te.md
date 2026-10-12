---
id: 11-inventory-warehouse-and-transportation/mobile-rf-devices-in-warehousing-with-production-integration-63w-ae-te
title: Mobile RF Devices in Warehousing with Production Integration (63W_AE) - Test Script (63W_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 63W: confirming staging and putaway warehouse tasks via mobile RF devices with production integration."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-mobile-rf-devices]
aliases: [63W_S4CLD2608_BPD_EN_AE]
keywords: [Mobile RF Devices in Warehousing, mobile rf devices, warehouse tasks, staging warehouse tasks, putaway warehouse tasks, production integration, test scripts, business roles, resource groups, business conditions]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/63W_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1145
topic: 11-inventory-warehouse-and-transportation/ewm-mobile-rf-devices
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Mobile RF Devices in Warehousing with Production Integration (63W_AE) - Test Script (63W_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/63W_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Mobile RF Devices in Warehousing** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Mobile RF Devices in Warehousing with Production Integration (63W_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232857390)

[2 Prerequisites 3](#_Toc232857391)

[2.1 System Access 3](#_Toc232857392)

[2.2 Roles 3](#_Toc232857393)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232857394)

[2.4 Additional Manual Configuration 4](#_Toc232857395)

[2.5 Business Conditions 4](#_Toc232857396)

[2.6 Preliminary Steps 5](#_Toc232857397)

[3 Overview Table 6](#_Toc232857398)

[4 Test Procedures 7](#_Toc232857399)

[4.1 Confirm Staging Warehouse Tasks in RF Environment 7](#_Toc232857400)

[4.2 Confirm Putaway Warehouse Tasks in RF Environment 7](#_Toc232857401)

[5 Appendix 9](#_Toc232857402)

[5.1 Process Integration 9](#_Toc232857403)

[5.1.1 Preceding Processes 9](#_Toc232857404)

[5.1.2 Succeeding Processes 9](#_Toc232857405)

## Purpose

Overview

This scope item allows you to use mobile RF devices in warehouse processes with production integration. There's a set of out-of-the-box transactions available to perform different mobile warehouse activities such as staging. This process activates the necessary configuration to determine queues during warehouse task creation. Based on these queues, the workload can be distributed to multiple resources working in the warehouse. Once you set up the relevant master data, you can assign resource groups to resources and thus control the activity areas of a warehouse where a resource is active. Resource planners can choose to work system guided or manually choose their next warehouse order. Via verification profiles, you can define which verification fields are mandatory and which can be skipped during the scanning process.

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

The following master data need to be maintained to support RF Framework:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Presentation Devices | SE01 | Portrait Mode |  |
| Resource Group | SALLSCNTSHA1SHR1 | Access to all QueuesPhysical InventoryStandard Storage OperatingAll Except Standard Storage Operating |  |
| Queue Sequence for Resource Group | SI-001SO-001 And so on. |  | For the detailed list of Queue Sequences for Resource Groups, refer to the set-up instruction guide mentioned below this table. |
| Resource | SALL-1SCNT-1SHA1-1SHR1-1 | Access to all QueuesPhysical InventoryStandard Storage OperatingAll Except Standard Storage Operating |  |

For the detailed steps, refer to the same name chapter under the chapter

Configuration with SAP Central Business Configuration > Starter System with Sample Master Data > Maintain Master Data

In the Set-up Instruction guide for scope item 63W - Mobile RF Devices in Warehousing with Production Integration

For other Master Data, Organization Data , see in the corresponding chatper in the reference test scripts.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/32edde562596a40d81df8248d65ad5de)

Before you start the testing, please make sure that the steps in the [Warehouse Management Setup Guide.docx (Public)](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_588%20Warehouse%20Management%20Setup.docx) published on SAP Activate Roadmap Viewer have been completed.

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 3DV - Warehouse Production Integration | To confirm warehouse tasks using the RF environment, perform all steps until you reach step Confirm Staging Warehouse Tasks or step Confirm Putaway Warehouse Tasks in the 3DV- Warehouse Production Integration test script. Follow the procedure described in section Variant 2: With Radio Frequency Device. |
| 5HO – Warehouse Production Integration with Synchronous Goods Receipt | To confirm warehouse tasks using the RF environment, perform all steps until you reach step Confirm Staging Warehouse Task or step Confirm Putaway Warehouse Tasks in the 5HO – Warehouse Production Integration with Synchronous Goods Receipt test script. Follow the procedure described in section Variant 2: With Radio Frequency Device. |
| 3VT – Warehouse Kanban Supply into Production | To confirm warehouse tasks using the RF environment, perform all steps until you reach step in the 3VT – Warehouse Kanban Supply into Production test script. Follow the procedure described in section . |
| 41U – Warehouse Goods Receipt from Repetitive Manufacturing | To confirm warehouse tasks using the RF environment, perform all steps until you reach step in the 41U – Warehouse Goods Receipt from Repetitive Manufacturing test script. Follow the procedure described in section . |
| 6NI – Warehouse Advanced Production Integration | To confirm warehouse tasks using the RF environment, perform all steps until you reach step , or in the 6NI – Warehouse Advanced Production Integration test script. Follow the procedure described in section . |
| 3BR - Warehouse Inbound Processing | You have completed the step described in Warehouse Inbound Processing test script so that you have the stock to do the posting changes. |

### Preliminary Steps

See Preliminary Steps in the reference test scripts.

## Overview Table

This scope item consists of several process steps provided in the table below.

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage only contains the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the homepage using the search bar.

If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder.

| Process Step | Business Role | App / Transaction | Expected Results |
| --- | --- | --- | --- |
| [Confirm Staging Warehouse Tasks in RF Environment](#unique_10) [page ] 7 | Warehouse Operative (EWM) | Test RF Environment (/SCWM/RFUI) |  |
| [Confirm Putaway Warehouse Tasks in RF Environment](#unique_11) [page ] 7 | Warehouse Operative (EWM) | Test RF Environment (/SCWM/RFUI) |  |

## Test Procedures

### Confirm Staging Warehouse Tasks in RF Environment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

To confirm staging warehouse tasks in the RF Environment, follow the steps described in the test script associated with the scope item you are testing.

Go to TestProcedures > Material Staging for Production > Confirm Staging Warehouse Task > Variant 2: With Radio Frequency Devices in the Warehouse Production Integration (3DV) and Warehouse Production Integration with Synchronous Goods Receipt (5HO) test scripts.

You can find the documents here:

[3DV](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/latest/SolP/3DV?region=DE)

[5HO](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/latest/SolP/5HO?region=DE)

Go to TestProcedures > Option 1: Status Control in Warehouse > Confirm Warehouse Task > Variant 2: With Radio Frequency Devices in the Warehouse Kanban Supply into Production (3VT).

You can find the document here [3VT](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/latest/SolP/3VT?region=DE).

### Confirm Putaway Warehouse Tasks in RF Environment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

To confirm putaway warehouse tasks in the RF Environment, follow the steps described in the test script associated with the Scope Item you are testing.

For the Production Integration Process with Synchronous GR, go to Test procedures > Goods Receipt from Production with Synchronous Goods Movements > Confirm Putaway Warehouse Tasks > Variant 2: With Radio Frequency Devices in the Warehouse Production Integration with Synchronous Goods Receipt (5HO) test script.

You can find the document here: [5HO](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/latest/SolP/5HO?region=DE).

For the production Integration Process with delivery-based GR, go to Test Procedures > Delivery-Based Goods Receipt from Production > Confirm Putaway Warehouse Tasks > Variant 2: With Radio Frequency Devices in the Warehouse Production Integration (3DV) test script.

You can find the document here:

[3DV](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/latest/SolP/3DV?region=DE)

Go to Test Procedures > Confirm Putaway Warehouse Tasks in the Warehouse Goods Receipt from Repetitive Manufacturing (41U) test script.

You can find the document here [41U](https://me.sap.com/processnavigator/SolS/EARL_SolS-013/latest/SolP/41U?region=DE).

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

See the chapter [Business Conditions](#unique_7) [page ] 4

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
|  |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-mobile-rf-devices-in-warehousing-with-quality-management-6]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/63W_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 14,549 chars in the whole document
