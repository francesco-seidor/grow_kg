---
id: 10-procurement/test-script-procurement-of-production-components-consumer-products-5w3
title: "Test Script: Procurement of Production Components – Consumer Products (5W3_AE) (5W3_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5W3 (AE): procure batch-managed raw material with QM and packaging without QM, plant 3310."
cluster: 10-procurement
tags: [kb/procurement, topic/direct-material-procurement, topic/end-to-end-produce-and-sell]
aliases: [5W3_S4CLD2608_BPD_EN_AE]
keywords: [Direct Material Procurement, procurement of production components, purchase requisitions, purchase orders, flexible workflow approval, automatic purchase order creation, source inspection, goods receipt inspection, usage decision, goods receipt]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5W3_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1124
topic: 10-procurement/direct-material-procurement
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Procurement of Production Components – Consumer Products (5W3_AE) (5W3_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5W3_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Direct Material Procurement** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Procurement of Production Components – Consumer Products (5W3_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232857774)

[2 Prerequisites 5](#_Toc232857775)

[2.1 System Access 5](#_Toc232857776)

[2.2 Roles 5](#_Toc232857777)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232857778)

[2.4 Business Conditions 9](#_Toc232857779)

[2.5 Preliminary Steps 9](#_Toc232857780)

[2.5.1 Create Purchasing Info Record 9](#_Toc232857781)

[2.5.2 Check Flexible Workflow for Purchase Requisitions Approval 12](#_Toc232857782)

[2.5.3 Configure Flexible Workflow for Purchase Requisition 13](#_Toc232857783)

[2.5.4 Manage Conditions to Restart Flexible Workflow for Purchase Requisitions 14](#_Toc232857784)

[2.5.5 Check Flexible Workflow for Purchase Order Approval 16](#_Toc232857785)

[2.5.6 Configure Flexible Workflow for Purchase Order 17](#_Toc232857786)

[2.5.7 Manage Conditions to Restart Flexible Workflow for Purchase Orders 18](#_Toc232857787)

[2.5.8 Master Data Update for Automatic Purchase Order Creation from Purchase Requisition 20](#_Toc232857788)

[2.5.8.1 Change Material Master Data - Purchasing Data 20](#_Toc232857789)

[2.5.8.2 Change Supplier Master Data - Purchasing Organization Data 21](#_Toc232857790)

[2.5.8.3 Generate Source List 22](#_Toc232857791)

[2.5.9 Expand Inspection Method Long Text (Optional) 24](#_Toc232857792)

[2.5.10 Change Inspection Plan for Raw Material 25](#_Toc232857793)

[2.5.11 Create Quality Info Record in Procurement (Optional) 26](#_Toc232857794)

[2.5.12 Create Batch (Optional) 27](#_Toc232857795)

[3 Overview Table 29](#_Toc232857796)

[4 Test Procedures 33](#_Toc232857797)

[4.1 Procurement of Stock Material with QM – Raw Material 33](#_Toc232857798)

[4.1.1 Create Purchase Requisition 33](#_Toc232857799)

[4.1.1.1 Option 1: Create Purchase Requisition via MRP Run 33](#_Toc232857800)

[4.1.1.1.1 Option 1: Create Planned Independent Requirements 33](#_Toc232857801)

[4.1.1.1.2 Option 2: Create Planned Independent Requirements by Upload File 35](#_Toc232857802)

[4.1.1.1.3 Material Requirements Planning at Plant Level 37](#_Toc232857803)

[4.1.1.2 Option 2: Create Purchase Requisition manually 39](#_Toc232857804)

[4.1.2 Create Purchase Order 41](#_Toc232857805)

[4.1.2.1 Option 1: Convert Purchase Requisitions to Purchase Orders 41](#_Toc232857806)

[4.1.2.2 Option 2: Create Purchase Order Manually 42](#_Toc232857807)

[4.1.3 Preview Purchase Order (Optional) 45](#_Toc232857808)

[4.1.4 Change Purchase Order (Optional) 46](#_Toc232857809)

[4.1.5 Monitor Purchase Order Items (Optional) 47](#_Toc232857810)

[4.1.6 Execute Mass Changes to Purchase Orders (Optional) 48](#_Toc232857811)

[4.1.7 Source Inspection Process (Optional) 50](#_Toc232857812)

[4.1.7.1 Review Quality Settings in Material Master (Optional) 50](#_Toc232857813)

[4.1.7.2 Review Quality Info Record (Optional) 51](#_Toc232857814)

[4.1.7.3 Display Inspection Plan for Inspection Characteristics (Optional) 52](#_Toc232857815)

[4.1.7.4 Quality Inspection (Inspection before Goods Receipt) 53](#_Toc232857816)

[4.1.7.4.1 Create Inspection Lot 53](#_Toc232857817)

[4.1.7.4.2 Display Quality Technician Overview (Optional) 55](#_Toc232857818)

[4.1.7.4.3 Change Inspection Lot and Assign Batch 55](#_Toc232857819)

[4.1.7.4.4 Record Inspection Results 57](#_Toc232857820)

[4.1.7.4.5 Display Quality Engineer Overview (Optional) 58](#_Toc232857821)

[4.1.7.4.6 Make Usage Decision 60](#_Toc232857822)

[4.1.8 Post Goods Receipt 61](#_Toc232857823)

[4.1.9 Preview Goods Receipt Slip and Label (Optional) 62](#_Toc232857824)

[4.1.10 Check Goods Receipt Details (Optional) 63](#_Toc232857825)

[4.2 Quality Inspection (Goods Receipt Inspection) 64](#_Toc232857826)

[4.2.1 Display Material Stock Before Quality Inspection (Optional) 64](#_Toc232857827)

[4.2.2 Display Inspection Plan for Inspection Characteristics (Optional) 65](#_Toc232857828)

[4.2.3 Display Quality Technician Overview (Optional) 67](#_Toc232857829)

[4.2.4 Display Open Inspection Lots (Optional) 68](#_Toc232857830)

[4.2.5 Record Inspection Results 69](#_Toc232857831)

[4.2.6 Display Quality Engineer Overview (Optional) 72](#_Toc232857832)

[4.2.7 Make Usage Decision 74](#_Toc232857833)

[4.2.8 Display Material Stock after Quality Inspection (Optional) 76](#_Toc232857834)

[4.2.9 Display Inspection Results History (Optional) 77](#_Toc232857835)

[4.3 Procurement of Stock Material without QM – Packaging 78](#_Toc232857836)

[4.3.1 Create Purchase Requisiton 78](#_Toc232857837)

[4.3.1.1 Option 1: Create Purchase Requisition via MRP run 78](#_Toc232857838)

[4.3.1.2 Option 2: Create Purchase Requisition manually 79](#_Toc232857839)

[4.3.2 Approve Purchase Requisition 81](#_Toc232857840)

[4.3.3 Automatic Conversion of Purchase Requisition to Purchase Order 82](#_Toc232857841)

[4.3.4 Approve Purchase Order (Optional) 83](#_Toc232857842)

[4.3.5 Post Goods Receipt 84](#_Toc232857843)

[4.4 Evaluations 85](#_Toc232857844)

[4.4.1 Batch Information Cockpit – Top-Down and Bottom-Up Analysis 85](#_Toc232857845)

[5 Appendix 88](#_Toc232857846)

[5.1 Process Integration 88](#_Toc232857847)

[5.2 Preceding Processes 88](#_Toc232857848)

[5.3 Succeeding Processes 88](#_Toc232857849)

## Purpose

Overview

This scope item outlines the purchasing process in the Consumer Products industry for procuring batch-managed raw materials (for example, coffee beans) and packaging materials (for example, bags, cartons) needed for production (for example, in coffee displays).

The process operates as a procure-to-stock scenario. It uses purchase requisitions generated by the Material Requirements Planning (MRP) process or manually by a requester. You can convert a purchase requisition to a purchase order manually or automatically. Alternatively, the purchase orders can be created manually.

Purchase orders may require approval before being issued to a supplier. Once approved, goods are shipped from the supplier, and the goods receipt is created with reference to the corresponding purchase order.

For some materials, quality inspection activities may be relevant upon goods receipt. For the raw coffee beans, a quality inspection is performed. For packaging material, it isn't necessary in this scope item.

At goods receipt, the material is posted to quality inspection stock, and an inspection lot is created based on an inspection plan. The quality technician records the inspection results by selecting the relevant work center. Based on the results, the quality engineer makes a usage decision, such as accepting or rejecting the material, posting the material to unrestricted stock or blocked stock, or triggering return to the supplier, with the option of posting as a consumed sample.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data, and business conditions.

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
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Manager - Procurement | SAP_BR_MANAGER_PROCUREMENT | My Inbox / My Inbox - Buying | SAP_CORE_SPT_MYINBOX_PC / SAP_MM_SPT_BUYING_MYINBOX_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Quality Planner | SAP_BR_QUALITY_PLANNER | Quality Planning | SAP_BR_QUALITY_PLANNER |  |
| Quality Technician | SAP_BR_QUALITY_TECHNICIAN | Quality Inspection | SAP_BR_QUALITY_TECHNICIAN |  |
| Quality Engineer | SAP_BR_QUALITY_ENGINEER | Quality Engineering | SAP_BR_QUALITY_ENGINEER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Material Master Data:

| Data | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | RM0501 | Raw Coffee Beans- Arabica | Batch Managed Raw Material |
| Material | PK0501 | Coffee Bag "Medium" 1 kg | Batch Managed Packaging Material, MRP and Costing Relevant |
| Material | PK0502 | Coffee Bag "Dark" 1 kg | Batch Managed Packaging Material, MRP and Costing Relevant |
| Material | PK0504 | Label | Batch Managed Packaging Material |
| Material | PK0507 | Carton for 12x 1 kg Bags | Packaging Material, MRP and Costing relevant |
| Material | PK0508 | Display Carton Coffee Beans 48 * 1 kg | Packaging Material, MRP and Costing relevant |

Organization Data:

| Data | Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331R | Storage Location Returns |  |
| Controlling Area | A000 | Controlling Area A000 |  |
| Cost Center | 33101301 | Manufacturing 1 (AE) |  |

Suppliers:

Below mentioned Suppliers (Business Parters) will be used in this scenario.

| Data | Value | Details | Comments |
| --- | --- | --- | --- |
| Supplier | 33305001 | Domestic AE Supplier CP001 |  |
| Supplier | 33300002 | Domestic Supplier 2 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchasing Organization | 3310 | Purchase Organization 3310 |  |

Quality Master Inspection Characteristics:

The following Master Inspection Characteristics are used in this scenario:

| Master Data | Value | Master Data Details | Comments |
| --- | --- | --- | --- |
| Master Inspection Characteristic | YQM00006 | Relative Humidity (%) |  |
| Master Inspection Characteristic | YQM00010 | Pest Control |  |
| Master Inspection Characteristic | YQM00011 | Defect Grade Raw Coffee Beans (NYBOT) |  |
| Master Inspection Characteristic | YQM00012 | Sensory Raw Coffee Beans (SCAA) |  |

Quality Inspection Plan:

Quality Inspection Plan uses the standard work center ‘QMLABS’ provided as part of standard best practices.

For more information on creating your own master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS |
| 3Y1 | Create Product Master of Type "Packaging" - MDS |
| BNQ | Create Quality Inspection Plan - MDS |
| BNE | Create Supplier Master - MDS |
| BHD | Create Purchasing Info Record - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation | You have completed the step described in the Standard Cost Calculation (BEG) test script. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |
| J58 - Accounting and Financial Close | Execute to create open posting periods. |

### Preliminary Steps

#### Create Purchasing Info Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create Purchasing Info Records for Raw Material RM0501 and Supplier 33300002 and for the Packaging Materials PK0501, PK0502, PK0504, PK0507 and PK0508 and Supplier 33305001.

|  |
| --- |
| Note If the Purchasing Info Records for the materials already exists in the system, you can skip this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982) . | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen is displayed. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: StandardPurchasing Organization: 3310Supplier: 33300002Material: RM0501Plant: 3310Purchasing Group: 002 | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: TodayAvailable To: 31.12.9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: EXWIncoterm Location 1: VENDOR | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: 1Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10.0Tax Code: <Input Tax Code>Tax Rate Valid From: Select value from F4 helpNote When the TDT (time dependent tax) is activated via SSCUI 101016 (Define Tax Codes for Sales and Purchases) for Country of company code and Tax Code is given, the Tax Rate Valid From field is mandatory. You can enter current date, which will be adjusted to validity start date of tax code according to the setting in SSCUI.Order Unit: KGStandard Order Quantity: 10Goods-Receipt-Based Invoice Verification: selectNo Evaluated Receipt Settlement: select | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Conditions section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To: 31.12.9999Amount: 4.44Pricing Unit: 1Currency: AEDChoose Apply. | Condition Data is added. |  |
| 9 | Enter Reference Data (optional) | You can enter reference data. | Reference data is added. |  |
| 10 | Create your data | Choose Create. | The purchasing info record is created. |  |
| 11 | Repeat Steps | Repeat the above steps to create the Info Record for the packaging materials using the following data:PK0501: Supplier 33305001, Purchasing Group 002, net price: 45 AED per 100 PC.PK0502: Supplier 33305001, Purchasing Group 002, net price: 45 AED per 100 PC.PK0504: Supplier 33305001, Purchasing Group 002, net price: 5 AED per 100 PC.PK0507: Supplier 33305001, Purchasing Group 002, net price: 1,30 AED per 1 PC.PK0508: Supplier 33305001, Purchasing Group 002, net price: 47,50 AED per 1 PC. |  |  |

#### Check Flexible Workflow for Purchase Requisitions Approval

Purpose

In this procedure, you check the flexible workflow for purchase requisition approval.

When you use the flexible workflow to approve the purchase requisition, make sure Flexible Workflow for Purchase Requisition with NB document is activated, and Flexible Workflow for Purchase Requisition Approval is configured.

The flexible workflow for Purchase Requistions can be activated on document type level either on header level (overall release activated) or on line item level (overall release not activated). In this scenario the line item activation is executed.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution: Realize Phase screen, search Activate Flexible Workflow for Purchase Requisitions, then choose Search.Select the line of the item and go to the next screen.On the Configure Your Solution - Requirements Processing screen, choose Configure on the line of configuration step with name Activate Flexible Workflow for Purchase Requisitions. | The Document Types Purchase requisition Change screen is displayed. |  |
| 5 | Check Flexible Workflow for PR Approval | Verify the following entries:Purchasing Doc. Type: NBOverall Release for Purchase Requisition: <Not Selected>Scenario based workflow: <Selected> | The Scenario based workflow is active for Purchase Requisitions with Document Type: NB. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflow for Purchase Requisitions.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Document Types Purchase requisition Change screen displays. |  |
| 3 | Check Flexible Workflow for PR Approval | Verify the following entries:Purchasing Doc. Type: NBOverall Release for Purchase Requisition: <Not Selected>Scenario based workflow: <Selected> | The Scenario based workflow is active for Purchase Requisitions with Document Type: NB. |  |

Result

The Scenario based workflow is active for Purchase Requistions with Document Type: NB. The flexible workflow is set up so that the approval will be executed on purchase requisition line item level. The approval on Purchase Requistion header level is not activated.

#### Configure Flexible Workflow for Purchase Requisition

Purpose

In this procedure, you configure release conditions for Purchase Requisition Approval on the line item level.

|  |
| --- |
| Note When you start to process this step, please make sure that the flexible workflow for purchase requisition document type NB has been activated in your system. |

|  |
| --- |
| Note For the Workflow Name and Steps Name, you can translate to other languages via app Workflow Content Translation, for example translate it from English to German. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Workflows for Purchase Requisitions (F2705). | The Manage Workflows screen is displayed. |  |
| 3 | Choose Workflow Scenario | Choose workflow Release of Purchase Requisition Item | All existing workflows are displayed. |  |
| 4 | Create Manage Workflow | Choose Create, and make the following entries:Workflow Name: <Test Workflow for Purchase Requisition>From the Start Conditions section, add the following preconditions:Purchasing Group of the purchase requisition item is: SelectedPurchasing Group: 002Choose Create another condition, and make the following entries:Net amount is equal to or greater than: 10Currency: AEDIn the Steps area, choose Create and make the following entries:Step Type: Release of Purchase Requisition itemIn the RECIPIENTS area, make the following entries:Assignment By: UserUser: Select User from value help (with Employee ID MANAGER_PROCUREMENT)Choose OK.Step to be completed by: One of the recipients.Choose Create.Choose Save. | The Workflow for Purchase Requisition is configured. |  |
| 5 | Activate Workflow Item | Select the Workflow Item just created, and choose Activate. | The Workflow Item is activated. |  |

|  |
| --- |
| Note Please make sure default workflow Automatic Approval of Purchase Requisition Item has been activated as last step. |

#### Manage Conditions to Restart Flexible Workflow for Purchase Requisitions

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note If country version needs to be added, choose Set Country Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution: Realize Phase screen, search Manage Conditions to Restart Flexible Workflow, then choose Search.Select the line of the item for Item Name Requirements Processing, and go to the next screen.On the Requirements Processing screen, search for Manage Conditions to Restart Flexible Workflow for Purchase Requisitions and choose Configure. | The Manage Conditions to Restart Flexible Workflow screen is displayed. |  |
| 5 | Conditions to Restart Flexible Workflow | You can see that the Purchase Requisition Attributes have been enabled for the Restart Flexible Workflow for Purchase Requisitions, Self-Service Procurement and Professional Procurement. | The conditions to Restart Flexible Workflow for Purchase Requisitions has been verified. |  |

SAP Central Business Configuration:

| Test Step # | Test Step | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Check Define Rules for Determination of Master Form Template | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Manage Conditions to Restart Flexible Workflow for Purchase Requisitions.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Conditions to Restart Flexible Workflow | You can see that the Purchase Requisition Attributes have been enabled for the Restart Flexible Workflow for Purchase Requisitions, Self-Service Procurement and Professional Procurement. | The conditions to Restart Flexible Workflow for Purchase Requisition have been verified. |  |

Result

The conditions to Restart Flexible Workflow for Purchase Requisition have been verified.

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

In this procedure, you configure release conditions for Purchase Order Approval.

|  |
| --- |
| Note When you start to process this step, please make sure that the flexible workflow for purchase document type NB has been activated in your system. |

|  |
| --- |
| Note For the Workflow Name and Steps Name, you can translate to other languages via app Workflow Content Translation, for example translate it from English to German. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Workflows for Purchase Orders (F2872). | The Manage Workflows screen is displayed. |  |
| 3 | Create Manage Workflow | Choose Create, and make the following entries:Workflow Name: <Test Workflow for Purchase Order>From the Start Conditions section, add the following preconditions:Purchasing group of purchase order is: SelectedPurchasing Group: 002Choose Create another condition, and make the following entries:Total net amount of purchase order is greater than: SelectedAmount: For example, 10Currency: AEDIn the Steps area, choose Create and make the following entries:Step Type: Release of Purchase OrderIn the Recipients area, make the following entries:Assignment By: UserUser: Select User from value help (with Employee ID PURCHASING_MANAGER)Choose OK.Step to be completed by: One of the recipients.Choose Create.Choose Save. | The Workflow for Purchase Order is configured. |  |
| 4 | Activate Workflow Item | Select the Workflow Item just created, and choose Activate. | The Workflow Item is activated. |  |

|  |
| --- |
| Note Please make sure default workflow Automatic Release of Purchase Order has been activated. |

#### Manage Conditions to Restart Flexible Workflow for Purchase Orders

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note If country version needs to be added, choose Set Country Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution: Realize Phase screen, search Manage Conditions to Restart Flexible Workflow, then choose Search.Select the line of the item for Item Name Purchase Order Processing, and go to the next screen.On the Purchase Order Processing screen, search for Manage Conditions to Restart Flexible Workflow for Purchase Orders and choose Configure. | The Manage Conditions to Restart Flexible Workflow for POs screen is displayed. |  |
| 5 | Conditions to Restart Flexible Workflow | You can see that the Purchase Order Attributes have been enabled for the Restart Flexible Workflow for PO and Always Restart for Restart Type. | The conditions to Restart Flexible Workflow for Purchase Order have been verified. |  |

SAP Central Business Configuration:

| Test Step # | Test Step | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Check Define Rules for Determination of Master Form Template | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Manage Conditions to Restart Flexible Workflow.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Conditions to Restart Flexible Workflow | You can see that the Purchase Order Attributes have been enabled for the Restart Flexible Workflow for PO and Always Restart for Restart Type. | The conditions to Restart Flexible Workflow for Purchase Order have been verified. |  |

Result

The conditions to Restart Flexible Workflow for Purchase Order has been verified.

#### Master Data Update for Automatic Purchase Order Creation from Purchase Requisition

|  |
| --- |
| Note If you want to perform the step Procurement of Stock Material without QM - Packaging, run these Preliminary steps. |

Prerequisite

By default, you have completed the creation of master data, including material master data, supplier master data and Info Record.

You can find general information on how to create master data objects in the Master Data Scripts (MDS) BNF and BNE.

##### Change Material Master Data - Purchasing Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for changing material master data for the materials used for automatic purchase order creation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Master Data Specialist - Product Data role. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Change Material (MM02). | The Change Material (Initial Screen) displays. |  |
| 3 | Enter Material Basic Data | On the Change Material screen, make the following entries:Material: PK0501Choose Select View(s). | The Select View(s) screen displays. |  |
| 4 | Choose Views | On the Select View(s) screen, choose Purchasing and Continue. | The Organizational Levels displays. |  |
| 5 | Enter Organizational Levels Data | On the Organizational Levels screen, make the following entries:Plant: 3310Choose Continue. | The Change Material XXXXX (Material general) displays. |  |
| 6 | Select Autom.PO | Scroll down to the General Data section and select the following:Autom.PO: <selected> | Autom.PO is selected. |  |
| 7 | Save your data | Choose Save. | The material master data is updated. |  |
| 8 | Repeat Steps | Repeat the steps above for the other packaging materials PK0502, PK0504, PK0507 and PK0508. |  |  |

Result

The Autom.PO checkbox is selected.

##### Change Supplier Master Data - Purchasing Organization Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for changing supplier master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using the Master Data Specialist - Business Partner Data role. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Choose Maintain Business Partner (BP). | The Maintain Business Partner screen displays. |  |
| 3 | Enter Business Partner | Make the following entry and choose Enter:Find: Business PartnerBy: Supplier NumberSupplier Number: 33305001Choose Start. The Supplier row displays.Double-click the Supplier Partner row. | The Supplier information screen displays. |  |
| 4 | Switch to Change mode | Ensure you are in Change mode. Otherwise, select Switch Between Display and Change. | The Change mode screen displays. |  |
| 5 | Change BP role | In the Change in BP role field, choose the following value: Supplier (defined) |  |  |
| 6 | Open Purchasing Organization Data | Choose the Purchasing tab at the top of the screen. | The Purchasing Organization sub section screen displays. |  |
| 7 | Enter Purchasing Data | Choose Switch Organization.Make the following entry and choose Enter:Purch. Organization: 3310 |  |  |
| 8 | Select Automatic PO checkbox | From the Purchasing Data section, scroll down to the Additional Purchasing Data section, make the following entry:Automatic Purchase Order: <selected> | The Automatic PO checkbox is selected. |  |
| 9 | Save your data | Choose Save. | The Supplier change is saved. |  |

##### Generate Source List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating source list.

|  |
| --- |
| Note If you have more than one supplier, choose one fixed supplier in the source list. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Purchaser role. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Source Lists (F1859). | The Manage Source Lists screen displays. |  |
| 3 | Create Source List | Choose Create. | The Source List screen displays. |  |
| 4 | Enter General Information | Go to General Information area and make the following entries:Material: PK0501Plant: 3310Choose Generate. |  |  |
| 5 | Search these Sources for the Material and Plant | On the Generated Sources sceen, make the following entries:Valid From: <Current Date>Valid To: <31.12.9999>Choose Go, | The Sources are displayed. |  |
| 6 | Choose Sources | Go to Sources (X) area.Choose all lines of items.Choose Replace Existing.If you have warning message, choose OK. |  |  |
| 7 | Choose a fixed Source | Go to Supplier 33305001 and make the following entries:Materials Planning: Record Relevant for MRP (1)Status: Fixed Status (Fixed) | The Supplier has been assigned to Fixed Supplier. |  |
| 8 | Save your Data | Choose Create. | The Source List is created. |  |
| 9 | Repeat Steps | Repeat previous steps for the other packaging materials PK0502, PK0504, PK0507 and PK0508. |  |  |

#### Expand Inspection Method Long Text (Optional)

Purpose

Furthermore, you can expand the long text of inspection method for detailed description.

Prerequisite

Inspection Methods GRADE_RB Defect Grade (NYBOT) and SCORE_RB Sensory of Raw Coffee Beans (SCAA) are already available in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment. |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as a Quality Planner. | The Start page appears. |  |
| 2 | Access the SAP Fiori App. | Choose Change Inspection Method (QS33). | The Change Inspection Method Version: Initial Screen appears. |  |
| 3 | Enter Initial Data. | Make the following entries:Plant: 3310Inspect. Method: GRADE_RBChoose Inspection Method. | The Change Inspection Method Version: General Data screen appears. |  |
| 4 | Expand General Data. | Open the existing entry for more details by clicking the Change long text button next to the short text field under General Information:Defect Grade (NYBOT).A sample of 300 g is analyzed to assess the defects.Go back to General Data screen. | The Change Inspection method long text: Language XX screen appears. |  |
| 5 | Save Data. | To save your data, choose Save. |  |  |
| 6 | Check next inspection method. | Repeat steps 1–3 for Inspection Method SCORE_RB. |  |  |
| 7 | Expand General Data. | Open the existing entry for more details and check, if the following long text appears:Sensory of Raw Coffee Beans (SCAA)Specialty Coffee Cupping according SCAA. |  |  |

#### Change Inspection Plan for Raw Material

Purpose

To run through this business scenario, the inspection plans for raw material RM0501 needs to be adapted regarding some master specific limits of quantitative master inspection characteristics.

Prerequisite

Master Inspection Characteristics and inspection plan are already available in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Planner. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Open Change Inspection Plan (QP02). | Change Inspection Plan (Initial Screen) appears. |  |
| 3 | Enter Data | In the Change Inspection Plan (Initial screen), make the following entries:Material: RM0501Plant: 3310Key Date: <today>Choose Continue. | The Change Inspection Plan: Operation Overview view appears. |  |
| 4 | Select Entry Instruction | In the Inspection Plan Change: Task List Overview screen, select the row with Raw Coffee Beans Arabica and then choose Operations. | Only needed, if more than one inspection plan is assigned to the plan group. |  |
| 5 | Select Inspection Characteristic | Mark the operation line 0010 Physical Inspection and choose Inspection Characteristics.Select Master Inspection Characteristic YQM00006 Relative Humidity and choose Control Indicators. | Master Inspection Characteristic is selected in the inspection plan. |  |
| 6 | Change Control Indicator for Inspection Characteristic | In the Edit Characteristic Control Indicators view, change the following options: flagLower Specif. Limit and Upper Specif. LimitChoose Continue without further changes.Choose Continue to exit edit.Replace Lower and Upper Limit with: 11-12% | The control indicators for MIC are changed. |  |
| 7 | Save the Changes | Choose Save. |  |  |

#### Create Quality Info Record in Procurement (Optional)

Purpose

If you want to perform source inspection before goods receipt as an additional procurement process step, the quality Info Record in Procurement must be maintained for the relevant material - supplier - plant combination.

This step is only relevant for source inspection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Quality Info Record - Procurement (QI01). | The Create Q-Info Record view displays. |  |
| 3 | Enter General Data | Make the following entries:Material: RM0501Supplier: 33300002Plant: 3310Choose Continue. |  |  |
| 4 | Enter Release Data | In the Release section, enter the following data:Release Until: 31.12.9999 |  |  |
| 5 | Enter Inspection Control Data | In the Inspection Control section, enter the following data:Source Inspection: 0102Lead Time (In Days) Source: 0Source Insp. – No GR: No (Uncheck tickbox) | There are different constellations, which can be used for performing a source inspection. In this example, both a source inspection and a goods receipt inspection shall be done.Note Please confirm upcoming warning message. |  |
| 6 | Save Your Data | Choose Save. | Your data is saved. |  |

#### Create Batch (Optional)

Purpose

If you want to perform source inspection before goods receipt, a SAP batch should be created before, containing the object which is to be inspected, e.g. supplier batch.

This step is only relevant for source inspection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Batch (MSC1N). | The Create Batch view displays. |  |
| 3 | Enter General Data | Make the following entries:Material: RM0501Batch: <no entry>Plant: 3310Choose Continue. | Note Please confirm message Caution! Internal number assignment for materials handled in batches. |  |
| 4 | Enter Basic Data | In the Basic Data 1 section, scroll down to Trading Data and enter a supplier batchSupplier Batch: e.g. 1234 |  |  |
| 5 | Save Your Data | Choose Save. | Your data is saved.Note down the batch: ________________ |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Output |
| --- | --- | --- | --- |
| Procurement of Stock Material with QM - Raw Material |  |  |  |
| Create Purchase Requisition |  |  |  |
| Option 1: Create Purchase Requisition via MRP Run |  |  |  |
| [Option 1: Create Planned Independent Requirements](#unique_23) [page ] 33 | Production Planner | Maintain PIRs (F3445) | Planned Independent Requirements are created. |
| [Option 2: Create Planned Independent Requirements by Upload File](#unique_24) [page ] 35 | Production Planner | Maintain PIRs (F3445) | Planned Independent Requirements are created. |
| [Material Requirements Planning at Plant Level](#unique_25) [page ] 37 | Production Planner | Schedule MRP Runs (F1339) | MRP Run for the required materials is completed. |
| [Create Purchase Requisition - Option 2: Create Purchase Requisition manually](#unique_26) | Purchaser | Manage Purchase Requisitions - Professional (F2229) | Purchase requisitions are created manually. |
| [Create Purchase Order - Option 1: Convert Purchase Requisitions to Purchase Orders](#unique_27) | Purchaser | Process Purchase Requisitions (F1048A) | A purchase order is created. |
| [Create Purchase Order - Option 2: Create Purchase Order manually](#unique_28) | Purchaser | Manage Purchase Orders (F0842A) | A purchase order is created. |
| [Preview Purchase Order (Optional)](#unique_29) | Purchaser | Manage Purchase Orders (F0842A) | The preview of an existing purchase order is done. |
| [Change Purchase Order (Optional)](#unique_30) | Purchaser | Manage Purchase Orders (F0842A) | An existing purchase order is changed. |
| [Monitor Purchase Order Items (Optional)](#unique_31) | Purchaser | Monitor Purchase Order Items (F2358) | The purchase order items are monitored. |
| [Execute Mass Changes to Purchase Orders (Optional)](#unique_32) | Purchaser | Mass Changes to Purchase Orders (F2593) | Changes to multiple selected Purchase Orders in bulk are done. |
| Source Inspection Process (Optional) |  |  |  |
| [Review Quality Settings in Material Master (Optional)](#unique_33) | Master Data Specialist - Product Data | Display Material (MM03) | The material master is displayed. |
| [Review Quality Info Record (Optional)](#unique_34) | Quality Planner | Manage Quality Info Records (F2256A) | The quality info record is displayed. |
| [Display Inspection Plan for Inspection Characteristics (Optional)](#unique_35) | Quality Planner | Display Inspection Plan (QP03) | The data of inspection plan for the material is displayed. |
| Quality Inspection (Inspection before Goods Receipt) |  |  |  |
| [Create Inspection Lot](#unique_36) | Quality Engineer | Source Inspections - Worklist (QI07) | Inspection Lot is created. |
| [Display Quality Technician Overview (Optional)](#unique_37) | Quality Technician | Quality Technician Overview (F2361) | List of open inspection results is displayed. |
| [Change Inspection Lot and Assign Batch](#unique_38) | Quality Technician | Manage Inspection Lots (F2343) | The Quality Technician opens the created source inspection lot and assigns relevant batch with supplier batch information. |
| [Record Inspection Results](#unique_39) | Quality Technician | Record Inspection Results (F1685A) | Inspection results are recorded. |
| [Display Quality Engineer Overview (Optional)](#unique_40) | Quality Engineer | Quality Engineer Overview (F2360) | The open inspection lots are displayed. The Quality Engineer can select the next inspection lot he or she wants to record the usage decision for. |
| [Make Usage Decision](#unique_41) | Quality Engineer | Manage Usage Decisions (F2345) | Usage decision is posted. |
| [Post Goods Receipt](#unique_42) | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | The goods receipt to a purchase order is posted. |
| [Preview Goods Receipt Slip and Label (Optional)](#unique_43) | Warehouse Clerk | Material Documents Overview (F1077) | The material document is reviewed. |
| [Check Goods Receipt Details (Optional)](#unique_44) | Warehouse Clerk | Material Documents Overview (F1077) | The goods receipt fact sheet is displayed. |
| Quality Inspection (Goods Receipt Inspection) |  |  |  |
| [Display Material Stock Before Quality Inspection (Optional)](#unique_45) | Inventory Manager | Stock - Single Material (F1076) | Material stock is displayed. |
| [Display Inspection Plan for Inspection Characteristics (Optional)](#unique_46) | Quality Technician | Display Inspection Plan (QP03) | The data of inspection plan for the material is displayed. |
| [Display Quality Technician Overview (Optional)](#unique_47) | Quality Technician | Quality Technician Overview (F2361) | List of open inspection results is displayed. |
| [Display Open Inspection Lots (Optional)](#unique_48) | Quality Technician | Manage Inspection Lots (F2343) | The open inspection lots are displayed. The Quality Technician can select the next inspection lot for which he or she wants to record inspection results. |
| [Record Inspection Results](#unique_49) | Quality Technician | Record Inspection Results (F1685A) | Inspection results are recorded. |
| [Display Quality Engineer Overview (Optional)](#unique_50) | Quality Engineer | Quality Engineer Overview (F2360) | The open inspection lots are displayed. The Quality Engineer can select the next inspection lot he or she wants to record the usage decision for. |
| [Make Usage Decision](#unique_51) | Quality Engineer | Manage Usage Decisions (F2345) | Usage decision is posted. |
| [Display Material Stock after Quality Inspection (Optional)](#unique_52) | Warehouse Clerk | Stock - Single Material (F1076) | Material stock is displayed. Depending on the usage decision, the stock quantity is shown in the blocked stock, in unrestricted use stock or in another storage location. |
| [Display Inspection Results History (Optional)](#unique_53) | Quality Engineer | Display Results History (F2428) | The inspection results history is reviewed. |
| Procurement of Stock Material without QM – Packaging |  |  |  |
| [Create Purchase Requisition - Option 1: Create Purchase Requisition via MRP run](#unique_54) | Production Planner | various | Purchase requisitions are created by MRP run. |
| [Create Purchase Requisition - Option 2: Create Purchase Requisition manually](#unique_55) | Purchaser | Manage Purchase Requisitions - Professional (F2229) | Purchase requisitions are created manually. |
| [Approve Purchase Requisition](#unique_56) | Manager - Procurement | My Inbox - All Items (F5331) | Purchase Requisition is approved. |
| [Automatic Conversion of Purchase Requisition to Purchase Order](#unique_57) | Purchaser | Schedule Purchasing Jobs - Advanced (F1702) | Purchase orders are released automatically via job. |
| [Approve Purchase Order](#unique_58) | Purchasing Manager | My Inbox - All Items (F5331) | A purchase order is released. |
| [Post Goods Receipt](#unique_59) | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | The receipt of goods with reference to an existing purchase order is posted. |
| Evaluations |  |  |  |
| [Batch Information Cockpit – Top Down and Bottom-Up-Analysis](#unique_60) | Quality Technician | Batch Information Cockpit (BMBC) | Batch usage is reviewed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Procurement of Stock Material with QM – Raw Material

#### Create Purchase Requisition

##### Option 1: Create Purchase Requisition via MRP Run

###### Option 1: Create Planned Independent Requirements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create Planned Independent Requirements (PIRs). PIRs are used to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split according to dates. In Option 1 these PIRs will be loaded by manually.

|  |
| --- |
| Note Instead of creating a single requirement, sometimes one or more planned independent requirements can be maintained and included in a requirement plan for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries and choose Go:Plant: 3310Period Indicator: Weekly(W)Version Active: Select all optionsMaterial: FG0502 | The searched material item displays. If the material filter is not directly available choose Adapt Filters, select the Material Filter, enter the desired material and choose OK.Note If no PIRs for FG0502 have been maintained in the system before, the selection is empty in the app. In that case please leave this app and access the app Create PIRs (MD61), make the following entries on the Create Planned Independent Requirements: Initial Screen and choose Continue:Plant: 3310Period Indicator: Weekly (W)Version: 00Material: FG0502Choose Save and restart with step 1. |  |
| 5 | Edit PIRs. | Select the material item and choose Edit in the upper right corner of the screen.On the Edit PIRs screen, enter quantities per week, for example:Week 1 (current week + 1 week): 40 PCWeek 2 (current week + 2 weeks): 80 PCWeek 3 (current week + 3 weeks): 80 PCWeek 4 (current week + 4 weeks): 100 PCWeek 5 (current week + 5 weeks): 80 PCWeek 6 (current week + 6 weeks): 80 PCVersion is Active: YES | Note If already stock for FG0502 is available, increase the quantity for PIR of current week + 1 for the stock already available. As an alternative, remove the stock to get planned orders in next step. |  |
| 6 | Save PIR's Draft | Choose Save in the bottom right corner of the screen. | The PIRs draft is saved. |  |

###### Option 2: Create Planned Independent Requirements by Upload File

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use planned independent requirements to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split over time according to dates. In Option 2, these PIRs will be loaded by Upload File.

|  |
| --- |
| Note Instead of creating a single requirement, sometimes a requirements plan that includes one or more planned independent requirements can be maintained for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Weekly(W)Version Active: Select all optionsMaterial: FG0502 | Note If no PIRs for FG0502 have been maintained in the system before, the selection is empty in the app. In that case please leave this app and access the app Create PIRs (MD61), make the following entries on the Create Planned Independent Requirements: Initial screen and choose Continue:Plant: 3310Period Indicator: Weekly (W)Version Active: 00Search: FG0502Choose Save and restart with step 4. |  |
| 5 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 6 | Download Template | Select the material item and choose Edit in the upper right.Choose button Download to Spreadsheet to download the template to your local work space.Then choose Back without saving. |  |  |
| 7 | Edit PIRs. | Open the Spreadsheet in an adequate program and enter quantities per period, for example:In the upcoming several weeks, enter following values for PIR:Week 1 (current week + 2 weeks): 40 PCWeek 2 (current week + 3 weeks): 80 PCWeek 3 (current week + 4 weeks): 80 PCWeek 4 (current week + 5 weeks): 100 PCWeek 5 (current week + 6 weeks): 80 PCWeek 6 (current week + 7 weeks): 80 PCVersion is Active: YESSave your PIRs in the spreadsheet. | Note We recommend to check the stock for finished material before entering the PIRs (see prerequisites). If there is still stock available for FG0502, enhance the first PIR for the stock already available to generate a reproducable capacity situation (e.g. actual stock plus 250 PC). To check the stock, you can Log on to the SAP Fiori Launchpad as a Production Planner and Open the app Manage Material Coverage - New Version (F0251A). |  |
| 8 | Upload PIRs. | On the Maintain PIRs screen, choose button Upload and Edit. On the Pop Up select the file you adjusted in previous step and choose Continue. Review the uploaded data. |  |  |
| 9 | Save PIRs Draft | Choose Save at bottom right. | The PIRs are saved |  |

###### Material Requirements Planning at Plant Level

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

The Make-to-Stock finished goods are planned at plant level. There is now a requirement for in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirements Planning (MRP)Job Name: MRP for FG0502Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: <select>Recurrence Pattern: Single RunChoose OK.Choose Step 3.For 3. Parameters section:Plant: 3310Material: FG0502Changed BOM Components: <select>Stock Transfer Materials: <select>Scheduling: 2Planning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG0502 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

##### Option 2: Create Purchase Requisition manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Purchase Requisition can be created via MRP run (see Option 1) or they can be created manually (Option 2).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment. |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Purchase Requisitions - Professional (F2229). | The Manage Purchase Requisitions – Professional screen displays. |  |
| 3 | Create New Purchase Requisition | Choose Create. | The Purchase Requisition screen displays. |  |
| 4 | Enter Document Type | From the Document Type drop-down, select Purchase Requisition (NB). |  |  |
| 5 | Add Item | In the Items section, choose Create then choose Material. | The Purchase Requisition Item screen appears. |  |
| 6 | Enter Detail Data | Enter the following values in General Information section:Item Category: StandardMaterial: RM0501Plant: 3310Enter the following values in Quantity and Date section:Quantity: 10Delivery Date: default valueRequisition Date: default valueRelease Date: default valueEnter the following values in Contact Information section:Requirement Tracking Number: For example, TestTrackPurchasing Organization: 3310Purchasing Group: 002Choose Apply and you will automatically go back to the Purchase Requisition screen. |  |  |
| 7 | Create your Entries | Choose Create. | The purchase requisition is created.Note down the purchase requisition number ___________. |  |

Result

The Purchase Requisition is created.

#### Create Purchase Order

##### Option 1: Convert Purchase Requisitions to Purchase Orders

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
| 2 | Access App | Open Process Purchase Requisitions (F1048A).Note If you want to use the Save Draft feature in this app, you have to use a personalized user. | A list of Requisitions is displayed. |  |
| 3 | Search for Purchase Requisition | Select material RM0501 and plant 3310. Choose Go.Note If the field material is not displayed by default, choose Adapt Filters and select the field Material ID. Choose OK. | The Purchase Requisition is displayed. |  |
| 4 | Select Purchase Requisition | Select the Purchase Requisition you created in previous step or select one created by MRP run earlier. Then click on Show More per Row. | The Purchase Requisition has been selected for source assignment. |  |
| 5 | Assign Source to Purchase Requisition | If the Purchase Requisition has been assigned the source, then you don't need to assign source again for this step. If the Purchase Requisition hasn't been assigned the source, choose Assign Source of Supply, and select the source from a category present in the Assign Source of Supply window. | The assignment of one source to the requisition is done.Note If the purchase requisition runs into an approval process, please execute the chapter [Approve Purchase Requisition](#unique_56) [page ] 81 and then continue. |  |
| 6 | Prepare the Purchase Order | Select the purchase Requisition where the assigned supplier is displayed and choose Create Purchase Order. | The Manage Purchase Requisitions screen is displayed. |  |
| 7 | Create the Purchase Order | In the New Purchase Order screen, make the following entries:Purchase Doc Type: Standard PO.Choose Order. | The purchase order is created.Note down the purchase order number ___________. |  |
| 8 | Back to Manage Purchase Requisition | Once the order is saved, the Message toast Purchase order has been created is displayed. Click on Back button. | The Processing Status of Purchase Requisition has been changed to PO created. |  |

##### Option 2: Create Purchase Order Manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a purchase order for stock material directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen is displayed. |  |
| 3 | Start Purchase Order Creation | Without making any selection, choose Create. | The Purchase Order screen is displayed. |  |
| 4 | Enter Purchase Order Data | Enter all of the necessary data.On the General Information tab, make the following entries:Purchasing Doc. Type: Standard PO (NB)Supplier: 33300002Company Code: 3310Purchasing Organization: 3310Purchasing Group: 002Currency: AEDOn the Delivery and Invoice tab, make the following entries and choose Enter:Payment Terms: 0003Go to Supplier Contact Data tab, the Supplier Address, Telephone, Fax, Contact Person are shown.On the Notes tab, choose > or < to search for Header Text. On the Header text column, enter the free text: xxx for testing.On the Items tab, from the Purchase Order Items screen, choose Create and make the following entries:Material: RM0501Plant: 3310Order Quantity: <quantity>Net Order Price: <price>Navigate to the selected item by clicking on the Chevron (>) or by directly clicking on the item line.On the General Information tab, make the following entry:Storage Location: 331CGo to the Delivery Address tab and then navigate to the Address field. Click on the F4 value help to select the Address Number, and then choose Enter.Note This step is optional. If there is no appropriate Address Number in the system for usage, please skip this step.From the Purchase Order Item section, choose Process Flow tab.The following entries display:Goods Receipt: yesInvoice Receipt: <selected>Verify Goods-Receipt-Based Invoice Verification is selected.On the tab Tax, check the following entries:Tax Code: <Default Value>Tax Date: <Default Value>On the Schedule Lines tab, make the following entry:Delivery date: <a date in the future>From the Purchase Order Item section, choose Attachments tab.Select Doc. Type to Upload: For External UseChoose Upload to upload an attachment.Choose Apply to go back to the Purchaser Order screen.Note If you want your purchase order to be assigned to an approver, choose a quantity and total net amount of purchase order higher than 500AED (for Purchase Groups = 002) | The Purchase Order screen is displayed. |  |
| 5 | Generate Output Preview (Optional) | Click the Output Preview button on the header of the purchase order and select the output option as required.Note The Output Preview button is only avaliable when your purchase order is in status Draft, In Approval, Not Yet Sent, or Output Error. | An output preview in PDF format is generated. |  |
| 6 | Verify Purchase Order for Completeness and Save Purchase Order | Choose Order to save the Purchase Order. | A new Purchase Order is created if no error is displayed in the dialog box.Note down the purchase order number________ and its Delivery Date________. |  |
| 7 | Check the Purchase Order | Open the created purchase order in display mode and check if the values are displayed as text (code). | The relevant values are displayed as text and code. |  |
| 8 | Check the 6 Column Facet in the Tab | Click on the tab (General Information, Delivery and Invoice, Supplier Contact Data). | The tab (General Information,Delivery and Invoice, Supplier Contact Data) will be having the 6 column facet. |  |

|  |
| --- |
| Note If you do not know who should approve the purchase orders you created, then you can use App Manage Purchase Orders to display the created purchase order: Go to the Approval Details tab and check the approvers listed in section Approval Details. |

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
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Purchase Orders (F0842A).Note If you want to use the Save Draft feature in this app, you have to use a personalized user. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Select Purchase Order | Enter the Purchase Order number in the Purchase Order search box, and choose Go. Select the row for the Purchase Order you want to preview and use the little arrow on the right side to check the PO detail. | The Purchase Order screen is displayed. |  |
| 4 | Preview the Purchase Order | If you have selected a purchase order in the purchase order overview list without an 'Advanced' Purchase Order indicator, then continue.Go to the Output Management tab. In the Output Management section, choose Show More per Row and then click on the PDF icon at Display.If you have selected a purchase order in the purchase order overview list with 'Advanced' Purchase Order indicator, which means the the purchase order was created by the app Create Purchase Order - Advanced (ME21N), then you will be forwarded to the ME23N. There is no print preview available.Note When the Relevant and Merge are both selected for the document type SL1 and channel print in SSCUI: 103542 (Define Output Settings for Document Type), you upload the attachments of SL1 document type in Attachments Tab at the item level in App: Manage Purchase Orders, then the output should contain the Attachments as Document along with PO output.At the Output line item, the number of attachments for the Line item should match the number of attachments we attached. | The Purchase Order is opened in PDF format. |  |

#### Change Purchase Order (Optional)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Purchase Orders (F0842A).Note If you want to use the Save Draft feature in this app, you have to use a personalized user. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Select Purchase Order | Enter the Purchase Order number in the Purchase Order search box, and choose Go. Select the row for the Purchase Order you want to change and use the little arrow on the right side to enter the PO detail, then choose Edit, if you have selected a purchase order in the purchase order overview list without an 'Advanced' Purchase Order indicator.If you have selected a purchase order in the purchase order overview list with 'Advanced' Purchase Order indicator, which means the the purchase order was created by the app Create Purchase Order - Advanced (ME21N), then change in the change mode by pressing the button Display/Change. | The Purchase Order screen is shown.The Purchase order is opened in change mode. |  |
| 4 | Change Purchase Order | Change certain field values of the Purchase Order. | The Purchase Order values are changed. |  |
| 5 | Check Purchase Order for completeness | Choose Order, if you have selected a purchase order in the purchase order overview list without 'Advanced' Purchase Order indicator. If you have selected a purchase order in the purchase order overview list with 'Advanced' Purchase Order indicator, then choose Save to save the purchase order. | The Purchase Order is complete. |  |
| 6 | Messages (Optional) | Choose Messages (if possible). | If a message is displayed, you must correct the Purchase Order. If no message is displayed, the Purchase Order is complete. |  |
| 7 | Save Purchase Order | Choose Order to save the Purchase Order, if you have selected a purchase order in the purchase order overview list without 'Advanced' Purchase Order indicator. If you have selected a purchase order in the purchase order overview list with 'Advanced' Purchase Order indicator, then choose Save to save the purchase order. | The Purchase Order has been saved. The system displays a success message Purchase order has been saved. |  |

#### Monitor Purchase Order Items (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can monitor each item in purchase orders, but by default only overdue items would be listed in the app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Monitor Purchase Order Items (F2358). | The Monitor Purchase Order Items screen is displayed. |  |
| 3 | Search for Purchase Orders | The basic filters are displayed.Purchase Order, Display Currency, Material Group, Material, Supplier, Plant, and so on.Make the above entries accordingly, then choose Go. | The search results show the details with the respective filter criteria.You can choose Adapt Filters to select filters. |  |
| 4 | Display Purchase Order | Choose the individual line item of the Purchase Order for which you want to display the PO details. | The Purchase Order Item screen is shown. |  |
| 5 | Verify data | Verify the data displayed on the object page. | The data should correspond to the Purchase Order. |  |

#### Execute Mass Changes to Purchase Orders (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can apply changes to multiple selected Purchase Orders in bulk.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Mass Changes to Purchase Orders (F2593) app. | The Mass Changes to Purchase Orders screen is displayed. |  |
| 3 | Search for Purchase Orders Items | Set values to some filters to search Purchase Orders. For example,Material GroupPurchasing OrganizationPurchasing GroupPlantThen choose GO. | The search results show the details with the respective filter criteria. |  |
| 4 | Select Purchase Order | Select several POs by clicking the checkbox beside the purchase order number. | Purchase Order has been selected. |  |
| 5 | Choose Mass Edit | After selecting an individual purchase order, choose Mass Edit. | A dialog box will open displaying fields for 2 categories – Header fields, Item fields for which values can be changed. |  |
| 6 | Apply Mass Changes | Set new values in the given desired fields.For example: Terms of Payment: Replace Field Value: 0002.Choose Apply Mass Changes. Choose Apply to confirm the Apply Mass Changes screen. Choose Close to close the Success screen. | New values will be set to desired fields for selected Purchase Orders / Items. |  |
| 7 | Check Application Jobs | Choose Monitor Mass Changes.On the Monitor Mass Changes screen, enter the Created At with Today and remove Created By filter as blank. Choose Go and then choose Mass Change Jobs tab. Navigate to the selected Mass Change Job by clicking on the Chevron (>) or by directly clicking on the Mass Change Job line. | It will navigate to Monitor Mass Changes screen.Verify if the job is successful for the selected Purchase Orders. |  |

#### Source Inspection Process (Optional)

Purpose

If you want to perform source inspection before goods receipt as an additional procurement process step, you can run through the following steps. This step is only relevant for source inspection.

With this setup, it is possible to inspect the raw material before goods receipt to decide whether the material shall be unloaded from tanker. In case of approval, the warehouse clerk posts the goods receipt to quality inspection stock creating a further inspection lot for the physical and sensory quality inspections by QM Labs and Sensory Experts. If the material is rejected, the process ends without receiving material but with sending back to the supplier.

##### Review Quality Settings in Material Master (Optional)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Display Material (MM03) app. | The Display Material (Initial Screen) displays. |  |
| 3 | Enter Material | Enter RM0501 in the field Material and choose Continue. | The Select View(s) pop-up is displayed. |  |
| 4 | Open Quality Management View | Select Quality Management view. Choose Org.Levels button and enter 3310 for Plant. Choose Continue button or choose Enter. | The Display MaterialRM0501(Raw Materials) screen is displayed. |  |
| 5 | Review Quality Management in Procurement Settings | The following settings are done:QM in Procur. Active: flaggedQM Control Key: 0000 |  |  |
| 6 | Review Inspection Setup | Choose button Insp. Setup and review the inspection types assigned to the material. | Inspection type 0102 Source Inspection is assigned additionally to goods receipt inspection with inspection type 01 (Goods Receipt Inspection for Purchase Order). |  |

##### Review Quality Info Record (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Quality info record has been set up to influence procurement functions. In this example the source inspection and goods receipt inspection shall be performed.

If a quality inspection is needed for a specific material supplier combination before goods receipt is posted, you can enable supplier source inspection by maintaining the source inspection type, lead time and indicator Source Insp. – No GR.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Planner. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Quality Info Records (F2256A) app. | The Manage Quality Info Records screen displays. |  |
| 3 | Enter Search Fields | Make the following entries and choose GoPlant: 3310Material: RM0501Supplier: 33300002Click on the quality info record. |  |  |
| 4 | Review Release Data | In the Release section, review the following data:Release Until: 31.12.9999 |  |  |
| 5 | Review Inspection Control Data | In the Inspection Control section, review the following data:Source Inspection: 0102Lead Time (In Days): 0Source Inspection Instead of GR Inspectn: No (unchecked) | Source Inspection Instead of GR Inspectn: If you do not set this indicator, the system creates one inspection lot for same purchase order item before goods receipt AND another inspection lot after goods receipt. |  |

##### Display Inspection Plan for Inspection Characteristics (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the inspection plan is related to the raw material. The inspection plan defines all inspection characteristics used in the source inspection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Inspection Plan (QP03). | The Manage Inspection Plans screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Continue.Material: RM0501Plant: 3310 |  |  |
| 4 | Select Entry Instruction | In the Inspection Plan Display: Task List Overview screen, select the row with Source Inspection Raw Coffee Beans and then choose Operations. | Only needed, if more than one inspection plan is assigned to the plan group. |  |
| 5 | Go to Inspection Characteristics Overview Screen | Select the operation 0010 and choose either Inspection Characteristics or Menu > Go To > Inspection Characteristic Overview (F7) . | The Display Inspection Plan: Characteristics Overview screen displays. |  |
| 6 | Review the Inspection Characteristics | There is one Master Inspection Characteristic which is Qualitative:Pest Control | You have now reviewed the inspection characteristics for which data has to be maintained within a later step.The sampling procedure and catalog can be reviewed in detail. |  |

##### Quality Inspection (Inspection before Goods Receipt)

###### Create Inspection Lot

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The raw material undergoes a quality inspection to ensure that it meets the predefined quality requirements.

In this step, the quality engineer creates inspection lots per worklist. Then, the quality technician records the inspection results for the required inspection characteristics. Afterwards, the quality engineer completes the inspection with a usage decision.

|  |
| --- |
| Note Usually, this inspection lot creation is done by a job. |

Prerequisite

The inspection is processed based on inspection lot. In this business process, a purchase order item for the material exists and QM in procurement is active with control key 0000 and an additional inspection type of inspection lot origin 01 (Goods Receipt). Furthermore, a quality info record is maintained with inspection type and lead time.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Source Inspections - Worklist (QI07). | The Worklist of Source Inspections screen displays.You can get an overview of the purchase order items where a source inspection is planned dependent from their delivery time. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Execute:Supplier: 33300002Material: RM0501Plant: 3310Delivery Date: <delivery date> (from previous steps)Opening Period: 0Inspect w/o batch: flagged | Note A list of purchase orders for materials with source inspection is displayed. The system selects all purchase order items whose delivery date lies before the delivery date entered on the selection screen.The opening period controls the traffic light display in the selected list after executing:The light is green, if the delivery date from the purchase order item minus the lead time from the quality info record lies before the current date plus the opening period.The light is red, if the above does not apply.Note Causes the system to create a (source) inspection lot, although there is no batch defined in the purchasing document. |  |
| 4 | Create Inspection Lot | Select line and choose Inspection Lot:Purch.Doc: <purchase order> (from previous steps) |  |  |
| 5 | Save Inspection Lot | Choose Save. | Line disappears from worklist because source inspection lot is created. |  |

###### Display Quality Technician Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, you can display an overview of open inspection lots via the overview page for quality technicians.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Technician Overview (F2361). | The Quality Technician Overview screen displays.You can get an overview of the inspection lots with open results recording and the inspection lots without an inspection plan. |  |

###### Change Inspection Lot and Assign Batch

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection lot is used to record the results of the source inspection in reference to the relevant purchase order.

Prerequisite

In this business process, the inspection lot is created via source inspection worklist. A batch was prepared before with assignment to the supplier batch.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Material: RM0501Inspection Lot Status: OutstandingInspection Lot Origin: Goods Receipt | Alternatively, you can search for the Purch.Doc <Purchase Order ID> (from previous step)If purchase order is not displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, select Purchasing Document and choose OK. Choose Go. |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot with column equals to the Purchasing Document: <purchase order> (from previous steps). | The Purchase Order number assigned with Inspection Lot is displayed.If the Purchase Order column does not appear, please choose the button Settings. In the View Settings dialog box, select Purchasing Document and choose OK.Note down the inspection lot ____________________ |  |
| 5 | Check Inspection Lot | Under Origin, verify the referenced Purchasing Document/Item. | The purchase order item from which the source inspection lot originates is displayed. |  |
| 6 | Choose Operations (Optional) | In Results, choose operation Inspection before Goods Receipt (10). | For checking the relevant inspection data, e.g. characteristic Pest Control |  |
| 7 | Change Inspection Lot | Exit and go back to Manage Inspection Lots list. Click the hyperlink of inspection lot and select Change Inspection Lot. | The Change Inspection Lot: Supplier Data screen displays. |  |
| 8 | Add Batch | Assign batch to inspection lot and choose Save.Batch: <batch ID> (from preliminary steps) | Inspection Lot XXXX was changed appears and the batch is assigned to the inspection lot. |  |

###### Record Inspection Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The results are recorded in the inspection lot according to the defined inspection parameters in the inspection plan.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A). | The Record Inspection Results screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Purchase Order: <Purchase Order ID> (from previous steps). | If Purchase Order isn't displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, find Procurement and choose More Filters. Select Purchase Order and choose OK. Choose Go. |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the Inspection Lot. |  |  |
| 5 | Choose Record Results | Choose Record Multiple Results on top of the list. Choose Edit. |  |  |
| 6 | Enter Inspection Result | Depending on the inspection result, select one of the following two options:Positive ResultPest Control: Code Group - Code QUAL01 OKNegative ResultPest Control: Code Group - Code QUAL01 NOK | For qualitative characteristics (Pest Control) the value help is needed to select a value.The default number of inspected objects is calculated based on the sample size reviewed in an earlier step.In case of negative inspection results, a general defect is created in the background, if auto-defect recording is planned for the inspection characteristic.If needed, you can add a remark with further details.For the inspection characteristic Pest Control, a short documentation is required if it is rejected, e.g. Beetles or Grubs. |  |
| 7 | Create Defects (Optional) | Optionally, you can add a defect code from list.Select relevant Inspection Characteristics and choose Create Defect. Select Defect Level from list, e.g. for inspection characteristic.Select Defect Code Group - Code, e.g. DEFPEST 0001 Beetles.Choose Create. | The Select Defect Code Group screen displays. |  |
| 8 | Save Inspection Lot | Choose Save. | The inspection lot is saved. QM source inspection has been performed and results recorded. |  |

###### Display Quality Engineer Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the inspection lot depending on the inspection result. As an optional entry point for making this usage decision, you can use the app Quality Engineer Overview (F2360). Furthermore, the Quality Engineer Overview (F2360)app displays inspection lots without an inspection plan (e.g. if automatic assignment of an inspection plan is not set up in the material master or if automatic assignment failed), inspection lots without usage decision, inspection lots ready for usage decision. If negative inspection results are recorded, you can check the detect details in app Manage Defects (F2649) directed from the app Quality Engineer Overview (F2360) via the cards Inspection Lots with Defects, Top Defective Materials, or Top Defects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Engineer Overview (F2360). | The Quality Engineer Overview screen displays. |  |
| 3 | In Card: Inspection Lots without Inspection Plan choose one entry (Optional) | Choose card Inspection Lots Without Inspection Plan. | To assign missing data and ensure automatic inspection plan determination for further usage. |  |
| 4 | In Card: Select Inspection Lots Without Usage Decision (Optional) | Choose card Inspection Lots Without Usage Decision. | You can process further as described in Make Usage Decision Chapter. |  |
| 5 | Select the Corresponding Inspection Lot you have created before (Optional) | In the inspection lot list, select the inspection lot. | The Manage Usage Decisions screen displays. Alternative Entry to Chapter Manage Usage Decision. |  |
| 6 | Select one of the Inspection Lot by Results Recording Status (Optional) | Select one of the Inspection Lot by Results Recording Status (Optional). | Alternative Entry to Chapter Manage Usage Decision. |  |
| 7 | Select Card Inspection Lots Ready for Usage Decision (Optional) | Choose card Inspection Lots Ready for Usage Decision. | All inspection lots with positive results get collectively an accepted usage decision (e.g. defaulted by A1) when pressing button Make Quick Usage Decision. |  |
| 8 | In Card: Inspection Lots with Defects (Optional) | (In case negative inspection results have been recorded and defects have been created) Select one of the inspection lot origins, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 9 | In card: Top Defective Materials (Optional) | (In case negative inspection results have been recorded and defects have been created) Select one of the materials inspected, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 10 | In card: Top Defects (Optional) | (In case negative inspection results have been recorded and defects have been created) Select one of the defect codes recorded, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |

###### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection results are recorded. You must decide whether to accept the raw material depending on the inspection result. If you do not want to use the Quality Engineer Overview (F2360), you can open the Manage Usage Decisions (F2345) app directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Usage Decisions (F2345). | The Manage Usage Decisions screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Purchasing Document: <purchase order> (from previous steps) | If Purchasing Document is not displayed in the Filters, choose Adapt Filters. On the dialog box Adapt Filters, find Procurement and choose More Filters. Select Purchasing Document and choose OK. Choose Go.Alternatively, you can search for the batch <Batch ID> or <Inspection Lot ID> (from previous step). |  |
| 4 | Select Corresponding Inspection Lot | In the inspection lot list, select the corresponding inspection lot. | The Inspection Lot screen displays. |  |
| 5 | Display Defects | Scroll down to the Defects area. Check the details of Defects. | Only available you when have recorded a negative result. For a pest control rejection, there will be a texture/color type defect, for a humidity rejection, there will be a tolerance defect displayed. |  |
| 6 | Choose Edit and Add Document | Choose Edit. In the Document section choose Upload, select the path and add the document. | For example to upload pictures to visualize the defect. |  |
| 7 | Enter UD code | Depending on the inspection result, select one of the following options and then confirm with Save.UD code: A1 (Accepted – unrestricted stock)A2 (Accepted-unrestricted – minor quality)A3 (Accepted-unrestricted - sample consumption)Negative ResultUD code: R1 (Rejected – blocked stock)R210 (Rejected-return supplier w/o delivery)R220 (Rejected-return supplier with delivery)Choose Yes if dialog Confirmation Prompt appear. | Note For source inspection, you can use the same UD codes as for inspection lots which are created from goods receipt posting.Because source inspection lots are not stock relevant, the follow-up action behind the codes are not relevant.Note If the material is batch-managed, you must assign a batch to the inspection lot before saving.Working with source inspection, the batch can be prepared and already assigned to the purchase order during purchase order creation or by changing the purchase order ideally when the tanker leaves the supplier side respective latest when the tanker arrives at customer side. |  |
| 8 | Save Usage Decision | Choose Save. | The usage decision is made for raw material. |  |

#### Post Goods Receipt

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Post Goods Receipt for Purchasing Document (F0843). | The Post Goods Receipt for Purchase Order screen is displayed. |  |
| 3 | Enter Purchase Order | Enter the Purchase Order ID from previous step and choose Enter. | The system displays the data for the goods receipt on the Goods Receipt screen. |  |
| 4 | Enter Delivery Note | Make the following entries and choose Enter:Delivery Note: <Delivery Note>Printing: Individual slip |  |  |
| 5 | Enter batch (Optional) | If source inspection was performed with acceptance before:Batch: <batch ID> (from previous steps) | Batch is manually determined at goods receipt by assigning the batch which was inspected before (while additional source inspection). |  |
| 6 | Select Item | From the Items section, select the goods receipt item to be posted. | You can see that the Post button is activated. |  |
| 7 | Post | Choose Post. | The system displays the message Material Document xxx posted. |  |

#### Preview Goods Receipt Slip and Label (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this step, the material document is previewed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Material Documents Overview (F1077). | The Material Documents Overview is displayed. |  |
| 3 | Search for Goods Receipts Material Document | Make the following entries and choose the Go button.Plant: 3310Material Document: <Material document> from previous step | The relevant Material Document item displays. |  |
| 4 | Select Material Document for Goods Receipt | Select the row for which you would like to see the material documents. | The Material Document screen displays. |  |
| 5 | Check Goods Receipt Details | Check the General Information, Attachments, Item, Document Flow and Process Flow. | In the General Information section, you can see the Posting Date, Document Date. |  |
| 6 | Select the Material Document Item | In the Items section, select the row of material document item that you want to preview. | The Material Document Item screen displays. |  |
| 7 | Preview the Material Document Goods Receipt Slip | In the Output Management section, choose Show More per Row, and choose Display Document icon in the item of which Output Type is GOODS_RECEIPT_PO_SLIP. | The Goods Receipt Slip is opened in PDF format.Note In case Display Document is not visible on screen, switch layout to Show More per row |  |
| 8 | Back to Launchpad | Choose the Home button to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

#### Check Goods Receipt Details (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the goods receipt fact sheet is displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Material Documents Overview (F1077) . | The Material Documents Overview screen is displayed. |  |
| 3 | Search for Goods Receipts Material Document | Make the following entries and choose Go:Plant: 3310Material Document: <Material Document> | On the Material Documents Overview screen, the relevant Material Documents / Material Document items are shown. |  |
| 4 | Select Material Document for Goods Receipt | Select the row for which you would like to see the material documents. | The list of the Material Documents is displayed.The Goods Receipts Details are shown. |  |
| 5 | Check Goods Receipts Details | Check the General Information, and the Material Document Items. | In the General Data section, the correct Posting Date, Document Date, and the Delivery Note are shown. |  |
| 6 | Display Document Flow | Switch to the section Process Flow. | The Process Flow shows the Purchase Order and the Material Document as a flow chart. |  |
| 7 | Back to Launchpad | Choose Home to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

### Quality Inspection (Goods Receipt Inspection)

#### Display Material Stock Before Quality Inspection (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, a review of the raw material stock is done. Due to quality inspection, the material isn't available for other processing.

Prerequisite

The goods receipt from purchase order was posted for the raw material directly to quality inspection stock. This is caused by material master settings for inspection type 01 Goods Receipt Inspection for Purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori Launchpad as a Inventory Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material screen displays. |  |
| 3 | Enter Material | Make the following entries and choose Enter:Material: RM0501 | Stock for the material is displayed. |  |
| 4 | Check Stock Quantity | Check the Quality Inspection Stock under the plant 3310 and storage location 331C for your batch <Batch ID>. | Stock for the material, batch, and storage location is checked. |  |

#### Display Inspection Plan for Inspection Characteristics (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you display the inspection plan that is related to the raw material. The inspection plan defines all inspection characteristics used later in the quality inspection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment. |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Inspection Plan (QP03). | The Display Inspection Plan: Initial Screen screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Continue.Material: RM0501Plant: 3310 |  |  |
| 4 | Select Entry Instruction | In the Inspection Plan Display: Task List Overview, choose Inspection Plan with Group Counter GrC 1. In Task List Overview screen, select the row with Raw Coffee Beans Arabica and then choose Operations. | Only needed, if more than one inspection plan is assigned to the plan group. |  |
| 5 | Go to Inspection Characteristics Overview Screen | Select the entry for Operation 0010 and choose Inspection Characteristics.Note If you couldn't find Inspection Characteristics in your screen, choose Menu > Inspection Characteristics. | The Display Inspection Plan: Characteristic Overview screen displays. |  |
| 6 | Review the Inspection Characteristics | There are two Master Inspection Characteristics:One is Quantitative – Relative Humidity (%).The other one is Qualitative – Defect Grade Raw Coffee Beans (NYBOT) with inspection method Defect Grade (NYBOT).For all, sample size 1 is to be inspected.Auto-defect recording is defined if characteristic Relative Humidity is rejected. | You've now reviewed the inspection characteristics for which data has to be maintained later. |  |
| 7 | Go to Inspection Characteristics Overview Screen | Select the entry for Operation 0020 and choose Inspection Characteristics.Note If you couldn't find Inspection Characteristics in your screen, choose Menu > Inspection Characteristics. | The Display Inspection Plan: Characteristic Overview screen displays. |  |
| 8 | Review the Inspection characteristics | There's one Master Inspection Characteristic:It's Qualitative – Sensory Raw Coffee Beans (SCAA) with inspection method Sensory of Raw Coffee Beans (SCAA).Sample size 1 is to be inspected. | You've now reviewed the inspection characteristic for which data has to be maintained later. |  |

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

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Technician Overview (F2361). | The Quality Technician Overview screen displays.You can get an overview of the inspection lots with open results recording and the inspection lots without an inspection plan.Choose card Inspection Lots with Open Results Recording, No Inspection Points if you want to record results for this goods receipt inspection lot. |  |

#### Display Open Inspection Lots (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection lot is used to record the results of the inspection operation. In this optional step, the references to the goods receipt and purchase order are verified as well as assigned inspection methods with long texts used for quality inspection.

Prerequisite

In this scope item, the inspection lot is created automatically upon goods receipt for the purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Plant: 3310Material: RM0501Inspection Lot Status: OutstandingInspection Lot Origin: Goods Receipt | Alternatively, you can search for the Purch.Doc <Purchase Order ID> (from previous step)If purchase order is not displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, select Purchasing Document and choose OK. Choose Go. |  |
| 4 | Select Inspection Lot | In the inspection lot list, select the inspection lot with column equals to the Purchasing Document: <purchase order> (from previous steps) | The Purchase Order number assigned with Inspection Lot is displayed.If the Purchase Order column does not appear, please choose the button Settings. In the View Settings dialog box, select Purchasing Document and choose OK.Note down the inspection lot ____________________Note down the batch number ____________________ |  |
| 5 | Check Inspection Lot by Selecting the Line | Under Origin, verify the referenced purchase order and material document. | The purchase order number and material document number from which the inspection lot originates are displayed. |  |
| 6 | Choose Operation (optional) | In Result, choose operation Physical Inspection. | Inspection Characteristics Relative Humidity and Defect Grade Raw Beans (NYBOT) can be reviewed with their specifications and calculated sample sizes. |  |
| 7 | Choose Characteristic (optional) | Click Defect Grade Raw Coffee Beans (NYBOT) in the characteristics column. | A dialog box appears with the Characteristics Details with the link to the Inspection Method. |  |
| 8 | Display Text | In General, Long Text is displayed. |  |  |
| 9 | Choose Operation (optional) | In Result, choose operation Sensory Inspection (Coffee Cupping). | Inspection Characteristic Sensory Raw Coffee Beans (SCAA) can be reviewed with their specifications and calculated sample sizes. |  |
| 10 | Choose Characteristic (optional) | Click Sensory Raw Coffee Beans (SCAA) in the characteristics column. | A dialog box appears with the Characteristics Details with the link to the Inspection Method. |  |
| 11 | Display Text | In General, Long Text is displayed. |  |  |

#### Record Inspection Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the quality technician performs the quality inspection and records the inspection result(s) by selecting the relevant work center.

The result is recorded in the inspection lot according to the defined inspection parameters in the inspection plan.

Prerequisite

The inspection is processed based on inspection lot. In this scope item, the inspection lot is automatically created upon goods receipt for purchase order.

Procedure

Record Inspection Results for one Inspection Lot

If inspection results shall be recorded for one or only a few inspection lots, execute the following process flow:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A). | The Record Inspection Results screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Purchase Order: <Purchase Order ID> (from previous step). | If purchase order isn't displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, select Purchase Order and choose OK. Choose Go.Alternatively, you can search for the batch <Batch ID> or <Inspection Lot ID> (from previous step). |  |
| 4 | Display the Corresponding Operations | Switch from Inspection Lots list to the Operations list. | Both Inspection lot operations with relevant work center are offered. |  |
| 5 | Enter Additional Filter Fields | Expand Header for additional filter, make the following entry and choose Go.Work Center: QMLABS | If Work Center is not displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, select Work Center and choose OK. Choose Go.Only Inspection lot operations and master characteristics for filtered work center will be offered for results recording. |  |
| 6 | Choose Record Results | Choose Record Multiple Results in the right bottom. |  |  |
| 7 | Enter Inspection Result | Depending on the inspection result, select one of the following two options:Positive ResultRelative Humidity : Mean Value (%): 11Defect Grade Raw Coffee Beans (NYBOT): Code Group - Code: GRADE-RB 2 (Premium Grade)Negative ResultRelative Humidity : Mean Value (%): 13 | For qualitative characteristic (Defect Grade Raw Coffee Beans (NYBOT)) the search help is needed to select a value. For the quantitative characteristic (Relative Humidity) a number can be entered directly.The default number of inspected objects is calculated based on the sample size reviewed in an earlier step. |  |
| 8 | Save Inspection Lot | Choose Save. After success message, choose Back | The inspection lot is saved. QM Inspection for work center QMLABS has been performed and results recorded. |  |
| 9 | Change Filter Fields | Expand Header for additional filter, make the following entry and choose Go.Work Center: QMSENS | If Work Center is displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, select Work Center and choose OK. Choose Go.Only Inspection lot operations and master characteristics for filtered work center will be offered for results recording. |  |
| 10 | Choose Record Results | Choose Record Multiple Results in the right bottom. |  |  |
| 11 | Enter Inspection Result | Select one entry: e.g.Sensory Raw Coffee Beans (SCAA): Code Group - Code: SENS2_RB 0020 (Excellent) | For qualitative characteristic (Sensory Raw Coffee Beans (SCAA)) the search help is needed to select a value.The default number of inspected objects is calculated based on the sample size reviewed in an earlier step. |  |
| 12 | Save Inspection Lot | Choose Save. | The inspection lot is saved. QM Inspection for work center QMSENS has been performed and results recorded. |  |

Optional: Process-Optimized Results Recording for Multiple Inspection Lots

If inspection results shall be recorded for multiple inspection lots at the same time (mass processing), execute the following process flow.

|  |
| --- |
| Caution Note that this app can only be used for quality inspections with master inspection characteristics. It is not possible to capture inspection results for inspections with plan characteristics. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results in Table Form (F3365). | The Record Inspection Results in Table Form screen displays. |  |
| 3 | Enter Filter Fields | Maintain filter values and choose Go. | A list of inspection lots is displayed. |  |
| 4 | Select Inspection Lots and Inspection Characteristics | Select the inspection lots for which inspection results shall be recorded and choose Record Multiple Results.In the pop-up window Select Characteristics for Result Recording, select the master inspection characteristics for which inspection results shall be recorded and choose button OK. | The Record Inspection Results in Table Form screen displays.Note The system creates one table line item per inspection lot operation. Each master inspection characteristic is displayed in a separate column. The valuation of the inspection characteristic is displayed in a separate adjacent column. If a master inspection characteristic is assigned to another inspection operation, the respective table field is grayed out. |  |
| 5 | Show Inspection Details (Optional) | Click one inspection characteristic in the table and choose Show Details. | The side panel opens and detailed inspection data are displayed (e.g. inspection specifications, master inspection characteristic, inspection method, test equipment, and inspection remarks). |  |
| 6 | Show Work Center (Optional) | Choose Settings button in the upper right corner of the table. In the Define Column Properties popup, select Work Center and choose OK. | An additional Work Center column is displayed. |  |
| 7 | Enter Inspection Results | Enter inspection results. See above for example data. | For qualitative results, a corresponding value help is provided. Quantitative inspection results can be entered directly.Note Depending on the defined valuation mode (check inspection method details), the valuation is either done automatically by the system or must be done manually by the user.If an inspection result requires an inspection remark (check master inspection characteristic settings), it is possible to navigate to the next inspection result. Open Details side panel and maintain the inspection remark in section Remarks. |  |
| 8 | Save Inspection Data | Choose Save. | Inspection results are saved and a success message is displayed. |  |

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

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Engineer Overview (F2360). | The Quality Engineer Overview (F2360) screen displays. |  |
| 3 | In Card: Inspection Lots without Inspection Plan choose one entry (Optional) |  | To assign missing data and ensure automatic inspection plan determination for further usage. |  |
| 4 | In Card: Select Inspection Lots Without Usage Decision (Optional) | Choose card Inspection Lots Without Usage Decision | You can process further as described in the chapter [Make Usage Decision](#unique_51) [page ] 74. |  |
| 5 | Select the Corresponding Inspection Lot you have created before (Optional) | In the inspection lot list, select the inspection lot. | The Manage Usage Decisions screen displays. Alternative Entry to chapter [Make Usage Decision](#unique_51) [page ] 74. |  |
| 6 | Select one of the Inspection Lot by Results Recording Status (Optional) | Select one of the Inspection Lot by Results Recording Status (Optional) | Alternative Entry to chapter [Make Usage Decision](#unique_51) [page ] 74. |  |
| 7 | Select Card Inspection Lots Ready for Usage Decision (Optional) |  | All inspection lots with positive results get collectively an accepted usage decision (e.g. defaulted by A1) when pressing button Make Quick Usage Decision. |  |
| 8 | In Card: Inspection Lots with Defects (Optional) | (In case negative inspection results have been recorded and auto-defect recording has been defined). Select one of the inspection lot origins, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 9 | In Card: Top Defective Materials (Optional) | (In case failed inspection results have been recorded and auto-defect recording has been defined). Select one of the materials inspected, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 10 | In Card: Top Defects (Optional) | (In case negative inspection results have been recorded and auto-defect recording has been defined). Select one of the defect codes recorded, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |

#### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the goods receipt depending on the inspection result. If you don't want to use the Quality Engineer Overview (F2360), you can open the Manage Usage Decisions (F2345) app directly.

|  |
| --- |
| Note In case of positive recorded results (in previous step), immediate auto-usage decision with "Accepted-unrestricted stock (A1)" is performed in background if respective plant specific settings are prepared in customizing. In this case, you can skip this chapter. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Usage Decisions (F2345). | The Manage Usage Decisions screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Purchasing Document: <Purchase Order> (from previous steps). | If Purchase Document isn't displayed in the filters, choose Adapt Filters. On the dialog box Adapt Filters, select Purchase Document and choose OK. Choose Go.Alternatively, you can search for the batch <Batch ID> or <Inspection Lot ID> (from previous step). |  |
| 4 | Select Corresponding Inspection Lot | In the inspection lot list, select the corresponding inspection lot. | The Inspection Lot screen displays. |  |
| 5 | Display Defects | Scroll down to the Defects area. Check the details of Defects. | Only available when you have recorded a negative result with defect. For a pest control rejection, a pest infestation type defect will be displayed. |  |
| 6 | Choose Edit and Add Document (Optional) | Choose Edit. In the Document section choose Upload, select the path and add the document. | For example, to upload pictures to visualize the defect. |  |
| 7 | Enter UD code | Go to Usage Decision tab.Depending on the inspection result, select one of the following two options and then confirm with Save.UD code: A1 (Accepted – unrestricted stock)A2 (Accepted-unrestricted – minor quality)A3 (Accepted-unrestricted-sample consumption)Negative ResultUD code: R1 (Rejected – blocked stock)R210 (Rejected-return supplier w/o delivery)R220 (Rejected-return supplier with delivery)Choose Yes if dialog Confirmation Prompt appears. | Note For source inspection, you can use the same UD codes as for inspection lots which are created from goods receipt posting.Because source inspection lots are not stock relevant, the follow-up-action behind the codes are not relevant.Note If the material is batch managed, you must assign a batch to the inspection lot before saving.One way is described in this test script by preparing a batch for assignment.Another way of working with source inspection, the batch can be prepared due to close alignments with supplier. In this case, the batch can be assigned to the purchase order during purchase order creation or by changing the purchase order ideally when the tanker leaves the supplier side respective latest when the tanker arrives at customer side. |  |
| 8 | Save Usage Decision | Choose Save. | The usage decision is made with regard to the raw material. |  |

#### Display Material Stock after Quality Inspection (Optional)

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

- Positive Result (A1, A2): quantity is increased in Unrestricted Use Stock and quantity is reduced in Quality Inspection Stock
- Positive Result for ‘sample consumption’ (A3): partial quantity is increased in Unrestricted Stock, inspected quantity is consumed and therefore not in stock anymore, and full quantity is reduced in Quality Inspection Stock
- Negative Result ‘Blocked Stock’ (R1) : quantity is increased in Blocked Stock and quantity is reduced in Quality Inspection Stock
- Negative Result ‘Return to Supplier w/o Delivery’ (R210): quantity is reduced in Quality Inspection Stock
- Negative Result ‘Return to Supplier with Delivery’ (R220): quantity is increased in return storage location Blocked Stock and quantity is reduced in Quality Inspection Stock

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock – Single Material screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and press Enter.Material:RM0501 |  |  |
| 4 | Check Stock Quantity | Check the changed quantities of the Quality Inspection Stock, Unrestricted Use Stock (in case of positive usage decision) or Blocked storage location 331C/331R (in case of negative usage decision). | The stock quantities for raw material RM0501 and <Batch ID> are updated based on the quality inspection and respective usage decision of the previous steps. |  |

#### Display Inspection Results History (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This optional process step shows you how to display inspection results history.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Results History (F2428). |  |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Aggregation Level: Master Inspection Characteristic | A list of inspection characteristics displays. |  |
| 4 | Select Inspection Characteristics | Select an Inspection Characteristics, for example, YQM00006 Relative Humidity. | Some information is shown about the selected characteristics for process control, for example:A diagram displays the development of the recorded results for this characteristic with lower and upper limit.Statistical Values for Control Chart and Process Capability. E.g: Mean Value. |  |
| 5 | Change Filter Fields | Make the following entries and choose Go.Aggregation Level: Inspection Plan Characteristic | A list of inspection characteristics displays.If master characteristics are used in different plans, you can select them (plan specific) by using the filter Inspection Plan Characteristic. |  |

### Procurement of Stock Material without QM – Packaging

In this section, the procurement process for a packaging material without Quality Management is described. This procurement process is using automatic purchase order creation from purchase requisition.

When you perform the following steps Automatic Purchase Order Creation from Purchase Requisition, you have to run Master Data update from the Preliminary Steps: “[Master Data Update for Automatic Purchase Order Creation from Purchase Requisition](#unique_14)”.

|  |
| --- |
| Note This section describes the purchasing of the packaging material PK0502. Repeat the section “Procurement of Stock Material without QM – Packaging” for the packaging materials PK0501, PK0504, PK0507 and PK0508 if you need stock for them as well. |

#### Create Purchase Requisiton

##### Option 1: Create Purchase Requisition via MRP run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step you create purchase requisitions by MRP run. This process step can be executed when scope item 5HK (Quality Management in Discrete Manufacturing – Consumer Products) or 5OI (Production Capacity Evaluation and Leveling – Consumer Products) is activated in the system.

The components which need to be purchased in this scope item are components for the production of the finished materials FG0502, FG0511 or FG0512. The creation of PIRs for material FG0502 will result in requirements for the components which need to be purchased.

Prerequisite

The scope item 5HK (Quality Management in Discrete Manufacturing – Consumer Products) or 5OI (Production Capacity Evaluation and Leveling – Consumer Products) must be activated in the system.

Procedure

If you use 5HK scope item, follow the steps described in the following sections:

Chapter “Anonymous Forecast and MRP”

- Create Planned Independent Requirements
- Material Requirements Planning at Plant Level
- Evaluate Stock / Requirements Situation

If you use 5OI scope item, follow the steps described in the following sections:

- Create Planned Independent Requirements
- Material Requirements Planning at Plant Level

|  |
| --- |
| Note If no purchase requisitions are created for the materials, either the available stock of the raw and packaging materials is sufficient for the planned production volume or a production version is automatically selected during MRP run which does not require the respective material. In that case use “[Option 2: Create Purchase Requsition manually](#unique_55)” to be able to run through the test case. |

##### Option 2: Create Purchase Requisition manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Purchase Requisition can be created manually.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Manage Purchase Requisitions - Professional (F2229). | The Manage Purchase Requisitions – Professional screen displays. |  |
| 3 | Create Purchase Requisition | Choose Create. | The Purchase Requisition screen displays. |  |
| 4 | Enter Document Type | Enter Document Type: Pur. Requisition (NB) and select Automatic Source Determination. |  |  |
| 5 | Add Item | In the Items section, choose Create, then choose Material to add new items to Purchase Requisitions. | The Purchase Requisition Item screen appears. |  |
| 6 | Enter detail data | Enter the following values in General Information section:Item Category: StandardMaterial: PK0502Plant: 3310Enter the following values in Quantity and Date section:Quantity: 10.000,00Delivery Date: <default value>Requisition Date: <default value>Release Date: <default value>Enter the following values in Contact Information section:Purchasing Organization: 3310, and choose Enter.Purchasing Group: 002, and choose Enter.Go to Source of Supply area and make sure one source has been assigned. If no Source of Supply is assigned, choose button Assign Source of Supply.Choose Apply. |  |  |
| 7 | Save your entries | Choose Create and confirm the popup message. | The Purchase Requisition is created. |  |
| 8 | Repeat Steps | Repeat steps for PK0501, PK0507, PK0508 and PK0504. |  |  |

Result

The Purchase Requisition is created.

#### Approve Purchase Requisition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you release a purchase requisition. If the total amount of PR > 500 AED and purchase group is 002, then the purchase requisitions should be approved. To decide which PRs need approval, please refer to [Configure Flexible Workflow for Purchase Order](#unique_12) [page ] 17 in Preliminary step.

Prerequisite

A purchase requisition must exist for release.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Manager - Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F5331). | A list of all items in the inbox is displayed. |  |
| 3 | Search for Purchase Requisition Status | Make the following entry and choose Enter:Search: <Purchase Requisition number> | The Purchase Requisition is displayed. |  |
| 4 | Approve Purchase Requisition Item | Select the Purchase Requisition Item on the left side of the screen and choose Approve at the bottom right. | The Submit Decision screen is displayed. |  |
| 5 | Enter Approval Reason | Enter the approval reason if necessary, and then choose Submit. | The Purchase Requisition Item is approved. |  |

|  |
| --- |
| Note If an attachment is uploaded during purchase requisition creation, in My Inbox App, the attachment can be found under Attachments tab of the purchase requisition item. |

#### Automatic Conversion of Purchase Requisition to Purchase Order

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Schedule Purchasing Jobs - Advanced (F1702). | The Application Jobs screen displays |  |
| 3 | Create Job | Choose Create. | The New Job screen displays. |  |
| 4 | Define a Job | On the New Job: Automatic Creation of Purchase Orders from Requisitions screen, make the following entries:Choose 1 Template Selection and go to 1. Template Selection area to make the following entries:Job Template: <Job Template>, for example, Automatic Creation of Purchase Orders from RequisitionsJob Name: <Job Name>, for example, Automatic Creation of Purchase Orders from RequisitionsChoose Step 2 and go to 2. Scheduling Options area to make the following entries:Start Immediately : <selected>Start: <Current Time>Note If the job needs to be run on a regular basis, choose Define Recurrence Pattern.Choose Step 3 and go to 3. Parameters area to make the following entries:Per Requisition:<selected>Per Company Code: <selected>Per Contract: <selected>Purchase Requisition: <Created PR Number>Note Set Parameter settings according to your needs.Choose Schedule. | The job is created. |  |
| 5 | Convert Purchase Requisition to Purchase Order | On the Application Jobs screen.Go to Jobs (X) area and check the status until it changes to Finished. | The Job automatically converts Purchase Requisition to Purchase Order. |  |
| 6 | Check Result | Choose Result.Choose Preview. | The Purchase Order is created. |  |

|  |
| --- |
| Note You may go to the Fiori Launchpad main screen. On the Fiori Launchpad main screen, choose Search button on the top. Choose Purchase Order from the drop-down box, and enter the Purchase Order number in the field Search In: Purchase Orders. Select the Purchase Order you want to display on the Search screen. |

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

### Evaluations

#### Batch Information Cockpit – Top-Down and Bottom-Up Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this functionality you can identify which batches are delivered to which customer and which raw material batches are used for the production of which finished product. You can adapt the selection in the Batch Information Cockpit to customer-specific requirements by creating user-specific groups. You can get additional information by using subsequent actions.

In this case the evaluation is limited to the purchasing process. As soon as you have purchased the raw materials RM0501 and/or delivered the finished good to a customer the evaluation is automatically enhanced with these information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto the SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad using the Quality Technician role. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Batch Information Cockpit (BMBC). | The Batch Information Cockpit screen displays. |  |
| 3 | Select batches | On the Batch Information Cockpit screen, make the following entries.Go to Material (Original) tab.Material (Original): RM0501Plant: 3310For batch class and characteristics relevant materials, refer to Master Data, Organizational Data, and Other Data section.Choose Execute Selection. | One or multiple batches are displayed in the left screen area Selection Result for Batches. The standard sorting is done per material number. |  |
| 4 | Expand Selection | In the section Selection Result for Batches, select checkbox for RM0501 and then choose Expand subtree or Expand node. | The selection result is analyzed and a batch for further investigation is identified. |  |
| 5 | Start Analysis | Right click on one selected batch and choose either Usage (Top-Down) or Usage (Bottom-up). | The batch where-used list displays. |  |
| 6 | Analyze the batch where used list | The usage of the batch can be analyzed and the specific documents (such as batch master record, production orders and sales order) can be accessed via double click. |  |  |
| 7 | Analyze assigned Inspection lots | Mark one line in the Details (Usage) table and choose button Inspection Lots to review inspection lots assigned to the selected element. |  |  |
| 8 | Analyze material document | Select one document and choose Documents. | The usage displays again and after selecting documents the respective material document display. |  |
| 9 | Go to the material document | Select the material document in the pop up and choose Choose (F2).Note To display the material document, you need further authorizations that are granted by your company, for example, SAP_BR_INVENTORY_MANAGER. | The material document displays.Note Your user should have the appropriate authorizations. |  |

|  |
| --- |
| Note The materials PK0501, PK0502 and PK0504 are also batch managed. You can execute the steps mentioned above for these materials but need to skip the inspection lot analysis as these packaging materials are not subject to Quality Management during procurement process. |

## Appendix

### Process Integration

N/A

### Preceding Processes

The following processes and conditions can precede this process.

| Process | Business Condition |
| --- | --- |
| 5OI - Production Capacity Evaluation and Leveling – Consumer Products | You can execute this scope item before executing 5W3. In that case you can skip the process steps "Option 1: Create Purchase Requisition via MRP Run " from this test case. |

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 5HK - Quality Management in Discrete Manufacturing – Consumer Products | You can execute the scope item afterwards. The components for the production process are already purchased with this scope item and are available in stock. |
| 5W4 - Subcontracting - Consumer Products | You can execute the scope item afterwards. The components for the production process are already purchased with this scope item and are available in stock. |

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
> Flagged while digesting this document, not verified: Approve Purchase Requisition says PRs need approval when total > 500 AED and purchase group 002, but the PR workflow is configured with net amount >= 10 AED.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Approve Purchase Order says POs need approval when total > 500 AED and purchase group is 001, but the PO workflow and manual PO note use purchasing group 002.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Storage location 331C is used in PO, goods receipt and stock steps but the organization data lists only 331A, 331B and 331R.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/direct-procurement-with-inbound-delivery-2tx-ae-test-script-sap-s-4han]]
- related-to :: [[10-procurement/test-script-cross-company-purchasing-organization-2r3-ae-854]]
- related-to :: [[10-procurement/test-script-sap-s-4hana-cloud-public-edition-procurement-of-direct-mat]]
- see-also :: [[08-sales-order-management/customer-returns-management-consumer-products-61v-ae-test-script-sap-s]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5W3_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 157,066 chars in the whole document
