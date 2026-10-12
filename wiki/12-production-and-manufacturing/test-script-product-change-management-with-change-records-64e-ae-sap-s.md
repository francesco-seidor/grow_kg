---
id: 12-production-and-manufacturing/test-script-product-change-management-with-change-records-64e-ae-sap-s
title: "Test Script: Product Change Management with Change Records (64E_AE) - SAP S/4HANA Cloud Public Edition 2608 (64E_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 64E: change record lifecycle (create, assign BOM, submit, approve, implement, close, release) in S/4HANA Cloud 2608."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/change-records]
aliases: [64E_S4CLD2608_BPD_EN_AE]
keywords: [Product Change Management with Change Records, change records, product change management, change record status flow, bill of material changes, change request approval, change record profile, classification setup, business roles, test scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/64E_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1149
topic: 12-production-and-manufacturing/change-records
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Product Change Management with Change Records (64E_AE) - SAP S/4HANA Cloud Public Edition 2608 (64E_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/64E_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Product Change Management with Change Records** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Product Change Management with Change Records (64E_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232857422)

[2 Prerequisites 4](#_Toc232857423)

[2.1 System Access 4](#_Toc232857424)

[2.2 Roles 4](#_Toc232857425)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232857426)

[2.4 Business Conditions 6](#_Toc232857427)

[2.5 Preliminary Steps 7](#_Toc232857428)

[2.5.1 Create Characteristic 7](#_Toc232857429)

[2.5.2 Create Class 8](#_Toc232857430)

[2.5.3 Define Change Record Profile 9](#_Toc232857431)

[2.5.4 Assign Classification to Change Record Profile 10](#_Toc232857432)

[3 Overview Table 13](#_Toc232857433)

[4 Test Procedures 14](#_Toc232857434)

[4.1 Create Change Record 14](#_Toc232857435)

[4.2 Assign BOM to Change Record 15](#_Toc232857436)

[4.3 Submit Change Request 16](#_Toc232857437)

[4.4 Check Change Request 17](#_Toc232857438)

[4.5 Approve Change Request 18](#_Toc232857439)

[4.6 Start Change Implementation 19](#_Toc232857440)

[4.7 Perform Change Implementation for BOM 20](#_Toc232857441)

[4.7.1 Start Changes for BOM 21](#_Toc232857442)

[4.7.2 Modify BOM 22](#_Toc232857443)

[4.7.3 Changes Completed 23](#_Toc232857444)

[4.7.4 Release Changes for the BOM 24](#_Toc232857445)

[4.8 Close Change Implementation 25](#_Toc232857446)

[4.9 Release Change 26](#_Toc232857447)

[4.10 Appendix 27](#_Toc232857448)

[4.10.1 Process Integration 27](#_Toc232857449)

[4.10.1.1 Preceding Processes 28](#_Toc232857450)

[4.10.1.2 Succeeding Processes 28](#_Toc232857451)

## Purpose

Overview

SAP S/4HANA Cloud Public Edition, product change management with change records flexibly orchestrates the management of enterprise product changes. It can handle several types of objects that are affected by the intended changes, such as materials, BOMs, master recipes, and documents. The change record keeps all information in one place. The progress of the change is controlled by a dedicated status management, and the change process is supported by workflow capabilities of process routing. Collaboration using comments during the change process allows effective communication with all involved parties.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/64E_S4CLD2602_BPD_EN_AE.docx) ). |

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

tW

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| BOM Engineer | SAP_BR_BOM_ENGINEER | Bills Of Material | SAP_BR_BOM_ENGINEER |  |
| Development Manager - Discrete Industries | SAP_BR_DEVELOPMENT_MANAGER_DIN | Change Management | SAP_BR_DEVELOPMENT_MANAGER_DIN |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | FG126 | Finished Good MTS for Discrete Industry (PD planning) |  |
| Material | SG21 | SEMI21,PD,RepetitiveManuf. |  |
| Material | SG22 | SEMI22,PD,Phantom |  |
| Material | RM122 | RAW122,PD,Batch-Fifo,ProcureImport |  |
| Material | RM128 | RAW128,PD,Consignment |  |
| Material | RM120 | RAW120,PD,QualityManaged |  |
| Material | SG23 | SEMI23,PD,Subcontracting |  |
| Material | SG25 | SEMI25,PD,ExternalProcurement |  |
| Material | SG124 | SEMI124,PD,Subassembly |  |
| Material | RM20 | RAW20,PD |  |
| Material | RM27 | RAW27,PD,PackagingBox |  |
| Engineering Bill of Material |  |  | The Engineering Bill of Material is created in scope item 64F, which is a prerequisite scope item. |
| Document |  |  | The Document that will be assigned in this test script is created in scope item 64F, which is a prerequisite scope item.Document ID: ________________________________ |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNR | Create Product Master of type "Raw Material" - MDS (“ROH”) |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS (“HALB”) |
| BNT | Create Product Master of type "Finished Good" - MDS (“FERT”) |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 64F - Bill of Material Management | Bill of Material Management needs to be created as prerequisite. This Bill of Material Management is used in this scope item, 64E, as sample data for demonstrating the change record process. Also, the document ID of the attachment that was added to this Engineering Bill of Material must be available. |
| 1NJ - Responsibility Management | A team needs to be created in the app Manage Teams and Responsibilities (F2412) to determine the responsibilities for approving change records. Refer to test script 1NJ- Responsibility Management for a step-by-step description.Set up the team with the following values:Team Name TEAM_SCR1_001Team Status Ready to UseTeam Type SCR1Members:User Name → FunctionBOM_ENGINEER → SBOM_ENGDESIGN_ENGINEER → SDES_ENGDEVELOPMENT_MANAGER → SDEV_MGRNote The user names in your organization will differ. Assign corresponding users within that are working in these roles. Also multiple users can be assigned to the same Function. |

### Preliminary Steps

#### Create Characteristic

Purpose

Use this procedure to create characteristics for your business processes.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Manage Characteristics (CT04) app. | The Characteristics screen displays. |  |
| 3 | Enter the Characteristic Name | Make the following entry and choose the Create icon.Characteristic: <Characteristic name> | The Create Characteristic screen displays. |  |
| 4 | Enter Basic Data | On the Basic data tab, make the following entries.Basic data section:Description: <A valid description>Status: Released (default)Format section:Data Type: <A valid data type>Number of Chars: <A valid number of Char>Decimal Places: <A valid decimal place> |  |  |
| 5 | Enter the values | On the Values tab, in the Allowed Values section, enter your own values:Char. Value:XXXX (User preferred Value) |  |  |
| 6 | Save the Characteristic | Choose Save. | The characteristic is created. |  |

#### Create Class

Purpose

In this process step, you create a class with class type – 106.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Classes (CL02). | The Class screen displays. |  |
| 3 | Enter the Class name | Make the following entries and choose the Create icon.Class: <Any valid class>Class Type: 106 | The Create Class screen displays. |  |
| 4 | Enter Basic Data | On the Basic data tab, make the following entries.Basic data section:Description: Assign the characteristic created in the Create Characteristic sectionStatus: Released (Default)Same classification section:Choose Do not check (Default) |  |  |
| 5 | Enter Char. | On the Char. tab, make the following entry.Char.:<Your valid characteristic value> |  |  |
| 6 | Save the Class | Choose Save. | The class is created. |  |

#### Define Change Record Profile

Purpose

This procedure allows you to define change record profile.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution and make the following entries:Note To create country-/region-dependent settings for the intended local version, choose Set Local Version.Application Area: Select R&D EngineeringSub Application Area: Select Project Control and Product DevelopmentChoose the filtered row, find the step Define Change Record Profile and choose Configure. | The Define Change Record Profile screen displays. |  |
| 4 | Create the Entry | Choose New Entries.Enter the following details:ChgRecdPrf: <As per user Preference>Change Record Profile Description: <Any valid description> | The change record profile is defined. |  |
| 5 | Save the Entries | Choose Save. | Data is saved. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Configuration Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Change Record Profile.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Change Record Profile screen displays. |  |
| 3 | Create the Entry | Choose New Entries.Enter the following details:ChgRecdPrf: <As per user Preference>Change Record Profile Description: <Any valid description> | The change record profile is defined. |  |
| 4 | Save the Entries | Choose Save. | The data is saved. |  |

#### Assign Classification to Change Record Profile

Purpose

This procedure allows you to assign classification to change record profile.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution and make the following entries:Note To create country-/region-dependent settings for the intended local version, choose Set Local Version.Application Area: Select R&D EngineeringSub Application Area: Select Project Control and Product DevelopmentChoose the filtered row, find the step Assign Classification to Change Record Profile and choose Configure. | The Assign Classification to Change Record Profile screen displays. |  |
| 4 | Create the Entry | Choose New Entries.Enter the following details:ChgRecdPrf: Assign the change record profile created in the step [Define Change Record Profile](#unique_9) [page ] 9.Class Type: 106Class: Assign the class created in the step [Create Class](#unique_8) [page ] 8. | A classification to change record profile is assigned. |  |
| 5 | Save the Entries | Choose Save. | Data is saved. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Configuration Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Classification to Change Record Profile.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Classification to Change Record Profile screen displays. |  |
| 3 | Create the Entry | Choose New Entries.Enter the following details:ChgRecdPrf: Assign the change record profile created in the step [Define Change Record Profile](#unique_9) [page ] 9.Class Type: 106Class: Assign the class created in the step [Create Class](#unique_8) [page ] 8. | The Assign Classification to Change Record Profile screen displays. |  |
| 4 | Save the Entries | Choose Save. | The data is saved. |  |

## Overview Table

This scope item consists of several process steps, provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App / Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Change Record](#unique_12) [page ] 14 | Development Manager - Discrete Industries | Manage Change Records (Version 2) (F2097A) | A new Change Master is created. |
| [Assign BOM to Change Record](#unique_13) [page ] 15 | BOM Engineer | Manage Change Records (Version 2) (F2097A) | A new Bill of Material managed with a Change Master is created. |
| [Submit Change Request](#unique_14) [page ] 16 | BOM Engineer | Manage Change Records (Version 2) (F2097A) | Change Master Status is set to Inactive. |
| [Check Change Request](#unique_15) [page ] 17 | Development Manager - Discrete Industries | Manage Change Records (Version 2) (F2097A) | Bill of Material is changed via Change Master. |
| [Approve Change Request](#unique_16) [page ] 18 | Development Manager - Discrete Industries | Manage Change Records (Version 2) (F2097A) | Change Master Status is set to Inactive. |
| [Start Change Implementation](#unique_17) [page ] 19 | Development Manager - Discrete Industries | Manage Change Records (Version 2) (F2097A) | A new material is created. |
| [Perform Change Implementation for BOM](#unique_18) [page ] 20 | BOM Engineer | Manage Change Records (Version 2) (F2097A) | A new Change Master is created. |
| [Close Change Implementation](#unique_19) [page ] 25 | Development Manager - Discrete Industries | Manage Change Records (Version 2) (F2097A) | Copied Bill of Material is created. |
| [Release Change](#unique_20) [page ] 26 | Development Manager - Discrete Industries | Manage Change Records (Version 2) (F2097A) | Bill of Material is discarded. |

## Test Procedures

### Create Change Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Development Manager creates a Change Record.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 2 | Log On | Log on to the SAP Fiori launchpad as a Development Manager - Discrete Industries |  |  |
| 3 | Access App | Open the Manage Change Records (Version 2) (F2097A) app. | The Manage Change Records screen displays. |  |
| 4 | Create Change Record | Choose Create Change Record in the upper-right corner above the Change Records table. | The change record type Discrete Industry Change is displayed. |  |
| 5 | Choose Change Record Type | Select Discrete Industry Change. | The Change Record screen is displayed. |  |
| 6 | Maintain Change Record Header | On the Header Details tab, make entries similar to the following example and press Enter:Description: To create change recordIn the General Information section:Detailed Description: To create change record |  |  |
| 7 | Upload Attachments | Under the Attachments tab, choose Upload.Select the files that you want to upload, and choose OK. | The attachment is uploaded. |  |
| 8 | Maintain Class (Optional) | Before proceeding, ensure that all the steps outlined in the Preliminary Steps section have been completed:[Create Characteristic](#unique_7) [page ] 7[Create Class](#unique_8) [page ] 8[Define Change Record Profile](#unique_9) [page ] 9[Assign Classification to Change Record Profile](#unique_10) [page ] 10Classification tab:Navigate to the Classification tab and maintain the following:Choose Assign Class and select the class created in the [Create Class](#unique_8) [page ] 8 step.If applicable, select the appropriate characteristic values defined in the [Create Characteristic](#unique_7) [page ] 7 step. | The class is assigned. |  |
| 9 | Choose Create | On the Change Record screen, choose Create. | The Change Record is created. |  |

### Assign BOM to Change Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The BOM Engineer adds Bill Of Material (BOM) to the change record which is created by the Development Manager - Discrete Industries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer |  |  |
| 2 | Access App | Open the Manage Change Records (Version 2) (F2097A) app. |  |  |
| 3 | Choose the Change Record | Change Record: Type the Change Record number which is created in[Create Change Record](#unique_12) [page ] 14Choose Go.Choose the arrow on the right of the change record. |  |  |
| 4 | Add BOM | Choose Edit on the top right corner of the Change Record page.In the Items section dropdown, choose Bill Of Material.Choose Create in the upper-right corner of the Bill Of Material section and make the following entries:Material : FG126(Choose FG126 again from the dropdown list that appears after you enter FG126 as the material.)Relevance:ChangeProcessing Status: Change PossibleSelect the Material BOM by clicking on the arrow on the extreme right to open the processing status on the screen. Choose Apply after selecting the processing status. | The BOM is added to the change record. |  |
| 5 | Choose Save | On the Change Record screen, choose Save. | The Change Record is saved. |  |

### Submit Change Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The BOM Engineer reviews and submits the change request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer |  |  |
| 2 | Access App | Open the Manage Change Records (Version 2) (F2097A) app. |  |  |
| 3 | Choose the Change Record | Change Record: Type the Change Record number which is created in[Create Change Record](#unique_12) [page ] 14Choose Go.Choose the arrow on the right of the change record. |  |  |
| 4 | Enter Edit Mode | Choose Edit in the top-right corner of the Change Record page | Change Record is in edit mode |  |
| 5 | Choose Task | Choose Change Status in the upper-right corner of the Change Records header. |  |  |
| 6 | Approve the Change Record | Choose Submit Change Request. | You get a message saying that the change request is successfully changed to the next status.The record status is changed to Change Request in Review. |  |
| 7 | Save | On the Change Record screen choose Save | The Change Record is saved. |  |

### Check Change Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Development Manager - Discrete Industries, changes the status to 'Change Request Checked'.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Development Manager - Discrete Industries |  |  |
| 2 | Access App | Open the Manage Change Records (Version 2) (F2097A) app. |  |  |
| 3 | Choose the Change Record | Change Record: Type the Change Record number which is created in[Create Change Record](#unique_12) [page ] 14Choose GoChoose the arrow on the right of the change record. |  |  |
| 4 | Enter Edit Mode | Choose Edit in the top-right corner of the Change Record page | Change Record is in edit mode |  |
| 5 | Choose Task | Choose Change Status in the upper-right corner of the Change Records header. |  |  |
| 6 | Approve the Change Record | Choose Change Request Checked. | You get a message saying the change request is changed to the next status.The record status is changed to Request Ready for Approval. |  |
| 7 | Save | On the Change Record screen choose Save | The Change Record is saved. |  |

### Approve Change Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Development Manager - Discrete Industries changes the status to 'Approve Change Request'.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Development Manager - Discrete Industries |  |  |
| 2 | Access App | Open the Manage Change Records (Version 2) (F2097A) app. |  |  |
| 3 | Choose the Change Record | Change Record: Type the Change Record number which is created in[Create Change Record](#unique_12) [page ] 14Choose GoChoose the arrow on the right of the Change Record |  |  |
| 4 | Enter Edit Mode | Choose Edit in the top-right corner of the Change Record page | Change Record is in edit mode |  |
| 5 | Choose Task | Choose Change Status in the upper-right corner of the Change Records header. |  |  |
| 6 | Approve the Change Record | Choose Approve Change Request | You get a message saying that the change request is successfully changed to the next status.Record Status is changed to Change Request Approved. |  |
| 7 | Save | On the Change Record screen choose Save | The Change Record is saved. |  |

### Start Change Implementation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Development Manager - Discrete Industries, changes the status to 'Start Change Implementation'.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Development Manager - Discrete Industries. |  |  |
| 2 | Access App | Open the Manage Change Records (Version 2) (F2097A) app. |  |  |
| 3 | Choose the Change Record | Change Record: Type the Change Record number which is created in[Create Change Record](#unique_12) [page ] 14Choose GoChoose the arrow on the right of the Change Record. |  |  |
| 4 | Enter Edit Mode | Choose Edit in the top-right corner of the Change Record page | Change Record is in edit mode |  |
| 5 | Choose Task | Choose Change Status in the upper-right corner of the Change Records header. |  |  |
| 6 | Approve the Change Record | Choose Start Change Implementation. | You get a message saying that the change record is successfully changed to the next status.The record Status is changed to Change In Process.Change Number is created. |  |
| 7 | Save | On the Change Record screen, choose Save. | The Change Record is saved. |  |

### Perform Change Implementation for BOM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The BOM Engineer updates the BOM and releases the BOM changes.

#### Start Changes for BOM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The BOM Engineer changes the status of BOM to 'change started'.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer. |  |  |
| 2 | Access App | Open the Manage Change Records (Version 2) (F2097A) app. |  |  |
| 3 | Choose the Change Record | Change Record: Type the Change Record number which is created in[Create Change Record](#unique_12) [page ] 14Choose GoChoose the arrow on the right of the Change Record | Change Record opens |  |
| 4 | Enter Edit Mode | Choose Edit in the top-right corner of the Change Record page | Change Record is in edit mode |  |
| 5 | Change Completed | In the Items section, under Bill Of Material , do the following:Select the checkbox.Choose the arrow icon on the right of the Material BOM.Choose Change Processing Status in the upper-right corner above the Material BOM's table.Choose Change Started. | The Processing Status of the BOM is changed to Change Started. |  |
| 6 | Save | On the Change Record screen choose Save. | The Change Record is saved. |  |

#### Modify BOM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The BOM Engineer changes the Master Recipe.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer |  |  |
| 2 | Access App | Open the Manage Change Records (Version 2) (F2097A) app. |  |  |
| 3 | Choose the Change Record | Change Record: Type the Change Record number which is created in [Create Change Record](#unique_12) [page ] 14Choose GoChoose the arrow on the right of the change record. | The change record opens. |  |
| 4 | Navigate to change the BOM | On the Change Record screen, choose the Items tab.From the Items dropdown list, choose Bill of Material.In the Bill Of Material table, click on the material link.Select Maintain Bill Of material from the dropdown list.Open the Maintain Bill Of Material (Version 2) app.To change the Bill of Material, follow the steps that are described in the test procedure 'Bill of Material Management' of the 64F- Bill of Material Management scope item.Select the Material Bills of Material displayed in the Maintain Bill of Material screen by clicking on the right most arrow in that row. | The Change Material BOM app is displayed. |  |
| 5 | Modify Base Quantity | Choose Edit and select Edit from the dropdown list.Choose the Components tabChoose 0010 BOM Itemfrom the table and change the Component Quantity to 200Choose SaveChoose Back to go back to the Manage Change Records app. | You get a message saying that the BOM FG126 is saved.The Manage Change Records app is displayed. |  |

#### Changes Completed

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the BOM Engineer closes changes implementation

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer. |  |  |
| 2 | Access App | Open the Manage Change Records (Version 2) (F2097A) app. |  |  |
| 3 | Choose the Change Record | Change Record: Type the Change Record number which is created in step[Create Change Record](#unique_12) [page ] 14Choose GoChoose the arrow on the right of the Change Record | The change record opens |  |
| 4 | Enter Edit Mode | Choose Edit in the top-right corner of the Change Record page | Change Record is in edit mode |  |
| 5 | Change Completed | In the Items section, inside Bill Of Material, do the following:Select the material check box..Choose the Change Processing Status button in the upper-right above the BOM table.Choose Change Completed | The Processing Status of the BOM status changed to Change Completed. |  |
| 6 | Save | On the Change Record screen choose Save | The Change Record is saved. |  |

#### Release Changes for the BOM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The BOM Engineer changes the status to 'changes released'.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer. |  |  |
| 2 | Access App | Open the Manage Change Records (Version 2) (F2097A) app. |  |  |
| 3 | Choose the Change Record | Change Record: Type the change record number which is created in[Create Change Record](#unique_12) [page ] 14Choose GoChoose the arrow on the right of the change record. | The change record opens. |  |
| 4 | Enter Edit Mode | Choose Edit in the top-right corner of the Change Record page. | Change Record is in edit mode |  |
| 5 | Change Completed | In the Items section, under BOM, do the following:Select the check box.Choose Change Processing Status in the upper-right corner above the BOM table.Choose Change Released. | The Processing Status of the BOM is changed to Change Released. |  |
| 6 | Save | On the Change Record screen, choose Save. | The Change Record is saved. |  |

### Close Change Implementation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Development Manager - Discrete Industries changes the status to 'Close Change Implementation'.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Development Manager - Discrete Industries. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open the Manage Change Records (Version 2) (F2097A) app. |  |  |
| 3 | Choose the Change Record | Change Record: Type the change record number which is created in [Create Change Record](#unique_12) [page ] 14.Choose Go.Choose the arrow on the right of the Change Record. |  |  |
| 4 | Enter Edit Mode | Choose Edit in the top-right corner of the Change Record page | Change Record is in edit mode |  |
| 5 | Choose Task | Choose Change Status in the upper-right corner of the Change Records header. |  |  |
| 6 | Approve the Change Record | Choose Close Change Implementation | You get a message saying that the change record is successfully Changed to the next status. The record status is changed to Change Closed. |  |
| 6 | Save | On the Change Record screen choose Save. | The Change Record is saved. |  |

### Release Change

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Development Manager - Discrete Industries changes the status to 'release change'

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Development Manager - Discrete Industries. |  |  |
| 2 | Access App | Open the Manage Change Records (Version 2) (F2097A) app. |  |  |
| 3 | Choose the Change Record | Change Record: Type the change record number which is created in [Create Change Record](#unique_12) [page ] 14Choose Go.Choose arrow on the right of the change record. |  |  |
| 4 | Check Change Record | Choose Change Record and click Change Change Master.Check the validity date and go to Objects.Check if the corresponding objects are locked (For Example, in this case all the BOM objects should be locked). You will be redirected to Change Change Master: Material BOM: Overview Screen. | Objects are locked and visible in Change Master |  |
| 5 | Enter Edit Mode | Choose Edit in the top-right corner of the Change Record page | Change Record is in edit mode |  |
| 6 | Approve the Change Record | Under Change Status tab, Choose Release Change. A message is displayed stating that the change record is successfully changed to the next status. | The record status is changed to Change Released. |  |
| 7 | Save | On the Change Record screen choose Save | The Change Record is saved. |  |

### Appendix

#### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

##### Preceding Processes

##### Succeeding Processes

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
> Flagged while digesting this document, not verified: The Overview Table's Expected Results do not match the Test Procedures: e.g. Submit Change Request and Approve Change Request both list 'Change Master Status is set to Inactive', Release Change lists 'Bill of Material is discarded', while the procedures state statuses Change Request in Review, Change Request Approved and Change Released.

## Connections
- part-of :: [[_cluster]]
- see-also :: [[12-production-and-manufacturing/test-script-bill-of-material-management-64f-ae-sap-s-4hana-cloud-publi]]
- see-also :: [[13-quality-ehs-and-compliance/test-script-lean-management-of-change-process-4yx-sap-s-4hana-cloud-pu]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/64E_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 42,586 chars in the whole document
