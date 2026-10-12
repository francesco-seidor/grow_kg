---
id: 01-solution-foundation-and-platform/test-script-data-migration-to-sap-s-4hana-from-sap-bh3-1268
title: "Test Script: Data Migration to SAP S/4HANA from SAP (BH3) (BH3_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script (BH3) for migrating data directly from an SAP source system with the migration cockpit: role setup, steps, validation."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/data-migration-cockpit]
aliases: [BH3_S4CLD2608_BPD_EN_XX]
keywords: [Data Migration with the Migration Cockpit (Direct Transfer…, data migration, migration cockpit, migration project, business roles, mapping tasks, staging tables, migration simulation, migration monitoring, data validation]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BH3_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1268
topic: 01-solution-foundation-and-platform/data-migration-cockpit
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Data Migration to SAP S/4HANA from SAP (BH3) (BH3_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BH3_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Data Migration with the Migration Cockpit (Direct Transfer and Staging Tables)** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Data Migration to SAP S/4HANA from SAP (BH3) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232793702)

[2 Prerequisites 4](#_Toc232793703)

[3 Technical Business Role Templates for Data Migration 5](#_Toc232793704)

[4 Migration Objects for SAP S/4HANA Cloud Public Edition 6](#_Toc232793705)

[5 Preliminary Steps: User Settings 7](#_Toc232793706)

[5.1 Create and Assign Business Role for Data Migration 7](#_Toc232793707)

[6 Overview Table 8](#_Toc232793708)

[7 Test Procedures 9](#_Toc232793709)

[7.1 Start the SAP S/4HANA Cloud Public Edition Migration Cockpit 9](#_Toc232793710)

[7.2 Create Migration Project 10](#_Toc232793711)

[7.3 Select Data from Source System 11](#_Toc232793712)

[7.4 Use Staging Tables as Intermediate Storage (Optional) 12](#_Toc232793713)

[7.4.1 Extracting Data to Staging Tables 12](#_Toc232793714)

[7.4.2 Transferring Data from Staging Tables to the Migrate Your Data App 13](#_Toc232793715)

[7.5 Prepare Mapping Tasks 14](#_Toc232793716)

[7.6 Process Mapping Tasks 14](#_Toc232793717)

[7.7 Simulate the Migration 15](#_Toc232793718)

[7.8 Migrate Data to the Target System 16](#_Toc232793719)

[7.9 Check Data Migration Status. 17](#_Toc232793720)

[7.10 Validate Migrated Data 18](#_Toc232793721)

[8 Appendix 20](#_Toc232793722)

[8.1 ALE/IDoc Distribution After Data Migration 20](#_Toc232793723)

## Purpose

Overview

Customers can use the SAP S/4HANA migration cockpit as part of the SAP S/4HANA Cloud Public Edition license. If the customers choose to migrate data directly from an SAP system, they use a communication arrangement to connect the SAP S/4HANA migration cockpit to the source system. The migration cockpit selects data from the source system by using specific criteria.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| Note SAP S/4HANA Cloud Private Edition refers to the default on-premise suite on the SAP HANA platform, SAP S/4HANA Cloud Public Edition refers to our cloud suite on SAP Business Technology Platform. |

|  |
| --- |
| Caution Data protection legislation may require that personal data is deleted once the data has served its originally defined purpose and is also no longer subject to additional legal data retention requirements. If data protection legislation is applicable in your case, then migrating personal data that should have been deleted could be interpreted as the processing of personal data without any legally justified purpose. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

- In addition, you have to install the add-on DMIS 2011 SP23 (or higher) in the source system. This add-on is included in the license for SAP S/4HANA Cloud Public Edition. For more information, see SAP Notes [1577441](https://me.sap.com/notes/1577441), [1577503](https://me.sap.com/notes/1577503), and [1648747](https://me.sap.com/notes/1648747).
- You have ensured access to both the source ECC system and the target SAP S/4HANA Cloud Public Edition system.

|  |
| --- |
| Note If you are using staging tables as intermediate storage, create a database connection to the remote SAP HANA schema by setting up a communication arrangement for communication scenario SAP_COM_0678 (Migration Cockpit Integration). Follow the setup instructions as described for Data Migration to SAP S/4HANA from Staging ([2Q2](https://me.sap.com/processnavigator/SolS/SolS-013/2602/SolP/2Q2)). |

Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/ab5a01312a7f3f336f509fc2c25a4635)

x

## Technical Business Role Templates for Data Migration

To create a business role for your data migration user, you need to know the migration objects that they want to use in your migration project. You then need to add the respective business catalogs to your business role. For information about the necessary business catalog, see the documentation for the migration object.

You can find an extensive table listing all migration objects available for SAP S/4HANA Cloud Public Edition, as well as the business catalogs required for creation, in the [SAP S/4HANA Cloud Public Edition product assistance](https://help.sap.com/viewer/cc9ecc5f5f6b400a98d10e930324f7ad).

Use the following business role templates to access the Migrate Your Data Migration - Cockpit(F3473)app:

| ID (Role Template) | Name (Role Template) | ID (Launchpad Space) | Name (Launchpad Space) |
| --- | --- | --- | --- |
| SAP_BR_CONFIG_EXPERT_DATA_MIG | Configuration Expert - Data Migration | SAP_BR_CONFIG_EXPERT_DATA_MIG | Data Migration |

## Migration Objects for SAP S/4HANA Cloud Public Edition

You can find an extensive table listing all migration objects available for SAP S/4HANA Cloud Public Edition, together with their respective migration object documentation, in the [SAP S/4HANA Cloud Public Edition product assistance](https://help.sap.com/viewer/cc9ecc5f5f6b400a98d10e930324f7ad) or via the short link [https://help.sap.com/S4_CE_MO](https://help.sap.com/S4_CE_MO).

## Preliminary Steps: User Settings

Use

In these steps, you set up the necessary user settings for migrating your data.

### Create and Assign Business Role for Data Migration

Use

You create and assign the required business role for data migration using the business role template mentioned under [Technical Business Role Templates for Data Migration](#unique_3) [page ] 5 and adjust it to the user's requirements.

Prerequisites

To create a business role for your data migration user, you need to know the migration objects that they want to use in their migration project. You then need to add the respective business catalogs to their business role.

Procedure

1. Log on to SAP Fiori launchpad as an administrator. Open the Maintain Business Roles (F1492) app. On the initial screen, select Create From Template to create a new role based on the technical business role template for data migration.
2. Select the required template as listed under [Technical Business Role Templates for Data Migration](#unique_3) [page ] 5. Define the ID and the description of the new business role. Choose OK.
3. On the Assigned Business Catalogs tab, you can see which catalogs are already assigned to this role. To be able to migrate data, you need to add additional catalogs according to the data migration user's requirements. Add the required business catalogs for the migration objects that the data migration user wants to use in their migration project.
4. Choose Maintain Restrictions. By default, the Read, Value Help category for each business catalog is set to Unrestricted and the user has no write access. For data migration, you also need to set the Write, Read, Value Help category to Unrestricted.
5. On the Assigned Business Users tab, you can assign the data migration users to your new business role. These users will receive the authorizations as defined in the business role.
6. Save the business role to activate it.

|  |
| --- |
| Note If you go back to the business roles overview without saving the business role, the business role will automatically be saved in a draft status. You can access it again and edit it from the business roles overview. |

## Overview Table

This scope item consists of several process steps provided in the table below.

| Process Step | UI Type | Business Condition | Expected Results |
| --- | --- | --- | --- |
| [Start the SAP S/4HANA Cloud Public Edition Migration Cockpit](#unique_8) [page ] 9 | Migration Cockpit | This section describes how you start the SAP S/4HANA migration cockpit. | The migration cockpit is displayed. |
| [Create Migration Project](#unique_9) [page ] 10 | Migration Cockpit | This section describes how you create a migration project in the migration cockpit. | A migration project is created. |
| [Select Data from Source System](#unique_10) [page ] 11 | Migration Cockpit | This section describes how you select the relevant data from the source system. | The data is selected from the source system based on specified criteria. |
| [Prepare Mapping Tasks](#unique_11) [page ] 14 | Migration Cockpit | This section describes the steps necessary to prepare the mapping tasks. | The mapping tasks associated with the migration objects are identified. |
| [Process Mapping Tasks](#unique_12) [page ] 14 | Migration Cockpit | This section describes the steps necessary to process the mapping tasks. | The mapping tasks associated with the migration objects are processed and confirmed. |
| [Simulate the Migration](#unique_13) [page ] 15 | Migration Cockpit | This section describes the steps necessary to prepare for the final migration. | The data is ready to be migrated to the target system. |
| [Migrate Data to the Target System](#unique_14) [page ] 16 | Migration Cockpit | This section describes how you migrate your data into the target system. | The data is transferred from the source system to the target system. |
| [Check Data Migration Status.](#unique_15) [page ] 17 | Migration Cockpit | This section describes how you check the status of your migration projects and objects. | You are up-to-date with the status of your migration projects and objects. Necessary changes in migration projects can then be made. |
| [Validate Migrated Data](#unique_16) [page ] 18 | SAP Fiori launchpad | This section describes how you validate completeness and correctness of the migrated data in the target system using corresponding business functions. | The relevant data can be found in the corresponding business functions. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Start the SAP S/4HANA Cloud Public Edition Migration Cockpit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This section describes how you start the SAP S/4HANA Cloud Public Edition Migration Cockpit.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Start SAP Fiori launchpad | Log on to your SAP S/4HANA Cloud Public Edition system. | The Home page appears. |  |
| 2 | Open Migration Cockpit | Choose the Migrate Your Data - Migration Cockpit(F3473) tile. |  |  |

|  |
| --- |
| Note For more information on the SAP S/4HANA Cloud Public Edition Migration Cockpit in SAP S/4HANA Cloud Public Edition, see the [product assistance on SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/f32db0c240484241abc53a876253e118.html). |

Result

The Migrate Your Data home screen appears.

### Create Migration Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This section describes how you create a migration project in the migration cockpit.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Create New Project | Choose Create and then Migrate Data Directly from SAP System on the Migration Projects home screen. | The New Migration Project dialog window appears. |  |
| 2 | Choose Settings for Migration Project | Make the required entry in the New Migration Project dialog window:Name:Name of your migration project.Scenario:Only the migration scenario SAP ERP to SAP S/4HANA Cloud Public Edition is available.Connection to Source System:Select or enter the communication arrangement used to connect the source system.See the product assistance for further information.After making the required entries, choose Step 2. |  |  |
| 3 | Select Data | Specify the relevant criteria that is used to select the data for the relevant migration objects.After specifying the relevant criteria, choose Step 4. |  |  |
| 4 | Choose Migration Objects | Choose all relevant migration objects for your project. Then, choose the arrow to add them to the Selected Migration Object table on the right. When you’r, choose Review. |  |  |
| 5 | Add Dependent Objects (optional) | The system checks for predecessor objects and might ask you whether you want to add additional migration objects to your project. For more details, choose Select Objects.Choose Add or Do Not Add as required. | An overview page with your project settings is displayed. |  |
| 6 | Create Migration Project | Double-check your project settings and choose Create Project. |  |  |

|  |
| --- |
| Note After an SAP S/4HANA Cloud Public Edition release upgrade, any new migration objects won’t get added to existing migration projects. To be able to use new migration objects, you need to create a new migration project. |

Further Information

Find [further information about project settings](https://help.sap.com/viewer/d5699934e7004d048c4801b552f3b013/latest/en-US/08b9a967045643bd8c80fdc29e70b944.html) in the product assistance on SAP Help Portal.

### Select Data from Source System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This section describes how you select your data from the source system.

The SAP S/4HANA Cloud Public Edition migration cockpit uses migration objects to transfer data to the SAP S/4HANA Cloud Public Edition system. The data for the migration objects is selected from the source system based on specific criteria such as company codes. For example if you use company codes, only data that is relevant for the specified company codes will be selected from the source system. In this way, you restrict the data that is transferred to the target SAP S/4HANA Cloud Public Edition system for the relevant migration objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select Data | On the Migration Project screen, select the relevant migration object.In the Action column, choose Select Data and then New Selection. | The system selects the relevant instances for the migration object. In the Data column, you can view the number of selected instances. |  |
| 2 | Select Additional Instances (optional) | On the Migration Project screen, choose the action Select Data and then New Selection or Add Additional Instances. | The system selects all the instances again or any additional instances for the migration object. |  |

Result

The data is selected from the source system.

### Use Staging Tables as Intermediate Storage (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

The Migrate Your Data creates staging tables for the selected data within the remote SAP HANA schema and stores the selected data in these tables. You can then adjust the values directly in the relevant database tables if needed.

#### Extracting Data to Staging Tables

Use

This section explains how to extract data to staging tables for the relevant migration objects in your project.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Extract to Staging Tables | On the Migration Project screen, select the relevant migration object.In the Action column, choose Extract to Staging Tables. | The system extracts the selected data for the migration object to the staging tables in the remote SAP HANA schema. In the Data column, you can view the number of staging tables. |  |

Result

The data is successfully extracted to the staging tables.

#### Transferring Data from Staging Tables to the Migrate Your Data App

Use

This section describes how to transfer data from the staging tables to the Migrate Your Data app, which is a necessary step before proceeding with the migration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Transfer from Staging Tables | On the Migration Project screen, select the relevant migration object.In the Action column, choose Transfer from Staging Tables. | The system transfers the data from the staging tables to the Migrate Your Data app. In the Data column, you can view the number of staging tables. |  |

Result

The data is successfully transferred from the staging tables to the Migrate Your Data app.

### Prepare Mapping Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

Before migrating your data to the productive system, you need to conduct a couple of preparational steps.

This section describes how you prepare mapping tasks for the migration object before you can proceed with the simulation or the migration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Mapping Tasks | On the Migration Project screen, select the relevant migration object.In the Action column, choose Prepare Mapping Tasks. | The Prepare Mapping Tasks dialog box appears. |  |
| 2 | Choose Instances for Preparation | Select the option available for the migration object instances and choose the action Prepare Mapping Tasks. | The system prepares the mapping tasks to be processed for the relevant migration object instances. On the Migration Project screen, in the Mapping Tasks column, you can view the number of open mapping tasks. |  |

Further Information

Find [further information about project settings](https://help.sap.com/viewer/d5699934e7004d048c4801b552f3b013/latest/en-US/08b9a967045643bd8c80fdc29e70b944.html) in the product assistance on SAP Help Portal.

### Process Mapping Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This section describes how you process open mapping tasks for the migration object before you can proceed with the simulation or the migration.

After the system has selected the data for a migration object from the source system, you need to process any open mapping tasks for the migration object before you can proceed with the simulation or the migration. Examples of mapping tasks include Value Mapping tasks (where you specify target values for corresponding source values) and Fixed Value tasks (where you set default values for target fields).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | View Mapping Tasks | On the Mapping Tasks screen, you can view the open mapping tasks (open mapping tasks have the status To be Confirmed) as well as any confirmed mapping tasks. |  |  |
| 2 | Confirm Mapping Tasks | Process the tasks by entering the relevant target values, and confirming these target values. You can then set the status of the task to Confirmed.[Find more information about mapping tasks in the product assistance.](https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/76cbbf659549445384b91ffd0353b698.html?locale=en-US) |  |  |

Further Information

For more information about the SAP S/4HANA Cloud Public Edition Migration Cockpit in SAP S/4HANA Cloud Public Edition, see the [product assistance on SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/f32db0c240484241abc53a876253e118.html).

### Simulate the Migration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This section describes how you simulate the transfer of data to the target SAP S/4HANA Cloud Public Edition system.

Note that no data is written to the target SAP S/4HANA Cloud Public Edition system during the simulation process, but you can view all the messages that would occur during an actual data transfer (for example information about a cost center that does not exist).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Simulate the Migration | Once you have processed all open tasks for a migration object, you can simulate the transfer of data.On the Migration Project screen, select the relevant migration object and choose the action Simulate.[Find more information about simulation in the product assistance.](https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/76cbbf659549445384b91ffd0353b698.html?locale=en-US) | The system displays the New Simulation dialog box. |  |
| 2 | Choose Instances for Simulation | Select the appropriate option for available for migration object instances and choose the action Start Simulation.You can view the number of instances that have been simulated successfully, and the number of instances that have errors. For more information, choose the relevant number in the Simulation column. | The system simulates the relevant migration object instances. |  |

Further Information

For more information about the SAP S/4HANA Cloud Public Edition Migration Cockpit in SAP S/4HANA Cloud Public Edition, see the [product assistance on SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/f32db0c240484241abc53a876253e118.html).

### Migrate Data to the Target System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This section describes how you migrate your data into your target system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Migrate Data | On the Migration Project screen, select the relevant migration object and choose the action Migrate. | The system displays the New Migration dialog box. |  |
| 2 | Choose Instances for Migration | Select the appropriate option for available for migration object instances and choose the action Start Migration.You can view the number of instances that have been migrated successfully, and the number of instances that have errors. For more information, choose the relevant number in the Migration column. | The system migrates relevant migration object instances. |  |

Result

The data is transferred from the source system to the target system.

Further Information

For more information on the SAP S/4HANA Migration Cockpit in SAP S/4HANA Cloud Public Edition, see the [product assistance on SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/f32db0c240484241abc53a876253e118.html).

### Check Data Migration Status.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This section describes how you can check the status of your migration instances.

Prerequisite

You've started migrating data to your SAP S/4HANA system for at least one migration object.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Monitor Migration Process | On the Migration Project screen, choose Monitoring. | You can monitor the status of the actions performed on a migration object.The system displays the Monitoring screen, where you can view the active and completed activities, for example Migration Started or Migration Completed. |  |
| 2 | View Migration Progress | On the Migration Project screen, in the Migration Progress column, you can view the status of the migration.If the migration has started for a migration object, you can view the progress in percentage values. |  |  |

Result

You have up-to-date information about the status of your migration projects and objects.

### Validate Migrated Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This section describes how you validate completeness and correctness of the migrated data in the target system using corresponding business functions.

Prerequisite

You've migrated at least one migration object instance to your SAP S/4HANA Cloud Public Edition system for a migration object.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | View Migration Results (optional) | On the Migration Object Instances screen, switch to the Migration Results view. | The system displays one or more fields that contain the migration results in the Result of Step column. If this option is not available, try the method in Step 2. |  |
| 2 | Access the Corresponding App | Open the corresponding app of the SAP S/4HANA Cloud Public Edition system and check completeness of the migrated data.You can also navigate directly to the relevant app by clicking an entry in the Result of Step column, if available. | All migrated data is displayed in the corresponding SAP S/4HANA Cloud Public Edition app. |  |

|  |
| --- |
| Note Check the [migration object documentation](https://help.sap.com/s4_ce_mo) for the name of the required app and the corresponding business catalog. |

Result

All migrated data can be found in the corresponding business functions.

## Appendix

### ALE/IDoc Distribution After Data Migration

If you want to distribute data from your SAP S/4HANA Cloud Private Edition or SAP S/4HANA Cloud Public Edition system to other systems using master data integration, read the migration object documentation carefully before you start migrating the data with the Migration Cockpit.

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
- related-to :: [[01-solution-foundation-and-platform/test-script-data-migration-to-sap-s-4hana-from-staging-2q2-848]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BH3_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 31,413 chars in the whole document
