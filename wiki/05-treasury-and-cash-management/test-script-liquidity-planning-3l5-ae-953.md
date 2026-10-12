---
id: 05-treasury-and-cash-management/test-script-liquidity-planning-3l5-ae-953
title: "Test Script: Liquidity Planning (3L5_AE) (3L5_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud 2608 test script 3L5_AE: configure and schedule financial plan data jobs importing cash flows from SAP Analytics Cloud for liquidity planning."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/liquidity-planning]
aliases: [3L5_S4CLD2608_BPD_EN_AE]
keywords: [Liquidity Planning, sap analytics cloud integration, financial plan data jobs, plan data mapping, cash flow analysis, cash management, communication arrangement, succeeding processes, 3L5]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3L5_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-953
topic: 05-treasury-and-cash-management/liquidity-planning
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Liquidity Planning (3L5_AE) (3L5_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3L5_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Liquidity Planning** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Liquidity Planning (3L5_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232853142)

[2 Prerequisites 3](#_Toc232853143)

[2.1 Additional Manual Configuration 3](#_Toc232853144)

[2.2 System Access 3](#_Toc232853145)

[2.3 Roles 3](#_Toc232853146)

[2.4 Master Data, Organizational Data, and Other Data 4](#_Toc232853147)

[3 Overview Table 5](#_Toc232853148)

[4 Test Procedures 6](#_Toc232853149)

[4.1 Manage Financial Plan Data Jobs for SAP Analytics Cloud Integration 6](#_Toc232853150)

[4.2 Schedule Financial Plan Data Jobs for SAP Analytics Cloud Integration 9](#_Toc232853151)

[5 Appendix 12](#_Toc232853152)

[5.1 Succeeding Processes 12](#_Toc232853153)

## Purpose

Overview

The scope item supports the liquidity planning by supplying the planning tool with historical/actual and short-term/mid-term forecast cash flow data, based on which the end user can draw up the long-term plan of the liquidity trend.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/216803a1a98681f6396cc3c00b6ed8ed)

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log on |
| --- | --- | --- | --- | --- |
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |

### Master Data, Organizational Data, and Other Data

Default Values

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. These master data represent materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

The business process is enabled with this organization-specific master data, examples are provided in the next section.

Operational Focus

SAP Best Practices delivers standard values for more than one operational focus area, such as Services, Manufacturing, or Trade. This means that you may find more than one master data table below. Use the master data that matches the operational focus of your company (Services, Manufacturing, or Trade).

|  |
| --- |
| Note Additional Default ValuesYou can test the scope item with other SAP Best Practices default values that have the same characteristics.Check your SAP ECC system to find out which other material master data exists. |

|  |
| --- |
| Note Using Your Own Master DataYou can also use customized values for any material or organizational data for which you have created master data. For more information on how to create master data, see the Master Data Procedures documentation. |

Use the following master data in the process steps described in this document:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  | Company code |

## Overview Table

This scope item consists of several process steps provided in the following tables.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Manage Financial Plan Data Jobs for SAP Analytics Cloud Integration](#unique_8) [page ] 6 | Cash Management Specialist | Manage Financial Plan Data Jobs - for SAP Analytics Cloud Integration (SAC_INT_PULL) | The tenant ID and configuration ID are defined for plan data. |
| [Schedule Financial Plan Data Jobs for SAP Analytics Cloud Integration](#unique_9) [page ] 9 | Cash Management Specialist | Schedule Financial Plan Data Jobs - for SAP Analytics Cloud Integration (F7902) | The cash flows are imported from SAP Analytics Cloud. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Manage Financial Plan Data Jobs for SAP Analytics Cloud Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you prepare the SAP S/4HANA Cloud Public Edition system for the required integration by defining transformation rules and creating the Configuration ID for Financial Plan Data configuration object.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Plan Data Jobs - for SAP Analytics Cloud Integration (SAC_INT_PULL). | The Tenant ID for Financial Plan Data: Change view displays. |  |
| 3 | Define Tenant ID for Plan Data | Choose New Entries, and enter the following data:Tenant ID for Plan Data: for example, LiquidityPlanning_SACCommunication Arrangement: <the communication arrangement for scenario SAP_COM_0443>Note The communication scenario, communication system and result URL are automatically derived according to the communication arrangement. |  |  |
| 4 | Save Tenant ID | Choose Save. | The tenant ID is created for plan data. |  |
| 5 | Define Configuration ID for Plan Data | In the left Dialog Structure, choose Configuration ID for Financial Plan.Choose New Entries, and enter the following data:Configuration ID for Import: for example, CON_LIQUIDITYPLANDescription: for example, Configuration ID for LiquidityPlanning WBActive: <selected>Target Type: FQM_FLOWTenant ID for Plan Data: <Tenant ID created in above step>, for example, LiquidityPlanning_SACProvider ID for Plan Data: <the technical ID for the Modeler of SAC>, for example, C33MWS9IZOSUJK3CSS9OAGULFKNoteYou can use any SAP Analytics Cloud model. Examples for a typical model for integrating Liquidity Planning: Liquidity Planning model (SAP__FI_CLM_IM_LIQUIDITY_PLAN)You need to access the SAP Analytics Cloud tenant to find the technical ID of the SAP Analytics Cloud model.Package Size: for example, 50000 |  |  |
| 6 | Save Configuration ID | Choose Save. | The Configuration ID is created for plan data. |  |
| 7 | Define Mapping of Plan Data | In the left Dialog Structure, choose Mapping of Financial Plan Data.Choose New Entries, for example, and enter the following data:Table 1: Mapping of Dimension FieldsSAP S/4HANA Cloud Public Edition FieldIn ScopeMapping TypeSource FieldField AttributeFixed ValueCommentAMOUNTField MappingAMOUNTThe Amount field is mandatory when you write back.Please ensure all the flows you write back is not zero, otherwise this flow will be skipped.CURRENCYField MappingCURRENCYOnly transaction currency is supported when you write back.COMPANY_CODEXField MappingSAP_ALL_COMPANY_CODECompany code field is mandatory when you write back.LIQUIDITY_ITEMField MappingSAP_CLM_LIQUIDITY_ITEMMake sure liquidity item is valid.MEMO_RECORD_TYPEXAttribute MappingVersionMEMO_RECORD_TYPEMemo Record Type field is mandatory when you write back to FQM_FLOW.Two default memo record types are delivered:WD is for Planned Item Category and WA is for Payment Advice Category.PLANNING_GROUPFixed ValueWDMake sure planning group is valid.TRANSACTION_DATEXAttribute MappingDateDateTransaction date field is mandatory when you write back.When you write back, ensure the date written back should feature format YYYY-MM-DD, on a daily basis.NoteYou can use above fields from FCLM_SAC_STAGING table of SAP S/4HANA Cloud Public Edition system to export data.Please be aware that COMPANY_CODE, TRANSACTION_DATE, MEMO_RECORD_TYPE, AMOUNT, CURRENCY are the minimal fields to export data. In other words, the model that you try to write back should have mapping relationship of these fields.In Scope: The plan data scope (or deletion scope) defines the plan data record is reversed (overwritten) by the new plan data record which comes from the source model. |  |  |
| 8 | Define Filter Settings for Plan Data | In the left Dialog Structure, choose Filter Settings for Financial Plan Data.Choose New Entries, and enter the following data:Source Field: for example, VersionOption: for example, EqualFixed Value: for example, public.Forecast6_SATNoteIf you set a constant mapping for memo_record_type, it’d better to set version as filter, then one version can be related with one memo record type.You can also create filter for company code, date, and so on. | The tenant ID is created for plan data. |  |
| 9 | Save | Choose Save. | The mapping and filter settings are created for plan data. |  |

### Schedule Financial Plan Data Jobs for SAP Analytics Cloud Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can trigger integration process as a background job.

|  |
| --- |
| Note To specify which configuration must be executed, you need to provide mandatory parameter Configuration ID for Import on previous step, which must be created upfront in the Schedule Financial Plan Data Jobs - for SAP Analytics Cloud Integration (F7902) app. |

|  |
| --- |
| Note The relevant value for the source fields (for example, company code, liquidity items) should exist in SAP S/4HANA Cloud Public Edition system before you schedule plan data jobs for SAP Analytics Cloud Integration. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Financial Plan Data Jobs - for SAP Analytics Cloud Integration (F7902). | The Schedule Financial Plan Data Jobs for SAP Analytics Cloud Integration screen displays. |  |
| 3 | Create a New Application Job | On the current view, choose Create to create an application job. | The New Job: Schedule Financial Plan Data Jobs for SAP Analytics Cloud Integration screen displays. |  |
| 4 | Choose Job Template | In the Template Selection section, enter the following data:Job Template: Schedule Financial Plan Data Jobs for SAP Analytics Cloud IntegrationJob Name: for example, Schedule Financial Plan Data Jobs for SAP Analytics Cloud Integration |  |  |
| 5 | Maintain Scheduling Options | Choose Step 2.In the Scheduling Options section, enter the following data:Start Immediately: <Selected or deselected>Note If you choose start immediately, you don't need to maintain other parameters.Start: <current time or any future time as needed>Time Zone: <time zone>For Recurrence Pattern, choose Define Recurrence Pattern.In the Scheduling Information dialog box, the additional scheduling options are available.Recurrence Pattern: for example, WeeklyEvery: for example, 1On: for example, MondayEnd: <Optional>On Non-Working Day: <Optional>Calendar: for example, Germany(Standard)Choose OK. | If you would like to run this job immediately, you need to select the Start Immediately checkbox.If you would schedule this job at a specific time, you need to define the Start and Time Zone fields. |  |
| 6 | Maintain Parameter | Choose Step 3.In the Parameter section, enter the following data:Configuration ID for Import: <the configuration ID created in the previous step>, for example, CON_LIQUIDITYPLANTest: <as needed> | Parameters are maintained. |  |
| 7 | Check | Choose Check. |  |  |
| 8 | Run this Application Job | Choose Schedule to run this application job.Choose Yes to confirm the dialog box. |  |  |
| 9 | Check Application Jobs Log | Choose Go to update the job status. When the job status changes to Finished, choose Log to navigate to the job log. | Job log displays.Note If the job is executed successfully, the cash flows will be imported from SAP Analytics Cloud with planning Level WD or WA. Two default memo record types are delivered:WD is for Planned Item Category and WA is for Payment Advice Category.You can check the cash flows via Cash Flow Analyzer (F2332) app.If error message occurs, you can use App Display Cash Management Logs (F4991) and solve the issue. |  |
| 10 | Check Cash Flows | Open Cash Flow Analyzer (F2332) to check the cash flows imported from SAP Analytics Cloud. |  |  |

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following test scripts:

| Process | Business Condition |
| --- | --- |
| Advanced Cash Operations (J78) | Review the cash flow items you imported by executing the Cash Flow Analyzer procedure in this test script. |

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
- see-also :: [[05-treasury-and-cash-management/test-script-intercompany-process-for-cash-concentration-2u8-ae-869]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3L5_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 18,089 chars in the whole document
