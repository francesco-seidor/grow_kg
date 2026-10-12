---
id: 06-management-accounting/product-cost-related-master-data-changes-consumer-products-61w-ae-test
title: Product Cost Related Master Data Changes – Consumer Products (61W_AE) Test Script (61W_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script (scope item 61W, AE) for off-cycle standard cost updates: BOM change, price change, costing run, analytics."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/product-costing-and-standard-cost-updates]
aliases: [61W_S4CLD2608_BPD_EN_AE]
keywords: [Product Costing Runs and Standard Cost Updates, product cost master data changes, bom change with change master, change master, material price change, future prices, costing run, info record condition, costing variants, material price analysis]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/61W_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1141
topic: 06-management-accounting/product-costing-and-standard-cost-updates
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Product Cost Related Master Data Changes – Consumer Products (61W_AE) Test Script (61W_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/61W_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Product Costing Runs and Standard Cost Updates** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Product Cost Related Master Data Changes – Consumer Products (61W_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232857915)

[2 Prerequisites 4](#_Toc232857916)

[2.1 System Access 4](#_Toc232857917)

[2.2 Roles 4](#_Toc232857918)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232857919)

[2.4 Business Conditions 7](#_Toc232857920)

[2.5 Preliminary Steps 7](#_Toc232857921)

[2.5.1 Check Product Cost Planning SSCUIs 7](#_Toc232857922)

[2.5.2 Check Purchasing Info Record 8](#_Toc232857923)

[2.5.3 Check Bill of Material 9](#_Toc232857924)

[3 Overview Table 11](#_Toc232857925)

[4 Test Procedures 13](#_Toc232857926)

[4.1 Periodic Product Cost Related Master Data Changes 13](#_Toc232857927)

[4.1.1 Changes in Quantity Structure 13](#_Toc232857928)

[4.1.1.1 Periodic BOM Change with Change Master 13](#_Toc232857929)

[4.1.1.1.1 Create Change Master 13](#_Toc232857930)

[4.1.1.1.2 Exchange a Component in the Material BOM 14](#_Toc232857931)

[4.1.1.1.3 Set Change Master Status to Inactive 16](#_Toc232857932)

[4.1.1.1.4 Manually Create Production Order (Optional) 17](#_Toc232857933)

[4.1.2 Changes of Material Price 18](#_Toc232857934)

[4.1.2.1 Option 1: One-Step Price Change 18](#_Toc232857935)

[4.1.2.1.1 Price Change for Individual Material 18](#_Toc232857936)

[4.1.2.2 Option 2: Two-Step Price Change 20](#_Toc232857937)

[4.1.2.2.1 Enter Future Prices 20](#_Toc232857938)

[4.1.2.2.2 Release Planned Price Changes 21](#_Toc232857939)

[4.1.3 Changes of Info Record Condition 23](#_Toc232857940)

[4.2 Periodic Cost Estimation Based on Changed Product Cost Related Master Data Changes 24](#_Toc232857941)

[4.2.1 Create Costing Run 25](#_Toc232857942)

[4.2.2 Execute Costing Run 26](#_Toc232857943)

[4.3 Analytics 28](#_Toc232857944)

[4.3.1 Display Material Price Change Documents 28](#_Toc232857945)

[4.3.2 Material Price Analysis 29](#_Toc232857946)

[4.3.3 Execute Costing Run Comparision 30](#_Toc232857947)

[4.4 Quantity Structure Re-Exchanges (Optional) 31](#_Toc232857948)

[4.4.1 Periodic BOM Re-Exchange with Change Master (Optional) 31](#_Toc232857949)

[4.4.1.1 Create Change Master (Optional) 31](#_Toc232857950)

[4.4.1.2 Change to Original Component in the Material BOM (Optional) 33](#_Toc232857951)

[4.4.1.3 Set Change Master Status to Inactive (Optional) 34](#_Toc232857952)

[4.4.1.4 Manually Create Production Order (Optional) 35](#_Toc232857953)

## Purpose

Overview

This scope item gives you an example of possible handling options for updating standard costs outside of the annual operations planning within a Consumer Products industry process. Updates in standard costs are necessary when unforeseen events influence the material valuation significantly. As examples, the valuation-related changes are based on the following business situations:

1. A quantity structure change in the Bill of Material (BOM) is needed because of quality problems with a component. A change-master-controlled update of a production BOM is used for the exchange of a production component. The change-number-controlled approach allows a date-effectivity-based attribute management on both the BOM header and BOM items levels. The BOM header and items can only be changed with a new active change number. Setting the change number status to active releases the scope per change number. Once the status becomes inactive, changes are no longer possible.
2. Significant price change for a raw material.

After the unforeseen valuation-related changes are done, a new off-cycle costing run is created and executed to reflect the changes accordingly in the master data.

Analytics, such as material price analysis and costing run comparison, complete the process.

This scope item can also support parallel standard costing. However, the current test process is to use the costing variant PYC1 based on the related delivered standard settings.

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Logon |
| --- | --- | --- | --- | --- |
| BOM Engineer | SAP_BR_BOM_ENGINEER | Bills Of Material | SAP_BR_BOM_ENGINEER |  |
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Cost Accountant - Inventory | SAP_BR_INVENTORY_ACCOUNTANT | Inventory Accounting | SAP_BR_INVENTORY_ACCOUNTANT |  |
| Production Engineer - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC | Production Engineering - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Material Master Data:

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Material | FG0513 | Carton 12x1kg Bags Dark Beans Guatemala | Batch-Managed Finished Good, Make-to-Stock |
| Material | RM0502 | Raw Coffee Beans - Guatemala | Batch-Managed Raw Material |
| Material | PK0505 | Coffee Bag "Light" 1 kg | Batch-Managed Packaging Material, MRP and Costing Relevant |
| Material | PK0506 | Coffee Bag "Light" 1 kg NEW | Batch-Managed Packaging Material, MRP and Costing Relevant, Material for Exchange |
| Material | PK0507 | Carton for 12 x 1kg Bags | Packaging Material, MRP and Costing Relevant |
| Material | PK0504 | Label (Batch) | Batch Managed Packaging Material, MRP and Costing Relevant |

Organizational Data:

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |
| Controlling Area | A000 | Controlling Area A000 |  |
| Cost Center | 33101301 | Manufacturing 1 (AE) |  |

Bill of Material Structure:

| Material | Level | Material Type | Unit | Characteristics of Material | Component Quantity | Component UOM |
| --- | --- | --- | --- | --- | --- | --- |
| FG0513 | 0 | FERT | PC | Finished Material, Batch-Managed, Make-to-Stock | 10 | PC |
| RM0502 | 1 | ROH | PC | Raw Material, Batch-Managed, External Procurement | 132 | KG |
| PK0505 | 1 | VERP | PC | Packaging Material, Batch-Managed, External Procurement | 120 | PC |
| PK0504 | 2 | VERP | PC | Label | 10 | PC |
| PK0507 | 2 | VERP | PC | Packaging Material | 10 | PC |

For more information on creating your own master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS |
| 3Y1 | Create Product Master of Type "Packaging" - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BLD | Create Production Version - MDS |
| 2ZW | Create Batch Management Master Data - MDS |

### Business Conditions

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |
| J58 - Accounting and Financial Close | Execute to create open posting periods. |
| BNU - Create Costing Run - MDS | Complete all steps in the test script. |

### Preliminary Steps

#### Check Product Cost Planning SSCUIs

The following scope item assumes the use of the standard content settings for the costing variant PYC1 with the related assignments for the material valuation.

In case there are adoptions based on your business requirements in place or are planned to be set up, please be aware that this might as well influence this scope item as changes to the strategy sequence of the valuation variant will lead to other results.

Example:

| Costing Variant | Valuation Variant – Strategy Sequence (Material valuation) | Description | Comment |
| --- | --- | --- | --- |
| PYC1 | Valuation Variant - 0Y1/Plant 3310:Material ValuationPriority 1 – Price from Purchasing Info RecordPriority 2 – Valuation Price According to Price Control in Material Master | Cost Estimate Standard | This Costing Variant is used to create standard product cost estimates for the selected materials. Based on the result, the material valuation data will be updated. |
| P00L | Valuation Variant - 00L/Plant 3310Material ValuationPriority 1 – Planned Price 1*Priority 2 – Price from Purchasing Info RecordPriority 3 – Standard PricePriority 4 – Moving Average Price | Legal Mat Cst Est Ldgr-0L | This Costing Variant is used to create standard product cost estimates for the selected materials for Ledger 0L. Based on the result, the material valuation data will be updated for Ledger 0L only. |

* The Planned Price 1 can be set in the material master directly or in case of mass changes for these updated please refer to the scope item “Mass Load and Mass Maintenance for Product (1RM)”.

The current scope item assumes the use of the standard content settings for the costing variant PYC1 with the related assignments.

For more detailed information the following scope item can be referred “Standard Cost Calculation (BEG)”.

#### Check Purchasing Info Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the Purchasing Info Record for RM0502.

|  |
| --- |
| Note If other scope items have already been executed, it might be that a Purchasing Info Record for material RM0502 exists. Based on the valuation strategy of the costing variant the Purchasing Info Record will be taken with first priority and the additional step “Changes of Info Record Condition” is needed during process execution. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Enter Selection | On the Manage Purchsing Info Records screen, make the following entries and choose Go:Material Number: RM0502Plant: 3310 |  |  |
| 4 | Review Data | On the Manage Purchasing Info Records screen, the related data is shown in the section Info Records:If no Info Record is shown, you need to skip the step “Changes of Info Record Condition”, as this step is not relevant for the subsequent process steps.If an Info Record is displayed, you need to run the step “Changes of Info Record Condition” in any case, as this is relevant for the subsequent process steps. |  |  |

#### Check Bill of Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the BOM for FG0513.

|  |
| --- |
| Note If this scope item has already been executed, the master data structure is changed. Within this step, you check the BOM for semifinished material FG0513. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Maintain Bill Of Material - Create, change & display BOMs (F1813). | The Maintain Bill of Material screen is displayed. |  |
| 3 | Enter Selection | On the Maintain Bill of Material screen, make the following entries and choose Go:Material Number: FG0513Plant: 3310 |  |  |
| 4 | Review BOM | On the Maintain Bill of Material screen, go to the Bills of Material list and click the line with material number FG0513 to view the components.If the component PK0505 is displayed and no change number is visible in column Change number for that component, this scope item has not been executed and you can continue with next step.If the component PK0505 is displayed but a change number is visible in column Change number, click on the Display Timeline button next to the Select Change Number field and review the entries. Make a note of the dates when the change to PK0506 and the change back to PK0505 has been executed. Ideally these dates are the same and you can continue with next step.Note If previous test has not followed exactly the validity dates of this scope item or there is a time frame between the two dates, you might need to adopt validity date for change master or production order creation date while you run through this scenario according to that information.If the component PK0506 is displayed, click on the Display Timeline button next to the Change Number field and review the entries. Make a note when the change from PK0505 to PK0506 has been executed. Run chapter Create Change Master (Optional) to Set Change Master Status to Inactive (Optional) and use the date noted as Valid From date for Change Master (if the date is in the past use current date). |  |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the home page will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the home page using the search bar.

If you want to personalize the home page and include the hidden apps, navigate to your user profile and choose Settings > App Finder.

| Process Step | Business Role | Transaction/App | Expected Output |
| --- | --- | --- | --- |
| Periodic Product Cost Related Master Data Changes |  |  |  |
| Changes in Quantity Structure |  |  |  |
| Periodic BOM Change with Change Master |  |  |  |
| [Create Change Master](#unique_11) | BOM Engineer | Create Change Master (CC01) | A Change Master is created. |
| [Exchange a Component in the Material BOM](#unique_12) | BOM Engineer | Maintain Bill Of Material - Create, change & display BOMs (F1813) | The BOM is changed. |
| [Set Change Master Status to Inactive](#unique_13) [page ] 16 | BOM Engineer | Manage Change Masters (F2212) | The Change Master is changed. |
| [Manually Create Production Order (Optional)](#unique_14) [page ] 17 | Production Supervisor - Discrete Manufacturing | Create Production Order (CO01) | A Production Order is created. |
| Changes of Material Price |  |  |  |
| Option 1: One-Step Price Change |  |  |  |
| [Price Change for Individual Material](#unique_15) [page ] 18 | Cost Accountant - Inventory | Manage Material Valuations (F2680) | The Material Price is updated directly. |
| Option 2: Two-Step Price Change |  |  |  |
| [Enter Future Prices](#unique_16) [page ] 20 | Cost Accountant - Inventory | Manage Material Valuations (F2680) | The new future valuation prices are updated in all currencies and valuations in the material ledger data and the company code currency in the material master record. |
| [Release Planned Price Changes](#unique_17) [page ] 21 | Cost Accountant - Inventory | Manage Material Valuations (F2680) | The future prices (in the various currencies and valuations) is updated as the current standard price or valuation price. |
| [Changes of Info Record Condition](#unique_18) [page ] 23 | Purchaser | Manage Purchasing Info Records (F1982) | The purchase info records are corrected. |
| Periodic Cost Estimation Based on Changed Product Cost Related Master Data Changes |  |  |  |
| [Create Costing Run](#unique_19) [page ] 25 | Cost Accountant - Inventory | Manage Costing Runs - Estimated Costs (F1865) | Costing run is created. |
| [Execute Costing Run](#unique_20) [page ] 26 | Cost Accountant - Inventory | Manage Costing Runs - Estimated Costs (F1865) | Costing run is executed. |
| Analytics |  |  |  |
| [Display Material Price Change Documents](#unique_21) | Cost Accountant - Inventory | Display Material Price Change Documents (F6684) | All material price change documents can be reviewed. |
| [Material Price Analysis](#unique_22) [page ] 29 | Cost Accountant - Inventory | Manage Material Valuations (F2680) | Inventory value, new price, and flow of value change is reviewed. |
| [Execute Costing Run Comparision](#unique_23) [page ] 30 | Cost Accountant - Inventory | Costing Run Comparison (S_ALR_87099932) | Costing Runs are compared. |
| Quantity Structure Re-Exchanges (Optional) |  |  |  |
| Periodic BOM Re-Exchange with Change Master (Optional) |  |  |  |
| [Create Change Master (Optional)](#unique_24) [page ] 31 | BOM Engineer | Create Change Master (CC01) | A Change Master is created. |
| [Change to Original Component in the Material BOM (Optional)](#unique_25) [page ] 33 | BOM Engineer | Maintain Bill Of Material - Create, change & display BOMs (F1813) | The BOM is changed. |
| [Set Change Master Status to Inactive (Optional)](#unique_26) [page ] 34 | BOM Engineer | Change Change Master (CC02) | The Change Master is changed. |
| [Manually Create Production Order (Optional)](#unique_27) [page ] 35 | Production Supervisor - Discrete Manufacturing | Create Production Order (CO01) | A Production Order is created. |

## Test Procedures

### Periodic Product Cost Related Master Data Changes

#### Changes in Quantity Structure

There are different possibilities to influence the quantity structure. One option is the exchange of a component within the BOM used for production (and calculation). Assume that there is a quality issue with component PK0505 which is delivered from Supplier A. This component needs to be exchanged by a more expensive component PK0506 from Supplier B until the quality problems of Supplier A are resolved.

This process step shows you how to change BOM with change master to track this change and stay compliant.

##### Periodic BOM Change with Change Master

###### Create Change Master

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the Change Master.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Change Master (CC01). |  |  |
| 3 | Enter Change Number | On the Create Change Master: Initial Screen, enter data provided in the following example and press Enter.Change Number: 61W_XX (XX can be any number)Remain default values in other fields. |  |  |
| 4 | Enter Change Master Data | On the Create Change Master: Change Header screen, enter data provided in the following example and press Enter.In the empty field next to Change Number, enter Change Master for BOM FG0513.Valid From: <Today +1 month>Change no. status: 01 Active |  |  |
| 5 | Select Checkboxes for Bill of Material | On the Create Change Master: Object Types screen, in the Object types table, Bill of Material row, select the following checkboxes:Actv.ObjectMgtRec |  |  |
| 6 | Select BOM | Choose Objects and select tab Mat. BOM. On the screen Create Change Master: Material BOM: Overview. Make the following entries and press Enter:Material: FG0513Plant: 3310BOM Usg: 1 |  |  |
| 7 | Choose Save | Choose Save. | The Change Master is created. |  |

###### Exchange a Component in the Material BOM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to exchange one of the materials with another material with which you can go ahead with production. Because component PK0505 has some quality problems in the current delivery, you want to use the same raw material PK0506 from supplier B to go ahead with your production.

You do a change in bill of material with change master to track this change and stay compliant.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Bill Of Material - Create, change & display BOMs (F1813). |  |  |
| 3 | Search for the BOM to be changed | On the Maintain Bill of Material screen make the following entries and choose Go:Material: FG0513Plant: 3310BOM Usage: Production | The BOM to be changed displays. |  |
| 4 | Choose the BOM to be changed | Choose the correct BOM to be changed by clicking on it. |  |  |
| 5 | Edit the Bill of Materials | Select Edit with Change Number. |  |  |
| 6 | Assign Change Master | On the Edit with Change Number screen, make the following entries and choose Edit with Change Number:Use Exisiting Change Number: YESChange Number: Select the Change Master 61W_XX from the list (the change master created in previous step) |  |  |
| 7 | Change BOM Item | In the BOM Item Number 0020 line in the Components tab, exchange the material PK0505 by PK0506. |  |  |
| 8 | Choose Save | Choose Save. | The BOM is changed. |  |
| 9 | Select a Change Number | On the Maintain Bill of Material screen you can review the changes.If you select a specific date in Selected Date you will see the valid Bill of Materials for the chosen date.If you select one of the available change numbers from the Select Change Number Field, you see the changes relevant to this change number. The Selected Date is filled according to the Change Master Date. | Note The changed component will only display when the relevant Change Number is selected. |  |

###### Set Change Master Status to Inactive

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to set the Change Master Status to Inactive so that this specific Change Master can't be used anymore for managing further changes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Change Masters (F2212). | The Manage Change Master app launches. |  |
| 3 | Search for Change Number to be changed | On the Manage Change Masters screen, make the following selection and choose Go.Change Number: 61W_XX (XX can be any number)Note If you already see your Change number in the table, skip this step. | The relevant Change Masters are displayed. |  |
| 4 | Make changes to Change Number | Click on the change number in the overview table. On the Change Master screen, choose Enter. | The Change Change Master: Change Header screen is displayed. |  |
| 5 | Set Change Master Status | In the Change no.Status field, select 02-Inactive and choose OK. | The Change Master Status is set to Inactive; then the Change Master can't be used anymore. |  |
| 6 | Choose Save | Choose Save. | The Change Master is changed. |  |

###### Manually Create Production Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a production order for seminfinished material FG0513 and check if the new material PK0506 is adopted as component.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Production Order (CO01). | The Production Order Create: Initial Screen displays. |  |
| 3 | Enter the Order Information | Make the following entries and choose Enter.Material: FG0513Production Plant: 3310Order Type: YBM1 |  |  |
| 4 | Enter the Order Details | Make the following entries and choose Enter.Total Qty: 10End: <Today's date +6 weeks>Note Confirm the information pop up with Continue. If you want to avoid the pop up you need to post intial stock for the components. | The Start date is calculated and the date falls after the valid-from date of change master. |  |
| 5 | Check Component | Choose Components. | Component PK0506 displays instead of PK0505. |  |
| 6 | Save | Choose Save. |  |  |

#### Changes of Material Price

You can make a price change with the following two alternatives:

- Option 1: In a single processing step with immediate effect: When material costs are changed, inventory is revaluated with all price controls, including valuation with standard price and valuation with periodic unit price.
- Option 2: Change in a two-step procedure via determine Future Prices and Releasing Planned Prices.

For more detailed information the following scope item can be referred “Managing Material Price Changes and Inventory Values (1ZT)”.

##### Option 1: One-Step Price Change

###### Price Change for Individual Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity updates the material price of a single material with immediate effect.

Alternatively, you can use the app Upload Material Inventory Prices (F4006) to update the material prices of multiple materials at once.

|  |
| --- |
| Note The price must be updated for each Ledger such as 0L and 2L or 3L separately. Inventory prices can as well be changed per ledger via app Manage Material Valuations (F2680). |

For this scope item it is assumed that the follow on standard cost estimation will update all ledgers with same standard cost (not ledger specific).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Material Valuations (F2680). | The Manage Material Valuations (F2680) screen displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:Company Code: 3310Material: RM0502Plant: 3310 | The Current Material Valuation screen displays by ledger. |  |
| 4 | Enter Data | Select the first entry in the table to navigate to the details page. Choose Change Inventory Prices on the top right of the screen (if Change Inventory Prices is not visible, choose the More icon first.)Select the current date as the Posting Date.In the Company code currency row of the Reference Price area, change the value of New Price to a different numeric value, for example 5.5.In the Prices in other Valuations area, select the overall checkbox left of the Valuation View. Now the Convert Prices button becomes active. Choose Convert Prices.Choose Save. |  |  |

##### Option 2: Two-Step Price Change

The price change in a two-step procedure will be used to prepare price changes effective on a specific date in the future, for example the first day of the next period. The price release will be done manually in this scope item.

###### Enter Future Prices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The new future valuation prices are updated in all currencies and valuations in the material ledger data and the company code currency in the material master record.

|  |
| --- |
| Note The price must be updated for each Ledger such as 0L and 2L or 3L separately. |

For this scope item, it is assumed that the follow on standard cost estimation will update all ledgers with same standard cost (not ledger specific).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Material Valuations (F2680). | The Manage Material Valuations (F2680) screen displays. |  |
| 3 | Enter Data | Make the following entries:Material: RM0502Plant: 3310Choose the Go button. |  |  |
| 4 | Enter Data | Select the box for the material with Currency Type 10 (Company code Currency) and choose Change Future Prices with Reference.Make following entries:Valid from: <Start of Next Period>Valid from Date: <keep defaulted date or enter a specific date in the future>Price Source: Standard PriceLedger to Be Translated From: 0L (Ledger 0L)Currency Type to Be Translated From: 10 (CCde Crcy)Currency Translation Date: <same data as set for Valid from Date>Exchange Rate Type: M (Standard translation at average rate)Additional Factor: Example 1.25Choose the OK button.Note Make the same entries for Crcy type/val.view 30 (Group currency) except for Currency Type/Valuation To Be Translated From should be set to Group currency. | Additional Factor: Here, you can specify a factor by which the price of the material should be multiplied.Example:If you want to increase the price of a material by 10%, enter the factor 1.1.If you want to decrease the price of a material by 10%, enter the factor 0.9. |  |
| 5 | Review Data | Select the line to navigate to the Current Material Valuation view of the material. | Here you can see the impact of price change in the future price based on additional factor that you specified.You can review the future price for company code and group. |  |

###### Release Planned Price Changes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The system does the following:

- Updates the valid future prices (in the various currencies and valuations) as the current standard price or valuation price.
- Calculates a revaluation amount for the specific inventory quantity and revaluates the inventory value by this amount.

The offsetting entry takes place in the revaluation account in accordance with account determination.

If no material stock exists, only the price is changed.

|  |
| --- |
| Note The price must be updated for each Ledger such as 0L and 2L or 3L separately. |

Prerequisites

Valid planned prices must exist in the system (validity date), meaning that the validity date must be reached. If no valid planned prices exist in the system, the materials will remain valuated with the price used before.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Material Valuations (F2680). | The Manage Material Valuations (F2680) screen displays. |  |
| 3 | Enter Data | Make the following entries:Material: Example RM0502Plant: 3310Choose the Go button. |  |  |
| 4 | Enter Data | Select both valuation views for the material (Company code currency and Group currency) and choose Release Planned Price Changes. |  |  |
| 5 | Enter Data | In the Release Planned Price Changes dialog box, make an entry in Document Header Text and deselect Consider Thresholds for Price Changes. Choose the Save button to execute. |  |  |
| 6 | Display Changes | Select on the entry again to navigate to the Current Material Valuation view for the material. | You can see the updated inventory price for the material in both Company code currency and Group currency. |  |

#### Changes of Info Record Condition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity updates already existing Info Record data accordingly with the former material price change.

|  |
| --- |
| Note If no Info Record for the material RM0502 and plant 3310 already exists in the system, you can skip this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Enter Selection | On the Manage Purchasing Info Records screen, make the following entries and choose Go:Material Number: RM0502Plant: 3310 |  |  |
| 4 | Review Data | On the Manage Purchsing Info Records screen, related data is shown in the section Info Records.If no Info Record is shown, skip this step.If an Info Record is displayed, select the related data and open the detailed information. |  |  |
| 5 | Edit Data | On the Purchasing Info Records screen, for the selected Info Record, choose Edit |  |  |
| 6 | Enter Condition Data | In the Conditions section, choose the detailed information for the current valid condition record.In the General Information area, make the following entries:Amount: <same or higher value than the one set in the former chapter “Changes of Material Price”, for example 5.55>Choose Apply. | Condition Data is changed. |  |
| 7 | Save your Data | Choose Save. | The purchasing info record is saved. |  |

### Periodic Cost Estimation Based on Changed Product Cost Related Master Data Changes

In the following activities, you create a costing run.

The following table shows the combinations available in standard content for separate ledger based standard product costing.

| Costing Type | Ledger | Costing Variant | Valuation Variant | Costing Sheet | Impact |
| --- | --- | --- | --- | --- | --- |
| 01 | Blank - means update to all Ledgers | PPC1-Standard Cost Est. (Mat.) | 001 | XXXXPC (XXXX represents default company code) | Will update all ledgers with same standard cost |
| 01 | Blank - means update to all Ledgers | PYC1-Cost Estimate Standard 0Y1 | 0Y1 | XXXXPC (XXXX represents default company code) | Will update all ledgers with same standard cost |
| 01 | Blank - means update to all Ledgers | PYC2-Cost Estimate Plan 0Y2 | 0Y2 | XXXXPC (XXXX represents default company code) | Will update all ledgers with same standard cost |
| 0L | 0L - only update to 0L | P00L-Legal Mat Cst Est Ldgr-0L) | 00L | XXXXPC (XXXX represents default company code) | Will update Ledger 0L only |
| 2L | 2L - only update to 2L | P02L-Legal Mat Cst Est Ldgr-2L | 02L | XXXXPC (XXXX represents default company code) | Will update Ledger 2L (should use only when you have Ledger 2L in FI) |
| 3L | 3L - only update to 3L | P03L-Legal Mat Cst Est Ldgr-3L | 03L | XXXXPC (XXXX represents default company code) | Will update Ledger 3L (should use only when you have Ledger 3L in FI) |

For this scope item the Costing Variant PYC1 is assumed to be used for the creation of the valuation relevant standard cost estimation.

#### Create Costing Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a costing run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Costing Runs - Estimated Costs (F1865). | The Manage Costing Runs Estimated Costs view displays. |  |
| 3 | Creating Costing Run | Choose the Create button. | The Create New Costing Run view displays. |  |
| 4 | Enter Parameters for Costing Run | Make the following entries and choose Enter.Costing Run: 61W_XX (XX can be any number)Costing Run Date: <later than validity of BOM component change, i.e. at least 1 month>Description: Costing Run 61W_XX (XX can be any number)Costing Variant: PYC1Costing Version: 1Controlling Area: A000Company Code: 3310Costing Date From: <later than validity of BOM component change, i.e. at least 1 month>Costing Date To: <Adopt the default value>Qty Structure Date: <later than validity of BOM component change, i.e.at least 1 month>Valuation Date: <later than validity of BOM component change, i.e. at least 1 month> |  |  |
| 5 | Save Costing Run | Choose the Save button. |  |  |

#### Execute Costing Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you execute the costing run. Configured materials are not included.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Costing Runs - Estimated Costs (F1865). | The Manage Costing Runs Estimated Costs view displays. |  |
| 3 | Select Costing Run | Search for the costing run created in the previous step.Select the costing run and choose Edit. |  |  |
| 4 | Open Costing Run | Check the following entry:Costing Run: The costing run created in the previous step is entered.In the Edit Costing Run screen, expand the Processing section. |  |  |
| 5 | Create Cost Estimates | In the Processing table, for each row, there is a Change Parameter button in the Parameters column. Choose the one in the selection row and make the following entries:Material Type : HALB, ROH, FERTPlant: 3310Material : <Material numbers of relevant Materials, for this scope item FG0513 is assumed>Deselect Background Processing and select option Explode Multilevel Structure (that is already preselected).Save your entries and choose Back.Choose Execute, which displays in the Execute column, and the status light for the Selection row turns green. | The selection is executed. |  |
| 6 | Create Cost Estimates | From the Costing row, choose the Change Parameter button. On the Costing Run: Cost Estimate – Change Parameters view, deselect Background Processing indicator and then choose Save.Choose Back.Choose Execute, which displays in the Execute column and the status light for the Costing row turns green. | Costing Run is executed. |  |
| 7 | Create Cost Estimates | From the menu, in case the Edit is not visible directly, choose Menu > Edit > Costing Results .If the status light for this row is red, review the Costing levels report. Correct errors in the report. To re-run the costing (if necessary), repeat steps for Selection Struct. Explosion and Costing Rows. | Costing Run is executed. |  |
| 8 | Create Cost Estimates | On the Analysis row, choose the Change Parameter button. Select SAP&11 for the parameter setting and then select Choose. On the Costing Run: Analysis - Change Parameters view, deselect Background Processing checkbox and then choose Save.Choose Back.Choose Execute, which displays in the Execute column.Choose Back and confirm the message with yes to leave the list. | Costing Run is executed.Note Based on the given analysis results for the cost estimations the relevant components can be checked. In case the component PK0506 is not part of the expected quantity structure, please refer to the chapter “Check Bill of Material” under preliminary steps and rerun the related steps accordingly. |  |
| 9 | Create Cost Estimates | On the Marking row, choose the Lock button.On the Price Update: Organizational Measure view, select the company code 3310 row for the appropriate ledger 0L.In the Permitted Costing Variant dialog box, enter the costing variant of PYC1 and the costing version of 01, and then choose Enter. The status light of the row turns green.Choose Back.Choose Change Parameter and deselect Test Run and Background Processing.Choose Save.Choose Back, and choose Execute. | Costing Run is executed. |  |
| 10 | Create Cost Estimates | On the Release row, choose Change Parameter and deselect Test Run and Background Processing.Choose Save.Choose Back, and choose Execute. | The current prices will be updated in the material master data.Note The new standard price cannot be updated before the first day of the validity of the costing run. For example, if costing run is valid from 01/01/<current year>, then releasing the standard price is possible on 01/01/<current year> at the earliest. |  |

### Analytics

#### Display Material Price Change Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity displays documents created by price changes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Material Price Change Documents (F6684). | The Display Material Price Change Documents screen displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:Company Code: 3310Material: RM0502Plant: 3310 | All price change documents display. |  |

#### Material Price Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This report app helps you view inventory value, new price, and flow of value change.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Material Valuations (F2680) . | The Manage Material Valuations screen displays. |  |
| 3 | Material Valuations | Make the following entries and choose the Go button:Material: FG0513 or RM0502Plant: 3310 | The Current Material Valuations view displays. |  |
| 4 | Select the Material | Select the desired line item and choose Material Price Analysis.Note For detailed information the selection fields Prices can be expanded. | The Material Price Analysis screen displays. You can enter the Period/Year and review the inventory details. |  |
| 5 | Report | The report containing the movement price, total stock, and other information related to the material displays. |  |  |

#### Execute Costing Run Comparision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Costing Run Comparison (S_ALR_87099932). | The Analyze/Compare Material Cost Estimates view displays. |  |
| 3 | Execute Report | Make the following entries and choose the Execute button:Costing run 1: <61W_XX>Note Should be the same costing run ID which had been created within the previous step of this script "Periodic Cost Estimation Based on Changed Product Cost Related Master Data Changes".Costing run 2: <costing run ID from initial standard costing>Note Costing run ID which had been used for the initial cost estimation based on the Business Condition, please refer to chapter Prerequisites part Business Condition and scope item BNU - Create Costing Run. | The screen presents a comparison of the selected costing runs. |  |

### Quantity Structure Re-Exchanges (Optional)

The initial supplier A resolved the quality issues with component PK0505, and you are able to use again the original material/component PK0505 in production for semifinished Material FG0513. You prefer using PK0505 only because it causes less costs if you are using material from supplier A.

This process step shows you how to change bill of material with change master to track this change and stay compliant.

|  |
| --- |
| Note If you want to execute this scope item more than once, you must reset the master data to the initial situation. You can use this section to reset the BOM (i.e. change back from component PK0506 to PK0505) |

#### Periodic BOM Re-Exchange with Change Master (Optional)

##### Create Change Master (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a new change master.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Change Master (CC01). | The Create Change Master app launches. |  |
| 3 | Enter Change Number | On the Create Change Master: Initial Screen, enter data as provided in the following example and press Enter.Change Number: 61W_XX (XX change be any number)Leave default values in other fields. |  |  |
| 4 | Enter Change Master Data | On the Create Change Master: Change Header screen, enter data as provided in the following example and press Enter.In the field beside Change Number: Change Master for BOM FG0513.Valid From:<Today + 1 month>Change no. status: 01 Active |  |  |
| 5 | Select Checkboxes for Bill of Material | On the Create Change Master: Object Types screen, from Object types table, Bill of Material row, select the following checkboxes:Actv.ObjectMgtRec |  |  |
| 6 | Choose Save | Choose Save. | The Change Master is created. |  |

##### Change to Original Component in the Material BOM (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

For example, supplier A resolved the quality issues, and you are able to use again the original material/component PK0505 in production FG0513. You prefer using PK0505 only because it costs less if you are using material from supplier A.

This process step shows you how to change bill of material with change master to track this change and stay compliant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Bill Of Material - Create, change & display BOMs (F1813). |  |  |
| 3 | Search for the BOM to be Changed | On the Maintain Bill of Material screen, make the following entries and choose Go:Material: FG0513Plant: 3310BOM Usage: Production | The BOM to be changed displays. |  |
| 4 | Choose the BOM to be Changed | Choose the correct BOM to be changed. |  |  |
| 5 | Edit the Bill of Materials | Select Edit with Change Number from the Edit dropdown list. |  |  |
| 6 | Assign Change Master | On the Edit with Change Number screen, make the following entries and choose Edit with Change Number:Use Exisiting Change Number: YESChange Number: Select the Change Master 61W_XX from the list (the change master created in previous step) | The Assign Change Number dialog box displays. |  |
| 7 | Change BOM Item | On the Components tab, change the value of the BOM Item Number 0020 line to PK0505. |  |  |
| 8 | Choose Save | Choose Save. | The BOM is changed. |  |
| 9 | Select a Change Number | On the Maintain Bill of Material Screen you can review the changes.If you select a specific date in Selected Date you will see the valid Bill of Materials for the chosen date.If you select one of the available change numbers from the Select Change Number Field, you see the changes relevant to this change number. The Selected Date is filled according to the Change Master Date. | The changed component will only display when the relevant Change Number is selected. |  |

##### Set Change Master Status to Inactive (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to set the Change Master Status to Inactive so that this specific Change Master cannot be used anymore for managing further changes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a BOM Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Change Master (CC02). | The Change Change Master app launches. |  |
| 3 | Search for Change Number to be changed | On the Change Master: Initial Screen, make entries similar to the following example and press Enter.Change Number: 61W_XX (Change master created in previous step) | The relevant Change Masters are displayed. |  |
| 4 | Set Change Master Status | In the Change No.Status field, select 02-Inactive. | The Change Master Status is set to Inactive; then the Change Master can't be used anymore. |  |
| 5 | Choose Save | Choose Save. | The Change Master is saved. |  |

##### Manually Create Production Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a production order for the finished material FG0513 and check that the original material PK0505 is adopted as component.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the Production Supervisor - Discrete Manufacturing | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Production Order (CO01). | The Production Order Create: Initial Screen displays. |  |
| 3 | Enter the Order Information | Make the following entries and press Enter:Material: FG0513Production Plant: 3310Order Type: YBM1 |  |  |
| 4 | Enter the Order Details | Make the following entries and press Enter:Total Qty: 10End: <Today's date + 6 weeks> | The Start date is calculated and the date falls after the valid-from date of change master. |  |
| 5 | Check Component | Choose Components.Note Confirm the information pop up with Continue. If you want to avoid the pop up you need to post intial stock for the components. | Component PK0505 displays instead of PK0506. |  |
| 6 | Save | Choose Save and make a note of your production order number. |  |  |

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
- related-to :: [[06-management-accounting/crear-ejecucion-del-calculo-del-coste-mds-bnu-678]]
- related-to :: [[06-management-accounting/criar-execucao-de-calculo-de-custos-mds-bnu-680]]
- related-to :: [[06-management-accounting/kalkulationslauf-anlegen-sds-bnu-676]]
- related-to :: [[06-management-accounting/master-data-script-create-costing-run-mds-bnu-677]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/61W_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 60,604 chars in the whole document
