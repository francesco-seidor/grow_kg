---
id: 16-two-tier-erp-and-central-finance/test-script-project-data-replication-to-central-finance-3w1-978
title: Test Script - Project Data Replication to Central Finance (3W1) (3W1_S4CLD2608_BPD_EN_XX)
description: "Test script for scope item 3W1: create and release a project in the source system and verify replication of project accounting data to Central Finance."
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/central-finance-replication]
aliases: [3W1_S4CLD2608_BPD_EN_XX]
keywords: [Central Finance Replication from Subsidiaries, central finance, project data replication, project creation, project release, enterprise projects, communication arrangements, business roles, test scripts, 3W1]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3W1_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-978
topic: 16-two-tier-erp-and-central-finance/central-finance-replication
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script - Project Data Replication to Central Finance (3W1) (3W1_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3W1_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Central Finance Replication from Subsidiaries** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Project Data Replication to Central Finance (3W1) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232830388)

[2 Prerequisites 3](#_Toc232830389)

[2.1 System Access 3](#_Toc232830390)

[2.2 Roles 3](#_Toc232830391)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232830392)

[2.4 Additional Manual Configuration 4](#_Toc232830393)

[2.5 Preliminary Steps 4](#_Toc232830394)

[3 Overview Table 5](#_Toc232830395)

[4 Test Procedures 6](#_Toc232830396)

[4.1 Create Project 6](#_Toc232830397)

[4.2 Release Project 7](#_Toc232830398)

## Purpose

Overview

This scope item enables the setup of an integration between SAP S/4HANA Cloud Public Edition and Central Finance in SAP S/4HANA to replicate the project accounting structure data. SOAP message-based communication and SAP Cloud Connector are used as integration technology.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites to conducting the test in terms of systems, users, master data, organizational data, and other test data and business conditions.

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
| Project Financial Controller | SAP_BR_PROJ_FIN_CONTROLLER | Project Control - Finance | SAP_BR_PROJ_FIN_CONTROLLER |  |

### Master Data, Organizational Data, and Other Data

Default Values

The organizational structure and master data of your company was created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

The business process is enabled with this organization-specific master data, examples are provided in the next section.

Use the following master data in the process steps described in this document:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | <company code> |  |  |
| Cost Center | For example, xx101501 (where xx is the first two digits of your company code) |  |  |
| Profit Center | For example, YB900 |  |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/e87b6515879119904ee3078d1e08ac7c)

### Preliminary Steps

- The Integration Scenario SAP_COM_0470 is activated.
- CFIN Value- and Key-Mapping is maintained in the target system.

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Project](#unique_9) [page ] 6 | Project Financial Controller | Project Control - Enterprise Projects (F3215) | The project definition and WBS elements are created in the source system with all the required parameters. |
| [Release Project](#unique_10) [page ] 7 | Project Financial Controller | Project Control - Enterprise Projects (F3215) | The project status is changed to REL (Release) and the data is replicated in the CFIN system. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a project with a project definition using the Project Control - Enterprise Projects (F3215) Fiori app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Financial Controller in the subsidiary source system. |  |  |
| 2 | Access App | Open Project Control - Enterprise Projects (F3215) | The Project Control screen displays. |  |
| 3 | Create Project | Choose Create and make the following entries in the Header tab:Project Name: for example, RND_CFIN_TESTProject ID: for example, RnD_00001Project Profile: Overhead ProjectPlanned Start: <current date>Planned Finish : <current date + 3 months>Make the following entries in the General Information tab:Responsible Cost Center: <cost center>Profit Center: <profit center> | Note Note down the Project ID. |  |
| 4 | Save Project | Choose Create. | The project is created with the provided parameters.One WBS element with the following details is created under the project identification. |  |

### Release Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release the project.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Financial Controller in the subsidiary source system. |  |  |
| 2 | Access App | Open Project Control - Enterprise Projects (F3215) . | The Project Control screen screen displays. |  |
| 3 | Open Project | Make the following entries and choose Go:Project : <Project ID from the previous process step> |  |  |
| 4 | Release Project | Choose the project from the list.At the top of the screen, choose Processing Status > Release . | The project is released.NoteYou can change the processing status with the Project Briefs (F2602) Fiori app as a Project Manager.Once released, a project cannot be renamed or deleted. |  |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the target Central Finance system. |  |  |
| 2 | Call Transaction | Call transaction CJ20N. | The Project Builder screen screen displays. |  |
| 3 | Open Project | Choose Project > Open .Make the following entries and choose Open:Project Definition: <Project ID from the previous process step> | The replicated project is displayed. |  |

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
- related-to :: [[16-two-tier-erp-and-central-finance/test-script-process-integration-of-sap-s-4hana-finance-with-central-fi]]
- related-to :: [[16-two-tier-erp-and-central-finance/test-script-subsidiary-integration-of-sap-s-4hana-cloud-to-central-fin]]
- related-to :: [[16-two-tier-erp-and-central-finance/two-tier-consolidation-of-autonomous-subsidiaries-via-central-finance]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3W1_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 11,415 chars in the whole document
