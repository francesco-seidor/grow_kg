---
id: 01-solution-foundation-and-platform/test-script-abap-core-data-services-extraction-for-sap-data-intelligen
title: "Test Script: ABAP Core Data Services Extraction for SAP Data Intelligence (53M) (53M_S4CLD2608_BPD_EN_XX)"
description: "Test script for scope item 53M: extracting ABAP CDS view data from S/4HANA Cloud Public Edition to SAP Data Intelligence via pipelines and replication flows."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/cds-data-extraction]
aliases: [53M_S4CLD2608_BPD_EN_XX]
keywords: ["CDS-Based Data Extraction to BW, Datasphere, Data…", cds view extraction, sap data intelligence, pipeline modeler, cloud data integration, replication flows, policy management, additional manual configuration, test scripts, 53M]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/53M_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1061
topic: 01-solution-foundation-and-platform/cds-data-extraction
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: ABAP Core Data Services Extraction for SAP Data Intelligence (53M) (53M_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/53M_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **CDS-Based Data Extraction to BW, Datasphere, Data Intelligence, HANA and SAC** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | ABAP Core Data Services Extraction for SAP Data Intelligence (53M) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232822596)

[2 Prerequisites 3](#_Toc232822597)

[2.1 System Access 3](#_Toc232822598)

[2.2 Roles 3](#_Toc232822599)

[2.3 Additional Manual Configuration 3](#_Toc232822600)

[3 Test Procedures 4](#_Toc232822601)

[3.1 Build Pipeline to Consume Core Data Services View Data 4](#_Toc232822602)

[3.2 Build Pipeline to Consume Data from Cloud Data Integration Source 6](#_Toc232822603)

[3.3 Create Replications 7](#_Toc232822604)

## Purpose

Overview

Accelerate your ABAP core data services extraction from SAP S/4HANA Cloud Public Edition to SAP Data Intelligence. You must perform additional configuration steps to activate the ABAP core data services integration scenario between SAP S/4HANA Cloud Public Edition and SAP Data Intelligence.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note This best practice is for customers who want to extract data from SAP S/4HANA Cloud Public Edition to SAP HANA Cloud and who already have an existing SAP Data Intelligence license. |

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

The communication arrangements and connections in SAP Data Intelligence have been created in the Setup Instructions.

### System Access

| System | Details |
| --- | --- |
| SAP Data Intelligence | You need a SAP Data Intelligence user with access to the SAP Data Intelligence system that is connected to your SAP S/4HANA Cloud Public Edition system |

### Roles

Policy Management is the component in SAP Data Intelligence responsible for authorizations. You will need below policies assigned to execute the steps in this test script

Table 1:

| Name | Description |
| --- | --- |
| sap.dh.developer | Working with Pipeline Modeler |
| sap.dh.metadata | Working with Metadata Explorer |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/a95d52f94430d6ee4759e32b8c71c4d2)

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Build Pipeline to Consume Core Data Services View Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You build pipeline to consume core data services view data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open SAP Data Intelligence | Log on SAP Data Intelligence | You successfully logged on and the Home page is displayed. |  |
| 2 | Open Modeler | Click on Modeler tile | The Data Intelligence Modeler window is opened. |  |
| 3 | Create Pipeline | Choose Create Graph button on the left panel. | A new Pipeline is created. |  |
| 4 | Add ABAP CDS Reader Operator | Switch to Operators tab on the left panel. Find and drag the ABAP CDS Reader operator onto the canvas. | The ABAP CDS Reader Operator is placed on the canvas. |  |
| 5 | Configure ABAP CDS Reader Operator | Choose Open Configuration beside the ABAP CDS Reader operator. A Configuration Panel should appear on the right side. Maintain below values for the configuration:ABAP Connection: the connection you created in Set-Up guide, for example ZS40532Version: com.sap.abap.cds.reader.v2Subscription Type: NewSubscription Name: s001ABAP Core Data Services Name: The core data services view you wish to extract data from, for example, I_JOURNALENTRYTransfer Mode: Initial LoadRecords per roundtrip: 50000 | The ABAP CDS Reader Operator is configured. |  |
| 6 | Add Write File Operator | From theOperators tab on the left panel, find and drag the Write File operator onto the canvas. (You can use the search box to search for the operator). | The Write File Operator is placed on the canvas. |  |
| 7 | Configure Write File Operator | Choose Open Configuration beside the Write File operator. A Configuration Panel should appear on the right side. Maintain below values for the configuration:Connection: Choose Connection Management for Configuration Type,DI_DATA_LAKE for Connection IDPath mode: Static(from configuration)Path: for example, /shared/cdsdata/I_JOURNALENTRY.csvMode: Append | The Write File Operator is configured. |  |
| 8 | Connect the Operators | Drag the output from ABAP CDS Reader Operator onto the input of Write File Operator. In the popup Select Conversion window, choose the first option that says Converts the value as the payload in a File message. If the input is a message, no data is modified. Otherwise, the resulting file message receives empty attributes. Choose OK | The operators are connected. |  |
| 9 | Save and execute the pipeline | Press Save button to save the pipeline. Enter Name and other information when prompted, press OK.There could be a warning message which says The layout information for this graph was missing or incomplete. Choose OK. After the pipeline is saved, press Run button. | Switch to the Status tab below. You should see the status of the pipeline would first appear in pending status and then turn into running state |  |
| 10 | Check Data Loaded | Open another window in browser and log on SAP Data Intelligence. Click on Metadata Explorer tile. Choose Browse Connections. Choose DI_DATA_LAKE connection, navigate to the path defined in Write File operator, for example /shared/cdsdata/I_JOURNALENTRY.csv. You can chooseView Fact Sheet to check the data loaded | If there is any data available in the core data services, you should be able to see them loaded via Data Preview |  |
| 11 | Stop the pipeline | Back to the Data Intelligence Modeler window. In the Status tab below, choose Stop Process for your running pipeline. | The pipeline should turn into completed status. |  |

### Build Pipeline to Consume Data from Cloud Data Integration Source

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You build pipeline to consume data from Cloud Data Integration source.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open SAP Data Intelligence | Log on SAP Data Intelligence | You successfully logged on and the Home page is displayed. |  |
| 2 | Open Modeler | Click on Modeler tile | The Data Intelligence Modeler window is opened. |  |
| 3 | Create Pipeline | Choose Create Graph button on the left panel. | A new Pipeline is created. |  |
| 4 | Add Cloud Data Integration Consumer Operator | Switch to Operators tab on the left panel. Find and drag the Cloud Data Integration Consumer operator onto the canvas. | The Cloud Data Integration Consumer Operator is placed on the canvas. |  |
| 5 | Configure Cloud Data Integration Consumer Operator | Choose Open Configuration beside the Cloud Data Integration Consumer operator. A Configuration Panel should appear on the right side. Then click the pencil button for the Source field. Maintain below values for the configuration:Connection ID: the connection you created in Set-Up guide, for example ZS40531Source: click the Browse button, expand and choose/ABAP_CDS/I_COMPANYCODE/MasterDataColumns: click the Add Column button and choose for example the CompanyCode and CompanyCodeName field. (Press and hold CTRL to select multiple fields) | The Cloud Data Integration Consumer Operator is configured. |  |
| 6 | Add Flowagent File Producer Operator | From theOperators tab on the left panel, find and drag the Flowagent File Producer operator onto the canvas. (You can use the search box to search for the operator). | The Flowagent File Producer Operator is placed on the canvas. |  |
| 7 | Configure Flowagent File Producer Operator | Choose Open Configuration beside the Flowagent File Producer operator. A Configuration Panel should appear on the right side. Maintain below values for the configuration:Storage type: sdlSDL Connection: Choose DI_DATA_LAKE for Connection IDSDL file name: for example, /shared/I_COMPANYCODE.csv | The Write File Operator is configured. |  |
| 8 | Connect the Operators | Drag the output (outConfig) from Cloud Data Integration Consumer Operator onto the input of Flowagent File Producer Operator. | The operators are connected. |  |
| 9 | Save and execute the pipeline | Press Save button to save the pipeline. Enter Name and other information when prompted, press OK. After the pipeline is saved, press Run button. | Switch to the Status tab below. You should see the status of the pipeline would first appear in pending status and then turn into running state |  |
| 10 | Check Data Loaded | Open another window in browser and log on SAP Data Intelligence. Click on Metadata Explorer tile. Choose Browse Connections. Choose DI_DATA_LAKE connection, navigate to the path defined in Write File operator, for example /shared/I_COMPANYCODE.csv. You can chooseView Fact Sheet to check the data loaded | If there is any data available in the core data services view, you should be able to see them loaded via Data Preview |  |
| 11 | Stop the pipeline | Back to the Data Intelligence Modeler window. In the Status tab below, choose Stop Process for your running pipeline. | The pipeline should turn into completed status. |  |

### Create Replications

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You create Replications to consume S/4HANA Cloud core data services view data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Open SAP Data Intelligence | Log on SAP Data Intelligence. | You successfully logged on and the home page is displayed. |  |
| 2. | Open Modeler | Click on Modeler tile. | The Data Intelligence Modeler window is opened. |  |
| 3. | Create Replications | Click Replications tab, and then click Create Replication Flow, and then enter the Name and click OK . | Replication Flow Editor is opened. |  |
| 4 | Configure General Data | In General Tab, maintain below values for the configuration:Source Connection: Choose the S/4 HANA Cloud connection ID created in Connection ManagementSource Container: Select CDTarget Connection: Choose the HANA_DB connection ID created in Connection ManagementTarget Container: Select the target SchemaThen Save the change | You have configured the general data for replication. |  |
| 5 | Create Tasks | Click Tasks Tab, and click Create to create a task:Add Datasets: For example, I_BUSINESSPARTNERLoad Type: Initial Only | You have added the task. |  |
| 6 | Save and Deploy the Replication | Click Save, then click Deploy. | The Replication is saved and deployed. |  |
| 7 | Run | Click Run to start the replication. | Data is replicated to the target table. |  |

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
- related-to :: [[01-solution-foundation-and-platform/test-script-abap-core-data-services-extraction-for-sap-datasphere-53l]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/53M_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 15,348 chars in the whole document
