---
id: 12-production-and-manufacturing/test-script-lot-size-of-one-with-advanced-variant-configuration-55e-ae
title: "Test Script: Lot Size of One with Advanced Variant Configuration (55E_AE) (55E_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 55E (AE): make-to-order robot with advanced variant configuration, from inquiry to payments."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/variant-configured-production]
aliases: [55E_S4CLD2608_BPD_EN_AE]
keywords: [Production of Variant-Configured Products, lot size of one, advanced variant configuration, make-to-order production, test scripts, sales inquiry and quotation, material requirements planning, component procurement, stock transport orders, production orders]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/55E_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1068
topic: 12-production-and-manufacturing/variant-configured-production
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Lot Size of One with Advanced Variant Configuration (55E_AE) (55E_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/55E_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Production of Variant-Configured Products** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Lot Size of One with Advanced Variant Configuration (55E_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232855986)

[2 Prerequisites 5](#_Toc232855987)

[2.1 System Access 5](#_Toc232855988)

[2.2 Roles 5](#_Toc232855989)

[2.3 Master Data, Organizational Data, and Other Data 7](#_Toc232855990)

[2.4 Additional Manual Configuration 14](#_Toc232855991)

[2.5 Business Conditions 15](#_Toc232855992)

[2.6 Preliminary Steps 15](#_Toc232855993)

[2.6.1 Create Purchasing Info Record 15](#_Toc232855994)

[2.6.2 Change Configuration Profile to Assign Characteristic Group 17](#_Toc232855995)

[2.6.3 Create Initial Material Stock 18](#_Toc232855996)

[2.6.4 Creating Stock in Supplying Plant 19](#_Toc232855997)

[2.6.5 Optional: Configure Flexible Workflow for Stock Transport Order 20](#_Toc232855998)

[2.6.5.1 Optional: Check Flexible Workflow for Stock Transport Order Approval 20](#_Toc232855999)

[2.6.5.2 Configure Flexible Workflow for Stock Transport Order 22](#_Toc232856000)

[2.6.6 Edit User-Specific Parameters for Supplier Invoices (Optional) 23](#_Toc232856001)

[2.6.7 Create Condition Records (Optional) 24](#_Toc232856002)

[2.6.8 Change Inspection Plan for Configurable product 24](#_Toc232856003)

[3 Overview Table 26](#_Toc232856004)

[4 Test Procedures 31](#_Toc232856005)

[4.1 Customer Sales Order and MRP 31](#_Toc232856006)

[4.1.1 Create Sales Inquiry 31](#_Toc232856007)

[4.1.2 Create Sales Quotation for Configurable Material 32](#_Toc232856008)

[4.1.3 Create Sales Order with Reference to Sales Quotation 34](#_Toc232856009)

[4.1.4 Material Requirements Planning at Plant Level 36](#_Toc232856010)

[4.1.5 Evaluate Stock/Requirements Situation 38](#_Toc232856011)

[4.2 Procurement of Components 40](#_Toc232856012)

[4.2.1 Convert Purchase Requisitions to Purchase Orders 40](#_Toc232856013)

[4.2.2 Preview Purchase Order (Optional) 42](#_Toc232856014)

[4.2.3 Create Inbound Deliveries 43](#_Toc232856015)

[4.2.4 Post Goods Receipt for Inbound Delivery 44](#_Toc232856016)

[4.2.5 Check Range of Stock Coverage 45](#_Toc232856017)

[4.3 Intracompany Stock Transfer 47](#_Toc232856018)

[4.3.1 Evaluate Stock/Requirements Situation 47](#_Toc232856019)

[4.3.2 Process Stock Transport Requisition (with MRP) 48](#_Toc232856020)

[4.3.3 Change Stock Transport Order (with MRP) 49](#_Toc232856021)

[4.3.4 Optional: Approve Stock Transport Order 50](#_Toc232856022)

[4.3.5 Optional: Check Stock Transport Order Approval Details 51](#_Toc232856023)

[4.4 Production of Subassembly in Issuing Plant 52](#_Toc232856024)

[4.4.1 Convert Planned Orders to Production Orders for Subassembly 52](#_Toc232856025)

[4.4.2 Review Production Order (Optional) 53](#_Toc232856026)

[4.4.3 Release Production Order 55](#_Toc232856027)

[4.4.4 Confirm Production Operations for Assembly 56](#_Toc232856028)

[4.4.5 Post Goods Receipt for Assembly Production Order 57](#_Toc232856029)

[4.4.6 Evaluating Stock/Requirements Situation (Optional) 58](#_Toc232856030)

[4.4.7 Create Replenishment Delivery for Stock Transport Order 59](#_Toc232856031)

[4.4.8 Optional: Create Pro Forma F8 Invoice 60](#_Toc232856032)

[4.4.9 Pick and Post Goods Issue for Stock Transport Order 61](#_Toc232856033)

[4.4.10 Check Status of Stock Transfer 62](#_Toc232856034)

[4.4.11 Confirm Quantities for Putaway 63](#_Toc232856035)

[4.4.12 Post Goods Receipt for Inbound Delivery 64](#_Toc232856036)

[4.5 Production Order Execution for Subassembly 65](#_Toc232856037)

[4.5.1 Convert Planned Orders to Production Orders for Subassembly 65](#_Toc232856038)

[4.5.2 Review Production Order (Optional) 66](#_Toc232856039)

[4.5.3 Execute Material Staging for Subassembly 68](#_Toc232856040)

[4.5.4 Release Production Order 69](#_Toc232856041)

[4.5.5 Confirm Production Operations for Subassembly 71](#_Toc232856042)

[4.5.6 Post Goods Receipt for Subassembly Production Order 72](#_Toc232856043)

[4.5.7 Review Production Order 73](#_Toc232856044)

[4.5.8 Evaluating Stock/Requirements Situation (Optional) 75](#_Toc232856045)

[4.6 Production Order Execution for Final Assembly 76](#_Toc232856046)

[4.6.1 Convert Planned Orders to Production Orders for Final Assembly 76](#_Toc232856047)

[4.6.2 Review Production Order (Optional) 77](#_Toc232856048)

[4.6.3 Release Production Order 79](#_Toc232856049)

[4.6.4 Confirm Production Operations for Final Assembly 80](#_Toc232856050)

[4.6.5 Post Goods Issue for Final Assembly Production Order Components 81](#_Toc232856051)

[4.6.6 Post Goods Receipt for Final Assembly Production Order 83](#_Toc232856052)

[4.6.7 Evaluating Stock/Requirements Situation (Optional) 84](#_Toc232856053)

[4.7 Quality Inspection during Goods Receipt from Production 85](#_Toc232856054)

[4.7.1 Display Inspection Plan 85](#_Toc232856055)

[4.7.2 Display Quality Technician Overview (Optional) 86](#_Toc232856056)

[4.7.3 Display Open Inspection Lots 87](#_Toc232856057)

[4.7.4 Display Inspection Methods 88](#_Toc232856058)

[4.7.5 Record Inspection Results 89](#_Toc232856059)

[4.7.6 Display Quality Engineer Overview (Optional) 91](#_Toc232856060)

[4.7.7 Make Usage Decision 92](#_Toc232856061)

[4.7.8 Display Material Stock after Usage Decision 93](#_Toc232856062)

[4.8 Outbound Delivery Processing 94](#_Toc232856063)

[4.8.1 Create Delivery 94](#_Toc232856064)

[4.8.2 Execute Picking 96](#_Toc232856065)

[4.8.3 Maintain Serial Numbers 97](#_Toc232856066)

[4.8.4 Post Goods Issue 98](#_Toc232856067)

[4.9 Accounts Receivable 100](#_Toc232856068)

[4.9.1 Create Billing Document 100](#_Toc232856069)

[4.9.2 Post Incoming Payments 102](#_Toc232856070)

[4.10 Accounts Payable 104](#_Toc232856071)

[4.10.1 Create Supplier Invoice 104](#_Toc232856072)

[4.10.2 Post Outgoing Payment 106](#_Toc232856073)

[5 Appendix 108](#_Toc232856074)

[5.1 Preceding Processes 108](#_Toc232856075)

[5.2 Succeeding Processes 108](#_Toc232856076)

## Purpose

Overview

This scope item focuses on a Make-to-Order scenario (Lot Size of One) that integrates with production planning and execution, procurement, inquiry, quotation, sales, and logistics execution up to invoicing and incoming and outgoing payments, covering multilevel configurable materials. The configurable material is defined as a bill of material.

In this process, the storyline starts with an inquiry for a robot, proceeding to a quotation and on confirmation a sales order is created with an individual configuration. This is captured by defining the different component characteristics desired by the customers and considering the constraints and dependencies of the components. The sales price calculation is then based on the individually chosen characteristics of the components. The sales order is considered for production planning when doing the materials requirements planning (MRP). Configured subassemblies are procured externally based on the procurement proposal generated during MRP. Another configured subassembly is transferred to production plant from another plant belonging to the same company code. Special procurement indicators are used to define stock transfer locations.

Stock is placed in special sales order stock at all times and serialized (as of level subassembly). By serializing stock throughout the process, this allows customers to gain transparency for items that are built in the configured finished good.

The production execution for the individual robot takes place after one subassembly is procured externally (including configuration information), while another subassembly is internally produced. The finished good (robot) is subject to quality inspection at the end of production.

Once production is complete, the goods are delivered to the customer and invoiced. The process finishes with posting of incoming payments from the customer as well as outgoing payments to the vendor for purchased subassemblies.

Related SCN Blog for material BOM graphical representation:

- [Understanding variations in Lot Size of One (LS1) E2E scenario](https://blogs.sap.com/2023/11/29/understanding-variations-in-lot-size-of-one-ls1-e2e-scenario/)

Related SCN Blog for E2E process flow of 55E:

- [Working with E2E Lot Size of One (CTO scenario) with Advanced Variant Configuration | Scope Item '55E'](https://blogs.sap.com/2022/08/07/customer-engagement-for-lot-size-of-one-mto-scenario-with-advanced-variant-configuration-scope-item-55e/)
- [Insights into Lot Size-of-One End to End Scenario (55E) based on Configure to Order / Make to Order](https://community.sap.com/t5/enterprise-resource-planning-blogs-by-sap/insights-into-lot-size-of-one-end-to-end-scenario-55e-based-on-configure-to/ba-p/13577406)

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
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC | PURCHASER |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC | PURCHASING_MANAGER |
| Material Planner - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC | Material Planning - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC | MATL_PLNR_EXT_PROC |
| Product Configuration Modeler | SAP_BR_PRODUCT_CONFIG_MODELER | Variant Configuration | SAP_BR_PRODUCT_CONFIG_MODELER | PRODUCT_CONFIG_MODELER |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK | WAREHOUSE_CLERK |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT | AR_ACCOUNTANT |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT | AP_ACCOUNTANT |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR | PRODN_PLNR |
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | PRODN_SUPERVISOR_DISC |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | PRODN_OPTR_DISC |
| Quality Technician | SAP_BR_QUALITY_TECHNICIAN | Quality Inspection | SAP_BR_QUALITY_TECHNICIAN | QUALITY_TECHNICIAN |
| Quality Engineer | SAP_BR_QUALITY_ENGINEER | Quality Engineering | SAP_BR_QUALITY_ENGINEER | QUALITY_ENGINEER |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC | INTERNAL_SALES_REP |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST | SHIPPING_SPECIALIST |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK | BILLING_CLERK |
|  |  | Billing |  | BILLING_CLERK |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST | RECEIVING_SPECIALIST |
| Quality Planner | SAP_BR_QUALITY_PLANNER | Quality Planning | SAP_BR_QUALITY_PLANNER | QUALITY_PLANNER |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT | BPC_EXPERT |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER | INVENTORY_MANAGER |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

Material Master Data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | AVC_E2E_ROBOT | Robot Multi-Level | Configurable Material |
| Material | AVC_E2E_LINK_ARM | Link Arm (Configurable) | Configurable Material |
| Material | AVC_E2E_CONTROL | Control Unit (Configurable) | Configurable Material |
| Material | AVC_E2E_DRIVE_ARM | Drive Arm (Configurable) | Configurable Material |
| Material | AVC_E2E_BASE_FRAME | Base Frame | Semi-finished Material |
| Material | AVC_E2E_MOTOR_1XX | Motor 1XX | Semi-finished Material |
| Material | AVC_E2E_MOTOR_2XX | Motor 2XX | Semi-finished Material |
| Material | AVC_E2E_D_ARM_50 | Drive Arm Length 50 | Semi-finished Material |
| Material | AVC_E2E_D_ARM_70 | Drive Arm Length 70 | Semi-finished Material |
| Material | AVC_E2E_L_ARM_30 | LINK Arm Length 30 | Semi-finished Material |
| Material | AVC_E2E_L_ARM_45 | LINK Arm Length 45 | Semi-finished Material |
| Material | AVC_E2E_L_ARM_60 | LINK Arm Length 60 | Semi-finished Material |
| Material | AVC_E2E_BRD_PAINT | Painting Unit | Semi-finished Material |
| Material | AVC_E2E_BRD_SEAL | Sealing Unit | Semi-finished Material |
| Material | AVC_E2E_SEALING | Sealing Unit | Trading Good |
| Material | AVC_E2E_PAINTING | Painting Unit | Trading Good |
| Material | AVC_E2E_CNTRL_CAB | Control Cabin | Trading Good |

Organization Data:

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Plant | 3320 | Plant 2 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |
| Storage Location | 332A | Std. storage 1 |  |
| Cost Center | 33101301 | Manufacturing 1 (AE) |  |

CharacteristicsData:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Characteristic | AVC_RBT_MOTOR_GRP | Motor Group |  |
| Characteristic | AVC_RBT_SPEED_GRP | Speed |  |
| Characteristic | AVC_RBT_SPEED_1 | Speed Motor 1 |  |
| Characteristic | AVC_RBT_SPEED_2 | Speed Motor 2 |  |
| Characteristic | AVC_RBT_SPEED_3 | Speed Motor 3 |  |
| Characteristic | AVC_RBT_SPEED_4 | Speed Motor 4 |  |
| Characteristic | AVC_RBT_SPEED_5 | Speed Motor 5 |  |
| Characteristic | AVC_RBT_SPEED_6 | Speed Motor 6 |  |
| Characteristic | AVC_RBT_LEN_DRIVEARM | Length of Drive Arm |  |
| Characteristic | AVC_RBT_LEN_LINKARM | Length of Link Arm |  |
| Characteristic | AVC_RBT_RMAX_REQ | Reach(Maximum) - Requested |  |
| Characteristic | AVC_RBT_RMAX_TECH | Reach(Maximum) -Technical |  |
| Characteristic | AVC_RBT_REGION | Region |  |
| Characteristic | AVC_RBT_RMIN_REQ | Reach (Minimum) - Requested |  |
| Characteristic | AVC_RBT_RMIN_TECH | Reach (Minimum) - Technical |  |
| Characteristic | AVC_RBT_SLA | Service level agreement |  |
| Characteristic | AVC_RBT_TYPE_ARM | Arm Type |  |
| Characteristic | SDCOM_VKOND | Variant condition |  |
| Characteristic | VBPA_WE_LAND1 | Country Key |  |
| Characteristic | AVC_RBT_LEN_ARM | Length of Arm |  |

Class Data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Class | AVC_RBT_SALES | Robot Sales Data | Class of Type 300 |
| Class | AVC_RBT_ROBOT_REQ | Robot Sales Requirement Data | Class of Type 300 |
| Class | AVC_RBT_ROBOT_ENG | Robot Technical Data | Class of Type 300 |
| Class | AVC_RBT_CN_L_ARM | Link Arm | Class of Type 300 |
| Class | AVC_RBT_CONTROL | Control Data | Class of Type 300 |
| Class | AVC_RBT_CN_MOTOR | Motor | Class of Type 200 |

Dependency Data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Dependencies | AVC_RBT_DEF_LEN_ARM_CTO | Set default values for arm len |  |
| Dependencies | AVC_RBT_PRICING_SLA | Pricing SLA |  |
| Dependencies | AVC_RBT_PRICING_REACH_CTO | Pricing Conditions for Robot |  |
| Dependencies | AVC_RBT_PR_CN_MOTOR1 | Set values for class node |  |
| Dependencies | AVC_RBT_PR_CN_MOTOR2 | Set values for class node |  |
| Dependencies | AVC_RBT_PR_CN_MOTOR3 | Set values for class node |  |
| Dependencies | AVC_RBT_PR_CN_MOTOR4 | Set values for class node |  |
| Dependencies | AVC_RBT_PR_CN_MOTOR5 | Set values for class node |  |
| Dependencies | AVC_RBT_PR_CN_MOTOR6 | Set values for class node |  |
| Dependencies | AVC_RBT_SC_PAINT | Select for Painting |  |
| Dependencies | AVC_RBT_SC_SEAL | Select for Sealing |  |

Class Node Data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Class Node | AVC_RBT_CN_ARM (200) |  |  |
| Material | AVC_E2E_D_ARM_50 |  |  |
| Material | AVC_E2E_D_ARM_70 |  |  |
| Material | AVC_E2E_D_ARM_30 |  |  |
| Material | AVC_E2E_D_ARM_45 |  |  |
| Material | AVC_E2E_D_ARM_60 |  |  |
| Class Node | AVC_RBT_CN_MOTOR (200) |  |  |
| Material | AVC_E2E_MOTOR_1XX |  |  |
| Material | AVC_E2E_MOTOR_2XX |  |  |
| Class Node | AVC_RBT_CN_TOOL (200)) |  |  |
| Material | AVC_E2E_PAINTING |  |  |
| Material | AVC_E2E_SEALING |  |  |

Bill of Material Structure

| Material | Level | Material Type | Unit | Characteristics of Material | Component Quantity | Component UOM |
| --- | --- | --- | --- | --- | --- | --- |
| AVC_E2E_ROBOT | 0 | KMAT | PC | Configurable Material for MTO processing with Serial Number. |  |  |
| Tool Class Node | 1 | Class Item |  |  | 1 |  |
| AVC_E2E_BASE_FRAME | 1 | HALB | PC | External procured. | 1 | PC |
| AVC_E2E_LINK_ARM | 1 | KMAT | PC | Configurable Material for MTO processing with Serial Number. | 1 | PC |
| AVC_E2E_CONTROL | 1 | KMAT | PC | External procured with Serial Number. | 1 | PC |
| AVC_E2E_DRIVE_ARM | 1 | KMAT | PC | Configurable Material for Stock Transfere processing with Serial Number. | 1 | PC |

| Material | Level | Material Type | Unit | Characteristics of Material | Component Quantity | Component UOM |
| --- | --- | --- | --- | --- | --- | --- |
| AVC_E2E_LINK_ARM | 0 | KMAT | PC | Configurable Material for MTO processing with Serial Number. |  |  |
| Arm Class Node | 1 | Class Item |  |  | 1 |  |
| Motor | 1 | Class Item |  |  | 1 |  |
| Motor | 1 | Class Item |  |  | 1 |  |
| Motor | 1 | Class Item |  |  | 1 |  |
| Motor | 1 | Class Item |  |  | 1 |  |
| Motor | 1 | Class Item |  |  | 1 |  |
| Motor | 1 | Class Item |  |  | 1 |  |

Work center

Below table mentions the work centers to be used in this scenario. These are standard work centers available as part of best practice and hence it is not needed to create new Work Centers.

| Work Center | Plant | Work Center Category | Work center Description |
| --- | --- | --- | --- |
| ASSEMBLE | 3310 | 0001 | Assembly |
| ASSEMBLY | 3310 | 0001 | Assembly |
| ASSEMBLY | 3320 | 0001 | Assembly |
| PACK01 | 3310 | 0001 | Packing Line 1 |
| TESTING | 3310 | 0001 | Testing |

Suppliers:

Supplier masters (Business Partner) provided as part of standard best practices will be used. No need to create new supplier masters for this E2E scenario. Below mentioned Suppliers (Business Partners) will be used in this scenario.

Suppliers for country – AE:

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Supplier | 33300001 | Domestic AE Supplier 1 |  |
| Supplier | 33413320 | for example New Plant 3320 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |

Customer:

Customer masters (Business Partners) provided as part of standard best practices will be used. No need to create new Customer masters for this E2E scenario. Below mentioned Customers (Business Partners) will be used in this scenario.

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Sold-to Party | 33100001 | Domestic UAE Customer 1 |  |
| Ship-to Party | 33100001 | Domestic UAE Customer 1 |  |
| Payer | 33100001 | Domestic UAE Customer 1 |  |
| Sales Organization | 3310 |  |  |
| Distribution Channel | 10 |  |  |
| Division | 00 |  |  |
| Shipping point | 3310 |  | For AE customers |
| Shipping point | 3320 |  | For AE customers |
| Company code | 3310 |  |  |

Quality Master Inspection Characteristics:

Master Inspection Characteristics that are delivered as part of standard SAP Best Practices for SAP S/4HANA Cloud Public Edition will be used in this scenario and there is NO need to create new one.

Only one Master Inspection Characteristic is used in this scenario and the same is below.

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Master Inspection Characteristic | YQUALI01 | Surface |  |

Quality Inspection Plan:

Quality Inspection Plan uses the standard work center ‘QMLABS’ provided as part of standard best practices.

For more information on creating your own master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) <Indicate master data scripts used as baseline for this specification>

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| 2T7 | Create Product Master of Type "Configurable Material" - MDS - MDS |
| BNF | Create Product Master of type "Trading Good" - MDS - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BND | Create Customer Master - MDS |
| BNQ | Create Quality Inspection Plan - MDS |
| BNE | Create Supplier Master - MDS |
| BHD | Create Purchasing Info Record - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/37c9796f7e9087d3d6df14b5cc50e069)

### Business Conditions

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |
| J58 - Accounting and Financial Close | Execute to create open posting periods. |
| BFA - Basic Bank Account Management | Bank account master data is processed. |
| 22T - Set Up Configurable Model Using Variant Configuration | To simulate configurable materials, the 22T - Set Up Configurable Model Using Variant Configuration scope item must be activated in the system. |
| 4R8 - Engineer-to-Order Production with Variant Configuration | To use configurable materials, the - 4R8 -Engineer-to-Order Production with Variant Configurationscope item must be activated in the system. |
| 1YT - Make-to-Order Production with Variant Configuration | To use configurable materials, the 1YT - Make-to-Order Production with Variant Configurationscope item must be activated in the system. |

### Preliminary Steps

#### Create Purchasing Info Record

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Create Purchasing Info Record (ME11) app. | The Create Info Record: Initial Screen is displayed. |  |
| 3 | Enter Info Record Data | Make the following entries:Supplier: 33300001Material: AVC_E2E_CONTROLPurchasing Organization : 3310Plant: 3310Info category: Standard (Default)Choose Enter. | The Create Info Record: General Data screen is displayed. |  |
| 4 | Enter Purchasing Data | Choose Purch. Org. Data 1 and make the following entries:Pl. Deliv. Time: 2(Default)Purch. Group : 001(Default)Standard Qty: 1Tax Code: <Input Tax Code>​Conf. Control​: ​0004 Inbound Delivery​ ​Note If time dependent tax (TDT) is activated, and fields Country/Region Key for company code, Validity Periods and Tax Code are maintained via SSCUI 101016 in SAP S/4HANA Cloud Public Edition or the configuration activity Define Tax Codes for Sales and Purchases in Central Business Configuration, you must maintain the Tax Rate Valid From field in the New Purchasing Info Record screen. If you enter the current date, this date will be adjusted to a valid start date for your tax code according to the SSCUI/configuration activity settings.If Registration for Indirect Taxation Abroad (RITA) is activated, and tax registration country and tax code are maintained for company code via SSCUI 103464 in SAP S/4HANA Cloud Public Edition or the configuration activity Activate RITA and Maintain Tax Registration Countries in Central Business Configuration, you must maintain the Tax Country field. The default value of this field is the country ID of company code, but you can change it to a valid country ID that is maintained in the SSCUI/configuration activity accordingly.Net Price: 340 | Purchasing Data is added. |  |
| 5 | Save Data | Choose Save. | A purchasing info record is saved. |  |
| 6 | Enter Info Record Data | Repeat steps 3-6 forMaterial:AVC_E2E_BASE_FRAME and AEDNet Price:110 |  |  |

#### Change Configuration Profile to Assign Characteristic Group

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you assign characteristic group to configuration profile.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Product Configuration Modeler. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the VC Modeling Environment (PMEVC) app. | The Initial Screen of Variant Configuration Modeling Environment screen displays. |  |
| 3 | Enter the configuration model data | On the initial screen, make the following entries, and choose Enter Model.Material: AVC_E2E_ROBOTClass Type: 300 (Default)Plant: 3310BOM Application: PP01 | The configuration screen displays. |  |
| 4 | Assign characteristic group to profile | In the Object section, expand the root node and double-click the configuration profile CTO node.The Configuration Profile screen displays in the right pane.Select the Characterstic Groups tab.Choose Assign Characteristic Groups.A dialog box to confirm whether to leave the page with unsaved data might be displayed.Choose Edit. | The Configuration Profile screen displays in a new browser tab. |  |
| 5 | Assign group to configuration profile | Choose Edit.Choose Assign Group.In Select: Characteristic Groups screen, search for AVC_ROBOT_BASIC, and choose Go.Select the item displayed under the Items section, and choose Ok. On the Configuration Profile screen, the selected characteristic is displayed under the Characteristic Groups section.Maintain the sorting order for the characteristic group as 1.Choose Save.Repeat the steps 1 and 5 for the following characteristic group .Sorting Order: 2Characteristic Group: AVC_RBT_REACHChoose Close. | Characteristics group is assigned to the configuration profile. |  |

#### Create Initial Material Stock

Purpose

In a real business scenario, initial material stock are usually purchased from external suppliers through standard purchasing or subcontracting processes. For only testing purpose, this process step shows you how to create and post the initial material stock to storage locations directly.

Prerequisite

Before creating initial material stocks, we recommend that you check stock level for AVC_E2E_MOTOR_1XX, AVC_ E2E _MOTOR_2XX, AVC_E2E_L_ARM_30, AVC_E2E_L_ARM_45 and AVC_E2E_L_ARM_60. To do that, log onto the SAP Fiori launchpad as a Production Planner, and open Manage Material Coverage - New Version (F0251A) app. Remove some stock if there is already sufficient amount of stock in store. Otherwise, no planned orders can be generated later. You can either post initial stock directly to the storage locations, or refer to test scripts from Procurement of Direct Materials (J45) or Scheduling Agreements in Procurement (BMR) test scripts for purchasing processes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Post Goods Movement (MIGO) screen displays. |  |
| 3 | Choose Document Type | Choose Goods Receipt and Other. |  |  |
| 4 | Enter Data | In the Detail Data section, make the following entries and press Enter. Choose Next Item and select Item OK to add entries.On the Where tab:Movement Type: 561Plant: 3310Storage Location: 331C for AVC_E2E_MOTOR_XXX and AVC_E2E_L_ARM_XX materialsStorage Location:331B for AVC_E2E_PAINTING/AVC_E2E_SEALING materialsOn the Quantity tab:Quantity:<100 PC>On the Material tab:Material: <BOM Material>, You must create initial stock for AVC_E2E_MOTOR_1XX, AVC_E2E_MOTOR_2XX, AVC_E2E_L_ARM_30, AVC_E2E_L_ARM_45, AVC_E2E_L_ARM_60, AVC_E2E_SEALING and AVC_E2E_PAINTING |  |  |
| 5 | Check | Choose Check. | The document is ready to be posted. |  |
| 6 | Post | Choose Post. | Material document XXX is posted and materials are available in stock. |  |

#### Creating Stock in Supplying Plant

Purpose

In a real business case, the materials are usually purchased from external suppliers; in that case, that process is covered by the standard purchasing or subcontracting processes. For the purpose of this test, we post initial stock directly to the storage locations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Enter Material | Make the following entry and choose Enter.Material: AVC_E2E_D_ARM_50, AVC_E2E_D_ARM_70Plant: 3320 |  |  |
| 4 | Select Stock | Select the icon beside the stock that you want to add initial stock, for example:Storage Location: 332AUnrestricted-Use Stock | The Manage Stock dialog box opens. The Storage Location, Stock Type and Current Quantity are displayed according to your entries in previous steps. |  |
| 5 | Add Initial Stock | Make the following entries and choose Post:Document Date: <Today>Posting Date: <Today>Stock Change: Initial EntryQuantity: Enter a number, for example, <10> | The system displays the following message. The stock has been added.1 document has been created: Material Document XXXXXXXXXX/20XX |  |

#### Optional: Configure Flexible Workflow for Stock Transport Order

##### Optional: Check Flexible Workflow for Stock Transport Order Approval

Purpose

In this procedure, you check flexible workflow for purchase order approval.

Make sure Flexible Workflow for Purchase Order with UD document is activated, and flexible workflow for purchase order approval is configured.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen displays. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution screen, search Activate Flexible Workflow for Purchase Orders, then choose Go.Select the line of the item and go to next screen.On the Configure Your Solution - Purchase Order Processing screen, choose Configure on the line of Activate Flexible Workflow for Purchase Orders the configuration step. | The Document Types Purchase Order Change screen displays. |  |
| 5 | Activate Flexible Workflow for PO Approval | Make sure the following entries are made:Document Type: UDScenario based workflow: XNote You might be asked to enter a customizing request number, either choose your own customizing request or create a new one. Then choose Continue. | The scenario based workflow is active for purchase orders with Document Type: UD. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Configuration Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflow for Purchase Orders.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Activate Flexible Workflow for Purchase Orders screen displays. |  |
| 3 | Activate Flexible Workflow for PO Approval | Make sure the following entries are made:Document Type: UDScenario based workflow: XNote You might be asked to enter a customizing request number, either choose your own customizing request or create a new one. Then choose Continue. | The scenario based workflow is active for purchase orders with Document Type: UD. |  |

Result

The Scenario based workflow is active for Document Type: UD.

##### Configure Flexible Workflow for Stock Transport Order

Purpose

In this procedure, you configure your release conditions for purchase order approval.

When you start to process this step, please make sure that the flexible workflow for purchase document type NB has been activated in your system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Purchase Orders (F2872). | The Manage Workflows screen displays. |  |
| 3 | Create Manage Workflow | Choose Create and make following entry:Name: Test Workflow for Stock Transport Order UDGo to the Start Conditions area and select Document type of purchase order is: Stock Transp. OrderDel (UD)Choose Add and make the following entry:Purchasing group of purchase order is: 001Go to the Steps area, choose Create, and then make the following entry on the next screen:Step Type: Release of Purchase OrderGo to the Recipients area:Assignment By: UserUser: Select a user from value help (with Employee ID PURCHASING_MANAGER).Step to be completed by：One of the recipients.Choose Create.Choose Save. | The workflow for stock Transport order is configured. |  |
| 4 | Activate Workflow Item | Choose the just created Workflow Item and choose Activate. | The workflow item is activated. |  |

#### Edit User-Specific Parameters for Supplier Invoices (Optional)

Purpose

In this procedure, you will edit User-Specific parameters for supplier invoices.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Edit Supplier Invoice Settings (F3813) | The Edit Supplier Invoice Settings screen is displayed. |  |
| 3 | Set parameter | Check parameter Display Journal Entry: XNote If parameter is checked, when invoice is created, system message contains invoice and journal entry number.If parameter is unchecked, when invoice is created, system message contains invoice number only.When this parameter is changed, for APP Create Supplier Invoice, it will take effective immediately. For APP Create Supplier Invoice – Advanced, user needs to logout and login again to put it into effect. | Change has been saved successfully. |  |

Result

Parameter Display Journal Entry has been set successfully.

#### Create Condition Records (Optional)

Purpose

In case you have fine-tuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BET | Create Sales Pricing Condition - MDS |

#### Change Inspection Plan for Configurable product

Purpose

To run through this business scenario, the inspection plans for configured material AVC_E2E_ROBOT must be adapted regarding some master specific limits of master inspection characteristics.

Prerequisite

Master Inspection Characteristics are already available in the system.

Procedure

Create Inspection Plan for Semifinished Materials

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Planner. | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Change Inspection Plan (QP02) app. | Change Inspection Plan: (Initial Screen) appears. |  |
| 3 | Enter Data | In the Change Inspection Plan: (Initial Screen) make the following entries:Material: AVC_E2E_ROBOTPlant: 3310Key Date: <today>Choose Continue. | The Inspection Plan Change: Operation Overview screen appears |  |
| 4 | Enter Inspection Characteristics | Mark the operation line 0010 and choose Inspection Characteristics.Mark line item for master inspection characteristic YQUALI01 and choose Unlock Master Inspection Characteristics. Click on Continue in the pop up.Then go to Control Indicators for inspection characteristic YQUALI01 and adopt results conformation to Single Result. Click on Continue in the pop up.Click on Save. | Single Results recording is activated. |  |

## Overview Table

The Lot Size of One with Advanced Variant Configuration scenario consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Customer Sales order & MRP |  |  |  |
| [Create Sales Inquiry](#unique_18) [page ] 31 | Internal Sales Representative | Manage Sales Inquiries (F2370) | Sales Inquiry is created. |
| [Create Sales Quotation for Configurable Material](#unique_19) [page ] 32 | Internal Sales Representative | Manage Sales Quotations (F1852) | Sales Quotation is created. |
| [Create Sales Order with Reference to Sales Quotation](#unique_20) [page ] 34 | Internal Sales Representative | Manage Sales Orders (F1873). | Sales Order is created. |
| [Material Requirements Planning at Plant Level](#unique_21) [page ] 36 | Production Planner | Schedule MRP Runs (F1339) | MRP run was carried out successfully. |
| [Evaluate Stock/Requirements Situation](#unique_22) [page ] 38 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Stock/Requirement Situation is evaluated. |
| Procurement of Components |  |  |  |
| [Convert Purchase Requisitions to Purchase Orders](#unique_23) [page ] 40 | Purchaser | Process Purchase Requisitions (F1048A) | Purchase Order is created. |
| [Preview Purchase Order (Optional)](#unique_24) [page ] 42 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order is displayed. |
| [Create Inbound Deliveries](#unique_25) [page ] 43 | Receiving Specialist | Inbound Deliveries for Purchase Orders (VL34) | Inbound Delivery is created. |
| [Post Goods Receipt for Inbound Delivery](#unique_26) [page ] 44 | Receiving Specialist | Change Inbound Delivery (VL32N) | Goods Receipt is posted. |
| [Check Range of Stock Coverage](#unique_27) [page ] 45 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Stock/Requirements situation is evaluated. |
| Intracompany Stock Transfer |  |  |  |
| [Evaluate Stock/Requirements Situation](#unique_28) [page ] 47 | Material Planner - External Procurement | Monitor Material Coverage - Net / Individual Segments (F2101A) |  |
| [Process Stock Transport Requisition (with MRP)](#unique_29) [page ] 48 | Purchaser | Process Purchase Requisitions (F1048A) | A Stock Transport Order will be created. |
| [Change Stock Transport Order (with MRP)](#unique_30) [page ] 49 | Purchaser | Change Purchase Order - Advanced (ME22N) | The Stock Transport Order will be changed. |
| [Optional: Approve Stock Transport Order](#unique_31) [page ] 50 | Purchasing Manager | My Inbox - All Items (F0862) | A Stock Transport Order is approved |
| [Optional: Check Stock Transport Order Approval Details](#unique_32) [page ] 51 | Purchaser | Manage Purchase Orders (F0842A) |  |
| Production of Subassembly in Issuing Plant |  |  |  |
| [Convert Planned Orders to Production Orders for Subassembly](#unique_33) [page ] 52 | Production Planner | Manage Material Coverage - New Version (F0251A) | Production Order is displayed. |
| [Review Production Order (Optional)](#unique_34) [page ] 53 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | Status of Production Order is displayed. |
| [Release Production Order](#unique_35) [page ] 55 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | Production Order is released. |
| [Confirm Production Operations for Assembly](#unique_36) [page ] 56 | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | All Production Operations are confirmed. |
| [Post Goods Receipt for Assembly Production Order](#unique_37) [page ] 57 | Warehouse Clerk | Post Goods Movement (MIGO) | Goods Receipt for Final Assembly. |
| [Evaluating Stock/Requirements Situation (Optional)](#unique_38) [page ] 58 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Stock/Requirements Situation is evaluated. |
| [Create Replenishment Delivery for Stock Transport Order](#unique_39) [page ] 59 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | Outbound Delivery is created. |
| [Optional: Create Pro Forma F8 Invoice](#unique_40) [page ] 60 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing with F8 type is created. |
| [Pick and Post Goods Issue for Stock Transport Order](#unique_41) [page ] 61 | Shipping Specialist | Change Outbound Delivery (VL02N) | Goods Issue is posted. |
| [Check Status of Stock Transfer](#unique_42) [page ] 62 | Warehouse Clerk | Stock - Single Material (F1076) |  |
| [Confirm Quantities for Putaway](#unique_43) [page ] 63 | Receiving Specialist | Inbound Deliveries for Putaway (VL06IP) | The material of the Inbound Delivery has been Putaway. |
| [Post Goods Receipt for Inbound Delivery](#unique_44) [page ] 64 | Receiving Specialist | Inbound Deliveries for Goods Receipt (VL06IG) | Goods Receipt is posted for the Inbound Delivery. |
| Production Order Execution for Subassembly |  |  |  |
| [Convert Planned Orders to Production Orders for Subassembly](#unique_45) [page ] 65 | Production Planner | Manage Material Coverage - New Version (F0251A) | Production Order is created. |
| [Review Production Order (Optional)](#unique_46) [page ] 66 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | Production Order Status is checked. |
| [Execute Material Staging for Subassembly](#unique_47) [page ] 68 | Production Operator - Discrete Manufacturing | Stage Materials for Production (MF60) | Material Staging is executed. |
| [Release Production Order](#unique_48) [page ] 69 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | Production Order is released. |
| [Confirm Production Operations for Subassembly](#unique_49) [page ] 71 | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | All Production Operations are displayed. |
| [Post Goods Receipt for Subassembly Production Order](#unique_50) [page ] 72 | Warehouse Clerk | Post Goods Movement (MIGO) | Goods Receipt for Subassembly is posted. |
| [Review Production Order](#unique_51) [page ] 73 | Production Supervisor - Discrete Manufacturing | Manage Production Operations (F2335) | Production Order is reviewed. |
| [Evaluating Stock/Requirements Situation (Optional)](#unique_52) [page ] 75 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Stock/Requirement Situation is displayed. |
| Production Order Execution for Final Assembly |  |  |  |
| [Convert Planned Orders to Production Orders for Final Assembly](#unique_53) [page ] 76 | Production Planner | Manage Material Coverage - New Version (F0251A) | Production Order is displayed. |
| [Review Production Order (Optional)](#unique_54) [page ] 77 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | Status of Production Order is displayed. |
| [Release Production Order](#unique_55) [page ] 79 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | Production Order is released. |
| [Confirm Production Operations for Final Assembly](#unique_56) [page ] 80 | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | All Production Operations are confirmed. |
| [Post Goods Issue for Final Assembly Production Order Components](#unique_57) [page ] 81 | Warehouse Clerk | Post Goods Movement (MIGO) | Goods Issue for Production Order Components is posted. |
| [Post Goods Receipt for Final Assembly Production Order](#unique_58) [page ] 83 | Warehouse Clerk | Post Goods Movement (MIGO) | Goods Receipt for Final Assembly. |
| [Evaluating Stock/Requirements Situation (Optional)](#unique_59) [page ] 84 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Stock/Requirements Situation is evaluated. |
| Quality Inspection during Goods Receipt from Production |  |  |  |
| [Display Inspection Plan](#unique_60) [page ] 85 | Quality Technician | Display Inspection Plan (QP03) | Inspection Plan is displayed. |
| [Display Quality Technician Overview (Optional)](#unique_61) [page ] 86 | Quality Technician | Quality Technician Overview (F2361) | Quality Technician Overview is displayed. |
| [Display Open Inspection Lots](#unique_62) [page ] 87 | Quality Technician | Manage Inspection Lots (F2343) | Open Inspection Lots are displayed. |
| [Display Inspection Methods](#unique_63) [page ] 88 | Quality Technician | Display Inspection Methods (F0311A) | Inspection Methods are displayed. |
| [Record Inspection Results](#unique_64) [page ] 89 | Quality Technician | Record Inspection Results (F1685A) | Inspection Results are recorded. |
| [Display Quality Engineer Overview (Optional)](#unique_65) [page ] 91 | Quality Engineer | Quality Engineer Overview (F2360) | Quality Engineer Overview is displayed. |
| [Make Usage Decision](#unique_66) [page ] 92 | Quality Engineer | Record Usage Decision (QA11) | Usage Decision is recorded. |
| [Display Material Stock after Usage Decision](#unique_67) [page ] 93 | Warehouse Clerk | Stock - Single Material (F1076) | The stock quantities for subassembly material are updated based on the quality inspection and respective usage decision. |
| Outbound Delivery Processing |  |  |  |
| [Create Delivery](#unique_68) [page ] 94 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Delivery is created. |
| [Execute Picking](#unique_69) [page ] 96 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Delivery is picked. |
| [Maintain Serial Numbers](#unique_70) [page ] 97 | Shipping Specialist | Change Outbound Delivery (VL02N) | Serial Numbers of picked materials are recorded. |
| [Post Goods Issue](#unique_71) [page ] 98 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Goods Issue is posted. |
| Accounts Receivable |  |  |  |
| [Create Billing Document](#unique_72) [page ] 100 | Billing Clerk | Create Billing Documents - VF01 (VF01) | Billing Document is created. |
| [Post Incoming Payments](#unique_73) [page ] 102 | Accounts Receivable Accountant | Post Incoming Payments (F1345) | Incoming Payments are posted. |
| Accounts Payable |  |  |  |
| [Create Supplier Invoice](#unique_74) [page ] 104 | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) | Supplier Invoice is created. |
| [Post Outgoing Payment](#unique_75) [page ] 106 | Accounts Payable Accountant | Post Outgoing Payments (F1612) | Outgoing Payments are posted. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Customer Sales Order and MRP

#### Create Sales Inquiry

Purpose

This activity enables you to enter a sales inquiry after a customer has requested one.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Internal Sales Representative. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Inquiries (F2370). | The Manage Sales Inquires Initial screen displays. |  |
| 3 | Choose Create Inquiry | Choose Create Inquiry . | The Create Inquiry screen displays. |  |
| 4 | Enter Inquiry type | On the Create Inquiry screen, enter the following data and choose Continue:Inquiry Type: IN |  |  |
| 5 | Enter Inquiry Details | On the Create Inquiry: Overview screen, make the following entries and choose Enter:Sold-to party: 33100001Ship-to party: 33100001Customer Reference: <Reference Text>Material: AVC_E2E_ROBOTOrder Quantity: 1 PC |  |  |
| 6 | Start Multi-Level configuration | On the Variant Configuration screen, go to tab Reach, provide the following Item values and choose Enter.Length of Drive Arm: <select one of the values>Length of Link Arm: <select one of the values>Reach (Minimum) Requested: <enter a value from value range>Reach (Maximum) - Requested : <enter a value from value range> | The values of Reach (Minimum) – Technical and Reach (Maximum) – Technical are determined automatically |  |
| 7 | Continue Multi-Level configuration | On the Variant Configuration screen, go to tab Basic, provide the following Item values and choose Done.Service Level Agreement: <select one of the values>Robot Application: <select one of the values>Speed: <enter a value from interval> | The values of Speed Motor X are determined automatically |  |
| 8 | Save | Choose Save. Take note of the inquiry number. |  |  |

#### Create Sales Quotation for Configurable Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to enter the sales quotation with reference to a previously created sales inquiry.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Quotations (F1852). | The Manage Sales Quotations (F1852) screen displays. |  |
| 3 | Navigate to Create Sales Quotation Screen | On the Manage Sales Quotations (F1852) screen, choose Create Quotation. |  |  |
| 4 | Enter Quotation Details | Make the following entries and choose Create with Reference:Quotation Type: QTSales Organization: 3310Distribution Channel: 10Division: 00In the Create with Reference pop-up on tab Quotation enter the following data and choose CopyInquiry: <inquiry created in previous step> | Quotation creation started |  |
| 5 | Check Availability | On the On the Review Availability Check Result screen, choose Apply. | Delivery date is confirmed |  |
| 6 | Maintain Customer Reference and Valid to date | Make the following entries and choose Enter:Cust. Reference: <enter a reference number>Valid to: <enter a date>, for example, one month after today | Customer Reference maintained in Sales Quotation |  |
| 7 | Change Multi-Level-Configuration | To check/change configuration, mark Item in All Items section and choose Item Details: Configuration icon above the line item.On the Variant Configuration screen, go to tab Reach and Basic to check the configuration and make changes if required.Choose Enter when done. | Configuration is updated |  |
| 8 | Review Availability Check Results | If Required Delivery Date cannot be met, a confirmed Delivery Date is suggested. Check the date and choose Apply | Delivery Date is confirmed |  |
| 9 | Check Pricing | Select Quotation item and select Item Conditions icon above the line item. Pricing of variant components displays.Check the condition value of condition type PVA0.The value of this condition depends on the Service level agreement chosen in the configurationChoose Back. |  |  |
| 10 | Display Print Preview | On the Create Quotation: Overview screen, choose Header Output Preview button.On the Display Quotation xxx: Output screen, select the line already created for the print output and choose Display Document.Check the variant pricing and configuration details on the displayed PDF document.Choose Back. | Choose your local destination and choose Print. |  |
| 11 | Save Document | Choose Save. Make a note of the quotation number: __________.Note In case the document is incomplete before save, please maintain missing data. Do also ensure that Quotation is costed without any errors (Check in Display Sales Quotation and in menu option Extras > Costing . If costing has not been executed, please run costing and save. | The quotation is saved. |  |

#### Create Sales Order with Reference to Sales Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a customer order regarding the quotation after the customer accepted the quotation. Finally, the order confirmation is printed and can be sent to the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Sales Orders - VA01 (VA01). | The Create Sales Documents .screen displays. |  |
| 3 | Enter the Order Type and the Sales Organization | Make the following entries and choose Create with Reference:Order Type: OR | The dialogue window Create with Reference displays. |  |
| 4 | Enter Quotation Number | Make the following entries and choose Copy:Quotation: <Quotation Number> (The Quotation from previous step)On the Review Availability Check Result screen, choose Apply. | The Create MTO Standard Order: Overview displays. |  |
| 5 | Change the Delivery Date and Enter Order Details | Make the following entries and choose Enter:Cust. Reference: <Enter a reference number> |  |  |
| 6 | Check Configuration | Select the line item and choose Item details: Configuration. On the Variant Configuration screen, check characteristics value and choose Done.Note Changing configuration in sales order may change product cost, and results in different product costs in quotation and corresponding sales order. Therefore, if changing of configuration is required by customer, it is suggested to cancel sales order/quotation and create a new quotation instead. |  |  |
| 7 | Display Print Preview | On the Create Sales Order: Overview screen, choose Header Output Preview button.On the Display Sales Order xxx: Output screen, select the line already created for the print output and choose Display Document.Check the variant pricing and configuration details on the displayed PDF document. | Choose your local destination and press Print. |  |
| 8 | Save | Choose Save.Note In case the document is incomplete before save, please maintain missing data. Do also ensure that Sales Order is costed without any errors (Check in Display Sales Orders and in menu option Extras > Costing . If costing has not been executed, please run costing and save).Note Changing configuration in sales order may change product cost, and results in different product costs in quotation and corresponding sales order. Therefore, if changing of configuration is required by customer, it is suggested to cancel sales order/quotation and create a new quotation instead. | Sales order is saved.Note If the sales order might require approval, please refer to scope item Sell from Stock (BD9), and complete the activities of Process Sales Order Approval. |  |

|  |
| --- |
| Note If you maintain different material prices by Ledger (scope item 1ZT - Managing Material Price Changes and Inventory Values) and want to do Ledger specific sales order costing, please refer to the scope item BEG - Standard Cost Calculation and its step Appendix > Manage Order BOM Cost Estimates in Parallel Valuation . |

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

The Make-to-Stock finished goods are planned at plant level. There is now a requirement for AVC_E2E_ROBOT in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirements Planning (MRP)Job Name: <MRP for AVC_E2E_ROBOT >Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: <select>Recurrence Pattern: Single RunChoose OK.Choose Step 3.For 3.Parameters section:Plant: 3310Material: AVC_E2E_ROBOTChanged BOM Components: <select>All Order BOM Components: <select>Stock Transfer Materials: <select>Planning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for AVC_E2E_ROBOT in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

#### Evaluate Stock/Requirements Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock/requirements situation for Make-to-Order finished goods (AVC_E2E_ROBOT) in the stock/requirements list after the requirement planning is performed.

Prerequisite

Requirement planning is carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments (F2101A) screen displays. |  |
| 3 | Select Material | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries.To display all relevant materials enter the following data and press Go:Individual Segment: <Quotation Number created in previous step>-<Item number> e.g. 41967-10Select all displayed materials and then choose Manage Materials. | The Material and Material Details sub screens display. |  |
| 4 | Review Stock / Requirements List | Select the corresponding material on the Material screen on the left side. | The detailed stock / requirements list for each material displays. |  |
| 5 | Display Planned Order | From the list on the Material sub screen on your left, select the material for which you want to check for the planned order:Material: AVC_E2E_ROBOTMaterial: AVC_E2E_LINK_ARMMaterial: AVC_E2E_CONTROLMaterial: AVC_E2E_BASE_FRAMEMaterial: AVC_E2E_DRIVE_ARM.On the Material Details subscreen, choose PldOrd XXXX or PurRqs XXXX in the MRP Element column.Note The BOM explosion during the MRP run has generated dependent requirements for the demand-driven planned components. If there is not enough inventory to fulfill the requirements, planned orders and purchase requisitions are created for both inhouse-produced and externally-procured materials. | The selected planned order details are displayed on pop-up screen.Note The planned order is generated only when there is shortage for these materials.If you want to display more information of the planned order, choose Open... > Planned Order at the bottom right of the dialog box. |  |
| 6 | Rescheduling Check (Optional) | On the Stock/Requirements List tab, the Rescheduling column displays the rescheduling status of the following MRP elements.PurReqPurchase OrdersPlanned OrdersProduction OrdersProcess OrdersIf needed,you can choose the following icons in Rescheduling column for corresponding functions:Reschedule in (bring operation forward if the receipt element lies after the requirement date)Reschedule out (postpone operation, if the receipt element lies before the requirement date)Plan Process according to scheduleCancel ProcessExcess StockExcess in individual segment |  |  |

### Procurement of Components

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
| 2 | Access App | Open Process Purchase Requisitions (F1048A) .Note If you want to use the Save Draft feature in this app, you have to use a personalized user. | The Process Purchase Requisitions screen is displayed. |  |
| 3 | Search for Purchase Requisition | Enter the Purchase Requisition number and choose Go. | The Purchase Requisition is displayed. |  |
| 4 | Select Purchase Requisition | Select the Purchase Requisition from previous step for material AVC_E2E_CONTROL. | The Purchase Requisition has been selected for source assignment. |  |
| 5 | Assign Source to Purchase Requisition | Click on 'Show more per Row' and check if for the relevant Purchase Requisition a source has been assigned in field Fixed Supplier. In this case no assignment of source is required. If the Purchase Requisition hasn't been assigned a source, then click on 'Assign Source of Supply' button in field Fixed Supplier and select a supplier in the ‘Assign Source of Supply’ window and click on Assign button. Click on OK button in the success message. | The assignment of one source to the requisition is done. |  |
| 6 | Prepare the Purchase Order | Select the purchase Requisition where the assigned supplier is displayed and choose Create Purchase Order. | The Process Purchase Requisitions screen is displayed. |  |
| 7 | Create the Purchase Order | On the Purchase Order screen in the Basic Data section, make the following entry:Purchase Order Type: Standard PO.Choose Order.Check the data below in the purchaser order created after Save.Go to Process Control area:Goods Receipt: <Selected>GR-Based Inv.Verif: <Selected>Go to the Tax area:Tax Code: <00>Note Additional Fiscal Data were delivered to send to the External Tax Partner Engine more specific data about the purchasing scenario that the customer is processing. The user can configure the values for AFD fields that will be available on Purchase order creation screen. Those are the new fields Business transaction and Usage purpose.Some cases are standard delivered by SAP, but the customer can also add your own data to the table, according procedure described in Create Master Data for Brazil (JD0_BR).If the iNote scenario applies to your business process, it is necessary to acess the Change Purchase Order - Advanced app (ME22N) to review the purchase order.In this app, go to Brazil tab, open the button Additional Fiscal Data and input these fields:Business transactionSelect the option that is related to the purchasing process.Usage purposeSelect the option that is related to the business process.Note The planned freight received separately from the material Nota Fiscal Document is not supported by the Integration with External Tax Calculation Engines in Brazilian Localization. | The purchase order is created. |  |
| 8 | Back to Manage Purchase Requisition | Once the order is saved the message 'Purchase order has been created' is displayed. Go back to ‘Process Purchase Requisition’ overview screen. | Purchase Requisition list is displayed again.The Processing Status of Purchase Requisition has been changed to PO created. |  |
| 9 | Convert Purchase Requisition for other Material | Repeat steps 3 to 8 with the following data:Material: AVC_E2E_BASE_FRAME | The purchase order is created. |  |

#### Preview Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can preview an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Purchaser role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Purchase Order | Open Manage Purchase Orders (F0842A).If you want to use the Save Draft feature in this app, you have to use a personalized user. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Select Purchase Order | Enter the Purchase Order number in the Purchase Order search box, and choose Go. Select the row for the Purchase Order you want to preview and use the little arrow on the right side to enter the PO detail. | The Standard PO xxxxx Created by xxxxx screen is displayed. |  |
| 4 | Preview the Purchase Order | Choose Messages at the top of the screen.On the Display Pur. Order :: Output screen, select the checkbox of the entry in the Output table and choose Display PDF Document. | The Purchase Order is opened in PDF format.The Characteristic Names and Characteristic Values are displayed. |  |
| 5 | Review the Characteristic Values | Review the Characteristic Values for material AVC_E2E_CONTROL. The values are inherited from the Sales Order which is created in previous step.Choose Configuration on the Material Data tab. On the Variant Configuration screen, check whether the characteristic values displayed are same as the ones chosen in the sales order. Choose Close once done. | The Characteristic Values are reviewed. |  |

#### Create Inbound Deliveries

Purpose

In this activity, you create the inbound deliveries. Please use the the purchase order created in the step.Convert Purchase Requisition to Purchase Order.

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
| 1 | Log on | Log onto the SAP Fiori Launchpad using the role Receiving Specialist. | The Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Inbound Deliveries for Purchase Orders (VL34). | The Generation of Inbound Deliveries screen displays. |  |
| 3 | Create Inbound Delivery | Make the following entries then choose Execute:Document Number: XXX (Enter the purchase order number created in previous step)Delivery Date: XXX Delete the default date and enter the delivery date in purchase orderTest Run: uncheckedThe Inbound Delivery Number is displayed, write it down for further use. | A new Inbound Delivery is created.The Inbound Delivery Number is displayed. |  |

#### Post Goods Receipt for Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post the goods receipt for the material against the inbound delivery of scheduling agreement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2. | Access the App | Open Change Inbound Delivery (VL32N). | The Change Inbound Delivery (VL32N) screen displays. |  |
| 3 | Enter detail data | On the initial screen, enter the following values then choose Continue:Inbound Delivery Number: Select your inbound delivery created in step above, using input helpNote If the Delivery pop up appears then select Inbound Delivery: Not Posted for GR, and enter following data and choose Go:Supplier 33300001Delivery Date: Today's dateSelect one item from the search result, choose OK | The Inbound Delivery xxxxxxxxx Change: Overview screen displays. |  |
| 4 | Confirm Quantities for Putaway | In Item Overview tab, enter the following details:Putaway Qty: xxxSLoc: 331BNote The putaway quantity should equal to the delivery quantityAnd choose Save. | Back to the Change Inbound Delivery screen and Inbound Delivery xxxxxxxxx has been saved message displays. |  |
| 5 | Maintain Serial Number | If material is serial number managed, e.g. AVC_E2E_CONTROL, mark the item and go to Menu > Extras > Serial Numbers .In Popup choose Create Serial Number automatically and press Continue. |  |  |
| 6 | Post Goods Receipt | Choose Post Goods Receipt. | The system message Goods receipt for inbound delivery xxxxxxxxx posted (material Document 500xxxxxxx) appears. The material is posted to the unrestricted use stock with storage location 331B and plant 3310. You can display the stock overview in APP Display Stock Overview (MMBE). |  |
| 7 | Repeat for all Inbound Deliveries | Repeat steps 3 to 6 for all inbound deliveries. | Goods Receipt is posted. |  |

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
| 2 | Access the App | Open the Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments (F2101A) screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. |  |  |
| 4 | Select Material | Choose Adapt Filters to add the Material filter if not added, enter the following value:Material: AVC_E2E_ROBOT, AVC_E2E_LINK_ARM, AVC_E2E_BASE_FRAME, AVC_E2E_CONTROL | The Manage Material Coverage screen displays. |  |
| 5 | Review Stock / Requirements List | Select the corresponding material on the Material screen on the left side. | The detailed stock / requirements list for each material displays. |  |
| 6 | Display Planned Order | From the list on the Material subscreen on your left, select the material for which you want to check for the planned order.Material: AVC_E2E_ROBOT, AVC_E2E_LINK_ARM, , AVC_E2E_CONTROLNote The BOM explosion during the MRP run has generated dependent requirements for the demand driven planned components. If there is not enough inventory to fulfill the requirements, planned orders and purchase requisitions are created for both inhouse-produced and externally-procured materials. | The selected planned order displays.Note The planned order is generated only when there is storage for these materials.If you want to display more information of the planned order, choose Open > Planned Order at the bottom right of the dialog box. |  |
| 7 | Rescheduling Check (Optional) | In the Stock/Requirements List, the Rescheduling column displays the rescheduling status of the following MRP Elements.PurReqPurchase OrdersPlanned OrdersProduction OrdersProcess OrdersYou can choose below icons in the Rescheduling column to perform corresponding actions.Reschedule in (Bring operation forward if the receipt element lies after the requirement date)Reschedule out (Postpone operation, if the receipt element lies before the requirement date)Plan Process according to scheduleCancel ProcessExcess StockExcess in individual segment | Corresponding actions perform. |  |

### Intracompany Stock Transfer

#### Evaluate Stock/Requirements Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the requirement planning has been performed, you want to display the stock/requirements situation for the Semifinished Goods (AVC_E2E_DRIVE_ARM) in the stock/requirements list.

Prerequisite

Requirement planning has been carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 4 | Select Material and Show Shortages | In the search area, make the following entries and choose Go.Material: AVC_E2E_DRIVE_ARMSelect the filtered rows and choose Manage Materials. | The Manage Material Coverage screen displays. |  |
| 5 | Verify Purchase Requisitions that are Available | In the Stock/Requirements List, find available purchase requisitions. Look for rows with PurRqs items. | The MRP has created purchase requisition. |  |

#### Process Stock Transport Requisition (with MRP)

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
| 2 | Access App | Open Process Purchase Requisitions (F1048A) .Note If you want to use the Save Draft feature in this app, you have to use a personalized user. | The Process Purchase Requisitions screen is displayed. |  |
| 3 | Search for Purchase Requisition | Enter the Purchase Requisition number and choose Go. | The Purchase Requisition is displayed. |  |
| 4 | Select Purchase Requisition | Select the Purchase Requisition from previous step for material AVC_E2E_DRIVE_ARM. | The Purchase Requisition has been selected for source assignment. |  |
| 5 | Prepare the Purchase Order | Select the purchase Requisition where the assigned supplier is displayed and choose Create Purchase Order.Confirm the Pop-up. | The Process Purchase Requisitions screen is displayed. |  |
| 6 | Create the Purchase Order | Pop up message with purchase order created is displayed. | The purchase order is created. |  |
| 7 | Back to Manage Purchase Requisition | In the dialog box, choose OK. | Purchase Requisition list is displayed again.The Processing Status of Purchase Requisition has been changed to PO created. |  |

#### Change Stock Transport Order (with MRP)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to perform when changes within the stock transfer purchase order have to be made.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Purchase Order - Advanced (ME22N) . | Selected stock transport order is displayed. |  |
| 3 | Enter Stock Transportation Order | Choose Other Purchase Order and enter the Stock Transport Order Number created in the previous step and then choose Other Document.Then choose Display/Change to switch to edit mode. |  |  |
| 4 | Change Data (Text) | Open header details or items details.Choose the Texts tab. Select the type of text to be entered, and enter text. | Selected stock transport order displays. |  |
| 5 | Change Data (Storage Location) | Open items overview:1. Check the storage location and change if different from 331A.2. Change the Delivery Date to tomorrow. | The stock transport order is changed. |  |
| 6 | Change Data (Confirmation Control) | Choose the Confirmation tab, Select the option Inbound Delivery from the dropdown list Conf. Control and choose Enter.Save the changes by choosing Save. | The stock transport order is updated and saved. |  |

#### Optional: Approve Stock Transport Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the activity, the Purchase Manager releases a stock transport order.

A prerequisite is the existence of a stock transport order that can be released. Purchasing group is 001 and all stock transport order in UD require an approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | A list of already created purchase orders displays. |  |
| 3 | Search for Purchase Order Status | Enter the stock transport order number in the search area, then choose Search. | The purchase orders without follow-on documents (w/o status Follow-On Documents) and purchase group is 001 have the status in approval. |  |
| 4 | Open Approve Purchase Orders | On the My Inbox screen, select the purchase order from the left screen. | The My Inbox screen displays. |  |
| 5 | Approve Purchase Order | On the Release Purchase Order screen confirm your created purchase Order information.Choose Approve.On the Submit Decision screen, add note if necessary and choose Submit. | Stock transport order is approved. |  |

#### Optional: Check Stock Transport Order Approval Details

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to check an existing stock transport order's approval details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen displays. |  |
| 3 | Search for Stock Transport Order | Enter the stock transport order number in the search area, and then choose Go. |  |  |
| 4 | Choose Purchase Order | Choose the row for the purchase order you want to preview, then go to Purchase Order screen. | The Purchase Order screen displays. |  |
| 5 | Check Approval Details | Go to the Approval Details area and check the approval information. | The purchase order's approval details display. |  |

### Production of Subassembly in Issuing Plant

#### Convert Planned Orders to Production Orders for Subassembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Daily MRP run creates planned orders for goods to be produced internally. This process step shows you how to convert the planned orders to production orders for semifinished goods in the issuing plant, based on the configuration in receiving plant when reached the planned start date.

Prerequisite

The MRP run has generated planned orders for AVC_E2E_DRIVE_ARM (subassembly).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A). | The Check Material Coverage displays with Find Material dialog box. |  |
| 3 | Select Material | Enter the following data and choose Go.Material: AVC_E2E_DRIVE_ARMPlant: 3320Shortage Definition: MRP Standard | The Manage Material Coverage screen displays. |  |
| 4 | Find Planned Order | Search for the Quotation Number created in previous step in field Individual segment and click on the line item.If no planned orders are generated, it could be because AVC_E2E_DRIVE_ARM has sufficient amount of stock in store. In this case, remove some stock. |  |  |
| 5 | Convert Planned Order to Production Order | Select Convert from Edit dropdown list in the Action column for a planned order (PldOrd XXXX).In the Convert Planned Order XXXX dialog box, choose Convert to Production Order radio button, confirm End Date and Quantity. Choose OK. | The production order is created. |  |

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
| 2 | Access the App | Open Manage Production Orders (F2336). | The Manage Production Order screen displays. |  |
| 3 | Check Default Area of Responsibility (Supervisor) | Choose the user icon and select App Settings. Choose tab Production Supervisor.Check if only this entry displays, and choose OK:Plant 2 AE (3320)MTO VC- Valuated (YB3)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries.Next choose Work Center.Check if only this entry displays, and choose OK:Plant 2 AE (3320)ASSEMBLY (ASSEMBLY)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. |  |  |
| 4 | Select Production Order | On the Manage Production Orders (F2336) screen, choose Adapt Filters to display more filter options.In the Adapt Filters dialog box, choose More Filters. Select Material and Production Plant and choose OK. Choose Go.Status: CreatedMaterial: AVC_E2E_DRIVE_ARMProduction Plant: 3320 | The Material and Production Plant fields are added to the filter bar.The searched order displays. |  |
| 5 | Review Material Availability Status | In the Issues column, check the Missing Components icon to the right of the order to display the missing components. | For AVC_E2E_DRIVE_ARM, it is expected, that all components are available. |  |
| 6 | Check PRT (Optional) | If Production Resources/Tools (PRTs) are assigned to the production order, you can check PRT details within this app.Select the order, and choose Order Schedule facet. Choose Settings for the Operations part, and make sure PRTs is selected in the View Settings. PRT hyperlink is available for the operations. |  |  |

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
| 3 | Check Default Area of Responsibility (Supervisor) | Choose the user icon and select App Settings. In the Area of Responsibility dialog box, choose Production Supervisor, check if this entry displays and choose OK:Plant 2 AE (3320)MTO VC- Valuated (YB3)Choose Assign to select this entry if not displayed; choose the Unassign icon to remove any other plant entries. Choose OK.Next choose Work Center, check if this entry displays and choose OK:Plant 2 AE (3320)ASSEMBLY (ASSEMBLY)Choose Assign to select this entry if not displayed; choose the Unassign icon to remove any other plant entries. Choose OK. |  |  |
| 4 | Select Production OrderCheck details of Production Order | On the Manage Production Orders screen, choose Adapt FiltersAdapt Filters dialog box, choose More filters. Select to display more filter options. In the Material and Production Plant to display more filter options. and choose OK. Choose Go.Enter the following filter criteria, and choose Go:Status: CreatedMaterial: AVC_E2E_DRIVE_ARM | The Material and Production Plant fields are added to filter bar.The searched order displays. |  |
| 5 | Execute Release | Select the searched order. Choose Release. | The order is released. |  |

#### Confirm Production Operations for Assembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents include the processing status of orders, operations, sub-operations, and individual capacities. It is an instrument for controlling orders. This process step shows you how to confirm final assembly production order operations for configurable material AVC_E2E_ROBOT.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). |  |  |
| 3 | Enter Production Order and Operation | On the Enter Order and Operation screen, make the following entries and choose Go:Order: <production order number for finished goods>Operation: <operation number>, for example, <0010> |  |  |
| 4 | Enter Quantities Data | In the Quantities section, make the following entries:Yield:<Quantity of prod. order less scra>Scrap:<scrap amount> |  |  |
| 5 | Enter Activities Data and Save | In the Activities section, make the following entries:Setup: <setup time>Machine: <machine time>Labor: <labor time>For partial confirmation, choose Post.For final confirmation, choose Post and Complete. | Confirmation is made. |  |

#### Post Goods Receipt for Assembly Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods receipt for production order of assembly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Enter Goods Receipt Order | Choose Goods Receipt > Order in the header area and make the following entries:Order: <production order number for finished goods>GR goods receipt: <101>Document date: <default>Posting date: <default>On the General tab, next to the Printer icon, select Print via Output Control (mouseover) checkbox, and choose Individual Slip. |  |  |
| 4 | Enter Quantity | On the Quantity tab, confirm production order quantities.On the Where tab, enter the following entry:Storage Location: <332A (Std. storage 1)> |  |  |
| 5 | Set Item OK and Post | Select the Item OK checkbox and choose Post. | The system displays the message Material document 500xxxxxxx posted. |  |

#### Evaluating Stock/Requirements Situation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock/requirements situation for finished goods.

Prerequisite

Goods Receipt posting is carried out for finished goods.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage screen displays. |  |
| 3 | Select Criteria | In the Material field, enter the following materials and choose GO.Material: AVC_E2E_DRIVE_ARM | The Material screen and Material Details screen display. | Stock Availability situation for all materials displays. |
| 4 | Review Stock Availability | Analyze the stock availability situation of materials AVC_E2E_DRIVE_ARM |  | The stock availability situation of the materials is noted from the Shortage Quantity and Stock Availability columns. |
| 5 | Selection of Materials | Use the Check box and select the rows which have AVC_E2E_DRIVE_ARM as the Material No and click Manage Materials on the screen |  | The Material and Material Details screens display.Stock/Requirement list for all the selected materials is displayed. |
| 6 | Display Stock situation of finished goods | From the list on the Material screen on your left, select the material for which you want to check.Material: AVC_E2E_DRIVE_ARMObserve the stock situation for material | Stock quantity has increased by the quantity of goods receipt done in earlier step. |  |
| 7 | End of validation | Click the Back button twice. | SAP Fiori App home screen appears. End of validation of stock check.. |  |

#### Create Replenishment Delivery for Stock Transport Order

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
| 1. | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2. | Access the App | Open My Purchase Orders - Due for Delivery (VL10B). | The Goods Movement screen displays |  |
| 3. | Enter data for PO display | Choose the Purchase Orders Tab and make the following entries then choose Execute:Shipping Point/Receiving Pt: 3320Delivery creation dates: (From): delivery creation From date Delete the default dateDelivery creation dates: (To delivery creation To date Delete the default dateCalcRuleDefltDlvCrDt: calculation rulePurchasing Document: Choose a stock transport order that created in Create Stock Transport Order step . | The Activities Due for Shipping Purchase Orders, Fast Display screen appears. PO due to delivery is listed out. |  |
| 4. | Create Delivery | Select stock transport orders from the list. Choose Background to create delivery in background. | Activities due for shipping purchase orders, fast display screen appears. |  |
| 5. | Check Delivery Number | Choose More > Show/Hide Delivery , and note down the delivery number shown in the SD Doc. field. | A delivery is created. |  |

#### Optional: Create Pro Forma F8 Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create Pro Forma invoice in the selling company.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Documents screen displays. |  |
| 3 | Maintain Billing Date | Choose billing type Pro Forma Invoice for Delivery (F8) and maintain billing date, for example, current date.Enter Delivery Number.Choose Enter. |  |  |
| 4 | Save | Choose Save. | The F8 billing document is created. |  |
| 5 | Search Billing Document | Open Display Billing Documents (VF03). | The Display Billing Document screen displays. |  |
| 6 | Display Billing Document | On the Display Billing Documents (VF03) screen, enter the Billing Number, and choose Continue. | The Billing Document screen displays. |  |
| 7 | Check Output Condition | On the Pro Forma Invoice for Delivery xxxxxxxx (F8) Display: Overview screen, choose Change Bill. Doc., and then choose Menu > Goto > Header > Output . | The Invoice xxxxxxxx Change: Output screen displays. |  |
| 8 | Display Print Preview | On the Pro Forma Invoice for Delivery xxxxxxxx (F8) Change: Output screen, select the output entry and choose Display Document. | A preview of the PDF document displays. |  |
| 9 | Print Billing Document | From the preview of the document, choose Print. |  |  |

#### Pick and Post Goods Issue for Stock Transport Order

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen displays. |  |
| 3 | Enter Delivery Number | On the Change Outbound Delivery screen, enter the delivery document number from the earlier section and choose Continue. | The Replenishment Dlv. XXXXXXXX Change: Overview screen displays. |  |
| 4 | Enter Serial Number | Go to Change Menu > Extras > Serial Numbers.In the Maintain Serial Numbers Pop-up enter Serial Number and press Continue. |  |  |
| 5 | Enter Picking Data | Choose Picking tab, and make the following entries:Picked Qty: <picked quantity>Choose Save. | The system shows the message:Replenishment Dlv. XXXXXXXX has been saved.The screen return to the Change Outbound Delivery screen. |  |
| 6 | Post Goods Issue | On the Change Outbound Delivery screen, choose Post Goods Issue. | Note When posting goods issue of outbound delivery, the inbound delivery in receiving plant is automatically triggered when confirmation control in Purchase order is set to “Inbound Delivery”.To check the Inbound delivery in receiving plant :- Open Display Purchase Order - Advanced (ME23N) and Choose Other Document > Enter the Stock Transport Order Number > Choose the Confirmation tab > Note down Inbound delivery. |  |

#### Check Status of Stock Transfer

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material screen displays. |  |
| 3 | Enter Material Number | Enter material AVC_E2E_DRIVE_ARM and choose Enter. In column Stock In Transit, click on the hyperlink to get information on Sales Order Stock in Transit. | You receive an overview of the material. This concerns all material that has left the supplying plant and hasn't yet reached the receiving plant. |  |

#### Confirm Quantities for Putaway

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity is performed to confirm all the materials of the Inbound Delivery have been put away in the correct quantities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Receiving Specialist. | The Fiori Launchpad displays. |  |
| 2 | Access the App | Open Inbound Deliveries for Putaway (VL06IP). | The Inbound Deliveries for Putaway screen displays. |  |
| 3 | Enter Inbound Delivery Number | Make the following entries then choose Execute:Purchasing document: Enter the stock transport number created in the previous step.Delivery Date: Delete the default date.Choose Change Inbound Deliveries | The selected Inbound Delivery displays. |  |
| 4 | Confirm Quantities for Putaway | On Stock Placement tab, enter the Putaway Qty for the items: XXXNote The putaway quantity should equal to the Delivery Qty.And choose Save. | Back to the Inbound Deliveries for Putaway screen andInbound Delivery XXX has been saved.message displays. |  |

#### Post Goods Receipt for Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity is performed to Post Goods Receipt for the Inbound Delivery to receive the materials to stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Inbound Deliveries for Goods Receipt (VL06IG). | The Inbound Deliveries for Goods Receipt screen displays. |  |
| 3 | Enter Inbound Delivery Number | Make the following entries then choose Execute:Purchasing document: Enter stock transport order number created in the previous step.Delivery Date: Delete the default date | The Goods Receipt for Inbound Deliveries to be Posted screen shows up.The selected inbound deliveries are shown. |  |
| 4 | Change the Inbound Delivery | Check the selected inbound deliveries and choose Post Goods Receipt.The Specify Actual Goods Receipt Date dialog box displays and choose Continue. | The goods receipt is posted.A success message is shown. |  |

### Production Order Execution for Subassembly

#### Convert Planned Orders to Production Orders for Subassembly

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

The MRP run has generated planned orders for AVC_E2E_LINK_ARM (subassembly).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A). | The App displays with Find Material dialog box. |  |
| 3 | Select Material | Enter the following data and choose Go.Material: AVC_E2E_LINK_ARMPlant: 3310Shortage Definition: MRP Standard | The Manage Material Coverage screen displays. |  |
| 4 | Find Planned Order | Search for the Quotation Number created in previous step in field Individual segment and click on the line item.Note If no planned orders are generated, it could be because AVC_E2E_LINK_ARM has sufficient amount of stock in store. |  |  |
| 5 | Convert Planned Order to Production Order | Select Convert from Edit dropdown list in the Action column for a planned order (PldOrd XXXX).In the Convert Planned Order XXXX dialog box, choose Convert to Production Order radio button, confirm End Date and Quantity. Choose OK. | The production order is created. |  |

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

Production orders are created for subassembly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). |  |  |
| 3 | Check Default Area of Responsibility (Supervisor) | Choose the user icon and select App Settings. Choose tab Production Supervisors.Check if only this entry is assigned:Plant 1 AE (3310)MTO VC - Valuated (YB3)Choose Assign after selecting this entry if not assigned; choose Unassign by selecting any other plant entries that are assigned.Next choose Work Centers / Resources.Check if only this entry assigned, and choose Go Back:Plant 1 AE (3310)Testing (TESTING)Choose Assign after selecting this entry if not assigned; choose Unassign by selecting any other plant entries that are assigned. | The Manage Production Order screen displays. |  |
| 4 | Select Production Order | On the Manage Production Orders (F2336) screen, choose Adapt Filters to display more filter options.In the Adapt Filters dialog box, choose More Filters. Select Material and Production Plant and choose OK. Choose Go.Status: CreatedMaterial: AVC_E2E_LINK_ARMProduction Plant: 3310 | The Material and Production Plant fields are added to the filter bar.The searched order displays. |  |
| 5 | Review Material Availability Status | In the Issues column, check the Missing Components icon to the right of the order to display the missing components.Missing Components | For AVC_E2E_LINK_ARM, the expected missing components are AVC_E2E_MOTOR_1XX, AVC_E2E_MOTOR_2XX and AVC_E2E_L_ARM_XX(material depending on configuration). The materials are supplied after the Material Staging step. |  |
| 6 | Check PRT (Optional) | If Production Resources/Tools (PRTs) are assigned to the production order, you can check PRT details within this app.Select the order, and choose Order Schedule facet. Choose Settings for the Operations part, and make sure PRTs is selected in the View Settings. PRT hyperlink is available for the operations. |  |  |

#### Execute Material Staging for Subassembly

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
| 3 | Enter Details | Make the following entries and choose Execute.In the Staging Types section:SLoc Level: <select>Plant:3310Selection Horizon for Reqmts: <date must be in the future - after scheduled start date>On the Production/Process Orders tab:Order: < Production Order Number for AVC_E2E_LINK_ARM > | The Pull List: Storage Location Level screen displays. |  |
| 4 | Choose Replenishment Elements | In the Total Reqmts table, select the line items and choose Replenishment Proposals on the top of the screen.Review staged quantities and choose Replenishment Elements. |  |  |
| 5 | Enter Replenishment Storage Location and Stage Material | In the Replen. Element table, in the RepLoc column, enter 331C for staged materials.Choose Stage. |  |  |
| 6 | Save | Save your entries.Missing materials are transferred to the shop floor from the designated storage area.With this step, the shortage of materials AVC_E2E_MOTOR_1XX, AVC_ E2E _MOTOR_2XX and AVC_E2E_L_ARM_XX for Subassembly production order is supplied. | Materials are staged for subassembly. |  |

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
| 2 | Access the App | Open Manage Production Orders (F2336). | The Manage Production Orders (F2336) screen displays. |  |
| 3 | Check Default Area of Responsibility (Supervisor) | Choose the user icon and select App Settings. In the Area of Responsibility dialog box, choose Production Supervisor, check if this entry displays and choose OK:Plant 1 AE (3310)MTO VC - Valuated (YB3)Choose Assign to select this entry if not displayed; choose the Unassign icon to remove any other plant entries. Choose OK.Next choose Work Center, check if this entry displays and choose OK:Plant 1 AE (3310)Testing (TESTING)Choose Assign to select this entry if not displayed; choose the Unassign icon to remove any other plant entries. Choose OK. |  |  |
| 4 | Select Production OrderCheck details of Production Order | On the Manage Production Orders screen, choose Adapt Filters to display more filter options. In the Adapt Filters dialog box, choose More filters. Select Material and Production Plant and choose OK. Choose Go.Enter the following filter criteria, and choose Go:Status: CreatedMaterial: AVC_E2E_LINK_ARMProduction Plant: 3310 | The Material and Production Plant fields are added to filter bar.The searched order displays. |  |
| 5 | Execute Release | Select the searched order. Choose Release. | The order is released.Note With the release of production order for subassembly production, the shortage of material AVC_E2E_LINK_ARM for final assembly production order is supplied. |  |

#### Confirm Production Operations for Subassembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents include the processing status of orders, operations, sub-operations, and individual capacities. It's an instrument for controlling orders. This process step shows you how to confirm subassembly production order operations for semifinished material AVC_E2E_LINK_ARM. A goods movement document is generated when the last operation is confirmed. The backflush is carried out together with the confirmation steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). |  |  |
| 3 | Enter Production Order and Operation | On the Enter Order and Operation screen, make the following entries and choose Go:Order: <Production Order Number for semifinished goods>Operation: <operation number> for example, <0010> |  |  |
| 4 | Enter Quantities Data | In the Quantities section, make the following entries:Yield: <Quantity of prod. order less scrap>Scrap: <scrap amount> |  |  |
| 5 | Check Material Movements | In the Material Movements section, check the material list.Note The system shows you an overview materials table for which the material withdraws are done along with operation confirmation.The material AVC_E2E_MOTOR_1XX, , AVC_E2E_MOTOR_2XX and AVC_E2E_L_ARM_XX is set for backflush (in material master) for withdraws to be done automatically after the operation is confirmed. |  |  |
| 6 | Enter Activities Data and Save | In the Activities section, make the following entries:Setup: <setup time>Machine: <machine time>Labor: <labor time>For partial confirmation, choose Post.For final confirmation, choose Post and Complete. | Confirmation is made. |  |
| 7 | Repeat Steps | Go back and repeat steps 3 to 6 for Operation 0020 and 0030. |  |  |
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

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Enter Goods Receipt Order Data | Make the following entries:Select Goods Receipt and Order from the dropdown list on top of the screen.Order: <Production order number for semifinished goods>GR/GI Slip No.: <101>Document date: <default>Posting date: <default>On the General tab, next to the Printer icon, select Print via Output Control (mouseover) checkbox, and choose Individual Slip. |  |  |
| 4 | Enter Quantity | On the Quantity tab, confirm production order quantitiesOn the Where tab:Storage Location: < 331B (Std. storage 2)>On the Serial Numbers tab, select all the serials numbers for the yield quantities except the scrap ones. |  |  |
| 5 | Set Item OK and Post | Select the Item OK checkbox and choose Post. | The system displays the message: Material document 500xxxxxxx posted |  |

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
| 3 | Select Production Order | On the Manage Production Operations screen, choose Adapt Filters to display more filter options.In the Adapt Filters dialog box, choose More Filters. Select Material and Plant and choose OK. Choose Go.Enter the following filters criteria and choose Go.Material: AVC_E2E_LINK_ARMOrder: <Order created above for subassembly>Plant: 3310 | The Material and Plant fields are then added to filter bar.Selected order displays. |  |
| 4 | Check Detailed Operations Status | Check detailed information for selected production operations.Operation Issue:Empty if there is no production order issue.Delay or Missing Components / PRT issue or Quantity Deviation / Quality Issue information shows if relevant issue exists.Components:Material, total quantity and Issued / open quantity information for order components displays.Order Schedule:Detailed operation information with relevant work center, confirmed quantity, start and end time displays.Work Center Schedule:The relevant order covering the same work center capacity (operation is partially confirmed) displays.Operations not Started:The relevant order that would cover the same work center capacity (operation is released) displays.Confirmation:Detailed confirmation information with Yield, Scrap, Rework quantity displays if confirmation has been executed.Inspection:Detailed inspection lots information displays if existed. | Detailed operations status displays. |  |

#### Evaluating Stock/Requirements Situation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock/requirements situation for semi-finished materials.

Prerequisite

Goods Receipt posting is carried out for semi-finished materials.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage screen displays. |  |
| 3 | Select Criteria | In the Material field, enter the following materials and choose GO.Material: AVC_E2E_LINK_ARM . | The Material screen and Material Details screen display. | Stock Availability situation for all materials displays. |
| 4 | Review Stock Availability | Analyze the stock availability situation of materials AVC_E2E_LINK_ARM . |  | The stock availability situation of the materials is noted from the Shortage Quantity and Stock Availability columns. |
| 5 | Selection of Materials | Use the Check box and select the rows which have AVC_E2E_LINK_ARM as the Material No and click Manage Materials on the screen |  | The Material and Material Details screens display.Stock/Requirement list for all the selected materials is displayed.Rows with SchLne items are displayed for the finished product. |
| 6 | Display Stock situation of semi-finished materials | From the list on the Material screen on your left, select the material for which you want to check.Material: AVC_E2E_LINK_ARMObserve the stock situation for material | Stock quantity has increased by the quantity of goods receipt done in earlier step. |  |
| 7 | End of validation | Click the Back button twice. | SAP Fiori App home screen appears. End of validation of stock check.. |  |

### Production Order Execution for Final Assembly

#### Convert Planned Orders to Production Orders for Final Assembly

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

The MRP run has generated planned orders for AVC_E2E_ROBOT (final subassembly).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A). | The Check Material Coverage displays with Find Material dialog box. |  |
| 3 | Select Material | Enter the following data and choose Go.Material: AVC_E2E_ROBOTPlant: 3310Shortage Definition: MRP Standard | The Manage Material Coverage screen displays. |  |
| 4 | Find Planned Order | Search for the Quotation Number created in previous step in field Individual segment and click on the line item.If no planned orders are generated, it could be because AVC_E2E_ROBOT has sufficient amount of stock in store.In this case, remove some stock. Go back to create PIRs and run MRP again to generate planned orders. |  |  |
| 5 | Convert Planned Order to Production Order | Select Convert from Edit dropdown list in the Action column for a planned order (PldOrd XXXX).In the Convert Planned Order XXXX dialog box, choose Convert to Production Order radio button, confirm End Date and Quantity. Choose OK.Note Please ensure that the Work Scheduling view is maintained for material AVC_E2E_ROBOT. | The production order is created. |  |

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
| 2 | Access the App | Open Manage Production Orders (F2336). | The Manage Production Order screen displays. |  |
| 3 | Check Default Area of Responsibility (Supervisor) | Choose the user icon and select App Settings. Choose tab Production Supervisors.Check if only this entry is assigned:Plant 1 AE (3310)MTO VC - Valuated (YB3)Choose Assign after selecting this entry if not assigned; choose Unassign by selecting any other plant entries that are assigned.Next choose Work Centers / Resources.Check if only this entry assigned, and choose Go Back:Plant 1 AE (3310)ASSEMBLE (ASSEMBLE)Choose Assign after selecting this entry if not assigned; choose Unassign by selecting any other plant entries that are assigned. |  |  |
| 4 | Select Production Order | On the Manage Production Orders (F2336) screen, choose Adapt Filters to display more filter options.In the Adapt Filters dialog box, choose More Filters. Select Material and Production Plant and choose OK. Choose Go.Status: CreatedMaterial: AVC_E2E_ROBOTProduction Plant: 3310 | The Material and Production Plant fields are added to the filter bar.The searched order displays. |  |
| 5 | Review Material Availability Status | In the Issues column, check the Missing Components icon to the right of the order to display the missing components. | For AVC_E2E_ROBOT, it is expected, that all components are available. |  |
| 6 | Check PRT (Optional) | If Production Resources/Tools (PRTs) are assigned to the production order, you can check PRT details within this app.Select the order, and choose Order Schedule facet. Choose Settings for the Operations part, and make sure PRTs is selected in the View Settings. PRT hyperlink is available for the operations. |  |  |

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
| 3 | Check Default Area of Responsibility (Supervisor) | Choose the user icon and select App Settings. In the Area of Responsibility dialog box, choose Production Supervisor, check if this entry displays and choose OK:Plant 1 AE (3310)MTO VC - Valuated (YB3)Choose Assign to select this entry if not displayed; choose the Unassign icon to remove any other plant entries. Choose OK.Next choose Work Center, check if this entry displays and choose OK:Plant 1 AE (3310)ASSEMBLE (ASSEMBLE)Choose Assign to select this entry if not displayed; choose the Unassign icon to remove any other plant entries. Choose OK. |  |  |
| 4 | Select Production OrderCheck details of Production Order | On the Manage Production Orders screen, choose Adapt Filters to display more filter options. In the Adapt Filters dialog box, choose More filters. Select Material and Production Plant and choose OK. Choose Go.Enter the following filter criteria, and choose Go:Status: CreatedMaterial: AVC_E2E_ROBOTProduction Plant: 3310 | The Material and Production Plant fields are added to filter bar.The searched order displays. |  |
| 5 | Execute Release | Select the searched order. Choose Release. | The order is released. |  |

#### Confirm Production Operations for Final Assembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents include the processing status of orders, operations, sub-operations, and individual capacities. It is an instrument for controlling orders. This process step shows you how to confirm final assembly production order operations for configurable material AVC_E2E_ROBOT.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). |  |  |
| 3 | Enter Production Order and Operation | On the Enter Order and Operation screen, make the following entries and choose Go:Order: <production order number for finished goods>Operation: <operation number>, for example, <0010> |  |  |
| 4 | Enter Quantities Data | In the Quantities section, make the following entries:Yield:<Quantity of prod. order less scra>Scrap:<scrap amount> |  |  |
| 5 | Enter Activities Data and Save | In the Activities section, make the following entries:Setup: <setup time>Machine: <machine time>Labor: <labor time>For partial confirmation, choose Post.For final confirmation, choose Post and Complete. | Confirmation is made. |  |

#### Post Goods Issue for Final Assembly Production Order Components

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods issue for production order of final assembly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App. | Open Post Goods Movement (MIGO). |  |  |
| 3 | Enter Goods Issue Order. | Choose Goods Issue > Order in the header area and make the following entries:Order: <production order number for finished goods>GI for Order: <261>Document date: <default>Posting date: <default>On the General tab, next to the Printer icon, select Print via Output Control (mouseover) checkbox, and choose Individual Slip. |  |  |
| 4 | Enter Quantity. | On the Quantity tab, confirm production order quantities.On the Where tab, enter the following entry:Storage Location: <331B (Std. storage 2) 331A (Std. storage 1) for material >AVC_E2E_DRIVE_ARMOn the Serial Numbers tab, select all the serials numbers for the yield quantities except the scrap ones. |  |  |
| 5 | Set Item OK | Select the Item OK checkbox. |  |  |
| 6 | Check other materials. | Repeat steps 4 and 5 for all items. |  |  |
| 7 | Post Goods Movement | Choose Post. | The system displays the message Material document 500xxxxxxx posted. |  |

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

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Enter Goods Receipt Order | Choose Goods Receipt > Order in the header area and make the following entries:Order: <production order number for finished goods>GR goods receipt: <101>Document date: <default>Posting date: <default>On the General tab, next to the Printer icon, select Print via Output Control (mouseover) checkbox, and choose Individual Slip. |  |  |
| 4 | Enter Quantity | On the Quantity tab, confirm production order quantities.On the Where tab, enter the following entry:Storage Location: <331A (Std. storage 1)>On the Serial Numbers tab, select all the serials numbers for the yield quantities except the scrap ones. |  |  |
| 5 | Set Item OK and Post | Select the Item OK checkbox and choose Post. | The system displays the message Material document 500xxxxxxx posted. |  |

#### Evaluating Stock/Requirements Situation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock/requirements situation for finished goods.

Prerequisite

Goods Receipt posting is carried out for finished goods.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage screen displays. |  |
| 3 | Select Criteria | In the Material field, enter the following materials and choose GO.Material: AVC_E2E_ROBOT | The Material screen and Material Details screen display. | Stock Availability situation for all materials displays. |
| 4 | Review Stock Availability | Analyze the stock availability situation of materials AVC_E2E_ROBOT |  | The stock availability situation of the materials is noted from the Shortage Quantity and Stock Availability columns. |
| 5 | Selection of Materials | Use the Check box and select the rows which have AVC_E2E_ROBOT as the Material No and click Manage Materials on the screen |  | The Material and Material Details screens display.Stock/Requirement list for all the selected materials is displayed.Rows with SchLne items are displayed for the finished product. |
| 6 | Display Stock situation of finished goods | From the list on the Material screen on your left, select the material for which you want to check.Material: AVC_E2E_ROBOTObserve the stock situation for material | Stock quantity has increased by the quantity of goods receipt done in earlier step. |  |
| 7 | End of validation | Click the Back button twice. | SAP Fiori App home screen appears. End of validation of stock check.. |  |

### Quality Inspection during Goods Receipt from Production

#### Display Inspection Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you display the inspection plan.

|  |
| --- |
| Note In case you want to perform quality inspection for characteristic values used in sales order configuration of the product you can check a potential workaround in SAP Note 3460063 - Restrictions for Advanced Variant Configuration SAP S/4HANA 2408 CE. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Inspection Plan (QP03). | The Display Inspection Plan: Initial Screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Continue.Material: AVC_E2E_ROBOTPlant: 3310 |  |  |
| 4 | Go to Inspection Characteristics Overview Screen | Select the entry for Operation 0010 and choose Inspection Characteristics.Note If you could not find Inspection Characteristics in your screen, choose More > Inspection Characteristics. | The Display Inspection Plan: Characteristic Overview screen displays. |  |
| 5 | Review the Inspection Characteristics | The assigned Master Inspection Characteristics is Surface | You have now reviewed the inspection characteristics for which data has to be maintained later. |  |

#### Display Quality Technician Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, you can display an overview of open inspection lots via the overview page for quality technicians.

Prerequisite

The goods receipt from production order was posted for the configurable material directly to quality inspection stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Technician Overview (F2361). | The Quality Technician Overview (F2361) screen displays.You can get an overview of the inspection lots with open results recording and the inspection lots without an inspection plan. |  |

#### Display Open Inspection Lots

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection lot is used to record the results of the inspection operation. In this optional step, the references to the Goods Receipt and Production Order are verified as well as the sample size used for quality inspection reviewed.

Prerequisite

In this scope item, the inspection lot is created automatically upon goods receipt for the production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment. |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App. | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots (F2343) screen displays. |  |
| 3 | Filter Fields | Make the following entries and choose Go.Plant: 3310Material: AVC_E2E_ROBOTMaterial Document: Obtained from previous step | If Material Document isn't displayed in the Filters, choose Adapt Filters. On the popup screen Adapt Filters, find Inventory Management and choose More Filters. Select Material Document and choose OK. Choose Go. |  |
| 4 | Select the Corresponding Inspection Lot. | In the inspection lot list, select the inspection lot. |  |  |
| 5 | Check Inspection Lot. | In the Origin tab, verify the referenced production order and material document. | The production order number and material document number from which the inspection lot originates are displayed. |  |
| 6 | Check Inspection Lot – Quantities. | Under Origin , check the sample size. | The size of the sample for quality inspection is displayed. |  |

#### Display Inspection Methods

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection method is reviewed with attached document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Inspection Methods (F0311A). | The Inspection Method screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Inspection Method: SURFACE |  |  |
| 4 | Select Inspection Methods | In the Inspection Methods list, click the Inspection Method Surface. | Inspection Method is displayed. |  |

#### Record Inspection Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The quality technician executes the quality inspection and records inspection results for the inspection lot.

Procedure

Record Inspection Results for one Inspection Lot

If inspection results shall be recorded for one or only a few inspection lots, execute the following process flow:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log Onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A) | The Record Inspection Results screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Material: AVC_E2E_ROBOTOrder: from previous step. | If Order is not displayed in the Filters, please choose Filters. On the popup screen Filters, find Production and choose More Filters . Select Order and choose OK. Choose Go. |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot.Choose Record Multiple Results.Select the Inspection Characteristics and choose Edit. |  |  |
| 5 | Enter Inspection Result | In tab Results press Add/Add Row in case no line item for results recording is present.Depending on the inspection result, select one of the following two options:Positive ResultSuperficie: Code Group - Code SURFACE 0020 (Smooth)Negative ResultSuperficie: Code Group - Code SURFACE 0010 (Rough)Inspection Unit No: <serial number of inspected material> | For the qualitative characteristic (surface) the search help is needed to select a value.The valuation and close are performed automatically, and the status is set to Valuated.The default number of inspected objects is calculated based on the sample size reviewed in an earlier step. The number of inspected objects can be manually changed. As well a number of nonconforming objects can be maintained directly in the respective fields for every inspection characteristic. |  |
| 6 | Save Inspection Lot | Choose Save.Note Depending on sampling procedure, manual valuation might be required after saving inspection results.In this case return to inspection objects screen after results recording, choose Edit and manually set valuation status to accepted or rejected, depending on inspection result. | The inspection lot is saved. QM Inspection for manufactured goods has been performed and result recorded. |  |

#### Display Quality Engineer Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the inspection lot depending on the inspection result. As an optional entry point for making this usage decision, you can use the app Quality Engineer Overview (F2360). Furthermore, the Quality Engineer Overview (F2360) app displays inspection lots without an inspection plan (e.g. if automatic assignment of an inspection plan is not set up in the material master or if automatic assignment failed), inspection lots without usage decision, inspection lots ready for usage decision. If negative inspection results are recorded, you can check the detect details in app Manage Defects (F2649) directed from the app Quality Engineer Overview (F2360) via the cards Inspection Lots with Defects, Top Defective Materials, or Top Defects.

|  |
| --- |
| Caution For this scope item example, auto-defect recording is performed in quality inspection for goods receipt (End-Product Control) because deviations shall be tracked as defects later. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Engineer Overview (F2360). | The Quality Engineer Overview (F2360) screen displays. |  |
| 3 | In Card: Inspection Lots without Inspection Plan choose one entry (optional) |  | Assign missing data and ensure automatic inspection plan determination for further usage. |  |
| 4a | In Card: Select Inspection Lots Without Usage Decision (Optional) | Choose card Inspection Lots Without Usage Decision | You can process further as described in [Make Usage Decision](#unique_66) [page ] 92. |  |
| 4b | Select the Corresponding Inspection Lot you have created before (optional) | In the inspection lot list, select the inspection lot. | The Usage Decision screen displays. |  |
| 4c | Select one of the Inspection Lot by Results Recording Status (Optional) | Select one of the Inspection Lot by Results Recording Status (Optional) | Alternative Entry to [Make Usage Decision](#unique_66) [page ] 92. |  |
| 5 | Select Card Inspection Lots Ready for Usage Decision (optional) |  | All inspection lots with positive results get collectively an accepted usage decision (e.g. defaulted by A1) when pressing button Make Quick Usage Decision. |  |
| 6 | In Card: Inspection Lots with Defects (optional) | (In case negative inspection results have been recorded) Select one of the inspection lot origins, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 7 | In Card: Top Defective Materials (optional) | (In case negative inspection results have been recorded) Select one of the materials inspected, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 8 | In Card: Top Defects (optional) | (In case negative inspection results have been recorded) Select one of the defect codes recorded, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. |  |  |

#### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the material depending on the inspection result. This process step shows you how to make usage decision.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Usage Decision (QA11). | The Record Usage Decision: Initial screen displays. |  |
| 3 | Enter Inspection Lot number | On the Record Usage Decision: Initial Screen, make the following entry:Inspection Lot: <your Inspection Lot number from previous step>Choose Continue. | The Record Usage Decision: Characteristic Overview screen appears, and your inspection lot is displayed. |  |
| 4 | Display Defects | Check the details of defects on the Defects tab. | Only available if you have recorded a Negative result. |  |
| 5 | Attach a Document | On the Documents tab, choose Add, select the path and add the document. | For example, to upload pictures to visualize the defect. |  |
| 6 | Enter Usage Decision Code | On the Characteristics tab, in the Usage Decision section, depending on the inspection result, select one of the following entries as the UD code:Positive ResultA1 - AcceptedNegative ResultR1 - Rejected |  |  |
| 7 | Save Usage Decision | Choose Save. |  |  |

#### Display Material Stock after Usage Decision

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material (F1076) screen displays. |  |
| 3 | Enter Selection Fields | Make the following entry and choose Enter.Material: AVC_E2E_ROBOT |  |  |
| 4 | Check Stock Quantity | Check the changed quantities of the Quality Inspection Stock, Unrestricted Use Stock (in case of positive usage decision) or Blocked Stock (in case of negative usage decision). | The stock quantities for Final Assembly material AVC_E2E_ROBOT are updated based on the quality inspection and respective usage decision of the previous steps. |  |

### Outbound Delivery Processing

#### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries (F0869A) screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 3310Planned Creation Date: <Delivery selection date>Sales Document: Sales order number created previously |  |  |
| 4 | Create Delivery | Select your sales order items and choose Create Deliveries. | Creation of a delivery is triggered. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays, delivery is created successfully. Delivery number displays on Deliveries tab. |  |

|  |
| --- |
| Note Depending on the scope item settings, the availability is checked at the delivery creation using the available inventory and replenishment lead time. Without sufficient stock, the created delivery has no confirmed quantities, and therefore does not start the warehouse management picking process. As soon as there is sufficient stock for delivery creation, the system creates a delivery with the starting of the picking process in warehouse management. |

To avoid open deliveries, ensure there is sufficient inventory quantity at the time for delivery creation. Additionally, you have the following options to restrict the creation of deliveries with no confirmed quantities.

You may increase the replenishment lead time which is used during the availability check (has to be larger than the selection period used for delivery creation).

You may change the customization settings for the incompleteness procedure for delivery creation, so that only complete deliveries may be saved.

You may change the customization settings for the used delivery-item-category. The Check quantity 0 field must be adapted to B = Situation Rejected with An Error Message.

|  |
| --- |
| Note With the Analyze Delivery Logs app, you can display an overview about the logs of all the deliveries which have been created in your system. You can filter by, for example, Created by and other additional settings. If you select the arrow on the right of each delivery log entry you can display the exact message type and text and also the related sales document. |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) |  |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery (VL02N) screen, enter the Delivery Number, and choose Continue.From the Outbound Delivery xxxxxxxx Change: Overview screen, choose Menu > Extras > Delivery Output > Output Control . | The Outbound Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Outbound Delivery: Output screen, select the line with the DELIVERY_PICK_LIST Output Type, and choose Display Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Pick List | From the preview of the document, choose Print. | The delivery pick list is printed. |  |

#### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to pick deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries, and choose Execute:Shipping Point/Receiving Pt: 3310Under the Picking Data tab, selectOnly Picking Without WM: X |  |  |
| 5 | Change Outbound Deliveries | From Day’s Workload for Picking, select your delivery number, and choose Change Outbound Deliveries. |  |  |
| 6 | Choose Enter | Enter the value in following field:Picked Qty: 1Choose Enter. |  |  |
| 7 | Save | Choose Save. | The delivery has been decided. |  |

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

Run this step if material is managed by Serial Numbers.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3 | Enter Outbound Delivery Number | In the Outbound Delivery field, enter the outbound delivery number, and choose Enter. |  |  |
| 4 | Navigate to Serial Numbers | On the Delivery XXXXXXXXX Change: Overview screen, choose Menu > Extras > Serial Numbers . |  |  |
| 5 | Maintain Serial Numbers | On the Maintain Serial Numbers screen, pick serial number created in production process of AVC_E2E_ROBOT. |  |  |
| 6 | Save Document | Choose Save. |  |  |

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods issues for delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entry and choose Execute.Shipping Point/Receiving Pt: 3310 |  |  |
| 4 | Post Goods Issue | Select your outbound delivery note, and choose Post Goods Issues.Select today’s date from the dialog box, and choose Continue. | A message confirms the goods issue has been posted. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery (VL03N) screen displays. |  |
| 3 | Issue Delivery Output | In the Outbound Delivery field, enter <Outbound Delivery Number>, and choose Continue.On the Delivery xxxxxxxx Display: Overview screen, choose Extras > Delivery Output > Output Control. | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery Note, and choose Display Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

### Accounts Receivable

#### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you handle the billing.

Create Billing Document

Table 3: Overview

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings, you can make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for billing due list | In the search condition, use criteria if necessary. | Sales document(s) display in the result. |  |
| 5 | Select item(s) for billing | Select row(s) of SD Document created previously and choose button Create Billing Documents. | The Create Billing Document screen displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, for example current date, then press button OK. | The draft billing document with TMP xxxxxx displays. |  |
| 7 | Save Billing Document | On the Manage Billing Document screen, choose Save.The draft version billing document with TMP xxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | The system generates an invoice for billing. |  |
| 8 | ODN Number | Check whether the ODN number is generated for the billing document. | ODN number is generated in the Reference field. |  |

|  |
| --- |
| Note When the bundling functionality in context of IFRS15 is tested you can see the financial document created in the IFRS ledger (Ledger Group 2L). |

Manage Billing Documents

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Document screen displays. |  |
| 3 | Search Billing Document | Enter the Billing document number recorded in previous step. Choose Enter. | The billing document created in previous step displays |  |
| 4 | Display Billing document | Select the billing document item, and choose Display. | The billing document displays. |  |
| 5 | Check Output Condition | Choose the last assignment block - Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT |  |
| 6 | Display Print Preview | Choose Preview. | Preview for PDF document displays. |  |
| 7 | Cancel Billing Document (Optional) | Select certain billing document and choose Cancel Billing Docs. | Message Billing Document Canceled displays. |  |
| 8 | Update New Attachment (Optional) | In the Edit mode, add, delete and update the attachments. Save your changes by pressing Save button in the footer bar. |  |  |
| 9 | Update New Text (Optional) | In the Edit mode, you can add, delete and update these texts. Save your changes by pressing Save button in the footer bar. |  |  |

#### Post Incoming Payments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the incoming payments from the customer.

For a payment of an invoice where a down payment is applied, the incoming payment amount should be the remainder invoice balance (the remainder invoice balance is the invoice value less the down payment to be applied).

Prerequisites

Invoices are posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post Incoming Payments (F1345).Note For some countries, if withholding tax is to be posted during payment, use the Post Incoming Payments for Japan - For Customers (FBZ1) app. | The Post Incoming Payments view displays. |  |
| 3 | Enter General Information | Make the following entries in the General Information area:Company Code : 3310Posting date : dateJournal Entry date : dateValue date : today’s dateJournal Entry Type : DZ (Customer Payment) |  |  |
| 4 | Enter Bank Data | Make the following entries in the Bank data area.G/L Account : 11001060House Bank/Account ID : AEBK1/AEAC1 or AEBK2/AEAC2Amount : customer invoice amountNote If the incoming payment is part of a down payment, enter the remainder invoice balance amount, which is the invoice value less the down payment amount to be applied.Currency : AED |  |  |
| 5 | Enter Open Items | Make the following entry:Customer Account : 33100001Choose the Propose Items button. | The open items are displayed in the bottom half of the view. |  |
| 6 | Clear Items | Choose Items to Clear by choosing the Clear button in last item column. | The selected item is transferred to view Items to be Cleared. |  |
| 7 | Down Payment | Note Only execute this step if the payment is for an invoice where a down payment will be applied.In the Items to Be Cleared column, Allocated Amount, enter the remainder invoice balance amount, which is the invoice value less the down payment amount to be applied.Choose Enter. | The balance is zero and the document can be posted. |  |
| 8 | Post Entries | Choose Post. | The Activated dialog box displays details of document number generated. |  |
| 9 | Post on Account | Repeat steps 1–4. |  |  |
| 10 | Enter Data | Choose Post on account and enter the following:Account Type : CustomerCustomer : 33100001Credit Amount : same amount as in step 4. |  |  |
| 11 | Save | Choose Post. | Document is posted. |  |

### Accounts Payable

#### Create Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the supplier invoice with PO/GR relation.

Additionally, it is possible to insert a note in multiple languages when creating a supplier invoice via app Create Supplier Invoice. The note can be saved when holding, parking, saving, or posting the invoice, and it can be read when displaying the invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Supplier Invoice (F0859). | The Create Supplier Invoices screen is displayed. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount: <XXX>Currency: AEDInvoice Date: <Today>Posting Date: <Today>Reference: <XXX>(reference invoice number from invoicing party)Invoice Party: 33300001Exchange Rate: <XXX> | The Exchange Rate should be changed from AED in EUR according to the customizing settings. The Exchange Rate is changeable. |  |
| 4 | Enter Purchasing Document References | Add references in section Purchasing Document References.Make the following entries (use a PO you created previously).Reference Document Category: Purchase Order/Scheduling AgreementPurchase Order/Scheduling Agreement: <PO number> | All items of the referenced Purchase Order are added to the Invoice Items section. |  |
| 5 | Select Invoice Items | Select the Invoice Items you want to create invoice for. | You should see material items and delivery costs items, which refer to the entered purchase order document. Check if items for planned delivery costs have an item text. |  |
| 6 | Check Invoice Items Data | Check Amount, Quantity and Tax Code (there may already be a tax code that was copied from the purchase order). | The Amount, the Quantity, the Tax Code are consistent. |  |
| 7 | Check Tax Code | In the Tax section, check if there is tax code information and enter the tax amount if the tax rate is greater than zero. | In the Tax area, you should see the same tax codes as in the items. If there is no tax, specify that the tax code is <Input Tax Code>. |  |
| 8 | Block Invoice on Item Level (Optional) | Choose the invoice item arrow on the right side of the item to navigate to the item details.On the next screen, set flag for Manually Blocked. Choose Check. On the lower part of the details screen, the Blocking Reasons section shows Manual. Choose Back to Supplier Invoice to get back to the previous screen. | The item is blocked with a blocking reason. |  |
| 9 | Check Balance | The system automatically calculates tax amount, which is item amount multiplied by tax rate. Check the balance (difference between the calculated amount and the gross amount you entered in step 3) on the upper left corner. | The balance should be zero (or within the defined tolerance). |  |
| 10 | Simulate Supplier Invoice and Check Messages | Choose Simulate.You can check the simulation results in Overview and Details area. | The Supplier Invoice is simulated. |  |
| 11 | Post Invoice | Choose Post. | The invoice is posted. The system message is shown. |  |

#### Post Outgoing Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can post outgoing payments either manually or automatically. The manual posting process is described in the following example. The manual outgoing payment generated in this step does not go through an approval process and does not create a payment medium.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post Outgoing Payments (F1612). | The Post Outgoing Payments (F1612) view displays. |  |
| 3 | General Information | Make the following entries:General Information sectionCompany Code: 3310Posting Date: <Today's date>Journal Entry Date: <Today's date>Value Date: <Today's date>Reference (optional): <reference>Journal Entry Type: KZHeader Text: <header text>Bank Data sectionHouse Bank / Account: AEBK1/AEAC1G/L Account: 11001000Amount / Currency: <amount to pay on existing invoice>, for example, 119,00AEDFees: OptionalAssignment: OptionalExchange Rate: OptionalAmount / CCode Currency: Optional | A list of open items is displayed in the Open Items \| Standard section. |  |
| 4 | Open Item Selection | In the Open Item Selection section, make the following entry:Supplier Account: 33300001and choose the Show Items button. |  |  |
| 5 | Select/Deselect | Select an item to pay, and in the Clear column, choose Clear. | The item to pay transfers to the Items to be Cleared / Standard section. |  |
| 6 | Post | Choose Post.Note The generated payment does not require approval. | The system displays Journal entry xxxxxxxxxx was successfully posted in company code3310 notification. |  |
| 7 | Display | To view the posted document, choose Display. | The posted document is displayed. |  |
| 8 | Back | Choose the Back button. | The system displays Journal entry has already been posted. You can now post a new payment notification. |  |
| 9 | Dismiss notification | Choose OK to dismiss the notification. |  |  |

## Appendix

### Preceding Processes

The following processes and conditions can proceed this process.

| Process | Business Condition |
| --- | --- |
| BD6 – Basic Credit Management | Follow the procedure for Set Credit Limit process steps in the Basic Credit Management (BD6) scope item. |

### Succeeding Processes

The following processes and conditions can succeed this process.

| Process | Business Condition |
| --- | --- |
| Event-Based Production Cost Posting (3F0) | This procedure updates work-in-process calculation, overhead calculation, and variance calculation by linking the posting to the events.Start from CE2105, the default Best Practice content is based on event-based result analysis for new customer install and add new country only, rather than previous period-end posting. For existing customers (who activated content before 2105), the default remain unchanged to Period-End Closing – Plant BEI till customer makes the decision to switch. For migration to Event based from Periodic please refer [Production Settlement in Parallel Ledgers](https://help.sap.com/viewer/4032610758dc437089f0c28320eec93f/LATEST/en-US/e49a3770f22547a392455154f3eef6e2.html). If you are still using period-end posting, you may need to refer to non-standard Scope Item BEI - Period-End Closing – Plant. |
| Accounts Payable (J60) | Complete the following activities described in the test script:Payment RunPost Outgoing Payment |
| Accounting and Financial Close (J58) | Dispose of the inventory by returning to the vendor. Do not process any other activities in this document after running the external process.Using the master data from this document, complete the following activities described in the test script:Run the test script in its entirety, using the master data from this test script document. |
| Real-Time Reporting and Monitoring for Procurement (1JI) | The Procurement Overview Page gives the Purchaser the most important and relevant information at a glance – instead of navigating through many different transactions and reports.The global filter helps the Purchaser to focus the entire Procurement Overview Page to view all information according to specific suppliers, material groups, purchasing groups, and more.Using contextual navigation, the Purchaser can immediately act upon the displayed information by accessing the app or the object instance or get more detailed information in the corresponding KPI Drill-Downs. |
| Core Inventory Management (BMC) | Complete the following activities:Perform the selected step you want to perform for the Blocked stock. |
| Sales Order Fulfillment Monitoring and Operations(Optional) (BKK) | This scope item describes the collection of periodic activities, such as day ending activities or legal requirements.Using the master data from this document, complete all the activities described in the Test Script of the scope item: Sales Order Fulfillment Monitoring and Operations (BKK) (Chapters Review Sales Documents blocked for billing , Review Billing Due List, Review Log of collective invoice creation and Review List Blocked (for accounting) Billing Documents). |

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
- related-to :: [[02-business-partner-and-product-master-data/set-up-configurable-model-using-variant-configuration-22t-ae-test-scri]]
- related-to :: [[12-production-and-manufacturing/test-script-make-to-order-production-with-variant-configuration-1yt-ae]]
- related-to :: [[12-production-and-manufacturing/test-script-make-to-stock-production-with-variant-configuration-21d-ae]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/55E_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 185,339 chars in the whole document
