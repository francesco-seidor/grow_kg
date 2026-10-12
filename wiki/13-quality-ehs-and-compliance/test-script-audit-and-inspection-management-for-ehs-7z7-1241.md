---
id: 13-quality-ehs-and-compliance/test-script-audit-and-inspection-management-for-ehs-7z7-1241
title: "Test Script: Audit and Inspection Management for EHS (7Z7) (7Z7_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 7Z7: create EHS checklists, run inspections, and add CAPA tasks to findings."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/ehs-audits-and-inspections]
aliases: [7Z7_S4CLD2608_BPD_EN_XX]
keywords: [EHS Audits and Inspections, audit and inspection management, ehs checklists, inspections, capa tasks, findings management, business roles, test prerequisites, demo data, three-system landscape]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7Z7_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1241
topic: 13-quality-ehs-and-compliance/ehs-audits-and-inspections
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Audit and Inspection Management for EHS (7Z7) (7Z7_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7Z7_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **EHS Audits and Inspections** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Audit and Inspection Management for EHS (7Z7) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232792962)

[2 Prerequisites 3](#_Toc232792963)

[2.1 System Access 3](#_Toc232792964)

[2.2 Roles 3](#_Toc232792965)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232792966)

[2.4 Preliminary Steps 4](#_Toc232792967)

[3 Overview Table 6](#_Toc232792968)

[4 Test Procedures 7](#_Toc232792969)

[4.1 Create a Checklist 7](#_Toc232792970)

[4.2 Create an Inspection 8](#_Toc232792971)

[4.3 Create a CAPA task 9](#_Toc232792972)

## Purpose

Overview

This scope item supports you in conducting inspections to ensure your company's compliance with external or internal product standards and regulations. This includes an inspection questionnaire and a systematic examination by an inspector, followed by structured review and action planning by a supervisor. The process helps you identify areas of nonconformity within your organization, address the root causes, and implement corrective and preventive actions (CAPAs) to ensure continuous compliance and transparency.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| Note For Environment, Health, and Safety, we deliver sample content (such as reports and regulations) that you can adapt according to your requirements. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Note Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the product assistance in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following link). |

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
| Environmental Manager | SAP_BR_EHS_ENV_MGMT | Environment Management | SAP_EHS_SP_ENV_MGMT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Location | Plant Wiesbaden | Location. |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| Master Data ID | Description |
| --- | --- |
| 3SR | Create EHS Location - MDS |

### Preliminary Steps

Purpose

Before you begin with the test procedures, make sure that you complete the steps below.

Procedure

1. Open the SAP Fiori launchpad.
2. If the Manage Locations (F3404) tile is not available on your SAP Fiori launchpad home screen, add it via the App Finder.

|  |
| --- |
| Note To add a tile to your SAP Fiori launchpad home screen, go to your profile in the upper right corner of the screen. Select the Edit Home Page option from the list. Then, select the blank tile that appears to go to the App Finder. In the Search field on the upper right side of the screen, enter the name of the app that you want to add to your SAP Fiori launchpad, and press Enter. The app appears in your search results. Select the pin to add the app tile to your SAP Fiori launchpad home screen. In the footer, the system shows a message that the tile has been added successfully. To exit edit mode, go back to your SAP Fiori launchpad home screen and select the Exit Edit Mode option from the list under your profile. |

1. Open the Manage Locations app.
2. Select the Plant Wiesbaden location and choose the hyperlink.
3. Make sure that the location is set to Active to enable its use in the test procedures.

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar (2434549).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Name (Role Template) | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create a Checklist](#unique_8) [page ] 7 | Environmental Manager | Manage Checklist/Questionnaire (F9072) | A checklist is created with defined sections and questions. |
| [Create an Inspection](#unique_9) [page ] 8 | Environmental Manager | My Inspections (F9071) | An inspection is created, questions are answered, findings are documented, and the inspection is submitted for review. |
| [Create a CAPA task](#unique_10) [page ] 9 | Environmental Manager | Manage Findings(F9073) | A task is created for the finding, then completed, and the finding is closed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create a Checklist

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspector creates a checklist, adds sections and questions, and releases the checklist for use in inspections.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Checklist/Questionnaire (F9072) app. | The Manage Questionnaire/Checklist app screen is displayed. |  |
| 3 | Create a Checklist | Choose Create. On the New Checklist popup, enter the basic details:Name: Fire Safety ComplianceCategory: SafetyValidity Area: AndorraChoose Continue. | The object page of the newly created checklist is displayed. |  |
| 4 | Add Section | Choose Add and enter the following title:Section: Fire Prevention | The checklist contains two sections. |  |
| 5 | Add Questions | Select the section and choose Add to add 3 questions.Question: Are all electrical wiring and appliances regularly inspected for damage and wear?Question: Is flammable material stored safely and away from heat sources?Question: Are smoking policies enforced and designated smoking areas equipped with proper disposal units?After filling the questions, choose Apply. | The questions are added to the relevant section and the user is redirected to the object page of the checklist. |  |
| 6 | Add Questions | Choose Save. | Changes are saved. |  |
| 7 | Release the Checklist | From the Set Status dropdown, select Released. | The checklist status is set to Released and is available for use in inspections. |  |

### Create an Inspection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspector creates a inspection, answers questions, and submits the inspection for review.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the My Inspections (F9071) app. | The My Inspections app is displayed. |  |
| 3 | Start Inspection | Choose Start Ad hoc Inspection and enter the following details:.Name: Plant WiesbadenChecklist: Fire Safety ComplianceChoose Continue. | The object page of the inspection is displayed. |  |
| 4 | Answer Questions | Select each question and enter the following details:Select Your Response: YesSelect Your Response: NoSelect Your Response: Not Applicable | Questions appear as Answered in the object page |  |
| 5 | Create a Finding | For one of the questions, enter:Description: Installed disposal unit in the designated smoking area is full.Choose Apply. | A finding with a Finding ID is created. |  |
| 6 | Finalize Inspection | Choose Submit for Review and confirm the submission. | The status of the inspection is updated to Submitted for Review. |  |

### Create a CAPA task

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection supervisor reviews the finding, adds corrective and preventive action (CAPA) tasks, and closes the finding.

Prerequisites

You need to have at least one finding recorded during an inspection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Findings (F9073) app. | The Manage Findings app screen is displayed. |  |
| 3 | Open a Finding | Search for and select the following finding:Finding: Installed disposal unit in the designated smoking area is full. | The object page of the finding is displayed. |  |
| 4 | Set a Category | Choose Set Category and enter:Category: Non-Conformity. | The category of the finding is set to Non-Conformity. |  |
| 5 | Set a Priority Level | Choose Set Priority and enter:Priority: High. | The priority level of the finding is set to High. |  |
| 6 | Add CAPA Task | In the Tasks section, choose Add Tasks, select Task, enter the relevant details in the task definition, and navigate back to the Manage Findings app. | The object page of the finding is displayed where the supervisor can create the CAPA. |  |
| 7 | Close Finding | When the task is done, choose Close. | The status of the finding is set to Closed. |  |

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
- see-also :: [[13-quality-ehs-and-compliance/ehs-lokation-anlegen-sds-3sr-358]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7Z7_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 16,974 chars in the whole document
