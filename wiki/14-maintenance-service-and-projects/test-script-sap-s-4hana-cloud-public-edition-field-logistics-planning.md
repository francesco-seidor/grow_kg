---
id: 14-maintenance-service-and-projects/test-script-sap-s-4hana-cloud-public-edition-field-logistics-planning
title: "Test Script SAP S/4HANA Cloud Public Edition: Field Logistics Planning and Execution – Direct Procurement (5OM_AE) (5OM_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud test script for scope item 5OM_AE: Field Logistics non-stock procurement, receipt, transport and return between base and remote plants."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/field-logistics]
aliases: [5OM_S4CLD2608_BPD_EN_AE]
keywords: [Field Logistics Planning and Execution, field logistics, non-stock items, maintenance orders, purchase orders, goods receipt, return processing, warehouse tasks, goods issue and transport, single plant setup]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5OM_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1118
topic: 14-maintenance-service-and-projects/field-logistics
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition: Field Logistics Planning and Execution – Direct Procurement (5OM_AE) (5OM_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5OM_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Field Logistics Planning and Execution** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Field Logistics Planning and Execution – Direct Procurement (5OM_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232857597)

[2 Prerequisites 4](#_Toc232857598)

[2.1 System Access 4](#_Toc232857599)

[2.2 Roles 4](#_Toc232857600)

[2.3 Master Data and Organizational Data 5](#_Toc232857601)

[2.4 Additional Manual Configuration 6](#_Toc232857602)

[2.5 Business Conditions 6](#_Toc232857603)

[3 Overview Table 7](#_Toc232857604)

[4 Test Procedures 9](#_Toc232857605)

[4.1 Option A: Create a Maintenance Order 9](#_Toc232857606)

[4.2 Option B: Create Project Demand 12](#_Toc232857607)

[4.2.1 Create Project 12](#_Toc232857608)

[4.2.2 Create Demand 13](#_Toc232857609)

[4.3 Create Purchase Order 15](#_Toc232857610)

[4.3.1 Create Purchase Order 15](#_Toc232857611)

[4.3.2 Approve Purchase Order (Optional) 16](#_Toc232857612)

[4.4 Purchase Order Confirmations (Optional) 17](#_Toc232857613)

[4.4.1 Create Inbound Delivery 17](#_Toc232857614)

[4.4.2 Create Confirmation and Advance Shipping Notice (ASN) in SAP Ariba 19](#_Toc232857615)

[4.5 Post Goods Receipt at Base Using 107 Movement Type Two-step GR Process (Optional) 20](#_Toc232857616)

[4.6 Update Non-Stock Details (Optional) 21](#_Toc232857617)

[4.7 Receive Non-stock Items at Base 22](#_Toc232857618)

[4.7.1 Process the Receipt 22](#_Toc232857619)

[4.7.2 Post Partial Goods Receipt at Base (Optional) 25](#_Toc232857620)

[4.7.3 Review Outbound Delivery w/o Reference 27](#_Toc232857621)

[4.7.4 Review Warehouse Tasks 28](#_Toc232857622)

[4.7.5 Add Attachments (Optional) 29](#_Toc232857623)

[4.7.6 Goods Receipt Reversal (Optional) 30](#_Toc232857624)

[4.8 Single Plant Setup 31](#_Toc232857625)

[4.8.1 Create a Maintenance Order 32](#_Toc232857626)

[4.8.2 Create Purchase Order 34](#_Toc232857627)

[4.8.3 Receive at Base 35](#_Toc232857628)

[4.8.4 Issue to Order 38](#_Toc232857629)

[4.9 Move to Stock at Base (Optional) 39](#_Toc232857630)

[4.10 Review Item Status in Overview Dashboard (Optional) 40](#_Toc232857631)

[4.11 Release of Hold and Ready for Transport (Optional) 41](#_Toc232857632)

[4.11.1 Release of Hold in Maintenance Order 41](#_Toc232857633)

[4.11.2 Review Non-stock Item Transport Ready Status 42](#_Toc232857634)

[4.11.3 Review Delivery Block Release in Outbound Delivery 43](#_Toc232857635)

[4.12 Post Goods Issue and Initiate Transport 44](#_Toc232857636)

[4.12.1 Complete Open Warehouse Tasks 44](#_Toc232857637)

[4.12.2 Post Goods Issue 45](#_Toc232857638)

[4.12.3 Initiate Transport from Base 46](#_Toc232857639)

[4.13 Receive Non-stock Item at Remote 47](#_Toc232857640)

[4.13.1 Process Receipt 47](#_Toc232857641)

[4.13.2 Issue to Order 49](#_Toc232857642)

[4.14 Move to Stock at Remote (Optional) 49](#_Toc232857643)

[4.15 Process Return for Non-stock Items 50](#_Toc232857644)

[4.15.1 Initiate Return 50](#_Toc232857645)

[4.15.2 Create Additional Handling Units (Optional) 52](#_Toc232857646)

[4.15.3 Complete Open Warehouse Tasks 53](#_Toc232857647)

[4.15.4 Enter Load Quantity and Dispatch 54](#_Toc232857648)

[4.16 Receive Non-stock Items at Base 56](#_Toc232857649)

[4.16.1 Receive Returned Non-stock Items at Base 56](#_Toc232857650)

[4.16.2 Move to Stock at Base (Optional) 57](#_Toc232857651)

[4.17 Create Ad hoc Items (Optional) 58](#_Toc232857652)

[4.17.1 Create Ad hoc Item for Base to Remote 59](#_Toc232857653)

[4.17.2 Create Ad hoc Item for Remote to Base (Return) 60](#_Toc232857654)

## Purpose

Overview

This scope item supports the logistics between a supplying base and remote locations – receiving products needed for maintenance operations at the base and forwarding them to the remote, as well as return from the remote back to the base.

This covers the following supply scenarios (SP15):

- Non-stock items with material master
- Non-stock items without material master (free text items)

The process covers the following return scenarios:

- Return to base (to inventory, to scrap, to vendor)

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Maintenance Planner | SAP_BR_MAINTENANCE_PLANNER | Maintenance Planning | SAP_BR_MAINTENANCE_PLANNER |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Receiving Specialist (IOG) | SAP_BR_RCVG_SPECIALIST_IOG | Field Logistics Planning and Execution / Transfers - Field Logistics / Field Logistics - Tracking |  |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk (IOG) | SAP_BR_WAREHOUSE_CLERK_IOG | Field Logistics Planning and Execution / Transfers - Field Logistics / Field Logistics - Tracking | SAP_BR_SC_ANALYST_IOG |  |
| Project Financial Controller | SAP_BR_PROJ_FIN_CONTROLLER | SAP_BR_PROJ_FIN_CONTROLLER | SAP_BR_PROJ_FIN_CONTROLLER |  |
| Project Controller - Resourcing and Procurement | SAP_BR_PROJ_PROC_CONTROLLER | SAP_BR_PROJ_PROC_CONTROLLER | SAP_BR_PROJ_PROC_CONTROLLER |  |
| Administrator | SAP_BR_ADMINISTRATOR( Catalog- SAP_CA_BC_OC) | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC | SAP_BR_ADMINISTRATOR |  |

### Master Data and Organizational Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents material, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 1710 | Company Code 1710 |  |
| Plant | FORP | Plant 2 US (Remote Plant) | Flex.Org App extension |
| Storage Location | FORN | Std. storage 1 | Flex.Org App extension in Plant 1 US |
| Storage Location | FORH | Std. storage 2 | Flex.Org App extension in Plant 1 US |
| Shipping Point | FORP | Shipping Point FORP | Flex.Org App extension |
| Sales Organization | FLPO | Sales Organization in Company 1710 (Remote) | Flex.Org App extension |
| Purchase Organization | FLPO | Purchase Organization in Company 1710 | Flex.Org App extension |
| Plant | FOBP | Plant 3 US (Base Plant) | Flex.Org App extension |
| Sales Organization | FOBP | Sales Organization in Company 1710(Base) | Flex.Org App extension |
| Material | FLOG-NLAG | Non-Stock material |  |
| Supplier | VENFLPO | External Vendor |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/0b822478e3f11861de7d55e940e91973)

### Business Conditions

Before execution of this scope item, please ensure that the below scope items are active and the corresponding set-up for those scope items are executed if required. These configuration steps are specific for your implementation. They include mandatory settings that are not delivered by SAP and must be created by you. For more information, refer to the document in the SAP Signavio Process Navigator.

| Scope Item | Business Condition |
| --- | --- |
| 40G - Field Logistics Planning and Execution | Has to be activated and setup completed |
| 4AH - Field Logistics Planning and Execution – Supplier Items | Has to be activated and setup completed |
| 4RF - Project Control – Resourcing and Procurement | Has to be activated and setup completed |
| 42K - Automation of Source-to-Pay with SAP Business Network | Has to be activated and setup completed |

## Overview Table

This scope item consists of several process steps, provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App / Transaction | Expected Results |
| --- | --- | --- | --- |
| Create Maintenance Order | Maintenance Planner | Create Maintenance Order app | Maintenance order is created for the malfunction report. |
| Create Purchase Order from Purchase Requisition | Purchaser | Create Purchase Order (ME21N) | A purchase order with non-stock material line item created. |
| Approve Purchase Order | Purchasing Manager | My Inbox - All Items (F0862) | The purchase order is approved. |
| Update Packaging Material, Storage Location, and Dimension in the Manage Logistics appAdd attachments in Manage Logistics app | Receiving Specialist (IOG) | Manage Logistics - Supplier Items (F5082) | Packaging material, storage location, and dimension are updated. |
| Confirm Receipt at Base with Visual Inspection | Receiving Specialist (IOG) | Process Receipts - Stock and Supplier Items (F5316) | Receipt at the base with the visual inspection done. |
| Overview Pages | Receiving Specialist (IOG) | Receipt and Return Overview | To view the non-stock items in the overview page cards. |
| Pick Outbound Deliveries | Shipping Specialist (IOG) | Change Outbound Delivery | Perform the picking task. |
| Process warehouse tasks at base | Warehouse Clerk (EWM) | Process Warehouse Tasks | Confirm open warehouse tasks. |
| Receive at remote | Receiving Specialist (IOG) | Process Receipts - Stock and Supplier Items (F5316) | Receipt at the remote. |
| Return Process for non-stock items | Warehouse Clerk (IOG) | Initiate Returns By product (F4252) | The return is initiated from remote. |
| Process warehouse tasks at remote | Warehouse Clerk (EWM) | Process Warehouse Tasks | Confirm open warehouse tasks. |
| Process cross plant receipts | Warehouse Clerk (IOG) | Process Cross-Plant Receipts (F4713) | Receive items back at the base during returns or receive the transferred items from another remote. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

|  |
| --- |
| Note Field Logistics enables intercompany code processes by coordinating and executing the physical movement of goods between different company codes. For required configurations and prerequisites, refer to the setup guide for scope items 40G and 5OM. |

|  |
| --- |
| Note Supply process determination is supported in maintenance orders created through maintenance plan scheduling, using both the Schedule Maintenance Plan (IP10) app and the Mass Schedule Maintenance Plan (IP30H and F2774) app. |

### Option A: Create a Maintenance Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create the purchase requisition from the maintenance order and use the maintenance order to collect all the materials required to correct the malfunction in the remote plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Maintenance Order app. | The Create Order screen is displayed. |  |
| 3 | Create Maintenance Order | On the Create Order screen, choose Order type: Preventive Maintenance YBA2, Planning Plant: FORP and then choose Continue. | The order type is selected. |  |
| 4 | Enter the Details | On the Create Preventive Maintenance Order: %00000000001 screen, go to the General Data tab.Make the following entries:In the Responsibilities section,Work Center: FORP-PM Work Center Plant: FORP | The work center details are entered. |  |
| 5 | Define the Operations to be Performed to Resolve the Malfunction | Go to the Operation Data tab. You can see the operation overview in the Operations table for operation 0010: | Selecting the item number. |  |
| 6 | Select Material | Choose Material s tab at the bottom of the screen.On the Materials tab, you can create a non-stock material either from Material Master or Free Text Material or use a stock material as non-stock. All these options are described below, you can select one or any combination of more than 1 option for your testing.Option 1: Using Free Text Material.Description: NS Free TextItem Category: Non-stock item (N)Quantity: 20Unit: KGG/L Account: 52001000Material Group: YBMM00Purchasing Organization: FLPOPurchasing Group: 001Hold On-Shore: X (optional)Option 2: Using Non-Stock Material Master (type NLAG)Material: FLOG-NLAGQuantity: 20G/L Account: 51700000Purchasing Organization: FLPOPurchasing Group: 001Hold On-Shore: X (optional)Option 3: SP11, SP12, SP13 or SP14 material as non-stock.(This option is subject to the setup of flexible supply process determination for SP11 to SP14 materials)Material: FLOG-SP14 (or FLOG-SP11/ FLOG-SP12/ FLOG-SP13)Item Category : Non-stock item (N)Quantity: 20Purchasing Organization : FLPOPurchasing Group: 001G/L Account: 51700000Note This option can only be used with the following flexible supply processes configuration, as in all cases the supply process is determined as SP15.SP11 version selected as V2 or V3: The item category is configured as blank, and you choose item category non-stock Item during maintenance order creation,SP12 version selected as V1: The item category is configured as blank, and you choose item category non-stock Item during maintenance order creation.SP13 version selected as V2 or V3: The item category is configured as blank, and you choose item category non-stock Item during maintenance order creation.SP12 version selected as V1: The item category is configured as blank, and you choose item category non-stock Item during maintenance order creation.SP15 is selected as supply process. | Item material details are entered. Item category should be defaulted to N and Field Logistics supply process should be defaulted to SP15 for all options. |  |
| 7 | Check Entries | Choose Check Entries on the top left corner of the screen. | Entries have been checked. |  |
| 8 | Hold on Shore Flag (optional) | Check hold on shore flag for all items that have to be held. You can maintain a hold indicator for one or more non-stock items within an operation.Hold On-Shore: XNote The flag Hold On-Shore is part of the Field Logistics functionality for holding and cross-docking. For necessary configuration and prerequisites refer to the setup guide of scope item 40G, as well as the SAP documentation. | Hold flag is checked.Any further delivery of the related physical items to the offshore plant will be blocked until the hold flag is cleared. |  |
| 9 | Save Order | Choose Save. | Maintenance Order 4000XXX is saved. Purchase Request 1000XXXX is also createdNote down the purchase requisition generated for SP15 for further use.Delivery date in PR is calculated as below:Delivery date in PR = (Work Order Requirement Date) - (GR process time (FOBP) (Factory Days) - (Planned Delivery Time (FORP)) (Calendar Days) - (Planned Delivery Time (FOBP)) (Calendar Days) - (GR process time (FORP) (Factory Days) |  |
| 10 | Phase Control Check (optional) | Check the phase control status at header and operation level.Note Use of the phase control statuses TOH and TPOH is part of the Field Logistics functionality for holding and cross-docking. For necessary configuration and prerequisites refer to the setup guide of scope item 40G, as well as the SAP documentation. | The phase control on header level should have the active status:TOH in case all components of the order have the flag Hold On-Shore setTPOH in case some components of the order have the flag Hold On-Shore setNeither, in case no components have the flag setThe phase control on operation level should have the active status:TOH in case all components of the operation have the flag Hold On-Shore setTPOH in case some components of the operation have the flag Hold On-Shore setNeither, in case no items have the flag set |  |
| 11 | Release Order | In the Set System Status menu, choose Release.Choose Save. | Status of this maintenance order changes to Rel. |  |
| 12 | Log Out | Choose Sign Out. |  |  |

### Option B: Create Project Demand

#### Create Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create purchase requisition from the project and demand flow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Financial Controller. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the app Project Control - Enterprise Projects (F3215). | The Project Control screen displays. |  |
| 3 | Create Project | Choose Create.Enter the following:Project Name: NewBoreXXXProject ID: NewBoreIDXXXProject Profile: Overhead ProjectPlanned Start: <One month from current date>Planned Finish: <Two months from current date>Responsible Cost Center: 17101101Profit Center: YB600Choose Create.To enter the plant details, choose Edit.Enter lant: FORP. | The New Project screen displays. |  |
| 4 | Save Project | The item details are provided. | Project PNXXX is saved. |  |
| 5 | Release Project | Go to the Processing Status menu on the top.Select the Release option. | The project is released. |  |

#### Create Demand

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create a demand for the project.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Controller - Resourcing and Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the app Manage Project Demand (F4562). | The Manage Project Demand screen displays. |  |
| 3 | Create Demand | Click on Create on the Items tab.On the New Demand screen, you can either create demand from material master data or use free text material.Option 1: In the case of material master data, enter the following on the Demand tab:Demand Name: NewBoreDemandXXXWBS Element: NewBoreIDXXX(Enter the Project ID created during Project Creation)Press Enter.Material: FLOG-NLAGQuantity: 1Demand ID: XXXOption 2: In the case of free text material, enter the following on the Demand tab:Demand Name: NewBoreDemandXXXWBS Element: NewBoreIDXXX(Enter the project ID created during project creation)Press Enter.Quantity: 1Unit Of Measure: WeeksDemand ID: XXXDemand Type: Non-Stock MaterialPlant: FORPMaterial Group: YBMM01Purchasing Group: 001Purchasing Organization: FLPOChoose Create. | The New Demand screen displays. |  |
| 4 | Request the Demand | Search the newly created demand NewBoreDemandXXX, on the Materials tab on the left side of the screen.Select the checkbox for the searched demand.Choose Change Demand Status.Select Request on WBS Element release | The purchase requisition is created. In case of free text demand, the item description of PR will be the demand name (NewBoreDemandXXX). |  |

### Create Purchase Order

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can formalize a specific requirement for a non-stock material from the vendor by creating a purchase order and from the purchase requisition created by the maintenance order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the app Create Purchase Order - Advanced (ME21N). | The Create Order screen is displayed. |  |
| 3 | Create Order | On the Purchase Order screen, enter the details as below.On the Item Overview tab:Purchase Requisition: Purchase requisition number created during plant maintenance order Net Price: 100On the Basic Data tab:Supplier: VENFLPOPress Enter | The purchase order details are provided. |  |
| 4 | Save Purchase Order | Choose Save. | The purchase order 45XXXXXXX is created.This will create the data automatically in Manage Logistics app. |  |

|  |
| --- |
| Note It is possible to create standalone Purchase Requisitions and Purchase Order at Field Logistics plants (Base and Remote) as part of direct procurement of required goods without reference to any supply process in Field Logistics. |

#### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can approve a purchase order if the purchase order is not released yet.

A prerequisite is the existence of a purchase order that can be released.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items(F0862). | A list of existing purchase orders is displayed. |  |
| 3 | Search for Purchase Order Status | Make the following entry and choose Enter:Search: <Purchase Order number> | The purchase order is displayed. |  |
| 4 | Approve Purchase Order | Select the purchase order on the left side of the screen.Choose Approve at the bottom right.Enter the approval reason, if necessary.Choose Submit. | The Submit Decision screen is displayed.The purchase order is approved. |  |

### Purchase Order Confirmations (Optional)

Confirmations are used when you wish to receive advance information (via the shipping notification or inbound delivery) about the expected goods receipt date.

#### Create Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To simulate a confirmation from the supplier, you can manually create an inbound delivery against the purchase order which was created in the above section.

|  |
| --- |
| Note This is possible only if the user has selected confirmation or inbound delivery for conf. control in the confirmation tab of item detail section. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the app Create Inbound Delivery. | The Create Inbound Delivery screen is displayed. |  |
| 3 | Enter the data | Enter the details below.Supplier: VENFLPOPurchase Order: The above created purchase order number.Delivery Date: Delivery date from the above purchase order.Press enter. | All the purchase order items will be listed here. |  |
| 4 | Create Full or Partial Inbound Delivery | You can either create full delivery quantity inbound delivery or multiple / partial quantity inbound delivery.Update the dimension information (for example, gross weight, volume) and delivery date.Click on Save. | If full delivery quantity is entered, then in the list page of Process Receipts - Stock and Non-stock items (F5316) app, you will get one record under To Be Received section. Else user will see multiple records.The dimension information and delivery date will get updated in Manage Logistics - Supplier Items (F5082) app (in object page of item).This inbound delivery will be listed under Confirmation tab of Item Detail section for this purchase order in Change Purchase Order-Advanced app. |  |
| 5 | Entering Putaway Quantity in Process Receipts - Stock and Non-stock items (F5316) app. | Search this purchase order in the Process Receipts - Stock and Non-stock items (F5316) app list page.Navigate to the object page.Click on Update Delivery.Enter putaway quantity and click on Update Delivery. | You can check this putaway quantity in inbound delivery using app Change Inbound Delivery against this inbound delivery number. |  |

#### Create Confirmation and Advance Shipping Notice (ASN) in SAP Ariba

If you have integration with the SAP Ariba system, the purchase order created in SAP S/4HANA Cloud Public Edition will be replicated in the SAP Ariba system automatically. In the SAP Ariba system, you can trigger order confirmation and advance shipping notice (ASN). The confirmation will be replicated to SAP S/4HANA Cloud Public Edition as acknowledgment and ASN will be replicated as an inbound delivery document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can get the latest delivery date, quantity, and unit via confirmation or advance shipping notice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Ariba System | Log on to the SAP Ariba system as Ariba Supplier. | The SAP Ariba Seller Portal Dashboard screen is displayed. |  |
| 2 | Search the Purchase Order | Enter the purchase order number, which was created in the SAP S/4HANA Cloud Public Edition system. | The purchase order is displayed if the confirmation control has the value Confirmations in the purchase order on the Confirmation tab in the SAP S/4HANA Cloud Public Edition system. |  |
| 3 | Select the Purchase Order | Enter the purchase order, which was created in the above step. | This displays the list of items of the entered purchase order. |  |
| 4 | Navigate to the Object Page | Click on the purchase order number to navigate to the object detail page. | This displays the object detail page.Routing Status: will be sent |  |
| 5 | Purchase Order Confirmation (Optional) | Users can confirm the purchase order by clicking Confirm Entire Order.Enter the confirmation number, supplier reference number, and comments.Click on Next.Click on Submit.Click on Done. | Routing Status: changes to Acknowledged.Confirmation record is created in SAP S/4HANA Cloud Public Edition system purchase order also on the Confirmation tab with confirmation category as AB (Order Acknowledgment). |  |
| 6 | Create Shipping Notice | Select the confirmed purchase order from the above steps and click on Create Ship Notice. | Another confirmation record is created in the SAP S/4HANA Cloud Public Edition system purchase order on the Confirmation tab with the confirmation category as LA (Inbound Delivery).Information such as delivery date, actual delivery quantity, delivery quantity unit, and actual delivery quantity are updated back to Manage Logistics non-stock items. |  |

### Post Goods Receipt at Base Using 107 Movement Type Two-step GR Process (Optional)

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

| Test Step# | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement application. | The Post Goods Movement screen is displayed. |  |
| 3 | Choose the Process and Movement Type for Warehouse and Non-Warehouse Managed Scenarios | Choose Goods ReceiptChoose Purchase OrderEnter the purchase order and movement type 107. | The goods receipt data is displayed on the screen. |  |
| 4 | Choose the Process and Movement Type for Non-Inbound Delivery Scenario | Choose Goods ReceiptChoose Purchase OrderEnter the purchase order and movement type 107. | The goods receipt data is displayed on the screen. |  |
| 5 | Check and Verify the Details | Check and verify all the details like material, quantity, and storage location. | All details are checked. |  |
| 6 | Post Goods Receipt | Select the items for which a goods receipt is to be posted.Choose Post | Goods receipt is posted.The system displays the message, material document xxx posted. |  |

|  |
| --- |
| Note After goods receipt with 107 is completed, then the next step 109 can be done from Process Receipts - Stock and Non-stock items (F5316) |

### Update Non-Stock Details (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to update the missing information if known before the item arrives at the base. This update is to be done using the Manage Logistics - Supplier Items (F5082) application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG) role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Logistics - Supplier Items(F5082) app. | The screen with section Arriving at Base open is displayed. |  |
| 3 | Select the Purchase Order | Enter the purchase order, which was created in the above step. | The list of items of the entered purchase order is displayed. |  |
| 4 | Navigate to the Object Page | Select the required item to navigate to the object detail page | The object detail page is displayed. |  |
| 5 | Update the Packaging Material | Choose Edit.Enter the following details:Packaging Material: PMPALLETStorage Location: FOBW (Cloud Warehouse Management enabled) or FOBN (non-Cloud Warehouse Management enabled).Update the values for weight, length, width, height, and units as applicable. | Entering data. |  |
| 6 | Save the Changes | Choose Save. | Data is saved. |  |

### Receive Non-stock Items at Base

#### Process the Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can confirm the receipt of items at the base using Process Receipts - Stock and Non-stock items (F5316).

For receiving at base in a single plant scenario, refer to section [Single Plant Setup](#unique_24) [page ] 31.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to Fiori Launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Receipts - Stock and Non-stock items (F5316) app. | The screen with the section To Be Received is displayed. |  |
| 3 | Select the Purchase Order | Enter the purchase order, which was created in [Create Purchase Order](#unique_15) [page ] 15 | This displays the list of items that are in To Be Received status. |  |
| 4 | Navigate to the Object Page | Select the required item to navigate to the object page. | This displays the object detail page. |  |
| 5 | Update the Required Information | Choose the Receive button on the top.Enter the following details:Visual inspection: Passed / Passed – minor surface damages (Optional)Storage location: FOBWPackaging material: PMPALLETNote The goods receipt posting with 109 will be supported with only full quantity of the LE IBD and EWM IBD item for which 107 has happened.For example, in case 107 movement is already completed, the same quantity is updated for 109 movement and no further update is allowed in system. | Entered data is available in the respective fields. |  |
| 6 | Check for Errors | Choose Check. | No errors would show if the simulation of goods receipt completes without any error. |  |
| 7 | Confirm the Changes | Choose Confirm. | If you go back to the list page of this Process Receipts - Stock and Non-stock items (F5316) app, you can see under the selected purchase order the received quantity is 20 under the Received tab. Whereas you cannot find the selected purchase order entry under To Be Received tab.You can navigate to the Manage Logistics app by clicking the Manage Logistics on the top of the object page and verifying the documents under the Business Document section. |  |
| 8 | Print Preview | Choose Print Preview.Select Product Label and HU Label | This allows you to check the details and layout before printingProduct label displays following details:ProductProduct DescriptionGoods Receipt DateReceived QuantityOrder CategoryOrderGoods Receipt NumberPurchase Order/ItemVisual InspectionQuality Managed StatusItem TypePrint DateField Logistics StatusInstructionsHandling Unit label displays following details:Outbound Delivery NumberHandling Unit NumberReceived QuantityPacked QuantityGoods Receipt NumberGoods Receipt DateItem TypePrint DateOrder CategoryOrder NumberOrder DescriptionGross WeightPurchase order/ItemsField Logistics StatusInstructionsNote Field logistics enables you to print instructions dynamically on Product label and Handling until label based on processes with respect to field logistics status. |  |
| 9 | Download | Click on Download. | The user can choose to download the Product label and HU label details from the print preview as an PDF file. |  |
| 10 | Trigger Output Management Queue | Click on Print.Select Product Label and HU Label | The Product Label and Handling Unit Label details are sent to the print queue without previewing the details.If the necessary configurations are maintained, Printing the labels will trigger an email notification as well.Details of the queue can be viewed from the Manage Output Items app.Note Field logistics supports extensibility which enables you to implement your custom logic in filling in the values for the custom fields added to the print label forms. |  |

#### Post Partial Goods Receipt at Base (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to confirm the receipt at the base if a partial quantity item is received (Create Partial Goods Receipt).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG) role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Receipts - Stock and Non-stock items (F5316) app. | A screen with the To Be Received tab is displayed. |  |
| 3 | Select the Purchase Order | Enter the purchase order, which was created in [Create Purchase Order](#unique_15) [page ] 15 | The list of items which are in To Be Received tab is displayed. |  |
| 4 | Navigate to the Object Page | Select the required item to the Object detail page. | The page navigates to the object page. |  |
| 5 | Update the Packaging and Other Data | Choose Receive.Set the visual inspection appropriately.If packaging material is not entered in the above step, then select packaging material as PMPALLET.Select the storage location as FOBW.Change the Delivered Quantity from 20 to 8. (or any other quantity less than 20 to make it a partial receipt) | Entering the data. |  |
| 6 | Check for Errors | Choose Check. | No errors would show if the simulation of goods receipt executes without an error. |  |
| 7 | Confirm the Changes | Choose Confirm. | If you navigate back to the list page of the Process Receipt app, you can see this received quantity as 8 on the Received tab.Whereas you can see the remaining quantity 12 on the tab To Be Received.You can navigate to the Manage Logistics App by clicking Manage Logistics on the top of the object page and verifying the below points under the Business Document section. |  |
| 8 | Print Label of Product and Handling Unit (Optional) | Choose Print Label. | If you select the Product Label checkbox and choose Print Label, then the label will display product details along with the QR Code. Product details will be like product ID, description, item type, and unit of measure. The system will also display maintenance order, purchase order, goods receipt date, and print date.If you select Handling Unit Label checkbox and choose Print Label, then the label will display ship to address, outbound delivery number, LE handling unit number, item type, maintenance order, purchase order, goods receipt date, and print date. The QR code is also displayed along. |  |

#### Review Outbound Delivery w/o Reference

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once the non-stock item is received at the base, a logistic execution outbound delivery without reference document is created automatically. Below are some variations of the use cases system supports based on the input during the process receipt.

- If supplying plant is different from the demand plant, an outbound delivery document w/o reference is created automatically. Additionally, items are fully picked up in the delivery automatically.
- If packaging material is entered during the receipt, a LE handling unit is created automatically and associated with the outbound delivery document created earlier. Additionally, all the items are fully packed by default to the handling unit created.
- If the maintenance work order item was created with Hold On-Site as Yes, a delivery block is set on the outbound delivery w/o reference with the blocking reason as Hold at Base (FL).

You can view the outbound delivery w/o reference document using the Display Outbound Delivery application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to Fiori Launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG) . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Logistics - Supplier Items (F5082) app.Enter the purchase order which was used in the previous step.Choose the required item to navigate to the object page. | The Manage Logistics screen is displayed. |  |
| 3 | Navigate to the Outbound Delivery | Under the Business Documents facet, click the field Outbound Delivery value hyperlink. | The page navigates the Display Outbound Delivery application. |  |
| 4 | Confirm the Picking and Packing Status | Under the header details, Processing > Overall Status section find below status:Picking status: Fully PickedPacking status: Completely Packed | Value is displayed as expected. |  |
| 5 | Confirm the Delivery Block Value | Under the header details, Processing > Administration > Control section find delivery block value. | If the maintenance work order item was created with Hold On-Site as Yes, then the delivery block would show the value Hold at Base (FL).If the maintenance work order item was created with Hold On-Site as No, then the delivery block would show the blank value. |  |

|  |
| --- |
| Note In case outbound delivery is deleted using Change Outbound Delivery application or outbound delivery creation failed due to other reason, in such cases outbound delivery can be created using action Create Outbound Delivery from Manage Logistics-Supplier Items application. |

#### Review Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After a non-stock Item is received at the base, to enable the minimum warehouse movements for a non-stock Item, a cloud warehouse management enabled empty handling unit is created automatically. This is created in reference to a logistics execution handling unit. Below are some variations of the use cases system supports based on the input during the process of receipt.

- If the base storage location entered during the receipt is cloud warehouse management enabled and packaging material is provided, a cloud warehouse management handling unit is created automatically.
- In addition, If the maintenance work order item was created with Hold On-Site as Yes and a cloud warehouse management handling unit is created then a warehouse task is created automatically with the source bin as GR-AREA and the destination bin as HOLD-AREA.
- If the maintenance work order item was created with Hold On-Site as No and a cloud warehouse management handling unit is created, then a warehouse task is created automatically with the source bin as GR-AREA and the destination bin as GI-AREA.

|  |
| --- |
| Note The destination area is determined based on the customization value maintained in cloud warehouse management customizing (Assign Storage Bins to Warehouse Process Type). |

You can view the warehouse task created in the Manage Logistics - Supplier Items (F5082) application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to Fiori Launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Logistics - Supplier Items (F5082) app.Enter the purchase order which was used in the previous step.Choose the required item to navigate to the object page. | The Manage Logistics screen is displayed. |  |
| 3 | Navigate to the Warehouse Task | Under the Business Documents facet, you can find warehouse task.To confirm or cancel the open warehouse task, user needs to login as warehouse_clerk_ewm user and find the Process Warehouse Task app.In Process Warehouse Task app, give warehouse number as FOBP and warehouse task as the warehouse task number which can be found in Manage Logistics - Supplier Items (F5082) app and click on GO.Click on check for required warehouse task and click on confirm or cancel accordingly. | The page navigates the Process Warehouse Task application.The source and the destination bin field have expected bin values. |  |

#### Add Attachments (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can upload additional information as attachments to the non-stock items in the Manage Logistics - Supplier Items (F5082) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG) role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Logistics - Supplier Items(F5082). | The Manage Logistics screen is displayed. |  |
| 3 | Upload File | Choose Edit.Go to Attachments and choose Upload.Upload a file. | The file is uploaded, and data is saved. |  |
| 4 | Add a Link | In the Attachments tab, choose Add a Link.Follow the prerequisite steps provided below to add a URL link.Login as an Administrator to app Maintain Protection Allowlists (F3195).In the Trusted Network Zones tab, choose Plus (+) to add a new entry.Enter Website Domain name, Schema (as HTTP / HTTPS) and Port (as *).Enter the URL and Description of the link. | The link is attached. |  |
| 5 | Save Entries | Choose Save. | The data is saved. |  |

#### Goods Receipt Reversal (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to cancel the confirmed receipt at the base.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to Fiori Launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the app Process Receipts - Stock and Non-stock items (F5316). | The Process Receipts screen is displayed. |  |
| 3 | Select the Purchase Order | Enter the purchase order, which was created in the [Process the Receipt](#unique_23) [page ] 22 step. | This displays the items on the To be Received tab. |  |
| 4 | Navigate to Object Page | Select the required line item to navigate to the object page. | This displays the object page. |  |
| 5 | Update Other Data | Choose Reverse.Select the Posting Date.Enter Additional Note and choose Reverse. | Goods receipt reversal popup is displayed for two-step reverse wizard in case warehouse task and handling unit is existing for an item.It will cancel the open warehouse task.It will delete the Handling unit assigned to outbound delivery.Goods receipt reversal is posted.On refresh, the status changes to Cancelled Receipt At Base.In the worklist of the Process Receipts - Stock and Non-stock items (F5316) app, this purchase order gets listed on the To Be Received tab.In the Manage Logistics app, the milestone and status are set to Cancelled Receipt At Base. |  |

### Single Plant Setup

The single plant (or self-sufficient plant, or base as remote) scenario is a simplified scenario where demand plant = supply plant. The maintenance as well as warehousing and procurement activities take place in the same plant. The prerequisites and configuration to run this scenario are mentioned in the setup guide.

|  |
| --- |
| Note Only the steps up to receiving at base apply for this scenario since it does not include any further logistics movement to the offshore plant. |

#### Create a Maintenance Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create the purchase requisition from the maintenance order and use the maintenance order to collect all the materials required to correct the malfunction in the remote plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Maintenance Order app. | The Create Order screen is displayed. |  |
| 3 | Create Maintenance Order | On the Create Order screen, choose Order type: Preventive Maintenance YBA2, Planning Plant: FOBP and then choose Continue. | The order type is selected. |  |
| 4 | Enter the Details | On the Create Preventive Maintenance Order: %00000000001 screen, go to the General Data tab.Make the following entries:In the Responsibilities section,Work Center: FOBP-PMWork Center Plant: FOBP | The work center details are entered. |  |
| 5 | Define the Operations to be Performed to Resolve the Malfunction | Go to the Operation Data tab. You can see the operation overview in the Operations table for operation 0010. | Selecting the item number. |  |
| 6 | Select Material | Choose Materials tab at the bottom of the screen.On the Materials tab, you can create a non-stock material either from Material Master or Free Text Material or use a stock material as non-stock. All these options are described below, you can select one or any combination of more than 1 option for your testing.Option 1: Using Free Text Material.Material Group: YBMM00 (if this field is not available in the table then add this from the settings before you add this Free text non-stock material line)Description: NS Free TextItem Category: Non-stock item (N)Quantity: 20Unit: EAG/L Account: 52001000Purchasing Organization : FLPOPurchasing Group: 001Option 2: Using Non-Stock Material Master (type NLAG)Material: FLOG-NLAGQuantity: 20G/L Account: 52001000Purchasing Organization : FLPOPurchasing Group : 001Option 3: SP11, SP12, SP13 or SP14 material as non-stock.(This option is subject to the setup of flexible supply process determination for SP11 to SP14 materials)Material: FLOG-SP14 (or FLOG-SP11/ FLOG-SP12/ FLOG-SP13)Item Category: Non-stock item (N)Quantity: 20Purchasing Organization: FLPOPurchasing Group: 001G/L Account: 51700000Note This option can only be used with the following flexible supply processes configuration, as in all cases the supply process is determined as SP15.SP11 version selected as V2 or V3: The item category is configured as blank and you choose item category non-stock item during maintenance order creation.SP12 version selected as V1: The item category is configured as blank and you choose item category non-stock Item during maintenance order creation.SP13 version selected as V2 or V3: The item category is configured as blank and you choose item category non-stock item during maintenance order creation.SP14 version selected as V1: The item category is configured as blank and you choose item category non-stock item during maintenance order creation.SP15 is selected as supply process. | Item material details are entered. Item category should be defaulted to N and Field Logistics supply process should be defaulted to SP15 for all options. |  |
| 7 | Check Entries | Choose Check Entries on the top left corner of the screen. | Entries have been checked. |  |
| 8 | Save Order | Choose Save. | Maintenance Order 4000XXX is saved. Purchase Request 1000XXXX is also created. |  |
| 9 | Release Order | In the Set System Status menu, choose Release.Choose Save. | Status of this maintenance order changes to Rel. |  |
| 10 | Log Out | Choose Sign Out. |  |  |

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can formalize a specific requirement for a non-stock material from the vendor by creating a purchase order and from the purchase requisition created by the maintenance order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the application Create Purchase Order - AdvancedME21N. | The Create Order screen is displayed. |  |
| 3 | Create Order | On the Purchase Order screen, enter the details as below.In Item Overview tab:Purchase Requisition: Purchase requisition number created during plant maintenance order Net Price: 100In Basic Data tab:Supplier: VENFLPOPress Enter | The purchase order details are provided. |  |
| 4 | Save Purchase Order | Choose Save | The purchase order 45XXXXXXX is created.This will create the data automatically in Manage Logistics app. |  |

#### Receive at Base

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can confirm the receipt of items at the base using the Process Receipts - Stock and Non-stock items (F5316) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to Fiori Launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Receipts - Stock and Non-stock items (F5316) app. | The screen with the section To Be Received is displayed. |  |
| 3 | Select the Purchase Order | Enter the Purchase Order which was created in the Create Purchase Order. | This displays the list of items that are in To Be Received status. |  |
| 4 | Navigate to the Object Page | Select the required item to navigate to the object page. | This displays the object detail page. |  |
| 5 | Update the Required Information | Choose to Receive button on the top.Choose below details:Visual inspection: Passed (Optional)Storage location: FOBW.Packaging Material: PMPALLET.Note The goods receipt posting with 109 will be supported with only full quantity of the LE IBD and EWM IBD item for which 107 has happened.For example, in case 107 movement is already completed, the same quantity is updated for 109 movement and no further update is allowed in system.Immediate issue to Maint. Order: X (optional)Note The field Immediate Issue to Maint. Order will only be available for the user to update for non-stock Items ordered for a single plant scenario plant (supplying plant = demand plant). Users can choose this option to additionally consume the item along with the Receipt in a single step. If this flag is set, the next step of issuing to order is obsolete. | Entered data is available in the respective fields. |  |
| 6 | Check for Errors | Choose Check. | No errors would show if the simulation of goods receipt completes without any error. |  |
| 7 | Confirm the Changes | Choose Confirm. | If you go back to the list page of this Process Receipt app, you can see under the selected purchase order the received quantity is 20 under the Received tab. Whereas you cannot find the selected Purchase Oder entry under the To Be Received tab.You can navigate to the Manage Logistics app by clicking the Manage Logistics on the top of the object page and verifying the documents under the Business Document section. |  |
| 8 | Print Preview | Choose Print Preview.Select Product Label and HU Label | This allows you to check the details and layout before printing.Product label displays following details:ProductProduct DescriptionGoods Receipt DateReceived QuantityOrder CategoryOrderGoods Receipt NumberPurchase Order/ItemVisual InspectionQuality Managed StatusItem TypePrint DateField Logistics StatusInstructionsHandling Unit label displays following details:Outbound Delivery NumberHandling Unit NumberReceived QuantityPacked QuantityGoods Receipt NumberGoods Receipt DateItem TypePrint DateOrder CategoryOrder NumberOrder DescriptionGross WeightPurchase order/ItemsField Logistics StatusInstructionsNote Field logistics enables you to print instructions dynamically on Product label and Handling until label based on processes with respect to field logistics status. |  |
| 9 | Download | Click on Download. | The user can choose to download the Product label and HU label details from the print preview as an PDF file. |  |
| 10 | Trigger Output Management Queue | Click on Print.Select Product Label and HU Label | The Product Label and Handling Unit Label details are sent to the print queue without previewing the details.If the necessary configurations are maintained, printing the labels will trigger an email notification as well.Details of the queue can be viewed from the Manage Output Items app.Note Field logistics supports extensibility which enables you to implement your custom logic in filling in the values for the custom fields added to the print label forms. |  |

#### Issue to Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After a non-stock item is received at the (single) plant, the goods receipt and consumption is booked, but it might take some time until they are physically consumed by the order.

The user can execute this successive step with the action Issue-to-order in the Manage Logistics - Supplier Items (F5082) application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG) role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Logistics - Supplier Items (F5082).Enter the purchase order which was used in the previous step.Choose the required item to navigate to the object page. | The Manage Logistics screen is displayed. |  |
| 3 | Perform the Issue-to-Order Action | Click on Issue to Order. | A milestone called Issue to Order is created and the status of the item turns to Issued to Order. |  |

### Move to Stock at Base (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to move the non-stock items to stock if this is idle for a long period. This update is to be done using the Manage Logistics app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to Fiori Launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG) role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the app Manage Logistics - Supplier Items (F5082). | The screen with section Arriving at Base is displayed. |  |
| 3 | Select the Purchase Order | Enter the purchase order, which was created in the above step. | This displays the list of items of the entered purchase order. |  |
| 4 | Navigate to Object Page | Select the required item to navigate to the object detail page. | This displays the object detail page. |  |
| 5 | Move to Stock (Optional) | Choose Move to Stock and fill in the below details:Product: FLOG-SP14 (example)Storage Location: FLBNGoods Movement Type: 501Choose Move to Stock.Note: If the status is Received at Base or Ready to Transport then this step can be performed after the configured number of days are passed (refer to Set-up Guide). | The milestone will be updated with the value Move to Stock and the status also will be set to Move to Stock.If the storage location is warehouse managed, then an IBD is created else a goods movement document is created. These documents will be displayed in the business process flow section. |  |

### Review Item Status in Overview Dashboard (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can review the status of non-stock items using the Receipts and Returns Overview (F5479) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the app Receipts and Returns Overview (F5479). | The Receipts and Returns Overview (F5479) screen is displayed. |  |
| 3 | Select the Non-stock Items in Filter | Choose the required non-stock items type filter value. | The cards auto-refresh and loads the filtered data based on your selection. |  |
| 4 | Analyze Different Cards Data and Navigate | Multiple cards display the selected non-stock items data. The cards Delayed Receipt, To Be Received and Receipts show the selected items at different stages in the process.Choose a data set to navigate to from the card by clicking on a chart. | Application navigates to Process Receipts - Stock and Non-stock items (F5316) app and shows the data pre-populated. |  |

### Release of Hold and Ready for Transport (Optional)

#### Release of Hold in Maintenance Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

For changing the Hold On-Shore value of the maintenance order item navigate to Change Maintenance Order application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Change Maintenance Order application | The Change Order screen is displayed. |  |
| 3 | Create Maintenance Order | On the Change Order screen, choose the order number of the maintenance order created earlier then choose Continue. | The order type is selected. |  |
| 4 | Locate the Items for which the Hold Indicator is to be Changed | Go to the Operation Data > Components tab. You can see all the items displayed in the change mode. |  |  |
| 5 | Change and Save | Locate the item for which the hold indicator is to be removed and make the below change:Hold On-Shore: uncheck |  |  |
| 6 | Save Order | Choose Save. | Maintenance order 4000XXX is saved. |  |

#### Review Non-stock Item Transport Ready Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can view the non-stock item status changed in the Manage Logistics - Supplier Items (F5082) application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG) role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Logistics - Supplier Items (F5082).Enter the purchase order which was used in the previous step.Choose the required item to navigate to the object page. | The Manage Logistics screen is displayed. |  |
| 3 | Navigate to the Milestone View Facet | You can see the latest milestone Ready for Transport.The maintenance order is on Hold: NoStatus: Ready for Transport | Values are displayed as expected. |  |

#### Review Delivery Block Release in Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can view the delivery block released changed in the Display Outbound Delivery application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG) role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Logistics - Supplier Items (F5082).Enter the purchase order which was used in the previous step.Choose the required item to navigate to the object page. | The Manage Logistics screen is displayed. |  |
| 3 | Navigate to the Outbound Delivery | Under the Business Documents facet, click the field Outbound Delivery value hyperlink. | The page navigates to the Display Outbound Delivery application. |  |
| 4 | Confirm the Delivery Block Value | Under the header details Processing > Administration > Control section find the delivery block value. | Since the maintenance work order item was changed with Hold On-Site to blank, then the delivery block would show the blank value. |  |

### Post Goods Issue and Initiate Transport

#### Complete Open Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can change the warehouse task to complete the Process Warehouse Task application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG) role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Logistics - Supplier Items (F5082).Enter the purchase order which was used in the previous step.Choose the required item to navigate to the object page. | The Manage Logistics screen is displayed. |  |
| 3 | Navigate to the Warehouse Task | Under the Business Documents facet, you can find warehouse task.To confirm or cancel the open warehouse task, user needs to login as warehouse_clerk_ewm user and find the Process Warehouse Task app.In Process Warehouse Task app, give warehouse number as FOBP and warehouse task as the warehouse task number which can be found in Manage Logistics - Supplier Items (F5082) app and click on GO.Click on check for required warehouse task and click on confirm or cancel accordingly. | The page navigates the Process Warehouse Task application.The source and the destination bin field have expected bin values. |  |
| 4 | Select and Complete the Warehouse Task | Mark the warehouse task displayed on the list page and click on the Confirm. | Warehouse task status is changed to Confirmed. |  |

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can post the goods issue in the Change Outbound Delivery application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG) role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Logistics - Supplier Items (F5082).Enter the purchase order which was used in the previous step.Choose the required item to navigate to the object page. | The Manage Logistics screen is displayed. |  |
| 3 | Navigate to the Outbound Delivery | Under the Business Documents facet, you can find OBD number.Login as SHIPPING_SPECIALIST and search for Change Outbound Delivery app. | The page navigates the Change Outbound Delivery application. |  |
| 4 | Post the Goods Issue | Click on the Post-Goods Issue on the header area. | Goods issue is successfully posted. |  |

#### Initiate Transport from Base

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can trigger the required milestone from the Manage Logistics - Supplier Items (F5082) application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG) role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Logistics - Supplier Items (F5082).Enter the purchase order which was used in the previous step.Choose the required item to navigate to the object page. | The Manage Logistics screen is displayed. |  |
| 3 | Navigate to the Milestone View Facet | You can see the latest milestone Ready for Transport.The maintenance order is on Hold: NoStatus: Ready for Transport | Values are displayed as expected. |  |
| 4 | Trigger Initiation of the Transport from the Base | Click on Initiate Transport. | The milestone Transport Initiated is triggered successfully. |  |

### Receive Non-stock Item at Remote

#### Process Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can receive the item at the destination location and mark the item as Received

|  |
| --- |
| Note Process Receipts - Stock and Non-stock items (F5316) application does not support receiving items at a remote plant for intercompany code scenario. It is recommended to use Process Cross-Plant Receipts (F4713) application for posting goods receipts at remote plants. |

.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG) role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Receipts - Stock and Non-stock items (F5316) app. | The To Be Received tab is displayed. |  |
| 3 | Select the Purchase Order | Enter the purchase order which was created in the step Create Purchase Order. | The list of items, which are in the To Be Received status is displayed. |  |
| 4 | Navigate to the Object Page | Choose the required Item to navigate to the object detail page. | This displays the object detail page. |  |
| 5 | Update the Required Information | Choose to Receive on the top.Set the visual inspection appropriately.Select the storage location, for example, FORH | Entering the data. |  |
| 6 | Check for Errors | Choose Check | No errors would show if the simulation of goods receipt is complete without an error. |  |
| 7 | Confirm the Changes | Choose Confirm. | A milestone called Received at Remote is triggered in the Manage Logistics application.If the remote storage location entered during the receipt is cloud warehouse management enabled and packaging material was provided during the receipt at the base, a cloud warehouse management handling unit is created automatically.In addition, a warehouse task is created automatically with the source bin as GR-AREA and the destination bin as GENERAL-AREA. |  |
| 8 | Navigate to the Warehouse Task | Under the Business Documents facet, you can find warehouse task.To confirm or cancel the open warehouse task, user needs to login as warehouse_clerk_ewm and find the Process Warehouse Task app.In the Process Warehouse Task app, enter warehouse number as FORP and warehouse task as the warehouse task number and click on GO.Click on check for required warehouse task and click on confirm or cancel accordingly. | The page navigates to the Process Warehouse Task application.The source and the destination bin field have expected bin values. |  |
| 9 | Select and Confirm the Warehouse Task | Mark the warehouse task displayed on the list page and click Confirm. | Warehouse task status is changed to Confirmed. |  |

#### Issue to Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After a non-stock item is received at the (single) plant, the goods receipt and consumption is booked, but it might take some time until they are physically consumed by the order.

The user can execute this successive step with the action Issue-to-order in the Manage Logistics - Supplier Items (F5082) application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG) role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Logistics - Supplier Items (F5082).Enter the purchase order which was used in the previous step.Choose the required item to navigate to the object page. | The Manage Logistics screen is displayed. |  |
| 3 | Perform the Issue-to-Order Action | Click on Issue to Order. | A milestone called Issue to Order is created and the status of the item turns to Issued to Order. |  |

### Move to Stock at Remote (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to move the non-stock items to stock at remote if this is idle for a long period. This update is to be done using the Manage Logistics - Supplier Items (F5082) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to Fiori Launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG) role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the app Manage Logistics - Supplier Items (F5082). | The screen with section Arriving at Base is displayed. |  |
| 3 | Select the Purchase Order | Enter the purchase order, which was created earlier and status as Received at Remote. | This displays the list of items of the entered purchase order. |  |
| 4 | Navigate to Object Page | Select the required item to navigate to the object detail page. | This displays the object detail page. |  |
| 5 | Move to Stock (Optional) | Choose Move to Stock and fill in the below details:Product: FLOG-SP14 (example)Storage Location: FLBNGoods Movement Type: 501Choose Move to Stock. | The milestone will be updated with the value Moved to Stock at Remote and the status also will be set to Moved to Stock at Remote.If the storage location is warehouse managed enabled, then an inbound delivery is created else a goods movement document is created. These documents will be displayed in the business process flow section. |  |

### Process Return for Non-stock Items

#### Initiate Return

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can initiate returns for the non-stock Items. The following steps are applicable if the non-stock items are issued from the base and received at remote using the Process Cross-Plant Receipts (F4713) application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk (IOG). | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Application | Open Initiate Returns - By product (F4252) app. | The Initiate Returns screen is displayed. |  |
| 3 | Set Default Plant as an Application Setting | On the Initiate Returns screen, in the user settings for the app, choose App settings.This needs to be done only for the initial login (one-time setting).Enter the following details:Base Plant: FOBPRemote Plant: FORP | The base plant and remote plant are set.The message Base plant and remote plant set is displayed. |  |
| 4 | Select Remote Plant in Filter Settings | The plant is a mandatory filter, select the remote plant from drop-down list:Plant: FORP | The remote plant is set. |  |
| 5 | Select Return Item | Set the return status as At Remote, supply process as Non-stock Item.Choose Go.Select the line item for the non-stock Item, which is in status At Remote.Choose Chevron.Example: Machine1 | The non-stock items are displayed for which returns need to be initiated.The item navigates to the object page. |  |
| 6 | Enter Details to Initiate Returns | Choose Initiate Returns.Enter the below details on the object page, to request a return:Recommended Action: Return to VendorReference Maintenance Order (Optional)Comments (Optional)Returnable quantity in order unit: 1 EASave your changes. | Status of the return line updated to Return Scheduled.Milestone events are created and status is updated to Return Initiated in the Manage Logistics app.In the Manage Logistics App, you can also view the Actual End Date getting updated.A new return outbound delivery w/o reference is created and displayed in the document flow section.If packaging material was entered during the receipt at the base, a LE handling unit is created automatically and associated with the outbound delivery document created earlier. Additionally, all the items are fully packed by default to the handling unit created.If the remote storage location was entered during the receipt at remote and a cloud warehouse management handling unit was created, it will be reused to create pick warehouse tasks to initiate the return. A warehouse task is created automatically with the source bin as GR-AREA and the destination bin as GI-AREA.The Handling Unit section lists the default handling unit created. |  |
| 7 | Return Document Flow | Select the Return Document Flow tab. | Maintenance order (if existing), outbound delivery without reference warehouse task is displayed on the Return Document Flow tab. |  |

#### Create Additional Handling Units (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create handling units as per the need for the revised return packaging while initiating the return.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk (IOG). | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Application | Open Initiate Returns - By product (F4252) app. | The Initiate Returns screen is displayed. |  |
| 3 | Select Return Item | Set the return status as Return Scheduled, supply process as Non-stock Item Logistics.(If the field is not visible, select from Adapt Filters).Choose Go.Select the line item for the non-stock item, which is in the status Return Scheduled.Choose Chevron.Example: Machine1 | The non-stock items are displayed for which an additional handling unit is to be createdThe item navigates to the object page. |  |
| 4 | Delete Default Handling Unit | Go to the Handling Unit tab.Select the handling unit to be deleted from the list of handling unitsClick on the Delete HU button. | The handling unit gets successfully deleted and removed from the handling unit section. |  |
| 5 | Create Additional Handling Unites | Choose the button Maintain HUIn the Create Handling Unit popup enter the below details:Packaging material: XXXXQuantity to be packed: XClick on Create. | A popup appears to capture details to create a handling unit.On create, handling units are created successfully and listed on the Handling Unit section of the Initiate return object page.The system automatically also creates warehouse tasks for each handling unit If the remote storage location entered during the receipt at remote was cloud warehouse management enabled. |  |
| 6 | Return Document Flow | Select the Return Document Flow tab. | All the warehouse tasks are displayed on the Return Document Flow tab. |  |

#### Complete Open Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can change the warehouse task to complete the Process Warehouse Task application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to Fiori Launchpad | Log on to the SAP Fiori launchpad as Warehouse Clerk EWM. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Application | Open Process Warehouse Tasks app.Enter the purchase order which was used in the previous step.Choose the required item to navigate to the object page. | The page navigates the Process Warehouse Task application. |  |
| 3 | Enter Filter Values | Enter the warehouse number as FORP.Fill in the warehouse task numbers created in the previous step. | A list of warehouse tasks is displayed. |  |
| 4 | Select and Complete the Warehouse Task | Mark the warehouse task displayed on the list page and click on Confirm. | Warehouse task status is changed to Confirmed. |  |

#### Enter Load Quantity and Dispatch

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can initiate returns for the non-stock items.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to Fiori Launchpad | Log on to the SAP Fiori launchpad as Warehouse Clerk (IOG). | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Application | Open Initiate Returns - By product (F4252) app. | The Initiate Returns screen is displayed. |  |
| 3 | Select Remote Plant in Filter Settings | The plant is a mandatory filter, select the remote plant from drop-down list.Plant: FORP | The remote plant is set. |  |
| 4 | Select Return Item | Set the return status as Return Scheduled, supply process as Non-stock Item Logistics.(If the field is not visible, select from Adapt Filters).Choose Go.Select the line item for the non-stock item, which is in the status Return Scheduled.Choose Chevron.Example: Machine1 | The non-stock Items are displayed which have to be dispatched from base.The item navigates to the object page. |  |
| 5 | Enter Load Quantity | Choose Edit.Enter the below details on the object page for picking:Load quantity: 1 EA (should be the same as returnable quantity)Save your changes. | Status of the return line updated to Ready For Dispatch.Delivery updated with picked quantity. |  |
| 6 | Dispatch | Select the non-stock item with return status Ready for Dispatch.Choose Dispatch. | Return line updated to status Dispatched.Milestone events are created, and status is updated to Transport Initiated from Remote in the Manage Logistics - Supplier Items (F5082) app. |  |
| 7 | Return Document Flow | Select the Return Document Flow tab. | Maintenance order (if existing), outbound delivery without reference warehouse tasks are displayed on the Return Document Flow tab. |  |
| 8 | Print Label of Handling Unit (Optional) | Choose Print Label. | If you select Handling Unit Label checkbox and click the Print Label button, then the label will display ship to address, outbound delivery number, LE handling unit number, item type, maintenance order, purchase order, goods receipt date, and print date. The QR Code is also displayed along. |  |

### Receive Non-stock Items at Base

#### Receive Returned Non-stock Items at Base

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can receive the non-stock Items at the base that were dispatched from the remote location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk (IOG). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Cross-Plant Receipts (F4713) app. | The Process Cross-Plant Receipts screen is displayed. |  |
| 3 | Set the Plant | In the Process Cross-Plant Receipts screen, receiving plant is a mandatory setting.Enter Plant: FOBPChoose Go. | The container IDs dispatched from remote locations are displayed in the worklist. |  |
| 4 | Select Reference Document | Select the reference document number from Delivery Item tab. | Reference document has status Dispatched. |  |
| 5 | Scan Label (Optional) | Instead of manual selection, product or handling unit label can be scanned.Choose Scan to scan the barcode or the QR code. | Scanned values from the barcode is filtered and displayed in the list page.Note Handling unit label items, once scanned are auto received. Status is updated to Received on scanning. |  |
| 6 | Update Handling Decision (Optional) | Choose Edit.Handling decision is enabled for the product with status Dispatched.Verify the handling decision Return to Vendor / Return to Scrap / Return to Base Inventory.Choose Save. | Handling decision is set, but the product status remains same. |  |
| 7 | Update the Received Status | Select the product in the item list.Choose Receive. | Product status updated from Dispatched (Black) to Received (Green).The return purchase order with the outbound delivery document is created if the handling decision selected was Return to Vendor and the check box indicating the return delivery is selected.In case of any error the status is updated to Receipt in Process (Yellow).Note The handling decisions are defaulted based on recommended action. |  |
| 8 | Resend Notification to the Team (Optional) | Choose Notify. | A notification email is sent to the team of users as configured. |  |

#### Move to Stock at Base (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to move the non-stock items to stock back at base once received from return process. This update is to be done using the Manage Logistics - Supplier Items (F5082) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to Fiori Launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Logistics - Supplier Items (F5082) app. | The screen with section Arriving at Base is displayed. |  |
| 3 | Select the Purchase Order | Enter the purchase order, which was created earlier and status as Received Back at Base. | This displays the list of items of the entered purchase order. |  |
| 4 | Navigate to Object Page | Select the required item to navigate to the object detail page. | This displays the object detail page. |  |
| 5 | Move to Stock (Optional) | Choose Move to Stock and fill in the below details:Product: FLOG-SP14 (example)Storage Location: FLBNGoods Movement Type: 501Choose Move to Stock. | The milestone will be updated with the value Move to Stock and the status also will be set to Move to Stock.If the storage location is warehouse managed enabled, then an inbound delivery is created else a goods movement document is created. These documents will be displayed in the business process flow section. |  |

### Create Ad hoc Items (Optional)

Ad hoc items are free flowing items to be transported (for example, box of tools, luggage, medicine, gifts) which are not connected to any maintenance order or purchase order. Such items could be created and moved from a base to remote or from a remote plant to a base plant independently.

#### Create Ad hoc Item for Base to Remote

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An ad hoc item to be sent from a base plant to a remote plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG). | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori App | Open Manage Logistics - Supplier Items (F5082) app. | The Manage Logistics list page is displayed.Arriving at Base section is displayed. |  |
| 3 | Create an Ad hoc Item | Click on Create > Ad hoc Item . | Create ad hoc item popup screen is displayed. |  |
| 4 | Enter Data | Enter the below details:Description: Medicine BoxQuantity: 1Quantity Unit: EachSource Plant: FOBPSource Storage Location: FOBNDestination Plant: FORPRequired by Date: Any date in the future (3 days from today) | Data is entered. |  |
| 5 | Saving Ad hoc Item | Click on Create Ad hoc Item. | Ad hoc item is created at base plant FOBP. |  |
| 6 | Search Created Ad hoc Item | In the list page, enter the description which you entered above and click on Go. | The created ad hoc item will be displayed under Received at Base section.Ad hoc items are auto received and made ready for transport with an outbound delivery w/o reference, as soon as they are created. |  |
| 7 | Navigate to Object Page | Click on the item listed. | The milestone event will be Received at Base or Ready for Transport based on the outbound delivery picking status.In the business document section, you can see the outbound delivery created. |  |

#### Create Ad hoc Item for Remote to Base (Return)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An ad hoc item to be sent from a remote plant to a base plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG). | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori App | Open Manage Logistics - Supplier Items (F5082) app. | The Manage Logistics list page is displayed.Arriving at Base section is displayed. |  |
| 3 | Create an Ad hoc Item | Click on Create > Ad hoc Item . | Create ad hoc item popup screen is displayed. |  |
| 4 | Enter Data | Enter the below details:Description: Empty medicine box returnQuantity: 1Quantity Unit: EachSource Plant: FORPSource Storage Location: FOBNDestination Plant: FOBPRequired by Date: Any date in the future (3 days from today) | Data is entered. |  |
| 5 | Saving Ad hoc Item | Click on Create Ad hoc Item. | Ad hoc item is created at base plant FOBP. |  |
| 6 | Search Created Ad hoc Item | In the list page, enter the description which you entered above and click on Go. | The created ad hoc item will be displayed under Issued from Base section. |  |
| 7 | Navigate to Object Page | Click on the item listed. | The milestone event will be Return/Transfer Initiated.This item will be visible in Initiate Returns - By product (F4252) app with the status Return Scheduled.In the business document section, you can see the outbound delivery created. |  |

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
> Flagged while digesting this document, not verified: Remote receipt is tested with Process Receipts (F5316), and the overview table also lists F5316 for Receive at remote, but the same section says F5316 does not support remote receipt in the intercompany code scenario (F4713 recommended) and the return section assumes items were received at remote using F4713.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/test-script-field-logistics-planning-and-execution-40g-ae-sap-s-4hana-part-01]]
- related-to :: [[14-maintenance-service-and-projects/test-script-field-logistics-planning-and-execution-supplier-items-4ah]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5OM_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 102,085 chars in the whole document
