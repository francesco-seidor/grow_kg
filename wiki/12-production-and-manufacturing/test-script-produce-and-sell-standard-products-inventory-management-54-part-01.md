---
id: 12-production-and-manufacturing/test-script-produce-and-sell-standard-products-inventory-management-54-part-01
title: "Test Script: Produce and Sell Standard Products – Inventory Management (54U_AE), SAP S/4HANA Cloud Public Edition (54U_S4CLD2608_BPD_EN_AE) — part 1 of 2"
description: "S/4HANA Cloud Public Edition test script, scope item 54U_AE (UAE, plant 3310): make-to-stock production of a serial-numbered product, planning to payment."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/end-to-end-produce-and-sell]
aliases: []
keywords: [End-to-End Produce-and-Sell Scenarios, production planning, predictive mrp, material requirements planning, kanban, subcontracting, repetitive manufacturing, production order execution, quality inspection, capacity leveling]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/54U_S4CLD2608_BPD_EN_AE.docx#lines-1-3191"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1066
topic: 12-production-and-manufacturing/end-to-end-produce-and-sell
language: EN
part: 1/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Produce and Sell Standard Products – Inventory Management (54U_AE), SAP S/4HANA Cloud Public Edition (54U_S4CLD2608_BPD_EN_AE) — part 1 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/54U_S4CLD2608_BPD_EN_AE.docx`, part 1 of 2 (lines 1–3191 of the extracted text), extracted with `mammoth`. Grouped under **End-to-End Produce-and-Sell Scenarios** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Produce and Sell Standard Products – Inventory Management (54U_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 5](#_Toc232855760)

[2 Prerequisites 6](#_Toc232855761)

[2.1 System Access 6](#_Toc232855762)

[2.2 Roles 6](#_Toc232855763)

[2.3 Master Data, Organizational Data, and Other Data 9](#_Toc232855764)

[2.4 Business Conditions 15](#_Toc232855765)

[2.5 Preliminary Steps 16](#_Toc232855766)

[2.5.1 Create Purchasing Info Record - Components 16](#_Toc232855767)

[2.5.2 Create Purchasing Info Record - Subcontracting 18](#_Toc232855768)

[2.5.3 Initial Requirement Situation (Optional) 20](#_Toc232855769)

[2.5.4 Check Flexible Workflow for Purchase Order Approval 21](#_Toc232855770)

[2.5.5 Configure Flexible Workflow for Purchase Order 22](#_Toc232855771)

[2.5.6 Create Purchase Contract 23](#_Toc232855772)

[2.5.7 Generate Source List 25](#_Toc232855773)

[2.5.8 Create Scheduling Agreement w/o Release doc for Standard Procurement 26](#_Toc232855774)

[2.5.9 Generate Source List 28](#_Toc232855775)

[2.5.10 Create Initial Material Stock 29](#_Toc232855776)

[2.5.11 Create Product Cost Collectors 30](#_Toc232855777)

[2.5.12 Create Preliminary Cost for the Product Cost Collectors 31](#_Toc232855778)

[2.5.13 Create Queue for Kanban Card Printing 32](#_Toc232855779)

[2.5.14 Define MRP Area 33](#_Toc232855780)

[2.5.15 Assign MRP Area to Material 35](#_Toc232855781)

[2.5.16 Maintain Output Control for Kanban Summarized JIT Call 37](#_Toc232855782)

[2.5.17 Create Control Cycle for External Kanban Processing 38](#_Toc232855783)

[2.5.17.1 Control Cycle for Event-driven Kanban: External Processing with Purchase Order 38](#_Toc232855784)

[2.5.18 Control Cycle for Classic Kanban: In-House Production 39](#_Toc232855785)

[2.5.18.1 Control Cycle for In-House Production: Production Orders with MRP 39](#_Toc232855786)

[2.5.19 Control Cycle for Classic Kanban: Stock Transfer 40](#_Toc232855787)

[2.5.20 Check Available Capacity in Work Center 41](#_Toc232855788)

[2.5.21 Check Formulas in Work Center 42](#_Toc232855789)

[2.5.22 Check Routings 43](#_Toc232855790)

[2.5.23 Check Production Version 44](#_Toc232855791)

[3 Overview Table 46](#_Toc232855792)

[4 Test Procedure 53](#_Toc232855793)

[4.1 Anonymous Forecast and MRP 53](#_Toc232855794)

[4.1.1 Create Planned Independent Requirements 53](#_Toc232855795)

[4.1.2 Schedule pMRP Simulation Creation 54](#_Toc232855796)

[4.1.3 Process pMRP Simulations 56](#_Toc232855797)

[4.1.4 Check Planned Independent Requirements 59](#_Toc232855798)

[4.1.5 Material Requirements Planning at Plant Level 60](#_Toc232855799)

[4.1.6 Evaluate Stock/Requirements Situation 62](#_Toc232855800)

[4.2 Procurement of Raw Materials 64](#_Toc232855801)

[4.2.1 Convert Purchase Requisitions to Purchase Orders 64](#_Toc232855802)

[4.2.2 Display Purchase Order (Optional) 65](#_Toc232855803)

[4.2.3 Create Inbound Delivery 66](#_Toc232855804)

[4.2.4 Confirm Quantities for Putaway 67](#_Toc232855805)

[4.2.5 Post Goods Receipt for Inbound Delivery 68](#_Toc232855806)

[4.2.6 Display Material Stock Before Quality Inspection (optional) 69](#_Toc232855807)

[4.2.7 Quality Inspection 70](#_Toc232855808)

[4.2.7.1 Display Open Inspection Lots (optional) 70](#_Toc232855809)

[4.2.7.2 Record Inspection Results 71](#_Toc232855810)

[4.2.7.3 Make Usage Decision 74](#_Toc232855811)

[4.2.8 Display Material Stock after Quality Inspection (optional) 76](#_Toc232855812)

[4.2.9 Evaluate Stock/Requirements Situation (Optional) 77](#_Toc232855813)

[4.2.10 Display Procurement Overview (Optional) 78](#_Toc232855814)

[4.3 Raw Material Procurement based on Scheduling Agreement 79](#_Toc232855815)

[4.3.1 Display Delivery Schedule 79](#_Toc232855816)

[4.3.2 Print Scheduling Agreement (Optional) 80](#_Toc232855817)

[4.3.3 Post Goods Receipt 81](#_Toc232855818)

[4.3.4 Evaluate the Stock/Requirement Situation (Optional) 82](#_Toc232855819)

[4.3.5 Display Procurement Overview (Optional) 83](#_Toc232855820)

[4.4 Subcontracting with Serial Number Management 84](#_Toc232855821)

[4.4.1 Convert Purchase Requisition to Purchase Order 84](#_Toc232855822)

[4.4.2 Change Purchase Order 85](#_Toc232855823)

[4.4.3 Monitor Subcontracting Documents (Optional) 86](#_Toc232855824)

[4.4.4 Approve Purchase Orders (Optional) 87](#_Toc232855825)

[4.4.5 Create Outbound Delivery 88](#_Toc232855826)

[4.4.6 Pick and Post Goods Issue 89](#_Toc232855827)

[4.4.7 Receive Goods from Subcontracting PO 90](#_Toc232855828)

[4.5 Repetitive Production Execution for Semi-Finished Component 92](#_Toc232855829)

[4.5.1 Adjust Planning in Planning Table 92](#_Toc232855830)

[4.5.2 Check Range of Stock Coverage 93](#_Toc232855831)

[4.5.3 Create Inspection Lot for Production Version 95](#_Toc232855832)

[4.5.4 Material Staging 95](#_Toc232855833)

[4.5.5 Display Routing for Inspection Characteristics 97](#_Toc232855834)

[4.5.6 Display Open Inspection Lots(Optional) 98](#_Toc232855835)

[4.5.7 Record Inspection Results 99](#_Toc232855836)

[4.5.8 Make Usage Decision 101](#_Toc232855837)

[4.5.9 Confirm Repetitive Manufacturing Inclusive Backflush of Materials 102](#_Toc232855838)

[4.6 Kanban Discrete Production Execution for Semifinished component and Kanban Procurement SG014 104](#_Toc232855839)

[4.6.1 Event-driven Kanban: External Processing and PDF Print of Kanban Card 104](#_Toc232855840)

[4.6.1.1 Create Event-Driven Kanban 105](#_Toc232855841)

[4.6.1.2 Variant 1: Set Kanban to FULL 106](#_Toc232855842)

[4.6.1.3 Variant 2: Goods Receipt 107](#_Toc232855843)

[4.6.1.4 Print the Kanban Card 108](#_Toc232855844)

[4.6.2 Classic Kanban: In-House Production - Production Orders with MRP 109](#_Toc232855845)

[4.6.2.1 Set Available Kanban to EMPTY 109](#_Toc232855846)

[4.6.2.2 Production Capacity Leveling for Discrete Manufacturing 110](#_Toc232855847)

[4.6.2.2.1 Check Capacity Situation 110](#_Toc232855848)

[4.6.2.2.2 Apply Changes to Available Capacity 112](#_Toc232855849)

[4.6.2.2.3 Production Scheduling 114](#_Toc232855850)

[4.6.2.2.4 Review Work Center Schedules 116](#_Toc232855851)

[4.6.2.3 Pick Components for Production Order 118](#_Toc232855852)

[4.6.2.4 Confirm Production Operation 119](#_Toc232855853)

[4.7 Production Order Execution 121](#_Toc232855854)

[4.7.1 Convert Planned Order to Production Order 121](#_Toc232855855)

[4.7.2 Review Production Order (Optional) 122](#_Toc232855856)

[4.7.3 Material Staging for Production Order 124](#_Toc232855857)

[4.7.4 Set Available Kanban to EMPTY 125](#_Toc232855858)

[4.7.5 Set Available Kanban to FULL 127](#_Toc232855859)

[4.7.6 Release Production Order 128](#_Toc232855860)

[4.7.7 Check Serial Numbers 129](#_Toc232855861)

[4.7.8 Pick Components for Final Assembly 130](#_Toc232855862)

[4.7.9 Confirm Production Operations of Production Order 131](#_Toc232855863)

[4.7.10 Review Production Order 133](#_Toc232855864)

[4.7.11 Post Goods Receipt for Production Order 134](#_Toc232855865)

[4.7.12 Evaluate Stock/Requirements Situation (Optional) 135](#_Toc232855866)

[4.8 Customer Order Creation And Outbound Delivery creation 136](#_Toc232855867)

[4.8.1 Create Sales Order 136](#_Toc232855868)

[4.8.2 Create Delivery with Order Reference 138](#_Toc232855869)

[4.8.3 Maintain Serial Numbers 139](#_Toc232855870)

[4.8.4 Execute Picking 140](#_Toc232855871)

[4.9 Quality inspection in Outbound Delivery 141](#_Toc232855872)

[4.9.1 Display Quality Technician Overview (Optional) 141](#_Toc232855873)

[4.9.2 Display Open Inspection Lots (Optional) 142](#_Toc232855874)

[4.9.3 Record Inspection Results 143](#_Toc232855875)

[4.9.4 Display Quality Engineer Overview (Optional) 145](#_Toc232855876)

[4.9.5 Make Usage Decision 145](#_Toc232855877)

[4.10 Outbound Delivery Processing 147](#_Toc232855878)

[4.10.1 Material Accepted 147](#_Toc232855879)

[4.10.1.1 Post Goods Issue for Outbound Delivery 147](#_Toc232855880)

[4.10.1.2 Proof of Delivery (Optional) 148](#_Toc232855881)

[4.10.2 Material Rejected 149](#_Toc232855882)

[4.10.2.1 Post Unrestricted Stock to Blocked Stock 149](#_Toc232855883)

[4.10.2.2 Update Delivery 150](#_Toc232855884)

[4.10.3 Display Inspection Results History (Optional) 152](#_Toc232855885)

[4.11 Accounts Receivable 153](#_Toc232855886)

[4.11.1 Create Billing Document 153](#_Toc232855887)

[4.11.2 Post Incoming Payments 154](#_Toc232855888)

[4.12 Accounts Payable 156](#_Toc232855889)

[4.12.1 Create Supplier Invoice with PO/GR relation 156](#_Toc232855890)

[4.12.2 Post Outgoing Payment 158](#_Toc232855891)

[5 Appendix 161](#_Toc232855892)

[5.1 Succeeding Processes 161](#_Toc232855893)

## Purpose

Overview

This scope item enables production planning and execution for a serial-number-managed finished good in make-to-stock scenarios, as well as prompt reactions to incoming sales orders (sell from stock).

The process starts with the creation of a demand forecast for finished goods, represented by planned independent requirements (PIRs).

Predictive Material and Resource Planning (pMRP) enables you to create, schedule, and evaluate pMRP simulations with constraints that support you in making informed decisions for your production planning. You can take over the resulting simulated demand and release it to your operational data as planned independent requirements.

Based on PIRs, material requirements planning (MRP) creates a production plan for finished goods and explodes the entire bill of material (BOM). As a result, raw material demand is planned. Production planners can analyze and manually change the planned order-based production plan.

The process of capacity leveling (scheduling) enables production planners to assign orders and operations from the production plan to available timeslots of capacities, letting the planners schedule the best option for their manufacturing.

Raw material demand leads to component demands that trigger procurement scenarios (external procurement via purchase orders and inbound delivery as well as procurement based on scheduling agreements and Kanban). Upon goods receipt, the materials are quality inspected.

Subcontract Purchasing enables you to process Subcontract Purchase Orders, to create outbound deliveries for the components shipped to the subcontractor. With the supply of the finished material, the goods receipt is created. The consumption of the sent components is recorded upon the receipt of the value-added finished material.

The production process itself covers the conversion of planned orders into production orders, order release, material staging and picking, confirmation of order operations, and goods receipt posting.

Raw materials within production can be replenished by Kanban procurement. A semifinished good is produced via a repetitive manufacturing scenario integrated with in-process inspection and Kanban.

Order-based target and actual cost is created, ensuring fully integrated material and value streams. For an additional subassembly, repetitive manufacturing is executed.

The process continues with the creation of a sales order, performing the delivery with picking and quality inspection at goods issue, invoicing, ending with the clearing after incoming payment.

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
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Production Supervisor - Repetitive Manufacturing | SAP_BR_PRODN_SUPERVISOR_RPTV | Production Management - Repetitive Manufacturing | SAP_BR_PRODN_SUPERVISOR_RPTV |  |
| Production Operator - Repetitive Manufacturing | SAP_BR_PRODN_OPTR_RPTV | Production Execution - Repetitive Manufacturing | SAP_BR_PRODN_OPTR_RPTV |  |
| Production Planner - Lean Manufacturing | SAP_BR_PRODN_PLNR_LEAN_MFG | Production Planning - Lean Manufacturing | SAP_BR_PRODN_PLNR_LEAN_MFG |  |
| Production Operator - Lean Manufacturing | SAP_BR_PRODN_OPTR_LEAN_MFG | Production Execution - Lean Manufacturing | SAP_BR_PRODN_OPTR_LEAN_MFG |  |
| Production Engineer - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC | Production Engineering - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Quality Technician | SAP_BR_QUALITY_TECHNICIAN | Quality Inspection | SAP_BR_QUALITY_TECHNICIAN |  |
| Quality Engineer | SAP_BR_QUALITY_ENGINEER | Quality Engineering | SAP_BR_QUALITY_ENGINEER |  |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Cost Accountant - Production | SAP_BR_PRODN_ACCOUNTANT | Product Costing | SAP_BR_PRODN_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

Material Master Data:

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Material | FG011 | ELECTRIC FAN | Finished Product with Serial number.Relevant for planning. MRP Planned and Produced internally as per Make to Stock strategy.Not Batch Managed. Not Handling Unit Managed. Not split valuated. Not EWM Managed.Sold to customer. This product will undergo quality inspection just before delivery to customer. |
| Material | RM011 | ELECTRIC MOTOR | Externally Procured Material.MRP Planned and procured from external supplier.Not EWM managed. Applicable for Quality Management. Not Serial number managed. Not Batch Managed. Not Handling Unit Managed. |
| Material | RM012 | CASING | Externally Procured Material.Procurement with refernce to a purchase contract.MRP Planned and procured from external supplier.Not EWM managed. Not applicable for Quality Management. Not Serial number managed. Not Batch Managed. Not Handling Unit Managed. |
| Material | SG011 | CONTROL BOARD | Semifinished Material.MRP Planned and produced internally using repetitive manufacturing process.Only Inventory Managed (Not EWM managed). Applicable for Quality Management. Not Serial number managed. Not Batch Managed. Not Handling Unit Managed. |
| Material | RM013 | CAPACITOR | Procured from external supplier. MRP Planned. Lot for Lot planning.Only Inventory Managed (Not EWM managed). Not applicable for Quality Management. Not Serial number managed. Not Batch Managed. Not Handling Unit Managed. |
| Material | RM014 | RESISTOR | Procured from external supplier. MRP Planned. Lot for Lot planning.Only Inventory Managed (Not EWM managed). Not applicable for Quality Management. Not Serial number managed. Not Batch Managed. Not Handling Unit Managed. |
| Material | RM017 | FAN BASE | Externally Procured Material.Procurement with refernce to a Summarized JIT Call (MRP, Alerts).MRP Planned and procured from external supplier.Not EWM managed. Not applicable for Quality Management. Not Serial number managed. Not Batch Managed. Not Handling Unit Managed. |
| Material | RM018 | FAN STAND | Externally Procured Material.Procurement with refernce to a Purchase Order.MRP Planned and procured from external supplier.Not EWM managed. Not applicable for Quality Management. Not Serial number managed. Not Batch Managed. Not Handling Unit Managed. |
| Material | RM019 | ALUMINUM SHEET | Externally Procured Material.MRP Planned and procured from external supplier.Not EWM managed. Not applicable for Quality Management. Not Serial number managed. Not Batch Managed. Not Handling Unit Managed. |
| Material | SG013 | FAN BLADE | Semifinished Material.MRP Planned and produced internally using KANBAN repetitive manufacturing process.Only Inventory Managed (Not EWM managed). Not applicable for Quality Management. Not Serial number managed. Not Batch Managed. Not Handling Unit Managed. |
| Material | SG014 | FAN STAND ASSEMBLY | Semifinished Material.MRP Planned and produced internally using KANBAN discrete manufacturing process.Only Inventory Managed (Not EWM managed). Not applicable for Quality Management. Not Serial number managed. Not Batch Managed. Not Handling Unit Managed. |
| Material | SG022 | SENSOR MODULE | Semifinished Material.MRP Planned and procured externally via subcontracting process, serialized. Not Batch Managed. Not Handling Unit Managed. |
| Material | RM023 | TEMPERATURE SENSOR | Externally Procured Material.MRP Planned and procured from external supplier, in this test script posted as initial stock posting, serialized. |
| Material | RM024 | VIBRATION SENSOR | Externally Procured Material.MRP Planned and procured from external supplier, in this test script posted as initial stock posting, serialized. |
| Material | RM025 | SENSOR SOCKET | Externally Procured Material.MRP Planned and procured from external supplier, in this test script posted as initial stock posting. |
| Material | RM026 | TRANSMITTER | Externally Procured Material.MRP Planned and procured from external supplier, in this test script posted as initial stock posting. |

Organization Data:

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |
| Controlling Area | A000 | Controlling Area A000 |  |
| Cost center | 33101301 | Manufacturing 1 (AE) |  |

Bill of Material Structure

| Material | Level | Material Type | Unit | Characteristics of Material | Component Quantity | Component UOM |
| --- | --- | --- | --- | --- | --- | --- |
| FG011 | 0 | FERT | PC | Finished Good for MTS processing with Serial Number and Discrete Manufacturing |  |  |
| RM011 | 1 | ROH | PC | External procured. | 1 | PC |
| RM012 | 1 | ROH | PC | External procured. | 1 | PC |
| SG011 | 1 | HALB | PC | Internally Produced- Repetitive Manufacturing | 1 | PC |
| RM013 | 2 | ROH | PC | External procured. | 1 | PC |
| RM014 | 2 | ROH | PC | External procured. | 1 | PC |
| SG013 | 1 | HALB | PC | Internally Produced- KANBAN Repetitive Manufacturing | 1 | PC |
| RM019 | 2 | ROH | KG | External procured. | 1 | KG |
| SG014 | 1 | HALB | PC | Internally Produced- KANBAN Discrete Manufacturing | 1 | PC |
| RM017 | 2 | ROH | PC | External procured. | 1 | PC |
| RM018 | 2 | ROH | PC | External procured. | 1 | PC |
| SG022 | 1 | HALB | PC | External procured via subcontracting process. | 1 | PC |
| RM023 | 2 | ROH | PC | External procured. | 1 | PC |
| RM024 | 2 | ROH | PC | External procured. | 1 | PC |
| RM025 | 2 | ROH | PC | External procured. | 1 | PC |
| RM026 | 2 | ROH | PC | External procured. | 1 | PC |

Work center

| Work Center | Plant | Work Center Category | Work center Description |
| --- | --- | --- | --- |
| ASSEMBLY | 3310 | 0001 | Assembly |
| PACK01 | 3310 | 0001 | Packing Line 1 |
| TESTING | 3310 | 0001 | Testing |
| ASSPKG | 3310 | 0001 | CP-WC5, Assembly and Packaging |
| FINICLN | 3310 | 0001 | CP-WC4, Finishing and leaning |
| TURNING1 | 3310 | 0001 | CP-WC1, Turning 1 |
| TURNING2 | 3310 | 0001 | CP-WC2, Turning 2 |
| DRILING | 3310 | 0001 | CP-WC3, Drilling |

Routing:

Create a routing for the Finished & Semi-finished product FG011,SG011,SG013 ,SG014 mentioned in this document. Routing must be created in plant 3310.

| Product | Operation | Description | Work Center | Work Center (Alternative) |
| --- | --- | --- | --- | --- |
| FG011 | 0010 | Assembly | ASSEMBLY |  |
|  | 0020 (Critical Operation) | Final Acceptance | TESTING |  |
|  | 0030 | Packaging | PACK01 |  |
| SG011 | 0010 | Control Board Assembly | WINDING |  |
|  | 0020 | Final work and quality inspection | WORK |  |
| SG014 | 0010 | Turning Machine 1 | TURNING1 |  |
|  | 0020 (Critical Operation) | Turning Machine 2 | TURNING2 | TURNING9 |
|  | 0030 | Drilling machine | DRILING |  |
|  | 0040 | Finishing | FINICLN |  |
|  | 0050 | Clearing | FINICLN |  |
| SG013 | 0010 (Critical Operation) | Assembly | ASSPKG | ASSPKG9 |
|  | 0020 | Finish and clean | FINICLN |  |

Production Version:

Create production version for the finished & semi-finished product FG011 ,SG011, SG013, SG014 using the BOM and routing created in the above steps. Production Version must be created in plant 3310.

Suppliers:

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Supplier | 33300001 | Domestic Supplier 1 |  |
| Supplier | 33300002 | Domestic Supplier 2 |  |
| Supplier Subcontracting | 33300007 | Domestic AE Subcontractor A | Note If you want to send form print outs via e-mail instead of using the print functionality, make sure that you have maintained a valid e-mail address in the vendor master data. |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |

Customer:

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Sold-to Party | 33100001 | Domestic UAE Customer 1 |  |
| Ship-to Party | 33100001 | Domestic UAE Customer 1 |  |
| Payer | 33100001 | Domestic UAE Customer 1 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Shipping point | 3310 | Shipping Point 3310 |  |
| Company code | 3310 | Company Code 3310 |  |

Quality Master Inspection Characteristics:

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Master Inspection Characteristic | YQUALI01 | Surface |  |

Quality Inspection Plan:

Quality Inspection Plan uses the standard work center ‘QMLABS’ provided as part of standard best practices.

Quality inspection needs to be created in plant 3310.

For more information on creating your own master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BLD | Create Production Version - MDS |
| BNQ | Create Quality Inspection Plan - MDS |
| BNE | Create Supplier Master - MDS |
| BHD | Create Purchasing Info Record - MDS |
| BND | Create Customer Master - MDS |

### Business Conditions

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation | You have completed the step described in the Standard Cost Calculation (BEG) test script. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |
| J58 - Accounting and Financial Close | Execute to create open posting periods. |

### Preliminary Steps

#### Create Purchasing Info Record - Components

|  |
| --- |
| Note If the Info Records for the material combination of materials: RM011 and supplier: 33300001; RM013 and supplier: 33300001; material: RM012, RM018 and supplier: 33300002 already exist in the system, you can skip this step. |

Complete the following procedure to create records for all of your components.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Manage Purchasing Info Records (F1982) . | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create Purchasing Info Records. | The Purchasing Info Record Screen is displayed. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Organization: 3310Purchasing Info Record Category: StandardSupplier: 33300001Material: RM011Plant: 3310Purchasing Group: 002 | Header data is added. |  |
| 5 | Enter General Information | In the General Information section, make the following entries:Available From:TodayAvailable To:12/31/9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | In the Purchasing Data section, make the following entries:Incoterm: EXWIncoterm Location 1: VENDOR LOCATION | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: 2Under Delivery Tolerance in %: 0Over Delivery Tolerance in %: 0Tax Code: <Input Tax Code>Confirmation Control: Inbound DeliveryOrder Unit: PCStandard Order Quantity: 1Goods-Receipt-Based Invoice Verification: selectNo Evaluated Receipt Settlement: selectNote When the Time Dependent Tax (TDT) is activated via the Define Tax Codes for Sales and Purchases activity for Country of company code and Tax Code is given, the Tax Rate Valid From field is mandatory. You can enter current date, which will be adjusted to validity start date of tax code according to the setting in the activity.When the RITA (Registration for Indirect Taxation Abroad) is activated, tax registration country is maintained for company code in Activate RITA and Maintain Tax Registration Countries and tax code is given, the Tax Country field is mandatory, in which the country ID of company code is given as a default value, but you can change to the valid country ID that is maintained in the activity accordingly.Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or via the configuration activity in the Realize phase in the project experience of SAP Central Business Configuration.Time Dependent Tax (TDT) and RITA (Registration for Indirect Taxation Abroad) does not apply to Brazil. | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To: 12/31/9999Amount: 50Pricing Unit: 1Unit of Measure: PCCurrency: AEDChoose Apply. | Condition Data is added |  |
| 9 | Save your data | Choose Create. | The purchasing info record is saved. |  |

|  |
| --- |
| Note Repeat the above steps to create the info record for material RM013 and supplier 33300001.Repeat the above steps to create the info record for materials RM012, RM018 and supplier 33300002.While creating the info records for RM018 and RM012, amount in step 8 must be set as 10 AED per 1 PC.For materials RM013 and RM018, Confirmation Control should be left blank instead of 'Inbound Delivery'. |

|  |
| --- |
| Note For Embargo CheckIf you want to execute an Embargo Control please refer to Scope Item 1WC (Embargo Control). |

#### Create Purchasing Info Record - Subcontracting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record screen is displayed. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: SubcontractingPurchasing Organization: 3310Supplier: 33300007Material: SG022Plant: 3310Purchasing Group: 001 | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: TodayAvailable To: 12/31/9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: EXWIncoterm Location 1: VENDOR | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: 10Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10.0Tax Code: <Input Tax Code>Order Unit: PCStandard Order Quantity: 100Goods-Receipt-Based Invoice Verification: X | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To: 12/31/9999Amount: 0.59Pricing Unit: 1Currency: AEDChoose Apply. | Condition Data is added. |  |
| 9 | Enter Reference Data (optional) | You can enter reference data. | Reference data is added. |  |
| 10 | Save your data | Choose Create. | The purchasing info record is saved. |  |

Result

The subcontracting info record is created.

#### Initial Requirement Situation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The MRP run only creates purchase requisitions if the demand is bigger than the available quantity. You can check the requirement situation in the Stock/Requirement List. If necessary, you can reduce the quantity of unrestricted use by posting a goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to Fiori Launchpad as a Production Planner, |  |  |
| 2 | Open the Fiori App | Open Monitor Material Coverage - Net / Individual Segments (F2101A) . | The Monitor Material Coverage (Original) screen displays. |  |
| 3 | Select Material | Select the checkbox for material SG022 and choose the Manage Materials button (top right). | The Material screen and Material Details screen display. |  |
| 4 | Check stock | Select the corresponding material. | The detailed Stock/Requirements List for each material displays. |  |

#### Check Flexible Workflow for Purchase Order Approval

Purpose

In this procedure, you check the flexible workflow for purchase order approval.

When you use the flexible workflow to approve the purchase order, make sure Flexible Workflow for Purchase Order with NB document is activated, and Flexible Workflow for Purchase Order Approval is configured.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution: Realize Phase screen, search Activate Flexible Workflow for Purchase Orders, then choose Search.Select the line of the item and go to the next screen.On the Configure Your Solution - Purchase Order Processing screen, choose Configure on the line of configuration step with name Activate Flexible Workflow for Purchase Orders. | The Document Types Purchase order Change screen is displayed. |  |
| 5 | Check Flexible Workflow for PO Approval | Verify the following entries:Purchasing Doc. Type: NBScenario based workflow: <Selected> | The Scenario based workflow is active for Purchase Orders with Document Type: NB. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Active Flexible Workflow | Go to the Configuration app. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflow for Purchase Orders.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Document Types Purchase order Change screen displays. |  |
| 3 | Check Flexible Workflow for PO Approval | Verify the following entries:Purchasing Doc. Type: NBScenario based workflow: <Selected> | The Scenario based workflow is active for Purchase Orders with Document Type: NB. |  |

Result

The Scenario based workflow is active for Document Type: NB.

#### Configure Flexible Workflow for Purchase Order

Purpose

In this procedure, you configure your release conditions for Purchase Order Approval.

|  |
| --- |
| Note When you start to process this step, make sure that the flexible workflow for purchase document type NB has been activated in your system. |

|  |
| --- |
| Note For the Workflow Name and Steps Name, you can translate to other languages via app Workflow Content Translation, for example translate it from English to German. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Purchase Orders (F2872). | The Manage Workflows screen is displayed. |  |
| 3 | Create Manage Workflow | Choose Create and make the following entries:Name: Test Workflow for Purchase OrderSelect Start Conditions, and in the Start Conditions area, make the following entries:Purchasing group of purchase order is: SelectedPurchasing Group: 001Choose Add another condition and make the following entries:Total Net Amount of Purchase Order is greater than: SelectedAmount: For example, 500Currency: AEDIn Steps area, choose Create and make the following entries:Type: Release of Purchase OrderIn the RECIPIENTS area, make the following entries:Assignment By: UserUser: Select User from value help (with Employee ID PURCHASING_MANAGER)Choose OK.Step to be completed by: One of the recipientsChoose Create.Choose Save. | The workflow for Purchase Order is configured. |  |
| 4 | Activate Workflow Item | Select the Workflow Item just created and choose Activate. | The Workflow Item is activated. |  |

|  |
| --- |
| Note Please make sure default workflow Automatic Release of Purchase Order has been activated. |

#### Create Purchase Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a Reference Purchase contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Purchaser | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Purchase Contracts (F1600A) . | The Manage Purchase Contracts screen displays. |  |
| 3 | Enter Contract Header details | Choose Create and make the following entries:Contract Type: Choose MK Quantity ContractValid From: Start date of the contractValid To: End date of the contractPurchasing Org.: 3310Purchasing Group:002Supplier: 33300002Currency:AEDIn section Delivery and Payment Terms:Incoterm:EXWIncoterm Location1:Vendor Location |  |  |
| 4 | Enter Contract Item details | In the Items tab, choose Create and make the following entries:Material: RM012Plant:3310 .In section Quantity and Price:Net price: Enter a net price , 10 AED per PC.Target Quantity: For example, 5000. If RITA is enabled at company code level, Tax Country field is available for input in purchase contract item GR/IR facet during creation and updating.In the Supplier Confirmation Control tab, enter the following details:Confirmation Control:0004In section GR/IR Control:Select GR-Based invoice verificationTax Code: <Input Tax Code> (If not already populated)Choose Apply.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. | The Purchase Contract screen displays. |  |
| 5 | Save Purchase Contract | Choose Create and when the purchase contract number is displayed, write it down for further use. | A new Purchase Contract is created. Purchase Contract Number is displayed |  |

#### Generate Source List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you maintain the contract as the source.

Table 1: Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Open the Fiori launchpad with the Purchaser role. | The Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Manage Source Lists (F1859). | The Manage Source Lists screen is displayed. |  |
| 3. | Maintain the filter of the source list | On the screen Manage Source List, in the filter, make the following entries:Material: RM012.Plant: 3310.Then choose Go. | If the source list item was already maintained, it will be shown. |  |
| 4. | Check the source list | If there is one item that is valid in the current period, ignore the following steps. If there isn't a valid item, continue with the next steps. |  |  |
| 5. | Create source list | On the screen Manage Source List, choose Create. | The Source List screen is displayed. |  |
| 6. | Enter the detail data | Choose Generate. |  |  |
| 7. | Use the Generated source to choose determine source | On the screen Source List, make the following entries:Material For example: RM012Plant For example:3310Choose Generate.On the popup screen Generated Sources, make the following entries:Valid From: For example, TodayValid to: For example, Today +7 daysChoose Go.The valid source of supply are listed. Choose the check box of one contract, for example, select the contract that you created in chapter [Create Purchase Contract](#unique_12) [page ] 23.Then choose Add to Existing. |  |  |
| 8. | Save the source list | Choose Create.If there are any empty lines highlighted in red color, then these empty lines with red must be deleted by selecting them and clicking Delete. After all the empty lines are deleted, choose Create. | The source list is saved. |  |

#### Create Scheduling Agreement w/o Release doc for Standard Procurement

Purpose

This activity is used to create the scheduling agreement w/o release doc for the material/supplier combination, for example, material RM013 and supplier 33300001, if it has not been maintained yet. If the scheduling agreement is already present in the system you can skip this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad, as Purchaser. | SAP Fiori launchpad displays |  |
| 2 | Access App | Open Manage Purchase Scheduling Agreements (F2179). | The Manage Purchase Scheduling Agreements list page displays |  |
| 3 | Create Scheduling Agreement | Select Create to create a new scheduling agreement | The New Purchase Scheduling Agreement header view displays. |  |
| 4 | Enter Header Data | Create a new scheduling agreement with the following data:Supplier: 33300001Agreement type: LP (Scheduling Agreement)Validity Start: <today>Validity End: <MM/DD/YYYY>,for example,today + 720 daysPurchasing Organization: 3310Purchasing Group: 002In section Delivery and Payment:Target Value : 200000 AED |  |  |
| 5 | Add Items to Scheduling Agreement | From the New Purchase Scheduling Agreement view, choose the Items facets and select Create. | The Purchase Scheduling Agreement Item view displays. |  |
| 6 | Enter Item data | On the Items facets view, make the following entries:Plant: 3310Material: RM013Target Quantity: 10000Net Order Price: Defaulted from Info recordTax Code: <Input Tax Code> (Default Value from Info Record)Tax Date: Default TodayChoose Apply at the bottom of the view. |  |  |
| 7 | Save | Return to the New Purchase Scheduling Agreement header view and choose Create at the bottom of the view.Make a note of the schedule agreement number. | A schedule agreement is created. |  |

#### Generate Source List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you maintain the scheduling agreement as the source.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Open the Fiori launchpad with the Purchaser role. | The Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Manage Source Lists (F1859). | The Manage Source Lists screen is displayed. |  |
| 3. | Maintain the filter of the source list | In the filter, make the following entries:Material: RM013.Plant: 3310.Then choose Go. | If the source list item was already maintained, it will be shown. |  |
| 4. | Check the source list | If there is one item that is valid in the current period, ignore the following steps. If there isn't a valid item, continue with the next steps. |  |  |
| 5. | Create source list | Choose the Create button. | The Source List screen is displayed. |  |
| 6. | Enter the detail data | Enter data in the following fields:Material For example: RM013Plant For example:3310Choose Generate. |  |  |
| 7. | Use the Generated source to choose determine source | In the Generated Sources screen, enter data in the following fields:Valid From: For example, TodayValid to: For example, Today +99 daysChoose Go.Then choose the check box of one Purchase Scheduling Agreement, for example, select the Purchase Scheduling agreement that you created in step Create Scheduling Agreement w/o Release doc for Standard Procurement of this scenario.And choose Add to Existing.For the row which has the selected Purchase Scheduling Agreement, for the column Materials Planning, select the value Record relevant to MRP Sched. Lines generated automatically (2). |  |  |
| 8. | Save the source list | Choose Save.If there are any empty lines highlighted in red color, then these empty lines with red must be deleted by selecting them and clicking Delete.After all the empty lines are deleted, choose Create. | The source list is saved. |  |

#### Create Initial Material Stock

Purpose

In a real business scenario, initial material stock is usually purchased from external suppliers through standard purchasing or subcontracting processes. For only testing purpose, this process step shows you how to create and post the initial material stock to storage locations directly.

Prerequisite

Before creating initial material stocks, we recommend that you check stock level for RM014, RM017, SG013, RM023, RM024, RM025 and RM026. To do that, log onto the SAP Fiori launchpad as a Production Planner, and open Manage Material Coverage - New Version (F0251A) app. Remove some stock if there is already sufficient amount of stock in store. Otherwise, no planned orders can be generated later. You can either post initial stock directly to the storage locations, or refer to test scripts from Procurement of Direct Materials (J45) or Scheduling Agreements in Procurement (BMR) test scripts for purchasing processes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Choose Document Type | Make the following entries:Trans./Event: Goods ReceiptReference Document: Other | The Goods Receipt Other - XXXX screen displays. |  |
| 4 | Enter Data | In the Detail Data section, make the following entries and press Enter.On the Where tab:Movement Type: 561Plant: 3310Storage Location: 331COn the Quantity tab:Quantity:<100 PC>On the Material tab:Material: RM014Choose Next Item and select Item OK to add entries. |  |  |
| 5 | Enter the Goods Receipt Other Screen: Serial Number Tab | On the Goods Receipt Other screen: Serial Numbers tab, enter the serial number of your received material.Only relevant for material RM023 and RM024. |  |  |
| 6 | Check | Choose Check. | The document is ready to be posted. |  |
| 7 | Post | Choose Post. | Material document XXX is posted and materials are available in stock. |  |
| 8 | Repeat the steps for Initial Stock | Repeat Steps from 3 to 6 for Material: RM017 and SG013 with Storage Location:331B.Repeat Steps from 3 to 6 for Material: RM023, RM024, RM025 and RM026 with Storage Location:331A and Unit of Measure as PC. |  |  |

#### Create Product Cost Collectors

Purpose

This step can only be executed if product cost planning is activated.

|  |
| --- |
| Note The product cost collector might have already been created in connection with other scope items. To have a check if the related ones are already created, please use the App Maintain Product Cost Collectors (KKF6N) with the selection based on the given material/plant data. In case the product cost collector already exists, the selectable entry on the left panel will be displayed and this step can be skipped. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Product Cost Collectors - Production Versions - Collective (KKF6M). | The Create Multiple Product Cost Collector for Production Versions screen displays. |  |
| 3 | Enter Relevant Values | Make the following entries and choose Execute.Plant: 3310Order Type: YBMROnly Repetitive Mfg Mat.: <select>Caution Once the product cost collector is created, it can't be created again with the same data. |  |  |
| 4 | Select Production Versions | The Select Production Versions screen could display if there is more than one production version or more than one material. | The Select Production Versions screen may display if there is more than one production version or more than one material. |  |
| 5 | Save | Select the row for the production version of material SG011,SG013. Choose Save. | The message log displays. |  |
| 6 | Exit | Choose Exit. |  |  |

#### Create Preliminary Cost for the Product Cost Collectors

Purpose

In this topic, you create preliminary costs for the product cost collectors.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Preliminary Cost Estimate - Product Cost Collectors (MF30). | The Creation of Preliminary Cost Estimates For Product Cost Collectors screen displays. |  |
| 3 | Enter Relevant Values | Make the following entries and choose Execute.Costing Date : <Current Date>Plant: 3310 |  |  |

#### Create Queue for Kanban Card Printing

Purpose

A new printing queue for Kanban which would be assigned in the Kanban control cycle is created. Ask your system administrator to complete this step because the Administrator role is required to access the app.

A default printing queue has to be used if you don't create a specific Kanban printing queue, which would be difficult to find among other printings.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Print Queues (F1260). | The Maintain Print Queues (F1260) screen displays. |  |
| 3 | Create a New Queue | Choose New.On the New Print Queue screen, make the following entries:Queue: Kanban_PrintDescription: Printing for KanbanFormat: PDFCommunication user: <Choose an existing user>Retention: 1Choose Create. | The Queue has been created. |  |

#### Define MRP Area

Purpose

The purpose of this activity is to define an MRP area used in Kanban external processing, assigned with pre-defined Kanban Storage Location. This step can only be executed once, and if such MRP area already exists, skip this step.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | On the Configure Your Solution: Realize Phase screen, select the values as shown below:Application Area: ManufacturingSub Application Area: Material Requirements Planning | A search result list is displayed in the All Items area. |  |
| 5 | Find the Entry | In the All Items area, choose the following entry: Master Data. | The Configure Your Solution - Master Data screen displays. |  |
| 6 | Navigate to SSCUI 103068 | In the Configuration Steps section, navigate to step Define MRP Areas for Plant/Storage Locations. Choose Configure in the Actions column. | The Define MRP Areas for Plant/Storage Locations: Change screen displays. |  |
| 7 | Check if MRP Area Exists | Check if MRP area already exists with below parameter combination:MRP Area Type: 02 Storage LocationPlant: 3310Receiving Location: 331EIf the previous combination exists, you can use this MRP Area in subsequent procedure to assign it to material master, and ignore remaining steps in this procedure; if not, perform the following steps 8–10 for MRP definition. |  |  |
| 8 | New Entry | On the screen Define MRP Areas for Plant/Storage Locations: Change, choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 9 | Input Parameters | On the screen New Entries: Details of Added Entries, make the following entries:MRP Area: for example, KANBAN3310MRP Area Type: 02 Storage LocationMRP Area Text: <Description>Plant: 3310Press Enter, and make the following entry:Receiving Location: 331E |  |  |
| 10 | Save | Choose Save.Note If such MRP area already exists, you will get an error message indicating that the storage location is assigned to several MRP areas. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define MRP Areas for Plant/Storage Locations | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define MRP Areas for Plant/Storage Locations.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define MRP Areas for Plant/Storage Lo-cations: Change screen displays. |  |
| 3 | Check if MRP Area Exists | Check if MRP area already exists with below parameter combination:MRP Area Type: 02 Storage LocationPlant: 3310Receiving Location: 331EIf the previous combination exists, you can use this MRP Area in subsequent procedure to assign it to material master, and ignore remaining steps in this procedure; if not, perform the following steps 4–6 for MRP definition. |  |  |
| 4 | New Entry | On the screen Define MRP Areas for Plant/Storage Locations: Change, choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 5 | Input Parameters | On the screen New Entries: Details of Added Entries, make the following entries:MRP Area: for example, KANBAN3310MRP Area Type: 02 Storage LocationMRP Area Text: <Description>Plant: 3310Press Enter, and make the following entry:Receiving Location: 331E |  |  |
| 6 | Save | Choose Save.Note If such MRP area already exists, you will get an error message indicating that the storage location is assigned to several MRP areas. |  |  |

#### Assign MRP Area to Material

Purpose

The purpose of this activity is to assign an MRP area to material RM018.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Material (MM02). | The Change Material (Initial Screen) screen displays. |  |
| 3 | Enter Material | On the Change Material (Initial Screen) screen, make the following entry:Material: RM018Choose Select View(s). | The Select View(s) dialog displays. |  |
| 4 | Select Views | Select the MRP 1 view, and choose Org. Levels. | The Organizational Levels dialog displays. |  |
| 5 | Organizational Levels | In the popup dialog Organizational Levels, make the following entries:Plant: 3310Storage Location: <Leave it blank>Choose Continue. | The Change Material XXX screen displays. |  |
| 6 | Check if MRP Area exists | Navigate to the MRP 1 tab, and find section MRP Areas.If MRP Area Exists is selected (flagged), please skip the remaining steps; if not selected, go on with next steps to assign one MRP Area. |  |  |
| 7 | Input MRP Area | Choose button MRP Areas. In the popup table Overview: MRP Areas, you need to maintain one line to assign the MRP Area.For field MRP Area, open Value Help. Input below Restrictions and choose Go:MRP Area Type: 02 (Storage Location)Receiving Location: 331EThere should be only one search result, choose this MRP Area, and choose OK. |  |  |
| 8 | Input other parameters | Double-click the line you created and make the following entry on the MRP 1 tab:MRP Type: ND |  |  |
| 9 | Adopt | Choose Adopt twice, and make sure the MRP Area Exists is selected (flagged) now. | The MRP Area Exists is flagged now. |  |
| 10 | Save | On the Change Material screen, choose Save. | The MRP area is assigned to material RM018. |  |

#### Maintain Output Control for Kanban Summarized JIT Call

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Output Parameter Determination (W0138). |  |  |
| 3 | Choose Show Rules for | On the Show Rules for field, choose the triangle button and choose Summarized JIT Call from the dropdown list. |  |  |
| 4 | Choose the Determination Step and Maintain Table Contents | On the Determination Step Field, choose the triangle button.Choose Channel, and maintain the following entry in Table Contents.Entry 1 as below:Output type: SUMMARIZED_JIT_CALL (Summarized JIT Call)Role: LFChannel: PRINT (Printout)Exclusive Indicator: – (false)Choose Printer Settings, and maintain the following entry in Table Contents.Entry 1 as below:Output type: SUMMARIZED_JIT_CALL (Summarized JIT Call)Role: LFPrint Queue: <your queue>Number of Copies: 1Note To maintain Table Contents.Choose Edit on Output Parameter Determination.Choose Insert New Row if a new row has to be added.Choose the triangle button on the field to be maintained.Choose Direct Value Input on the dropdown list.Input the value.Choose Activate, on the popup screen choose yes to save.Choose Display. |  |  |

#### Create Control Cycle for External Kanban Processing

##### Control Cycle for Event-driven Kanban: External Processing with Purchase Order

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Kanban Control Cycles (PKMC). |  |  |
| 3 | Navigate to Create Control Cycle Screen | Make the following entries and choose Edit.Plant: 3310Choose Create Control Cycle. | The Create Control Cycle screen displays. |  |
| 4 | Enter the Selection Details | Make the following entries and choose Continue:Event-Driven Kanban: SelectedMaterial: RM018Supply Area: KANBAN_04Lifecycle status: Released | The Control Cycle Maintenance: Change screen displays. |  |
| 5 | Enter the Control Cycle Details | Make the following entry:Container Quantity: 100In the next part, choose the Replenishment Strategy tab. On this tab, select External Procurement and enter the value <PD01>, and then choose Enter.The tab changes its title from Replenishment strategy to External Procurement. Continue to enter the following entries:Purchasing Org: 3310Supplier: 33300002Choose another tab Print Control, and make the following entries under Print Kanban Card:Print Queue: KANBAN_PRINTForm Template: PP_KANBAN_CARD |  |  |
| 6 | Save | Choose Save Control Cycle | You created an external Kanban control cycle for material RM018. |  |

#### Control Cycle for Classic Kanban: In-House Production

##### Control Cycle for In-House Production: Production Orders with MRP

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Kanban Control Cycles (PKMC). |  |  |
| 3 | Navigate to Create Control Cycle Screen | Make the following entries and choose Edit.Plant: 3310Choose Create Control Cycle. | The Create Control Cycle screen displays. |  |
| 4 | Enter the Selection Details | Make the following entries and choose Continue:Classic Kanban: SelectedMaterial: SG014Supply Area: KANBAN_05Lifecycle status: Released | The Control Cycle Maintenance: Change screen displays. |  |
| 5 | Enter the Control Cycle Details | Number of Containers: 3Container Quantity: 100Maximum Empty Containers: 2Number of Load Carriers: 1Go to the next part and in the Replenishment Strategy section, select In-House Production, enter PD60 and choose Enter.Person Responsible: 001Production Version: 0001 |  |  |
| 6 | Save | Choose Save Control Cycle. | You have created an internal Kanban control cycle for material SG014. |  |

#### Control Cycle for Classic Kanban: Stock Transfer

Purpose

In this step, you create a control cycle for classic Kanban that can be used for direct stock transfer. In the control cycle, you define the demand source, the supply source and the procedure that must be used to replenish the Kanban material. You also define the number of Kanbans that circulate among the supply source and the demand source, as well as the quantity a Kanban contains.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Kanban Control Cycles (PKMC). |  |  |
| 3 | Navigate to Create Control Cycle Screen | Make the following entries and choose Edit.Plant: 3310Choose Create Control Cycle. | The Create Control Cycle screen displays. |  |
| 4 | Enter the Selection Details | Make the following entries and choose Continue:Classic KANBAN: SelectedMaterial: RM012Supply Area: KANBAN_03Lifecycle status: Released | The Control Cycle Maintenance: Change screen displays. |  |
| 5 | Enter the Control Cycle Details | Make the following entries:Number of Containers: 5Container quantity: 100Maximum Empty Containers: 2Number of Load Carriers: 1Go to the next part and in Replenishment Strategy tab, select Stock Transfer, enter PD03 and choose Enter.Storage Location: 331C |  |  |
| 6 | Save | Choose Save Control Cycle. | You have created a Kanban control cycle for material RM012. |  |

#### Check Available Capacity in Work Center

Purpose

In the Best Practice pre-delivered contents, standard available capacity is applied to the work centers, and no shifts are assigned initially. In case these values have been adjusted during test, we recommend that you have a check to have better understanding of current available capacity for work center TURNING1, TURNING2, DRILING, FINICLN and ASSPKG.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Work Center (CR02). | The Change Work Center: Initial Screen displays.You can also add this app to the main page if it’s not listed: Choose the user icon, and select App Finder. Click the plus icon of Change Work Center to add the tile. |  |
| 3 | Enter Plant and Work Center | On the Change Work Center (CR02) screen, make the following entries, and press Enter:Plant: 3310Work Center: <Work Center>, for example, TURNING1, TURNING2, DRILING, FINICLN and ASSPKG |  |  |
| 4 | Choose Capacity Category 001 | Choose the Capacities tab, and you can find there are two capacity categories defined: 001 and 002.Double-click Capacity category: 001 | The Change Work Center Capacity: Header screen displays. |  |
| 5 | Check Standard Available Capacity | On the Change Work Center Capacity: Header screen for capacity 001, check standard available capacity. The following values are pre-set in this test scenario:Start time: 07:00:00End time: 16:00:00Length of breaks: 01:00:00Capacity Utilization: 100No. Ind. Capacities: 1For test purpose, we recommend using the same values as above. |  |  |
| 6 | Check Intervals and Shifts | Choose Intervals and Shifts in the upper left corner.On the Change Work Center Capacity: Intervals of Available Capacity screen for capacity 001, available shifts are listed in the table at the bottom of the page. We recommend deleting any additional shifts effective within next 6 weeks.Choose any line you want to delete, and then choose Delete in the upper right corner.Choose Back twice to screen Change Work Center: Capacity Overview. |  |  |
| 7 | Choose Capacity Category 002 | Under the Capacities tab, double-click Capacity category: 002. | The Change Work Center Capacity: Header screen displays. |  |
| 8 | Check Default Settings for Capacity Category 002 | Repeat step #5 and #6 for category 002. |  |  |
| 9 | Save | Choose Save. | Work center XXX in plant 3310 was changed. |  |

#### Check Formulas in Work Center

Purpose

This process step shows you how to check and set the formulas used in work centers for critical operation. Formula under the Capacities tab is used to calculate the capacity requirements of the operation segments, while formula under the Scheduling tab is used to calculate execution time of the operation. You need to check and set formulas for following work centers: TURNING2, TURNING9, ASSPKG and ASSPKG9.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Work Center (CR02). |  |  |
| 3 | Enter Plant and Work Center | On the Change Work Center: Initial Screen, make the following entries and press Enter:Plant: 3310Work Center: <Work Center> |  |  |
| 4 | Check Formulas under Capacities Tab | Choose Capacities tab, check formulas under Capacity category section: 001. For test purpose, we recommend using the same values as below:Setup Formula: SAP005Processing Formula: SAP006 |  |  |
| 5 | Check Formulas under Scheduling Tab | Choose Scheduling tab, check following settings. For test purpose, we recommend using the same values as below:Scheduling basis section:Capacity category: 001Execution time section:Duration of Setup: SAP001Processing Duration: SAP002 |  |  |
| 6 | Exit | Choose Save or Cancel |  |  |

#### Check Routings

Purpose

If you want to use SAP pre-delivered demo data to run through this scenario, you need to check Routing settings in your system. We recommend it to be consistent with what we described in section Routing under chapter Master Data for Discrete Manufacturing. If it is not consistent, you need to manually change it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Routing (CA02). |  |  |
| 3 | Select Semi-finished Goods | On the Change Routing: Initial Screen screen, enter the following data and choose Continue:Plant: 3310Material: SG013 |  |  |
| 4 | Check Routings for Semi-finished Goods | In the list under Header Overview, check listed routing versions. You can tick each line, choose Operation to see detailed operations for each Routing version. For pre-delivered demo data, we deliver two routing versions with respective operations.GrC: 1Operation 0010 - Work Center: ASSPKGOperation 0020 - Work Center: FINICLNGrC: 2Operation 0010 - Work Center: ASSPKG9Operation 0020 - Work Center: FINICLNIf the work center in respective operation in your system is not identical with above, you need to manually change it. |  |  |
| 5 | Select Semi-finished Goods | Go back to the selection page, enter the following data and press Enter:Plant: 3310Material: SG014 |  |  |
| 6 | Check Routings for Semi-finished Goods | Check listed Routing versions for semi-finished goods as the same way in step 4. For detailed Operation information, please check chapter Master Data for Discrete Manufacturing. |  |  |

#### Check Production Version

Purpose

Production Versions are used as source of supply during production scheduling. This process step shows you how to check the alternative work centers which are assigned to the critical operation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Versions - C223 (C223). | The Production Version: Mass Processing screen displays. |  |
| 3 | Select Semi-finished Goods | In the Selection Conditions area, enter the following data and press Enter:Plant: 3310Material: SG014 |  |  |
| 4 | Check Production Version for Semi-finished Goods | Check listed production versions. For pre-delivered demo data, we deliver two production versions with respective production line assignment.Production Version: 0001Production Line: TURNING2Production Version: 0002Production Line: TURNING9 |  |  |
| 5 | Select Semi-finished Goods | In the Selection Conditions area, enter the following data and press Enter:Plant: 3310Material: SG013 |  |  |
| 6 | Check Production Version for Semi-finished Goods | Check listed production versions. For pre-delivered demo data, we deliver two production versions with respective production line assignment.Production Version: 0001Production Line: ASSPKGProduction Version: 0002Production Line: ASSPKG9 |  |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Anonymous Forecast and MRP |  |  |  |
| [Create Planned Independent Requirements](#unique_31) [page ] 53 | Production Planner | Maintain PIRs (F3445) | Independent Requirements for Finished Goods are created. |
| [Schedule pMRP Simulation Creation](#unique_32) | Production Planner | Schedule pMRP Simulation Creation (F3968) | Application job is finished with no error |
| [Process pMRP Simulations](#unique_33) | Production Planner | Process pMRP Simulations (F3934) | The capacity issues are reduced. |
| [Check Planned Independent Requirements](#unique_34) | Production Planner | Maintain PIRs (F3445) | The PIRs for top level materials are updated into requirement plan version 00. |
| [Material Requirements Planning at Plant Level](#unique_35) [page ] 60 | Production Planner | Schedule MRP Runs (F1339) | MRP run executed for Finished Goods and its component materials at Plant level. |
| [Evaluate Stock/Requirements Situation](#unique_36) [page ] 62 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Stock/Requirements situations for the planned materials are analyzed. |
| Procurement of Raw Materials |  |  |  |
| [Convert Purchase Requisitions to Purchase Orders](#unique_37) [page ] 64 | Purchaser | Process Purchase Requisitions (F1048A) | Source of supply is assigned to Purchase Requisition. Purchase Requisition converted to Purchase Order. |
| [Display Purchase Order (Optional)](#unique_38) [page ] 65 | Purchaser | Manage Purchase Orders (F0842A) | The Manage Purchase Orders screen is displayed with a list of existing Purchasing Document Items. Check the status of the Purchase Order. |
| [Create Inbound Delivery](#unique_39) [page ] 66 | Receiving Specialist | Inbound Deliveries for Purchase Orders (VL34) | Inbound delivery created with reference to purchase order. |
| [Confirm Quantities for Putaway](#unique_40) [page ] 67 | Receiving Specialist | Inbound Deliveries for Putaway (VL06IP) | Putaway performed for inbound delivery document. |
| [Post Goods Receipt for Inbound Delivery](#unique_41) [page ] 68 | Receiving Specialist | Post Goods Receipt for Inbound Delivery (F2502) | Goods receipt is posted. |
| [Display Material Stock Before Quality Inspection (optional)](#unique_42) [page ] 69 | Warehouse Clerk | Stock - Single Material (F1076) | Quantity received is posted in Quality Stock. |
| Quality Inspection |  |  |  |
| [Display Open Inspection Lots (optional)](#unique_43) [page ] 70 | Quality Technician | Manage Inspection Lots (F2343) | Inspection Lot is displayed. |
| [Record Inspection Results](#unique_44) [page ] 71 | Quality Technician | Record Inspection Results (F1685A) | Inspection Results are recorded |
| [Make Usage Decision](#unique_45) [page ] 74 | Quality Engineer | Manage Usage Decisions (F2345) | Usage Decision is made. |
| [Display Material Stock after Quality Inspection (optional)](#unique_46) [page ] 76 | Warehouse Clerk | Stock - Single Material (F1076) | Stock quantities are updated based on Quality Inspection. |
| [Evaluate Stock/Requirements Situation (Optional)](#unique_47) [page ] 77 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Stock/Requirements situation for the planned materials is analyzed. |
| [Display Procurement Overview (Optional)](#unique_48) [page ] 78 | Purchaser | Procurement Overview (F1990) | Cards for various procurement documents are displayed. |
| Raw Material Procurement based on Purchase Scheduling Agreement |  |  |  |
| [Display Delivery Schedule](#unique_49) [page ] 79 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | A Delivery Schedule of purchase scheduling agreement is displayed. |
| [Print Scheduling Agreement (Optional)](#unique_50) [page ] 80 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | The Scheduling Agreement is printed. |
| [Post Goods Receipt](#unique_51) [page ] 81 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Goods receipt is posted against the scheduling agreement. |
| [Evaluate the Stock/Requirement Situation (Optional)](#unique_52) [page ] 82 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | The stock/requirement situation is displayed. |
| [Display Procurement Overview (Optional)](#unique_53) [page ] 83 | Purchaser | Procurement Overview (F1990). | Cards for various procurement documents are displayed. |
| Subcontracting with Serial Number Management |  |  |  |
| [Convert Purchase Requisition to Purchase Order](#unique_54) | Purchaser | Process Purchase Requisitions (F1048A) | Purchase order is created. |
| [Change Purchase Order](#unique_55) | Purchaser | Change Purchase Order - Advanced (ME22N) | PO is updated. |
| [Monitor Subcontracting Documents (Optional)](#unique_56) | Purchaser | Monitor Subcontracting Documents (F3095) |  |
| [Approve Purchase Orders (Optional)](#unique_57) | Purchasing Manager | My Inbox - All Items (F0862) | Purchase orders are approved. |
| [Create Outbound Delivery](#unique_58) | Purchaser | Display Subcontracting Stocks by Supplier (ME2ON) | Outbound Delivery created. |
| [Pick and Post Goods Issue](#unique_59) | Shipping Specialist | Change Outbound Delivery (VL02N) |  |
| [Receive Goods from Subcontracting PO](#unique_60) | Warehouse Clerk | Post Goods Movement (MIGO) | Material document and journal entry showing receipt of purchased material and consumption of components. |
| Repetitive Production Execution for Semifinished Component |  |  |  |
| [Adjust Planning in Planning Table](#unique_61) [page ] 92 | Production Supervisor - Repetitive Manufacturing | Manage Repetitive Manufacturing (MF50) | The Planning Table Initial Screen: Change Mode displays. |
| [Check Range of Stock Coverage](#unique_62) [page ] 93 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | The Monitor Material Coverage screen displays. |
| [Create Inspection Lot for Production Version](#unique_63) [page ] 95 | Quality Technician | Process Inspection Lots for Production Versions (MFPR) | Inspection Lot for the Production version is created. |
| [Material Staging](#unique_64) [page ] 95 | Production Operator - Repetitive Manufacturing | Stage Materials for Production (MF60) | The Material Staging for Planned Orders screen displays. |
| [Display Routing for Inspection Characteristics](#unique_65) [page ] 97 | Production Engineer - Discrete Manufacturing | Display Routing (CA03) | The Display Routing: Initial Screen screen displays. |
| [Display Open Inspection Lots(Optional)](#unique_66) [page ] 98 | Quality Technician | Manage Inspection Lots (F2343) | Inspection Lot is displayed. |
| [Record Inspection Results](#unique_67) [page ] 99 | Quality Technician | Record Inspection Results (F1685A) | Inspection Results are recorded. |
| [Make Usage Decision](#unique_68) [page ] 101 | Quality Engineer | Manage Usage Decisions (F2345) | Usage Decision is made. |
| [Confirm Repetitive Manufacturing Inclusive Backflush of Materials](#unique_69) [page ] 102 | Production Operator - Repetitive Manufacturing. | Confirm Repetitive Manufacturing (MFBF). | The REM Confirmation - Transaction Variant: None screen displays. |
| Kanban Discrete Production Execution for Semifinished component and Kanban Procurement SG014 |  |  |  |
| Event-driven Kanban: External Processing and PDF Print of Kanban Card |  |  |  |
| [Create Event-Driven Kanban](#unique_70) [page ] 105 | Production Operator - Lean Manufacturing | Display Kanbans: Demand View (PK13N) | Purchase Order generated for Kanban based procurement. |
| [Variant 1: Set Kanban to FULL](#unique_71) [page ] 106 | Production Operator - Lean Manufacturing | Set Kanban Container Status (F3717) | Kanban Status set to Full and goods receipt for purchase order posted. |
| [Variant 2: Goods Receipt](#unique_72) [page ] 107 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Goods receipt for purchase order posted. |
| [Print the Kanban Card](#unique_73) [page ] 108 | Production Operator - Lean Manufacturing | Collective Kanban Print (PK17) | Kanban Card Printed. |
| Classic Kanban: In-House Production - Production Orders with MRP |  |  |  |
| [Set Available Kanban to EMPTY](#unique_74) [page ] 109 | Production Operator - Lean Manufacturing | Set Kanban Container Status (F3717) | Production order is generated and automatically released. |
| Production Capacity Leveling for Discrete Manufacturing |  |  |  |
| [Check Capacity Situation](#unique_75) [page ] 110 | Production Planner | Manage Work Center Capacity (F3289) | capacities for overload on bottleneck resources are checked. |
| [Apply Changes to Available Capacity](#unique_76) [page ] 112 | Production Planner | Manage Work Center Capacity (F3289) | The bottlenecks for all resources are resolved. |
| [Production Scheduling](#unique_77) [page ] 114 | Production Planner | Capacity Scheduling Table (F3770) | Schedules are realigned. |
| [Review Work Center Schedules](#unique_78) [page ] 116 | Production Planner | Capacity Scheduling Board (F3951) | Schedule status by the visualization of the Gantt chart is displayed. |
| [Pick Components for Production Order](#unique_79) [page ] 118 | Production Operator - Discrete Manufacturing | Pick Components for Production Orders (CO27) | Goods movements are posted for components. |
| [Confirm Production Operation](#unique_80) [page ] 119 | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | Confirm all operations of production order. Goods Receipt Posting also done at the confirmation of last operation. Kanban set to full. |
| Production Order Execution |  |  |  |
| [Convert Planned Order to Production Order](#unique_81) [page ] 121 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Planned Orders for Finished Goods are converted to Production Orders. |
| [Review Production Order (Optional)](#unique_82) [page ] 122 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | Validate the availability of components used in production order. |
| [Material Staging for Production Order](#unique_83) [page ] 124 | Production Operator - Discrete Manufacturing | Stage Materials for Production (MF60) | The components needed for the production order are moved from various storage locations to the production storage location, if needed. |
| [Set Available Kanban to EMPTY](#unique_84) [page ] 125 | Production Operator - Lean Manufacturing | Set Kanban Container Status (F3717) | Kanban status set to Empty. |
| [Set Available Kanban to FULL](#unique_85) [page ] 127 | Production Operator - Lean Manufacturing | Set Kanban Container Status (F3717) | Kanban status set to Full. |
| [Release Production Order](#unique_86) [page ] 128 | Production Operator - Discrete Manufacturing | Manage Production Orders (F2336) | Production order for Finished Goods is released. |
| [Check Serial Numbers](#unique_87) [page ] 129 | Production Operator - Discrete Manufacturing | Display Production Order (CO03) | Serial numbers generated for Finished goods are displayed in production order. |
| [Pick Components for Final Assembly](#unique_88) [page ] 130 | Production Operator - Discrete Manufacturing | Pick Components for Production Orders (CO27) | Goods movements are posted for components. |
| [Confirm Production Operations of Production Order](#unique_89) [page ] 131 | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | Confirm all operations of production order. |
| [Review Production Order](#unique_90) [page ] 133 | Production Operator - Discrete Manufacturing | Manage Production Operations (F2335) | Check the status of production order. |
| [Post Goods Receipt for Production Order](#unique_91) [page ] 134 | Warehouse Clerk | Post Goods Movement (MIGO) | The goods receipt for the production order is posted. |
| [Evaluate Stock/Requirements Situation (Optional)](#unique_92) [page ] 135 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Stock/Requirements situations for the planned materials are analyzed. |
| Customer Order Creation and Outbound Delivery Creation |  |  |  |
| [Create Sales Order](#unique_93) [page ] 136 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales order is created. |
| [Create Delivery with Order Reference](#unique_94) [page ] 138 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Outbound delivery is created for sales order. |
| [Maintain Serial Numbers](#unique_95) [page ] 139 | Shipping Specialist | Manage Outbound Deliveries (F0867A) | Serial numbers assigned to the delivery item. |
| [Execute Picking](#unique_96) [page ] 140 | Shipping Specialist | Manage Outbound Deliveries (F0867A) | Outbound delivery is picked. |
| Quality inspection in Outbound Delivery |  |  |  |
| [Display Quality Technician Overview (Optional)](#unique_97) [page ] 141 | Quality Technician | Quality Technician Overview (F2361) | Cards for various Quality Objects are displayed. |
| [Display Open Inspection Lots (Optional)](#unique_98) [page ] 142 | Quality Technician | Display Inspection Lots without Usage Decision(QVM3) | Inspection lot is displayed. |
| [Record Inspection Results](#unique_99) [page ] 143 | Quality Technician | Record Inspection Results (F1685A) | Inspection results are recorded. |
| [Display Quality Engineer Overview (Optional)](#unique_100) [page ] 145 | Quality Engineer | Quality Engineer Overview (F2360) | Cards for various Quality Objects are displayed. |
| [Make Usage Decision](#unique_101) [page ] 145 | Quality Engineer | Manage Usage Decisions (F2345) | Usage decision captured on inspection lot. |
| Outbound Delivery Processing |  |  |  |
| Material Accepted[Post Goods Issue for Outbound Delivery](#unique_102) [page ] 147 | Shipping Specialist | Manage Outbound Deliveries (F0867A) | Goods issues for delivery are posted. |
| [Proof of Delivery (Optional)](#unique_103) [page ] 148 | Shipping Specialist | Automatic Confirmation - Proof of Delivery (VLPODQ) | Generate proof of delivery. |
| Material Rejected[Post Unrestricted Stock to Blocked Stock](#unique_104) [page ] 149 | Warehouse Clerk | Post Goods Movement (MIGO) | Rejected goods moved to Blocked Stock. |
| [Update Delivery](#unique_105) [page ] 150 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Delivery is updated. |
| [Display Inspection Results History (Optional)](#unique_106) [page ] 152 | Quality Engineer | Display Results History (F2428) | History of Inspection results is displayed. |
| Accounts Receivable |  |  |  |
| [Create Billing Document](#unique_107) [page ] 153 | Billing Clerk | Create Billing Documents (F0798) | Billing document is created for the delivery. |
| [Post Incoming Payments](#unique_108) [page ] 154 | Accounts Receivable Accountant | Post Incoming Payments (F1345). | Incoming Payment is posted. |
| Accounts Payable |  |  |  |
| [Create Supplier Invoice with PO/GR relation](#unique_109) [page ] 156 | Accounts Payable Accountant | Create Supplier Invoice (F0859). | Supplier invoice created in the system. |
| [Post Outgoing Payment](#unique_110) [page ] 158 | Accounts Payable Accountant | Post Outgoing Payments (F1612). | Outgoing Payment is posted. |

## Test Procedure

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
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries and choose Go:Plant: 3310Period Indicator: Weekly(W)Version Active: Select all optionsMaterial: FG011 | The searched material item displays. |  |
| 5 | Edit PIRs | Select the material item and choose Edit in the upper right corner of the screen.On the Edit PIRs screen, enter quantities per week, for example:Week 1 (current week + 4 weeks): 100 PCWeek 2 (current week + 5 weeks): 100 PCWeek 3 (current week + 6 weeks): 75 PCWeek 4 (current week + 7 weeks): 100 PCWeek 5 (current week + 8 weeks): 75 PCWeek 6 (current week + 9 weeks): 100 PCWeek 7 (current week + 10 weeks): 100 PCWeek 8 (current week + 11 weeks): 75 PCVersion is Active: YES |  |  |
| 6 | Save PIRs Draft | Choose Save in the bottom right corner of the screen. | The PIRs are saved. |  |

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
| 6 | Enter Selection Criteria | Choose Step 3.In the Parameter Section area, make the following entries:ID for Reference Data: 54U_PMRP_<MMDD>Bucket Category: WStart Date of Reference: <Today’s date + 1 day>End Date of Reference: <Today’s date + 16 weeks>Simulation ID: 54U_PMRP_SIMU_<MMDD>Simulation Description: 54U_PMRP_SIMU_<MMDD>For the Object Selection sub-area:Plant: 3310Material: FG011MRP Controller: 001For the Document Data sub-area:Opening Stock: <blank> | MMDD is today’s date, for example, if the date is August 1st, then MMDD = 0801. |  |
| 8 | Schedule a New Job | Choose Check.If there are no error messages, choose Schedule.A new job is created and displayed in the Application Jobs table. | Confirm that the application job finishes with no errors. |  |

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
| 3 | Filter the Simulation | On the Process pMRP Simulations screen, filter the simulation with the reference ID you just created and choose Go.Reference Data : 54U_PMRP_<MMDD> | The simulation displays. |  |
| 4 | Copy the Simulation | Select the checkbox of the filtered simulation, and choose Copy in the upper right corner.On the Copy screen, make the following entries and choose Copy.Copy from Current Simulation: XNew Simulation ID: 54U_PMRP_SIMU_<MMDD>_CNew Simulation Description: 54U_PMRP_SIMU_<MMDD>_COPYOverload Tolerance: 2% | The system shows Simulation Copied.You can repeat this step to create several copies of one pMRP Simulation to figure out the best adjusted simulation. |  |
| 5 | Check the Copied Simulation | On the Process pMRP Simulations screen, choose the row of the new copied simulation with simulation ID: 54U_PMRP_SIMU_<MMDD>_C | The Demand Plan Simulation screen displays. |  |
| 6 | Check the Demand-Plan Simulation | On the Demand Plan Simulation screen, you can check the Capacity Issues, Delivery Performance, and Violated Constraints.You can check the demand plan simulation quantities for materials in each period, you can switch the displayed mode, for example:Simulation Table Selection: Reference /Simulation | In our scenario, we would only focus to reduce the capacity issue from top-level material FG011.If there is no capacity issue or violated constraints, skip step 7-15. |  |
| 7 | Check Issue Worklist | At the top of screen, choose the Capacity Issues quantity, the Capacity Issues page displays.Choose Show in Issue Work List, the Issue List screen displays.In the Issues area, you could see Issue Category, Affected Objects, Affected Weeks, Affected Demands, Impact Score, Impact Caused By and Impact Cause.You could choose Clear Filter icon after Filtered by: Capacity Issues, then you could get the overall issue lists, including Violated Constraints if applicable.Choose one Capacity Overload issue, choose Disregard Capacity Issues. On the pop-up Disregard Capacity Issues screen, choose OK.Choose Demand Plan Simulation on the top of screen and navigate back. | The selected issues are disregarded in this simulation.And the capacity issue quantities are reduced. |  |
| 8 | Check Capacity Plan Simulation | On the Demand Plan Simulation screen, choose the <75> (simulation quantity) in the red box for FG011, the Inspector area displays the relevant capacity overload issues.In the Issues area, choose Capacity Plan Simulation.On the Capacity Plan Simulation screen, you can check the Demand/Remaining Capcity in Hours in table view by default.Choose Show Work Center Overview near the top right corner of Capacity Plan Simulation screen, then it shows in graphic view.Check the overload demand in red for work center whose remaining capacity is less than zero, it indicates the capacity issue. | Continue to reduce the capacity issues or violated constraints in step 9-16. |  |
| 9 | Shift Demand | Choose the first demand in red for the work center, for example, TURNING2.In the Top-Level Materials area, navigate to FG011 for the latest week, and choose Shift Demand on the right.On the Shift Top-Level Demand screen, maintain the following entry:Shift Demand To: <the earliest week>Choose Adopt Proposal, the Quantity is automatically updated with the Proposed Quantity.Choose Apply. | The capacity issues are reduced.You can choose Undo or Redo icon to withdraw or resume your changes of simulation.You can choose Show Change History icon to review all your changes in the Global History area. |  |
| 10 | Check Multi-Level Material Simulation | Choose the next demand in red for a work center, for example, TURNING2.In the Top-Level Materials area, navigate to FG011, and choose Multi-Level Material Simulation. | The Multi-Level Material Simulation screen displays. |  |
| 11 | Change Source of Supply | On the Multi-Level Material Simulation screen, you could see simulation details for BOM components in Bill of Material area.Choose the Issues for semi-finished goods SG014, and then choose Change Source of Supply to distribute demand into different production versions to balance workload.On the Change Source of Supply screen, choose Adopt Proposal, the Quantity Distribution for two production versions are automatically updated with the Proposed Distribution. Choose Apply. | The capacity issues are reduced. |  |
| 12 | Check Simulation Component | Choose Simulation Views at the top and choose Simulation Components.On the Simulation Components screen, you could see simulation quantities for both head materials and components. You can change display mode from Materials to Supply. | The Simulation Components screen displays. |  |
| 13 | Check Simulation Summary | Choose Simulation Summary at the top.On the Simulation Summary screen, you could check Change in Demand, Change in Capacity, Preproduction or Early Procurement, Change of Source of Supply, Unresolved Issues, and Disregarded Capacity Issues. | The Simulation Summary screen displays. |  |
| 14 | Check Demand Plan Simulation Again | Choose Simulation Views at the top and navigate back to Demand Plan Simulation. | The Demand Plan Simulation screen displays. |  |
| 15 | Release Simulation | Choose Navigation Menu icon at the top left and navigate to Process pMRP Simulations.On the Process pMRP Simulations screen, filter the simulation with the reference ID and choose Go.Reference Data : 54U_PMRP_<MMDD>Choose Release for the copied simulation with less capacity issues.On the Release screen, make following entries and choose Release.Under Create PIRs section,DDMRP Components: unmarkedTop-Level Materials: <X>Subassembly Components: <X>Under Top-Level Materials maintain the below,Requirement Version: 00 Requirements PlanVersion Active: YesUnder Subassembly Components maintain the below,Requirement Version: 00 Requirements PlanVersion Active: Yes | The simulation status is changed into Released. |  |

#### Check Planned Independent Requirements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the adjusted PIRs for top level material FG011. They are adjusted to ensure less capacity issues.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Material: FG011Plant: 3310Period Indicator: Weekly (W)Version Active: Select all options |  |  |
| 5 | Filter Result | Choose Go to execute. | The material item displays. |  |
| 6 | Check PIRs | Select the filtered material items whose last modified date is today, and choose Edit in the upper-right corner.On the Edit PIRs screen, check the generated PIRs for FG011. | The PIRs for top level materials are updated into requirement plan version 00. |  |

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

The Make-to-Stock finished goods are planned at plant level. There is now a requirement for the FG011 material and 3310 plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirement Planning (MRP)Job Name: <MRP for FG011>Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.For 3 Parameters section:Plant: 3310Material: FG011Changed BOM Components: selectScheduling: 2Planning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG011 in the search box and choose Go at the top right section of the screen. | System schedules a new MRP job. |  |

#### Evaluate Stock/Requirements Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock/requirements situation.

Prerequisite

Requirement planning is carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments (F2101A) screen displays. |  |
| 3 | Select Material | In the field Material, enter material RM011, RM012, RM013, RM014, RM017, RM018 and RM019 choose GO. |  |  |
| 4 | Review Stock Availability | Analyze the stock availability situation of materials RM011, RM012, RM013, RM014, RM017, RM018 and RM019 | Stock availability situation of materials RM011, RM012, RM013, RM014, RM017, RM018 and RM019 is analyzed/noted with the data present under columns First Shortage, Shortage quantity, Shortage Duration (Working Days), Stock availability. |  |
| 5 | Selection of materials | Use the Check box and select the rows which have the Material No RM011,RM012, RM013, RM014, RM017, RM018 and RM019 and click on Manage Materials. | The Material and Material Details subscreens display.Stock/Requirement list for all the selected materials is displayed. |  |
| 6 | Display Purchase Requisition | From the list on the Materials sub screen on your left, select the material for which you want to check for the purchase Requisition:Material: RM011, RM012.On the Material Details sub screen, choose PurRqs XXXX in the MRP Element column. You can choose the earliest purchase requisition.Note The BOM explosion during the MRP run has generated dependent requirements for the demand-driven planned components. If there is not enough inventory to fulfill the requirements, purchase requisitions are created for externally purchase requisition. | The selected purchase Requisition details are displayed on pop-up screen.The Purchase Requisition is generated only when there is shortage for these materials.If you want to display more information of the Purchase Requisition, choose Open > Document Info at the bottom right of the dialog box.Note down the Purchase Requisition numbers for both materials. |  |
| 7 | Display Schedule Lines | From the list on the Material sub screen on your left, select the material for which you want to check for the schedule line:Material: RM013On the Material Details sub screen, choose SchLne XXXX in the MRP Element column. You can choose the earliest schedule lines.Note The BOM explosion during the MRP run has generated dependent requirements for the demand-driven planned components. If there is not enough inventory to fulfill the requirements, delivery schedule lines are created for the scheduling agreement item in place. | The selected schedule line item details are displayed on pop-up screen.The delivery schedule line items is generated only when there is shortage for these materials.If you want to display more information of the Purchase Requisition, choose Open > Document Info at the bottom right of the dialog box.Select the item and select the Delivery Schedule.Note down the Schedule line item number, Scheduled quantity and Open quantity. |  |

### Procurement of Raw Materials

#### Convert Purchase Requisitions to Purchase Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity when you want to convert assigned Purchase Requisitions to Purchase Orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Process Purchase Requisitions (F1048A) .Note If you want to use the Save Draft feature in this app, you have to use a personalized user. | A list of Requisitions is displayed. |  |
| 3 | Search for Purchase Requisition | Enter the Purchase Requisition Number for the RM011 material (that you noted in the previous topic) and choose Go.Note If the Purchase Requisition Number is not displayed in the Filters, choose Adapt Filters. On the Adapt Filters pop-up screen find Purchase Requisition Data choose More Filters. Select Purchase Requisition Number and choose OK. Choose Go. | The Purchase Requisition is displayed. |  |
| 4 | Select Purchase Requisition | Select the Purchase Requisition. | The Purchase Requisition has been selected for source assignment. |  |
| 5 | Assign Source to Purchase Requisition | Choose Show More per Row button.If the Purchase Requisition has been assigned the source, the same is displayed under the Assigned Supplier column, then you do not need to assign source again in this step and proceed to next step.If the Purchase Requisition has not been assigned to the source, choose Assign Source of Supply, and select Info record (XXXXXX) as the source. | The assignment of one source to the requisition is done.Purchase requisition updated successfully. |  |
| 6 | Prepare the Purchase Order | Select the purchase Requisition where the assigned supplier is displayed and choose Create Purchase Order.You can close any warning or error messages that are displayed. | The Manage Purchase Requisitions screen is displayed. |  |
| 7 | Create the Purchase Order | In the New Purchase Order screen, make the following entries:Purchase Order Type: Standard PO.Choose Order. | The purchase order is created. |  |
| 8 | Back to Manage Purchase Requisition | In the dialog box, choose OK. | Purchase Requisition list is displayed again.The Processing Status of Purchase Requisition has been changed to PO created. |  |
| 9 | Convert Purchase Requisition to Purchase Order | Repeat steps 2 to 8 of this process to convert the Purchase Requisition of RM012 to Purchase Order.In step 5, choose Contract (xxxxx) as the source instead of Purchase Info Record. | The Purchase Order is created. Note the Purchase Order number. |  |

|  |
| --- |
| Note For Embargo CheckIf you want to execute an Embargo Control please refer to Scope Item 1WC (Embargo Control). |

#### Display Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you view the status of purchase orders created in above step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders (F0842A)screen is displayed. |  |
| 3 | Search for Purchase Order | Enter the Purchase Order number noted in the earlier step for material RM011 and choose Go. | The Purchase Order is displayed. |  |
| 4 | Check status of Purchase Order | Status of Purchase Order is mentioned under column Approval Status. Check the code present under this column. | The Purchase Order must be in status Approved (or) no need of approval. |  |
| 5 | Repeat the Steps | Repeat step number 2 to 4 for the Purchase Order for material RM012. While repeating the step, use the Purchase Order number of RM012 noted in the previous step. |  |  |

If the purchase orders that you have created are to be approved and if you do not know who should approve the purchase orders you created, then you can use the Manage Purchase Orders (F0842A) app to display the created purchase order: Go to the Approval Details tab and check the approvers listed in section Approval Details. For more information about approving the purchase order, refer to the test script of scope item J45.

#### Create Inbound Delivery

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
| 1 | Log on | Log onto the SAP Fiori Launchpad using the Role Receiving Specialist . | The Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Inbound Deliveries for Purchase Orders (VL34) . | The Generation of Inbound Deliveries screen displays. |  |
| 3 | Create Inbound Delivery | Make the following entries then choose Execute:Document Number: XXX.Enter the purchase order number created in previous step for the RM011 material.Delivery Date:XXX Delete the default date and enter the delivery date in purchase orderTest Run: uncheckedThe Inbound Delivery Number is displayed, write it down for further use. | A new Inbound Delivery is created.The Inbound Delivery Number is displayed. |  |
| 4 | Repeat step to create inbound delivery for remaining purchase order. | Repeat Step 3 to create inbound delivery for the purchase order created for RM012. |  |  |

#### Confirm Quantities for Putaway

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity confirms that all the materials have been put away in the correct quantities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the Role Receiving Specialist . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Inbound Deliveries for Putaway (VL06IP) . | The Inbound Deliveries for Putaway screen displays. |  |
| 3 | Enter inbound delivery number | Make the following entries then choose Execute:Inbound Delivery: XXX created in the previous step for the RM011 material. | The selected Inbound Delivery displays. |  |
| 4 | Change the inbound delivery | Select Inbound deliveries and click Change Inbound Deliveries. | The Inbound Delivery XXX Change: Overview screen displays. |  |
| 5 | Confirm Quantities for Putaway | In Item Overview tab, input the Putaway Qty: XXXNote The put away quantity should equal to the delivery QtyAnd choose Save. | Back to the Inbound Deliveries for Putaway screen and Inbound Delivery XXX has been saved message displays. |  |
| 6 | Repeat step | Repeat steps 2 to 5 to confirm Putaway quantity present in Inbound delivery of RM012. While repeating these steps, use Inbound delivery of RM012. |  |  |

#### Post Goods Receipt for Inbound Delivery

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
| 1 | Log on | Log onto the SAP Fiori Launchpad using the Role Receiving Specialist . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Receipt for Inbound Delivery (F2502). | The Goods Receipt screen displays. |  |
| 3 | Enter inbound delivery number | Make the following entries then choose Enter:Enter Inbound Delivery Number: XXX that you created in the previous step for the RM011 material. | The Goods Receipt screen displays.The selected Inbound Deliveries are shown. |  |
| 4 | Change the inbound delivery | Select the item for this inbound delivery. Choose Post. | The goods receipt is posted.A success message is shown. |  |
| 5 | Repeat previous steps to post GR for remaining Inbound delivery | Repeat the steps 2 to 4 to perform the goods receipt for inbound delivery of RM012. While repeating this process, in step number 3, use the inbound delivery of RM012. | The goods receipt is posted.A success message is shown. |  |

#### Display Material Stock Before Quality Inspection (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, a review of the material stock is done. Due to quality inspection, the material is not available for other processing.

Prerequisite

The goods receipt from purchase order was posted for the trading goods to quality inspection stock.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock Single Material screen displays. |  |
| 3 | Enter Material | Make the following entries and choose Enter:Material: RM011 | Stock for the material is displayed. |  |
| 4 | Check Stock Quantity | Check the Quality Inspection Stock under the plant 3310 and storage location 331C. | Quantity received is posted in quality stock. |  |

#### Quality Inspection

##### Display Open Inspection Lots (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection lot is used to record the results of the inspection operation. In this optional step, the references to the goods receipt and purchase order are verified as well as the sample size used for quality inspection reviewed.

Prerequisite

In this scope item, the inspection lot is created automatically upon goods receipt for the purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots screen displays. |  |
| 3 | Select Inspection Lot | In the inspection lot list, select the inspection lot which you created before. | Inspection lot is displayed. |  |
| 4 | Check Inspection Lot by Selecting the Line | Under Origin, verify the referenced purchase order and material document. | The purchase order number and material document number from which the inspection lot originates are displayed. |  |
| 5 | Choose Operation (optional) | In Result, choose operation QM for Procurement GR. | For checking the attachment in the inspection method optionally.If you have attached a document in the inspection method as described in BNQ - Create Quality Inspection Plan - MDS, the Quality Technician can review the attachment referring to step 7 to 9. |  |
| 6 | Choose Characteristic (optional) | Click Surface in the characteristics column. | A dialog box appears with the Characteristics Details with the link to the Inspection Method. |  |
| 7 | Display the Attachment (optional) | Under Documents, the attachment for an illustration of the surface is displayed. |  |  |
| 8 | Display Text | In General , Long Text is displayed. |  |  |

##### Record Inspection Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

If inspection results shall be recorded for one or only a few inspection lots, execute the following process flow:

|  |
| --- |
| Note For the purpose of recording multiple results for several inspection lots, the app Record Inspection Results in Table Form (F3365) can be used. In this app you can record the inspection results for several master inspection characteristics for different inspection lots in a table on a single screen, for example inspecting one characteristic for several materials. This is described in the optional step. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A). | The Record Inspection Results screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Purchase Document: From previous step | If purchase order is not displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, select Purchase Order and choose OK. Choose Go. |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot. |  |  |
| 5 | Record Results | Choose Record Multiple Results in the bottom-right corner. |  |  |
| 6 | Enter Inspection Result | Depending on the inspection result, select one of the following two options:Positive ResultSurface: Code Group - Code SURFACE 0020 (Smooth)Length: Mean Value (cm): 160Negative ResultSurface: Code Group - Code SURFACE 0010 (Rough)Length: Mean Value (cm): 90 | For qualitative characteristic (Surface) the search help is needed to select a value. For the quantitative characteristic (Length) a number can be entered directly.The default number of inspected objects is calculated based on the sample size reviewed in an earlier step. The number of inspected objects can be manually changed. As well a number of nonconforming objects can be maintained directly in the respective fields for every inspection characteristic. |  |
| 7 | Save Inspection Lot | Choose Save. | The inspection lot is saved. QM Inspection for procurement goods has been performed and result recorded. |  |

Optional: Process-Optimized Results Recording for Multiple Inspection Lots

If inspection results shall be recorded for multiple inspection lots at the same time (mass processing), execute the following process flow.

|  |
| --- |
| Caution Note that this app can only be used for quality inspections with master inspection characteristics. It is not possible to capture inspection results for inspections with plan characteristics. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results in Table Form (F3365). | The Record Inspection Results in Table Form screen displays. |  |
| 3 | Enter Filter Fields | Maintain filter values and choose Go. | A list of inspection lots is displayed. |  |
| 4 | Select Inspection Lots and Inspection Characteristics | Select the inspection lots for which inspection results shall be recorded and choose Record Multiple Results.In the pop-up window Select Characteristics for Result Recording, select the master inspection characteristics for which inspection results shall be recorded and choose button OK. | The Record Inspection Results in Table Form screen displays.Note The system creates one table line item per inspection lot operation. Each master inspection characteristic is displayed in a separate column. The valuation of the inspection characteristic is displayed in a separate adjacent column. If a master inspection characteristic is assigned to another inspection operation, the respective table field is grayed out. |  |
| 5 | Show Inspection Details (Optional) | Click one inspection characteristic in the table and choose Show Details. | The side panel opens and detailed inspection data are displayed (e.g. inspection specifications, master inspection characteristic, inspection method, test equipment, and inspection remarks). |  |
| 6 | Show Work Center (Optional) | Choose the Settings icon in the upper-right corner of the table. In the Define Column Properties pop-up, select Work Center and choose OK. | An additional Work Center column is displayed. |  |
| 7 | Enter Inspection Results | Enter inspection results. See above for example data. | For qualitative results, a corresponding value help is provided. Quantitative inspection results can be entered directly.Note Depending on the defined valuation mode (check inspection method details), the valuation is either done automatically by the system or must be done manually by the user.If an inspection result requires an inspection remark (check master inspection characteristic settings), it is not possible to navigate to the next inspection result. Open Details side panel and maintain the inspection remark in section Remarks. |  |
| 8 | Save Inspection Data | Choose Save. | Inspection results are saved and a success message is displayed. |  |

##### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the assembly depending on the inspection result. If you do not want to use the Quality Engineer Overview (F2360), you can open the Manage Usage Decisions (F2345) app directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Usage Decisions (F2345). | The Manage Usage Decisions screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Inspection Lot: From previous step |  |  |
| 4 | Select Corresponding Inspection Lot | Select the corresponding inspection lot. | The Inspection Lot screen displays. |  |
| 5 | Display Defects | Scroll down to the Defects area. Check the details of Defects. | Only available you when have recorded a Negative result. For a surface rejection, there will be a surface defect, for a length rejection, there will be a tolerance defect displayed. |  |
| 6 | Choose Edit and Add Document | Choose Edit. In the Document section choose Upload, select the path and add the document. | For example to upload pictures to visualize the defect. |  |
| 7 | Enter UD code | Depending on the inspection result, select one of the following two options and then confirm with Save.UD code: A1 (Accepted – unrestricted stock)A2 (Accepted-unrestricted – minor quality)A3 (Accepted-unrestricted-sample consumption)Negative ResultUD code: R1 (Rejected – blocked stock)R210(Rejected-return supplier w/o delivery)R220 (Rejected-return supplier with delivery)Choose Yes if dialog Confirmation Prompt appear. | Note The corresponding Stock Posting is processed automatically in the background for the complete quantity for Usage Decision codes A1, A2, R1, R210 and R220. |  |
| 8 | Modify Stock Posting (Optional) | In the Inspection Lot Stock section, enter the quantities to be posted in different stock posting proposals. | Note If you want to return a subset with UD code R220, you can split the quantity and post To Unrestricted Use and Return Inventory Posting, respectively. If you want to document sample consumption with UD code A3, you can split the quantity and post To Unrestricted Use and To Sample Consumption, respectively. It is also possible to transfer the (partial or full) quantity to a different material. |  |
| 8 | Save Usage Decision | Choose Save. | The usage decision is made with regard to the trading goods. The system automatically triggers the material movements associated with the usage decision code. |  |

#### Display Material Stock after Quality Inspection (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, we now verify the material movement done based on the usage decision codes by looking again at the material stock.

Procedure

Dependent on the usage decision of the previous steps, the quantity of the material is posted differently.

- Positive Result (A1, A2,): quantity is increased in Unrestricted Use Stock and quantity is reduced in Quality Inspection Stock
- Positive Result for ‘sample consumption’ (A3): partial quantity is increased in Unrestricted Stock, inspected quantity is consumed and therefore not in stock anymore, and full quantity is reduced in Quality Inspection Stock
- Negative Result ‘Blocked Stock’ (R1) : quantity is increased in Blocked Stock and quantity is reduced in Quality Inspection Stock
- Negative Result ‘Return to Supplier w/o Delivery’ (R210): quantity is reduced in Quality Inspection Stock
- Negative Result ‘Return to Supplier with Delivery’ (R220): quantity is increased in return storage location Blocked Stock and quantity is reduced in Quality Inspection Stock

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076) . | The Stock – Single Material screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and press Enter.Material:RM011 |  |  |
| 4 | Check Stock Quantity | Check the changed quantities of the Quality Inspection Stock, Unrestricted Use Stock (in case of positive usage decision) or Blocked storage location331A/331R (in case of negative usage decision). | The stock quantities for material RM011 are updated based on the quality inspection and respective usage decision of the previous steps. |  |

#### Evaluate Stock/Requirements Situation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock/requirements situation.

Prerequisite

Requirement planning is carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments (F2101A) screen displays. |  |
| 3 | Select Material | In the field Material, enter material RM011 & RM012 choose GO. |  |  |
| 4 | Review Stock Availability | Analyze the stock availability situation of materials RM011 & RM012. | Stock availability situation of materials RM011 & RM012 is analyzed/noted with the data present under columns First Shortage, Shortage quantity, Shortage Duration (Working Days), Stock availability. |  |
| 5 | Selection of materials | Use the Check box and select the rows which have the Material No RM011 & RM012 and and click on Manage Materials. | The Material and Material Details subscreens display.Stock/Requirement list for all the selected materials is displayed. |  |
| 6 | Display stock situation of raw materials | From the list on the Material sub screen on your left, select the material for which you want to check for the purchase order:Material: RM011 & RM012Observe the stock situation for material RM011 & RM012. | Stock quantity has increased by the quantity of goods receipt done in earlier step. |  |

#### Display Procurement Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In a single page, Purchaser can have a look at details of multiple purchasing documents. For example, purchaser can monitor purchase contracts, monitor unsourced purchase requisition items, Monitor overdue purchase order items. Monitor purchase order items by delivery schedule date.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Procurement Overview (F1990). | The Procurement Overview (F1990) screen displays. |  |
| 3 | Selection criteria | Enter data in following fields and choose GO.Display Currency: AEDPurchasing Organisation: 3310Objective of this step is to show the inbuilt analytical capabilities in procurement area. Expectation in this step for the tester is to ensure that system displays different procurement object cards and no need to do any additional validation. | System displays multiple purchase cards on the screen.For example:Monitor purchase contracts: Displays the number of purchase contracts (X of XXX) on this card. This card also displays limited number of purchase contract numbers on screen.Monitor purchase requisition items: Displays the number of purchase requisitions (X of XXX) on this card. We can sort it by criteria: Open or unsourced.Monitor Purchase Order Items: Displays the number of purchase orders (X of XXX) on this card. We can sort it by criteria: overdue or in approval.Monitor Supplier confirmations: We can sort it by Missing Confirmation, Delivery Date Variance, Quantity Variance.And other procurement related cards will appear |  |

### Raw Material Procurement based on Scheduling Agreement

#### Display Delivery Schedule

Purpose

The purpose of this activity is to check the delivery schedule for the scheduling agreement if it has been generated while executing MRP Run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Logon on to Fiori launchpad as Purchaser . | The SAP Fiori launchpad displays. |  |
| 2. | Access the App | Open Manage Purchase Scheduling Agreements (F2179) . | You will get into Manage Scheduling Agreements list page. |  |
| 3. | Find scheduling agreement number | Find the correct scheduling agreement through the search criteria, populate: Purchasing Org. 3310, Agreement Type LP (Scheduling Agreement), Material RM013, then choose Go. Select one item from the search result. | System displays a list of scheduling agreements under Scheduling Agreements. |  |
| 4. | Select Scheduling Agreement | Select the scheduling agreement for material RM013 noted in earlier section.Navigate to the selected scheduling agreement by clicking on cheveron (>) or by directly clicking on the scheduling agreement number from the list page. | The Scheduling agreement header object page appears in display mode. |  |
| 5. | Maintain Delivery Schedule | Click on Edit at the right upper corner on the Manage Scheduling Agreement Header Object page.In Items tab, click on the desired Scheduling Agreement Item for which delivery schedule needs to be displayed. | The Scheduling Agreement Item screen displays. |  |
| 6. | Maintain Delivery Schedule | Go to the Schedule Lines section on the Scheduling Agreement Item screen. System displays the list of schedule line number under column Schedule line.Check the delivery date and update <todays date> in Schedule line having open quantity. Choose Save. Note the schedule line number, scheduled quantity and open quantity. | Schedule line numbers displayed under column Schedule line |  |

#### Print Scheduling Agreement (Optional)

Purpose

The purpose of this activity is to print view the scheduling agreement for the product/supplier combination for the new Scheduling agreement or for the one which is already present in the system

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto Fiori launchpad | Log onto the Fiori launchpad as Purchaser . | The SAP Fiori Launchpad displays. |  |
| 2. | Access the App | Open Manage Purchase Scheduling Agreements (F2179) . | The Manage Purchase Scheduling Agreements screen displays. |  |
| 3. | Find scheduling agreement number | Enter the purchase scheduling agreement created above or find the appropriate scheduling agreement through the search criteria, such as: Supplier<supplier number created for this scenario>, Agreement Type LP, Purchasing Organization 3310, then choose Go. Select one item from the search result. | The desired scheduling agreement appears on the list page of Manage Purchase Scheduling Agreements. |  |
| 4. | Select Scheduling Agreement | Navigate to the selected scheduling agreement by clicking on Chevron (>) or by directly clicking on the Scheduling agreement number from the list page. | The Scheduling agreement header object page appears in display mode. |  |
| 5. | View the output form for scheduling agreement | Go to the Output controls tab and view the output settings maintained for the scheduling agreement. Click on Show More per Row to see PDF sign | PDF form for scheduling agreement shall open. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this step, you post the goods receipt for the material against the scheduling agreement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as Warehouse Clerk . | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Post Goods Receipt for Purchasing Document (F0843). | The Goods Receipt Purchase Order screen appears. |  |
| 3 | Enter Purchase Order | Enter the scheduling agreement number and choose Enter. | The system displays the data for the goods receipt on the Goods Receipt screen. |  |
| 4 | Enter Delivery Note | Make the following entries:Delivery Note: <note number>Printing: Choose Individual slip from the drop-down list.And choose Enter. |  |  |
| 5 | Select Item | Select the items for which a goods receipt is to be posted. | The Post button is activated. |  |
| 6 | Post | Choose Post. | The system displays this message:1 document(s) created:Material Document5xxxxxxxxx 2xxx |  |

#### Evaluate the Stock/Requirement Situation (Optional)

Purpose

This process step shows you how to display the stock/requirements situation for material RM013 in the stock/requirements list.

Prerequisite

Goods Receipt is carried out for material RM013.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments (F2101A) screen displays. |  |
| 3 | Select Material | In the field Material, enter material RM013 and choose GO. | Stock Availability situation of material RM013 will be displayed. |  |
| 4 | Review Stock Availability | Analyze the stock availability situation of material RM013. | Stock availability situation of material RM013 is noted with the data present under columns Shortage quantity, Stock availability. |  |
| 5 | Selection of Materials | Use the Check box and select the rows which have the Material No RM013 and click Manage Materials present at the right side corner of the screen. | The Material and Material Details subscreens display.Stock/Requirement list for all the selected materials is displayed. |  |
| 6 | Display Stock Situation of Raw Materials | From the list on the Material sub screen on your left, select the material for which you want to check for the planned order:Material: RM013Observe the stock situation for material RM013. | Stock quantity has increased by the quantity of goods receipt done in earlier step. |  |

#### Display Procurement Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In a single page, Purchaser can have a look at details of multiple purchasing documents. For example, purchaser can monitor purchase contracts, monitor unsourced purchase requisition items, Monitor overdue purchase order items. Monitor purchase order items by delivery schedule date.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Procurement Overview (F1990). | The Procurement Overview (F1990) screen displays. |  |
| 3 | Selection criteria | Enter data in following fields and choose GO.Display Currency: AEDPurchasing Organisation: 3310Objective of this step is to show the inbuilt analytical capabilities in procurement area. Expectation in this step for the tester is to ensure that system displays different procurement object cards and no need to do any additional validation. | System displays multiple purchase cards on the screen.For example:Monitor purchase contracts: Displays the number of purchase contracts (X of XXX) on this card. This card also displays limited number of purchase contract numbers on screen.Monitor purchase requisition items: Displays the number of purchase requisitions (X of XXX) on this card. We can sort it by criteria: Open or unsourced.Monitor Purchase Order Items: Displays the number of purchase orders (X of XXX) on this card. We can sort it by criteria: overdue or in approval.Monitor Supplier confirmations: We can sort it by Missing Confirmation, Delivery Date Variance, Quantity Variance.And other procurement related cards will appear |  |

### Subcontracting with Serial Number Management

#### Convert Purchase Requisition to Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, a purchase requisition for planned subcontracting is assigned and a corresponding purchase order is created.

|  |
| --- |
| Note If you want to use the Save Draft feature in this app, you have to use a personalized user. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser role. | The SAP Fiori launchpad displays. |  |
| 2 | Open Manage Purchase Requisitions | Open Process Purchase Requisitions (F1048A). | A list of Requisitions is displayed. |  |
| 3 | Search for Purchase Requisition | Search for Purchase Requisition for material SG022 (using the purchase requisition that you noted in the previous topic) and choose Go.Note If the field Purchase Requisition Number is not displayed in the list of filters, choose Adapt Filters. On the Adapt Filters pop-up screen, search for Purchase Requisition Number. Select the entry Purchase Requisition Number and choose OK. | The Purchase Requisition is displayed. |  |
| 4 | Assign Source to Purchase Requisition | Select the purchase requisition.Choose Show More per Row button on the side of Create Contract. If the Purchase Requisition has been assigned the source, the same is displayed under the Assigned Supplier column, then you do not need to assign source again in this step and proceed to next step.If the Purchase Requisition has not been assigned to the source, choose Assign Source of Supply, and select Info record (XXXXXX) as the source. | The assignment of one source to the requisition is done. The Purchase Requisition is updated successfully. |  |
| 5 | Prepare the Purchase Order | Select the purchase requisition where the assigned supplier is displayed and choose Create Purchase Order. You can close any warning or error messages that are displayed. | The Purchase Order screen is displayed. |  |
| 6 | Create the Purchase Order | In the New Purchase Order screen, choose Standard PO from Purchase Order Type drop down list. Choose Order. | The purchase order is created. |  |
| 7 | Back to Manage Purchase Requisition | Choose Back to go to Purchase Requisitions list. | Purchase Requisition list is displayed again. The converted Purchase Requisition has disappeared from the list. |  |

#### Change Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity changes a purchase order for subcontract material.This activity is required to assign serial numbers to the semifinished good to be procured from Subcontractor.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the Fiori Launch Pad using the Purchaser role. | The Fiori Launch Pad is displayed. |  |
| 2 | Open Purchase Order | Open Change Purchase Order - Advanced (ME22N). | The Change Purchase Order screen is displayed with the last processed purchasing document. |  |
| 3 | Enter Purchase Order data | Click on Other Purchase Order and fill with the Purchase Order number created in previous step. Ensure that radio button Pur.Order is selected. Choose Other Document. | All data is entered. The Purchase Order displays. |  |
| 4 |  | In the area of Item Detail:Switch to Delivery Schedule, and choose Assign Serial Number. Choose Create Serial Number Automatically, and then choose Continue. | Serial Numbers are assigned to subassembly. |  |
| 5 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | The Purchase Order is updated. |  |

#### Monitor Subcontracting Documents (Optional)

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the Fiori App | Open Monitor Subcontracting Documents (F3095). | The Monitor Subcontracting Documents screen displays. |  |
| 3 | Monitor Subcontracting Document | Enter the following data:Subcontractor: 33300007Choose Go.Note If the subcontractor field does not appear on the screen, select the field on Adapt Filter. |  |  |
| 4 | Monitor Subcontracting Document | Choose View to check the Assembly Flow. | If you have multilevel subcontracting, the graph can be displayed here. |  |
| 5 | Manage Purchase Order | Check the details of your subcontracting document by clicking the item. |  |  |

#### Approve Purchase Orders (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

All the purchase orders that require release by an authorized person are listed and must be approved. About the PO approve user setting, please refer to the step Configure Your Release Conditions for PO Approval (Only for SAP S/4HANA Enterprise Management Cloud) in J45.

|  |
| --- |
| Note Only POs with a value higher than 500.00 AED can be released in this transaction. POs with a value under this amount do not need to be released. For POs under this amount, this step can be skipped. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as aPurchasing Manager. | The Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). |  |  |
| 3 | Check Purchase Order Status | Search for Purchase Order with Need Approval Status. | The Purchase Orders without follow-on documents (w/o status Follow-On Documents) and a net value of 500 AED or more have the status In Approval. |  |
| 4 | Release Purchase Order | Select the Purchase Order on the left side of the screen and choose Approve at the bottom right. | The Submit Decision screen is displayed. |  |
| 5 | Enter Release Reason | Enter the approval reason if necessary, and then choose Submit. | The Purchase Order is approved. |  |
| 6 | Back to Fiori Launch Pad | Choose the Home button to go back to the Fiori Launchpad. | The Fiori Launchpad is displayed. |  |

#### Create Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

|  |
| --- |
| Note This chapter does not apply to Brazil. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Display Subcontracting Stocks by Supplier (ME2ON). | The app name screen displays. |  |
| 3 | Subcontracting Cockpit (Original) | Enter the following data:Supplier (Original) : 33300007Assembly : SG022Plant : 3310Components Provided: RM33 and RM34With requirements from subcontracting Purchase Requisitions: XWith external receipts from Purchase Requisitions: XWith external receipts from Purchase Orders: XChoose Execute. |  |  |
| 4 | Subcontracting Cockpit (Original) | Expand the group of Requirements via SC Orders for below materials:Material (Original) : RM023, RM024, RM025 and RM026Find the line items with your purchase order number. Use Ctrl to select multiple lines.Select Create Delivery. |  |  |
| 5 | Creating Delivery for Subcontracting Purchase Orders | Enter Stor.Location for both lines:Stor.Location: 331AUse Ctrl to select multiple lines and choose Create Document.Note down your delivery number. |  |  |

#### Pick and Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

|  |
| --- |
| Note This chapter does not apply to Brazil. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Change Outbound Delivery (VL02N). | The app name screen displays. |  |
| 3 | Change Outbound Delivery (Original) | Enter the following data:Outbound Delivery: <your delivery>Choose Continue. |  |  |
| 4 | Picking | Choose Picking tab.Enter picked quantity equal to the delivery quantity. |  |  |
| 5 | Serial number | Select line item 10 (Material RM023)Choose Menu > Extras > Serial Number .Choose Create serial number automatically.Note down the serial number created.Choose Continue. |  |  |
| 6 |  | Repeat above step for material RM024. |  |  |
| 7 | Post Goods Issue (Original) | On the Delivery for Subcon. xxxxxxx Change: Overview screen, choose Post Goods Issue. |  |  |

#### Receive Goods from Subcontracting PO

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

|  |
| --- |
| Note This chapter does not apply to Brazil. |

In this step, you post the goods receipt for the material against the subcontracting PO.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The Fiori Launch Pad is displayed. |  |
| 2 | Open Post Goods Movement tile | Open Post Goods Movement (MIGO). | The Post Goods Receipt for Purchase Order (Original). screen is displayed. |  |
| 3 | Select Goods Receipt Order screen | On the Goods Receipt Order screen, make the following entries and choose Enter:Goods Receipt: <Select>Purchasing Order: <Select>Order number:<Purchase Order number>GR goods receipt:101 | The items of the selected Purchase Order display. |  |
| 4 | Choose the Quantity tab and confirm the quantity | Confirm the quantity. |  |  |
| 5 | Select Item ok Indicator | Select the Item OK checkbox. |  |  |
| 6 | Serial number | Expand item SG022.Select the line item for raw material RM023.In detailed data, switch to Serial Number tab.Enter the serial number noted in last chapter for RM023.Select the line item for raw material RM024.In detailed data, switch to Serial Number tab.Enter the serial number noted in last chapter for RM024. |  |  |
| 7 | Post | Choose Post. | The system displays the message1 document(s) created: Material document 5000000XX 20XX.. |  |

### Repetitive Production Execution for Semi-Finished Component

#### Adjust Planning in Planning Table

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to plan the production of materials on the production lines.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Repetitive Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Repetitive Manufacturing (MF50). |  |  |
| 3 | Enter Details | On the Planning Table Initial Screen: Change Mode screen, make the following entries:Plant: 3310Under Selection by Production Version section, choose radio button Material and then enter material number：Material: SG011Choose Execute. | The Planning Table for Repetitive Manufacturing: Change Mode screen displays. |  |
| 4 | Change the Quantity | In the Material Data section, change any planned quantities in the row 0001 WINDING.If you want to change the periods in the planning table, choose Menu > View > Period > Week (Month or Day) . | In the Total Capacity Data section, you can monitor capacity load utilization of the production lines.More information about usage of the planning table for capacity planning and planning quantities, please refer to appendix Usage of the Planning Table for planning Production Quantities. |  |
| 5 | Save | Choose Save. |  |  |

Result

Material production is planned on production lines and the planned orders are fixed.

When there are quantity changes, log on the SAP Fiori launchpad as a Production Planner, access the Monitor Material Coverage app, and review the planned order number.

#### Check Range of Stock Coverage

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with the following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 4 | Select Material | Choose Adapt Filters to add the Material filter if not added, enter the following value, and choose Go:Material: RM013Select the material and choose Manage Materials. | The Manage Material Coverage screen displays. |  |
| 5 | Rescheduling Check (Optional) | In the Stock/Requirements List, the Rescheduling column displays the rescheduling status of the following MRP Elements.PurReqPurchase OrdersPlanned OrdersProduction OrdersProcess OrdersYou can choose below icons in the Rescheduling column to perform corresponding actions.Reschedule in (Bring operation forward if the receipt element lies after the requirement date)Reschedule out (Postpone operation, if the receipt element lies before the requirement date)Plan Process according to scheduleCancel ProcessExcess StockExcess in individual segment | The corresponding actions are performed. |  |
| 6 | Review the Status and Coverage Days | Make the following entries and choose Refresh:Shortage Definition: Stock Day's Supply |  |  |
| 7 | Repeat for other material | Repeat the steps 2 to 5 for the RM014 material. |  |  |
| 8 | Return to Home | Choose the Home icon. |  |  |

#### Create Inspection Lot for Production Version

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/FailComment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Process Inspection Lots for Production Versions (MFPR) | The Process Inspection Lots for Production Versions(MFPR) screen displays. |  |
| 3 | Enter Details | Make the following entries and choose Execute.QM : ActivePlant: 3310Material number: SG011Production version: 0001 | The Process Inspection Lots for Production Versions(MFPR) screen displays.The green flag indicates the materials that are relevant to Quality Management |  |
| 4 | Create inspection lot | Click the option 'Selection of Versions w/o Inspection Lot' for material and then choose'Create Inspection Lot'to generate the inspection lots for the production version | Inspection lot for matreial and production version created.Note The red light in the list indicates that results recording and usage decision are already done for an inspection lot and the system is now ready to create a new inspection lot. The green light indicates that results recording and usage decision for the inspection lot are pending. |  |

#### Material Staging

Purpose

This process step shows you how to stage materials for production. In case there is sufficient stock available on the production storage location 331B, no line items are generated. If you want to print the Pull List, please also execute relevant steps and check printing result.

Prerequisites

Stock must be available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Repetitive Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stage Materials for Production (MF60). | The Material Staging for Planned Orders screen displays. |  |
| 3 | Enter Details | Make the following entries and choose Execute.Staging Types: SLoc.Level (Activate checkbox)Plant: 3310Selection Horizon for Remts: <A date>Note Requirements falling on a later date will not be taken into account in the pull list.Planned Orders: <Planned Order Number> Access Manage Material Coverage - New Version (F0251A) app as a Production Planner to view the planned order generated for SG011.Bulk Material: <Adapt Indicator if necessary> | The Pull List: Storage Location Level screen displays. |  |
| 4 | Choose Replenishment Proposal | Select the required line items from the left-hand margin and choose Replenishment Proposals from the top of the screen. |  |  |
| 5 | Choose Replenishment Elements | Review the staged quantity and choose Replenishment elements. |  |  |
| 6 | Enter Replenishment Storage Location | On the bottom half of the split screen, select the lines and enter the replenishment storage location 331C for material RM014 and for material RM013. |  |  |
| 7 | Choose Print | If you want to print the Pull List, you can execute following printing steps, else please go directly to step 12.Choose Print at the upper right of the screen. |  |  |
| 8 | Print List Selection | In the popup window Print List Selection, choose following entries and choose Continue:Print List Selection: Replenishment Proposals | The print list will be displayed. |  |
| 9 | Check Print List | Check the print list, and choose Print at the upper right of the screen. |  |  |
| 10 | Select Output Parameters | In the popup window Print List Selection, choose following entries and choose Continue:Print List Selection: Replenishment Proposals | Message “Spool request (number XXXX) sent to SAP printer XXXX” indicates successful printing. |  |
| 11 | Go Back | Go back to the stage screen. |  |  |
| 12 | Select Stage | Select the replenishment element in the bottom half of the screen, and choose Stage at the middle of the screen. |  |  |
| 13 | Choose Save | Choose Save. |  |  |

#### Display Routing for Inspection Characteristics

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step we review the automatically created inspection point for operation 0020 as well as the inspection characteristics which will have to be maintained in the Quality inspection step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Routing (CA03). | The Display Routing: Initial Screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Continue.Material: SG011Plant: 3310 |  |  |
| 4 | Review the Inspection Points Setting | Double-click Operation 0020.Scroll down to the Quality Management: Inspection Points section.After reviewing, choose Back. | A Time-related inspection point is defined for this operation in the routing. |  |
| 5 | Review the Inspection Characteristics | Select Operation 0020 and choose Inspection Characteristics.There are two Master Inspection Characteristics: One is Qualitative –SurfaceThe others is Quantitative - Length | If Inspection Characteristics is not displayed, choose More. In the dialogue box, find Inspection Characteristics. |  |

#### Display Open Inspection Lots(Optional)

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
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots screen displays. |  |
| 3 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot which you created before. | Inspection lot is displayed. |  |
| 4 | Check Inspection Lot | Under Origin, verify the production version. | The production version from which the inspection lot originates is displayed. |  |
| 5 | Choose Operation (optional) | In Result , choose operation QM for Production Version. | For checking the attachment in the inspection method optionally.If you have attached a document in the inspection method as described in BNQ - Create Quality Inspection Plan, the Quality Technician can review the attachment referring to step 7 to 9. |  |
| 6 | Choose Characteristic (optional) | Click Surface in the characteristics column. | A dialog box appears with the Characteristics Details with the link to the Inspection Method. |  |
| 7 | Display the Attachment (optional) | Under Documents, the attachment for an illustration of the surface is displayed. |  |  |
| 8 | Display Text | In General , Long Text is displayed. |  |  |

#### Record Inspection Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you perform the inspection and record the result to decide if you can go on with the next operation of the production order. The result is recorded in the inspection lot according to the defined inspection parameters in the routing.

The master inspection characteristic diameter is valuated leveraging a SPC control chart. If the control chart has not been activated, yet, the user must valuate the character-istic manually. After activation of the control chart, the respective characteristic is automatically valuated by the system according to the control charts action limits.

As it is currently not possible to specify the control charts limits manually, a minimal amount of data points must have been collected before the card can be activated.

Prerequisite

The inspection is processed based on inspection lot. In this scope item, the inspection lot is automatically created upon release of the production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results - Hierarchical Worklist (QE51N). | The Results Recording Worklist screen displays.Note The app Record Results for Inspection Points (F2689) can be used as an alternative to capture inspection results for inspection points. However, manual valuation of an inspection characteristic with an inactive SPC card is only possible using the Record Inspection Results - Hierarchical Worklist (QE51N) app. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Execute.Plant： 3310Insp. Lot Origin： 13Material: SG011 | The Results Records: Characteristic Overview screen displays.If Order is not displayed in the Filters, please choose filters. On the popup screen Filters, find Production and choose More Filters. Select Order and choose OK. Choose Go. |  |
| 4 | Select the Corresponding Inspection Lot | On the left pane, expand the corresponding inspection lot which you want to record a result. | If a dialogue appears asking to save, choose Cancel. |  |
| 5 | Choose the First Inspection Point | Choose the first inspection point Date/Time which is under the activity 0020 Final work and quality inspection Work Center Work for machine/person. | When the work center is selected, the cursor jumps automatically to the result. |  |
| 6 | Enter Inspection Result for the First Inspection Point | Depending on the inspection result, select one of the following two options and then confirm with Choose.Positive ResultSurface – Result: 0020 (Smooth)Length – Result: 170Negative ResultSurface – Result: 0010 (Rough)Length – Result: 90 | For the qualitative characteristic surface the search help is needed to select a value.For the quantitative characteristic length a number can be entered directly.For the quantitative characteristic diameter five independent values need to be input and the system will calculate the mean value. |  |
| 7 | Close the First Inspection Point | Choose Enter. | The valuation and close are performed automatically for characteristics surface and length. Characteristic diameter must be valuated manually until there is an active control chart.. The status is set to 5 Processing is completed. |  |
| 8 | Save the First Inspection Point | Choose Save.Optional: Confirm produced quantity, e.g. 25 pc | The first inspection point is saved. |  |
| 9 | Create the Next Inspection Point | Choose Next Inspection (Shortest Interval 30 Min) which is under the activity 0020 Final work and quality inspection Work Center Work for machine/person with a click. | The next inspection point is created with current Date/Time.Normally, the next inspection point is created after 30 minutes. |  |
| 10 | Enter Inspection Result for the Next Inspection Point | Depending on the inspection result, select one of the following two options:Positive Result: see aboveNegative Result: see above | For the qualitative characteristic surface the search help is needed to select a value.For the quantitative characteristic length a number can be entered directly.For the quantitative characteristic diameter five independent values need to be input and the system will calculate the mean value. |  |
| 11 | Close the Next Inspection Point | Choose Enter. | The valuation and close are performed automatically for characteristics surface and length. Characteristic diameter must be valuated manually until there is an active control chart.The status is set to 5 Processing is completed. |  |
| 12 | Save the Next Inspection Point | Choose Save.Optional: Confirm produced quantity, e.g. 25 pc | The next inspection point is saved. Quality Inspection for in-process control is performed and the result is recorded. |  |

#### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the assembly depending on the inspection result. If you do not want to use the Quality Engineer Overview (F2360), you can open the Manage Usage Decisions (F2345) app directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Usage Decisions (F2345). | The Manage Usage Decisions (F2345) screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go:Plant: 3310Material: SG011Usage Decision Made: No |  |  |
| 4 | Click the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot created from previous step. |  |  |
| 5 | Review of Inspection Points | Select the tab Inspection Points, and review the detailed inspection results recorded previously. |  |  |
| 6 | Display Defects | Scroll down to the Defects area. Check the details of Defects. | Only available you have recoreded a Negative result. |  |
| 7 | Enter UD code | ChooseEdit and select the tab Usage Decision. The UD code you select depends on the Inspection Result, please select one of the following two options:Positive ResultUD code: A UD13 AcceptedNegative ResultUD code: R UD13 Rejected |  |  |
| 8 | Save Usage Decision | Choose Save. | Usage decision has been made for in process control inspection lot. |  |

#### Confirm Repetitive Manufacturing Inclusive Backflush of Materials

Purpose

This activity executes multiple activities in a single step, such as finished product goods receipt, backflush of component materials, posting of costs to cost collector, and creation of material and Journal Entry.

Errors can occur in backflushing. For example, there may not be sufficient warehouse stock available or important data, such as the issue storage location, may be missing. You then have the following options:

Make corrections immediately in a component overview.

Backlogs are created for the complete requirement quantities of the components with errors.

You can process these backlogs later. If negative stocks are allowed for the material in the storage location, the system posts negative stock quantities in certain circumstances.

|  |
| --- |
| Note Goods Receipt's Goods Movement Type is 131 and Goods Issue's Goods Movement Type is 261. |

Prerequisite

Planned orders must exist.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Repetitive Manufacturing role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Repetitive Manufacturing (MFBF). | The REM Confirmation - Transaction Variante: None screen displays. |  |
| 3 | Enter Selection Data | Make the following entries:Assembly backflush: XMake-to-stock: system proposesPlanned Order: Planned Order Number (from previous step)Note When the system proposes quantities, change as required.Choose Enter. | Note down the Posting Date and Document Date in the screen. |  |
| 4 | Post with Corrections | Choose Post with Correction.Select the production version, if prompted. |  |  |
| 5 | Post | Choose Post. |  |  |

|  |
| --- |
| Note The app Confirm Repetitive Manufacturing (MFBF) can be used to perform Reporting Point (RP) confirmation and backflush.Process step:Reporting point confirmation related steps can be performed by logging in as the Production Operator - Repetitive Manufacturing role.To perform reporting point confirmation in the app, enable the indicator for RP Backflush and provide the operation number of the reporting point in the field Reporting Point.Purpose of RP confirmation:Reporting Points are operations in the routing where milestone confirmation is enabled using appropriate control key.Reporting Point (RP) confirmation allows users to:Record and calculate the work in process quantitiesRecord component consumption at a specific operation (reporting point)Record scrap quantities at a specific operation (reporting point)Prerequisites for RP confirmation:Enable RP backflush indicator during configuration of the appropriate REM profile and assign the REM profile to the material master. REM profile can be adjusted to make RP backflush optional or mandatory.In routing, use control keys which have milestone confirmation enabled and assign the routing to appropriate production version.Standard cost estimate or cost estimate based on production version is completed for the material.Additional processes related to reporting point confirmation available for this role are:The app Display Reporting Point Quantity (MF26)to provide an overview of confirmation quantities at reporting points.The app Reset Reporting Point Confirmations (MF4R)to reverse the confirmation and backflush done at a reporting point. |

Result

Semi finished material is received into stock and raw materials are issued from stock. To view the Material document, log on the SAP Fiori Launchpad as the Warehouse Clerk, then open Material Document Overview.

### Kanban Discrete Production Execution for Semifinished component and Kanban Procurement SG014

#### Event-driven Kanban: External Processing and PDF Print of Kanban Card

In event-driven Kanban, material provision is not based on a predefined number of Kanbans or a predefined Kanban quantity. Instead, it is based on actual material consumption. The material is not continually provided and replenished at a supply area. It is only replenished when specifically requested. In this case, the material is procured externally with purchase orders.

##### Create Event-Driven Kanban

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a Kanban for material RM018.

Prerequisite

The control cycle for material RM018 is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Kanban Board (F4630). |  |  |
| 3 | Filter and Locate | Make following entries and press Enter.Plant: 3310Production Supply Area: KANBAN_04 |  |  |
| 4 | Create an Empty Kanban | In the control cycle of material RM018, choose + Create Containers. | The Create Containers screen displays. |  |
| 5 | Enter Details of Kanban | Check the parameters and choose Create.Requested Quantity: <Default quantity of containers, for example 100> | An empty event-driven container is created. |  |
| 6 | Check the Kanban Information | Choose the empty kanban container to display the replenishment information and the Purchasing Order. |  |  |

##### Variant 1: Set Kanban to FULL

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you set a Kanban to full for material RM018.

Prerequisite

The control cycle for material RM018 is created and one Kanban has the status Empty. The Purchasing Order is released.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Set Kanban Container Status (F3717). |  |  |
| 3 | Select the Kanban | Select a Kanban container on the left part of the screen. Choose Value Help icon to open Select: Barcode window. Choose Show Filter to make following entries and press Enter.Plant: 3310Production Supply Area: KANBAN_04From the Items list, choose one of the Kanban for RM018 with Current Status EMPTY. | The Kanban you entered displays. |  |
| 4 | Check Kanban Information | On the right part of the screen, check the following entry:Target Status: FULL |  |  |
| 5 | Set the Kanban to Full | On the left part of the screen, choose Save at the bottom. | The Kanban status is changed to FULL, which automatically results in a goods receipt in the storage location. |  |

##### Variant 2: Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you set a Kanban to full for material RM018.

Prerequisite

The control cycle for material RM018 is created and one Kanban has the status Empty.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Receipt for Purchasing Document (F0843) |  |  |
| 3 | Enter Purchase Order | Enter the purchase order ID and choose Enter.Purchase Document: <Purchase Order from Create Kanban step> |  |  |
| 4 | Select Item | From the Items section, select the goods receipt item to be posted.Material: RM018Quantity: <Quantity> | The Post button is activated. |  |
| 5 | Post | Choose Post. | The goods receipt to a purchase order with Kanban indicator automatically results in a status change of the Kanban to Full. This corresponds to the purchase order. |  |

##### Print the Kanban Card

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you print the Kanban card.

If you want to print the Kanban card in reality, you need to install SAP Cloud Print Manager for Pull Integration. For details, please refer to SAP note [3048273](https://me.sap.com/notes/3048273).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Collective Kanban Print (PK17). | The Collective Kanban Print screen displays. |  |
| 3 | Select Supply Area | Make the flowing entries and choose Execute.Plant: 3310Material: RM018 |  |  |
| 4 | Print the Kanban Card | Expand the list.Select the checkbox of your Kanban ID.Choose Print Kanbans.Choose Yes to confirm the Print Kanbans information. | The Kanban card is printing. |  |
| 5 | Display Kanban (Optional) | If you want to check detailed information for the Kanban, select the checkbox of your Kanban ID, and choose Display Kanban. |  |  |
| 6 | Back | Choose Home. |  |  |

Result

Administrator can check technical status of the printing queue through the app Maintain Print Queues (F1260).

#### Classic Kanban: In-House Production - Production Orders with MRP

This process step shows you how to produce the material SG014 via production order.

##### Set Available Kanban to EMPTY

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to set an available Kanban to EMPTY to trigger the in-house production of material SG014.

Prerequisite

The Kanban control cycle for material SG014 is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Set Kanban Container Status (F3717). |  |  |
| 3 | Select the Kanban | You can select a Kanban container on the left part of the screen. Choose the Value Help icon to open Select: Barcode window. Choose Show Filters to make following entries and press Enter.Plant: 3310Production Supply Area: KANBAN_05From the Items list, choose one of the Kanban for SG014 with Current Status WAIT or FULL. | The Kanban you entered displays on the Entered tab. |  |
| 4 | Check Kanban Information | On the right part of the screen, check the following entry:Target Status: EMPTY |  |  |
| 5 | Set the Kanban to Empty | On the left part of the screen, choose Save at the bottom. | Container saved. |  |
| 6 | Select Saved Container | On the left part of the screen, choose the Saved tab, and choose the changed container. |  |  |
| 7 | Check Generated Production Order | On the right part of the screen, check following:Current Status: EMPTYProduction Order: <XXXX>Note down the generated production order number. |  |  |

Result

When setting the container to empty the system will automatically create and directly release a production order with order type YPK1. With this strategy, one production order will be created for one empty Kanban container.

##### Production Capacity Leveling for Discrete Manufacturing

###### Check Capacity Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

During MRP, planned orders are created and scheduled to meet the material requirements. This process step shows you how to check the capacities for overload on bottleneck resources.

The Work center group is used as selection criterion to cover all coffee production resources the planner is responsible for.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Work Center Capacity (F3289). | The Manage Work Center Capacity (F3289) screen displays. |  |
| 3 | Check App Settings | Choose the user icon, and select App Settings.In the App Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if only following entry is assigned:Plant: 3310 ( Plant 1 AE) / MRP Controller: 001.Choose AOR status button of this entry if not assigned, click AOR status button of the corresponding entry to unassign any other entry then choose Back.Check entries for Load Personalization:Critical Load: 100%Normal Load: 80%Note You add Work Center Group as a filter by choosing Adapt Filters > More Filters (Master Data) . Select Work Center Group, choose OK, and then choose Go. |  |  |
| 4 | Filter | Choose following entries as filter, and choose Go.Editing Status: AllLoad Type: OverLoadEvaluation Horizon: From today to 8 weeks afterWe here only focus on capacity requirement due to PIRs we just created. | You can also use dynamic Evaluation Horizon: “Today – X / + Y days” and Overdue Horizon to calculate the overdue in a user-defined timeframe/ help checking utilization for the past.A list of bottleneck work centers with Overload situations are presented in an overview list.If no Overload work center listed, for test purpose, you can go back to Section “Create Planned Independent Requirements”, increase the PIRs for SG013 in step 7. Then rerun the whole process.Note If you want to check all work centers, choose Load Type: All |  |
| 5 | Check Bottleneck Work Centers | Choose button Settings above table. From Columns, you can choose different KPIs.KPIs on Capacity load (e.g. Max. Load, First Overload, Total Capacity Requirement etc.) give an overview on capacity situation.Critical situations are highlighted by utilization chart. Red/Yellow/Green bar shows different percentage level of capacity utilization, with color coding according to the Critical Load/Normal Load settings. The red bar indicates the available capacity exceeds Critical Load percentage, thus there is bottleneck with the work center.Note If the button Show Details is displayed on top of the table, click on it to display all selected columns. |  |  |
| 6 | Next Step | After identifying the bottleneck work center(s), stay on this page and go on with the test as described in the next section. |  |  |

###### Apply Changes to Available Capacity

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

For the bottleneck work centers, you may need to optimize capacity utilization by changing available capacity, e.g., via adding/changing shifts.

|  |
| --- |
| Note If you want to apply changes to multiple work centers at once, please use the app Mass Maintenance of Work Center Capacities (F5381). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Work Center Capacity (F3289). | The Manage Work Center Capacity (F3289) screen displays. |  |
| 3 | Check Capacity Situation | Check capacity utilization to identify bottleneck work center, as described in last section Check Capacity Situation. |  |  |
| 4 | Choose Bottleneck Work Center | Use the Work Center filter to filter bottleneck work centers with value help. From the displayed list, choose one of the work centers, for example:Work center: TURNING2( CP-WC2, Turning 2)Capacity Category: Machine (001) |  |  |
| 5 | Check Detailed Capacity Load | Details on capacity load of the specific work center capacity can be seen on the detailed page. Different views are available for monitoring composition and source order operations of capacity load.In Overview section, Utilization Chart gives graphical presentation of capacity load for specific period. You can choose different filter to show utilization in different period. Find the specific dates or period in which bottleneck would occur.In Operations section, the list provides details on related source orders, e.g. Planned Order for SG014 resp. .The Shift section provides a review of available capacity for the specific work center. Check the shifts on bottleneck dates and consider which shifts can be added on these dates to increase available capacity. For example, if shift YS3 is not arranged, you might consider adding YS3 on these dates for this work center. | Bottleneck dates and possible additional shifts are identified. |  |
| 6 | Choose Edit | Choose Edit in the upper right of the page. | Entries under section Shift become editable. |  |
| 7 | Add Shift | Under section Shift, choose +, and choose Add Shift. Enter following entries, and choose OK.Date Range: specific period during which you would like to add shift, dependent on the bottleneck datesShift Definition: YS3 (add other shifts if YS3 is already assigned)Recurrence: Daily | Add Shift screen pops up. |  |
| 8 | Check Shift is Added | Check items in Shift section, choose More at the bottom of the page to show more entries. Shift YS3 is added for the Date Range you specified.You can choose Settings icon above the table, to set filter e.g., Shift Definition equals to YS3, in order to shorten the list.After checking, choose Save. |  |  |
| 9 | Further Adjustment (Optional) | On the detailed Work Center Capacity screen, choose Edit in the upper right of the page.Under section Shift, you can adjust following parameters if needed, and choose Save.Shift Utilization: for example, 150%Number of Capacities: for example, 2In order to resolve your overload situation you could also use the function Copy Shifts in the Display mode of work center capacity, to copy a shift from one work center to another. |  |  |
| 10 | Check Bottleneck | Check capacity utilization in Overview section. After adding shift, capacity utilization during the specific period should be decreased, to reflect better match between requirement capacity and available capacity. Check if the bottleneck is resolved (all the bars are green), if not, please go back and repeat step 2-6 till no overload anymore. | The bottleneck is resolved. |  |
| 11 | Check Bottleneck for all the Resources | For all the other bottleneck resources, repeat step 1-7 to apply changes to available capacity.Note If you already solve all bottlenecks here, you will not have bottleneck situations available for the following Production Capacity Leveling Process. Even though you can execute capacity leveling without bottleneck situation we recommend to partly keep the bottlenecks. | The bottleneck for all resources is resolved. |  |

###### Production Scheduling

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In preliminary steps, the planned orders are generated after MRP Run, and the capacity situation is evaluated and adjusted. This process step shows you how to assign orders and operations from the initially created production plan to available timeslots of capacities.

Procedure

| Procedure Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Capacity Scheduling Table (F3770). |  |  |
| 3 | Check App Settings | In the App Settings dialog box, check if only below entry is assigned:For Industry Type, select the following value and choose OK:Industry Type: DiscreteIn the Basis Controls section, select Area for Responsibility. Select Plant and MRP Controller and choose Assign. Check if only below entries are assigned:Plant 1 AE (3310)MRP Controller 001 (001) |  |  |
| 4 | Filter | Choose Adapt Filters. Flag the entry Work Center Group and choose OK.Choose the following entries as filter and choose Go.Evaluation Horizon: for example, next 1 monthStatus: Not Dispatched and Dispatched | Critical operation for orders which fulfill the search criteria are displayed.If the tested products are MTO relevant, choose the settings to check Sales Orders and Sales Order Items. |  |
| 5 | Choose Order | Orders for , SG014 and SG013 are displayed in the list. Choose the desired order you want to dispatch. | The Capacity Scheduling Table screen displays. |  |
| 6 | Check Operation Information | In the top section of the detailed screen, check the detailed information about the critical operation.. |  |  |
| 7 | Check Available Time Buckets | In the below area of the right panel, the available source of supply would display under the grid table.Use the calendar selection box to adjust the date bucket in which you need to dispatch the order.For orders producing and SG014, the work centers TURNING2 and TURNING9 can be used as alternative work centers.For orders producing SG013, the work centers ASSPKG and ASSPKG9 can be used as alternative work centers. | The available capacity (XX H) for each day displays in the time bucket table. |  |
| 8 | Check Strategy | Choose Set Strategy in the upper right corner of the left panel. You can check relevant settings here and adjust if necessary.Planning ModeScheduling ControlDirectionIn this case, we choose the Bucket mode as an example. | There are two planning modes:Bucket: Allocate orders to first available timeslot.Sequence: Define an exact time for the order to start/end (depending on the planning direction). |  |
| 9 | Check Order Information | Under Sourcing & Scheduling section, on the right panel, choose the tab page Additional Information to check detailed order information. |  |  |
| 10 | Check Source of Supply | Under Available Sources of Supply in the bucket table, relevant production version displays. Check the production version marked as Assign. If you want to adopt some other production version instead, you can check the relevant line in the Assign column. |  |  |
| 11 | Choose Available Time Bucket | In the bucket table, choose the radio button before the available capacity (XX H) you want to assign. You may view the available capacity (XX H) by Day, Week or Shift, as well as select the date range. |  |  |
| 12 | Dispatch and Review the Dispatched Orders | Choose Dispatch.Mark the radio button in front of the available capacity once again.Choose Review Dispatched Orders to review the dispatched orders. | A message displays: Dispatch of Order XXXX Operation XXXX scheduled from XXX to XXX was successful. |  |
| 13 | Cancel Dispatch (Optional) | If you need to cancel the dispatch process, select the corresponding operation and choose Deallocate. | The Status becomes Not Dispatched. |  |
| 14 | Realign Schedules (Optional) | If you need to realign the schedule, select corresponding items and choose Realign Schedules.Note Realigning the schedule is only available on the overview screen. Choose back to return to this screen from the details view.Enter the off-set number of days and time, choose Realign (choose Save and Realign if you want to set the day and time as default). | A message Realign Schedules executed appears. For details, see Message Manager.You could choose Insert Operation for Future or Past. The offset threshold for Past is defined in App Settings > Past Threshold (Maximum of 30 days). |  |
| 15 | Choose Save | Choose Save at the bottom of the left panel. |  |  |

Result

The planned orders are rescheduled according to the available timeslot you choose.

###### Review Work Center Schedules

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step allows the production planner to monitor schedule status by the visualization of Gantt chart.

Procedure

| Procedure Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Capacity Scheduling Board (F3951). |  |  |
| 3 | Filter | Choose Adapt Filters. Flag the entry Work Center Group and choose OK.Choose the following entries as filters and choose Go.Evaluation Horizon: for example, next 1 monthProduct:SG013Status: Not Dispatched and Dispatched |  |  |
| 4 | Monitor Status | Monitor the schedule status in dashboard.View detailed information by selecting the color-bar and choosing Operation Info. |  |  |
| 5 | Reschedule the Operation | Hover over a bar (operation) to display the order information tooltip.Click on a bar and choose Manage Operation.Move the operation by dragging and dropping the bar within the same production version or across different production versions on the Manage Operation page. | The following messages are displayed:Order XXX saved successfully. Order XXX Operation XXX is rescheduled successfully from XXX to XXX.Note You can only drag and drop bars to reschedule bottleneck operations.A single bar (operation) can be dropped across different production versions. Multiple bars (operations) that are selected at one time can only be dropped in the assigned production version and the order is rescheduled accordingly in the same production version. |  |
| 6 | Save Gantt Chart Settings (Optional) | On the Capacity Scheduling Board screen, you can personalize your Gantt chart settings and save the view.Display Work Center GroupsIn the upper left corner, expand the dropdown box, and you can choose to display Pacemaker Work Centers or All Work Centers. Choose the Settings icon on the left, select Work Center Group, and choose OK. The work center groups are displayed on the left.Display Order ID and Product IDIn the upper right corner, choose the Zoom In or Zoom Out icon to adjust the scale of the Gantt chart. Choose the Settings icon on the right to adjust the Gantt chart settings, select Order ID and Product ID. Choose OK. The order ID and product ID are now displayed on the bar.Save Your Personalized ViewAfter configuring your personalized settings, you can save the view by choosing the arrow icon next to the Standard view under the Evaluation Horizon. Choose Save As. Name your view and choose Save. | Your personalized Gantt chart settings are saved as a new view.On the Manage Operation page, the changes to the zoom value and the Gantt chart settings will be reflected on the Capacity Scheduling Board screen.On the Order Details page, only the changes to the Gantt chart settings will be reflected on the Capacity Scheduling Board screen. |  |

##### Pick Components for Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to pick the released production order.

Prerequisite

Ensure that sufficient material is present on stock for RM017 and RM018. To check the stock, you can use the warehouse user and the app Display Stock Overview (MMBE).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Pick Components for Production Orders (CO27). |  |  |
| 3 | Enter Relevant Search Criteria | Make the following entries and choose Execute.Profile: 000002Production Order: <Your Production Order number> | The Order Information System: Detail List of Components screen displays. |  |
| 4 | Picking | Select the relevant reservations and choose Picking. |  |  |
| 5 | Post | Choose Post to post the goods movements. | The goods movements have been posted. |  |

##### Confirm Production Operation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents contains the processing status of orders, operations, sub-operations, and individual capacities. It is an instrument for controlling orders. This process step shows you how to uses time event confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). |  |  |
| 3 | Enter Production Order and Operation | On the Enter Order and Operation screen, make the following entries and choose Go:Order: <Your Production Order number>Operation: 0010 |  |  |
| 4 | Enter Fields in Quantities Section | In the Quantities section, make the following entries:Yield: <enter the amount you want to Confirm>Scrap: <enter the amount you want to Scrap> |  |  |
| 5 | Check Material Movements (only for Operation 0050) | In the Material Movements section, check the material list. | For Operation 0050, SG014 would list here. |  |
| 6 | Enter Fields in Activities Section | In the Activities section, make the following entries:Setup: <enter the setup time you want to confirm for this operation>Machine: <enter the machine time you want to confirm for this operation>Labor: <enter the labor time you want to confirm for this operation> |  |  |
| 7 | Save Your Entries | Choose Post and Complete to make final confirmation for this operation. |  |  |
| 8 | Repeat Steps | Go back and repeat steps 3 to 7 from operation number 0020 to 0050, save your entries. |  |  |

Result

The last operation will trigger automatic GR posting when confirming the operation. Kanban container status will be set to full again.

### Production Order Execution

#### Convert Planned Order to Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to convert planned order to production order.

Prerequisite

Requirement planning is carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments (F2101A) screen displays. |  |
| 3 | Select Criteria | In the Search bar, enter FG011 and choose GO. | Stock Availability situation of all materials starting with FG011 will be displayed. |  |
| 4 | Selection of Materials | Use the Check box and select the row which has Material No as FG011 and click on Manage Materials present at the right side corner of the screen. | The Material and Material Details sub screens display.Stock/Requirement list for the selected material is displayed. |  |
| 5 | Convert Planned Order to Production Order | For the planned order (PldOrd XXXX) noted in previous section, select Convert from Edit dropdown list in the Action column.In the Convert Planned Order XXXX dialog box, choose Convert to Production Order radio button, confirm End Date and Quantity. Choose OK. | The production order is created. Note the Production Order number. |  |
| 6 | End of process step | Click back button twice to come out of this Fiori app and to go back to home screen. | Exited the Fiori app: Monitor Material Coverage - Net / Individual Segments (F2101A) |  |

#### Review Production Order (Optional)

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
| 3 | Check Default Area of Responsibility (Supervisor) | Choose the user icon and choose App Settings. Choose tab Production Supervisors.In the AOR Status column, choose the button to assign or unassign entries, and make sure only the following entries are assigned:Plant 1 AE 3310MTS DI- Valuated (YB1)Choose Back.Choose OK again to come back to Manage Production Orders screen | The Manage Production Order screen displays. |  |
| 4 | Select Production Order | On the Manage Production Orders (F2336) screen, make the following entries and choose Go. If needed, you can adjust filter options through Adapt Filters.Status: CreatedMaterial: FG011Production Plant: 3310 | The Material and Production Plant fields are added to the filter bar.The searched order displays. |  |
| 5 | Check details of Production Order | Select the production order to be reviewed (which we have created in the previous step). If there are issues for the selected production order, the issues will be shown under the Issues column.Choose Edit in the top right corner. | The Production Order Change: Header screen is displayed.Details of the selected production order are displayed. |  |
| 6 | Check PRT (Optional) | If Production Resources/Tools (PRTs) are assigned to the production order, you can check PRT details within this app.Select the order, and choose Order Schedule facet. Choose Settings for the Operations part, and make sure PRTs is selected in the View Settings. PRT hyperlink is available for the operations. |  |  |
| 7 | Check Long Text Copied from Planned Order (Optional) | If any long text is maintained for the planned order, you can check it in the converted production order.Select the order and choose Edit Order in the upper right corner.On the Production Order Change screen, choose tab Long Text, and check the text. | The long text maintained in the planned order is copied to the converted production order. |  |
| 8 | Schedule, cost and availability check functions on Production Order | On the Production Order Change: Header screen, click Schedule Order > Cost Order > Material. | For Schedule Order, the Scheduling is carried out (see log) message is displayed.Upon click of Cost Order, system should give a message that Costing is carried out (see log).Upon click of Material, if all component materials are available, system should give a message that All checked materials in order xxxx are availableIf there are missing components, system displays the Availability Check screen that lets you know that there are missing components. If material RM012 is mentioned in missing parts, then perform staging mentioned in next section. |  |
| 9 | Save the Production Order | Click Save. | System gives a message Order number XXXX saved. |  |

#### Material Staging for Production Order

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
| 3 | Enter Details | Make the following entries and choose Execute.In the Staging Types section:SLoc Level: <select>Plant:3310Selection Horizon for Reqmts: <date must be in the future - after scheduled start date>On the Production/Process Orders tab:Order: <Production Order Number for FG011> | The Pull List: Storage Location Level screen displays. |  |
| 4 | Choose Replenishment Elements | In the Total Reqmts table, select the line items and choose Replenishment Proposal on the top of the screen.Review staged quantities and choose Replenishment Elements. |  |  |
| 5 | Enter Replenishment Storage Location | At the bottom half of the split screen, in the RepLoc column of the Replen. Element table, enter 331C for staged materials. |  |  |
| 6 | Stage and Save | Choose Stage and choose Save.Note Missing materials are transferred to the shop floor from the designated storage area.The shortage of raw material for final assembly production order is supplied with this step. | Material is staged for final assembly. |  |

#### Set Available Kanban to EMPTY

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you set an available Kanban to EMPTY to trigger a reservation for material RM012.

Prerequisite

The Kanban control cycle for material RM012 is created and sufficient stock is available of material RM012 in storage location 331C.

Procedure

It is possible to change status of Kanban Container with various Fiori apps. You can choose one of them to execute the task in this step (set to EMPTY) and subsequent steps (for example, set to FULL) where applicable. Here we provide two options you can leverage, and you can choose either of them.

Option 1:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Set Kanban Container Status (F3717). |  |  |
| 3 | Select the Kanban | Select a Kanban container on the left part of the screen. Choose Value Help icon to open Select: Barcode window. Choose Show Filters to make following entries and press Enter.Plant: 3310Production Supply Area: KANBAN_03From the Items list, choose one of the Kanban for RM012 with Current Status of either WAIT or FULL. | The Kanban you entered displays. |  |
| 4 | Check Kanban Information | On the right part of the screen, check the following entry:Target Status: EMPTY |  |  |
| 5 | Set the Kanban to Empty | On the left part of the screen, choose Save at the bottom. | Setting an available KANBAN to empty results in a reservation for the material. |  |

Option 2:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Kanban Board (F4630).Note You can find the app under category Production Control - Kanban Monitoring. |  |  |
| 3 | Search | Make following entries and choose Go:Plant: 3310Production Supply Area: KANBAN_03Material: RM012 |  |  |
| 4 | Select Kanban Container | In the Control Cycle, choose Kanban Container with WAIT or FULL status. You can check the legend for description of visual elements.Container Details panel displays on the right side.You can check detailed information. |  |  |
| 5 | Set the Kanban to Empty | Choose Set to EMPTY above the list. |  |  |

#### Set Available Kanban to FULL

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you change the status of the Kanban you processed in the previous step to FULL. This will be done when the material is delivered.

Prerequisite

The status of the Kanban is previously set to EMPTY.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Set Kanban Container Status (F3717). |  |  |
| 3 | Select the Kanban | Select a Kanban container on the left part of the screen. Choose Value Help icon to open Select: Barcode window. Choose Show Filters to make the following entries and press Enter.Plant: 3310Production Supply Area: KANBAN_03From the Items list, choose one of the Kanban for RM012 with Current Status: EMPTY. | The Kanban you entered displays. |  |
| 4 | Check Kanban Information | On the right part of the screen, check the following entry:Target Status: FULL |  |  |
| 5 | Set the Kanban to Full | On the left part of the screen, choose Save at the bottom. |  |  |

#### Release Production Order

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
| 3 | Select the Production Order. | On the Manage Production Orders screen, choose Adapt Filters to display more filter options. In the Adapt Filters dialog box, choose More filters. Select Material and Production Plant and choose OK.Enter the following filter criteria, and choose Go:Status: CreatedMaterial: FG011Production Plant: 3310 | The Material and Production Plant fields are added to filter bar.The searched order displays. |  |
| 4 | Check details of Production Order | Select the Production Order to be released.Choose Release in the top right corner. | The Release carried out message displays and the order is released.If Release Order dialog box displays with message Non-Availability of Material, it means there is not sufficient stock stored for FG011‘s components.You can either choose Release Order in the dialog box to release order directly. Or you can choose to go back to the Create Initial Material Stock preliminary step to post more initial material stock. When enough material stock is posted, complete production order processing for finished goods, and then release production order for final assembly. |  |

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
| 5 | Post | Choose Post to post the goods movements. | The goods movements are posted. |  |

#### Confirm Production Operations of Production Order

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
| 4 | Enter Quantities Data | In the Quantities section, make the following entries:Yield: <yield amount>Scrap: <scrap amount>Note System automatically populates the values in the above fields. |  |  |
| 5 | Check Material Movements | In the Material Movements section, check the material list. | The system displays an overview table of all materials for which the withdrawing is automatically done with the confirmation of the operation.If there are not any materials set for backflush (in material master), then no materials display in the table. |  |
| 6 | Enter Activities Data | In the Activities section, make the following entries:Setup: <setup time>Machine: <machine time>Labor: <labor time>Note System automatically populates the values in the above fields. |  |  |
| 7 | Save Your Entries | For partial confirmation, choose Post.For final confirmation, choose Post and Complete. | Confirmation is made. |  |
| 8 | Repeat Steps | Go back and repeat steps 3 to 7 for Operation <0020> and <0030>. | The final confirmation for the Production Order is made for all operations. |  |

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
| 3 | Select Production Order | On the Manage Production Operations screen, choose Adapt Filters to display more filter options.In the Adapt Filters dialog box, select Material and Production Plant and choose OK.Enter the following filters criteria and choose Go.Material: FG011Plant: 3310 | The Material and Plant fields are then added to filter bar.Selected order displays.Operations of production order must be in status Confirmed. |  |

#### Post Goods Receipt for Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods receipt for production order of final assembly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Enter Goods Receipt Order | Choose Goods Receipt > Order in the header area and make the following entries:Order: <production order number for finished goods>GR goods receipt: <101>Document date: <default>Posting date: <default>On the General tab, next to the Printer icon, select Print via Output Control (mouseover) checkbox, and choose Individual Slip. |  |  |
| 4 | Enter Quantity | On the Quantity tab, confirm production order quantities.On the Where tab, enter the following entry:Storage Location: <331A (Std. storage 1)>On the Serial Numbers tab, select all the serials numbers for the yield quantities except the scrap ones. |  |  |
| 5 | Set Item OK and Post | Select the Item OK checkbox and choose Post. | The system displays the message Material document 500xxxxxxx posted. |  |

#### Evaluate Stock/Requirements Situation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock/requirements situation for FG011.

Prerequisite

Goods Receipt for Production Order is completed in the previous steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments (F2101A) screen displays. |  |
| 3 | Select Material | In the field Material, enter material FG011 and choose GO. |  |  |
| 4 | Selection of materials | Use the Check box and select the rows which have the Material No FG011 and click Manage Materials. | The Material and Material Details subscreens display.Stock/Requirement list for all the selected materials is displayed. |  |
| 5 | Check the stock situation | The Screen Stock/Requirements list should show the updated stock quantity.Stock information appears as first row in the table present in this screen. Stock quantity is displayed under columns Quantity, Available. | Updated Stock Quantity is displayed. Stock quantity is increased by the amount of quantity posted as goods receipt for Production Order. |  |

### Customer Order Creation And Outbound Delivery creation

#### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order for material FG011.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873) . | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On Manage Sales Orders screen, select Create Sales Order - VA01. |  |  |
| 4 | Enter the Order type OR (Standard Order) | On the Create Sales Documents screen, make the following entries and choose Enter:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries:Sold To party: 33100001Ship To party: 33100001Cust. Reference: <Reference number> Enter a customer purchase order number as referenceCust.Ref.Date: for example, <today>Requested Delivery Date: Current date plus 8 working daysNote If a popup appears for example after changing the Delivery Date, choose Enter and accept it.Material Number: FG011.Order Quantity: <Quantity> For example, <02 PC>Plant: 3310Once the above data is entered, go into the details of sales order line item. To go to the details of the sales order line item, either double click on the sales order line item or select the line item and click on the Display Item details icon. |  |  |
| 6 | Enter storage location data in sales order line item | On the Create Standard Order: Item Data screen, click the Shipping tab.Enter data in following fields:Storage Location:331AClick the Back button | System accepts storage location details entered by user. |  |
| 7 | Perform Availability check | Select the line item of sales order and click on the Check Item Availability icon.Results of availability check should be displayed in the Review Availability Check Result screen. | Screen Review Availability Check Result appears.Confirmed Delivery date appears under column confirmed Del. Date.Confirmed Quantity appears under column Confirmed Quantity.If you are OK with the results, click on Apply. This should take you back to the Create Standard Order: Overview screen.If you want to know the details of Availability check, then click online item and system should take you the screen: Standard Order: Availability Control where you should see the details of availability check. |  |
| 8 | Save Document | Choose Save. Make a note of the sales order number.Note If the customer is related to Legal Control for International Business and Intrastat Declaration for business within the European Union, a pop up message appears saying “Item XX is blocked by Legal Control (International Trade)”. Choose Enter and accept it. | The order is saved and sales order number is displayed at the bottom of screen.System gives a message: Standard Order XXXX has been saved. |  |

|  |
| --- |
| Note If you want to check the SAP Watch List Screening, please follow scope item 1WE. If you would test it in the context of PSSP, please manually change the address of the customer of your sales order to an address, that would create a hit in WLS and follow the steps from 1WE. |

#### Create Delivery with Order Reference

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the delivery document with reference to sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as aShipping Specialist . |  |  |
| 2. | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries screen displays. |  |
| 3. | Search Sales Order | Make the following entries and choose Go:Shipping point: 3310Planned Creation Date: <input the date range>SD Document: Sales order number created previously |  |  |
| 4. | Create Delivery | Select your sales order items and choose Create Deliveries. | Creation of a delivery is triggered. |  |
| 5. | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays, delivery is created successfully with delivery number shown on tab Deliveries.Make a note of the delivery number. | Make a note of the delivery number. |
| 6. | Check Inspection Lot Number | Click on the delivery number. In the pop-up screen, click the delivery number again. | Screen Outbound Delivery displayed. |  |
| 7. | Check Inspection Lot number | In Screen Outbound Delivery, click on tab Items. In tab Items, click on > to go into details of line item. System displays screen: Outbound Delivery Item. In screen Outbound Delivery Item, in tab General Information, note down the inspection lot number assigned to field Inspection Lot. | Inspection lot number noted. |  |

#### Maintain Serial Numbers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to maintain serial number to the material.

Prerequisites

Run this step if Serial Number is used in product master, such as FG011.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as aShipping Specialist. |  |  |
| 2. | Access the SAP Fiori App | Open Manage Outbound Deliveries (F0867A). | The Manage Outbound Deliveries (F0867A) screen displays. |  |
| 3. | Selection Criteria | Make the following entries and choose Go.Shipping point: 3310Overall Status: Ready for Picking | List of outbound deliveries displayed on the screen as per selection criteria. |  |
| 4. | Select Outbound Delivery for maintaining serial number | Select the outbound delivery created in previous step and click on Pick. | Screen Pick Outbound Delivery is displayed. |  |
| 5. | Select delivery line item for maintaining serial numbers | Select delivery line item and click on Serial number status.Note: Serial number status is in Red Color. | Screen Delivery Item XXXX is displayed. |  |
| 6. | Maintain Serial numbers | Screen: Delivery item X of XIn the table Serial Numbers, take the value help and provide the serial numbers. Or refer to the serial numbers noted in previous steps and key in the serial number values. Select the serial number and after this click Apply. | Serial number maintained in delivery line item and screen Pick Outbound Delivery is displayed. |  |
| 7 | Save Serial numbers in Outbound Delivery document | Choose Save. | Delivery is saved and status of Serial number Status is changed to green. |  |

#### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. It shows you how to execute picking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as aShipping Specialist. |  |  |
| 2. | Access the SAP Fiori App | Open Manage Outbound Deliveries (F0867A). | The Manage Outbound Deliveries (F0867A) screen displays. |  |
| 3 | Selection Criteria | Make the following entries and choose Go.Shipping point: 3310Overall Status: Ready for Picking | List of outbound deliveries displayed on the screen as per selection criteria. |  |
| 4. | Select Outbound Delivery for picking | Select the outbound delivery created in previous step and click on Pick. | Screen Pick Outbound Delivery is displayed. |  |
| 5. | Enter Picked Quantity | Enter Picked quantity in field Picking Quantity.Picked Quantity must be equal to delivery Qtyand hit Enter. | Entered picked quantity is accepted by system. |  |
| 6 | Save | Choose Save. | The delivery has been saved with picked quantity. |  |

### Quality inspection in Outbound Delivery

#### Display Quality Technician Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This optional process step shows you how to display the open inspection lot list via the overview page for quality technicians.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Quality Technician Overview (F2361). | The Quality Technician Overview screen displays.You can get an overview of the inspection lots with open results recording and navigate directly to the Record Inspection Results App. Additionally, you can check the inspection lots without an inspection plan. |  |

#### Display Open Inspection Lots (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This optional process step shows you how to display the open inspection lot list via the Manage Inspection Lots app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Inspection Lots without Usage decision (QVM3). | The Inspection Lots without Usage Decision screen displays. |  |
| 3 | Enter Filter FIelds | In screen Inspection Lots without Usage Decision, make the following entries and choose Execute:Lot created: Ensure correct valid to date (for example: 10 days in future as the valid to date)Plant: 3310Insp. Lot Origin: 10Material: FG011 | Screen Inspection Lots without Usage Decision is displayed.Inspection lots without usage decision are displayed as per the selection criteria. |  |
| 4 | Select Inspection Lot | In the inspection lot list, click the inspection lot that was created before. | Screen Display Inspection lot is displayed. |  |
| 5 | Check Inspection Lot | Under tab Data for Lot Origin, in section Data for goods issue, verify the referenced sales order number and delivery number. | The sales order number, delivery number from which the inspection lot originates is displayed. |  |

#### Record Inspection Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to record the inspection results.

Procedure

Record Inspection Results for one Inspection Lot

If inspection results shall be recorded for one or only a few inspection lots, execute the following process flow:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A). | The Record Inspection Results (F1685A) screen displays. |  |
| 3 | Enter Filter Fields | Make the following entry and choose Go.Delivery: Obtained from previous step | If Delivery is not displayed in the Filters, choose Adapt Filters. On the pop-up screen Filters, find Sales and Distribution and choose More Filters. Select Delivery and choose OK. Choose Go |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the corresponding inspection lot for the delivery created in a previous step. |  |  |
| 5 | Choose Record Results | Choose Record Multiple Results at the top right. |  |  |

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Approve Purchase Orders: the note says only POs with a value higher than 500.00 AED are released, while the expected result says a net value of 500 AED or more has status In Approval, so the boundary at exactly 500 AED is ambiguous.

> [!warning] Conflict
> Flagged while digesting this document, not verified: The Overview Table lists Record Inspection Results (F1685A) for the repetitive-manufacturing inspection step and Production Operator - Lean Manufacturing with Display Kanbans: Demand View (PK13N) for Create Event-Driven Kanban, but the procedures use Record Inspection Results - Hierarchical Worklist (QE51N) and Production Planner - Lean Manufacturing with Kanban Board (F4630).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Create Outbound Delivery (subcontracting) names components provided as RM33 and RM34, whereas the master data and the surrounding steps use RM023, RM024, RM025 and RM026.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/test-script-produce-and-sell-standard-products-inventory-management-54-part-02]]
- related-to :: [[08-sales-order-management/customer-returns-management-consumer-products-61v-ae-test-script-sap-s]]
- related-to :: [[12-production-and-manufacturing/produce-and-sell-standard-products-warehouse-managed-54v-ae-test-scrip]]
- related-to :: [[12-production-and-manufacturing/production-capacity-evaluation-and-leveling-consumer-products-5oi-ae-t]]
- related-to :: [[10-procurement/test-script-procurement-of-production-components-consumer-products-5w3]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/54U_S4CLD2608_BPD_EN_AE.docx` — lines 1–3191 of the extracted text · extracted with `mammoth` · 280,122 chars in the whole document
