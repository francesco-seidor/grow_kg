---
id: 12-production-and-manufacturing/test-script-sap-s-4hana-cloud-public-edition-predictive-material-and-r
title: Test Script SAP S/4HANA Cloud Public Edition - Predictive Material and Resource Planning (4B5_AE) (4B5_S4CLD2608_BPD_EN_AE)
description: "SAP test script for scope item 4B5 (AE, 2608): predictive MRP simulations, PIR release, plus supplier and production-line constraint use cases."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/mrp-and-predictive-mrp]
aliases: [4B5_S4CLD2608_BPD_EN_AE]
keywords: [Material Requirements Planning and Predictive MRP, predictive material and resource planning, pmrp simulation, planned independent requirements, simulation scheduling, flexible constraints, supplier constraints, production line constraints, test script, supplier collaboration]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4B5_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1018
topic: 12-production-and-manufacturing/mrp-and-predictive-mrp
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Predictive Material and Resource Planning (4B5_AE) (4B5_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4B5_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Material Requirements Planning and Predictive MRP** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Predictive Material and Resource Planning (4B5_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232854944)

[2 Prerequisites 4](#_Toc232854945)

[2.1 System Access 4](#_Toc232854946)

[2.2 Roles 4](#_Toc232854947)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232854948)

[2.4 Business Conditions 8](#_Toc232854949)

[2.5 Preliminary Steps 8](#_Toc232854950)

[2.5.1 Create Master Data 8](#_Toc232854951)

[2.5.1.1 Create Material Master Data 8](#_Toc232854952)

[2.5.1.2 Create Bill of Material Structure 9](#_Toc232854953)

[2.5.1.3 Create Routing 9](#_Toc232854954)

[2.5.1.4 Create Production Version 10](#_Toc232854955)

[2.5.1.5 Create Purchasing Info Records 11](#_Toc232854956)

[2.5.2 Check Available Capacity in Work Center 13](#_Toc232854957)

[3 Overview Table 15](#_Toc232854958)

[4 Test Procedures 17](#_Toc232854959)

[4.1 Main Scenario 17](#_Toc232854960)

[4.1.1 Create Planned Independent Requirements 17](#_Toc232854961)

[4.1.2 Schedule pMRP Simulation Creation 19](#_Toc232854962)

[4.1.3 Process pMRP Simulations 21](#_Toc232854963)

[4.1.4 Check Planned Independent Requirements 24](#_Toc232854964)

[4.1.5 pMRP with Supplier Collaboration (Optional) 25](#_Toc232854965)

[4.1.5.1 Download Component Data from pMRP Simulation 26](#_Toc232854966)

[4.1.5.2 Create Price Request from Suppliers 26](#_Toc232854967)

[4.2 Use Cases (Optional) 27](#_Toc232854968)

[4.2.1 Use-Case A： Dealing with External Constraints for Supplier(s) 27](#_Toc232854969)

[4.2.1.1 Variant 1: Flexible Contraints for Multiple Suppliers 27](#_Toc232854970)

[4.2.1.1.1 Define Flexible Contraints for Multiple Suppliers 27](#_Toc232854971)

[4.2.1.1.2 Copy Simulation from Main Scenario 29](#_Toc232854972)

[4.2.1.1.3 Process pMRP Simulation 30](#_Toc232854973)

[4.2.1.1.4 Update Flexible Constraints 32](#_Toc232854974)

[4.2.1.1.5 Reprocess the pMRP Simulation 33](#_Toc232854975)

[4.2.1.2 Variant 2: Flexible Constraints for Multiple Materials of a Single Supplier 33](#_Toc232854976)

[4.2.1.2.1 Define Flexible Contraints for Multiple Materials 33](#_Toc232854977)

[4.2.1.2.2 Copy Simulation from Main Scenario 35](#_Toc232854978)

[4.2.1.2.3 Process pMRP Simulation 36](#_Toc232854979)

[4.2.2 Use-Case B: Dealing with Internal Constraints for Production lines 37](#_Toc232854980)

[4.2.2.1 Define Constraints for Production Line 37](#_Toc232854981)

[4.2.2.2 Copy Simulation from Main Scenario 39](#_Toc232854982)

[4.2.2.3 Process pMRP Simulation 40](#_Toc232854983)

[4.2.2.4 Update the Production Line Constraints 41](#_Toc232854984)

[4.2.2.5 Reprocess the pMRP Simulation 42](#_Toc232854985)

[5 Appendix 43](#_Toc232854986)

[5.1 Succeeding Processes 43](#_Toc232854987)

## Purpose

Overview

Predictive Material and Resource Planning (pMRP) enables you to create, schedule, and evaluate pMRP simulations that support you in making informed decisions for your production planning.

You can create and schedule pMRP simulations with your top-level demands and resource constraints. During the simulation creation, the system creates simplified data, based on your forecasted product demand and master data for material- and resource-planning, which is used as reference data in pMRP.

After the creation, you can process and evaluate your simulation. The number of capacity issues and a delivery performance KPI are constantly updated to enable you to compare your simulated changes so that you can assess the impact of changes to your simulation.

Finally, after you decide which simulation best fits your production plan, you can take over the resulting component demand and release it to your operational data as planned independent requirements.

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
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Production Engineer - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC | Production Engineering - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | FG1_CP | CP-FG1, Shaft with Rolling Bearings |  |
| Material | SG1_CP | CP-SG1, Shaft |  |
| Material | FG3_CP | CP-FG3, Shaft with Rolling Bearings | Manually create it in section Preliminary Steps. |
| Material | SG3_CP | CP-SG3, Shaft | Manually create it in section Preliminary Steps. |
| Material | RM1_CP | CP-RM1, Steel |  |
| Material | RM2_CP | CP-RM2, Rolling Bearing |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |

Bill of Material Structure

This overview shows the bill of material structure and the usage of each component if you have activated all optional enhancements.

| Material | Level | Material Type | Unit | Characteristics of Material | Comment |
| --- | --- | --- | --- | --- | --- |
| FG1_CP | 0 | FERT | PC | Finished Good |  |
| SG1_CP | 1 | SEMI | PC | Semi-finished Goods |  |
| RM1_CP | 2 | RAW | PC | Raw material, component for SG1_CP |  |
| RM2_CP | 1 | RAW | PC | Raw material |  |
| FG3_CP | 0 | FERT | PC | Finished Good | Manually create it in section Preliminary Steps. |
| SG3_CP | 1 | SEMI | PC | Semi-finished Goods | Manually create it in section Preliminary Steps. |
| RM1_CP | 2 | RAW | PC | Raw material, component for SG3_CP |  |
| RM2_CP | 1 | RAW | PC | Raw material |  |

Work Center

This overview shows work centers used for this scenario.

| Work Center | Description |
| --- | --- |
| TURNING1 | CP-WC1, Turning 1 |
| TURNING2 | CP-WC2, Turning 2 |
| TURNING9 | CP-WC2 (Alt), Turning 9 |
| DRILING | CP-WC3, Drilling |
| FINICLN | CP-WC4, FINISHING AND CLEANING |
| ASSPKG | CP-WC5, ASSEMBLY AND PACKAGING |
| ASSPKG9 | CP-WC5 (Alt), ASSEMBLY AND PACKAGING 9 |

Routing

This overview shows Routing for Semi-finished goods and Finished goods.

| Material | Operation | Description | Work Center | Comment |
| --- | --- | --- | --- | --- |
| SG1_CP | 0010 | Turning Machine 1 | TURNING1 |  |
| SG1_CP | 0020 | Turning Machine 2 | TURNING2 |  |
| SG1_CP | 0030 | Drilling machine | DRILING |  |
| SG1_CP | 0040 | Finishing | FINICLN |  |
| SG1_CP | 0050 | Clearing | FINICLN |  |
| FG1_CP | 0010 | Assembly | ASSPKG |  |
| FG1_CP | 0020 | Finish and clean | FINICLN |  |
| SG3_CP | 0010 | Turning Machine 1 | TURNING1 | Manually create it in section Preliminary Steps. |
| SG3_CP | 0020 | Turning Machine 2 | TURNING2 | Manually create it in section Preliminary Steps. |
| SG3_CP | 0030 | Drilling machine | DRILING | Manually create it in section Preliminary Steps. |
| SG3_CP | 0040 | Finishing | FINICLN | Manually create it in section Preliminary Steps. |
| FG3_CP | 0010 | Assembly | ASSPKG | Manually create it in section Preliminary Steps. |
| FG3_CP | 0020 | Finish and clean | FINICLN | Manually create it in section Preliminary Steps. |

Available Capacity for Work Center

This overview shows predefined shifts.

| Shift | Start time | End time | Length of Break |
| --- | --- | --- | --- |
| YS1, Early Shift | 06:00:00 | 14:00:00 | 00:30:00 |
| YS2, Late Shift | 14:00:00 | 22:00:00 | 00:30:00 |
| YS3, Night Shift | 22:00:00 | 06:00:00 | 00:30:00 |

For more information about creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BLD | Create Production Version - MDS |

### Business Conditions

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation | You have completed the step described in the BEG test script. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described BNZ master data script. Posting Period is up-to-date. |

### Preliminary Steps

#### Create Master Data

This chapter shows you how to create essential master data in our business scenario.

##### Create Material Master Data

This process step shows you how to create new material master data.

Refer to Create Product Master of type "Finished Good" - MDS (BNT) master data script for the following two new materials FG3_CP and SG3_CP, copied from FG1_CP and SG1_CP .

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | FG3_CP | CP-FG3, Shaft with Rolling Bearings | Copied from material FG1_CP |
| Material | SG3_CP | CP-SG3, Shaft | Copied from material SG1_CPIn the MRP3 view, maintain the following entries:Period Indicator: WStrategy Group: 70Mixed MRP: 1 |

##### Create Bill of Material Structure

This process step shows you how to create bill of material (BOM) structure.

Refer to Create Material BOM for Production and Sales - MDS (BNK) master data script to create following BOM structure for new materials FG3_CP and SG3_CP.

| Material | Item | Material Type | Quantity | Unit | Characteristics of Material |
| --- | --- | --- | --- | --- | --- |
| FG3_CP | Head | FERT | 1 | PC | Finished Good |
| SG3_CP | 0010 | SEMI | 1 | PC | Semi-finished Goods |
| RM2_CP | 0020 | RAW | 2 | PC | Raw material |

| Material | Item | Material Type | Quantity | Unit | Characteristics of Material |
| --- | --- | --- | --- | --- | --- |
| SG3_CP | Head | SEMI | 1 | PC | Semi-finished Goods |
| RM1_CP | 0010 | RAW | 1 | PC | Raw material |

##### Create Routing

This process step shows you how to create routing for the material.

Refer to Create Routing - MDS (BNL) master data script to create following operations for new materialsFG3_CP and SG3_CP, please copy from existing materialFG1_CP& SG1_CPand make minor changes as following table shows.

| Material | Group Counter | Operation | Description | Work Center | Setup | Activity | Labor |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FG3_CP | 1 | 0010 | Assembly | ASSPKG | 15 min | 3 min | 3 min |
| FG3_CP | 1 | 0020 | Finish and clean | FINICLN | 15 min | 2 min | 2 min |
| FG3_CP | 2 | 0010 | Assembly | ASSPKG9 | 15 min | 1 min | 1 min |
| FG3_CP | 2 | 0020 | Finish and clean | FINICLN | 15 min | 2 min | 2 min |

| Material | Group Counter | Operation | Description | Work Center | Setup | Activity | Labor |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SG3_CP | 1 | 0010 | Turning Machine 1 | TURNING1 | 30 min | 5 min | 5 min |
| SG3_CP | 1 | 0020 | Turning Machine 2 | TURNING2 | 30 min | 25 min | 25 min |
| SG3_CP | 1 | 0030 | Drilling machine | DRILING | 30 min | 5 min | 5 min |
| SG3_CP | 1 | 0040 | Finishing & Clearing | FINICLN | 15 min | 2 min | 2 min |
| SG3_CP | 2 | 0010 | Turning Machine 1 | TURNING1 | 30 min | 5 min | 5 min |
| SG3_CP | 2 | 0020 | Turning Machine 9 | TURNING9 | 30 min | 10 min | 10 min |
| SG3_CP | 2 | 0030 | Drilling machine | DRILING | 30 min | 5 min | 5 min |
| SG3_CP | 2 | 0040 | Finishing & Clearing | FINICLN | 15 min | 2 min | 2 min |

##### Create Production Version

This process step shows you how to create production version for new materials.

Refer to Create Production Version - MDS (BLD) master data script to create the following production versions for new materials FG3_CP and SG3_CP. Copy from existing materials FG1_CP and SG1_CP, and make minor changes as the following table shows.

|  |
| --- |
| Note If you need to test Use-Case B: Dealing with Internal Constraints for Production Lines, make sure to maintain the production line field during production version creation. |

| Material | Production Version | Production Version Text | Task Listy Type | Group Counter | Alternative BOM | BOM Usage |
| --- | --- | --- | --- | --- | --- | --- |
| FG3_CP | 0001 | Production Version 001 | Routing | 1 | 1 | 1 |
| FG3_CP | 0002 | Production Version 002 | Routing | 2 | 1 | 1 |
| SG3_CP | 0001 | Production Version 001 | Routing | 1 | 1 | 1 |
| SG3_CP | 0002 | Production Version 002 | Routing | 2 | 1 | 1 |

##### Create Purchasing Info Records

Purpose

This process step shows you how to create info records for raw materials.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records (F1982) screen displays. |  |
| 3 | Search Purchasing Info Record | Search the info record by following filters.Material: RM1_CPSupplier: 33300001; 33300002If the info records for both suppliers exist, then note down the info record number and skip the following steps.If no such info records, then proceed to create it. |  |  |
| 4 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record screen displays. |  |
| 5 | Enter Header Data | Make the following entries:Purchasing Info Record Category: StantardSupplier: 33300001Material: RM1_CPPurchasing Organization: 3310Material Group: L002Plant: 3310Purchasing Group: 001 | Header data is added. |  |
| 6 | Enter General Information | Make the following entries:Salesperson: <Sales Name>Supplier Telephone Number: <0172595959> | General Information is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: 2Order Unit: PCStandard Order Quantity: 10Goods-Receipt-Based Invoice Verification: unmarked | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose the Create icon. Enter the following data:Valid From: <Today’s Date>Amount: 1Currency: AEDPricing Unit: 1Valid To: <12/31/9999>Choose the Apply icon. | Your Condition Data is added |  |
| 9 | Save Your Data | Choose Save. | A purchasing info record is saved.Note down the purchasing info record number. |  |
| 10 | Create Another Info Record | Repeat step 4 - 9 to create purchasing info records for another supplier with same parameters and make some minor changes.In step 5, make change for the following entries:Supplier: 33300002In step 7, make change for the following entries:Delivery Time in Days: 1In step 8, make change for the following entries:Amount: 1.5 | A new purchasing info record is saved. |  |
| 11 | Create Further Info Records for Raw Materials ( This is an optional step for the use case ) | Repeat the steps 4 – 9 for the following supplier and material:Supplier: 33300002Material: RM2_CP |  |  |

#### Check Available Capacity in Work Center

Purpose

In the Best Practice pre-delivered contents, standard available capacity is applied to the work centers, and no shifts assigned initially. In case these values have been adjusted during test, we recommend that you have a check to have better understanding of current available capacity for work center TURNING1, TURNING2,TURNING9, DRILING, FINICLN, ASSPKG, and ASSPKG9.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Work Center (CR02). |  |  |
| 3 | Enter Plant and Work Center | On the Change Work Center (CR02) screen, make the following entries, and choose Enter:Plant: 3310Work Center: <Work Center> |  |  |
| 4 | Choose Capacity Category 001 | Choose Capacities tab, you can find there are two capacity categories defined: 001 and 002.Double-click capacity category 001. | The Change Work Center: Capacity Overview screen displays. |  |
| 5 | Check Standard Available Capacity | On the Change Work Center: Capacity Overview screen for capacity 001, check standard available capacity. Following values are pre-set in this test scenario:Start time: 07:00:00End time: 16:00:00Length of break: 01:00:00Capacity Utilization: 100No. Ind. Capacities: 1For test purpose, we recommend using the same values as above. |  |  |
| 6 | Check Intervals and Shifts | Choose Intervals and Shifts in the upper left corner.On the Change Work Center Capacity: Header screen for capacity 001, available shifts are listed in the table at the bottom of the page. We recommend deleting any additional shifts effective within next 6 weeks.Choose any line you want to delete, then choose Delete line icon in the upper right.Choose Back twice to screen Change Work Center Capacity: Header. |  |  |
| 7 | Choose Capacity Category 002 | Under Capacities tab, double-click capacity category 002. | The Change Work Center: Capacity Overview screen displays. |  |
| 8 | Check Default Settings for Capacity Category 002 | Repeat step #5 and #6 for category 002. |  |  |
| 9 | Save | Choose Save. | Work center XXX in plant 3310 was changed. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Planned Independent Requirements](#unique_15) [page ] 17 | Production Planner | Maintain PIRs (F3445) | Independent Requirements for top level materials are created. |
| [Schedule pMRP Simulation Creation](#unique_16) [page ] 19 | Production Planner | Schedule pMRP Simulation Creation (F3968) | pMRP Simulation is created for top level materials. |
| [Process pMRP Simulations](#unique_17) [page ] 21 | Production Planner | Process pMRP Simulations (F3934) | Process PMRP Simulations to reduce capacity issues and then release it. |
| [Check Planned Independent Requirements](#unique_18) [page ] 24 | Production Planner | Maintain PIRs (F3445) | Check the updated independent requirements for top level materials. |
| [pMRP with Supplier Collaboration (Optional)](#unique_19) [page ] 25 |  |  |  |
| [Download Component Data from pMRP Simulation](#unique_20) [page ] 26 | Production Planner | Process pMRP Simulations (F3934) | The excel file is downloaded. |
| [Create Price Request from Suppliers](#unique_21) [page ] 26 |  |  |  |
| [Use Cases (Optional)](#unique_22) [page ] 27 |  |  |  |
| [Define Flexible Contraints for Multiple Suppliers](#unique_23) [page ] 27 | Production Planner | Define Flexible Constraints (F4449) | The constraints are saved. |
| [Copy Simulation from Main Scenario](#unique_24) [page ] 29 | Production Planner | Schedule pMRP Simulation Creation (F3968) |  |
| [Process pMRP Simulation](#unique_25) [page ] 30 | Production Planner | Process pMRP Simulations (F3934) |  |
| [Update Flexible Constraints](#unique_26) [page ] 32 | Production Planner | Define Flexible Constraints (F4449) |  |
| [Reprocess the pMRP Simulation](#unique_27) [page ] 33 |  |  |  |
| [Define Flexible Contraints for Multiple Materials](#unique_28) [page ] 33 | Production Planner | Define Flexible Constraints (F4449) | The constraints are saved. |
| [Copy Simulation from Main Scenario](#unique_29) [page ] 35 | Production Planner | Schedule pMRP Simulation Creation (F3968) |  |
| [Process pMRP Simulation](#unique_30) [page ] 36 | Production Planner | Process pMRP Simulations (F3934) |  |
| [Define Constraints for Production Line](#unique_31) [page ] 37 | Production Planner | Define Flexible Constraints (F4449) | The constraints are saved. |
| [Copy Simulation from Main Scenario](#unique_32) [page ] 39 | Production Planner | Schedule pMRP Simulation Creation (F3968) |  |
| [Process pMRP Simulation](#unique_33) [page ] 40 | Production Planner | Process pMRP Simulations (F3934) |  |
| [Update the Production Line Constraints](#unique_34) [page ] 41 | Production Planner | Define Flexible Constraints (F4449) |  |
| [Reprocess the pMRP Simulation](#unique_35) [page ] 42 | Production Planner | Process pMRP Simulations (F3934) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

In real business scenario, customer could have incoming demand peak during a period, with the help of predictive material and resource planning, customer could evaluate the feasibility and even adjust demand accordingly by identifying bottlenecks, increasing capacity, distributing load to other sources and preproduction.

### Main Scenario

This section describes test procedures for each process step that belongs to this scope item.

In real business scenario, customer could have incoming demand peak during a period, with the help of predictive material and resource planning, customer could evaluate the feasibility and even adjust demand accordingly by identifying bottlenecks, increasing capacity, distributing load to other sources and preproduction.

Note: In any case, the main scenario (Chapter 4) must be executed so that the simulation of the optional scenarios can also take place.

#### Create Planned Independent Requirements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use planned independent requirements to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split over time according to dates.

|  |
| --- |
| Note Instead of creating a single requirement, sometimes a requirement's plan that includes one or more planned independent requirements can be maintained for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 002 (002)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Weekly(W)Material: FG1_CP , FG3_CPVersion Active: Select all options |  |  |
| 5 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 6 | Edit PIRs | Select the filtered material items, and choose Edit in the upper-right corner.On the screen, set Version Active to Yes and enter quantities per period, for example:In the upcoming several weeks, enter the following values for PIR:Week 1 (current week + 4 weeks): <75 PC>.Week 2 (current week + 5 weeks): <75 PC>.Week 3 (current week + 6 weeks): <75 PC>.Week 4 (current week + 7 weeks): <75 PC>.Week 5 (current week + 8 weeks): <75 PC>.Week 6 (current week + 9 weeks): <75 PC>.Week 7 (current week + 10 weeks): <75 PC>.Week 8 (current week +11 weeks): <75 PC>. | Maintain PIRs for all other weeks as zero. |  |
| 7 | Save PIRs Draft | Choose Save in the bottom right corner of the screen. | The PIRs are saved. |  |

#### Schedule pMRP Simulation Creation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create pMRP simulations.

|  |
| --- |
| Note Besides creating a pMRP simulation using top level materials, there are two other job templates for creating pMRP simulations: Creation of pMRP Data via Workcenter and Creation of pMRP Data via Components. This test script focuses only on creating pMRP simulations using top level materials. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule pMRP Simulation Creation (F3968). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job screen displays. |  |
| 4 | Enter Job Details | In the 1. Template Selection area, enter the following entries:Job Template: <Creation of pMRP Data via Top Level Materials>Job Name: <Creation of pMRP Data via Top Level Materials> |  |  |
| 5 | Define Recurrence Pattern | Choose Step 2.In the 2. Scheduling Option area, maintain the following entry:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries and choose OK.Start Immediately: <select>Recurrence Pattern: Single Run | The Scheduling Information screen displays. |  |
| 6 | Enter Selection Criteria | Choose Step 3.In the Parameter Section area, make the following entries:ID for Reference Data: 4B5_PMRP_<MMDD>Bucket Category: WStart Date of Reference: <Today’s date + 21 days>End Date of Reference: <Today’s date + 16 weeks>Simulation ID: 4B5_PMRP_SIMU_<MMDD>Simulation Description: 4B5_PMRP_SIMU_<MMDD>Delete Existing pMRP Data: <blank>For the Object Selection sub-area:Plant: 3310Material: FG1_CP , FG3_CPMRP Controller: 002For the Document Data sub-area:Opening Stock: <blank>Resource Overload Tolerance: for example, <10> | MMDD is today’s date, for example, if the date is August 1st, then MMDD = 0801.Note The parameters in Object Selection determine the size or scope of pMRP simulation, which is to filter subset products from all relevant products.The parameters in Document Data determine which planning data is meaningful for all active products during pMRP simulation. The parameters are different from those in Object Selection. |  |
| 8 | Schedule a New Job | Choose Check.If there are no error messages, choose Schedule.A new job is created and displayed in the Application Jobs table. | Confirm that the application job finishes with no errors.If error messages are displayed, such as: Reference ID/Simulation ID XXX already exists and cannot be created.If you want to keep existing pMRP data, use a new reference ID or simulation ID.If you want to delete existing pMRP data, select the Delete Existing pMRP Data field. You can then ignore these errors as warning messages. |  |

#### Process pMRP Simulations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to process the created pMRP simulations to handle bottlenecks and constraints.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process pMRP Simulations (F3934). | The Process pMRP Simulations screen displays. |  |
| 3 | Filter the Simulation | On the Process pMRP Simulations screen, filter the simulation with the reference ID you just created and choose Go.Reference Data : 4B5_PMRP_<MMDD> | The simulation displays. |  |
| 4 | Refresh Reference Data (Optional) | When you update demands, stock settings or constraints, refresh reference data instead of recreating pMRP simulations.Select the checkbox of the filtered simulation, and choose Refresh Reference Data in the upper-right corner.In the Refresh Reference Data dialog, make the following entries and choose Refresh.Update Demands and Stock: YesChange Demand or Stock Settings: YesUpdate Constraints: Yes | The message Reference data has been updated successfully! is displayed. |  |
| 5 | Copy the Simulation | Select the checkbox of the filtered simulation, and choose Copy in the upper right corner.On the Copy screen, make the following entries and choose Copy.Copy from Current Simulation: XNew Simulation ID: 4B5_PMRP_SIMU_<MMDD>_CNew Simulation Description: 4B5_PMRP_SIMU_<MMDD>_C | The system shows Simulation Copied.You can repeat this step to create several copies of one pMRP Simulation to figure out the best adjusted simulation. |  |
| 6 | Check the Copied Simulation | On the Process pMRP Simulations screen, choose the row of the new copied simulation with simulation ID: 4B5_PMRP_SIMU_<MMDD>_C | The Demand Plan Simulation screen displays. |  |
| 7 | Check the Demand-Plan Simulation | On the Demand Plan Simulation screen, you can check the Capacity Issues, Delivery Performance, and Violated Constraints.You can check the demand plan simulation quantities for materials in each period, you can switch the displayed mode, for example:Simulation Table Selection: Reference /Simulation | In our scenario, we only focus on reducing the capacity issue from top-level material FG3_CP, and make a comparison with another product FG1_CP.If there is no capacity issue or violated constraints, skip step 8 - 16. |  |
| 8 | Check Issue Worklist | At the top of screen, choose the Capacity Issues quantity, the Capacity Issues page displays.Choose Show in Issue List, the Issue List screen displays.In the Issues area, you could see Issue Category, Affected Objects, Affected Weeks, Affected Demands, Impact Score, Impact Caused By and Impact Cause.You could choose Clear Filter icon after Filtered by: Capacity Issues, then you could get the overall issue lists, including Violated Constraints in our case.Choose one Capacity Overload issue, choose Disregard Capacity Issues. On the pop-up Disregard Capacity Issues screen, choose OK.Choose Demand Plan Simulation on the top of screen and navigate back. | The selected issues are disregarded in this simulation.And the capacity issue quantities are reduced. |  |
| 9 | Check Capacity Plan Simulation | On the Demand Plan Simulation screen, choose the <75> (simulation quantity) in the red box for FG3_CP, the Inspector area displays the relevant capacity overload issues.In the Issues area, choose Capacity Plan Simulation.On the Capacity Plan Simulation screen, you can check the Demand/Remaining Capcity in Hours in table view by default.Choose Show Work Center Overview near the top right corner of Capacity Plan Simulation screen, then it shows in graphic view.Check the overload demand in red for work center whose remaining capacity is less than zero, it indicates the capacity issue. | Continue to reduce the capacity issues or violated constraints in step 10-17.Note When overload demand shows a negative value without red highlighting, it means the resource overload tolerance has been applied, and the ratio of overload demand (H) to 40H is less than the resource overload tolerance percentage. |  |
| 10 | Shift Demand | Choose the first demand in red for the work center, for example, TURNING2.In the Top-Level Materials area, navigate to FG3_CP for the latest week, and choose Shift Demand on the right.On the Shift Top-Level Demand screen, maintain the following entry:Shift Demand To: <the earliest week>Choose Adopt Proposal, the Quantity is automatically updated with the Proposed Quantity.Choose Apply. | The capacity issues are reduced.You can choose Undo or Redo icon to withdraw or resume your changes of simulation.You can choose Show Change History icon to review all your changes in the Global History area. |  |
| 11 | Check Multi-Level Material Simulation | Choose the next demand in red for a work center, for example, TURNING2.In the Top-Level Materials area, navigate to FG3_CP, and choose Multi-Level Material Simulation. | The Multi-Level Material Simulation screen displays. |  |
| 12 | Change Source of Supply | On the Multi-Level Material Simulation screen, you could see simulation details for BOM components in Bill of Material area.Choose the Issues for semi-finished goods SG3_CP, and then choose Change Source of Supply to distribute demand into different production versions to balance workload.On the Change Source of Supply screen, choose Adopt Proposal, the Quantity Distribution for two production versions are automatically updated with the Proposed Distribution. Choose Apply. | The capacity issues are reduced. |  |
| 13 | Pull in Quantity | Repeat step 11.Choose the Issues for semi-finished goods SG3_CP, then you could choose Pull in Quantity to distribute partial quantity to reduce workload.On the Pull in Quantity screen, choose Adopt Proposal, the Capacity Distribution for the previous period is automatically updated with the Proposed Distribution, choose Apply. | The capacity issues are reduced. |  |
| 14 | Reduce Issues | Continue to reduce the capacity issues by any approach mentioned in step 9-13. |  |  |
| 15 | Check Simulation Component | Choose Simulation Views at the top and choose Simulation Components.On the Simulation Components screen, you could see simulation quantities for both head materials and components. You can change display mode from Materials to Supply. | The Simulation Components screen displays. |  |
| 16 | Check Simulation Summary | Choose Simulation Summary at the top.On the Simulation Summary screen, you could check Change in Demand, Change in Capacity, Preproduction or Early Procurement, Change of Source of Supply, Unresolved Issues, and Disregarded Capacity Issues. | The Simulation Summary screen displays. |  |
| 17 | Check Demand Plan Simulation Again | Choose Simulation Views at the top and navigate back to Demand Plan Simulation.Compare the simulation quantity for materials FG1_CP and FG3_CP. | The Demand Plan Simulation screen displays. |  |
| 18 | Release Simulation | Choose Navigation Menu icon at the top left and navigate to Process pMRP Simulations.On the Process pMRP Simulations screen, filter the simulation with the reference ID and choose Go.Reference Data : 4B5_PMRP_<MMDD>Choose Release for the copied simulation with less capacity issues.On the Release screen, make following entries and choose Release.Create PIRs for Demand-Driven MRP Components: unmarkedCreate PIRs for Top-Level Materials: <X>Create PIRs for Subassembly Components: <X>Requirement Version for Top-Level Materials : 00 REQUIREMENTS PLANVersion Active for Top-Level Materials: YesRequirement Version for Subassembly Components: 00 REQUIREMENTS PLANVersion Active for Subassembly Components: Yes | The simulation status is changed into Released. |  |

#### Check Planned Independent Requirements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the adjusted PIRs for top level materials FG1_CP , FG3_CP, and subassembly material, SG3_CP. They are adjusted to ensure less capacity issues.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Material: FG1_CP , FG3_CP, SG3_CPPlant: 3310Period Indicator: Weekly (W)Version Active: Select all options |  |  |
| 5 | Filter Result | Choose Go to execute. | The material item displays. |  |
| 6 | Check PIRs | Select the filtered material items whose last modified date is today, and choose Edit in the upper-right corner.On the screen, check the generated PIRs for FG1_CP , FG3_CP, and SG3_CP. | The PIRs for top level materials are updated into requirement plan version 00. |  |

#### pMRP with Supplier Collaboration (Optional)

Purpose

This chapter shows you how to leverage pMRP simulation for components and help them find suppliers, it is an extended story line with procurement.

In real business, the planner may have no knowledge about the suppliers and prices for his desired component, he can first download the component data from the pMRP simulation, and then follow Request for Price (1XF) scope item to request suppliers for price quotation in.

##### Download Component Data from pMRP Simulation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to download necessary data from the pMRP Component view.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process pMRP Simulations (F3934). | The Process pMRP Simulations screen displays. |  |
| 3 | Filter the Simulation | On the Process pMRP Simulations screen, filter the simulation with the reference ID you just created and choose Go.Reference Data : 4B5_PMRP_<MMDD>_2Choose the row of the filtered simulation and navigate to Demand Plan Simulation screen. | The Demand Plan Simulation screen displays. |  |
| 4 | Navigate to Simulation Components | Choose Simulation Views at the top and choose Simulation Components.On the Simulation Components screen, you could see simulation quantities for both head materials and components. | The Simulation Components screen displays. |  |
| 5 | Download Components Data | Choose Download to Excel File icon. | The excel file is downloaded. |  |

##### Create Price Request from Suppliers

Please execute the following steps in Request for Price (1XF) scope item to find suppliers for our components without concrete suppliers, for example, RM2_CP.

- Create Price Request

Please use the following entries to create price request in item tab in Manage RFQ app.

Material: RM2_CP, Plant: 3310, Requested Quantity: <quantities in excel>, Delivery Data: <Monday of the week in excel>

- Create Supplier Quotation

Please maintain different net order prices for two bidders.

- Display Supplier Quotation (Optional)
- Compare and Award Supplier Quotation
- Create Follow-on Documents

### Use Cases (Optional)

The following examples illustrate possible business cases, which consider a higher differentiation within the process design. Within pMRP different restrictions can be repre-sented, which are considered within the simulation. These are examined in more detail below.The process can be performed again with the existing master data of the main scenario.

Please keep in mind that individual scenarios can overlap, which is not a problem - but makes it difficult to understand. If a use case is to be considered separately from anoth-er, it is recommended to delete the generated data. The deletion is done using the same Fiori apps as the creation!

#### Use-Case A： Dealing with External Constraints for Supplier(s)

##### Variant 1: Flexible Contraints for Multiple Suppliers

###### Define Flexible Contraints for Multiple Suppliers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Suppose we have 2 suppliers whose material goes into our products. However, these suppliers can only supply us in limited quantities for a specific period. During the planning phase, we need to ensure the planned requirements and the associated production do not violate supplier constraints.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Define Flexible Constraints (F4449). | The Define Flexible Constraints screen displays. |  |
| 3 | Filter Material and Create a Constraint Object | On the Define Flexible Constraints screen, make the follwing entries and choose GoPlant: 3310Material: RM1_CPIf no existing constrains, choose Add, make the following entries and choose OK:Plant: 3310Constraint Scope: Single MaterialMaterial: RM1_CP | If the constrains for RM1_CP already exist, choose the row of filtered material constraint. |  |
| 4 | Create Material Constraints | On the Constraint screen, make the following entriesPeriod Type: WeekConstraint Catagory: Supplier | Contraint is added.If the material constraints for both suppliers already exist, skip step 4 and proceed from step 5. |  |
| 5 | Maintain Material Constraints | Choose the row of material constraint for supplier and navigate to Material Constraint screen.Check the Basic Data and Constraint Quantities details.In the Constraint Quantities area, ensure the maximum quantity 50 is maintained from current week till next 12 weeks for supplier 33300001Week 1 (current week): <50 PC>Week 2 (current week + 1 weeks): <50 PC>Week 3 (current week + 2 weeks): <50 PC>Week 4 (current week + 3 weeks): <50 PC>Week 5 (current week + 4 weeks): <50 PC>Week 6 (current week + 5 weeks): <50 PC>Week 7 (current week + 6 weeks): <50 PC>Week 8 (current week + 7 weeks): <50 PC>Week 9 (current week + 8 weeks): <50 PC>Week 10 (current week + 9 weeks): <50 PC>Week 11 (current week + 10 weeks): <50 PC>Week 12 (current week + 11 weeks): <50 PC>If any quantity is missing, add it accordingly.Choose Edit and then choose Add. On the Add screen, make following entries and choose OK.Timeframe to Define Constraint Quantities: <the start of the week - the end of the week>Number of Periods: 1 WeekQuantities of All Selected Periods (Optional): 50 | If the constraints for some period already exist, you could choose Edit to change the value. |  |
| 6 | Save Constraints | Choose Save in the bottom right corner of the screen. | The constraints are saved. |  |
| 7 | Maintain Material Constraint for Another Suppplier | Repeat step 5 and step 6.Ensure maximum quantity 200 is maintained from current week till next 12 weeks for supplier 33300002. |  |  |

We now use the already existing simulation from chapter 4 to look at it again with the new restrictions. Therefore we will copy the simulation!

###### Copy Simulation from Main Scenario

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

We can copy the existing simulation from main scenario to look at it again with the new restrictions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule pMRP Simulation Creation (F3968). | The Process pMRP Simulations screen displays. |  |
| 3 | Copy the Existing Simulation | Mark the simulation from the main scenario and click copy. | The Creation of pMRP screen displays |  |
| 4 | Define Job Name | The system automatically suggests a job name. Choose Step 2. |  |  |
| 5 | Sheduling Options | Choose Step 3. |  |  |
| 6 | Change Reference and Simulation ID | On the parameters screen change the name of the reference data and the simulation ID to 4B5_PMRP_<MMDD>_A1 and 4B5_PMRP_SIM_<MMDD>_A1 |  |  |
| 7 | Schedule the Simulation | Choose Schedule. |  |  |

###### Process pMRP Simulation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can now see what effect a limited supply from suppliers will have on our planned production. You can also see what corrective actions the system suggests to avoid a supply bottleneck.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process pMRP Simulations (F3934). | The Process pMRP Simulations screen displays. |  |
| 3 | Filter and Enter the Simulation | On the Process pMRP Simulations screen, filter the simulation with the reference ID you just created and choose Go.Reference Data : 4B5_PMRP_<MMDD>_A1 | The Demand Plan Simulation screen displays. |  |
| 4 | Copy the Simulation | Choose the checkbox of the filtered simulation, and choose Copy in the upper right corner.On the Copy screen, make the following entires and choose Copy.Copy from Current Simulation: XNew Simulation ID: 4B5_SIM_<MMDD>_A1CNew Simulation Description: 4B5_PMRP_SIMU_<MMDD>_A1C | It shows Simulation Copied. |  |
| 5 | Check the Copied Simulation | On the Process pMRP Simulations screen, choose against the row of the newly copied simulation with simulation ID: 4B5_SIM_<MMDD>_A1C | The Demand Plan Simulation screen displays. |  |
| 6 | Mark the First Restriction Violation | On the Demand Plan Simulation screen, mark the first week in which the system detects a violated constraint. | The inspector panel displays.Constraint violation and the constraint amount are also shown in the Simulation Components view. From here you can navigate to the Multi-Level Simulation as well. |  |
| 7 | Choose Multi-Level Material Simulation | In the Inspector area, choose Multi-Level Material Simulation | The Multi-Level Material Simulation screen displays. |  |
| 8 | Mark the Raw-Material Component and Change Source of Supply | On the Multi-Level Material Simulation screen, you could see simulation details for com-ponents in Bill of Material area.Choose the Issues for raw material RM1_CP,then you choose Change Source of Supply to distribute demand into different suppliers to balance workload. |  |  |
| 9 | Change Supply Source | On the Change Source of Supply screen, choose Adopt Proposal, the Quantity Distribution for two production versions are automatically updated with the Proposed Distribution, choose Apply. | The supplier constraint issue is reduced. |  |
| 10 | Repeat the Steps | Repeat the steps 5 – 7 for all existing supply constaints issue. |  |  |

The requirements for individual weeks can be adjusted interactively - the system calculates the effects on capacity for each changed requirement - if delivery restrictions are defined, the system will also take these into account in the validation of the new planning situation.

###### Update Flexible Constraints

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Assuming after the simulation is created, the supplier informs that there will be changes in supply restrictions - this circumstance should be taken into account in planning.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Define Flexible Constraints (F4449). | The Define Flexible Constraints screen displays. |  |
| 3 | Filter Material | On the Define Flexible Constraints screen, filter the material and choose Go.Material: RM1_CP | The filtered material constraints display. |  |
| 4 | Maintain Material Constraints | Choose the row of material constraint for supplier and navigate to Material Constraint screen.Choose Edit in the upper right corner so that you can change the existing constraints.In the Constraint Quantities area, ensure the maximum quantity 40 is maintained from current week till next 7 weeks for supplier 33300001.Week 1 (current week): <40 PC>Week 2 (current week + 1 weeks): <40 PC>Week 3 (current week + 2 weeks): <40 PC>Week 4 (current week + 3 weeks): <40 PC>Week 5 (current week + 4 weeks): <40 PC>Week 6 (current week + 5 weeks): <40 PC>Week 7 (current week + 6 weeks): <40 PC> | If the constraints for some period already exist, you could choose Edit to change the value. |  |
| 5 | Save Constraints | Choose Save in the bottom right corner of the screen. | The constraints are saved. |  |

###### Reprocess the pMRP Simulation

After the constraints get updated, it could impact the existing simulation directly, refer to step Process the PMRP Simulation from Variant 1: Flexible Contraints for Multiple Suppliers to resolve new violated constraints.

After that, you could refer to step, Process pMRP Simulations to release the simulation and Check Planned Independent Requirements from Main Scenario to check updated PIRs.

##### Variant 2: Flexible Constraints for Multiple Materials of a Single Supplier

###### Define Flexible Contraints for Multiple Materials

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In real business scenario, a supplier could have a maximum capacity for his whole product portfolio. We could maintain such constraints for several material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |
| 2 | Access the App | Open Define Flexible Constraints (F4449). | The Define Flexible Constraints screen displays. |
| 3 | Filter Material and Create a Constraint Object | On the Define Flexible Constraints screen, make the following entries and choose Go:Plant: 3310Supplier: 33300002If no existing constrains, choose Add, and make the following entries:Plant: 3310Constraint Scope: Multiple MaterialsMaterial Selection By: Materials procured from a supplierSupplier: 33300002Choose OK. | Constraints are added and the detailed Constraint screen displays. |
| 4 | Create Material Constraints | On the Constraint screen, make the following entries in Basic Data area:Period Type: WeekDisplayed UoM: Piece (PC)Choose Create. |  |
| 5 | Maintain Material Constraints | In the Constraint Materials area, choose Add if the following materials are not in the list:Material 1: RM2_CPMaterial 2: <Other material such as RM015>In the Constraint Quantities area, choose Add to maintainn following constraints.Week 1 (current week + 1 weeks): <500 PC>Week 2 (current week + 2 weeks): <500 PC>Week 3 (current week + 3 weeks): <500 PC>Week 4 (current week + 4 weeks): <500 PC>Week 5 (current week + 5 weeks): <50 PC>Week 6 (current week + 6 weeks): <50 PC>Week 7 (current week + 7 weeks): <50 PC>Week 8 (current week + 8 weeks): <50 PC> | If RM2_CP already exists in the Constraint Materials area, just mark it and unmark other materials. |
| 6 | Create the Constraint | Choose Create. |  |

###### Copy Simulation from Main Scenario

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

We can copy the existing simulation from main scenario to look at it again with the new restrictions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule pMRP Simulation Creation (F3968) . | The Schedule pMRP Simulation Creation (F3968) screen displays. |  |
| 3 | Copy the Existing Simulation | Mark the simulation from the main scenario and choose Copy. Alternatively, you can create a new simulation and then follow the steps for creating a simulation as in the main scenario. | The Creation of pMRP screen displays |  |
| 4 | Define Job Name | The system automatically suggests a job name - choose Step 2. |  |  |
| 5 | Sheduling Options | Choose Step 3. |  |  |
| 6 | Change Reference and Simulation ID | On the parameters screen change the name of the reference data and the simulation ID to 4B5_PMRP_<MMDD>_A2and 4B5_PMRP_SIM_<MMDD>_A2 | If the name is assigned, you can also choose your own. |  |
| 7 | Schedule the Simulation | Choose Schedule. |  |  |

###### Process pMRP Simulation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step deals with the material group constraints for RM2_CP in Process pMRP Simulation.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process pMRP Simulations (F3934). | The Process pMRP Simulations screen displays. |  |
| 3 | Filter the Simulation | On the Process pMRP Simulations screen, filter the simulation with the reference ID you just created and choose Go.Reference Data : 4B5_PMRP_<MMDD>_A2 or the name you created in the previous step.Choose the row of the filtered simulations. | The simulation displays. |  |
| 4 | Check Multi-Level Material Simulation | On the Demand Plan Simulation screen, the system shows many violated constraints. For example you can solve the material group constraints issue.Choose the first demand in red with supply constraints issue, for example, 75 in current week + 4In the Inspector area , navigate to FG3_CP and choose Multi-Level Material Simulation | The Multi-Level Material Simulation screen displays. |  |
| 6 | Pull in Quantity | On the Multi-Level Material Simulation, we try to solve the issue for RM2_CP.Choose the supplier constraint issues for raw material RM2_CP, then you could choose Pull in Quantity to preproduce partical quantity to reduce workload.On the Pull in Quantity screen, choose Adopt Proposal, the Capacity Distribution for the previous period is automatically updated with the Proposed Distribution, choose Apply. | The supply constraint is reduced. |  |
| 7 | Repeat the steps | Repeat the steps 4 – 5 for all existing supply constaints issue. |  |  |

If the flexible constraints needs to be changed, you could refer to step [Update Flexible Constraints](#unique_26) [page ] 32 and [Reprocess the pMRP Simulation](#unique_27) [page ] 33 from Variant 1: Flexible Contraints for Multiple Suppliers.

#### Use-Case B: Dealing with Internal Constraints for Production lines

##### Define Constraints for Production Line

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you could define internal constrains for production line.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Define Flexible Constraints (F4449). | The Define flexible Constraints screen displays. |  |
| 3 | Filter for the Material and Plant | On the Define Flexible Constraints screen, make the following filters and choose Go.Plant: 3310Material: FG3_CP |  |  |
| 4 | Filter Material and Create a Constraint Object | If no existing constrains, choose Add, make the following entries and choose OK:Plant: 3310Constraint Scope: Single MaterialMaterial: FG3_CP | Constraints Added and the detailed Constraint screen displays. |  |
| 5 | Create the Constraint | On the Constraint screen, make the following entries in Basic Data area and Choose Create:Period Type: WeekDsiplay UoM: Piece (PC)Constraint Catagory: Production LineProduction Line: ASSPKG |  |  |
| 6 | Enter the Constraints | Week 1 (current week): <25 PC>Week 2 (current week + 1 weeks): <25 PC>Week 3 (current week + 2 weeks): <25 PC>Week 4 (current week + 3 weeks): <25 PC>Week 5 (current week + 4 weeks): <25 PC>Week 6 (current week + 5 weeks): <25 PC>Week 7 (current week + 6 weeks): <25 PC> |  |  |
| 7 | Save | Save the changes |  |  |
| 8 | Repeat | Repeat the steps 4 -7 for ASSPKG9Please maintain the weekly constraint quantity 250 for ASSPKG9. |  |  |

##### Copy Simulation from Main Scenario

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

We can copy the existing simulation from main scenario to look at it again with the new restrictions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule pMRP Simulation Creation (F3968). | The Schedule pMRP Simulation Creation (F3968) screen displays. |  |
| 3 | Copy the Existing Simulation | Mark the simulation from the main scenario and choose Copy. | The Creation of pMRP screen displays |  |
| 4 | Define Job Name | The system automatically suggests a job name, choose Step 2 . |  |  |
| 5 | Sheduling Options | Click on Step 3 . |  |  |
| 6 | Change Reference and Simulation ID | On the parameters screen change the name of the reference data and the simulation ID to 4B5_PMRP_<MMDD>_B and 4B5_PMRP_SIM_<MMDD>_B. |  |  |
| 7 | Schedule the Simulation | Click on Schedule |  |  |

##### Process pMRP Simulation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

We can now see how a restriction of the production line affect our plan.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process pMRP Simulations (F3934). | The Process pMRP Simulations screen displays. |  |
| 3 | Filter and Enter the Simulation | On the Process pMRP Simulations screen, filter the simulation with the reference ID you just created and choose Go.Reference Data : 4B5_PMRP_<MMDD>_B | The Demand Plan Simulation screen displays. |  |
| 4 | Copy the Simulation | Choose the checkbox of the filtered simulation, and choose Copy in the upper right corner.On the Copy screen, make the following entires and choose Copy.Copy from Current Simulation: XNew Simulation ID: 4B5_PMRP_SIMU_<MMDD>_B1New Simulation Description: 4B5_PMRP_SIMU_<MMDD>_B1 | It shows Simulation Copied. |  |
| 5 | Check the Copied Simulation | On the Process pMRP Simulations screen, choose against the row of the newly copied simulation with simulation ID: 4B5_PMRP_SIMU_<MMDD>_B1 | The Demand Plan Simulation screen displays. |  |
| 6 | Mark the First Restriction Violation | On the Demand Plan Simulation screen ,mark the first week in which the system detects a violated constraint. | The Inspector panel displays. |  |
| 7 | Choose Multi-Level Matrerial Simulation | In the Inspector panel choose Multi-Level Material Simulation. | The Multi-Level Material Simulation screen displays. |  |
| 8 | Mark the Finished Goods and Change Source of Supply | On the Multi-Level Material Simulation screen, you could see simulation details for components in Bill of Material area.Choose the Issues for finished goods FG1_CP/FG3_CP, then you choose Change Source of Supply to distribute demand into different Production Versions to balance workload. |  |  |
| 9 | Change Supply Source | On the Change Source of Supply screen, choose Adopt Proposal, the Quantity Distribution for two production versions are automatically updated with the Proposed Distribution, choose Apply. | The material constraint issue is reduced. |  |
| 10 | Repeat the Steps | Repeat steps 5-7 for all existing violated constraints in other weeks. |  |  |

##### Update the Production Line Constraints

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Suppose we are informed that there is going to a maintenance interval. We want to take this into account and therefore, update the production line restrictions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Define Flexible Constraints (F4449). | The Define Flexible Constraints screen displays. |  |
| 3 | Filter Material | On the Define Flexible Constraints screen, filter the material and choose Go.Material: FG3_CP | The filtered material constraints display. |  |
| 4 | Maintain Material Constraints | Choose the row with the material constraint which you created in the previous step an navigate Material Constraint screen.By clicking Editin the upper right corner you can change the existing constraints.In the Constraint Quantities area enter the following dataWeek 1 (current week): <40 PC>Week 2 (current week + 1 weeks): <40 PC>Week 3 (current week + 2 weeks): <40 PC>Week 4 (current week + 3 weeks): <40 PC>Week 5 (current week + 4 weeks): <40 PC>Week 6 (current week + 5 weeks): <40 PC>Week 7 (current week + 6 weeks): <40 PC> |  |  |
| 6 | Save Constraints | Choose Save in the bottom right corner of the screen. | The constraints are saved. |  |

##### Reprocess the pMRP Simulation

After the constraints get updated, it could impact the existing simulation directly, you could refer to step Process the PMRP Simulation from Variant 1: Flexible Contraints for Multiple Suppliers to resolve new violated constraints.

After that, you could refer to Process pMRP Simulations to release the simulation and Check Planned Independent Requirements from Main Scenario to check updated PIRs.

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Scope Item | Business Condition |
| --- | --- |
| 31L - Production Capacity Evaluation | After requirement plan is optimized by predictive material and resource planning, you can proceed with further operation process for capacity scenario in 31L test script. |

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
- related-to :: [[12-production-and-manufacturing/test-script-material-requirements-planning-j44-ae-sap-s-4hana-cloud-pu]]
- related-to :: [[12-production-and-manufacturing/test-script-planning-and-production-in-other-plant-consumer-products-7]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4B5_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 72,801 chars in the whole document
