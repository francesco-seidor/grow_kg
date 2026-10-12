---
id: 13-quality-ehs-and-compliance/test-script-permit-to-work-7z4-ae-sap-s-4hana-cloud-public-edition-123
title: "Test Script: Permit to Work (7Z4_AE) - SAP S/4HANA Cloud Public Edition (7Z4_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 7Z4 (AE) Permit to Work: configuration prerequisites and test steps for work permit templates and work permits, 2608 release."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/permit-to-work]
aliases: [7Z4_S4CLD2608_BPD_EN_AE]
keywords: [Permit to Work, work permit lifecycle, work permit templates, permit types, work permit approval, permit template types, nature of work, permit to work profile, teams and responsibilities, function profiles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7Z4_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1239
topic: 13-quality-ehs-and-compliance/permit-to-work
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Permit to Work (7Z4_AE) - SAP S/4HANA Cloud Public Edition (7Z4_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7Z4_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Permit to Work** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Permit to Work (7Z4_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232860801)

[2 Prerequisites 4](#_Toc232860802)

[2.1 System Access 4](#_Toc232860803)

[2.2 Roles 4](#_Toc232860804)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232860805)

[2.4 Preliminary Steps 6](#_Toc232860806)

[2.4.1 Maintain Permit to Work Profile for Planning Plant 6](#_Toc232860807)

[2.4.2 Define Permit Types 8](#_Toc232860808)

[2.4.3 Define Permit Template Types 10](#_Toc232860809)

[2.4.4 Define Nature of Work 13](#_Toc232860810)

[2.4.5 Assign Nature of Work 15](#_Toc232860811)

[2.4.6 Define Team Types (Optional) 17](#_Toc232860812)

[2.4.7 Define Functions (Optional) 19](#_Toc232860813)

[2.4.8 Define Function Profile (Optional) 21](#_Toc232860814)

[2.4.9 Assign Function Profile to Team Category (Optional) 23](#_Toc232860815)

[2.4.10 Manage Teams and Responsibilities (Optional) 24](#_Toc232860816)

[2.4.11 Configure Flexible Workflow for Permit (Optional) 25](#_Toc232860817)

[3 Overview Table 28](#_Toc232860818)

[4 Test Procedures 29](#_Toc232860819)

[4.1 Work Permit Template 29](#_Toc232860820)

[4.1.1 Create Work Permit Template 29](#_Toc232860821)

[4.1.2 Submit for Approval for Work Permit Template 30](#_Toc232860822)

[4.2 Work Permit 31](#_Toc232860823)

[4.2.1 Create Work Permit 31](#_Toc232860824)

[4.2.2 Submit For Approval for Work Permit 33](#_Toc232860825)

[4.2.3 Approve Work Permit 34](#_Toc232860826)

[4.2.4 Issue Work Permit 35](#_Toc232860827)

[4.2.5 Extend Work Permit (Optional) 36](#_Toc232860828)

[4.2.6 Return and Deactivate Work Permit (Optional) 37](#_Toc232860829)

[4.2.7 Activate and Handout Work Permit (Optional) 38](#_Toc232860830)

[4.2.8 Closure of Work Permit 39](#_Toc232860831)

[5 Appendix 41](#_Toc232860832)

[5.1 Process Integration 41](#_Toc232860833)

[5.1.1 Preceding Processes 41](#_Toc232860834)

## Purpose

Overview

The Permit to Work (PTW) process is a formal system used in various asset-centric industries to ensure that high-risk jobs (such as hot work, confined space entry, electrical isolation, work at height, and so on) are performed safely and in compliance with regulations. It acts as an authorization tool that ensures work is conducted under controlled conditions and facilitates collaboration between maintenance, operations and safety departments.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

|  |
| --- |
| Caution In a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/4HI_S4CLD2408_BPD_EN_DE.docx) ). |

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
| Maintenance Supervisor | SAP_BR_MAINT_SUPERVISOR | Maintenance Supervision | SAP_BR_MAINTENANCE_SUPERVISOR |  |
| Maintenance Technician | SAP_BR_MAINTENANCE_TECHNICIAN | Maintenance Execution | SAP_BR_MAINTENANCE_TECHNICIAN |  |
| Plant Manager | SAP_BR_PLANT_MANAGER | Plant Management | SAP_BR_PLANT_MANAGER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Work Center | RES-0100 | Mechanics |  |
| Work Center | RES-0200 | Electric |  |
| Work Center | RES-0300 | Instrumentation |  |
| Functional Location | 3310-XXX-XXX-XXXXX-XXXX-XXXX | 3310 and the substructures |  |
| Equipment | 21010XXXX | 210100001 ~ 210100092 |  |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| 5LM | Create Functional Location - MDS |
| 5MF | Create Equipment - MDS |
| 5MH | Create Maintenance Work Center - MDS |

### Preliminary Steps

#### Maintain Permit to Work Profile for Planning Plant

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to configure Permit to Work Profile for Planning Plant.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country/region-dependent settings for the intended local version, choose Set Local Version.Select the Application Area as Asset ManagementSelect the Sub Application Area as Maintenance ManagementSelect the row with the item name: Permit to Work | Configure Your Solution screen is displayed. |  |
| 4 | Open Maintain Permit to Work Profile for Planning Plant | Under Configuration Steps, select the step name " Maintain Permit to Work Profile for Planning Plant " and click on Configure | The Maintain Permit to Work Profile for Planning Plant screen will be displayed |  |
| 5 | Create the Entry | Click on New Entries,Enter the following details:Planning Plant: 3310Maximum Orders to Work Permit: < Enter the number of Orders eg: 999>Partner Determination procedure: PMPTSelect Check box for Order Assignment required in Work permitSelect Check box for Maintain Issue History if issue history need to be displayed in the Manage Work Permit AppClick on Save | The Maintain Permit to Work Profile for Planning Plant has been configured. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Implementation Activities. | The Manage Your Solution screen is displayed. |  |
| 3 | Access Configuration | To locate the activity in the tree view, click on the Search icon.Enter the SSCUI ID - 107252 | The Activity in Tree View is displayed. |  |
| 4 | Open Maintain Permit to Work Profile for Planning Plant | Select the Node, a new screen will open to maintain the entries | The Maintain Permit to Work Profile for Planning Plant screen will be displayed |  |
| 5 | Create the Entry | Click on New Entries,Enter the following details:Planning Plant: 3310Maximum Orders to Work Permit: 999Partner Determination procedure: PMPTSelect Check box for Order Assignment required for Work permitSelect Check box for Maintain Issue History if issue history need to be displayed in the Manage Work Permit AppClick on Save | The Maintain Permit to Work Profile for Planning Plant has been configured. |  |

#### Define Permit Types

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to configure the permit types.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country/region dependent settings for the intended local version, choose Set Local Version.Select the Application Area as Asset ManagementSelect the Sub Application Area as Maintenance ManagementSelect the row with the item name: Permit to Work. | The Configure Your Solution screen displays. |  |
| 4 | Open Define Permit Types | Under Configuration Steps, find the step name Define Work Permit Types and choose Configure. | The Define Permit Types screen displays. |  |
| 5 | Define Permit Types | Choose New Entries.Planning Plant: 3310Work Permit Type: <Enter the Permit Type>Work Permit Type Description: <Enter the description>Is Approval Required?: SelectNote If the Is Approval Required? checkbox is not selected, the permit will not be sent for approval. Planners need to mark it ready for issue while processing the permit.Under the Number Range section:Int. No. Range: <Enter the Number Range number>Under Default Values Determination:Offset Values: <Enter the offset value in Days>Default Work Permit Validity: <Enter the Validity in Hrs>Maximum Validity of Work Permit: <Enter the maximum Validity in Hrs>Default Start Time for Work Permit: <Enter the default start time in HH:MM:SS format>Choose Save. | The Permit Type has been configured. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Work Permit Types | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: SSCUI ID - 107253Define Work Permit Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Work Permit Types screen displays. |  |
| 3 | Define Permit Types | Choose New Entries, and make the following entries:Planning Plant:3310Work Permit Type: <Enter the Permit Type>Work Permit Type Description: <Enter the description>Is Approval Required?: SelectNote If the Is Approval Required? checkbox is not selected, the permit will not be sent for approval. Planners need to mark it ready for issue while processing the permit.Under Number Range SectionInt. No. Range: <Enter the Number Range number>Under the Default Values Determination:Offset Values: <Enter the offset value in Days>Default Work Permit Validity: <Enter the Validity in Hrs>Maximum Validity of Work Permit: <Enter the maximum Validity in Hrs>Default Start Time for Work Permit: <Enter the default start time in HH:MM:SS format>Choose Save | The Permit Type has been configured. |  |

#### Define Permit Template Types

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to Configure the Permit Template Types

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country/regiondependent settings for the intended local version, choose Set Local Version.Select the Application Area as Asset ManagementSelect the Sub Application Area as Maintenance ManagementSelect the row with the item name: Permit to Work | Configure Your Solution screen is displayed. |  |
| 4 | Open Define Permit Template Types | Under Configuration Steps, select the step name Define Work Permit Template Types and click on Configure. | The Define Permit Template Types screen will be displayed. |  |
| 5 | Define Permit Template Types | Click on New Entries.Planning Plant: 3310Work Permit Template Type: <Enter the Permit Template Type>Work Permit Template Type Description: <Enter the description>Under Number Range section:Int. No. Range: <Enter the Number Range number>Under Default Values Determination:Offset Values: <Enter the offset value in Days>Default Work Permit Validity: <Enter the Validity in Hrs>Maximum Validity of Work Permit: <Enter the maximum Validity in Hrs>Default Start Time for Work Permit: <Enter the default start time in HH:MM:SS format>Ref Work Permit Type : < Select the Permit Type>Click Save | The Permit Template Type has been configured. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Implementation Activities. | The Manage Your Solution screen is displayed. |  |
| 3 | Access Configuration | To locate the activity in the tree view, click on the Search icon.Enter the SSCUI ID - 107249 | The Activity in Tree View is displayed. |  |
| 4 | Open Define Permit Template Types | Select the Node, a new screen will open to maintain the entries | The Maintain Permit to Work Profile for Planning Plant screen will be displayed |  |
| 5 | Define Permit Template Types | Click on New EntriesPlanning Plant :3310Permit Template Type : <Enter the Permit Type>Template Type Description : <Enter the description>Under Number Range SectionInt. No. Range : <Enter the Number Range number>Under Default Values DeterminationOffset Values: <Enter the offset value in Days>Default Work Permit Validity - <Enter the Validity in Hrs>Maximum Validity of Work Permit: <Enter the maximum Validity in Hrs>Default Start Time for Work Permit: <Enter the default start time in HH:MM:SS format>Ref Work Permit Type: <Select the Work Permit Type>Click Save | The Permit Type has been configured. |  |

#### Define Nature of Work

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to Configure the Nature of Work

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country/regiondependent settings for the intended local version, choose Set Local Version.Select the Application Area as Asset ManagementSelect the Sub Application Area as Maintenance ManagementSelect the row with the item name: Permit to Work | Configure Your Solution screen is displayed. |  |
| 4 | Open Define Nature of Work | Under Configuration Steps, select the step name Define Nature of Work and click on Configure. | The Define Nature of Work screen will be displayed. |  |
| 5 | Define Nature of Work Group | Click on New Entries.Nature of Work Group: <Enter the Group>Nature of Work Group Description: <Enter the Description>Click on Save. | The Nature of work Group have been configured. |  |
| 6 | Define Nature of Work Items | Click on New Entries.Nature of Work Item: <Enter the Item>Nature of Work Item Description: <Enter the Item Description>Click on Save. | The Nature of work Item have been configured. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Implementation Activities. | The Manage Your Solution screen is displayed. |  |
| 3 | Access Configuration | To locate the activity in the tree view, click on the Search icon.Enter the SSCUI ID - 107251 | The Activity in Tree View is displayed. |  |
| 4 | Open Define Nature of Work | Select the Node, a new screen will open to maintain the entries | The Maintain Permit to Work Profile for Planning Plant screen will be displayed |  |
| 5 | Define Nature of Work Group | Click on New EntriesNature of Work Group: <Enter the Group>Nature of Work Group Description: <Enter the Description>Click on Save | The Nature of Work Group have been configured. |  |
| 6 | Define Nature of Work Items | Click on New EntriesNature of Work Item: <Enter the Item>Nature of Work Item Description: <Enter the Item Description>Click on Save | The Nature of Work Item have been configured. |  |

#### Assign Nature of Work

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to Configure the assignment of Nature of Work Group and Items to Work Permit Types or Work Permit Template Types.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country/regiondependent settings for the intended local version, choose Set Local Version.Select the Application Area as Asset ManagementSelect the Sub Application Area as Maintenance ManagementSelect the row with the item name: Permit to Work | Configure Your Solution screen is displayed. |  |
| 4 | Open Assign Nature of Work | Under Configuration Steps, select the step name Assign Nature of Work and click on Configure. | The Assign Nature of Work screen will be displayed. |  |
| 5 | Select Work Permit/Template Type and Assignment of Nature of Work | All the Work Permit Type/Work Permit Template Types will be displayed.Select any line item and double-click on Assign NoW to Work Permit/Template type.Click on New Entries and maintain:Nature of Work Group: <Select the Nature of Work Group from the dropdown>.Nature of Work Item: <Select the Nature of Work Item from the dropdown>.Click on Save. | The assignment of Nature of Work to Work Permit/Template type has been configured. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Implementation Activities. | The Manage Your Solution screen is displayed. |  |
| 3 | Access Configuration | To locate the activity in the tree view, click on the Search icon.Enter the SSCUI ID - 107248 | The Activity in Tree View is displayed. |  |
| 4 | Open Assign Nature of Work | Select the Node, a new screen will open to maintain the entries | The Maintain Permit to Work Profile for Planning Plant screen will be displayed |  |
| 5 | Select Work Permit/Template Type and Assignment of Nature of Work to Permit/Template Type | All the Work Permit Type/Work Permit Template Types will be displayed.Select any line item and double-click on Assign NoW to Work Permit/Template Type.Click on New EntriesNature of Work Group: <Select the Nature of Work Group from the dropdown>Nature of Work Item: <Select the Nature of Work Item from the dropdown>Click on Save | The Assignment of Nature of Work to Work Permit/Template Type has been configured. |  |

#### Define Team Types (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this configuration item, you can create and manage team types for team categories. A team type inherits its functions and responsibility definitions from its associated team category. If necessary, you may need to exclude functions and responsibility definitions from a team type based on a team's requirements.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country/region dependent settings for the intended local version, choose Set Local Version.Select Application Area as Application Platform and InfrastructureSelect Sub Application Area as Responsibility ManagementChoose the row with the item name: Teams | The Configure Your Solution screen displays. |  |
| 4 | Open Define Team Types | Under Configuration Steps, select the step name Define Team Type and choose Configure. | The Define Team Type screen displays. |  |
| 5 | Create Team Type | Choose New Entries and maintain the following entries:Team Type: Enter a unique nameTeam Category: EAM_WORK_PERMITEnter a description for the custom team type.Choose Save. | The team type is defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Team Types | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: SSCUI ID – 101066 Define Team TypesChoose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Team Types screen displays. |  |
| 3 | Create a Team Type | Choose New Entries and maintain the following entries:Team Type: Enter a Unique nameTeam Category: EAM_WORK_PERMITEnter a description for the custom team type.Choose Save. | The team type is defined. |  |

#### Define Functions (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this configuration item, you can create a function. You can group relevant functions into function profiles.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country/region dependent settings for the intended local version, choose Set Local Version.Select Application Area as Application Platform and Infrastructure.Select Sub Application Area as Responsibility Management.Choose the row with the item name: Functions. | The Configure Your Solution screen displays. |  |
| 4 | Open Functions | Under Configuration Steps, find the step Define Functions and choose Configure. | The Define Functions screen displays. |  |
| 5 | Create Functions | Choose New Entries and maintain the following entries:Function: Enter a unique name for the functionFunction Description: Enter a description for the functionChoose Save. | The function is defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Functions | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: SSCUI ID – 101065 Define FunctionsChoose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Functions screen displays. |  |
| 3 | Create Functions | Choose New Entries and maintain the following entries:Function: Enter a unique name for the functionFunction Description: Enter a description for the functionChoose Save. | The function is defined. |  |

#### Define Function Profile (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This configuration step enables you to create a function profile and assign functions to the profile. You can group similar functions for a business process in a function profile.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country/region dependent settings for the intended local version, choose Set Local Version.Select Application Area as Application Platform and InfrastructureSelect Sub Application Area as Responsibility ManagementChoose the row with the item name: Functions | The Configure Your Solution screen displays. |  |
| 4 | Open Functions | Under Configuration Steps, find the step Define Function Profiles and choose Configure. | The Define Function Profiles screen displays. |  |
| 5 | Create a Function Profile | Choose New Entries and maintain the following entries:Profile: Enter a unique name for the function profileFunction Profile Description: Enter a description for the function profileChoose Save. | The function profile is defined. |  |
| 6 | Assign Function Profile to Functions | Select the newly configured function profile and click on the next configuration node: Function Profile to Function MappingChoose New Entries and maintain the following entries:Select a relevant function from function list and choose OK.Repeat the above steps if more functions need to be selected.Choose Save. | The assignment of Function Profile to Functions is completed. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Function Profiles | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: SSCUI ID – 101067 Define Function ProfilesChoose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Function Profiles screen displays. |  |
| 3 | Create a Function Profile | Choose New Entries and maintain the following entries:Profile: Enter a unique name for the function profileFunction Profile Description: Enter a description for the function profileChoose Save. | The function profile is defined. |  |
| 4 | Assign Function Profile to Functions | Select the newly configured function profile and click on the next configuration node: Function Profile to Function MappingChoose New Entries and maintain the following entries:Select a relevant function from function list and choose OK.Repeat the above steps if more functions need to be selected.Choose Save. | The assignment of Function Profile to Functions is completed. |  |

#### Assign Function Profile to Team Category (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this configuration step, you can assign a function profile to a team category. A function profile consists of a group of relevant functions. Functions and function profiles are assigned to team categories and inherited by teams types.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country/region dependent settings for the intended local version, choose Set Local Version.Select Application Area as Application Platform and InfrastructureSelect Sub Application Area as Responsibility ManagementChoose the row with the item name: Teams | The Configure Your Solution screen displays. |  |
| 4 | Open Teams | Under Configuration Steps, find the step Assign Function Profiles to Team Categoryand choose Configure. | The Assign Function profile to team category screen displays. |  |
| 5 | Assign a Function Profile to a Team Category | Choose New Entries and maintain the following entries:Team Category: EAM_WORK_PERMITProfile: Select the function profile from the function list and choose OK.Choose Save. | The assignment of function profile to team category is completed. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Assign Function Profiles to Team Category | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Function Profiles to Team CategoryChoose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Function Profiles to Team Category screen displays. |  |
| 3 | Assign a Function Profile to a Team Category | Choose New Entries and maintain the following entries:Team Category: EAM_WORK_PERMITProfile: Select the function profile from the function list and choose OK.Choose Save. | The assignment of function profile to team category is completed. |  |

#### Manage Teams and Responsibilities (Optional)

Purpose

In this procedure, you configure teams and responsibility for projects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Teams and Responsibilities - Asset Management (F4988).Choose Create. | The New Team screen displays. |  |
| 3 | Maintain the Team Details | Make the following entries:On the Team Information tab:Name: Permit ManagementDescription: Permit ManagementGlobal ID: specify a unique IDType: Select the team type configured for team category: EAM_WORK_PERMITStatus: EnabledOn the Team Members tab:Choose Create, and maintain the following values:Business Partner: use the search function to find the business partnerNote The Business Partner should have the business catalog SAP_EAM_BC_PTW_MNG_APPRVR_PC for approving or rejecting the work permit.Functions: select a function |  |  |
| 4 | Create the Team | Choose Create. | The team is created. |  |

#### Configure Flexible Workflow for Permit (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can configure and activate flexible workflow for maintenance orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Work Permit (F9428). | The Manage Workflows screen displays. |  |
| 3 | Check Automatic Approval of Work Permit | In the Workflows list, choose Automatic Approval of Work Permit, and make sure workflow Automatic Approval of Work Permit is in active status. If not, select it and choose Activate. | The workflow item is activated. |  |
| 4 | Manage Workflow | You can also create a custom workflow. When a workflow is triggered, it determines the agents who can approve the maintenance order.Below is a custom workflow created for reference:Choose Create and make following entry:Workflow Name: <Enter Text>Go to the START CONDITIONS area and select Work Permit Type: <Enter Work Permit Type> |  |  |
| 5 | Create Step Sequence | Go to the STEPS area, choose Create, and then make the following entries on the next screen:Go to the RECIPIENTS area:Assignment By: TeamTeam: <Select the created team from dropdown list>Step to be completed by: For example, one of the recipientsGo to the Step Conditions area and select Main Work Center of the Maintenance Order: <Enter Main Work Center>.Add more conditions if required by choosing the plus icon.Choose Create. |  |  |
| 6 | Save Workflow | Choose Save. | The workflow is created. |  |
| 7 | Activate Workflow | Go back to the workflow list.Select the required workflow and choose Activate. | The workflow is activated. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Work Permit Template](#unique_19) [page ] 29 | Maintenance Planner | Manage Work Permit Templates (F4692) | The Work Permit Template is created |
| [Submit for Approval for Work Permit Template](#unique_20) [page ] 30 | Maintenance Planner | Manage Work Permit Templates (F4692) | The status will update to No Approval Required |
| [Create Work Permit](#unique_21) [page ] 31 | Maintenance Planner | Manage Work Permits (F6579) | The work permit is created. |
| [Submit For Approval for Work Permit](#unique_22) [page ] 33 | Maintenance Planner | Manage Work Permits (F6579) | The status changes to Ready for Issue. |
| [Approve Work Permit](#unique_23) [page ] 34 | Plant Manager | My Inbox - All Items (F0862) | The work permit is approved. |
| [Issue Work Permit](#unique_24) [page ] 35 | Maintenance Supervisor | Manage Work Permits (F6579) | The status changes to Live/Handout. |
| [Extend Work Permit (Optional)](#unique_25) [page ] 36 | Maintenance Supervisor | Manage Work Permits (F6579) | The Validity End Date is updated. |
| [Return and Deactivate Work Permit (Optional)](#unique_26) [page ] 37 | Maintenance Supervisor | Manage Work Permits (F6579) | The status changes to Suspended. |
| [Activate and Handout Work Permit (Optional)](#unique_27) [page ] 38 | Maintenance Supervisor | Manage Work Permits (F6579) | The status changes to Live/Handout. |
| [Closure of Work Permit](#unique_28) [page ] 39 | Maintenance Supervisor | Manage Work Permits (F6579) | The status changes to Closed. |

## Test Procedures

### Work Permit Template

#### Create Work Permit Template

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A Work Permit Template is used to simplify and speed up the creation of work permits by providing a predefined structure with standard information such as partners, reference/safety documents and responsibility info. It ensures consistency, accuracy, and compliance across all permits while reducing manual effort and errors.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Maintenance Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Work Permit Templates (F4692). | The Manage Work Permit Templates page appears. |  |
| 3 | Create Work Permit | Choose Create. | A pop-up screen appears. |  |
| 4 | Enter Creation Parameters | Enter the following and choose Continue:Planning Plant: 3310Work Permit Type: Select from drop-down (for example, YHT)Reference Work Permit Template: Select the existing work permit template from the drop-down (Optional)Choose Create | The Create Work Permit Template page displays. |  |
| 5 | Maintain General Information | Make the following entries:Template Description: <Description> (for example, Hot Work Permit Template)Main Work Center: RES-0100Work Center Plant: 3310Planner Group: Select from the listTechnical Object: Select from the list (Optional)Nature of Work: Select the relevant option | The work permit template is created with Work Permit Processing Status Planning and Preparation. | The General Information has been maintained |
| 6 | Maintain Partner Functions (Optional) | Choose the Partner Functions tab.Choose Add. In the pop-up dialog box, select the Partner Function and choose Add. | The Partner Functions are maintained. |  |
| 7 | Add Attachment/URL (Optional) | On the Attachments tab:Select Document type from the dropdown.Choose Upload and select the files you want to upload.Alternatively, choose Add a Link to provide a link to relevant information for the maintenance notification. | The files and the links are added to the Work Permit Template. |  |
| 8 | Save | Choose Create. | The Work Permit Template is created with Processing Status Planning and Preparation. |  |

#### Submit for Approval for Work Permit Template

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The permit template created in the previous step has to be submitted for approval for processing the permit further.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Work Permit Templates (F4692). | The Manage Work Permit Templates page appears. |  |
| 3 | Get Work Permit Template | Search for the Work Permit Template created in the previous step. Once the Work Template is visible in the List, click on the arrow in the extreme right to enter into the object page. | The Work Permit Template page displays. |  |
| 4 | Submit for Approval | Choose Actions and select Submit for Approval. A pop up message is displayed to confirm the selection. Choose OK. | The Work Permit Template processing status changes from Planning and Preparation to No Approval Required. |  |

|  |
| --- |
| Note Currently, there is no workflow in place for approving Work Permit templates. When a Work Permit template is submitted for approval, its status is automatically updated to 'No Approval required'. |

### Work Permit

#### Create Work Permit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To provide authorization for jobs that require high-risk activities, Permit to Work provides Work Permit, a formal printed document with the description of the work, the requirements to be fulfilled, and the safety measures to be followed. A work permit authorizes the receiver to carry out the specified work at the specified time and acts as an agreement between the issuer and the receiver about the conditions, risks, and precautions involved.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Maintenance Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Work Permits (F6579). | The Manage Work Permits screen appears. |  |
| 3 | Create Work Permit | Choose Create. | A pop up screen appears. |  |
| 4 | Enter Creation Parameters | Enter the following information.Planning Plant: 3310Work Permit Type: Select from drop down (eg: YHP)Reference Maintenance Order: Select the maintenance order from the dropdown (Optional Step)Create with reference to: Select either Permit or Template from the options (Optional Step)Reference Work Permit / Work Permit Template: Select the permit or template from the list (Optional Step)Choose Create. | The Create Work Permit screen displays. |  |
| 5 | Maintain General Information | Make the following entries:Work Permit Description: <Description> Enter a description. For example, Hot Work Permit.Main Work Center: RES-0100Work Center Plant: 3310Planner Group: Select from the listTechnical object: Select from the listSelect Nature of Work: Select the relevant nature of work from the list displayed | The General Information has been maintained |  |
| 6 | Maintain Partner (Optional) | Click on Partner TabClick on Add, a pop up screen appears to select the Partner Function and click on add.Select the Partner Number. | The Partners are maintained. |  |
| 7 | Add Attachment/URL (Optional) | In the Attachments tab:Select Document type from the dropdown list.Choose Upload and select the files you want to upload.Alternatively, choose Add a Link to provide a link to relevant information for the maintenance notification. | The files and the links are added to the Work Permit . |  |
| 8 | Save | Choose Create. | The Work Permit is created with Processing Status Planning and Preparation. |  |

#### Submit For Approval for Work Permit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Permit created in the previous step has to be submitted for approval for processing the permit further.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Maintenance Planner. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Work Permits (F6579). | The Manage Work Permits screen appears. |  |
| 3 | Get Work Permit | Search for the Work Permit created in the previous step. Once the Work Permit is visible in the list, click on the arrow in the extreme right to enter into the object page. | The Work Permit page displays. |  |
| 4 | Assign Maintenance Order | Choose Edit to go to the Assigned Order tab and choose Add. Find the maintenance order to be added and choose OK.Note If no order assignment is required for work permit, uncheck Order assignment required in work permit in SSCUI: Maintain Permit to Work Profile for Planning Plant. | Maintenance order will be assigned to work permit. |  |
| 5 | Submit for Approval | Choose Save. Then choose Actions and select Submit for Approval. A pop up is displayed to confirm the selection. Choose OK. | The work permit processing status changes from Planning and Preparation to Approval in Progress. |  |

|  |
| --- |
| Note If flexible workflow is not configured then, the work permit needs to be marked as Ready for Issue by selecting Actions > Set Ready for Issue . |

#### Approve Work Permit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to approve work permits from the My Inbox - All Items (F0862) app.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

|  |
| --- |
| Note The Business Partner should have the business catalog SAP_EAM_BC_PTW_MNG_APPRVR_PC for approving or rejecting the work permit. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Plant Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | A list of work permits that are ready for approval is displayed. |  |
| 3 | Approve Work Permit | On the My Inbox screen, choose a workflow request for a work permit. You can review the information page that provides details about the work permit or navigate to display the work permit by choosing Open Task.Enter a comment in the Comments section.Choose Approve to approve the work permit and add decision note if needed.Note If a work permit is rejected, it can be processed further and sent for approval again by the planner. | The work permit is approved and the permit is removed from the list in My Inbox.The processing status changes to Ready for Issue once approval is completed. |  |

#### Issue Work Permit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The approved work permit has to be assigned to a technician to present it to the relevant department to allow him/her to the premise to carry out the maintenance activity.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Maintenance Supervisor. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Work Permits (F6579). | The Manage Work Permit screen appears. |  |
| 3 | Get Work Permit | Search for the work permit created in the previous step. Once the work permit is visible in the list, click on the arrow in the extreme right to enter into the object page. | The Work Permit page displays. |  |
| 4 | Assign Technician | Choose Actions and select Handout Work Permit. A pop up will appear to confirm the selection. Choose OK.A new pop-up window is displayed. Input the following details:Issued To: <Select the Technician ID>Contingent ID: <Select the Contigent ID>Comments: <Enter the comments>Choose Hand Out. | The work permit processing status changes from Ready for issue to Live/Handed out. |  |

#### Extend Work Permit (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the Work requires more time to finish than the Validity End Date, then Work Permit can be extended to a desired Validity End Date.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Supervisor. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Work Permits (F6579). | The Manage Work Permit screen appears. |  |
| 3 | Get Work Permit | Search for the Work Permit created in the previous step. Once the Work Permit is visible in the List, click on the arrow in the extreme right to enter into the object page. | The Work Permit page displays. |  |
| 4 | Extend Work Permit | Choose Extend Validity. A pop-up screen appears.Enter the Validity End Date and Time.Click on Extend Validity.Changes are saved automatically. | The work permit Validity End Date/Time has been updated. |  |

#### Return and Deactivate Work Permit (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When there is an unforeseen event which blocks the maintenance technician to carry out the maintenance activity during the permit period, then the permit has to be returned and deactivated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Maintenance Supervisor. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Work Permits (F6579). | The Manage Work Permit screen appears. |  |
| 3 | Get Work Permit | Search for the work permit created in the previous step. Once the work permit is visible in the list, click on the arrow in the extreme right to enter into the object page. | The Work Permit page displays. |  |
| 4 | Return and Deactivate Work Permit | Choose Actions and select Return and Deactivate Work Permit. A pop up will appear to confirm the selection. Choose OK. | The work permit processing status changes from Live/Handed out to Suspended. |  |

#### Activate and Handout Work Permit (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the unforeseen event is over and the technician is ready to carry out the maintenance activity on premise, then the permit needs to be activated back and handed over to the technician.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Maintenance Supervisor. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Work Permits (F6579). | The Manage Work Permit page appears. |  |
| 3 | Get Work Permit | Search for the work permit created in the previous step. Once the work permit is visible in the list, click on the arrow in the extreme right to enter into the object page. | The Work Permit page displays. |  |
| 4 | Activate and Handout Work Permit | Choose Actions and select Activate and Handout Work Permit. A pop up will appear to confirm the selection. Choose OkA New Pop Up will appear, Input the following details:Issued To: <Select the Technician ID>Contingent ID: <Select the Contigent ID>Comments: <Enter the comments>Choose Hand Out | The work permit status changes from Suspended to Live/Handed out. |  |

|  |
| --- |
| Note The Issue History tab provides detailed information regarding the permit handout, including the issuer, recipient, and the date of issue. |

#### Closure of Work Permit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the technician has performed the maintenance activity and no work is pending, the work permit has to be returned and closed

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Supervisor. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Work Permits (F6579). | The Manage Work Permit page appears. |  |
| 3 | Get Work Permit | Search for the work permit created in the previous step. Once the work permit is visible in the list, click on the arrow in the extreme right to enter into the object page. | The Work Permit page displays. |  |
| 4 | Return and Close Work Permit | Choose Actions and select Return and Close Work Permit. A pop up will appear to confirm the selection. Choose OK. | The work permit Processing Status changes from Live/Handed out to Closed. |  |

## Appendix

### Process Integration

#### Preceding Processes

In cases where a maintenance activity necessitates a Work Permit, a corresponding maintenance order must be initiated beforehand.

| Process | Business Condition |
| --- | --- |
| Reactive Maintenance (4HI) | Maintenance Order can be assigned to a Work Permit. |
| Proactive Maintenance (4HI) | Maintenance Order can be assigned to a Work Permit. |
| Operational & Overhead Maintenance (4WM) | Maintenance Order can be assigned to a Work Permit. |
| Improvement Maintenance (4VT) | Maintenance Order can be assigned to a Work Permit. |

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
- see-also :: [[14-maintenance-service-and-projects/reactive-maintenance-4hh-ae-test-script-sap-s-4hana-cloud-public-editi]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7Z4_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 65,053 chars in the whole document
