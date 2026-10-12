---
id: 01-solution-foundation-and-platform/test-script-responsibility-management-1nj-746
title: "Test Script: Responsibility Management (1NJ) (1NJ_S4CLD2608_BPD_EN_XX)"
description: "S/4HANA Cloud test script for scope item 1NJ: creating teams, team hierarchies, responsibility rules, contexts and team categories in Fiori apps."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/responsibility-management-and-situation-handling]
aliases: [1NJ_S4CLD2608_BPD_EN_XX]
keywords: [Responsibility Management and Situation Handling, responsibility management, team creation, team hierarchy, responsibility rules, responsibility contexts, custom context, team categories, test scripts, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1NJ_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-746
topic: 01-solution-foundation-and-platform/responsibility-management-and-situation-handling
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Responsibility Management (1NJ) (1NJ_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1NJ_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Responsibility Management and Situation Handling** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Responsibility Management (1NJ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc234353093)

[2 Prerequisites 3](#_Toc234353094)

[2.1 Additional Manual Configuration 3](#_Toc234353095)

[2.2 System Access 3](#_Toc234353096)

[2.3 Roles 3](#_Toc234353097)

[3 Overview Table 4](#_Toc234353098)

[4 Test Procedures 5](#_Toc234353099)

[4.1 Create Team 5](#_Toc234353100)

[4.2 Maintain Hierarchy Across Teams 7](#_Toc234353101)

[4.3 Create Rules 8](#_Toc234353102)

[4.4 Extend Context and Map Rules 9](#_Toc234353103)

[4.5 Create Custom Context 11](#_Toc234353104)

[4.6 Create Custom Team Category 12](#_Toc234353105)

## Purpose

Overview

As we move toward an intelligent enterprise, intelligent systems need to determine agents who are automatically notified about events and who are responsible for business processes and objects. It is essential to define and manage these responsibilities, including authorizations for various contexts, and retrieve the correct contacts who can react to tasks and activities. Responsibility Management provides the Teams concept through which you can group responsible members with appropriate definitions for responsibilities. These members are assigned functions that uniquely describe the nature of their work. Functions and responsibility definitions help as a selection criterion for refining agent determination. With this scope item you can configure function, function profile, custom responsibility definitions, and team types for Responsibility Management.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/1c912c48000036fc064078edd9caee7c)

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
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Extensibility Specialist | SAP_BR_EXTENSIBILITY_SPEC | Extensibility / Extensibility | SAP_BR_EXTENSIBILITY_SPEC / SAP_CA_SPT_EXT_PC |  |

|  |
| --- |
| Note For on-premise, for the SAP_WFRT/WF_BATCH technical user, assign the same authorization objects as that of the Business Process Specialist business role additionally. |

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Team](#unique_7) [page ] 5 | Business Process Specialist | Manage Teams and Responsibilities - Procurement (F2412) | A team is created. |
| [Maintain Hierarchy Across Teams](#unique_8) [page ] 7 | Business Process Specialist | Manage Teams and Responsibilities - Procurement (F2412) | Teams are maintained in hierarchy. |
| [Create Rules](#unique_9) [page ] 8 | Extensibility Specialist | Manage Responsibility Rules (F4637) | A rule is created. |
| [Extend Context and Map Rules](#unique_10) [page ] 9 | Extensibility Specialist | Manage Responsibility Contexts (F4636) | Rules are mapped to an extended context. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Team

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create the teams as Responsible.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as Business Process Specialist. |  |  |
| 2 | Access App | Open Manage Teams and Responsibilities - Procurement (F2412). | The Teams list page is displayed. |  |
| 3 | Create New Team | Choose Create.Note You can also copy teams from the existing team list. |  |  |
| 4 | Maintain General Information | On the Team screen, there are four facets:Team InformationResponsibility DefinitionsTeam OwnersTeam MembersIn the Team Information section, enter the following values:NameGlobal IDTypeDescriptionStatusCategoryChoose the status as Enabled or Disabled.The Type and Category values can be selected from the value help.Note On selecting the type, category is generated automatically.Now, you have entered new team information. | New team is created. |  |
| 5 | Maintain Responsibility Definition Values for Generated Attributes | On selecting the type, Responsibility Definitions are populated and values can be maintained by the user.Note This is an optional step. |  |  |
|  | Maintain Team Owner | The business process specialist can change or add team owners.Note If the business process specialist (who is creating the team) has a business user, this business process specialist is then defaulted as team owner. |  |  |
| 6 | Maintain Team Member | In the Team Members section, choose Create. Then either enter the business partner, or select one or more business partners.Choose the relevant function value from F4 help for all business partners.Assign the functions to multiple business partners using Manage Functions.Then choose Create on the lower right. |  |  |

### Maintain Hierarchy Across Teams

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create the teams as Responsible.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as Business Process Specialist. |  |  |
| 2 | Access App | Open Manage Teams and Responsibilities - Procurement (F2412). | The Teams list page is displayed. |  |
| 3 | Maintain Hierarchy | There are two ways of maintaining teams in hierarchies:Maintaining a hierarchy of already-created teamsCreating a new subteam for a team |  |  |
| 4 | Maintaining Hierarchy of Already-Created Teams | Select a team from the teams list page and choose Show Hierarchy.You’re navigated to another list, which shows the selected team in a hierarchical format.Select the team and choose Manage Sub Teams. A list of current and potential subteams is displayed.Add subteams by toggling the yes/no button.Choose OK. |  |  |
| 5 | Creating New Subteam for a Team | Choose a team for which you want to create a subteam. You’re navigated to the team details page.Choose Create Subteam.Enter the required details and choose Save.After saving the subteam, choose Show Hierarchy to view the hierarchy of the teams created. |  |  |

### Create Rules

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a responsibility rule.

Prerequisite

Create a BAdI implementation with the BAdI filter value same as the responsibility rule ID. For more information, refer to the [Set-up instructions](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/Setup/1NJ_Set-Up_EN_XX.pdf).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as Extensibility Specialist. |  |  |
| 2 | Access App | Open Manage Responsibility Rules (F4637). | The Rules list page is displayed. |  |
| 3 | Choose Custom Rule Tab | Choose the Custom Rule tab. |  |  |
| 4 | Create Rules | Choose Create.Note You can also copy an existing standard or custom rule. |  |  |
| 5 | Maintain General Information | On the Rule screen, there are two facets:General InformationParametersIn the General Information section, enter the following values:IDDescriptionNoteUpon maintaining the rule ID, BAdI filter is defaulted to Rule ID.If the system is ATO-enabled, the ATO prefix is appended to the rule ID upon saving. |  |  |
| 6 | Maintain Parameters | In the Parameters section, enter the following values:NameDescriptionTypeCDS ViewCDS FieldsChoose the type from the following options:ElementStructureTableChoose Save. |  |  |

### Extend Context and Map Rules

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you extend a context and map it to a Responsibility Rule.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as Extensibility Specialist. |  |  |
| 2 | Access App | Open Manage Responsibility Contexts (F4636). | The Contexts list page is displayed. |  |
| 3 | Extend Standard Context | Select a Standard Responsibility Context from the list page.Choose Extend. |  |  |
| 4 | Maintain General Information | On the Context screen, there are three facets:General InformationTeam CategoryAgent RuleIn the General Information section, the standard context ID Is automatically populated either with the ATO prefix or Z_. The ID can be changed.Note Team Category is populated automatically from Parent Context. |  |  |
| 5 | Maintain Agent Rules | On the Agent Rule screen, there are two facets:General InformationRule Parameter MappingIn the General Information section, enter the following values:IDDescriptionResponsibility Rule ID (custom)In the Rule Parameter Mapping section, enter the following values:NameDescriptionData SourceValue (text value)Note After entering Responsibility Rule ID, Name and Description are populated automatically.Enter either a Data Source or Value parameter.Choose Apply and Save. |  |  |

### Create Custom Context

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a context and map it to a team category and/or a Responsibility Rule.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as Extensibility Specialist. |  |  |
| 2 | Access App | Open Manage Responsibility Contexts (F4636). | The Contexts list page is displayed. |  |
| 3 | Create Custom Context | Navigate to the Custom tab, and choose Create. |  |  |
| 4 | Maintain General Information | On the Context screen, there are three facets:General InformationTeam CategoryAgent RuleIn the General Information section, the ATO prefix is automatically populated. You can add an ID that starts with the ATO prefix. |  |  |
| 5 | Maintain Team Category | Choose Create, and select the team category that you want to map to the custom context. |  |  |
| 6 | Maintain Agent Rules | On the Agent Rule screen, there are two facets:General InformationRule Parameter MappingIn the General Information section, enter the following values:IDDescriptionResponsibility Rule ID (custom)Data SourceIn the Rule Parameter Mapping section, enter the following values:NameDescriptionData SourceValue (text value)Enter either a Data Source or Value parameter.Choose Apply and Save. |  |  |

### Create Custom Team Category

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a custom team category.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as Extensibility Specialist. |  |  |
| 2 | Access App | Open Manage Team Categories (F6616). | The team category list page is displayed. |  |
| 3 | Create Custom Team Category | Choose Create and enter the team category ID in the pop-up. |  |  |
| 4 | Maintain General Information | On the Team Category screen, there is one facet:General InformationIn the General Information section, the ID field is automatically populated with the ID entered in initial pop-up. You can manually change the ID value. Enter the team category description, and select Create. | The team category is created. |  |

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
- related-to :: [[01-solution-foundation-and-platform/test-script-situation-handling-31n-sap-s-4hana-cloud-public-edition-89]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1NJ_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 18,493 chars in the whole document
