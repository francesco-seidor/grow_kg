---
id: 10-procurement/test-script-subcontracting-consumer-products-5w4-ae-sap-s-4hana-cloud
title: "Test Script: Subcontracting - Consumer Products (5W4_AE), SAP S/4HANA Cloud Public Edition (5W4_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5W4_AE: subcontracting with batch anonymization, MRP areas, quality inspection and invoicing (plant 3310)."
cluster: 10-procurement
tags: [kb/procurement, topic/subcontracting-procurement, topic/end-to-end-produce-and-sell]
aliases: [5W4_S4CLD2608_BPD_EN_AE]
keywords: [Subcontracting Procurement, subcontracting process, subcontracting purchase order, planned independent requirements, material requirements planning, subcontracting mrp area, batch traceability, component transfer to subcontractor, goods receipt, quality inspection]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5W4_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1125
topic: 10-procurement/subcontracting-procurement
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Subcontracting - Consumer Products (5W4_AE), SAP S/4HANA Cloud Public Edition (5W4_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5W4_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Subcontracting Procurement** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Subcontracting – Consumer Products (5W4_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232857680)

[2 Prerequisites 5](#_Toc232857681)

[2.1 System Access 5](#_Toc232857682)

[2.2 Roles 5](#_Toc232857683)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232857684)

[2.4 Business Conditions 9](#_Toc232857685)

[2.5 Preliminary Steps 9](#_Toc232857686)

[2.5.1 Define Item Category Determination in Deliveries 9](#_Toc232857687)

[2.5.2 Create Purchasing Info Record (Optional) 10](#_Toc232857688)

[2.5.3 Check Flexible Workflow for Purchase Order Approval 12](#_Toc232857689)

[2.5.4 Configure Flexible Workflow for Purchase Order 13](#_Toc232857690)

[2.5.5 Change Master Inspection Characteristic Visual Pack Check 14](#_Toc232857691)

[2.5.6 Create Initial Material Stock 15](#_Toc232857692)

[2.5.7 Create Batch 17](#_Toc232857693)

[3 Overview Table 19](#_Toc232857694)

[4 Test Procedures 22](#_Toc232857695)

[4.1 Anonymous Forecast and MRP 22](#_Toc232857696)

[4.1.1 Option 1: Create Planned Independent Requirements 22](#_Toc232857697)

[4.1.2 Option 2: Create Planned Independent Requirements by Upload File 24](#_Toc232857698)

[4.1.3 Material Requirements Planning at Plant Level 26](#_Toc232857699)

[4.1.4 Evaluate Stock/Requirements Situation and Prepare Planned Order for Subcontracting 28](#_Toc232857700)

[4.1.5 Convert Planned Order to Purchase Requisiton 29](#_Toc232857701)

[4.2 Subcontracting 30](#_Toc232857702)

[4.2.1 Create Purchase Order 30](#_Toc232857703)

[4.2.1.1 Option 1: Convert Purchase Requisition to Purchase Order 30](#_Toc232857704)

[4.2.1.2 Option 2: Create Purchase Order manually 32](#_Toc232857705)

[4.2.1.3 Option 3 : Create Purchase Order manually with Inbound Delivery 33](#_Toc232857706)

[4.2.2 Approve Purchase Orders (Optional) 35](#_Toc232857707)

[4.2.3 Monitor Subcontracting Documents (Optional) 36](#_Toc232857708)

[4.2.4 Material Requirements Planning at Plant Level (Optional) 37](#_Toc232857709)

[4.2.5 Evaluate Stock/Requirements Situation (Optional) 38](#_Toc232857710)

[4.2.6 Transfer Components to the Subcontractor 40](#_Toc232857711)

[4.2.7 Batch Transfer Posting 41](#_Toc232857712)

[4.2.8 Batch Traceability 42](#_Toc232857713)

[4.2.9 Evaluate Stock/Requirements Situation 43](#_Toc232857714)

[4.2.10 Create Inbound Delivery for Subcontracting Purchase Order (Optional) 44](#_Toc232857715)

[4.2.11 Goods Receipt for Subcontracting Purchase Order 45](#_Toc232857716)

[4.2.11.1 Option 1: Receive Goods for Subcontracting Purchase Order 45](#_Toc232857717)

[4.2.11.2 Option 2: Receive Goods from Subcontracting Purchase Order with Inbound Delivery 47](#_Toc232857718)

[4.2.12 Evaluate Stock/Requirements Situation 48](#_Toc232857719)

[4.3 Quality Inspection 49](#_Toc232857720)

[4.3.1 Display Material Stock Before Quality Inspection (Optional) 49](#_Toc232857721)

[4.3.2 Display Inspection Plan for Inspection Characteristics (Optional) 50](#_Toc232857722)

[4.3.3 Display Quality Technician Overview (Optional) 51](#_Toc232857723)

[4.3.4 Display Open Inspection Lots (Optional) 52](#_Toc232857724)

[4.3.5 Record Inspection Results 53](#_Toc232857725)

[4.3.6 Display Quality Engineer Overview (Optional) 55](#_Toc232857726)

[4.3.7 Make Usage Decision 57](#_Toc232857727)

[4.3.8 Display Material Stock after Usage Decision (Optional) 58](#_Toc232857728)

[4.4 Invoicing 59](#_Toc232857729)

[4.4.1 Create Supplier Invoice 59](#_Toc232857730)

[4.4.2 Review Supplier Invoice (Optional) 61](#_Toc232857731)

[4.5 Batch Traceability 62](#_Toc232857732)

[4.5.1 Batch Information Cockpit - Top-Down and Bottom-Up Analysis 62](#_Toc232857733)

[5 Appendix 64](#_Toc232857734)

[5.1 Process Integration 64](#_Toc232857735)

[5.2 Preceding Processes 64](#_Toc232857736)

[5.3 Succeeding Processes 64](#_Toc232857737)

## Purpose

Overview

This business process describes a subcontracting process in the Consumer Products industry, using Subcontracting MRP Areas for disposition and Quality Inspection during goods receipt from subcontractor. It outlines a typical display packaging process executed by a subcontractor with the provision of components. Workflow functionalities are optional.

The process begins with creating demand forecast for finished subcontracting materials, represented by Planned Independent Requirements (PIRs). You can enter these PIRs manually or upload them via a load file. Based on PIRs, Material Requirements Planning creates a purchasing plan for the finished materials and explodes the Bill of Materials structure for the component, which will be provided to the subcontractor. As a result, finished and packaging material demands are planned, leading to planned orders or purchase requisitions that trigger alternative procurement or production scenarios (not part of this business process).

The display packaging can either be done in house (via production order – not part of the scenario) or sent to a subcontractor, for example, due to machine breakdown or limited capacity. The MRP run creates planned orders that can be converted to a production order (not part of this scenario) or to a purchase requisition. The purchase requisition is converted into a subcontract purchase order. As an alternative, the purchase order can be created manually by a requestor. The purchase order is subject to approval based on predefined parameters before being issued to the subcontractor.

The system creates the outbound delivery, and the materials are picked and shipped to the subcontractor. The picking process transfers the components to the subcontracting MRP Area, indicating that the company still owns the components, but they are now at the subcontractor site.

The consumption of the sent components from the subcontracting MRP Area is recorded upon the receipt of the value-added finished material. When you supply the finished material, the goods receipt is created. Subsequently, the invoicing process is triggered.

As a process variant, inbound deliveries can be created to be able to monitor the delivery date. In that case, the goods receipt will be executed with relation to the inbound delivery and not to the purchase order.

The components sent to the subcontractor and the subcontracted material are batch-managed. This might cause difficulties with the batch confirmation of the installed components, especially when producing the subcontracted material consumes several components. The subcontractor, who receives the component batches, can't always guarantee which component batch was consumed in which subcontracted material batch. This can be due to organizational, personnel, or cost reasons.

To ensure traceability, the component batches are partially anonymized before they are sent to the subcontractor. This means that several component batches of a product are combined into one anonymous delivery batch by transferring the batch to batch of the component. It is easier for the subcontractor to report back the delivery batch of the components that has been included in a subcontracted material batch.

When the goods receipt is posted for the subcontracted finished good, the components are automatically posted and the component stock at the subcontractor is decreased.

The finished material is posted to quality inspection stock and an inspection lot is created based on an inspection plan. The quality technician records the inspection results. Based on these results, the quality engineer makes a usage decision, such as accepting or rejecting the material, or posting the material to unrestricted or blocked stock. If the results are rejected, a defect is automatically recorded.

If the components and the display are batch-managed, there can be difficulties with the batch confirmation of the installed components, especially when several components are installed in a display. If the display consists of several components and their component batches and the subcontractor has been sent several component batches, they cannot always guarantee that they can record which component batch was installed in which display batch. This can be due to organizational, personnel, or cost reasons.

To ensure traceability, the component batches are partially anonymized before they are sent to the subcontractor. This means that several component batches of a product are combined into one delivery batch. It is easier for the subcontractor to report back the delivery batch of the components that have been included in a display batch.

The component batch is made anonymous as a delivery batch by transferring the batch to batch of the component.

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
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Quality Technician | SAP_BR_QUALITY_TECHNICIAN | Quality Inspection | SAP_BR_QUALITY_TECHNICIAN |  |
| Quality Engineer | SAP_BR_QUALITY_ENGINEER | Quality Engineering | SAP_BR_QUALITY_ENGINEER |  |
| Quality Planner | SAP_BR_QUALITY_PLANNER | Quality Planning | SAP_BR_QUALITY_PLANNER |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

This scope item requires new master data set to be created and the needed master data objects are mentioned below.

Material Master Data:

Material Masters mentioned in this document are to be created for plants. Refer to the attached file to know the field level values to be used in for the new materials to be created.

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Material | FG0502 | Display Medium + Dark Roast 48 x 1 kg Arabica | Batch Managed Finished Material, Manufacturing Date |
| Material | FG0511 | Carton 12x1kg Bags Medium Beans Arabica | Batch Managed Finished Material, Component for Subcontracting |
| Material | FG0512 | Carton 12x1kg Bags Dark Beans Arabica | Batch Managed Finished Material, Component for Subcontracting |
| Material | PK0508 | Display Carton Coffee Beans 48 x 1 kg | Packaging Material, Costing relevant |
| Material | PK0504 | Label | Packaging Material, Costing relevant |

Organization Data

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |
| Controlling Area | A000 | Controlling Area A000 |  |

Bill of Material Structure

| Material | Level | Material Type | Unit | Characteristics of Material | Component Quantity | Component UOM |
| --- | --- | --- | --- | --- | --- | --- |
| FG0502 | 0 | FERT | PC | Finished Good for MTS and Subcontract processing with Batch Management | 1 | PC |
| FG0511 | 1 | FERT | PC | Finished Material, Batch Managed | 2 | PC |
| FG0512 | 1 | FERT | PC | Finished Material, Batch Managed | 2 | PC |
| PK0508 | 1 | VERP | PC | Packaging Material, Display Carton | 1 | PC |
| PK0504 | 1 | VERP | PC | Packaging Material, Label | 1 | PC |

Suppliers:

Below mentioned Suppliers (Business Partners) will be used in this scenario.

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Supplier | 33305001 | Domestic AE Supplier 05001 | Subcontractor |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |

Quality Master Inspection Characteristics

The following Master Inspection Characteristic are used in this scenario.

| Master data | Value | Plant | Master. data details | Comments |
| --- | --- | --- | --- | --- |
| Master Inspection Characteristic | YQM00008 | 3310 | Visual Pack Check |  |
| Master Inspection Characteristic | YQM00009 | 3310 | Label Check |  |

For more information on creating your own master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BLD | Create Production Version - MDS |
| BNQ | Create Quality Inspection Plan - MDS |
| BNE | Create Supplier Master - MDS |
| BHD | Create Purchasing Info Record - MDS |
| 3Y1 | Create Product Master of Type "Packaging" - MDS |
| 2ZW | Create Batch Management Master Data - MDS |

### Business Conditions

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation | You have completed the step described in the Standard Cost Calculation (BEG) test script. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |
| J58 - Accounting and Financial Close | Execute to create open posting periods. |

### Preliminary Steps

#### Define Item Category Determination in Deliveries

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
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen is displayed. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Application Area: Supply ChainSub Application Area: Delivery Management | All entries are displayed in All Items section. |  |
| 5 | Item Name | Choose Item Deliveries and choose arrow at the item end. | A List of configuration steps displays. |  |
| 6 | Choose Configuration Step | For Deliveries, Choose the as action step Define Item Category Determination in Deliveries and press Configure. | The Configuration opens. |  |
| 7 | New Entries | Add a new entry for following combination:Delivery Type: ELItem category Group: ERLAUsage: VDefault Item category : ELN |  |  |
| 8 | Save your data | Choose Save. | The Delivery Type is enhanced for Item Category. |  |

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
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Create Purchasing Info Record (ME11). | The Create Info Record: Initial Screen displays. |  |
| 3 | Enter Initial Data | Make the following entries:Supplier: 33305001Material: FG0502Purchasing Organization: 3310Plant: 3310Select Subcontracting, then press Enter. | The Create Info Record: General Data screen displays. |  |
| 4 | Choose Purch. Org. Data 1 | Choose Purch.Org.Data 1. | The Create Info Record: Purch. Organization Data1 screen displays. |  |
| 5 | Enter Item Data | Enter the following values:Pl. Deliv. Time: 10 DayPurch.Group: 001Tol. Underdl: 10%Tol. Overdl: 10%Standard Qty: 100Net Price: 25,00Price unit: PCTax Code: <Input Tax Code>Version: 0003Press Enter. |  |  |
| 6 | Save your data | Choose Save. | A purchasing info record for subcontracting procurement is saved. |  |

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

#### Change Master Inspection Characteristic Visual Pack Check

Purpose

To run through this business scenario, master inspection characteristic YQM00008 Visual Pack Check and YQM00009 Label Check need to be changed to enable classed results recording.

Prerequisite

Master Inspection Characteristic is already available in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Planner. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Change Master Inspection Characteristic (QS23). | Change Master Insp. Characteristic Version: Initial Screen appears. |  |
| 3 | Change Data for Master Inspection Characteristic | In the Change Master Insp. Characteristic Version: Initial Screen make the following entries:Plant: 3310Master Inspection Characteristic: YQM00008 Visual Pack CheckChoose Master Inspection Characteristic. | Change Master Insp. Characteristic Version: General Data view appears. |  |
| 4 | Change Control Indicator for Master Inspection Characteristic | In the Edit Characteristic Click Control Indicators, Change the following option: flagClassed RecordingChoose Continue without further changes.Choose Continue to exit edit. | The control indicator for MIC is changed. |  |
| 5 | Save Your Data | Choose Save. | Your data is saved. |  |
| 6 | Change next Master Inspection Characteristic | Repeat steps 1 - 5 for Master Inspection Characteristic YQM00009 Label Check. |  |  |

#### Create Initial Material Stock

Purpose

In a real business scenario, initial material stock are usually purchased from external suppliers through standard purchasing or subcontracting processes. For only testing purpose, this process step shows you how to create and post the initial material stock to storage locations directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Post Goods Movement (MIGO) screen displays. |  |
| 3 | Choose Document Type | Choose Goods Receipt and Other. Select for Init.entry of stBal. 561 without any stock indicator and press Enter. |  |  |
| 4 | Enter Data | In the Detail Data section, make the following entries and press Enter:On the Where tab:Goods Movement Type: 561Plant: 3310Storage Location: 331C for PK05XX (Packaging Materials), 331A for FG05XX (Finished Materials)On the Quantity tab:Quantity: <Quantity>, for example, <1000 PC>On the Material tab:Material: <BOM Material>, refer to section Master Data, Organizational Data, and Other Data for Bill of Material Structure. You must create initial stock for all materials except for FG0502.On the Batch tab (only available when materials are batch managed):Batch: <batch number> (optional)For FG05XX materials enter Date of Manufacturing: <today´s date>Ensure that Item OK is selected and choose Next Item to maintain entries for the next material. |  |  |
| 5 | Check | Choose Check. | The document is ready to be posted. |  |
| 6 | Post | Choose Post. | Material document XXX is posted and materials are available in stock. |  |

|  |
| --- |
| Note We recommend that you check stock level for FG0502. To do that, log on to the SAP Fiori launchpad as a Production Planner, and open Manage Material Coverage - New Version (F0251A) app. Remove some stock if there is already sufficient amount of stock in store. Otherwise, no planned orders can be generated later. Use Post Goods Movement (MIGO) app with movement type 562 resp. for Init.entry of stBal. 562 without any stock indicator to remove stock and run the test again. |

#### Create Batch

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Even most batches are automatically created during goods receipt it's also necessary to create batches manually. The DRAFT framework enables the creation of a draft instance that can be converted to an active instance at any point in time.

For the subcontracted finished good the batch which will be ordered will be created in advance. The batches from the Finished goods defines the shelf-life expiration date of the subcontracted finished good. In our example, the earliest shelf-life expiration date of the batches of the Finished goods will be used as shelf-life expiration date to the finished good.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment. |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Batches (F2462). | The Manage Batches screen displays. |  |
| 3 | Create a Draft Version of a Master Batch Record | Choose Create in the header area. | The Batch screen displays and a new draft master batch record is created. |  |
| 4 | Maintain the Master Batch Record | Make following entries in the Header Data section and choose Enter:Material : FG0502Batch: <batch number for the finished good>Shelf-life expiration date:<earliest shelf life expiration date of the components>Date of Manufacture: <Current date>Country/Region of Origin: AE | The classification of the batch displays when the material field valuted.When you select enter the draft version of the master batch record is saved and the respective information displays in the bottom status bar.Depending on the configuration of the classification the characteristics can be valuated or are displayed as read only fields. |  |
| 5 | Leave the Page | Leave the page without choosing Create.Choose Back. | The Home screen displays. |  |
| 6 | Access the App | Open Manage Batches (F2462). | The Manage Batches screen displays. |  |
| 7 | Search the Draft Master Batch Record | Make following entries:Material Number: FG0502Editing Status: Own DraftChoose Go. | The list of suitable draft Master Batch Records displays. You should also find the one created in step 4. |  |
| 8 | Save the Daft Master Batch Record | Choose the line with the draft master batch record and choose Create on the Batch screen. | The draft master batch record is opened and is converted to a persistent one. If the batch number is configured to be assigned automatically, it will be populated.The batch fact sheet is shown in display mode.Make a note of the batch number ____________________. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the home page will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the home page using the search bar.

If you want to personalize the home page and include the hidden apps, navigate to your user profile and choose Settings > App Finder.

| Process Step | Business Role | Transaction/App | Expected Output |
| --- | --- | --- | --- |
| Anonymous Forecast and MRP |  |  |  |
| [Option 1: Create Planned Independent Requirements](#unique_15) | Production Planner | Maintain PIRs (F3445) | Planned Independent Requirements for Finished Material are created. |
| [Option 2: Create Planned Independent Requirements by Upload File](#unique_16) | Production Planner | Maintain PIRs (F3445) | Planned Independent Requirements for Finished Material are created. |
| [Material Requirements Planning at Plant Level](#unique_17) [page ] 26 | Production Planner | Schedule MRP Runs (F1339) | Planned Independent Requirements for Finished Materials and also the components are planned. |
| [Evaluate Stock/ Requirements Situation and Prepare Planned Order for Subcontracting](#unique_18) | Production Planner | Monitor Stock / Requirements List - Old Version (MD04) | The Stock/Requirements situation for the planned materials is analyzed. |
| [Convert Planned Order to Purchase Requisition](#unique_19) | Production Planner | Convert Planned Orders - to Purchase Requisitions (MD15) | A subcontracting purchase requisition is created. |
| Subcontracting |  |  |  |
| [Create Purchase Order - Option 1: Convert Purchase Requisition to Purchase Order](#unique_20) | Purchaser | Create Purchase Order via Purchase Requisition Assignment List (ME58) | A Purchase Order is created. |
| [Create Purchase Order - Option 2: Create Purchase Order manually](#unique_21) | Purchaser | Create Purchase Order - Advanced (ME21N) | A Purchase Order is created. |
| [Create Purchase Order - Option 3: Create Purchase Order manually with Inbound Delivery](#unique_22) | Purchaser | Create Purchase Order - Advanced (ME21N) | A Purchase Order is created. |
| [Approve Purchase Order (Optional)](#unique_23) | Purchasing Manager | My Inbox - All Items (F0862) | A purchase Order is released. |
| [Monitor Subcontracting Documents (Optional)](#unique_24) | Purchaser | Monitor Subcontracting Documents (F3095) | The subcontracting documents are reviewed. |
| [Material Requirements Planning at Plant Level (Optional)](#unique_25) [page ] 37 | Production Planner | Schedule MRP Runs (F1339) | Planned Independent Requirements for Finished Materials and also the components are planned. |
| [Evaluate Stock/Requirements Situation (Optional)](#unique_26) | Production Planner | Monitor Stock / Requirements List - Old Version (MD04) | The Stock/Requirements situation for the planned materials is analyzed. |
| [Transfer Components to the Subcontractor](#unique_27) | Inventory Manager | Subcontracting Cockpit (F2948) | The components are delivered to the subcontractor. |
| [Batch Transfer Posting](#unique_28) [page ] 41 | Warehouse Clerk | Post Goods Movement (MIGO) | Batches are transferred to delivery batch. |
| [Batch Traceability](#unique_29) [page ] 42 | Quality Technician | Batch Information Cockpit (BMBC) | Batch analysis is executed. |
| [Evaluate Stock/Requirements Situation](#unique_30) | Production Planner | Monitor Stock / Requirements List - Old Version (MD04) | The Stock/Requirements situation for the planned materials is analyzed. |
| [Create Inbound Delivery for Subcontracting Purchase Order (Optional)](#unique_31) | Receiving Specialist | Create Inbound Delivery (VL31N) | The inbound delivery for a subcontracting purchase order is created. |
| [Goods Receipt for Subcontacting Purchase Order - Option 1: Receive Goods from Subcontracting Purchase Order](#unique_32) | Warehouse Clerk | Post Goods Movement (MIGO) | The goods receipt from subcontracting material is posted. |
| [Goods Receipt for Subcontracting Purchase Order -Option 2: Receive Goods from Subcontracting Purchase Order with Inbound Delivery](#unique_33) | Receiving Specialist. | Change Inbound Delivery (VL32N) | The The Change inbound delivery Initial screen is displayed. |
| [Evaluate Stock/Requirements Situation](#unique_34) | Production Planner | Monitor Stock / Requirements List - Old Version (MD04) | The Stock/Requirements situation for the planned materials is analyzed. |
| Quality Inspection |  |  |  |
| [Display Material Stock Before Quality Inspection (Optional)](#unique_35) | Inventory Manager | Stock - Single Material (F1076) | Material stock is displayed. |
| [Display Inspection Plan for Inspection Characteristics (Optional)](#unique_36) | Quality Technician | Display Inspection Plan (QP03) | The data of inspection plan for the material is displayed. |
| [Display Quality Technician Overview (Optional)](#unique_37) | Quality Technician | Quality Technician Overview (F2361) | The inspection results history is reviewed. |
| [Display Open Inspection Lots (Optional)](#unique_38) | Quality Technician | Manage Inspection Lots (F2343) | The open inspection lots are displayed. The Quality Technician can select the next inspection lot for which he or she wants to record inspection results. |
| [Record Inspection Results](#unique_39) | Quality Technician | Record Inspection Results - Hierarchical Worklist (QE51N) | Inspection results are recorded. |
| [Display Quality Engineer Overview (Optional)](#unique_40) | Quality Engineer | Quality Engineer Overview (F2360) | The open inspection lots are displayed. The Quality Engineer can select the next inspection lot he or she wants to record the usage decision for. |
| [Make Usage Decision](#unique_41) | Quality Engineer | Manage Usage Decisions (F2345) | Usage decision is posted. |
| [Display Material Stock after Usage Decision (Optional)](#unique_42) | Warehouse Clerk | Stock - Single Material (F1076) | Material stock is displayed. Depending on the usage decision, the stock quantity is shown in the blocked stock, in unrestricted use stock or in another storage location. |
| Invoicing |  |  |  |
| [Create Supplier Invoice](#unique_43) | Accounts Payable Accountant | Create Supplier Invoice (F0859) | Invoice verification is done. |
| [Review Supplier Invoice (Optional)](#unique_44) | Accounts Payable Accountant | Supplier Invoices List (F1060A) | Invoice verification is done using document list. |
| Batch Traceability |  |  |  |
| [Batch Information Cockpit - Top-Down and Bottom-Up Analysis](#unique_45) | Quality Technician | Batch Information Cockpit (BMBC) | Batch Analysis is executed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Anonymous Forecast and MRP

#### Option 1: Create Planned Independent Requirements

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

#### Option 2: Create Planned Independent Requirements by Upload File

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

The Make-to-Stock finished goods are planned at plant level. There is now a requirement for FG0502 in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirements Planning (MRP)Job Name: MRP for FG0502Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: <select>Recurrence Pattern: Single RunChoose OK.Choose Step 3.For 3. Parameters section:Plant: 3310Material: FG0502Changed BOM Components: <select>Stock Transfer Materials: <select>Scheduling: 2Planning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG0502 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

#### Evaluate Stock/Requirements Situation and Prepare Planned Order for Subcontracting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock/requirements situation for Make-to-Stock finished goods (FG0502). The material FG0502 is mainly used for inhouse production but subcontracting is also possible, for example due to machine breakdown. Therefore you prepare a planned order for subcontracting.

Prerequisite

Requirement planning is carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Monitor Stock / Requirements List - Old Version (MD04). | The Monitor Stock / Requirements List screen displays. |  |
| 3 | Maintain Data | On the Stock/Requirements List: Initial Screen make the following entries and choose Continue :Material: FG0502Plant: 3310 | The Stock/Requirements List as of xxx hrs is displayed. |  |
| 4 | Review Stock / Requirements Situation | On the Stock/Requirements List as of xxx hrs check the planned orders created by the MRP run for material FG0502. | The planned orders created by MRP run are displayed. |  |
| 5 | Prepare Planned Order | Double Click on one of the planned orders you want to use for Subcontracting.On the Additional Data for MRP Element Screen Choose Change Element.Change the Production Version to 0003 and choose Save.Afterwards choose Refresh to update the Stock-/Requirements List.Make a note of the Planned Order Number ______. | The Production version is changed to 0003. |  |

#### Convert Planned Order to Purchase Requisiton

Purpose

This process step shows you how to convert the planned order relevant to subcontracting into a purchase requisition.

Prerequisite

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Convert Planned Orders - to Purchase Requisitions (MD15). | The Monitor Stock / Requirements List: Initial Screen is displayed. |  |
| 3 | Maintain Data | On the Collective Conversion of PlndOrd. To Pur.Req.: Initial Screen Screen make the following entries and choose Continue.Select radio button for MaterialMaterial: FG0502Plant: 3310Procurement Type: X | The planned orders created by MRP run are displayed. |  |
| 4 | Select Planned Order | Select the Planned Order noted in previous step and choose Convert Online. |  |  |
| 5 | Adopt Purchase Requisiton | On the Convert Planned Order into Purchase Req Details Screen make the following Entry:Item Category: LChoose button Assign Source of Supply.Choose button Process Components. The list of components which will be delivered to the subcontractor is shown.Choose Menu – Component List – Component Availability to check if all components are available.Choose Back twice. |  |  |
| 6 | Save your Entries | Choose Save. |  |  |

### Subcontracting

#### Create Purchase Order

##### Option 1: Convert Purchase Requisition to Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, a purchase requisition for planned subcontracting is assigned and a corresponding purchase order is created. In the purchase order the batch number which was created in the preliminary steps is maintained.

|  |
| --- |
| Note If you want to use the Save Draft feature in this app, you have to use a personalized user. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the Purchaser role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Create Purchase Order via Purchase Requisition Assignment List (ME58). | A selection screen is displayed. |  |
| 3 | Select Purchase Requisition | Search for all Purchase Requisition for material which are assigned to the subcontractingSupplier: 33305001Click on Execute. | The Assign and Process Purchase Requisitions screen is displayed. |  |
| 4 | Transfer Purchase Requisitions with assignment | Mark the Supplier in the Assignments register tab and click on Create Purchase Order. | The Purchase Requisitions list is displayed in screen Create Purchase Order. |  |
| 5 | Prepare the Purchase Order | Select the purchase requisition which was converted from Planned Order to Purchase Requisition.Click on Adopt to move the selected Purchase requisition to the shopping cart.A pop up might come up. In that case click on Re-Explode in the pop-up to reexplode the Bill Of Material. | The Purchase Order screen is prepared and maintained with the data from the Purchase Requisition. |  |
| 6 | Enter Batch | Under Item Detail Select the Material Data and make the following entry:Batch Number: <Batch number from preliminary steps> |  |  |
| 7 | Check the component list | Check the exploded component list in the detail data in register tab Select Material Data.Click on Components top-right corner in Material Data to display the list of components for the main line item FG0502.Note In case no batch number is automatically assigned to the PO, the batch number should be maintained manually in the PO. | Components are maintained from the Bill Of Material. |  |
| 8 | Maintain Tax Code | Click on register tab Invoice and enter the Tax Code for the line item.Tax Code: <Input Tax Code> |  |  |
| 9 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A Purchase Order is created. |  |

##### Option 2: Create Purchase Order manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity creates a purchase order for subcontract material. This activity is only required if you do not convert an existing purchase requisition as described in the section ”Convert Purchase Requisition to Purchase Order”.

|  |
| --- |
| Note You can store purchase order data as template for frequently used data. To save the data to a template, choose Save as Template. To load data from a template, choose Load from Template. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad Purchaser . | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order screen is displayed with a list of existing Purchasing Document Items. |  |
| 3 | Create Purchase Order data | Enter the following data :Enter Supplier : 33305001 and choose EnterPurchasing Org: 3310Purchasing Group: 001Company Code: 3310Currency: AEDEnter the below Items sectionItem Category: Subcontracting (L)Material (Original): FG0502Quantity: x PCDelivery Date: <enter Date>Plant: 3310Storage Location: 331ABatch: <batch number> and choose EnterIn the Item Details section open the tab InvoiceTax Code: <Input Tax Code> |  |  |
| 5 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A Purchase Order is created. Make a note of the purchase order number ________. |  |

##### Option 3 : Create Purchase Order manually with Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity creates a purchase order for subcontracting material. This activity is only required if you do not convert an existing purchase requisition as described in the section ”Convert Purchase Requisition to Purchase Order”. In addition to option 2, this purchasing order requires the creation of an inbound delivery afterward. The goods receipt will not be posted with respect to the purchase order but the inbound delivery.

|  |
| --- |
| Note You can store purchase order data as a template for frequently used data. To save the data to a template, choose Save as Template. To load data from a template, choose Load from Template |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad Purchaser . | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order screen is displayed with a list of existing Purchasing Document Items. |  |
| 3 | Create Purchase Order data | Enter the following data :Enter Supplier : 33305001choose Enter and make the following entries:Purchasing Org: 3310Purchasing Group: 001Company Code: 3310Currency: AEDEnter the below Items sectionItem Category: Subcontracting (L)Material : FG0502Quantity: x PCDelivery Date: <enter Date>Plant: 3310Storage Location: 331AIn the Item Details section, open the tab Material Data.Press Create Batch and confirm the popup with Enter. A batch number is populated in the Batch Number text box.In the Item Details section, open the tab Invoice and enter the following values.Tax Code: <Input Tax Code>In the Item Details section, open the tab Confirmations and enter the following values.Conf. control: 0004 Inbound Delivery |  |  |
| 5 | Save Purchase Order | Choose Save and when the purchase order number is displayed, write it down for further use. | A Purchase Order is created. Make a note of the purchase order number ________. |  |

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
| Note Only POs with a value higher than 500.00 AED and Purchasing Group 001 have to be released in this transaction. POs with a value under this amount do not need to be released. For POs under this amount, this step can be skipped. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on the SAP Fiori Launchpad with the Purchasing Manager role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Approve Purchase Order | Open My Inbox - All Items (F0862). | A list of already created Purchase Orders is displayed. |  |
| 3 | Check Purchase Order Status | Click on Filter. In the pop-up, filter by Status, select statuses Ready and In Progress. Click on OK. | The Purchase Orders without follow-on documents (w/o status Follow-On Documents) and a net value of 500 AED or more have the status In Approval. |  |
| 4 | Release Purchase Order | Select the Purchase order in left of the screen and click Approve in bottom right. | The Submit Decision dialog box is displayed. |  |
| 5 | Enter Release Reason | Enter the approval reason if needed, then choose Submit. | The Purchase Order is approved. |  |
| 6 | Back to Fiori Launchpad | Choose the Home button to go back to the Fiori Launchpad. | The Fiori Launchpad is displayed. |  |

#### Monitor Subcontracting Documents (Optional)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the Fiori App | Open Monitor Subcontracting Documents (F3095). | The Monitor Subcontracting Documents screen displays. |  |
| 3 | Monitor Subcontracting Document | Enter the following data:Subcontractor: 33305001Choose Go.Note If the subcontractor field does not appear on the screen, select the field on Adapt Filter. |  |  |
| 5 | Manage Purchase Order | Check the details of your subcontracting document by clicking the item. |  |  |

#### Material Requirements Planning at Plant Level (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The aim of material requirements planning is to tailor available capacities and receipts on time to suit requirements quantities. You can use MRP or consumption-based planning for this purpose. Single-item multilevel requirement planning is performed for plant 3310.

The conversion of purchase requisitions to purchase orders for material FG0502 has created. Subcontracting requirements for the components FG0511, FG0512, PK0504 and PK0508 between plant MRP Area 3310 and Subcontracting MRP Area 3310SUB051. This business process works with MRP Areas stock transfer elements which are generated for stock movements between the MRP Areas during MRP run.

The MRP run is an optional step which enables you to get more familiar with the planning with MRP Areas itself. It is not required to run through the process.

Prerequisite

The Make-to-Stock finished goods are planned at plant level. There is now a requirement for FG0502 in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirements Planning (MRP)Job Name: MRP for FG0502Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: <select>Recurrence Pattern: Single RunChoose OK.Choose Step 3.For 3. Parameters section:Plant: 3310Material: FG0502Changed BOM Components: <select>Stock Transfer Materials: <select>Scheduling: 2Planning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG0502 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

#### Evaluate Stock/Requirements Situation (Optional)

Purpose

This process step shows you how to display the stock/requirements situation for the Finished and packaging materials which will be provided to the subcontractor during subcontracting process.

In this step, you can check the stock transfer elements created during MRP run for components provided to the subcontractor.

Prerequisite

Requirement planning is carried out after subcontracting purchase order creation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Monitor Stock / Requirements List - Old Version (MD04). | The Stock / Requirements List: Initial Screen is displayed. |  |
| 3 | Select Material | On the Stock / Requirements List: Initial Screen make the following entries and choose Continue.Material: FG0511Plant: 3310 | The Stock/Requirements List as of xxx hrs is displayed. |  |
| 4 | Review Stock / Requirements Situation for Components to be provided to the MRP area of the subcontractor | On the Stock/Requirements List as of xxx hrs check the stock transfer elements created during MRP run.For the plant MRP Area 3310 a material reservation has been created for material FG0511. Double click on the reservation for more details.In the Stock/Requirements List, change from the plant MRP area to the subcontractor MRP area, make the following entries and choose the button Refresh.MRP Area: 3310SUB051The MRP Run in previous step has now created Transport Reservations to the Subcontracting MRP Area 3310SUB051. |  |  |
| 5 | Review Intra-Plant View | To be able to better monitor planning situations where more than one MRP Area is involved, two additional tabs are provided for the Stock/Requirements List.To see the planning situation for all MRP areas in one plant, choose the tab Intra-Plant View. Click on the button Vendor on top of the Intra-Plant View list to see the vendor linked to the corresponding MRP area.The elements in the Intra-Plant View are basically sorted according to the planning date. Choose button Separate MRP Areas to see the MRP elements separated for each of the MRP Areas.Check the Stock for both MRP Areas, 3310 and 3310SUB051. |  |  |
| 6 | Check other Subcontracting Components (Optional) | If you want to check the other subcontracting components, repeat steps #3 to #5 for materials FG0512, PK0504 and PK0508. |  |  |

#### Transfer Components to the Subcontractor

Purpose

This process step shows how to transfer components to the subcontractor.

Prerequisite

Requirement planning is carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Inventory Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Subcontracting Cockpit (F2948). | The Subcontracting Cockpit Screen is displayed. |  |
| 3 | Search for Component or Assembly | Set values to some filters to search ComponentsSubcontractor: 33305001Plant: 3310Choose GO.Note If no components are displayed please check the filter for the ‘Shipping Date’. In SAP standard the filter is restricted from -15 days to +15 days. If the shipping date is outside this time frame the number of days has to be changed in the filter criterias. | The search results show the details with the respective filter Criteria. Following columns must contain relevant data:ComponentPlantSubcontractorStock Balance |  |
| 4 | Display Purchase Order Item for a component | Choose small Arrow next to Component to expand the details. | All purchase order with items number corresponding to the component must be displayed in Document Item column.. |  |
| 5 | Post Goods Issue | Choose all PO Items from your purchase order and then choose Post Goods Issue. | There will be navigation to the Post Goods Issue (MIGO_GI). |  |
| 6 | Enter Detail Data | Check the following entries:Component: <Component which was chosen>Movement Type: 541Plant: 3310Storage Location: 331A (for FGXXXX materials) or 331C (for PKXXXX materials)Pending Quantity: <Depending on component>Base Unit of Measure: PCPlease make sure the components have stock in the storage location. If not, please do initial stock for them.If the component is batch managed in the system search the batch numbers via the search help and choose the correct batch from the list.It's also possible to post goods issue towards reservation if there's any. |  |  |
| 7 | Item OK | Check if the processing status is valid. |  |  |
| 8 | Post | Select all the items and Post Goods Issue. | The system displays the message Document 49XXXXXXXX posted with X item(s). |  |

#### Batch Transfer Posting

Purpose

The batches delivered to the subcontractor are in the special stock of subcontracting stock. These batches must now be transferred to the delivery batch number.

Prerequisite

The goods issue for the delivery of the component batch has taken place.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Post Goods Movement Tile | Open Post Goods Movement (MIGO). | The Goods Movement screen displays. |  |
| 3 | Screen Settings | In the upper area, enter the following data and choose Enter.Trans./ Event: Transfer PostingReference Document: OtherMovement Type: 309Special Stock Indicator: O | Entries are made. |  |
| 4 | Enter Material Data | Choose the tab Transfer Posting, enter the following data and choose Enter.From Material:< batch managed component from previous step> e.g. FG0511Destination Material: <same value as in the field before>From Plant: 3310Destination Plant: 3310From Batch: <batch used in chapter before>Destination batch: ddmmyyyySupplier: 33305001Follow above steps for FG0512 material as well. | dd=day, mm=month, yyyy=yearUnder the field "Special stock“. |  |
| 5 | Enter Material Data | Enter the following data on the tab Quantity and choose Enter.Quantity: <Qty in Unit of Entry from previous step> | Entries are made. |  |
| 6 | Enter Organization Data | Enter the following data on the tab where and choose Enter.Movement type: 309 OPlant: 3310Item Ok: <select> | Entries are made. |  |
| 7 | Check | Check if the processing status is valid. |  |  |
| 8 | Post | Choose Post. | Material document 49XXXXX posted. |  |

#### Batch Traceability

Purpose

In this step you check which batches are transferred to the subcontracting batch number.

Prerequisite

A batch transfer posting has been executed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad using the Quality Technician. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Batch Information Cockpit (BMBC). | The Batch Information Cockpit screen displays. |  |
| 3 | Screen Settings | In the Material, enter the following data and choose Execute Selection.Material: Material of batch componentPlant: 3310 | Entries are recorded. |  |
| 4 | Selection Results | Look for the delivery batch choose Display Batch. | dd=day, mm=month, yyyy=yearDetails of the delivery batch appears in the right detail screen. |  |
| 5 | Menu Bar | In the menu bar expand Details and open Usage. | In the lower area you can see the top-down analysis that shows you which batches were included in the delivery batch. |  |

|  |
| --- |
| Note You can proceed in the same way by selecting the component batch instead of the delivery batch. In this case, select the "Bottom-up" function. |

#### Evaluate Stock/Requirements Situation

Purpose

This process step shows you how to display the stock/requirements situation for Make-to-Stock finished goods (FG0502) and the components relevant for delivery to the subcontractor (finished and packaging materials) in the stock/requirements list after delivery of components to the subcontractor.

Prerequisite

Requirement planning is carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Monitor Stock / Requirements List - Old Version (MD04). | The Monitor Stock / Requirements List: Initial Screen is displayed. |  |
| 3 | Select Material | On the Monitor Stock / Requirements List: Initial Screen make the following entries and choose Continue.Material: FG0511Plant: 3310 | The Stock/Requirements List as of xxx hrs is displayed. |  |
| 4 | Review Stock / Requirements Situation for Subcontracting Component | On the Stock/Requirements List as of xxx hrs choose tab Intra-Plant View and press button Separate MRP Areas.The stock where the goods issue has been booked for has been automatically moved from the plant MRP Area 3310 to the MRP Area 3310SUB051 from the subcontractor.You can check directly which materials are currently on subcontractor site. The stock has been removed from the plant MRP area and is not considered in the plant MRP run anymore but in the MRP run for the subcontracting MRP Area 3310SUB051.You can also review for the other subcontracting components FG0512, PK0504 and PK0508. | The detailed Stock / Requirements List is displayed. |  |

#### Create Inbound Delivery for Subcontracting Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create an inbound delivery for a subcontracting purchase order.

|  |
| --- |
| Note This step is only possible if you executed option 3 for purchase order creation earlier: [Option-3 Create Purchase Order manually with Inbound Delivery](#unique_22) |

Prerequisite

Subcontracting purchase order (Option 3 from purchase order creation alternatives) created and approved.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Receiving Specialist. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open App | Open Create Inbound Delivery (VL31N). | The Create Inbound Delivery screen is displayed. |  |
| 3 | Enter Purchase Order | In the field Purchase order enter the subcontracting purchase order and choose Continue.Purchase Order: <Purchase Order from previous step> | The Inbound Delivery Create: Overview screen is displayed. |  |
| 4 | Select the tab Stock Placement | On the tab Stock Placement, enter in the field Putaway Qty the quantity equal to the delivery quantity and choose Save. | Inbound Delivery XXX has been saved message is displayed. |  |

#### Goods Receipt for Subcontracting Purchase Order

##### Option 1: Receive Goods for Subcontracting Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post the goods receipt for the material against the subcontracting PO.

|  |
| --- |
| Note This step is only possible if you executed option 1 or 2 for purchase order creation earlier(see 4.2.1.1: Option 1: Convert Purchase Requisition to Purchase Order or 4.2.1.2: Create Purchase Oder manually with inbound delivery) |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Post Goods Movement Tile | Open Post Goods Movement (MIGO). | The Goods Receipt Purchase Order - <User name> screen is displayed (or the name of the last process step which was executed in this app). |  |
| 3 | Select Goods Receipt Purchase Order Screen | Enter your PO number or search your subcontracting purchase order. | The items of the selected Purchase Order are displayed. |  |
| 4 | Check Quantity | Check the quantity of the Purchase Order and correct it in the detail data register tab Quantity, if needed. |  |  |
| 5 | Mark Item OK | Mark item OK in detail data in register tab Quantity. |  |  |
| 6 | Check Item | Click on Check to check the line item. | Note An Error message Enter the date of production and information ‘Batch XXX created’ might appear in a pop-up. In that case make the necessary entries. |  |
| 7 | OK | Accept the messages by clicking ENTER. |  |  |
| 8 | Check Batch Data | In the detail data in register tab Batch the information from the procured batch number is displayed. Please check the data. |  |  |
| 9 | Expand the Line Item | Click on the expand icon next to the line 1 item and the components are displayed.Note The quantities are corrected due to the BOM. If the quantity is changed after the expansion the quantities are not automatically recalculated. | The system displays all components and the quantities. |  |
| 10 | Maintain Components | Enter the batch numbers for the components if they are batch managed. | Batches are maintained on detail data. |  |
| 11 | Post | Choose Post. | The system displays the message Material document 5000000XX 202X posted. |  |

##### Option 2: Receive Goods from Subcontracting Purchase Order with Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post the goods receipt for the material against an Inbound Delivery.

|  |
| --- |
| Note This step is only possible if you executed option 3 for purchase order creation earlier: [Create Purchase Order manually with Inbound Delivery](#unique_22). |

Prerequisite

Inbound Delivery was created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Receiving Specialist. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Change Inbound Delivery (VL32N). | The The Change inbound delivery Initial screen is displayed. |  |
| 3 | Enter Inbound Delivery | In the field Inbound delivery enter the Inbound Delivery number and choose Continue. | The item overview of the inbound delivery is displayed. |  |
| 4 | Select the item on the Item Overview | Select the item Item overview tab. Mark one line and choose Item Detail. | The item detailed List is displayed. |  |
| 5 | Enter Shelf life and Batch for Subcontracted Material | Select the Material tab, make the following entries:Shelf Life Expiration or Date of ManufactureBatch numberChoose Back. | The Shelf Life Expiration or Date of Manufacture will be determined depending what you have entered. |  |
| 6 | Enter Batch Number for Component | Select the item Item overview tab and press SC Components. The pop up Edit components appears.Enter for each component where it is required a batch number and choose Confirm. |  |  |
| 7 | Post Goods Receipt | When you are back on the Item Overview tab, choose Post Goods Receipt. | The system saves Inbound Delivery. |  |

#### Evaluate Stock/Requirements Situation

Purpose

This process step shows you how to display the stock/requirements situation for Make-to-Stock finished goods (FG0502) and the components relevant for delivery to the subcontractor (finished and packaging materials) in the stock/requirements list after Goods receipt of components to the subcontractor.

Prerequisite

Requirement planning is carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Monitor Stock / Requirements List - Old Version (MD04). | The Monitor Stock / Requirements List: Initial Screen is displayed. |  |
| 3 | Select Material | On the Monitor Stock / Requirements List: Initial Screen make the following entries and choose Continue.Material: FG0502Plant: 3310 | The Stock/Requirements List as of xxx hrs is displayed. |  |
| 4 | Review Stock / Requirements Situation for Subcontracting Material | On the Stock/Requirements List as of xxx hrs review the stock listed for material FG0502.The unrestricted stock has not been increased, yet. This is attributed to the fact that only free available Stock is visible in the Stock/Requirements list. The material FG0502 is subject to quality inspection during goods receipt inspection and hence posted into quality inspection stock first. A disposition relevant quality Inspection Lot with the amount of posted goods receipt has been created. After quality inspection and accepted usage decision the inspection lot disappears, and the quantity is available in the unrestricted stock. | The detailed stock / requirements list is displayed. |  |
| 5 | Review Stock / Requirements Situation for Subcontracting Component | On the Monitor Stock/Requirements List Screen make the following entries and choose Refresh.Material: FG0511Plant: 3310Choose tab Intra-Plant view and press button Separate MRP Areas. Review the stock in the subcontracting area 3310SUB051 The stock has been reduced for the amount the components that has been booked during goods receipt of subcontracting material.Repeat the review for material FG0512, PK0504 and PK0508. |  |  |

### Quality Inspection

Purpose

The material from subcontractor undergoes a quality inspection to ensure that it meets the predefined quality requirements. In this step, the quality technician records the inspection result for the required inspection characteristics. Afterwards, the quality engineer completes the inspection with a usage decision.

Prerequisite

The inspection is processed based on inspection lot. In this business process, the inspection lot has been created automatically upon goods receipt for the purchase order.

#### Display Material Stock Before Quality Inspection (Optional)

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

The goods receipt from purchase order was posted for the subcontracting material to quality inspection stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Inventory Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material screen displays. |  |
| 3 | Enter Material | Make the following entries and choose Enter:Material: FG0502 | Stock for the material and batch (from previous step) is displayed. |  |
| 4 | Check Stock Quantity | Check the Quality Inspection Stock under the plant 3310 and storage location 331A. | Quantity received is posted in quality stock. |  |
| 5 | Check Inspection Lots (Optional) | Choose Manage Stock on the bottom of the screen. Choose then Manage Inspection Lots on the bottom of the screen. | Inspection Lots for the selected material are displayed if you have further QM authorizations. |  |

#### Display Inspection Plan for Inspection Characteristics (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the inspection plan is related to the subcontracted material. The inspection plan defines all inspection characteristics used later in the quality inspection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Inspection Plan (QP03). | The Display Inspection Plan screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Continue.Material: FG0502Plant: 3310 |  |  |
| 4 | Select Entry Instruction | In the Inspection Plan Display: Task List Overview screen, select the row with GR Subcontracting Display and then choose Operations. | Only needed, if more than one inspection plan is assigned to the plan group. |  |
| 5 | Go to Inspection Characteristics Overview Screen | Select the operation 0010 and Choose either Inspection Characteristics or Menu > Inspection Characteristics . | The Display Inspection Plan: Characteristics Overview screen displays. |  |
| 6 | Review the Inspection Characteristics | There are two qualitative Master Inspection Characteristics:One is Visual Pack CheckOne is Label Check | You have now reviewed the inspection characteristics for which data has to be maintained within a later step.The sampling procedures and characteristics can be reviewed in detail. |  |

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

The inspection lot is used to record the results of the inspection operation. In this optional step, the references to the goods receipt and purchase order are verified as well as the sample size used for quality inspection reviewed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose GO.Plant: 3310Material: FG0502Inspection Lot Status: OutstandingInspection Lot Origin: Goods Receipt (01) | Alternatively, you can search for the Purch.Doc <purchase order ID> (from previous step).If purchase order is not displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, select Purchasing Document and choose Ok. Choose Go. |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot with column equals to the Purch.Doc <purchase order> (from previous steps). | The Purchase Order number assigned with Inspection Lot is displayed.If the Purchase Order column does not appear, please choose the button Settings. In the View Settings dialog box, select Purchasing Document and choose OK.Note down the inspection lot ____.Note down the batch number ____. |  |
| 5 | Check Inspection Lot | Under Origin, verify the referenced purchase order and material document. | The purchase order number and material document number from which the inspection lot originates are displayed. |  |
| 6 | Choose Operation (Optional) | In Result, choose operation GR Subcontracting. |  |  |
| 7 | Choose Characteristic (Optional) | Click Visual Pack Check in the Characteristics column. | A dialog box appears with the Characteristics Details. |  |
| 8 | Choose Characteristic (Optional) | Click Label Check in the Characteristics column. | A dialog box appears with the Characteristics Details. |  |

#### Record Inspection Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the quality technician performs the quality inspection and records the inspection result(s) for operation 0010 (GR Subcontracting). The result is recorded in the inspection lot according to the defined inspection parameters in the inspection plan.

Prerequisite

The inspection is processed based on inspection lot. In this scope item, the inspection lot is automatically created upon goods receipt for purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results - Hierarchical Worklist (QE51N). | The Results Recording screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Execute.Plant: 3310Insp. Lot Origin： 01(Goods Receipt)Material: FG0502Batch: <Batch ID> from previous stepLot Created: <choose one week ago until today> | The Results Recording Worklist Screen displays.Caution In Cloud system, Dynamic Selection (e.g. for Purchase order) is not offered.Alternatively you can search for the <Batch ID> or <Inspection Lot ID> from previous step. |  |
| 4 | Select the Corresponding Inspection Lot | On the left pane, expand the corresponding inspection lot which you want to record a result. | If a dialogue appears asking to Save, choose Cancel. |  |
| 5 | Choose the Characteristic | Select the characteristic which is under the activity 0010 GR Subcontracting Work Center Quality Check Point with a click (or use icon Select a Characteristic). | When the characteristic is selected Record Results for XXXX TEST : Classes for Characteristic page opens, where the class size can be recorded. |  |
| 6 | Enter Inspection Result for Characteristic | Depending on the inspection result, classify the no. of inspected displays and then confirm with Save.Positive ResultVisual Pack Check: <enter no. of displays in class size> of class NOKLabel Check: <enter no. of displays in class size> of class OKNegative ResultVisual Pack Check: <enter no. of displays in class size> of class OKLabel Pack Check: <enter no. of displays in class size> of class NOK | For both qualitative characteristics a 100% check is performed, assigning the no. of displays to the corresponding class OK or NOK.Auto Valuation is done by the system.The status is set to 5 Processing is completed. |  |

#### Display Quality Engineer Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the inspection lot depending on the inspection result. As an optional entry point for making this usage decision, you can use the app Quality Engineer Overview (F2360). Furthermore, the Quality Engineer Overview (F2360) app displays inspection lots without an inspection plan (e.g. if automatic assignment of an inspection plan is not set up in the material master or if automatic assignment failed), inspection lots without usage decision, inspection lots ready for usage decision.

If negative inspection results are recorded, you can check the defect details in app Manage Defects (F2649) directed from the app Quality Engineer Overview (F2360) via the cards Inspection Lots with Defects, Top Defective Materials, or Top Defects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Quality Engineer Overview (F2360). | The Quality Engineer Overview screen displays. |  |
| 3 | In Card: Inspection Lots without Inspection Plan choose one entry (Optional) |  | To assign missing data and ensure automatic inspection plan determination for further usage. |  |
| 4a | In Card: Select Inspection Lots Without Usage Decision (Optional) | Choose card Inspection Lots Without Usage Decision. | You can process further as described in Make Usage Decision Chapter. |  |
| 4b | Select the Corresponding Inspection Lot you have created before (Optional) | In the inspection lot list, select the inspection lot. | The Manage Usage Decisions screen displays. Alternative Entry to Chapter Manage Usage Decision. |  |
| 4c | Select one of the Inspection Lot by Results Recording Status (Optional) | Select one of the Inspection Lot by Results Recording Status (Optional). | Alternative Entry to Chapter Manage Usage Decision. |  |
| 5 | Select Card Inspection Lots Ready for Usage Decision (Optional) |  | All inspection lots with positive results get collectively an accepted usage decision (e.g. defaulted by A1) when pressing button Make Quick Usage Decision. |  |
| 6 | In Card: Inspection Lots with Defects (Optional) | (In case negative inspection results have been recorded and auto-defect recording has been defined) Select one of the inspection lot origins, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 7 | In Card: Top Defective Materials (Optional) | (In case failed inspection results have been recorded and auto-defect recording has been defined) Select one of the materials inspected, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |
| 8 | In Card: Top Defects (Optional) | (In case negative inspection results have been recorded and auto-defect recording has been defined) Select one of the defect codes recorded, then you will be directed to app Manage Defects (F2649) automatically. Choose the relevant defect ID to check the details of the defect. | The defect details are displayed. |  |

#### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Inspection is done, and the Inspection result is recorded. You must decide whether or not to accept the material coming back from subcontractor depending on the Inspection result. If you do not want to use the Quality Engineer Overview, you can open the Manage Usage Decisions app directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Usage Decisions (F2345). | The Manage Usage Decisions screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Purch.Doc: <Purchase Order> (from Previous steps). | If Purchase Document is not displayed in the filters, choose Adapt Filters. On the dialog box Adapt Filters, Select Purchasing Document and choose OK. Choose GO.Alternatively, you can search for the <batch ID> or <Inspection lot ID> from previous step.If batch is not displayed in the Filters, choose Adapt Filters. In the dialog box Adapt Filters, select Batch and choose Ok, Choose Go. |  |
| 4 | Select Corresponding Inspection Lot | In the Inspection lot list, select the corresponding Inspection lot. | The Inspection Lot screen displays. |  |
| 5 | Display Defects | Scroll down to the Defects area. Check the details of Defects. | Only available when you have recorded a negative result. For a visual pack check rejection, there will be a packaging defect, for label check rejection, there will be a labeling defect displayed. |  |
| 6 | Choose Edit and Add Document | Choose Edit In the Document section Choose Upload, select the path and add the document. | For example, to upload pictures to visualize the defect. |  |
| 7 | Enter UD code | Depending on the inspection result, select one of the following options and then confirm with Save.Positive ResultUD code:A1 (Accepted–unrestricted stock)A2 (Accepted-unrestricted –minor quality)A3 (Accepted-unrestricted-sample consumption)Negative Result:UD code: R1 (Rejected–blocked stock)Choose Yes if dialog Confirmation Prompt appears. | Note The corresponding Stock Posting is processed automatically in the background for the complete quantity for Usage Decision codes A1, A2, R1.Note Please do not use R210 (Return to Supplier w/o Delivery) and R220 (Return to Supplier with Delivery) for this scenario, because in case of deviations, the subcontracted material would be reworked in the current plant but not sent back to subcontractor. |  |
| 8 | Modify Stock Posting (Optional) | In the Inspection Lot Stock section, enter the quantities to be posted in different stock posting proposals. |  |  |
| 9 | Save Usage Decision | Choose Save. | The usage decision is made for the material from subcontractor. The system automatically triggers the material movements associated with the usage decision code. |  |

#### Display Material Stock after Usage Decision (Optional)

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
- Negative Result ‘Return to Supplier w/o Delivery’ (R210): Do not use for this scenario
- Negative Result ‘Return to Supplier with Delivery’ (R220): Do not use for this scenario

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076) | The Stock – Single Material screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and press Enter.Material: FG0502 |  |  |
| 4 | Check Stock Quantity | Check the changed quantities of the Quality Inspection Stock, Unrestricted Use Stock (in case of positive usage decision) or Blocked storage location 331A. | The stock quantities for material FG0502 are updated based on the quality inspection and respective usage decision of the previous steps. |  |

### Invoicing

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
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Accounts Payable Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Create Supplier Invoice (F0859). | The Create Supplier Invoice screen displays. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Reference: <xxx> (reference invoice number from invoicing party)Gross Invoice Amount : <XXX>Invoice Date: <Today>Currency: AEDPosting Date: <Today>Invoicing Party: 33305001 | The Create Supplier Invoices screen displays. |  |
| 4 | Enter Purchase Order References | In Purchase Document References make the following entries (use a PO you created previously) and choose Enter.Make the following entries (use a PO you created previously).Reference Document Category: Purchase Order/ Scheduling AgreementPurchase Order: <PO number> | The Purchase Order References screen displays. |  |
| 5 | Select Purchase Order Items | Check the selection of the Purchase Order Items.Confirm the warning messages. | All items of the selected Purchase Order are added to the Purchase Order Item table.You should see material items which refer to the entered purchase order document. |  |
| 6 | Check the Invoice Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Purchase Order Item's table displays. |  |
| 7 | Check Tax Date | In case the time dependent tax is activated, in the section Tax, the Tax Date indicates the tax calculation date according to the tax rates settings in the prerequisites.Make the following entries.Tax Reporting Date: <Today>Tax Date: <Today>Note The Tax Date is the key date for calculating tax, please maintain it carefully according to your financial business requirements. |  |  |
| 8 | Check Tax Code | In the section Tax check if there is tax code information. | In the Tax tab, you should see the same tax codes as in the items.If there is no tax, specify the tax code <Input Tax Code>. |  |
| 9 | Check the Balance | Calculate the tax amount from the item amount multiplied by the tax value. | The balance should be zero (or within the defined tolerance). |  |
| 10 | Simulate Supplier Invoice and Check Messages | Choose Simulate.If there are no differences (or if the value is within the defined tolerance), a new screen Simulation appears. You can check the simulation results in Simulation Overview and Simulation Details area.The Supplier Invoice is complete to post. Check the Gross Invoice Amount against the items plus tax amount (if tax code is, <Input Tax Code> you do not have any tax amount). | The supplier invoice is complete to post. |  |
| 11 | Post Invoice | Choose Post. | The invoice is posted. |  |

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
| 3 | Enter General Data | Make the following entries:Invoicing Party: 33305001Company Code: 3310Choose Go. |  |  |
| 4 | Check invoice | Check Display to check the invoice. |  |  |

### Batch Traceability

#### Batch Information Cockpit - Top-Down and Bottom-Up Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this functionality you can identify which batches are delivered to which customer and which raw material batches are used for the production of which finished product. You can adapt the selection in the Batch Information Cockpit to customer-specific requirements by creating user-specific groups. You can get additional information by using subsequent actions.

In this case the evaluation is limited to the production process. As soon as you have purchased the raw materials and/or delivered the finished good FG0502 to a customer the evaluation is automatically enhanced with these information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto the SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad using the Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Batch Information Cockpit (BMBC). | The Batch Information Cockpit screen displays. |  |
| 3 | Select batches | On the Batch Information Cockpit screen, make the following entries.Go to Material tab.Material : FG0502Plant: 3310Choose Execute Selection. | One or multiple batches are displayed in the left screen area Selection Result for Batches. The standard sorting is done per material number. |  |
| 4 | Expand selection | In the section Selection Result for Batches select Checkbox for FG0502 and then choose Expand subtree or Expand node. | The selection result is analyzed and a batch for further investigation is identified. |  |
| 5 | Start Analysis | Right click on one selected batch and choose either Usage (Top-Down) or Usage (Bottom-up). | The batch where used list displays. |  |
| 6 | Analyze the batch where used list | The usage of the batch can be analyzed and the specific documents (such as batch master record, production orders and sales order) can be accessed via double click. |  |  |
| 7 | Analyze assigned Inspection lots | Mark one line in the Details (Usage) table and choose button Inspection Lots to review inspection lots assigned to the selected element. |  |  |
| 8 | Analyze Batch Master | Choose Details in the header area and select Batch Master. | The batch master screen displays. |  |
| 9 | Analyze material document | Choose Details again and choose Usage.Select one document and choose Documents. | The usage displays again and after selecting documents the respective material document display. |  |
| 10 | Go to the material document | Select the material document in the pop up and choose Choose (F2).To display the material document, you need further authorizations that are granted by your company, for example, SAP_BR_INVENTORY_MANAGER. | The material document displays.Note Your user has to have the appropriate authorizations. |  |

## Appendix

### Process Integration

N/A

### Preceding Processes

The following processes and conditions can precede this process.

| Process | Business Condition |
| --- | --- |
| 5HK - Quality Management in Discrete Manufacturing - Consumer Products | You can execute this scope item before executing 5W4. Stock for the Components handed over to the Subcontractor can be produced if you execute the scope item 5HK until the section “Production order Conversion for Finished Material FG0502" In that case you can skip the process steps "Create Planned Independent Requirements" and "Materials Requirements Planning at Plant Level" of this test script. |
| 5OI - Production Capacity Evaluation and Leveling - Consumer Products | You can execute this scope item before executing 5W4. In that case you can skip the process steps "Create Planned Independent Requirements" and "Materials Requirements Planning at Plant Level" of this test script. |
| 5W3 - Procurement with and without QM - Consumer Products | You can execute this scope item to procure components relevant for the subcontracting process. |

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 5HL - Sell from Stock - Consumer Products | You can sell the subcontracting material to customers using this scope item. |

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
> Flagged while digesting this document, not verified: Purchase order approval threshold is worded inconsistently: 'higher than 500.00 AED' in the note versus 'net value of 500 AED or more' in the expected result of the approval step.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/test-script-scheduling-agreement-for-subcontracting-procurement-2nx-ae]]
- related-to :: [[10-procurement/test-script-subcontracting-bmy-ae-sap-s-4hana-cloud-public-edition-129]]
- see-also :: [[08-sales-order-management/customer-returns-management-consumer-products-61v-ae-test-script-sap-s]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5W4_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 114,622 chars in the whole document
