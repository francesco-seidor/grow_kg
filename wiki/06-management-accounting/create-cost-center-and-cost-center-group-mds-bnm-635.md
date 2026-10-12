---
id: 06-management-accounting/create-cost-center-and-cost-center-group-mds-bnm-635
title: Create Cost Center and Cost Center Group - MDS (BNM) (BNM_S4CLD2608_Master_Data_EN_XX)
description: "SAP S/4HANA Cloud 2608 master data script for creating cost centers and cost center groups (global hierarchy or set-based), plus where-used analytics."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/cost-centers-and-groups]
aliases: [BNM_S4CLD2608_Master_Data_EN_XX]
keywords: [Cost Centers and Cost Center Groups, cost centers, cost center groups, standard hierarchy, global hierarchies, where-used list, business roles, master data prerequisites, master data integration, public sector management]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNM_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-635
topic: 06-management-accounting/cost-centers-and-groups
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create Cost Center and Cost Center Group - MDS (BNM) (BNM_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNM_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Cost Centers and Cost Center Groups** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Cost Center and Cost Center Group - MDS (BNM) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233905003)

[2 Prerequisites 3](#_Toc233905004)

[2.1 System Access 3](#_Toc233905005)

[2.2 Roles 3](#_Toc233905006)

[2.3 Required Organizational Units 3](#_Toc233905007)

[2.4 Mandatory and Optional Master Data 4](#_Toc233905008)

[2.5 Main Parameters for Data Creation 4](#_Toc233905009)

[3 Overview Table 5](#_Toc233905010)

[4 Test Procedures 6](#_Toc233905011)

[4.1 Creating Cost Center Master Data 6](#_Toc233905012)

[4.2 Creating Cost Center Group Master Data 8](#_Toc233905013)

[4.3 Analytics 10](#_Toc233905014)

[4.3.1 Where-Used List - Cost Centers Actual 10](#_Toc233905015)

[5 Appendix 12](#_Toc233905016)

[5.1 Cost Center Replication from SAP S/4HANA Cloud Public Edition to SAP Master Data Integration (Optional) 12](#_Toc233905017)

## Purpose

Cost centers represent organizational unit areas of responsibility to which financial costs can be assigned. Dividing an organization into cost centers allows you to follow several goals.

Assigning costs to cost centers lets you determine where costs are incurred within the organization.

If you plan costs at cost-center level, you can check cost efficiency at the point where costs are incurred.

If you want to assign overhead costs accurately to individual products, services, or market segments, you need to further allocate the costs to those cost centers directly involved in the creation of the products or services. From these cost centers you can then use different methods to assign the activities and costs to the relevant products, services, and market segments.

This enables you to valuate semi-finished and finished products in Product Cost Controlling (CO-PC), and to calculate contribution margins in Profitability Analysis (CO-PA)

Cost center groups represent a hierarchical structure of cost centers known as the standard hierarchy. Each cost center that is created must be assigned to a group in the standard hierarchy. This ensures that the standard hierarchy contains all the cost centers in the controlling group. When analyzing the standard hierarchy, the SAP system automatically includes all cost centers.

Note that cost centers may be assigned to any number of alternative groups. However, alternative groups cannot be created when maintaining the standard hierarchy.

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

The organizational structure and master data of your company was created in your ERP system during implementation. The organizational structure reflects the structure of your company. The master data represents cost centers and cost center groups, depending on the operational focus of your company.

| Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Controlling Area | General Data | Mandatory |  |
| Company Code | Organizational Units | Mandatory |  |

### Mandatory and Optional Master Data

Cost center and cost center group master data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a cost center data record.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Hierarchy Area | Organizational Units | Mandatory |  |
| Business Area | Organizational Units | Optional |  |
| Functional Area | Organizational Units | Optional |  |
| Profit Center | Organizational Units | Mandatory |  |

### Main Parameters for Data Creation

This scope item has no business conditions.

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Creating Cost Center Master Data](#unique_9) [page ] 6 | Cost Accountant - Overhead | Manage Cost Centers - Old Version (F1443A) | Cost centers can be created according to new business requirements. |
| [Creating Cost Center Group Master Data](#unique_10) [page ] 8 | Cost Accountant - Overhead | Manage Global Hierarchies (F2918) or Manage Cost Center Groups (F1024) | Cost center groups can be created according to new business requirements. |
| [Where-Used List - Cost Centers Actual](#unique_11) [page ] 10 | Cost Accountant - Overhead | Manage Cost Centers - Old Version (F1443A) |  |

## Test Procedures

This section describes procedures for each process step that belongs to this scope item. You can use these procedures also for testing the master data creation.

### Creating Cost Center Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note Standard Hierarchy Node 1~As of 2502 Edition, for new customer installations, the Standard Hierarchy will be delivered using the global hierarchy functionality with the value of 1~. Previous customers can continue to use the set-based Standard Hierarchy value of 0001.When creating the very first cost center in the productive system, you must select the value 1~ in the search dropdown list in the Standard Hierarchy Node field. This establishes the top-level node 1~ in the Standard Hierarchy. Once the very first cost center in the system is created, the Standard Hierarchy node 1~ is also created automatically. As of 2502 Edition, SAP S/4HANA Cloud Public Edition Public Edition default content is always shipped with Standard Hierarchy 1~ and must be used as the top level. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Cost Centers - Old Version (F1443A). | The app opens. |  |
| 3 | Create a New Cost Center | Choose Create to create a new cost center. |  |  |
| 4 | Enter New Cost Center | On the General Information tab, make the following entries:Cost Center: <Text>Name: <Text>Description: <Text>Person Responsible: <Person responsible>Valid From:<01/01/2017>Valid To:<12/31/9999>Cost center category: <Cost center category>Optionally, you can change the default values for valid dates and select a reference from the existing cost center master data. | A new section opens, displaying the general information. |  |
| 5 | Enter Cost Center Organizational Data | In the Organizational Units section, on the Cost Center screen, make the following entries:Standard Hierarchy Node: <1~>Company Code: <Company code>Functional area: <Functional area>Profit Center: <Profit center>For PSM Only:Note If you have Public Sector Management (PSM) installed, these fields will be available for input after the PSM company code is selected.Fund: <Fund>Fund Fixed Assignment: <Yes/No>Grant: <Grant>Grant Fixed Assignment: <Yes/No>Functional Area Fixed Assignment: <Yes/No>Note The Fixed assignment check box for Functional Area, Fund, and Grant displays only after entering respective master data.Budget carrying cost center: <Cost center>Budget availability control profile: <Profile>Budget availability control is active: <Yes/No> | The selection scrolls, displaying the organizational data. |  |
| 6 | Create | Choose Create. | The cost center is created. |  |

### Creating Cost Center Group Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

For this chapter, the Basic Data for the Material must be already filled out as described in chapter: [Creating Cost Center Master Data](#unique_9) [page ] 6. Begin this procedure after you have saved the Master Data entries in the previous chapter.

|  |
| --- |
| Note Either Manage Global Hierarchies (F2918) or Manage Cost Center Groups (F1024) can be used when creating alternative hierarchies but only one method (Global Hierarchy Groups or Set-Based Groups) should be selected. Both methods are described in the below steps.Existing customers are allowed to continue to use the Set-Based Groups related app Manage Cost Center Groups (F1024) until they completely migrate and mark the migration status as Complete using the BPC Expert Role via this path: Business Process Configuration > Accounting > General Settings: Migrate Set-Based Groups to Global Hierarchies (F6228).SAP-delivered Cost Center Group demo master data is also created using Set-Based Groups and can also be converted.You can find more information on the conversion of Cost Center Group to Global Hierarchy via: [https://help.sap.com/docs/SAP_S4HANA_CLOUD/c56f622a2edf491b9f1b596b55587009/635e615de9a848eb9129edb0da88cbcc.html?state=DRAFT](https://help.sap.com/docs/SAP_S4HANA_CLOUD/c56f622a2edf491b9f1b596b55587009/635e615de9a848eb9129edb0da88cbcc.html?state=DRAFT). |

Procedure: Option 1 - Global Hierarchy Groups

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Global Hierarchies (F2918). | The app opens. |  |
| 3 | Choose Create | In the Hierarchy List section, choose Create. | The New Hierarchy screen displays. |  |
| 4 | Enter New Cost Center Hierarchy | On the New Hierarchy screen, make the following entries and select Create:Type: Cost Center HierarchyHierarchy ID: <Any ID up to 10 characters>Caution The total length of hierarchy ID and node ID cannot exceed 14 characters.Controlling Area: A000Hierarchy Description: <Any description>Valid From: <Current date> |  |  |
| 5 | Edit New Cost Hierarchy | On the Hierarchy List screen, select the detail icon > and select Edit for your newly created Cost Center Hierarchy.Select the newly created Cost Center Hierarchy, choose More on the right side of the screen, and then choose Fast Entry.On the Fast Entry screen, select Cost Center and make the following entry:ID: <Select the cost center(s) you want to add using the search function>Select OK when you finish and select Save.Go back to the Cost Center Hierarchy screen and select Activate. | The newly created Cost Center Hierarchy is now activated. |  |

Procedure: Option 2 - Set-Based Groups

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Cost Center Groups (F1024). | The app opens. |  |
| 3 | Create a New Cost Center Group | In the Result List: Cost Center Group section, choose New. |  |  |
| 4 | Enter New Cost Center Group | On the Cost Center Group: New screen, make the following entries:Controlling Area: <A000>Cost Center Group: <Cost center group>Choose Continue and make the following entry:Name: <Name>Choose Save.Optionally, you can choose a reference from the existing Cost Center Groups. | The Cost Center Groups: New screen displays. |  |
| 5 | Enter Cost Center Organizational Data | On the Cost Center Groups: New screen, make the following entries:On the top level, you can create new master data by choosing New:New child group: <Cost center group>On the lower levels, you can add by choosing New:New child group: <Cost center group>New sibling group: <Cost center group>On the top level, you can add existing master data by choosing Add:Add child group: <Cost center groupAdd cost center: <Cost center>Add cost center range: <Cost center(s)>On the lower levels, you can add by choosing New:New child group: <Cost center group>New sibling group: <Cost center group>Add cost center: <Cost center>Add cost center range: <Cost center(s)> | New master data displays on the Cost Center Groups: New screen. |  |
| 6 | Save Your Data | Choose Save. | The Cost Center Group is created and saved. |  |

### Analytics

#### Where-Used List - Cost Centers Actual

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity allows you to see where the cost centers are used in other master data such as activity type, profit centers, and actual cost allocations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Cost Centers - New Version (F1443B). | The Manage Cost Centers screen displays. |  |
| 3 | Selection Criteria | Make the following entry and choose Go:Cost Center: <your cost center> |  |  |
| 4 | Where Used | Select the desired cost center and choose Where Used.Select one option from the dropdown list. For example, In All Objects. | A report showing where the cost centers are currently used displays. For details, you can select the master data object type and drill in further. |  |

|  |
| --- |
| Note The Where-Used List - Cost Centers (F3549) app can also be used to determine where the cost centers are currently used. |

## Appendix

### Cost Center Replication from SAP S/4HANA Cloud Public Edition to SAP Master Data Integration (Optional)

This link describes replication of SAP S/4HANA Cloud Public Edition cost center master data via SAP Master Data Integration to other Cloud applications such as SAP SuccessFactors:[https://help.sap.com/viewer/6b39bd1d0e5e4099a5b65d835c29c696/LATEST/en-US/decbb94c95fa421ead9101e4c43683f7.html](https://help.sap.com/viewer/6b39bd1d0e5e4099a5b65d835c29c696/LATEST/en-US/decbb94c95fa421ead9101e4c43683f7.html).

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
- related-to :: [[06-management-accounting/mds-bnm-637]]
- related-to :: [[06-management-accounting/mds-bnm-639]]
- related-to :: [[06-management-accounting/script-de-dados-mestre-criar-centro-de-custo-e-grupo-de-centros-de-cus]]
- related-to :: [[06-management-accounting/script-de-datos-maestros-crear-centro-de-coste-y-grupo-de-centros-de-c]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNM_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 18,890 chars in the whole document
