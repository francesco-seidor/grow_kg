---
id: 14-maintenance-service-and-projects/test-script-sap-s-4hana-cloud-public-edition-time-recording-1q4-ae-754
title: Test Script SAP S/4HANA Cloud Public Edition - Time Recording (1Q4_AE) (1Q4_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud 2608 test script for scope item 1Q4 Time Recording: Manage My Timesheet, optional approval, BAdIs, and time confirmation in closed periods."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/time-recording]
aliases: [1Q4_S4CLD2608_BPD_EN_AE]
keywords: [Time Recording, timesheet, timesheet approval, data entry profiles, closed period time confirmation, timesheet validation, work locations and task types, accounting objects, business roles, demo data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1Q4_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-754
topic: 14-maintenance-service-and-projects/time-recording
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Time Recording (1Q4_AE) (1Q4_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1Q4_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Time Recording** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Time Recording (1Q4_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232847412)

[2 Prerequisites 4](#_Toc232847413)

[2.1 System Access 4](#_Toc232847414)

[2.2 Roles 4](#_Toc232847415)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232847416)

[2.4 Business Conditions 5](#_Toc232847417)

[2.5 Preliminary Steps 6](#_Toc232847418)

[2.5.1 Maintain Data Entry Profiles 6](#_Toc232847419)

[2.5.2 (Optional) Configure Work Locations/Task Types 7](#_Toc232847420)

[2.5.3 (Optional) Override the Default Approval Process 8](#_Toc232847421)

[2.5.4 (Optional) Validate Timesheet Entries 8](#_Toc232847422)

[3 Overview Table 10](#_Toc232847423)

[4 Test Procedures 11](#_Toc232847424)

[4.1 Record Actual Working Time 11](#_Toc232847425)

[4.2 Approval of Working Times (Optional) 14](#_Toc232847426)

[5 Appendix 15](#_Toc232847427)

[5.1 Process Integration 15](#_Toc232847428)

[5.1.1 Preceding Processes 15](#_Toc232847429)

[6 Time confirmation in closed periods 16](#_Toc232847430)

## Purpose

Overview

Time recording in enterprise services facilitates work-time tracking for employees against WBS elements, cost centers, and internal orders. In a time entry sheet, all configured accounting objects are visible on a time recording screen. Nonbillable time can also be maintained for full time accountability.

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
| Employee | SAP_BR_EMPLOYEE |  |  |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company is created in your system during activation . The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Receiver Cost Center | 33101601 - Marketing |  |  |
| Sender Cost Center | 33101101 - Financials |  |  |
| Activity Type | 8 - ConsultingNote Cost rates are maintained for the following combination: Sender cost center 33101101 and activity Type 8. Make sure the sender cost center 33101101 is assigned to the user for whom timesheet is to be recorded. |  |  |
| Cost Rates | 800 EU | Refer to 1NT, Preliminary Steps, Maintain Cost Rates. |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNN | Create Activity Type and Activity Type Hierarchy - MDS |
| 3KW | Create CO Cost Rates - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 1NT - Project Control – Finance | A project must be created and released to be used as the accounting object for the time posting. |
| 35E - Project Control – Research and Development Projects | A project must be created and released to be used as the accounting object for the time posting. |
| 35F - Project Control – Capital Projects | A project must be created and released to be used as the accounting object for the time posting. |

### Preliminary Steps

#### Maintain Data Entry Profiles

Purpose

In this step, you can configure Accounting objects for the Timesheet.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, proceed with one of the following:

- Configure Your Solution:
    1. Log on to the SAP Fiori Launchpad in the SAP S/4HANA Cloud Public Edition system as Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).
    2. Navigate to Manage your Solution > Configure Your Solution.
    3. On the Configure Your Solution: Realize Phase screen, make the following entries:
        - Application Area: Human Resource
        - Sub Application Area: Timesheet
    4. Select the line items with the item name Define and Maintain Settings for Timesheet Application.
    5. Choose Maintain Data Entry Profiles, and then choose Configure.
- SAP Central Business Configuration:
    1. Log on to the project experience in SAP Central Business Configuration.
    2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain Data Entry Profiles.
    3. Choose Open Documentation for the found line item to see more details about this configuration activity.
    4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.

| Step | Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Maintain Data Entry Profile | Double-click the record.Choose the following different receivers from :Note Furthermore, you can use the Self Service Configuration UI Maintain Data Entry Profiles.To switch on or off the approval process by selecting or deselecting Aproval Required Checkbox. By default, approval is not required for internal employees.To enable recording information on work location process by selecting or deselecting Work Location Checkbox. By default, recording information on work location is not required for internal employees.The options Unstaffed Project and Overtime are not relevant for the Time Recording (1Q4) scope item.Choose Save. | Data Entry profile is saved. |  |

#### (Optional) Configure Work Locations/Task Types

Purpose

In this step, you can optionally define work locations/task types.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, proceed with one of the following:

- Configure Your Solution:
    1. Log on to the SAP Fiori Launchpad in the SAP S/4HANA Cloud Public Edition system as Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).
    2. Navigate to Manage your Solution > Configure Your Solution.
    3. On the Configure Your Solution: Realize Phase screen, make the following entries:
        - Application Area: Human Resource
        - Sub Application Area: Timesheet
    4. Select the line items with the item name Define and Maintain Settings for Timesheet Application.
    5. Go through the SSCUIs listed in the following table. Select each item and choose Configure.
- SAP Central Business Configuration:
    1. Log on to the project experience in SAP Central Business Configuration.
    2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the activities listed in the following table.
    3. Choose Open Documentation for the found line item to see more details about this configuration activity.
    4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.

| Configuration Item/SSCUI Title | Description | Configuration Item/SSCUI ID |
| --- | --- | --- |
| Maintain Work Locations | Defines work locations. | 102827 |
| Specify Task Types, Components and Levels | Specify Task Types | 101864 |

#### (Optional) Override the Default Approval Process

BAdI HCM: Timesheet Approver Determination (HCM_CATS_V1_APPROVER_DETRMN)

You can use this BAdI to determine the approver for each timesheet entry and the BAdI also enables you to auto approve the timesheet entry.

|  |
| --- |
| Note The Approval process needs to be switched on by selecting the Approval Required field in the Configuration Item/SSCUI Maintain Data Entry Profiles for data entry profile S4H_INT. |

Procedure

1. Log on to the SAP Fiori Launchpad in the SAP S/4HANA Cloud Public Edition system as Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).
2. Open the Extensibility Cockpit (F2866) app.
3. To create BAdI implementation, carry out the relevant steps from the topic in the guide to create and maintain custom logic that can be used to enhance applications.

|  |
| --- |
| Remember Select from Business Context= HCM:Timesheet Aprrover Determination. |

#### (Optional) Validate Timesheet Entries

BAdI HCM: Timesheet Validations (HCM_CATS_V1_TS_VALIDATION)

You can use this BAdI to perform the customer specific timesheet validations/checks when you save the timesheet entry.

|  |
| --- |
| NoteThe HCM: Timesheet Validations BAdI supports both warning and error messages.When error messages are enabled, you cannot record and submit time entries in the Manage My Timesheet app, after the error message is displayed.When warning messages are enabled, you can record and submit time in the Manage My Timesheet app, even after the warning message is displayed.The BAdI is implemented for a particular task, stipulating that the workforce can only enter 7 hours per day in the Manage My Timesheet app. If a particular employee records and submits time that exceeds 7 hours for a specific day, a warning message is displayed. The employee can still proceed to submit the excess hours. |

Procedure

1. Log on to the SAP Fiori Launchpad in the SAP S/4HANA Cloud Public Edition system as Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).
2. Open the Extensibility Cockpit (F2866) app.
3. To create BAdI implementation, carry out the relevant steps from the topic in the guide to create and maintain custom logic that can be used to enhance applications.

|  |
| --- |
| Remember Select from Business Context= HCM:Timesheet Validations. |

## Overview Table

This scope item consists of several process steps provided in the table below.

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Record Actual Working Time

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you perform the time recording process through the Manage My Timesheet (F1823) app.

Working time is entered directly by the employee and not with delegates. Besides the times, a short description or note can also be entered per day and tasks.

|  |
| --- |
| Note Cost rates are maintained for the following combination: Sender Cost Center 33101101 and Activity Type 8. Make sure the Sender Cost Center 33101101 is assigned to the user for who the timesheet is to be recorded. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to the SAP Fiori launchpad as the user for whom timesheet is to be recorded. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open the Manage My Timesheet (F1823) app. | The My Timesheet Overview screen displays.Non-project related task types, which are non-billable, are automatically prefilled in the My Tasks list for employees.The Self Service Configuration UI can be used to define non-project related task types.To employee who has multiple employments, the tasks within his active employment will be shown. In case there are multiple active employments, you can find Employment information in upper left. By pressing the employment link, a pop up screen Select Employment comes out for you to select the right employment for time recording. |  |
| 3 | Select Date Range | By default, the timesheet shows the current week.If you want to record times in a different week, select the date range line on the top of the screen under My Timesheet. | A calendar entry dialog box displays allowing you to choose the week you wish to display.The weekend days (Saturday and Sunday are shown in a different color).The Calendar Settings button allows you to set:Show Work Week Specify Task Types : Yes or No (if not, Saturday and Sunday are shown)Start Week From: (for example, Monday)Time Format : Clock notation (for example, 12:30) or Decimal notation (for example, 12.5) |  |
| 4 | Manage my tasks | In the right part of the screen, choose the Menu button, then open the list item Manage My Tasks. | My task list displays. |  |
| 5 | Create a task | In the lower right-hand corner, choose the Create Task button. | The New Task window displays. |  |
| 6 | Choose Accounting objects | Choose Accounting objects (for example: Receiver Cost Center Receiver Cost center 33101601 and an Activity Type (for example, 8 - Consulting ), then click Save.Note Activity type is mandatory for recording on cost centers, internal orders, and WBS element.A combination of different accounting objects is not possible. The timesheet app allows you to record time for the following accounting objects:- WBS Element: Maintain WBS Element and Activity Type to record time for the WBS Element.- Receiver Cost Center: Maintain Receiver Cost Center and Activity Type to record time for the Receiver Cost Center.- Internal Order: Maintain Internal Order and Activity Type to record time for the Internal Order. | The possible receivers can be defined using the Self Service Configuration UI Maintain Data Entry Profiles. |  |
| 7 | Record Working Time – create new time entry | Enter the working times per days, hours, and tasks.Choose a task from the list of the available tasks. To enter the working times, click on the number of hours you want to record.For example, if you want to record 5 hours, choose the cell just below the number 5 on the day on which you want to record the hours.Save your entry. | The new time entries are visualized on the days you have chosen as rectangular boxes.The height of each box fits the number of hours you have inserted.Each entry shows the task title descriptions and the number of hours recorded in hh : mm format.On save, the records are automatically approved and transferred to CO.NoteThe HCM_CATS_V1_APPROVER_DETRMN (Timesheet Approver Determination) BAdI can be used to override the default approval process.For details, see [(Optional) Override the Default Approval Process](#unique_9) [page ] 8 and [Approval of Working Times (Optional)](#unique_14) [page ] 14 .The HCM_CATS_V1_B_TS_VALIDATION (Timesheet Validation) BAdI can be used to provide checks before saving timesheet entries. For details, see [(Optional) Validate Timesheet Entries](#unique_10) [page ] 8. |  |
| 8 | Record working time – Create additional time entries | Repeat the previous step for any additional time entry you want to record taking into account the already existing entries.Save your entry. | The times are saved. |  |
| 9 | Record Working Time – modify existing entries | Choose an existing entry, and in the Details dialog box, adapt the Duration field by inserting the number of hours in hh : mm format.Save your entry. | The height of the time entry is adapted according to the new recorded hours. |  |
| 10 | Record Working Time – delete existing entries | Choose the Delete button that is on the cross icon on the top-right corner of an entry.Save your entry. | The selected entry disappears. |  |
| 11 | Enter a Work Location and/or Note for an ac-tivity (optional) | To enter an optional Work Location and/or Note for an activity, just choose the entry and scroll down to find the Details screen. In Work Location field, Choose F4 to select a proper Work Location.Enter a description in the Note field and save.Note Field length in the Note field is restricted to 300 chars. | A dialog box is displayed. The Details of the activity is saved.The possible Work Locations are maintained in SSCUI Maintain Work Locations. |  |

### Approval of Working Times (Optional)

Context

The recorded time of the employee in the previous steps do not need further approval as they are automatically approved by default.

Procedure

As described in [(Optional) Override the Default Approval Process](#unique_9) [page ] 8, the TimeSheet Approver Determination BAdI is used to override the default approval process. Using the BAdI, you can define the approvers and the time entries that are subject to approval (that is, the time recorded on WBS elements, cost centers, internal orders, non-project-related task types).

|  |
| --- |
| Note The business catalog SAP_HCM_BC_TS_WIAPPROVE_PC needs to be added to the role assigned to the approver determined by the BAdI, so that the approver can approve the entries through the My Inbox (F3328) app. |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

You may first have completed the following processes and conditions before you start with the test steps:

| Process | Business Description |
| --- | --- |
| Exception-Based Core HR with SAP SuccessFactors Employee Central- JB1 | This process should be run to have employee data replicated to SAP S/4HANA. |
| Project Control – Finance - 1NT | A project must be created and released to be used as the accounting object for the time posting. |
| Internal Order – Actual - BEV | An Internal Order must be created and released to be used as the accounting object for the time posting. |
| Project Control – Research and Development Projects - 35E | A project must be created and released to be used as the accounting object for the time posting. |
| Project Control – Capital Projects - 35F | A project must be created and released to be used as the accounting object for the time posting. |

## Time confirmation in closed periods

Purpose

In case a consultant records time in a closed financial accounting period, the time confirmations are still saved to ensure a correct utilization reporting and a correct con-firmation date on the billing document. However, the transfer of the timesheet documents to accounting fails. The failed documents are stored in an operation que and an error log is created. As a result, you need to transfer the failed time recordings to controlling with a posting date in an open period.

For example:

- The consultant enters his time on March 26 for February 7, with February being a closed financial period.
- An accountant can post this confirmation in the next open period by providing a posting date, for example March 1.
- This will create a journal entry with:
    - Document date March 26
    - Posting date March 1
    - Service rendered date February 7

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as an Overhead Accountant | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Process Unposted Time Confirmations. | CATS: Transfer to Controlling app is opened. |  |
| 3 | Find out the Time Record-ings in closed periods | Choose “Test Run” and click on “Execute”.Memorize the Employee ID, Date, or Document Number for which you want to correct the CO postings (e.g.: Employee ID Employee), then go back to CATS: Transfer to Controlling. | A list of a list of records containing errors (and also time recordings in closed periods) is displayed.Memorize the time recordings in closed periods which you want to transfer to controlling. |  |
| 4 | Transfer Time Recording to Controlling | Enter the memorized Selection Parameters (e.g.: Insert Employee as Employee ID) as well as a posting date in an open period.Deselect Test Run and click on Execute | All applicable time entries will result in journal entries (e.g. all time recordings of Employee).A journal entry will be created including the field “service rendered date”, for which the consultant entered the confirmation. The service rendered date is stored in the journal entry and forwarded to Time and Material billing. With the service ren-dered date the cost rate is derived. |  |

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
> Flagged while digesting this document, not verified: Validation BAdI is named HCM_CATS_V1_TS_VALIDATION in the preliminary steps but HCM_CATS_V1_B_TS_VALIDATION in the test step 7 note.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/test-script-time-recording-project-based-services-j12-ae-1297]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1Q4_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 25,715 chars in the whole document
