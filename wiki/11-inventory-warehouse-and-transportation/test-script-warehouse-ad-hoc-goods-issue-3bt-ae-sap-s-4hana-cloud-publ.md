---
id: 11-inventory-warehouse-and-transportation/test-script-warehouse-ad-hoc-goods-issue-3bt-ae-sap-s-4hana-cloud-publ
title: "Test Script: Warehouse Ad Hoc Goods Issue (3BT_AE) - SAP S/4HANA Cloud Public Edition (3BT_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud test script for scope item 3BT_AE: unplanned warehouse goods issue, scrapping and synchronous goods movements, with roles, data and steps."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-physical-inventory-and-stock-handling]
aliases: [3BT_S4CLD2608_BPD_EN_AE]
keywords: ["EWM Physical Inventory, Scrapping and Ad Hoc Goods Issue", ad hoc goods issue, scope item testing, warehouse tasks, scrapping, warehouse task confirmation, synchronous goods movements, storage location transfer, cost center consumption, radio frequency devices]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3BT_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-923
topic: 11-inventory-warehouse-and-transportation/ewm-physical-inventory-and-stock-handling
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Warehouse Ad Hoc Goods Issue (3BT_AE) - SAP S/4HANA Cloud Public Edition (3BT_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3BT_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **EWM Physical Inventory, Scrapping and Ad Hoc Goods Issue** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Warehouse Ad Hoc Goods Issue (3BT_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232852133)

[2 Prerequisites 4](#_Toc232852134)

[2.1 System Access 4](#_Toc232852135)

[2.2 Roles 4](#_Toc232852136)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232852137)

[2.4 Business Conditions 7](#_Toc232852138)

[2.5 Preliminary Steps 7](#_Toc232852139)

[2.5.1 Define Default Values for Warehouse Clerk (EWM) 7](#_Toc232852140)

[2.5.2 Define Default Values for Warehouse Operative (EWM) 8](#_Toc232852141)

[3 Overview Table 9](#_Toc232852142)

[4 Test Procedures 10](#_Toc232852143)

[4.1 Create Ad-Hoc Warehouse Task (Option 1) 10](#_Toc232852144)

[4.2 Create Posting Change and Warehouse Task for Scrapping (Option 2) 11](#_Toc232852145)

[4.3 Confirm Warehouse Task 12](#_Toc232852146)

[4.3.1 Variant 1: With Fiori App 12](#_Toc232852147)

[4.3.2 Variant 2: With Radio Frequency Devices 13](#_Toc232852148)

[4.4 Post Ad-Hoc Goods Issue 15](#_Toc232852149)

[4.4.1 Post Ad-Hoc Goods Issue to Another Storage Location 15](#_Toc232852150)

[4.4.2 Post Ad-Hoc Goods Issue for Consumption with Cost Center 16](#_Toc232852151)

[4.4.3 Post Ad-Hoc Goods Issue for Scrapping 17](#_Toc232852152)

[4.5 Synchronous Goods Movements for Ad-Hoc Goods Issues 19](#_Toc232852153)

[4.5.1 Post Synchronous Goods Movements to Another Storage Location 19](#_Toc232852154)

[4.5.2 Post Synchronous Goods Movements to Cost Center 20](#_Toc232852155)

[4.5.3 Post Synchronous Goods Movements for Scrapping 22](#_Toc232852156)

[5 Appendix 24](#_Toc232852157)

[5.1 Process Integration 24](#_Toc232852158)

[5.1.1 Preceding Processes 24](#_Toc232852159)

## Purpose

Overview

This scope item can be used to post unplanned goods issues without reference to outbound deliveries. There are various use cases such as scrapping and goods issue to another storage location. For scrapping, you initiate this process by creating a posting change and a warehouse task to move the material to be scrapped from the source bin to the scrapping zone. After the physical goods movement is completed, you post the unplanned goods issue.

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
| Warehouse Clerk (EWM) | SAP_BR_WAREHOUSE_CLERK_EWM | Warehouse Office | SAP_BR_WAREHOUSE_CLERK_EWM |  |
| Warehouse Operative (EWM) | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Warehouse Floor | SAP_BR_WAREHOUSE_OPERATIVE_EWM |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning) | Storage |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad. | Fixed Bin Storage |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFO | Bulk Storage |
| Material | RM124 | RAW124,VB,Consumption,FixedBin |  |
| Material | TG0011 | Trading Good 0011,PD,Regular Proc. | General Storage |
| Material | TG0013 | Trad. Good 0013,PD,Regular Proc. | General Storage |
| Packaging Material | PMPALLET | Pallet |  |
| Packaging Material | PMCARTON | Carton |  |
| Packaging Material | PMWIREBASKET | Wire basket |  |
| Packaging Material | PMPALLET_GTLP | Pallet for GTL |  |
| Packaging Material | PMCARTON_GTL | Carton for GTL |  |
| Packaging Material | PMWIREBASKET_GTL | Wire basket for GTL |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Plant | 3310 |  |  |
| Storage Location | 335W |  |  |
| EWM Warehouse | 3350 |  |  |
| Custodian | 33413310 |  |  |
| Entitled to Dispose | 33413310 |  |  |
| Division | 00 |  |  |
| Distribution Channel | 10 |  |  |
| Shipping Point | 3310 |  |  |
| Ship to party | 33100003 | Domestic UAE Customer 3 |  |
| Sold to party | 33100003 | Domestic UAE Customer 3 |  |
| Carrier | 33300001 | Domestic UAE Supplier 1 |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |
| 2YX | Create Customer-Material Info Record - MDS |
| 3KS | Maintain Production Supply Area - MDS |
| 3KR | Maintain Storage Bins and Fixed Bin Assignments - MDS |
| 3KQ | Maintain Warehouse Products Attributes - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS (All Scope Items) | A new posting period was created as part of process BNZ - Create New Open MM Posting Period - MDS (Master Data Script).The posting period is up to date. |
| 2Q2 - Data Migration to SAP S/4HANA from Staging or3BR - Warehouse Inbound Processing (All Scope Items) | You can use the Migration Cockpit for setting up your Warehouse Stock with a provided template.Alternatively, you can also get stock using scope item Warehouse Inbound Processing (3BR). Scope item 3BR is used as a predecessor for the Ad-hoc Goods Issue. |

### Preliminary Steps

#### Define Default Values for Warehouse Clerk (EWM)

Purpose

In this step, you define the default warehouse number for Warehouse Clerk (EWM).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on to SAP Fiori launchpad | Open the SAP Fiori Launchpad as Warehouse Clerk (EWM) |  |  |
| 2. | Choose App | Choose tab page Warehouse ProcessingOpen App Change Inbound Deliveries - Deliveries (F1706). |  |  |
| 3. | Choose the User Icon | Choose the Icon for the logon user.Choose Settings. |  |  |
| 4. | Enter Default Value | Choose Default ParametersAnd make the following entry:Warehouse Number.: 3350Choose Save. |  |  |

#### Define Default Values for Warehouse Operative (EWM)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on to SAP Fiori launchpad | Open the SAP Fiori Launchpad as Warehouse Operative (EWM) |  |  |
| 2. | Choose the User Icon | Choose the Icon for the logon user.Choose Settings. |  |  |
| 3. | Enter Default Value | Choose Default Values.And make the following entry in the section Material Management :Warehouse Number.: 3350Choose Save. |  |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App / Transaction |
| --- | --- | --- |
| [Create Ad-Hoc Warehouse Task (Option 1)](#unique_10) [page ] 10 | SAP_BR_WAREHOUSE_CLERK_EWM | Create Product Warehouse Tasks (/SCWM/MONNAV_CR_P_WT) |
| [Create Posting Change and Warehouse Task for Scrapping (Option 2)](#unique_11) [page ] 11 | SAP_BR_WAREHOUSE_CLERK_EWM | Create Posting Changes (/SCWM/MONNAV_CR_PC) |
| Confirm Warehouse Task[Variant 1: With Fiori App](#unique_12) [page ] 12 | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Process Warehouse Tasks (F4595) |
| Confirm Warehouse Task[Variant 2: With Radio Frequency Devices](#unique_13) [page ] 13 | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Test RF Environment (/SCWM/RFUI) |
| Post Ad-Hoc Goods Issue[Post Ad-Hoc Goods Issue to Another Storage Location](#unique_14) [page ] 15 | SAP_BR_WAREHOUSE_CLERK_EWM | Post Goods Issue - Unplanned (/SCWM/ADGI) |
| Post Ad-Hoc Goods Issue[Post Ad-Hoc Goods Issue for Consumption with Cost Center](#unique_15) [page ] 16 | SAP_BR_WAREHOUSE_CLERK_EWM | Manage Physical Stock - Products (F5340) |
| Post Ad-Hoc Goods Issue[Post Ad-Hoc Goods Issue for Scrapping](#unique_16) [page ] 17 | SAP_BR_WAREHOUSE_CLERK_EWM | Manage Physical Stock - Products (F5340) |
| [Synchronous Goods Movements for Ad-Hoc Goods Issues](#unique_17) [page ] 19 | SAP_BR_WAREHOUSE_CLERK | Post Goods Movement (MIGO) |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

Please consider, Ad-hoc Warehouse Tasks can be executed also via the app Create HU Warehouse Tasks which has minor differences in the executable steps.

### Create Ad-Hoc Warehouse Task (Option 1)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is for creating an ad-hoc warehouse task to move stock from a storage type to the final goods issue storage type. This can be required for immediate situations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on to SAP Fiori launchpad | Open the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open SAP Fiori Create Product Warehouse Tasks (/SCWM/MONNAV_CR_P_WT). | The Create Product Warehouse Tasks (/SCWM/MONNAV_CR_P_WT) screen displays. |  |
| 3. | Decide your filter criteria | Enter Storage Type: For example, S001Choose Execute. | The Create Product Warehouse Task screen displays. |  |
| 4. | Choose your Stock | Choose one of the stock lines and select More Methods > Create Warehouse Task. | The Create Warehouse Task dialog box (that requests for data) is displayed. |  |
| 5. | Create Warehouse Task | Create the warehouse task and enter the following data:Src Trgt Qty AUoM (Quantity): For example,1Destination Bin: For Example GI-AREA-01The Destination Storage Type is automatically filled in, for example S920 .Warehouse Process Type: S999Choose Create WT. | The warehouse task is created, as you can see in the display log. A Warehouse Task List is automatically printed in the background.You must find the open product warehouse task in the monitor node Warehouse Task. Therefore, note down the warehouse task number. |  |
| 6. | Complete the step | Note down the warehouse task number.Choose Continue to close the log and then choose Home or repeat the steps, if necessary. |  |  |

### Create Posting Change and Warehouse Task for Scrapping (Option 2)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to create an ad-hoc warehouse task from a storage type to the scrap area.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on to SAP Fiori launchpad | Open the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open SAP Fiori Create Posting Changes (/SCWM/MONNAV_CR_PC). | The Create Posting Changes (/SCWM/MONNAV_CR_PC) screen displays. |  |
| 3. | Decide your filter criteria | Storage Type: For example, S001Choose Execute. | The Create Posting Changes screen displays. |  |
| 4. | Choose your Stock | Choose one of the stock lines and More Methods then choose Change Stock Type. | A dialog box requesting data for Change Stock Type is displayed. |  |
| 5. | Enter required data | Stock Type: SQty f. Post. Change (Quantity): for example, 1Warehouse Process Type: S420Destination Storage Bin: SCRAP-AREAThe Destination Storage Type is automatically chosen: For example, S840Choose Create Posting Chg.. | The posting change from F to S and the warehouse order/task are created. The Warehouse Task List is printed automatically in the background. |  |
| 6. | Complete the step | Note down the warehouse task number.Choose Continue to close the log and then choose Home or repeat the steps, if necessary. |  |  |

### Confirm Warehouse Task

#### Variant 1: With Fiori App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A Warehouse Tasks List is printed and handed over to the Warehouse Operative (EWM) who performs the warehouse tasks and confirms them in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Open the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open SAP Fiori Process Warehouse Tasks (F4595) |  |  |
| 3 | Enter your Warehouse Task Number | On the Warehouse Tasks screen, make the following entries:Warehouse Task: <WT number noted down in the previous step>Choose Go. | Warehouse Task is displayed now. |  |
| 4 | Confirm Warehouse Task | Mark the checkbox for the selected warehouse task and choose Confirm. | The following system message appears: <Warehouse task confirmed> |  |

#### Variant 2: With Radio Frequency Devices

Test Case ID <X.XX> for Warehouse Operative (EWM) using Mobile RF Devices in Warehousing. Use it to ensure proper functionality of SAP Fiori app Test RF Environment and to verify the correct set-up of Mobile RF Devices.

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
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Test RF Environment (/SCWM/RFUI)Note Here the app allows you to test working in an RF environment. For working with Mobile RF Devices, see also SAP Note [3048632](https://me.sap.com/notes/3048632). |  |  |
| 3 | Enter Data for RFUI | Whse No: 3350Resource: SHA1-1 or SHR1-1Dflt Dvc.: SE01Choose Enter.Note Use resource SHA1-1 for stock moving from S001 or into S001 , for example queue SO-001 or SI-001.Use SHR1-1 for stock movement which does not involve S001, for example queue SO-F01, SO-B01 and so on. |  |  |
| 4 | Choose Menu | Choose 01 System-Guided > 02 SystemGuided Queue. |  |  |
| 5 | Enter Queue Name | In the Queue field, enter for example SO-001 or SS-001.Choose Enter. |  |  |
| 6 | Create Picking HU | Make the following entries:Pack.Mat: PMPALLETChoose Handling.The picking HU is created. |  |  |
| 7 | Choose Next | Scroll the screen to right with > and choose Next. |  |  |
| 8 | Enteror Verify the Source Information fields | Enter or verify the following fields, if they are required:Src.Bin (Source Bin)SrceHU (Source HU)Prod. (Product)ActQty (Quantity)Choose Enter. |  |  |
| 9 | Verify the Destination information fields | Verify the following fields:DstBin (Destination Bin)Choose Enter. |  |  |
| 10 | Repeat Steps | Repeat step 6 -9 until no suitable warehouse orders are found. |  |  |
| 11 | Logoff RFUI | You can choose Back to the previous screens.Choose Logoff.Choose Save. |  |  |

### Post Ad-Hoc Goods Issue

#### Post Ad-Hoc Goods Issue to Another Storage Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is to post the ad-hoc goods issue to another storage location. This is a succeeding step of the Create Ad Hoc Warehouse Task (Option 1).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Open the Fiori Launch Pad as a Warehouse Clerk (EWM). | The Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Fiori Post Goods Issue - Unplanned (/SCWM/ADGI). | The Post Goods Issue - Unplanned (/SCWM/ADGI) screen displays. |  |
| 3 | Enter the Selection Data | On the Post Unplanned Goods Issue selection screen, make the following entries:Whse No: 3350Select Scrap Stock Only: UnflagGI Process: Storage LocationStorage Location: 331AChoose Execute. | Post Unplanned GI - Warehouse Number 3350 is displayed. |  |
| 4 | Choose Stock and Post Goods Issue | Select one of the stock lines and then choose Post GI. | The goods issue is posted and has generated a Warehouse Material Document. |  |
| 5 | Complete the step | Choose Home or navigate back to repeat the steps if required. |  |  |

#### Post Ad-Hoc Goods Issue for Consumption with Cost Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is to post an ad-hoc goods issue for consumption from a cost center. This is a succeeding step of the Create Ad Hoc Warehouse Task (Option 1).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Open the Fiori Launch Pad as a Warehouse Clerk (EWM). | The Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Fiori Manage Physical Stock - Products (F5340). | The Manage Physical Stock - Products (F5340) screen displays. |  |
| 3 | Enter the Selection Data | Make the following entries:Whse No: 3350Product: <Product>Choose Go. | Selected product stock in warehouse 3350 is displayed. |  |
| 4 | Choose Stock | Select one of the stock lines and then choose Consume. | The Consume screen displays. |  |
| 5 | Enter Data and Post Goods Issue | On the Consume Screen, make the following entries:Account Assignment Category: 10 Cost CenterAccount Assignment Object: For example 33101501.Quantity to Post: <Quantity>Unit of Measure: <UoM>And choose Post. | Goods Issue is posted and has generated a Warehouse Document. |  |
| 6 | Check Warehouse Document | On the Success dialog screen, choose Manage Warehouse Documents to check the posted warehouse document and navigate to each warehouse document item for more details. |  |  |
| 7 | Complete the step | Choose Home or navigate back to repeat the steps if required. |  |  |

#### Post Ad-Hoc Goods Issue for Scrapping

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is to post a goods issue for scrapping. This is the succeeding step of the Create Posting Change Warehouse Task for Scrapping (Option 2).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Open the Fiori Launch Pad as a Warehouse Clerk (EWM). | The Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Fiori Manage Physical Stock - Products (F5340). | The Manage Physical Stock - Products (F5340) screen displays. |  |
| 3 | Enter the Selection Data | Make the following entries:Whse No: 3350Stock Type: S ScrappingChoose Go. | Selected product stock in warehouse 3350 is displayed. |  |
| 4 | Choose Stock | Select one of the stock lines and then choose Scrap. | The Scrap screen displays. |  |
| 5 | Enter Data and Post Goods Issue | On the Scrap Screen, make the following entries:Quantity to Post: <Quantity>Unit of Measure: <UoM>Choose Post. | Goods Issue is posted and has generated a Warehouse Document. |  |
| 6 | Check Warehouse Document | On the Success dialog screen, choose Manage Warehouse Documents to check the posted warehouse document and navigate to each warehouse document item for more details. |  |  |
| 7 | Complete the step | Choose Home or navigate back to repeat the steps if required. |  |  |

### Synchronous Goods Movements for Ad-Hoc Goods Issues

#### Post Synchronous Goods Movements to Another Storage Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is to post Ad-Hoc goods issue to another storage location with synchronous goods movements in Inventory Management and the warehouse. More information can be found in chapter [Purpose](#unique_1) [page ] 1.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as the SAP_BR_WAREHOUSE_CLERK. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Enter Selection Data | Make the following entries and choose Enter.Choose Transfer Posting in field Trans./EventChoose Other in field Reference DocumentEnter movement type 311Choose Continue if there is dialog box for Change to Default Values. |  |  |
| 4 | Enter Material | Choose Transfer Posting tab, and make the following entries:Material: <Material Number>, for example TG11Plant: 3310.Stor.Loc. in From section :335W.Stor.Loc. in Dest section: 331A.Choose Enter. |  |  |
| 5 | Enter Quantity | Choose Quantity tab, and make the following entries:Qty in Unit of Entry: <Quantity>Unit of Entry: <Unit>Choose Enter. |  |  |
| 6 | Enter Storage Bin | On the Warehouse Management tab, make the following entries:Storage Bin :<Storage Bin which contains material stock>.Choose Enter. |  |  |
| 7 | Select Item ok Indicator | Select Item OK checkbox.Choose Check. Confirm the message Document is O.K. by choosing Enter. |  |  |
| 8 | Post | Choose Post. | The system displays the message:Material document xxxxxxxxxx posted.Make a note of the Material Document number. |  |

#### Post Synchronous Goods Movements to Cost Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is to post Ad-Hoc goods issue to cost center with synchronous goods movements in Inventory Management and the warehouse. More information can be found in chapter [Purpose](#unique_1) [page ] 1.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as the SAP_BR_WAREHOUSE_CLERK. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Enter Selection Data | Make the following entries and choose Enter.Choose Goods Issue in field Trans./EventChoose Other in field Reference DocumentEnter movement type 201Choose Continue if there is dialog box for Change to Default Values. |  |  |
| 4 | Enter Material | Choose Material tab, and make the following entries:Material: <Material Number>, for example TG11 |  |  |
| 5 | Enter Quantity | Choose Quantity tab, and make the following entries:Qty in Unit of Entry: <Quantity>Unit of Entry: <Unit>Choose Enter. |  |  |
| 6 | Enter Data | Choose Where tab, and make the following entries:Movement Type: 201Plant: 3310.Storage Location: 335W.Choose Enter. |  |  |
| 7 | Enter Account Assignment Data | Choose Account Assignment tab, and make the following entries:Cost Center: <Cost Center> for example 33101301Choose Enter. |  |  |
| 8 | Enter Storage Bin | On the Warehouse Management tab, make the following entries:Storage Bin :<Storage Bin which contains material stock>.Choose Enter. |  |  |
| 9 | Select Item ok Indicator | Select Item OK checkbox.Choose Check. Confirm the message Document is O.K. by choosing Enter. |  |  |
| 10 | Post | Choose Post. | The system displays the message:Material document xxxxxxxxxx posted.Make a note of the Material Document number. |  |

#### Post Synchronous Goods Movements for Scrapping

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is to post Ad-Hoc goods issue for scrapping with synchronous goods movements in Inventory Management and the warehouse. More information can be found in chapter [Purpose](#unique_1) [page ] 1.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as the SAP_BR_WAREHOUSE_CLERK. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Enter Selection Data | Make the following entries and choose Enter.Choose Goods Issue in field Trans./EventChoose Other in field Reference DocumentEnter movement type 551Choose Continue if there is dialog box for Change to Default Values. |  |  |
| 4 | Enter Material | Choose Material tab, and make the following entries:Material: <Material Number>, for example TG11 |  |  |
| 5 | Enter Quantity | Choose Quantity tab, and make the following entries:Qty in Unit of Entry: <Quantity>Unit of Entry: <Unit>Choose Enter. |  |  |
| 6 | Enter Data | Choose Where tab, and make the following entries:Movement Type: 551Plant: TG11.Storage Location: 335W.Choose Enter. |  |  |
| 7 | Enter Account Assignment Data | Choose Account Assignment tab, and make the following entries:Cost Center: <Cost Center> for example 33101501 .Choose Enter. |  |  |
| 8 | Enter Storage Bin | On the Warehouse Management tab, make the following entries:Storage Bin :<Storage Bin which contains material stock>.Choose Enter. |  |  |
| 9 | Select Item ok Indicator | Select Item OK checkbox.Choose Check. Confirm the message Document is O.K. by choosing Enter. |  |  |
| 10 | Post | Choose Post. | The system displays the message:Material document xxxxxxxxxx posted.Make a note of the Material Document number. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

You may first have completed the following processes and conditions before you start with the test steps:

| Process | Business Condition |
| --- | --- |
| Create New Open MM Posting Period - MDS (BNZ) | You have completed the step described in the Open New MM Period master data script. Posting Period is up to date. |

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
> Flagged while digesting this document, not verified: Internal inconsistency: the scrapping synchronous goods movement (movement type 551) Where-tab step lists 'Plant: TG11', but TG11 is a material in the sample data and the plant is 3310 everywhere else in the script.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-sap-ewm-integration-warehouse-stock-handling-2yl-ae-889]]
- related-to :: [[11-inventory-warehouse-and-transportation/warehouse-physical-inventory-3bx-ae-test-script-sap-s-4hana-cloud-publ]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3BT_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 35,819 chars in the whole document
