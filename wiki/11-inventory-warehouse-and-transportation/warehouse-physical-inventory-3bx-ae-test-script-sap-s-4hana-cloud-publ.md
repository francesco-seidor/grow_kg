---
id: 11-inventory-warehouse-and-transportation/warehouse-physical-inventory-3bx-ae-test-script-sap-s-4hana-cloud-publ
title: "Warehouse Physical Inventory (3BX_AE) - Test Script, SAP S/4HANA Cloud Public Edition (3BX_S4CLD2608_BPD_EN_AE)"
description: "Test script for SAP S/4HANA Cloud scope item 3BX_AE: warehouse physical inventory and cycle counting, from document creation to difference posting."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-physical-inventory-and-stock-handling]
aliases: [3BX_S4CLD2608_BPD_EN_AE]
keywords: ["EWM Physical Inventory, Scrapping and Ad Hoc Goods Issue", warehouse physical inventory, cycle counting, test scripts, physical inventory documents, count result entry, radio frequency counting, count confirmation, inventory difference analysis, tolerance groups]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3BX_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-926
topic: 11-inventory-warehouse-and-transportation/ewm-physical-inventory-and-stock-handling
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Warehouse Physical Inventory (3BX_AE) - Test Script, SAP S/4HANA Cloud Public Edition (3BX_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3BX_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **EWM Physical Inventory, Scrapping and Ad Hoc Goods Issue** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Warehouse Physical Inventory (3BX_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232852184)

[2 Prerequisites 4](#_Toc232852185)

[2.1 System Access 4](#_Toc232852186)

[2.2 Roles 4](#_Toc232852187)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232852188)

[2.4 Additional Manual Configuration 7](#_Toc232852189)

[2.5 Business Conditions 7](#_Toc232852190)

[2.6 Preliminary Steps 7](#_Toc232852191)

[2.6.1 Define Default Values for Warehouse Clerk (WM) 7](#_Toc232852192)

[2.6.2 Define Default Values for Warehouse Operative (WM) 8](#_Toc232852193)

[2.6.3 Assign User to Tolerance Group for Clearing 8](#_Toc232852194)

[2.6.4 Assign User to Tolerance Group for Difference Analyzer 9](#_Toc232852195)

[2.6.5 Define Cycle Counting Indicator 10](#_Toc232852196)

[2.6.6 Assign Cycle Counting Indicator 12](#_Toc232852197)

[3 Overview Table 13](#_Toc232852198)

[4 Test Procedures 14](#_Toc232852199)

[4.1 Variant 1: Create and Print Cycle Counting Document 14](#_Toc232852200)

[4.2 Variant 2: Create and Print Counting Document 15](#_Toc232852201)

[4.3 Variant 3: Create Counting Document with Radio Frequency 16](#_Toc232852202)

[4.4 Enter Count Result 18](#_Toc232852203)

[4.4.1 Variant 1: With Fiori App 18](#_Toc232852204)

[4.4.2 Variant 2: With Radio Frequency Devices 19](#_Toc232852205)

[4.5 Confirm Inventory Count Results 22](#_Toc232852206)

[4.6 Analyze Differences 24](#_Toc232852207)

## Purpose

Overview

In this scope item, you can plan, conduct, and confirm regular counts of actual product quantities in the warehouse and compare the physical stock to the data in the system. You first create physical inventory documents for a chosen number of storage bins or products or based on cycle counting indicators. The cycle counting method is used to count products at regular intervals during a year. You can set up counting intervals based on cycle count indicators. After the documents are created and printed, you count the stock in the warehouse. You enter the count result in the system and review discrepancies in the system quantities. By posting the PI documents, you adjust the book inventory in the storage bins to align it with the physical inventory counts. The inventory may be recounted until final counts are accepted. Finally, inventory differences are posted to reconcile stocks in the SAP S/4HANA Cloud Public Edition system.

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
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trad.Good 11,PD,Reg.Trading | Storage |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad. | Fixed Bin Storage |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFO | Bulk Storage |
| Material | TG0011 | Trading Good 0011,PD,Regular Proc. | General Storage |
| Material | TG0013 | Trading Good 0013,PD,Regular Proc. | General Storage |
| Company Code | 3310 |  |  |
| Purchase Organization | 3310 |  |  |
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
| Storage Type | S970 | Clarification Zone |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| 3KQ | Maintain Warehouse Products Attributes - MDS |
| 3KR | Maintain Storage Bins and Fixed Bin Assignments - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/94d961d12c4f0bc013f495cec9d52ac0)

Before you start the testing, please make sure that the steps in the [Warehouse Management Setup Guide.docx (Public)](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_588%20Warehouse%20Management%20Setup.docx) published on SAP Activate Roadmap Viewer have been completed.

If you are working with a radio frequency device, carry out the steps described in Mobile RF Devices in Warehousing (63V).

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the procedure in the Create New Open MM Posting Period - MDS test script. |
| 3BR - Warehouse Inbound Processing or2Q2 - Data Migration to SAP S/4HANA from Staging | You have completed the procedure in the Warehouse Inbound Processing test script or in the Data Migration to SAP S/4HANA from Staging test script. |

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

#### Assign User to Tolerance Group for Clearing

Purpose

Here, you assign individual logon users to tolerance groups which have previously been defined in the system.

Generally, the assignment of users to tolerance groups determines whether a logon user can post differences or enter values within the tolerance boundaries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Assign Tolerance Group - Count Confirmation (/SCWM/PI_USER). |  |  |
| 3 | Close Warning Message | If there’s a warning message for the initial value, choose Continue to confirm it. |  |  |
| 4 | Switch to Edit Mode | Choose Edit. |  |  |
| 5 | Assign to Tolerance Group | Choose New Entries and make the following entries:User: <User>.AA:Tolerance Group: STOLCHECK.Note Choose STOLCHECK if you want to have the tolerance check, otherwise choose SNOTOLCHECK.Choose Save. |  |  |

#### Assign User to Tolerance Group for Difference Analyzer

Purpose

In this transaction, you assign individual logon users to tolerance groups which have previously been defined in the system configuration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed |  |
| 2 | Access App | Open Assign Tolerance Group - Differences (/SCWM/PI_USER_DIFF). |  |  |
| 3 | Close Warning Message | If there is a warning message for the initial value, choose Continue to confirm it. |  |  |
| 4 | Switch to Edit Mode | Choose Edit. |  |  |
| 5 | Assign Tolerance Group (Original) | Choose New Entries to create entries as needed. Here, you need to make assignments to real users that you use in your system. Therefore, the following users given in angle brackets (<>) are only examples.If you log on as a background job user, enter the following data:User: <User>Tolerance Group: SNOTOLCHECKNote Choose STOLCHECK if you want to have the tolerance check. Otherwise, choose SNOTOLCHECK.Choose Save.Note If you choose SNOTOLCHECKs on company code level, there's still a maximum value limitation by default. If a physical inventory document exceeds value 100,000 on header level or 10,000 on item level, the user is not allowed to post any inventory differences for this document. However, the maximum value can be adjusted via the Maintain Physical Inventory Tolerance configuration step. |  |  |

#### Define Cycle Counting Indicator

Purpose

In this step, you define the sample counting indicator. For each indicator, you define

- the interval in work days after which a new physical inventory should be performed.
- the buffer time in work days.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Configuration Expert - Business Process Configuration . |  |  |
| 2 | Choose App | Open Manage Your Solution (F1241). |  |  |
| 3 | Choose Option | Choose Configure Your Solution.Search for Configure Cycle Counting. |  |  |
| 4 | Navigate to the Configuration Step | Choose the configuration item and navigate to the Configure Cycle Counting step, then choose Configure. |  |  |
| 5 | Enter Data | Choose New Entries and enter the following data:1st Entry:Warehouse Number: 3350.CC Option : A .Interval: 60.Buffer: 5.2nd Entry:Warehouse Number: 3350.CC Option : B .Interval: 120.Buffer: 5.3rd Entry:Warehouse Number: 3350.CC Option : C .Interval: 240.Buffer: 5.Choose Save. |  |  |

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed unter Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

#### Assign Cycle Counting Indicator

Purpose

In this step, you assign the cycle counting indicator to the product master. The maintenance of the cycle counting indicator is also supported in data migration of warehouse products (see the Data Migration to SAP S/4HANA from Staging (2Q2) scope item).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Master Data Specialist - Product Data. |  |  |
| 2 | Choose App | Open Manage Product Master Data (F1602). |  |  |
| 3 | Enter Selection Data | Maintain the following selection value:Product: TG12.Choose Go. |  |  |
| 4 | Select Product | Choose the entry of the product. |  |  |
| 5 | Choose Tab | Choose the Warehouse Management tab and then the Warehouse subtab. |  |  |
| 6 | Choose Warehouse | Choose the row for warehouse number 3350. |  |  |
| 7 | Enter Data | Maintain the following value:Cycle Counting Indicator: A.Note Depending on the counting interval for the product, you assign different cycle counting indicators.Choose Apply. |  |  |
| 8 | Save Data | Choose Save. |  |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Variant 1: Create and Print Cycle Counting Document](#unique_15) [page ] 14 | Warehouse Operative (EWM) | Create Inventory Documents - Cycle Counting (/SCWM/PI_CC_CREATE) | You have created a physical inventory document. |
| [Variant 2: Create and Print Counting Document](#unique_16) [page ] 15 | Warehouse Operative (EWM) | Create Inventory Documents - Physical Inventory (/SCWM/PI_DOC_CREATE) | You have created and printed the counting documents. |
| [Enter Count Result](#unique_17) [page ] 18 | Warehouse Operative (EWM) | Count Physical Inventory - Paper-Driven Counting (F3340) | You have entered the count result. |
| [Confirm Inventory Count Results](#unique_18) [page ] 22 | Warehouse Clerk (EWM) | Confirm Inventory Count Results (/SCWM/MONNAV_PI_CONF) | You have checked and confirmed the inventory count results. |
| [Analyze Differences](#unique_19) [page ] 24 | Warehouse Clerk (EWM) | Analyze Differences (/SCWM/DIFF_ANALYZER) | You have cleared all differences and a material document is created. |

## Test Procedures

### Variant 1: Create and Print Cycle Counting Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) creates a physical inventory document for inventory counting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Warehouse Operative (EWM). |  |  |
| 2 | Access App | Open Create Inventory Documents - Cycle Counting (/SCWM/PI_CC_CREATE). |  |  |
| 3 | Enter Selection Data | Maintain the following entries:Warehouse Number: 3350.Cycle Counting Indicator: A.Count Date: <Current date or date in the future>.Print PI Document: X.You can enter other selection data such as activity area, products, and storage bins.Choose Execute. | The PI document is created. |  |
| 4 | Create Physical Inventory Document | Select the line(s) for which a physical inventory should be processed.Choose Create.Note down the physical inventory document number. |  |  |

### Variant 2: Create and Print Counting Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The warehouse operative creates the physical inventory document for inventory counting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Create Inventory Documents - Physical Inventory (/SCWM/PI_DOC_CREATE). |  |  |
| 3 | Enter Selection Data | Maintain the following entries:Warehouse Number: 3350.Physical Inventory Procedure: AL (Annual Physical Inventory (Storage-Bin-Specific))Note You can choose another physical inventory procedure, for example, HL, HS, or AS, according to your requirement.Count Date: <Current date or date in the future>Print PI Document: XYou can enter other selection data such as activity area, products, and storage bins.Choose Execute. | The PI document is created. |  |
| 4 | Create Physical Inventory Document | Select the lines for which a physical inventory should be processed.Choose Create.Note down the physical inventory document number. |  |  |

### Variant 3: Create Counting Document with Radio Frequency

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) creates the ad-hoc physical inventory document for inventory counting with the mobile Radio Frequency device.

|  |
| --- |
| Note For Working with Mobile RF Devices, make sure all the steps as described in the Setup Instruction guide for scope item 63V - Mobile RF Devices in Warehousing have been performed. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM) . | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Test RF Environment(/SCWM/RFUI). |  |  |
| 3 | Enter Data for RFUI | On the screen, make the following entries:Whse No: 1750Resource: SCNT-1Dflt Dvc.: SE01 |  |  |
| 4 | Choose Enter. | Choose Enter. | The 05 Internal Process button is displayed. |  |
| 5 | Choose Menu | Choose 05 Internal Process > 01 Inventory Counting > 03 Adhoc Inv. Creation. | Empty text input fields Stor.Bin and Product are displayed. |  |
| 6 | Enter Data for PI document | Make the following entries:Stor.Bin: <Enter Storage Bin for which you want to count>Product: < Enter Product >Note Note If you just enter Storage bin data, the Ad-hoc Bin Specific PI document with HL procedure is created.If you enter both storage bin and product data, the Ad-hoc product specific PI document with HS procedure will be created. |  |  |
| 7 | Set Block Indicator (Optional) | Choose SetBlk, if required.Note Note This indicator is used to block the storage bin, if a physical inventory document is created for bin-specific physical inventory or to block product movement for product-specific physical inventory. |  |  |
| 8 | Create Counting Document | Choose CrPI. | The SAP dialog box appears.The following system message appears:S: Document <document number year>created (/LIME/PI_CORE040) |  |
| 9 | Choose Enter | In the SAP dialog box, choose Enter. |  |  |
| 10 | Note down the document number | Note down the document number. |  |  |

### Enter Count Result

#### Variant 1: With Fiori App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) enters the count result in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). |  |  |
| 2 | Access App | Open Count Physical Inventory - Paper-Driven Counting (F3340). |  |  |
| 3 | Select Physical Inventory Document | Maintain the following selection values:Warehouse Number: 3350.Document Year: <Current Year>.Physical Inventory Document: <PI document created before>.Choose Go.Choose the PI document and choose Count. |  |  |
| 4 | Enter Count Results | Enter Counter.Enter Count Date and Time.If the count date is equal to the current date, you can leave the field blank as it is filled automatically.Enter Quantity and UoM.If the bin is empty, check 'Bin Empty'. |  |  |
| 5 | Save Your Changes | Choose Save. |  |  |

#### Variant 2: With Radio Frequency Devices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) enters the count result via mobile Radio Frequency device.

|  |
| --- |
| Note For working with Mobile RF Devices, make sure all the steps as described in the Set-up Instruction guide for scope item 63V - Mobile RF Devices in Warehousing have been performed. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Test RF Environment(/SCWM/RFUI) |  |  |
| 3 | Enter Data for RFUI | On the screen, make the following entries:Whse No: 1750Resource :SCNT-1Dflt Dvc. :SE01 |  |  |
| 4 | Choose Enter. | Choose Enter. | The 01 System-Guided button is displayed. |  |
| 5 | Choose 01 System-Guided > 02 SystemGuided Queue. | Choose 01 System-Guided > 02 SystemGuided Queue. | Empty text input field Queue is displayed. |  |
| 6 | Enter Queue Name | make the following entries:Queue: <queue>Note Example:SP-001 Physical Inventory in Standard StorageSP-B01 Physical Inventory in Bulk StorageSP-F01 Physical Inventory in Fixed Bin StorageSP-GEN Physical Inventory in General Storage |  |  |
| 7 | Choose Enter. | Choose Enter. | A field labeled Stor.BinAn entry showing: <storage bin>Location designation: <XX>An empty text field next to the storage bin entryare displayed. |  |
| 8 | Verify Storage Bin | Verify the Stor.Bin (Storage Bin).Copy the <storage bin entry> to the empty text field next to the storage bin entry. |  |  |
| 9 | Choose Enter. | Choose Enter. | Bin: <storage bin>Material: <material>Description:<material description>Unit:<PC (Pieces)>Total:<PC (Pieces)>is displayed. |  |
| 10 | Choose Enter | Choose Enter. | An empty text field next to the material entry is displayed.Note if an empty text field next to the HU: field is displayed, go to step 16. |  |
| 11 | Verify the product. | Verify the product.Copy the <material number> to the empty text field next to the material entry. |  |  |
| 12 | Choose Enter. | Choose Enter. | The quantity field becomes editable. |  |
| 13 | Enter quantity | make the following entries:Quantity: <quantity>UOM: <unit of measurement> |  |  |
| 14 | Choose Enter. | Choose Enter. | The entered quantity is displayed in the Total field.Note if an empty text field next to the SN: field is displayed, go to step 25. |  |
| 15 | Save Counting Result | Choose Save.Note Scroll the screen to right if you cannot find the button with button >. | The following system message appears: E: Suitable warehouse orders were not found (/SCWM/RF_EN056)Note Although this is an error message it confirms that the counting task is completed. |  |
| 16 | Enter HU for Counting (optional) | make the following entries:HU: <HU number> |  |  |
| 17 | Choose Enter. | Choose Enter. | The entered HU number appears below the HU field with an X. |  |
| 18 | Repeat until all Hus are entered. | Repeat until all Hus are entered. |  |  |
| 19 | Choose Enter. | Choose Enter. | An empty text field next to the material entry is displayed. |  |
| 20 | Verify the product. | Verify the product.Copy the <material number> to the empty text field next to the material entry. |  |  |
| 21 | Choose Enter. | Choose Enter. | The quantity field becomes editable. |  |
| 22 | Enter quantity | make the following entries:Quantity: <quantity>UOM: <unit of measurement> | The entered quantity is displayed in the Total field. |  |
| 23 | Choose Enter. | Choose Enter. |  |  |
| 24 | Save the HU entry | Choose Save.Note Scroll the screen to right if you cannot find the button with button >. | The following system message appears: E: Suitable warehouse orders were not found (/SCWM/RF_EN056)Note Although this is an error message it confirms that the counting task is completed. |  |
| 25 | Enter Serial Numbers (optional) | make the following entries:SN: <serial number> |  |  |
| 26 | Choose Enter. | Choose Enter. | The entered serial number appears below the SN field with an X. |  |
| 27 | Repeat Serial Number entry | Repeat the serial number entry until all serial numbers of the physical stock in the bin are entered. |  |  |
| 28 | Save serial numbers entered | Choose Save. | The entered quantity is displayed in the Total field. |  |
| 29 | Save total quantity | Choose Save.Note Scroll the screen to right if you cannot find the button with button >. | The following system message appears: E: Suitable warehouse orders were not found (/SCWM/RF_EN056)Note Although this is an error message it confirms that the counting task is completed. |  |
| 30 | Repeat Steps | Repeat steps until no suitable warehouse orders are found. |  |  |

### Confirm Inventory Count Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Clerk (EWM) checks the counting result and posts the difference. In case that the difference is outside tolerance, he or she can trigger the recounting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Confirm Inventory Count Results(/SCWM/MONNAV_PI_CONF). | The Enter warehouse number dialog box appears. |  |
| 3 | Enter warehouse number | In the Enter warehouse number dialog box, make the following entries:Warehouse No.: 1750. |  |  |
| 4 | Choose Continue. | Choose Continue. | The Confirm Inventory Count Result - Whse. <warehouse> (Time Zone <time zone>) screen appears. |  |
| 5 | Choose Set Selection Criteria. | On the Confirm Inventory Count Result - Whse. <warehouse> (Time Zone <time zone>) screen, choose Set Selection Criteria. | The /SCM/SAPLPI_HISTORY dialog box appears. |  |
| 6 | Search PI Document | In the /SCM/SAPLPI_HISTORY dialog box, make the following entries:Physical Inventory Status: COUN.Count Date: <Count Date you entered before>. |  |  |
| 7 | Choose Execute. | Choose Execute. | The screen displays an inventory count results table. |  |
| 8 | Select physical inventory document | Select one line with your physical inventory document. | The selected line is highlighted. |  |
| 9 | Choose More methods > Post Phys. Inv. Document. | Choose More methods > Post Phys. Inv. Document. | The Display Logs dialog box appears.The following system messages appear:Document <number> postedAction was executed successfully |  |
| 10 | Trigger Recount (optional) | If the selected PI document is not posted in the previous step, choose More methods > Recount Phys. Inv. Document to trigger the recounting. | The status of the PI document changes to RECO. A new PI document is created for recounting. |  |

### Analyze Differences

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Clerk (EWM) posts the differences to the ERP to align the stock figures.

|  |
| --- |
| Note It is not possible to post the serial number differences on item level as this leads to problems upon lost and found of a serial number. See more details in note [2871065](https://me.sap.com/notes/2871065) |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Analyze Differences(/SCWM/DIFF_ANALYZER). | The SAP dialog box appears. |  |
| 3 | Set Default Values | In the SAP dialog box, make the following entries:Warehouse No.: 1750.Phys. Inv. Diff.: X.WT Difference: X. |  |  |
| 4 | Choose Continue. | Choose Continue. | The Difference Analyzer - Warehouse<warehouse> (Time Zone <time zone>) screen appears. |  |
| 5 | Enter Product | On the Difference Analyzer - Warehouse<warehouse> (Time Zone <time zone>) screen, make the following entries:Find Product: <Product>Note Example: TG11 |  |  |
| 6 | Choose Search. | Choose Search. | The Differences – Cumulative table is displayed with records if differences were recorded before. |  |
| 7 | Select one record. | Select one record. | The selected line is highlighted. |  |
| 8 | Choose Post + Save. | Choose Post + Save. | The Post Differences? dialog box appears. |  |
| 9 | Choose Yes. | In the Post Differences? dialog box, choose Yes. | The following system message appears: Warehouse task <number> created. |  |

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
> Flagged while digesting this document, not verified: Internal inconsistency in warehouse number: sample data, default values, Fiori counting and cycle counting steps use warehouse 3350, but the RF steps (Whse No: 1750), Confirm Inventory Count Results (Warehouse No.: 1750) and Analyze Differences (Warehouse No.: 1750) use 1750.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-sap-ewm-integration-warehouse-stock-handling-2yl-ae-889]]
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-warehouse-ad-hoc-goods-issue-3bt-ae-sap-s-4hana-cloud-publ]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3BX_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 36,695 chars in the whole document
