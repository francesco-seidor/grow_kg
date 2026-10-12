---
id: 01-solution-foundation-and-platform/test-script-abap-core-data-services-extraction-for-sap-datasphere-53l
title: "Test Script: ABAP Core Data Services Extraction for SAP Datasphere (53L) (53L_S4CLD2608_BPD_EN_XX)"
description: "Test script for scope item 53L: extracting ABAP CDS views from S/4HANA Cloud Public Edition 2608 into SAP Datasphere via views, data flows, entity import and replication flows."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/cds-data-extraction]
aliases: [53L_S4CLD2608_BPD_EN_XX]
keywords: ["CDS-Based Data Extraction to BW, Datasphere, Data…", abap cds extraction, sap datasphere, graphical view preview, data flow, entity import, replication flow, datasphere roles, setup instructions, test scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/53L_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1060
topic: 01-solution-foundation-and-platform/cds-data-extraction
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: ABAP Core Data Services Extraction for SAP Datasphere (53L) (53L_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/53L_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **CDS-Based Data Extraction to BW, Datasphere, Data Intelligence, HANA and SAC** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | ABAP Core Data Services Extraction for SAP Datasphere (53L) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232830701)

[2 Prerequisites 3](#_Toc232830702)

[2.1 System Access 3](#_Toc232830703)

[2.2 Roles 3](#_Toc232830704)

[2.3 Additional Manual Configuration 3](#_Toc232830705)

[3 Test Procedures 4](#_Toc232830706)

[3.1 Create Graphical View to Preview ABAP Core Data Services View Data 4](#_Toc232830707)

[3.2 Create Data Flow to Consume ABAP Core Data Services View Data 5](#_Toc232830708)

[3.3 Import entities from S4 HANA Cloud 6](#_Toc232830709)

[3.4 Replicate Data from S4 HANA Cloud to SAP HANA Cloud 7](#_Toc232830710)

## Purpose

Overview

Accelerate your ABAP core data services extraction from SAP S/4HANA Cloud Public Edition to SAP Datasphere. You must perform additional configuration steps to activate the ABAP OData integration between SAP S/4HANA Cloud Public Edition and SAP Datasphere.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

The communication arrangements and connections in S/4 HANA Cloud and SAP Datasphere have been created in set-up instructions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| SAP Datasphere | You need an SAP Datasphere user with access to the SAP Datasphere system that is connected to your SAP S/4HANA Cloud Public Edition system. |

### Roles

You will need below policies assigned to execute the steps in this test script

| Name | Description |
| --- | --- |
| DW Modeler | Datasphere Modeler: Entity Relationship Privileges |
| DW Integrator | Datasphere Integrator: Limited Privileges |
| DW Space Administrator | Datasphere Space Administrator: Full Privileges |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/1e6938175090653a5336ff230abc4aad)

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Graphical View to Preview ABAP Core Data Services View Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You create graphical view to preview ABAP core data services view data. You could use SAP S/4 HANA Cloud Connection or Cloud Data Integration Connection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Open SAP Datasphere | Log on SAP Datasphere. | You successfully logged on and the home page is displayed. |  |
| 2. | Open Graphical View editor | Click the Data Builder, select the Space in which you want to create a view, and choose New Graphical View. | The Graphical View editor opens. |  |
| 3. | Display Sources | Choose Sources tab, which lists all the connections to sources, database user schemas, and HDI containers associated with your space. Choose a connection you created in setup guide and expand to view its contents.A maximum of 1,000 items can be displayed in any node and you can only search across the displayed items. To search across the full contents of a node, click Import from Connections to open the node in the Import Objects from Connection dialog and search again. | Core Data Services Views in S/4 HANA Cloud are displayed. |  |
| 4. | Select Core Data Services View Object | Select the object of your choice, and then drag and drop it onto the diagram.The source is added to the diagram, its symbol is selected, and its properties are displayed in the side panel. In addition, an output node, initially entitiled view 1, which represents the final output structure of the view, is created in the diagram and linked to the source.Save Remote Table. | The imported remote table is saved. |  |
| 5 | Preview Data | Choose the remote table, choose Preview data. | Remote table data is previewed. |  |

### Create Data Flow to Consume ABAP Core Data Services View Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You create data flow to consume ABAP core data services view data. You could use SAP S/4 HANA Cloud Connection or Cloud Data Integration Connection or SAP ABAP Connection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open SAP Datasphere | Log on SAP Datasphere. | You successfully logged on and the home page is displayed. |  |
| 2 | Open Data Flow editor | Click the Data Builder, select the Space in which you want to create a view, and choose New Data Flow. | The Data Flow editor opens. |  |
| 3 | Display Sources | Choose Sources tab, which lists all the connections to sources, database user schemas, and HDI containers associated with your space. Choose a connection you created in setup guide and Expand to view its contents. | Core data services views in S/4 HANA Cloud are displayed. |  |
| 4 | Select Core Data Services View Object | Select the object of your choice, and then drag and drop it onto the diagram. | A core data services view source is added. |  |
| 5 | Add Target Table | Choose the Source Object and Context buttons appear on the right. You can choose Add table and enter Technical name of target in the property panel object. Then choose Create and Deploy Table in the information dialog, choose Create and Deploy again. | The target table is placed on the canvas. |  |
| 6 | Save and execute the data flow | Press Save button to save the pipeline. In the Save Data Flow dialog, enter Business Name and Technical Name, choose SaveAfter the date flow is saved, press Execute button. | In the Properties panel, you can check the Execution Status. You should see the status of the pipeline would first appear in started status and then turn into running state |  |
| 7 | Preview Data Loaded | When the Execution Status is Completed, you can choose the target table then choose Preview Data | If there is any data available in the core data services view, you should be able to see them loaded. |  |

### Import entities from S4 HANA Cloud

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You import entities from S4 HANA Cloud system. You could use SAP S/4 HANA Cloud Connection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Open SAP Datasphere | Log on SAP Datasphere. | You successfully logged on and the home page is displayed. |  |
| 2. | Import Entities | Click the Data Builder, select the Space in which you want to import entities, then click Import and choose Import Entities. | The related user interface opens. |  |
| 3. | Select Connection | Select the desired connection and choose Next Step . | Connection shows up. |  |
| 4. | Select Entities | Search or browser the right entities and check them, then choose Next Step. | Entities show up. |  |
| 5 | Import and Deploy | The summary is showed, choose Import and Deploy. | Entities are being imported, check notification for status. |  |

### Replicate Data from S4 HANA Cloud to SAP HANA Cloud

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You replicate data from S4 HANA Cloud system to SAP HANA Cloud system with help of SAP Datasphere Replication Flow. You could use SAP S/4 HANA Cloud ABAP Connection and SAP HANA Cloud connection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open SAP Datasphere | Log on SAP Datasphere. | You successfully logged on and the home page is displayed. |  |
| 2 | New Replication Flow | Click the Data Builder, select the Space in which you want to import entities, then click the tab Flows and choose New Replication Flow. | The related user interface opens. |  |
| 3 | Select Source Connection | Select the desired S/4 HANA Cloud connection (Type ABAP) as source connection. | Connection shows up. |  |
| 4 | Select Source Container | Click Select Source Containe, click/CDS_EXTRACTION then choose Select. | Source Container is selected. |  |
| 5 | Add Source Objects | Click Add Source Objects, in the popup windows, search and select the desried objects for example: I_BUSINESSPARTNER, mark checkbox and then choose Next, in the next screen, review the objects and mark the checkbox, then choose Add Selection. | Source objects are imported and added. |  |
| 6 | Select Target Connection | Click icon Browse target connection , in the popup windows, select the desired SAP HANA Cloud connection. | Target Connection is selected. |  |
| 7 | Select Container | Click icon Browse Target Container, click desired container here take DBADMIN as example, be sure to use a suitable schema, then choose Select. After selected the target container, you could rename the target objects, in our case , we keep the default. | Target container is selected. |  |
| 8 | Save | Choose a suitable name and click Save | Replication Flow is saved. |  |
| 9 | Deploy | Choose Deploy. | Replication Flow is deployed. |  |
| 10 | Run | ChooseRun, and check the execution status. You could check the target system to make sure data is replicated to the target system. | Data is replicated to target system. |  |

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
- related-to :: [[01-solution-foundation-and-platform/abap-core-data-services-extraction-for-sap-hana-6n4-test-script-1179]]
- related-to :: [[01-solution-foundation-and-platform/cds-based-extraction-with-sap-s-4hana-cloud-public-edition-35d-test-sc]]
- related-to :: [[01-solution-foundation-and-platform/import-connection-setup-with-sap-analytics-cloud-1yb-786]]
- related-to :: [[01-solution-foundation-and-platform/test-script-abap-core-data-services-extraction-for-sap-data-intelligen]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/53L_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 14,102 chars in the whole document
