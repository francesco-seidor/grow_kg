---
id: 15-retail-operations/test-script-physical-inventory-for-distribution-centers-5fs-ae-sap-s-4
title: "Test Script: Physical Inventory for Distribution Centers (5FS_AE) - SAP S/4HANA Cloud Public Edition (5FS_S4CLD2608_BPD_EN_AE)"
description: "S/4HANA Cloud Public Edition 2608 test script for scope item 5FS_AE: prerequisites and steps for physical inventory and cycle counting in distribution centers."
cluster: 15-retail-operations
tags: [kb/retail-operations, topic/dc-inventory-and-physical-inventory]
aliases: [5FS_S4CLD2608_BPD_EN_AE]
keywords: [Inventory Management and Physical Inventory for…, physical inventory, cycle counting, cycle counting classification, physical inventory documents, inventory count entry, count differences, inventory difference posting, test scripts, recount]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FS_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1087
topic: 15-retail-operations/dc-inventory-and-physical-inventory
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Physical Inventory for Distribution Centers (5FS_AE) - SAP S/4HANA Cloud Public Edition (5FS_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FS_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Inventory Management and Physical Inventory for Distribution Centers** in Retail Operations. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Physical Inventory for Distribution Centers (5FS_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232856791)

[2 Prerequisites 4](#_Toc232856792)

[2.1 System Access 4](#_Toc232856793)

[2.2 Roles 4](#_Toc232856794)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232856795)

[2.4 Business Conditions 6](#_Toc232856796)

[2.5 Preliminary Steps 6](#_Toc232856797)

[2.5.1 Set Initial Stock for Material 6](#_Toc232856798)

[2.5.2 Define Cycle Counting Indicator 7](#_Toc232856799)

[2.5.3 Define Cycle Counting Classification 8](#_Toc232856800)

[3 Overview Table 10](#_Toc232856801)

[4 Test Procedures 11](#_Toc232856802)

[4.1 Check the Physical Inventory Document that is Open 11](#_Toc232856803)

[4.2 Create Physical Inventory Documents 12](#_Toc232856804)

[4.3 Print Physical Inventory Documents (Only Relevant for S/4HANA Cloud System) 13](#_Toc232856805)

[4.4 Physical Count 14](#_Toc232856806)

[4.5 Enter Inventory Count 15](#_Toc232856807)

[4.6 List Count Differences 16](#_Toc232856808)

[4.7 Recount (Optional) 17](#_Toc232856809)

[4.8 Post Inventory Count Differences 18](#_Toc232856810)

[4.9 Display Physical Inventory Document Object Page (Optional) 20](#_Toc232856811)

[4.10 Physical Inventory Analysis (Optional) 21](#_Toc232856812)

## Purpose

Overview

Real-time accurate stock information is essential for many key processes involving distribution centers, for example requirements planning or replenishment, allocation processes, and accounting. Especially for the sales process, it's mandatory to base availability information for the customer on up-to-date stock information (determined via Available-To-Promise calculation, which also considers, among others, planned goods receipts and issues). Furthermore, regular physical inventory counting is mandatory to meet legal requirements. Typically, inventory of all articles must be counted at least once a year.

Physical inventory counts can be triggered via various methods, such as cycle counting used to carry out physical inventory for sets of articles at regular intervals during a year.

First, physical inventory documents are created. The actual physical inventory is then executed by measuring, counting, and weighing stock, and entering the results in the physical inventory documents.

If the results differ from the expected quantities, a recount can be triggered or an immediate stock adjustment can be posted. The stock adjustment is documented by an article document and a corresponding update in financial accounting.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| Note In the retail industry, specific terms differ from the standard terms used in other lines of business. Therefore, SAP solutions which provide business processes across multiple lines of businesses may use terms for the corresponding business objects, transactions, and user interfaces that deviate from the retail terminology. For integration and reuse reasons, the SAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business business may thus include different terms that refer to the same concept. SAP intends to harmonize the terminology in the future.The following terms are used synonymously in this document:Table 1:Standard Terms in Lines of BusinessSAP S/4HANA Cloud Public Edition, retail, fashion, and vertical business businessMaterial, productArticleMaterial group, product groupMerchandise categoryPlant, locationSite (as superordinate term) - store and distribution center (DC) |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible through SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Inventory Manager (Retail) | SAP_BR_INVENTORY_MGR_RFM | Retail Inventory Management | SAP_BR_INVENTORY_MGR_RFM |  |
| Warehouse Clerk (Retail) | SAP_BR_WAREHOUSE_CLERK_RFM | Retail Inventory Processing | SAP_BR_WAREHOUSE_CLERK_RFM |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Plant | 3350 | DC 3350 AE |  |
| Storage Location | 995A | Storage Loc. DC | Shop floor w/o lean WM |
| Company Code | 3310 | Company Code 3310 |  |
| Material, single article | R_1006, R_1007 | My Best Frozen StrawberriesMy Best Frozen Raspberries | See sections Business Conditions and Preliminary Steps. |
| Material, generic article | R_1003 | ChocolateVariants;R_1003001R_1003002R_1003003R_1003004R_1003005R_1003006R_1003007R_1003008R_1003009R_1003010R_1003011R_1003012R_1003013R_1003014 | See sections Business Conditions and Preliminary Steps. |
| Display | R_2007 | Chocolate Bar Display |  |
| Sales Set | R_1052 | My Best Blond Shampoo & ConditionerComponents: R_1051 and R_1052 |  |
| Profit Center | Y3350 | Template DC |  |

### Business Conditions

Before you can test this scope item, you must have completed the following processes and fulfilled the following business conditions before you can go through this scope item:

| Scope Item ID | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting period is up to date. |

### Preliminary Steps

#### Set Initial Stock for Material

Purpose

To execute this scope item, the materials must be available in stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail) |  |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) app. | The action which was chosen last time is displayed. |  |
| 3 | Input Movement Type | Make the following entry and choose Enter.Executable Action in Transaction MIGO: Goods ReceiptReference Document for MIGO Transaction: Other | Goods Receipt Other-< Username > screen displays |  |
| 4 | Enter Material | On the Goods Receipt Other Screen: Material tab, make the following entry and choose Enter:Material: R_1006 | Material details are provided. |  |
| 5 | Enter Quantity Data | On the Goods Receipt Other screen: Quantity tab, make the following entry and choose Enter:Qty in Unit of Entry: 100Unit of Entry: <PC> | Quantity details are provided. |  |
| 6 | Enter details under where tab | On the Goods Receipt Other screen: Where tab, make the following entries and choose Enter:Movement Type: 561 (Receipt per initial entry of stock balances into unr. use)Plant : 3350Storage Location: 995A | Movement type, Plant and storage details are provided. |  |
| 7 | Save your entries | Choose Post. | Material document posted message in displayed. |  |

Financial Postings:

| Material | Debited Accounts | G/L Accounts | Profit Center |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 13600000Inventory TradingGd | 39912000Inv Init SF&amp;Fin Bal | Y3350 |

#### Define Cycle Counting Indicator

Use

The following procedure provides instructions for creating cycle counting indicator.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Cycle Counting.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Cycle Counting: Change screen is displayed. |  |
| 3 | Cycle Counting | Create the following settings:Choose New Entries to create 3 new entries with the following data:First Entry:Plnt: 3350CC Phys. Inv. Ind.: <A>No. of phys. invtories: <12>Float Time: <5>Usable: ValidSecond Entry:Plnt: 3350CC Phys. Inv. Ind.: <B>No. of phys. invtories: <6>Float Time: <3>Usable: ValidThird Entry:Plnt: 3350CC Phys. Inv. Ind.: <C>No. of phys. invtories: <5>Float Time: <2>Usable: Valid |  |  |
| 4 | Save Your Entries | Choose Save. | The cycle counting indicator is saved. |  |

|  |
| --- |
| Note These process steps are also applicable to the retail stores. |

#### Define Cycle Counting Classification

Purpose

This process step shows how to maintain Cycle Counting Indicator via Cycle Counting - Classification (F4486).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager (Retail) |  |  |
| 2 | Access the App | Open app.Cycle Counting - Classification (F4486) | Cycle Counting - Classification screen is displayed. |  |
| 3 | Enter Parameters | Enter the following data:Analytics Start Date: <First Day in This Year>Analytics End Date: <Today>Inventory Consumption Group: 000(STANDARD CONSUMPTION GROUP)Plant: 3350Product: R_1006Choose Go. |  |  |
| 4 | Maintain Physical Inventory Indicator | Select products under the Unclassified tab and choose Classify.In the Classify dialog box, enter below details:Cycle Counting Indicator : Replace Field Values and ACycle Counting Indicator Fixed: YesChoose Save. | A classify dialogue box displays.Physical Inventory Indicator is saved. |  |

## Overview Table

This scope item consists of several <choose the appropriate entity: process steps, reports, items> provided in the table below.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Check the Physical Inventory Document that is Open](#unique_11) [page ] 11 | Inventory Manager (Retail) | Manage Physical Inventory Documents (F0379A) | The Physical Inventory Document screen is displayed. |
| [Create Physical Inventory Documents](#unique_12) [page ] 12 | Inventory Manager (Retail) | Create Physical Inventory Documents (F3197) | The system generates physical inventory documents. |
| [Print Physical Inventory Documents (Only Relevant for S/4HANA Cloud System)](#unique_13) [page ] 13 | Inventory Manager (Retail) | Manage Physical Inventory Documents (F0379A) | The print physical inventory document screen is displayed |
| [Physical Count](#unique_14) [page ] 14 | Warehouse Clerk (Retail) |  | Execute the physical count manually |
| [Enter Inventory Count](#unique_15) [page ] 15 | Warehouse Clerk (Retail) | Manage Physical Inventory Count (F5430) | The enter inventory count Initial screen is displayed. |
| [List Count Differences](#unique_16) [page ] 16 | Inventory Manager (Retail) | Manage Physical Inventory Documents (F0379A) | Difference quantity of the material is verified. |
| [Recount (Optional)](#unique_17) [page ] 17 | Inventory Manager (Retail) | Manage Physical Inventory Documents (F0379A) | The Physical Inventory Document screen is displayed. |
| [Post Inventory Count Differences](#unique_18) [page ] 18 | Inventory Manager (Retail) | Manage Physical Inventory Documents (F0379A) | The List of inventory differences selection screen is displayed. |
| [Display Physical Inventory Document Object Page (Optional)](#unique_19) [page ] 20 | Inventory Manager (Retail) | Manage Physical Inventory Documents (F0379A) | The Physical Inventory Document screen is displayed. |
| [Physical Inventory Analysis (Optional)](#unique_20) [page ] 21 | Inventory Manager (Retail) | Physical Inventory Analysis (W0058) | The prompts screen is displayed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Check the Physical Inventory Document that is Open

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the open physical inventory document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager (Retail). |  |  |
| 2 | Access the App | Open Manage Physical Inventory Documents (F0379A) app. | The Manage Physical Inventory Documents screen displays. |  |
| 3 | Enter Data | Make the following entries:Plant: 3350Storage Location: 995AChoose Adapt Filters, select Adjustment Status and choose OK, then enter the following data:Adjustment Status: Select items <Not Posted> and <Partially Posted>and choose Go. | The Physical Inventory Documents screen displays. |  |
| 4 | Choose an Item | Choose one of the filtered items in Physical Inventory Documents list.If there are no open Physical Documents present, please skip step 4 and 5. | The Physical Inventory Documents screen displays. |  |
| 5 | Review Header Data | If Count Status is not counted, process the following steps:Enter Inventory CountPost Inventory Count DifferencesIf Adjustment Status is blank, process the following step:Post Inventory Count DifferencesFor the detailed instructions of how to "Enter Inventory Count" and "Post Inventory Count Difference", please go to test procedures chapter and the corresponding steps in the following sections. |  |  |

### Create Physical Inventory Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use Create Physical Inventory Documents (F3197) to create the documents for the physical inventory.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Inventory Manager (Retail) |  |  |
| 2 | Access the App | Open Create Physical Inventory Documents (F3197) app. | Create Physical Inventory Documents (F3197) screen is displayed. |  |
| 3 | Search Materials | In the upper area, enter the following data and choose Go:Posted to Stock: YesPlant: 3350Storage Location: 995AThe display sorting sequence can be adjusted by choosing Setting in the upper right corner of material list section.Hint: If you have executed this function before, your historical data are suggested. | The stock overview is displayed. |  |
| 4 | Adapt Filters | In the upper area, choose Adapt Filters and select Material Type and choose OK, then enter the following data and choose OK:Material Type: Trading GoodsAfter setting up the selection criteria, choose Go. | The filters are set. |  |
| 5 | Create Physical Inventory Document: Select Materials | On the Unrestricted-Used Stock tab, select the following material and choose Create Physical Inventory Documents:Material: R_1006 | Create Physical Inventory Documents dialog box displays. |  |
| 6 | Create Physical Inventory Document | In the Create Physical Inventory Documents dialog box, enter the following data and afterwards press create:Split Documents by: NoneMaximum Number of Items: <Default>Planned Count Date: <Today>Document Date:<Today>Expand the Additional Header Data, enter the following data:Physical Inventory Reference:<Enter any value to be used to link the documents created by this transaction>Set Posting Block：<Select>Freeze Book Inventory: <Deselect> | A document is created.Make a note of the created document number.The material list is displayed again, your selected article is not displayed here anymore. |  |

### Print Physical Inventory Documents (Only Relevant for S/4HANA Cloud System)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as Inventory Manager (Retail). |  |  |
| 2 | Access the App | Open Manage Physical Inventory Documents (F0379A) app. | The Manage Physical Inventory Documents screen is displayed. |  |
| 3 | Enter Data | Make the following entries:Physical Inventory Document: <Physical Inventory Document>Fiscal year : <current year>and choose Go. | The physical inventory document is appeared. |  |
| 4 | Select the Document | Choose the document entry. | The Physical Inventory Document screen is displayed with the details of the selected physical inventory document. |  |
| 5 | Print Document | Select Print Document icon at the right top corner. | Print Physical Inventory Document window is displayed. |  |
| 6 | Print Document | Choose the required settings and select Print. | The following message is appeared, Physical Inventory Document <Physical Inventory Document> <Fiscal Year> was printed. |  |

### Physical Count

Purpose

This process step shows you how to execute the physical count (Manual activity).

Procedure

This is a manual activity. It isn’t a system activity.

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail) |  |  |
| 2 | Access the App | Open Manage Physical Inventory Count (F5430) app. | Manage Physical Inventory Count (F5430) Initial screen is displayed. |  |
| 3 | Enter Parameters | Make the following entries and choose Go.Physical Inventory Document: Physical Inventory DocumentFiscal Year: <current year>Planned Count Date: <Planned Count Date as in Physical Inventory Document> [optional] | An entry with the given details displays with Count Status as Not Counted under the section Documents |  |
| 4 | Select the Document | Choose the document entry. | Manage Physical Inventory Count (F5430) screen displays with the details of the selected physical inventory document. |  |
| 5 | Choose Edit and enter quantity | Choose Edit displaying on the top right corner of the screenEnter the quantity in the below fieldCounted Quantity in the Entry: <<Quantity>> | Quantity Entered |  |
| 6 | Choose Save | Choose Save | Changes have been saved message displayed on the screen. |  |
| 7 | Verify the status | Navigate back to Manage Physical Inventory Count (F5430) initial screen and verify the status. | Status of the Physical Inventory document changes to Fully Counted. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager (Retail) |  |  |
| 2 | Access the App | Open Manage Physical Inventory Documents (F0379A) app. | The Manage Physical Inventory Documents screen is displayed. |  |
| 3 | Enter Data | Make the following entries:Physical Inventory Document： <Physical Inventory Document>Fiscal Year : <current year>and choose Go. | The physical inventory document is displayed. |  |
| 4 | Select the Document | Choose the document entry. | The Physical Inventory Document screen is displayed with the details of the selected physical inventory document. |  |
| 5 | Choose Post | Under Items section, select the item and choose Post. | Post window is displayed with the material details. |  |
| 6 | Verify Difference Quantity | Verify the Difference Quantity of the material. | Difference quantity of the material is verified. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager (Retail). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Physical Inventory Documents (F0379A) app. | The Manage Physical Inventory Documents screen displays. |  |
| 3 | Search Physical Inventory Documents | In the upper area, enter the following data and choose Go:Physical Inventory Document: <document number> (The document must be counted)Fiscal Year: <current year>Plant: 3350Storage Location: 995A | The Physical Inventory Document is displayed. |  |
| 4 | Check Details in Physical Inventory Document | In the Physical Inventory Documents area, choose the document that is displayed. | The Physical Inventory Document screen displays. |  |
| 5 | Selection for Recount | In the Items section, select materials to recount and choose Recount.In the Recount dialog box, make the following entries:Planned Count Date: <Today>Document Date: <Today>Expand the Additional Header Data, enter the following data:Physical Inventory Reference: <Enter any value to be used to link the documents created by this transaction>Set Posting Block: <Select>Then choose Create. | Recount document successfully created message displays. |  |
| 6 | Post Differences | To post the differences for the recounted document, execute the below sections:[Enter Inventory Count](#unique_15) [page ] 15[List Count Differences](#unique_16) [page ] 16[Post Inventory Count Differences](#unique_18) [page ] 18 |  |  |

### Post Inventory Count Differences

|  |
| --- |
| Note This section is not applicable, if the document is recounted. |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager (Retail) |  |  |
| 2 | Access the App | Open Manage Physical Inventory Documents (F0379A) app. | The Manage Physical Inventory Documents screen is displayed. |  |
| 3 | Enter Data | Make the following entries:Physical Inventory Document: <Physical Inventory Document>Fiscal year : <current year>and choose Go. | The physical inventory document is appeared. |  |
| 4 | Select the Document | Choose the document entry. | The Physical Inventory Document screen is displayed with the details of the selected physical inventory document. |  |
| 5 | Choose Post | Under Items section, select the item and choose Post. | Post window is displayed with the material details. |  |
| 6 | Choose Post | Choose Post. | Successfully posted message is appeared.Material document number is generated.Note If the difference is zero, no material document is created.Physical Inventory status changes to Counted,Adjusted. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad using the Inventory Manager (Retail) |  |  |
| 2 | Access the App | Open Manage Physical Inventory Documents (F0379A) app. | The Manage Physical Inventory Documents screen displays. |  |
| 3 | Search for Physical Inventory Document | Make the following settings and choose Go.Physical Inventory Document: <Physical Inventory Document>Fiscal year: <current year>Plant: 3350Storage Location : 995ACount Status: <Fully counted>Optional you can extend the selection criteria: Therefore, choose Adapt Filter. Here, extend Process Data and enter your user ID in the field Created by. | The requested search result is displayed. |  |
| 4 | Select Physical Inventory Document | Select the row of the Physical Inventory Document you want to overview. | Physical Inventory Document screen is displayed. |  |
| 5 | Check Physical Inventory Document Details | Check the Items, General Information, Output Management and Attachments details. | The correct detail information is displayed. |  |
| 6 | Back to Launch Pad | Select Home to go back to the Fiori launchpad. | The Fiori launchpad is displayed. |  |

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

Before you proceed to test this function, please follow the above detailed steps in Physical Inventory for Distribution Centers ( 5FS ), in order to have several physical inventory documents as test data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager (Retail) |  |  |
| 2 | Access the App | Open Physical Inventory Analysis (W0058) app. | Physical Inventory Analysis screen is displayed. |  |
| 3 | Choose Go | Choose Go beside Adapt Filters. | Details are displayed. |  |
| 4 | Select Measures | On the left section of DIMENSIONS screen, choose arrow beside Measures against Column s to expand the options.Choose Plus symbol against the field need to be added in the column, for example: Counted Quantity | The column Counted Quantity is added in the right-side analysis result. |  |
| 5 | Remove Measures | Choose Minus symbol the field that already selected as measures and need to be removed.For example, Book Value | The Book Value column is removed from the right-side analysis result. |  |
| 6 | Add Rows | On the left section of screen, In Available Fields section Choose Add field button against the field that needs to be added or drag the dimension field that needs to be added and drop it in the section of Rows.For example, drag Storage location and drop it below the Plant field in the section of Rows. | The Storage Location row is added in the right-side analysis is displayed. |  |
| 7 | Switch the Sequence of Dimension in Row | In the Rows section, drag and drop dimension field to adjust the sequence.For example, drag and drop Storage Location above Plant | The sequence of row dimension is adjusted. |  |
| 8 | Remove Rows | Drag the dimension field in the section of Rows and drop it back to the dimension section.For example, Storage Location | The Storage Location row is removed from the right-side analysis display. |  |
| 9 | Change Layout to Bar Chart | Choose Graphical Display on the right section of the screen. | The layout of analysis result is changed to bar chart. |  |
| 10 | Change Layout to Query Information | Choose Query Information on the right section of the screen. | Details displayed. |  |

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
- related-to :: [[15-retail-operations/test-script-inventory-management-for-distribution-centers-5fq-ae-sap-s]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5FS_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 34,024 chars in the whole document
