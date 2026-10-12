---
id: 12-production-and-manufacturing/test-script-demand-driven-replenishment-planning-and-execution-2qi-ae
title: "Test Script: Demand-Driven Replenishment Planning and Execution (2QI_AE) (2QI_S4CLD2608_BPD_EN_AE)"
description: "S/4HANA Cloud test script for scope item 2QI_AE: demand-driven replenishment planning, execution, projected on-hand alerts and buffer performance (plant 3310)."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/demand-driven-replenishment]
aliases: [2QI_S4CLD2608_BPD_EN_AE]
keywords: [Demand-Driven Replenishment (DDMRP), demand-driven replenishment, replenishment planning, replenishment execution, projected on-hand alerts, historical buffer performance, net flow position, mrp type, planner overview, mrp runs]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2QI_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-849
topic: 12-production-and-manufacturing/demand-driven-replenishment
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Demand-Driven Replenishment Planning and Execution (2QI_AE) (2QI_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2QI_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Demand-Driven Replenishment (DDMRP)** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Demand-Driven Replenishment Planning and Execution (2QI_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232849715)

[2 Prerequisites 4](#_Toc232849716)

[2.1 System Access 4](#_Toc232849717)

[2.2 Roles 4](#_Toc232849718)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232849719)

[2.4 Business Conditions 7](#_Toc232849720)

[2.5 Preliminary Steps 8](#_Toc232849721)

[2.5.1 Create Initial Stock 8](#_Toc232849722)

[2.5.2 Maintain Rounding Value 9](#_Toc232849723)

[2.5.3 Check MRP Type 9](#_Toc232849724)

[3 Overview Table 11](#_Toc232849725)

[4 Test Procedures 14](#_Toc232849726)

[4.1 Replenishment Planning 14](#_Toc232849727)

[4.1.1 Replenishment Planning Review 14](#_Toc232849728)

[4.1.2 Create Demand for Finished Goods 16](#_Toc232849729)

[4.1.2.1 Create Sales Order (Option 1) 16](#_Toc232849730)

[4.1.2.1.1 Create Sales Order for Finished Goods 16](#_Toc232849731)

[4.1.2.1.2 Schedule MRP Runs 17](#_Toc232849732)

[4.1.2.1.3 Convert Planned Order to Production Order (For MRP Type D1 only) 19](#_Toc232849733)

[4.1.2.1.4 Firm Planned Order (For MRP Type D2 only) 20](#_Toc232849734)

[4.1.2.2 Create Production Order/Planned Order (Option 2) 21](#_Toc232849735)

[4.1.2.2.1 Create Production Order (For MRP Type D1 only) 21](#_Toc232849736)

[4.1.2.2.2 Create Firmed Planned Order for Finished Goods (For MRP Type D2 Only) 22](#_Toc232849737)

[4.1.3 Check Planner Overview 23](#_Toc232849738)

[4.1.4 Replenishment Planning 25](#_Toc232849739)

[4.2 Replenishment Execution 27](#_Toc232849740)

[4.2.1 Replenishment Execution 27](#_Toc232849741)

[4.2.2 Post Goods Issue 29](#_Toc232849742)

[4.2.3 Replenishment Execution Review 30](#_Toc232849743)

[4.2.4 Succeeding Production Execution 32](#_Toc232849744)

[4.2.5 Post Goods Receipt 32](#_Toc232849745)

[4.2.6 Replenishment Execution Review 33](#_Toc232849746)

[4.3 Projected On-Hand Alerts 35](#_Toc232849747)

[4.3.1 Check Projected On-Hand Alert 35](#_Toc232849748)

[4.3.2 Create Situation for Safety Stock Alert (Optional) 36](#_Toc232849749)

[4.3.3 Review Projected On-Hand Alert (Optional) 37](#_Toc232849750)

[4.3.4 Create Situation for Threshold Alert (Optional) 37](#_Toc232849751)

[4.3.5 Create Situation for Stockout Alert (Optional) 38](#_Toc232849752)

[4.3.6 Review Projected On-Hand Alert 38](#_Toc232849753)

[4.4 Review Historical Buffer Performance 39](#_Toc232849754)

[5 Appendix 41](#_Toc232849755)

[5.1 Succeeding Processes 41](#_Toc232849756)

## Purpose

Overview

Demand-driven replenishment (DD) helps you efficiently plan and manage supply chains based on customer demand, rather than through traditional MRP procedures. It forms the basis for a reliable material flow by defining buffers at strategically important points and adjusting these buffers regularly.

Dedicated apps provide views for replenishment planning and execution. With replenishment planning, an overview of the buffer information sorted by planning priority is shown. With this, you can trigger replenishment on time to avoid stock shortages and delays in the completion of production or sales orders due to insufficient stock. With replenishment execution, you can view the current stock situation for each product and check that sufficient on-hand stock is available for production. You can expedite replenishment directly, and by using readily available contact details, such as contacting the supplier of a purchase order or the production supervisor of the component production order.

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
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | F-10A | FIN10A, MTS-DDMRP, PD |  |
| Material | F-10B | FIN10B, MTS-DDMRP, PD |  |
| Material | S-201 | SEMI201, MTS, D1, Subassembly |  |
| Material | S-202 | SEMI202, MTS, D1 |  |
| Material | S-301 | SEMI301, MTS, PD, Subassembly |  |
| Material | R-302 | RAW302, PD |  |
| Material | R-401 | RAW401, D1 |  |
| Plant | 3310 | Plant 1 AE |  |
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
| F-10B | 0 | FERT | PC | Finished goods |  |
| S-201 | 1 | SEMI | PC | Semi-finished goods as decoupling point |  |
| S-301 | 2 | SEMI | PC | Semi-finished goods as decoupling point |  |
| R-401 | 3 | RAW | PC | External procured |  |
| R-302 | 2 | RAW | PC | External procured |  |
| S-202 | 1 | SEMI | PC | Semi-finished goods as decoupling point |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

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
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |
| BJ5 - Make-to-Stock Production – Discrete Manufacturing | If you need to create production order for semi-finished DDR product, then after the production order is created, complete the following activities described in the test script Make-to-Stock Production – Discrete Manufacturing (BJ5).Material Staging for Subassembly (Semi-finished Good). Make sure that the required components are available in stock.Picking Components (Semi-finished Good)Confirming Production Operations for Subassembly (Semi-finished Good) – please note the order confirmation date and order release datePost Goods Receipt for Production Order |
| J45 - Procurement of Direct Materials | If you require to create purchase order for semi-finished DDR product or raw DDR product, complete the following activities described in the test script J45 - Procurement of Direct Materials.Create Purchase Order manuallyPost Goods Receipt for Purchase Order |
| 1Y2 - Demand-Driven Buffer Level Management | You have completed the step described in the Test Script Demand-Driven Buffer Level Management (1Y2) to calculate the buffer levels for buffered products, S-201, S-202 and R-401. |

### Preliminary Steps

#### Create Initial Stock

Purpose

We need to make the components of S-201 available for production. In a real business case, the products are usually purchased from external suppliers in that case, process is covered by the standard purchasing or subcontracting processes. For the purpose of this test, we post initial stock directly to the storage locations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as an Inventory Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock (F1062) screen displays. |  |
| 3 | Specify Material | Make the following entries and choose Enter:Material: S-301Plant: 3310 | The Stock overview for the product is displayed. |  |
| 4 | Select Stock | In the screen, you can check Storage Location, Unrestricted-Use Stock, Blocked Stock, Stock in Quantity Inspection.Choose the Unrestricted - Use Stock icon for relevant storage location.Storage Location: 331B | If current quantity for S-301 in storage location 331B is enough, then skip step 5.The storage location is 331B for SXX and 331C for RXX products. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Document Date: TodayPosting Date: TodayStock Change: Initial EntryQuantity: <Quantity>, for example, 300 | The system displays Material document XXX created. The stock has been added. |  |
| 6 | Create Initial Stock for R-302 | Repeat step 3 -5 for material R-302, storage location: 331C. |  |  |

You can either post initial stock directly to the storage location or refer to the Procurement of Direct Materials (J45) or Scheduling Agreements in Procurement (BMR) test scripts.

#### Maintain Rounding Value

Purpose

In this step, rounding value for product S-201 is maintained. This value will be considered later when calculating the demand for product.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Material (MM02). | The Change Material (Initial Screen) screen displays. |  |
| 3 | Select Material | Enter the material details and choose Enter.Material: S-201Select the MRP1 view and choose Continue icon.Enter the plant details and choose Continue icon.Plant: 3310 | The Change Material S-201 (Semifinished Product) screen displays. |  |
| 4 | Enter Rounding Value | In the MRP1 view, check the following data.Rounding value: <Quantity>, for example, 100 | You can enter the rounding value, which is used to adjust the quantity for planned orders in replenishment apps. |  |
| 5 | Choose Save | Choose Save. | Material XXX changed. |  |

#### Check MRP Type

Purpose

In this step, check which MRP Type is maintained for buffered product S-201.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Material (MM02). | The Change Material (Initial Screen) screen displays. |  |
| 3 | Select Material | Enter the material details and choose Enter.Material: S-201Select the MRP1 view and choose Continue icon.Enter the plant details and choose Continue icon.Plant: 3310 | The Change Material S-201 (Semifinished Product) screen displays. |  |
| 4 | Check MRP Type | In the MRP1 view, check the current MRP type. | If current MRP type is D1 and you want to consider firmed planned order or repetitive requirements, you can change it to D2. This is due to:MRP type D1 is used in DDR and excludes all dependent requirements.MRP type D2 is used in DDR and includes dependent requirements from firmed or repetitive requirements.Different MRP types can also lead the succeeding steps to create demand steps during replenishment planning procedure. |  |
| 5 | Choose Save | Choose Save. | Material XXX changed. |  |

## Overview Table

The Accounts Payable scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Master Data

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Replenishment Planning |  |  |  |
| [Replenishment Planning Review](#unique_11) [page ] 14 | Production Planner | Replenishment Planning - By Planning Priority (F6241) | You can review the initial planning priority, net flow position and proposed quantity for buffered product S-201. |
| Create Demand for Finished Goods |  |  |  |
| Create Sales Order (Option 1) |  |  |  |
| [Create Sales Order for Finished Goods](#unique_12) [page ] 16 | Internal Sales Representative | Manage Sales Orders (F1873) | The sales order for finished goods, F-10A is created. |
| [Schedule MRP Runs](#unique_13) [page ] 17 | Production Planner | Schedule MRP Runs (F1339) | You can execute MRP runs for finished goods, F-10A. |
| [Convert Planned Order to Production Order (For MRP Type D1 only)](#unique_14) [page ] 19 | Production Planner | Manage Material Coverage - New Version (F0251A) | The planned order of F-10A is converted into production order. |
| [Firm Planned Order (For MRP Type D2 only)](#unique_15) [page ] 20 | Production Planner | Manage Material Coverage - New Version (F0251A) | The planned order for F-10A is firmed. |
| Create Sales Order (Option 2) |  |  |  |
| [Create Production Order (For MRP Type D1 only)](#unique_16) [page ] 21 | Production Supervisor - Discrete Manufacturing | Create Production Order (CO01) | The production order for finished goods, F-10A is created. |
| [Create Firmed Planned Order for Finished Goods (For MRP Type D2 Only)](#unique_17) [page ] 22 | Production Planner | Manage Planned Orders (F4170) | The firmed planned order for finished goods F-10A is firmed. |
| [Check Planner Overview](#unique_18) [page ] 23 | Production Planner | Planner Overview (F2832) | You can check the overview page for 3 demand-driven replenishment relevant apps |
| [Replenishment Planning](#unique_19) [page ] 25 | Production Planner | Replenishment Planning - By Planning Priority (F6241) | You can execute replenishment planning supply creation for buffered production.You can review the planning status after MRP run. |
| Replenishment Execution |  |  |  |
| [Replenishment Execution](#unique_20) [page ] 27 | Production Planner | Replenishment Execution - By On-Hand Status (F6242) | You can review initial on-hand stock status for buffered product, S-201. |
| [Post Goods Issue](#unique_21) [page ] 29 | Warehouse Clerk | Post Goods Movement (MIGO) | Trigger goods issue to reduce available on-hand stock. |
| [Replenishment Execution Review](#unique_22) [page ] 30 | Production Planner | Replenishment Execution - By On-Hand Status (F6242) | You can review on-hand stock status for buffered product, S-201, and expedite supply. |
| [Succeeding Production Execution](#unique_23) [page ] 32 | Several roles | Several apps | Refer to scope item BJ5 - Make-to-Stock Production – Discrete Manufacturing● Release Production Order for Final Assembly● Pick components for Final Assembly● Final Confirmation of Production Operations for Final Assembly |
| [Post Goods Receipt](#unique_24) [page ] 32 | Warehouse Clerk | Post Goods Movement (MIGO) | You can post goods receipt for production order of S-201 |
| [Replenishment Execution Review](#unique_25) [page ] 33 | Production Planner | Replenishment Execution - By On-Hand Status (F6242) | You can review on-hand stock status for buffered product, S-201 after production execution |
| Projected On-Hand Alerts |  |  |  |
| [Check Projected On-Hand Alert](#unique_26) [page ] 35 | Production Planner | Projected On-Hand Alerts - Stockout (F6243) |  |
| [Create Situation for Safety Stock Alert (Optional)](#unique_27) [page ] 36 | Production Supervisor - Discrete Manufacturing | Create Production Order (CO01) |  |
| [Review Projected On-Hand Alert (Optional)](#unique_28) [page ] 37 |  |  |  |
| [Create Situation for Threshold Alert (Optional)](#unique_29) [page ] 37 |  |  |  |
| [Create Situation for Stockout Alert (Optional)](#unique_30) [page ] 38 |  |  |  |
| [Review Projected On-Hand Alert](#unique_31) [page ] 38 | Production Planner | Projected On-Hand Alerts - Stockout (F6243) |  |
| [Review Historical Buffer Performance](#unique_32) [page ] 39 | Production Planner | Historical Buffer Performance - Outliers in last month (F7147) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

|  |
| --- |
| Note Before you start the test procedure, please confirm you have completed all the step described in the Test Script Demand-Driven Buffer Level Management (1Y2) to calculate the buffer levels for buffered products, S-201, S-202 and R-401.Materials with the status where MRP message is set to A (warning) or B (error) will be excluded from the following apps. If you have no results generated when using the following Demand-Driven apps, clarify the material status.Planner Overview (F2832)Replenishment Planning - By Planning Priority (F6241)Replenishment Execution - By On-Hand Status (F6242) |

In demand-driven replenishment, the planning run is the process step that is used to generate new supply elements. In consumption-based planning procedures, a supply element is created when the stock level falls below a predefined, static reorder point. In demand-driven replenishment, however, the planning run creates a new supply element (such as a purchase requisition, a planned order, or a stock transfer requisition) when the net flow position falls below the reorder point that is maintained in stock level management or, if not here, then in the material master.

### Replenishment Planning

#### Replenishment Planning Review

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you an overview of the buffer information sorted by the planning priority. Using this information, you can trigger replenishment on time to avoid stock shortages and possible delays in the completion of production or sales orders as a result of insufficient stock.

You can check if the planning priority status is green in app Replenishment Planning by Planning Priority.

If yes, please proceed to step [Create Demand for Finished Goods](#unique_34) [page ] 16

If no, please skip and proceed to step [Check Planner Overview](#unique_18) [page ] 23

Net flow position (NFP) is the quantity of stock derived from net flow equation, which is summing up the on-hand stock and the open supply, and subtracting the actual unfulfilled demand, which includes sales orders due on the current date, sales orders that are overdue and qualified order spikes, if any.

Besides the order spikes on the plant level coming from buffer profile, there can also be product-specific spike parameters that overwrite the plant setting that is maintained by the Mass Maintenance of Products (DD) (F2825) app. You can refer to step Buffer Profile Maintenance (Optional) in scenario 1Y2 for more details of these spike parameters.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Replenishment Planning - By Planning Priority (F6241). | The Replenishment Planning screen displays. |  |
| 3 | Filter Product | On the Replenishment Planning screen, make the following entries and choose Go:Search: S-201Planning Priority Status: <Mark all status> | You could customize the filters by choosing Adapt Filters.If there are no results displayed in the system, also confirm whether the Area of Responsibility is correctly maintained for plant 3310.Choose User > App Settings, then the Area of Responsibility screen displays. |  |
| 4 | Check Results for Filtered Products | You can see the columns of Planning Priority, Net Flow Position, Proposed Quantity, and Planning Action for buffered product S-201.Choose the Settings icon to display the buffer levels, Maximum stock, Reorder Point, and Safety stock.Or you can choose against Product S-201, the screen displays with product general information, Safety Stock, Reorder Point, Maximum Stock, and Decoupled Lead Time.You can also navigate to links, Manage Buffer Levels (F2706), Manage Product Master Data (F1602) and so on.Note down the Net Flow Position, Proposed Quantity, and Reorder Point for buffered product S-201. | You could customize the columns by choosing Settings icon.Planning priority = Net Flow Position / Maximum StockNet Flow Position = On-Hand Stock + Open Supply - Open Past (Including Today’s) Demand - Qualified Spike Demand.Qualified demand is a real demand that derived from a production order or sales order, instead of from a planned order.Qualified Spike Demand: When calculating qualified spike demand, the system considers the open, future quantities of aggregated daily demands. A qualified spike is a future daily demand that lies above the spike threshold and within the spike horizon.If Net Flow Position is above Reorder Point, Proposed Quantity and Planning Action remains blank, the status is green.Proceed to step [Create Demand for Finished Goods](#unique_34) [page ] 16.If Net Flow Position is below Reorder Point, require to trigger replenishment to maximum stock level, Proposed Quantity displays non-zero value, Planning Action displays Create Supply, the status is red or yellow.Skip and proceed to step [Check Planner Overview](#unique_18) [page ] 23. |  |

#### Create Demand for Finished Goods

In the following activities, you could create demand for finished goods F-10A to bring the planning status of buffered product S-201 into yellow or red.

If the MRP Type for S-201 is D1, as a tester, you can choose either of the following two options to create demand for finished goods.

Option 1. Create sales order

Option 2. Create production order

And the quantity of the production order or sales order is quite critical. It could consume the stock of S-201 and could just make the net flow position of S-201 to drop below its current reorder point, thus bring the planning status of buffered product S-201 into yellow or red.

The quantity of production order or sales order for F-10A shall be greater than the net flow position of S-201 subtracting reorder point of S-201.

Sales/Production order quantity for F-10A > NFP – reorder point for S-201

After completing tasks in this chapter, please proceed the steps in [Check Planner Overview](#unique_18) [page ] 23

If the MRP type for S-201 is D2, skip this chapter and proceed with [Create Firmed Planned Order for Finished Goods (For MRP Type D2 Only)](#unique_17) [page ] 22.

##### Create Sales Order (Option 1)

If you choose option 1 create sales order, please skip steps under [Create Production Order/Planned Order (Option 2)](#unique_36) [page ] 21 and proceed with [Check Planner Overview](#unique_18) [page ] 23.

###### Create Sales Order for Finished Goods

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the sales order for finished products F-10A. Pay attention to create the correct sales quantity.

The quantity of sales order for F-10A should be greater than the net flow position of S-201 subtracting reorder point of S-201.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders (F1873) screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On the Manage Sales Orders screen, choose Create > Create Sales Order - VA01 . |  |  |
| 4 | Enter the Order type OR (Standard Order) | On the Create Sales Documents screen, make the following entries and press Enter:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries:Sold to Party: 33100003Ship to Party: 33100003Cust. Reference: <Reference number>Material Number: F-10AQuantity: <Quantity> | The quantity for sales order is critical, and the tester must decide the proper sales order quantity to make the following scenario.First review the current buffer results and NFP quantity for S-201 in step [Replenishment Planning Review](#unique_11) [page ] 14.Regarding to design the sales order quantity, it can consume current stock of S-201 and make the NFP of S-201 drop below its current reorder point, and will later trigger replenishment.Sales order quantity for F-10A > NFP - reorder point for S-201 |  |
| 6 | Save Document | Choose Save. Make a note of the sales order number. | The order is saved.Note If the sales order might require approval, refer to scope item Sell from Stock (BD9), and complete the activities of Process Sales Order Approval. |  |

###### Schedule MRP Runs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to execute MRP.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirement Planning (MRP)Job Name: <MRP for F-10A>Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: <select>Recurrence Pattern: Single RunChoose OK.Choose Step 3.For 3 Parameters section:Plant: 3310Material: F-10AChanged BOM Components: <select>Planning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for F-10A in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

###### Convert Planned Order to Production Order (For MRP Type D1 only)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to convert the planned order for F-10A to production order, which is a qualified demand for the buffered product S-201. Please ensure MRP type for S-201 is D1. If MRP type is D2, skip this step and proceed with the step [Firm Planned Order (For MRP Type D2 only)](#unique_15) [page ] 20.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A). | The Manage Material Coverage screen displays. |  |
| 3 | Select Material | On the Manage Material Coverage screen, make the following entries and choose Go:Material: F-10APlant: 3310Shortage Definition: MRP Standard | The material item displays. |  |
| 4 | Find Planned Order | Choose the material item and check the generated planned order. |  |  |
| 5 | Convert Planned Order to Production Order | On the right screen, choose Convert from the dropdown list in Actions column for PldOrd XXX, and confirm date and quantity.Choose Convert. | Please double clarify the MRP type for S-201 is D1, so the planned order needs to be converted into production order.If the MRP type is D2, skip this step and proceed with [Firm Planned Order (For MRP Type D2 only)](#unique_15) [page ] 20.The production order is created.Note down the production order number for product F-10A. |  |

###### Firm Planned Order (For MRP Type D2 only)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to firm the planned order for F-10A, which is a qualified demand for the buffered product S-201. Please ensure MRP type for S-201 is D2. If MRP type is D1, skip this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A). | The Manage Material Coverage screen displays. |  |
| 3 | Select Material | On the Manage Material Coverage screen, make the following entries and choose Go:Material: F-10APlant: 3310Shortage Definition: MRP Standard | The material item displays. |  |
| 4 | Find Planned Order | Choose the material item and check the generated planned order. | Please double clarify the MRP type for S-201 in preliminary step. For MRP type D2, the firmed planned order is qualified demand. |  |
| 5 | Firm Planned Order | Choose against the generated planned order PldOrd XXX, then choose Change Planned Order.On the Change Planned Order: Stock Order screen, in the Firming area, make the following entry, and choose Save:Planned Order: X | The planned order is firmed.Note down the planned order number for product F-10A. |  |

##### Create Production Order/Planned Order (Option 2)

In this chapter, you can create qualified demand directly. If MRP type is D1, you can create production order for F-10A; if MRP type is D2, you can create the firmed planned order directly for F-10A.

###### Create Production Order (For MRP Type D1 only)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If the MRP type for S-201 is D1, then you will need to create production order for finished goods F-10A to bring the planning status of buffered product S-201 into yellow or red. In this activity, the production order for finished products F-10A is created as qualified demand for S-201 directly. Pay attention to the creation of the correct order quantity.

The quantity of production order for F-10A shall be greater than the net flow position of S-201 subtracting reorder point of S-201.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Production Order (CO01). | The Production Order Create: Initial Screen displays. |  |
| 3 | Enter the Order Information | Make the following entries:Materials : F-10AProduction Plant: 3310Order Type: YBM1and Choose Enter. | The Production Order Create: Header screen displays. |  |
| 4 | Enter the Order Details | Make the following entries:Quantity: QuantityEnd Date: Date, for example, Today's date +2 Daysand choose Enter. | The quantity for production order is quite critical.Please first review current buffer results and NFP quantity for S-201 in step [Replenishment Planning](#unique_19) [page ] 25.Regarding to design the production order quantity, it could consume current stock of S-201 and could just make the NFP ofS-201 drop below its current reorder point, and would later trigger replenishment.Production order quantity for F-10A > NFP - reorder point for S-201 |  |
| 5 | Save | Choose Save and make a note of your production order number |  |  |

###### Create Firmed Planned Order for Finished Goods (For MRP Type D2 Only)

Purpose

If the MRP type for S-201 is D2, then you will need to create firmed planned order for finished goods F-10A to bring the planning status of buffered product S-201 into yellow or red.

And the quantity of the planned order is quite critical. It can consume the stock of S-201, and can even make the net flow position of S-201 to drop below its current reorder point, thus bringing the planning status of buffered product S-201 into yellow or red.

The quantity of planned order for F-10A shall be greater than the net flow position of S-201 subtracting reorder point of S-201.

Planned order quantity for F-10A > NFP – reorder point for S-201.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Planned Orders (F4170). | The Manage Planned Orders Screen displays. |  |
| 3 | Create New Order | On the Manage Planned Orders screen, choose the button Create New Order. | The Create Planned Order: Initial Screen displays. |  |
| 4 | Enter the Order Information | Make the following entry and choose Continue:Planned Order Profile: LA | The Create Planned Order: Stock Order displays. |  |
| 5 | Enter the Order Details | Make the following entries:Material: F-10AMRP Area: 3310Order Quantity: <Quantity>Start Date: <Today’s Date>Firming Planned Order: X | The quantity for planned order is quite critical, tester should decide the proper sales order quantity to make following scenario.First review current buffer results and NFP quantity for S-201 in [Replenishment Planning Review](#unique_11) [page ] 14.Regarding the design of the planned order quantity, it can consume current stock of S-201 and can make the NFP of S-201 drop below its current reorder point, and later trigger replenishment.Planned order quantity for F-10A > NFP - reorder point for S-201. |  |
| 6 | Save | Choose Save and the planned order XXX will be created. |  |  |

#### Check Planner Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can check the overview page for 3 DDR relevant apps, manage buffers levels, replenishment execution by on-hand status and replenishment planning by planning priority.

The Planner Overview (F2832) shows in a single page the most important information and tasks related to demand-driven replenishment that are relevant for you right now. The information is displayed on set of cards. This allows you to focus on the most important tasks, and view, filter, and react to information quickly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Planner Overview (F2832). | The Planner Overview screen displays.Confirm whether the Area of Responsibility is correctly maintained for plant 3310.Select User > App Settings > Area of Responsibility , and then the Area of Responsibility screen displays. |  |
| 3 | Check the General Information | In the Buffer Level Management area, the quantity of deviations is supported by system proposals, and it is the same as the buffer values that are displayed in app Manage Buffer Levels (F2706). It usually indicates the number of materials whose proposal shall be processed.In the Replenishment Planning area, the quantity is based on planning priority. It is the same as the buffer value that is displayed in the app Replenishment Planning (F2831), and it usually indicates the number of materials whose net flow position is below reorder point, or below safety stock, or at 0 or below with demand.In the Replenishment Execution area, the quantity is based on on-hand stock status. It is the same as the buffer value that is displayed in the app Replenishment Execution (F2831), and it usually indicates the number of materials whose on-hand stock is out of stock with demand, or below On-Hand Alert Threshold, or below safety stock. |  |  |
| 4 | Check the Detailed Information | In all the three sections, you can choose different modes of characteristics to break down the buffers.Breakdown by Value (ABC)Breakdown by Lead Time (EFG)Breakdown by Variability (XYZ)Breakdown by BOM Usage (PQR)Breakdown by Procurement TypeWhat’s more, you can click against each breakdown bar, and it will navigate to such buffers in relevant DDR apps.For example, in the Replenishment Planning area, you choose mode - Breackdown by Value(ABC).You approach the bar for value A, the information displays asValue Indicator: ABuffers to Be Replenished: xxThen click the bar, the Replenishment Planning screen displays, and the buffers whose value indicator is A display in the Buffers area. |  |  |

#### Replenishment Planning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you an overview of the buffer information sorted by the planning priority. Using this information, you can trigger replenishment on time to avoid stock shortages and possible delays in the completion of production or sales orders as a result of insufficient stock.

At this time, the planning priority shall be in yellow/ red, the net flow position shall be lower than reorder point and the proposed quantity shall be non-zero.

If not, then it indicates that the quantity for sales order/production order of finished goods is not proper in step [Create Demand for Finished Goods](#unique_34) [page ] 16.

Return to step [Create Demand for Finished Goods](#unique_34) [page ] 16 to set a proper quantity.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Replenishment Planning - By Planning Priority (F6241) . | The Replenishment Planning screen displays. |  |
| 3 | Filter Product | On the Replenishment Planning screen, make the following entries and choose Go:Search: S-201Planning Priority Status: Mark all status | You could customize the filters by choosing Adapt Filters.If there are no results displayed in the system, please confirm whether the Area of Responsibility is correctly maintained for plant 3310.Choose User > App Settings > Area of Responsibility , then Area of Responsibility Screen displays. |  |
| 4 | Check Results for Filtered Products | You could see the columns of Planning Priority, Net Flow Position, Proposed Quantity, Planning Action for buffered product S-201.Choose Settings icon to display the buffer levels, Maximum stock, Reorder Point, Safety stock. | You could customize the columns by choosing Settings icon.Planning priority = Net Flow Position / Maximum StockNet Flow Position = On-Hand Stock + Open Supply - Open Past (Including Today’s) Demand - Qualified Spike Demand.At this time, the planning priority shall be in yellow/red, the net flow position shall be lower than reorder point, the proposed quantity shall be non-zero, the button Create Supply shall display for product S-201. |  |
| 5 | Choose Create Supply | Create Supply only occurs if proposed quantity is non-zero.Choose Create Supply to trigger MRP for buffered product S-201. | The dialog box displays Supply Order creation in progress with job ID XXX.If Create Supply is missing, return to step [Create Demand for Finished Goods](#unique_34) [page ] 16 again to set a proper quantity for sales order/production order.You can also choose the checkbox of product S-201, then choose Create Supply on the top to trigger mass change.Then Supply order creation in progress with job ID XXX displays, note down the job ID. Choose Logs and navigate to Application Jobs screen, choose Filters and filtered by Job ID and choose Go.You can choose Navigate to the job log and Navigate to the job details for the filtered job to see more information.Go back to the Replenishment Planning screen. |  |
| 6 | Check Replenishment Details | Choose the row for buffered product S-201, and it navigates to the Replenishment Planning Details screen.You can choose Expand Node icon to check the low-level material for buffered product S-201.You can also check the Supply/Demand List, Product Information and Notes.In the Supply/ Demand List area, you can switch All MRP Elements or DD-Relevant MRP Elements.The MRP elements display with Date, MRP element, Actions, Additional Information, Spike, Quantity, and Projected Stock.In the Product Information area, Product Data, MRP Data, Lot Sizing, Scheduling, and Source of Supply display. | The screen Replenishment Planning Details displays.If the material type is D2, then the dependent requirements from planned orders may impact the projected stock for S-201. |  |
| 7 | Convert Planned Order into Production Order | In the Supply/ Demand List area, you can see the new PldOrd XXX with the rounding quantity of Proposed Quantity.Choose the expand icon in Actions. You can choose Edit or Convert or Delete for planned order.Choose Convert.Then choose Convert on the Convert screen.The PrdOrd XXX displays as MRP element, you can choose it and choose Display Production Order, and it navigates to Production Order Display: Header screen.Note down the production order number. | The selected planned order is converted to Production Order: XXX.You can choose Edit or Convert or Delete for planned order.If the material has rounding value defined in MRP1 view in material master data, then it supports Apply Rounding when editing.You can only choose Edit for production order.You can choose Create Order button if necessary. |  |
| 8 | Check Results | Go to the Replenishment Planning Details screen and choose back icon.Check the updated Net Flow Position, it shall be same value as or a little bigger value than maximum stock quantity.Check the updated Proposed Quantity, the value shall be blank this time.Check the updated Planning Priority, it should be 100.00% in green or above 100% in blue. | Now the planning status is changed from yellow/red into green or black depending on the resulting stock level. If 100% of max. stock the status is green but when above 100% of max. stock the status turns black. |  |

### Replenishment Execution

#### Replenishment Execution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can check the On-hand Stock status for buffered products, S-201.

If the on-hand stock is above safety stock, then please proceed step [Post Goods Issue](#unique_21) [page ] 29.

If the on-hand stock is under alert (below safety stock) and you could see Expedite Supply button, then please skip and proceed to step [Replenishment Execution Review](#unique_22) [page ] 30.

If the on-hand stock is under alert (below safety stock) and you could only see Expedited On XXX information, then please skip and proceed to step [Succeeding Production Execution](#unique_23) [page ] 32

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Replenishment Execution - By On-Hand Status (F6242) . | The Replenishment Execution screen displays. |  |
| 3 | Filter Product | On the Replenishment Execution screen, make the following entries and choose Go:Search: S-201On-Hand Stock Status: Select all status | You could customize the filters by clickingAdapt Filters button.If there are no results displayed in the system, please confirm whether the Area of Responsibility is correctly maintained for plant 3310.Click User > App Settings > Area of Responsibility, thenArea of Responsibility Screen displays. |  |
| 4 | Check Results for Filtered Products | You could see the columns of On-Hand Buffer Status, On-Hand Stock, Open Supply, and Execution Action for buffered product, S-201.Please choose the Settings icon to display the buffer levels, Maximum Stock (DLT), Reorder Point (DLT), and Safety Stock (DLT).Or you could click against Product S-201, and the screen displays with product general information, Safety Stock (DLT), Reorder Point (DLT), Maximum Stock (DLT) and Decoupled Lead Time.You could also navigate to links, Manage Buffer Levels (F2706), Manage Product Master Data (F1602).Tip Choose More Links, and select Manage Buffer Levels (F2706) and Manage Product Master Data (F1602). Then choose OK. | You could customize the columns by click the Settings icon.On-Hand Buffer Status = On-hand stock / Safety Stock |  |
| 5 | Check Expedite Supply | Check whether the Expedite Supply button displays or On-Hand Buffer Status is below 100% for buffered product, S-201.If yes, then skip and proceed to step [Replenishment Execution Review](#unique_22) [page ] 30.If nothing displays in Execution Action column, then proceed to step [Post Goods Issue](#unique_21) [page ] 29.If the status information displays in Execution Action column, which indicates you have expedited the open supply before and current scenario is not worse, so please skip and proceed to step [Succeeding Production Execution](#unique_23) [page ] 32 | Note down the On-Hand Stock, Open Supply, Safety Stock for buffered product S-201.In column Execution Action, non-blank value displays when the on-hand stock is below safety stock and open supply quantity is not zero.If the material is not expedited before, then Expedited Supply button displays.If the material is expedited before,If the open supply quantity is more than expedited supply quantity last time or the current on-hand stock status is lower than the on-hand stock status for last expedited execution, the Expedited Button displays.If not, then the status information like Expedited on XXX displays.So, if the Expedite Supply button is missing here, please analysis the scenario and choose proper action. |  |
| 6 | Check Replenishment Details | Choose the row for buffered product S-201, it will navigate to Replenishment Execution Details screen.You could choose Expand Node icon to check the low level material for buffered product S-201.You could also check the Supply/Demand List, Product Information.In Supply/ Demand List area, stock requirements list with Date, MRP element, Additional Information, Spike, Quantity, and Projected Stock.In Product Information area, Product Data, MRP Data, Lot Sizing, Scheduling and Source of Supply display. | A new screen displays for replenishment details, supply/demand list and product information |  |

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, goods issue will be posted for buffered product S-201, to make the on-hand stock status changing into Below Safety Stock.

The quantity of the goods issue is critical. It can consume the on-hand stock of S-201 and make it drop below safety stock.

The quantity of goods issue shall be bigger than on-hand stock subtracting safety stock. (GI quantity > on-hand stock - safety stock)

After finishing the step, proceed to step [Replenishment Execution Review](#unique_22) [page ] 30.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Post Goods Movement screen displays. |  |
| 3 | Select Goods Issue-Other | Make the following entries:Trans./Event: Goods IssueReference Document: Other |  |  |
| 4 | Specify Material | Make the following entries and press Enter:Document Date : <Today’s date>Posting Date: <Today’s date>Movement type: 201Material: S-201Quantity: <Quantity>Plant: 3310Storage Location: 331B for S-XX and 331C for R-XX products. | Make sure that the quantity shall never be larger than the on-hand stock level.GI quantity > on-hand stock - safety stock and GI quantity < on-hand stock. The on-hand stock and safety stock are the quantity you noted down in step [Replenishment Execution](#unique_20) [page ] 27. |  |
| 5 | Enter Cost Center | On the Account Assignment tab:Cost Center: <Cost Center> - you can search with company code 3310, and choose cost center, for example, 33101301 |  |  |
| 6 | Check | Choose Check. | Document is ok. |  |
| 7 | Post | Choose Post. | Material document XXX posted. |  |

#### Replenishment Execution Review

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the On-hand Stock status for buffered products S-201.

The on-hand stock is expected to be under alert (below safety stock). If not, then return to step [Post Goods Issue](#unique_21) [page ] 29 to do so.

With this app, you can view today's stock situation for each product and check that sufficient on-hand stock is available for production. Using this information, the planner can try to speed up replenishment by contacting the supplier of a purchase orders or the production supervisor of the component production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Replenishment Execution - By On-Hand Status (F6242). | The Replenishment Execution screen displays.You could also refer to step [Check Planner Overview](#unique_18) [page ] 23 and navigate to Replenishment Execution - By On-Hand Status (F6242) app as well. |  |
| 3 | Filter Product | On the Replenishment Execution screen, make the following entries and choose Go:Search: S-201On-Hand Stock Status: Select all status | You can customize the filters by choosing Adapt Filters.If there are no results displayed in the system, confirm whether the Area of Responsibility is correctly maintained for plant 3310.Select User > App Settings > Area of Responsibility , and then the My Area of Responsibility screen displays. |  |
| 4 | Check Results for Filtered Products | You can see the columns of On-Hand Buffer Status, On-Hand Stock, Open Supply, and Execution Action for buffered product S-201.Choose the Settings icon to display the buffer levels, Maximum Stock (DLT), Reorder Point (DLT), and Safety Stock (DLT). Then choose OK. | You can customize the columns by choosing the Settings icon.On-Hand Buffer Status = On-Hand Stock / Safety Stock |  |
| 5 | Choose Expedite Supply | The Expedite Supply button occurs for buffered product S-201.Choose Expedite Supply. The Expedite Supply screen displays. | If Expedite Supply is missing in the Execution Action column:If nothing displays in Execution Action column, return to step [Post Goods Issue](#unique_21) [page ] 29 again to set a proper quantity for goods issue of S-201.If the status information displays in Execution Action column, which indicates you have expedited the open supply before and current scenario is not worse, so please proceed to step [Succeeding Production Execution](#unique_23) [page ] 32. |  |
| 6 | Check Details | On the Expedite Supply screen, you could see generic information, like On-Hand Buffer Status, On-Hand Stock, Below On-Hand Alert Threshold by and Below Safety Stock by fields.The open supply listed in the order section.You can see Order Progress information.For unconfirmed production order, you can change Planned Availability Date into an earlier date and choose Save and Expedite. Then the successful information screen displays.You can choose PrdOrd XXX in ID column to navigate into the Manage Product Master Data screen to see order details. | You have successfully expedited supply. |  |

#### Succeeding Production Execution

After convert the planned order to production order, please execute traditional production execution for product S-201, refer to scope item BJ5 - Make-to-Stock Production – Discrete Manufacturing.

|  |
| --- |
| Note The relevant production orders are based on the one created in [Replenishment Planning](#unique_19) [page ] 25 of this test script. |

Execute traditional production execution.

- Release Production Order for Final Assembly
- Pick components for Final Assembly
- Final Confirmation of Production Operations for Final Assembly

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to post the goods receipt for the production order of S-201.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori App | Open Post Goods Movement (MIGO). | The Post Goods Movement (MIGO) screen displays. |  |
| 3 | Enter Goods Receipt Order Data | Make the following entries and press Enter:Trans./Event: Goods ReceiptReference Document: OrderOrder Number: <Production order number you noted before>GR goods receipt: 101Document Date: defaultPosting Date: default | Screen name can deviate until the first two entries are selected.The production order is what you noted down in step Convert Planned Order to Production Order for buffered product S-201. |  |
| 4 | Enter Quantity | Choose the Quantity tab and enter the quantity you confirmed in the previous step. |  |  |
| 5 | Choose Storage Location | On the Where tab, choose the storage location 331B, which is Std. storage 2 |  |  |
| 6 | Set Item OK Indicator | Set Item OK indicator for each item. |  |  |
| 7 | Check and Post | Choose Check and then choose Post. | The system displays the message: Material document 500xxxxxxx posted. |  |

#### Replenishment Execution Review

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can check the On-hand Stock status for buffered products, S-201.

The on hand stock is increased now.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Replenishment Execution - By On-Hand Status (F6242). | The Replenishment Execution screen displays. |  |
| 3 | Filter Product | On the Replenishment Execution screen, make the following entries and choose Go:Search: S-201On-Hand Stock Status: Select all status | You could customize the filters by clickingAdapt Filters button.If there are no results displayed in the system, please confirm whether the Area of Responsibility is correctly maintained for plant 3310.Click User > App Settings > Area of Responsibility, thenArea of Responsibility Screen displays. |  |
| 4 | Check Results for Filtered Products | You could see the columns of On-Hand Buffer Status, On-Hand Stock, Open Supply, and Execution Action for buffered product, S-201.Choose the Settings icon to display the buffer levels, Maximum Stock (DLT), Reorder Point (DLT), and Safety Stock (DLT). Then choose OK. | You could customize the columns by choose the Settings icon.On-Hand Buffer Status = On-Hand Stock / Safety Stock. |  |
| 5 | Check Replenishment Details | Choose the row for buffered product S-201, it will navigate to Replenishment Execution Details screen.The stock quantity is increased. | The screen Replenishment Execution Details displays. |  |

### Projected On-Hand Alerts

#### Check Projected On-Hand Alert

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can check the current projected on-hand stock for product S-201.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Projected On-Hand Alerts - Stockout (F6243) | The Projected On-Hand Alerts screen displays. |  |
| 3 | Filter Product | On the Projected On-Hand Alerts screen, make the following entries and choose Go:Projected On-Hand Alerts: Select All AlertsSearch box: S-201 | You could customize the filters by choosing Adapt Filters.If there are no results displayed in the system, it indicates the projected on-hand stock statuses for all buffered products are safe. Thus no action required and you could just skip following steps. |  |
| 4 | Check Stock Alert for Filtered Products | You can see the time in column Stockout Alert, Threshold Alert, and Safety Stock Alert for buffered product. | The time for Stockout Alert shows you when the projected stock is lower than zero; the time for Threshold Alert shows you when the projected stock is lower than threshold; the time for Safety Stock Alert shows you when the projected stock is lower than safety stock.You can customize the columns by choosing the Settings icon.For product S-201, the stockout alert, threshold alert, or safety stock alert can be empty as the projected stock is in good status after replenishment order executed in [Replenishment Execution](#unique_20) [page ] 27, then proceed from step [Create Situation for Safety Stock Alert (Optional)](#unique_27) [page ] 36 to create situation for alerts.If the stockout alert, threshold alert or safety stock alert already exists, you could check alerts details directly in test step [Review Projected On-Hand Alert](#unique_31) [page ] 38 and skip all the proceeding steps. |  |
| 5 | Check Safety Stock | Choose the Settings icon, and select Safety Stock (DLT), Safety Stock On Safety Stock Alert and Safety Stock On Threshold Alert. Choose OK.Choose against the date for any alert, then you could see Projected On-Hand Status, Date, Projected Stock and Safety Stock. | Note down Safety Stock quantity. |  |
| 6 | Navigate to Details | Choose the row for any buffered product, and it will navigate to the Projected On-Hand Alerts Details screen. | You can see alert details on the Projected On-Hand Alerts tab.If the tab is missing, note down the projected stock quantity and the End of Decoupled Lead Time, proceed from step [Create Situation for Safety Stock Alert (Optional)](#unique_27) [page ] 36 to create the qualified demand for product.If the tab exists, you can skip all the proceeding steps and check the Supply/Demand List tab, you can check Planning View and Execution View, you can also choose Chart icon to get a more intuitive view for stock projection.On the Supply/Demand List tab, you can switch to the Planning View and Execution View. |  |

#### Create Situation for Safety Stock Alert (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the production order for finished products F-10A is created as qualified demand for S-201 directly. Pay attention to creating the correct order quantity and order date to make the projected stock is just between safety stock and threshold.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Production Order (CO01). | The Production Order Create: Initial Screen displays. |  |
| 3 | Enter the Order Information | Make the following entries and choose Enter:Materials : F-10AProduction Plant: 3310Order Type: YBM1 | The Production Order Create: Header screen displays. |  |
| 4 | Enter the Order Details | Make the following entries and choose Enter:Quantity: <Quantity>Start Date: <Date>Scheduling Type: Forwards | The quantity and date for production order is quite critical.Regarding to design the production order quantity, it could consume projected stock of S-201 and could just make the projected stock of S-201 is between threshold quantity and safety stock quantity, and would cause the safety stock alert.Production order quantity for F-10A > Projected Stock – safety stock of S-201; and Production order quantity for F-10A < Projected Stock – 0.5*safety stock of S-201.The date shall be between Today and End of Decoupled Lead Time. |  |
| 5 | Save | Choose Save and make a note of your production order number |  |  |

#### Review Projected On-Hand Alert (Optional)

Repeat step [Check Projected On-Hand Alert](#unique_26) [page ] 35. When navigating to the Projected On-Hand Alerts Details screen, you can find the new Projected On-Hand Alerts tab with the Projected On-Hand Status in orange, which indicates safety stock alert.

Note down the latest Projected Stock, Safety Stock, and Threshold.

#### Create Situation for Threshold Alert (Optional)

Repeat step 4.3.2 Create Production Orders, create a new production order of F-10A as qualified demand of S-201 to make its projected stock under threshold. Pay attention to creating the correct order quantity and order date to make the new projected stock is just between threshold and zero.

In order to meet the situation, the second production order quantity of F-10A shall be between <the latest Projected Stock - threshold> and <the latest Projected Stock>.

The date shall be between the first order date and End of Decoupled Lead Time.

#### Create Situation for Stockout Alert (Optional)

Repeat step 4.3.2 Create Production Orders, create a new production order of F-10A as qualified demand of S-201 to make its projected stock under zero. Pay attention to creating the correct order quantity and order date to make the new projected stock is lower than zero.

In order to meet the situation, the third production order quantity of F-10A shall be bigger than the latest Projected Stock in step 4.3.5.

The date shall be between the second order date and End of Decoupled Lead Time.

#### Review Projected On-Hand Alert

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can check 3 kinds of alert for projected on-hand stock of product S-201.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Projected On-Hand Alerts - Stockout (F6243). | The Projected On-Hand Alerts screen displays. |  |
| 3 | Filter Product | On the Projected On-Hand Alerts screen, make the following entries and choose Go:Search box: S-201Projected On-Hand Alerts: Mark All Alerts | You can customize the filters by choosing Adapt Filters. |  |
| 4 | Check Stock Alert for Filtered Products | You could see the time in Stockout Alert, Threshold Alert, Safety Stock Alert for buffered product. | The time for Stockout Alert shows you when the projected stock is lower than zero; the time for Threshold Alert shows you when the projected stock is lower than threshold; the time for Safety Stock Alert shows you when the projected stock is lower than safety stock. |  |
| 5 | Check Alert Details | Choose against the date for any alert, and then you can see Projected On-Hand Status, Date, Projected Stock, and Safety Stock. | Note down the date if necessary. |  |
| 6 | Navigate to Details | Choose the row for any buffered product, and it navigates to the Projected On-Hand Alerts Details screen. | You can see alert details on the Projected On-Hand Alerts tab.On the Supply/Demand List tab, you can switch to the Planning View and Execution View.Choose the Chart icon, and you can have an intuitive view for stock projection. |  |

### Review Historical Buffer Performance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can check historical buffer performance with stock details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Historical Buffer Performance - Outliers in last month (F7147). | The Historical Buffer Performance screen displays. |  |
| 3 | Filter Products | On the Historical Buffer Performance screen, make the following entries and choose Go:Evaluation Horizon: <Last Quarter>Plant: 3310 | You can customize the filters by choosing Adapt Filters.If there are no results displayed in the system, also confirm whether the Area of Responsibility is correctly maintained for plant 3310.Choose the user icon and select App Settings to open the Area of Responsibility screen. |  |
| 4 | Check Outliers for Buffered Products | You can see the Outlier Micro Chart, Total Outliers, Low Red, High Red for buffered products in the Buffered Stock Product area. |  |  |
| 5 | Navigate to Historical Stock Product Details | Choose the row of a specific buffered product.You can see Stock Zone Overview, Total Outliers, Low Red, High Red, Above High Red, Low Yellow, High Yellow in Outliers Occurrence Details area for each month. | The Historical Buffer Product Details screen displays. |  |

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 1Y2 - Demand-Driven Buffer Level Management | After replenishment execution, you could proceed scenario 1Y2 - Demand-Driven Buffer Level Management.The replenishment process shall loop back into buffer positioning to continuously improve material flow and process flow. Scenarios 2QI and 1Y2 are in a loop. |

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
> Flagged while digesting this document, not verified: Final check in Replenishment Planning says the resulting priority is 100.00% in green or above 100% in blue, while its expected result says the status turns black above 100% of max stock.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Create Demand for Finished Goods says to skip the whole chapter when S-201 is MRP type D2, yet Option 1 contains the D2-only step 'Firm Planned Order' and Option 2 the D2-only 'Create Firmed Planned Order', which the same text routes D2 users to.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/test-script-demand-driven-buffer-level-management-1y2-ae-sap-s-4hana-c]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2QI_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 77,515 chars in the whole document
