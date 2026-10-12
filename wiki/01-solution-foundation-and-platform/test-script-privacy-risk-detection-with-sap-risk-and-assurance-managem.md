---
id: 01-solution-foundation-and-platform/test-script-privacy-risk-detection-with-sap-risk-and-assurance-managem
title: "Test Script: Privacy Risk Detection with SAP Risk and Assurance Management (3KX) (3KX_S4CLD2608_BPD_EN_XX)"
description: "Test script for scope item 3KX on SAP S/4HANA Cloud Public Edition: creating automated procedures, controls and work packages to detect privacy risks, e.g. in sales orders."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/governance-risk-and-control-monitoring]
aliases: [3KX_S4CLD2608_BPD_EN_XX]
keywords: ["Risk, Control and Privacy Monitoring (SAP Risk and…", privacy risk detection, automated procedures, controls, work packages, procedure run results, information lifecycle management, risk and assurance management, compliance roles, data protection and privacy]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3KX_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-950
topic: 01-solution-foundation-and-platform/governance-risk-and-control-monitoring
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Privacy Risk Detection with SAP Risk and Assurance Management (3KX) (3KX_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3KX_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Risk, Control and Privacy Monitoring (SAP Risk and Assurance Management)** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Privacy Risk Detection with SAP Risk and Assurance Management (3KX) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232834220)

