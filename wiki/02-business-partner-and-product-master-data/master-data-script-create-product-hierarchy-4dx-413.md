---
id: 02-business-partner-and-product-master-data/master-data-script-create-product-hierarchy-4dx-413
title: "Master Data Script: Create Product Hierarchy (4DX) (4DX_S4CLD2608_Master_Data_EN_XX)"
description: SAP S/4HANA Cloud Public Edition 2608 master data script (4DX) for configuring product hierarchy nodes and creating/activating a Product Hierarchy in Manage Product Hierarchies.
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-hierarchy]
aliases: [4DX_S4CLD2608_Master_Data_EN_XX]
keywords: [Product Hierarchies, product hierarchy, product hierarchy nodes, master data creation, business roles, sales orders, central business configuration, organizational units, 4DX]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4DX_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-413
topic: 02-business-partner-and-product-master-data/product-hierarchy
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Product Hierarchy (4DX) (4DX_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4DX_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Product Hierarchies** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Product Hierarchy (4DX) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904698)

[2 Prerequisites 3](#_Toc233904699)

[2.1 System Access 3](#_Toc233904700)

[2.2 Roles 3](#_Toc233904701)

[2.3 Required Organizational Units 4](#_Toc233904702)

[2.4 Mandatory and Optional Master Data 4](#_Toc233904703)

[2.5 Main Parameters for Data Creation 4](#_Toc233904704)

[2.5.1 Product Hierarchy Nodes 4](#_Toc233904705)

[2.6 Preliminary Steps 5](#_Toc233904706)

[2.6.1 Create Nodes for Product Hierarchies 5](#_Toc233904707)

[3 Overview Table 8](#_Toc233904708)

[4 Test Procedures 9](#_Toc233904709)

[4.1 Create Product Hierarchy 9](#_Toc233904710)

## Purpose

In this document you find a description of how to create Product Hierarchy master data for your SAP S/4HANA Cloud Public Edition system. The description includes those data segments that are relevant for the master data to work in a "usual" system environment. The reader mainly learns which data segments and fields usually need to be filled with input values. Fields that are not relevant for the scope of the SAP S/4HANA Cloud Public Edition content are not described in this document although they may display on the screen.

A Product Hierarchy master data that is created, can be used for assigning distribution chains with a Product Hierarchy, which in turn is used for further processing in Sales Orders.

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
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Required Organizational Units

Some segments of master data are dependent on the organizational units of the company. General (Central) Data does not depend on an organizational unit or the company code. The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| Sales Data | Plant, Sales Org, Distribution Channel | Tax Data, Item Category Group, Loading Group, and so on. |  | Plant:____________Sales Organization:____________Distribution Channel:______________ |

### Mandatory and Optional Master Data

Master data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a Product Hierarchymaster data record.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Product | In the Manage Product Hierarchies app, a hierarchy is assigned with multiple Product as leaf / end nodes. | Mandatory | When you assign product records created in the Manage Product Master Data app, as leaf nodes in Manage Product Hierarchies app, it provides completeness / business relevance to the hierarchy. |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a Product Hierarchymaster data record.

#### Product Hierarchy Nodes

The Self-Service Configuration UI (Configuration Step) available for Product, Configure Nodes for Product Hierarchies accessed by filtering Application Area for Database and Data Management should be maintained to be able to select or form the Hierarchy structure.

This Configuration provides option to create multiple node values and a description for each node.

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

### Preliminary Steps

#### Create Nodes for Product Hierarchies

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The entries created from the Self-Service Configuration step Configure Nodes for Product Hierarchies is a prerequisite for creating a Product Hierarchy.

|  |
| --- |
| Note This step is to be performed by the Configuration Expert user in usual business scenario. |

Procedure

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using your user credentials. | The Start page appears. |  |
| 2 | Open SAP Fiori App | In the Implementation Cockpit section, choose the Manage Your Solution (F1241). | A new page opens, showing the Manage Your Solution (F1241) screen.Note This application is part of Configuration Expert - Business Process Configuration role template. |  |
| 3 | Select Configure Your Solution | In the Manage Your Solution app, choose Configure Your Solution. | A new page opens, showing Configure Your Solution: Change Phase. |  |
| 4 | Select the Application Area | In Configure Your Solution application, select the filter for Application Area, and choose Database and Data Management option. | The number of entries shown in the result table is reduced to few records. |  |
| 5 | Select the Sub Application Area | In the Configure Your Solution app, select the filter for Sub Application Area, and choose Product option. | The number of records provided in the result list is reduced to one. |  |
| 6 | Product Configurations Steps | From the entries shown in table, choose on the record with Product as Sub Application Area.And then choose the section title Configuration Steps. | Section displays the list of multiple product configuration steps. |  |
| 7 | Configure Nodes for Product Hierarchy | In the Configuration Step Configure Nodes for Product Hierarchies, choose Configure. | The application page Product Hierarchy Subnode ID Maintenance opens. |  |
| 8 | Create New Entries | Choose New Entries. | Editable page opens for maintaining new Subnodes with title New Entries: Overview of Added Entries. |  |
| 9 | Enter New Subnodes | Provide multiple entries for Subnodes required in the target Product Hierarchy.For example, a <Drinks> Hierarchy could have:Here the Product Hierarchy Nodes could be <AERATED_DRINKS>, <NON_AERATED_DRINKS> and so on.The description for the Subnodes could be maintained as <Aerated Drinks>, <Non-Aerated Drinks> and so on. |  |  |
| 10 | Save the Entries | Choose Save on the bottom footer of the page. | The application page Product Hierarchy Subnode ID Maintenance reappears with the new entries provided. |  |
| 11 | Exit | Choose Exit and log off. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Configure Nodes for Product Hierarchies.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Create New Entries | Choose New Entries. | Editable page opens for maintaining new Subnodes with title New Entries: Overview of Added Entries. |  |
| 4 | Enter New Subnodes | Provide multiple entries for Subnodes required in the target Product Hierarchy.For example, a <Drinks> Hierarchy could have:Here the Product Hierarchy Nodes could be <AERATED_DRINKS>, <NON_AERATED_DRINKS> and so on.The description for the Subnodes could be maintained as <Aerated Drinks>, <Non-Aerated Drinks> and so on. |  |  |
| 5 | Save the Entries | Choose Save on the bottom footer of the page. | The application page Product Hierarchy Subnode ID Maintenance reappears with the new entries provided. |  |
| 6 | Exit | Choose Exit and log off. |  |  |

## Overview Table

This master record consists of several segments provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Segment | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Product Hierarchy](#unique_11) [page ] 9 | Master Data Specialist - Product Data | Manage Product Hierarchies (F4359) | Product Hierarchy Master Data record is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Product Hierarchy

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions on how to create a Product Hierarchy with Products assigned to the Hierarchy as end nodes. After activation of the Hierarchy, it can be consumed during the creation of Sales Orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using your user credentials. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Product Hierarchies (F4359). | The app opens. |  |
| 3 | Create Product Hierarchy | On the Manage Product Hierarchies screen, choose + (Create a new hierarchy). | The Create New Hierarchy screen displays. |  |
| 4 | Enter Product Hierarchy Data | On the Create New Hierarchy screen, make the following entries:Type: For example, <Product Hierarchy>.Hierarchy ID: For example, <DRINKS>.Hierarchy Description: For example, <Drinks Hierarchy>.Valid From: <Enter a date for the Hierarchy's validity to start from>Valid To: <Change the default date if required to have a time-dependent Hierarchy> |  |  |
| 5 | Choose Create | On the Create New Hierarchy screen, choose Create. | The Hierarchy list is filtered to show the newly created Product Hierarchy entry with the Status displayed as Draft. |  |
| 6 | Choose the New Product Hierarchy | In the Manage Product Hierarchies (F4359) app, choose the newly created Product Hierarchy with the Draft status listed in the result. | The structure of the Product Hierarchy displays in a tree table format. |  |
| 7 | Edit the Product Hierarchy | Choose Edit from the footer of the screen. | The screen displays in edit mode, allowing you to change values or add new nodes. |  |
| 8 | Add Nodes for the Root Node | Choose + (Add) for the first node. | The Add Node screen displays. |  |
| 9 | Choose Subnodes of the Root | On the Add Node screen, Subnode is selected by default.Enter data for the Node field. The values configured in the Preliminary Step [Create Nodes for Product Hierarchies](#unique_9) [page ] 5 can be used here.For example, <AERATED_DRINKS>, <NON_AERATED_DRINKS>, and so on.Note The value help can help you to select multiple nodes and assign them to the selected node of the Hierarchy.Choose OK. | The selected nodes are added as child nodes in the tree table structure for the root node of the Product Hierarchy. |  |
| 10 | Add Nodes to Subnodes | Choose + (Add) for the node to add further subnodes.For example, Choose + (Add) for the <NON_AERATED_DRINKS> node. | The Add Node screen displays. |  |
| 11 | Choose Nodes for Subnodes | On the Add Node screen, select further nodes from the value help to add as the subnodes of the <NON_AERATED_DRINKS> node (for example).Choose OK. | The selected nodes are added as child nodes in the tree table structure for the selected node of the Product Hierarchy. |  |
| 12 | Add Products to Hierarchy | Choose + (Add) for the node to add Products to Hierarchy. | The Add Node screen displays. |  |
| 13 | Choose Product | On the Add Node screen,choose Product. | On the Add Node screen, the input field changes to Product. |  |
| 14 | Assign Products to Hierarchy | On the Add Node screen, select entries in the Product field to assign the required Products to the Hierarchy node.Note The value help can help you to select multiple Products and assign them to the selected subnode of the Hierarchy. | The selected Products are assigned to the required subnode of the Product Hierarchy. |  |
| 15 | Save the Product Hierarchy | Choose Save. | The changes are saved. |  |
| 16 | Activate the Product Hierarchy | Choose Activate. | The Product Hierarchy is activated, and the Status changes from Draft to Active. |  |

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
- related-to :: [[02-business-partner-and-product-master-data/4dx-415]]
- related-to :: [[02-business-partner-and-product-master-data/4dx-417]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-dados-mestre-criar-hierarquia-de-produtos-4dx-416]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-datos-maestros-crear-jerarquia-de-productos-4dx-414]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4DX_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 18,158 chars in the whole document
