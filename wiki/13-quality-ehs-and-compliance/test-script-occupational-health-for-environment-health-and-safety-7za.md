---
id: 13-quality-ehs-and-compliance/test-script-occupational-health-for-environment-health-and-safety-7za
title: "Test Script: Occupational Health for Environment, Health, and Safety (7ZA) - SAP S/4HANA Cloud Public Edition (7ZA_S4CLD2608_BPD_EN_XX)"
description: "Test script for scope item 7ZA Occupational Health: prerequisite configuration, then health centers, protocols, appointments and health service requests."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/health-and-safety-and-occupational-health]
aliases: [7ZA_S4CLD2608_BPD_EN_XX]
keywords: [Health and Safety Management and Occupational Health, occupational health, number ranges, location types, preliminary configuration, health protocols, health centers, health service providers, health center appointments, health service requests]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7ZA_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1243
topic: 13-quality-ehs-and-compliance/health-and-safety-and-occupational-health
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Occupational Health for Environment, Health, and Safety (7ZA) - SAP S/4HANA Cloud Public Edition (7ZA_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7ZA_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Health and Safety Management and Occupational Health** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Occupational Health for Environment, Health, and Safety (7ZA) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232792991)

[2 Prerequisites 4](#_Toc232792992)

[2.1 System Access 4](#_Toc232792993)

[2.2 Roles 4](#_Toc232792994)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232792995)

[2.4 Preliminary Steps 5](#_Toc232792996)

[2.4.1 Maintain Number Range for Health Protocol Identifier 5](#_Toc232792997)

[2.4.2 Maintain Number Range for Health Service Request Identifier 6](#_Toc232792998)

[2.4.3 Maintain Number Range for Health Service Request Results Identifier 7](#_Toc232792999)

[2.4.4 Maintain Number Range for Personal Health Card Identifier 8](#_Toc232793000)

[2.4.5 Maintain Number Range for Health Service Item Result Identifier 10](#_Toc232793001)

[2.4.6 Create Location Types for Health Centers and Health Service Providers 11](#_Toc232793002)

[2.4.7 Define Health-Related Location Types 12](#_Toc232793003)

[2.4.8 Specify Roles of Persons Responsible for Locations 13](#_Toc232793004)

[2.4.9 Define Location Roles 14](#_Toc232793005)

[2.4.10 Define Health Protocol Categories 16](#_Toc232793006)

[2.4.11 Define Health Protocol Types 17](#_Toc232793007)

[2.4.12 Define Health Protocol Owners 18](#_Toc232793008)

[2.4.13 Define Health Service Types 19](#_Toc232793009)

[2.4.14 Define Health Service Items 20](#_Toc232793010)

[3 Overview Table 23](#_Toc232793011)

[4 Test Procedures 24](#_Toc232793012)

[4.1 Create Health Service Providers 24](#_Toc232793013)

[4.2 Create Health Centers 25](#_Toc232793014)

[4.3 Manage Health Centers and Service Providers 27](#_Toc232793015)

[4.4 Manage Occupational Health Protocols 28](#_Toc232793016)

[4.5 Set a Health Center as My Location 31](#_Toc232793017)

[4.6 Create a Health Center Appointment in the Default Health Center 32](#_Toc232793018)

[4.7 Refine a Health Center Appointment 34](#_Toc232793019)

[4.8 Manage Health Center Appointments: Change Health Center and Create an Appointment 35](#_Toc232793020)

[4.9 Manage Health Service Requests 37](#_Toc232793021)

[4.10 Display Health Center Appointments in the System 39](#_Toc232793022)

## Purpose

Overview

This scope item supports general employee occupational healthcare in your enterprise and planning and execution of special health protocols. These include fit-for-work examinations, health surveillance, consultations, health campaigns, and more. Special surveillance is required for persons who may be exposed to chemical, physical, or biological influences at their workplace, or who perform activities that pose a health hazard. These processes help that your company always stays up to date with safety standards and compliance obligations.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) |
| --- | --- | --- |
| Master Data Specialist - Occupational Health | SAP_BR_OH_MASTER_DTA_SPCLST | SAP_EHS_SPT_OH_MASTER_DTA_SPCLST_PC |
| Receptionist - Occupational Health | SAP_BR_OH_RECEPTIONIST | SAP_EHS_SPT_OH_RECEPTIONIST_PC |
| Physician - Occupational Health | SAP_BR_OH_PHYSICIAN | SAP_EHS_SPT_OH_PHYSICIAN_PC |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data.

### Preliminary Steps

Before you can start testing, you have to perform the preliminary steps described below.

#### Maintain Number Range for Health Protocol Identifier

In the configuration environment for SAP S/4HANA Cloud Public Edition, you use the application Manage Your Solution and the option Configure Your Solution to choose the activity Maintain Number Range for Health Protocol Identifier (EHOHM_NR_PROTID).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Go to Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Go to Maintain Number Range for Health Protocol Identifier | On the Configure Your Solution screen, search for the following configuration step: Maintain Number Range for Health Protocol Identifier. Choose the magnifying glass icon next to the search field to start the search.In the search result, select the Occupational Health Management configuration activity and navigate to the detail screen.On the Configure Your Solution - Occupational Health Management screen, go to the Maintain Number Range for Health Protocol Identifier configuration step and choose Configure. | The Maintain Number Range for Health Protocol Identifier screen is displayed. |  |
| 5 | Check Number Range Object and go to Intervals | The following number range shall be displayed:EHOHM_PROT Health Protocol IDChoose the button to display Intervals. | The number range intervals for Health Protocol Identifier is displayed. |  |
| 6 | Check Delivered Entry | Check if the following delivered entry exists:Number Range No.: 01From Number: 00000000000000000001To Number: 99999999999999999999NR Status: 0 or higher, depending on test systemExternal: unmarkedIf the entry 01 exists, leave the activity. Choose Cancel. |  |  |
| 7 | Create New Entry | Perform steps 7 to 8 only if the configuration from step 6 is not available.Choose Display <-> Change to switch to change mode.Choose the plus symbol (Insert Line).Maintain the values as described in step 6.Keep the External flag unmarked; do not maintain a value in NR Status. | A dialog appears to make new entries. |  |
| 8 | Save the Entry | Choose Save. | The new entry is saved, and the system responds with a message that the data was saved. |  |

#### Maintain Number Range for Health Service Request Identifier

In the configuration environment for SAP S/4HANA Cloud Public Edition, you use the application Manage Your Solution and the option Configure Your Solution to choose the activity Maintain Number Range for Health Service Request Identifier (EHOHM_NR_SRID).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Go to Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Go to Maintain Number Range for Health Service Request Identifier | On the Configure Your Solution screen, search for the following configuration step: Maintain Number Range for Health Service Request Identifier. Choose the magnifying glass icon next to the search field to start the search.In the search result, select the Occupational Health Management configuration activity and navigate to the detail screen.On the Configure Your Solution - Occupational Health Management screen, go to the Maintain Number Range for Health Service Request Identifier configuration step and choose Configure. | The Maintain Number Range for Health Service Request Identifier screen is displayed. |  |
| 5 | Check Number Range Object and go to Intervals | The following number range is displayed:EHOHM_SR Health Service Request IDChoose the button to display Intervals. | The number range intervals for the health service request identifier are displayed. |  |
| 6 | Check Delivered Entry | Check if the following entry exists:Number Range No.: 01From Number: 00000000000000000001To Number: 99999999999999999999NR Status: 0 or higher, depending on test systemExternal: unmarkedIf entry 01 exists, leave the activity. Choose Cancel. |  |  |
| 7 | Create New Entry | Perform steps 7 to 8 only if the configuration from step 6 is not available.Choose Display <-> Change to switch to change mode.Choose the plus symbol (Insert Line).Maintain the values as described in step 6.Keep the External flag unmarked; do not maintain a value in NR Status. | A dialog appears to make new entries. |  |
| 8 | Save the Entry | Choose Save. | The new entry is saved, and the system responds with a message that the data was saved. |  |

#### Maintain Number Range for Health Service Request Results Identifier

In the configuration environment for SAP S/4HANA Cloud Public Edition, you use the application Manage Your Solution and the option Configure Your Solution to choose the activity Maintain Number Range for Health Service Request Results Identifier (EHOHM_NR_SRRID).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Go to Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Go to Maintain Number Range for Health Service Request Results Identifier | On the Configure Your Solution screen, search for the following configuration step: Maintain Number Range for Health Service Request Results Identifier. Choose the magnifying glass icon next to the search field to start the search.In the search result, select the Occupational Health Management configuration activity and navigate to the detail screen.On the Configure Your Solution - Occupational Health Management screen, go to the Maintain Number Range for Health Service Request Results Identifier configuration step and choose Configure. | The Maintain Number Range for Health Service Request Results Identifier screen is displayed. |  |
| 5 | Check Number Range Object and go to Intervals | The following number range is displayed:EHOHM_SR Health Service Request Results IDChoose the button to display Intervals. | The number range intervals for the health service request results identifier are displayed. |  |
| 6 | Check Delivered Entry | Check if the following entry exists:Number Range No.: 01From Number: 00000000000000000001To Number: 99999999999999999999NR Status: 0 or higher, depending on test systemExternal: unmarkedIf entry 01 exists, leave the activity. Choose Cancel. |  |  |
| 7 | Create New Entry | Perform steps 7 to 8 only if the configuration from step 6 is not available.Choose Display <-> Change to switch to change mode.Choose the plus symbol (Insert Line).Maintain the values as described in step 6.Keep the External flag unmarked; do not maintain a value in NR Status. | A dialog appears to make new entries. |  |
| 8 | Save the Entry | Choose Save. | The new entry is saved, and the system responds with a message that the data was saved. |  |

#### Maintain Number Range for Personal Health Card Identifier

In the configuration environment for SAP S/4HANA Cloud Public Edition, you use the application Manage Your Solution and the option Configure Your Solution to choose the activity Maintain Number Range for Personal Health Card Identifier (EHOHM_NR_PHCID).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Go to Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Go to Maintain Number Range for Personal Health Card Identifier | On the Configure Your Solution screen, search for the following configuration step: Maintain Number Range for Personal Health Card Identifier. Choose the magnifying glass icon next to the search field to start the search.In the search result, select the Occupational Health Management configuration activity and navigate to the detail screen.On the Configure Your Solution - Occupational Health Management screen, go to the Maintain Number Range for Personal Health Card Identifier configuration step and choose Configure. | The Maintain Number Range for Personal Health Card Identifier screen is displayed. |  |
| 5 | Check Number Range Object and go to Intervals | The following number range shall be displayed:EHFND_PHC Personal Health Card IDChoose the button to display Intervals. | The number range intervals for the personal health card identifier are displayed. |  |
| 6 | Check Delivered Entry | Check if the following entry exists:Number Range No.: 01From Number: 00000000000000000001To Number: 99999999999999999999NR Status: 0 or higher, depending on test systemExternal: unmarkedIf entry 01 exists, leave the activity. Choose Cancel. |  |  |
| 7 | Create New Entry | Perform steps 7 to 8 only if the delivery configuration from step 6 is not available.Choose Display <-> Change to switch to change mode.Choose the plus button (Insert Line).Maintain the values as described in step 6.Keep the External flag unmarked; do not maintain a value in NR Status. | A dialog appears to make new entries. |  |
| 8 | Save the Entry | Choose Save. | The new entry is saved, and the system responds with a message that the data was saved. |  |

#### Maintain Number Range for Health Service Item Result Identifier

In the configuration environment for SAP S/4HANA Cloud Public Edition, you use the application Manage Your Solution and the option Configure Your Solution to choose the activity Maintain Number Range for Health Service Item Result Identifier (EHOHM_NR_SIRID).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Go to Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Go to Maintain Number Range for Health Service Item Result Identifier | On the Configure Your Solution screen, search for the following configuration step: Maintain Number Range for Health Service Item Result Identifier. Choose the magnifying glass icon next to the search field to start the search.In the search result, select the Occupational Health Management configuration activity and navigate to the detail screen.On the Configure Your Solution - Occupational Health Management screen, go to the Maintain Number Range for Health Service Item Result Identifier configuration step and choose Configure. | The Maintain Number Range for Health Service Item Result Identifier screen is displayed. |  |
| 5 | Check Number Range Object and go to Intervals | The following number range shall be displayed:EHOHM_SIR Health Service Item Result IDChoose the button to display Intervals. | The number range intervals for the health service item result identifier are displayed. |  |
| 6 | Check Delivered Entry | Check if the following entry exists:Number Range No.: 01From Number: 00000000000000000001To Number: 99999999999999999999NR Status: 0 or higher, depending on test systemExternal: unmarkedIf entry 01 exists, leave the activity. Choose Cancel. |  |  |
| 7 | Create New Entry | Perform steps 7 to 8 only if the configuration from step 6 is not available.Choose Display <-> Change to switch to change mode.Choose the plus symbol (Insert Line).Maintain the values as described in step 6.Keep the External flag unmarked; do not maintain a value in NR Status. | A dialog appears to make new entries. |  |
| 8 | Save the Entry | Choose Save. | The new entry is saved, and the system responds with a message that the data was saved. |  |

#### Create Location Types for Health Centers and Health Service Providers

In the configuration environment for SAP S/4HANA Cloud Public Edition, you use the application Manage Your Solution and the option Configure Your Solution to choose the configuration activity Specify Location Types (EHFND_LOC_TYPE).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Go to Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Go to Specify Location Types | On the Configure Your Solution screen, search for the following configuration step: Specify Location Types. Choose the magnifying glass icon next to the search field to start the search.In the search result, select the Foundation for Environment, Health, and Safety configuration activity and navigate to the detail screen.On the Configure Your Solution - Foundation for Environment, Health, and Safety screen, go to the Specify Location Types configuration step and choose Configure. | The Specify Location Types screen is displayed. |  |
| 5 | Check Delivered Entries | Check if the following delivered entries exist:Location Type: SAP_LTY_HCType Description: Health CenterLocation Type: SAP_LTY_HSPType Description: Health Service ProviderIf the entries exist, leave the activity. Choose Cancel. |  |  |
| 6 | Create New Entries | Perform steps 6 to 9 only if the delivery configuration from step 4 is not available.Choose New Entries. | A dialog appears to make new entries. |  |
| 7 | New Entry: Create Health Center Type | In the first row, enter the following:Location Type: ZEHFND_LTY_HC.Type Description: Health Center. |  |  |
| 8 | New Entry: Create Health Service Provider | In the second row, enter the following:Location Type: EHFND_LTY_HSP.Type Description: Health Service Provider. |  |  |
| 9 | Save the Entries | Choose Save. | The new entries are saved, and the system responds with a message that the data was saved. |  |

#### Define Health-Related Location Types

In the configuration environment for SAP S/4HANA Cloud Public Edition, you use the application Manage Your Solution and the option Configure Your Solution to choose the configuration activity Define Health-Related Location Types (EHOHM_HLOC_TYPE).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Go to Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Go to Define Health-Related Location Types | On the Configure Your Solution screen, search for the following configuration step: Define Health-Related Location Types. Choose the magnifying glass icon next to the search field to start the search.In the search result, select the Occupational Health Management configuration activity and navigate to the detail screen.On the Configure Your Solution - Occupational Health Management screen, go to the configuration step Define Health-Related Location Types and choose Configure. | The Define Health-Related Location Types screen is displayed. |  |
| 5 | Check Delivered Entries | Check if the following delivered entries exist:Health Location Type: 01 Health CenterLocation Type: Health CenterHealth Location Type: 021 Health Service ProviderLocation Type: Health Service ProviderIf the entries exist, leave the activity. Choose Cancel. |  |  |
| 6 | Create New Entries | Perform steps 6 to 9 only if the delivery configuration from step 4 is not available.Choose New Entries. | A dialog appears to make new entries. |  |
| 7 | New Entry: Create Health Center Type | In the first row, select the health location type Health Center from the drop-down menu.Select the location type ZEHFND_LTY_HC - Health Center from the drop-down menu. |  |  |
| 8 | New Entry: Create Health Service Provider | In the second row, select the health location type Health Service Provider from the drop-down menu.Select the location type ZEHFND_LTY_HSP - Health Service Provider from the drop-down menu. |  |  |
| 9 | Save the Entries | Choose Save. | The new entries are saved, and the system responds with a message that the data was saved. |  |

#### Specify Roles of Persons Responsible for Locations

In the configuration environment for SAP S/4HANA Cloud Public Edition, you use the application Manage Your Solution and the option Configure Your Solution to choose the configuration activity Specify Roles of Persons Responsible for Locations (EHFNDV_LOCROLE).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Go to Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Go to Specify Roles of Persons Responsible for Locations | On the Configure Your Solution screen, search for the following configuration step: Specify Roles of Persons Responsible for Locations. Choose the magnifying glass icon next to the search field to start the search.In the search result, select the Foundation for Environment, Health, and Safety configuration activity and navigate to the detail screen.On the Configure Your Solution - Foundation for Environment, Health, and Safety screen, go to the Specify Roles of Persons Responsible for Locations configuration step (ID: 105389) and choose Configure. | The Specify Roles of Persons Responsible for Locations screen is displayed. |  |
| 5 | Check Delivered Entries | Check if the following delivered entries exist. The flag Allow Multiple Persons Responsible should always be marked.Role: SAP_EHSM_OH_NURSEDescription: Occupational Health NurseRole: SAP_EHSM_OH_PHYSICIANDescription: Occupational Health PhysicianRole: SAP_EHSM_OH_RECEPTIONISTDescription: Occupational Health ReceptionistIf the entries exist, leave the activity. Choose Cancel. |  |  |
| 6 | Create New Entries | Perform steps 6 to 7 only if the configuration from step 5 is not available.Choose New Entries.Maintain three values of your own choice. One each for a nurse, a physician and a receptionist. The flag Allow Multiple Persons Responsible should always be marked.You should name the roles Occupational Health Nurse, Occupational Health Physician, and Occupational Health Receptionist.Make a note of the role IDs – you will need them later. | A dialog appears to make new entries. |  |
| 7 | Save the Entries | Choose Save. | The new entries are saved, and the system responds with a message that the data was saved. |  |

#### Define Location Roles

In the configuration environment for SAP S/4HANA Cloud Public Edition, you use the application Manage Your Solution and the option Configure Your Solution to choose the activity Define Location Roles (EHFND_LOC_OHROL).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Go to Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Go to Define Location Roles | On the Configure Your Solution screen, search for the following configuration step: Define Location Roles. Choose the magnifying glass icon next to the search field to start the search.In the search result, select the Occupational Health Management configuration activity and navigate to the detail screen.On the Configure Your Solution - Occupational Health Management screen, go to the Define Location Roles configuration step and choose Configure. | The Define Location Roles screen is displayed. |  |
| 5 | Check Delivered Entries | Check if the following entries exist:Location Role Code: Occupational Health NurseRole: Occupational Health NurseLocation Role Code: Occupational Health PhysicianRole: Occupational Health PhysicianLocation Role Code: Occupational Health ReceptionistRole: Occupational Health ReceptionistIf the entries exist, leave the activity. Choose Cancel. |  |  |
| 6 | Create New Entries | Perform steps 6 to 9 only if the delivery configuration from step 5 is not available.Choose New Entries. | A dialog appears to make new entries. |  |
| 7 | New Entry: Create Assignment for Occupational Health Nurse | In the first row, select the Location Role Code Occupational Health Nurse from the drop-down menu or the role you created manually for this purpose. |  |  |
| 8 | New Entry: Create Assignment for Occupational Health Physician | In the second row, select the Location Role Code Occupational Health Physician from the drop-down menu or the role you created manually for this purpose. |  |  |
| 9 | New Entry: Create Assignment for Occupational Health Receptionist | In the third row, select the Location Role Code Occupational Health Receptionist from the drop-down menu or the role you created manually for this purpose. |  |  |
| 10 | Save the Entries | Choose Save. | The new entries are saved, and the system responds with a message that the data was saved. |  |

#### Define Health Protocol Categories

In the configuration environment for SAP S/4HANA Cloud Public Edition, you use the application Manage Your Solution and the option Configure Your Solution to choose the activity Define Health Protocol Categories (EHOHM_PROT_CAT).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Go to Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Go to Define Health Protocol Categories | On the Configure Your Solution screen, search for the following configuration step: Define Health Protocol Categories. Choose the magnifying glass icon next to the search field to start the search.In the search result, select the Occupational Health Management configuration activity and navigate to the detail screen.On the Configure Your Solution - Occupational Health Management screen, go to the Define Health Protocol Categories configuration step and choose Configure. | The Define Health Protocol Categories screen is displayed. |  |
| 5 | Check Delivered Entries | Check if the following delivered entries exist. The flag Inactive should always be unmarked:Health Protocol Category IDHealth Protocol Category NameInactiveSAP_HPC_CAMPHealth CamgaignSAP_HPC_EXAMFit-for-Duty ExaminationSAP_HPC_PROTHealth Surveillance ProtocolSAP_HPC_SCREHealth ScreeningIf the entries exist, leave the activity. Choose Cancel. |  |  |
| 6 | Create New Entries | Perform steps 6 to 7 only if the configuration from step 5 is not available.Choose New Entries.Maintain four values on your own choice for the ID.You should use the names as described in step 5.Make a note of the category IDs – you might need them later. | A dialog appears to make new entries. |  |
| 7 | Save the Entries | Choose Save. | The new entries are saved, and the system responds with a message that the data was saved. |  |

#### Define Health Protocol Types

In the configuration environment for SAP S/4HANA Cloud Public Edition, you use the application Manage Your Solution and the option Configure Your Solution to choose the activity Define Health Protocol Types (EHOHM_PROT_TYPE).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Go to Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Go to Define Health Protocol Types | On the Configure Your Solution screen, search for the following configuration step: Define Health Protocol Types. Choose the magnifying glass icon next to the search field to start the search.In the search result, select the Occupational Health Management configuration activity and navigate to the detail screen.On the Configure Your Solution - Occupational Health Management screen, go to the Define Health Protocol Types configuration step and choose Configure. | The Define Health Protocol Types screen is displayed. |  |
| 5 | Check Delivered Entries | Check if the following delivered entries exist. The flag Inactive should always be unmarked:Health Protocol Type IDHealth Protocol Type NameInactiveMandatorySAP_HPT_MANDMandatoryXSAP_HPT_OFFROfferedSAP_HPT_REQUOn RequestIf the entries exist, leave the activity. Choose Cancel. |  |  |
| 6 | Create New Entries | Perform steps 6 to 7 only if the configuration from step 5 is not available.Choose New Entries.Maintain three values of your own choice for the ID.Use the names as described in step 5.Set the Mandatory flags as described in step 5.Make a note of the type IDs – you might need them later. | A dialog appears to make new entries. |  |
| 7 | Save the Entries | Choose Save. | The new entries are saved, and the system responds with a message that the data was saved. |  |

#### Define Health Protocol Owners

In the configuration environment for SAP S/4HANA Cloud Public Edition, you use the application Manage Your Solution and the option Configure Your Solution to choose the activity Define Health Protocol Owners (EHOHM_PROT_OWNR).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Go to Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Go to Define Health Protocol Owners | On the Configure Your Solution screen, search for the following configuration step: Define Health Protocol Owners. Choose the magnifying glass icon next to the search field to start the search.In the search result, select the Occupational Health Management configuration activity and navigate to the detail screen.On the Configure Your Solution - Occupational Health Management screen, go to the Define Health Protocol Owners configuration step and choose Configure. | The Define Health Protocol Owners screen is displayed. |  |
| 5 | Check Delivered Entries | Check if the following delivered entries exist. The flag Inactive should always be unmarked:Health Protocol Owner IDHealth Protocol Owner NameInactiveSAP_HPO_INTInternalSAP_HPO_EXTExternalIf the entries exist, leave the activity. Choose Cancel. |  |  |
| 6 | Create New Entries | Perform steps 6 to 7 only if the configuration from step 5 is not available.Choose New Entries.Maintain two values on your own choice for the ID.Use the names as described in step 5.Make a note of the owner IDs – you might need them later. | A dialog appears to make new entries. |  |
| 7 | Save the Entries | Choose Save. | The new entries are saved, and the system responds with a message that the data was saved. |  |

#### Define Health Service Types

In the configuration environment for SAP S/4HANA Cloud Public Edition, you use the application Manage Your Solution and the option Configure Your Solution to choose the activity Define Health Service Types (EHOHM_SRV_TYPE).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Go to Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Go to Define Health Service Types | On the Configure Your Solution screen, search for the following configuration step: Define Health Service Types. Choose the magnifying glass icon next to the search field to start the search.In the search result, select the Occupational Health Management configuration activity and navigate to the detail screen.On the Configure Your Solution - Occupational Health Management screen, go to the Define Health Service Types configuration step and choose Configure. | The Define Health Service Types screen is displayed. |  |
| 5 | Check Delivered Entries | Check if the following entries exist. The flag Inactive should always be unmarked:Health Service Type IDHealth Service Type NameInactiveSAP_HST_PRWAPre-Work AssessmentSAP_HST_INEXInitial ExaminationSAP_HST_FUEXFollow-up ExaminationSAP_HST_INCOInitial ConsultationSAP_HST_FUCOFollow-up ConsultationSAP_HST_SIASSingle AssignmentSAP_HST_EODAEnd-of-Duty AssessmentSAP_HST_POWAPost-Work AssessmentIf the entries exist, leave the activity. Choose Cancel. |  |  |
| 6 | Create New Entries | Perform steps 6 to 7 only if the configuration from step 5 is not available.Choose New Entries.Maintain the values from step 5 of your own choice for the ID.Use the names as described in step 5.Make a note of the owner IDs – you might need them later. | A dialog appears to make new entries. |  |
| 7 | Save the Entries | Choose Save. | The new entries are saved, and the system responds with a message that the data was saved. |  |

#### Define Health Service Items

In the configuration environment for SAP S/4HANA Cloud Public Edition, you use the application Manage Your Solution and the option Configure Your Solution to choose the activity Define Health Service Items (EHOHM_SRV_ITEM).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Go to Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Go to Define Health Service Items | On the Configure Your Solution screen, search for the following configuration step: Define Health Service Items. Choose the magnifying glass icon next to the search field to start the search.In the search result, select the Occupational Health Management configuration activity and navigate to the detail screen.On the Configure Your Solution - Occupational Health Management screen, go to the Define Health Service Items configuration step and choose Configure. | The Define Health Service Items screen is displayed. |  |
| 5 | Check Delivered Entries | Check if the following entries exist. The flag Inactive should always be unmarked:Health Service Item IDHealth Service Item NameHealth Service Item CategoryInactiveSAP_HSI_ADT_ADTAlcohol and Drug TestAlcohol and Drug TestSAP_HSI_ANA_OCCOccupational Health HistoryAnamnesisSAP_HSI_ANA_OWNOwn Health HistoryAnamnesisSAP_HSI_ANA_FAMFamily Health HistoryAnamnesisSAP_HSI_AUD_AUDIOAudiometryAudiometrySAP_HSI_CON_HSUVHealth Surveillance ConsultationConsultationSAP_HSI_CON_ERGOErgonomic ConsultationConsultationSAP_HSI_CON_CHEMChemicals ConsultationConsultationSAP_HSI_CON_TRAVTravel ConsultationConsultationSAP_HSI_DIA_PREPre-DiagnosisDiagnosisSAP_HSI_LEX_CBCComplete Blood CountLaboratory ExaminationSAP_HSI_LEX_CBCSComplete Blood Count without DifferentialLaboratory ExaminationSAP_HSI_LEX_URINUrinalysisLaboratory ExaminationSAP_HSI_MED_PAINPain RelieverMedicationSAP_HSI_MED_COGHCough MedicineMedicationSAP_HSI_MED_EAREar DropsMedicationSAP_HSI_MRI_MRIMRI - HeadMRISAP_HSI_PEX_BODYBody ValuesPhysical ExaminationSAP_HSI_PEX_LUNGLung Function TestPhysical ExaminationSAP_HSI_PEX_MUSCMuscle Function TestPhysical ExaminationSAP_HSI_PEX_VISVision TestVision TestSAP_HSI_XRY_ARMX-Ray - ArmX-RaySAP_HSI_XRY_LEGX-Ray - LegX-RaySAP_HSI_XRY_THRXX-Ray - ThoraxX-RaySAP_HSI_VAC_FLUFlu-ShotVaccinationSAP_HSI_VAC_COVCovid VaccinationVaccinationSAP_HSI_VAC_YEFYellow Fever VaccinationVaccinationIf the entries exist, leave the activity. Choose Cancel. |  |  |
| 6 | Create New Entries | Perform steps 6 to 7 only if the configuration from step 5 is not available.Choose New Entries.Maintain the values from step 5 with your own choice for the IDs.Use the names as described in step 5.Assign the health service item categories as described in step 5.Make a note of the item IDs – you might need them later. | A dialog appears to make new entries. |  |
| 7 | Save the Entries | Choose Save. | The new entries are saved, and the system responds with a message that the data was saved. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Health Service Providers](#unique_22) [page ] 24 | Manage Master Data – Occupational Health | Manage Health Center Structure | A health service provider is created. |
| [Create Health Centers](#unique_23) [page ] 25 | Manage Master Data – Occupational Health | Manage Health Center Structure | A health center is created and persons in dedicated roles are assigned. |
| [Manage Health Centers and Service Providers](#unique_24) [page ] 27 | Manage Master Data – Occupational Health | Manage Health Centers and Service Providers | Data from health centers and / or health service providers will be adopted and saved. |
| [Manage Occupational Health Protocols](#unique_25) [page ] 28 | Manage Master Data – Occupational Health | Manage Occupational Health Protocols | Health protocols for occupational health processes are created. |
| [Set a Health Center as My Location](#unique_26) [page ] 31 | Receptionist – Occupational Health | Manage Health Center Structure | A health center has been assigned as “My Location” to have it as default health center in the appointment calendar. |
| [Create a Health Center Appointment in the Default Health Center](#unique_27) [page ] 32 | Receptionist – Occupational Health | Manage Health Center Ap-pointments | A health service request is created together with its appointment data in the health center assigned as “My Location”. |
| [Refine a Health Center Appointment](#unique_28) [page ] 34 | Receptionist – Occupational Health | Manage Health Center Ap-pointments | A health service request and its appointment data are adapted in the default health center. |
| [Manage Health Center Appointments: Change Health Center and Create an Appointment](#unique_29) [page ] 35 | Receptionist – Occupational Health | Manage Health Center Ap-pointments | Switch to a different health center than the one set as “My Location” and create an appointment. |
| [Manage Health Service Requests](#unique_30) [page ] 37 | Physician – Occupational Health | Manage Health Service Requests | A health service request is processed, and health-related person-specific data is maintained. |
| [Display Health Center Appointments in the System](#unique_31) [page ] 39 | Receptionist – Occupational Health or Physician – Occupational Health | Monitor Health Center Ap-pointments | Display health service request appointments that are saved in the system. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Health Service Providers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

The occupational health service items or treatments executed during a health service request are provided by a health service provider. Health service providers are represented by EHS locations. Thus, you must create locations first with the location type Health Service Provider.

The following steps assume that there are no health service providers in your system yet. If there are already health service providers, you can skip this section. In this case, in the following sections, choose one of the already existing health service providers to perform the processes in Occupational Health.

The creation of locations is only possible in the hierarchy view for EHS locations.

Procedure

Create a Health Service Provider

| Step | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Occupational Health. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Start the Manage Health Center Structure app. | The initial screen of the app is displayed. |  |
| 3 | Create a New Location Structure | Choose New. | A dialog to enter the relevant information is displayed. |  |
| 4 | Enter Relevant Data | Enter the following data:Location: UXT HSP WalldorfLocation Type: HealthServiceProviderRevision Start Date: <today's date>Country: DE |  |  |
| 5 | Save Your Entries | Choose Save.You can ignore the warning that no country/region was entered if you did not enter a country on the address tab. |  |  |
| 6 | Return to Location Structure | Choose Return to Location Structure. |  |  |
| 7 | Choose Created Location / Health Service Provider | Choose Set Status and select Active. Choose Save. | The adopted data is saved to the database. |  |

Result

A health service provider was created and is visible as a new structure root.

### Create Health Centers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

Health centers are the locations where health-related treatments (service items) are performed. Health centers are represented by EHS locations. Thus, you must first create locations with the location type Health Service Provider and assign a Health Center to them.

The following steps assume that there are no health centers in your system yet. If there are already health centers, you can skip this section. In this case, in the following sections, choose one of the already existing health centers to perform the processes in Occupational Health.

Procedure

| Step | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select the Previously Created Health Service Provider | Select the previously created location UXT HSP Walldorf.This is done in the Manage Health Center Structure app.If you don’t see this location, choose Show All Locations first. |  |  |
| 2 | Create a New Health Center | Choose New.This creates a new location (health center) hierarchically below the selected location (health service provider). | A dialog to enter the relevant information is displayed. |  |
| 3 | Enter Relevant Data | Enter the following data:Location: Health Center WalldorfLocation Type: Health CenterRevision Start Date: <today's date>Country: DE |  |  |
| 4 | Enter Person Responsible | On the Persons Responsible tab, make the following entries in an empty line:Name: Enter your own business userRole: OH Physician |  |  |
| 5 | Select the New Entry | Select the radio button of the new entry in the first column. |  |  |
| 6 | Assign Calendar Type | Choose the Calendar Types button.In the Calendar Types pop-up, select the following entries:Calendar Type: Medical ExaminationsCalendar Type: Psychological ExaminationsChoose OK to accept the assignment. |  |  |
| 7 | Create Three Additional Role Assignments | Repeat the steps described under 4, 5, and 6 to create three additional entries with the following values:First entry:Name: Enter your own business userRole: OH NurseCalendar Type: CombinedSecond entry:Name: Enter your own business userRole: OH ReceptionistCalendar Type:Psychological ExaminationsThird entry:Name: Enter a business user other than your ownRole: OH PhysicianCalendar Type: Medical Examinations |  |  |
| 8 | Save Your Entries | Choose Save.You can ignore the warning that no country/region was entered. |  |  |
| 9 | Return to Location Structure | Choose Return to Location Structure. |  |  |
| 10 | Choose Created Location | Choose Set Status and select Active. Choose Save. | The adopted data is saved to the database |  |

Result

You created a health center with two medical physicians, one psychologist and one receptionist for the health center.

### Manage Health Centers and Service Providers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

Health centers are driven by health service providers. There might be internal or external service providers. In any case, the health centers must be assigned to their service providers by using the EHS location hierarchy. This was done in the steps above in the hierarchy view. If it is required to change the properties of a health center or a service provider, you must use the Manage Health Centers and Service Providers app.

Procedure

| Step | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Occupational Health. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Start the Manage Health Centers and Service Providers app. | The initial screen of the app is displayed. |  |
| 3 | Start Search | Choose the tab Search.Enter the ID of the health center you created into the search field Location.Choose Go. | The search starts and the hit list is displayed. |  |
| 4 | Open Your Health Center | Choose the location you want to edit to open it. | The selected location opens in edit mode to show the location’s details. |  |
| 5 | Edit Properties | Change some properties of your health center. For example, assign a country. |  |  |
| 6 | Save Your Entries | Choose Save.You can ignore the warning that no country/region was entered. | The adopted data is saved to the database. |  |

Result

You selected a health center and changed some of its properties.

### Manage Occupational Health Protocols

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

A health protocol is a standardized set of procedures or guidelines designed to address specific medical or health-related situations. Health protocols are used to ensure consistent and effective treatment across different patients and healthcare providers. They outline steps for consultation, treatment, follow-up, and monitoring of conditions, aiming to optimize patient outcomes and maintain safety standards. Examples include health protocols for administering health surveillance, specific medications, responding to emergency situations, or conducting medical screenings.

The following steps assume that no health protocols exist in your system yet or that you want to create a new health protocol.

Procedure

| Step | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Occupational Health. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Start the Manage Occupational Health Protocols app. | The initial screen of the app is displayed. |  |
| 3 | Create a New Health Protocol | Choose Go to create a list of existing health protocols in your system.Choose Create to create a new health protocol. | A dialog to display existing health protocols and to create new health protocols is displayed. |  |
| 4 | Enter Relevant Data | In the General Information section, enter the following data:External ID: leave it at the default value (internal ID) or set it to PROT_<your user number>Title: Health Surveillance for NoiseType: OfferedCategory: Health Surveillance ProtocolCalendar Type: Medical ExaminationsOwner: InternalStart Date: <today's date> (as defaulted)End Date: Dec. 31, 9999 (as defaulted) |  |  |
| 5 | Save Your Entries | Choose Create at the bottom of the screen. | The data you just entered is saved. |  |
| 6 | Add Health Service Types | Choose Edit.In the Health Service Types section, choose Add and enter the following data:Health Service Type: Initial ConsultationIs First: mark the checkboxAge in Years: leave empty (as defaulted)Gender: Not specifiedHazard Category: ChemicalChoose the small arrow to open the details of this data set. Enter the following data:Next Health Service Type: Follow-up ConsultationNext Health Service Type Due: 12 MonthsIn the Health Service Items section, choose Add and enter the following data:Health Service Item: Health Surveillance Consultation (Category: Consultation)Add a second health service item in the same way:Health Service Item: Occupational Health History (Category: Anamnesis)Choose Apply at the bottom of the screen.Back on the main object page for health protocol maintenance, choose Save. | The mode changes into edit mode to enable you to perform changes.The basic data for health service type is created.Data to define the next health service type is maintained.Health service items are added to the health service type in the new health protocol.The added health service type is saved. |  |
| 7 | Add a Second Health Service Type | Repeat the sequence of step 6 to add a second health service type.Choose Edit.In the Health Service Types section, choose Add and enter the following data:Health Service Type: Follow-up ConsultationIs First: leave checkbox unmarkedAge in Years: leave empty (as defaulted)Gender: Not specifiedHazard Category: ChemicalChoose the small arrow to open the details of this data set. Enter the following data:Next Health Service Type: Follow-up ConsultationNext Health Service Type Due: 36 MonthsIn the Health Service Items section, choose Add and enter the following data:Health Service Item: Health Surveillance Consultation (Category: Consultation)Choose Apply at the bottom of the screen.Back on the main object page for health protocol maintenance, choose Save. | The mode changes into edit mode to enable you to perform changes.The basic data for health service type is created.Data to define the next health service type is maintained.One health service item is added to the health service type in the new health protocol.The added health service type is saved. |  |
| 8 | Optional Step: Add a Compliance Obligation | Choose Edit.In the Compliance Obligations section, choose Add and enter the following data:Compliance Obligations: <enter a value from the dropdown list, if any value appears>Choose Save. | A compliance obligation was added to the health protocol. |  |
| 9 | Add Duration and Cost | Choose Edit.In the Duration and Cost section, choose Add and enter the following data:Health Service Provider: <use the search help and select the health service provider you entered earlier>Duration: 25Cost: 30 EURChoose Save. | Duration and cost for this health protocol have been assigned for the selected health service provider. |  |
| 10 | Set Status to Active | Choose Set in Progress.Choose Set to Active.Confirm the confirmation pop-up by choosing OK. | The status of the health protocol was set to Active. |  |

Result

A health protocol was created with its respective details and can now be used in the further Occupational Health processes.

### Set a Health Center as My Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

Health centers are the locations where health-related processes (health service items) are performed. Health centers are represented by EHS locations. As a receptionist, you work in one dedicated default health center. For this, you must set this health center as "My Location" in the Manage Health Center Structure app.

The following steps assume that health centers created in the earlier scenarios exist in your system. If there is already a health center assigned as "My Location", you can skip this section.

Procedure

| Step | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select the Previously Created Health Center | In the Manage Health Center Structure app, select the previously created location UXT HSP Walldorf.If you don't see this location, choose Show All Locations first. |  |  |
| 2 | Assign Health Center as "My Location" | Right-click on the location UXT HSP Walldorf.The context menu shows the option Set as "My Location". | A dialog to enter the relevant information is displayed. |  |
| 3 | Check Assignment and Close the App | The health center you just set as "My Location" is displayed in the field My Location.Close the application. | The selected health center is now set as "My Location" and can be used in the further processes. |  |

Result

A health center was set to be "My Location" so that it appears as default health center in the Manage Health Center Appointments application.

### Create a Health Center Appointment in the Default Health Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

The health-related services in Occupational Health are handled by health service requests. These requests are processed in health centers. To achieve this, an appointment for a health service request must be made. This includes the information about the patient, the physician, the health protocol or health service item, and the date, time, and duration of the appointment. This test is for an Occupational Health Receptionist who is responsible for handling the appointments for a dedicated health center.

The following steps assume that a health center exists that was assigned as "My Location" and that at least one health protocol was created as described above. The health center also needs to have persons responsible for Occupational Health assigned as described in the test scenarios above.

Procedure

| Step | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Receptionist - Occupational Health. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Start the Manage Health Center Appointments application.There are two ways to create new appointment data:Option 1: Use the create buttonOption 2: Click and drag in the calendar | The initial screen of the app is displayed.It shows the appointment calendar, focused on the default health center (UXT Health Center Walldorf).The rows show the persons responsible for Occupational Health in the assigned calendar types. |  |
| 3 | Create a New Health Service Request (Option 1) | Option 1 – Use the create button:In the first row, choose the entry with your user's name, the role Occupational Health Physician and calendar type Medical Examinations. (This data was created in the test scenario to create a health center.)The line is marked and the button New Health Service Request gets activated.Choose New Health Service Request. |  |  |
| 4 | Enter Relevant Data (Option 1) | In the pop-up New Health Service Request, enter the following data:Title: <enter a title of your choice for the health service request>Patient: <use the search help to select a person – they should possess a working contract>Health Protocol: <use the search help to select the entry Health Surveillance for Noise / Initial Consultation>Appointment Notes: <enter a free text>Appointment Date and Time: <use the entry help to choose the current date and a time later than the current time>Appointment Duration in Minutes: 35Choose Create. | You will only be able to see potential patients if persons with assigned working contracts exist in the system.An appointment for a health service request for a patient is created for the current date in the default health center.The data is automatically saved. |  |
| 5 | Create a New Health Service Request (Option 2) | Option 2 - Click and drag:In any row, click left and hold down the mouse button over a dedicated start time for the appointment. Drag the cursor to the right to mark the duration and time for the appointment.Lift the left mouse button. The pop-up for creation of a health service request appears. |  |  |
| 6 | Enter Relevant Data (Option 2) | In the pop-up New Health Service Request, enter the data in a similar way as described in step 4; enter data of your choice.You can test to create the appointment without assignment of a health protocol (this field is not mandatory).The date, start time and duration should be defaulted from the click-and-drag step you just performed. You can even adapt this data in the pop-up.Choose Create. | An appointment for a health service request for a patient is created for the current date in the default health center.The data is automatically saved. |  |

Result

A health service request together with its appointment data was created for the default health center.

### Refine a Health Center Appointment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

Appointments for health service requests have been created in the test scenario before. It could be the case that the appointment data or data regarding the health service request need to be adapted for an already existing appointment. For example, health protocols and/or health service items could be added or removed or the date/time/duration of an appointment needs to be changed.

The following steps assume that appointments for health centers have been created. The health center needs to be assigned as "My Location" and also needs to have persons responsible for Occupational Health assigned as described in the test scenarios above. All these steps have been performed in the scenarios before.

Procedure

| Step | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Receptionist - Occupational Health. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Start the Manage Health Center Appointments application.You should see the appointments created in the test scenario above. If not, check the health center and/or the date which is displayed. Otherwise, create an appointment, following the steps shown above (option 2 would be the fastest way). | The initial screen of the app is displayed.It shows the appointment calendar, focused on the default health center (UXT Health Center Walldorf).The rows show the persons responsible for Occupational Health in the assigned calendar types. |  |
| 3 | Open the Refinement Page for an Appointment | Search for an appointment in the calendar view and double left-click on it.The page Health Service Request opens in display mode with the data of the selected health service request. You are now able to refine the existing data. |  |  |
| 4 | Adapt Date, Start Time or Duration | Choose Edit.Choose Change Appointment.Change the following data:Appointment Date and Time: <use the entry help to change date and time>Appointment Duration in Minutes: <enter a different duration>Confirm your changes by choosing Change Appointment.Choose Save. | The UI changes into edit mode.A pop-up Change Appointment opens.The date, time and/or duration for the appointment has changed. The pop-up closes and the changed data shall be reflected in the header section of the object page.The changed appointment data is saved.The object page changes into display mode. |  |
| 5 | Adapt Data from the Health Service Request | Choose Edit.In the section Appointment Notes, change the description.In the section Health Protocols, add an additional health protocol.If at least one protocol is already assigned, choose Add.Use the entry helps to define a valid combination of health protocol and health service type.Optional:Add one or more additional health protocols with different data.Try to remove a health protocol – it shall work, also removing dependent health service items.In the section Health Service Items, there might already be items shown which derive from the assigned health protocols.If at least one protocol is already assigned, choose Add.Use the entry help to select a health service item (which is not yet assigned).Health protocol related items show the referring health protocol in the column Source Health Protocol.Optional:Try to delete a referenced health service item – it shall not work.Try to delete a manually added health service item – it shall work.Choose Save. | The dialog shall change into edit mode.Additional health protocol / health service type combinations shall be assigned – or removed.Removal of a health protocol shall also remove the dependent health service item (depending on master data set-up of the health protocol).Health service items can be added or removed upon the user's decisions.Referenced health service items shall not be removable manually.The changed data is saved. A message that data was successfully saved is displayed. |  |
| 6 | Navigate Back to the Appointment Calendar View | Choose the small arrow to the left at the top-left section of the page. | The system switches the display back to the calendar view to the place where we started from (same health center and day displayed). |  |

Result

Properties of the health center appointment and the health service request have been changed and saved. Multiple health protocols and/or health service items can be assigned in this way.

### Manage Health Center Appointments: Change Health Center and Create an Appointment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

Appointments for health service requests are usually created for the default health center which was set as "My Location". However, it might sometimes be necessary to work with another health center, without changing the default health center in the master data (for example, of a receptionist). An example could be that a health team performs a mobile health day at another plant of the company.

The following steps assume that a health center is assigned as "My Location". Another health center for a mobile health day must be created for the target location. The persons responsible for Occupational Health must be assigned to both health centers as described in the test scenarios above.

Procedure

| Step | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Receptionist - Occupational Health. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Start the Manage Health Center Appointments application.You should see the appointments created in the test scenario above. If not, check the health center and/or the date which is displayed. Otherwise create an appointment, following the steps shown above (option 2 would be the fastest way). | The initial screen of the app is displayed.It shows the appointment calendar, focused on the default health center (UXT Health Center Walldorf) which was set as "My Location".The rows show the persons responsible for Occupational Health in the assigned calendar types. |  |
| 3 | Change to Another Health Center | To open the health appointment calendar for a different health center, choose Change Health Center.In the search pop-up window, select a target health center from the displayed list.Optional: Test the filter fields that are provided. | A list of health centers with their assigned health service providers is displayed.The target health center shall be used to open the appointment calendar view. The persons assigned to that health center are displayed. |  |
| 4 | Maintain Appointments in the Target Health Center | Maintain appointments for the target health center as described above in the test scenario Create a Health Center Appointment in the Default Health Center. | You should be able to work for the target health center in a similar way to the default health center. |  |

Result

In the health center appointment calendar, you changed to another health center than the default one and created an appointment for that health center.

### Manage Health Service Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

After a health service request has been created and an appointment has been made, the request must be processed. Usually, this is done by an occupational health physician or a medical assistant. Processing begins once the patient receives the planned services. The physician will go through the planned data, might adapt it and start the processing. Then, health-related data will be maintained, for example, analyzing the health history and providing dedicated consultations, examinations or vaccinations. Once all data has been maintained and results have been derived, the health service request is closed and saved for later analysis and documentation.

The following steps assume that a health center appointment has been made for a health service request in the health center which is assigned as "My Location" to the user.

Procedure

| Step | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Physician - Occupational Health. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Start the Manage Health Service Requests application.Choose Go to create a list of health service requests according to the settings in the filter fields.The appointments created in the test scenarios above are displayed. If not, check the health center and/or the date which is displayed. Otherwise, create an appointment, following the steps shown above (option 2 would be the fastest way).Use the filter fields to test the filtering of the list. | The initial screen of the app is displayed.It shows a list of appointments, focused on the default health center (UXT Health Center Walldorf) which was set as "My Location".The entries shall correspond to the filter values provided. |  |
| 3 | Select a Health Service Request | To open the health service request from the list view, click in the row you want to select.Select a health service request for processing where the following status are set:Health Service Request Status: NewAppointment Status: Confirmed | A list of health centers with their assigned health service providers is displayed.The object page of the selected health service request should open and display the data of the request as well as the appointment data. |  |
| 4 | Adapt Data from the Health Service Request | On the object page of the health service request, you can edit the data of the request as well as of the appointment.Choose Edit.Perform changes to the data as described in test scenario Refine a Health Center Appointment.Be sure to assign at least one health protocol and one health service item to the health service request.Choose Save. | After choosing Edit, the screen should switch into maintenance mode, and you can change the data. This page corresponds to the one for refinement of appointments during the scheduling process.The system saves the changed data and changes back into display mode. |  |
| 5 | Start Processing of a Health Service Request | Choose Process Health Service Request to start the maintenance of the results for the request.Check that the section Closing Data appears at the bottom of the screen.Check that it is possible to select health service items, health protocols and the basic data of the health service request. | The UI should switch into a split screen mode where the user can select the different content on the left side. On the right side of the split screen, the details view of the selected object shall be displayed.At the bottom of the screen, a section with data to close the health service request appears.The different data sets that have been assigned to the health service request are selectable. |  |
| 6 | Maintain Results for Health Service Items | In the section Health Service Items, select one assigned health service item.If no health service item is assigned yet, add one by choosing Add (described in test scenario Refine a Health Center Appointment).Status: PerformedDate Performed: <leave it at the default entries>Comment: <enter a free text of your choice>Maintain comparable entries with all health service items that are assigned to the health service request. You may vary in the values of the fields you maintain.Choose Save. | The details view of the selected data set should be displayed on the right side of the split screen.The health service item received results.All assigned health service items should have received some results.The maintained data is saved by the system. |  |
| 7 | Maintain Results for Health Protocols | In the section Health Protocols, select one assigned health protocol.If no health protocol is assigned yet, add one by choosing Add (described in test scenario Refine a Health Center Appointment).Entry Date: <leave it at the default entries>Date Performed: <leave it at the default entries>Next Due Date: <leave it at the default entries or set it manually to a date in the future>Reservation: no concernsValid Until: <leave it at the default entries or set it manually to a date in the future>Physician: <select your user>Comment: <enter a free text of your choice>Maintain comparable entries with all health protocols that are assigned to the health protocols. You may vary in the values of the fields you maintain.Choose Save. | The detail view of the selected data set should be displayed on the right side of the split screen.The Entry Date is the date of the appointment – it can be changed (e.g., if someone is late).The Date Performed indicates when the results have been entered.The Next Due Date indicates the date for a re-occurrence.All health protocols assigned to the health service request have received results.The maintained data is saved by the system. |  |
| 8 | Maintain Important Information about the Patient | The system shows important information about the person. This person-specific free text is assigned to the person directly (not to the health service request). It can contain information about allergies or other important health-related data or even comments.Choose Edit Information to change the free text field into edit mode.Maintain some information on the patient.Choose Save. | An entry in the free text field was made and saved. It should now appear in every health service request for that patient. |  |
| 9 | Close the Health Service Request | Once all data for a health service request is maintained, the user ends the process by closing the request.In the section Closing Data, perform the following entries:Status: CompletePhysician: <search and enter your user>Closing Date: <leave it at the default entries or set it manually to the current time>Health Service Refused: <leave it empty>Person Informed: <leave it empty>Consultation Duration: 43Choose Save.If any warning pop-up is displayed, choose the Save or Continue option. | Upon choosing Close Health Service Request, the status of the health service request switches to Closed. The data will be saved and the UI changes into a non-editable mode. |  |

Result

You selected a health service request and processed it. You provided results for health service items and health protocols and closed the health service request.

### Display Health Center Appointments in the System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

Appointments for health service requests are assigned to the health centers where they should be processed. To keep an overview of existing appointments using a filterable list, the Monitor Health Center Appointments app is used.

The following steps assume that health center appointments have been made for a health service request in one or several health centers.

Procedure

| Step | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Physician – Occupational Health or as Receptionist – Occupational Health. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Start the Monitor Health Center Appointments app.Choose Go to create a list of health service requests according to the settings in the filter fields.You should see the appointments created in the test scenarios above. If not, check the health center and/or the date which is displayed. Otherwise create an appointment, following the steps shown above (option 2 would be the fastest way). | The initial screen of the app is displayed.It shows a list of appointments, focused on the default health center (UXT Health Center Walldorf) which was set as "My Location".The entries shown correspond to the filter values provided. |  |
| 3 | Test the Filter Settings | Use filter fields to test the filtering of the list.Test different combinations of filters. For example, set a specific health center and/or change the time interval for appointments to be displayed.Choose Go to create the list anew after changing the filter values.Adapt the filters by choosing Adapt Filters. Mark and unmark different fields in the pop-up and confirm your choice by choosing OK.Check that the marked filter fields appear.Test filtering with the adapted filter settings. Choose Go to create the list anew.Save your filter settings with your own view. Name the view by your choice – for example, use your username.Check that you can switch between the filter views by choosing the small arrow pointing downwards besides the filter name on the top left side of the screen (by default, it is named Standard).Choose Go to create the list anew after changing the filter view.Restart the application and check that your filter view still exists.Choose Go to create the list – your selected filter view should be considered. | The entries shown correspond to the filter values provided.You should be able to change the filter fields.Only the marked filter fields shall be used from the system and shall be considered in the creation of the list.There shall be the possibility to create own reusable views for filtering by own criteria.The system should consider the selected view for filtering the resulting list entries.Also, after restarting the application, your saved filter view shall appear again. |  |
| 4 | Test the Column Layout | Change the column layout by choosing the gear button in the header line of the list.Mark and unmark different fields in the pop-up and confirm your choice by choosing OK.Check that only the columns that were marked are used for the list.Choose Go to create the list anew. | A pop-up should appear that enables you to select the columns to be displayed.You should be able to mark or unmark different columns and use the new setup.The list should use only the columns that were marked in the settings. |  |
| 5 | Export the List | Test the export functionality for the list. This will only work if a list has been created. Choose Go to create one.Choose Export to export the displayed list as an Excel file.Download the Excel file to your local computer, open it, and check that the information provided in the file corresponds to the data provided in the list within the SAP system.Optional: Also test the Export As… function to be able to change the name and type of the download file.Choose the following values:File Name: Health Service Request_<your user name>Format: PDFInclude filter settings: <mark the checkbox>Choose the different options to adapt the resulting PDF layout as wished.Choose Export.Wait for the PDF file to be generated.Download the file to your local computer.Open the downloaded file and check that the information provided in the file corresponds to the layout, setup and data provided for the export. | The Excel file should be generated.Depending on your computer settings, the file is directly downloaded, or you must confirm a pop-up to do that.The data in the Excel file should correspond to the data provided in the SAP system.The PDF file should be generated. Depending on your computer settings, the file is directly downloaded, or you must confirm a pop-up to do that.The file name should correspond to the name you gave it and the filter settings should be displayed on the upper part of the PDF file, if you selected the option above. |  |

Result

You can create lists of existing health center appointments. You can influence the results by filtering. You can influence the filter fields that are used, save filtering views and export the data in different formats.

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
> Flagged while digesting this document, not verified: The Create Health Centers Result says the center has two medical physicians, one psychologist and one receptionist, but the steps assign two OH Physicians, one OH Nurse and one OH Receptionist (no psychologist role).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[13-quality-ehs-and-compliance/health-and-safety-management-54a-ae-test-script-sap-s-4hana-cloud-publ]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7ZA_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 83,752 chars in the whole document
