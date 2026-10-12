---
id: 11-inventory-warehouse-and-transportation/serial-number-management-in-logistics-bll-ae-test-script-1284
title: Serial Number Management in Logistics (BLL_AE) Test Script (BLL_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item BLL_AE: creating, maintaining and displaying serial numbers, history, status and logs (AE localization)."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/serial-number-management]
aliases: [BLL_S4CLD2608_BPD_EN_AE]
keywords: [Serial Number Management, serial number master data, serial number history, serial number status, serial number logs, test scripts, serial number changes, business roles, initial stock posting, sample master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BLL_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1284
topic: 11-inventory-warehouse-and-transportation/serial-number-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Serial Number Management in Logistics (BLL_AE) Test Script (BLL_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BLL_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Serial Number Management** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Serial Number Management in Logistics (BLL_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Serial Number Management in Logistics (BLL_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232862209)

[2 Prerequisites 4](#_Toc232862210)

[2.1 System Access 4](#_Toc232862211)

[2.2 Roles 4](#_Toc232862212)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232862213)

[2.4 Business Conditions 6](#_Toc232862214)

[2.5 Preliminary Steps 6](#_Toc232862215)

[2.5.1 Open a New Material Management (MM) Period 6](#_Toc232862216)

[2.5.2 Initialize Material Stock 6](#_Toc232862217)

[3 Overview Table 8](#_Toc232862218)

[4 Test Procedures 9](#_Toc232862219)

[4.1 Create Serial Number Master Data (Optional) 9](#_Toc232862220)

[4.2 Maintain Serial Number Master Data 10](#_Toc232862221)

[4.3 Display Serial Number Data 12](#_Toc232862222)

[4.4 Display Serial Number History 13](#_Toc232862223)

[4.4.1 Display Serial Number History 13](#_Toc232862224)

[4.4.2 Display Serial Number History (Alternative) 14](#_Toc232862225)

[4.5 Display Serial Number Status 15](#_Toc232862226)

[4.6 Display Serial Number Action Log 16](#_Toc232862227)

[4.6.1 Display Serial Number Change Log 16](#_Toc232862228)

[4.6.2 Display Serial Number Action Log 17](#_Toc232862229)

[4.7 Display Serial Number Changes 18](#_Toc232862230)

## Purpose

Overview

This scope item enables you to serialize and thus differentiate between individual material items. The history of serialized items enables tracking during goods movements. In this way, it's possible to carry out root cause analysis for any issues with materials.

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
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |
| Storage Location | 331R | Storage Location Returns |  |
| Company Code | 3310 |  |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing group | 001 / 002 | Group 001 / Group 002 | depending on material |
| Vendor | 33300001 | Domestic UAE Supplier 1 |  |
| Material | TG20 | Trading Good for Reg. Trading (reorder point planning) | See sections Business Conditions and Preliminary Steps. |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNE | Create Supplier Master - MDS |

### Business Conditions

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |
| BMC - Core Inventory Management | The materials must be available in stock which is created using the Manage Stock (F1062) or Transfer Stock - In-Plant (F1061) app described in Core Inventory Management (BMC). |

### Preliminary Steps

#### Open a New Material Management (MM) Period

External Process

For this activity, run the following step from the BNZ to close the Material Management period and open a new posting period:

Closing MM Period and Opening New Posting Period

#### Initialize Material Stock

Purpose

In a real business case, the materials are usually purchased from external suppliers. For this test, we post initial stock directly to the storage locations. This process step shows you how to initialize material stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Input Material | Make the following entries and choose Enter:Material: TG20Plant: Plant 1 AE (3310) |  |  |
| 4 | Select Stock | Select the icon beside the stock that you want to add initial stock, for example:Storage Location: 331AUnrestricted-Use Stock | The Manage Stock dialog box opens and is prefilled with the Storage Location, Stock Type and Current Quantity you entered in previous steps. |  |
| 5 | Add Initial Stock | Make the following entries and choose Post:Special Stock Type: Keep default as Standard stockDocument Date: <Today>Posting Date: <Today>Stock Change: Initial EntryQuantity: Enter a number, for example, 100Serial Numbers: Select search help icon and go to dialog Assign Serial Numbers; Choose Auto-Create and Apply. | The system displays the following message. The stock has been added.1 document has been created: Material Document XXXXXXXXXX/20XX |  |

## Overview Table

This scope item consists of the process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Serial Number Master Data (Optional)](#unique_10) [page ] 9 | Inventory Manager | Manage Material Serial Numbers (F6879) | The serial number master data is created. |
| [Maintain Serial Number Master Data](#unique_11) [page ] 10 | Inventory Manager | Manage Material Serial Numbers (F6879) | The serial number master data is maintained. |
| [Display Serial Number Data](#unique_12) [page ] 12 | Inventory Manager | Display Material Serial Number - IQ03 (IQ03) | The system displays the serial number data details. |
| [Display Serial Number History](#unique_13) [page ] 13 | Inventory Manager | Serial Number History (F7368) | The system displays serial number history. |
| [Display Serial Number History (Alternative)](#unique_14) [page ] 14 | Inventory Manager | Display Material Serial Number - IQ03 (IQ03) | The system displays serial number history. |
| [Display Serial Number Status](#unique_15) [page ] 15 | Inventory Manager | Display Material Serial Number - IQ03 (IQ03) | The system displays the status of the serial number. |
| [Display Serial Number Change Log](#unique_16) [page ] 16 | Inventory Manager | Serial Number History (F7368) | The system displays the details of the serial number usage list. |
| [Display Serial Number Action Log](#unique_17) [page ] 17 | Inventory Manager | Display Material Serial Number - IQ03 (IQ03) | The system displays the details of serial number action log. |
| [Display Serial Number Changes](#unique_18) [page ] 18 | Inventory Manager | Display Material Serial Number - IQ03 (IQ03) | The system displays the serial number changes. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Serial Number Master Data (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create serial numbers for the material in system.

|  |
| --- |
| Note Serial numbers are created in a sequential manner (like 1, 2, 3) in the system. This is automatically handled in the solution. With the BAdI LOSN_CBO_SERIAL_NUMBER_INT and the developer extensibility BADl LOSN_SER_NUM_INT_CREATE for public cloud, we provide the flexibility on handling the serial number creation function to create serial numbers automatically in accordance with a custom pattern.BAdI can be used in the following situations:Creation of serial numbers based on different business procedures, for example, goods receipt from purchase order or production order.Creation of serial numbers via Create Material Serial Number (IQ01) as a Master Data Specialist - Maintenance Management if no serial number is entered. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Material Serial Numbers (F6879). | The Manage Material Serial Numbers screen displays. |  |
| 3 | Create a Single Serial Number | Choose Create.Make the following entries in the Create dialog box and choose Continue:Material: TG20Serial Number: <Serial Number>Equipment Category: for example, Serial Numbers in Logistics (X)On the Manage Material Serial Numbers screen, make the following entry:Stock Type: Unrestricted-Use Stock (01)Choose Create. | The material serial number is created and saved. The Manage Material Serial Numbers screen displays. |  |
| 4 | Return to the Initial Screen | Choose Back. | The Manage Material Serial Numbers screen displays with the Material Serial Numbers list. |  |
| 5 | Create Mass Material Serial Numbers (Optional) | Choose Mass Create.Make the following entries in the dialog box:Material: TG20Category: for example, Serial Numbers in Logistics (X)From Serial Number: <First serial number>To Serial Number: <Last serial number>Choose Mass Create. | The Information screen displays. The Mass Material Serial Numbers Mass Creation job is scheduled. |  |

### Maintain Serial Number Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You have already created serial numbers in the system. Manual adjustment is needed for serial number records.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Material Serial Numbers (F6879). | The Manage Material Serial Numbers screen displays. |  |
| 3 | Search Serial Number | Make the following entries and press Enter:Material: TG20Serial Number (Optional): <The serial number you just created> | The list of serial numbers displays. |  |
| 4 | Choose Serial Number | Choose a row of serial number from the list. | The Serial Number Data details page displays. |  |
| 5 | Change Serial Number (Optional) | Choose Additional Functions and select Change Serial Number from the dropdown list.Enter the new serial number and choose Change Serial Number. | The serial number is changed. |  |
| 6 | Change Material Number (Optional) | Choose Additional Functions and select Change Material from the dropdown list. Enter the new material number and choose Change Material. When doing this, the system always checks whether the new combination of material and serial number already exists in the system. If the combination does exist, the change is not authorized.The material changes are not authorized within the scope of master data management, if the serial number is currently in stock. | The material number is changed. |  |
| 7 | Change Category (Optional) | Choose Additional Functions and select Change Equipment Category from the dropdown list. Enter the new category and choose Change Equipment Category. The new category must be the same reference type as the current one. | The category is changed. |  |
| 8 | Change Stock Information (Optional) | Choose Edit to change stock information. The following is an example:Stock Type: Unrestricted-Use Stock (01)Plant: Plant 1 AE (3310)Storage Location: Std. storage 1 (331A)An error message may pop out when you maintain relevant information in the Stock Information section depending on the configuration of the serial number profile. | The stock information is changed. |  |

### Display Serial Number Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You have already created serial numbers in the system. Now you want to see the content of the serial number as well as history, status, usage list, logs, and more.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Display Material Serial Number - IQ03 (IQ03). | The Display Material Serial Number: Initial screen displays. |  |
| 3 | Maintain Master Data | Enter the following data and press Enter:Material: TG20Serial Number: <serial number> | The Display Material Serial Number: SerNo Detail screen displays. |  |

### Display Serial Number History

With the history for the master record of the serial numbers, you can view which operations affected the serial numbers (document data).

You can find all documents that have been created for the serial number here:

- Production order
- Handling unit
- Physical inventory
- Sales order
- Delivery (inbound delivery, outbound delivery)
- Inspection lot
- Goods document

Different colors are used in the history to map the document data. The legend shows you the meaning of the individual colors.

Every field in the history has a quick info text.

#### Display Serial Number History

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Serial number history shows the history of the serial number.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Serial Number History (F7368). | The Serial Number History screen displays. |  |
| 3 | Filter Data | Make the following entries and choose Go:Material: TG20Plant: for example, 3310 | The list of serial numbers for the material and plant displays. |  |
| 4 | Display History | Choose the row of a serial number in the list.On the right screen, choose the History tab. | The detailed history displays. |  |
| 5 | Back to Initial Screen | Choose Back to go back to the Serial Number History screen. | The Serial Number History screen displays. |  |

#### Display Serial Number History (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Serial number history shows the documents where the serial number was touched (for example, material movements, deliveries and others).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Display Material Serial Number - IQ03 (IQ03). | The Display Material Serial Number: Initial screen displays. |  |
| 3 | Maintain Master Data | Make the following entries and press Enter:Material: TG20Serial Number: <serial number> | The Display Material Serial Number: SerNo Detail screen displays. |  |
| 4 | Display History | On the Display Material Serial Number: SerNo Detail screen, choose the SerData tab and choose History.To view the legend, from the menu, choose Settings > Color legend .Choose Continue. |  |  |
| 5 | Back to Initial Screen | Choose Back to go back to the Display Material Serial Number: SerNo Detail screen. | The Display Material Serial Number: SerNo Detail screen displays. |  |

### Display Serial Number Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Serial number status shows the current status of the serial number.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Display Material Serial Number - IQ03 (IQ03). | The Display Material Serial Number: Initial screen displays. |  |
| 3 | Maintain Master Data | Make the following entries and press Enter:Material: TG20Serial Number: <serial number> | The Display Material Serial Number: SerNo Detail screen displays. |  |
| 4 | Display Status | On the Display Material Serial Number: SerNo Detail screen, choose the Status icon.If you choose All Statuses, the system displays the statuses that can be assigned to the serial number. If you choose Active Status, the system hides the statuses that are not active. | The system displays the status of the serial number. There could be more than one active status: AVLB Available ECUS At customer site EDEL Assigned in delivery note ESTO In the warehouse. |  |
| 5 | Back to Initial Screen | Choose Back to go back to the Display Material Serial Number: SerNo Detail screen. | The Display Material Serial Number: SerNo Detail screen displays. |  |

### Display Serial Number Action Log

#### Display Serial Number Change Log

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The serial number change log shows what happened to the serial number, who made the change, and when it was made.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Serial Number History (F7368). | The Serial Number History screen displays. |  |
| 3 | Enter Serial Number Selection Criteria | Make the following entries and press Enter:Material: TG20Plant: 3310 | A list of serial numbers matching the selection criteria is displayed. |  |
| 4 | Display Serial Number Details | In the Serial Numbers list, choose a row of serial number. | The serial number history details are displayed. |  |
| 5 | Display Change Log | Choose Display Change Log. | The Change Log screen displays. |  |

#### Display Serial Number Action Log

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Serial number action log shows what happened to the serial number by whom and when.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Display Material Serial Number - IQ03 (IQ03). | The Display Material Serial Number: Initial screen displays. |  |
| 3 | Maintain Master Data | Make the following entries and press Enter:Material: TG20Serial Number: <serial number> | The Display Material Serial Number: SerNo Detail screen displays. |  |
| 4 | Display Status | On the Display Material Serial Number: SerNo Detail screen, from the menu, choose Extras > Action log . | The Action Log is shown. |  |
| 5 | Back to Initial Screen | Choose Continue to go back to the Display Material Serial Number: SerNo Detail screen. | The Display Material Serial Number: SerNo Detail screen displays. |  |

### Display Serial Number Changes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Serial number changes show per each field when, what and by whom it was changed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Display Material Serial Number - IQ03 (IQ03). | The Display Material Serial Number: Initial screen displays. |  |
| 3 | Maintain Master Data | Make the following entries and press Enter:Material: TG20Serial Number: <serial number> | The Display Material Serial Number: SerNo Detail screen displays. |  |
| 4 | Display Status | On the Display Material Serial Number: SerNo Detail screen, from the menu, choose Extras > Display changes . | The Change Documents screen displays. |  |
| 5 | Back to Initial Screen | Choose Back to go back to the Display Material Serial Number: SerNo Detail screen. | The Display Material Serial Number: SerNo Detail screen displays. |  |

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
- see-also :: [[10-procurement/complementary-procurement-functions-2tw-ae-test-script-sap-s-4hana-clo]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BLL_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 28,876 chars in the whole document
