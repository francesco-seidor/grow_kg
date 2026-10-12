---
id: 14-maintenance-service-and-projects/test-script-field-logistics-planning-and-execution-supplier-items-4ah
title: "Test Script: Field Logistics Planning and Execution – Supplier Items (4AH_AE) (4AH_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 4AH_AE: supplier item and rental logistics from PO and receipt at base to remote, transfer, return and Fieldglass."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/field-logistics]
aliases: [4AH_S4CLD2608_BPD_EN_AE]
keywords: [Field Logistics Planning and Execution, supplier items, field logistics, test prerequisites, maintenance orders, limit purchase requisition, purchase orders, fieldglass integration, goods receipt, warehouse tasks]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4AH_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1008
topic: 14-maintenance-service-and-projects/field-logistics
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Field Logistics Planning and Execution – Supplier Items (4AH_AE) (4AH_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4AH_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Field Logistics Planning and Execution** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Field Logistics Planning and Execution – Supplier Items (4AH_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232854813)

[2 Prerequisites 5](#_Toc232854814)

[2.1 System Access 5](#_Toc232854815)

[2.2 Roles 5](#_Toc232854816)

[2.3 Master Data and Organizational Data 6](#_Toc232854817)

[2.4 Additional Manual Configuration 7](#_Toc232854818)

[2.5 Business Conditions 8](#_Toc232854819)

[3 Overview Table 9](#_Toc232854820)

[4 Test Procedures 10](#_Toc232854821)

[4.1 Option A: Create a Maintenance Order 10](#_Toc232854822)

[4.2 Option B: Create Project Demand 13](#_Toc232854823)

[4.2.1 Create Project 13](#_Toc232854824)

[4.2.2 Create Demand 14](#_Toc232854825)

[4.3 Create Limit PR for Rental / Renewal Extension (Optional) 15](#_Toc232854826)

[4.4 Create Purchase Order 17](#_Toc232854827)

[4.4.1 Create Purchase Order Without Hierarchy 17](#_Toc232854828)

[4.4.2 Create Hierarchy Purchase Order (Optional) 19](#_Toc232854829)

[4.4.3 Approve Purchase Order (Optional) 20](#_Toc232854830)

[4.5 Onboard Supplier Item via SAP Fieldglass (Optional) 21](#_Toc232854831)

[4.5.1 Add New Equipment as Worker to SOW 21](#_Toc232854832)

[4.5.2 Approve the Worker (as a Buyer) 22](#_Toc232854833)

[4.5.3 Verify the New Supplier Items in Field Logistics 23](#_Toc232854834)

[4.5.4 Fill Manifest Activities Item 24](#_Toc232854835)

[4.5.5 Verify Details of the Supplier Items in Field Logistics 25](#_Toc232854836)

[4.6 Create Supplier Item 26](#_Toc232854837)

[4.6.1 Option 1: Create Supplier Item from Purchase Order 26](#_Toc232854838)

[4.6.2 Option 2: Create Supplier Item from Manage Logistics 28](#_Toc232854839)

[4.7 Post Goods Receipt at Base Using 107 Movement Type Two-step GR Process (Optional) 29](#_Toc232854840)

[4.8 Update Supplier Item Details (Optional) 30](#_Toc232854841)

[4.9 Receipt at Base 31](#_Toc232854842)

[4.9.1 Review Item Status with Overview Dashboard (Optional) 31](#_Toc232854843)

[4.9.2 Process Receipt 32](#_Toc232854844)

[4.9.3 Review Outbound Delivery w/o Reference 35](#_Toc232854845)

[4.9.4 Review Warehouse Tasks 36](#_Toc232854846)

[4.9.5 Add Attachments (Optional) 38](#_Toc232854847)

[4.9.6 Goods Receipt Reversal (Optional) 39](#_Toc232854848)

[4.10 Single Plant Setup 40](#_Toc232854849)

[4.10.1 Create a Maintenance Order 40](#_Toc232854850)

[4.10.2 Create Purchase Order Without Hierarchy 42](#_Toc232854851)

[4.10.3 Receive at Base 43](#_Toc232854852)

[4.10.4 Issue to Order 46](#_Toc232854853)

[4.11 Release of Hold and Ready for Transport (Optional) 47](#_Toc232854854)

[4.11.1 Release of Hold in Maintenance Order 47](#_Toc232854855)

[4.11.2 Review Supplier Item Transport Ready Status 48](#_Toc232854856)

[4.11.3 Review Delivery Block Release in Outbound Delivery 49](#_Toc232854857)

[4.12 Post Goods Issue and Initiate Transport 50](#_Toc232854858)

[4.12.1 Complete Open Warehouse Tasks 50](#_Toc232854859)

[4.12.2 Post Goods Issue 51](#_Toc232854860)

[4.12.3 Initiate Transport from Base 52](#_Toc232854861)

[4.13 Receive Supplier Item at Remote 53](#_Toc232854862)

[4.13.1 Process Receipt 53](#_Toc232854863)

[4.13.2 Complete Open Warehouse Tasks 54](#_Toc232854864)

[4.14 Transfer Supplier Items to Another Remote Location (Optional) 56](#_Toc232854865)

[4.14.1 Initiate Transfer 56](#_Toc232854866)

[4.14.2 Transfer Approval (Optional) 57](#_Toc232854867)

[4.14.3 Cancel Transfer (Optional) 58](#_Toc232854868)

[4.14.4 Perform Transfer 59](#_Toc232854869)

[4.14.5 Receive Transferred Items 61](#_Toc232854870)

[4.15 Process Return for Supplier Items 62](#_Toc232854871)

[4.15.1 Initiate Return 62](#_Toc232854872)

[4.15.2 Create Additional Handling Units (Optional) 64](#_Toc232854873)

[4.15.3 Complete Open Warehouse Tasks 65](#_Toc232854874)

[4.15.4 Enter Load Quantity and Dispatch 66](#_Toc232854875)

[4.16 Receive Returned Supplier Items at Base 68](#_Toc232854876)

[4.17 Return to Supplier for Single Plant Setup 69](#_Toc232854877)

[4.18 Track Milestone Completion in Fieldglass 70](#_Toc232854878)

[4.19 Renew Rentals 71](#_Toc232854879)

## Purpose

Overview

This scope item supports the logistics process for services-related items, such as supplier items and rentals needed for maintenance operations or project-based demand. The process covers the receipt of these items at the supplying base, the logistics to the remote location, and the return process.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data, and business conditions.

### System Access

Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role.

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Maintenance Planner | SAP_BR_MAINTENANCE_PLANNER | Maintenance Planning | SAP_BR_MAINTENANCE_PLANNER |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Receiving Specialist (IOG) | SAP_BR_RCVG_SPECIALIST_IOG | Field Logistics Planning and Execution | SAP_BR_SC_ANALYST_IOG |  |
| Supply Chain Analyst (IOG) | SAP_BP_SC_ANALYST_IOG | Supply Chain Analyst (IOG) | SAP_BP_SC_ANALYST_IOG |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk (IOG) | SAP_BR_WAREHOUSE_CLERK_IOG | Field Logistics Planning and Execution | SAP_BR_SC_ANALYST_IOG |  |
| Project Financial Controller | SAP_BR_PROJ_FIN_CONTROLLER | SAP_BR_PROJ_FIN_CONTROLLER | SAP_BR_PROJ_FIN_CONTROLLER |  |
| Project Controller - Resourcing and Procurement | SAP_BR_PROJ_PROC_CONTROLLER | SAP_BR_PROJ_PROC_CONTROLLER | SAP_BR_PROJ_PROC_CONTROLLER |  |
| Administrator | SAP_BR_ADMINISTRATOR( Catalog- SAP_CA_BC_OC) | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC | SAP_BR_ADMINISTRATOR |  |
| Ariba Supplier |  | SAP Ariba Supplier |  |  |
| Fieldglass Supplier |  | Fieldglass Supplier |  |  |
| Fieldglass Buyer |  | Fieldglass Buyer |  |  |

### Master Data and Organizational Data

The organizational structure and master data of your company is created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. You can also use the following sample data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 | Company Code 3310 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Plant | FORP | Plant 2 AE (Remote Plant) | Flex.Org App extension |
| Storage Location | FORN | Std. storage 1 | Flex.Org App extension in Plant 2 AE |
| Storage Location | FORH | Std. storage 2 | Flex.Org App extension in Plant 2 AE |
| Shipping Point | FORP | Shipping Point FORP | Flex.Org App extension |
| Plant | FNRP | Plant 3 AE (Remote Plant) | Flex.Org App extension |
| Storage Location | FNRP | Std. storage 1 | Flex.Org App extension in Plant 3 AE |
| Sales Organization | FLPO | Sales Organization in Company 3310 | Flex.Org App extension |
| Purchase Organization | FLPO | Purchase Organization in Company 3310 | Flex.Org App extension |
| Plant | FOBP | Plant 4 AE (Base Plant) | Flex.Org App extension |
| Sales Organization | FOBP | Sales Organization in Company 3310 (Remote) | Flex.Org App extension |
| Service | FLOG-SERV | Field Logistics Sample Service |  |
| Supplier | VENPLPO | External Vendor |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/aa03a46f60af296a6e37304f67146d8d)

### Business Conditions

Before execution of this scope item, check whether the below scope items are active and the corresponding setup for those scope items is executed if required. These configuration steps are specific for your implementation. These include mandatory settings that are not delivered by SAP and must be created by you. For more information, refer to the document in the SAP Signavio Process Navigator.

List of dependent scope items that have to be active:

| Scope Item | Business Condition |
| --- | --- |
| 40G - Field Logistics Planning and Execution |  |
| BH1 - Corrective Maintenance |  |
| BMR - Scheduling Agreements in Procurement |  |
| BMK - Return to Supplier |  |
| 22Z - Procurement of Services |  |
| 4RF - Project Control – Resourcing and Procurement |  |
| 42K - Automation of Source-to-Pay with SAP Business Network - Optional |  |
| 4R2 - Service Procurement with SAP Business Network and SAP Fieldglass - Optional |  |

## Overview Table

This scope item consists of several process steps provided in the table below:

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Create Maintenance Order | Maintenance Planner | Create Maintenance Order | A maintenance order is created for the malfunction report. |
| Create Project | Project Financial Controller | Project Control - Enterprise Projects (F3215) | The project is created. |
| Create Demand | Project Controller - Resourcing and Procurement | Manage Project Demand (F4562) | The demand is created against the project. |
| Create Purchase Order from Purchase Requisition | Purchaser | Create Purchase Order - Advanced (ME21N) | A purchase order with a service line item is created. |
| Approve Purchase Order | Purchasing Manager | My Inbox - All Items (F0862) | The purchase order is approved. |
| Create Supplier Item | Receiving Specialist (IOG) | Manage Logistics - Supplier Items (F5082) | A supplier item is created. |
| Confirm Receipt at Base and Remote with Visual Inspection | Receiving Specialist (IOG) | Process Receipts - Stock and Non-stock items (F5316) | Receipt at the base and remote with the visual inspection done. |
| Pick Outbound Deliveries | Shipping Specialist | Change Outbound Delivery | Perform the picking task. |
| Process Warehouse Tasks at Base and Remote | Warehouse Clerk EWM | Process Warehouse Tasks | Confirm open warehouse tasks |
| Initiate Return for Supplier Items | Warehouse Clerk (IOG) | Initiate Returns - By product (F4252) | The return is initiated from remote. |
| Initiate and Cancel Transfers | Supply Chain Analyst (IOG) | Initiate Transfers (F6664) | The transfer is initiated or canceled. |
| View an Overview of the Received and Return Items | Receiving Specialist (IOG) | Receipts and Returns Overview (F5479) | Multiple cards show the rental or third-party items data. |
| Process Cross Plant Receipts | Warehouse Clerk (IOG) | Process Cross-Plant Receipts (F4713) | Receive items back at the base during returns or receive the transferred items from another remote. |

## Test Procedures

This section describes the test procedures for each process step that are executed as part of this scope item.

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
| 2 | Access the App | Open the app Create Maintenance Order app. | The Create Order screen is displayed. |  |
| 3 | Create Maintenance Order | On the Create Order screen, make the following entries:Select Order type: Corrective Maintenance YBA2Planning Plant: FORPChoose Continue. | The order type is selected. |  |
| 4 | Enter Details | On the Create Corrective Maintenance Order: %00000000001 screen, go to the General Data tab.Make the following entries:In the Responsibilities section:Work Center: FORP-PMWork Center Plant: FORP | The work center details are entered. |  |
| 5 | Define the Operations to be Performed to Resolve the Malfunction | Go to the Operation Data tab. You can see the operation overview in the Operations table for operation 0010: |  |  |
| 6 | Select Service | Choose the Services tab at the bottom of the screen.On the Service tab, you can create a service item either from Product Master, free text service item or both.Follow the steps below to create the items.Service item from Product Master:Product: FLOG-SERVQuantity: 1Unit: WKG/L Account: 52001000Hold On-Shore: XFree text service itemMaterial Group: P001Product: FLOG-SERVQuantity: 1Unit: WKPurchase Org: FLPOPurchase Group: 001G/L Account: 52001000Hold On-Shore: XNote Setting the flag Hold On-Shore to X is done for the hold scenarios. You can maintain a hold indicator for one or more service items within an operation. By doing this, any further delivery of the related physical items to the offshore plant will be blocked until the hold flag is cleared. | The service details are provided. |  |
| 7 | Check Entries | Choose Check Entries on the top left corner of the screen.You can edit the Service Start and End Date (Optional). | Entries have been checked. |  |
| 8 | Save Order | Choose Save. | Maintenance order 4000XXX is saved.Purchase request 1000XXXX is also created. |  |
| 9 | Phase Control Check (optional | Check the phase control status at header and operation level.Note Use of the phase control statuses TOH and TPOH is part of the Field Logistics functionality for holding and cross-docking. For necessary configuration and prerequisites refer to the setup guide of scope item 40G, as well as the SAP documentation. | The phase control on header level should have the active status:TOH in case all components of the order have the flag Hold On-Shore set.TPOH in case some components of the order have the flag Hold On-Shore set.Neither, in case no components have the flag set.The phase control on operation level should have the active status:TOH in case all components of the operation have the flag Hold On-Shore set.TPOH in case some components of the operation have the flag Hold On-Shore set.Neither, in case no items have the flag set. |  |
| 10 | Release Order | In the Set System Status menu, click on Release.Choose Save. | Status of this maintenance order changes to Rel. |  |
| 10 | Log out | Choose Sign Out. |  |  |

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

You can create a demand from the project.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Controller - Resourcing and Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the app Manage Project Demand (F4562). | The Manage Project Demand screen displays. |  |
| 3 | Create Demand | Choose Create, on the Services tab.On the New Demand screen, you can either create demand from material master data or use free text material.In the case of material master data, enter the following on the Demand tab:Demand Name: NewBoreDemandXXXWBS Element: NewBoreIDXXX(Enter the project ID created during project creation)Press Enter.Material: FLOG-SERVQuantity: 1Demand ID: XXXIn the case of free text material, enter the following on the Demand tab:Demand Name: NewBoreDemandXXXWBS Element: NewBoreIDXXX(Enter the project ID created during project creation)Press Enter.Material: FLOG-SERVQuantity: 1Demand ID: XXXDemand Type: Service MaterialPlant: FORPMaterial Group: YBMM01Purchasing Group: 001Purchasing Organization: FLPOClick on Create. | The New Demand screen displays. |  |
| 4 | Request the Demand | Search the newly created demand NewBoreDemandXXX, on the Services tab on the left side.Select the checkbox for the searched demand.Choose Change Demand Status > Request . | The purchase requisition is created. In the case of free text demand, the item description of PR will be the demand name (NewBoreDemandXXX). |  |

### Create Limit PR for Rental / Renewal Extension (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create a manual limit PR to support rental renewal. This can be used along with the above automatically created PR while creating a purchase order.

Using this limit PR, you can create a purchase order beyond the PMO or demand services dates and their quantities. Here are the two use cases:

1. While creating the first purchase order, you know that the planned quantities / dates in PMO / Demand are not going to be met, you can use this limit line in the purchase order. Follow the below procedure in this section to create the limit PR.
2. While creating the purchase order, you do not know about the rental renewal. In this case, if the service end date or quantity is getting over and you need to extend the service, then update the purchase order by creating a new service line item. Refer to section 4.12 for a detailed procedure.

You can create purchase requisition from project and demand flow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the app Manage Purchase Requisitions - Professional (F2229). | The list of existing purchase requisitions is displayed. You can search for an already created purchase requisition or create a new purchase requisition. |  |
| 3 | Create a New Limit PR | Click on Create. | The New Purchase Requisition screen displays. |  |
| 4 | Enter Header Details | Enter the following:Purchase Requisition Description: <limit PR data>Document Type: <purchase requisition (NB)> |  |  |
| 5 | Create Limit Item | In the Limit Items area, click on Create.Select the Service option.Enter the following details:Plant: FORPAccount Assignment Category: Order (FF)Item Description: Limit ItemOverall Limit: 10Expected Value: 10Desired Supplier: VENFLPOIn Requisition Period:Start Date: <select 1 week from today’s date>End Date: <select 2 weeks from today’s date>In the Account Assignments (1) details screen, enter the below data:G/L Account: 71100200Order: <the plant maintenance order number created in 4.1>Choose Apply.In Contact Information, enter the following:Purchasing Group: 001Choose Apply in the Item Details screen.Click on Create. | The Item Details screen displays. |  |

### Create Purchase Order

In this step we will create purchase orders with reference to purchase requisition created earlier. You can either create a normal, non-hierarchy purchase order or choose to create hierarchy purchase order if such feature is activated in your system.

#### Create Purchase Order Without Hierarchy

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can formalize a specific requirement for a service from the vendor by creating a purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the app Create Purchase Order - Advanced (ME21N). | The Create Order screen is displayed. |  |
| 3 | Create Order | On the Purchase Order screen, enter the details below.On the Item Overview tab:Purchase Requisition: XXXUse one of the three options to enter the purchase requisition number.Purchase requisition created during plant maintenance order or demand (applicable when the purchase order is created for the first time for any service)Limit PR created manuallyUse both purchase requisitions. Create two line items for adding the PR numbers.In line item1 enter the PR created during plant maintenance order or demand and in line item2 enter the limit PR.Press Enter.On the Basic Data tab:Supplier: VENFLPOPress Enter.On the Org. Data tab:Purchasing Org.: FLPOPress Enter.On the Item Detail tab, in the Invoice menu:Check Goods Receipt Bsd IVNet Price: 10Press Enter. | The purchase order details are provided. |  |
| 4 | Save Purchase Order | Choose Save. | The purchase order 45XXXXXXX is created. |  |

#### Create Hierarchy Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can formalize a specific requirement for a service from the vendor by creating a purchase order with hierarchy items.

An item hierarchy is a means of grouping items (services or materials) in purchasing documents. An item hierarchy can consist of one or multiple item sets with subitems. This way you can structure and sort your items.

For example, if you are purchasing materials and services for different departments of a company, you can use item hierarchies to group the items by department.

|  |
| --- |
| Note A hierarchy purchase order could only be created instead of normal purchase order where the procurement hierarchy feature is activated. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the app Create Purchase Order - Advanced (ME21N). | The Create Order screen is displayed. |  |
| 3 | Create Order | On the Purchase Order screen, enter the details below.Supplier: VENFLPOIn the header section:Purch. Org: FLPOPurch. Group: 001On the items section:Click on Create Item Set.Short Text: Item set for rentalSelect this item.Click on Create Hierarchy Item.On the Item Overview tab:Purchase requisition: XXXUse one of the three options to enter the purchase requisition number.Purchase requisition created during plant maintenance order or demand (applicable when the purchase order is created for the first time for any service).Limit purchase requisition (PR) created manuallyUse both purchase requisitions. Create two line-items for adding the purchase requisition numbers.In line item1 enter the purchase requisition created during plant maintenance order or demand and in line item2 enter the limit purchase requisition.Press Enter.In the Item Details section, under Account Assignment tab, enter below details:G/L Account: 52001000Cost Center: 17101101 | The purchase order details are provided. |  |
| 4 | Save Purchase Order | Choose Save. | The purchase order 45XXXXXXX is created. |  |

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

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the app My Inbox - All Items (F0862). | A list of existing purchase orders is displayed. |  |
| 3 | Search for Purchase Order | In the search criteria, enter the purchase order number and press Enter. | The purchase order is displayed. |  |
| 4 | Approve Purchase Order | Select the purchase order on the left side of the screen and choose Approve at the bottom right.Enter the approval reason (optional) and then choose Submit. | The Submit Decision screen is displayed.The purchase order is approved. |  |

### Onboard Supplier Item via SAP Fieldglass (Optional)

If customers have opted in for the scope item related to service procurement with Ariba network and SAP Fieldglass, the below steps in this section would be appliable. The scope enables an efficient process for the procurement of services between the purchaser and suppliers. It ensures a seamless procurement process with an emphasis on collaboration between buyers, purchasers, and services suppliers. It is assumed that all the pre-requisite setup instructions mentioned in the setup guide are completed to establish the connection between Fieldglass and Field Logistics in SAP S/4HANA.

During the above procurement flow, the service line of the purchase order will be transferred to Fieldglass as a Statement of Work (SOW) via the Ariba network. This SOW can be viewed in Fieldglass within both buyer and supplier personas.

#### Add New Equipment as Worker to SOW

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Suppliers identify rental or supplier-owned items to be required to complete a service. They add equipment as a worker to the SOW with all the required information for logistics execution.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on Fieldglass system with a Supplier role. | The SAP Fieldglass system is displayed. |  |
| 2 | Search for SOW Corresponding to Your Field Logistics Purchase Order | Search for SOW corresponding to your Field Logistics purchase order. | SOW is selected. |  |
| 3 | Choose the SOWs | Click on the SOW link. | A list of existing SOWs is displayed. |  |
| 4 | Verify the Details | Verify the details for example contract dates, budget amount. | Details should match with that of the Field Logistics service item. |  |
| 5 | Accept the SOW | Click on the button Accept. | Manage tab details will be displayed. |  |
| 6 | Add SOW Worker | Click on Add SOW worker link in the SOW worker section.First Name: Drilling MachineLast Name: 100 TonsWorker’s Email: Search for SOW Corresponding to Your Field Logistics<something@somecompany.com>Start Date: Today’s date (or a week from now)End Date: One month from today’s date.Display candidate’s workforce record to the buyer: NoClick on Add. | Worker details are added.Here in Fieldglass, adding a worker is like adding equipment in Field Logistics. |  |
| 7 | Add Attachment (Optional) | Click on Add Attachments.Click on Choose File and select the appropriate file.Click on Attach. |  |  |

#### Approve the Worker (as a Buyer)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The buyer needs to approve the worker to continue with the onboarding processes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on Fieldglass system with a Buyer role. | The SAP Fieldglass system is displayed. |  |
| 2 | Search for SOW Corresponding to Your Field Logistics Purchase Order | Search for SOW corresponding to your Field Logistics purchase order. | SOW is selected. |  |
| 3 | Choose the SOWs | Click on the SOW link. | A list of existing SOWs is displayed. |  |
| 4 | Approve Workorder | In the SOW worker section, click on Approve.On the popup, click on Approve. | Workorder details will be displayed. |  |

#### Verify the New Supplier Items in Field Logistics

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To check the supplier item created once the worker is added to the SOW.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the app Manage Logistics - Supplier Items (F5082). | The Manage Logistics screen is displayed. |  |
| 3 | Search for the New Supplier Item Created from Fieldglass | Search by the item description or serial number or purchase order item. | Note There might be a time delay in replicating the worker information from the Fieldglass system to supplier items in S/4HANA Field Logistics. If the items do not display even after, report the replication error where an integration expert would need to look at the integration points for possible errors.You will see the supplier item in Field Logistics. |  |

#### Fill Manifest Activities Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The supplier will complete the mandatory manifest activity item in the Fieldglass system. Through this supplier provides the mandatory details for example, product dimensions, serial number, dangerous goods. This updates back to Supplier Item in the Field Logistics system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on Fieldglass system with a Supplier role. | The SAP Fieldglass system is displayed. |  |
| 2 | SOWs are Listed | A list of SOWs is displayed. | A list of existing SOWs is displayed. |  |
| 3 | Search for SOW Corresponding to Your Field Logistics Purchase Order | Search for SOW corresponding to your Field Logistics purchase order. |  |  |
| 4 | Updating the Details | Select the worker.Go to activity items manifest (LN).Click on Mark as Complete.Pop up provides supplier item fields for example, dimension information, dangerous goods indicator.Fill all the values and update as Mark as Complete. | All the details for example, dimension, dangerous goods indicator will be updated. |  |

#### Verify Details of the Supplier Items in Field Logistics

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To check the supplier item details updated via manifest activity item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on Fieldglass system with a Receiving Specialist (IOG) role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the app Manage Logistics - Supplier Items (F5082). | The Manage Logistics screen is displayed. |  |
| 3 | Search for New Supplier Item Created from Fieldglass | Search by the item description or serial number or purchase order item. | Note There might be a time delay in replicating the worker information from the Fieldglass system to supplier items in Field Logistics. If the items do not display even after, report the replication error where an integration expert would need to look at the integration points for possible errors.You will see the supplier item here in Field Logistics. |  |
| 4 | View the Details | Navigate to the object page.Verify all the details replicated from the Fieldglass for example, item number, description, dimension details, weight, service start date, service end date, category of danger, rate. | All the details of Fieldglass are successfully replicated in Field Logistics with milestone event item created. | If attachment of a file is done in Fieldglass, then it will be visible in Manage Logistics - Supplier Items (F5082) app under Attachment section. |

### Create Supplier Item

|  |
| --- |
| Note This section of creation of supplier item becomes optional in case of Fieldglass integration for rental or third-party items. |

#### Option 1: Create Supplier Item from Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can add rental or third-party items as material items to purchase orders directly with special item categories. They will create rental or third-party supplier item records in the Manage Logistics app automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the app Change Purchase Order - Advanced (ME22N). | The Change Order screen is displayed. |  |
| 3 | Create New Item | On the Purchase Order screen, enter the details below.On the Item Overview tab, enter the following:Short text: CraneAccount assignment category: FItem category: R – Rental or V- Vendor ownedPO quantity: 1Quantity unit of measure: EAMaterial group: R001Plant: FOBPNote The product ID field will be left empty if there is no material master maintained for the rental items or select a material number if a material master is available.On the Account Assignment tab, enter the following:Order number (same as service line)Press Enter. |  |  |
| 4 | Save Purchase Order | Choose Save. | The purchase order 45XXXXXXX is updated.A new supplier item of type rental or third party is created in the Manage Logistics application.Note This will create the rental or third-party item in the Manage Logistics application. |  |

#### Option 2: Create Supplier Item from Manage Logistics

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to create a supplier item to represent the rental or third-party item required for service. This activity is done from the Manage Logistics - Supplier Items (F5082) application. This will also update the corresponding purchase order by creating a free text material item automatically. This item will be received and tracked in the entire logistics process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the app Manage Logistics - Supplier Items (F5082). | The Manage Logistics screen is displayed. |  |
| 3 | Create New Item | Click on Create.Enter the following for the supplier item:Purchase Order ID / Item: XXX(Enter the purchase order ID along with the item)Item typePackaging typeItem number: XXXX0011Note Enter the serial number or leave it blank if there are no material master is maintained for the rental items or select a product master material number if available.Description: Drilling Machine |  |  |
| 4 | Save Supplier Item | Choose Create. | The supplier item is created with a new purchase order line-item numberIn the purchase order, a new free text item is created with an item category as either R (rental item) or V (third party-owned) accordingly.Note If the purchase order is of type hierarchy item, then the rental or third-party item will be created under the same item set in which the selected service is present.Milestone event for this item is item created. |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement application. | The Post Goods Movement screen is displayed. |  |
| 3 | Choose the Process and Movement Type for Non-warehouse Managed Scenarios | Choose Goods Receipt.Choose Purchase Order.Enter the purchase order and movement type 107. | The goods receipt data is displayed on the screen. |  |
| 4 | Choose the Process and Movement Type for Non-inbound Delivery Scenario | Choose Goods Receipt.Choose Purchase Order.Enter the purchase order and movement type 107. | The goods receipt data is displayed on the screen. |  |
| 5 | Check and Verify the Details | Check and verify all the details like material, quantity, and storage location. | All details are checked. |  |
| 6 | Post Goods Receipt | Select the items for which a goods receipt is to be posted.Choose Post. | Goods receipt is posted.The system displays the message, material document xxx posted. |  |

|  |
| --- |
| Note After goods receipt with 107 is completed, then the next step 109 can be done from Process Receipts - Stock and Non-stock items (F5316) application. |

### Update Supplier Item Details (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can update the packaging material, storage location, and dimension information for the items in the Manage Logistics - Supplier Items (F5082) application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the app Manage Logistics - Supplier Items (F5082). | The Arriving at Base tab is displayed. |  |
| 3 | Select Purchase Order | Enter the purchase order, which was created in the [Create Purchase Order](#unique_15) [page ] 17 process. | The list of items of the entered purchase order is displayed. |  |
| 4 | Navigate to Object Page | Click on the required line item to navigate to the object page. | The object detail page is displayed. |  |
| 5 | Update the Missing Information if Known Already | Choose Edit.Enter the following details:Packaging Material: PMPALLETStorage Location: FOBW (EWM enabled) or FOBN (non EWM Enabled).Update the values for weight, length, width, height, and units. | The packaging, storage location and dimension information are updated. |  |
| 6 | Save the Changes | Choose Save. | The data is saved. |  |

### Receipt at Base

#### Review Item Status with Overview Dashboard (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can review the status of rental and third-party items using the Receipts and Returns Overview (F5479) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the app Receipts and Returns Overview (F5479). | The different cards of the view pages are displayed. |  |
| 3 | Select Rental Item Type in the Filter | Choose the item type filter value as Rental or Third-party Item. | The cards auto-refresh and load only rental or third-party data. |  |
| 4 | Analyze Different Cards Data and Navigate | Multiple cards show the rental or third-party items data. The cards delayed receipt, to be received and receipts show the rental items at different stages in the process.Choose a data set to navigate to from the card by clicking on a chart. | Application navigates to Process Receipts - Stock and Non-stock items (F5316) application and shows the data pre-populated. |  |

#### Process Receipt

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
| 1 | Log on to Fiori Launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Receipts - Stock and Non-stock items (F5316) app. | The screen with the section To Be Received is displayed. |  |
| 3 | Select the Purchase Order | Enter the purchase order, which was created in [Create Purchase Order](#unique_15) [page ] 17. | This displays the list of items that are in To Be Received status. |  |
| 4 | Navigate to the Object Page | Select the required item to navigate to the object page. | This displays the object detail page. |  |
| 5 | Update the Required Information | Choose Receive on the top.Enter the following details:Visual inspection: Passed / Passed – minor surface damages (Optional)Storage location: FOBWPackaging material: PMPALLETNote The goods receipt posting with 109 will be supported with only full quantity of the LE IBD and EWM IBD item for which 107 has happened.For example, in case 107 movement is already completed, the same quantity is updated for 109 movement and no further update is allowed in system. | Entered data is available in the respective fields. |  |
| 6 | Check for Errors | Choose Check. | No errors would show if the simulation of goods receipt completes without any error. |  |
| 7 | Confirm the Changes | Choose Confirm. | Go back to the list page of the Process Receipts - Stock and Non-stock items (F5316) app, you can see for the selected purchase order the received quantity as 1 under the Received tab.Choose Manage Logistics at the top right to navigate to the Manage Logistics app.Verify the documents created in the business document section. |  |
| 8 | Print Preview (Optional) | Choose Print Preview.Select Product Label and HU Label | This allows you to check the details and layout before printing.Product and handling unit label are displayed for all products.Product and handling unit label are displayed for all products..ProductProduct DescriptionGoods Receipt DateReceived QuantityOrder CategoryOrderGoods Receipt NumberPurchase Order/ItemVisual InspectionQuality Managed StatusItem TypePrint DateField Logistics StatusInstructionsHandling unit label displays following details:Outbound Delivery NumberHandling Unit NumberReceived QuantityPacked QuantityGoods Receipt NumberGoods Receipt DateItem TypePrint DateOrder CategoryOrder NumberOrder DescriptionGross WeightPurchase order/ItemsField Logistics StatusInstructionsNote Field logistics enables you to print instructions dynamically on Product label and Handling until label based on processes with respect to field logistics status. |  |
| 9 | Download | Click on Download. | The user can choose to download the Product label and HU label details from the print preview as an PDF file. |  |
| 10 | Trigger Output Management Queue | Click on Print.Select Product Label and HU Label | The Product Label and Handling Unit Label details are sent to the print queue without previewing the detailsIf the necessary configurations are maintained, Printing the labels will trigger an email notification as well.Details of the queue can be viewed from the Manage Output Items app.Note Field logistics supports extensibility which enables you to implement your custom logic in filling in the values for the custom fields added to the print label forms. |  |

#### Review Outbound Delivery w/o Reference

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once the supplier item is received at the base, a logistic execution outbound delivery without reference document is created automatically. Below are some variations of the use cases system supports based on the input during the process receipt.

- If supplying plant is different from the demand plant, an outbound delivery document w/o reference is created automatically. Additionally, items are fully picked up in the delivery automatically.
- If packaging material is entered during the receipt, a LE handling unit is created automatically and associated with the outbound delivery document created earlier. Additionally, all the items are fully packed by default to the handling unit created.
- If the maintenance work order item was created with Hold On-Site as Yes, a delivery block is set on the outbound delivery w/o reference with the blocking reason as Hold at Base (FL).

You can view the outbound delivery w/o reference document using the Display Outbound Delivery application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to Fiori Launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG). | The SAP Fiori launchpad displays. |  |
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

After a supplier Item is received at the base, to enable the minimum warehouse movements for a supplier Item, a cloud warehouse management enabled empty handling unit is created automatically. This is created in reference to a logistics execution handling unit. Below are some variations of the use cases system supports based on the input during the process of receipt.

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
| 3 | Navigate to the Warehouse Task | Under the Business Documents facet, you can find warehouse task.To confirm or cancel the open warehouse task, user needs to login as warehouse_clerk_ewm user and find the Process Warehouse Task app.In Process Warehouse Task app, give warehouse number as FOBP and warehouse task as the warehouse task number which found in Manage Logistics - Supplier Items (F5082) app and click on GO.Click on check for required warehouse task and click on confirm or cancel accordingly. | The page navigates the Process Warehouse Task application.The source and the destination bin field have expected bin values. |  |

#### Add Attachments (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can upload additional information as attachments to the items in the Manage Logistics - Supplier Items (F5082) application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the app Manage Logistics - Supplier Items (F5082).Enter the purchase order, which was used in the previous step.Choose the required item to navigate to the object page. | The Manage Logistics screen is displayed. |  |
| 3 | Upload File | Choose Edit.Go to Attachments and choose Upload.Upload a file. | The file is uploaded. |  |
| 4 | Add a Link | On the Attachments tab, choose to Add a Link.Follow the prerequisite steps provided below to add a URL link.NoteLogin as an Administrator to the app Maintain Protection Allowlists (F3195).In the Trusted Network Zones tab, choose Plus (+) to add a new entry.Enter a Website Domain name, Schema (as HTTP / HTTPS) and Port (as *)Enter the URL and Description of the link. | The link is attached. |  |
| 5 | Save the Entries | Choose Save. | The data is saved. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the app Process Receipts - Stock and Non-stock items (F5316). | The To be Received tab is displayed. |  |
| 3 | Select Purchase Order | Enter the Purchase Order which was created in the [Process Receipt](#unique_32) [page ] 32 process. | This displays the items on the Received tab. |  |
| 4 | Navigate to Object Page | Click on the required line item to navigate to the object page. | This displays the object page. |  |
| 5 | Reverse Goods Receipt | Choose Reverse at the top.Select the Posting Date.Enter Additional Note.Choose Reverse. | Goods receipt reversal popup is displayed for two-step reverse wizard in case warehouse task and handling unit is existing for an item.It will cancel the open warehouse task.It will delete the Handling unit assigned to outbound delivery.Goods receipt reversal is posted.On refresh, the status changes to Cancelled Receipt At Base.In the worklist of the Process Receipts - Stock and Non-stock items (F5316) app, this purchase order gets listed on the To Be Received tab.In the Manage Logistics app, the milestone and status are set to Cancelled Receipt At Base. |  |

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
| 2 | Access the App | Open Create Maintenance Order app | The Create Order screen is displayed. |  |
| 3 | Create Maintenance Order | On the Create Order screen, choose Order type: Preventive Maintenance YBA2, Planning Plant: FOBP and then choose Continue. | The order type is selected. |  |
| 4 | Enter the Details | On the Create Preventive Maintenance Order: %00000000001 screen, go to the General Data tab.Make the following entries:In the Responsibilities section,Work Center: FOBP-PMWork Center Plant: FOBP | The work center details are entered. |  |
| 5 | Define the Operations to be Performed to Resolve the Malfunction | Go to the Operation Data tab. You can see the operation overview in the Operations table for operation 0010. | Selecting the item number. |  |
| 6 | Select Material | Choose Services tab at the bottom of the screen.On the Services tab, you can create a service item either from Product Master or Free Text Service Item, or both.Below are the steps to create these items.Service item from Product Master.Product: FLOG-SERVQuantity: 1Unit: WKG/L Account: 52001000Free text service itemMaterial: P001Product: FLOG-SERVQuantity: 1Unit: WKPurchasing Org: FLPOPurchasing Group: 001G/L Account: 52001000 | Item material details are entered. Item category should be defaulted to N and Field Logistics supply process should be defaulted to SP15 for all options. |  |
| 7 | Check Entries | Choose Check Entries on the top left corner of the screen.You can edit service start and end date (optional). | Entries have been checked. |  |
| 8 | Save Order | Choose Save. | Maintenance Order 4000XXX is saved. Purchase Request 1000XXXX is also created. |  |
| 9 | Release Order | In the Set System Status menu, choose Release.Choose Save. | Status of this maintenance order changes to Rel. |  |
| 10 | Log Out | Choose Sign Out. |  |  |

#### Create Purchase Order Without Hierarchy

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can formalize a specific requirement for a service from the vendor by creating a purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the app Create Purchase Order - Advanced ME21N | The Create Order screen is displayed. |  |
| 3 | Create Order | On the Purchase Order screen, enter the details below.3. In Item Overview tab:Purchase Requisition: XXXUse Purchase requisition created during plant maintenance order or demand (applicable when the purchase order is created for the first time for any service).Press Enter.In Basic Data tab:Supplier:VENFLPOPress Enter.In Org. Data tab:Purchasing Org: FLPOPress Enter.In Item Detail tab, Invoice menu:Check Goods Receipt Bsd IVNet Price: 10Press Enter. | The purchase order details are provided. |  |
| 4 | Save Purchase Order | Choose Save. | The purchase order 45XXXXXXX is created. |  |

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
| 5 | Update the Required Information | Choose to Receive button on the top.Choose below details:Visual inspection: Passed / Passed – minor surface damagesStorage location: FOBW.Packaging Material: PMPALLET.Immediate issue to Maint. Order: X (optional)Note The field Immediate Issue to Maintenance Order will only be available for the user to update for rental items ordered for a single plant scenario plant (supplying plant = demand plant). Users can choose this option to additionally consume the item along with the receipt in a single step. If this flag is set, the next step of issuing to order is obsolete. | Entered data is available in the respective fields. |  |
| 6 | Check for Errors | Choose Check. | No errors would show if the simulation of goods receipt completes without any error. |  |
| 7 | Confirm the Changes | Choose Confirm. | If you go back to the list page of this Process Receipt app, you can see under the selected purchase order the received quantity is 20 under the Received tab. Whereas you cannot find the selected Purchase Oder entry under the To Be Received tab.You can navigate to the Manage Logistics app by clicking the Manage Logistics on the top of the object page and verifying the documents under the Business Document section. |  |
| 8 | Print Preview | Choose Print.Select Product Label and HU Label | This will allow you to check the details and layout before printing.Product and handling unit label are displayed for all materials.Product and handling unit label are displayed for all materials.ProductProduct DescriptionGoods Receipt DateReceived QuantityOrder CategoryOrderGoods Receipt NumberPurchase Order/ItemVisual InspectionQuality Managed StatusItem TypePrint DateField Logistics StatusInstructionsHandling unit label displays following details:Outbound Delivery NumberHandling Unit NumberReceived QuantityPacked QuantityGoods Receipt NumberGoods Receipt DateItem TypePrint DateOrder CategoryOrder NumberOrder DescriptionGross WeightPurchase order/ItemsField Logistics StatusInstructionsNote Field logistics enables you to print instructions dynamically on Product label and Handling until label based on processes with respect to field logistics status. |  |
| 9 | Download | Click on Download | The user can choose to download the Product label and HU label details from the print preview as an PDF file. |  |
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

After a rental item is received at the (single) plant, the goods receipt and consumption is booked, but it might take some time until they are physically consumed by the order.

The user can execute this successive step with the action Issue-to-order in the Manage Logistics - Supplier Items (F5082) application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG) role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Logistics - Supplier Items (F5082).Enter the purchase order which was used in the previous step.Choose the required item to navigate to the object page. | The Manage Logistics screen is displayed. |  |
| 3 | Perform the Issue-to-Order Action | Click on Issue to Order. | A milestone called Issue to Order is created and the status of the item turns to Issued to Order. |  |

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
| 4 | Locate the Service for which the Hold Indicator is to be Changed | Go to the Operation Data > Services tab. You can see all the items displayed in the change mode. |  |  |
| 5 | Change and Save | Locate the service line for which the hold indicator is to be removed and make the below changes:Hold On-Shore: uncheck |  |  |
| 6 | Save Order | Choose Save. | Maintenance order 4000XXX is saved. |  |

#### Review Supplier Item Transport Ready Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can view the supplier item status changed in the Manage Logistics - Supplier Items (F5082) application.

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

.

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
| 3 | Navigate to the Warehouse Task | Under the Business Documents facet, you can find warehouse task.To confirm or cancel the open warehouse task, user needs to login as warehouse_clerk_ewm user and find the Process Warehouse Task app.In Process Warehouse Task app, give warehouse number as FOBP and warehouse task as the warehouse task number which found in Manage Logistics - Supplier Items (F5082) app and click on GO.Click on check for required warehouse task and click on confirm or cancel accordingly. | The page navigates the Process Warehouse Task application.The source and the destination bin field have expected bin values. |  |
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

### Receive Supplier Item at Remote

#### Process Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can receive the item at the destination location and mark the item as Received.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG) role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Receipts - Stock and Non-stock items (F5316) app. | The To Be Received tab is displayed. |  |
| 3 | Select the Purchase Order | Enter the purchase order which was created in the step Create Purchase Order. | The list of items, which are in the To Be Received status is displayed. |  |
| 4 | Navigate to the Object Page | Choose the required Item to navigate to the object detail page. | This displays the object detail page. |  |
| 5 | Update the Required Information | Choose to Receive on the top.Set the visual inspection appropriately.Select the storage location as FORH.Note The field Immediate Issue to Maint. Order is selected by default. The items will be issued once they are received, and hence they will not be available for an Initiate Transfer. (Refer to[Transfer Supplier Items to Another Remote Location (Optional)](#unique_52) [page ] 56 ) | Entering the data. |  |
| 6 | Check for Errors | Choose Check. | No errors would show if the simulation of goods receipt is complete without an error. |  |
| 7 | Confirm the Changes | Choose Confirm. | A milestone called Received at Remote is triggered in the Manage Logistics application.If the remote storage location entered during the receipt is cloud warehouse management enabled and packaging material was provided during the receipt at the base, a cloud warehouse management handling unit is created automatically.In addition, a warehouse task is created automatically with the source bin as GR-AREA and the destination bin as GENERAL-AREA. |  |

#### Complete Open Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After a supplier Item is received at the remote, to enable the minimum warehouse movements for a supplier item, a Cloud Warehouse Management enabled empty handling unit is created automatically. Below are some variations of the use cases system supports based on the input during the process of receipt.

- If the remote storage location entered during the receipt is Cloud Warehouse Management enabled and packaging material is provided, a Cloud Warehouse Management handling unit is created automatically.
- A warehouse task is created automatically with the source bin as GR-AREA and the destination bin as GEN-AREA.

You can change the warehouse task to complete the Process Warehouse Task application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a user with Receiving Specialist (IOG) role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Logistics - Supplier Items (F5082).Enter the purchase order which was used in the previous step.Choose the required item to navigate to the object page. | The Manage Logistics screen is displayed. |  |
| 3 | Navigate to the Warehouse Task | Under the Business Flow Diagram, there will be remote warehouse task tile with the respective warehouse task number.To confirm or cancel the open warehouse task, user needs to login warehouse_clerk_ewm user and find the Process Warehouse Task app.In Process Warehouse Task app, give warehouse number as FORP and warehouse task as the warehouse task number which can be found in Manage Logistics - Supplier Items (F5082) app and click on GO.Click on check for required warehouse task and click on confirm or cancel accordingly. | The page navigates to the Process Warehouse Task application.The source and the destination bin field have expected bin values. |  |
| 4 | Select and Complete Warehouse Task | Mark the warehouse task displayed on the list page and click on Confirm. | Warehouse task status is changed to Confirmed. |  |
| 5 | Perform Issue to Order | Log on to the SAP Fiori launchpad as a user with Receiving Specialist (IOG)Open Manage Logistics - Supplier Items (F5082).Enter the purchase order which was used in the previous step.Choose the required item to navigate to the object page.Click on Issue to Order | Issue to order completed successfully. |  |

### Transfer Supplier Items to Another Remote Location (Optional)

Supplier items are often reused between service operations and hence be transferred from one offshore location to another. The below process steps allow the initiation and transfer of supplier items.

#### Initiate Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can initiate the transfer of a supplier item using the Initiate Transfers application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Supply Chain Analyst (IOG) role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Initiate Transfers (F6664).Enter the purchase order which was used in the previous step.Choose the required item to navigate to the object page. | The object page is displayed. |  |
| 3 | Initiate the Transfer | Click on the Initiate Transfer. | A popup appears to capture the details. |  |
| 4 | Complete the Input and Confirm | Enter below details:Requesting purchase order: 40XXXXXXXRequesting plant: FNRPClick on Confirm.Note For necessary plant configuration and master data, refer the steps mentioned for plant FORP in the setup guide of scope item 40G | The transfer is initiated successfully.As part of this step below business, documents have been updated automatically.A new supplier Item material line gets created on the requesting service purchase order for the current remote plant.A milestone called Transferred to another Purchase Order is registered against the source supplier item. A new supplier item is created with reference to the requesting purchase order with the milestone Transfer Initiated.A goods receipt with goods movement (101) is triggered for the new material item to mark the consumption to the requesting a purchase order.A LE Outbound deliver w/o reference document is created for the Supplier Item at the current remote plant to begin the logistics transfer. |  |
| 5 | Access the New Supplier Item | On the search filter, enter the requesting purchase order which was used in the initiate transfer step.Choose the required item to navigate to the object page. | The object page is displayed. |  |
| 6 | Navigate to Manage Logistics from the Object Page | Navigate to the object page of the transfer ItemUnder the related apps section on the top header click on the Manage Logistics. | The user navigates to the object page of the Manage Logistics application. |  |
| 7 | Verify the Expected Results Mentioned the Step 4 | Verify the below information:Purchase orderLatest milestoneStatusOutbound deliveryGoods receipt documentParent supplier item | Requesting purchase order with the new item is displayed on the header area:Latest milestone: Transfer InitiatedStatus: Received at RemoteOutbound delivery: XXXXXXGoods receipt document: XXXXXXXParent supplier item: <hyperlink for the item number> |  |

|  |
| --- |
| Note In case outbound delivery is deleted using Change Outbound Delivery application or outbound delivery creation failed due to other reason, in such cases outbound delivery can be created using action Create Outbound Delivery from Initiate Transfer application. |

#### Transfer Approval (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can send the transfer request for approval depending on customizing. Refer to setup guide for more details on the customization.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Transfer Approval user.Note Refer 4AH setup guide for username. | The SAP Fiori launchpad displays. |  |
| 2 | Access My Inbox | Navigate to My Inbox tab. | You can see all the approvals. |  |
| 3 | Select Approval Record | Select the appropriate record for approval or rejection. | You can see the details on the detail page on right side. |  |
| 4 | Perform Approve or Reject. | Perform the action Approve or Reject.Enter decision note and click on Submit. | On approval, this purchase order item will be created in the target purchase order. |  |

#### Cancel Transfer (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can cancel the transfer until the supplier item is dispatched from the current remote plant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Supply Chain Analyst (IOG) role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Initiate Transfers (F6664).Enter the requesting purchase order which was used in the initiate transfer step.Choose the required item to navigate to the object page. | The object page is displayed. |  |
| 3 | Cancel the Transfer | Click on the Cancel Transfer. | A popup appears to reconfirm the cancellation.On click on Confirm, the success message Transfer Cancelled successfully is displayed. |  |
| 4 | Access the Previous Supplier Item | On the search filter, enter the source purchase order which was used before the initiate transfer step.Choose the required item to navigate to the object page. | The object page is displayed. |  |
| 5 | Navigate to Manage Logistics from the Object Page | Navigate to the object page of the transfer item.Under the related apps section on the top header click on the Manage Logistics. | The user navigates to the object page of the Manage Logistics application. |  |
| 6 | Verify the Expected Results Mentioned the Step 4 | Verify the below information:Purchase orderLatest milestoneStatusOutbound deliveryGoods receipt document | Original purchase order with the new item is displayed on the header area:Latest milestone: Transfer CancelledStatus: Received at RemoteOutbound delivery: XXXXXXGoods receipt document: XXXXXXX |  |

#### Perform Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can perform the additional steps to execute the transfer for the supplier items from the Initiate Returns - By product (F4252) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk (IOG). | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Application | Open Initiate Returns - By product (F4252) app. | The Initiate Returns screen is displayed. |  |
| 3 | Set Default Plant as an Application Setting | On the Initiate Returns screen, in the user settings for the app, choose App settings.This needs to be done only for the initial login (one-time setting)Enter the below details:Base plant: FOBPRemote plant: FORP | The base plant and remote plant are set.The message base plant and remote plant set is displayed. |  |
| 4 | Select Remote Plant in Filter Settings | The plant is a mandatory filter, select the remote plant from drop-down list.Plant: FORP | The remote plant is set. |  |
| 5 | Select Supplier Item | Set the status as Transfer Scheduled, supply process as Services: Supplier Item Logistics.(If the field is not visible, select from Adapt Filters).Choose Go.Choose Chevron.Example: Machine1 | The supplier items are displayed for which transfer action needs to be performed.The item navigates to the object page. |  |
| 6 | Enter Load Quantity | Choose Edit.Enter the below details on the object page, for picking:Load quantity: 1 EA (should be the same as returnable quantity)Save your changes. | Status of the line updated to Ready for Dispatch.Delivery updated with picked quantity. |  |
| 7 | Dispatch | Select the supplier item with the status Ready for Dispatch.Choose Dispatch. | Return line updated to status Dispatched.Milestone events are created, and status is updated to Transport Initiated from Remote in the Manage Logistics - Supplier Items (F5082) app. |  |
| 8 | Document Flow | Choose Chevron for the product.Example: Machine1Select the Return Document Flow tab. | The page navigates to the object page.The maintenance order (if existing) and outbound delivery without reference lane is displayed on the Return Document Flow tab. |  |

#### Receive Transferred Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can receive the items at the remote that were transferred from another remote.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk (IOG). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Cross-Plant Receipts (F4713) app. | The Process Cross-Plant Receipts screen is displayed. |  |
| 3 | Set the Plant | In the Process Cross-Plant Receipts screen, receiving plant is a mandatory setting.Enter Plant: FNRPChoose Go | The container IDs dispatched from remote locations are displayed in the worklist. |  |
| 4 | Select Reference Document | Select the reference document number from Delivery Item tab. | Reference document has status Dispatched. |  |
| 5 | Scan Label (Optional) | Instead of manual selection, product or handling unit label can be scanned.Choose Scan to scan the barcode or the QR code. | Scanned values from the barcode is filtered and displayed in the list page.Note Handling unit label items, once scanned are auto received. Status is updated to Received on scanning. |  |
| 6 | Update Handling Decision (Optional) | Choose Edit.Handling decision is enabled for the product with status Dispatched.Set the handling decision as Set to Usage.Choose Save. | Handling decision is set, but the product status remains same. |  |
| 7 | Update the Received Status | Select the product in the item list.Choose Receive. | Product status updated from Dispatched (Black) to Received (Green).In case of any error the status is updated to Receipt in Process (Yellow).Note The handling decisions are defaulted based on recommended action. |  |
| 8 | Resend Notification to the Team (Optional) | Choose Notify. | A notification email is sent to the team of users as configured. |  |

### Process Return for Supplier Items

#### Initiate Return

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can initiate returns for the supplier Items. The following steps are applicable if the supplier items are issued from the base and received at remote using the Process Cross-Plant Receipts (F4713) application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk (IOG). | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Application | Open Initiate Returns - By product (F4252) app. | The Initiate Returns screen is displayed. |  |
| 3 | Set Default Plant as an Application Setting | On the Initiate Returns screen, in the user settings for the app, choose App settings.This needs to be done only for the initial login (one-time setting).Enter the following details:Base Plant: FOBPRemote Plant: FORP | The base plant and remote plant are set.The message Base plant and remote plant set is displayed. |  |
| 4 | Select Remote Plant in Filter Settings | The plant is a mandatory filter, select the remote plant from drop-down list:Plant: FORP | The remote plant is set. |  |
| 5 | Select Return Item | Set the return status as At Remote, supply process as Services: Supplier Item Logistics.(If the field is not visible, select from Adapt Filters).Choose Go.Select the line item for the supplier item, which is in status At Remote.Choose Chevron.Example: Machine1 | The supplier items are displayed for which returns need to be initiated.The item navigates to the object page. |  |
| 6 | Enter Details to Initiate Returns | Choose Initiate Returns.Enter the below details on the object page, to request a return:Recommended Action: Return to VendorReference Maintenance Order (Optional)Comments (Optional)Returnable quantity in order unit: 1 EASave your changes. | Status of the return line updated to Return Scheduled.Milestone events are created, and status is updated to Return Initiated in the Manage Logistics app.In the Manage Logistics App, you can also view the Actual End Date getting updated.A new return outbound delivery w/o reference is created and displayed in the document flow section.If packaging material was entered during the receipt at the base, a LE handling unit is created automatically and associated with the outbound delivery document created earlier. Additionally, all the items are fully packed by default to the handling unit created.If the remote storage location was entered during the receipt at remote and a cloud warehouse management handling unit was created, it will be reused to create pick warehouse tasks to initiate the return. A warehouse task is created automatically with the source bin as GR-AREA and the destination bin as GI-AREA.The Handling Unit section lists the default handling unit created. |  |
| 7 | Return Document Flow | Select the Return Document Flow tab. | Maintenance order (if existing), outbound delivery without reference warehouse task are displayed on the Return Document Flow tab. |  |

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
| 3 | Select Return Item | Set the return status as Return Scheduled, supply process as Services: Supplier Item Logistics.(If the field is not visible, select from Adapt Filters).Choose Go.Select the line item for the supplier item, which is in the status Return Scheduled.Choose Chevron.Example: Machine1 | The supplier items are displayed for which an additional handling unit is to be createdThe item navigates to the object page. |  |
| 4 | Delete Default Handling Unit | Go to the Handling Unit tab.Select the handling unit to be deleted from the list of handling unitsClick on the Delete HU button. | The handling unit gets successfully deleted and removed from the handling unit section. |  |
| 5 | Create Additional Handling Unites | Choose the button Maintain HU.In the Create Handling Unit popup enter the below details:Packaging material: XXXXQuantity to be packed: XClick on Create. | A popup appears to capture details to create a handling unit.On create, handling units are created successfully and listed on the Handling Unit section of the Initiate return object page.The system automatically also creates warehouse tasks for each handling unit If the remote storage location entered during the receipt at remote was cloud warehouse management enabled. |  |
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

You can initiate returns for the supplier items.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to Fiori Launchpad | Log on to the SAP Fiori launchpad as Warehouse Clerk (IOG). | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Application | Open Initiate Returns - By product (F4252) app. | The Initiate Returns screen is displayed. |  |
| 3 | Select Remote Plant in Filter Settings | The plant is a mandatory filter, select the remote plant from drop-down list.Plant: FORP | The remote plant is set. |  |
| 4 | Select Return Item | Set the return status as Return Scheduled, supply process as Services: Supplier Item Logistics.(If the field is not visible, select from Adapt Filters).Choose Go.Select the line item for the supplier item, which is in the status Return Scheduled.Choose Chevron.Example: Machine1 | The supplier items are displayed which have to be dispatched from base.The item navigates to the object page. |  |
| 5 | Enter Load Quantity | Choose Edit.Enter the below detail on the object page for picking:Load quantity: 1 EA (should be the same as returnable quantity)Save your changes. | Status of the return line updated to Ready For Dispatch.Delivery updated with picked quantity. |  |
| 6 | Dispatch | Select the supplier item with return status Ready for Dispatch.Choose Dispatch. | Return line updated to status Dispatched.Milestone events are created, and status is updated to Transport Initiated from Remote in the Manage Logistics - Supplier Items (F5082) app. |  |
| 7 | Return Document Flow | Select the Return Document Flow tab. | Maintenance order (if existing), outbound delivery without reference warehouse tasks are displayed on the Return Document Flow tab. |  |
| 8 | Print Label of Handling Unit (Optional) | Choose Print Label. | If you select Handling Unit Label checkbox and click the Print Label button, then the label will display ship to address, outbound delivery number, LE handling unit number, item type, maintenance order, purchase order, goods receipt date, and print date. The QR Code is also displayed along. |  |

### Receive Returned Supplier Items at Base

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can receive the supplier items at base that were dispatched from remote.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (IOG). | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori App | Open Process Cross-Plant Receipts (F4713) app. | The Process Cross-Plant Receipts screen is displayed. |  |
| 3 | Set the Plant | In the Process Cross-Plant Receipts screen, receiving plant is a mandatory setting.Enter Plant: FOBPClick on Go. | The container IDs dispatched from remote locations are displayed in the worklist. |  |
| 4 | Select Reference Document | Select the reference document number from Delivery Item tab. | Reference document has status Dispatched. |  |
| 5 | Scan Label (Optional) | Instead of manual selection, product or handling unit label can be scanned.Choose Scan to scan the barcode or the QR code. | Scanned values from the barcode is filtered and displayed in the list page.Note Handling unit label items, once scanned are auto received. Status is updated to Received on scanning. |  |
| 6 | Update Handling Decision (Optional) | Choose Edit.Handling decision is enabled for the product with status Dispatched.Select handling decision Return to Vendor from dropdown.Choose Save. | Handling decision is set, but the product status remains same. |  |
| 7 | Update the Received Status | Select the product in the item list.Choose Receive. | Product status updated from Dispatched (Black) to Received (Green).The Manage Logistics - Supplier Items (F5082) application will register a milestone Return to Supplier Initiated for the corresponding item.A movement type of 122 - Return to Vendor is posted against the original purchase order item.In case of any error, the status is updated to Partially Processed (Yellow).Note The handling decisions are defaulted based on recommended action. |  |
| 8 | Resend Notification to the Team (Optional) | Choose Notify. | A notification email is sent to the team of users as configured. |  |

### Return to Supplier for Single Plant Setup

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Self-sufficient plants are those plants where supply and demand lie within the same plant. You should make the required configuration mentioned in the setup guide to make a plant self-sufficient.

The return process of the supplier items issued to an order belonging to a self-sufficient plant is different from the normal multiple plant scenario. Below are the steps for such a return process.

You can return the supplier item using the action return to supplier in the Manage Logistics - Supplier Items (F5082) application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist (IOG). | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori App | Open Manage Logistics - Supplier Items (F5082) app.Enter the purchase order item associated with the supplier item.Choose the required item to navigate to the object page. | The Manage Logistics object page is displayed. |  |
| 3 | Perform the Return | Click on Return to Supplier. | The Manage Logistics application will register a milestone Return to Supplier Initiated for the corresponding item.A movement type of 122 – Return to Vendor is posted against the original purchase order item. |  |

### Track Milestone Completion in Fieldglass

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If the customers have opted in for the scope item related to service procurement with Ariba network and SAP Fieldglass, the below steps in this section would be appliable. During the flow number of major milestones actions for example, Received at Base, Transport Initiated to Remote, Return Initiated, Return to Supplier Initiated are triggered in the Field Logistics system. The integration with the Fieldglass system ensures that all such milestones are replicated back to the corresponding SOW in the Fieldglass system as completed activity items. This SOW along with the activity items can be viewed in Fieldglass in both buyer and supplier personas.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on Fieldglass system with a Supplier or Buyer role. | The SAP Fieldglass system is displayed. |  |
| 2 | Choose the SOWs | Click on the SOW link. | A list of existing SOWs is displayed. |  |
| 3 | Search for SOW Corresponding to Your Field Logistics Purchase Order | Search for SOW corresponding to your Field Logistics purchase order. | SOW is selected. |  |
| 4 | See all the Available Activity Items with their Statuses | Click on the SOW Worker menu.Click on Worker ID.Click on the Manage menu. | All the milestone events are visible with Completed Statues. |  |

### Renew Rentals

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the rental service period is completed, you have to extend the rental service period with the service provider. You can renew or extend the purchase order with the service provider (supplier), by including the below limit Item PR while creating the purchase order in step “Create Purchase Order”. Below are the steps to create a service limit PR.

You can use this new service line item for extended service billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the app Manage Purchase Requisitions - Professional (F2229). | The Manage Purchase Requisition professional screen is displayed. |  |
| 3 | Create a Limit PR | Click on Create. | New purchase requisition screen will open. |  |
| 4 | Enter General Information Data | Purchase Requisition Description: Limit PRDocument Type: Purchase Requisition (NB) | General information data is entered. |  |
| 5 | Create Limit Item | Click on Create under section Limit Items by selecting Service as an option. | Purchase Requisition Item screen will open. |  |
| 6 | Enter Purchase Requisition Item Details | Enter below data:Plant: FORPAccount Assignment Category: Order (F)Item Description: Limit ItemOverall Limit: 1000Expected Value: 100Desired Supplier: VenflpoStart Date: Today’s dateEnd Date: 1 month from today’s datePurchasing Group: 001Inside Account Assignments sub-section, Order: Maintenance order number which was created in the above section Create Maintenance Order. | Purchase requisition Item data values are entered. |  |
| 7 | Save Limit PR | Click on Apply in Purchase Requisition Item screen.Then click on Create in Purchase Requisition screen.(Ignore the warnings if any occur) | Purchase requisition is created. |  |
| 8 | Use this Limit PR while Creating PO | For the rental renewal process include this Limit PR along with the service line-item PR (created in step Create Maintenance Order) while creating purchase order in the step Create Purchase Order. |  |  |

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
> Flagged while digesting this document, not verified: Limit PR values differ between sections: Overall Limit 10 / Expected Value 10 in 'Create Limit PR for Rental / Renewal Extension' versus Overall Limit 1000 / Expected Value 100 in 'Renew Rentals'.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Remote warehouse task destination bin is GENERAL-AREA in 'Receive Supplier Item at Remote > Process Receipt' but GEN-AREA in the following 'Complete Open Warehouse Tasks' purpose text.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/test-script-field-logistics-planning-and-execution-40g-ae-sap-s-4hana-part-01]]
- related-to :: [[14-maintenance-service-and-projects/test-script-sap-s-4hana-cloud-public-edition-field-logistics-planning]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4AH_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 117,382 chars in the whole document
