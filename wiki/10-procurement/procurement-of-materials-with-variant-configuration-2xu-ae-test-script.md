---
id: 10-procurement/procurement-of-materials-with-variant-configuration-2xu-ae-test-script
title: Procurement of Materials with Variant Configuration (2XU_AE) - Test Script (2XU_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script (scope item 2XU, UAE) for procuring variant-configured materials: prerequisites, PO to goods receipt to supplier invoice."
cluster: 10-procurement
tags: [kb/procurement, topic/procurement-with-variant-configuration]
aliases: [2XU_S4CLD2608_BPD_EN_AE]
keywords: [Procurement of Variant-Configured Materials, variant configuration, purchase orders, purchase order approval, flexible workflow, purchasing info record, variant pricing, goods receipt, supplier invoice, purchase requisition by MRP]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2XU_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-887
topic: 10-procurement/procurement-with-variant-configuration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Procurement of Materials with Variant Configuration (2XU_AE) - Test Script (2XU_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2XU_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Procurement of Variant-Configured Materials** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Procurement of Materials with Variant Configuration (2XU_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Procurement of Materials with Variant Configuration (2XU_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232851073)

[2 Prerequisites 4](#_Toc232851074)

[2.1 System Access 4](#_Toc232851075)

[2.2 Roles 4](#_Toc232851076)

[2.3 Master Data and Organizational Data 5](#_Toc232851077)

[2.4 Business Conditions 8](#_Toc232851078)

[2.5 Preliminary Steps 8](#_Toc232851079)

[2.5.1 Variant Pricing Configuration 8](#_Toc232851080)

[2.5.1.1 Create Characteristic 8](#_Toc232851081)

[2.5.1.2 Maintain Class 9](#_Toc232851082)

[2.5.1.3 Create Dependency 10](#_Toc232851083)

[2.5.2 Create Purchasing Info Record 11](#_Toc232851084)

[2.5.3 Maintain Characteristic Display for Procurement 12](#_Toc232851085)

[2.5.4 Create Purchase Requisition by MRP 14](#_Toc232851086)

[2.5.5 Check Flexible Workflow for Purchase Order Approval 18](#_Toc232851087)

[2.5.6 Configure Flexible Workflow for Purchase Order 20](#_Toc232851088)

[3 Overview Table 21](#_Toc232851089)

[4 Test Procedures 22](#_Toc232851090)

[4.1 Create Purchase Orders 22](#_Toc232851091)

[4.1.1 Option A: Create Purchase Order 22](#_Toc232851092)

[4.1.2 Option B: Create Purchase Order with Inbound Delivery 24](#_Toc232851093)

[4.2 Approve Purchase Order (Optional) 25](#_Toc232851094)

[4.3 Preview Purchase Order (Optional) 26](#_Toc232851095)

[4.4 Change Purchase Order (Optional) 27](#_Toc232851096)

[4.5 Create Inbound Deliveries (Optional) 28](#_Toc232851097)

[4.6 Confirm Quantities for Putaway (Optional) 29](#_Toc232851098)

[4.7 Post Goods Receipt 30](#_Toc232851099)

[4.8 Create Supplier Invoice 31](#_Toc232851100)

[4.9 Review Supplier Invoice (Optional) 33](#_Toc232851101)

[5 Appendix 35](#_Toc232851102)

[5.1 Succeeding Process 35](#_Toc232851103)

## Purpose

Overview

Variant configuration is an important tool in the manufacturing process. Improve your company's product Engineering, Sales, Procurement, and Manufacturing performance with SAP software for integrated variant configuration and classification. Enable your business process to handle highly individualized products in sales, Procurement and Manufacturing.

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
| Product Configuration Modeler | SAP_BR_PRODUCT_CONFIG_MODELER | Variant Configuration | SAP_BR_PRODUCT_CONFIG_MODELER |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |

### Master Data and Organizational Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | CM-MLFL-KM-VXX | Multi-Level Forklifter |  |
| Material | SF-FL-FORKSEAT-VXX | Seat Type of Fork lifter(HALB) | Initial stock posting required |
| Material | SF-FL-COMB | Forklift Base Combustion Model | Initial stock posting required |
| Material | SF-FL-ELECTRIC | Forklift Base Electrical Model | Initial stock posting required |
| Material | SF-FL-CWEIGHT | Forklift Counterweight Plate | Initial stock posting required |
| Material | SF-FL-TIRE-CUSH | Forklift Cushion Tire | Initial stock posting required |
| Material | SF-FL-TIRE-PNEU | Forklift Pneumatic Tire | Initial stock posting required |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Supplier | 33300001 | Domestic UAE Supplier 1 | Note If you want to send form print outs via e-mail in stead of using the print functionality make sure that you have maintained a valid e-mail address in the supplier master data. |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchase group | 001 | Group 001 |  |

Bill of Material Structure

This overview shows the bill of material structure and the usage of each component if you have activated all optional enhancements.

This is a super BOM list for configurable materials. Not all components necessarily used in production order.

| Material | Level | Material Type | Unit | Characteristics of Material | Optional Enhancements |
| --- | --- | --- | --- | --- | --- |
| CM-MLFL-KM-VXX | 0 | KMAT | PC | Multi-Level Forklifter |  |
| SF-FL-COMB | 1 | HALB | PC | Forklift Base Combustion Model |  |
| SF-FL-ELECTRIC | 1 | HALB | PC | Forklift Base Electrical Model |  |
| SF-FL-CWEIGHT | 1 | HALB | KG | Forklift Counterweight Plate |  |
| SF-FL-TIRE-CUSH | 1 | HALB | PC | Forklift Cushion Tire |  |
| SF-FL-TIRE-PNEU | 1 | HALB | PC | Forklift Pneumatic Tire |  |
| SF-FL-FORKSEAT-VXX | 1 | HALB | PC | Seat Type of Fork lifter(HALB) |  |

Application Groups

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Application Groups | MM | Purchase Order |  |

Characteristic Display

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Characteristic Display | MM_FK_ST | Assigned Characteristics:Seat TypeStandard ValueSeat Color |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| 2NI | Create Application Group and Characteristic Display - MDS |
| 2T7 | Create Product Master of Type "Configurable Material" - MDS |
| BHD | Create Purchasing Info Record - MDS |

### Business Conditions

Before this test script can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ – Create New Open MM Posting Period - MDS | Complete all relevant steps. |
| BHD – Create Purchasing Info Record - MDS | Refer to the chapter Create Purchasing Info Record to create the Info Record for this Scope Item (for more information, see Preliminary Steps). |
| 1YT – Make-to-Order Production with Variant Configuration | To run through this test script, the Purchase Requisition must be created by Material Requirements Planning (MRP).Run through the 1YT Make-to-Order Production with Variant Configuration process(for more information, see Preliminary Steps). |

### Preliminary Steps

#### Variant Pricing Configuration

##### Create Characteristic

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Product Configuration Modeler. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the app | Open Manage Characteristics (CT04). | The Characteristics screen is displayed. |  |
| 3 | Enter the characteristic name | Make the following entry and choose Create:Characteristic: AVC_CR_VAR_PRICE_VXX | The Create Characteristic screen is displayed. |  |
| 4 | Enter basic data | On the Basic data tab, make the following entries.In the Basic data section:Description: Variant PricingStatus: Released (default)In the Format section:Data Type: Character FormatNumber of Chars: 20In the Value Assignment section:Select the Multiple Values radio button. | Basic data is added. |  |
| 5 | Enter additional data | On the Addnl data tab, make the following entries.In the Reference to Table Field section:Table Name: MMCOMField Name: VKOND | Additional data is added. |  |
| 6 | Save the characteristic | Choose Save. | The characteristic is created. |  |

##### Maintain Class

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Product Configuration Modeler. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the app | Open Manage Classes (CL02). | The Class screen is displayed. |  |
| 3 | Enter the class name | Make the following entries and choose Change:Class: AVC_CL_FORKSEAT_VXClass type: 300 | The Create Class screen is displayed. |  |
| 4 | Add the new characteristic | On the Char. tab, add the characteristic AVC_CR_VAR_PRICE_VXX and choose Save. | The characteristic is added. |  |

##### Create Dependency

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Product Configuration Modeler. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the app | Open VC Modeling Environment (PMEVC). | The Initial Screen of Variant Configuration Modeling Environment screen is displayed. |  |
| 3 | Enter the configuration model data | On the initial screen, make the following entries and choose Enter Model.Material: SF-FL-FORKSEAT-VXXClass Type: 300 (Default) | The Create Characteristic screen is displayed. |  |
| 4 | Create new dependency | Right-click the profile AVC_CP_FORKSEAT_VXX in the object list and choose Create Dependency – Global (Reusable).On the Create Dependency on Configuration Profile screen, make the following entries:Dependency: AVC_AIR_SEATTYPEDependency Type: ProcedureChoose Continue.On the Basic data tab, make the following entries.Description: Dependency for the Seat TypeStatus: In PreparationOn the Editor tab:Add the following formula:$SELF.AVC_CR_VAR_PRICE_VXX = 'AVC_AIR_SEATTYPE'IF $SELF.AVC_CR_SEATTYPE_VXX = 'AIR',$SELF.AVC_CR_VAR_PRICE_VXX = 'AVC_HVY_SEATTYPE'IF $SELF.AVC_CR_SEATTYPE_VXX = 'HVY'Choose Save.Go back to the Basic Data tab and choose Edit. Change the Status from In Preparation to Released.Choose Save. | The dependency is created. |  |

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
| 3 | Enter Info Record Data | Make the following entries:Supplier: 33300001Material: SF-FL-FORKSEAT-VXXPurchasing Organization : 3310Plant: 3310Info category: Standard (Default)Choose Enter. | The Create Info Record: General Data screen is displayed. |  |
| 4 | Enter Purchasing Data | Choose Purch. Org. Data 1 and make the following entries:Pl. Deliv. Time: 2(Default)Purch. Group : 001(Default)Standard Qty: 1Tax Code: <Input Tax Code>Note If time dependent tax (TDT) is activated, and fields Country/Region Key for company code, Validity Periods and Tax Code are maintained via SSCUI 101016 in SAP S/4HANA Cloud Public Edition or the configuration activity Define Tax Codes for Sales and Purchases in Central Business Configuration, you must maintain the Tax Rate Valid From field in the New Purchasing Info Record screen. If you enter the current date, this date will be adjusted to a valid start date for your tax code according to the SSCUI/configuration activity settings.If Registration for Indirect Taxation Abroad (RITA) is activated, and tax registration country and tax code are maintained for company code via SSCUI 103464 in SAP S/4HANA Cloud Public Edition or the configuration activity Activate RITA and Maintain Tax Registration Countries in Central Business Configuration, you must maintain the Tax Country field. The default value of this field is the country ID of company code, but you can change it to a valid country ID that is maintained in the SSCUI/configuration activity accordingly.Net Price: 3,100 | Purchasing Data is added. |  |
| 5 | Create Variant Condition | Choose Variant Conditions, enter the variant condition name AVC_AIR_SEATTYPE and click Choose. | Overview of Condition Types screen is displayed. |  |
| 6 | Enter Condition Record Data | Double-click PVA1. On the Validity Periods: Conditions screen, choose Choose and make the following entries:Material: SF-FL-FORKSEAT-VXXVariant: AVC_AIR_SEATTYPEAmount:200Choose Back, then choose Variant Conditions and make the entries below to create a new variant condition:Material: SF-FL-FORKSEAT-VXXVariant: AVC_HVY_SEATTYPEAmount:300Click Choose. | The condition records are created. |  |
| 7 | Save Data | Choose Save. | A purchasing info record is saved. |  |

#### Maintain Characteristic Display for Procurement

Purpose

You need to create the characteristic display for procurement first, so that it can be choosed during the purchase order creation. Then the characteristic values will be displayed for the purchase item on the screen. You can check and skip this step if the entries exit already.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Configuration Modeler. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Maintain Char. Display for Configuration (CU_CHAR_DISPLAY) | The Change View “Application Group”: Overview screen is displayed. |  |
| 3 | Create Application Group | Choose New Entries on the upper left side of the screen. Make the following entries on the right:Transact.: Purchase OrderAppl. Grp: MMChoose Save. | The application group is created. |  |
| 4 | Create Characteristic Display | Double click the entry of Characteristic Display on the left side. Choose New Entries on the upper left side of the screen. Make the following entries on the right:Char. Display: MM_FK_STDescription : Purchase Fork Lifter SeatAppl. Grp: MMChoose Save. | The characteristic display is created. |  |
| 5 | Assignment to the Characteristic Values | Check the checkbox of the entry of Char. Display created previously, and double click the entry of Characteristic Assignment on the left side. Choose New Entries on the upper left side of the screen. Make the following entries on the right:Seq. : 0Characteristic Name: AVC_CR_SEATTYPE_VXXCol.: 6Create two more new entries:Seq.: 1Characteristic Name : AVC_CR_SEAT_COLOR_VXXCol.: 6Seq.: 2Characteristic Name : AVC_CR_VAR_PRICE_VXXCol.: 20Choose Save. | The characteristic values are assigned to the characteristic display. |  |

#### Create Purchase Requisition by MRP

Purpose

The BOM component (SF-FL-FORKSEAT-VXX) is purchased externally. The purchase requisition must be created from sales order and material requirements planning (MRP) run.

For this scenario, you can refer to the 1YT - Make-to-Order Production with Variant Configuration scope item as prerequisites.

Procedure

1. Run through the following steps to create the sales order.

The steps can be referred to the chapter Make to Order Production with Multilevel Configurable Material - Create Sales Order with Configurable Material in the 1YT - Make-to-Order Production with Variant Configuration scope item.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Sales Orders - VA01 (VA01). | The Create Sales Documents screen displays. |  |
| 3 | Enter the Order type OR (Standard Order) | On the Create Sales Documents screen, make the following entries and choose Continue:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 4 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries and press Enter:Sold To party: 33100001Ship To party: 33100001Cust. Reference: Reference number Enter a customer purchase order number as referenceRep. Deliv. Date: <Current date - 5 days>Material Number: CM-MLFL-KM-VXXQuantity: for example, 1 PCNote If you want to create billing plan for this sales order, manually enter the following value as well. If not, press Enter.ItCa (Item category): CBTDNote If you want to procure finished material directly, for example CM-MLFL-KM-VXX, please change procurement type of material to F using app Change Material (MM02) |  |  |
| 5 | Enter Characteristic Value for Header Material | On the Variant Configuration screen, choose Default Group. Select value for characteristics below:Lifter Model: <Heavy, Standard>Power Source: <Combustion, Electrical>. Combustion displays as default value.Choose Technical and select value for other characteristics.Wheel Type: <Cushion Tires, Pneumatic Tires>Fork Size: <Small, Normal, Large>Counterweight (KG): <1.000, 2.000, 5.000>Battery Capacity(Ah) : <50, 80, 140>The combination of value for characteristic is constrained by Constraint Net. Only the following combinations are acceptable.Combination One:Lifter Model: HeavyPower Source: CombustionCounterweight (KG): <5.000> is filled in automaticallyWheel Type: Cushion Tires or Pneumatic TiresFork Size: Small or Medium or LargeCombination Two:Lifter Model: StandardPower Source: CombustionWheel Type: Cushion Tires is filled in automaticallyFork Size: Small or Normal or LargeCounterweight (KG): 1.000 or 2.000Combination Three:Lifter Model: StandardPower Source: ElectricalWheel Type: Cushion Tires is filled in automaticallyFork Size: Small or Normal or LargeCounterweight (KG): 1.000 or 2.000Battery Capacity(Ah): 50 or 80 or 140 (140 only available when fork size is L) |  |  |
| 6 | Enter Characteristic value for Component Material | Choose Toggle Structure Panel icon on the top right corner.Choose product SF-FL-FORKSEAT-VXX in the Configuable item panel.Choose value for the following characteristic and choose Done.Seat Color: Black, White or GreySeat Type: Standard, Heavy Duty, or Air suspensionNote Heavy Duty is only selectable if the fork lifter model is Heavy. | Configurable item panel displays. |  |
| 7 | Save Document | On the Review Availability Check Result screen, click Apply.Choose Save. Make a note of the sales order number: __________. | The order is saved.Note If the sales order might require approval, please refer to scope item Sell from Stock (BD9), and complete the activities of Process Sales Order Approval. |  |

1. Run through the following steps to run the MRP.

The steps can be referred to the chapter Make to Order Production with Multilevel Configurable Material - Manufacturing Steps Production Order Processing in 1YT Make-to-Order Production with Variant Configuration scope item.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen is displayed. |  |
| 3 | Enter the Basic Parameters for New Job | Choose Create above the table.On the New Jobs screen, make the following entries:Job Template: Material Requirement Planning (MRP)Job Name:MRP for CM-MLFL-KM-VXXStart Schedule Immediately: XPlant: 3310Material :CM-MLFL-KM-VXXChanged BOM Components: XPlanning Mode: 1 |  |  |
| 4 | Enter the Scheduling Parameters for New Job | Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Schedule Immediately: XRecurrence Pattern: Single RunChoose OK. |  |  |
| 5 | Schedule New Job | On the New Jobs screen, choose Schedule. | The new job is created and is displayed in the table of Application Jobs. |  |
| 6 | Refresh the Application Jobs list | To check the status of the jobs created by you, choose Go on the upper right part of the screen. | The Application Jobs table refreshes. |  |

1. Find the Purchase Requisition created by MRP run.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net and Individual Segments screen is displayed. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 4 | Select the Material | Select the checkbox of the following entry and choose Manage Materials.Material: SF-FL-FORKSEAT-VXXIndividual Segment: CustSt xxxxxxxx-10 (the quotation or sales order number created by youNote If the expected entry can't be found, choose the user icon in the upper right corner, and choose App Settings.On the MRP Settings screen, choose Area of Responsibility.On the Area of Responsibility screen, choose line or lines for plant, for example, 3310, then choose Assign.Choose Back.Repeat your search again. | The Manage Material Coverage screen displays.Note that you select the right individual segment for the customer order. |  |
| 5 | Find the Purchase Requisition | Find the generated Purchase Requsition. |  |  |

#### Check Flexible Workflow for Purchase Order Approval

Purpose

In this procedure, you check the flexible workflow for purchase order approval.

When you use the flexible workflow to approve the purchase order, make sure Flexible Workflow for Purchase Order with NB document should be activated, and you should configure Flexible Workflow for Purchase Order Approval.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution screen, search Activate Flexible Workflow for Purchase Orders, then choose Go.Select the line of the item and go to the next screen.On the Configure Your Solution – Purchase Order Processing screen, choose Configure on the line of configuration step with name Activate Flexible Workflow for Purchase Orders. | The Document Types Purchase order Change screen is displayed. |  |
| 5 | Check Flexible Workflow for PO Approval | Check the following entries:Document Type: NBScenario based workflow:X | The Scenario based workflow is active for Purchase Orders with Document Type: NB. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Configuration app and search for the following activity: Activate Flexible Workflow for Purchase Orders.Choose Open Documentation for the line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Document Types Purchase order Change screen displays. |  |
| 3 | Check Flexible Workflow for PO Approval | Check the following entries:Document Type: NBScenario based workflow:X | The Scenario based workflow is active for Purchase Orders with Document Type: NB. |  |

Result

The Scenario based workflow is active for Document Type: NB.

#### Configure Flexible Workflow for Purchase Order

Purpose

In this procedure, you configure your release conditions for Purchase Order Approval.

Note When you start to process this step, please make sure that the flexible workflow for purchase document type NB has been activated in your system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Fiori launchpad is displayed. |  |
| 2 | Open Manage Workflow for Purchase Order | Open Manage Workflows for Purchase Orders (F2872). | The Manage Workflows screen is displayed. |  |
| 3 | Create Manage Workflow | Choose Create and make the following entry:Name: Test Workflow for Purchase OrderIn the Start Conditions area, select Purchasing group of purchase order is with 003 value:Choose Create another condition and make the following entries:Choose Total net amount of purchase order is greater thanPrice: 5000 .Currency: AEDIn Step Sequence area choose Create and make following entries:Type: Release of Purchase OrderUser: Select user with Purchasing_manager from F4 help.Step to be completed by: One of the recipients.Choose Create.Choose Save. | The workflow for purchase order is configured. |  |
| 4 | Activate Workflow Item | Select the just created workflow Item and choose Activate. | The workflow item is activated. |  |

|  |
| --- |
| Note Please make sure the default workflow Automatic Release of Purchase Order has been activated.For the Workflow and Step names, you can translate them to other languages, for example from English to German via the Workflow Content Translation app. |

## Overview Table

This scope item consists of several process steps that are listed in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | APP | Expected Results |
| --- | --- | --- | --- |
| [Option A: Create Purchase Order](#unique_16) [page ] 22 | Purchaser | Create Purchase Order - Advanced (ME21N) | Purchase Order is created. |
| [Approve Purchase Order (Optional)](#unique_17) [page ] 25 | Purchasing Manager | My Inbox - All Items (F5331) | Purchase Order is approved. |
| [Preview Purchase Order (Optional)](#unique_18) [page ] 26 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order is previewed.. |
| [Change Purchase Order (Optional)](#unique_19) [page ] 27 | Purchaser | Change Purchase Order - Advanced (ME22N) | Purchase Order is changed.. |
| [Create Inbound Deliveries (Optional)](#unique_20) [page ] 28 | Receiving Specialist | Inbound Deliveries for Purchase Orders (VL34) | Inbound delivery is created |
| [Confirm Quantities for Putaway (Optional)](#unique_21) [page ] 29 | Receiving Specialist | Inbound Deliveries for Putaway (VL06IP) | The Inbound Deliveries for Putaway Screen appears. |
| [Post Goods Receipt](#unique_22) [page ] 30 | Warehouse Clerk | Post Goods Movement (MIGO) | Goods Receipt is posted. |
| [Create Supplier Invoice](#unique_23) [page ] 31 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | Supplier Invoice is created. |
| [Review Supplier Invoice (Optional)](#unique_24) [page ] 33 | Accounts Payable Accountant | Supplier Invoices List (F1060A) | Supplier Invoice is reviewed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Purchase Orders

#### Option A: Create Purchase Order

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
| 1 | Log on | Open the SAP Fiori launchpad with the Purchaser role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Create Purchase Order | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order screen is displayed. |  |
| 3 | Search the Purchase Requistion | Choose Document Overview On on the upper left side of the screen.Choose Selection Variant below and choose Purchase Requisitions.Enter the purchase requisition number created by MRP in the field Purchase Requisition Number and choose Execute on the lower right side of the screen. | The Purchase Requisition is displayed for reference. |  |
| 4 | Adopt the Purchase Requisition | Choose the purchase requisition and then choose Adopt at the top. | The item and detailed information of Purchase Requisition will be copied to Purchase Order draft. |  |
| 5 | Enter General Data | Make the following entries:Supplier: 33300001Purch. Org.: 3310Note If you want the purchase order to be assigned to an approver, then total PO amount should be higher than 500 AED for Purchasing Groups 003. |  |  |
| 6 | Review the Characteristic Values | Review the Characteristic Values. The values are inherited from the Sales Order which is created in Scope Item Make-to-Order Production with Variant Configuration.Display the values in the following ways:On Item Overview section, choose Char. Display, locate above the item line, and choose Purchase Fork Lifter Seat from the dropdown list. The columns of characteristic name Seat Type, Seat Color and Variant Configuration will be displayed in the item line. Check whether the characteristic values displayed are same as the ones chosen in the sales order.Choose Configuration on the Material Data tab. On the Advanced Variant Configuration screen, check whether the characteristic values displayed are same as the ones chosen in the sales order. Choose Close once done. | The Characteristic Values are reviewed. |  |
| 7 | Review the Conditions | The price with variant will be calculated per the dependency created in [Create Dependency](#unique_9) [page ] 10 and [Create Purchasing Info Record](#unique_10) [page ] 11.If the value of Seat Type is AIR, the condition type PVA1 with 20% amount will be used and added to the standard price.If the value of Seat Type is HVY (Heavy), the condition type PVA1 with 30% amount will be used and added to the standard price. | The Conditions are reviewed. |  |
| 8 | Save the Purchase Order | Choose Save in the lower right corner of the screen. | The Purchase Order is created. |  |

#### Option B: Create Purchase Order with Inbound Delivery

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
| 1 | Log on | Open the SAP Fiori launchpad with the Purchaser role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Creat Purchase Order | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order screen is displayed. |  |
| 3 | Search the Purchase Requistion | Choose Document Overview On on the upper left side of the screen.Choose Selection Variant below and choose Purchase Requisitions.Enter the purchase requestion number created by MRP in the field Purchase Requisition Number and choose Execute on the lower right side of the screen. | The Purchase Requisition is displayed for reference. |  |
| 4 | Adopt the Purchase Requisition | Choose the purchase requisition and then choose Adopt at the top. | The item and detailed information of Purchase Requisition will be copied to Purchase Order draft. |  |
| 5 | Enter General Data | Make the following entries:Supplier: 33300001Purch. Org.: 3310If you want the purchase order to be assigned to an approver, then total PO amount should be higher than 500 AED for Purchasing Groups 003.Select item, then choose Confirmations tab:Conf. Control: Inbound DeliveryChoose Delivery Schedule tab:Delivery Date: TodayChoose Apply. |  |  |
| 6 | Review the Characteristic Values | Review the characteristic values. The values are inherited from the sales order which is created in scope item Make-to-Order Production with Variant Configuration.Display the values in the following ways:On Item Overview section, choose Char. Display, locate above the item line, and and choose Purchase Fork Lifter Seat from the dropdown list. The columns of characteristic name Seat Type, Seat Color and Variant Configuration will be displayed in the item line. Check whether the characteristic values displayed are same as the ones chosen in the sales order.Choose Configuration on the Material Data tab. On the Advanced Variant Configuration screen, check whether the characteristic values displayed are same as the ones chosen in the sales order. Choose Close once done. | The Characteristic Values are reviewed. |  |
| 7 | Review the Conditions | The price with variant will be calculated per the dependency created in [Create Dependency](#unique_9) [page ] 10 and [Create Purchasing Info Record](#unique_10) [page ] 11.If the value of Seat Type is AIR, the condition type PVA1 with 20% amount will be used and added to the standard price.If the value of Seat Type is HVY (Heavy), the condition type PVA1 with 30% amount will be used and added to the standard price. | The Conditions are reviewed. |  |
| 8 | Save the Purchase Order | Choose Save in the lower right corner of the screen. | The purchase order is created. |  |

### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you release a purchase order. If the total amount of PO > 500 AED and purchase group is 003, then the PO should do the approval. PO release amount is configured in AED in configure Flexible workflow for Purchase Order, and it converted to the country currency amount for purchase order approval.

Prerequisite

A purchase order must exist for release.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F5331). | A list of existing Purchase Orders is displayed. |  |
| 3 | Search for Purchase Order Status | Make the following entry and choose Enter:Search: <Purchase Order number> | The Purchase Order is displayed. |  |
| 4 | Approve Purchase Order | Select the Purchase Order on the left side of the screen and choose Approve at the bottom right. | The Submit Decision screen is displayed. |  |
| 5 | Enter Approval Reason | Enter the approval reason if necessary, and then choose Submit.Note If attachment is uploaded during purchase order creation, in My Inbox App, the attachment can be found under Attachments tab of the purchase order. The attachment will be renamed with prefix 'H_'. | The Purchase Order is approved. |  |

### Preview Purchase Order (Optional)

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

### Change Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can change an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Purchaser role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Purchase Order | Open Change Purchase Order - Advanced (ME22N).If you want to use the Save Draft feature in this app, you have to use a personalized user. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Select Purchase Order | Enter the Purchase Order number in the Purchase Order search box, and choose Go. Select the row for the Purchase Order you want to change and use the little arrow on the right side to enter the PO detail, then choose Display/Change to switch to edit mode. | The Display Purchase Order Advanced screen is shown.The Purchase order is opened in change mode. |  |
| 4 | Change Purchase Order | Change certain field values of the Purchase Order. | The Purchase Order values are changed. |  |
| 5 | Display the characteristic values | In the Char. Display dropdown list, choose Product Folk Lifter.The characteristic values will be displayed on the right side of the item below, | The Purchase Order is completed. |  |
| 6 | Messages (Optional) | Choose Messages(if possible). | If a message is displayed, you must correct the Purchase Order. If no message is displayed, the Purchase Order is completed. |  |
| 7 | Save Purchase Order | Choose Order to save the Purchase Order. | The Purchase Order has been saved. The system displays a success message Purchase order xxx has been saved. |  |

### Create Inbound Deliveries (Optional)

Purpose

|  |
| --- |
| Note If you didn’t perform the step: [Option B: Create Purchase Order with Inbound Delivery](#unique_26) [page ] 24, please skip this step. |

In this activity, you create the inbound deliveries. Please use the the purchase order created in the step: [Option B: Create Purchase Order with Inbound Delivery](#unique_26) [page ] 24

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

### Confirm Quantities for Putaway (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If you didn’t perform the step: [Option B: Create Purchase Order with Inbound Delivery](#unique_26) [page ] 24, please skip this step.

This activity confirms that all the materials have been put away in the correct quantities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the role Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Inbound Deliveries for Putaway (VL06IP). | The Inbound Deliveries for Putaway screen displays. |  |
| 3 | Enter inbound delivery number | Make the following entries then choose Execute:Delivery Date: Delete the default dateInbound Delivery: XXX | The selected Inbound Delivery displays. |  |
| 4 | Change the inbound delivery | Select Inbound deliveries and click Change Inbound Deliveries. | The Inbound Delivery XXX Change: Overview screen displays. |  |
| 5 | Confirm Quantities for Putaway | In Item Overview tab, input the Putaway Qty: XXXNote The put away quantity should equal to the delivery QtyAnd choose Save. | Back to the Inbound Deliveries for Putaway screen and Inbound Delivery XXX has been saved message displays. |  |

### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Goods ordered by a purchase order arrive at warehouse. The goods receipt is to be posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the Fiori Launch Pad with the Warehouse Clerk role. | The Fiori launchpad is displayed. |  |
| 2 | Open Post Goods Movement tile | Open Post Goods Movement (MIGO) | The Goods Receipt for Purchase Order screen is displayed. |  |
| 3 | Select Goods Receipt Order screen | On the Goods Receipt Purchase Order screen, make the following entries and choose Enter:Goods Receipt: <Select>Purchasing Order: <Select>Order number: <Purchase Order number>GR goods receipt: 101 | The items of the selected Purchase Order are displayed. |  |
| 4 | Choose the Quantity tab and confirm the quantity | Confirm the quantity. |  |  |
| 5 | Select Item ok Indicator | Select the Item OK checkbox. |  |  |
| 6 | Post | Choose Post. | The goods receipt is posted. A system message is shown. |  |

### Create Supplier Invoice

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
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount: <XXX>Currency: AEDInvoice Date: <Today>Posting Date: <Today>Reference: <XXX>(reference invoice number from invoicing party)Input the NF number in the reference field. Use a dash - to input the NF Series, when applicable (for example, 12345-001).Invoice Party: 33300001In case of purchase orders created with foreign currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount: <XXX>Currency: <XXX>(change the invoice currency, for example from AED to USD)Invoice Date: <Today>Posting Date: <Today>Reference: <XXX>(reference invoice number from invoicing party)Select Show More in lower right area and make the following entry:Exchange Rate: <XXX> | The Exchange Rate should be changed from AED in EUR according to the customizing settings. The Exchange Rate is changeable. |  |
| 4 | Enter Purchasing Document References | Add references in section Purchasing Document References.Make the following entries (use a PO you created previously).Reference Document Category: Purchase Order/Scheduling AgreementPurchase Order/Scheduling Agreement: <PO number> | All items of the referenced Purchase Order are added to the Invoice Items section. |  |
| 5 | Select Invoice Items | Select the Invoice Items you want to create invoice for. | You should see material items and delivery costs items, which refer to the entered purchase order document. Check if items for planned delivery costs have an item text. |  |
| 6 | Check Invoice Items Data | Check Amount, Quantity and Tax Code (there may already be a tax code that was copied from the purchase order). | The Amount, the Quantity, the Tax Code are consistent. |  |
| 7 | Check Tax Code | In the Tax section, check if there is tax code information and enter the tax amount if the tax rate is greater than zero. | In the Tax area, you should see the same tax codes as in the items. If there is no tax, specify that the tax code is <Input Tax Code>. |  |
| 8 | Block Invoice on Item Level (Optional) | Choose the invoice item arrow on the right side of the item to navigate to the item details.On the next screen, set flag for Manually Blocked. Choose Check. On the lower part of the details screen, the Blocking Reasons section shows Manual. Choose Back to Supplier Invoice to get back to the previous screen. | The item is blocked with a blocking reason. |  |
| 9 | Check Balance | The system automatically calculates tax amount, which is item amount multiplied by tax rate. Check the balance (difference between the calculated amount and the gross amount you entered in step 3) on the upper left corner. | The balance should be zero (or within the defined tolerance). |  |
| 10 | Simulate Supplier Invoice and Check Messages | Choose Simulate.You can check the simulation results in Overview and Details area. | The Supplier Invoice is simulated. |  |
| 11 | Post Invoice | Choose Post. | The invoice is posted. The system message is shown. |  |

### Review Supplier Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The invoice verification is done in this activity using the list overview on invoice documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Accounts Payable Accountant role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Supplier Invoices List App | Open Supplier Invoices List (F1060A). | The Supplier Invoices List screen is displayed. |  |
| 3 | Enter General Data | Enter the Supplier Invoice number in the Invoice Document No. search box and choose Go.Or you can make the following entries and choose Go to search the documents.Invoicing Party: 33300001Company Code: 3310 | The Supplier Invoices are listed in the result. |  |
| 4 | Select Supplier Invoice | Select the row for the Supplier Invoice you want to check and use the little arrow on the right side to enter the details. | The details of Supplier Invoice is displayed. |  |

## Appendix

### Succeeding Process

After completing the activities in this test script, you can continue testing the following business processes:

Table 2:

| Process | Business Condition |
| --- | --- |
| Accounts Payable (J60) | Complete the following activities described in the test script:Payment RunPost Outgoing Payment |
| Accounting and Financial Close (J58) | Dispose of the inventory by returning to the vendor. Do not process any other activities in this docu­ ment after running the external process.Using the master data from this document, complete the following activities described in the test script:Run the test script in its entirety, using the master data from this test script document. |
| Real-Time Reporting and Monitoring for Procurement (1JI) | The Procurement Overview Page gives the Purchaser the most important and relevant information at a glance – instead of navigating through many different transactions and reports.The global filter helps the Purchaser to focus the entire Procurement Overview Page to view all information according to specific suppliers, material groups, purchasing groups, and more.Using contextual navigation, the Purchaser can immediately act upon the displayed information by accessing the app or the object instance or get more detailed information in the corresponding KPI Drill-Downs. |

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
> Flagged while digesting this document, not verified: PO approval threshold is stated as total amount above 500 AED for purchasing group 003 in the PO and approval sections, but the configured test workflow uses total net amount greater than 5000 AED.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Variant condition PVA1 is created with absolute amounts 200 and 300 in the info record, but the PO step says PVA1 applies 20% and 30% added to the standard price.

## Connections
- part-of :: [[_cluster]]
- see-also :: [[02-business-partner-and-product-master-data/anwendungsgruppe-und-merkmalsanzeige-anlegen-sds-2ni-268]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2XU_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 59,006 chars in the whole document
