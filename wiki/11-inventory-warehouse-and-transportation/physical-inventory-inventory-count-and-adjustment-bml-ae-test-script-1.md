---
id: 11-inventory-warehouse-and-transportation/physical-inventory-inventory-count-and-adjustment-bml-ae-test-script-1
title: Physical Inventory – Inventory Count and Adjustment (BML_AE) Test Script (BML_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script (UAE, plant 3310) for physical inventory: create documents, print, count, recount, post differences, notifications, analysis."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/physical-inventory]
aliases: [BML_S4CLD2608_BPD_EN_AE]
keywords: [Physical Inventory Count and Adjustment, physical inventory, inventory count, physical inventory documents, inventory count differences, test scripts, recount, situation handling, inventory notifications, physical inventory analysis]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BML_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1290
topic: 11-inventory-warehouse-and-transportation/physical-inventory
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Physical Inventory – Inventory Count and Adjustment (BML_AE) Test Script (BML_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BML_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Physical Inventory Count and Adjustment** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Physical Inventory – Inventory Count and Adjustment (BML_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232862361)

[2 Prerequisites 4](#_Toc232862362)

[2.1 System Access 4](#_Toc232862363)

[2.2 Roles 4](#_Toc232862364)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232862365)

[2.4 Business Conditions 6](#_Toc232862366)

[2.5 Preliminary Steps 6](#_Toc232862367)

[2.5.1 Open New MM Period 6](#_Toc232862368)

[2.5.2 Initialize Material Stock 6](#_Toc232862369)

[2.5.3 Check Open Physical Inventory Document 7](#_Toc232862370)

[2.5.4 Prerequisite for Situation Handling in Physical Inventory (Optional) 9](#_Toc232862371)

[2.5.4.1 Manage Teams and Responsibilities 9](#_Toc232862372)

[2.5.4.2 Manage Situation Types 10](#_Toc232862373)

[3 Overview Table 13](#_Toc232862374)

[4 Test Procedures 15](#_Toc232862375)

[4.1 Create Physical Inventory Documents 15](#_Toc232862376)

[4.1.1 Option A: Create Physical Inventory Documents (Mass Creation) 15](#_Toc232862377)

[4.1.2 Option B: Create Physical Inventory Document (Single Creation) 17](#_Toc232862378)

[4.2 Print Physical Inventory Documents 18](#_Toc232862379)

[4.3 Physical Count 20](#_Toc232862380)

[4.4 Enter Inventory Count 20](#_Toc232862381)

[4.5 Manually Trigger Notification for Physical Inventory (Optional) 22](#_Toc232862382)

[4.6 Check Notification of Physical Inventory (Optional) 23](#_Toc232862383)

[4.7 Dismiss Notification of Physical Inventory (Optional) 24](#_Toc232862384)

[4.8 List Count Differences 25](#_Toc232862385)

[4.9 Recount (Optional) 26](#_Toc232862386)

[4.10 Post Inventory Count Differences 27](#_Toc232862387)

[4.11 Display Physical Inventory Document Object Page (Optional) 29](#_Toc232862388)

[4.12 Physical Inventory Analysis (Optional) 30](#_Toc232862389)

## Purpose

Overview

The process begins with the generation of the required inventory count sheets. Materials can be blocked here for posting during the physical inventory. Once the inventory sheets are printed out, the actual physical inventory count is realized for the given materials. The count result is entered in the system and discrepancies in the system quantities are reviewed. The inventory may be recounted until final counts are accepted and inventory differences are posted.

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
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the provided sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 | Shop floor w/o lean WM |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |
| Storage Location | 331R | Storage Location Returns |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing group | 001/002 | Group 001/Group 002 | depending on material |
| Supplier | 33300001 | Domestic UAE Supplier 1 |  |
| Material | TG20 | Trading Good for Reg. Trading (reorder point planning) | See sections Business Conditions and Preliminary Steps. |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning) | See sections Business Conditions and Preliminary Steps. |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad. | See sections Business Conditions and Preliminary Steps. |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met:

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You’ve completed the step described in the master data script. Posting Period is up-to-date.The material TG20, TG11, and TG12 are available in stock in considerable quantity.Recommended Quantity: 100 |
| 31N - Situation Handling | Install this scope item for the situation handling steps. |

### Preliminary Steps

#### Open New MM Period

External Process

For this activity, run the following step from the Create New Open MM Posting Period - MDS (BNZ) to close MM period and open new posting period:

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
| 5 | Add Initial Stock | Make the following entries and choose Post:Special Stock Type: Keep default as Standard StockStock Change: Initial EntryQuantity: Enter a number, for example, 100Serial Numbers: Select search help icon and on the dialog Assign Serial Numbers, select Auto-Create and choose the button Apply.Document Date: <Today>Posting Date: <Today> | The system displays a message Material document XXXXXXXXXX/XXXX created. The stock has been added. |  |
| 6 | Repeat Steps (Optional) | You can refer to the steps above if you want to initialize stock for TG11 (the material without serial number). |  |  |

#### Check Open Physical Inventory Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note Because the system can only have one open Physical Inventory document for the same material, it is necessary to check open physical inventory document before any testing procedures. |

Purpose

This process step shows you how to check the open physical inventory document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. |  |  |
| 2 | Access the App | Open Manage Physical Inventory Documents (F0379A). | The Manage Physical Inventory Documents screen displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:Plant: 3310Adjustment Status: Select items Not Posted and Partially Posted; |  |  |
| 4 | Choose an Item | Choose one of the filtered items in Physical Inventory Documents list.If system hasn't any open Physical Document, please skip step 4 and 5. | The Physical Inventory Documents screen displays. |  |
| 5 | Review Header Data | If Count Status is Not Counted, process the following steps:Enter Inventory CountPost Inventory Count DifferencesIf Adjustment Status is blank, process the following step:Post Inventory Count DifferencesNote For the detailed instructions of how to "Enter Inventory Count" and "Post Inventory Count Difference", please go to test procedures chapter and the corresponding steps in the following documents. |  |  |

#### Prerequisite for Situation Handling in Physical Inventory (Optional)

##### Manage Teams and Responsibilities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to link the list of users who are supposed to receive Physical Inventory notifications.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Teams and Responsibilities (F2412). | The Manage Teams and Responsibilities screen displays. |  |
| 3 | Check Existing Teams | On the Manage Teams and Responsibilities screen, make the following entry and choose Go:Type: SPHYSINVMOIn the Teams area, choose again the row of the filtered team, check if Warehouse Clerk and Inventory Manager are maintained in the Team Members section.If so, then the team is created already. Please skip following steps. If not maintained, then continue the following steps. | Either a list of teams is displayed or no teams can be found. |  |
| 4 | Create Team | Choose Create and make the following entries:Name: PHYSICAL INVENTORY MONITORINGStatus: EnabledType: SPHYSINVMOScroll down to the Team Owner section and choose Create.In the Business Partner field, enter the selection dialog box. In the Select: Team Owner dialog box, enter Inventory Manager in the search bar and press Enter. Select the line item with Inventory Manager in the Last Name column.Then go to the Team Members section and choose Create.In the Select: Business User dialog box, enter the business role, e.g., Inventory Manager, in the search bar and press Enter. Select the line item with Inventory Manager in the Last Name column. Choose OK.Note If you can't find the business role, enter the user ID assigned with the business role, e.g., Inventory Manager.In this line of item, go to field Functions, choose search help.In the Select: Functions dialog box, in the Items table, select the line item with SMMIM_IM in the Function column and choose OK. | User Inventory Manager is assigned to Physical Inventory Monitoring. |  |
| 5 | Save Team | Choose Save. | The team has been created. |  |

##### Manage Situation Types

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to set up the situation types by using the template.

|  |
| --- |
| Note Please make sure 31N - Situation Handling is activated if you want to execute this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Situation Types (F2947). | The Manage Situation Type screen displays. |  |
| 3 | Check Existing Situation Type | Choose the Situation Types tab, and make the following entries and choose Go:Name (In search box): MAN_PHYSICAL_INVENTORY_MONITORChoose the row of the filtered Situation Types and check whether existing types can be reused for Physical Inventory.If so, skip step 4 and only modify Start Batch Job At in step 5; if not, continue the following steps to create a new one. | Either a list of situation type is displayed or no situation types can be found. |  |
| 4 | Copy Standard Situation Template | On the Manage Situation Types screen, there are two tabs: Situation Templates and Situation Types.Choose the Situation Templates tab and choose Go to search the Standard Situation Templates: MAN_PHYSICAL_INVENTORY_MONITORCheck the box before standard situation template: MAN_PHYSICAL_INVENTORY_MONITOR and choose Copy | The situation type is copied. |  |
| 5 | Create Custom Situation Template | On the Situation Type screen, make the following entries:ID: ZMAN_PHYSICAL_INVENTORY_MONITORName: Physical Inventory MonitoringDisplay Sequence: HighIn the Conditions section, check added filters: For example:In the Is Counted field, select Yes from the dropdown.In the Is Recounted field, select No from the dropdown.In the Is Difference Posted field, select No from the dropdown.Note Filters can be adjusted for different use case scenarios. In this case, filters are set to only select the open Physical Inventory documents.Go to the Recipients section, remove all Responsibility Definitions and make the following choices:Filter by Member Function: Inventory ManagerGo to the Situation Monitoring section, check Monitor Instances.Go to the Batch Job Scheduling section, make the following entries:Time Zone: UTCStart Batch Job At: <UTC 8:00> If you want to let your team members receive the notification at UTC 8:00.Choose Create.Note In-App Situation Message can be customized by editing the Short Description and Message Details fields. | The situation type is created. |  |
| 6 | Enable Situation Template | In the Enable Situation Type dialog box, choose Yes. | The situation is enabled. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App / Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Physical Inventory Documents](#unique_13) [page ] 15 |  |  |  |
| [Option A: Create Physical Inventory Documents (Mass Creation)](#unique_14) [page ] 15 | Warehouse Clerk | Create Physical Inventory Documents (F3197) | The system generates physical inventory documents. |
| [Option B: Create Physical Inventory Document (Single Creation)](#unique_15) [page ] 17 | Warehouse Clerk | Create Physical Inventory Documents (F3197) | The Create Physical Inventory Documents screen displays. |
| [Print Physical Inventory Documents](#unique_16) [page ] 18 | Inventory Manager | Manage Physical Inventory Documents (F0379A) | The system generates a physical inventory count sheet, documents are printed. |
| [Physical Count](#unique_17) [page ] 20 | Warehouse Clerk |  | Count is completed. |
| [Enter Inventory Count](#unique_18) [page ] 20 | Warehouse Clerk | Manage Physical Inventory Count (F5430) | Counts are entered. |
| [Manually Trigger Notification for Physical Inventory (Optional)](#unique_19) [page ] 22 | Business Process Specialist | Manage Situation Types (F2947) |  |
| [Check Notification of Physical Inventory (Optional)](#unique_20) [page ] 23 | Inventory Manager | Notifications |  |
| [Dismiss Notification of Physical Inventory (Optional)](#unique_21) [page ] 24 | Inventory Manager | Notifications |  |
| [List Count Differences](#unique_22) [page ] 25 | Inventory Manager | Manage Physical Inventory Documents (F0379A) | The system generates a report about the count differences. |
| [Recount (Optional)](#unique_23) [page ] 26 | Inventory Manager | Manage Physical Inventory Item List - New Version (F8634) | New physical inventory document is created. |
| [Post Inventory Count Differences](#unique_24) [page ] 27 | Inventory Manager | Manage Physical Inventory Documents (F0379A) | Differences are posted. |
| [Display Physical Inventory Document Object Page (Optional)](#unique_25) [page ] 29 | Inventory Manager | Manage Physical Inventory Documents (F0379A) | The physical inventory document is displayed. |
| [Physical Inventory Analysis (Optional)](#unique_26) [page ] 30 | Inventory Manager | Physical Inventory Analysis (W0058) | The Physical Inventory Analysis screen displays. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Physical Inventory Documents

Purpose

You perform this activity to create the documents for the physical inventory. You have two options to create the physical inventory documents:

- Option A: Create Physical Inventory Documents (Mass Creation).
- Option B: Create Physical Inventory Document (Single Creation).

You can choose either option A or option B to execute the physical inventory document creation. For more information, see the next two tasks.

|  |
| --- |
| Note For one material, choose option A or B (not both), because system can only have one open Physical Inventory document for the same material. In option B, the test script specifically covers the creation of Physical Inventory Documents for serial number-managed material. |

#### Option A: Create Physical Inventory Documents (Mass Creation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use the app Create Physical Inventory Document to create physical inventory documents for selected materials or groups of materials.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Physical Inventory Documents (F3197). | The Create Physical Inventory Documents screen displays. |  |
| 3 | Search Materials | In the upper area, enter the following data and choose Go:Posted to Stock: YesPlant: 3310Storage Location: 331ANote The display sorting sequence can be adjusted by choosing Settings in the upper right corner of material list section. | The stock overview displays. |  |
| 4 | Adapt Filters | In the upper-right area, choose Adapt Filters. In the search box, search for Material Type, and then select the item and choose OK.The Material Type filter is now available in the filter bar. From the dropdown list of Material Type, select Trading Goods, and then choose Go. | The filters are set. |  |
| 5 | Create Physical Inventory Document: Select Materials | On the Unrestricted-Use Stock tab, select all the trading goods for which you want to create physical inventory documents and choose Create Physical Inventory Documents.For example, select Material TG11 and TG12.Note If you want to schedule a job to create physical inventory documents, choose the next button Schedule Physical Inventory Document Creation. Physical inventory document will be created for the goods filtered via the filter bar (filters such as Plant, Storage Location, Material Type). The text tab ((Un-)Restricted-Use Stock, for example) displays the number of items in brackets which will be considered for the background job.Please be noted that a maximum of 999 items can be contained in one physical inventory document. | The Create Physical Inventory Documents dialog box displays. |  |
| 6 | Create Physical Inventory Document | In the Create Physical Inventory Documents dialog box, enter the following data:Split Documents by: NoneNote If choosing not to split document, you can further define sorting option, for example as sort by Storage Bin – Material.You can also select, for example, Split Documents by: Material if you want to create separate document for each material.Maximum Number of Items: <Default>Planned Count Date: <Today>Document Date:<Today>Expand the Additional Header Data, enter the following data:Physical Inventory Reference:<Enter any value to be used to link the documents created by this transaction>Set Posting Block：<Select>Freeze Book Inventory: <Deselect>Choose Create. | The system displays a success message:1 document with 2 items has been created. Physical Inventory Document 1000000XX Make a note of the created document number: __________. |  |

#### Option B: Create Physical Inventory Document (Single Creation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create physical inventory document for a single material manually (single creation).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Physical Inventory Documents (F3197). | The Create Physical Inventory Documents screen displays. |  |
| 3 | Adapt Filters | In the upper-right area, choose Adapt Filters. In the search box, search for Material, then select the item and choose OK. | The Material filter is now available on the filter bar. |  |
| 4 | Search Material | In the Material filter, enter the following material and choose Go:Material: TG20 | The stock overview for selected material displays. |  |
| 5 | Create Physical Inventory Document: Select Materials | On the Unrestricted-Used Stock tab, select the line of material TG20 and choose Create Physical Inventory Documents. | The Create Physical Inventory Documents dialog box displays. |  |
| 6 | Create Physical Inventory Document | In the Create Physical Inventory Documents dialog box, enter the following data:Split Documents by: NoneMaximum Number of Items: <Default>Planned Count Date: <Today>Document Date: <Today>Expand the Additional Header Data, enter the following data:Physical Inventory Reference:<Enter any value to be used to link the documents created by this transaction>Set Posting Block: <Select>Freeze Book Inventory: <Deselect>Then choose Create. | A document is created. Make a note of the created document number: __________ |  |

### Print Physical Inventory Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to print the documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Physical Inventory Documents (F0379A). | The Print Physical Inventory Document screen displays. |  |
| 3 | Set Filters | Make the following entries in filters and choose Go:Plant: 3310Storage Location: 331A | Physical inventory documents display. |  |
| 4 | Background Print | Click on the Background Print button. | The Background Print popup displays. |  |
| 5 | Trigger Print | In the Items with Status part, check only Not Yet Counted and uncheck all the other options.Click the Background Print button. | A message shows "Print job successfully scheduled.". |  |
| 6 | View Application Job (Optional) | In the message dialog, click the Application Job link. | The Manage Physical Inventory Documents: Mass Printing screen displays. |  |
| 7 | Check Physical Inventory Documents | Go back to the App Manage Physical Inventory Documents (F0379A), and navigate to specific physical inventory document which has count progress as zero:For example, in the filter Physical Inventory Document, enter the document number you created in previous step, and choose Go.Click the line of the physical inventory document. | The physical inventory document page of the specific document displays. |  |
| 8 | Check Print Status | On the upper right corner of the Items table, click the Settings button.In View Settings dialog, search for Printed, then check this option and click OK.A new column Printed is added to the table. Check if its value is Yes. | The print status is yes. |  |
| 9 | Check Output | Go to the Output Management section, click the line of the print job just generated.Note As detailed information is not fully displayed, from the upper right corner of Output Management, click the view button Show More per Row. | Detailed information of the specific job is displayed in the Output Management section. |  |
| 10 | View Print Output | Click the Display button to view the PDF output. | The PDF document of the print job displays in a new browser window. |  |
| 11 | Select Printer | Review the PDF document and choose Print. | The Print dialog box displays. |  |
| 12 | Print | Select an available printer and choose Print. | The document is printed. |  |

### Physical Count

Purpose

This process step is about executing physical count offline in your own plants (manual activity).

Procedure

This is a manual activity. It isn’t an SAP system activity.

### Enter Inventory Count

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to transfer results of the counting into the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Physical Inventory Count (F5430). | The Manage Physical Inventory Count screen displays. |  |
| 3 | Search Physical Inventory Documents | In the upper area, enter the following data and choose Go:Physical Inventory Document: <document number>Fiscal Year: <current year> | The Physical Inventory Documents display in the Documents area. |  |
| 4 | Select Data | In the lower area, choose the line of physical inventory document created in the previous step. | The Manage Physical Inventory Count screen displays. |  |
| 5 | Result of Counting | Choose Edit and enter the result of count quantity in the column Counted Quantity in Entry Unit.Note Enter a suitable count number. You can manage inventory differences by setting maximum thresholds for each physical inventory document and its items. Value thresholds per company code can be defined via the SSCUI Manage Tolerances for Physical Inventory Differences (ID: 106788). Additionally in this SSCUI, you may assign individual users to a tolerance group.Please be noted that this SSCUI applies current setting. Settings are not transportable between quality system and production system and the settings need to be maintained separately. For more information, CBC user can refer to [Settings via SAP Central Business Configuration (3-System Landscape)](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html).Note Besides directly entering value in the App, there’s another option to enter inventory count via Excel. After choosing the Edit button, click the Items Download/Upload button in the upper right corner of the screen to first download a template, enter counts offline, and then upload the edited Excel.Then choose Save. | The counts have been saved. |  |
| 6 | Optional: Result of Counting (with Serial Number Managed Material) | If you want to count material managed by serial number, for example, TG20, there are two options:Option 1: Enter inventory count in AppClick the line of material and enter the Physical Inventory Document Item screen. By default displays the General Information tab. Go to the Serial Numbers tab, choose checkbox if you count the specified serial number material, then choose Apply in the lower right corner.Then choose Save.Option 2: Enter inventory count via Excel Download/UploadIn the physical inventory document page, Choose Edit. The Items Download/Upload button is now visible in the upper right corner of the screen.Click the button, in the popup dialog, choose Download Excel Template. In the downloaded template, enter correct count number in the column Counted Quantity in Unit of Entry. Then go to the next sheet, Serial Numbers, and enter Item No. and new serial numbers.Save the Excel, go back to the App, click again the Items Download/Upload button. Then upload the Excel. The count value and serial number will be auto-updated in the App.Note Process this step only if you choose option B to create physical inventory document which uses serial number managed material. | The counts have been saved. |  |

### Manually Trigger Notification for Physical Inventory (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step shows how to manually trigger physical inventory notification to assigned members.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Situation Types (F2947). | The Manage Situation Types screen displays. |  |
| 3 | Find the Situation Type Created Previously | Choose the Situation Types tab, and make the following entries and choose Go:Name (In search box): ZMAN_PHYSICAL_INVENTORY_MONITOR | The situation type is display. |  |
| 4 | Trigger the Notification Manually | Click to enter the situation type, then choose Trigger Now. | An information dialogue box displays. |  |
| 5 | Confirm the Backgroud Job for Creating Situation Instances | Choose OK. | Background job is confirmed. |  |

### Check Notification of Physical Inventory (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step shows how to check notifications for physical inventory sent to the selected responsible team members. Notifications can either be triggered manually (see [Manually Trigger Notification for Physical Inventory (Optional)](#unique_19) [page ] 22), or automatically by the system on a regular basis based on the Batch Job Scheduling parameters maintained in preliminary step [Manage Situation Types](#unique_11) [page ] 10.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Check Notifications | On the home screen, choose the Notifications icon in the upper right corner. | The following notification displays:Physical Inventory document XXXXXXXXXX/00XX needs attention. |  |
| 3 | Navigate to Physical Inventory Document Overview App | Choose the detailed notification line Physical Inventory document XXXXXXXXXX/00XX needs attention. | The Physical Inventory Document displays. |  |
| 4 | Check information on Physical Inventory Document | Choose the line of Physical Inventory Document with alert. | Situation is displayed as Physical Inventory document item needs attention. |  |

### Dismiss Notification of Physical Inventory (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step shows how to dismiss notification of physical inventory sent to the selected responsible team members.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Check Notifications | On the home screen, choose the Notifications icon in the upper right corner. | The following notification displays:Physical Inventory document XXXXXXXXXX/00XX needs attention. |  |
| 3 | Navigate to Physical Inventory Document Overview App | Choose the detailed notification line Physical Inventory document XXXXXXXXXX/00XX needs attention. | The Physical Inventory Document displays. |  |
| 4 | Check information on Physical Inventory Document | Choose the line of Physical Inventory Document with alert. | Situation is displayed as Physical Inv Doc Item needs attention. |  |
| 5 | Dismiss Situation | Choose Close Situation.Note Under the Situation tab, check if there is more than one situation. If so, only select and dismiss the relevant situation. | A Close Situation dialog box displays. |  |
| 6 | Select Reason for Dismiss | Select Resolved and choose Confirm. | Situation is closed. |  |

### List Count Differences

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is only necessary if differences are encountered.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Physical Inventory Documents (F0379A). | The Manage Physical Inventory Documents screen displays. |  |
| 3 | Adapt Filters | In the upper right area, choose Adapt Filters. Check the field Adjust Status, and choose OK. | The filters are set. |  |
| 4 | Search Physical Inventory Documents | Make the following entries in filters and choose Go.Plant： 3310Count Status： Fully CountedAdjustment Status： Not PostedClick the line of the physical inventory document. | The physical inventory document page of the specific document displays.On this screen, in the Items tab, details of the physical inventory documents are displayed. |  |
| 5 | Show More per Row | On the upper right corner of the table of the Items tab, click the view button Show More per Row. | All detailed information displays. |  |
| 6 | Display More Columns Relevant to Difference | Then click the Settings button, the View Settings dialog popup.Check more fields to display in the column, for example:Difference ValueDifference Value based on Count EntryClick OK. | The table displays existing differences of book and count quantity that can be printed, if necessary.Option A: If the count isn’t accepted, go to the task [Recount (Optional)](#unique_23) [page ] 26.Option B: If the count is accepted, go to the task [Post Inventory Count Differences](#unique_24) [page ] 27. |  |

### Recount (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is only necessary if the warehouse manager or controller decides to recount a material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Physical Inventory Item List - New Version (F8634). | The Manage Physical Inventory Item List screen displays. |  |
| 3 | Search Physical Inventory Documents | In the upper area, enter the following data and choose Go:Physical Inventory Document: <document number>Fiscal Year: <current year> | The Physical Inventory Documents are displayed in the documents area. |  |
| 4 | Check Details in Physical Inventory Document | In the lower Physical Inventory Documents area, review the number of Difference Quantity or Difference Value Count Entry of the physical inventory items that were counted in the previous step.Note In the upper-left corner of the document item list, you can find a dropdown list containing different inventory status. You may use it as a quick filter. For example, by selecting Inventory Status: Only Counted, you can filter all the line items of the physical document that are counted but not yet posted with differences. |  |  |
| 5 | Create a New Recount Document | From the item list, select the items that cannot be accepted and choose Recount.In the Recount dialog box, make the following entries:Planned Count Date: <Today>Document Date: <Today>Then choose Create. | A new recount document is successfully created.View Document (100000xxx) |  |
| 6 | Recount Inventory | To recount the inventory, repeat the same inventory count procedure starting from the chapter Print Physical Inventory Documents. |  |  |

### Post Inventory Count Differences

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the results of the physical inventory. Once the count is reviewed by the warehouse manager, the warehouse monitoring can post the inventory count differences.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Physical Inventory Documents (F0379A). | The Manage Physical Inventory Documents screen displays. |  |
| 3 | Adapt Filters | In the upper-right area, choose Adapt Filters. Select the field Adjustment Status, and choose OK. | The filters are set. |  |
| 4 | Search Physical Inventory Documents | Make the following entries in filters and choose Go.Plant： 3310Count Status： Fully CountedAdjustment Status： Not PostedChoose the row of the physical inventory document. | The physical inventory document page of the specific document displays.On the Items tab, details of the physical inventory document item are displayed. |  |
| 5 | Select Items to Post | Select the line items with materials and choose Post. | The Post screen displays. |  |
| 6 | Post | Validate the posting date and choose Post.NoteAlternatively, if you want to post differences at item level, follow step 7 and 8.If the quantity posted is different from the actual quantity, and you want to ensure no significant difference will be posted, you can leverage the SSCUI Manage Tolerances for Physical Inventory Differences (ID: 106788). | The system displays the message Successfully Posted.The adjustment status of line item has changed to Fully Posted.Material Document XXXXXXXXXX is generated and displayed in the line item. |  |
| 7 | Access the App (Optional) | Open Manage Physical Inventory Item List - New Version (F8634). | The Manage Physical Inventory Item List screen displays. |  |
| 8 | Post Differences at Item Level (Optional) | Make the following entries in filters and choose Go:Plant： 3310In the lower-left area, select Inventory Status: Only Counted from the dropdown list.Select the row of the physical inventory document and choose Post.Validate the difference information and choose Post. | The system displays the message Successfully Posted. |  |

### Display Physical Inventory Document Object Page (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the physical inventory documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Inventory Manager role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Physical Inventory Documents (F0379A) | The Physical Inventory Document screen displays. |  |
| 3 | Search for Physical Inventory Document | Make the following settings and choose Go.Physical Inventory Document: Physical Inventory DocumentPlant: 3310 | The requested search result displays. |  |
| 4 | Select Physical Inventory Document | Select the row of the Physical Inventory Document you want to overview. | The Physical Inventory Document screen display. |  |
| 5 | Check Physical Inventory Document Details | Check the General Information, Process Data and Items details. | The correct detail information shows. |  |
| 6 | Back to Launch Pad | Select Home to go back to the Fiori launchpad. | The Fiori launchpad displays. |  |

### Physical Inventory Analysis (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to analyze physical inventory in your company to identify opportunities for process improvement.

Prerequisite

Before you proceed to test this function, please follow the above detailed steps in Physical Inventory – Inventory Count and Adjustment (BML), in order to have several physical inventory documents available for analyze.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Physical Inventory Analysis (W0058). | The Physical Inventory Analysis screen displays. |  |
| 3 | Set Search Parameter | Apply the following filter and choose Go.Fiscal Year: <Current Year>Note Choose fiscal year according to the physical inventory documents created in the previous steps. | Data Analysis tab displays values of the physical inventory documents. |  |
| 4 | Select Measures | In the left Navigation Panel, go to the Dimensions section, then choose arrow beside Measures to expand the options.Click the + button beside the field you want to add to display, for example: Counted Quantity.Note To avoid updating the analysis results lively, in the Navigation Panel, choose the Settings arrow besides Dimensions and select Defer Layout Update from the dropdown list. This is useful when processing large amount of data. | The Column Counted Quantity is added to the right-side data analysis result. |  |
| 5 | Remove Measures | Click the - button beside the field that already selected as measures and need to be removed, for example, Book Value. | The Book Value column is removed from the right-side data analysis result. |  |
| 6 | Add Rows | In the left Navigation Panel, drag the dimension field that needs to be added and drop it in Rows section, or click the button <!-- image omitted: unnamed -->(Add Field to Row Axis) beside the dimension field.For example, drag Storage location and drop it below the Plant field in the Rows section. | The Storage Location row is added to the right-side data analysis result. |  |
| 7 | Switch the Sequence of Dimension in Row | In the Rows section, drag and drop dimension field to adjust the sequence.For example, drag and drop Storage Location above Plant. | The sequence of row dimension is adjusted. |  |
| 8 | Remove Rows | Drag the dimension field, for example, Storage Location, in the Rows section and drop it back to the dimension section, or click the button <!-- image omitted: unnamed -->(Remove Field from Row Axis) beside the dimension field. | The Storage Location row is removed from the right-side data analysis display. |  |
| 9 | Change Layout to Bar Chart | On the right side, choose the tab Graphical Display beside Data Analysis. | The layout of analysis result is changed to bar chart. |  |
| 10 | Personalize Chart Settings | Choose the Settings button on the upper-right corner of the Graphical Display screen. | You can change the chart type to, for example a line chart or stacked bar chart and determine whether to show Legend or Tooltip or not. |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/physical-inventory-cycle-counting-4lu-ae-test-script-sap-s-4hana-cloud]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BML_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 53,175 chars in the whole document
