---
id: 10-procurement/test-script-subcontracting-bmy-ae-sap-s-4hana-cloud-public-edition-129
title: "Test Script: Subcontracting (BMY_AE) - SAP S/4HANA Cloud Public Edition (BMY_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item BMY (UAE) subcontracting in S/4HANA Cloud Public Edition 2608: prerequisites and test steps, with and without serial numbers."
cluster: 10-procurement
tags: [kb/procurement, topic/subcontracting-procurement]
aliases: [BMY_S4CLD2608_BPD_EN_AE]
keywords: [Subcontracting Procurement, subcontracting, subcontracting purchase order, serial number management, outbound delivery, goods receipt, supplier invoice, purchase order approval, goods issue, inbound delivery]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BMY_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1292
topic: 10-procurement/subcontracting-procurement
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Subcontracting (BMY_AE) - SAP S/4HANA Cloud Public Edition (BMY_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BMY_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Subcontracting Procurement** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Subcontracting (BMY_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232862450)

[2 Prerequisites 4](#_Toc232862451)

[2.1 System Access 4](#_Toc232862452)

[2.2 Roles 4](#_Toc232862453)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232862454)

[2.4 Business Conditions 7](#_Toc232862455)

[2.5 Preliminary Steps 8](#_Toc232862456)

[2.5.1 Create Purchasing Info Record (Optional) 8](#_Toc232862457)

[2.5.2 Initial Requirement Situation (Optional) 10](#_Toc232862458)

[2.5.3 Creating Planned Independent Requirements 11](#_Toc232862459)

[2.5.4 Material Requirements Planning at Plant Level 12](#_Toc232862460)

[2.5.5 Initializing Material Stock 14](#_Toc232862461)

[2.5.5.1 Option 1: For Non-Serial Number Managed Material 14](#_Toc232862462)

[2.5.5.2 Option 2: For Serial Number Managed Material 15](#_Toc232862463)

[2.5.6 Check Flexible Workflow for Purchase Order Approval 16](#_Toc232862464)

[2.5.7 Configure Flexible Workflow for Purchase Order 17](#_Toc232862465)

[2.5.8 Assign Shipping Points 18](#_Toc232862466)

[3 Overview Table 20](#_Toc232862467)

[4 Test Procedures 22](#_Toc232862468)

[4.1 Part 1: Subcontracting without Serial Number Management 22](#_Toc232862469)

[4.1.1 Convert Purchase Requisition to Purchase Order 22](#_Toc232862470)

[4.1.2 Create Purchase Order 23](#_Toc232862471)

[4.1.3 Monitor Subcontracting Documents (Optional) 25](#_Toc232862472)

[4.1.4 Approve Purchase Orders (Optional) 25](#_Toc232862473)

[4.1.5 Preview Purchase Orders (Optional) 26](#_Toc232862474)

[4.1.6 Option 1 : Outbound Delivery 27](#_Toc232862475)

[4.1.6.1 Handling Unit Management (Optional) 28](#_Toc232862476)

[4.1.6.2 Create Outbound Delivery 28](#_Toc232862477)

[4.1.6.3 Pick and Post Goods Issue 29](#_Toc232862478)

[4.1.7 Option 2: Transfer Posting 30](#_Toc232862479)

[4.1.8 Receive Goods from Subcontracting PO 31](#_Toc232862480)

[4.1.9 Create Supplier Invoice 32](#_Toc232862481)

[4.1.10 Review Supplier Invoice (Optional) 34](#_Toc232862482)

[4.2 Part 2: Subcontracting with Serial Number Management 35](#_Toc232862483)

[4.2.1 Create Purchase Order 35](#_Toc232862484)

[4.2.2 Approve Purchase Orders (Optional) 37](#_Toc232862485)

[4.2.3 Create Outbound Delivery 38](#_Toc232862486)

[4.2.4 Handling Unit Management (Optional) 39](#_Toc232862487)

[4.2.5 Pick and Post Goods Issue 40](#_Toc232862488)

[4.2.6 Create Inbound Delivery (Optional) 41](#_Toc232862489)

[4.2.7 Receive Goods from Subcontracting PO 42](#_Toc232862490)

[4.2.8 Post Goods Receipt for Inbound Delivery (Option 2) 43](#_Toc232862491)

[4.2.9 Create Supplier Invoice 44](#_Toc232862492)

[5 Appendix 47](#_Toc232862493)

[5.1 Succeeding Processes 47](#_Toc232862494)

## Purpose

Overview

A subcontract purchase requisition is either generated via the Material Requirements Planning (MRP) process or manually by a requestor. The purchase requisition is converted into a subcontract purchase order. The purchase order is subject to approval based on predefined parameters before being issued to the subcontractor. The outbound delivery is created, and the goods are picked and shipped to the subcontractor. With the supply of the finished material, the goods receipt is created. The consumption of the sent components is recorded upon the receipt of the value-added finished material. Subsequently, the invoicing process is triggered.

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
| Configuration Expert | SAP_BR_CONFIGURATION_EXPERT |  |  |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Accounts Payable Accountant for United Arab Emirates | SAP_BR_AP_ACCOUNTANT_AE |  |  |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | SG23 | SEMI23,PD,Subcontracting | See sections Business Conditions and Preliminary StepsFor the specific plant, set the Special Procurement Key to “30” for Subcontracting. |
| Material | RM13 | RAW13,PD,Subcontracting | Material provided to subcontractor |
| Material | RM14 | RAW14,PD,Subcontracting | Material provided to subcontractor |
| Material | SG27RM33RM34 | SEMI27,PD,SubcontractingRAW33,PD,SubcontractingRAW34,PD,Subcontracting | Enabled with serial number management |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Vendor | 33300007 | Domestic AE Subcontractor A | Note If you want to send form print outs via e-mail instead of using the print functionality make sure that you have maintained a valid e-mail address in the vendor master data. |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchase group | 001 | Group 001 |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNR | Create Product Master of type "Raw Material" - MDS) |
| BNE | Create Supplier Master - MDS |
| BHD | Create Purchasing Info Record - MDS |

### Business Conditions

Before this test script can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | Complete all relevant steps. |
| BJ5 - Make-to-Stock Production – Discrete Manufacturing | To execute this test script, the required materials must be available in stock. You can create stock by following the steps outlined in the Initializing Material Stock section under Preliminary Steps.If you are working with finished goods (FERT), you have the option to run the Make-to-Stock Production – Discrete Manufacturing BJ5 process for material FG126 to generate a purchase order with SG23. Please note that this step is optional and not mandatory. |

|  |
| --- |
| Note If Pick Confirmation is enabled for a shipping point, you'll encounter the error Picking request not yet confirmed when you pick and post goods issue for the respective shipping point. To avoid this error, ensure the folowing:Go to SSCUI 101903 Define Confirmation Requirements.Verify that the Pick Confirmation setting for the relevant shipping point is set to Blank, which ensures no confirmation. |

### Preliminary Steps

#### Create Purchasing Info Record (Optional)

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
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: SubcontractingPurchasing Organization: 3310Supplier: 33300007Material: SG23Plant: 3310Purchasing Group: 001 | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: TodayAvailable To: 12/31/9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: EXWIncoterm Location 1: VENDORNote Incoterms and their corresponding versions are grouped in the F4 value help. Selecting an Incoterm automatically populates its associated version, which can be subsequently modified or removed if needed. | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: 10Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10.0Tax Code: <tax code>Note If time dependent tax (TDT) is activated, and fields Country/Region Key for company code, Validity Periods and Tax Code are maintained via SSCUI 101016 in SAP S/4HANA Cloud Public Edition or the configuration activity Define Tax Codes for Sales and Purchases in Central Business Configuration, you must maintain the Tax Rate Valid From field in the New Purchasing Info Record screen. If you enter the current date, this date will be adjusted to a valid start date for your tax code according to the SSCUI/configuration activity settings.If Registration for Indirect Taxation Abroad (RITA) is activated, and tax registration country and tax code are maintained for company code via SSCUI 103464 in SAP S/4HANA Cloud Public Edition or the configuration activity Activate RITA and Maintain Tax Registration Countries in Central Business Configuration, you must maintain the Tax Country field. The default value of this field is the country ID of company code, but you can change it to a valid country ID that is maintained in the SSCUI/configuration activity accordingly.Order Unit: PCStandard Order Quantity: 100Goods-Receipt-Based Invoice Verification: X | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To: 12/31/9999Amount: 0.59Pricing Unit: 1Currency: AEDChoose Apply. | Condition Data is added. |  |
| 9 | Enter Reference Data (optional) | You can enter reference data. | Reference data is added. |  |
| 10 | Save your data | Choose Create. | The purchasing info record is saved. |  |

Result

The subcontracting info record is created.

#### Initial Requirement Situation (Optional)

Purpose

The MRP run only creates purchase requisitions if the demand is bigger than the available quantity. You can check the requirement situation in the Stock/Requirement List. If necessary, you can reduce the quantity of unrestricted use by posting a goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to Fiori Launchpad as a Production Planner, |  |  |
| 2 | Open the Fiori App | Open Monitor Material Coverage - Net / Individual Segments (F2101A) . | The Monitor Material Coverage (Original) screen displays. |  |
| 3 | Check Default Area of Responsibility | On the Monitor Material Coverage - Net / Individual Segments screen, choose your user name and choose App Settings.On the MRP Settings screen, choose Area of Responsibility:Check only this entry is displayed there:Plant 1 AE / 001 (MRP Controller 001) |  |  |
| 3 | Select Material | Select the checkbox for material SG23 and choose the Manage Materials button. | The Material screen and Material Details screen display. |  |
| 4 | Check stock | Select the corresponding material. | The detailed Stock/Requirements List for each material displays. |  |

#### Creating Planned Independent Requirements

Purpose

Planned independent requirements are used to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split over time according to dates.

|  |
| --- |
| Note Instead of creating a single requirement, sometimes a requirements plan that includes one or more planned independent requirements can be maintained for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Production Planner . | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445) | The Manage PIRs (Original) screen displays. |  |
| 3 | Check Default Area of Responsibility | On the Maintain PIRs, choose your user name and choose App Settings.On the MRP Settings screen, choose Area of Responsibility:Check only this entry is displayed there:Plant 1 AE/001 (MRP Controller 001) | If the entry Plant 1 AE/001 is not present in the Area of Responsibility screen ,choose Add to select it and then choose OK.For other plant entries in the Area of Responsibility screen, choose Delete to remove the others and then choose OK. |  |
| 4 | Select Material | On the Manage PIRs (Original) screen, , make the following entries:Plant: 3310Period Indicator: Monthly (M)Search: SG23.Note Please make sure you have the same setting in material master data MRP 3 view for Period Indicator. If no, please refer to master data script BNS for adaption. |  |  |
| 5 | Filter Result | Choose Go. | The material item displays. |  |
| 6 | Select Material Item | Check the material item, and choose Edit in the upper right. |  |  |
| 7 | Edit PIRs | On the Edit PIRs screen, enter quantities per period, for example:PIR: 100. |  |  |
| 8 | Save PIRs Draft | Choose Save. | The PIRs Draft is saved. |  |

#### Material Requirements Planning at Plant Level

Purpose

The aim of material requirements planning is to tailor available capacities and receipts on time to suit requirements quantities. You can use MRP or consumption-based planning for this purpose. Single-item multilevel requirement planning is performed for plant 3310.

Prerequisite

The semi product is planned at plant level. There is now a requirement for the material SG23 in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs (Original) screen displays. |  |
| 3 | Enter Basic Parameters for New Job | Choose Create above the table.On the New Jobs screen, make the following entries:Job Template: Material Requirement Planning (MRP)Job Name: MRP forSG23Choose Step 2 and make the following entries:Start Immediately: XNote If the job needs to be run on a regular basis, choose Define Recurrence Pattern.Choose Step 3 and make the following entries:Plant: 3310Material (Original) : SG23Changed BOM Components: XPlanning Mode: 1 |  |  |
| 4 | Enter Scheduling Parameters for New Job | Choose Define Recurrence Pattern.In the Scheduling Information screen, make the following entries:Start Immediately: XRecurrence Pattern: Single RunChoose OK. |  |  |
| 5 | Schedule New Job | In the New Job screen, choose Schedule. | The new job displays in the Application Jobs (Original) table. |  |
| 6 | Refresh Application Jobs List | To check the status of the job you created, choose Go in the top right section of the screen. | The Application Jobs table is refreshed. |  |

#### Initializing Material Stock

##### Option 1: For Non-Serial Number Managed Material

Purpose

In a real business case, the materials are usually purchased from external vendors. In this case, the process is covered by the standard purchasing or subcontracting processes. For the purpose of this test, we post initial stock directly to the storage locations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori launchpad as an Inventory Manager . | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | TheManage Stock (Original) screen displays. |  |
| 3 | Enter Material | Make the following entries and press Enter:Material (Original) : For example, RM13 and RM14Plant: For example, 3310, Plant 1 AE | The stock overview for the material is displayed. |  |
| 4 | Select Stock | Select the icon next to the stock to add initial stock. For example:Storage Location: 331C (for RMxx materials)Unrestricted Use Stock | A dialog box displays. The Storage Location, Stock Type, and Current Quantity fields are displayed according to your entries in previous steps. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Document date: <Today>Posting date: <Today>Stock Change: Initial EntryQuantity: <Enter a quantity> | The system displays the message Material document XXX created. The stock is added. |  |

##### Option 2: For Serial Number Managed Material

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the role Warehouse Clerk . | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) . | The Goods Receipt Other screen displays. | It only displays it that way if it was your last transaction. So the action for the User should be to select field Reference Document for MIGO Transaction Other |
| 3 | Input Movement Type | Make the following entries and choose Enter:Business Transaction: Goods ReceiptBusiness Transaction: OtherMovement Type: 561 - Receipt per initial entry of stock balances into unr.-use |  |  |
| 4 | Input on the Goods Receipt Other screen: Material tab | On the Goods Receipt Other screen: Material tab, make the following entry and choose Enter:Material (Original) : RM33/RM34 |  |  |
| 5 | Input on the Goods Receipt Other screen: Quantity tab | On the Goods Receipt Other screen: Quantity tab, make the following entries and choose Enter:Qty in Unit of Entry: <Qty in UOM>Unit of Entry: PC |  |  |
| 6 | Input on the Goods Receipt Other screen: Where tab | On the Goods Receipt Other screen: Where tab, make the following entries and choose Enter:Plant: 3310Storage Location: 331C |  |  |
| 7 | Input on the Goods Receipt Other screen: Serial Numbers tab | On the Goods Receipt Other screen: Serial Numbers tab, enter the serial number. |  |  |
| 8 | Save your entries. | Click Item OK and Post. |  |  |

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

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Purchase Orders (F2872). | The Manage Workflows screen is displayed. |  |
| 3 | Create Manage Workflow | Choose Create and make the following entries:Name: Test Workflow for Purchase OrderSelect Start Conditions, and in the Start Conditions area, make the following entries:Purchasing group of purchase order is: SelectedPurchasing Group: 001Choose Add another condition and make the following entries:Total Net Amount of Purchase Order is greater than: SelectedAmount: For example, 10Currency: AEDIn Steps area, choose Create and make the following entries:Type: Release of Purchase OrderIn the RECIPIENTS area, make the following entries:Assignment By: UserUser: Select User from value help (with Employee ID PURCHASING_MANAGER)Choose OK.Step to be completed by: One of the recipientsChoose Create.Choose Save. | The workflow for Purchase Order is configured. |  |
| 4 | Activate Workflow Item | Select the Workflow Item just created and choose Activate. | The Workflow Item is activated. |  |

|  |
| --- |
| Note Please make sure default workflow Automatic Release of Purchase Order has been activated. |

#### Assign Shipping Points

Purpose

Assign the shipping points per shipping condition, loading group and plant.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The Fiori launchpad is displayed. |  |
| 2 | Access to App | Open Manage Your Solution (F1241) and search for Assign Shipping Points. | Screen displays to assign shipping points. |  |
| 3 | Maintain configuration | Maintain configuration for classifying subcontracting Billing types:Shipping Condition: 01Loading Group: 0001Plant: 3310Proposed Shipping Point: 3310Choose Save. | The data is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Assign Shipping Points | Go to the Business Processes Configuration app and search for the following activity: Assign Shipping Points.Choose the configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | Assign Shipping Points: Change displays to maintain the shipping points. |  |
| 3 | Maintain configuration | Maintain configuration for classifying subcontracting Billing types:Shipping Condition: 01Loading Group: 0001Plant: 3310Proposed Shipping Point: 3310Choose Save. | The data is saved. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| Part 1: Subcontracting without Serial Number Management |  |  |  |
| [Convert Purchase Requisition to Purchase Order](#unique_17) [page ] 22 | Purchaser | Process Purchase Requisitions - Deprecated (F1048) | Purchase order is created. |
| [Create Purchase Order](#unique_18) [page ] 23 | Purchaser | Manage Purchase Orders (F0842A) | PO is created. |
| [Monitor Subcontracting Documents (Optional)](#unique_19) [page ] 25 | Purchaser | Monitor Subcontracting Documents (F3095) |  |
| [Approve Purchase Orders (Optional)](#unique_20) [page ] 25 | Purchasing Manager | My Inbox - All Items (F0862). | Purchase orders are approved. |
| [Preview Purchase Orders (Optional)](#unique_21) [page ] 26 | Purchaser | Manage Purchase Orders (F0842A) |  |
| [Option 1 : Outbound Delivery](#unique_22) [page ] 27 |  |  |  |
| [Handling Unit Management (Optional)](#unique_23) [page ] 28 |  |  |  |
| [Create Outbound Delivery](#unique_24) [page ] 28 | Purchaser | Display Subcontracting Stocks by Supplier (ME2ON) | Outbound Delivery created. |
| [Pick and Post Goods Issue](#unique_25) [page ] 29 | Shipping Specialist | Change Outbound Delivery (VL02N) |  |
| [Option 2: Transfer Posting](#unique_26) [page ] 30 | Inventory Manager | Subcontracting Cockpit (F2948) |  |
| [Receive Goods from Subcontracting PO](#unique_27) [page ] 31 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Material document and journal entry showing receipt of purchased material and consumption of components. |
| [Create Supplier Invoice](#unique_28) [page ] 32 | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) |  |
| [Review Supplier Invoice (Optional)](#unique_29) [page ] 34 | Accounts Payable Accountant | Supplier Invoices List (F1060A) | Invoice has been reviewed. |
| Part 2: Subcontracting with Serial Number Management |  |  |  |
| [Create Purchase Order](#unique_30) [page ] 35 | Purchaser | Create Purchase Order - Advanced (ME21N) | PO is created. |
| [Approve Purchase Orders (Optional)](#unique_31) [page ] 37 | Purchasing Manager | My Inbox - All Items (F0862) | Purchase orders are approved. |
| [Create Outbound Delivery](#unique_32) [page ] 38 | Purchaser | Display Subcontracting Stocks by Supplier (ME2ON) | Outbound delivery is created. |
| [Pick and Post Goods Issue](#unique_33) [page ] 40 | Shipping Specialist | Change Outbound Delivery (VL02N) |  |
| [Create Inbound Delivery (Optional)](#unique_34) [page ] 41 | Receiving Specialist | Create Inbound Delivery (VL31N) |  |
| [Receive Goods from Subcontracting PO](#unique_35) [page ] 42 | Warehouse Clerk | Post Goods Movement (MIGO) | Material document and journal entry showing receipt of purchased material and consumption of components. |
| [Post Goods Receipt for Inbound Delivery (Option 2)](#unique_36) [page ] 43 | Receiving Specialist. | Change Inbound Delivery (VL32N) |  |
| [Create Supplier Invoice](#unique_28) [page ] 32 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | Invoice document and journal entry. |
| Part 3: Subcontracting with chargeable components |  |  |  |
| Part 4: Direct supply of Chargeable Components (Supplier -> Subcontractor) |  |  |  |
| Part 5: Issue Compliance Reports for Japan Subcontract Act |  |  |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Part 1: Subcontracting without Serial Number Management

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
| 3 | Select Purchase Requisition | Search for a Purchase Requisition for material SG23 with Sources available, and choose the link of the sources. | The Select Source of Supply screen is displayed. |  |
| 4 | Assign Source to Purchase Requisition | Choose a displayed source with a real price (not zero). | The assignment of one source to the requisition is done. The Purchase Requisitions list is displayed. |  |
| 5 | Prepare the Purchase Order | Select the purchase requisition where the assigned supplier is displayed and choose Create Purchase Order (Original). | The Purchase Order Preview screen is displayed. |  |
| 6 | Create the Purchase Order | Select Standard order from Purchase Order Type drop down list, and choose Save. | The purchase order is created. |  |
| 7 | Back to Manage Purchase Requisition | In the dialog box, choose OK. | Purchase Requisition list is displayed again. The converted Purchase Requisition has disappeared from the list. |  |

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity creates a purchase order for subcontract material. This activity is only required if you do not convert an existing purchase requisition as described in Assign Purchase Requisition / Create Subcontract Order.

|  |
| --- |
| Note You can store purchase order data as template for frequently used data. To save the data to a template, choose Save as Template. To load data from a template, choose Load from Template. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Purchaser . | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Create Purchase Order screen is displayed with a list of existing Purchasing Document Items. |  |
| 3 | Start Purchase Order creation | Without making any selection, choose Create . | The Purchase Order Screen is shown. |  |
| 4 | Create Purchase Order data | Enter the following data and choose Enter:Supplier :33300007Purchasing Org: 3310Purchasing Group: 001Company Code: 3310Currency: AEDIn the Items section, choose Create:Item Category: SubcontractingMaterial (Original): SG23Quantity: x PCNet. Price: xAEDPlant: 3310Storage Location: 331BChoose Details on the right of your item and go to Purchase Order Item screen.Choose Apply. |  |  |
| 5 | Generate Output Preview (Optional) | Choose Output Preview on the header of the purchase order An output preview in PDF format is generated.Note The Output Preview button is only avaliable when your purchase order is in status Draft, In Approval, Not Yet Sent, or Output Error.To also view subcontracting data, adapt your custom form template with the required subcontracting fields. Use the form data provider service FDP_EF_PURCHASE_ORDER_SRV, specifically the entities POSubcontractingComponentsNode and POHierSubcontractingComponentsNode.Please refer to the [Subcontracting Data in Purchase Order Output](https://help.sap.com/docs/SAP_S4HANA_CLOUD/ee9ee0ca4c3942068ea584d2f929b5b1/3c75b1e92ff14f10add44eb643643850.html) | An output preview in PDF format is generated. |  |
| 5 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A Purchase Order is created. |  |

#### Monitor Subcontracting Documents (Optional)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the Fiori App | Open Monitor Subcontracting Documents (F3095). | The Monitor Subcontracting Documents screen displays. |  |
| 3 | Monitor Subcontracting Document | Enter the following data:Subcontractor: 33300007Choose Go.Note If the subcontractor field does not appear on the screen, select the field on Adapt Filter. |  |  |
| 4 | Monitor Subcontracting Document | Choose Show More Per Row.Choose View next to Assembly Flow. | If you have multilevel subcontracting, the graph can be displayed here. |  |
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
| 1 | Log on | Log on the SAP Fiori Launchpad with the Purchasing Manager role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Approve Purchase Order | Open My Inbox - All Items (F0862). | A list of already created Purchase Orders is displayed. |  |
| 3 | Check Purchase Order Status | Click on Filter. In the pop-up, filter by Status, select statuses Ready and In Progress. Click on OK. | The Purchase Orders without follow-on documents (w/o status Follow-On Documents) and a net value of 500 AED or more have the status In Approval. |  |
| 4 | Release Purchase Order | Select the Purchase order in left of the screen and click Approve in bottom right. | The Submit Decision dialog box is displayed. |  |
| 5 | Enter Release Reason | Enter the approval reason if needed, then choose Submit. | The Purchase Order is approved. |  |
| 6 | Back to Fiori Launchpad | Choose the Home button to go back to the Fiori Launchpad. | The Fiori Launchpad is displayed. |  |

#### Preview Purchase Orders (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can preview an existing purchase order.

|  |
| --- |
| Note To also view subcontracting data, adapt your custom form template with the required subcontracting fields. Use the form data provider service FDP_EF_PURCHASE_ORDER_SRV, specifically the entities POSubcontractingComponentsNode and POHierSubcontractingComponentsNode.Please refer to the [Subcontracting Data in Purchase Order Output](https://help.sap.com/docs/SAP_S4HANA_CLOUD/ee9ee0ca4c3942068ea584d2f929b5b1/3c75b1e92ff14f10add44eb643643850.html). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on the SAP Fiori Launchpad with the Purchaser role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Purchase Orders (F0842A).Note If you want to use the Save Draft feature in this app, you have to use a personalized user. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Select Purchase Order | Enter the Purchase Order number in the Purchase Order search box, and choose Go. Select the row for the Purchase Order you want to preview and use the little arrow on the right side to check the PO detail. | The Purchase Order screen is displayed. |  |
| 4 | Preview the Purchase Order | Go to the Output Management tab. In the Output Management section, choose Show More per Row and choose Display Document. | The Purchase Order is opened in PDF format. |  |

#### Option 1 : Outbound Delivery

The purpose of this activity is to create the delivery and post goods issue.

##### Handling Unit Management (Optional)

Purpose

You can execute packing for delivery items right in a outbound delivery.

Procedure

Complete all the activities described in the test script 4MM Handling Unit Management.

##### Create Outbound Delivery

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
| 3 | Search for Component or Assembly | Set values to some filters to search Components. :Subcontractor: 33300007Plant: 3310Choose GO. | The search results show the details with the respective filter Criteria.Following columns must contain relevant data:ComponentPlantSubcontractorStock Balance |  |
| 4 | Display Purchase Order Item for a component | Choose small Arrow next to Component to expand the details. | All purchase order with items number corresponding to the component must be displayed in Purchase Order Items column. |  |
| 5 | Create Delivery | Choose a PO Item and then choose Create Delivery. |  |  |
| 6 | Enter Detail Data | Make the following entries:Material (Original): RM13/RM14Storage Location: 331CShipping Point: 3310Note Please make sure the RM13/RM14 have stock in the storage location. If no, please do initial stock for them.It's also possible to post goods issue towards reservation if there's any. |  |  |
| 7 | Item OK | Verify if the processing status is Valid. |  |  |
| 8 | Post | Choose Create Delivery. | The system displays the messageDelivery 00xxxxxxxx has been saved.. |  |

##### Pick and Post Goods Issue

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

#### Option 2: Transfer Posting

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
| 1 | Logon | Log on to the SAP Fiori launchpad as an Inventory Manager. | The Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Subcontracting Cockpit (F2948) | The Subcontracting Cockpit (Original) screen is displayed. |  |
| 3 | Search for Component or Assembly | Set values to some filters to search Components. :Subcontractor: 33300007Plant: 3310Choose GO. | The search results show the details with the respective filter Criteria. Following columns must contain relevant data:ComponentPlantSubcontractorStock Balance |  |
| 4 | Display Purchase Order Item for a component | Choose small Arrow next to Component to expand the details | All purchase order with items number corresponding to the component must be displayed in “Purchase Order Items” column. |  |
| 5 | Post Goods Issue (Original) | Choose a PO Item and then choose Post Goods Issue . | There will be navigation to the ‘Post Goods Issue’ app. |  |
| 6 | Enter detail data | Make the following entries:Material : RM13/RM14Storage Location: 331CNote Please make sure the RM13/RM14 have stock in the storage location. If no, please do initial stock for them.It's also possible to post goods issue towards reservation if there's any. |  |  |
| 7 | Item OK | check if the processing status is Valid |  |  |
| 8 | Post | Select all the items and Post Goods Issue . | The system displays the message Materialdocument 4900000XX XXXX posted . |  |

#### Receive Goods from Subcontracting PO

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
| 1 | Log on | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The Fiori Launch Pad is displayed. |  |
| 2 | Open Post Goods Movement tile | Open Post Goods Receipt for Purchasing Document (F0843). | The Post Goods Receipt for Purchasing Document screen is displayed. |  |
| 3 | Select Goods Receipt Order screen | Enter your PO number or search your subcontracting purchase order. | The items of the selected Purchase Order display. |  |
| 4 | Select Item | Select the item for which a goods receipt is to be posted. |  |  |
| 5 | Post | Choose Post. | The system displays the message1 document(s) created: Material document 5000000XX 20XX. |  |

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
| 4 | Enter Purchase Order References | In Purchasing Document References, make the following entries (use a PO you created previously) and choose Enter.Make the following entries (use a PO you created previously).Reference Document Category: Purchase Order/ Scheduling AgreementPurchase Order/Scheduling Agreement: <PO number> | The Purchase Document References screen displays. |  |
| 5 | Select Purchase Order Items | Check the selection of the Purchase Order Items.Confirm the warning messages. | All items of the selected Purchase Order are added to the Purchase Order Item table.You should see material items which refer to the entered purchase order document. |  |
| 6 | Check the Invoice Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Purchase Order Item's table displays. |  |
| 7 | Check Tax code | In the section Tax check if there is tax code information. | In the Tax tab, you should see the same tax codes as in the items.If there is no tax, specify the tax code <Input Tax Code>. |  |
| 8 | Check the balance | Calculate the tax amount from the item amount multiplied by the tax value. | The balance should be zero (or within the defined tolerance). |  |
| 9 | Simulate Supplier Invoice and Check Messages | Choose Simulate.If there are no differences(or if the value is within the defined tolerance), a new screen Simulation appears. You can check the simulation results in Simulation Overview and Simulation Details area.The Supplier Invoice is complete to post. Check the Gross Invoice Amount against the items plus tax amount (if tax code is,<Input Tax Code> you do not have any tax amount) | The supplier invoice is complete to post. |  |
| 10 | Post Invoice | Choose Post. | The invoice is posted. |  |

#### Review Supplier Invoice (Optional)

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
| 1 | Log on | Log on to the SAP Fiori Launchpad as an Accounts Payable Accountant. | The Fiori Launchpad is displayed. |  |
| 2 | Open the Fiori App | Open Supplier Invoices List (F1060A). |  |  |
| 3 | Enter General Data | Make the following entries:Invoice Party: 33300007Company Code: 3310Choose Go. |  |  |
| 4 | Check invoice | Check Display to check the invoice. |  |  |

### Part 2: Subcontracting with Serial Number Management

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity creates a purchase order for subcontract material. This activity is only required if you do not convert an existing purchase requisition as described in Assign Purchase Requisition / Create Subcontract Order.

|  |
| --- |
| Note You can store purchase order data as template for frequently used data. To save the data to a template, choose Save as Template . To load data from a template, choose Load from Template . |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The Fiori Launch Pad is displayed. |  |
| 2 | Open Create Purchase Order | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order (Original) screen is displayed with a list of existing Purchasing Document Items. |  |
| 3 | Enter Purchase Order data | Enter the following data and choose Enter:Order type : Standard POSupplier (Original) : 33300007In the area of Header / Org. Data :Purchasing Org : 3310Purchasing Group : 001Company Code: 3310In the area of Item Overview:Item Category : LMaterial (Original) : SG27Quantity: 2 PCNet. Price: x AEDPlant: 3310Storage Location: 331BIn the area of Item Detail:Switch to Delivery Schedule, and choose Assign Serial Number. Choose Create Serial Number Automatically, and then choose Continue. | All data is entered. The Item Detail screen displays.Depending on the relevance of chain liability for the supplier on a purchase order, some steps or fields may or may not be displayed. If chain liability is relevant, you must enter the start and finish dates for the work, along with the number of hours to be worked. If you are posting a portion of the invoice to your sub-contractor’s blocked account, enter the percentage of the line items that are wage-relevant. This enables the system to propose the amount to be posted to the blocked account. |  |
| 4 | (Optional) Confirmation | If you want to use Serial Numbers in Subcontracting Components in Inbound Delivery:Switch to Confirmations, choose Conf. Control: 0004 Inbound Delivery | Confirmation key is entered. |  |
| 5 | Generate Output Preview (Optional) | Choose Print Preview on the top of the purchase order and select the output option as required, choose Display Document.Note The Print Preview button is only available when your purchase order is in status In Approval, Not Yet Sent, or Output Error when the purchase order is in display mode.To also view subcontracting data,Adapt your custom form template with the required subcontracting fields. Use the form data provider service FDP_EF_PURCHASE_ORDER_SRV, specifically the entities POSubcontractingComponentsNode and POHierSubcontractingComponentsNode.For saved purchase orders, choose Components in the Material Data section to display each subcontracting material using Print Preview in change mode. For purchase orders that are in approval, not yet sent, or have an output error, Print Preview appears in display mode.Please refer to the [Subcontracting Data in Purchase Order Output](https://help.sap.com/docs/SAP_S4HANA_CLOUD/ee9ee0ca4c3942068ea584d2f929b5b1/3c75b1e92ff14f10add44eb643643850.html). |  |  |
| 6 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use.Note You have to choose Components in tab Material Data for each subcontracting material to be display in Print Preview in change mode or display mode post the Purchase Order is saved. | A Purchase Order is created. |  |

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
| 1 | Log on | Log on to the SAP Fiori launchpad as aPurchasing Manager. | The Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | A list of already created Purchase Orders is displayed. |  |
| 3 | Check Purchase Order Status | Search for Purchase Order with Need Approval Status. | The Purchase Orders without follow-on documents (w/o status Follow-On Documents) and a net value of 500 AED or more have the status In Approval. |  |
| 4 | Release Purchase Order | Select the Purchase Order on the left side of the screen and choose Approve at the bottom right. | The Submit Decision screen is displayed. |  |
| 5 | Enter Release Reason | Enter the approval reason if necessary, and then choose Submit. | The Purchase Order is approved. |  |
| 6 | Back to Fiori Launch Pad | Choose the Home button to go back to the Fiori Launch pad. | The Fiori Launch Pad is displayed. |  |

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
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Display Subcontracting Stocks by Supplier (ME2ON). | The app name screen displays. |  |
| 3 | Subcontracting Cockpit (Original) | Enter the following data:Supplier (Original) : 33300007Components Provided: RM33 and RM34With requirements from subcontracting Purchase Requisitions: XWith external receipts from Purchase Requisitions: XWith external receipts from Purchase Orders: XChoose Execute. |  |  |
| 4 | Subcontracting Cockpit (Original) | Expand the group of Requirements via SC Orders for below materials:Material (Original) : RM33 and RM34Find the line items with your purchase order number. Use Ctrl to select both lines.Select Create Delivery. |  |  |
| 5 | Creating Delivery for Subcontracting Purchase Orders | Enter Stor.Location for both lines:Stor.Location: 331CUse Ctrl to select the both lines and choose Create Delivery.Note down your delivery number. |  |  |

#### Handling Unit Management (Optional)

Purpose

You can execute packing for delivery items right in a outbound delivery.

Procedure

Complete all the activities described in the test script 4MM Handling Unit Management.

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
| 3 | Change Outbound Delivery (Original) | Enter the following data:Outbound Delivery: <your delivery>Choose Continue. |  |  |
| 4 | Picking | Choose Picking tab.Enter picked quantity equal to the delivery quantity. |  |  |
| 5 | Serial number | Select line item 10Choose Menu > Extras > Serial Number .Choose Create serial number automatically.Note down the serial number created.Choose Continue. |  |  |
| 6 |  | Repeat above step for line item 20. |  |  |
| 7 | Post Goods Issue (Original) | On the Delivery for Subcon. xxxxxxx Change: Overview screen, choose Post Goods Issue. |  |  |

#### Create Inbound Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to create inbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Create Inbound Delivery (VL31N). | The Create Inbound Delivery is displayed. |  |
| 3 | Create Inbound Delivery | Enter the following data:Supplier: 33300007Purchase Order: XXX (Enter the purchase order number created in previous step).Choose Continue. |  |  |
| 4 | Enter Serial Number | Select line item 10.Choose SC Components.In the dialog box Edit Components of New Delivery – Item 10, choose following items:RAW33, PD, Subcontracting (RM33)Choose Serial Numbers.In the pop-up screen Maintain Serial Numbers, enter the serial number noted in last chapter for RM33.Choose Continue (Enter).Repeat the same to RAW34, PD, Subcontracting(RM34)Choose Assign Serial Numbers.In the pop-up screen Maintain Serial Numbers, enter the serial number noted in last chapter for RM34.Choose Confirm. | Picking status becomes green. |  |
| 5 | Save Inbound Delivery | Choose Save.Note down the delivery number you created. | The messageInbound Delivery 18XXXXXXXX has been saved.displays. |  |

#### Receive Goods from Subcontracting PO

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
| 1 | Log on | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The Fiori Launch Pad is displayed. |  |
| 2 | Open Post Goods Movement tile | Open Post Goods Movement (MIGO). | The Post Goods Receipt for Purchase Order (Original). screen is displayed. |  |
| 3 | Select Goods Receipt Order screen | On the Goods Receipt Order screen, make the following entries and choose Enter:Goods Receipt: <Select>Purchasing Order: <Select>Order number:<Purchase Order number>GR goods receipt:101 | The items of the selected Purchase Order display. |  |
| 4 | Choose the Quantity tab and confirm the quantity | Confirm the quantity. |  |  |
| 5 | Select Item ok Indicator | Select the Item OK checkbox. |  |  |
| 6 | Serial number | Expand item SG27.Select the line item for raw material RM33.In detailed data, switch to Serial Number tab.Enter the serial number noted in last chapter for RM33.Select the line item for raw material RM34.In detailed data, switch to Serial Number tab.Enter the serial number noted in last chapter for RM34. |  |  |
| 7 | Post | Choose Post. | The system displays the message1 document(s) created: Material document 5000000XX 20XX.. |  |

#### Post Goods Receipt for Inbound Delivery (Option 2)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

n this step, you post the goods receipt for the inbound delivery against the subcontracting purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Change Inbound Delivery (VL32N). | The Change Inbound Delivery screen is displayed. |  |
| 3 | Enter Inbound Delivery | Enter the inbound delivery number and choose Enter. | The system displays the data for the goods receipt on the Inbound Delivery Change screen. |  |
| 4 | Post Putaway Quantity | Enter the putaway quantity and check the storage location to be posted.Choose Save. |  |  |
| 5 | Post Goods Receipt | Choose Post Goods Receipt. | The system displays the messageGoods receipt for inbound delivery 18xxxxxxx posted (material document 5xxxxxxxxx). |  |

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
| 4 | Enter Purchase Order References | In Purchasing Document References, make the following entries (use a PO you created previously) and choose Enter.Make the following entries (use a PO you created previously).Reference Document Category: Purchase Order/ Scheduling AgreementPurchase Order/Scheduling Agreement: <PO number> | The Purchase Document References screen displays. |  |
| 5 | Select Purchase Order Items | Check the selection of the Purchase Order Items.Confirm the warning messages. | All items of the selected Purchase Order are added to the Purchase Order Item table.You should see material items which refer to the entered purchase order document. |  |
| 6 | Check the Invoice Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Purchase Order Item's table displays. |  |
| 7 | Check Tax code | In the section Tax check if there is tax code information. | In the Tax tab, you should see the same tax codes as in the items.If there is no tax, specify the tax code <Input Tax Code>. |  |
| 8 | Check the balance | Calculate the tax amount from the item amount multiplied by the tax value. | The balance should be zero (or within the defined tolerance). |  |
| 9 | Simulate Supplier Invoice and Check Messages | Choose Simulate.If there are no differences(or if the value is within the defined tolerance), a new screen Simulation appears. You can check the simulation results in Simulation Overview and Simulation Details area.The Supplier Invoice is complete to post. Check the Gross Invoice Amount against the items plus tax amount (if tax code is,<Input Tax Code> you do not have any tax amount) | The supplier invoice is complete to post. |  |
| 10 | Post Invoice | Choose Post. | The invoice is posted. |  |

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Accounts Payable (J60) | Complete the following activities described in the test script:Payment RunPost Outgoing Payment |
| Accounting and Financial Close (J58) | Dispose of the inventory by returning to the vendor. Do not process any other activities in this document after running the external process.Using the master data from this document, complete the following activities described in the test script:Run the test script in its entirety, using the master data from this test script document. |
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
> Flagged while digesting this document, not verified: Overview Table app names differ from the procedures: it lists 'Process Purchase Requisitions - Deprecated (F1048)' (procedure uses F1048A), ME2ON for Part 1 Create Outbound Delivery (procedure uses Subcontracting Cockpit F2948), and 'Create Supplier Invoice - Advanced (MIRO)' for Part 1 (procedure uses Create Supplier Invoice F0859).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Approval threshold wording is inconsistent: the note says only POs 'higher than 500.00 AED' can be released, while the expected result says POs with a net value of '500 AED or more' have status In Approval.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/test-script-scheduling-agreement-for-subcontracting-procurement-2nx-ae]]
- related-to :: [[10-procurement/test-script-subcontracting-consumer-products-5w4-ae-sap-s-4hana-cloud]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BMY_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 74,272 chars in the whole document
