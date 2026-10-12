---
id: 12-production-and-manufacturing/test-script-demand-driven-buffer-level-management-1y2-ae-sap-s-4hana-c
title: "Test Script: Demand-Driven Buffer Level Management (1Y2_AE) - SAP S/4HANA Cloud Public Edition (1Y2_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud 2608 test script for scope item 1Y2 (AE): demand-driven buffer positioning, buffer sizing and buffer level management, plus pMRP use cases."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/demand-driven-replenishment]
aliases: [1Y2_S4CLD2608_BPD_EN_AE]
keywords: [Demand-Driven Replenishment (DDMRP), demand-driven replenishment, buffer positioning, product classification, decoupled lead time, buffer sizing, buffer proposal calculation, buffer levels, buffer profiles, predictive mrp]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1Y2_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-784
topic: 12-production-and-manufacturing/demand-driven-replenishment
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Demand-Driven Buffer Level Management (1Y2_AE) - SAP S/4HANA Cloud Public Edition (1Y2_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1Y2_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Demand-Driven Replenishment (DDMRP)** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Demand-Driven Buffer Level Management (1Y2_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232848452)

[2 Prerequisites 4](#_Toc232848453)

[2.1 System Access 4](#_Toc232848454)

[2.2 Roles 4](#_Toc232848455)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232848456)

[2.4 Business Conditions 8](#_Toc232848457)

[2.5 Preliminary Steps for Main Scenario 8](#_Toc232848458)

[2.5.1 Check Buffer Level Status 8](#_Toc232848459)

[2.5.2 Create Initial Data (Optional) 9](#_Toc232848460)

[2.5.2.1 Create Initial Stock for Buffered Products 10](#_Toc232848461)

[2.5.2.2 Post Goods Issue for Buffered Products 11](#_Toc232848462)

[2.5.2.3 Maintain PIRs for Components 12](#_Toc232848463)

[3 Overview Table 14](#_Toc232848464)

[4 Test Procedures 16](#_Toc232848465)

[4.1 Main Scenario 16](#_Toc232848466)

[4.1.1 Buffer Positioning 16](#_Toc232848467)

[4.1.1.1 Schedule Product Classification 16](#_Toc232848468)

[4.1.1.2 Mass Maintenance of Products 19](#_Toc232848469)

[4.1.1.3 Check Buffer Positioning 21](#_Toc232848470)

[4.1.2 Buffer Sizing 24](#_Toc232848471)

[4.1.2.1 Schedule Lead Time Classification of Products 24](#_Toc232848472)

[4.1.2.2 Buffer Profile Maintenance (Optional) 27](#_Toc232848473)

[4.1.2.3 Schedule Buffer Proposal Calculation 29](#_Toc232848474)

[4.1.2.4 Manage Buffer Levels 31](#_Toc232848475)

[4.2 Use Cases(Optional) 35](#_Toc232848476)

[4.2.1 Use Case A: Buffer Positioning – Inbound Protection 35](#_Toc232848477)

[4.2.1.1 Schedule Product Classification 35](#_Toc232848478)

[4.2.1.2 Initialize MRP Type 35](#_Toc232848479)

[4.2.1.3 Buffer Positioning - Inbound Protection 35](#_Toc232848480)

[4.2.2 Use Case B: Use pMRP for ADU Calculation 37](#_Toc232848481)

[4.2.2.1 Maintain PIRs for Finished Goods 37](#_Toc232848482)

[4.2.2.2 Schedule pMRP Simulation Creation 39](#_Toc232848483)

[4.2.2.3 Process pMRP Simulations 40](#_Toc232848484)

[4.2.2.4 Check PIRs for Components 41](#_Toc232848485)

[5 Appendix 43](#_Toc232848486)

[5.1 Succeeding Processes 43](#_Toc232848487)

[5.2 Related APIs and Communication Arrangements 43](#_Toc232848488)

## Purpose

Overview

Demand-driven replenishment (DD) helps to plan and manage supply chains efficiently based on customer demand, rather than through traditional MRP procedures. It forms the basis for a reliable material flow by defining buffers at strategically important points and adjusting these buffers regularly.

Products at all Bill-of-Material (BoM) levels are classified based on average demand, lead time, BoM usage, and variability to identify if they are relevant for demand-driven replenishment. A well-balanced buffer level is proposed for DD-relevant products to ensure that they are sufficiently stocked to meet average demand, but in low enough quantities to prevent excessive storage costs or losses due to expiry. An app helps planners manage safety stock, reorder point, and maximum stock through the buffer level proposals. To support the calculation of buffer levels, predictive material and resource planning (pMRP) can be deployed.

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
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | F-10A | FIN10A, MTS-DDMRP,PD |  |
| Material | F-10B | FIN10B, MTS-DDMRP,PD |  |
| Material | S-201 | SEMI201,MTS,D1,Subassembly |  |
| Material | S-202 | SEMI202,MTS,D1 |  |
| Material | S-301 | SEMI301,MTS,PD,Subassembly |  |
| Material | R-302 | RAW302, PD |  |
| Material | R-401 | RAW401, D1 |  |
| Material | F-20A | FIN20A, MTS-DDMRP,PD |  |
| Material | S-210 | SEMI210,MTS,PD,Subassembly |  |
| Material | S-310 | SEM310,MTS,PD,Subassembly |  |
| Material | R-410 | RAW410, PD |  |
| Material | R-412 | RAW412, PD |  |
| Material | S-208 | SEMI208,MTS,PD,Subassembly |  |
| Material | S-315 | SEM315,MTS,PD,Subassembly |  |
| Material | R-411 | RAW411, PD |  |
| Material | R-311 | RAW311, PD |  |
| Plant | 3310 | Plant 1 AE |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 001 | Group 001 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |

Bill of Material Structure

This overview shows the bill of material structure and the usage of each component if you have activated all optional enhancements.

| Material | Level | Material Type | Unit | Characteristics of Material | Optional Enhancements |
| --- | --- | --- | --- | --- | --- |
| F-10A | 0 | FERT | PC | Finished goods |  |
| S-201 | 1 | SEMI | PC | Semi-finished goods as decoupling point |  |
| S-301 | 2 | SEMI | PC | Semi-finished goods as decoupling point |  |
| R-401 | 3 | RAW | PC | External procured |  |
| R-302 | 2 | RAW | PC | External procured |  |
| S-203 | 1 | SEMI | PC | Stock transfer material |  |
| F-10B | 0 | FERT | PC | Finished goods |  |
| S-201 | 1 | SEMI | PC | Semi-finished goods as decoupling point |  |
| S-301 | 2 | SEMI | PC | Semi-finished goods as decoupling point |  |
| R-401 | 3 | RAW | PC | External procured |  |
| R-302 | 2 | RAW | PC | External procured |  |
| S-202 | 1 | SEMI | PC | Semi-finished goods as decoupling point |  |

| Material | Level | Material Type | Unit | Characteristics of Material | Optional Enhancements |
| --- | --- | --- | --- | --- | --- |
| F-20A | 0 | FERT | PC | Finished goods |  |
| S-210 | 1 | SEMI | PC | Semi-finished goods |  |
| S-310 | 2 | SEMI | PC | Semi-finished goods |  |
| R-410 | 3 | RAW | PC | External procured |  |
| R-412 | 3 | RAW | PC | External procured |  |
| S-208 | 1 | SEMI | PC | Semi-finished goods |  |
| S-315 | 2 | SEMI | PC | Semi-finished goods |  |
| R-411 | 3 | RAW | PC | External procured |  |
| R-311 | 2 | RAW | PC | External procured |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) (MDS):

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

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation | You have completed the step described in the Test Script Standard Cost Calculation (BEG) |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up-to-date. |

### Preliminary Steps for Main Scenario

#### Check Buffer Level Status

Purpose

This process step shows you how to identify whether it is the first time to run DDMRP scenario.

If yes, then proceed with preliminary step [Create Initial Data (Optional)](#unique_8) [page ] 9 to create transaction data for buffered products.

If no, then skip preliminary step [Create Initial Data (Optional)](#unique_8) [page ] 9.

Buffered product is a product or component for which the stock is dynamically managed using buffer levels based on green, yellow and red buffer zones.

Buffer level is a properly managed buffer which ensures that a product or component is sufficiently stocked to meet average demand, but in low enough quantities to prevent excessive storage costs or losses due to expiry.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Buffer Levels (F2706). | The Manage Buffer Levels (F2706) screen displays. |  |
| 3 | Filter Product | On the Manage Buffer Levels (F2706) screen, filter by product and choose Go.Editing Status: AllProposal Status: <ALL>Product: S-201; S-202; R-401Plant: 3310Max Stock Deviation: <Blank> | If you are the first tester, please kindly maintain Area of Responsibility as 'Plant 1 AE (3310)' |  |
| 4 | Check Buffer Level Status | In the Buffers list, check whether buffer level results of 3 DD-relevant products display.A. If the product is missing, this is the first time to test the scenario for such product, so there is no transaction data in system now, proceed to preliminary step [Create Initial Data (Optional)](#unique_8) [page ] 9 to create transaction data for DD-relevant products (buffered products).B. If all products display, then it is not the first time to test scenario, skip preliminary step [Create Initial Data (Optional)](#unique_8) [page ] 9. | If there is no result displayed in the system, first confirm whether the Area of Responsibility is correctly maintained as plant 3310.Choose User > App Settings , and then the Area of Responsibility screen displays. |  |

#### Create Initial Data (Optional)

Purpose

This process step shows you how to create initial data for Demand-Driven Replenishment products (DD-relevant products/buffered products) to calculate average daily usage.

1. Average daily usage (ADU) is defined as average usage of a product or component on a daily basis, calculated based on the demand over a selected averaging interval. It is the average quantity for goods issue of a specific product in the horizon days.
2. Buffered products are products for which the stock is dynamically managed using buffer levels based on green, yellow and red buffer zones.

In our scenario, we assume R-401 is a buffered product with only historical consumption data, so we create initial stock and post goods issue for it.

We also assume S-201 is a new buffered product without any historical data, so we maintain PIRs in the future.

We also assume S-202 is a buffered with both historical consumption value and future PIRs, so we create initial stock and post goods issue and maintain PIRs for it.

If there is no goods issue posted during the horizon days for past or no PIRs during the horizon days for future, then ADU equals to zero, and it could impact the results of buffer level calculation.

##### Create Initial Stock for Buffered Products

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create initial stock for buffered products S-202 & R-401.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Specify Material | Make the following entries and press Enter:Material: S-202Plant: 3310 | The Stock overview for the product displays. |  |
| 4 | Select Stock | On the screen, you can check Storage Location, Unrestricted-Use Stock, Blocked Stock, and Stock in Quality Inspection.Choose Unrestricted - Use Stock icon for relevant storage location.Storage Location : 331B | If current quantity for S-202 in storage location 331B is enough, then skip step 5.The storage location is 331B for SXX and 331C for RXX products. |  |
| 5 | Enter Parameters | Make the following entries and choose Post:Document Date: <Today’s date - 1 Day>Posting Date: <Today’s date - 1 Day>Stock Change: Initial EntryQuantity: <Quantity>, for example, 200 | The system displays the following message. The stock has been added.1 document has been created: Material Document XXXXXXXXXX/20XXAdjust the Quantity value to ensure the updated Unrestricted-Use Stock quantity for buffered products S-202 is 200. |  |
| 6 | Create Initial Stock for Other Materials | Repeat steps 3-7 for following materials.Material: R-401 | The storage location is 331C for RXX products. |  |

You can either post initial stock directly to the storage location or refer to test scripts Procurement of Direct Materials (J45) or Scheduling Agreements in Procurement (BMR).

##### Post Goods Issue for Buffered Products

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create goods issue for buffered products S-202 & R-401 for average daily usage calculation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Post Goods Movement (MIGO) screen displays. |  |
| 3 | Choose Goods Issue-Other | Make the following entries:Trans./Event: Goods IssueReference Document: Other |  |  |
| 4 | Specify Material | Make the following entries and press Enter:Document Date : <Today’s date - 1 Day>Posting Date: <Today’s date - 1 Day>Movement type: 201Material: S-202Quantity: <Quantity>, for example, 100Plant: 3310Storage Location: 331B for S-XX and 331C for R-XX products. | Make sure that the quantity shall never be larger than the on-hand stock level. |  |
| 5 | Enter Cost Center | On the Account Assignment tab:Cost Center : <Cost Center> - you can search with company code 3310, and choose cost center, for example, 33101301 |  |  |
| 6 | Check | Choose Check. | Document is ok. |  |
| 7 | Post | Choose Post. | Material document XXX posted. |  |
| 8 | Post Goods Issue for Other Materials | Repeat steps 3-7 for following materials.Material: R-401 |  |  |

##### Maintain PIRs for Components

Purpose

This process step shows you how to create PIRs for buffered products S-201 & S-202 for average daily usage calculation.

You can either choose option 1 or option 2.

Option 1: Use Case C

Use pMRP for ADU calculation, the PIRs could be automatically generated for S-201 & S-202.

Option 2: Manually Maintain PIRs

In this option, the PIRs are manually created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Weekly (W)Version Active: Select all optionsSearch: S-201; S-202 |  |  |
| 5 | Filter Result | Choose Go to execute. | The material item displays. |  |
| 6 | Edit PIRs | Select the material item, and choose Edit in the upper-right corner.On the screen, enter quantities per period, for example:PIR for S-201: 70 for next 3 periodsPIR for S-202: 70 for next 3 periodsMake sure the version is active.Version Active: Yes |  |  |
| 7 | Save PIRs | Choose Save at bottom right. | The PIRs are saved. |  |

## Overview Table

The scope item Demand-Driven Buffer Level Management (1Y2) consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Main Scenario |  |  |  |
| Buffer Positioning |  |  |  |
| [Schedule Product Classification](#unique_13) [page ] 16 | Production Planner | Schedule Product Classification (DD) (F2823) | Execute classification calculation for value, BoM usage and variability. |
| [Mass Maintenance of Products](#unique_14) [page ] 19 | Production Planner | Mass Maintenance of Products (DD) (F2825) | Check classification results for Demand-Driven replenishment products. |
| [Check Buffer Positioning](#unique_15) [page ] 21 | Production Planner | Buffer Positioning (F3282) | Monitor and decide which products to buffer and unbuffer by checking buffer analysis. |
| Buffer Sizing |  |  |  |
| [Schedule Lead Time Classification of Products](#unique_16) [page ] 24 | Production Planner | Schedule Lead Time Classification of Products (DD) (F2871) | Execute classification calculation for lead time. |
| [Buffer Profile Maintenance (Optional)](#unique_17) [page ] 27 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | Execute buffer proposal calculation. |
| [Schedule Buffer Proposal Calculation](#unique_18) [page ] 29 | Production Planner | Schedule Buffer Proposal Calculation (F2837) | Execute buffer proposal calculation. |
| [Manage Buffer Levels](#unique_19) [page ] 31 | Production Planner | Manage Buffer Levels (F2706) | Check buffer levels with current& proposed results for buffered product. |
| Use Cases (Optional) |  |  |  |
| Use Case A: Buffer Positioning – Inbound Protection |  |  |  |
| [Schedule Product Classification](#unique_20) [page ] 35 | Production Planner | Schedule Product Classification (DD) (F2823) | Execute classification calculation for value, BoM usage and variability. |
| [Initialize MRP Type](#unique_21) [page ] 35 | Production Planner | Mass Maintenance of Products (DD) (F2825) | Initialize some special products as unbuffered products. |
| [Buffer Positioning - Inbound Protection](#unique_22) [page ] 35 | Production Planner | Buffer Positioning (F3282) | Monitor and decide which products to buffer and unbuffer by checking buffer analysis. |
| Use Case B: Use pMRP for ADU Calculation |  |  |  |
| [Maintain PIRs for Finished Goods](#unique_23) [page ] 37 | Production Planner | Maintain PIRs (F3445) |  |
| [Schedule pMRP Simulation Creation](#unique_24) [page ] 39 | Production Planner | Schedule pMRP Simulation Creation (F3968) |  |
| [Process pMRP Simulations](#unique_25) [page ] 40 | Production Planner | Process pMRP Simulations (F3934) |  |
| [Check PIRs for Components](#unique_26) [page ] 41 | Production Planner | Maintain PIRs (F3445) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

|  |
| --- |
| Note Materials with the status where MRP message is set to A (warning) or B (error) will be excluded from the following jobs and apps. If you have no results generated when using the following Demand-Driven apps, clarify the material status.Schedule Product Classification (DD) (F2823)Mass Maintenance of Products (DD) (F2825)Buffer Positioning (F3282)Schedule Lead Time Classification of Products (DD) (F2871)Schedule Buffer Proposal Calculation (F2837)Manage Buffer Levels (F2706) |

### Main Scenario

#### Buffer Positioning

This process step shows you how to calculate three kinds of classification to make strategic buffer positioning for demand-driven replenishment materials.

In other words, we could check the classification results to decide whether a material shall be positioned as a buffered product.

In our current standard scenario, to ease your understanding and testing complexity, we have set three materials S-201 (in-house production), S-202 (external procurement) and R-401 (external procurement) as buffered products by default.

If you want to make strategic buffer positioning and adjust buffered or unbuffered product, please adopt change for specific products,F-20A,S-210,S-310,R-410,R-412,S-208,S-315,R-411,R-311 in [Use Case A: Buffer Positioning – Inbound Protection](#unique_29) [page ] 35.

##### Schedule Product Classification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to classify your products by systematically evaluating them based on their goods issue value (ABC classification), usage across BOMs (PQR classification) and variation in actual demand (XYZ classification) across a specified evaluation interval. Classifying your products helps identify whether they are relevant for Demand-Driven Replenishment, and define inputs for their buffer settings. Additionally, you can schedule runs to reclassify your products periodically to keep their classifications up-to-date, so that you get accurate results as you proceed with Demand-Driven Replenishment.

- Classification type 1: Value (ABC, A for high, B for medium, C for low)

Value is the percentage radio of absolute value for the specific material to whole absolute value in the plant. (Absolute value is relevant with price and consumption in past several days)

- Classification type 2: Variability (XYZ, X for low, Y for medium, Z for high)

XYZ Classification: Classifying a product or component into type X, Y or Z based on the variation in its goods issue value, with products classified as type X having the lowest variation and products classified as type Z having the highest variation.

Variability is the coefficient of variation for consumption, which is the percentage radio of sample standard deviation to sample mean of daily consumption in past several days.

- Classification type 3: BoM Usage (PQR, P for high, Q for medium, R for low).

PQR Classification: Classifying a product or component into type P, Q or R based on its usage in BOMs, with products classified as type P being used in the highest number of BOMs and products classified as type R being used in the lowest number of BOMs.

BoM usage is the number that the product works as the BoM component.

You can use SSCUI Assignment of Profile for Goods Issue Selection (DD) to refine flexible classification with goods issue exclusion profile.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Product Classification (DD) (F2823). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create to create a new application job. | The New Job screen displays. |  |
| 4 | Enter Job Details | In the Template Selection area, enter the following entries:Job Template: Product Classification for Demand- Driven ReplenishmentJob Name: Product Classification for Demand- Driven Replenishment |  |  |
| 5 | Define Recurrence Pattern | Choose Step 2.In the 2. Scheduling Option area, maintain the following entries:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries and choose OK.Start Immediately: XRecurrence Pattern: Single Run | The Scheduling Information screen displays. |  |
| 6 | Enter Selection Criteria | Choose Step 3.In the 3. Parameters area, make the following entries.For Selection Criteria subarea:Product: S-201, S-202, R-401Plant: 3310Number of Days (Past): for example, 10 | As product S-201 is new material with no historical data, thus classification of value and variability for product S-201 could have some problem, please just ignore the error. |  |
| 7 | Enter Parameters | In the Parameters subarea, make the following entries:I. Thresholds for Value (ABC) ClassificationUsage Values in %: X (if unmarked, then Value (ABC) Classification parameter can’t be maintained)A (High): for example, 70B (Medium): for example, 20C (Low): for example, 10II. Thresholds for BoM Usage (PQR) ClassificationBOM Usage: X (if unmarked, then PQR parameter can’t be maintained)Exclude Alternate BOM: X (if unmarked, then alternate BOM will be considered)P (High): for example, 3Q (Medium): for example, 2R (Low): maintained by default and unchangedIII. Thresholds for Variability (XYZ) ClassificationCoefficient of Variation: X (if unmarked, then XYZ parameter can’t be maintained)X (Low): for example, 0.2Y (Medium): for example, 0.5Z (High): Maintained by default and unchangedExclude Non Goods Issue Days: BlankIV. Job ParametersExcl. Mnlly.Classified Prods.: BlankMaintain Logs: XParallel Processing: Blank | You could adjust the classification parameters with the real business requirement.The parameter values you enter here are all thresholds for classification calculation.If you enable Exclude Non Goods Issue Days, then non-goods issue days will be exclusive for XYZ classification.If you enable Excl. Mnlly.Classified Prods, then manually classified products will be exclusive for product classification. |  |
| 8 | Schedule New Job | Then choose Check. If there are no error messages, choose Schedule.A new job is created and displayed in the Application Jobs table. | If there is any error like No per day consumption data found for material XXX, please ensure you have transaction data in past period (as you entered, for example 10 days). If there is no transaction data in the specific period, please refer to preliminary step [Create Initial Data (Optional)](#unique_8) [page ] 9 to execute.Note If you run product classification for bulk materials or phantom assembly, you could receive warnings like X products excluded from run due to phantom assembly and bulk, as they are meaningless to be buffered candidates. |  |

##### Mass Maintenance of Products

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display and change product details (master data records) relevant to Demand-Driven Replenishment. After you have classified or reclassified your products, you can view the results of the classifications in this app, decide whether the material is relevant for strategic stock positioning. You can use the mass change feature to change the master data records for several products simultaneously.

ABC Classification: Classifying a product or component into type A, B or C based on its goods issue value, with products classified as type A having the largest goods issue value and products classified as type C having the smallest goods issue value.

XYZ Classification: Classifying a product or component into type X, Y or Z based on the variation in its goods issue value, with products classified as type X having the lowest variation and products classified as type Z having the highest variation.

PQR Classification: Classifying a product or component into type P, Q or R based on its usage in BOMs, with products classified as type P being used in the highest number of BOMs and products classified as type R being used in the lowest number of BOMs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Mass Maintenance of Products (DD) (F2825). | The Mass Maintenance of Products (DD) screen displays. |  |
| 3 | Filter Product | On the Mass Maintenance of Products (DD) screen, filter by product and choose Go.Product: R-401Plant: 3310 | Note In real business scenario, customer could adapt the filter conditions, for example filter by classification results or filter by candidates of buffered products, then you could decide whether the material is relevant for strategic stock positioning.If yes, then change the MRP type into D1 for such material and proceed the [Buffer Sizing](#unique_30) [page ] 24 chapter .In our best practice scenario, we have already set S-201, S-202, S-203 & R-401 as buffered products (with MRP type D1) by default, you could just check the classification results for them in this activity, and proceed the [Buffer Sizing](#unique_30) [page ] 24 chapter later. |  |
| 4 | Check Classification Results | In the Products area, check the classification results.The Value Indicator, Variability Indicator, DLT Indicator, BOM Usage Indicator, and MRP Type for the products display. | You could choose the Settings icon to adjust the displayed columns. If you are the first tester, the DLT Indicator could remain unclassified. |  |
| 5 | Mass Change Classification Results | Check the classification results for filtered products.Choose the indicator for the products, and choose Edit. The Edit screen displays.You can change the parameters for Product, Classification, Lead Time, and Product Specific Spike Parameters.For Classification, you can change the parameters such as Value Indicator, Variability Indicator, DLT Indicator, and BOM Usage Indicator.For Lead Time, you can change the parameters such as Horizon for Past, Horizon for Future, ILT Calc.Meth, DLT Multiplier for Past, and DLT Multiplier for Future for the selected products.For Product Specific Spike Parameters, you can change the parameters such as Product Splike Horizon Constant, Product Splike Horizon Multiplier, and Product Spike Threshold Factor for the selected products.Mandatorily change Horizon for Past (in Days) into 10 days.Mandatorily maintain ILT Calc. Method as HCRE by default. | The Change screen displays.Please ensure there is transaction data for 3 buffered products in the horizon for past period, here in past 10 days. If not, please return back to preliminary step [Create Initial Data (Optional)](#unique_8) [page ] 9.Horizon for Past and Horizon for Future are used to calculate ADU - average daily usage, defined as average usage of a product or component on a daily basis, calculated based on the demand over a selected averaging interval.In our scenario, we make product R-401 with only historical consumption value to calculate ADU. We make product S-201 with only future planned independent requirement as demand to calculate ADU. We make product S-202 with both historical consumption value and future PIRs to calculate ADU. |  |
| 6 | Apply Changes | Choose Apply Changes.On the Apply Changes screen, choose Apply.Confirm the changes are applied for your selected products in the Mass Maintenance: Products (DD) screen. | The Apply Changes screen displays. |  |
| 7 | Initialize Setting for Material | Repeat steps 3-6 for following products.Product: S-201Do not maintain Horizon for Past (in Days), but Horizon for Future (in Days) into 14 days.Manually initialize the Value Indicator, Variability Indicator, DLT Indicator and BOM Usage Indicator if the value is unclassified. | Since product S-201 is a new product without any historical data, so we use forward-looking ADU calculation with PIRs in the future. |  |
| 8 | Initialize Setting for Material | Repeat steps 3-6 for following products.Product: S-202Mandatory change Horizon for Past (in Days) into 10 days, and maintain Horizon for Future (in Days) into 14 days. | Product S-202 is a material with both historical consumption data and PIRs in the future. |  |

##### Check Buffer Positioning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to monitor and decide which products to buffer and unbuffer by checking buffer analysis.

In our test script, we keep pre-delivered buffer positioning for S-201,S-202 & R-401 to make scenario stable for testing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Buffer Positioning (F3282). | The Buffer Positioning screen displays. |  |
| 3 | Filter Product | On the Buffer Positioning (F3282) screen, filter by product and choose Go.Product: S-201; S-202; R-401Plant: 3310 | In real business scenario, production planner could adapt the filter conditions, for example filter by classification results or filter by candidates of buffered products, then you could decide buffer or unbuffer the product.In our best practice scenario, we have already set S-201, S-202, R-401 as buffered products (with MRP type D1) by default, you could just check the buffer analysis for them in this activity, and proceed to Buffer Sizing later. |  |
| 4 | Check Buffer Analysis Results | In the Products area, you can see MRP Type, Buffered, Classifications, Product Type, Lead Time, Simulated DLT for the filtered products. | If you are the first tester, the Simulated DLT could remain blank.You could choose Settings icon to adjust the displayed columns. |  |
| 5 | Take Action | Choose all the filtered products.Choose Simulate DLT, check the updated value in column Simulated DLT . | In real business scenario, production planner could choose the filtered product and choose Buffer and Unbuffer button.Note In our pre-delivered scenario, please keep our current settings and do not make change to avoid testing complexity. |  |
| 6 | Navigate to Buffer Analysis Details | Check the buffer analysis details for filtered product.Choose the row for product, for example, S-201 and R-401. | The Buffer Analysis screen displays. |  |
| 7 | Check Buffer Analysis Details | On the top of the screen, check the product details for the filtered product.Check the Longest Path in Upstream tab by default.Change the mode into BOM in Upstream tab to check the whole BoM upstream structure.Check the Immediate Parent in Downstream tab.Change the mode into Next Buffers in Downstream tab to check next buffers.Change the mode into Finished Goods in Downstream tab to check finished goods.Click against the product in Product column, you can navigate to relevant links, like Manage Product Master Data (F1602) and so on. | Focus on upstream analysis with S-201.Focus on downstream analysis with R-401.For pre-delivered material, S-201.The Longest Path is S-201 and first lower level R-302.The BOM is S-201 ，first lower level R-302, S-301 and second lower level R-401.The Immediate Parent are F-10A and F-10B.For pre-delivered material, R-401.The Longest Path and BOM are same, R-401.The Immediate Parent is S-301.The Next Buffers is S-201.The Finished Goods are F-10A and F-10B.In real business scenario, after check all these buffer analysis, you can make a decision and choose button Buffer/Unbuffer for the product if necessary, refer to [Use Case A: Buffer Positioning – Inbound Protection](#unique_29) [page ] 35.Note In our pre-delivered scenario, please keep our current settings and do not make change to avoid testing complexity.On the Upstream tab, if a bulk material exists as a BOM component, you can see the Bulk Material icon with tooltip ILT will be considered as 0 days for product XXX, plant XXX as it is a bulk product. |  |
| 8 | Check Network Graph | On the screen Buffer Analysis, choose Network Graph icon to check the graph view.You can filter the path mode from Longest Path into Product Flow, you can adjust highlight mode with No Highlight, Value Indicator and so on. And you can change path mode into BOM and BOM Usage, then the orientation is up and down.You can click against any component, then choose Show Details icon or Add to Favorites icon or Hide Immediate Parents/Children and Hide All Parents/Children icon.If you choose Show Details icon, the product details displays and you can navigate by click Buffer Analysis to buffer/unuffer this component.If you choose Add to Favorites icon, then if you filter by Highlight Favorites, this component is highlighted.If you choose Hide Immediate Parents/Children and Hide All Parents/Children icon, then the upstream flow of such components could collapse and expand.You can choose the Zoom in, Zoom Out, Zoom to Fit, or Enter Full Screen icon as you like to adjust display size. | Note In our pre-delivered scenario, keep our current settings and do not make buffer/unbuffer change to avoid testing complexity.If a bulk material exists as a BOM component, its Lead Time shows 0 Days in network graph. |  |
| 9 | Share | Choose Share at the top of screen, and then choose Send E-Mail or Save as Tile.Option 1. Choose Send E-mail, and then an e-mail template is displayed with the current link.Option 2. Choose Save as Tile, then fill in Tile, Subtitle, Description and Group for the new tile. The new tile will be displayed in the SAP Fiori launchpad accordingly. |  |  |

#### Buffer Sizing

This process step shows you how to calculate buffer levels – maximum stock level, reorder point and safety stock for buffered products.

- Maximum stock - the cumulative sum of the quantities of the red, yellow and green zones, denoting the suggested stock buffer level above which the stored inventory quantity can be considered as excessive
- Reorder point - the cumulative sum of the quantities of the red and yellow zones, which indicates a need for replenishment of the stock buffer, that is, creation of a supply order, whenever the available stock falls below this point
- Safety stock - the minimum recommended stock buffer level that should be maintained, denoted by the buffer value at the top of the red zone

After buffer sizing execution, you could proceed with the scenario Demand-Driven Replenishment Planning and Execution (2QI) for detailed replenishment process.

##### Schedule Lead Time Classification of Products

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to classify your Demand-Driven Replenishment-relevant products by evaluating them based on their Decoupled Lead Time (EFG classification) across a specified evaluation interval. Classifying your products based on their Decoupled Lead Time (DLT) will help define inputs for their buffer settings. Additionally, you can schedule runs to reclassify your products periodically to keep their classifications up-to-date, so that you get accurate results as you proceed with Demand-Driven Replenishment.

Classification type 4: Lead Time (EFG, E for short, F for medium, G for long)

Classifying a product or component into type E, F or G based on its decoupled lead time, with products classified as type E having the shortest decoupled lead time and products classified as type G having the longest decoupled lead time. An EFG classification is typically used together with the procurement type for a product or component.

If there is transactional data (production order or purchase order) for buffered products, then the lead time is calculated as below:

For in-house production material, like S-201

Lead time = The production order final confirmation time - the production order creation time.

If order creation time is 7/12/2017 2:00:00 AM, the finish execution time for final confirmation is 7/12/2017 8:00:00 AM, then the lead time is 6/24 = 0.25 days.

The unit of lead time is day.

If there are several production orders during the horizon period, then the lead time is calculated as the average quantity of those lead times.

For external procurement material, like S-202 and R-401

Lead time = The date of goods receipt for purchase order - the date of purchase order creation.

If PO creation and GR posting are executed in the same day, then the lead time is one day.

If PO created in 5/1/2017, goods receipt for PO posted on 5/2/2017 (which indicates posting date is 5/2/2017), then the lead time is also one day.

If purchase order posting date is before purchase order creation date, then the purchase order is regarded as invalid and ignored during individual lead time calculation to prevent negative value.

If there are several purchase orders during the horizon period, then the lead time is calculated as the average quantity.

If there is no transactional data for buffered products, then the lead time is derived from material master data.

For in-house production material, like S-201, lead time is in-house production time in MRP2 view, for external procurement material, like S-202 and R-401, lead time is planned delivery time in MRP2 view.

Lead time (also called individual lead time) is defined as the total time required to receive a product in your inventory after placing an order, whether via manufacture, purchase or transfer from another location.

Decoupled lead time is calculated for buffered product (DD-relevant product) by considering the longest path in the BoM chain. In other words, decoupled lead time is a sum of the longest lead times of non-buffered products in a sequence headed by a buffered product in a BoM, adding up to a cumulative lead time for the buffered product.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Lead Time Classification of Products (DD) (F2871). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create to create a new application job. | The New Job screen displays. |  |
| 4 | Enter Job Details | In the 1. Template Selection area, enter the following entries:Job Template: Decoupled Lead Time (EFG) Classification of Products (DD)Job Name: Decoupled Lead Time (EFG) Classification of Products (DD) |  |  |
| 5 | Define Recurrence Pattern | Choose Step 2.In the 2. Scheduling Option area, maintain the following entries:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entry and choose OK.Start Immediately: XRecurrence Pattern: Single Run | The Scheduling Information screen displays. |  |
| 6 | Enter Selection Criteria | Choose Step 3.In the 3. Parameters area, make the following entries.For Selection Criteria subarea:Plant: 3310Product: S-201, S-202, R-401Number of Days (Past): for example, 10 |  |  |
| 7 | Enter Parameters | In the Parameters subarea, make the following entries:DLT Thresholds for Make (in Days) (E): 2DLT Thresholds for Make (in Days) (F): 4DLT Thresholds for Buy(in Days) (E): 2DLT Thresholds for Buy (in Days) (F): 4DLT Thresholds for Transfer (in Days) (E): 2DLT Thresholds for Transfer (in Days) (F): 4In the Job Parameters area, make the following entries:Excl. Mnlly.Classified Prods.: BlankParallel Processing: BlankMaintain Logs: X | You could adjust the classification parameters with the real business requirement.3 parameters are maintained by default and keep unchanged.DLT Thresholds for Make (in Days) (G):DLT Thresholds for Buy (in Days) (G):DLT Thresholds for Transfer (in Days) (G):If you enable Excl. Mnlly.Classified Prods, then manually classified products will be exclusive for product classification. |  |
| 8 | Schedule a New Job | Then choose Check. If there are no error messages, choose Schedule.A new job is created and displayed in the Application Jobs table. |  |  |

##### Buffer Profile Maintenance (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to maintain a buffer profile, which is a set of buffer control parameters. They are assigned to DD-relevant products based on their classification regarding lead time, variability, and procurement type.

In our pre-delivered scenario, we have created the buffer profile DEFAULT, you can review or change the detailed control parameters and plant assignment of buffer profile DEFAULT.

You could also create a new buffer profile and make plant assignment (please be informed that only one buffer profile could be assigned to one plant) in SSCUI Buffer Profile Assignment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241).On the Manage Your Solution screen, choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 3 | Filter SSCUI | Make the following entries and press Enter:Search: Buffer Profile AssignmentApplication Area: ManufacturingSub Application Area: Demand-Driven ReplenishmentChoose the filtered item. On the Configure Your Solution - Profile Assignment screen, choose Configure for Buffer Profile Assignment to navigate into detailed screen.Select the checkbox for buffer profile DEFAULT in the Set of Profiles area. |  |  |
| 4 | Check SSCUI | Choose Buffer Profile Details in the Dialog Structure area.On the Buffer Profile Details screen, check the listing DLT Factor, Variability Factor and Buffer Profile Description for different Procurement Type, Variability Indicator, DLT Indicator and Minimum Order Quantity.You could also change the DLT Factor or Variability Factor or Buffer Profile Description if necessary. | The Buffer Profile Details screen displays.Lead time factor: A factor that is part of a buffer profile and that helps define the buffer levels for a group of products based on their decoupled lead time classification.Variability factor: A factor that is part of a buffer profile and that helps define the buffer levels for a group of products based on their variability (XYZ) classification. |  |
| 5 | Check the Plant Setting | Choose Plant Settings in the Dialog Structure area.You can check that buffer profile DEFAULT is assigned to the pre-delivered plant by default.You can check the value of Spike Horizon Constant, Spike Horizon DLT Multiplier, Spike Threshold, and On Hand Alert Threshold.The default value of Spike Horizon Constant is 0.The default value of Spike Horizon DLT Multiplier is 1.The default value of Spike Threshold is 0.5.The default value of On Hand Alert Threshold is 0.5.Note The spike threshold and horizon parameters can also be maintained on the product level in app Mass Maintenance of Products (DD) (F2825). | The Plant Settings screen displays.Formula 1:Order Spike Horizon = DLT * Spike Horizon DLT Multiplier + Spike Horizon ConstantFormula 2:Order Spike Threshold = safety stock * Spike ThresholdThe default value of Spike Threshold is 0.5.Spike Horizon Constant: A constant, usually measured in days, which helps calculate the Order Spike Horizon when summed with the product of the Spike Horizon DLT Multiplier (SHM) and the Decoupled Lead Time (DLT).The default value is 0.Spike Horizon DLT Multiplier: A multiplicative factor that when multiplied with the Decoupled Lead Time (DLT) and summed with a Spike Horizon Constant (SHC) helps calculate the order spike horizon, which helps identify order spikes.The default value is 1.Order Spike Threshold: A selected quantity that in combination with the Order Spike Horizon qualifies an order spike.On Hand Alert Threshold, it is used in app Replenishment Execution (F2831) to compare the value of On-Hand Stock and the value of safety stock multiplied with On Hand Alert Threshold. |  |
| 6 | Create a New Buffer Profile (Optional) | Choose Set of Profiles in the Dialog Structure area, and then choose Edit > New entries(F5) to create a new buffer profile ID. After entering all required parameters, choose Save.Select the checkbox of the new buffer profile, and then choose Buffer Profile Details in the Dialog Structure area. Then choose Edit > New entries(F5) to create new buffer profile details. After entering all required parameters, choose Save.Choose Plant Settings in the Dialog Structure area. Then choose Edit > New entries(F5) to make assignment of new buffer profile with relevant plants. After entering all required parameters, choose Save. | Please be informed that only one buffer profile can be assigned to a plant.Plant 3310 is now assigned to the buffer profile DEFAULT, so if you would like to assign plant 3310 with new buffer profile, first delete the default assignment. |  |

##### Schedule Buffer Proposal Calculation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to generate buffer (stock) level proposals for your Demand-Driven Replenishment-relevant products based on their average daily usage, decoupled lead time, buffer profiles and several other factors. Additionally, you can schedule runs to recalculate the buffer proposals periodically to keep them up-to-date, so that you maintain appropriate levels of inventory while using Demand-Driven Replenishment.

You can use SSCUI Assignment of Profile for Goods Issue selection (DD) to refine flexible average daily usage with goods issue exclusion profile.

The following are the denotations for SAP calculated buffer levels:

- Top of Red Zone – Safety Stock
- Top of Yellow Zone – Reorder Point
- Top of Green Zone – Maximum Stock Level

The following are some formulas for reference:

ADU: Average Daily Usage

The average goods issue quantity and PIR quantity of a specific product in the horizon period.

- Red Zone formula: (Yellow Zone * Lead Time Factor) * (1 + Variability Factor)
- Yellow Zone formula: ADU * Decoupled Lead Time
- Green Zone formula: Maximum of {Yellow Zone * Lead Time Factor}

OR {Minimum Order Quantity}

OR {Order Cycle Time * ADU}

It offers possibility for customers to overwrite our SAP calculated buffer levels with key user extensibility BADI DD_BUFFERLEVELZONE.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Buffer Proposal Calculation (F2837). | The Application Jobs screen displays. |  |
| 3 | Create a New Job | Choose Create to create a new application job. | The New Job screen displays. |  |
| 4 | Enter Job Details | In the 1. Template Selection area, enter the following entries:Job Template: Buffer Proposal Calculation for Demand-Driven ReplenishmentJob Name: Buffer Proposal Calculation for Demand-Driven Replenishment |  |  |
| 5 | Define Recurrence Pattern | Choose Step 2.In the 2. Scheduling Option area, maintain the following entries:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entry and choose OK.Start Immediately: XRecurrence Pattern: Single Run | The Scheduling Information screen displays. |  |
| 6 | Enter Selection Criteria | Choose Step 3. In the 3. Parameters area, make the following entries.For Product Selection Criteria subarea:Plant: 3310Product : S-201, R-401 |  |  |
| 7 | Select Parameters for JOB | In the Automated Proposal Processing Options subarea, make the following entries:Adopt with Tolerance: blankAllow decrease up to %: blankAllow increase up to %: blankAlways Adopt Proposals: blankDo not Adopt Proposals: XIn the Average Daily Usage area, make the following entries:Based on Fixed Interval: XBased on Rolling Interval: blankExclude Non Goods Issue Days: blankIn the Decoupled Lead Time area, make the following entries:Reuse values from Prod. Master: blankRecalculate: XIn the Job Parameters area, make the following entries:Parallel Processing: blankMaintain Logs: X | If you choose Adopt with Tolerance, then the proposal would be automatically adopted if the decrease or increase percentage of TOG (maximum stock level) is in the range. If not, then the proposal has to be manually adopted in proceeding process.If you choose Always Adopt Proposals, then the proposal would always be automatically adopted.If you choose Do Not Adopt Proposals, then the proposal would not be automatically adopted, but only manually adopted.If you choose Reuse values from Prod.Master, then decoupled lead time is reused from product master.If you choose Recalculate, then decoupled lead time is recalculated.If you choose Based on Fixed Interval, then average daily usage calculation interval for future days has the fixed reference date. For example, if the horizon for future is 14 days, then to-day’s ADU interval is from today to <today + 14 days>; then tomorrow’s ADU interval is still today to <today + 14 days>.We choose this mode for product S-202 and R-401.If you choose Based on Rolling Interval, then average daily usage calculation interval for future days has the rolling reference date.If you enable Exclude Non Goods Issue Days, then non-goods issue days will be exclusive for ADU calculation. |  |
| 8 | Schedule New Job | On the New Job screen, choose Schedule.A new job is created and displays in the Application Jobs table. | Confirm that the application job is finished with no error. |  |
| 9 | Schedule New Job for S-202 | Repeat step 3-8 for product S-202.In Step 7, in the Average Daily Usage area, make the following entries:Based on Fixed Internal: blankBased on Rolling Interval: X | We choose Based on Rolling Interval mode for pMRP material S-202 only.If you choose Based on Rolling Interval, then average daily usage calculation interval for future days has the rolling reference date. For example, if the horizon for future is 14 days, then today’s ADU interval is from today to <today + 14 days>; then tomorrow’s ADU interval is from tomorrow to <tomorrow + 14 days>. |  |

##### Manage Buffer Levels

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to ensure that products are available when needed by managing the safety stock, reorder point and maximum stock through buffer proposals for optimized Demand-Driven Replenishment. Buffer level proposals are necessary to adjust the buffer levels to the ever changing reality and thereby ensure that a product is sufficiently stocked to meet average demand, but in low enough quantities to prevent excessive storage costs or losses due to expiry. Buffer level is a properly-managed buffer that ensures a product or component is sufficiently stocked to meet average demand, but in low enough quantities to prevent excessive storage costs or losses due to expiry.

Buffer level proposal is a well-balanced buffer level proposed by the Manage Buffer Levels app to ensure that a product or component is sufficiently stocked to meet average demand, but in low enough quantities to prevent excessive storage costs or losses due to expiry.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Buffer Levels (F2706). | The Manage Buffer Levels screen displays. |  |
| 3 | Filter Product | On the Manage Buffer Levels (F2706) screen, filter by product and choose Go.Editing Status: ALLProposal Status: ALLProduct: S-201; S-202;R-401Plant: 3310Max Stock Deviation: Blank | In the Buffers list, the buffer levels of 3 Demand-Driven Replenishment(DDR) products display.If results don't display, please confirm whether you execute previous step [Schedule Buffer Proposal Calculation](#unique_18) [page ] 29 successfully.If there is no result displays in the system, please also confirm whether the Area of Responsibility is correctly maintained for plant 3310.Choose User > App Settings, then Area of Responsibility Screen displays. |  |
| 4 | Check Buffer Level Status | In the Buffers area, the buffer levels of 3 buffered products display.You could choose Setting to adjust the displayed columns on the screen.You could see Max.Stock Today, Buffer Levels (Historical and Proposed), Average Daily Usage (Historical and Future), Change in DLT, Change in Variability and Information columns by default.If you regard the proposed changes for products as reasonable, you could either make single change or mass change.For singe change, choose the button Adopt for each specific product.For mass change, select the checkboxes of relevant products and choose Adopt on the top. And the Information screen displays to inform you Job XXX has been scheduled. Choose OK. Please note down the job number and then you can check the job details by choosing Logs in the upper right.If you regard the proposed changes are big, you could click against the row for the specific buffered product to check detailed information. | The Manage Buffer Levels screen displays with detailed information.If current proposed buffer values of are zero, please confirm whether you have created transaction data (production order / purchase order) for such buffered product in preliminary steps [Create Initial Data (Optional)](#unique_8) [page ] 9.Current Value is the value currently used by DDR process.Proposed Value is the value that has been calculated in the Schedule Buffer Proposal Calculation (F2837) app by the latest DDR run.The current and proposed buffer values are used round value for measuring unit PC and EA.If you choose the button Adopt, the executed buffer levels results are updated to material master.The reorder point field and maximum stock level field in MRP1 view, and safety stock field in MRP2 view will be consistent with the buffer levels from DDR table.For Mass change, choose Logs.In the new Application Jobs screen, choose Adapt Filters. On the Adapt Filters screen, choose More Filters. Choose Job ID in the new screen Select Filters and choose OK.On the Adapt Filters screen, fill in the Job ID field with the number you noted down before and choose Go.The filtered job displays in the Application Jobs screen, choose Navigate to the job details icon.On the Job Details screen. check General Information , Scheduling Options, Run Details and Parameters. |  |
| 5 | Check Detailed Buffer Level Status | On the Manage Buffer Levels screen with detailed information.You could see general product details on the top of screen, Max.Stock Deviation, Change in ADU, Change in DLT, Proposal Run On, Proposal Status and Buffer Profile.You could see four tabs, Buffer Levels, Average Daily Usage, Decoupled Lead Time and Classifications.In the Buffer Levels area, if you maintain DLT Multiplier for Past or DLT Multiplier for Future in [Mass Maintenance of Products](#unique_14) [page ] 19, then you could see note ‘Horizon for Past is XXX Days and Horizon for Future is XXX Days’ in the head.In the Buffer Levels area, you could see both historical and prospective buffer levels, the buffer levels display with 3 colored zones for a special day in Chart view, you could click against the colored zone to check the exact buffer levels for date.You could choose the Show Adjustments button, then Zone Adjustments area displays, you could change Red Zone (red zone adjustment factor), Yellow Zone (yellow zone adjustment factor), Green Zone (green zone adjustment factor) for a period to adjust the current buffer level.You could also change the view into Performance view, then you could check the Actual Stock quantity if you click against the black point.You could also change the view into Comparison View to check the comparison between current buffer levels with proposed buffer levels.You could choose the Table icon for each view.In the Average Daily Usage area you could see both Goods Issued in blue Monthly PIRs, Weekly PIRs, Daily PIRs in yellow. You could click against the black point to check the ADU for Proposal Run for date. The prospective goods issue quantity is the same with today’s quantity. You could also see the highlighted ADU Horizon period.You could choose the Show Adjustments button, then Demand Adjustments area displays, you could change Demand Adjustment for a period and see Adjusted ADU.You could also choose Table icon to change the view.In the Decoupled Lead Time area, you can see general lead time information, BOM Explosion Date, DLT for Current Buffer, DLT for Proposed Buffer, and Change in DLT.You could also see details in Longest Path in Stock's Replenishment Network. The lead time details for each product display in the node.You can choose Product flow that navigate to Buffer Analysis screen.In the Classifications area, you can see the Buffer Profile (Current vs. Proposed) and Classification (Current vs. Proposed). | You could manually adjust buffer levels for a period. Please choose Show Adjustments button in Buffer Levels area, then Zone Adjustments area displays. Please choose Edit on the top right of the screen, and then choose Create. Then you can maintain adjustment factors, Red Zone, Yellow Zone and Green Zone for a specific period as you required.For example, make following entries and choose Enter.Period: <this month>Red Zone: 1.50Yellow Zone: 1.50Green Zone: 1.50Choose Simulate Changes, and you can see that the buffer zones are adjusted in Buffer Levels area in Planning View.Then select the checkbox and choose Save and Adopt in bottom right.You could manually adjust demand for a period similarly in Average Daily Usage tab as well.Please be informed that demand change will also impact buffer level changes.Note If you choose the button Save and Adopt, the adjusted buffer levels results are updated to material master if the user has the authorization to change material master.The reorder point field and maximum stock level field in MRP1 view, and safety stock field in MRP2 view will be consistent with the current buffer levels.Because of the different ADU calculation method setting in Schedule Buffer Proposal Calculation section, for product S-202, the ADU for future keeps gradually down; for product S-201 and R-401, the ADU for future keeps unchanged.In the Average Daily Usage area, the PIRs are converted from weekly PIRs into daily PIRs, for example, if the weekly PIR is 70 as you generated in preliminary step so the converted daily PIRs quantity is 70/7=10. |  |
| 6 | Mass Adjust Zone and Demand | Choose the Back icon and return to the overview Manage Buffer Levels screen.You can select more than one product and choose Adjust > Zone or Adjust > Demand, then choose Absolut or Relative or Copy. Then the Mass Adjust Buffers screen displays. | It is used to massively adjust zone and demand.Enter adjustment parameters as you like and choose Apply Adjustment. It is quite similar with single zone adjustment introduced in step 5. |  |
| 7 | Adopt the Proposal | Choose the Back icon and return to the overview Manage Buffer Levels screen.You can choose Adopt if necessary.Please note down the Current number of Max.Stock Today for S-201, S-202 and R-401. | Current Value is the value currently used by DDR process.Current safety stock = current red zoneCurrent reorder point = current red zone + yellow zoneCurrent max stock level = current red zone + yellow zone + green zoneIf you don’t want to adopt proposals, you can choose Discard.As the Schedule Buffer Proposal Calculation (F2837) job could be automatically executed, but you don’t want to run valid buffer proposals for a product in a special period, you can choose Proposal Runs > Suspend. And please fill in the Suspension Period and choose Suspend. As a result in Information column, Proposal runs suspended from XXX to XXX displays.If you want to resume the suspension, please choose Proposal Runs > Resume, then choose Resume on Resume Proposal Creation screen. |  |

### Use Cases(Optional)

#### Use Case A: Buffer Positioning – Inbound Protection

This process step shows you how to make strategic buffer positioning and adjust buffered or unbuffered product based on business requirements.

In real business, you can adjust buffer positioning with different strategies. In our standard scenario, we introduce inbound protection, which can compress lead time.

##### Schedule Product Classification

Refer to step [Schedule Product Classification](#unique_13) [page ] 16 for products F-20A,S-210,S-310,R-410,R-412,S-208,S-315,R-411,R-311.

The classification calculation for these products is to make them visible to check MRP type in Mass Maintenance of Products (DD) (F2825)) app.

If there is any alarm like missing consumption data, please ignore it.

##### Initialize MRP Type

Refer to step [Mass Maintenance of Products](#unique_14) [page ] 19 for products F-20A,S-210,S-310,R-410,R-412,S-208,S-315,R-411,R-311.

Only maintain the MRP type of all products as PD to initialize them as unbuffered products. For other fields, remain unchanged.

##### Buffer Positioning - Inbound Protection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to monitor and decide which products to buffer and unbuffer by checking buffer analysis.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Buffer Positioning (F3282). | The Buffer Positioning screen displays. |  |
| 3 | Filter Product | On the Buffer Positioning screen, filter by product and choose Go.Product: F-20A, S-210, S-310, R-410, R-412, S-208, S-315, R-411, R-311Plant: 3310 |  |  |
| 4 | Check Buffer Analysis Results | In the Products area, you can see MRP Type, Buffered, Classifications, Product Type, Lead Time, Decoupled Lead Time for the filtered products. | If you are the first tester, the Decoupled Lead Time could remain blank.You could choose Settings icon to adjust the displayed columns. |  |
| 5 | Decoupled Lead Time | Choose all the filtered products.Choose Simulate DLT, and check the updated value in column Decoupled Lead Time. | In real business scenario, production planner could choose the filtered product and choose Buffer and Unbuffer button. |  |
| 6 | Navigate to Buffer Analysis Details | Check the buffer analysis details for filtered product.Choose the row for product, for example, F-20A | The Buffer Analysis screen displays. |  |
| 7 | Check Buffer Analysis Details | On the top of the screen, check the product details for the filtered product.Choose Network Graph and choose Product Flow mode to check the product flow for whole upstream structure.Choose the Legend icon and you can see that the longest path marked yellow consists of F-20A, S-210, S-310, and R-410. | For predelivered material, F-20A.The initial Longest Path is F-20A first lower level S-210, second lower level S-310 and third lower level R-410. |  |
| 8 | Buffer Positioning | In order to compress lead time, we can buffer R-410 which has a long individual lead time.Click against R-410, then choose Show Details icon, the product details display and choose Buffer Analysis. Then you navigate to another Buffer Analysis screen for product R-410, choose Buffer button.Make the following entries in Buffer screen and choose Apply Changes.MRP Type: D1Maximum Stock Level: <Quantity>, for example, 500Reorder Point: <Quantity>, for example,300Safety Stock: <Quantity>, for example,200Lot Sizing Procedure: H1Minimum Lot Size: <Quantity>, for example,100On the Apply Changes screen, choose Apply. | Product R-410 is buffered.You can choose MRP Type as D2 if you want to consider firmed planned order or repetitive requirements. This is due to:MRP type D1 is used in DDR and excludes all dependent requirements.MRP type D2 is used in DDR and includes dependent requirements from firmed or repetitive requirements. |  |
| 9 | Recheck Buffer Analysis Details | Choose back icon to navigate back to Buffer Analysis screen of product F-20A.Choose the Legend icon and you can see that longest path marked yellow consists of F-20A, S-210, S-310, and R-412. | The updated Longest Path is F-20A, first lower level S-210, second lower level S-310 and third lower level R-412. |  |
| 10 | Second Buffer Positioning | To compress lead time, we can buffer R-412 which has a long individual lead time the same as R-410.Repeat steps 8 to buffer product R-412.Repeat steps 9 to recheck buffer analysis details again for product F-20A. Now the longest path is changed and the decoupled lead time for F-20A is compressed. | Product R-412 is buffered.The updated Longest Path is F-20A, the first lower level S-208, second lower level S-315, and third lower level R-411.The decoupled lead time for F-20A is compressed. |  |

#### Use Case B: Use pMRP for ADU Calculation

This process step shows you a new option to generate PIRs for buffered sub-components for ADU calculation, it uses predictive material and resource planning (pMRP).

When finished this part, return to execute back main scenario.

##### Maintain PIRs for Finished Goods

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, PIRs are maintained for finished goods F-10A and F-10B.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Material: F-10A; F-10B; S-201; S-202Plant: 3310Period Indicator: Weekly (W)Version Active: Select all options |  |  |
| 5 | Filter Result | Choose Go to execute. | The material item displays. |  |
| 6 | Edit PIRs | Select the material items and choose Edit in the upper-right corner of the screen.On the screen, enter quantities per period, for example:PIR for F-10A: 0 for current period, 70 for next 3 periodsPIR for F-10B: 0 for current period ,105 for next 3 periodsMake sure the version is active.Version Active: Yes | Choose past date, for example, past 2 periods in Maintain Quantities per Period.Initialize all the PIRs for S-201 and S-202 into zero. |  |
| 7 | Save PIRs | Choose Save at bottom right. | The PIRs are saved. |  |

##### Schedule pMRP Simulation Creation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create pMRP Simulation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule pMRP Simulation Creation (F3968). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create to create a new application job. | The New Job screen displays. |  |
| 4 | Enter Job Details | In the 1. Template Selection area, enter the following entries:Job Template: Creation of pMRP Data via Top-Level MaterialsJob Name: Creation of pMRP Data via Top-Level Materials |  |  |
| 5 | Define Recurrence Pattern | Choose Step 2.In the 2. Scheduling Option area, maintain the following entries:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries and choose OK.Start Immediately: XRecurrence Pattern: Single Run | The Scheduling Information screen displays. |  |
| 6 | Enter Selection Criteria | Choose Step 3.In the 3. Parameters area, make the following entries.For Reference and Bucket Definition subarea:ID for Reference Data: DDR_PMRP_REFE_<MMDD>Bucket Category: WStart Date of Reference: <Today’s Date + 1 day>End Date of Reference: <Today’s Date + 5 weeks>For Simulation Name subarea:Simulation ID: DDR_PMRP_<MMDD>Simulation Description: DDR_PMRP_SIMULATION_<MMDD>For Object Selection subarea:Plant: 3310Material: F-10A, F-10BFor Document Data subarea:Opening Stock: <blank> | MMDD is today’s date, for example, if the date is August 1st, then MMDD = 0801. |  |
| 7 | Schedule New Job | Then choose Check. If there are no error messages, choose Schedule.A new job is created and displayed in the Application Jobs table. | Confirm that the application job is finished with no error. |  |

##### Process pMRP Simulations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to process the created pMRP Simulation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process pMRP Simulations (F3934). | The Process pMRP Simulations screen displays. |  |
| 3 | Filter the Simulation | On the Process pMRP Simulations screen, filter the simulation and choose Go.Create on : <Today’s date> | The simulation displays. |  |
| 4 | Copy the Simulation | Choose the filtered simulation, and choose Copy in the upper right corner.On the Copy screen, make the following entries and choose Copy.New Simulation ID: DDR_PMRP_<MMDD>_02New Simulation Description: DDR_PMRP_SIMULATION_<MMDD>_02 | It shows Simulation plan copied. |  |
| 5 | Check the Copied Simulation | On the Process pMRP Simulations screen, choose against the row of the new copied simulation with simulation ID: DDR_PMRP_<MMDD>_02 | The Demand Plan Simulation screen displays. |  |
| 6 | Adjust Simulation Quantity | You can check and adjust the quantities accordingly.You can change Quantities Displayed mode to check the difference between reference and adjusted simulation. |  |  |
| 7 | Release the Copied Simulation | Choose the Back icon.On the Process pMRP Simulations screen, choose Release for the copied simulation.On the Release screen, make the following entries and choose Release.Create PIRs for Demand-Driven MRP Components: XCreate PIRs for Top-Level Materials: XRequirement Version for Top-Level Materials: 00 Requirements PlanVersion Active for Top-Level Materials: Yes | The Simulation Status displays as Released. |  |

##### Check PIRs for Components

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check generated PIRs for semi-finished goods S-201 and S-202.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Material: F-10A; F-10B; S-201; S-202Plant: 3310Period Indicator: Weekly (W)Version Active: Select all options |  |  |
| 5 | Filter Result | Choose Go to execute. | The material item displays. |  |
| 6 | Check PIRs | Select the filtered material items, and choose Edit in the upper-right corner.On the screen, make the following entry:Maintain Quantities per Period: <Today’s date - 1 week>Check the generated PIRs for S-201 and S-202.Version Active: YES | The PIRs for components are generated. |  |

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 2QI - Demand-Driven Replenishment Planning and Execution (Mandatory) | After buffer sizing execution, you could proceed another scenario Demand-Driven Replenishment Planning and Execution (2QI) for detailed replenishment process. |

### Related APIs and Communication Arrangements

If you want to utilize API for integration scenario, refer to APIs and Communication Arrangements for Scope Items in SAP S/4HANA Cloud Public Edition to set up relevant communication arrangements.

For details regarding the interfaces, access the SAP Best Practice Explorer for SAP S/4HANA Cloud Public Edition and navigate to Accelerators > Implementation > APIs.

| Integration Scenario | Integration Scenario Name |
| --- | --- |
| SAP_COM_0009 | Product Integration |
| SAP_COM_0349 | Demand Driven Replenishment Buffer Profile Integration |
| SAP_COM_0359 | Demand Driven Replenishment Buffer Sizing Integration |

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
> Flagged while digesting this document, not verified: Schedule Buffer Proposal Calculation step 7 says Fixed Interval ADU mode is chosen 'for product S-202 and R-401', but step 6 selects S-201 and R-401 and step 9 and the later Manage Buffer Levels note say S-202 alone uses Rolling Interval (S-201 and R-401 fixed).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Mass Maintenance of Products step 3 lists S-201, S-202, S-203 and R-401 as buffered products by default, while Buffer Positioning and the preliminary steps name only three buffered products (S-201, S-202, R-401) and the BOM table describes S-203 as a stock transfer material.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/test-script-demand-driven-replenishment-planning-and-execution-2qi-ae]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1Y2_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 87,480 chars in the whole document
