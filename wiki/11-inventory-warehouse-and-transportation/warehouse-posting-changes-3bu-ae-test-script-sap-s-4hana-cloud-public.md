---
id: 11-inventory-warehouse-and-transportation/warehouse-posting-changes-3bu-ae-test-script-sap-s-4hana-cloud-public
title: "Warehouse Posting Changes (3BU_AE) - Test Script, SAP S/4HANA Cloud Public Edition (3BU_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 3BU_AE: posting changes in the warehouse (unrestricted to blocked/quality stock) via warehouse, inventory management or synchronous routes."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-posting-changes]
aliases: [3BU_S4CLD2608_BPD_EN_AE]
keywords: [Warehouse Posting Changes, stock type change, transfer posting, synchronous goods movements, warehouse tasks, radio frequency devices, business roles, test data, preliminary steps, customer returns]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3BU_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-924
topic: 11-inventory-warehouse-and-transportation/ewm-posting-changes
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Warehouse Posting Changes (3BU_AE) - Test Script, SAP S/4HANA Cloud Public Edition (3BU_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3BU_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Warehouse Posting Changes** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Warehouse Posting Changes (3BU_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232852271)

[2 Prerequisites 4](#_Toc232852272)

[2.1 System Access 4](#_Toc232852273)

[2.2 Roles 4](#_Toc232852274)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232852275)

[2.4 Business Conditions 6](#_Toc232852276)

[2.5 Preliminary Steps 6](#_Toc232852277)

[2.5.1 Define Default Values for Warehouse Clerk (WM) 6](#_Toc232852278)

[2.5.2 Define Default Values for Warehouse Operative (WM) 7](#_Toc232852279)

[3 Overview Table 8](#_Toc232852280)

[4 Test Procedures 9](#_Toc232852281)

[4.1 Option 1: Posting Changes Triggered in Warehouse 9](#_Toc232852282)

[4.1.1 Posting Change 9](#_Toc232852283)

[4.2 Option 2: Posting Changes Triggered in Inventory Management 11](#_Toc232852284)

[4.2.1 Trigger Transfer Posting 11](#_Toc232852285)

[4.2.2 Create Warehouse Tasks for Posting Changes 12](#_Toc232852286)

[4.3 Option 3: Synchronous Posting Changes 13](#_Toc232852287)

[4.3.1 Create Synchronous Posting Change 13](#_Toc232852288)

[4.4 Confirm Warehouse Task for Posting Changes 15](#_Toc232852289)

[4.4.1 Variant 1: With Fiori App 15](#_Toc232852290)

[4.4.2 Variant 2: With Radio Frequency Devices 16](#_Toc232852291)

[5 Appendix 20](#_Toc232852292)

[5.1 Process Integration 20](#_Toc232852293)

[5.1.1 Preceding Processes 20](#_Toc232852294)

## Purpose

Overview

With this scope item, you can make posting changes (for example, unrestricted to blocked stock) in the warehouse. Posting changes can be triggered in two different ways.

- When an inventory management posting initiates a posting change, it generates an outbound delivery. This delivery is then distributed to the warehouse, recognized as a posting change. Based on this document, you can, for example, create warehouse tasks to move the blocked/quality stock to the clarification zone.
- You can also trigger posting changes by selecting stock and changing the stock type with the help of the warehouse monitor. By doing this, a posting change is triggered, and warehouse tasks are created to move the selected stock to the appropriate storage type, if necessary.

|  |
| --- |
| Note Since SAP S/4HANA 2208 Cloud Essentials edition, the following changes apply to this process:Synchronous goods movements are enabled on warehouse level by default for goods movements that are not related to production or external procurement. These movements are posted now directly to the warehouse. This increases the stock synchronization between Inventory Management and embedded Warehouse Management with no deliveries and warehouse requests. See more details in[Configuration of Other Direct Goods Movements Using Post Goods Movement \| SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/87f9b54f9c4f4e75aff0061860a6589a/3ae43fa9b0614a89bb7e3fa7dde18787.html?q=configuration%20of%20other%20direct%20goods%20movements)However, if you still want to use the deliveries for movements that are not related to production or external procurement with the Post Goods Movement App, you can deactivate the default setting on warehouse level with SSC-UI Activate Synchronous Goods Movements in the Warehouse (ID 105672). In addition, the SSC-UI allows to activate synchronous goods movements for individual movement types. More information can be found in the help document for this SSC-UI. |

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
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Warehouse Clerk (EWM) | SAP_BR_WAREHOUSE_CLERK_EWM | Warehouse Office | SAP_BR_WAREHOUSE_CLERK_EWM |  |
| Warehouse Operative (EWM) | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Warehouse Floor | SAP_BR_WAREHOUSE_OPERATIVE_EWM |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trad.Good 11,PD,Reg.Trading | Storage |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFO | Fixed Bin Storage |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad. | Bulk Storage |
| Material | TG0011 | Trading Good 0011,PD,Regular Proc. | General Storage |
| Material | TG0013 | Trading Good 0013,PD,Regular Proc. | General Storage |
| Plant | 3310 |  |  |
| Storage Location | 335W |  |  |

Organizational Master Data in Warehouse:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Warehouse | 3350 |  |  |
| Custodian | 33413310 |  |  |
| Entitled to Dispose | 33413310 |  |  |

Warehouse-Specific Master Data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Storage Type | S001 | Storage |  |
| Storage Type | SF01 | Fixed Bin Storage |  |
| Storage Type | SB01 | Bulk Storage |  |
| Storage Type | SG01 | General Storage |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| 3KQ | Maintain Warehouse Products Attributes - MDS |
| 3KR | Maintain Storage Bins and Fixed Bin Assignments - MDS |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS master data script. The posting period is up to date. |
| 3BR - Warehouse Inbound Processing | You have completed the step described in the Warehouse Inbound Processing test script so that you have the stock to do the posting changes. |

### Preliminary Steps

#### Define Default Values for Warehouse Clerk (WM)

Purpose

In this step, you can define the default warehouse number for the Warehouse Clerk (EWM).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). |  |  |
| 2 | Choose Avatar | Choose your avatar.Then, choose Settings. |  |  |
| 3 | Enter Default Value | Choose Default Values.Enter the following data:Warehouse Number: 3350.Choose Save. |  |  |

#### Define Default Values for Warehouse Operative (WM)

Purpose

In this step, you can define the default warehouse number for the Warehouse Operative (EWM).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The Fiori launchpad is displayed. |  |
| 2 | Choose Avatar | Choose your avatar.Then, choose Settings. |  |  |
| 3 | Enter Default Value | Choose Default Values.In the Material Management section, enter the following data:Warehouse Number: 3350.Choose Save. |  |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Option 1: [Posting Change](#unique_10) [page ] 9 | Warehouse Clerk (EWM) | Create Posting Changes (/SCWM/MONNAV_CR_PC) | You have posted the stock change. |
| Option 2: [Trigger Transfer Posting](#unique_11) [page ] 11 | Warehouse ClerkInventory Manager | Transfer Stock - In-Plant (F1061) | You have triggered the transfer posting. |
| Option 2: [Create Warehouse Tasks for Posting Changes](#unique_12) [page ] 12 | Warehouse Clerk (EWM) | Process Posting Change Item (/SCWM/MONNAV_PROC_PC) | You have created warehouse tasks for posting changes. |
| Option 3:[Create Synchronous Posting Change](#unique_13) [page ] 13 | Warehouse ClerkInventory Manager | Post Goods Movement (MIGO) | You have created synchronous posting change. |
| [Confirm Warehouse Task for Posting Changes](#unique_14) [page ] 15 | Warehouse Operative (EWM) | Process Warehouse Tasks (F4595) | You have confirmed the warehouse task. |

## Test Procedures

### Option 1: Posting Changes Triggered in Warehouse

#### Posting Change

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Posting change is initiated from the warehouse. For example, the Warehouse Clerk (EWM) wants to change the stock type from Unrestricted Use to Quality Inspection or to Blocked Stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Create Posting Changes(/SCWM/MONNAV_CR_PC). | The Enter warehouse number dialog box appears. |  |
| 3 | Enter Warehouse Number | In the Enter warehouse number dialog box, make the following entries:Warehouse Number: 1750.Note: Skip this step if there's no dialog box to enter the warehouse number. |  |  |
| 4 | Choose Continue. | Choose Continue. | The /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box appears. |  |
| 5 | Enter Product | In the /SCWM/SAPLSTOCK_OVERVIEW_MON dialog box, make the following entries:Product: <product>Note Example: TG11. |  |  |
| 6 | Choose Execute. | Choose Execute. | The Create Posting Change screen appears. |  |
| 7 | Select line | In the table Create Posting Change select the checkbox in one line. |  |  |
| 8 | Choose More Methods > Change Stock Type. | Choose More Methods > Change Stock Type. | The Change Stock Type dialog box appears. |  |
| 9 | Enter data | In the Change Stock Type dialog box, make the following entries:Stock Type: Q or B.Qty F. Post. Change: <Enter the quantity that you want to post the stock change for>.Whse Proc. Type: S400. |  |  |
| 10 | Choose Check Input (Enter). | Choose Check Input (Enter). | No error message appears. |  |
| 11 | Choose Create Posting Chg (F8). | Choose Create Posting Chg (F8). | The Display Logs dialog box appears.The following system messages appear:1 stock items created with quantity <quantity>Stock type for 1 stock items changed from F to BNote Example: if you entered stock type B and the stock type before was F.Warehouse task <number> createdWarehouse task <number> createdWarehouse order creation startedWarehouse order <number> created |  |
| 12 | Note down the warehouse task number. | Note down the warehouse task number. |  |  |
| 13 | Choose Continue. | In the Display Logs dialog box, choose Continue (Enter). | In the table Create Posting Change a new line with data you entered before is displayed. |  |

### Option 2: Posting Changes Triggered in Inventory Management

#### Trigger Transfer Posting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Posting change is initiated from inventory management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Transfer Stock - In-Plant(F1061). | The Transfer Stock – In-Plant screen is displayed. |  |
| 3 | Open Stock Overview | On the Transfer Stock – In-Plant screen, make the following entries:Material: TG11Plant: 1710 | The table Material by Storage Location is displayed. |  |
| 4 | Choose Transfer from Stock | Choose the Select icon beside the unrestricted stock for Storage Location175W that you want to transfer from. | The icons besides the other stock quantities change to the Target icon. |  |
| 5 | Choose Transfer to Blocked and Quality Stock | For stock transfer to blocked stock, choose the Target icon beside the blocked stock for Storage Location175W that you want to transfer to. | The Transfer Stock – In-Plant dialog box appears. |  |
| 6 | Enter quantity | In the Transfer Stock – In-Plant dialog box, make the following entries:Quantity: <your quantity> PC |  |  |
| 7 | Post | Choose Post. | The Success dialog box appears.The following system message appears:1 document has been created:Outbound Delivery Document<document number> |  |
| 8 | Choose OK. | In the Success dialog box, Choose OK. | The following system message appears:Outbound Delivery <document number> created |  |

#### Create Warehouse Tasks for Posting Changes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Clerk (EWM) creates warehouse tasks for posting changes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Process Posting Change Item(/SCWM/MONNAV_PROC_PC). | The /SCWM/SAPLWIP_POSTING_CHANGES dialog box appears. |  |
| 3 | Enter Data | In the SCWM/SAPLWIP_POSTING_CHANGES dialog box, make the following entries:Posting Change: <outbound delivery number from the previous step> |  |  |
| 4 | Choose Execute. | Choose Execute (F8). | The Process Posting ChangeItem screen appears.In the table Process Posting ChangeItem the document is displayed. |  |
| 5 | Select the checkbox | Select the checkbox in the line of the document. |  |  |
| 6 | Create WT in Background | Choose More Methods > Create WT in Background. | The Display Logs dialog box appears.The following system messages appear:Warehouse task <number> createdWarehouse order <number> created |  |
| 7 | Note down the warehouse task number. | Note down the warehouse task number. |  |  |
| 8 | Choose Continue. | In the Display Logs dialog box, choose Continue (Enter). |  |  |

### Option 3: Synchronous Posting Changes

#### Create Synchronous Posting Change

Purpose

This step is create synchronous posting change in Inventory Management and the warehouse. More information can be found in chapter [Purpose](#unique_1) [page ] 1.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as the Warehouse Clerk or Inventory Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement(MIGO). | The Transfer Posting Other screen appears. |  |
| 3 | Enter Data | On the Transfer Posting Other screen, make the following entries:Trans./Event: Transfer PostingReference Document: OtherMovement type: 344 or 322Note Note: Choose Continue if there is dialog box for Change to Default Values. |  |  |
| 4 | Choose Enter | Choose Enter |  |  |
| 5 | Navigate to the Transfer Posting tab. | Navigate to the Transfer Posting tab. |  |  |
| 6 | Enter Material | On the Transfer Posting tab, and make the following entries:Material: <Material Number>, for example TG11Plant: 1710.Location in From section:175W.Location in Dest section: 175W |  |  |
| 7 | Choose Enter | Choose Enter |  |  |
| 8 | Navigate to the Quantity tab. | Navigate to the Quantity tab. |  |  |
| 9 | Enter Quantity | On the Quantity tab make the following entries:Qty in Unit of Entry: <Quantity>.Unit of Entry: <Unit>. |  |  |
| 10 | Choose Enter | Choose Enter |  |  |
| 11 | Navigate to the Warehouse Management tab. | Navigate to the Warehouse Management tab. |  |  |
| 12 | Enter Storage Bin | On the Warehouse Management tab, make the following entries:Storage Bin :<Storage Bin which contains material unrestricted used stock>.Note Example: S001-01-01.Choose Enter. |  |  |
| 13 | Choose Enter | Choose Enter |  |  |
| 14 | Select Item ok Indicator | Select Item OK checkbox. |  |  |
| 15 | Choose Check. | Choose Check. | The following system message appears: Document is O.K. |  |
| 16 | Post | Choose Post. | The following system message appears: Material document <number> posted. |  |
| 17 | Note down the material document number. | Note down the material document number. |  |  |

### Confirm Warehouse Task for Posting Changes

#### Variant 1: With Fiori App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A put-away list / warehouse task list / pick list is printed and handed over to the Warehouse Operative (EWM), who performs the warehouse tasks and confirms them in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Process Warehouse Tasks(F4595). | The Process Warehouse Tasks screen appears. |  |
| 3 | Enter Warehouse Task Number | On the Process Warehouse Tasks screen, make the following entries:Warehouse Task: <WT number noted down in the previous step> |  |  |
| 4 | Choose Go. | Choose Go. |  |  |
| 5 | Select the warehouse task checkbox. | Select the warehouse task checkbox. |  |  |
| 6 | Confirm Warehouse Task | Choose Confirm. | The following system message appears: Warehouse task <number> confirmed. |  |

#### Variant 2: With Radio Frequency Devices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) performs the warehouse tasks and confirms them in the system with mobile Radio Frequency device.

|  |
| --- |
| Note For working with Mobile RF Devices, make sure all the steps as described in the Set-up Instruction guide for scope item 63V - Mobile RF Devices in Warehousing have been performed. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Test RF Environment(/SCWM/RFUI)Note Note Here the App allows you to test working in an RF environment. For working with Mobile RF Devices, see also SAP Note 3048632. |  |  |
| 3 | Enter Data for RFUI | Make the following entries:Whse No: 1750Resource: SHA1-1 or SHR1-1Dflt Dvc.: SE01Note Note Use resource SHA1-1 for stock moving from S001 or into S001, for example queue SO-001 or SI-001Use SHR1-1 for stock movement which does not involve S001, for example queue SO-F01, SO-B01 and etc. |  |  |
| 4 | Choose Enter. | Choose Enter. | More buttons appear. |  |
| 5 | Choose Menu | Choose 01 System-Guided > 02 SystemGuided Queue . | The field Queue is displayed and editable. |  |
| 6 | Enter Queue Name | Make the following entries:Queue: <queue>Note Example:SS-001 Posting change from Standard StorageSS-F01 Posting change from Fixed Bin StorageSS-B01 Posting change from Bulk StorageSS-G01 Posting change from General Storage |  |  |
| 7 | Choose Enter. | Choose Enter. | The editable fieldsPick-HUPack.Mat:appear. |  |
| 8 | Create Picking HU | Make the following entries:Pack.Mat: PMPALLET |  |  |
| 9 | Choose HUCrt. | Choose HUCrt. | The picking HU is created and the number is displayed. |  |
| 10 | Choose Next | Scroll the screen to right with > and choose Next. | The editable fieldsSrc.BinActQtyappear. |  |
| 11 | Enter or Verify the Source Information fields | Make the following entries:Src.Bin: <source bin>Note copy the displayed source bin value into the editable field next to it.Note Example: S001-01-01.ActQty: <quantity>Note copy the displayed value from above into the editable field. |  |  |
| 12 | Choose Enter. | Choose Enter. | The DstBin (Destination Bin) is displayed. |  |
| 13 | Verify the Destination information fields | Make the following entries:DstBin: <destination bin>Note copy the displayed destination bin value into the editable field next to it.Note Example: QUAL-I01 if you chose Stock Type: Q before or CL-AREA if you chose Stock Type: B. |  |  |
| 14 | Choose Enter. | Choose Enter. |  |  |
| 15 | Repeat Steps | Repeat step until no suitable warehouse orders are found. | The following system message appears:E: Suitable warehouseorders were not found(/SCWM/RF_EN056)Note Although this is an error message this confirms that no further processing is required. |  |
| 16 | Choose Enter. | Choose Enter. | The Back button appears. |  |
| 17 | Choose Back | Choose Back | The Logoff button appears. |  |
| 18 | Logoff RFUI | Choose Logoff. | The Save button appears. |  |
| 19 | Choose Save. | Choose Save. | The system leaves the app. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

You may first have completed the following processes and conditions before you start with the test steps.

|  |
| --- |
| Note When running the following preceding processes along with the warehouse processes, make sure the material master data has been extended to your warehouse storage locations and the corresponding warehouse products have been created.Please refer to the Master Data Script BNF to create the storage location data for your material master data.Please refer to the Master Data Script 3KQ to create the corresponding warehouse products. |

| Scope Item ID | Business Condition |
| --- | --- |
| Customer Returns |  |
| BKP - Customer Returns | Complete the activities described in either one of the following options of the test script.In Scenario 1: Goods are Returned to Seller:A return order with follow-up activity 0001 - Receive into Plant was created. The return products were received afterwards. In chapter Perform Material Inspection, you chose the follow-up activity 0011 Transfer to Free Available Stock or 0012 Transfer to Scrap. The posting change delivery gets created for warehouse transfer posting, you then follow the steps below in this test script to fulfil the warehouse ac-tivities.Create Warehouse Tasks for Posting ChangesConfirm Warehouse Task for Posting Changes |
| Returns from Stock Transfer Order |  |
| 2TS - Intercompany Stock Transfer Returns | Complete the activities described in either one of the following options of the test script.The Post Goods Receipt for Inbound Delivery has been done. In chapter Perform Material Inspection, you chose the follow-up activity 0011 Transfer to Free Available Stock or 0012 Transfer to Scrap. The posting change delivery gets created for warehouse transfer posting, you then follow the steps below in this test script to fulfil the warehouse activities.Create Warehouse Tasks for Posting ChangesConfirm Warehouse Task for Posting Changes |
| 5WI - Intra-Company Returns Stock Transfers | Complete the activities described in either one of the following options of the test script.The Post Goods Receipt for Inbound Delivery has been done. In chapter Perform Material Inspection, you chose the follow-up activity 0011 Transfer to Free Available Stock or 0012 Transfer to Scrap. The posting change delivery gets created for warehouse transfer posting, you then follow the steps below in this test script to fulfil the warehouse activities.Create Warehouse Tasks for Posting ChangesConfirm Warehouse Task for Posting Changes |

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

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Sample data lists warehouse 3350, plant 3310 and storage location 335W, but test steps use warehouse 1750, plant 1710 and storage location 175W.

## Connections
- part-of :: [[_cluster]]
- see-also :: [[13-quality-ehs-and-compliance/quality-management-in-stock-handling-1mr-ae-test-script-739]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3BU_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 30,892 chars in the whole document
