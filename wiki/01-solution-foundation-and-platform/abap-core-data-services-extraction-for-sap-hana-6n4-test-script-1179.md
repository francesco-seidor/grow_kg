---
id: 01-solution-foundation-and-platform/abap-core-data-services-extraction-for-sap-hana-6n4-test-script-1179
title: ABAP Core Data Services Extraction for SAP HANA (6N4) - Test Script (6N4_S4CLD2608_BPD_EN_XX)
description: Test script (6N4) for replicating ABAP CDS views from S/4HANA Cloud Public Edition to SAP HANA via a Replication Task in SAP Web IDE.
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/cds-data-extraction]
aliases: [6N4_S4CLD2608_BPD_EN_XX]
keywords: ["CDS-Based Data Extraction to BW, Datasphere, Data…", cds data extraction, replication task, sap web ide, hdi container, roles and privileges, test scripts, remote source grants, 6N4]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6N4_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1179
topic: 01-solution-foundation-and-platform/cds-data-extraction
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# ABAP Core Data Services Extraction for SAP HANA (6N4) - Test Script (6N4_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6N4_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **CDS-Based Data Extraction to BW, Datasphere, Data Intelligence, HANA and SAC** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | ABAP Core Data Services Extraction for SAP HANA (6N4) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232826511)

[2 Prerequisites 3](#_Toc232826512)

[2.1 System Access 3](#_Toc232826513)

[2.2 Roles and Privileges 3](#_Toc232826514)

[2.3 Additional Manual Configuration 4](#_Toc232826515)

[3 Test Procedures 5](#_Toc232826516)

[3.1 Create Replication Task with SAP Web IDE 5](#_Toc232826517)

## Purpose

Overview

Accelerate your ABAP core data services data extraction from SAP S/4HANA Cloud Public Edition to SAP HANA by performing the configuration steps to bridge the integration between the two systems.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

The communication arrangements and connections in SAP S/4HANA Cloud Public Edition and SAP HANA On Premise have been created in Setup Instructions.

### System Access

You need to have an SAP HANA database user to access SAP HANA and a XS Advance developer user to access SAP Web IDE, the SAP HANA database user is preferred to be the DP Agent Admin user.

You could consult your system administrator for the user and URL of the SAP WEB IDE, it usually looks like this https://yourhanahost:53075.

|  |  |
| --- | --- |
|  | Details |
| SAP HANA | You need a user with access to the SAP HANA system that is connected to your SAP S/4HANA Cloud Public Edition system, prefer to use the same user(DP Agent Admin User) which connecting SAP HANA DP Agent and SAP HANA.You also need a user to access SAP Web IDE with role WebIDE_Developer assigned. |

### Roles and Privileges

You will need below policies assigned to your SAP Web IDE user within XS Advance.

| Name | Description |
| --- | --- |
| Roles:WebIDE_DeveloperSpace:Need to be a space member of the space which you plan to use to contain the contentSpace developer role need to be assigned to this user |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/da9d709dbaa49e47a881752b01524e68)

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Replication Task with SAP Web IDE

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You create a Project via SAP Web IDE, within the project, create a Replication Task to replicate data from source system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open SAP Web IDE | Log on SAP HANA Web IDE with your developer user:https://host:portIn most case it will looks like this:https://host:53075 | You successfully logged on and the Default page is displayed. |  |
| 2 | Create a New Project | In top left corner, click icon Development , then right click the Workspace icon, choose New, then click Project from Template, in Template Selection Tab, choose SAP HANA Database Application, then click Next, input your desired Project Name, then click Next, choose the desired Space your user is assigned to and you could use default SAP HANA Database Version which should be the same version with your SAP HANA Platform system, then click Finish. | The project is created. |  |
| 3 | Build the new project | Right click on the new name of the new Project, choose Build then Build to build the whole projec, then right click the database application under folder db, then choose Build then Build to build the HDI Container we need for the next steps. | The project is built and HDI Container is created. |  |
| 4 | Add HDI Container to Database Explorer | Click Database Explorer button, in the top left corner under Development, then click the Plus icon, choose HDI Container as the Instance type and select the container just created in the previous step, normally it contains user name and project name and other information, we will check the replicated data later within the container. | HDI Container is added to the Database Explorer. |  |
| 5 | Create SAP HANA Service Connection for Database Application | Go back to project created in the previous steps, right click on db folder and choose SAP HANA Service Connection, selectNon-HDI Container as Type and choose Create a new user-provided service as the Action; Fill in all the mandatory fields for example:Service Name: DemoGrantServiceHost: Your SAP HANA host addressPort: your tenant port somelike 3xx41 xx is your SAP HANA instance numberUser: Your DP Admin user created in the setup instructionPassword: your passwordClick Test Connection to check if the connection is setup, click Add if the test is OK. | You have created the SAP HANA Service Connection. |  |
| 6 | Create Grants File | Right click src folder of Database Application, select New ->File to create the grant file, input for example grants.hdbgrantsas the file name, take below sample as a draft for your grant file, make sure to change the grant service name and remote source name. In our case replace DemoGrantService with your own grant service name and replace RS_S4CE with your own remote source name and save the file.Sample file:{"DemoGrantService":{"object_owner":{"global_object_privileges":[{"name":"RS_S4CE","type":"REMOTE SOURCE","privileges":["CREATE VIRTUAL TABLE","CREATE VIRTUAL FUNCTION","CREATE REMOTE SUBSCRIPTION","PROCESS REMOTE SUBSCRIPTION EXCEPTION","ALTER","DROP"]}]},"application_user":{"global_object_privileges":[{"name":"RS_S4CE","type":"REMOTE SOURCE","privileges":["CREATE VIRTUAL TABLE","CREATE VIRTUAL FUNCTION","CREATE REMOTE SUBSCRIPTION","PROCESS REMOTE SUBSCRIPTION EXCEPTION","ALTER","DROP"]}]}}} | Grants file created. |  |
| 7 | Create Replication Task | Right click src folder and select New->Replication Task. Input Task name and click Create, the content panel shows, click top right icon Connect to a remote source, choose the desired remote source and click OK, then click the top right icon Add Objects, expand the folder ABAP_CDS and select your desired core data services view for example I_BUSINESSPARTNER then expand it and check MasterData(check Facts if your core data services is transaction data), adapter the Target Table name with your preferred value, choose Initial load only as Replication Behavior, then click OK. At last, build the project and database application again as in step 3. | The Replicaiton Task is created and the project is build. |  |
| 8 | Execute Replication Task | Right click on the Replication Task and choose Run->Execute RepTask. | The Replication Task is executed. |  |
| 9 | Check Data in the HDI Container | Click Database Explorer tab in the top left, choose and expand the HDI Container added in step 4, click on Tables all tables will list below, right click on the target table you specific at step 7 and click Open Data, check the data. | Data has been replicated to the target table. |  |

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
- related-to :: [[01-solution-foundation-and-platform/cds-based-extraction-with-sap-s-4hana-cloud-public-edition-35d-test-sc]]
- related-to :: [[01-solution-foundation-and-platform/import-connection-setup-with-sap-analytics-cloud-1yb-786]]
- related-to :: [[01-solution-foundation-and-platform/test-script-abap-core-data-services-extraction-for-sap-data-intelligen]]
- related-to :: [[01-solution-foundation-and-platform/test-script-abap-core-data-services-extraction-for-sap-datasphere-53l]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6N4_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 10,991 chars in the whole document
