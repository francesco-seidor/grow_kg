---
id: 12-production-and-manufacturing/make-to-order-production-semifinished-goods-planning-and-assembly-1bm
title: Make-to-Order Production – Semifinished Goods Planning and Assembly (1BM_AE) Test Script (1BM_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1BM_AE: MTO semifinished goods planning via PIRs, MRP, production orders and sales order consumption (plant 3310)."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/make-to-order-semifinished-planning]
aliases: [1BM_S4CLD2608_BPD_EN_AE]
keywords: [Make-to-Order with Semi-Finished Goods Planning, make-to-order production, planned independent requirements, material requirements planning, material coverage monitoring, production order processing, production order output, production order confirmation, sales order processing, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1BM_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-710
topic: 12-production-and-manufacturing/make-to-order-semifinished-planning
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Make-to-Order Production – Semifinished Goods Planning and Assembly (1BM_AE) Test Script (1BM_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1BM_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Make-to-Order with Semi-Finished Goods Planning** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Make-to-Order Production – Semifinished Goods Planning and Assembly (1BM_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232846643)

[2 Prerequisites 4](#_Toc232846644)

[2.1 System Access 4](#_Toc232846645)

[2.2 Roles 4](#_Toc232846646)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232846647)

[2.4 Business Conditions 8](#_Toc232846648)

[2.5 Preliminary Step 8](#_Toc232846649)

[2.5.1 Initial Material Stock 8](#_Toc232846650)

[2.5.2 Define Output Parameter Determination 9](#_Toc232846651)

[3 Overview Table 12](#_Toc232846652)

[4 Test Procedures 14](#_Toc232846653)

[4.1 Anonymous Forecast and Material Requirements Planning for Semifinished Product 14](#_Toc232846654)

[4.1.1 Create Planned Independent Requirements 14](#_Toc232846655)

[4.1.2 Material Requirements Planning 15](#_Toc232846656)

[4.1.3 Monitor Material Coverage 17](#_Toc232846657)

[4.2 Production Order Processing for Semifinished Product 18](#_Toc232846658)

[4.2.1 Create Production Order 18](#_Toc232846659)

[4.2.2 Release Production Order with Output Setting 19](#_Toc232846660)

[4.2.3 Preview Output Document for Production Order 21](#_Toc232846661)

[4.2.4 Confirm Production Order for Semifinished Product 22](#_Toc232846662)

[4.2.5 Review Production Order for Semifinished Product 24](#_Toc232846663)

[4.3 Sales Order Processing for Finished Products 26](#_Toc232846664)

[4.3.1 Alternative 1: Make-to-Order Production – Finished Goods Sales and Final Assembly(BJE) 26](#_Toc232846665)

[4.3.2 Alternative 2: Incoming Sales Order and Consumption of the Component 26](#_Toc232846666)

[4.3.2.1 Create Sales Order for Finished Product 26](#_Toc232846667)

[4.3.2.2 Monitor Material Coverage for Semifinished Product 27](#_Toc232846668)

[4.3.2.3 Material Requirements Planning for Finished Product 28](#_Toc232846669)

[4.3.2.4 Monitor Material Coverage for Semifinished and Finished Product 30](#_Toc232846670)

[4.4 Review Manufacturing Object Pages 31](#_Toc232846671)

[5 Appendix 33](#_Toc232846672)

[5.1 Process Integration 33](#_Toc232846673)

[5.1.1 Succeeding Processes 33](#_Toc232846674)

## Purpose

Overview

This scope item supports production planning for semifinished components within a Make-to-Order (MTO) environment before the receipt of incoming sales orders. This reduces the lead time of sales orders for finished goods received that are received later.

Demand forecast is created for semifinished components that are represented through planned independent requirements (PIRs). Based on PIRs, Material Requirements Planning (MRP) creates a production plan for the component and explodes the bill of material structure for higher low-level codes. As a result, the demand for semifinished component production and raw material is planned.

The production process is made up of the following: Conversion of planned orders to production orders, order release, confirmation of order operations with automatic backflush of components, and goods receipt posting.

The scenario is completed with the receipt of an incoming sales order and either the consumption of the component part of this scope item, or by reference to the entire MTO scenario in the BJE scope item.

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
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices Baseline package, you can use the following baseline package sample data:

Manufacturing

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | FG228 | FIN228,MTO,PD,Fifo |  |
| Material | SG21 | SG21 |  |
| Material | SG22 | SG22 |  |
| Material | SG25 | SG25 |  |
| Material | SG23 | SEMI23,PD,Subcontracting |  |
| Material | RM13 | RAW13,PD,Subcontracting |  |
| Material | RM14 | RAW14,PD,Subcontracting |  |
| Material | SG224 | SG224 |  |
| Material | RM16 | RM16 |  |
| Material | RM20 | RM20 |  |
| Material | RM27 | RM27 |  |
| Material | RM120 | RM120 |  |
| Material | RM122 | RM122 |  |
| Material | RM124 | RM124 |  |
| Material | RM128 | RM128 |  |
| Customer | 33100001 |  |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Shipping Point | 3310 |  |  |
| Sales Organization | 3310 |  |  |
| Distribution Channel | 10 |  |  |
| Division | 00 |  |  |

Bill of Material Structure

This overview shows the bill of material structure and the usage of each component if you have activated all optional enhancements.

| Material | Level | Material Type | Unit | Characteristic of Material | Optional Enhancements |
| --- | --- | --- | --- | --- | --- |
| FG228 | 0 | FERT | PC | Finished Good for MT0 processing |  |
| SG21 | 1 | SEMI | PC | SF Repetitive Manufacturing |  |
| RM12 | 2 | RAW | PC | External procured |  |
| SG22 | 1 | SEMI | PC | SF, Phantom Assembly |  |
| RM16 | 2 | RAW | PC | External procured |  |
| SG23 | 1 | SEMI | PC | External procured with subcontract |  |
| RM13 | 2 | RAW | PC | External procured |  |
| RM14 | 2 | RAW | PC | External procured |  |
| RM122 | 1 | RAW | PC | External procured with Batch Management (FIFO-Strategy) |  |
| RM128 | 1 | RAW | PC | External procured with Consignment Processing |  |
| RM13 | 2 | RAW | PC | External procured |  |
| RM14 | 2 | RAW | PC | External procured |  |
| SG224 | 1 | SEMI | PC | Internal production of subassembly (MTO strategy) |  |
| RM124 | 2 | RAW | PC | External procured using Fixed Bin |  |
| RM27 | 1 | RAW | PC | External procured, Packaging Box |  |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Master Data Script Text |
| --- | --- |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BLD | Create Production Version - MDS |

### Business Conditions

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Comment |
| --- | --- |
| BNU - Create Costing Run - MDS (master data script) | You have completed the steps described in the master data script BNU: Create Costing Run - MDS |

### Preliminary Step

#### Initial Material Stock

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Input Material | Make the following entries and press Enter:Material Master: RM124Plant: 3310 | The Stock overview for the material displays. |  |
| 4 | Select Stock | Select the icon beside the stock that you want to add initial stock, for example:Storage Location: 331BUnrestricted - Use Stock | A dialog box opens. The Storage Location, Stock Type, and Current Quantity display according to your entries in the previous steps. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Document Date: todayPosting Date: todayStock Change: Initial EntryQuantity: <quantity number> | The system displays the following message. The stock has been added.1 document has been created: Material Document XXXXXXXXXX/20XX |  |

#### Define Output Parameter Determination

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App (for Cloud system) | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). |  |  |
| 3 | Access the Customizing Path ( for the SAP S/4HANA Cloud Private Edition system) | For the SAP S/4HANA Cloud Private Edition system, access IMG activity IMG > Cross-Application Components > Output Control > Define Business Rules for Output Determination .Transaction Code: OPD. |  |  |
| 4 | Choose Show Rules For | In the Show Rules for field, select the triangle button and choose Manufacturing Order (Production Planning) in the dropdown list. |  |  |
| 5 | Choose the Determination Step and Maintain Table Contents | In the Determination Step field, select the triangle button.Choose Channel and add the following two entries in Table Contents.Entry one as below:Output type: PICK_LIST (Pick List)Channel: EMAIL (Email)Exclusive Indicator: - (false)Entry two as below:Output type: ORDER_DATA_LIST (Order Data List)Channel: EMAIL (Email)Exclusive Indicator: - (false)Choose Email Recipient and maintain the following two entries in Table Contents (Regarding default e-mail settings here, you can input your own data here).Entry one as below:Output type: PICK_LIST (Pick List)Email Type Code: TO (To)Email Address: <Your own Email address>, for example, [SET_Dummy@sap.com](mailto:SET_Dummy@sap.com).Entry two as below:Output type: ORDER_DATA_LIST (Order Data List)Email Type Code: TO (To)Email Address: <Your own Email address>, for example, [SET_Dummy@sap.com](mailto:SET_Dummy@sap.com).Choose Email Settings and maintain the following two entries in Table Contents.Entry one as below:Output type: PICK_LIST (Pick List)Sender Email: <Your own Email address>, for example, [SET_Dummy@sap.com](mailto:SET_Dummy@sap.com).Email Template: PP_MOR_PICK_LISTEntry two as below:Output type: ORDER_DATA_LIST (Order Data List)Sender Email: <Your own Email address>, for example, [SET_Dummy@sap.com](mailto:SET_Dummy@sap.com).Email Template: PP_MOR_DATA_LISTChoose Form Template, and maintain the following two entries in Table Contents.Entry one as below:Output type: PICK_LIST (Pick List)Channel: EMAIL (Email)Form Template: PP_MOR_PICK_LISTEntry two as below:Output type: ORDER_DATA_LIST (Order Data List)Channel: EMAIL (Email)Form Template: PP_MOR_DATA_LISTNote To maintain Table Contents.Choose Edit on Output Parameter Determination.Choose Insert New Row if a new row has to be added.Choose the triangle button on the field to be maintained.Choose Direct Value Input on the dropdown list.Input the value.Choose Activate, in the dialog box choose Yes to save. |  |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Anonymous Forecast and Material Requirements Planning for Semifinished Product |  |  |  |
| [Create Planned Independent Requirements](#unique_10) [page ] 14 | Production Planner | Maintain PIRs (F3445) | The Application Jobs screen displays. |
| [Material Requirements Planning](#unique_11) [page ] 15 | Production Planner | Schedule MRP Runs (F1339) | The Application Jobs screen displays. |
| [Monitor Material Coverage](#unique_12) [page ] 17 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | The Monitor Material Coverage - Net / Individual Segments (F2101A) Screen displays. |
| Production Order Processing for Semifinished Product |  |  |  |
| [Create Production Order](#unique_13) [page ] 18 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | The Monitor Material Coverage - Net / Individual Segments (F2101A) screen displays. |
| [Release Production Order with Output Setting](#unique_14) [page ] 19 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | The Manage Production Orders (F2336) screen displays. |
| [Preview Output Document for Production Order](#unique_15) [page ] 21 | Production Supervisor - Discrete Manufacturing | Change Production Order (CO02) |  |
| [Confirm Production Order for Semifinished Product](#unique_16) [page ] 22 | Production Operator - Discrete Manufacturing | Confirm Production Order Operation (CO11N) | The Perform Work screen displays. |
| [Review Production Order for Semifinished Product](#unique_17) [page ] 24 | Production Operator - Discrete Manufacturing | Manage Production Operations (F2335) | The Manage Production Operations (F2335) screen displays. |
| Sales Order Processing for Finished Products |  |  |  |
| [Alternative 1: Make-to-Order Production – Finished Goods Sales and Final Assembly(BJE)](#unique_18) [page ] 26 |  |  |  |
| Alternative 2: Incoming Sales Order and Consumption of the Component |  |  |  |
| [Create Sales Order for Finished Product](#unique_19) [page ] 26 | Internal Sales Representative | Manage Sales Orders (F1873) | The Manage Sales Orders (F1873) screen displays. |
| [Monitor Material Coverage for Semifinished Product](#unique_20) [page ] 27 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | The Monitor Material Coverage - Net / Individual Segments (F2101A) Screen displays. |
| [Material Requirements Planning for Finished Product](#unique_21) [page ] 28 | Production Planner | Schedule MRP Runs (F1339) | The Application Jobs screen displays. |
| [Monitor Material Coverage for Semifinished and Finished Product](#unique_22) [page ] 30 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | The Monitor Material Coverage - Net / Individual Segments (F2101A) displays. |
| [Review Manufacturing Object Pages](#unique_23) [page ] 31 | Any role for production listed in Roles chapter. | Search function | The list of search result displays. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Anonymous Forecast and Material Requirements Planning for Semifinished Product

#### Create Planned Independent Requirements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create Planned Independent Requirements (PIRs). PIRs are used to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, that is, one planned quantity split over time according to dates.

|  |
| --- |
| Note Instead of creating a single requirement, sometimes a requirement plan that includes one or more planned independent requirements can be maintained for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Monthly(M)Version Active: Select all optionsSearch: SG224 |  |  |
| 5 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 6 | Edit PIRs | Select the material item and choose Edit in the upper-right corner of the screen.On the screen, enter quantities per period, for example:PIR: 100 for all periodsMake sure the version is active.Version Active: Yes |  |  |
| 7 | Save PIRs Draft | Choose Save at bottom right. | The PIRs are saved. |  |

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
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirement Planning (MRP)Job Name: <MRP for SG224>Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.For 3 Parameters section:Plant: 3310Material: SG224Changed BOM Components: selectPlanning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for SG224 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

#### Monitor Material Coverage

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock and requirements situation for the semifinished product (SG224) in the stock and requirements list after the requirements planning performed.

Prerequisite

Requirements planning has been carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments (F2101A) Screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 4 | Select Material | In the search area, make the following entries and choose Go.Material: SG224Select the filtered rows and choose Manage Materials. | The Manage Material Coverage screen displays. |  |
| 5 | Review Stock and Requirements List | Choose the corresponding material in the Materials list on the left side. | The detailed Stock and Requirements List for each material displays. |  |
| 6 | Display Planned Order | From the left Materials list, choose the material for which you want to check the planned order.Material: SG224On the right screen, choose PldOrd XXXX in column MRP Element. | The Planned Order you selected displays in the dialog box.If there is no shortage for those materials, the planned order will not be generated.If you want to display more information about the planned order, at the bottom of this dialogue, choose Document Info . |  |
| 7 | Note | The BOM explosion during the MRP run has generated dependent requirements for the demand-driven planned components. If inventory does not cover the requirements, planned orders are created for in-house-produced materials or purchase requisitions for externally procured materials. |  |  |

### Production Order Processing for Semifinished Product

#### Create Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create production order. The MRP run creates planned orders that will be produced internally. When the planned opening date reaches, the planned orders are converted to production orders.

Prerequisite

The MRP run has generated a planned order for material SF Subassembly SG224.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage-Net / Individual Segments screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 4 | Select Material | In the search area, make the following entries and choose Go.Material: SG224Select the filtered rows and choose Manage Materials. | The Manage Material Coverage screen displays. |  |
| 5 | Find Planned Order | Find the generated planned order. | Order information displays. |  |
| 6 | Convert Planned Order to Production Order | Select Convert from the dropdown list of column Actions. Choose Convert to Production Order and confirm the date and quantity. Then choose Convert. | The production order is created. |  |

#### Release Production Order with Output Setting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to releases the order and all its operations at order header level . The order and the operations receive the status REL (released). You can also release a production order in create and change modes.

Prerequisite

The production order created by the MRP controller is assigned a release date in accordance with the scheduling margin key.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). | The Manage Production Orders (F2336) screen displays. |  |
| 3 | Check Default Area of Responsibility (Supervisor) | Choose the user icon and select App Settings. Choose tab Production Supervisors.In the AOR Status column, choose the button to assign or unassign entries, and make sure only the following entries are assigned:Plant 1 AE 3310MTS DI - Valuated (YB1)Choose Back. | If the Plant 1 AE 3310 is blank on the Area of Responsibility(Supervisor) screen, choose Add to select it and then choose OK.For other plant entries on the Area of Responsibility (Supervisor) screen, choose Delete to remove the others and then choose OK. |  |
| 4 | Select Production Order | On the Manage Production Orders (F2336) screen, enter the following search condition as filter.Choose Adapt Filters to display more selection filter. Select the checkbox for Material and Production Plant and choose Go. Choose OK. Material and Production Plant fields are then added to filter bar.Status: CreatedMaterial: SG224Production Plant: 3310Choose Go to execute. | The Manage Production Orders (F2336) screen displays. |  |
| 5 | Edit Production Order | On the Manage Production Orders (F2336) screen, select the searched order. Choose Edit in the top right corner. | The Production Order Change: Header screen displays. |  |
| 6 | Navigate to Output Management | Choose Menu > Order > Output > Manage Output Items . | The Overview Output Management: Output screen displays. |  |
| 7 | Check Default Output Settings | On the Overview Output Management: Output screen, you could check output item lists under Output section.Select the output item and choose Display Details.For items with PRINT Channel, you can check and make necessary changes to parameters under Channel Details: Print.Print Queue: <DEFAULT, or other valid Print Queue>For items with EMAIL Channel, you can check and make necessary changes to parameters under Channel Details: Email.Email Address: <a valid address which you can receive Emails> | Four items should be listed with default settings, with status of In Preparation:Output Type: PICK_LIST; Channel: PRINTOutput Type: PICK_LIST; Channel: EMAILOutput Type: ORDER_DATA_LIST; Channel: EMAILOutput Type: ORDER_DATA_LIST; Channel: PRINT |  |
| 8 | Preview the PDF Document | Select the output item and choose Display PDF Document.In the pop-up document, you could check the detailed information of the production order, for example, Order Type, Order Quantity and so on. |  |  |
| 9 | Execute Release | Go back to the Production Order Change: Header screen, select Release Order in the top left corner. |  |  |
| 10 | Save Production Order | Choose Save. |  |  |
| 11 | Check Output | Check output.For items with EMAIL Channel, you can check e-mail box which is specified as Email recipient.For items with PRINT Channel, you can check the printed file through Maintain Print Queues (F1260) app using Administrator role. | Note If there are no components to pick in the order, the output items with Output Type: PICK_LIST will not print, as no picklist is needed. |  |

#### Preview Output Document for Production Order

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Production Order (CO02) | The Production Order Change: Initial screen displays. |  |
| 3 | Enter Production Order Data | On the Change Production Order (CO02) screen, make the following entry and choose Continue:Order: <Production Order Number you noted> | The Production order Change: Header screen displays. |  |
| 4 | Navigate to Output Management | Select Menu > Order > Output > Manage Output Items | The Overview Output Management: Output screen displays. |  |
| 5 | Check Output Item | On the Overview Output Management: Output screen, you could check the status of output items under Output section. | The output item with Completed status means the item is successfully printed. |  |
| 6 | Adjust Production Order Qty (Optional) | Go back to Production Order Change: Header screen, make following entries and press Enter:Total Qty: <input a new value> |  |  |
| 7 | Navigate to Output Management (Optional) | Select Menu > Order > Output > Manage Output Items . |  |  |
| 8 | Add New Output Items (Optional) | On the Overview Output Management: Output screen, choose Add Output.You can refer to default output settings, and fill in necessary parameters for the newly created Output Item according to your printing requirement.Select the added item, and choose Display Details to fill in other mandatory fields.After you maintained the new output item, choose Send Output to print it. | You create and send new output items to reflect the modified production order.Note You can also regenerate all default output items by choosing Determine Items, and then make necessary changes. |  |
| 9 | Save Production Order (Optional) | Go back to the Production Order Change: Header screen, choose Save. | You should get new printout indicating new quantity (if any) for the production order. |  |

#### Confirm Production Order for Semifinished Product

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents include the processing status of orders, operations, suboperations. It is an instrument for controlling orders. Here you have to confirm the operations of the production order for semi-finished material SF Subassembly SG224. When you confirm the last operation, the system generates a goods movement document for SF Subassembly SG224. The backflush is carried out together with the confirmation steps. Via the confirmation the goods receipt for semifinished material SG224 will also be executed automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Order Operation (CO11N). | The Perform Work screen displays. |  |
| 3 | Enter Production Order and Operation | On the Perform Work screen, make the following entries and choose Enter:Order: <Production Order Number you noted>Operation: for example, 0010 |  |  |
| 4 | Enter Fields in Quantities Section | In the Quantities section, make the following entries:Yield: <enter the amount you want to Confirm>Scrap: <enter the amount you want to Scrap> |  |  |
| 5 | Check Material Movements | In the Material Movements section, check the material list. | The system shows an overview table of all materials for which the withdrawing is done automatically with the confirmation of the operation.The material RM124 is set for backflush (in material master) so that the withdrawing is done automatically after you confirm the operation. |  |
| 6 | Enter Fields in Activities Section | In the Activities section, make the following entries:Setup: <enter the setup time you want to confirm for this operation>Machine: <enter the machine time you want to confirm for this operation>Labor: <enter the labor time you want to confirm for this operation> |  |  |
| 7 | Save Your Entries | Select Post and Complete to make final confirmation for this operation. | Confirmation has been created. If you would like to make partial confirmation, you can choose Post. |  |
| 8 | Repeat Steps | Go back and repeat steps 3 to 7 for operation number 0020 and save your entries. |  |  |

#### Review Production Order for Semifinished Product

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display and check the order using the app Manage Production Operations (F2335) for the Semifinished Product SG224 after the release or confirm of finished goods orders is performed,

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Operations (F2335). | The Manage Production Operations screen displays. |  |
| 3 | Select Production Order | On the Manage Production Operations screen, enter the following search condition as filter.Choose the user icon and select App Settings. Choose against Area of Responsibility Production Supervisor. Check if only this entry is assigned:Plant 1 AE 3310MTS DI - Valuated (YB1)Choose Back.Choose Adapt Filters to display more selection filters. Select the checkbox for Material and Production Plant, and choose OK. The Material and Production Plant fields are then added to the filter bar.Status: ConfirmedMaterial: SG224Production Plant: 3310Choose Go to execute. | The selected order displays. |  |
| 4 | Check Detailed Operations Status | Check detailed information for selected production operations.Issue:Empty if there is no issue for production order.Delay / Missing Components / PRT issue / Quantity Deviation / Quality Issue information shows if relevant issue exists.Components:Material, total quantity and Issued / open quantity information for order components displaysOrder Schedule:Detailed operation information with relevant work center, confirmed quantity, start or end time displays.Work Center Schedule:The relevant order that covering the same work center capacity (operation is partially confirmed) displayed.Operations not Started:The relevant order that would cover the same work center capacity (operation is released) displayed.Confirmation:Detailed confirmation information with Yield, Scrap; Rework quantity displays if confirmation executed.Inspection:Detailed inspection lots information displays if existed | Detailed operations status displays. |  |

### Sales Order Processing for Finished Products

#### Alternative 1: Make-to-Order Production – Finished Goods Sales and Final Assembly(BJE)

You can execute the scope item BJE for completing process of sales and production for finished products FG228.

Procedure

Complete all the activities described in the test script of the scope item BJE (Make-to-Order Production – Finished Goods Sales and Final Assembly)

#### Alternative 2: Incoming Sales Order and Consumption of the Component

##### Create Sales Order for Finished Product

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order for material FG228 that customer requires.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | Choose Create. Select Create Sales Order – VA01 from the Action dropdown list. | The Create Sales Document screen displays. |  |
| 4 | Enter the Order Type OR (Standard Order) | On the Create Sales Document screen, make the following entries:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00Choose Continue. |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries:Sold to party: 33100001Ship-to party: 33100001Customer Reference: <PO number>Order Reason: <Order Reason>Req. Deliv. Date: <Current date + 2 days>Material Number: FG228Order Quantity: <Quantity> |  | PO Number: Enter a customer purchase order number as referenceOrder Reason: for example, Excellent priceQuantity: for example, 10 PC |
| 6 | Save Document | Choose Save.On the Information message choose Continue. On the Review Availability Check Result screen, check the confirmed delivery date and choose Apply.Make a note of the sales order number: __________. | Note If the sales order might require approval, please refer to scope item Sell from Stock (BD9), and complete the activities of Process Sales Order Approval. |  |

##### Monitor Material Coverage for Semifinished Product

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can note down the PIR of SG224 before MRP run. MRP generates dependent requirement for SG224 which consumes the PIR.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments (F2101A) screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 4 | Enter Relevant Search Criteria | In the search area, make the following entries and choose Go.Material : SG224Select the filtered rows and choose Manage Materials. | The Manage Material Coverage screen displays. |  |
| 5 | View the Report | Check and note down the PIR (IndReq VSFB) of the material SG224. |  |  |
| 6 | Back | Choose Home. |  |  |

##### Material Requirements Planning for Finished Product

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
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirement Planning (MRP)Job Name: <MRP for FG228>Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: <select>Recurrence Pattern: Single RunChoose OK.Choose Step 3.Choose 4 Parameters and make the following entries:Plant: 3310Material: FG228Changed BOM Components: <select>Planning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG228 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

##### Monitor Material Coverage for Semifinished and Finished Product

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to monitor dependent requirement of SG224 generated by MRP. Compare current PIR with the PIR you note down in section [Monitor Material Coverage for Semifinished Product](#unique_20) [page ] 27, you will find the PIR is consumed by the dependent requirement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments screen displays. |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |
| 4 | Enter Relevant Search Criteria | In the search area, make the following entries and choose Go.Material: SG224Material: FG228Select the filtered rows and choose Manage Materials. | The Manage Material Coverage screen displays.Mark FG228 for the customer order from section [Create Sales Order for Finished Product](#unique_19) [page ] 26 and SG224 without individual segments. |
| 5 | View the Report | Check and compare the PIR (IndReq VSFB) of material SG224 with the individual segment of the customer order FG228 .Results for FG228 : An individual planned order was created for the sales order.Results for SG224 : A dependent requirement from the sales order shows up in the net segment and has consumed the PIR created before.Select the DepReq to show details for the sales order and planned order. | The PIR (IndReq VSFB) of SG224 is consumed. |
| 6 | Back | Choose Home. |  |

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

### Process Integration

The process to be tested in this test script is part of the chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 3F0 (Event-Based Production Cost Posting) | This procedure updates work-in-process calculation, overhead calculation, and variance calculation by linking the posting to the events.Note Start from CE2105, the default Best Practice content is based on event-based result analysis for new customer install and add new country only, rather than previous period-end posting. For existing customers (who activated content before 2105), the default remains unchanged to Period-End Closing – Plant BEI till customer makes the decision to switch. For migration to Event based from Periodic please refer [Production Settlement in Parallel Ledgers](https://help.sap.com/viewer/4032610758dc437089f0c28320eec93f/LATEST/en-US/e49a3770f22547a392455154f3eef6e2.html). If you are still using period-end posting, you may need to refer to non-standard Scope Item BEI - Period-End Closing – Plant. |

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
- see-also :: [[12-production-and-manufacturing/test-script-bill-of-material-management-64f-ae-sap-s-4hana-cloud-publi]]
- see-also :: [[08-sales-order-management/test-script-advanced-intercompany-sales-make-to-order-and-variant-conf]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1BM_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 54,079 chars in the whole document
