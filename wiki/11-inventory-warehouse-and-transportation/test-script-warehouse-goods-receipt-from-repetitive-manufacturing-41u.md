---
id: 11-inventory-warehouse-and-transportation/test-script-warehouse-goods-receipt-from-repetitive-manufacturing-41u
title: "Test Script: Warehouse Goods Receipt from Repetitive Manufacturing (41U_AE) (41U_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 41U: goods receipt of repetitive manufacturing output into the warehouse, with putaway variants."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-production-integration]
aliases: [41U_S4CLD2608_BPD_EN_AE]
keywords: [EWM Production Supply and Receipt, warehouse goods receipt, repetitive manufacturing, warehouse task creation, manual warehouse tasks, putaway confirmation, radio frequency devices, business roles, production version, warehouse product attributes]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/41U_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-994
topic: 11-inventory-warehouse-and-transportation/ewm-production-integration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Warehouse Goods Receipt from Repetitive Manufacturing (41U_AE) (41U_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/41U_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **EWM Production Supply and Receipt** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Warehouse Goods Receipt from Repetitive Manufacturing (41U_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232854334)

[2 Prerequisites 4](#_Toc232854335)

[2.1 System Access 4](#_Toc232854336)

[2.2 Roles 4](#_Toc232854337)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232854338)

[2.4 Business Conditions 6](#_Toc232854339)

[2.5 Preliminary Steps 7](#_Toc232854340)

[2.5.1 Maintain Production Version 7](#_Toc232854341)

[2.5.2 Maintain Warehouse Product Attributes 9](#_Toc232854342)

[2.5.3 Define Default Values for Warehouse Clerk (EWM) 10](#_Toc232854343)

[2.5.4 Define Default Values for Warehouse Operative (EWM) 10](#_Toc232854344)

[3 Overview Table 12](#_Toc232854345)

[4 Test Procedures 13](#_Toc232854346)

[4.1 Check Material Document (Optional) 13](#_Toc232854347)

[4.2 Check Goods Movement Document (Optional) 14](#_Toc232854348)

[4.3 Variant 1: Automatic Warehouse Task Creation 15](#_Toc232854349)

[4.3.1 Check Warehouse Task (Optional) 15](#_Toc232854350)

[4.4 Variant 2: Manual Warehouse Task Creation 16](#_Toc232854351)

[4.4.1 Pack Finished Material (Optional) 16](#_Toc232854352)

[4.4.2 Create HU Warehouse Task (Optional) 16](#_Toc232854353)

[4.4.3 Create Product Warehouse Task 17](#_Toc232854354)

[4.5 Confirm Putaway Warehouse Tasks 17](#_Toc232854355)

[4.5.1 Variant 1: With Fiori App 17](#_Toc232854356)

[4.5.2 Variant 2: With Radio Frequency Devices 18](#_Toc232854357)

[5 Appendix 21](#_Toc232854358)

[5.1 Process Integration 21](#_Toc232854359)

[5.1.1 Succeeding Processes 21](#_Toc232854360)

## Purpose

Overview

This scope item allows you to perform the goods receipt of finished material from repetitive manufacturing into the warehouse. With the repetitive manufacturing confirmation, finished material is received into the specified warehouse goods receipt bin and raw material is issued from stock. The goods receipt (movement type 131) and the goods issue (movement type 261) are posted synchronously in one material document. A new warehouse product attribute/indicator allows you to specify for each product whether to create warehouse tasks from the goods receipt bin to the final storage bin automatically during goods receipt posting or manually after goods receipt posting. In the case of a manual warehouse task creation, you can pack the material into a handling unit as required. You then create warehouse tasks manually to move the material/handling unit from the production goods receipt area to the final storage bin.

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Production Engineer - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC | Production Engineering - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |  |
| Production Supervisor - Repetitive Manufacturing | SAP_BR_PRODN_SUPERVISOR_RPTV | Production Management - Repetitive Manufacturing | SAP_BR_PRODN_SUPERVISOR_RPTV |  |
| Production Operator - Repetitive Manufacturing | SAP_BR_PRODN_OPTR_RPTV | Production Execution - Repetitive Manufacturing | SAP_BR_PRODN_OPTR_RPTV |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Warehouse Clerk (EWM) | SAP_BR_WAREHOUSE_CLERK_EWM | Warehouse Office | SAP_BR_WAREHOUSE_CLERK_EWM |  |
| Warehouse Operative (EWM) | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Warehouse Floor | SAP_BR_WAREHOUSE_OPERATIVE_EWM |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | RM12 | Raw Material Ext. Procurement |  |
| Material | SG21 | SEMI21, PD, Repetitive Manuf. |  |
| Standard Routing | SG21 | SEMI21,PD,RepetitiveManuf |  |
| Company Code | 3310 |  |  |
| Plant | 3310 |  |  |
| Storage Location | 335W |  |  |

Bill of Material Structure

This overview shows the bill of material structure and the usage of each component.

| Material | Level | Material Type | Unit | Characteristic of Material |
| --- | --- | --- | --- | --- |
| SG21 | 0 | SEMI | PC | Semifinished Good Repetitive Manuf. |
| RM12 | 1 | RAW | PC | Raw Material |

Organizational Master Data in Warehouse:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Warehouse | 3350 |  |  |
| Custodian | 33413310 |  |  |
| Entitled to Dis-pose | 33413310 |  |  |

Warehouse-Specific Master Data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Storage Type | SG01 | General Storage |  |
| Storage Type | S915 | Goods Receipt from Produc-tion |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| 3KQ | Maintain Warehouse Products Attributes - MDS |
| 3KR | Maintain Storage Bins and Fixed Bin Assignments - MDS |
| 3Y1 | Create Product Master of Type "Packaging" - MDS |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BJH - Make-to-Stock Production – Repetitive Manufacturing | You have completed the steps described in the Make-to-Stock Production – Repetitive Manufacturing Test Script.Before you start with BJH, make sure you create the production version 0090 as described in the step Maintain Production Versionin the Preliminary Stepssection.Pay attention that you then use the production version 0090 for the following steps in BJH:Preliminary steps:Create Product Cost CollectorsCreate Preliminary Cost for the Product Cost CollectorTest Procedures:Anonymous Forecast and MRPCreate Planned Independent RequirementsMaterial Requirements Planning (MRP)Adjust Planning in Planning TableCheck Range of Stock CoverageMaterial StagingConfirm Repetitive Manufacturing Inclusive Backflush of MaterialsNote As there is no quota arrangement to calculate the portion between production version 0001 and 0090, the MRP run always creates a planned order for production version 0001. As such, you can manually enter the planned order for production version 0090 in the Adjust Planning in Planning Table step. |
| 3BR - Warehouse Inbound Processing | You have completed the step described in Warehouse Inbound Processing test script so that you have the stock to do the posting changes. |

### Preliminary Steps

#### Maintain Production Version

Purpose

Maintain additional settings in production version required for warehouse process.

|  |
| --- |
| Note In case a semi-finished product is to be used as a component for a subsequent production step for final assembly of a finished product, you have the opportunity to move the product to the subsequent PSA without having to carry out the putaway process first. For this, you enter a target PSA in the production version of the product. When automatic warehouse task creation is activated as per default in this test script, upon goods receipt of the semi-finished product, the system will create a warehouse task towards the bin associated with this PSA via the control cycle for the material and PSA. You can find the target PSA field in the 'Other Data' section in the production version. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad using the role Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Production Versions - C223 (C223). |  |  |
| 3 | Enter selection data | Make the following entries and choose Enter.Plant: 3310Material: SG21 |  |  |
| 4 | Select the production version | Select the production version 0090 and choose Detail view. |  |  |
| 5 | Enter data | On the Maintain Production Version: Detail screen, make the following entries:Receiving Location: 335WWarehouse Number: 3350Destination Bin: PR-AREAChoose Save Changes and close the screen.Choose Consistency Check.On the Production Version: Mass Processing screen, choose Back.Choose Save.Note An additional storage location 335I and the corresponding availability group 002 can be introduced in the Cloud WM as an optional setup. Compared to the single storage location 335W / availability group 001 setup, the new setup can help distinguish stock that is still in the process of putaway and that is already in the warehouse.For example, the storage location 335I is used as the goods receipt storage location. During the goods receipt process, the stock remains in the storage location 335I and isn't available for sale (Stock Type F0 – Unrestricted Use in Putaway) until the putaway warehouse task(s) is/are confirmed. Once the putaway is finished, the stock is automatically posted to the storage location 335W and becomes available for sale (Stock Type F – Unrestricted Use in Warehouse).To enable the 335I storage location / availability setup, there are manual setup steps to be performed according to the instructions provided in the Warehouse Management Setup Guide. For more information, see chapter Additional Manual Configuration. |  |  |

#### Maintain Warehouse Product Attributes

Purpose

In this section, you maintain warehouse product attributes using the Warehouse Monitor (/SCWM/MON) app. This app can be used for single and mass changes.

You only need to perform this step if you want to test Variant 2: Manual Warehouse Task Creation. If you go with Variant 1: Automatic Warehouse Task Creation, skip this preliminary step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as the Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Warehouse Monitor (/SCWM/MON). | The Warehouse Management Monitor SAP - Warehouse Number XX50 screen is displayed. |  |
| 3 | Choose Menu | In the hierarchy in the left screen area, choose Product Master Data > Warehouse Attribute. |  |  |
| 4 | Enter Product Number | In the /SCWM/SAPLPROD_OVERVIEW dialog box, enter the following data:Basic Attributes section:Product Number: SG21.Additional Options section:Only Prods W/o Whse Data: X.Choose Execute. | The system displays the products that haven’t been maintained yet with warehouse data on the right screen area. |  |
| 5 | Select Products | In the Warehouse Attributes area, select the products. Then choose More Methods > Mass Change/Create. |  |  |
| 6 | Select Products | In the /SCWM/SAPLPROD_OVERVIEW dialog box, make the following entries:In the Warehouse Data section:Reset Proc.Type Det. Ind.: X .Choose Execute.Resetting the process type determination indicator is only relevant for Variant 2: Manual Warehouse Task Creation in test procedures.If you choose Variant 1: Automatic Warehouse Task Creation, skip this step or make the following entries:In the Warehouse Data section:Proc.Type Det. Ind.: S1.Choose Execute. |  |  |
| 7 | Save Your Data | In the dialog box, confirm the changes. | A system message tells you that the products are saved successfully. |  |

#### Define Default Values for Warehouse Clerk (EWM)

Use

In this step, you define the default warehouse number for Warehouse Clerk (EWM).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the Fiori Launchpad as Warehouse Clerk (EWM) |  |  |
| 2. | Choose App | Choose tab page Warehouse Processing.Open app Change Inbound Deliveries - Deliveries (F1706). |  |  |
| 3. | Choose the User Icon | Choose the Icon for the logon user.Choose Settings. |  |  |
| 4. | Enter Default Value | Choose Default Parameters and make the following entry:Warehouse No.: 3350Choose Save. |  |  |

#### Define Default Values for Warehouse Operative (EWM)

Use

In this step, you define the default warehouse number for Warehouse Operative (EWM).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the Fiori Launchpad as Warehouse Operative (EWM). |  |  |
| 2. | Choose the User Icon | Choose the Icon for the logon user.Choose Settings. |  |  |
| 3. | Enter Default Value | Choose Default Values.And make the following entry in the section Material Management:Warehouse No.: 3350Choose Save. |  |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App / Transaction | Expected Results |
| --- | --- | --- | --- |
| [Check Material Document (Optional)](#unique_12) [page ] 13 | SAP_BR_WAREHOUSE_CLERK | Material Documents Overview (F1077) |  |
| [Check Goods Movement Document (Optional)](#unique_13) [page ] 14 | SAP_BR_WAREHOUSE_CLERK_EWM | Warehouse Monitor (/SCWM/MON) |  |
| [Check Warehouse Task (Optional)](#unique_14) [page ] 15 | SAP_BR_WAREHOUSE_CLERK_EWM | Warehouse Monitor (/SCWM/MON) |  |
| [Pack Finished Material (Optional)](#unique_15) [page ] 16 | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Pack Warehouse Stock (F3738) |  |
| [Create HU Warehouse Task (Optional)](#unique_16) [page ] 16 | SAP_BR_WAREHOUSE_CLERK_EWM | Create HU Warehouse Tasks (/SCWM/MONNAV_CR_HUWT) |  |
| [Create Product Warehouse Task](#unique_17) [page ] 17 | SAP_BR_WAREHOUSE_CLERK_EWM | Create Product Warehouse Tasks (/SCWM/MONNAV_CR_P_WT) |  |
| [Confirm Putaway Warehouse Tasks](#unique_18) [page ] 17 | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Process Warehouse Tasks (F4595) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Check Material Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is for checking material document posted during repetitive manufacturing backflush.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Open the SAP Fiori Launchpad with the Warehouse Clerk role. | The SAP Fiori launchpad displays. |  |
| 2 | Open Management Document Overview | Open Material Documents Overview (F1077). | The Material Documents Overview displays. |  |
| 3 | Search for Material Document | Search material documents using different criteria. Select Adapt Filters and all basic filters are displayed. Enter the entries accordingly, then choose Go.For example:Stock Change: AllMaterial: SG21Choose the row of a certain material document to view details. | The relevant Material Documents / Material Document items are shown.The GR with movement type 131 and the GI with movement type 261 are posted synchronously in one material movement document. |  |

### Check Goods Movement Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is for checking goods movement document of goods receipt posting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Fiori Warehouse Monitor (/SCWM/MON) |  |  |
| 3. | Select the node | On the Warehouse Management Monitor SAP - Warehouse Number xxxx screen, choose Documents > Warehouse Tasks and doubleclick on the node. |  |  |
| 4. | Enter the selection data | Make the following entries:Whse Proc. Category: 5 Goods Receipt PostingProduct: SG21 .Choose Run. | The goods receipt is reflected in a warehouse task of Warehouse Process Category 5 (Goods Receipt Posting) for the finished product SG21 .For component RM12, there is no EWM goods movement document of warehouse process category 6 (Goods Issue Posting), as it is consumed from an inventory-managed storage location 331B. |  |

### Variant 1: Automatic Warehouse Task Creation

#### Check Warehouse Task (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is for checking warehouse task from the production goods receipt storage type to the final storage type.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Warehouse Monitor (/SCWM/MON) |  |  |
| 3. | Select the node | On the Warehouse Management Monitor SAP - Warehouse Number xxxx screen, choose Documents > Warehouse Task and doubleclick on the node. |  |  |
| 4. | Enter the selection data | Make the following entries:Whse Process Type: .Product: SG21 .Choose Run. | The warehouse task for synchronous goods movement during backflush for repetitive manufacturing should be displayed. |  |

### Variant 2: Manual Warehouse Task Creation

#### Pack Finished Material (Optional)

Refer to the process step Pack Product into Handling Unit in Scope Item Warehouse Internal Repacking (3BW) using storage bin PR-AREA. Note down the HU number.

In the test script, go to Test Procedures > Pack Product into Handling Unit . Go to scope item [3BW](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/3BW) in the SAP Signavio Process Navigator.

#### Create HU Warehouse Task (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is for creating a HU warehouse task from a storage type to the final storage type. This might be required for immediate situations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Create HU Warehouse Tasks (/SCWM/MONNAV_CR_HUWT) |  |  |
| 3. | Decide on your filter criteria | Storage Type:S915.Handling Unit: <Handling Unit created in the previous step>Choose Execute. |  |  |
| 4. | Select your Stock | Select one of the stock lines and choose More Methods and then select Create Warehouse Task. | A dialog box with a request for data Create Warehouse Task is displayed. |  |
| 5. | Create Warehouse Task | Create the warehouse task and enter the following data:Destination Bin: SG01-GENERALWarehouse Process Type: S116Choose Create WT.Note down the warehouse task number. | As you can see in the display log, a warehouse task is created. A Warehouse Task List is automatically printed in the background.You must find the open product warehouse task in the monitor node Warehouse Task. Therefore, note down the warehouse task number. |  |

#### Create Product Warehouse Task

Refer to solution activity Create Ad Hoc Warehouse Task (Option 1) in Scope Item Warehouse Ad Hoc Goods Issue (3BT) using storage type S915 , destination storage bin SG01-GENERAL and warehouse process type S116.

In the test script, go to Test Procedures > Create Ad Hoc Warehouse Task (Option 1) . Go to scope item [3BT](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/3BT) in the SAP Signavio Process Navigator.

### Confirm Putaway Warehouse Tasks

#### Variant 1: With Fiori App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) processes the replenishment warehouse task.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Process Warehouse Tasks(F4595). |  |  |
| 3 | Enter Warehouse Task Number | On the Process Warehouse Tasks screen, make the following entries:Warehouse Task <WT number noted down in the previous step>.Choose Go. |  |  |
| 4 | Confirm Warehouse Task | Mark the checkbox for the selected warehouse task and choose Confirm.Note If you have the two availability groups setup for your warehouse, as soon as the putaway warehouse tasks are confirmed, the system automatically posts the stock type for this stock from ‘Unrestricted Use in Putaway (F0)’ to ’Unrestricted Use in Warehouse (F)’. | The following system message appears: <Warehouse task confirmed> |  |

#### Variant 2: With Radio Frequency Devices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) performs the replenishment warehouse tasks and confirms them in the system with mobile Radio Frequency device.

|  |
| --- |
| Note For working with mobile RF Devices, make sure all the steps as described in the Setup Instruction guide for scope item 63V - Mobile RF Devices in Warehousing have been performed. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open the SAP Fiori app Test RF Environment (/SCWM/RFUI)Note Here the App allows you to test working in an RF environment. For working with Mobile RF Devices, see also SAP Note [3048632](https://me.sap.com/notes/3048632). |  |  |
| 3 | Enter Data for RFUI | Whse No: 3350Resource: SHR1-1: SE01Choose Enter. |  |  |
| 4 | Choose Menu | Choose 01 System-Guided > 02 SystemGuided Queue. |  |  |
| 5 | Enter Queue Name | In the Queue field, enter for example SI-G01Choose Enter |  |  |
| 6 | Verify Source Bin and Enter HU | Note This step is Only relevant if you create handling unit for goods receipt.Verify the Src.Bin (Source Bin)HU: < Enter the HU ID from step Pack Finished Material (Optional)> |  |  |
| 7 | Verify the Source information fields | Verify the following fields if they are required:Src.Bin (Source Bin)Prod. (Product)Srce Qty (Source Quantity)Choose Enter . |  |  |
| 8 | Verify the Destination Information fields | Verify the following fields if they are required:Prod. (Product)ActQty (Quantity)Dest.Qty (Destination Quantity)DstBin (Destination Bin)Choose Enter . |  |  |
| 9 | Repeat Steps | Repeat step 6 -8 until no suitable warehouse orders are found. |  |  |
| 10 | Logoff RFUI | You can choose Back to the previous screens.Choose Logoff.Choose Save.Note If you have the two availability groups setup for your warehouse, as soon as the putaway warehouse tasks are confirmed, the system automatically posts the stock type for this stock from ‘Unrestricted Use in Putaway (F0)’ to ’Unrestricted Use in Warehouse (F)’. |  |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Make-to-Stock Production – Repetitive Manufacturing | Refer to the process step Post Processing of Error Records in Scope Item Make-to-Stock Production – Repetitive Manufacturing (BJH).In the test script, go to Test Procedures > Post Processing of Error Records . Go to scope item [BJH](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/BJH) in the SAP Signavio Process Navigator. |

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
- related-to :: [[11-inventory-warehouse-and-transportation/atualizar-area-de-abastecimento-da-producao-mds-3ks-344]]
- related-to :: [[11-inventory-warehouse-and-transportation/maintain-production-supply-area-mds-3ks-341]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3ks-343]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3ks-345]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/41U_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 31,567 chars in the whole document
