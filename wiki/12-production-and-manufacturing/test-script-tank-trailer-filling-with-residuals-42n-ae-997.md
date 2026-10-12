---
id: 12-production-and-manufacturing/test-script-tank-trailer-filling-with-residuals-42n-ae-997
title: "Test Script: Tank Trailer Filling with Residuals (42N_AE) (42N_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script (scope item 42N_AE): fill tank trailers from a process order, netting residual stock via container ID and MQC."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/storage-tank-management]
aliases: [42N_S4CLD2608_BPD_EN_AE]
keywords: [Storage Tank Management and Tank Trailer Filling, tank trailer filling, residual stock, container id, batch determination, material quantity calculation, process order, goods issue, process order confirmation, goods receipt]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/42N_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-997
topic: 12-production-and-manufacturing/storage-tank-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Tank Trailer Filling with Residuals (42N_AE) (42N_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/42N_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Storage Tank Management and Tank Trailer Filling** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Tank Trailer Filling with Residuals (42N_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232854479)

[2 Prerequisites 4](#_Toc232854480)

[2.1 System Access 4](#_Toc232854481)

[2.2 Roles 4](#_Toc232854482)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232854483)

[2.4 Business Conditions 6](#_Toc232854484)

[2.5 Preliminary Steps 7](#_Toc232854485)

[2.5.1 Add Formula for MQC 7](#_Toc232854486)

[2.5.2 Post Initial Stock for **SG2200** 8](#_Toc232854487)

[2.5.3 Post Residual Stock for FG6500 9](#_Toc232854488)

[2.5.3.1 Check Container ID 10](#_Toc232854489)

[2.5.3.2 Check Residual Stock with Filling Container ID 10](#_Toc232854490)

[2.5.3.3 Residual Stock Posting for FG6500 12](#_Toc232854491)

[3 Overview Table 14](#_Toc232854492)

[4 Test Procedures 15](#_Toc232854493)

[4.1 Create Process Order with Batch for Tank Trailer Filling 15](#_Toc232854494)

[4.2 Assign Container ID to the Batch 16](#_Toc232854495)

[4.3 Execute Batch Determination in Process Order 17](#_Toc232854496)

[4.4 Goods Issue of Components 19](#_Toc232854497)

[4.4.1 Goods Issue via Pick List 19](#_Toc232854498)

[4.4.2 Manual Goods Issue (Instead of Picking List) 20](#_Toc232854499)

[4.5 Confirm Process Order 21](#_Toc232854500)

[4.6 Post Goods Receipt for Process Order 22](#_Toc232854501)

[5 Appendix 24](#_Toc232854502)

[5.1 Succeeding Processes 24](#_Toc232854503)

## Purpose

Overview

The process starts with creation of a filling process order based on an internal or external requirement.

As a prerequisite, the tank trailer with a dedicated container ID should be weighed and the existing residual quantity should be posted to a separate residual storage location. This residual stock is considered during the subsequent filling process for the same container ID.

Using container ID as a reference batch characteristic, the batch and quantity of residual stock for the specific container ID is determined for the process order using batch determination.

The net quantity of manufactured product to be filled into the tank trailer is calculated by deducting the residual material that was already present in the tank from the total filling order quantity. A simple material quantity calculation formula is used for this purpose. The appropriate batches are selected using batch determination.

The filling process order is executed to complete the tank trailer filling process.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

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
| Production Supervisor - Process Manufacturing | SAP_BR_PRODN_SUPERVISOR_PROC | Production Management - Process Manufacturing | SAP_BR_PRODN_SUPERVISOR_PROC |  |
| Production Operator - Process Manufacturing | SAP_BR_PRODN_OPTR_PROC | Production Execution - Process Manufacturing | SAP_BR_PRODN_OPTR_PROC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Production Engineer - Process Manufacturing | SAP_BR_PRODN_ENG_PROC | Production Engineering - Process Manufacturing | SAP_BR_PRODN_ENG_PROC |  |
| BOM Engineer | SAP_BR_BOM_ENGINEER | Bills Of Material | SAP_BR_BOM_ENGINEER |  |
| Quality Technician | SAP_BR_QUALITY_TECHNICIAN | Quality Inspection | SAP_BR_QUALITY_TECHNICIAN |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure:

Table 1: Manufacturing

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | FG6500 | FIN6500, PI, PD, Tank Trailer Material |  |
| Material | SG2200 | SEMI2200, MTS-PI, PD, with Co- & By-Product | Manufactured product to be filled into the tank trailer |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 | Std. storage for production |
| Storage Location | 331B | Std. storage 2 | Std. storage for production |
| Storage Location | 331F | Residual SLoc | Stock in residual storage location represents the residual quantity (left over) available in the tank trailer |

This overview shows the bill of materials structure and the usage of each component.

Table 2: Bill of Materials Structure

| Material | Level | Material Type | Base Quantity | Unit | Comments |
| --- | --- | --- | --- | --- | --- |
| FG6500 | 0 | FERT | 1000 | KG |  |
| FG6500 | 1 | FERT | 100 | KG | The actual issued quantity of the residual material is dependent on reality. |
| SG2200 | 1 | HALB | 900 | KG | The net quantity to be filled into the tank trailer will be re-calculated. |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 3: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| 3X8 | Create Resource - MDS |
| 3X9 | Create Master Recipe - MDS |
| BLD | Create Production Version - MDS |
| 2ZW | Create Batch Management Master Data - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation | You have completed the step described in the test scrip BEG. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the test script BNZ. Posting Period is up to date. |

### Preliminary Steps

#### Add Formula for MQC

Purpose

The purpose of this activity is to add formula for Material Quantity Calculation (MQC) via changing master recipe. By setting formula, we want to dynamically calculate the net quantity of manufactured product to be filled, which is equal to the total quantity minus the residual quantity.

Prerequisites

Master Recipe must be defined already.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Production Engineer - Process Manufacturing. |  |  |
| 2 | Access the App | Open Change Master Recipe (C202). |  |  |
| 3 | Enter | Make the following entries and choose Enter.Material: FG6500Plant: 3310 |  |  |
| 4 | Check Master Recipe | Following Master Recipe should display based on standard Best Practice content:Recipe Group: 43310043Recipe: 1 |  |  |
| 5 | Check Material Assignment | Choose Materials tab page in the recipe, following materials should display under Material Component Assignments table:Material: FG6500Material: SG2200If more than one header material and /or production version exist for your recipe, select the material or production version whose material quantity calculation you want to maintain. |  |  |
| 6 | Choose MQC | On Materials tab, choose Material Quantity Calc.. |  |  |
| 7 | Check MQC | The Material Quantity Calculation screen appears. It consists of two sections:The lower section contains lines with data for each operation, phase, and material contained in the recipe. You can find following lines with materials.LineObject DescriptionTypeItemFormula IndicatorSign1:QuantityUOM1FG6500MT0000-1000KG2..FG6500MT0010100KG3..SG2200MT0020900KGIn the Formula Definition section, you can display the formula defined for the field that you have selected in the lower section. |  |  |
| 8 | Enter Formula | Place the cursor on the following cell and choose Select Formula.Line: SG2200Column: 1:Quantity, with default value: 900In the Formula Definition section, enter the following formula:[001,001]-[002,001] |  |  |
| 9 | Save Formulas | Choose Save formulas. |  |  |
| 10 | Save | On Change Master Recipe: Recipe screen, choose Save. |  |  |

#### Post Initial Stock for SG2200

Purpose

Initial stock posting for SG2200 is not required if you want to run through scope item 3L7 to produce it. This process step shows you how to post initial stock for the manufactured product directly to the storage location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | Screen name adapts according to entries. |  |
| 3 | Choose Goods Receipt-Other | Make the following entries and choose Enter.Trans./Event: Goods ReceiptReference Document: OtherMovement Type: 561 | Screen name adapts after entries are made. |  |
| 4 | Specify Material | Under the Material tab, make the following entries:Material: SG2200 | Ensure that detail data is expanded. |  |
| 5 | Specify Quantity | Under the Quantity tab, make the following entries:Qty in Unit of Entry: 1000 |  |  |
| 6 | Specify Plant and Storage Location | Under the Where tab, make the following entries:Plant: 3310Storage location: 331B |  |  |
| 7 | Check Item | Choose Enter, and ensure Item OK is selected. |  |  |
| 8 | Choose Check | Choose Check. | A popup screen displays showing creating batch XXXX. Choose Continue. |  |
| 9 | Post Goods Movement | Choose Post. | Material document XXX posted.Materials are available in stock. |  |

#### Post Residual Stock for FG6500

This process step shows you how to post residual stock for material FG6500 to the residual storage location with assigned container ID. Please be noted that, only one batch with valid stock can exist in the residual storage location for one Container ID at one time.

In real business case, operator will post this goods receipt after receiving containers with remaining leftovers (residual material) returned by customer.

##### Check Container ID

Purpose

Each tank trailer container has a unique container ID. It is represented by characteristic values in the system. This process step shows you how to check the container IDs which have already been defined for you. Optionally you can keep the characteristic values as empty and enter manually during each goods receipt returned by customer. In real business case both scenarios are possible.

Prerequisites

Characteristics must be defined already.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Characteristics (CT04). |  |  |
| 3 | Enter | Make the following entries and choose Enter.Characteristics: YQ_CONTAINER |  |  |
| 4 | Check Pre-defined Container ID | Under the Values tab, check pre-defined values:CON-01: Container01CON-02: Container02CON-03: Container03CON-04: Container04CON-05: Container05 |  |  |
| 5 | Exit | Choose Exit. |  |  |

##### Check Residual Stock with Filling Container ID

Purpose

This process step shows you how to check in the residual storage location whether there is already existing batch with specific container ID before posting initial stock. For test purpose, we assume container ID of the tank trailer container need to be filled is CON-02.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Batch Information Cockpit (BMBC). |  |  |
| 3 | Enter Under Classification Tab | On the right part of the screen, choose Classification tab, enter following value under Search with Characteristics:Selection Class: YQ_FILLINGChoose Create Values. |  |  |
| 4 | Enter Container ID | Characteristic Values section would display under the value you just enter. In this section, enter the container ID:Container IDs: CON-02 |  |  |
| 5 | Input Other Filters | On the right part of the screen, make following entries for other tabs:Material tab:Material: FG6500Plant: 3310Stock tab:No Zero Stock Lines: XStorage Location: 331FChoose Execute Selection. | Selection Result for Batches displays in the left part of the screen. |  |
| 6 | Display Stock | Choose Display Selection Result for Stock on the upper left corner. | A new table displays in the lower left part of the screen. |  |
| 7 | Check Residual Stock | On the lower left part of the screen, Selection Result for Batches displays showing the stock for your selection. You can expand the result to plant, storage location, and batch level (if any). Check if any batch exists under residual storage location 331FCase 1: If no search result, it means no batch exists with this container ID in storage location, you can proceed to next test procedure to do initial stock posting;Case 2: If there is only one batch, it means in the system the residual stock with this container ID is already recorded, thus you don’t need to do initial stock posting for it. You can check details for this batch by dragging the scroll bar to the right. Make a note of the batch number and Unrestricted stock.Note It is not consistent with real business case if there are more than one batch in the search result. Please do some stock handlement to get rid of this situation. |  |  |

##### Residual Stock Posting for FG6500

Purpose

This process step shows you how to post residual stock for the material FG6500 to the residual storage location 331F and assign Container ID CON-02 to the generated batch. In real business case, the batch represents the residual quantity that might be present inside the tank trailer returned from customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | Screen name adapts according to entries. |  |
| 3 | Choose Goods Receipt-Other | Make the following entries and choose Enter.Trans./Event: Goods ReceiptReference Document: OtherMovement Type: 561 | Screen name adapts after entries are made. |  |
| 4 | Specify Material | Under the Material tab, make the following entries:Material: FG6500 | Ensure that detail data is expanded. |  |
| 5 | Specify Quantity | Under the Quantity tab, make the following entries:Qty in Unit of Entry: <Quantity>, for example, 20 |  |  |
| 6 | Specify Plant and Storage Location | Under the Where tab, make the following entries:Plant: 3310Storage Location: 331F |  |  |
| 7 | Check Item | Choose Enter, and ensure Item OK is selected. |  |  |
| 8 | Choose Check | Choose Check. | A popup screen displays showing creating batch XXXX. Choose Continue. |  |
| 9 | Check Batch | Under the Batch tab, a batch is generated. Make a note of the batch number of this batch: __________. | The classification screen displays. |  |
| 10 | Choose Classification | Choose Classification behind the batch number. |  |  |
| 11 | Enter Container ID | On the Classification screen, enter the container ID and choose Back:Container IDs: CON-02 |  |  |
| 12 | Choose Check | Choose Check. |  |  |
| 13 | Post Goods Movement | Choose Post. | Material document XXX posted.Materials are available in stock. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Process Order with Batch for Tank Trailer Filling](#unique_14) [page ] 15 | Production Supervisor - Process Manufacturing | Create Process Order (COR1) | Process Order is created for tank trailer filling. |
| [Assign Container ID to the Batch](#unique_15) [page ] 16 | Production Supervisor - Process Manufacturing | Manage Batches (F2462) | Container ID is assigned to the produced batch. |
| [Execute Batch Determination in Process Order](#unique_16) [page ] 17 | Production Supervisor - Process Manufacturing | Change Process Order (COR2) | Materials are assigned to process order with proper batch number and quantity. |
| [Goods Issue of Components](#unique_17) [page ] 19 |  |  |  |
| [Goods Issue via Pick List](#unique_18) [page ] 19 | Production Operator - Process Manufacturing | Pick Components for Process Orders (COIK) | Components under picking list are posted. |
| [Manual Goods Issue (Instead of Picking List)](#unique_19) [page ] 20 | Warehouse Clerk | Post Goods Movement (MIGO) | Goods movements are posted. |
| [Confirm Process Order](#unique_20) [page ] 21 | Production Operator - Process Manufacturing | Confirm Process Order Phase (COR6N) | Confirmation of the process order is carried out. |
| [Post Goods Receipt for Process Order](#unique_21) [page ] 22 | Warehouse Clerk | Post Goods Movement (MIGO) | The goods receipt for the process order is posted. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Process Order with Batch for Tank Trailer Filling

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create process orders for tank trailer filling.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Process Order (COR1). |  |  |
| 3 | Enter Parameters | Make the following entries and choose Continue:Material Number: FG6500Production Plant: 3310Process Order Type: YQ02 |  |  |
| 4 | Enter General Data | On the General Data tab, make the following entries:Total Qty: <total quantity to be filled>, for example, <100>Scheduling - Type: Current date | If information dialog pop up saying Order has missing parts, choose Continue and Release Order. |  |
| 5 | Enter Goods Receipt Data | On the Goods Receipt tab, go to the Receipt section, and make the following entry:Batch: choose Create Batch.Make a note of the generated batch number: __________. You will assign container ID to the produced batch in next step. | Batch number will be generated. |  |
| 6 | Save | Choose Save.Make a note of this process order number: __________. | Process Order saved.Note In this scenario, process order is configured as automatically released. |  |

### Assign Container ID to the Batch

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to assign container ID of the filling container where you are going to fill the produced batch you created before in the process order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Batches (F2462). |  |  |
| 3 | Search Batch | Make the following filters and choose Go.Material: FG6500Batch: XXXX (batch number from previous step) |  |  |
| 4 | Select Batch | On the search result list, select the entry that does not represent a plant specific stock.Choose Edit on the fact sheet. |  |  |
| 5 | Assign Container ID | Choose Classification tab, enter the Container ID.Container IDs: CON-02 (Container ID - 02) |  |  |
| 6 | Save | Choose Save. | Container ID is assigned to the batch. |  |

### Execute Batch Determination in Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to consume the leftover quantity from the tank trailer, for example, quantity from residual storage location with respect to filling container ID (from last step) and recalculate required quantities for the manufactured material to be filled into the tank trailer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Process Order (COR2). | The Change Process Order: Initial screen displays. |  |
| 3 | Enter Process Order Number | Make the following entries and choose Continue.Process Order: XXXX (from previous steps) | The Change Process Order: Header - General Data screen displays. |  |
| 4 | Navigate to Material List | Choose Material List. | The Change Process Order: Material List screen displays. |  |
| 5 | Check Material List | In the Material List, two items are listed. The Requirement quantity of each item is precalculated according to BOM structure. |  |  |
| 6 | Choose Item FG6500 and Check Storage Location | For item with material FG6500, make sure the residual storage location is assigned:Storage Location: 331FSelect this item and choose Execute batch determination above the list. Choose Enter to ignore any information dialog. | The Batch Determination CO: Select Batches screen displays. |  |
| 7 | Find Batch and Enter Quantity | In the Batch Selection list, find the batch with filling container ID ( CON-02,Container02 ), as indicated by the description under Characteristic Sorting, and check the Available Quantity for this batch .For this Batch, enter following:Split Quantity: equals to available quantity for this batch. | The batch number and quantity for the batch is what you enter in preliminary step "Initial Stock Posting for FG6500" if relevant. |  |
| 8 | Remove Quantity for Other Batches | For all other batches listed in the Batch Selection list (if any), remove any suggested Split Quantity. |  |  |
| 9 | Choose Copy | Choose Copy, and choose Enter to ignore any information dialog. | Go back to Change Process Order: Material List screen. |  |
| 10 | Check Determined Batch for FG6500 | In the Material List, a new line is generated for Item FG6500, in which the batch has been determined. Check the Requirement Quantity of this batch and make sure it is equal with the quantity you just enter. If not, manually change it and choose Enter. | The complete quantity of the batch is assigned. |  |
| 11 | Remove Any Additional Requirement Quantity for FG6500 | In the header line of Item FG6500, if there is any remaining requirement quantity, remove it to empty and choose Enter. | Choose Enter to ignore any information dialog. |  |
| 12 | Choose MQC | On the Change Process Order: Material List screen, choose Material Quantity Calculation button on the top, | The Material Quantity Calculation screen displays. |  |
| 13 | Save Calculation Result | Check calculation result. Choose Save formula and copy result. |  |  |
| 14 | Check Requirement Quantity for SG2200 | In the Material List, for item with material SG2200, the Requirement quantity will adjust accordingly if needed. | The net quantity of SG2200 is calculated by deducting the residual material FG6500 from the total quantity supposed to be filled. |  |
| 15 | Choose Item SG2200 | Select item SG2200 and choose Execute batch determination button above the list. Choose Enter to ignore any information dialog. |  |  |
| 16 | Choose Copy | Choose Copy. | Go back to Change Process Order: Material List screen. In addition, the batch number has been determined. |  |
| 17 | Save | Choose Save. |  |  |

### Goods Issue of Components

Purpose

The withdrawal of the components is used for the process order. This withdrawal can be done by using the picking list or doing a manual goods issue.

#### Goods Issue via Pick List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how all materials that are moved to the production storage location can be issued to the process order using the pick list when the released process order is ready for picking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Pick Components for Process Orders (COIK). | The Picking List: Initial screen displays. |  |
| 3 | Enter Restriction and Execute | Make the following entries and then choose Execute.Profile: 000002Process Order: <XXXX>(from previous steps)Plant: 3310 | The Order Information System: Detail List of Components screen displays. |  |
| 4 | Picking Materials | Select all items and choose Picking. | The Picking list screen displays. On this screen, a list of all the selected reservations displays. |  |
| 5 | Post Goods Movements | Choose Post. | The goods movements are posted. |  |

#### Manual Goods Issue (Instead of Picking List)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how the system performs a goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Initial screen displays. |  |
| 3 | Enter Process Order | Make the following entries and then choose Enter.Trans./Event: Goods IssueReference Document: OrderOrder number: XXXX (from previous steps)Movement Type: 261 | The screen name adapts after entries are made. |  |
| 4 | Check Each Item | For each item shown, select Item OK. | Ensure that detail data is expanded. |  |
| 5 | Post Goods Movements | Choose Post. | The goods movements have been posted. |  |

### Confirm Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents include the processing status of order, operations, phases and individual capacities. It is an instrument to control the order. The time ticket confirmation allows recording either the default times for machine and labour usage, or record actual times for major deviations. Backflushed materials will be posted automatically during respective phase confirmations. You can post scrap quantities as an optional. If no major deviations occurred, only the last phase (milestone) must be confirmed. Using milestone confirmation, all prior phases are confirmed automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Process Order Phase (COR6N). | The Enter Time Ticket for Process Order screen displays. |  |
| 3 | Enter Confirmation Option | Make the following entries and then choose Enter.Order: <XXXX> (from previous steps)Choose Enter or select phase (0020) from search help of Phase field.Confirm type: Final confirmationClear open reservations: X | If the system shows the message Total quantity confirmed not equal to planned quantity to be confirmed, choose Enter to ignore it. |  |
| 4 | Propose Actual Data | Choose Actual Data, make the changes for the following fields:Scrap: <Enter the amount you want to Scrap>Yield: <Based on the origin quantities minus Scrap>Reason for Var: <Enter scarp reason if need>, for example, <0001> | The Quantities and Activities will be filed automatically. You can make necessary change. |  |
| 5 | Save Confirmation | Choose Save. | The final confirmation of the last operation is carried out. Costs and activity quantities are recalculated in proportion to the yield quantity. |  |

### Post Goods Receipt for Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods receipt for the process order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Initial screen displays. |  |
| 3 | Enter Process Order | Make the following entries and then choose Enter.Trans./Event: Goods ReceiptReference Document: OrderOrder Number: <XXXX>(from previous steps)Movement Type: 101 | Screen name adapts after entries are made. |  |
| 4 | Check Product | Check the product listed in the table. |  |  |
| 5 | Enter Goods Receipt Storage Location | On the Where tab, make the following entry:Storage Location: 331A |  |  |
| 6 | Check Item | Select Item OK for each line. | Ensure that detail data is expanded. |  |
| 7 | Check | Choose Check in the lower right corner. |  |  |
| 8 | Post Goods Movement | Choose Post. | The goods movements are posted. |  |

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 3F0 (Event-Based Production Cost Posting) | This procedure updates work-in-process calculation, overhead calculation, and variance calculation by linking the posting to the events.Note Start from CE2105, the default Best Practice content is based on event-based result analysis for new customer install and add new country only, rather than previous period-end posting. For existing customers (who activated content before 2105), the default remain unchanged to Period-End Closing – Plant BEI till customer makes the decision to switch. For migration to Event based from Periodic please refer [Production Settlement in Parallel Ledgers](https://help.sap.com/viewer/4032610758dc437089f0c28320eec93f/LATEST/en-US/e49a3770f22547a392455154f3eef6e2.html). If you are still using period-end posting, you may need to refer to non-standard Scope Item BEI - Period-End Closing – Plant. |

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
- related-to :: [[12-production-and-manufacturing/inbound-storage-tank-management-process-manufacturing-3uk-ae-971]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/42N_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 38,353 chars in the whole document
