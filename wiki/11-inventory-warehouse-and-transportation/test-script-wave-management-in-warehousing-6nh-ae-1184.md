---
id: 11-inventory-warehouse-and-transportation/test-script-wave-management-in-warehousing-6nh-ae-1184
title: "Test Script: Wave Management in Warehousing (6NH_AE) (6NH_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 6NH Wave Management in Warehousing: wave templates, wave job, simulation, release, logs, exception handling."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-wave-management]
aliases: [6NH_S4CLD2608_BPD_EN_AE]
keywords: [Wave Management in Warehousing, wave management, wave templates, wave generation job, wave simulation, wave release, wave exception handling, warehouse tasks, warehouse outbound processing, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6NH_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1184
topic: 11-inventory-warehouse-and-transportation/ewm-wave-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Wave Management in Warehousing (6NH_AE) (6NH_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6NH_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Wave Management in Warehousing** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Wave Management in Warehousing (6NH_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232859468)

[2 Prerequisites 3](#_Toc232859469)

[2.1 System Access 3](#_Toc232859470)

[2.2 Roles 3](#_Toc232859471)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232859472)

[2.4 Business Conditions 4](#_Toc232859473)

[2.5 Preliminary Steps 4](#_Toc232859474)

[2.5.1 Maintain Wave Templates 4](#_Toc232859475)

[3 Overview Table 7](#_Toc232859476)

[4 Test Procedures 8](#_Toc232859477)

[4.1 Schedule Background Job for Wave Generation 8](#_Toc232859478)

[4.2 Simulate Wave (Optional) 9](#_Toc232859479)

[4.3 Release Wave 11](#_Toc232859480)

[4.4 Display Wave Release Log and Warehouse Task (Optional) 12](#_Toc232859481)

[5 Appendix 14](#_Toc232859482)

[5.1 Process Integration 14](#_Toc232859483)

[5.1.1 Preceding Processes 14](#_Toc232859484)

[5.1.2 Succeeding Processes 14](#_Toc232859485)

[5.2 Wave Exception Handling 14](#_Toc232859486)

## Purpose

Overview

This scope item allows you to run and optimize the process of creating picking warehouse tasks by using wave management to extend the warehouse outbound process. The process starts with the creation of waves via the schedule background job report, which combines items from the outbound deliveries based on certain criteria. The Warehouse Clerk (EWM) releases the picking waves by using the warehouse monitor. The system determines the location for picking the stock and allocates the stock to the warehouse task. You can also check the log history of wave and warehouse tasks using the warehouse monitor.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Warehouse Clerk (EWM) | SAP_BR_WAREHOUSE_CLERK_EWM | Warehouse Office | SAP_BR_WAREHOUSE_CLERK_EWM |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| EWM Warehouse | 3350 | Warehouse |  |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 3BS – Warehouse Outbound Processing | This Scope Item has the same Business Conditions as listed in the same chapter of the test script Warehouse Outbound Processing (3BS). |

### Preliminary Steps

#### Maintain Wave Templates

Purpose

In this step, you create a wave template that defines the attributes of all the waves that are created from it. Wave templates allow the same wave attributes to be reused for different warehouse request items that comply with the same conditions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Maintain Wave Templates .If the Determine Work Area: Entry window appears, enter the following values:Warehouse Number: 3350Choose Apply (Enter). | The Application Jobs screen appears. |  |
| 3 | Create New Entry | On the Define Wave Template: Change screen, choose New Entries. |  |  |
| 4 | Create Template | On the New Entries: Details of Added Entries screen, make the following entries:Wave Template: <Wave Template Name>.Description: <Wave Template Description>Wave Type: ST01Wave Category: S1Release Method: ManualBin Denial: Leave Item in Wave (Release Wave Again Later)Choose Save.Choose Back. |  |  |
| 5 | Enter Wave Template Time Attributes | Select the row of the wave template created in the previous step.In the Dialog Structure, double-click Define Wave Template Time Attributes.On the Define Wave Template Time Attributes: Change screen, choose New Entries.On the New Entries: Details of Added Entries screen, enter the following values:Template Option: 1Cutoff Time: 08:00:00Release Time: 08:30:00Pkng Cmpl. Time: 10:30:00Packg Cmpl.Time: 11:10:00Stgg Cmpl. Time: 11:15:00Wave Cmpl. Time: 11:30:00Choose Next Entry. |  |  |
| 6 | Create 2nd Wave Template Time Attributes | Repeat the previous step with the following data:Template Option: 2Cutoff Time: 15:00:00Release Time: 15:30:00Pkng Cmpl. Time: 17:30:00Packg Cmpl.Time: 18:10:00Stgg Cmpl. Time: 18:15:00Wave Cmpl. Time: 18:30:00Choose Save. |  |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Schedule Background Job for Wave Generation](#unique_10) [page ] 8 | Warehouse Clerk (EWM) | Schedule Wave Creation (F7309) | Scheduled job has the status ‘Finished’ and the wave is created. |
| [Simulate Wave (Optional)](#unique_11) [page ] 9 | Warehouse Clerk (EWM) | Warehouse Monitor (/SCWM/MON) | Wave release is simulated with logs. |
| [Release Wave](#unique_12) [page ] 11 | Warehouse Clerk (EWM) | Warehouse Monitor (/SCWM/MON) | Waves are released. Warehouse orders and warehouse tasks are created. |
| [Display Wave Release Log and Warehouse Task (Optional)](#unique_13) [page ] 12 | Warehouse Clerk (EWM) | Warehouse Monitor (/SCWM/MON) | Wave release log and warehouse task / warehouse order are displayed. |

## Test Procedures

This section describes the test procedures for each process step that belongs to this scope item.

### Schedule Background Job for Wave Generation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to run application job for wave creation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Schedule Wave Creation (F7309) | The Application Jobs screen appears. |  |
| 3 | Create Job | On the Application Jobs screen, choose Create. |  |  |
| 4 | Select Template | On the New Job: Schedule Wave Creation screen, in the 1. Template Selection section, make the following entries:Job Template: Schedule Wave CreationJob Name: for example Job for Wave CreationChoose Step 2. |  |  |
| 5 | Enter Schedule Options | In the 2. Scheduling Options section, choose Start Immediately.You can define the start time and recurrence pattern of your own preference. For testing purpose, you can enter Start Immediately.Choose Step 3. |  |  |
| 6 | Enter Parameters | In the 3. Parameters section, make the following entries:Warehouse Number: <your warehouse number>Whse Req. Doc Cat.: Outbound Delivery Order (PDO)Wave Template: <The one created in Maintain Wave Templates step>Wave Template Option:<One of the options created in Maintain Wave Templates stepWave Completion Date:TodayDocument: Use value help to make the following entriesEqual to <Your ODO number>, or between <from ODO number> <to ODO number>Choose Schedule. | The Application Jobs screen appears. |  |
| 7 | Check Job Status | On the Application Jobs screen, the application job is created with status In Process. You can choose GO to refresh the list until the status turns to Finished. |  |  |

### Simulate Wave (Optional)

Purpose

You can simulate waves before releasing them. The simulation can be triggered in the warehouse management monitor using the methods Simulate Waves or Simulate Single Waves.

After the wave was simulated, you can perform other actions from the Wave Simulation: Results screen. You can view warehouse order creation information. By choosing Display Log, you can view the wave simulation log. You can also manually release waves from this screen.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launch Pad | Open the SAP Fiori Launch Pad with the Warehouse Clerk (EWM) role. | The SAP Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Warehouse Monitor (/SCWM/MON). | The Warehouse Monitor (/SCWM/MON) screen displays. |  |
| 3 | Enter Default Value | Enter the following default values on the Warehouse Management Monitor screen, if not done yet:Warehouse Number: 3350Choose Execute. | The Warehouse Management Monitor SAP screen displays. |  |
| 4 | Navigate to Select Wave Item Node | Expand Outbound > Documents and double-click on Wave Item. |  |  |
| 5 | Enter Document Number | On the /SCWM/SAPLWIP_WAVE dialog box, in the Wave Item section, enter the following value:Document number: <Your ODO number(s)>Choose Execute.Note down the wave number(s). | All wave items of the selected wave are now displayed in the lower (right) screen area.It makes sure that the all the waves and wave items relevant to your outbound delivery orders are displayed. |  |
| 6 | Navigate to Select Wave Node | Expand Outbound > Documents and double-click on Wave. |  |  |
| 7 | Enter Wave Number | On the /SCWM/SAPLWIP_WAVE dialogbox, enter the following value:Wave: <Your wave number(s)>Choose Execute. | One or several waves are displayed on the upper-right screen side. |  |
| 8 | Simulate Wave | Select the Wave(s) and choose More method > Simulate Single Waves or select the waves and choose More method > Simulate Waves.Note Waves can be simulated in the following ways:If you choose to simulate releasing multiple waves, the system creates warehouse orders for the warehouse tasks that were created for all the waves.You can also choose to simulate single waves. Even if you select multiple waves for this type of simulation, the system simulates the release of each individual wave and creates warehouse orders for the warehouse tasks that were created for each individual wave. | The system displays the wave, wave items, created warehouse orders and warehouse tasks on the Wave Simulation: Results screen. |  |

|  |
| --- |
| Note When there is not enough stock for a product, the system log might tell you that for some of the ordered items, a warehouse task couldn't be created. In this case, you need to make sure that the storage type, from which picking shall take place, is replenished. Once there is enough stock, you can release the wave and create a warehouse task as expected. |

### Release Wave

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release wave(s) manually in the warehouse management monitor.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launch Pad | Open the SAP Fiori Launch Pad with the Warehouse Clerk (EWM) role. | The SAP Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Warehouse Monitor (/SCWM/MON). | The Warehouse Monitor (/SCWM/MON) screen displays. |  |
| 3 | Enter Default Value | Enter the following default values on the Warehouse Management Monitor screen, if not done yet:Warehouse Number: 3350Choose Execute. | The Warehouse Management Monitor SAP screen displays. |  |
| 4 | Navigate to Wave Node | Expand Outbound > Documents and double-click on Wave. |  |  |
| 5 | Enter Wave Number | On the /SCWM/SAPLWIP_WAVE dialog box, enter the following value:Wave: <Your wave number(s)>Choose Execute. | One or several waves are displayed in the upper-right screen side. |  |
| 6 | Release Wave | Select your wave(s) and choose More method > Release Wave. | The system confirms that the warehouse tasks have been created for the wave(s) in a new screen Display Logs. |  |
| 7 | Choose Continue | Choose Continue (Enter) to close the step. |  |  |

|  |
| --- |
| Note Waves can be released in several other ways besides releasing manually in the warehouse management monitor. For example, waves be released immediately upon creation or released automatically on the release day and release time set in the wave template. You can choose the wave release strategy that serves best to your business needs in the wave template header when creating the wave templates.You can release waves multiple times. For example, you have released a wave, but the system can only create some of the required warehouse tasks since there isn't enough stock. You can release the wave again later when more stock is available. |

### Display Wave Release Log and Warehouse Task (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you display the wave release log and the warehouse tasks / orders created with wave release.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launch Pad | Open the SAP Fiori Launch Pad with the Warehouse Clerk (EWM) role. | The SAP Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Warehouse Monitor (/SCWM/MON). | The Warehouse Monitor (/SCWM/MON) screen displays. |  |
| 3 | Enter Default Value | Enter the following default values on the Warehouse Management Monitor screen, if not done yet:Warehouse Number: 3350Choose Execute. | The Warehouse Management Monitor SAP screen displays. |  |
| 4 | Navigate to Wave Node | Expand Outbound > Documents and double-click on Wave. |  |  |
| 5 | Enter Wave Number | On the /SCWM/SAPLWIP_WAVE dialog box, enter the following value:Wave: <Your wave number(s)>Choose Execute. | One or several waves are displayed in the upper-right screen side. |  |
| 6 | Display Release Log | Select one of the waves and choose More method > Display > Release Log. | The wave release log is displayed in a new window: Display Logs. |  |
| 7 | Choose Continue | Choose Continue (Enter) to close the Display Logs screen. |  |  |
| 8 | Display Warehouse Tasks and/or Warehouse Orders | Select one of the waves and choose Warehouse Task or Warehouse Order. | The created warehouse task(s) or warehouse order(s) are displayed. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can proceed this process.

| Process | Business Condition |
| --- | --- |
| 3BS – Warehouse Outbound Processing | This Scope Item has the same Business Conditions as listed in the same chapter of the Test Script Warehouse Outbound Processing (3BS). |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 3BS - Warehouse Outbound Processing | To complete the warehouse processing, proceed with the step Confirm Pick Warehouse Tasks in test script Warehouse Outbound Processing (3BS). |

### Wave Exception Handling

During wave release you may experience exceptions such as bin denial.

You can select one of the following actions when creating wave templates:

- Default: Leave an item in a wave and release the wave again later.
- Remove an item from a wave, but only if stock can be found in alternative source bins. That means the item are reassigned to another wave.
- Immediately create a warehouse task in the same wave.
- Remove an item from a wave, without considering whether stock can be found in alternative source bins. That means the item gets removed from the wave without reassignment. Bin denial isn't triggered when choosing this option. However, if there are open warehouse tasks for the current wave item, the item cannot be deleted from the wave.

|  |
| --- |
| Note You have to define your own exception code for bin denial to use the wave exception handling for bin denial. On how to define exception codes, please refer to [https://help.sap.com/docs/SAP_S4HANA_CLOUD/87f9b54f9c4f4e75aff0061860a6589a/e8a30c35c57f4391a22aa6102fa3be24.html](https://help.sap.com/docs/SAP_S4HANA_CLOUD/87f9b54f9c4f4e75aff0061860a6589a/e8a30c35c57f4391a22aa6102fa3be24.html). |

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
- see-also :: [[11-inventory-warehouse-and-transportation/sap-ewm-integration-outbound-processing-to-customer-2vk-ae-test-script]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6NH_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 22,812 chars in the whole document
