---
id: 11-inventory-warehouse-and-transportation/physical-inventory-cycle-counting-4lu-ae-test-script-sap-s-4hana-cloud
title: "Physical Inventory – Cycle Counting (4LU_AE) – Test Script, SAP S/4HANA Cloud Public Edition (4LU_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script (4LU, AE) for cycle counting: prerequisites, indicator setup, and count-to-posting steps with Fiori apps."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/physical-inventory]
aliases: [4LU_S4CLD2608_BPD_EN_AE]
keywords: [Physical Inventory Count and Adjustment, cycle counting, physical inventory, cycle counting indicator, cycle counting classification, physical inventory documents, physical inventory printing, inventory count entry, count differences, inventory recount]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4LU_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1034
topic: 11-inventory-warehouse-and-transportation/physical-inventory
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Physical Inventory – Cycle Counting (4LU_AE) – Test Script, SAP S/4HANA Cloud Public Edition (4LU_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4LU_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Physical Inventory Count and Adjustment** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Physical Inventory – Cycle Counting (4LU_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232855262)

[2 Prerequisites 4](#_Toc232855263)

[2.1 System Access 4](#_Toc232855264)

[2.2 Roles 4](#_Toc232855265)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232855266)

[2.4 Business Conditions 6](#_Toc232855267)

[2.5 Preliminary Steps 6](#_Toc232855268)

[2.5.1 Open New MM Period 6](#_Toc232855269)

[2.5.2 Initialize Material Stock 6](#_Toc232855270)

[2.5.3 Check Open Physical Inventory Document 7](#_Toc232855271)

[2.5.4 Define Cycle Counting Indicator 9](#_Toc232855272)

[2.5.5 Define Cycle Counting Classification 11](#_Toc232855273)

[3 Overview Table 13](#_Toc232855274)

[4 Test Procedures 14](#_Toc232855275)

[4.1 Create Physical Inventory Documents 14](#_Toc232855276)

[4.2 Print Physical Inventory Documents (Only Relevant for SAP S/4HANA Cloud Public Edition System) 16](#_Toc232855277)

[4.3 Physical Count 18](#_Toc232855278)

[4.4 Enter Inventory Count 18](#_Toc232855279)

[4.5 List Count Differences 20](#_Toc232855280)

[4.6 Recount (Optional) 21](#_Toc232855281)

[4.7 Post Inventory Count Differences 22](#_Toc232855282)

[4.8 Display Physical Inventory Document Object Page (Optional) 23](#_Toc232855283)

[4.9 Physical Inventory Analysis (Optional) 24](#_Toc232855284)

## Purpose

Overview

The cycle counting method is a special physical inventory procedure where inventory is counted at regular intervals within a fiscal year. In general, it starts with classification of materials based on ABC analysis or at the user's discretion. Additional counting intervals are set based on classification of materials. The counting intervals depend on the cycle count indicator. Creation of physical inventory documents then takes place. The creation can either be done manually by a requester or automatically (applicable for large volumes) based on cycle count indicator. The physical stocks are compared and realized for the given materials in the system. Any discrepancies in the system quantities and physical count are reviewed. The inventory may be recounted until final counts are accepted and inventory differences are posted.

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

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the provided sample data to go through the test procedure.

| Master | Sample Value | Details | Comments |
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
| Material | TG0011 | Trading Good 0011,PD,Regular Proc. | See Business Conditions and Preliminary Steps sections. |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |

### Business Conditions

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Comment |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You’ve completed the step described in the master data script. Posting Period is up-to-date.The material TG0011 is available in stock in considerable quantity. Recommended Quantity: 100. |

### Preliminary Steps

#### Open New MM Period

External Process

For this activity, run the following step from the Create New Open MM Posting Period - MDS (BNZ) to close MM period and open new posting period:

• Closing MM Period and Opening New Posting Period

#### Initialize Material Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In a real business case, the materials are usually purchased from external suppliers. For this test, we post initial stock directly to the storage locations. This process step shows you how to initialize material stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Input Material | Make the following entries and choose Enter:Material: TG0011Plant: Plant 1 AE (3310) |  |  |
| 4 | Select Stock | Select the icon beside the stock that you want to add initial stock, for example:Storage Location: 331AUnrestricted-Use Stock | The Manage Stock dialog box opens and is prefilled with the Storage Location, Stock Type and Current Quantity you entered in previous steps. |  |
| 5 | Add Initial Stock | Make the following entries and choose Post:Special Stock Type: Keep default as Standard stockStock Change: Initial EntryQuantity: Enter a number, for example, 100Document Date: <Today>Posting Date: <Today> | The system displays a message Material document XXXXXXXXXX/XXXX created. The stock has been added. |  |

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

#### Define Cycle Counting Indicator

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows how to configure Cycle Counting Indicator via SSCUI Cycle Counting (ID: 103357).

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Select Configure Your Solution Icon | Choose Configure Your Solution on the Manage Your Solution screen. | A list of configurable items is displayed. |  |
| 4 | Search SSCUI | Enter the following data in the search box and press Enter.103357Choose the line item named Physical Inventory. | SSCUIs Cycle Counting (ID: 103357) displays. |  |
| 5 | Configure Cycle Counting Indicator | Choose Configure for Cycle Counting (ID: 103357).Choose New Entries to create 3 new entries with the following data:First Entry:Plnt: 3310CC Phys. Inv. Ind.: <A>No. of phys. invtories: <12>Float Time: <5>Usable: ValidSecond Entry:Plnt: 3310CC Phys. Inv. Ind.: <B>No. of phys. invtories: <6>Float Time: <3>Usable: ValidThird Entry:Plnt: 3310CC Phys. Inv. Ind.: <C>No. of phys. invtories: <5>Float Time: <2>Usable: Valid | Change View Settings For Cycle Counting: Overview screen displays. |  |
| 6 | Save Your Entries | Choose Save. | The Cycle Counting Indicator is saved. |  |

SAP Central Business Configuration:

| Step | Step Name | Instruction | Expected Result | Example |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Configuration Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Cycle Counting.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Cycle Counting screen displays. |  |
| 3 | Configure Cycle Counting Indicator | Choose New Entries to create 3 new entries with the following data:First Entry:Plnt: 3310CC Phys. Inv. Ind.: <A>No. of phys. invtories: <12>Float Time: <5>Usable: ValidSecond Entry:Plnt: 3310CC Phys. Inv. Ind.: <B>No. of phys. invtories: <6>Float Time: <3>Usable: ValidThird Entry:Plnt: 3310CC Phys. Inv. Ind.: <C>No. of phys. invtories: <5>Float Time: <2>Usable: Valid | Change View Settings For Cycle Counting: Overview screen displays. |  |
| 4 | Save Your Entries | Choose Save. | The Cycle Counting Indicator is saved. |  |

#### Define Cycle Counting Classification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows how to maintain Cycle Counting Indicator via Cycle Counting - Classification (F4486).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Cycle Counting - Classification (F4486). | The Cycle Counting - Classification screen displays. |  |
| 3 | Search Material | Enter the following data:Analytics Start Date: <First Day in This Year>Analytics End Date: <Today>Inventory Consumption Group: 000(STANDARD CONSUMPTION GROUP)Plant: 3310Product: TG0011Choose Go. | The material is displayed. |  |
| 4 | Maintain Physical Inventory Indicator | Select material(s) under the Unclassified tab and choose Classify.In the Classify dialog box, choose Replace Field Values and A from the dropdown lists for Cycle Counting Indicator. Choose Yes for the Cycle Counting Indicator Fixed field.Choose Save. | A classify dialogue box displays.Physical Inventory Indicator is saved. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App / Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Physical Inventory Documents](#unique_13) [page ] 14 | Inventory Manager | Job Scheduling and Mass Processing - Physical Inventory (F4550) | Physical inventory documents are generated. |
| [Print Physical Inventory Documents (Only Relevant for SAP S/4HANA Cloud Public Edition System)](#unique_14) [page ] 16 | Inventory Manager | Manage Physical Inventory Documents (F0379A) | The system generates a physical inventory count sheet, documents are printed. |
| [Physical Count](#unique_15) [page ] 18 | Warehouse Clerk |  | Count is completed. |
| [Enter Inventory Count](#unique_16) [page ] 18 | Warehouse Clerk | Manage Physical Inventory Count (F5430) | Counts are entered. |
| [List Count Differences](#unique_17) [page ] 20 | Inventory Manager | Manage Physical Inventory Documents (F0379A) | The table displays existing differences of book and count quantity that can be printed, if necessary. |
| [Recount (Optional)](#unique_18) [page ] 21 | Inventory Manager | Manage Physical Inventory Item List - New Version (F8634) | A new physical inventory document is created. |
| [Post Inventory Count Differences](#unique_19) [page ] 22 | Inventory Manager | Manage Physical Inventory Documents (F0379A) | Differences are posted. |
| [Display Physical Inventory Document Object Page (Optional)](#unique_20) [page ] 23 | Inventory Manager | Manage Physical Inventory Documents (F0379A) | The physical inventory document is displayed. |
| [Physical Inventory Analysis (Optional)](#unique_21) [page ] 24 | Inventory Manager | Physical Inventory Analysis (MMIM_FPM_OVP_PI_ITEM (MMIM_FPM_OVP_PI_ITEM)). | The Physical Inventory Analysis screen displays. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Physical Inventory Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To create documents for the physical inventory, you have two options:

- Option A: Schedule Physical Inventory Jobs
- Option B: Create Physical Inventory Documents Manually

You can choose either option A or option B to execute the creation of physical inventory documents. You can follow the procedure below for option A to create physical inventory documents by scheduling backend jobs. If you want to go through the process for option B to create physical inventory documents manually, check the step in test script Physical Inventory – Inventory Count and Adjustment (BML).

|  |
| --- |
| Note The system supports only one open physical inventory document for the same material. |

Procedure

Option A: Schedule Physical Inventory Jobs

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Job Scheduling and Mass Processing - Physical Inventory (F4550). | The Application Jobs screen displays. |  |
| 3 | Create a Job | Choose Create to create a new job. | The New Job screen displays. |  |
| 4 | Define a Job (Step 1) | On the New Job screen, make the following entries:In the Template Selection area:Job Template: <Job Template>, for example: Cycle Counting: Create Physical Inventory DocumentsJob Name: <Job Name>, for example: Cycle Counting: Create Physical Inventory DocumentsNote For annual inventory task, please select: <Annual Inventory: Create Physical Inventory Documents> for the Regular Stock job template. |  |  |
| 5 | Define a Job (Step 2) | Choose Step 2 to go to the Scheduling Options area:Start Immediately: <select>Job Start: <Current Time>Note If the job needs to be run on a regular basis, choose Define Recurrence Pattern. |  |  |
| 6 | Define a Job (Step 3) | Choose Step 3 to go to the Parameters area.Process Selection:Process Type: <Cycle Counting>Selection Criteria:Material: TG0011Plant: 3310Storage Location: 331ADocument Header:Date Selection Type: <Relative>Planned Count Date Interval: <Next 30 Days>Freeze Book Inventory: <Select>Note If selecting Relative, choose a Planned Count Date Interval. If selecting Static, select dates for Planned Count Date From and Planned Count Date To.Split Criteria: NoneSorting: Choose your preferred way of sorting for the physical inventory documents to be created, for example sorting by Storage Bin or by Material Group.Choose Schedule. | The job is created. |  |
| 7 | Check Job Status | On the Application Jobs screen, check the status of the job created from last step. It can take a few minutes for the background job to create physical inventory documents. Please wait until the job status changes from In Process to Finished before processing the next step. | The job status becomes Finished. |  |
| 8 | Check Log | On the Application Jobs screen, choose the Log for the job created previously. | A document is created. Make a note of the created document number: __________ |  |

|  |
| --- |
| Note Leverage two predefined job templates (annual physical inventory, cycle counting) and adapt them to your needs. Based on the selected template, the system plans all materials that have to be counted since the last planning run or have reached a certain counting frequency. If you want to go through the step to create physical inventory documents manually, refer to test script Physical Inventory – Inventory Count and Adjustment (BML). |

### Print Physical Inventory Documents (Only Relevant for SAP S/4HANA Cloud Public Edition System)

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
| 4 | Background Print | Choose the Background Print button. | The Background Print popup displays. |  |
| 5 | Trigger Print | In the Items with Status part, select only Not Yet Counted and deselect all the other options.Click the Background Print button. | A message shows "Print job successfully scheduled.". |  |
| 6 | View Application Job (Optional) | In the message dialog, choose the Application Job link. | The Manage Physical Inventory Documents: Mass Printing screen displays. |  |
| 7 | Check Physical Inventory Documents | Go back to the app Manage Physical Inventory Documents (F0379A), and navigate to specific physical inventory document which has count progress as zero:For example, in the filter Physical Inventory Document, enter the document number you created in previous step, and choose Go.Click the line of the physical inventory document. | The physical inventory document page of the specific document is displayed. |  |
| 8 | Check Print Status | On the upper right corner of the Items table, click the Settings button.In View Settings dialog, search for Printed, then check this option and click OK.A new column Printed is added to the table. Check if its value is Yes. | The print status is yes. |  |
| 9 | Check Output | Go to the Output Management section, click the line of the print job just generated.Note As detailed information is not fully displayed, from the upper right corner of Output Management, click the view button Show More per Row. | Detailed information of the specific job is displayed in the Output Management section. |  |
| 10 | View Print Output | Choose the Display button to view the PDF output. | The PDF document of the print job displays in a new browser window. |  |
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
| 5 | Result of Counting | Choose Edit and enter the result of count quantity in Counted Quantity in Entry Unit.Note Enter a suitable count number. You can manage inventory differences by setting maximum thresholds for each physical inventory document and its items. Value thresholds per company code can be defined via the SSCUI Manage Tolerances for Physical Inventory Differences (ID: 106788). Additionally in this SSCUI, you may assign individual users to a tolerance group.Please be noted that this SSCUI applies current setting. Settings are not transportable between quality system and production system and the settings need to be maintained separately. For more information, CBC user can refer to [Settings via SAP Central Business Configuration (3-System Landscape)](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html).Note Besides directly entering value in the App, there’s another option to enter inventory count via Excel. After choosing the Edit button, click the Items Download/Upload button in the upper right corner of the screen to first download a template, enter counts offline, and then upload the edited Excel.Then choose Save. | The counts have been saved. |  |

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
| 3 | Adapt Filters | In the upper right area, choose Adapt Filters. Select Adjustment Status, and choose OK. | The filters are set. |  |
| 4 | Search Physical Inventory Documents | Make the following entries in filters and choose Go.Plant： 3310Count Status： Fully CountedAdjustment Status： Not PostedChoose the line of the physical inventory document. | The physical inventory document page of the specific document displays.On this screen, on the Items tab, details of the physical inventory documents are displayed. |  |
| 5 | Show More per Row | In the upper right corner of the table of the Items tab, click the view button Show More per Row. | All detailed information displays. |  |
| 6 | Display More Columns Relevant to Difference | Then choose the Settings button, and the View Settings dialog pops up.Select more fields to be displayed in the column, for example:Difference ValueDifference Value based on Count EntryChoose OK. | The table shows the differences between the book quantity and the count quantity that can be printed, if needed.Option A: If the count isn’t accepted, go to the task [Recount (Optional)](#unique_18) [page ] 21.Option B: If the count is accepted, go to the task [Post Inventory Count Differences](#unique_19) [page ] 22. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Physical Inventory Documents (F0379A). | The Physical Inventory Document Overview screen displays. |  |
| 3 | Search for Physical Inventory Document | Make the following settings and choose Go.Physical Inventory Document: <Document Number>Plant: <3310> | The requested search result displays. |  |
| 4 | Select Physical Inventory Document | Select the row of the Physical Inventory Document you want to overview. | The Physical Inventory Document screen display. |  |
| 5 | Check Physical Inventory Document Details | Check the General Information, Process Data and Items details. | The correct detail information shows. |  |
| 6 | Back to Launchpad | Choose Home to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad displays. |  |

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

Before you proceed to test this function, please follow the above detailed steps in Physical Inventory – Cycle Counting (4LU), in order to have several physical inventory documents available for analyze.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Physical Inventory Analysis (MMIM_FPM_OVP_PI_ITEM (MMIM_FPM_OVP_PI_ITEM)). | The Physical Inventory Analysis screen displays. |  |
| 3 | Set Search Parameter | Apply the following filter and choose Go.Fiscal Year: <Current Year>Note Choose fiscal year according to the physical inventory documents created in the previous steps. | Data Analysis tab displays values of the physical inventory documents. |  |
| 4 | Select Measures | In the left Navigation Panel, go to the Dimensions section, then choose arrow beside Measures to expand the options.Click the + button beside the field you want to add to display, for example: Counted Quantity.Note To avoid updating the analysis results lively, in the Navigation Panel, choose the Settings arrow besides Dimensions and select Defer Layout Update from the dropdown list. This is useful when processing large amount of data. | The Column Counted Quantity is added to the right-side data analysis result. |  |
| 5 | Remove Measures | Click the - button beside the field that already selected as measures and need to be removed, for example, Book Value. | The Book Value column is removed from the right-side data analysis result. |  |
| 6 | Add Rows | In the left Navigation Panel, drag the dimension field that needs to be added and drop it in Rows section, or click the button <!-- image omitted: unnamed -->(Add Field to Row Axis) beside the dimension field.For example, drag Storage location and drop it below the Plant field in the Rows section. | The Storage Location row is added to the right-side data analysis result. |  |
| 7 | Switch the Sequence of Dimension in Row | In the Rows section, drag and drop dimension field to adjust the sequence.For example, drag and drop Storage Location above Plant. | The sequence of row dimension is adjusted. |  |
| 8 | Remove Rows | Drag the dimension field, for example, Storage Location, from the Rows section and drop it back to the dimension section, or click the button <!-- image omitted: unnamed -->(Remove Field from Row Axis) beside the dimension field. | The Storage Location row is removed from the right-side data analysis display. |  |
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
- related-to :: [[11-inventory-warehouse-and-transportation/physical-inventory-inventory-count-and-adjustment-bml-ae-test-script-1]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4LU_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 43,009 chars in the whole document
