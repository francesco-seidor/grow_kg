---
id: 14-maintenance-service-and-projects/create-measuring-point-mds-5mi-467
title: Create Measuring Point - MDS (5MI) (5MI_S4CLD2608_Master_Data_EN_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (5MI): configure measuring point category and create measuring points and counters in Maintenance Management."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/measuring-points-and-counters]
aliases: [5MI_S4CLD2608_Master_Data_EN_XX]
keywords: [Measuring Points and Counters, measuring point, measuring counter, measuring point category, condition based maintenance, master data scripts, business roles, maintenance management, 5MI]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MI_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-467
topic: 14-maintenance-service-and-projects/measuring-points-and-counters
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create Measuring Point - MDS (5MI) (5MI_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MI_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Measuring Points and Counters** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Measuring Point - MDS (5MI) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904773)

[2 Prerequisites 3](#_Toc233904774)

[2.1 System Access 3](#_Toc233904775)

[2.2 Roles 3](#_Toc233904776)

[2.3 Required Organization Units 3](#_Toc233904777)

[2.4 Mandatory and Optional Master Data 4](#_Toc233904778)

[2.5 Main Parameters for Data Creation 4](#_Toc233904779)

[2.5.1 Measuring Point Category 4](#_Toc233904780)

[3 Overview Table 7](#_Toc233904781)

[4 Procedure 8](#_Toc233904782)

[4.1 Create Measuring Point 8](#_Toc233904783)

[4.2 Create Measuring Counter 9](#_Toc233904784)

## Purpose

In this document, you can find a description of how to create a measuring point master data record for your S/4HANA system. The description includes those data segments that are relevant for the master data to work in a "usual" system environment. The reader mainly learns which data segments and fields usually need to be filled with input values. Fields that are not relevant for the scope of the S/4HANA content delivery by SAP Best Practices are not described in this document although they may appear on the user interface (UI).

## Prerequisites

This section summarizes all prerequisites for creating measuring point.

### System Access

The test should be conducted with the following system:

Table 1:

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Space) | ID (Space) |
| --- | --- | --- | --- |
| Master Data Specialist - Maintenance Management | SAP_BR_MD_SPECIALIST_EAM | Master Data - Maintenance Management | SAP_EAM_SPT_MD_SPECIALIST_PC |

### Required Organization Units

Some segments of master data are dependent on the organizational units of the company. General (central) data does not depend on an organizational unit or the company code. The following table gives an overview of different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

### Mandatory and Optional Master Data

Measuring Point data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a measuring point.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Technical Object |  | Mandatory | Equipment or Functional location. |
| Characteristic |  | Mandatory | Characteristics describe the properties of objects. The values of a characteristic specify the properties. |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a measuring point.

#### Measuring Point Category

The measuring point category determines which data can be maintained in the master record for the measuring point. Measuring points are distinguished in the system by measuring point category. Each measuring point category is identified by a key, which is the first thing you assign to the measuring point when you create it in the system.

Table 2:

| Measuring Point Category | Description |
| --- | --- |
| M | MeasPoint (general) |

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to configure the measuring point category.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version.Select the Application Area as Asset ManagementSelect the Sub Application Area as Maintenance ManagementSelect the row with the item name: Master Data | Configure Your Solution screen is displayed. |  |
| 4 | Open Define Measuring Point Categories | Under Configuration Steps, select the step name "Define Measuring Point Categories" and click on Configure | Measuring Point categories screen will be displayed |  |
| 5 | Enable conditions for CBM (optional) | Select the Measuring Point Category “M”Enter MeasRange Message as “W”Tick the Checkbox for Create NotificationsClick on Save | Conditions for CBM has been established |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Implementation Activities | The Manage Your Solution screen is displayed. |  |
| 3 | Access Configuration | To locate the activity in the tree view, click on search icon and select the extended Search optionEnter the Node Text/Activity Description: "Define Measuring Point Categories" and click on continue | The Activity in Tree View is displayed. |  |
| 4 | Open Define Measuring Point Categories | Under Configuration Steps, select the step name "Define Measuring Point Categories" and click on Configure | Measuring Point categories screen will be displayed |  |
| 5 | Enable conditions for CBM (Optional) | Select the Measuring Point Category “M”Enter MeasRange Message as “W”Tick the Checkbox for Create NotificationsClick on Save | Conditions for CBM has been established |  |

## Overview Table

This scope item consists of several process steps that are listed in the table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Measuring Point](#unique_10) [page ] 8 | SAP_BR_MD_SPECIALIST_EAM | Create Measuring Point (EAMS_WDA_MP_OIF) app | Measuring point is created. |

## Procedure

This section describes procedures for each process step that belongs to this scope item. You can use these procedures also for testing the master data creation.

### Create Measuring Point

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data specialist SAP_BR_MD_SPECIALIST_EAM. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the Create Measuring Point (EAMS_WDA_MP_OIF) app. | A new window opens, showing the Create Measuring point screen. |  |
| 3 | Enter Details | Enter the following:Measuring Point/Counter: <Measuring Point>Reference Object Type: <Technical object> | A new screen appears displaying the reference object. |  |
| 4 | Enter Reference Object details | Enter the following:Technical Object:<Equipment/Floc No>Press Enter or choose Continue. | Create Measuring Point |  |
| 5 | General Data | On the General Data section, enter the following:Description: <Description of Measuring Point>Characteristic: For example, OPERATING_HOUR/PRESSUREMeasuring Point Category: M (MeasPoint General) |  |  |
| 6 | Enter Target Limits and Counter Data | On the Target Limits and Counter Data section, enter the following:Target Value: For example, 10 PAUpper Range Limit: For example, 15 PALower Range Limit: For example, 5 PA |  |  |
| 7 | Enter Measurement Tolerance (Optional) | On the Measurement Tolerance Section, enter the following:Upper Measurement Tolerance: For example, 12 PALower Measurement Tolerance: For example, 7 PA |  |  |
| 8 | Maintain Condition (Only for Condition Based Maintenance) | On the Maintain Condition Section,Click the Checkbox for Enable condition, select any condition : For example, For condition : MEASUREMENT READING > UPPER LIMITEnter the following detailsObject type (notification type) : For example, Reactive WorkPriority : Select the Priority required for the notification to be created, For Example 1 Very HighActive: Click the checkbox to make this Condition activeLong Text: Enter the Long Text for the notification to be createdDescription: Enter the description for the notification to be created |  |  |
| 9 | Check Entries | Choose Check Entries. | The entries are checked. |  |
| 10 | Save your data | Save your entries. | measuring point is created. |  |

### Create Measuring Counter

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data specialist SAP_BR_MD_SPECIALIST_EAM. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the Create Measuring Point (EAMS_WDA_MP_OIF) app. | A new window opens, showing the Create Measuring point screen. |  |
| 3 | Enter Details | Enter the following:Measuring Point/Counter: <Counter>Reference Object Type: <Technical object> | A new screen appears displaying the reference object. |  |
| 4 | Enter Reference Object | Enter the following:Technical Object: <Equipment/Floc No>Press Enter or choose Continue. | Create Measuring Point (Counter) screen opens. |  |
| 5 | Enter General Data | On the General Data section, enter the following:Description: <Description of Measuring Counter>Measuring Point Category: M (MeasPoint General)Characteristic: For example, OPERATING_HOUR/PRESSURE | General Data are Maintained |  |
| 6 | Enter Target Limits and Counter Data | On the Target Limits and Counter Data section, enter the following:Overflow Reading: <Counter Overflow Reading>Annual Estimate: <Annual Estimate of Tech Object>Measurement Range Unit | Target Limits are maintained |  |
| 7 | Check Entries | Choose Check Entries. | The entries are checked. |  |
| 8 | Save your data | Save your entries. | measuring point is created. |  |

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
- related-to :: [[14-maintenance-service-and-projects/5mi-469]]
- related-to :: [[14-maintenance-service-and-projects/crear-punto-de-medicion-mds-5mi-468]]
- related-to :: [[14-maintenance-service-and-projects/criar-ponto-de-medicao-mds-5mi-470]]
- related-to :: [[14-maintenance-service-and-projects/mds-5mi-471]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MI_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 15,054 chars in the whole document
