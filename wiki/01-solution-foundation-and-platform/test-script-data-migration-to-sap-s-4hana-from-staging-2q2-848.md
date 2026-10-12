---
id: 01-solution-foundation-and-platform/test-script-data-migration-to-sap-s-4hana-from-staging-2q2-848
title: "Test Script: Data Migration to SAP S/4HANA from Staging (2Q2) (2Q2_S4CLD2608_BPD_EN_XX)"
description: "S/4HANA Cloud Public Edition test script (scope item 2Q2): migrating data via staging tables with the migration cockpit, plus roles and finance/logistics notes."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/data-migration-cockpit]
aliases: [2Q2_S4CLD2608_BPD_EN_XX]
keywords: [Data Migration with the Migration Cockpit (Direct Transfer…, data migration, migration cockpit, staging tables, migration projects, migration templates, migration simulation, data migration status, data validation, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2Q2_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-848
topic: 01-solution-foundation-and-platform/data-migration-cockpit
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Data Migration to SAP S/4HANA from Staging (2Q2) (2Q2_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2Q2_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Data Migration with the Migration Cockpit (Direct Transfer and Staging Tables)** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Data Migration to SAP S/4HANA from Staging (2Q2) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232841865)

[2 Prerequisites 4](#_Toc232841866)

[2.1 System Access 4](#_Toc232841867)

[2.2 Roles 4](#_Toc232841868)

[2.2.1 Technical Business Role Templates for Data Migration 4](#_Toc232841869)

[2.2.2 Additional Business Catalogs Needed for Data Migration 5](#_Toc232841870)

[3 Migration Objects for SAP S/4HANA Cloud Public Edition 6](#_Toc232841871)

[4 Preliminary Steps 7](#_Toc232841872)

[4.1 Create and Assign Business Role for Data Migration 7](#_Toc232841873)

[5 Additional Manual Configuration 9](#_Toc232841874)

[5.1 Set Up Database Connection 9](#_Toc232841875)

[5.1.1 Create SAP HANA Cloud Instance 9](#_Toc232841876)

[5.1.2 Set Up Communication Arrangement 9](#_Toc232841877)

[6 Business Conditions 10](#_Toc232841878)

[7 Overview Table 11](#_Toc232841879)

[8 Test Procedures 12](#_Toc232841880)

[8.1 Start the SAP S/4HANA Migration Cockpit 12](#_Toc232841881)

[8.2 Create Migration Project 13](#_Toc232841882)

[8.3 Fill Staging Tables Using Migration Templates 14](#_Toc232841883)

[8.4 Fill Staging Tables Using Your Preferred Tools 15](#_Toc232841884)

[8.5 Prepare and Simulate the Migration 17](#_Toc232841885)

[8.6 Migrate Data to the Target System 18](#_Toc232841886)

[8.7 Check Data Migration Status 18](#_Toc232841887)

[8.8 Validate Imported Data 20](#_Toc232841888)

[9 Appendix 22](#_Toc232841889)

[9.1 General Topics and Limitations 22](#_Toc232841890)

[9.1.1 Unit of Measure Conversion 22](#_Toc232841891)

[9.1.2 ALE/IDoc Distribution After Data Migration 22](#_Toc232841892)

[9.2 Financials 22](#_Toc232841893)

[9.2.1 Document Types for Data Migration 22](#_Toc232841894)

[9.2.2 Document Date 22](#_Toc232841895)

[9.2.3 *Define Settings for Legacy Data Transfer* (FINS_MIG_CTRL_1) 23](#_Toc232841896)

[9.2.4 Transfer Booking Account 24](#_Toc232841897)

[9.2.5 Migrate Financial Plan Data 24](#_Toc232841898)

[9.3 Logistics 25](#_Toc232841899)

[9.3.1 Advanced Variant Configuration 25](#_Toc232841900)

[9.4 FAQs 26](#_Toc232841901)

## Purpose

Overview

With SAP S/4HANA Cloud Public Edition, you can use the included SAP S/4HANA migration cockpit to migrate your data. When you choose the Migrate Data Using Staging Tables approach, the SAP S/4HANA migration cockpit creates staging tables for the migration objects that are relevant for your project and migrates the data from these staging tables to the target SAP S/4HANA Cloud Public Edition system.

- If you use the Local SAP S/4HANA Database Schema option, the SAP S/4HANA migration cockpit generates the staging tables in the local ABAP schema of the SAP S/4HANA Cloud Public Edition system. We recommend using this option if you want to populate the staging tables using the template files provided by SAP.
- If you use the Remote SAP HANA Database Schema option, you specify the relevant connection to a remote SAP HANA system. The SAP S/4HANA migration cockpit generates the staging tables there. The set-up instructions provided for this scope item are only relevant for this option.

|  |
| --- |
| Note The scope item covers some technical prerequisites. Please note that additional costs may apply. For the successful communication configuration between the SAP HANA Cloud instance and the SAP S/4HANA migration cockpit, you need to have set up SAP HANA Cloud on the SAP Business Technology Platform. After activation, you need to set up the communication arrangement SAP_COM_0678. |

|  |
| --- |
| Note SAP S/4HANA refers to the default on-premise suite on the SAP HANA platform, SAP S/4HANA Cloud Public Edition refers to our cloud suite on SAP Business Technology Platform. |

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

|  |
| --- |
| Caution Data protection legislation may require that personal data is deleted once the data has served its originally defined purpose and is also no longer subject to additional legal data retention requirements. If data protection legislation is applicable in your case, then migrating personal data that should have been deleted could be interpreted as the processing of personal data without any legally justified purpose. |

|  |
| --- |
| Note Migration objects are built for initial migration of your data to your SAP S/4HANA Cloud Public Edition system. This means that you can create data with a migration object, but you can't change or update existing data with it.For some migration objects there are "Extend" migration objects available, that you can use to extend existing data to other organizational levels. If you want to change or update existing data, use the respective maintenance apps (available for all business objects) or mass processing apps (these are only available for selected business objects). Please note that such apps fall outwith the responsibility of data migration development. |

To get the latest information about the SAP S/4HANA migration cockpit, also check SAP Note [2538700](https://me.sap.com/notes/2538700) - Collective SAP Note and FAQ for SAP S/4HANA migration cockpit - File/Staging (Cloud / SAPSCORE)

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP Business Technology Platform | In case you're using the Remote SAP HANA Database Schema, you have to create an SAP HANA Cloud instance on SAP Business Technology Platform with your Global account for SAP Business Technology Platform. The SAP HANA Cloud instance is needed to create the staging tables used by the SAP S/4HANA migration cockpit. Refer to the [2Q2](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/2Q2) set-up instructions on SAP Signavio Process Navigator for more information about how to create a SAP S/4HANA Cloud Public Edition instance on SAP Business Technology Platform. |

### Roles

#### Technical Business Role Templates for Data Migration

Use the following business role templates to access the Migrate Your Data - Migration Cockpit (F3473), Data Migration Status (F3280), and Define Settings for Legacy Data Transfer (FINS_MIG_CTRL_1) apps:

| ID (Role Template) | Name (Role Template) | ID (Launchpad Space) | Name (Launchpad Space) |
| --- | --- | --- | --- |
| SAP_BR_CONFIG_EXPERT_DATA_MIG | Configuration Expert - Data Migration | SAP_BR_CONFIG_EXPERT_DATA_MIG | Data Migration |
| Only required if Remote SAP HANA Database Schema is used:SAP_BR_CONF_EXPERT_BUS_NET_INT | Configuration Expert - Business Network Integration | SAP_CORE_SPT_INT_PC / SAP_CON_SPT_CONCUR_INT_PC / SAP_OC_SPT_INT_PC / SAP_CA_SPT_DATA_REP_PC / SAP_CA_SPT_BUS_NETWORK_INT_PC | Business Network Integration / Business Network Integration - Concur Integration / Business Network Integration - Output Control / Business Network Integration - Data Replication / Configuration Expert - Business Network Integration Cross Applications |

#### Additional Business Catalogs Needed for Data Migration

In addition to the business catalogs that are part of the [Technical Business Role Templates for Data Migration](#unique_4) [page ] 4, the data migration user also needs business catalogs specific to the migration objects that are needed to migrate the related business objects.

You can find an extensive table listing all migration objects available for SAP S/4HANA Cloud Public Edition, as well as the business catalogs required for creation, in the [SAP S/4HANA Cloud Public Edition product assistance](https://help.sap.com/viewer/cc9ecc5f5f6b400a98d10e930324f7ad).

For some search helps for mapping tasks, there are additional authorization checks. These authorizations, however, might not be covered by the business catalog used for data migration for a specific migration object. In this case, refer to SAP Knowledge Base Article [3344907](https://launchpad.support.sap.com/#/notes/3344907).

## Migration Objects for SAP S/4HANA Cloud Public Edition

You can find an extensive table listing all migration objects available for SAP S/4HANA Cloud Public Edition, together with their respective migration object documentation, in the [SAP S/4HANA Cloud Public Edition product assistance](https://help.sap.com/viewer/cc9ecc5f5f6b400a98d10e930324f7ad) or via the short link [https://help.sap.com/S4_CE_MO](https://help.sap.com/S4_CE_MO).

## Preliminary Steps

Use

In these steps, you set up the necessary user settings for migrating your data.

### Create and Assign Business Role for Data Migration

Use

You create and assign the required business role for data migration using the business role template mentioned under [Technical Business Role Templates for Data Migration](#unique_4) [page ] 4 and adjust it to the user's requirements.

Prerequisites

To create a business role for your data migration user, you need to know the migration objects that they want to use in their migration project. You then need to add the respective business catalogs to their business role. Refer to [Additional Business Catalogs Needed for Data Migration](#unique_5) [page ] 5.

Procedure

1. Log on to SAP Fiori launchpad as an administrator. Open the Maintain Business Roles (F1492) app. On the initial screen, select Create From Template to create a new role based on the technical business role template for data migration.
2. Select the required template as listed under [Technical Business Role Templates for Data Migration](#unique_4) [page ] 4. Define the ID and the description of the new business role. Choose OK.
3. On the Assigned Business Catalogs tab, you can see which catalogs are already assigned to this role. To be able to migrate data, you need to add additional catalogs according to the data migration user's requirements. Add the required business catalogs for the migration objects that the data migration user wants to use in their migration project. Refer to [Additional Business Catalogs Needed for Data Migration](#unique_5) [page ] 5.
4. Choose Maintain Restrictions. By default, the Read, Value Help category for each business catalog is set to Unrestricted and the user has no write access. For data migration, you also need to set the Write, Read, Value Help category to Unrestricted.
5. On the Assigned Business Users tab, you can assign the data migration users to your new business role. These users will receive the authorizations as defined in the business role.
6. Save the business role to activate it.

|  |
| --- |
| Note If you go back to the business roles overview without saving the business role, the business role will automatically be saved in a draft status. You can access it again and edit it from the business roles overview. |

Result

The data migration user now has the authorization that they need in order to conduct their migration project.

## Additional Manual Configuration

|  |
| --- |
| Note The additional manual configuration that is described here is only necessary if you are using the "Remote SAP HANA Database Schema" option. If your are using the “Local SAP S/4HANA Database Schema” option, you can skip this section. |

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/0b0e955d215a17a9ff23d9a84f152351)

### Set Up Database Connection

To use the transfer option staging tables of the SAP S/4HANA migration cockpit, you first must first deploy the SAP HANA Cloud instance on SAP Business Technology Platform and set up the communication arrangement to allow the migration cockpit to communicate with these tables.

#### Create SAP HANA Cloud Instance

To migrate data to SAP S/4HANA Cloud Public Edition by using the staging tables functionality of the SAP S/4HANA migration cockpit, you must first deploy the SAP HANA Cloud instance on SAP Business Technology Platform.

Find more information about creating SAP HANA Cloud instances [here](https://help.sap.com/viewer/9ae9104a46f74a6583ce5182e7fb20cb/latest/en-US/784a1dbb421a4da29fb1e3bdf5f198ec.html) and in the [2Q2](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/2Q2) set-up instruction on SAP Signavio Process Navigator.

#### Set Up Communication Arrangement

The database connection between the SAP S/4HANA Cloud Public Edition tenant and the SAP HANA Cloud instance is created via a communication arrangement of the Migration Cockpit Integration communication scenario.

Refer to the [2Q2](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/2Q2) set-up instructions on SAP Signavio Process Navigator.

## Business Conditions

If you are using the Remote SAP HANA Database Schema option, the following business conditions have to be met, before this scope item can be tested.

| Business Condition |
| --- |
| With the Remote SAP HANA Database Schema:Acquire SAP Business Technology Platform user and passwordSAP HANA Cloud instance is set up in SAP Business Technology PlatformCommunication arrangement is activated in SAP S/4HANA Cloud Public Edition system for communication with an SAP HANA database |
| Content is activated |
| Org. structures and additional settings are made. |

## Overview Table

This scope item consists of several process steps provided in the table below.

| Process Step | UI Type | Business Condition | Expected Results |
| --- | --- | --- | --- |
| [Start the SAP S/4HANA Migration Cockpit](#unique_15) [page ] 12 | Migration Cockpit | This section describes how you start the SAP S/4HANA migration cockpit. | The migration cockpit is displayed. |
| [Create Migration Project](#unique_16) [page ] 13 | Migration Cockpit | This section describes how you create a migration project in the migration cockpit. | A migration project is created. |
| [Fill Staging Tables Using Your Preferred Tools](#unique_17) [page ] 15 | Migration cockpit (Web Dynpro) | This section describes how you fill staging tables. | The staging table is opened and new data is entered. |
| [Prepare and Simulate the Migration](#unique_18) [page ] 17 | Migration Cockpit | This section describes the steps necessary to prepare for the final migration. | The data is ready to be migrated to the target system. |
| [Migrate Data to the Target System](#unique_19) [page ] 18 | Migration Cockpit | This section describes how you import your data into the target system. | The data is transferred from the staging table to the target system. |
| [Check Data Migration Status](#unique_20) [page ] 18 | Data Migration Status app | This section describes how you use the Data Migration Status (F3280) app to check the status of your migration projects and objects. | You are up-to-date with the status of your migration projects and objects. Necessary changes in migration projects can then be made. |
| [Validate Imported Data](#unique_21) [page ] 20 | SAP Fiori launchpad | This section describes how you validate completeness and correctness of the migrated data in the target system using corresponding business functions. | All data from the staging table can be found in the corresponding business functions. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Start the SAP S/4HANA Migration Cockpit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This section describes how you start the SAP S/4HANA migration cockpit.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Start SAP Fiori launchpad | Log on to your SAP S/4HANA Cloud Public Edition system. | The Home page appears. |  |
| 2 | Open Migration Cockpit | Choose the Migrate Your Data - Migration Cockpit (F3473) tile. |  |  |

|  |
| --- |
| Note For more information on the SAP S/4HANA migration cockpit in SAP S/4HANA Cloud Public Edition, see the [product assistance on SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/f32db0c240484241abc53a876253e118.html). |

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
| 1 | Create Migration Project | Choose Create on the Migration Projects home screen. | The New Migration Project dialog window appears. |  |
| 2 | Choose Settings for Migration Project | Make the required entry in the New Migration Project dialog window:Name:Name of your migration project.Mass Transfer ID:See note below this table.Database Connection:If you want to use staging tables that are located in the local ABAP schema, choose the option Local SAP S/4HANA Database Schema.If you want to use files to fill the staging tables with data, choose the option Local SAP S/4HANA Database Schema. The system generates the staging tables in the internal schema of the SAP S/4HANA system.If you want to use staging tables that are located in an SAP HANA schema that isn’t the local ABAP schema of your system, select the option Remote SAP HANA Database Schema and enter a valid database connection to the staging system or choose one from the search help list.[See the product assistance for further information.](https://help.sap.com/viewer/d5699934e7004d048c4801b552f3b013/latest/en-US/aa6a939478474887a411a73aea67a624.html)After making the required entries, choose Step 2. |  |  |
| 3. | Choose Migration Objects | Choose all relevant migration objects for your project. Then, choose the arrow to add them to the Selected Migration Object table on the right-hand side. When you’ve finished your selection, choose Review. |  |  |
| 4 | Add Dependent Objects (optional) | The system checks for dependent object and might ask you whether you want to add additional migration objects to your project. For more details, choose View Details.Choose Add or Do Not Add as required. | An overview page with your project settings is displayed. |  |
| 5 | Create Migration Project | Double-check your project settings and choose Create Project. |  |  |

|  |
| --- |
| Note After an SAP S/4HANA Cloud Public Edition release upgrade, any new migration objects won’t get added to existing migration projects. To be able to use new migration objects, you need to create a new migration project. If there are still migration objects missing after creating a new migration project, please see SAP Note [2538700](https://me.sap.com/notes/2538700) for further information. |

Further Information

Find [further information about project settings](https://help.sap.com/viewer/d5699934e7004d048c4801b552f3b013/latest/en-US/08b9a967045643bd8c80fdc29e70b944.html) in the product assistance on SAP Help Portal.

### Fill Staging Tables Using Migration Templates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This section describes how you transfer your data from the migration template to staging tables.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Download Template | On the Migration Project screen, select the relevant migration object and choose Download Template. |  |  |
| 2. | Fill in Template | Enter the data you want to migrate into the template and save your file. |  |  |
| 3. | Upload File | On the Migration Project screen, select the relevant migration object and choose the action Upload File.The system displays the Migration Object Tables screen. On the Files tab, you upload the files and view the status of the validation and transfer process. To upload a file, you can either choose Upload or use the drag and drop function.The system uploads the file to the SAP S/4HANA migration cockpit. On the Files tab, you can view the status of the upload. |  |  |
| 4. | Validate Data | The system validates the data in the file. On the Files tab, you can view the status of the validation as well as information such as the time the process was started.[Find more information about issue handling and validation in the product assistance.](https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/47082e0d2baf40f5854f429dea179706.html) |  |  |
| 5. | Transfer Data | Once the file has been validated successfully, the system automatically starts transferring the data in the file to the staging tables that were generated for that migration object. Once all the data in the file has been transferred to the staging tables, the system displays the information Data Successfully Transferred to Staging Tables. You can also view information such as the number of transferred migration object instances. |  |  |

### Fill Staging Tables Using Your Preferred Tools

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

You can fill the staging tables manually or by using your preferred tools (for example SAP Data Services or SAP Smart Data Integration, SDI).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Fill Staging Tables | Fill the staging tables manually or by using your preferred toolsNote Make sure the key fields, the mandatory fields and fields' default initial values contain valid data.More information can be found in SAP Note [2733253](https://me.sap.com/notes/2733253) – FAQ for SAP S/4HANA migration cockpit. Migration approach: Transfer / Migrate data from staging tables, and in SAP Community Blogs, for example, [here](https://blogs.sap.com/2019/12/02/sap-s-4-hana-migration-cockpit-migrating-data-using-staging-tables-and-methods-for-populating-the-staging-tables/). | The staging table contains the data. |  |

Additional Information

|  |  |  |
| --- | --- | --- |
| Filling staging tables... | Using a secondary database connection"Remote SAP HANA Database" | Using the same scheme "Local SAP HANA Database" |
| In SAP S/4HANA Cloud Public Edition | SAP Business Technology PlatformVia openSQL, third party ETL Tools or from SAP like SAPHANA Studio, SDI, ADP, SAP Data Services | Only via XML or CSV template files |

- Sometimes it's necessary to synchronize staging tables with migration objects. Reasons for that could be changed default views of the migration project, changed active views of the migration object, or changed migration object content. The staging tables that must be changed have the status Synchronization Required. You must synchronize these tables before you can use them for data transfer.
    - To synchronize all the staging tables of a migration object, choose Start Synchronization on the Migration Object Details screen.
    - To synchronize a single staging table, choose Start Synchronization on the Staging Table Details screen of the table.
- To show the documentation of the staging table go to the staging table details screen and choose Show. A window appears that shows information about Field Name, Group, and Description, as well as which field is Key and which field is Mandatory.
- If you fill the SAP HANA staging tables with values, be aware of the following datatypes and the rules:
    - Date fields might be shown in SAP HANA as NVARCHAR length 8 with DEFAULT 00000000. The format of the value is YYYYMMDD, so 2018-DEC-31 must be entered 20181231. Initial values must be set to the defined DEFAULT value.
    - Time fields might be shown in SAP HANA as NVARCHAR length 6 with DEFAULT 000000. The format of the value is HHMMSS, so 2:34:12 pm/14:34:12 must be entered 143412. Initial values must be set to the defined DEFAULT value.
    - Numerical character fields of ABAP data type NUMC must contain leading zeros. You can determine such fields as they are NVARCHAR with a default value with one zero minimum. So NVARCHAR (3) with DEFAULT 000 is a NUMC field with length 3. The value 90, for example, must be entered as 090, the value 0 as 000. You can cross-check this when you download the template for this object in a project with transfer option Transfer Data from File. The field is shown in the field list of the template as number with length 3 and 0 decimals.
    - Decimal values must have a '.' as decimal separator.

Find more information on this in SAP Note [2733253](https://me.sap.com/notes/2733253) – FAQ for SAP S/4HANA migration cockpit - Transfer option: Transfer data from staging tables.

Result

The system created the staging tables automatically, and you entered new data using your preferred tools.

### Prepare and Simulate the Migration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

Before migrating your data to the productive system, you need to conduct a couple of preparational steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Prepare the Staging Tables | On the Migration Project screen, select the relevant migration object.In the Action column, choose Prepare.The system will prepare the staging tables so that they can be used to transfer your data. |  |  |
| 2. | Complete Mapping of Data | You need to process any open mapping tasks for the migration object before you can proceed with the simulation or the migration.On the Migration Project screen, in the Mapping Tasks column, you can view the number of open and completed tasks for each migration object.[Find more information about mapping tasks in the product assistance.](https://help.sap.com/docs/SAP_S4HANA_CLOUD/d5699934e7004d048c4801b552f3b013/76cbbf659549445384b91ffd0353b698.html?locale=en-US) |  |  |
| 3. | Simulate the Migration | Once you have processed all open tasks for a migration object and prepared the staging tables, you can simulate the transfer of dataOn the Migration Project screen, select the relevant migration object and choose Actions and then Simulate. The system simulates the migration for all migration object instances in the staging tables for the migration object. |  |  |

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
| 1. | Migrate Data | On the Migration Project screen, select the relevant migration object and choose the action Migrate. The system will migrate all migration object instances in the staging tables for the migration object. |  |  |

Result

The data is transferred from the staging table to the target system.

### Check Data Migration Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This section describes how you use the Data Migration Status (F3280) app to check the status of your migration projects and objects.

Prerequisite

You've started migrating data to your SAP S/4HANA Cloud Public Edition system for at least one migration object.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open Data Migration Status app | Choose the Data Migration Status (F3280) app. | The Data Migration Status page appears. Here you can see an overview of all migration objects that you've started using so far. The table shows the total number of records, the number of imported records, the number of records that are ready for import, and the number of failed records. In the right column you find a progress bar on the status of your objects. |  |
| 2 | Optional: Apply Filters | You can apply filters on the overview table to find the object you're looking for faster. Therefore, choose Expand Header and the filter header expands. You can use the first field for free text search, or you can use the Migration Period, Migration Project, Object Name, and Record Status fields for your query. After you've entered the desired values, choose Go. | The table is filtered according to your requirements. |  |
| 3 | Drill Down on a Migration Object | For more information on a migration object, just choose the name of the respective object. | A pane opens on the right side. In the first table in this pane, you find an overview of all Records of this migration object. This table shows the Source ID, Status, Description, Project, and Audit Status. In the second table in this pane, you find an overview of all Messages of this migration object. This table shows all Message Types, Messages, and the Number of messages. |  |
| 4 | Optional: Apply Filters | You can apply filters on both the Records and the Messages table to find the record or message you're looking for faster. For the Records table, you can use the field for free text search on the right side, or you can use the dropdown list on the left side to filter for the Status or the Audit Status of the records. For the Messages table, you can use the message type options – Error and Warning – to filter for the Message Type. | The table is filtered according to your requirements. |  |
| 5 | Drill Down on a Record or a Message | For more information on a record or a message, just choose the name of the respective object. | A pane opens on the right side. In this pane, you find detailed information on the record or the message. |  |
| 6 | Close all Panes | You can close every pane by choosing the close symbol in the upper right corner of the pane. | The panes are closed and you're back on the Data Migration Status page. |  |

Result

You are up-to-date with the status of your migration projects and objects, and you can make the necessary changes in your migration projects.

Further Information

Make sure you read the [SAP S/4HANA Cloud Public Edition product assistance](https://help.sap.com/viewer/d5699934e7004d048c4801b552f3b013/latest/en-US/30b5a3e91d0d469bb321360586003211.html). There, you can find detailed information on the features of the Data Migration Status app, for example how to use the audit function, how to set up notifications, and lots more.

You can find frequently asked questions relating to the Data Migration Status app in the SAP Knowledge Base Article [2681413](https://me.sap.com/notes/2681413).

### Validate Imported Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This section describes how you validate completeness and correctness of the migrated data in the target system using corresponding business functions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Corresponding App | Open the corresponding app of the SAP S/4HANA Cloud Public Edition system and check completeness of the imported data. | All migrated data is displayed in the corresponding SAP S/4HANA Cloud Public Edition app. |  |

|  |
| --- |
| Note Check the [migration object documentation](https://help.sap.com/s4_ce_mo) for the name of the required app and the corresponding business role, or for the required backend transaction to validate the data in the system. |

Result

All migrated data can be found in the corresponding business functions.

## Appendix

### General Topics and Limitations

#### Unit of Measure Conversion

Find detailed information in SAP Knowledge Base Article [2907822](https://me.sap.com/notes/2907822).

#### ALE/IDoc Distribution After Data Migration

If you want to distribute data from your SAP S/4HANA Cloud Public Edition system to other systems via Application Link Enabling (ALE), carefully read SAP Knowledge Base Article [2858316](https://me.sap.com/notes/2858316) before you start migrating the data using the SAP S/4HANA migration cockpit.

### Financials

#### Document Types for Data Migration

The document type for all open item and open balance migration objects can be freely chosen and entered into the Document Type field.

For migration of general ledger balances, we recommend the document type UE, and for open item migration objects, we recommend the document types DR (Customer Invoice) and KR (Vendor Invoice), respectively.

#### Document Date

The document date must be the same date as in the original data record.

#### Define Settings for Legacy Data Transfer (FINS_MIG_CTRL_1)

Migration Key Date/Posting Date for Financial Documents

Before you go live with SAP S/4HANA Cloud Public Edition, you may want to do an initial transfer of open balances and open items from a legacy system to your SAP S/4HANA Cloud Public Edition system. You transfer such data using the SAP S/4HANA migration cockpit.

To ensure a proper transfer of your legacy financial transactional data, use the Define Settings for Legacy Data Transfer (FINS_MIG_CTRL_1) app to maintain the migration key date on which you want to complete all preparatory activities for each company code before the actual data transfer.

The migration key date must allow for you to complete the following actions:

- Complete all postings available up to this date, in full, in the source system
- Reconcile and close the journals in the source system for the period
- Extract source data and enter it into the migration templates
- Clean and convert data as needed
- Validate the imported data against your legacy system

The date chosen is usually the end of a period (month, quarter, year) since this will fit in with the normal reconciliation cycle.

Please note that the migration key date is also used as the posting date when the legacy data is actually transferred to your SAP S/4HANA Cloud Public Edition system.

Set the Legacy Data Transfer Status for each migration key date provided:

- In Preparation: migration key date is still unclear (migration of transactional data is not possible)
- Ongoing: required for the initial data transfer (migration of transactional data is possible)
- Completed: after successful completion of the initial data transfer (migration of transactional data is not possible)

For the following financial objects, the posting date will be automatically derived by the predefined migration key date for the related company code which is maintained via the aforementioned app:

- FI - Accounts payable open item
- FI - Accounts receivable open item
- FI - G/L account balance and open/line item
- Material inventory balance
- FI - Historical balance (deprecated) (migration key date is required to allow the migration of historical balances only up until this initial transfer date)

Exception

- For the financial object FI-CA - Open item, a field for posting date is available on the migration template. The posting date is marked as mandatory on the template and must be provided for each data record. The migration key date has no additional effect on the provided posting date.
- For the financial object Fixed asset - Master data, use the Make Company Code Settings - Asset Accounting-Specific (F7312) app to specify the data transfer date, document type, and the legacy data transfer status.

|  |
| --- |
| Note See also [General Ledger Accounting > Current Settings in the SAP S/4HANA Cloud Public Edition product assistance](https://help.sap.com/viewer/0fa84c9d9c634132b7c4abb9ffdd8f06/latest/en-US/ac2759e115d64984b32bc4eacb4bd418.html) for further information on the configuration of the Migration Key Date before migrating transactional data. |

#### Transfer Booking Account

The transfer booking accounts to be used for the Open item and Open balance migration objects are as follows:

| Account | Description | Migration Cockpit Object Name |
| --- | --- | --- |
| 39911000 | Initial Entry of Raw Material Balances | Material inventory balance |
| 39912000 | Initial Entry SF & Finish Gds Balances | Material inventory balance |
| 39913000 | Initial FI-AM offset | Fixed asset - Postings |
| 39914000 | Initial FI-AR offset | FI - Accounts receivable open item |
| 39915000 | Initial FI-AP offset | FI - Accounts payable open item |
| 39916000 | Initial other G/L offset | FI - G/L account balance and open/line item |
| 39917000 | Initial other Open Item G/L offset | FI - G/L account balance and open/line item |

#### Migrate Financial Plan Data

If you have financial plan data in your legacy system that you want to import to your SAP S/4HANA system, you may do so by using the Import Financial Plan Data (F1711)

By using this app, you can import periodic financial plan data for the following planning areas:

- Cost Centers
- Projects
- Profit Centers
- Market Segments
- P&L
- Balance Sheet
- Functional Areas

For further information on this app, check the [SAP Fiori apps reference library](https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/?appId=F1711) and refer to the [online help](https://help.sap.com/docs/SAP_S4HANA_CLOUD/1cbcff7ccd35405ab445b223c1ab1588/c5e0cd55db8c3105e10000000a44538d.html).

### Logistics

#### Advanced Variant Configuration

To create objects of a configuration model, create the objects in the following order:

| # | Object Name | Comments |
| --- | --- | --- |
| 1 | ECM - Change master | If you want to use a change number, create a new change number first. |
| 2 | Document info record |  |
| 3 | Characteristic | Dependencies must be added manually. |
| 4 | Class |  |
| 5 | VC - Variant table structure |  |
| 6 | VC - Variant table entry |  |
| 7 | VC - Object dependencies | Only for global dependencies. Create object dependencies with status Released. In case of a syntax error in the dependency the creation of this dependency will be prevented. |
| 8 | Product |  |
| 9 | Object classification - General template |  |
| 10 | VC - Constraint |  |
| 11 | VC - Dependency net |  |
| 12 | VC - Configuration profile |  |
| 13 | Material BOM |  |

|  |
| --- |
| Note Migration of local dependencies is currently not supported for all objects. Please read the migration object documentation carefully to determine which objects support this. |

### FAQs

For frequently asked questions regarding migrating data using the SAP S/4HANA migration cockpit, see SAP Knowledge Base Article [2733253](https://me.sap.com/notes/2733253).

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
- related-to :: [[01-solution-foundation-and-platform/test-script-data-migration-to-sap-s-4hana-from-sap-bh3-1268]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2Q2_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 44,097 chars in the whole document