[2 Use Cases 3](#_Toc232834221)

[3 Prerequisites 4](#_Toc232834222)

[3.1 Additional Manual Configuration 4](#_Toc232834223)

[3.2 System Access 4](#_Toc232834224)

[3.3 Roles 4](#_Toc232834225)

[3.4 Master Data, Organizational Data, and Other Data 5](#_Toc232834226)

[3.5 Business Conditions 5](#_Toc232834227)

[4 Overview Table 6](#_Toc232834228)

[5 Test Procedures 7](#_Toc232834229)

[5.1 Create Automated Procedure 7](#_Toc232834230)

[5.2 Create Control 8](#_Toc232834231)

[5.3 Create Work Package 10](#_Toc232834232)

[5.4 Display Automated Procedure Run Result 12](#_Toc232834233)

## Purpose

Overview

With SAP Risk and Assurance Management data protection and privacy controls, SAP establishes effective means to analyze and detect data protection and privacy anomalies in your connected SAP S/4HANA Cloud Public Edition system.

The use of personal information is strictly regulated by various regulations. Privacy risks exist when this type of data is collected and processed. As a supplement to manual governance, this scope item enables the automatic detection of privacy risks for personnel information and relevant documents (such as sales orders), providing insights on regulatory reporting and proactive auditing.

This document provides a general procedure for testing the scope item after solution activation. Detection of privacy risks in sales order is taken as an example in this test script. Besides, you can also implement other use cases based on your requirements. Please refer to [Use Cases](#unique_2) [page ] 3 for more details.

Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

## Use Cases

SAP Risk and Assurance Management provides pre-defined business content, such as controls, automated procedures. They can be used as a quick start of your business as well as for demo and education purpose.

For more information on pre-defined business content, please refer to the Business Content section in this [document](https://help.sap.com/spg).

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/1c43a73b798538647d39951fc1313029)

### System Access

Before this scope item can be tested, you must have access to SAP Risk and Assurance Management system and finish the onboarding process of SAP Risk and Assurance Management.

| System | Details |
| --- | --- |
| SAP Risk and Assurance Management | Accessible via SAP Risk and Assurance Management Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

In SAP Risk and Assurance Management:

| Business Role | Role Collection | Log On |
| --- | --- | --- |
| Specialist | compliance_specialist | Please ask your system administrator to assign to the tester. |
| Manager | compliance_manager | Please ask your system administrator to assign to the tester. |

For more information, please refer to User and Authorization Management in this [document](https://help.sap.com/viewer/9f06df5970b84ee18b9aa33c8fb0e4bd/1.0.0.0/en-US).

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represent materials, business partners, depending on the operational focus of your company.

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 1KA - Information Lifecycle Management | Information lifecycle management has been activated and retention rules has been maintained for the relevant objects such as sales order and HR objects.For example, if you want to detect privacy risk in sales order, you need to assign ILM object SD_VBAK to the appropriate existing audit area or a new one. Then create ILM policy and maintain retention rules under this combination of audit area and ILM object. |

## Overview Table

The Privacy Risk Detection with SAP Risk and Assurance Management (3KX) scope item consists of several process steps provided in the table below.

| Process Step | System/Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Automated Procedure](#unique_10) [page ] 7 | SAP Risk and Assurance Management/Specialist | Manage Automated Procedures | New AP is created and activated successfully. |
| [Create Control](#unique_11) [page ] 8 | SAP Risk and Assurance Management/Specialist | Manage Controls | New Control is created successfully. |
| [Create Work Package](#unique_12) [page ] 10 | SAP Risk and Assurance Management/Specialist | Manage Work Packages | New Work Package is created successfully. |
| [Display Automated Procedure Run Result](#unique_13) [page ] 12 | SAP Risk and Assurance Management/Specialist or Manager | Display Automated Procedure Runs | Results of Automated Procedure runs are listed successfully. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Automated Procedure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The compliance specialist creates a new Automated Procedure (AP) to retrieve data in S/4HANA Cloud. This new AP is mandatory for the following Control creation.

Prerequisite

Before you start creating a new Automated Procedure, make sure the setup guide of this scope item has been followed through to ensure connectivity between SAP Risk and Assurance Management and S/4HANA Cloud. What’s more, make sure the baseline content packages are imported successfully during your onboarding for SAP Risk and Assurance Management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Risk and Assurance Management as Specialist. |  |  |
| 2 | Option One: Adjust and Activate Pre-delivered Automated Procedure | Open the Manage Automated Procedures tile.Select a pre-delivered Automated Procedure, for example, Check sales orders against ILM retention rules, and drill down to the detailed page.Choose Edit on the upper right part of the screen.In the Systems section, choose Add under Systems to add the appropriate destination.In the Time-Related Settings section, verify and adjust the Time-Related Settings which will be used as a criteria when retrieving data.Choose Save and Activate to activate the Standard Automated Procedure. | Standard Automated Procedure is activated successfully. |  |
| 2 | Option Two: Create Your Own Automated Procedure | Open the Manage Automated Procedures tile.On the upper right of the Procedures List, choose Create.In the HEADER section, fill in the following details:Procedure Name: <Enter as appropriate, for example, ZAP_SO>System Type: <Select from the dropdown list>Destination: <Select from value help>Source Type: <Select from the dropdown list>OData Service Name: /sap/opu/odata/sap/GRCSPG_BASELINE_CONTENT_SRVOData Entity Set Name: <Enter as appropriate, for example, SalesOrderSet>Note For available pre-delivered OData Entity Set, you can refer to the chapter: [Use Cases](#unique_2) [page ] 3.In the DESCRIPTION section, enter as appropriate.Choose Save. Then choose Edit .In the Time-Related Settings section, fill in the following details:Reference Period: <Select as appropriate, for example, Calendar Date>Field for Time Selection: <Select as appropriate, for example, Created On>In the Parameters section, choose Add to add other fields as additional input parameters and then choose Select.Choose Save and Activate to activate the newly created procedure. | New Automated Procedure is created and activated successfully. |  |

### Create Control

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The compliance specialist creates a new Control or use the pre-delivered standard Control to include Automated Procedure. It is mandatory for the following Work Package creation.

Prerequisite

Before you start creating a new Control, make sure the newly created Automated Procedure in the prior steps is activated successfully.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Risk and Assurance Management as Manager. |  |  |
| 2 | Option One: Assign Automated Procedure to Standard Control | Open the Manage Controls tile.Select a pre-delivered Control, for example, Sales orders get destroyed when their retention period expires, and drill down to the detailed page.Choose Edit, and then navigate to the Procedures tab.Choose Add in the Automated Procedures section.Search and select the Automated Procedure created in previous step, then choose OK.Choose Define under the Destination column to define the Destinations for the Procedures.Choose Edit in the Destinations and Parameters view, fill in the input parameters and choose Save.Choose Activate to activate the Control. | Automated Procedure is assigned to Standard Control. |  |
| 3 | Option Two: Create Your Own Control | Open the Manage Controls tile.On the upper right of the Controls List, choose Create and fill in the following details:Name: <Enter as appropriate, for example, ZControl_SO>Valid From: <Select as appropriate, for example, today>Valid To: <Select as appropriate, for example, the end of current month>Significance: <Select from the dropdown list, for example, Standard>Control Risk Level: <Select from the dropdown list, for example, Medium>Recommended Monitoring Frequency: <Select from the dropdown list, for example, Any Frequency>Choose the Description tab, enter as appropriate.Choose the Procedures tab, and choose Add in the Automated Procedures section.Select the Automated Procedure created in the previous step and then choose OK.Choose Define under the Destination column to define the Destinations for the Procedures.Choose Edit in the Destinations and Parameters view, fill in the input parameters and choose Save.Choose Create, and then choose Activate to activate the Control. | Your Own Control is created with Automated Procedure assigned. |  |

### Create Work Package

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The compliance specialist creates a new Work Package to include Control and schedule regular automatic job for the privacy risk detection.

Prerequisite

Before you start creating a new Work Package, make sure the newly created Control in the prior steps is created successfully and assigned the right target destination system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Risk and Assurance Management as Specialist. |  |  |
| 2 | Create Work Package | Open the Manage Work Packages tile.On the upper right of the Packages List, choose Create and then choose Control Performance. | New Work Package page is displayed on the right part of the screen. |  |
| 3 | Enter Information for New Work Package | In the General Information section, fill in the following details:Name: <Enter as appropriate, for example, ZWP_SO>Reference Period: <Select from the dropdown list, for example, Calendar Date>Note Like Reference Period in Automatic Procedure, there are three types of reference period: Calendar Date, Fiscal Period, and No Date. The Reference Period selected must be consistent with the value selected in the Automatic Procedure created in previous step. For example, select Calendar Date.Start Date: <Select as appropriate, for example, today>End Date: <Select as appropriate, for example, No End Date>Run Frequency: <Select from the dropdown list, for example, Run Once on Activation>Checking Period: <Select as appropriate, for example, Data range of last year>Note A Checking Period is a time period by which the data checked by automated procedures are filtered. You need to define the checking period used for each run of a work package when the Reference Period is Calendar Date or Fiscal Period.Navigate to the Controls and Procedures tab.Choose Add. Select the Control created in the previous steps and choose OK.Select the Destinations in the Enabled Destinations column to enable the Destinations for the Work Package.Choose the Description tab, and enter as appropriate.Choose Create. | New Work Package is created. |  |
| 4 | Activate the Work Package | Choose Activate. | The work package is active and work package run will be triggered as planned. |  |

### Display Automated Procedure Run Result

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The work package created above will run as schedule after activation. The compliance specialist or the compliance manager log on to the SAP Risk and Assurance Management system to view the result of automated procedure run and take actions for the risk.

Prerequisite

Before you start the test procedures, make sure the work package is scheduled successfully and the first run is finished.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Risk and Assurance Management as Manager. |  |  |
| 2 | Display the Procedure Runs Results | Open Display Automated Procedure Runs.In the Procedure Runs list, select the completed Procedure Runs scheduled by the work package which was created in the previous steps. | The detailed run results report will be displayed. |  |
| 3 | Remediate the Risks (Optional) | Please refer to [Use Cases](#unique_2) [page ] 3 for more details. |  |  |

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
- related-to :: [[01-solution-foundation-and-platform/test-script-control-monitoring-with-sap-risk-and-assurance-management]]
- related-to :: [[01-solution-foundation-and-platform/test-script-key-risk-indicator-monitoring-with-sap-risk-management-2u2]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3KX_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 18,441 chars in the whole document
