---
id: 10-procurement/test-script-scheduling-agreement-for-subcontracting-procurement-2nx-ae
title: "Test Script: Scheduling Agreement for Subcontracting Procurement (2NX_AE) - SAP S/4HANA Cloud Public Edition (2NX_S4CLD2608_BPD_EN_AE)"
description: "S/4HANA Cloud 2608 (AE) test script, scope item 2NX: subcontracting scheduling agreements, with and without serial numbers, from creation to supplier invoice."
cluster: 10-procurement
tags: [kb/procurement, topic/scheduling-agreements, topic/subcontracting-procurement]
aliases: [2NX_S4CLD2608_BPD_EN_AE]
keywords: [Purchase Scheduling Agreements, scheduling agreement, subcontracting procurement, test scripts, serial number management, delivery schedule, purchasing info record, outbound delivery, goods receipt, supplier invoice]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2NX_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-837
topic: 10-procurement/scheduling-agreements
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Scheduling Agreement for Subcontracting Procurement (2NX_AE) - SAP S/4HANA Cloud Public Edition (2NX_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2NX_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Purchase Scheduling Agreements** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Scheduling Agreement for Subcontracting Procurement (2NX_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232849569)

[2 Prerequisites 4](#_Toc232849570)

[2.1 System Access 4](#_Toc232849571)

[2.2 Roles 4](#_Toc232849572)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232849573)

[2.4 Business Conditions 7](#_Toc232849574)

[2.5 Preliminary Steps 8](#_Toc232849575)

[2.5.1 Create Subcontracting Info Record 8](#_Toc232849576)

[2.5.1.1 Create Subcontracting Info Record for Non-Serial Number Managed Material 8](#_Toc232849577)

[2.5.1.2 Create Subcontracting Info Record for Serial Number Managed Material 10](#_Toc232849578)

[2.5.2 Initialize Material Stock (Optional) 12](#_Toc232849579)

[2.5.2.1 Initialize Material Stock for Non-Serial Number Managed Material 12](#_Toc232849580)

[2.5.2.2 Initialize Material Stock for Serial Number Managed Material 13](#_Toc232849581)

[2.5.3 Activate Flexible Workflow for Scheduling Agreement Approval (Optional) 14](#_Toc232849582)

[2.5.4 Configure Flexible Workflow for Scheduling Agreement (Optional) 15](#_Toc232849583)

[2.5.5 Edit User-Specific Parameters for Supplier Invoices (Optional) 16](#_Toc232849584)

[2.5.6 Assign Shipping Points 17](#_Toc232849585)

[3 Overview Table 19](#_Toc232849586)

[4 Test Procedures 21](#_Toc232849587)

[4.1 Part 1: Scheduling Agreement for Subcontracting without Serial Number Management 21](#_Toc232849588)

[4.1.1 Create Scheduling Agreement – Subcontracting 21](#_Toc232849589)

[4.1.1.1 Create Scheduling Agreement – Direct / without Reference (Option 1) 21](#_Toc232849590)

[4.1.1.2 Create Scheduling Agreement with Purchase Requisition Reference (Option 2) 23](#_Toc232849591)

[4.1.1.2.1 Create Purchase Requisition 23](#_Toc232849592)

[4.1.1.2.2 Convert Purchase Requisition to Scheduling Agreement – Subcontracting 24](#_Toc232849593)

[4.1.2 Approve Scheduling Agreement (Optional) 26](#_Toc232849594)

[4.1.3 Generate Delivery Schedule from MRP run (Optional) 27](#_Toc232849595)

[4.1.3.1 Create Planned Independent Requirements 27](#_Toc232849596)

[4.1.3.2 Schedule MRP Run 28](#_Toc232849597)

[4.1.3.3 Evaluate Stock Requirement Situation 30](#_Toc232849598)

[4.1.4 Maintain Delivery Schedule 31](#_Toc232849599)

[4.1.5 Print Scheduling Agreement 33](#_Toc232849600)

[4.1.6 Monitor Subcontracting Documents (Optional) 34](#_Toc232849601)

[4.1.7 Create Outbound Delivery 35](#_Toc232849602)

[4.1.8 Pick and Post Goods Issue 36](#_Toc232849603)

[4.1.9 Post Goods Receipt 37](#_Toc232849604)

[4.1.10 Create Supplier Invoice 38](#_Toc232849605)

[4.2 Part 2: Scheduling Agreement for Subcontracting with Serial Number Management 40](#_Toc232849606)

[4.2.1 Create Scheduling Agreement – Subcontracting 40](#_Toc232849607)

[4.2.2 Approve Scheduling Agreement (Optional) 42](#_Toc232849608)

[4.2.3 Maintain Delivery Schedule 43](#_Toc232849609)

[4.2.4 Create Outbound Delivery 44](#_Toc232849610)

[4.2.5 Pick and Post Goods Issue 46](#_Toc232849611)

[4.2.6 Create Inbound Delivery 47](#_Toc232849612)

[4.2.7 Post Goods Receipt for Inbound Delivery 48](#_Toc232849613)

[4.2.8 Create Supplier Invoice 49](#_Toc232849614)

[5 Appendix 52](#_Toc232849615)

[5.1 Succeeding Process 52](#_Toc232849616)

## Purpose

Overview

The use of scheduling agreements can shorten processing times and reduce the amount of paperwork you are faced with. One delivery schedule can replace many discrete purchase orders or contract release orders.

A purchase requisition of type RV-Outline Agreement Requisition can be created with subcontracting line items (Item Category – L Subcontracting) manually by a requestor. The purchase requisition can be converted into a scheduling agreement. The scheduling agreement is subject to approval based on predefined parameters before you generate delivery schedule or schedule lines (manually or via MRP run) and communicate them to the subcontractor. The outbound delivery is created, and the goods are picked and shipped to the subcontractor. With the supply of the finished material, the goods receipt is created. The invoicing process is then triggered.

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
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Material Planner - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC | Material Planning - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | SG26 | SEMI26,PD,Subcontracting | See sections Business Conditions and Preliminary StepsFor the specific plant, set the Special Procurement Key to “30” for Subcontracting in MRP View 2. |
| Material | RM13 | RAW13,PD,Subcontracting | Material provided to subcontractor |
| Material | RM14 | RAW14,PD,Subcontracting | Material provided to subcontractor |
| Material | SG27 | SEMI27,PD,Subcontracting | Enabled with serial number management |
| Material | RM33 | RAW33,PD,Subcontracting | Material provided to subcontractor, enabled with serial number management |
| Material | RM34 | RAW34,PD,Subcontracting | Material provided to subcontractor, enabled with serial number management |
| Material | RM14 |  |  |
| Material | RM14 |  |  |
| Material | RM14 |  |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |
| Supplier | 33300007 | Domestic AE Subcontractor A | Note If you want to send form print outs via e-mail in stead of using the print functionality make sure that you have maintained a valid e-mail address in the supplier master data. |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchase group | 001 | Group 001 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNE | Create Supplier Master - MDS |
| BHD | Create Purchasing Info Record - MDS |
| BF6 | Create Scheduling Agreement - MDS |

### Business Conditions

Before this test script can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ – Create New Open MM Posting Period - MDS | Complete all relevant steps. |
| BJ5 – Make-to-Stock Production – Discrete Manufacturing | To run through this test script, the materials must be available in stock. If you use finished goods (FERT) you can either:Run through the BJ5 Make-to-Stock Production – Discrete Manufacturing process (for material FG126) orCreate stock using transaction MIGO(for more information, see Preliminary Steps). |

### Preliminary Steps

#### Create Subcontracting Info Record

##### Create Subcontracting Info Record for Non-Serial Number Managed Material

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
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record screen is displayed. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: SubcontractingPurchasing Organization: 3310Supplier: 33300007Material: SG26Plant: 3310Purchasing Group: 001 | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: TodayAvailable To: 12/31/9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: EXWNote Incoterms and their corresponding versions are grouped in the F4 value help. Selecting an incoterm automatically populates its associated version, which can be subsequently modified or removed if needed.Incoterm Location 1: VENDOR | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: 10Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10.0Tax Code: <Input Tax Code>Order Unit: PCStandard Order Quantity: 100Goods-Receipt-Based Invoice Verification: X | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To: 12/31/9999Amount: 0.59Pricing Unit: 1Currency: AEDChoose Apply. | Condition Data is added. |  |
| 9 | Enter Reference Data (optional) | You can enter reference data. | Reference data is added. |  |
| 10 | Save your data | Choose Create. | The purchasing info record is saved. |  |

Result

The subcontracting info record is created.

##### Create Subcontracting Info Record for Serial Number Managed Material

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
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record screen is displayed. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: SubcontractingPurchasing Organization: 3310Supplier: 33300007Material: SG27Plant: 3310Purchasing Group: 001 | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: TodayAvailable To: 12/31/9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: EXWNote Incoterms and their corresponding versions are grouped in the F4 value help. Selecting an incoterm automatically populates its associated version, which can be subsequently modified or removed if needed.Incoterm Location 1: VENDOR | Purchasing data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: 10Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10.0Tax Code: <Input Tax Code>Order Unit: PCStandard Order Quantity: 100Goods-Receipt-Based Invoice Verification: XConfirmation Control: 0004 Inbound Delivery | Delivery and quantity data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To: 12/31/9999Amount: 0.59Pricing Unit: 1Currency: AEDChoose Apply. | Condition data is added. |  |
| 9 | Enter Reference Data (Optional) | You can enter reference data. | Reference data is added. |  |
| 10 | Save Your Data | Choose Create. | The purchasing info record is saved. |  |

Result

The subcontracting info record is created.

#### Initialize Material Stock (Optional)

##### Initialize Material Stock for Non-Serial Number Managed Material

Purpose

In a real business case, the materials are usually purchased from external suppliers. In this case, the process is covered by the standard purchasing or subcontracting processes. For the purpose of this test, we post initial stock directly to the storage locations in case there is no enough stock (Unrestricted Use).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as an Inventory Manager. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen is displayed. |  |
| 3 | Enter Material | Make the following entries and choose Enter :Material: For example, RM13 and RM14Plant: For example, 3310, Plant 1 AE | The stock overview for the material is displayed. |  |
| 4 | Select Stock | Select the icon next to the stock to add initial stock. For example:Storage Location:331C (for RMxx materials)Unrestricted Use Stock | A dialog box appears. The Storage Location, Stock Type, and Current Quantity fields are displayed according to your entries in previous steps. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Document date: TodayPosting date: TodayStock Change: Initial EntryQuantity: Enter a quantity | The system displays the message 1 document has been created: Material Document XXXXXXXXXX/XXXX. |  |

##### Initialize Material Stock for Serial Number Managed Material

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Receipt Other screen is displayed.Note This screen will display only if this is your last transaction. The user should select field Reference Document for MIGO Transaction Other. |  |
| 3 | Input Movement Type | Make the following entries and choose Enter :Business Transaction: Goods ReceiptBusiness Transaction: OtherMovement Type: 561 - receipt per initial entry of stock balances into unreuse |  |  |
| 4 | Maintain Material | On the Goods Receipt Other screen, navigate to Material tab, make the following entry and choose Enter:Material (Original): RM33/RM34 |  |  |
| 5 | Maintain Quality | On the Goods Receipt Other screen, navigate to Quantity tab, make the following entries and choose Enter:Qty in Unit of Entry: <Qty in UOM>Unit of Entry: PC |  |  |
| 6 | Maintain Location | On the Goods Receipt Other screen, navigate to the Where tab, make the following entries and choose Enter:Plant: 3310Storage Location: 331C |  |  |
| 7 | Maintain Serial Number | On the Goods Receipt Other screen, navigate to the Serial Number tab, enter your serial number, or click Auto-Create Serial Numbers. |  |  |
| 8 | Save Your Entries | Click Item OK and Post. |  |  |

#### Activate Flexible Workflow for Scheduling Agreement Approval (Optional)

Purpose

In this procedure, you activate flexible workflow for scheduling agreement approval.

If you want to use the flexible workflow to manually approve the scheduling agreement , you have to process the steps: Activate Flexible Workflow for Scheduling Agreement Approval and Configure Flexible Workflow for Scheduling Agreement .

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution screen, search item Activate Flexible Workflow for Purchase Scheduling Agreements. then click the line Scheduling Agreement Processing.On the Configure Your Solution – Scheduling Agreement Processing screen, In Configuration steps area, choose the Configure button for item Activate Flexible Workflow for Purchase Scheduling Agreements. | The Document Types Scheduling Agreement Change screen is displayed. |  |
| 5 | Activate Flexible Workflow for SA(Scheduling Agreement) Approval | Make the following entries and choose Save:Document Type Scenario based workflowLP XLPA XNote You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue. | The scenario based workflow is active for scheduling agreements with document type: LP and LPA. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Configuration app and search for the following activity: Activate Flexible Workflow for Purchase Scheduling Agreements.Choose Open Documentation for the line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Document Types Scheduling Agreement Change screen displays. |  |
| 3 | Activate Flexible Workflow for SA(Scheduling Agreement) Approval | Make the following entries and choose Save:Document Type Scenario based workflowLP XLPA XNote You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue. | The scenario based workflow is active for scheduling agreement s with document type: LP and LPA. |  |

#### Configure Flexible Workflow for Scheduling Agreement (Optional)

Purpose

In this procedure, you configure your release conditions for Scheduling Agreement Approval.

When you start to process this step, please make sure that the flexible workflow for purchase document type LP has been activated in your system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Manage Workflow for Scheduling Agreement | Open Manage Workflows for Purchase Scheduling Agreements (F3044). | The Manage Workflows screen is displayed. |  |
| 3 | Create Manage Workflow | Choose Create and make following entries:Name: Test Workflow for Scheduling AgreementIn the Start Conditions area choose Purchasing Group of scheduling agreement is with value: 001Choose Create Alternative Preconditions and make the following entry:Choose Document type of Scheduling Agreement is with description Scheduling Agreement from dropdown list.In Step area choose Createand make following entries:Step Type: Release Scheduling AgreementRECIPIENTSUser: Select User with Purchasing_manager from F4 help.Step to be completed by: One of the recipientsChoose Create.Choose Save. | The Workflow for Scheduling Agreement is configured. |  |
| 4 | Activate Workflow Item | Select the just created Workflow Item and choose Activate. | The Workflow Item is activated. |  |

|  |
| --- |
| Note Please make sure default workflow automatic release of scheduling agreement has been activated. |

#### Edit User-Specific Parameters for Supplier Invoices (Optional)

Purpose

In this procedure, you will edit User-Specific parameters for supplier invoices.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Choose Edit Supplier Invoice Settings (F3813). | The Edit Supplier Invoice Settings screen is displayed. |  |
| 3 | Set parameter | Check parameter Display Journal Entry: XNote If parameter is checked, the system message contains invoice and journal entry number when invoice is created.If parameter is unchecked, the system message contains invoice number only when invoice is created.When this parameter is changed, it will be effective immediately for the APP Create Supplier Invoice. However, for the APP Create Supplier Invoice - Advanced, user needs to logout and login again to make it effective. | Change has been saved successfully. |  |

Result

Parameter Display Journal Entry has been set successfully.

#### Assign Shipping Points

Purpose

This chapter instructs you on how to assign shipping points.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Your Solution (F1241), choose Configure Your Solution and search for Assign Shipping Points.Choose Assign Shipping Points. | The Shipping Point and Goods Receiving Point Determination screen displays. |  |
| 3 | Maintain Shipping Points | On the Assign Shipping Points: Change screen, choose New Entries and make the following entries:Shipping Condition: 01Loading Group: 0001Plant: 3310Proposed Shipping Point: 3310Choose Save. | The shipping point is maintained. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Activity | Go to the Configuration app and search for the following activity: Assign Shipping Points.Choose the configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Shipping Points: Change screen displays. |  |
| 3 | Maintain Shipping Points | On the Assign Shipping Points: Change screen, choose New Entries and make the following entries:Shipping Condition: 01Loading Group: 0001Plant: 3310Proposed Shipping Point: 3310Choose Save. | The shipping point is maintained. |  |

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 1: Scheduling Agreement for Subcontracting Procurement without Serial Number Management

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Part 1: Scheduling Agreement for Subcontracting without Serial Number Management |  |  |  |
| [Create Scheduling Agreement – Direct / without Reference (Option 1)](#unique_16) [page ] 21 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | A Schedule Agreement is created. |
| [Create Scheduling Agreement with Purchase Requisition Reference (Option 2)](#unique_17) [page ] 23 |  |  |  |
| [Create Purchase Requisition](#unique_18) [page ] 23 | Purchaser | Create Purchase Requisition - Advanced (ME51N) |  |
| [Convert Purchase Requisition to Scheduling Agreement – Subcontracting](#unique_19) [page ] 24 | Purchaser | Create Scheduling Agreement (ME31L) |  |
| [Create Purchase Requisition](#unique_18) [page ] 23 | Purchaser | Create Purchase Requisition - Advanced (ME51N) | A Purchase Requisition is created. |
| [Convert Purchase Requisition to Scheduling Agreement – Subcontracting](#unique_19) [page ] 24 | Purchaser | Create Scheduling Agreement (ME31L) | A Schedule Agreement is created. |
| [Approve Scheduling Agreement (Optional)](#unique_20) [page ] 26 | Purchasing Manager | My Inbox - All Items (F0862) | Schedule Agreements are changed. |
| Generate Delivery Schedule from MRP run (Optional) |  |  | Material delivery schedule lines are displayed. |
| [Create Planned Independent Requirements](#unique_21) [page ] 27 | Production Planner | Maintain PIRs (F3445) |  |
| [Schedule MRP Run](#unique_22) [page ] 28 | Production Planner | Schedule MRP Runs (F1339) |  |
| [Evaluate Stock Requirement Situation](#unique_23) [page ] 30 | Material Planner - External Procurement | Manage Material Coverage - New Version (F0251A) |  |
| [Maintain Delivery Schedule](#unique_24) [page ] 31 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | A Delivery Schedule is created. |
| [Print Scheduling Agreement](#unique_25) [page ] 33 | Production Planner | Manage Purchase Scheduling Agreements (F2179) | Scheduling Agreement output triggered / PDF form for scheduling agreement is displayed. |
| [Monitor Subcontracting Documents (Optional)](#unique_26) [page ] 34 | Purchaser | Monitor Subcontracting Documents (F3095) | Subcontracting documents with next delivery date and quantity are displayed |
| [Create Outbound Delivery](#unique_27) [page ] 35 | Inventory Manager | Subcontracting Cockpit (F2948) | Outbound Delivery is created. |
| [Pick and Post Goods Issue](#unique_28) [page ] 36 | Shipping Specialist | Pick Outbound Delivery (F0868) | Goods Issue is posted against the scheduling agreement. |
| [Post Goods Receipt](#unique_29) [page ] 37 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Goods receipt is posted against the scheduling agreement. |
| [Create Supplier Invoice](#unique_30) [page ] 38 | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) | The Supplier Invoice is posted. |

Part 2: Scheduling Agreement for Subcontracting Procurement with Serial Number Management

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Scheduling Agreement – Subcontracting](#unique_31) [page ] 40 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | A schedule agreement is created. |
| [Approve Scheduling Agreement (Optional)](#unique_32) [page ] 42 | Purchasing Manager | My Inbox - All Items (F0862) | Schedule agreements are changed. |
| [Maintain Delivery Schedule](#unique_33) [page ] 43 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | A delivery schedule is created. |
| [Create Outbound Delivery](#unique_34) [page ] 44 | Inventory Manager | Subcontracting Cockpit (F2948) | The outbound delivery is created. |
| [Pick and Post Goods Issue](#unique_35) [page ] 46 | Shipping Specialist | Pick Outbound Delivery (F0868) | The goods issue is posted against the scheduling agreement. |
| [Create Inbound Delivery](#unique_36) [page ] 47 | Receiving Specialist | Create Inbound Delivery (VL31N) | The inbound delivery is created. |
| [Post Goods Receipt for Inbound Delivery](#unique_37) [page ] 48 | Receiving Specialist | Change Inbound Delivery (VL32N) | The goods receipt is posted against the scheduling agreement. |
| [Create Supplier Invoice](#unique_38) [page ] 49 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | The supplier invoice is posted. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Part 1: Scheduling Agreement for Subcontracting without Serial Number Management

#### Create Scheduling Agreement – Subcontracting

##### Create Scheduling Agreement – Direct / without Reference (Option 1)

Purpose

This activity is used to create scheduling agreement for material/supplier combination, for example, material SG26 and supplier 33300007, directly or without reference to any preceding purchasing document like purchase requisition, if it has not been maintained yet.

If scheduling agreement is already present in system, you can skip this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Purchase Scheduling Agreements (F2179). | The Manage Scheduling Agreements list page is displayed. |  |
| 3 | Create Scheduling Agreement | Select Create to create a new scheduling agreement | The New Scheduling Agreement header view is displayed. |  |
| 4 | Enter Header Data | Create a new scheduling agreement with the following data:Agreement Type: Scheduling Agreement(LP)Supplier:33300007Validity Start: Default TodayValidity End: MM/DD/YYYY e.g.today + 720 daysPurchasing Group: 001Purchasing Organization: 3310Company Code: 3310Target Value: 2000 AED |  |  |
| 5 | Add Items to Scheduling Agreement | From the New Purchase Scheduling Agreement view, choose the Items facets and select Create. | The New Scheduling Agreement Item view is displayed. |  |
| 6 | Enter Item data | On the Items facets view, make the following entries:Item Category: L (Subcontracting)Plant: 3310Storage Location:331BMaterial: SG26Net Order Price: Default Value from Info recordTarget Quantity:100Tax Code: V1 (Default Value from Info Record)Tax Date: Default TodayNote Field Tax Date is only available for countries/regions whose Time-Dependent Taxes (TDT) is enabled.Note If the RITA is activated and tax registration countries is maintained for company code in Finance SSCUI 103464/Configuration Activity (Activate RITA and maintain tax registration countries), then the tax country can be taken, or you can also choose different tax country value from the list.Choose Apply at the bottom of the view. |  |  |
| 7 | Save | Return to the New Purchase Scheduling Agreement view and choose Create at the bottom of the view.Make a note of the scheduling agreement number. | A scheduling agreement is created. |  |

##### Create Scheduling Agreement with Purchase Requisition Reference (Option 2)

###### Create Purchase Requisition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create Purchase Requisition of document type ‘RV’- Outline Agreement Requisition with subcontracting line items with item category ‘L- Subcontracting’.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Create Purchase Requisition -Advanced | Open Create Purchase Requisition - Advanced (ME51N). | Create Purchaser Requisition screen is displayed. |  |
| 3 | Select Requisition Document Type | Choose Document type RV Outline Agrmt. Reqn. from drop-down list | The Item Overview screen is displayed. |  |
| 4 | Enter Subcontracting Material line item | On the Create Purchase Requisition screen, make the following entries in the Item Overview area:Item Category – LMaterial – SG26Quantity – Desired Quantity or 100Plant – 3310Storage Location – 331B | System defaults the description and other entry aids. |  |
| 5 | Save | Choose Save at the bottom of the view.Make a note of the Purchase Requisition number. | A Purchase Requisition is created. |  |

###### Convert Purchase Requisition to Scheduling Agreement – Subcontracting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you convert purchase requisition to a scheduling agreement. If the document type of scheduling agreement is LP and the purchase group is 001, then the scheduling agreement should undergo an approval.

Prerequisite

A purchase requisition (document type ‘RV – outline agreement requisition’) must exist.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Create Scheduling Agreement (ME31L) | The Create Scheduling Agreement: Initial Screen view is displayed. |  |
| 3 | Create Scheduling Agreement with reference to Purchase Requisition | Choose Reference to PReq from top to enter Purchase requisition number and Item number created in [Create Purchase Requisition](#unique_18) [page ] 23 step.Choose Continue | You will be prompted to make the entries as in step 4. |  |
| 4 | Enter Agreement Data | Enter the following values:Supplier: 33300007Agreement type: LPAgreement Date: todayPurchasing Organization: 3310Purchasing Group:001Plant:3310Storage Location: 331Band choose Enter twice.Note If the Item Overview is displayed in stead of the header data, then choose Header Details(F6). | The Create Scheduling Agreement Header Data view is displayed. |  |
| 5 | Enter Validity End Date | On the Create Scheduling Agreement Header Data view, enter the Validity end date, for example, today + 720 days.and choose Enter. | The Create Scheduling Agreement Item overview view is displayed. |  |
| 6 | Adopt item details from Purchase Requisition | Choose Purchase Requisition and choose Adopt | The screen Create Scheduling Agreement: Selection list : Purchase Requisitions is displayedPurchase Requisition item details are adopted on item overview screen of Scheduling Agreement. |  |
| 7 | Check Tax Related Details | Choose More -> Item Details, maintain the following information:Tax Code: the default value from info record, for example, I1Tax Date: Default today | Note If the RITA is activated and tax registration countries is maintained for company code in Finance SSCUI 103464 (Activate RITA and maintain tax registration countries), then the Tax Country can be taken, or you can also choose different Tax Country value from the list. |  |
| 8 | Save | Choose Save at the bottom of the view.Make a note of the scheduling agreement number. | A scheduling agreement is created. |  |

#### Approve Scheduling Agreement (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you release a Scheduling Agreement. If the document type of scheduling agreement is LP and the purchase group is 001, then the scheduling agreement should undergo approval, provided flexible workflow is enabled for Scheduling Agreement as in Preliminary Steps as part of Prerequisites.

Prerequisite

A Scheduling Agreement must exist for release.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Purchasing Manager. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Approve Scheduling Agreement | Open My Inbox - All Items (F0862). | A list of already created Scheduling Agreements is displayed. |  |
| 3 | Search for Scheduling Agreement Sta tus | Enter the Scheduling Agreement number in the search area, then choose Search. | The Scheduling Agreements without follow-on documents (w/o status Follow-On Documents) have the status In Approval. |  |
| 4 | Release Scheduling Agreement | Select the Scheduling Agreement in left of the screen and choose Release in bottom right. | The Submit Decision screen is displayed. |  |
| 5 | Enter Release Reason | Enter the approval reason if needed, then choose Submit. | The Scheduling Agreement is approved. |  |
| 6 | Back to SAP Fiori Launchpad | Choose Home to go back to the SAP Fiori Launchpad. | The SAP Fiori Launchpad is displayed. |  |

#### Generate Delivery Schedule from MRP run (Optional)

##### Create Planned Independent Requirements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Planned independent requirements are used to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split over time according to dates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). |  |  |
| 3 | Check Default Area of Responsibility | Choose the User icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE(3310)MRP Controller 001(001）Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries.You can refer to BJ5 - Make-to-Stock Production – Discrete Manufacturing for this update.Plant 1 AE(3310)001 (MRP Controller 001) |  |  |
| 4 | Select Material | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Monthly (M)Version Active: Select allSearch: SG26Note Please make sure you have the same setting in material master data MRP 3 view for Period Indicator. If no, please refer to master data script BNS - Create Product Master of type "Semi-Finished Good" - MDS for adaption. |  |  |
| 5 | Filter Result | Choose Go to execute. | The material item is displayed. |  |
| 6 | Select Material Item | Select the material item, and choose Edit on the upper right part of the screen. |  |  |
| 7 | Edit PIRs | On the Edit PIRs screen, enter quantities per period, for example:PIR: 100 for all 12 periodsVersion is Active: YES |  |  |
| 8 | Save PIRs | Choose Save in the lower right corner. | The PIRs are saved. |  |

##### Schedule MRP Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The aim of material requirements planning is to tailor available capacities and receipts on time to suit requirements quantities. You can use MRP or consumption-based planning for this purpose. Single-item multilevel requirement planning is performed for plant 3310.

Prerequisite

The semi product is planned at plant level. There is now a requirement for the material SG26 in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirement Planning (MRP)Job Name: <MRP for SG26>Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.For 3 Parameters section:Plant: 3310Material: SG26Changed BOM Components: selectPlanning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for SG26 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

##### Evaluate Stock Requirement Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The requirement planning has generated schedule lines in the scheduling agreement for material SG26. In this procedure you want to monitor the material coverage situation.

Prerequisite

Requirements planning has been carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as a Material Planner - External Procurement. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments screen is displayed. |  |
| 3 | Check Default Area of Responsibility | On the Monitor Material Coverage - Net / Individual Segments screen, select the user (on the top right corner).choose the user icon, and select App Settings.On MRP Settings screen, choose Area of Responsibility.On My Area of Responsibility screen, check if the entry with below criteria is assigned:Plant 1 AE 3310MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. |  |  |
| 4 | Check Default App Setting | On the Monitor Material Coverage - Net / Individual Segments screen, select the user (on the top right corner).On MRP Settings screen, check if the button of Manage Material Coverage (F0251A) is switched to on.Switch the buttone to ON if it is off.If the button is switched to ON, in following steps, the system will navigate you to Manage Material Coverage (F0251A).If the button is switched to OFF, in following steps, the system will navigate you to Manage Material Coverage (F0251).In this chapter, we describe the configuration steps after the toggle button is switched to ON. |  |  |
| 5 | Search for Material | On the Monitor Material Coverage – Net and Individual Segments screen, make the following entry and choose Go.Material: SG26 | The relevant material is displayed. |  |
| 6 | Select Material | Select the checkbox before the Materials Number, and then choose Manage Materials. | The Material screen and Material Details screen display. |  |
| 7 | Review Stock/Requirements List | Select the corresponding material on the left Material screen. | The detailed Stock/Requirements List for each material is displayed. |  |
| 8 | Open Quickview for MRP Element | On the Material Details screen, choose the SchLne XXXX in column MRP Element. | The SchLne XXX you clicked will display on the pop-up. |  |
| 9 | Open Scheduling Agreement | On the pop up screen SchLne XXX, choose Display Scheduling Agreement. | The Display Scheduling Agreement: Item Overview screen is displayed. |  |
| 10 | Display Delivery Schedule | Check the checkbox before the item number, and then More > Delivery Schedule . | The Display Scheduling Agreement: Delivery Schedule for Item XXX screen is displayed.The system displays the scheduled quantity and dates. |  |

#### Maintain Delivery Schedule

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to create the delivery schedule for the scheduling agreement if it has not been maintained while creating the scheduling agreement.

|  |
| --- |
| Note When you create scheduling agreement with item category Subcontracting, then a default schedule line with quantity 1 PCS is generated. This scenario is fulfilled only when you enter the mandatory fields, such as Plant, Item Category, Material, and Target Quantity. You can further edit or delete this schedule line and add more schedule lines for the item. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchase Scheduling Agreements (F2179) | The Manage Purchase Scheduling Agreements screen is displayed. |  |
| 3 | Find scheduling agreement number | Find the appropriate newly created scheduling agreement through the search criteria, such as: Supplier 33300007, Agreement Type LP Scheduling Agreement, Purchasing Organization 3310, then choose Go. Select one item from the search result. | The desired scheduling agreement appears on the list page of Manage Purchase Scheduling Agreements. |  |
| 4 | Select Scheduling Agreement | Navigate to the selected scheduling agreement by clicking on Cheveron (>) or by directly clicking on the Scheduling agreement number from the list page. | The Scheduling agreement header ob­ ject page appears in display mode. |  |
| 5 | Maintain Delivery Schedule | Choose Edit at the right upper corner on the Manage Scheduling Agreement Header Object page.On Items tab, choose the desired item for which delivery schedule needs to be maintained. | The Purchase Scheduling Agreement Item screen is displayed. |  |
| 6 | Maintain Delivery Schedule | Go to the Schedule Lines section on the Purchase Scheduling Agreement Item screen and choose Create. You will get into the Manage Purchase Scheduling Agreements screen to maintain the schedules for the item, make following entries:Date type: Day formatDelivery Date: Today's dateDelivery Time: 10:00:00Schedule Quantity: 10Choose Apply twice at the right bottom to add a schedule line. | You will be navigated back to Scheduling Agreement Header object page. |  |
| 7 | Save | Choose Save from the Scheduling Agreement Header object page | Scheduling agreement will get updated with schedule lines. |  |

#### Print Scheduling Agreement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to preview the scheduling agreement for the material/supplier combination for the new Scheduling agreement or for the one which is already present in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Com ment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori launchpad as a Purchaser. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the Fiori app | Open Manage Purchase Scheduling Agreements (F2179). | The Manage Purchase Scheduling Agreements screen is displayed. |  |
| 3 | Find scheduling agreement number | Find the appropriate scheduling agreement through the search criteria, such as: Supplier 33300007, Agreement Type Scheduling Agreement (LP), Purchase Organization 3310, then choose Go. Select one item from the search result. | The desired scheduling agreement appears on the list page of Manage Purchase Scheduling Agreements. |  |
| 4 | Select Scheduling Agreement | Navigate to the selected scheduling agreement by clicking on Cheveron (>) or by directly clicking on the Scheduling agreement number from the list page. | The Scheduling agreement header object page appears in display mode. |  |
| 5 | View the output form for scheduling agreement | Go to Output controls facet & view the output settings maintained for the scheduling agreement. Choose the PDF sign to view the output form of scheduling agreement.PDF sign or symbol would be inactive. If the Status is in Error, then you need to choose Retry to have PDC symbol or sign activated to view the Output PDF form. | PDF form for scheduling agreement shall open. |  |

#### Monitor Subcontracting Documents (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to monitor subcontracting documents with next delivery due dates with quantity. Also, track the delivery and shipping statuses (such as overdue, On time, Due today, and Completed).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Com ment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori launchpad as a Purchaser. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Monitor Subcontracting Documents (F3095). | The Monitor Subcontracting Documents screen is displayed. |  |
| 3 | Monitor subcontracting documents | Enter the following data:Subcontractor: 33300007Plant: 3310Document Type: Scheduling Agreement (LP) (from dropdown list)Choose GO.Note If the subcontractor field doesn't appear on the screen, select the field on Adapt Filter. | The List with Scheduling Agreement Items is displayed with Next Delivery Date and Next Delivery Quantity. |  |
| 4 | Monitor subcontracting documents | Choose View to check the Assembly Flow.Choose Close. | If you have multi-level subcontracting, the graph can be displayed here. |  |
| 5 | Manage Scheduling Agreement | Check the details of your subcontracting document by clicking the item. |  |  |

#### Create Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to create outbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Com ment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Inventory Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Subcontracting Cockpit (F2948). | The app name screen is displayed. |  |
| 3 | Subcontracting Cockpit | Enter the following data:Shipping Date: date range covering scheduling agreement due datesPlant: 3310Subcontractor: 33300007Choose Go |  |  |
| 4 | Subcontracting Cockpit | Expand the following groups of Components under Document Items:RAW13,PD,Subcontracting(RM13)RAW14,PD,Subcontracting(RM14)Find the line items with your Scheduling Agreement number. Select both lines and then choose Create Delivery |  |  |
| 5 | Creating Delivery for Sub contracting Scheduling Agreement Schedule line | Enter Storage Location and Shipping point for both lines:Storage Location: 331CShipping point: 3310Select both lines and then choose Create DeliveryNote down your delivery number. | Delivery 00XXXXXXXX has been saved.Outbound delivery is created |  |

#### Pick and Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to Pick and Post Goods Issue against the Outbound delivery created in earlier step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Shipping Specialist. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Pick Outbound Delivery (F0868). | The app name screen is displayed. |  |
| 3 | Pick Outbound Delivery | Enter the following data:Outbound Delivery: your deliveryChoose Enter. |  |  |
| 4 | Picking | In Picking Section under Delivery Items.Enter Picking quantity equal to the delivery quantity. Select both the items.Choose Save. | Picking status become Green |  |
| 5 | Post GI | GI Ready Tab appears.Select Actual GI Date.Choose Post GI. | Good Issue document is created.GI Posted; GI Number XXXXXXXX |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post the goods receipt for the material against the subcontracting Scheduling Agreement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Receipt for Purchasing Document (F0843). | The Goods Receipt screen is displayed. |  |
| 3 | Enter Purchase Order | Enter the scheduling agreement number and choose Enter. | The system displays the data for the goods receipt on the Goods Receipt screen. |  |
| 4 | Enter Delivery Note | Make the following entries:Delivery Note: <note number>Printing: Choose Individual slip from the dropdown list.Choose Enter. |  |  |
| 5 | Select Item | Select the items for which a goods receipt is to be posted.Enter the delivered quantity and check the storage location to be posted. | The Post button is activated. |  |
| 6 | Post | Choose Post. | The system displays the message 1 material document(s) posted: 5xxxxxxxxx 2xxx. |  |

#### Create Supplier Invoice

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
| 1 | Log onto Fiori Launchpad | Open the SAP Fiori launchpad with the Accounts Payable Accountantrole. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Create Supplier Invoice (F0859) . | The Create Supplier Invoices screen displays. |  |
| 3 | Enter General Data | On the Create Supplier Invoice screen, make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount : XXXCurrency: AEDInvoice Date: TodayPosting Date: TodayInvoice Party: 33300007Reference: xxx(reference invoice number from invoicing party) | The Create Supplier Invoices screen displays. |  |
| 4 | Enter Purchasing Document References | In Purchasing Document References area, make the following entries (use a Scheduling agreement you created previously):References Document Category: Purchase Order/ Scheduling AgreementPurchase Order/ Scheduling Agreement: xxx | The Purchase Order References screen displays. |  |
| 5 | Check the Invoice Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the Scheduling Agreement ). | The Purchase Order Item's table displays. |  |
| 6 | Check Tax code | In the section Tax check if there is tax code information and enter the tax amount.when the tax code value is greater than zero.If there is no tax, specify the tax code <Input Tax Code>. | In the Tax area, you should see the same tax codes as in the items. |  |
| 7 | Check the balance | Calculate the tax amount from the item amount multiplied by the tax value. Check the balance (difference between the calculated amount and the gross Amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 8 | Simulate Supplier Invoice and Check Messages | Choose Simulate.If there are no differences(or if the value is within the defined tolerance), a new screen Simulation appears. You can check the simulation results in Simulation Overview and Simulation Details area. | The supplier Invoice is complete to post. |  |
| 9 | Post Invoice | Choose Post. | The invoice is posted. The system displays the message:Documents have been created.Supplier invoice: xxxxxxxxxx/xxxxJournal entries: xxxxxxxxxx/xxxxDo you want to create a new supplier invoice? |  |

### Part 2: Scheduling Agreement for Subcontracting with Serial Number Management

#### Create Scheduling Agreement – Subcontracting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity is used to create scheduling agreement for material/supplier combination, for example, material SG27 and supplier 33300007, directly or without reference to any preceding purchasing document like purchase requisition, if it has not been maintained yet.

If scheduling agreement is already present in system, you can skip this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchase Scheduling Agreements (F2179). | The Manage Scheduling Agreements list page is displayed. |  |
| 3 | Create Scheduling Agreement | Select Create to create a new scheduling agreement. | The New Scheduling Agreement header view is displayed. |  |
| 4 | Enter Header Data | Create a new scheduling agreement with the following data:Agreement Type: Scheduling Agreement(LP)Supplier: 33300007Validity Start: Default TodayValidity End: MM/DD/YYYY e.g. today + 720 daysPurchasing Group: 001Purchasing Organization: 3310Company Code: 3310Target Value: 2000 AED |  |  |
| 5 | Add Items to Scheduling Agreement | From the New Purchase Scheduling Agreement view, choose the Items facet and select Create. | The New Scheduling Agreement Item view is displayed. |  |
| 6 | Enter Item data | On the Items view, make the following entries:Item Category: L (Subcontracting)Plant: 3310Storage Location:331BMaterial: SG27Net Order Price: Default Value from Info RecordConfirmation Control: 0004 (default value from info record)Target Quantity:100Tax Code: V1 (default value from info record)Tax Date: Default TodayNote Field Tax Date is only available for countries/regions whose Time-Dependent Taxes (TDT) is enabled.Note If the RITA is activated and tax registration countries is maintained for company code in Finance SSCUI 103464/ configuration activity (Activate RITA and maintain tax registration countries), then the tax country can be taken, or you can also choose different tax country value from the list.Choose Apply at the bottom of the view. |  |  |
| 7 | Save | Return to the New Purchase Scheduling Agreement view and choose Create at the bottom of the view.Make a note of the scheduling agreement number. | A scheduling agreement is created. |  |

#### Approve Scheduling Agreement (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you release a scheduling agreement. If the document type of scheduling agreement is LP and the purchase group is 001, then the scheduling agreement should undergo approval, provided flexible workflow is enabled for scheduling agreement as in Preliminary Steps as part of Prerequisites.

Prerequisite

A scheduling agreement must exist for release.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Purchasing Manager. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Approve Scheduling Agreement | Open My Inbox - All Items (F0862). | A list of already created scheduling agreements is displayed. |  |
| 3 | Search for Scheduling Agreement Status | Enter the scheduling agreement number in the search area, then choose Search. | The scheduling agreements without follow-on documents (w/o status Follow-On Documents) in status In Approval. |  |
| 4 | Release Scheduling Agreement | Select the scheduling agreement in left of the screen and choose Release in bottom right. | The Submit Decision screen is displayed. |  |
| 5 | Enter Release Reason | Enter the approval reason if needed, then choose Submit. | The scheduling agreement is approved. |  |
| 6 | Back to SAP Fiori Launchpad | Choose Home to go back to the SAP Fiori Launchpad. | The SAP Fiori Launchpad is displayed. |  |

#### Maintain Delivery Schedule

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to create the delivery schedule for the scheduling agreement if it has not been maintained while creating the scheduling agreement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchase Scheduling Agreements (F2179) | The Manage Purchase Scheduling Agreements screen is displayed. |  |
| 3 | Find Scheduling Agreement Number | Find the appropriate newly created scheduling agreement through the search criteria, such as: Supplier 33300007, Agreement Type LP Scheduling Agreement, Purchasing Organization 3310, then choose Go. Select one item from the search result. | The desired scheduling agreement appears on the list page of Manage Purchase Scheduling Agreements. |  |
| 4 | Select Scheduling Agreement | Navigate to the selected scheduling agreement by clicking on cheveron (>) or by directly clicking on the scheduling agreement number from the list page. | The scheduling agreement header object page appears in display mode. |  |
| 5 | Maintain Delivery Schedule | Choose Edit at the right upper corner on the manage scheduling agreement header object page.On Items tab, choose the desired item for which delivery schedule needs to be maintained. | The Purchase Scheduling Agreement Item screen is displayed. |  |
| 6 | Maintain Delivery Schedule | Go to the Schedule Lines section on the Purchase Scheduling Agreement Item screen and choose Create. You will get into the Manage Purchase Scheduling Agreements screen to maintain the schedules for the item, make following entries:Date type: Day formatDelivery Date: Today's dateDelivery Time: 10:00:00Schedule Quantity: 10Choose Apply twice at the right bottom to add a schedule line. | You will be directed back to scheduling agreement header object page. |  |
| 7 | Save | Choose Save from the scheduling agreement header object page. | Scheduling agreement will get updated with schedule lines. |  |

#### Create Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to create outbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Com ment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as an Inventory Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Subcontracting Cockpit (F2948). | The app name screen is displayed. |  |
| 3 | Subcontracting Cockpit | Enter the following data:Shipping Date: date range covering scheduling agreement due datesPlant: 3310Subcontractor: 33300007Choose Go |  |  |
| 4 | Subcontracting Cockpit | Expand the following groups of Components under Document Items:RAW33, PD, Subcontracting (RM33)RAW34, PD, Subcontracting(RM34)Find the line items with your scheduling agreement number. Select both lines and then choose Create Delivery. |  |  |
| 5 | Creating Delivery for Subcontracting Scheduling Agreement Schedule Line | Enter storage location and shipping point for both lines:Storage Location: 331CShipping point: 3310Select both lines and then choose Create Delivery.Note down your delivery number. | The message Delivery 00XXXXXXXX has been saved. pops up.Outbound delivery is created. |  |

#### Pick and Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to pick and post goods issue against the outbound delivery created in earlier step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Shipping Specialist. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Pick Outbound Delivery (F0868). | The app name screen is displayed. |  |
| 3 | Pick Outbound Delivery | Enter the following data:Outbound Delivery: your delivery number.Choose Enter. |  |  |
| 4 | Picking | In Picking section under Delivery Items.Enter picking quantity equal to the delivery quantity. | Picking status becomes green. |  |
| 5 | Create Serial Number | Select line item 10.Choose Serial Number Status.Choose Add Multiple.Click to select Serial Number or press SHIFT and click to select a range.Choose OK.Choose Apply.Note down the serial number you created. |  |  |
| 6 | Maintain Line Item 20 | Exceute the same steps mentioned above for line item 20. |  |  |
| 7 | Post Goods Issue | Choose Save.Select Actual GI Date.Choose Post GI. | Good issue document is created.The message GI Posted; GI Number XXXXXXXX pops up. |  |

#### Create Inbound Delivery

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
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Receiving Specialist. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Create Inbound Delivery (VL31N). | The app name screen is displayed. |  |
| 3 | Create Inbound Delivery | Enter the following data:Supplier: 33300007Purchase Order: XXX (Enter the scheduling agreement number created in previous step).Choose Enter. |  |  |
| 4 | Enter Serial Number | Select line item 10.Choose SC Components.In the dialog box Edit Components of New Delivery – Item 10, choose each of the following items:RAW33, PD, Subcontracting (RM33)RAW34, PD, Subcontracting(RM34)Choose Assign Serial Numbers.In the pop-up screen Maintain Serial Numbers, enter serial numbers manually, or choose Create Serial Number Automatically.Note The serial numbers in consumed components maybe are not the same ones specified in previous outbound delivery, but they are the ones of the serial numbers that's in subcontracting stock at the supplier, and the received ones for semifinished goods receipt from the supplier.Choose Continue (Enter).Repeat the above metioned steps for the second component.Choose Confirm. | Picking status becomes green. |  |
| 5 | Save Inbound Delivery | Choose Save.Note down the delivery number you created. | The message Inbound Delivery 18XXXXXXXX has saved. pops up. |  |

#### Post Goods Receipt for Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post the goods receipt for the inbound delivery against the subcontracting scheduling agreement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Receiving Specialist. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Change Inbound Delivery (VL32N). | The Change Inbound Delivery screen is displayed. |  |
| 3 | Enter Inbound Delivery | Enter the inbound delivery number and choose Enter. | The system displays the data for the goods receipt on the Inbound Delivery Change screen. |  |
| 4 | Check and Update Serial Numbers | Select line item 10.Follow the navigation path below: Menu > Extras > Serial Numbers .Choose Create Serial Number Automatically.Choose Continue.Choose SC Components.In the dialog box Edit Components - Delivery 18xxxxxxx – 10, choose each of the following items and click Serial Numbers to check and update serial numbers if needed.RAW33, PD, Subcontracting (RM33)RAW34, PD, Subcontracting(RM34)Choose Confirm. |  |  |
| 5 | Post Putaway Quantity | Select the item whose goods receipt is to be posted.Enter the putaway quantity and check the storage location to be posted.Choose Save. |  |  |
| 6 | Post Goods Receipt | Choose Post Goods Receipt. | The system displays the message 1 Goods receipt for inbound delivery 18xxxxxxx posted (material document 5xxxxxxxxx). |  |

#### Create Supplier Invoice

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
| 1 | Log onto Fiori Launchpad | Open the SAP Fiori launchpad with the Accounts Payable Accountant role. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Create Supplier Invoice (F0859) . | The Create Supplier Invoices screen displays. |  |
| 3 | Enter General Data | On the Create Supplier Invoice screen, make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount : XXXCurrency: AEDInvoice Date: TodayPosting Date: TodayInvoice Party: 33300007Reference: xxx(reference invoice number from invoicing party) | The Create Supplier Invoices screen displays. |  |
| 4 | Enter Purchasing Document References | In Purchasing Document References area, make the following entries by using a scheduling agreement you created previously:References Document Category: Purchase Order/ Scheduling AgreementPurchase Order/ Scheduling Agreement: xxx | The Purchase Order References screen displays. |  |
| 5 | Check the Invoice Items Data | Check the Amount, the Quantity, and the Tax Code. There may already be a tax code that was copied from the scheduling agreement. | The Purchase Order Item table displays. |  |
| 6 | Check Tax Code | In the section Tax check if there is tax code information and enter the tax amount.when the tax code value is greater than zero.If there is no tax, specify the tax code <Input Tax Code>. | In the Tax area, you should see the same tax codes as in the items. |  |
| 7 | Check the Balance | Calculate the tax amount from the item amount multiplied by the tax value. Check the balance (difference between the calculated amount and the gross Amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 8 | Simulate Supplier Invoice and Check Messages | Choose Simulate.If there are no differences(or if the value is within the defined tolerance), a new screen Simulation appears. You can check the simulation results in Simulation Overview and Simulation Details area. | The supplier invoice is complete to post. |  |
| 9 | Post Invoice | Choose Post. | The invoice is posted. The system displays the message:Documents have been created.Supplier invoice: xxxxxxxxxx/xxxxJournal entries: xxxxxxxxxx/xxxxDo you want to create a new supplier invoice? |  |

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
> Flagged while digesting this document, not verified: Overview Table lists Part 1 Create Supplier Invoice as 'Create Supplier Invoice - Advanced (MIRO)', but the test procedure uses Create Supplier Invoice (F0859).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Overview Table assigns Evaluate Stock Requirement Situation to app Manage Material Coverage - New Version (F0251A), but the procedure opens Monitor Material Coverage - Net / Individual Segments (F2101A) and then navigates to F0251A or F0251 depending on a toggle.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Overview Table gives the Production Planner role for Print Scheduling Agreement, but the procedure logs on as Purchaser.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/master-data-script-create-scheduling-agreement-mds-bf6-557]]
- related-to :: [[10-procurement/mds-bf6-559]]
- related-to :: [[10-procurement/mds-bf6-561]]
- related-to :: [[10-procurement/scheduling-agreements-in-procurement-bmr-ae-test-script-sap-s-4hana-cl]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2NX_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 83,994 chars in the whole document
