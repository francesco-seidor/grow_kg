---
id: 01-solution-foundation-and-platform/cds-based-extraction-with-sap-s-4hana-cloud-public-edition-35d-test-sc
title: CDS-Based Extraction with SAP S/4HANA Cloud Public Edition (35D) - Test Script (35D_S4CLD2608_BPD_EN_XX)
description: "SAP test script for scope item 35D: verifying CDS-based data extraction via ODP from S/4HANA Cloud Public Edition to BW/4HANA (source system, data flow, extracted data)."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/cds-data-extraction]
aliases: [35D_S4CLD2608_BPD_EN_XX]
keywords: ["CDS-Based Data Extraction to BW, Datasphere, Data…", cds-based extraction, operational data provisioning, test script, source system verification, data flow verification, extracted data verification, bw modeling tools, business roles, set-up instructions]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/35D_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-917
topic: 01-solution-foundation-and-platform/cds-data-extraction
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# CDS-Based Extraction with SAP S/4HANA Cloud Public Edition (35D) - Test Script (35D_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/35D_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **CDS-Based Data Extraction to BW, Datasphere, Data Intelligence, HANA and SAC** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | CDS-Based Extraction with SAP S/4HANA Cloud Public Edition (35D) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232836908)

[2 Prerequisites 3](#_Toc232836909)

[2.1 System Access 3](#_Toc232836910)

[2.2 Roles 3](#_Toc232836911)

[2.3 Additional Manual Configuration 3](#_Toc232836912)

[2.4 Preliminary Steps 4](#_Toc232836913)

[2.4.1 BW Modeling Tools Installation 4](#_Toc232836914)

[2.4.2 Object List 4](#_Toc232836915)

[3 Test Procedures 5](#_Toc232836916)

[3.1 Verify the Source System 5](#_Toc232836917)

[3.2 Verify the Data Flow 6](#_Toc232836918)

[3.3 Verify the Extracted Data 7](#_Toc232836919)

## Purpose

Overview

You can accelerate your virtual data model data extraction and replication to SAP BW/4HANA, SAP BW on SAP HANA, or other target applications from SAP S/4HANA Cloud Public Edition. Use the Operational Data Provisioning (ODP) framework, which supports the delta mechanism for change data capture (CDC).

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| SAP BW/4HANA System | You need an SAP BW/4HANA user with access to the Data Warehousing Workbench of the SAP BW system that is connected to your SAP S/4HANA Cloud Public Edition system. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name | ID | Log On |
| --- | --- | --- |
| BW/4HANA Modeler | SAP_BW4_MODELER |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/dee31e5f3dd49b75eebaf80e13fb9ec2)

### Preliminary Steps

#### BW Modeling Tools Installation

BW Modeling Tools need to be installed and added in Eclipse to perform testing. For detailed steps, please refer to the set-up instructions of the scope item Core Data Services-Based Extraction with SAP S/4HANA Cloud Public Edition (35D): Preparation > Install BW Modeling Tools.

#### Object List

Following objects have been created in prerequisite Set-Up instruction, there might be different names based on different system environment, you can ask for them from developers / testers who performed Set-Up instruction.

| Object | Name |
| --- | --- |
| Source System | CCF715 |
| DataSource | IEQP_DS |
| DataStore Object | IEQP_DSO |
| Data Transfer Process | DTP-Full RSDS IEQP_DS CCF715 > ADSO IEQP_DSO |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Verify the Source System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You open the BW/4HANA system to verify if source system has been created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Open SAP BW/4HANA | Log on SAP BW/4HANA | You successfully logged on and SAP Easy Access page is displayed. |  |
| 2. | Access BW Workbench | Run TCode RSA1 | The Process Chain Display Planning View page is displayed. |  |
| 3. | Find Source System | In the Source System panel, expand ODP – ABAP CDS Views and find the source system XXX that you created in Set-up Instructions or you are required to test in your own scenario (for example, CCF715). | The source system is displayed. |  |
| 4. | Verify the Source System | Right-click the source system and choose Check. | Source system connection XXX OK is displayed at the bottom of the screen. |  |

### Verify the Data Flow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You open the BW Modeling Perspective of Eclipse to verify if Data Source, DataStore Object, and Data Transfer Process has been created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Open BW/4HANA project from Eclipse | Open the Eclipse and navigate to the BW/4HANA system using the BW Modeling Perspective. | You successfully open the BW/4HANA project. |  |
| 2. | Check the Data Source | In the Data Sources node, expand the ABAP CDS Views folder and then expand the source system (for example, CCF715).Check if data source (for example, IEQP_DS) exists and activated (usually it's under NODESNOTCONNECTED folder). | Data Source IEQP_DS is displayed. |  |
| 3. | Check the DataStore Object | In the BW Repository node, expand the NODESNOTCONNECTED folder and then expand the DataStore Object (advanced) folder.Check if DSO (for example, IEQP_DSO) exists and activated. | Data Store Object IEQP_DSO is displayed. |  |
| 4. | Check the Data Transfer Process | In the DataStore Object (advanced) > IEQP_DSO node, expand the Data Transfer Process folder and check if DTP (for example， DTP-Full RSDS IEQP_DS CCF715 > ADSO IEQP_DSO ) exists and activated. | Data Transfer Process DTP-Full RSDS IEQP_DS CCF715 > ADSO IEQP_DSO is displayed. |  |

### Verify the Extracted Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You open the data browser to verify if data has been extracted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Open BW/4HANA project from Eclipse | Open the Eclipse and navigate to the BW/4HANA system using the BW Modeling Perspective. | You successfully open the BW/4HANA project. |  |
| 2. | Open DTP - Eclipse | In the DataStore Object (advanced) IEQP_DSO node, expand the Data Transfer Process folder and open DTP in previous section (for example，DTP-Full RSDS IEQP_DS CCF715 ADSO IEQP_DSO) | Data Transfer ProcessDTP-Full RSDS IEQP_DS CCF715 ADSO IEQP_DSO is displayed. |  |
| 3. | Open Fiori Launchpad | From DTP screen, find Show monitors button list and choose Process Monitor, there will be a SAP Fiori Launchpad opened in default web browser, enter your user information to login. From opened Fiori app, click SAP logo from top screen to navigate to home page.In case you encountered error like "App could not be opened either due to an incorrect SAP Fiori launchpad configuration or a missing role assignment" from browser pop-up, please verify with system admin if your user has been assigned to necessary roles like SAP_BW4_MODELER. | A Fiori app like Process Monitor - BW Cockpit is displayed via Eclipse jump. In Fiori Launchpad home page, title like Home - BW Cockpit QBW \| 003 is displayed, and several BW apps like DataStore Objects, InfoObjects, Process Chains shown. |  |
| 4. | Open DSO - BW Cockpit | In Fiori Launchpad home page, choose app DataStore Objects from Data Management group. In the opened Manage DataStore Objects - BW Cockpit app, filter DSO (advanced) by DSO name in previous section such as IEQP_DSO, and open this DSO. | After opening filtered DSO IEQP_DSO, Manage - BW Cockpit app displayed with page title IEQP_DSO (or DSO description), and one or more requests can be found under Default View tab. |  |
| 5. | Open Active Data Table - BW Cockpit | From DSO screen, choose the latest request which has Storage type Active Data Table. In the opened Manage Request - BW Cockpit screen, choose Active Data Table link, and continue to choose Contents. | Display DataStore Table Data - BW Cockpit Fiori app displayed with title like Display Active Table of IEQP_DSO. |  |
| 6. | Verify Data | In the opened Display DataStore Table Data - BW Cockpit Fiori app, check if data records exists. | Table Size like 60,116 exists and records under Details area exists, which means the activation is successful. |  |

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
- related-to :: [[01-solution-foundation-and-platform/import-connection-setup-with-sap-analytics-cloud-1yb-786]]
- related-to :: [[01-solution-foundation-and-platform/test-script-abap-core-data-services-extraction-for-sap-data-intelligen]]
- related-to :: [[01-solution-foundation-and-platform/test-script-abap-core-data-services-extraction-for-sap-datasphere-53l]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/35D_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 12,718 chars in the whole document
