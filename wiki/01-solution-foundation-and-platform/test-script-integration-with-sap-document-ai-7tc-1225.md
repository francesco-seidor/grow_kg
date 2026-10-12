---
id: 01-solution-foundation-and-platform/test-script-integration-with-sap-document-ai-7tc-1225
title: "Test Script: Integration with SAP Document AI (7TC) (7TC_S4CLD2608_BPD_EN_XX)"
description: SAP S/4HANA Cloud 2608 test script (7TC) for checking the Manage Document AI Schema Registration Subscriptions app (F8996) and activating/deactivating schemas.
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/document-ai-integration]
aliases: [7TC_S4CLD2608_BPD_EN_XX]
keywords: [SAP Document AI Integration, sap document ai, schema registration, document inbound processing, schema activation, health check, business roles, manual configuration, test scripts, 7TC]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7TC_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1225
topic: 01-solution-foundation-and-platform/document-ai-integration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Integration with SAP Document AI (7TC) (7TC_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7TC_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **SAP Document AI Integration** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Integration with SAP Document AI (7TC) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232842560)

[2 Prerequisites 3](#_Toc232842561)

[2.1 System Access 3](#_Toc232842562)

[2.2 Roles 3](#_Toc232842563)

[2.3 Additional Manual Configuration 3](#_Toc232842564)

[3 Overview Table 4](#_Toc232842565)

[4 Test Procedures 5](#_Toc232842566)

[4.1 Check Availability of Manage Document AI Registration Subscriptions App 5](#_Toc232842567)

## Purpose

Overview

This scope item integrates SAP Document AI with SAP S/4HANA Cloud Public Edition, enabling automated document inbound processing for various application scenarios. SAP Document AI supports multiple document ingestion channels, allowing documents to be uploaded manually, via API or email ingestion.

By leveraging preconfigured schemas and AI models, SAP Document AI automatically extracts structured data from uploaded documents. This extracted data is then utilized within application scenarios to create or update business records.

Additionally, by reviewing and correcting extraction results, the AI extraction logic can be fine-tuned to better accommodate client-specific documents.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition system | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP Business Technology Platform | Your system administrator provides you with a URL and the login details. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Business Role or Template) | ID | Description (Space) | ID | Log On |
| --- | --- | --- | --- | --- |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC |  |
| Configuration Expert | SAP_BR_CONF_EXPERT_BUS_NET_INT | Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/adf4cc30aadea6fd3f9793d91c300792)

## Overview Table

This scope item consists of the process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Check Availability of Manage Document AI Registration Subscriptions App | Business Process Specialist and Configuration Expert | Manage Document AI Schema Registration Subscriptions (F8996) | List of registered schemas available for subscriptions are displayed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Check Availability of Manage Document AI Registration Subscriptions App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this test step, you are checking the availability of the Manage Document AI Workspace app on SAP Fiori launchpad.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with a user having both roles, Business Process Specialist and Configuration Expert. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Manage Document AI Schema Registration Subscriptions (F8996) app. Click Go. | The Manage Document AI Schema Registration Subscriptions app opens with the list of schemas for the default client. |  |
| 3 | Select the schema Registration | Click on the radio button next to Schema with Registration ID | The registration ID selected |  |
| 4 | Activate | Click on the Activate Button | Schema activation is initiated and runs in the background. The Status column changes to “Active” once the process is completed successfully. Logs can be checked on the detail page. |  |
| 5 | Deactivate | Click on the Deactivate Button | Schema deactivation is initiated and runs in the background. The Status column changes to “Inactive” once the process is completed successfully. Logs can be checked on the detail page. |  |
| 6 | Health Check | Click on the Health check | Schema health check is initiated and runs in the background. The health check status column is updated with time of check once the process is completed successfullyLogs can be checked on the detail page. |  |
| 7 | SAP Document AI | Click on the SAP Document AI | It should navigate to the SAP Document AI app to view and manage schema |  |
| 8 | Logs | Select the schema registration | In Detail page, Different Logs can be viewed- Schema Activation / Deactivation, Schema Subscription Health Check and Schema Document Processing. |  |

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
> Flagged while digesting this document, not verified: Purpose text refers to the 'Manage Document AI Workspace' app while the test case and app are named Manage Document AI Schema Registration Subscriptions (F8996)

## Connections
- part-of :: [[_cluster]]
- see-also :: [[01-solution-foundation-and-platform/test-script-sap-archiving-and-document-access-core-by-opentext-integra]]
- see-also :: [[08-sales-order-management/test-script-create-sales-orders-from-unstructured-data-4x9-ae-sap-s-4h]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7TC_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 9,943 chars in the whole document
