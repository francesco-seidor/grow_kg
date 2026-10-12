---
id: 12-production-and-manufacturing/test-script-production-order-combination-7to-ae-sap-s-4hana-cloud-publ
title: "Test Script: Production Order Combination (7TO_AE) - SAP S/4HANA Cloud Public Edition 2608 (7TO_S4CLD2608_BPD_EN_AE)"
description: "SAP Best Practices test script (UAE localization) for scope item 7TO: combining MTS/MTO production orders into a combined order, executing it and reviewing original orders."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/production-order-combination]
aliases: [7TO_S4CLD2608_BPD_EN_AE]
keywords: [Production Order Combination, combine production orders, review combined orders, posting rules, release production orders, production order confirmation, material staging, component picking, production goods receipt, maintain combined orders]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7TO_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1227
topic: 12-production-and-manufacturing/production-order-combination
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Production Order Combination (7TO_AE) - SAP S/4HANA Cloud Public Edition 2608 (7TO_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7TO_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Production Order Combination** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Production Order Combination (7TO_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232860670)

[2 Prerequisites 4](#_Toc232860671)

[2.1 System Access 4](#_Toc232860672)

[2.2 Roles 4](#_Toc232860673)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232860674)

[2.4 Business Conditions 7](#_Toc232860675)

[2.5 Preliminary Steps 8](#_Toc232860676)

[2.5.1 Create Standard Production Orders 8](#_Toc232860677)

[2.5.1.1 Alternative 1: Create Standard MTS Production Orders 8](#_Toc232860678)

[2.5.1.1.1 Create Planned Independent Requirements 9](#_Toc232860679)

[2.5.1.1.2 Material Requirements Planning at Plant Level 10](#_Toc232860680)

[2.5.1.1.3 Evaluate Stock/Requirements Situation 12](#_Toc232860681)

[2.5.1.1.4 Conversion to Production Orders for Subassembly and Final Assembly 14](#_Toc232860682)

[2.5.1.2 Alternative 2: Create Standard MTO Production Orders 15](#_Toc232860683)

[2.5.1.2.1 Create Sales Order 16](#_Toc232860684)

[2.5.1.2.2 Material Requirements Planning for Sales Order 18](#_Toc232860685)

[2.5.1.2.3 Create Production Order 20](#_Toc232860686)

[2.5.2 Initial Stock Posting for the Material in BoM 22](#_Toc232860687)

[2.5.2.1 Create Initial Material Stock 22](#_Toc232860688)

[2.5.2.2 Initial Stock Posting for the Material in BoM 24](#_Toc232860689)

[3 Overview Table 26](#_Toc232860690)

[4 Test Procedures 28](#_Toc232860691)

[4.1 Combine Production Orders 28](#_Toc232860692)

[4.1.1 Alternative 1: Combine Production Orders – Combine Orders 28](#_Toc232860693)

[4.1.2 Alternative 2: Combine Production Orders – Combine Operations 29](#_Toc232860694)

[4.2 Review Combined Orders 30](#_Toc232860695)

[4.2.1 Select Orders Using the Combination Indicator 30](#_Toc232860696)

[4.2.2 Review Order Details 31](#_Toc232860697)

[4.2.3 Review Posting Rules 33](#_Toc232860698)

[4.3 Material Staging 34](#_Toc232860699)

[4.3.1 Material Staging for Subassembly 34](#_Toc232860700)

[4.4 Release Combined Orders 36](#_Toc232860701)

[4.5 Pick Components 37](#_Toc232860702)

[4.5.1 Pick Components (Picking List) 37](#_Toc232860703)

[4.6 Confirm Production Order Operations 39](#_Toc232860704)

[4.6.1 Confirm Operations Before Last Operation 39](#_Toc232860705)

[4.6.2 Confirm Last Operation 40](#_Toc232860706)

[4.7 Post Goods Receipts for Original Order 42](#_Toc232860707)

[4.7.1 Post Goods Receipt for Production Order 42](#_Toc232860708)

[4.7.2 Review Original Order Status 43](#_Toc232860709)

[5 Appendix 45](#_Toc232860710)

[5.1 Remove from Combined Order 45](#_Toc232860711)

[5.2 Add to Combined Order 46](#_Toc232860712)

[5.3 Cancel Order Combination 47](#_Toc232860713)

[5.4 Succeeding Processes 48](#_Toc232860714)

## Purpose

Overview

This scope item enables a production order combination scenario for make-to-stock and make-to-order production orders for customers who want to reduce production costs and increase production efficiency.

The process starts with identifying production orders that are still in a created status and can be combined based on criteria (such as Material, Material Attributes, Production Plant) and combining them to create a combined production order, which takes over the execution of operations with the necessary consolidated components from the underlying production orders.

Combined orders can be released for production with their combined operations from their underlying original orders also released. Combined operations from the combined order can be confirmed. When the last combined operation is confirmed, the underlying original orders are also confirmed with the distributed yield quantity. Components for combined order are consumed in the goods issue, and the goods receipt then always happens for the receiving original orders.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

The test is conducted in the following systems:

| System | Details |
| --- | --- |
| System | Access using the SAP Fiori® Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | FG228 | FIN228, MTO, PD, Fifo | Material FG228 adopts Strategy Group B6 (Planning w/o final assy – MTO w/o costing) in material master - MRP3 view. |
| Material | FG227 | FIN227, MTO, PD | To test order BOM management process, you can use FG227.Material FG227 adopts Strategy Group S5 (Planning w/o final assy – MTO w/o costing) in material master - MRP3 view. |
| Material | SG21 | SEMI21,PD,RepetitiveManuf. |  |
| Material | SG22 | SEMI22,PD,Phantom |  |
| Material | SG25 | SEMI25,PD,ExternalProcurement |  |
| Material | SG23 | SEMI23,PD,Subcontracting |  |
| Material | RM13 | RAW13,PD,Subcontracting |  |
| Material | RM14 | RAW14,PD,Subcontracting |  |
| Material | SG224 | SEMI224,MTO,PD,Subassembly |  |
| Material | RM16 | RAW16,PD |  |
| Material | RM20 | RAW20,PD |  |
| Material | RM27 | RAW27,PD,PackagingBox |  |
| Material | RM122 | RAW122,PD,Batch-Fifo,ProcureImport |  |
| Material | RM124 | RAW124,VB,Consumption,FixedBin |  |
| Material | RM128 | RAW128,PD,Consignment |  |
| Customer | 33100001 | Domestic UAE Customer 1 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

Bill of Material Structure for SG224

This overview shows the bill of material structure and the usage of each component if you have activated all optional enhancements.

| Material | Level | Material Type | Unit | Characteristic of Material |
| --- | --- | --- | --- | --- |
| SG224 | 0 | SEMI | PC | Semifinished Good Repetitive Manuf. |
| RM124 | 1 | RAW | PC | Raw Material |

Bill of Material for FG228 and FG227

This overview shows the bill of material structure and the usage of each component if you have activated all optional enhancements.

| Material | Level | Material Type | Unit | Characteristic of Material | Optional Enhancements |
| --- | --- | --- | --- | --- | --- |
| FG228 | 0 | FERT | PC | Finished Good for MT0 processing |  |
| FG227 | 0 | FERT | PC | Finished Good for MT0 processing |  |
| SG22 | 1 | SEMI | PC | SF, Phantom Assembly | Initial Stock Posting |
| RM16 | 2 | RAW | PC | External procured | Initial Stock Posting |
| RM122 | 1 | RAW | PC | External procured with Batch Management (FIFO-Strategy) | Initial Stock Posting |
| RM128 | 1 | RAW | PC | External procured with Consignment Processing | Initial Stock Posting |
| SG25 | 1 | SEMI | PC | SF Ext. Procurement | Initial Stock Posting |
| SG224 | 1 | SEMI | PC | Internal production of subassembly (MTO strategy) |  |
| RM27 | 1 | RAW | PC | External procured, Packaging Box | Initial Stock Posting |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BND | Create Customer Master - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BLD | Create Production Version - MDS |
| 2ZW | Create Batch Management Master Data - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNU - Create Costing Run - MDS | You have completed the steps described in the master data script. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the steps described in the master data script. Posting Period is up-to-date. |
| BJ5 - Make-to-Stock Production – Discrete Manufacturing | Optional: if you want to combine Make to Stock Production order |

### Preliminary Steps

#### Create Standard Production Orders

##### Alternative 1: Create Standard MTS Production Orders

This process step shows you how to create original orders for Make-to-Stock (MTS) cases.

To create MTS production orders, use the following organization data.

| Master Data | Sample Value |
| --- | --- |
| Material | FG126 |
| Plant | 3310 |

Follow the steps below to create MTS production orders:

- [Create Planned Independent Requirements](#unique_8) [page ] 9
- [Material Requirements Planning at Plant Level](#unique_9) [page ] 10
- [Evaluate Stock/Requirements Situation](#unique_10) [page ] 12
- [Conversion to Production Orders for Subassembly and Final Assembly](#unique_11) [page ] 14

|  |
| --- |
| Note Make a note of the order number you created for later steps. |

###### Create Planned Independent Requirements

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

###### Material Requirements Planning at Plant Level

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

###### Evaluate Stock/Requirements Situation

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

###### Conversion to Production Orders for Subassembly and Final Assembly

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

##### Alternative 2: Create Standard MTO Production Orders

This process step shows you how to create original orders for Make-to-Order (MTO) cases.

To create MTO production orders, use the following organization data.

| Master Data | Sample Value |
| --- | --- |
| Material | FG228/FG227 |
| Plant | 3310 |

Follow the steps below to create MTO production orders:

- [Create Sales Order](#unique_13) [page ] 16
- [Material Requirements Planning for Sales Order](#unique_14) [page ] 18
- [Create Production Order](#unique_15) [page ] 20

|  |
| --- |
| Note Make a note of the order number you created for later steps. |

###### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create a sales order according to customer requirement. Later customer may require a technical change for the product. In this case, a sales order is created without reference to quotation. For this test, you can use sample material FG227.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders (F1873) screen, choose Create > Create Sales Order – VA01 .Make the following entries and choose Continue:Order Type: ORSales Organization: 3310 | The Create Standard Order: Overview screen displays. |  |
| 4 | Enter Order Details | Make the following entries and press Enter:Sold-to Party: 33100001Ship-to Party: 33100001Cust. Reference: <PO number>Cust. Ref. Date: <Today's Date>On the Sales tab:Req.deliv.date: <Delivery Date (Today + 1 Month)>In the All Items table:Material: FG227Order Quantity: <Quantity>, for example, 10 | The Create Standard Order: Overview screen displays. |  |
| 5 | Choose Billing Plan | On the Create Standard Order: Overview screen, in the All Items table, select the item. Choose Menu > Goto > Item > Billing Plan .Note If the Selection Criteria - Milestones for billing plan dialog box displays, choose Cancel. |  |  |
| 6 | Enter Billing Plan Details and Save | On the Create Standard Order: Item Data screen, make the first entry (down payment) with the following data:Billing Date: <Today's Date>DtDS (Date Description): <Y009>Bill.value: <Down Payment Value to be Invoiced>, for example, <10>DCat (Date Category): <03>Press Enter.Block: Delete <Y2>Make the second entry with the following data:Billing Date: <Today's Date + 1 Month>DtDS (Date Description): <Y008>DCat (Date Category): <02>Press Enter.Choose Back icon, and choose Save.Note If the sales order requires approval, refer to Sell from Stock (BD9) scope item, and complete the Process Sales Order Approval (Optional) step.After sales order is saved, you can check costing of sales order in display mode.Follow menu path Menu > Extras > Costing .On the Costing Structure session, check if the component is the same as in BoM of FG227. | A message displays: Standard Order XXXXX has been saved. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Search for Sales Order | Use filter bar to search for the created sales order.Enter <sales order number> in the Sales Order field. | Searched sales order displays. |  |
| 4 | Print Sales Order | Choose sales order number and choose Display Sales Order - VA03 (If it is not displayed, find it from More Links).On the Display Standard Order XXX: Overview screen, choose Header Output Preview.Select the line created with completed status and choose Display Document.Choose Print icon to print your sales order. | Sales order is printed. |  |

|  |
| --- |
| Note If you maintain different material prices by Ledger (scope item 1ZT - Managing Material Price Changes and Inventory Values) and want to do Ledger specific sales order costing, please refer to the scope item BEG - Standard Cost Calculation and its step Appendix > Manage Order BOM Cost Estimates in Parallel Valuation . |

###### Material Requirements Planning for Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to start the MRP run for the sales order you created before.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor External Requirements (F0246A). | The Monitor External Requirements screen displays. |  |
| 3 | Check Default Area of Responsibility | Choose user icon and select App Settings. In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, ensure that only the following entries are assigned:Plant 1 AE 3310MRP Controller 001 (001)Tip If not, set the AOR Status toggle for the aforementioned entries to AOR Is Assigned and for all the other entries to AOR Is Unassigned.Choose Back. |  |  |
| 4 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 5 | Search for Material | On the upper-right screen, choose Adapt Filters to display more filter options. In the Adapt Filters dialog box, select Material and choose OK.Enter the following data and choose Go:Material: FG228 or FG227Select the line item with your sales order number, such as CusOrd-XXXXX-10.Choose Manage Requirements. | The Manage External Requirements screen displays. |  |
| 6 | Start MRP Run | Choose the material item. On the lower-right screen, choose Start MRP Run. | An MRP run is started immediately in background. |  |
| 7 | Check Generated Planned Order | Choose the generated planned order, and choose Open > Document Info .Choose Components, and check if the components are the same as those in BoM. | If you have entered BOM explosion number for material in sales order, this BOM explosion number will be copied to generated planned order. |  |

###### Create Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a production order without an external processing operation.

Prerequisite

Planned orders for assembly finished good (FG228 or FG227 ) is generated in the same way as for parts production.

Procedure

Access the transaction choosing one of the following navigation options:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments screen displays. |  |
| 3 | Check Default Area of Responsibility | Choose user icon and select APP Settings icon. In the MRP Settings dialog box, choose Area of Responsibility.Check if only the following entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status button to set the status for the above entry to AOR Is Assigned if not yet assigned.Choose AOR Status button to unassign the rest of other entries.Choose Back. |  |  |
| 4 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 5 | Search for Material | Enter the following data and choose Go:Material: <FG228 or FG227>Select the line item with your sales quotation / sales order number, such as CustSt XXXXXX-10..Choose Manage Materials. | The Manage Material Coverage screen displays.Note that you select the right individual segment for the WBS ID. |  |
| 6 | Convert Planned Order to Production Order | Choose the material item and then choose the generated planned order on the right screen. Select Convert from the dropdown list under column Actions. Choose Convert. | A message displays: Production order XXXXXXXX was created. |  |
| 7 | Rescheduling Check (Optional) | On the Stock/Requirements List tab, the Rescheduling column displays the rescheduling status of the following MRP Elements.PurReqPurchase OrdersPlanned OrdersProduction OrdersProcess OrdersIf needed, you can choose the following icons in Rescheduling column for corresponding functions:Reschedule in (bring operation forward if the receipt element lies after the requirement date)Reschedule out (postpone operation, if the receipt element lies before the requirement date)Plan Process according to scheduleCancel ProcessExcess StockExcess in individual segment | Corresponding actions perform. |  |

#### Initial Stock Posting for the Material in BoM

|  |
| --- |
| Note Initial stock posting is not required if you want to execute complete procurement or semifinished component production processes for selected materials in the multi-level BoM of FG126, FG228, and FG227. |

This process step shows you how to post the initial stock for BoM materials FG126, FG228, and FG227.

|  |
| --- |
| Note Alternatively, you can run the procurement scope items. |

You may follow either one of the following procedures to post the initial stock for BoM materials:

- Alternative 1: To post the initial stock of BoM material FG126, follow this step: [Create Initial Material Stock](#unique_17) [page ] 22
- Alternative 2: To post the initial stock of BoM materials FG228 and FG227, follow this step: [Initial Stock Posting for the Material in BoM](#unique_18) [page ] 24

##### Create Initial Material Stock

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

##### Initial Stock Posting for the Material in BoM

|  |
| --- |
| Note Initial stock posting is not required if you want to execute complete procurement or semifinished component production processes for selected materials in the multilevel BoM of FG228 and FG227.For the semifinished material SG224, you can either post initial stock here, or run through Make-to-Order Production – Semifinished Goods Planning and Assembly (1BM) scope item first to produce enough stock before creating sales orders for finished goods.For the semifinished material SG21, you can either post initial stock here, or run through Make-to-Stock Production – Repetitive Manufacturing (BJH) scope item to produce enough stock via repetitive manufacturing process.For the remaining semifinished and raw materials in the multilevel BoM of FG228 or FG227 you can post initial stock. |

Purpose

This process step shows you how to post initial stock for BoM materials of FG228 and FG227.

|  |
| --- |
| Note Alternatively, you can run the procurement scope items. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) | The Goods Receipt Other - XXX (your user name) screen displays. |  |
| 3 | Enter Details | Make the following entries:Trans./Event: Goods ReceiptReference Document: OtherIn the Detail Data section, make the following entries and press Enter. Select Next Item icon to add entries.On the Where tab:Goods Movement Type: 561 (Init.entry of stBal.)Plant: 3310Storage Location: 331BOn the Quantity tab:Quantity: <Quantity>, for example, <100>On the Material tab:Material: <BOM Material>, see the Bill of Material Structure for FG228 and FG227 in the Master Data, Organizational Data, and Other Data section for a detailed materials list.Run through Make-to-Order Production – Semifinished Goods Planning and Assembly (1BM) test script if you do not want to post initial stock for SG224.Select Item OK, and choose Check. | A message displays: The Document is OK. You also post initial stock for material RM20 in case you test with material FG227. |  |
| 4 | Post | Confirm the message that the batch has been created and choose Post. | A message displays: Material document XXXXXXXX posted. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Combine Production Orders |  |  |  |
| [Alternative 1: Combine Production Orders – Combine Orders](#unique_20) [page ] 28 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | A combined order is created. |
| [Alternative 2: Combine Production Orders – Combine Operations](#unique_21) [page ] 29 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | A combined order is created. |
| Review Combined Orders |  |  |  |
| [Select Orders Using the Combination Indicator](#unique_22) [page ] 30 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | The combined order and its child original orders are displayed. |
| [Review Order Details](#unique_23) [page ] 31 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | The details of the original orders are reviewed. |
| [Review Posting Rules](#unique_24) [page ] 33 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | The posting rule details are reviewed. |
| [Material Staging](#unique_25) [page ] 34 |  |  |  |
| [Material Staging for Subassembly](#unique_26) [page ] 34 | Production Operator - Discrete Manufacturing | Stage Materials for Production (MF60) | Materials are staged for subassembly. |
| [Release Combined Orders](#unique_27) [page ] 36 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | The combined order is released. |
| [Pick Components](#unique_28) [page ] 37 |  |  |  |
| [Pick Components (Picking List)](#unique_29) [page ] 37 | Production Operator - Discrete Manufacturing | Pick Components for Production Orders (CO27) | The components are post. |
| Confirm Production Order Operations |  |  |  |
| [Confirm Operations Before Last Operation](#unique_30) [page ] 39 | Production Operator - Discrete Manufacturing | Confirm Production Order Operation (CO11N) | All operations except the last operation is confirmed. |
| [Confirm Last Operation](#unique_31) [page ] 40 | Production Operator - Discrete Manufacturing | Confirm Production Order Operation (CO11N) | The last operation of combined order is confirmed. |
| [Post Goods Receipts for Original Order](#unique_32) [page ] 42 |  |  |  |
| [Post Goods Receipt for Production Order](#unique_33) [page ] 42 | Warehouse Clerk | Post Goods Receipt for Production Order (F3110) | Goods receipt for production order is posted. |
| [Review Original Order Status](#unique_34) [page ] 43 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | The status of the original order is checked. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Combine Production Orders

#### Alternative 1: Combine Production Orders – Combine Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After standard production orders are generated in the section Create Standard Production Orders, the production supervisor may decide to completely combine them to a combined order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). |  |  |
| 3 | Search for Original Orders | On the Manage Production Orders screen, make the following entry, and then choose Go. You can also filter your standard production order via the filters such as Material and Plant.Order: <Order Number Created in Step Create Standard MTS Production Orders> | The target original orders are displayed in the Orders area. |  |
| 4 | Select the Original Orders | In the Orders area, select the original orders you want to combine and choose Combine Order > Create Combined Order | The Select a Reference Order dialog box pops up. |  |
| 5 | Select a Reference Order | In the Select a Reference Order dialog box, make sure the order types are YBOC. Select an original order as the reference order, and choose OK. | A combined order is created. |  |

#### Alternative 2: Combine Production Orders – Combine Operations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After standard production orders are generated in section Create Standard Production Orders, the production supervisor may decide to partially combine them to a combined order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). |  |  |
| 3 | Search for Original Orders | On the Manage Production Orders screen, make the following entry, and then choose Go. You can also filter your standard production order via the filters such as Material and Plant.Order: <Order Number Created in Step Create Standard MTS Production Orders> | The target original orders are displayed in the Orders area. |  |
| 4 | Select the Original Orders | In the Orders area, select the original orders you want to combine and choose Combine Order > Create Combined Operations . | The Select Operations to Combine dialog box pops up. |  |
| 5 | Select a Reference Order | In the Select Operations to Combine dialog box, make the following entries:Reference Order: <Reference Order Number>Order Type: <Target Combined Order Type, such as YBOC>In the Operations section, select the operations to be combined. Then choose Confirm. | A combined order is created. |  |

Result

A combined order is created.

|  |
| --- |
| NoteThe combined order type must be configured with distribution rule PP5.The order combination only supports production orders using Event-Based Costing.For the reference order: The head material of the reference order is copied to the combined order. The operations from the reference order are also copied to the combined order. |

### Review Combined Orders

#### Select Orders Using the Combination Indicator

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Combination indicator is a specific selection criteria. It is used to group combined orders that combine entire orders or some of the operations in original orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). |  |  |
| 3 | Adapt Filters | On the Manage Production Orders screen, choose Adapt Filters.Select Combination Indicator and choose OK to display it as a selection criteria. |  |  |
| 4 | Input Selection Criteria | Make the following entries and choose Go.Status: CreatedMaterial: the head material of the combined order, which is copied from reference original orderCombination Indicator: Select Combination by Order (H) for orders combination; select Combination by Operation (O) for operations combination | The combined order and its child original orders you created in section [Alternative 1: Combine Production Orders – Combine Orders](#unique_20) [page ] 28 are displayed. |  |
| 5 | Stay On the Page | Continue with the next step [Review Order Details](#unique_23) [page ] 31. |  |  |

#### Review Order Details

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the combination order is created, go through the combination order and original order to understand combination logic.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). |  |  |
| 3 | Go to Production Order Details | To proceed with the previous step, click on the order number. On the pop-up panel, choose the Related Actions icon in the bottom-right corner, and then choose Production Order. | The Production Orders screen displays. |  |
| 4 | Check Order Details | Check the following details:General Information:Request Order Type: Combined Order (Z)Total Quantity: Sum of the quantities from original ordersCombination Indicator: Combination by Order (H) or Combination by Operation (O)Dates/Times: The end date from the earliest original orderEvent-Based Posting: YesOperations:Orders combination: All the operations from reference order are copied into the combined order. For common operations, the process time is accumulated, but the setup time and teardown time are not accumulated.Operations combination: The selected operations from reference order are copied into the combined order. For common operations, the process time is accumulated, but the setup time and teardown time are not accumulated.Components:Orders combination: The components in all the original orders are copied into the combined order. The quantities of common components are accumulated.Operations combination: The components allocated to the combined operations are copied into combined BOM. The quantities of common components are accumulated. |  |  |
| 5 | Go Back to the Manage Production Orders Screen | Choose Back to go back to the Manage Production Orders screen. |  |  |
| 6 | Display Target Order | Repeat step [Select Orders Using the Combination Indicator](#unique_22) [page ] 30 to display target combined order. | The Manage Production Orders screen displays your combined order. |  |
| 7 | Go to the Details Page of the Combined Order | Choose the row of the combined order. | The Manage Production Orders screen displays. |  |
| 8 | Go to the Details of the Original Order | Navigate to the Order Items section, and you can find the combined original orders. Click on one of the order number.Then on the pop-up panel, choose the Related Actions icon in the bottom-right corner, and then choose Production Order. | The Production Orders screen displays the details of the original orders. |  |
| 9 | Check the Details of the Original Order | Navigate to the Operations section, and choose the Settings icon to adjust the layout. Select Combined Order and choose OK.You can see the combined order number displayed for combined operations. |  |  |

|  |
| --- |
| NoteOnce the original orders are combined, the combined order is the main object to manage production execution. Both the component reservation and the requirement on capacity are moved to the combined order.Once the operations are combined, the combined operations are separated from other operations in the original orders. The combined operations are disabled in the original orders. |

#### Review Posting Rules

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review posting rules to understand cost distribution logic.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). |  |  |
| 3 | Display Target Order | Repeat [Select Orders Using the Combination Indicator](#unique_22) [page ] 30 to display the target combined order. |  |  |
| 4 | Display Posting Rules – Event-Based | Select the combined order, choose Related Apps in the upper-right corner, and select Display Posting Rules – Event-Based. | The Display Posting Rules - Event Based screen displays. |  |
| 5 | Select Combined Order | On the Display Posting Rules - Event Based screen, choose the row of a combined order. | The Order – Event-Based screen displays. |  |
| 6 | Check the Details of the Posting Rules | On the Order – Event-Based screen, check the posting rule details:Receiver: original ordersEquivalence No: planned quantity of original ordersPosting Type: Full Settlement |  |  |

|  |
| --- |
| Note The posting rules for combined orders always use the original orders as receivers to show the cost distribution, which is based on planned quantity of the original orders. |

### Material Staging

This process step shows you how to do material staging for combined orders. If you have posted initial stock in section [Initial Stock Posting for the Material in BoM](#unique_16) [page ] 22, material staging is not necessary because the component is available in issuing stock.

For detailed instructions, see [Material Staging for Subassembly](#unique_26) [page ] 34.

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

### Release Combined Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to release a combined order and check the REL status of orders afterwards.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). |  |  |
| 3 | Display Target Order | Repeat [Select Orders Using the Combination Indicator](#unique_22) [page ] 30 to display target combined order. | The Manage Production Orders screen displays your combined order. |  |
| 4 | Release the Combined Order | Select your combined order and choose Release. Confirm any warning messages. | A message pops up indicating the order is released (with possible warning messages.) |  |
| 5 | Check the Status of the Released Combined Order | Click on the order number of the released combined order. On the pop-up panel, you can see the Order Status of combined order is Released. |  |  |
| 6 | Navigate to the Combined Order Details Page | Choose the row of the released combined order to go to the Manage Production Orders screen. |  |  |
| 7 | Check the Status of Original Orders | Navigate to the Order Items section, and click on the order number of the original order. On the pop-up panel, choose the Related Actions icon in the bottom-right corner, and then choose Production Order.Navigate to the Status section, and check the following details:Orders combination: the status of the original order is REL standing for released.Operations combination: if the operations in the original order are completely combined, the status of the original order is REL standing for released. If not completely combined, the status of the original order is PREL standing for partially released. |  |  |

|  |
| --- |
| Note Whenever a combined order is released, the corresponding combined operations in the original orders are released automatically. |

### Pick Components

|  |
| --- |
| Note It is possible to post components consumption to the combined order. It is not possible to post components consumption to the original order. |

For detailed instructions, see [Pick Components (Picking List)](#unique_29) [page ] 37.

#### Pick Components (Picking List)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

Ensure that sufficient material is present on stock. To check this, use Monitor Stock / Requirements List - Old Version (MD04) App.

Purpose

The released production order is now ready for picking. Only those materials that are not in the service stock at the assembly aisle are to be picked. For picking, the operator selects the specific picking list that can be called up directly with the production order number. The operator has a series of further selection options to allow for optimal worklist selection. This process step shows you how to pick components (picking list).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Pick Components for Production Orders (CO27). | The Picking List: Initial Screen displays. |  |
| 3 | Enter Relevant Search Criteria | Make the following entries and choose Execute.Profile: 000002Production Order: <Your Production Order number> | The Order Information System: Detail List of Components screen displays. |  |
| 4 | Picking | Select the relevant reservations and choose Picking. | A list of all the selected reservations displays. |  |
| 5 | Batch Determination | Some materials are batch managed, for example: RM122, select relation line item and choose Batch Determination.Make the following entry and choose Copy.Split Quantity: <split quantity> | The Batch Determination MM: Select Batches screen displays. |  |
| 6 | Post | Choose Post to post the goods movements. |  |  |

### Confirm Production Order Operations

#### Confirm Operations Before Last Operation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to confirm operations except the last operation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Confirm Production Order Operation (CO11N) app. |  |  |
| 3 | Enter Production Order and Operation | On the Enter Time Ticket for Operation Order screen, make the following entries and choose Enter:Order: <Production Order Number>Operation: <Operation Number>, for example, 0010 |  |  |
| 4 | Enter Quantities Data | In the Quantities section, make the following entries:Yield: <Yield Amount>Scrap: <Scrap Amount>In the Activities section:Setup: <Setup Time>Machine: <Machine Time>Labor: <Labor Time> | You may choose Actual Data to get default values. |  |
| 5 | Check Material Movements | In the Goods Movements section, check the material list. | The system displays an overview table of all materials for which the withdrawing is automatically done with the confirmation of the operation.If there are not any materials set for backflush (in material master), then no materials are displayed in the table. |  |
| 6 | Save Your Entries | Choose Back.For partial confirmation, select Partial confirmation from the Confirm.type dropdown list.For final confirmation, select Final confirmation from the Confirm.type dropdown list.Choose Save. | Confirmation is made. |  |
| 7 | Repeat Steps | Repeat steps 3-7 for all the operations before last operation. | Confirmation is made for all operations except the last operation. |  |

Result

You successfully confirm all operations except the last operation.

#### Confirm Last Operation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to confirm combined order operations. When you confirm the last operation, specify the distribution quantity for each original order. The app Confirm Production Operation (F3069) does not support Distribution Quantity or auto confirmation of original orders during the confirmation of the combined order. Instead, use the Confirm Production Order Operation (CO11N) app. The costs collected in a combined order are distributed back to the original order based on the proportion of distribution quantities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Confirm Production Order Operation (CO11N) app. |  |  |
| 3 | Enter Production Order and Operation | On the Enter Time Ticket for Operation Order screen, make the following entries and choose Enter:Order: <Production Order Number>Operation: <Last Operation Number>, for example, 0040Confirm.type: Final confirmation | The Quantity Distribution button appears on the top of the page. |  |
| 4 | Get Default Data | Choose Actual Data, and you can get the planned data in the following fields:In the Quantities section:Yield: <Yield Amount>Scrap: <Scrap Amount>In the Activities section:Setup: <Setup Time>Machine: <Machine Time>Labor: <Labor Time> | The planned values are automatically filled in the fields. You may adjust them manually. |  |
| 5 | Confirm Distributed Quantity | Choose Quantity Distribution to navigate to the Quantity Distribution screen. In the field Yield Quantity, you can see planned quantity of the original orders, and you can check and adjust them. Costs collected in the combined order are distributed back to the original orders in the proportion of Yield Quantity here.Choose Execute. You are navigated back to the Enter Time Ticket for Operation Order screen. |  |  |
| 6 | Check the Goods Movement | On the Enter Time Ticket for Operation Order screen, choose Goods Movements.On the Enter Confirmation for Production Order: Goods Movements screen, you can adjust the backflushed components or planned goods receipt in the case of automatic goods receipt.Then choose Back. |  |  |
| 7 | Save confirmation | On the Enter Time Ticket for Operation Order screen, Choose Save.On the following screen, it shows the original orders are confirmed as well. | The last operation of combined order is confirmed. The original orders are confirmed automatically. |  |

|  |
| --- |
| NoteIt is mandatory to specify distribution quantity, as it decides in which proportion the cost can be distributed back to the original orders.In the case of automatic goods receipt, it's posted directly to the original orders.You can also confirm combined orders at the header level using the app Confirm Production Order (CO15). Ensure you complete the confirmed quantity distribution to the original orders before saving the confirmation. Confirmed quantity distribution to the original orders should be completed before saving the confirmation. |

### Post Goods Receipts for Original Order

|  |
| --- |
| Note It is possible to post goods receipts to original orders. It is not possible to post goods receipts to combined orders. |

#### Post Goods Receipt for Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods receipt for the production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Receipt for Production Order (F3110). | The Post Goods Receipt for Production Order screen displays. |  |
| 3 | Enter Order Number | Make the following entry and press Enter:Order: <Production Order Number Created Previously> |  |  |
| 4 | Check and Post | In the Items section, select the item and choose Post.The Success dialog box displays with the following message: 1 material document(s)posted: XXXXXXXXX.Choose OK. | Goods receipt for production order has been posted. |  |

#### Review Original Order Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After you finish the actions from logistics perspective, check the status of original orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). |  |  |
| 3 | Display Target Order | Make the following entries and choose Go:Status: ConfirmedMaterial: the head material of the combined order, which is copied from template original orderCombination Indicator: Select Combination by Order (H) for the entire order combination; select Combination by Operation (O) for partial operations combination |  |  |
| 4 | Go to the Combined Order Details Page | Click on the order number. On the pop-up panel, choose the Related Actions icon in the bottom-right corner, and then choose Production Order. | The Production Orders screen displays. |  |
| 5 | Check the Status of the Combined Order | Navigate to the Status section, and you can check the status of the combined order, such as CNF and GMPS.Then go back to the Manage Production Orders main screen. |  |  |
| 6 | Go to the Object Sheet of the Combined Order | Choose the row of a target combined order. | The Manage Production Orders screen displays. |  |
| 7 | Go to the Original Order Details Page | Navigate to the Order Items section, and click on the order number.On the pop-up panel, choose the Related Actions icon in the bottom-right corner, and then choose Production Order. | The Production Orders screen displays. |  |
| 8 | Check the Status of the Original Order | Navigate to the Status section, and check the status of the original order, such as CNF, DLV, and GMPS. |  |  |

## Appendix

### Remove from Combined Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows how to remove an original order from a combined order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). |  |  |
| 3 | Input Selection Criteria | Make the following entries and choose Go:Status: CreatedMaterial: the head material of the target original orderOrder: the number of the target original order | The target original order is displayed. |  |
| 4 | Remove from Combined Order | Select the original order, and choose Combine Order > Remove from Combined Order . | The original order is removed from the combined order. |  |

|  |
| --- |
| Note A combined order must contain at least two original orders. You cannot remove an original order from a combined order that contains only two original orders, which leads to an error message. In this case, you can cancel the order combination. |

### Add to Combined Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows how to add another original order to a combined order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). |  |  |
| 3 | Input Selection Criteria | Make the following entries and choose Go:Status: CreatedMaterial: the head material of the target original orderOrder: the order number of the target original order | The target original order is displayed. |  |
| 4 | Select Target Original Order | Select the original order, and choose Combine Order > Add to Combined Order . | The Add to Combined Order dialog box is displayed. |  |
| 5 | Add to Combined Order | In the Add to Combined Order dialog box, input selection criteria in the fields, such as Order, Material, Actual Start, and Scheduled End to filter target combined order. Then select the combined order and choose OK. | The original order is added to the combined order. |  |

### Cancel Order Combination

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows how to cancel a combined order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). |  |  |
| 3 | Input Selection Criteria | Make the following entries and choose Go:Status: CreatedMaterial: the head material of the target orderOrder: the number of the target orderCombination Indicator: Select Combination by Order (H) for the entire order combination; select Combination by Operation (O) for partial operations combination | The target combined order is displayed. |  |
| 4 | Cancel Combined Order | Select the combined order, and choose Combine Order > Cancel Combined Order . Choose Yes to confirm the pop-up message. | The combined order is cancelled. |  |

|  |
| --- |
| Note The combined order is marked for deletion and all relations between the combined order and original orders are removed, including capacity requirements and component reservations for the combined order. Original orders turn into standard orders under the Request Order Type and all the capacity requirements as well as component reservations for original orders are restored. |

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 3F0 (Event-Based Production Cost Posting) | This procedure updates work-in-process calculation, overhead calculation, and variance calculation by linking the posting to the events.Note Starting from CE2105, the default Best Practice content is based on event-based result analysis for new customer install and add new country only, rather than previous period-end posting. For existing customers (who activated content before 2105), the default remain unchanged to Period-End Closing – Plant BEI till customer makes the decision to switch. For migration to Event based from Periodic, please refer to [Production Settlement in Parallel Ledgers](https://help.sap.com/viewer/4032610758dc437089f0c28320eec93f/LATEST/en-US/e49a3770f22547a392455154f3eef6e2.html). If you are still using period-end posting, you may need to refer to non-standard Scope Item BEI - Period-End Closing – Plant. |

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
- see-also :: [[12-production-and-manufacturing/test-script-make-to-stock-production-discrete-manufacturing-bj5-ae-sap]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7TO_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 80,767 chars in the whole document
