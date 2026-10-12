---
id: 01-solution-foundation-and-platform/test-script-output-management-1lq-733
title: "Test Script: Output Management (1LQ) (1LQ_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 1LQ: checking availability of output management and output control apps and configuration steps."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/output-management]
aliases: [1LQ_S4CLD2608_BPD_EN_XX]
keywords: [Output Management and External Output Systems, output management, output control, output management apps, output management configuration, output control configuration, email outbound, form templates, business roles, central business configuration]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1LQ_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-733
topic: 01-solution-foundation-and-platform/output-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Output Management (1LQ) (1LQ_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1LQ_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Output Management and External Output Systems** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Output Management (1LQ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232850296)

[2 Prerequisites 3](#_Toc232850297)

[2.1 System Access 3](#_Toc232850298)

[2.2 Roles 3](#_Toc232850299)

[2.3 Additional Manual Configuration 4](#_Toc232850300)

[3 Overview Table 5](#_Toc232850301)

[4 Test Procedures 7](#_Toc232850302)

[4.1 Check Availability of Output Management Apps 7](#_Toc232850303)

[4.2 Check Availability of Output Control Apps 8](#_Toc232850304)

[4.3 Check Availability of Output Management Configuration 9](#_Toc232850305)

[4.4 Check Availability of Output Control Configuration 11](#_Toc232850306)

## Purpose

This scope item provides best practice information for SAP S/4HANA output management that can be used to implement business scenarios that include output-related tasks. This focuses on the reuse of SAP S/4HANA output control service that is available for different business applications (such as billing document or purchase order). The reuse service offers different capabilities for output of business documents to business receivers. The features that are available in the context of the application are specific to that business application.

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
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Extensibility Specialist | SAP_BR_EXTENSIBILITY_SPEC | Extensibility / Extensibility | SAP_BR_EXTENSIBILITY_SPEC / SAP_CA_SPT_EXT_PC |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/edc3c25dd998caf2468718ae50960e55)

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Check Availability of Output Management Apps](#unique_7) [page ] 7 | Extensibility Specialist | Maintain Email Templates (F1306)Maintain Form Templates (F1434)Manage Logos (F2761)Manage Texts (F2894) | The apps are available and can be accessed. |
| [Check Availability of Output Control Apps](#unique_8) [page ] 8 | Administrator | Maintain Print Queues (F1260)Monitor Email Transmission (F5442)Manage Output Items (F2279)Output Parameter DeterminationAdobe Document Services Configuration (F4971) | The apps are available and can be accessed. |
| [Check Availability of Output Management Configuration](#unique_9) [page ] 9 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) or SAP Central Business Configuration | The following configuration steps are available and can be accessed:Define Allowed Email Receiver Domains For Email OutboundDefine Allowed Email Sender Domains For Email OutboundDefine Default Email Sender Address For Email Outbound |
| [Check Availability of Output Control Configuration](#unique_10) [page ] 11 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) or SAP Central Business Configuration | The following configuration steps are available and can be accessed:Assign Document Types for OutputAssign Email TemplatesAssign Form TemplatesAssign Output ChannelsDefine Business Rules for Output Parameter DeterminationDefine Output TypesDefine Output Settings for Document TypesDefine Rules for Determination of Master Form TemplateManage Application Object Type Activation |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Check Availability of Output Management Apps

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this test step, you're checking the availability of output management apps on SAP Fiori launchpad.

Procedure

| Test Step # | Test Step | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Extensibility Specialist. |  |  |
| 2 | Check Availability of Page | Check that the Output Management group is available on the Extensibility page. | The Output Management group appears on SAP Fiori launchpad. |  |
| 3 | Access the App | Open the Maintain Email Templates - Deprecated (F1306) app. | The Maintain Email Templates - Deprecated (F1306) app opens.You can ignore the error message. |  |
|  |  | Go back to the home page. |  |  |
| 4 | Access the App | Open the Maintain Form Templates (F1434) app. | The Maintain Form Templates (F1434) app opens.You can ignore the error message. |  |
|  |  | Go back to the home page. |  |  |
| 5 | Access the App | Open the Manage Logos (F2761) app. | The Manage Logos (F2761) app opens.You can ignore the error message. |  |
|  |  | Go back to the home page. |  |  |
| 6 | Access the App | Open the Manage Texts (F2894) app. | The Manage Texts (F2894) app opens.You can ignore the error message. |  |

### Check Availability of Output Control Apps

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this test step, you're checking the availability of output control apps on SAP Fiori launchpad.

Procedure

| Test Step # | Test Step | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Check Availability of Page | Check that the Output Management group is available on the Technical Monitoring page. | The Output Management page appears on SAP Fiori launchpad. |  |
| 3 | Access the App | Open the Maintain Print Queues (F1260) app. | The Maintain Print Queues (F1260) app opens. |  |
|  |  | Go back to the home page. |  |  |
| 4 | Access the App | Open the Monitor Email Transmissions (F5442) app. | The Monitor Email Transmissions (F5442) app opens. |  |
|  |  | Go back to the home page. |  |  |
| 5 | Access the App | Open the Manage Output Items (F2279) app. | The Manage Output Items (F2279) app opens. |  |
|  |  | Go back to the home page. |  |  |
| 6 | Access the App | Open the Output Parameter Determination app. | The Output Parameter Determination app opens. |  |
|  |  | Go back to the home page. |  |  |
| 7 | Access the App | Open the Adobe Document Services Configuration (F4971) app. | The Adobe Document Services Configuration (F4971) app opens. |  |

### Check Availability of Output Management Configuration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this test step, you’re checking that all configuration steps for the System Administration configuration item are available.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open the Manage Your Solution (F1241) app. | The Manage Your Solution (F1241) app opens. |  |
| 3 | Access the App | Open the Configure Your Solution app. | The Configure Your Solution app opens. |  |
| 4 | Search for Configuration Items | As application area, select Application Platform and Infrastructure. As sub application area, select Output Management. | The list displays the results. There are two items. One with item name Output Control and one with item name System Administration. |  |
| 5 | Access Configuration Item | Select the System Administration configuration item. | A list with configuration steps opens. |  |
| 6 | Check Configuration Step | For the Define Allowed Email Sender Domains For Email Outbound configuration step, select Configure. | The Define Allowed Email Sender Domains For Email Outbound activity opens. |  |
| 7 |  | Go back to the configuration steps overview. |  |  |
| 8 | Check Configuration Step | For the Define Default Email Sender Address for Email Outbound configuration step, select Configure. | The Define Default Email Sender Address for Email Outbound activity opens. |  |
| 9 |  | Go back to the configuration steps overview. |  |  |
| 10 | Check Configuration Step | For the Define Allowed Email Receiver Domains For Email Outbound configuration step, select Configure. | The Define Allowed Email Receiver Domains For Email Outbound activity opens. |  |

SAP Central Business Configuration:

| Test Step # | Test Step | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Check Define Email Sender Domain | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the activity: Define Allowed Email Sender Domains For Email Outbound.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Check Define Default Email Sender Address | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Default Email Sender Address For Email Outbound.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 4 | Check Define Email Receiver Addresses for Test Systems | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Allowed Email Receiver Domains For Email Outbound.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |

### Check Availability of Output Control Configuration

Purpose

In this test step, you’re checking that all configuration steps for the Output Control configuration item are available.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open the Manage Your Solution (F1241) app. | The Manage Your Solution (F1241) app opens. |  |
| 3 | Access the App | Open the Configure Your Solution app. | The Configure Your Solution app opens. |  |
| 4 | Search for Configuration Items | As application area, select Application Platform and Infrastructure. As sub application area, select Output Management. | The list displays the results. There are two items. One with item name Output Control and one with item name System Administration. |  |
| 5 | Access Configuration Item | Select the Output Control configuration item. | A list with configuration steps opens. |  |
| 6 | Check Configuration Step | For the Define Rules for Determination of Master Form Template configuration step, select Configure. | The Define Rules for Determination of Master Form Template activity opens. |  |
|  |  | Go back to the configuration steps overview. |  |  |
| 8 | Check Configuration Step | For the Assign Form Templates configuration step, select Configure. | The Assign Form Templates activity opens. |  |
|  |  | Go back to the configuration steps overview. |  |  |
| 10 | Check Configuration Step | For the Assign Email Templates configuration step, select Configure. | The Assign Email Templates activity opens. |  |
|  |  | Go back to the configuration steps overview. |  |  |
| 12 | Check Configuration Step | For the Assign Document Types for Output configuration step, select Configure. | The Assign Document Types activity opens. |  |
|  |  | Go back to the configuration steps overview. |  |  |
| 14 | Check Configuration Step | For the Define Output Settings for Document Types configuration step, select Configure. | The Define Output Settings for Document Types activity opens. |  |
|  |  | Go back to the configuration steps overview. |  |  |
| 16 | Check Configuration Step | For the Manage Application Object Type Activation configuration step, select Configure. | The Manage Application Object Type Activation activity opens. |  |

SAP Central Business Configuration:

| Test Step # | Test Step | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Check Define Rules for Determination of Master Form Template | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Rules for Determination of Master Form Template.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The activity is available.The documentation opens.You can access the activity in the SAP S/4HANA Cloud Public Edition system. |  |
| 3 | Check Assign Form Templates | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Form Templates.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to SAP S/4HANA Cloud Public Edition system. Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The activity is available.The documentation opens.You can access the activity in the SAP S/4HANA Cloud Public Edition system. |  |
| 4 | Check Assign Email Templates | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Email Templates.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The activity is available.The documentation opens.You can access the activity in the SAP S/4HANA Cloud Public Edition system. |  |
| 5 | Check Assign Document Types | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Document Types for Output.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The activity is available.The documentation opens.You can access the activity in the SAP S/4HANA Cloud Public Edition system. |  |
| 6 | Check Define Output Settings for Document Types | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Output Settings for Document Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The activity is available.The documentation opens.You can access the activity in the SAP S/4HANA Cloud Public Edition system. |  |

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
- related-to :: [[01-solution-foundation-and-platform/bp-cld-entpr-2608-forms-list-en-ae-134]]
- related-to :: [[01-solution-foundation-and-platform/test-script-integration-of-external-output-management-solution-7dj-120]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1LQ_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 23,088 chars in the whole document
