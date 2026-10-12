---
id: 12-production-and-manufacturing/test-script-bill-of-material-management-64f-ae-sap-s-4hana-cloud-publi
title: "Test Script: Bill of Material Management (64F_AE) - SAP S/4HANA Cloud Public Edition (64F_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 64F: BOM creation, major/minor change, handover to manufacturing, where-used and mass maintenance."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/material-boms]
aliases: [64F_S4CLD2608_BPD_EN_AE]
keywords: [Material BOMs for Production and Sales, bill of material management, bill of material creation, change masters, bom changes, preliminary bom items, bom groupings, where-used mass replacement, engineering to manufacturing bom, bom mass maintenance]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/64F_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1150
topic: 12-production-and-manufacturing/material-boms
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Bill of Material Management (64F_AE) - SAP S/4HANA Cloud Public Edition (64F_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/64F_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Material BOMs for Production and Sales** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Bill of Material Management (64F_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232858089)

[2 Prerequisites 4](#_Toc232858090)

[2.1 Additional Manual Configurations 4](#_Toc232858091)

[2.2 System Access 4](#_Toc232858092)

[2.3 Roles 4](#_Toc232858093)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232858094)

[2.5 Business Conditions 7](#_Toc232858095)

[2.6 Preliminary Steps 7](#_Toc232858096)

[2.6.1 Prepare Design Document 7](#_Toc232858097)

[2.6.2 Configure Bill of Materials (Optional) 7](#_Toc232858098)

[3 Overview Table 9](#_Toc232858099)

[4 Test Procedures 13](#_Toc232858100)

[4.1 Create and Change Bill of Material 13](#_Toc232858101)

[4.1.1 Create Bill of Material 13](#_Toc232858102)

[4.1.1.1 Define Effectivity of the BOM Changes 13](#_Toc232858103)

[4.1.1.2 Create Bill of Material 14](#_Toc232858104)

[4.1.1.3 Add Preliminary BOM Components (Optional) 17](#_Toc232858105)

[4.1.1.4 Create BOM Groupings (Optional) 19](#_Toc232858106)

[4.1.1.5 Release Change 20](#_Toc232858107)

[4.1.2 Change Bill of Material 21](#_Toc232858108)

[4.1.2.1 Major Change 21](#_Toc232858109)

[4.1.2.1.1 Define Effectivity of the BOM Changes 21](#_Toc232858110)

[4.1.2.1.2 Copy (Create) Header Material (Optional) 23](#_Toc232858111)

[4.1.2.1.3 Copy BOM 24](#_Toc232858112)

[4.1.2.1.4 Change Bill Of Material 25](#_Toc232858113)

[4.1.2.1.5 Release Change 26](#_Toc232858114)

[4.1.2.2 Minor Change 27](#_Toc232858115)

[4.1.2.2.1 Change BOM 27](#_Toc232858116)

[4.1.2.2.2 Release Change 29](#_Toc232858117)

[4.1.3 Replace Preliminary Items (Optional) 30](#_Toc232858118)

[4.1.3.1 Replace Preliminary Component with Actual Material 30](#_Toc232858119)

[4.1.4 Where-used and Mass Replacement 32](#_Toc232858120)

[4.1.4.1 Define Effectivity of the BOM Changes 32](#_Toc232858121)

[4.1.4.2 Execute Where-Used for Component to Replace 33](#_Toc232858122)

[4.1.4.3 Replace Material for the Selected BOMs 34](#_Toc232858123)

[4.1.4.4 Release Change 35](#_Toc232858124)

[4.2 Basic Handover 36](#_Toc232858125)

[4.2.1 Define Effectivity of the BOM Changes 36](#_Toc232858126)

[4.2.2 Copy Engineering BOM to Manufacturing BOM 37](#_Toc232858127)

[4.2.3 Adjust Manufacturing BOM for Production 39](#_Toc232858128)

[4.2.4 Release Change 40](#_Toc232858129)

[4.3 Mass Maintenance of Bill of Material 41](#_Toc232858130)

[4.3.1 Perform Mass Maintenance of Bill of Material Items 41](#_Toc232858131)

[4.3.1.1 Define Effectivity of the BOM Changes 41](#_Toc232858132)

[4.3.1.2 Mass Maintenance of BOM Items 42](#_Toc232858133)

[4.3.1.3 Simulate Mass Change of BOM Items 44](#_Toc232858134)

[4.3.1.4 Execute Mass Change of BOM Items 45](#_Toc232858135)

[4.3.1.5 Release Change 46](#_Toc232858136)

[4.3.2 Perform Mass Addition of Bill of Material Items 47](#_Toc232858137)

[4.3.2.1 Define Effectivity of the BOM Changes 47](#_Toc232858138)

[4.3.2.2 Mass Addition of BOM Items 48](#_Toc232858139)

[4.3.2.3 Simulate Mass Addition of BOM Items 49](#_Toc232858140)

[4.3.2.4 Execute Mass Addition of BOM Items 50](#_Toc232858141)

[4.3.2.5 Release Change 51](#_Toc232858142)

[4.3.3 Perform Mass Maintenance of Bill of Material Headers 52](#_Toc232858143)

[4.3.3.1 Define Effectivity of the BOM Changes 52](#_Toc232858144)

[4.3.3.2 Mass Maintenance of BOM Headers 53](#_Toc232858145)

[4.3.3.3 Simulate Mass Change of BOM Headers 55](#_Toc232858146)

[4.3.3.4 Execute Mass Change of BOM Headers 56](#_Toc232858147)

[4.3.3.5 Release Change 57](#_Toc232858148)

## Purpose

Overview

Bill of Material Management provides the following functionalities:

- Create and maintain single and multi-level bills of material (BOMs).
- Using change masters, different effectivities of BOM changes on component level can be defined, revisioned planned, and released.
- The Where-Used capability allows BOM engineers to find all occurrences of a certain component across BOMs. In combination with a mass replace function, component replacements can easily be managed.
- BOM engineers can use BOM groupings to represent the modular structure of the product in a multilevel BOM, group component variants in variant BOMs, and group a BOM without creating additional materials.
- Using preliminary BOM items, the BOM engineer can describe the custom engineered components in engineer-to-order and customer-to-order scenarios (such as in the tendering phase) without creating materials, and can create placeholders for later enhancement of business objects, such as documents or materials.
- With requirements-driven development, requirements and block definition diagrams can be linked to product lifecycle management objects such as document info records, materials, and configurable BOMs.
- Perform mass maintenance of BOMs

The BOM Engineers can select the relevant BOMs with comprehensive search functions and then add, change, or delete BOM items, as well as change or delete BOM headers across the whole selection in one step. The BOM Engineers can also simulate BOM changes prior to executing and releasing them. The execution protocol helps to re-execute changes that could not be processed.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configurations

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

### System Access

| Resource | Details |
| --- | --- |
| System | Accessible through the SAP Fiori launchpad. Your system administrator provides you the URL to access various apps assigned to your role. |
| Cloud Foundry System (Enterprise Architecture Designer) | Your system administrator provides you with the URL of the SAP Cloud Foundry to access the SAP Enterprise Architecture Designer application.For more information about administering the application, search for the Administering SAP Enterprise Architecture Designer, cloud edition guide on SAP Help Portal.Ensure that the user is created with the required authorizations. For more information, see the sections Creating Repository Groups, Granting Rights to Users and Groups, and Granting Access Permissions on Repository Items in the guide.Note To assign the requirements as mentioned in each test procedure, you need to select the following check box : Edit Extensions on Web. For more information, refer Granting Rights to Users and Groups, in the guide. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| BOM EngineerThe BOM Engineer creates bills of material and consistent overall product model, drives changes across organizations, and is responsible for the change process until handover to manufacturing.Is typically a member of the R&D group of the company. | SAP_BR_BOM_ENGINEER | Bills Of Material | SAP_BR_BOM_ENGINEER |  |
| Production Engineer - Discrete ManufacturingMaintains the production-specific master data such as BOM, routing, and so on, for discrete manufacturing.Collaborates closely with the engineering and planning departments, production supervisors, and other people relevant to manufacturing. | SAP_BR_PRODN_ENG_DISC | Production Engineering - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | FG126 | Finished Good MTS for Discrete Industry (PD planning) | Note Create a new material each time when you re-execute the test script. Refer to the Master Data scripts(MDS) in this chapter for more information. |
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

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS (“ROH”) |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS (“HALB”) |
| BNT | Create Product Master of type "Finished Good" - MDS (“FERT”) |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BNR - Create Product Master of type "Raw Material" - MDS | You can create raw materials using the Create Material app. |
| BNS - Create Product Master of type "Semi-Finished Good" - MDS | You can create semi-finished products using the Create Material app. |
| BNT - Create Product Master of type "Finished Good" - MDS | You can create finished products using the Create Material app. |

### Preliminary Steps

#### Prepare Design Document

Design documents are provided by the Design Engineer and are an integral part of the Bill of Material concept.

Prepare a file in .pdf format (for instance a CAD drawing file representing the final assembly of the finished-good described by the Bill of Material); it will be used later in the process step 'Create Bill of Material'.

#### Configure Bill of Materials (Optional)

Purpose

In this step, you can update BOM-related configurations using the following SSCUIs as per your requirements.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, proceed with one of the following:

- Configure Your Solution:
    1. Log on to the SAP Fiori Launchpad in the SAP S/4HANA Cloud Public Edition system as Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).
    2. Navigate to Manage your Solution > Configure Your Solution.
    3. On the Configure Your Solution: Realize Phase screen, make the following entries:
        - Application Area: R&D/Engineering
        - Sub Application Area: Project Control and Product Development
    4. Go through the SSCUIs listed in the following table. Select each item and choose Configure.
- SAP Central Business Configuration:
    1. Log on to the project experience in SAP Central Business Configuration.
    2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the activities listed in the following table.
    3. Choose Open Documentation for the found line item to see more details about this configuration activity.
    4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.

| Configuration Step/SSCUI Title | Description | Configuration Step/SSCUI ID |
| --- | --- | --- |
| Define Material Types Allowed for BOM Header | Define Material Types Allowed for BOM Header | 101162 |
| Define Allowed Material Types for BOM Items | Define Allowed Material Types for BOM Items | 101163 |
| Define Item Categories | Define Item Categories | 102081 |
| Define Variable-Size Item Formulas | Define Variable-Size Item Formulas | 102815 |
| Define BOM Application for BOM Explosion | Define BOM Application for BOM Explosion | 103808 |
| Define BOM Usages | Define BOM Usages | 101915 |
| Define Default Values for the Item Status | Define Default Values for the Item Status | 101879 |
| Define Control Data for BOM Usage | Define Control Data for BOM Usage | 102164 |

## Overview Table

This scope item consists of several process steps, provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App / Transaction | Expected Results |
| --- | --- | --- | --- |
| Create and Change Bill of Material |  |  |  |
| Create Bill of Material |  |  |  |
| [Define Effectivity of the BOM Changes](#unique_12) [page ] 13 | BOM Engineer | Manage Change Masters (F2212) | A new change master is created. |
| [Create Bill of Material](#unique_13) [page ] 14 | BOM Engineer | Maintain Bill Of Material - Create, change & display BOMs (F1813) | A new bill of material managed with a change master is created. |
| [Add Preliminary BOM Components (Optional)](#unique_14) [page ] 17 | BOM Engineer | Maintain Bill Of Material - Create, change & display BOMs (F1813) | A new preliminary component is added to the newly created BOM. |
| [Create BOM Groupings (Optional)](#unique_15) [page ] 19 | BOM Engineer | Manage Multilevel Bill of Material (F5238) | BOMs are grouped as specified. |
| [Release Change](#unique_16) [page ] 20 | BOM Engineer | Manage Change Masters (F2212) | Change master status is set to Inactive. |
| Change Bill of Material |  |  |  |
| [Major Change](#unique_17) [page ] 21 |  |  |  |
| [Define Effectivity of the BOM Changes](#unique_18) [page ] 21 | BOM Engineer | Manage Change Masters (F2212) | A new change master is created. |
| [Copy (Create) Header Material (Optional)](#unique_19) [page ] 23 | Master Data Specialist - Product Data | Create Material (MM01) | A new material is created. |
| [Copy BOM](#unique_20) [page ] 24 | BOM Engineer | Maintain Bill Of Material - Create, change & display BOMs (F1813) | The existing BOM is copied to the newly created material. |
| [Change Bill Of Material](#unique_21) [page ] 25 | BOM Engineer | Maintain Bill Of Material - Create, change & display BOMs (F1813) | Specified changes are made to the copied BOM. |
| [Release Change](#unique_22) [page ] 26 | BOM Engineer | Manage Change Masters (F2212) | Change master status is set to Inactive. |
| [Minor Change](#unique_23) [page ] 27 |  |  |  |
| [Change BOM](#unique_24) [page ] 27 | BOM Engineer | Maintain Bill Of Material - Create, change & display BOMs (F1813) | Changes to the BOM are saved. |
| [Release Change](#unique_25) [page ] 29 | BOM Engineer | Manage Change Masters (F2212) | Change master status is set to Inactive. |
| Replace Preliminary Items (Optional) |  |  |  |
| [Replace Preliminary Component with Actual Material](#unique_26) [page ] 30 | BOM Engineer | Maintain Bill Of Material - Create, change & display BOMs (F1813) | Preliminary components are replaced with Stock or Non-stock items. |
| Where-used and Mass Replacement |  |  |  |
| [Define Effectivity of the BOM Changes](#unique_27) [page ] 32 | BOM Engineer | Manage Change Masters (F2212) | A new change master is created. |
| [Execute Where-Used for Component to Replace](#unique_28) [page ] 33 | BOM Engineer | Material where used list in BOMs - where used list, hierarchy and replace Materials in BOMs (F2214) | A where-used list is displayed for the selected component. |
| [Replace Material for the Selected BOMs](#unique_29) [page ] 34 | BOM Engineer | Material where used list in BOMs - where used list, hierarchy and replace Materials in BOMs (F2214) | The component is replaced in the selected BOMs. |
| [Release Change](#unique_30) [page ] 35 | BOM Engineer | Manage Change Masters (F2212) | Change master status is set to Inactive. |
| Basic Handover |  |  |  |
| [Define Effectivity of the BOM Changes](#unique_31) [page ] 36 | Production Engineer - Discrete Manufacturing | Manage Change Masters (F2212) | A new change master is created. |
| [Copy Engineering BOM to Manufacturing BOM](#unique_32) [page ] 37 | Production Engineer - Discrete Manufacturing | Maintain Bill Of Material - Create, change & display BOMs (F1813) | MBOM is created. |
| [Adjust Manufacturing BOM for Production](#unique_33) [page ] 39 | Production Engineer - Discrete Manufacturing | Maintain Bill Of Material - Create, change & display BOMs (F1813) | MBOM is reworked. |
| [Release Change](#unique_34) [page ] 40 | Production Engineer - Discrete Manufacturing | Manage Change Masters (F2212) | Change master status is set to Inactive. |
| Perform Mass Maintenance of Bills of Material Items |  |  |  |
| [Define Effectivity of the BOM Changes](#unique_35) [page ] 41 | BOM Engineer | Manage Change Masters (F2212) | A new change master is created. |
| [Mass Maintenance of BOM Items](#unique_36) [page ] 42 | BOM Engineer | Mass Maintenance of Bill of Material Items (F6578) | Selected BOM items with a change master and provided data are maintained. |
| [Simulate Mass Change of BOM Items](#unique_37) [page ] 44 | BOM Engineer | Mass Maintenance of Bill of Material Items (F6578) | Changes to the BOM items are successfully simulated. |
| [Execute Mass Change of BOM Items](#unique_38) [page ] 45 | BOM Engineer | Mass Maintenance of Bill of Material Items (F6578) | Changes to the BOM items are successfully executed. |
| [Release Change](#unique_39) [page ] 46 | BOM Engineer | Mass Maintenance of Bill of Material Items (F6578) | Change master is released. |
| Perform Mass Addition of Bills of Material Items |  |  |  |
| [Define Effectivity of the BOM Changes](#unique_40) [page ] 47 | BOM Engineer | Manage Change Masters (F2212) | A new change master is created. |
| [Mass Addition of BOM Items](#unique_41) [page ] 48 | BOM Engineer | Mass Addition of Bill of Material Items (F6862) | Selected BOM headers with a change master and provided BOM item data are maintained. |
| [Simulate Mass Addition of BOM Items](#unique_42) [page ] 49 | BOM Engineer | Mass Addition of Bill of Material Items (F6862) | Addition of BOM items is successfully simulated. |
| [Execute Mass Addition of BOM Items](#unique_43) [page ] 50 | BOM Engineer | Mass Addition of Bill of Material Items (F6862) | Addition of BOM items to the BOM headers is successfully completed. |
| [Release Change](#unique_44) [page ] 51 | BOM Engineer | Mass Addition of Bill of Material Items (F6862) | Change master is released. |
| Perform Mass Maintenance of BOM Headers |  |  |  |
| [Define Effectivity of the BOM Changes](#unique_45) [page ] 52 | BOM Engineer | Manage Change Masters (F2212) | A new change master is created. |
| [Mass Maintenance of BOM Headers](#unique_46) [page ] 53 | BOM Engineer | Mass Maintenance of Bills of Material Headers (F6863) | Selected BOM headers with a change master and provided data are maintained. |
| [Simulate Mass Change of BOM Headers](#unique_47) [page ] 55 | BOM Engineer | Mass Maintenance of Bills of Material Headers (F6863) | Changes to the BOM headers are successfully simulated. |
| [Execute Mass Change of BOM Headers](#unique_48) [page ] 56 | BOM Engineer | Mass Maintenance of Bills of Material Headers (F6863) | Changes to the BOM headers are successfully executed. |
| [Release Change](#unique_49) [page ] 57 | BOM Engineer | Mass Maintenance of Bills of Material Headers (F6863) | Change master is released. |

## Test Procedures

### Create and Change Bill of Material

#### Create Bill of Material

##### Define Effectivity of the BOM Changes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Execute the following process steps to create change master that will be used for the Create Bill of Material Items in the next steps.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as BOM Engineer. |  |  |
| 2 | Access the Fiori App | Open the Manage Change Masters (F2212) app.On the Manage Change Masters screen, choose Create. | The Create Change Master: Initial Screen is displayed. |  |
| 3 | Maintain Change Number | On the Create Change Master: Initial Screen screen, enter data as provided in the following example and press Enter.Example Change Number: CN001In the other fields, leave the default values. |  |  |
| 4 | Maintain Change Master Data | On the Create Change Master: Change Header screen, enter data as provided in the following example and press Enter:Field beside Change Number: Change Master for BOM FG126.Valid From: TodayChange no. status: 01 Active |  |  |
| 5 | Add object types to change master | On the Create Change Master: Object Types screen, Object Types table, Bill of Material row, select the following checkboxes:Actv.ObjectMgtRec |  |  |
| 6 | Save Change Master | Choose Save. | The change master is created. |  |

##### Create Bill of Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a new Bill of Material controlled using the change master.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as BOM Engineer | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the Fiori App | Open the Maintain Bill of Material - Create, change & display BOMs (Version 2) (F1813A) app . |  |  |
| 3 | Create BOM | On the Maintain Bill of Material screen, choose Create BOM. | The Create BOM dialog box is displayed. |  |
| 4 | Maintain BOM Header data | Enter data similar to the following example and choose Create BOM:Example Material: FG126Change Number: CN001BOM usage: 2 (Engineering/Design)Valid From: Today | The Maintain Bill of Material screen is displayed and by default, the Components tab is open. |  |
| 5 | Maintain BOM Component Data | In the BOM Item Number 0010 line, make entries similar to the following example:Example Component: SG21Component quantity: 1 PC(Press Enter to enable Component and Component Quantity fields.)The Item Category value is L (Stock Item), by default. | BOM Item Number 0010, Component, Component Description, and Component quantity are displayed in the first table row. |  |
| 6 | Maintain Additional BOM Components data | Repeat the above step for BOM Item Numbers 0020 to 0090 with the following entries:ComponentComponent quantity in PCSG221RM1221RM1281RM1201SG231SG251SG1241RM201 | BOM Item Number 0010 to 0090, Component, Component Description, and Component quantity are displayed in the table rows. |  |
| 7 | Navigate to Item Detail | In the BOM Item Number 0100 row, click the details arrow on the extreme right side of the table.On the Maintain Bill of Material screen, make entries similar to the following example under the Basic Details tab:Example Item Category: Preliminary ItemComponent quantity: 1Component UoM: EAChoose Apply. |  |  |
| 8 | Maintain BOM Item Category Text item (‘T’) | Choose + (Add) to create a new item 0110.In the BOM Item Number 0110 row, choose T(Text Item) from the Item category drop-down list. |  |  |
| 9 | Navigate to Item Detail | In the BOM Item Number 0110 row, click the details arrow on the extreme right side of the table.On the Maintain Bill of Material screen, make entries similar to the following example under the Basic Details tab:Example Component quantity: 1Component UoM: PCOn the Status/Long Text tab, make entries similar to the following example.Example Item Text: Documentation | The Maintain Bill of Material screen with the details section for the entered item is displayed. |  |
| 10 | Upload Attachment | Choose the Header Attachments tab.Choose Upload.In the Open dialog box, select the Drawing_0100.pdf file, and choose Open.Choose Apply. | A new attachment is created, and the Maintain Bill of Material screen with the BOM item table is displayed. |  |
| 11 | Save the BOM | On the Maintain Bill of Material screen, choose Create. | The Bill of Material is saved. |  |
| 12 | Retrieve document info record information | Access the same component created in step 8, BOM Item Number 0110 and choose the details arrow on the right side of the table. | The name of the attached file is displayed with additional information:Uploaded ByUploaded OnFile SizeDocument Info RecordNote down the Document Info Record information. It will be used later on in the succeeding processes.Document Info Record ID:________________________________ |  |
| 13 | Return to the BOM item table screen | On the Maintain Bill of Material screen, choose Back. | The Maintain Bill of Material screen with the BOM item table is displayed. |  |
| 14 | Save the BOM | Choose Save. | The Bill of Material is saved, the BOM status is set to 1 (Active). |  |

##### Add Preliminary BOM Components (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can add preliminary items BoM components using the change master.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the Fiori App | Open the Maintain Bill of Material - Create, change & display BOMs (Version 2) (F1813A) app. |  |  |
| 3 | Search BOM | On the Maintain Bill Of Material window, enter data similar to the following example and choose OK.Note For example take the BOM for the Material and Usage which was created in [Create Bill of Material](#unique_13) [page ] 14 .Example Material: FG126 | The Maintain Bill of Material screen displays the searched BOM. |  |
| 4 | Navigate to BOM components | Select the BOM displayed in the previous step. | The Maintain Bill of Material screen is displayed and by default, the Components tab is open. |  |
| 5 | Modify BOM components | On the Maintain Bill of Material screen, choose Edit.In case the additional Preliminary BOM Components is assigned to an existing change number, use the following process step insteadChoose Edit and select Edit with Change Number from the dropdown menu.In the Edit with Change Number pop-up window, maintain entries similar to the following example and choose Edit with Change Number:Use Existing Change Number: YesChange Number: CN001 | In the Maintain Bill of Material screen, the Components tab is editable. |  |
| 6 | Enter BOM Item Category Preliminary Item (‘P’) | Choose + (Add) to create a new item 0100.In the BOM Item Number 0100 line, choose Preliminary Item (‘P’) from the Item category drop-down list and and enter the minimum mandatory data , like Component Quantity and unit. |  |  |
| 7 | Apply changes | On the Maintain Bill of Material screen, choose Apply.Note This step is only needed in case the detailed view of the component has been opened. |  |  |
| 8 | Save BOM | On the Maintain Bill of Material screen, choose Create (in case of a newly created BOM) or Save (in case of changing an existing BOM) | The Bill of Material is saved.Note If you have added preliminary BOM component, then execute [Replace Preliminary Component with Actual Material](#unique_26) [page ] 30 before releasing the change. |  |

##### Create BOM Groupings (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is for logical grouping of BOM components.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as BOM Engineer. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the Fiori App | Open the Manage Multilevel Bill Of Material (F5238) app. |  |  |
| 3 | Search BOM | On the Manage Multilevel Bill of Material screen, enter data similar to the following example and choose OK:Example Material: FG126 | The Manage Multilevel Bill of Material screen is displayed. |  |
| 4 | Navigate to BOM components | Select the BOM displayed in the previous step. | The Manage Multilevel Bill of Material screen is displayed and by default, the Components tab is open. |  |
| 5 | Modify BOM components | On the Manage Multilevel Bill of Material screen, mark one line of component and choose Edit from the three dots at the upper right side of the table. | On the Manage Multilevel Bill of Material screen, the Components tab becomes editable. |  |
| 6 | Manage grouping | Select the BOM item which you want to group, then choose Manage Group.Example Select Raw Materials to groupMaterials: RM122, RM128, RM120, RM20, RM27 |  |  |
| 7 | Group BOM | In order to group certain BOM items, select the BOM item, choose Manage Group, and then choose Group. | The Create BOM Item Group dialog box is displayed. |  |
| 8 | Create BOM Item group | On the Create BOM Item Group dialog box, enter data similar to the following example, and choose Create.Example Group Name: Raw MaterialsGroup Description: Raw MaterialsBOM Component: Selected BOMs in previous step | A new Group is formed in the Manage Multilevel Bill of Material. |  |
| 9 | Save BOM group | On the Manage Multilevel Bill of Material screen, choose Save. | The new group is created and saved. |  |

##### Release Change

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you set the status of the change master to Inactive so that it cannot be used further to manage any other changes.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as BOM Engineer. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the Fiori App | Open the Manage Change Masters(F2212) app. | The Manage Change Masters screen is displayed. |  |
| 3 | Maintain Change Number | Enter the change number created in [Create Bill of Material](#unique_13) [page ] 14, and press Enter. Choose the listed Change Number.Example Change Number: CN001 | The Change Master screen is displayed. |  |
| 4 | Set the Change Master Status | Choose Edit.In the Change No. Status field, select 02-Inactive. | The status of the change master is set to Inactive. |  |
| 5 | Save the Change Master | Choose Save. | The change master is saved. |  |

#### Change Bill of Material

##### Major Change

Purpose

This is a positive case of Form Fit and Function Change.

In General, when the change in BOM is not small then follow these steps.

###### Define Effectivity of the BOM Changes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Creation of the change master that will be used for the Bill of Material change in the next step.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as BOM Engineer. |  |  |
| 2 | Access the Fiori App | Open the Manage Change Masters (F2212) app.On the Manage Change Masters screen, choose Create. | The Create Change Master: Initial Screen is displayed. |  |
| 3 | Maintain Change Number | On the Create Change Master: Initial Screen screen, enter data as provided in the following example and press Enter.Example Change Number: CN002In the other fields, leave the default values. |  |  |
| 4 | Maintain Change Master Data | On the Create Change Master: Change Header screen, enter data as provided in the following example and press Enter:Field beside Change Number: Change Master for BOM FG126.Valid From: TodayChange no. status: 01 Active |  |  |
| 5 | Add object types to change master | On the Create Change Master: Object Types screen, Object Types table, Bill of Material row, select the following checkboxes:Actv.ObjectMgtRec |  |  |
| 6 | Save Change Master | Choose Save. | The change master is created. |  |

###### Copy (Create) Header Material (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, new header material gets created for bill of material. However, this is optional because user can also use similar available material

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer or Master Data Specialist - Product Data. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Material (MM01)app. | The Create Material (Initial Screen) screen appears. |  |
| 3 | Copy(Create) Material | On the Create Material (Initial Screen) screen, make entries similar to the following example::Example Material : FG126_V1Industry : 1 RetailMaterial Type :Finished ProductCopy From:FG126Choose Continue. | The Select View(s) pop up screen appears. |  |
| 4 | Choose Views | Select Basic Data 1 and Basic Data 2.Choose Continue (Enter). | The Create Material FG126_V1 (Finished Product) screen appears. |  |
| 5 | Save Your Data | On the Create Material (Initial Screen) screen, do the following:Choose Save. A message confirming that the material has been created appears. | Material FG126_V1 is created. |  |

###### Copy BOM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The test step is used to create a new BOM for a new material with Change Master by coping an existing BOM.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as BOM Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori App | Open Maintain Bill Of Material - Create, change & display BOMs (Version 2) (F1813A) app. |  |  |
| 3 | Search for the BOM to be copied | Enter the following data and choose Go.Example Material: FG126BOM Usage: Engineering/Design | The BOM to be copied is listed. |  |
| 4 | Select the BOM to be copied | Select the radio button corresponding to BOM to be copied and choose Copy BOM. | The Copy BOM dialog box is displayed. |  |
| 5 | Enter Material Detail | Enter the following data, and choose Copy BOM.Example Material: FG126_V1BOM Usage: 2 (Engineering/Design)Change Number: CN002Copy Components: Yes | Maintain Bill of Material is displayed in draft Mode. |  |
| 6 | Save the BOM | On the Maintain Bill of Material screen, choose Create. | The new Bill of Material is saved. |  |

###### Change Bill Of Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Changing the Bill of Material via a Change Master.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the Fiori App | Open Maintain Bill of Material - Create, change & display BOMs (Version 2) (F1813A)app. |  |  |
| 3 | Search for the BOM to be changed | Enter the following data and choose Go:Example Material : FG126_v1BOM Usage: Engineering/Design | The draft BOM is displayed. |  |
| 4 | Select the BOM to be changed | Example See above selection. | The Maintain Bill of Material screen of the draft BOM is displayed. |  |
| 5 | Edit with Change Master | Choose Edit and select Edit with Change Number from the dropdown menu.In the Edit with Change Number pop-up window, maintain entries similar to the following example and choose Edit with Change Number:Use Existing Change Number: YesChange Number: CN002 |  |  |
| 6 | Enter a new component by choosing + (Add) in the Components tab. | On the Maintain Bill of Material screen, choose + Add. |  |  |
| 7 | Enter BOM Item Category, Component, and Component quantity | In the BOM Item Number 0110 line, make the following entries:Example Item Category:Stock ItemComponent:RM20Component quantity:5 PC |  |  |
| 8 | Save | On the Maintain Bill of Materialscreen, choose Save | The BOM is changed. |  |

###### Release Change

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you set the status of the change master to Inactive so that it cannot be used further to manage any other changes.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as BOM Engineer. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the Fiori App | Open the Manage Change Masters (F2212) app. | The Manage Change Masters screen is displayed. |  |
| 3 | Maintain Change Number | Enter the change number created for the major change of BOM, and then press Enter.Example Change Number: CN002 | The Change Master screen is displayed. |  |
| 4 | Set the Change Master Status | Choose Edit.In the Change No. Status field, select 02-Inactive. | The status of the change master is set to Inactive. |  |
| 5 | Save the Change Master | Choose Save. | The change master is saved. |  |

##### Minor Change

Purpose

This is a negative case of Form Fit and Function Change.

In General, when the change is small, follow these steps.

###### Change BOM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can change the Bill of Material using a Change Master.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the Fiori App | Open Maintain Bill of Material - Create, change & display BOMs (Version 2) (F1813A) app. |  |  |
| 3 | Search for the BOM to be changed | Material: FG126BOM Usage: Engineering/Design | The BOM to be changed is listed. |  |
| 4 | Click the BOM to be changed | Select the correct BOM to be changed. | The BOM to be changed is displayed |  |
| 5 | Choose Display Timeline Button and select the change number | Choose DiplayTimelineBtn button (next to Selected Change Number fieldIf an inactive (status 2) change number is selected (marked bold in header) then change Selected Date to any new date on the Maintain Bill of Material screen and choose OK. | Selected Date is active and Date is changed |  |
| 6 | Edit the Bill of Materials | Choose Edit (If Edit button is not appearing on the screen, select More (depicted by three dots) and choose Edit) |  |  |
| 7 | Create Change Master | Choose Edit with Change Number from the dropdown menu. | The Edit with Change Number pop-up window appears. |  |
| 8 | Maintain Change Master data | In the Edit with Change Number pop-up window, maintain entries similar to the following example and choose Edit with Change Number:Use Existing Change Number: NoChange Number: CN003Example Start Date: Today + 1 weekDescription:Change number for changes to FG126 BOM | Change Master is created. |  |
| 9 | Enter BOM Item Category, Component, and Component quantity | On the Maintain Bill of Material screen, Choose + (Add Single row) and in the Components tab, make entries similar to the following example:Example Item Category: Stock ItemComponent: RM27Component quantity: 1 PC |  |  |
| 10 | Check the validity date for the new component | Note the date in the Valid From column for the above component and the assigned Change Number date in the timeline. |  |  |
| 12 | Choose Save | On the Maintain Bill of Material screen, choose Save. | The BOM is changed. |  |
| 13 | Select a Change Number | Choose DiplayTimelineBtn button (next to the Selected Change Number field), select one of the available change numbers, and check the corresponding component configuration of the BOM.Example Change Number:CN003 | The newly added component will only be displayed when the relevant Change Number is selected. |  |

###### Release Change

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you set the status of the change master to Inactive so that it cannot be used further to manage any other changes.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as BOM Engineer. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the Fiori App | Open the Manage Change Masters (F2212) app. | The Manage Change Masters screen is displayed. |  |
| 3 | Maintain Change Number | Enter the change number created for the minor change of BOM in the Change BOM step, and then press Enter. Select the listed Change Number.Example Change Number: CN003 | The Change Master screen is displayed. |  |
| 4 | Set the Change Master Status | Choose Edit.In the Change No. Status field, select 02-Inactive. | The status of the change master is set to Inactive. |  |
| 5 | Save the Change Master | Choose Save. | The change master is saved. |  |

#### Replace Preliminary Items (Optional)

##### Replace Preliminary Component with Actual Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can replace the preliminary items with actual material.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as BOM Engineer |  |  |
| 2 | Access the Fiori App | Open the Maintain Bill of Material - Create, change & display BOMs (Version 2) (F1813A) app. |  |  |
| 3 | Search for the BOM to be changed | Make the following entries:Material: FG126BOM Usage: Engineering/Design | The BOM to be changed is listed. |  |
| 4 | Click the BOM to be changed | Select the correct BOM to be changed. | The BOM to be changed is displayed |  |
| 5 | Choose Display Timeline Button and select the change number | Choose the DiplayTimelineBtn button (next to Selected Change Number field.If an inactive (status 2) change number is selected (marked bold in header) then change Selected Date to any new date on the Maintain Bill of Material screen. | The Selected Date is active and the date is changed |  |
| 6 | Edit the Bill of Materials | Choose Edit (If Edit button is not appearing on the screen, select More (depicted by three dots) and choose Edit). |  |  |
| 7 | Create Change Master | Choose Edit with Change Number from the dropdown menu. | The Edit with Change Number pop-up window appears. |  |
| 8 | Maintain Change Master Data | In the Edit with Change Number pop-up window, maintain entries similar to the following example and choose Edit with Change Number:Example Use Existing Change Number: NoChange Number: CN002Start Date: Today + 1 weekDescription: Change number to Replace Preliminary Items for BOM FG126 | The Change Master is created. |  |
| 9 | Replace Preliminary Item with Actual Material | On the Maintain Bill of Material screen, Choose BOM item Number 100 and choose Convert Item Category.On the Convert Item Category pop-up, maintain entries similar to following example and choose Convert.Example Component: RM27Item Category: L(Stock Item)Note For item category, choose the related item which have been set up with item category P (Preliminary) | The component is available for the preliminary item. |  |
| 10 | Save | Choose Save. | The BOM is changed. |  |

#### Where-used and Mass Replacement

##### Define Effectivity of the BOM Changes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Creation of the change master that will be used for the Bill of Material changes in the next step.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as BOM Engineer. |  |  |
| 2 | Access the Fiori App | Open the Manage Change Masters (F2212) app.On the Manage Change Masters screen, choose Create. | The Create Change Master: Initial Screen is displayed. |  |
| 3 | Maintain Change Number | On the Create Change Master: Initial Screen screen, enter data as provided in the following example and press Enter.Example Change Number: CN004In the other fields, leave the default values. |  |  |
| 4 | Maintain Change Master Data | On the Create Change Master: Change Header screen, enter data as provided in the following example and press Enter:Field beside Change Number: Change Master for BOM FG126.Valid From: TodayChange no. status: 01 Active |  |  |
| 5 | Add object types to change master | On the Create Change Master: Object Types screen, Object Types table, Bill of Material row, select the following checkboxes:Actv.ObjectMgtRec |  |  |
| 6 | Save Change Master | Choose Save. | The change master is created. |  |

##### Execute Where-Used for Component to Replace

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you check the where-used information of a material across multiple BOMs.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as BOM Engineer. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the app | Open the Material where used list in BOMs - where used list, hierarchy and replace Materials in BOMs (F2214) app. | The Material Where-Used screen is displayed. |  |
| 3 | Search a material | Make entries similar to the following example, and choose Go.ExampleComponent: RM27BOM Usage: Engineering/Design | All bill of materials that use the searched material as a component are listed in the search results.Note To customize the view settings of the search results, choose the Settings icon displayed on the top-right of the list. On the View Settings dialog box, make the desired settings, and choose OK. |  |
| 4 | View hierarchy | Select the BOM which you want to view and choose View Hierarchy. | The hierarchical view of the bill of materials displays. You can select a node and then:Choose the Expand/Collapse icon in the hierarchical view to collapse or expand the node.Choose the Node Details icon to view the details of the node. |  |

##### Replace Material for the Selected BOMs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you change multiple BOMs to replace a component material with another material.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as BOM Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the Material where used list in BOMs - where used list, hierarchy and replace Materials in BOMs (F2214) app. | The Material Where-Used screen displays. |  |
| 3 | Search a material | Make entries similar to the following example, and choose Go.ExampleComponent: RM27BOM Usage: Engineering/Design | The list of bill of materials that use the searched material as a component displays.Note To customize the view settings, choose the Settings icon displayed on the top right corner of the list. On the View Settings dialog box, customize the settings, and choose OK. |  |
| 4 | Replace the material with another material | In the list, select the bill of materials for which you want to replace the component material. For example, FG29 and SG224.Choose Replace Material.In the Replace Material dialog box, make the entries similar to the following example, and choose OK.ExampleReplacement Material: RM20Quantity and Unit of Measure 100 PCChange Number: CN004Tip Use the change number created in [Define Effectivity of the BOM Changes](#unique_27) [page ] 32. | For the selected bill of materials, the Change Status changes to Replaced and the Item Change Number column displays the specified change number (for example, CN004). |  |
| 5 | Confirm the material replacement | Select the bill of materials with the change status Replaced. For example, FG29 and SG224.Choose Confirm Replacement Material. | The material is replaced and a confirmation message is displayed. |  |

##### Release Change

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you set the status of the change master to Inactive so that it cannot be used further to manage any other changes.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as BOM Engineer. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the Fiori App | Open the Manage Change Masters (F2212) app. | The Manage Change Masters screen is displayed. |  |
| 3 | Maintain Change Number | Enter the change number created for the major change of BOM, and then press Enter.Example Change Number: CN004 | The Change Master screen is displayed. |  |
| 4 | Set the Change Master Status | Choose Edit.In the Change No. Status field, select 02-Inactive. | The status of the change master is set to Inactive. |  |
| 5 | Save the Change Master | Choose Save. | The change master is saved. |  |

### Basic Handover

#### Define Effectivity of the BOM Changes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create the change master that is used to create the manufacturing BOM.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Production Engineer - Discrete Manufacturing. |  |  |
| 2 | Access the Fiori App | Open the Manage Change Masters (F2212) app.On the Manage Change Masters screen, choose Create. | The Create Change Master: Initial Screen is displayed. |  |
| 3 | Maintain Change Number | On the Create Change Master: Initial Screen screen, enter data as provided in the following example and press Enter.Example Change Number: CN005In the other fields, leave the default values. |  |  |
| 4 | Maintain Change Master Data | On the Create Change Master: Change Header screen, enter data as provided in the following example and press Enter:Field beside Change Number: Change Master for BOM FG126.Valid From: TodayChange no. status: 01 Active |  |  |
| 5 | Add object types to change master | On the Create Change Master: Object Types screen, Object Types table, Bill of Material row, select the following checkboxes:Actv.ObjectMgtRec |  |  |
| 6 | Save Change Master | Choose Save. | The change master is created. |  |

#### Copy Engineering BOM to Manufacturing BOM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process, you create a new manufacturing bill of material (MBOM) as a copy of an engineering bill of material (EBOM).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the app | Open the Maintain Bill of Material - Create, change & display BOMs (Version 2) (F1813A) app. | The Maintain Bill of Material screen is displayed. |  |
| 3 | Find the EBOM | Make the following entries, and choose Go:Material: FG126BOM Usage: Engineering/Design | The EBOM is displayed in the search results. |  |
| 4 | Hand over the EBOM to manufacturing | Select the BOM FG126, and then choose Copy BOM.Choose radio button from current app.On the Copy BOM dialog box, make the following entries:Material: FG126BOM Usage: 1Plant: 3310Change Number: CN005Select the Copy Components check box. (Selected by default)Choose Copy BOM. | The EBOM is copied over to a new MBOM, which displays in the draft mode. |  |
| 5 | Save the MBOM | Choose Create. | The MBOM is created. |  |

#### Adjust Manufacturing BOM for Production

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you add a new component to the BOM and release it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Production Engineer - Discrete Manufacturing.Note If you are already logged on and the BOM details are already displayed, then skip to test step 5. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the app | Open the Maintain Bill of Material - Create, change & display BOMs (Version 2) (F1813A) app. | The Maintain Bill of Material screen is displayed. |  |
| 3 | Find BOM | Make the following entries and choose Go:Material: FG126Plant: 3310BOM Usage: Production | BOM is displayed in the result list. |  |
| 4 | Open BOM | Select the BOM in the result list. | The BOM details are displayed. |  |
| 5 | Edit BOM | Choose Edit.Tip If the Edit button is not visible, then choose More options and then choose Edit. | BOM can be edited now. |  |
| 6 | Enter BOM Item Category, Component, and Component quantity | Make the following entries in the top row:Item Category: Stock item (default)Component: RM129Component quantity: 2 PCNote In case the listed top row should not be replaced, a new component can be added::Choose Edit with Change Number from the dropdown menu instead of EditOn the Maintain Bill of Material screen, Choose + (Add Single row) and in the Components tab, make entries similar to the following example:Item Category: Stock item (default)Component: RM129Component quantity: 2 PC | BOM Item Number, Component, Component Description, and Component quantity are displayed in the top row in the table. |  |
| 7 | Save BOM | In the Maintain Bill of Materia screen, choose Save. | The BOM is saved and a confirmation message is displayed. |  |

#### Release Change

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you set the status of the change master to Inactive so that it cannot be used further to manage any other changes.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the Fiori App | Open the Manage Change Masters (F2212) app. | The Manage Change Masters screen is displayed. |  |
| 3 | Maintain Change Number | Enter the change number created for the major change of BOM, and then press Enter.Example Change Number: CN005 | The Change Master screen is displayed. |  |
| 4 | Set the Change Master Status | Choose Edit.In the Change No. Status field, select 02-Inactive. | The status of the change master is set to Inactive. |  |
| 5 | Save the Change Master | Choose Save. | The change master is saved. |  |

### Mass Maintenance of Bill of Material

#### Perform Mass Maintenance of Bill of Material Items

##### Define Effectivity of the BOM Changes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Creation of the change master that will be used for the Mass Maintenance of Bills of Material Items in the next step.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as BOM Engineer. |  |  |
| 2 | Access the Fiori App | Open the Manage Change Masters (F2212) app.On the Manage Change Masters screen, choose Create. | The Create Change Master: Initial Screen is displayed. |  |
| 3 | Maintain Change Number | On the Create Change Master: Initial Screen screen, enter data as provided in the following example and press Enter.Example Change Number: CN006In the other fields, leave the default values. |  |  |
| 4 | Maintain Change Master Data | On the Create Change Master: Change Header screen, enter data as provided in the following example and press Enter:Field beside Change Number: Change Master for BOM FG126.Valid From: TodayChange no. status: 01 Active |  |  |
| 5 | Add object types to change master | On the Create Change Master: Object Types screen, Object Types table, Bill of Material row, select the following checkboxes:Actv.ObjectMgtRec |  |  |
| 6 | Save Change Master | Choose Save. | The change master is created. |  |

##### Mass Maintenance of BOM Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can maintain the data to change or delete multiple BOM Items.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as BOM Engineer. |  |  |
| 2 | Access App | Open the Mass Maintenance of Bill of Material Items (F6578) app. | The Mass Maintenance of Bills of Material Items screen is displayed. |  |
| 3 | Set filter for the BOM Item | On the Mass Maintenance of Bills of Material Items screen, maintain search criteria for the Bill of Material for which you want to make the changes and choose Go.Example Component: SG21Plant: 3310 | A list of relevant BOMs is displayed. |  |
| 4 | Start Selection for BOM Items to edit or delete. | On the Mass Maintenance of Bills of Material Items screen, from the list, select (using the checkbox on the left column) BOM Items to edit or delete. | The corresponding BOM components are selected and highlighted. |  |
| 5 | Maintain BOM Items | If you want to mass edit the selected BOM items:Choose Maintain Selected BOMs or Maintain All BOMs, and then choose Edit.In the Edit BOM Items dialog box, enter data as provided in the following example.Example Change Number: CN006Select Mode of Processing: Run Job in BackgroundJob Description: Edit BOM Items JobIn Select Attributes to Edit, choose Spare Part Indicator, and set the value as X.If you want to mass delete the selected BOM items:Choose Maintain Selected BOMs, and then choose Delete.In the Delete BOM Items dialog box, enter data as provided in the following example.Example Change Number: CN006Select Mode of Processing: Run Job in BackgroundJob Description: Delete BOM Items JobNote If the BOM is created with the change number then it can only be deleted with change number and if the BOM is not created with the change number then you don't have to enter any change number for deletion. | If Edit selected then Edit BOM Items pop-up window appears with all the data you have maintained as provided in the example.If Delete selected then Delete BOM Items pop-up window appears with all you have maintained as provided in the example. |  |
| 6 | Simulate Mass change of BOM Items | For instructions to apply the changes to the BOM items, see [Simulate Mass Change of BOM Items](#unique_37) [page ] 44. |  |  |

##### Simulate Mass Change of BOM Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can simulate the changes made to the BOM items in the [previous step](#unique_36).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Simulate Mass change of BOM Items | In the [previous step](#unique_36), you have maintained the BOM items as per the example. Choose Simulate to start the simulation process. | A dialog box Success appears with a message that job has been scheduled. |  |
| 2 | Check Simulation Protocol | On the Success dialog box, choose View Job Details.On the Monitor Mass Maintenance of Bills of Material screen, select the row with the scheduled job once the Processing Status of the job is Finished. | The BOM Mass Maintenance Log screen is displayed with simulation results as Processing status: Success Processing Description: BOM Item operation successfully executedIf the Processing status is Success, then continue with the [next step](#unique_38), else choose Re-Simulate. |  |
| 3 | Execute Mass change of BOM items | For instructions to apply the changes to the BOM items, see [Execute Mass Change of BOM Items](#unique_38) [page ] 45. |  |  |

##### Execute Mass Change of BOM Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can save the changes made to the BOM items in the [previous step](#unique_37).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Execute Mass Change of BOM Items | In the [previous step](#unique_37), simulation of mass change of BOM items is successful.On the BOM Mass Maintenance Log screen, choose Execute at the bottom-right corner to apply the BOM Items change.On the Re-Execute BOM Items dialog box, choose Run Job in background, provide Job Description, and then choose Execute. | A dialog box Success appears with a message that job has been scheduled. |  |
| 2 | Check Execution Protocol | On the Success dialog box, choose View Job Details.Select the row with the scheduled job in Monitor Mass Maintenance of Bills of Material screen once the Processing Status of the job is Finished. | The BOM Mass Maintenance Log screen is displayed with execution results as Processing status: Success Processing Description: BOM Item operation successfully executed.If the Processing status is Failed, then choose Re-Execute. |  |

##### Release Change

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you set the status of the change master to Inactive so that it cannot be used further to manage any other changes.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as BOM Engineer. |  |  |
| 2 | Access the Fiori App | Open the Manage Change Masters(F2212) app. | The Manage Change Masters screen is displayed. |  |
| 3 | Maintain Change Number | Enter the change number created for the mass maintenance of BOM items, and press Enter.Example Change Number: CN006 | The Change Master screen is displayed. |  |
| 4 | Set the Change Master Status | Choose Edit.In the Change No. Status field, select 02-Inactive. | The status of the change master is set to Inactive. |  |
| 5 | Save the Change Master | Choose Save. | The change master is saved. |  |

#### Perform Mass Addition of Bill of Material Items

##### Define Effectivity of the BOM Changes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Creation of the change master that will be used for the Mass Maintenance of Bills of Material Items in the next step.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as BOM Engineer. |  |  |
| 2 | Access the Fiori App | Open the Manage Change Masters (F2212) app.On the Manage Change Masters screen, choose Create. | The Create Change Master: Initial Screen is displayed. |  |
| 3 | Maintain Change Number | On the Create Change Master: Initial Screen screen, enter data as provided in the following example and press Enter.Example Change Number: CN007In the other fields, leave the default values. |  |  |
| 4 | Maintain Change Master Data | On the Create Change Master: Change Header screen, enter data as provided in the following example and press Enter:Field beside Change Number: Change Master for BOM FG126.Valid From: TodayChange no. status: 01 Active |  |  |
| 5 | Add object types to change master | On the Create Change Master: Object Types screen, Object Types table, Bill of Material row, select the following checkboxes:Actv.ObjectMgtRec |  |  |
| 6 | Save Change Master | Choose Save. | The change master is created. |  |

##### Mass Addition of BOM Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can maintain the data to add BOM Item to BOM Headers.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as BOM Engineer. |  |  |
| 2 | Access App | Open the Mass Addition of Bill of Material Items (F6862) app. | The Mass Addition of Bills of Material Itemsscreen is displayed. |  |
| 3 | Set filter for the BOM Header | On the Mass Addition of Bills of Material Item screen, maintain search criteria for the Bill of Material for which you want to make the changes, and choose Go.Example Material: FG126Plant: 3310 | A list of relevant BOMs is displayed. |  |
| 4 | Start Selection of BOM Headers to Add BOM Items | On the Mass Addition of Bills of Material Item screen, from the list, select (using the checkbox on the left column) BOM components to add. | The corresponding BOM headers are selected and highlighted. |  |
| 5 | Addition of BOM Item to BOM Headers | On the Mass Addition of Bills of Material Item screen, choose Add Item to Selected BOM Headers or Add Item to All BOM Headers. | The Add BOM Item dialog box is displayed. |  |
| 6 | Maintain data to add item to BOM Headers | On the Add BOM Item dialog box, enter data as in the following example.Example Change Number: CN007Item Category: Stock Item(L)Component: SG21Component Quantity: 01Component UoM: PCSelect Mode of Processing: Run Job in BackgroundJob Description: Mass Addition Job |  |  |
| 7 | Simulate BOM Addition | For instructions to simulate the changes, see [Simulate Mass Addition of BOM Items](#unique_42) [page ] 49. |  |  |

##### Simulate Mass Addition of BOM Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can simulate the addition of a BOM item to BOM headers.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Simulate BOM item Addition to BOM Headers | In the [previous step](#unique_41), you have maintained the BOM items as per the example. Choose Simulate to start the simulation process. | A dialog box Success appears with a message that job has been scheduled. |  |
| 2 | Check Simulation Protocol | On the Success dialog box, choose View Job Details.On the Monitor Mass Maintenance of Bills of Material screen, select the row with the scheduled job once the Processing Status of the job is Finished. | The BOM Mass Maintenance Log screen is displayed with simulation results asProcessing status: SuccessProcessing Description: BOM Itemoperation successfully executedIf the Processing status is Success, then continue with the [next step](#unique_43), else choose Re-Simulate. |  |
| 3 | Execute Mass Addition of BOM Items | For instructions to execute the mass addition of BOM items, see [Execute Mass Addition of BOM Items](#unique_43) [page ] 50. |  |  |

##### Execute Mass Addition of BOM Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can save the changes made in the [previous step](#unique_42).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Execute Mass Addition of BOM Items | In the [previous step](#unique_42), simulation of mass addition of BOM items is successful.On the BOM Mass Maintenance Log screen, choose Execute at the bottom-right corner save the added BOM items to the selected BOM headers.On the Re-Execute BOM Items dialog box, choose Run Job in background, provide Job Description, and then choose Execute. | A dialog box Success appears with a message that job has been scheduled. |  |
| 2 | Check Execution Protocol | On the Success dialog box, choose View Job Details.Select the row with the scheduled job in Monitor Mass Maintenance of Bills of Material screen once the Processing Status of the job is Finished. | The BOM Mass Maintenance Log screen is displayed with execution results asProcessing status: SuccessProcessing Description: BOM Header operation successfully executed.If the Processing status is Failed, then choose Re-Execute. |  |

##### Release Change

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you set the status of the change master to Inactive so that it cannot be used further to manage any other changes.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as BOM Engineer. |  |  |
| 2 | Access the Fiori App | Open the Manage Change Masters(F2212) app. | The Manage Change Masters screen is displayed. |  |
| 3 | Maintain Change Number | Enter the change number created for the mass addition of BOM items, and press Enter.Example Change Number: CN007 | The Change Master screen is displayed. |  |
| 4 | Set the Change Master Status | Choose Edit.In the Change No. Status field, select 02-Inactive. | The status of the change master is set to Inactive. |  |
| 5 | Save the Change Master | Choose Save. | The change master is saved. |  |

#### Perform Mass Maintenance of Bill of Material Headers

##### Define Effectivity of the BOM Changes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Creation of the change master that will be used for the Mass Maintenance of Bills of Material Items in the next step.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as BOM Engineer. |  |  |
| 2 | Access the Fiori App | Open the Manage Change Masters (F2212) app.On the Manage Change Masters screen, choose Create. | The Create Change Master: Initial Screen is displayed. |  |
| 3 | Maintain Change Number | On the Create Change Master: Initial Screen screen, enter data as provided in the following example and press Enter.Example Change Number: CN008In the other fields, leave the default values. |  |  |
| 4 | Maintain Change Master Data | On the Create Change Master: Change Header screen, enter data as provided in the following example and press Enter:Field beside Change Number: Change Master for BOM FG126.Valid From: TodayChange no. status: 01 Active |  |  |
| 5 | Add object types to change master | On the Create Change Master: Object Types screen, Object Types table, Bill of Material row, select the following checkboxes:Actv.ObjectMgtRec |  |  |
| 6 | Save Change Master | Choose Save. | The change master is created. |  |

##### Mass Maintenance of BOM Headers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you maintain the data to change or delete multiple BOM Headers.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as BOM Engineer. |  |  |
| 2 | Access App | Open the Mass Maintenance of Bills of Material Headers (F6863) app. | The Mass Maintenance of Bills of Material Headers screen is displayed. |  |
| 3 | Set filter for BOM Header | On the Mass Maintenance of Bills of Material Headers screen, maintain search criteria for the Bill of Material for which you want to make the changes and choose Go.Example Material: FG126Plant: 3310 | A list of relevant BOMs is displayed. |  |
| 4 | Start Selection for BOM Headers to edit or delete. | On the Mass Maintenance of Bills of Material Headers screen, from the list, select (using the checkbox on the left column) BOM Headers to edit or delete. | The corresponding BOM headers are selected and highlighted. |  |
| 5 | Maintain BOM Headers | If you want to edit the selected BOM headers en masse:Choose Maintain Selected BOMs or Maintain All BOMs, and then choose Edit.In the Edit BOM Headers dialog box, enter data as provided in the following example.Example Change Number: CN008Select Mode of Processing: Run Job in BackgroundJob Description: Edit BOM Headers JobIn Select Attributes to Edit, choose Base Quantity, and set the value as 01.If you want to delete the selected BOM headers::Choose Maintain Selected BOMs, and then choose Delete.In the Delete BOM Items dialog box, enter data as provided in the following example.Example Change Number: CN008Select Mode of Processing: Run Job in BackgroundJob Description: Delete BOM Headers JobNote If the BOM is created with the change number then it can only be deleted with change number and if the BOM is not created with the change number then you don't have to enter the change number for deletion | If you selected Edit, then the Edit BOM Headers dialog box is displayed with the data that you entered as in the example.If you selected Delete, then the Delete BOM Headers dialog box is displayed with the data that you entered as in the example. |  |
| 6 | Simulate Mass change of BOM Headers | For instructions to apply the changes to the BOM headers, see [Simulate Mass Change of BOM Headers](#unique_47) [page ] 55. |  |  |

##### Simulate Mass Change of BOM Headers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can simulate the changes made to the BOM headers in the [previous step](#unique_46).

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Simulate Mass Change of BOM Headers | In the [previous step](#unique_46), you have maintained the BOM headers as per the example. Choose Simulate to start the simulation process. | A dialog box Success appears with a message that job has been scheduled. |  |
| 2 | Check Simulation Protocol | On the Success dialog box, choose View Job Details.On the Monitor Mass Maintenance of Bills of Material screen, select the row with the scheduled job once the Processing Status of the job is Finished. | The BOM Mass Maintenance Log screen is displayed with simulation results asProcessing status: SuccessProcessing Description: BOM Header operation successfully executedIf the Processing status is Success, then continue with the [next step](#unique_48), else choose Re-Simulate. |  |
| 3 | Execute Mass Addition of BOM Items | For instructions to apply the changes to the BOM headers, see [Execute Mass Change of BOM Headers](#unique_48) [page ] 56. |  |  |

##### Execute Mass Change of BOM Headers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can save the changes made to the BOM headers in the [previous step](#unique_47).

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Execute Mass Change of BOM Headers | In the [previous step](#unique_47), simulation of mass change of BOM headers is successful.On the BOM Mass Maintenance Log screen, choose Execute at the bottom-right corner to apply the BOM headers change.On the Re-Execute BOM Items dialog box, choose Run Job in background, provide Job Description, and then choose Execute. | A dialog box Success appears with a message that job has been scheduled. |  |
| 2 | Check Execution Protocol | On the Success dialog box, choose View Job Details.Select the row with the scheduled job in Monitor Mass Maintenance of Bills of Material screen once the Processing Status of the job is Finished. | The BOM Mass Maintenance Log screen is displayed with execution results asProcessing status: SuccessProcessing Description: BOM Item operation successfully executed.If the Processing status is Failed, then choose Re-Execute. |  |

##### Release Change

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you set the status of the change master to Inactive so that it cannot be used further to manage any other changes.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as BOM Engineer. |  |  |
| 2 | Access the Fiori App | Open the Manage Change Masters(F2212) app. | The Manage Change Masters screen is displayed. |  |
| 3 | Maintain Change Number | Enter the change number created for the mass maintenance of BOM headers, and press Enter.Example Change Number: CN008 | The Change Master screen is displayed. |  |
| 4 | Set the Change Master Status | Choose Edit.In the Change No. Status field, select 02-Inactive. | The status of the change master is set to Inactive. |  |
| 5 | Save the Change Master | Choose Save. | The change master is saved. |  |

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
> Flagged while digesting this document, not verified: Internal: the Overview Table lists the Release Change steps of the three mass-maintenance sections under apps F6578/F6862/F6863 (expected result 'Change master is released'), while the detailed procedures release the change master in Manage Change Masters (F2212).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/bom-mds-bnk-625]]
- related-to :: [[12-production-and-manufacturing/crear-lista-de-materiales-para-material-para-produccion-y-ventas-mds-b]]
- related-to :: [[12-production-and-manufacturing/create-material-bom-for-production-and-sales-mds-bnk-623]]
- related-to :: [[12-production-and-manufacturing/mds-bnk-627]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/64F_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 91,371 chars in the whole document
