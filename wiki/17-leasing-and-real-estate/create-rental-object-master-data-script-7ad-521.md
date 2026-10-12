---
id: 17-leasing-and-real-estate/create-rental-object-master-data-script-7ad-521
title: Create Rental Object – Master Data Script (7AD) (7AD_S4CLD2608_Master_Data_EN_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (scope item 7AD) for creating usable, rentable and intercompany rental objects, with prerequisites and test steps."
cluster: 17-leasing-and-real-estate
tags: [kb/leasing-and-real-estate, topic/real-estate-contracts-and-leasing]
aliases: [7AD_S4CLD2608_Master_Data_EN_XX]
keywords: [Real Estate Rental Objects and Lease Accounting, rental objects, usable objects, rentable objects, intercompany lease, usage categories, usage types, number ranges, measurement types, architecture objects]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7AD_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-521
topic: 17-leasing-and-real-estate/real-estate-contracts-and-leasing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Create Rental Object – Master Data Script (7AD) (7AD_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7AD_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Real Estate Rental Objects and Lease Accounting** in Leasing and Real Estate. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Rental Object – MDS (7AD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc233904828)

[2 Prerequisites 4](#_Toc233904829)

[2.1 System Access 4](#_Toc233904830)

[2.2 Roles 4](#_Toc233904831)

[2.3 Required Organizational Units 4](#_Toc233904832)

[2.4 Mandatory and Optional Master Data 5](#_Toc233904833)

[2.5 Main Parameters for Data Creation 5](#_Toc233904834)

[2.5.1 Usage Category 5](#_Toc233904835)

[2.5.2 Usage Types and Number Ranges 6](#_Toc233904836)

[2.5.3 Ownership ID 7](#_Toc233904837)

[2.5.4 Portfolio ID 7](#_Toc233904838)

[2.5.5 Measurements 8](#_Toc233904839)

[2.5.6 Real Estate Architecture Object Type and Number Range 9](#_Toc233904840)

[2.5.7 Real Estate Architecture Object Hierarchy 9](#_Toc233904841)

[2.6 Preliminary Steps 9](#_Toc233904842)

[2.6.1 Validate MDI Service Readiness 9](#_Toc233904843)

[3 Overview Table 10](#_Toc233904844)

[4 Test Procedure 11](#_Toc233904845)

[4.1 Create Usable Object Without Portfolio Structure 11](#_Toc233904846)

[4.2 Create Usable Object with Portfolio Structure 12](#_Toc233904847)

[4.3 Create Rentable Object Without Portfolio Structure 14](#_Toc233904848)

[4.4 Change Rentable Object with Portfolio Structure 15](#_Toc233904849)

[4.5 Create Intercompany Rentable Object with Portfolio Structure 15](#_Toc233904850)

[4.6 Create Intercompany Rentable Object Without Portfolio Structure 17](#_Toc233904851)

[4.7 Create Intercompany Usable Object with Portfolio Structure 18](#_Toc233904852)

[4.8 Create Intercompany Usable Object Without Portfolio Structure 19](#_Toc233904853)

## Purpose

A generic rental object can be either a usable or a rentable object.

A usable object is an object leased in or owned by an enterprise and defines the scope for own usage, external or intercompany lease-out. The usable object can be subject of a real estate lease-in contract. The enterprise acts from a customer perspective.

A rentable object is an object that can be leased out by an enterprise to an external tenant or affiliated company. The rentable object can be subject of a real estate lease-out contract. The enterprise acts from a vendor perspective.

Generic rental objects are used in the different scenarios as follows:

a) External lease-in or owned objects

You define external leased-in or owned objects as usable objects. You can use the usage category Usable Object with Portfolio Structure (UP) or Usable Object w/o Portfolio Structure (UW) for this. Usable objects are required for all subsequent processes.

b) External lease-out objects

You define external lease-out objects as rentable objects. You can use the usage category Rentable Object with Portfolio Structure (RP) or Rentable Object w/o Portfolio Structure (RW) for this. Each rentable object needs a relation to a usable object. Therefore, you need to have created a usable object first (see a)).

c) Intercompany lease objects

To set up an intercompany lease process, the following objects are required:

1. Usable object (external leased-in or owned) (see a))
2. Intercompany rentable object (usage category Intercompany Rentable Object with Portfolio Structure (I3) or Intercompany Rentable Object without Portfolio Structure (I4)) with a relation to a usable object (see 1.) within the lessor company code
3. Intercompany usable object (usage category Intercompany Usable Object with Portfolio Structure (I1) or Intercompany Usable Object without Portfolio Structure (I2)) within the lessee company code with a relation to an intercompany rentable object within the lessor company code (see 2.)

Afterwards, you can continue with 2. and 3. to set up an additional intercompany lease process for a third company code, or with b) to create an external lease-out object. The additional intercompany rentable object or external rentable object in this case has a relation to the intercompany usable object.

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
| Real Estate Specialist - Location Management | SAP_BR_RE_SPECIALIST_LOCAT | Location Management | SAP_FIN_SPT_RE_LOCATION_PC |  |
| Contract Specialist - Leasing | SAP_BR_RECM_SPECIALIST | Leasing Contract Management / Leasing Contract Management - Sales-Based Rent | SAP_BR_RECM_SPECIALIST / SAP_BR_RECM_SALES_REPORTER |  |

### Required Organizational Units

The organizational structure and master data of your company was created in your ERP system during implementation. The organizational structure reflects the structure of your company. The master data represents usable objects, depending on the operational focus of your company.

| Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Company Code | General Data | Mandatory |  |

### Mandatory and Optional Master Data

Usable and rentable object master data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a usable/rentable data record.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Cost Center | Account Assignment Object | Mandatory | Either Cost Center or WBS Element |
| WBS Element | Account Assignment Object | Mandatory | Either Cost Center or WBS Element |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are required to create a generic rental object.

#### Usage Category

Usage Categories determine the kind and business behavior of a generic rental object. Following Usage Categories are supported:

1. Usable Object with Portfolio Structure (UP) – These usable objects require the use of the Master Data Integration service on the BTP (MDI) to establish the relationship to real estate architecture objects provided by an external application.
2. Usable Object w/o Portfolio Structure (UW) – For these usable objects a relationship to real estate architecture objects is not possible.
3. Rentable Object with Portfolio Structure (RP) – These rentable objects require the use of the Master Data Integration service on the BTP (MDI) to establish the relationship to real estate architecture objects provided by an external application.
4. Rentable Object w/o Portfolio Structure (RW) – For these rentable objects a relationship to real estate architecture objects is not possible.
5. Intercompany Rentable Object with Portfolio Structure (I3) – These rentable objects are used in an intercompany lease-out scenario and require the use of the Master Data Integration service on the BTP (MDI) to establish the relationship to real estate architecture objects provided by an external application.
6. Intercompany Rentable Object without Portfolio Structure (I4) – These rentable objects are used in an intercompany lease-out scenario without a relationship to real estate architecture objects.
7. Intercompany Usable Object with Portfolio Structure (I1) – These usable objects are used in an intercompany lease-in scenario and require a relationship to a rentable object of usage category Intercompany Rentable Object with Portfolio Structure (I3).
8. Intercompany Usable Object without Portfolio Structure (I2) – These usable objects are used in an intercompany lease-in scenario and require a relationship to a rentable object of usage category Intercompany Rentable Object without Portfolio Structure (I4).

#### Usage Types and Number Ranges

For each usage category different usage types can be defined to differentiate the objects and their business behavior within the category. The usage types determine the number ranges for the object master record IDs. You cannot change the assignment or IDs afterwards. If a usage type is assigned to an internal number range, you cannot enter the master record ID manually. In this case, leave the field blank as the system automatically chooses a number from the assigned numeric number range.

The following usage types and corresponding number ranges are pre-defined:

| Usage Type | Usage Category | Number Range | Comments |
| --- | --- | --- | --- |
| DP/Hardware (SU01) | Usable Object w/o Portfolio Structure (UW) | 010000000 - 019999999 |  |
| Fixtures Fittings (SU02) | Usable Object w/o Portfolio Structure (UW) | 020000000 - 029999999 |  |
| Machinery (SU03) | Usable Object w/o Portfolio Structure (UW) | 030000000 - 039999999 |  |
| Vehicles (SU04) | Usable Object w/o Portfolio Structure (UW) | 040000000 - 049999999 |  |
| Office Equipment (SU05) | Usable Object w/o Portfolio Structure (UW) | 050000000 - 059999999 |  |
| Office Building (SU06) | Usable Object with Portfolio Structure (UP) | 060000000 - 069999999 | Demo purpose only |
| Retail (SU07) | Usable Object with Portfolio Structure (UP) | 070000000 - 079999999 | Demo purpose only |
| Residential (SU08) | Usable Object with Portfolio Structure (UP) | 080000000 - 089999999 | Demo purpose only |
| Office (SR01) | Rentable Object with Portfolio Structure (RP) | 1000000000 - 1099999999 | Demo purpose only |
| Shop (SR02) | Rentable Object with Portfolio Structure (RP) | 1100000000 - 1199999999 | Demo purpose only |
| Apartment (SR03) | Rentable Object with Portfolio Structure (RP) | 1200000000 - 1299999999 | Demo purpose only |
| Vehicles (SR04) | Rentable Object w/o Portfolio Structure (RW) | 1300000000 - 1399999999 | Demo purpose only |
| LO Office ICO (SRI1) | Intercompany Rentable Object with portfolio structure (I3) | 3100000000 - 3199999999 | Demo purpose only |
| LI Office ICO (SUI1) | Intercompany Usable Object with portfolio structure (I1) | 3000000000 - 3099999999 | Demo purpose only |
| LO Office Equip. ICO (SRI2) | Intercompany Rentable Object without portfolio structure (I4) | 6100000000 - 6199999999 | Demo purpose only |
| LI Office Equip. ICO (SUI2) | Intercompany Usable Object without portfolio structure (I2) | 6000000000 - 6099999999 | Demo purpose only |

To configure Number Ranges and Usage Types use following SSCUIs:

- Define Number Ranges for Generic Rental Objects (ID: 106591)
- Define Usage Types for Generic Rental Objects (ID: 106592)

#### Ownership ID

Usable objects can be subject to different legal control. The legal control type must be maintained using the Ownership ID attribute. The characteristic values of the ownership ID can be defined in the configuration.

The following ownership IDs are pre-defined:

- Lease-In (S001)
- Owned (S002)

To configure Ownership IDs, use SSCUI: Define Ownership IDs for Usable Objects (ID: 106593).

#### Portfolio ID

Usable objects of usage category 'Usable Object w/o Portfolio Structure (UW)' can be grouped by a portfolio ID. The characteristic values of the portfolio ID can be defined in the configuration.

The following portfolio IDs for sub-grouping of Office Equipment and Vehicles are pre-defined for demo purpose:

- Diesel Car (S401)
- Gasoline Car (S402)
- Electric Car (S403)
- Office Appliances (S501)
- Office Furniture (S502)
- Mounting Solutions (S503)

To configure Portfolio IDs, use SSCUI: Define Portfolio IDs for Usable Objects (ID: 106594).

#### Measurements

Usable and/or rentable objects can have measurements. Based on these measurements, condition amounts can be calculated in contracts. Measurements of different types can be summed up to a total measurement.

The following measurement types are pre-defined for demo purpose:

| Measurement Type | Default Unit | Area Measurement | Total Measurement | Comments |
| --- | --- | --- | --- | --- |
| Office Area (SG11) | Square meter (M2) | X |  | Totaled to usable area (ST99) |
| Meeting Area (SG13) | Square meter (M2) | X |  | Totaled to usable area (ST99) |
| Pantry (SF04) | Square meter (M2) | X |  | Totaled to usable area (ST99) |
| Restroom (SD01) | Square meter (M2) | X |  | Totaled to usable area (ST99) |
| Technical Room (SC04) | Square meter (M2) | X |  | Totaled to usable area (ST99) |
| Elevator (SA02) | Square meter (M2) | X |  | Totaled to usable area (ST99) |
| Corridor (SE01) | Square meter (M2) | X |  | Totaled to usable area (ST99) |
| Shop (SG22) | Square meter (M2) | X |  | Totaled to usable area (ST99) |
| Living Space (SG41) | Square meter (M2) | X |  | Totaled to usable area (ST99) |
| Lobby Foyer (SE02) | Square meter (M2) | X |  | Totaled to usable area (ST99) |
| Parking Space (SK01) | Square meter (M2) | X |  |  |
| Usable Area (ST99) | Square meter (M2) | X | X |  |

To configure measurement types and total measurements, use following SSCUIs:

- Define Measurement Types (ID: 105394)
- • Define Total Measurements (ID: 105395)

#### Real Estate Architecture Object Type and Number Range

Generic rental objects of usage category 'Usable Object with Portfolio Structure (UP)' or 'Rentable Object with Portfolio Structure (RP)' refer to Real Estate Architecture Objects provided by an external application via Master Data Integration service on the BTP (MDI). For synchronization purpose real estate architecture object types must be configured. The real estate architecture object type determines the architecture object category and used number range in the system.

The following real estate architecture object types and corresponding number ranges are pre-defined for demo purpose:

| Architecture Object Types | Architecture Objects Category | Number Ranges | Comments |
| --- | --- | --- | --- |
| Site (S1SI) | Site (1) | 10000000 - 19999999 |  |
| Building (S2BU) | Building (2) | 20000000 - 29999999 |  |
| Land (S2LA) | Land (3) | 30000000 - 39999999 |  |
| Floor (S3FL) | Others (99) | 40000000 - 49999999 |  |
| Room (S4RO) | Others (99) | 50000000 - 59999999 |  |

To configure Number Ranges and Real Estate Architecture Object Types, use following SSCUIs:

- Define Number Range for Architecture Object (ID: 106628)
- Define Architecture Object Type (ID: 106629)

#### Real Estate Architecture Object Hierarchy

Based on the architecture object types a hierarchy can be defined. This hierarchy is used in reporting.

To configure an architecture object type hierarchy, use SSCUI: Define Permitted Superordinate Architecture Object Types (ID: 106630).

### Preliminary Steps

#### Validate MDI Service Readiness

If you want to create usable/rentable objects with portfolio structure (usage category UP and RP, or I1 and I3), a connection to an external application which provides real estate architecture objects via Master Data Integration service on the BTP (MDI) is required.

For set-up instruction and prerequisites, please see scope item 77V - Master Data Integration for Contract and Lease Management.

## Overview Table

This scope item consists of several processes provided in the following tables.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Diagram | Business Roles | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Usable Object Without Portfolio Structure](#unique_17) [page ] 11 | Contract Specialist - Leasing or Real Estate Specialist - Location Management | Manage Usable Objects |  |
| [Create Usable Object with Portfolio Structure](#unique_18) [page ] 12 | Contract Specialist - Leasing or Real Estate Specialist - Location Management | Manage Usable Objects |  |
| [Create Rentable Object Without Portfolio Structure](#unique_19) [page ] 14 | Contract Specialist - Leasing or Real Estate Specialist - Location Management | Manage Rentable Object |  |
| [Change Rentable Object with Portfolio Structure](#unique_20) [page ] 15 | Contract Specialist - Leasing or Real Estate Specialist - Location Management | Manage Rentable Object |  |
| [Create Intercompany Rentable Object with Portfolio Structure](#unique_21) [page ] 15 | Contract Specialist - Leasing or Real Estate Specialist - Location Management | Manage Rentable Object |  |
| [Create Intercompany Rentable Object Without Portfolio Structure](#unique_22) [page ] 17 | Contract Specialist - Leasing or Real Estate Specialist - Location Management | Manage Rentable Object |  |
| [Create Intercompany Usable Object with Portfolio Structure](#unique_23) [page ] 18 | Contract Specialist - Leasing or Real Estate Specialist - Location Management | Manage Usable Objects |  |
| [Create Intercompany Usable Object Without Portfolio Structure](#unique_24) [page ] 19 | Contract Specialist - Leasing or Real Estate Specialist - Location Management | Manage Usable Objects |  |

## Test Procedure

### Create Usable Object Without Portfolio Structure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Contract Specialist - Leasing or Real Estate Specialist - Location Management. | The Start page appears. |  |
| 2 | Open Manage Usable Objects | Open Manage Usable Objects. | The Manage Usable Objects screen appears. |  |
| 3 | Create Usable Objects | Choose Create and make the following entries.In the Header section:Usable Object Name: <Your object name>Usage Category: Usable Object w/o Portfolio Structure (UW)Usable Object Usage Type : <Select a usage type, for example, Vehicles (SU04)>Company Code: <Select a company code, for example, Company Code (1010) >Usable Object: <Your object ID in case of external number range, otherwise leave the field empty>In the General Information section:Portfolio ID (optional): <Select a portfolio ID, for example, Diesel Car (S401)>Authorization Group (optional): <Select an authorization group (this field is only visible if an authorization group is configured)>Ownership ID: <Select an ownership ID, for example, Lease-In (S001)>Validity Start Date: <Date from which your object is valid, for example, current date>Validity End Date: <Date until which your object is valid>In the Leading Account Assignment Object section, choose Create and make the following entries.Object Type of Assigned Object: <Select an object type, for example, Cost Center (KS)>Account Assignment Object: <Your account assignment object>Note A leading account assignment object must be assigned for the entire object validity. The account assignment object can change during the validity of the object. However, no overlaps or gaps may occur. Usable objects that belong to the same portfolio ID can use the same or different leading account assignment objects. A leading account assignment object used for a portfolio ID cannot be used as the leading account assignment object in another portfolio ID.Choose Apply.Optional:For the Measurement section, choose Create and make the following entries.Measurement Type: <Select a measurement type>Amount: <Amount of the measurement>Choose Apply.Choose Create. | The usable object is created. |  |

### Create Usable Object with Portfolio Structure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Contract Specialist - Leasing or Real Estate Specialist - Location Management. | The Start page appears. |  |
| 2 | Open Manage Usable Objects | Open Manage Usable Objects. | The Manage Usable Objects screen appears. |  |
| 3 | Create Usable Objects | Choose Create and make the following entries.In the Header section:Usable Object Name: <Your object name>Usage Category: Usable Object with Portfolio Structure (UP)Usable Object Usage Type : <Select a usage type, for example, Office Building (SU06)>Company Code: <Select a company code, for example, Company Code (1010) >Usable Object: <Your object ID in case of external number range, otherwise leave the field empty>In the General Information section:Building/Land Object Number: <Select the architecture object (building/land) to which the usable object refers (parent object)>Authorization Group (optional): <Select an authorization group (this field is only visible if an authorization group is configured)>Ownership ID: <Select an ownership ID, for example, Lease-In (S001)>Validity Start Date: <Date from which your object is valid, for example, current date>Validity End Date: <Date until which your object is valid>In the Leading Account Assignment Object section, choose Create and make the following entries.Object Type of Assigned Object: <Select an object type, for example, Cost Center (KS)>Account Assignment Object: <Your account assignment object>Note A leading account assignment object must be assigned for the entire object validity. The account assignment object can change during the validity of the object. However, no overlaps or gaps may occur. Usable objects that belong to the same building or land can use the same or different leading account assignment objects. A leading account assignment object used for a building or land cannot be used as the leading account assignment object in another building or land.Choose Apply.In the Architecture Object Usage section, choose Create and make the following entries.Note Uable objects require the use of the Master Data Integration service on the BTP (MDI) to establish the relationship to real estate architecture objects provided by an external application.Architecture Object Type: <Select the architecture object type, for example, Building (S2BU)>Architecture Object Number: <Select the architecture object, that is represented by the usable object>Note You can group several real estate architecture objects together to one usable object.Optional:In the System Status section, choose Lock for Intercompany Setup if you want to prevent that the rentable objects (RP) synchronized from a third party real estate management solution will be automatically assigned to usable objects as long as your intercompany setup isn't finished.Your usable object has the status Intercompany Rental Only which prevents an external rental.Choose Unlock for Intercompany setup after you have finished the intercompany setup.For the Measurement section, choose Create and make the following entries.Measurement Type: <Select a measurement type>Amount: <Amount of the measurement>Choose Apply.Choose Create. | The usable object is created. |  |

### Create Rentable Object Without Portfolio Structure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Contract Specialist - Leasing or Real Estate Specialist - Location Management. | The Start page appears. |  |
| 2 | Open Manage Rentable Object | Open Manage Rentable Object. | The Manage Rentable Objects screen appears. |  |
| 3 | Create Rentable Objects | Choose Create and make the following entries.In the Header section:Rentable Object Name: <Your object name>Usage Category: Rentable Object w/o Portfolio Structure (RW)Rentable Object Usage Type : <Select a usage type, for example, Vehicles (SR04)>Company Code: <Select a company code, for example, Company Code (1010) >Rentable Object: <Your object ID in case of external number range, otherwise leave the field empty>In the General Information section:Rentable Object Category: <Select a rentable object category, for example, External (E)>Authorization Group (optional): <Select an authorization group (this field is only visible if an authorization group is configured)>Validity Start Date: <Date from which your object is valid, for example, current date>Validity End Date: <Date until which your object is valid>In the Usable Object Assignment section, choose Create and make the following entries.Usable Object: <Assign the usable object to which the rentable object refers>Choose Apply.Optional:For the Measurement section, choose Create and make the following entries.Measurement Type: <Select a measurement type>Amount: <Amount of the measurement>Choose Apply.Choose Create. | The rentable object is created. |  |

### Change Rentable Object with Portfolio Structure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Contract Specialist - Leasing or Real Estate Specialist - Location Management. | The Start page appears. |  |
| 2 | Open Manage Rentable Object | Open Manage Rentable Object. | The Manage Rentable Objects screen appears. |  |
| 3 | Change Rentable Objects | Search for the Rentable Object with the object ID.Select the Rentable Object. Choose Edit and make the following entries.In the General Information section:Authorization Group (optional): <Select an authorization group (this field is only visible if an authorization group is configured)>In the Usable Object Assignment section, the following entry can be created or maintained:Usable Object: <Assign the usable object to which the rentable object refers>Note Please note there can be only one assignment here.Choose Apply.Optional:In the Measurement section, the following entry can be created or maintained:Measurement Type: <Select a measurement type>Amount: <Amount of the measurement>Choose Apply.Choose Save. | The rentable object is changed. |  |

### Create Intercompany Rentable Object with Portfolio Structure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Contract Specialist - Leasing or Real Estate Specialist - Location Management. | The Start page appears. |  |
| 2 | Open Manage Rentable Object | Open Manage Rentable Object. | The Manage Rentable Objects screen appears. |  |
| 3 | Create Rentable Objects | Choose Create and make the following entries.In the Header section:Rentable Object Name: <Your object name>Usage Category: Intercompany Rentable Object with portfolio structure (I3)Rentable Object Usage Type: <Select a usage type, for example, LO Office ICO (SRI1)>Company Code: <Select a company code, for example, Company Code (1010)>Rentable Object: <Your object ID in case of external number range, otherwise leave the field empty>In the General Information section:Building/Land Object Number mandatory:Building/Land Object Number: <Select the architecture object (building/land) to which the intercompany rentable object refers (parent object)>Authorization Group (optional): <Select an authorization group (this field is only visible if an authorization group is configured)>Validity Start Date: <Date from which your object is valid, for example, current date>Validity End Date: <Date until which your object is valid>In the Usable Object Assignment section, make the following entries.Usable Object: <Assign the usable object can be an intercompany usable object (I1) or a non intercompany usable object (UP) to which the intercompany rentable object refers>Choose Apply.For the Architecture Object Usage section, choose Create and make the following entries.Architecture Object Type: <Select the architecture object type, for example, Room (S4RO)>Architecture Object Number: <Select the architecture object, that is represented by the usable object>Measurement Based Usage: <As defaulted, Yes>Choose Enter Full Screen in the top right. In Architecture Usage Measurement, choose Create and make the following entries:Measurement Type: <Your measurement type>, for example, Office Area (SG11)Amount: <Your amount>Validity Start Date: <Date from which your object is valid>Validity End Date: <Date until which your object is valid>Choose Apply.Choose Create. | The rentable object is created. |  |

### Create Intercompany Rentable Object Without Portfolio Structure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Contract Specialist - Leasing or Real Estate Specialist - Location Management. | The Start page appears. |  |
| 2 | Open Manage Rentable Object | Open Manage Rentable Object. | The Manage Rentable Objects screen appears. |  |
| 3 | Create Rentable Objects | Choose Create and make the following entries.In the Header section:Rentable Object Name: <Your object name>Usage Category: Intercompany Rentable Object without portfolio structure (I4)Rentable Object Usage Type: <Select a usage type, for example, LO Office Equip. ICO (SRI2)>Company Code: <Select a company code, for example, Company Code (1010)>Rentable Object: <Your object ID in case of external number range, otherwise leave the field empty>In the General Information section:Authorization Group (optional): <Select an authorization group (this field is only visible if an authorization group is configured)>Validity Start Date: <Date from which your object is valid, for example, current date>Validity End Date: <Date until which your object is valid>In the Usable Object Assignment section, choose Create and make the following entries.Usable Object: <Assign the usable object can be an intercompany usable object (I2) or a non intercompany usable object (UW) to which the intercompany rentable object refers>Choose Apply.Optional:For the Measurement section, choose Create and make the following entries.Measurement Type: <Select a measurement type>Amount: <Amount of the measurement>Choose Apply.Choose Create. | The rentable object is created. |  |

### Create Intercompany Usable Object with Portfolio Structure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Contract Specialist - Leasing or Real Estate Specialist - Location Management. | The Start page appears. |  |
| 2 | Open Manage Usable Objects | Open Manage Usable Objects. | The Manage Usable Objects screen appears. |  |
| 3 | Create Usable Objects | Choose Create and make the following entries.In the Header section:Usable Object Name: <Your object name>Usage Category: Intercompany Usable Object with portfolio structure (I1)Usable Object Usage Type: <Select a usage type, for example, LI Office ICO (SUI1)>Company Code: <Select a company code, for example, Company Code (1020)>Usable Object: <Your object ID in case of external number range, otherwise leave the field empty>In the General Information section:Building/Land Object Number: <Select the architecture object (building/land) to which the intercompany usable object refers (parent object)>Authorization Group (optional): <Select an authorization group (this field is only visible if an authorization group is configured)>Note The Validity Start Date and the Validity End Date will be determined from the assigned Intercompany Rentable Object.In the Leading Account Assignment Object section, choose Create and make the following entries.Object Type of Assigned Object: <Select an object type, for example, Cost Center (KS)>Account Assignment Object: <Your account assignment object>Note A leading account assignment object must be assigned for the entire object validity. The account assignment object can change during the validity of the object. However, no overlaps or gaps may occur. Usable objects that belong to the same building or land can use the same or different leading account assignment objects. A leading account assignment object used for a building or land cannot be used as the leading account assignment object in another building or land.Choose Apply.In the Intercompany Rentable Object Assignment section, choose Create and make the following entries.Intercompany Rentable Object: <Assign the intercompany rentable object to which the intercompany usable object refers>Choose Apply.Note The scope of intercompany lease-in is limited to the leased-out scope by the affiliated company. An intercompany rentable object from the lessor company code must be assigned.Optional:In the System Status section, choose Lock for Intercompany Setup if you want to prevent that the rentable objects (RP) synchronized from a third party real estate management solution will be automatically assigned to usable objects as long as your intercompany setup isn't finished.Your intercompany usable object has the status Intercompany Rental Only which prevents an external rental.Choose Unlock for Intercompany setup after you have finished the intercompany setup.For the Measurement section, choose Create and make the following entries.Measurement Type: <Select a measurement type>Amount: <Amount of the measurement>Choose Apply.Choose Create. | The usable object is created. |  |

### Create Intercompany Usable Object Without Portfolio Structure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Contract Specialist - Leasing or Real Estate Specialist - Location Management. | The Start page appears. |  |
| 2 | Open Manage Usable Objects | Open Manage Usable Objects. | The Manage Usable Objects screen appears. |  |
| 3 | Create Usable Objects | Choose Create and make the following entries.In the Header section:Usable Object Name: <Your object name>Usage Category: Intercompany Usable Object without portfolio structure (I2)Usable Object Usage Type: <Select a usage type, for example, LI Office Equip. ICO (SUI2)>Company Code: <Select a company code, for example, Company Code (1020)>Usable Object: <Your object ID in case of external number range, otherwise leave the field empty>In the General Information section:Portfolio ID (optional): <Select a portfolio ID, for example, Office Appliances (S501)>Authorization Group (optional): <Select an authorization group (this field is only visible if an authorization group is configured)>Note The Validity Start Date and the Validity End Date will be determined from the assigned Intercompany Rentable Object.In the Leading Account Assignment Object section, choose Create and make the following entries.Object Type of Assigned Object: <Select an object type, for example, Cost Center (KS)>Account Assignment Object: <Your account assignment object>Note A leading account assignment object must be assigned for the entire object validity. The account assignment object can change during the validity of the object. However, no overlaps or gaps may occur. Usable objects that belong to the same building or land can use the same or different leading account assignment objects. A leading account assignment object used for a building or land cannot be used as the leading account assignment object in another building or land.Choose Apply.In the Intercompany Rentable Object Assignment section, choose Create and make the following entries.Intercompany Rentable Object: <Assign the intercompany rentable object to which the intercompany usable object refers>Note The scope of intercompany lease-in is limited to the leased-out scope by the affiliated company. An intercompany rentable object from the lessor company code must be assigned.Choose Apply.Optional:For the Measurement section, choose Create and make the following entries.Measurement Type: <Select a measurement type>Amount: <Amount of the measurement>Choose Apply.Choose Create. | The usable object is created. |  |

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
- related-to :: [[17-leasing-and-real-estate/sap-s-4hana-cloud-public-edition-mds-7ad-523]]
- related-to :: [[17-leasing-and-real-estate/sap-s-4hana-cloud-public-edition-mds-7ad-525]]
- related-to :: [[17-leasing-and-real-estate/script-de-dados-mestre-criar-objeto-de-locacao-mds-7ad-524]]
- related-to :: [[17-leasing-and-real-estate/script-de-datos-maestros-crear-objeto-de-alquiler-mds-7ad-522]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7AD_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 39,203 chars in the whole document
