---
id: 01-solution-foundation-and-platform/walkme-premium-integration-7te-test-script-1226
title: WalkMe Premium Integration (7TE) Test Script (7TE_S4CLD2608_BPD_EN_XX)
description: "SAP Best Practices test script for the WalkMe Premium Integration scope item (7TE): customizing and publishing user assistant content in S/4HANA Cloud Public Edition."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/in-app-user-assistance]
aliases: [7TE_S4CLD2608_BPD_EN_XX]
keywords: [In-App User Assistance (SAP Enable Now and WalkMe), walkme integration, user assistant content, content publishing, walkme roles, business roles, manual configuration, quality assurance testing, system access, 7TE]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7TE_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1226
topic: 01-solution-foundation-and-platform/in-app-user-assistance
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# WalkMe Premium Integration (7TE) Test Script (7TE_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7TE_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **In-App User Assistance (SAP Enable Now and WalkMe)** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | WalkMe Premium Integration (7TE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232828550)

[2 Prerequisites 3](#_Toc232828551)

[2.1 System Access 3](#_Toc232828552)

[2.2 Roles 3](#_Toc232828553)

[2.2.1 WalkMe Account 3](#_Toc232828554)

[2.2.2 SAP S/4HANA Cloud Public Edition Tenant 4](#_Toc232828555)

[2.3 Additional Manual Configuration 4](#_Toc232828556)

[3 Overview Table 5](#_Toc232828557)

[4 Test Procedures 6](#_Toc232828558)

[4.1 Customize and Add Standard Assistant Content for SAP S/4HANA Cloud Public Edition 6](#_Toc232828559)

[4.1.1 Customize Standard User Assistant Content 6](#_Toc232828560)

## Purpose

Overview

This scope item allows the integration of the WalkMe Premium digital adoption platform product to SAP S/4HANA Cloud Public Edition to enhance user adoption by user behavior insights, in-application guidance, and step-by-step workflow automation.

Additionally, you can customize standard SAP content and use all features for in app-guidance including AI features, ActionBots (Limited), and workflows.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

- Access to the SAP S/4HANA Cloud Public Edition system.
- The WalkMe Premium Integration setup for SAP S/4HANA Cloud Public Edition requires a WalkMe Account to create and edit WalkMe Content.
- The content author has a WalkMe Editor downloaded on their computer.
- The content author has a WalkMe Editor Extension downloaded on their browser.

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition Tenant | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role.https://my301430.s4hana.ondemand.com/ui?edithelp=true#Shell-home.Note This is a sample URL. Use the URL to your Fiori launchpad instead. |
| WalkMe Account | Use the WalkMe Account credentials provided to you in your onboarding email. |
| WalkMe Editor | Download and install the WalkMe Editor application on your computer from https://download.walkme.cloud.sap/. |
| WalkMe Editor Extension | Download and install the WalkMe Editor Extension on your browser. It's required for creating WalkMe Content.Refer to: https://support.walkme.com/knowledge-base/user-extension-faq/#brief-overview |

### Roles

#### WalkMe Account

Use

The WalkMe Integration for SAP S/4HANA Cloud Public Edition requires a WalkMe account to create, edit, and publish WalkMe content.

Procedure

1. You have a WalkMe user provided with Builder or Content Manager role.
2. Log in to your WalkMe account using the credentials provided to you.

Result

The Builder role lets you create and modify WalkMe content and settings, except for publishing and user management.

If you need access to publishing also you will need to be assigned as a Content Manager.

Please refer to [https://support.walkme.com/knowledge-base/roles-and-permissions/](https://support.walkme.com/knowledge-base/roles-and-permissions/).

#### SAP S/4HANA Cloud Public Edition Tenant

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Logon |
| --- | --- | --- | --- | --- |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/54b6ba2840cf605d7a9d500c0e1ea6fd)

## Overview Table

This scope item consists of several items provided in the table below.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Customize and Add Standard Assistant Content for SAP S/4HANA Cloud Public Edition](#unique_8) [page ] 6 |  | WalkMe Editor | WalkMe content has changed or new content is visible in SAP S/4HANA Cloud Public Editionemphasis> Tenant |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Customize and Add Standard Assistant Content for SAP S/4HANA Cloud Public Edition

| Step No | Test Step | Description |
| --- | --- | --- |
| 1 | [Customize Standard User Assistant Content](#unique_10) [page ] 6 | Customize standard user assistant content that is provided for SAP S/4HANA Cloud Public Edition. |

#### Customize Standard User Assistant Content

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Customize standard user assistant content that is provided for SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Open WalkMe Editor | Click Open WalkMe Editor and log in to the SAP EU data center to view and test your accelerator content. | The WalkMe Editor opens up, so you can further customize and test the content. |  |
| 2 | Build Content | Click the blue + button in the WalkMe Editor and select ShoutOut.Name your ShoutOut and choose from the available templates.Set it to play always.Save once you have finished customizing. | The ShoutOut is now visibile in the WalkMe Editor. |  |
| 3 | Publish to WalkMe Test Environment | Select the checkbox of the ShoutOut created and Publish the content to your Test Environment from the WalkMe Editor. | The content should be visible only in your Test Environment (not Production).Note It is a content building best practice to always publish to Test Environment before Production. |  |
| 4 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad with a business user with SAP_BR_ADMINISTRATOR role to view and test your content. | After logging in the S4HANA system, the user refreshes the screen and sees the content created. |  |
| 5 | Perform QA | Do a Quality Assurance (QA) check to confirm that the content is functioning. | Enter the testing environment and follow the process exactly as it was built. Does the content block important information on the screen? Run it A-to-Z once or twice on different browsers. The best practice is to run the sanity check on a smaller screen to check that everything still appears correctly and on the lowest supported browser versions. |  |
| 6 | Publish to Production | After you confirm that the content functions correctly, publish to Production Environment. | Content will now be live and available to end users. |  |

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
- related-to :: [[01-solution-foundation-and-platform/test-script-sap-enable-now-integration-3n5-962]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7TE_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 11,344 chars in the whole document
