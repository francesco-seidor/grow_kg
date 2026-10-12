---
id: 06-management-accounting/master-data-script-create-activity-type-and-activity-type-hierarchy-bn
title: Master Data Script - Create Activity Type and Activity Type Hierarchy (BNN) (BNN_S4CLD2608_Master_Data_EN_XX)
description: "English SAP master data script BNN for creating activity types and activity type hierarchies in Controlling, with change log and where-used analytics, release 2608."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/activity-types]
aliases: [BNN_S4CLD2608_Master_Data_EN_XX]
keywords: [Activity Types and Activity Type Hierarchies, activity types, activity type hierarchy, cost center planning, change log, where-used list, master data scripts, controlling area, secondary cost elements, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNN_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-641
topic: 06-management-accounting/activity-types
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script - Create Activity Type and Activity Type Hierarchy (BNN) (BNN_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNN_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Activity Types and Activity Type Hierarchies** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Activity Type and Activity Type Hierarchy - MDS (BNN) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904986)

[2 Prerequisites 3](#_Toc233904987)

[2.1 System Access 3](#_Toc233904988)

[2.2 Roles 3](#_Toc233904989)

[2.3 Required Organizational Units 3](#_Toc233904990)

[2.4 Mandatory and Optional Master Data 4](#_Toc233904991)

[2.5 Main Parameters for Data Creation 4](#_Toc233904992)

[2.6 Preliminary Steps 4](#_Toc233904993)

[2.6.1 User Settings - Set Controlling Area 4](#_Toc233904994)

[3 Overview Table 5](#_Toc233904995)

[4 Test Procedures 6](#_Toc233904996)

[4.1 Creating Activity Type Master Data 6](#_Toc233904997)

[4.2 Creating Activity Type Hierarchy Master Data 7](#_Toc233904998)

[4.3 Analytics 8](#_Toc233904999)

[4.3.1 Activity Type Change Log 8](#_Toc233905000)

[4.3.2 Where-Used List - Activity Types 9](#_Toc233905001)

## Purpose

Activity types represents the activities produced by a cost center within a controlling area. Activity types are uses to plan and allocate activities recorded and measured in activity units. Activity quantities are valuated using an activity price which is maintained on the cost center.

Activity types are used as follows:

To determine the quantity-based output of a cost center. The plan activity quantities of production and service cost centers must be reconciled with the master production schedule in logistics. This determines the required plan activity quantity, as well as the plan capacity.

To control the activity quantities on the cost centers. This enables the measurement of the operating rate or the rate of capacity utilization of a cost center.

In addition to manual planning of activity quantities, you can also use indirect activity allocation to plan activity quantities automatically.

Activity type hierarchies are also useful in planning. Since there is no multiple selection tool available for activity types, activities can be collected in activity type hierarchies to enable planning of several activity types at one time.

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
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |

### Required Organizational Units

The organizational structure and master data of your company was created in your ERP system during implementation. The organizational structure reflects the structure of your company. The master data represents activity types and activity type hierarchies, depending on the operational focus of your company.

| Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Controlling Area | General Data | Mandatory |  |

### Mandatory and Optional Master Data

Default Values

The organizational structure and master data of your company was created in your ERP system during implementation. The organizational structure reflects the structure of your company. The master data depending on the operational focus of your company.

The business process is enabled with this organization-specific master data, examples are provided in the next section.

Activity type and an activity type hierarchy records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in an activity type data record.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Cost Element | General Data | Mandatory | Secondary cost element (cost element type ‘43’) |
| G/L Account |  | Mandatory | For Secondary cost element (cost element type ‘43’) |

### Main Parameters for Data Creation

This scope item has no business conditions.

### Preliminary Steps

#### User Settings - Set Controlling Area

| Step # | Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Choose Settings | Under the user context menu, choose Settings. | The User Setings window appears. |  |
| 3 | Choose Default Values | Choose Default Values on the window. | The Default Values window appears. |  |
| 4 | Enter Data | In the CO Area field, enter <CO area value>, then choose Save. | Controlling area, for example, A000, is set for your user. |  |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction | Expected Results |
| --- | --- | --- | --- |
| [Creating Activity Type Master Data](#unique_10) [page ] 6 | Cost Accountant - Overhead | Manage Activity Types (F1605A) | Activity types can be created according to new business requirements. |
| [Creating Activity Type Hierarchy Master Data](#unique_11) [page ] 7 | Cost Accountant - Overhead | Manage Global Hierarchies (F2918) | Activity type hierarchies can be created according to new business requirements. |
| [Activity Type Change Log](#unique_12) [page ] 8 | Cost Accountant - Overhead | Change Log - Activity Types (F3866) |  |
| [Where-Used List - Activity Types](#unique_13) [page ] 9 | Cost Accountant - Overhead | Manage Activity Types (Version 2) (F1605A) |  |

## Test Procedures

This section describes procedures for each process step that belongs to this scope item. You can use these procedures also for testing the master data creation.

### Creating Activity Type Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Activity Types (F1605A). | The app opens. |  |
| 3 | Choose Create | Choose Create. |  |  |
| 4 | Enter Activity Type Data | On the New Activity Type: New screen, on the General Data tab, make the following entries:Enter Activity Type: Description TextActivity Unit: <Activity unit>Name: <Name>Activity Type description: <Enter a description>Valid From: <Current date>Valid To: <Year-end date>Cost center category: <Cost center category>Activity Type Category: <Activity type category>Allocation Cost Element: For example, 94304000.Price Indicator: <Price indicator> | The General Data section and various tabs display.Note You can find the SAP-recommended values for SAP S/4HANA Cloud Public Edition (as others though visible might not be supported) below:Activity type category: only 1 (manual entry and manual allocation) is supported.Price indicator: only 3 (price is set manually) is supported.Actual activity type category: should be blank.Actual price indicator: should be blank by default. Only if you have activated scope item 33Q - Actual Costing, you should use 5 or 7 (for details about those two values, you may refer to the section in the test script of 33Q). |  |
| 5 | Save Your Data | Choose Create. | The activity type is created and saved. |  |

### Creating Activity Type Hierarchy Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

You have filled out and saved the basic data for the material as described in [Creating Activity Type Master Data](#unique_10) [page ] 6.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Global Hierarchies (F2918). | The app opens. |  |
| 3 | Choose Create | In the Hierarchy List section, choose Create. | The New Hierarchy screen displays. |  |
| 4 | Enter New Activity Type Hierarchy | On the New Hierarchy screen, make the following entries and select Create:Type: Activity Type HierarchyHierarchy ID: <Any ID up to 10 characters>Caution The total length of hierarchy ID and node ID cannot exceed 14 characters.Controlling Area: A000Hierarchy Description: <Any description> |  |  |
| 5 | Edit New Activity Type Hierarchy | On the Hierarchy List screen, select the detail icon > and select Edit for your newly-created Activity Type Hierarchy.Select the newly-created Activity Type Hierarchy, choose More on the right side of the screen, and then choose Fast Entry.On the Fast Entry screen, select Activity Type and make the following entry:ID: <Select the activity type(s) you want to add using the search function>Select OK when you finish and select Save.Go back to the Activity Type Hierarchy screen and select Activate. | The newly-created Activity Type Hierarchy is now activated. |  |

### Analytics

#### Activity Type Change Log

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the change log for activity types.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Change Log - Activity Types (F3866). | The Change Log – Activity Types dialog box displays. |  |
| 3 | Selection Criteria | Make the following entries:Activity Type: <Any Activity type> |  |  |
| 4 | Choose | Choose Go. | A report showing change detail history displays. |  |

#### Where-Used List - Activity Types

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity allows you to see where activity types are used in other master data such as profit centers, and actual cost allocations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Activity Types (Version 2) (F1605A). | The app opens. |  |
| 3 | Selection Criteria | Make the following entries:Activity Type: <Any Activity type> |  |  |
| 4 | Where Used | Select the desired cost center and choose Where Used – Activity Types. | A report showing where activity types are currently used is displayed. For de­ tails, you can select the Master data object type and drill in further. |  |

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
- related-to :: [[06-management-accounting/criar-tipo-de-atividade-e-hierarquia-de-tipo-de-atividade-mds-bnn-644]]
- related-to :: [[06-management-accounting/leistungsart-und-leistungsartenhierarchie-anlegen-sds-bnn-640]]
- related-to :: [[06-management-accounting/mds-bnn-643]]
- related-to :: [[06-management-accounting/mds-bnn-645]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNN_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 15,831 chars in the whole document
