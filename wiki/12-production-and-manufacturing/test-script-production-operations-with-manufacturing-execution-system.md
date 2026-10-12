---
id: 12-production-and-manufacturing/test-script-production-operations-with-manufacturing-execution-system
title: "Test Script: Production Operations with Manufacturing Execution System (1Y5) (1Y5_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1Y5: MES integration with final assembly production order processing, roles, apps and steps."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/mes-and-shop-floor-integration]
aliases: [1Y5_S4CLD2608_BPD_EN_XX]
keywords: [Manufacturing Execution System and Third-Party Shop Floor…, manufacturing execution system, mes integration, production order processing, material staging, production order release, component picking, production confirmation, goods receipt, serial numbers]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1Y5_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-785
topic: 12-production-and-manufacturing/mes-and-shop-floor-integration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Production Operations with Manufacturing Execution System (1Y5) (1Y5_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1Y5_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Manufacturing Execution System and Third-Party Shop Floor Integration** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Production Operations with Manufacturing Execution System (1Y5) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232850067)

[2 Prerequisites 4](#_Toc232850068)

[2.1 System Access 4](#_Toc232850069)

[2.2 Roles 4](#_Toc232850070)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232850071)

[2.4 Additional Manual Configuration 5](#_Toc232850072)

[2.5 Business Conditions 6](#_Toc232850073)

[3 Overview Table 7](#_Toc232850074)

[4 Test Procedures 8](#_Toc232850075)

[4.1 Production Order Processing for Final Assembly 8](#_Toc232850076)

[4.1.1 Material Staging for Final Assembly 8](#_Toc232850077)

[4.1.2 Release Production Order for Final Assembly 9](#_Toc232850078)

[4.1.3 Check Serial Numbers 11](#_Toc232850079)

[4.1.4 Process and Confirm Shop Floor in Manufacturing Execution System 12](#_Toc232850080)

[4.1.5 Pick Components for Final Assembly 12](#_Toc232850081)

[4.1.6 Confirm Production Operations for Final Assembly 14](#_Toc232850082)

[4.1.7 Review Production Order 14](#_Toc232850083)

[4.1.8 Final Confirmation of Production Operations for Final Assembly 16](#_Toc232850084)

[4.1.9 Post Goods Receipt for Final Assembly Production Order 16](#_Toc232850085)

[4.1.10 Preview Goods Receipt Slip and Label (Optional) 17](#_Toc232850086)

[5 Follow-Up Processes 19](#_Toc232850087)

[5.1 Succeeding Processes 19](#_Toc232850088)

## Purpose

Overview

This scope item covers the setup of the integration from SAP S/4HANA Cloud Public Edition to Manufacturing Execution Systems (MES).

An MES integrates business and manufacturing processes that help to run efficient, high quality production on the shop floor.

You can use this scope item as an example of how to integrate a local customer shop floor system directly into SAP S/4HANA Cloud Public Edition, giving manufacturing staff a clear overview of production operations and improving analytical capability for the management team. SAP S/4HANA Cloud Public Edition is the system of record for all master data. An MES or a shop floor system is the system of record for all work in progress (WIP) data.

This communication scenario provides end points (inbound and outbound), which are needed to integrate an on-premise third-party MES solution (Manufacturing Execution System) to production operation through ALE IDocs, BAPI, and OData calls.

|  |
| --- |
| Note For more information, please refer to the [Prerequisites](#unique_2) [page ] 4 section. |

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Note If this scope item also includes set-up instructions, all steps in the set-up instructions must be completed before beginning this test script. |

- OData and SOAP web services are offered to integrate SAP S/4HANA Cloud Public Edition with SAP S/4HANA Cloud Private Edition and cloud third-party solutions.
- For exceptional cases and based on individual customer requests, SAP admits usage of BAPIs and IDocs on a temporary basis to integrate your solution wherever the currently available OData and SOAP web services are not sufficient.
- This admittance is restricted to individual customers and to a well-defined set of BAPIs and IDocs, which have been technically enabled by SAP for this purpose. To get this approval, please follow the process described in SAP Note [2653671](https://me.sap.com/notes/2653671).
- These BAPIs and IDocs are available as is and will not be functionally extended. They will be maintained for a limited period of time. The maintenance of a BAPI/IDoc will end 12 months after the availability of an equivalent OData or SOAP web service.
- SAP will provide services according to the roadmap for OData and SOAP web services.
- These web services might not be a 1:1 replacement for the enabled BAPIs and IDocs. However, the new web services can be mapped to the old interfaces.
- In your SAP S/4HANA Cloud Private Edition environment, it’s mandatory to use the SAP Cloud Connector to call BAPIs in SAP S/4HANA Cloud Public Edition. It’s not technically possible to do mappings in SAP Cloud Platform Integration in order to call BAPIs in SAP S/4HANA Cloud Public Edition.

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
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data or the sample data provided with scenario BJ5 to go through the test.

For more information on creating master data objects, see the [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/d6e8df2a98ebf93d47c669477462f251)

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation | You 've completed the step described in the Standard Cost Calculation (BEG) test script. |
| BNZ - Create New Open MM Posting Period - MDS | You've completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |
| BJ5 - Make-to-Stock Production – Discrete Manufacturing | You've completed the steps up until and including the Material Staging for Final Assembly section of the Make-to-Stock Production – Discrete Manufacturing (BJ5) test script. |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Material Staging for Final Assembly](#unique_9) [page ] 8 | Production Operator - Discrete Manufacturing | Stage Materials for Production (MF60) | You've staged materials for production. |
| [Release Production Order for Final Assembly](#unique_10) [page ] 9 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | You've released the order and all its operations. |
| [Check Serial Numbers](#unique_11) [page ] 11 | Production Operator - Discrete Manufacturing | Display Production Order (CO03) | You've checked and noted down the serial numbers. |
| [Process and Confirm Shop Floor in Manufacturing Execution System](#unique_12) [page ] 12 | n/a | n/a | The shop floor item has been processed and confirmed in the Manufacturing Execution System. |
| [Pick Components for Final Assembly](#unique_13) [page ] 12 | Production Operator - Discrete Manufacturing | Pick Components for Production Orders (CO27) | You've picked the components for the final assembly. |
| [Confirm Production Operations for Final Assembly](#unique_14) [page ] 14 | n/a | n/a | The shop floor item has been processed and confirmed in the Manufacturing Execution System. |
| [Review Production Order](#unique_15) [page ] 14 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | You've checked the production order.. |
| [Final Confirmation of Production Operations for Final Assembly](#unique_16) [page ] 16 | n/a | n/a | The shop floor item has been processed and confirmed in the Manufacturing Execution System. |
| [Post Goods Receipt for Final Assembly Production Order](#unique_17) [page ] 16 | Warehouse Clerk | Post Goods Movement (MIGO) | You've posted the goods receipt for the production order. |
| [Preview Goods Receipt Slip and Label (Optional)](#unique_18) [page ] 17 | Warehouse Clerk | Material Documents Overview (F1077) | You've previewed the material documents. |

## Test Procedures

This section describes procedures for each process step that belongs to this scope item.

### Production Order Processing for Final Assembly

#### Material Staging for Final Assembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you stage materials for production. If there's sufficient stock available in the production storage location, no line items are generated.

Prerequisite

Stock must be available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Stage Materials for Production (MF60). | The Material Staging for Planned Orders screen is displayed. |  |
| 3 | Enter Details | Make the following entries and choose Execute.Staging Types: SLoc.Level Select the checkbox.Plant: 1010Selection Horizon for Remts: Date must be in the future - after scheduled start dateChoose the Production/Process Order tab.Production Order: <Production Order Number> | The Pull List: Storage Location Level screen is displayed. |  |
| 4 | Choose Replenishment Proposal | Select the required line items from the left-hand margin and choose Replenishment proposal from the top of the screen. |  |  |
| 5 | Choose Replenishment Elements | Review the staged quantity and choose Replenishment elements. |  |  |
| 6 | Enter Replenishment Storage Location | On the bottom half of the split screen, select the lines and enter the replenishment storage location (101C). You need to enter a batch number for some materials. Choose Batch Determination to decide the batch.For example: RM122 |  |  |
| 7 | Choose Stage | Choose Stage in the center of the screen. |  |  |
| 8 | Save | Choose Save. | Missing materials are transferred to the shop floor from the designated storage area. The shortage of raw material for final assembly production order is supplied with this step. |  |

#### Release Production Order for Final Assembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You carry out a release at order operation level to release the order and all its operations. The order and the operations receive the REL (released) status.

Prerequisite

The production order created by the MRP controller has been assigned a release date in accordance with the scheduling margin key.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). |  |  |
| 3 | Check Default Area of Responsibility (Supervisor) | To check the default area of responsibility (supervisor), choose your avatar (in the top left corner) and choose App Settings > Area of Responsibility > Production Supervisor .In the Area of Responsibility (Supervisor) dialog box, check that only the following entry is displayed:Plant 1 DE (1010)MTS DI - Valuated (YB1) |  |  |
| 4 | Select Production Order | Enter the following search condition as filter.Choose Adapt Filters to display more selection filter.Choose More filters under Material and Plant.Select the checkbox for Material and Plant and choose Go.Choose OK. The Material and Plant fields are then added to filter bar.Status: CreatedMaterial: FG126Plant: 1010Choose Go. |  |  |
| 5 | Execute Release | Review the staged quantity and choose Replenishment elements. | The order is released.Note If the Release Order dialog box pops up and says Non-Availability of Material, it means that you have not made sufficient stock for the components of FG126. You can choose Release Order in the dialog box to release the order forcedly. Or you can carry out the preliminary steps to do the intial material stock posting and complete the production order processing for semi-finished goods and come back to release this order again. |  |
| 6 | Edit Order | On the Manage Production Orders (F2336) screen, choose the icon (in the top right corner). |  |  |
| 7 | Execute Release | Choose More Functions > Release . Make sure that it says REL in the Status field. | A system message tells you that the release has been carried out. |  |
| 8 | Save Changes | Choose Save. | The order is released. |  |

#### Check Serial Numbers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Finished Good material is managed with serial numbers. The system generates a serial number for each finished good when the production order is released.

Prerequisite

The serial number profile is defined in the material master record and the production order is released.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Display Production Order (CO03). | The Prodcution Order Display: Initial Screen is displayed. |  |
| 3 | Enter the Number | Make the following entries and press Enter.Order: <Order Number> | The Prodcution Order Display: Header screen is displayed. |  |
| 4 | Choose More → Header → Serial Number | Choose More > Header > Serial Number. | The Display Serial Number dialog box is displayed. |  |
| 5 | Check the Serial Number | In the Display Serial Number dialog box, the serial numbers generated during production order releasing are listed. Make a note of the serial numbers. |  |  |
| 6 | Choose Back | Close the dialog box and choose Back. |  |  |

#### Process and Confirm Shop Floor in Manufacturing Execution System

The Outbound Delivery IDoc is received in the (third-party) Manufacturing Execution system. Some follow-up processes need to be done there:

- Pick Components for Final Assembly
- Process Shop Floor Item
- Confirm Shop Floor Item

The confirmation information is sent back automatically to SAP S/4HANA Cloud Public Edition.

#### Pick Components for Final Assembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The released production order is now ready for picking. Only those materials that are not in the service stock at the assembly aisle are to be picked. For picking, the production operator selects the specific picking list that can be called up directly with the production order number. The production operator has a series of further selection options to allow for optimal worklist selection.

Prerequisite

Make sure that there's sufficient material in stock. To check the stock, you can use the warehouse user and the Display Stock Overview (MMBE) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Pick Components for Production Orders (CO27). | The Picking List: Initial Screen is displayed. |  |
| 3 | Enter Relevant Search Criteria | Make the following entries and choose Execute.Profile: 000002Production Order: <Your Production Order number> | The Order Information System: Detail List of Components screen is displayed. |  |
| 4 | Picking | Select the relevant reservations and choose Picking. | A list of all the selected reservations is displayed. |  |
| 5 | Batch Determination | Some materials are management by batch, for example, RM122. Select relation line item and choose Batch Determination. | The Batch Determination MM: Select Batches screen is displayed. |  |
| 6 | Enter Detail | Make the following entries and choose Copy. Split quantity:Quantity. |  |  |
| 7 | Post | Choose Post to post the goods movements. | The goods movements have been posted. |  |

#### Confirm Production Operations for Final Assembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents the processing status of orders, operations, sub-operations, and individual capacities. It's an instrument for controlling orders.

The confirmations have to be done in the respective Manufacturing Execution system and will be distributed to SAP S/4HANA Cloud Public Edition.

|  |
| --- |
| Note In practice some operations produce scrap due to operational or component defects. If you want to simulate this process, refer to the Rework Processing – Work-in-Process (BJQ) scope item. |

Prerequisite

The production order for finished product has been released and distributed to a Manufacturing Execution system.

Procedure

Confirm the operations in the connected Manufacturing Execution system and make sure to distribute them to SAP S/4HANA Cloud Public Edition.

#### Review Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After releasing or confirming the finished goods orders, the production supervisor could display and check the order using the Manage Production Orders (F2336) app for the FG126 Finished Good MTS.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). |  |  |
| 3 | Select Production Order | On the Manage Production Orders (F2336) screen, enter the following search condition as filter.Choose Adapt Filters to display more selection filter. Choose More filters under Material and Plant. Select the checkbox for Material and Plant and choose Go. Then, choose OK. The Material and Plant fields are then added to the filter bar.Make the following entries:Material: FG126Plant: 1010Choose Go. | The selected order is displayed. |  |
| 4 | Check Detailed Operations Status | Check the detailed information for the selected production operations.Issue:Empty if there's no issue for production order.Delay or Missing Components / PRT issue or Quantity Deviation / Quality Issue information shows if there's a relevant issue.Components:Material, total quantity and Issued / open quantity information for order components is displayedOrder Schedule:Detailed operation information with relevant work center, confirmed quantity, start and end time is displayed.Work Center Schedule:The relevant order covering the same work center capacity (operation is partially confirmed) is displayed.Operations not Started:The relevant order that would cover the same work center capacity (operation is released) is displayed.Confirmation:Detailed confirmation information with Yield, Scrap, and Rework quantity is displayed if the confirmation has been executed.Inspection:Detailed inspection lots information is displayed if there's any. | The detailed operations status is displayed. |  |

#### Final Confirmation of Production Operations for Final Assembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the usual business practices, confirmations of all assembly activities of the production order are executed before posting the goods receipt. The backflush is carried out together with the confirmation steps.

Procedure

Confirm the last operation in the connected Manufacturing Execution system and make sure to distribute it to SAP S/4HANA Cloud Public Edition.

#### Post Goods Receipt for Final Assembly Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the goods receipt for the production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Enter Goods Receipt | On the Post Goods Movement (MIGO) screen, make the following entries:Goods Receipt First top-left frameOrder Second top-left frameOrder: <Production order number you noted down before>GR goods receipt: 101Document date: leave defaultPosting date: leave defaultChoose Open Head.data and select the Print via Output Control indicator and choose Individual Slip as Version for Printing GR/GI Slip. |  |  |
| 4 | Enter Quantity | On the Where tab, choose the storage.Location: Std. storage 1 171AIf the Scrap quantity is booked, on the Serial Numbers tab, select the exact serial numbers for the yield quantities. |  |  |
| 5 | Set Item OK and Post | Select the Item OK checkbox and choose Post. | A system message is displayed, confirming that the material document has been posted. |  |

#### Preview Goods Receipt Slip and Label (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you preview the material document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Documents Overview | Open Material Documents Overview (F1077). |  |  |
| 3 | Search for Goods Receipts Material Document | Make the following entries and choose Go.Plant: 1010Material Document: Material document number from the previous step | The relevant material document item is displayed. |  |
| 4 | Select Material Document for Goods Receipt | Select the row for which you'd like to see the material documents. | The Material Document screen is displayed. |  |
| 5 | Check Goods Issue Details | Check the General Information, Attachments, Item, Document Flow and Process Flow. | In the General Information section, you can see the Posting Date and Document Date. |  |
| 6 | Select the Material Document Item | In the Items section, select the row of the material document item that you want to preview. | The Material Document (Original) screen is displayed. |  |
| 7 | Preview the Material Document Goods Receipt Slip | In the Output Management section, choose the Display Document (Original) icon for the item of which the Output Type is GOODS_RECEIPT_PO_SLIP. | The Goods Receipt Slip is opened in PDF format. |  |
| 8 | Preview the Material Document Goods Receipt Label | In the Output Management section, choose the Display Document (Original) icon for the item of which the Output Type is GOODS_RECEIPT_LABEL. | The Goods Receipt Label is opened in PDF format. |  |
| 9 | Choose Home | Choose Home. | The SAP Fiori launchpad is displayed. |  |

## Follow-Up Processes

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes.

| Process | Business Condition |
| --- | --- |
| Period-End Closing – Plant (BEI) (Optional) | These are executed collectively as a part of month-end closing. For more information on the month-end closing procedure, see the Period-End Closing – Plant test script.Note The month-end closing can only be carried out once a month. |

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
- related-to :: [[12-production-and-manufacturing/test-script-third-party-shop-floor-execution-discrete-industry-3w4-980]]
- related-to :: [[12-production-and-manufacturing/test-script-third-party-shop-floor-execution-process-industry-3w3-979]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1Y5_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 31,736 chars in the whole document
