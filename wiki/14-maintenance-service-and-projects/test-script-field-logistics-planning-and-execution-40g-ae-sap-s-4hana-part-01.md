---
id: 14-maintenance-service-and-projects/test-script-field-logistics-planning-and-execution-40g-ae-sap-s-4hana-part-01
title: "Test Script: Field Logistics Planning and Execution (40G_AE) - SAP S/4HANA Cloud Public Edition (40G_S4CLD2608_BPD_EN_AE) — part 1 of 2"
description: "SAP test script for scope item 40G: field logistics supply (SP11-SP14) between base and remote plants, goods receipt/reversal, quality, and returns, in Fiori apps."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/field-logistics]
aliases: []
keywords: [Field Logistics Planning and Execution, field logistics, supply processes, dual plant setup, single plant setup, maintenance orders, goods receipt, goods receipt reversal, stock transport orders, field logistics returns]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/40G_S4CLD2608_BPD_EN_AE.docx#lines-1-2554"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-991
topic: 14-maintenance-service-and-projects/field-logistics
language: EN
part: 1/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Field Logistics Planning and Execution (40G_AE) - SAP S/4HANA Cloud Public Edition (40G_S4CLD2608_BPD_EN_AE) — part 1 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/40G_S4CLD2608_BPD_EN_AE.docx`, part 1 of 2 (lines 1–2554 of the extracted text), extracted with `mammoth`. Grouped under **Field Logistics Planning and Execution** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Field Logistics Planning and Execution (40G_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232854282)

[2 Prerequisites 5](#_Toc232854283)

[2.1 System Access 5](#_Toc232854284)

[2.2 Roles 5](#_Toc232854285)

[2.3 Master Data, Organizational Data, and Other Data 7](#_Toc232854286)

[2.4 Business Conditions 8](#_Toc232854287)

[2.5 Additional Manual Configuration 9](#_Toc232854288)

[2.6 Preliminary Steps 10](#_Toc232854289)

[2.6.1 Manage Authorizations for Creating Additional Documents 10](#_Toc232854290)

[2.6.2 Create Technical Object 10](#_Toc232854291)

[3 Overview Table 12](#_Toc232854292)

[4 Test Procedures 14](#_Toc232854293)

[4.1 Dual Plant Setup 14](#_Toc232854294)

[4.1.1 Create Maintenance Request 15](#_Toc232854295)

[4.1.2 Screen Maintenance Request 16](#_Toc232854296)

[4.1.3 Create Maintenance Order 17](#_Toc232854297)

[4.1.4 Approve Maintenance Order (Optional) 23](#_Toc232854298)

[4.1.5 Release Maintenance Order 23](#_Toc232854299)

[4.1.6 Run Material Requirements Planning (MRP) at Remote Plant and Base Plant 25](#_Toc232854300)

[4.1.7 Convert Purchase Requisition to Purchase Order 26](#_Toc232854301)

[4.1.8 Check for Automatically Created Inbound Delivery from Purchase Order 29](#_Toc232854302)

[4.1.9 Post Goods Receipt at Base Using 107 Movement Type Two-step GR Process (Optional) 31](#_Toc232854303)

[4.1.10 Post Goods Receipt at Base Plant 32](#_Toc232854304)

[4.1.11 Display Open Inspection Lots - QM Active (Optional) 41](#_Toc232854305)

[4.1.12 Record Inspection Results - QM Active (Optional) 42](#_Toc232854306)

[4.1.13 Record Usage Decision - QM Active 43](#_Toc232854307)

[4.1.14 Create Putaway Warehouse Tasks (Optional) 45](#_Toc232854308)

[4.1.15 Confirm Warehouse Tasks 47](#_Toc232854309)

[4.1.16 Create Nested Handling Unit (Optional) 48](#_Toc232854310)

[4.1.17 Check Automatically Created Stock Transport Order 49](#_Toc232854311)

[4.1.18 Update/Check Stock Transport Order 50](#_Toc232854312)

[4.1.19 Check Automatically Created Outbound Delivery 51](#_Toc232854313)

[4.1.20 Create Replenishment Delivery for Stock Transport Order 52](#_Toc232854314)

[4.1.21 Update / Check Outbound Delivery 53](#_Toc232854315)

[4.1.22 Remove Hold from Maintenance Order (Optional) 54](#_Toc232854316)

[4.1.23 Pack Items into Handling Units (Optional) 55](#_Toc232854317)

[4.1.24 Create Pick Warehouse Tasks 56](#_Toc232854318)

[4.1.25 Confirm Pick Warehouse Tasks 58](#_Toc232854319)

[4.1.26 Post Goods Issue 59](#_Toc232854320)

[4.1.27 Post Goods Receipt at Remote Plant 59](#_Toc232854321)

[4.1.28 Post Goods Issue for Maintenance Order 62](#_Toc232854322)

[4.2 Single Plant Setup 64](#_Toc232854323)

[4.2.1 Create Maintenance Request 64](#_Toc232854324)

[4.2.2 Screen Maintenance Request 65](#_Toc232854325)

[4.2.3 Create Maintenance Order 66](#_Toc232854326)

[4.2.4 Approve Maintenance Order (Optional) 69](#_Toc232854327)

[4.2.5 Release Maintenance Order 70](#_Toc232854328)

[4.2.6 Run Material Requirements Planning (MRP) at Single Plant - Purchase Requisition Creation 71](#_Toc232854329)

[4.2.7 Convert Purchase Requisition to Purchase Order 72](#_Toc232854330)

[4.2.8 Check for Automatically Created Inbound Delivery from Purchase Order 74](#_Toc232854331)

[4.2.9 Post Goods Receipt at Base Using 107 Movement Type Two-step GR Process (Optional) 76](#_Toc232854332)

[4.2.10 Post Goods Receipt at Single Plant 77](#_Toc232854333)

[4.2.11 Display Open Inspection Lots - QM Active (Optional) 82](#_Toc232854334)

[4.2.12 Record Inspection Results - QM Active (Optional) 84](#_Toc232854335)

[4.2.13 Record Usage Decision - QM Active (Optional) 85](#_Toc232854336)

[4.2.14 Create Putaway Warehouse Tasks (Optional) 87](#_Toc232854337)

[4.2.15 Confirm Warehouse Tasks 88](#_Toc232854338)

[4.2.16 Post Goods Issue for Maintenance Order 89](#_Toc232854339)

[4.2.17 Direct Purchase for Single Plant 90](#_Toc232854340)

[4.3 Goods Receipt Reversal (Optional) 91](#_Toc232854341)

[4.3.1 Goods Receipt Reversal Process 91](#_Toc232854342)

[4.3.1.1 Warehouse Management Active in Base Plant 92](#_Toc232854343)

[4.3.1.2 Warehouse Management Inactive in Base Plant 95](#_Toc232854344)

[4.4 View Supply Process Document Flow 98](#_Toc232854345)

[4.5 Physical Inventory Process for Field Logistics Materials at Base Plant 99](#_Toc232854346)

[4.6 Physical Inventory Process for Field Logistics Materials at Remote Plant 100](#_Toc232854347)

[4.7 Field Logistics Returns Process 100](#_Toc232854348)

[4.7.1 Return by Maintenance Order 100](#_Toc232854349)

[4.7.1.1 Return to Inventory and Create Return Draft 100](#_Toc232854350)

[4.7.2 Initiate Returns by Product 103](#_Toc232854351)

[4.7.2.1 Create Replenishment Delivery 104](#_Toc232854352)

[4.7.2.1.1 Replenishment Delivery Using Initiate Returns by Product App 104](#_Toc232854353)

[4.7.2.1.2 Replenishment Delivery using My Purchase Orders Due for Delivery App 111](#_Toc232854354)

[4.7.2.2 Change the Returns STO - Confirmation Control key (Optional) 112](#_Toc232854355)

[4.7.2.3 Pick and Pack Delivery 113](#_Toc232854356)

[4.7.2.4 Print Label (Optional) 116](#_Toc232854357)

[4.7.2.5 Dispatch Goods 117](#_Toc232854358)

[4.7.2.6 Receive Goods at Base 118](#_Toc232854359)

[4.7.2.7 Verify Returns Process Flow (Optional) 122](#_Toc232854360)

[4.7.2.8 Confirm Warehouse Tasks 123](#_Toc232854361)

[4.7.2.9 Manage Request for Inspecting Items (Optional) 124](#_Toc232854362)

[4.7.2.9.1 Assign Inspection Plan and Record Inspection Results 124](#_Toc232854363)

[4.7.2.9.2 Record Inspection Results (Optional - Warehouse Managed Scenario) 126](#_Toc232854364)

[4.7.2.9.3 Record Usage Decision 127](#_Toc232854365)

[4.7.2.10 Create and Confirm Warehouse Tasks for Picking 129](#_Toc232854366)

[4.8 Technically Complete Maintenance Order 130](#_Toc232854367)

## Purpose

Overview

This scope item supports the logistics between a supplying base and remote locations – receiving products needed for maintenance operations at the base and forwarding them to the remote, as well as return from the remote back to the base.

The supply process accommodates several scenarios, including situations where stock is available both at the remote location and the base, only at the base, or solely at the remote site. Additionally, it supports direct purchase.

On the return side, the process addresses various scenarios such as returning items to base inventory, sending them back to the vendor, returning them for inspection, or for repair and recertification. It also includes provisions for temporary storage.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites to conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role.

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Maintenance Planner | SAP_BR_MAINTENANCE_PLANNER | Maintenance Planning | SAP_BR_MAINTENANCE_PLANNER |  |
| Material Planner - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC | Material Planning - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC |  |
| Maintenance Technician | SAP_BR_MAINTENANCE_TECHNICIAN | Maintenance Execution | SAP_BR_MAINTENANCE_TECHNICIAN |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Quality Technician | SAP_BR_QUALITY_TECHNICIAN | Quality Inspection | SAP_BR_QUALITY_TECHNICIAN |  |
| Quality Engineer | SAP_BR_QUALITY_ENGINEER | Quality Engineering | SAP_BR_QUALITY_ENGINEER |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Supply Chain Analyst (IOG) | SAP_BR_SC_ANALYST_IOG | Field Logistics Planning and Execution / Transfers - Field Logistics / Field Logistics - Tracking | SAP_BR_SC_ANALYST_IOG |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk (EWM) | SAP_BR_WAREHOUSE_CLERK_EWM | Warehouse Office | SAP_BR_WAREHOUSE_CLERK_EWM |  |
| Warehouse Clerk (IOG) | SAP_BR_WAREHOUSE_CLERK_IOG | Field Logistics Planning and Execution / Transfers - Field Logistics / Field Logistics - Tracking | SAP_BR_SC_ANALYST_IOG |  |
| Warehouse Operative (EWM) | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Warehouse Floor | SAP_BR_WAREHOUSE_OPERATIVE_EWM |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Business Network Integration / Business Network Integration - Concur Integration / Business Network Integration - Output Control / Business Network Integration - Data Replication / Configuration Expert - Business Network Integration Cross Applications | SAP_CORE_SPT_INT_PC / SAP_CON_SPT_CONCUR_INT_PC / SAP_OC_SPT_INT_PC / SAP_CA_SPT_DATA_REP_PC / SAP_CA_SPT_BUS_NETWORK_INT_PC |  |
| Receiving Specialist (IOG) | SAP_BR_RCVG_SPECIALIST_IOG | Field Logistics Planning and Execution / Transfers - Field Logistics / Field Logistics - Tracking | SAP_BR_SC_ANALYST_IOG |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company is created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Follow the steps mentioned in the setup instructions for this scope item.

Use your own master data to go through the test procedure. You can also use the following sample data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 | Company Code 3310 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Plant | FORP | Plant 2 AE (Remote Plant) | Flex.Org App extension |
| Storage Location | FORN | Std. storage 1 | Flex.Org App extension in Plant 1 AE |
| Storage Location | FORH | Std. storage 2 | Flex.Org App extension in Plant 1 AE |
| Shipping Point | FORP | Shipping Point FORP | Flex.Org App extension |
| Sales Organization | FORP | Sales Organization in Company 3310 | Flex.Org App extension |
| Purchase Organization | FLPO | Purchase Organization in Company 3310 | Flex.Org App extension |
| Plant | FOBP | Plant 3 AE (Base Plant) | Flex.Org App extension |
| Storage Location | FOBW | Std. storage 1 | Flex.Org App extension in Plant 1 AE |
| Shipping Point | FOBP | Shipping Point FOBP | Flex.Org App extension |
| Sales Organization | FOBS | Sales Organization in Company 3310 | Flex.Org App extension |
| Material | FLOG-SP11 | Material stockable at Base and Remote | Refer the section on master data extension in the Setting Up Field Logistics Preventive Maintenance (40G) guide |
| Material | FLOG-SP12 | Material stockable at Base Only | Refer the section on master data extension in the Setting Up Field Logistics Preventive Maintenance (40G) guide |
| Material | FLOG-SP13 | Material stockable at Remote Only | Refer the section on master data extension in the Setting Up Field Logistics Preventive Maintenance (40G) guide |
| Material | FLOG-SP14 | Material not stockable at Base and Remote | Refer the section on master data extension in the Setting Up Field Logistics Preventive Maintenance (40G) guide |
| Supplier | BP1001650 | External Vendor | Refer the section on master data extension in the Setting Up Field Logistics Preventive Maintenance (40G) guide |

### Business Conditions

You have completed the steps described in the following master data scripts:

| Scope Item | Business Condition |
| --- | --- |
| 4HI - Proactive Maintenance |  |
| 4HH - Reactive Maintenance |  |
| BME - Stock Transfer with Delivery |  |
| 2TX - Direct Procurement with Inbound Delivery |  |
| J45 - Procurement of Direct Materials |  |
| 3BR - Warehouse Inbound Processing |  |
| 3BS - Warehouse Outbound Processing |  |
| BNQ - Create Quality Inspection Plan - MDS |  |
| BNY - Create Quality Management Attributes for Material/Product Master - MDS |  |
| BF5 - Create Quality Info Record - MDS |  |
| 1FM - Quality Management in Procurement |  |
| 3M0 - Quality Management in Warehousing |  |
| BML - Physical Inventory – Inventory Count and Adjustment |  |
| 3BX - Warehouse Physical Inventory |  |
| BNZ - Create New Open MM Posting Period - MDS | Posting period is up to date using Create New Open MM Posting Period - MDS |
| BMR - Scheduling Agreements in Procurement |  |
| BMK - Return to Supplier |  |
| 1NJ - Responsibility Management |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/75bdb8ae21fd82c476fa58bf6120516c)

### Preliminary Steps

#### Manage Authorizations for Creating Additional Documents

Supply processes SP13 and SP14 require the creation of additional follow-on documents at various stages of the end-to-end process, such as:

- Outbound Delivery for SP13 process.
- Stock Transport Order and Outbound Delivery for SP14 process.

Additional authorization is required for subsequent document creation, for the following cases:

- Non quality managed material when goods receipt for SP13 and SP14 processes are not performed using Process Receipts application.
- Quality managed material when usage decision is performed for SP13 and SP14 processes.

Before executing SP13 and SP14 processes, contact your administrator for managing the authorizations for the following roles (in cases required):

- Warehouse Clerk
- Warehouse Clerk EWM
- Quality Engineer
- Receiving Specialist

For more information, refer to [Catalogs for Creating Additional Documents](https://help.sap.com/docs/SAP_S4HANA_CLOUD/74ffc024fd794eeca49dc8ffe7f9870d/079d86b60a554d71a13428a0b6e8e6e7.html).

#### Create Technical Object

If the maintenance order type is used is YA01 – Reactive Maintenance, you require a technical object to create a maintenance request.

1. Log on to SAP Fiori Launchpad with user MAINTENANCE_PLANNER.
2. Access the app Create Technical Object (W0029).
3. Enter the Technical Object type- Functional Location/ Equipment, click Continue.

For example, choose Functional Location.

1. Enter the following:
    - Technical Object- FORP-TO
    - Technical Object Category- M – Technical system – standard

Click on Continue.

1. Go to Organizational Data tab.

Enter the following:

-
    1. Planning Plant- FORP
    2. Company code- 1710
    3. Maintenance Work center- FORP-PM

1. Choose Save.

Note down the technical object name.

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Create Maintenance Request | Maintenance Planner | Create Maintenance Request (F1511A) | Maintenance request is created. |
| Screen Maintenance Request | Maintenance Planner | Screen Maintenance Requests (F4072) | Maintenance request is accepted. |
| Create Maintenance Order | Maintenance Planner | Create Maintenance Order | Maintenance order is created for the malfunction report. |
| p |  |  |  |
| Approve Maintenance Order (Optional) | Maintenance Planner | My Inbox - All Items (F0862) | Maintenance order is approved. |
| Release Maintenance Order | Maintenance Planner | Change Maintenance Order (IW32) | Maintenance order is released for execution. |
| Run Material Requirements Planning (MRP) | Material Planner - External Procurement | Monitor Material Coverage - Net / Individual Segments (F2101A) | MRP is run for material at remote plant. |
| Create Stock Transport Order | Purchaser | Process Purchase Requisitions - Deprecated (F1048) | A stock transport order is created. |
| Run Material Requirements Planning (MRP) | Material Planner - External Procurement | Monitor Material Coverage - Net / Individual Segments (F2101A) | MRP is run for material at base plant. |
| Create Purchase Order from Purchase Requisition | Purchaser | Process Purchase Requisitions - Deprecated (F1048) | A purchase order is created. |
| Automatic Inbound Delivery Creation | Purchaser | Change Purchase Order - Advanced (ME22N) | Inbound delivery is created and distributed to warehouse. |
| Post Goods Receipt at Base Plant | Receiving Specialist (IOG) | Process Receipts - Stock and Non-stock items (F5316) | Goods receipt is performed. |
| Usage Decision for Quality Managed Material | Quality Engineer | Record Usage Decision (QA11) | Inspection lot is created. |
| Putaway Warehouse Task - Confirmation | Warehouse Clerk (EWM) | Change Inbound Deliveries - Deliveries (F1706) |  |
| Outbound Delivery Creation | Shipping Specialist | Change Outbound Delivery (VL02N) | For SP13 and SP14 processes outbound delivery is automatically created. |
| Pick Warehouse Task - Creation and Confirmation | Warehouse Clerk (EWM) | Change Outbound Delivery (VL02N) | The warehouse tasks are created. |
| Repack Handling Units | Warehouse Operative (EWM) | Pack Handling Units - Advanced (/SCWM/PACK) | Handling units are repacked. |
| Post Goods Issue from Base plant | Warehouse Clerk (EWM) | Post Goods Issue (MIGO_GI) | Goods issue is posted. |
| Post Goods Receipt at Remote plant | Warehouse Clerk (EWM) | Post Goods Receipt for Purchasing Document (F0843) | Goods receipt is posted. |
| Post Goods Issue to Maintenance Order | Warehouse Clerk | Post Goods Issue (MIGO_GI) | Goods issue is posted and material document is created. |
| Technically Complete Maintenance Order | Maintenance Planner | Find Maintenance Orders - Completion (F2175) | The maintenance order is technically completed after the required maintenance work has been performed. |

The returns process steps in this scope item are provided in the table below.

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Initiate Returns by maintenance order | Warehouse Clerk (IOG) | Initiate Returns - By maintenance order (F4682) | Returns STO is created for the maintenance order. |
| Initiate Returns by product | Warehouse Clerk (IOG) | Initiate Returns - By product (F4252) | Returns STO is created with the respective details. |
| Display the Returns STO | Purchaser | Change Purchase Order - Advanced (ME22N) | View the returns STO. |
| Create Replenishment Delivery for the STO | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | Replenishment delivery is created. |
| Dispatch Goods to the Base | Warehouse Clerk (IOG) | Initiate Returns - By product (F4252) | Product is dispatched from remote location. |
| Receive Goods at the Base | Warehouse Clerk (IOG) | Process Cross-Plant Receipts (F4713) | Goods are received at the base and the returned products are processed. |

## Test Procedures

This section describes the test procedures for each process step that belongs to this scope item.

### Dual Plant Setup

The classic setup within Field Logistics defines a combination of a demand plant (remote location) and its default supply plant (base location) that is, it is a dual plant setup. The required items are either already stocked at the base or are procured by the base. The external supplier sends the items to the base plant, and they are then transferred from the base to the remote plant based on stock transport order (STO) and outbound deliveries. The dual plant process supports the following supply processes:

- SP11: Stock located at base and remote location

In this scenario, the availability of the material is first checked in remote plant. If the demand for the material cannot be attained by stock available at remote plant, a stock transport requisition is created and subsequently converted to a stock transport order for the base plant. MRP run at base plant checks the available stock, if the demand for the material is not fulfilled yet, a purchase requisition is created. This purchase requisition is subsequently converted to a purchase order to procure this material from an external vendor. The material is then received at the base plant and relevant warehouse and quality activities are performed.

If the selected version is V1 or V3, on saving the maintenance order stock transport requisition (STR) is automatically created at remote plant. Hence, MRP run at remote plant is not required for these versions. The stock is issued from the base plant to remote plant. When the goods reach the remote plant, it is received and issued against the maintenance order.

- SP12: Stock located at base location only

In this scenario, stock transport requisition is created from the maintenance order, which is subsequently converted to a stock transport order for the base plant.

Later, MRP run at base plant checks the available stock, if the demand for the material is not fulfilled yet, a purchase requisition is created. This purchase requisition is subsequently converted to a purchase order to procure this material from an external vendor. The material is then received at the base plant and relevant warehouse and quality activities are performed.

The stock is issued from the base plant to remote plant. When the goods reach the remote plant, it is received and issued against the maintenance order.

This supply process supports both quality and non-quality managed materials. For non-quality managed materials, you can enter the material as FLOG-SP12.

You can procure the SP12 materials using SP15 supply process with appropriate supply process version configuration. On saving the maintenance order, an STR is created instead of a PR. This is due to the special procurement key that is maintained as 45 in Material Master of SP12 materials. To use the flexibility of SP15 for these materials, you can remove the special procurement key 45 in the Material Master for the plant where this flexibility is required.

- SP13: Stock located at remote location only

In this scenario, the availability of the material is first checked in remote plant. If the demand for the material cannot be attained by stock available at remote plant, a stock transport requisition is created and subsequently converted to a stock transport order for the base plant. This conversion automatically creates a purchase requisition for the base plant, which is subsequently converted to a purchase order to procure this from external vendor. The material is received at the base plant; warehouse and quality relevant activities are performed.

If the selected version is V1 or V3, on saving the maintenance order STR is automatically created at remote plant. Hence MRP run at remote plant is not required for these versions.

The stock is issued from the base plant to remote plant. When the goods reach the remote plant, it is received and issued against the maintenance order.

- SP14: Direct purchase

In this scenario, purchase requisition is created from the maintenance order, which is subsequently converted to a purchase order for the base plant to procure this material from an external vendor. The material is then received at the base plant and relevant warehouse and quality activities are performed. The stock is issued from the base plant to remote plant. When the goods reach the remote plant, it is received and issued against the maintenance order.

|  |
| --- |
| NoteThese supply processes support both quality and non-quality managed materials.For non-quality managed materials, you can enter the material as FLOG-SP11.You can procure all the materials using SP15 supply process with appropriate supply process version configuration. On saving the maintenance order, an STR is created instead of a PR. This is due to the special procurement key that is maintained as 45 in Material Master of SP11 / SP12 / SP13 materials. To use the flexibility of SP15 for these materials, you can remove the special procurement key 45 in the Material Master for the plant for the material where this flexibility is required.The following procedures are not applicable for non-quality managed materials:[Display Open Inspection Lots - QM Active (Optional)](#unique_14) [page ] 41[Record Inspection Results - QM Active (Optional)](#unique_15) [page ] 42[Record Usage Decision - QM Active](#unique_16) [page ] 43Supply process determination is supported in maintenance orders created through maintenance plan scheduling, using both the Schedule Maintenance Plan (IP10) app and the Mass Schedule Maintenance Plan (IP30H and F2774) app. |

#### Create Maintenance Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is the initiation phase of maintenance where an employee creates a maintenance request. You can create a maintenance request using the Create Maintenance Request (F1511A) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Maintenance Request (F1511A). | The Create Maintenance Request screen is displayed. |  |
| 3 | Maintenance Request Creation | Enter the following:Technical Object: FORP-TO (created in [Create Technical Object](#unique_10) [page ] 10)Description: Example: FL Maintenance RequestPriority: Select a priority from the dropdown. Example: Medium. | Details are entered. |  |
| 4 | Save the Entries | Choose Submit. | Maintenance request is saved.Note down the maintenance request number. |  |

#### Screen Maintenance Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is the screening phase of the maintenance process. As a supervisor you have to review the maintenance request, change responsibility of the requests (if required) and take appropriate decision to proceed with request, reject or send back seeking more information.

You can review and accept the maintenance request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Screen Maintenance Requests (F4072) app. | The Screen Maintenance Request screen is displayed. |  |
| 3 | Filter | To filter the maintenance request created in previous section, enter the following.Planning Plant: FORPTechnical Object: FORP-TO.Choose Go. | Maintenance request is filtered and displayed under the Open tab. |  |
| 4 | Accept | Click Chevron to navigate to the maintenance request.Review the maintenance request, click Edit to make changes if needed.Save the changes.Choose Accept to accept the maintenance request. | Maintenance request is accepted. |  |

#### Create Maintenance Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Maintenance order is used to collect all the materials required to correct the malfunction in the remote plant. It also derives the supply process for a material in a plant, which defines how the material is stocked at remote and base plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Create Maintenance Order | Open the Create Maintenance Order app. | The Create Order screen is displayed. |  |
| 3 | Create Maintenance Order | On the Create Order screen, choose order type: Reactive Maintenance YA01.Header Notification: Enter the maintenance request created in previous section.Choose Continue. |  |  |
| 4 | Enter Details | On the Create Reactive Maintenance Order: %00000000001 screen, go to the General Data tab.In the Responsibilities section,Work Center: FORP-PM | Work center is entered. |  |
| 5 | Define the Operations to be Performed to Resolve the Malfunction | Go to the Operation Data tab. You can see the operation overview in the Operations table for operation 0010:The system calculates the duration of the operation based on the time you entered in Work field and on how many people you scheduled in the number field to perform this operation. You have now made the required entries in the header data screen of the order. |  |  |
| 6 | Select Material for SP11 Supply Process | Select the operation 0010 and choose Material tab, below the maintenance request list in the screen.On the Materials tab, enter the following for each material:Note For non-quality managed materials, as an example you can provide the material as FLOG-SP11 for the respective supply process.Material: FLOG-SP11Quantity: 5 EAPlant: FORPNote For the SP11 process, both item category and procurement type are flexible. This flexibility can be achieved with the SSCUI configuration Maintain Supply process determination by Plant node by an appropriate version selection against each supply process.For more details on the SSCUI, view the setup instructions for this scope item (section Configure Field Logistics).To duplicate a material line in the list with all item data, choose Copy Material. You can then change specific fields in the copied line. | Item category should be defaulted to L and Field Logistics supply process should be defaulted to SP11 for the first line item.The available versions and variations for the SP11 process are provided here.SP11 version selected as blank: Standard SP11 Field logistics process: The item category is always set as Stock Item, the procurement type is configured as Blank. Hence, the MRP Run checks the availability in the remote plant and creates STR if needed.SP11 version selected as V1: The item category is always set as Stock Item and the procurement type is selected as STR. STR is automatically created on saving or releasing of the maintenance or-der.SP11 version selected as V2: The item category is configured as Blank. You can choose between item category Stock Item or Non-stock Item during maintenance order creation. If the selected item category is Stock Item (or it is left blank), the supply process is determined as SP11 and the settings from V2 apply. If the selected item category is Non-stock Item, the supply process is determined as SP15.The procurement type is configured as Blank for this version. Hence, the MRP Run checks the availability in the remote plant and creates STR if needed.SP11 version selected as V3: The item category is configured as Blank. Hence you can choose between item category Stock Item or Non-stock Item during maintenance order creation. If the selected item category is Stock Item, the supply process is determined as SP11 and the settings from V3 apply. If the item category is Non-stock Item, the supply process is determined as SP15.The procurement type is configured as STR. Hence, STR is automatically created on saving or releasing of the maintenance order.SP11 version selected as V5:Creating account assigned STR with item category N in maintenance order.The item category is configured as N (non-stock) and the supply process is determined as SP11 during maintenance order creation.The procurement type is configured as account assigned STR. Hence, STR is automatically created on saving or releasing of the maintenance order with account assignment category F. |  |
| 7 | Select Material for SP12 Supply Process | Select the operation 0010 and choose Materials tab, below the maintenance request list in the screen.On the Materials tab, enter the following for each material:Note For non-quality managed materials, as an example you can provide the material as FLOG-SP12 for the respective supply process.Material: FLOG-SP12Quantity: 5 EAPlant: FORPNote For the SP12 process, the item category is flexible and the procurement type is always STR. This flexibility can be achieved with the SSCUI configuration Maintain Supply process determination by Plant node by appropriate version selection against each supply process.For more details on the SSCUI, view the setup instructions for this scope item (section Configure Field Logistics).The available versions and its variations for SP12 process are provided here.To duplicate a material line in the list with all item data, choose Copy Material. You can then change specific fields in the copied line. | Item category should be defaulted to L and Field Logistics supply process should be defaulted to SP12 for the first line item.SP12 version selected as blank: Standard SP12 Field logistics process The item category is always set as Stock Item, the procurement type is STR. STR is automatically created on saving or releasing of the maintenance order.SP12 version selected as V1: The item category is configured as Blank. You can choose between item category Stock Item or Non-stock Item during maintenance order creation. If the chosen item category is Stock Item (or is left blank), the supply process is determined as SP12 and the settings for V1 apply. If the item category is Non-stock Item, the supply process is determined as SP15.The procurement type is configured as STR. Hence, STR is automatically created on saving or releasing of the maintenance order.SP12 version selected as V5:Creating account assigned STR with item category N in maintenance order.The item category is configured as N (non-stock) and the supply process is determined as SP12 during maintenance order creation.The procurement type is configured as account assigned STR. Hence, STR is automatically created on saving or releasing of the maintenance order with account assignment category F. |  |
| 8 | Select Material for SP13 Supply Process | Select the operation 0010 and choose Materials tab, below the maintenance request list in the screen.On the Materials tab, enter the following for each material:Note For non-quality managed materials, as an example you can provide the material as FLOG-SP13 for the respective supply process.Material: FLOG-SP13Quantity: 5 EAPlant: FORPNote For the SP13 process, both item category and procurement type are flexible. This flexibility can be achieved with the SSCUI configuration Maintain Supply process determination by Plant node by appropriate version selection against each supply process.For more details on the SSCUI, view the setup instructions for this scope item (section Configure Field Logistics).To duplicate a material line in the list with all item data, choose Copy Material. You can then change specific fields in the copied line. | Item category should be defaulted to L and Field Logistics supply process should be defaulted to SP13 for the first line item.The available versions and its variations for SP13 process are provided here.SP13 version selected as blank: Standard SP13 Field logistics process The item category is always set as Stock Item, the procurement type is configured as Blank. Hence, the MRP Run checks the availability in the remote plant and creates STR if needed.SP13 version selected as V1: The item category is always set as Stock Item and the procurement type is selected as STR. STR is automatically created on saving or releasing of the maintenance order.SP13 version selected as V2: The item category is configured as Blank. You can choose between item category Stock Item or Non-stock Item during maintenance order creation. If the chosen item category is Stock Item (or is left blank), the supply process is determined as SP13 and the settings from V2 apply. If the item category is Non-stock Item, the supply process is determined as SP15.The procurement type is configured as Blank for this version. Hence, the MRP Run checks the availability in the remote plant and creates STR if needed.SP13 version selected as V3: The item category is configured as Blank’. Hence, you can choose between item category Stock Item or Non-stock Item during maintenance order creation. If the selected item category is Stock Item (or is left blank), the supply process is deter-mined as SP13. If the selected item category is Non-stock Item, the supply process is determined as SP15.The procurement type is configured as STR. Hence, STR is automatically created on saving or releasing of the maintenance order.SP13 version selected as V5:Creating account assigned STR with item category N in maintenance order.The item category is configured as N (non-stock) and the supply process is determined as SP13 during maintenance order creation.The procurement type is configured as account assigned STR. Hence, STR is automatically created on saving or releasing of the maintenance order with account assignment category F. |  |
| 9 | Select Material for SP14 Supply Process | Select the operation 0010 and choose Materials tab, below the maintenance request list in the screen.On the Materials tab, enter the following for each material:Note For non-quality managed materials, as an example you can provide the material as FLOG-SP14 for the respective supply process.Material: FLOG-SP14Quantity: 5 EAPlant: FORPNote For the SP14 process, the item category is flexible and the procurement type is al-ways PR. This flexibility can be achieved with the SSCUI configuration Maintain Supply process determination by Plant node by appropriate version selection against each supply process.For more details on the SSCUI, view the setup instructions for this scope item (section Configure Field Logistics).To duplicate a material line in the list with all item data, choose Copy Material. You can then change specific fields in the copied line. | Item category should be defaulted to L and Field Logistics supply process should be defaulted to SP14 for the first line item.The available versions and its variations for SP14 process are provided here.SP14 version selected as blank: Standard SP14 Field logistics process The item category is always set as Stock Item, the procurement type is PR. PR is automatically created on saving or releasing of the maintenance order.SP14 version selected as V1: The item category is configured as Blank. You can choose between item category Stock Item or Non-stock Item during maintenance order creation. If the selected item category is Stock Item (or is left blank), the supply process is determined as SP14 and the settings for V1 apply. If the item category is Non-stock Item, the supply process is determined as SP15.The procurement type is configured as PR. Hence, PR is automatically created on saving or releasing of the maintenance order. |  |
| 10 | Enter Storage Location (Optional) | In storage location field, enter FORN(MM-IM managed storage location) | Storage location is updated. |  |
| 11 | Add Recipient Location (Optional) | Select the line item and under the column Recipient Location, press F4 from keyboard.User can choose the recipient location applicable for them. |  |  |
| 12 | Reservation / Purchase Requisition Creation Instance | From the maintenance order, the purchase requisition can be created collectively or individually.You can configure this for each plant / order type, as described in the setup instructions for this scope item.You can select the instance for stock transport requisition / purchase requisition creation for the supply processes.Select the required option from the dropdown list of Reservation/Purc.req column in component level from the Materials tab.Purchase requisitions can be created immediately on saving the maintenance order or when the order is released.Select the option From Release for all line items. | Reservation/Purc.req column is selected as From Release for all line items. |  |
| 13 | Hold on Shore Flag (optional) | Check hold on shore flag for all items that have to be held. You can maintain a hold indicator for one or more items.Hold On-Shore: XNote The flag Hold On-Shore is part of the Field Logistics functionality for holding and cross-docking. In case hold flag is not applicable for the line item a warning message is displayed. For necessary configuration and prerequisites for hold and cross-dock refer to the setup guide of scope item 40G, as well as the SAP documentation. | Hold flag is checked.Any further delivery of the related physical items to the offshore plant will be blocked until the hold flag is cleared. |  |
| 14 | Maintain Settlement Category | Select Costs tab and under Settlement Rules maintain a settlement category.For example:Settlement category: Cost CenterSettlement receiver: Choose from search help, like 17101701. | Settlement category is maintained. |  |
| 15 | Check Entries | Choose Check Entries on the top left corner of the screen. | Entries have been checked. |  |
| 16 | Save Order | Choose Save. | Order 4000XXX is saved. |  |
| 17 | Phase Control Check (optional) | Check the phase control status at header and operation level.Note Use of the phase control statuses TOH and TPOH is part of the Field Logistics functionality for holding and cross-docking. In case phase control is not setup properly the relevant control status will not be available but hold and cross-dock functionality will work as expected. For necessary configuration and prerequisites refer to the setup guide of scope item 40G, as well as the SAP documentation. | The phase control on header level should have the active status:TOH in case all components of the order have the flag Hold On-Shore setTPOH in case some components of the order have the flag Hold On-Shore setNeither, in case no components have the flag setThe phase control on operation level should have the active status:TOH in case all components of the operation have the flag Hold On-Shore setTPOH in case some components of the operation have the flag Hold On-Shore setNeither, in case no items have the flag set |  |
| 18 | Submit for Approval | In the Change Status dropdown on top left, select Submit for Approval. | Maintenance order is submitted for approval.The order goes for approval as per the workflow maintained.Note If there are no custom workflows maintained, order gets approved automatically. |  |

#### Approve Maintenance Order (Optional)

Purpose

You can approve the maintenance order from the My Inbox app.

|  |
| --- |
| Note This step involves Flexible Workflow which can be set up by the customer. Any agent configured in workflow can approve the maintenance order. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862) app. | The My Inbox app displays list of orders available for approval. |  |
| 3 | Approve / Reject Maintenance Order | On the My Inbox screen, select the workflow request for maintenance order, you can review information page which gives detail of maintenance order like general data, responsibilities, account assignment, cost, dates etc.Update comment in Comments section.Approve maintenance order and add decision note if required.Note If the maintenance order is rejected, it can be further processed with required details and can be sent for approval again. | Maintenance order is approved, and order will be removed from the list in My Inbox.Maintenance order is in Ready to Prepare phase. |  |

#### Release Maintenance Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The maintenance order is used to collect all costs for a maintenance task and to debit the cost center that incurred the costs using the settlement functions in the CO module (Controlling).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Change Maintenance Order app.Enter the order number and press Continue. | The Change Reactive Maintenance: 4XXXXXX screen displays. |  |
| 3 | Release and Save the Order | On the Change Reactive Maintenance screen, choose Set System Status.Choose Release from the Change Status dropdown (top left).Choose Save. | The maintenance order is released and saved.For SP11 line item (component 0010), stock transport requisition at remote plant (FORP) is created if selected versions are V1 or V3.Note down the stock transport requisition generated for SP11 for further use.Delivery date in STR is calculated as below:Delivery date in STR = (Work Order Requirements date) – (GR processing time for remote plant in days) from factory calendar.For SP12 line item (component 0020), stock transport requisition at remote plant (FORP) is created.Note down the stock transport requisition generated for SP12 for further use.Delivery date in STR is calculated as below:Delivery date in STR = (Work Order Requirements date) – (GR processing time for remote plant in days) from factory calendar.For SP13 line item (component 0030), stock transport requisition at remote plant (FORP) is created if selected versions are V1 or V3.Note down the stock transport requisition generated for SP13 for further use.Delivery date in STR is calculated as below:Delivery date in STR = (Work Order Requirements date) – (GR processing time for remote plant in days) from factory calendar.For SP14 line item (component 0040), purchase requisition at Base plant (FOBP) is created.Note down the purchase requisition generated for SP14 for further use.Delivery date in PR is calculated as below:Delivery date in PR = (Work Order Requirement Date) - (GR process time (FOBP) (Factory Days) - (Planned Delivery Time (FORP)) (Calendar Days) - (Planned Delivery Time (FOBP)) (Calendar days) - (GR process time (FORP) (Factory Days)Note If quantity or requirement date in maintenance order is changed before creation of stock transport order or purchase order for materials, the updated quantity and delivery date reflects in Stock Transport Requisition or Purchase Requisition.If quantity or requirement date in maintenance order is changed after creation of stock transport order or purchase order for materials, the updated quantity or delivery date will not reflect in stock transport requisition or purchase requisition. Instead a new stock transport requisition or purchase requisition is created for the updated quantity. |  |

#### Run Material Requirements Planning (MRP) at Remote Plant and Base Plant

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can start the MRP run for material at remote plant and base plant.

MRP run at remote plant is applicable to following cases:

- SP11 and SP13 Blank and V2 versions only

MRP run at base plant is applicable to following cases:

- SP11 all versions
- SP12 all versions

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage screen is displayed. |  |
| 3 | Add Area of Responsibility (One-time activity) | Choose User icon (at top right corner) > MRP Setting > Area of responsibility | MRP Settings screen should be displayed. |  |
| 4 | Select Plant and MRP Controller | Select the checkboxes for:Plant: FORP (in case running for remote) and FOBP (in case running for base)MRP Controller 001Choose Assign.Click on Back. | Area of responsibility FORP / /FOBP should be added. |  |
| 5 | Select Material and Show Shortages | In the search filter, make the following entry for Materials and choose Go.Material: FLOG-SP11 / FLOG-SP12 / FLOG-SP13Select filtered row with plant FORP or FOBP and choose Manage Materials. | The Material Details screen is displayed. |  |
| 6 | Start MRP run for Material without Scheduling Agreement | On the left of Materials screen, choose material as per requirement.On the screen Material Details, choose Start MRP Run. | The MRP Run in progress notification is displayed and then the MRP Run completed notification is displayed. |  |
| 7 | Verify Purchase Requisitions that are Available | In the stock/requirements list, stock transfer request and purchase requisitions are shown as MRP results.After the screen refreshes, look for rows with PurRqs items to check more details (mostly the last entry under MRP element column).To view more details of the purchase requisition (PR) item:Click on PurRqs item.Choose Open.Click Purchase Requisition. | The MRP has created stock transfer request (STR) and purchase requisition that can be used for the procurement of materials at remote plant and base plant respectively.Note down the STR / PR number created above.Note In case of intercompany code process, the STR/PR will be created. For required configurations and prerequisites, refer to the setup guide for scope item 40G. |  |

#### Convert Purchase Requisition to Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use the below steps to perform following activities:

- You can assign stock transport requisitions to a source of supply and convert assigned source stock transport requisitions to stock transport orders.
- You can assign purchase requisitions to a source of supply and convert assigned source purchase requisitions to purchase orders.

Procedure

Stock transport requisition can be converted to stock transport order using either of the below options.

Table 1: Option A: Conversion using Cloud Job

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Launch the SAP Fiori App | Open Schedule Purchasing Jobs - Advanced(F1702). | The Schedule Purchasing Jobs - Advanced screen is displayed. |  |
| 3 | Schedule New Job | On the Schedule Purchasing Jobs-Advanced screen, choose Create >Step 2 > Step 3 > Parameters. | The Automatic Creation of Purchase Orders from Requisitions screen is displayed. |  |
| 4 | Input Purchase Requisition | In the Parameters section enter the stock transport requisition created in [Run Material Requirements Planning (MRP) at Remote Plant and Base Plant](#unique_22) [page ] 25.Choose Schedule. | The stock transport requisition is entered and job is scheduled. |  |
| 5 | Job Log | In the Jobs screen area, when the status of the scheduled job changes to Finished, choose on Log or Results to view the stock transport order created. | The stock transport order is created.For V5 version, the STO is created with account assignment category F.In case of intercompany code process, the STO will be created. For required configurations and prerequisites, refer to the setup guide for scope item 40G.Note For SP13 purchase requisition for base plant is automatically created when STR is converted to STO. |  |
| 6 | Convert Purchase Requisition to Purchase Order | Repeat the above steps to convert purchase requisition to purchase order. | The purchase order is created. |  |

Table 2: Option B: Conversion using Manage Purchase Requisitions App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open Process Purchase Requisitions - Deprecated (F1048). | The Manage Purchase Requisitions screen is displayed. |  |
| 3 | Search for Purchase Requisition | On the Manage Purchase Requisitions screen, enter the following:Plant: FORPPurchasing Organization: FLPOChoose Go. | The Purchase Requisition list is displayed. |  |
| 4 | Select Purchase Requisition | Select the purchase requisitions created in the previous step.In Assigned Supplier, choose 1 Sources. | The Select Source of Supply screen is displayed. |  |
| 5 | Assign Source to Purchase Requisition | On the Select Source of Supply screen, choose a displayed source with a real price (not zero).Example BP1001489. | The assignment of one source to the requisition is done. The Purchase Requisition list is displayed. |  |
| 6 | Prepare the Purchase Order | Choose the purchase requisition that the assigned supplier is displayed.Choose Create Purchase Order.If a dialog appears, click on Close. | The Manage Purchase Requisitions screen is displayed. |  |
| 7 | Create Purchase Order | Choose UD - StockTranspOrderDel as the purchase order type.Choose Save.Note down the STO number for the following steps. | The stock transport order is created.StockTranspOrderDel created under the number 450000XXXX.Note down the STO number for the following steps.For V5 version, the STO is created with account assignment category F.Note For SP13 purchase requisition for base plant is automatically created when STR is converted to STO. |  |
| 8 | Convert Purchase Requisition to Purchase Order | Repeat the above steps to convert purchase requisition to purchase order. | The purchase order is created. |  |

Table 3: Option C (Two-Step GR Process): Conversion using Create Purchase Order-Advanced

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open Create Purchase Order-Advanced (F1720). | The Purchase Order screen is displayed. |  |
| 3 | Enter Purchase Requisition | On the Create Purchase Order-Advanced screen, enter the purchase requisition number created in previous step. | All details are displayed to proceed. |  |
| 4 | Select Origin Accept Checkbox | At item details, go to Delivery tab and select the Origin Accept checkbox. | The origin accept checkbox is selected. |  |
| 5 | Save Details | Check all the details at header and item level.Click Save. | The purchase order is created having all materials.Note down the purchase order corresponding to purchase requisition. |  |

|  |
| --- |
| Note Stock transport requisition(STR) to stock transport order (STO) conversion is blocked for SP11 (version V1 and V3) and SP12 (version blank and V1 ) items in case block STR indicator is set in Field Logistics configuration mentioned in the setup guide of scope item 40G and Hold flag is updated in maintenance order. Hold flag must be removed from maintenance order before proceeding.It is possible to create standalone Purchase Requisitions and Purchase Order at Field Logistics plants (Base & Remote) as part of direct procurement of required goods without reference to any supply process in Field Logistics. |

#### Check for Automatically Created Inbound Delivery from Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can check the automatically created inbound delivery(s) from the purchase order.

For more information, refer to [Creating Automatic Inbound Delivery](https://help.sap.com/viewer/DRAFT/74ffc024fd794eeca49dc8ffe7f9870d/latest/en-US/5249493b25934d4cb7bc9db6cd4836c2.html). Also note that creation of inbound delivery is optional for non warehouse managed cases and the following steps in this section are not applicable in case inbound delivery is not created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Change Purchase Order - Advanced (ME22N). | The Change Purchase Order - Advanced screen is displayed. |  |
| 3 | Enter Purchase Order | Enter the purchase order number created in [Convert Purchase Requisition to Purchase Order](#unique_23) [page ] 26.Click Other Purchase OrderEnter PO Number: XXXChoose Other Document. | Purchase order is displayed.The line items are displayed. |  |
| 4 | Inbound Delivery from Item Overview Section | Select a line item and go to Item details > Confirmations tab.In the Confirmations tab, check if inbound delivery is created.Note If a purchase order line item has different delivery dates, multiple inbound deliveries are created for each delivery date. | Note down the inbound delivery number. |  |
| 5 | Access the App | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad is displayed. |  |
| 6 | Update Storage Location | Access the app Change Inbound Delivery (VL32N).Enter the inbound delivery number (noted in step 4).Under the Stock Placement tab, enter the storage location: FOBWSave the entries. | The Change Inbound Delivery screen is displayed.The inbound delivery is saved and distributed to warehouse in case of warehouse managed storage location. |  |
| 7 | Verify Field Logistics Indicator | Go to Processing tab in the inbound delivery item details section.This should be updated as Relevant for putaway in case of SP11, SP12, and SP13 (version Blank or V2).This should be updated as On Hold (H) in case of SP13 (version V1 or V3) and SP14 whenever Hold on Shore flag is checked in maintenance order.This should be updated as Relevant for cross-docking (C) in case of SP13 and SP14 whenever Hold on Shore flag is not checked in maintenance order. | Correct value should be updated in the field. |  |
| 8 | Check SSCUI if Inbound Delivery Not Found | Log on to Fiori Launchpad with the role SAP_BR_BPC_EXPERT.Access the app: Manage Your Solution and select required country version and choose Configure Your Solution.Select the SSCUI Oil and Gas > Logistics Planning and Execution > Field Logistics General Settings > Maintain Inbound delivery creation at PlantChoose Configure.Ensure the Create IBD checkbox is selected. | Inbound delivery is automatically created only if Create IBD checkbox is selected. |  |
| 9 | Check AIF Monitor if Inbound Delivery Not Found | In case inbound delivery is not found under the Confirmations tab:Log on to Fiori Launchpad as Configuration Expert - Business Network Integration. | Fiori Launchpad is displayed. |  |
| 10 | Access the App | Access the app Message Dashboard (/AIFX/WDA_MSG_MONITOR).Set the filter to current date and go to Results List. | Filter is set to current date. |  |
| 11 | Select the Queue for Field Logistics | Under Results List, in All Messages column select the link for the number of documents corresponding to the row:RFC Monitoring for Field Logistics - /OILUF . | Monitoring and Error Handling screen is displayed. |  |
| 12 | Check the Message | Under section Interface to Monitor qRFC IBD Creation - FLOG_IBD/ note down the inbound delivery(s) corresponding to the delivery dates in the purchase order.If IBD creation resulted in error, fix the error and click Reprocess.Refresh the results by clicking Refresh. | Message for Inbound delivery creation is displayed Inbound Delivery XXX creation Successful for PO XXXX with Delivery Date XXXXXX.Note down the inbound delivery number. |  |

#### Post Goods Receipt at Base Using 107 Movement Type Two-step GR Process (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can post the goods receipt using movement types 107 for warehouse and non-warehouse scenarios in addition to a one-step GR using movement type 101.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement application. | The Post Goods Movement screen is displayed. |  |
| 3 | Choose the Process and Movement Type for Warehouse and Non-warehouse Managed Scenarios | Choose Goods Receipt.Choose Inbound Delivery.Enter the inbound delivery and movement type 107. | The goods receipt data is displayed on the screen. |  |
| 4 | Choose the Process and Movement Type for Non-inbound Delivery Scenario | Choose Goods Receipt.Choose Purchase Order.Enter the purchase order and movement type 107. | The goods receipt data is displayed on the screen. |  |
| 5 | Check and Verify the Details | Check and verify all the details like material, quantity, and storage location. | All details are checked. |  |
| 6 | Post Goods Receipt | Select the items for which a goods receipt is to be posted.Choose Post. | Goods receipt is posted.The system displays the message, material document xxx posted. |  |

|  |
| --- |
| Note After goods receipt with 107 is completed, then the next step 109 can be done from Process Receipts - Stock and Non-stock items (F5316) application. |

#### Post Goods Receipt at Base Plant

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can post the goods receipt. S/4HANA is being updated accordingly. You can also receive subcontracting purchase order line items using Process Receipts - Stock and Non-stock items (F5316) application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG). | The SAP Fiori launchpad is displayed. |  |
| 2 | User Settings (optional) | Click on User icon on top right and choose Settings.Go to Default values and enter the details below:Plant: Example: FOBP.Choose Save. | Default settings for the user is saved.When user settings are saved, on launch, automatically these filters are seen. |  |
| 3 | Access the App | Open Process Receipts - Stock and Non-stock items (F5316). | The Process Receipt screen is displayed. |  |
| 4 | Scan Handling Unit | If the vendor handling unit label is already available, choose Scan in To Be Received tab and scan the QR code label for handling unit.The search filters would be filled in automatically.Note Scanning functionality in Process Receipts application complies with handling units in serialized shipping container code (SSCC) number range only. | Handling unit label is scanned. Purchase order details are filtered automatically. |  |
| 5 | Select Filters | Default filters for the app are as shown below.Purchase Order: <your purchase order number created in step convert purchase requisition to purchase order>Planned Delivery Date: <delivery date in PO (optional)>Product/Supplier Item: <material>Plant: <Example: FOBP>Choose Go.Note Single or multiple purchase orders can be received simultaneously by selecting the purchase orders and clicking Receive. | The list page displays the purchase order items. |  |
| 6 | Details of PO Line Item | Select the purchase order line item from list page.The header section shows the following details:Purchase order/line item, product, supplier, product/supplier item, priority, item type.Status: To be received.Line item level details are segregated into following tabs with field details as below:Quantity: PO open quantity, PO total quantity and inbound delivery quantity.Receipt Information: Delivery note, document date, posting date, planned delivery date, visual inspection, quality management (yes/no), valuation type.Item Information: Delivered quantity, storage location, stock type.Handling Units: Handling units created for this product are displayed.Plant options: Plant, storage type, warehouse, batch information like batch, manufacturing date, shelf life expiry date.Predecessor Documents: Maintenance order, purchase requisition, purchase order, inbound delivery, stock transport requisition, material document at base, stock transport order, outbound delivery, warehouse task.Attachments: in case any attachments to be added.Serial number (optional): Warehouse managed and non-warehouse managed scenarios for serialized material.Item distribution (optional): Item distribution could be used to distribute the delivered quantity into different storage locations, stock types, batches, and serial number for non-warehouse managed scenarios only.Check if all the details populated are correct.Note: For subcontracting purchase order line items, item category will be L (subcontracting). | All the values populated under each field is correct. |  |
| 7 | Create Batch (optional) | In case the material is batch managed, to create new batches click Create batch.Enter the batch name, manufacturing date, shelf life expiry date.Click on Create batch. | New batch created for the material. |  |
| 8 | Update Delivery | Choose Update Delivery.Update Delivery is activated only for scenarios with inbound delivery.In the Update Delivery popup:Update stock type for the delivery, if required. Stock type can be chosen from the search help as Blocked, or Unrestricted use, or Quality Inspection. Stock type field will be visible for inbound delivery items distributed to warehouse only.Enter the batch created for the material, if the material is batch managed.Enter the valuation type, if the material is split valuated.Select the Auto create (serialization) checkbox to serialize the whole delivered quantity, if the material is serialized.Select Forego Hold or Cross-docking checkbox to enable the Forego scenario based on hold or cross-docking status. (Optional)Enter putaway quantity and putaway quantity unit if required. These fields are visible for items of inbound delivery not distributed to warehouse.Enter storage location: FOBW / FOBN (optional)Choose Update Delivery.Note For warehouse managed storage location, delivery is distributed to warehouse management as well. | The Update Delivery popup appears.The details entered in the popup are saved to the inbound delivery. |  |
| 9 | Create Handling Units (optional for SP11 and SP12 process and forego hold or cross-dock cases) | Choose Create HU (at the handling units facet level).Enter the following details in the popup:Quantity to be Packed: <Example: 5>Pack Unit: <Example: EA>Packaging Material: <Example: PMCARTON>.Number of Handling Units: <Example: 2>Choose Create HU. | Success message appears confirming the handling units creation.Parent handling units section displays the handling units created. |  |
| 10 | Verify Field Logistics Status (In Maintenance Order) | This should be updated as " " in case of SP11 and SP12.This should be updated as On Hold (H) in case of SP13 (version V1 and V3) and SP14 whenever Hold on Shore flag is checked in maintenance order.This should be updated as Relevant for cross-docking (C) in case of SP13( V1 and V3) and SP14 whenever Hold on Shore flag is not checked in maintenance order.) | Correct value is updated as per the scenario. |  |
| 11 | Verify the Field Logistics Status (in Warehouse Managed Inbound Delivery) | This should be updated as Relevant for putaway in case of SP11, SP12, and SP13 (version Blank and V2) and forego hold or cross-dock.This should be updated as On Hold in case of SP13 (version V1 and V3) and SP14 whenever Field Logistics indicator is On Hold in warehouse managed delivery.This should be updated as Relevant for cross-docking (C) in case of SP13 and SP14 whenever Field Logistics indicator is relevant for cross-docking in warehouse managed delivery. | Correct value is updated as per the scenario. |  |
| 12 | Item Distribution (Optional) | Choose Item Distribution.Edit and click on Distribute.Enter the following details:Quantity to be Received: 5Total quantity must be less than or equal to the quantity actually delivered.Unit of Measurement: EAStorage Location: FORN.Stock Type by defaults selected as unrestricted-use.In case of serialized material, auto-create serial number option will be visible in item page. Enable the option to create serial number automatically.Choose Save.Select the item distribution line item to go to object page.The header section shows the following details:Item information:Delivered quantity, storage location, and stock type information.Plant information.In case the material is batch managed, details such as batch number, manufacturing date, and shelf-life expiration date will be shown.If batch is not assigned or blank, then option is available to assign the batch from F4 help.Serial numberIn case of serialized material, options are given to assign serial number automatically or manually. | Success message appears confirming the item distribution.Item distribution facet displays the line items distributed.Success message appears confirming the batch and Serial number creation. |  |
| 13 | Serial Number (Optional) | Serial number facet will be displayed if material is serialized.Choose Serial Numbers.You can view or update already assigned serial numbers in extended warehouse managed inbound delivery (EWM IBD), logistics execution inbound delivery (LE IBD) and purchase order (PO) items at base plant.In case serial number is not assigned in EWM IBD, LE IBD, or PO items, click on Assign Serial Numbers to assign serial number automatically or select the existing serial number from F4 help. | Success message appears confirming the serial number creation.Serial number facet displays the serial number created. |  |
| 14 | Click on Receive | Choose Receive.Enter the delivered quantity. For partial delivery, delivered quantity can be lesser than inbound delivery quantity.Note The goods receipt posting with 109 will be supported with only full quantity of the LE IBD and EWM IBD item for which 107 has happened.For example, in case 107 movement is already completed, the same quantity is updated for 109 movement and no further update is allowed in system.Stock type: For a non-quality managed material stock type can be changed while performing goods receipt. | Delivered quantity is entered.Note In warehouse managed active scenarios, if GR is posted with partial quantity for a line item, then a new inbound delivery gets created automatically for the remaining quantity and line items. |  |
| 15 | Select Visual Inspection (Optional) | From the visual inspection dropdown, select the value based on the visual inspection result.Example: Passed.Visual Inspection result can be passed, failed, not performed or passed - minor surface damages. | Visual inspection is selected. |  |
| 16 | Check Values | Choose Check.This simulates the goods receipt process and lists out possible errors, information and warnings before confirming goods receipt. | Message appears as Document is O.K. |  |
| 17 | Confirm Quantity | Validate the quantity value in quantity field with the actual received quantity and change the quantity if required.Choose Confirm. | Confirmation message appears.Receipt of inbound delivery item XXXXX is confirmed is displayed.For a quality managed material, on posting goods receipt, a notification is triggered to Quality Engineer as per the system configuration.Configuration steps are mentioned in Setup Guide.Note For subcontracting purchase order line items, components of the item will be received with the same quantity as the main item in the background. |  |
| 18 | Goods Receipt Document | Choose Back to navigate to the list page.Click Go to refresh the data and select Received tab.The purchase order is now visible under Received tab.Choose Chevron to navigate to object page for this purchase order line item.Received details are segregated into following tabs with field details as below:Receipt information: delivery note, document date, posting date, created by, visual inspection, quality management, valuation type, external ID, additional Note.Item Information: received quantity, goods movement type, storage location, unit of measure, inventory stock type.Handling Units: handling units created for this product are displayed. In case nested handling unit, both parent and child handling units are displayed.Plant: plant, warehouse number, storage bin, storage type.Follow-On documents: material document number, warehouse task, inspection lot, outbound delivery, stock transport order.Attachments: in case any attachments exists.Note down these values for further execution. | Note down the goods receipt number.All the details related to receipt are validated and confirmed.NoteInspection lot is created automatically for quality managed material. Note down this value. |  |
| 19 | Outbound Delivery | Navigate to outbound delivery facet in follow on documents section.If any outbound delivery exists, it will be displayed.Note down this value. | For a non-quality managed SP13/SP14 material, outbound delivery is automatically created on performing post goods receipt.Multiple outbound delivery might be created.The storage location where the item was received will be passed on as issuing storage location to STO and then OBD so that the items will be issued from the same storage location where they were received. |  |
| 20 | Stock Transport Order | Navigate to stock transport order facet in follow on documents section.If any stock transport order exists, it will be displayed.Note down this value. | For a non-quality managed SP14 material, stock transport order is automatically created on performing post goods receipt. Note down this value.Multiple stock transport order might be created.Delivery date in STO is calculated for SP14 process as Delivery date in STO = Work order requirement date – GR processing time in remote plant. |  |
| 21 | Warehouse Task | Navigate to warehouse managed task facet in follow on documents section.If any warehouse managed task exists, it will be displayed.Note down this value. | Warehouse task is automatically created in warehouse managed storage location if selected.For a quality managed material, on posting goods receipt a warehouse task from goods receipt area to quality area to be created (in case if it is not created automatically) and confirmed before doing usage decision.For a non-quality managed material, on posting goods receipt:SP11/SP12 process: Putaway task is created automatically to move items from good receipt area to destination storage bin.SP13 process:Putaway warehouse task is created automatically for the inbound delivery from goods receipt area to hold area for items on hold.Putaway warehouse task is created automatically for the inbound delivery from goods receipt area to destination storage area for items marked for forego hold or cross-dock.SP14 process:Putaway warehouse task is created automatically for the inbound delivery from goods receipt area to hold area for items on hold.Putaway warehouse task is created automatically for the inbound delivery from goods receipt area to destination storage area for items marked for forego hold or cross-dock. |  |
| 22 | Print Preview | Choose Print Preview.Select Product Label and HU Label. | This allows you to check the details and layout before printing.Product and handling unit label are displayed for all products.Product label displays following details:QR CodeProductItem TypeReceived quantityGoods receipt dateGoods receipt numberMaintenance order numberPurchase order/itemVisual inspection statusQuality managed statusField Logistics StatusProduct label is also displayed with batch and serial number in case the material is batch and serial profile managed respectively.Handling unit label is displayed with all details of outbound delivery and stock transport order for SP13 and SP14 processes.Handling unit label displays following details:Ship-toOutbound Delivery/ItemHandling UnitField Logistics StatusReceived QuantityPacked QuantityGoods Receipt NumberGoods Receipt DateItem TypePrint DateMaintenance OrderMaintenance Order DescriptionGross WeightPurchase Order/ItemStock Transport Order/ItemInstructionNote Field logistics enables you to print instructions dynamically on Product label and Handling until label based on processes with respect to field logistics status. |  |
| 23 | Print Preview | Click on Print Preview | This will allow you to check the details and layout before printing.The user has the option to download and/or print the details on the top right of the preview pop-up. |  |
| 24 | Download | Click on Download | The user can choose to download the Product label and HU label details from the print preview as an PDF file. |  |
| 25 | Trigger Output Management Queue | Click on PrintSelect Product Label and HU Label | The Product Label and Handling Unit Label details are sent to the print queue without previewing the details.If the necessary configurations are maintained, Printing the labels will trigger an email notification as well.Details of the queue can be viewed from the Manage Output Items app.Note Field logistics supports extensibility which enables you to implement your custom logic in filling in the values for the custom fields added to the print label forms. |  |

|  |
| --- |
| Note In case of warehouse managed hold and cross-dock scenarios all items to be received need to be packed and all items that are packed need to be received together. |

#### Display Open Inspection Lots - QM Active (Optional)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots screen is displayed. |  |
| 3 | Select Filters | If purchase order is not displayed in the filters, choose Adapt Filters.On the dialog box Adapt Filters, select Procurement and choose More Filters.Select Purchase Document and choose OK.Choose Go.Now enter the purchase order created at base plant.Choose Go. | Inspection lot is displayed. |  |
| 4 | Select Inspection Lot | In the inspection lot list, select the inspection lot which you created before. | Inspection lot is displayed.Make a note of the inspection lot number. |  |
| 5 | Check Inspection Lot by Selecting the Line | Under Origin, verify the referenced purchase order and material document. | The purchase order number and material document number from which the inspection lot originates are displayed. |  |
| 6 | Choose Operation (optional) | In Results, choose operation QM for procurement GR. | For checking the attachment in the inspection method optionally.If you have attached a document in the inspection method as described in BNQ - Create Quality Inspection Plan - MDS, the quality technician can review the attachment referring to step 7 to 9. |  |
| 7 | Choose Characteristic (optional) | Choose Surface in the Characteristics column. | A dialog box appears with the characteristics details with the link to the inspection method. |  |
| 8 | Display the Attachment (optional) | Under Documents, the attachment for an illustration of the surface is displayed. |  |  |
| 9 | Display Text |  | In General, long text is displayed. |  |

#### Record Inspection Results - QM Active (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If inspection results need to be recorded for one or only a few inspection lots, execute the steps that follow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A). | The Record Inspection Results screen displays. |  |
| 3 | Select Filters | Enter the purchasing document created in the previous step. | If purchase order is not displayed in the filters, choose Adapt Filters. In the dialog box Adapt Filters, find Procurement and choose More Filters. Select Purchase Order and choose OK. Choose Go. |  |
| 4 | Select Inspection Lot | In the inspection lot list, select the inspection lot. |  |  |
| 5 | Choose Record Results | Choose Record Multiple Results in the right bottom. | The purchase order number and material document number from which the inspection lot originates are displayed. |  |
| 6 | Enter Inspection Result | Depending on the inspection result, select one of the following two options:Positive Result:Surface: Code Group - Code SURFACE 0020 (Smooth)Length: Mean Value (cm): 160Negative Result:Surface: Code Group - Code SURFACE 0010 (Rough)Length: Mean Value (cm): 90 | For qualitative characteristic (Surface) the search help is needed to select a value. For the quantitative characteristic (Length) a number can be entered directly.The default number of inspected objects is calculated based on the sample size reviewed in an earlier step. The number of inspected objects can be manually changed. A number of nonconforming objects can be maintained directly in the respective fields as well for every inspection characteristic.With the app Record Results – Hierarchical View, a user can exceptionally overrule the automatic evaluation, for example, to document that the tolerance is always at the upper limit, then the generic defect ‘tolerance issue’ will be used. |  |
| 7 | Save Inspection Lot | Choose Save. | The inspection lot is saved. QM Inspection for procurement goods has been performed and result recorded. |  |

#### Record Usage Decision - QM Active

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the assembly depending on the inspection result. If you do not want to use the Quality Engineer Overview, you can open the Record Usage Decisions app directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer .Note To configure the user QUALITY_ENGINEER contact your Administrator. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the Notification | Click on notification button (Bell icon). | A message appears as notification: Inspection Lot 1XXXXXXXXXX was created for plant FOBP. |  |
| 3 | Inspection Lot Display | Click on the latest notification to navigate to the Record Usage Decision (QA11) app.Alternatively, you can access the Record Usage Decision (QA11) app and enter the inspection lot number.Press Enter. | The Record Usage Decisions screen is displayed.Inspection lot details are displayed. |  |
| 4 | Validate the Origin | Click on Inspection Lot, a new screen opens.Under Data of Origin tab, check whether the material document / purchase order corresponds to the documents posted / created in earlier sections. | Inspection lot quantities are entered. |  |
| 5 | Enter Usage Decision | Under the Characteristics tab, enter the usage decision from the following options:UD code: A1 (Accepted - unrestricted stock)A2 (Accepted -unrestricted - minor quality)A3 (Accepted -unrestricted - sample consumption)Negative ResultUD code: R1 (Rejected - blocked stock)R210 (Rejected - return supplier w/o delivery)R220 (Rejected - return supplier with delivery)Choose Yes if dialog Confirmation Prompt appears.Alternatively, usage decision can also be entered by clicking on WM Inspection. | Usage decision is entered. |  |
| 6 | Save Usage Decision | Choose Save. | The usage decision is made. The system automatically triggers the material movements associated with the usage decision code.Note For a quality managed material, when the user QUALITY_ENGINEER configured with additional authorization saves the usage decision:Outbound delivery is created automatically for SP13 process. Multiple outbound deliveries can be created based on Field logistics indicator in inbound delivery.Stock transport order and outbound delivery is created automatically for SP14 process.Multiple stock transport order can be created.Putaway task from quality area to final storage destination is created in case of forego hold or cross-dock scenario and from quality to hold area for items on hold.In case more than one item is packed in a handling unit then warehouse task to hold area is automatically created only if usage decision is accepted for all item in that handling unit. This automatic warehouse task creation works only if settings are maintained in Define Follow-Up Actions for Quality Results section mentioned in 40G setup guide. |  |
| 7 | Consolidated Stock Transport Order or Purchase Order |  | In case the stock transport order consists of multiple stock transport requisitions or if the purchase order consists of multiple purchase requisitions, the number of follow-on documents created is different for each case.For more information, refer to [SP13 Goods Receipt Consolidation Scenarios and Document Creation](https://help.sap.com/docs/SAP_S4HANA_CLOUD/74ffc024fd794eeca49dc8ffe7f9870d/b692cf8c4962425780b357ee86c561a7.html) . |  |

#### Create Putaway Warehouse Tasks (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

As a warehouse clerk, you can create warehouse tasks for putaway.

|  |
| --- |
| Note For supply processes SP11 and SP12, if goods receipt is posted using Process Receipts - Stock and Non-stock items (F5316) app, the putaway warehouse task for the inbound delivery is automatically created for non-quality managed materials.For supply process SP13 and SP14, in case of hold and forego hold / cross-dock, if goods receipt is posted using Process Receipts - Stock and Non-stock items (F5316) application, the putaway warehouse task for the inbound delivery is automatically created. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Inbound Deliveries - Deliveries (F1706). | The Change Inbound Delivery screen displays. |  |
| 3 | Select Filters | On the Change Inbound Deliveries screen, select Filters. | The Filters dialog box appears. |  |
| 4 | Enter Purchase Order Number | On the Filters dialog box, enter the following:Purchase Order: Purchase order numberInbound Delivery: Inbound delivery number. |  |  |
| 5 | Choose Go | Choose Go. | The inbound delivery is displayed on the Change Inbound Deliveries screen. |  |
| 6 | Select Inbound Delivery | On the Change Inbound Deliveries screen, select the inbound delivery. | The inbound delivery is displayed. |  |
| 7 | Select Delivery Items | On the Change Inbound Deliveries screen, select the delivery items. |  |  |
| 8 | Choose Create Tasks | Choose Create Tasks. | The message Tasks created is displayed. |  |
| 9 | Choose Warehouse Tasks | In the Delivery Item section, choose Warehouse Tasks. | The warehouse tasks created are displayed. Note down the warehouse task number. |  |

#### Confirm Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A putaway list is printed and handed over to the warehouse operative. This is used to perform the warehouse tasks and confirm them in the system. Note that the warehouse clerk can also confirm the warehouse tasks using the app Warehouse Monitor (Business Catalog WM – Monitoring).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Warehouse Tasks - Putaway. |  |  |
| 3 | Enter Warehouse Task Number | On the Process Warehouse Tasks - Putaway screen, select warehouse task number. |  |  |
| 4 | Choose Go | Choose Go. |  |  |
| 5 | Select Warehouse Task | Select the warehouse task. |  |  |
| 6 | Confirm Warehouse Task | Choose Confirm. | The message Warehouse task confirmed is displayed. |  |

#### Create Nested Handling Unit (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The warehouse operative packs the already created handling unit in a new (parent) handling unit. This packing is supported only in hold area and goods issue area after confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Access the app Pack Handling Units - Advanced. | The Pack Handling Units – Advanced screen is displayed. |  |
| 3 | Enter the Warehouse Task | Enter the following details:Warehouse number: FOBPWork center: WP99Handling unit: Child handling unit created via Process Receipts - Stock and Non-stock items (F5316) app. | The packing screen is displayed. |  |
| 4 | Create New Handling Unit | Enter the following details in create handling section:Pack material: PMPALLETNumber of handling unit:1Storage bin: In the same storage bin as child handling unit (created in Process Receipts - Stock and Non-stock items (F5316) app).Click on execute. | New handling unit is created. |  |
| 5 | Repack in Parent HU | Drag and drop all the child handling unit to the new handling units to pack.Choose Save. | Handling units are packed.Inbound delivery is saved. |  |

#### Check Automatically Created Stock Transport Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can view the STO that is automatically created, when goods receipt is posted in a direct purchase scenario (SP14).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Process Receipts - Stock and Non-stock items (F5316). | The Process Receipt screen is displayed. |  |
| 3 | PO Filter | Enter the purchase order received earlier.Purchase order line item would be listed out in Received tab.Select the line item to navigate to details. | Purchase order details are shown. |  |
| 4 | Follow on Documents Successful | Select Follow-On Documents tab.Material document, stock transport order, outbound delivery information is available under this section. | Note down the stock transport order, outbound delivery number for further execution.Note In case of intercompany code process, the STO will be created. For required configurations and prerequisites, refer to the setup guide for scope item 40G. |  |

If the follow-on documents are not displayed, follow the below steps:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with user Configuration Expert - Business Network Integration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Message Dashboard | Open Message Dashboard - SAP Application Interface Framework . | The Interface Monitor screen is displayed. |  |
| 3 | Results List | In the results list, select the link for successfully processed number of documents corresponding to below row.RFC Monitoring for Field Logistics - /OILUF | The Monitoring and Error Handling screen is displayed. |  |
| 4 | Stock Transport Order Created | Note down the STO related to the IBD displayed in the Interface to monitor qRFC STO Creation - FLOG_STO/1 screen area.Note: If STO creation resulted in error, fix the error and click on reprocess icon and then refresh the results by clicking on refresh icon. | Message for STO creation is displayed STO XXXXX Creation Successful for IBD XXXX. |  |

#### Update/Check Stock Transport Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to update the storage location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Order screen is displayed. |  |
| 3 | Search for Purchase Order | On the Manage Purchase Orders screen, enter the purchase order: <stock transport order number from step [Convert Purchase Requisition to Purchase Order](#unique_23) [page ] 26. | The purchase order is displayed. |  |
| 4 | Select Purchase Order | Select the purchase order you created in the step [Convert Purchase Requisition to Purchase Order](#unique_23) [page ] 26.Choose Edit. | Purchase order details should be editable. |  |
| 5 | Save Order | Choose Save/Order. | Purchase order should be saved. |  |

#### Check Automatically Created Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to check the automatically created outbound delivery (If the outbound delivery is already noted from steps in Process Receipts app). This is applicable for SP13 V1 and V3 and SP14 process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration - CONF_EXPERT_BUS_NET_INT. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Message Dashboard - SAP Application Interface Framework .Set the filter to current date and go to Results List. | The Interface Monitor screen is displayed.Filter is set to current date. |  |
| 3 | Results List | Under Results List, select the link for successfully processed number of documents corresponding to below row:RFC Monitoring for Field Logistics - /OILUF | Monitoring and Error Handling screen. |  |
| 4 | Outbound Delivery Created | Note down the OBD related to the STO displayed in the Interface to Monitor qRFC OBD Creation - FLOG_OBD/1 section.If outbound delivery creation results in error, fix the error and then, click Reprocess icon.Click Refresh to refresh the results list. | The message Outbound delivery XXX created for stock transport order XXXX is displayed.Note down the OBD number.Note In the intercompany code process, the outbound delivery is created. For required configurations and prerequisites, refer to the setup guide for scope item 40G. |  |

Note down the outbound delivery number.

Execute the procedures in [Confirm Pick Warehouse Tasks](#unique_33) [page ] 58 > Goods Issue from Base Plant to Remote Plant > Goods Receipt at Remote Plant as a next step.

For detailed steps to perform these procedures, refer the sections [Create Pick Warehouse Tasks](#unique_34) [page ] 56 to [Post Goods Receipt at Remote Plant](#unique_35) [page ] 59.

For executing the SP13 process, use the below data:

- Material: FLOG-SP13 or FLOG-SP13-NO-QM for non-quality managed material.
- Stock Transport Order: Noted from step [Convert Purchase Requisition to Purchase Order](#unique_23) [page ] 26 for SP13 process.

|  |
| --- |
| Note For SP13,Multiple outbound deliveries can be created based on items in the inspection lot and its Field Logistics status. Different outbound delivery is created for hold and cross-dock items.Outbound delivery is created for forego hold or cross-dock scenario. |

#### Create Replenishment Delivery for Stock Transport Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity to create delivery for SP11 and SP12 process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Purchase Orders - Due for Delivery (VL10B). | The Goods Movement screen is displayed. |  |
| 3 | Enter Data for PO Display | On the Purchase Orders tab page, enter the following:Delivery creation dates (From): Delivery creation from date. Delete the default date.Delivery creation dates (To): Delivery creation to date. Delete the default date.Purchasing Document: Choose a stock transport order that was updated in the previous step [Update/Check Stock Transport Order](#unique_31) [page ] 50.Choose Execute. | The purchase order due for delivery is displayed in the Activities Due for Shipping Purchase Orders, Fast Display screen. |  |
| 4 | Create Delivery | Select stock transport orders from the list. Choose Background to create delivery in the background. | Activities Due for Shipping Purchase Orders, Fast Display screen is displayed. |  |
| 5 | Check Delivery Number | Choose More > Show/Hide Delivery and note down the delivery number shown in the SD Doc. field. | A delivery is created.Note down the outbound delivery number.Note In the intercompany code process, the outbound delivery is created. For required configurations and prerequisites, refer to the setup guide for scope item 40G. |  |

#### Update / Check Outbound Delivery

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen is displayed. |  |
| 3 | Enter Delivery Number | On the Change Outbound Delivery screen, enter the delivery document number from the earlier section and choose Continue. | The Change Outbound Delivery screen displays. |  |
| 4 | Check Field Logistic Indicator | Double click on line item and go to Processing tab.Check Field Logistics indicator field value. | Check Field Logistics indicator field value is displayed as S (stock removal for demand) for SP11 (V1 and V3 version), and SP12 (all version). |  |
| 5 | Check Reference Details | Go to Predecessor Data tab to view reference details. | Check the following reference details for SP11 (V1 and V3 version) and SP12 (all version).Reference document: Maintenance order number.Reference item: Operation number of item in maintenance order.Reference document type: MO (maintenance order) |  |
| 6 | Enter Storage Location | On the Picking tab, enter the storage location FOBW. | Storage location is updated. |  |
| 7 | Save the Changes | Choose Save. | Outbound delivery is saved and delivery is distributed to warehouse.In case the hold flag is active in the maintenance order the outbound delivery is not distributed for SP13 and SP14.For SP13 and SP14, picking warehouse task is created automatically for the outbound delivery from goods receipt area to goods issue area for items relevant for cross-docking in case of non-quality managed and from quality area to goods issue area for quality managed. |  |

#### Remove Hold from Maintenance Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

For changing the hold on-shore value of the maintenance order item, navigate to Change Maintenance Order application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Change Maintenance Order (IW32). | The change order screen is displayed. |  |
| 3 | Create Maintenance Order | On the Change Order screen, choose the order number of the maintenance order created earlier then choose Continue. | The order details are displayed. |  |
| 4 | Locate the Items for which the Hold Indicator is to be Changed | Go to Operation Data > Components > tab. You can see all the items displayed in the change mode. |  |  |
| 5 | Change and Save | Locate the item for which the hold indicator is to be removed and make the below change:Hold On-Shore: uncheck |  |  |
| 6 | Save Order | Choose Save. | Maintenance order 4000XXX is saved. |  |

#### Pack Items into Handling Units (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is to finalize the outbound process by posting the done status.

|  |
| --- |
| Note This step is applicable only for SP11 and SP12 process |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Manage Outbound Delivery Orders (F6498) app. | The Manage Outbound Delivery Orders screen is displayed. |  |
| 3 | Search/Enter Outbound Delivery | Search the outbound delivery order using the appropriate filter options, or enter the warehouse number and delivery document. | Outbound delivery is listed out. |  |
| 4 | Navigate to Object Page | Choose Chevron to navigate to object page. | Item navigates to the object page. |  |
| 5 | Select Packing | Choose Packing at the header level. | Packing screen is displayed. |  |
| 6 | Create Handling Unit | Select Packaging Material from the search help.Choose the Storage Bin, as shown in left panel, then choose Execute. | Your handling unit is automatically created now. You can also see the handling unit number on the left side panel. |  |
| 7 | Select Stock to be Packed | Select the material to be packed.Drag and drop into the handling unit created. | The item appears under the handling unit.According to your pack steps, you see on the left side your packed materials. |  |

#### Create Pick Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, the warehouse clerk creates warehouse tasks for picking.

|  |
| --- |
| Note For supply processes SP13 and SP14 cross-docking scenario, if goods receipt is posted using Process Receipts - Stock and Non-stock items (F5316) app, the picking warehouse task for the outbound delivery is automatically created.A notification is triggered in case creation of pick warehouse task fails due to open putaway task for an item which was previously on hold.Configuration steps for this are mentioned in setup instructions for this scope item. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM).To check the default warehouse number, choose User > Settings > Default Values > Warehouse Number (FOBP). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Outbound Delivery Orders (F6498). | The Manage Outbound Delivery Orders screen is displayed. |  |
| 3 | Search/Enter Outbound Delivery | Search the outbound delivery order using the appropriate filter options or enter the warehouse number & delivery document. | Outbound delivery is listed out. |  |
| 4 | Navigate to Object Page | Choose Chevron to navigate to object page. | Item navigates to object page. |  |
| 5 | Create Pick Warehouse Tasks | Select outbound delivery order item.Select ItemChoose Create Pick Warehouse TaskSelect Create Pick Tasks Manually from dropdown listChoose Create | Warehouse task is created. Picking list is automatically printed in the background. |  |
| 6 | Choose the Outbound Delivery Order to Find the Warehouse Task Created | Double-click on the outbound delivery order. | The outbound delivery order screen is displayed. |  |
| 7 | Choose Warehouse Tasks | Choose Warehouse Tasks. | The Warehouse Task screen is displayed. |  |
| 8 | Note the Warehouse Task Number | Note down the number displayed. | Note down the outbound delivery order. |  |

#### Confirm Pick Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Pick list is printed in the earlier step and handed over to the warehouse operative who performs the warehouse tasks and confirms them in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Warehouse Tasks (F3880). |  |  |
| 3 | Enter the Warehouse Task | Enter the warehouse task number created in the previous section and choose Go. |  |  |
| 4 | Confirm Warehouse Task | Select the checkbox for the selected warehouse task and choose Confirm. |  |  |

|  |
| --- |
| Note You can create nested handling unit in goods issue area as well. Refer to [Create Nested Handling Unit (Optional)](#unique_29) [page ] 48 for detailed steps. |

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can follow this process for issuing goods from base plant without container assignment. If the items in outbound delivery must be packed in containers and dispatched, please refer 6BA scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Manage Outbound Delivery Orders (F6498) app. | The Manage Outbound Delivery Orders screen is displayed. |  |
| 3 | Warehouse Managed: Post Goods Issue | Search the outbound delivery order using the appropriate filter options or enter the warehouse number and delivery document.Select the outbound delivery order and choose Goods Issue. | Goods issue is posted and has generated a warehouse material document.Note In case of non warehouse managed outbound delivery goods issue can be posted using Change Outbound Delivery (VL02N). |  |

#### Post Goods Receipt at Remote Plant

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can receive goods at remote location.

Receiving storage location in the remote plants should be MM-IM managed.

|  |
| --- |
| Note Process Receipts - Stock and Non-stock items (F5316) application does not support receiving items at a remote plant for intercompany code scenario. It is recommended to use Process Cross-Plant Receipts (F4713) application for posting goods receipts at remote plants. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG). | The SAP Fiori launchpad is displayed. |  |
| 2 | User Settings (optional) | Click on User icon on top right and choose Settings.Go to Default values and enter the details below:Plant: Example: FORP.Choose Save. | Default settings for the user is saved.When user settings are saved, on launch, automatically these filters are seen. |  |
| 3 | Access the App | Open Process Receipts - Stock and Non-stock items (F5316). | The Process Receipt screen is displayed. |  |
| 4 | Scan HU | If the vendor HU label is already available, choose Scan on To Be Received tab and scan the HU label.The search filters would be filled in automatically.Note Scanning functionality in Process Receipts application complies with handling units in serialized shipping container code (SSCC) number range only. | HU label is scanned. Purchase order details are filtered automatically. |  |
| 5 | Select Filters | Default filters for the app are as shown below.Purchase Order: <your stock transport order (STO) manage number created in step Convert Purchase requisition to Purchase order>Planned Delivery Date: <delivery date in STO (optional)>Product/Supplier Item: <material>Plant: <Example: FOBP>Choose Go.Note Goods receipts at remote is displayed against the outbound delivery item for which post goods issue is already posted.Single or multiple purchase orders can be received simultaneously by selecting the purchase orders and clicking Receive. | The list page displays the purchase order entered. |  |
| 6 | Click on Receive | In the To be Received tab, click the purchase order filtered out. | Navigates to the details of Purchase order line item. |  |
| 7 | Details of PO Line Item | The Header section shows the following details:Purchase order / line item, product, supplier, product / supplier item, priority, item type.Status: To be Received.Line item level details are segregated into following tabs with field details as below:Quantity: PO open quantity, PO total quantity and inbound delivery quantity.Receipt Information: delivery note, document date, posting date, planned delivery date, visual inspection, quality management (Yes / No), valuation type.Item Information: delivered quantity, storage location, stock type.Handling Units: handling units created for the outbound delivery are displayed, if any exist.Plant options: plant, storage type, warehouse, batch information like batch, manufacturing date, shelf life expiry date.Predecessor Documents: maintenance order, purchase requisition, purchase order, inbound delivery, stock transport requisition, material document at base, stock transport order, outbound delivery, warehouse task.Attachments: in case any attachments to be added.Serial number (optional): only in case of non-warehouse managed scenarios for serialized material.Item distribution (optional): only in case of non-warehouse managed scenarios. Item distribution could be used to distribute the delivered quantity into different storage locations, stock types or batches,Check if all the details populated are correct. | All the values populated under each field is correct. |  |
| 8 | Create Batch (optional) | In case the material is batch managed, to create new batches click Create batch.Enter the batch name, manufacturing date, shelf life expiry date.Choose Create batch. | New batch created for the material. |  |
| 9 | Click on Receive | Choose Receive.Enter the delivered quantity. For partial delivery, delivered quantity can be lesser than inbound delivery quantity.Stock type: For a non-quality managed material stock type can be changed while performing goods receipt.Batch: <your batch details> | Delivered quantity is entered. |  |
| 10 | Select Visual Inspection | From the visual inspection dropdown, select the value based on the visual inspection result.Example: Passed.Visual inspection result can be passed, failed, not performed or passed - minor surface damages. | Visual inspection is selected. |  |
| 11 | Enter Storage Location | If the storage location is not pre-filled, enter the storage location.Example: FORN | Storage location is selected. |  |
| 12 | Check Values | Choose Check.This simulates the goods receipt process and lists out possible errors, information and warnings before confirming goods receipt. | Message appears as Document is O.K. |  |
| 13 | Confirm GR | Validate the quantity value in quantity field with the actual received quantity and change the quantity if required.Choose Confirm. | Confirmation toast message appears:Receipt for all items of purchase order XXXXXXX is confirmed. |  |
| 14 | Goods Receipt Document | Navigate back to the list page by clicking on Back icon.Click Go to refresh the data and select the Received tab.The purchase order is now visible under Received tab.Choose Chevron to navigate to object page for this purchase order line item.Received details are segregated into following tabs with field details as below:Receipt information: delivery note, document date, posting date, created by, visual inspection, quality management, valuation type, external ID.Item Information: received quantity, goods movement type, storage location, unit of measure, inventory stock type.Plant: plant, warehouse number, storage bin, storage type.Follow-On documents: material document number, warehouse task, inspection lot, outbound delivery, stock transport order.Attachments: in case any attachments exists. | Note down the goods receipt number.All the details related to receipt are validated and confirmed. |  |

#### Post Goods Issue for Maintenance Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The steps in this section are relevant for SP11 and SP14 processes. This activity is performed when you want to issue material to maintenance order created or stock reserved against reservation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Issue. | The Post Goods Issue screen is displayed. |  |
| 3 | Select Maintenance Order | Select goods issue and order. |  |  |
| 4 | Select the Maintenance Order | Select the maintenance order created in section [Create Maintenance Order](#unique_19) [page ] 17.Press Enter. | The goods issue is displayed on the Goods Issue screen. |  |
| 5 | Enter Storage Location | On the Where tab, enter the storage location FORN.Press Enter. |  |  |
| 6 | Select Item and Post Goods Receipt | Select the items for which a goods receipt is to be posted.Choose Post. | The Post button is activated.The system displays the message Material document xxx posted.Note If materials are not procured against the current maintenance order then a warning message is displayed as Only 0.000 units received for maintenance order/operation/item 000004XXXXXXX/00XX/00XX. |  |

### Single Plant Setup

Single plant setup is a special case in which the base operates as a forward operating location. Items are supplied from a supply base, the remote base will hold, manage and forward to remote locations.

This scenario is to test implementation for single plant for supply process SP11, SP14 in work order for example, order procurement of materials for a plant which serves as both base plant and as well as remote plant and receiving the procured materials and store them in the same plant which serves as both base plant and as well as remote plant.

- Stock Located at Single Plant

In this scenario, the availability of the material is first checked with MRP run at single plant. If the demand for the material is not fulfilled yet, a purchase requisition is created. This purchase requisition is subsequently converted to a purchase order to procure this material from an external vendor. The material is then received at the base plant and relevant warehouse and quality activities are performed.

For SP11 to work for single plant its mandatory for version to V4.

- Direct Purchase for Single Plant

Follow the steps in this section for Supply Process SP14- Direct Purchase only.

In this scenario, purchase requisition is created from the maintenance order, which is subsequently converted to a purchase order for the base plant to procure this material from an external vendor. The material is then received at the base plant and relevant warehouse and quality activities are performed. The stock is issued from the base plant to remote plant. When the goods reach the remote plant, it is received and issued against the maintenance order.

To execute the process for SP14 supply process, follow the sequence of step as mentioned from section [Convert Purchase Requisition to Purchase Order](#unique_43) [page ] 72 to section [Record Inspection Results - QM Active (Optional)](#unique_15) [page ] 42 using below data.

Material: FLOG-SP14

Purchase requisition: Noted down from section [Release Maintenance Order](#unique_44) [page ] 70.

Note down the stock transport order, outbound delivery and warehouse task automatically created on posting goods receipt for SP14 process from section [Post Goods Receipt at Single Plant](#unique_45) [page ] 77.

|  |
| --- |
| NoteThis supply process supports both quality and non-quality managed materials.The following procedures are not applicable for non-quality managed materials:[Display Open Inspection Lots - QM Active (Optional)](#unique_14) [page ] 41[Record Inspection Results - QM Active (Optional)](#unique_15) [page ] 42 |

#### Create Maintenance Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is the initiation phase of maintenance where an employee creates a maintenance request. You can create a maintenance request using the Create Maintenance Request (F1511A) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Maintenance Request (F1511A). | The Create Maintenance Request screen is displayed. |  |
| 3 | Maintenance Request Creation | Enter the following:Technical Object: FOBP-TO (created in [Create Technical Object](#unique_10) [page ] 10)Description: Example: FL Maintenance RequestPriority: Select a priority from the dropdown. Example: Medium. | Details are entered. |  |
| 4 | Save the Entries | Choose Submit. | Maintenance request is saved.Note down the maintenance request number. |  |

#### Screen Maintenance Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is the screening phase of the maintenance process. As a supervisor you have to review the maintenance request, change responsibility of the requests (if required) and take appropriate decision to proceed with request, reject or send back seeking more information.

You can review and accept the maintenance request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Screen Maintenance Requests (F4072) app. | The Screen Maintenance Request screen is displayed. |  |
| 3 | Filter | To filter the maintenance request created in previous section, enter the following.Planning Plant: FOBPTechnical Object: FOBP-TO.Choose Go. | Maintenance request is filtered and displayed under the Open tab. |  |
| 4 | Accept | Click Chevron to navigate to the maintenance request.Review the maintenance request, click Edit to make changes if needed.Save the changes.Choose Accept to accept the maintenance request. | Maintenance request is accepted. |  |

#### Create Maintenance Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Maintenance order is used to collect all the materials required to correct the malfunction in the remote plant. It also derives the supply process for a material in a plant, which defines how the material is stocked at remote and base plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Create Maintenance Order | Open the Create Maintenance Order app. | The Create Order screen is displayed. |  |
| 3 | Create Maintenance Order | On the Create Order screen, choose order type: Reactive Maintenance YA01.Header Notification: Enter the maintenance request created in previous section.Choose Continue. |  |  |
| 4 | Enter Details | On the Create Reactive Maintenance Order: %00000000001 screen, go to the General Data tab.In the Responsibilities section,Work Center: FOBP-PM | Work center is entered. |  |
| 5 | Define the Operations to be Performed to Resolve the Malfunction | Go to the Operation Data tab. You can see the operation overview in the Operations table for operation 0010:The system calculates the duration of the operation based on the time you entered in Work field and on how many people you scheduled in the number field to perform this operation. You have now made the required entries in the header data screen of the order. |  |  |
| 6 | Select Material for SP11 Supply Process | Select the operation 0010 and choose Material tab, below the maintenance request list in the screen.On the Materials tab, enter the following for each material:Note For non-quality managed materials, as an example you can provide the material as FLOG-SP11 for the respective supply process.Material: FLOG-SP11Quantity: 5 EAPlant: FOBPNote For the SP11 process it is mandatory to keep version as V4. This can be achieved with the SSCUI configuration Maintain Supply process determination by Plant node by an appropriate version selection against each supply process.For more details on the SSCUI, view the setup instructions for this scope item (section Configure Field Logistics).To duplicate a material line in the list with all item data, choose Copy Material. You can then change specific fields in the copied line. | Item category should be defaulted to L and Field Logistics supply process should be defaulted to SP11 for the first line item. |  |
| 7 | Select Material for SP14 Supply Process | Select the operation 0010 and choose Materials tab, below the maintenance request list in the screen.On the Materials tab, enter the following for each material:Note For non-quality managed materials, as an example you can provide the material as FLOG-SP14 for the respective supply process.Material: FLOG-SP14Quantity: 5 EAPlant: FOBPNote To duplicate a material line in the list with all item data, choose Copy Material. You can then change specific fields in the copied line. | Item category should be defaulted to L and Field Logistics supply process should be defaulted to SP14 for the first line item. |  |
| 8 | Reservation / Purchase Requisition Creation Instance | From the maintenance order, the purchase requisition can be created collectively or individually.You can configure this for each plant / order type, as described in the setup instructions for this scope item.You can select the instance for stock transport requisition / purchase requisition creation for the supply processes.Select the required option from the dropdown list of Reservation/Purc.req column in component level from the Materials tab.Purchase requisitions can be created immediately on saving the maintenance order or when the order is released.Select the option From Release for all line items. | Reservation/Purc.req column is selected as From Release for all line items. |  |
| 9 | Check Entries | Choose Check Entries on the top left corner of the screen. | Entries have been checked. |  |
| 10 | Save Order | Choose Save. | Order 4000XXX is saved. |  |
| 11 | Submit for Approval | In the Change Status dropdown on top left, select Submit for Approval. | Maintenance order is submitted for approval.The order goes for approval as per the workflow maintained.Note If there are no custom workflows maintained, order gets approved automatically. |  |

#### Approve Maintenance Order (Optional)

Purpose

You can approve the maintenance order from the My Inbox app.

|  |
| --- |
| Note This step involves Flexible Workflow which can be set up by the customer. Any agent configured in workflow can approve the maintenance order. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862) app. | The My Inbox app displays list of orders available for approval. |  |
| 3 | Approve / Reject Maintenance Order | On the My Inbox screen, select the workflow request for maintenance order, you can review information page which gives detail of maintenance order like general data, responsibilities, account assignment, cost, dates etc.Update comment in Comments section.Approve maintenance order and add decision note if required.Note If the maintenance order is rejected, it can be further processed with required details and can be sent for approval again. | Maintenance order is approved, and order will be removed from the list in My Inbox.Maintenance order is in Ready to Prepare phase. |  |

#### Release Maintenance Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The maintenance order is used to collect all costs for a maintenance task and to debit the cost center that incurred the costs using the settlement functions in the CO module (Controlling).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Change Maintenance Order app.Enter the order number and press Continue. | The Change Reactive Maintenance: 4XXXXXX screen displays. |  |
| 3 | Maintain Settlement Category | Select Costs tab and under Settlement Rules maintain a settlement categoryFor example,Settlement category: Cost CenterSettlement receiver: Choose from search help like 17101701. | Settlement category is maintained. |  |
| 4 | Approval (optional) | Click on Change Status and choose Submit for Approval.Note: In case submit for approval is not active, this step may be skipped.Click on Refresh and check whether the subphase is in status Approved. | Maintenance order is approved. |  |
| 5 | Release and Save the Order | On the Change Reactive Maintenance screen, choose Set System Status.Choose Release from the Change Status dropdown (top left).Choose Save. | The maintenance order is released and saved.For SP14 line item (component 0040), purchase requisition at Base plant (FOBP) is created.Note down the purchase requisition generated for SP14 for further use. |  |

#### Run Material Requirements Planning (MRP) at Single Plant - Purchase Requisition Creation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can start the MRP run for material at base plant for SP11 supply process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coveragescreen is displayed. |  |
| 3 | Add Area of Responsibility (One-time activity) | Choose User icon (at top right corner) > MRP Setting > Area of responsibility | MRP Settings screen should be displayed. |  |
| 4 | Select Plant and MRP Controller | Select the checkboxes for:Plant: FOBPMRP Controller 001Choose Assign.Click on Back. | Area of responsibility FOBP should be added. |  |
| 5 | Select Material and Show Shortages | In the search filter, make the following entry for Materials and choose Go.Material: FLOG-SP11Select the filtered row with plant FOBP and choose Manage Materials. | The Material Details screen is displayed. |  |
| 6 | Start MRP run for Material without Scheduling Agreement | Choose material FLOG-SP11 on left of Materials screen.On the screen Material Details, choose Start MRP Run. | The MRP run in progress notification is displays first, then MRP Run completed notification displays. |  |
| 7 | Verify Purchase Requisitions that are Available | In the stock / requirements list, purchase requisitions are shown as MRP results.After the screen refreshes, look for rows with PurRqs items to check more details (mostly the last entry under MRP element column).To view more details of the purchase requisition (PR) item:Choose Open.Click Purchase Requisition. | The MRP has created stock transport requisitions that can be used for the procurement of materials from plant.Note down the PR number created above. |  |

#### Convert Purchase Requisition to Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can assign purchase requisitions to a source of supply and convert assigned source purchase requisitions to purchase orders.

Procedure

Purchase requisition can be converted to purchase order using either of the below options.

Table 4: Option A: Conversion using Cloud Job

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Launch the SAP Fiori App | Open Schedule Purchasing Jobs - Advanced(F1702). | The Schedule Purchasing Jobs - Advanced screen is displayed. |  |
| 3 | Schedule New Job | To enter the purchase requisition, on the Schedule Purchasing Jobs-Advanced screen, choose Create >Step 2 > Step 3 > Parameters. | The Automatic Creation of Purchase Orders from Requisitions screen is displayed. |  |
| 4 | Select Purchase Requisition | In the Parameters Section enter the purchase requisition created in [Run Material Requirements Planning (MRP) at Single Plant - Purchase Requisition Creation](#unique_50) [page ] 71 process.Choose Schedule. | The purchase requisition is entered and job is scheduled. |  |
| 5 | Job Log | In the Jobs section, when the status of the scheduled job changes to Finished, choose Log or Results to view the purchase order created. | The purchase order is created. |  |

Table 5: Option B: Conversion using Manage Purchase Requisitions App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Launch the SAP Fiori App | Open Process Purchase Requisitions - Deprecated (F1048). | The Manage Purchase Requisitions screen is displayed. |  |
| 3 | Search for Purchase Requisition | On the Manage Purchase Requisitions screen, enter the following:Plant: FOBPPurchasing Organization: FLPOChoose Go. | The Purchase Requisition list is displayed. |  |
| 4 | Select Purchase Requisition | Select the purchase requisitions created in the previous step.In Assigned Supplier, choose 1 Sources. | The Select Source of Supply screen is displayed. |  |
| 5 | Assign Source to Purchase Requisition | On the Select Source of Supply screen, choose a displayed source with a real price (not zero), for example, BP1001650. | The assignment of one source to the requisition is done. The Purchase Requisition list is displayed. |  |
| 6 | Prepare the Purchase Order | Choose the purchase requisition that the assigned supplier is displayed.Choose Create Purchase Order. | The Manage Purchase Requisitions screen is displayed. |  |
| 7 | Create the Purchase Order | Choose Standard PO as the purchase order type.Choose Save.Choose OK. | The stock transport order is created.Standard purchase order created under the number 450000XXXX.Note down the purchase order number for the following steps. |  |

#### Check for Automatically Created Inbound Delivery from Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can check the automatically created inbound delivery(s) from the purchase order.

For more information, refer to [Creating Automatic Inbound Delivery](https://help.sap.com/viewer/DRAFT/74ffc024fd794eeca49dc8ffe7f9870d/latest/en-US/5249493b25934d4cb7bc9db6cd4836c2.html).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Change Purchase Order - Advanced (ME22N). | The Change Purchase Order - Advanced screen is displayed. |  |
| 3 | Enter Purchase Order | Enter the purchase order number created in [Convert Purchase Requisition to Purchase Order](#unique_43) [page ] 72.Click Other Purchase OrderEnter PO Number: XXXChoose Other Document. | Purchase order is displayed.The line items are displayed. |  |
| 4 | Inbound Delivery from Item Overview Section | Select a line item and go to Item details > Confirmations tab.In the Confirmations tab, check if inbound delivery is created.Note If a purchase order line item has different delivery dates, multiple inbound deliveries are created for each delivery date. | Note down the inbound delivery number. |  |
| 5 | Access the App | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad is displayed. |  |
| 6 | Update Storage Location | Access the app Change Inbound Delivery (VL32N).Enter the inbound delivery number (noted in step 4).Under the Stock Placement tab, enter the storage location: FOBWSave the entries. | The Change Inbound Delivery screen is displayed.The inbound delivery is saved and distributed to warehouse. |  |
| 7 | Check SSCUI if Inbound Delivery Not Found | Log on to Fiori Launchpad with the role SAP_BR_BPC_EXPERT.Access the app: Manage Your Solution and select required country version and choose Configure Your Solution.Select the SSCUI Oil and Gas > Logistics Planning and Execution > Field Logistics General Settings > Maintain Inbound delivery creation at PlantChoose Configure.Ensure the Create IBD checkbox is selected. | Inbound delivery is automatically created only if Create IBD checkbox is selected. |  |
| 8 | Check AIF Monitor if Inbound Delivery Not Found | In case inbound delivery is not found under the Confirmations tab:Log on to Fiori Launchpad as Configuration Expert - Business Network Integration. | Fiori Launchpad is displayed. |  |
| 9 | Access the App | Access the app Message Dashboard (/AIFX/WDA_MSG_MONITOR).Set the filter to current date and go to Results List . | Filter is set to current date. |  |
| 10 | Select the Queue for Field Logistics | Under Results List, in All Messages column select the link for the number of documents corresponding to the row:RFC Monitoring for Field Logistics - /OILUF . | Monitoring and Error Handling screen is displayed. |  |
| 11 | Check the Message | Under section Interface to Monitor qRFC IBD Creation - FLOG_IBD/ note down the inbound delivery(s) corresponding to the delivery dates in the purchase order.If IBD creation resulted in error, fix the error and click Reprocess.Refresh the results by clicking Refresh. | Message for Inbound delivery creation is displayed Inbound Delivery XXX creation Successful for PO XXXX with Delivery Date XXXXXX.Note down the inbound delivery number. |  |

#### Post Goods Receipt at Base Using 107 Movement Type Two-step GR Process (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can post the goods receipt using movement types 107 for warehouse and non-warehouse scenarios in addition to a one-step GR using movement type 101.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement application. | The Post Goods Movement screen is displayed. |  |
| 3 | Choose the Process and Movement Type for Warehouse and Non-warehouse Managed Scenarios | Choose Goods Receipt.Choose Inbound Delivery.Enter the inbound delivery and movement type 107. | The goods receipt data is displayed on the screen. |  |
| 4 | Choose the Process and Movement Type for Non-inbound Delivery Scenario | Choose Goods Receipt.Choose Purchase Order.Enter the purchase order and movement type 107. | The goods receipt data is displayed on the screen. |  |
| 5 | Check and Verify the Details | Check and verify all the details like material, quantity, and storage location. | All details are checked. |  |
| 6 | Post Goods Receipt | Select the items for which a goods receipt is to be posted.Choose Post. | Goods receipt is posted.The system displays the message, material document xxx posted. |  |

|  |
| --- |
| Note After goods receipt with 107 is completed, then the next step 109 can be done from Process Receipts - Stock and Non-stock items (F5316) application. |

#### Post Goods Receipt at Single Plant

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can post the goods receipt. S/4HANA is being updated accordingly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG). | The SAP Fiori launchpad is displayed. |  |
| 2 | User Settings (Optional) | Click on User icon on top right and choose Settings.Go to Default values and enter the details below:Plant: Example: FOBP.Choose Save. | Default settings for the user is saved.When user settings are saved, on launch, automatically these filters are seen. |  |
| 3 | Access the App | Open Process Receipts - Stock and Non-stock items (F5316). | The Process Receipt screen is displayed. |  |
| 4 | Scan Handling Unit | If the vendor HU label is already available, choose Scan in To Be Received tab and scan the QR code for handling unit.The search filters would be filled in automatically.Note Scanning functionality in Process Receipts application complies with handling units in serialized shipping container code (SSCC) number range only. | Handling unit label is scanned. Purchase order details are filtered automatically. |  |
| 5 | Select Filters | Default filters for the app are as shown below.Purchase Order: <your purchase order number created in step convert purchase requisition to purchase order>Planned Delivery Date: <delivery date in PO (optional)>Product/Supplier Item: <material>Plant: <Example: FOBP>Choose Go.Note Single or multiple purchase orders can be received simultaneously by selecting the purchase orders and clicking Receive. | The list page displays the purchase order items. |  |
| 6 | Details of Purchase Order Line Item | Select the purchase order line item from list page.The header section shows the following details:Purchase order / line item, product, supplier, product / supplier item, priority, item type.Status: To be received.Line item level details are segregated into following tabs with field details as below:Quantity: PO open quantity, PO total quantity and inbound delivery quantity.Receipt Information: Delivery note, document date, posting date, planned delivery date, visual inspection, quality management (yes/ no), valuation type.Item Information: Delivered quantity, storage location, stock type.Handling Units: Handling units created for this material are displayed.Plant options: Plant, storage type, warehouse, batch information like batch, manufacturing date, shelf life expiry date.Predecessor Documents: Maintenance order, purchase requisition, purchase order, inbound delivery, stock transport requisition, material document at base, stock transport order, outbound delivery, warehouse task.Attachments: in case any attachments to be added.Serial number (optional): only in case of warehouse and non-warehouse managed scenarios for serialized material. | All the values populated under each field is correct. |  |
| 7 | Create Batch (optional) | In case the material is batch managed, to create new batches click Create batch.Enter the batch name, manufacturing date, shelf life expiry date.Click on Create batch. | New batch created for the material. |  |
| 8 | Update Delivery | Choose Update Delivery.Update Delivery is activated only for scenarios with inbound delivery.In the Update Delivery popup:Update stock type for the delivery, if required. Stock type can be chosen from the search help as Blocked, or Unrestricted use, or Quality Inspection. Stock type field will be visible for inbound delivery items distributed to warehouse only.Enter the batch created for the material, if the material is batch managed.Enter the valuation type, if the material is split valuated,Select the Auto create (serialization) checkbox to serialize the whole delivered quantity, if the material is serialized.Enter putaway quantity and putaway quantity unit if required. These fields are visible for items of inbound delivery not distributed to warehouse.Enter storage location: FOBW / FOBN (optional)Choose Update Delivery.Note For warehouse managed storage location, delivery is distributed to warehouse management as well. | The Update Delivery popup appears.The details entered in the popup are saved to the inbound delivery. |  |
| 9 | Create Handling Units (optional for SP11 and SP12 process and forego hold or cross-dock cases) | Choose Create HU (at the header level).Enter the following details in the popup:Quantity to be Packed: <Example: 5>Pack Unit: <Example: EA>Packaging Material: <Example: PMCARTON>.Number of Handling Units: <Example: 2>Choose Create HU. | Success message appears confirming the handling units creation.Handling units section displays the handling units created. |  |
| 10 | Verify Field Logistics Status (In Maintenance Order) | This should be updated as Relevant for putaway in case of SP11 and SP14. | Correct value is updated as per the scenario. |  |
| 11 | Verify the Field Logistics Status (in Warehouse Managed Inbound Delivery) | This should be updated as Relevant for putaway in case of SP11 and SP14. | Correct value is updated as per the scenario. |  |
| 12 | Serial Number (Optional) | Serial number facet will be displayed if material is serialized.Choose Serial Numbers.You can view or update already assigned serial numbers in extended warehouse managed inbound delivery (EWM IBD), logistics execution inbound delivery (LE IBD) and purchase order (PO) items at base plant.In case serial number is not assigned in EWM IBD, LE IBD, or PO items, click Assign Serial Numbers to assign serial number automatically or select the existing serial number from F4 help. | Success message appears confirming the serial number creation.Serial number facet displays the serial number created. |  |
| 13 | Click on Receive | Choose Receive.Enter the delivered quantity. For partial delivery, delivered quantity can be lesser than inbound delivery quantity.Note The goods receipt posting with 109 will be supported with only full quantity of the LE IBD and EWM IBD item for which 107 has happened.For example, in case 107 movement is already completed, the same quantity is updated for 109 movement and no further update is allowed in system.Stock type: For a non-quality managed material stock type can be changed while performing goods receipt. | Delivered quantity is entered.Note In warehouse managed active scenarios, if GR is posted with partial quantity for a line item, then a new inbound delivery gets created automatically for the remaining quantity and line items. |  |
| 14 | Select Visual Inspection (Optional) | From the visual inspection dropdown, select the value based on the visual inspection result.Example: Passed.Visual Inspection result can be Passed, Failed, Not Performed or Passed - minor surface damages. | Visual inspection is selected. |  |
| 15 | Check Values | Choose Check.This simulates the goods receipt process and lists out possible errors, information and warnings before confirming goods receipt. | Message appears as Document is O.K. |  |
| 16 | Confirm Quantity | Validate the quantity value in quantity field with the actual received quantity and change the quantity if required.Choose Confirm. | Confirmation toast message appears.Receipt of inbound delivery item XXXXX is confirmed message is displayed.For a quality managed material, on posting goods receipt:A notification is triggered to Quality Engineer as per the system configuration.Configuration steps are mentioned in setup instructions for this scope item.In case of warehouse managed storage location is selected a warehouse task from GR area to Quality area is created.For a non-quality managed material, on posting goods receipt, putaway task is created automatically to move items from GR area to destination storage area. |  |
| 17 | Goods Receipt Document | Choose Cancel in the confirmation message popup.Click Go to refresh the data and select Received tab.The purchase order is now visible under Received tab.Choose Chevron to navigate to object page for this purchase order line item.Received details are segregated into following tabs with field details as below:Receipt information: Delivery note, document date, posting date, created by, visual inspection, quality management, valuation type, external id, additional note.Item Information: Received quantity, goods movement type, storage location, unit of measure, inventory stock type.Handling Units: Handling units created for this material are displayed.Plant: Plant, warehouse number, storage bin, storage type.Follow-On documents: Material document number, warehouse task, inspection lot, outbound delivery, stock transport order.Attachments: in case any attachments exists.Note down these values for further execution. | Note down the goods receipt number.All the details related to receipt are validated and confirmed.NoteWarehouse task is automatically created in warehouse managed scenarios. Note down this value.Inspection lot is created automatically for quality managed material. Note down this value. |  |
| 18 | Print Preview | Choose Print Preview.Select Product Label and HU Label. | This allows you to check the details and layout before printingProduct and handling unit label are displayed for all products.Product label displays following details:QR CodeProductItem TypeReceived QuantityGoods receipt dateGoods receipt numberMaintenance order numberPurchase order/itemVisual inspection statusQuality managed statusField Logistics StatusNote Field logistics enables you to print instructions dynamically on Product label based on processes with respect to Field Logistics statuses. |  |
| 19 | Download | Click on Download. | The user can choose to download the Product label and HU label details from the print preview as an PDF file. |  |
| 20 | Trigger Output Management Queue | Click on Print.Select Product Label and HU Label. | The Product Label and Handling Unit Label details are sent to the print queue without previewing the details.If the necessary configurations are maintained, Printing the labels will trigger an email notification as well.Details of the queue can be viewed from the Manage Output Items app.Note Field logistics supports extensibility which enables you to implement your custom logic in filling in the values for the custom fields added to the print label forms. |  |

#### Display Open Inspection Lots - QM Active (Optional)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots screen is displayed. |  |
| 3 | Select Filters | If purchase order is not displayed in the filters, choose Adapt Filters.On the dialog box Adapt Filters, select Procurement and choose More Filters.Select Purchase Document and choose OK.Choose Go.Now enter the purchase order created at base plant.Choose Go. | Inspection lot is displayed. |  |
| 4 | Select Inspection Lot | In the inspection lot list, select the inspection lot which you created before. | Inspection lot is displayed.Make a note of the inspection lot number. |  |
| 5 | Check Inspection Lot by Selecting the Line | Under Origin, verify the referenced purchase order and material document. | The purchase order number and material document number from which the inspection lot originates are displayed. |  |
| 6 | Choose Operation (optional) | In Results, choose operation QM for procurement GR. | For checking the attachment in the inspection method optionally.If you have attached a document in the inspection method as described in BNQ - Create Quality Inspection Plan - MDS, the quality technician can review the attachment referring to step 7 to 9. |  |
| 7 | Choose Characteristic (optional) | Choose Surface in the Characteristics column. | A dialog box appears with the characteristics details with the link to the inspection method. |  |
| 8 | Display the Attachment (optional) | Under Documents, the attachment for an illustration of the surface is displayed. |  |  |
| 9 | Display Text |  | In General, long text is displayed. |  |

#### Record Inspection Results - QM Active (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If inspection results need to be recorded for one or only a few inspection lots, execute the steps that follow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A) . | The Record Inspection Results screen displays. |  |
| 3 | Select Filters | Enter the purchasing document created in the previous step. | If purchase order is not displayed in the filters, choose Adapt Filters. In the dialog box Adapt Filters, find Procurement and choose More Filters. Select Purchase Order and choose OK. Choose Go. |  |
| 4 | Select Inspection Lot | In the inspection lot list, select the inspection lot. |  |  |
| 5 | Choose Record Results | Choose Record Multiple Results in the right bottom. | The purchase order number and material document number from which the inspection lot originates are displayed. |  |
| 6 | Enter Inspection Result | Depending on the inspection result, select one of the following two options:Positive Result:Surface: Code Group - Code SURFACE 0020 (Smooth)Length: Mean Value (cm): 160Negative Result:Surface: Code Group - Code SURFACE 0010 (Rough)Length: Mean Value (cm): 90 | For qualitative characteristic (Surface) the search help is needed to select a value. For the quantitative characteristic (Length) a number can be entered directly.The default number of inspected objects is calculated based on the sample size reviewed in an earlier step. The number of inspected objects can be manually changed. A number of nonconforming objects can be maintained directly in the respective fields as well for every inspection characteristic.With the app Record Results – Hierarchical View, a user can exceptionally overrule the automatic evaluation, for example, to document that the tolerance is always at the upper limit, then the generic defect ‘tolerance issue’ will be used. |  |
| 7 | Save Inspection Lot | Choose Save. | The inspection lot is saved. QM Inspection for procurement goods has been performed and result recorded. |  |

#### Record Usage Decision - QM Active (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the assembly depending on the inspection result. If you do not want to use the Quality Engineer Overview, you can open the Record Usage Decisions app directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer .Note To configure the user QUALITY_ENGINEER contact your Administrator. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the Notification | Click on notification button (Bell icon). | A message appears as notification: Inspection Lot 1XXXXXXXXXX was created for plant FOBP. |  |
| 3 | Inspection Lot Display | Click on the latest notification to navigate to the Record Usage Decision (QA11) app.Alternatively, you can access the Record Usage Decision (QA11) app and enter the inspection lot number.Press Enter. | The Record Usage Decisions screen is displayed.Inspection lot details are displayed. |  |
| 4 | Validate the Origin | Click on Inspection Lot, a new screen opens.Under Data of Origin tab, check whether the material document / purchase order corresponds to the documents posted / created in earlier sections. | Inspection lot quantities are entered. |  |
| 5 | Enter Usage Decision | Under the Characteristics tab, enter the usage decision from the following options:UD code: A1 (Accepted - unrestricted stock)A2 (Accepted -unrestricted - minor quality)A3 (Accepted -unrestricted - sample consumption)Negative ResultUD code: R1 (Rejected - blocked stock)R210 (Rejected - return supplier w/o delivery)R220 (Rejected - return supplier with delivery)Choose Yes if dialog Confirmation Prompt appears.Alternatively, usage decision can also be entered by clicking on WM Inspection. | Usage decision is entered. |  |
| 6 | Save Usage Decision | Choose Save. | The usage decision is made. The system automatically triggers the material movements associated with the usage decision code.Note For a quality managed material, when the user QUALITY_ENGINEER configured with additional authorization saves the usage decision, putaway task from quality area to final storage destination is created. |  |

#### Create Putaway Warehouse Tasks (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

As a warehouse clerk, you can create warehouse tasks for putaway.

|  |
| --- |
| Note For supply process SP11 and SP14, in case of hold, if goods receipt is posted using Process Receipts - Stock and Non-stock items (F5316) application, the putaway warehouse task for the inbound delivery is automatically created. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Inbound Deliveries - Deliveries (F1706). | The Change Inbound Delivery screen displays. |  |
| 3 | Select Filters | On the Change Inbound Deliveries screen, select Filters. | The Filters dialog box appears. |  |
| 4 | Enter Purchase Order Number | On the Filters dialog box, enter the following:Purchase Order: Purchase order numberInbound Delivery: Inbound delivery number. |  |  |
| 5 | Choose Go | Choose Go. | The inbound delivery is displayed on the Change Inbound Deliveries screen. |  |
| 6 | Select Inbound Delivery | On the Change Inbound Deliveries screen, select the inbound delivery. | The inbound delivery is displayed. |  |
| 7 | Select Delivery Items | On the Change Inbound Deliveries screen, select the delivery items. |  |  |
| 8 | Choose Create Tasks | Choose Create Tasks. | The message Tasks created is displayed. |  |
| 9 | Choose Warehouse Tasks | In the Delivery Item section, choose Warehouse Tasks. | The warehouse tasks created are displayed. Note down the warehouse task number. |  |

#### Confirm Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A putaway list is printed and handed over to the warehouse operative. This is used to perform the warehouse tasks and confirm them in the system. Note that the warehouse clerk can also confirm the warehouse tasks using the app Warehouse Monitor (Business Catalog WM – Monitoring).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Warehouse Tasks - Putaway. |  |  |
| 3 | Enter Warehouse Task Number | On the Process Warehouse Tasks - Putaway screen, select warehouse task number. |  |  |
| 4 | Choose Go | Choose Go. |  |  |
| 5 | Select Warehouse Task | Select the warehouse task. |  |  |
| 6 | Confirm Warehouse Task | Choose Confirm. | The message Warehouse task confirmed is displayed. |  |

#### Post Goods Issue for Maintenance Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The steps in this section are relevant for SP11 and SP14 processes. This activity is performed when you want to issue material to maintenance order created or stock reserved against reservation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Issue. | The Post Goods Issue screen is displayed. |  |
| 3 | Select Maintenance Order | Select goods issue and order. |  |  |
| 4 | Select the Maintenance Order | Select the maintenance order created in section [Create Maintenance Order](#unique_48) [page ] 66.Press Enter. | The goods issue is displayed on the Goods Issue screen. |  |
| 5 | Enter Storage Location | On the Where tab, enter the storage location FOBW.Press Enter. |  |  |
| 6 | Select Item and Post Goods Receipt | Select the items for which a goods receipt is to be posted.Choose Post. | The Post button is activated.An outbound delivery has been created.The system displays the message Delivery xxxxxx created.Note If materials are not procured against the current maintenance order then a warning message is displayed as Only 0.000 units received for maintenance order/operation/item 000004XXXXXXX/00XX/00XX. |  |

#### Direct Purchase for Single Plant

Follow the steps in this section for Supply Process SP14 - Direct Purchase only.

In this scenario, purchase requisition is created from the maintenance order, which is subsequently converted to a purchase order for the base plant to procure this material from an external vendor. The material is then received at the base plant and relevant warehouse and quality activities are performed. The stock is issued from the base plant to remote plant. When the goods reach the remote plant, it is received and issued against the maintenance order.

To execute the process for SP14 supply process, follow the sequence of step as mentioned from section [Convert Purchase Requisition to Purchase Order](#unique_43) [page ] 72 to section [Post Goods Issue for Maintenance Order](#unique_58) [page ] 89 using below data.

Material : FLOG-SP14

Purchase requisition: Noted down from section [Release Maintenance Order](#unique_44) [page ] 70

Note down the stock transport order, outbound delivery and warehouse task automatically created on posting goods receipt for SP14 process from section [Post Goods Receipt at Single Plant](#unique_45) [page ] 77.

|  |
| --- |
| NoteThis supply process supports both quality and non-quality managed materials.For non-quality managed materials, you can enter the material as FLOG-SP14-NO-QM.The following procedures are not applicable for non-quality managed materials:[Display Open Inspection Lots - QM Active (Optional)](#unique_53) [page ] 82[Record Inspection Results - QM Active (Optional)](#unique_54) [page ] 84 |

### Goods Receipt Reversal (Optional)

You perform this activity when you want to reverse the goods movement done in section [Post Goods Receipt at Base Plant](#unique_26) [page ] 32.

There are multiple cases where goods movement reversal is possible as documented below.

#### Goods Receipt Reversal Process

Goods receipts is posted for the inbound delivery or purchase order at the base plant or remote plant. You can perform goods receipts reversal at remote and base plants using the Process Receipts - Stock and Non-stock items (F5316) application.

Goods receipt at base plant can be reversed if the following conditions are met.

For quality managed materials:

1. For warehouse managed active cases (EWM at base), goods receipt at base plant can be reversed if the putaway warehouse task is not confirmed and usage decision is not performed.
2. For non-warehouse managed cases with inbound delivery (IM at base with IBD), goods receipt at base plant can be reversed if the usage decision is not performed.
3. For non-warehouse managed cases without inbound delivery (IM at base), goods receipt at base plant can be reversed if the usage decision is not performed.

For non-quality managed materials:

1. For warehouse managed active (EWM at base), goods receipt at base plant can be reversed if the putaway or picking warehouse task is not confirmed.
2. For non-warehouse managed cases with inbound delivery (IM at base with IBD), goods receipt at base plant can be reversed if goods issue is not posted for the outbound delivery.
3. For non-warehouse managed cases without inbound delivery (IM at base), goods receipt at base plant can be reversed if goods issue is not posted for the outbound delivery.

Based on the supply process, execute the steps up to [Post Goods Receipt at Base Plant](#unique_26) [page ] 32 to create the test data as required.

|  |
| --- |
| Note For non-quality managed materials, on posting goods receipt for supply process SP13 and SP14, subsequent follow-on documents are created as below.Outbound delivery is created automatically for SP13 process.Stock transport order and outbound delivery is created automatically for SP14 process. |

For the goods receipt reversal scenarios, when STO is created from multiple STRs or PO is created from multiple PRs, the goods receipt reversal is different in each case.

For more information, refer to [SP13 Goods Receipt Consolidation Scenarios and Document Creation](https://help.sap.com/docs/SAP_S4HANA_CLOUD/74ffc024fd794eeca49dc8ffe7f9870d/b692cf8c4962425780b357ee86c561a7.html).

##### Warehouse Management Active in Base Plant

Purpose

You can perform goods receipt reversal for a non-quality managed material SP13 where warehouse managed location is active.

Follow the prerequisites steps for creating the test data.

Prerequisites

1. Create a non-quality managed material of type SP13 FLOG-SP13-NO-QM.

The steps are documented in Configuration Guide for 40G scope item.

1. Create purchase info records for this material in FORP and FOBP plant.

The steps are documented in Configuration Guide for 40G scope item.

1. Follow the steps in [Create Maintenance Request](#unique_17) [page ] 15 and [Release Maintenance Order](#unique_21) [page ] 23 to create maintenance order for the material FLOG-SP13-NO-QM.
2. Execute the steps [Run Material Requirements Planning (MRP) at Remote Plant and Base Plant](#unique_22) [page ] 25 to [Convert Purchase Requisition to Purchase Order](#unique_23) [page ] 26 to create stock transport requisition and convert stock transport requisition to stock transport order with automatic purchase requisition creation in [Convert Purchase Requisition to Purchase Order](#unique_23) [page ] 26 to [Check for Automatically Created Inbound Delivery from Purchase Order](#unique_24) [page ] 29 with storage location as FOBW.
3. Execute the steps with the purchase requisition number obtained from above step. Follow the procedures from [Convert Purchase Requisition to Purchase Order](#unique_23) [page ] 26 to [Post Goods Receipt at Base Plant](#unique_26) [page ] 32.
4. Execute steps in [Check Automatically Created Outbound Delivery](#unique_32) [page ] 51.

Note down the outbound delivery number.

There are multiple instances when goods receipt reversals can be triggered which are provided. Execute the prerequisite steps to create the data and test each case.

|  |
| --- |
| Note Goods receipt reversal cannot be done if any of the warehouse task (inbound delivery or outbound delivery warehouse tasks) is confirmed. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Case 1: Warehouse tasks not created for Inbound Delivery |  |  |  |
| 1 | Reverse Goods Receipt | Log on to SAP Launchpad with user Receiving Specialist (IOG).Access the app: Process Receipts.Enter the corresponding purchase order / inbound delivery number in filter.Choose Go.Click on the purchase order filtered out.Choose Reverse. | Goods receipt reversal popup is displayed. |  |
| 2 | Confirm Reversal | Enter the following details in the popup:Posting date: <select a date>.Document Header Text: <your note> (Optional).Choose Reverse. | Goods receipt reversal is posted.Confirmation message is displayed on reversal.Reversed material document number is displayed under follow-on-documents.Goods movement type is displayed as goods receipt for purchase order reversal (102 movement).Reversed quantity with negative value is displayed in both list page and object page.In case of two-step goods receipt reversal process, the goods movement type is 108 and 110 against 107 and 109 movement respectively.Note For quality-managed material:For any supply process: Inspection lot already created would be cancelled if usage decision is not done.For non-quality managed material:For SP13: Additionally, when goods receipts is reversed for a non-quality managed material, outbound delivery quantity will be set to zero and goods issue will be done automatically (if picking task is not confirmed).For SP14: When goods receipts is reversed for a non-quality managed material, outbound delivery quantity will be set to zero and goods issue will be done automatically (if picking task is not confirmed).In case outbound delivery is not distributed then outbound delivery is deleted. |  |
| 3 | Check Whether Outbound Delivery Quantity is Set to Zero | Access the app Message Dashboard.Set the filter to current date and go to Results list. | Filter is set to current date. |  |
| 4 | Results List | Under Results list, select the link for successfully processed number of documents corresponding to the row:RFC Monitoring for Field Logistics - /OILUF | Monitoring and Error Handling screen is displayed. |  |
| 5 | OBD Deletion for SP13 and SP14 | Under section Interface to Monitor qRFC OBD Creation - FLOG_OBD_CAN/1 note down the outbound delivery deleted. | Message for Outbound Delivery cancellation is displayed Outbound Delivery XXXX deleted.Note down the outbound delivery number. |  |
| 6 | STO Marked for Deletion for SP14 | Under section Interface to Monitor qRFC OBD Creation - FLOG_STO_CAN/1 note down the stock transport order created for the outbound delivery. | Message for stock transport order cancellation is displayed Stock Transport Order XXXXXX set for deletion.Note down the stock transport order number. |  |
|  | Case 2: Warehouse tasks for inbound or outbound delivery exist. |  |  |  |
| 7 | Reverse Goods Receipt | Log on to SAP Launchpad with user Receiving Specialist (IOG).Access the app: Process Receipts.Enter the corresponding purchase order or inbound delivery number in filter.Choose Go.Click on the purchase order filtered out.Choose Reverse. | Goods receipt reversal popup is displayed. |  |
| 8 | Confirm Reversal | Enter the following details in the popup:Posting date: <select a date>.Document header text: <your note>. (Optional)Choose Reverse. | Step 1: Cancel warehouse task pop up will appear and then proceed with OK.Warehouse Task 100000XXXX is Cancelled.Step 2: Now click on Reverse to reverse the goods receipt.Reversed receipt for selected item(s) of purchase order 018000XXXX.Goods receipt reversal is posted.Confirmation message is displayed on reversal.Reversed material document number is displayed in follow-on-documents tab.Goods movement type is displayed as goods receipt for purchase order reversal (102 movement).Reversed quantity with negative value is displayed in both list page and object page.In case of two-step goods receipt reversal process, the goods movement type is 108 and 110 against 107 and 109 movement respectively.Note For quality-managed material:For any supply process: Inspection lot already created would be cancelled if usage decision is not doneFor non-quality managed material:For SP13: Additionally, when goods receipts is reversed for a non-quality managed material, outbound delivery quantity will be set to zero and goods issue will be done automatically (if picking task is not confirmed).For SP14: When goods receipts is reversed for a non-quality managed material, outbound delivery quantity will be set to zero and goods issue will be done automatically (if picking task is not confirmed).In case outbound delivery is not distributed then outbound delivery is deleted instead of updating of quantity to zero. | Goods receipt reversal is posted. Outbound delivery quantity is set as 0. |
| 9 | Check Whether Outbound Delivery Quantity is set to zero | Access the app Message Dashboard.Set the filter to current date and go to results list. | Filter is set to current date. |  |
| 10 | Results List | Under results list, select the link for successfully processed number of documents corresponding to the row:RFC Monitoring for Field Logistics - /OILUF | Monitoring and Error Handling screen is displayed. |  |
| 11 | OBD Deletion for SP13 and SP14 | Under section Interface to Monitor qRFC OBD Creation - FLOG_OBD_CAN/1 note down the outbound delivery deleted. | Message for outbound delivery cancellation is displayed, Outbound Delivery XXXX deleted.Note down the outbound delivery number. | Outbound delivery quantity is set as 0 and goods issue is done. |
| 12 | STO Marked for Deletion for SP14 | Under section Interface to Monitor qRFC OBD Creation - FLOG_STO_CAN/1 note down the stock transport order created for the outbound delivery. | Message for stock transport order cancellation is displayed, Stock Transport Order XXXXXX set for deletion.Note down the stock transport order number. |  |

##### Warehouse Management Inactive in Base Plant

Purpose

You can perform goods receipt reversal for a non-quality managed material SP13, where warehouse managed location is inactive in base plant and goods receipt is done for inbound delivery.

Follow the prerequisites steps for creating the test data.

Prerequisites

1. Create a non-quality managed material of type SP13 FLOG-SP13-NO-QM.

The steps are documented in Configuration Guide for 40G scope item.

1. Create purchase info records for this material in FORP and FOBP plant.

The steps are documented in Configuration Guide for 40G scope item.

1. Follow the steps in [Create Maintenance Request](#unique_17) [page ] 15 and [Release Maintenance Order](#unique_21) [page ] 23 to create maintenance order for the material FLOG-SP13-NO-QM.
2. Execute the steps [Run Material Requirements Planning (MRP) at Remote Plant and Base Plant](#unique_22) [page ] 25 to [Convert Purchase Requisition to Purchase Order](#unique_23) [page ] 26 to create stock transport requisition and convert stock transport requisition to stock transport order with automatic purchase requisition creation in section [Convert Purchase Requisition to Purchase Order](#unique_23) [page ] 26 to [Check for Automatically Created Inbound Delivery from Purchase Order](#unique_24) [page ] 29 with storage location as FOBN.
3. Execute the steps with the purchase requisition number obtained from above step. Follow the procedures from [Run Material Requirements Planning (MRP) at Remote Plant and Base Plant](#unique_22) [page ] 25 to [Post Goods Receipt at Base Plant](#unique_26) [page ] 32.

|  |
| --- |
| Note To configure the userWAREHOUSE_CLERK_EWM contact your administrator. |

1. Execute steps in [Check Automatically Created Outbound Delivery](#unique_32) [page ] 51.

Note down the outbound delivery number.

Procedure

OBD Picking status: Not yet picked / partially picked / fully picked

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to Fiori launchpad as SHIPPING SPECIALIST.Access the app Change Outbound Delivery.Enter outbound delivery number noted from the prerequisites step 6. | Change Outbound Delivery screen is displayed. |  |
| 2 | Check Outbound Delivery Status | Under the Picking tab, select the picking quantity.Outbound delivery is either fully picked / partially picked / not yet picked.Under Goods Movement tab, select the goods movement status.Outbound delivery is fully picked / partially picked / not yet picked.In case goods movement status is C- completely processed, goods reversal of inbound delivery is not possible. | Outbound delivery is fully picked / partially picked / not yet picked.Outbound delivery has not posted goods Issue. |  |
| 3 | Reverse Goods Receipt: | Log on to SAP Launchpad with user Receiving Specialist (IOG)Access the app: Process Receipts.Enter the corresponding purchase order / inbound delivery number in filter.Choose Go.The purchase order would be displayed under Received tab.Click on the purchase order filtered out.Choose Reverse. | The Fiori launchpad is displayed.Reverse Goods Movement screen appears. |  |
| 4 | Post Goods Reversal Movement | Enter the following details in the popup:Posting date: <select a date>.Document Header Text: <your note>.Choose Reverse. | Goods receipt reversal is posted.Confirmation message is displayed on reversal.Reversed material document number is displayed in follow-on-documents tab.Goods movement type is displayed as goods receipt for purchase order reversal (102 Movement).Reversed quantity with negative value is displayed in both list page and object page.In case of two-step goods receipts reversal process, the goods movement type is 108 and 110 against 107 and 109 movement respectively.Note For Quality-Managed material:For any Supply process: Inspection lot already created would be cancelled.For Non-Quality Managed material:For SP13: Additionally, when goods receipts is reversed for a non-quality managed material, outbound delivery would be deleted automatically.For SP14: When goods receipts is reversed for a non-quality managed material, outbound delivery would be deleted automatically and stock transport order line item would be marked for deletion. |  |
| 5 | Check whether Outbound Delivery got Deleted: | Access the app Message DashboardSet the filter to current date and go to Results List. | Filter is set to current date |  |
| 6 | Results List | Under Results List, select the link for successfully processed number of documents corresponding to below row.RFC Monitoring for Field Logistics - /OILUF | Monitoring and Error Handling screen is displayed. |  |
| 7 | OBD Deletion for SP13 and SP14 | Under section Interface to Monitor qRFC OBD Creation - FLOG_OBD_CAN/1 note down the outbound delivery deleted. | Message for outbound delivery cancellation is displayed Outbound Delivery XXXX deleted.Note down the outbound delivery number. |  |
| 8 | STO Marked for Deletion for SP14 | Under section Interface to Monitor qRFC OBD Creation - FLOG_STO_CAN/1 note down the stock transport order created for the outbound delivery. | Message for stock transport order cancellation is displayed Stock Transport Order XXXXXX set for deletion.Note down the stock transport order number. |  |

### View Supply Process Document Flow

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Supply Chain Analyst (IOG). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Supply Process Document Flow app. | The Supply Process Document Flow screen is displayed. |  |
| 3 | View Maintenance Order | Make the following entries and choose Go.If maintenance order is not displayed in the Filters, choose Adapt Filters.On the Adapt Filters dialog box, find Basic and choose More Filters.Select the maintenance order and choose OK.Choose Go.Enter the maintenance order which was created in initial sections and then choose Go. | Maintenance order is displayed. |  |
| 4 | View Supply Process Document Flow | In the maintenance order for the FLOG-SP11 material line item, click the Chevron.This is applicable for SP11 version V1 and V3.Navigate to Supply Process Document Flow tab.Check block for maintenance order, Stock transfer request, stock transfer Order good receipt material document, outbound delivery number, stock transport order number, logistic outbound warehouse task number, goods receipt material document at remote plant, goods issue material document number at base plant are displayed correctly.In case of goods receipt reversal, the reverse document block will be displayed.Check the specific line item for purchase requisition / purchase order.In the maintenance order for the FLOG-SP12 material line item, click the Chevron.Navigate to Supply Process Document Flow tab.Check block for maintenance order, Stock requisition number, stock transfer order, good receipt material document, logistic outbound delivery number, stock transport order number, outbound warehouse task number, goods receipt material document at remote plant, goods issue material document number at base plant are displayed correctly.In case of goods receipt reversal, the reverse document block will be displayed.In the maintenance order for the FLOG-SP13 material line item, click the Chevron.This is applicable for SP13 version V1 and V3.Navigate to Supply Process Document Flow tab.Check block for maintenance order, stock transfer request, stock transfer order, purchase requisition, purchase order processing, logistic inbound delivery, good receipt material document, logistic outbound delivery number, stock transport order number, inbound warehouse task number, outbound warehouse task number, goods receipt material document at remote plant, goods issue material document number at base plant are displayed correctly.In case of goods receipt reversal, the reverse document block will be displayed.Check the specific line item for purchase requisition / purchase order.In the maintenance order for the FLOG-SP14 material line item, click the Chevron.This is applicable for SP14 version blank, V1, and V4.Navigate to Supply Process Document Flow tab.Check block for maintenance order, requisition processing, purchase order processing, logistic inbound delivery, good receipt material document, logistic outbound delivery number, stock transport order number, inbound warehouse task number, outbound warehouse task number, goods receipt material document at remote plant, goods issue material document number at base plant and goods issue document against the maintenance order (if done already) are displayed correctly.In case of goods receipt reversal, the reverse document block will be displayed.Check the specific line item for purchase requisition / purchase order.Note The Supply Process Document Flow app shows the document flow specific to the line item selected from the list view. | All order numbers and document number will be displayed correctly with the status.The document flow and corresponding statuses is displayed for the maintenance order. |  |

### Physical Inventory Process for Field Logistics Materials at Base Plant

Perform the steps as mentioned in scope item 3BX - Warehouse Physical Inventory for materials stockable at base plant FOBP with the following parameters:

- Warehouse numbers: FOBP
- Storage location: FOBW
- Party entitled to dispose: BP1001489
- Material: FLOG-SP12/ FLOG-SP11

### Physical Inventory Process for Field Logistics Materials at Remote Plant

Perform the steps mentioned in scope item BML - Physical Inventory -Inventory Count and Adjustment for materials stockable at remote plant FORP with the following parameters:

- Plant: FORP
- Storage Location: FORN
- Material: FLOG-SP11, FLOG-SP13

### Field Logistics Returns Process

Prerequisites

- The Field Logistics Forward process is executed and stock is available to return from remote location.
- To ensure stock is available at remote location, execute partial Goods Issue to the order while executing Forward process.

#### Return by Maintenance Order

You can return the product from the remote location to the vendor with or without warehouse.

##### Return to Inventory and Create Return Draft

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The maintenance technician informs the material coordinator at the remote location that some materials issued to the maintenance order were not used and can be returned. These materials must be placed back into remote stock before initiating return.

|  |
| --- |
| Note You can use the maintenance order for which quantity has been issued (withdrawn quantity field). |

You can process the returns for a Supply Process SP14 product with respect to the maintenance order which has brought it to stock using the Initiate Returns - By maintenance order (F4682) application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (IOG). | The SAP Fiori launchpad displays. |  |
| 2 | Launch the App | Open Initiate Returns - By maintenance order (F4682) app. | The Initiate Returns screen is displayed. |  |
| 3 | Set Maintenance Order in Filter Settings | On the Initiate Returns screen, maintenance order is a mandatory filter.Maintenance Order: XXXX.(Input order created for FLOG-SP14.)Choose Go. | The maintenance order is set and components for the selected maintenance order is displayed. |  |
| 4 | Select a Product | Select the product FLOG-SP14.The aggregated requested quantity, withdrawn quantity and returned quantity is displayed.Choose Chevron. | Item navigates to the object page. |  |
| 5 | Execute Back to Remote Stock | Navigate to tab Reservation Item.Item with negative line item is displayed in the Reservation Item table.Choose Return to Stock. | A pop up is displayed to enter the storage location and the quantity for which the goods issue should be reversed. |  |
| 6 | Select Back to Remote Stock | Enter the following details:Quantity Withdrawn: 1 EAStorage Location: FORNInitiate Returns: Un CheckedChoose Return to Stock. | Stock quantity would be increased in the Initial screen to be verified.The below messages appear:“The item <Reservation Item number> with reservation <Reservation number> is returned to stock”.Note If the recipient location is maintained in the maintenance order and the corresponding configurations are maintained for warehouse management, the warehouse task must have the staging area of the recipient location as the source bin.Note Checking the Initiate Returns checkbox would automatically create a return draft after posting the movement.The batch / serial / valuation type details for the stock are displayed. |  |
| 7 | Select Initiate Returns | The object page displays the product details, reservation item details (purchasing information) and the return history (returned request information).Choose Initiate Returns. | Returns Initiation tab is displayed. |  |
| 8 | Create the STO | Enter below details in Return Initiation tab.Returnable Quantity: 1EARemote Storage Location: FORN / FORHBatch, Serial Number and Valuation Type details if the product is batch or serial managed or has a valuation type.Choose Save. | A pop up appears Stock transport order xxxxxxxxx created. Status would be set as Return Requested. Do you wish to Navigate to the Item. Clicking on Yes will navigate you to the item in the Initiate Returns - By product (F4252) app.Batch and serial number are now displayed for the STO.Make a note of the STO number. |  |
| 9 | Perform Initiate Returns for other Supply Processes (Optional) | Steps 3-10 can be performed for other supply processes by using the appropriate maintenance order for those SPs. |  |  |

|  |
| --- |
| Note The Return to Stock option in list page, brings the whole withdrawn quantity back to stock. Example: If 5EA is the withdrawn quantity, stock quantity increases by 5 after back to remote stock is done.In case of returning stock back to warehouse managed remote location, the goods issue reversal posting creates an inbound delivery for which the goods issue and warehouse task is created. The inbound delivery created can be viewed in the document flow section of Display Maintenance Order application. The warehouse task for the inbound delivery created need to be confirmed in Confirm Warehouse Tasks application (Warehouse_Clerk_EWM).When the Maintenance Technician executes the final confirmation for maintenance orders in the Perform Maintenance Jobs (F5104A) application, a return can be initiated from the Perform Maintenance Jobs (F5104A) application itself, or can be initiated by following the procedures mentioned in this section. While final confirmation is executed, the Warehouse Clerk (IOG) receives a notification regarding the products in the operation being confirmed to initiate the required action. The final confirmation in the Perform Maintenance Job application can be referred from the scope item 4HH, section Execute Maintenance Order.While executing the Return to Stock, the final issue is set for the reservation item, confirming the requirement is closed. |

#### Initiate Returns by Product

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can process the returns for a Supply Process SP14 product with respect to the maintenance order which has brought it to stock using the Initiate Returns - By product (F4252) application.

|  |
| --- |
| Note The following steps can be performed in continuation to [Return by Maintenance Order](#unique_68) [page ] 100 or initiate a new return process for available products in the remote plant inventory. |

Prerequisite

Ensure that the following entries are maintained for default recommended action from the Setting Up Field Logistics Planning and Execution (40G) document in the system to perform the below steps.

|  |
| --- |
| Note This is an example table to help with the below scenario |

Maintain Default Recommended Action to Initiate Returns

| Supply Process | Recommended Action |
| --- | --- |
| SP11 | Return for Repair / Recertify |
| SP12 | Return to base inventory |
| SP13 | Temporary Storage |
| SP14 | Return to vendor |

##### Create Replenishment Delivery

Purpose

You can create a replenishment delivery using any one of the following options:

- Initiate Returns - By product (F4252) app - User can create a delivery along with an STO.
- My Purchase Orders Due for Delivery app - User can create a delivery separately using the STO.

###### Replenishment Delivery Using Initiate Returns by Product App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create a replenishment delivery for the STO directly from the Initiate Returns by Product app by entering the required data. The recommended action is defaulted based on the value maintained in SSUI per supply process.

Procedure

Initiate Returns without Scanning

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (IOG). | The SAP Fiori launchpad displays. |  |
| 2 | Launch the App | Open Initiate Returns - By product (F4252) app. | The Initiate Returns screen is displayed. |  |
| 3 | Set Default Plants as Application Setting | On the Initiate Returns screen, in the user settings for the app, choose App settings.This needs to be done only for the initial login (one-time setting).Enter the base plant FOBP and remote plant FORP. | The base and remote plant are set.Base plant and remote plant set. message is displayed. |  |
| 4 | Select Remote Plant in Filter Settings | Plant is a mandatory filter, select the remote plant FORP. | The remote plant is set. |  |
| 5 | Search for Reference Document Number | On the Initiate Returns screen, enter the STO number from the step in [Return by Maintenance Order](#unique_68) [page ] 100 in the reference document filter.(If field is not visible, select from Adapt Filters). | The Reference document number is displayed with return status as Return Draft. |  |
| 6 | Select the Line for the Reference Document Number | Select the line item for the Reference document number, which is in Return Draft status and click on Chevron. | The item navigates to the object page. |  |
| 7 | Verify the Storage Bin (Optional) | Verify the value of the field storage bin under Additional Details section. | The value in the field storage bin is auto updated from the product master. |  |
| 8 | Enter Remaining Details for the Returns | Choose Edit.Enter the below details in the object page to request for return:Base Storage Location: FOBN (FOBW for warehouse scenario)Recommended Action: Return to Vendor (The recommended action is defaulted)Returnable Quantity in Order unit: 1 EASelect Create Outbound Deliv checkbox (if outbound delivery has to be created along with STO).Save your changes.Note User can override the defaulted recommended action if required. | The return entry is saved with the provided details.The status is updated to Return Scheduled.The batch, serial number, and valuation type information for the product is displayed in the STO. |  |
| 9 | Verify Documents in Document Flow | Go to document flow section and check the documents created. | Document section will have all the documents created from Initiate Returns by maintenance order till the current step. |  |
| 10 | Initiate Returns for SP11 Material | Go to the list page of Initiate Returns and select the line item FLOG-SP11, which is in At Remote status and click on Chevron. | The item navigates to the object page. |  |
| 11 | Verify the Storage Bin (Optional) | Verify the value of the field storage bin under Additional Details section. | The value in the field storage bin is auto updated from the product master. |  |
| 12 | Initiate Returns for SP11 Material | Choose Initiate Return.Enter the below details in the object page to request for return:Base Storage Location: FOBN (FOBW for warehouse scenario)Recommended Action: Return for Repair/Recertify (The recommended action is defaulted)Returnable Quantity in Order unit: 1 EASelect Create Outbound Deliv checkbox (if outbound delivery has to be created along with STO).Save your changes.Note User can override the defaulted recommended action if required. | A pop up appears with the created returns STO which is in status Return Scheduled.The batch, serial number, and valuation type information for the product is displayed in the STO.Note In the object page, if user initiates returns for multiple line items i.e. line items of same material having different Batch/Serial number/Valuation type, then a single STO with multiple line items is created. Each line in the STO will correspond to the Batch/Serial Number/Valuation type that was selected. |  |
| 13 | Initiate Returns for SP11 Material | Click on No in the navigation pop up. |  |  |
| 14 | Initiate Returns for SP12 Material | Repeat step 10 for FLOG-SP12 material. |  |  |
| 15 | Verify the Storage Bin (Optional) | Verify the value of the field storage bin under Additional Details section. | The value in the field storage bin is auto updated from the product master. |  |
| 16 | Initiate Returns for SP12 Material | Choose Initiate Return.Enter the below details in the object page to request for return:Base Storage Location: FOBN (FOBW for warehouse scenario)Recommended Action: Return for Return to base inventory (The recommended action is defaulted)Returnable Quantity in Order Unit: 1 EASelect Create Outbound Deliv checkbox (if outbound delivery has to be created along with STO).Save your changes.Note User can override the defaulted recommended action if required. | A pop up appears with the created returns STO which is in status Return Scheduled.The batch, serial number, and valuation type information for the product is displayed in the STO.Note In the object page, if user initiates returns for multiple line items i.e. line items of same material having different Batch/Serial number/Valuation type, then a single STO with multiple line items is created. Each line in the STO will correspond to the Batch/Serial Number/Valuation type that was selected. |  |
| 17 | Initiate Returns for SP12 Material | Click on No in the navigation pop up. |  |  |
| 18 | Initiate Returns for SP13 Material | Repeat step 10 for FLOG-SP13 material. |  |  |
| 19 | Verify the Storage Bin (Optional) | Verify the value of the field storage bin under Additional Details section. | The value in the field storage bin is auto updated from the product master. |  |
| 20 | Initiate Returns for SP13 Material | Choose Initiate Return.Enter the below details in the object page to request for return:Base Storage Location: FOBN (FOBW for warehouse scenario)Recommended Action: Return for Temporary Storage (The recommended action is defaulted)Returnable Quantity in Order Unit: 1 EAReference Maintenance Order: Choose valid maintenance order from the list.Select Create Outbound Deliv checkbox (if outbound delivery has to be created along with STO).Save your changes.Note User can override the defaulted recommended action if required. | A pop up appears with the created returns STO which is in status Return Scheduled.The batch, serial number, and valuation type information for the product is displayed in the STO.Note In the object page, if user initiates returns for multiple line items i.e. line items of same material having different Batch/Serial number/Valuation type, then a single STO with multiple line items is created. Each line in the STO will correspond to the Batch/Serial Number/Valuation type that was selected. |  |
| 21 | Initiate Returns for SP13 Material | Click on No in the navigation pop up. |  |  |

Initiate Returns using Scan Option

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (IOG). | The SAP Fiori launchpad displays. |  |
| 2 | Launch the App | Open Initiate Returns - By product (F4252) app. | The Initiate Returns screen is displayed. |  |
| 3 | Set Default Plants as Application Setting | On the Initiate Returns screen, in user settings for the app, choose App settings.This needs to be done only for the initial login (one-time setting).Enter the base plant FOBP and remote plant FORP. | The base and remote plant are set.Base plant and remote plant set. message is displayed. |  |
| 4 | Select Remote Plant in Filter Settings | Plant is a mandatory filter, select the remote plant FORP. | The remote plant is set. |  |
| 5 | Scan HU or Product Label | On the Initiate Returns screen, choose Scan.(If field is not visible, select from Adapt Filters). | The fields are populated with the entries in the barcode or QR code, and the list page is displayed with the filter selection. |  |
| 6 | Select the Line for the Reference Document Number | Select the line item for the reference document number, which is in Return Draft status.Choose Chevron. | The item navigates to the object page. |  |
| 7 | Verify the Storage Bin (Optional) | Verify the value of the field storage bin under Additional Details section. | The value in the field storage bin is auto updated from the product master. |  |
| 8 | Enter Remaining Details for the Returns | Choose Edit.Enter the below details in the object page to request for return:Base Storage Location: FOBN (FOBW for warehouse scenario)Recommended Action: Return to Vendor (The recommended action is defaulted)Returnable Quantity in Order Unit: 1 EASelect Create Outbound Deliv checkbox (if outbound delivery has to be created along with STO).Save your changes.Note User can override the defaulted recommended action if required. | The return entry is saved with the provided details.The status is updated to Return Scheduled.The batch, serial number, and valuation type information for the product is displayed in the STO. |  |
| 9 | Verify Documents in Document Flow | Go to document flow section and check the documents created. | Document section will have all the documents created from Initiate Returns by maintenance order till the current step. |  |
| 10 | Initiate Returns for SP11 Material | Go to the list page of Initiate Returns and select the line item FLOG-SP11, which is in At Remote status and click on Chevron. | The item navigates to the object page. |  |
| 11 | Verify the Storage Bin (Optional) | Verify the value of the field storage bin under Additional Details section. | The value in the field storage bin is autoupdated from the product master. |  |
| 12 | Initiate Returns for SP11 Material | Choose Initiate Return.Enter the below details in the object page to request for return:Base Storage Location: FOBN (FOBW for warehouse scenario)Recommended Action: Return for Repair/Recertify (The recommended action is defaulted)Returnable Quantity in Order Unit: 1 EASelect Create Outbound Deliv checkbox (if outbound delivery has to be created along with STO).Save your changes.Note User can override the defaulted recommended action if required. | A pop up appears with the created returns STO which is in status Return Scheduled.The batch, serial number, and valuation type information for the product is displayed in the STO.Note In the object page, if user initiates returns for multiple line items i.e. line items of same material having different Batch/Serial number/Valuation type, then a single STO with multiple line items is created. Each line in the STO will correspond to the Batch/Serial Number/Valuation type that was selected. |  |
| 13 | Initiate Returns for SP11 Material | Click on No in the navigation pop up. |  |  |
| 14 | Initiate Returns for SP12 Material | Repeat step 10 for FLOG-SP12 material. |  |  |
| 15 | Verify the Storage Bin (Optional) | Verify the value of the field storage bin under Additional Details section. | The value in the field storage bin is auto updated from the product master. |  |
| 16 | Initiate Returns for SP12 Material | Choose Initiate Return.Enter the below details in the object page to request for return:Base Storage Location: FOBN (FOBW for warehouse scenario)Recommended Action: Return for Return to base inventory (The recommended action is defaulted)Returnable Quantity in Order Unit: 1 EASelect Create Outbound Deliv checkbox (if outbound delivery has to be created along with STO).Save your changes.Note User can override the defaulted recommended action if required. | A pop up appears with the created returns STO which is in status Return Scheduled.The batch, serial number, and valuation type information for the product is displayed in the STO.Note In the object page, if user initiates returns for multiple line items i.e. line items of same material having different Batch/Serial number/Valuation type, then a single STO with multiple line items is created. Each line in the STO will correspond to the Batch/Serial Number/Valuation type that was selected. |  |
| 17 | Initiate Returns for SP12 Material | Click on No in the navigation pop up. |  |  |
| 18 | Initiate Returns for SP13 Material | Repeat step 10 for FLOG-SP13 material. |  |  |
| 19 | Verify the Storage Bin (Optional) | Verify the value of the field storage bin under Additional Details section. | The value in the field storage bin is auto updated from the product master. |  |
| 20 | Initiate Returns for SP13 Material | Choose Initiate Return.Enter the below details in the object page to request for return:Base Storage Location: FOBN (FOBW for warehouse scenario)Recommended Action: Return for Temporary Storage (The recommended action is defaulted)Returnable Quantity in Order Unit: 1 EAReference Maintenance Order: Choose valid maintenance order from the list.Select Create Outbound Deliv checkbox (if outbound delivery has to be created along with STO).Save your changes.Note User can override the defaulted recommended action if required. | A pop up appears with the created returns STO which is in status Return Scheduled.The batch, serial number, and valuation type information for the product is displayed in the STO.Note In the object page, if user initiates returns for multiple line items i.e. line items of same material having different Batch/Serial number/Valuation type, then a single STO with multiple line items is created. Each line in the STO will correspond to the Batch/Serial Number/Valuation type that was selected. |  |
| 18 | Initiate Returns for SP13 material | Click on No in the navigation pop up. |  |  |

###### Replenishment Delivery using My Purchase Orders Due for Delivery App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create a replenishment delivery for the STO.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori App | Open My Purchase Orders Due for Delivery app. | The My Purchase Orders Due for Delivery screen is displayed. |  |
| 3 | Provide Inputs | On the Purchase Orders tab page, enter the STO, which was created in [Initiate Returns by Product](#unique_70) [page ] 103.Clear the other fields.Choose Execute. | The STO is displayed. |  |
| 4 | Select the STO | On the My Purchase Orders screen, select the STO and choose Background. | The delivery is created and can be displayed in logs. |  |
| 5 | Display Delivery | Select the option More and click on Show/Hide Delivery. | The delivery is displayed.Note If the STO has multiple line items each with its own Batch/Serial Number/Valuation type, then the Outbound delivery will also be created with multiple line items and it will inherit the Batch/Serial Number/Valuation type of the STO. |  |
| 6 | Open Delivery | Choose the Delivery Number. | Display Delivery is displayed. |  |

##### Change the Returns STO - Confirmation Control key (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can display the STO created for the returns from the remote to base plant and update the confirmation control key if inbound delivery is needed for goods receipt.

This step is only required if inbound delivery is required and is optional.

|  |
| --- |
| Note For warehouse managed base storage location, the confirmation control key is updated while creating STO. Hence, this step is not required. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access Fiori Launchpad | Open Change Purchase Order - Advanced (ME22N) app. | The Change Purchase Order screen is displayed. |  |
| 3 | Set Remote Plant | On the Change Purchase Order screen, choose Other Purchase Order and enter the STO created in [Return by Maintenance Order](#unique_68) [page ] 100. | The returns STO is displayed in change mode. |  |
| 4 | Enter Confirmation Control Key | At the item level, enter the following:Storage location - Base storage location as entered in the step [Initiate Returns by Product](#unique_70) [page ] 103.Confirmations Control key: 0004Save the changes. | The STO is created, and the confirmation control and storage location are updated. |  |

##### Pick and Pack Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can pick and pack the items for which return was requested through the Initiate Returns - By product (F4252) application, for the delivery.

|  |
| --- |
| Note If picking is done for partial quantity, another STO must be triggered for returning the remaining quantity as partial delivery indicator in STO is updated as B (create only one delivery). |

|  |
| --- |
| NoteThe picking is not done from the Initiate Returns - By product (F4252) application for remote location which is warehouse managed, for example, the load quantity field is disabled. Once user enters the source storage bin, warehouse task is created and the user can navigate to the warehouse task from the document flow to confirm it.Note that returns process for warehouse managed location, follows pick and pack strategy. |

Procedure

Table 6: LE at Remote:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk (IOG). | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori App | Open Initiate Returns - By product (F4252) app. | The Initiate Returns screen is displayed. |  |
| 3 | Search Item to be Dispatched | On the Initiate Returns screen, search with the status Return Scheduled or reference document created in step [Create Replenishment Delivery](#unique_71) [page ] 104.Choose Go. | The item with material and status is displayed. |  |
| 4 | Select Item | On the Initiate Returns screen, select the line item with status Return Scheduled for the STO created earlier. | The object page is displayed. |  |
| 5 | Enter Load Quantity | On the object page, enter the load quantity, which is the goods issue quantity and save. | Load quantity is saved and the status of item is updated to Ready for Dispatch.The delivery is picked. |  |
| 6 | Pack (Optional) | Click on Maintain HU. Enter following details:Packaging material: Cartons / Pallets (for example)Quantity: < >Click on Create. | Handling units are created and packed for the outbound delivery. |  |

Table 7: Warehouse Managed at Remote:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk (IOG). | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori App | Open Initiate Returns - By product (F4252) app. | The Initiate Returns screen is displayed. |  |
| 3 | Search Item to be Dispatched | On the Initiate Returns screen, search with the status Return Scheduled or reference document created in step [Create Replenishment Delivery](#unique_71) [page ] 104.Choose Go. | The item with material and status is displayed. |  |
| 4 | Select Item | On the Initiate Returns screen, select the line item with status Return Scheduled for the STO created earlier. | The object page is displayed. |  |
| 5 | Enter Source Storage Bin | In edit mode, source storage bin field is enabled. Click on value help to select the source storage bin. For example, CL-AREA.Click on Save. | Warehouse task is created with source storage bin as CL-AREA, which is displayed in the returns document flow section.Note Warehouse task can be confirmed in Process Warehouse Tasks application in Warehouse_Clerk_EWM role. Once confirmed, the returns stock transport order status is updated to ready for dispatch. If the Warehouse_Clerk_EWM role is assigned the user can navigate and confirm it from the document flow section. |  |
| 6 | Pack | For Returns STO from warehouse managed remote location (FORH), click on Maintain HU to enter following details:Packaging material: < >Click on Create. | For the outbound delivery order, handling units are created and are linked to the warehouse task. |  |

|  |
| --- |
| Note If the pick warehouse task is not created via the returns application and you chose to create and confirm the same using the standard warehouse managed apps, the picking status shall still get updated in the returns applications for example, the resultant status would now be ready for dispatch. |

##### Print Label (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can print the labels for selected items for which return was requested through the Initiate Returns - By product (F4252) application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (IOG). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Initiate Returns - By product (F4252). | The Initiate Returns - By product screen is displayed. |  |
| 3 | Select Remote Plant in Filter Settings | Plant is a mandatory filter, select the remote plant FORP. | The remote plant is set. |  |
| 4 | Search for Reference Document Number | Select the line item for the reference document number using the Adapt Filters. | The item is selected. |  |
| 5 | Print Preview | Navigate inside the line item and click on Preview HU Label. | The handling unit label is previewed. |  |
| 6 | Print Preview | Navigate inside the line item and click on Preview Product Label. | The product label is previewed. |  |
| 7 | Print Label | On the Initiate Returns list page screen, choose Print.Choose Product Label or HU Label.Note: HU label can be printed in all status except At Remote, Return Draft and Return Requested status. Product label can be printed in all status except At Remote. | The Product or HU label for the selected item is printed (the print queue can be checked in the Manage Output Items application with Administrator user). |  |

##### Dispatch Goods

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can dispatch the items for which return was requested through the Initiate Returns - By product (F4252) application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk (IOG). | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori App | Open Initiate Returns - By product (F4252) app. | The Initiate Returns screen is displayed. |  |
| 3 | Search item to be Dispatched | On the Initiate Returns screen, search with the status Return Scheduled or reference document created in step [Create Replenishment Delivery](#unique_71) [page ] 104.Choose Go. | The item with material and status is displayed. |  |
| 4 | Dispatch Item | Select the item from the worklist, which is in status Ready for Dispatch.Choose Dispatch. | The items are dispatched from the remote location. |  |
| 5 | Select Item | Select the line item with status Dispatched.Choose Chevron. | The object page is displayed. |  |
| 6 | Verify Document Flow | To view the document flow, scroll down in the object page. | The documents created is displayed starting from Returns STO, OBD, GI and IBD.Note down the inbound delivery number. |  |

##### Receive Goods at Base

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can receive the delivery items and items assigned to handling units at base and trigger further processes based on handling decision, which were dispatched through the Initiate Returns - By product (F4252) app or the Process Cross-Plant Receipts (F4713) application.

|  |
| --- |
| Note The LE scenario with handling unit is not supported in the Process Cross-Plant Receipts (F4713) application. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk (IOG). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Cross-Plant Receipts (F4713) app. | The Process Cross-Plant Receipts screen is displayed. |  |
| 3 | Set the Supplying Plant | In the Process Cross-Plant Receipts screen, supplying plant is a mandatory setting.Enter Destination Plant: FOBPChoose Go. | The container IDs dispatched from remote locations are displayed in the List Overview. |  |
| 4 | Select Reference Document | Select the reference document number from Delivery Item tab. | Reference documents has status Dispatched. |  |
| 5 | Scan Label (optional) | Instead of manual selection, product or HU label can be scanned.Choose Scan to scan the barcode or the QR code. | Scanned values from the barcode is filtered and displayed in the list page.Note Handling unit label items, once scanned are auto received. Status is updated to Received on scanning. |  |
| 6 | Update Handling Decision (optional) | Choose Edit.Handling Decision is enabled for the product with status Dispatched.Select a different handling decision from dropdown.Choose Save. | Handling decision is set, but the product status remains same. |  |
| 7 | Update Visual Inspection (optional) | Choose Edit.The field visual inspection is open for editing.Choose from the dropdown and save.Choose Save. | The visual inspection field is updated. |  |
| 8 | Verify the Storage Bin (Optional) | Verify the value of the field storage bin under general information. | The value in the field storage bin is autoupdated from the product master. |  |
| 9 | Receive the Repair / Recertify Line item (FLOG-SP11) | Select the product in the item list.Choose Receive. | Product status updated from Dispatched (Black) to Received (Green).Goods receipt for the selected item is posted in backend.Note down the warehouse task (warehouse managed), Subcontracting purchase order numberNote If the warehouse task creation fails due to lock issues in the IBD they can be verified using the AIF/ERR transaction. Once verified, either re-trigger the AIF entry or manually create the warehouse task using the app Change Inbound deliveries – deliveries.In case of any error the status is updated to Receipt in Process (Yellow).All the documents generated are visible in the document flow section.Note The handling decisions are defaulted based on recommended action.If the material was a Quality Managed Material, the Field Inspection lot and the document flow would be updated with the Inspection lot value along with the option to navigate to the new inspection lot. |  |
| 10 | Resend Notification to the Team | Choose Notify. | A notification email is sent to the team of users as configured. |  |
| 11 | Reverse the Goods Receipt (Optional) | The Goods Receipt created in the above step can be cancelled using the Post Goods Movement app (Change Inbound deliveries – deliveries for Warehouse managed items). | Product status gets reverted to Dispatched from Received.Goods Receipt is deleted and removed from the field.Subcontracting Purchase order is deleted and removed from the field.The above documents are removed from the document flow section.Note For warehouse managed products, the warehouse task needs to be cancelled for the Goods Receipt Reversal. |  |
| 12 | Receive the Return to Base Inventory Line Item (FLOG-SP12) | Select the product in the item list.Choose Receive. | Product status updated from Dispatched (Black) to Received (Green).Goods receipt for the selected item is posted in backend.Note down the warehouse task (warehouse managed).Note If the warehouse task creation fails due to lock issues in the IBD they can be verified using the AIF/ERR transaction. Once verified, either re-trigger the AIF entry or manually create the warehouse task using the app Change Inbound deliveries – deliveriesIn case of any error the status is updated to Receipt in Process (Yellow).All the documents generated are visible in the document flow section.Note The handling decisions are defaulted based on recommended action.If the material was a Quality Managed Material, the Field Inspection lot and the document flow would be updated with the Inspection lot value along with the option to navigate to the new inspection lot. |  |
| 13 | Resend Notification to the Team | Choose Notify. | A notification email is sent to the team of users as configured. |  |
| 14 | Reverse the Goods Receipt (Optional) | The Goods Receipt created in the above step can be cancelled using the Post Goods Movement app (Change Inbound deliveries – deliveries for Warehouse managed items). | Product status gets reverted to Dispatched from Received.Goods Receipt is deleted and removed from the field.The above document is removed from the document flow section.Note For warehouse managed products, the warehouse task needs to be cancelled for the Goods Receipt Reversal. |  |
| 15 | Receive the Temporary Storage Line Item (FLOG-SP13) | Select the product in the item list.Choose Receive. | Product status updated from Dispatched (Black) to Received (Green).Goods receipt for the selected item is posted in backend.Note down the warehouse task (warehouse managed), stock transport order number.Note If the warehouse task creation fails due to lock issues in the IBD they can be verified using the AIF/ERR transaction. Once verified, either re-trigger the AIF entry or manually create the warehouse task using the app Change Inbound deliveries – deliveriesNote down the outbound delivery numberIn case of any error the status is updated to Receipt in Process (Yellow).All the documents generated are visible in the document flow section.Note The handling decisions are defaulted based on recommended action.If the material was a Quality Managed Material, the Field Inspection lot and the document flow would be updated with the Inspection lot value along with the option to navigate to the new inspection lot. |  |
| 16 | Resend Notification to the Team | Choose Notify. | A notification email is sent to the team of users as configured. |  |
| 17 | Reverse the Goods Receipt (Optional) | The Goods Receipt created in the above step can be cancelled using the Post Goods Movement app (Change Inbound deliveries – deliveries for Warehouse managed items). | Product status gets reverted to Dispatched from Received.Goods Receipt is deleted and removed from the field.Stock Transport order is deleted and removed from the field.Outbound delivery is deleted.The above documents are removed from the document flow section.Note For warehouse managed products, the warehouse task needs to be cancelled for the Goods Receipt Reversal. |  |
| 18 | Receive the Return to Vendor Line Item (FLOG-SP14) | Select the product in the item list.Choose Receive. | Product status updated from Dispatched (Black) to Received (Green).Goods receipt for the selected item is posted in backend.Note down the warehouse task (warehouse managed), returns purchase order number.Note If the warehouse task creation fails due to lock issues in the IBD they can be verified using the AIF/ERR transaction. Once verified, either re-trigger the AIF entry or manually create the warehouse task using the app Change Inbound deliveries – deliveriesIn case of any error the status is updated to Receipt in Process (Yellow).All the documents generated are visible in the document flow section.Note The Returns Purchase order field is editable even after the item is received. The user can maintain the Return Purchase order as neededThe handling decisions are defaulted based on recommended action.If the material was a Quality Managed Material, the Field Inspection lot and the document flow would be updated with the Inspection lot value along with the option to navigate to the new inspection lot. |  |
| 19 | Resend Notification to the Team | Choose Notify. | A notification email is sent to the team of users as configured. |  |
| 20 | Reverse the Goods Receipt (Optional) | The Goods Receipt created in the above step can be cancelled using the Post Goods Movement app (Change Inbound deliveries – deliveries for Warehouse managed items). | Product status gets reverted to Dispatched from Received.Goods Receipt is deleted and removed from the field.Returns Purchase order is deleted and removed from the field.The above documents are removed from the document flow section.Note For warehouse managed products, the warehouse task needs to be cancelled for the Goods Receipt Reversal. |  |

##### Verify Returns Process Flow (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can view status update after goods are received at the base in the Initiate Returns - By product (F4252) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk (IOG). | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori App | Open Initiate Returns - By product (F4252) app. | The Initiate Returns screen is displayed. |  |
| 3 | Select item | Filter the STO created in the [Create Replenishment Delivery](#unique_71) [page ] 104 step by entering it in reference document field (If not visible, select it from Adapt Filters). | STO line status is Received at Base. |  |
| 4 | Choose Chevron | Choose Chevron. | STO details are displayed in the object page. |  |
| 5 | View Document Flow | Choose the tab Return Document Flow. | The goods receipt document and warehouse tasks are displayed. |  |

##### Confirm Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A putaway list is printed and handed over to the warehouse operative. The person can perform the warehouse tasks and confirm them in the system.

|  |
| --- |
| Note The warehouse clerk can also confirm the warehouse tasks using the app Warehouse Monitor (Business Catalog WM - Monitoring). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Warehouse Tasks app. |  |  |
| 3 | Enter Warehouse Task Number | On the Process Warehouse Tasks screen, select warehouse task number (created in [Receive Goods at Base](#unique_78) [page ] 118).Choose Go. |  |  |
| 4 | Select Warehouse Task | Select the warehouse task. |  |  |
| 5 | Confirm Warehouse Task | Choose Confirm. | The message Warehouse task confirmed. is displayed. |  |

##### Manage Request for Inspecting Items (Optional)

This section provides next steps of the process when handling decision is request for inspection.

###### Assign Inspection Plan and Record Inspection Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To record inspection results for a single inspection lot, execute the following process flow.

Prerequisite

In this scope item, the inspection lot is created automatically upon goods receipt for the purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A). | The Record Inspection Lots screen is displayed. |  |
| 3 | Select Filters | Make the following entries and choose Go.Purchase Document:STO created in the step [Create Replenishment Delivery](#unique_71) [page ] 104.If purchase order is not displayed in the filters, choose Adapt Filters.On the dialog box Adapt Filters, select Procurement and choose More Filters.Select Purchase Document and choose OK. Choose Go. | Inspection lot is displayed. |  |
| 4 | Select Inspection Lot | In the inspection lot list, select the corresponding inspection lot. | Inspection lot is displayed.Make a note of the inspection lot number. |  |
| 5 | Choose Record Results | Choose Record Multiple Results in the right bottom. |  |  |
| 6 | Enter Inspection Result | Depending on the inspection result, select one of the following two options:Positive Result:Surface: Code Group - Code SURFACE 0020 (Smooth)Length: Mean Value (cm): 160Negative Result:Surface: Code Group - Code SURFACE 0010 (Rough)Length: Mean Value (cm): 90 | For qualitative characteristic (surface) the search help is needed to select a value. For the quantitative characteristic (length) a number can be entered directly.The default number of inspected objects is calculated based on the sample size reviewed in an earlier step. The number of inspected objects can be manually changed. A number of nonconforming objects can be maintained directly in the respective fields as well for every inspection characteristic.With the app Record Results – Hierarchical View, a user can exceptionally overrule the automatic evaluation, for example, to document that the tolerance is always at the upper limit, then the generic defect ‘tolerance issue’ will be used. |  |
| 7 | Save Inspection Lot | Choose Save. | The inspection lot is saved. QM inspection for procurement goods has been performed and result recorded. |  |

###### Record Inspection Results (Optional - Warehouse Managed Scenario)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Record inspection results for a single inspection lot.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A). | The Record Inspection Lots screen is displayed. |  |
| 3 | Select Filters | Make the following entries and choose Go.Purchase Document:STO created in the [Create Replenishment Delivery](#unique_71) [page ] 104.If purchase order is not displayed in the filters, choose Adapt Filters.On the dialog box Adapt Filters, select Procurement and choose More Filters.Select Purchase Document and choose OK. Choose Go. | Inspection lot is displayed. |  |
| 4 | Select Inspection Lot | In the inspection lot list, select the corresponding inspection lot. | Inspection lot is displayed.Make a note of the inspection lot number. |  |
| 5 | Choose Record Results | Choose Record Multiple Results in the right bottom. |  |  |
| 6 | Enter Inspection Result | Depending on the inspection result, select one of the following two options:Positive Result:Surface: Code Group - Code SURFACE 0020 (Smooth)Length: Mean Value (cm): 160Negative Result:Surface: Code Group - Code SURFACE 0010 (Rough)Length: Mean Value (cm): 90 | For qualitative characteristic (surface) the search help is needed to select a value. For the quantitative characteristic (length) a number can be entered directly.The default number of inspected objects is calculated based on the sample size reviewed in an earlier step. The number of inspected objects can be manually changed. A number of nonconforming objects can be maintained directly in the respective fields as well for every inspection characteristic.With the app Record Results – Hierarchical View, a user can exceptionally overrule the automatic evaluation, for example, to document that the tolerance is always at the upper limit, then the generic defect ‘tolerance issue’ will be used. |  |
| 7 | Save Inspection Lot | Choose Save. | The inspection lot is saved. QM inspection for procurement goods has been performed and result recorded. |  |

###### Record Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the assembly depending on the inspection result. If you do not want to use the Quality Engineer Overview, you can open the Record Usage Decisions app directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a QUALITY_ENGINEER .Note To configure the user QUALITY_ENGINEER contact your Administrator. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Record Usage Decision (QA11). | The Record Usage Decisions: Initial Screen is displayed. |  |
| 3 | Enter Inspection Lot | Choose Inspection Lot on top right. | The Inspection Lot screen is displayed. |  |
| 4 | Enter Inspection Lot Quantities | Under the new tab which opens, enter the quantity into each of the sections. | The Inspection Lot quantities are entered. |  |
| 5 | Enter Usage Decision | Under the Characteristics, enter the usage decision from the following options:UD code: A1 (Accepted - unrestricted stock)A2 (Accepted -unrestricted - minor quality)A3 (Accepted -unrestricted - sample consumption)Negative ResultUD code: R1 (Rejected - blocked stock)R210 (Rejected - return supplier w/o delivery)R220 (Rejected - return supplier with delivery)Choose Yes if dialog Confirmation Prompt appears. | Usage decision is entered.If UD code is A1, quantity is posted to the Unrestricted stock at baseIf UD code is R1, quantity is posted to Blocked stock. |  |
| 8 | Save Usage Decision | Choose Save. | Stock moves to unrestricted or blocked stock from quality stock based on usage decision. |  |

##### Create and Confirm Warehouse Tasks for Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can pick goods from the base location and issue it to the vendor.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Create Technical Object enters company code 1710, while the sample data table lists company code 3310 for the plants used in the test.

> [!warning] Conflict
> Flagged while digesting this document, not verified: The Overview Table assigns Post Goods Receipt at Remote plant to Warehouse Clerk (EWM) with app F0843 and Post Goods Issue from Base plant to MIGO_GI, whereas the procedures use Receiving Specialist (IOG) with Process Receipts (F5316) and Warehouse Clerk (EWM) with Manage Outbound Delivery Orders (F6498).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Single Plant Setup intro says the SP14 sequence runs from Convert Purchase Requisition to Purchase Order through Record Inspection Results, while section Direct Purchase for Single Plant says it runs through Post Goods Issue for Maintenance Order.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/test-script-field-logistics-planning-and-execution-40g-ae-sap-s-4hana-part-02]]
- related-to :: [[14-maintenance-service-and-projects/test-script-field-logistics-planning-and-execution-supplier-items-4ah]]
- related-to :: [[14-maintenance-service-and-projects/test-script-sap-s-4hana-cloud-public-edition-field-logistics-planning]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/40G_S4CLD2608_BPD_EN_AE.docx` — lines 1–2554 of the extracted text · extracted with `mammoth` · 255,822 chars in the whole document
