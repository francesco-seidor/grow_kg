---
id: 14-maintenance-service-and-projects/create-maintenance-work-center-mds-5mh-461
title: Create Maintenance Work Center - MDS (5MH) (5MH_S4CLD2608_Master_Data_EN_XX)
description: "SAP Best Practices master data script for creating a plant maintenance work center (CR01) in S/4HANA Cloud Public Edition 2608, with step-by-step test procedure."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/maintenance-work-centers]
aliases: [5MH_S4CLD2608_Master_Data_EN_XX]
keywords: [Maintenance Work Centers, maintenance work center, work center category, master data creation, business roles, standard value key, work center capacity, work center costing, test procedures, 5MH]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MH_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-461
topic: 14-maintenance-service-and-projects/maintenance-work-centers
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create Maintenance Work Center - MDS (5MH) (5MH_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MH_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Maintenance Work Centers** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Maintenance Work Center - MDS (5MH) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904783)

[2 Prerequisites 3](#_Toc233904784)

[2.1 System Access 3](#_Toc233904785)

[2.2 Roles 3](#_Toc233904786)

[2.3 Required Organizational Units 3](#_Toc233904787)

[2.4 Mandatory and Optional Master Data 4](#_Toc233904788)

[2.5 Main Parameters for Data Creation 4](#_Toc233904789)

[2.5.1 Work Center Category 4](#_Toc233904790)

[3 Overview Table 5](#_Toc233904791)

[4 Procedure 6](#_Toc233904792)

[4.1 Create Maintenance Work Center 6](#_Toc233904793)

## Purpose

In this document you find a description of how to create a maintenance work center master data record for your S/4HANA system. The description includes those data segments that are relevant for the master data to work in a "usual" system environment. The reader mainly learns which data segments and fields usually need to be filled with input values. Fields that are not relevant for the scope of the S/4HANA content delivery by SAP Best Practices are not described in this document although they may appear on the user interface (UI).

A maintenance work center master record that is created as described here can be used for maintenance processes.

## Prerequisites

This section summarizes all prerequisites for creating a work center.

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
| Production Engineer - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC | Production Engineering - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |

### Required Organizational Units

Some segments of master data are dependent on the organizational units of the company, General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| All data | Plant |  | All the data for work center depends on plant. | Plant: –––––-- |

### Mandatory and Optional Master Data

Work center data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in an work center.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Standard value key | In the work center screen, Basic Data tab, you find the entry of standard value key in standard value Maintenance section. | Mandatory | The system uses standard values as parameters with origin standard value in formulas to calculate execution time, capacity requirements and costs. You use the standard value key to assign a parameter ID to standard values. This parameter ID identifies the standard value in a formula. You can use the parameter ID to determine the key word for a standard value, such as setup, machine or labor. |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a maintenance work center:

#### Work Center Category

The work center category determines which data can be maintained in the master record for the work center. The work centers can be distinguished by their category (for example, production work center, maintenance work center, service work center, and so on.)

Table 2:

| Work Center Category | Description |
| --- | --- |
| 0005 | Plant Maintenance |

## Overview Table

This scope item consists of several process steps that are listed in the table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Maintenance Work Center](#unique_10) [page ] 6 | SAP_BR_PRODN_ENG_DISC | Create Work Center (CR01) | Work center is created. |

## Procedure

This section describes procedures for each process step that belongs to this scope item. You can use these procedures also for testing the master data creation.

### Create Maintenance Work Center

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a SAP_BR_PRODN_ENG_DISC. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Work Center (CR01). | A new window opens showing the Create Work Center: Initial Screen. |  |
| 3 | Enter Plant Code | Enter the Plant Code: <1010> | The Create Organization screen is displayed. |  |
| 4 | Enter Work Center ID | Enter the Work Center ID: <RES-0100>Note The field length of work center ID is less than 8. |  |  |
| 5 | Work Center category | Choose work center category: <0005 > Plant Maintenance |  |  |
| 6 | Choose Basic Data | Choose Basic Data button on the top left corner of the screen. | The create work center: basic data screen appears. |  |
| 7 | Enter Work Center Description, Select Person Responsible, Usage and Standard Value Key | On the Basic Data tab, enter the following data:Description: for example, RES-0100Person responsible: for example, <YMM> Plant Maintenance Mech SupervisorUsage: for example, <004> Only Maintenance Task ListsStandard value key: for example, <SAP0> No Standard Values |  |  |
| 8 | Enter Control Key | Choose Default Values tab, enter the following data:Control Key: for example, <YBM1> Plant Maintenance-Internal. |  |  |
| 9 | Set Up the Capacity and Other Formulas | On the Capacities tab, enter the following data:Capacity Category: for example, <002> PersonOther Formula: for example, <YBPM01> Proj:RqmtsNetwkMai | Choose Enter. The Create Work Center Capacity: Header screen appears. |  |
| 10 | Set Up Work Center Capacity | In the Work Center Capacity: Header section, enter the following data:Capacity Category Description: for example, Mechanics CapacityCapacity Responsible: for example, <A> Planner Group AFactory Calendar: ID Calendar for your country for example, <01> Germany (Standard)Capacity Base Unit: for example, <H> HourStart Time: for example, <06:00:00>End Time: for example, <14:30:00>Length of breaks: for example, <00:30:00>Capacity Utilization: for example, <100>No. Ind. Capacities: for example, <10>Long Term Planning: <X> | Choose Enter. The screen goes back to capacity overview. |  |
| 11 | Enter Scheduling Data | On the Scheduling tab, enter the following data:Capacity Category: for example, <002> Person |  |  |
| 12 | Enter Costing Data | On the Costing tab page, enter the following data:Start date: for example, <01/01/2015>Cost center: for example, < 10101701> Plant & Maint (DE)Activity type int. processing: for example, <11> Personnel HoursFormula key for costing: for example, <YBPM01> Proj:RqmtsNetwkMaint |  |  |
| 13 | Save your Data | Save your entries | The entries are saved. |  |

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
- related-to :: [[14-maintenance-service-and-projects/criar-centro-de-trabalho-de-manutencao-mds-5mh-464]]
- related-to :: [[14-maintenance-service-and-projects/mds-5mh-463]]
- related-to :: [[14-maintenance-service-and-projects/mds-5mh-465]]
- related-to :: [[14-maintenance-service-and-projects/script-de-datos-maestros-crear-puesto-de-trabajo-de-mantenimiento-mds]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MH_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 11,361 chars in the whole document
