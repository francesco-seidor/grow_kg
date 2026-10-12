---
id: 12-production-and-manufacturing/test-script-make-to-stock-production-discrete-manufacturing-bj5-ae-sap
title: "Test Script: Make-to-Stock Production – Discrete Manufacturing (BJ5_AE), SAP S/4HANA Cloud Public Edition (BJ5_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item BJ5_AE: MTS discrete manufacturing from PIRs and MRP to production orders and goods receipt."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/make-to-stock-discrete-and-repetitive]
aliases: [BJ5_S4CLD2608_BPD_EN_AE]
keywords: [Make-to-Stock Discrete and Repetitive Manufacturing, make-to-stock production, planned independent requirements, material requirements planning, planned order conversion, material availability status, material staging, production order release, production order confirmation, goods receipt posting]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BJ5_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1270
topic: 12-production-and-manufacturing/make-to-stock-discrete-and-repetitive
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Make-to-Stock Production – Discrete Manufacturing (BJ5_AE), SAP S/4HANA Cloud Public Edition (BJ5_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BJ5_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Make-to-Stock Discrete and Repetitive Manufacturing** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Make-to-Stock Production – Discrete Manufacturing (BJ5_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232861713)

[2 Prerequisites 4](#_Toc232861714)

[2.1 System Access 4](#_Toc232861715)

[2.2 Roles 4](#_Toc232861716)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232861717)

[2.4 Business Conditions 8](#_Toc232861718)

[2.5 Preliminary Steps 8](#_Toc232861719)

[2.5.1 Create Initial Material Stock 8](#_Toc232861720)

[3 Overview Table 10](#_Toc232861721)

[4 Test Procedures 13](#_Toc232861722)

[4.1 Anonymous Forecast and MRP 13](#_Toc232861723)

[4.1.1 Create Planned Independent Requirements 13](#_Toc232861724)

[4.1.2 Material Requirements Planning at Plant Level 14](#_Toc232861725)

[4.1.3 Evaluate Stock/Requirements Situation 16](#_Toc232861726)

[4.2 Production Order Conversion and Available-to-Promise Check 18](#_Toc232861727)

[4.2.1 Conversion to Production Orders for Subassembly and Final Assembly 18](#_Toc232861728)

[4.2.2 Review Order Progress 20](#_Toc232861729)

[4.3 Production Order Processing for Subassembly 22](#_Toc232861730)

[4.3.1 Review Material Availability Status for Production Orders 22](#_Toc232861731)

[4.3.2 Material Staging for Subassembly 24](#_Toc232861732)

[4.3.3 Release Production Order for Subassembly 25](#_Toc232861733)

[4.3.4 Confirm Production Operations for Subassembly 27](#_Toc232861734)

[4.3.5 Post Goods Receipt for Subassembly Production Order 28](#_Toc232861735)

[4.4 Production Order Processing for Final Assembly 29](#_Toc232861736)

[4.4.1 Review Material Availability Status for Production Orders 29](#_Toc232861737)

[4.4.2 Material Staging for Final Assembly 31](#_Toc232861738)

[4.4.3 Release Production Order for Final Assembly 33](#_Toc232861739)

[4.4.4 Check Serial Numbers 34](#_Toc232861740)

[4.4.5 Pick Components for Final Assembly 35](#_Toc232861741)

[4.4.6 Confirm Production Operations for Final Assembly 37](#_Toc232861742)

[4.4.7 Review Production Order 38](#_Toc232861743)

[4.4.8 Final Confirmation of Production Operations for Final Assembly 40](#_Toc232861744)

[4.4.9 Post Goods Receipt for Final Assembly Production Order 41](#_Toc232861745)

[4.5 Collective Orders 42](#_Toc232861746)

[4.5.1 Create Planned Independent Requirements for **FG130** 42](#_Toc232861747)

[4.5.2 Material Requirements Planning at Plant Level for **FG130** 43](#_Toc232861748)

[4.5.3 Evaluate Stock/Requirements Situation 45](#_Toc232861749)

[4.5.4 Conversion to Production Orders for Subassembly and Final Assembly 46](#_Toc232861750)

[4.5.5 Review Material Availability Status for Production Orders 48](#_Toc232861751)

[4.5.6 Material Staging for Subassembly and Final Assembly 49](#_Toc232861752)

[4.5.7 Release Production Order for **FG130** 51](#_Toc232861753)

[4.5.8 Confirm Production Operations for **SG30** and **FG130** 52](#_Toc232861754)

[4.5.9 Post Goods Receipt for Final Assembly Production Order **FG130** 54](#_Toc232861755)

[4.6 Check PIR Quality (Optional) 55](#_Toc232861756)

[4.6.1 Sell from Stock for **FG126** 55](#_Toc232861757)

[4.6.2 Check PIR Quality 55](#_Toc232861758)

[4.7 Review Scrap Report 56](#_Toc232861759)

[4.8 Review Manufacturing Object Pages 57](#_Toc232861760)

[5 Appendix 59](#_Toc232861761)

[5.1 Succeeding Processes 59](#_Toc232861762)

[5.2 Document Integration 60](#_Toc232861763)

[5.3 Production Resources Tools 61](#_Toc232861764)

[5.4 Additional Functional Information 61](#_Toc232861765)

## Purpose

Overview

This scope item enables production planning in make-to-stock scenarios for a serial number managed finished good.

The process starts with the creation of a demand forecast for finished goods represented by Planned Independent Requirements (PIRs). Based on PIRs, Material Requirements Planning (MRP) creates a production plan for finished goods and explodes the entire bill of material structure. As a result, semifinished component production and raw material demand is planned. Production planners can analyze and manually change the planned order-based production plan.

Raw material demand leads to purchase requisitions that trigger alternative procurement scenarios referenced in this scope item.

The production process itself is entirely covered by using the conversion of planned into production orders, order release, material staging and picking, confirmation of order operations, and goods receipt posting. Order-based target and actual cost is created, ensuring fully integrated material and value streams.

|  |
| --- |
| Note Starting with CE2102, Create Production Resources/Tools functionalities are available.Starting with CE2202, Collective Orders functionalities are available. |

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
| Production Engineer - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC | Production Engineering - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | FG126 | Serial Number Managed Finished Good MTS |  |
| Material | FG130 | Finished Good for Collective Orders |  |
| Material | SG21 | Semifinished Good Repetitive Manuf. |  |
| Material | SG22 | Semifinished Good Phantom |  |
| Material | SG23 | EMI23, PD, Subcontracting |  |
| Material | SG25 | Semifinished Good Ext. Procurement |  |
| Material | SG124 | Semifinished Good Subassembly |  |
| Material | SG30 | Semi-Finished Good for Collective Orders |  |
| Material | RM13 | RAW13, PD, Subcontracting |  |
| Material | RM14 | RAW14, PD, Subcontracting |  |
| Material | RM16 | Raw Material Ext. Procurement |  |
| Material | RM20 | Raw Material Ext. Procurement Contract |  |
| Material | RM27 | RAW Material Packaging Box |  |
| Material | RM120 | RAW Material Ext. Procurement with QM in Procurement |  |
| Material | RM122 | RAW Material, Ext. Procurement, Batch controlled (FIFO-strategy) |  |
| Material | RM124 | RAW Material Ext. Procurement Consumption based |  |
| Material | RM128 | RAW Material Ext. Procurement with Consignment |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |

Bill of Material Structure

This overview shows the bill of material structure and the usage of each component if you have activated all optional enhancements.

| Material | Level | Material Type | Unit | Characteristics of Material | Optional Enhancements |
| --- | --- | --- | --- | --- | --- |
| FG126 | 0 | FERT | PC | Finished Good for MTS processing with Serial Number |  |
| SG21 | 1 | SEMI | PC | SF Repetitive Manufacturing | Only if Make-to-Stock Production – Repetitive Manufacturing (BJH) scope item is activated. |
| RM12 | 2 | RAW | PC | External procured |  |
| SG22 | 1 | SEMI | PC | SF, Phantom Assembly |  |
| RM16 | 2 | RAW | PC | External procured |  |
| RM122 | 1 | RAW | PC | External procured with Batch Management |  |
| RM128 | 1 | RAW | PC | External procured with Consignment Processing | Only if Scheduling Agreements in Procurement (BMR) scope item is activated. |
| SG23 | 1 | SEMI | PC | External procured with subcontract |  |
| RM13 | 2 | RAW | PC | External procured |  |
| RM14 | 2 | RAW | PC | External procured |  |
| SG25 | 1 | SEMI | PC | SEMI25, PD, External Procurement |  |
| SG124 | 1 | SEMI | PC | Internal production of subassembly (MTS strategy) |  |
| RM124 | 2 | RAW | PC | External procured using Fixed Bin |  |
| RM20 | 1 | RAW | PC | External procured contract |  |
| RM27 | 1 | RAW | PC | External procured – Packaging Box |  |
| FG130 | 0 | FERT | PC | Finished Good for Collective Orders |  |
| SG30 | 1 | SEMI | PC | Semi-Finished Good for Collective Orders |  |
| RM124 | 2 | RAW | PC | External procured using Fixed Bin |  |
| RM20 | 1 | RAW | PC | External procured contract |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

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
| 5CP | Create Production Resources/Tools - MDS |

|  |
| --- |
| Note In case you want to create your own number ranges for production orders or process orders, see SAP Note [3388387](https://me.sap.com/notes/3388387). |

### Business Conditions

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation | You have completed the step described in the Standard Cost Calculation (BEG) test script. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |

### Preliminary Steps

#### Create Initial Material Stock

Purpose

In a real business scenario, initial material stock is usually purchased from external suppliers through standard purchasing or subcontracting processes. For only testing purpose, this process step shows you how to create and post the initial material stock to storage locations directly.

Prerequisite

Before creating initial material stocks, we recommend that you check stock level for FG130 and SG30. To do that, log onto the SAP Fiori launchpad as a Production Planner, and open Manage Material Coverage - New Version (F0251A) app. Remove some stock if there is already sufficient amount of stock in store. Otherwise, no planned orders can be generated later. You can either post initial stock directly to the storage locations, or refer to test scripts from Procurement of Direct Materials (J45) or Scheduling Agreements in Procurement (BMR) test scripts for purchasing processes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Choose Document Type | Make the following entries:Trans./Event: Goods ReceiptReference Document: Other | The Goods Receipt Other - XXXX screen displays. |  |
| 4 | Enter Data | In the Detail Data section, make the following entries and press Enter.On the Where tab:Movement Type: 561Plant: 3310Storage Location: 331B for SGXX and 331C for RMXX materialsOn the Quantity tab:Quantity:<100 PC>On the Material tab:Material: <BOM Material>, refer to section Master Data, Organizational Data, and Other Data for Bill of Material Structure. You must create initial stock for all materials except for SG124 , FG126 , FG130, SG30, and RM128. Post initial material stock for RM128 after you finish Review Order Progress in Make-to-Stock Production – Discrete Manufacturing (BJ5).Choose Next Item and select Item OK to add entries. |  |  |
| 5 | Check | Choose Check. | The document is ready to be posted. |  |
| 6 | Post | Choose Post. | Material document XXX is posted and materials are available in stock. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Planned Independent Requirements](#unique_9) [page ] 13 | Production Planner | Maintain PIRs (F3445) | Independent Requirements for Finished Goods are created. |
| [Material Requirements Planning at Plant Level](#unique_10) [page ] 14 | Production Planner | Schedule MRP Runs (F1339) | Independent Requirements for Finished Goods are planned. |
| [Evaluate Stock/Requirements Situation](#unique_11) [page ] 16 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Stock/Requirements situation for the planned materials are analyzed. |
| [Conversion to Production Orders for Subassembly and Final Assembly](#unique_12) [page ] 18 | Production Planner | Manage Material Coverage - New Version (F0251A) | Planned Orders for Finished Goods and Semi-finished Goods are converted to Production Orders. |
| [Review Order Progress](#unique_13) [page ] 20 | Production Planner | Review Order Progress - Multilevel View (F7681) | The overall issues for fulfilling the production order are displayed. |
| [Review Material Availability Status for Production Orders](#unique_14) [page ] 22 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | Missing parts for the production order are displayed. |
| [Material Staging for Subassembly](#unique_15) [page ] 24 | Production Operator - Discrete Manufacturing | Stage Materials for Production (MF60) | The components needed for the Semi-finished Goods production order are moved from various storage locations to the production storage location. |
| [Release Production Order for Subassembly](#unique_16) [page ] 25 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | Production order for Semi-finished Goods is released. |
| [Confirm Production Operations for Subassembly](#unique_17) [page ] 27 | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | Production order for Semi-finished Goods is confirmed. |
| [Post Goods Receipt for Subassembly Production Order](#unique_18) [page ] 28 | Warehouse Clerk | Post Goods Movement (MIGO) | The goods receipt for the Semi-finished Goods is posted. |
| [Review Material Availability Status for Production Orders](#unique_19) [page ] 29 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | Missing parts for the production order are displayed. |
| [Material Staging for Final Assembly](#unique_20) [page ] 31 | Production Operator - Discrete Manufacturing | Stage Materials for Production (MF60) | The components needed for the Finished Goods production order are moved from various storage locations to the production storage location. |
| [Release Production Order for Final Assembly](#unique_21) [page ] 33 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | Production order for Finished Goods is released. |
| [Check Serial Numbers](#unique_22) [page ] 34 | Production Operator - Discrete Manufacturing | Display Production Order (CO03) | The serial numbers for Finished Goods are generated. |
| [Pick Components for Final Assembly](#unique_23) [page ] 35 | Production Operator - Discrete Manufacturing | Pick Components for Production Orders (CO27) | Goods movements are posted. |
| [Confirm Production Operations for Final Assembly](#unique_24) [page ] 37 | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | Operations except for last one are confirmed. |
| [Review Production Order](#unique_25) [page ] 38 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) |  |
| [Final Confirmation of Production Operations for Final Assembly](#unique_26) [page ] 40 | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | Final confirmation of the last operation is carried out. |
| [Post Goods Receipt for Final Assembly Production Order](#unique_27) [page ] 41 | Warehouse Clerk | Post Goods Movement (MIGO) | The goods receipt for the production order is posted. |
| [Create Planned Independent Requirements for FG130](#unique_28) [page ] 42 | Production Planner | Maintain PIRs (F3445) |  |
| [Material Requirements Planning at Plant Level for FG130](#unique_29) [page ] 43 | Production Planner | Schedule MRP Runs (F1339) |  |
| [Evaluate Stock/Requirements Situation](#unique_30) [page ] 45 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) |  |
| [Conversion to Production Orders for Subassembly and Final Assembly](#unique_31) [page ] 46 | Production Planner | Manage Material Coverage - New Version (F0251A) |  |
| [Review Material Availability Status for Production Orders](#unique_32) [page ] 48 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) |  |
| [Material Staging for Subassembly and Final Assembly](#unique_33) [page ] 49 | Production Operator - Discrete Manufacturing | Stage Materials for Production (MF60) |  |
| [Release Production Order for FG130](#unique_34) [page ] 51 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) |  |
| [Confirm Production Operations for SG30 and FG130](#unique_35) [page ] 52 | Production Operator - Discrete Manufacturing | Confirm Production Order Operation (CO11N) |  |
| [Post Goods Receipt for Final Assembly Production Order FG130](#unique_36) [page ] 54 | Warehouse Clerk | Post Goods Movement (MIGO) |  |
| [Check PIR Quality (Optional)](#unique_37) [page ] 55 |  |  |  |
| [Sell from Stock for FG126](#unique_38) [page ] 55 |  |  |  |
| [Check PIR Quality](#unique_39) [page ] 55 | Production Planner | Maintain PIRs (F3445) |  |
| [Review Scrap Report](#unique_40) [page ] 56 | Production Supervisor - Discrete Manufacturing | Material Scrap - Maximum Deviation (F2035) - Maximum Deviation |  |
| [Review Manufacturing Object Pages](#unique_41) [page ] 57 | Any role for production listed in chapter Roles | Search function |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Anonymous Forecast and MRP

#### Create Planned Independent Requirements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create Planned Independent Requirements (PIRs). PIRs are used to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split according to dates.

|  |
| --- |
| Note Instead of creating a single requirement, sometimes one or more planned independent requirements can be maintained and included in a requirement plan for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries and choose Go:Plant: 3310Period Indicator: Weekly(W) or Monthly(M)Version Active: Select all optionsMaterial: FG126Note Period is set to Week, because it is set in material master of the bearing. | The searched material item displays. |  |
| 5 | Edit PIRs | Select the material item and choose Edit in the upper-right corner of the screen.On the screen, enter quantities per period, for example:PIR: 100 for all 12 periodsMake sure the version is active.Version Active: Yes |  |  |
| 6 | Save PIRs Draft | Choose Save in the bottom right corner of the screen. | The PIRs draft is saved. |  |

#### Material Requirements Planning at Plant Level

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use Material Requirement Planning (MRP) to tailor available capacities and receipts on time to suit requirement quantities. As a result, single-item multi-level requirement planning is performed for plant 3310.

Prerequisite

The Make-to-Stock finished goods are planned at plant level. There is now a requirement for FG126 in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirement Planning (MRP)Job Name: <MRP for FG126 >Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: <select>Recurrence Pattern: Single RunChoose OK.Choose Step 3.For 3.Parameters section:Plant: 3310Material: FG126Changed BOM Components: <select>Planning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG126 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

#### Evaluate Stock/Requirements Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock/requirements situation for Make-to-Stock finished goods (FG126) in the stock/requirements list after the requirement planning is performed.

Prerequisite

Requirement planning is carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments (F2101A) screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 4 | Select Material | Search in the Material bar, select the following materials and then choose Manage Materials:Material: FG126Material: SG124 | The Manage Material Coverage screen displays. |  |
| 5 | Review Stock / Requirements List | Choose the corresponding material in the Materials list on the left side. | The detailed stock / requirements list for each material displays. |  |
| 6 | Display Planned Order | From the Materials list on the left side, choose the material for which you want to check for the planned order:Material: FG126Material: SG124On the right screen, choose PldOrd XXXX in the MRP Element column.Note The BOM explosion during the MRP run has generated dependent requirements for the demand-driven planned components. If there is not enough inventory to fulfill the requirements, planned orders and purchase requisitions are created for both inhouse-produced and externally-procured materials.Depending on the elements created in the MRP run, refer to Procurement of Direct Materials(J45) or Scheduling Agreements in Procurement (BMR) test scripts for processing externally-procured materials. | The selected planned order displays.Note The planned order is generated only when there is storage for these materials.If you want to display more information of the planned order, choose Document Info at the bottom of the dialog box. |  |
| 7 | Rescheduling Check (Optional) | On the Stock/Requirements List tab, the Rescheduling column displays the rescheduling status of the following MRP elements.PurReqPurchase OrdersPlanned OrdersProduction OrdersProcess OrdersIf needed, you can choose the following icons in the Rescheduling column for corresponding functions:Reschedule in (bring operation forward if the receipt element lies after the requirement date)Reschedule out (postpone operation, if the receipt element lies before the requirement date)Plan Process according to scheduleCancel ProcessExcess StockExcess in individual segment |  |  |

### Production Order Conversion and Available-to-Promise Check

#### Conversion to Production Orders for Subassembly and Final Assembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Daily MRP run creates planned orders for goods to be produced internally. This process step shows you how to convert the planned orders to production orders for both semifinished goods and finished goods when reached the planned start date.

Prerequisite

The MRP run has generated planned orders for SG124 (subassembly) and FG126 (final assembly).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A). | The Manage Material Coverage screen displays. |  |
| 3 | Select Material | On the Manage Material Coverage screen, enter the following data and choose Go.Material: FG126Plant: 3310Shortage Definition: MRP StandardChoose the row of the filtered material to check more details. | The Manage Material Coverage screen displays with more details. |  |
| 4 | Find Planned Order | Check the generated planned orders.If no planned orders are generated, it could be because FG126 has sufficient amount of stock in store. In this case, remove some stock. Go back to create PIRs and run MRP again to generate planned orders. |  |  |
| 5 | Add Planned Order Long Text (Optional) | Click on the planned order number (PldOrd XXXX) under column MRP Element. In the pop-up dialog PldOrd XXXX, choose Change Planned Order.On the Change Planned Order screen, choose tab Long Text, enter the text, and choose Save. | The long text maintained here can be later copied to the converted production order. |  |
| 6 | Convert Planned Order to Production Order | Select Convert from Edit dropdown list in the Actions column for a planned order (PldOrd XXXX).In the Convert Planned Order XXXX dialog box, choose Convert to Production Order, confirm Delivery Date and Quantity. Choose Convert. | The production order is created. |  |
| 7 | Convert Planned Order to Production Order for Semifinished Goods | Open Manage Planned Orders (F4170). | The Manage Planned Orders screen displays. |  |
| 8 | Filter Planned Orders | On the Manage Planned Orders screen, enter the following data and choose Go.Material: SG124In the Planned Orders area, you can check the generated planned orders.Select Convert from Edit drop down list in the Actions column for a planned order (PldOrd XXX) .In the Convert Planned Order XXXX dialog box, choose Production Order, confirm Delivery Date and Quantity. Choose Convert.You can also perform mass conversion for production order/process order/purchase requisition by selecting multiple planned orders and choosing Convert to. The system then performs a check to validate if the selected planned orders can be converted to the designated order types.A success dialog box pops up if all planned orders are validated successfully. Choose OK and the message is displayed: Planned order converted successfully. The successful message is displayed at the bottom left.A warning dialog box pops up to prompt the number of failed orders and possible reasons if failed orders exist. Choose Convert to XXX, and the failed messages and successful messages are displayed at the bottom left. | If no planned orders are generated, please first ensure if AOR is maintained correctly for plant 3310 and MRP controller 001.Check the message:Planned Order XXX converted to Production order XXX |  |

|  |
| --- |
| Note Start from CE2202, it's possible to change the default settlement rule receiver from material to cost center or WBS element for event-based production orders/process orders. For details, you can check the chapter Create/Change Settlement Rule for Non-Material Settlement in Scope Item 3F0 (Event-Based Production Cost Posting). |

#### Review Order Progress

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to solve material shortage issues of a production order after reviewing the material availability in a BOM structure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Review Order Progress - Multilevel View (F7681). | You can also navigate to Review Order Progress – Multilevel View through app Manage Material Coverage - New Version (F0251A) or Monitor Internal Requirements (F0263A).Access the app Manage Material Coverage - New Version (F0251A). Make the following entries and choose Go:Material: FG126Plant: 3310Choose the line item of the displayed material. Under tab Stock/Requirements List, click the production order in the MRP Element column, and choose Review Order Progress – Multilevel View.Access the app Monitor Internal Requirements (F0263A). Select Ordered Requirements from Shortage Definition, choose Adapt Filters, adopt the Order filter to search your production order number, and click the affected production order number. Choose Related Actions > Review Order Progress – Multilevel View. |  |
| 3 | Display Multilevel Order Report | On the Review Order Progress – Multilevel View screen, make the following entries and choose Go.Document Type: Production Order (FE)Production Order Number: <Production Order Number>Use the value help to find the production order number. | The BOM structure of the order is displayed and the component availability is checked.For listed components, if there is missing quantity or component that requires reschedule in action/finish date in the past, the following icons are displayed:The error icon indicates detailed errors at the corresponding component level.The warning icon indicates if there is a start date or opening date in the past. |  |
| 4 | Review Order Issues | In the Issues column, choose the icon in the top row. | The overall issues for fulfilling the order are displayed.You can also check issues at different levels by choosing the issue icon listed in different rows. |  |
| 5 | Solve Order Issues | In the Material Number column, click the component which is causing issues.In the pop-up window, choose Related Actions > Manage Material Coverage. | The Manage Material Coverage screen displays.The production planner can adopt corresponding actions to make up the shortage. To proceed testing subsequent steps, follow chapter [Create Initial Material Stock](#unique_7) [page ] 8 to post material stock for RM128 to make sure there’s sufficient amount of stock:Material: RM128Quantity: <100 PC>Note In response to the update of requirement/supply, the replenishment to a sales order (Make-to-Stock) is dynamic, because the pegging logic is first in first out.If the shortage component is not displayed, remove some stock for RM128. You can refer to chapter [Create Initial Material Stock](#unique_7) [page ] 8. Follow the steps except for step 4, where the following entries must be made:On the Where tab:Movement Type: 562On the Material tab:Material: RM128 |  |

### Production Order Processing for Subassembly

#### Review Material Availability Status for Production Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review material availability status for production orders.

Prerequisite

Production orders are created for subassembly and final assembly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). |  |  |
| 3 | Check Default Area of Responsibility (Supervisor) | Choose the user icon and select App Settings. Choose tab Production Supervisors.In the AOR Status column, choose the button to assign or unassign entries, and make sure only the following entries are assigned:Plant 1 AE 3310MTS DI- Valuated (YB1)Choose Back. | The Manage Production Order screen displays. |  |
| 4 | Select Production Order | On the Manage Production Orders (F2336) screen, make the following entries and choose Go. If needed, you can adjust filter options through Adapt Filters.Status: CreatedMaterial: FG126Production Plant: 3310 | The Material and Production Plant fields are added to the filter bar.The searched order displays. |  |
| 5 | Review Material Availability Status | In the Issue column, check the Component Issue icon to the right of the order to display the missing components. | For FG126, the expected missing components are RM122, RM20, SG124. The raw materials are supplied after the Material Staging for Final Assembly step.Note However, it’s also possible that SG124 is not a missing component for the final assembly production order. This happens when you have SG124 supplied (released production order for SG124 or unrestricted stock) already, but it's not yet reserved by any final assembly production orders. |  |
| 6 | Check PRT (Optional) | If Production Resources/Tools (PRTs) are assigned to the production order, you can check PRT details within this app.Select the order, and choose Order Schedule facet. Choose Settings for the Operations part, and make sure PRTs is selected in the View Settings. PRT hyperlink is available for the operations. |  |  |
| 7 | Check Long Text Copied from Planned Order (Optional) | If any long text is maintained for the planned order, you can check it in the converted production order.Select the order and choose Edit Order in the upper right corner.On the Production Order Change screen, choose tab Long Text, and check the text. | The long text maintained in the planned order is copied to the converted production order. |  |

|  |
| --- |
| Note You can use the following procedure when you want to monitor the uncovered requirements originating from production orders with the Monitor Internal Requirements (F0263A) app. Before continuing with the following procedure, make sure at least the stock of one component is less than the requested amount of the current production order. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On (Optional) | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App (Optional) | Open Monitor Internal Requirements (F0263A). | The Monitor Internal Requirements screen displays. |  |
| 3 | Search for Material (Optional) | On the upper-right screen, choose Adapt Filters to display more filter options. In the Adapt Filters dialog box, select Source Material, Planning Plant, Order, and choose OK.Enter the following data and choose Go:Source Material: SG124Planning Plant: 3310Order: <Production Order Number> | The shortage component and affected order display.For SG124, the expected missing component is RM124. The semifinished goods are supplied after the Release Production Order for Subassembly step.Note The shortage component displays only when the current replenishment of the component is less than the requested amount of the current production order. |  |
| 4 | Review Material Availability Status | Under Component, select the check box of the material item for which you want to check details of the missing component. Choose Manage Requirements. | The Manage Internal Requirements screen displays with the shortage material details. |  |

#### Material Staging for Subassembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to stage materials for subassembly production.

|  |
| --- |
| Note If there is sufficient amount of stock available in the production storage location, then no line items are generated. In this case, you can skip this step and proceed onward. |

Prerequisite

Stock must be available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stage Materials for Production (MF60). | The Material Staging for Planned Orders screen displays. |  |
| 3 | Enter Details | Make the following entries and choose Execute.In the Staging Types section:SLoc Level: <select>Plant: 3310Selection Horizon for Reqmts: <date must be in the future - after scheduled start date>On the Production/Process Orders tab:Order: <Production Order Number for Semifinished Material> | The Pull List: Storage Location Level screen displays. |  |
| 4 | Choose Replenishment Elements | In the Total Reqmts table, select the line items and choose Replenishment Proposal on the top of the screen.Review staged quantities and choose Replenishment Elements. |  |  |
| 5 | Enter Replenishment Storage Location and Stage Material | In the Replen. Element table, in the RepLoc column, enter 331C for staged materials.Choose Stage. |  |  |
| 6 | Save | Save your entries.Note Missing materials are transferred to the shop floor from the designated storage area.With this step, the shortage of material RM124 for Subassembly production order is supplied. | Materials are staged for subassembly. |  |

#### Release Production Order for Subassembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to release the order at header level, which releases the entire order and all its operations. The order and the operations receive the REL (released) status.

Prerequisite

The production order created by the MRP controller is assigned a release date in accordance with the scheduling margin key.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). | The Manage Production Order screen displays. |  |
| 3 | Check Default Area of Responsibility (Supervisor) | Choose the user icon and select App Settings. Choose tab Production Supervisors.In the AOR Status column, choose the button to assign or unassign entries, and make sure only the following entries are assigned:Plant 1AE (3310)MTS DI - Valuated (YB1)Choose Back. |  |  |
| 4 | Select Production OrderCheck details of Production Order | On the Manage Production Orders screen, choose Adapt Filters to display more filter options. In the Adapt Filters dialog box, select Material and Production Plant and choose OK.Enter the following filter criteria, and choose Go:Status: CreatedMaterial: SG124Production Plant: 3310 | The Material and Production Plant fields are added to filter bar.The searched order displays. |  |
| 5 | Execute Release | Select the searched order. Choose Release. | The order is released.Note With the release of production order for subassembly production, the shortage of material SG124 for final assembly production order is supplied. |  |

#### Confirm Production Operations for Subassembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents include the processing status of orders, operations, sub-operations, and individual capacities. It's an instrument for controlling orders. This process step shows you how to confirm subassembly production order operations for semifinished material SG124 . A goods movement document is generated when the last operation is confirmed. The backflush is carried out together with the confirmation steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). |  |  |
| 3 | Enter Production Order and Operation | On the Enter Order and Operation screen, make the following entries and choose Go:Order: <Production Order Number for semifinished goods>Operation: <operation number> for example, <0010> |  |  |
| 4 | Enter Quantities Data | In the Quantities section, make the following entries:Yield: <Quantity of prod. order less scrap>Scrap: <scrap amount> |  |  |
| 5 | Check Material Movements | In the Material Movements section, check the material list.Note The system shows you an overview materials table for which the material withdraws are done along with operation confirmation.The material RM124 , is set for backflush (in material master) for withdraws to be done automatically after the operation is confirmed. |  |  |
| 6 | Enter Activities Data and Save | In the Activities section, make the following entries:Setup: <setup time>Machine: <machine time>Labor: <labor time>For partial confirmation, choose Post.For final confirmation, choose Post and Complete. | Confirmation is made. |  |
| 7 | Repeat Steps | Go back and repeat steps 3 to 6 for Operation 0020. |  |  |
| 8 | Good Receipt | When all Operations are finally confirmed all materials consumed in production are backflushed. | backflush for all consumed materials is done. |  |

#### Post Goods Receipt for Subassembly Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods receipt for subassembly production order.

Prerequisite

The final confirmation of production for semifinished goods is made.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Display Material Document screen displays. |  |
| 3 | Enter Goods Receipt Order Data | Make the following entries:Select Goods Receipt and Order from the dropdown list on top of the screen.Order: <Production order number for semifinished goods>GR/RI Slip No.: <101>Document date: <default>Posting date: <default> |  |  |
| 4 | Enter Data and Post Goods Receipts | Enter the following entries, and select Item OK for each item:On the Quantity tab:Quantity: <quantity>On the Where tab:Storage Location: 331BStd. storage 2Choose Check, then choose Post. | The system displays the message: Material document 500xxxxxxx posted |  |

### Production Order Processing for Final Assembly

#### Review Material Availability Status for Production Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review material availability status for production orders.

Prerequisite

Production orders are created for subassembly and final assembly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). |  |  |
| 3 | Check Default Area of Responsibility (Supervisor) | Choose the user icon and choose App Settings. Choose tab Production Supervisors.In the AOR Status column, choose the button to assign or unassign entries, and make sure only the following entries are assigned:Plant 1 AE 3310MTS DI- Valuated (YB1)Choose Back. | The Manage Production Order screen displays. |  |
| 4 | Select Production Order | On the Manage Production Orders (F2336) screen, make the following entries and choose Go. If needed, you can adjust filter options through Adapt Filters.Status: CreatedMaterial: FG126Production Plant: 3310 | The Material and Production Plant fields are added to the filter bar.The searched order displays. |  |
| 5 | Review Material Availability Status | In the Issue column, check the Component Issue icon to the right of the order to display the missing components. | For FG126, the expected missing components are RM122, RM20, SG124. The raw materials are supplied after the Material Staging for Final Assembly step.Note However, it’s also possible that SG124 is not a missing component for the final assembly production order. This happens when you have SG124 supplied (released production order for SG124 or unrestricted stock) already, but it's not yet reserved by any final assembly production orders. |  |
| 6 | Check PRT (Optional) | If Production Resources/Tools (PRTs) are assigned to the production order, you can check PRT details within this app.Select the order, and choose Order Schedule facet. Choose Settings for the Operations part, and make sure PRTs is selected in the View Settings. PRT hyperlink is available for the operations. |  |  |
| 7 | Check Long Text Copied from Planned Order (Optional) | If any long text is maintained for the planned order, you can check it in the converted production order.Select the order and choose Edit Order in the upper right corner.On the Production Order Change screen, choose tab Long Text, and check the text. | The long text maintained in the planned order is copied to the converted production order. |  |

|  |
| --- |
| Note You can use the following procedure when you want to monitor the uncovered requirements originating from production orders with the Monitor Internal Requirements (F0263A) app. Before continuing with the following procedure, make sure at least the stock of one component is less than the requested amount of the current production order.Under Component, select the check box of the material item for which you want to check details of the missing component. Choose Manage Requirements. The Manage Internal Requirements screen is displayed with the shortage material details. |

#### Material Staging for Final Assembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to stage materials for final assembly production.

|  |
| --- |
| Note If there is sufficient stock available in the production storage location, then no line items are generated. |

Prerequisite

Stock must be available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stage Materials for Production (MF60). | The Material Staging for Planned Orders screen displays. |  |
| 3 | Enter Details | Make the following entries and choose Execute.In the Staging Types section:SLoc Level: <select>Plant:3310Selection Horizon for Reqmts: <date must be in the future - after scheduled start date>On the Production/Process Orders tab:Order: <Production Order Number for finished Goods> | The Pull List: Storage Location Level screen displays. |  |
| 4 | Choose Replenishment Elements | In the Total Reqmts table, select the line items and choose Replenishment Proposal on the top of the screen.Review staged quantities and choose Replenishment Elements. |  |  |
| 5 | Enter Replenishment Storage Location and Batch NumberEnter Replenishment Storage Location | At the bottom half of the split screen, in the RepLoc column of the Replen. Element table, enter 331C for staged materials.Some materials require a batch number to be entered. Choose Batch/Stck Determination and check the proposed batch and quantity. Adopt if needed and confirm your selection with Copy. For example: RM122. |  |  |
| 6 | Stage and Save | Choose Stage and choose Save.Note Missing materials are transferred to the shop floor from the designated storage area.The shortage of raw material for final assembly production order is supplied with this step. | Material is staged for final assembly. |  |

#### Release Production Order for Final Assembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A release at order operation level results in the release of the order and all its operation. The order and the operations receive the REL (released) status.

Prerequisite

The production order created by the MRP controller is assigned a release date in accordance with the scheduling margin key.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). |  |  |
| 3 | Check Default Area of Responsibility (Supervisor) | Choose the user icon and select App Settings. Choose tab Production Supervisors.In the AOR Status column, choose the button to assign or unassign entries, and make sure only the following entries are assigned:Plant 1 AE (3310)MTO w/o VC - Val.(YB4)Choose Back. |  |  |
| 4 | Select Production Order | On the Manage Production Orders screen, choose Adapt Filters to display more filter options. In the Adapt Filters dialog box, select Material and Production Plant and choose OK.Enter the following filter criteria, and choose Go:Status: CreatedMaterial: FG126Production Plant: 3310 | The Material and Production Plant fields are added to the filter bar.Corresponding orders display. |  |
| 5A | Scenario A: In a typical case, you directly release the production order. | Select the order to be released.Choose Release in the top right corner. | The 1 of 1 orders have been released message displays and the order is released.Note If Release Order dialog box displays with message Non-Availability of Material, it means there is not sufficient stock stored for FG126's components.You can either choose Release Order in the dialog box to release order directly. Or you can choose to go back to the Create Initial Material Stock preliminary step to post more initial material stock. When enough material stock is posted, complete production order processing for semifinished goods, and then release production order for final assembly. |  |
| 5B | Scenario B: Release production order after releasing work production order from Rework Processing – Work-in-Process (BJQ) test script. | On the Manage Production Orders screen, choose Edit in the top right corner.On the Production order Change: Header screen, choose Menu > Functions > Release .Ensure REL displays in the Status field.Choose Save. | See Expected Result in step [5A](#unique_21). |  |

#### Check Serial Numbers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The finished goods material is managed with serial numbers. The system generates a serial number for each finished good when the production order is released. This process step shows you how to check the serial numbers.

Prerequisite

The serial number profile is defined in the material master record and the production order is released.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Production Order (CO03). |  |  |
| 3 | Enter the Number | Make the following entry and choose Continue:Order: <production order number for finished goods> | The Production Order Display: Initial Screen displays. |  |
| 4 | Navigate to Serial Number Screen | Choose Menu > Header > Serial Numbers on the top of the screen. | The Display Serial Number dialog box displays. |  |
| 5 | Check the Serial Number | In the Display Serial Numbers dialog box, the serial numbers generated during production order release are listed. Make a note of the serial numbers. |  |  |
| 6 | Back | Close the dialog box and choose the Back icon. |  |  |

#### Pick Components for Final Assembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to pick components for final assembly, which are not in the service stock at the assembly line. For picking, the warehouse manager selects the specific picking list that can be called up directly with the production order number. The warehouse manager has a series of further selection options for optimal worklist selection.

Prerequisite

Ensure there is sufficient amount of component in the service stock. To check the stock level, you can use the Inventory Manager user role to access the Display Stock Overview (MMBE) App.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Pick Components for Production Orders (CO27). | The Picking List: Initial Screen displays. |  |
| 3 | Enter Relevant Search Criteria | Make the following entries and choose Execute.Profile: <000002>Production Order: <production order for finished goods> | The Order Information System: Detail List of Components screen displays. |  |
| 4 | Picking | Select the relevant reservations and choose Picking. | A list of all the selected reservations displays. |  |
| 5 | Batch Determination | Some materials, such as RM122, are managed by batch numbers.Select relevant line item and choose Batch Determination to assign batch numbers. | The Batch Determination MM: Select Batches screen displays. |  |
| 6 | Enter Detail | Make the following entry and choose Copy:Split Quantity: <spilt quantity> |  |  |
| 7 | Post | Choose Post to post the goods movements. | The goods movements are posted. |  |

#### Confirm Production Operations for Final Assembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents include the processing status of orders, operations, sub-operations, and individual capacities. It is an instrument for controlling orders. This process step shows you how to use time event confirmation.

|  |
| --- |
| Note In a real business scenario, some operations produce scrap due to operational or component defects. If you want to activate this process, refer to Rework Processing – Work-in-Process (BJQ) test script. |

Prerequisite

The production order for finished goods is released.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). | The Enter Order and Operation screen displays. |  |
| 3 | Enter Production Order and Operation | On the Enter Order and Operation screen, make the following entries and choose Go:Order: <production order number for finished goods>Operation: <operation number>, for example, <0010> | The Confirm Production Operation screen displays. |  |
| 4 | Enter Quantities Data | In the Quantities section, make the following entries:Yield:<yield amount>Scrap:<scrap amount> |  |  |
| 5 | Check Material Movements | In the Material Movements section, check the material list. | The system displays an overview table of all materials for which the withdrawing is automatically done with the confirmation of the operation.If there are not any materials set for backflush (in material master), then no materials display in the table. |  |
| 6 | Enter Activities Data | In the Activities section, make the following entries:Setup: <setup time>Machine: <machine time>Labor: <labor time> |  |  |
| 7 | Save Your Entries | For partial confirmation, choose Post.For final confirmation, choose Post and Complete. | Confirmation is made. |  |
| 8 | Repeat Steps | Go back and repeat steps 3 to 7 for Operation<0020> and <0030>. | The final confirmation for the assembly order is made. |  |

#### Review Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display and check the production order for finished goods after its release or confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Operations (F2335) | The Manage Production Operations screen displays. |  |
| 3 | Select Production Order | On the Manage Production Operations screen, choose Adapt Filters to display more filter options.In the Adapt Filters dialog box, select Material and Production Plant and choose OK.Enter the following filters criteria and choose Go.Material: FG126Production Plant: 3310 | The Material and Plant fields are then added to filter bar.Selected order displays. |  |
| 4 | Check Detailed Operations Status | Check detailed information for selected production operations.Operation Issue:Empty if there is no production order issue.Delay or Missing Components / PRT issue or Quantity Deviation / Quality Issue information shows if relevant issue exists.Components:Material, total quantity and Issued / open quantity information for order components displays.Order Schedule:Detailed operation information with relevant work center, confirmed quantity, start and end time displays.Work Center Schedule:The relevant order covering the same work center capacity (operation is partially confirmed) displays.Operations not Started:The relevant order that would cover the same work center capacity (operation is released) displays.Confirmation:Detailed confirmation information with Yield, Scrap, Rework quantity displays if confirmation has been executed.Inspection:Detailed inspection lots information displays if existed. | Detailed operations status displays. |  |

#### Final Confirmation of Production Operations for Final Assembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to execute confirmations of all assembly activities of the production order before posting the goods receipt. The backflush is carried out together with the confirmation steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). |  |  |
| 3 | Enter Production Order and Operation | On the Enter Order and Operation screen, make the following entries and choose Go:Order: <production order number for finished goods>Operation:<last operation number>, for example, <0040>. |  |  |
| 4 | Enter Quantities Data | In the Quantities section, make the following entries:Yield: <yield amount>Scrap: <scrap amount> |  |  |
| 5 | Enter Activities Data | In the Activities section, make the following entries:Setup: <setup time>Machine: <machine time>Labor: <labor time> |  |  |
| 6 | Save Your Entries | Choose Post and Complete to make final confirmation for this operation. | The final confirmation of the last operation is made. |  |

#### Post Goods Receipt for Final Assembly Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods receipt for production order of final assembly.

|  |
| --- |
| Note If you enabled scope item Handling Unit Management (4MM), you can create handling units at the end of production and post goods receipts for handling units. By this way, the stock can be posted directly into storage and is available for picking. For details, refer to scope item 4MM. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Enter Goods Receipt Order | Choose Goods Receipt > Order in the header area and make the following entries:Order: <production order number for finished goods>GR goods receipt: <101>Document date: <default>Posting date: <default>On the General tab, next to the Printer icon, select Print via Output Control (mouseover) checkbox, and choose Individual Slip. |  |  |
| 4 | Enter Quantity | On the Quantity tab, confirm production order quantities.On the Where tab, enter the following entry:Storage Location: <331A (Std. storage 1)>On the Serial Numbers tab, select all the serials numbers for the yield quantities except the scrap ones. |  |  |
| 5 | Set Item OK and Post | Select the Item OK checkbox and choose Post. | The system displays the message Material document 500xxxxxxx posted. |  |

### Collective Orders

#### Create Planned Independent Requirements for FG130

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create Planned Independent Requirements (PIRs). PIRs are used to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split according to dates.

|  |
| --- |
| Note Instead of creating a single requirement, sometimes one or more planned independent requirements can be maintained and included in a requirement plan for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries and choose Go:Plant: 3310Period Indicator: Weekly(W) or Monthly(M)Version Active: Select all optionsMaterial: FG130 | The searched material item displays. |  |
| 5 | Edit PIRs | Select the material item and choose Edit in the upper right corner of the screen.On the screen, enter quantities per week, for example:PIR: <Quantity>, for example, <100>Make sure the version is active.Version Active: Yes |  |  |
| 6 | Save PIRs Draft | Choose Save in the bottom right corner of the screen. | The PIRs draft is saved. |  |

#### Material Requirements Planning at Plant Level for FG130

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use Material Requirement Planning (MRP) to tailor available capacities and receipts on time to suit requirement quantities. As a result, single-item multi-level requirement planning is performed for plant 3310.

Prerequisite

The Make-to-Stock finished goods are planned at plant level. There is now a requirement for FG130 in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirement Planning (MRP)Job Name: <MRP for FG130 >Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.For 3 Parameters section:Plant: 3310Material: FG130Changed BOM Components: selectPlanning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG130 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

#### Evaluate Stock/Requirements Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock/requirements situation for Make-to-Stock collective order finished goods (FG130) in the stock/requirements list after the requirement planning is performed.

Prerequisite

Requirement planning is carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 4 | Select Material | Search in the Material bar, select the following materials and then choose Manage Materials:Material: FG130Material: SG30 | The Manage Material Coverage screen displays. |  |
| 5 | Review Stock / Requirements List | Choose the corresponding material in the Materials list on the left side. | The detailed stock / requirements list for each material displays. |  |
| 6 | Display Planned Order | From the Materials list on the left side, choose the material for which you want to check for the planned order.Material: FG130Material: SG30On the right screen, choose PldOrd XXXX in the MRP Element column.Note The BOM explosion during the MRP run has generated dependent requirements for the demand-driven planned components. If there is not enough inventory to fulfill the requirements, planned orders and purchase requisitions are created for both inhouse-produced and externally-procured materials.Depending on the elements created in the MRP run, refer to Procurement of Direct Materials (J45) or Scheduling Agreements in Procurement (BMR) test scripts for processing externally-procured materials. | The selected planned order displays.Note The planned order is generated only when there is storage for these materials.If you want to display more information of the planned order, choose Document Info at the bottom of the dialog box. |  |

#### Conversion to Production Orders for Subassembly and Final Assembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Daily MRP run creates planned orders for goods to be produced internally. This process step shows you how to convert the planned orders to production orders for finished goods FG130 when you have reached the planned start date. Then the planned order from SG30 was changed to production order automatically.

Prerequisite

The MRP run has generated planned orders for SG30 (subassembly) and FG130 (final assembly).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A). | The Manage Material Coverage screen displays. |  |
| 3 | Select Material | Enter the following data and choose Go.Material: FG130Plant: 3310Shortage Definition: MRP Standard | The material item displays. |  |
| 4 | Find Planned Order | Check the material item and generated planned order.If no planned orders are generated, it could be because FG130 has sufficient amount of stock in store. In this case, remove some stock. Go back to create PIRs and run MRP again to generate planned orders. |  |  |
| 5 | Convert Planned Order to Production Order | Select Convert from Edit dropdown list in the Actions column for a planned order (PldOrd XXXX).In the Convert Planned Order XXXX dialog box, choose Convert to Production Order radio button, confirm date and quantity. Choose Convert. | The production order is created for FG130, and the production order is created for SG30 automatically. |  |

#### Review Material Availability Status for Production Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review material availability status for production orders.

Prerequisite

Production orders are created for subassembly and final assembly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). |  |  |
| 3 | Check Default Area of Responsibility (Supervisor) | Choose the user icon and select App Settings. Choose tab Production Supervisors.In the AOR Status column, choose the button to assign or unassign entries, and make sure only the following entries are assigned:Plant 1 AE (3310)MTS DI- Valuated (YB1)Choose Back. | The Manage Production Order screen displays. |  |
| 4 | Select Production Order | On the Manage Production Orders screen, choose Adapt Filters to display more filter options.In the Adapt Filters dialog box, select Material and Production Plant and choose OK.Enter the following filter criteria, and choose Go:Status: CreatedMaterial: FG130Production Plant: 3310 | The Material and Production Plant fields are added to the filter bar.The searched order displays. |  |
| 5 | Review Material Availability Status | In the Issue column, check the Component Issue icon to the right of the order to display the missing components.Repeat steps 4 to 5 for material SG30. | For FG130, the expected missing components are RM20, SG30. The raw materials are supplied after the Material Staging for Final Assembly step.For SG30, the expected missing components is RM124. The raw materials are supplied after the Material Staging for Final Assembly step.Note However, it’s also possible that SG30 is not a missing component for the final assembly production order. This happens when you have SG30 supplied (released production order for SG30 or unrestricted stock) already, but it's not yet reserved by any final assembly production orders. |  |

#### Material Staging for Subassembly and Final Assembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to stage materials for subassembly and final assembly production.

|  |
| --- |
| Note If there is sufficient amount of stock available in the production storage location, then no line items are generated. In this case, you can skip this step and proceed with the next one. |

Prerequisite

Stock must be available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stage Materials for Production (MF60). | The Material Staging for Planned Orders screen displays. |  |
| 3 | Enter Details | Make the following entries and choose Execute.In the Staging Types section:SLoc Level: <select>Plant: 3310Selection Horizon for Reqmts: <date must be in the future - after scheduled start date>On the Production/Process Orders tab:Order: <Production Order Number for Material SG30> | The Pull List: Storage Location Level screen displays. |  |
| 4 | Choose Replenishment Elements | In the Total Reqmts table, select the line items and choose Replenishment Proposal on the top of the screen.Review staged quantities and choose Replenishment Elements. |  |  |
| 5 | Enter Replenishment Storage Location and Stage Material | In the Replen. Element table, in the RepLoc column, enter 331C for staged materials.Choose Stage. |  |  |
| 6 | Save | Save your entries.Missing materials are transferred to the shop floor from the designated storage area.With this step, the shortage of material RM124 for subassembly production order is supplied. | Materials are staged for subassembly SG30. |  |
| 7 | Repeat material staging for finished goods FG130 | Go back and repeat steps 3 to 6 for finished goods FG130. | Materials are staged for subassembly FG130. |  |

#### Release Production Order for FG130

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A release at order operation level results in the release of the order and all its operation. The order and the operations receive the REL (released) status. Release for production order of Finished Good FG130, then the Production Order for Subassembly SG30 is released to production automatically.

Prerequisite

The production order created by the MRP controller is assigned a release date in accordance with the scheduling margin key.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). |  |  |
| 3 | Check Default Area of Responsibility (Supervisor) | Choose the user icon and select App Settings. Choose tab Production Supervisors.In the AOR Status column, choose the button to assign or unassign entries, and make sure only the following entries are assigned:Plant 1 AE (3310)MTS DI - Valuated (YB1)Choose Back. |  |  |
| 4 | Select Production Order | On the Manage Production Orders screen, choose Adapt Filters to display more filter options. In the Adapt Filters dialog box, select Material and Production Plant and choose OK.Enter the following filter criteria, and choose Go:Status: CreatedMaterial: FG130Production Plant: 3310 | The Material and Production Plant fields are added to the filter bar.Corresponding orders display. |  |
| 5 | Edit production order of FG130. | Select the order to be released.Choose Edit Order in the top right corner. | The Structure of Collective order XXXX screen displays. The structure of production order of FG130 and production order of SG30 can be checked here. |  |
| 6 | Directly release the production order. | Choose the first line: production order of FG130, and click Read Order. Check details of production order of FG130, then click Back to go back screen Production Order Change: Collective Order OverviewChoose the first line: production order of FG130, and click Release Order (green flag).Choose Save. | The Release carried out message displays and the Production order of Finished Good FG130 is released. The Production Order for Subassembly SG30 is released to production automatically. |  |

#### Confirm Production Operations for SG30 and FG130

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents include the processing status of orders, operations, sub-operations, and individual capacities. It is an instrument for controlling orders. This process step shows you how to use time event confirmation.

Prerequisite

The production orders for subassembly SG30 and finished goods FG130 are released.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Order Operation (CO11N). | The Enter Time Ticket for Production Order screen displays. |  |
| 3 | Enter Production Order and Operation | On the screen, make the following entries and choose Enter:Order: <production order number for subassembly SG30>Confirm.type: Final confirmation, | The order number displays. |  |
| 4 | Enter Quantities Data | In the Quantities section, make the following entries and press Enter:Yield: <yield amount>Scrap: <scrap amount> |  |  |
| 5 | Check Material Movements | Choose Goods Movements, and check the material list. | The system displays an overview table of all materials for which the withdrawing is automatically done with the confirmation of the operation.If there are not any materials set for backflush (in material master), then no materials display in the table. |  |
| 6 | Enter Activities Data | Choose Back.In the Activities section, make the following entries:Setup: <setup time>Machine: <machine time>Labor: <labor time> |  |  |
| 7 | Save Your Entries | Choose Save. | Confirmation is made. |  |
| 8 | Repeat confirmation for finished goods FG130 | Go back and repeat steps 3 to 7 for Operation<0010>, <0020> and <0030> for finished goods FG130. | The final confirmation for the finished goods order is made. |  |

#### Post Goods Receipt for Final Assembly Production Order FG130

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods receipt for production order of final assemblyFG130. Then the goods receipt for SG30 would be post automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Enter Goods Receipt Order | Choose Goods Receipt > Order in the header area and make the following entries:Order: <production order number for finished goods FG130>GR goods receipt: <101>Document date: <default>Posting date: <default>On the General tab, next to the Printer icon, select Print via Output Control (mouseover) checkbox, and choose Individual Slip. |  |  |
| 4 | Enter Quantity | On the Quantity tab, confirm production order quantities.On the Where tab, enter the following entry:Storage Location: 331A (Std. storage 1) |  |  |
| 5 | Set Item OK and Post | Select the Item OK checkbox and choose Post. | The system displays the message Material document 500xxxxxxx posted.The goods receipt for production order of final assembly FG130 is posted. The goods receipt for SG30 is post alongside automatically. |  |

### Check PIR Quality (Optional)

You can check the PIR accuracy in this chapter after the finished goods FG126 has been sold from stock to customers.

#### Sell from Stock for FG126

After posting goods receipt for finished goods FG126, you can sell it from stock, please refer to scope item BD9 - Sell from Stock to complete the sales procedure.

Pay attention to record sales order quantity in following step:

- Create Sales Order

#### Check PIR Quality

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check PIR accuracy.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries and choose Go:Plant: 3310Period Indicator: Weekly(W) or Monthly(M)Version Active: Select all optionsMaterial: FG126 | The searched material item displays. |  |
| 5 | Check Accuracy | On the Material screen, check the PIRs, Withdrawal Quantity, Sales Quantity, Accuracy, Proposed PIRs, Accuracy (Proposed PIRs) in Planning Data area.The Sales Quantity for each period is the sales order quantity created in the step [Sell from Stock for FG126](#unique_38) [page ] 55. | Accuracy = (PIRs + Withdrawal Quantity) / Sales Quantity |  |

### Review Scrap Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review the scrap report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Material Scrap - Maximum Deviation (F2035). | The Material Scrap screen displays. |  |
| 3 | Investigate Scrap | Materials Scrap can be displayed by various filters.You could choose the corresponding material in Chart to display the details. |  |  |

### Review Manufacturing Object Pages

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review different object pages available for different roles in the manufacturing process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner.Note You can use any role in section Roles above. | The SAP Fiori launchpad displays. |  |
| 2 | Search Material | Choose the Search icon in the upper right part of the screen.Make the following entries and choose Search:Search: <BOM Header Material>, refer to section Master Data, Organizational Data, and Other Data. | The system displays a list of objects using the selected material. |  |
| 3 | Display Object | In the All field, select an object from the dropdown list and choose the Search icon. | The displaying list of objects is limited to the object type selected. If no object is selected, a message would display instead. |  |
| 4 | Tailor the Result Display | Under the search line, choose an icon (for example, filter, display as table, sort and so on) to filter the results list. | The results list is filtered according to your selections. |  |
| 5 | Repeat Steps | Repeat steps 1 to 5 for any other role in this test script and any other object offered in the search function. | The result list of objects displayed differs by the role you use to log on. |  |

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Decoupling Processes Carried out During Confirmation (Optional) | When you carry out a confirmation, processes are triggered that could negatively affect the response time of the confirmation process. For example, goods movements and actual costs determination.You alleviate this situation by decoupling these processes from the actual confirmation.Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:Manage Your Solution:Log on to the SAP Fiori Launchpad in the SAP S/4HANA Cloud Public Edition system with the business role Configuration Expert - Business Process Configuration.Log on to the SAP Fiori Launchpad in the SAP S/4HANA Cloud Public Edition system as a Configuration Expert - Business Process Configuration.Navigate to the Manage Your Solution (F1241) app and choose Configure Your Solution.On the Configure Your Solution screen, search for the following configuration step: Define Time for Confirmation Processes and Define Confirmation Parameters.In the search result, choose the configuration activity and go to the next screen.Choose Configure of the corresponding step in the Configuration Steps area.SAP Central Business Configuration:Log on to the project experience in SAP Central Business Configuration.Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Time for Confirmation Processes, Define Confirmation Parameters.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.To post these confirmation processes, you can access the Schedule Posting of Predefined Confirmation Processes (F5255) app as a Production Supervisor - Discrete Manufacturing. You use the app to define which processes are to be executed in the job. As a general guide:Automatic goods receipts should be processed soon after the actual confirmation. This applies to materials that are processed further or that are needed in Sales, for which it is particularly important that stock levels are kept up-to-date. Processing should be online or executed as an update task.Backflushing withdrawals can be processed in longer periods (for example twice a day). Since the material has already been withdrawn physically from the storage location, stock levels are not as important. However, other consumers of the material and material requirements planning should be notified.Actual costs determination can take place less frequently (for example once a day). Actual costs determination is not important for smooth production processing. It is needed for controlling and should be adapted to the demands of this department. |
| Technical Completion of Production Order (Optional) | You can access the Schedule Order Technical Completion Run (F3841) app as a Production Supervisor - Discrete Manufacturing to schedule a job to set production orders as Technical Completion.If you need to set a production order to Technical Completion separately, you can access the Manage Material Coverage - New Version (F0251A) app as a Production Planner, find your production order and select Delete.Note This functionality is only available if the production order hasn’t yet been confirmed. |
| 3F0 (Event-Based Production Cost Posting) | This procedure updates work-in-process calculation, overhead calculation, and variance calculation by linking the posting to the events.Note Start from CE2105, the default Best Practice content is based on event-based result analysis for new customer install and add new country only, rather than previous period-end posting. For existing customers (who activated content before 2105), the default remain unchanged to Period-End Closing – Plant BEI till customer makes the decision to switch. For migration to Event based from Periodic please refer [Production Settlement in Parallel Ledgers](https://help.sap.com/viewer/4032610758dc437089f0c28320eec93f/LATEST/en-US/e49a3770f22547a392455154f3eef6e2.html). If you are still using period-end posting, you may need to refer to non-standard Scope Item BEI - Period-End Closing – Plant. |
| Close Confirmed Production/Process Orders (Optional) | Search for Schedule Order Closing Runs - Close Production/Process Orders (F4305) app as a Production Supervisor - Discrete Manufacturing to schedule a job to set orders as Closed (CLSD). |
| Plant Management Overview (Optional) | To analyze your Plant Data, you can make use of the Fiori app Plant Management Overview - Old Version (F3020). As a Plant Manager you can get information about following topics from an overview page:Inspection Lots with Defects, Top Defective MaterialsIdentification of stock value by stock types or special stock types |

### Document Integration

You can create fixed links between orders and documents in the Document Management System (DMS). This ensures that the correct document versions are supplied during the production process. In addition, this also allows you to keep track of which documents were used to produce a certain order.

Only documents of type SPP can be assigned to the production order. Documents are defined in the Manage Documents app or the Create Document app.

Display Outputs of the Order

A menu option is available to display the print files of the order. Choose More > Order > Output > Manage Output Items . A list of all available outputs is displayed.

If a business document contains attachments, you can include all or some of these in the output. For every output item, you can see the number of selected attachments and the number of available attachments.

To add attachments to an output item, select these numbers to display a list of all the available attachments. Once you save your changes, the numbers are updated. You can merge PDF attachments along with the rendered form into a single PDF document, if the print queue format is PDF.

### Production Resources Tools

Starting with SAP S/4HANA Cloud Public Edition2102, Create Production Resources/Tools - MDS functionalities are available with both applications and Self-Service Configuration UIs.

Unlike machines and fixed assets, PRTs are movable (not stationary) operating resources that are required to perform an activity and can be used repeatedly.

There are several categories of Create Production Resources/Tools - MDS available. The category determines the characteristics and business functions that a PRT can have.

With SAP S/4HANA Cloud Public Edition2102 you can use the following PRT types, refer to Create Production Resources/Tools - MDS master data script to create your own PRTs:

- Material PRT
- Document as PRT
- Miscellaneous PRT

With SAP S/4HANA Cloud Public Edition2111, the PRT below is also enabled:

- Equipment PRT

You can assign different types of Create Production Resources/Tools - MDS to the task lists and production orders for which they are required. PRTs assigned to the task list are automatically copied to the production order.

Also, you can analyze the usage of the Create Production Resources/Tools - MDS in the production orders.

### Additional Functional Information

If you want to know functional information for Discrete and Process Manufacturing beyond what is described in the test scripts of the best practice scope items for SAP S/4HANA Cloud Public Edition, you could check SAP Note [3441318](https://me.sap.com/notes/3441318).

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
> Flagged while digesting this document, not verified: Internal inconsistency: the Release Production Order for Final Assembly step (FG126) says to assign only AOR entry 'MTO w/o VC - Val.(YB4)', whereas every other supervisor AOR check in the script (including the FG126 availability review) assigns 'MTS DI - Valuated (YB1)'.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Internal inconsistency: the Overview Table lists Manage Production Orders (F2336) for the Review Production Order step, but the procedure itself opens Manage Production Operations (F2335).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/test-script-make-to-stock-production-repetitive-manufacturing-bjh-ae-s]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BJ5_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 108,317 chars in the whole document
