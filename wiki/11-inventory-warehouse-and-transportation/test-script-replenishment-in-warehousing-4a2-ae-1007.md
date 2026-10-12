---
id: 11-inventory-warehouse-and-transportation/test-script-replenishment-in-warehousing-4a2-ae-1007
title: "Test Script: Replenishment in Warehousing (4A2_AE) (4A2_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 4A2: planned/automatic replenishment of fixed bins in EWM, with job scheduling and task confirmation."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-replenishment]
aliases: [4A2_S4CLD2608_BPD_EN_AE]
keywords: [EWM Replenishment of Fixed Bins, warehouse replenishment, fixed bin assignment, replenishment jobs, warehouse tasks, radio frequency devices, warehouse default values, warehouse monitor, business roles, master data scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4A2_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1007
topic: 11-inventory-warehouse-and-transportation/ewm-replenishment
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Replenishment in Warehousing (4A2_AE) (4A2_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4A2_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **EWM Replenishment of Fixed Bins** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Replenishment in Warehousing (4A2_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232854743)

[2 Prerequisites 3](#_Toc232854744)

[2.1 System Access 3](#_Toc232854745)

[2.2 Roles 3](#_Toc232854746)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232854747)

[2.4 Business Conditions 5](#_Toc232854748)

[2.5 Preliminary Steps 5](#_Toc232854749)

[2.5.1 Define Default Values for Warehouse Clerk (EWM) 5](#_Toc232854750)

[2.5.2 Define Default Values for Warehouse Operative (EWM) 6](#_Toc232854751)

[2.5.3 Assign Fixed Bin 6](#_Toc232854752)

[3 Overview Table 8](#_Toc232854753)

[4 Test Procedures 9](#_Toc232854754)

[4.1 Replenish Stock 9](#_Toc232854755)

[4.2 Schedule Job for Replenishment 10](#_Toc232854756)

[4.3 Check Replenishment Warehouse Tasks (Optional) 11](#_Toc232854757)

[4.4 Confirm Replenishment Warehouse Tasks 12](#_Toc232854758)

[4.4.1 Variant 1: With Fiori App 12](#_Toc232854759)

[4.4.2 Variant 2: With Radio Frequency Devices 13](#_Toc232854760)

## Purpose

Overview

With this process, you can plan and automate the creation of replenishment warehouse tasks to ensure the right inventory levels for your products in the areas where picking is done. This scope item supports planned and automatic replenishment of fixed storage bins. The planned replenishment can be started either interactively or as a regular application background job. In contrast, with automatic replenishment, the system starts replenishment when a warehouse task is confirmed. The system creates replenishment warehouse tasks if the current stock is below the defined threshold for the product’s fixed bin. The replenishment quantity is calculated as the difference between the maximum and the current bin quantity. At the end of the process, the warehouse operative confirms the warehouse tasks and makes sure that the stock is moved from the reserve to the picking area.

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

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG0012 | Trad. Good 0012,Reord. Pt.,Regular Proc. |  |
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
| Storage Type | SF01 | Fixed Bin Storage |  |
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
| BNZ - Create New Open MM Posting Period - MDS | You’ve completed the procedure described in the Create New Open MM Posting Period - MDS master data script. The posting period is up to date. |
| 3BR - Warehouse Inbound Processing or2Q2 - Data Migration to SAP S/4HANA from Staging | You've completed the procedure in the Warehouse Inbound Processing test script or in the Data Migration to SAP S/4HANA from Staging test script.Make sure you to have at least stock of 1 PAL or 48 PC for TG0012 in storage type SG01. |

### Preliminary Steps

#### Define Default Values for Warehouse Clerk (EWM)

Purpose

In this step, you define the default warehouse number for the Warehouse Clerk (EWM).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Change Inbound Deliveries - Deliveries |  |  |
| 3 | Choose Avatar | Choose your avatar.Then, choose Settings. |  |  |
| 4 | Enter Default Value | Choose Default Values.Enter the following data:Warehouse No.: 3350Choose Save. |  |  |

#### Define Default Values for Warehouse Operative (EWM)

Purpose

In this step, you define the default warehouse number for the Warehouse Operative (EWM).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM) . |  |  |
| 2 | Choose Avatar | Choose your avatar.Then, choose Settings. |  |  |
| 3 | Enter Default Value | Choose Default Values.In the Material Management section, enter the following data:Warehouse No.: 3350.Choose Save. |  |  |

#### Assign Fixed Bin

Purpose

In this step, you assign fixed storage bins to products.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Assign Fixed Bins |  |  |
| 3 | Enter Data | On the Assign Fixed Storage Bin screen, enter the following data:Warehouse Number:3350Product: TG0012Choose Run. |  |  |
| 4 | Maintain Fixed Bin | Choose Edit to switch to change mode.Choose Create.Make the following entries:Warehouse Number: 3350Party Entitled to Dispose: 33413310Storage Bin: SF01-03-03Product: TG0012Max.Qty: 100DisplayUoM Max. Qty: PCMin.Qty: 4DisplayUoM Min. Qty: PCChoose Save.Note If for storage type SF01, the replenishment level is set as Storage Bin Level for Fixed Bins by default, the stock levels are read for the invidual fixed bins. The replenishment quantites are calculated based on the stocks available in the bin compared to the required quantities. |  |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Replenish Stock](#unique_11) [page ] 9 | Warehouse Clerk (EWM) | Replenish Stock (/SCWM/REPL) |  |
| [Schedule Job for Replenishment](#unique_12) [page ] 10 | Warehouse Clerk (EWM) | Schedule Replenishment (F4319) |  |
| [Check Replenishment Warehouse Tasks (Optional)](#unique_13) [page ] 11 | Warehouse Clerk (EWM) | Warehouse Monitor (/SCWM/MON) |  |
| [Confirm Replenishment Warehouse Tasks](#unique_14) [page ] 12 | Warehouse Operative (EWM) | Process Warehouse Tasks (F4595) |  |

## Test Procedures

### Replenish Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can run through the following steps to perform a Planned Replenishment to create replenishment task(s).

In a real-life environment, you can schedule the Planned Replenishment Run as a regular background job.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with theWarehouse Clerk (EWM) role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Replenish Stock (/SCWM/REPL). |  |  |
| 3 | Schedule Replenishment | On the Schedule Replenishment screen, make the following entries:Plnd Rplnshmt: X.Warehouse Number: 3350.Party Entitled to Dispose: 33413310 .Product: TG0012 .Show Log Immediately: X .Choose Execute. |  |  |
| 4 | Perform Replenishment | On the Select Replenishment Items screen, check the proposed quantity to be replenished.Select the line item to be processed.Choose Perform ReplenishmentNote If the stock of TG0012 is not below the Min.Qty (4 PC) in the fixed storage bin, there is no replenishment proposal. The replenishment quantity is calculated as the difference between the maximum bin quantity and the current bin quantity, and then it is rounded to a multiple of the minimum replenishment quantity. You can maintain the minimum replenishment quantity in the product master via the Manage Product Master Data (F1602) app. See the details in the master data script Maintain Warehouse Products Attributes - MDS. If no minimum replenishment quantity is maintained in the product master, the system rounds the quantity with the basic Unit of Measure of the product. |  |  |

### Schedule Job for Replenishment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to run job for warehouse replenishment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Replenishment (F4319). |  |  |
| 3 | Enter Basic Parameters for New Job | Choose Create above the table.On the New Job screen, make the following entries:Job Template: Schedule Replenishment.Job Name: Schedule Replenishment for TG0012Choose Step 2. |  |  |
| 4 | Enter Scheduling Parameters for New Job | Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: x.Recurrence Pattern: Single Run.Choose OK.Choose Step 3. |  |  |
| 5 | Enter Parameters | Parameters:Plnd Rplnshmnt: xWarehouse Number:3350Party Entitled to Dispose:33413310Product:TG0012Execute in the Background:xShow Log Immediately:x |  |  |
| 6 | Schedule New Job | On the New Job screen, choose Schedule. | The new job is created and displays in the table of Application Jobs. |  |
| 7 | Refresh Application Jobs List | To check the status of the job you created, choose Go. | The Application Jobs table is refreshed. |  |
| 8 | Verify the Job Results | To see the outcome of the job, choose the icon in Results column. |  |  |

### Check Replenishment Warehouse Tasks (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is for checking warehouse task from replenishment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on to SAP Fiori Launchpad | Open the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Warehouse Monitor (/SCWM/MON) |  |  |
| 3. | Select the node | On the Warehouse Management Monitor SAP - Warehouse Number xxxx screen, choose Documents > Warehouse Task. Double-click on the node. |  |  |
| 4. | Enter the selection data | Make the following entries:Whse Process Type: S310Product: TG0012 .Choose Execute.Note down the warehouse task number. | The warehouse task for replenishment is displayed. |  |

### Confirm Replenishment Warehouse Tasks

#### Variant 1: With Fiori App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) processes the replenishment warehouse task.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Process Warehouse Tasks(F4595). |  |  |
| 3 | Enter Warehouse Task Number | On the Process Warehouse Tasks screen, make the following entries:Warehouse Task <WT number noted down in the previous step>.Choose Go. |  |  |
| 4 | Confirm Warehouse Task | Mark the checkbox for the selected warehouse task and choose Confirm. | The following system message appears: Warehouse task confirmed |  |

#### Variant 2: With Radio Frequency Devices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) performs the replenishment warehouse tasks and confirms them in the system with mobile Radio Frequency device.

|  |
| --- |
| Note For Working with Mobile RF Devices, make sure all the steps as described in the Setup Instruction guide for scope item 63V - Mobile RF Devices in Warehousing have been performed. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2. | Access the SAP Fiori app | Open the SAP Fiori app Test RF Environment (/SCWM/RFUI)Note Here the App allows you to test working in an RF environment. For working with Mobile RF Devices, see also SAP Note [3048632](https://me.sap.com/notes/3048632). |  |  |
| 3 | Enter Data for RFUI | Whse No: 3350Resource: SHR1-1Dflt Dvc.: SE01Choose Enter. |  |  |
| 4 | Choose Menu | Choose 01 System-Guided > 02 SystemGuided Queue. |  |  |
| 5 | Enter Queue Name | In the Queue field, enter for example SR-G01-F01.Choose Enter |  |  |
| 6 | Create Picking HU | Make the following entries:Pack.Mat: PMPALLETChoose Handling.The picking HU is created. |  |  |
| 7 | Choose Next | Scroll the screen to right with > and choose Next. |  |  |
| 8 | Enteror Verify the Source Information fields | Enter or verify the following fields if they are required:Src.Bin (Source Bin)SrceHU (Source HU)Prod. (Product)ActQty (Quantity)Choose Enter |  |  |
| 9 | Verify the Destination information fields | Verify the following fields:DstBin (Destination Bin)Choose Enter. |  |  |
| 10 | Repeat Steps | Repeat steps 6 to 9 until no suitable warehouse orders are found. |  |  |
| 11 | Logoff RFUI | You can choose Back to the previous screens.Choose Logoff.Choose Save. |  |  |

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
- see-also :: [[11-inventory-warehouse-and-transportation/stammdatenskript-lagerplatze-und-fixplatzzuordnungen-pflegen-sds-3kr-3]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4A2_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 21,792 chars in the whole document
