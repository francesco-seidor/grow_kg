---
id: 14-maintenance-service-and-projects/test-script-sap-s-4hana-cloud-public-edition-engineer-products-and-sys
title: Test Script SAP S/4HANA Cloud Public Edition - Engineer Products and Systems – Project with Production (6GD_AE) (6GD_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud 2608 (AE) test script for scope item 6GD: Engineer-to-Order project with production, from quotation through production, billing, revenue recognition and project close."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/engineer-to-order-project-with-production]
aliases: [6GD_S4CLD2608_BPD_EN_AE]
keywords: [Engineer-to-Order Project with Production, engineer-to-order, project with revenue, wbs elements, business roles, master data, sales quotation, sales order, down payment, preliminary procurement]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6GD_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1167
topic: 14-maintenance-service-and-projects/engineer-to-order-project-with-production
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Engineer Products and Systems – Project with Production (6GD_AE) (6GD_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6GD_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Engineer-to-Order Project with Production** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Engineer Products and Systems – Project with Production (6GD_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232858375)

[2 Prerequisites 5](#_Toc232858376)

[2.1 System Access 5](#_Toc232858377)

[2.2 Roles 5](#_Toc232858378)

[2.3 Master Data, Organizational Data, and Other Data 7](#_Toc232858379)

[2.4 Additional Manual Configuration 13](#_Toc232858380)

[2.5 Business Conditions 13](#_Toc232858381)

[2.6 Preliminary Steps 14](#_Toc232858382)

[2.6.1 Maintain Financial Statement Versions 14](#_Toc232858383)

[2.6.2 Create Project Coding Mask (Optional) 17](#_Toc232858384)

[2.6.3 Create Project Types for WBS Elements (Optional) 19](#_Toc232858385)

[2.6.4 Maintain Budget Availability Profile (Optional) 21](#_Toc232858386)

[2.6.5 Manage Teams and Responsibility for Projects (Optional) 25](#_Toc232858387)

[2.6.6 Manage Situation Types (Optional) 26](#_Toc232858388)

[2.6.7 Check Flexible Workflow for Purchase Order Approval 27](#_Toc232858389)

[2.6.8 Configure Flexible Workflow for Purchase Order 28](#_Toc232858390)

[2.6.9 Create Purchasing Info Record - Components 29](#_Toc232858391)

[2.6.10 Create Initial Material Stock 31](#_Toc232858392)

[3 Overview Table 34](#_Toc232858393)

[4 Test Procedures 40](#_Toc232858394)

[4.1 Create and Send Sales Quotation to Customer 40](#_Toc232858395)

[4.2 Create Project 42](#_Toc232858396)

[4.3 Describe Project 48](#_Toc232858397)

[4.4 Upload Planned Costs and Revenues 49](#_Toc232858398)

[4.5 Change Sales Quotation 51](#_Toc232858399)

[4.6 Re-upload Planned Costs and Revenues 52](#_Toc232858400)

[4.7 Release Project 54](#_Toc232858401)

[4.8 Procurement Process for long lead Components 55](#_Toc232858402)

[4.8.1 Define Demand for Preliminary Procurement 55](#_Toc232858403)

[4.8.2 Material Requirements Planning 57](#_Toc232858404)

[4.8.3 Monitor Material Coverage 59](#_Toc232858405)

[4.8.4 Convert Purchase Requisitions to Purchase Orders 60](#_Toc232858406)

[4.8.5 Approve Purchase Order (Optional) 61](#_Toc232858407)

[4.8.6 Post Goods Receipt 62](#_Toc232858408)

[4.8.7 Create Supplier Invoice 63](#_Toc232858409)

[4.9 Create Sales Order 65](#_Toc232858410)

[4.9.1 Create Sales Order with Reference to Sales Quote and Assign WBS Element 65](#_Toc232858411)

[4.9.2 Check the Recognition Key on Project (Optional) 67](#_Toc232858412)

[4.9.3 Down Payment Process (Optional) 68](#_Toc232858413)

[4.9.3.1 Change Sales Orders (Remove Billing Block) (Optional) 68](#_Toc232858414)

[4.9.3.2 Create Down Payment Request (Optional) 69](#_Toc232858415)

[4.9.3.3 Post Down Payment (Optional) 71](#_Toc232858416)

[4.10 Material Requirements Planning for Sales Order 73](#_Toc232858417)

[4.11 Procurement Process for Raw Material 75](#_Toc232858418)

[4.11.1 Monitor Material Coverage 75](#_Toc232858419)

[4.11.2 Process Stock Transport Requisition 76](#_Toc232858420)

[4.11.3 Monitor Material Coverage 78](#_Toc232858421)

[4.11.4 Convert Purchase Requisitions to Purchase Orders 79](#_Toc232858422)

[4.11.5 Approve Purchase Order (Optional) 80](#_Toc232858423)

[4.11.6 Post Goods Receipt 81](#_Toc232858424)

[4.11.7 Create Supplier Invoice 82](#_Toc232858425)

[4.11.8 Post Goods Issue for Stock Transport Order 84](#_Toc232858426)

[4.11.9 Check Status of Stock Transfer with Overdue Materials - Stock in Transit (Optional) 85](#_Toc232858427)

[4.11.10 Post Goods Receipt for Stock Transport Order 86](#_Toc232858428)

[4.12 Subcontracting with Plant Stock Components 87](#_Toc232858429)

[4.12.1 Monitor Material Coverage 88](#_Toc232858430)

[4.12.2 Convert Purchase Requisition to Purchase Order 89](#_Toc232858431)

[4.12.3 Approve Purchase Order (Optional) 90](#_Toc232858432)

[4.12.4 Create Outbound Delivery 91](#_Toc232858433)

[4.12.5 Pick and Post Goods Issue 92](#_Toc232858434)

[4.12.6 Receive Goods from Subcontracting Purchase Order 93](#_Toc232858435)

[4.12.7 Create Supplier Invoice 94](#_Toc232858436)

[4.13 Production of Finished Goods 96](#_Toc232858437)

[4.13.1 Create Production Order for Finished Goods 96](#_Toc232858438)

[4.13.2 Material Staging for Final Assembly 97](#_Toc232858439)

[4.13.3 Release Production Orders 99](#_Toc232858440)

[4.13.4 Pick Components (Picking List) 100](#_Toc232858441)

[4.13.5 Confirm Assembly Activities 101](#_Toc232858442)

[4.13.6 Analyze Event-Based Work in Process (Optional) 103](#_Toc232858443)

[4.13.7 Post Goods Receipt for Production Order 103](#_Toc232858444)

[4.13.8 Analyze Event-Based Production Variances (Optional) 104](#_Toc232858445)

[4.13.9 Monitor Projects via Project Cost Report 105](#_Toc232858446)

[4.14 Bundle Spare Parts Through Production Order 106](#_Toc232858447)

[4.14.1 Create Production Order for Spare Parts Bundle 106](#_Toc232858448)

[4.14.2 Material Staging for Production Order 107](#_Toc232858449)

[4.14.3 Release Production Orders 108](#_Toc232858450)

[4.14.4 Confirm Assembly Activities 110](#_Toc232858451)

[4.14.5 Analyze Event-Based Work in Process (Optional) 111](#_Toc232858452)

[4.14.6 Post Goods Receipt for Production Order 112](#_Toc232858453)

[4.14.7 Analyze Event-Based Production Variances (Optional) 113](#_Toc232858454)

[4.15 Create Outbound Delivery 113](#_Toc232858455)

[4.16 Execute Picking 114](#_Toc232858456)

[4.17 Post Goods Issue 116](#_Toc232858457)

[4.18 Check Event Based Revenue Recognition – Project Accounted Sales 117](#_Toc232858458)

[4.19 Change Sales Orders (Remove Billing Block) 118](#_Toc232858459)

[4.20 Billing 119](#_Toc232858460)

[4.21 Clear Down Payment (Optional) 121](#_Toc232858461)

[4.22 Check Event Based Revenue Recognition – Project Accounted Sales (Optional) 123](#_Toc232858462)

[4.23 Accounts Receivable Overview 123](#_Toc232858463)

[4.24 Post Incoming Payments 124](#_Toc232858464)

[4.25 Time Recording 126](#_Toc232858465)

[4.25.1 Record Actual Working Time 127](#_Toc232858466)

[4.26 Complete Milestone 130](#_Toc232858467)

[4.27 Monitor Projects via Project Cost Report 131](#_Toc232858468)

[4.28 Check Event Based Revenue Recognition – Project Accounted Sales 132](#_Toc232858469)

[4.28.1 Monitor Revenue Recognition (Event-Based): Projects 133](#_Toc232858470)

[4.28.2 Run Revenue Recognition: Projects 134](#_Toc232858471)

[4.29 Close Project 135](#_Toc232858472)

## Purpose

Overview

This scope item provides an end-to-end solution process focusing on the Engineer-to-Order (ETO) scenario for manufacturers of highly customized products and systems.

The item settings in the sales order process connect the manufacturing process with project WBS elements. These subordinate WBS element costs aggregate to the Billing WBS in the Cost of Goods Sold calculation for the revenue. This solution also enables project revenue and various cost reporting.

On the logistical side, you can use the project user interface to create and maintain material requirements such as planning and long lead time early material (internal or external) procurement. You can also provide material requirements directly to the project using project production orders supported by project stock components manufactured by subcontract vendors.

The project cost report shows revenue and additional cost data that is directed towards the project but not yet posted, is also enabled.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role for the Administrator in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/8fa28e0107984d42a99b9eea67856cea.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Project Financial Controller | SAP_BR_PROJ_FIN_CONTROLLER | Project Control - Finance | SAP_BR_PROJ_FIN_CONTROLLER |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Employee | SAP_BR_EMPLOYEE | Self Services / Self Services / Employee Overview Space | SAP_BR_EMPLOYEE / SAP_CA_SPT_EMPLOYEE_CROSS_PC / SAP_EAM_SPT_EMPLOYEE_PC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |
| Project Manager | SAP_BR_PROJECTMANAGER | Project Management | SAP_BR_PROJECTMANAGER |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
|  |  |  |  |  |
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Cost Accountant - Sales | SAP_BR_SALES_ACCOUNTANT | Sales Accounting | SAP_BR_SALES_ACCOUNTANT |  |
| Accounts Receivable Manager | SAP_BR_AR_MANAGER | Accounts Receivable | SAP_BR_AR_MANAGER |  |
| Project Controller - Resourcing and Procurement | SAP_BR_PROJ_PROC_CONTROLLER | Project Control – Resourcing and Procurement | SAP_BR_PROJ_PROC_CONTROLLER |  |
| Cost Accountant - Inventory | SAP_BR_INVENTORY_ACCOUNTANT | Inventory Accounting | SAP_BR_INVENTORY_ACCOUNTANT |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Material Planner - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC | Material Planning - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC |  |

### Master Data, Organizational Data, and Other Data

Some of the organizational structure and master data of your company have already been created while others need to be created by yourself. The following chapter will describe what master data is required to execute the 6GD test procedure.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

|  |
| --- |
| Note In the following table(s), field values for sample data required to run the subsequent test procedures are listed. For all other fields, you can pick values according to your process needs. Details on creating additional master data are described in the Preliminary Steps section. |

|  |
| --- |
| RememberWhile creating the finished-good (FG) material for the Project Stock scenario using the Create Product Master of type "Finished Good" - MDS(BNT) master data script, maintain the following attribute for the material:Strategy Group: E2The Event-Based Production Cost Posting(3F0) master data script needs to be executed only for the Project Stock scenario. |

Material Master Data

The following Material Masters are used to successfully realize this ETO Scenario:

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Material | FG0611 | FINISHED GOOD 1,ETO-DI,PD,SERIAL NUM | Finished Product with Serial number on Project stock.MRP Planned and Produced internally with project related manufacturing.Sold to customer. |
| Material | FG0612 | FINISHED GOOD 2,ETO-DI,PD | Finished Product on Project stock. MRP Planned and produced internally.Sold to customer. |
| Material | SG0611 | SEMI FINISHED 1,PHANTOM | Phantom assembly group. |
| Material | SG0612 | SEMI FINISHED 2,ETO,PD,SUBCON | Semifinished Material on project stock. MRP Planned and pro-cured via subcontracting vendor. |
| Material | RM0611 | RAW MAT 1,PD | Externally Procured Material on normal stock. MRP Planned. |
| Material | RM0612 | RAW MAT 2,ETO,PD | Externally Procured Material on normal stock. MRP Planned. |
| Material | RM0613 | RAW MAT 3,PD | Externally Procured Material on normal stock. MRP Planned. |
| Material | RM0614 | RAW MAT 4,PD | Externally Procured Material on normal stock. MRP Planned. |
| Material | RM0615 | RAW MAT 5,ETO,PRELIMINARY PROCUREMENT,PD | Externally Procured Material with Serial numbers on project stock. Long lead item. MRP Planned. |
| Material | NS0611 | NON-STOCK GOOD FOR PROJECT BILLING | Material Type NLAG, ItemCategoryType SERV |

Organization Data

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Controlling Area | A000 | Controlling Area A000 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Plant | 3310 | Plant 1 AE |  |
| Cost center | 3310130133101302 | Manufacturing 1 (AE) |  |
| Costing Sheet | 3310PI | Costing Sheet-PS Projects |  |
| Activity Types | 8 | Consulting |  |
| G/L Account | 6100500061007000610030006100800010010000440020004100000041000400 | Trav. Expense - Ground transportationTrav. Expense - Airfare, Rail, MileageTravel Expenses - Hotel and AccommodationTravel Expenses - MiscellaneousPetty CashSales Discounts - DomesticRev Domestic ProdSales Revenue w/ Cost Element |  |
| Profit Center | YB600 | Shared Services |  |
| Functional Area | YB25 | Consulting/Services |  |

Project and Sales Order Structure

The following table represents the connection between project structure and sales order structure used throughout the 6GD test script.

| Project Name | Root WBS Element | Subordinate WBS elements on first level | Sales Order Item | Description |
| --- | --- | --- | --- | --- |
| Project ID (Example: R.000001) |  |  |  | Project Definition |
|  | WBS1 ID (Example: R.000001) |  | Item 0010 (Material NS0611) | Root WBS element as billing element (cost aggregator) assigned to Item 0010 |
|  |  | WBS2 ID (Example: R.0000011) | Item 0020 (Material FG0611) | Subordinate WBS element as non-billing WBS element (Finish Goods) assigned to Item 0020 |
|  |  | WBS3 ID (Example: R.0000012) | Item 0030 (Material FG0612) | Subordinate WBS element as non-billing WBS element (Spare Parts Bundle) assigned to Item 0030 |
|  |  | WBS4 ID (Example: R.0000013) |  | Subordinate WBS element a non-billing WBS element (time recording) |

Bill of Material Structure

BOM structure mentioned below must be created and made available as part of this new scope item. The BOM consists of the below referenced structure and can be created by referring to the Preliminary Section – Create Bill of Material (BOM).

| Material | Level | Material Type | Unit | Characteristics of Material | Component Quantity | Component UOM |
| --- | --- | --- | --- | --- | --- | --- |
| FG0611 | 0 | FERT | PC | Internally produced. | 1 | PC |
| SG0611 | 1 | HALB | PC | Phantom assembly group. | 1 | PC |
| RM0611 | 2 | ROH | PC | External procured. | 1 | PC |
| RM0612 | 2 | ROH | PC | External procured. | 1 | PC |
| RM0615 | 1 | ROH | PC | External procured as long lead item via planned independent requirement. | 1 | PC |
| SG0612 | 1 | HALB | PC | External procured with subcontracting process. | 1 | PC |
| RM0613 | 2 | ROH | PC | External procured. Normal stock consigned to subcon-tract vendor. | 1 | PC |
| RM0614 | 2 | ROH | PC | External procured. Normal stock consigned to subcon-tract vendor. | 1 | PC |
| FG0612 | 0 | FERT | PC | Internally produced. | 1 | PC |
| RM0611 | 1 | ROH | PC | External procured. | 1 | PC |
| RM0613 | 1 | ROH | PC | External procured. | 1 | PC |

Work Center

Below table mentions the work centers to be used in thisn't E2E ETO scenario. These are standard work centers available as part of best practice and hence it is needed to create new Work Centers.

| Work Center | Plant | Work Center Category | Work Center Description |
| --- | --- | --- | --- |
| ASSEMBLY | 3310 | 0001 | Assembly |
| TESTING | 3310 | 0001 | Testing |
| PACK01 | 3310 | 0001 | Packing Line 1 |

Routing:

Routing (Master Data Script BNL) required for the finished products FG0611 and FG0612 using control key YBP1 for this scenario. Routings for semifinished goods are not needed. Refer to the section Create Bill of Material (BOM) for more details.

Production Version:

Production version (Master Data Script BLD) for the finished products FG0611 and FG0612 and semifinished products SG0611 and SG0612 are required for this scenario. Refer to the section Create Bill of Material (BOM) for more details.

Suppliers:

Supplier masters (Business Partner) provided as part of standard best practices will be used. No need to create new supplier masters for this E2E scenario. Below mentioned Suppliers (Business Partners) will be used in this scenario.

| Master Data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Supplier | 33300001 | Domestic UAE Supplier 1 | Note If you want to send form print outs via email instead of using the print functionality make sure that you have maintained a valid email ad-dress in the vendor master data. |
| Supplier | 33300007 | Domestic AE Subcontractor A | Note If you want to send form print outs via email instead of using the print functionality make sure that you have maintained a valid email ad-dress in the vendor master data. |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchase group | 001 | Group 001 |  |
| Shipping point | 3310 | Shipping Point 3310 |  |

Customer:

Customer masters (Business Partners) provided as part of standard best practices will be used. No need to create new supplier masters for this E2E scenario. Below mentioned Customers (Business Partners) will be used in this scenario.

| Master Data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Sold-to Party | 33100004 | Domestic UAE Customer 4 |  |
| Ship-to Party | 33100004 | Domestic UAE Customer 4 |  |
| Payer | 33100004 | Customer domestic 04 |  |
| Sales Organization | 3310 |  |  |
| Distribution Channel | 10 |  |  |
| Division | 00 |  |  |
| Company Code | 3310 |  |  |

Purchasing Info Record:

A new purchasing info record to be created for the supplier 33300001 for Raw Material RM0612, RM0615 and also for the supplier33300007 for the subcontracting material SG0612. For RM0612 in plant 3320, for RM0615 and SG0612 in plant 3310 and all with 3310 purchasing organization.

For more information on creating your own master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNG | Create G/L Account and Cost Element - MDS |
| BNH | Create Profit Center - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| 3F0 | Event-Based Production Cost Posting |
| BLD | Create Production Version - MDS |
| BNQ | Create Quality Inspection Plan - MDS |
| BNE | Create Supplier Master - MDS |
| BHD | Create Purchasing Info Record - MDS |
| BND | Create Customer Master - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/c39de0cfb9d5ed4407f0ad6fdb2efa54)

### Business Conditions

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Business Condition |
| --- | --- |
| BKJ - Sales Order Processing with Customer Down Payment | To execute the sales order related activities for the project, the scope item must be activated. |
| BDA - Free of Charge Delivery | To execute the sales order for free goods related activities for the project, the scope item must be activated. |
| J59 - Accounts Receivable | To manage the open receivable invoices that are automatically created from the sales processes for the project, the scope item must be activated. |
| 4GQ - Event-Based Revenue Recognition – Project-Based Sales | To execute the Revenue Recognition for Project based sales, the 4GQ - Event-Based Revenue Recognition – Project-Based Salesscope item must be activated. |
| 31Q - Sales Order Processing for Sales Kits | To execute the event based revenue recognition for project based sales, the 31Q - Sales Order Processing for Sales Kitsscope item must be activated. |
| 4I9 - Project Control – Sales | To execute the event based revenue recognition for project based sales, the 4I9scope item must be activated. |
| 4RF - Project Control – Resourcing and Procurement | To execute the project related procurement, scope item 4RFmust be activated. |
| 3F0 - Event-Based Production Cost Posting | To trigger journal entries for work in process, overhead and production variances with the underlying events (goods movements and order confirmations). |

### Preliminary Steps

#### Maintain Financial Statement Versions

Purpose

In this activity, you maintain the financial statement (FS) version. This activity must be carried out only if you choose to add additional G/L accounts.

|  |
| --- |
| Note Please make sure the Set-up Instructions have been completed before continuing. |

|  |
| --- |
| Note You can access and use Manage Financial Statement Versions (OB58) as a General Ledger Accountant to display financial statement version data. However, changes can only be made and saved using the procedure below. |

|  |
| --- |
| Caution This test step is relevant only if the new Q2P maintenance mode for G/L accounts is switched on. In case you are not on new Q2P for G/Ls, you need to use the Manage Financial Statement Versions (OB58) app. |

It is important that all G/L accounts used for revenue/deductions in a project/product profitability must be included and mapped to the Financial Statement Version YPS2 and tagged to a single respective semantic tag. Note that if you are just adding GL to an existing predelivered node, tags are already mapped. This is essential as many functionalities in project reporting and budgeting use these values to report all costs booked.

There are two factors to consider:

1. Assign all the G/Ls relevant for cost booking under any existing node/item under Cost of Goods Sold. All the predelivered existing items are already mapped.

2. Create a new node/item under Cost of Goods Sold. All nodes/items must be mapped to semantic tag ACT_COST and an individual tag. For example, material cost is mapped to overall cost tag ACT_COST and individual tag MATCST.

|  |
| --- |
| Note This step is only required if you add a new node/item under Cost of Goods Sold. If you are using project budgeting, the budget controls are via semantic tags. In the budget, you can either map ACT_COST tag or any other child level tag as long as it is a part of overall ACT_COST and assigned to FSV YPS2. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: General Ledger

1. For the row with Item Name of Chart of Accounts, choose Details (>).
2. For the Define Financial Statement Versions row, choose Configure.

|  |
| --- |
| Note If you cannot find the configuration activity, the Q2P maintenance mode for FSVs is not active for your system. Complete the changes with the Manage Financial Statement Versions (OB58) app (part of General Ledger Accountant). |

1. Continue with the procedure in the table below.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Define Financial Statement Versions activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select Financial Statement Version | Select the following financial statement version and choose the Financial Statement Items button.FS Version: YPS2 | The Change Financial Statement Version view displays. |  |
| 2 | New Node | Drill at the top nodes until you find the Cost of Goods Sold node. To add your new node, choose the Create Items button. |  |  |
| 3 | Save | Choose Save. |  |  |

Add Semantic Tags to Newly Created Node

Purpose

In this activity, you assign semantic tags to the newly created node.

Prerequisites

Before you do this step, you need to know the item number for the newly created item. To find this item number:

- Open the Manage Financial Statement Versions (OB58) app as a General Ledger Accountant.
- In the Change View "Financial Statement Versions": Overview view, select the YPS2 financial statement version and choose the Financial Statement Items button.
- Choose Menu > Settings > Change, in the Change Settings dialog box, select Item keys visible and choose the Continue button. Note the number of the new items created.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. Choose Configure Your Solution.
4. Make the following entries:

Application Area: Finance

Sub Application Area: General Ledger

1. For the row with Item Name of Chart of Accountss, choose Details (>).
2. For the Assign Semantic Tags to Financial Statement Versions row, choose Configure.

|  |
| --- |
| Note If you cannot find the SSCUI, the Q2P maintenance mode for FSVs is not active for your system. Complete the changes with Assign Semantic Tags to Financial Statement Versions (FINSC_FAGL2SEMTA) app (part of General Ledger Accountant). |

1. Continue with the procedure in the table below.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app.
3. Search for the Assign Semantic Tags to Financial Statement Versions activity and choose Go to Activity.
4. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose the New Entries button. | The New Entry dialog box displays. |  |
| 2 | New Entry Type | Select Assign Semantic Tag to FS Item and choose Continue. | The New Entries: Details of Added Entries view displays. |  |
| 3 | Enter Data | Make the following entries and choose Save:FS Version: YPS2FS Items: <The new item you created as part of the Prerequisites section in this step>Semantic Tag: ACT_COSTRepeat the step with individual tag. Select the tag from existing available tags. |  |  |

#### Create Project Coding Mask (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create the coding mask for the project structure. The coding mask applies to the external identification of project definitions as well as WBS elements.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori Launchpad as aConfiguration Expert - Business Process Configuration |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Navigate to configuration activity | Choose the link Configure Your Solution.Make the following entries:Application Area: Enterprise Portfolio & Project ManagementSub Application Area: Project Financials ControlClick the line item displayed in the Configuration Items sectionSelect Define Project Coding Mask and choose Configure | The Change View "Project Number Editing': Overview screen is displayed. |  |
| 4 | Create a Coding Mask Entry | Perform the following actions to create the coding mask:Choose New EntriesEnter the following details:PrjID: ACoding mask: /XXXXXX-00Description: Test Coding Mask for Key ALock: <Select/Deselect>Choose Save.This step is optional.Once the coding mask is created, deletion is not possible.You cannot create commercial or internal projects in the project services processes, namely:Customer Project Management (J11)Internal Project Management (1A8)that begins with any coding key defined for coding masks. | Project Coding Mask will be saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Navigate to configuration activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Create a Project Coding Mask.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Project Number Editing": Overview screen is displayed. |  |
| 3 | Create a Coding Mask Entry | Perform the following actions to create the coding mask:Choose New EntriesEnter the following details:PrjID: ACoding mask: /XXXXXX-00Description: Test Coding Mask for Key ALck: <Select/Deselect>Choose Save.This step is optional.Once the coding mask is created, deletion is not possible.You cannot create commercial or internal projects in the project services processes, namely:Customer Project Management (J11)Internal Project Management (1A8)that begins with any coding key defined for coding masks. | Project Coding Mask will be saved. |  |

#### Create Project Types for WBS Elements (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Project Type is generally used to group or classify projects, it is primarily used for the reporting.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori Launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Navigate to configuration activity | Choose the link Configure your solution.Make the following entriesApplication Area: Enterprise Portfolio & Project ManagementSub Application Area: Project Financials ControlClick on the line item displayed in the worklist sectionSelect Create Project Types for WBS Elements and choose Configure | The Create Project Types for WBS Elements app is displayed. |  |
| 4 | Create a Project Type | Perform the following actions to create the project type:Choose New EntriesEnter the details as mentioned in the following example :Typ: RDDescription: RD ProjectsChoose Save. | Project Type is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Navigate to configuration activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Create Project Types for WBS Eleements.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Create Project Types for WBS Elements screen is displayed. |  |
| 3 | Create a Project Type | Perform the following actions to create the project type:Choose New EntriesEnter the details as mentioned in the following example :Typ: RDDescription: RD ProjectsChoose Save. | Project Type is saved. |  |

#### Maintain Budget Availability Profile (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Maintain Budget Availability Profile app is used to create the Budget Availability control profile.

Prerequisites

If you intend to use Project Budget, make sure that you activate the non-standard scope item Commitment Management (2I3) which is a prerequisite for budgeting. Once activated, commitment management ledger 0E is active and applicable for all company codes and countries/regions. These commitments are updated in Extension Ledger 0E (predelivered) in ACDOCA table. Commitments are reduced by various business transactions such as goods receipt. The default content for Project Budgeting utilizes profiles PS001 and you can either update this profile or create your own profile via configuration activity Maintain Budget Availability Control Profile for Projects.

Ensure that you perform the Preliminary Steps of this document to update the following:

- Maintain Financial statement YPS2
- Tag ACT_COST which is mandatory for G/Ls relevant for Budget check. Note that currently Commitment/Budget do not work for Purchase order without material.
- Maintain Financial Statement Versions (FSV)
- Assign Semantic Tags for FSV
- Set Report Relevancy
- Replicate Runtime Hierarchy. Make sure G/Ls relevant for Budget are part of this structure.

To view commitments in the report, an open purchase order and/or requisition must exist. For details on creating purchase orders, refer to Consumable Purchasing (BNX).

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori Launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Navigate to configuration activity | Choose the link Configure your solution.Make the following entries:Application Area: FinanceSub Application Area: Overhead Cost ManagementClick on the line item Budget Management displayed in the list.Select Maintain Budget Availability Control Profile for Projects and choose Configure. | The Maintain Budget Availability Profile app is displayed. |  |
| 4 | Create an Availability Control Profile Entry | Perform the following actions to create the availability control profile:Choose New EntriesEnter the details as shown in the following example:Profile: ZS001Availy Ctrl Type: Project SystemBudget Availy Ctrl: Profile Name : Default Bdgt Availability prflTime Range: Annual Budget / Overall BudgetBudget Currency: Global Currency/Project CurrencyPress Enter.Overall Budget needs to be selected if you want to perform the budget check across Fiscal years whereas Annual Budget needs to be selected if you want to perform the check per Fiscal year.Gobal Currency needs to be selected if you want to calculate the financials at controlling area level whereas Project Currency needs to be selected if you want to check financials at project level.For this newly created Availability Control Profile, maintain the Semantic Tags and Tolerance Limits.Select the AVC profile and choose Semantic Tags and maintain entries as shown in the following example:Choose New EntriesSem. Tag: ACT_COSTSemantic Tag Name: Actual Cost% of Budget used Before First Notification: 80%% Increment for Further Notifications: 5%Press Enter.Select the Semantic tag and choose Tolerance Limits and maintain entries as shown in the following example:Choose New EntriesActy Grp: All Activity GroupsMsgType: Warning/Error%: 90.00Press Enter.Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Navigate to configuration activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain Budget Availability Control Profile for Projects.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Maintain Budget Availability Profile screen is displayed. |  |
| 3 | Create an Availability Control Profile Entry | Perform the following actions to create the availability control profile:Choose New EntriesEnter the details as shown in the following example:Profile: ZS001Availy Ctrl Type: Project SystemBudget Availy Ctrl: Profile Name : Default Bdgt Availability prflTime Range: Annual Budget / Overall BudgetBudget Currency: Global Currency/Project CurrencyPress Enter.Overall Budget needs to be selected if you want to perform the budget check across Fiscal years whereas Annual Budget needs to be selected if you want to perform the check per Fiscal year.Gobal Currency needs to be selected if you want to calculate the financials at controlling area level whereas Project Currency needs to be selected if you want to check financials at project level.For this newly created Availability Control Profile, maintain the Semantic Tags and Tolerance Limits.Select the AVC profile and choose Semantic Tags and maintain entries as shown in the following example:Choose New EntriesSem. Tag: ACT_COSTSemantic Tag Name: Actual Cost% of Budget used Before First Notification: 80%% Increment for Further Notifications: 5%Press Enter.Select the Semantic tag and choose Tolerance Limits and maintain entries as shown in the following example:Choose New EntriesActy Grp: All Activity GroupsMsgType: Warning/Error%: 90.00Press Enter.Choose Save. |  |  |

|  |
| --- |
| Note In a real business scenario, projects sometimes run overbudget. With the automatic loss handling feature, event-based revenue recognition calculates the amount needed for loss provision and the necessary adjustments to the loss provision automatically with period-end closing. Refer to Maintain Settings for Event-Based Revenue Recognition under Preliminary Steps in the scope item 4GQ - Event-Based Revenue Recognition – Project-Based Sales. |

#### Manage Teams and Responsibility for Projects (Optional)

Purpose

In this procedure, you configure teams and responsibility for projects.

Note For details on the process of setting up teams and responsibility determination, see the Setting Up Responsibility Determination (1NJ) guide.

You can also define your own responsibility management (functions, teams, and responsibilities) by making use of the following SSCUIs:

- Map Function Profiles to Standard Team Category
- Classify Functions for Standard Team Category
- Map Custom Responsibility Definitions to Standard Team Category
- Define Team Types

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access the App | Open Manage Teams and Responsibilities (F2412) .Choose Create. | The New Team screen is displyed. |  |
| 3 | Maintain the Team details | Make the following entries:On the Team Information tab:Name: Team_EPPM Description: Team of EPPMStatus:EnabledType: SEPPM_PFCOn the Team Members tab:Choose Create, and maintain the following values:Business Partner: use the search function to find the business partner of Project Financial ControllerFunctions: Project Financial Controller |  |  |
| 4 | Create the Team | Choose Create. | The team is created. |  |

#### Manage Situation Types (Optional)

Purpose

In this procedure, you configure the situation type by using template.

Note For details on situations and the process to set up situation types, see the Setting Up Situation Handling (31N) guide.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Business Process Specialist - Business Process Configuration |  |  |
| 2 | Open Manage Situation Types | Open Manage Situation Types (F2947) app. | The Manage Situation Types screen is displayed. |  |
| 3 | Select the Template to Copy | In the Standard section, enter the ID EPPM_PROJBUDGETTHRESHOLDEXCEEDED and choose Go.Select the latest version of EPPM_PROJBUDGETTHRESHOLDEXCEEDED, then choose Copy. | The Situation Type screen is displayed. |  |
| 4 | Maintain the Situation | Make the following entries and choose Save:Admin InformationID: Z_BUDGET THRESHOLDName: Budget Consumption SituationSituation DisplayShort Description:Details:Notification:Resend Notifications: YESConditionsMaintain the values against the corresponding attributes/ filters to configure the conditions and use this function.Notification RecipientsResponsibility by teams: Choose + and maintain the team created through the 'Manage Teams and Responsibilities' app and maintain the value Project Financial Controller in the field Member Functions if necessary.Responsibility Rules: Choose + and maintain the project related users mapped/linked to the projects in the 'Project Brief' app for the roles of Project Financial Controller and Project Manager. | The situation type is maintained |  |
| 5 | Enable The Situation Type | Choose Enable, it will change from NO to YES. |  |  |

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

#### Create Purchasing Info Record - Components

|  |
| --- |
| Note If the Info Records for the material combination of materials:RM0612 , RM0615 and supplier: 33300001, and material: SG0612 and supplier: 33300007 already exist in the system, you can skip this step. |

Complete the following procedure to create records for all of your components.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Manage Purchasing Info Records (F1982) . | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create Purchasing Info Records. | The Purchasing Info Record Screen is displayed. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Organization: 3310Purchasing Info Record Category: StandardSupplier: 33300001Material: RM0612Plant: 3320Purchasing Group: 001 | Header data is added. |  |
| 5 | Enter General Information | In the General Information section, make the following entries:Available From:TodayAvailable To:12/31/9999 | General Information is added. |  |
| 6 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: 2Under Delivery Tolerance in %: 0Over Delivery Tolerance in %: 0Tax Code: <Input Tax Code>Confirmation Control: <blank>Order Unit: PCStandard Order Quantity: 1Goods-Receipt-Based Invoice Verification: selectNo Evaluated Receipt Settlement: selectNote When the Time Dependent Tax (TDT) is activated via the Define Tax Codes for Sales and Purchases activity for Country of company code and Tax Code is given, the Tax Rate Valid From field is mandatory. You can enter current date, which will be adjusted to validity start date of tax code according to the setting in the activity.When the RITA (Registration for Indirect Taxation Abroad) is activated, tax registration country is maintained for company code in Activate RITA and Maintain Tax Registration Countries and tax code is given, the Tax Country field is mandatory, in which the country ID of company code is given as a default value, but you can change to the valid country ID that is maintained in the activity accordingly.Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or via the configuration activity in the Realize phase in the project experience of SAP Central Business Configuration.Time Dependent Tax (TDT) and RITA (Registration for Indirect Taxation Abroad) does not apply to Brazil. | Delivery and Quantity Data is added. |  |
| 7 | Enter Condition Data | In the Condition section, choose Create and click on Navigation to get details screen.In the General Information area, make the following entries:Valid From: TodayValid To: 12/31/9999Amount: 120Pricing Unit: 1Unit of Measure: PCCurrency: AEDChoose Apply. | Condition Data is added |  |
| 8 | Save your data | Choose Create. | The purchasing info record is saved. |  |

|  |
| --- |
| Note Repeat the above steps to create the info record for material RM0615 in plant 3310, with a price of 12500 EUR and supplier 33300001.Repeat the above steps to create the info record for material SG0612 in plant 3310, with a subcon service price of 250 EUR and supplier 33300007. Use ME11 and ensure Purchasing Info Record Category: Subcontracting and Production Version: 0001 while creating info record for SG0612. |

#### Create Initial Material Stock

|  |
| --- |
| Note In the following table(s), field values for sample data required to run the subsequent test procedures are listed. For all other fields, you can pick values according to your process needs.Also, if your system has been used in the past, price of the stock uploaded will not be exactly the same as the uploaded price since there could be existing movements with a difference price. |

Purpose

In a real business scenario, initial material stock are usually purchased from external suppliers through standard purchasing or subcontracting processes. For only testing purpose, this process step shows you how to create and post the initial material stock to storage locations directly.

Prerequisite

Before creating initial material stocks, we recommend that you check stock level for RM0611,RM0613 and RM0614. To do that, log onto the SAP Fiori launchpad as a Production Planner, and open Manage Material Coverage - New Version (F0251A) app. Remove some stock if there is already sufficient amount of stock in store. Otherwise, no planned orders can be generated later. You can either post initial stock directly to the storage locations, or refer to test scripts from Procurement of Direct Materials (J45) or Scheduling Agreements in Procurement (BMR) test scriptsfor purchasing processes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Post Goods Movement (MIGO) screen displays |  |
| 3 | Choose Document Type | Select Goods Receipt and Other. | The Goods Receipt Other - Example WarehouseClerk screen displays. |  |
| 4 | Enter Data | In the Detail Data section, make the following entries and press Enter.On the Where tab:Movement Type: 561Plant: 3310Storage Location: 331COn the Quantity tab:Quantity:<100 PC>Ext. Amount LC:RM0611: 200000RM0613: 75000RM0614: 125000On the Material tab:Material:RM0611,RM0613,RM0614 , refer to section Master Data, Organizational Data, and Other Data for Bill of Material Structure.Choose Next Item and select Item OK to add entries. |  |  |
| 5 | Check | Choose Check. | The document is ready to be posted. |  |
| 6 | Post | Choose Post. | Material document XXX is posted and materials are available in stock. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the home page will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the home page using the search bar.

If you want to personalize the home page and include the hidden apps, navigate to your user profile and choose Settings > App Finder.

| Process Step | Business Role | Transaction/App | Expected Output |
| --- | --- | --- | --- |
| [Create and Send Sales Quotation to Customer](#unique_19) [page ] 40 | Internal Sales Representative | Manage Sales Quotations (F1852) |  |
| [Create Project](#unique_20) | Project Financial Controller | Project Control - Enterprise Projects (F3215) | Project definition and WBS Elements with all the required parameters will be created. |
| [Describe Project](#unique_21) | Project Manager - Commercial Services | My Projects - Project Manager (F1876) | Project details and team members are added. |
| [Upload Planned Costs and Revenues](#unique_22) | Project Financial Controller | Import Financial Plan Data (F1711) | Planned costs for the project WBS Element are posted. |
| [Change Sales Quotation](#unique_23) [page ] 51 | Internal Sales Representative | Manage Sales Quotations (F1852) |  |
| [Re-upload Planned Costs and Revenues](#unique_24) [page ] 52 | Internal Sales Representative | Import Financial Plan Data (F1711) |  |
| [Release Project](#unique_25) | Project Financial Controller | Project Control - Enterprise Projects (F3215) | The project status is changed to REL (Release). |
| Procurement Process for long lead Components |  |  |  |
| [Preliminary Procurement](#unique_26) | Project Controller - Resourcing and Procurement | Manage Project Demand (F4562) | Independet material requirement for the long lead item will be created. |
| [Material Requirements Planning](#unique_27) | Production Planner | Schedule MRP Runs (F1339) | Material is planned for the long lead component |
| [Monitor Material Coverage](#unique_28) | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Purchase Requistions are generated. |
| [Convert Purchase Requisition to Purchase Order](#unique_29) | Purchaser | Process Purchase Requisitions - Deprecated (F1048) | Purchase Orders are created. |
| [Approve Purchase Order (Optional)](#unique_30) | Purchasing Manager | My Inbox - All Items (F5331) | Purchase Order is approved. |
| [Post Goods Receipt](#unique_31) | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Goods Receipt is posted. |
| [Create Supplier Invoice](#unique_32) | Accounts Payable Accountant | Create Supplier Invoice (F0859) | Supplier Invoice is created for the Raw Material. |
| Create Sales Order |  |  |  |
| [Create Sales Order with Reference to Sales Quote and Assign WBS Element](#unique_33) [page ] 65 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales Order is created with Project Stock and assigned to non-billing and billing WBS Element. |
| [Check the Recognition Key on Project (Optional)](#unique_34) | Project Financial Controller | Project Control - Enterprise Projects (F3215) | Verify Revenue Recognition Key is updated on the Project. |
| Down Payment Proces (Optional) |  |  |  |
| [Change Sales Orders (Remove Billing Block) (Optional)](#unique_35) | Internal Sales Representative | Manage Sales Orders (F1873) | Billing if blocked is removed. |
| [Create Down Payment Request (Optional)](#unique_36) | Billing Clerk | Create Billing Documents (F0798) | Down payment request is generated. |
| [Post Down Payment (Optional)](#unique_37) | Accounts Payable Accountant | Post Incoming Payments (F1345) | Down Payment is posted |
| [Material Requirements Planning for Sales Order](#unique_38) | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Material is planned for the Items in the sales order |
| Procurement Process for Raw Material |  |  |  |
| [Monitor Material Coverage](#unique_39) [page ] 75 | Material Planner - External Procurement | Monitor Material Coverage - Net / Individual Segments (F2101A) | Purchase Requistions are generated for the RM. |
| [Process Stock Transport Requisition](#unique_40) [page ] 76 | Purchaser | Process Purchase Requisitions - Deprecated (F1048) | Purchase Order is created for the Raw Material. |
| [Monitor Material Coverage](#unique_41) | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Purchase Requistions are generated for the RM. |
| [Convert Purchase Requisition to Purchase Order](#unique_18) | Purchaser | Process Purchase Requisitions - Deprecated (F1048) | Purchase Order is created for the Raw Material |
| [Approve Purchase Order (Optional)](#unique_42) | Purchasing Manager | My Inbox - All Items (F5331) | Purchase Order is approved if it have an approval workflow defined |
| [Post Goods receipt](#unique_43) | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Goods Receipt is posted for the Raw Material |
| [Create Supplier Invoice](#unique_32) | Accounts Payable Accountant | Create Supplier Invoice (F0859) | Supplier Invoice is created for the Raw Material. |
| [Post Goods Issue for Stock Transport Order](#unique_44) [page ] 84 | Warehouse Clerk | Post Goods Movement (MIGO) | Goods Issue is posted for Raw Material leaving supplying plant for sourcing plant. |
| [Check Status of Stock Transfer with Overdue Materials - Stock in Transit (Optional)](#unique_45) [page ] 85 | Warehouse Clerk | Stock - Single Material (F1076) | Checking the stock in transit. |
| [Post Goods Receipt for Stock Transport Order](#unique_46) [page ] 86 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Goods Receipt is posted for the Raw Material to receiving plant. |
| Subcontracting with Plant Stock Components |  |  |  |
| [Monitor Material Coverage](#unique_47) | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Purchase Requistions are generated for the Material which needs procurement via Subcontracting |
| [Convert Purchase Requisition to Purchase Order](#unique_48) | Purchaser | Process Purchase Requisitions - Deprecated (F1048) | Purchase Order is created for the subcontracting material. |
| [Approve Purchase Order (Optional)](#unique_30) | Purchasing Manager | My Inbox - All Items (F5331) | Purchase Order is approved. |
| [Create Outbound Delivery](#unique_49) | Inventory Manager | Subcontracting Cockpit (F2948) | Outbound Delivery is created |
| [Pick and Post Goods Issue](#unique_50) | Shipping Specialist | Change Outbound Delivery (VL02N) | Goods Issue is posted for the Subcontracting material |
| [Receive Goods from Subcontracting Purchase Order](#unique_51) | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Semifinished good is received by subcontracting PO. |
| [Create Supplier Invoice](#unique_52) | Accounts Payable Accountant - Procurement | Create Supplier Invoice (F0859) | Supplier Invoice is created for the subcontracting material. |
| Production of Finished Good |  |  |  |
| [Create Production Order for Finished Good](#unique_53) | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Production Order for the finished goods is available |
| [Material Staging for Final Assembly](#unique_54) | Production Operator - Discrete Manufacturing | Stage Materials for Production (MF60) | Material is staged for final assembly. |
| [Release Production Order](#unique_55) | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | Production Order is released. |
| [Pick Components (Picking List)](#unique_56) | Production Operator - Discrete Manufacturing | Pick Components for Production Orders (CO27) | Components required for assembly are picked and posted. |
| [Confirm Assembly Activities](#unique_57) | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | Assembly is confirmed. |
| [Event-Based Work in Process (Optional)](#unique_58) | Cost Accountant - Production | Work in Process - Event-Based (F3498) | Review event-based WIP and variance |
| [Post Goods Receipt for Production Order](#unique_59) | Warehouse Clerk | Post Goods Receipt for Production Order (F3110) | Goods receipt for production order is posted. |
| [Analyze Event-Based Production Variances (Optional)](#unique_60) | Cost Accountant - Production | Order Cost Details - Event-Based (F4254) | Analyze event-based orders |
| [Monitor Projects via Project Cost Report](#unique_61) | Project Financial Controller | Project Cost Report - Plan/Actual (F2513) | All plan, actual costs, and their variances can be analyzed |
| [Monitor Projects via Project Cost Report](#unique_61) | Project Financial Controller | Project Cost Report - Plan/Actual (F2513) | All plan, actual costs, and their variances can be analyzed |
| Bundle Spare Part via Production Order |  |  |  |
| [Create Production Order for Spare Part Bundle](#unique_62) | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Production Order for spar part bundle is available |
| [Material Staging for Final Assembly (BJ5)](#unique_63) | Production Operator - Discrete Manufacturing | Stage Materials for Production (MF60) | Material is staged for final assembly. |
| [Release Production Orders](#unique_64) | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | Production Order is released. |
| [Confirm Assembly Activities](#unique_65) | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | Assembly is confirmed. |
| [Event-Based Work in Process (Optional)](#unique_66) | Cost Accountant - Production | Work in Process - Event-Based (F3498) | Review event-based WIP and variance |
| [Post Goods Receipt for Production Order](#unique_67) | Warehouse Clerk | Post Goods Receipt for Production Order (F3110) | Goods receipt for production order is posted. |
| [Analyze Event-Based Production Variances (Optional)](#unique_68) | Cost Accountant - Production | Order Cost Details - Event-Based (F4254) | Analyze event-based orders |
| [Create Outbound Delivery](#unique_69) | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Outbound delivery for sales order is created. |
| [Execute Picking](#unique_70) | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Picking is executed. |
| [Post Goods Issue](#unique_71) | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Goods issue for delivery is posted. |
| [Check Event Based Revenue Recognition – Project Accounted Sales](#unique_72) | Cost Accountant - Sales | 1. Manage Real-Time Revenue Recognition Issues (F4101)2. Run Revenue Recognition - Projects (F4277) | The profitability and the recognized revenue for the project can be analyzed |
| [Change Sales Orders (Remove Billing Block) (Optional)](#unique_73) | Internal Sales Representative | Manage Sales Orders (F1873) | Billing block for sales order is removed. |
| [Billing](#unique_74) | Billing Clerk | Create Billing Documents (F0798) | Billing is executed. |
| [Check Event Based Revenue Recognition – Project Accounted Sales (Optional)](#unique_75) | Cost Accountant - Sales | 1. Manage Real-Time Revenue Recognition Issues (F4101)2. Run Revenue Recognition - Projects (F4277)3. Projects - Actuals (F0961) | The profitability and the recognized revenue for the project after billing the sales order item can be analyzed. |
| [Accounts Receivable](#unique_76) | Accounts Receivable Manager | Accounts Receivable Overview (F3242) | Accounts receivable overview is displayed. |
| [Post Incoming Payments](#unique_77) | Accounts Receivable Accountant | Post Incoming Payments (F1345) | Incoming payments are posted. |
| [Time Recording](#unique_78) | Employee | Manage My Timesheet (F1823) | The recorded time is posted. |
| [Time Recording](#unique_79) | Employee | Manage My Timesheet (F1823) | The recorded time is posted. |
| [Complete Milestone](#unique_80) | Project Manager | My Projects - Project Manager (F1876) | Milestones are updated with the actual dates and completed. |
| [Monitor Projects via Project Cost Report](#unique_81) | Project Financial Controller | Project Cost Report - Plan/Actual (F2513) | All plan, actual costs, and their variances can be analyzed |
| [Check Event Based Revenue Recognition – Project Accounted Sales](#unique_82) [page ] 132 | Cost Accountant - Sales | Event-Based Revenue Recognition - Projects (F4767) | Project revenue recoginition checked |
| [Monitor Revenue Recognition (Event-Based): Projects](#unique_83) [page ] 133 | Cost Accountant - Sales | Event-Based Revenue Recognition - Projects (F4767) |  |
| [Run Revenue Recognition: Projects](#unique_84) [page ] 134 | Cost Accountant - Sales | Run Revenue Recognition - Projects (F4277) |  |
| [Close Project](#unique_85) | Project Financial Controller | Project Control - Enterprise Projects (F3215) | Project Status is changed to CLSD (Closed). |

## Test Procedures

### Create and Send Sales Quotation to Customer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

As an ETO manufacturer, you have a potential customer for whom you are creating a sales quotation. This process step shows you how to create a sales quotation and send it to the customer.

| Item Number | Material ID | Price | Currency | Quantity | UoM | ItCa (Item Category) |
| --- | --- | --- | --- | --- | --- | --- |
| 0010 | NS0611 | 40000 | EUR | 1 | PC | AGX |
| 0020 | FG0611 | 1 | EUR | 1 | PC | CBQX |
| 0030 | FG0612 | 1 | EUR | 1 | PC | CBQX |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Quotations (F1852). |  |  |
| 3 | Create Sales Quotation | On the Manage Sales Quotations (F1852) screen, choose Create Quotation.Make the following entries and press Enter:Quotation Type: QTSales Organization: 3310Distribution Channel: 10Division: 00 | The Create Quotation: Overview screen displays. |  |
| 4 | Enter the Quotation Details | Make the following entries:Sold - to Party: 33100004Ship - to Party: 33100004Cust. Reference: <PO Number>Cust. Ref. Date: <Today's Date>Req. Deliv. Date: <Today plus 2 month>Valid to: <Today plus 12 weeks>In the All Items table, create an entry with the following data:Material: <According to the table above>Price: <According to the table above>Order Quantity: <According to the table above>Item Category: <According to the table above>Choose Save (Ctrl+S). | A message displays: Message Quotation XXXXXXXX has been saved.The order is saved and the quotation is sent to the printer.Note Ignore any dialog box. |  |

Printing Form (Optional)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Quotations (F1852). | The Manage Sales Quotations screen displays. |  |
| 3 | Search for Sales Quotation | Use filter bar to search for the created sales quotation.Enter <sales quotation number> in the Sales Quotation field. | Searched sales quotation displays. |  |
| 4 | Display Quotation Print Previewn | Choose sales quotation number and choose Display Sales Quotation.On the Display Quotation XXX: Overview screen, choose Menu > Extras > Output > Header > Edit . Select the sales quotation line item and choose Display PDF Document. | Preview for PDF document displays. |  |

Result

A sales quotation is created and sent to the customer.

### Create Project

Purpose

In this activity, you can create a project with revenue with the project definition and WBS element using the Project Control - Enterprise Projects (F3215) app.

Projects with Revenue allow revenue G/L journal entries postings after release. The profitability segment characteristics can be maintained in the settlement rule, however running the settlement isn’t required anymore due to the direct attribution of cost postings.

For hierarchical project accounting requirements, you can also create a hierarchical project structure by calling up the Project Planning application from the Project Control - Enterprise Projects (F3215) app.

|  |
| --- |
| Note For extended project management capabilities like project scheduling, please refer to the scope item Collaborative Project Management (6JN ) |

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Project Control - Enterprise Projects (F3215). | The Project Control screen is displayed. |  |
| 3 | Create Project: Definition | Choose Create.Make entries as shown in the following example in the Header and General Information sections:HeaderProject Name: Project with RevenueProject ID: R.000001Project Profile: Project with RevenueMultiple Sales Order Item Scenario: SelectedNote By selecting this check box, you can assign more than one billing relevant sales order item to the same billing work package.Choose the right setting on the project before the first save. After the first save, this decision cannot be changed.The setting done on the project level would be valid for all the billing work packages in that project.Sales order items having different revenue recognition keys cannot be assigned to the same billing work package.In case the Multiple Sales Order Item Scenario is NOT selected, the profitability characteristics are automatically derived based on the sales order and sales order item. In case the Multiple Sales Order Item Scenario is selected, the profitability characteristics must be defined by the user in the Settlement Rule.Planned Start: Today (MM/dd/yyyy)Planned Finish: Today + 3 months (MM/dd/yyyy)General information:Responsible Cost Center: 33101501 (R&D Cost center) (for example)Profit Center: YB600 (Shared Services)Project Currency: AED(Automatically filled based on the cost center)Note You can specify the currency at project level different from controlling area currency, to run project- specific financial reports.Project Manager: the Project Manager IDPriority: the priority suitable for projectProject Type: Project Type created in [Create Project Types for WBS Elements (Optional)](#unique_10) [page ] 19Attachments: Choose + to upload project relevant documents from your local drive.Note To rename the existing attachment, choose the Edit icon present next to the attachment and change the file name according to the requirement and choose Rename.Choose Create.The project is saved and a confirmation message is displayed. | Project is created with the provided definition parameters.One WBS Element with details as shown in the following example will be created under the project:WBS Element ID: R.000001Project Name: Project with Revenue |  |
| 4 | Add Values to the Project Summary Task WBS Element | Once the project is created, from the header section, choose Edit.Make the following entries:General InformationPlant: 3310Functional Area: YB25 (Consulting/Services)ControlCosting Sheet: 3310PIThe following are optional entries, maintain them according to your requirements.Budget Availability Control Profile: ZS001If project currency is maintained, you can assign a budget availability control profile where the budget currency is maintained as Global Currency or Project Currency.If project currency is not maintained, you can only assign an availability control profile where the budget currency is maintained as Global Currency.Budget Availability Control Profile is active: SelectedAs soon as you have selected and used a Budget Avability Control Profile, a budget needs to be uploaded.You can define your own budget availability control profile using the Maintain Budget Availability Profile SSCUI.As soon as you have planned budget for your project and activated the budget availability control, the hierarchy changes are no longer possible.Block FunctionsTime Recording: <Selected/Not Selected>Activity Allocation: <Selected/Not Selected>Purchasing: <Selected/Not Selected>Concur Expense Posting: <Selected/Not Selected>Other Expense Posting: <Selected/Not Selected>Setting up the block functions at Project Header level will not impact the complete project hierarchy.The Block functions need to be set at the individual Work Package level to enable the functionalityEven if the user blocks purchasing for a WBS Element, the system can still generate purchasing documents if the account assignment category in the purchase document is "Q" (Project Make-to-Order) and the account is associated with that WBS Element.To resolve this issue, refer to the following Knowledge Base Article (KBA) note and apply the resolution mentioned in it.[https://me.sap.com/notes/3459521](https://me.sap.com/notes/3459521)Choose Save.A system message tells you that the project has been savedNote In case you have entered a budget availability control profile and activated the budget availability control, all the postings resulting into commitments or actual costs will be checked against the available budget of the WBS element used as account assignment object.In case the WBS element does not have any budget, the next higher level budget carrying WBS element will be used for the budget availability check.Depending on the tolerance limits defined for the availability control profile, the system can raise warning or error messages.Depending on the Time Range defined for the availability control profile, you will be able to check the budget consumption for a particular fiscal year or across fiscal years. This setting is valid for all kind of expense postings and expected expense postings (for example, purchase requisition or purchase orders) to a WBS element.Warning messages from budget availability check are not shown in case of automatic periodic postings and certain goods movement. | WBS Element updates with all the provided parameters. |  |
| 6 | Navigate to Project Planning | Once the project is created, from the header section, choose Related Apps. A pop-up screen appearsFrom the pop-up screen, select Project Planning to go to the Project Planning app.Note By default, the project will open in the Display mode. To edit the project, choose Edit. | The Project Planning app is opened and you can make further entries. |  |
| 7 | Create WBS Packages under Project Summary Task WBS Element | In the Project Structure view, select WBS Element created in the above step, and choose Create.Make the following entries in the Details screen onto the right.ID: <Example: R.0000011>Name: WBS for project planningProfit Center: <This data is pre-populated from the first WBS level>Responsible Cost Center: <This data is pre-populated from first WBS level>Planned Start: TodayPlanned Finish: Today + 3 monthsIn the Project Structure view, select WBS Element created in the above step, and choose Create.ID: <Example: R.0000012>Name: WBS for project executionProfit Center: <This data is pre-populated from the first WBS level>Responsible Cost Center: <This data is pre-populated from first WBS level>Planned Start: TodayPlanned Finish: Today + 3 monthsCreate work package structure based on your requirements.Note You can also create workpackage by making use of the Copy functionality available in the Project Planing ApplicationNote In the Project Planning app, the user is able to maintain multiple billing work packages by setting the Billing Element flag. In order to ensure the correct handling of CO-PA attributes, the billing work packages can not be in the same sub-structure, meaning that it is not allowed to have one billing element under another billing element in the structure. Also, the work packages that are under a billing element must have the same company code, profit center and functional area to ensure the same profitability segment postings. | Project with WBS Element structure is updated with the provided parameters. |  |
| 7 | Create WBS Packages under Project Summary Task WBS Element | In the Project Structure view, select the Root WBS Element created in the previous step (should have the same name as the project), and choose Create.ID: <Example: R.0000011>The ID is given by the system and can be adapted.Make the following entries in the newly created WBS element:Name: WBS for project planningProfit Center: <This data is pre-populated from the first WBS level>Responsible Cost Center: <This data is pre-populated from first WBS level>Planned Start: TodayPlanned Finish: Today + 3 monthsIn the Project Structure view, select WBS Element created in the previous step, and choose Create.Make the following entries in the newly created WBS element:ID: <Example: R.0000012>Name: WBS for project executionProfit Center: <This data is pre-populated from the first WBS level>Responsible Cost Center: <This data is pre-populated from first WBS level>Planned Start: TodayPlanned Finish: Today + 3 monthsIn the Project Structure view, select WBS Element created in the previous step, and choose Create.Make the following entries in the newly created WBS element:ID: <Example: R.0000013>Name: WBS for project executionProfit Center: <This data is pre-populated from the first WBS level>Responsible Cost Center: <This data is pre-populated from first WBS level>Planned Start: TodayPlanned Finish: Today + 3 monthsChoose table view.In the next step adjust the filter: choose settings and choose a billing element. Select OK to confirm.Ensure the Root WBS element should have a tick while the three subordinate WBS elements should have the value No.Create WBS element structure based on your requirements.Note In case you want to mark a Level 2 WBS Element as Billing Element, you need to navigate to Project Planning, create a Level 2 WBS Element, uncheck the Billing Element Flag of the Root Level WBS Element and check the Billing Element Flag of newly created Level 2 WBS Element.Note You can also create a WBS element by making use of the Copy functionality available in the Project Planing ApplicationNote In the Project Planning app, the user is able to maintain multiple billing work packages by setting the Billing Element flag. In order to ensure the correct handling of CO-PA attributes, the billing work packages cannot be in the same sub-structure, meaning that it is not allowed to have one billing element under another billing element in the structure. Also, the WBS elements that are under a billing element must have the same company code, profit center and functional area to ensure the same profitability segment postings. | Project with WBS Element structure is updated with the provided parameters. Three non-billing subordinate WBS Elements below the root WBS Element should be created. |  |
| 8 | (Optional) Assign Profitability Segment | From the header section, choose EditUnder the Control section choose the Assign button below the field Profitability SegmentOn the Assignment to Profitability Segment pop screen, make the following entries:Functional Area: YB10Plant : 1010Choose Derive and CloseNote Once the project / billing work package is account assigned to only one billing and pricing relevant sales order items (and multiple free of charge SO items), the profitability characteristics are automatically derived once the billing work package is assigned to the sales order item. In this case, the maintenance of the profitability segment is optional. However, If a profitability segment is maintained, this would have priority and the profitability characteristics for each posting would be taken from profitability segment.In case the project/ billing work package is account assigned to multiple billing and pricing relevant sales order items (and multiple free of charge SO items) it is recommended to maintain the profitability segment attributes so that postings can derive the values from the segment. In case these are not maintained, no profitability attribute would be derived. | The Project Control screen is displayed with the system message confirming that the settlement rule is saved.Note Users can maintain a profitability segments for the billing element only. The characteristics are used to attribute cost/revenue postings to the billing and lower level Work Packages. |  |
| 10 | Save Project Structure | Choose Save. | Project with WBS Element structure is saved. |  |

### Describe Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Project Manager describes the project details, such as Milestones, for the first time.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager. |  |  |
| 2 | Access My Projects (Active Projects) | Open My Projects - Project Manager (F1876) app. Choose Planned Projects to go to Project Briefs. | The Project Briefs screen appears. |  |
| 3 | Open the Project | From the Projects displayed, select the project and click to open the project. | Selected project is displayed. |  |
| 4 | Choose Edit | Choose Edit to change the project from Display to Edit mode.Note By default, the project will open in the display mode. | Project is editable. |  |
| 5 | Maintain Priority and Project Type | Select the priority and project type suitable for the project from the drop-down option list. |  |  |
| 6 | Define Milestones | From the Milestones tab, click Create to add the list of relevant milestones. | All the milestones are saved and displayed. |  |
| 7 | Maintain the Planned Finish Dates for the Milestones | For each milestone, select the Planned Finish date. | Planned Finish dates for the milestone are maintained. |  |
| 8 | Define Team | Scroll down to the Responsibilities section and choose + to maintain the names of steering committee team members, project financial controller and team members with relevant roles.Note The assigned team members will be able to find the WBS elements of Projects assigned in the search box of the Time Recording app and create tasks with those WBS elements and record their time according to the steps mentioned in the Time Recording (1Q4) test script.Choose Create. | Team member details are maintained |  |

### Upload Planned Costs and Revenues

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you upload planned costs to WBS elements.

|  |
| --- |
| Note You will be able to use the Analytics Cloud functionality to input planned costs to the project by using the test script for scope item [2YG](https://me.sap.com/processnavigator/SolP/2YG).If Project Budget Profile is selected and used, upload a budget using the planning template (see Adapt the Project Planning Template section below) and planning category BUDGET01. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open the Import Financial Plan Data (F1711) app. | The Import Financial Plan Data screen is displayed. |  |
| 3 | Download Template; Fill the planned costs in the CSV file | Choose Download Templates. A pop-up window appears.In the pop-up window, choose , (Comma) from the Separator for .csv files dropdown and then choose Project Planning; the template CSV file will be downloaded to the local machine.Choose Close.Access the file and fill the plan values.Make sure to save the file in CSV (Comma delimited) (*.csv) format.Note Remember the location of the file stored. | CSV file is saved with the plan costs. |  |

Adapt the Project Planning Template

A template table is provided for your reference with sample values as follows:

| Category | Posting Period | Company Code | Project Definition | Work Breakdown Structure Element (WBS Element) | Account Number | Amount in Global Currency | Global Currency |
| --- | --- | --- | --- | --- | --- | --- | --- |
| X | X | X | X |  |  |  |  |
| PLN | <current month>Example 2 | 3310 | R.000001 | R.000001 | 41000000 | -40000 | USD |
| PLN | <current month>Example 2 | 3310 | R.000001 | R.0000011 | 61005000 | 20000 | USD |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 4 | Import Planned Cost Data | Choose Browse. Select the CSV file from the local system which has the planned cost data already maintained for the project created above.Choose Import Source File. | The plan data has been imported successfully. |  |

### Change Sales Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After you have sent the quotation to customer, the customer sends a specification document and requests a commercial change (discount). Therefore, you change the quotation and send to the customer. A file of the specification document is attached to sales quotation as well. This process step shows you how to change sales quotation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Quotations (F1852). | The Manage Sales Quotations screen displays. |  |
| 3 | Search for Sales Quotation | Use filter bar to search for the created sales quotation.Enter <sales quotation number> in the Sales Quotation field. | Searched sales quotation displays. |  |
| 4 | Navigate to Sales Quotation Screen | Choose sales quotation number and choose Change Sales Quotation. | The Change Quotation XXXXXXXX: Overview screen displays. |  |
| 5 | Create Attachment for Sales Quotation (Optional) | Choose Services for Object on top right corner of the screen, choose Create Attachment.In the File Upload dialog box, choose OK.Choose local path and Customer specification file you downloaded. | A message displays: The attachment was successfully created. |  |
| 6 | Check Attachment (Optional) | Choose Services for Object, choose Attachment list and Continue. | Attachment brings up on the Service: Attachment list screen. |  |
| 7 | Enter Discount Amount and Save | On the Sales tab, in the All Items table, select line Item 10 (NS0611), and select Display Item Details button.Choose the Conditions tab.In the Pricing Element table, choose + (Insert Rows) icon to add a new entry with the following data and press Enter:CnTy: DPG4Amount: <25>Choose Save. | The Change Quotation screen displays with a message: Quotation XXXXXXXX has been saved. The new price of the quotation should be 30000 EUR after discount. |  |
| 8 | Save the Sales Order | Choose Save. |  |  |

Result

You entered a customer discount and created an attachment for sales quotation.

### Re-upload Planned Costs and Revenues

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you re-upload planned costs to WBS elements.

|  |
| --- |
| Note You will be able to use the Analytics Cloud functionality to input planned costs to the project by executing the [2YG test script](https://me.sap.com/processnavigator/SolP/2YG).If Project Budget Profile is selected and used, upload a budget using the planning template (see Adapt the Project Planning Template section below) and planning category BUDGET01. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open the Import Financial Plan Data (F1711). | The Import Financial Plan Data screen is displayed. |  |
| 3 | Download Template and Fill the Planned Costs in the CSV File | Choose Download Templates. A pop-up window appears.In the pop-up window, choose , (Comma) from the Separator for .csv files dropdown and then choose Project Planning; the template CSV file will be downloaded to the local machine.Choose Close.Make sure to save the file in CSV (Comma delimited) (*.csv) format.Note Remember the location of the file stored. | CSV file is saved with the planned costs. |  |

Adapt the Project Planning Template

A template table is provided for your reference with sample values as follows:

| Category | Posting Period | Company Code | Project Definition | Work Breakdown Structure Element (WBS Element) | Account Number | Amount in Global Currency | Global Currency |
| --- | --- | --- | --- | --- | --- | --- | --- |
| X | X | X | X |  |  |  |  |
| PLN | <current month>Example 2 | 1010 | R.000001 | R.000001 | 41000000 | -30000 | USD |
| PLN | <current month>Example 2 | 1010 | R.000001 | R.0000011 | 61005000 | 20000 | USD |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 4 | Import Planned Cost Data | Choose Browse. Select the CSV file from the local system which has the planned cost data already maintained for the project created above.Choose Import Source File. | The plan data has been imported successfully. |  |

### Release Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you release the project to enable the project execution.

|  |
| --- |
| Note To use the workflow for the project release approval process, perform the steps described in Review Workflow for the Release of a Project (Optional) of the Project Review (1YF) test script, using the project from this document. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open the Project Control - Enterprise Projects (F3215) app. | The Project Control screen is displayed. |  |
| 3 | Open Project | In the Standard section, make the following entries, and choose Go.Project : <Refer the respective Project created in [Create Project](#unique_20) [page ] 42.R.000001 (for Revenue Project). | At least one entry is displayed in the Worklist area. |  |
| 4 | Release project and structure | Select the project and in header section choose Processing Status > Release. | Project status is changed to Released.You can also use the Change Processing Status option in the Project Briefs app in a Project Manager role.Project once released cannot be renamed or deleted. |  |
| 5 | Maintain actual start date in WBS Elements | Choose Related Apps > Project Planning. Choose Edit to open the project in change mode.For all the created WBS elements, maintain the Actual Start Date field in the Project Structure View page.Note If the Actual Start field is not displayed, then select the Settings icon on the right of the top tool bar menu and view in the table mode.Choose Save. | Project is saved with WBS elements Actual start dates. |  |

### Procurement Process for long lead Components

|  |
| --- |
| Note You can skip these process steps for procuring long lead components by directly receiving the material into the receiving storage location by using the MIGO transaction (refer to chapter Create Initial Material Stock). |

#### Define Demand for Preliminary Procurement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you define demand for material in project stock which helps in planning, triggering, and monitoring preliminary procurement of long lead stock materials for enterprise projects. This process step results in the creation of Planned Independent Requirements (PIR). A demand represents a certain need of a WBS element at a certain time and at a certain location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Controller - Resourcing and Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Project Demand (F4562). | The Manage Project Demand screen is displayed. The screen has the following four tabs:All DemandsServicesMaterialsResources |  |
| 3 | Create Demand for Stock Materials | Select the Materials tab and choose Create.Make the following entries in the Demand section:Demand Name: <Example: New Demand For Stock Material>WBS Element: It is needed to enter the first subordinate WBS; the same which is assigned to the sales order item where FG0611 is entered.Demand ID: Incremental Demand ID is automatically generated.Note The Demand ID field is a free text field. Any value can be maintained, but duplicate values under the same WBS element are not allowed.You can create demands only for projects which support project stock such as the Profile Investment Project and Project with Revenue. You can also only use materials which support this process.Demand Type: Project Stock, Preliminary ProcurementMaterial:Example RM0615Quantity:Example 1Note You can change the demand dates and demand quantity of service or non-stock demands even after a demand was requested.Plant: Automatically derived from the WBS Element.Example 1710Date Alignment: Align with WBS Element start dateDemand Date: Automatically determined from WBS elementBased on the date alignment selected, the demand date gets automatically selected from the WBS element.Demand Status: Requested on SaveMake the following entries in the Procurement section:Requirement Plan: <Automatically populated>Note In case the requirement plan is a duplicate ID, please manually enter a unique requiremt plan ID.Choose Create. | The following demands are created with the provided definition parameters. |  |

#### Material Requirements Planning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use Material Requirements Planning (MRP) to tailor available capacities and receipts on time to suit requirements quantities. Single item multi-level requirement planning is performed for plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirement Planning (MRP)Job Name: <MRP for RM0615Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Recurrence Pattern: Single RunChoose OK.Choose Step 3.For 3 Parameters section:Plant: 3310Material: RM0615Material Scope: All Materials (A) selectChanged BOM Components: selectPlanning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for RM0615 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

#### Monitor Material Coverage

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock and requirements situation for the raw material (RM0615) in the stock and requirements list after the requirements planning performed.

Prerequisite

Requirements planning has been carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments (F2101A) Screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 4 | Select Material | In the search area, make the following entries and choose Go.Material: RM0615Select the filtered rows and choose Manage Materials. | The Manage Material Coverage screen displays. |  |
| 5 | Review Stock and Requirements List | Choose the corresponding material in the Materials list on the left side. | The detailed Stock and Requirements List for each material displays. |  |
| 6 | Display Purchase Requisition | From the left Materials list, choose the material for which you want to check the purchase requisition (assigned to your project).Material: RM0615On the right screen, choose and take note of the PurRqs. XXXX in column MRP Element. | The Purchase Requisition you selected displays in the dialog box.If there is no shortage for those materials, the purchase requisition will not be generated.If you want to display more information about the purchase requisition, at the bottom of this dialogue, choose Document Info > Purchase Requisition . |  |
| 7 | Note | The BOM explosion during the MRP run has generated dependent requirements for the planned components. If inventory does not cover the requirements, planned orders are created for in-house-produced materials or purchase requisitions for externally procured materials. |  |  |

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
| 3 | Search for Purchase Requisition | Enter the Purchase Requisition number. If the field purchase requisition is not displayed, change the filter settings accordingly. Choose Go. | The Purchase Requisition is displayed. |  |
| 4 | Select Purchase Requisition | Select the Purchase Requisition. | The Purchase Requisition has been selected for source assignment. |  |
| 5 | Assign Source to Purchase Requisition | Choose Show More per Row. If the Purchase Requisition has been assigned the source, then you don't need to assign source again for this step. If the Purchase Requisition hasn't been assigned the source, choose Assign Source of Supply, and select Info Record (XXXXXX) as the source. | The assignment of one source to the requisition is done. |  |
| 6 | Prepare the Purchase Order | Select the purchase Requisition where the assigned supplier is displayed and choose Create Purchase Order.You can close any warning or error messages that are displayed. | The Purchase Order Preview screen is displayed. |  |
| 7 | Create the Purchase Order | In the New Purchase Order screen, make the following entries:Purchase Order Type: Standard PO.Choose Order. | The purchase order is created. |  |
| 8 | Back to Process Purchase Requisition | Click on Back to go to Process Purchase Requisitions (F1048A). | Purchase Requisition list is displayed again.The Processing Status of Purchase Requisition has been changed to PO created. |  |

#### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you release a purchase order. If the total amount of PO > 500 AED and purchase group is 001, then the purchase orders should be approved. To decide which POs need approval, please refer to Configure Flexible Workflow for Purchased Order in Preliminary step.

Prerequisite

A purchase order must exist for release.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862) . | A list of existing Purchase Orders is displayed. |  |
| 3 | Search for Purchase Order Status | Make the following entry and choose Enter:Search: <Purchase Order number> | The Purchase Order is displayed. |  |
| 4 | Approve Purchase Order | Select the Purchase Order on the left side of the screen and choose Approve at the bottom right. | The Submit Decision screen is displayed. |  |
| 5 | Enter Approval Reason | Enter the approval reason if necessary, and then choose Submit. | The Purchase Order is approved. |  |

|  |
| --- |
| Note If an attachment is uploaded during purchase order creation, in My Inbox App, the attachment can be found under Attachments tab of the purchase order. |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity posts the receipt of goods with reference to an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Post Goods Receipt for Purchasing Document (F0843). | The Post Goods Receipt for Purchasing Document screen is displayed. |  |
| 3 | Search for Purchase Order | Enter your Purchase Order number in the search field and choose Enter. | A list of Purchasing Documents displays. |  |
| 4 | Select Item | Select your line item for which goods receipt is to be posted. Inside the item view, ensure Storage Location is 331C and select Apply at the bottom. | The system displays the data for the goods receipt on the Goods Receipt screen. |  |
| 5 | Enter Delivery Note | On the main screen, enter a Delivery Note on the header. | The Post Goods Receipt screen displays. |  |
| 6 | Post | Choose Post. | The system displays the message Material Document <Document No> posted. |  |

#### Create Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform the invoice verification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Supplier Invoice (F0859) . | The Create Supplier Invoices screen is displayed. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Reference: Enter the reference document number of the supplier for example: 12345678Gross Invoice Amount : <XXX>Currency: AEDInvoice Date: <Today>Posting Date: <Today>Baseline Date: <Today> (in Payment tab)Invoice Party: 33300001 (same as source of supply in PO) | The Create Supplier Invoices screen displays. |  |
| 4 | Enter Purchase Order References | In Purchasing Document References, make the following entries (use a PO you created previously) and choose Enter.Reference Document Category: Purchase Order/ Scheduling AgreementPurchase Order: <PO number> | The Purchase Order References screen displays. |  |
| 5 | Select Purchase Order Items | Check the selection of the Purchase Order Items.Confirm the warning messages. | All items of the selected Purchase Order are added to the Purchase Order Item table.You should see material items and delivery costs items which refer to the entered purchase order document. Check if items for planned delivery costs have an item text. |  |
| 6 | Check the Purchase Order Items Data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Purchase Order Item's table displays. |  |
| 7 | Check Tax code | In the section Tax check if there is tax code information and enter the tax amount.when the tax code value is greater than zero. | In the Tax tab, you should see the same tax codes as in the items.If there is no tax, specify the tax code <Input Tax Code>. |  |
| 8 | Check the Balance | Calculate the tax amount from the item amount multiplied by the tax value. Check the balance (difference between the calculated amount and the gross Amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 9 | Simulate Supplier Invoice and Check Messages | Choose Simulate.If there are no differences(or if the value is within the defined tolerance), a new screen Simulation appears. You can check the simulation results in Simulation Overview and Simulation Details area.Check the Gross Invoice Amount against the items plus tax amount (if tax code is <Input Tax Code> , you do not have any tax amount) | The supplier invoice is complete to simulate. |  |
| 10 | Post Invoice | Choose Post. | The invoice is posted. The system displays the message that the invoice xxx has been posted and document no. 51xxxxxxxx has been created. |  |

### Create Sales Order

#### Create Sales Order with Reference to Sales Quote and Assign WBS Element

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order with a sales order item that has a billing plan where the first item is a down-payment. The sales order item has the project created before as account assignment.

Procedure

Use the following table as reference when creating the sales order items:

| Item Number | Material ID | Quantity | UoM | ItCa (Item Category) | WBS Element |
| --- | --- | --- | --- | --- | --- |
| 0010 | NS0611 | 1 | PC | CTAD | Root WBS |
| 0020 | FG0611 | 1 | PC | CBLN | Subordinate WBS Element 1 |
| 0030 | FG0612 | 1 | PC | CBLN | Subordinate WBS Element 2 |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Create Sales Documents screen, choose Create, and choose Create Sales Order-VA01.Make the following entries and choose Create with Reference:Order Type: ORSales Organization: 3310In the Create with Reference dialog box, make the following entries and choose Copy.Quot.: <Sales Quotation Number Created Previously> | The Create Standard Order: Overview screen displays. |  |
| 4 | Enter Order Details | Make the following entries and press Enter.Cust. Reference: <Cust. Reference>Cust. Ref. Date: <Today's Date>On the Sales tab:Req. Deliv. Date: <Today's Date + 1 Month> |  |  |
| 5 | Enter Item Details | Select the item on the Sales Overview and enter:Item Category: <According to the table above>Select the line item. Choose More > Goto > Item > Account Assignment (or click on the line item) and enter:WBS Element: <According to the table above>Repeat this for all 3 Sales Order line items. |  |  |
| 6 | Choose Billing Plan | Select the item. Choose Menu > Goto > Item > Billing Plan .Note Alternatively, you can assign billing plan on header level: Choose Menu > Goto > Header > Billing Plan . The header billing plan will be applied to all items with item category CBAO, CTAD, or CTAX. Amount is proportionally to the value of the items participating in the down payment process distributed to the items. |  |  |
| 7 | Enter Details | For the first line item (Down Payment), make the following entries for the advance payment:Billing Date: <billing date>. For example, enter today's date.Bill Value: <amount of billing>. For example: Down Payment amountDate category (DCat): 04 |  |  |
| 8 | Enter Details | For the second line item (Closing Invoice), make the following entries for the advance payment:Billing Date: <billing date>. For example, enter today's date.Date category(DCat): 02 |  |  |
| 9 | Enter | Choose Enter. Confirm system messages with enter if necessary. |  |  |
| 10 | Save Sales Order | Choose Back.Choose Save and save your entries and proceed with the price related warning message. |  |  |

#### Check the Recognition Key on Project (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to ensure that the Recognition Key is updated on project, which is a MUST for the Event-Based Revenue Recognition Posting.

Prerequisite

In case the project/ billing work package is account assigned to multiple billing and pricing relevant sales order items (and multiple free of charge SO items) , which means the Multiple Sales Order Item Scenario is selected on Project Header,

The derivation happens automatically when a pricing/billing relevant sales order item is account assigned to the billing WBS element.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Project Control(F3215). | The Project Control screen is displayed. |  |
| 3 | Check Recognition Key | Go to Project Control screen and check the revenue section. | The Project Control screen is displayed with the updated Recognition Key. |  |

#### Down Payment Process (Optional)

In case of including the down payment process, following test procedures should be completed.

##### Change Sales Orders (Remove Billing Block) (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to remove billing block from a sales order.

Prerequisite

The billing block must be manually removed for the first down payment request to be processed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders (F1873) screen displays. |  |
| 3 | Search For Sales Order | Enter search term(s) in filter bar and choose Go: for example, enter sales order number in Sales Order field. | Sales order displays in result list. |  |
| 4 | Navigate to Sales Order Screen | Select the sales order number and choose Change Sales Orders - VA02 (VA02). | The Change Sales Order xxx: Overview screen displays. |  |
| 5 | Choose Billing Plan | Select the line item. From the menu, choose Menu > Goto > Item > Billing plan .Note Alternatively, If you assign billing plan on header level: Choose Menu > Goto > Header > Billing Plan . Removal of billing block on header level also unlocks items automatically. | The Change Standard Order xxx: Item Data screen displays. |  |
| 6 | Remove Billing Block | In the Dates section, in the Block column delete the billing block for the Down payment item (keep the billing block for the Final Invoice item). |  |  |
| 7 | Back | Choose Back. |  |  |
| 8 | Save | Save your entries. | The billing block is removed. |  |

##### Create Down Payment Request (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a down payment request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798) under Sales > Billing Documents . | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings at the bottom bar. You can make the settings as follows :Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: ONAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for Billing List | In the search condition, enter criteria if necessary. | SD document(s) displays in the result. |  |
| 5 | Choose Sales Document | More than one SD document item appear in Billing Due List Items table, select the row relevant to down payment request, and choose Create Billing Documents. | The Create Billing Documents screen displays. |  |
| 6 | Maintain Billing Type and Billing Date | Choose billing type Down payment request (FAZ) and maintain billing date, for example current date, then choose Create. | The draft billing document is created. |  |
| 7 | Save Billing Document | On the Billing Document screen, choose Save.The draft billing document with ID TMPxxxxxxxx turns into a saved billing document with ID xxxxxxxx.Make a note of the billing document number: __________. | Billing document is generated. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| none | 21191000 Down payment requests (customers) | none | none |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797) under Sales - Billing Document | The Manage Billing Documents screen displays. |  |
| 2 | Search the Billing Document | Enter the billing document number recorded previously in Billing Document field and choose Enter. | The billing document which is created previously displays. |  |
| 3 | Display Billing Document | Select the billing document item, and choose Display. | The billing document screen displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, go to Output Items the last assignment block. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | On the Billing Document screen, select certain Billing document and choose Cancel billing Document. | Billing Document Canceled log displays. |  |
| 7 | Update New Attachment (Optional) | In the Edit mode, add, delete, and update the attachments.Save your changes by choosing Save in the footer bar. |  |  |
| 8 | Update New Text (Optional) | In the Edit mode, you can add, delete and update the texts.Save your changes by choosing Save in the footer bar. |  |  |

##### Post Down Payment (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the down payment received from your customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Accounts Receivable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Incoming Payments (F1345). | The Post Incoming Payments (F1345) screen displays. |  |
| 3 | Enter Details | Make the following entries and choose Propose Items:General Information area:Company Code: 3310Posting Date: Current dateJournal Entry Date: <Current date>Value Date: Current datePeriod: Current periodJournal Entry Type: DZ (Customer Payment)Bank Data areaG/L Account (Company Code CoA): 11001010House Bank: AEBK1/AEAC1Bank Account: AEAC1Amount: Down Payment Amount / AEDNote Enter the amount of the journal entry the customer has been debited with in the previous step (billing value plus value added tax).Open Item Selection areaAccount Type/Account ID: Customer / 33100004 |  |  |
| 4 | Search for Down Payment Request | Choose Select More.In Line Item Type field, select checkbox in Special G/L Transactions and deselect other values from drop-down menu, then choose OK. | Select More dialog box displays.All down payment request documents which meet the conditions are listed in Open Items table. |  |
| 5 | Select Down Payment Request | Choose Clear in the down payment request document entry in Open Items table. | The item is copied to Items to Be Cleared table. |  |
| 6 | Post | Choose Post. | Success dialog box pop ups, the information Journal entry 14XXXXXXXX successfully posted displays. |  |
| 7 | Display Journal Entry | Choose Display. | The Manage Journal Entries screen displays. Detailed information involved in down payment journal entry is shown. |  |

|  |
| --- |
| Note After the down payment is cleared, the delivery block set from SSCUI Define Date Categories for Billing Plan Types can be removed automatically if the checkbox Relevant for Down Payments is flagged in SSCUI Define Billing Plan Types for Milestone Billing for billing plan type 90.The delivery block in a schedule line won’t be removed automatically if the delivery block reason code differs from the one set in SSCUI Define Date Categories for Billing Plan Types. |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| none | 11001060 Bank Account21191500 Tax sett.dwn pmt cus | 21190000 Down Payments - Customers22000000 Output tax (MWS) | none |

### Material Requirements Planning for Sales Order

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
| 5 | Check MRP Run Parameters | Choose the user icon, and then choose the App Settings icon. On the MRP Settings dialog box, choose MRP Run Parameters.On the MRP Run Parameters dialog box:Select the Changed BOM Components checkbox.In the Scheduling drop-down list, select Lead Time Scheduling and Capacity Planning.Choose Save Settings.On the MRP Settings dialog box, choose OK. |  |  |
| 6 | Search for Material | Enter the following data and choose Go:Material: <FG0611 or FG0612>, <Depends on which material you test with> |  |  |
| 7 | Selection of Material | Select the rows which have FG0611 or FG0612 as the material.Choose Manage Materials. | The Material screen and Material Details screen display.Note that you select the right individual segment for the customer order. |  |
| 8 | Start MRP Run | Select the line item with your sales quotation / sales order number, such as CustSt XXXXXX-10.Choose Start MRP run. | A MRP run is started immediately in background. |  |
| 9 | Check Generated Planned Order | Choose the generated planned order, and choose Open > Planned Order .Choose Component Overview, check if the components are the same as in BoM. |  |  |

### Procurement Process for Raw Material

|  |
| --- |
| Note You can skip these process steps of procurement by directly receiving the material into the receiving storage location by using the MIGO transaction (refer to chapter Create Initial Material Stock). |

#### Monitor Material Coverage

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the requirement planning has been performed, you want to display the stock/requirements situation for the Raw Material (RM0612) in the stock/requirements list.

Prerequisite

Requirement planning has been carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 4 | Select Material and Show Shortages | In the search area, make the following entries and choose Go.Material: RM0612Plant: 3310Individual segment: created WBS elementSelect the filtered rows and choose Manage Materials. | The Manage Material Coverage screen displays. |  |
| 5 | Verify Purchase Requisitions that are Available | In the Stock/Requirements List, to find available purchase requisitions, look for rows with PurRqs items.Take note of the PurRqs. XXXX in column MRP Element. | The MRP has created purchase requisitions that can be used for the Procurement of Direct Materials (J45) test script. |  |

#### Process Stock Transport Requisition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how a purchase requisition for stock transfer is assigned and a corresponding purchase order is created.

If you want to use the Save Draft feature in this app, you have to use a personalized user.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Acess the App | Open Assign and Process Purchase Requisitions (ME57). | The Assign and Process Purchase Requisitions screen displays. |  |
| 3 | Search for Purchase Requisition | On the Assign and Process Purchase Requisitions screen, make the following entries:Purchase Requisition NumberAssigned Purchase Requisitions: XPartly Ordered Requisitions: XRequisitions for Overall Release: XRequisitions for Item-Wise Release: XThen choose Run (F8). | The Assign and Process Purchase Requisitions screen with purchase requisition items shows. |  |
| 4 | Select Purchase Requisition | Select the purchase requisition you want to process.To convert the assigned purchase requisitions into stock transfer orders, choose Edit Items.Ensure the following data in the purchase requisition item:Item category: USupplying Plant: 3320Storage Location: 331CThen choose Enter.The plant 3320 is shown as source of supply on the tab Assignments in the upper area.Choose Save. | The supplying plant 3320 shows as a line in Assignments part: Supplier/Supplying plant XXXX. |  |
| 5 | Process Assignments | Select the line with supplying plant in Assignment section, Choose Create Purchase Order. | The Create Purchase Order screen shows. |  |
| 6 | Adopt the Purchase Requisition and Create Purchase Order | In the dialog box, check the entries:Order Type: UB (Stock Transp. Order)Doc. Date: todayPurchase Group: 001Purchase Organization: 3310Company Code: 3310The Purchase Requisition is shown on the left in the document overview.Select this purchase requisition and choose Adopt. | The Create Purchase Order screen displays.All the information of the purchase requisition is copied into the stock transfer order. |  |
| 7 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | The system displays a message:Stock Transp. Order created under the number 45xxxxxxxx. |  |

#### Monitor Material Coverage

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock and requirements situation for the raw material (RM0612) in the stock and requirements list after the requirements planning performed.

Prerequisite

Requirements planning has been carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments (F2101A) Screen displays. |  |
| 3 | Select Material | Mark the checkbox of the following materials, and choose Manage Materials.Material: RM0612 | The Manage Material Coverage screen displays. |  |
| 4 | Review Stock and Requirements List | Select the corresponding material which assign to the used WBS element and plant 3320 on the left Material screen. | The detailed Stock and Requirements List for each material displays. |  |
| 5 | Display Planned Order | From the list on the left Material screen, select the material for which you want to check the purchase requisition.Material: RM0612On the Material Details screen, select and take note of the PurRqs. XXXX and take note of the purchase requisition number. |  |  |
| 6 | Note | The BOM explosion during the MRP run has generated dependent requirements for the demand-driven planned components. If inventory does not cover the requirements, planned orders are created for in-house-produced materials or purchase requisitions for externally procured materials. |  |  |

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
| 3 | Search for Purchase Requisition | Enter the Purchase Requisition number. If the field purchase requisition is not displayed, change the filter settings accordingly. Choose Go. | The Purchase Requisition is displayed. |  |
| 4 | Select Purchase Requisition | Select the Purchase Requisition. | The Purchase Requisition has been selected for source assignment. |  |
| 5 | Assign Source to Purchase Requisition | Choose Show More per Row. If the Purchase Requisition has been assigned the source, then you don't need to assign source again for this step. If the Purchase Requisition hasn't been assigned the source, choose Assign Source of Supply, and select Info Record (XXXXXX) as the source. | The assignment of one source to the requisition is done. |  |
| 6 | Prepare the Purchase Order | Select the purchase Requisition where the assigned supplier is displayed and choose Create Purchase Order.You can close any warning or error messages that are displayed. | The Purchase Order Preview screen is displayed. |  |
| 7 | Create the Purchase Order | In the New Purchase Order screen, make the following entries:Purchase Order Type: Standard PO.Choose Order. | The purchase order is created. |  |
| 8 | Back to Process Purchase Requisition | Click on Back to go to Process Purchase Requisitions (F1048A). | Purchase Requisition list is displayed again.The Processing Status of Purchase Requisition has been changed to PO created. |  |

#### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you release a purchase order. If the total amount of PO > 500 AED and purchase group is 003, then the purchase orders should be approved. To decide which POs need approval, please refer to Configure Flexible Workflow for Purchase Order in Preliminary step.

Prerequisite

A purchase order must exist for release.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F5331). | A list of existing Purchase Orders is displayed. |  |
| 3 | Search for Purchase Order Status | Make the following entry and choose Enter:Search: <Purchase Order number> | The Purchase Order is displayed. |  |
| 4 | Approve Purchase Order | Select the Purchase Order on the left side of the screen and choose Approve at the bottom right. | The Submit Decision screen is displayed. |  |
| 5 | Enter Approval Reason | Enter the approval reason if necessary, and then choose Submit. | The Purchase Order is approved. |  |

|  |
| --- |
| Note If an attachment is uploaded during purchase order creation, in My Inbox App, the attachment can be found under Attachments tab of the purchase order. |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity posts the receipt of goods with reference to an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Post Goods Receipt for Purchasing Document (F0843). | The Post Goods Receipt for Purchasing Document screen is displayed. |  |
| 3 | Search for Purchase Order | Enter your Purchase Order number in the search field and choose Enter. | A list of Purchasing Documents displays. |  |
| 4 | Select Item | Select your line item for which goods receipt is to be posted. Inside the item view, ensure Storage Location is 331C and select Apply at the bottom. | The system displays the data for the goods receipt on the Goods Receipt screen. |  |
| 5 | Enter Delivery Note | On the main screen, enter a Delivery Note on the header. | The Post Goods Receipt screen displays. |  |
| 6 | Post | Choose Post. | The system displays the message Material Document <Document No> posted. |  |

#### Create Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform the invoice verification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Supplier Invoice (F0859) . | The Create Supplier Invoices screen is displayed. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Reference: Enter the reference document number of the supplier for example: 12345678Gross Invoice Amount : <XXX>Currency: AEDInvoice Date: <Today>Posting Date: <Today>Baseline Date: <Today> (in Payment tab)Invoice Party: 33300001 (same as source of supply in PO) | The Create Supplier Invoices screen displays. |  |
| 4 | Enter Purchase Order References | In Purchasing Document References, make the following entries (use a PO you created previously) and choose Enter.Reference Document Category: Purchase Order/ Scheduling AgreementPurchase Order: <PO number> | The Purchase Order References screen displays. |  |
| 5 | Select Purchase Order Items | Check the selection of the Purchase Order Items.Confirm the warning messages. | All items of the selected Purchase Order are added to the Purchase Order Item table.You should see material items and delivery costs items which refer to the entered purchase order document. Check if items for planned delivery costs have an item text. |  |
| 6 | Check the Purchase Order Items Data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Purchase Order Item's table displays. |  |
| 7 | Check Tax code | In the section Tax check if there is tax code information and enter the tax amount.when the tax code value is greater than zero. | In the Tax tab, you should see the same tax codes as in the items.If there is no tax, specify the tax code <Input Tax Code>. |  |
| 8 | Check the Balance | Calculate the tax amount from the item amount multiplied by the tax value. Check the balance (difference between the calculated amount and the gross Amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 9 | Simulate Supplier Invoice and Check Messages | Choose Simulate.If there are no differences(or if the value is within the defined tolerance), a new screen Simulation appears. You can check the simulation results in Simulation Overview and Simulation Details area.Check the Gross Invoice Amount against the items plus tax amount (if tax code is <Input Tax Code> , you do not have any tax amount) | The supplier invoice is complete to simulate. |  |
| 10 | Post Invoice | Choose Post. | The invoice is posted. The system displays the message that the invoice xxx has been posted and document no. 51xxxxxxxx has been created. |  |

#### Post Goods Issue for Stock Transport Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods issue for stock transport order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Post Goods Receipt Purchase Order screen displays. |  |
| 3 | Select Goods Issue Order | On the following screen, make the following entries and choose Enter:Goods Issue: SelectPurchasing Order: SelectPurchasing Document Number: Purchase document number(Movement Type): 351 QChoose Execute or choose Enter. | The items for the selected purchase order displays. |  |
| 4 | Enter Data Details | Make the following entries:Quantity: quantity, for example, <1>Storage Location: 332AMake sure RM0612 have project stock in the storage location. If not, please do initial stock for them. |  |  |
| 5 | Check Item OK | Check if the item OK indicator is set. |  |  |
| 6 | Post | Choose Post. |  |  |

#### Check Status of Stock Transfer with Overdue Materials - Stock in Transit (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how notifications for overdue stock in transit send to the selected responsible team member. The detection process is automatically triggered by the system on a regular basis based on the batch job scheduling parameters maintained in preliminary step Create Situation Types.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The Fiori launchpad displays. |  |
| 2 | Check Notifications | On the home screen, choose the Notifications icon in the upper right corner. | The following notification displays: Stock Transport Order XXXXXXXXXX/00XX is overdue. |  |
| 3 | Navigate to Overdue Material Stock in Transit App | Choose the detailed notification line Stock Transport Order XXXXXXXXXX/00XX is overdue. | The Overdue Materials - SiT screen displays.Note If there is no notification, the Warehouse Clerk can navigate to the app Overdue Material – Stock in Transit and search directly for the Purchase Order. |  |
| 4 | Check Information on Overdue Stock Transport Order | Choose Stock Transport Order line of that have overdue alert. | Situation displays as Stock Transport Order is overdue. |  |

#### Post Goods Receipt for Stock Transport Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the stock transport order and post goods receipt.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Receipt for Purchasing Document (F0843). | The Purchasing Document screen displays. |  |
| 3 | Search for Purchasing Document | Open Purchasing Document Search. | A list of purchasing documents displays. |  |
| 4 | Select the Stock Transport Order | Select your purchase order. | The system displays the data for the goods receipt on the Post Goods Receipt screen. |  |
| 5 | Enter Delivery Note | Make the following entries and choose Enter.Delivery Note: xxxPrinting (Controls output management after posting): Individual slip |  |  |
| 6 | Select Item and Post Goods Receipt | Select the items for which a goods receipt is to be posted.Enter the following data:Storage Location: 331CChoose Post. | The Post is activated. The Post Goods Receipt screen displays. The system shows the message: Material document xxx posted. |  |

### Subcontracting with Plant Stock Components

|  |
| --- |
| Note You can skip these process steps of subcontracting by directly receiving the material into the receiving storage location by using the MIGO transaction (refer to chapter Create Initial Material Stock). |

|  |
| --- |
| Note You are also able to perform subcontracting with special stock component, but please keep in mind the following :Special Stock Subcon Process:The special stock subcontracting process is the same as the described process in this chapter with the exception of using special stock components.Master Data Changes:To enable special stock for the 6GD scenario (mixed stock subcon with RM0613 as plant and RM0614 as special) please proceed to change the material master for RM0614, under tab MRP4, and change the Individual/Col. Value to ‘1 ‘or ‘Blank’.Apply for feature (must do):As we need to onboard you on the limitations* that we have currently, we require you to apply for this feature in the form of an incident under component: MM-PUR-GF-SCR-2CLAdditional Steps:Please ensure the availability of RM0614 (Q) in your inventory as this is needed in the process. Refer to the “Create Initial Material Stock” chapter in “Preliminary Steps” for more details.*Before using the new solution, please refer to restriction note: [3728529](https://me.sap.com/notes/3728529) - Subcontracting with Special Stock |

#### Monitor Material Coverage

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock and requirements situation for the semifinished product (SG0612) in the stock and requirements list after the requirements planning performed.

Prerequisite

Requirements planning has been carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments (F2101A) Screen displays. |  |
| 3 | Select Material | Mark the checkbox of the following materials, and choose Manage Materials.Material: SG0612Individual Segment: Your WBS Element | The Manage Material Coverage screen displays. |  |
| 4 | Review Stock and Requirements List | Select the corresponding material on the left Material screen. | The detailed Stock and Requirements List for each material displays. |  |
| 5 | Display Purchase Requisition | From the list on the left Material screen, select the material for which you want to check the purchase requisition.Material: SG0612On the Material Details screen, select and take note of the PurRqs. XXXX and take note of the purchase requisition number. |  |  |
| 6 | Note | The BOM explosion during the MRP run has generated dependent requirements for the demand-driven planned components. If inventory does not cover the requirements, planned orders are created for in-house-produced materials or purchase requisitions for externally procured materials. |  |  |

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
| 1 | Log on | Open the Fiori Launch Pad using the Purchaser role. | The Fiori Launch Pad is displayed. |  |
| 2 | Open Manage Purchase Requisitions | Open Process Purchase Requisitions (F1048A). | A list of Requisitions is displayed. |  |
| 3 | Select Purchase Requisition | Search for a Purchase Requisition for material SG0612 with Sources available, and choose the link of the sources. | The Select Source of Supply screen is displayed. |  |
| 4 | Assign Source to Purchase Requisition | Choose a displayed source with a real price (not zero). | The assignment of one source to the requisition is done. The Purchase Requisitions list is displayed. |  |
| 5 | Prepare the Purchase Order | Select the purchase requisition where the assigned supplier is displayed and choose Create Purchase Order (Original). | The Purchase Order Preview screen is displayed. |  |
| 6 | Create the Purchase Order | Select Standard order from Purchase Order Type drop down list, and choose Save. | The purchase order is created. |  |
| 7 | Back to Manage Purchase Requisition | In the dialog box, choose OK. | Purchase Requisition list is displayed again. The converted Purchase Requisition has the status PO created. |  |

|  |
| --- |
| Note If you have not changed the flexible workflow for purchase order the automatic approval of the purchase order is active. In case you have an approval process in place, go to Subcontracting (BMY) test script and run Approve Purchase Orders as a Purchasing Manager with master data for this test script. About the PO approve user setting, please refer to the step Configure Your Release Conditions for PO Approval (Only for SAP S/4HANA Enterprise Management Cloud) in J45. You can use the App Manage Purchase Orders to display the created purchase order: Go to the Approval Details tab and check the approvers listed in section Approval Details. |

#### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you release a purchase order. If the total amount of PO > 500 AED and purchase group is 001, then the purchase orders should be approved. To decide which POs need approval, please refer to Configure Flexible Workflow for Purchased Order in Preliminary step.

Prerequisite

A purchase order must exist for release.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862) . | A list of existing Purchase Orders is displayed. |  |
| 3 | Search for Purchase Order Status | Make the following entry and choose Enter:Search: <Purchase Order number> | The Purchase Order is displayed. |  |
| 4 | Approve Purchase Order | Select the Purchase Order on the left side of the screen and choose Approve at the bottom right. | The Submit Decision screen is displayed. |  |
| 5 | Enter Approval Reason | Enter the approval reason if necessary, and then choose Submit. | The Purchase Order is approved. |  |

|  |
| --- |
| Note If an attachment is uploaded during purchase order creation, in My Inbox App, the attachment can be found under Attachments tab of the purchase order. |

#### Create Outbound Delivery

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Subcontracting Cockpit (F2948). | The Subcontracting Cockpit (Original) screen is displayed. |  |
| 3 | Search for Component or Assembly | Set values to some filters to search Components. :Subcontractor: 33300007Plant: 3310Shipping Date: <insert a valid range>Choose GO. | The search results show the details with the respective filter Criteria.Depending on the view setting the relevant data is shown. | The stock balance is calculated by selecting the link. |
| 4 | Display Purchase Order Item for a component | Choose small Arrow next to Component (RM0613 and RM0614) to expand the details. | All purchase order with items number corresponding to the component must be displayed in Purchase Order Items column. |  |
| 5 | Create Delivery | Choose the two PO Components with your purchaser order number (RM0613 and RM0614)and then choose Create Delivery. |  |  |
| 6 | Enter Detail Data | Enter Stor.Location for both lines:Storage Location: 331C |  |  |
| 7 | Post Delivery | Choose Create Delivery. Note down your delivery number. |  |  |

#### Pick and Post Goods Issue

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
| 1 | Log on | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Change Outbound Delivery (VL02N). | The app name screen displays. |  |
| 3 | Change Outbound Delivery | Enter the following data:Outbound Delivery: <your delivery>Choose Continue. |  |  |
| 4 | Picking | Choose Picking tab.Enter picked quantity equal to the delivery quantity.Choose Save. |  |  |
| 5 | Post Goods Issue (Original) | On the Change Outbound Delivery screen, choose Post Goods Issue. | The system displays the message 'Delivery for Subcon. xxx saved, material document xxx created.' |  |

#### Receive Goods from Subcontracting Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post the goods receipt for the material against the subcontracting PO.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The Fiori Launch Pad is displayed. |  |
| 2 | Open Post Goods Movement tile | Open Post Goods Movement (MIGO). | The Post Goods Receipt for Purchase Order (Original) screen is displayed. |  |
| 3 | Select Goods Receipt Order Screen | On the Goods Receipt Order screen, make the following entries and choose Enter:Goods Receipt: <Select>Purchase Order: <Select>Order number: <Purchase Order number>GR goods receipt: 101 | The items of the selected Purchase Order display. |  |
| 4 | Choose the Quantity tab and confirm the quantity | Confirm the quantity. |  |  |
| 5 | Select Item OK Indicator | Select the Item OK checkbox. |  |  |
| 6 | Post | Choose Post. | The system displays the message:Material Document <Document No> posted. |  |

#### Create Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform the invoice verification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Accounts Payable Accountant role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Supplier Invoice (F0859). | The New Supplier Invoices screen is displayed. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Reference: <xxx> (reference invoice number from invoicing party)Gross Invoice Amount : <XXX>Currency: AEDInvoice Date: <Today>Posting Date: <Today>Invoice Party: 33300007 | The New Supplier Invoices screen displays. |  |
| 4 | Enter Purchase Order References | In Purchasing Document References, make the following entries (use a PO you created previously) and choose Enter.Reference Document Category: Purchase Order/ Scheduling AgreementPurchase Order/Scheduling Agreement: <PO number> | The Purchase Document References screen displays. |  |
| 5 | Select Purchase Order Items | Check the selection of the Purchase Order Items.Confirm the warning messages. | All items of the selected Purchase Order are added to the Purchase Order Item table.You should see material items and delivery costs items which refer to the entered purchase order document. |  |
| 6 | Check the Invoice Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Purchase Order Item's table displays. |  |
| 7 | Check Tax code | In the section Tax check if there is tax code information. | In the Tax tab, you should see the same tax codes as in the items.If there is no tax, specify the tax code <Input Tax Code>. |  |
| 8 | Check the balance | Calculate the tax amount from the item amount multiplied by the tax value. | The balance should be zero (or within the defined tolerance). |  |
| 9 | Simulate Supplier Invoice and Check Messages | Choose Simulate.If there are no differences(or if the value is within the defined tolerance), a new screen Simulation appears. You can check the simulation results in Simulation Overview and Simulation Details area.The Supplier Invoice is complete to post. Check the Gross Invoice Amount against the items plus tax amount (if tax code is,<Input Tax Code> you do not have any tax amount) | The supplier invoice is complete to post. |  |
| 10 | Post Invoice | Choose Post. | The invoice is posted. |  |

### Production of Finished Goods

#### Create Production Order for Finished Goods

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

Planned orders for assembly finished good ( or FG0611) is generated in the same way as for parts production.

Procedure

Access the transaction choosing one of the following navigation options:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments screen displays. |  |
| 3 | Check Default Area of Responsibility | Choose user icon and select APP Settings icon. In the MRP Settings dialog box, choose Area of Responsibility.Check if only the following entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status button to set the status for the above entry to AOR Is Assigned if not yet assigned.Choose AOR Status button to unassign the rest of other entries.Choose Back. |  |  |
| 4 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 5 | Search for Material | Enter the following data and choose Go:Material: FG0611Select the line item with your WBS ID (individual segment).Choose Manage Materials. | The Manage Material Coverage screen displays.Note that you select the right individual segment for the WBS ID. |  |
| 6 | Convert Planned Order to Production Order | Choose the material item and then choose the generated planned order on the right screen. Select Convert from the dropdown list under column Actions. Choose Convert. | A message displays: Production order XXXXXXXX was created. |  |

#### Material Staging for Final Assembly

Test Administration

Customer project: Please fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID |  | Testing Date |  |
| Tester Name |  | Duration |  |
| Business Role(s) |  | Responsibility | State the Service Provider, Customer or Joint Service Provider and Customer |

Purpose

This process step shows you how to stage materials for final assembly production.

|  |
| --- |
| Note If there is sufficient stock available in the production storage location, then no line items are generated. |

Prerequisite

Stock must be available.

| Test Step Number | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stage Materials for Production (MF60). | The Material Staging for Planned Orders screen displays. |  |
| 3 | Enter Details | Make the following entries and choose Execute.In the Staging Types section:SLoc Level: selectPlant: 3310Selection Horizon for Reqmts: date must be in the future - after scheduled start dateOn the Production/Process Orders tab:Order: Production Order Number for fin-ished Goods | The Pull List: Storage Location Level screen displays. |  |
| 4 | Choose Replenishment Elements | In the Total Reqmts table, select the line items and choose Replenishment Proposal on the top of the screen.Review staged quantities and choose Replenishment Elements. |  |  |
| 5 | Enter Replenishment Storage Location and Batch Number | At the bottom half of the split screen, in the RepLoc column of the Replen Element table, enter 331C for staged materials. |  |  |
| 6 | Stage and Save | Choose Stage and choose Save.Note Missing materials are transferred to the shop floor from the designated storage area.The shortage of raw material for final assembly production order is supplied with this step. | Material is staged for final assembly. |  |

#### Release Production Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

The production order created by the MRP controller is assigned a release date in accordance with the scheduling margin key.

Purpose

This process step shows you how to release production orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). | The Manage Production Orders screen displays. |  |
| 3 | Check Default Area of Responsibility (Supervisor) | In the Area of Responsibility dialog box, choose Production Supervisor.In the Area of Responsibility (Supervisor) dialog box, check whether this entry displays:Plant 1 AE (3310)MTO w/o VC Val. (YB9)Choose + to add it if not displayed; choose the Delete icon to remove the other entries. Choose OK. |  |  |
| 4 | Search for Production Order | On the Manage Production Orders screen, choose Adapt Filters to display more filter options.Choose More Filters, and select Material and Production Plant. Choose Go.Enter the following filter criteria to search for your production order and press Enter:Status: CreatedMaterial: FG0611Production Plant: 3310Choose the filtered production order entry. | The Material and Production Plants fields are added to the filter bar.Searched production order displays. |  |
| 5 | Release Production Order | Choose the production order you created previously.On the XXXXXXX (production order number) page, choose Release in the top right corner of the screen. | Order is released. |  |
| 6 | Check Item Serial Number | Select the production order in the Manage Production Orders (F2336) app. Choose Related Apps on the top right menu bar and in the pop-up menu, choose Change Production Orders.Once inside the production order, choose Menu > Header > Serial Numbers .Check and make necessary changes to the serial number(s) accordingly.Please make note of the serial number(s) for later processes. | Serial Number(s) noted down. |  |

|  |
| --- |
| Note Please execute the 'Analyze Event-Based Production Costs' step from the Event-Based Production Cost Posting (3F0) test script. This activity will allow you to analyze event-based order plan costs. You would be able to see detailed plan costs of selected order. Production order preliminary/plan costs is the valuation basis of special project stock in ETO scenario. |

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
| 4 | Picking | Select the relevant reservations RM0615andSG0612 and choose Picking. | A list of all the selected reservations displays. |  |
| 5 | Batch Determination | Choose Post to post the goods movements. |  |  |

#### Confirm Assembly Activities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents the processing status of orders, operations, sub operations, and individual capacities. It is an instrument for controlling orders. This scope item uses time event confirmation. This process step shows you how to confirm assembly activities.

|  |
| --- |
| Note In practice, some operations produce scrap due to operational or component defects. To simulate this process, refer to Rework Processing – Work-in-Process (BJQ) scope item and perform steps described in the related test scripts. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). | The Perform Work screen displays. |  |
| 3 | Enter Production Order and Operation | On the Enter Order and Operation screen, make the following entries and press Enter:Order: <Production Order Number>Operation: <Operation Number>, for example, <0010> |  |  |
| 4 | Enter Quantities Data | In the Quantities section, make the following entries:Yield: <Yield Amount>Scrap: <Scrap Amount> |  |  |
| 5 | Check Material Movements | In the Material Movements section, check the material list. | The system displays an overview table of all materials for which the withdrawing is automatically done with the confirmation of the operation.If there are not any materials set for backflush (in material master), then no materials display in the table. |  |
| 6 | Enter Activities Data | In the Activities section, make the following entries:Setup: <Setup Time>Machine: <Machine Time>Labor: <Labor Time> |  |  |
| 7 | Save your Entries | For partial confirmation, choose Post.For final confirmation for this operation, choose Post and Complete. | Confirmation is made. |  |
| 8 | Repeat Steps | Go back and repeat steps 3-7 for Operation <0020> and <0030>. |  |  |

#### Analyze Event-Based Work in Process (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the report to review event-based WIP, this step is executed for partially confirmed or partial delivered production orders.

Procedure

To execute this activity, execute the Analyze Event-Based Work in Process step from the Event-Based Production Cost Posting (3F0) test script.

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

#### Analyze Event-Based Production Variances (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the report to review event-based production variances, this step is executed for final delivered or technical completed production orders.

Procedure

To execute this activity, execute the Analyze Event-Based Order Costs step from the Event-Based Production Cost Posting (3F0) test script.

#### Monitor Projects via Project Cost Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, analyze the cost structure of your project and check planned cost.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller . |  |  |
| 2 | Access App | Open the Project Cost Report - Plan/Actual (F2513) app. | The Project Cost screen displays. |  |
| 3 | Enter Selection Criteria | In the Standard section, make the following entries, and choose Go.Project: <Refer to the project created in [Create Project](#unique_20)>Planning Category 1: PlanPlanning Category 2: CPM BaselineR.000001 (for Revenue Project) | Project stock is increased and actual costs related to production orders is reduced by each goods receipts of production order.At the final goods receipt, Project stock is increased and the total production variances is posted to financial accounting as well on project (WBS element). |  |
| 4 | Navigation to Project Cost Report - Line items; view details of different cost | Select the project in the table, and choose View Details.On the Project Costs - line items screen, check financials using the drill-down and filter options. | Plan and Actual costs are displayed. |  |

### Bundle Spare Parts Through Production Order

#### Create Production Order for Spare Parts Bundle

Test Administration

Customer project: Please fill in the project-specific parts, as below.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | X.XX | Testing Date |  |
| Tester Name |  | Duration |  |
| Business Role(s) |  | Responsibility | State the Service Provider, Customer or Joint Service Provider and Customer |

Purpose

This process step shows you how to create production order without external processing operation.

Prerequisite

Planned orders for assembly finished goods (FG0612) are generated in the same way as for parts production.

Procedure

Access the transaction choosing one of the following navigation options:

| Test Step Number | Test Step Name | Instruction | Expected Result | Pass/Fail Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad dis-plays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments screen displays. |  |
| 3 | Check Default Area of Responsibility | Choose user icon and choose the MRP Settings icon. In the MRP Settings dialog box, choose Area of ResponsibilityCheck if only the following entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. |  |  |
| 4 | Search for Material | Enter the following data and choose Go:Material:FG0612Select the line item with your sales quotation / sales order number, such as CustSt - 10.Choose Manage Materials in the lower right corner of the screen. | The Material screen and Material Details screen display.Note that you select the right individual segment for the customer order. |  |
| 5 | Convert Planned Order to Production Order | Find the generated planned order. Select Convert from the Action dropdown list. Choose Convert, and choose OK. | A message displays: production order has been created. |  |

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
| 3 | Enter Details | Make the following entries and choose Execute.In the Staging Types section:SLoc Level: <select>Plant:3310Selection Horizon for Reqmts: <date must be in the future - after scheduled start date>On the Production/Process Orders tab:Order: <Production Order Number for > | The Pull List: Storage Location Level screen displays. |  |
| 4 | Choose Replenishment Elements | In the Total Reqmts table, select the line items and choose Replenishment Proposal on the top of the screen.Review staged quantities and choose Replenishment Elements. |  |  |
| 5 | Enter Replenishment Storage Location | At the bottom half of the split screen, in the RepLoc column of the Replen. Element table, enter 331C for staged materials. |  |  |
| 6 | Stage and Save | Choose Stage and choose Save.Note Missing materials are transferred to the shop floor from the designated storage area.The shortage of raw material for final assembly production order is supplied with this step. | Material is staged for final assembly. |  |

#### Release Production Orders

Test Administration

Customer project: Please fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID |  | Testing Date |  |
| Tester Name |  | Duration |  |
| Business Role(s) |  | Responsibility | State the Service Provider, Customer or Joint Service Provider and Customer |

Prerequisite

The production order created by the MRP controller is assigned a release date in accordance with the scheduling margin key.

Purpose

This process step shows you how to release production orders.

Procedure

| Test Step Number | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log On Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). | The Manage Production Orders screen displays. |  |
| 3 | Check Default Area of Responsibility (Supervisor) | In the Area of Responsibility dialog box, choose Production Supervisor.In the Area of Responsibility (Supervisor) dialog box, check whether this entry displays:Plant 1 AE(3310)ETO w/o VC Val. (YB9)Choose + to add it if not displayed; choose the Delete icon to remove the other entries. Choose OK. |  |  |
| 4 | Search for Production Order | On the Manage Production Orders screen, choose Adapt Filters to display more filter options.Choose More Filters, and select Material and Production Plant. Choose Go.Enter the following filter criteria to search for your production order and press Enter:Status: CreatedMaterial:FG0612Production Plant: 3310Choose the filtered production order entry. | The Material and Production Plant fields are added to the filter bar.Searched production order displays. |  |
| 5 | Release Production Order | Choose the production order you created previously.On the production order number page, choose Release in the top right corner of the screen. | Order is released. |  |

|  |
| --- |
| Note Please execute the 'Analyze Event-Based Production Costs' step from the Event-Based Production Cost Posting (3F0) test script. This activity will allow you to analyze event-based order plan costs. You would be able to see detailed plan costs of selected order. Production order preliminary/plan costs is the valuation basis of special project stock in ETO scenario. |

#### Confirm Assembly Activities

Test Administration

Customer project: Please fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID |  | Testing Date |  |
| Tester Name |  | Duration |  |
| Business Role(s) |  | Responsibility | State the Service Provider, Customer or Joint Service Provider and Customer |

Purpose

The confirmation documents the processing status of orders, operations, sub operations, and individual capacities. It is an instrument for controlling orders. This scope item uses time event confirmation. This process step shows you how to confirm assembly activities.

|  |
| --- |
| Note In practice, some operations produce scrap due to operational or component defects. To simulate this process, refer to Rework Processing - Work-in-Process (BJQ) scope item and perform steps described in the related test scripts. |

Procedure

| Test Step Number | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). | The Perform Work screen displays. |  |
| 3 | Enter Production Order and Operation | On the Enter Order and Operation screen, make the following entries and press Enter:Order: Production Order NumberOperation: Operation Number, for example, 0010 |  |  |
| 4 | Enter Quantities Data | In the Quantities section, make the following entries:Yield: Yield AmountScrap: Scrap Amount |  |  |
| 5 | Check Material Movements | In the Material Movements section, check the material list. | The system displays an overview table of all mate-rials for which the withdrawing is automatically done with the confirmation of the operation. If there are not any materials set for backflush (in material master), then no materials display in the table. |  |
| 6 | Enter Activities Data | In the Activities section, make the following entries:Setup: Setup TimeMachine: Machine TimeLabor: Labor Time |  |  |
| 7 | Save your Entries | For partial confirmation, choose Post.For final confirmation for this operation, choose Post and Complete. | Confirmation is made. |  |

#### Analyze Event-Based Work in Process (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the report to review event-based WIP, this step is executed for partially confirmed or partial delivered production orders.

Procedure

To execute this activity, execute the Analyze Event-Based Work in Process step from the Event-Based Production Cost Posting (3F0) test script.

#### Post Goods Receipt for Production Order

Test Administration

Customer project: Please fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID |  | Testing Date |  |
| Tester Name |  | Duration |  |
| Business Role(s) |  | Responsibility | State the Service Provider, Customer or Joint Service Provider and Customer |

Purpose

This process step shows you how to post the goods receipt for the production order.

Table 1:

| Test Step Number | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Post Goods Receipt for Production Order app (F3110). | The Post Goods Receipt for Production Order screen displays |  |
| 3 | Enter Order Number | Make the following entry and press Enter:Order: Production Order Number Created Previously |  |  |
| 4 | Check and Post | In the Items section, select the item and choose Post.The Success dialog box displays with the following mes-sage: 1 material document(s)posted:Choose OK. | Goods receipt for production order has been posted. |  |

#### Analyze Event-Based Production Variances (Optional)

Test Administration

Customer project: Please fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID |  | Testing Date |  |
| Tester Name |  | Duration |  |
| Business Role(s) |  | Responsibility | State the Service Provider, Customer or Joint Service Provider and Customer |

Purpose

In this activity, you run the report to review event-based production variances, this step is executed for Final Delivered or Technical Completed production orders.

Procedure

To execute this activity, execute the Analyze Event-Based Order Costs step from the Event-Based Production Cost Posting (‏3F0‏) test script.

### Create Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a delivery.

Prerequisite

The goods receipt was posted to the individual customer’s stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries - From Sales Orders (F0869A) screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: <shipping point> for example, 3310Planned Creation Date: <Delivery selection date>Order: <Sales order number created previously> |  |  |
| 4 | Create Delivery | Select your sales order and choose Create Deliveries. | A delivery is triggered to be created. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays, delivery is created successfully with delivery number shown on tab Deliveries. |  |

|  |
| --- |
| Note With app Analyze Delivery Logs (F0870A), you can display an overview about the logs of all delivery creation in system. You can search for logs according to different filter criteria, for example: created by and additional settings. Detailed log information is listed via selecting the arrow on the right of each delivery log entry:If delivery is created successfully, delivery number is shown on tab Deliveries, else, you can display the exact message type, text and also the related sales document on tab Messages. |

### Execute Picking

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
| 4 | Enter Shipping Point | Make the following entries, and choose Execute:Shipping Point: 3310Under the Picking Data tab, selectOnly Picking Without WM: X |  |  |
| 5 | Change Outbound Deliveries | From Day’s Workload for Picking, select your delivery number, and choose Change Outbound Deliveries. |  |  |
| 6 | Check Batch Split | Choose the Picking tab, check if batch split exists in the Batch Split Indicator column. |  |  |
| 7 | Enter Picked Quantity | If batch spilt exists, choose Batch Split Exists to expand sub item(s), enter <quantity equal to delivery Qty> in Picked Qty field for sub item.Note Sales BOM sub item materials are not relevant for the logistics process i.e. batch or picking quantity update.If batch split doesn't exist, enter <quantity equal to delivery Qty> in Picked Qty field for picking related item(s). |  |  |
| 8 | Choose Enter | Choose Enter. |  |  |
| 9 | Save | Choose Save. | The delivery has been decided. |  |

### Post Goods Issue

Test Administration

Customer project: Please fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID |  | Testing Date |  |
| Tester Name |  | Duration |  |
| Business Role(s) |  | Responsibility | State the Service Provider, Customer or Joint Service Provider and Customer |

Purpose

This process step shows you how to post goods issues for delivery.

| Test Step Number | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open the app Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue.Make the following entries and choose ExecuteShipping Point: 3310 |  |  |
| 4 | Post Good Issue | Select your outbound delivery and choose Post Goods Issues.Select today’s date from the dialog box, and choose Continue. | A message confirms the goods issue has been posted. |  |

|  |
| --- |
| Note Please note that material FG0611 is serial number managed. You need to maintain the serial number for the item manually in the outbound delivery. Otherwise, the goods issue will not be posted, and there will be errors. |

Financial Posting

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 51600000Consptn Trde Gds | 13600000Inventory TradingGd | None |

|  |
| --- |
| Note When the bundling functionality in context of IFRS15 is tested, the financial document in IFRS ledger (Ledger Group 2L) with the adjusted revenue amount displays.To check the financial document, use the Warehouse Clerk role, and access the Display Material Document List app (MB51). |

Printing Form

| Test Step Number | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery (VL03N) screen displays. |  |
| 3 | Issue Delivery Output | In the Outbound Delivery field, enter Outbound Delivery Number, and choose Continue.On the Delivery Display: Overview screen, choose Menu > Extras > Delivery Output > Output Control . | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery Note, and choose Display PDF Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

### Check Event Based Revenue Recognition – Project Accounted Sales

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you the profitability and the recognized revenue for the project after billing the sales order item.

Procedure

To execute this activity, execute the following steps from the 4GQ- Event-Based Revenue Recognition – Project-Based Sales test script:

1. Monitor Revenue Recognition (Event-Based): Projects
2. Run Revenue Recognition: Projects
3. Project Actual Data Reporting

|  |
| --- |
| Note In order to check the revenue recorded on the project, maintain the details as follows while executing the above mentioned steps:Fiscal Year Period: <enter a period in the PPP/YYYY format>Ledger: 0LCompany Code: 3310Project Definition: <R.000001> |

|  |
| --- |
| Note If there are issues identified in the Manage Real-Time Revenue Recognition Issues (F4101) app, please align with your finance team on resolving or skipping these errors. You cannot run Revenue Recognition with errors. |

### Change Sales Orders (Remove Billing Block)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to remove a billing block from a sales order.

This step is needed when including the down payment process.

Prerequisite

COGS has been recognized. To recognize revenue in the same month to keep FI and PA in synch, the billing block must be removed manually to process the final invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Search For Sales Order | Enter search term(s) in filter bar, and choose Go:Sales Order: <Sales Order Number> | Sales order is displayed in result list. |  |
| 4 | Navigate to Sales Order Screen | Select sales order number and choose Changes Sales Orders. | Sales order is displayed in result list. |  |
| 5 | Choose Billing Plan | Select the line item. From the menu, choose Menu > Goto > Item > Billing Plan .Note Alternatively, If you assign billing plan on header level: Choose Menu > Goto > Header > Billing Plan . Removal of billing block on header level also unlocks items automatically. | The Change Standard Order xxx: Item Data screen displays. |  |
| 6 | Delete Billing Block | In the Dates section, in the Block column, delete the billing block for the Final Invoice item. |  |  |
| 7 | Back | Choose Back. |  |  |
| 8 | Save | Save your entries. | The billing block is removed. |  |

### Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to bill a customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01) under Sales - Billing Document. | The Create Billing Document screen displays. |  |
| 3 | Search for Billing List | In the search condition, enter criteria if necessary. | SD document(s) displays in the result. |  |
| 4 | Choose Sales Document | Select the row of SD Document created previously and choose Create Billing Documents. |  |  |
| 5 | Maintain Billing Type and Billing Date | Choose billing type F2 Invoice (F2) and maintain Billing Date, for example, <current date>, then choose OK. | Prepaid down payment is displayed as a separate item in the final invoice document. |  |
| 6 | Save Billing Document | On the Billing Document screen, choose Save. The draft billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | Billing document is generated. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 12100000 Rcvbls Domestic21190000 Down Payments - Customers22000000 Output tax (MWS) | 41000000 Rev Domestic Prod12100000 Rcvbls Domestic21191500 Tax sett.dwn pmt cus22000000 Output tax (MWS) | none |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797) under Sales - Billing Document | The screen Manage Billing Document displays. |  |
| 2 | Search the Billing Document | Enter the billing document number recorded previously choose Enter. | The billing document which is created previously displays. |  |
| 3 | Display the Billing Document | Select the billing document item, and choose Display. | The billing document screen displays. |  |
| 4 | Check Output Condition | On the Billing Document screen go to the last assignment block, Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | On the Billing Document screen, select certain Billing document and choose Cancel billing Document. | There is a log displayed, Billing Document Canceled. |  |
| 7 | Update New Attachment (Optional) | In the Edit mode, add, delete and update the attachments. Save your changes by pressing Save in the footer bar. |  |  |
| 8 | Update New Text (Optional) | In the Edit mode, you can add, delete and update the texts. Save your changes by pressing Save in the footer bar. |  |  |

### Clear Down Payment (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note You can use the app Manage Customer Line Items and search against your WBS for any down payments which have still not been cleared. |

Purpose

In this process step, the down payment is moved to the Items to Be Cleared section and the balance is set to zero.

This process step is mandatory if the [Post Down Payment (Optional)](#unique_37) [page ] 71 process step is executed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Clear Incoming Payments - Manual Clearing (F0773). |  |  |
| 3 | Enter Customer Information | Choose the Clear Open Items button.Make the following entries and choose OK:Customer: 33100004Company Code: 3310 | A list of open payments still to be cleared is displayed. |  |
| 4 | Select More | To display open Items and special G/L transactions, choose Select More (…) button, and choose:Line Item Type: Normal Open Items and special G/L Transactions | Normal open Items and special G/L transactions are displayed in Open Items section. |  |
| 5 | Down Payment | Note Only execute this step if you are clearing an open item (invoice) against a down payment.In section Open Items, select the invoice where you applied the incoming payment in step Post Incoming Payment and also choose the down payment posted in step Post Down Payment by clicking the Clear button in the last column of each Journal entry.Skip next test step and continue to test step Simulate (Optional) or Post. | When the invoice is chosen, the assigned incoming payment is also selected. In the Items to Be Cleared section, the balance of the open item (invoice) displays.The down payment is moved to the Items to Be Cleared section. The balance becomes zero. Verify at the top of the view. |  |
| 6 | Open Item Selection | Note Skip this test step if you executed previous test step Down PaymentIn the Open Items section, choose items to clear by clicking the Clear button in the last column.Note The sum of the chosen open items to be cleared must be zero, check that the Balance is zero (top right) so the posting can occur. | The item to be cleared is transferred to the Items To be Cleared section on the right of the view. |  |
| 7 | Simulate (Optional) | Before posting, there is the option of simulating the posting. | A view showing the posting to be created when the document is posted displays. |  |
| 8 | Post | Choose the Post button at the bottom of the view. | The system displays Success and also displays the document number, company code, and year created with option buttons to Display or go to the Payment List. |  |

### Check Event Based Revenue Recognition – Project Accounted Sales (Optional)

Test Administration

Customer project: Please fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID |  | Testing Date |  |
| Tester Name |  | Duration |  |
| Business Role(s) |  | Responsibility | State the Service Provider, Customer or Joint Service Provider and Customer |

Purpose

This process step shows you the profitability and the recognized revenue for the project at the time of posting goods issue for deliveries from the sales order item.

Procedure

To execute this activity, execute the following steps from the 4GQ - Event-Based Revenue Recognition – Project-Based Sales test script:

- Monitor Revenue Recognition (Event-Based): Projects
- Run Revenue Recognition: Projects

In order to check the revenue recorded on the project, maintain the details as follows while executing the above mentioned steps:

- Fiscal Year Period: <Enter a period in the PPP/YYYY format>
- Ledger: 0L
- Company Code: 3310
- Project Definition: R.000001

### Accounts Receivable Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure guides you through the accounts receivable overview. In this activity, you review an overview of relevant figures and statistics related to the accounts receivable process. The Accounts Receivable Overview (F3242) app offers a central point of entry and an overview of the department.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager.Note Once you log on, you can customize fields to be displayed by default. To do so, choose User > Settings > Default Values , then add the Display Currency, Company Code, and Supplier fields. Save your changes. |  |  |
| 2 | Access the SAP Fiori App | Open Accounts Receivable Overview (F3242). |  |  |
| 3 | Edit Criteria | Make the following entries and choose Go:Display Currency: AEDNote You can change the currency If needed.Net Due Interval 1: for example, 30Net Due Interval 2: for example, 60Net Due Interval 3: for example, 90Company Code: <any> | Relevant figures and statistics display in the lower part of the screen.Some of the cards displayed are:Quick LinksAR Aging AnalysisMy InboxDays Sales OutstandingCash Collection TrackerAR BreakdownTop 10 Debtors |  |
| 4 | Navigate to Options | There are different, available options for reviewing figures and statistics.You can change the global filters if needed. The visible cards can be customized.Each card mentioned in the prior step provides you with functions to view and manage various accounts payable functions and information | Figures and statistics display according to available options. |  |

### Post Incoming Payments

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

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post Incoming Payments (F1345).Note For some countries/regions, if withholding tax is to be posted during payment, use the Post Incoming Payments for Japan - For Customers (FBZ1) app. | The Post Incoming Payments view displays. |  |
| 3 | Enter General Information | Make the following entries in the General Information area:Company Code : 3310Posting date : dateJournal Entry date : dateValue date : today’s dateJournal Entry Type : DZ (Customer Payment) |  |  |
| 4 | Enter Bank Data | Make the following entries in the Bank data area.G/L Account: 11001060House Bank/Account ID : AEBK1/AEAC1Amount : customer invoice amountNote If the incoming payment is part of a down payment, enter the remainder invoice balance amount, which is the invoice value less the down payment amount to be applied.Currency : AED |  |  |
| 5 | Enter Open Items | Make the following entries:Customer Account : 33100004Choose the Propose Items button. | The open items are displayed in the bottom half of the view. |  |
| 6 | Clear Items | Choose Items to Clear by choosing the Clear button in last item column. | The selected item is transferred to view Items to be Cleared. |  |
| 7 | Down Payment | Note Only execute this step if the payment is for an invoice where a down payment is applied.In the Items to Be Cleared column, Allocated Amount, enter the remainder invoice balance amount, which is the invoice value less the down payment amount to be applied.Choose Enter. | The balance is zero and the document can be posted. |  |
| 8 | Post Entries | Choose Post. | The Activated dialog box displays details of document number generated. |  |
| 9 | Post on Account | Repeat steps 1–4. |  |  |
| 10 | Enter Data | Choose Post on account and enter the following:Account Type: CustomerCustomer: 33100004Credit Amount : same amount as in step 4. |  |  |
| 11 | Save | Choose Post. | Document is posted. |  |

### Time Recording

Purpose

In this activity, employee enters the time recording for WBS Element using Manage My Timesheet (F1823) application.

Procedure

To execute this activity, you must execute the procedure in the following sub-step (which is from the Time Recording (1Q4) test script) using the WBS Element from this document: Record Actual Working Time.

|  |
| --- |
| NoteUse the user role Employee to perform time recording. While creating the task, maintain the Activity Type as 8 and use the WBS element created in the [Create Project](#unique_20) step of this test script.You can maintain the cost rate for the combination of activity type, company code and cost center using the app Manage Cost Rates - Services (F3161). This app can be accessed using the role Cost Accountant - Overhead. The cost rate must be maintained before time recording.To find the cost center for the user Employee, login with the user role Employee and select Employee-Workforce(Deprecated) in the top Search In dropdown of the search bar. Search for the user Employee. Expand the user Employee to see detailed information including the Cost Center. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| WBS Element | <Subordinate WBS Element 3>Note Use the value of the Subordinate WBS Element 3 for time recording. | <WBS for project execution> |  |

#### Record Actual Working Time

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you perform the time recording process through the Manage My Timesheet (F1823) app.

Working time is entered directly by the employee and not with delegates. Besides the times, a short description or note can also be entered per day and tasks.

|  |
| --- |
| Note Cost rates are maintained for the following combination: Sender Cost Center 33101101 and Activity Type 8. Make sure the Sender Cost Center 33101101 is assigned to the user for who the timesheet is to be recorded. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to the SAP Fiori launchpad as the user for whom timesheet is to be recorded. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open the Manage My Timesheet (F1823) app. | The My Timesheet Overview screen displays.Non-project related task types, which are non-billable, are automatically prefilled in the My Tasks list for employees.The Self Service Configuration UI can be used to define non-project related task types.To employee who has multiple employments, the tasks within his active employment will be shown. In case there are multiple active employments, you can find Employment information in upper left. By pressing the employment link, a pop up screen Select Employment comes out for you to select the right employment for time recording. |  |
| 3 | Select Date Range | By default, the timesheet shows the current week.If you want to record times in a different week, select the date range line on the top of the screen under My Timesheet. | A calendar entry dialog box displays allowing you to choose the week you wish to display.The weekend days (Saturday and Sunday are shown in a different color).The Calendar Settings button allows you to set:Show Work Week Specify Task Types : Yes or No (if not, Saturday and Sunday are shown)Start Week From: (for example, Monday)Time Format : Clock notation (for example, 12:30) or Decimal notation (for example, 12.5) |  |
| 4 | Manage my tasks | In the right part of the screen, choose the Menu button, then open the list item Manage My Tasks. | My task list displays. |  |
| 5 | Create a task | In the lower right-hand corner, choose the Create Task button. | The New Task window displays. |  |
| 6 | Choose Accounting objects | Choose Accounting objects (for example: Receiver Cost Center Receiver Cost center 33101601 and an Activity Type (for example, 8 - Consulting ), then click Save.Note Activity type is mandatory for recording on cost centers, internal orders, and WBS element.A combination of different accounting objects is not possible. The timesheet app allows you to record time for the following accounting objects:- WBS Element: Maintain WBS Element and Activity Type to record time for the WBS Element.- Receiver Cost Center: Maintain Receiver Cost Center and Activity Type to record time for the Receiver Cost Center.- Internal Order: Maintain Internal Order and Activity Type to record time for the Internal Order. | The possible receivers can be defined using the Self Service Configuration UI Maintain Data Entry Profiles. |  |
| 7 | Record Working Time – create new time entry | Enter the working times per days, hours, and tasks.Choose a task from the list of the available tasks. To enter the working times, click on the number of hours you want to record.For example, if you want to record 5 hours, choose the cell just below the number 5 on the day on which you want to record the hours.Save your entry. | The new time entries are visualized on the days you have chosen as rectangular boxes.The height of each box fits the number of hours you have inserted.Each entry shows the task title descriptions and the number of hours recorded in hh : mm format.On save, the records are automatically approved and transferred to CO.NoteThe HCM_CATS_V1_APPROVER_DETRMN (Timesheet Approver Determination) BAdI can be used to override the default approval process. .The HCM_CATS_V1_B_TS_VALIDATION (Timesheet Validation) BAdI can be used to provide checks before saving timesheet entries. |  |
| 8 | Record working time – Create additional time entries | Repeat the previous step for any additional time entry you want to record taking into account the already existing entries.Save your entry. | The times are saved. |  |
| 9 | Record Working Time – modify existing entries | Choose an existing entry, and in the Details dialog box, adapt the Duration field by inserting the number of hours in hh : mm format.Save your entry. | The height of the time entry is adapted according to the new recorded hours. |  |
| 10 | Record Working Time – delete existing entries | Choose the Delete button that is on the cross icon on the top-right corner of an entry.Save your entry. | The selected entry disappears. |  |
| 11 | Enter a Work Location and/or Note for an ac-tivity (optional) | To enter an optional Work Location and/or Note for an activity, just choose the entry and scroll down to find the Details screen. In Work Location field, Choose F4 to select a proper Work Location.Enter a description in the Note field and save.Note Field length in the Note field is restricted to 300 chars. | A dialog box is displayed. The Details of the activity is saved.The possible Work Locations are maintained in SSCUI Maintain Work Locations. |  |

### Complete Milestone

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Project Manager changes the status of the milestone to be approved based on the feedback received from the Project Steering Committee during the review meeting and sets the actual dates for the approved milestones.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager. |  |  |
| 2 | Access App | Open the My Projects - Project Manager (F1876) app. Go to Project Brief Overview using the card Upcoming Milestones - Active Projects. | The Project Overview screen appears and the list of projects is displayed. |  |
| 3 | Select Project in which Milestones are to be Approved | Select the project and click to navigate to the Project Brief screen. | Details of the selected project are displayed.Selected project opens and can be updated. |  |
| 4 | Choose Edit | Choose Edit to change the project from Display to Edit mode.Note By default, the project opens in the display mode. | Selected project opens in the edit mode. |  |
| 5 | Set Milestones Status to Approved | Set Milestone Approval Status to Approved. | Milestone Approval Status is added in the Milestone section. |  |
| 6 | Update the Actual Finish Date | Update the Actual Finish Date for the approved Milestones.Note Actual Date can be updated only for the released projects.Choose Save. | The Actual Finish date is updated. |  |

### Monitor Projects via Project Cost Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, analyze the cost structure of your project and check planned cost.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller . |  |  |
| 2 | Access App | Open the Project Cost Report - Plan/Actual (F2513) app. | The Project Cost screen displays. |  |
| 3 | Enter Selection Criteria | In the Standard section, make the following entries, and choose Go.Project: <Refer to the project created in [Create Project](#unique_20)>Planning Category 1: PlanPlanning Category 2: CPM BaselineR.000001 (for Revenue Project) | Details of the project structure and the corresponding planned, actual costs, project stock costs, and commitments are displayed. |  |
| 4 | Navigation to Project Cost Report - Line items; view details of different cost | Select the project in the table, and choose View Details.On the Project Costs - line items screen, check financials using the drill-down and filter options. | Plan and Actual costs are displayed. |  |

### Check Event Based Revenue Recognition – Project Accounted Sales

Test Administration

Customer project: Please fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID |  | Testing Date |  |
| Tester Name |  | Duration |  |
| Business Role(s) |  | Responsibility | State the Service Provider, Customer or Joint Service Provider and Customer |

Purpose

This process step shows you the profitability and the recognized revenue for the project at the time of posting goods issue for deliveries from the sales order item.

Procedure

To execute this activity, you must execute the procedures in the following sub-steps (which are from the Event-Based Revenue Recognition – Project-Based Sales (4GQ) test script):

|  |
| --- |
| Remember The Run Revenue Recognition - Projects (F4277) app must be executed for all ledgers (0L, 2L, and 3L). |

#### Monitor Revenue Recognition (Event-Based): Projects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Event-based revenue recognition calculates and posts real-time revenue and cost adjustment for professional service with sales order integration based on cost-based POC (default RA key EPMFC) or RA EPMCC-completed contract method.

Processes that don't write a general ledger entry don't result in any real-time revenue recognition postings. For example, changes of plan data don't directly result in revenue recognition postings. Period-end-closing postings (periodic revenue recognition) correct the event-based postings. After the period-end-closing, the posted values are correct and no separate settlement is required any longer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Event-Based Revenue Recognition - Projects (F4767). | The Revenue Recognition - (Event-Based) (2) - Projects view displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Company Code: 3310Project Definition: R.000001 | Your project revenue recognition details are shown. |  |
| 4 | Review Detail | Select your billing element and choose the Details button. | The project detail is now shown for the current period and includes details such as project status and periodic view/charts.Note To view a different period, choose the Set Parameters tab and change to another To Period value. |  |

#### Run Revenue Recognition: Projects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the event-based revenue recognition for projects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Run Revenue Recognition - Projects (F4277). | The New Job: Run Revenue Recognition - Projects view displays. |  |
| 3 | New Job | Choose the Create button. | The New Job view displays. |  |
| 4 | Enter Selection Criteria | Make the following entries and choose the Schedule button:Job Template: Run Revenue Recognition – ProjectsJob Name: <Enter a description or leave the default description>Choose Step 2.Start Immediately: <checked>Choose Step 3. Select the Fixed Period or Dynamic Period. If you select the dynamic period, in To Dynamic Fiscal Period/Year, use the dropdown to select, for example, Current Fiscal Period.Company Code: 3310Ledger: 0LRemember The Run Revenue Recognition - Projects (F4277) app must be executed for all ledgers (0L, 2L, and 3L). | The new job is executed. |  |

### Close Project

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
| Note All the pending down payments should be cleared before you proceed with the project closure. You can use the app Manage Customer Line Items and search for your WBS.A detailed process on clearing down payments is explained in the Accounts Receivable (J59) test script.. |

In this activity, you close the completed project, that is, you set the project processing status to Closed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open the Project Control - Enterprise Projects (F3215) app. | The Project Control screen displays. |  |
| 3 | Open Project | In the Standard section, make the following entries, and choose Go.Project: <Refer to the project created in the [Create Project](#unique_20) test procedure.> | At least one entry is displayed in the Worklist area. |  |
| 4 | Close project and structure | Select the Project and in the header section, choose Processing Status > Complete . Then, choose Processing Status > Close . | The project is saved with the processing status Closed. |  |

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
> Flagged while digesting this document, not verified: Approve Purchase Order step in the long lead components section states approval is needed for purchase group 003 and PO > 500 AED, while the same step elsewhere and the workflow configuration use purchase group 001.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Re-upload of planned costs sample template uses company code 1010 while the initial upload and the rest of the script use company code 3310.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Approval step references app My Inbox - All Items as F5331 in the first procurement block but F0862 in later blocks.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Document says Business Role 'Project Manager - Commercial Services' in the overview table while the Roles section lists Project Manager (SAP_BR_PROJECTMANAGER).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Release Production Order step lists area of responsibility 'MTO w/o VC Val. (YB9)' for FG0611 but 'ETO w/o VC Val. (YB9)' for FG0612 with the same code YB9.

## Connections
- part-of :: [[_cluster]]
- see-also :: [[12-production-and-manufacturing/test-script-engineer-to-order-production-with-variant-configuration-4r]]
- see-also :: [[14-maintenance-service-and-projects/project-billing-project-based-services-4e9-ae-test-script-1021]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6GD_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 237,170 chars in the whole document
