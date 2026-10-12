---
id: 01-solution-foundation-and-platform/import-connection-setup-with-sap-analytics-cloud-1yb-786
title: Import Connection Setup with SAP Analytics Cloud (1YB) (1YB_S4CLD2608_BPD_EN_XX)
description: Test script (1YB) for loading S/4HANA master data into an SAP Analytics Cloud public dimension via OData import connection.
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/cds-data-extraction]
aliases: [1YB_S4CLD2608_BPD_EN_XX]
keywords: ["CDS-Based Data Extraction to BW, Datasphere, Data…", sap analytics cloud, odata connection, public dimensions, master data import, planning integration, communication arrangement, additional configuration, 1YB]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1YB_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-786
topic: 01-solution-foundation-and-platform/cds-data-extraction
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Import Connection Setup with SAP Analytics Cloud (1YB) (1YB_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1YB_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **CDS-Based Data Extraction to BW, Datasphere, Data Intelligence, HANA and SAC** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Import Connection Setup with SAP Analytics Cloud (1YB) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232850252)

[2 Prerequisites 3](#_Toc232850253)

[2.1 System Access 3](#_Toc232850254)

[2.2 Roles 3](#_Toc232850255)

[2.3 Additional Manual Configuration 3](#_Toc232850256)

[3 Overview Table 4](#_Toc232850257)

[4 Test Procedures 5](#_Toc232850258)

[4.1 Load Master Data into a Public Dimension 5](#_Toc232850259)

## Purpose

Overview

This scope item is for customers integrating SAP Analytics Cloud to SAP S/4HANA Cloud Public Edition for planning and analysis or group financial planning. The customer can replicate master data and actual or plan transaction data from SAP S/4HANA Cloud Public Edition into SAP Analytics Cloud for planning via OData services in SAP S/4HANA Cloud Public Edition.

The integration requires SAP S/4HANA Cloud and SAP Analytics Cloud for planning.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via the SAP Analytics Cloud. Your system administrator provides you with the URL to access the various apps assigned to your role.Your system administrator created the OData connection (For example, S4HODATACON) as part of the customer guide for this scope item. The source system connects to the SAP S/4HANA Cloud Public Edition system, which also created communication arrangement with communication scenario SAP_COM_0087. |

### Roles

| Name | ID | Log on |
| --- | --- | --- |
| SAP Analytics Cloud has Viewer, Modeler, Planner Reporter role. |  | Please ask your system administrator to assign to the testers. |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/0055f2947251d80cf7c7ead881a3853a)

## Overview Table

This scope item consists of several process steps, reports, items provided in the following table.

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Load Master Data into a Public Dimension](#unique_7) [page ] 5 |  | Dimensions | Successful data loading |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Load Master Data into a Public Dimension

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You have already implemented the set-up guide for Integration between SAP S/4HANA Cloud Public Edition and SAP Analytics Cloud. Before you perform the test procedures below, you are required to check the configuration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Analytics Cloud | Log on to SAP Analytics Cloud. | The Home screen is displayed. |  |
| 2 | Access Browse Dimension | Open Main Menu > Modeler > Public Dimensions. | The Public Dimensions screen is displayed. |  |
| 3 | Access Import Data | Select your public dimension and choose Import Data > Datasource.On the Select a Datasource screen, choose SAP S/4HANA Cloud Private Edition. Under Connection, select a name, for example S4HODATACON. | The Connection is set. |  |
| 4 | Create New Query | Choose Create New Query and then choose Next.On the New Query for SAP S/4HANA Cloud Private Edition screen, enter a name for the query.Select your entity type (for example, A_ProfitCenter) and choose Next.On the Build SAP S/4HANA Cloud Private Edition Query screen, drag the fields that you need for the public dimension (for example, Profit Center and Name) into the Selected Data area.Choose Create.A data preview is displayed. Adjust the proposed mapping of the OData columns to the columns of the public dimensions.Choose Finish Mapping and then choose Finish. | Master data is imported into public dimension. |  |

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

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Document describes SAP S/4HANA Cloud Public Edition integration, but the test steps select the datasource 'SAP S/4HANA Cloud Private Edition'.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[01-solution-foundation-and-platform/abap-core-data-services-extraction-for-sap-hana-6n4-test-script-1179]]
- related-to :: [[01-solution-foundation-and-platform/cds-based-extraction-with-sap-s-4hana-cloud-public-edition-35d-test-sc]]
- related-to :: [[01-solution-foundation-and-platform/test-script-abap-core-data-services-extraction-for-sap-data-intelligen]]
- related-to :: [[01-solution-foundation-and-platform/test-script-abap-core-data-services-extraction-for-sap-datasphere-53l]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1YB_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 7,991 chars in the whole document
