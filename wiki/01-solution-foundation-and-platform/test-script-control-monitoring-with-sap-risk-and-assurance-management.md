---
id: 01-solution-foundation-and-platform/test-script-control-monitoring-with-sap-risk-and-assurance-management
title: "Test Script: Control Monitoring with SAP Risk and Assurance Management (3KY) (3KY_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 3KY: automated procedures, controls, work packages, run results and issues in SAP Risk and Assurance Management."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/governance-risk-and-control-monitoring]
aliases: [3KY_S4CLD2608_BPD_EN_XX]
keywords: ["Risk, Control and Privacy Monitoring (SAP Risk and…", control monitoring, automated procedures, controls, work packages, procedure run results, issue management, risk and assurance management, test scripts, odata services]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3KY_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-951
topic: 01-solution-foundation-and-platform/governance-risk-and-control-monitoring
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Control Monitoring with SAP Risk and Assurance Management (3KY) (3KY_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3KY_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Risk, Control and Privacy Monitoring (SAP Risk and Assurance Management)** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Control Monitoring with SAP Risk and Assurance Management (3KY) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232836346)

[2 Use Cases 3](#_Toc232836347)

[3 Prerequisites 4](#_Toc232836348)

[3.1 Additional Manual Configuration 4](#_Toc232836349)

[3.2 System Access 4](#_Toc232836350)

[3.3 Roles 4](#_Toc232836351)

[3.4 Master Data, Organizational Data, and Other Data 5](#_Toc232836352)

[3.5 Business Conditions 5](#_Toc232836353)

[4 Overview Table 6](#_Toc232836354)

[5 Test Procedures 7](#_Toc232836355)

[5.1 Create Automated Procedure 7](#_Toc232836356)

[5.1.1 Option One: Adjust and Activate Pre-delivered Automated Procedure 7](#_Toc232836357)

[5.1.2 Option Two: Create Your Own Automated Procedure 8](#_Toc232836358)

[5.2 Create Control and Assign Automated Procedure 10](#_Toc232836359)

[5.3 Create Work Package and Assign Control 11](#_Toc232836360)

[5.4 Display Procedure Run Results 13](#_Toc232836361)

[5.5 Manage Issues 14](#_Toc232836362)

## Purpose

Overview

With SAP Risk and Assurance Management, the compliance manager defines controls and procedures to monitor operational processes and detect anomalies when connected to the SAP S/4HANA Cloud Public Edition system.

Operational processes generate many documents on a daily basis. This scope item enables continuous monitoring of transaction information and detects activities that may cause a financial loss, reputational damage, or other negative consequences for your organization. The results from these monitored processes provide insights regarding the operational processes within a company.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Use Cases

SAP Risk and Assurance Management provides pre-defined business content, such as controls, automated procedures. They can be used as a quick start of your business as well as for demo and education purpose. The content is automatically delivered to your SAP Risk and Assurance Management system after you've successfully subscribed SAP Risk and Assurance Management in SAP Business Technology Platform (SAP BTP).

For more information on the pre-defined business content, please refer the document Business Content in [SAP Risk and Assurance Management Help Portal](https://help.sap.com/ram).

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/8aaaa5451f060285b03b1a68d4a3e6a1)

### System Access

| System | Details |
| --- | --- |
| SAP Risk and Assurance Management | Accessible via the SAP Risk and Assurance Management Fiori launchpad. Your system administrator provides you the logon information to access the system. |

### Roles

Below Role Templates are in SAP Risk and Assurance Management:

| Name | Description | ID | Log On |
| --- | --- | --- | --- |
| Compliance Specialist |  | Compliance_Specialist | Please ask your system administrator to assign to the tester. |
| Compliance Manager |  | Compliance_Manager | Please ask your system administrator to assign to the tester. |

For more information, please refer to the chapter User and Authorization Management of the Administration Guide for [SAP Risk and Assurance Management Help Portal](https://help.sap.com/ram).

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represent materials, business partners, depending on the operational focus of your company.

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| J58- Accounting and Financial Close | Make sure J58 is activated before performing test procedures described in this test script, because Post General Journal Entries contained in J58 is required for successful execution of this test script as in the demo case we are monitoring the general journals posted to the prior fiscal period. |

## Overview Table

This scope item consists of several process steps provided in the table below.

| Process Step | Business Role | System | App/Transaction | Expected Results |
| --- | --- | --- | --- | --- |
| [Option One: Adjust and Activate Pre-delivered Automated Procedure](#unique_10) [page ] 7 | Compliance Specialist | SAP Risk and Assurance Management | Manage Automated Procedures | Automated Procedure is activated. |
| [Option Two: Create Your Own Automated Procedure](#unique_11) [page ] 8 | Compliance Specialist | SAP Risk and Assurance Management | Manage Automated Procedures | Automated Procedure is created and activated. |
| [Create Control and Assign Automated Procedure](#unique_12) [page ] 10 | Compliance Manager | SAP Risk and Assurance Management | Manage Controls | Controls with Automated Procedures assigned is created. |
| [Create Work Package and Assign Control](#unique_13) [page ] 11 | Compliance Manager | SAP Risk and Assurance Management | Manage Work Packages | Work Package with Controls/ Automated Procedures is created. |
| [Display Procedure Run Results](#unique_14) [page ] 13 | Compliance Manager | SAP Risk and Assurance Management | Display Automated Procedure Runs | Procedure Run results shows correctly. |
| [Manage Issues](#unique_15) | Compliance Specialist | SAP Risk and Assurance Management | Process Issues | Issues identified from Automated Procedure Runs created correctly. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Automated Procedure

#### Option One: Adjust and Activate Pre-delivered Automated Procedure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity is to adjust and activate pre-delivered Automated Procedure (AP) to retrieve data in S/4HANA.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Risk and Assurance Management as Compliance Specialist. | SAP Risk and Assurance Management Launchpad is displayed. |  |
| 2 | Access Manage Automated Procedures | Open Manage Automated Procedures tile. | The Manage Automated Procedures screen is displayed. |  |
| 3 | Adjust and Activate Pre-delivered Automated Procedure | Select a pre-delivered Automated Procedure. For example, General Journals Posted to the Prior Fiscal Period, and drill down to the detail page.Choose Edit at the right top of the page.In the Destination section, choose Add to add the Destination Name created in the Chapter Communication Set-up in SAP Risk and Assurance Management of the Set-up Instruction for this scope item. For example, XYZ.In the Time-Related Settings section, verify and adjust the Time-Related Settings which will be later used for the time selection of the data.Choose Save and Activate. | Automated Procedures is activated. |  |

#### Option Two: Create Your Own Automated Procedure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity is to create your own Automated Procedure (AP) to retrieve data in S/4HANA.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Risk and Assurance Management as Compliance Specialist. | SAP Risk and Assurance Management Launchpad is displayed. |  |
| 2 | Access Manage Automated Procedures | Open Manage Automated Procedures tile. | The Manage Automated Procedures screen is displayed. |  |
| 3 | Create Automated Procedures | Choose Create.In the Header tab, enter the following data:Procedure Name: <For example, General Journals Posted to the Prior Fiscal Period Test>System Type: <Select as appropriate>Destination: <The Destination Name Created in Chapter Communication Set-up in SAP Risk and Assurance Management of the Set-up Instruction for this scope item. For example, XYZ>Source Type: OData ServiceOData Service Name: <The OData Service Name is part of the URL of an OData service and is required in order to retrieve OData metadata. Enter the OData Service name published in Chapter Create Communication Arrangement of the Set-up Instruction for this scope item. For example, /sap/opu/odata/sap/C_JRNLENTRITMPRIORFSCLPERD_CDS>OData Entity Set Name: <The OData Entity Set Name is part of the URL of an OData service and is required to retrieve OData metadata. Enter the OData Entity Set Name for the OData Service published during the communication setup for this scope item. For example, C_JrnlEntrItmPriorFsclPerd>For available pre-delivered standard Automated Procedure, OData Service and corresponding Entity Set, you can refer to chapter [Use Cases](#unique_2) [page ] 3.Note If you are creating Automated Procedure with Published Custom CDS view OData Service, the Entity Name can also be found in the metadata of the OData service. To check the metadata of the OData service, you can add “$metadata” behind the URL of the OData Service then visit it via browser.Note SAP Risk and Assurance Management supports to monitor different business data via pre-delivered communication scenario or published custom CDS view. Refer to detailed set-up steps in Set-up Instruction for this scope.Fill in description as appropriate in Description.Choose Save and then choose Edit.In the Time-Related Settings section, choose Reference Period from the dropdown list which will be later used for the time selection of the data. For example, choose Calendar Date for field Reference Period, then choose Creation Date for field Field for Time Selection.Note Depending on the OData metadata retrieved, there may be three types of Reference Periods to choose from:Table 1: Time-Related SettingsReference PeriodDescriptionCalendar DateThe automated procedure can be run on the basis of calendar date ranges.Fiscal PeriodThe automated procedure can be run on the basis of fiscal periods.No DateThe automated procedure can be run without a time selection.Note Once you select your reference period, you must specify the Field for Time Selection. The options in this list depend on the reference period you selected as well as the OData metadata retrieved.Example: If you choose Calendar Date as the reference period, the field for time selection could be a creation date, a journal entry date, or a posting date, and so on.In the Parameters section, choose Add to add other fields as additional input parameters and then choose Select.Choose Save and Activate. | Automated Procedures is created and active. |  |

### Create Control and Assign Automated Procedure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The procedure below serves a guide on how to creates a new Control or use the pre-delivered standard Control to include Automated Procedure. It is mandatory for the following Work Package creation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Risk and Assurance Management as Compliance Manager. | SAP Risk and Assurance Management Launchpad is displayed. |  |
| 2 | Access Manage Controls | Open Manage Controls tile. | The Manage Controls screen is displayed. |  |
| 3 | Create Control | Choose Create and then fill in the following details:Name: <Control Name>Valid From: <Valid From date, for example, the first day of the current year>Valid To: <Valid To date, for example, the last day of the current year>Navigate to the Procedures tab. Choose Add for section Automated Procedures.Select the Automated Procedure created in the previous step and then choose OK.Choose Define in the Destination column to define the Destinations for the Procedures.Choose Edit in Destinations and Parameters screen, then fill in the input parameters and choose Save.Choose Create. | Control is created with Automated Procedure assigned. |  |
| 4 | Activate the Control | Choose Activate. | The Control is active. |  |

### Create Work Package and Assign Control

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity is to create Work Package to include Control and schedule automatic job for Work Package run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Risk and Assurance Management as Compliance Manager. | SAP Risk and Assurance Management Launchpad is displayed. |  |
| 2 | Access Manage Work Packages | Open Manage Work Packages tile. | The Manage Work Packages screen is displayed. |  |
| 3 | Create Work Package | Choose Create. Then choose Control Performance and fill in the following details:Name: <Work Package Name>Reference Period: <Select as appropriate. For example, Calendar Date>Note Like Reference Period in Automatic Procedure, there are three types of reference period: Calendar Date, Fiscal Period, and No Date. The Reference Period selected must be consistent with the value selected in the Automatic Procedure created in previous step. For example, select Calendar Date.Start Date: <Start Date for Work Package, for example, the first day of the current year>End Date: <End Date for Work Package, for example, No End Date>Run Frequency: <The frequency to schedule runs within the Work Package, for example, Run Once on Activation>Checking Period: <The Date range for checking period, for example, the first day of the current year - the last day of the current year>Note A Checking Period is a time period by which the data checked by automated procedures are filtered. You need to define the checking period used for each run of a work package when the Reference Period is Calendar Date or Fiscal Period.Fill in description as appropriate in the Description section.Navigate to the Controls and Procedures tab.Choose Add. Select the Control created in the previous steps and choose OK.Select the Destinations in the Enabled Destinations column to enable the Destinations for the Work Package.Choose Create. | Work Package is created with Control assigned. |  |
| 4 | Activate the Work Package | Choose Activate. | The Work Package is active and work package run will be trigger as planned. |  |

### Display Procedure Run Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity is to display the results for scheduled automated procedure run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Risk and Assurance Management as Compliance Manager. | SAP Risk and Assurance Management Launchpad is displayed. |  |
| 2 | Access Display Automated Procedure Runs | Open Display Automated Procedure Runs tile.Note Run results will also be listed in the detail of the corresponding work package. You can go to the tab Runs for the work package in app Manage Work Packages. Then you can select the completed runs to check the detailed run results. | The Display Automated Procedure Runs screen is displayed. |  |
| 3 | Display the Procedure Runs Results | In the Automated Procedure Runs list, select the completed Procedure Runs scheduled by the work package which was created in the previous steps. | The detail run results report is displayed. |  |

### Manage Issues

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity is to manage the issues identified from Automated Procedure Runs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Risk and Assurance Management as Compliance Specialist. | SAP Risk and Assurance Management Launchpad is displayed. |  |
| 2 | Access Process Issues | Open Process Issues. | The detailed list of issues identified from Automated Procedure Runs is displayed. |  |
| 3 | Set Status for Issues to In Process | Select the check box of the issues you want to change. Choose Edit Status and select In Process from the dropdown list. | The status for the issue is changed to In Process. |  |
| 4 | Add Comment and Set Conclusion for issues | Choose the issue you want to change and choose Edit. Then fill in the following details in the detail screen:Comment: <Enter as appropriate>Conclusion: <Select from the dropdown list. For example, Confirmed>Choose Save. | Issue is saved with Conclusion. |  |
| 5 | Set Status for Issues to Completed | Back to the Process Issues screen, select the check box of the issues you want to change. Choose Edit Status and select Completed from the dropdown list. | The status for the issue is changed to Completed. |  |

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
- related-to :: [[01-solution-foundation-and-platform/test-script-continuous-control-monitoring-with-sap-process-control-2oh]]
- related-to :: [[01-solution-foundation-and-platform/test-script-key-risk-indicator-monitoring-with-sap-risk-management-2u2]]
- related-to :: [[01-solution-foundation-and-platform/test-script-privacy-risk-detection-with-sap-risk-and-assurance-managem]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3KY_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 22,252 chars in the whole document
