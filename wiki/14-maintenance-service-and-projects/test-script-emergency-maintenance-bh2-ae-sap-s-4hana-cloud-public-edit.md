---
id: 14-maintenance-service-and-projects/test-script-emergency-maintenance-bh2-ae-sap-s-4hana-cloud-public-edit
title: "Test Script: Emergency Maintenance (BH2_AE) - SAP S/4HANA Cloud Public Edition (BH2_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item Emergency Maintenance (BH2): report, repair, goods issue, complete malfunction, review object page."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/corrective-and-emergency-maintenance]
aliases: [BH2_S4CLD2608_BPD_EN_AE]
keywords: [Corrective and Emergency Maintenance, emergency maintenance, malfunction reports, repair malfunction, post goods issue, complete malfunction report, asset maintenance object page, initial material stock, business roles, test data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BH2_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1267
topic: 14-maintenance-service-and-projects/corrective-and-emergency-maintenance
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Emergency Maintenance (BH2_AE) - SAP S/4HANA Cloud Public Edition (BH2_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BH2_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Corrective and Emergency Maintenance** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Emergency Maintenance (BH2_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232861641)

[2 Prerequisites 4](#_Toc232861642)

[2.1 System Access 4](#_Toc232861643)

[2.2 Roles 4](#_Toc232861644)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232861645)

[2.4 Business Conditions 5](#_Toc232861646)

[2.5 Preliminary Steps 6](#_Toc232861647)

[2.5.1 Initializing Material Stock 6](#_Toc232861648)

[3 Overview Table 8](#_Toc232861649)

[4 Test Procedures 9](#_Toc232861650)

[4.1 Report Malfunction 9](#_Toc232861651)

[4.2 Repair Malfunction 10](#_Toc232861652)

[4.3 Post Goods Issue 12](#_Toc232861653)

[4.4 Complete Malfunction Report 13](#_Toc232861654)

[4.5 Review Asset Maintenance Object Page 15](#_Toc232861655)

[5 Appendix 17](#_Toc232861656)

[5.1 Process Integration 17](#_Toc232861657)

[5.1.1 Preceding Processes 17](#_Toc232861658)

[5.1.2 Succeeding Processes 17](#_Toc232861659)

[5.2 Additional Features 17](#_Toc232861660)

## Purpose

Overview

This scope item uses order recording after an event to log unforeseen and urgent maintenance work by creating and confirming an order in the same operation. The technician can identify an issue affecting a piece of equipment, immediately fix the issue, and later report the time spent and the material consumed. The technician can enter required data quickly. It can then be used for planning objects (such as maintenance orders) and for actual recording (order confirmation, notification data, and goods movements). Planned data does not differ from the actual data, which is the work recorded on an operation corresponding to the confirmed actual work. The order is created, released, and if required, technically completed. In addition, you can install, dismantle, or replace pieces of equipment.

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
| Maintenance Planner | SAP_BR_MAINTENANCE_PLANNER | Maintenance Planning | SAP_BR_MAINTENANCE_PLANNER |  |
| Maintenance Technician | SAP_BR_MAINTENANCE_TECHNICIAN | Maintenance Execution | SAP_BR_MAINTENANCE_TECHNICIAN |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. You can also use the following sample data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Equipment | 233100091 | Cooling Water Circulation Pump |  |
| Spare Parts Material | SP001 | Bearing |  |
| Spare Parts Material | SP002 | Coupling |  |
| Spare Parts Material | SP003 | Shaft |  |
| Spare Parts Material | SP004 | Gaskets 1mm |  |
| Spare Parts Material | SP005 | Mechanical Seal |  |
| Spare Parts Material | SP006 | Spur gear IS651 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331B | Std. storage 2 |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS(BNZ) master data script. Posting Period is up to date. |

### Preliminary Steps

#### Initializing Material Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In a real business case, the materials are usually purchased from external suppliers. In this case, the process is covered by the standard purchasing or subcontracting processes. This process step shows you how to post initial stock directly to the storage locations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Input Material | Make the following entries and choose Enter:Material: < material number>. Select one of the Spare Parts Material mentioned in the previous section Master Data, Organizational Data, and Other Data.Plant: Plant 1 AE (3310) |  |  |
| 4 | Select Stock | Select the icon beside the stock that you want to add initial stock, for example:Storage Location: Std. storage 2 (331B)Unrestricted-Use Stock | A dialog box opens. The Storage Location, Stock Type and Current Quantity display according to your entries in the previous steps. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Document Date: <today>Posting Date: <today>Stock Change: initial entryQuantity: <quantity number> | The system displays Material document XXX created. The stock has been added. |  |

## Overview Table

The scope item Emergency Maintenance (BH2) consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Report Malfunction](#unique_9) [page ] 9 | Maintenance Technician | Report Malfunction (F2023) | Unplanned job is created. |
| [Repair Malfunction](#unique_10) [page ] 10 | Maintenance Technician | Repair Malfunction | Unplanned job is confirmed incl. time recording, con-firming material used. |
| [Post Goods Issue](#unique_11) [page ] 12 | Warehouse Clerk | Post Goods Movement (MIGO) | Spare parts are consumed. |
| [Complete Malfunction Report](#unique_12) [page ] 13 | Maintenance Technician | Manage Malfunction Reports (F2023) |  |
| [Review Asset Maintenance Object Page](#unique_13) [page ] 15 | Maintenance Planner |  |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Report Malfunction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After Event recording or confirm unplanned job suites the purpose that an event has occurred which requires quick and immediate intervention from the maintenance technician. In such an emergency, the maintenance technician performs the required maintenance activity to restore the condition of the equipment. Maintenance technician identifies an issue at a piece of equipment, immediately fixes the issue and reports later the time spent and the material consumed. In most cases, he is not able to identify the equipment number and searches along the hierarchy of the Functional Location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Maintenance Technician. | The SAP Fiori launchpad displays. |  |
| 2. | Access the App | Open Report Malfunction (F2023). | The Create Malfunction Report screen displays. |  |
| 3 | Report Malfunction | On the Create Malfunction Report screen, make the following entries:Technical Object: 233100091Note You can also search for an object by plain text. Use the value help button and provide a keyword, such as <water pump>. In the result list, select the equipment with number 233100091, a description of Cooling Water Circulation Pump, and Maintenance Planning Plant 3310. To see all details regarding technical objects, use the app Find Technical Objects. There you can search either by plain text in Search field or by applying different filters.Description: <Describe the unforeseen event>Effect: For example, <Production restricted (2)>.If default report time need to be adjusted, make the following entries:Reported on: <Date><Time>Choose Save.Please note down the Order Number as well as the Notification Number for following test. | Order 4XXXXXX saved with notification 1XXXXXXX. |  |
| 4 | Add Attachment/URL (Optional) | In the Attachments area, Choose Upload and select JPG or PNG file to upload. | Picture or photo is uploaded to your notification. |  |

### Repair Malfunction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After event recording suites the purpose that an event has occurred which requires quick and immediate intervention from the maintenance technician. In such an emergency, the maintenance technician performs the required maintenance activity to restore the condition of the equipment. The maintenance technician identifies an issue at a piece of equipment, immediately fixes the issue and reports later the time spent and the material consumed. Very often he is not able to identify the equipment number and searches along the hierarchy of the functional location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Repair Malfunctions. | The Manage Maintenance Jobs screen displays.This app can be used to show the user’s work items only. |  |
| 3 | Search for Malfunction Report | On the Manage Maintenance Jobs screen, choose filter and make the following entries:Jobs: Mine onlyTechnical Object: 233100091Choose Go. | Malfuntion Report list in the Manage Maintenance Jobs screen. |  |
| 4 | Choose Malfunction Report number | Choose the line of the Malfunction Report from the previous section. | Navigate to Process Malfunction Report Screen. |  |
| 5 | Add Work Items | On the Process Malfunction Report screen. Go to Job Details Section.In the Work area, choose the Edit button.In the Edit Work Item pop-up dialog box, make the following entries:Work Center: RES-0100Planned Effort: For example: <1 Hour>Choose Save. |  |  |
| 6 | Add Spare parts used | On the Process Malfunction Report screen. Go to Job Details Section.In the Parts area, choose Add button.On the select parts screen, in the Bill of Material tab, select Material SP001.Quantity: For example: <1 pc>Choose Add then choose back button on the top left corner.Note Check material availability in the column In Stock; If the material shows Not Available in that column, you can create initial material stock according to Preliminary Steps in the previous chapter. | Item SP001 has been added to your report. |  |
| 7 | Release Malfunction Report | On the Process Malfunction Report screen, choose Release button at the floating toolbar. The work item status is changed to Ready for Work. | The status of Malfunction Report changed from Created to Released. |  |
| 8 | Start work | On the Process Malfunction Report screen, in the Job Details section choose In Process from the dropdown list for overall status at the work item level.Note the exact time when you choose In Process. | The status of malfunction report changed to In Process. |  |
| 9 | Process Maintenance Job offline | Wait for few minutes.For example: 5-6 minutes | This step is not related with operation in system. It simulates in real business scenario that a technician has several minutes of preparation. |  |
| 10 | Pause Work | On the Process Malfunction Report screen, choose Work Paused at the work item level. Choose Waiting for Parts in Select Reason dialog box.Choose OK. |  |  |
| 11 | Partial Confirmation | In Pause Work dialog box, choose checkbox Create partial time confirmation, and check the system proposed Actual Work hour automatically.Choose OK. | Actual work is 0.1 hours if you wait 6 minutes after choosing status In Process. |  |
| 12 | Restart Work | On the Process Malfunction Report screen, choose In Process at the work item level. |  |  |
| 13 | Mark Work is Done | On the Process Malfunction Report screen, choose Work is done at the work item level. |  |  |
| 14 | Edit Work Item | On the Process Malfunction Report screen, go to Job Details section.In the Work area, choose Record Time.On the Confirm Actual Effort dialog box, make the following entries:Additional Effort: 0.8 HoursPosting Date: Keep the default dateFinal Confirmation: Select this checkboxChoose Save. | Actual Effort is proposed automatically by system. |  |

### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The material which is actually consumed will be posted by Warehouse Clerk.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Post Goods Movement screen displays. |  |
| 3 | Choose Goods Issue-Order | Choose Goods Issue-Order. |  |  |
| 4 | Specify Order Number | Enter the Maintenance Order Number which created at the previous step, and choose Execute. | The General Information of this order displays. |  |
| 5 | Specify Quantity | In Quantity tab, enter quantity of spare parts, for example, <1 PC> |  |  |
| 6 | Select Item Ok | Choose Item OK. |  |  |
| 7 | Check | Choose Check. |  |  |
| 8 | Post | Choose Post. | Material document XXX posted. |  |

### Complete Malfunction Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Maintenance technician record the damage details, causes and activity code for future analysis. After that, technician will set this malfunction report as complete and close it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Malfunction Reports (F2023). | The Manage Malfunction Reports screen displays. |  |
| 3 | Search for Malfunction Report | On the Manage Malfunction Reports screen, choose filter and make the following entries:Notification Type: M2, Malfunction ReportTech. Object: 233100091Status: Work is doneChoose Go. |  |  |
| 4 | Choose Malfunction Report Number | Choose the line of the Malfunction Report from the previous section. | Navigate to Process Malfunction Report screen. |  |
| 5 | Enter Malfunction Details | On the Process Malfunction Report screen. Go to Malfunction Details section.In the Item area, choose Add button.In the Add Malfunction Details dialog box, make the following entries:Object Part: ME01 BearingDamage: for example, Bearing damageChoose Save. |  |  |
| 6 | Edit Malfunction Details | On the Process Malfunction Report screen, go to Malfunction Details section.In the Item area, choose Edit button at the line of you added at previous step.In the Edit Malfunction Details dialog box, make the following entries:Select Cause tab: for example: ME02 Corrosion.Check the Root Cause indicator.Select Activity tab: for example: ME00 Part replaced.Choose Save. |  |  |
| 7 | Mark Breakdown Indicator | On the Process Malfunction Report screen, go to Malfunction Duration section, choose Edit;In the Malfunction Duration dialog box, check Breakdown indicator and choose Save. |  |  |
| 8 | Complete Malfunction Report | On the Process Malfunction Report screen, choose Complete button at the floating toolbar. |  |  |
| 9 | Close Malfunction Report | On the Process Malfunction Report screen, choose Close Report button on the floating toolbar. |  |  |

### Review Asset Maintenance Object Page

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the different objects pages available for different roles in the area of Asset Management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner.Note You can use any of the maintenance roles from the sections above. | The SAP Fiori launchpad displays. |  |
| 2 | Start Search | Choose Search in the upper right area of the launchpad. | An input field displays. |  |
| 3 | Search Criteria | In the dropdown list, choose Equipment and input Equipment, for example, 233100091. |  |  |
| 4 | Tailor the Result Display | Below the search line, choose a symbol (for example, filter, display as table, sort, and so on) to filter the results list. | The results list is filtered according to your selections. |  |
| 5 | Review Object Page | Review overview information for Equipment via Object page. |  |  |
| 6 | Repeat Steps | Repeat steps 1 to 5 for any other role in this test script and any other object offered in the search function.For example:NotificationOrderOrder Confirmation | The list of objects offered for search differs by the role you used to log on. |  |

## Appendix

### Process Integration

#### Preceding Processes

You may first have completed the following processes and conditions before you start with the test steps:

| Process | Business Condition |
| --- | --- |
| MDS: Create New Open MM Posting Period - MDS | ScopeItem_BusinessCondition |
|  |  |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| BF7-Period-End Closing – Maintenance Orders | A maintenance order technically completed as part of Emergency Maintenance |

### Additional Features

After completing the activities in this test script, you can also continue testing the Fiori App: Technical Object Breakdowns. You can log on system as business role: Maintenance Planner and find this app in tile EAM - Asset Information System. The test results (one or several maintenance orders for technical objects) which you created in this test script can be the sample data for Technical Object Breakdowns app to display graphical analysis.

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
- related-to :: [[14-maintenance-service-and-projects/reactive-maintenance-4hh-ae-test-script-sap-s-4hana-cloud-public-editi]]
- related-to :: [[14-maintenance-service-and-projects/test-script-corrective-maintenance-bh1-ae-sap-s-4hana-cloud-public-edi]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BH2_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 25,701 chars in the whole document
