---
id: 11-inventory-warehouse-and-transportation/test-script-sap-ewm-integration-warehouse-stock-handling-2yl-ae-889
title: "Test Script: SAP EWM Integration – Warehouse Stock Handling (2YL_AE) (2YL_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 2YL_AE: EWM integration with S/4HANA Cloud Public Edition covering initial stock upload, physical inventory and scrapping."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-physical-inventory-and-stock-handling]
aliases: [2YL_S4CLD2608_BPD_EN_AE]
keywords: ["EWM Physical Inventory, Scrapping and Ad Hoc Goods Issue", ewm integration, test scripts, initial stock upload, physical inventory, stock scrapping, difference analyzer, tolerance groups, material documents, warehouse tasks]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2YL_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-889
topic: 11-inventory-warehouse-and-transportation/ewm-physical-inventory-and-stock-handling
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: SAP EWM Integration – Warehouse Stock Handling (2YL_AE) (2YL_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2YL_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **EWM Physical Inventory, Scrapping and Ad Hoc Goods Issue** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | SAP EWM Integration – Warehouse Stock Handling (2YL_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232851140)

[2 Prerequisites 4](#_Toc232851141)

[2.1 Additional Manual Configuration 4](#_Toc232851142)

[2.2 System Access 4](#_Toc232851143)

[2.3 Roles 4](#_Toc232851144)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232851145)

[2.5 Business Conditions 6](#_Toc232851146)

[2.6 Preliminary Steps 6](#_Toc232851147)

[2.6.1 Initial Stock Upload 6](#_Toc232851148)

[2.6.1.1 Data Files for Initial Stock Upload 6](#_Toc232851149)

[2.6.1.2 Stock Overview After Initial Stock Upload 7](#_Toc232851150)

[2.6.2 Physical Inventory 7](#_Toc232851151)

[2.6.2.1 Assign User to Tolerance Group for Recount/Clearing 7](#_Toc232851152)

[2.6.2.2 Assign User to Tolerance Group for Difference Analyzer 9](#_Toc232851153)

[2.6.2.3 Creating User Settings for the Difference Analyzer Transaction 10](#_Toc232851154)

[2.6.2.4 Check Warehouse Time Zone 10](#_Toc232851155)

[2.6.2.5 Determine and Set Prices from SAP S/4HANA System 11](#_Toc232851156)

[3 Overview Table 13](#_Toc232851157)

[4 Test Procedures 15](#_Toc232851158)

[4.1 Initial Stock Upload 15](#_Toc232851159)

[4.1.1 Upload Initial Stock in SAP EWM System 15](#_Toc232851160)

[4.1.2 Check Material Documents (Optional) 16](#_Toc232851161)

[4.2 Physical Inventory 17](#_Toc232851162)

[4.2.1 Create Physical Inventory Documents in SAP EWM System 18](#_Toc232851163)

[4.2.2 Enter Count Results in SAP EWM System 19](#_Toc232851164)

[4.2.3 Analyze Physical Inventory Differences and Post Them to SAP S/4HANA Cloud Public Edition From the SAP EWM System 20](#_Toc232851165)

[4.2.4 Check Material Documents (Optional) 21](#_Toc232851166)

[4.3 Scrapping 22](#_Toc232851167)

[4.3.1 Select Stock to Be Scrapped in SAP EWM 23](#_Toc232851168)

[4.3.2 Create Ad-Hoc Warehouse Tasks for Scrapping Damaged Stock in SAP EWM 23](#_Toc232851169)

[4.3.3 Confirm Warehouse Order in SAP EWM 25](#_Toc232851170)

[4.3.4 Empty Scrapping Zone and Post Goods Issue in SAP EWM 25](#_Toc232851171)

[4.3.5 Check Material Documents (Optional) 26](#_Toc232851172)

[5 Appendix 28](#_Toc232851173)

[5.1 Process Integration 28](#_Toc232851174)

[5.1.1 Preceding Processes 28](#_Toc232851175)

## Purpose

Overview

This scope item covers core warehouse management processes, including scrapping, physical inventory, initial stock upload and their integration into SAP S/4HANA Cloud Public Edition. The system communicates goods movements such as physical inventory differences, initial stock upload, and ad-hoc posting changes to SAP S/4HANA Cloud Public Edition by means of goods movement messages.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/49ff2a33cc650149fcf487d9bbef91d3)

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

The organizational structure and master data of your company have created in your system during the activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, it depends on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 333D | Standard storage 1 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing group | 001/001 | Group 001 |  |
| Material | TG11 | Trading Good for Regular Procurement (PD planning) |  |
| Packaging Material | PMPALISU | EWM Pallet Stock Initial Upload (no SSCC#) | Internal Number Range Used |
| Storage Type | Y001 | General Storage |  |
| Storage Type | Y002 | Picking Area of the General Storage |  |
| Warehouse | 333 | Decentral EWM-managed Warehouse in SAP S/4HANA |  |
| EWM Warehouse | 3330 | Decentral EWM Warehouse |  |
| Ent. To Dispose | 33413310 |  |  |
| Ship to party | 33100003 | Domestic UAE Customer 3 |  |
| Sold to party | 33100003 | Domestic UAE Customer 3 |  |
| Division | 00 |  |  |
| Distribution Channel | 00 |  |  |
| Supply Chain Unit | YWAREHOUSE-3330 |  |  |

### Business Conditions

The business process described in this test script is part of a larger chain of integrated business processes or scope items. As a result, you must have completed the following processes and fulfilled the following business conditions before you can start any activities in this scope item:

| Scope Item ID | Business Condition |
| --- | --- |
| 2VJ - SAP EWM Integration – Inbound Processing from Supplier | To ensure that there is enough stock for use in the outbound process, you can bring stock into the warehouse using inbound processing. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the master data script. Posting Period is up to date. |

### Preliminary Steps

#### Initial Stock Upload

##### Data Files for Initial Stock Upload

The different .csv data files referred to in the following sections of this process are available in the SAP EWM Integration - Batch Management Set-Up Instruction Guide in the Appendix chapter.

Attached to the Set-Up Instruction Guide are the following .zip files:

- Initial_Stock_Upload_Data_DE.zip

The .zip file contains all necessary data to populate stock for the example products.

To provide stocks into the General Storage, you apply the following .csv file:

- isu_TG11.csv

|  |
| --- |
| Note The data files use bins (separated by Fast Movers/Slow Movers section) that are at the very end of the standard bin sorting. |

The provided handling unit (HU) IDs for pallets are external numbers (for example, ISU33-HU01) indicating that these HUs do come from an initial stock upload.

The HUs created by the initial stock upload (for example, ISU33-HU01) use a specific packaging material, PMPALISU. It does not use SSCC numbering 11, but allows for external alphanumeric IDs (in our example: ISU33-HU01).

##### Stock Overview After Initial Stock Upload

Purpose

The following paragraphs describe how you can fill the warehouse’s General Storage with stock using the example products. You can start outbound processing or do replenishment without an explicit need to go through the corresponding inbound processing. When you apply the example data provided in the isu_SN01.csv to an empty storage, you can end up with the following stock situation for a TG11 product:

| Storage Type | HU# | Storage Bin | Qty(BUoM) | Qty(AUoM) | Csv file | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| SN01 |  | 001.01.01.01 | 48 PC | 1 PAL | isu_SN01 | Bin full |
| SN01 |  | 001.01.01.02 | 48 PC | 1 PAL | isu_SN01 | Bin full |
| SN01 |  | 001.01.01.03 | 48 PC | 1 PAL | isu_SN01 | Bin full |

#### Physical Inventory

##### Assign User to Tolerance Group for Recount/Clearing

Purpose

In this transaction, you assign individual logon users to tolerance groups, that are previously defined in the system configuration.

Generally, the assignment of users to tolerance groups determines whether a logon user can post differences or enter values within the tolerance boundaries the assigned tolerance group grants to the user.

The assignment is also subdivided by activity area. The examples assume physical inventory activities in the area of the main storage type Y001, respectively, in the activity area with the same ID as the corresponding storage type.

|  |
| --- |
| Note Without having such assignment of your user, you may not be able to do a difference posting as later described in the process step description. |

For demo and testing purposes, the simplest way to have no restrictions is to assign a user to the "SUPERVISOR" tolerance group. This group "bypasses" any value restrictions. In a productive system environment, you follow a much more restrictive policy.

You can make a decision for one of the two Activity Areas, depending on which scenario you want to conduct.

For Activity Area Y002, use AL, the storage-bin-specific annual count method.

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/PI_USER | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Settings > Physical Inventory > Assign User to Tolerance Group for Recount/Clearing |

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Assignment of User to Tolerance Group Posting and Recount/Clearing screen appears. |  |
| 2 | Set default value | When starting this transaction initially, enter Warehouse Number 3330 on the screen. If not asked, conduct the following steps:Choose Table View > Other View .Make the following entries:Warehouse Number: 3330Choose Enter. |  |  |
| 3 | Switch to Edit Mode | Choose Display > Change . |  |  |
| 4 | Assign to Tolerance Group | Choose New Entries and make the following entries:Tol. Grp Posting: CLERKIf you log on as a SUPERVISOR, make the following entry:User: <user supervisor>Tol. Grp Posting: SUPERVISORChoose Save. |  |  |

##### Assign User to Tolerance Group for Difference Analyzer

Purpose

In this transaction, you assign individual logon users to tolerance groups, which have previously been defined in the system configuration (refer to the EWA building block configuration guide). Generally, the assignment of users to tolerance groups determines whether a logon user can view and process differences in the Difference Analyzer.

For demo and testing purposes, the simplest way to have no restrictions is to assign a user to the "SUPERVISOR" tolerance group since this group "bypasses" any value restrictions. In a productive system environment, you would follow a much more restrictive policy.

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/PI_USER_DIFF | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Settings > Physical Inventory > Assign User to Tolerance Group for Difference Analyzer |

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Assignment of User to Tolerance Group Difference Analyzer screen appears. |  |
| 3 | Set default value | Choose Table View > Other ViewMake the following entries:Warehouse Number:3330Choose Enter. |  |  |
| 4 | Switch to Edit Mode | Choose Display > Change |  |  |
| 5 | Assign to Tolerance Group | Choose New Entries to create entries as needed. Here you need to make assignments to real system users. Therefore, the users given in <> brackets are only examples.User: user ClerkTolGr Diff.Analyzer: CLERKIf you logon as a supervisor, make the following entry:User: user SupervisorTolGr Diff.Analyzer: SUPERVISORChoose Save. |  |  |

##### Creating User Settings for the Difference Analyzer Transaction

Purpose

In this step, you set up user settings that are necessary for the Difference Analyzer transaction.

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/DIFF_ANALYZER | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Settings > Physical Inventory > Difference Analyzer |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Difference Analyzer - Warehouse 3330 screen appears. |  |
| 2 | Choose Default Values | Choose Default Values (F5) on the upper left corner. | A dialog box appears. |  |
| 3 | Set Values | Make the following entries:Warehouse No.: 3330Phys.Inv. Diff.: [X]Choose Continue (Enter). |  |  |

##### Check Warehouse Time Zone

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCMB/SCUMAIN | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Master Data > Maintain Supply Chain Unit |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Supply Chain Unit: Initial Screen screen appears. |  |
| 2 | Enter the Selection Data | On the Supply Chain Unit: Initial screen, make the following entries:Supply Chain Unit: YWAREHOUSE- 3330Type: 1002 | The Supply Chain Unit: Maintenance screen appears. |  |
| 3 | Check the Time Zone | Choose DisplayOn the Supply Chain Unit: Maintenance screen, on the General tab, in the Time Zone section, note the time zone of the warehouse, for example, CET - Central Europe Time. Daylight saving time is ignored by the system.During the paper-based inventory, the manually entered count date is considered to be in the Warehouse Time Zone. Your personal time zone settings in the SAP GUI are ignored.From the warehouse perspective, time and date of the count results must not be in the future. |  |  |

##### Determine and Set Prices from SAP S/4HANA System

Purpose

To be able to send the values of inventory deviations to SAP S/4HANA, the valuation prices have to be transferred out of SAP S/4HANA into EWM.

Procedure

1. Access the activity using the following navigation options:

| Transaction Code | Easy Access Menu(SAP EWM) |
| --- | --- |
| /SCWM/VALUATION_SET | Extended Warehouse Management > Physical Inventory > Periodic Processing Determine And Set Prices From ERP |

1. On the Determine and Set Prices screen, enter the following data:

| Field Name | Description | User Action and Values | Comment |
| --- | --- | --- | --- |
| Warehouse Number |  | 3330 |  |
| Party Entitled to Dispose |  | 33413310 |  |
| Product |  | TG11 |  |

1. Choose Goto > Variants > Save as a variant to save as a variant.
2. On the Variant Attributes screen, make the following entries:

| Field Name | Description | User Action and Values | Comment |
| --- | --- | --- | --- |
| Variant Name |  | YVALSET |  |
| Description |  | Sample Product's valuation PI |  |
| Only for Background Processing |  | [ ] | This flag has to be set only for usage in a background job. |

1. Choose Save.
2. On the Determine and Set Prices screen, choose Execute.
3. On the Valuation Set – Warehouse Number 3330 screen, select all rows.
4. Choose Execute

The following system message appears: Valuation data was saved.

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Initial Stock Upload

| Process Step, Report, or Item | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Upload Initial Stock in SAP EWM System](#unique_16) [page ] 15 |  | /SCWM/ISU | Socks to the different storage types are created with help of example data. (.csv) |
| [Check Material Documents (Optional)](#unique_17) [page ] 16 | Inventory Manager | Material Documents Overview (F1077) | Material document along with its financial posting is posted in the SAP S/4HANA system |

Physical Inventory

| Process Step, Report, or Item | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create Physical Inventory Documents in SAP EWM System](#unique_18) [page ] 18 |  | /SCWM/MON | Create PI documents. |
| [Enter Count Results in SAP EWM System](#unique_19) [page ] 19 |  | /SCWM/PI_PROCESS | Activate PI documents. |
| [Analyze Physical Inventory Differences and Post Them to SAP S/4HANA Cloud Public Edition From the SAP EWM System](#unique_20) [page ] 20 |  | /SCWM/DIFF_ANALYZER | All differences are posted to SAP S/4HANA |
| [Check Material Documents (Optional)](#unique_21) [page ] 21 | Inventory Manager | Material Documents Overview (F1077) | Material document along with its financial posting is posted in the SAP S/4HANA system |

Scrapping

| Process Step, Report, or Item | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Select Stock to Be Scrapped in SAP EWM](#unique_22) [page ] 23 | Warehouse Clerk (EWM) | /SCWM/MON | The system navigates to transaction SCWM/MON where the selected stock is displayed. |
| [Create Ad-Hoc Warehouse Tasks for Scrapping Damaged Stock in SAP EWM](#unique_23) [page ] 23 | Warehouse Clerk (EWM) | /SCWM/ADPROD | The warehouse tasks are created.The scrap stock is now in the scrap zone. |
| [Confirm Warehouse Order in SAP EWM](#unique_24) [page ] 25 | Warehouse Clerk (EWM) | /SCWM/TO_CONF | The warehouse tasks are confirmed.The scrap stock is now in the scrap zone. |
| [Empty Scrapping Zone and Post Goods Issue in SAP EWM](#unique_25) [page ] 25 | Warehouse Clerk (EWM) | /SCWM/ADGI | The unplanned goods issue is posted in SAP EWM and SAP S/4HANA.The scrap zone is empty in SAP EWM.The stock is decreased in EWM and SAP S/4HANA. |
| [Check Material Documents (Optional)](#unique_26) [page ] 26 | Inventory Manager | Material Documents Overview (F1077) | Material document along with its financial posting is posted in the SAP S/4HANA system |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Initial Stock Upload

You can use this process to initially provide stock to bins of the different final storage types provided with the warehouse. It gives a good example how stock upload can be done, and is also a simple and quick way to set the stage for testing.

The stock data for the upload is provided via different sheets containing products and storage types. The upload creates handling units using an internal HU numbering instead of assigning Standard Shipping Container Codes (SSCC) as done in the basic inbound process. The upload always populates bins listed at the end of a storage type to avoid possible overlaps with bins occupied by standard processes.

#### Upload Initial Stock in SAP EWM System

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/ISU | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Interfaces > Data Upload > Stock Data Transfer |

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Stock Data Transfer screen appears. |  |
| 2 | Fill in data | In the Stock Data Transfer screen, ensure that the following fields are complete:Warehouse Number: 3330Language: ENNumber of HUs per posting: 50Local File: XDisplay Data: X |  |  |
| 3 | Choose Open Folder | Choose Open Folder.Locate the*.csv files on your computer.isu_TG11.csvChoose Open.The system displays the path and file name of the selected .csv file.On the Stock Data Transfer screen, choose Upload.On the SAP GUI Security screen, choose Allow This One Time.Choose OK. | On the Stock Data Transfer screen, the uploaded rows from the .csv file are displayed |  |
| 4 | Upload the Initial Stock | Choose Start Stock Data transfer (F8).Record the number of the warehouse material document for later use.Note This is the Warehouse Material Document (a specific EWM Material Document).This is not the SAP S/4HANA Material Document ID. |  |  |

#### Check Material Documents (Optional)

Purpose

Along with populating the warehouse with stock and HUs, there is also a financial posting in the SAP S/4HANA system. The movement type for this is 561, the standard movement type for initial stock upload during a cut over before going live with an SAP S/4HANA materials management.

The check step is to show you the material document along with its financial posting in the SAP S/4HANA system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Material Documents Overview (F1077). |  |  |
| 3 | Change settings | In the Material Documents section, choose Settings on the right-hand side.Choose the column for Goods Movement Type.Choose OK. |  |  |
| 4 | Enter Selection data | On top of the screen, make the following entries:Stock Change: STOCK INCREASEStock Change Level: PlantPlant: 3310Storage Location: 333SMaterial: TG11Posting Date: The date when you uploaded initial stock into the warehouse.Choose your material and choose GO. |  |  |
| 5 | Check the material document | Choose Go.Material documents are listed.Note down the number of the Material Document with movement type 561.Choose the SAP S/4HANA Material Document.On the Display Material Document ########## screen, check the Delivery Note (located in the s tab).Note The delivery note contains the warehouse number concatenated with the warehouse document number. The warehouse document is posted from the previous step and can be displayed in the warehouse monitor in the corresponding warehouse task node. |  |  |

### Physical Inventory

In this process, you create physical inventory (PI) documents for a chosen number of storage bins or products on a regular basis to distribute the workload for physical inventory over the year.

By posting the PI documents, you adjust the book inventory in the storage bins to align it with the physical inventory counts. At different points in the process, tolerance checks control the count results and final postings that adjust the stock situation. Along with this process, you monitor the progress of your physical inventory within the warehouse monitor.

Besides these test step, there are several processes, which are not described in this document, such as the Recounting of PI documents, product specific counting, printing of PI documents, RF-counting, creating PI areas, adjust tolerances, or scheduling background jobs. In the below section, you find a lean process description with a focus on integration perspective.

#### Create Physical Inventory Documents in SAP EWM System

Purpose

As a part of the periodic physical inventory procedure, you can check the ongoing progress of PI per the storage bins or products through the warehouse management monitor.

During the periodic physical inventory procedure, you can check the progress of Physical Inventory in the warehouse management monitor and create new PI documents with Physical Inventory Procedure AL Annual Physical Inventory (Storage-Bin-Specific).

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/MON | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Monitoring > Warehouse Management Monitor |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Warehouse Management Monitor screen appears. |  |
| 2 | Enter data for Warehouse Monitor | Choose Default Values (F5).In the dialog box, make the following entries:Warehouse Number: 3330Monitor: SAPChoose Execute (F8). |  |  |
| 3 | Enter the Selection Data | In the folder hierarchy on the left, expandPhysical InventoryPhysical Inventory ProgressDouble-click the Storage Bin folder. On the /SCWM/SAPLPI_STATUS screen, make the following entries:Activity Area: Y002Completion Date: current dateChoose Execute (F8).Choose the row for Activity Area: Y002.Choose Open Bins for which you can perform physical inventory counting. |  |  |
| 4 | Create Physical Document | Select one open bin, and choose the More methods dropdown menu.Choose Create Phys.Inv. Document option. | The following message appears: Selection produced X results in total.You have created a PI document for a product due for periodic inventory counting. |  |
| 5 | Selection Physical Inventory Document | Select items and choose Set Flag .Check whether column active is checked.Choose Save.The following system message appears: Document <document number> <year> created.Note down that PI document number (for example, 100059) as you are going to need it later.Choose Edit. | The Status of your selected items is green now.Physical inventory Document - Process screen is now displayed. |  |

#### Enter Count Results in SAP EWM System

Purpose

In case of paper-driven PI, the warehouse clerk enters the count results into the system with the help of the PI count documents.

Also in case of complicated count results (for example, unexpected finding of many items or complete HUs), the desktop transaction is the better choice. This may also apply to an unplanned ("ad hoc") inventory count (checking a doubtful bin or product, which probably generates significant differences).

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/PI_COUNT | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Physical Inventory > Enter Count Results |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Enter Count Results screen appears. |  |
| 2 | Enter the Selection Data | On the Physical Inventory Document – Process – Whse No. 3330 Doc. Year 20XX screen, in the Find field, ensure Phys. Inv. Doc. has set as default. Otherwise, choose it in the dropdown menu.Enter the Physical Inventory Document Number from the previous step in the input field next to the Phys. Inv. Doc field.Choose Perform Search . |  |  |
| 3 | Select the PI Doc. | In the top table, choose the item(s) with your PI Doc. Number. |  |  |
| 4 | Enter Count Data on Header Level | Choose Count .In the Physical Inventory Document – Process dialog box, enter the following:Counter: Counter NameCount Date: Date and Time in 24-hour-formatChoose Continue (Enter).Note See chapter Check Warehouse Time Zone.We recommend using the time field in the standard 24-hour mode, for entries with am/pm-indicator you would have to use the input help. |  |  |
| 5 | Enter Count Data on Item Level | Choose all lines and switch to Form View.If there are no products in the storage bin, choose SBin Empty.If there are products in the storage bin, enter the product quantity and UoM in the Qty AUoM fields.(You have to navigate to Next Entry via the arrow on the left side).Choose Save.Choose Continue. | On the Count Items tab, there can be more than one item.Note down displayed numbers | PI document has the status Posted (POST) if the differences have been calculated and they are within the counting tolerance limit. |

#### Analyze Physical Inventory Differences and Post Them to SAP S/4HANA Cloud Public Edition From the SAP EWM System

Purpose

With the help of a background job, most of the differences are automatically posted to SAP S/4HANA Cloud Public Edition in the previous step. If the value of some differences violates the tolerances assigned to the background user, the warehouse clerk or the supervisor has to review these differences in the Difference Analyzer. For example, they analyze the movements of the product and may decide that a new PI is necessary. After the review, they manually post these differences to SAP S/4HANA Cloud Public Edition.

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/DIFF_ANALYZER | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Settings > Physical Inventory > Difference Analyzer |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Difference Analyzer - Warehouse 3330 screen appears. |  |
| 2 | Enter Selection Data | On the Difference Analyzer - Warehouse3330 screen, choose Open Advanced Search.In the Advanced Search section, on the Details section, enter the following:Physical Inventory Procedure: AL |  |  |
| 3 | Post Differences | Select the line items (if any), and choose Post.If the Post Differences dialog box appears, prompting you clear any differences confirm with Yes.Note the ID it is required for the next step. | A message Warehouse material document 1000000##### created appears.The differences are automatically posted to SAP S/4HANA Cloud Public Edition.To check the posting, you can log on with user role Inventory Manager and find app Display Material Document List. You can enter in the Reference field the concatenated value from above, for example, 10101000000#####and track your process. If you forgot the reference, search for Movement Type 711 to 712. |  |

#### Check Material Documents (Optional)

Purpose

Along with populating the warehouse with stock and HUs, there is also a financial posting in the SAP S/4HANA system. The movement type used for this is 561, which is the standard movement type for initial stock upload during a cutover before going live with an SAP S/4HANA materials management.

The check step is to show you the material document along with its financial posting in the SAP S/4HANA system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad with the Inventory Manager role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Material Documents Overview (F1077) . |  |  |
| 3 | Change settings | In the section Material Documents, choose Settings on the right-hand side.Choose the column for Goods Movement Type.Choose OK. |  |  |
| 4 | Enter Selection data | On top of the screen, make the following entries:Stock Change:Stock Change Level: PlantPlant: 3310Storage Location: 333SMaterial: TG11Posting Date: The date when you uploaded initial stock into the warehouse.Choose your material and choose GO |  |  |
| 5 | Check the material document | Material documents are listed.Note down the number of the Material Document with movement type 711 or 712. |  |  |
| 6 | Choose your document | Verify the movement type and the document number from previous step. |  |  |

### Scrapping

Purpose

In this process, you can decide to scrap goods that are currently stored in any of the storage types in the warehouse. The scrapping process can be initiated based on the expired shelf life of a stock item, or it can be triggered by discovering damaged goods in the warehouse in daily work.

For the first approach, you can search for expired stock items in the Warehouse Monitor. You then initiate the scrapping by creating the needed warehouse orders and tasks. The system supports scrapping for all storage types. Depending on the physical layout of the warehouse, the system automatically creates the warehouse orders and tasks and assigns them to the corresponding RF queues. The actual scrappings, including the financially relevant postings, are then either done manually or by means of a periodically scheduled program.

#### Select Stock to Be Scrapped in SAP EWM

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/MON | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Monitoring > Warehouse Management Monitor |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Warehouse Management Monitor screen appears. |  |
| 2 | Display Stock Overview | On the Warehouse Management Monitor SAP – Warehouse Number 3330 screen,choose Stock and Bin from the navigation area.Your Warehouse Monitor should be expanded.Next Double-click on Stock Overview. | /SCWM/SAPLSTOCK_OVERVIEW_MON screen is displayed. |  |
| 3 | Search for Product | On the /SCWM/SAPLSTOCK_OVERVIEW_MON screen, fill in your material what should be scrapped.Navigate to Product: TG11Choose Execute. | In the result list, you see the different storage types and bin which contain stock of that product.Identify the Damaged Stock that needs to be Scrapped.Note down the storage location and bin. |  |

#### Create Ad-Hoc Warehouse Tasks for Scrapping Damaged Stock in SAP EWM

Purpose

The Warehouse Operative (EWM) creates ad-hoc warehouse tasks to scrap damaged stock and physically move the stock to the scrapping zone.

Prerequisite

Damaged stock detected in the warehouse.

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/ADPROD | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Work Scheduling > Create Warehouse Task Without Reference > Move Product |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Create Product Warehouse Task in Warehouse Number 1730 screen appears. |  |
| 2 | Set default value | Enter Warehouse Number: 3330Warehouse Process Type: Y420 |  | Upper right section. |
| 3 | Choose your Product, which should be Scrapped | In the Create Product Warehouse Task in Warehouse Number 3330 screen, change the search criteria to Storage Bin.Fill the Storage Bin as you have written before. It should contain the damaged product TG11.Choose Execute(F8)Fill the Storage Destination Type: Y840 | The warehouse tasks are created.Note down the warehouse order number. |  |
| 4 | Create warehouse tasks to scrapping area | Select the line for your product.Switch to the Form View.Enter the quantity in field (Src Trgt Qty AUM): The number of damaged products.Fill Storage Destination Type: Y840Destination Bin: SCRAP-ZONEAfterwards: Choose Create + Save to save the warehouse tasks. | The warehouse tasks are created.Note down the warehouse order number. |  |

#### Confirm Warehouse Order in SAP EWM

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/TO_CONF | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Execution > Confirm Warehouse Task |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Confirm Warehouse Task in Warehouse Number 3330 screen appears. |  |
| 2 | Search for Warehouse Tasks | In the Confirm Warehouse Task in Warehouse Number, 3330, enter the Warehouse Order from previous step.Choose Search. | WO confirmed - WTS confirmed. |  |
| 3 | Choose | Choose Confirm + Save for the warehouse tasks. | The warehouse material document xx is created. |  |

#### Empty Scrapping Zone and Post Goods Issue in SAP EWM

Purpose

The Warehouse Clerk (EWM) empties the scrap zone by posting an unplanned goods issue.

|  |
| --- |
| Note You can schedule a periodic background job for this step (not described in detail here). |

Prerequisite

Prior steps were successfully performed to confirm the warehouse task for the scrap stock.

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/ADGI | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Execution > Post Unplanned Goods Issue |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Post Unplanned Goods Issue screen appears. |  |
| 2 | Enter Data for posing | On the Post Unplanned Goods Issue selection screen, make the following entries:Whse No: 3330Storage Type: Y840GI Process: SCRP ScrappingChoose Execute (F8). | The screen Post Unplanned GI – Warehouse Number 3330 is displayed.Physical Stock. |  |
| 3 | Post GI | Select all required items and choose Post GI. | In the status bar, a message confirming the creation of a warehouse material document appears.The goods issue is posted. The scrap zone is empty and the stock is decreased in SAP S/4HANA. |  |

#### Check Material Documents (Optional)

Purpose

Along with populating the warehouse with stock and HUs, there is also a financial posting in the SAP S/4HANA system. The movement type for this is 561, the standard movement type for initial stock upload during a cutover before going live with an SAP S/4HANA materials management.

The check step is to show you the material document along with its financial posting in the SAP S/4HANA system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Material Documents Overview (F1077). | Material Documents Overview screen is displayed. |  |
| 3 | Enter Selection data | On the top of the screen, make the following entries:Stock Change: Stock Increase or Stock decreasePlant: 3310Storage Location: 333SMaterial: TG11Posting Date: TodayChoose GO. | You can see two documents: One is for the posting change from free to blocked stock and the other document is for the status of the post goods issue. |  |
| 4 | Choose | Choose your document. | The Material Document view is displayed. |  |
| 5 | Check the material document | Check the following criteria:QuantityMovement Type: For the transfer posting from free to blocked Stock: 344 or for Scrapping: 551Stock Type: 07 | These criteria must be the same as in EWM after the Process Post Goods Issue. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

First you may have completed the following processes and conditions before you start with the test steps:

| Business Condition | Comment |
| --- | --- |
| SAP EWM Integration – Inbound Processing from Supplier (2VJ) | To ensure that there is enough stock for use in the outbound process, you bring stock into the warehouse using inbound processing. |
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
> Flagged while digesting this document, not verified: Storage Location is 333D in the master data table but 333S in the Material Documents Overview selection steps (initial stock upload, physical inventory and scrapping checks).

> [!warning] Conflict
> Flagged while digesting this document, not verified: The Stock Overview After Initial Stock Upload table refers to isu_SN01.csv and storage type SN01 (bins 001.01.01.01 to .03) while the Data Files section and master data name isu_TG11.csv and storage types Y001/Y002.

> [!warning] Conflict
> Flagged while digesting this document, not verified: The Purpose text of the Check Material Documents steps under Physical Inventory and Scrapping states movement type 561 (initial stock upload), but their test steps check movement types 711/712 and 344/551 respectively.

> [!warning] Conflict
> Flagged while digesting this document, not verified: The /SCWM/ADPROD access step expects a screen for Warehouse Number 1730 while all other steps and the master data use warehouse 3330.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-warehouse-ad-hoc-goods-issue-3bt-ae-sap-s-4hana-cloud-publ]]
- related-to :: [[11-inventory-warehouse-and-transportation/warehouse-physical-inventory-3bx-ae-test-script-sap-s-4hana-cloud-publ]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2YL_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 44,813 chars in the whole document
