---
id: 08-sales-order-management/master-data-script-create-location-substitution-and-exclusion-mds-5ng
title: "Master Data Script: Create Location Substitution and Exclusion - MDS (5NG) (5NG_S4CLD2608_Master_Data_EN_XX)"
description: SAP S/4HANA Cloud Public Edition 2608 master data test script (5NG) for creating plant and storage location substitution and exclusion records in Fiori.
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/product-and-location-substitution]
aliases: [5NG_S4CLD2608_Master_Data_EN_XX]
keywords: ["Product, Plant and Storage Location Substitution", plant substitution, plant exclusion, storage location substitution, storage location exclusion, substitution reasons, substitution groups, substitution controls, organizational units, order fulfillment manager role]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NG_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-473
topic: 08-sales-order-management/product-and-location-substitution
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Location Substitution and Exclusion - MDS (5NG) (5NG_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NG_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Product, Plant and Storage Location Substitution** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Location Substitution and Exclusion - MDS (5NG) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc233904825)

[2 Prerequisites 4](#_Toc233904826)

[2.1 System Access 4](#_Toc233904827)

[2.2 Roles 4](#_Toc233904828)

[2.3 Required Organizational Units 4](#_Toc233904829)

[2.4 Mandatory Master Data 5](#_Toc233904830)

[2.5 Preliminary Steps for Plant Substitution 5](#_Toc233904831)

[2.5.1 Create Reason for Plant Substitution (Optional) 5](#_Toc233904832)

[2.5.2 Create Group for Plant Substitution (Optional) 6](#_Toc233904833)

[2.5.3 Create Control for Plant Substitution (Optional) 8](#_Toc233904834)

[2.6 Preliminary Steps for Storage Location Substitution 9](#_Toc233904835)

[2.6.1 Create Reason for Storage Location Substitution (Optional) 9](#_Toc233904836)

[2.6.2 Create Group for Storage Location Substitution (Optional) 10](#_Toc233904837)

[2.6.3 Create Control for Storage Location Substitution (Optional) 12](#_Toc233904838)

[3 Overview Table 14](#_Toc233904839)

[4 Test Procedures 15](#_Toc233904840)

[4.1 Plant Substitution 15](#_Toc233904841)

[4.1.1 Create Plant Substitution 15](#_Toc233904842)

[4.1.2 Create Plant Exclusion 16](#_Toc233904843)

[4.2 Storage Location Substitution 17](#_Toc233904844)

[4.2.1 Create Storage Location Substitution 17](#_Toc233904845)

[4.2.2 Create Storage Location Exclusion 19](#_Toc233904846)

## Purpose

In this document, you will find how to create a Location Substitution and Exclusion master data for your SAP S/4HANA Cloud Public Edition system.

The Location Types Plant and Storage Location are supported for Substitution and Exclusion.

Plant Substitution is a technique used to substitute one Plant with another Plant. A Plant Substitution can be created for various reasons. For example:

- The Source Plant is under maintenance
- The Source Plant is in containment zone
- Product stock is not available in the Source Plant

Plant Exclusion enables Customers to exclude a Plant from being a Substitute. For example, Plant Exclusion can be created for a Plant which is temporarily shut down.

Storage Location Substitution is a technique used to substitute one Storage Location with another Storage Location within the same Plant. A Storage Location Substitution can be created for various reasons. For example:

- The Source Storage Location is not available
- Product Stock is not available in the Source Storage Location within the Plant

Storage Location Exclusion enables Customers to exclude a Sotrage Location from being a substitute.

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Order Fulfillment Manager | SAP_BR_ORDER_FULFILLMNT_MNGR | Order Fulfillment Management | SAP_BR_ORDER_FULFILLMNT_MNGR |  |

### Required Organizational Units

The organizational structure reflects the structure of your company.

Plant Substitutes can be dependent on the organizational units (Sales Organization and Distribution Channel) of the company. It can also be independent of the organizational unit.

Storage Location Substitute is dependent on the organizational unit (Plant) of the company. It is always dependent of the organizational unit.

The following table gives an overview of the relevant organizational units.

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| Plant Substitution and Plant Exclusion | Sales Organization |  | Sales Organization is not mandatory in PlantSubstitution/Exclusion. PlantSubstitution/Exclusion can happen without Sales Organization restriction. | Sales Organization:____________ |
| Plant Substitution and Plant Exclusion | Distribution Channel |  | Distribution Channel is not mandatory in Plant Substitution/Exclusion. Plant Substitution/Exclusion can happen without Distribution Channel restriction. | Distribution Channel:____________ |
| Storage Location Substitution and Storage Location Exclusion | Plant |  | Plant is mandatory in Storage Location Substitution/Exclusion. Storage Location Substitution/Exclusion cannot happen without Plant. | Plant: 1010 |

### Mandatory Master Data

| Master Data Object | Used in Data Segment | Mandatory/Optional | Comments |
| --- | --- | --- | --- |
| NA | NA | NA | NA |

### Preliminary Steps for Plant Substitution

#### Create Reason for Plant Substitution (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating reason for plant substitution/exclusion. Apps available to you are dependent upon your assigned role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Order Fulfillment Manager. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Manage Substitution Reasons - Locations (F5313). | The Manage Substitution Reasons - Locations screen is displayed. |  |
| 3 | Choose Create | On the Manage Substitution Reasons - Locations screen, choose Create. | The Manage Substitutions Reasons- Locations Create screen is displayed. |  |
| 4 | Enter Reason | In the Header section, make the following entry.Location Type: <Plant>Reason: <Enter the new Reason code for Plant substitution, for example, NEW_PLANT> |  |  |
| 5 | Create Your Data | Choose Create. | System message shows Reason is created. |  |
| 6 | Choose Create | In the Description section, choose Create. | The Reason Description Create screen is displayed. |  |
| 7 | Enter Description Data | In the Description section, make the following entries:Language Key: <Enter Language applicable for reason, for example, EN English>Reason Description: <Enter text to describe the reason, for example, New plant is available> |  |  |
| 8 | Create Your Data | Choose Create. | System message shows Description Created. |  |

#### Create Group for Plant Substitution (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating Group for Plant Substitution/Exclusion. Apps available to you are dependent upon your assigned role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Order Fulfillment Manager. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Manage Substitution Groups - Locations (F5311). | The Manage Substitution Groups - Locations screen is displayed. |  |
| 3 | Choose Create | On the Manage Substitution Groups - Locations screen, choose Create. | The Manage Substitutions Groups - Locations Create screen is displayed. |  |
| 4 | Enter Group | In the Header section, make the following entry:Location Type: <Plant>Group: <Enter the new Group for substitution, for example, SOUTH_REGION> |  |  |
| 5 | Create Your Data | Choose Create. | System message shows Group Created. |  |
| 6 | Choose Create | In the Description section, choose Create. | The Group Description Create screen is displayed. |  |
| 7 | Enter Description Data | In the Description section, make the following entries:Language Key: <Enter Language applicable for Group, for example, EN English>Group Description: <Enter text to describe the group, for example, Plants available in south region> |  |  |
| 8 | Create Your Data | Choose Create. | System message shows Group Description Created. |  |
| 9 | Choose Back | In the Title section, Choose < (Back). | The Manage Substitutions Groups - Location s screen is displayed. |  |
| 10 | Activate Group Data | Choose Set to Active. | System message shows that Status changed. |  |

#### Create Control for Plant Substitution (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating control for Plant substitution/exclusion controls. Apps available to you are dependent upon your assigned role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Order Fulfillment Manager. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Manage Substitution Controls - Locations (F5312). | The Manage Substitution Controls - Location s screen is displayed. |  |
| 3 | Choose Create | On the Manage Substitution Controls - Locations screen, choose Create. | The Manage Substitution Controls- Locations Create screen is displayed. |  |
| 4 | Enter Control | In the Header section, make the following entry.Location Type: <Plant>Control: <Enter the new control for substitution, for example, REGION> |  |  |
| 5 | Create Your Data | Choose Create. | System message shows Control Created. |  |
| 6 | Choose Create | In the Description section, choose Create. | The Control Description Create screen is displayed. |  |
| 7 | Enter Description Data | In the Description section, make the following entries:Language Key: <Enter Language applicable for Control, for example, EN English>Control Description: <Enter text to describe the Control, for example, Control for a Region> |  |  |
| 8 | Create Your Data | Choose Create. | System message shows Control Description Created. |  |
| 9 | Choose Back | In the Title section, Choose < (Back). | The Manage Substitution Controls- Locations screen is displayed. |  |
| 10 | Assign Groups | In the Assigned Groups section, choose Assign. | The Assign Groups to Control dialog is displayed. |  |
| 11 | Choose Group | In the Assign Groups to Control dialog, search and choose Group.For example, choose Group<SOUTH_REGION>Choose Assign. | System message shows Group(s) have been assigned. |  |

### Preliminary Steps for Storage Location Substitution

#### Create Reason for Storage Location Substitution (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating reason for storage location substitution/exclusion. Apps available to you are dependent upon your assigned role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Order Fulfillment Manager. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Manage Substitution Reasons - Locations (F5313). | The Manage Substitution Reasons - Locations screen is displayed. |  |
| 3 | Choose Create | On the Manage Substitution Reasons - Locations screen, choose Create. | The Reason screen is displayed. |  |
| 4 | Enter Reason | In the Header section, make the following entry.Location Type: <Storage Location>Reason: <Enter the new Reason code for Storage Location substitution, for example, NEW_SLOC> |  |  |
| 5 | Create Your Data | Choose Create. | System message shows Reason is created. |  |
| 6 | Choose Create | In the Description section, choose Create. | The Reason Description screen is displayed. |  |
| 7 | Enter Description Data | In the Description section, make the following entries:Language Key: <Enter Language applicable for reason, for example, EN English>Reason Description: <Enter text to describe the reason, for example, New storage location is available> |  |  |
| 8 | Create Your Data | Choose Create. | System message shows Description Created. |  |

#### Create Group for Storage Location Substitution (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating Group for Storage Location Substitution/Exclusion. Apps available to you are dependent upon your assigned role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as aOrder Fulfillment Manager. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Manage Substitution Groups - Locations (F5311). | The Manage Substitution Groups - Locations screen is displayed. |  |
| 3 | Choose Create | On the Manage Substitution Groups – Locations screen, choose Create. | The Manage Substitutions Groups - Locations Create screen is displayed. |  |
| 4 | Enter Group | In the Header section, make the following entry:Location Type: <Storage Location>Group: <Enter the new Group for substitution, for example, COLD_STORAGE> |  |  |
| 5 | Create Your Data | Choose Create. | System message shows Group Created. |  |
| 6 | Choose Create | In the Description section, choose Create. | The Group Description Create screen is displayed. |  |
| 7 | Enter Description Data | In the Description section, make the following entries:Language Key: <Enter Language applicable for Group, for example, EN English>Group Description: <Enter text to describe the group, for example, Storage Location for Cold Storage items> |  |  |
| 8 | Create Your Data | Choose Create. | System message shows Group Description Created. |  |
| 9 | Choose Back | In the Title section, choose < (Back) | The Manage Substitutions Groups-Locations screen is displayed. |  |
| 10 | Activate Group Data | Choose Set to Active. | System message shows that Status changed. |  |

#### Create Control for Storage Location Substitution (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating control for Storage Location substitution/exclusion controls. Apps available to you are dependent upon your assigned role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Order Fulfillment Manager. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Manage Substitution Controls - Locations (F5312). | The Manage Substitution Controls - Locations screen is displayed. |  |
| 3 | Choose Create | On the Manage Substitution Controls - Locations screen, choose Create. | The Manage Substitution Controls-Locations Create screen is displayed. |  |
| 4 | Enter Control | In the Header section, make the following entry.Location Type: <Storage Location>Control: <Enter the new control for substitution, for example, STORAGE_TYPE> |  |  |
| 5 | Create Your Data | Choose Create. | System message shows Control Created. |  |
| 6 | Choose Create | In the Description section, choose Create. | The Control Description Create screen is displayed. |  |
| 7 | Enter Description Data | In the Description section, make the following entries:Language Key: <Enter Language applicable for Control, for example, EN English>Control Description: <Enter text to describe the Control, for example, Control for Type of Storage> |  |  |
| 8 | Create Your Data | Choose Create. | System message shows Control Description Created. |  |
| 9 | Choose Back | In the Title section, Choose < (Back). | The Manage Substitution Controls-Locations screen is displayed. |  |
| 10 | Assign Groups | In the Assigned Groups section, choose Assign. | The Assign Groups to Control dialog is displayed. |  |
| 11 | Choose Group | In the Assign Groups to Control dialog, search and choose Group.For example, choose Group<COLD_STORAGE>Choose Assign. | System message shows Group(s) have been assigned. |  |

## Overview Table

This scope item consist of the process segments provided in the below table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Segment | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Plant Substitution](#unique_14) [page ] 15 | Order Fulfillment Manager | Manage Substitutions - Locations (F5314) | Plant Substitution record is created. |
| [Create Plant Exclusion](#unique_15) [page ] 16 | Order Fulfillment Manager | Manage Exclusions - Locations (F5315) | Plant Exclusion record is created. |
| [Create Storage Location Substitution](#unique_16) [page ] 17 | Order Fulfillment Manager | Manage Substitutions - Locations (F5314) | Storage Location Substitution record is created. |
| [Create Storage Location Exclusion](#unique_17) [page ] 19 | Order Fulfillment Manager | Manage Exclusions - Locations (F5315) | Storage Location Exclusion record is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Plant Substitution

#### Create Plant Substitution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating Plant Substitution. Apps available to you are dependent upon your assigned role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Substitutions - Locations (F5314). | The Manage Substitutions - Locations screen displays. |  |
| 3 | Choose Create | In the Manage Substitutions - Locations view, under the Plant section, choose Create. | The Manage Substitutions - Locations flexible column layout with Create screen displays. |  |
| 4 | Enter Header Data | In the Header section, make the following entries:Plant: <Enter the plant which requires a substitute>Substitute Plant: <Enter the substitute>Sales Organization: <Sales Organization number>Distribution Channel: <Distribution Channel number>Plant and Substitute Plant data is mandatory to create a substitution. |  |  |
| 5 | Enter General Information Data | In the General Information section, make the following entries:Reason: <Enter the reason for creating substitute. For example, NEW_PLANT>Group: <Enter the substitution group. For example, SOUTH_REGION>Valid From: <Enter the start date and time for validity>Valid To: <Enter the end date and time for validity>Time Zone: <Enter the time zone applicable for validity>The above entries are optional. |  |  |
| 6 | Create Your Data | Choose Create. | System message displays Substitution Created. |  |
| 7 | Activate Plant Substitution Data | Choose Set to Active. | System message displays Status Changed. |  |
| 8 | Display Graph | Choose View Graph | The Display Plant Network Graph screen displays. |  |

#### Create Plant Exclusion

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating Plant Exclusion. Apps available to you are dependent upon your assigned role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Exclusions - Locations (F5315). | The Manage Exclusions - Locations screen displays. |  |
| 3 | Choose Create | In the Manage Exclusions - Locations (Plant) view, choose Create. | The Plant Exclusion screen displays. |  |
| 4 | Enter Header Data | In the Header section, make the following entries:Plant: <Enter the plant which needs to be excluded from Substitution>Sales Organization: <Sales Organization number>Distribution Channel: <Distribution Channel number>Plant is mandatory to create an exclusion. |  |  |
| 5 | Enter General Information Data | In the General Information section, make the following entries:Reason: <Enter the reason for excluding the Plant>Group: <Enter the group applicable for Plant exclusion>Valid From: <Enter the start date and time for validity>Valid To: <Enter the end date and time for validity>Time Zone: <Enter the time zone applicable for validity>The above entries are optional. |  |  |
| 6 | Create Your Data | Choose Create. | System message displays Exclusion Created. |  |
| 7 | Activate Plant Exclusion Data | Choose Set to Active. | System message displays Status Changed. |  |

### Storage Location Substitution

#### Create Storage Location Substitution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating Storage Location Substitution. Apps available to you are dependent upon your assigned role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Substitutions - Locations (F5314). | The Manage Substitutions - Locations screen displays. |  |
| 3 | Choose Storage Location | On the Manage Substitutions - Locations screen, choose the Storage Location tab. | The Manage Substitutions - Locations (Storage Location) screen displays. |  |
| 4 | Choose Create | On the Storage Location tab, choose Create. | The Manage Substitutions - Locations flexible column layout with Create screen displays. |  |
| 5 | Enter Header Data | In the Header section, make the following entries:Plant: <Plant number>Storage Location: <Enter the storage location which requires a substitute>Substitute Storage Locationt: <Enter the substitute>Plant and Substitute Storage Location data is mandatory to create a substutition while Storage Location is optional. Plant is selected by default when Storage Location is selected. |  |  |
| 6 | Enter General Information Data | In the General Information section, make the following entries:Reason: <Enter the reason for creating substitute. For example, NEW_SLOC>Group: <Enter the substitution group. For example, COLD_STORAGE>Valid From: <Enter the start date and time for validity>Valid To: <Enter the end date and time for validity>Time Zone: <Enter the time zone applicable for validity>The above entries are optional. |  |  |
| 7 | Create Your Data | Choose Create. | System message displays Substitution Created. |  |
| 8 | Activate Storage Location Substitution Data | Choose Set to Active. | System message displays Status Changed. |  |
| 9 | Display Graph | Choose View Graph. | The Display Storage Location Network Graph screen displays. |  |

#### Create Storage Location Exclusion

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating Storage Location Exclusion. Apps available to you are dependent upon your assigned role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Order Fulfillment Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Exclusions - Locations (F5315). | The Manage Exclusions - Locations screen displays. |  |
| 3 | Choose Storage Location | In the Manage Exclusions - Locations view, choose Storage Location. | The Manage Exclusions - Locations (Storage Location) screen displays. |  |
| 4 | Choose Create | In the Manage Exclusions - Locations (Storage Location) view, choose Create. | The Manage Exclusions - Locations Create screen displays. |  |
| 5 | Enter Header Data | In the Header section, make the following entries:Plant: <Plant number>Storage Location: <Enter the storage location which needs to be excluded from Substitution>Both Plant and Storage Location are mandatory for exclusion. |  |  |
| 6 | Enter General Information Data | In the General Information section, make the following entries:Reason: <Enter the reason for excluding the Storage Location>Group: <Enter the group applicable for Storage Location exclusion>Valid From: <Enter the start date and time for validity>Valid To: <Enter the end date and time for validity>Time Zone: <Enter the time zone applicable for validity>The above entries are optional. |  |  |
| 7 | Create Your Data | Choose Create. | System message displays Exclusion Created. |  |
| 8 | Activate Storage Location Exclusion Data | Choose Set to Active. | System message displays Status Changed. |  |

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
- related-to :: [[08-sales-order-management/lokationsersetzung-und-ausschluss-anlegen-sds-5ng-472]]
- related-to :: [[08-sales-order-management/mds-5ng-475]]
- related-to :: [[08-sales-order-management/mds-5ng-477]]
- related-to :: [[08-sales-order-management/script-de-dados-mestre-criar-substituicao-e-exclusao-de-local-mds-5ng]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NG_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 30,385 chars in the whole document
